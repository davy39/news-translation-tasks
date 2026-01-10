---
title: Avons-nous encore besoin des frameworks JavaScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-04T16:58:19.000Z'
originalURL: https://freecodecamp.org/news/do-we-still-need-javascript-frameworks-42576735949b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aZspWn6gQ0bzfIy7nWswmw.png
tags:
- name: Angular
  slug: angular
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Avons-nous encore besoin des frameworks JavaScript ?
seo_desc: 'By Luke Joliat

  As a web developer, I try to assess my toolbox regularly and determine if I can
  do without this or that tool. Recently, I have been investigating just how easy
  it is to develop a complex front end application without a front end framew...'
---

Par Luke Joliat

En tant que développeur web, j'essaie d'évaluer régulièrement ma boîte à outils et de déterminer si je peux me passer de tel ou tel outil. Récemmment, j'ai étudié à quel point il est facile de développer une application front-end complexe sans framework front-end.

#### **Qu'est-ce qu'un framework JavaScript ?**

En termes simples, un framework JavaScript est un outil que vous pouvez utiliser pour développer des applications web avancées, en particulier des SPAs.

À l'époque, les développeurs web implémentaient la logique front-end en s'appuyant fortement sur vanilla JS et jQuery. Mais, à mesure que les applications front-end devenaient de plus en plus complexes, les outils ont évolué pour répondre à cette complexité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PNlbgb05IwSxOhAz0aA2rg.png)

Les frameworks populaires aujourd'hui ont quelques points communs principaux. La plupart des frameworks/bibliothèques front-end, de Vue à React, fournissent une combinaison des éléments suivants :

* Synchronisation de l'état et de la vue
* Routage
* Un système de templates
* Des composants réutilisables

#### **Les frameworks sont-ils encore nécessaires ?**

Cela dépend de la manière dont vous insistez sur le mot _nécessaire_. Beaucoup soutiendraient que les frameworks front-end ne sont pas et n'ont jamais été nécessaires. Ce sont des outils très utiles, cependant.

La question est donc : les frameworks sont-ils le jQuery d'aujourd'hui ? Les problèmes qu'ils résolvent seront-ils abordés par des changements comme ceux apportés à l'API DOM ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*rSC0B8I9cLTDhiArUeildw.jpeg)

Il est difficile de le dire, mais les avancées en JS natif, la spécification des composants web et les outils de build facilement configurables ont rendu le développement d'une SPA sans framework aussi facile que jamais.

Pour approfondir cette question, j'ai développé une application monopage en utilisant uniquement vanilla JavaScript, des composants web natifs et Parcel. Il y a eu quelques pièges et difficultés en cours de route qui ont mis en lumière les forces des frameworks JS.

En même temps, une fois que j'ai surmonté les obstacles initiaux, j'ai été surpris par la simplicité de créer une application monopage avec juste vanilla JS.

#### Aperçu

L'application est simple. Il s'agit d'une application de recettes avec des capacités CRUD de base. L'utilisateur peut créer, modifier, supprimer, ajouter aux favoris et filtrer une liste de recettes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qJ5c-HSAPNo5CW8L_K8j1A.png)
_L'écran d'accueil_

![Image](https://cdn-media-1.freecodecamp.org/images/1*wpy9DOp8LnB2JrQ8rcHKow.png)
_Écran de création de recette_

#### Composants

Créer un composant web est également simple. Vous créez une classe qui étend `HTMLElement` (ou `HTMLParagraphElement`, etc.), puis utilisez cette classe pour définir un élément personnalisé.

Vous pouvez également utiliser des hooks de cycle de vie tels que _connectedCallback, disconnectedCallback, attributeChangedCallback._

#### Routage

Le routage pour l'application de recettes est également assez simple. Étant donné un événement de navigation, je définis le contenu de l'application sur le composant web correspondant.

Initialement, j'utilisais un package npm appelé Vanilla JS Router. Avec l'[API d'historique du navigateur](https://developer.mozilla.org/en-US/docs/Web/API/History), ce n'est pas si complexe d'implémenter le vôtre en moins de 100 lignes de code ! Note : Je n'implémente pas de logique vraiment complexe comme les gardes de route.

C'est un résumé rapide. Je veux garder cet article à une longueur raisonnable. Je pourrais écrire un article de suivi avec une explication plus approfondie de l'application. J'ai implémenté quelques fonctionnalités amusantes comme le défilement infini, un téléchargeur personnalisé de glisser-déposer, et plus encore !

### Rétrospective

Après avoir créé l'application, j'ai pris le temps de réfléchir aux avantages et inconvénients de tout le processus du début à la fin. Je commencerai par les mauvaises nouvelles.

### Inconvénients

#### La spécification est encore en évolution

![Image](https://cdn-media-1.freecodecamp.org/images/1*wCpfEUhah-4JgDR068I3hQ.png)

La spécification des composants web est à la fois ancienne et nouvelle. Elle existe depuis beaucoup plus longtemps que je ne le pensais initialement. _Les composants web ont été [introduits par Alex Russell](https://en.wikipedia.org/wiki/Web_Components#cite_note-16) à la conférence Fronteers 2011 pour la première fois._ Cependant, l'élan derrière les composants web a vraiment grandi au cours de l'année ou des deux dernières années. Ainsi, il y a encore beaucoup de bouleversements dans la spécification. Par exemple, les imports HTML ont été abandonnés, bien que la plupart de la documentation/ressources les mentionnent encore.

#### Tests

![Image](https://cdn-media-1.freecodecamp.org/images/1*BuoxeY29sd0U2GYmJ29GVA.png)

Il n'y a pas beaucoup de ressources dédiées pour tester les composants web natifs. Il existe quelques outils prometteurs comme [skatejs ssr](https://github.com/skatejs/skatejs/tree/master/packages/ssr) et le [web component tester](https://github.com/Polymer/tools/tree/master/packages/web-component-tester) de Polymer. Mais ces outils sont vraiment conçus pour être utilisés avec leurs bibliothèques respectives. Cela présente certaines difficultés pour une utilisation avec des composants web natifs.

#### Détection des changements

Avoir un système sous-jacent qui maintient automatiquement la vue synchronisée avec le modèle de données est incroyable. C'est ce qui a attiré beaucoup de gens vers Angular et d'autres frameworks en premier lieu.

Maintenir l'état synchronisé avec la vue n'est pas si difficile à petite échelle. Mais cela peut rapidement devenir incontrôlable, et vous vous retrouvez à ajouter des tonnes d'écouteurs d'événements et de sélecteurs de requête.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xlSabT49zJjvW6xjrgykJg.png)

#### Le Shadow DOM

Je suis vraiment partagé concernant le Shadow DOM. D'une part, j'adore l'idée d'encapsulation. C'est un modèle de conception sensé, rend votre cascade de styles plus gérable, simplifie vos préoccupations, etc. Cependant, il pose également des problèmes lorsque vous souhaitez que certaines choses pénètrent cette encapsulation (comme une feuille de style partagée), et il existe des débats en cours sur [la meilleure façon de faire cela.](https://www.smashingmagazine.com/2016/12/styling-web-components-using-a-shared-style-sheet/)

#### Génération de structures DOM

Une partie de la magnificence des frameworks/bibliothèques comme Angular et React est qu'ils sont maîtres de leur DOMaine. C'est-à-dire qu'ils sont excellents pour rendre et re-rendre efficacement des structures dans le DOM. D'après le [blog Angular University](https://blog.angular-university.io/why-angular-angular-vs-jquery-a-beginner-friendly-explanation-on-the-advantages-of-angular-and-mvc/) :

> _Angular ne génère pas de HTML puis ne le passe pas au navigateur pour qu'il soit analysé, au lieu de cela Angular génère des structures de données DOM directement !_

Angular, par exemple, contrairement à jQuery, rend les structures de données DOM directement. C'est-à-dire, au lieu de passer du HTML au navigateur pour qu'il soit analysé, puis rendu en structures de données DOM. Cela est plus performant car cela élimine cette étape d'analyse. Le Virtual DOM est également très utile, car il vous évite de tout re-rendre chaque fois que vous devez mettre à jour votre vue.

### Avantages

D'autre part, il y a des avantages indéniables à développer des applications de cette manière :

#### Taille du bundle

Le produit final peut être (insistons sur _peut_) tellement plus petit et plus compact que tout ce qui est développé avec un framework moderne. Par exemple, la build finale de mon application de recettes entièrement fonctionnelle était moins de la moitié de la taille d'une build Angular fraîche.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Z0SqFAFZ2StMTBcHK_hvuA.png)
_Taille du bundle Angular_

![Image](https://cdn-media-1.freecodecamp.org/images/1*EvAcQ6E__FUVjwiCkxdRmw.png)
_Bundle de l'application de recettes_

![Image](https://cdn-media-1.freecodecamp.org/images/1*dCm_mrJfj1B2761WIb8vQA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RLLfjCifUd6QwuXIQhYggg.png)

Note : Ce sont les tailles de bundle optimisées et mises à jour.

#### Compréhension

![Image](https://cdn-media-1.freecodecamp.org/images/1*YkPg-F5x1xzLjJ6vQ0KIjA.png)

Si vous n'avez vraiment développé qu'avec un framework et son CLI, ce peut être un excellent exercice de créer une application web sans outils supplémentaires. En tant que personne qui souhaite atteindre un certain niveau de maîtrise (dans la mesure du possible) du développement web, il a été essentiel pour moi d'acquérir plus d'expérience pratique avec les outils de build, les API du navigateur, les modèles de conception, etc.

#### Performance

![Image](https://cdn-media-1.freecodecamp.org/images/1*tEpzCAu3z7YMMiJayzjKGQ.jpeg)

Ce que ces frameworks et bibliothèques front-end font en coulisses est incroyable. Cependant, vous pouvez payer un prix en termes de performance si vous décidez de les utiliser ; il n'y a pas de repas gratuit. Il existe de nombreux freins potentiels à la performance à grande échelle : qu'il s'agisse de re-rendus inutiles, d'écouteurs redondants, de comparaisons d'objets profonds ou de manipulations DOM inutiles et volumineuses. Vous pouvez éliminer beaucoup de complexité ici en implémentant les choses à partir de zéro.

Les équipes Angular et React semblent conscientes de ces pièges et ont fourni des choses comme les remplacements de méthode _shouldUpdate_ et la détection de changement _onPush_ comme moyen d'optimiser davantage les performances.

#### Simplicité et propriété du code

![Image](https://cdn-media-1.freecodecamp.org/images/1*e7jkx0XuOzlMh9jypofNgQ.jpeg)

Vous prenez un risque chaque fois que vous intégrez du code tiers. Ce risque est réduit avec des bibliothèques/frameworks éprouvés, mais jamais vraiment éliminé. Si vous pouvez vous en sortir en écrivant du code vous-même ou avec votre équipe, vous pouvez réduire ce risque et maintenir une base de code que vous connaissez de fond en comble.

#### Notes et anecdotes intéressantes

J'ai adoré travailler avec Parcel. Il m'a semblé un peu plus limité que Webpack à certains moments lorsque j'ai essayé de contourner certains cas particuliers, mais j'ai trouvé que la ligne de conduite 'zero config' se vérifiait, pour la plupart.

Il est également clair pour moi que beaucoup qualifient React de 'bibliothèque' et Vue de 'framework progressif'. Bien que je comprenne les raisons de cela, je pense que React, Vue et Angular résolvent beaucoup des mêmes problèmes. Ainsi, je les considère tous ensemble sous le terme 'frameworks'.

Pourquoi ne pas utiliser Stencil ou Polymer ? Je voulais éviter l'utilisation de packages, bibliothèques et frameworks autant que possible. Je voulais voir jusqu'où les standards web avaient évolué pour répondre au développement moderne (à part les outils de build).

Je suis sûr qu'il existe de nombreuses autres façons de développer une SPA ou une application front-end en général sans framework ou bibliothèque majeur, j'ai essayé une méthode ici, et j'adorerais en entendre parler d'autres !

### Résumé

Une excellente heuristique pour la décision d'utiliser ou non un framework est ce que j'appelle, 'le point de bascule'. Il arrive un moment, à mesure que votre application grandit, où vous finissez par créer votre propre framework afin de réutiliser la fonctionnalité et la structure. Par exemple, vous avez un tas de formulaires et vous voulez créer une logique réutilisable pour la validation réactive.

Si vous arrivez à ce point, vous devez décider s'il vaut la peine d'investir du temps dans la création de systèmes pour accomplir ce que vous pouvez rapidement accomplir avec un framework ou une bibliothèque. Il y aura différents points de bascule selon vos contraintes de temps ou de budget, mais les frameworks sont toujours très pertinents dans les bons scénarios.

Cela dit, beaucoup de ce que font les frameworks deviendra probablement plus facile à faire avec des bibliothèques plus petites et/ou du code natif avec le temps. Prenez mon application comme exemple. En même temps, si les grands frameworks et bibliothèques restent polyvalents, ils pourraient se métamorphoser, s'adapter et persister. Sinon, ils pourraient finir comme jQuery — un outil du passé pour la plupart.

### Conclusion

En conclusion, il existe des moyens prometteurs de développer des applications front-end complexes sans frameworks. Cependant, la spécification pour des choses comme les composants web est encore en évolution et il y a des problèmes à résoudre. Les frameworks font encore beaucoup de choses incroyables et peuvent rendre le développement beaucoup plus fluide.

À l'heure actuelle, autant que je puisse en juger, les avantages de l'utilisation d'un framework l'emportent souvent sur les inconvénients. Cependant, si les frameworks ne commencent pas à résoudre de nouveaux problèmes et à continuer d'évoluer, ils finiront par disparaître.

### Ressources

[**Guide Angular pour débutants : Pourquoi Angular ? Les principaux avantages**](https://blog.angular-university.io/why-angular-angular-vs-jquery-a-beginner-friendly-explanation-on-the-advantages-of-angular-and-mvc/)  
[_Note : Cet article fait partie de la série en cours Angular pour débutants, voici la série complète : Angular For Beginners
026blog.angular-university.io_](https://blog.angular-university.io/why-angular-angular-vs-jquery-a-beginner-friendly-explanation-on-the-advantages-of-angular-and-mvc/)[**Comparaison avec d'autres frameworks - Vue.js**](https://vuejs.org/v2/guide/comparison.html#Runtime-Performance-1)  
[_Vue.js - Le framework JavaScript progressif_vuejs.org_](https://vuejs.org/v2/guide/comparison.html#Runtime-Performance-1)[**Optimisation des performances - React**](https://reactjs.org/docs/optimizing-performance.html)  
[_En interne, React utilise plusieurs techniques astucieuses pour minimiser le nombre d'opérations DOM coûteuses nécessaires pour mettre à jour le
026reactjs.org_](https://reactjs.org/docs/optimizing-performance.html)[**Composants Web**](https://developer.mozilla.org/en-US/docs/Web/Web_Components)  
[_En tant que développeurs, nous savons tous que réutiliser le code autant que possible est une bonne idée. Cela n'a traditionnellement pas été si
026developer.mozilla.org_](https://developer.mozilla.org/en-US/docs/Web/Web_Components)[**La raison la plus profonde pour laquelle les frameworks JavaScript modernes existent**](https://medium.com/dailyjs/the-deepest-reason-why-modern-javascript-frameworks-exist-933b86ebc445)  
[_J'ai vu beaucoup, beaucoup de gens utiliser un framework moderne comme React, Angular ou Vue.js aveuglément. Ces frameworks fournissent
026medium.com_](https://medium.com/dailyjs/the-deepest-reason-why-modern-javascript-frameworks-exist-933b86ebc445)[**Styling Web Components Using A Shared Style Sheet**](https://www.smashingmagazine.com/2016/12/styling-web-components-using-a-shared-style-sheet/)  
[_Les composants web sont une nouvelle fonctionnalité incroyable du web, permettant aux développeurs de définir leurs propres éléments HTML personnalisés
026www.smashingmagazine.com_](https://www.smashingmagazine.com/2016/12/styling-web-components-using-a-shared-style-sheet/)