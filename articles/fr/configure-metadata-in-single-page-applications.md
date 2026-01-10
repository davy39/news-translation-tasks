---
title: Comment configurer les métadonnées pour une application monopage
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-20T17:20:15.000Z'
originalURL: https://freecodecamp.org/news/configure-metadata-in-single-page-applications
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/meta-data-for-spa-seo.jpg
tags:
- name: JavaScript
  slug: javascript
- name: metadata
  slug: metadata
- name: React
  slug: react
- name: SEO
  slug: seo
- name: ' Single Page Applications '
  slug: single-page-applications
seo_title: Comment configurer les métadonnées pour une application monopage
seo_desc: "By Scott Gary\nWhy Metadata Matters\nMetadata is an integral part of any\
  \ modern web app, because it's inherently tethered to search engine optimization\
  \ (SEO). \nSearch engines and their respective results page (SERPS) rely on metadata\
  \ to properly index ..."
---

Par Scott Gary

## Pourquoi les métadonnées sont importantes

Les métadonnées sont une partie intégrante de toute application web moderne, car elles sont intrinsèquement liées à l'optimisation pour les moteurs de recherche (SEO).

Les moteurs de recherche et leurs pages de résultats respectives (SERPS) s'appuient sur les métadonnées pour indexer et afficher correctement les informations relatives à chaque site.

De plus, les balises méta sont utilisées pour afficher correctement le contenu de votre site sur une plateforme de médias sociaux donnée, comme des articles ou des objets à vendre.

Pour cette raison, il est crucial de comprendre comment les métadonnées sont configurées dans une application web moderne.

L'application monopage (SPA) est une implémentation moderne d'application web incroyablement populaire. La plupart des frameworks aujourd'hui l'utilisent d'une manière ou d'une autre. La configuration des métadonnées dans les frameworks SPA les plus populaires d'aujourd'hui sera le sujet de ce tutoriel.

## L'application monopage et les métadonnées

La nature des SPA rend la configuration des métadonnées moins directe que pour les applications multipages classiques. Je vais essayer de clarifier ce sujet en décrivant les concepts clés suivants :

1. La structure d'une SPA.
2. Le problème de la modification des métadonnées dans une SPA.
3. Les solutions de métadonnées disponibles utilisant probablement les trois frameworks SPA les plus populaires : React, Svelte et Vue.

Vous devriez avoir une compréhension de base du HTML, des métadonnées et de l'un des trois frameworks SPA pour comprendre les concepts que nous allons aborder. Mais je vais garder les choses accessibles aux débutants, alors ne vous inquiétez pas !

## Comment fonctionnent les applications monopages

Avant de plonger dans le sujet, vous devez bien comprendre ce qui constitue une SPA.

Comme son nom l'indique, une application monopage consiste littéralement en une seule page HTML envoyée par le serveur. Cette page n'est qu'une coquille HTML vide et ressemblera à ceci :

```html
<!DOCTYPE html>
	<html>
		<head>
		<title>Accueil | Démystifier les métadonnées des SPA</title>
		<meta name="description" content="Comment configurer les frameworks SPA populaires pour maintenir des métadonnées de site de qualité."/>
		<link rel="stylesheet" href="./stylesheet.css" type="text/css" 			/>
		</head>
		<body>
			<script src="/bundle.min.js" type="text/javascript">					</script>
		</body>
	</html>
```

Vous vous demandez peut-être comment un site web entier est dérivé de cette coquille HTML vide.

Cela est possible car, avec la page HTML, il y aura un code JavaScript côté client extensif qui génère le contenu pour chaque page. Ce code est inclus dans la page via la balise <script>, que vous pouvez voir dans le corps de cette coquille HTML.

## Défis de la configuration des métadonnées dans une SPA

Dans la section précédente, regardez le HTML trouvé dans la balise head. Les différentes balises qui commencent par 'meta' sont nos métadonnées, ainsi que la balise title.

Ce n'est pas une représentation exhaustive des balises méta, car beaucoup d'autres sont couramment utilisées. Mais le titre et la description nous serviront bien pour ce tutoriel.

La balise title est une partie très importante des métadonnées et doit refléter un titre pertinent pour la page actuelle dans le navigateur. Pour l'instant, elle est tout à fait adaptée pour la page d'accueil. Mais que se passe-t-il lorsque l'utilisateur navigue vers une autre page ?

**Les métadonnées doivent changer en conséquence, et les frameworks SPA ne font pas cela magiquement.**

Vous ne pouvez pas changer le HTML brut, car chaque page utilise la même coquille et refléterait donc les mêmes métadonnées pour chaque page. Vous avez donc besoin d'une stratégie de codage astucieuse.

## Plugins SPA pour la maintenance des métadonnées

Les frameworks SPA sont fortement axés sur l'injection de HTML dans le DOM afin de rendre le contenu à l'écran. Cela signifie que la mise à jour de la balise body est l'objectif central du framework. Pour cette raison, la mise à jour de la balise head tend à être une fonctionnalité négligée.

Pour de nombreux frameworks SPA comme React, la communauté des développeurs a comblé le vide, créant des bibliothèques qui simplifient le processus de gestion des métadonnées.

Ce sera le sujet du reste de cet article – les bibliothèques de métadonnées et leur utilisation pour les frameworks SPA les plus populaires.

### Code JavaScript de base qui modifie les balises de métadonnées

Avant de plonger dans ces bibliothèques de métadonnées, il est crucial de comprendre qu'au bout du compte, ce n'est que du code. Alors regardons un exemple de base de code JavaScript qui peut modifier la balise title et la méta description :

```javascript
document.getElementsByTagName('meta')["description"].content = "Nouvelle méta description !";

document.title = "Nouveau titre !";
```

Les bibliothèques suivantes feront beaucoup de travail supplémentaire en plus de cet exemple de code de base, mais il est toujours bon de soulever le rideau et de voir que ce qui se passe vraiment est généralement assez simple.

## React-Helmet – Comment configurer les métadonnées dans ReactJs

React est une bibliothèque basée sur les composants pour construire des SPA évolutives. Elle offre toutes sortes de fonctionnalités que les développeurs peuvent utiliser pour construire des applications haute performance. La maintenance des métadonnées n'en fait pas partie.

Heureusement, les développeurs de la communauté React ont créé react-helmet, une bibliothèque de composants qui simplifie grandement le processus de modification de vos métadonnées dans la balise <head>.

React-helmet est maintenant considéré comme obsolète au profit de react-helmet-async, plus robuste. Nous n'entrerons pas dans les détails, mais sachez que lorsque react-helmet est mentionné de nos jours, la plupart des équipes et des développeurs utilisent en réalité react-helmet-async.

Voici un exemple de base de code react-helmet-async :

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { Helmet, HelmetProvider } from 'react-helmet-async';

const app = (
	<HelmetProvider>
	<App>
	<Helmet>
	<title>Accueil | Démystifier les métadonnées des SPA</title>
	<meta name="description" content="Comment configurer les frameworks SPA populaires pour maintenir des métadonnées de site de qualité."/>
	</Helmet>
	<h1>Bonjour le monde</h1>
	</App>
	</HelmetProvider>
);
```

Comme vous pouvez le voir, l'implémentation est assez simple. Les étapes suivantes sont effectuées :

1. Installez react-helmet-async avec npm ou yarn.
2. Importez Helmet et HelmetProvider depuis react-helmet-async
3. Enveloppez toute l'application dans le composant HelmetProvider.
4. Utilisez des balises méta HTML standard dans le composant Helmet.

Après avoir suivi ces étapes, vous pouvez maintenant utiliser le composant Helmet dans n'importe quel composant de votre application React.

Helmet a été conçu pour simplifier les choses. Selon la documentation :

> "Helmet prend des balises HTML simples et génère des balises HTML simples. C'est très simple et adapté aux débutants en React."

## Svelte-Meta-Tags – Comment configurer les métadonnées dans Svelte

Svelte est un nouveau venu dans le monde des SPA qui gagne rapidement en popularité. En bref, les gens qui l'utilisent l'adorent. La modification des métadonnées avec Svelte est gérée via la bibliothèque de composants svelte-meta-tags.

Avec une trajectoire aussi ascendante, il est important de se familiariser avec la gestion des métadonnées dans une SPA Svelte.

Svelte est un autre framework déclaratif qui abstrait une grande partie du travail lourd en vous permettant d'écrire du code 'HTML like' directement dans l'application.

Sans entrer dans ce qui distingue Svelte et pourquoi c'est une perspective intéressante (cela vaut le coup d'œil !), plongeons dans le code relatif à notre maintenance des métadonnées :

```
<script>
import { MetaTags } from 'svelte-meta-tags';
</script>
<h1>
	Métadonnées dans Svelte
</h1>
<MetaTags
	title='Accueil | Démystifier les métadonnées des SPA'
	description='Comment configurer les frameworks SPA populaires pour maintenir des métadonnées de site de qualité.'
/>
```

Les étapes pour utiliser svelte-meta-tags sont les suivantes :

1. Installez svelte-meta-tags avec npm ou yarn
2. Importez le composant MetaTags.
3. Définissez chaque propriété de métadonnées nécessaire à sa valeur respective.

Similaire en difficulté à react-helmet, le composant MetaTags est très adapté aux débutants et facile à prendre en main. Il supporte toutes les balises de métadonnées modernes (pour une liste complète, consultez la documentation).

## Vue-Meta – Comment configurer les métadonnées dans Vue.js

Vue existe depuis un peu plus longtemps que Svelte, mais est encore environ un an plus jeune que React. Au cours des dernières années, Vue a connu un regain de popularité, c'est pourquoi je l'ai choisi comme l'un des trois principaux frameworks SPA à examiner.

Comme les deux frameworks précédents, Vue est déclaratif et basé sur les composants. Mais l'implémentation des bibliothèques de plugins est légèrement différente. Regardons cela.

Vue utilise un fichier de configuration appelé **main.js** qui initialise l'application Vue. Puisque nous allons utiliser le plugin vue-meta dans toute l'application, c'est ici que nous voudrons importer notre plugin.

Dans Vue, vous faites cela avec la méthode `Vue.use()`, et cela ressemblera à ceci :

```
Main.js
import Vue from 'vue';
import VueMeta from 'vue-meta';
import App from './App.vue';

Vue.use(VueMeta);
	new Vue({
	el: '#app',
	render: h => h(App)
});
```

Maintenant que nous avons importé le composant VueMeta, nous pouvons lui envoyer des données en exportant une propriété appelée **metaInfo** depuis n'importe quel composant Vue.

Voici un exemple de composant Vue d'atterrissage qui utilise le plugin vue-meta :

```
Landing.vue
<template>
	<div>Métadonnées SPA</div>
</template>
<script>
	export default {
		name: 'landing',
		data () {
		return {}
		},
		metaInfo: {
		title: 'Accueil | Démystifier les métadonnées des SPA',
		description: 'Comment configurer les frameworks SPA populaires pour maintenir des métadonnées de site de qualité.'
		}
		}
</script>
```

Chaque composant Vue exporte un objet à utiliser par l'application Vue, et puisque nous avons importé le plugin VueMeta dans le fichier **main.js**, Vue recherchera la propriété metaInfo que nous avons exportée depuis notre composant **landing**.

Tout ce que nous avons à faire est de lui fournir des données, et nos balises méta sont générées pour nous !

## SEO des SPA et métadonnées – Conclusion

Pour chacun des trois frameworks SPA, nous avons vu des exemples de code qui aboutiront aux balises de métadonnées trouvées dans le balisage HTML au début de ce tutoriel.

La modification des métadonnées dans les applications SPA n'est pas aussi simple que pour les applications multipages, même celles qui sont dynamiques par nature. Comprendre ce concept facilitera la vie tout en utilisant la myriade de frameworks SPA disponibles aujourd'hui.

Les métadonnées sont une partie intégrante de toute application web moderne. Espérons qu'après avoir lu ce tutoriel, vous vous sentirez confiant pour appliquer ce concept à votre prochaine construction SPA.

Intéressé à en apprendre davantage sur les métadonnées des applications monopages et l'optimisation pour les moteurs de recherche ? Lisez notre guide complet sur le [SEO pour les SPA](https://www.ohmycrawl.com/spa-seo/) pour monter en niveau et comprendre pleinement comment cela fonctionne.