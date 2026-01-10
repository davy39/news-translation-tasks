---
title: Comment se préparer aux entretiens React – Guide technique pour les entretiens
  front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-08T00:29:16.000Z'
originalURL: https://freecodecamp.org/news/prepare-for-react-technical-interviews
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Build-a-React-Code-Editor-That-Compiles-and-Executes-in-10--Languages--2-.png
tags:
- name: coding interview
  slug: coding-interview
- name: Front-end Development
  slug: front-end-development
- name: interview questions
  slug: interview-questions
- name: Interviewing
  slug: interviewing
- name: React
  slug: react
seo_title: Comment se préparer aux entretiens React – Guide technique pour les entretiens
  front-end
seo_desc: "By Manu Arora\nA front-end technical interview is an opportunity for a\
  \ potential employer to assess your skills and knowledge in web development.  \n\
  The interviewer will ask you questions about your experience and skills in HTML,\
  \ CSS, and JavaScript. T..."
---

Par Manu Arora

Un entretien technique pour un poste de développeur front-end est une opportunité pour un employeur potentiel d'évaluer vos compétences et connaissances en développement web. 
  
L'intervieweur vous posera des questions sur votre expérience et vos compétences en HTML, CSS et JavaScript. Il vous posera probablement également des questions spécifiques sur des frameworks comme React, Angular, Vue, ou tout autre framework qu'ils utilisent. 
  
Ils peuvent également vous donner un défi de codage pour tester vos capacités dans un domaine particulier. 
  
Aujourd'hui, nous allons examiner les problèmes les plus courants posés lors d'un entretien technique pour un poste de développeur front-end, en nous concentrant sur React et JavaScript.

## Ce que les intervieweurs recherchent

Lors d'un entretien pour un poste de développeur web front-end, soyez prêt à discuter de vos compétences et de votre expérience avec divers langages de programmation, outils et frameworks. 
  
Les intervieweurs voudront également voir que vous avez une bonne compréhension des dernières tendances et technologies en matière de développement web. 
  
Soyez prêt à parler de vos projets passés et de la manière dont vous avez abordé la résolution de divers défis. 
  
Assurez-vous de mettre en avant vos compétences en résolution de problèmes en discutant de la manière dont vous avez relevé divers défis lors de votre processus de développement. 
  
Enfin, n'oubliez pas de mettre en avant vos points forts.

## Questions les plus fréquemment posées lors d'un entretien technique pour un poste de développeur front-end

Les problèmes posés lors d'un entretien technique pour un poste de développeur front-end sont assez simples et courants. Si vous avez codé activement pendant au moins 6 mois, vous serez familier avec la plupart des concepts abordés.

Une fois que vous aurez pratiqué les bonnes questions avec une approche basée sur le temps, vous devriez être en mesure de réussir les entretiens.

Examinons les questions les plus courantes.

## Map, ForEach, Filter et Reduce

Les questions les plus fréquemment posées (généralement au début des entretiens) concernent les `méthodes de tableau`. L'intervieweur veut évaluer votre aisance avec la manipulation de tableaux.

#### La méthode `.map()`

La méthode `.map()` parcourt un tableau, exécute la logique que vous écrivez à l'intérieur du corps de map, et retourne un **NOUVEAU** tableau.

```javascript
let arr = [
  { id: 1, age: 12, name: 'Manu' },
  { id: 2, age: 24, name: 'Quincy' },
  { id: 3, age: 22, name: 'Abbey' },
]

let names = arr.map((el) => el.name)
console.log(names)
// Sortie: [ 'Manu', 'Quincy', 'Abbey' ]
```

#### La méthode `.forEach()`

ForEach est similaire à `.map()` mais il NE RETOURNE PAS de tableau.

```javascript
let arr = [
  { id: 1, age: 12, name: 'Manu' },
  { id: 2, age: 24, name: 'Quincy' },
  { id: 3, age: 22, name: 'Abbey' },
]

arr.forEach((el) => el.age += 10);
console.log(arr);

// Sortie: 22 32 44
```

#### La méthode `.filter()`

La méthode filter, comme son nom l'indique, aide à filtrer les valeurs à l'intérieur d'un tableau en fonction d'une condition booléenne. 

Si la condition booléenne est vraie, le résultat sera retourné et ajouté dans le tableau final. Sinon, il sera ignoré. Filter retourne également un tableau, tout comme la méthode `.map()`.

```javascript
let arr = [
  { id: 1, age: 12, name: 'Manu' },
  { id: 2, age: 24, name: 'Quincy' },
  { id: 3, age: 22, name: 'Abbey' },
]

let tooYoung = arr.filter((el) => el.age <= 14);
console.log(tooYoung);

// Sortie: [ { id: 1, age: 12, name: 'Manu' } ]
```

#### La méthode `.reduce()`

En termes simples, la méthode `.reduce()` prend en compte une `valeur précédente`, une valeur actuelle et un `accumulateur`. 

Le type de retour de la méthode `.reduce()` est toujours une seule valeur. Elle est utile lorsque vous souhaitez traiter toutes les valeurs du tableau et vouloir obtenir un résultat accumulé.

```javascript
// Calcule l'âge total des trois personnes.
let arr = [
  { id: 1, age: 12, name: 'Manu' },
  { id: 2, age: 24, name: 'Quincy' },
  { id: 3, age: 22, name: 'Abbey' },
]

let totalAge = arr.reduce((acc, currentObj) => acc + currentObj.age, 0)
console.log(totalAge)

// Sortie: 57
```

Ici, `currentObj` est l'objet qui est parcouru. De plus, la valeur `acc` stocke le résultat et est finalement sortie dans le tableau totalAge.

## Comment implémenter des Polyfills

Une autre question importante d'entretien est [Comment implémenter des polyfills](https://www.algochurn.com/frontend/polyfills) des méthodes de tableau map et filter.

Un polyfill est un extrait de code (en termes d'architecture web JavaScript) utilisé pour les fonctionnalités du monde moderne sur les anciens navigateurs qui ne l'implémentent pas nativement.

En termes simples, un polyfill est une implémentation personnalisée des fonctions JavaScript natives. Une sorte de création de votre propre méthode `.map()` ou `.filter()`.

#### Comment utiliser le polyfill `.map()`

```javascript
let data = [1, 2, 3, 4, 5];

Array.prototype.myMap = function (cb) {
  let arr = [];
  for (let i = 0; i < this.length; i++) {
    arr.push(cb(this[i], i, this));
  }
  return arr;
};
const mapLog = data.myMap((el) => el * 2);
console.log(mapLog);
```

La méthode `myMap` prend un `callback` qui est exécuté à l'intérieur du corps de `myMap`. Nous avons essentiellement une boucle `for` native à l'intérieur du corps de myMap, qui parcourt `this.length`. Ce n'est rien d'autre que la longueur du tableau à travers lequel la fonction `myMap` est appelée.

Puisque la syntaxe de `map()` est `arr.map(currentElement, index, array)`, et que la fonction `myMap()` prend en compte exactement cela.

De plus, puisque `map()` retourne un nouveau tableau, nous créons un tableau vide et y poussons les résultats. À la fin, nous le retournons.

#### Comment utiliser le polyfill `.filter()`

```javascript
let data = [1, 2, 3, 4, 5];

Array.prototype.myFilter = function (cb) {
  let arr = [];
  for (let i = 0; i < this.length; i++) {
    if (cb(this[i], i, this)) {
      arr.push(this[i]);
    }
  }
  return arr;
};
const filterLog = data.myFilter((el) => el < 4);
console.log(filterLog);
```

`.filter()` est très similaire à `.map()` en termes d'implémentation. Mais puisque `filter` filtre les résultats en fonction d'une valeur booléenne, nous avons une condition `if()` supplémentaire pour filtrer les résultats et les pousser conditionnellement à l'intérieur du tableau.

## Qu'est-ce que le Debouncing ?

C'est une question d'entretien célèbre avec beaucoup d'utilisations et d'implémentations pratiques dans le monde réel.

Le `Debouncing` est une méthode pour empêcher une fonction d'être invoquée trop souvent, et au lieu de cela, attendre un certain temps jusqu'à ce qu'elle soit appelée pour la dernière fois avant de l'invoquer. 
  
Prenez l'exemple d'Amazon. Chaque fois que vous tapez quelque chose dans la barre de recherche, lorsque vous vous arrêtez pendant AU MOINS 0,5 seconde, les résultats sont alors récupérés. C'est exactement ce qu'est le debouncing.

Afin d'implémenter le debouncing, prenons un exemple : générer un nom d'utilisateur pour un utilisateur en fonction de l'entrée de l'utilisateur.

<iframe src="https://codesandbox.io/embed/proud-surf-uiu2v?fontsize=14&hidenavigation=1&theme=dark"
     style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;"
     title="proud-surf-uiu2v"
     allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking"
     sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"
   ></iframe>

```javascript
import "./styles.css";
let inputEle = document.getElementById("inputElement");
let username = document.getElementById("username");

let generateUsername = (e) => {
  username.innerHTML = e.target.value.split(" ").join("-");
};
let debounce = function (cb, delay) {
  let timer;
  return function () {
    let context = this;
    clearTimeout(timer);
    timer = setTimeout(() => {
      cb.apply(context, arguments);
    }, delay);
  };
};

inputEle.addEventListener("keyup", debounce(generateUsername, 300));
```

Ici, nous essayons de créer un nom d'utilisateur personnalisé basé sur l'entrée de l'utilisateur. Maintenant, si l'utilisateur commence à taper, nous ne voulons pas le créer immédiatement, mais plutôt attendre 300 millisecondes avant de créer le nom d'utilisateur. Nous essayons de simuler un appel API ici, alors supposez que l'utilisateur tape quelque chose et qu'il doit faire un appel API au backend et récupérer une réponse.

La fonction `debounce()` prend deux valeurs, `cb` et `delay`. `cb` est la fonction de rappel qui est exécutée lorsque le minuteur expire. 
  
Nous utilisons `setTimeout()` pour créer un minuteur de délai, ce qui signifie que la fonction à l'intérieur du corps de setTimeout sera exécutée après un certain temps.

La méthode `apply` est utilisée pour appeler la fonction de rappel avec l'`objet` avec lequel elle a été initialement appelée, en appliquant les arguments et le contexte à celle-ci.

## Qu'est-ce que les Closures ?

Selon la [documentation mdn pour les closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures),

> Une closure est la combinaison d'une fonction regroupée (enclose) avec des références à son état environnant (l'environnement lexical). En d'autres termes, une closure vous donne accès à la portée d'une fonction externe depuis une fonction interne. En JavaScript, les closures sont créées chaque fois qu'une fonction est créée, au moment de la création de la fonction.

Pour simplifier cela, prenons un exemple et comprenons comment fonctionnent les closures.

```javascript
function start() {
  var name = "Manu"; // name est une variable locale créée par start()
  function displayName() {
    // displayName() est la fonction interne, une `closure`
    alert(name); // utilise la variable déclarée dans la fonction parente
  }
  displayName();
}
start(); // "Manu" boîte d'alerte affichée
```

Ici, une closure est formée entre la fonction `start()` et la fonction `displayName()`. La fonction `displayName()` a accès à la variable `name` présente dans la fonction `start()`.

En termes simples, la fonction interne connaît son environnement (l'environnement lexical).

J'ai écrit un blog entier sur [comment réussir les entretiens JavaScript](https://manuarora.in/blog/ace-the-javascript-interview#closures). Jetez un coup d'œil si vous voulez en savoir plus sur le processus d'entretien JavaScript en profondeur.

## React Hooks

Les questions les plus populaires posées lors d'un entretien de codage pour un poste de développeur front-end en ce qui concerne les hooks React sont :

1. `useState()`
2. `useReducer()`
3. `useEffect()`
4. `useRef()`
5. Hooks personnalisés et leur implémentation.

### Comment fonctionne le hook `useState()`

Pour gérer un état à l'intérieur de votre composant, le hook `useState()` est votre hook de prédilection. 
  
Prenons un exemple et comprenons :

<iframe src="https://codesandbox.io/embed/thirsty-lewin-uo8ylh?fontsize=14&hidenavigation=1&theme=dark"
     style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;"
     title="thirsty-lewin-uo8ylh"
     allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking"
     sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"
   ></iframe>

```javscript
import { useState } from "react";
import "./styles.css";

export default function App() {
  const [title, setTitle] = useState("freeCodeCamp");
  const handleChange = () => {
    setTitle("FCC");
  };
  return (
    <div className="App">
      <h1>{title} useState</h1>
      <button onClick={handleChange}>Change Title</button>
    </div>
  );
}

```

La méthode `useState()` nous donne deux valeurs, la variable `state` et `une fonction pour changer` cette variable d'état.

Dans l'extrait de code ci-dessus, nous créons un état `title` pour stocker le titre de la page. L'état initial est passé comme `freeCodeCamp`.

Au clic sur le bouton, nous pouvons utiliser la méthode `setTitle()` pour changer la variable d'état en `FCC`.

La méthode `useState()` est votre ressource de prédilection pour la gestion d'état dans un composant fonctionnel.

### Comment fonctionne le hook `useReducer()`

En termes simples, `useReducer()` est la manière cool de gérer l'état dans votre application. Il est plus structuré et vous aide à maintenir un état complexe dans votre application.

Prenons un exemple pour comprendre le hook useReducer :

<iframe src="https://codesandbox.io/embed/ecstatic-marco-o8wh00?fontsize=14&hidenavigation=1&theme=dark"
     style="width:100%; height:500px; border:0; border-radius: 4px; overflow:hidden;"
     title="ecstatic-marco-o8wh00"
     allow="accelerometer; ambient-light-sensor; camera; encrypted-media; geolocation; gyroscope; hid; microphone; midi; payment; usb; vr; xr-spatial-tracking"
     sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"
   ></iframe>

```javscript
import "./styles.css";
import { useReducer } from "react";

const initialState = { title: "freeCodeCamp", count: 0 };

function reducer(state, action) {
  switch (action.type) {
    case "change-title":
      return { ...state, title: "FCC" };
    case "increment-counter":
      return { ...state, count: state.count + 1 };
    default:
      throw new Error();
  }
}

export default function App() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      <div className="App">
        <h1>{state.title} CodeSandbox</h1>
        <button onClick={() => dispatch({ type: "change-title" })}>
          Change Title
        </button>
        <button onClick={() => dispatch({ type: "increment-counter" })}>
          Increment Counter
        </button>
      </div>
      <p style={{ textAlign: "center" }}>{state.count}</p>.
    </>
  );
}

```

Le hook `useReducer()` prend deux paramètres, la fonction `reducer` et une valeur `initialState`. 
  
La fonction reducer est une implémentation basée sur `switch-case` qui retourne la valeur d'état finale que `useReducer()` utilise en interne pour fournir au composant.

Les valeurs retournées par la fonction `useReducer()` sont `state` et `dispatch`. Le `state` est la valeur d'`état` réelle qui peut être utilisée à l'intérieur du composant. Dans notre cas, l'état a deux valeurs : `title et count`. Ce titre et ce compte peuvent être manipulés en utilisant la méthode `dispatch()` qui est retournée par la méthode `useReducer()`.

Dans le cas ci-dessus, pour changer le titre, nous avons écrit un cas de `change-title` à l'intérieur de la fonction reducer. Cela peut être déclenché à l'aide de la fonction `dispatch({ type: "change-title" })`. Cela déclenchera la fonction de changement de titre et changera l'état de l'attribut `title`. 
  
De même, la même chose se produit pour la partie `count` qui est présente dans l'application. 
  
Comme je l'ai dit plus tôt, c'est une manière cool d'implémenter l'état à l'intérieur de votre application. 😉

### Comment fonctionne le hook `useEffect()`

Pensez-y de cette manière : si vous voulez avoir un `effet secondaire` à une variable d'état qui change, vous pouvez utiliser le hook `useEffect()` pour le déclencher. 
  
Par exemple, disons que si la `valeur d'entrée` de votre boîte d'entrée change, et que vous voulez appeler une API après qu'elle ait changé. Vous pouvez écrire la logique du `gestionnaire d'API` dans le bloc `useEffect()`.

```javascript
import React, {useState, useEffect} from 'react';

export const App = () => {
    const [value, setValue] = useState('');
    useEffect(() => {
      console.log('value changed: ', value);
    }, [value])
	return <div>
        	<input type="text" name="username" value={value} onChange={(e) => setValue(e.target.value)} />
        </div>
}
```

Ici, nous avons une `boîte d'entrée` qui a une valeur d'état de `value` attachée à celle-ci. Cette valeur changera lorsque l'utilisateur essaiera d'entrer quelque chose. 
  
Une fois que la valeur a été mise à jour et a été rendue, le bloc `useEffect()` entrera en jeu et l'instruction `console` sera déclenchée, sortant la dernière valeur d'état qui est présente. 
  
Ici, un bon cas d'utilisation de `useEffect()` peut être d'implémenter des `appels API`. Supposons que vous voulez appeler une API avec la valeur du champ d'entrée. Le bloc de fonction useEffect sera la meilleure façon de le faire.

Une autre partie de cela est le `tableau de dépendances` qui est le deuxième argument du hook `useEffect()`. Dans notre cas, nous avons mentionné `[value]` comme deuxième argument.

Cela signifie essentiellement que CHAQUE FOIS QUE LA `value` CHANGE, la fonction à l'intérieur de useEffect est déclenchée. Si vous ne passez rien dans le `tableau de dépendances`, le bloc de fonction est déclenché une fois.

### Comment fonctionne le hook `useRef()`

Le hook useRef nous donne la capacité de muter le DOM (mais ce n'est pas la seule implication de useRef).

Selon la documentation :

> useRef retourne un objet ref mutable dont la propriété .current est initialisée à l'argument passé (initialValue). L'objet retourné persistera pour toute la durée de vie du composant.

En termes simples, nous allons utiliser useRef si nous voulons persister la valeur de quelque chose pour tout le cycle de vie du composant. L'implémentation de base de useRef vient avec les éléments DOM. Prenons un exemple :

```javascript
function TextInputWithFocusButton() {
  const inputEl = useRef(null);
  const onButtonClick = () => {
    // `current` pointe vers l'élément de texte monté
    inputEl.current.focus();
  };
  return (
    <>
      <input ref={inputEl} type="text" />
      <button onClick={onButtonClick}>Focus the input</button>
    </>
  );
}
```

Ici, nous attribuons une propriété `ref` au bloc `input`. Cela sera associé à la référence `inputEl` que nous avons créée.

Maintenant, cet élément `input` peut être manipulé comme nous le souhaitons. Nous pouvons modifier l'attribut `style` et le rendre beau, nous pouvons prendre la propriété `value` pour voir ce qui est retenu par l'élément d'entrée comme valeur, et ainsi de suite.

Dans l'exemple ci-dessus, lorsque nous cliquons sur le bouton, l'`input` est mis au point et nous pouvons immédiatement commencer à taper. Nous pouvons faire cela avec l'aide de `inputEl.current.focus()` – essentiellement la méthode `focus()` présente sur l'objet `current`.

### Qu'est-ce que les hooks personnalisés ?

L'une des questions les plus fréquemment posées que j'ai vues lors des entretiens pour un poste de développeur front-end est de [créer un hook personnalisé pour les événements de clavier](https://www.algochurn.com/frontend/usekeypress-custom-hook).

Nous avons vu de nombreux hooks différents, mais l'intervieweur pourrait vous demander de créer un hook vous-même. Cela pourrait être un défi pour certains, mais avec un peu de pratique, cela devient beaucoup plus facile.

Comprenons ce qu'est un `Hook` :

L'utilisation de base d'un hook personnalisé est d'extraire la logique d'une fonction dans son propre composant.

Imaginez ce qui se passera si vous devez `écouter une pression sur la touche Entrée` à l'intérieur de chacun de vos composants. Au lieu d'écrire la logique pour `écouter` encore et encore, nous pouvons extraire la logique dans un composant à part et l'utiliser où nous voulons (juste comme nous utilisons `useState()` ou `useEffect()`).

Il y a quelques conditions pour qu'une fonction soit appelée un `Hook` :

1. Elle doit toujours commencer par le mot-clé `use`.
2. Nous pouvons décider de ce qu'elle prend comme arguments, et de ce qu'elle doit retourner, le cas échéant.

```javascript
// Hook personnalisé : useAvailable
function useAvailabe(resource) {
  const [isAvailable, setIsAvailable] = useState(null);

  // ...

  return isAvailable;
}

// Utilisation :
  const isAvailable = useAvailable(cpu);

```

Ici, peu importe combien de fois nous appelons `useState` et `useEffects` à l'intérieur du hook personnalisé, ils seront complètement indépendants de la fonction où nous utilisons le hook personnalisé. 
  
Prenons un exemple de création d'un hook personnalisé pour `stocker des valeurs dans le stockage local`.

### Comment créer un hook personnalisé – exemple useLocalStorage

Le hook personnalisé useLocalStorage est un moyen de persister des données dans le stockage local. Obtenez et définissez des valeurs à l'intérieur du stockage local en utilisant des paires `clé` et `valeur` afin que chaque fois que l'utilisateur revient à votre application web, il voit le même résultat qu'il a utilisé précédemment.

L'implémentation ci-dessous est celle d'une simple valeur de balise `select` qui, une fois modifiée, persiste les données dans le stockage local.

`useLocalStorage.js`

```javascript
// Utilisation du hook personnalisé Local Storage
import { useState } from 'react';

function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    if (typeof window === 'undefined') {
      return initialValue;
    }
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.log(error);
      return initialValue;
    }
  });
  const setValue = (value) => {
    try {
      const valueToStore =
        value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      if (typeof window !== 'undefined') {
        window.localStorage.setItem(key, JSON.stringify(valueToStore));
      }
    } catch (error) {
      console.log(error);
    }
  };
  return [storedValue, setValue] as const;
}

export default useLocalStorage;

```

`App.js`

```javascript
import * as React from 'react';
import './style.css';
import useLocalStorage from './useLocalStorate';

export default function App() {
  const [storedValue, setStoredValue] = useLocalStorage(
    'select-value',
    'light'
  );

  return (
    <div>
      <select
        className="select"
        value={storedValue}
        onChange={(e) => setStoredValue(e.target.value)}
      >
        <option value="dark">Dark</option>
        <option value="light">Light</option>
      </select>
      <p className="desc">
        Valeur du stockage local : <span>{storedValue}</span>
      </p>
    </div>
  );
}
```

Ici, le hook `useLocalStorage` prend deux paramètres, le `nom de la clé de stockage local` à stocker, et une valeur `par défaut` qui doit être présente.

Le hook retourne deux valeurs : la `valeur de stockage local` de la clé que vous utilisez et un moyen de `changer cette valeur de clé` en nous donnant une `méthode de définition`. Dans ce cas, la méthode `setStoredValue`.

Dans le fichier `useLocalStorage.js`, nous essayons d'abord d'`OBTENIR` la valeur de stockage local avec cette clé en utilisant la méthode `localStorage.getItem()`. Si cela existe, nous définissons la valeur. Si elle est trouvée, nous `JSON.parse()` la valeur et la retournons. Sinon, la valeur initiale fournie est définie comme valeur par défaut. 
  
La fonction `setLocalStorage()` prend en compte si la valeur passée est une fonction ou une simple valeur de variable. Elle prend également en charge la définition de la valeur du stockage local en utilisant la fonction `localStorage.setItem()`.

## Comment se démarquer en tant que développeur en créant des projets parallèles

Ce qui a toujours fonctionné pour moi et m'a aidé à me démarquer, ce sont mes projets parallèles que j'ai construits. 
  
À mon avis, vous n'avez pas besoin de construire 10 projets parallèles basiques et standardisés. Essayez plutôt de construire un ou deux projets vraiment bons où vous pouvez implémenter tous les concepts de React/HTML/CSS/JavaScript et tout ce que vous avez appris. 
  
Supposons que l'intervieweur ait 14 entretiens dans une semaine et doive examiner les CV de 14 candidats. Ils seront plus intéressés par votre profil parce que vous avez créé un `site web de raccourcissement de liens qui facture 1 $ après chaque 1000 visites de liens` plutôt qu'un clone d'Amazon / Netflix.

Encore une fois, il n'y a rien de mal à créer des clones et à pratiquer vos compétences. Mais il est toujours bon d'avoir au moins 1 projet unique qui vous aide à vous démarquer de la foule. 
  
De plus, la création de projets parallèles vous aidera à monter en compétences en tant que développeur. Il n'est pas probablement possible de tout savoir à l'avance lorsque vous créez un projet à partir de zéro. En cours de route, vous devrez apprendre de nombreuses compétences différentes et vous améliorer dans celles-ci.

## Pratique, Pratique, Pratique.

Il y a un célèbre dicton qui dit :

%[https://twitter.com/mannupaaji/status/1566350128767987712]

et cela est vrai dans une large mesure. 

Moi-même, j'ai échoué des centaines de fois avant de décrocher mon premier emploi. C'est le feedback constant et les itérations que vous devez faire pour obtenir ce que vous voulez. 

Dans notre cas, obtenir un emploi en développement front-end devient facile lorsque :

* Vous avez une connaissance approfondie de vos compétences – React dans ce cas (ainsi que HTML, CSS et JS).
* Vous avez un ensemble de projets à présenter, ce qui vous permet de vous démarquer.
* Vous êtes prêt à consacrer du temps et des efforts pour apprendre davantage et vous challenger.
* Vous lisez régulièrement le blog de freeCodeCamp et pratiquez les questions qui y sont posées (😉)

## **Conclusion**

Il y a beaucoup de questions à pratiquer pour un tour de codage en machine. L'intervieweur peut poser différents ensembles de questions pour tester vos compétences. 
  
Vous pouvez utiliser [**Algochurn**](https://algochurn.com) pour pratiquer les questions d'entretien [JavaScript](https://www.algochurn.com/blog/top-5-react-front-end-questions-to-practice-before-a-technical-interview-round) les plus populaires, les [questions d'entretien React](https://algochurn.com/frontend), et les [questions algorithmiques](https://algochurn.com/problems) posées lors d'un entretien technique pour un poste de développeur front-end, ainsi que leurs solutions et approches.

Si vous avez des questions, n'hésitez pas à me contacter via [Twitter(@mannupaaji)](https://twitter.com/mannupaaji) et/ou mon [site web(manuarora.in)](https://manuarora.in)

Bonne chance et bon codage ! 👕🧑💻