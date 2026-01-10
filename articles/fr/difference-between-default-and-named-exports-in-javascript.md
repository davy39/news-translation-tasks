---
title: Quelle est la différence entre les exports par défaut (Default) et les exports
  nommés (Named) en JavaScript ?
date: '2023-08-14T16:36:15.000Z'
author: freeCodeCamp
authorURL: https://www.freecodecamp.org/news/author/yazdun/
originalURL: https://freecodecamp.org/news/difference-between-default-and-named-exports-in-javascript
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Frame-6-2.jpg
tags:
- name: JavaScript
  slug: javascript
seo_desc: "By Yazdun Fadali\nJavaScript is one of the most popular programming languages\
  \ among web developers. And it offers multiple ways to organize and share code between\
  \ different files. \nWhen working with modules, you might come across two common\
  \ ways of ex..."
---


JavaScript est l'un des langages de programmation les plus populaires parmi les développeurs web. Il offre plusieurs façons d'organiser et de partager du code entre différents fichiers.

<!-- more -->

Lorsque vous travaillez avec des modules, vous rencontrerez deux façons courantes d'exporter : les exports par défaut (`Default exports`) et les exports nommés (`Named exports`).

Comprendre la différence entre ces deux méthodes est essentiel pour gérer efficacement votre base de code et la rendre plus facile à maintenir.

Dans cet article, nous explorerons les différences entre les exports par défaut et nommés en JavaScript. Nous mettrons en évidence leurs cas d'utilisation et les meilleures pratiques pour vous aider à choisir la bonne approche pour vos projets.

## Table des matières

-   [Ce que vous allez apprendre](#heading-ce-que-vous-allez-apprendre)
-   [Pour commencer](#heading-pour-commencer)
-   [Que sont les modules JavaScript](#heading-que-sont-les-modules-javascript) ?
-   [Qu'est-ce que le mot-clé export exactement en JavaScript](#heading-qu-est-ce-que-le-mot-cle-export-exactement-en-javascript) ?
-   [Qu'est-ce que l'export par défaut en JavaScript](#heading-qu-est-ce-que-l-export-par-defaut-en-javascript) ?
-   [Qu'est-ce que l'export nommé en JavaScript](#heading-qu-est-ce-que-l-export-nomme-en-javascript) ?
-   [Comment créer une application simple en utilisant les modules JavaScript](#heading-comment-creer-une-application-simple-en-utilisant-les-modules-javascript)
-   [Conclusion](#heading-conclusion)

## Ce que vous allez apprendre

Dans ce tutoriel, vous découvrirez d'abord les modules JavaScript et comment ils améliorent le code et facilitent sa gestion. Vous explorerez les exports par défaut et les exports nommés, en comprenant quand utiliser chacun d'eux.

Pour mettre tout cela en pratique, vous créerez une application simple de changement de couleur (color flipper) qui regroupe tous ces concepts, rendant votre expérience d'apprentissage concrète.

J'ai également créé un tutoriel vidéo basé sur cet article. Vous pouvez le regarder [ici sur YouTube][9].

Voici la [Démo en direct][10] de ce que nous allons créer :

![Il y a un bouton au milieu de l'écran, vous pouvez cliquer sur ce bouton et changer la couleur d'arrière-plan de l'élément body](https://www.freecodecamp.org/news/content/images/2023/08/ezgif-5-d38eb39cfc--1-.gif)

Application Color flipper

## Pour commencer

Pour commencer ce tutoriel, j'ai déjà préparé un projet boilerplate qui contient toutes les dépendances requises. Cela élimine le besoin de configurer votre projet de zéro.

Clonez simplement le [boilerplate de départ][11] depuis le dépôt GitHub, puis suivez le tutoriel. De cette façon, vous pourrez vous concentrer sur l'apprentissage et l'implémentation des concepts sans vous perdre dans les détails de configuration.

Code source GitHub (n'hésitez pas à mettre une étoile si vous appréciez le tutoriel ⭐️ ) :

-   Boilerplate de départ : [Voir sur GitHub][12]
-   Version finale : [Voir sur GitHub][13]

Une fois que vous avez configuré le boilerplate de départ et que vous l'avez lancé avec succès sur votre machine locale, vous pouvez passer à la section suivante.

## Que sont les modules JavaScript ?

Imaginez que vous ayez un projet JavaScript volumineux et complexe, avec de nombreux fichiers et fonctions différents. Cela peut devenir désordonné et difficile à gérer !

Eh bien, les modules JavaScript sont comme de petits conteneurs qui vous aident à mieux organiser votre code et à le rendre plus facile à utiliser et à maintenir.

Considérez un module comme une boîte séparée où vous pouvez placer du code lié. À l'intérieur de cette boîte, vous pouvez avoir des variables, des fonctions ou même des classes qui travaillent ensemble pour accomplir des tâches spécifiques. Ces modules agissent comme de petites unités autonomes qui peuvent être facilement réutilisées dans différentes parties de votre projet.

L'une des caractéristiques essentielles des modules JavaScript est qu'ils vous permettent de décider quelles parties du code vous souhaitez partager avec d'autres parties du projet. Vous pouvez choisir d'exporter certaines fonctions ou données d'un module, les rendant accessibles au reste de votre base de code.

À l'inverse, vous pouvez également importer du code d'autres modules lorsque vous avez besoin de leurs fonctionnalités. C'est comme emprunter des outils dans la boîte à outils d'un ami quand vous avez besoin de réparer quelque chose.

Les modules JavaScript nous aident à :

1.  **Organiser le code** : Les modules vous permettent de regrouper le code lié dans des fichiers séparés, rendant votre projet plus organisé et gérable.
2.  **Encapsuler le code** : Chaque module agit comme une unité autonome, vous pouvez donc masquer certaines parties du code et n'exposer que ce que vous voulez que les autres utilisent.
3.  **Réutilisabilité** : Vous pouvez facilement réutiliser des modules dans différentes parties de notre projet, réduisant la duplication de code et favorisant un processus de développement plus efficace.
4.  **Gestion des dépendances** : Les modules vous aident à gérer les dépendances entre les différentes parties du projet, facilitant le suivi de la manière dont tout s'imbrique.

Pour mieux comprendre ce concept, créons un petit jeu amusant. Nous allons créer une classe JavaScript pour un animal de compagnie virtuel. Cet animal aura un nom et une espèce, et vous pourrez interagir avec lui en jouant avec lui ou en le nourrissant :

```javascript
// 📂 Pet.js

export class VirtualPet {
  constructor(name, species) {
    this.name = name;
    this.species = species;
    this.energy = 100;
  }

  // Play with the pet
  play() {
    this.energy -= 10;
    this._checkStats();
  }

  // Feed the pet
  feed() {
    this.energy += 20;
    this._checkStats();
  }

  // Private method to check and limit the stats
  _checkStats() {
    if (this.energy > 100) {
      this.energy = 100;
    }

    if (this.energy < 0) {
      this.energy = 0;
    }
  }

  // Get the pet's status
  getStatus() {
    return `${this.name} the ${this.species} - Energy: ${this.energy}`;
  }
}
```

Le mot-clé `export` est une partie fondamentale de ce système de modules, vous permettant d'exposer des parties spécifiques de votre code pour être utilisées dans d'autres fichiers.

En utilisant `export`, vous pouvez rendre votre classe `VirtualPet` disponible pour d'autres parties de votre application ou même dans des fichiers entièrement séparés.

Cela vous permet d'encapsuler le comportement de l'animal dans son propre module, favorisant la modularité du code et empêchant l'accès non souhaité aux fonctionnalités internes.

Maintenant, vous pouvez importer la classe `VirtualPet` depuis le module `pet.js` en utilisant l'instruction `import` dans un autre fichier :

```javascript
// 📂 Play.js

import { VirtualPet } from './pet.js';

const myPet = new VirtualPet("Fido", "Dog");

console.log(myPet.getStatus()); // Fido the Dog - Energy: 100

myPet.play();
console.log(myPet.getStatus()); // Fido the Dog - Energy: 90

myPet.feed();
console.log(myPet.getStatus()); // Fido the Dog - Energy: 100
```

Beau travail ! Vous avez réussi à créer un animal de compagnie virtuel en utilisant les modules JavaScript. 🎉

Dans cette section, vous avez appris ce que sont les modules JavaScript et comment le mot-clé `export` vous aide à organiser et partager le code efficacement. Dans la section suivante, vous en apprendrez davantage sur les différentes méthodes d'exportation et d'importation de modules JavaScript à travers divers fichiers.

## Qu'est-ce que le mot-clé `export` exactement en JavaScript ?

En JavaScript, l'instruction `export` est utilisée dans les modules pour exposer des variables, des fonctions ou des classes afin qu'elles puissent être consultées et utilisées dans d'autres parties de l'application ou dans des fichiers séparés.

En utilisant `export`, vous rendez certaines parties de votre code accessibles à l'extérieur du module. Cela vous permet de réutiliser et de promouvoir une structure de code modulaire et organisée.

En JavaScript, il existe deux manières principales d'exporter des valeurs : les exports par défaut, utilisés pour une seule valeur par fichier, et les exports nommés, permettant plusieurs exports par fichier.

## Qu'est-ce que l'export par défaut en JavaScript ?

En JavaScript, un export par défaut (`default export`) est un moyen de partager une seule valeur, fonction ou classe comme élément principal d'un fichier avec d'autres parties de votre code.

Lorsque vous avez un fichier qui doit être utilisé dans d'autres parties de votre application, vous pouvez marquer un élément de ce fichier comme export par défaut en utilisant la syntaxe `export default`.

Cela signifie que lorsque vous importez depuis ce fichier dans une autre partie de votre code, vous n'avez pas besoin d'utiliser des accolades `{}` autour de l'instruction d'importation. Au lieu de cela, vous pouvez lui donner le nom que vous voulez lors de l'importation, ce qui le rend plus pratique à utiliser.

```js
// 📂 math.js
const add = (a, b) => a + b;
export default add;

// 📂 main.js
import myAddFunction from './math.js';
const result = myAddFunction(5, 10); // Ceci appellera la fonction add de math.js et stockera le résultat dans la variable 'result'.
```

## Qu'est-ce que l'export nommé en JavaScript ?

Les exports nommés (`named exports`) en JavaScript vous permettent d'exporter plusieurs fonctions, variables ou classes d'un seul fichier en tant qu'entités distinctes. Au lieu d'exporter tout comme une seule unité, vous pouvez nommer spécifiquement et exporter chaque partie individuellement.

Cela vous donne plus de contrôle sur les parties du code que vous souhaitez partager avec d'autres modules. Lors de l'importation de ces exports nommés dans d'autres fichiers, vous devez utiliser les noms exacts qui ont été utilisés lors de l'exportation, garantissant que vous pouvez accéder et utiliser les fonctionnalités spécifiques dont vous avez besoin du fichier source.

```javascript
// 📂 math.js
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

// 📂 main.js
import { add, subtract } from './math.js';

const result1 = add(5, 3); // result1 sera 8
const result2 = subtract(10, 4); // result2 sera 6
```

En JavaScript, un fichier ne peut avoir qu'un seul export par défaut, mais il peut avoir autant d'exports nommés que nécessaire.

Jetons un coup d'œil aux différences entre les exports nommés et les exports par défaut :

### Exports nommés vs Exports par défaut :

Voici quelques caractéristiques des exports nommés :

-   Lorsque vous utilisez des exports nommés, vous pouvez exporter plusieurs valeurs, fonctions ou classes d'un seul fichier, en donnant à chacune d'elles un nom spécifique.
-   Vous devez envelopper les éléments que vous souhaitez exporter dans des accolades `{}` lors de leur importation dans un autre fichier, et vous devez utiliser les noms exacts utilisés lors de l'exportation.
-   Les exports nommés sont parfaits lorsque vous souhaitez partager plusieurs choses d'un fichier et leur donner des noms distincts à utiliser dans d'autres parties de votre code.
-   Un fichier peut avoir autant d'exports nommés que vous le souhaitez.

Voici quelques caractéristiques des exports par défaut :

-   Les exports par défaut sont utiles lorsque vous ne voulez exporter qu'une seule chose principale d'un fichier. C'est comme marquer cet élément comme le plus important à partager.
-   Lors de l'importation d'un export par défaut dans un autre fichier, vous pouvez lui donner n'importe quel nom lors de l'importation, et vous n'avez pas besoin d'utiliser d'accolades `{}`.
-   Un fichier ne peut avoir qu'un seul export par défaut.

### Comment combiner les exports nommés et par défaut :

Il est important de noter qu'un fichier peut avoir à la fois des exports nommés et un export par défaut.

Cela signifie que vous pouvez exporter un élément principal en utilisant `export default`, tout en exportant plusieurs valeurs supplémentaires en utilisant `export`.

Cette flexibilité vous permet d'organiser et de partager différentes parties de votre code efficacement, facilitant l'accès et l'utilisation des fonctionnalités exportées par d'autres parties de votre application.

## Comment créer une application simple en utilisant les modules JavaScript

Dans cette dernière section, vous allez créer une application sympa de changement de couleur (color flipper) en utilisant les modules JavaScript. Vous apprendrez à diviser votre code en fichiers séparés, le rendant réutilisable dans toute votre application et l'organisant efficacement. Plongeons-nous dedans et amusons-nous à construire cette application ensemble.

Si vous ne l'avez pas encore fait, veuillez vous référer à la section [Pour commencer](#heading-pour-commencer) pour configurer le projet boilerplate avant de continuer. Cela vous permettra de progresser dans le tutoriel.

![image-24](https://www.freecodecamp.org/news/content/images/2023/08/image-24.png)

Une fois que vous aurez lancé le projet boilerplate, vous pourrez voir la page suivante dans votre navigateur.

Maintenant, commençons à coder. Ouvrez d'abord `./main.js` et vous pourrez voir le code suivant :

```javascript
//📂./main.js

import "./style.css";

document.querySelector("#app").innerHTML = `
  <div>
    <button id="flipper" type="button">Start Flipping</button>
  </div>
`;
```

Ce code inclut un fichier CSS et définit le contenu de l'élément avec l'ID "app" sur un `div` contenant un bouton avec l'ID "flipper" et le texte "Start Flipping".

Ensuite, vous ajouterez la logique JavaScript pour implémenter la fonctionnalité qui change la couleur d'arrière-plan de l'application lorsque le bouton "Start Flipping" est cliqué.

Pour changer la couleur d'arrière-plan, vous pouvez utiliser un tableau de couleurs, qui est déjà préparé pour vous à l'intérieur de `./colors.js`. Tout ce que vous avez à faire est d'exporter ce tableau afin de pouvoir l'utiliser dans d'autres modules JavaScript au sein de votre application :

```javascript
//📂./colors.js

const colors = [
  "#007bff",
  "#f1c40f",
  "#27ae60",
  "#e74c3c",
  "#8e44ad",
  "#3498db",
  "#f39c12",
];

export default colors;
```

Une fois que vous aurez ajouté `export default colors` à ce fichier, vous pourrez accéder à cette variable dans d'autres modules en l'important.

Maintenant, importons ces `colors` dans `./utils.js` et procédons à l'implémentation d'une fonction qui gérera le changement de couleur d'arrière-plan de votre application :

```javascript
//📂./utils.js

import colorsData from "./colors";

export function getRandomColor() {
  const randomIndex = Math.floor(Math.random() * colorsData.length);
  return colorsData[randomIndex];
}
```

Analysons le code étape par étape :

1.  `import colorsData from "./colors"` : Cette ligne importe les données du fichier `./colors` dans notre fichier actuel. Les données de `./colors` sont assignées à une variable appelée `colorsData`, que nous pouvons maintenant utiliser dans ce fichier.
2.  `export function getRandomColor() { ... }` : Cette ligne définit une fonction appelée `getRandomColor()`. La fonction calcule un index aléatoire à partir du tableau `colorsData` et renvoie la couleur à cet index.

Maintenant, parlons de la façon dont `export default` fonctionne :

Dans le fichier `./colors`, il y a un `default export` du tableau `colors`. Lors de l'utilisation de `export default`, nous pouvons importer directement la valeur exportée sans avoir besoin d'utiliser des accolades `{}` autour d'elle lors de l'importation.

Par exemple, si vous deviez importer plusieurs valeurs du fichier `./colors`, vousutiliseriez des accolades `{}`. Mais comme il n'y a qu'un seul export par défaut dans le fichier `./colors`, vous pouvez l'importer directement sans avoir besoin d'accolades.

De plus, vous pouvez choisir n'importe quel nom lors de l'importation d'un export par défaut. Dans ce cas, vous l'avez nommé `colorsData`, mais vous auriez pu utiliser n'importe quel autre nom, et cela fonctionnerait toujours de la même manière.

Pour l'étape suivante, importons la fonction `getRandomColor` que vous venez de créer dans le fichier `./main.js` et utilisons-la pour changer la couleur d'arrière-plan de votre application :

```javascript
//📂./main.js

import "./style.css";
import { getRandomColor } from "./utils";

document.querySelector("#app").innerHTML = `
  <div>
    <button id="flipper" type="button">Start Flipping</button>
  </div>
`;

document.querySelector("#flipper").addEventListener("click", () => {
  const body = document.body;
  const randomColor = getRandomColor();
  body.style.backgroundColor = randomColor;
});
```

Dans ce code, vous avez utilisé l'import nommé pour accéder à la fonction `getRandomColor` depuis le fichier `./utils`. L'instruction `import { getRandomColor } from "./utils"` vous permet d'importer spécifiquement la fonction `getRandomColor` par son nom exact depuis le module `./utils`.

Une fois que vous avez importé la fonction `getRandomColor`, vous pouvez l'utiliser directement dans votre code sans aucun préfixe ou modification. Par exemple, vous appelez `getRandomColor()` sans avoir besoin de spécifier le module d'où elle provient. Cela rend le code plus propre et plus simple.

En utilisant l'import nommé, vous pouvez choisir précisément quelles fonctions, variables ou constantes vous souhaitez importer d'un module. Cela facilite l'accès aux seules parties spécifiques du code dont vous avez besoin dans votre fichier actuel. Cela aide également à garder votre code organisé et permet un meilleur contrôle sur les fonctionnalités que vous utilisez de différents modules.

Notez qu'avec les imports nommés, le nom doit correspondre des deux côtés.

Beau travail jusqu'à présent ! Voici le résultat actuel :

![Ceci est un aperçu de l'application color flipper, il y a un bouton au centre de l'écran et une fois que vous cliquez dessus, cela change la couleur d'arrière-plan du corps du document](https://www.freecodecamp.org/news/content/images/2023/08/ezgif-1-6b91c14ad7.gif)

Application Color flipper

Maintenant, créons une autre fonction utilitaire qui changera le texte du bouton pour afficher la valeur hexadécimale de la couleur actuelle :

```javascript
//📂./utils.js

import colorsData from "./colors";

export function getRandomColor() {
  const randomIndex = Math.floor(Math.random() * colorsData.length);
  return colorsData[randomIndex];
}

export function changeButtonText(text, element) {
  const button = document.querySelector(element);
  button.innerText = text;
}
```

`changeButtonText` vous permettra de changer le texte affiché sur un bouton. Vous pouvez appeler cette fonction avec deux paramètres : le `text` que vous souhaitez afficher sur le bouton, et l'`element` qui représente le sélecteur du bouton. Une fois appelée, la fonction mettra à jour le texte du bouton avec le `text` spécifié.

Ajoutons cela au fichier `./main.js` et voyons comment cela fonctionne en action :

```javascript
//📂./main.js

import "./style.css";
import { getRandomColor, changeButtonText } from "./utils";

document.querySelector("#app").innerHTML = `
  <div>
    <button id="flipper" type="button">Start Flipping</button>
  </div>
`;

document.querySelector("#flipper").addEventListener("click", () => {
  const body = document.body;
  const randomColor = getRandomColor();
  changeButtonText(`Current Color is ${randomColor}`, "#flipper");
  body.style.backgroundColor = randomColor;
});
```

Vous avez importé la fonction `changeButtonText` en utilisant l'import nommé depuis le fichier `./utils`. La fonction prend deux arguments : le texte que nous voulons afficher sur le bouton et le sélecteur du bouton que nous voulons mettre à jour. Elle change dynamiquement le texte du bouton pour afficher le texte spécifié avec la valeur de la couleur actuelle.

Voici le résultat final :

![Il y a un bouton au milieu de l'écran, vous pouvez cliquer sur ce bouton et changer la couleur d'arrière-plan de l'élément body](https://www.freecodecamp.org/news/content/images/2023/08/ezgif-5-d38eb39cfc--1-.gif)

Résultat final

C'est tout – félicitations pour avoir construit votre application color flipper en utilisant les modules JavaScript ! 🎉

L'approche modulaire vous aide à organiser et à réutiliser le code efficacement, rendant votre application fonctionnelle et facile à maintenir. Bien joué !

## Conclusion

En conclusion, les exports JavaScript offrent des outils puissants pour gérer l'organisation du code et partager des fonctionnalités entre différentes parties de nos applications.

Nous avons exploré les différences entre les exports nommés, permettant d'exporter plusieurs entités d'un fichier avec des noms spécifiques, et les exports par défaut, marquant une entité principale comme l'export majeur. Les deux mécanismes sont essentiels pour favoriser la modularité et la réutilisabilité du code.

En comprenant ces techniques d'exportation, vous pouvez créer des structures de code plus organisées et efficaces, ce qui permet une meilleure évolutivité dans vos projets JavaScript.

Merci d'avoir lu ceci jusqu'au bout ! Vous pouvez me suivre sur [Twitter][15] où je partage plus de conseils utiles sur le développement web. Bon code !

[1]: #heading-ce-que-vous-allez-apprendre
[2]: #heading-pour-commencer
[3]: #heading-que-sont-les-modules-javascript
[4]: #heading-qu-est-ce-que-le-mot-cle-export-exactement-en-javascript
[5]: #heading-qu-est-ce-que-l-export-par-defaut-en-javascript
[6]: #heading-qu-est-ce-que-l-export-nomme-en-javascript
[7]: #heading-comment-creer-une-application-simple-en-utilisant-les-modules-javascript
[8]: #heading-conclusion
[9]: https://youtu.be/YHRXgUeF1dA
[10]: https://fcc-javascript-modules.netlify.app/
[11]: https://github.com/Yazdun/fcc-javascript-modules/tree/starter
[12]: https://github.com/Yazdun/fcc-javascript-modules/tree/starter
[13]: https://github.com/Yazdun/fcc-javascript-modules
[14]: #heading-pour-commencer
[15]: https://twitter.com/Yazdun