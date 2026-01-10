---
title: Comment utiliser Debounce et Throttle dans React et les abstraire en Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-15T04:00:00.000Z'
originalURL: https://freecodecamp.org/news/debounce-and-throttle-in-react-with-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/og-image.png
tags:
- name: hooks
  slug: hooks
- name: React
  slug: react
seo_title: Comment utiliser Debounce et Throttle dans React et les abstraire en Hooks
seo_desc: "By Divyanshu Maithani\nHooks are a brilliant addition to React. They simplify\
  \ a lot of logic that previously had to be split up into different lifecycles with\
  \ class components. \nThey do, however, require a different mental model, especially\
  \ for first-..."
---

Par Divyanshu Maithani

Les [Hooks](https://reactjs.org/docs/hooks-intro.html) sont un ajout brillant à React. Ils simplifient beaucoup de logique qui devait auparavant être divisée en différents cycles de vie avec les composants `class`. 

Ils nécessitent cependant un modèle mental _différent_, [surtout pour les débutants](https://overreacted.io/making-setinterval-declarative-with-react-hooks/).

> J'ai également enregistré une courte [série vidéo](https://www.youtube.com/playlist?list=PLMV09mSPNaQlN92-1Dkz5NDlNgGQJEo75) sur cet article que vous pourriez trouver utile.

## Debounce et Throttle

Il existe de nombreux articles de blog écrits sur debounce et throttle, donc je ne vais pas expliquer comment écrire votre propre debounce et throttle. Pour faire court, considérons [`debounce`](https://lodash.com/docs/4.17.15#debounce) et [`throttle`](https://lodash.com/docs/4.17.15#throttle) de Lodash.

Si vous avez besoin d'un rappel rapide, les deux acceptent une fonction (callback) et un _délai_ en millisecondes (disons `x`) et retournent ensuite une autre fonction avec un comportement spécial :

- `debounce` : retourne une fonction qui peut être appelée un nombre quelconque de fois (possiblement en successions rapides) mais n'invoquera le callback **qu'après avoir attendu** `x` ms depuis le dernier appel.
- `throttle` : retourne une fonction qui peut être appelée un nombre quelconque de fois (possiblement en successions rapides) mais n'invoquera le callback **au plus** **une fois** toutes les `x` ms.

## Cas d'utilisation

Nous avons un éditeur de blog minimal (voici le [dépôt GitHub](https://github.com/wtjs/react-debounce-throttle-hooks/)) et nous souhaitons sauvegarder l'article de blog dans la base de données 1 seconde après que l'utilisateur ait arrêté de taper.

> Vous pouvez également vous référer à [ce Codesandbox](https://codesandbox.io/s/github/wtjs/react-debounce-throttle-hooks) si vous souhaitez voir la version finale du code.

Une version minimale de notre éditeur ressemble à ceci :

```js
import React, { useState } from 'react';
import debounce from 'lodash.debounce';

function App() {
	const [value, setValue] = useState('');
	const [dbValue, saveToDb] = useState(''); // serait normalement un appel API

	const handleChange = event => {
		setValue(event.target.value);
	};

	return (
		<main>
			<h1>Blog</h1>
			<textarea value={value} onChange={handleChange} rows={5} cols={50} />
			<section className="panels">
				<div>
					<h2>Éditeur (Client)</h2>
					{value}
				</div>
				<div>
					<h2>Sauvegardé (BD)</h2>
					{dbValue}
				</div>
			</section>
		</main>
	);
}
```

Ici, `saveToDb` serait en réalité un appel API vers le backend. Pour garder les choses simples, je le sauvegarde dans l'état et le rend ensuite sous forme de `dbValue`. 

Puisque nous voulons effectuer cette opération de sauvegarde uniquement après que l'utilisateur ait arrêté de taper (après 1 seconde), cela devrait être _debounced_.

[Voici](https://github.com/wtjs/react-debounce-throttle-hooks/tree/starter) le dépôt et la branche du code de démarrage.

## Création d'une fonction debounced

Tout d'abord, nous avons besoin d'une fonction debounced qui enveloppe l'appel à `saveToDb` :

```js
import React, { useState } from 'react';
import debounce from 'lodash.debounce';

function App() {
	const [value, setValue] = useState('');
	const [dbValue, saveToDb] = useState(''); // serait normalement un appel API

	const handleChange = event => {
		const { value: nextValue } = event.target;
		setValue(nextValue);
		// highlight-starts
		const debouncedSave = debounce(() => saveToDb(nextValue), 1000);
		debouncedSave();
		// highlight-ends
	};

	return <main>{/* Même chose qu'avant */}</main>;
}
```

Cependant, cela ne fonctionne pas réellement car la fonction `debouncedSave` est créée à chaque appel de `handleChange`. Cela finira par debouncer chaque frappe plutôt que de debouncer toute la valeur d'entrée.

## useCallback

[`useCallback`](https://reactjs.org/docs/hooks-reference.html#usecallback) est couramment utilisé pour les optimisations de performance lors du passage de callbacks à des composants enfants. Mais nous pouvons utiliser sa contrainte de mémoisation d'une fonction de callback pour nous assurer que `debouncedSave` référence la même fonction debounced à travers les rendus.

> J'ai également écrit [cet article](https://www.freecodecamp.org/news/understanding-memoize-in-javascript-51d07d19430e/) ici sur freeCodeCamp si vous souhaitez comprendre les bases de la mémoisation.

Cela fonctionne comme prévu :

```js
import React, { useState, useCallback } from 'react';
import debounce from 'lodash.debounce';

function App() {
	const [value, setValue] = useState('');
	const [dbValue, saveToDb] = useState(''); // serait normalement un appel API

	// highlight-starts
	const debouncedSave = useCallback(
		debounce(nextValue => saveToDb(nextValue), 1000),
		[], // ne sera créé qu'une seule fois initialement
	);
	// highlight-ends

	const handleChange = event => {
		const { value: nextValue } = event.target;
		setValue(nextValue);
		// Même si handleChange est créé à chaque rendu et exécuté
		// il référence le même debouncedSave qui a été créé initialement
		debouncedSave(nextValue);
	};

	return <main>{/* Même chose qu'avant */}</main>;
}
```

## useRef

[`useRef`](https://reactjs.org/docs/hooks-reference.html#useref) nous donne un objet mutable dont la propriété `current` fait référence à la valeur initiale passée. Si nous ne la changeons pas manuellement, la valeur persistera pendant toute la durée de vie du composant. 

Cela est similaire aux propriétés d'instance de classe (c'est-à-dire définir des méthodes et des propriétés sur `this`).

Cela fonctionne également comme prévu :

```js
import React, { useState, useRef } from 'react';
import debounce from 'lodash.debounce';

function App() {
	const [value, setValue] = useState('');
	const [dbValue, saveToDb] = useState(''); // serait normalement un appel API

	// Cela reste le même à travers les rendus
	// highlight-starts
	const debouncedSave = useRef(debounce(nextValue => saveToDb(nextValue), 1000))
		.current;
	// highlight-ends

	const handleChange = event => {
		const { value: nextValue } = event.target;
		setValue(nextValue);
		// Même si handleChange est créé à chaque rendu et exécuté
		// il référence le même debouncedSave qui a été créé initialement
		debouncedSave(nextValue);
	};

	return <main>{/* Même chose qu'avant */}</main>;
}
```

Continue reading on [my blog](https://divyanshu013.dev/blog/react-debounce-throttle-hooks/) for how to abstract these concepts into custom hooks or check out the [video series](https://www.youtube.com/playlist?list=PLMV09mSPNaQlN92-1Dkz5NDlNgGQJEo75).

You may also follow me on [Twitter](https://twitter.com/divyanshu013) to stay updated on my latest posts. I hope you found this post helpful. :)