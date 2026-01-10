---
title: Comment convertir les Hooks React en HOCs pour les composants hérités
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-07T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/react-hooks-to-hocs
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/hooks-to-hoc.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
seo_title: Comment convertir les Hooks React en HOCs pour les composants hérités
seo_desc: 'By Rico Kahler

  Super TL;DR: here ? https://github.com/ricokahler/hocify ? is a library that converts
  hooks into HOCs.

  Scenario: You made this beautiful custom hook and you''re happily using it in your
  new function components. You then realize that thi...'
---

Par Rico Kahler

**Super TL;DR :** voici ? [https://github.com/ricokahler/hocify](https://github.com/ricokahler/hocify) ? une bibliothèque qui convertit les hooks en HOCs.

Scénario : Vous avez créé ce magnifique [hook personnalisé](https://reactjs.org/docs/hooks-custom.html) et vous l'utilisez joyeusement dans vos nouveaux composants fonctionnels. Vous réalisez ensuite que ce hook personnalisé pourrait être utilisé dans l'un de vos anciens composants basés sur des classes, alors vous essayez de l'utiliser en le plaçant comme ceci...

```js
import React from 'react';
import useCoolCustomHook from './useCoolCustomHook';

class ClassComponent extends React.Component {
  // ...
  
  render() {
    // ? alerte spoiler : cela ne fonctionne pas
    const coolStuff = useCoolCustomHook();

    return <div>{/* ... */}</div>
  }
}

export default ClassComponent;
```

...mais ensuite vous voyez ce message d'erreur :

![Image](https://www.freecodecamp.org/news/content/images/2019/10/image-4.png)
_Ceci est le message d'erreur réel que vous obtenez lorsque vous essayez d'utiliser des hooks dans un composant de classe._

Disons que ce composant est vraiment complexe et déjà bien testé. Vous préféreriez ne pas réécrire le composant basé sur une classe en tant que composant fonctionnel, et vous préféreriez ne pas réécrire votre hook personnalisé en tant que composant d'ordre supérieur.

Que faites-vous dans cette situation ?

---

**TL;DR,** J'ai écrit une bibliothèque `hocify`, qui convertit les hooks en HOCs afin qu'ils puissent être utilisés dans des composants basés sur des classes.

Consultez la bibliothèque ici : [https://github.com/ricokahler/hocify](https://github.com/ricokahler/hocify)

Cependant, si vous êtes curieux de savoir comment j'en suis arrivé là, continuez à lire pour l'histoire complète !

---

Les hooks sont géniaux ! Ils sont la [réponse de l'équipe React à de nombreux problèmes dans React aujourd'hui](https://youtu.be/dpw9EHDh2bM?t=757). Cependant, leur utilisation vient avec un prérequis :

> Les hooks ne peuvent être appelés qu'à l'intérieur du corps d'un composant fonctionnel.

C'est malheureux car cela nous empêche d'utiliser des modules plus récents basés sur des hooks dans nos anciens composants basés sur des classes.

Heureusement pour nous, il existe des moyens astucieux de contourner cela. Cet article expliquera comment convertir des hooks en HOCs afin qu'ils puissent être utilisés dans des composants de classe.

> **Avertissement :** Le but d'utiliser des hooks dans des composants de classe est plus pour la compatibilité des modules plus récents basés sur des hooks avec des composants plus anciens basés sur des classes. Si votre composant est déjà implémenté en tant que fonction, alors utilisez le hook directement. Si vous écrivez un nouveau composant, essayez de l'écrire en tant que composant fonctionnel.

## L'exemple de hook : useMousePosition

Commençons par créer un hook personnalisé que nous voulons utiliser dans un composant de classe.

Le hook que nous allons créer capturera les positions `x` et `y` actuelles de la souris sur l'écran et les rapportera au composant.

? `useMousePosition.js` : le hook personnalisé

```js
import { useState, useEffect } from 'react';

function useMousePosition() {
  const [x, setX] = useState(0);
  const [y, setY] = useState(0);
  
  useEffect(() => {
    const handleMouseMove = e => {
      setX(e.clientX);
      setY(e.clientY);
    };

    document.addEventListener('mousemove', handleMouseMove);
    
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);
    
  return { x, y };
}

export default useMousePosition;
```

? `ExampleComponent.js` : exemple d'utilisation du hook ci-dessus

```js
import React from 'react';
import useMousePosition from './useMousePosition';

function ExampleComponent() {
  const { x, y } = useMousePosition();
    
  return <div>Position actuelle de la souris : ({x}, {y})</div>;
}

export default ExampleComponent;
```

[**Voir la démonstration.**](https://codesandbox.io/s/boring-babbage-959ow?fontsize=14)

Nous utiliserons ce hook dans le reste des exemples.

## Réalisation 1 : Vous pouvez utiliser des hooks dans des composants de classe en les enveloppant et en passant des props.

La première étape de ce voyage est de déterminer comment obtenir les données et les effets du hook dans un composant de classe.

Les hooks ne peuvent être utilisés que dans des composants fonctionnels, donc une option que nous avons est d'envelopper le composant de classe avec un composant fonctionnel et de passer les données requises en tant que props.

```js
import React from 'react';

class ClassComponent extends React.Component {
  render() {
    const { x, y } = this.props;
      
    return <div>Position actuelle de la souris : ({x}, {y})</div>;
  }
}

function WrapperComponent() {
  const { x, y } = useMousePosition();
  
  return <ClassComponent x={x} y={y} />;
}

export default WrapperComponent;
```

[**Voir la démonstration.**](https://codesandbox.io/s/hocify-example-hook-0lyjx?fontsize=14)

## Réalisation 2 : Vous pouvez écrire une fonction qui prend un composant et retourne un composant enveloppé.

L'étape suivante est de rendre cet enveloppement générique afin que nous puissions appliquer ce hook à _n'importe quelle_ classe.

Nous pouvons le faire en utilisant des [composants d'ordre supérieur (aka HOCs)](https://reactjs.org/docs/higher-order-components.html). Les HOCs sont des fonctions qui prennent un composant et retournent un autre composant qui enveloppe le composant d'entrée. Ce modèle nous permet d'injecter des props au composant d'entrée à partir du composant d'enveloppement.

Si le composant enveloppant retourné est implémenté en utilisant une fonction, alors nous pouvons utiliser des hooks là-dedans !

```js
function withMousePosition(Component) {  
  function WrappedComponent(props) {
    const { x, y } = useMousePosition();
      
    return <Component x={x} y={y} {...props} />;
  }
    
  return WrappedComponent;
}

class ClassComponent extends React.Component {
  render() {
    const { x, y } = this.props;
      
    return <div>Position actuelle de la souris : ({x}, {y})</div>;
  }
}

export default withMousePosition(ClassComponent);
```

[**Voir la démonstration.**](https://codesandbox.io/s/hocify-realization-2-qyu09?fontsize=14)

## Réalisation 3 : Vous pouvez écrire une fonction qui prend un hook et retourne un HOC.

Pouvons-nous aller encore plus loin avec cette idée ?

Oui ! De la même manière que nous avons écrit une fonction qui retournait un composant, nous pouvons aller un cran plus haut et écrire une fonction qui prend un hook et retourne un composant d'ordre supérieur.

Le bloc de code suivant est la fonction `hocify` (c'est HOC-ify — similaire aux conventions `stringify` ou `promisify`).

`hocify` est une fonction qui prend un hook et retourne un HOC.

?  `hocify.js` 

```js
import React from 'react';

function hocify(useHook) {
  function hoc(InputComponent) {
    function WrapperComponent(props) {
      const result = useHook();
      
      return <InputComponent {...result} {...props} />
    }
      
    return WrapperComponent;
  }
    
  return hoc;
}

export default hocify;
```

? Utilisation dans `ClassComponent.js` :

```js
import React from 'react';
import hocify from 'hocify';
import useMousePosition from './useMousePosition';

const withMousePosition = hocify(useMousePosition);

class ClassComponent extends React.Component {
  render() {
    const { x, y } = this.props;
      
    return <div>Position actuelle de la souris : ({x}, {y})</div>;
  }
}

export default withMousePosition(ClassComponent);
```

[**Voir la démonstration.**](https://codesandbox.io/s/hocify-realization-3-3mmg9?fontsize=14)

> **Note :** Il pourrait être tentant d'appeler `hocify` un "higher order hook" ou un autre mélange de mots, mais je recommanderais de s'abstenir ?

## Réalisation 4 : Cette chose ne serait-elle pas bien dans un package ?

Probablement !

`npm install --save hocify` 

Consultez la bibliothèque ici : [https://github.com/ricokahler/hocify](https://github.com/ricokahler/hocify)

> **Dernière note :** Il y a quelques considérations dans la bibliothèque non mentionnées ici.  
> Lisez la documentation avant de l'utiliser.

Merci pour la lecture !