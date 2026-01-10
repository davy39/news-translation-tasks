---
title: Comment utiliser Redis pour booster vos APIs Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T03:50:58.000Z'
originalURL: https://freecodecamp.org/news/redis-caching-essentials-with-node-and-mongoose
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/adobe-spark-post--1--1.png
tags:
- name: api
  slug: api
- name: mongoose
  slug: mongoose
- name: node
  slug: node
- name: Redis
  slug: redis
seo_title: Comment utiliser Redis pour booster vos APIs Web
seo_desc: "By Tarique Ejaz\nPerformance is an essential parameter to consider when\
  \ you're designing any piece of software. It is particularly important when it comes\
  \ to what happens behind-the-scenes. \nWe, as developers and technologists, adopt\
  \ multiple tweaks a..."
---

Par Tarique Ejaz

La performance est un paramètre essentiel à considérer lors de la conception de tout logiciel. Elle est particulièrement importante en ce qui concerne ce qui se passe en coulisses. 

En tant que développeurs et technologues, nous adoptons de multiples ajustements et implémentations afin d'améliorer la performance. C'est là que le caching entre en jeu. 

> Le caching est défini comme un mécanisme de stockage de données ou de fichiers dans un emplacement de stockage temporaire d'où ils peuvent être instantanément accessibles chaque fois que nécessaire. 

Le caching est devenu une nécessité dans les applications web de nos jours. Nous pouvons utiliser Redis pour booster nos APIs web - qui sont construites en utilisant Node.js et MongoDB.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/redis.jpg)
_"Le caching jouerait apparemment encore un rôle super important dans 100 à 200 ans."_

## Redis : Aperçu pour les débutants 

[Redis](https://redis.io/), selon la documentation officielle, est défini comme un magasin de structures de données en mémoire qui est utilisé comme une base de données, un courtier de messages ou un stockage de cache. Il supporte des structures de données telles que les chaînes, les hachages, les listes, les ensembles, les ensembles triés avec des requêtes de plage, les bitmaps, les hyperloglogs, les index géospatiaux avec des requêtes de rayon et les flux. 

D'accord, c'est beaucoup de structures de données. Pour simplifier, presque toutes les structures de données supportées peuvent être condensées en une forme de chaîne ou une autre. Vous aurez plus de clarté à mesure que nous passerons par l'implémentation.

Mais une chose est claire. Redis est puissant, et lorsqu'il est utilisé correctement, il peut rendre nos applications non seulement plus rapides mais aussi incroyablement efficaces. Assez parlé. Mettons-nous au travail.

## Parlons code

Avant de commencer, vous devrez installer Redis sur votre système local. Vous pouvez suivre ce processus de [configuration rapide](https://redis.io/topics/quickstart) pour démarrer Redis. 

Terminé ? Super. Commençons. Nous avons une application simple créée en Express qui utilise une instance dans MongoDB Atlas pour lire et écrire des données.

Nous avons deux APIs principales créées dans le fichier de route `/blogs`.

```js
...

// GET - Récupère tous les articles de blog pour l'utilisateur requis
blogsRouter.route('/:user')
    .get(async (req, res, next) => {
        const blogs = await Blog.find({ user: req.params.user });

        res.status(200).json({
            blogs,
        });
    });

// POST - Crée un nouvel article de blog
blogsRouter.route('/')
    .post(async (req, res, next) => {
        const existingBlog = await Blog.findOne({ title: req.body.title });

        if (!existingBlog) {
            let newBlog = new Blog(req.body);

            const result = await newBlog.save();

            return res.status(200).json({
                message: `Blog ${result.id} est créé avec succès`,
                result,
            });
        }

        res.status(200).json({
            message: 'Un blog avec le même titre existe',
        });
    });
    
...
```

### Ajoutons un peu de Redis

Nous commençons par télécharger le package npm [`redis`](https://www.npmjs.com/package/redis) pour nous connecter au serveur Redis local. 

```js
const mongoose = require('mongoose');
const redis = require('redis');
const util = require('util');

const redisUrl = 'redis://127.0.0.1:6379';
const client = redis.createClient(redisUrl);
client.hget = util.promisify(client.hget);

...
```

Nous utilisons la fonction `utils.promisify` pour transformer la fonction `client.hget` afin qu'elle retourne une promesse au lieu d'un rappel. Vous pouvez en lire plus sur la `promisification` [ici](https://javascript.info/promisify).

La connexion Redis est en place. Avant d'écrire plus de code de caching, prenons un peu de recul et essayons de comprendre quelles sont les exigences que nous devons remplir et les défis probables auxquels nous pourrions être confrontés. 

Notre stratégie de caching doit être en mesure de répondre aux points suivants.

* Mettre en cache la requête pour tous les articles de blog d'un utilisateur particulier
* Effacer le cache chaque fois qu'un nouvel article de blog est créé

Les défis probables auxquels nous devons être attentifs lors de la mise en œuvre de notre stratégie sont :

* La bonne façon de gérer la création de clés pour stocker les données de cache
* La logique d'expiration du cache et l'expiration forcée pour maintenir la fraîcheur du cache
* L'implémentation réutilisable de la logique de caching

Très bien. Nous avons noté nos points et connecté Redis. Passons à l'étape suivante.

### Remplacement de la fonction Exec par défaut de Mongoose

Nous voulons que notre logique de caching soit réutilisable. Et non seulement réutilisable, nous voulons aussi qu'elle soit le premier point de contrôle avant de faire une requête à la base de données. Cela peut être facilement fait en utilisant un simple hack de piggy-backing sur la fonction exec de mongoose.

```js
...

const exec = mongoose.Query.prototype.exec;

...

mongoose.Query.prototype.exec = async function() {
	...

 	const result = await exec.apply(this, arguments);

    console.log('Source de données : Base de données');
    return result;
}

...
```

Nous utilisons l'objet prototype de mongoose pour ajouter notre code de logique de caching comme première exécution dans la requête.

### Ajout du Cache comme une Requête

Afin de désigner quelles requêtes doivent être mises en cache, nous créons une requête mongoose. Nous fournissons la capacité de passer l'`user` à utiliser comme clé de hachage via l'objet `options`. 

> **Note :** La clé de hachage sert d'identifiant pour une structure de données de hachage qui, en termes simples, peut être énoncée comme la clé parente d'un ensemble de paires clé-valeur. Ainsi, permettant la mise en cache d'un plus grand nombre d'ensemble de requêtes-valeurs. Vous pouvez en lire plus sur les hachages dans Redis [ici](https://redislabs.com/ebook/part-1-getting-started/chapter-1-getting-to-know-redis/1-2-what-redis-data-structures-look-like/1-2-4-hashes-in-redis/).

```js
...

mongoose.Query.prototype.cache = function(options = {}) {
    this.enableCache = true;
    this.hashKey = JSON.stringify(options.key || 'default');

    return this;
};

...
```

Ayant fait cela, nous pouvons facilement utiliser la requête `cache(<options argument>)` avec les requêtes que nous voulons mettre en cache de la manière suivante.

```js
...
    
const blogs = await Blog
                    .find({ user: req.params.user })
                    .cache({ key: req.params.user });
          
...
```

### Élaboration de la Logique de Cache

Nous avons mis en place une requête commune réutilisable pour désigner quelles requêtes doivent être mises en cache. Allons de l'avant et écrivons la logique centrale de caching.

```js
...

mongoose.Query.prototype.exec = async function() {
    if (!this.enableCache) {
        console.log('Source de données : Base de données');
        return exec.apply(this, arguments);
    }

    const key = JSON.stringify(Object.assign({}, this.getQuery(), {
        collection: this.mongooseCollection.name,
    }));

    const cachedValue = await client.hget(this.hashKey, key);

    if (cachedValue) {
        const parsedCache = JSON.parse(cachedValue);

        console.log('Source de données : Cache');

        return Array.isArray(parsedCache) 
                ?  parsedCache.map(doc => new this.model(doc)) 
                :  new this.model(parsedCache);
    }

    const result = await exec.apply(this, arguments);
    
    client.hmset(this.hashKey, key, JSON.stringify(result), 'EX', 300);

    console.log('Source de données : Base de données');
    return result;
};

...
```

Chaque fois que nous utilisons la requête `cache()` avec notre requête principale, nous définissons la clé `enableCache` sur true. 

Si la clé est false, nous retournons la requête principale `exec` par défaut. Sinon, nous formons d'abord la clé pour récupérer et stocker/rafraîchir les données de cache. 

Nous utilisons le nom de la `collection` avec la requête par défaut comme nom de clé pour le bien de l'unicité. La clé de hachage utilisée est le nom de l'`user` que nous avons déjà défini précédemment dans la définition de la fonction `cache()`. 

Les données mises en cache sont récupérées en utilisant la fonction `client.hget()` qui nécessite la clé de hachage et la clé consécutive comme paramètres. 

> **Note :** Nous utilisons toujours `JSON.parse()` lors de la récupération de données depuis Redis. Et de manière similaire, nous utilisons `JSON.stringify()` sur la clé et les données avant de stocker quoi que ce soit dans Redis. Cela est fait puisque Redis ne supporte pas les structures de données JSON.

Une fois que nous avons obtenu les données mises en cache, nous devons transformer chacun des objets mis en cache en un modèle mongoose. Cela peut être fait simplement en utilisant `new this.model(<object>)`. 

Si le cache ne contient pas les données requises, nous faisons une requête à la base de données. Ensuite, ayant retourné les données à l'API, nous rafraîchissons le cache en utilisant `client.hmset()`. Nous définissons également un temps d'expiration de cache par défaut de 300 secondes. Cela est personnalisable en fonction de votre stratégie de caching.

La logique de caching est en place. Nous avons également défini un temps d'expiration par défaut. Ensuite, nous examinons l'expiration forcée du cache chaque fois qu'un nouvel article de blog est créé.

### Expiration Forcée du Cache

Dans certains cas, comme lorsque l'utilisateur crée un nouvel article de blog, l'utilisateur s'attend à ce que le nouvel article soit disponible lorsqu'il récupère tous les articles. 

Pour ce faire, nous devons effacer le cache lié à cet utilisateur et le mettre à jour avec de nouvelles données. Nous devons donc forcer l'expiration. Nous pouvons le faire en invoquant la fonction `del()` fournie par Redis. 

```js
...

module.exports = {
    clearCache(hashKey) {
        console.log('Cache nettoyé');
        client.del(JSON.stringify(hashKey));
    }
}

...
```

Nous devons également garder à l'esprit que nous allons forcer l'expiration sur plusieurs routes. Une façon extensible est d'utiliser ce `clearCache()` comme un middleware et de l'appeler une fois qu'une requête liée à une route a terminé son exécution. 

```js
const { clearCache } = require('../services/cache');

module.exports = async (req, res, next) => {
    // attendre que le gestionnaire de route ait fini de s'exécuter
    await next(); 
    
    clearCache(req.body.user);
}

```

Ce middleware peut être facilement appelé sur une route particulière de la manière suivante.

```js
...

blogsRouter.route('/')
    .post(cleanCache, async (req, res, next) => {
    
    ...
    
    }
    
...
```

Et nous avons terminé. Je suis d'accord que c'était beaucoup de code. Mais avec cette dernière partie, nous avons configuré Redis avec notre application et pris en charge presque tous les défis probables. Il est temps de voir notre stratégie de caching en action.

## Redis en Action

Nous utilisons [Postman](https://www.postman.com/) comme client API pour voir notre stratégie de caching en action. C'est parti. Passons en revue les opérations de l'API, une par une.

1. Nous créons un nouvel article de blog en utilisant la route `/blogs`

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot--50-.png)
_Création d'un nouvel article de blog_

2. Nous récupérons ensuite tous les articles de blog liés à l'utilisateur `tejaz`

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot--51-.png)
_Récupération de tous les articles de blog pour l'utilisateur tejaz_

3. Nous récupérons une fois de plus tous les articles de blog pour l'utilisateur `tejaz`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot--52-.png)
_Récupération de tous les articles de blog pour l'utilisateur tejaz une fois de plus_

Vous pouvez clairement voir que lorsque nous récupérons depuis le cache, le temps pris est passé de **409ms** à **24ms**. Cela booste votre API en diminuant le temps pris de presque **95%.** 

De plus, nous pouvons clairement voir que l'expiration du cache et les opérations de mise à jour fonctionnent comme prévu.

Vous pouvez trouver le code source complet dans le dossier `redis-express` ici.

%[https://github.com/tarique93102/article-snippets/tree/master/redis-express]

## Conclusion

Le caching est une étape obligatoire pour toute application performante et intensive en données. Redis vous aide à atteindre facilement cet objectif dans vos applications web. C'est un outil super puissant, et s'il est utilisé correctement, il peut définitivement offrir une excellente expérience aux développeurs ainsi qu'aux utilisateurs du monde entier.

Vous pouvez trouver l'ensemble complet des commandes Redis [ici](https://redis.io/commands). Vous pouvez l'utiliser avec `redis-cli` pour surveiller vos données de cache et les processus de l'application. 

Les possibilités offertes par une technologie particulière sont vraiment sans fin. Si vous avez des questions, vous pouvez me contacter sur `[LinkedIn](https://www.linkedin.com/in/tarique-ejaz/)`. 

En attendant, continuez à coder.