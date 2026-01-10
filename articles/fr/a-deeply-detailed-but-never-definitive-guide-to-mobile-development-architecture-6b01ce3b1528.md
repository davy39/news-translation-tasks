---
title: Un guide profondément détaillé mais jamais définitif sur l'architecture du
  développement mobile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T16:34:24.000Z'
originalURL: https://freecodecamp.org/news/a-deeply-detailed-but-never-definitive-guide-to-mobile-development-architecture-6b01ce3b1528
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kHze88HBCkKt8Tw4MESC9Q.png
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Un guide profondément détaillé mais jamais définitif sur l'architecture
  du développement mobile
seo_desc: 'By Jose Berardo Cunha

  Native, Web, PWA, hybrid, Cross-Compiled… what is “the best” way to develop for
  Android and iOS platforms? What looks reasonable? And how are you supposed to choose
  among the options? In this article, I’ll lay it all out so you ...'
---

Par Jose Berardo Cunha

Native, Web, PWA, hybride, Cross-Compiled… quelle est la « meilleure » façon de développer pour les plateformes Android et iOS ? Qu'est-ce qui semble raisonnable ? Et comment êtes-vous censé choisir parmi les options ? Dans cet article, je vais tout expliquer pour que vous puissiez prendre une décision éclairée.

Tout d'abord, permettez-moi de vous fournir un peu de contexte. Je suis consultant senior en informatique, et l'idée de mettre ensemble ce guide est née de discussions avec l'un de nos clients sur ce qui pourrait être la meilleure approche pour eux. Oui, juste pour eux. Et nous avons réalisé que nous n'avions pas de stratégie bien définie, une base solide et fiable, pour nous aider à trouver la bonne réponse.

Et vous savez quoi ? Je n'ai pas non plus trouvé un tel guide facilement sur Internet. Bien qu'il existe plusieurs articles sur ce sujet, aucun de ceux que j'ai rencontrés n'était raisonnablement complet. Malheureusement, la majorité néglige beaucoup de concepts ou, pire encore, sont essentiellement faux.

Maintenant, j'aimerais avoir une vue plus large. Et tandis que j'aide potentiellement quelqu'un à prendre ses propres décisions, je demande également à la communauté plus de réflexions sur le sujet.

Ce guide se compose de deux parties :

1. Niveaux architecturaux du développement mobile (celui-ci)
2. Comment prendre votre décision

Il est également disponible sur [YouTube sous forme de série de 10 vidéos](https://www.youtube.com/watch?v=B_vADCc-3HI&list=PLrUPmiKGH0g6TyS3F_FqOxnxWNXhZBqkR) et en tant que [cours gratuit sur Udemy](https://www.udemy.com/mobile-development-architecture). Là, vous trouverez le même matériel écrit qu'ici, les mêmes vidéos de la série YouTube, ainsi que des quiz pour fixer tous les sujets et une certification finale.

Alors, commençons.

### Introduction

En ce qui concerne les plateformes mobiles, [il est discutable qu'il n'y ait que deux grands acteurs](http://gs.statcounter.com/os-market-share/mobile/worldwide) : Android et iOS. D'autres technologies comme Tizen, Blackberry ou Windows Phone sont soit mortes, soit présentes depuis un certain temps et n'ont aucune perspective d'atteindre une part de marché significative.

Un rapide coup d'œil à ce duopole massif pourrait vous faire penser que les développeurs n'ont pas beaucoup d'options lors de la création d'applications mobiles. Cette idée ne pourrait pas être plus éloignée de la vérité, cependant. Vous pouvez rapidement repérer une poignée de langages de programmation utilisés : C/C++, Java, Kotlin, Objective-C, Swift, JavaScript, TypeScript, C#, Dart, Ruby, et je suis sûr d'en avoir oublié quelques-uns.

Il en va de même pour les frameworks de développement mobile. À moins que vous ne soyez pas développeur, ou que vous n'ayez pas été au courant des nouvelles technologies au cours des 10 dernières années, vous avez probablement entendu parler de Cordova/PhoneGap, React Native, Xamarin, Ionic, Nativescript ou Flutter, pour ne citer que quelques solutions multiplateformes pour les applications mobiles.

Alors, examinons tous ces éléments de l'architecture et décomposons un peu les choses.

#### TL;DR

Il n'y a pas de gagnant clair. Toutes les approches ont des avantages et des inconvénients, et peuvent être soit les mieux adaptées, soit les moins adaptées pour votre prochain projet. Dans ce guide, je classe de nombreuses solutions différentes en divers niveaux selon la distance de leurs architectures par rapport à la plateforme native.

### Applications Natives

Pour commencer, allons directement au cœur du sujet. Notre premier niveau architectural est celui des Applications Natives.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y6li0mJWKGdZ95utOH7meA.png)
_Niveau des Applications Natives — Où vous développez pour chaque plateforme spécifique (cela peut être encore plus spécifique lorsque l'on considère le NDK)_

C'est le niveau où vous devez être conscient des idiosyncrasies de chaque plateforme. Ce n'est pas mon intention de m'y attarder, je veux juste mentionner quelques choses dans un peu de contexte.

#### iOS

En commençant par iOS, simplement parce que c'est plus simple, il n'y a qu'Apple qui règne sur le monde. À l'origine, les développeurs devaient apprendre l'Objective-C, une variation orientée objet propriétaire de C avec une certaine inspiration de SmallTalk ([et une API au nom incroyablement long](https://mackuba.eu/2010/10/31/the-longest-names-in-cocoa/) ).

En 2014, Apple a annoncé Swift, un langage multi-paradigme, qui était beaucoup plus facile que son prédécesseur. Il est toujours possible de gérer le code hérité Objective-C, mais Swift a atteint des niveaux de maturité élevés. Donc, si vous prévoyez d'apprendre à développer nativement pour iOS, Swift est définitivement là où vous devriez commencer.

#### Android

Côté Android, il y a un certain nombre de fabricants différents. [La grande majorité d'entre eux s'appuient sur des processeurs ARM](https://www.androidpit.com/fastest-smartphone-processors). Mais en général, les applications Android reposent sur des instances de machines virtuelles ([instances d'ART](https://developer.android.com/guide/platform/index.html#art)) pour aider à gérer les spécificités sous-jacentes potentielles ([non sans de nombreux trucs incroyables](https://source.android.com/devices/tech/dalvik/#features)).

C'est pourquoi, à l'origine, le langage de choix était Java. Non seulement il a été le langage le plus populaire au monde pendant près de deux décennies ([avec quelques échanges de position avec C](https://www.tiobe.com/tiobe-index/)), mais il est également notable pour sa machine virtuelle Java (JVM). Cela a permis aux développeurs de compiler leur code en bytecode intermédiaire qui pouvait être lu et exécuté par la JVM.

Avec le kit de développement natif Android (NDK), il est également possible de développer des parties critiques de l'application directement en code natif, en écrivant en C/C++. Dans ce cas, vous devez être conscient des particularités de la plateforme sous-jacente.

Kotlin est un langage dévoilé par JetBrains en 2011. Lorsqu'il est sorti pour la première fois, malgré sa flexibilité et sa concision, il n'était pas plus qu'un autre langage JVM avec des concurrents plus réussis comme Scala, Clojure ou Groovy. Cependant, après sa première version majeure en 2016, il a rapidement commencé à se démarquer, surtout après que Google a annoncé qu'il serait officiellement pris en charge sur la plateforme Android lors de la [Google I/O 2017](https://www.youtube.com/watch?v=EtQ8Le8-zyo).

Kotlin devient le langage de première classe de Google (actuellement Kotlin et Java — dans cet ordre — sont utilisés dans toute la documentation officielle d'Android). Un remplacement total de Java est attendu encore plus maintenant que la Cour d'appel fédérale des États-Unis a statué sur le [procès sans fin](http://money.cnn.com/2018/03/27/news/companies/google-oracle-case/index.html) intenté par Oracle accusant Google de violer les droits d'auteur de Java.

### Composants natifs

En développant dans ce niveau, vous pouvez également tirer parti de toutes les API natives et, en particulier, des composants natifs. Cela évite à votre application de devoir réinventer la roue.

J'ai publié une vidéo de démonstration sur la façon de créer un projet simple sur Xcode (iOS) et Android Studio. Si vous voulez la consulter :

#### Avantages des applications natives

* Meilleure performance et meilleur engagement utilisateur
* Fonctionnalités natives de pointe
* IDE très performants Android Studio / Xcode
* Langages modernes de haut niveau Kotlin / Swift
* Approche très bas niveau avec NDK

#### Inconvénients des applications natives

* Deux bases de code à maintenir
* Nécessitent une installation (sauf Android Instant Apps)
* Difficile à analyser pour le SEO
* Très coûteux pour inciter les utilisateurs à télécharger l'application

### Applications Web

De l'autre côté du spectre, nous avons les Applications Web. Les Applications Web sont essentiellement des applications exécutées par le navigateur. Vous n'écrivez pas de code ciblant la plateforme, mais plutôt tout navigateur fonctionnant par-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HIDGvnpanv4vQ3vLrc7IhA.png)
_Niveau des Applications Web — clairement au-dessus d'une barre de navigateur ciblant une bête située entre Android et iOS._

Dans ce niveau, vous trouverez un nombre insensé de concurrents se disputant. Mais ils utilisent tous un arsenal constitué des mêmes armes : HTML, CSS et Javascript.

Les frameworks et bibliothèques Web, même lorsqu'ils utilisent des pré-compilateurs CSS comme [LESS](http://lesscss.org/) ou [SASS](https://sass-lang.com/), même les langages pré-compilés JavaScript comme [TypeScript](http://www.typescriptlang.org/), [CoffeeScript](https://coffeescript.org/) ou [Flow](https://flow.org/en/), même les symbiose comme [JSX](https://reactjs.org/docs/introducing-jsx.html) ou [Elm](http://elm-lang.org/), en laissant de côté des outils comme [Babel](https://babeljs.io/) utilisés pour transpiler tout en JavaScript avec différents niveaux configurables de conformité avec les spécifications annuelles d'ECMAScript (ES6 / ES7 / ES8, ou si vous préférez ES2015 / ES2016 / ES2017 / ES2018).

À la fin de la journée, ils sont tous du HTML, du CSS et du JavaScript rendus et exécutés par le navigateur. Il n'y a pas d'accès direct aux API natives comme la caméra, la vibration, l'état de la batterie ou le système de fichiers, mais certaines d'entre elles peuvent être atteintes via les API Web :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JZu_xrK3KAbCL_qaIS4jHw.png)
_[Puis-je compter sur les fonctionnalités de la plateforme Web pour construire mon application ?](https://whatwebcando.today" rel="noopener" target="_blank" title=")_

Le gros problème avec les API Web est leur niveau de maturité. Beaucoup d'entre elles ne sont pas supportées par certains navigateurs. Il y a des différences dans les implémentations, surtout entre les navigateurs mobiles.

#### Avantages des applications Web

* Code partagé entre les plateformes et les navigateurs de bureau
* Ne nécessitent pas d'installation préalable, il suffit de naviguer et d'utiliser
* Des tonnes de frameworks et de bibliothèques pour les accompagner
* Meilleur pour le SEO

#### Inconvénients des applications Web

* Performance inférieure
* Difficile d'obtenir une expérience utilisateur native
* Nécessitent une connexion Internet
* Non disponibles sur les magasins d'applications officiels
* API pas aussi mature et fiable que l'API native

### Frameworks et composants Web

[Angular](https://angular.io/), [React](https://reactjs.org/), et [Vue](https://vuejs.org/) sont probablement les frameworks Web les plus populaires en 2018. Pour être précis, cependant, React est considéré comme une simple bibliothèque en raison de sa nature flexible et moins dogmatique. Angular, en revanche, est un framework très dogmatique. Vue se situe quelque part entre les deux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hWUMcJv-8wWJni6PDOAAaQ.png)
_Angular vs React vs Vue_

Angular, à l'origine appelé [AngularJS](https://angularjs.org/), a été présenté au monde en 2010 par Google. Il a rapidement commencé à briller, grâce à son inversion de paradigmes par rapport à d'autres bibliothèques de l'époque (comme [jQuery](https://jquery.com/), la plus populaire à l'époque). Au lieu de parler directement aux éléments HTML pour manipuler l'état de l'UI, avec AngularJS, les templates étaient magiquement mis à jour chaque fois que le modèle JavaScript était mis à jour.

Alors qu'AngularJS devenait de plus en plus populaire, il a également grandi en termes de fonctionnalités. Il est devenu un framework complet et dogmatique qui a été l'un des premiers à prendre au sérieux les SPAs (Single Page Apps). Cette croissance (dans les deux aspects) a été responsable de certains problèmes de performance et de bloat de l'API.

React a été créé par Facebook pour résoudre leurs propres besoins au niveau de la couche de présentation. Il a introduit de nombreux aspects qui sont soudainement devenus très populaires, comme le DOM virtuel, le flux de données unidirectionnel (à l'origine nommé [Flux](https://facebook.github.io/flux/docs/in-depth-overview.html#content), surtout populaire à travers une bibliothèque d'implémentation appelée [Redux](https://redux.js.org/)), et un mélange de HTML et JavaScript appelé [JSX](https://reactjs.org/docs/introducing-jsx.html).

Ce n'est qu'en 2016, après de longs débats et des changements majeurs inattendus, que Google a lancé la version deux de son populaire framework web. Ils l'ont appelé Angular, au lieu d'AngularJS. Mais, comme beaucoup de gens appelaient déjà la première version « Angular » (sans le suffixe « JS »), les gens ont commencé à appeler la nouvelle version Angular 2. Cela a posé un problème de nommage, car Google a également annoncé qu'il publierait de nouvelles versions majeures tous les 6 mois.

À mon avis, c'était une erreur monumentale. J'ai déjà vu cela auparavant (avec Struts vs Struts 2/WebWork, par exemple). Ils ont un produit massivement populaire qui semble avoir atteint son plateau, et il a commencé à être plus critiqué qu'applaudit. Si Google décide de le reconstruire à partir de zéro, ils ne devraient jamais, en aucun cas, simplement changer sa version majeure. Comment les gens peuvent-ils faire confiance à ce qu'ils ne répéteront pas cela à chaque nouvelle version majeure ? La version deux est censée présenter des changements majeurs, mais cela ne signifie pas qu'elle peut être totalement révisée.

Angular est un framework web spectaculaire, et je m'y intéresse vraiment. Cependant, c'est une bête complètement nouvelle. Il n'a pas grand-chose à voir avec AngularJS. Même Vue, qui est un autre framework incroyable (probablement l'un des plus agréables à utiliser, d'ailleurs) ressemble plus à AngularJS à vol d'oiseau. Je pense que cela a provoqué un mouvement significatif loin d'Angular et a contribué de manière substantielle à la popularité de React.

Vue est le seul des trois frameworks web les plus populaires qui ne soit pas soutenu par une grande entreprise. Il a en fait été lancé par un ancien développeur de Google. Grâce à sa simplicité formidable et à son empreinte minuscule, il a attiré l'attention d'une communauté massive et enthousiaste.

Bien qu'il existe des solutions plus complètes, elles fonctionnent toutes sur le concept de [composants web](https://www.webcomponents.org/). Il existe une spécification ouverte à leur sujet actuellement en cours chez W3C, et quelques implémentations intéressantes comme [Polymer](https://www.polymer-project.org/), [Stencil](https://stenciljs.com/) et [X-Tag](https://x-tag.github.io/).

Dans la troisième vidéo de la série, je ne passe pas trop de temps à discuter des frameworks mais je discute des bibliothèques de composants web :

### Applications Mobiles vs Applications Web

Je ne suis pas sûr que vous l'ayez remarqué, mais l'ordre des niveaux que je présente ici suit ce que je pense être le chemin le plus facile pour apprendre toutes les approches. J'ai commencé par le Niveau Natif, le développement mobile le plus authentique. Ensuite, j'ai décidé de voler directement à l'autre extrême pour présenter le Niveau Web, qui est le niveau qui a été disponible depuis les premiers smartphones.

Ce n'est que maintenant, après avoir élaboré une comparaison entre les deux extrémités de mon diagramme, que je vais commencer à parler de nombreuses approches multiplateformes pour construire des applications mobiles.

Il y a un long débat entre les Applications Mobiles et les Applications Web. Tout ce que je dis sur les Applications Mobiles n'est pas exclusif au Niveau Natif. Il est également applicable à tous les niveaux multiplateformes que je présente plus tard.

#### Le dilemme du comportement de l'utilisateur

![Image](https://cdn-media-1.freecodecamp.org/images/1*OYBXoiGa1wc3jYpxnJwUog.png)
_Les utilisateurs passent plus de temps sur les Applications Mobiles (87%) que sur les Sites Web Mobiles (13%)_

Selon une [enquête Comscore en 2017](https://www.comscore.com/layout/set/popup/Request/Presentations/2017/The-2017-US-Mobile-App-Report?logo=0&c=12), la fidélité d'un utilisateur à une application mobile est bien plus pertinente que celle aux sites web mobiles. Selon un [article aligné sur Forbes](https://www.forbes.com/sites/quora/2017/12/19/why-many-online-shopping-sites-are-becoming-mobile-shopping-apps/#1e86018f62c2), cela est généralement dû à la commodité (par exemple, les boutons de l'écran d'accueil, les widgets, les notifications en haut), à la vitesse (par exemple, des interfaces plus fluides, des démarrages presque instantanés) et aux paramètres enregistrés (par exemple, le contenu hors ligne).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Jh90US1AS-UQWB4xIwAYWw.png)
_Les Sites Web Mobiles atteignent plus de personnes (8,9M de visiteurs uniques mensuels contre 3,3M des Applications Mobiles)_

D'autre part, dans les mêmes données de Comscore, nous apprenons que les clients peuvent être atteints plus facilement à partir des sites web mobiles, car ils ne sont pas autant liés à leurs quelques applications de préférence. Si vous comparez les sites web les plus populaires avec les applications les plus téléchargées, il est estimé qu'une moyenne de 8,9 millions de visiteurs uniques par mois accèdent aux 1000 sites web les plus populaires. C'est presque trois fois plus que la moyenne des utilisateurs uniques des 1000 applications les plus téléchargées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hcjh-XXWh_j9x3iIy1BxvQ.png)
_Distribution (Application Web) x Engagement (Application Mobile)_

C'est tout une question de distribution contre engagement. Votre application web a plus de chances d'être consultée, car les utilisateurs sont plus susceptibles d'essayer de nouvelles choses lorsqu'ils naviguent sur leurs navigateurs mobiles. Mais les Applications Mobiles se sont avérées plus engageantes et captent l'attention des utilisateurs pendant des périodes beaucoup plus longues.

Maintenant que vous comprenez le dilemme, examinons les Applications Web Progressives. C'est une approche si liée au niveau des Applications Web que je la classe comme un simple addendum aux Applications Web. Mais c'est un grand perturbateur et un sérieux candidat pour la chose la plus nouvelle et la plus cool dans le développement web et mobile.

### Applications Web Progressives

Les Applications Web Progressives (PWA) sont un ensemble d'outils utilisés pour donner aux utilisateurs d'Applications Web la même expérience à laquelle ils sont habitués lorsqu'ils exécutent des Applications Mobiles. Cela signifie que les Applications Web peuvent tirer parti des niveaux potentiellement plus élevés de distribution avec des niveaux plus décents d'engagement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*raQWH9nuC6o8dY73a7dp3A.png)
_Addendum des Applications Web Progressives au niveau des Applications Web_

Google a défini trois qualifications principales pour les PWA : elles doivent être [Fiables, Rapides et Engageantes](https://developers.google.com/web/progressive-web-apps/#reliable).

Les fonctionnalités appelées [Service Workers](https://developers.google.com/web/ilt/pwa/introduction-to-service-worker) et l'[App Shell](https://developers.google.com/web/fundamentals/architecture/app-shell) sont la fondation des Applications Web Progressives. Elles ont été créées pour promouvoir la fiabilité des applications, car elles sont maintenant conçues pour fonctionner indépendamment du statut de connexion de l'appareil. Cela inclut le mode hors ligne, ainsi que les connexions médiocres. Elles fournissent également un gain de performance perçu significatif, car les applications se lancent en utilisant des données mises en cache localement, ce qui élimine les retards pour les téléchargements de contenu synchrones.

Vous pourriez considérer la fiabilité comme un vecteur indirect d'engagement. Les utilisateurs ne sont pas affectés pendant leurs trajets en train, par exemple. Ils peuvent rester engagés.

Il en va de même pour la vitesse. Selon Google :

> 53 % des utilisateurs abandonneront un site s'il met plus de 3 secondes à charger !

Cependant, être exclusivement fiable et rapide au chargement ne garantit pas nécessairement un engagement élevé. Les PWA tirent parti des fonctionnalités liées aux mobiles qui étaient autrefois exclusives aux applications mobiles, comme une option « Ajouter à l'écran d'accueil » et des Notifications Push.

En ce qui concerne la fonctionnalité « Ajouter à l'écran d'accueil », vous pourriez remarquer qu'Apple dispose d'une fonctionnalité similaire depuis le tout premier iPhone. [Certaines personnes soutiennent même que les Applications Web Progressives sont le nouveau nom fantaisiste de Google pour une idée originale d'Apple](https://youtu.be/EFGltzFSK-c?start=651).

Et vous ne pouvez pas complètement être en désaccord. Certaines idées reviennent en cycle. Elles arrivent, disparaissent, puis reviennent avec un nouveau nom et quelques améliorations (par exemple, les Service Workers), afin qu'elles puissent enfin rester.

D'autre part, il est difficile d'être complètement d'accord. Le discours de Steve Jobs sur le Web 2.0 + AJAX et l'annonce mémorable de l'iPhone lors de la WWDC 2007 ne sont pas suffisamment convaincants pour le qualifier de père, ou même de prophète, des PWA.

Pour être juste, la capacité d'ajouter à l'écran d'accueil sur l'iPhone n'a été rien de plus qu'une fonctionnalité subtile, presque cachée, pour générer des icônes de bureau qui démarrent simplement les Applications Web en mode plein écran. Elle a tout le fardeau des cycles de requête-réponse HTTP et aucun chemin clair autour des caches.

Les PWA partent du bon point. Elles explorent comment les installations précédentes des Applications Web ne sont pas nécessaires sans perdre l'amorçage côté client des Applications Mobiles. Cela signifie que tout ce dont un utilisateur a besoin pour sa première interaction après le démarrage peut être mis en cache localement (lire : App Shell) et gardé disponible dès qu'il clique sur « Ajouter à l'écran d'accueil ».

Passons à une autre caractéristique bien connue des PWA, parlons de la fonctionnalité super engageante (ou ré-engageante) du monde des Applications Mobiles : les Notifications Push. Ce sont des messages de style alerte qui apparaissent sur la barre/zone de notification supérieure, ainsi que sur les écrans de verrouillage. Ils ont le pouvoir de ramener les utilisateurs vers votre application une fois qu'ils reçoivent la notification.

Pour renforcer l'attrait des PWA, Google a regroupé toutes les API Web modernes sous l'égide des PWA. Attendez-vous donc à voir des choses comme les demandes de paiement, la gestion des identifiants, le WebVR, les capteurs, le WebAssembly et le WebRTC dans le contexte des Applications Web Progressives. Mais ces fonctionnalités ne sont pas nécessairement liées aux PWA, et certaines sont même nées avant que le terme PWA ne soit inventé.

#### PWA et Apple

Apple, en revanche, a annoncé ses premiers jalons solides vers les PWA seulement en mars 2018. [Bien qu'il y ait encore certaines limitations, les progrès sont appréciables](https://medium.com/@firt/progressive-web-apps-on-ios-are-here-d00430dee3a7). Certaines des limitations pourraient être liées au fait que Safari a pris du retard par rapport à ses concurrents. D'autres pourraient être attribuées à la philosophie de contrôle strict d'Apple.

Néanmoins, [Apple a un App Store plus rentable que Google](https://www.techrepublic.com/article/google-play-hits-record-19b-downloads-but-apples-app-store-still-makes-more-money/). Apple affirme que plus de critères sur les publications d'applications apportent plus de fiabilité globale, et les PWA sont susceptibles de nuire aux revenus de l'App Store. Cela suggère que certaines limitations qui semblent être intentionnellement imposées (comme 50 Mo de taille maximale de cache PWA) coûteront plus cher à être révoquées.

#### Malheureusement, les PWA ne sont pas parfaites

Les solutions Web et, à différents niveaux, toutes les solutions multiplateformes luttent pour atteindre l'excellence et l'exhaustivité des Applications Natives. Chaque nouvelle fonctionnalité, et chaque détail particulier à Android ou iOS, rend cette sensation native de plus en plus difficile à atteindre à mesure que vous éloignez votre application du niveau natif.

Dans l'ensemble, les PWA corrigent certains problèmes du niveau des Applications Web. Mais il y a d'autres problèmes qui ne peuvent pas être résolus par une solution fonctionnant sur un navigateur.

#### Ce que les PWA corrigent

* Plus d'expérience « native »
* Temps de chargement plus rapides
* Ne nécessitent pas de connexion Internet
* Forcent les développeurs Web à être conscients des situations où il n'y a pas de connexion ainsi que d'une mauvaise connexion
* Incorporent des fonctionnalités des Applications Mobiles comme les Notifications Push, la Géolocalisation ou la Reconnaissance Vocale

#### Ce qu'elles ne corrigent pas

* Lenteur inhérente
* Non disponibles sur les magasins d'applications (pas encore)
* Toujours pas entièrement supportées par tous les navigateurs
* Manquent toujours de fonctionnalités mobiles comme le NFC, la Lumière Ambiante, le Géofencing
* Manquent également de support pour les particularités d'Android ou d'iOS comme le PiP, les bannières d'applications intelligentes, les widgets d'écran de lancement et le 3D touch

Dans la vidéo ci-dessous, je fais un bref aperçu des PWA.

### Applications Hybrides

À ce niveau, nous commençons à plonger dans le monde des Applications Mobiles. Nous allons commencer par le niveau le plus éloigné : les Applications Hybrides.

Le terme Hybride est également couramment appliqué à toutes les solutions multiplateformes. Ici, cependant, je le restreins aux Applications qui fonctionnent à l'intérieur de composants mobiles, appelés WebViews.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hk7QdcVm2K8NpPd0FXrZBQ.png)
_Le niveau des Applications Hybrides. En dessous de la ligne du navigateur mais au-dessus des WebViews_

Dans les démonstrations de la deuxième vidéo, mon objectif en ajoutant WebView comme exemple Hello World était de clarifier qu'il existe un composant natif pour chaque plateforme capable de fonctionner comme un navigateur réel.

#### Cordova/PhoneGap

Des solutions comme [Cordova](https://cordova.apache.org/)/[PhoneGap](https://phonegap.com/) comblent l'écart (désolé pour le jeu de mots peu inspiré) entre les Applications Web et Mobiles. Elles fournissent des outils pour empaqueter le code HTML, JavaScript et CSS du développeur (ainsi que tout autre actif comme des images ou des vidéos) et les transformer en Applications Mobiles (oui, de vraies applications Android ou iOS). Ces applications ont leur WebView exclusif pour interpréter et exécuter le code web original, en commençant par le fichier « index.html » dans le dossier principal de l'application (normalement appelé « www »). Elles font également le pont entre le code JavaScript et les API natives via des plugins qui sont partiellement implémentés en JavaScript et partiellement dans un langage natif.

Alors, clarifions les choses. Les Applications Hybrides sont capables d'accéder aux API natives (au lieu des API Web), mais elles sont enfermées dans la WebView. Un bouton avec Cordova doit être un bouton HTML rendu par une WebView au lieu d'un bouton natif mobile.

C'est le niveau magique qui permet aux entreprises de porter leurs Applications Web vers des Applications Mobiles pour être distribuées par les magasins d'applications. Donc, tout framework web est autorisé ici.

#### Ionic

Des frameworks comme [Ionic](https://www.ionicframework.com/) enveloppent Cordova dans leurs propres solutions. Avec Ionic, vous n'avez pas besoin d'utiliser l'interface de ligne de commande (CLI) de Cordova, car toutes ses commandes sont enveloppées par le CLI d'Ionic.

Récemment, l'équipe Ionic a décidé de prendre les rênes de toute la pile des Applications Hybrides. Ils ont donc lancé un remplacement proposé pour Cordova appelé [Capacitor](https://capacitor.ionicframework.com/). Capacitor prend en charge les plugins Cordova et peut également être utilisé par un projet non-Ionic.

Vous pouvez me regarder passer par un exemple Hello World de Cordova dans la cinquième vidéo de la série :

#### Avantages des Applications Hybrides

* Ce sont essentiellement des applications web qui peuvent être distribuées sur les magasins d'applications officiels
* Peuvent être utilisées avec n'importe quel framework/bibliothèque JavaScript
* Le code est toujours très partageable entre les plateformes
* Accès aux fonctionnalités natives (par exemple, caméra, accéléromètre, liste de contacts)

#### Inconvénients des Applications Hybrides

* Lutte avec les problèmes de performance et de consommation de mémoire, car les vues web sont responsables du rendu de tout à l'écran
* Doivent imiter tous les composants d'interface utilisateur natifs sur une seule vue web
* Plus difficiles à être acceptées et publiées sur l'App Store
* Prennent généralement plus de temps pour avoir les fonctionnalités natives disponibles pour ces environnements

### Web Natif

Web Natif est un niveau relativement nouveau et souvent mal compris. C'est là que les Applications Web rencontrent les composants natifs. Bien qu'Appcelerator (Axway) Titanium existe depuis longtemps, il y a quelques concurrents relativement nouveaux qui justifient de faire de cela une catégorie complètement séparée d'applications mobiles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MLfTZk4rl_3nFNW-OoXO4A.png)
_Les Applications Web Natif n'ont pas besoin de WebView car elles communiquent directement avec d'autres composants natifs_

Comme vous pouvez le voir ci-dessus, il n'y a pas de vue web pour rendre et exécuter votre application. Alors, comment votre JavaScript est-il exécuté ? Est-il compilé ? Eh bien, si vous considérez la transpilation (compilation d'un langage à un autre — par exemple TypeScript à JavaScript), le bundling, la minification, le mangling et l'obfuscation comme une compilation, oui, JavaScript est compilé.

Mais le problème est que cela ne rend pas votre JavaScript directement compréhensible par les systèmes d'exploitation Android ou iOS. Et, en théorie, il n'y a pas de composant natif qui sert uniquement de moteur JavaScript sans le fardeau du moteur de mise en page HTML.

La stratégie consiste à livrer des moteurs JavaScript (normalement [V8](https://developers.google.com/v8/) pour Android et [JavaScriptCore](https://developer.apple.com/documentation/javascriptcore) pour iOS) avec votre code. Bien qu'ils aient de petites empreintes et soient très rapides, ils sont quelque chose d'externe qui doit être fourni par votre application.

D'autre part, cette approche tend à avoir de meilleures performances d'interface utilisateur, car tous les composants sont les mêmes (ou sont basés sur la même chose pour React Native, par exemple) que ceux utilisés par les Applications Natives.

#### Avantages des Applications Web Natif

* Atteindre les deux plateformes avec une seule base de code
* À peu près les mêmes performances que les applications natives, car elles traitent également avec les composants d'interface utilisateur natifs
* Des ajustements sont nécessaires, mais le code est toujours partageable avec le développement web

#### Inconvénients des Applications Web Natif

* Même avec une seule base de code, le développeur doit être conscient des composants natifs
* Courbe d'apprentissage plus raide que les Applications Hybrides / Web pour les développeurs web, surtout en ce qui concerne la mise en page

#### React Native

Dans la partie 6 de la série, je fais un rapide Hello World dans React Native. Cela montre, dans l'inspecteur de mise en page d'Android Studio, quels composants ont été rendus dans l'émulateur. Je compare avec les exemples précédents, en m'assurant qu'il n'y a pas de WebView.

#### Nativescript

Un autre framework incroyable qui m'a particulièrement intéressé au cours des deux dernières années ([j'ai un cours sur Udemy à ce sujet](https://www.udemy.com/angular-native) — en portugais), est [Nativescript](https://www.nativescript.org/). Il est similaire à React Native mais n'est pas lié au monde React ([il existe une intégration non officielle, Nativescript-Preact, cependant](https://github.com/staydecent/nativescript-preact)).

Avec Nativescript, vous pouvez développer en utilisant du JavaScript vanilla, TypeScript, Angular et, plus récemment, Vue. Bien sûr, vous pouvez utiliser d'autres frameworks, mais ceux-ci sont les officiellement supportés. Il est également assez bien documenté, d'ailleurs.

Nativescript dispose d'outils comme [Nativescript Sidekick](https://www.nativescript.org/nativescript-sidekick) et [Nativescript Playground](https://play.nativescript.org/), ainsi que des structures de projet basées sur des [modèles](https://market.nativescript.org/?tab=templates) qui peuvent être fournis par la communauté. Cela devrait vous aider dans la création de projets, en vous donnant la capacité de démarrer, déployer, tester et exécuter sur des simulateurs dans le cloud et des appareils iPhone même lorsque vous ne développez pas en utilisant un Mac.

Dans la septième partie de la série, je fais un Hello World en utilisant Sidekick ainsi qu'un autre projet démarré à partir du CLI et un [modèle de clone WhatsApp](https://github.com/Especializa/nativescript-whatsapp-template) que j'ai créé à des fins d'apprentissage.

Il est important de jeter un coup d'œil à l'inspecteur de mise en page lorsque votre application s'exécute sur un émulateur Android. Avec Nativescript, il montre les composants natifs (encore une fois, pas de WebView), et des instances directes de classes Android courantes comme TextView. Cela est différent de React Native, qui a ses propres classes pour envelopper les composants natifs.

C'est probablement pourquoi Nativescript affirme qu'il n'y a pas de délai entre le moment où une nouvelle fonctionnalité est disponible sur iOS et Android et le moment où vous pouvez l'utiliser dans un projet Nativescript. Par exemple, [ils ont publié sur leur blog](https://www.nativescript.org/blog/preview-of-augmented-reality-in-nativescript) un projet AR le même jour où iOS 11 a été officiellement publié avec la nouvelle API ARKit.

#### Weex

Un autre framework digne d'être mentionné dans cette catégorie est [Weex](https://weex.apache.org/). C'est un projet développé par Alibaba, et est actuellement incubé à la Apache Software Foundation (ASF). Il utilise des balises HTML courantes comme `<d`iv> et des commandes CSS i`nside &`lt;style> pour appeler des composants natifs. D'après leur documentation :

> Bien que les composants dans Weex ressemblent à des balises HTML, vous ne pouvez pas tous les utiliser. Au lieu de cela, vous ne pouvez utiliser que les composants intégrés et vos composants personnalisés.

### Cross Compilé

À ce niveau, il est temps de sauter du train du Web. C'est le niveau le plus proche du développement natif, mais il a l'avantage d'utiliser une seule base de code pour cibler Android et iOS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dNq3N6jsMK3lKII2xD4bWw.png)
_Niveaux de développement maintenant complets avec les Applications Cross Compilées_

#### RubyMotion et Xamarin

Il existe des solutions comme [RubyMotion](http://www.rubymotion.com/). C'est un moyen d'écrire des applications mobiles en utilisant Ruby et de les compiler directement pour la plateforme ciblée (comme si elles avaient été créées en utilisant un langage « natif »).

Une autre option est [Xamarin](https://www.xamarin.com/), où vous écrivez en C#, compilez en un bytecode intermédiaire, et déployez votre application avec une instance du [Mono](https://www.mono-project.com/) common language runtime. Cette approche a le même inconvénient que le Web Natif (où V8 et JavaScriptCore sont livrés par votre application), mais peut également s'appuyer sur des compilations JIT pour optimiser l'application à l'exécution.

#### Flutter

Enfin, mais non des moindres, j'aimerais mentionner [Flutter](https://flutter.io/). C'est la nouvelle initiative cool de Google pour le développement mobile. Il s'inscrit dans la catégorie Cross Compilé car vous écrivez des applications en utilisant le [langage Dart](https://www.dartlang.org/) et les compilez pour la plateforme native.

Flutter a innové dans certains aspects. Probablement le plus remarquable est le fait qu'il fournit son propre ensemble de composants.

**Quoi ? Son propre ensemble de composants ?**

Oui, Flutter fournit un certain nombre de composants différents afin que vous puissiez complètement ignorer ceux de la plateforme. Il dispose de composants génériques ainsi que de composants [Material Design](https://flutter.io/widgets/material/) pour Android, et de composants [Cupertino](https://flutter.io/widgets/cupertino/) pour iOS.

Plutôt qu'une machine virtuelle .Net (comme Xamarin) ou des moteurs JavaScript (comme les frameworks Web Natif), avec Flutter votre application livrera les composants que vous décidez d'utiliser.

**Sont-ils des composants natifs ?**

Oui, ils le sont. Votre application est native, aussi. Tout est compilé pour l'architecture native. Cependant, gardez à l'esprit qu'ils ne sont pas les composants natifs préexistants.

**Quel est l'intérêt de cela ?**

Eh bien, à mon avis, cette solution est intelligente et audacieuse. J'attendais de parler des avantages et des inconvénients, mais comme ce n'est qu'une technologie particulière, permettez-moi de les aborder maintenant.

L'un des plus grands défis pour les solutions Web Natif et Cross Compilé (rappelons, au-dessus du Natif mais en dessous de la WebView dans nos niveaux) est de savoir comment gérer les composants natifs. Par exemple, un problème important est de savoir comment les disposer. C'est parce qu'ils n'ont pas été créés pour être utilisés par ces ressources externes. De plus, ils n'ont pas été créés en gardant à l'esprit une contrepartie sur l'autre plateforme. La barre de navigation Android ne fonctionne pas comme la barre de navigation UINavBar d'iOS, par exemple.

Avec Flutter, les composants sont créés en gardant toujours à l'esprit la multiplateforme. Alors, examinons les avantages et les inconvénients du niveau des Applications Cross Compilées :

#### Avantages des Applications Cross Compilées

* Atteindre les deux plateformes avec un seul langage
* À peu près les mêmes performances que les applications natives, car elles traitent également avec les composants d'interface utilisateur natifs

#### Inconvénients des Applications Cross Compilées

* Support légèrement retardé pour les dernières mises à jour de la plateforme
* Code non partageable avec le développement web
* Même avec une seule base de code, le développeur doit être conscient des composants natifs

PS : Avec Flutter, vous fournirez votre propre ensemble de widgets avec le code de votre application.

### Architecture d'exécution des Applications Mobiles

![Image](https://cdn-media-1.freecodecamp.org/images/1*BI2on3Tup2LSs5MjToEcWw.png)
_Quatre architectures d'exécution différentes pour les Applications Mobiles._

Comme vous pouvez le voir, les solutions Cross Compilées peuvent être réparties sur trois des quatre quadrants différents. En haut à gauche, vous trouvez les solutions Natives et Cross Compilées (par exemple RubyMotion), où votre application (en vert) est compilée en binaires natifs. Elle communique directement avec les Widgets OEM (Original Equipment Manufacturer widgets — ce que nous avons appelé composants natifs) ainsi qu'avec l'API native.

Le quadrant en haut à droite est exclusif aux Applications Hybrides. Votre application est nécessairement du HTML/CSS/JavaScript exécuté par la WebView native (comme nous l'avons fait dans la cinquième vidéo de la série). Cordova/PhoneGap ou Capacitor peuvent fournir un pont pour permettre à votre code JavaScript de communiquer avec les API natives.

Le quadrant en bas à gauche est où toutes les solutions Web Natif, ainsi que Xamarin, s'intègrent. Votre application n'est pas compilée en code natif (mais plutôt en un flux binaire dans Xamarin) et elle enveloppe un interpréteur pour agir comme un pont vers tout ce qui se trouve sur la plateforme.

Enfin, en bas à droite, j'aurais pu dire Cross Compilé, mais cela semble très particulier à Flutter. C'est différent des autres stratégies Cross Compilées qui semblent plus traditionnelles. Dans ce cas, il n'y a pas de pont, mais il n'y a également pas de contact avec les Widgets OEM (au moins pas besoin de cela).

Remarquez que les Applications Web (même en incluant les PWA) ne sont pas dans le graphique, car elles ne touchent pas du tout l'environnement natif.

Dans la partie 8 de la série, je discute des Applications Cross Compilées et me concentre sur Flutter avec un projet Hello World.

### Conclusion

Pour résumer, j'espère qu'il est clair pour vous qu'il n'y a pas de grand gagnant ici. Il n'est pas facile de repérer les idiosyncrasies et les points communs pour une classification générale. Mon intention n'était pas de présenter la part de marché de chaque stratégie ou d'essayer de trouver le moyen le plus productif, le plus agréable ou le plus fiable de construire des applications mobiles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yx4X3FwFbhYi51M0TCWtEw.png)
_Tous les niveaux de développement mobile avec leurs principales caractéristiques._

Mon intention était de présenter un aperçu des acteurs et des approches qu'ils adoptent, afin que vous puissiez choisir ce qui convient le mieux à vos besoins.

#### Quelques conseils pour vous aider à trouver votre chemin

Permettez-moi d'être un peu plus catégorique à ce stade et de soulever quelques questions et réponses qui, je l'espère, pavent votre chemin.

Avant de continuer, devinez quoi ? Exactement ! J'ai mis ensemble une autre vidéo couvrant ce que je m'apprête à dire :

#### **1. Mon application a-t-elle besoin de processus CPU intensifs ?**

Si la réponse est **oui** : Applications Natives.  
Rappelez-vous : plus vous descendez, plus votre application tend à être performante.

Les applications qui nécessitent une puissance de calcul intensive, par exemple le Machine Learning (même en exécutant simplement des modèles pré-entraînés), sont de bons candidats pour le niveau Natif (ou, au moins, Cross Compilé).

Si vous pensez aux jeux, vous avez peut-être entendu parler des moteurs de jeu Unreal et Unity. Ils sont la voie à suivre pour de nombreuses entreprises de jeux, et j'ai l'impression qu'ils s'intègrent quelque part dans la couche Cross Compilé. J'ai décidé de les laisser hors de cette liste simplement parce que je commence à m'inquiéter de la longueur de cet article. :)

#### **2. Mon équipe est-elle assez grande pour maintenir deux bases de code ?**

Si la réponse est **non** : Tout sauf les Applications Natives.  
Rappelez-vous : plus vous montez, plus vous êtes abstrait et indépendant de la plateforme.

C'est la plus grande chose qui retient les gens lorsqu'ils envisagent les Applications Natives. En général, deux bases de code rendent les choses coûteuses et difficiles à faire évoluer. En théorie, vous ne voulez pas avoir une application avec beaucoup plus de fonctionnalités sur Android que sur iOS, ou vice-versa.

Si les deux éléments 1 et 2 sont pertinents pour votre application, vous devez nommer celui qui est crucial. Ou, encore une fois, envisagez un terrain d'entente avec l'approche Cross Compilé.

#### **3. Que fait le mieux mon équipe ?**

Si la réponse est **C#** : Xamarin.  
Si la réponse est **Java** : Natif (Android).  
Si la réponse est **Web/JavaScript** : Du Web au Web Natif.

Cela semble évident, mais, croyez-moi, j'ai vu des cas où les gens le tiennent pour acquis. Sauf lorsque Apple est venu avec Objective-C, rejetant ainsi le pari de Steve Jobs sur une approche de type PWA pour les applications sur iPhone, toutes les solutions sont construites en gardant à l'esprit les capacités précédentes des développeurs.

#### **4. D'où viennent mes utilisateurs ?**

Si la réponse est **Inconnu** (ou autre que les magasins d'applications) : Applications Web Progressives.  
Rappelez-vous : Devoir installer des applications depuis les App Stores cause une friction supplémentaire.

Nous avons discuté du pouvoir de distribution du Web sur les applications mobiles en général (tous les niveaux en dessous du navigateur).

#### Mix d'approches

Les technologies Web vous permettent d'avoir une base de code mixte et de cibler non seulement les plateformes mobiles mais aussi les ordinateurs de bureau. Je connais des solutions comme [Electron](https://electronjs.org/) qui facilitent le déploiement de votre application sur les ordinateurs Windows, Mac ou Linux. Mais je parle de faire en sorte qu'une Application Web (ou encore mieux une PWA) partage du code avec une Application Mobile.

D'accord, vous pourriez penser que Cordova le fait plutôt décemment. Eh bien, je suis d'accord. Les Applications Hybrides sont des applications Web exécutées par une WebView, mais j'essaie toujours de vous convaincre de penser hors des sentiers battus. Et si vous voulez une Application Web, avec des templates HTML, qui partage du code avec une Application Web Natif ?

Selon le modèle architectural que vous utilisez pour structurer votre application, les choses peuvent être facilitées en réutilisant la logique métier et beaucoup de code boilerplate, comme le routage et la gestion d'état. Vous devez simplement définir deux ensembles de templates, un pour le web, un autre pour le mobile.

Il existe des projets de base pour vous aider à démarrer. Par exemple, avec [Angular-Native-Seed](https://github.com/TeamMaestro/angular-native-seed), vous démarrez un projet Angular qui est prêt à être déployé sur des appareils mobiles. Cela peut être aussi simple que de créer un fichier de template avec différentes extensions :

```
Extension                      | Plateforme------------------------------ | --------------------------.{html/scss}                   | Recommandé pour le Web.tns.{html/scss}               | Uniquement pour le mobile.tns.ios.{html/scss}           | Uniquement pour iOS.tns.android.{html/scss}       | Uniquement pour Android.tns.ios.phone.{html/scss}     | Uniquement pour iOS Phone .tns.android.phone.{html/scss} | Uniquement pour Android Phone
```

Il suffit de décorer votre composant Angular avec un `templateUrl` et le bon fichier de template sera sélectionné en fonction de la plateforme en cours d'exécution.

Dans l'extrait ci-dessus, `my-component.android.html` serait automatiquement sélectionné lors de l'exécution sur Android.

Parfois, les choses ne sont pas simples. Il y a une chance que vous ayez un composant complètement séparé juste pour une plateforme particulière. Mais avoir cela géré par votre application dans une seule base de code ne devrait pas être un gros problème.

Jetez un coup d'œil [ici](http://jkaufman.io/react-web-native-codesharing/) et voyez comment réaliser quelque chose de similaire avec React (Web) et React Native.

Cela conduit à une autre question. Quand devez-vous opter pour l'Hybride et quand devez-vous opter pour le Web Natif ?

Mon avis sur cela est le suivant : si la performance et l'expérience utilisateur native sont ce que vous visez, optez simplement pour le Web Natif. D'autre part, si garder la mise en page cohérente sur toutes les cibles est le gros problème, et que gérer deux ensembles ou plus de templates et de feuilles de style semble écrasant, optez simplement pour l'Hybride.

Comme vous pouvez le voir, en ce qui concerne le développement mobile, l'une de ces approches pourrait fonctionner pour vous. Tant que les fournisseurs ou les mainteneurs supportent leurs produits, il y a une bonne raison d'essayer chacune de celles mentionnées dans cette étude.

J'espère que cela a été utile et que vous avez apprécié ce voyage à travers de nombreuses solutions et stratégies de développement mobile différentes.

### Qu'est-ce qui suit ?

Vous avez peut-être remarqué que je n'ai pas ajouté la dernière vidéo de la série. D'accord, la voici :

Celle-ci est entièrement consacrée à vous aider à décider **quelle est la meilleure technologie mobile à apprendre en 2018**. Si vous vous demandez quelle est la meilleure technologie à choisir pour votre prochain projet, alors je dirais **cela dépend**. Je ne veux pas simplement dire **"Peu importe. Choisissez et choisissez. Je vous souhaite tout le meilleur"**. J'aimerais vous fournir un chemin pour un processus d'apprentissage plus efficace, afin que vous puissiez maîtriser plus d'une technologie rapidement. Alors, regardez cette dernière vidéo.

Il y a une convergence qui se produit à travers les plateformes mobiles et les langages deviennent de plus en plus similaires. Regardez cette dernière vidéo, même si vous ne codez pas. Je présente de nombreuses fonctionnalités de Kotlin, Swift et TypeScript. À la fin, je veux simplement que vous réalisiez qu'ils ne sont pas si différents. Faites-moi confiance. Jetez un coup d'œil à la vidéo et faites-moi savoir dans la section des commentaires. J'ai vraiment hâte d'avoir vos réflexions à ce sujet.

Merci d'avoir lu !