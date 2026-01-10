---
title: Apprendre les Hooks React en construisant une application de dessin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-05T17:04:06.000Z'
originalURL: https://freecodecamp.org/news/learn-react-hooks-by-building-a-paint-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/hooks-logo.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: Scrimba
  slug: scrimba
seo_title: Apprendre les Hooks React en construisant une application de dessin
seo_desc: 'By Per Harald Borgen

  According to people in the know, React Hooks are hot, hot, hot. In this article,
  we follow Christian Jensen''s 14-part tutorial to find out about the basics of this
  new feature of React. Follow along to find out more!


  Intro


  Hook...'
---

Par Per Harald Borgen

Selon les experts, les Hooks React sont très populaires. Dans cet article, nous suivons le [tutoriel en 14 parties de Christian Jensen](https://scrimba.com/g/greacthooks?utm_source=dev.to&utm_medium=referral&utm_campaign=greacthooks_launch_article) pour découvrir les bases de cette nouvelle fonctionnalité de React. Suivez-nous pour en savoir plus !

![Les Hooks React que nous allons apprendre dans ce cours](https://thepracticaldev.s3.amazonaws.com/i/mh1hdo0zzhtgei8gv614.png)

# Introduction

![Application de dessin que nous allons construire pendant ce projet](https://thepracticaldev.s3.amazonaws.com/i/1j9osq1fshioocmoo0v4.png)

Les Hooks sont une nouveauté dans la bibliothèque React et permettent de partager la logique entre les composants et de les rendre réutilisables.

Dans ce cours, nous allons construire une application de dessin similaire à Microsoft Paint, qui nous permettra de nommer notre projet, de changer de couleurs, d'obtenir une nouvelle série de couleurs et, bien sûr, de peindre.

Scrimba permet de mettre en pause les screencasts à tout moment et de jouer avec le code. C'est une excellente façon d'apprendre en pratiquant !

# Prérequis

Le cours suppose quelques [connaissances préalables d'ES6](https://www.freecodecamp.org/news/learn-modern-javascript-in-this-free-28-part-course-7ec8d353eb/), [JSX, State et Props](https://www.freecodecamp.org/news/learn-react-js-in-5-minutes-526472d292f4/), mais ne vous inquiétez pas, nous vous avons couvert - consultez nos articles Scrimba en cliquant sur les liens ci-dessus.

Si vous êtes complètement nouveau dans React, assurez-vous de consulter notre [cours Scrimba React](https://scrimba.com/g/glearnreact?utm_source=dev.to&utm_medium=referral&utm_campaign=greacthooks_launch_article)

# `useState` - Partie 1

Tout d'abord, nous donnons à notre application un moyen de gérer l'état en utilisant `useState`.

Dans notre composant `<Playground.js />`, nous déclarons un composant appelé `<Playground />` et créons des boutons pour incrémenter et décrémenter. Nous donnons ensuite à `useState` un argument de (0) et utilisons la déstructuration d'état pour obtenir `state` et `setState` (la fonction qui met à jour l'état) à partir de notre fonction `useState`. Ceux-ci sont maintenant renommés en `count` et `setCount`. Nous affichons ensuite notre compteur dans le navigateur.

Enfin, nous affichons des boutons qui mettent à jour le compteur en utilisant une fonction en ligne qui sera déclenchée au clic.

![Incrémentation du compteur avec nos boutons](https://thepracticaldev.s3.amazonaws.com/i/kohiz9hz2f49n5i80l71.png)

Pour nous assurer que notre compteur est précis, nous passons une fonction à notre fonction `setState` au lieu d'une valeur. Cette fonction prend l'état actuel comme argument, qui est ensuite mis à jour :

```js
import React, { useState } from "react";
import randomColor from "randomcolor";

export default function Playground() {
	const [count, setCount] = useState(0);
	return (
		<div>
			{count}
			<button onClick={() => setCount((currentCount) => currentCount - 1)}>
				-
			</button>
			<button onClick={() => setCount((currentCount) => currentCount + 1)}>
				+
			</button>
		</div>
	);
}
```

Si vous êtes inquiet de la performance des fonctions en ligne, consultez [ce](https://cdb.reacttraining.com/react-inline-functions-and-performance-bdff784f5578) blog.

# `useState` - Partie 2

Maintenant, nous ajoutons notre champ de saisie de nom au composant `<Name.js />` afin que l'utilisateur puisse nommer son projet.

Pour configurer `<Name.js />` avec un Hook `useState`, nous devons importer le Hook avec une importation nommée, puis configurer notre état. Notre état sera `name` et nous le mettrons à jour avec setName. Nous appelons ensuite `useState` et passons une chaîne vide comme valeur d'état par défaut.

Nous avons maintenant besoin d'un élément d'entrée avec quatre propriétés. Ce sont :

- `value`, qui sera toujours l'état `name` ci-dessus
- `onChange`, qui utilisera `setState` en ligne pour mettre à jour `name` en passant la valeur dans `setState`
- `onClick` qui utilise setSelectionRange qui prend un index de début de 0 et un index de fin de la longueur de la chaîne pour sélectionner le nom entier, ce qui facilite la modification du nom pour l'utilisateur final.
- `placeholder`, que nous définissons sur 'Sans titre'.

```js
import React, { useState } from "react";

export default function Name() {
	const [name, setName] = useState("");
	return (
		<label className="header-name">
			<input
				value={name}
				onChange={(e) => setName(e.target.value)}
				onClick={(e) => e.target.setSelectionRange(0, e.target.value.length)}
				placeholder="Sans titre"
			/>
		</label>
	);
}
```

Nous pouvons maintenant nommer notre projet et sélectionner le nom pour le réinitialiser en un seul clic :

![Champ de saisie du nom du projet en action.](https://thepracticaldev.s3.amazonaws.com/i/rgupvtuwliarlt2woyrj.png)

# `useEffect`

Actuellement, notre composant Playground.js se contente d'afficher un compteur où nous pouvons incrémenter ou décrémenter le compte. Maintenant, nous allons le mettre à jour pour que chaque fois que le compte est modifié, la couleur de quelque chose soit également modifiée.

Nous utilisons le Hook `useState` pour définir la couleur initiale, que nous définissons sur `null` et la fonction pour la mettre à jour (`setColor`). Maintenant, nous configurons `useEffect` pour mettre à jour cette couleur. Le premier argument de `useEffect` est setColor, que nous voulons définir sur une `randomColor`.

Comme nous voulons qu'un changement dans `count` déclenche `useEffect`, nous le définissons comme deuxième argument. Si la valeur du compte n'a pas changé, le Hook n'exécutera pas l'effet et la couleur restera la même.

```js
import React, { useState, useEffect } from "react";
import randomColor from "randomcolor";

export default function Playground() {
	const [count, setCount] = useState(0);

	const [color, setColor] = useState(null);
	useEffect(() => {
		setColor(randomColor());
	}, [count]);

	return (
		<div style={{ borderTop: `10px solid ${color}` }}>
			{count}
			<button onClick={() => setCount((currentCount) => currentCount - 1)}>
				-
			</button>
			<button onClick={() => setCount((currentCount) => currentCount + 1)}>
				+
			</button>
		</div>
	);
}
```

Maintenant, notre couleur change chaque fois que nous incrémentons ou décrémentons notre compteur.

![couleur initiale](https://thepracticaldev.s3.amazonaws.com/i/6b6n7h96pkk89llw6abi.png)

![couleur changée par un incrément](https://thepracticaldev.s3.amazonaws.com/i/vawilltd0p7mu15lwa1d.png)

![couleur changée par un deuxième incrément](https://thepracticaldev.s3.amazonaws.com/i/sq1ouu7f3d7u26kuov3f.png)

![couleur changée par un décrément](https://thepracticaldev.s3.amazonaws.com/i/f2paopu37b35ojior8s7.png)

# Défi `useState` & `useEffect`

Il est maintenant temps de tester les compétences que nous avons acquises jusqu'à présent. Dans ce screencast, une fonction qui obtient quelques couleurs aléatoires pour nous a été ajoutée à <Paint.js /> :

```js
const getColors = () => {
	const baseColor = randomColor().slice(1);
	fetch(`https://www.thecolorapi.com/scheme?hex=${baseColor}&mode=monochrome`)
		.then((res) => res.json())
		.then((res) => {
			setColors(res.colors.map((color) => color.hex.value));
			setActiveColor(res.colors[0].hex.value);
		});
};
```

Notre tâche est d'écrire les fonctions pour `setColors`, qui nous donnera un tableau de couleurs hexadécimales et `setActiveColor`, qui nous indiquera quelle est la couleur active.

Si nous configurons tout correctement, l'interface utilisateur sera mise à jour avec cinq couleurs sur lesquelles nous pouvons cliquer pour les développer. Nous n'avons besoin que de `useState` et `useEffect` pour ce test.

# Solution `useState` & `useEffect`

Dans [ce](https://scrimba.com/p/pKkkVU3/cDbkNJsg?utm_source=dev.to&utm_medium=referral&utm_campaign=greacthooks_launch_article) screencast, Christian nous explique comment donner de la fonctionnalité au composant `<ColorPicker />`. À la fin, nous avons maintenant quelques couleurs :

![couleurs visibles dans l'interface utilisateur](https://thepracticaldev.s3.amazonaws.com/i/rxe2h70fqoldqf6ouoss.png)

# Nettoyage de `useEffect`

Maintenant, nous ajoutons un composant appelé `<WindowSize.js />` qui affichera la largeur et la hauteur de la fenêtre en bas de l'écran lorsque l'utilisateur redimensionne la fenêtre. Cela disparaît ensuite après une demi-seconde.

Lorsque nous configurons un minuteur ou un écouteur d'événements, nous devons également le nettoyer une fois que le composant est démonté. Cela nécessite deux éléments d'état - la taille de la fenêtre et la visibilité du composant `<WindowSize />` :

```js
export default function WindowSize() {
	const [[windowWidth, windowHeight], setWindowSize] = useState([
		window.innerWidth,
		window.innerHeight,
	]);
	const [visible, setVisible] = useState(false);
}
```

Maintenant, nous configurons notre effet, qui ajoute l'écouteur d'événements :

```js
useEffect(() => {
	const handleResize = () => {};
	window.addEventListener("resize", handleResize);
});
```

Ensuite, nous configurons la phase de nettoyage. Cela retourne la fonction et un tableau vide est passé pour indiquer que `useEffect` ne doit s'exécuter qu'au premier montage. Le nettoyage s'exécutera ensuite et supprimera l'écouteur d'événements :

```js
useEffect(() => {
	const handleResize = () => {};
	window.addEventListener("resize", handleResize);
	return () => window.removeEventListener("resize", handleResize);
}, []);
```

Nous configurons maintenant la taille de la fenêtre, la visibilité et le minuteur pour que la fenêtre de redimensionnement apparaisse puis disparaisse après 500 millisecondes :

```js
const [visible, setVisible] = useState(false);
useEffect(() => {
	const handleResize = () => {
		setWindowSize([window.innerWidth, window.innerHeight]);
		setVisible(true);
		setTimeout(() => setVisible(false), 500);
	};
	window.addEventListener("resize", handleResize);
	return () => window.removeEventListener("resize", handleResize);
}, []);
```

Cependant, nous ne voulons pas ajouter un nouveau minuteur chaque fois que l'utilisateur redimensionne la fenêtre, donc nous devons également nettoyer le minuteur avec `clearTimeout(timeoutId)` :

```js
timeoutId = setTimeout(() => setVisible(false), 500);
```

Pour donner à `clearTimeout` l'`timeoutId` de la dernière fois que la fonction a été exécutée, nous utilisons des _closures_, ce qui signifie que nous déclarons notre variable `timeoutId` en dehors de la fonction `handleResize`. De cette façon, la variable est toujours disponible pour la fonction interne. Chaque fois que la fonction s'exécute, le délai précédent sera effacé et un nouveau sera configuré.

Enfin, nous affichons notre fonction de redimensionnement dans le navigateur. Le code final peut être vu dans le screencast.

Maintenant, chaque fois que l'utilisateur redimensionne sa fenêtre, la taille de la fenêtre est définie sur la taille actuelle de la fenêtre, la visibilité est définie sur vrai, et un minuteur est démarré pour définir la visibilité sur faux après 500 millisecondes.

![navigateur avec la fonction de redimensionnement affichée](https://thepracticaldev.s3.amazonaws.com/i/bg2ir6q0ik2zfrhdh8f0.png)

# Défi `useRef`

Si vous avez besoin d'accéder aux éléments DOM réels dans React, vous devrez peut-être utiliser des Refs. React a un Hook, `useRef`, qui est dédié aux Refs.

Pour utiliser une Ref, elle doit être ajoutée à l'élément :

```js
<input
	ref={inputRef}
	type="range"
	onChange={(e) => setCount(e.target.value)}
	value={count}
/>
```

Cette entrée est un curseur qui met à jour le `count` et donc la couleur sélectionnée. Comme la valeur est également liée au compte, le curseur s'ajustera également si le compte est modifié via les boutons que nous avons ajoutés précédemment.

Nous avons maintenant déclaré notre Ref, mais nous devons également la configurer en appelant `useRef` :

```js
const inputRef = useRef();
```

Afin de focaliser l'entrée chaque fois que nous changeons le compte avec les boutons, nous ajoutons simplement la logique nécessaire à l'intérieur de l'effet qui s'exécute lorsque les boutons sont cliqués :

```js
 useEffect(() => {
    setColor(randomColor())
    inputRef.current.focus()
  },
```

![Curseur en focus](https://thepracticaldev.s3.amazonaws.com/i/l0gksyz0v6rd5ve9x0pl.png)

Actuellement, le canevas est défini à la hauteur de la fenêtre elle-même, ce qui permet à l'utilisateur de faire défiler le canevas, ce qui peut entraîner des espaces vides si l'image est exportée.

Notre défi est maintenant de nous assurer que le canevas de notre application de dessin n'est pas plus grand que la fenêtre moins la hauteur de l'en-tête. Pour ce faire, nous devons utiliser useRef pour obtenir la hauteur de l'en-tête et la soustraire de la hauteur de la fenêtre.

# Solution `useRef`

Dans [ce](https://scrimba.com/p/pKkkVU3/c66w99up?utm_source=dev.to&utm_medium=referral&utm_campaign=greacthooks_launch_article) screencast, Christian nous explique comment obtenir la hauteur correcte du canevas avec `useRef`.

Après cela, l'utilisateur ne peut plus faire défiler, sauf pour quelques pixels de décalage entre le navigateur de Scrimba et un navigateur régulier. Il n'y a plus d'espace vide en bas de l'image.

# `useCallback` & `useMemo` + Défi

Dans ce screencast, nous sommes introduits au concept de _mémoisation_. Cela se produit lorsqu'une fonction pure retourne la même sortie d'un calcul qu'elle a précédemment traité, plutôt que de relancer l'ensemble du calcul :

```js
function Calculate(num) {
	// premier appel, num === 3... ok je vais calculer cela
	return fetchComplicatedAlgorithmToAdd47(3); // retourne 50 après un certain temps

	// deuxième appel, num === 5... ok je suppose que je dois calculer cela aussi
	return fetchComplicatedAlgorithmToAdd47(5); // retourne 52 après un certain temps

	// troisième appel, num === 3... ATTENDEZ, j'ai déjà vu cela ! Je connais celui-ci !
	return 50; // immédiatement
}
```

React fournit deux Hooks qui nous permettent d'utiliser la mémoisation : `useCallback` et `useMemo`.

### `useCallback`

Nous commençons par un composant très simple dans Playground.js qui affiche le nombre de fois que la fonction a été rendue :

```js
function Calculate(num) {
	const renderCount = useRef(1);
	return <div>{renderCount.current++}</div>;
}
```

![compte de rendu dans le navigateur.](https://thepracticaldev.s3.amazonaws.com/i/t1l5jq70ub57jb3g1vc0.png)

Maintenant, disons que le composant ne doit se rendre que lorsque le compte change, mais pas lorsque la couleur change. Pour y parvenir, nous pourrions utiliser `useCallback`. Nous attribuons le résultat de `useCallback` à une variable appelée `calculate` :

```js
const calculate = useCallback(<Calculate />, [count]);
```

Nous allons maintenant rendre notre nouvelle variable `calculate` au lieu du composant `<Calculate />`. Maintenant, le composant ne se rend que lorsque le compte est modifié, et non lorsque le bouton 'Changer de couleur' est cliqué.

Nous devons également rendre notre composant `<Calculate />` au lieu de la variable que nous avons utilisée précédemment et créer une fonction de rappel. Nous utilisons `useCallback` et l'attribuons à une variable appelée `cb`. Le `count` est la seule dépendance, ce qui signifie que si le compte change, nous obtiendrons une nouvelle instance de fonction :

```js
const cb = useCallback((num) => console.log(num), [count]);
```

Maintenant, nous passons un nombre (qui est défini sur le compte) au composant `Calculate` et à la fonction de rappel, que nous enregistrons dans la console. Chaque fois que le composant `Calculate` est réaffiché (c'est-à-dire lorsque les boutons plus et moins sont cliqués), le compte actuel sera enregistré dans la console.

Cependant, avec cette méthode, le compte est également enregistré dans la console lorsque nous cliquons sur le bouton 'Changer de couleur'. Cela est dû au fait que nous utilisons la mémoisation pour notre fonction `console.log`, mais pas pour notre composant réel, ce qui signifie qu'il ne vérifie pas si la fonction de rappel est la même qu'une précédente.

### `React.memo`

Pour résoudre ce problème, nous ajoutons React.memo au composant `Calculate`. Maintenant, il vérifiera les entrées et verra si elles sont les mêmes, et ne se rendra pas si c'est le cas :

```js
const Calculate = React.memo(({ cb, num }) => {
	cb(num);
	const renderCount = useRef(1);
	return <div>{renderCount.current++}</div>;
});
```

Le bouton 'Changer de couleur' n'enregistre plus le compte dans la console.

### `useMemo`

Pour voir ce que `useMemo` peut faire, nous ajoutons un appel `useCallback` juste à côté d'un appel `useMemo` :

```js
useCallback(() => console.log("useCallback"));
useMemo(() => console.log("useMemo"));
```

Cela nous indique que `useMemo` est utilisé chaque fois que la fonction est rendue. Cela est dû au fait que `useCallback` retourne les fonctions, tandis que `useMemo` retourne le résultat de la fonction :

```js
useCallback(() => console.log("useCallback")); // retourne la fonction
useMemo(() => console.log("useMemo")); // retourne le résultat de la fonction
```

`useMemo` peut être utilisé pour certaines fonctions coûteuses que vous souhaitez mémoïser. `useCallback`, en revanche, est meilleur pour passer un rappel dans un composant lorsque vous ne voulez pas rendre le composant inutilement.

Le screencast se termine par un nouveau défi. Notre application de dessin offre actuellement seulement quelques couleurs à utiliser. Notre défi est d'ajouter une fonctionnalité à un bouton de rafraîchissement nouvellement ajouté afin que l'utilisateur puisse cliquer sur le bouton et obtenir de nouvelles couleurs. Cela devrait avoir lieu dans `RefreshButton.js`, qui prend actuellement un rappel et devrait appeler ce rappel lorsque le bouton de rafraîchissement est cliqué. Notre défi est de passer le rappel en utilisant `useCallback` ou `useMemo`.

![Bouton de rafraîchissement nécessitant une fonctionnalité](https://thepracticaldev.s3.amazonaws.com/i/3fdokbwtn6h2gr7xwo44.png)

En tant que défi bonus, nous sommes également invités à utiliser `React.memo` pour mémoïser le composant `<Name />`, qui est actuellement rendu inutilement chaque fois que nous changeons nos couleurs.

# Solution `useCallback`

Maintenant, Christian nous guide à travers la solution des défis précédents, suivez-le dans [ce](https://scrimba.com/p/pKkkVU3/c9PEyQC4?utm_source=dev.to&utm_medium=referral&utm_campaign=greacthooks_launch_article) screencast.

À la fin du screencast, notre bouton de rafraîchissement fournit maintenant de nouvelles couleurs brillantes lorsqu'il est cliqué :

![Bouton de rafraîchissement changeant les couleurs - 1](https://thepracticaldev.s3.amazonaws.com/i/ryhwc1o6fcn7liligbhd.png)

![Bouton de rafraîchissement changeant les couleurs - 2](https://thepracticaldev.s3.amazonaws.com/i/t0vnezx4e2fumqq60qeb.png)

# Hooks personnalisés

Ici, nous apprenons les Hooks personnalisés en refactorisant le composant `<WindowSize />` en un Hook. C'est idéal pour la réutilisabilité.

Actuellement, `<WindowSize />` gère deux ensembles d'états différents ; la taille de la fenêtre et la visibilité. Comme la visibilité pourrait ne pas être nécessaire dans les utilisations futures de `<WindowSize />`, nous déplaçons sa logique dans notre composant `<Paint />`, qui est également où nous utiliserons notre Hook `useWindowSize`.

Les lignes suivantes sont supprimées de `WindowSize.js` :

```js
let timeoutId;
///
setVisible(true);
clearTimeout(timeoutId);
timeoutId = setTimeout(() => setVisible(false), 500);
```

De plus, les lignes suivantes doivent maintenant être retournées par `<Paint.js />` au lieu de `<WindowSize />` :

```js
<div className={`window-size ${visible ? "" : "hidden"}`}>
	{windowWidth} x {windowHeight}
</div>
```

La largeur et la hauteur de la fenêtre seront retournées par `<WindowSize />` :

```js
return [windowWidth, windowHeight];
```

Pour rendre les variables `windowWidth` et `windowHeight` disponibles, nous ajoutons le code suivant à `<Paint.js />` :

```js
const [windowWidth, windowHeight] = useWindowSize();
```

Pour implémenter la logique de visibilité afin que nous puissions afficher et masquer la taille de la fenêtre selon les besoins, nous passons un rappel à notre Hook `useWindowSize` et utilisons une Ref pour rendre `timeoutID` disponible entre les rendus :

```js
let timeoutId = useRef();
const [windowWidth, windowHeight] = useWindowSize(() => {
	setVisible(true);
	clearTimeout(timeoutId.current);
	timeoutId.current = setTimeout(() => setVisible(false), 500);
});
```

Nous pouvons maintenant appeler cela lorsque nous en avons besoin depuis `<WindowSize />` :

```js
export default function useWindowSize(cb) {
	const [[windowWidth, windowHeight], setWindowSize] = useState([
		window.innerWidth,
		window.innerHeight,
	]);

	useEffect(() => {
		const handleResize = () => {
			cb();
			setWindowSize([window.innerWidth, window.innerHeight]);
		};
		window.addEventListener("resize", handleResize);
		return () => window.removeEventListener("resize", handleResize);
	}, []);
	return [windowWidth, windowHeight];
}
```

Nous avons maintenant la même fonctionnalité qu'avant mais la logique `<WindowSize />` est dans un Hook réutilisable.

La leçon se termine par un autre défi - convertir le composant `<Canvas />` en une fonction qui utilise des Hooks au lieu de méthodes de cycle de vie.

# Construction de l'application de dessin avec des Hooks

Ce screencast nous guide à travers la conversion de `<Canvas />` en un composant fonctionnel utilisant des Hooks. Il nous montre également comment refactoriser notre application pour la rendre beaucoup plus propre et plus lisible. Un grand avantage de l'utilisation des Hooks est que toute la logique liée est à côté l'une de l'autre, contrairement à nos anciens composants dans lesquels les éléments de logique liés étaient séparés les uns des autres.

À la fin du screencast, notre application de dessin est enfin terminée et nous sommes prêts à peindre nos chefs-d'œuvre :

![utilisation de notre application de dessin](https://thepracticaldev.s3.amazonaws.com/i/04cpj3smokmoxf3ivx7f.png)

# Conclusion

Nous avons maintenant terminé le cours sur les Hooks React. Nous avons appris :

- `useState`, qui gère l'état
- `useEffect`, qui effectue des effets secondaires,
- `useRef`, qui obtient des références aux éléments DOM et conserve les valeurs entre les rendus
- `useCallback`, qui crée des fonctions qui n'ont pas besoin d'être créées à chaque rendu
- `useMemo`, qui mémoïse les calculs coûteux
- `React.Memo`, qui peut entourer un composant React et le mémoïser
- `Hooks personnalisés`, qui nous permettent de créer notre propre logique réutilisable.

Il y a deux règles à garder à l'esprit lors de l'utilisation de ces Hooks :

1. N'appeler les Hooks qu'au niveau supérieur du composant React, c'est-à-dire pas dans des blocs if ou autre chose de similaire.
2. N'appeler les Hooks que depuis des fonctions React, pas depuis vos propres fonctions personnalisées.

Félicitations pour avoir suivi le tutoriel et appris toutes les compétences utilisées dans ce projet. Pour approfondir votre apprentissage, consultez le cours gratuit de six heures de Scrimba [Apprendre React gratuitement](https://scrimba.com/course/glearnreact?utm_source=dev.to&utm_medium=referral&utm_campaign=greacthooks_launch_article) qui vise à faire de vous un expert React !

Bon codage !