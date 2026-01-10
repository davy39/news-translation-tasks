---
title: Tutoriel React Background Image – Comment définir backgroundImage avec le style
  CSS en ligne
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2020-12-14T16:03:20.000Z'
originalURL: https://freecodecamp.org/news/react-background-image-tutorial-how-to-set-backgroundimage-with-inline-css-style
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/fcc-bg-image-2.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Tutoriel React Background Image – Comment définir backgroundImage avec
  le style CSS en ligne
seo_desc: 'There are four ways to set a backgroundImage style property using React''s
  inline CSS.

  This tutorial will show you all four methods, with code samples for each.

  Here''s an Interactive Scrim of Setting a Background Image with React



  How to Set a Backgr...'
---

Il existe quatre façons de définir la propriété de style `backgroundImage` en utilisant le CSS en ligne de React.

Ce tutoriel vous montrera les quatre méthodes, avec des exemples de code pour chacune.

### Voici un Scrim Interactif pour Définir une Image de Fond avec React

<iframe src="https://scrimba.com/scrim/co9b0447ba3a6a610fe96f96b?embed=freecodecamp,mini-header,no-sidebar" width="100%" height="420"></iframe>

## Comment Définir une Image de Fond dans React en Utilisant une URL Externe

Si votre image est située quelque part en ligne, vous pouvez définir l'image de fond de votre élément en plaçant l'URL comme ceci :

```jsx
function App() {
  return (
    <div style={{ 
      backgroundImage: `url("https://via.placeholder.com/500")` 
    }}>
      Bonjour le Monde
    </div>
  );
}
```

Le code ci-dessus rendra un seul élément `<div>` avec le style `background-image: url([https://via.placeholder.com/500](https://via.placeholder.com/500))` appliqué.

## Comment Définir une Image de Fond dans React à Partir de Votre Dossier /src

Si vous initialisez votre application avec Create React App et que votre image se trouve dans le dossier `src/`, vous pouvez d'abord `importer` l'image, puis la placer comme fond de votre élément :

```jsx
import React from "react";
import background from "./img/placeholder.png";

function App() {
  return (
    <div style={{ backgroundImage: `url(${background})` }}>
      Bonjour le Monde
    </div>
  );
}

export default App;
```

Lorsque vous exécutez la commande `npm start`, React affichera une erreur "Failed to Compile" et arrêtera la construction si l'image est introuvable :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/React-failed-to-compile-image.png)
_React a échoué à compiler. L'image est introuvable._

Ainsi, vous n'afficherez aucun lien d'image brisé sur votre application web. Dans le code ci-dessus, la valeur de `backgroundImage` est définie en utilisant une chaîne de modèle, ce qui vous permet d'intégrer des expressions JavaScript.

## Comment Définir une Image de Fond dans React en Utilisant la Méthode d'URL Relative

Le dossier `public/` dans Create React App peut être utilisé pour ajouter des actifs statiques à votre application React. Tous les fichiers que vous placez dans ce dossier seront accessibles en ligne.

Si vous placez un fichier `image.png` dans le dossier `public/`, vous pouvez y accéder à l'adresse `<votre adresse hôte>/image.png`. Lorsque vous exécutez React sur votre ordinateur local, l'image devrait être à l'adresse `http://localhost:3000/image.png`.

Vous pouvez ensuite attribuer l'URL relative à votre adresse hôte pour définir l'image de fond. Voici un exemple :

```jsx
<div style={{ backgroundImage: "url(/image.png)" }}>
  Bonjour le Monde
</div>
```

En définissant le chemin de l'URL sur `/image.png` comme dans l'exemple ci-dessus, le navigateur recherchera l'image de fond à l'adresse `<votre adresse hôte>/image.png`.

Vous pouvez également créer un autre dossier dans `public/` si vous souhaitez organiser vos images dans des dossiers. Par exemple :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/Screen-Shot-2020-12-14-at-20.18.30.png)
_Création d'un dossier img/ dans le dossier public/_

N'oubliez pas d'ajuster la valeur de `backgroundImage` à `url(/img/image.png)` si vous décidez de créer le dossier.

## Comment Définir une Image de Fond dans React en Utilisant la Méthode d'URL Absolue

Vous pouvez également inclure l'URL absolue en utilisant la variable d'environnement `PUBLIC_URL` de Create React App comme ceci :

```jsx
<div style={{ 
  backgroundImage: `url(${process.env.PUBLIC_URL + '/image.png'})` 
}}>
  Bonjour le Monde
</div>
```

Lorsque vous exécutez cela sur votre ordinateur local, les scripts React géreront la valeur de la variable `PUBLIC_URL`. Lorsque vous l'exécutez localement, cela ressemblera à une URL relative au lieu d'une URL absolue :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/absolute-url-background-image-1.png)
_L'URL absolue de l'image n'est pas affichée sur l'ordinateur local_

L'URL absolue ne sera visible que lorsque vous déployez React dans une application de production.

## Comment Définir une Image de Fond avec des Propriétés Supplémentaires

Si vous souhaitez personnaliser davantage l'image de fond, vous pouvez le faire en ajoutant des propriétés supplémentaires après `backgroundImage`. Voici un exemple :

```jsx

<div style={{ 
  backgroundImage: `url(${process.env.PUBLIC_URL + '/image.png'})`,
  backgroundRepeat: 'no-repeat',
  width:'250px' 
}}>
  Bonjour le Monde
</div>
```

Les propriétés définies ci-dessus ajouteront `background-repeat: no-repeat` et `width: 250px` ainsi que le style `background-image` à l'élément `<div>`.

Merci d'avoir lu. Si vous avez aimé cet article et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre _Beginning Modern JavaScript_ [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png)](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif et doux qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : _Vous comprendrez vraiment ce que vous faites avec JavaScript._

À la prochaine !