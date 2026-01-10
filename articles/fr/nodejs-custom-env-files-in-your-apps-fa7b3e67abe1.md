---
title: Comment personnaliser les fichiers .env de Node.js pour différents environnements
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-05T14:11:53.000Z'
originalURL: https://freecodecamp.org/news/nodejs-custom-env-files-in-your-apps-fa7b3e67abe1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*s20L9h0d1TmrZGrxLZAZ7Q.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment personnaliser les fichiers .env de Node.js pour différents environnements
seo_desc: 'By Erisan Olasheni


  Have you ever found yourself in a situation where you needed custom environment
  variables for different development stages of your app? Here is a one-line solution.


  Development has been much easier since the invention of the .env...'
---

Par Erisan Olasheni

> **_Vous êtes-vous déjà retrouvé dans une situation où vous aviez besoin de variables d'environnement personnalisées pour différentes étapes de développement de votre application ? Voici une solution en une ligne._**

Le développement est devenu beaucoup plus facile depuis l'invention du fichier `.env`. Vous pouvez facilement définir vos variables d'environnement et leurs valeurs avec la syntaxe `ENV_VARIABLE=VALUE` et hop ! Ces variables sont chargées comme vos variables d'environnement, ce qui permet d'y accéder rapidement :

```bash
console.log(process.env.ENV_VARIABLE)
```

Au cas où vous vous demanderiez encore ce que tout cela signifie, vous êtes probablement nouveau dans l'utilisation du fichier `.env`. Il s'agit en fait d'un simple fichier de configuration texte utilisé pour définir certaines variables que vous souhaitez passer dans l'environnement de votre application.

Ce fichier a besoin d'un **parseur** pour fonctionner. Le parseur lit les définitions de variables **une par une** et les parse dans l'environnement. Il utilise le format **ENV_VARIABLE=VALUE** (dans le cas de Node.js : `process.env[ENV_VARIABLE]=VALUE`).

Bien sûr, ce n'est pas une fonctionnalité intégrée dans Node.js. Vous devez l'implémenter avec un module populaire appelé **dotenv**.

C'est une bonne solution de contournement, car elle a vraiment facilité le développement entre co-développeurs et au sein de la communauté de développement dans son ensemble. Personnellement, j'avais utilisé le module **dotenv**, jusqu'à ce que je sois bloqué en essayant de trouver une solution qui pourrait me permettre d'utiliser un fichier de configuration différent pour un environnement particulier. Ce serait encore plus cool...n'est-ce pas ? Oui ! Mais malheureusement, le module **dotenv** ne nous offre pas cette fonctionnalité.

**Alors, que faire ensuite ? Nous avons besoin de cette fonctionnalité pour faciliter le développement et les tests à travers différentes étapes de développement !**

### Que diriez-vous de fichiers .env personnalisés pour différentes étapes d'environnement ?

Ne pensez-vous pas que ce serait une bonne solution ? Définir des variables d'environnement personnalisées en créant simplement un fichier _.env.envname_ ? Cool ! C'est ce que **custom-env** est venu faire.

**Custom env est une bibliothèque conçue pour faciliter le développement en permettant plusieurs configurations .env pour différents environnements.** Cela est fait en chargeant les variables d'environnement à partir d'un fichier .env.envname dans l'objet `process.env` de node.

#### Installation

Il suffit de l'installer avec la commande suivante :

```bash
npm i custom-env
```

#### Utilisation

```bash
require('custom-env').env()
```

Par défaut, _custom-env_ utilise le fichier .env pour votre environnement de développement. Cependant, pour personnaliser pour une autre étape, ajoutez le nom comme suffixe comme dans _.env.envname._

**Exemple**

Nous pouvons définir une variable d'environnement personnalisée pour un **développement de staging.**

* Créez un fichier .env.staging
* Définissez vos variables

```bash
APP_ENV=staging
APP_NAME=custom environment app
DB_HOST=localhost
DB_USER=user
DB_PASS=pass
```

* Accédez à vos variables

```js
// Require custom-env et définissez votre fichier env préféré

require ('custom-env').env('staging')

console.log(process.env.APP_ENV)

console.log(process.env.APP_NAME)

console.log(process.env.DB_HOST)

console.log(process.env.DB_PASS)
```

**Sortie attendue**

```bash
staging
custom environment app
localhost
user
pass
```

C'est tout, c'est assez facile. N'hésitez pas à définir plus de variables pour différentes étapes que vous pensez avoir, comme :

_.env.testing, .env.staging, .env.server1, .env.server2, .env.localhost_

### Définir pour l'environnement actuel

Vous pouvez dire à _custom-env_ d'utiliser une configuration qui correspond à votre étape de développement actuelle en passant **true** à la méthode `_env()`.

**Exemple**

**Fichier : index.js**

```js
// Passez true à env() pour qu'il utilise l'étape de l'environnement actuel.

require('custom-env').env(true)

console.log(process.env.APP_NAME)
console.log(process.env.USERNAME)
console.log(process.env.PASSKEY)
```

Maintenant, définissons un fichier de configuration de staging :

**Fichier : .env.staging**

```bash
APP_NAME=Staging Node App
USER_NAME=John
PASSKEY=J*h*
```

Maintenant, servons node avec l'environnement de staging :

```bash
NODE_ENV=staging node index.js
```

**Sortie attendue**

![Image](https://cdn-media-1.freecodecamp.org/images/7tb8GikXlYKDDLXQoSaVwvOKfAxsG9iOVcNz)
_Obtient les variables selon l'environnement **staging**._

**Et voilà !**

### Documentation complète

Pour la documentation complète de _custom-env_, visitez la page **npm** [https://www.npmjs.com/package/custom-env](https://www.npmjs.com/package/custom-env)

### Code source

Vous pouvez obtenir ou contribuer au code source de _custom-env_ à l'adresse [https://github.com/erisanolasheni/custom-env](https://github.com/erisanolasheni/custom-env)

**_Bon codage !_**