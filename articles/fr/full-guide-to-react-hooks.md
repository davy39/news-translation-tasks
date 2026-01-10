---
title: Comment utiliser les Hooks React – Tutoriel complet pour débutants
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-01-17T01:04:42.000Z'
originalURL: https://freecodecamp.org/news/full-guide-to-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/steve-johnson-6sB8gMRlEAU-unsplash.jpg
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment utiliser les Hooks React – Tutoriel complet pour débutants
seo_desc: 'Hi everyone! Hooks are one of the main features of modern React code and
  one of the first concepts you should get comfortable with when learning about this
  library.

  In this article I''m going to explain some of the most useful hooks React provides
  us ...'
---

Bonjour à tous ! Les Hooks sont l'une des principales fonctionnalités du code React moderne et l'un des premiers concepts avec lesquels vous devez vous familiariser lorsque vous apprenez cette bibliothèque.

Dans cet article, je vais expliquer certains des Hooks les plus utiles que React nous fournit, comment ils fonctionnent et des exemples de situations dans lesquelles nous pouvons les utiliser.

J'espère que vous apprécierez la lecture. C'est parti !

# Table des matières

* [Un peu d'histoire sur React et à quoi servent les Hooks](#heading-un-peu-dhistoire-sur-react-et-a-quoi-servent-les-hooks)
    
* [Hooks React fréquemment utilisés](#heading-hooks-react-frequemment-utilises)
    
    * [Hook UseState](#heading-usestate-hook)
        
    * [Hook UseEffect](#useEffect-hook)
        
    * [Hook UseContext](#useContext-hook)
        
    * [Hook UseRef](#useRef-hook)
        
    * [Hook UseReducer](#useReducer-hook)
        
* [Quelques Hooks moins courants mais toujours utiles](#heading-quelques-hooks-moins-courants-mais-toujours-utiles)
    
    * [Hook UseCallback](#useCallback-hook)
        
    * [Hook UseMemo](#useMemo-hook)
        
* [Hooks React personnalisés](#heading-hooks-react-personnalises)
    
* [Résumé](#heading-resume)
    

# Un peu d'histoire sur React et à quoi servent les Hooks

Comme vous le savez peut-être, React est une bibliothèque open-source utilisée pour construire des interfaces utilisateur de manière plus simple et plus efficace que les outils qui l'ont précédée (principalement vanilla JS et jQuery). Elle a été développée par Meta (anciennement Facebook) et publiée en 2013.

Les Hooks étaient une fonctionnalité introduite des années plus tard en 2016 (dans la version 16.8 de React). Pour avoir une idée de ce à quoi servent les Hooks et pourquoi ils constituent une amélioration par rapport à ce qui était fait auparavant, examinons un exemple de code "pré-Hooks" par rapport à un code React moderne "post-Hooks".

Dans l'ancien code React, nous utilisions des composants de classe. Ceux-ci avaient une méthode `render` qui contenait le JSX responsable du rendu de l'UI.

Et si nous voulions que ce composant stocke un état, nous devions le déclarer dans une méthode de constructeur et le modifier en appelant `this.setState`. Voici un court exemple pour vous donner une idée :

```javascript
// javascript
import React from "react"

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

      return (
        <div className="App">

          <button onClick={this.handleIncrement}>Incrémenter</button>
          <button onClick={this.handleDecrement}>Décrémenter</button>

          <h2>{this.state.count}</h2>
        </div>
      )
    }
  }

  export default Counter
```

Il est important de mentionner que les composants de fonction (ce que nous utilisons aujourd'hui) étaient également disponibles dans React "pré-Hooks". Mais nous ne pouvions les utiliser que pour des composants sans état – c'est-à-dire des composants qui ne stockaient pas d'état et n'étaient pas responsables d'une logique complexe autre que le rendu de l'UI.

Avec l'incorporation des Hooks, nous pouvons maintenant utiliser des composants de fonction (et leur composition plus directe et moins verbeuse) avec toutes les fonctionnalités plus complexes que les composants de classe nous offraient.

En bref, les Hooks sont des choses que nous utilisons pour implémenter la logique et les fonctionnalités dans nos composants.

Voici un autre exemple où nous transformons ce que nous avions dans notre composant de classe en un composant fonctionnel :

```javascript
// javascript
import { useState } from 'react'

export default function Counter() {

    const [count, setCount] = useState(0)

    const handleIncrement = () => setCount(count+1)
    const handleDecrement = () => setCount(count-1)

    return (
        <div className="App">
            <button onClick={() => handleIncrement()}>Incrémenter</button>
            <button onClick={() => handleDecrement()}>Décrémenter</button>

            <h2>{count}</h2>
        </div>                    
    )
}
```

# Hooks React fréquemment utilisés

Maintenant que vous avez une idée de ce à quoi servent les Hooks et pourquoi ils sont meilleurs que ce qui existait avant, examinons les plus utilisés, les occasions où ils sont utiles et comment les implémenter.

## Hook UseState

Dans React moderne, nous construisons nos applications avec des **composants fonctionnels**. Les composants sont eux-mêmes des fonctions JavaScript, des morceaux de code indépendants et **réutilisables**.

Le but de construire l'application avec des composants est d'avoir une architecture modulaire, avec une séparation claire des préoccupations. Cela rend le code plus facile à comprendre, plus facile à maintenir et plus facile à réutiliser lorsque c'est possible.

L'**état est un objet qui contient des informations** sur un certain composant. Les fonctions JavaScript simples n'ont pas la capacité de stocker des informations. Le code qu'elles contiennent s'exécute et "disparaît" une fois l'exécution terminée.

Mais grâce à l'état, les composants fonctionnels React peuvent stocker des informations même après l'exécution. Lorsque nous avons besoin qu'un composant stocke ou "se souvienne" de quelque chose, ou qu'il agisse différemment en fonction de l'environnement, l'état est ce dont nous avons besoin pour qu'il fonctionne de cette manière.

Il est important de mentionner que tous les composants d'une application React n'ont pas besoin d'avoir un état. Il existe également des composants sans état qui se contentent de rendre leur contenu sans avoir besoin de stocker des informations, et c'est tout à fait normal.

Une autre chose importante à mentionner est que le changement d'état est l'une des deux choses qui font qu'un composant React se re-rend (l'autre est un changement dans les props). De cette manière, l'état stocke des informations sur le composant et contrôle également son comportement.

Pour implémenter l'état dans nos composants, React nous fournit un Hook appelé **useState**. Voyons comment il fonctionne avec l'exemple suivant.

```js
// javascript
// App.js
import { useState } from 'react'

function App() {

  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <p>Le compte est : {count}</p>

      <div>
        <button onClick={() => setCount(count+1)}>Ajouter 1</button>
        <button onClick={() => setCount(count-1)}>Diminuer 1</button>

        <button onClick={() => setCount(count+10)}>Ajouter 10</button>
        <button onClick={() => setCount(count-10)}>Diminuer 10</button>

        <button onClick={() => setCount(0)}>Réinitialiser le compte</button>
      </div>
    </div>
  )
}

export default App
```

* Tout d'abord, nous importons le Hook depuis React : `import { useState } from 'react'`
    
* Ensuite, nous initialisons l'état : `const [count, setCount] = useState(0)`
    

Ici, nous fournissons un nom de variable pour l'état (`count`) et un nom de fonction que nous utiliserons chaque fois que nous devons mettre à jour cet état (`setCount`). Ensuite, nous définissons la valeur initiale de l'état (`0`), qui sera la valeur chargée par défaut chaque fois que l'application démarre.

* Enfin, comme mentionné ci-dessus, chaque fois que nous voulons mettre à jour l'état, nous devons utiliser la fonction que nous avons déclarée : `setCount`. Pour l'utiliser, nous devons simplement l'appeler en lui passant le nouvel état que nous voulons comme paramètre. C'est-à-dire, si nous voulons ajouter 1 à l'état précédent, nous appelons `setCount(count+1)`.
    

Comme mentionné également, cela provoquera une mise à jour de l'état et le re-rendu du composant. Ce qui, dans notre application, signifie que nous verrons à l'écran que le compteur augmente.

Il est important de mentionner que la fonction setState est **asynchrone**. Donc si nous essayons de lire l'état immédiatement après l'avoir mis à jour, comme ceci :

```js
<button onClick={() => {
          setCount(count+1)
          console.log(count)
}}>Ajouter 1</button>
```

nous obtiendrions la valeur précédente de l'état, sans la mise à jour.

La manière correcte de lire l'état après la mise à jour serait d'utiliser le Hook **useEffect**. Il nous permet d'exécuter une fonction après chaque re-rendu de composant (par défaut) ou après tout changement de variable particulier que nous déclarons.

Quelque chose comme ceci :

```js
useEffect(() => console.log(value), [value])
```

De plus, le fait que useState soit asynchrone a des implications lorsque l'on considère des changements d'état très fréquents et rapides.

Prenons, par exemple, le cas d'un utilisateur qui appuie sur le bouton AJOUTER plusieurs fois de suite, ou une boucle qui émet un événement de clic un certain nombre de fois.

En mettant à jour l'état comme `setCount(count+1)`, nous prenons le risque que `count` ne soit pas encore mis à jour lorsque le prochain événement est déclenché.

Par exemple, disons qu'au début `count = 0`. Ensuite, `setCount(count+1)` est appelé et l'état est mis à jour de manière asynchrone.

Mais ensuite, `setCount(count+1)` est à nouveau appelé, avant que la mise à jour de l'état ne soit terminée. Cela signifie que `count` est toujours égal à `0`, ce qui signifie que le deuxième `setCount` ne mettra pas à jour l'état correctement.

Une approche plus défensive consisterait à passer à `setCount` une fonction de rappel, comme ceci : `setCount(prevCount => prevCount+1)`.

Cela garantit que la valeur à mettre à jour est la plus récente et nous évite le problème mentionné ci-dessus. Chaque fois que nous effectuons des mises à jour sur un état précédent, nous devrions utiliser cette approche.

Si vous souhaitez approfondir les méthodes de gestion de l'état dans React, vous pouvez consulter [cet article](https://www.freecodecamp.org/news/how-to-manage-state-in-a-react-app/) que j'ai écrit il y a quelque temps.

## Hook UseEffect

Avec useState, useEffect sera probablement le Hook que vous utiliserez le plus lors du développement d'une application React. C'est comme le pain et le beurre pour le développeur React.

UseEffect vous permet d'exécuter un effet secondaire sur votre composant. Un effet secondaire signifie essentiellement quelque chose qui se produit après qu'une autre chose spécifique se soit produite.

Un cas d'utilisation typique est de récupérer des données une fois que le composant a été monté. Supposons que nous avons une fonction appelée `fetchData` qui est responsable de cela – notre Hook useEffect pourrait ressembler à ceci :

```plaintext
  useEffect(() => { fetchData() }, [])
```

La structure de ce Hook est assez simple. Il accepte deux arguments. Tout d'abord, nous avons un callback qui exécute notre fonction, puis nous avons un tableau appelé "tableau de dépendances". Si nous le laissons vide comme dans l'exemple, le callback s'exécutera après le rendu du composant.

Maintenant, supposons que nous voulons que notre effet secondaire s'exécute après qu'une variable a changé. En suivant l'exemple précédent que nous avons utilisé pour le Hook useState, pour notre effet secondaire après que la variable `count` a changé, nous pourrions définir useEffect comme ceci :

```plaintext
// javascript
// App.js
import { useState } from 'react'

function App() {

  const [count, setCount] = useState(0)
  
  useEffect(() => { console.log('Le compte a changé !') }, [count])

  return (
    <div className="App">
      <p>Le compte est : {count}</p>

      <div>
        <button onClick={() => setCount(count+1)}>Ajouter 1</button>
        <button onClick={() => setCount(count-1)}>Diminuer 1</button>

        <button onClick={() => setCount(count+10)}>Ajouter 10</button>
        <button onClick={() => setCount(count-10)}>Diminuer 10</button>

        <button onClick={() => setCount(0)}>Réinitialiser le compte</button>
      </div>
    </div>
  )
}

export default App
```

Une troisième et dernière chose à mentionner à propos de useEffect est la possibilité de retourner une fonction de "nettoyage". Cette fonction de "nettoyage" s'exécutera lorsque le composant sera démonté. En suivant notre exemple précédent, l'ajout d'une fonction de nettoyage pourrait ressembler à ceci :

```javascript
  useEffect(() => {
    fetchData()
    return cleanUp()
  }, [])
```

Les fonctions de nettoyage dans useEffect sont normalement utilisées pour annuler les abonnements afin d'éviter que React essaie de mettre à jour l'état d'un composant qui a déjà été démonté.

Pour plus d'informations sur la fonction de nettoyage de useEffect, vous pouvez vous référer à [cet article](https://blog.logrocket.com/understanding-react-useeffect-cleanup-function/).

## Hook UseContext

L'API de contexte React a été publiée en 2016 avec la version 16.3 de React. Ce que le contexte fait dans React, c'est fournir une solution pour le [prop drilling](https://www.freecodecamp.org/news/avoid-prop-drilling-with-react-context-api/).

Le prop drilling fait référence à la situation dans laquelle nous avons un composant parent qui stocke un état. Et sous ce parent, nous avons plusieurs niveaux de composants enfants.

Si nous devons rendre cet état dans un composant enfant qui est profondément imbriqué dans cette structure, la solution serait de passer l'état en tant que props tout au long de la chaîne de composants.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/propDrilling.png align="left")

*Un graphique du prop drilling*

Cette option fonctionne très bien. Le problème est que nous devrions répéter le même code dans de nombreux endroits différents, ce qui, si nous devons changer notre code plus tard (vous devrez toujours le faire tôt ou tard), est quelque chose de très fastidieux à travailler et sujet aux erreurs et aux bugs.

L'API de contexte résout cette situation en fournissant "un endroit" pour stocker l'état qui doit être consommé depuis de nombreuses parties différentes de notre application, et à travers différents niveaux de l'arbre des composants.

Le fonctionnement est le suivant : le composant de contexte stockera l'état donné, et depuis n'importe quel composant donné, nous pouvons lire et mettre à jour cet état, peu importe où se trouve ce composant. Nous oublions toutes les props. Au lieu de cela, nous pouvons simplement travailler directement avec le contexte et tous les composants qui lisent cet état de contexte se re-rendront lorsque l'état sera mis à jour.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/context.png align="left")

*Un graphique de la même situation mais en utilisant le contexte*

Maintenant que nous avons les bases théoriques, voyons comment le Hook useContext nous permet d'utiliser cette API. L'implémentation typique ressemblerait à ceci. Dans un dossier "contexte", nous aurons deux fichiers. `Context.js` et `ContextProvider.js`.

Dans `Context.js`, nous allons simplement initialiser l'API de contexte en utilisant la fonction `createContext`, qui prend comme argument l'état initial que nous voulons fournir (nous ne voulons rien dans ce cas, donc nous pouvons simplement passer null).

```plaintext
/// Context.js 
import { createContext } from 'react'

const Context = createContext(null)

export default Context

Dans `ContextProvider.js`, nous allons importer le contexte que nous avons initialisé dans le fichier précédent. Nous allons également initialiser les états que nous voulons consommer plus tard et mettre à jour depuis les composants de notre application. Enfin, nous retournons le fournisseur de contexte et avec l'objet `value`, nous passons tous les états et les fonctions setState que nous voulons consommer plus tard.

Le contextProvider est un HOC. Un **composant d'ordre supérieur ou HOC** est similaire à une fonction d'ordre supérieur en JavaScript (j'ai un article à ce sujet [ici](https://gercocca.hashnode.dev/higher-order-functions-and-callbacks)). 

Les fonctions d'ordre supérieur sont des fonctions qui prennent d'autres fonctions comme arguments OU retournent d'autres fonctions. Les HOC de React prennent un composant comme prop, et le manipulent à une certaine fin sans changer le composant lui-même. Vous pouvez penser à cela comme des composants enveloppants.
```

/// ContextProvider.js import { useState } from 'react' import Context from './Context'

const ContextProvider = ({children}) =&gt; {

const \[darkModeOn, setDarkModeOn\] = useState(true) const \[englishLanguage, setEnglishLanguage\] = useState(true)

return ( &lt;Context.Provider value={{ darkModeOn, setDarkModeOn, englishLanguage, setEnglishLanguage }} &gt; {children} &lt;/Context.Provider&gt; ) }

export default ContextProvider

```plaintext

Dans notre fichier `App.js`, nous allons envelopper tous les composants que nous voulons pouvoir interagir avec l'état avec notre contextProvider. Dans ce cas, nous voulons que toute l'application puisse consommer et mettre à jour le contexte, donc nous l'enveloppons tout.
```

/// App.js

import './App.scss' import { Suspense, lazy } from 'react' import { BrowserRouter as Router, Routes, Route } from 'react-router-dom' import ContextProvider from './context/ContextProvider' import ErrorBoundary from './ErrorBoundary'

const Header = lazy(() =&gt; import ('./components/header/Header')) const AboutPage = lazy(() =&gt; import ('./components/aboutPage/AboutPage')) const ProjectsPage = lazy(() =&gt; import('./components/projectsPage/ProjectsPage')) const ShortrProject = lazy(() =&gt; import('./components/projectsPage/shortrProject/ShortrProject')) const MixrProject = lazy(() =&gt; import('./components/projectsPage/mixrProject/MixrProject')) const HelprProject = lazy(() =&gt; import('./components/projectsPage/helprProject/HelprProject')) const MyWebsiteProject = lazy(() =&gt; import('./components/projectsPage/myWebsiteProject/MyWebsiteProject')) const CurriculumPage = lazy(() =&gt; import('./components/curriculumPage/CurriculumPage')) const BlogPage = lazy(() =&gt; import('./components/blogPage/BlogPage')) const ContactPage = lazy(() =&gt; import('./components/contactPage/ContactPage'))

export default function App() { return (

&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;

&lt;Route path='/' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/projects' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/projects/helpr' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/projects/myWebsite' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/projects/mixr' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/projects/shortr' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/curriculum' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/blog' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

&lt;Route path='/contact' element={&lt;Suspense fallback={&lt;&gt;&lt;/&gt;}&gt;}/&gt;

) }

```plaintext

Enfin, depuis le composant où nous voulons lire/mettre à jour l'état du contexte, nous importons le contexte et le Hook useContext et nous déstructurons les états et les fonctions de la manière suivante (et nous utilisons simplement les fonctions d'état et setState régulières).
```

import { useContext, useState } from 'react' import Context from '../../context/Context'

import { Link, NavLink } from 'react-router-dom'

const Header = () =&gt; {

const { darkModeOn, setDarkModeOn, englishLanguage, setEnglishLanguage } = useContext(Context)

const \[showMobileMenu, setShowMobileMenu\] = useState(false)

const openMobileMenu = () =&gt; { document.body.classList.add('mobileMenu-open') setShowMobileMenu(true) }

const hideMobileMenu = () =&gt; { document.body.classList.remove('mobileMenu-open') setShowMobileMenu(false) }

return ( &lt;header className={darkModeOn ? 'header header-dark' : 'header header-light'}&gt;

# Germán Cocca

# G

* {englishLanguage ? 'À propos' : 'Sobre mi'}
    
* {englishLanguage ? 'Projets' : 'Proyectos'}
    
* Blog
    
* Curriculum
    
* {englishLanguage ? 'Contact' : 'Contacto'}
    

&lt;button data-testid='es-language-btn' className={englishLanguage ? '' : 'selected'} onClick={() =&gt; setEnglishLanguage(false)}&gt;ES &lt;button data-testid='en-language-btn' className={englishLanguage ? 'selected' : ''} onClick={() =&gt; setEnglishLanguage(true)}&gt;EN

&lt;input type='checkbox' data-testid='dark-mode-toggle' id='dark-mode-toggle' aria-checked='true' className='toggle-checkbox' checked={darkModeOn} onClick={() =&gt; setDarkModeOn(!darkModeOn)} /&gt;

[&lt;div className="hamburguer-icon" onClick={() =&gt; showMobileMenu ? hideMobileMenu() : openMobileMenu()}&gt; &lt;div className={!showMobileMenu ? 'line' : 'line top'}&gt; &lt;div className={!showMobileMenu ? 'line' : 'line center'}&gt; &lt;div className={!showMobileMenu ? 'line' : 'line bottom'}&gt;](#menu)

&lt;nav id='mobile-menu' className={showMobileMenu ? 'mobile-menu-active' : 'mobile-menu'}&gt;

* &lt;NavLink to='/' onClick={() =&gt; hideMobileMenu()}&gt;{englishLanguage ? 'À propos' : 'Sobre mi'}
    
* &lt;NavLink to='/projects' onClick={() =&gt; hideMobileMenu()}&gt;{englishLanguage ? 'Projets' : 'Proyectos'}
    
* &lt;NavLink to='/blog' onClick={() =&gt; hideMobileMenu()}&gt;Blog
    
* &lt;NavLink to='/curriculum' onClick={() =&gt; hideMobileMenu()}&gt;Curriculum
    
* &lt;NavLink to='/contact' onClick={() =&gt; hideMobileMenu()}&gt;{englishLanguage ? 'Contact' : 'Contacto'}
    
* &lt;button className={englishLanguage ? '' : 'selected'} onClick={() =&gt; { setEnglishLanguage(false) hideMobileMenu() }}&gt;ES &lt;button className={englishLanguage ? 'selected' : ''} onClick={() =&gt; { setEnglishLanguage(true) hideMobileMenu() }}&gt;EN
    

) }

export default Header

````plaintext

C'est un peu plus de code que simplement tout passer par les props, mais c'est beaucoup plus maintenable, simple et facile à comprendre une fois que c'est configuré.

Une autre chose intéressante à mentionner est que nous pouvons avoir de nombreux contextes différents dans notre application. Nous pouvons les séparer par préoccupations. Par exemple, disons que nous en avons un pour les états d'authentification, un autre concernant les préférences et la configuration de l'utilisateur, un autre pour les paiements ou autre chose... Et ensuite nous pouvons envelopper ces contextes uniquement autour des composants spécifiques qui ont besoin de les utiliser. 

Donc, si nous avons beaucoup d'informations qui doivent être partagées dans notre application, avoir de nombreux contextes différents serait une approche plus modulaire et ordonnée pour cela.

## Hook UseReducer

UseReducer est un Hook qui nous permet d'implémenter des reducers de manière native dans notre application pour gérer des états complexes. Si vous êtes familier avec [Redux](https://redux.js.org/) ou des bibliothèques de gestion d'état similaires, le mot "reducer" vous dit probablement quelque chose.

En gros, les reducers sont une sorte de fonction qui prennent deux arguments ou plus, effectuent une sorte d'action avec eux et retournent un seul résultat qui découle des deux arguments. 

Un **reducer** est une fonction pure qui prend l'état précédent et une action comme arguments et retourne l'état suivant. Il est appelé reducer parce que c'est le même type de fonction que vous pourriez passer à un tableau : `Array.prototype.reduce(reducer, initialValue)`.

Mais avant de plonger dans les reducers, pourquoi en avons-nous besoin si nous avons déjà le Hook useState pour gérer notre état ? 

Eh bien, un problème qui peut survenir lorsque vous utilisez useState est le cas où le nouvel état à définir dépend de l'état précédent ou lorsque des changements d'état se produisent très fréquemment dans notre application. 

Dans ces occasions, useState peut provoquer un comportement inattendu et imprévisible. C'est là que les **reducers** interviennent pour résoudre ce problème.

**useReducer** est le Hook que React fournit et qui nous permet d'implémenter des reducers pour gérer notre état. Voici un exemple d'implémentation :

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
      <p>Le compte est : {state.count}</p>

      <div>
        <button onClick={() => dispatch({type: 'ADD'})}>Ajouter 1</button>
        
        <button onClick={() => dispatch({type: 'SUB'})}>Diminuer 1</button>

        <button onClick={() => dispatch({type: 'ADD10'})}>Ajouter 10</button>
        <button onClick={() => dispatch({type: 'SUB10'})}>Diminuer 10</button>

        <button onClick={() => dispatch({type: 'RESET'})}>Réinitialiser le compte</button>
      </div>
    </div>
  )
}

export default App
````

* Nous commençons par importer le Hook depuis React : `import { useReducer } from 'react'`
    
* Ensuite, nous déclarons une fonction reducer, qui prendra comme paramètres l'état actuel et une action à effectuer sur celui-ci. À l'intérieur, elle aura une instruction switch qui lira le type d'action, exécutera l'action correspondante sur l'état et retournera l'état mis à jour.
    

Il est courant d'utiliser des instructions switch sur les reducers et des lettres majuscules pour déclarer les actions.

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

* Ensuite, il est temps de déclarer notre Hook **useReducer**, qui ressemble beaucoup au Hook useState. Nous déclarons une **valeur pour notre état** ('state' dans notre cas), une **fonction que nous utiliserons pour le modifier** ('dispatch'), et ensuite useReducer prendra la **fonction reducer** comme premier paramètre et l'**état par défaut** comme deuxième paramètre.
    

```js
const [state, dispatch] = useReducer(reducer, { count: 0 })
```

* Enfin, pour mettre à jour notre état, nous n'appellerons pas directement le reducer, mais nous appellerons la fonction que nous venons de créer ('dispatch'), en lui passant le type d'action correspondant que nous voulons exécuter. En coulisses, la fonction dispatch se connectera avec le reducer et modifiera réellement l'état.
    

```js
<button onClick={() => dispatch({type: 'ADD'})}>Ajouter 1</button>
```

C'est un peu plus de code que d'utiliser useState, mais useReducer n'est pas si complexe après tout.

Pour résumer, nous avons juste besoin de :

* Un reducer, c'est-à-dire la fonction qui consolidera tous les changements d'état possibles
    
* Une fonction dispatch, qui enverra les actions de modification au reducer.
    

Le problème ici est que les éléments de l'UI ne pourront pas mettre à jour l'état directement comme ils le faisaient auparavant en appelant setState avec une valeur. Maintenant, ils devront appeler un type d'action et passer par le reducer, ce qui rend la gestion de l'état plus modulaire et prévisible.

De plus, si vous êtes familier avec Redux et d'autres bibliothèques de gestion d'état, vous avez probablement remarqué qu'avec l'API de contexte et le Hook useReducer, nous pouvons facilement implémenter les mêmes fonctionnalités que Redux fournit, mais de manière native dans React maintenant. Donc, personnellement, je pense que pour la plupart des cas d'utilisation, vous n'avez pas besoin d'une bibliothèque de gestion d'état dans le code React moderne.

L'histoire était différente avant, cependant, et c'est probablement pourquoi tant de bibliothèques de gestion d'état sont devenues populaires et pourquoi tant de développeurs les utilisent encore aujourd'hui.

## Hook UseRef

Le Hook useRef est une fonction qui retourne un objet ref mutable dont la propriété `.current` est initialisée avec l'argument passé (`initialValue`). L'objet retourné persistera pendant toute la durée de vie du composant.

Il y a deux utilisations principales de useRef : suivre une variable mutable à travers les re-rendus, et accéder aux nœuds DOM ou aux éléments React.

Nous pouvons déclarer une ref en utilisant le Hook useRef de la manière suivante : `const ref = useRef(initialValue)`. Ensuite, `reference.current` accède à la valeur de référence, et `reference.current = newValue` met à jour la valeur de référence. C'est assez simple.

Il y a 2 choses à retenir sur les refs :

1. La valeur de la référence est conservée entre les re-rendus du composant.
    
2. La mise à jour d'une référence ne déclenche pas un re-rendu du composant.
    

Pour voir un exemple de cela, imaginons un cas où nous devons compter le nombre de clics sur un bouton sans re-rendre un composant. Nous pourrions faire cela comme ceci :

```plaintext
import { useRef } from 'react';

function LogButtonClicks() {
    const countRef = useRef(0);
    
    const handle = () => {
        countRef.current++;
        console.log(`Cliqué ${countRef.current} fois`);
    };
    
    console.log('Je me suis rendu !');
    
    return <button onClick={handle}>Cliquez-moi</button>;
}
```

En mettant à jour et en journalisant la ref, nous évitons le re-rendu du composant et atteignons notre objectif. Donc, les 2 principales différences entre les références et l'état sont :

1. La mise à jour d'une référence ne déclenche pas de re-rendu, tandis que la mise à jour de l'état fait que le composant se re-rend.
    
2. Et aussi... La mise à jour de la référence est synchrone (la valeur de référence mise à jour est disponible immédiatement), tandis que la mise à jour de l'état est asynchrone (la variable d'état est mise à jour après le re-rendu).
    

# Quelques Hooks moins courants mais toujours utiles

Ici, je vais présenter deux Hooks qui sont utilisés pour la mémoisation dans React. Si vous n'êtes pas familier avec la mémoisation, vous pouvez vous référer à [cet article](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/) que j'ai écrit il y a quelque temps à ce sujet.

En gros, la mémoisation signifie faire en sorte que les composants "se souviennent" des props et de l'état, afin qu'ils se re-rendent uniquement si les props/l'état ont changé et évitent les re-rendus inutiles. Cela améliore les performances de l'application.

## Hook UseCallback

useCallback mémoïse les fonctions de rappel reçues en tant que props, afin qu'elles ne soient pas recréées à chaque re-rendu. L'utilisation correcte de useCallback peut améliorer les performances de notre application.

La manière dont nous pouvons l'implémenter est en enveloppant la fonction que nous passons en tant que props à un composant enfant dans le Hook useCallback, comme ceci :

```plaintext
import { useCallback } from 'react'
import Child from "./child"

export default function Counter() {

    return (
        <div className="App">
             <Child name={ useCallback(() => {console.log('Really Skinny Jack')}, [])  } />
        </div>                    
    )
}
```

Ce que fait useCallback, c'est de conserver la valeur de la fonction malgré le re-rendu du composant parent. Cela signifie que la prop de l'enfant restera la même tant que la valeur de la fonction restera la même également. Et cela résout le problème du re-rendu inutile de l'enfant.

Pour l'utiliser, nous devons simplement envelopper le Hook useCallback autour de la fonction que nous déclarons. useCallback a également un tableau de dépendances, comme useEffect. Dans le tableau présent dans le Hook, nous pouvons déclarer des variables qui déclencheraient le changement de la valeur de la fonction lorsque la variable change également (exactement de la même manière que useEffect fonctionne).

```javascript
const testingTheTest = useCallback(() => { 
    console.log("Testé");
  }, [a, b, c]);
```

## Hook UseMemo

**useMemo** est un Hook très similaire à useCallback. Mais au lieu de mettre en cache une fonction, useMemo mettra en cache la **valeur de retour d'une fonction**.

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

# Hooks React personnalisés

Si vous y réfléchissez, les Hooks sont simplement des fonctions qui nous permettent d'implémenter une logique couramment utilisée dans nos composants.

En suivant cette même ligne de pensée, dans les applications React, il est courant d'extraire les fonctionnalités fréquemment utilisées dans des fonctions et de les exporter avec un nom commençant par le préfixe `use`. C'est ce que nous appelons un Hook personnalisé.

Regardons un exemple de Hook personnalisé qui nous retourne la taille actuelle de la fenêtre lorsque nous l'appelons.

```plaintext
// Hook
const useWindowSize = () => {
  // Initialiser l'état avec une largeur/hauteur indéfinie
  const [windowSize, setWindowSize] = useState({
    width: undefined,
    height: undefined,
  });

// Gestionnaire à appeler lors du redimensionnement de la fenêtre
  const handleResize = () => {
    // Définir la largeur/hauteur de la fenêtre sur l'état
    setWindowSize({
        width: window.innerWidth,
        height: window.innerHeight,
      });
  }

  useEffect(() => {
    // Ajouter un écouteur d'événement
    window.addEventListener("resize", handleResize);
    // Appeler le gestionnaire immédiatement pour que l'état soit mis à jour avec la taille initiale de la fenêtre
    handleResize();
    // Retirer l'écouteur d'événement lors du nettoyage
    return () => window.removeEventListener("resize", handleResize);
  }, []); // Tableau vide garantit que l'effet n'est exécuté qu'au montage

  return windowSize;
}

export default useWindowSize;
```

Après, nous pouvons appeler et utiliser notre Hook personnalisé dans n'importe quel composant de la manière suivante :

```plaintext
// Utilisation
function App() {
  const size = useWindowSize();
  return (
    <div>
      {size.width}px / {size.height}px
    </div>
  );
}
```

Comme vous pouvez le voir dans l'exemple, les Hooks personnalisés peuvent également utiliser les Hooks natifs de React à l'intérieur d'eux. Mais pensez à eux comme à des fonctions qui exécutent une certaine logique couramment utilisée nécessaire dans diverses parties de notre application. Ce n'est rien de plus complexe que cela, vraiment.

Si vous souhaitez en savoir plus sur les Hooks personnalisés, [voici un site web dédié exclusivement à ce sujet](https://usehooks.com/).

# Résumé

Eh bien, tout le monde, dans cet article, nous avons examiné les Hooks, un sujet central dans les applications React actuelles. Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/01/kobe-bryant-mamba-out.gif align="left")