---
title: Le modèle Model-View-Controller est-il mort sur le front-end ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-09T19:43:47.000Z'
originalURL: https://freecodecamp.org/news/is-mvc-dead-for-the-frontend-35b4d1fe39ec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZByyohMUALGVRHbMX9739Q.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Le modèle Model-View-Controller est-il mort sur le front-end ?
seo_desc: 'By Alex Moldovan

  More and more front-end developers are adopting unidirectional architectures. So
  what’s the future for the classic Model-View-Controller (MVC) approach?

  In order to understand how we got to this point, let’s first review the evolutio...'
---

Par Alex Moldovan

De plus en plus de développeurs front-end adoptent des [architectures unidirectionnelles](http://staltz.com/unidirectional-user-interface-architectures.html). Alors, quel est l'avenir de l'approche classique Model-View-Controller (MVC) ?

Pour comprendre comment nous en sommes arrivés là, examinons d'abord l'évolution de l'architecture front-end.

Au cours des quatre dernières années, j'ai travaillé sur un grand nombre de projets web et j'ai passé beaucoup de temps à architecturer des front-ends et à intégrer des frameworks.

Avant 2010, **JavaScript** — le langage de programmation dans lequel _jQuery_ a été écrit — était utilisé principalement pour ajouter des manipulations DOM aux sites web traditionnels. Les développeurs ne semblaient pas se soucier beaucoup de l'architecture elle-même. Des choses comme le [revealing module pattern](https://toddmotto.com/mastering-the-module-pattern/#revealing-module-pattern) étaient suffisamment bonnes pour structurer nos bases de code.

Notre discussion actuelle sur l'architecture front-end vs back-end n'a émergé qu'à la fin de 2010. C'est à ce moment-là que les développeurs ont commencé à prendre au sérieux le concept d'_application monopage_. C'est également à ce moment-là que des frameworks comme [Backbone](http://backbonejs.org/) et [Knockout](http://knockoutjs.com/) ont commencé à devenir populaires.

Étant donné que beaucoup des principes sur lesquels ces frameworks étaient construits étaient assez nouveaux à l'époque, leurs concepteurs ont dû chercher ailleurs pour s'inspirer. Ils ont emprunté des pratiques déjà bien établies pour l'architecture côté serveur. Et à ce moment-là, tous les frameworks côté serveur populaires impliquaient une sorte d'implémentation du modèle classique [MVC](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller) (également connu sous le nom de MV* [en raison de ses variations](https://www.quora.com/What-are-the-main-differences-between-MVC-MVP-and-MVVM-design-patterns-for-the-JavaScript-developer)).

Lorsque [React.js](https://facebook.github.io/react/) a été introduit pour la première fois comme une [bibliothèque de rendu](http://stackoverflow.com/questions/148747/what-is-the-difference-between-a-framework-and-a-library#answer-148788), de nombreux développeurs [s'en sont moqués](https://www.youtube.com/watch?v=x7cQ3mrcKaY) parce qu'ils percevaient sa manière de traiter le HTML en JavaScript comme contre-intuitive. Mais ils ont négligé la contribution la plus importante que React a apportée — **l'Architecture Basée sur les Composants**.

React n'a pas inventé les composants, mais il a poussé cette idée un peu plus loin.

Cette avancée majeure en architecture a été négligée même par Facebook, lorsqu'ils ont présenté React comme le « V dans le MVC ».

En passant, je fais encore des cauchemars après avoir examiné une base de code qui avait à la fois [Angular 1.x et React fonctionnant ensemble](https://github.com/ngReact/ngReact).

2015 nous a apporté un changement majeur de mentalité — du modèle MVC familier aux **Architectures Unidirectionnelles et Flux de Données** dérivés de Flux et de la Programmation Réactive Fonctionnelle, soutenus par des outils comme [Redux](https://github.com/reactjs/redux) ou [RxJS](https://github.com/Reactive-Extensions/RxJS).

### Alors, où tout a-t-il mal tourné pour MVC ?

MVC est probablement encore la meilleure façon de gérer le côté serveur. Des frameworks comme [Rails](http://rubyonrails.org/) et [Django](https://www.djangoproject.com/) sont un plaisir à utiliser.

Les problèmes viennent du fait que les principes et les séparations que MVC a introduits sur le serveur ne sont pas les mêmes que sur le client.

#### Couplage Contrôleur-Vue

Ci-dessous se trouve un diagramme montrant comment la Vue et le Contrôleur interagissent sur le serveur. Il n'y a que deux points de contact entre eux, tous deux traversant la frontière entre le client et le serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/x2aH1-TooFRpF33v1bSoVaemZKS4vpVQHNj-)
_MVC Serveur_

Lorsque vous passez à MVC sur le client, un problème se pose. Les contrôleurs ressemblent à ce que nous appelons le « code-behind ». Le Contrôleur est fortement dépendant de la Vue. Dans la plupart des implémentations de frameworks, il est même créé par la Vue (comme c'est le cas avec, par exemple, ng-controller dans Angular).

![Image](https://cdn-media-1.freecodecamp.org/images/GO1Gdu-H1atMgUXbf2qIwxWs6ncqqEoQCi2v)
_MVC Client_

De plus, lorsque vous pensez au [Principe de Responsabilité Unique](http://www.oodesign.com/single-responsibility-principle.html), cela enfreint clairement les règles. Le code du contrôleur client traite à la fois de la **gestion des événements** et de la **logique métier**, à un certain niveau.

#### **Modèles Obèses**

Réfléchissez un peu au type de données que vous stockez dans un Modèle côté client.

D'une part, vous avez des données comme _utilisateurs_ et _produits_, qui représentent votre **État de l'Application**. D'autre part, vous devez stocker l'**État de l'UI** — des choses comme _showTab_ ou _selectedValue_.

Similaire au Contrôleur, le Modèle enfreint le Principe de Responsabilité Unique, car vous n'avez pas de moyen séparé de gérer l'**État de l'UI** et l'**État de l'Application**.

### Alors, où les composants s'intègrent-ils dans ce modèle ?

Les composants sont : **Vues** + **Gestion des Événements** + **État de l'UI**.

Le diagramme ci-dessous montre comment vous divisez réellement le modèle MVC original pour obtenir les composants. Ce qui reste au-dessus de la ligne est exactement ce que **Flux** essaie de résoudre : la gestion de l'**État de l'Application** et de la **Logique Métier**.

![Image](https://cdn-media-1.freecodecamp.org/images/zu0i01opFa-1t7seaTGrMnNLM1TRh353RUZg)

Avec la popularité de React et de **l'architecture basée sur les composants**, nous avons vu l'émergence des **architectures unidirectionnelles** pour gérer l'état de l'application.

L'une des raisons pour lesquelles ces deux approches fonctionnent si bien ensemble est qu'elles couvrent entièrement l'approche classique MVC. Elles offrent également une bien meilleure séparation des préoccupations en matière de construction d'architectures front-end.

Mais ce n'est plus une histoire de React. Si vous regardez [Angular 2](https://angular.io/), vous verrez exactement le même modèle appliqué, même si vous avez différentes options pour gérer l'état de l'application comme [ngrx/store](https://github.com/ngrx/store).

Il n'y avait vraiment rien que MVC aurait pu faire de mieux sur le client. Il était voué à l'échec dès le début. Nous avions juste besoin de temps pour le voir. À travers ce processus de cinq ans, l'architecture front-end a évolué pour devenir ce qu'elle est aujourd'hui. Et lorsque vous y réfléchissez, cinq ans ne sont pas si longs pour que les meilleures pratiques émergent.

MVC était nécessaire au début parce que nos applications front-end devenaient de plus en plus grandes et complexes, et nous ne savions pas comment les structurer. Je pense qu'il a servi son but, tout en fournissant une bonne leçon sur la prise d'une bonne pratique d'un contexte (le serveur) et son application à un autre (le client).

### Alors, que nous réserve l'avenir ?

Je ne pense pas que nous reviendrons à l'architecture classique MVC de sitôt pour nos applications front-end.

Alors que de plus en plus de développeurs commencent à voir les avantages des composants et des architectures unidirectionnelles, l'accent sera mis sur la construction de meilleurs outils et bibliothèques qui suivent cette voie.

Ce type d'architecture sera-t-il la meilleure solution dans cinq ans ? Il y a de bonnes chances que cela se produise, mais rien n'est certain.

Il y a cinq ans, personne n'aurait pu prédire comment nous en arriverions à écrire des applications aujourd'hui. Je ne pense donc pas qu'il soit prudent de parier sur l'avenir maintenant.

C'est à peu près tout ! J'espère que vous avez apprécié la lecture de cet article. Vos commentaires sont les bienvenus ci-dessous.

Si vous avez aimé l'article, cliquez sur le cœur vert ci-dessous et je saurai que mes efforts ne sont pas vains.