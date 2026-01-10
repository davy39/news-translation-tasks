---
title: Comment commencer à tester vos applications React en utilisant React Testing
  Library et Jest
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-12T17:39:01.000Z'
originalURL: https://freecodecamp.org/news/8-simple-steps-to-start-testing-react-apps-using-react-testing-library-and-jest
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/cover-3.png
tags:
- name: React
  slug: react
- name: Testing
  slug: testing
seo_title: Comment commencer à tester vos applications React en utilisant React Testing
  Library et Jest
seo_desc: 'By Ibrahima Ndaw

  Testing is often seen as a tedious process. It''s extra code you have to write,
  and in some cases, to be honest, it''s not needed. But every developer should know
  at least the basics of testing. It increases confidence in the products ...'
---

Par Ibrahima Ndaw

Les tests sont souvent perçus comme un processus fastidieux. C'est du code supplémentaire que vous devez écrire, et dans certains cas, soyons honnêtes, ce n'est pas nécessaire. Mais chaque développeur devrait connaître au moins les bases des tests. Cela augmente la confiance dans les produits qu'ils construisent, et pour la plupart des entreprises, c'est une exigence.

Dans le monde React, il existe une bibliothèque incroyable appelée `react-testing-library` qui vous aide à tester vos applications React plus efficacement. Vous l'utilisez avec Jest.

Dans cet article, nous verrons les 8 étapes simples que vous pouvez suivre pour commencer à tester vos applications React comme un pro.

* [Prérequis](#heading-prerequisites)
* [Bases](#heading-basics)
* [Qu'est-ce que React Testing Library ?](#what-is-react-testing-library)
* [1. Comment créer un instantané de test ?](#heading-1-how-to-create-a-test-snapshot)
* [2. Tester les éléments DOM](#heading-2-testing-dom-elements)
* [3. Tester les événements](#heading-3-testing-events)
* [4. Tester les actions asynchrones](#heading-4-testing-asynchronous-actions)
* [5. Tester React Redux](#heading-5-testing-react-redux)
* [6. Tester React Context](#heading-6-testing-react-context)
* [7. Tester React Router](#heading-7-testing-react-router)
* [8. Tester les requêtes HTTP](#heading-8-testing-http-request)
* [Réflexions finales](#heading-final-thoughts)
* [Prochaines étapes](#heading-next-steps)

## Prérequis

Ce tutoriel suppose que vous avez au moins une compréhension de base de React. Je me concentrerai uniquement sur la partie testing.

Et pour suivre, vous devez cloner le projet en exécutant dans votre terminal :

```shell
  git clone https://github.com/ibrahima92/prep-react-testing-library-guide

```

Ensuite, exécutez :

```shell
  yarn

```

Ou, si vous utilisez NPM :

```shell
npm install

```

Et c'est tout ! Maintenant, plongeons dans quelques bases.

## Bases

Certaines choses clés seront beaucoup utilisées dans cet article, et comprendre leur rôle peut vous aider dans votre compréhension.

`it ou test` : décrit le test lui-même. Il prend comme paramètres le nom du test et une fonction qui contient les tests.

`expect` : la condition que le test doit passer. Il comparera le paramètre reçu à un matcher.

`un matcher` : une fonction qui est appliquée à la condition attendue.

`render` : la méthode utilisée pour rendre un composant donné.

```jsx
import React from 'react'
import {render} from '@testing-library/react'
import App from './App'
 
 it('should take a snapshot', () => {
    const { asFragment } = render(<App />)
    
    expect(asFragment(<App />)).toMatchSnapshot()
   })
});

```

Comme vous pouvez le voir, nous décrivons le test avec `it`, puis nous utilisons `render` pour afficher le composant App et nous attendons que `asFragment(<App />)` corresponde à `toMatchSnapshot()` (le matcher fourni par [jest-dom](https://github.com/testing-library/jest-dom)). 

Au fait, la méthode `render` retourne plusieurs méthodes que nous pouvons utiliser pour tester nos fonctionnalités. Nous avons également utilisé la déstructuration pour obtenir la méthode.

Cela étant dit, passons à la section suivante et apprenons-en plus sur la React Testing Library.

## Qu'est-ce que la React Testing Library ?

La React Testing Library est un package très léger créé par [Kent C. Dodds](https://twitter.com/kentcdodds). C'est un remplacement pour [Enzyme](https://enzymejs.github.io/enzyme/) et fournit des fonctions utilitaires légères au-dessus de `react-dom` et `react-dom/test-utils`. 

La React Testing Library est une bibliothèque de test DOM, ce qui signifie qu'au lieu de traiter avec des instances de composants React rendus, elle gère les éléments DOM et leur comportement face à de vrais utilisateurs. 

C'est une excellente bibliothèque, elle est (relativement) facile à utiliser, et elle encourage de bonnes pratiques de test. Notez que vous pouvez également l'utiliser sans Jest.

"Plus vos tests ressemblent à la manière dont votre logiciel est utilisé, plus ils peuvent vous donner confiance."

Alors, commençons à l'utiliser dans la section suivante. Au fait, vous n'avez pas besoin d'installer de packages, puisque `create-react-app` vient avec la bibliothèque et ses dépendances.

## 1. Comment créer un instantané de test

Un instantané, comme le suggère le nom, nous permet de sauvegarder l'instantané d'un composant donné. Cela aide beaucoup lorsque vous mettez à jour ou faites du refactoring, et que vous voulez obtenir ou comparer les changements.

Maintenant, prenons un instantané du fichier `App.js`.

* `App.test.js`

```jsx
import React from 'react'
import {render, cleanup} from '@testing-library/react'
import App from './App'

 afterEach(cleanup)
 
 it('should take a snapshot', () => {
    const { asFragment } = render(<App />)
    
    expect(asFragment(<App />)).toMatchSnapshot()
   })
});

```

Pour prendre un instantané, nous devons d'abord importer `render` et `cleanup`. Ces deux méthodes seront beaucoup utilisées tout au long de cet article. 

`render`, comme vous pouvez le deviner, aide à rendre un composant React. Et `cleanup` est passé comme paramètre à `afterEach` pour simplement tout nettoyer après chaque test afin d'éviter les fuites de mémoire.

Ensuite, nous pouvons rendre le composant App avec `render` et obtenir `asFragment` comme valeur retournée par la méthode. Et enfin, assurez-vous que le fragment du composant App correspond à l'instantané.

Maintenant, pour exécuter le test, ouvrez votre terminal et naviguez à la racine du projet et exécutez la commande suivante :

```shell
  yarn test

```

Ou, si vous utilisez npm :

```shell
  npm test

```

En résultat, il créera un nouveau dossier `__snapshots__` et un fichier `App.test.js.snap` dans `src` qui ressemblera à ceci :

* `App.test.js.snap`

```jsx
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`Take a snapshot should take a snapshot 1`] = `
<DocumentFragment>
  <div class="App">
    <h1>Testing</h1>
  </div>
</DocumentFragment>
`;

```

Et si vous faites un autre changement dans `App.js`, le test échouera, car l'instantané ne correspondra plus à la condition. Pour le faire passer, appuyez simplement sur `u` pour le mettre à jour. Et vous aurez l'instantané mis à jour dans `App.test.js.snap`.

Maintenant, passons à la suite et commençons à tester nos éléments.

## 2. Tester les éléments DOM

Pour tester nos éléments DOM, nous devons d'abord regarder le fichier `TestElements.js`.

* `TestElements.js`

```jsx
import React from 'react'

const TestElements = () => {
 const [counter, setCounter] = React.useState(0)
  
 return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={() => setCounter(counter + 1)}> Up</button>
    <button disabled data-testid="button-down" onClick={() => setCounter(counter - 1)}>Down</button>
 </>
    )
  }
  
export default TestElements

```

Ici, la seule chose que vous devez retenir est `data-testid`. Il sera utilisé pour sélectionner ces éléments à partir du fichier de test. Maintenant, écrivons le test unitaire :

Test si le compteur est égal à 0 :

`TestElements.test.js`

```jsx
import React from 'react';
import { render, cleanup } from '@testing-library/react';
import TestElements from './TestElements'

afterEach(cleanup);

  it('should equal to 0', () => {
    const { getByTestId } = render(<TestElements />); 
    expect(getByTestId('counter')).toHaveTextContent(0)
   });

```

Comme vous pouvez le voir, la syntaxe est assez similaire au test précédent. La seule différence est que nous utilisons `getByTestId` pour sélectionner les éléments nécessaires (rappelons `data-testid`) et vérifier si le test est passé. En d'autres termes, nous vérifions si le contenu textuel `<h1 data-testid="counter">{ counter }</h1>` est égal à 0.

Test si les boutons sont activés ou désactivés :

`TestElements.test.js` (ajoutez le bloc de code suivant au fichier)

```jsx
   it('should be enabled', () => {
    const { getByTestId } = render(<TestElements />);
    expect(getByTestId('button-up')).not.toHaveAttribute('disabled')
  });

  it('should be disabled', () => {
    const { getByTestId } = render(<TestElements />); 
    expect(getByTestId('button-down')).toBeDisabled()
  });

```

Ici, comme d'habitude, nous utilisons `getByTestId` pour sélectionner les éléments et vérifier pour le premier test si le bouton a un attribut `disabled`. Et pour le second, si le bouton est désactivé ou non.

Et si vous enregistrez le fichier ou relancez dans votre terminal `yarn test`, le test passera.

_Félicitations ! Votre premier test a réussi !_

![congrats](https://media.giphy.com/media/3o6fJ1BM7R2EBRDnxK/source.gif)

Maintenant, apprenons comment tester un événement dans la section suivante.

## 3. Tester les événements

Avant d'écrire nos tests unitaires, vérifions d'abord à quoi ressemble `TestEvents.js`.

* `TestEvents.js`

```jsx
import React from 'react'

const TestEvents = () => {
  const [counter, setCounter] = React.useState(0)
  
return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={() => setCounter(counter + 1)}> Up</button>
    <button data-testid="button-down" onClick={() => setCounter(counter - 1)}>Down</button>
 </>
    )
  }
  
  export default TestEvents

```

Maintenant, écrivons les tests.

Test si le compteur s'incrémente et se décrémente correctement lorsque nous cliquons sur les boutons :

`TestEvents.test.js`

```jsx
import React from 'react';
import { render, cleanup, fireEvent } from '@testing-library/react';
import TestEvents from './TestEvents'

  afterEach(cleanup);
  
  it('increments counter', () => {
    const { getByTestId } = render(<TestEvents />); 
    
    fireEvent.click(getByTestId('button-up'))

    expect(getByTestId('counter')).toHaveTextContent('1')
  });

  it('decrements counter', () => {
    const { getByTestId } = render(<TestEvents />); 
    
    fireEvent.click(getByTestId('button-down'))

    expect(getByTestId('counter')).toHaveTextContent('-1')
  });


```

Comme vous pouvez le voir, ces deux tests sont très similaires sauf pour le contenu textuel attendu.

Le premier test déclenche un événement de clic avec `fireEvent.click()` pour vérifier si le compteur s'incrémente à 1 lorsque le bouton est cliqué.

Et le second vérifie si le compteur se décrémente à -1 lorsque le bouton est cliqué.

`fireEvent` a plusieurs méthodes que vous pouvez utiliser pour tester les événements, alors n'hésitez pas à plonger dans la documentation pour en apprendre plus.

Maintenant que nous savons comment tester les événements, passons à la section suivante et apprenons comment gérer les actions asynchrones.

## 4. Tester les actions asynchrones

Une action asynchrone est quelque chose qui peut prendre du temps à se compléter. Cela peut être une requête HTTP, un minuteur, etc.

Maintenant, vérifions le fichier `TestAsync.js`.

* `TestAsync.js`

```jsx
import React from 'react'

const TestAsync = () => {
  const [counter, setCounter] = React.useState(0)

  const delayCount = () => (
    setTimeout(() => {
      setCounter(counter + 1)
    }, 500)
  )
  
return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={delayCount}> Up</button>
    <button data-testid="button-down" onClick={() => setCounter(counter - 1)}>Down</button>
 </>
    )
  }
  
  export default TestAsync

```

Ici, nous utilisons `setTimeout()` pour retarder l'événement d'incrémentation de 0,5s.

Test si le compteur est incrémenté après 0,5s :

`TestAsync.test.js`

```jsx
import React from 'react';
import { render, cleanup, fireEvent, waitForElement } from '@testing-library/react';
import TestAsync from './TestAsync'

afterEach(cleanup);
  
  it('increments counter after 0.5s', async () => {
    const { getByTestId, getByText } = render(<TestAsync />); 

    fireEvent.click(getByTestId('button-up'))

    const counter = await waitForElement(() => getByText('1')) 

    expect(counter).toHaveTextContent('1')
  });

```

Pour tester l'événement d'incrémentation, nous devons d'abord utiliser async/await pour gérer l'action car, comme je l'ai dit plus tôt, cela prend du temps à se compléter.

Ensuite, nous utilisons une nouvelle méthode d'assistance `getByText()`. Cela est similaire à `getByTestId()`, sauf que `getByText()` sélectionne le contenu textuel au lieu de l'id ou data-testid.

Maintenant, après avoir cliqué sur le bouton, nous attendons que le compteur soit incrémenté avec `waitForElement(() => getByText('1'))`. Et une fois que le compteur est incrémenté à 1, nous pouvons maintenant passer à la condition et vérifier si le compteur est effectivement égal à 1.

Cela étant dit, passons maintenant à des cas de test plus complexes.

_Êtes-vous prêt ?_

![ready](https://media.giphy.com/media/Y3MbPtRn74uR3Ziq4P/source.gif)

## 5. Tester React Redux

Si vous êtes nouveau dans React Redux, [cet article](https://www.ibrahima-ndaw.com/blog/7-steps-to-understand-react-redux/) pourrait vous aider. Sinon, vérifions à quoi ressemble `TestRedux.js`.

* `TestRedux.js`

```jsx
import React from 'react'
import { connect } from 'react-redux'

const TestRedux = ({counter, dispatch}) => {

 const increment = () => dispatch({ type: 'INCREMENT' })
 const decrement = () => dispatch({ type: 'DECREMENT' })
  
 return (
  <>
    <h1 data-testid="counter">{ counter }</h1>
    <button data-testid="button-up" onClick={increment}>Up</button>
    <button data-testid="button-down" onClick={decrement}>Down</button>
 </>
    )
  }
  
export default connect(state => ({ counter: state.count }))(TestRedux)

```

Et pour le reducer :

* `store/reducer.js`

```jsx
export const initialState = {
    count: 0,
  }
  
  export function reducer(state = initialState, action) {
    switch (action.type) {
      case 'INCREMENT':
        return {
          count: state.count + 1,
        }
      case 'DECREMENT':
        return {
          count: state.count - 1,
        }
      default:
        return state
    }
  }

```

Comme vous pouvez le voir, il n'y a rien de fantaisiste, c'est juste un composant Counter basique géré par React Redux.

Maintenant, écrivons les tests unitaires.

Test si l'état initial est égal à 0 :

`TestRedux.test.js`

```jsx
import React from 'react'
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import { render, cleanup, fireEvent } from '@testing-library/react';
import { initialState, reducer } from '../store/reducer'
import TestRedux from './TestRedux'

const renderWithRedux = (
  component,
  { initialState, store = createStore(reducer, initialState) } = {}
) => {
  return {
    ...render(<Provider store={store}>{component}</Provider>),
    store,
  }
}

 afterEach(cleanup);

it('checks initial state is equal to 0', () => {
    const { getByTestId } = renderWithRedux(<TestRedux />)
    expect(getByTestId('counter')).toHaveTextContent('0')
  })

```

Il y a quelques choses que nous devons importer pour tester React Redux. Et ici, nous créons notre propre fonction d'assistance `renderWithRedux()` pour rendre le composant puisqu'elle sera utilisée plusieurs fois.

`renderWithRedux()` reçoit comme paramètres le composant à rendre, l'état initial et le store. Si il n'y a pas de store, il en créera un nouveau, et s'il ne reçoit pas d'état initial ou de store, il retourne un objet vide.

Ensuite, nous utilisons `render()` pour rendre le composant et passer le store au Provider.

Cela étant dit, nous pouvons maintenant passer le composant `TestRedux` à `renderWithRedux()` pour tester si le compteur est égal à `0`.

Test si le compteur s'incrémente et se décrémente correctement :

`TestRedux.test.js` (ajoutez le bloc de code suivant au fichier)

```jsx
it('increments the counter through redux', () => {
  const { getByTestId } = renderWithRedux(<TestRedux />, 
    {initialState: {count: 5}
})
  fireEvent.click(getByTestId('button-up'))
  expect(getByTestId('counter')).toHaveTextContent('6')
})

it('decrements the counter through redux', () => {
  const { getByTestId} = renderWithRedux(<TestRedux />, {
    initialState: { count: 100 },
  })
  fireEvent.click(getByTestId('button-down'))
  expect(getByTestId('counter')).toHaveTextContent('99')
})

```

Pour tester les événements d'incrémentation et de décrémentation, nous passons un état initial comme deuxième argument à `renderWithRedux()`. Maintenant, nous pouvons cliquer sur les boutons et tester si le résultat attendu correspond à la condition ou non.

Maintenant, passons à la section suivante et introduisons React Context.

_React Router et Axios viendront ensuite, êtes-vous toujours avec moi ?_

![of-course](https://media.giphy.com/media/l41YfdYdptDB9RHIA/source.gif)

## 6. Tester React Context

Si vous êtes nouveau dans React Context, consultez d'abord [cet article](https://www.ibrahima-ndaw.com/blog/redux-vs-react-context-which-one-should-you-choose/). Sinon, vérifions le fichier `TextContext.js`.

* `TextContext.js`

```jsx
import React from "react"

export const CounterContext = React.createContext()

const CounterProvider = () => {
  const [counter, setCounter] = React.useState(0)
  const increment = () => setCounter(counter + 1)
  const decrement = () => setCounter(counter - 1)

  return (
    <CounterContext.Provider value={{ counter, increment, decrement }}>
      <Counter />
    </CounterContext.Provider>
  )
}

export const Counter = () => {  
    const { counter, increment, decrement } = React.useContext(CounterContext)   
    return (
     <>
       <h1 data-testid="counter">{ counter }</h1>
       <button data-testid="button-up" onClick={increment}> Up</button>
       <button data-testid="button-down" onClick={decrement}>Down</button>
    </>
       )
}

export default CounterProvider

```

Maintenant, l'état du compteur est géré via React Context. Écrivons le test unitaire pour vérifier s'il se comporte comme prévu.

Test si l'état initial est égal à 0 :

`TextContext.test.js`

```jsx
import React from 'react'
import { render, cleanup,  fireEvent } from '@testing-library/react'
import CounterProvider, { CounterContext, Counter } from './TestContext'

const renderWithContext = (
  component) => {
  return {
    ...render(
        <CounterProvider value={CounterContext}>
            {component}
        </CounterProvider>)
  }
}

afterEach(cleanup);

it('checks if initial state is equal to 0', () => {
    const { getByTestId } = renderWithContext(<Counter />)
    expect(getByTestId('counter')).toHaveTextContent('0')
})

```

Comme dans la section précédente avec React Redux, ici nous utilisons la même approche, en créant une fonction d'assistance `renderWithContext()` pour rendre le composant. Mais cette fois, elle ne reçoit que le composant comme paramètre. Et pour créer un nouveau contexte, nous passons `CounterContext` au Provider.

Maintenant, nous pouvons tester si le compteur est initialement égal à 0 ou non.

Test si le compteur s'incrémente et se décrémente correctement :

`TextContext.test.js` (ajoutez le bloc de code suivant au fichier)

```jsx
  it('increments the counter', () => {
    const { getByTestId } = renderWithContext(<Counter />)

    fireEvent.click(getByTestId('button-up'))
    expect(getByTestId('counter')).toHaveTextContent('1')
  })

  it('decrements the counter', () => {
    const { getByTestId} = renderWithContext(<Counter />)

    fireEvent.click(getByTestId('button-down'))
    expect(getByTestId('counter')).toHaveTextContent('-1')
  })

```

Comme vous pouvez le voir, ici nous déclenchons un événement de clic pour tester si le compteur s'incrémente correctement à 1 et se décrémente à -1.

Cela étant dit, nous pouvons maintenant passer à la section suivante et introduire React Router.

## 7. Tester React Router

Si vous voulez plonger dans React Router, [cet article](https://www.ibrahima-ndaw.com/blog/the-complete-guide-to-react-router/) pourrait vous aider. Sinon, vérifions le fichier `TestRouter.js`.

* `TestRouter.js`

```jsx
import React from 'react'
import { Link, Route, Switch,  useParams } from 'react-router-dom'

const About = () => <h1>About page</h1>

const Home = () => <h1>Home page</h1>

const Contact = () => {
  const { name } = useParams()
  return <h1 data-testid="contact-name">{name}</h1>
}

const TestRouter = () => {
    const name = 'John Doe'
    return (
    <>
    <nav data-testid="navbar">
      <Link data-testid="home-link" to="/">Home</Link>
      <Link data-testid="about-link" to="/about">About</Link>
      <Link data-testid="contact-link" to={`/contact/${name}`}>Contact</Link>
    </nav>
    
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/about:name" component={Contact} />
      </Switch>
    </>
  )
}

export default TestRouter

```

Ici, nous avons quelques composants à rendre lors de la navigation sur la page d'accueil.

Maintenant, écrivons les tests :

* `TestRouter.test.js`

```jsx
import React from 'react'
import { Router } from 'react-router-dom'
import { render, fireEvent } from '@testing-library/react'
import { createMemoryHistory } from 'history'
import TestRouter from './TestRouter'


const renderWithRouter = (component) => {
    const history = createMemoryHistory()
    return { 
    ...render (
    <Router history={history}>
        {component}
    </Router>
    )
  }
}

it('should render the home page', () => {

  const { container, getByTestId } = renderWithRouter(<TestRouter />) 
  const navbar = getByTestId('navbar')
  const link = getByTestId('home-link')

  expect(container.innerHTML).toMatch('Home page')
  expect(navbar).toContainElement(link)
})

```

Pour tester React Router, nous devons d'abord avoir un historique de navigation pour commencer. Par conséquent, nous utilisons `createMemoryHistory()` pour, comme le suggère le nom, créer un historique de navigation.

Ensuite, nous utilisons notre fonction d'assistance `renderWithRouter()` pour rendre le composant et passer `history` au composant `Router`. Avec cela, nous pouvons maintenant tester si la page chargée au début est la page d'accueil ou non. Et si la barre de navigation est chargée avec les liens attendus.

Test si la navigation vers d'autres pages avec les paramètres fonctionne lorsque nous cliquons sur les liens :

`TestRouter.test.js` (ajoutez le bloc de code suivant au fichier)

```jsx
it('should navigate to the about page', ()=> {
  const { container, getByTestId } = renderWithRouter(<TestRouter />) 

  fireEvent.click(getByTestId('about-link'))

  expect(container.innerHTML).toMatch('About page')
})

it('should navigate to the contact page with the params', ()=> {
  const { container, getByTestId } = renderWithRouter(<TestRouter />) 
   
  fireEvent.click(getByTestId('contact-link'))
   
  expect(container.innerHTML).toMatch('John Doe')
})

```

Maintenant, pour vérifier si la navigation fonctionne, nous devons déclencher un événement de clic sur les liens de navigation.

Pour le premier test, nous vérifions si le contenu est égal au texte dans la page À propos, et pour le second, nous testons les paramètres de routage et vérifions s'ils sont passés correctement.

Nous pouvons maintenant passer à la section finale et apprendre comment tester une requête Axios.

_Nous avons presque terminé !_

![still-here](https://media.giphy.com/media/h3inb3B7bEAq43iui9/source.gif)

## 8. Tester les requêtes HTTP

Comme d'habitude, voyons d'abord à quoi ressemble le fichier `TextAxios.js`.

* `TextAxios.js`

```jsx
import React from 'react'
import axios from 'axios'

const TestAxios = ({ url }) => {
  const [data, setData] = React.useState()

  const fetchData = async () => {
    const response = await axios.get(url)
    setData(response.data.greeting)    
 }     
 
 return (
  <>
    <button onClick={fetchData} data-testid="fetch-data">Load Data</button>
    { 
    data ?
    <div data-testid="show-data">{data}</div>:
    <h1 data-testid="loading">Loading...</h1>
    }
  </>
     )
}

export default TestAxios

```

Comme vous pouvez le voir ici, nous avons un composant simple qui a un bouton pour faire une requête. Et si les données ne sont pas disponibles, il affichera un message de chargement.

Maintenant, écrivons les tests.

Test si les données sont récupérées et affichées correctement :

`TextAxios.test.js`

```jsx
import React from 'react'
import { render, waitForElement, fireEvent } from '@testing-library/react'
import axiosMock from 'axios'
import TestAxios from './TestAxios'

jest.mock('axios')

it('should display a loading text', () => {

 const { getByTestId } = render(<TestAxios />)

  expect(getByTestId('loading')).toHaveTextContent('Loading...')
})

it('should load and display the data', async () => {
  const url = '/greeting'
  const { getByTestId } = render(<TestAxios url={url} />)

  axiosMock.get.mockResolvedValueOnce({
    data: { greeting: 'hello there' },
  })

  fireEvent.click(getByTestId('fetch-data'))

  const greetingData = await waitForElement(() => getByTestId('show-data'))

  expect(axiosMock.get).toHaveBeenCalledTimes(1)
  expect(axiosMock.get).toHaveBeenCalledWith(url)
  expect(greetingData).toHaveTextContent('hello there')
})

```

Ce cas de test est un peu différent car nous devons gérer une requête HTTP. Et pour cela, nous devons simuler une requête axios avec l'aide de `jest.mock('axios')`.

Maintenant, nous pouvons utiliser `axiosMock` et appliquer une méthode `get()` à celui-ci. Enfin, nous utiliserons la fonction Jest `mockResolvedValueOnce()` pour passer les données simulées comme paramètre.

Avec cela, maintenant pour le deuxième test, nous pouvons cliquer sur le bouton pour récupérer les données et utiliser async/await pour les résoudre. Et maintenant, nous devons tester 3 choses :

1. Si la requête HTTP a été effectuée correctement
2. Si la requête HTTP a été effectuée avec l'`url`
3. Si les données récupérées correspondent à l'attente.

Et pour le premier test, nous vérifions simplement si le message de chargement est affiché lorsque nous n'avons pas de données à montrer.

Cela étant dit, nous avons maintenant terminé les 8 étapes simples pour commencer à tester vos applications React.

_N'ayez plus peur de tester._

![not-scared](https://media.giphy.com/media/xUA7beT9PDJoDNAmgU/200w_d.gif)

## Réflexions finales

La React Testing Library est un excellent package pour tester les applications React. Elle nous donne accès aux matchers `jest-dom` que nous pouvons utiliser pour tester nos composants plus efficacement et avec de bonnes pratiques. Espérons que cet article a été utile et qu'il vous aidera à construire des applications React robustes à l'avenir.

Vous pouvez trouver le projet terminé [ici](https://github.com/ibrahima92/react-testing-library-guide)

Merci de l'avoir lu !

[Lire plus d'articles](https://www.ibrahima-ndaw.com/)  -  [S'abonner à ma newsletter](https://ibrahima-ndaw.us5.list-manage.com/subscribe?u=8dedf5d07c7326802dd81a866&id=5d7bcd5b75)   -   [Me suivre sur twitter](https://twitter.com/ibrahima92_)

Vous pouvez lire d'autres articles comme celui-ci sur [mon blog](https://www.ibrahima-ndaw.com/blog/react-testing-library-guide/).

## Prochaines étapes

[Documentation de React Testing Library](https://testing-library.com/docs/react-testing-library/intro)

[Cheatsheet de React Testing Library](https://testing-library.com/docs/react-testing-library/cheatsheet)

[Cheatsheet des matchers Jest DOM](https://github.com/testing-library/jest-dom)

[Documentation de Jest](https://jestjs.io/docs/en/getting-started.html)