---
title: Comment créer une visualisation pour le problème Two Sum de Leetcode – Projet
  HTML, CSS et JavaScript
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2023-11-21T21:08:22.000Z'
originalURL: https://freecodecamp.org/news/build-a-visualization-for-leetcode-two-sum-problem
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/nubelson-fernandes--Xqckh_XVU4-unsplash.jpg
tags:
- name: coding interview
  slug: coding-interview
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: leetcode
  slug: leetcode
seo_title: Comment créer une visualisation pour le problème Two Sum de Leetcode –
  Projet HTML, CSS et JavaScript
seo_desc: "With the current state of the job market, there are a lot of people grinding\
  \ out LeetCode as a way to prepare for technical interviews. \nBut sometimes it\
  \ would be nice if there were a visualization showing the algorithms behind these\
  \ problems. \nIn th..."
---

Avec l'état actuel du marché de l'emploi, de nombreuses personnes s'entraînent sur [LeetCode](https://leetcode.com/) pour se préparer aux entretiens techniques.

Mais parfois, il serait utile d'avoir une visualisation montrant les algorithmes derrière ces problèmes.

Dans ce tutoriel, nous allons créer une [visualisation](https://codepen.io/Jessica-Wilkins-the-decoder/full/eYxVyKN) montrant plusieurs approches pour un problème populaire de LeetCode appelé [Two Sum](https://leetcode.com/problems/two-sum/). Nous utiliserons HTML, CSS et JavaScript vanille pour construire ce projet.

## Table des matières

- [Prérequis](#heading-prerequisites)
- [Installation du projet](#heading-installation)
- [Comment résoudre le problème Two Sum de LeetCode](#heading-comment-resoudre-le-probleme-two-sum-de-leetcode)
    - [Description](#heading-description)
    - [Approche par force brute](#heading-approche-par-force-brute)
    - [Solution JavaScript par force brute et complexité temporelle](#heading-solution-javascript-par-force-brute-et-complexite-temporelle)
    - [Approche et solution avec Map](#heading-approche-et-solution-avec-map)
    - [Complexité temporelle pour la solution avec Map](#heading-complexite-temporelle-pour-la-solution-avec-map)
- [Aperçu de la visualisation pour Two Sum](#heading-aperçu-de-la-visualisation-pour-two-sum)
- [Ajout de la visualisation par force brute](#heading-ajout-de-la-visualisation-par-force-brute)
    - [Création des variables const et let](#heading-creation-des-variables-const-et-let)
    - [Création de la fonction getClassName](#heading-creation-de-la-fonction-getclassname)
    - [Création de la fonction bruteForceApproach](#heading-creation-de-la-fonction-bruteforceapproach)
- [Comment désactiver le bouton bruteForceSolutionBtn lorsque l'animation est en cours](#heading-comment-desactiver-le-bouton-bruteforcesolutionbtn-lorsque-lanimation-est-en-cours)
- [Ajout de la visualisation de la solution avec Map](#heading-ajout-de-la-visualisation-de-la-solution-avec-map)
    - [Création des variables const](#heading-creation-des-variables-const)
    - [Création de la fonction asynchrone optimalApproach](#heading-creation-de-la-fonction-asynchrone-optimalapproach)
- [Comment réinitialiser la sortie du tableau pour la solution avec Map](#heading-comment-reinitialiser-la-sortie-du-tableau-pour-la-solution-avec-map)
- [Code final de la solution et exemple en direct](#heading-code-final-de-la-solution-et-exemple-en-direct)
- [Conclusion](#heading-conclusion)


## Prérequis

Ce tutoriel suppose que vous avez des connaissances de base en HTML, CSS et JavaScript. Si vous n'avez pas suivi de cours pour débutants dans l'une de ces langues, je vous suggère de commencer par ces ressources :

* [Certification Conception Web Responsive de freeCodeCamp](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
* [Certification Algorithmes et Structures de Données JavaScript de freeCodeCamp](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)

Ce tutoriel suppose également que vous avez des connaissances de base sur l'utilisation d'un éditeur de code ou d'un IDE. Si ce n'est pas le cas, je vous suggère de consulter ces ressources :

* [Cours intensif sur Visual Studio Code](https://www.youtube.com/watch?v=WPqXP_kLzpo)
* [Comment utiliser CodePen](https://www.freecodecamp.org/news/how-to-use-codepen/)
* [Comment utiliser Replit](https://www.freecodecamp.org/news/how-to-use-replit/)

## Installation du projet

Vous êtes libre de construire ce projet dans votre éditeur de code local préféré, ou via un IDE ou un éditeur en ligne comme [CodePen](https://codepen.io/), [CodeSandbox](https://codesandbox.io/), ou [Replit](https://replit.com/).

Ce projet se composera de trois fichiers : `index.html`, `index.js` et `styles.css`. Puisque ce projet va principalement se concentrer sur JavaScript, j'ai fourni tout le HTML et le CSS dans [ce dépôt GitHub ici](https://github.com/jdwilkin4/leetcode-two-sum-starter-code).

Vous êtes libre de [forker](https://www.freecodecamp.org/news/how-to-fork-a-github-repository/) et [cloner](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) le dépôt, ou vous pouvez copier le code trouvé dans les fichiers HTML et CSS et l'ajouter à votre projet.

Une fois que vous avez configuré votre environnement de projet, vous devriez démarrer le serveur local et voir ce résultat à l'écran :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-19-at-4.18.24-PM.png)
_Styles de visualisation pour le problème Two Sum de Leetcode_

## Comment résoudre le problème Two Sum de LeetCode

Avant de pouvoir construire la visualisation pour ce problème, nous devons d'abord comprendre et résoudre le problème.

### Description

Pour ce problème, vous recevrez une liste de nombres dans n'importe quel ordre et un nombre cible. Le but est de trouver la paire de nombres qui additionnés donnent la cible et de retourner un tableau d'indices pour cette paire de nombres.

Dans cet exemple, nous avons la liste et le nombre cible suivants :

```js
[2,7,11,15]
cible : 9
```

Les nombres 2 et 7 égalent 9, donc nous retournerions `[0,1]` car cela représente les indices où la paire de nombres peut être trouvée dans le tableau.

Pour ce problème, vous pouvez supposer qu'il y aura au moins deux nombres ou plus dans le tableau et qu'il n'y aura qu'une seule solution possible.

Donc, par exemple, vous ne pouvez pas avoir cette entrée qui ne produit aucune solution car il n'y a pas deux nombres dans cette liste qui additionnés donnent la cible.

```js
[1,2,3,4,5]
cible : 55
```

Vous n'aurez pas non plus d'entrée avec plusieurs solutions. L'entrée suivante a deux réponses `[0,1]` et `[1,2]` qui vont à l'encontre des règles de ce problème.

```js
[3,3,3]
cible : 6
```

### Approche par force brute

L'approche la plus intuitive serait de commencer au début de la liste de nombres et de comparer chaque paire possible de nombres jusqu'à ce que nous trouvions la paire qui additionnée donne la cible.

Prenons cet exemple ici :

```js
[11, 15, 2, 7]
cible : 9

```

Nous pouvons commencer avec le premier nombre de la liste (11) et vérifier chaque paire possible pour voir si elle additionnée donne le nombre cible (9).

```
11 + 15 = 9 ? NON
11 + 2 = 9 ? NON
11 + 7 = 9 ? NON
```

Puisque aucune de ces paires n'égale la cible (9), nous passons au deuxième nombre de la liste (15) et vérifions toutes les paires possibles. Il n'est pas nécessaire de vérifier 11+15 car nous l'avons déjà fait plus tôt.

```
15 + 2 = 9 ? NON
15 + 7 = 9 ? NON
```

Puisque aucune de ces paires n'égale la cible (9), nous passons au troisième nombre de la liste (2) et vérifions toutes les paires possibles.

```
2 + 7 = 9 ? OUI !!!
```

Maintenant, nous avons trouvé la paire qui additionnée donne la cible, nous retournerions `[2,3]` car cela représente les indices où la paire de nombres peut être trouvée dans le tableau.

### Solution JavaScript par force brute et complexité temporelle

Cette solution utilise une boucle `for` imbriquée qui aurait une complexité temporelle de O(n²). La boucle externe est utilisée pour obtenir le nombre actuel dans la liste et la boucle interne est utilisée pour vérifier si la somme du nombre actuel et des autres nombres de la liste additionnés donnent la cible.

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function (nums, target) {
  if (nums.length === 2) return [0, 1];

  for (let i = 0; i < nums.length; i++) {
    const currentNum = nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      if (currentNum + nums[j] === target) return [i, j];
    }
  }
};

```

**Note :** J'ai ajouté une vérification supplémentaire dans ma solution pour vérifier si le tableau d'entrée n'a que deux nombres. Dans ce cas, nous retournons immédiatement `[0,1]` car ce sont les seuls indices possibles pour ce cas de test.

```js
 if (nums.length === 2) return [0, 1];
```

Jusqu'à présent, nos tableaux d'entrée ont été très petits. Mais si nous avions un tableau d'entrée de 100, 500 ou 1000+ nombres, cela pourrait prendre un certain temps pour trouver la paire qui additionnée donne la cible.

Dans la section suivante, nous allons examiner une solution qui utilise l'objet `Map` de JavaScript et s'exécute en temps linéaire O(n).

### Approche et solution avec Map

Dans l'approche par force brute, nous avons commencé au début du tableau et comparé toutes les paires possibles de nombres jusqu'à ce que nous trouvions la paire qui additionnée donne la cible. Mais dans cette approche, nous pouvons utiliser l'objet `Map` de JavaScript et une boucle `for` pour trouver cette paire.

L'objet `Map` de JavaScript est une collection de paires clé-valeur qui permet des recherches rapides et dispose de méthodes intégrées comme `set()`, `get()` et `has()`.

Travillons avec le même exemple que précédemment :

```js
[11, 15, 2, 7]
cible : 9

```

Nous pouvons commencer à parcourir le tableau et regarder le nombre actuel dans la liste qui serait `nums[i]`. Nous voulons également créer un nouvel objet `map` qui sera vide au début.

```js
const map = new Map();

for(let i=0; i<nums.length; i++){
    
}
```

À l'intérieur de notre boucle, nous devons calculer la différence qui sera la cible moins le nombre actuel.

```js
    const map = new Map();

    for(let i=0; i<nums.length; i++){
        const difference = target - nums[i]
    }
```

Puisque nous savons qu'il ne peut y avoir que deux nombres qui additionnés donnent la cible, nous pouvons vérifier si la différence est dans la `map`. Si c'est le cas, nous avons trouvé la paire et pouvons retourner les indices. Sinon, nous pouvons ajouter ce nombre actuel à la `map` ainsi que son indice.

```js
    const map = new Map();

    for(let i=0; i < nums.length; i++) {
        const difference = target - nums[i]

        if(map.has(difference)) {
            return [map.get(difference), i]
        } else {
            map.set(nums[i], i)
        }
    }
```

Dans le code suivant, la méthode `has()` est utilisée pour vérifier si la `clé` suivante est dans l'objet `map`. Cette méthode retournera un booléen vrai ou faux.

```js
map.has(difference)
```

La méthode `get()` est utilisée pour retourner cet élément de la `map`.

```js
 if(map.has(difference)) {
   return [map.get(difference), i]
 } 
```

La méthode `set()` ajoutera ou mettra à jour une entrée dans la `map` avec une clé et une valeur.

```js
else {
  map.set(nums[i], i)
}
```

Voici le code complet pour cette approche :

```js
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    if(nums.length === 2) return [0,1]

    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const difference = target - nums[i]

        if (map.has(difference)) {
            return [map.get(difference), i]
        } else {
            map.set(nums[i], i)
        }
    }
    
};
```

### Complexité temporelle pour la solution avec Map

Cette solution aurait une complexité temporelle linéaire O(n). Puisque nous n'utilisons qu'une seule boucle au lieu de deux, nous avons amélioré la complexité temporelle et ne fonctionnons plus en temps quadratique O(n²) comme nous le faisions auparavant.

Dans les prochaines sections, nous allons commencer à construire les visualisations pour chacune de ces approches.

## Aperçu de la visualisation pour Two Sum

Le but de ce projet est de créer des visualisations pour les solutions par map et par force brute.

Pour la solution par force brute, nous montrerons à quoi cela ressemble de parcourir chaque paire de nombres jusqu'à ce que nous trouvions la paire qui additionnée donne la cible.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-20-at-8.43.08-AM.png)
_Visualisation de l'approche par force brute_

Pour la solution avec map, nous montrerons la map en cours de construction et la vérification de la paire qui additionnée donne la cible.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-20-at-8.51.40-AM.png)
_Visualisation de la solution avec map_

## Ajout de la visualisation par force brute

### Création des variables `const` et `let`

Nous devons d'abord créer des variables `const` et leur assigner le résultat de l'accès aux éléments HTML responsables de l'affichage du bouton de solution par force brute et de la sortie.

```js
const bruteForceSolutionBtn = document.getElementById("brute-force-visual-btn");
const bruteForceNumbersOutput = document.querySelector(
  "#brute-force-output > .numbers-array"
);
const bruteForceTextOutput = document.querySelector(
  "#brute-force-output > .result-text"
);

```

L'étape suivante consiste à créer des variables `const` pour le tableau de cas de test et la cible qui seront utilisés pour les deux visualisations.

```js
const testCaseArray = [11, 15, 2, 7];
const target = 9;
```

Ensuite, nous devons créer les variables `let` qui représenteront le nombre actuel que nous examinons dans la boucle externe et le nombre complémentaire que nous examinons dans la boucle interne.

```js
let currentNum;
let currentCompliment;
```

### Création de la fonction `getClassName`

Dans notre visualisation, nous voulons montrer à l'utilisateur la paire actuelle de nombres que nous vérifions en appliquant des bordures de couleurs différentes autour d'eux. Le nombre actuel aura une bordure verte autour de lui et le nombre complémentaire actuel aura une bordure bleue autour de lui.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-20-at-10.02.46-AM.png)

Pour mettre à jour dynamiquement ces styles au fil du temps, nous devons créer une fonction qui sera responsable de l'ajout des classes appropriées au nombre actuel et à son complément.

Commencez par créer une nouvelle fonction `getClassName` qui prend un paramètre `num`.

```js
const getClassName = (num) => {
    
};
```

À l'intérieur de cette fonction, créez une instruction `switch` qui a le `num` pour l'expression que nous vérifions.

```js
const getClassName = (num) => {
  switch (num) {
    
  }
};
```

Le premier `case` doit vérifier `currentNum` et retourner une chaîne pour la classe `current-num`.

```js
const getClassName = (num) => {
  switch (num) {
    case currentNum:
      return "class='current-num'";
  }
};
```

Le deuxième `case` doit vérifier le `currentCompliment` et retourner une chaîne pour la classe `compliment-num`.

```js
const getClassName = (num) => {
  switch (num) {
    case currentNum:
      return "class='current-num'";
    case currentCompliment:
      return "class='compliment-num'";
  }
};
```

Pour le cas `default`, il doit retourner une chaîne vide car nous n'allons pas appliquer de classes pour cet élément.

```js
const getClassName = (num) => {
  switch (num) {
    case currentNum:
      return "class='current-num'";
    case currentCompliment:
      return "class='compliment-num'";
    default:
      return "";
  }
};
```

### Création de la fonction `bruteForceApproach`

Cette fonction sera responsable de l'exécution de la solution par force brute et de l'affichage de la visualisation sur la page.

Nous devons d'abord créer la fonction `bruteForceApproach` qui sera une fonction `async`.

```js
const bruteForceApproach = async () => {

};
```

Ensuite, nous devons ajouter la boucle externe pour notre tableau de cas de test.

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
  
  }
};
```

À l'intérieur de la boucle `for`, mettez à jour le `currentNum` pour lui assigner la valeur du nombre actuel que nous examinons dans le tableau de cas de test.

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
  }
};
```

Ensuite, créez la boucle `for` interne.

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
        
    }
  }
};
```

À l'intérieur de la boucle `for` interne, mettez à jour le nombre `currentCompliment` et assigniez-lui la valeur de `testCaseArray[j]`. Cela est censé représenter chaque nombre à droite du nombre actuel.

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
    }
  }
};
```

Ensuite, nous devons ajouter un `setTimeout` qui retardera les changements visuels apportés au balisage d'une seconde. C'est ce qui va aider à créer l'effet animé de montrer les différentes paires de nombres.

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
      await new Promise((resolve) => setTimeout(resolve, 1000));
    }
  }
};
```

Ensuite, nous devons mettre à jour le HTML pour la sortie. Commencez par assigner le tableau de cas de test à `bruteForceNumbersOutput.innerHTML`.

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
      await new Promise((resolve) => setTimeout(resolve, 1000));

      bruteForceNumbersOutput.innerHTML = testCaseArray;
    }
  }
};
```

Ensuite, nous voulons utiliser la méthode `map` sur le tableau, pour créer un nouveau tableau d'éléments `span` qui représente chaque nombre dans le tableau ainsi que les styles. Nous devons également enchaîner la méthode `join` sur celle-ci pour supprimer les virgules que la méthode `map` ajoute lorsque le nouveau tableau est créé.

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
      await new Promise((resolve) => setTimeout(resolve, 1000));

      bruteForceNumbersOutput.innerHTML = testCaseArray
        .map(
          (num, index) =>
            `
            <span ${getClassName(num)}>
            ${testCaseArray[index]}
            </span>
          `
        )
        .join("");
    }
  }
};
```

Si nous ne trouvons pas de paire qui additionnée donne la cible, alors nous voulons afficher un message à l'utilisateur. Mettez à jour le contenu textuel pour `bruteForceTextOutput` et assigniez-lui le message suivant :

```js
const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
      await new Promise((resolve) => setTimeout(resolve, 1000));

      bruteForceNumbersOutput.innerHTML = testCaseArray
        .map(
          (num, index) =>
            `
            <span ${getClassName(num)}>
            ${testCaseArray[index]}
            </span>
          `
        )
        .join("");

      bruteForceTextOutput.textContent = `La somme de ${currentNum} + ${currentCompliment} est-elle égale à ${target} ? NON !`;
    }
  }
};
```

La dernière partie consiste à ajouter une condition qui vérifie si nous avons trouvé la paire de nombres qui additionnée donne la cible. Si c'est le cas, alors nous pouvons afficher ce tableau d'indices final et `retourner` de la fonction.

```js
  if (currentNum + currentCompliment === target) {
      bruteForceTextOutput.textContent = `Indices finaux : [${i}, ${j}]`;
      return;
  }
```

Pour tester la visualisation par force brute, nous devons ajouter un écouteur d'événement au `bruteForceSolutionBtn`. L'écouteur d'événement doit écouter un événement `"click"` et doit référencer la fonction `bruteForceApproach`.

```js
bruteForceSolutionBtn.addEventListener("click", bruteForceApproach);

```

Voici votre code complet jusqu'à présent :

```js
const bruteForceSolutionBtn = document.getElementById("brute-force-visual-btn");
const bruteForceNumbersOutput = document.querySelector(
  "#brute-force-output > .numbers-array"
);
const bruteForceTextOutput = document.querySelector(
  "#brute-force-output > .result-text"
);
const testCaseArray = [11, 15, 2, 7];
const target = 9;
let currentNum;
let currentCompliment;

const getClassName = (num) => {
  switch (num) {
    case currentNum:
      return "class='current-num'";
    case currentCompliment:
      return "class='compliment-num'";
    default:
      return "";
  }
};

const bruteForceApproach = async () => {
  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
      await new Promise((resolve) => setTimeout(resolve, 1000));

      bruteForceNumbersOutput.innerHTML = testCaseArray
        .map(
          (num, index) =>
            `
            <span ${getClassName(num)}>
            ${testCaseArray[index]}
            </span>
          `
        )
        .join("");

      bruteForceTextOutput.textContent = `La somme de ${currentNum} + ${currentCompliment} est-elle égale à ${target} ? NON !`;

      if (currentNum + currentCompliment === target) {
        bruteForceTextOutput.textContent = `Indices finaux : [${i}, ${j}]`;
        return;
      }
    }
  }
};

bruteForceSolutionBtn.addEventListener("click", bruteForceApproach);

```

Essayez votre visualisation en cliquant sur le bouton "Show Visualization" pour l'approche par force brute.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-20-at-10.42.51-AM.png)
_Résultat du clic sur le bouton "show visualization" pour l'approche par force brute_

## Comment désactiver le bouton `bruteForceSolutionBtn` lorsque l'animation est en cours

Si vous essayez de cliquer sur le bouton `bruteForceSolutionBtn` plusieurs fois de suite, vous verrez des bugs dans l'animation. Pour corriger cela, nous devons désactiver le bouton lorsque l'animation est en cours et le réactiver lorsque l'animation est terminée.

À l'intérieur de la fonction `bruteForceApproach`, définissez l'attribut disabled pour le bouton `bruteForceSolutionBtn`.

```js
const bruteForceApproach = async () => {
  bruteForceSolutionBtn.setAttribute("disabled", "");
```

À l'intérieur de l'instruction `if`, supprimez l'attribut disabled pour le bouton `bruteForceSolutionBtn`.

```js
   if (currentNum + currentCompliment === target) {
        bruteForceTextOutput.textContent = `Indices finaux : [${i}, ${j}]`;
        bruteForceSolutionBtn.removeAttribute("disabled");
        return;
   }
```

Voici le code complet avec la correction :

```js
const bruteForceSolutionBtn = document.getElementById("brute-force-visual-btn");
const bruteForceNumbersOutput = document.querySelector(
  "#brute-force-output > .numbers-array"
);
const bruteForceTextOutput = document.querySelector(
  "#brute-force-output > .result-text"
);
const testCaseArray = [11, 15, 2, 7];
const target = 9;
let currentNum;
let currentCompliment;

const getClassName = (num) => {
  switch (num) {
    case currentNum:
      return "class='current-num'";
    case currentCompliment:
      return "class='compliment-num'";
    default:
      return "";
  }
};

const bruteForceApproach = async () => {
  bruteForceSolutionBtn.setAttribute("disabled", "");

  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
      await new Promise((resolve) => setTimeout(resolve, 1000));

      bruteForceNumbersOutput.innerHTML = testCaseArray
        .map(
          (num, index) =>
            `
            <span ${getClassName(num)}>
            ${testCaseArray[index]}
            </span>
          `
        )
        .join("");

      bruteForceTextOutput.textContent = `La somme de ${currentNum} + ${currentCompliment} est-elle égale à ${target} ? NON !`;

      if (currentNum + currentCompliment === target) {
        bruteForceTextOutput.textContent = `Indices finaux : [${i}, ${j}]`;
        bruteForceSolutionBtn.removeAttribute("disabled");
        return;
      }
    }
  }
};

bruteForceSolutionBtn.addEventListener("click", bruteForceApproach);

```

Essayez à nouveau la visualisation, et maintenant vous devriez voir que le bouton est désactivé lorsque l'animation est en cours.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-20-at-10.56.36-AM.png)
_Image montrant comment le bouton est désactivé lorsque l'animation est en cours_

## Ajout de la visualisation de la solution avec Map

### Création des variables `const`

Nous allons créer de nouvelles variables `const` qui représentent l'élément bouton de solution optimale, la sortie et les éléments de tableau pour l'animation.

```js
const optimalSolutionBtn = document.getElementById("optimal-visual-btn");
const currentValueOutput = document.getElementById("current-value-output");
const finalOptimalSolutionResult = document.getElementById(
  "final-optimal-result"
);
const table = document.getElementById("table-output");
const tableBodyOutput = document.getElementById("map-table-body");
```

Voici la liste complète des déclarations de variables pour les deux visualisations :

```js
const bruteForceSolutionBtn = document.getElementById("brute-force-visual-btn");
const bruteForceNumbersOutput = document.querySelector(
  "#brute-force-output > .numbers-array"
);
const bruteForceTextOutput = document.querySelector(
  "#brute-force-output > .result-text"
);
const optimalSolutionBtn = document.getElementById("optimal-visual-btn");
const currentValueOutput = document.getElementById("current-value-output");
const finalOptimalSolutionResult = document.getElementById(
  "final-optimal-result"
);
const table = document.getElementById("table-output");
const tableBodyOutput = document.getElementById("map-table-body");

const testCaseArray = [11, 15, 2, 7];
const target = 9;
let currentNum;
let currentCompliment;
```

### Création de la fonction asynchrone `optimalApproach`

La première étape consiste à créer la nouvelle fonction `optimalApproach` qui sera une fonction `async`. Vous pouvez l'ajouter en dessous de votre fonction `bruteForceApproach`.

```js
const optimalApproach = async () => {
    
};
```

Tout comme la fonction `bruteForceApproach`, nous voulons désactiver le bouton lorsque l'animation commence pour empêcher les utilisateurs de cliquer dessus plusieurs fois et de casser l'animation.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
};
```

Lorsque la page se charge pour la première fois, le tableau est masqué par défaut. Nous voulons afficher l'élément tableau lorsque l'animation commence.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
};
```

Chaque fois que nous exécutons cette animation, nous voulons afficher des messages à l'utilisateur pour savoir si nous avons trouvé la bonne paire ou non. Au début de l'animation, nous voulons effacer la sortie précédente.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
};
```

Ensuite, nous devons créer un objet `map` vide qui sera éventuellement mis à jour au fil du temps dans la boucle `for`.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
  const map = new Map();
};
```

Ensuite, nous devons créer une boucle `for` qui sera responsable de la boucle à travers chaque nombre dans le tableau et de la mise à jour de l'animation au fil du temps.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
  const map = new Map();

  for (let i = 0; i < testCaseArray.length; ++i) {
    
  }
};
```

À l'intérieur de la boucle, nous devons ajouter l'expression pour calculer la différence.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
  const map = new Map();

  for (let i = 0; i < testCaseArray.length; ++i) {
    const difference = target - testCaseArray[i];
  }
};
```

Ensuite, nous devons ajouter un `setTimeout` qui retardera les changements de 2 secondes dans le balisage HTML et aidera à l'effet d'animation.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
  const map = new Map();

  for (let i = 0; i < testCaseArray.length; ++i) {
    const difference = target - testCaseArray[i];

    await new Promise((resolve) => setTimeout(resolve, 2000));
  }
};
```

Nous devons ensuite ajouter une instruction `if` pour vérifier si la map contient la valeur de différence.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
  const map = new Map();

  for (let i = 0; i < testCaseArray.length; ++i) {
    const difference = target - testCaseArray[i];

    await new Promise((resolve) => setTimeout(resolve, 2000));

    if (map.has(difference)) {
        
    }
  }
};
```

À l'intérieur de l'instruction `if`, nous devons mettre à jour le contenu textuel pour afficher le résultat final du tableau d'indices à l'écran. Nous utiliserons la méthode `get` pour obtenir la valeur d'indice de la `map`.

```js
 if (map.has(difference)) {
      finalOptimalSolutionResult.textContent = `Indices finaux : [${map.get(
        difference
      )}, ${i}]`;
 }
```

Nous devons également mettre à jour la sortie pour afficher un message indiquant que nous avons trouvé la paire de nombres qui additionnés donnent la cible.

```js
  if (map.has(difference)) {
      finalOptimalSolutionResult.textContent = `Indices finaux : [${map.get(
        difference
      )}, ${i}]`;
      currentValueOutput.innerHTML = `
      <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
      <p>La différence(${difference}) est-elle dans notre map ? OUI, nous avons trouvé cette paire de nombres qui additionnés donnent la cible.</p>
    `;
  }
```

Nous devons également supprimer l'attribut disabled du bouton `optimalSolutionBtn` et retourner de la fonction.

```js
  if (map.has(difference)) {
      finalOptimalSolutionResult.textContent = `Indices finaux : [${map.get(
        difference
      )}, ${i}]`;
      currentValueOutput.innerHTML = `
      <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
      <p>La différence(${difference}) est-elle dans notre map ? OUI, nous avons trouvé cette paire de nombres qui additionnés donnent la cible.</p>
    `;
      optimalSolutionBtn.removeAttribute("disabled");
      return;
  }
```

Si la paire n'a pas été trouvée, alors nous devons ajouter une clause `else`.

```js
  if (map.has(difference)) {
      finalOptimalSolutionResult.textContent = `Indices finaux : [${map.get(
        difference
      )}, ${i}]`;
      currentValueOutput.innerHTML = `
      <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
      <p>La différence(${difference}) est-elle dans notre map ? OUI, nous avons trouvé cette paire de nombres qui additionnés donnent la cible.</p>
    `;
      optimalSolutionBtn.removeAttribute("disabled");
      return;
  } else {
        
  }
```

À l'intérieur de la clause `else`, nous devons mettre à jour le message pour montrer que nous n'avons pas trouvé la paire et que le nombre actuel `testCaseArray[i]` va être ajouté à la `map` ainsi que sa valeur d'indice.

```js
else {
      currentValueOutput.innerHTML = `
        <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
        <p>La différence(${difference}) est-elle dans notre map ? Non.</p>
        <p>Ajoutez le nombre actuel ${testCaseArray[i]} à notre map.</p>
      `;
}
```

Nous devons ensuite mettre à jour la sortie du tableau avec le nombre actuel et sa valeur d'indice.

```js
else {
      currentValueOutput.innerHTML = `
        <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
        <p>La différence(${difference}) est-elle dans notre map ? Non.</p>
        <p>Ajoutez le nombre actuel ${testCaseArray[i]} à notre map.</p>
      `;
      tableBodyOutput.innerHTML += `
      <tr>
        <td>${testCaseArray[i]}</td>
        <td>${i}</td>
      </tr>
    `;
}
```

Enfin, utilisez la méthode `set` pour définir le nombre actuel et la valeur d'indice dans la `map`.

```js
else {
      currentValueOutput.innerHTML = `
        <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
        <p>La différence(${difference}) est-elle dans notre map ? Non.</p>
        <p>Ajoutez le nombre actuel ${testCaseArray[i]} à notre map.</p>
      `;
      tableBodyOutput.innerHTML += `
      <tr>
        <td>${testCaseArray[i]}</td>
        <td>${i}</td>
      </tr>
    `;
      map.set(testCaseArray[i], i);
}
```

Voici le code complet pour votre fonction `optimalApproach`.

```js
const optimalApproach = async () => {
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
  const map = new Map();

  for (let i = 0; i < testCaseArray.length; ++i) {
    const difference = target - testCaseArray[i];

    await new Promise((resolve) => setTimeout(resolve, 2000));

    if (map.has(difference)) {
      finalOptimalSolutionResult.textContent = `Indices finaux : [${map.get(
        difference
      )}, ${i}]`;
      currentValueOutput.innerHTML = `
      <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
      <p>La différence(${difference}) est-elle dans notre map ? OUI, nous avons trouvé cette paire de nombres qui additionnés donnent la cible.</p>
    `;
      optimalSolutionBtn.removeAttribute("disabled");
      return;
    } else {
      currentValueOutput.innerHTML = `
        <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
        <p>La différence(${difference}) est-elle dans notre map ? Non.</p>
        <p>Ajoutez le nombre actuel ${testCaseArray[i]} à notre map.</p>
      `;
      tableBodyOutput.innerHTML += `
      <tr>
        <td>${testCaseArray[i]}</td>
        <td>${i}</td>
      </tr>
    `;
      map.set(testCaseArray[i], i);
    }
  }
};
```

Pour tester cette visualisation, ajoutez un écouteur d'événement au bouton `optimalSolutionBtn` et passez l'événement `"click"` et la référence de la fonction `optimalApproach`.

```js
optimalSolutionBtn.addEventListener("click", optimalApproach);

```

Lorsque vous cliquez sur le bouton "Show Visualization" pour la solution avec map, vous devriez voir l'animation, comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-20-at-12.05.05-PM.png)
_Visualisation pour la solution avec map_

## Comment réinitialiser la sortie du tableau pour la solution avec Map

Si vous essayez d'exécuter l'animation plusieurs fois, vous verrez que le tableau montre les résultats de l'exécution précédente.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/Screenshot-2023-11-20-at-12.09.35-PM.png)
_Tableau montrant les résultats de l'exécution précédente_

Pour corriger cela, nous pouvons réinitialiser le tableau avant chaque exécution de l'animation. Commencez par créer une fonction `resetTable` au-dessus de votre fonction `optimalApproach`.

```js
const resetTable = () => {
    
};

const optimalApproach = async () => {
    .........
```

À l'intérieur de cette fonction, effacez le tableau et les résultats textuels finaux.

```js
const resetTable = () => {
  tableBodyOutput.innerHTML = "";
  finalOptimalSolutionResult.textContent = "";
};
```

Appelez la fonction `resetTable` à l'intérieur de votre fonction `optimalApproach` afin de voir les résultats de la réinitialisation du tableau.

```js
const optimalApproach = async () => {
  resetTable();
  optimalSolutionBtn.setAttribute("disabled", "");
    ...........
```

Testez à nouveau votre animation, et maintenant vous devriez voir que les résultats du tableau sont réinitialisés avant chaque nouvelle exécution de l'animation.

## Code final de la solution et exemple en direct

Voici le code JavaScript complet pour les deux visualisations :

```js
const bruteForceSolutionBtn = document.getElementById("brute-force-visual-btn");
const bruteForceNumbersOutput = document.querySelector(
  "#brute-force-output > .numbers-array"
);
const bruteForceTextOutput = document.querySelector(
  "#brute-force-output > .result-text"
);
const optimalSolutionBtn = document.getElementById("optimal-visual-btn");
const currentValueOutput = document.getElementById("current-value-output");
const finalOptimalSolutionResult = document.getElementById(
  "final-optimal-result"
);
const table = document.getElementById("table-output");
const tableBodyOutput = document.getElementById("map-table-body");

const testCaseArray = [11, 15, 2, 7];
const target = 9;
let currentNum;
let currentCompliment;

const getClassName = (num) => {
  switch (num) {
    case currentNum:
      return "class='current-num'";
    case currentCompliment:
      return "class='compliment-num'";
    default:
      return "";
  }
};

const bruteForceApproach = async () => {
  bruteForceSolutionBtn.setAttribute("disabled", "");

  for (let i = 0; i < testCaseArray.length; ++i) {
    currentNum = testCaseArray[i];
    for (let j = i + 1; j < testCaseArray.length; ++j) {
      currentCompliment = testCaseArray[j];
      await new Promise((resolve) => setTimeout(resolve, 1000));

      bruteForceNumbersOutput.innerHTML = testCaseArray
        .map(
          (num, index) =>
            `
              <span ${getClassName(num)}>
              ${testCaseArray[index]}
              </span>
            `
        )
        .join("");

      bruteForceTextOutput.textContent = `La somme de ${currentNum} + ${currentCompliment} est-elle égale à ${target} ? NON !`;

      if (currentNum + currentCompliment === target) {
        bruteForceTextOutput.textContent = `Indices finaux : [${i}, ${j}]`;
        bruteForceSolutionBtn.removeAttribute("disabled");
        return;
      }
    }
  }
};

const resetTable = () => {
  tableBodyOutput.innerHTML = "";
  finalOptimalSolutionResult.textContent = "";
};

const optimalApproach = async () => {
  resetTable();
  optimalSolutionBtn.setAttribute("disabled", "");
  table.style.display = "block";
  currentValueOutput.innerHTML = "";
  const map = new Map();

  for (let i = 0; i < testCaseArray.length; ++i) {
    const difference = target - testCaseArray[i];

    await new Promise((resolve) => setTimeout(resolve, 2000));

    if (map.has(difference)) {
      finalOptimalSolutionResult.textContent = `Indices finaux : [${map.get(
        difference
      )}, ${i}]`;
      currentValueOutput.innerHTML = `
      <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
      <p>La différence(${difference}) est-elle dans notre map ? OUI, nous avons trouvé cette paire de nombres qui additionnés donnent la cible.</p>
    `;
      optimalSolutionBtn.removeAttribute("disabled");
      return;
    } else {
      currentValueOutput.innerHTML = `
        <p>Différence(${difference}) = cible(${target}) - nombre actuel(${testCaseArray[i]})</p>
        <p>La différence(${difference}) est-elle dans notre map ? Non.</p>
        <p>Ajoutez le nombre actuel ${testCaseArray[i]} à notre map.</p>
      `;
      tableBodyOutput.innerHTML += `
        <tr>
          <td>${testCaseArray[i]}</td>
          <td>${i}</td>
        </tr>
      `;
      map.set(testCaseArray[i], i);
    }
  }
};

bruteForceSolutionBtn.addEventListener("click", bruteForceApproach);
optimalSolutionBtn.addEventListener("click", optimalApproach);

```

Voici un [lien](https://codepen.io/Jessica-Wilkins-the-decoder/full/eYxVyKN) vers le résultat final en direct sur CodePen.

## Conclusion

J'espère que vous avez apprécié ce projet et que vous en avez appris un peu plus sur le fonctionnement du problème Two Sum.

Je vous encourage à jouer avec le projet et peut-être à ajouter de nouvelles fonctionnalités par vous-même, comme tester différents nombres ou demander des entrées utilisateur pour le tableau de nombres et les cibles. 👍🏾