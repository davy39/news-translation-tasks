---
title: Comment animer vos applications React avec 1 ligne de code
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2022-09-15T19:56:57.000Z'
originalURL: https://freecodecamp.org/news/animate-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/mugshotbot.com_customize_color-red-image-9129875b-mode-dark-pattern-topography-theme-two_up-url-https___freecodecamp.org.png
tags:
- name: animation
  slug: animation
- name: React
  slug: react
seo_title: Comment animer vos applications React avec 1 ligne de code
seo_desc: "Animations have the powerful ability to turn a boring, static application\
  \ into a more dynamic, memorable experience for your users. \nIn general, animations\
  \ can be quite difficult to set up, especially if you intend to animate multiple\
  \ components in y..."
---

Les animations ont le pouvoir de transformer une application statique et ennuyeuse en une expérience plus dynamique et mémorable pour vos utilisateurs. 

En général, les animations peuvent être assez difficiles à configurer, surtout si vous souhaitez animer plusieurs composants dans votre application. 

Dans ce tutoriel, nous verrons comment implémenter pratiquement toutes les animations courantes dans vos applications React avec une seule ligne de code en utilisant la bibliothèque **AutoAnimate**.

## Pourquoi vous devriez utiliser AutoAnimate

Si vous construisez une application React, il existe de nombreuses bibliothèques d'animation puissantes que vous pouvez choisir, comme Framer Motion.

L'inconvénient de la plupart de ces bibliothèques (ainsi que du CSS simple) est qu'elles nécessitent assez de code pour faire fonctionner vos animations. Traditionnellement, vous devez spécifier :

1. Les propriétés CSS que vous souhaitez animer
2. La durée pendant laquelle vous souhaitez que l'animation soit exécutée
3. Une fonction d'assouplissement qui détermine comment l'animation progresse pendant la durée de chaque cycle

AutoAnimate élimine le besoin de spécifier **aucun** de ces éléments.

La puissance d'AutoAnimate réside dans le fait qu'il vous permet d'animer toute votre application en utilisant une seule fonction appelée `autoAnimate`.

![Image](https://www.freecodecamp.org/news/content/images/2022/09/Screen-Shot-2022-09-15-at-11.37.45-AM.png)
_La bibliothèque d'animation AutoAnimate_

## Comment fonctionne AutoAnimate

`autoAnimate` prend un argument : une référence à l'élément parent que vous souhaitez animer. 

Le fonctionnement de la bibliothèque est tel que l'élément parent sera "auto-animé" ainsi que tous ses enfants immédiats.

Les animations ont lieu chaque fois qu'un des trois événements suivants se produit sur cet élément parent :

Si un élément enfant est **ajouté**, **supprimé** ou **déplacé**.

Nous allons voir comment vous pouvez utiliser AutoAnimate avec trois exemples : un composant extensible, un composant de liste et un composant de grille.

## Comment utiliser AutoAnimate

Il y a deux étapes pour commencer à utiliser auto animate :

1. Installez-le dans votre projet en utilisant soit yarn soit NPM 

```bash
npm install @formkit/auto-animate
```

2. Importez la fonction auto animate depuis la bibliothèque elle-même

```js
import autoAnimate from '@formkit/auto-animate'
```

Ce tutoriel couvre comment utiliser AutoAnimate dans les applications React, mais vous pouvez l'utiliser dans pratiquement n'importe quel projet JavaScript (y compris Svelte, Vue et Vanilla JS).

Pour animer n'importe quel élément parent, vous devez simplement passer une référence de l'élément à la fonction.

```js
import { useEffect, useRef } from 'react'

function Component() {
  const parentRef = useRef(null)

  useEffect(() => {
    if (parentRef.current) {
      autoAnimate(parentRef.current);   
    }
  }, [parent])

  return (
    <div ref={parentRef}>
    // ...
  )
}
```

Nous pouvons voir comment cela fonctionne sur des composants extensibles simples tels qu'un composant FAQ (Foire Aux Questions). 

Disons que nous voulons que nos utilisateurs puissent cliquer sur une div et l'étendre pour montrer plus de texte. 

Tout d'abord, nous créons une div avec du texte à afficher dans son état initial (`Show More`) ainsi que du texte à révéler lorsqu'on clique dessus.

Pour animer l'ouverture du texte, nous utilisons le hook `useRef` pour référencer l'élément parent et passons ensuite cette référence à la fonction auto animate. 

%[https://codesandbox.io/embed/epic-lamport-5y9uwk?fontsize=14&hidenavigation=1&theme=dark]

Et instantanément, nous avons un composant beaucoup plus engageant et animé en douceur.

## Comment animer des listes avec AutoAnimate

Un autre excellent cas d'utilisation pour auto animate est avec un composant de liste. 

Disons que nous construisons une application de todo et que nous souhaitons animer les nouveaux éléments qui sont ajoutés à la liste.

```js
import { useState } from "react"
import autoAnimate from "@formkit/auto-animate"

export default function App() {
  const [items, setItems] = useState(["Buy Gas", "Do Laundry"])

  function addItem() {
    const item = "Go To Store"
    setItems([...items, item])
  }

  return (
    <>
      <ul ref={parent}>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
      <button onClick={addItem}>Add Todo</button>
    </>
  )
}
```

Dans cet exemple, nous avons une liste de tâches à faire, et chaque fois que nous cliquons sur un bouton, il ajoute un nouvel élément à notre liste. 

Si nous voulons l'animer, nous pouvons répéter les mêmes étapes que précédemment, mais nous ajoutons une référence à l'élément parent (dans ce cas, une liste non ordonnée).

%[https://codesandbox.io/embed/unruffled-night-ugucy0?fontsize=14&hidenavigation=1&theme=dark]

Chaque fois que nous cliquons sur le bouton pour ajouter un nouvel élément à notre liste, chaque tâche est maintenant insérée dans la liste de manière fluide, animant à la fois sa position et son opacité.

## Comment personnaliser les animations

AutoAnimate est conçu pour être une solution tout-en-un pour les animations qui ne nécessite pas de configuration, mais il nous permet de personnaliser des valeurs telles que la durée et le moment où l'animation est jouée.

Pour un meilleur contrôle sur nos animations, nous pouvons utiliser `useAutoAnimate` qui peut être importé de cette manière :

```js
import { useAutoAnimate } from "@formkit/auto-animate/react";
```

Comme tout hook React, il est appelé en haut de tout composant React dans lequel nous voulons l'utiliser.

L'avantage de ce hook est que nous n'avons plus besoin d'utiliser le hook `useRef`. Au lieu de cela, le hook le retourne ainsi qu'une fonction qui nous permet de contrôler si nous voulons animer l'élément parent ou non.

```js
import { useAutoAnimate } from "@formkit/auto-animate/react";

export default function App() {
  const [parent, enable] = useAutoAnimate({ duration: 500 });
  const [isEnabled, setIsEnabled] = useState(true);

  function toggleEnabled() {
    enable(!isEnabled);
    setIsEnabled(!isEnabled);
  }
 
   // ...
 }
```

Disons que nous utilisons un formulaire pour ajouter un nouvel élément à cette grille et que nous voulons pousser doucement tous les autres éléments sur le côté.

AutoAnimate rend cela très facile une fois de plus, mais dans ce cas, nous utiliserons le hook `useAutoAnimate` pour effectuer l'animation après une demi-seconde. Pour ce faire, nous pouvons utiliser la propriété duration.

```jsx
  const [parent, enable] = useAutoAnimate({ duration: 500 });

```

Comme vous le voyez, il gère à la fois l'animation de la nouvelle carte ajoutée ainsi que l'animation de poussée de toutes les autres cartes sur le côté.

%[https://codesandbox.io/embed/boring-haze-k7tdjr?fontsize=14&hidenavigation=1&theme=dark]

Et c'est tout ! Maintenant, vous pouvez utiliser cette bibliothèque utile pour animer facilement vos applications React.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*