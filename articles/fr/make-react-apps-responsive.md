---
title: Comment rendre vos applications React réactives avec un Hook personnalisé
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-19T16:28:08.000Z'
originalURL: https://freecodecamp.org/news/make-react-apps-responsive
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/make-your-react-apps-responsive-with-a-custom-hook.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: responsive design
  slug: responsive-design
seo_title: Comment rendre vos applications React réactives avec un Hook personnalisé
seo_desc: 'How do you make your React applications responsive for any sized device?
  Let''s see how to do so by making our own custom React hook.

  At the top of my React site is a Header component. As I decrease the size of the
  page, I want to show fewer links:


  T...'
---

Comment rendre vos applications React réactives pour tout type d'appareil ? Voyons comment le faire en créant notre propre Hook React personnalisé.

En haut de mon site React se trouve un composant Header. Lorsque je réduis la taille de la page, je souhaite afficher moins de liens :

![redimensionnement de la fenêtre pour afficher l'en-tête](https://dev-to-uploads.s3.amazonaws.com/i/kxbnn3jmwjarkc8zrpbm.gif)

Pour ce faire, nous pourrions utiliser une requête média avec CSS, ou nous pourrions utiliser un Hook React personnalisé pour nous donner la taille actuelle de la page et masquer ou afficher les liens dans notre JSX.

Auparavant, j'utilisais un Hook de la bibliothèque appelée `react-use` pour ajouter cette fonctionnalité.

Au lieu d'importer une bibliothèque tierce entière, j'ai décidé de créer mon propre Hook qui fournirait les dimensions de la fenêtre, à la fois la largeur et la hauteur. J'ai appelé ce Hook `useWindowSize`.

## Comment créer le Hook personnalisé

Tout d'abord, nous allons créer un nouveau fichier .js dans notre dossier utilities (utils), avec le même nom que le Hook `useWindowSize`, et j'importerai React (pour utiliser les Hooks) tout en exportant le Hook personnalisé.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {}

```

Maintenant, comme je l'utilise dans un site Gatsby, qui est rendu côté serveur, j'ai besoin d'obtenir la taille de la fenêtre. Mais nous n'avons peut-être pas accès à celle-ci car nous sommes sur le serveur.

Pour vérifier et s'assurer que nous ne sommes pas sur le serveur, nous pouvons voir si le type de `window` n'est pas égal à la chaîne `undefined`.

Dans ce cas, nous pouvons retourner une largeur et une hauteur par défaut pour un navigateur, disons, 1200 et 800 dans un objet :

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  if (typeof window !== "undefined") {
    return { width: 1200, height: 800 };
  }
}
```

## Comment obtenir la largeur et la hauteur de la fenêtre

Et en supposant que nous sommes sur le client et que nous pouvons obtenir la fenêtre, nous pouvons utiliser le Hook `useEffect` pour effectuer un effet secondaire en interagissant avec `window`. Nous inclurons un tableau de dépendances vide pour nous assurer que la fonction d'effet est appelée uniquement une fois que le composant (dans lequel ce Hook est appelé) est monté.

Pour connaître la largeur et la hauteur de la fenêtre, nous pouvons ajouter un écouteur d'événement et écouter l'événement `resize`. Et chaque fois que la taille du navigateur change, nous pouvons mettre à jour un état (créé avec `useState`), que nous appellerons `windowSize` et le setter pour le mettre à jour sera `setWindowSize`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  if (typeof window !== "undefined") {
    return { width: 1200, height: 800 };
  }

  const [windowSize, setWindowSize] = React.useState();

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });
  }, []);
}
```

Lorsque la fenêtre est redimensionnée, le callback sera appelé et l'état `windowSize` sera mis à jour avec les dimensions actuelles de la fenêtre. Pour obtenir cela, nous définissons la largeur sur `window.innerWidth` et la hauteur sur `window.innerHeight`.

## Comment ajouter la prise en charge du SSR

Cependant, le code tel que nous l'avons ici ne fonctionnera pas. Et cela est dû à une règle clé des Hooks : ils ne peuvent pas être appelés de manière conditionnelle. Par conséquent, nous ne pouvons pas avoir une conditionnelle au-dessus de notre Hook `useState` ou `useEffect`, avant qu'ils ne soient appelés.

Pour corriger cela, nous allons définir la valeur initiale de `useState` de manière conditionnelle. Nous allons créer une variable appelée `isSSR`, qui effectuera la même vérification pour voir si la fenêtre n'est pas égale à la chaîne `undefined`.

Et nous allons utiliser un opérateur ternaire pour définir la largeur et la hauteur en vérifiant d'abord si nous sommes sur le serveur. Si nous y sommes, nous utiliserons la valeur par défaut. Sinon, nous utiliserons `window.innerWidth` et `window.innerHeight`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  // if (typeof window !== "undefined") {
  // return { width: 1200, height: 800 };
  // }
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });
  }, []);
}
```

Enfin, nous devons penser à ce qui se passe lorsque nos composants sont démontés. Que devons-nous faire ? Nous devons supprimer notre écouteur de redimensionnement.

### Suppression de l'écouteur d'événement de redimensionnement

Vous pouvez le faire en retournant une fonction de useEffect et nous supprimerons l'écouteur avec `window.removeEventListener`.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  // if (typeof window !== "undefined") {
  // return { width: 1200, height: 800 };
  // }
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  React.useEffect(() => {
    window.addEventListener("resize", () => {
      setWindowSize({ width: window.innerWidth, height: window.innerHeight });
    });

    return () => {
      window.removeEventListener("resize", () => {
        setWindowSize({ width: window.innerWidth, height: window.innerHeight });
      });
    };
  }, []);
}
```

Mais nous avons besoin d'une référence à la même fonction, et non à deux fonctions différentes comme nous l'avons ici. Pour ce faire, nous allons créer une fonction de callback partagée pour les deux écouteurs appelée `changeWindowSize`.

Et enfin, à la fin du Hook, nous retournerons notre état `windowSize`. Et c'est tout.

```js
// utils/useWindowSize.js

import React from "react";

export default function useWindowSize() {
  const isSSR = typeof window !== "undefined";
  const [windowSize, setWindowSize] = React.useState({
    width: isSSR ? 1200 : window.innerWidth,
    height: isSSR ? 800 : window.innerHeight,
  });

  function changeWindowSize() {
    setWindowSize({ width: window.innerWidth, height: window.innerHeight });
  }

  React.useEffect(() => {
    window.addEventListener("resize", changeWindowSize);

    return () => {
      window.removeEventListener("resize", changeWindowSize);
    };
  }, []);

  return windowSize;
}
```

## Comment utiliser le Hook

Pour utiliser le Hook, nous devons simplement l'importer là où nous en avons besoin, l'appeler et utiliser la largeur partout où nous voulons masquer ou afficher certains éléments.

Dans mon cas, cela se fait à partir de 500px. Là, je veux masquer tous les autres liens et n'afficher que le bouton Join Now, comme vous le voyez dans l'exemple ci-dessus :

```js
// components/StickyHeader.js

import React from "react";
import useWindowSize from "../utils/useWindowSize";

function StickyHeader() {
  const { width } = useWindowSize();

  return (
    <div>
      {/* visible uniquement lorsque la fenêtre est supérieure à 500px */}
      {width > 500 && (
        <>
          <div onClick={onTestimonialsClick} role="button">
            <span>Témoignages</span>
          </div>
          <div onClick={onPriceClick} role="button">
            <span>Prix</span>
          </div>
          <div>
            <span onClick={onQuestionClick} role="button">
              Question ?
            </span>
          </div>
        </>
      )}
      {/* visible à toute taille de fenêtre */}
      <div>
        <span className="primary-button" onClick={onPriceClick} role="button">
          Rejoindre maintenant
        </span>
      </div>
    </div>
  );
}
```

Ce Hook fonctionnera sur toute application React rendue côté serveur, comme Gatsby et Next.js.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : The React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*