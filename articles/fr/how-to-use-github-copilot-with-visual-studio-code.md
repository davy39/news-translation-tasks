---
title: Comment utiliser GitHub Copilot avec Visual Studio Code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-07-05T15:12:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-github-copilot-with-visual-studio-code
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/How-to-Build-a-Weather-Application-using-React--1-.png
tags:
- name: automation
  slug: automation
- name: GitHub
  slug: github
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment utiliser GitHub Copilot avec Visual Studio Code
seo_desc: 'By Nishant Kumar

  Hey everyone, welcome! In this article, we will learn how to use the GitHub Copilot
  AI tool with Visual Studio Code.

  What is GitHub Copilot?

  GitHub Copilot is a tool that can help you write easier and faster code. It is powered
  by GP...'
---

Par Nishant Kumar

Salut à tous, bienvenue ! Dans cet article, nous allons apprendre à utiliser l'outil d'IA GitHub Copilot avec Visual Studio Code.

## Qu'est-ce que GitHub Copilot ?

GitHub Copilot est un outil qui peut vous aider à écrire du code plus facilement et plus rapidement. Il est alimenté par **GPT-3**. Vous devez simplement écrire la description du code dont vous avez besoin – par exemple, écrire une fonction pour générer un nombre aléatoire, ou trier un tableau – et Copilot le crée pour vous.

Et il ne crée pas seulement une solution. Il en génère plusieurs, et vous pouvez choisir celle que vous préférez.

Dans ce tutoriel, nous allons apprendre à configurer l'outil d'IA GitHub Copilot pour Visual Studio Code, ainsi qu'à générer du code pour JavaScript, React et HTML.

## Comment installer GitHub Copilot

Pour ajouter GitHub Copilot, rendez-vous sur votre [GitHub](https://github.com/) et allez dans les paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-181658.png)

Choisissez GitHub Copilot dans le menu de gauche et autorisez-le simplement, puis cliquez sur le bouton **Enregistrer**.

Ouvrez maintenant Visual Studio Code et allez dans **Extensions**. Recherchez GitHub Copilot dans la barre de recherche.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-181954.png)

Installez GitHub Copilot et redémarrez votre Visual Studio Code.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-182152.png)

Et en bas, vous verrez que GitHub Copilot a été activé.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Untitled-design.png)

Mais gardez à l'esprit que nous n'avons que la version d'essai pour le moment. Et elle n'est valable que pour deux mois – l'essai gratuit se termine le 22 août. Nous devrons acheter la version complète après la fin de l'essai.

Cela vous coûtera 10 $ par mois, ou 100 $ par an.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-182753.png)

Maintenant que nous avons installé Copilot, passons à la partie plus amusante où nous allons l'utiliser.

## Comment utiliser GitHub Copilot pour générer du code JavaScript

Commençons par quelque chose de simple. Créons une fonction pour additionner deux nombres.

Dans un fichier JavaScript, écrivez simplement un commentaire comme "**Générer une fonction pour additionner deux nombres**".

```
//Générer une fonction pour additionner deux nombres
```

Puis appuyez sur Entrée. Il vous proposera des suggestions, que vous pouvez accepter en appuyant sur la **touche tabulation**.

```
//Générer une fonction pour additionner deux nombres
function add(a, b) {
```

Puis appuyez sur Entrée pour la ligne suivante, et lorsque la ligne de code suivante apparaît, appuyez à nouveau sur **tabulation**.

```
//Générer une fonction pour additionner deux nombres
function add(a, b) {
  return a + b;
}

```

Et voici votre fonction pour additionner deux nombres.

Maintenant, appelons la fonction **`add()`**. Écrivez l'invocation de la fonction, et elle acceptera automatiquement certains paramètres aléatoires.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--267--1.png)

Nous pouvons également soustraire, multiplier et diviser des nombres. 

## Comment utiliser GitHub Copilot pour générer une fonction affichant les couleurs de l'arc-en-ciel dans un tableau

Nous commencerons par un commentaire "**Générer un tableau de toutes les couleurs de l'arc-en-ciel**".

```
//Générer un tableau de toutes les couleurs de l'arc-en-ciel
```

Puis, comme avant, nous appuierons sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--268-.png)

Et il générera le tableau de toutes les couleurs de l'arc-en-ciel. 

```
//Générer un tableau de toutes les couleurs de l'arc-en-ciel
var colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
```

## Comment créer trois tableaux avec les types Number, String et Boolean et les fusionner dans un objet

Maintenant, essayons de créer un tableau de nombres, de chaînes de caractères et de valeurs booléennes.

```
//Créer un tableau de nombres
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//Créer un tableau de chaînes de caractères
var strings = ["hello", "world", "how", "are", "you"];

//Créer un tableau de booléens
var booleans = [true, false, true, false, true];
```

Maintenant, fusionnons-les dans un objet. Nous allons créer un **Objet** comme ceci :

```
var objects = [
    {
        number: 1,
        string: "hello",
        boolean: true
    },
    {
        number: 2,
        string: "world",
        boolean: false
    },
    {
        number: 3,
        string: "how",
        boolean: true
    },
]
```

Écrivez un commentaire qui dit "**Créer un tableau d'objets avec les éléments des tableaux ci-dessus comme paires clé-valeur**".

Vous pouvez appuyer sur la **touche Tab** pour accepter la solution, ou appuyer sur **CTRL + Entrée** pour ouvrir la page des solutions Copilot.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-185657.png)

Vous pouvez accepter n'importe quelle solution que vous voulez. Cliquez simplement sur **Accepter**.

```
//Créer un tableau de nombres
var numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

//Créer un tableau de chaînes de caractères
var strings = ["hello", "world", "how", "are", "you"];

//Créer un tableau de booléens
var booleans = [true, false, true, false, true];

//Créer un tableau d'objets avec les éléments des tableaux ci-dessus comme paires clé-valeur
var objects = [
  {
    number: 1,
    string: "hello",
    boolean: true,
  },
  {
    number: 2,
    string: "world",
    boolean: false,
  },
  {
    number: 3,
    string: "how",
    boolean: true,
  },
  {
    number: 4,
    string: "are",
    boolean: false,
  },
  {
    number: 5,
    string: "you",
    boolean: true,
  },
];

```

## Comment importer des éléments dans React et Express

Maintenant, essayons de voir comment les choses fonctionnent dans React et Express.

Nous allons simplement importer quelques modules.

Commençons par importer le **Hook useState** depuis **React**.

```
//Importer le Hook useState depuis react
```

Écrivez le commentaire, et appuyez sur Entrée. Copilot générera le code.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot--270-.png)

```
//Importer le Hook useState depuis react
import React, { useState } from 'react';
```

Essayons un autre exemple pour React, qui consiste à importer les Hooks useEffect et useState depuis React.

```
//Importer les Hooks useState et useEffect depuis react
import React, { useState, useEffect } from 'react';
```

Faisons quelque chose dans Express. Importons le **package npm CORS** dans Express, qui est conçu pour Node et Express. Et il sera ici.

```
//Importer cors depuis express
const cors = require('cors');
```

## Comment générer du code pour HTML

Essayons un peu de code HTML.

Tout d'abord, générons du code pour créer une liste non ordonnée, avec Nishant, 25 et Patna. 

```
Créer une balise ul avec les éléments de liste Nishant, 25 et Patna
    <ul>
      <li>Nishant</li>
      <li>25</li>
      <li>Patna</li>
    </ul>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/07/Screenshot-2022-07-02-191108.png)

Essayons la même chose, mais avec le style de liste défini sur none.

```
Créer une balise ul avec la liste ayant une classe de lists et les éléments
    Nishant, 25 et Patna et le style de liste défini sur none
    <ul class="lists" style="list-style: none">
      <li>Nishant</li>
      <li>25</li>
      <li>Patna</li>
    </ul>
```

Et le voilà. Incroyable, n'est-ce pas ?

## Conclusion

Dans cet article, vous avez appris ce qu'est GitHub Copilot et comment l'utiliser.

Vous pouvez également consulter ma vidéo sur le même sujet, qui est [Testons GitHub Copilot - Tutoriel GitHub Copilot avec Visual Studio Code](https://youtu.be/PdXBepPOqqI)

Merci d'avoir lu. Bon apprentissage.