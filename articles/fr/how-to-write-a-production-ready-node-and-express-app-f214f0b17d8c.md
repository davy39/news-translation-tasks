---
title: Comment écrire une application Node et Express prête pour la production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-08T21:07:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-a-production-ready-node-and-express-app-f214f0b17d8c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-1tLk1cFdmcEQfNhQ7LIUg.jpeg
tags:
- name: Express.js
  slug: expressjs
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment écrire une application Node et Express prête pour la production
seo_desc: 'By Shailesh Shekhawat

  Project Structuring

  When I started building Node & Express applications, I didn’t know how important
  it was to structure your application. Express doesn’t come with strict rules or
  guidelines for maintaining the project structur...'
---

Par Shailesh Shekhawat

### Structuration du projet

Lorsque j'ai commencé à construire des applications Node & Express, je ne savais pas à quel point il était important de structurer votre application. Express ne vient pas avec des règles ou des directives strictes pour maintenir la structure du projet.

Vous êtes libre d'utiliser n'importe quelle structure que vous voulez. Lorsque votre base de code grandit, vous finissez par avoir des gestionnaires de `route` longs. Cela rend votre code difficile à comprendre et il contient des bugs potentiels.

Si vous travaillez pour une startup, la plupart du temps vous n'aurez pas le temps de refactoriser votre projet ou de le modulariser. Vous pouvez vous retrouver dans une boucle sans fin de correction de bugs et de patchs.

<iframe src="https://giphy.com/embed/6csVEPEmHWhWg" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Avec le temps, en travaillant avec des petites et grandes équipes, j'ai réalisé quel type de structure peut grandir avec votre projet et rester facile à maintenir.

#### Modèle Vue Contrôleur

Le modèle [MVC](https://en.wikipedia.org/wiki/Model–view–controller) aide au développement rapide et parallèle. Par exemple, un développeur peut travailler sur la vue, tandis qu'un autre peut travailler sur la création de la logique métier dans le contrôleur.

Prenons un exemple d'une application simple de CRUD utilisateur.

```
project/
  controllers/
    users.js
  util/
    plugin.js
  middlewares/
    auth.js
  models/
    user.js
  routes/
    user.js
    router.js
  public/
    js/
    css/
    img/
  views/
    users/
      index.jade
  tests/
    users/
      create-user-test.js 
      update-user-test.js
      get-user-test.js
  .gitignore
  app.js
  package.json
```

* **controllers** : Définissez les gestionnaires de routes de votre application et la logique métier
* **util** : Écrivez des fonctions utilitaires/aides ici qui peuvent être utilisées par n'importe quel contrôleur. Par exemple, vous pouvez écrire une fonction comme `mergeTwoArrays(arr1, arr2)`.
* **middlewares** : Vous pouvez écrire des middlewares pour interpréter toutes les requêtes entrantes avant de passer au gestionnaire de route. Par exemple, 
 `router.post('/login', auth, controller.login)` où `auth` est une fonction middleware définie dans `middlewares/auth.js`.
* **models** : aussi une sorte de middleware entre votre contrôleur et la base de données. Vous pouvez définir un schéma et faire une validation avant d'écrire dans la base de données. Par exemple, vous pouvez utiliser un ORM comme [Mongoose](https://mongoosejs.com/) qui vient avec de grandes fonctionnalités et méthodes à utiliser dans le schéma lui-même
* **routes** : Définissez les routes de votre application, avec les méthodes HTTP. Par exemple, vous pouvez définir tout ce qui est lié à l'utilisateur.

```js
router.post('/users/create', controller.create)
router.put('/users/:userId', controller.update)
router.get('/users', controller.getAll)
```

* **public** : Stockez les images statiques dans `/img`, les fichiers JavaScript personnalisés et le CSS `/css`
* **views** : Contient les templates à rendre par le serveur.
* **tests** : Ici, vous pouvez écrire tous les tests unitaires ou les tests d'acceptation pour le serveur API.
* **app.js** : Agit comme le fichier principal du projet où vous initialisez l'application et les autres éléments du projet.
* **package.json** : Prend en charge les dépendances, les scripts à exécuter avec la commande `npm`, et la version de votre projet.

### **Gestion des exceptions et des erreurs**

Ceci est l'un des aspects les plus importants à considérer lors de la création de tout projet avec n'importe quel langage. Voyons comment gérer les erreurs et les exceptions de manière élégante dans une application Express.

#### **Utilisation des promesses**

L'un des avantages de l'utilisation des promesses par rapport aux callbacks est qu'elles peuvent gérer les exceptions/erreurs implicites ou explicites dans les blocs de code asynchrones ainsi que pour le code synchrone défini dans `.then()`, un callback de promesse

Il suffit d'ajouter `.catch(next)` à la fin de la chaîne de promesses. Par exemple :

```js
router.post('/create', (req, res, next) => {

   User.create(req.body)    // fonction pour stocker les données utilisateur dans la base de données
   .then(result => {
   
     // faire quelque chose avec le résultat
    
     return result 
   })
   .then(user => res.json(user))
   .catch(next)
})
```

#### **Utilisation de try-catch**

Try-catch est une méthode traditionnelle pour attraper les exceptions dans le code asynchrone.

Prenons un exemple avec une possibilité d'obtenir une exception :

```js
router.get('/search', (req, res) => {
 
  setImmediate(() => {
    const jsonStr = req.query.params
    try {
      const jsonObj = JSON.parse(jsonStr)
      
      res.send('Succès')
    } catch (e) {
      res.status(400).send('Chaîne JSON invalide')
    }
  })
})
```

#### **Éviter l'utilisation de code synchrone**

Le code synchrone, également connu sous le nom de code bloquant, car il bloque l'exécution jusqu'à ce qu'il soit exécuté.

Évitez donc d'utiliser des fonctions ou méthodes synchrones qui peuvent prendre des millisecondes ou des microsecondes. Pour un site web à fort trafic, cela s'accumulera et peut entraîner une latence élevée ou un temps de réponse des requêtes API.

Ne les utilisez pas en production, surtout :)

De nombreux modules Node.js viennent avec des méthodes `.sync` et `.async`, utilisez donc async en production.

Mais, si vous voulez toujours utiliser une API synchrone, utilisez le drapeau de ligne de commande `--trace-sync-io`. Il imprimera un avertissement et une trace de pile chaque fois que votre application utilise une API synchrone.

Pour plus d'informations sur les fondamentaux de la gestion des erreurs, voir :

* [Gestion des erreurs dans Node.js](https://www.joyent.com/developers/node/design/errors)
* [Construction d'applications Node robustes : Gestion des erreurs](https://strongloop.com/strongblog/robust-node-applications-error-handling/) (Blog StrongLoop)

> _Ce que vous ne devriez **pas** faire, c'est écouter l'événement `uncaughtException`, émis lorsqu'une exception remonte jusqu'à la boucle d'événements. Son utilisation est généralement [non préférée](https://nodejs.org/api/process.html#process_event_uncaughtexception)._

### **Journalisation correcte**

La journalisation est essentielle pour le débogage et l'activité de l'application. Elle est principalement utilisée à des fins de développement. Nous utilisons `console.log` et `console.error`, mais celles-ci sont des [fonctions synchrones](https://nodejs.org/api/console.html#console_console_1).

#### **À des fins de débogage**

Vous pouvez utiliser un module comme [debug](https://www.npmjs.com/package/debug). Ce module vous permet d'utiliser la variable d'environnement DEBUG pour contrôler quels messages de débogage sont envoyés à `console.err()`, le cas échéant.

#### **Pour l'activité de l'application**

Une façon est de les écrire dans la base de données.

Consultez [Comment j'ai utilisé les plugins mongoose pour auditer mon application](https://medium.freecodecamp.org/how-to-log-a-node-js-api-in-an-express-js-app-with-mongoose-plugins-efe32717b59).

Une autre façon est d'écrire dans un fichier **OU** d'utiliser une bibliothèque de journalisation comme [Winston](https://www.npmjs.com/package/winston) ou [Bunyan](https://www.npmjs.com/package/bunyan). Pour une comparaison détaillée de ces deux bibliothèques, voir l'article de blog StrongLoop [Comparaison de Winston et Bunyan pour la journalisation Node.js](https://strongloop.com/strongblog/compare-node-js-logging-winston-bunyan/).

### Le désordre de require("./../../../../../../")

Il existe différentes solutions de contournement pour ce problème.

Si vous trouvez un module qui devient populaire et s'il a une indépendance logique par rapport à l'application, vous pouvez le convertir en module npm privé et l'utiliser comme n'importe quel autre module dans package.json.

OU

```js
const path  = require('path');
const HOMEDIR  = path.join(__dirname,'..','..');
```

où `__dirname` est la variable intégrée qui nomme le répertoire qui contient le fichier actuel, et `..` ,`..` est le nombre requis de étapes vers le haut de l'arborescence des répertoires pour atteindre la racine du projet.

À partir de là, c'est simplement :

```js
const foo = require(path.join(HOMEDIR,'lib','foo'));
const bar = require(path.join(HOMEDIR,'lib','foo','bar'));
```

pour charger un fichier arbitraire dans le projet.

Faites-moi savoir dans les commentaires ci-dessous si vous avez de meilleures idées :)

### Définir NODE_ENV sur "production"

La variable d'environnement **NODE_ENV** spécifie l'environnement dans lequel une application est exécutée (généralement, développement ou production). L'une des choses les plus simples que vous pouvez faire pour améliorer les performances est de définir `**NODE_ENV**` sur "production".

Définir **NODE_ENV** sur "**production**" fait en sorte qu'Express :

* Met en cache les templates de vue.
* Met en cache les fichiers CSS générés à partir des extensions CSS.
* Génère des messages d'erreur moins verbeux.

[Les tests indiquent](http://apmblog.dynatrace.com/2015/07/22/the-drastic-effects-of-omitting-node_env-in-your-express-js-applications/) que simplement faire cela peut améliorer les performances de l'application d'un facteur de trois !

### **Utilisation d'un gestionnaire de processus**

Pour la production, vous ne devriez pas simplement utiliser `node app.j` — si votre application plante, elle sera hors ligne jusqu'à ce que vous la redémarriez.

Les gestionnaires de processus les plus populaires pour Node sont :

* [StrongLoop Process Manager](http://strong-pm.io/)
* [PM2](https://github.com/Unitech/pm2)
* [Forever](https://www.npmjs.com/package/forever)

Personnellement, j'utilise **PM2.**

Pour une comparaison fonction par fonction des trois gestionnaires de processus, voir [http://strong-pm.io/compare/](http://strong-pm.io/compare/). Pour une introduction plus détaillée aux trois, voir [Gestionnaires de processus pour les applications Express](https://expressjs.com/en/advanced/pm.html).

### Exécuter votre application dans un cluster

Dans un système multi-cœur, vous pouvez augmenter les performances d'une application Node de nombreuses fois en lançant un cluster de processus.

Un cluster exécute plusieurs instances de l'application, idéalement une instance sur chaque cœur de CPU. Cela distribue la charge et les tâches parmi les instances.

#### Utilisation du module cluster de Node

Le clustering est rendu possible avec le [module cluster](https://nodejs.org/dist/latest-v4.x/docs/api/cluster.html) de Node. Cela permet à un processus maître de générer des processus travailleurs. Il distribue les connexions entrantes parmi les travailleurs.

Cependant, plutôt que d'utiliser ce module directement, il est bien mieux d'utiliser l'un des nombreux outils disponibles qui le font pour vous automatiquement. Par exemple [node-pm](https://www.npmjs.com/package/node-pm) ou [cluster-service](https://www.npmjs.com/package/cluster-service).

#### Utilisation de PM2

Pour pm2, vous pouvez utiliser le cluster directement via une commande. Par exemple,

```js
# Démarrer 4 processus travailleurs
pm2 start app.js -i 4

# Détecter automatiquement le nombre de CPU disponibles et démarrer autant de processus travailleurs
pm2 start app.js -i max 
```

Si vous rencontrez des problèmes, n'hésitez pas à _[me contacter](https://101node.io) ou à commenter ci-dessous._ 
Je serais heureux de vous aider :)



_N'hésitez pas à applaudir si vous avez trouvé cela digne d'être lu !_

Références : [https://expressjs.com/en/advanced/best-practice-performance.html](https://expressjs.com/en/advanced/best-practice-performance.html)

_Publié à l'origine sur [101node.io](https://101node.io/blog/how-to-write-production-ready-node-express-app/) le 30 septembre 2018._