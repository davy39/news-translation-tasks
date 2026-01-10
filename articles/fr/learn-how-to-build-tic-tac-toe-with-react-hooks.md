---
title: Apprenez à créer un Tic-Tac-Toe avec React Hooks
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-29T13:49:57.000Z'
originalURL: https://freecodecamp.org/news/learn-how-to-build-tic-tac-toe-with-react-hooks
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-26-at-21.27.58.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
- name: React
  slug: reactjs
- name: Scrimba
  slug: scrimba
seo_title: Apprenez à créer un Tic-Tac-Toe avec React Hooks
seo_desc: 'By Per Harald Borgen

  If you have a good understanding of HTML, CSS, JavaScript, and React you might be
  wondering where to go next on your learning journey. So why not check out Scrimba''s
  brand new, free tutorial on how to build the classic tic-tac-to...'
---

Par Per Harald Borgen

Si vous avez une bonne compréhension de HTML, CSS, JavaScript et React, vous vous demandez peut-être où aller ensuite dans votre parcours d'apprentissage. Alors pourquoi ne pas consulter [le tout nouveau tutoriel gratuit de Scrimba](https://scrimba.com/course/greactgame?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) sur la création du jeu classique Tic-Tac-Toe en React ?

[![Jeu entièrement fonctionnel](https://dev-to-uploads.s3.amazonaws.com/i/xtcbjygjr8s9in2u3nnv.png)](https://scrimba.com/course/greactgame?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Cliquez ci-dessus pour accéder au tutoriel._

L'exemple de jeu est tiré des tutoriels officiels de React mais est mis à jour en utilisant les hooks React - le dernier sujet à la mode dans le monde React.

Cet article vous donne un aperçu du tutoriel et vous permet de cliquer sur les screencasts et de jouer avec le code à tout moment.

Si vos compétences en HTML, CSS, JavaScript ou React vous semblent fragiles, ne craignez rien - Scrimba propose une large gamme de tutoriels pour vous mettre à niveau. Nous recommandons les cours suivants pour vous préparer au tutoriel Tic-Tac-Toe :

- [Cours accéléré HTML & CSS](https://scrimba.com/course/ghtmlcss?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) avec Kevin Powell
- [Introduction à Javascript](https://scrimba.com/course/gintrotojavascript?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) avec Dylan C. Israel
- [Apprendre React gratuitement](https://scrimba.com/course/glearnreact?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) avec Bob Ziroll

Dans le style typique de Scrimba, le tutoriel "Créer un Tic-Tac-Toe avec React Hooks" contient de nombreux défis interactifs tout au long du parcours, afin que vous assimiliez vos connaissances et vous sentiez comme un magicien des hooks à la fin.

Le cours est dirigé par Thomas Weibenfalk, un développeur passionné, designer et instructeur de codage originaire de Suède. Thomas adore enseigner le développement front-end, surtout React, ce qui fait de lui l'enseignant idéal pour vous guider dans cette expérience d'apprentissage.

En supposant que vous êtes prêt à vous lancer avec le Tic-Tac-Toe, commençons !

## Introduction

[![Tic-tac-toe avec les hooks React](https://dev-to-uploads.s3.amazonaws.com/i/e9mee46gi4pz43um8h1t.png)](https://scrimba.com/p/pgGEGtW/cPkGD8Sm?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)

Dans [le premier scrim](https://scrimba.com/p/pgGEGtW/cPkGD8Sm?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), Thomas nous parle de ses plans pour le tutoriel et partage la [Documentation officielle de React](https://reactjs.org/tutorial/tutorial.html), à laquelle nous pouvons nous référer pour une explication plus détaillée des fonctionnalités utilisées pour construire le jeu.

En plus de nous expliquer la structure des fichiers qu'il a implémentée pour l'application, Thomas nous donne également un premier aperçu du produit final. Cliquez sur l'image ci-dessus pour visiter le cast.

## Échafaudage des composants

[Ensuite](https://scrimba.com/p/pgGEGtW/cV8eB8fp?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), Thomas nous explique comment configurer les fichiers Board.js, Game.js et Square.js nécessaires pour créer le jeu. Nous voyons également comment importer Game.js dans le fichier App.js.

```js
import React from "react";
import Game from "./components/Game";

const App = () => <Game />;

export default App;
```

## Composant Square et déstructuration des props

Dans [le prochain scrim](https://scrimba.com/p/pgGEGtW/cKp4eRfq?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), nous créons notre composant square en utilisant JSX pour ajouter un bouton :

```js
const Square = (props) => (
	<button onClick={props.onClick}>{props.value}</button>
);
```

Pour notre premier défi, Thomas nous encourage à déstructurer les props dans notre composant. [Cliquez ici](https://scrimba.com/p/pgGEGtW/cKp4eRfq?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) pour accéder au cast et essayer le défi.

## Composant Board et fonctions d'échafaudage

Il est maintenant temps de créer [le composant board](https://scrimba.com/p/pgGEGtW/cypaG6CZ?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) en important le composant square et en ajoutant neuf instances de celui-ci au board (notez que nous allons refactoriser cela avec une boucle pour améliorer le code plus tard) :

```js
<div>
	<Square value="1" onClick={() => onClick("dummy value")} />
	<Square value="2" onClick={() => onClick("dummy value")} />
	<Square value="3" onClick={() => onClick("dummy value")} />
	<Square value="4" onClick={() => onClick("dummy value")} />
	<Square value="5" onClick={() => onClick("dummy value")} />
	<Square value="6" onClick={() => onClick("dummy value")} />
	<Square value="7" onClick={() => onClick("dummy value")} />
	<Square value="8" onClick={() => onClick("dummy value")} />
	<Square value="9" onClick={() => onClick("dummy value")} />
</div>
```

Thomas prépare également les fonctions dont nous avons besoin dans Game.js, que nous compléterons plus tard.

## Style des carrés

[![app avec des carrés stylisés](https://dev-to-uploads.s3.amazonaws.com/i/2zhixfxneekxecwxi2vn.png)](https://scrimba.com/p/pgGEGtW/ceMPzwhB?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Cliquez sur l'image pour accéder au cast._

[Ensuite](https://scrimba.com/p/pgGEGtW/ceMPzwhB?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), nous stylisons nos carrés en utilisant la prop `style` par défaut :

```js
const style = {
	background: "lightblue",
	border: "2px solid darkblue",
	fontSize: "30px",
	fontWeight: "800",
	cursor: "pointer",
	outline: "none",
};

const Square = ({ value, onClick }) => (
	<button style={style} onClick={onClick}>
		{value}
	</button>
);
```

## Style du plateau

[![app avec un plateau stylisé](https://dev-to-uploads.s3.amazonaws.com/i/ynvasbhvjvj5kr9g5fe4.png)](https://scrimba.com/p/pgGEGtW/c8rJyKcD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Cliquez sur l'image pour accéder au scrim._

Maintenant que nos carrés sont prêts, il est temps de [styliser le plateau](https://scrimba.com/p/pgGEGtW/c8rJyKcD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article). Thomas nous lance en créant à nouveau un objet de style, cette fois avec CSS grid :

```js
const style = {
	border: "4px solid darkblue",
	borderRadius: "10px",
	width: "250px",
	height: "250px",
	margin: "0 auto",
	display: "grid",
	gridTemplate: "repeat(3, 1fr) / repeat(3, 1fr)",
};
```

Notre défi maintenant est d'appliquer l'objet de style au plateau. Rendez-vous [au scrim](https://scrimba.com/p/pgGEGtW/c8rJyKcD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) pour essayer.

N'oubliez pas, bien que Thomas ait fourni quelques excellentes options de style, Scrimba est entièrement interactif, vous êtes donc libre de personnaliser votre jeu comme vous le souhaitez - laissez libre cours à votre imagination !

## La fonction calculateWinner expliquée

```js
export function calculateWinner(squares) {
	const lines = [
		[0, 1, 2],
		[3, 4, 5],
		[6, 7, 8],
		[0, 3, 6],
		[1, 4, 7],
		[2, 5, 8],
		[0, 4, 8],
		[2, 4, 6],
	];
	for (let i = 0; i < lines.length; i++) {
		const [a, b, c] = lines[i];
		if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
			return squares[a];
		}
	}
	return null;
}
```

[Ensuite](https://scrimba.com/p/pgGEGtW/cBLrMvS2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), Thomas explique la fonction très importante `calculateWinner()`, qui est tirée du tutoriel original de [reactjs.org](https://reactjs.org/tutorial/tutorial.html). Rendez-vous [au cast](https://scrimba.com/p/pgGEGtW/cBLrMvS2?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) pour explorer la fonction et comprendre comment elle fonctionne.

## Créer des états et les remplir avec des données initiales

Dans le prochain [scrim](https://scrimba.com/p/pgGEGtW/c4Pw97tV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), nous commençons à créer la logique du jeu.

Nous commençons par ajouter un hook appelé `useState` dans Game.js et créons des états pour définir un plateau vide et spécifier le prochain joueur. Enfin, nous ajoutons `const winner`, qui nous indique si le dernier coup était un coup gagnant :

```js
const [board, setBoard] = useState(Array(9).fill(null));
const [xIsNext, setXisNext] = useState(true);
const winner = calculateWinner(board);
```

Dans Board.js, nous supprimons nos carrés rendus manuellement et les remplaçons par des carrés mappés comme promis précédemment. [Cliquez ici](https://scrimba.com/p/pgGEGtW/c4Pw97tV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) pour voir cela en détail :

```js
const Board = ({ squares, onClick }) => (
	<div style={style}>
		{squares.map((square, i) => (
			<Square key={i} value={square} onClick={() => onClick(i)} />
		))}
	</div>
);
```

## Créer la fonction handleClick

[Ensuite](https://scrimba.com/p/pgGEGtW/c67knwTy?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), nous créons la fonction `handleClick()`, qui effectue les calculs lorsque nous faisons un coup :

```js
const handleClick = (i) => {
	const boardCopy = [...board];
	// Si l'utilisateur clique sur une case occupée ou si le jeu est gagné, retourner
	if (winner || boardCopy[i]) return;
	// Placer un X ou un O dans la case cliquée
	boardCopy[i] = xIsNext ? "X" : "O";
	setBoard(boardCopy);
	setXisNext(!xIsNext);
};
```

## Fonction renderMoves et le dernier JSX

[![Jeu entièrement fonctionnel](https://dev-to-uploads.s3.amazonaws.com/i/xtcbjygjr8s9in2u3nnv.png)](https://scrimba.com/p/pgGEGtW/cNq2EQAL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Cliquez ci-dessus pour accéder au tutoriel._

[Dans ce scrim](https://scrimba.com/p/pgGEGtW/cNq2EQAL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), nous créons le JSX qui rend le jeu jouable.

```js
<>
  <Board squares={board} onClick={handleClick} />
  <div style={styles}>
    <p>
      {winner ? "Gagnant : " + winner : "Prochain joueur : " + (xIsNext ? "X" : "O")}
    </p>
  </div>
</>
```

Nous avons maintenant toutes les connaissances nécessaires pour créer un jeu de Tic-Tac-Toe entièrement fonctionnel avec React hooks !

## BONUS : Implémenter le voyage dans le temps

[![Fonctionnalité de voyage dans le temps en action](https://dev-to-uploads.s3.amazonaws.com/i/myoj1edcpkv3gx0ry7xj.png)](https://scrimba.com/p/pgGEGtW/cBLr6Df6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article)
_Cliquez sur l'image pour accéder au tutoriel bonus._

[Dans le scrim bonus](https://scrimba.com/p/pgGEGtW/cBLr6Df6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article), nous faisons passer notre jeu au niveau supérieur en implémentant le voyage dans le temps pour revoir les coups effectués tout au long du jeu. Cliquez ici pour obtenir les bonus de ce tutoriel.

Voilà donc un jeu de Tic-Tac-Toe entièrement fonctionnel utilisant React hooks ! J'espère que vous avez trouvé ce tutoriel utile. N'oubliez pas que vous pouvez vous y référer à tout moment pour rafraîchir votre mémoire sur les sujets abordés ou jouer avec le code dans les screencasts interactifs.

Ensuite, pourquoi ne pas consulter certains des nombreux autres tutoriels disponibles sur [Scrimba ?](https://scrimba.com/?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgame_launch_article) Avec une large gamme de sujets, il y en a pour tous les goûts.

Bon apprentissage :)

%[https://www.youtube.com/watch?v=Z5RbPrK4VqM]