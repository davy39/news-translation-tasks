---
title: Modules en JavaScript – CommonJS et ESmodules Expliqués
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-04-14T01:17:29.000Z'
originalURL: https://freecodecamp.org/news/modules-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/carson-arias-7Z03R1wOdmI-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
- name: modules
  slug: modules
seo_title: Modules en JavaScript – CommonJS et ESmodules Expliqués
seo_desc: 'Hi everyone! In this article we''re going to take a look at modules in
  JavaScript.

  Modules are a technique heavily used in today''s software design/architecture.

  First we''re going to learn what they are and the different types of modules that
  exist. Th...'
---

Bonjour à tous ! Dans cet article, nous allons examiner les modules en JavaScript.

Les modules sont une technique largement utilisée dans la conception/architecture logicielle d'aujourd'hui.

Tout d'abord, nous allons apprendre ce qu'ils sont et les différents types de modules qui existent. Ensuite, nous allons discuter de l'utilité des modules. Puis nous verrons des exemples et la syntaxe de base pour les types de modules les plus utilisés, et enfin nous discuterons du bundling, pourquoi il est nécessaire, et comment le faire.

Assez de bavardages, c'est parti ! =D

## Table des Matières

* [Qu'est-ce que les modules et pourquoi sont-ils utiles](#heading-quest-ce-que-les-modules-et-pourquoi-sont-ils-utiles)
    
* [Types de modules](#heading-types-de-modules)
    
    * [CommonJS](#heading-commonjs-modules)
        
    * [ESmodules](#heading-esmodules)
        
* [Utilisation des modules](#heading-utilisation-des-modules)
    
* [Bundling des modules](#heading-bundling-des-modules)
    
* [Résumé](#heading-resume)
    

# Qu'est-ce que les modules et pourquoi sont-ils utiles

Un module est simplement un morceau de code dans un fichier que vous pouvez appeler et utiliser depuis d'autres fichiers. Une conception modulaire est l'opposé d'avoir tout le code de votre projet dans un seul fichier.

Lors du développement d'un grand projet, il est très utile de diviser notre code en modules pour les raisons suivantes :

* C'est bon pour diviser les préoccupations et les fonctionnalités dans différents fichiers, ce qui aide à la visualisation et à l'organisation du code.
    
* Le code tend à être plus facile à maintenir et moins sujet aux erreurs et bugs lorsqu'il est clairement organisé.
    
* Les modules peuvent être facilement utilisés et réutilisés dans différents fichiers et parties de notre projet, sans avoir besoin de réécrire le même code.
    

Au lieu d'avoir tous les composants de notre programme dans un seul fichier, nous pouvons le diviser en parties ou modules, et rendre chacun d'eux responsable d'une seule fonctionnalité/préoccupation.

Si ce concept n'est pas encore assez clair, ne vous inquiétez pas. Nous verrons quelques exemples dans un instant.

# Types de modules

Comme pour presque tout dans la vie, et surtout en JavaScript, il existe de nombreuses façons d'implémenter des modules.

JavaScript ayant été créé à l'origine pour être simplement un petit langage de script pour les sites web, une fonctionnalité pour les grands projets comme les modules n'était pas supportée au début.

Mais à mesure que le langage et l'écosystème ont grandi, les développeurs ont commencé à voir le besoin de cette fonctionnalité. Et ainsi, différentes options et bibliothèques ont été développées pour ajouter cette fonctionnalité à JavaScript.

Parmi les nombreuses disponibles, nous allons seulement examiner CommonJS et ESmodules, qui sont les plus récents et les plus largement utilisés.

Commentaire de côté : Saviez-vous que [JavaScript a été créé à l'origine en seulement 10 jours de travail](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/) ?

Lors de l'analyse des complexités de JavaScript et de la compréhension de l'évolution du langage, je pense qu'il est important de garder à l'esprit que le langage n'a pas été créé à l'origine pour faire ce qu'il fait aujourd'hui. C'est la croissance de l'écosystème JavaScript qui a poussé à de nombreux changements qui ont eu lieu.

## Modules CommonJS

[CommonJS](https://en.wikipedia.org/wiki/CommonJS) est un ensemble de normes utilisées pour implémenter des modules en JavaScript. Le projet a été lancé par l'ingénieur Mozilla Kevin Dangoor en 2009.

CommonJS est principalement utilisé dans les applications JS côté serveur avec Node, car les navigateurs ne supportent pas l'utilisation de CommonJS.

En tant que commentaire de côté, Node n'utilisait que CommonJS pour implémenter des modules, mais aujourd'hui il supporte également ESmodules qui est une approche plus moderne.

Alors voyons à quoi ressemble CommonJS dans du code réel.

Pour implémenter des modules, vous avez besoin d'une application Node sur votre ordinateur. Créez-en une en exécutant `npm init -y`.

Tout d'abord, créons un fichier `main.js` avec une simple fonction dedans.

```plaintext
const testFunction = () => {
    console.log('Je suis la fonction principale')
}

testFunction()
```

D'accord, maintenant disons que nous voulons avoir une autre fonction appelée depuis notre fichier principal, mais nous ne voulons pas la fonction dedans car elle ne fait pas partie de notre fonctionnalité principale. Pour cela, créons un fichier `mod1.js` et ajoutons ce code :

```plaintext
const mod1Function = () => console.log('Mod1 est vivant !')
module.exports = mod1Function
```

`module.exports` est le mot-clé que nous utilisons pour déclarer tout ce que nous voulons exporter depuis ce fichier.

Pour utiliser cette fonction dans notre fichier `main.js`, nous pouvons le faire comme ceci :

```plaintext
mod1Function = require('./mod1.js')

const testFunction = () => {
    console.log('Je suis la fonction principale')
    mod1Function()
}

testFunction()
```

Voyez que nous déclarons ce que nous voulons utiliser et l'assignons ensuite au `require` du fichier que nous voulons utiliser. Facile comme bonjour. ;)

Si nous voulions exporter plus d'une chose depuis un seul module, nous pouvons le faire comme ceci :

```plaintext
const mod1Function = () => console.log('Mod1 est vivant !')
const mod1Function2 = () => console.log('Mod1 roule, bébé !')

module.exports = { mod1Function, mod1Function2 }
```

Et dans le fichier main.js, nous pouvons utiliser les deux fonctions comme ceci :

```plaintext
({ mod1Function, mod1Function2 } = require('./mod1.js'))

const testFunction = () => {
    console.log('Je suis la fonction principale')
    mod1Function()
    mod1Function2()
}

testFunction()
```

Et c'est à peu près tout. Assez simple, non ? C'est simple mais c'est un outil puissant à utiliser. =)

## ESmodules

Maintenant, passons en revue ESmodules. ESmodules est une norme qui a été introduite avec ES6 (2015). L'idée était de standardiser le fonctionnement des modules JS et d'implémenter ces fonctionnalités dans les navigateurs (qui ne supportaient pas auparavant les modules).

ESmodules est une approche plus moderne qui est actuellement supportée par les applications côté navigateur et côté serveur avec Node.

Voyons cela en code. Une fois de plus, nous commençons par créer une application Node avec `npm init -y`.

Maintenant, nous allons dans notre `package.json` et ajoutons `"type": "module"`, comme ceci :

```plaintext
{
  "name": "modulestestapp",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "module"
}
```

Si nous ne faisons pas cela et essayons d'implémenter ESmodules sur Node, nous obtiendrons une erreur comme ceci :

```plaintext
(node:29568) Warning: To load an ES module, set "type": "module" in the package.json or use the .mjs extension.
...
SyntaxError: Cannot use import statement outside a module
```

Maintenant, répétons exactement le même exemple. Dans notre fichier `main.js`, nous aurons le code suivant :

```plaintext
// main.js
import { mod1Function } from './mod1.js'

const testFunction = () => {
    console.log('Je suis la fonction principale')
    mod1Function()
}

testFunction()
```

Et dans `mod1.js`, nous aurons ceci :

```plaintext
// mod1.js
const mod1Function = () => console.log('Mod1 est vivant !')
export { mod1Function }
```

Remarquez qu'au lieu de `require`, nous utilisons `import` et au lieu de `module.exports`, nous utilisons `export`. La syntaxe est un peu différente mais le comportement est très similaire.

Encore une fois, si nous voulions exporter plus d'une chose depuis le même fichier, nous pourrions le faire comme ceci :

```plaintext
// main.js
import { mod1Function, mod1Function2 } from './mod1.js'

const testFunction = () => {
    console.log('Je suis la fonction principale')
    mod1Function()
    mod1Function2()
}

testFunction()
```

```plaintext
// mod1.js
const mod1Function = () => console.log('Mod1 est vivant !')
const mod1Function2 = () => console.log('Mod1 roule, bébé !')

export { mod1Function, mod1Function2 }
```

Une autre fonctionnalité disponible dans ESmodules est le renommage des imports, qui peut être fait comme ceci :

```plaintext
// main.js
import { mod1Function as funct1, mod1Function2 as funct2 } from './mod1.js'

const testFunction = () => {
    console.log('Je suis la fonction principale')
    funct1()
    funct2()
}

testFunction()
```

Remarquez que nous utilisons le mot-clé `as` après chaque fonction, puis nous la renommons comme nous le voulons. Plus tard dans notre code, nous pouvons utiliser ce nouveau nom au lieu du nom original de l'import. ;)

Une autre chose que vous pourriez faire est d'importer toutes les exports ensemble et de les mettre ensemble dans un objet, comme ceci :

```plaintext
// main.js
import * as mod1 from './mod1.js' 

const testFunction = () => {
    console.log('Je suis la fonction principale')
    mod1.mod1Function()
    mod1.mod1Function2()
}

testFunction()
```

Cela peut être utile dans les cas où, tout au long de notre code, nous voulons être explicites sur l'origine de chaque import. Voyez que les fonctions sont maintenant appelées comme `mod1.mod1Function()`.

La dernière chose à mentionner est le mot-clé `default`. Avec lui, nous pouvons définir une export par défaut pour un module donné. Comme ceci :

```plaintext
// mod1.js
const mod1Function = () => console.log('Mod1 est vivant !')
const mod1Function2 = () => console.log('Mod1 roule, bébé !')

export default mod1Function
export { mod1Function2 }
```

Et que signifie avoir une export par défaut ? Eh bien, cela signifie que nous n'avons pas à la déstructurer lorsque nous l'importons. Nous pouvons l'utiliser simplement comme ceci :

```plaintext
// main.js
import mod1Function, { mod1Function2 } from './mod1.js' 

const testFunction = () => {
    console.log('Je suis la fonction principale')
    mod1Function()
    mod1Function2()
}

testFunction()
```

Nous pouvons même renommer l'import comme nous le voulons sans le mot-clé `as`, puisque JavaScript "sait" que si nous ne déstructurons pas, nous ferons référence à l'import par défaut.

```plaintext
// main.js
import lalala, { mod1Function2 } from './mod1.js' 

const testFunction = () => {
    console.log('Je suis la fonction principale')
    lalala()
    mod1Function2()
}

testFunction()
```

Et cela résume à peu près tout sur ESmodules également. Simple, j'espère. =)

# Utilisation des modules

D'accord, maintenant que nous sommes clairs sur les différents types de modules disponibles et leur fonctionnement, voyons comment nous pouvons implémenter des modules dans un site web en utilisant HTML et Vanilla JS.

Créons un simple fichier HTML avec un titre, deux boutons, et une balise script liant à notre fichier `main.js`.

```plaintext
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Je suis juste un test...</h1>
    <button id="isAlive">Mod1 est-il vivant ?</button>
    <button id="isRolling">Mod1 roule-t-il ?</button>
    <script src="./main.js" type="module"></script>
</body>
</html>
```

Faites attention au fait que je déclare `type="module"` sur la balise script. Nous devons faire cela afin d'utiliser la fonctionnalité de module JS. Si nous ne le faisons pas, nous obtiendrons une erreur comme ceci :

```plaintext
Uncaught SyntaxError: Cannot use import statement outside a module
```

Si nous ouvrons notre fichier HTML, nous devrions obtenir quelque chose comme ceci :

![screenshot-2](https://www.freecodecamp.org/news/content/images/2022/04/screenshot-2.png align="left")

Notre fichier `main.js` contiendra ce code :

```plaintext
// main.js
import { mod1Function, mod1Function2 } from './mod1.js'

const testFunction = () => console.log('Je suis la fonction principale')

document.getElementById('isAlive').addEventListener('click', () => mod1Function())
document.getElementById('isRolling').addEventListener('click', () => mod1Function2())

testFunction()
```

Nous ajoutons simplement un écouteur d'événement de clic à chaque bouton pour que les fonctions provenant du fichier `mod1.js` soient exécutées.

D'accord, nous pouvons maintenant servir notre fichier HTML et voir si cela fonctionne. Nous devons servir le fichier, nous ne pouvons pas simplement ouvrir le HTML dans le navigateur car nous obtiendrions une erreur CORS comme ceci :

```plaintext
Access to script at ... from origin 'null' has been blocked by CORS policy: Cross origin requests are only supported for protocol schemes: http, data, chrome, chrome-extension, brave, chrome-untrusted, https.
```

Pour le servir rapidement, vous pouvez utiliser l'extension **Live server** de VS code, ou créer une application Node en exécutant `npm init -y` puis en exécutant `npx serve`.

Quoi qu'il en soit, une fois le fichier servi, nous pouvons cliquer sur chaque bouton et tester que nos fonctions s'exécutent correctement. Notre console devrait ressembler à ceci :

![screenshot_1-1](https://www.freecodecamp.org/news/content/images/2022/04/screenshot_1-1.png align="left")

Mais il y a une autre chose à ce sujet. Si nous allons dans l'onglet réseau des outils de développement du navigateur, et filtrons par fichiers JS, nous pouvons voir que le site charge deux fichiers, `main.js` et `mod1.js` :

![screenshot_3](https://www.freecodecamp.org/news/content/images/2022/04/screenshot_3.png align="left")

Bien sûr, si nous allons utiliser le code à l'intérieur de chaque fichier, les deux doivent être chargés – mais ce n'est pas la meilleure chose à faire. C'est parce que le navigateur doit effectuer deux requêtes différentes pour charger tout le JS nécessaire.

Nous devons toujours essayer de réduire les requêtes au minimum pour augmenter la performance de nos projets. Alors voyons comment nous pouvons faire cela avec l'aide d'un module bundler.

Commentaire de côté : si vous souhaitez une explication vidéo, [Kent C Dodds en a une excellente](https://egghead.io/lessons/javascript-use-javascript-modules-in-the-browser). Je vous recommande vraiment de le suivre, il est l'un des meilleurs enseignants JS. Et [voici une autre vidéo cool](https://www.youtube.com/watch?v=qgRUr-YUk1Q) par Fireship. ;)

# Bundling des modules

Comme mentionné précédemment, diviser notre code en modules est bien car notre base de code sera mieux organisée et il sera plus facile de réutiliser notre code.

Mais ce sont des avantages uniquement pour la phase de développement d'un projet. En production, les modules ne sont pas la meilleure chose, car forcer le navigateur à faire une requête pour chaque fichier JS peut nuire aux performances du site.

Ce problème peut être facilement résolu avec l'utilisation d'un module bundler. En termes simples, les module bundlers sont des programmes qui prennent les modules JS en entrée et les combinent en un seul fichier (de nombreux module bundlers ont beaucoup plus de fonctionnalités mais c'est leur concept de base).

Grâce à cela, en tant que développeurs, nous pouvons coder notre projet en le divisant en morceaux bien organisés, puis exécuter un module bundler pour obtenir le code final qui sera utilisé en production.

Cette étape de conversion du "code de développement" en "code de production" est normalement reconnue comme "build".

Il existe de nombreuses options à utiliser pour cela (comme [Browserify](https://browserify.org/), [Parcel](https://parceljs.org/), [Rollup.js](https://rollupjs.org/guide/en/), [Snowpack](https://www.snowpack.dev/)...) mais le plus largement utilisé est [Webpack](https://webpack.js.org/). Alors voyons un exemple en utilisant Webpack.

* Commentaire de côté 1 : Si vous voulez approfondir les module bundlers et leur fonctionnement, [cette vidéo géniale de Fireship](https://www.youtube.com/watch?v=5IG4UmULyoA&t=382s) pourrait être un bon point de départ.
    
* Commentaire de côté 2 : Webpack est un outil très robuste et sophistiqué qui peut faire beaucoup de choses en plus de bundler les fichiers JS. Consultez [leur documentation](https://webpack.js.org/) si vous voulez en savoir plus.
    

Super, nous pouvons maintenant commencer par créer une application Node (si vous ne l'avez pas déjà fait) en exécutant `npm init -y`. Ensuite, nous devrons installer Webpack et le CLI Webpack en exécutant `npm i --save-dev webpack webpack-cli`.

Ensuite, nous créerons un fichier `webpack.config.js` et mettrons ce code à l'intérieur :

```plaintext
/* webpack.config.js */
const path = require('path');

module.exports = {
  entry: './main.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
  },
};
```

Ce fichier sera responsable de la configuration de Webpack et de son fonctionnement dans notre application.

Ce que nous faisons ici en premier, c'est de définir le fichier d'entrée (`entry: './main.js'`). Webpack commencera par lire ce fichier puis analysera toutes les dépendances (modules importés depuis ce fichier). En d'autres termes, le fichier d'entrée est notre fichier JS principal où tous les autres modules sont importés.

Ensuite, nous déclarons la sortie – d'abord en déclarant le chemin où elle sera stockée puis en déclarant le nom du fichier bundlé.

```plaintext
output: {
    path: path.resolve(__dirname, 'dist'),
    filename: 'bundle.js',
},
```

Super ! Maintenant, allons dans notre fichier `package.json` et ajoutons un script `build`, comme ceci :

```plaintext
{
  "name": "testappv2",
  "version": "1.0.0",
  "description": "",
  "main": "main.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1",
    "build": "webpack"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "webpack": "^5.72.0",
    "webpack-cli": "^4.9.2"
  }
}
```

Ensuite, nous pouvons retourner à notre terminal et exécuter `npm run build`. Cela devrait créer un répertoire `dist` dans notre projet, et à l'intérieur un fichier `bundle.js`.

Si vous vérifiez ce fichier, vous verrez ce code à l'intérieur :

```plaintext
(()=>{"use strict";document.getElementById("isAlive").addEventListener("click",(()=>console.log("Mod1 est vivant !"))),document.getElementById("isRolling").addEventListener("click",(()=>console.log("Mod1 roule, bébé !"))),console.log("Je suis la fonction principale")})();
```

Vous verrez que c'est pratiquement le même code que nous avions distribué dans nos fichiers, mais tout bundlé dans un seul fichier et minifié.

La seule chose restante est de changer la balise script dans notre fichier `index.html` pour qu'elle consomme le JS bundlé maintenant, comme ceci :

```plaintext
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Je suis juste un test...</h1>
    <button id="isAlive">Mod1 est-il vivant ?</button>
    <button id="isRolling">Mod1 roule-t-il ?</button>
    <script src="./dist/bundle.js" type="module"></script>
</body>
</html>
```

Maintenant, nous pouvons le servir à nouveau, vérifier que le JS fonctionne toujours parfaitement, et si nous ouvrons à nouveau l'onglet réseau, nous devrions voir qu'un seul fichier est chargé ! =D

![screenshot_2-1](https://www.freecodecamp.org/news/content/images/2022/04/screenshot_2-1.png align="left")

J'espère que cet exemple simple vous a aidé à comprendre la pertinence des module bundlers et comment ils nous aident à combiner la grande expérience de développement de l'architecture modulaire avec de bonnes performances de site.

# Résumé

Eh bien, nous avons terminé pour aujourd'hui. Dans cet article, nous avons vu ce que sont les modules, pourquoi ils sont cool, les différentes façons dont vous pouvez implémenter des modules en JavaScript, et un exemple pratique de bundling de notre code avec Webpack.

Pour un guide complet sur les modules JS, vous pouvez consulter [cet article](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules).

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [linkedin](https://www.linkedin.com/in/germancocca/) ou [twitter](https://twitter.com/CoccaGerman).

Santé et à la prochaine ! =D

![giphy](https://www.freecodecamp.org/news/content/images/2022/04/giphy.gif align="left")