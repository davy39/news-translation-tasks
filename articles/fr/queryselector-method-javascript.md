---
title: Qu'est-ce que la méthode querySelector() et comment fonctionne-t-elle en JavaScript
  ?
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-12T23:00:54.000Z'
originalURL: https://freecodecamp.org/news/queryselector-method-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/fili-santillan-qp51FQhBnS0-unsplash.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Qu'est-ce que la méthode querySelector() et comment fonctionne-t-elle en
  JavaScript ?
seo_desc: 'In JavaScript, there will be times when you need to access an HTML element.
  The querySelector method is a web API that selects the first element that matches
  the specified CSS selector passed into it.

  But how does this work in more detail? In this ar...'
---

En JavaScript, il y aura des moments où vous devrez accéder à un élément HTML. La méthode `querySelector` est une API web qui sélectionne le premier élément correspondant au sélecteur CSS spécifié qui lui est passé.

Mais comment cela fonctionne-t-il plus en détail ? Dans cet article, nous examinerons plusieurs exemples sur la façon d'utiliser la méthode `querySelector` ainsi que la méthode `querySelectorAll`.

## Syntaxe de base pour la méthode `querySelector()`

La méthode `querySelector` est appelée sur l'objet `document` et prend en argument le sélecteur CSS de l'élément que vous souhaitez sélectionner.

```js
document.querySelector(selector);
```

Si le sélecteur correspond à un élément dans le document, la méthode retournera le premier élément correspondant. S'il n'y a pas de correspondances, la méthode retournera `null`.

## Comment utiliser la méthode `querySelector()` avec les sélecteurs de type

Un sélecteur de type en CSS fait référence au nom d'un élément HTML. Des exemples de cela seraient `button`, `div`, `p`, et ainsi de suite.

Dans cet exemple, nous avons un élément bouton dans le document HTML.

```html
<button>Afficher l'alerte</button>
```

Si nous voulions accéder à cet élément dans notre fichier JavaScript, nous pourrions utiliser la méthode `querySelector` comme ceci :

```js
const buttonElement = document.querySelector("button");
```

Cette ligne de code sélectionne le premier bouton qu'elle voit sur la page et assigne ce résultat à une variable `const` appelée `buttonElement`.

Si nous enregistrons cette variable `buttonElement` dans la console, voici ce que cela donnerait :

```js
console.log(buttonElement);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-11-at-3.11.37-PM.png)
_sortie de console.log pour l'exemple querySelector_

Nous pouvons utiliser cette variable `buttonElement` et ajouter un écouteur d'événement pour afficher une `alerte` lorsque le bouton est cliqué.

```js
buttonElement.addEventListener("click", () => {
  alert("Le bouton a été cliqué !");
});
```

Voici le code complet et un exemple interactif avec lequel jouer.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/ZEPqwBg]

## Comment utiliser la méthode `querySelector()` avec les sélecteurs de classe

Un sélecteur de classe en CSS fait référence au nom d'une classe utilisée dans un élément HTML. Des exemples de cela seraient `.container`, `.button`, et ainsi de suite.

Supposons que nous voulons créer un jeu de solitaire et que nous voulons masquer/afficher les règles du jeu lorsqu'un bouton est cliqué. Nous pourrions utiliser la méthode `querySelector` pour sélectionner le bouton et le conteneur des règles.

Voici le HTML de départ :

```html
<h1>Jouons au solitaire !</h1>
<main>
  <button class="rules-btn">Afficher les règles</button>
  <section class="rules-container">
    <h2>Règles du jeu</h2>
    <ul>
      <li>Il y a 7 colonnes de cartes</li>
      <li>La première colonne a 1 carte, la deuxième en a 2, la troisième en a 3, et ainsi de suite</li>
      <li>La première carte de chaque colonne est face visible, le reste est face cachée</li>
      <li>Déplacez les cartes pour construire 4 piles de cartes dans l'ordre ascendant</li>
      <li>Commencez avec les as et construisez jusqu'aux rois</li>
      <li>Déplacez les cartes en les glissant et en les déposant</li>
    </ul>
  </section>
</main>
```

Dans le fichier JavaScript, nous pouvons utiliser la méthode `querySelector` pour sélectionner le bouton des règles et le conteneur des règles.

```js
const rulesBtn = document.querySelector(".rules-btn");
const rulesContainer = document.querySelector(".rules-container");
```

Nous pouvons ensuite ajouter un écouteur d'événement à la variable `rulesBtn` pour afficher/masquer le conteneur des règles lorsque le bouton est cliqué. Nous utilisons la propriété `classList` pour basculer la classe `"show"` sur l'élément du conteneur des règles.

```js
rulesBtn.addEventListener("click", () => {
  rulesContainer.classList.toggle("show");
});
```

Voici un exemple interactif où vous pouvez voir le conteneur des règles s'afficher et se masquer lorsque le bouton est cliqué.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/LYagqMj]

Bien que le basculement fonctionne ici, il y a un petit bug dans le code. Par défaut, les règles seront masquées et le texte du bouton dit "Afficher les règles". Lorsque les règles sont affichées, le texte du bouton devrait changer pour "Masquer les règles", mais ce n'est pas le cas pour le moment.

Dans l'écouteur d'événement, nous pouvons mettre à jour le contenu textuel du bouton pour afficher "Masquer les règles" lorsque les règles sont affichées et "Afficher les règles" lorsque les règles sont masquées.

```js
rulesBtn.textContent = rulesContainer.classList.contains("show")
  ? "Masquer les règles"
  : "Afficher les règles";
```

Maintenant, le texte du bouton changera en fonction de l'état du conteneur des règles. Voici le code JavaScript complet :

```js
const rulesBtn = document.querySelector(".rules-btn");
const rulesContainer = document.querySelector(".rules-container");

rulesBtn.addEventListener("click", () => {
  rulesContainer.classList.toggle("show");
  rulesBtn.textContent = rulesContainer.classList.contains("show")
    ? "Masquer les règles"
    : "Afficher les règles";
});
```

Voici l'exemple interactif avec le code JavaScript mis à jour.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/LYagqoz]

## Comment utiliser la méthode `querySelectorAll()`

La méthode `querySelectorAll` est similaire à la méthode `querySelector`, mais au lieu de retourner le premier élément correspondant, elle retourne une `NodeList` de tous les éléments correspondants. Une `NodeList` est un objet de type tableau qui contient tous les éléments correspondant au sélecteur spécifié.

Dans cet exemple, nous avons une liste non ordonnée de sports et nous voulons générer des couleurs de fond aléatoires pour chaque élément de la liste.

Voici le HTML de départ :

```html
<button class="btn">Générer des couleurs de fond aléatoires</button>
<ul class="sports-list">
  <li>Football</li>
  <li>Basketball</li>
  <li>Tennis</li>
  <li>Golf</li>
  <li>Natation</li>
</ul>
```

Pour sélectionner tous les éléments de la liste dans la liste non ordonnée, nous pouvons utiliser la méthode `querySelectorAll` comme ceci :

```js
const sportsList = document.querySelectorAll(".sports-list li");
```

Si nous enregistrons la variable `sportsList` dans la console, voici ce que cela donnerait :

```js
console.log(sportsList);
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-11-at-6.10.19-PM.png)
_Exemple de NodeList_

Nous devons ensuite utiliser la méthode `querySelector` pour sélectionner le bouton.

```js
const randomColorBtn = document.querySelector(".btn");
```

Ensuite, nous pouvons créer une liste aléatoire de couleurs.

```js
const lightColorsArr = [
  "#FFDAB9",
  "#FFE4B5",
  "#FFFFE0",
  "#FAFAD2",
  "#F0FFF0",
  "#E0FFFF",
  "#AFEEEE",
  "#00CED1",
  "#00BFFF",
  "#1E90FF",
  "#ADD8E6",
  "#7FFFD4",
  "#7CFC00",
  "#7FFF00",
  "#32CD32",
  "#ADFF2F",
  "#FFFF00",
  "#FFD700",
  "#FFA500",
  "#FF6347",
];
```

Chaque fois que l'utilisateur clique sur le bouton, nous voulons mélanger la liste des couleurs et sélectionner 5 couleurs claires aléatoires dans le tableau. Nous pouvons utiliser l'algorithme de mélange de Fisher-Yates (https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle) pour mélanger le tableau, ce qui est une méthode courante pour mélanger un tableau en JavaScript.

```js
function shuffleArray(arr) {
  let currentIndex = arr.length;
  let randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [arr[currentIndex], arr[randomIndex]] = [
      arr[randomIndex],
      arr[currentIndex],
    ];
  }

  return arr;
}
```

Ensuite, nous pouvons ajouter un écouteur d'événement au bouton et mélanger le tableau.

```js
randomColorBtn.addEventListener("click", () => {
  const shuffledColors = shuffleArray(lightColorsArr);
});
```

Pour chaque élément de la liste, nous pouvons définir la couleur de fond sur une couleur aléatoire du tableau mélangé.

```js
sportsList.forEach((list, index) => {
  list.style.backgroundColor = shuffledColors[index];
});
```

Voici le code complet :

```js
const sportsList = document.querySelectorAll(".sports-list li");
const randomColorBtn = document.querySelector(".btn");

console.log(sportsList);

const lightColorsArr = [
  "#FFDAB9",
  "#FFE4B5",
  "#FFFFE0",
  "#FAFAD2",
  "#F0FFF0",
  "#E0FFFF",
  "#AFEEEE",
  "#00CED1",
  "#00BFFF",
  "#1E90FF",
  "#ADD8E6",
  "#7FFFD4",
  "#7CFC00",
  "#7FFF00",
  "#32CD32",
  "#ADFF2F",
  "#FFFF00",
  "#FFD700",
  "#FFA500",
  "#FF6347",
];

// algorithme de mélange de Fisher-Yates

function shuffleArray(arr) {
  let currentIndex = arr.length;
  let randomIndex;

  while (currentIndex !== 0) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    [arr[currentIndex], arr[randomIndex]] = [
      arr[randomIndex],
      arr[currentIndex],
    ];
  }

  return arr;
}

randomColorBtn.addEventListener("click", () => {
  const shuffledColors = shuffleArray(lightColorsArr);

  sportsList.forEach((list, index) => {
    list.style.backgroundColor = shuffledColors[index];
  });
});

```

Voici l'exemple interactif avec le code JavaScript complet. Cliquez sur le bouton et vous verrez les éléments de la liste changer pour des couleurs de fond aléatoires.

%[https://codepen.io/Jessica-Wilkins-the-flexboxer/pen/dyrgrOK]

## Conclusion

Les méthodes `querySelector` et `querySelectorAll` sont des API web utiles qui vous permettent d'accéder aux éléments du DOM. Vous pouvez utiliser ces méthodes pour sélectionner des éléments par type, classe, id, attribut, pseudo-classe et sélecteurs de pseudo-élément.

Je vous suggère d'expérimenter avec ces méthodes et de voir ce que vous pouvez créer dans vos propres projets.

J'espère que vous avez trouvé cet article utile et informatif. Bon codage !