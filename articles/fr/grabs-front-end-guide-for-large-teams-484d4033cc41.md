---
title: Notre grande équipe d'ingénieurs utilise ce guide de développement front-end
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-14T04:46:04.000Z'
originalURL: https://freecodecamp.org/news/grabs-front-end-guide-for-large-teams-484d4033cc41
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zC0ohmwFgQ9LPYHsIvJeSw.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Notre grande équipe d'ingénieurs utilise ce guide de développement front-end
seo_desc: 'By Yangshun Tay

  Front end development has never been so complex and exciting as it is today. New
  tools, libraries, frameworks, and plugins emerge every other day. There is so much
  to learn.

  Fortunately our web team at Grab has been keeping up with th...'
---

Par Yangshun Tay

Le développement front-end n'a jamais été aussi complexe et passionnant qu'aujourd'hui. De nouveaux outils, bibliothèques, frameworks et plugins émergent tous les deux jours. Il y a tant à apprendre.

Heureusement, notre équipe web chez [Grab](https://www.grab.com/sg/) a suivi les [dernières meilleures pratiques](https://blog.daftcode.pl/hype-driven-development-3469fc2e9b22) et a intégré l'écosystème JavaScript moderne dans nos applications web.

Le résultat est que nos nouvelles recrues ou ingénieurs back-end, qui ne sont pas nécessairement bien familiarisés avec l'écosystème JavaScript moderne, peuvent se sentir submergés par le barrage de nouvelles choses qu'ils doivent apprendre juste pour compléter leur fonctionnalité ou corriger un bug dans une application web.

Il est impératif qu'ils soient guidés pour embrasser cette évolution du front-end, apprendre à naviguer dans l'écosystème avec aisance, et devenir productifs dans la livraison de code à nos utilisateurs le plus rapidement possible. Nous avons élaboré un guide d'étude pour introduire pourquoi nous faisons ce que nous faisons.

Ce guide d'étude est inspiré par « [A Study Plan to Cure JavaScript Fatigue](https://medium.freecodecamp.com/a-study-plan-to-cure-javascript-fatigue-8ad3a54f2eb1#.g9egaapps) » et est légèrement opiné dans le sens où nous recommandons certaines bibliothèques/frameworks à apprendre pour chaque aspect du développement front-end, basés sur ce qui est actuellement jugé le plus adapté chez Grab.

Nous expliquons pourquoi une certaine bibliothèque est choisie et fournissons des liens vers des ressources d'apprentissage pour permettre au lecteur de l'adopter par lui-même. Des choix alternatifs qui peuvent être meilleurs pour d'autres cas d'utilisation sont également fournis pour référence et exploration personnelle.

Si vous êtes familiarisé avec le développement front-end et avez régulièrement suivi les dernières évolutions, ce guide ne sera probablement pas très utile pour vous. Il est destiné aux nouveaux venus dans le front-end.

Si votre entreprise explore également une pile JavaScript moderne, vous pourriez trouver ce guide d'étude utile pour votre entreprise aussi ! N'hésitez pas à l'adapter à vos besoins. Nous mettrons à jour ce guide d'étude périodiquement, selon nos derniers travaux et choix.

Notez que nous avons publié ce guide d'étude sur [GitHub](https://github.com/grab/front-end-guide) également, et nous y apporterons les futures mises à jour.

[**grab/front-end-guide**](https://github.com/grab/front-end-guide)
[_front-end-guide - ? Guide d'étude et introduction à la pile front-end moderne._github.com](https://github.com/grab/front-end-guide)

_Vous préparez-vous pour des entretiens techniques front-end ? Consultez ce [manuel](https://github.com/yangshun/front-end-interview-handbook) qui contient des réponses aux célèbres questions d'entretien pour un poste front-end._

[**yangshun/front-end-interview-handbook**](https://github.com/yangshun/front-end-interview-handbook)
[_front-end-interview-handbook - ? Réponses presque complètes aux "Questions d'entretien pour un poste front-end"_github.com](https://github.com/yangshun/front-end-interview-handbook)

**Prérequis**

* Bonne compréhension des concepts de programmation de base.
* À l'aise avec les actions de base en ligne de commande et familiarité avec les systèmes de contrôle de version du code source tels que Git.
* Expérience en développement web. Avoir construit des applications web rendues côté serveur en utilisant des frameworks comme Ruby on Rails, Django, Express, etc.
* Compréhension du fonctionnement du web. Familiarité avec les protocoles et conventions web comme HTTP et les API RESTful.

### Quelques sujets que nous aborderons dans cet article :

* Applications monopage (SPA)
* JavaScript nouvelle génération
* Interface utilisateur
* Gestion d'état
* Codage avec style
* Tests
* Linting JavaScript
* Linting CSS
* Types
* Système de build
* Gestion des paquets
* Intégration continue
* Hébergement
* Déploiement

N'hésitez pas à sauter certains de ces sujets si vous avez déjà une expérience préalable avec eux.

### Applications monopage (SPA)

Les développeurs web de nos jours font référence aux produits qu'ils construisent comme des applications web, plutôt que des sites web. Bien qu'il n'y ait pas de différence stricte entre les deux termes, les applications web tendent à être hautement interactives et dynamiques, permettant à l'utilisateur d'effectuer des actions et de recevoir une réponse pour leur action.

Traditionnellement, le navigateur reçoit du HTML du serveur et le rend. Lorsque l'utilisateur navigue vers une autre URL, un rafraîchissement complet de la page est nécessaire et le serveur envoie un nouveau HTML frais pour la nouvelle page. Cela s'appelle le rendu côté serveur.

Cependant, dans les SPA modernes, le rendu côté client est utilisé à la place. Le navigateur charge la page initiale à partir du serveur, ainsi que les scripts (frameworks, bibliothèques, code de l'application) et les feuilles de style nécessaires pour toute l'application. Lorsque l'utilisateur navigue vers d'autres pages, un rafraîchissement de la page n'est pas déclenché. L'URL de la page est mise à jour via l'[API History HTML5](https://developer.mozilla.org/fr/docs/Web/API/History_API). Les nouvelles données nécessaires pour la nouvelle page, généralement au format JSON, sont récupérées par le navigateur via des requêtes [AJAX](https://developer.mozilla.org/fr/docs/AJAX/Getting_Started) au serveur. Le SPA met ensuite à jour dynamiquement la page avec les données via JavaScript, qu'il a déjà téléchargé lors du chargement initial de la page. Ce modèle est similaire à la façon dont les applications mobiles natives fonctionnent.

Les avantages :

* L'application semble plus réactive et les utilisateurs ne voient pas le flash entre les navigations de page dû aux rafraîchissements complets de page.
* Moins de requêtes HTTP sont faites au serveur, car les mêmes ressources n'ont pas à être téléchargées à nouveau pour chaque chargement de page.
* Séparation claire des préoccupations entre le client et le serveur ; vous pouvez facilement construire de nouveaux clients pour différentes plateformes (par exemple, mobile, chatbots, montres intelligentes) sans avoir à modifier le code du serveur. Vous pouvez également modifier la pile technologique sur le client et le serveur indépendamment, tant que le contrat d'API n'est pas rompu.

Les inconvénients :

* Chargement initial de la page plus lourd en raison du chargement du framework, du code de l'application et des ressources nécessaires pour plusieurs pages.
* Il y a une étape supplémentaire à effectuer sur votre serveur qui consiste à le configurer pour router toutes les requêtes vers un seul point d'entrée et permettre au routage côté client de prendre le relais à partir de là.
* Les SPA dépendent de JavaScript pour rendre le contenu, mais tous les moteurs de recherche n'exécutent pas JavaScript lors de l'exploration, et ils peuvent voir un contenu vide sur votre page. Cela nuit involontairement au référencement de votre application.

Bien que les applications rendues côté serveur traditionnelles soient encore une option viable, une séparation claire client-serveur est plus évolutive pour les grandes équipes d'ingénierie, car le code client et serveur peut être développé et publié indépendamment. Cela est particulièrement vrai chez Grab lorsque nous avons plusieurs applications clientes qui accèdent au même serveur d'API.

Alors que les développeurs web construisent désormais des applications plutôt que des pages, l'organisation du JavaScript côté client est devenue de plus en plus importante. Dans les pages rendues côté serveur, il est courant d'utiliser des extraits de jQuery pour ajouter de l'interactivité utilisateur à chaque page. Cependant, lors de la construction de grandes applications, jQuery seul est insuffisant. Après tout, jQuery est principalement une bibliothèque pour la manipulation du DOM et ce n'est pas un framework ; il ne définit pas une structure et une organisation claires pour votre application.

Des frameworks JavaScript ont été créés pour fournir des abstractions de haut niveau sur le DOM, vous permettant de garder l'état en mémoire, hors du DOM. L'utilisation de frameworks apporte également les avantages de réutiliser des concepts recommandés et des meilleures pratiques pour construire des applications. Un nouvel ingénieur dans l'équipe qui n'est pas familier avec la base de code, mais qui a de l'expérience avec un framework, trouvera plus facile de comprendre le code car il est organisé dans une structure qui lui est familière. Les frameworks populaires ont beaucoup de tutoriels et de guides, et tirer parti des connaissances et de l'expérience des collègues et de la communauté aidera les nouveaux ingénieurs à se mettre rapidement à niveau.

#### Liens d'étude

* [Single Page App: avantages et inconvénients](http://stackoverflow.com/questions/21862054/single-page-app-advantages-and-disadvantages)
* [The (R)Evolution of Web Development](http://blog.isquaredsoftware.com/presentations/2016-10-revolution-of-web-dev/)
* [Here’s Why Client Side Rendering Won](https://medium.freecodecamp.com/heres-why-client-side-rendering-won-46a349fadb52)

### JavaScript nouvelle génération

Avant de plonger dans les divers aspects de la construction d'une application web JavaScript, il est important de se familiariser avec le langage du web — JavaScript, ou ECMAScript. JavaScript est un langage incroyablement polyvalent que vous pouvez également utiliser pour construire des [serveurs web](https://nodejs.org/en/), des [applications mobiles natives](https://facebook.github.io/react-native/) et des [applications de bureau](https://electron.atom.io/).

Avant 2015, la dernière mise à jour majeure était ECMAScript 5.1, en 2011. Cependant, ces dernières années, JavaScript a soudainement connu une énorme vague d'améliorations en un court laps de temps. En 2015, ECMAScript 2015 (précédemment appelé ECMAScript 6) a été publié et une tonne de constructions syntaxiques ont été introduites pour rendre l'écriture de code moins encombrante. Si vous êtes curieux à ce sujet, Auth0 a écrit un bel article sur [l'histoire de JavaScript](https://auth0.com/blog/a-brief-history-of-javascript/). À ce jour, tous les navigateurs n'ont pas encore pleinement implémenté la spécification ES2015. Des outils tels que [Babel](https://babeljs.io/) permettent aux développeurs d'écrire du ES2015 dans leurs applications et Babel les transpile en ES5 pour être compatibles avec les navigateurs.

Être familier avec ES5 et ES2015 est crucial. ES2015 est encore relativement nouveau et beaucoup de code open source et d'applications Node.js sont encore écrits en ES5. Si vous faites du débogage dans votre console de navigateur, vous ne pourrez peut-être pas utiliser la syntaxe ES2015. D'un autre côté, la documentation et les exemples de code pour de nombreuses bibliothèques modernes que nous introduirons plus tard ci-dessous sont encore écrits en ES2015. Chez Grab, nous utilisons [babel-preset-env](https://github.com/babel/babel-preset-env) pour profiter du gain de productivité des améliorations syntaxiques que l'avenir de JavaScript offre et nous l'aimons beaucoup jusqu'à présent. `babel-preset-env` détermine intelligemment quels plugins Babel sont nécessaires (quelles nouvelles fonctionnalités de langage ne sont pas supportées et doivent être transpilées) à mesure que les navigateurs augmentent le support natif pour plus de fonctionnalités du langage ES. Si vous préférez utiliser des fonctionnalités de langage qui sont déjà stables, vous pourriez trouver que [babel-preset-stage-3](https://babeljs.io/docs/plugins/preset-stage-3/), qui est une spécification complète qui sera très probablement implémentée dans les navigateurs, sera plus adapté.

Passez un jour ou deux à réviser ES5 et à explorer ES2015. Les fonctionnalités les plus utilisées dans ES2015 incluent « Arrows and Lexical This », « Classes », « Template Strings », « Destructuring », « Default/Rest/Spread operators », et « Importing and Exporting modules ».

**Durée estimée : 3–4 jours.** Vous pouvez apprendre/rechercher la syntaxe tout en apprenant les autres bibliothèques et en essayant de construire votre propre application.

#### Liens d'étude

* [Apprendre ES5 sur Codecademy](https://www.codecademy.com/learn/learn-javascript)
* [Apprendre ES2015 sur Babel](https://babeljs.io/learn-es2015/)
* [ES6 Katas](http://es6katas.org/)
* [Free Code Camp](https://www.freecodecamp.com/)
* [You Don’t Know JS](https://github.com/getify/You-Dont-Know-JS) (Contenu avancé, optionnel pour les débutants)

### Interface utilisateur — React

![Image](https://cdn-media-1.freecodecamp.org/images/9eWZb1BhoYVbahSnEgyN0KMFdKlIRAh4Aoho)

Si un projet JavaScript a pris d'assaut l'écosystème front-end ces dernières années, c'est bien [React](https://facebook.github.io/react/). React est une bibliothèque construite et open-sourcée par les brillants esprits de Facebook. Dans React, les développeurs écrivent des composants pour leur interface web et les composent ensemble.

React apporte de nombreuses idées radicales et encourage les développeurs à [repenser les meilleures pratiques](https://www.youtube.com/watch?v=DgVS-zXgMTk). Pendant de nombreuses années, les développeurs web ont appris qu'il était bon de séparer le HTML, le JavaScript et le CSS. React fait exactement le contraire et encourage à écrire votre HTML et [CSS dans votre JavaScript](https://speakerdeck.com/vjeux/react-css-in-js) à la place. Cela semble être une idée folle au premier abord, mais après l'avoir essayée, ce n'est en fait pas aussi étrange que cela en a l'air initialement. La raison est que la scène du développement front-end évolue vers un paradigme de développement basé sur les composants. Les fonctionnalités de React :

* **Déclaratif** — Vous décrivez ce que vous voulez voir dans votre vue et non comment l'obtenir. À l'époque de jQuery, les développeurs devaient imaginer une série d'étapes pour manipuler le DOM afin de passer d'un état de l'application à l'autre. Dans React, vous changez simplement l'état au sein du composant et la vue se mettra à jour elle-même en fonction de l'état. Il est également facile de déterminer à quoi ressemblera le composant simplement en regardant le balisage dans la méthode `render()`.
* **Fonctionnel** — La vue est une fonction pure de `props` et `state`. Dans la plupart des cas, un composant React est défini par `props` (paramètres externes) et `state` (données internes). Pour les mêmes `props` et `state`, la même vue est produite. Les fonctions pures sont faciles à tester, et il en va de même pour les composants fonctionnels. Les tests dans React sont facilités car les interfaces d'un composant sont bien définies et vous pouvez tester le composant en fournissant différents `props` et `state` et en comparant la sortie rendue.
* **Maintenable** — Écrire votre vue de manière basée sur les composants encourage la réutilisabilité. Nous trouvons que la définition des `propTypes` d'un composant rend le code React auto-documenté car le lecteur peut savoir clairement ce qui est nécessaire pour utiliser ce composant. Enfin, votre vue et votre logique sont auto-contenues dans le composant et ne doivent pas être affectées ni affecter d'autres composants. Cela facilite le déplacement des composants lors de refactorisations à grande échelle, tant que les mêmes `props` sont fournies au composant.
* **Hautes performances** — Vous avez peut-être entendu dire que React utilise un DOM virtuel (à ne pas confondre avec le [shadow DOM](https://developer.mozilla.org/fr/docs/Web/Web_Components/Shadow_DOM)) et qu'il ré-affiche tout lorsqu'il y a un changement d'état. Pourquoi avons-nous besoin d'un DOM virtuel ? Bien que les moteurs JavaScript modernes soient rapides, la lecture et l'écriture dans le DOM sont lentes. React conserve une représentation virtuelle légère du DOM en mémoire. Ré-afficher tout est un terme trompeur. Dans React, cela fait en fait référence à la ré-affichage de la représentation en mémoire du DOM, et non du DOM réel lui-même. Lorsqu'il y a un changement dans les données sous-jacentes du composant, une nouvelle représentation virtuelle est créée et comparée à la représentation précédente. La différence (ensemble minimal de changements requis) est ensuite appliquée au DOM réel du navigateur.
* **Facilité d'apprentissage** — Apprendre React est assez simple. L'API de React est relativement petite par rapport à [celle-ci](https://angular.io/docs/ts/latest/api/) ; il n'y a que quelques API à apprendre et elles ne changent pas souvent. La communauté React est l'une des plus grandes, et avec elle vient un écosystème vibrant d'outils, de composants UI open-source et une tonne de grandes ressources en ligne pour vous aider à commencer à apprendre React.
* **Expérience développeur** — Il existe un certain nombre d'outils qui améliorent l'expérience de développement avec React. [React Developer Tools](https://github.com/facebook/react-devtools) est une extension de navigateur qui vous permet d'inspecter votre composant, de voir et de manipuler ses `props` et `state`. Le [rechargement à chaud](https://github.com/gaearon/react-hot-loader) avec webpack vous permet de voir les changements dans votre code dans votre navigateur, sans avoir à rafraîchir le navigateur. Le développement front-end implique beaucoup de modifications de code, de sauvegarde et de rafraîchissement du navigateur. Le rechargement à chaud vous aide en éliminant la dernière étape. Lorsque des mises à jour de bibliothèques sont disponibles, Facebook fournit des [scripts codemod](https://github.com/reactjs/react-codemod) pour vous aider à migrer votre code vers les nouvelles API. Cela rend le processus de mise à jour relativement indolore. Bravo à l'équipe Facebook pour leur dévouement à rendre l'expérience de développement avec React excellente.

![Image](https://cdn-media-1.freecodecamp.org/images/N6ez3BL8jhqylPz2GDgOLQgDpRt-eLZleDe-)
_React Developer Tools en action !_

Au fil des ans, de nouvelles bibliothèques de vue encore plus performantes que React ont émergé. React peut ne pas être la bibliothèque la plus rapide, mais en termes d'écosystème, d'expérience d'utilisation globale et d'avantages, c'est toujours l'une des meilleures. Facebook canalise également des efforts pour rendre React encore plus rapide avec une [réécriture de l'algorithme de réconciliation sous-jacent](https://github.com/acdlite/react-fiber-architecture). Les concepts que React a introduits nous ont appris à écrire un meilleur code, des applications web plus maintenables et nous ont rendus meilleurs ingénieurs. Nous aimons cela.

Nous recommandons de suivre le [tutoriel](https://facebook.github.io/react/tutorial/tutorial.html) sur la construction d'un jeu de morpion sur la page d'accueil de React pour avoir une idée de ce qu'est React et de ce qu'il fait. Pour un apprentissage plus approfondi, consultez le cours gratuit très bien noté, [React Fundamentals](https://reacttraining.com/online/react-fundamentals) par les créateurs de [React Router](https://github.com/ReactTraining/react-router/), qui sont des experts de la communauté React. Il couvre également des concepts plus avancés qui ne sont pas couverts par la documentation React. [Create React App](https://github.com/facebookincubator/create-react-app) par Facebook est un outil pour échafauder un projet React avec une configuration minimale et est fortement recommandé pour démarrer de nouveaux projets React.

React est une bibliothèque, pas un framework, et ne traite pas des couches en dessous de la vue — l'état de l'application. Plus sur cela plus tard.

**Durée estimée : 3–4 jours.** Essayez de construire des projets simples comme une liste de tâches, un clone de Hacker News avec React pur. Vous allez lentement l'apprécier et peut-être rencontrer quelques problèmes en cours de route qui ne sont pas résolus par React, ce qui nous amène au sujet suivant...

#### Liens d'étude

* [Tutoriel officiel de React](https://facebook.github.io/react/tutorial/tutorial.html)
* [React Fundamentals](https://reacttraining.com/online/react-fundamentals)
* [Simple React Development in 2017](https://hackernoon.com/simple-react-development-in-2017-113bd563691f)
* [Presentational and Container Components](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0#.5iexphyg5)

#### Alternatives

* [Angular](https://angular.io/)
* [Ember](https://www.emberjs.com/)
* [Vue](https://vuejs.org/)
* [Cycle](https://cycle.js.org/)

### Gestion d'état — Flux/Redux

![Image](https://cdn-media-1.freecodecamp.org/images/kQtQqSAFtUDrMLd27NgqcGPbGGHQmzhKu3Br)

À mesure que votre application grandit, vous pourriez constater que la structure de l'application devient un peu désordonnée. Les composants de l'application peuvent avoir à partager et afficher des données communes, mais il n'y a pas de manière élégante de gérer cela dans React. Après tout, React n'est que la couche de vue, il ne dicte pas comment vous structurez les autres couches de votre application, comme le modèle et le contrôleur, dans les paradigmes MVC traditionnels. Dans un effort pour résoudre cela, Facebook a inventé Flux, une architecture d'application qui complète les composants de vue composables de React en utilisant un flux de données unidirectionnel. Lisez plus sur le fonctionnement de Flux [ici](https://facebook.github.io/flux/docs/in-depth-overview.html). En résumé, le modèle Flux a les caractéristiques suivantes :

* **Flux de données unidirectionnel** — Rend l'application plus prévisible car les mises à jour peuvent être suivies facilement.
* **Séparation des préoccupations** — Chaque partie dans l'architecture Flux a des responsabilités claires et est fortement découplée.
* **Fonctionne bien avec la programmation déclarative** — Le magasin peut envoyer des mises à jour à la vue sans spécifier comment faire la transition entre les vues.

Comme Flux n'est pas un framework à proprement parler, les développeurs ont essayé de proposer de nombreuses implémentations du modèle Flux. Finalement, un vainqueur clair a émergé, qui était [Redux](http://redux.js.org/). Redux combine les idées de Flux, du [modèle de commande](https://www.wikiwand.com/fr/Command_pattern) et de l'[architecture Elm](https://guide.elm-lang.org/architecture/) et est la bibliothèque de gestion d'état de facto que les développeurs utilisent avec React ces jours-ci. Ses concepts principaux sont :

* L'**état** de l'application est décrit par un simple objet JavaScript (POJO).
* Envoyez une **action** (également un POJO) pour modifier l'état.
* **Réducteur** est une fonction pure qui prend l'état actuel et l'action pour produire un nouvel état.

Les concepts semblent simples, mais ils sont vraiment puissants car ils permettent aux applications de :

* Avoir leur état rendu sur le serveur, démarré sur le client.
* Tracer, journaliser et revenir en arrière sur les changements dans toute l'application.
* Implémenter facilement les fonctionnalités d'annulation/répétition.

Le créateur de Redux, [Dan Abramov](https://github.com/gaearon), a pris grand soin d'écrire une documentation détaillée pour Redux, ainsi que de créer des tutoriels vidéo complets pour apprendre [Redux de base](https://egghead.io/courses/getting-started-with-redux) et [Redux avancé](https://egghead.io/courses/building-react-applications-with-idiomatic-redux). Ce sont des ressources extrêmement utiles pour apprendre Redux.

**Combinaison de la Vue et de l'État**

Bien que Redux n'ait pas nécessairement besoin d'être utilisé avec React, il est fortement recommandé car ils fonctionnent très bien ensemble. React et Redux ont beaucoup d'idées et de traits en commun :

* **Paradigme de Composition Fonctionnelle** — React compose des vues (fonctions pures) tandis que Redux compose des réducteurs purs (également des fonctions pures). La sortie est prévisible étant donné le même ensemble d'entrées.
* **Facile à Comprendre** — Vous avez peut-être entendu ce terme plusieurs fois, mais que signifie-t-il réellement ? Nous l'interprétons comme ayant le contrôle et la compréhension de notre code — Notre code se comporte de la manière à laquelle nous nous attendons, et lorsqu'il y a des problèmes, nous pouvons les trouver facilement. Grâce à notre expérience, React et Redux simplifient le débogage. Comme le flux de données est unidirectionnel, le suivi du flux de données (réponses du serveur, événements d'entrée utilisateur) est plus facile et il est simple de déterminer dans quelle couche le problème se produit.
* **Structure en Couches** — Chaque couche dans l'application / l'architecture Flux est une fonction pure et a des responsabilités claires. Il est relativement facile d'écrire des tests pour des fonctions pures.
* **Expérience de Développement** — Beaucoup d'efforts ont été consacrés à la création d'outils pour aider au débogage et à l'inspection de l'application pendant le développement, comme [Redux DevTools](https://github.com/gaearon/redux-devtools).

![Image](https://cdn-media-1.freecodecamp.org/images/AtBm2pdL5cP3oe5v6Mbc4Oq3xC48DEIfiDOn)
_Retour en arrière de l'état avec Redux DevTools_

Votre application devra probablement gérer des appels asynchrones comme des requêtes d'API distantes. [redux-thunk](https://github.com/gaearon/redux-thunk) et [redux-saga](https://github.com/redux-saga/redux-saga) ont été créés pour résoudre ces problèmes. Ils peuvent prendre un certain temps à comprendre car ils nécessitent une compréhension de la programmation fonctionnelle et des générateurs. Notre conseil est de ne les traiter que lorsque vous en avez besoin.

[react-redux](https://github.com/reactjs/react-redux) est une liaison officielle React pour Redux et est très simple à apprendre.

**Durée estimée : 4 jours.** Les cours egghead peuvent être un peu chronophages mais ils valent la peine d'y consacrer du temps. Après avoir appris Redux, vous pouvez essayer de l'incorporer dans les projets React que vous avez construits. Redux résout-il certains des problèmes de gestion d'état avec lesquels vous aviez du mal dans React pur ?

#### Liens d'étude

* [Page d'accueil de Flux](http://facebook.github.io/flux)
* [Page d'accueil de Redux](http://redux.js.org/)
* [Cours Egghead — Getting Started with Redux](https://egghead.io/courses/getting-started-with-redux)
* [Cours Egghead — Build React Apps with Idiomatic Redux](https://egghead.io/courses/building-react-applications-with-idiomatic-redux)
* [Liens React Redux](https://github.com/markerikson/react-redux-links)
* [You Might Not Need Redux](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367)

#### Alternatives

* [MobX](https://github.com/mobxjs/mobx)

### Codage avec Style — CSS Modules

![Image](https://cdn-media-1.freecodecamp.org/images/Xrq3gCJpzVoGVBeX9ILf3oEIZksqGlzyyccY)

CSS (Cascading Style Sheets) sont des règles pour décrire l'apparence de vos éléments HTML. Écrire un bon CSS est difficile. Cela prend généralement de nombreuses années d'expérience et de frustration avant de pouvoir écrire un CSS maintenable et évolutif. Le CSS, ayant un espace de noms global, est fondamentalement conçu pour des documents web, et pas vraiment pour des applications web qui favorisent une architecture basée sur les composants. Par conséquent, des développeurs front-end expérimentés ont conçu des méthodologies pour guider les gens sur la façon d'écrire un CSS organisé pour des projets complexes, comme l'utilisation de [SMACSS](https://smacss.com/), [BEM](http://getbem.com/), [SUIT CSS](http://suitcss.github.io/), etc.

> L'encapsulation des styles que les méthodologies CSS apportent est artificiellement imposée par des conventions et des directives. Elles se brisent dès que les développeurs ne les suivent pas.

Comme vous l'avez peut-être réalisé maintenant, l'écosystème front-end est saturé d'outils, et sans surprise, des outils ont été inventés pour [résoudre partiellement certains des problèmes](https://speakerdeck.com/vjeux/react-css-in-js) liés à l'écriture de CSS à grande échelle. « À grande échelle » signifie que de nombreux développeurs travaillent sur le même grand projet et touchent les mêmes feuilles de style. Il n'y a pas d'approche communément acceptée pour écrire du [CSS dans JS](https://github.com/MicheleBertoli/css-in-js) pour le moment, et nous espérons qu'un jour un vainqueur émergera, tout comme Redux l'a fait parmi toutes les implémentations de Flux. Pour l'instant, nous misons sur [CSS Modules](https://github.com/css-modules/css-modules). Les modules CSS sont une amélioration par rapport au CSS existant qui vise à résoudre le problème de l'espace de noms global dans CSS ; ils vous permettent d'écrire des styles qui sont locaux par défaut et encapsulés dans votre composant. Cette fonctionnalité est obtenue via des outils. Avec les modules CSS, de grandes équipes peuvent écrire des CSS modulaires et réutilisables sans craindre les conflits ou le remplacement d'autres parties de l'application. Cependant, à la fin de la journée, les modules CSS sont toujours compilés en CSS globalement nommé que les navigateurs reconnaissent, et il est toujours important d'apprendre et de comprendre comment fonctionne le CSS brut.

Si vous êtes un débutant complet en CSS, le cours [HTML & CSS](https://www.codecademy.com/learn/learn-html-css) de Codecademy sera une bonne introduction pour vous. Ensuite, lisez sur le [préprocesseur Sass](http://sass-lang.com/), une extension du langage CSS qui ajoute des améliorations syntaxiques et encourage la réutilisabilité des styles. Étudiez les méthodologies CSS mentionnées ci-dessus, et enfin, les modules CSS.

**Durée estimée : 3–4 jours.** Essayez de styliser votre application en utilisant l'approche SMACSS/BEM et/ou les modules CSS.

#### Liens d'étude

* [Cours Apprendre HTML & CSS sur Codecademy](https://www.codecademy.com/learn/learn-html-css)
* [Intro à HTML/CSS sur Khan Academy](https://www.khanacademy.org/computing/computer-programming/html-css)
* [SMACSS](https://smacss.com/)
* [BEM](http://getbem.com/introduction/)
* [SUIT CSS](http://suitcss.github.io/)
* [Spécification des CSS Modules](https://github.com/css-modules/css-modules)
* [Page d'accueil de Sass](http://sass-lang.com/)
* [Réponses aux questions d'entretien pour un poste front-end — HTML](https://medium.com/@yangshun/clearing-your-front-end-job-interview-html-706f8b2c7dca) F300
* [Réponses aux questions d'entretien pour un poste front-end — CSS](https://medium.com/@yangshun/clearing-your-front-end-job-interview-css-95bdd82871f2) F300

#### Alternatives

* [JSS](https://github.com/cssinjs/jss)
* [Styled Components](https://github.com/styled-components/styled-components)

### Maintenabilité

Le code est lu plus fréquemment qu'il n'est écrit. Cela est particulièrement vrai chez Grab, où la taille de l'équipe est grande et nous avons plusieurs ingénieurs travaillant sur plusieurs projets. Nous accordons une grande valeur à la lisibilité, à la maintenabilité et à la stabilité du code et il existe quelques moyens d'y parvenir : « Tests extensifs », « Style de codage cohérent » et « Vérification de type ».

### Tests — Jest + Enzyme

![Image](https://cdn-media-1.freecodecamp.org/images/YyaFO012oBmZNcWU-M8TPKTc0TbRwGsX6O5-)

[Jest](http://facebook.github.io/jest/) est une bibliothèque de tests de Facebook qui vise à rendre le processus de test indolore. Comme pour les projets Facebook, elle offre une excellente expérience de développement dès la sortie de la boîte. Les tests peuvent être exécutés en parallèle, ce qui réduit la durée. En mode surveillance, par défaut, seuls les tests des fichiers modifiés sont exécutés. Une fonctionnalité particulière que nous aimons est le « Snapshot Testing ». Jest peut sauvegarder la sortie générée de votre composant React et l'état Redux et l'enregistrer sous forme de fichiers sérialisés, afin que vous n'ayez pas à créer manuellement la sortie attendue vous-même. Jest est également livré avec des fonctionnalités intégrées de mocking, d'assertion et de couverture de test. Une bibliothèque pour les régner toutes !

![Image](https://cdn-media-1.freecodecamp.org/images/CzGw3xDVAGdiRFuWtihseiN6DCtGuBGzngP9)

React est livré avec quelques utilitaires de test, mais [Enzyme](http://airbnb.io/enzyme/) d'Airbnb facilite la génération, l'assertion, la manipulation et la traversée de la sortie de vos composants React avec une API de type jQuery. Il est recommandé d'utiliser Enzyme pour tester les composants React.

Jest et Enzyme rendent l'écriture de tests front-end amusante et facile. Lorsque l'écriture de tests devient agréable, les développeurs écrivent plus de tests. Il aide également que les composants React et les actions/réducteurs Redux soient relativement faciles à tester en raison de responsabilités et d'interfaces clairement définies. Pour les composants React, nous pouvons tester que, étant donné certains `props`, le DOM souhaité est rendu, et que les rappels sont déclenchés lors de certaines interactions utilisateur simulées. Pour les réducteurs Redux, nous pouvons tester que, étant donné un état antérieur et une action, un état résultant est produit.

La documentation pour Jest et Enzyme est assez concise, et elle devrait être suffisante pour les apprendre en la lisant.

**Durée estimée : 2–3 jours.** Essayez d'écrire des tests Jest + Enzyme pour votre application React + Redux !

#### Liens d'étude

* [Page d'accueil de Jest](http://facebook.github.io/jest/)
* [Testing React Applications with Jest](https://auth0.com/blog/testing-react-applications-with-jest/)
* [Page d'accueil de Enzyme](http://airbnb.io/enzyme/)
* [Enzyme: JavaScript Testing utilities for React](https://medium.com/airbnb-engineering/enzyme-javascript-testing-utilities-for-react-a417e5e5090f)

#### Alternatives

* [AVA](https://github.com/avajs/ava)
* [Karma](https://karma-runner.github.io/)

### Linting JavaScript — ESLint

![Image](https://cdn-media-1.freecodecamp.org/images/myKgW3Etlhph7Vw0CVws1w53cEUDVXViApAo)

Un linter est un outil pour analyser statiquement le code et trouver des problèmes avec eux, prévenant potentiellement des bugs/erreurs d'exécution et en même temps, imposant un style de codage. Le temps est économisé lors des revues de pull request lorsque les relecteurs n'ont pas à laisser des commentaires pointilleux sur le style de codage. [ESLint](http://eslint.org/) est un outil pour le linting de code JavaScript qui est hautement extensible et personnalisable. Les équipes peuvent écrire leurs propres règles de linting pour imposer leurs styles personnalisés. Chez Grab, nous utilisons le preset d'Airbnb `[eslint-config-airbnb](https://www.npmjs.com/package/eslint-config-airbnb)`, qui a déjà été configuré avec le bon style de codage dans le [guide de style JavaScript d'Airbnb](https://github.com/airbnb/javascript).

Pour la plupart, l'utilisation d'ESLint est aussi simple que de modifier un fichier de configuration dans votre dossier de projet. Il n'y a pas grand-chose à apprendre sur ESLint si vous n'écrivez pas de nouvelles règles pour lui. Soyez simplement conscient des erreurs lorsqu'elles apparaissent et cherchez sur Google pour trouver le style recommandé.

**Durée estimée : 1/2 jour.** Il n'y a pas grand-chose à apprendre ici. Ajoutez ESLint à votre projet et corrigez les erreurs de linting !

#### Liens d'étude

* [Page d'accueil d'ESLint](http://eslint.org/)
* [Guide de style JavaScript d'Airbnb](https://github.com/airbnb/javascript)

#### Alternatives

* [Standard](https://github.com/feross/standard)
* [JSHint](http://jshint.com/)

### Linting CSS — stylelint

![Image](https://cdn-media-1.freecodecamp.org/images/xlGl-bTK1NJXHI9jApueNAq9jgs9IhfYOm9d)

Comme mentionné précédemment, écrire un bon CSS est notoirement difficile. L'utilisation d'outils d'analyse statique sur le CSS peut aider à maintenir la qualité de notre code CSS et le style de codage. Pour le linting CSS, nous utilisons stylelint. Comme ESLint, stylelint est conçu de manière très modulaire, permettant aux développeurs d'activer/désactiver des règles et d'écrire des plugins personnalisés pour celui-ci. En plus du CSS, stylelint est capable d'analyser SCSS et a un support expérimental pour Less, ce qui réduit la barrière pour la plupart des bases de code existantes pour l'adopter.

![Image](https://cdn-media-1.freecodecamp.org/images/HQcOykWXe5GvTuzlUrE1Og1hHb7ijBis7X6d)

Une fois que vous avez appris ESLint, apprendre stylelint serait sans effort compte tenu de leurs similitudes. stylelint est actuellement utilisé par de grandes entreprises comme [Facebook](https://code.facebook.com/posts/879890885467584/improving-css-quality-at-facebook-and-beyond/), [Github](https://github.com/primer/stylelint-config-primer) et [Wordpress](https://github.com/WordPress-Coding-Standards/stylelint-config-wordpress).

Un inconvénient de stylelint est que la fonctionnalité de correction automatique n'est pas encore complètement mature et ne peut corriger qu'un nombre limité de règles. Cependant, ce problème devrait s'améliorer avec le temps.

**Durée estimée : 1/2 jour.** Il n'y a pas grand-chose à apprendre ici. Ajoutez stylelint à votre projet et corrigez les erreurs de linting !

#### Liens d'étude

* [Page d'accueil de stylelint](https://stylelint.io/)
* [Lint your CSS with stylelint](https://css-tricks.com/stylelint/)

#### Alternatives

* [Sass Lint](https://github.com/sasstools/sass-lint)
* [CSS Lint](http://csslint.net/)

### Types — Flow

![Image](https://cdn-media-1.freecodecamp.org/images/K0WtJqxf1otU0VrXIxZGvEbjEMuo6vjJLHwG)

La typage statique apporte de nombreux avantages lors de l'écriture d'applications. Ils peuvent attraper des bugs et des erreurs courants dans votre code tôt. Les types servent également de forme de documentation pour votre code et améliorent la lisibilité de votre code. À mesure qu'une base de code grandit, nous voyons l'importance des types car ils nous donnent une plus grande confiance lorsque nous faisons du refactoring. Il est également plus facile d'intégrer de nouveaux membres de l'équipe au projet lorsqu'il est clair quelles valeurs chaque objet contient et quels paramètres chaque fonction attend et retourne.

> Ajouter des types à votre code s'accompagne du compromis d'une verbosité accrue et d'une courbe d'apprentissage de la syntaxe. Mais ce coût d'apprentissage est payé d'avance et amorti sur le long terme. Dans des projets complexes où la maintenabilité du code compte et où les personnes travaillant dessus changent avec le temps, ajouter des types au code apporte plus d'avantages que d'inconvénients.

Récemment, j'ai dû corriger un bug dans une base de code que je n'avais pas touchée depuis des mois. C'est grâce aux types que j'ai pu facilement me rafraîchir la mémoire sur ce que faisait le code, et cela m'a donné confiance dans la correction que j'ai apportée.

Les deux principaux concurrents pour ajouter des types statiques à JavaScript sont [Flow](https://flow.org/) (par Facebook) et [TypeScript](https://www.typescriptlang.org/) (par Microsoft). À ce jour, il n'y a pas de vainqueur clair dans cette bataille. Pour l'instant, nous avons fait le choix d'utiliser Flow. Nous trouvons que Flow a une courbe d'apprentissage plus faible par rapport à TypeScript et qu'il nécessite relativement moins d'efforts pour migrer une base de code existante vers Flow. Étant construit par Facebook, Flow a une meilleure intégration avec l'écosystème React dès la sortie de la boîte. [James Kyle](https://twitter.com/thejameskyle), l'un des auteurs de Flow, a [écrit](http://thejameskyle.com/adopting-flow-and-typescript.html) une comparaison entre l'adoption de Flow et TypeScript.

De toute façon, il n'est pas extrêmement difficile de passer de Flow à TypeScript car la syntaxe et la sémantique sont assez similaires, et nous réévaluerons la situation à l'avenir. Après tout, utiliser l'un est mieux que de n'utiliser aucun.

Flow a récemment repensé leur page d'accueil et elle est assez bien maintenant !

**Durée estimée : 1 jour.** Flow est assez simple à apprendre car les annotations de type semblent être une extension naturelle du langage JavaScript. Ajoutez des annotations Flow à votre projet et embrassez le pouvoir des systèmes de types.

#### Liens d'étude

* [Page d'accueil de Flow](https://flow.org/)
* [TypeScript vs Flow](https://github.com/niieani/typescript-vs-flowtype)

#### Alternatives

* [TypeScript](https://www.typescriptlang.org/)

### Système de build — webpack

![Image](https://cdn-media-1.freecodecamp.org/images/A1zdHvG5RcAXEhRNWicSGqZkolrffGTOclBA)

Cette partie sera courte car la configuration de webpack peut être un processus fastidieux et pourrait décourager les développeurs qui sont déjà submergés par le barrage de nouvelles choses qu'ils doivent apprendre pour le développement front-end. En résumé, [webpack](https://webpack.js.org/) est un bundler de modules qui compile un projet front-end et ses dépendances en un bundle final à servir aux utilisateurs. Habituellement, les projets auront déjà la configuration webpack mise en place et les développeurs n'auront rarement à la changer. Avoir une compréhension de webpack est toujours un atout à long terme. C'est grâce à webpack que des fonctionnalités comme le rechargement à chaud et les modules CSS sont rendues possibles.

Nous avons trouvé le [tutoriel webpack](https://survivejs.com/webpack/foreword/) de SurviveJS être la meilleure ressource pour apprendre webpack. C'est un bon complément à la documentation officielle et nous recommandons de suivre le tutoriel en premier et de se référer à la documentation plus tard lorsque le besoin de personnalisation supplémentaire se présente.

**Durée estimée : 2 jours (Optionnel).**

#### Liens d'étude

* [Page d'accueil de webpack](https://webpack.js.org/)
* [SurviveJS — Webpack: From apprentice to master](https://survivejs.com/webpack/foreword/)

#### Alternatives

* [Rollup](https://rollupjs.org/)
* [Browserify](http://browserify.org/)

### Gestion des paquets — Yarn

![Image](https://cdn-media-1.freecodecamp.org/images/sKqHPiNFXJTUcDdMQBTd3V58X9ycF7qjdBKE)

Si vous jetez un coup d'œil dans votre répertoire `node_modules`, vous serez horrifié par le nombre de répertoires qu'il contient. Chaque plugin babel, chaque fonction lodash, est un paquet à part entière. Lorsque vous avez plusieurs projets, ces paquets sont dupliqués dans chaque projet et ils sont largement similaires. Chaque fois que vous exécutez `npm install` dans un nouveau projet, ces paquets sont téléchargés encore et encore même s'ils existent déjà dans un autre projet de votre ordinateur.

Il y avait aussi le problème de non-déterminisme dans les paquets installés via `npm install`. Certaines de nos builds CI échouent car au moment où le serveur CI installe les dépendances, il a récupéré des mises à jour mineures de certains paquets qui contenaient des changements cassants. Cela ne se serait pas produit si les auteurs de bibliothèques respectaient [semver](http://semver.org/) et si les ingénieurs n'avaient pas supposé que les contrats d'API seraient toujours respectés.

[Yarn](https://yarnpkg.com/) résout ces problèmes. Le problème de non-déterminisme des paquets installés est géré via un fichier `yarn.lock`, qui garantit que chaque installation résulte dans la même structure de fichiers exacte dans `node_modules` sur toutes les machines. Yarn utilise un répertoire de cache global dans votre machine, et les paquets qui ont déjà été téléchargés n'ont pas besoin d'être téléchargés à nouveau. Cela permet également l'installation hors ligne des dépendances !

Les commandes Yarn les plus courantes peuvent être trouvées [ici](https://yarnpkg.com/en/docs/usage). La plupart des autres commandes yarn sont similaires aux équivalents `npm` et il est acceptable d'utiliser les versions `npm` à la place. L'une de nos commandes préférées est `yarn upgrade-interactive` qui facilite la mise à jour des dépendances, surtout lorsque le projet JavaScript moderne nécessite tant de dépendances de nos jours. N'hésitez pas à la consulter !

npm@5.0.0 a été [publié en mai 2017](https://github.com/npm/npm/releases/tag/v5.0.0) et semble répondre à de nombreux problèmes que Yarn vise à résoudre. Restez à l'affût !

**Durée estimée : 2 heures.**

#### Liens d'étude

* [Page d'accueil de Yarn](https://yarnpkg.com/)
* [Yarn: A new package manager for JavaScript](https://code.facebook.com/posts/1840075619545360)

#### Alternatives

* [Le bon vieux npm](https://github.com/npm/npm/releases/tag/v5.0.0)

### Intégration continue

Nous utilisons [Travis CI](https://travis-ci.com/) pour notre pipeline d'intégration continue (CI). Travis est un CI très populaire sur Github et sa fonctionnalité de [matrice de build](https://docs.travis-ci.com/user/customizing-the-build#Build-Matrix) est utile pour les dépôts qui contiennent plusieurs projets comme ceux de Grab. Nous avons configuré Travis pour faire ce qui suit :

* Exécuter le linting pour le projet.
* Exécuter les tests unitaires pour le projet.
* Si les tests passent :
* La couverture de test générée par Jest est téléchargée sur [Codecov](https://codecov.io/).
* Générer un bundle de production avec webpack dans un répertoire `build`.
* `tar` le répertoire `build` en `<hash>.tar` et le télécharger sur un bucket S3 qui stocke toutes nos builds tar.
* Publier une notification sur Slack pour informer du résultat de la build Travis.

#### Liens d'étude

* [Page d'accueil de Travis](https://travis-ci.com/)
* [Page d'accueil de Codecov](https://codecov.io/)

#### Alternatives

* [Jenkins](https://jenkins.io/)
* [CircleCI](https://circleci.com/)

### Hébergement — Amazon S3

Traditionnellement, les serveurs web qui reçoivent une demande pour une page web rendent le contenu sur le serveur et retournent une page HTML avec du contenu dynamique destiné au demandeur. Cela est connu sous le nom de rendu côté serveur. Comme mentionné précédemment dans la section sur les applications monopage, les applications web modernes n'impliquent pas de rendu côté serveur, et il suffit d'utiliser un serveur web qui sert des fichiers d'actifs statiques. Nginx et Apache sont des options possibles et peu de configuration est nécessaire pour faire fonctionner les choses. La mise en garde est que le serveur web devra être configuré pour router toutes les requêtes vers un seul point d'entrée et permettre au routage côté client de prendre le relais. Le flux pour le routage front-end se déroule comme suit :

1. Le serveur web reçoit une requête HTTP pour une route particulière, par exemple `/users/john`.
2. Peu importe la route que le serveur reçoit, il sert `index.html` depuis le répertoire des actifs statiques.
3. Le fichier `index.html` doit contenir des scripts qui chargent un framework/bibliothèque JavaScript qui gère le routage côté client.
4. La bibliothèque de routage côté client lit la route actuelle et communique avec le framework MVC (ou équivalent le cas échéant) concernant la route actuelle.
5. Le framework JavaScript MVC rend la vue souhaitée en fonction de la route, éventuellement après avoir récupéré des données depuis une API si nécessaire. Par exemple, charger `UsersController`, récupérer les données utilisateur pour le nom d'utilisateur `john` au format JSON, combiner les données avec la vue et les rendre sur la page.

Une bonne pratique pour servir du contenu statique est d'utiliser la mise en cache et de les placer sur un CDN. Nous utilisons [Amazon Simple Storage Service (S3)](https://aws.amazon.com/s3/) car il peut à la fois héberger et servir de CDN pour notre contenu de site web statique. Nous trouvons que c'est une solution abordable et fiable qui répond à nos besoins. S3 offre l'option « Utiliser ce bucket pour héberger un site web », qui dirige essentiellement les requêtes pour toutes les routes vers la racine du bucket, ce qui signifie que nous n'avons pas besoin de nos propres serveurs web avec des configurations de routage spéciales.

Un exemple d'application web que nous hébergeons sur S3 est [Hub](https://hub.grab.com/).

En plus d'héberger le site web, nous utilisons également S3 pour héberger les fichiers `.tar` de build générés à partir de chaque build Travis réussi.

#### Liens d'étude

* [Page d'accueil d'Amazon S3](https://aws.amazon.com/s3/)
* [Héberger un site web statique sur Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html)

#### Alternatives

* [Google Cloud Platform](https://cloud.google.com/storage/docs/hosting-static-website)
* [Now](https://zeit.co/now)

### Déploiement

La dernière étape pour livrer le produit à nos utilisateurs est le déploiement. Nous utilisons [Ansible Tower](https://www.ansible.com/tower) qui est un logiciel d'automatisation puissant qui nous permet de déployer nos builds facilement.

Comme mentionné précédemment, tous nos commits, après un build réussi, sont téléchargés vers un bucket S3 central pour les builds. Nous suivons semver pour nos releases et avons des commandes pour générer automatiquement les notes de release pour la dernière release. Lorsqu'il est temps de publier, nous exécutons une commande pour taguer le dernier commit et le pousser vers notre environnement d'hébergement de code. Travis exécutera les étapes de CI sur ce commit tagué et téléchargera un fichier tar (comme `1.0.1.tar`) avec la version vers notre bucket S3 pour les builds.

Sur Tower, nous devons simplement spécifier le nom du `.tar` que nous voulons déployer vers notre bucket d'hébergement, et Tower fait ce qui suit :

1. Télécharge le fichier `.tar` souhaité depuis notre bucket S3 de builds.
2. Extrait le contenu et remplace le fichier de configuration pour l'environnement spécifié.
3. Télécharge le contenu vers le bucket d'hébergement.
4. Publie une notification sur Slack pour informer du déploiement réussi.

Ce processus complet est effectué en moins de 30 secondes et l'utilisation de Tower a rendu les déploiements et les retours en arrière faciles. Si nous réalisons qu'un déploiement défectueux a eu lieu, nous pouvons simplement trouver le tag stable précédent et le déployer.

#### Liens d'étude

* [Page d'accueil d'Ansible Tower](https://www.ansible.com/tower)

### Le voyage ne fait que commencer

Félicitations pour être arrivé jusqu'ici ! Le développement front-end aujourd'hui est [difficile](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f), mais il est aussi plus intéressant qu'avant. Ce que nous avons couvert jusqu'à présent aidera tout nouvel ingénieur de l'équipe web de Grab à se mettre rapidement à niveau avec nos technologies. Il y a beaucoup plus de choses à apprendre, mais construire une base solide dans les essentiels aidera à apprendre le reste des technologies. Cette [feuille de route pour les développeurs web front-end](https://github.com/kamranahmedse/developer-roadmap#-front-end-roadmap) utile montre les technologies alternatives disponibles pour chaque aspect.

[Grab](https://www.grab.com/) est la principale plateforme de transport en Asie du Sud-Est (SEA) et notre mission est de faire avancer la SEA, en tirant parti de la dernière technologie et des personnes talentueuses que nous avons dans l'entreprise. En mai 2017, Grab gère [2,3 millions de trajets par jour](https://www.bloomberg.com/news/videos/2017-05-11/tans-says-company-has-more-than-850-000-drivers-video) et nous grandissons et embauchons à un rythme rapide.

Par conséquent, nous avons pris nos décisions techniques en fonction de ce qui était important pour une équipe d'ingénierie de Grab en croissance rapide — la maintenabilité et la stabilité de la base de code. Ces décisions peuvent ou non s'appliquer à des équipes et projets plus petits. Évaluez ce qui fonctionne le mieux pour vous et votre entreprise.

À mesure que l'écosystème front-end grandit, nous explorons, expérimentons et évaluons activement comment les nouvelles technologies peuvent rendre notre équipe plus efficace et améliorer notre productivité. Nous espérons que cet article vous a donné un aperçu des technologies front-end que nous utilisons chez Grab. Si ce que nous faisons vous intéresse, [nous recrutons](https://grab.careers/) !

Si vous avez aimé cet article, n'oubliez pas de laisser un ? (Saviez-vous que vous pouvez applaudir plus d'une fois ? Essayez et voyez par vous-même !). Vous pouvez également nous suivre sur F[acebook](https://www.facebook.com/grabengineering/) et T[witter.](https://twitter.com/grabengineering)

_Cet article a été initialement publié sur le [Blog d'Ingénierie de Grab](http://engineering.grab.com/grabs-front-end-study-guide). Le guide d'étude original peut être trouvé sur [Github](https://github.com/grab/front-end-guide) et les futures mises à jour y seront apportées._

[**grab/front-end-guide**](https://github.com/grab/front-end-guide)
[_front-end-guide - ? Guide d'étude et introduction à la pile front-end moderne._github.com](https://github.com/grab/front-end-guide)

_Rédigé par [Tay Yang Shun](https://github.com/yangshun). Un grand merci à [Joel Low](https://github.com/lowjoel), [Li Kai](https://github.com/li-kai) et [Tan Wei Seng](https://github.com/xming13) qui ont révisé les brouillons de cet article._

_Vous préparez-vous pour des entretiens techniques front-end ? Consultez ce [manuel](https://github.com/yangshun/front-end-interview-handbook) qui contient des réponses aux célèbres questions d'entretien pour un poste front-end._

[**yangshun/front-end-interview-handbook**](https://github.com/yangshun/front-end-interview-handbook)
[_front-end-interview-handbook - ? Réponses presque complètes aux "Questions d'entretien pour un poste front-end"_github.com](https://github.com/yangshun/front-end-interview-handbook)

### Plus de lectures

**Général**

* [State of the JavaScript Landscape: A Map for Newcomers](http://www.infoq.com/articles/state-of-javascript-2016)
* [The Hitchhiker’s guide to the modern front end development workflow](http://marcobotto.com/the-hitchhikers-guide-to-the-modern-front-end-development-workflow/)
* [How it feels to learn JavaScript in 2016](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f#.tmy8gzgvp)
* [Roadmap to becoming a web developer in 2017](https://github.com/kamranahmedse/developer-roadmap#-frontend-roadmap)
* [Modern JavaScript for Ancient Web Developers](https://trackchanges.postlight.com/modern-javascript-for-ancient-web-developers-58e7cae050f9)

**Autres guides d'étude**

* [A Study Plan To Cure JavaScript Fatigue](https://medium.freecodecamp.com/a-study-plan-to-cure-javascript-fatigue-8ad3a54f2eb1#.c0wnrrcwd)
* [JS Stack from Scratch](https://github.com/verekia/js-stack-from-scratch)
* [A Beginner’s JavaScript Study Plan](https://medium.freecodecamp.com/a-beginners-javascript-study-plan-27f1d698ea5e#.bgf49xno2)