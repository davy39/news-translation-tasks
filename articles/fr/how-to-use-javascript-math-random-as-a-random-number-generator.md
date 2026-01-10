---
title: Comment utiliser JavaScript Math.random() comme générateur de nombres aléatoires
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-08-24T20:41:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-javascript-math-random-as-a-random-number-generator
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c990f740569d1a4ca1d9d.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
seo_title: Comment utiliser JavaScript Math.random() comme générateur de nombres aléatoires
seo_desc: "By Vijit Ail\nOften while developing projects, you will find yourself looking\
  \ for ways to generate random numbers. \nThe most common use cases for generating\
  \ random numbers are games of chance like rolling dice, shuffling playing cards,\
  \ and spinning ro..."
---

Par Vijit Ail

Souvent, lors du développement de projets, vous vous retrouverez à chercher des moyens de générer des nombres aléatoires. 

Les cas d'utilisation les plus courants pour la génération de nombres aléatoires sont les jeux de hasard comme le lancer de dés, le mélange de cartes à jouer et la rotation de roues de roulette.

Dans ce guide, vous apprendrez à générer un nombre aléatoire en utilisant la méthode `Math.random()` en construisant un mini-jeu de dés.

## La méthode Math.random()

L'objet `Math` en JavaScript est un objet intégré qui possède des propriétés et des méthodes pour effectuer des calculs mathématiques. 

Une utilisation courante de l'objet `Math` est de créer un nombre aléatoire en utilisant la méthode `random()`.

```js
const randomValue = Math.random();
```

Mais la méthode `Math.random()` ne retourne pas réellement un nombre entier. Au lieu de cela, elle retourne une valeur à virgule flottante entre 0 (inclus) et 1 (exclus). Notez également que la valeur retournée par `Math.random()` est de nature pseudo-aléatoire. 

Les nombres aléatoires générés par `Math.random()` peuvent sembler aléatoires, mais ces nombres se répéteront et finiront par afficher un motif non aléatoire sur une période de temps. 

C'est parce que la génération algorithmique de nombres aléatoires ne peut jamais être véritablement aléatoire par nature. C'est pourquoi nous les appelons des générateurs de nombres pseudo-aléatoires (PRNG).

Pour en savoir plus sur la méthode `Math.random()`, vous pouvez consulter [ce](https://www.freecodecamp.org/news/javascript-math-random-method-explained/) guide.

## Fonction de génération de nombres aléatoires

Maintenant, utilisons la méthode `Math.random()` pour créer une fonction qui retournera un entier aléatoire entre deux valeurs (incluses).

```js
const getRandomNumber = (min, max) => {
  return Math.floor(Math.random() * (max - min + 1)) + min;
};
```

Décomposons la logique ici.

La méthode `Math.random()` retournera un nombre à virgule flottante entre 0 et 1 (exclus). 

Ainsi, les intervalles seraient les suivants :

```
[0 .................................... 1)

[min .................................... max)
```

Pour factoriser le deuxième intervalle, soustrayez min des deux extrémités. Cela vous donnera un intervalle entre 0 et `max-min`.

```
[0 .................................... 1)

[0 .................................... max - min)
```

Ainsi, pour obtenir une valeur aléatoire, vous feriez ce qui suit :

```
const x = Math.random() * (max - min)
```

Ici, `x` est la valeur aléatoire.

Actuellement, `max` est exclu de l'intervalle. Pour le rendre inclusif, ajoutez 1. De plus, vous devez ajouter le `min` que vous avez soustrait précédemment pour obtenir une valeur entre `[min, max)`.

```js
const x = Math.random() * (max - min + 1) + min
```

Très bien, donc la dernière étape restante est de s'assurer que `x` est toujours un entier.

```js
const x = Math.floor(Math.random() * (max - min + 1)) + min
```

Vous pourriez utiliser la méthode `Math.round()` au lieu de `floor()`, mais cela vous donnerait une distribution non uniforme. Cela signifie que `max` et `min` auront chacun une chance sur deux de sortir comme résultat. L'utilisation de `Math.floor()` vous donnera une distribution parfaitement uniforme.

Maintenant que vous avez une bonne compréhension de la manière dont fonctionne la génération aléatoire, utilisons cette fonction pour simuler le lancer de dés.

## Le jeu de dés

Dans cette section, nous allons créer un mini-jeu de dés vraiment simple. Deux joueurs entrent leur nom et lancent les dés. Le joueur dont le dé a un nombre plus élevé gagne la manche. 

Tout d'abord, créez une fonction `rollDice` qui simule l'action de lancer les dés. 

À l'intérieur du corps de la fonction, appelez la fonction `getRandomNumber()` avec `1` et `6` comme arguments. Cela vous donnera un nombre aléatoire entre 1 et 6 (les deux inclus), tout comme le fonctionnement des dés réels. 

```js
const rollDice = () => getRandomNumber(1, 6);
```

Ensuite, créez deux champs de saisie et un bouton comme indiqué ci-dessous :

```html
<div id="app">
      <div>
        <input id="player1" placeholder="Entrez le nom du Joueur 1" />
      </div>
      <div>
        <input id="player2" placeholder="Entrez le nom du Joueur 2" />
      </div>
      <button id="roll">Lancer les dés</button>
      <div id="results"></div>
    </div>
```

Lorsque le bouton 'Lancer les dés' est cliqué, récupérez les noms des joueurs à partir des champs de saisie et appelez la fonction `rollDice()` pour chaque joueur.

```js
const getRandomNumber = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;


const rollDice = () => getRandomNumber(1, 6);

document.getElementById("roll").addEventListener("click", function () {
  // récupérer les noms des joueurs à partir des champs de saisie
  const player1 = document.getElementById("player1").value;
  const player2 = document.getElementById("player2").value;

  // lancer les dés pour les deux joueurs
  const player1Score = rollDice();
  const player2Score = rollDice();

  // initialiser une chaîne vide pour stocker le résultat
  let result = "";

  // déterminer le résultat
  if (player1Score > player2Score) {
    result = `${player1} a gagné la manche`;
  } else if (player2Score > player1Score) {
    result = `${player2} a gagné la manche`;
  } else {
    result = "Cette manche est un match nul";
  }

  // afficher le résultat sur la page
  document.getElementById("results").innerHTML = `
  <p>${player1} => ${player1Score}</p>
  <p>${player2} => ${player2Score}</p>
  <p>${result}</p>
  `;
});

```

Vous pouvez valider les champs de noms des joueurs et embellir le balisage avec un peu de CSS. Dans un souci de concision, je le garde simple pour ce guide.

C'est tout. Vous pouvez consulter la démonstration [ici](https://5zmdd.csb.app/).

## Conclusion

Ainsi, la génération de nombres aléatoires en JavaScript n'est pas si aléatoire après tout. Tout ce que nous faisons, c'est prendre des nombres en entrée, utiliser un peu de Math, et produire un nombre pseudo-aléatoire. 

Pour la plupart des applications et des jeux basés sur un navigateur, cette quantité d'aléatoire est suffisante et remplit son objectif. 

C'est tout pour ce guide. Restez en sécurité et continuez à coder comme une bête.