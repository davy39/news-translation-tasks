---
title: Comment animer vos applications React avec Lottie
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2021-03-10T17:07:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-animate-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/how-to-animate-react-apps.png
tags:
- name: animation
  slug: animation
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment animer vos applications React avec Lottie
seo_desc: "Animations can make for a more engaging user experience in our React apps.\
  \ \nTo make good looking animations, however, can be a great deal of work and can\
  \ require a lot of code.\nI am going to show you how to use a very powerful library\
  \ with React to m..."
---

Les animations peuvent rendre l'expérience utilisateur de nos applications React plus engageante.

Cependant, créer de belles animations peut demander beaucoup de travail et nécessiter beaucoup de code.

Je vais vous montrer comment utiliser une bibliothèque très puissante avec React pour créer des animations époustouflantes et pixel-perfectes qui améliorent vos applications, sans trop d'effort.

## Présentation de la bibliothèque Lottie pour React

La bibliothèque dont je parle s'appelle Lottie. Lottie offre une manière totalement différente de créer des animations impressionnantes en utilisant des animations produites dans le programme populaire Adobe After Effects, qui sont importées et exportées sous forme de fichiers JSON.

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/a8unjslg43xwnrjtvokh.gif)

Et surtout, pour trouver et utiliser ces animations, vous n'avez pas besoin d'avoir le programme Adobe After Effects.

## Comment utiliser LottieFiles

Tout ce que vous avez à faire est d'utiliser une ressource complètement gratuite appelée [LottieFiles](https://lottiefiles.com). C'est un site qui héberge des tonnes d'animations Lottie gratuites et payantes.

Supposons que nous voulons un logo React animé dans notre application (notez que vous pouvez utiliser n'importe quelle animation qu'ils mettent à disposition).

Je choisirai personnellement l'animation React suivante de LottieFiles dans laquelle [le logo React tourne](https://lottiefiles.com/6610-react-logo-spinning). À partir de là, nous pouvons la prévisualiser et changer des choses comme la couleur de fond.

Lorsque nous sommes prêts à l'utiliser, nous pouvons télécharger le fichier JSON de l'animation en sélectionnant Lottie JSON :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/4ulaytnlgqbk6eesw3un.png)

Quelle que soit la manière dont vous avez créé votre projet React, vous pouvez le placer dans le dossier de votre choix. Vous pouvez le mettre dans le dossier static à la racine de votre projet ou dans un dossier animations dans le dossier src.

C'est à vous de décider, car nous importerons les données JSON depuis le chemin de fichier.

J'ai choisi de placer mon fichier JSON (appelé react-logo.json) dans mon dossier static :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/6z09zv7kdv5ofkqvf8x3.png)

## Comment installer Lottie-Web

Une fois cela fait, nous installerons Lottie en important le package `lottie-web`.

```bash
npm i lottie-web
```

Notez qu'il existe un package Lottie alternatif appelé `react-lottie`, mais il utilise `lottie-web` en interne, qui peut être facilement utilisé directement comme vous le verrez dans un instant.

Une fois `lottie-web` installé, nous pouvons placer notre animation dans n'importe quel élément JSX en indiquant que nous voulons qu'elle réside dans un certain sélecteur.

La meilleure façon de faire cela est d'utiliser l'attribut id, car il ne doit être utilisé qu'une seule fois dans les éléments de notre application.

Dans notre cas, nous pourrions lui donner la valeur d'id `react-logo` :

```jsx
// src/App.js
import React from "react";

export default function App() {
  return (
    <div>
      <h1>Bonjour le monde</h1>
      <div id="react-logo" />
    </div>
  );
}
```

Pour utiliser Lottie, nous pouvons l'importer depuis `lottie-web` et nous importerons le JSON depuis l'endroit où nous l'avons placé :

```jsx
// src/App.js
import React from "react";
import lottie from "lottie-web";
import reactLogo from "../static/react-logo.json";

export default function App() {
  return (
    <div>
      <h1>Bonjour le monde</h1>
      <div id="react-logo" />
    </div>
  );
}
```

## Comment utiliser Lottie avec le hook useEffect

Utiliser Lottie lui-même est simple. Nous devons obtenir une référence à l'élément JSX/DOM dans lequel nous voulons placer l'animation et lui fournir les données JSON.

Pour interagir avec le DOM lui-même, nous devons nous assurer que le composant est monté, nous utiliserons donc `useEffect` pour effectuer un effet secondaire et passer un tableau de dépendances vide.

Dans `useEffect`, nous pouvons maintenant appeler `lottie.loadAnimation` pour exécuter notre animation, en lui passant un objet. Sur cet objet, la première chose que nous devons fournir est le conteneur, le nœud DOM dans lequel nous voulons que cette animation soit exécutée.

Nous pouvons utiliser n'importe quelle méthode pour référencer le nœud DOM ; personnellement, j'utiliserai `document.getElementById('react-logo')`.

```jsx
// src/App.js
import React from "react";
import lottie from "lottie-web";
import reactLogo from "../static/react-logo.json";

export default function App() {
  React.useEffect(() => {
    lottie.loadAnimation({
      container: document.querySelector("#react-logo"),
    });
  }, []);

  return (
    <div>
      <h1>Bonjour le monde</h1>
      <div id="react-logo" />
    </div>
  );
}


```

Et avec ce conteneur, nous devons simplement fournir les données JSON elles-mêmes sur une propriété appelée `animationData`.

```jsx
// src/App.js
import React from "react";
import lottie from "lottie-web";
import reactLogo from "../static/react-logo.json";

export default function App() {
  React.useEffect(() => {
    lottie.loadAnimation({
      container: document.querySelector("#react-logo"),
    });
  }, []);

  return (
    <div>
      <h1>Bonjour le monde</h1>
      <div id="react-logo" />
    </div>
  );
}


```

Après cela, vous devriez voir l'animation se lancer automatiquement :

![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/yfn5x0sklji6legt1egf.gif)

Si vous avez le même code que moi et que votre animation s'exécute dans une div vide, elle apparaîtra énorme.

Vous pouvez corriger cela en fournissant quelques styles et en ajoutant une largeur et une hauteur fixes pour la div conteneur :

```jsx
<div id="react-logo" style={{ width: 200, height: 200 }} />
```

## Propriétés de Lottie.loadAnimation

En plus de container et animationData, il existe d'autres propriétés importantes que nous pouvons passer à `loadAnimation` pour changer l'apparence et le fonctionnement de l'animation.

```jsx
lottie.loadAnimation({
  container: document.querySelector("#react-logo"),
  animationData: reactLogo,
  renderer: "svg", // "canvas", "html"
  loop: true, // boolean
  autoplay: true, // boolean
});


```

Ci-dessus, j'ai inclus tous les paramètres par défaut pour `loadAnimation`. Par défaut, l'animation est rendue en SVG, avec la propriété `renderer`. Cela offre le plus de fonctionnalités, mais l'option HTML peut être plus performante et supporte les calques 3D.

L'animation se répète ou se boucle à l'infini par défaut car `loop` est défini sur true. Vous pouvez désactiver ce comportement en le définissant sur false.

Le paramètre `autoplay` de l'animation est par défaut true, ce qui signifie que l'animation se lancera automatiquement lorsqu'elle sera chargée. Si vous souhaitiez exécuter l'animation de manière conditionnelle, vous pourriez la définir sur true ou false en utilisant une variable d'état (par exemple, si vous souhaitiez lire l'animation uniquement lorsqu'elle est visible).

## Comment ajouter Lottie Light

Enfin, la dernière chose que je mentionnerai à propos de Lottie est que `lottie-web` est une dépendance plutôt volumineuse.

Si vous souhaitez utiliser toutes ses fonctionnalités mais que vous êtes préoccupé par l'ajout de trop de code à votre bundle final, vous pouvez importer la version légère de Lottie comme suit :

```jsx
import lottie from "lottie-web/build/player/lottie_light";
```

## Code final

J'espère que cet article vous a aidé à vous lancer avec Lottie en tant que fonctionnalité intéressante à ajouter à vos projets React lorsque vous cherchez quelque chose de spécial dans vos applications web.

Consultez le [lien CodeSandbox](https://codesandbox.io/s/damp-dust-i7k1u?file=/src/App.js:174-292) si vous souhaitez jouer avec le code final vous-même.

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à tout comprendre par vous-même.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation : Le React Bootcamp**](https://www.thereactbootcamp.com)

**C'est le cours que j'aurais aimé avoir lorsque j'ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*