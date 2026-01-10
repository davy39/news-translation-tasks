---
title: Impossible d'utiliser l'instruction import en dehors d'un module [Erreur React
  TypeScript résolue]
date: '2022-11-15T15:30:56.000Z'
author: Ihechikara Abba
authorURL: https://www.freecodecamp.org/news/author/Ihechikara/
originalURL: https://freecodecamp.org/news/cannot-use-import-statement-outside-a-module-react-typescript-error-solved
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/markus-spiske-iar-afB0QQw-unsplash.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: node js
  slug: node-js
- name: TypeScript
  slug: typescript
seo_desc: "When building a web application, you may encounter the SyntaxError: Cannot\
  \ use import statement outside a module error. \nThis error might be raised when\
  \ using either JavaScript or TypeScript in the back-end. So you could be working\
  \ on the client side..."
---


Lors de la création d'une application web, vous pouvez rencontrer l'erreur `SyntaxError: Cannot use import statement outside a module`.

<!-- more -->

Cette erreur peut être levée lors de l'utilisation de JavaScript ou TypeScript en back-end. Vous pourriez donc travailler sur le côté client avec React, Vue, etc., et tout de même rencontrer cette erreur.

Vous pouvez également rencontrer cette erreur en travaillant avec JavaScript côté client.

Dans cet article, vous apprendrez comment corriger l'erreur `SyntaxError: Cannot use import statement outside a module` lors de l'utilisation de TypeScript ou JavaScript avec [Node][1].

Vous apprendrez également comment corriger cette erreur lors d'un développement JavaScript côté client.

## Comment corriger l'erreur TypeScript `SyntaxError: Cannot use import statement outside a module`

Dans cette section, nous allons travailler avec un serveur Node basique utilisant Express.

Notez que si vous utilisez la version la plus récente de TypeScript pour votre application Node, le fichier **tsconfig.json** possède des règles par défaut qui empêchent la levée de l'erreur `SyntaxError: Cannot use import statement outside a module`.

Il est donc fort probable que vous ne rencontriez pas l'erreur `SyntaxError: Cannot use import statement outside a module` si vous :

-   Installez la dernière version de TypeScript et utilisez le fichier **tsconfig.json** par défaut généré lors de l'exécution de `tsc init`.
-   Configurez correctement TypeScript pour Node et installez les packages nécessaires.

Mais supposons que vous n'utilisiez pas les dernières configurations du fichier **tsconfig.json**.

Voici un serveur Express qui écoute sur le port 3000 et affiche "Hello World!" dans la console :

```
import express from "express"

const app = express()

app.listen("3000", (): void => {
    console.log("Hello World!")
    // SyntaxError: Cannot use import statement outside a module
})
```

Le code ci-dessus semble devoir s'exécuter parfaitement, mais l'erreur `SyntaxError: Cannot use import statement outside a module` est levée.

Cela se produit parce que nous avons utilisé le mot-clé `import` pour importer un module : `import express from "express"`.

Pour corriger cela, rendez-vous dans le fichier **tsconfig.json** et faites défiler jusqu'à la section des modules.

Vous devriez voir une règle particulière comme celle-ci dans la section des modules :

```
/* Modules */
"module": "esnext"
```

Pour résoudre le problème, remplacez la valeur "esnext" par "commonjs".

C'est-à-dire :

```
/* Modules */
"module": "commonjs"
```

## Comment corriger l'erreur JavaScript `SyntaxError: Cannot use import statement outside a module`

La correction de l'erreur `SyntaxError: Cannot use import statement outside a module` lors de l'utilisation de JS natif est un peu différente de celle de TypeScript.

Voici notre serveur :

```
import express from "express";

const app = express();

app.listen(3000, () => {
    console.log("Hello World!");
    // SyntaxError: Cannot use import statement outside a module
});
```

Nous obtenons l'erreur `SyntaxError: Cannot use import statement outside a module` pour la même raison — nous avons utilisé le mot-clé `import` pour importer un module.

Pour corriger cela, allez dans le fichier **package.json** et ajoutez `"type": "module",`. Soit :

```
{
  "name": "js",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "type": "module",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

Maintenant, vous pouvez utiliser le mot-clé `import` sans obtenir d'erreur.

Pour corriger cette erreur lors d'un développement JavaScript côté client (sans framework), ajoutez simplement l'attribut `type="module"` à la balise script du fichier que vous souhaitez importer en tant que module. C'est-à-dire :

```
<script type="module" src="./add.js"></script>
```

## Résumé

Dans cet article, nous avons abordé l'erreur `SyntaxError: Cannot use import statement outside a module` en TypeScript et JavaScript.

Cette erreur se produit principalement lorsque vous utilisez le mot-clé `import` pour importer un module dans Node.js, ou lorsque vous oubliez l'attribut `type="module"` dans une balise `script`.

Nous avons vu des exemples de code qui génèrent l'erreur et comment les corriger en travaillant avec TypeScript et JavaScript.

Bon codage !

[1]: https://www.freecodecamp.org/news/node-js-server-side-javascript-what-is-node-used-for/