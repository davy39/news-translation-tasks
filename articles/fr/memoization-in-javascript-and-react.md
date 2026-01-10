---
title: Qu'est-ce que la mémoïsation ? Comment et quand mémoïser en JavaScript et React
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-04-26T21:16:12.000Z'
originalURL: https://freecodecamp.org/news/memoization-in-javascript-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-thisisengineering-3913016.jpg
tags:
- name: JavaScript
  slug: javascript
- name: optimization
  slug: optimization
- name: performance
  slug: performance
- name: React
  slug: react
- name: web performance
  slug: web-performance
seo_title: Qu'est-ce que la mémoïsation ? Comment et quand mémoïser en JavaScript
  et React
seo_desc: 'Hi everyone! In this article we will talk about memoization, an optimization
  technique that can help make heavy computation processes more efficient.

  We will start by talking about what memoization is and when it''s best to implement
  it. Later on we w...'
---

Bonjour à tous ! Dans cet article, nous allons parler de la mémoïsation, une technique d'optimisation qui peut aider à rendre les processus de calcul lourds plus efficaces.

Nous commencerons par parler de ce qu'est la mémoïsation et du moment où il est préférable de l'implémenter. Plus tard, nous donnerons des exemples pratiques pour JavaScript et React.

## Table des matières

* [Qu'est-ce que la mémoïsation](#heading-quest-ce-que-la-memoisation)
    
* [Comment fonctionne la mémoïsation](#heading-comment-fonctionne-la-memoisation)
    
* [Exemple de mémoïsation en JavaScript](#heading-exemple-de-memoisation-en-javascript)
    
* [Exemple de mémoïsation en React](#heading-exemple-de-memoisation-en-react)
    
    * [Composants purs](#heading-composants-purs)
        
    * [Classe PureComponent](#heading-classe-purecomponent)
        
    * [Composant d'ordre supérieur Memo](#heading-composant-dordre-superieur-memo)
        
    * [Quand utiliser le hook useCallback](#heading-quand-utiliser-le-hook-usecallback)
        
    * [Quand utiliser le hook useMemo](#heading-quand-utiliser-le-hook-usememo)
        
    * [Quand mémoïser](#heading-quand-memoiser)
        
* [Résumé](#heading-resume)
    

# Qu'est-ce que la mémoïsation ?

En programmation, **la mémoïsation est une technique d'optimisation** qui rend les applications plus efficaces et donc plus rapides. Elle le fait en stockant les résultats des calculs dans un cache, et en récupérant ces mêmes informations depuis le cache la prochaine fois qu'elles sont nécessaires au lieu de les recalculer.

En termes plus simples, cela consiste à stocker dans un **cache** la sortie d'une fonction, et à faire vérifier par la fonction si chaque calcul requis est dans le cache avant de le calculer.

Un **cache** est simplement un stockage de données temporaire qui contient des données afin que les demandes futures pour ces données puissent être servies plus rapidement.

La mémoïsation est un truc simple mais puissant qui peut aider à accélérer notre code, surtout lorsqu'on traite avec des fonctions de calcul répétitives et lourdes.

# Comment fonctionne la mémoïsation ?

Le concept de mémoïsation en JavaScript repose sur deux concepts :

* **Closures** : La combinaison d'une fonction et de l'environnement lexical dans lequel cette fonction a été déclarée. Vous pouvez en lire plus à leur sujet [ici](https://www.freecodecamp.org/news/closures-in-javascript/) et [ici](https://www.freecodecamp.org/news/scope-and-closures-in-javascript/).
    
* **Fonctions d'ordre supérieur** : Fonctions qui opèrent sur d'autres fonctions, soit en les prenant comme arguments, soit en les retournant. Vous pouvez en lire plus à leur sujet [ici](https://www.freecodecamp.org/news/higher-order-functions-in-javascript-examples/).
    

# Exemple de mémoïsation en JavaScript

Pour clarifier ce charabia, nous utiliserons l'exemple classique de la suite de Fibonacci.

La **suite de Fibonacci** est un ensemble de nombres qui commence par un ou un zéro, suivi d'un un, et qui se poursuit selon la règle que chaque nombre (appelé nombre de Fibonacci) est égal à la somme des deux nombres précédents.

Cela ressemble à ceci :

```javascript
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
```

Disons que nous devons écrire une fonction qui retourne le n-ième élément de la suite de Fibonacci. Sachant que chaque élément est la somme des deux précédents, une solution récursive pourrait être la suivante :

```javascript
const fib = n => {
  if (n <= 1) return 1
  return fib(n - 1) + fib(n - 2)
}
```

Si vous n'êtes pas familier avec la récursivité, c'est simplement le concept d'une fonction qui s'appelle elle-même, avec une sorte de cas de base pour éviter une boucle infinie (dans notre cas `if (n <= 1)`).

Si nous appelons notre fonction comme `fib(5)`, en coulisses notre fonction s'exécuterait comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Untitled-Diagram.drawio.png align="left")

Voyez que nous exécutons `fib(0), fib(1), fib(2) et fib(3)` plusieurs fois. Eh bien, c'est exactement le genre de problème que la mémoïsation aide à résoudre.

Avec la mémoïsation, il n'est pas nécessaire de recalculer les mêmes valeurs encore et encore – nous stockons simplement chaque calcul et retournons la même valeur lorsqu'elle est requise à nouveau.

En implémentant la mémoïsation, notre fonction ressemblerait à ceci :

```javascript
const fib = (n, memo) => {
    memo = memo || {}

    if (memo[n]) return memo[n]

    if (n <= 1) return 1
    return memo[n] = fib(n-1, memo) + fib(n-2, memo)
}
```

Ce que nous faisons d'abord, c'est vérifier si nous avons reçu l'objet **memo** en tant que paramètre. Si ce n'est pas le cas, nous le définissons comme un objet vide :

```javascript
memo = memo || {}
```

Ensuite, nous vérifions si memo contient la valeur que nous recevons en tant que paramètre dans ses clés. Si c'est le cas, nous la retournons. C'est là que la magie opère. Plus besoin de récursivité une fois que nous avons notre valeur stockée dans memo. =)

```javascript
if (memo[n]) return memo[n]
```

Si nous n'avons pas encore la valeur dans memo, nous appelons **fib** à nouveau, mais en passant maintenant **memo** en tant que paramètre, de sorte que les fonctions que nous appelons partageront les mêmes valeurs mémoïsées que nous avons dans la fonction "originale". Remarquez que nous ajoutons le résultat final au cache avant de le retourner.

```javascript
return memo[n] = fib(n-1, memo) + fib(n-2, memo)
```

Et c'est tout ! Avec deux lignes de code, nous avons implémenté la mémoïsation et significativement amélioré la performance de notre fonction !

# Exemple de mémoïsation en React

Dans React, nous pouvons optimiser notre application en évitant les re-rendus inutiles de composants en utilisant la mémoïsation.

Comme je l'ai mentionné également dans [cet autre article sur la gestion de l'état dans React](https://www.freecodecamp.org/news/how-to-manage-state-in-a-react-app/), les composants se re-rendent à cause de deux choses : un **changement d'état** ou un **changement de props**. C'est précisément l'information que nous pouvons "mettre en cache" pour éviter les re-rendus inutiles.

Mais avant de pouvoir passer au code, introduisons quelques concepts importants.

## Composants purs

React supporte les composants de classe ou fonctionnels. Un composant fonctionnel est une fonction JavaScript simple qui retourne du JSX, et un composant de classe est une classe JavaScript qui étend React.Component et retourne du JSX à l'intérieur d'une méthode render.

Et qu'est-ce qu'un composant pur alors ? Eh bien, basé sur le concept de pureté dans les paradigmes de programmation fonctionnelle, une fonction est dite pure si :

* Sa valeur de retour est uniquement déterminée par ses valeurs d'entrée
    
* Sa valeur de retour est toujours la même pour les mêmes valeurs d'entrée
    

De la même manière, un composant React est considéré comme pur s'il rend la même sortie pour le même état et les mêmes props.

Un composant fonctionnel pur pourrait ressembler à ceci :

```javascript
// Composant pur
export default function PureComponent({name, lastName}) {
  return (
    <div>Mon nom est {name} {lastName}</div>
  )
}
```

Voyez que nous passons deux props, et le composant rend ces deux props. Si les props sont les mêmes, le rendu sera toujours le même.

De l'autre côté, disons par exemple que nous ajoutons un nombre aléatoire à chaque prop avant le rendu. Alors la sortie pourrait être différente même si les props restent les mêmes, donc ce serait un composant impur.

```javascript
// Composant impur
export default function ImpurePureComponent({name, lastName}) {
  return (
    <div>Mon nom "impur" est {name + Math.random()} {lastName + Math.random()}</div>
  )
}
```

Les mêmes exemples avec des composants de classe seraient :

```plaintext
// Composant pur
class PureComponent extends React.Component {
    render() {
      return (
        <div>Mon nom est {this.props.name} {this.props.lastName}</div>
      )
    }
  }

export default PureComponent
```

```javascript
// Composant impur
class ImpurePureComponent extends React.Component {
    render() {
      return (
        <div>Mon nom "impur" est {this.props.name + Math.random()} {this.props.lastName + Math.random()}</div>
      )
    }
  }

export default ImpurePureComponent
```

## Classe PureComponent

Pour les **composants de classe purs**, pour implémenter la mémoïsation, React fournit la classe de base `PureComponent`.

Les composants de classe qui étendent la classe `React.PureComponent` ont certaines améliorations de performance et des optimisations de rendu. Cela est dû au fait que React implémente la méthode `shouldComponentUpdate()` pour eux avec une **comparaison superficielle pour les props et l'état**.

Voyons cela dans un exemple. Ici, nous avons un composant de classe qui est un compteur, avec des boutons pour changer ce compteur en ajoutant ou en soustrayant des nombres. Nous avons également un composant enfant auquel nous passons une prop name qui est une chaîne de caractères.

```javascript
import React from "react"
import Child from "./child"

class Counter extends React.Component {
    constructor(props) {
      super(props)
      this.state = { count: 0 }
    }

    handleIncrement = () => { this.setState(prevState => {
        return { count: prevState.count - 1 };
      })
    }

    handleDecrement = () => { this.setState(prevState => {
        return { count: prevState.count + 1 };
      })
    }

    render() {
      console.log("Parent render")

      return (
        <div className="App">

          <button onClick={this.handleIncrement}>Increment</button>
          <button onClick={this.handleDecrement}>Decrement</button>

          <h2>{this.state.count}</h2>

          <Child name={"Skinny Jack"} />
        </div>
      )
    }
  }

  export default Counter
```

Le composant enfant est un **composant pur** qui rend simplement la prop reçue.

```javascript
import React from "react"

class Child extends React.Component {
    render() {
      console.log("Skinny Jack")
      return (
          <h2>{this.props.name}</h2>
      )
    }
  }

export default Child
```

Remarquez que nous avons ajouté des console.logs aux deux composants afin d'obtenir des messages de console chaque fois qu'ils se rendent. Et à ce sujet, devinez ce qui se passe lorsque nous appuyons sur les boutons d'incrémentation ou de décrémentation ? Notre console ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/2022-04-24_21-59.png align="left")

Le composant enfant se re-rend même s'il reçoit toujours la même prop.

Pour implémenter la mémoïsation et optimiser cette situation, nous devons étendre la classe `React.PureComponent` dans notre composant enfant, comme ceci :

```javascript
import React from "react"

class Child extends React.PureComponent {
    render() {
      console.log("Skinny Jack")
      return (
          <h2>{this.props.name}</h2>
      )
    }
  }

export default Child
```

Après cela, si nous appuyons sur le bouton d'incrémentation ou de décrémentation, notre console ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/2022-04-24_22-00.png align="left")

Seulement le rendu initial du composant enfant et aucun re-rendu inutile lorsque la prop n'a pas changé. Facile comme bonjour. ;)

Avec cela, nous avons couvert les composants de classe, mais dans les composants fonctionnels, nous ne pouvons pas étendre la classe `React.PureComponent`. Au lieu de cela, React offre un HOC et deux hooks pour gérer la mémoïsation.

## **Composant d'ordre supérieur Memo**

Si nous transformons notre exemple précédent en composants fonctionnels, nous obtiendrions ce qui suit :

```javascript
import { useState } from 'react'
import Child from "./child"

export default function Counter() {

    const [count, setCount] = useState(0)

    const handleIncrement = () => setCount(count+1)
    const handleDecrement = () => setCount(count-1)

    return (
        <div className="App">
            {console.log('parent')}
            <button onClick={() => handleIncrement()}>Increment</button>
            <button onClick={() => handleDecrement()}>Decrement</button>

            <h2>{count}</h2>

            <Child name={"Skinny Jack"} />
        </div>                    
    )
}
```

```javascript
import React from 'react'

export default function Child({name}) {
console.log("Skinny Jack")
  return (
    <div>{name}</div>
  )
}
```

Cela provoquerait le même problème qu'avant, où le composant Child se re-rendait inutilement. Pour le résoudre, nous pouvons envelopper notre composant enfant dans le composant d'ordre supérieur `memo`, comme suit :

```javascript
import React from 'react'

export default React.memo(function Child({name}) {
console.log("Skinny Jack")
  return (
    <div>{name}</div>
  )
})
```

Un **composant d'ordre supérieur ou HOC** est similaire à une fonction d'ordre supérieur en javascript. Les fonctions d'ordre supérieur sont des fonctions qui prennent d'autres fonctions comme arguments OU retournent d'autres fonctions. Les HOC de React prennent un composant comme prop, et le manipulent à une fin sans changer le composant lui-même. Vous pouvez penser à cela comme des composants enveloppants.

Dans ce cas, `memo` fait un travail similaire à `PureComponent`, évitant les re-rendus inutiles des composants qu'il enveloppe.

## Quand utiliser le hook useCallback

Une chose importante à mentionner est que memo ne fonctionne pas si la prop passée au composant est une fonction. Refactorisons notre exemple pour voir cela :

```javascript
import { useState } from 'react'
import Child from "./child"

export default function Counter() {

    const [count, setCount] = useState(0)

    const handleIncrement = () => setCount(count+1)
    const handleDecrement = () => setCount(count-1)

    return (
        <div className="App">
            {console.log('parent')}
            <button onClick={() => handleIncrement()}>Increment</button>
            <button onClick={() => handleDecrement()}>Decrement</button>

            <h2>{count}</h2>

            <Child name={console.log('Really Skinny Jack')} />
        </div>                    
    )
}
```

```javascript
import React from 'react'

export default React.memo(function Child({name}) {
console.log("Skinny Jack")
  return (
    <>
        {name()}
        <div>Really Skinny Jack</div>
    </>
  )
})
```

Maintenant, notre prop est une fonction qui journalise toujours la même chaîne, et notre console ressemblera à nouveau à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/2022-04-24_22-04.png align="left")

C'est parce qu'en réalité, une nouvelle fonction est créée à chaque re-rendu du composant parent. Donc, si une nouvelle fonction est créée, cela signifie que nous avons une nouvelle prop et que cela signifie que notre composant enfant doit également se re-rendre.

Pour résoudre ce problème, React fournit le hook **useCallback**. Nous pouvons l'implémenter de la manière suivante :

```javascript
import { useState, useCallback } from 'react'
import Child from "./child"

export default function Counter() {

    const [count, setCount] = useState(0)

    const handleIncrement = () => setCount(count+1)
    const handleDecrement = () => setCount(count-1)

    return (
        <div className="App">
            {console.log('parent')}
            <button onClick={() => handleIncrement()}>Increment</button>
            <button onClick={() => handleDecrement()}>Decrement</button>

            <h2>{count}</h2>

             <Child name={ useCallback(() => {console.log('Really Skinny Jack')}, [])  } />
        </div>                    
    )
}
```

Et cela résout le problème du re-rendu inutile de l'enfant.

Ce que fait useCallback, c'est de conserver la valeur de la fonction malgré le re-rendu du composant parent, de sorte que la prop de l'enfant restera la même tant que la valeur de la fonction restera la même également.

Pour l'utiliser, nous devons simplement envelopper le hook useCallback autour de la fonction que nous déclarons. Dans le tableau présent dans le hook, nous pouvons déclarer des variables qui déclencheraient le changement de la valeur de la fonction lorsque la variable change également (exactement de la même manière que useEffect fonctionne).

```javascript
const testingTheTest = useCallback(() => { 
    console.log("Tested");
  }, [a, b, c]);
```

## Quand utiliser le hook useMemo

**useMemo** est un hook très similaire à useCallback, mais au lieu de mettre en cache une fonction, useMemo mettra en cache la **valeur de retour d'une fonction**.

Dans cet exemple, `useMemo` mettra en cache le nombre `2`.

```plaintext
const num = 1
const answer = useMemo(() => num + 1, [num])
```

Alors que `useCallback` mettra en cache `() => num + 1`.

```plaintext
const num = 1
const answer = useMemo(() => num + 1, [num])
```

Vous pouvez utiliser useMemo de manière très similaire au HOC memo. La différence est que useMemo est un hook avec un tableau de dépendances, et memo est un HOC qui accepte en paramètre une fonction optionnelle qui utilise les props pour mettre à jour conditionnellement le composant.

De plus, useMemo met en cache une valeur retournée entre les rendus, tandis que memo met en cache un composant React entier entre les rendus.

## Quand mémoïser

La mémoïsation dans React est un bon outil à avoir dans notre ceinture, mais ce n'est pas quelque chose que vous devriez utiliser partout. Ces outils sont utiles pour traiter des fonctions ou des tâches qui nécessitent des calculs lourds.

Nous devons être conscients que, en arrière-plan, ces trois solutions ajoutent également des frais généraux à notre code. Donc, si le re-rendu est causé par des tâches qui ne sont pas lourds en calcul, il peut être préférable de le résoudre d'une autre manière ou de le laisser tel quel.

Je recommande [cet article de Kent C. Dodds](https://kentcdodds.com/blog/usememo-and-usecallback) pour plus d'informations sur ce sujet.

# **Résumé**

C'est tout, tout le monde ! Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

Santé et à la prochaine ! =D

![Image](https://www.freecodecamp.org/news/content/images/2022/04/goodbye-1.gif align="left")