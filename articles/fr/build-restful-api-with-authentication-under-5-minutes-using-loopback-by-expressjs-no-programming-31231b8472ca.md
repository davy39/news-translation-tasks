---
title: Comment créer une API RESTful avec authentification en 5 minutes — tout depuis
  votre ligne de commande (Partie 1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-27T10:24:38.000Z'
originalURL: https://freecodecamp.org/news/build-restful-api-with-authentication-under-5-minutes-using-loopback-by-expressjs-no-programming-31231b8472ca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*r9V8K9siyS45bR95DLPQSA.gif
tags:
- name: api
  slug: api
- name: authentication
  slug: authentication
- name: Loopback
  slug: loopback
- name: Node.js
  slug: nodejs
- name: 'tech '
  slug: tech
seo_title: Comment créer une API RESTful avec authentification en 5 minutes — tout
  depuis votre ligne de commande (Partie 1)
seo_desc: 'By Niharika Singh

  If the title of this article excites you, then my friend, you’re about to achieve
  level 100 of satisfaction by the end. I’ll quickly go through the course of this
  article:


  What we are about to create: RESTful API which handles logs...'
---

Par Niharika Singh

Si le titre de cet article vous excite, alors mon ami, vous êtes sur le point d'atteindre le **niveau 100** de satisfaction à la fin. Je vais rapidement parcourir le contenu de cet article :

1. **Ce que nous allons créer :** une API RESTful qui gère les logs des articles alimentaires sur un menu de restaurant. La base de données utilisée en back-end sera MongoDB. (Vous pouvez littéralement utiliser n'importe quelle base de données sur cette planète. Il y a une liste exhaustive de connecteurs de base de données/non-base de données supportés par [LoopBack](https://loopback.io/) ci-dessous.)
2. **Qu'est-ce que LoopBack :** en termes extrêmement simples, il s'agit d'un framework Node.js open source et hautement extensible utilisé pour créer des APIs REST dynamiques et complètes très rapidement. Les APIs générées via LoopBack sont des APIs Swagger (le framework d'API le plus populaire au monde, et vous verrez pourquoi très bientôt). Le front-end pourrait être fait dans n'importe quel framework que vous aimez ; Angular ou React.
3. **Création d'application via CLI :** voici la partie WOW qui supprime toute la programmation impliquée. LoopBack CLI est si beau que toutes les heures de travail de développement sont réduites à quelques secondes. Ici, nous allons configurer notre base de données en utilisant CLI.
4. **Création de modèles de données via CLI :** encore une fois, pas de programmation. Tout via le beau CLI.
5. **Configuration de l'authentification via CLI :** si vous avez de l'expérience dans la création d'APIs, vous savez à quel point il est difficile de restreindre des parties de l'API en utilisant l'authentification. La configuration de l'authentification basée sur des tokens en utilisant Express+Node.js côté serveur est un casse-tête. Tout ce casse-tête sera éliminé en goûtant l'élixir de LoopBack ! C'est la boisson du paradis.

![Image](https://cdn-media-1.freecodecamp.org/images/iGHE28Ucn5MVvYyBssY3frS7FDU1HIUwo8AX)

#### Guide étape par étape :

**Pré-requis :** Assurez-vous d'avoir installé [Node.js](https://nodejs.org/en/), [Robomongo](https://robomongo.org/) et que le serveur MongoDB est en cours d'exécution.

#### **ÉTAPE 1 : Installer LoopBack CLI via NPM**

Ouvrez le terminal et écrivez la commande suivante pour installer LoopBack CLI afin que la commande 'lb' puisse être accessible. C'est uniquement via la commande 'lb' que nous pouvons générer des applications, des modèles, des sources de données, etc. Pour plus d'informations : [https://loopback.io/doc/en/lb2/Command-line-tools.html#using-yeoman](https://loopback.io/doc/en/lb2/Command-line-tools.html#using-yeoman)

```
$ npm install -g loopback-cli
```

Assurez-vous de l'installer globalement, sinon la commande 'lb' pourrait ne pas fonctionner pour vous.

#### **ÉTAPE 2 : Créer une application**

Créez un répertoire où vous souhaitez stocker votre projet. Je vais le nommer 'restaurant-menu'. Assurez-vous d'avoir ouvert ce répertoire dans votre terminal afin que tous les fichiers générés via LoopBack soient stockés dans ce dossier.

Ensuite, entrez la commande suivante :

```
$ lb
```

De nombreuses questions seront posées, comme celles affichées dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/R0sLAcXrQXqn-zeUSfj9thykmF9YwRcYKCNa)
_C'est à cela que cela devrait ressembler._

(Pour naviguer parmi les options, utilisez les touches fléchées de votre clavier)

### **L'API EST CRÉÉE !**

![Image](https://cdn-media-1.freecodecamp.org/images/rBQvFJ35WfSz3QdckTEmIqPc6KUZDzftWIBd)

Je ne plaisante pas. Vous ne me croyez pas ? Exécutez l'application en utilisant la commande suivante :

```
$ node .
```

![Image](https://cdn-media-1.freecodecamp.org/images/rAYYNopW-YM9SyR51w47dU6VI2lEsF1Rto1U)

Si vous pointez vers localhost:3000, vous verrez quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/yiv9xKmwl7OkCTdHmolz7o232lczz6KNBB6o)
_Cela vous indiquera uniquement quand l'API a été démarrée et depuis combien de secondes elle est en ligne._

Cependant, si vous allez sur localhost:3000/explorer, vous verrez la magnifique SwaggerAPI.

![Image](https://cdn-media-1.freecodecamp.org/images/nGKuHXxfQh-B85Ny9MIXh8GiXpyW7nSn6yCN)

LoopBack a configuré toutes les routes pour vous :

GET users, POST users, PUT users, DELETE users, Login, Log out, Change Password. Littéralement tout ! Cela prendrait autrement des heures de travail pour coder tout cela.

Ouvrez ce dossier dans n'importe quel éditeur de texte. J'utiliserai Atom.

#### **ÉTAPE 3 : Connexion à MongoDB**

Si vous ouvrez `**datasources.json**` dans le dossier Server, vous devriez voir quelque chose comme :

```json
{
  "db": {
    "name": "db",
    "connector": "memory"
  }
}

```

Cela signifie que présentement, la source de données utilisée est la mémoire de notre ordinateur. Nous devons changer cela pour Mongo. Alors installons le connecteur mongo :

```
$ npm install --save loopback-connector-mongodb
```

En parallèle, j'espère que mongod est en cours d'exécution. Voici comment vous saurez qu'il est en cours d'exécution :

```
2018-01-27T15:01:13.278+0530 I NETWORK  [thread1] waiting for connections on port 27017
```

Maintenant, connectons le connecteur !

```
$ lb datasource mongoDS --connector mongoDB
```

Cela posera beaucoup de questions comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/-satN8CMcb23tpBD1cmouXNwjbr4gLG9ArWj)

Maintenant, modifiez `**datasources.json**` car nous ne souhaitons pas utiliser la mémoire. Nous souhaitons utiliser Mongo.

```json
{
  "db": {
    "host": "localhost",
    "port": 27017,
    "url": "",
    "database": "food",
    "password": "",
    "name": "mongoDS",
    "user": "",
    "connector": "mongodb"
  }
}

```

Ainsi, notre base de données nommée : `**food**` est créée.

#### **ÉTAPE 4 : Création de modèles de données**

Exécutez la commande suivante pour créer des modèles de données :

```
$ lb model
```

![Image](https://cdn-media-1.freecodecamp.org/images/rhCkwWcP7f1SiI5ezMAvtdHhXU6eUllSB9pZ)

Vous pouvez ajouter autant de propriétés que vous le souhaitez à un modèle particulier. Pour arrêter d'entrer plus de propriétés, appuyez simplement sur Entrée pour sortir de la CLI.

Consultez `**dishes.json**` dans le dossier Common/Models.

```json
{
  "name": "dishes",
  "base": "PersistedModel",
  "idInjection": true,
  "options": { "validateUpsert": true },
  "properties": {
    "name": { "type": "string", "required": true },
    "price": { "type": "number", "required": true }
  },
  "validations": [],
  "relations": {},
  "acls": [],
  "methods": {}
}

```

Vous pouvez également modifier les propriétés à partir de ce fichier json. Il n'est pas nécessaire d'utiliser la CLI.

Maintenant, relançons le serveur en utilisant la commande suivante et dirigeons-nous vers localhost:3000/explorer

```
$ node .
```

Maintenant, vous verrez 2 modèles : `**dishes**`, et `**user**`

![Image](https://cdn-media-1.freecodecamp.org/images/yiCcXdhwh6KmkvQ65H6KHvjskh9pbc9JbXbr)

Maintenant, faisons un POST d'un `dish`.

![Image](https://cdn-media-1.freecodecamp.org/images/bncjurriEZN0SKiIdb7POrdOAocWlFjNAQHR)

Maintenant, faisons un GET du même `dish`.

![Image](https://cdn-media-1.freecodecamp.org/images/38k0M-rkWNr5-x1UDVtS0L7w9IDFWd0ucxlv)

Vous pouvez jouer avec d'autres requêtes HTTP également !

Ces APIs peuvent être accessibles en dehors de l'explorateur également :

[http://localhost:3000/api/dishes](http://localhost:3000/api/dishes)

![Image](https://cdn-media-1.freecodecamp.org/images/w-Hiil7wjDNHghvGoW488BgOsHwBzgVEDs2T)

#### **ÉTAPE 5 : AUTHENTIFICATION : La cerise sur le gâteau !**

Pour configurer l'authentification, exécutez la commande suivante :

```
$ lb acl
```

![Image](https://cdn-media-1.freecodecamp.org/images/bd94tNvvyNQzynur9S9CKyC-lSKoU8IKR2ye)

Maintenant, essayons de faire un GET des `**dishes**`. Avant cela, veuillez relancer le serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/BeN7OxZjcmu7EcRwPvf0PRab8HRavKLx3ya9)
_Ainsi, il ne GET aucun dish. Comme prévu. Parce que nous ne sommes pas connectés. Il nous alerte en disant Authentication required._

Authentifions-nous ! Pour cela, nous devons d'abord nous enregistrer. Alors nous faisons un POST dans `**users**`.

![Image](https://cdn-media-1.freecodecamp.org/images/IhYOhlb41zpLxsKOtVzX37Ji7dVriLKDv2Ln)

Maintenant, connectons-nous.

![Image](https://cdn-media-1.freecodecamp.org/images/hxCQm4xGEBEvevqPZtL6sgVN1mXoRV5tpj2u)

Maintenant, copiez l'ID dans le corps de la réponse et collez-le dans le champ Access Token en haut de la page.

![Image](https://cdn-media-1.freecodecamp.org/images/NY830CQpK2jD-BMJ0gvbDAadX1KOGyC8fh-r)

Maintenant, nous sommes authentifiés. YAY.

Maintenant, faisons un GET des `**dishes**` à nouveau.

![Image](https://cdn-media-1.freecodecamp.org/images/DhkE4UiURk9UHLXBvwWBLlM2PoWjeZuWc5dM)

HOORAY !

Félicitations si vous avez réussi à atteindre cette étape. Je suis si fier de vous.

Les prochaines étapes consisteraient à créer un front-end autour de cette API, ce qui sera fait plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/cJRJuth-oFUh34e3LYZXnP2dl75mFx3jHuPf)

#### Le tutoriel frontal de cet article peut être trouvé [ici](https://medium.freecodecamp.org/how-to-build-a-restful-api-with-authentication-in-5-minutes-all-from-your-command-line-part-2-dcf29d5de0bb). Dans ce tutoriel, j'ai utilisé ReactJS pour créer un front-end autour de cette API.

Au revoir les amis !

Bon codage.