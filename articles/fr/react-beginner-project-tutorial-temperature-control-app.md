---
title: Comment créer une application de contrôle de température en React – Conseils
  et code de démarrage inclus
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-08-07T16:15:43.000Z'
originalURL: https://freecodecamp.org/news/react-beginner-project-tutorial-temperature-control-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Build-a-Temperature-control-App.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment créer une application de contrôle de température en React – Conseils
  et code de démarrage inclus
seo_desc: "What we're building\nIn this beginner React project, we're going to learn\
  \ how to use state hooks, handle events, apply CSS based on state, and more! Check\
  \ it out:\n\nPrefer Video Tutorials?\nCheck out the YouTube tutorial here. \nTry\
  \ it yourself\nIf you wa..."
---

## Ce que nous construisons

Dans ce projet React pour débutants, nous allons apprendre à utiliser les hooks d'état, gérer les événements, appliquer du CSS en fonction de l'état, et plus encore ! Découvrez-le :

![](https://d33wubrfki0l68.cloudfront.net/971e266e2f7f4d42a19477cee7f608cf7b761b4a/e24a5/8363215fb6a3ce3c38580e3ba5fd86bd/project.gif)

### Préférez les tutoriels vidéo ?

[Regardez le tutoriel YouTube ici.](https://youtu.be/V3bhcxpoxQU) 

## Essayez par vous-même

Si vous voulez essayer par vous-même d'abord, voici les scénarios (vous pouvez également récupérer le CSS/code de démarrage ci-dessous) :

- Lorsque l'utilisateur clique sur le "bouton d'augmentation", la température doit augmenter
- La température ne peut pas dépasser 30
- Lorsque l'utilisateur clique sur le "bouton de diminution", la température doit diminuer
- La température ne peut pas descendre en dessous de 0
- Lorsque la température est de 15 ou plus, la couleur de fond doit passer au rouge (INDICE : J'ai inclus un style appelé "hot" que vous pouvez utiliser)
- Lorsque la température est inférieure à 15, la couleur de fond doit être bleue (INDICE : J'ai inclus un style appelé "cold" que vous pouvez utiliser)

## Installation/Code de démarrage

REMARQUE : Je suppose que vous avez un environnement de développement React configuré. Si ce n'est pas le cas, [regardez cette vidéo pour vous aider à commencer.](https://youtu.be/bZXjHauDNcg)

Tout ce dont nous avons besoin pour commencer est d'utiliser **create-react-app**. Ouvrez un terminal et exécutez :

```js
npx create-react-app temperature-control
```

Laissez le terminal faire son travail et ouvrez le projet dans VS Code (ou ce que vous utilisez).

Ensuite, allez dans **index.js**, supprimez tout et collez ce qui suit :

```jsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

ReactDOM.render(
	<React.StrictMode>
		<App />
	</React.StrictMode>,
	document.getElementById('root')
);
```

Allez dans **index.css**, supprimez tout et collez ce qui suit :

```css
body {
	font-family: sans-serif;
	text-align: center;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	text-align: center;
	min-height: 100vh;
}

.app-container {
	height: 400px;
	width: 300px;
	background: #2b5870;
	border-radius: 20px;
	box-shadow: 10px 10px 38px 0px rgba(0, 0, 0, 0.75);
}

.temperature-display-container {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 70%;
}

.temperature-display {
	display: flex;
	border-radius: 50%;
	color: #ffffff;
	height: 220px;
	width: 220px;
	text-align: center;
	justify-content: center;
	align-items: center;
	font-size: 48px;
	border: 3px #ffffff solid;
	transition: background 0.5s;
}

button {
	border-radius: 100px;
	height: 80px;
	width: 80px;
	font-size: 32px;
	color: #ffffff;
	background: rgb(105, 104, 104);
	border: 2px #ffffff solid;
}

button:hover {
	background: rgb(184, 184, 184);
	cursor: pointer;
}

button:focus {
	outline: 0;
}

.button-container {
	display: flex;
	justify-content: space-evenly;
	align-items: center;
}

.neutral {
	background: rgb(184, 184, 184);
}

.cold {
	background: #035aa6;
}

.hot {
	background: #ff5200;
}
```

Enfin, allez dans **App.js**, supprimez tout et collez ce qui suit :

```jsx
import React from 'react';

const App = () => {
	return (
		<div className='app-container'>
			<div className='temperature-display-container'>
				<div className='temperature-display'>10°C</div>
			</div>
			<div className='button-container'>
				<button>+</button>
				<button>-</button>
			</div>
		</div>
	);
};

export default App;
```

Maintenant, nous pouvons ouvrir un terminal dans VS Code et exécuter ce qui suit :

```js
npm start
```

Si tout s'est bien passé, vous devriez voir ce qui suit :

![](https://d33wubrfki0l68.cloudfront.net/45824af046bb04e327540bada2a1d40195df999a/fba86/static/1001b5afc2ce9716db3d331a43dc2327/f8915/starter.png)

Hourra ! Cela nous donne un beau modèle à utiliser, sans avoir à nous soucier du CSS.

## Rendre la valeur de la température dynamique - en utilisant l'état

La première chose que nous allons faire est de rendre la valeur de la température dynamique. Pour cela, nous allons stocker la **valeur de la température dans l'état**. Cela nous facilite l'accès à la valeur plus tard et nous permet d'effectuer des opérations logiques avec celle-ci.

> Si quelque chose change sur votre interface utilisateur, c'est une bonne idée de le mettre dans l'état.

Dans **App.js**, importez le hook **useState** en haut du fichier comme suit :

```jsx
import React, { useState } from 'react';
```

Ensuite, ajoutez ce qui suit dans la **fonction App** :

```jsx
const [temperatureValue, setTemperatureValue] = useState(10);
```

Un petit rappel sur **useState** - il nous permet de stocker des données dans l'état du composant. Le hook **useState** nous donne 2 choses :

- une variable qui contient la valeur actuelle de l'état
- une fonction pour changer la valeur de l'état.

Dans ce cas, nous avons appelé notre variable d'état **temperatureValue** et notre fonction **setTemperatureValue**. Nous avons initialisé notre temperatureValue à une valeur de **10**, en passant la **valeur 10** au hook useState.

Maintenant que nous avons une valeur d'état, il est temps de l'utiliser dans notre code. Rappelez-vous, les éléments que nous obtenons de **useState** peuvent être utilisés comme n'importe quelle variable ou fonction JavaScript (puisque c'est ce qu'ils sont).

Dans notre JSX, nous voulons remplacer la valeur de température codée en dur en utilisant notre nouvelle variable d'état. Changez cette ligne :

```jsx
<div className='temperature-display'>10°C</div>
```

Pour qu'elle devienne ceci :

```jsx
<div className='temperature-display'>{temperatureValue}°C</div>
```

Remarquez comment nous avons utilisé **{}** pour rendre notre variable **temperatureValue**. Maintenant, lorsque notre valeur de température change, le composant se rerendera et affichera la nouvelle valeur de température. 

Notre fichier **App.js** jusqu'à présent ressemble à ceci :

```jsx
import React, { useState } from 'react';

const App = () => {
	const [temperatureValue, setTemperatureValue] = useState(10);

	return (
		<div className='app-container'>
			<div className='temperature-display-container'>
				<div className='temperature-display'>{temperatureValue}°C</div>
			</div>
			<div className='button-container'>
				<button>+</button>
				<button>-</button>
			</div>
		</div>
	);
};

export default App;
```

Maintenant, si vous exécutez l'application et regardez le navigateur, vous verrez que les choses ont l'air identiques à avant. 

Mais si vous changez la **valeur initiale que nous passons au hook useState** de 10 à autre chose (par exemple 15), vous verrez que l'application se met à jour. Cela signifie que notre hook d'état fonctionne !

## Changer l'état au clic sur un bouton

Travaillons maintenant sur l'augmentation/diminution de la valeur de la température lorsque les boutons sont cliqués. 

Comme nous le savons, le hook useState nous donne une fonction **setTemperatureValue** que nous pouvons utiliser pour changer la **temperatureValue**. Il est donc logique de lier cela à l'événement **onClick** du bouton.

Nous allons d'abord faire le bouton d'augmentation. Remplacez le bouton d'augmentation par ce qui suit :

```jsx
<button onClick={() => setTemperatureValue(temperatureValue + 1)}>+</button>
```

Remarquez comment cela appelle la fonction **setTemperatureValue**. Nous prenons la **temperatureValue** actuelle, ajoutons 1, et passons cela comme argument.

Ainsi, puisque temperatureValue commence à 10, ajouter 1 définira la valeur de l'état à 11. Lorsque le bouton est cliqué à nouveau, l'état est défini à 12, et ainsi de suite.

Ensuite, nous ferons de même avec le bouton de diminution. Remplacez le bouton de diminution actuel par ce qui suit :

```jsx
<button onClick={() => setTemperatureValue(temperatureValue - 1)}>-</button>
```

Cela fait la même chose, sauf que nous diminuons la **temperatureValue** cette fois.

Notre code ressemble maintenant à ceci :

```jsx
import React, { useState } from 'react';

const App = () => {
	const [temperatureValue, setTemperatureValue] = useState(10);

	return (
		<div className='app-container'>
			<div className='temperature-display-container'>
				<div className='temperature-display'>{temperatureValue}°C</div>
			</div>
			<div className='button-container'>
				<button onClick={() => setTemperatureValue(temperatureValue + 1)}>+</button>
				<button onClick={() => setTemperatureValue(temperatureValue - 1)}>-</button>
			</div>
		</div>
	);
};

export default App;
```

Essayez d'exécuter cela dans le navigateur et de cliquer sur les boutons. Les valeurs augmenteront/diminueront.

## Changer la couleur en fonction de l'état

Maintenant, faisons quelque chose de plus avancé. Nous voulons que la couleur de fond de l'affichage change en fonction de la température. 

Si la température est de 15 degrés ou plus, nous voulons changer la couleur de fond en rouge. Si elle est inférieure à 15, nous voulons changer la couleur de fond en bleu. 

Si vous regardez le CSS, j'ai fourni 2 classes :

- `.cold` qui définit le fond en bleu
- `.hot` qui définit le fond en rouge

Si nous ajoutons l'une de ces classes à la div **temperature display**, cela change la couleur. Par exemple :

```jsx
<div className='temperature-display cold'>{temperatureValue}°C</div>
```

donnera à l'affichage de la température un fond bleu, tandis que :

```jsx
<div className='temperature-display hot'>{temperatureValue}°C</div>
```

donnera à l'affichage de la température un fond rouge.

D'accord, c'est bien et tout, mais comment ajoutons-nous ces classes **dynamiquement** en fonction de l'état ? 

Rappelez-vous, il est généralement bon de mettre les choses qui peuvent changer sur votre interface utilisateur dans l'état. Donc l'état est un endroit parfait pour stocker la classe CSS actuelle que nous voulons utiliser.

Allons-y et créons un autre hook d'état pour stocker la **temperatureColor** comme suit :

```jsx
const [temperatureColor, setTemperatureColor] = useState('cold');
```

Remarquez que nous initialisons notre objet d'état **temperatureColor** avec une valeur de "cold" (puisque notre valeur de température est initialement de 10 degrés, nous voulons que la couleur de fond soit bleue).

Nous pouvons ensuite utiliser des **littéraux de gabarit** pour ajouter dynamiquement les classes que nous voulons en utilisant cette variable d'état. Allez-y et mettez à jour le code avec ce qui suit :

```jsx
<div className={`temperature-display ${temperatureColor}`}>{temperatureValue}°C</div>
```

C'est une syntaxe un peu délicate à comprendre, alors ne vous inquiétez pas si vous ne comprenez pas tout de suite. 

Tout ce que cela fait, c'est créer une chaîne et appliquer dynamiquement la variable **temperatureColor**. Chaque fois que **temperatureColor** change en "hot", le composant se rerendera et la classe CSS "hot" sera ajoutée à la chaîne className à la place.

Notre code jusqu'à présent ressemble à ceci :

```jsx
import React, { useState } from 'react';

const App = () => {
	const [temperatureValue, setTemperatureValue] = useState(10);
	const [temperatureColor, setTemperatureColor] = useState('cold');

	return (
		<div className='app-container'>
			<div className='temperature-display-container'>
				<div className={`temperature-display ${temperatureColor}`}>{temperatureValue}°C</div>
			</div>
			<div className='button-container'>
				<button onClick={() => setTemperatureValue(temperatureValue + 1)}>+</button>
				<button onClick={() => setTemperatureValue(temperatureValue - 1)}>-</button>
			</div>
		</div>
	);
};

export default App;
```

Changez la variable d'état **temperatureColor** initiale en "hot" / "cold" et le fond de l'affichage de la température devrait changer.

Maintenant que nous savons que cela fonctionne, tout ce que nous avons à faire est de changer la variable d'état. Mais où faisons-nous cela ?

Eh bien, nous avons déjà un **gestionnaire onClick qui change la temperatureValue**, donc il est logique d'ajouter notre nouvelle logique à ce gestionnaire.

Jusqu'à présent, nous avons utilisé une **fonction en ligne** pour nos gestionnaires d'événements de clic. Et utiliser des fonctions en ligne est bien lorsque nous avons une fonction d'une ligne. 

Mais lorsque nous avons une fonction de plusieurs lignes avec beaucoup de logique, il est préférable de déplacer la fonction hors du JSX. Cela rend notre code un peu plus propre.

Allez-y et collez ce qui suit juste en dessous de tout le code d'état :

```jsx
const increaseTemperature = () => {
	setTemperatureValue(temperatureValue + 1);
};

const decreaseTemperature = () => {
	setTemperatureValue(temperatureValue - 1);
};
```

Ici, nous définissons 2 fonctions - une qui augmente la température et une autre qui la diminue. 

Ensuite, nous voulons changer les propriétés **onClick** de nos boutons pour appeler ces fonctions au lieu des fonctions en ligne que nous avions précédemment :

```jsx
    <button onClick={increaseTemperature}>+</button>
    <button onClick={decreaseTemperature}>-</button>
```

Maintenant, au lieu d'utiliser une fonction en ligne, nous passons une référence à nos fonctions _increaseTemperature_ et _decreaseTemperature_. Notre code jusqu'à présent ressemble à ceci :

```jsx
import React, { useState } from 'react';

const App = () => {
	const [temperatureValue, setTemperatureValue] = useState(10);
	const [temperatureColor, setTemperatureColor] = useState('cold');

	const increaseTemperature = () => {
		setTemperatureValue(temperatureValue + 1);
	};

	const decreaseTemperature = () => {
		setTemperatureValue(temperatureValue - 1);
	};

	return (
		<div className='app-container'>
			<div className='temperature-display-container'>
				<div className={`temperature-display ${temperatureColor}`}>{temperatureValue}°C</div>
			</div>
			<div className='button-container'>
				<button onClick={increaseTemperature}>+</button>
				<button onClick={decreaseTemperature}>-</button>
			</div>
		</div>
	);
};

export default App;
```

Remarquez comment rien n'a changé pour l'instant - nous sommes simplement en train de refactoriser notre code et de nous préparer pour les changements à venir. 

Maintenant, il est beaucoup plus facile d'ajouter de la logique de code pour l'un ou l'autre des événements de clic sur les boutons - nous écrivons simplement notre logique dans la fonction appropriée et tout va bien.

OK ! Le refactoring étant terminé, revenons à nos affaires. Nous avons dit que **lorsque la température est de 15 degrés ou plus, nous voulons changer la valeur de l'état temperatureColor**.

Nous pouvons ajouter cette logique à notre fonction **increaseTemperature** comme suit :

```jsx
const increaseTemperature = () => {
	const newTemperature = temperatureValue + 1;
	setTemperatureValue(newTemperature);

	if (newTemperature >= 15) {
		setTemperatureColor('hot');
	}
};
```

Qu'avons-nous fait ?

- Nous avons créé une variable pour stocker la valeur **newTemperature** (nous avons fait cela puisque nous utiliserons cette variable à plusieurs endroits)
- Nous avons défini la **temperatureValue**, comme nous l'avons fait auparavant
- Nous avons écrit une **instruction if** pour vérifier si la valeur **newTemperature** est supérieure ou égale à 15
- Si oui, alors nous utilisons la fonction **setTemperatureColor** pour définir la valeur de l'état **temperatureColor** à "hot"

Ainsi, chaque fois que nous cliquons sur le bouton suffisamment de fois pour que la **temperatureValue** soit supérieure ou égale à 15, la variable **temperatureColor** change, le composant se rerend, et la classe "hot" est ajoutée à l'affichage de la température comme par magie.

Mais attendez ! Nous n'avons pas encore géré la diminution. Ce qui est essentiellement similaire à la fonction d'augmentation :

```jsx
const decreaseTemperature = () => {
	const newTemperature = temperatureValue - 1;
	setTemperatureValue(newTemperature);
	if (newTemperature < 15) {
		setTemperatureColor('cold');
	}
};
```

Cette fois, nous soustrayons un et vérifions si la nouvelle valeur est inférieure à 15 avant de changer la **couleur de la température**

Notre code final de l'application ressemble à ceci :

```jsx
import React, { useState } from 'react';

const App = () => {
	const [temperatureValue, setTemperatureValue] = useState(10);
	const [temperatureColor, setTemperatureColor] = useState('cold');

	const increaseTemperature = () => {
		const newTemperature = temperatureValue + 1;
		setTemperatureValue(newTemperature);

		if (newTemperature >= 15) {
			setTemperatureColor('hot');
		}
	};

	const decreaseTemperature = () => {
		const newTemperature = temperatureValue - 1;
		setTemperatureValue(newTemperature);
		if (newTemperature < 15) {
			setTemperatureColor('cold');
		}
	};

	return (
		<div className='app-container'>
			<div className='temperature-display-container'>
				<div className={`temperature-display ${temperatureColor}`}>{temperatureValue}°C</div>
			</div>
			<div className='button-container'>
				<button onClick={increaseTemperature}>+</button>
				<button onClick={decreaseTemperature}>-</button>
			</div>
		</div>
	);
};

export default App;
```

Exécutez l'application et tout devrait fonctionner - hourra !

## Un défi à essayer

Vous avez peut-être remarqué que notre contrôle de température n'est pas très sûr - l'utilisateur peut augmenter la température jusqu'à atteindre 100°C, se faisant bouillir jusqu'à l'oubli, ou diminuer la température jusqu'à atteindre -100°C, se transformant en un énorme cube de glace.

Le défi, si vous choisissez de l'accepter, est d'empêcher la valeur de la température de **dépasser 30°C**, et de l'empêcher de **descendre en dessous de 30°C**.

INDICE : Les fonctions **increaseTemperature** et **decreaseTemperature** sont des endroits parfaits pour ajouter cette logique !