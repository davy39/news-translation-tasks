---
title: L'état React pour les vrais débutants
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-03-09T16:48:55.000Z'
originalURL: https://freecodecamp.org/news/react-state
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/react-state-absolute-beginners.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'State Management '
  slug: state-management
seo_title: L'état React pour les vrais débutants
seo_desc: "One of the most essential concepts that any modern JavaScript developer\
  \ needs to understand is state. \nIf you don't understand state, you're not going\
  \ to be able to fully use and take advantage of powerful libraries such as React\
  \ to build your applic..."
---

L'un des concepts les plus essentiels que tout développeur JavaScript moderne doit comprendre est **l'état**. 

Si vous ne comprenez pas l'état, vous ne pourrez pas utiliser pleinement et tirer parti de bibliothèques puissantes comme React pour construire vos applications. 

Voyons exactement ce qu'est l'état, comment il existe déjà dans vos applications JavaScript maintenant, et comment React nous permet de le gérer beaucoup plus facilement avec des hooks intégrés comme `useState`.

## Qu'est-ce que l'état ?

Une chose qui peut vous surprendre est que tout site web ou application que vous construisez avec du JavaScript simple implique déjà l'état. Il n'est simplement pas évident de savoir où il se trouve. 

Voici un exemple de base :

Supposons que nous construisons une application de compteur avec JavaScript. Nous voulons que cette application puisse afficher le compte actuel ainsi qu'augmenter et diminuer le compte d'une unité. 

Elle consistera simplement en le compte actuel ainsi qu'un bouton pour augmenter le compte d'une unité et un autre pour le diminuer d'une unité.

Voici à quoi ressemblera la version finale de notre application :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/TKZ1PcCJxw9ORF2DSIEdw.gif)
_L'application de compteur finale_

Voici le balisage de départ pour notre application :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Application de compteur</title>
    <meta charset="UTF-8" />
  </head>

  <body>
    <div>
      <button>+ 1</button>
      <span>0</span>
      <button>- 1</button>
    </div>
  </body>
</html>
```

En termes simples, **l'état est une donnée que nous devons gérer au fil du temps dans notre application.** 

L'état est souvent modifié par l'entrée de l'utilisateur et c'est le cas dans notre application ici. 

Quel est l'état dans notre application de compteur ? C'est le nombre de compte. 

Notre utilisateur peut augmenter ou diminuer la valeur de l'état en cliquant sur le bouton approprié. Ce qui est important, c'est que nous voulons afficher ces changements à notre utilisateur. 

## Problèmes avec l'état en JavaScript simple

Bien que l'état semble être un concept simple, il y a deux problèmes avec sa gestion lorsque vous utilisez uniquement du JavaScript simple :

1. Il n'est pas évident de savoir ce qu'est l'état ou où il se trouve.
2. La lecture et la mise à jour de l'état est un processus peu naturel et souvent répétitif lorsque l'on utilise les API natives du navigateur comme `document`. 

Comment mettrions-nous à jour notre état de compte lorsque notre utilisateur clique sur l'un ou l'autre bouton ?

Nous devons d'abord obtenir une référence à chaque élément. Pour ce faire en JavaScript simple, il est courant d'ajouter un attribut `id` unique à chaque élément, de sélectionner chaque élément en JavaScript avec la méthode `document.querySelector`, et de stocker la référence dans une variable locale :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Application de compteur</title>
    <meta charset="UTF-8" />
  </head>

  <body>
    <div>
      <button id="increment">+ 1</button>
      <span id="count">0</span>
      <button id="decrement">- 1</button>
    </div>

    <script>
      const increment = document.querySelector("#increment");
      const count = document.querySelector("#count");
      const decrement = document.querySelector("#decrement");
    </script>
  </body>
</html>
```

Maintenant que nous avons des références à chaque élément HTML, comment faire fonctionner le bouton d'incrémentation ?

Nous devons d'abord écouter un événement de clic sur notre bouton d'incrémentation. Ensuite, lorsque le bouton est cliqué, nous devons obtenir la valeur actuelle du compte à partir de l'élément avec l'`id` "count". 

Pour ce faire, nous plongeons dans le document HTML en utilisant l'API `document` et obtenons cette valeur avec `count.innerText`. La valeur `innerText` est une chaîne, donc nous la convertissons en nombre, ajoutons 1, puis écrivons cette valeur _en retour_ à `count.innerText`. 

Pour faire fonctionner le bouton de décrémentation, nous répétons les mêmes étapes. La seule différence est que nous utilisons l'expression `Number(count.innerText - 1)`.

```js
<!DOCTYPE html>
<html>
  <head>
    <title>Application de compteur</title>
    <meta charset="UTF-8" />
  </head>

  <body>
    <div>
      <button id="increment">+ 1</button>
      <span id="count">0</span>
      <button id="decrement">- 1</button>
    </div>

    <script>
      const increment = document.querySelector("#increment");
      const count = document.querySelector("#count");
      const decrement = document.querySelector("#decrement");

      increment.addEventListener("click", () => {
        count.innerText = Number(count.innerText) + 1;
      });

      decrement.addEventListener("click", () => {
        count.innerText = Number(count.innerText) - 1;
      });
    </script>
  </body>
</html>
```

Ce n'est pas trop de code, mais vous pouvez voir qu'il y a un certain nombre d'étapes ici qui ne sont pas très intuitives et répétitives :

* Ajouter un id arbitraire aux éléments HTML
* Interroger l'élément en utilisant JavaScript
* Stocker la référence de l'élément dans une variable
* Écouter l'événement approprié sur l'élément
* Obtenir la valeur actuelle de l'état en utilisant l'API `document`
* Écrire la nouvelle valeur de l'état sur la page avec `.innerText`

Ce sont beaucoup d'instructions de bas niveau qui sont nécessaires pour que notre programme fonctionne, mais elles ne nous aident pas à penser à l'état sous-jacent.

Comme nous l'avons vu, l'état vit dans le navigateur. Cela signifie que nous devons "trouver" l'état d'abord et ensuite le mettre à jour **impérativement** (d'une manière que l'ordinateur comprend mieux que nous).

Heureusement, React nous donne un moyen beaucoup plus facile de mettre à jour l'état et de _penser_ à l'état.

## Comment React nous aide-t-il à gérer l'état ?

Un avantage significatif de l'utilisation de React et pourquoi il est dans votre intérêt de l'utiliser pour développer vos applications JavaScript est qu'il vous donne des modèles beaucoup plus faciles pour mettre à jour votre état. 

Contrairement au JavaScript simple, React s'occupe du travail difficile de mise à jour de ce que l'utilisateur voit. Tout ce que nous avons à faire est de lui dire quel état nous gérons et quelle doit être la nouvelle valeur. 

Au lieu que l'état vive dans le navigateur et que nous devions le trouver chaque fois que nous devons le lire ou le mettre à jour, nous sommes en mesure de simplement le mettre dans une variable et ensuite mettre à jour la valeur de cette variable. Après cela, la mise à jour et la nouvelle valeur seront affichées à nos utilisateurs. 

**C'est tout le concept de la gestion de l'état dans React.** 

Au lieu d'utiliser un document HTML, nous pouvons écrire tout notre balisage dans un composant React. 

Il est écrit de manière identique à une fonction JavaScript régulière et il affiche les mêmes éléments HTML en utilisant une syntaxe identique appelée JSX.

```js
export default function Counter() {
  return (
    <div>
      <button>+ 1</button>
      <span>0</span>
      <button>- 1</button>
    </div>
  );
}
```

Comment pouvons-nous créer la même application de compteur avec React ? 

Dans notre application React, une fois que nous avons identifié ce qu'est notre état, nous le contrôlons en utilisant une variable JavaScript.

Cette variable peut être déclarée de nombreuses manières. La manière la plus populaire de gérer l'état des composants est avec le **hook `useState`**.

Un **hook** dans React fonctionne de manière très similaire aux fonctions JavaScript régulières. Cela signifie que nous pouvons l'appeler en haut de notre composant et nous lui passons la valeur par défaut comme valeur de départ pour notre application de compteur. 

Puisque la valeur de départ de notre compte est zéro, nous appelons simplement notre hook et lui passons la valeur `0` et cette valeur est mise dans notre variable d'état. 

```js
import { useState } from 'react';

export default function Counter() {
  // la valeur du compte vit et est gérée ici !
  const [count] = useState(0);  
    
  return (
    <div>
      <button>+ 1</button>
      <span>{count}</span> {/* utiliser les accolades pour afficher la valeur du compte : 0 */}
      <button>- 1</button>
    </div>
  );
}
```

Il n'est plus nécessaire d'utiliser `count.innerText`. Nous pouvons simplement afficher et lire la valeur de notre état en utilisant `count`.

Comme toute variable JavaScript, nous pouvons la nommer comme nous le souhaitons. Elle n'a pas besoin de s'appeler `count`. Vous pourriez l'appeler littéralement n'importe quoi d'autre tant que c'est un nom JavaScript valide.

La valeur de retour de `useState` est un tableau. Lorsque nous le déstructurons, la première valeur déstructurée est la variable d'état. La deuxième est la fonction pour mettre à jour l'état. 

```js
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);  
    
  return (
    <div>
      <button>+ 1</button>
      <span>{count}</span>
      <button>- 1</button>
    </div>
  );
}
```

Comment faire fonctionner le bouton d'incrémentation ?

Voici ce que nous _n'avons pas_ besoin de faire :

* Nous n'avons pas besoin d'ajouter un `id` à nos éléments HTML 
* Nous n'avons pas besoin de plonger dans le DOM et de déterminer quel bouton est lequel
* Nous n'avons pas besoin d'écouter un événement de clic avec `document.addEventListener`

Pour mettre à jour l'état lorsque vous cliquez sur un bouton, ajoutez la prop `onClick` à chaque bouton. Cela vous permet d'appeler une fonction lorsque le bouton est pressé par l'utilisateur. 

Pour le bouton d'incrémentation, nous mettrons à jour l'état en passant `count + 1` à `setCount`, et pour le bouton de décrémentation, nous passerons `count - 1` à `setCount`.

```js
import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);  
    
  function incrementCount() {
    setCount(count + 1);
  }
    
  function decrementCount() {
    setCount(count - 1);   
  }
    
  return (
    <div>
      <button onClick={incrementCount}>+ 1</button>
      <span>{count}</span>
      <button onClick={decrementCount}>- 1</button>
    </div>
  );
}
```

C'est tout le code dont nous avons besoin pour créer une application de compteur fonctionnelle avec React.

Lorsque chaque bouton est pressé et que l'état est mis à jour, React fera tout le travail de mise à jour de la page afin que l'utilisateur puisse voir le nouvel état.

C'est le grand avantage d'utiliser React par rapport au JavaScript simple : lorsque l'état est géré en utilisant des hooks comme `useState` et que React s'occupe de mettre à jour efficacement ce que l'utilisateur voit, nous pouvons créer des applications plus simples et plus fiables où l'état est facile à voir, à lire et à mettre à jour.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*