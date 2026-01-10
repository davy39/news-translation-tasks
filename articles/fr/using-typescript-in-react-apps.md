---
title: Comment utiliser TypeScript dans les applications React
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-01-30T16:59:27.000Z'
originalURL: https://freecodecamp.org/news/using-typescript-in-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/bruno-martins-OhJmwB4XWLE-unsplash.jpg
tags:
- name: React
  slug: react
- name: TypeScript
  slug: typescript
seo_title: Comment utiliser TypeScript dans les applications React
seo_desc: 'Hi everyone! A while ago I wrote an article about TypeScript, explaining
  its main features and why it''s a good idea to use it in large projects.

  Today we''re going to take a quick look at how we can use TypeScript in a React
  app, so you can get an ide...'
---

Bonjour à tous ! Il y a quelque temps, j'ai écrit [un article sur TypeScript](https://www.freecodecamp.org/news/an-introduction-to-typescript/), expliquant ses principales fonctionnalités et pourquoi c'est une bonne idée de l'utiliser dans les grands projets.

Aujourd'hui, nous allons jeter un coup d'œil rapide à la façon dont nous pouvons utiliser TypeScript dans une application React, afin que vous puissiez vous faire une idée de ce à quoi pourrait ressembler l'implémentation et quels sont ses avantages.

## **Table des matières**

* [Intro à TypeScript](#intro-a-typescript)
    
* [Comment typer les Props](#heading-comment-typer-les-props)
    
* [Comment typer les Hooks](#heading-comment-typer-les-hooks)
    
    * [Typer le hook useState](#heading-typer-le-hook-usestate)
        
    * [Typer le hook useRef](#heading-typer-le-hook-useref)
        
* [Conclusion](#heading-conclusion)
    

## Intro à TypeScript

À ce stade, vous devriez savoir que TypeScript est un sur-ensemble de JavaScript. Sur-ensemble signifie qu'il ajoute des fonctionnalités à ce que JavaScript offre.

TypeScript prend toutes les fonctionnalités et structures que JavaScript fournit en tant que langage, et y ajoute quelques éléments. La principale chose que TypeScript fournit est le typage statique.

En ce qui concerne React, outre tout ce que nous pouvons typer en vanilla JS (comme les variables, les paramètres de fonction et les valeurs de retour, etc.), nous pouvons principalement utiliser TypeScript pour typer deux choses : les props des composants et les hooks.

L'une des façons les plus simples de créer une application React avec TypeScript est d'utiliser [CRA](https://create-react-app.dev/docs/adding-typescript/), en exécutant `npx create-react-app my-app --template typescript`.

Si vous avez déjà une application CRA créée, dans la documentation vous avez des informations sur la façon d'installer TypeScript par-dessus. ;)

De plus, pour les exemples ici, nous allons utiliser CRA car c'est simple et pratique. Mais gardez à l'esprit que la plupart des frameworks comme [Next](https://nextjs.org/docs/basic-features/typescript), [Vite](https://vitejs.dev/guide/features.html#typescript) et [Astro](https://docs.astro.build/en/guides/typescript/) fournissent également un support pour TypeScript.

Ainsi, après avoir exécuté le script de CRA, vous aurez un projet qui ressemble quelque peu à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-299.png align="left")

Comme vous pouvez le voir, les fichiers sont maintenant nommés `.tsx`, ce qui est la façon dont le compilateur de TypeScript identifie que vous utiliserez TypeScript dans ce fichier.

Et en plus, nous avons un `tsconfig.json` qui est l'endroit où nous avons toute la configuration du compilateur. Vous pouvez en apprendre plus à ce sujet dans [l'article précédent que j'ai écrit](https://www.freecodecamp.org/news/an-introduction-to-typescript/#typescriptscompiler).

Maintenant, créons un composant et voyons comment nous pouvons utiliser TypeScript.

## Comment typer les Props

Pour cet exemple, nous allons configurer un composant factice responsable du rendu d'un nombre reçu en tant que props, et de l'ajout à ce nombre lorsqu'un bouton est cliqué.

Le code JavaScript régulier ressemblerait à quelque chose comme ceci :

```javascript
const DummyComponent = ({ number, setNumber }) => {

  return (
    <>
      <div>{number}</div>

      <button
        onClick={() => setNumber(prev => prev+1)}
      >
        ADD
      </button>
    </>
  )

}

export default DummyComponent
```

Et notre version entièrement typée ressemblera à ceci :

```javascript
import React, { Dispatch, SetStateAction } from 'react'

interface DummyProps {
  number: number
  setNumber: Dispatch<SetStateAction<number>>
}

const DummyComponent:React.FC<DummyProps> = ({ number, setNumber }) => {

  return (
    <>
      <div>{number}</div>

      <button
        onClick={() => setNumber(prev => prev+1)}
      >
        ADD
      </button>
    </>
  )

}

export default DummyComponent
```

Vous pouvez voir qu'à côté du nom du composant, nous avons ajouté des deux-points et `React.FC`. Cela indique essentiellement au composant TypeScript que `DummyComponent` est un composant fonctionnel React. Cela ne fait pas grand-chose en soi, mais cela aide avec l'intellisense de TypeScript.

À côté de cela, nous avons déclaré `<DummyProps>`. Cela déclare que l'objet props que ce composant recevra doit correspondre à l'interface `DummyProps`.

Une interface est la manière de TypeScript de typer un objet. Basiquement, nous déclarons toutes les propriétés que l'objet aura, et le type pour chacune d'entre elles.

Puisque ce composant recevra un état qui est un nombre, et une fonction pour mettre à jour cet état, c'est exactement ce que nous avons dans notre interface :

```javascript
interface DummyProps {
  number: number
  setNumber: Dispatch<SetStateAction<number>>
}
```

Ici, vous pouvez voir que pour la fonction `setNumber`, nous utilisons ce type : `Dispatch<SetStateAction>`. Ce n'est pas un type natif de TypeScript, mais il est fourni par React lui-même. Nous devons donc l'importer chaque fois que nous l'utilisons, comme ceci :  
`import React, { Dispatch, SetStateAction } from 'react'`.

Et c'est tout ! Vous avez maintenant typé vos props. Ce qui est cool avec cela, c'est que chaque fois que vous appelez ce composant, vous obtiendrez l'intellisense sur les props que le composant attend. De même, si vous essayez de passer une prop non déclarée dans l'interface du composant ou de fournir un type incorrect pour une prop attendue.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-300.png align="left")

*Intellisense sur les props attendues*

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-301.png align="left")

*Erreur de props inattendues*

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-302.png align="left")

*Mauvais type de prop*

C'est ce que les gens veulent dire lorsqu'ils disent que TypeScript auto-documente votre code. Avec juste quelques lignes de code standard, vous pouvez maintenant facilement voir ce que chaque composant attend et ce qu'il n'attend pas. Cela s'avère très utile lorsque vous travaillez sur de grands projets, avec des centaines de composants écrits principalement par d'autres personnes. ;)

## Comment typer les Hooks

En ce qui concerne les hooks, TypeScript est principalement utilisé pour typer les hooks `useState` et `useRef`. Voyons comment cela fonctionne.

#### Typer le hook `useState`

Voici à quoi ressemble `useState` sans types :

```javascript
const [number, setNumber] = useState<>(0)
```

Et avec les types, cela ressemble à ceci :

```javascript
const [number, setNumber] = useState<number>(0)
```

Presque pas besoin d'expliquer, n'est-ce pas ? Nous déclarons simplement le type de la valeur de l'état comme ceci : `<number>` et c'est tout. Si nous essayons jamais de mettre à jour cet état avec un type de valeur différent, nous obtiendrons un joli message d'erreur rouge pour nous empêcher de nous tirer une balle dans le pied. ;)

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-303.png align="left")

*Erreur de mauvais type*

Gardez à l'esprit que si nous voulons permettre à notre état de contenir différents types de valeurs, nous pouvons déclarer cela comme ceci : `const [number, setNumber] = useState<number | string>(0)`.

Maintenant, nous pouvons passer soit un nombre, soit une chaîne sans obtenir d'erreurs.

### Typer le hook `useRef`

`useRef` est un hook principalement utilisé pour référencer des éléments du DOM dans React. Si vous voulez en savoir plus sur le fonctionnement du hook, vous pouvez lire [ce guide](https://www.freecodecamp.org/news/full-guide-to-react-hooks/#useRef-hook) que j'ai récemment écrit.

Pour voir comment nous pouvons l'implémenter avec TypeScript, nous allons utiliser cet exemple :

```javascript
import React, { useEffect, useRef } from 'react'

const DummyComponent:React.FC = () => {

  const ref = useRef<HTMLInputElement>(null)

  useEffect(() => {
    if (ref.current) ref.current.focus()
  }, [])

  return (
      <input type="text" ref={ref} />
  )

}

export default DummyComponent
```

Comme vous pouvez le voir, nous initialisons la variable `ref` avec `null` et déclarons son type comme `HTMLInputElement`. Lorsque nous utilisons le hook useRef et déclarons son type, la variable peut être assignée soit à `null`, soit au type déclaré.

Ensuite, nous avons un hook `useEffect` qui se concentre sur l'élément s'il a une propriété `current`. Et enfin, nous retournons un élément `input` et assignons la référence que nous avons précédemment déclarée : `ref={ref}`.

Le côté cool de typer le hook `useRef` est que TypeScript nous empêchera d'essayer d'effectuer des actions ou de lire des données à partir de types qui ne correspondent pas.

Par exemple, si nous déclarions le type `number` pour la ref, nous obtiendrions les erreurs suivantes :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-364.png align="left")

*Impossible de se concentrer sur le type number*

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-365.png align="left")

*Impossible d'assigner une référence de nombre à un élément HTML*

Encore une fois, c'est bien car cela évite des erreurs stupides à l'avance et nous évite d'avoir à déboguer ces choses plus tard. Surtout lorsque vous travaillez avec de grandes bases de code où de nombreuses autres personnes travaillent également, TypeScript nous donne un environnement plus contrôlé et ordonné pour travailler.

## Conclusion

Eh bien, tout le monde, comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous souhaitez une analyse plus approfondie de ce sujet, je recommande [cette vidéo par Firebase](https://www.youtube.com/watch?v=ydkQlJhodio) ou cette autre par [Ben Awad](https://www.youtube.com/watch?v=Z5iWr6Srsj8).

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/01/goodbye-farewell.gif align="left")