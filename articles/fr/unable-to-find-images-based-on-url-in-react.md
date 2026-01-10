---
title: Impossible de trouver des images basées sur l'URL dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:19:00.000Z'
originalURL: https://freecodecamp.org/news/unable-to-find-images-based-on-url-in-react
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9a93740569d1a4ca266c.jpg
tags:
- name: React
  slug: react
- name: toothbrush
  slug: toothbrush
- name: url
  slug: url
seo_title: Impossible de trouver des images basées sur l'URL dans React
seo_desc: "If you're new to React and are having trouble accessing images stored locally,\
  \ you're not alone.\nImagine you have your images stored in a directory next to\
  \ a component like this:\n/src\n  /components\n    - component1\n    - component2\n\
  /img\n  - img1\n  - ..."
---

Si vous êtes nouveau dans React et que vous avez des difficultés à accéder aux images stockées localement, vous n'êtes pas seul.

Imaginez que vous avez vos images stockées dans un répertoire à côté d'un composant comme ceci :

```
/src
  /components
    - component1
    - component2
/img
  - img1
  - img2
```

Et vous essayez d'accéder aux images dans le répertoire `/img` depuis `component2` :

```jsx
import React, { Component, useState, useEffect } from 'react';
import { render } from 'react-dom'
import { useTransition, animated, config } from "react-spring";
import imgArr from './images';
import '../App.css';

const Slideshow = () => {
  const [index, set] = useState(0)
  const transitions = useTransition(imgArr[index], item => item.id, {
    from: { opacity: 0 },
    enter: {opacity: 1 },
    leave: { opacity: 0 },
    config: config.molasses,
  })
  useEffect(() => void setInterval(() => set(state => (state + 1) % 4), 2000), [])
  return transitions.map(({ item, props, key }) => (
    <animated.div
      key={key}
      className="bg"
      style={{ ...props, slideshowContainerStyle}}
    >
      <img className="img" src={require(item.url)} alt=""/>
    </animated.div>
  ))
}

const slideshowContainerStyle = {
 width: '80%',
 height: '300px'
}


export default Slideshow;

```

Vous avez essayé les chemins `../img/img1.jpg` et `..img/img1.jpg`, mais vous obtenez `Error: Cannot find module '<path>'` .

Alors, que se passe-t-il ici ?

## Un peu sur `create-react-app`

Comme la plupart des gens, vous avez probablement utilisé `create-react-app` pour démarrer votre projet.

Dans ce cas, l'utilisation de chemins relatifs peut être un peu délicate car `create-react-app` construit les fichiers HTML, CSS et JavaScript dans un dossier de sortie :

```
/public
  - index.html
  - bundle.js
  - style.css
```

Il existe plusieurs façons d'utiliser des images avec `create-react-app`, mais l'une des plus simples est d'inclure vos images dans `/public`. Lorsque votre projet est construit, `/public` sert de répertoire racine.

Vous pouvez en savoir plus sur l'ajout d'images ou d'autres actifs dans la [documentation de Create React App](https://create-react-app.dev/docs/adding-images-fonts-and-files/).

## Importation d'images

Si vous avez consulté la documentation, vous remarquerez que le code inclut des instructions `import` pour charger des actifs comme des images et des polices.

L'importation est utile lorsque votre actif, dans ce cas une image, se trouve dans le même répertoire ou près du composant qui l'utilise, et ne sera utilisé nulle part ailleurs. Par exemple, si vous avez un composant d'entrée avec des boutons qui utilisent des SVGs pour les icônes de pouce levé et de pouce baissé.

Un avantage de l'utilisation de `import` est qu'il générera une erreur lors de la construction si une faute de frappe est présente. Ce type de vérification aide à garantir que les utilisateurs ne verront pas une image cassée qui aurait pu passer inaperçue.