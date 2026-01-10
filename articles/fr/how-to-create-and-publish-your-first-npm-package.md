---
title: Comment créer et publier un package NPM – un guide étape par étape
subtitle: ''
author: Benjamin Semah
co_authors: []
series: null
date: '2023-02-01T21:36:23.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-and-publish-your-first-npm-package
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/npm-package-article-image.png
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
- name: node
  slug: node
- name: npm
  slug: npm
- name: Web Development
  slug: web-development
seo_title: Comment créer et publier un package NPM – un guide étape par étape
seo_desc: 'NPM is the largest software registry on the internet. There are over a
  million packages in the NPM Library.

  Developers publish packages on NPM to share their code with others. And organisations
  also use NPM to share code internally.

  In this article, ...'
---

NPM est le plus grand registre de logiciels sur Internet. Il y a plus d'un million de packages dans la bibliothèque NPM.

Les développeurs publient des packages sur NPM pour partager leur code avec d'autres. Et les organisations utilisent également NPM pour partager du code en interne.

Dans cet article, vous apprendrez comment créer un package. Et vous apprendrez également comment publier votre package sur NPM afin que d'autres puissent le télécharger et l'utiliser.

Commençons !

## Comment choisir un nom pour votre package NPM

La première chose que vous devez faire avant de créer votre package est de choisir un nom. Cela est important car votre package doit avoir un nom unique. Vous devez choisir un nom qui n'a pas encore été utilisé.

Lorsque vous décidez d'un nom, allez sur le [registre NPM](https://www.npmjs.com/) et effectuez une recherche. Assurez-vous qu'il n'y a pas de correspondance exacte avec le nom que vous avez choisi (ou une correspondance trop similaire).

Par exemple, s'il existe un package appelé `hellonpmpackage` et que vous décidez d'appeler le vôtre `hello-npm-package`, NPM générera une erreur lorsque vous tenterez de le publier.

Si un package avec le même nom que vous souhaitez utiliser existe déjà dans le registre NPM, vous avez alors deux options.

1. Vous pouvez choisir un nom différent.
   
2. Vous pouvez publier votre package en tant que package avec portée (voir la section « Publier des packages avec portée » ci-dessous).
   

## Comment créer un package NPM

Suivez les étapes ci-dessous pour créer votre package.

### 1. Installer Node

Si vous n'avez pas encore installé Node, vous devriez le faire. Vous pouvez visiter le site officiel pour [télécharger et installer Node.js](https://nodejs.org/en/download/). NPM est préinstallé avec Node.

### 2. Initialiser un dépôt Git

Créez un nouveau dossier de projet pour votre package et naviguez dans ce dossier. Ensuite, exécutez la commande suivante dans votre terminal :

```json
git init
```

Cela vous aidera à suivre les modifications que vous apportez à votre package. Assurez-vous également d'avoir une version distante de votre dépôt sur GitHub (ou votre service d'hébergement préféré).

### 3. Initialiser NPM dans votre projet

Pour ce faire, naviguez jusqu'au répertoire racine de votre projet et exécutez la commande suivante :

```json
npm init
```

Cette commande créera un fichier `package.json`. Vous recevrez des invites pour fournir les informations suivantes :

* `package-name` : Comme vous l'avez appris précédemment dans ce tutoriel, le nom de votre package doit être unique. Il doit également être en minuscules. Il peut inclure des traits d'union.
   
* `version` : La valeur initiale est 1.0.0. Vous mettez à jour le numéro lorsque vous mettez à jour votre package en utilisant la [version sémantique](https://www.freecodecamp.org/news/semantic-versioning-1fd6f57749f7/).
   
* `description` : Vous pouvez fournir une description de votre package ici. Indiquez ce que fait votre package et comment l'utiliser.
   
* `entry point` : Le fichier d'entrée pour votre code. La valeur par défaut est `index.js`.
   
* `test command` : Ici, vous pouvez ajouter la commande que vous souhaitez exécuter lorsque l'utilisateur exécute `npm run test`.
   
* `git repository` : Le lien vers votre dépôt distant sur GitHub.
   
* `keywords` : Ajoutez des mots-clés pertinents qui aideront les autres à trouver votre package sur le registre NPM.
   
* `author` : Ajoutez votre nom.
   
* `license` : Vous pouvez ajouter une licence ou utiliser la licence par défaut (Internet Systems Consortium (ISC) License).
   

Voir la capture d'écran ci-dessous pour un exemple de la manière de répondre aux questions de l'invite :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/npm-image1.PNG align="left")

*Création d'un fichier package.json*

*Note : J'ai laissé la* `test command` *vide car il n'y a pas de commande de test pour le package dans ce tutoriel.*

### 4. Ajoutez votre code

Maintenant, vous pouvez ajouter le code pour votre package.

Tout d'abord, vous devez créer le fichier qui sera chargé lorsque votre module sera requis par une autre application. Pour ce tutoriel, ce sera le fichier `index.js`.

À l'intérieur du fichier `index.js`, ajoutez le code pour votre package.

Pour ce tutoriel, je vais créer un package simple appelé `first-hello-npm`. Ce package retourne la chaîne de caractères `"Hello NPM!"`.

```javascript
//index.js

function helloNpm() {
  return "hello NPM"
}

module.exports = helloNpm
```

Après avoir créé votre fonction, vous devez l'exporter comme dans l'exemple ci-dessus. Ainsi, toute personne qui télécharge votre package peut le charger et l'utiliser dans son code.

Si vous avez suivi jusqu'ici, vous devriez maintenant avoir votre package créé. Mais avant de le publier, vous devez tester votre package. Tester votre package réduit les chances de publier des bugs dans le registre NPM.

## Comment tester votre package NPM

Les tests garantissent que votre package NPM fonctionne comme prévu. Il existe de nombreuses façons de tester votre package. Dans ce tutoriel, vous apprendrez l'une des méthodes les plus simples pour tester.

Tout d'abord, naviguez jusqu'à la racine de votre projet de `package`. Ensuite, exécutez la commande suivante :

```json
npm link
```

Cela rendra votre package disponible globalement. Et vous pourrez requérir le package dans un projet différent pour le tester.

Créez un dossier `test`. Et à l'intérieur de ce dossier de test, ajoutez un fichier `script.js`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/npm-image2.PNG align="left")

*Exemple d'un dossier de test avec un fichier script.js*

Dans l'exemple ci-dessus, le dossier de test ne contient que le fichier `script.js`. Il ne contient pas encore le package. Pour ajouter le package que vous avez créé à votre dossier de test, exécutez la commande suivante :

```json
npm link <nom-du-package>
```

Dans le cas du dossier de test pour ce tutoriel, j'exécuterai la commande suivante :

```json
npm link first-hello-npm
```

Cela créera un dossier `node-modules`. Et il ajoutera tous les fichiers et dossiers de votre package – voir la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/npm-image3.PNG align="left")

Dans le fichier `script.js`, vous pouvez maintenant requérir votre package et l'utiliser pour le test.

```javascript
// test/script.js

const helloNpm = require('first-hello-npm')

console.log(helloNpm())
```

Le package `first-hello-npm` est censé retourner la chaîne de caractères `"hello NPM!"`. Comme vous pouvez le voir sur la capture d'écran ci-dessous, le package fonctionne comme prévu lorsque j'exécute le script.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/npm-image4.PNG align="left")

*Résultat du test pour le package first-hello-npm*

Après avoir testé votre package et vous être assuré qu'il fonctionne comme prévu, vous pouvez maintenant le publier sur le registre NPM.

## Comment publier votre package NPM

Pour publier votre package sur le registre NPM, vous devez avoir un compte. Si vous n'avez pas de compte, visitez la [page d'inscription NPM](https://www.npmjs.com/signup) pour en créer un.

Après avoir créé le compte, ouvrez votre terminal et exécutez la commande suivante à la racine de votre package :

```json
npm login
```

Vous recevrez une invite pour entrer votre `nom d'utilisateur` et votre `mot de passe`. Si la connexion est réussie, vous devriez voir un message comme celui-ci :

`Connecté en tant que <votre-nom-dutilisateur> sur https://registry.npmjs.org/.`

Vous pouvez maintenant exécuter la commande suivante pour publier votre package sur le registre NPM :

```json
npm publish
```

Si tout se passe bien, vous devriez obtenir des résultats similaires à la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/npm-image7.png align="left")

*Notification indiquant que le package est publié avec succès.*

Si vous avez suivi jusqu'ici, alors félicitations ! Vous venez de publier votre premier package NPM.

Vous pouvez visiter le [site NPM](https://www.npmjs.com/) et effectuer une recherche pour votre package. Vous devriez voir votre package apparaître dans les résultats de recherche.

Par exemple, sur la capture d'écran ci-dessous, vous pouvez voir que le package `first-hello-npm` est maintenant disponible sur NPM.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/package-available.png align="left")

*Le package first-hello-npm est maintenant disponible sur NPM*

## Comment publier des packages NPM avec portée

Si un package existant a le même nom que vous souhaitez utiliser, la solution est de publier un package avec portée.

Lorsque vous publiez un package avec portée, vous avez la possibilité de le rendre public ou privé. S'il est privé, vous pouvez choisir avec qui vous souhaitez partager le package.

### Comment créer un package NPM avec portée

Pour créer un package avec portée, naviguez d'abord jusqu'à la racine du répertoire de votre package.

Ensuite, exécutez la commande `npm init` et passez votre `nom d'utilisateur` comme valeur au drapeau `scope` :

```json
npm init --scope=@votre-nom-dutilisateur
```

Répondez aux invites pour créer un fichier `package.json`. Pour le nom de votre package, le format doit être `@votre-nom-dutilisateur/nom-du-package`.

Par exemple `@benjaminsemah/first-hello-npm`.

Vous pouvez maintenant ajouter le code pour votre package et le tester. Le processus est le même que celui déjà expliqué ci-dessus.

Ensuite, pour publier votre package avec portée, exécutez la commande suivante dans votre terminal.

```json
npm publish --access public
```

Vous pouvez changer de `public` à `private` si vous ne souhaitez pas rendre le package disponible pour un usage public.

Vous devriez voir une réponse similaire à celle-ci.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/scoped-package-published.PNG align="left")

*Package avec portée publié avec succès.*

Félicitations si vous avez suivi jusqu'ici. Vous avez publié votre package avec portée. Vous devriez voir votre package avec portée sur NPM si vous le recherchez. Par exemple, dans la capture d'écran ci-dessous, vous pouvez voir le package avec portée que j'ai créé dans ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/scoped-package-available.png align="left")

*Package avec portée est maintenant disponible sur NPM*

## Conclusion

Les packages aident les développeurs à travailler plus rapidement. Et ils améliorent également la collaboration. Lorsque vous trouvez une manière plus intelligente de faire les choses, une façon de partager avec la communauté est de créer et de publier votre solution en tant que package.

Dans cet article, vous avez appris ce que sont les packages et pourquoi ils sont utiles. Vous avez également appris comment créer et publier des packages sur le registre NPM. La communauté des développeurs attend avec impatience tous les beaux packages que vous créerez et partagerez.

Merci d'avoir lu. Et bon codage !