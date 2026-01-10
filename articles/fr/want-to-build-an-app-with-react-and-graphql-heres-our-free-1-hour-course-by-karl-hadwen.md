---
title: Vous voulez créer une application avec React et GraphQL ? Voici notre cours
  gratuit d'1 heure par Karl Hadwen
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-18T20:00:00.000Z'
originalURL: https://freecodecamp.org/news/want-to-build-an-app-with-react-and-graphql-heres-our-free-1-hour-course-by-karl-hadwen
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-09-at-18.33.24.png
tags:
- name: GraphQL
  slug: graphql
- name: React
  slug: react
- name: Scrimba
  slug: scrimba
seo_title: Vous voulez créer une application avec React et GraphQL ? Voici notre cours
  gratuit d'1 heure par Karl Hadwen
seo_desc: 'By Per Harald Borgen

  If you''ve ever wondered how to connect React.js & GraphQL, then Scrimba''s hot
  one hour course is for you! The course jumps right into using a wide range of technologies
  to build a fast application with a concise amount of code - ...'
---

Par Per Harald Borgen

Si vous vous êtes déjà demandé comment connecter React.js et GraphQL, alors le cours d'une heure de Scrimba est fait pour vous ! Le cours plonge directement dans l'utilisation d'une large gamme de technologies pour construire une application rapide avec une quantité concise de code - qu'y a-t-il à ne pas aimer ?

## Pourquoi apprendre React et GraphQL ?

GraphQL a un temps de construction et d'itération plus rapide que les API REST et réduit la quantité de données envoyées depuis le serveur. Cela signifie des applications plus rapides et plus réactives - un must pour tout développeur React.

## Présentation de l'instructeur

Ce cours vous est présenté par Karl Hadwen - un développeur JavaScript et React avec plus de dix ans d'expérience. Karl anime également une [chaîne YouTube](https://www.youtube.com/channel/UC1DUQiZduv_yNZy0O7n_iHA) enseignant React, JavaScript et GraphQL, il est donc la personne idéale pour vous aider à améliorer vos compétences en React et GraphQL.

## Qu'est-ce qui est couvert dans le cours ?

Dans ce cours, nous apprendrons à construire une application front-end amusante qui utilise React, GraphQL et Apollo pour afficher des personnages, des faits et des images de Pokemon ! Le cours est interactif et direct, ce qui signifie que vous construirez quelque chose comme ceci en un rien de temps :

[![UI de l'application Pokemon](https://dev-to-uploads.s3.amazonaws.com/i/m93x4nidm7dfqsnaohbm.png)](https://scrimba.com/p/pdqXpfD/ckRd6NU9?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans la pure tradition de Scrimba, le cours de Karl est rempli de défis de codage interactifs pour vous aider à appliquer vos connaissances et à ancrer votre apprentissage, alors rendez-vous [sur Scrimba](https://scrimba.com/course/greactgraphql?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) maintenant et continuez à lire pour en savoir plus.

## Bienvenue dans le cours

Dans [le premier scrim](https://scrimba.com/p/pdqXpfD/ckRd6NU9?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), Karl nous présente les technologies que nous utiliserons dans le cours, qui sont :

- React
- GraphQL
- Apollo
- CSS
- l'API ouverte Pokemon.

## Installation de nos dépendances et création de notre projet squelette

[![Dépendances Apollo, GraphQL et React ajoutées au projet](https://dev-to-uploads.s3.amazonaws.com/i/an3cm74ty42qt0e4ptsm.png)](https://scrimba.com/p/pdqXpfD/ckRdVWSD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Cliquez sur l'image pour accéder au cours._

Maintenant, il est temps de [démarrer notre projet](https://scrimba.com/p/pdqXpfD/ckRdVWSD?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article). Tout d'abord, nous installons les dépendances Apollo, GraphQL et React. Ensuite, nous construisons les fichiers et dossiers dont nous avons besoin pour notre projet :

```js
import React from "react";
import { render } from "react-dom";
import { App } from "./App";

render(<App />, document.getElementById("root"));
```

## Donnons vie à notre application !

Maintenant, il est temps de donner vie à notre application en ajoutant à notre fichier d'application et en atteignant le serveur GraphQL :

```js
export function App() {
	const client = new ApolloClient({
		uri: "https://graphql-pokemon.now.sh",
	});

	return <p>Je suis un Pokemon</p>;
}
```

[Ce scrim](https://scrimba.com/p/pdqXpfD/c8qgp9TZ?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) nous guide à travers les étapes suivantes pour permettre à notre utilisateur d'interagir avec notre application :

- configuration du client Apollo
- construction du `ApolloProvider` et passage du client en tant que prop
- ajout de notre balise `<main>` et `PokemonsContainer`

## Parlons de GraphQL

[![champs qui peuvent être retournés par l'API ouverte pokemon](https://dev-to-uploads.s3.amazonaws.com/i/trsebt5rtu5zyetzn40b.png)](https://scrimba.com/p/pdqXpfD/cmmdmvc6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Cliquez sur l'image pour accéder au cours._

[Ce scrim](https://scrimba.com/p/pdqXpfD/cmmdmvc6?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) examine [le serveur GraphQL](https://graphql-pokemon.now.sh/) que nous utiliserons dans notre application. L'avantage de GraphQL est qu'il nous permet de demander uniquement les champs dont nous avons besoin depuis l'objet, contrairement à REST qui envoie toutes les informations disponibles. Karl nous montre cela en action en nous guidant à travers la construction et l'exécution de notre première requête GraphQL.

## Utilisation de notre composant conteneur pour mapper nos Pokemons !

Dans [le prochain scrim](https://scrimba.com/p/pdqXpfD/c4MGWJf8?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), nous construisons notre conteneur principal afin de pouvoir boucler sur nos Pokemons.

Karl commence par nous montrer comment obtenir les données de l'API Pokemon :

```js
const { data: { pokemons = [] } = {} } = useQuery(GET_POKEMONS, {
	variables: { first: 9 },
});
```

Ensuite, il est temps pour un défi interactif : passer deux props, la clé et `pokemon`. Rendez-vous sur [le cours](https://scrimba.com/p/pdqXpfD/c4MGWJf8?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) pour essayer le défi vous-même.

## Ajout d'une requête GraphQL et création de notre composant Pokemon !

[![Texte alternatif](https://dev-to-uploads.s3.amazonaws.com/i/09rwvu8lyfclzw1yv46o.png)](https://scrimba.com/p/pdqXpfD/cND38EfL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans [ce scrim](https://scrimba.com/p/pdqXpfD/cND38EfL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), nous commençons par construire notre requête GraphQL :

```js
import gql from "graphql-tag";

export const GET_POKEMONS = gql`
	query pokemons($first: Int!) {
		pokemons(first: $first) {
			id
			name
			image
			maxHP
			maxCP
			attacks {
				special {
					name
					damage
				}
			}
		}
	}
`;
```

Ensuite, Karl nous donne les bases de notre composant Pokemon :

```js
export function Pokemon({ pokemon }) {
	return <p>{pokemon.name}</p>;
}
```

Notre défi maintenant est de construire le composant Pokemon afin qu'il affiche toutes les informations récupérées depuis l'API. Cliquez sur [le cours](https://scrimba.com/p/pdqXpfD/cND38EfL?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) maintenant pour essayer.

## Finalisation de notre composant Pokemon

[Ensuite,](https://scrimba.com/p/pdqXpfD/cVnyLyfW?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) Karl nous explique comment mapper jusqu'à trois des multiples attaques d'un Pokemon :

```js
{
	pokemon.attacks.special.slice(0, 3).map((attack) => <span></span>);
}
```

Nous avons également un mini-défi consistant à ajouter une clé dans notre div `pokemon__attacks`. [Cliquez ici](https://scrimba.com/p/pdqXpfD/cVnyLyfW?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) pour essayer.

## Stylisons notre application !

[![Composant Pokemon stylisé](https://dev-to-uploads.s3.amazonaws.com/i/3lsg12e2b8dc0uwmjhe7.png)](https://scrimba.com/p/pdqXpfD/c8qgEqUV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Cliquez sur l'image pour accéder au cours._

Maintenant que nous avons créé notre application, il est temps de la styliser. Dans [ce scrim complet](https://scrimba.com/p/pdqXpfD/c8qgEqUV?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article), Karl nous guide à travers le stylisme de tous les éléments de notre application Pokemon et nous donne quelques défis CSS en cours de route. Bien sûr, les styles suggérés par Karl sont ses préférences personnelles - vous pourriez styliser votre application comme vous le souhaitez !

```css
.container .pokemon {
	width: 49%;
	background-color: #fff;
	background-clip: border-box;
	border: 1px solid rgba(0, 0, 0, 0.125);
	border-radius: 0.25rem;
	box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
	overflow: hidden;
	margin-bottom: 20px;
}
```

## Stylisation responsive de notre application

[![application stylisée de manière responsive sur un écran extra petit](https://dev-to-uploads.s3.amazonaws.com/i/tbtvim617msylhr92ld3.png)](https://scrimba.com/p/pdqXpfD/c2K7EgUa?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article)
_Cliquez sur l'image pour accéder au cours._

Dans [le dernier scrim](https://scrimba.com/p/pdqXpfD/c2K7EgUa?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) du cours, nous découvrons comment styliser notre application de manière responsive avec des requêtes média :

```css
@media (max-width: 800px) {
	.container .pokemon {
		width: 100%;
	}
}

@media (max-width: 400px) {
	.container .pokemon__attacks,
	.container .pokemon__meta {
		flex-wrap: wrap;
	}

	.container .pokemon__meta span,
	.container .pokemon__attacks span,
	.container .pokemon {
		width: 100%;
	}

	.container .pokemon__meta span {
		margin-bottom: 10px;
	}
}
```

Maintenant que c'est fait, notre application a fière allure sur toutes les tailles de navigateur.

Félicitations pour avoir terminé le cours - vous avez créé et stylisé une application React entièrement fonctionnelle qui interagit avec un serveur GraphQL, ce qui est une grande réalisation !

Espérons que vous avez appris beaucoup de choses tout au long de ce cours et que vous aurez l'occasion d'appliquer vos nouvelles connaissances à d'autres applications bientôt. En attendant, pourquoi ne pas vous rendre sur [Scrimba](https://scrimba.com?utm_source=dev.to&utm_medium=referral&utm_campaign=greactgraphql_launch_article) pour voir quels autres cours sont proposés ? Vous pourriez même les attraper tous :)

Quoi que vous décidiez d'apprendre ensuite, bon codage !


%[https://www.youtube.com/watch?v=w04_SuqvpzY]