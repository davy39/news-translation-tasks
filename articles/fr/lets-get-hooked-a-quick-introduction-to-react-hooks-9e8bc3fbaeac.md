---
title: 'Découvrons les Hooks : une introduction rapide aux React Hooks'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T18:53:07.000Z'
originalURL: https://freecodecamp.org/news/lets-get-hooked-a-quick-introduction-to-react-hooks-9e8bc3fbaeac
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hwW04YcPNKdDmkmDaoaXDw.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: hooks
  slug: hooks
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: 'tech '
  slug: tech
seo_title: 'Découvrons les Hooks : une introduction rapide aux React Hooks'
seo_desc: 'By Lekha Surasani

  Getting Started with React Hooks

  The React team introduced React Hooks to the world at React Conf in late October
  2018. In early February 2019, they finally came in React v16.8.0. While I, like
  most others probably, won’t be able to...'
---

Par Lekha Surasani

#### Introduction aux React Hooks

L'équipe React a présenté les React Hooks au monde lors de la React Conf à la fin octobre 2018. Début février 2019, ils ont finalement été intégrés dans React v16.8.0. Bien que, comme la plupart des autres probablement, je ne pourrai pas les utiliser en production pendant un certain temps (jusqu'à ce que nous décidions de mettre à jour React), j'ai été en train de les expérimenter en parallèle.

J'étais tellement enthousiaste à ce sujet que je vais donner une conférence d'introduction à ce sujet lors d'une rencontre locale. De plus, je donnerai une conférence sur les Hooks (et autres fonctionnalités à venir de React) à WeRockITConf à Huntsville en mai ! (ÉDITION : J'ai maintenant donné ces conférences et vous pouvez trouver les présentations et les ressources associées sur [mon site web](https://lekhasurasani.com/speaking) !) Mais pour l'instant, voici comment commencer avec les React Hooks !

# Que sont les Hooks exactement ?

Les React Hooks vous permettent d'utiliser l'état et d'autres fonctionnalités de React sans avoir à définir une classe JavaScript. C'est comme pouvoir profiter de la propreté et de la simplicité d'un Composant Pur _et_ de l'état et des méthodes du cycle de vie des composants. Cela est dû au fait que les Hooks sont simplement des fonctions JavaScript régulières ! Cela permet d'avoir un code plus propre et moins encombrant. Une comparaison côte à côte de ce à quoi ressemble le code avec et sans Hooks pour un simple composant de comptage :

```js
import './App.css';
import React, { useState } from 'react';

const HooksExample = () => {
    const [counter, setCount] = useState(0);

    return (
        <div className="App">
            <header className="App-header">
                Le bouton est pressé : { counter } fois.
                <button
                    onClick={() => setCount(counter + 1)}
                    style={{ padding: '1em 2em', margin: 10 }}
                >
                    Cliquez-moi !
                </button>
            </header>
        </div>
    )
}

export default HooksExample;
```

NoHooks.js :

```js
import './App.css';
import React, { Component } from 'react';

export class NoHooks extends Component {
    constructor(props) {
        super(props);
        this.state = {
            counter: 0
        }
    }
    
    render() {
        const { counter } = this.state;
        return (
            <div className="App">
                <header className="App-header">
                    Le bouton est pressé : { counter } fois.
                    <button
                        onClick={() => this.setState({ counter: counter + 1 }) }
                        style={{ padding: '1em 2em', margin: 10 }}
                    >
                        Cliquez-moi !
                    </button>
                </header>
            </div>
        )	
    }
}

export default NoHooks;
```

Non seulement le code est beaucoup plus petit — l'espace économisé s'accumule certainement pour les composants plus grands — mais il est aussi beaucoup plus _lisible_, ce qui est un énorme avantage des Hooks. Pour les débutants qui commencent tout juste avec React, il est plus facile pour eux de lire le premier bloc de code et de voir exactement ce qui se passe. Avec le deuxième bloc, nous avons quelques éléments superflus, et c'est assez pour vous faire arrêter et vous demander à quoi cela sert.

Une autre chose géniale à propos des hooks est que vous pouvez créer les vôtres ! Cela signifie que beaucoup de la logique d'état que nous devions réécrire d'un composant à l'autre, nous pouvons maintenant l'abstraire dans un hook personnalisé — et _la réutiliser_.

Un exemple où cela est particulièrement révolutionnaire (pour moi) qui me vient à l'esprit est l'utilisation avec les formulaires. Avec toute la logique d'état des formulaires, il est difficile de réduire la taille du composant. Mais maintenant, avec les hooks, les formulaires complexes peuvent devenir beaucoup plus simples sans l'utilisation d'autres bibliothèques de formulaires.

Mais avant d'en arriver là, examinons le hook en question — useState.

# useState

useState, comme son nom l'indique, est un hook qui vous permet d'utiliser l'état dans votre fonction. Nous le définissons comme suit :

const [ someState, updateState ] = useState(initialState)

Décomposons cela :

* **someState** : vous permet d'accéder à la variable d'état actuelle, _someState_
* **updateState** : fonction qui vous permet de mettre à jour l'état — tout ce que vous passez dedans devient le nouveau _someState_
* **initialState** : ce que vous voulez que _someState_ soit lors du rendu initial

(Si vous n'êtes pas familier avec la syntaxe de déstructuration de tableau, arrêtez-vous ici et lisez [ceci](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment#Basic_variable_assignment).)

Maintenant que nous comprenons le format de base de useState et comment l'appeler et l'utiliser, revenons à l'exemple précédent.

Dans cet exemple, **counter** est la variable d'état, **setCount** est la fonction de mise à jour, et **0** est l'état initial. Nous utilisons **setCount(counter + 1)** pour incrémenter le compteur lorsque le bouton est pressé, faisant de **counter + 1** la nouvelle valeur de **counter**. Alternativement, si nous voulions utiliser l'état précédent pour mettre à jour l'état actuel, nous pourrions passer l'ancien état à setCount :

`setCount(prevCount => prevCount + 1)`

Ceci est un exemple simple qui ne reflète pas ce que nous utiliserions normalement dans une application réelle. Mais examinons quelque chose que nous sommes plus susceptibles d'utiliser — un simple formulaire de connexion pour l'email et le mot de passe :

```js
import './App.css';
import React, { useState } from 'react';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        const { handleSubmit } = this.props;
        <div className="App">
            <header className="App-header">
                <form onSubmit={handleSubmit}>
                    <input value={ email } onChange={(e) => setEmail(e.target.value) } />
                    <input value={ password } onChange={(e) => setPassword(e.target.value) } />
                    <button type="submit">Soumettre</button>
                </form>
            </header>
        </div>
    )
}

export default LoginForm;
```

Nous avons deux champs d'état séparés et des fonctions de mise à jour d'état. Cela nous permet de créer des formulaires vraiment simples sans créer une classe JavaScript entière.

Si nous voulions simplifier cela davantage, nous pourrions créer un objet comme état. Cependant, useState remplace tout l'état au lieu de mettre à jour l'objet (comme le ferait setState), donc nous pouvons reproduire le comportement habituel de setState comme montré ci-dessous :

```js
import './App.css';
import React, { useState } from 'react';

const LoginForm = () => {
    const [login, setLogin] = useState({ email: '', password: '' });

    return (
        const { handleSubmit } = this.props;
        <div className="App">
            <header className="App-header">
                <form onSubmit={handleSubmit}>
                    <input value={ login.email } onChange={(e) => setLogin(prevState => { ...prevState, email: e.target.value }) } />
                    <input value={ login.password } onChange={(e) => setLogin(prevState => { ...prevState, password: e.target.value }) } />
                    <button type="submit">Soumettre</button>
                </form>
            </header>
        </div>
    )
}

export default LoginForm;
```

Si vous avez des objets d'état plus complexes que cela, vous voudrez soit les diviser en états séparés comme dans le premier exemple de connexion, soit utiliser useReducer (nous y viendrons bientôt !).

Nous avons donc l'état dans les hooks. Qu'en est-il des méthodes du cycle de vie des composants ?

# useEffect

useEffect est un autre hook qui gère componentDidUpdate, componentDidMount et componentWillUnmount en un seul appel. Si vous devez récupérer des données, par exemple, vous pourriez utiliser useEffect pour le faire, comme vu ci-dessous.

```js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const HooksExample = () => {
    const [data, setData] = useState();

    useEffect(() => {
        const fetchGithubData = async (name) => {
            const result = await axios(`https://api.github.com/users/${name}/events`)
            setData(result.data)
        }
        fetchGithubData('lsurasani')
    }, [data])

    

    return (
        <div className="App">
            <header className="App-header">
                {data && (
                    data.map(item => <p>{item.repo.name}</p>)
                )}
            </header>
        </div>
    )
}

export default HooksExample;
```

En regardant useEffect, nous voyons :

* Premier argument : Une fonction. À l'intérieur, nous récupérons nos données en utilisant une fonction asynchrone puis nous définissons **data** lorsque nous obtenons des résultats.
* Deuxième argument : Un tableau contenant **data**. Cela définit quand le composant se met à jour. Comme je l'ai mentionné précédemment, useEffect s'exécute lorsque componentDidMount, componentWillUnmount, _et_ componentDidUpdate s'exécuteraient normalement. À l'intérieur du premier argument, nous avons défini un état, ce qui provoquerait traditionnellement l'exécution de componentDidUpdate. Par conséquent, useEffect s'exécuterait à nouveau si nous n'avions pas ce tableau. Maintenant, useEffect s'exécutera sur componentDidMount, componentWillUnmount, et si **data** a été mis à jour, componentDidUpdate. Cet argument peut être vide — vous pouvez choisir de passer un tableau vide. Dans ce cas, seuls componentDidMount et componentWillUnmount seront jamais déclenchés. Mais vous devez spécifier cet argument si vous définissez un état à l'intérieur.

# useReducer

Pour ceux d'entre vous qui utilisent Redux, useReducer vous sera probablement familier. useReducer prend deux arguments — un **réducteur** et un **état initial**. Un réducteur est une fonction que vous pouvez définir qui prend l'état actuel et une « action ». L'action a un type, et le réducteur utilise une instruction switch pour déterminer quel bloc exécuter en fonction du type. Lorsqu'il trouve le bon bloc, il retourne l'état mais avec les modifications que vous définissez en fonction du type. Nous pouvons passer ce réducteur dans useReducer, puis utiliser ce hook comme ceci :

`const [ state, dispatch ] = useReducer(reducer, initialState)`

Vous utilisez dispatch pour dire quels types d'action vous voulez exécuter, comme ceci :

`dispatch({ type: name})`

useReducer est normalement utilisé lorsque vous devez gérer des états complexes — comme le formulaire d'inscription ci-dessous.

```js
import React, { useReducer } from 'react';

const reducer = (state, action) => {
    switch (action.type) {
        case 'firstName': {
            return { ...state, firstName: action.value };
            }
        case 'lastName': {
            return { ...state, lastName: action.value };
            }
        case 'email': {
            return { ...state, email: action.value };
            }
        case 'password': {
            return { ...state, password: action.value };
            }
        case 'confirmPassword': {
            return { ...state, confirmPassword: action.value };
            }
        default: {
            return state;
        }
    }
};

function SignupForm() {
    const initialState = {
        firstName: '',
        lastName: '',
        email: '',
        password: '',
        confirmPassword: '',
    }
    const [formElements, dispatch] = useReducer(reducer, initialState);

    return (
        <div className="App">
            <header className="App-header">
                <div>
                    <input placeholder="Prénom" value={ formElements.firstName} onChange={(e) => dispatch({ type: 'firstName', value: e.target.value }) } />
                    <input placeholder="Nom" value={ formElements.lastName} onChange={(e) => dispatch({ type: 'lastName', value: e.target.value }) } />
                    <input placeholder="Email" value={ formElements.email} onChange={(e) => dispatch({ type: 'email', value: e.target.value }) } />
                    <input placeholder="Mot de passe" value={ formElements.password} onChange={(e) => dispatch({ type: 'password', value: e.target.value }) } />
                    <input placeholder="Confirmer le mot de passe" value={ formElements.confirmPassword} onChange={(e) => dispatch({ type: 'confirmPassword', value: e.target.value }) } />
                </div>
            </header>
        </div>
    );
}

export default SignupForm;

```

Ce hook a de nombreuses applications supplémentaires, y compris la possibilité de spécifier quelques réducteurs dans toute notre application et de les réutiliser pour chacun de nos composants, en changeant en fonction de ce qui se passe dans ces composants. À un niveau élevé, cela est similaire à la fonctionnalité de Redux — nous pourrions donc éviter d'utiliser Redux pour des applications relativement plus simples.

# Hooks personnalisés

Nous avons donc couvert 3 hooks de base — examinons comment créer les nôtres. Vous souvenez-vous de l'exemple que j'ai mentionné précédemment avec le formulaire de connexion ? Le voici à nouveau pour vous rafraîchir la mémoire :

```js
import './App.css';
import React, { useState } from 'react';

const LoginForm = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        const { handleSubmit } = this.props;
        <div className="App">
            <header className="App-header">
                <form onSubmit={handleSubmit}>
                    <input value={ email } onChange={(e) => setEmail(e.target.value) } />
                    <input value={ password } onChange={(e) => setPassword(e.target.value) } />
                    <button type="submit">Soumettre</button>
                </form>
            </header>
        </div>
    )
}

export default LoginForm;
```

Nous utilisons useState pour les deux et définissons une variable d'état et une fonction de mise à jour pour les deux champs. Et si nous pouvions simplifier cela davantage ? Voici un hook personnalisé pour gérer tout type de changements de valeur d'entrée (note : la convention pour nommer un hook personnalisé est : use<description de la fonction>).

```js
import { useState } from 'react';

export const useInputValue = (initial) => {
    const [value, setValue] = useState(initial)
    return { value, onChange: e => setValue(e.target.value) }
}
```

Nous utilisons useState pour gérer les changements comme nous l'avons fait dans l'exemple précédent, mais cette fois nous retournons la valeur et une fonction onChange pour mettre à jour cette valeur. Ainsi, le formulaire de connexion peut maintenant ressembler à ceci :

```js
import React from 'react';
import { useInputValue } from './Custom'

const Form = () => {
    const email = useInputValue('')
    const password = useInputValue('')

    return (
        <div className="App">
            <header className="App-header">
                <div>
                    <input type="text" placeholder="Email" {...email} />
                </div>
                <div>
                    <input type="password" placeholder="Mot de passe" {...password} />
                </div>
            </header>
        </div>
    );
}

export default Form;
```

Nous initialisons useInputValue avec une chaîne vide pour les deux champs, et définissons le résultat au nom du champ. Nous pouvons remettre cela dans l'élément d'entrée afin que l'élément d'entrée rende la valeur et les fonctions onChange dynamiquement.

Maintenant, nous avons rendu ce formulaire encore plus simple — et notre hook personnalisé peut être réutilisé partout où nous avons besoin d'un élément de formulaire d'entrée !

Je pense que c'est l'une des choses les plus utiles à propos des hooks — la capacité de créer les vôtres et de permettre à cette logique d'état précédemment verrouillée à l'intérieur de chaque composant d'être extraite et réutilisée, permettant à chaque composant de devenir plus simple.

Nous avons donc passé en revue : useState, useEffect, useReducer, et enfin, les hooks personnalisés. Il y a quelques choses de base que nous n'avons pas encore couvertes — à savoir, les deux règles générales à suivre avec les Hooks :

1. **N'appeler les Hooks qu'au _niveau supérieur_** — Pas dans les boucles, les fonctions imbriquées, les conditions, etc. Cela garantit que les hooks sont toujours appelés dans le même ordre après chaque rendu. Cela est important car React s'appuie sur l'ordre dans lequel les Hooks sont appelés pour déterminer quel état correspond à un appel useState (si vous en utilisez plusieurs). Si l'un de vos hooks est caché dans une boucle, une fonction imbriquée ou une condition, l'ordre peut changer d'un rendu à l'autre, perturbant quel état correspond à quel useState.
2. **N'appeler les Hooks que depuis des fonctions React ou des hooks personnalisés** — En d'autres termes, n'appeler pas les Hooks depuis des fonctions JavaScript.

J'espère que cela clarifie comment et quand utiliser les hooks pour vous ! Voici quelques ressources supplémentaires que vous pouvez consulter :

* [La documentation React](https://reactjs.org/docs/hooks-intro.html)
* [Collection de ressources sur les Hooks](https://github.com/rehooks/awesome-react-hooks)

Si vous avez des questions ou des commentaires, n'hésitez pas à demander ci-dessous !