---
title: Comment utiliser des bibliothèques JavaScript dans les applications Angular
  2+
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-12T09:57:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-javascript-libraries-in-angular-2-apps
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/1_FDIQCYA3BNp9Ek-tqGeQjA-1--1.png
tags:
- name: Angular
  slug: angular
- name: angular2
  slug: angular2
- name: angular6
  slug: angular6
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser des bibliothèques JavaScript dans les applications Angular
  2+
seo_desc: "By Mohammad Kermani\nDo you remember when you were learning AngularJS (version\
  \ 1), and tutorials kept telling you that you don’t need to add JQuery into your\
  \ project? \nThat hasn't changed - you don’t need to add JQuery to your Angular\
  \ 2+ project. But ..."
---

Par Mohammad Kermani

_Vous souvenez-vous lorsque vous appreniez AngularJS (version 1), et que les tutoriels vous disaient constamment que vous n'aviez pas besoin d'ajouter JQuery à votre projet ?_

Cela n'a pas changé - vous n'avez pas besoin d'ajouter JQuery à votre projet Angular 2+. Mais si, pour une raison quelconque, vous devez utiliser certaines bibliothèques JavaScript, vous devez savoir comment les utiliser dans Angular. Alors, commençons depuis zéro.

_Je vais ajouter_ [_underscore.js_](http://underscorejs.org/) _à un projet et vous montrer comment cela fonctionne._

### 1. Créer un nouveau projet en utilisant Angular CLI

Si vous n'avez pas déjà CLI installé sur votre machine, [installez-le](https://cli.angular.io/). Après l'installation, créez un nouveau projet (si vous n'en avez pas déjà un).

ng new learning

Vous aurez maintenant un nouveau projet Angular nommé "**learning**".

### 2. Installer le package dans votre projet

Allez dans le projet que nous venons de créer :

cd learning

Utilisez votre gestionnaire de packages préféré pour installer la bibliothèque que vous allez utiliser ; j'utilise `npm` pour installer `underscore.js`.

npm install --save underscore

### 3. Importer la bibliothèque dans Angular (TypeScript)

Nous écrivons du code en TypeScript, et nous devons suivre ses règles. TypeScript doit comprendre `underscore.js`.

Comme vous le savez peut-être, TypeScript est un sur-ensemble typé de JavaScript qui compile en JavaScript standard. TypeScript a sa propre syntaxe, les fonctions et les variables peuvent avoir des types définis. Mais lorsque nous allons utiliser une bibliothèque externe comme underscore, nous devons déclarer des définitions de types pour TypeScript.

En JavaScript, le type des arguments n'est pas important et vous n'obtiendrez pas d'erreur pendant que vous écrivez du code. Mais TypeScript ne vous permettra pas de donner un tableau à une fonction qui accepte une chaîne de caractères en entrée. Alors voici la question : devons-nous réécrire `underscore.js` en TypeScript et définir les types là-bas ?

Bien sûr que non - TypeScript fournit des fichiers de déclaration _(*.d.ts)_ qui définissent les types et standardisent un fichier/bibliothèque JavaScript pour TypeScript.

Certaines bibliothèques incluent un fichier de typage et vous n'avez pas besoin d'installer la destination de type TypeScript pour elles. Mais dans le cas où une bibliothèque n'a pas de fichier `.d.ts`, vous devez l'installer.

Nous devons simplement trouver et importer le fichier de définition de type `underscore.js`. Je vous suggère d'utiliser [Type Search](https://microsoft.github.io/TypeSearch/) pour trouver le fichier de déclaration pour les bibliothèques dont vous avez besoin.

Recherchez `underscore` dans [Type Search](https://microsoft.github.io/TypeSearch/) et il vous redirige vers [types/underscore](https://www.npmjs.com/package/@types/underscore). Installez le fichier de déclaration en utilisant la commande suivante :

`npm install --save @types/underscore`

### 4. Importer la déclaration de type dans l'application Angular

Supposons que vous allez utiliser underscore dans votre fichier `app.component.ts`. Ouvrez le fichier `app.component.ts` avec votre IDE et ajoutez le code suivant en haut du fichier :

```
import * as _ from 'underscore';
/* OU simplement :
import 'underscore';
*/
```

Le TypeScript dans ce composant comprend maintenant `_` et il fonctionne facilement comme prévu.

### Question : Comment utiliser une bibliothèque qui n'a pas de définition de type (*.d.ts) dans TypeScript et Angular ?

Créez-le si le fichier `src/typings.d.ts` n'existe pas. Sinon, ouvrez-le et ajoutez votre package :

```
declare var yourLibrary: any;
```

Dans votre TypeScript, vous devez maintenant l'importer avec le nom donné :

```
import * as yourPreferedName from 'yourLibrary';
yourPreferedName.method();
```

### Conclusion

Pour conclure, faisons un exemple simple pour voir un exemple fonctionnel de `_`. Ouvrez `app.component.ts` et, à l'intérieur de la classe `appComponent`, écrivez un `constructor` qui retourne le dernier élément d'un tableau en utilisant la fonction `_.last()` d'underscore :

```
...
import * as _ from 'underscore';
...
export class AppComponent {
  constructor() {
    const myArray: number[] = [9, 1, 5];
    const lastItem: number = _.last(myArray); // Utilisation d'underscore
    console.log(lastItem); // 5
  }
}
```

Si vous ouvrez votre application Angular maintenant, vous obtiendrez `5` dans la console, ce qui signifie que nous avons correctement ajouté `underscore` à notre projet et qu'il fonctionne comme prévu.

Vous pouvez ajouter n'importe quelle bibliothèque JavaScript à votre projet en suivant simplement les mêmes étapes.

---

Vous pouvez me suivre [ici](https://medium.com/@kermani) pour plus d'articles sur la technologie et la programmation.