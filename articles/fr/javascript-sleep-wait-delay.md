---
title: Tutoriel JavaScript setTimeout – Comment utiliser l'équivalent JS de sleep,
  wait, delay et pause
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-03T02:08:26.000Z'
originalURL: https://freecodecamp.org/news/javascript-sleep-wait-delay
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b4c740569d1a4ca2aee.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Tutoriel JavaScript setTimeout – Comment utiliser l'équivalent JS de sleep,
  wait, delay et pause
seo_desc: "By Mehul Mohan\nJavaScript is the language of the web. And it hasn't been\
  \ the same since ES5 was released. More and more ideas and features are being ported\
  \ from different languages and being integrated in JavaScript. \nOne of those features\
  \ are Promis..."
---

Par Mehul Mohan

JavaScript est le langage du web. Et il n'est plus le même depuis la sortie d'ES5. De plus en plus d'idées et de fonctionnalités sont portées depuis différents langages et intégrées dans JavaScript. 

L'une de ces fonctionnalités est les Promises, qui sont probablement la fonctionnalité la plus utilisée en JavaScript après la sortie d'ES5.

Mais l'une des choses qui manque à JavaScript est un moyen de "mettre en pause" l'exécution pendant un certain temps et de la reprendre plus tard. Dans cet article, je vais expliquer comment vous pouvez y parvenir et ce que signifie réellement "mettre en pause" ou "sleep" en JavaScript. 

_Spoiler : JavaScript ne se "met jamais vraiment en pause"._

## TL;DR

Voici le code à copier-coller qui fait le travail :

```js
/**
 * 
 * @param duration Entrez la durée en secondes
 */
function sleep(duration) {
	return new Promise(resolve => {
		setTimeout(() => {
			resolve()
		}, duration * 1000)
	})
}
```

Mais que se passe-t-il réellement ici ?

## setTimeout et les fausses Promises

Voyons un exemple rapide utilisant l'extrait ci-dessus (nous verrons ce qui s'y passe plus tard) :

```js
async function performBatchActions() {
	// effectuer un appel API
	await performAPIRequest()

	// dormir pendant 5 secondes
	await sleep(5)

	// effectuer à nouveau un appel API
	await performAPIRequest()
}
```

Cette fonction `performBatchActions`, lorsqu'elle est appelée, exécute simplement la fonction `performAPIRequest`, attend **environ 5 secondes**, puis appelle à nouveau la même fonction. Notez que j'ai écrit **environ 5 secondes**, et non 5 secondes.

Une note importante à préciser : le code ci-dessus ne garantit pas un sommeil parfait. Cela signifie que si vous spécifiez une durée de, disons, 1 seconde, JavaScript **ne garantit pas** qu'il commencera à exécuter le code après le sommeil exactement après 1 seconde. 

Pourquoi pas ? me demanderez-vous. Malheureusement, c'est à cause du fonctionnement des timers en JavaScript et, en général, des Event Loops. Cependant, JavaScript garantit absolument que le morceau de code après le sommeil ne s'exécutera jamais **avant** le temps spécifié. 

Nous n'avons donc pas vraiment une situation totalement indéterminée, seulement partielle. Et dans la plupart des cas, c'est dans une marge de quelques millisecondes seulement.

## JavaScript est mono-thread

Un thread unique signifie qu'un processus JavaScript ne peut pas vraiment sortir du chemin tracé. Il doit tout faire - des écouteurs d'événements aux rappels HTTP, sur le même thread principal. Et quand une chose s'exécute, une autre ne peut pas s'exécuter. 

Considérez une page web dans laquelle vous avez plusieurs boutons et vous exécutez le code ci-dessus pour simuler un sommeil de, disons, 10 secondes. Que pensez-vous qu'il va se passer ?

Rien du tout. Votre page web fonctionnera très bien, vos boutons seront réactifs, et une fois le sommeil de 10 secondes terminé, le code suivant s'exécutera. Il est donc évident que JavaScript ne bloque pas réellement tout le thread principal car s'il le faisait, votre page web se serait figée et les boutons seraient devenus non cliquables. 

Alors, comment JavaScript a-t-il réellement mis en pause un thread unique, sans jamais vraiment le mettre en pause ?

## Voici l'Event Loop

Contrairement à d'autres langages, JavaScript ne se contente pas d'exécuter le code de manière linéaire de haut en bas. C'est un langage asynchrone piloté par les événements avec des tonnes de magie sous la forme de l'Event Loop. 

Une Event Loop divise votre code en événements synchrones et certains événements - comme les timers et les requêtes HTTP. Plus précisément, il y a deux files d'attente - une task queue et une microtask queue. 

Chaque fois que vous exécutez du JS, et qu'il y a un élément asynchrone (comme un événement de clic de souris ou une Promise), JavaScript le place dans la task queue (ou microtask queue) et continue l'exécution. Lorsqu'il termine un "tick" unique, il vérifie si les task queues et microtask queue ont du travail pour lui. Si oui, il exécutera le callback/effectuera une action.

Je recommanderais vraiment à toute personne intéressée par le fonctionnement détaillé des Event Loops de regarder cette vidéo :

%[https://www.youtube.com/watch?v=8aGhZQkoFbQ]

## Conclusion

Vous êtes venu ici pour une simple instruction de sommeil en JavaScript, et vous avez fini par apprendre l'un des éléments centraux de JavaScript - les Event Loops ! Incroyable, n'est-ce pas ? 

Eh bien, si vous avez aimé l'article, allez voir [codedamn](https://codedamn.com) - une plateforme que j'ai construite pour les développeurs et les apprenants comme vous. Connectons-nous également sur les réseaux sociaux - [twitter](https://twitter.com/mehulmpt) et [Instagram](https://instagram.com/mehulmpt). À bientôt !

Peace