---
title: Voici pourquoi le rendu côté client a gagné
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-12-12T05:45:25.000Z'
originalURL: https://freecodecamp.org/news/heres-why-client-side-rendering-won-46a349fadb52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*w7wu8p5kO8mYGGedd-zOZg.png
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Web Development
  slug: web-development
seo_title: Voici pourquoi le rendu côté client a gagné
seo_desc: 'By Cory House

  A decade ago, nearly everyone was rendering their web applications on the server
  using technologies like ASP.NET, Ruby on Rails, Java, and PHP.

  Then handy libraries like jQuery showed up, and suddenly server-side rendering everything
  di...'
---

Par Cory House

Il y a une décennie, presque tout le monde rendait ses applications web sur le serveur en utilisant des technologies comme ASP.NET, Ruby on Rails, Java et PHP.

Ensuite, des bibliothèques pratiques comme jQuery sont apparues, et soudain, le rendu côté serveur de tout n'avait plus nécessairement de sens. jQuery a été suivi par une longue liste de bibliothèques côté client comme Backbone, Knockout, Angular, Ember et React. Avec chaque itération, le rendu côté client est devenu plus facile et plus puissant.

Ce style porte de nombreux noms : applications monopage, SPAs, [JAM stack](https://jamstack.org)... appelez-le comme vous voulez. Le point est, aujourd'hui, le rendu côté client est devenu la manière de facto de construire des applications web riches... Mais pourquoi ?

### Hé tout le monde, faisons-le de la manière difficile

Il est indéniable que le rendu côté client est plus difficile à faire _bien_. Vous devez penser à la bundling, la transpilation, le linting, le cache busting, [et bien plus encore](http://bit.ly/jsdevenv). Faire du côté client correctement est si difficile que je passe en revue plus de 40 décisions que vous devez prendre pour tout faire correctement dans [mon nouveau cours Pluralsight](http://bit.ly/jsdevenv).

![Image](https://cdn-media-1.freecodecamp.org/images/73HS0XltTomG-PyVPetBGZMeUAzfAFYXE9js)
_Juste quelques raisons pour lesquelles le développement côté client est difficile._

Alors pourquoi nous infligeons-nous une telle douleur ? Parce que le rendu côté client offre une longue liste d'avantages que le rendu côté serveur ne peut tout simplement pas égaler.

Voici pourquoi le rendu côté client a gagné.

#### Pas de rechargement complet de page requis

Avec le rendu côté serveur traditionnel, le serveur répond en générant et en retournant une page complètement nouvelle pour chaque interaction. Cela ralentit souvent le temps de chargement, utilise plus de bande passante et crée une expérience utilisateur moins réactive.

Le rendu côté client évite de faire des requêtes inutiles pour une page complète lorsque seule une partie de la page a changé. Cela est particulièrement utile dans un monde qui navigue de plus en plus via des réseaux mobiles avec une latence élevée.

#### Chargement paresseux

Le rendu côté client supporte le chargement paresseux de sections de votre application pour économiser de la bande passante et accélérer le chargement initial. Par exemple, vous pouvez charger des enregistrements supplémentaires, des images et des publicités lorsque l'utilisateur fait défiler vers le bas, ou lorsque l'utilisateur change ses paramètres de recherche, le tout sans effectuer de postback complet.

![Image](https://cdn-media-1.freecodecamp.org/images/3yU4P3bfJc3DJnnee08TAvDYNyDz6s3U1Az8)

#### Interactions riches

Le rendu côté client supporte des interactions riches, animées, des transformations et des transitions. Faites disparaître une ligne à la suppression, ou faites apparaître une boîte de dialogue. Bien sûr, vous pouvez ajouter de telles fonctionnalités dans une application rendue côté serveur, mais cela conduit souvent à maintenir le même modèle à la fois sur le client et le serveur, ou à gérer la complexité de l'intégration des interactions JavaScript avec un framework côté serveur.

#### Hébergement économique

L'hébergement de fichiers statiques est généralement moins cher que l'hébergement de technologies côté serveur traditionnelles comme ASP.NET, PHP ou Ruby. Vous n'avez pas besoin de beaucoup de puissance pour servir un fichier statique. Servir des fichiers statiques est si bon marché en fait, que diverses options gratuites solides existent, y compris [Surge](http://surge.sh), [Firebase](https://firebase.google.com), et [Netlify](https://www.netlify.com).

#### Utilisation d'un CDN

Un front-end statique peut être hébergé via un réseau de diffusion de contenu (CDN). Les CDN offrent une meilleure performance en distribuant globalement les actifs ainsi qu'une meilleure scalabilité en supprimant la charge de votre serveur web. Les hôtes statiques mentionnés ci-dessus utilisent un CDN.

#### Déploiements faciles

Les fichiers statiques sont faciles à déployer. Vous n'avez pas nécessairement besoin d'effectuer une build monolithique pour générer de nouveaux binaires lorsqu'un petit changement se produit. Et avec certains des services mentionnés ci-dessus comme Surge et Netlify, vous pouvez facilement créer des déploiements automatisés via leurs CLIs fournis. Lorsque vous le faites, vous ne risquez pas de casser votre back-end - il est géré complètement séparément.

![Image](https://cdn-media-1.freecodecamp.org/images/KRBk6lWwSa2DA1XkzpGKoBdEb1GJagD6atXs)
_Des déploiements automatisés faciles ? Oui, s'il vous plaît._

#### Séparation des préoccupations renforcée

De nombreuses équipes ont du mal à garder l'accès aux données et la logique métier hors de l'interface utilisateur. Avec le rendu côté client, la séparation des préoccupations est renforcée de manière programmatique. Il n'y a aucun moyen d'accéder directement à la base de données. Vous devez faire un appel à un service séparé. Cela aide à favoriser une mentalité orientée service au sein des équipes de développement, car il n'y a aucun moyen de prendre un raccourci et d'appeler la base de données directement depuis l'UI.

#### Apprendre une fois, écrire partout

Imaginez que vous êtes un nouveau diplômé. Quel est le seul langage qui vous permettra de construire des applications web, des APIs, des applications mobiles et des applications de bureau ? JavaScript. De plus en plus, c'est précisément ce que les nouveaux diplômés atteignent. Pourquoi un nouveau diplômé devrait-il apprendre une technologie côté serveur dédiée lorsque JavaScript fonctionne partout ?

C'est pourquoi il continuera à dominer le monde.

JavaScript est comme Visa. Il est partout où vous voulez être.

![Image](https://cdn-media-1.freecodecamp.org/images/PmQXEu5omEhiJecQnNgWyyyQXE79yPyddzKB)

#### Même technologie UI pour le Web, le mobile natif et le bureau

Imaginez que vous voulez construire une application web de style SPA, une application mobile native et une application de bureau. Les frameworks JavaScript modernes d'aujourd'hui vous permettent d'utiliser la même technologie UI pour les trois scénarios.

Par exemple, vous pouvez utiliser Angular, Ionic et Electron pour travailler avec Angular pour les trois cibles. Ou vous pouvez utiliser React, React Native et Electron pour travailler avec React pour les trois cibles. Et les applications résultantes fonctionneront sur iOS, Android, Windows et macOS. Cela bat certainement l'apprentissage de Objective-C, Swift, Java, C#, WPF et plus pour supporter toutes ces plateformes !

![Image](https://cdn-media-1.freecodecamp.org/images/b15kJ-QlckdQfAfmPO-bvvr9Ko7fBnht6irG)
_Je suis presque sûr que ces parapluies épellent JS. Quelque part._

**Édition** — J'avais un point ici sur le support des Progressive Web Apps mais je me trompais. Vous n'avez pas besoin de faire du rendu côté client pour construire une PWA.

#### Tellement. De. Gratuit.

JavaScript évolue si rapidement que la partie la plus difficile du rendu côté client est de choisir comment vous allez le faire. Le nombre d'options gratuites est simplement écrasant et croît rapidement.

![Image](https://cdn-media-1.freecodecamp.org/images/yg9fOaun9NVSYKEGl5xDA7eso893PQldxwdi)
_#problemesdumondeoccidental_

Oui, c'est un grand problème. Et il n'y a pas besoin de payer pour les bibliothèques, frameworks et éditeurs dont votre équipe a besoin. Je passe en revue et configure des dizaines d'outils gratuits utiles dans « [Building a JavaScript Development Environment](http://bit.ly/jsdevenv) » ([essai gratuit](https://www.pluralsight.com/pricing)).

### Le rendu côté serveur a-t-il encore du sens ?

Bien sûr. Mais dans beaucoup moins de situations qu'avant.

Si vous avez besoin d'interactivité et ne pouvez pas compter sur JavaScript, alors évidemment le rendu côté client est exclu.

Si vous construisez un site principalement statique, le rendu côté serveur pourrait être plus facile. Bien que des outils géniaux comme [Jekyll](https://jekyllrb.com), [Gitbook](https://www.gitbook.com), [Gatsby](https://github.com/gatsbyjs/gatsby), et [d'innombrables alternatives](https://www.staticgen.com) empiètent également sur ce domaine. Et puisque ces outils génèrent simplement du HTML statique, vous n'avez pas à vous soucier des impacts SEO non plus.

Le SEO est un point de vente courant pour le rendu côté serveur, mais l'avènement du rendu isomorphique/universel dans des bibliothèques comme React a également abordé cette préoccupation. Le rendu universel était difficile, mais des outils modernes comme [next.js de Zeit](https://github.com/zeit/next.js) le rendent enfin trivial également !

Étant donné tous les avantages ci-dessus, je peine à trouver de bonnes raisons de faire du rendu côté serveur traditionnel.

Bien sûr, c'est toujours difficile à faire bien. Mais pour toutes les raisons ci-dessus, le rendu côté client a gagné.

[Cory House](https://twitter.com/housecor) est l'auteur de [plusieurs cours sur JavaScript, React, le code propre, .NET, et plus encore sur Pluralsight](http://pluralsight.com/author/cory-house). Il est consultant principal chez [reactjsconsulting.com](http://www.reactjsconsulting.com), architecte logiciel chez VinSolutions, un MVP Microsoft, et forme des développeurs logiciels à l'international sur des pratiques logicielles comme le développement front-end et le code propre. Cory tweete sur JavaScript et le développement front-end sur Twitter en tant que [@housecor](http://www.twitter.com/housecor).