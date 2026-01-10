---
title: React Hooks pour Débutants - Un Guide Simple sur useState et useEffect
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-06-02T14:53:21.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-using-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/beginners-guide-to-hooks.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
seo_title: React Hooks pour Débutants - Un Guide Simple sur useState et useEffect
seo_desc: '"What the heck are hooks?"

  I found myself asking this just as I thought I had covered all the basis of React.
  Such is the life of a frontend developer, the game is always changing. Enter Hooks.

  It''s always nice to learn something new right? Of course...'
---

"Mais qu'est-ce que les hooks ?"

Je me suis posé cette question alors que je pensais avoir couvert toutes les bases de React. Tel est le quotidien d'un développeur frontend, le jeu change constamment. Entrez les Hooks.

C'est toujours agréable d'apprendre quelque chose de nouveau, n'est-ce pas ? Bien sûr ! Mais parfois, nous devons nous demander "Pourquoi ? Quel est l'intérêt de cette nouvelle chose ? Dois-je l'apprendre ?"

Avec les hooks, la réponse est "pas tout de suite". Si vous avez appris React et que vous avez utilisé des composants basés sur des classes jusqu'à présent, il n'y a pas de précipitation à passer aux hooks. Les hooks sont optionnels et peuvent fonctionner en tandem avec vos composants existants. Vous détestez quand vous devez réécrire toute votre base de code pour faire fonctionner une nouvelle chose, n'est-ce pas ?

Quoi qu'il en soit, voici quelques raisons pour lesquelles les hooks ont été introduits en premier lieu et pourquoi je recommande aux débutants de les apprendre.

## Utilisation de l'état dans les composants fonctionnels

Avant les hooks, nous ne pouvions pas utiliser l'état dans les composants fonctionnels. Cela signifie que si vous avez un composant fonctionnel bien conçu et testé qui doit soudainement stocker un état, vous êtes coincé avec la tâche douloureuse de refactoriser votre composant fonctionnel en un composant de classe. 

Hourra ! Permettre l'état dans les composants fonctionnels signifie que nous n'avons pas à refactoriser nos composants de présentation [Consultez cet article pour plus d'informations](https://scotch.io/courses/5-essential-react-concepts-to-know-before-learning-redux/presentational-and-container-component-pattern-in-react).

## Les composants de classe sont encombrants

Admettons-le, les composants de classe viennent avec beaucoup de code boilerplate. Constructeurs, binding, utilisation de "this" partout. L'utilisation de composants fonctionnels élimine beaucoup de cela, ce qui rend notre code plus facile à suivre et à maintenir.

Vous pouvez en lire plus à ce sujet [dans la documentation React :](https://reactjs.org/docs/hooks-intro.html#classes-confuse-both-people-and-machines)

## Code plus lisible

Puisque les hooks nous permettent d'utiliser des composants fonctionnels, cela signifie qu'il y a moins de code par rapport aux composants de classe. Cela rend notre code plus lisible. Enfin, c'est l'idée. 

Nous n'avons pas à nous soucier de la liaison de nos fonctions, ou de nous rappeler à quoi "this" se rapporte, et ainsi de suite. Nous pouvons nous concentrer sur l'écriture de notre code.

> [Si vous débutez avec React, j'ai une série de publications pour commencer sur mon blog qui pourraient vous aider ! Consultez-le ici :](https://www.jschris.com)


## React State Hook

Ah, l'état. Un pilier de l'écosystème React. Commençons avec les Hooks en introduisant le hook le plus courant avec lequel vous allez travailler - `useState()`.

Examinons un composant de classe qui a un état.

```jsx

import React, { Component } from 'react';
import './styles.css';

class Counter extends Component {
	state = {
		count: this.props.initialValue,
	};

	setCount = () => {
		this.setState({ count: this.state.count + 1 });
	};

	render() {
		return (
			<div>
				<h2>Ceci est un compteur utilisant une classe</h2>
				<h1>{this.state.count}</h1>

				<button onClick={this.setCount}>Cliquez pour Incrémenter</button>
			</div>
		);
	}
}

export default Counter;

```

Avec React Hooks, nous pouvons réécrire ce composant et supprimer beaucoup de choses, le rendant plus facile à comprendre :

```jsx

import React, { useState } from 'react';

function CounterWithHooks(props) {
	const [count, setCount] = useState(props.initialValue);

	return (
		<div>
			<h2>Ceci est un compteur utilisant des hooks</h2>
			<h1>{count}</h1>
			<button onClick={() => setCount(count + 1)}>Cliquez pour Incrémenter</button>
		</div>
	);
}

export default CounterWithHooks;

```

À première vue, il y a moins de code, mais que se passe-t-il ?


### Syntaxe de l'État React


Nous avons vu notre premier hook ! Hourra !

```jsx
 const [count, setCount] = useState();
```

En gros, cela utilise l'affectation par déstructuration pour les tableaux. La fonction `useState()` nous donne 2 choses : 

- **une variable pour contenir la valeur de l'état**, dans ce cas, elle s'appelle `count` - **une fonction pour changer la valeur**, dans ce cas, elle s'appelle `setCount`.

Vous pouvez les nommer comme vous voulez :

```jsx

const [myCount, setCount] = useState(0);

```

Et vous pouvez les utiliser dans tout le code comme des variables/fonctions normales :

```jsx

function CounterWithHooks() {
	const [count, setCount] = useState();

	return (
		<div>
			<h2>Ceci est un compteur utilisant des hooks</h2>
			<h1>{count}</h1>
			<button onClick={() => setCount(count + 1)}>Cliquez pour Incrémenter</button>
		</div>
	);
}

```

Remarquez le hook `useState` en haut. Nous déclarons/destructurons 2 choses :

- `counter` : une valeur qui contiendra notre valeur d'état
- `setCounter` : une fonction qui changera notre variable `counter`

Alors que nous continuons à travers le code, vous verrez cette ligne :

```jsx

<h1>{count}</h1>

```

Ceci est un exemple de la façon dont nous pouvons utiliser une variable de hook d'état. Dans notre JSX, nous plaçons notre variable `count` dans `{}` pour l'exécuter en tant que JavaScript, et à son tour la valeur `count` est rendue sur la page. 

En comparant cela à l'ancienne méthode "basée sur les classes" d'utilisation d'une variable d'état :

```jsx

<h1>{this.state.count}</h1>

```

Vous remarquerez que nous n'avons plus besoin de nous soucier d'utiliser `this`, ce qui facilite beaucoup notre vie - par exemple, l'éditeur VS Code nous donnera un avertissement si `{count}` n'est pas défini, nous permettant de détecter les erreurs tôt. Alors qu'il ne saura pas si `{this.state.count}` est indéfini jusqu'à ce que le code soit exécuté.

Passons à la ligne suivante !

```jsx

 <button onClick={() => setCount(count + 1)}>Cliquez pour Incrémenter</button>

```

Ici, nous utilisons la fonction `setCount` (rappelons que nous l'avons destructurée/déclarée à partir du hook `useState()`) pour changer la variable `count`.

Lorsque le bouton est cliqué, nous mettons à jour la variable `count` de `1`. Puisque cela représente un changement d'état, cela déclenche un nouveau rendu, et React met à jour la vue avec la nouvelle valeur `count` pour nous. Super !

### Comment puis-je définir l'état initial ?

Vous pouvez définir l'état initial en passant un argument à la syntaxe `useState()`. Cela peut être une valeur codée en dur :

```jsx

 const [count, setCount] = useState(0);

```

Ou peut être pris à partir des props :

```jsx

 const [count, setCount] = useState(props.initialValue);

```

Cela définirait la valeur `count` à celle de `props.initialValue`.

Cela résume `useState()`. La beauté de cela est que vous pouvez utiliser des variables/fonctions d'état comme n'importe quelle autre variable/fonction que vous écriviez vous-même.

### Comment gérer plusieurs variables d'état ?

C'est une autre chose cool à propos des hooks. Nous pouvons en avoir autant que nous le souhaitons dans un composant :

```jsx

 const [count, setCount] = useState(props.initialValue);
 const [title, setTitle] = useState("Ceci est mon titre");
 const [age, setAge] = useState(25);

```

Comme vous pouvez le voir, nous avons 3 objets d'état séparés. Si nous voulons mettre à jour l'âge par exemple, nous appelons simplement la fonction **setAge()**. La même chose avec **count** et **title**. Nous ne sommes plus liés à l'ancienne méthode encombrante des composants de classe où nous avons un objet d'état massif stocké en utilisant **setState()** :

```jsx

this.setState({ count: props.initialValue, title: "Ceci est mon titre", age: 25 })

```


## Alors, qu'en est-il de la mise à jour des choses lorsque les props ou l'état changent ?

Lorsque nous utilisons des hooks et des composants fonctionnels, nous n'avons plus accès aux méthodes de cycle de vie de React comme `componentDidMount`, `componentDidUpdate`, et ainsi de suite. Oh, là là ! Ne paniquez pas mon ami, React nous a donné un autre hook que nous pouvons utiliser :

* _Roulement de tambour_ * 

## Entrez useEffect !

Le hook Effect (**useEffect()**) est l'endroit où nous plaçons les "effets secondaires".

Eh, effets secondaires ? Qu'est-ce que c'est ? Faisons une pause et discutons de ce qu'est réellement un effet secondaire. Cela nous aidera à comprendre ce que fait `useEffect()`, et pourquoi il est utile.

Une explication ennuyeuse et informatique serait.

> "En programmation, un effet secondaire est lorsqu'une procédure change une variable en dehors de sa portée"

En termes React, cela signifie "quand les variables ou l'état d'un composant changent en fonction d'une chose externe". Par exemple, cela pourrait être :

- Lorsqu'un composant reçoit de nouvelles props qui changent son état
- Lorsqu'un composant fait un appel API et fait quelque chose avec la réponse (par exemple, change l'état)

Alors pourquoi cela s'appelle-t-il un effet secondaire ? Eh bien, *nous ne pouvons pas être sûrs du résultat de l'action*. Nous ne pouvons jamais être certains à 100 % des props que nous allons recevoir, ou de la réponse d'un appel API. Et, nous ne pouvons pas être sûrs de la manière dont cela affectera notre composant. 

Bien sûr, nous pouvons écrire du code pour valider, et gérer les erreurs, et ainsi de suite, mais en fin de compte, nous ne pouvons pas être sûrs des effets secondaires de ces choses. 

Donc, par exemple, lorsque nous changeons l'état, en fonction d'une *chose externe*, cela est connu comme un effet secondaire.

Cela étant dit, revenons à React et au hook useEffect !

Lorsque nous utilisons des composants fonctionnels, nous n'avons plus accès aux méthodes de cycle de vie comme `componentDidMount()`, `componentDidUpdate()`, etc. Donc, en effet (jeu de mots intended), les hooks useEffect remplacent les hooks actuels du cycle de vie de React.

Comparons un composant basé sur une classe avec la façon dont nous utilisons le hook useEffect :

```jsx
import React, { Component } from 'react';

class App extends Component {
	componentDidMount() {
		console.log('Je viens de monter !');
	}

	render() {
		return <div>Insérez du JSX ici</div>;
	}
}
```

Et maintenant en utilisant useEffect() :

```jsx
function App() {
	useEffect(() => {
		console.log('Je viens de monter !');
	});

	return <div>Insérez du JSX ici</div>;
}
```

Avant de continuer, il est important de savoir que, par défaut, **le hook useEffect s'exécute à chaque rendu et re-rendu**. Donc, chaque fois que l'état change dans votre composant ou que votre composant reçoit de nouvelles props, il se re-rendra et provoquera l'exécution du hook useEffect à nouveau.

### Exécuter un effet une seule fois (componentDidMount)

Donc, si les hooks s'exécutent chaque fois qu'un composant se rend, comment pouvons-nous nous assurer qu'un hook ne s'exécute qu'une seule fois lorsque le composant est monté ? Par exemple, si un composant récupère des données à partir d'une API, nous ne voulons pas que cela se produise chaque fois que le composant se re-rend !

Le hook `useEffect()` prend un deuxième paramètre, un tableau, **contenant la liste des choses qui provoqueront l'exécution du hook useEffect**. Lorsqu'elles sont modifiées, elles déclencheront le hook d'effet. La clé pour exécuter un effet une seule fois est de passer un tableau vide :

```jsx
useEffect(() => {
	console.log('Cela ne s'exécute qu'une seule fois');
}, []);
```

Donc, cela signifie que le hook useEffect s'exécutera lors du premier rendu comme d'habitude. Cependant, lorsque votre composant se re-rend, le useEffect pensera "bien, je me suis déjà exécuté, il n'y a rien dans le tableau, donc je n'aurai pas à m'exécuter à nouveau. Retour au sommeil pour moi !" et ne fera simplement rien.

> En résumé, tableau vide = le hook `useEffect` s'exécute une fois au montage

### Utilisation des effets lorsque les choses changent (componentDidUpdate)

Nous avons couvert comment nous assurer qu'un hook `useEffect` ne s'exécute qu'une seule fois, mais qu'en est-il lorsque notre composant reçoit une nouvelle prop ? Ou lorsque nous voulons exécuter du code lorsque l'état change ? Les hooks nous permettent également de faire cela !

```jsx
 useEffect(() => {
	console.log("La prop name a changé !")
 }, [props.name]);
```

Remarquez comment nous passons des éléments au tableau useEffect cette fois, à savoir _props.name_. 

Dans ce scénario, le hook useEffect s'exécutera au premier chargement comme toujours. Chaque fois que votre composant reçoit une nouvelle **prop name** de son parent, le hook useEffect sera déclenché, et le code qu'il contient s'exécutera.

Nous pouvons faire la même chose avec les variables d'état :

```jsx
const [name, setName] = useState("Chris");

 useEffect(() => {
    console.log("La variable d'état name a changé !");
 }, [name]);
```

Chaque fois que la variable `name` change, le composant se re-rend et le hook useEffect s'exécutera et affichera le message. Puisque cela est un tableau, nous pouvons y ajouter plusieurs choses :

```jsx
const [name, setName] = useState("Chris");

 useEffect(() => {
    console.log("Quelque chose a changé !");
 }, [name, props.name]);
```

Cette fois, lorsque la variable d'état `name` change, ou que la `prop name` change, le hook useEffect s'exécutera et affichera le message de la console.

### Peut-on utiliser componentWillUnmount() ?

Pour exécuter un hook lorsque le composant est sur le point d'être démonté, nous devons simplement retourner une fonction à partir du hook `useEffect` :

```jsx
useEffect(() => {
	console.log('exécution de l'effet');

	return () => {
		console.log('démontage');
	};
});
```

## Puis-je utiliser différents hooks ensemble ?

Oui ! Vous pouvez utiliser autant de hooks que vous le souhaitez dans un composant, et les mélanger comme vous le souhaitez :

```jsx
function App = () => {
	const [name, setName] = useState();
	const [age, setAge] = useState();

	useEffect(()=>{
		console.log("le composant a changé");
	}, [name, age])

	return(
		<div>Du jsx ici...<div>
	)
}

```

## Conclusion - Et ensuite ?

Vous l'avez compris. Les hooks nous permettent d'utiliser de bonnes vieilles fonctions JavaScript pour créer des composants React plus simples et réduire beaucoup de code boilerplate. 

Maintenant, partez dans le monde des hooks React et essayez de construire des choses vous-même ! En parlant de construire des choses vous-même...