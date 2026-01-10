---
title: Comment configurer votre environnement ES6 rapidement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-25T12:46:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-and-run-es6-quickly-b3cb115ea3dd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*seBGHx_gW4Kkeq3Yh66cFw.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: web
  slug: web
seo_title: Comment configurer votre environnement ES6 rapidement
seo_desc: 'By Dler Ari

  As you may know, browsers are starting to catch up with ES6. However, not everything
  works as smooth as expected, and this can be a time-consuming and tedious problem
  to solve. If something goes wrong, trying to identify if the problem li...'
---

Par Dler Ari

Comme vous le savez peut-être, les navigateurs commencent à rattraper ES6. Cependant, tout ne fonctionne pas aussi bien que prévu, et cela peut être un problème chronophage et fastidieux à résoudre. Si quelque chose ne va pas, essayer d'identifier si le problème réside dans le code ou le navigateur n'est pas un processus facile.

Mais ne vous inquiétez pas, je vais vous montrer comment vous pouvez rapidement installer et écrire du code ES6, et surtout, le rendre compatible avec tous les navigateurs qui supportent ES5.

#### ES5 vers ES6

Pour écrire du code ES6, nous devons installer quelque chose qui peut le compiler en ES5. Nous allons utiliser `Rollup`. Il compile de petits morceaux de code en quelque chose de plus grand et plus complexe, comme une bibliothèque ou une application. Cela vous permet d'utiliser la POO (programmation orientée objet) qui rend votre code plus propre, structuré et modulaire, ainsi que d'autres fonctionnalités utiles. Pour clarifier, JS est orienté objet, mais ce n'est pas un langage orienté objet **basé sur les classes** comme Java, C++, C#, etc., jusqu'à la sortie de ES6.

Sinon, la chose la plus proche de la POO en ce qui concerne **l'inclusion de classes** avec ES5 est d'utiliser IIFE (Immediately Invoked Function Expression), ou d'installer des bibliothèques externes. Mais pourquoi dépendre de ressources externes lorsque vous avez un langage de base qui supporte le paradigme POO ? Beaucoup des langages de programmation les plus largement utilisés le supportent déjà (comme C++, Java, C# et PHP).

#### Pourquoi ES6 ?

Personnellement, je l'utilise parce qu'il me permet d'organiser mon code en fichiers séparés, ce qui facilite la mise à l'échelle et la maintenance du code.

Par exemple, dans mon HTML, j'ai un `script` qui charge `main.js`, et à l'intérieur de `main.js`, je charge plusieurs fichiers `JS` en utilisant les instructions `import` et `export`. Au lieu d'avoir plusieurs scripts dans mon fichier HTML, je n'en ai besoin que d'un (moins de code).

#### Prérequis

* Linux ou macOS (basé sur Debian)
* NPM (gestionnaire de paquets) installé
* Connaissances de base de la CLI

### Étape un : Installer Rollup

Pour utiliser `Rollup`, nous devons l'installer globalement. N'oubliez pas d'utiliser `sudo`. Cela vous permet d'accéder aux commandes `Rollup` dans n'importe quel projet avec lequel vous travaillez.

### Étape deux : Structure des fichiers

Après avoir installé `Rollup` globalement, l'étape suivante consiste à configurer la structure des dossiers et à créer deux dossiers `src` et `dest` à l'intérieur de votre projet. De plus, créez `index.html`.

* `src` → Fichiers ES6 (Où vous écrirez le code)
* `dest` → Génère un ES5 (Versions compilées de ES6)

![Image](https://cdn-media-1.freecodecamp.org/images/rr27ThFPxfFLGvHax9OptosBHLWBhRhXumoa)
_Structure des dossiers du projet ES6_

Gardez à l'esprit que le fichier `bundle.js` est généré automatiquement lorsque la commande `Rollup` est exécutée. Nous en parlerons plus tard.

### Étape trois : Créer un fichier de configuration

Créez un nouveau fichier et nommez-le `rollup.config.js`. Ensuite, ajoutez ce code :

![Image](https://cdn-media-1.freecodecamp.org/images/QYC3JcSz2eunCjok-wZVevaKxAVJHIkhJ-bP)
_Fichier de configuration pour rollup.config.js_

Assurez-vous que le chemin de la source `input` et `output` est correct avec votre structure de dossiers, et que ce fichier est placé dans le dossier principal.

### Étape quatre : Charger le fichier de script dans HTML

Nous sommes presque prêts, mais d'abord nous devons lier le bon fichier source dans notre modèle HTML. Cela chargera le fichier ES5 qui est compilé à partir de ES6.

![Image](https://cdn-media-1.freecodecamp.org/images/2s5VhC9I2wYk1AaXriy6ybxXYQliIXSupBhs)
_Le modèle HTML charge le script ES6_

### Étape cinq : Configurer les fichiers JS

Pour vérifier que la commande `Rollup` fonctionne, nous devons configurer une simple structure OOP. Nous allons créer une classe `car.js`, et l'`exporter par défaut` vers `main.js`.

Gardez à l'esprit que ce fichier exporte une nouvelle instance de la classe `car.js`, et cela permet d'accéder aux méthodes directement plutôt que d'écrire `const car = new Car()` dans la classe `main.js`.

Puisque je suis un ingénieur logiciel paresseux, traiter quelques caractères de code supplémentaires est chronophage :)

![Image](https://cdn-media-1.freecodecamp.org/images/5aKZz1Ppg7yzGGIPj16zbAqnSY7VDA7gpPzo)
_Classe car.js_

Ensuite, importez la classe `car.js` dans `main.js` afin d'accéder à la méthode `type()`.

![Image](https://cdn-media-1.freecodecamp.org/images/TAsHat7IhM9h1BgK-rdFNv1pHxCB0MPyTSv4)
_Classe main.js_

### Étape six : Compiler ES6 en ES5

Pour exécuter le fichier de configuration que nous avons créé, exécutez cette commande `$ rollup -c` ou `$ rollup --config` — les deux sont identiques.

Après avoir exécuté l'une des commandes, ouvrez `index.html` via un navigateur, puis ouvrez l'inspecteur (`ctrl + shift + I`) sur le navigateur, et allez dans `console`. Si vous voyez le texte `"Tesla Model S"`, cela signifie que tout a fonctionné avec succès.

Gardez à l'esprit que chaque fois que vous apportez des modifications aux fichiers ES6, vous devez les mettre à jour en exécutant la commande.

### Optionnel

Puisque vous avez installé `Rollup` globalement, vous pouvez compiler ES6 sans avoir besoin du fichier `rollup.config.js`. Cela fait exactement la même chose :

`$ rollup src/main.js — o dest/bundle.js — f iife`

Personnellement, je recommanderais d'exécuter `$ rollup -c` comme montré dans l'étape six puisque cela nécessite moins de code. N'oubliez pas que vous devez avoir le fichier `rollup.config.js` inclus lorsque vous exécutez cette commande.

*Si vous avez trouvé cette approche d'installation courte et utile pour ES6, veuillez commenter et applaudir. C'est bon karma.*