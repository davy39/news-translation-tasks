---
title: Comment créer un composant d'animation Fade-in réutilisable dans React avec
  GSAP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-reusable-fade-in-animation-component-in-react-with-gsap
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9983740569d1a4ca2029.jpg
tags:
- name: animation
  slug: animation
- name: React
  slug: react
- name: Web Design
  slug: web-design
seo_title: Comment créer un composant d'animation Fade-in réutilisable dans React
  avec GSAP
seo_desc: 'By Dillion Megida

  If you haven''t heard about or used GSAP, you''re missing out. GSAP is an animation
  library for components and elements. Their homepage shows a lot of awesome animations
  you can make with the tool.

  GSAP has a lot of configurations, an...'
---

Par Dillion Megida

Si vous n'avez pas entendu parler ou utilisé GSAP, vous passez à côté de quelque chose. GSAP est une bibliothèque d'animation pour les composants et les éléments. [Leur page d'accueil](https://greensock.com/gsap/) montre beaucoup d'animations impressionnantes que vous pouvez créer avec cet outil.

GSAP a de nombreuses configurations, et il n'y a pas une seule bonne façon d'atteindre un type d'animation. Nous allons donc examiner une façon (opinionée) de créer une animation 'Fade In' lorsqu'un composant se charge.

Cet article ne rentrera pas dans les détails sur l'utilisation de GSAP. Leur documentation est la ressource à consulter si vous souhaitez un guide approfondi pour apprendre l'outil.

## Ce que nous allons animer

Voici une petite description de ce que nous allons animer :

C'est quelque chose de simple. Lorsqu'un composant est chargé (n'importe où), il s'estompe. Nous allons également ajouter une direction pour que le composant s'estompe d'une zone à la position normale.

Nous allons également rendre le composant d'animation réutilisable afin de pouvoir l'appliquer à différents éléments.

## Commençons !

### Installation de GSAP

Tout d'abord, vous devez avoir un projet React configuré. [create-react-app](https://www.npmjs.com/package/create-react-app) est là pour vous si vous avez besoin d'en configurer un rapidement pour ce projet.

Pour installer GSAP, entrez la commande suivante dans votre terminal (avec le répertoire courant étant votre répertoire de projet React) :

```shell
npm install --save gsap
```

### Créer un composant d'animation utilisable

#### Configuration du composant

Appelons notre composant `FadeIn` :

```js
import React, {useRef, useEffect} from 'react'

const FadeInAnimation = ({children, wrapperElement = 'div', direction = null, ...props}) => {
  const Component = wrapperElement;
  const compRef = useRef(null)
  useEffect(() => {
    // animations
  }, [compRef])
  return (
    <Component ref={compRef} {...props}>
      {children}
    </Component>
  )
}

export default FadeInAnimation
```

Notre animation n'est pas encore prête, mais comprenons ce avec quoi nous commençons.

- `wrapperElement` : utilisé pour spécifier ce que sera le composant. Il a une valeur par défaut de `div`. C'est mieux que de créer un nœud DOM supplémentaire pour envelopper le composant que nous voulons animer.
- [`useRef`](https://reactjs.org/docs/hooks-reference.html#useref) : `gsap` en a besoin pour savoir quoi déclencher pour les animations. Avec cela, nous pouvons faire référence à notre composant dans le DOM.
- `useEffect` : sans cela, `gsap` déclenchera des animations avec une référence nulle (`useRef(null)`). Nous devons nous assurer que le composant est déjà monté, d'où ce hook.
- `children` : ce sera ce qui se trouve entre `<FadeInAnimation>` et `</FadeInAnimation>`. Cela peut être du texte, ou même un groupe d'éléments.
- `...props` : pour étendre la réutilisabilité, cela est nécessaire afin que les composants puissent appliquer d'autres props comme `className` et `style`.
- `direction` : pour les cas où nous voulons ajouter une direction à l'effet de fondu. La valeur par défaut est null.

Maintenant, passons à GSAP.

#### Configuration de l'animation

```js
import React, { useRef, useEffect } from "react";
import { gsap } from "gsap";

const FadeInAnimation = ({
  children,
  wrapperElement = "div",
  direction = null,
  delay = 0,
  ...props
}) => {
  const Component = wrapperElement;
  let compRef = useRef(null);
  const distance = 200;
  let fadeDirection;
  switch (direction) {
    case "left":
      fadeDirection = { x: -distance };
      break;
    case "right":
      fadeDirection = { x: distance };
      break;
    case "up":
      fadeDirection = { y: distance };
      break;
    case "down":
      fadeDirection = { y: -distance };
      break;
    default:
      fadeDirection = { x: 0 };
  }
  useEffect(() => {
    gsap.from(compRef.current, 1, {
      ...fadeDirection,
      opacity: 0,
      delay
    });
  }, [compRef, fadeDirection, delay]);
  return (
    <Component ref={compRef} {...props}>
      {children}
    </Component>
  );
};

export default FadeInAnimation;
```

Passons en revue ce qui s'est passé ici :

- Nous avons initialisé une variable `distance` à 200. Cela est utile pour les cas où une direction est appliquée. Vous pouvez également ajouter cela aux props d'entrée afin que le composant qui l'utilise puisse décider.
- Nous avons notre instruction `switch`. Cela permet de déterminer la direction du fondu, avec le cas par défaut pour les cas où la direction n'est pas spécifiée.
- Ensuite, [`gsap`](https://greensock.com/docs/v3/GSAP). Cela est exposé par GSAP pour animer notre composant. Il existe `.to`, `.from`, `.fromTo` et plus encore que vous pouvez trouver dans la documentation.
- `gsap.from` dans notre cas fait référence à l'état initial du composant avant l'état final (définis dans la feuille de style du composant). Nous ciblons l'élément actuel de la référence, appliquons une durée de 1 seconde et appliquons les options d'animation.
- `...fadeDirection` : nous étalons l'objet pour qu'il apparaisse comme `{x: 200}` ou comme spécifié. `x` est pour l'horizontal et `y` est pour le vertical.
- Ensuite, une opacité initiale de 0 et un délai tel que spécifié par le composant.

Et c'est tout. Créons un composant qui utilise cette animation géniale.

### Comment utiliser notre composant de fondu réutilisable

Rendez-vous dans le composant que vous souhaitez animer et faites quelque chose de similaire à ce qui suit :

```js
import React from "react";
import FadeInAnimation from "./FadeInAnimation";

export default function App() {
  return (
    <div>
      <FadeInAnimation wrapperElement="h1" direction="down">
        Bonjour CodeSandbox
      </FadeInAnimation>
      <FadeInAnimation wrapperElement="h2" direction="right" delay={2}>
        Commencez à éditer pour voir un peu de magie se produire !
      </FadeInAnimation>
      <FadeInAnimation
        style={{
          width: 200,
          color: "white",
          height: 200,
          backgroundColor: "purple"
        }}
        direction='up'
      >
        <p>Bonjour</p>
      </FadeInAnimation>
    </div>
  );
}
```

Comme on peut le voir ci-dessus, notre composant `FadeInAnimation` peut accepter une prop `style`. Souvenez-vous que nous avons fait `...props`.

Voici le résultat dans [CodeSandBox](https://codesandbox.io/s/react-gsap-fadein-effect-z8xqd?file=/src/App.js)

## Conclusion

C'est tout. Il s'agit d'une utilisation simple (opinionée) de GSAP pour les effets de fondu. 

Bien sûr, vous pouvez le configurer davantage, comme créer un effet de rebond de fondu, une rotation de fondu, et d'autres choses amusantes. Mais j'espère que cet article vous a donné une introduction brève et concise à la puissance de GSAP et à la manière de commencer à faire des choses incroyables sur le web.

Note de côté : cela est similaire à la configuration que j'utilise dans un nouveau package d'animation que je lance bientôt. Je le partagerai dans cet article lorsqu'il sera publié : )