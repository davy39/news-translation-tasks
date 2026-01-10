---
title: Comment gérer l'état dans une application React – Avec les Hooks, Redux et
  plus encore
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-03-21T23:31:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-state-in-a-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/lautaro-andreani-UYsBCu9RP3Y-unsplash.jpg
tags:
- name: React
  slug: react
- name: React
  slug: reactjs
- name: Redux
  slug: redux
- name: 'State Management '
  slug: state-management
seo_title: Comment gérer l'état dans une application React – Avec les Hooks, Redux
  et plus encore
seo_desc: 'Hi! In this article we''ll take a look at the many ways you can manage
  state in a React app.

  We''ll start by talking about what state is, and then go through the many tools
  you can use to manage it.

  We''ll look at the simple useState hook and also learn...'
---

Salut ! Dans cet article, nous allons examiner les nombreuses façons de gérer l'état dans une application React.

Nous commencerons par définir ce qu'est l'état, puis nous passerons en revue les nombreux outils que vous pouvez utiliser pour le gérer.

Nous verrons le simple hook useState et nous découvrirons également des bibliothèques plus complexes comme Redux. Ensuite, nous examinerons les options les plus récentes disponibles comme Recoil et Zustand.

## Table des matières

* [Qu'est-ce que l'état dans React ?](#heading-quest-ce-que-letat-dans-react)
    
* [Comment utiliser le Hook useState](#heading-comment-utiliser-le-hook-usestate)
    
    * [Comment utiliser useEffect pour lire les mises à jour de l'état](#heading-comment-utiliser-useeffect-pour-lire-les-mises-a-jour-de-letat)
        
    * [Comment passer un callback à la fonction de mise à jour de l'état](#heading-comment-passer-un-callback-a-la-fonction-de-mise-a-jour-de-letat)
        
* [Gérer l'échelle et la complexité](#heading-gerer-lechelle-et-la-complexite)
    
    * [Le contexte React](#heading-le-contexte-react)
        
    * [Comment utiliser le Hook useReducer](#heading-comment-utiliser-le-hook-usereducer)
        
    * [Et pour Redux ?](#heading-et-pour-redux)
        
* [Alternatives à Redux](#heading-alternatives-a-redux)
    
    * [Redux Toolkit](#heading-redux-toolkit)
        
        * [Une mention pour Redux Thunk et Redux Saga](#heading-une-mention-pour-redux-thunk-et-redux-saga)
            
    * [Recoil](#heading-recoil)
        
    * [Jotai](#heading-jotai)
        
    * [Zustand](#heading-zustand)
        
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce que l'état dans React ?

Dans le React moderne, nous construisons nos applications avec des **composants fonctionnels**. Les composants sont eux-mêmes des fonctions JavaScript, des morceaux de code indépendants et **réutilisables**.

L'objectif de la construction de l'application avec des composants est d'avoir une architecture modulaire, avec une séparation claire des préoccupations. Cela rend le code plus facile à comprendre, plus facile à maintenir et plus facile à réutiliser lorsque cela est possible.

L'**état est un objet qui contient des informations** sur un certain composant. Les fonctions JavaScript classiques n'ont pas la capacité de stocker des informations. Le code à l'intérieur s'exécute et "disparaît" une fois l'exécution terminée.

Mais grâce à l'état, les composants fonctionnels React peuvent stocker des informations même après l'exécution. Lorsque nous avons besoin qu'un composant stocke ou se "souvienne" de quelque chose, ou qu'il agisse d'une manière différente selon l'environnement, l'état est ce dont nous avons besoin pour qu'il fonctionne ainsi.

Il est important de mentionner que tous les composants d'une application React ne doivent pas nécessairement avoir un état. Il existe également des composants sans état (stateless) qui se contentent de rendre leur contenu sans avoir besoin de stocker d'informations, et c'est très bien ainsi.

Une autre chose importante à mentionner est que le changement d'état est l'une des deux choses qui provoquent le re-rendu d'un composant React (l'autre étant un changement de props). De cette façon, l'état stocke des informations sur le composant et contrôle également son comportement.

# Comment utiliser le Hook useState

Pour implémenter l'état dans nos composants, React nous fournit un hook appelé **useState**. Voyons comment il fonctionne avec l'exemple suivant.

Nous utiliserons l'exemple classique du compteur, dans lequel nous affichons un nombre et nous avons plusieurs boutons pour augmenter, diminuer ou réinitialiser ce nombre.

C'est un bon exemple d'application où nous devons stocker une information et rendre quelque chose de différent chaque fois que cette information change.

![5bueYQblr--2-](https://www.freecodecamp.org/news/content/images/2022/03/5bueYQblr--2-.gif align="left")

Le code de cette application ressemble à ceci :

```js
// App.js
import { useState } from 'react'

function App() {

  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <p>Le compteur est à : {count}</p>

      <div>
        <button onClick={() => setCount(count+1)}>Ajouter 1</button>
        <button onClick={() => setCount(count-1)}>Diminuer 1</button>

        <button onClick={() => setCount(count+10)}>Ajouter 10</button>
        <button onClick={() => setCount(count-10)}>Diminuer 10</button>

        <button onClick={() => setCount(0)}>Réinitialiser</button>
      </div>
    </div>
  )
}

export default App
```

* D'abord, nous importons le hook depuis React : `import { useState } from 'react'`
    
* Ensuite, nous initialisons l'état : `const [count, setCount] = useState(0)`
    

Ici, nous fournissons un nom de variable pour l'état (`count`) et un nom de fonction que nous utiliserons chaque fois que nous aurons besoin de mettre à jour cet état (`setCount`). Enfin, nous définissons la valeur initiale de l'état (`0`), qui sera la valeur chargée par défaut à chaque démarrage de l'application.

* Enfin, comme mentionné plus haut, chaque fois que nous voulons mettre à jour l'état, nous devons utiliser la fonction que nous avons déclarée : `setCount`. Pour l'utiliser, il suffit de l'appeler en lui passant le nouvel état souhaité en paramètre. C'est-à-dire que si nous voulons ajouter 1 à l'état précédent, nous appelons `setCount(count+1)`.
    

Comme mentionné également, cela provoquera une mise à jour de l'état et donc le re-rendu du composant. Ce qui, dans notre application, signifie que nous verrons le compteur augmenter à l'écran.

## Comment utiliser useEffect pour lire les mises à jour de l'état

Il est important de mentionner que la fonction setState est **asynchrone**. Donc, si nous essayons de lire l'état immédiatement après l'avoir mis à jour, comme ceci :

```js
<button onClick={() => {
          setCount(count+1)
          console.log(count)
}}>Ajouter 1</button>
```

nous obtiendrions la valeur précédente de l'état, sans la mise à jour.

La manière correcte de lire l'état après la mise à jour serait d'utiliser le hook **useEffect**. Il nous permet d'exécuter une fonction après chaque re-rendu du composant (par défaut) ou après le changement de n'importe quelle variable particulière que nous déclarons.

Quelque chose comme ça :

```js
useEffect(() => console.log(value), [value])
```

## Comment passer un callback à la fonction de mise à jour de l'état

De plus, le fait que useState soit asynchrone a des implications lorsqu'on envisage des changements d'état très fréquents et rapides.

Prenons, par exemple, le cas d'un utilisateur qui appuie sur le bouton AJOUTER plusieurs fois de suite, ou une boucle qui émet un événement de clic un certain nombre de fois.

En mettant à jour l'état comme `setCount(count+1)`, nous prenons le risque que `count` ne soit pas encore mis à jour lorsque l'événement suivant est déclenché.

Par exemple, disons qu'au début `count = 0`. Ensuite `setCount(count+1)` est appelé et l'état est mis à jour de manière asynchrone. Mais ensuite, à nouveau, `setCount(count+1)` est appelé, avant que la mise à jour de l'état ne soit terminée. Cela signifie que `count` est toujours égal à `0`, ce qui signifie que le deuxième `setCount` ne mettra pas à jour l'état correctement.

Une approche plus défensive consisterait à passer un callback à `setCount`, comme ceci : `setCount(prevCount => prevCount+1)`

Cela garantit que la valeur à mettre à jour est la plus récente et nous éloigne du problème mentionné ci-dessus. Chaque fois que nous effectuons des mises à jour basées sur un état précédent, nous devrions utiliser cette approche.

# Gérer l'échelle et la complexité

Jusqu'à présent, la gestion de l'état semble être un jeu d'enfant. Nous avons juste besoin d'un hook, d'une valeur et d'une fonction pour la mettre à jour, et nous sommes prêts.

Mais une fois que les applications commencent à devenir plus grandes et plus complexes, l'utilisation exclusive de cette méthode peut commencer à causer certains problèmes.

## Le contexte React

Le premier problème qui peut survenir est lorsque nous avons beaucoup de composants imbriqués et que nous avons besoin que de nombreux composants "frères" partagent le même état.

La réponse évidente ici est de faire remonter l'état ("lift state up"), ce qui signifie qu'un composant parent sera celui qui détiendra l'état et il le passera comme props aux composants enfants.

Cela fonctionne très bien, mais quand nous avons beaucoup de composants imbriqués, nous pouvons avoir besoin de passer des props à travers de nombreux niveaux de composants. C'est ce qu'on appelle le **"prop drilling"** et non seulement c'est inélégant, mais cela crée aussi un code difficile à maintenir.

Le prop drilling peut également provoquer des **re-rendus inutiles** qui peuvent affecter les performances de notre application. Si entre notre composant parent (qui stocke l'état) et nos composants enfants (qui consomment l'état) il y a d'autres composants ("composants intermédiaires"), nous devrons également passer les props à travers ces composants intermédiaires, même s'ils n'en ont pas besoin.

Cela signifie que ces "composants intermédiaires" seront re-rendus lorsque la prop change, même s'ils n'ont rien de différent à afficher.

Une solution à cela est d'utiliser le **contexte React** (React context), qui est en résumé un moyen de créer un composant wrapper qui enveloppe n'importe quel groupe de composants que nous voulons et peut passer des props directement à ces composants, sans avoir besoin de "forer" à travers des composants qui n'utiliseront pas nécessairement cet état.

La chose à surveiller lors de l'utilisation du contexte est que lorsque l'état du contexte change, tous les composants enveloppés qui reçoivent cet état seront re-rendus. Et cela pourrait ne pas être nécessaire selon le cas et pourrait également causer des problèmes de performance.

Il est donc toujours important de peser le pour et le contre : avons-nous vraiment besoin de rendre un état disponible pour de nombreux composants ou pouvons-nous simplement le garder local dans un seul composant ? Et si nous devons le rendre disponible pour de nombreux composants, est-ce vraiment une bonne idée de le mettre dans le contexte ou pouvons-nous simplement le faire remonter d'un niveau.

Kent C Dodds a écrit un [super article](https://kentcdodds.com/blog/application-state-management-with-react) sur ce sujet.

## Comment utiliser le Hook useReducer

Un autre problème peut survenir lors de l'utilisation de useState lorsque le nouvel état à définir dépend de l'état précédent (comme notre exemple de compteur) ou lorsque des changements d'état se produisent très fréquemment dans notre application.

Dans ces occasions, useState peut provoquer un comportement inattendu et imprévisible. C'est là que les **reducers** interviennent pour résoudre ce problème.

Un **reducer** est une fonction pure qui prend l'état précédent et une action comme argument, et retourne l'état suivant. On l'appelle un reducer parce que c'est le même type de fonction que vous pourriez passer à un tableau : `Array.prototype.reduce(reducer, initialValue)`.

**useReducer** est le hook fourni par React qui nous permet d'implémenter des reducers pour gérer notre état. En utilisant ce hook, notre exemple d'application précédent ressemblerait à ceci :

```js
// App.js
import { useReducer } from 'react'
import './App.scss'

function App() {

  function reducer(state, action) {
    switch (action.type) {
      case 'ADD': return { count: state.count + 1 }
      case 'SUB': return { count: state.count - 1 }
      case 'ADD10': return { count: state.count + 10 }
      case 'SUB10': return { count: state.count - 10 }
      case 'RESET': return { count: 0 }
      default: return state
    }
  }

  const [state, dispatch] = useReducer(reducer, { count: 0 })  

  return (
    <div className="App">
      <p>Le compteur est à : {state.count}</p>

      <div>
        <button onClick={() => dispatch({type: 'ADD'})}>Ajouter 1</button>
        
        <button onClick={() => dispatch({type: 'SUB'})}>Diminuer 1</button>

        <button onClick={() => dispatch({type: 'ADD10'})}>Ajouter 10</button>
        <button onClick={() => dispatch({type: 'SUB10'})}>Diminuer 10</button>

        <button onClick={() => dispatch({type: 'RESET'})}>Réinitialiser</button>
      </div>
    </div>
  )
}

export default App
```

* Encore une fois, nous commençons par importer le hook depuis React : `import { useReducer } from 'react'`
    
* Ensuite, nous déclarerons une fonction reducer, qui prendra comme paramètres l'état actuel et une action à effectuer sur celui-ci. À l'intérieur, elle aura une instruction switch qui lira le type d'action, exécutera l'action correspondante sur l'état et retournera l'état mis à jour.
    

> Il est courant d'utiliser des instructions switch dans les reducers et des majuscules pour déclarer les actions. ;)

```js
function reducer(state, action) {
    switch (action.type) {
      case 'ADD': return { count: state.count + 1 }
      case 'SUB': return { count: state.count - 1 }
      case 'ADD10': return { count: state.count + 10 }
      case 'SUB10': return { count: state.count - 10 }
      case 'RESET': return { count: 0 }
      default: return state
    }
  }
```

* Ensuite, il est temps de déclarer notre hook **useReducer**, qui ressemble assez au hook useState. Nous déclarons une **valeur pour notre état** ('state' dans notre cas), une **fonction que nous utiliserons pour le modifier** ('dispatch'), puis useReducer prendra la **fonction reducer** comme premier paramètre et l'**état par défaut** comme second paramètre.
    

```js
const [state, dispatch] = useReducer(reducer, { count: 0 })
```

* Enfin, pour mettre à jour notre état, nous n'appellerons pas le reducer directement, mais nous appellerons la fonction que nous venons de créer ('dispatch'), en lui passant le type d'action correspondant que nous voulons exécuter. En coulisses, la fonction dispatch se connectera au reducer et modifiera réellement l'état.
    

```js
<button onClick={() => dispatch({type: 'ADD'})}>Ajouter 1</button>
```

C'est un peu plus verbeux (boilerplate) que d'utiliser useState, mais useReducer n'est finalement pas si complexe.

Pour résumer, nous avons juste besoin de :

* Un reducer, qui est la fonction qui consolidera tous les changements d'état possibles.
    
* Une fonction dispatch, qui enverra les actions de modification au reducer.
    

L'idée ici est que les éléments de l'interface utilisateur ne pourront pas mettre à jour l'état directement comme ils le faisaient auparavant en appelant setState avec une valeur. Ils devront maintenant appeler un type d'action et passer par le reducer, ce qui rend la gestion de l'état plus modulaire et prévisible. ;)

## Et pour Redux ?

[Redux](https://redux.js.org/) est une bibliothèque qui existe depuis longtemps et qui est largement utilisée dans l'écosystème React.

Redux est un outil qui vient résoudre les deux problèmes mentionnés précédemment (prop drilling et comportement d'état imprévisible lors de changements d'état fréquents et complexes).

Il est important de mentionner que Redux est une bibliothèque agnostique, ce qui signifie qu'elle peut être implémentée sur n'importe quelle application front-end, pas seulement React.

L'ensemble d'outils de Redux est très similaire à ce que nous venons de voir avec useReducer, mais avec quelques éléments supplémentaires. Il y a trois blocs de construction principaux dans Redux :

* **Un store (magasin)** — un objet qui contient les données d'état de l'application.
    
* **Un reducer** — une fonction qui retourne des données d'état, déclenchée par un type d'action.
    
* **Une action** — un objet qui indique au reducer comment changer l'état. Il doit contenir une propriété type, et il peut contenir une propriété payload (charge utile) facultative.
    

En implémentant Redux, notre exemple d'application ressemblerait à ceci :

```js
// App.js
import './App.scss'

import { Provider, useSelector, useDispatch } from 'react-redux'
import { addOne, subOne, addSome, subSome, reset } from './store/actions/count.actions'

import store from './store'

function App() {

  const dispatch = useDispatch()
  const count = useSelector(state => state.count)

  return (
    <Provider store={store}>
      <div className="App">
        <p>Le compteur est à : {count}</p>

        <div>
          <button onClick={() => dispatch(addOne())}>Ajouter 1</button>
          
          <button onClick={() => dispatch(subOne())}>Diminuer 1</button>

          <button onClick={() => dispatch(addSome(10))}>Ajouter 10</button>
          <button onClick={() => dispatch(subSome(10))}>Diminuer 10</button>

          <button onClick={() => dispatch(reset())}>Réinitialiser</button>
        </div>
      </div>
    </Provider>
  )
}

export default App
```

En outre, nous aurions maintenant besoin d'un nouveau répertoire **store**, avec ses fichiers store, reducer et actions correspondants.

![Cbdp2DJY9](https://www.freecodecamp.org/news/content/images/2022/03/Cbdp2DJY9.png align="left")

```js
// index.js (STORE)
import { createStore } from 'redux'
import CountReducer from './reducers/count.reducer'

export default createStore(CountReducer)
```

```js
// count.reducer.js
import { ADD, SUB, ADDSOME, SUBSOME, RESET } from '../actions/count.actions'

const CountReducer = (state = { count: 0 }, action) => {
    switch (action.type) {
      case ADD: return { count: state.count + 1 }
      case SUB: return { count: state.count - 1 }
      case ADDSOME: return { count: state.count + action.payload }
      case SUBSOME: return { count: state.count - action.payload }
      case RESET: return { count: 0 }
      default: return state
    }
}

export default CountReducer
```

```js
// count.actions.js
export const ADD = 'ADD'
export const addOne = () => ({ type: ADD })

export const SUB = 'SUB'
export const subOne = () => ({ type: SUB })

export const ADDSOME = 'ADDSOME'
export const addSome = (value) => ({
    type: ADDSOME,
    payload: value
})

export const SUBSOME = 'SUBSOME'
export const subSome = (value) => ({
    type: SUBSOME,
    payload: value
})

export const RESET = 'RESET'
export const reset = () => ({ type: RESET })
```

C'est beaucoup plus de boilerplate que ce que nous avons vu auparavant (c'est ce pour quoi Redux est principalement critiqué), alors décomposons-le :

* Comme je l'ai mentionné, Redux est une bibliothèque externe, donc avant toute chose, nous devons l'installer en exécutant `npm i redux react-redux`. `redux` apportera les fonctions de base dont nous avons besoin pour gérer notre état et `react-redux` installera des hooks sympas pour lire et modifier facilement l'état depuis nos composants.
    
* Maintenant, la première chose est le **store**. Dans Redux, le store est l'entité qui possède toutes les informations d'état de l'application. Grâce à Redux, nous pourrons accéder au store depuis n'importe quel composant (tout comme avec le contexte).
    

Pour créer un store, nous importons la fonction `createStore` et lui passons un reducer en entrée.

Sachez que vous pouvez également combiner différents reducers et les passer au même store au cas où vous souhaiteriez séparer les préoccupations dans différents reducers.

```js
import { createStore } from 'redux'
import CountReducer from './reducers/count.reducer'

export default createStore(CountReducer)
```

* Ensuite, il y a le **reducer**, qui fonctionne exactement de la même manière que celui que nous avons vu avec useReducer. Il prend l'état par défaut et une action en paramètres, puis à l'intérieur il a une instruction switch pour lire le type d'action, exécuter la modification d'état correspondante et retourner l'état mis à jour.
    

```js
import { ADD, SUB, ADDSOME, SUBSOME, RESET } from '../actions/count.actions'

const CountReducer = (state = { count: 0 }, action) => {
    switch (action.type) {
      case ADD: return { count: state.count + 1 }
      case SUB: return { count: state.count - 1 }
      case ADDSOME: return { count: state.count + action.payload }
      case SUBSOME: return { count: state.count - action.payload }
      case RESET: return { count: 0 }
      default: return state
    }
}

export default CountReducer
```

* Viennent ensuite les **actions**. Les actions sont ce que nous allons utiliser pour dire au reducer comment mettre à jour l'état. Dans le code, vous pouvez voir que pour chaque action, nous déclarons des constantes pour les utiliser au lieu de simples chaînes de caractères (c'est une bonne pratique pour améliorer la maintenabilité), et des fonctions qui retournent soit juste un type, soit un type et un payload. Ces fonctions sont ce que nous allons dispatcher depuis notre composant afin de changer l'état. ;)
    

Notez que j'ai un peu modifié l'exemple afin de montrer ce que signifie payload lorsqu'on parle d'actions. Au cas où nous voudrions **passer un paramètre depuis le composant** lorsque nous dispatchons une action, **payload est l'endroit où cette information se trouvera**.

Dans l'exemple, vous pouvez voir que nous pouvons maintenant passer directement depuis le composant le nombre que nous voulons ajouter/soustraire lorsque nous appelons ADDSOME/SUBSOME.

```js
export const ADD = 'ADD'
export const addOne = () => ({ type: ADD })

export const SUB = 'SUB'
export const subOne = () => ({ type: SUB })

export const ADDSOME = 'ADDSOME'
export const addSome = value => ({
    type: ADDSOME,
    payload: value
})

export const SUBSOME = 'SUBSOME'
export const subSome = value => ({
    type: SUBSOME,
    payload: value
})

export const RESET = 'RESET'
export const reset = () => ({ type: RESET })
```

* Et enfin vient notre composant. Ici, nous avons 3 choses à noter :
    

1. D'abord, nous avons un composant **Provider** qui reçoit le **store** en props. C'est ce qui permet l'accès à notre store depuis tous les composants qu'il enveloppe.
    
2. Ensuite, nous avons un hook appelé **useDispatch()** (que nous utiliserons pour dispatcher des actions) et un autre appelé **useSelector()** (que nous utiliserons pour lire l'état depuis le store).
    
3. Enfin, remarquez que nous **dispatchons les fonctions** que nous avons déclarées dans le fichier des actions, et que nous passons une valeur en entrée lorsque cela correspond. Cette valeur est ce que l'action prend comme payload et ce que le reducer va utiliser pour modifier l'état. ;)
    

```js
import './App.scss'

import { useSelector, useDispatch } from 'react-redux'
import { addOne, subOne, addSome, subSome, reset } from './store/actions/count.actions'

function App() {

  const dispatch = useDispatch()
  const count = useSelector(state => state.count)

  return (
      <div className="App">
        <p>Le compteur est à : {count}</p>

        <div>
          <button onClick={() => dispatch(addOne())}>Ajouter 1</button>
          
          <button onClick={() => dispatch(subOne())}>Diminuer 1</button>

          <button onClick={() => dispatch(addSome(10))}>Ajouter 10</button>
          <button onClick={() => dispatch(subSome(10))}>Diminuer 10</button>

          <button onClick={() => dispatch(reset())}>Réinitialiser</button>
        </div>
      </div>
  )
}

export default App
```

Redux est un bel outil qui résout deux problèmes en même temps (prop drilling et changements d'état complexes). Cependant, il génère beaucoup de boilerplate et fait de la gestion d'état un sujet plus difficile à appréhender, surtout lorsqu'on traite avec différents fichiers et entités comme les actions, les reducers, un store...

Une chose importante à mentionner ici est que ces outils ou manières de gérer l'état ne s'excluent pas mutuellement, ils peuvent et devraient probablement être utilisés en même temps, chacun pour résoudre le problème spécifique pour lequel ils sont doués.

Dans le cas de Redux, ce problème est la gestion de l'**état global** (c'est-à-dire l'état qui affecte toute votre application ou une très grande partie de celle-ci). Il n'y aurait aucun sens à utiliser Redux pour gérer un compteur comme dans notre exemple ou l'ouverture et la fermeture d'une modale.

Une bonne règle d'or est : **useState pour l'état du composant, Redux pour l'état de l'application**.

# Alternatives à Redux

Si ce sujet n'est pas encore assez compliqué pour vous, ces dernières années, de nombreuses nouvelles bibliothèques sont apparues comme alternatives à Redux, chacune avec sa propre approche de la gestion de l'état.

Juste pour avoir une bonne vue d'ensemble, découvrons-les rapidement.

## Redux Toolkit

[Redux Toolkit](https://redux-toolkit.js.org/) est une bibliothèque construite par-dessus Redux, qui vise à supprimer une partie de la complexité et du boilerplate que Redux génère.

Redux Toolkit repose sur deux choses :

* Un **store**, qui fonctionne exactement de la même manière qu'un store Redux classique.
    
* Et des **slices** (tranches) qui condensent les actions et les reducers Redux classiques en une seule chose.
    

En implémentant Redux Toolkit, notre exemple d'application ressemblerait à ceci :

```js
// App.js
import './App.scss'

import { useSelector, useDispatch } from 'react-redux'
import { addOne, subOne, addSome, subSome, reset } from './store/slices/count.slice'

function App() {

  const dispatch = useDispatch()
  const count = useSelector(state => state.counter.count)

  return (
      <div className="App">
        <p>Le compteur est à : {count}</p>

        <div>
          <button onClick={() => dispatch(addOne())}>Ajouter 1</button>
          
          <button onClick={() => dispatch(subOne())}>Diminuer 1</button>

          <button onClick={() => dispatch(addSome(10))}>Ajouter 10</button>
          <button onClick={() => dispatch(subSome(10))}>Diminuer 10</button>

          <button onClick={() => dispatch(reset())}>Réinitialiser</button>
        </div>
      </div>
  )
}

export default App
```

```js
// index.js
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import { Provider } from 'react-redux'
import store from './store/index'

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <App />
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
)
```

```js
// Index.jsx (STORE)
import { configureStore } from '@reduxjs/toolkit'
import counterReducer from './slices/count.slice'

export const store = configureStore({
  reducer: {
      counter: counterReducer
  },
})

export default store
```

```js
// count.slice.jsx
import { createSlice } from '@reduxjs/toolkit'

const initialState = { count: 0 }

export const counterSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    addOne: state => {state.count += 1},
    subOne: state => {state.count -= 1},
    addSome: (state, action) => {state.count += action.payload},
    subSome: (state, action) => {state.count -= action.payload},
    reset: state => {state.count = 0}
  },
})

export const { addOne, subOne, addSome, subSome, reset } = counterSlice.actions

export default counterSlice.reducer
```

* D'abord, nous devons **l'installer** en exécutant `npm install @reduxjs/toolkit react-redux`
    
* Dans notre **store**, nous importons la fonction `configureStore` de Redux Toolkit, et créons le store en appelant cette fonction et en lui passant un objet avec un reducer, qui est lui-même un objet contenant une slice.
    

```js
export const store = configureStore({
  reducer: {
      counter: counterReducer
  },
})
```

* Une **slice**, comme je l'ai mentionné, est un moyen de condenser les actions et les reducers en une même chose. Nous importons la fonction `createSlice` de Redux Toolkit, puis nous déclarons l'état initial et initialisons la slice.
    

Celle-ci recevra comme paramètres le nom de la slice, l'état initial et les fonctions que nous dispatcherons depuis nos composants afin de modifier l'état.

Remarquez qu'il n'y a pas d'actions ici. L'interface utilisateur appellera directement les fonctions du reducer. C'est la complexité que Redux Toolkit "supprime".

```js
export const counterSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    addOne: state => {state.count += 1},
    subOne: state => {state.count -= 1},
    addSome: (state, action) => {state.count += action.payload},
    subSome: (state, action) => {state.count -= action.payload},
    reset: state => {state.count = 0}
  },
})
```

* Dans index.js, nous enveloppons notre application autour d'un composant provider afin de pouvoir accéder à l'état de n'importe où.
    

```js
    <Provider store={store}>
      <App />
    </Provider>
```

* Et enfin, depuis notre composant, nous lisons l'état et dispatcherons les fonctions de modification à l'aide de hooks, tout comme avec Redux classique.
    

```js
function App() {

  const dispatch = useDispatch()
  const count = useSelector(state => state.counter.count)

  return (
      <div className="App">
        <p>Le compteur est à : {count}</p>

        <div>
          <button onClick={() => dispatch(addOne())}>Ajouter 1</button>
          
          <button onClick={() => dispatch(subOne())}>Diminuer 1</button>

          <button onClick={() => dispatch(addSome(10))}>Ajouter 10</button>
          <button onClick={() => dispatch(subSome(10))}>Diminuer 10</button>

          <button onClick={() => dispatch(reset())}>Réinitialiser</button>
        </div>
      </div>
  )
}
```

Redux Toolkit vise à être un moyen plus simple de gérer Redux, mais à mon avis, c'est encore presque le même boilerplate et il n'y a pas une grande différence avec Redux classique.

### Une mention pour Redux Thunk et Redux Saga

[Redux Thunk](https://github.com/reduxjs/redux-thunk) et [Redux Saga](https://redux-saga.js.org/) sont deux autres bibliothèques de middleware populaires qui sont utilisées **conjointement** avec Redux.

Plus précisément, Thunk et Saga sont tous deux destinés à être utilisés lors du traitement des effets secondaires ou des tâches asynchrones.

## Recoil

![2CYCmD92D](https://www.freecodecamp.org/news/content/images/2022/03/2CYCmD92D.png align="left")

[Recoil](https://recoiljs.org/) est une bibliothèque de gestion d'état open source spécifiquement pour React, créée par Facebook (ou Meta, peu importe...). Selon leur site web, Recoil est conçu pour être "minimal et Reactish", dans le sens où il ressemble et se ressent comme du code React classique.

Recoil est basé sur l'idée d'**atomes** (atoms). Pour citer leur documentation,

> "Un atome représente un morceau d'état. Les atomes peuvent être lus et écrits depuis n'importe quel composant. Les composants qui lisent la valeur d'un atome sont implicitement abonnés à cet atome, de sorte que toute mise à jour de l'atome entraînera un re-rendu de tous les composants abonnés à cet atome".

En utilisant Recoil, notre exemple d'application ressemblerait à ceci :

```js
// App.js
import countState from './recoil/counter.atom'
import './App.scss'

import { useRecoilState } from 'recoil'

function App() {

  const [count, setCount] = useRecoilState(countState)

  return (
      <div className="App">
        <p>Le compteur est à : {count}</p>

        <div>
          <button onClick={() => setCount(count+1)}>Ajouter 1</button>
          
          <button onClick={() => setCount(count-1)}>Diminuer 1</button>

          <button onClick={() => setCount(count+10)}>Ajouter 10</button>
          <button onClick={() => setCount(count-10)}>Diminuer 10</button>

          <button onClick={() => setCount(0)}>Réinitialiser</button>
        </div>
      </div>
  )
}

export default App
```

```js
// index.js
import React from 'react'
import ReactDOM from 'react-dom'
import App from './App'
import { RecoilRoot } from 'recoil'

ReactDOM.render(
  <React.StrictMode>
    <RecoilRoot>
      <App />
    </RecoilRoot>
  </React.StrictMode>,
  document.getElementById('root')
)
```

```js
// counter.atom.jsx
import { atom } from 'recoil'

const countState = atom({
  key: 'countState', // ID unique (par rapport aux autres atomes/sélecteurs)
  default: 0 // valeur par défaut (alias valeur initiale)
})

export default countState
```

Comme vous pouvez probablement le voir immédiatement, c'est beaucoup moins de boilerplate que Redux. =D

* D'abord, nous l'installons en exécutant `npm install recoil`
    
* Les composants qui utilisent l'état Recoil ont besoin que `RecoilRoot` apparaisse quelque part dans l'arborescence parente. Nous enveloppons donc notre application avec.
    

```js
  <React.StrictMode>
    <RecoilRoot>
      <App />
    </RecoilRoot>
  </React.StrictMode>
```

* Ensuite, nous déclarons notre **atome**, qui est juste un objet contenant une clé et une valeur par défaut :
    

```plaintext
const countState = atom({
  key: 'countState', // ID unique (par rapport aux autres atomes/sélecteurs)
  default: 0 // valeur par défaut (alias valeur initiale)
})
```

* Enfin, dans notre composant, nous importons le hook `useRecoilState` et déclarons notre état avec celui-ci, en lui passant la clé unique que nous venons de déclarer dans notre atome.
    

```plaintext
const [count, setCount] = useRecoilState(countState)
```

Comme vous pouvez le voir, cela ressemble énormément à un hook useState ordinaire. *Reactish*... =P

Et depuis notre interface utilisateur, nous appelons simplement la fonction `setCount` pour mettre à jour notre état.

```js
<button onClick={() => setCount(count+1)}>Ajouter 1</button>
```

Minimal et très facile à utiliser. Recoil est encore un peu expérimental et pas si largement utilisé, mais vous pouvez voir pourquoi les développeurs du monde entier se tourneraient vers cet outil.

## Jotai

[Jotai](https://jotai.org/) est une bibliothèque de gestion d'état open source conçue pour React qui s'inspire de Recoil. Elle diffère de Recoil en recherchant une API encore plus minimaliste – elle n'utilise pas de clés sous forme de chaînes de caractères et est orientée TypeScript.

Tout comme Recoil, Jotai utilise des atomes. Un **atome** représente un morceau d'état. Tout ce dont vous avez besoin est de spécifier une valeur initiale, qui peut être des valeurs primitives comme des chaînes de caractères et des nombres, des objets et des tableaux. Ensuite, dans vos composants, vous consommez cet atome, et à chaque changement d'atome, ce composant se re-rendra.

En utilisant Jotai, notre exemple d'application ressemble à ceci :

```js
// App.js
import './App.scss'

import { useAtom } from 'jotai'

function App() {

  const [count, setCount] = useAtom(countAtom)

  return (
      <div className="App">
        <p>Le compteur est à : {count}</p>

        <div>
          <button onClick={() => setCount(count+1)}>Ajouter 1</button>
          
          <button onClick={() => setCount(count-1)}>Diminuer 1</button>

          <button onClick={() => setCount(count+10)}>Ajouter 10</button>
          <button onClick={() => setCount(count-10)}>Diminuer 10</button>

          <button onClick={() => setCount(0)}>Réinitialiser</button>
        </div>
      </div>
  )
}

export default App
```

```js
// counter.atom.jsx
import { atom } from 'jotai'

const countAtom = atom(0)

export default countAtom
```

Comme vous pouvez le voir, c'est encore plus minimal que Recoil.

* Nous l'installons en exécutant `npm install jotai`
    
* Ensuite, nous déclarons un atome avec une valeur par défaut :
    

```js
const countAtom = atom(0)
```

* Et nous le consommons avec notre composant en utilisant `useAtom` :
    

```js
const [count, setCount] = useAtom(countAtom)
```

Vraiment sympa et simple !

## Zustand

[Zustand](https://github.com/pmndrs/zustand) est une autre bibliothèque de gestion d'état open source conçue pour React. Elle est inspirée de Flux, une bibliothèque largement utilisée avant l'arrivée de Redux, et elle vise à être

> "une solution de gestion d'état barebones, petite, rapide, non-opinionée et évolutive, avec une API confortable basée sur les hooks et presque aucun boilerplate".

Zustand utilise un store d'une manière similaire à Redux, mais avec la différence que dans Zustand, le store est maintenant un hook, et il nécessite beaucoup moins de boilerplate.

En utilisant Zustand, notre exemple d'application ressemblerait à ceci :

```js
// App.js
import './App.scss'
import useStore from './store'

function App() {

  const count = useStore(state => state.count)
  const { addOne, subOne, add10, sub10, reset } = useStore(state => state)

  return (
      <div className="App">
        <p>Le compteur est à : {count}</p>

        <div>
            <button onClick={() => addOne()}>Ajouter 1</button>
          
          <button onClick={() => subOne()}>Diminuer 1</button>

          <button onClick={() => add10()}>Ajouter 10</button>
          <button onClick={() => sub10()}>Diminuer 10</button>

          <button onClick={() => reset()}>Réinitialiser</button>
        </div>
      </div>
  )
}

export default App
```

```js
// Index.jsx (STORE)
import create from 'zustand'

const useStore = create(set => ({
  count: 0,
  addOne: () => set(state => ({count: state.count += 1})),
  subOne: () => set(state => ({count: state.count -= 1})),
  add10: () => set(state => ({count: state.count += 10})),
  sub10: () => set(state => ({count: state.count -= 10})),
  reset: () => set({count: 0})
}))

export default useStore
```

* Nous l'installons en exécutant `npm install zustand`
    
* Nous créons un store avec la fonction `create` que nous avons importée de Zustand. À l'intérieur, nous définissons l'état par défaut et les fonctions que nous utiliserons pour modifier l'état.
    

```js
const useStore = create(set => ({
  count: 0,
  addOne: () => set(state => ({count: state.count += 1})),
  subOne: () => set(state => ({count: state.count -= 1})),
  add10: () => set(state => ({count: state.count += 10})),
  sub10: () => set(state => ({count: state.count -= 10})),
  reset: () => set({count: 0})
}))
```

* Ensuite, dans notre composant, nous importons le store que nous venons de créer, et nous y lisons l'état et les fonctions de modification de la manière suivante :
    

```js
  const count = useStore(state => state.count)
  const { addOne, subOne, add10, sub10, reset } = useStore(state => state)
```

Notre interface utilisateur peut appeler les fonctions de modification comme ceci :

```js
<button onClick={() => addOne()}>Ajouter 1</button>
```

Vous pouvez voir comment Zustand reprend les mêmes concepts que Redux, avec une approche beaucoup plus propre et simple.

# Conclusion

La gestion de l'état est l'un des sujets les plus complexes lorsqu'il s'agit de développement front-end. Et vous pouvez voir combien de personnes ont essayé de la faire fonctionner de manière prévisible et évolutive, mais aussi de manières propres et faciles à utiliser.

Surtout ces dernières années, de nombreux bons outils sont apparus offrant des moyens agréables de traiter la gestion de l'état.

En tant que développeurs, cependant, nous devons garder à l'esprit que Redux et d'autres bibliothèques ont été créées pour résoudre des problèmes de gestion d'état spécifiques, en particulier dans les applications très grandes, complexes et massivement utilisées.

Je pense que si vous ne rencontrez pas ces problèmes, il n'est vraiment pas nécessaire d'ajouter du boilerplate supplémentaire et de compliquer votre code. Même avec des bibliothèques modernes qui n'ajoutent presque aucun boilerplate.

React lui-même est une bibliothèque très robuste et solide, et des outils comme useState, useReducer et useContext sont tout à fait suffisants pour résoudre la plupart des problèmes. Je m'en tiendrais donc aux bases, à moins que, pour une raison quelconque, les bases ne suffisent plus.

Lorsqu'on a besoin d'une bibliothèque de gestion d'état plus spécifique et robuste, je pense que le choix est une question de décision entre fiabilité et simplicité.

Redux est la bibliothèque la plus mature et la plus utilisée, et cela s'accompagne de beaucoup de documentation, de communautés en ligne et de bugs précédemment trouvés et résolus à chaque nouvelle version.

Le mauvais côté, pour nous développeurs, c'est qu'elle nous présente de nouveaux concepts que nous devons apprendre et auxquels nous devons réfléchir. Nous devons également ajouter pas mal de code juste pour la faire fonctionner, et elle peut ajouter plus de complexité que les problèmes qu'elle aide à résoudre.

Au contraire, les bibliothèques modernes comme celles que nous avons vues sont beaucoup plus simples et vont droit au but, mais elles ne sont pas aussi largement utilisées et testées, et sont encore un peu expérimentales.

Mais d'après ce que nous pouvons voir pour le moment, il semble que ce ne soit qu'une question de temps avant que l'une ou certaines d'entre elles ne prennent les devants et deviennent l'outil le plus largement utilisé.

C'est tout ! J'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [linkedin](https://www.linkedin.com/in/germancocca/) ou [twitter](https://twitter.com/CoccaGerman). Salut et à la prochaine !