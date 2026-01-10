---
title: Comment configurer Tensorflow.js pour le machine learning dans votre navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-21T18:44:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-tensorflow-js-for-machine-learning-in-your-browser-2540b5c43411
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AlcVryPcarDIsQ9b9a6VVw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: JavaScript
  slug: javascript
- name: Machine Learning
  slug: machine-learning
- name: TensorFlow
  slug: tensorflow
- name: Web Development
  slug: web-development
seo_title: Comment configurer Tensorflow.js pour le machine learning dans votre navigateur
seo_desc: 'By Kevin Scott

  Until recently, just getting started writing your first line of machine learning
  code required a hefty upfront investment in time and money.

  Last year, I built my own PC specifically for machine learning. I researched the
  parts and ass...'
---

Par Kevin Scott

Jusqu'à récemment, le simple fait de commencer à écrire votre première ligne de code de machine learning nécessitait un investissement initial important en temps et en argent.

L'année dernière, [j'ai construit mon propre PC](http://thekevinscott.com/deep-learning-cryptocurrency-pc-1-hardware/) spécifiquement pour le machine learning. J'ai recherché les pièces et je l'ai assemblé moi-même. Rien que cela m'a coûté environ 1600 $ et 30 heures de temps de configuration. Je tente toujours de dompter la configuration de l'ordinateur et les bibliothèques pour qu'il fonctionne avec divers frameworks.

La bonne nouvelle est que commencer avec le machine learning n'a jamais été aussi facile. En fait, si vous lisez ceci, cela signifie que vous avez déjà les outils nécessaires pour vous lancer. **Vous pouvez maintenant apprendre le framework de machine learning Tensorflow directement dans votre navigateur, en utilisant JavaScript.**

### Tensorflow.js

![Image](https://cdn-media-1.freecodecamp.org/images/1*rsWM2fP8HtMBQnhd31Dzow.jpeg)
_Google I/O 2018 par [Bruno Sanchez-Andrade Nuño](https://www.flickr.com/photos/nasonurb/4649268142/in/photolist-85QHry-4RMuLP-6rHwUw-4RRzRS-8434Pj-83YVXe-4FLYVv-83SpSP-6TYsho-cww2Ej-oUgsLJ-6rwVWy-84KqdW-cvqdhq-TDNAMg-6TUr7z-oDPfkP-iJXS7Q-bDUXd-6TUqA4-83VSYq-6TYprJ-6U1qaL-6TWpTt-9Jo26U-6U1pQ5-gB66bX-dzG2FW-6TYmW9-83SEEc-dpkJrd-6TYnwA-qMXaBP-6TUotz-6TUmbi-jRSgF-iK1Pig-6TYwDs-GqG1if-83sPNj-oWgxXQ-6TUq68-6TYmgb-6rDpex-qMMZQZ-4RMiFv-9Gwi29-4RMJf2-cocCNf-4RRvyL" rel="noopener" target="_blank" title=")_

Google [a publié Tensorflow.js](https://www.youtube.com/watch?v=OmofOvMApTU) lors du Google I/O 2018. Il existe [d'énormes cas d'utilisation](https://thekevinscott.com/reasons-for-machine-learning-in-the-browser/) pour l'exécution d'algorithmes de machine learning dans le navigateur.

De plus, c'est une excellente opportunité d'utiliser JavaScript pour explorer les concepts de machine learning sans avoir à installer quoi que ce soit.

Si vous êtes nouveau dans JavaScript, ou si cela fait un moment que vous n'avez pas écrit de code front-end, certains des changements récents dans l'écosystème JavaScript pourraient vous dérouter. Je vais lister les bases de JavaScript moderne dont vous avez besoin pour exécuter les exemples Tensorflow.js et commencer à explorer le machine learning.

### Tutoriel d'installation

Permettez-moi de répéter quelque chose : **tout ce dont vous avez besoin pour exécuter Tensorflow.js est votre navigateur web.**

Il est facile de perdre de vue parmi toutes les discussions sur les transpilers, les bundlers et les packagers, mais tout ce dont vous avez besoin est un navigateur web pour exécuter Tensorflow.js. Le code que vous développez localement est le même code que vous pourrez envoyer à vos utilisateurs pour qu'ils l'exécutent dans leurs navigateurs.

Voyons trois façons rapides de faire fonctionner l'exemple Hello World sans installer quoi que ce soit. J'utiliserai le [code de démarrage](https://js.tensorflow.org/#getting-started) de la documentation Tensorflow.js.

#### `Premiers pas` avec la console de votre navigateur

Chaque navigateur web moderne est livré avec une sorte de console JavaScript interactive intégrée. J'utilise Chrome, qui inclut une console JavaScript que vous pouvez ouvrir avec « Affichage > Développeur > Console JavaScript ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZaPOW2eZ_ubo1hBnx6ugkg.gif)

Cette console JavaScript vous permet d'écrire du JavaScript et de l'exécuter immédiatement. Nous allons l'utiliser pour exécuter l'exemple de démarrage de la [documentation Tensorflow.js](https://js.tensorflow.org/#getting-started).

Tout d'abord, vous devrez inclure le fichier JavaScript Tensorflow.js. Une version hébergée du fichier est disponible via le [Content Delivery Network (CDN)](https://www.webopedia.com/TERM/C/CDN.html) ci-dessous. Une façon rapide d'inclure un fichier `.js` externe via la console est :

```
var script = document.createElement('script');script.src = "https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@0.10.0";document.getElementsByTagName('head')[0].appendChild(script);
```

Copiez et collez ceci dans votre console JavaScript, et vous aurez une copie de Tensorflow enregistrée sous la variable `tf`. (Si vous tapez `tf` dans votre console, vous verrez une référence à celle-ci).

Vous pouvez ensuite copier et coller le reste de l'exemple de démarrage (le JavaScript entre la deuxième balise `<script>`) en le collant directement dans votre console.

#### Premiers pas avec une plateforme d'hébergement JavaScript

Une approche alternative consiste à utiliser une plateforme d'hébergement JavaScript en ligne. Trois plateformes populaires sont [CodePen](https://codepen.io/), [JSFiddle](https://jsfiddle.net/) et [JSBin](https://jsbin.com/). Ces plateformes peuvent automatiquement inclure des scripts pour vous et prendre en charge la transpilation de votre code dans le navigateur, ce qui facilite grandement le démarrage.

Vous pouvez consulter [l'exemple suivant sur Codepen](https://codepen.io/thekevinscott/pen/aGapZL) pour voir une implémentation fonctionnelle. Assurez-vous d'ouvrir votre console de navigateur, comme expliqué ci-dessus, pour voir la sortie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7ID_fTBRD7koiRuH38zVNw.jpeg)

#### Premiers pas en local

Une troisième option pour faire fonctionner Tensorflow.js consiste à enregistrer le code sous forme de fichier `.html` et à l'ouvrir localement sur votre ordinateur. Et vous n'avez pas besoin d'un serveur web pour cela !

Copiez le code HTML dans un fichier et ouvrez-le dans votre navigateur web. Par exemple, si vous enregistrez le fichier sur votre bureau et que vous êtes sur un Mac, vous pourriez l'ouvrir dans votre navigateur avec l'URL suivante :

`file:///Users/YOURNAME/Desktop/sample.html`

Il est important de noter que la visualisation des fichiers HTML de cette manière introduit des limitations, notamment des problèmes de référencement des liens relatifs, de gestion des appels ajax et de sécurité, entre autres. Mais c'est un moyen rapide et facile de faire fonctionner quelque chose dans votre navigateur.

### Le flux de travail de développement JavaScript moderne

Espérons qu'à ce stade, vous pouvez voir à quel point il est facile de faire apparaître quelque chose de basique dans votre navigateur. Si vous commencez à regarder les exemples Tensorflow.js, vous pourriez vous demander :

* comment organiser mes fichiers ?
* comment gérer les bibliothèques tierces dans mon code ?
* qu'en est-il de ces erreurs de syntaxe ?

Dès que vous allez au-delà de l'exemple basique « Hello World » ci-dessus et que vous passez à certains des autres exemples, vous commencerez à rencontrer des problèmes de syntaxe et d'organisation. C'est là qu'un bon pipeline JavaScript sera votre meilleur ami.

#### Un peu d'histoire de JavaScript

Au fur et à mesure que nos attentes envers les applications web ont augmenté au cours de la dernière décennie, l'écosystème front-end a explosé en complexité.

JavaScript en particulier a beaucoup mûri en tant que langage de programmation, adoptant un certain nombre de changements progressistes tout en continuant à supporter l'une des plus grandes bases d'utilisateurs de tous les langages de programmation.

Les nouvelles modifications de la spécification du langage sont référencées avec des acronymes comme ES5, ES6, ES2015 et E2016.

« ES » signifie ECMAScript, et [JavaScript est basé sur cette norme](https://benmccormick.org/2015/09/14/es5-es6-es2016-es-next-whats-going-on-with-Javascript-versioning/). Les nombres 5 et 6 étaient traditionnellement utilisés pour désigner les versions de la norme, mais de nos jours, les années sont utilisées pour plus de clarté.

[La prise en charge moderne des navigateurs pour ES6 est inégale](http://kangax.github.io/compat-table/es6/). Certaines fonctionnalités de pointe ou proposées ne sont pas encore prises en charge, et les anciens navigateurs (en particulier Internet Explorer) ne prendront jamais en charge la dernière spécification.

En raison de cette instabilité, si vous souhaitez atteindre le public le plus large possible, vous utilisez ce que l'on appelle un [bundler ou transpiler](https://dev.to/kayis/4-Javascript-bundlers-2g4b). Il s'agit d'un logiciel qui convertit votre code JavaScript écrit avec des commodités modernes en une version largement adoptée. ES5 est largement pris en charge et est généralement une bonne cible.

De nombreux exemples Tensorflow.js utilisent une nouvelle syntaxe qui n'est pas encore largement prise en charge dans les navigateurs et nécessite une transpilation. Je vais d'abord expliquer la syntaxe, puis expliquer comment les faire fonctionner.

#### `import` et `export`

`import` et `export` sont deux éléments de syntaxe récemment introduits dans JavaScript pour importer des modules. La saga des modules JavaScript est [longue et sinueuse](https://ponyfoo.com/articles/brief-history-of-modularity), mais la [communauté s'est largement mise d'accord sur `import` plutôt que `require`](https://insights.untapt.com/webpack-import-require-and-you-3fd7f5ea93c0).

Malheureusement, en mai 2018, `import` n'est pris en charge par aucun navigateur, donc pour l'utiliser, vous devez utiliser un transpiler.

Dans la documentation de démarrage, vous verrez un exemple de `import` dès le début :

```
import * as tf from '@tensorflow/tfjs';
```

Cela revient essentiellement à :

```
var tf = require('@tensorflow/tfjs');
```

Vous pourriez également voir quelque chose comme :

```
import { util, tensor2d } from '@tensorflow/tfjs';
```

L'équivalent utilisant `require` est :

```
var tf = require("@tensorflow/tfjs");var util = tf.util;var tensor2d = tf.tensor2d
```

#### `async` et `await`

JavaScript a traditionnellement été largement utilisé avec des interfaces utilisateur, qui effectuent de nombreuses actions asynchrones. Il y a eu trois grands modèles pour gérer le code asynchrone au fil des ans : [callbacks, promesses et async/await](https://medium.com/@stevekonves/three-Javascript-async-patterns-1d2e7094860a).

`async`/`await` fournit un moyen de définir des fonctions asynchrones de manière synchrone. [De nombreux exemples Tensorflow.js](https://js.tensorflow.org/tutorials/webcam-transfer-learning.html) utilisent cette syntaxe `async` / `await`.

Voici deux versions du même code, la première écrite avec `async`/`await`, la seconde utilisant des promesses :

```
// Avec async/awaitasync function loadMobilenet() {  const mobilenet = await tf.loadModel(      'https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json');  // Retourne un modèle qui produit une activation interne.  const layer = mobilenet.getLayer('conv_pw_13_relu');  return tf.model({inputs: model.inputs, outputs: layer.output});});// Avec des promessesfunction loadMobilenet() {  return tf.loadModel('https://storage.googleapis.com/tfjs-models/tfjs/mobilenet_v1_0.25_224/model.json').then(function (mobilenet) {    // Retourne un modèle qui produit une activation interne.    const layer = mobilenet.getLayer('conv_pw_13_relu');    return tf.model({inputs: model.inputs, outputs: layer.output});  });});
```

Ces deux fonctionnalités du langage — `import`/`export` et `async`/`await` — rendent l'écriture de JavaScript plus agréable. Voyons les outils dont nous avons besoin pour les utiliser dans notre propre code.

### Outils JavaScript

Dans la documentation de démarrage, vous verrez cette note :

> Remarque : comme nous utilisons la syntaxe ES2017 (comme `import`), ce flux de travail suppose que vous utilisez un bundler/transpiler pour convertir votre code en quelque chose que le navigateur comprend. Voir nos exemples pour voir comment nous utilisons Parcel pour construire notre code. Cependant, vous êtes libre d'utiliser n'importe quel outil de construction que vous préférez.

Parlons des outils de construction.

#### Bundlers

![Image](https://cdn-media-1.freecodecamp.org/images/1*6mtkrbd03TcqOJGqqb0YlA.jpeg)
_Chef d'orchestre par [Rob Swystun](https://www.flickr.com/photos/rob_swystun/8098008837/in/photolist-dkApU2-KcT4m-4FRtTt-bs1ie-4FaQwJ-n4ZLz-5H5h5h-9QyqcV-HMKLpZ-bRcaTr-8AJzKR-o1hz5g-mUja5-4hde2s-ojw5ER-o1hzfM-7QTcn-baxtwT-o1gyBW-PZwwc-9Lqwso-o1gwTq-q6JLU3-4tpd7s-6utd7E-afAcD1-eQ5nNq-7k6Kmu-TZwnt4-hzhqsc-QW7UrX-6Sgmk9-di55YZ-c5g9mh-4sJY58-66uZkH-nuSDiR-tiR5Un-62C3pm-6GkQ63-5mXNoS-9rBtDY-8eJvZq-26reTMP-6o1GgZ-7nJCtp-kqpcEr-7r1AZJ-RAtTeU-8nX15C" rel="noopener" target="_blank" title=")_

Les bundlers ont pris le rôle de chef d'orchestre des codebases front-end en croissance. Un bundler est un programme qui prend votre code JavaScript et le « bundle » en un fichier compatible pour le navigateur.

Les bundlers transpileront également le code (convertir le code ES2018 en ES5, ainsi que d'autres dialectes comme React ou Typescript, en utilisant quelque chose comme [babel](https://babeljs.io/)), mettront en place le "hot reloading" pour rafraîchir le navigateur avec les changements de code sans recharger la page, et bien d'autres choses pour améliorer le développement front-end.

[Grunt](https://gruntjs.com/) et [Gulp](http://gulpjs.com/) étaient des bundlers populaires, mais ont récemment perdu en faveur de `[webpack](https://webpack.js.org/)`. D'autres bundlers incluent `[parcel](https://parceljs.org/)` et `[rollup](https://rollupjs.org/guide/en)`. Les exemples Tensorflow.js utilisent `parcel`.

#### Gestionnaires de paquets

Souvent, lorsque vous rencontrez une bibliothèque JavaScript, vous verrez des instructions d'installation comme `yarn add @tensorflow/tfjs` ou `npm install @tensorflow/tfjs`.

`[yarn](https://yarnpkg.com/en/)` et `[npm](https://www.npmjs.com/)` sont tous deux des gestionnaires de paquets. Ce sont des outils en ligne de commande utilisés pour installer et suivre vos dépendances JavaScript tierces.

`yarn` et `npm` sont assez similaires, et le choix de celui à utiliser dépend largement des préférences personnelles (bien que vous trouverez de nombreux débats en ligne si vous êtes intéressé par ce genre de choses).

L'un ou l'autre enregistrera vos dépendances dans un fichier `package.json` qui doit être ajouté à votre dépôt git. Ce fichier permettra à d'autres développeurs d'installer rapidement toutes les dépendances nécessaires pour votre projet et de faire fonctionner les choses rapidement.

Pour obtenir tous ces avantages, la première étape consiste à installer `npm` ou `yarn`, ainsi que `Node.js`. Une fois ceux-ci en place, vous pouvez suivre les instructions de n'importe quel exemple Tensorflow.js et ils devraient fonctionner directement. Habituellement, la configuration d'un nouveau projet front-end avec ces outils est un processus en une seule étape.

### Conclusion

Encore une fois, vous n'avez besoin d'aucun de ces outils pour travailler avec ces exemples, mais les utiliser rend les choses beaucoup plus faciles. Si vous avez l'intention de faire du développement JavaScript sérieux, je vous encourage à jouer avec ces outils, ainsi qu'avec d'autres outils JavaScript populaires comme [React](https://reactjs.org/) et [Typescript](https://www.typescriptlang.org://www.typescriptlang.org/), qui rendent la gestion de grandes bases de code beaucoup meilleure.

Publié à l'origine sur [thekevinscott.com](https://thekevinscott.com/tensorflowjs-hello-world)

Remerciements spéciaux à [Ari Zilnik](https://www.freecodecamp.org/news/how-to-set-up-tensorflow-js-for-machine-learning-in-your-browser-2540b5c43411/undefined).