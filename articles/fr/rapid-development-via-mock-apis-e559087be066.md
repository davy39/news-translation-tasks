---
title: Pas d'API ? Pas de problème ! Développement rapide via des API simulées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-16T13:41:52.000Z'
originalURL: https://freecodecamp.org/news/rapid-development-via-mock-apis-e559087be066
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Subl5K29BEplXnabKvek-A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Pas d'API ? Pas de problème ! Développement rapide via des API simulées
seo_desc: 'By Cory House

  Create a realistic mock API with Node.js in three quick steps

  In this era of service-oriented development, you need to get JSON to and from the
  server to make your front-end come alive. So an API is a necessity.

  But, great news: You don...'
---

Par Cory House

#### Créez une API simulée réaliste avec Node.js en trois étapes rapides

À l'ère du développement orienté services, vous devez envoyer et recevoir du JSON vers et depuis le serveur pour donner vie à votre front-end. Une API est donc une nécessité.

Mais bonne nouvelle : vous n'avez pas besoin de créer de vrais services web pour commencer. Il suffit de configurer une API simulée.

**Note :** Je dis API pour faire court. Les termes associés incluent Web API, service Web, API JSON et API RESTful.

#### Pourquoi une API simulée ?

Voici quatre raisons d'utiliser une API simulée :

1. **Pas encore d'API** — Peut-être que vous n'avez pas encore créé d'API. Une API simulée vous permet de commencer le développement sans attendre que l'équipe API construise les services dont vous avez besoin. Et si vous n'avez pas encore décidé comment concevoir vos services web, la simulation vous permet de prototyper rapidement différentes formes de réponse potentielles pour voir comment elles fonctionnent avec votre application.
2. **API lente ou peu fiable** — Les API existantes dans votre environnement de développement ou de QA sont-elles lentes, peu fiables ou coûteuses à appeler ? Si c'est le cas, une API simulée offre des réponses cohérentes et instantanées pour un développement rapide avec feedback. Et si vos services web existants tombent en panne, une API simulée vous permet de continuer à travailler.
3. **Éliminer les dépendances inter-équipes** — Une équipe séparée crée-t-elle les services web de votre application ? Une API simulée signifie que vous pouvez commencer à coder immédiatement et basculer vers les vrais services web lorsqu'ils sont prêts. Il suffit de s'accorder sur la conception proposée de l'API et de la simuler en conséquence.
4. **Travailler hors ligne** — Enfin, peut-être devez-vous travailler dans un avion, sur la route ou dans d'autres endroits où la connectivité est mauvaise. La simulation vous permet de travailler hors ligne car vos appels restent locaux.

### Créons une API simulée

La manière la plus simple que j'ai trouvée pour y parvenir utilise Node.js. Voici mon processus en trois étapes pour créer une API simulée réaliste :

1. Déclarer le schéma
2. Générer des données aléatoires
3. Servir des données aléatoires

Parcourons les trois étapes.

#### **Étape 1 — Déclarer le schéma**

Tout d'abord, déclarons le schéma pour notre API simulée en utilisant [JSON Schema Faker](https://github.com/json-schema-faker/json-schema-faker). Cela nous permettra de déclarer à quoi notre fausse API devrait ressembler. Nous déclarerons les objets et les propriétés qu'elle exposera, y compris les types de données. Il y a un [REPL en ligne pratique](http://json-schema-faker.js.org/) qui facilite l'apprentissage.

JSON Schema Faker prend en charge la génération de données aléatoires réalistes via trois bibliothèques open source : [Faker.js](https://github.com/marak/Faker.js/), [chance.js](http://chancejs.com/), et [randexp.js](https://fent.github.io/randexp.js/). Faker et Chance sont très similaires. Tous deux offrent une grande variété de fonctions pour générer des données aléatoires, y compris des noms, des adresses, des numéros de téléphone, des emails réalistes, et bien plus encore. Randexp crée des données aléatoires basées sur des expressions régulières. JSON Schema Faker nous permet d'utiliser Faker, Chance et Randexp dans nos définitions de schéma. Ainsi, vous pouvez déclarer exactement comment chaque propriété de votre API simulée doit être générée.

Voici un exemple de schéma pour générer des données utilisateur réalistes et aléatoires. J'enregistre ce fichier sous mockDataSchema.js :

```js
var schema = {
  "type": "object",
  "properties": {
    "users": {
      "type": "array",
      "minItems": 3,
      "maxItems": 5,
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number",
            "unique": true,
            "minimum": 1
          },
          "firstName": {
            "type": "string",
            "faker": "name.firstName"
          },
          "lastName": {
            "type": "string",
            "faker": "name.lastName"
          },
          "email": {
            "type": "string",
            "faker": "internet.email"
          }
        },
        "required": ["id", "type", "lastname", "email"]
      }
    }
  },
  "required": ["users"]
};

module.exports = schema;
```

Ce schéma utilise Faker.js pour générer un tableau d'utilisateurs avec des noms et des emails réalistes.

#### **Étape 2 — Générer des données aléatoires**

Une fois que nous avons défini notre schéma, il est temps de générer des données aléatoires. Pour automatiser les tâches de construction, je préfère utiliser les scripts npm plutôt que Gulp et Grunt. [Voici pourquoi](https://medium.freecodecamp.com/why-i-left-gulp-and-grunt-for-npm-scripts-3d6853dd22b8#.2cqrvlxhf).

Je crée un script npm dans package.json qui appelle un script Node séparé :

```json
"generate-mock-data": "node buildScripts/generateMockData"
```

Le script ci-dessus appelle un script Node appelé generateMockData. Voici ce qu'il y a dans generateMockData.js :

```js
/* Ce script génère des données simulées pour le développement local.
   Ainsi, vous n'avez pas à pointer vers une API réelle,
   mais vous pouvez profiter de données réalistes, mais aléatoires,
   et de chargements de page rapides grâce à des données locales et statiques.
 */

var jsf = require('json-schema-faker');
var mockDataSchema = require('./mockDataSchema');
var fs = require('fs');

var json = JSON.stringify(jsf(mockDataSchema));

fs.writeFile("./src/api/db.json", json, function (err) {
  if (err) {
    return console.log(err);
  } else {
    console.log("Données simulées générées.");
  }
});
```

J'appelle [json-schema-faker](https://www.npmjs.com/package/json-schema-faker) à la ligne 11, et je lui passe le schéma de données simulées que nous avons configuré à l'étape 1. Cela écrit finalement du JSON dans db.json, comme spécifié à la ligne 13 ci-dessus.

#### **Étape 3 — Servir des données aléatoires**

Maintenant que nous avons écrit des données aléatoires et réalistes dans db.json, servons-les ! [JSON Server](https://github.com/typicode/json-server) crée une API réaliste en utilisant le fichier JSON statique que nous avons créé. Pointons donc JSON Server vers le jeu de données simulé que nous avons généré dynamiquement à l'étape 2.

```json
"start-mockapi": "json-server --watch src/api/db.json --port 3001"
```

Cela démarre json-server et sert les données dans db.json sur le port 3001. Chaque objet de niveau supérieur est exposé sur un endpoint HTTP.

Voici la partie géniale : JSON Server simule une vraie base de données en sauvegardant les modifications dans le fichier db.json que nous avons créé à l'étape 2.

> **La beauté de JSON Server : il gère les créations, lectures, mises à jour et suppressions, donc cela semble totalement réel.**

**L'API simulée fonctionne exactement comme une vraie API, mais sans avoir à faire un vrai appel HTTP ou à mettre en place une vraie base de données !** Astucieux.

Cela signifie que nous pouvons faire du développement sans créer une vraie API d'abord. Nous devons simplement nous mettre d'accord sur les appels et la forme des données, puis l'équipe UI peut avancer sans avoir à attendre que l'équipe de service crée les services associés.

En résumé, pour que tout cela fonctionne, vous avez besoin de 3 lignes dans package.json :

```json
"generate-mock-data": "node buildScripts/generateMockData",
"prestart-mockapi": "npm run generate-mock-data",
"start-mockapi": "json-server --watch src/api/db.json --port 3001"
```

Le script start-mockapi exécute json-server et lui indique de surveiller le db.json que nous avons généré à l'étape 2. Avant que l'API simulée ne soit démarrée, les données simulées sont générées. Le script prestart-mockapi est appelé avant start-mockapi car il est préfixé par "pre". C'est la convention des scripts npm. Avec cette configuration, chaque fois que nous démarrons l'application, de nouvelles données simulées réalistes sont générées !

D'accord, nous sommes prêts à démarrer.

Tapez ceci :

```json
npm run start-mockapi
```

Et chargez ceci :

[http://localhost:3001/users](http://localhost:3001/users).

Vous devriez voir une liste d'utilisateurs retournée sous forme de JSON. Succès !

Pour voir comment tout cela s'assemble, [voici une démonstration fonctionnelle de cette configuration sur GitHub](https://github.com/coryhouse/mock-api-example).

De plus, mon nouveau cours "[Building a JavaScript Development Environment](https://app.pluralsight.com/library/courses/javascript-development-environment)" construit cela et bien plus à partir de zéro. ([essai gratuit](https://billing.pluralsight.com/individual/checkout))

![Image](https://cdn-media-1.freecodecamp.org/images/1*buNt_4s0mdYgZVU9ojz6Ew.png)

Enfin, envisagez [mocky.io](https://www.mocky.io) ou [fakejson.com](https://fakejson.com) pour des alternatives simples qui ne nécessitent aucune configuration.

#### La pointe de l'iceberg...

Cet article ne traite que d'une des plus de 40 décisions que vous devez prendre pour créer un nouvel environnement de développement JavaScript à partir de zéro :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zFePRtYWlugmbOxrzOYivQ.png)
_Déjà submergé ?_

Je passe en revue toutes ces décisions et construis un riche environnement de développement JavaScript à partir de zéro [ici](https://app.pluralsight.com/library/courses/javascript-development-environment/table-of-contents).

Générez-vous des API simulées aujourd'hui ? Avez-vous une configuration alternative à partager ? J'adorerais entendre parler de vos expériences dans les commentaires.

[Cory House](https://twitter.com/housecor) est l'auteur de [nombreux cours sur Pluralsight](http://pluralsight.com/author/cory-house), et consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com). Il est architecte logiciel chez VinSolutions, MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre.