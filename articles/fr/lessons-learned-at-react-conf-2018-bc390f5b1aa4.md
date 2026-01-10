---
title: Leçons apprises à React Conf 2018
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-14T16:29:01.000Z'
originalURL: https://freecodecamp.org/news/lessons-learned-at-react-conf-2018-bc390f5b1aa4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XxPm9SJhbJ_NHMdFRhbxeA.jpeg
tags:
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Leçons apprises à React Conf 2018
seo_desc: 'By Yangshun Tay

  I was fortunate to have attended React Conf 2018 thanks to my managers — it was
  an awesome event. I have been watching past React Conf videos online and it was
  exciting to be able to attend the event and listen to some of the best peo...'
---

Par Yangshun Tay

J'ai eu la chance d'assister à React Conf 2018 grâce à mes managers — c'était un événement incroyable. J'ai regardé des vidéos des précédentes React Conf en ligne et c'était excitant de pouvoir assister à l'événement et d'écouter en direct certaines des meilleures personnes de l'industrie !

React Conf est un événement de deux jours avec plus de 20 intervenants sur scène. Voici un résumé des points forts, afin que les personnes qui n'ont pas pu assister à l'événement puissent apprendre de mon expérience et décider rapidement si cela vaut la peine de regarder la vidéo complète, qui peut être trouvée sur [YouTube](https://www.youtube.com/watch?v=V-QO-KO90iQ&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ).

#### Ajouter un état aux composants fonctionnels et réutiliser la logique de cycle de vie avec les Hooks React

La conférence a commencé avec une présentation de Sophie Alpert, Engineering Manager de l'équipe React chez Facebook (à cette époque) et Dan Abramov, membre de l'équipe principale de React et créateur de Redux. Sophie a commencé la présentation avec une trivia intéressante : sur Google Trends, React est également plus populaire que l'énergie renouvelable et le jus d'orange !

Elle a ensuite réitéré que depuis le début de React en 2013, sa mission était de faciliter la création de grandes interfaces utilisateur. React essaie de simplifier les choses qui sont difficiles à faire, comme simplifier les dépendances de données asynchrones des composants avec suspense et améliorer les performances de rendu avec le time slicing, qui garantit que React traite les rendus les plus importants de votre application en premier.

Une autre chose que React fait bien est d'avoir une grande expérience développeur et des outils pendant que vous développez et déboguez votre application via l'extension React Devtools, qui a récemment ajouté une fonctionnalité de profiler pour aider les développeurs à comprendre ce qui se passe dans l'application.

Certaines choses dans React n'étaient toujours pas idéales — la réutilisation de la logique entre plusieurs composants a traditionnellement été faite en utilisant des composants d'ordre supérieur et des props de rendu. Ils résolvent le problème mais cela présente un inconvénient pour les développeurs qui doivent restructurer le code. Cela pourrait conduire à un enfer de wrappers et rendre le flux de données dans l'application difficile à suivre.

Le deuxième problème est que dans les composants géants, la logique peut parfois être enchevêtrée et répartie sur diverses méthodes de cycle de vie, comme l'abonnement à un store dans `componentDidMount` et le désabonnement dans `componentWillUnmount`.

La séparation de la logique tend à conduire à des situations où vous oubliez de nettoyer après le montage, ce qui pourrait causer des fuites de mémoire. Le dernier problème est les classes. Les composants fonctionnels doivent souvent être convertis en classes pour utiliser l'état et les méthodes de cycle de vie, et du code boilerplate doit être ajouté pour les supporter. L'utilisation de `this` et la liaison des callbacks peuvent également être déroutantes.

L'équipe React a une proposition pour les trois problèmes ci-dessus — les Hooks React.

Dan Abramov a ensuite pris la parole ! React utilise un processus de demande de commentaires (RFC) chaque fois que quelqu'un veut apporter des ajouts ou des modifications substantielles à React, et une proposition doit être écrite, détaillant la motivation et la conception du changement. La proposition pour les Hooks React peut être trouvée [ici](https://github.com/reactjs/rfcs/pull/68). Il convient de noter que les Hooks ne contiennent aucune modification cassante ou dépréciation et que leur utilisation est facultative.

Dan a donné une démonstration de la manière de convertir un composant de classe typique avec état pour utiliser des composants fonctionnels en utilisant quelques nouvelles API de Hooks React — `useState`, `useEffect` et `useContext`, et les avantages sont évidents. Nous sommes capables de co-localiser la logique de cycle de vie dans un hook `useEffect` et pouvons les réutiliser dans plusieurs composants. Cela a déclenché un mouvement de la communauté créant des packages npm de hooks utiles, et ils peuvent être trouvés [ici](https://github.com/rehooks/awesome-react-hooks).

L'utilisation des Hooks comporte [quelques mises en garde](https://reactjs.org/docs/hooks-rules.html) — vous ne pouvez pas appeler de hooks dans des conditions, ils doivent être au niveau supérieur de votre composant fonctionnel, et il existe un plugin linter qui vous avertit si vous n'utilisez pas correctement les hooks.

C'est parce que React s'appuie sur l'ordre d'exécution des hooks pour faire correspondre les valeurs d'état avec les hooks. Vous ne pouvez utiliser les hooks que dans des composants fonctionnels ou d'autres hooks personnalisés (qui, par convention, doivent commencer par `use`).

Facebook utilise les hooks en production depuis environ quatre mois maintenant, donc le comportement est relativement stable. Les hooks peuvent coexister avec votre code existant et vous pouvez commencer à les utiliser aujourd'hui et migrer progressivement votre code non-hooks pour utiliser les hooks.

Ryan Florence, créateur de React Router, a ensuite donné une démonstration de la manière de refactoriser certains cas d'utilisation réels pour utiliser les hooks. Ryan a d'abord parlé de la manière dont les render props donnent aux composants un faux sentiment de hiérarchie dans des situations comme un composant `<Media>` qui est utilisé pour interroger les tailles d'écran réactives, puis a refactorisé un composant utilisant deux composants `<Media>` avec des render props en utilisant un hook useMedia qu'il a créé sur le moment.

La prochaine démonstration concernait la refactorisation/création d'un carrousel accessible avec toutes les fonctionnalités essentielles — un bouton lecture/arrêt, un bouton avant/arrière et une barre de progression.

Le hook `useEffect` a été introduit plus en détail ici et comment ils peuvent être exécutés uniquement lorsque certains états/props ont changé, des choses que vous feriez dans `componentDidUpdate`. `useEffect` peut être utilisé pour réaliser les mêmes choses que ce dont vous avez besoin pour `componentDidMount`, `componentDidUpdate` et `componentWillUnmount`.

Enfin, Ryan a également démontré comment vous pourriez adopter une approche de données unidirectionnelle de type Flux/Redux dans votre application en utilisant le hook `useReducer`. Le hook `useReducer` retourne deux variables, `state` et `dispatch`.

Comme dans Redux, la fonction de réduction que vous fournissez à `useReducer` prendra l'état actuel et une action comme paramètres et produira un nouvel état en fonction de l'action passée.

Je vous recommande de regarder sa vidéo de démonstration divertissante et éclairante. Le code de sa démonstration en direct peut également être trouvé dans son [dépôt GitHub](https://github.com/ryanflorence/react-conf-2018).

P.S. J'ai également appris que le changement des clés d'un composant réinitialise son état, car le changement des clés démonte et remonte un composant. Un conseil très pratique !

#### Liens vidéo

* [React Aujourd'hui et Demain — Sophie Alpert & Dan Abramov](https://www.youtube.com/watch?v=V-QO-KO90iQ&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)
* [90% de React plus propre en utilisant les Hooks — Ryan Florence](https://www.youtube.com/watch?v=wXLf18DsV-I&index=2&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)

#### Améliorer l'expérience utilisateur et le bonheur des développeurs avec le rendu concurrent dans React

Le deuxième jour de la conférence a été lancé par Andrew Clark et Brian Vaughn. Lors du développement, il n'est pas rare de dégrader l'expérience utilisateur dans le processus de rendre notre application plus rapide. Andrew donne un [exemple de Ads Manager](https://twitter.com/acdlite/status/991503599246098432) comme l'une de ces applications, en raison du nombre élevé de spinners dans le flux de création résultant du codesplitting des composants ou de la récupération de données. Ces spinners n'apparaissent également que pendant une fraction de seconde car les données ne mettent pas longtemps à se charger sur un réseau rapide.

Au cours de l'année écoulée, l'équipe React a travaillé sur React concurrent, qui vise à faciliter la création d'applications haute performance par défaut avec une expérience utilisateur fluide et sans saccades.

React concurrent (précédemment appelé Async React) permet à React de travailler sur plusieurs choses à la fois et de basculer entre elles selon leur priorité. Aujourd'hui, React fonctionne encore de manière synchrone. Si un composant nécessite beaucoup de temps pour se mettre à jour, le thread principal sera bloqué et le navigateur ne pourra pas répondre aux entrées utilisateur jusqu'à ce que le travail soit terminé. Avec React concurrent, ce travail peut être mis en pause, et le thread principal peut répondre à l'entrée utilisateur, puis reprendre le travail. Cela s'appelle également le time slicing, la capacité à diviser le travail en morceaux et à répartir son exécution dans le temps.

Andrew utilise ensuite une application composée de trois onglets comme exemple. Avec `React.lazy`, il est facile de diviser le code de l'application et de charger le composant dans chaque onglet uniquement lorsqu'il est rendu. React propose également un composant `<Suspense>` qui permet aux développeurs de rendre des solutions de repli lorsque le code du composant n'est pas encore chargé.

Ces composants peuvent être placés n'importe où dans l'arborescence des composants et si une partie de l'arborescence n'a pas été chargée, le repli du composant `<Suspense>` le plus proche sera utilisé. Les fonctionnalités ci-dessus fonctionnent en mode synchrone et ne nécessitent aucune fonctionnalité de React concurrent. Un problème mentionné précédemment est que si une ressource se charge rapidement, il y a un spinner clignotant inutile. Avec React concurrent, ces spinners clignotants inutiles peuvent être évités car vous pouvez configurer le seuil que vous êtes prêt à attendre avant d'afficher le spinner de repli.

Une dernière chose qu'Andrew a montrée est la facilité avec laquelle il était possible de pré-charger et de pré-rendre le contenu des autres onglets pendant le temps d'inactivité que l'utilisateur passe à lire le contenu du premier onglet après son chargement. Il suffit de passer une prop `hidden` à un élément HTML et React dépriorisera tous ses enfants à une priorité hors écran et ne les chargera que lorsqu'il n'y aura rien d'autre à faire sur la page. Lors de la navigation vers les autres onglets, ils apparaissent instantanément, car ils ont déjà été chargés pendant le temps d'inactivité.

Brian Vaughn a ensuite démontré un nouvel outil de profilage intégré dans React Devtool (il est déjà dans votre navigateur) et une nouvelle API de profilage. Le profil fonctionne de manière similaire au profil de performance de Chrome, vous enregistrez certaines interactions et pouvez voir la durée de rendu et les graphiques de flammes des composants qui ont été rendus.

Cela aide à déboguer les re-rendus inutiles et à détecter les composants avec des rendus lents. Les informations de performance peuvent également être attribuées à des événements dans le code en utilisant l'API de traçage du planificateur expérimental. Notez que cette API n'est pas encore finalisée, donc utilisez-la avec prudence. En savoir plus sur la nouvelle fonctionnalité de traçage des interactions de React [ici](http://fb.me/react-interaction-tracing).

Jared Palmer, ingénieur principal chez Palmer HQ, a donné une démonstration de la manière dont il a amélioré l'expérience utilisateur de son clone Spotify (aptement nommé Suspensify) en utilisant les nouvelles fonctionnalités de React concurrent. React cache peut non seulement être utilisé pour mettre en cache les données de réponse de l'API, il peut également être utilisé pour mettre en cache des actifs tels que des images, des fichiers audio et des scripts.

Jared a montré comment il a tiré parti de l'API `unstable_createResource` et `<Suspense />` pour afficher une image de profil d'artiste de remplacement en basse résolution comme espace réservé pendant que l'image en haute résolution est téléchargée en arrière-plan, puis afficher l'image en haute résolution après son téléchargement. Les données chargées en utilisant l'API `unstable_createResource` se lisent également plus facilement car les développeurs n'ont plus à gérer explicitement et à écrire du code pour les états de chargement. Suspense apporte les avantages de coordonner et de charger les états facilement.

Enfin, il convient de noter que le code utilisant `<Suspense />` fonctionne toujours sans React concurrent ; les gains d'expérience utilisateur sont moindres, mais les gains d'expérience développeur restent.

#### Liens vidéo

* [Rendu Concurrent dans React — Andrew Clark et Brian Vaughn](https://www.youtube.com/watch?v=ByBPyMBTzM0&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=15)
* [Passage à React Suspense — Jared Palmer](https://www.youtube.com/watch?v=SCQgE4mTnjU&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=16)

#### React Native a des problèmes mais une solution est en cours

React Native est le framework de Facebook pour construire des applications mobiles natives en utilisant JavaScript et React. James Long, créateur de Prettier, parle de ce qui ne va pas avec React Native, en particulier les animations. Selon son expérience, lors de l'écriture de code React Native lié à la réponse aux interactions utilisateur et aux animations, l'expérience utilisateur est horrible en raison des animations saccadées.

La raison est que les interactions utilisateur sont gérées sur le thread natif, mais les effets d'interaction sont traités par le thread JavaScript via un pont asynchrone. Une solution à ce problème est d'utiliser la bibliothèque [React Native Gesture Handler](https://kmagiera.github.io/react-native-gesture-handler/), qui fournit une API déclarative exposant le système natif de toucher et de gestes de la plateforme à React Native. Pour des interactions et animations encore plus complexes, `[react-native-reanimated](https://github.com/kmagiera/react-native-reanimated)` (par le même auteur de React Native Gesture Handler) pourrait être utilisé pour représenter la logique où les API déclaratives ne peuvent pas.

Dans le pire des cas, les développeurs pourraient aller encore plus bas niveau et écrire du code et des API en langage natif. En conclusion, bloquez le thread principal lors de la gestion des animations et évitez Async lorsque cela est possible. Les API déclaratives sont excellentes pour de nombreux cas d'utilisation, mais les API impératives seraient utiles comme une issue de secours pour les cas d'utilisation complexes.

Parashuram, un ingénieur Facebook de l'équipe React Native, passe en revue un aperçu de l'architecture actuelle de React Native et des problèmes avec React Native actuel, qui est une réitération du point de James sur les interactions dans React Native ne donnant pas de réponses rapides aux interactions utilisateur auxquelles les gens sont habitués dans les applications purement natives et sur le web en raison du pont asynchrone entre le thread natif et le thread JavaScript.

La solution de l'équipe React Native à ce problème est une nouvelle interface pour communiquer entre JavaScript et le natif, appelée JavaScript Interface (JSI). C'est essentiellement une manière simple pour JavaScript de communiquer avec Objective-C ou Java (ou tout autre langage natif).

Le côté JavaScript obtient l'accès à un objet hôte très similaire aux éléments HTML (sur React Web) et vous pouvez ensuite appeler des méthodes et accéder à des propriétés sur celui-ci.

Vous pouvez également utiliser JSI pour obtenir des modules natifs qui retournent un objet hôte et vous pouvez appeler des méthodes sur eux, similaires aux appels RPC. Un autre changement que j'attends avec impatience, c'est que React Native pourrait déplacer certains des gestionnaires de vue et des modules natifs en dehors de la bibliothèque principale vers la communauté, ce qui rend React Native plus léger et facilite sa mise à jour tant que vous ne dépendez pas des modules externes. Facebook utilise React Native en interne, ainsi que d'autres grandes entreprises comme Microsoft, Pinterest et Zynga.

Par conséquent, Facebook est engagé à améliorer React Native et à avancer avec la communauté.

#### Liens vidéo

* [Allez-y, bloquez le thread principal — James Long](https://www.youtube.com/watch?v=ZXqyaslyXUw&index=24&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)
* [La nouvelle architecture de React Native — Parashuram N](https://www.youtube.com/watch?v=UcqRXTriUVI&index=25&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)

#### Vous pouvez utiliser (les meilleures fonctionnalités de) GraphQL sans GraphQL

Conor Hastings, un ingénieur chez Netflix, a passé en revue les principes de conception de GraphQL et explique pourquoi GraphQL est attrayant pour les ingénieurs. Il a donné une bonne analogie de la manière dont le REST traditionnel est similaire à commander une pizza sans pouvoir choisir les garnitures et se retrouver avec 40 garnitures contre l'utilisation de GraphQL où vous pouvez choisir uniquement les garnitures que vous voulez — cela élimine le problème de sur-récupération de données. D'autres avantages de GraphQL incluent la récupération de données hiérarchiques avec un seul aller-retour et les excellents outils de développement de GraphQL (GraphiQL).

Tous les logiciels n'ont pas besoin de GraphQL.

Cela ne vaut probablement pas la peine de créer une API GraphQL complète si votre application n'a pas besoin d'être maintenue, vos utilisateurs ont une connexion internet haut débit. Cependant, vous pouvez toujours utiliser des parties de GraphQL dans votre application et tirer parti de certaines des bonnes parties de GraphQL — à savoir, le système de requête puissant qui facilite la mise en forme des données pour répondre aux besoins de votre UI.

Conor présente ensuite [RouteQL](https://github.com/conorhastings/routeql), une bibliothèque qu'il a construite et qui vise à utiliser des outils de graphql-js (le parseur GraphQL côté client) et d'autres bibliothèques populaires de l'écosystème GraphQL afin que vous puissiez écrire des requêtes GraphQL dans le navigateur qui communiquent avec n'importe quel backend. En faisant quelques sacrifices et en abandonnant certains des avantages de GraphQL, nous pouvons toujours tirer parti de la puissance de GraphQL sans utiliser GraphQL. GraphQL est un excellent choix pour les applications pilotées par les données du serveur sans beaucoup d'état client.

#### Liens vidéo

* [GraphQL sans GraphQL — Conor Hastings](https://www.youtube.com/watch?v=YSEUAi1dAdk&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=10)

#### React aide à rendre les interfaces utilisateur sophistiquées

Matt Perry explique comment l'animation est réalisée en utilisant des bibliothèques d'animation existantes de style impératif telles que [animated](https://github.com/animatedjs/animated) et [Popmotion](https://github.com/Popmotion/popmotion) et leurs lacunes. Nous pouvons simplifier les API impératives en API déclaratives en identifiant les motifs de la logique impérative que nous écrivons. En solution au problème mentionné, Matt présente sa bibliothèque d'animation [Pose](https://popmotion.io/pose/) qui utilise une approche déclarative de type CSS pour l'animation, ce qui rend l'écriture d'animations courantes vraiment simple.

Dans une autre conférence d'Elizabet Oliveira (ou Miuki Miu sur le web), elle parle de ce qu'est SVG, des avantages des SVG, des différentes manières dont nous pouvons les utiliser sur le web et dans React. Lorsque les illustrations SVG doivent être animées et personnalisables, les écrire en tant que composants composables avec des props est particulièrement bénéfique.

[React-kawaii](https://github.com/miukimiu/react-kawaii) est une bibliothèque d'illustrations mignonnes construite par Elizabet qui sont facilement personnalisables. Vous pouvez changer la taille, la couleur, l'humeur (contenu) d'illustrations SVG complexes simplement en changeant les props. Consultez la [démo](https://react-kawaii.now.sh/) sur son site web.

#### Liens vidéo

* [Le chemin vers un avenir animé de manière déclarative — Matt Perry](https://www.youtube.com/watch?v=1e07uPWpvzI&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=4)
* [Illustrations SVG en tant que composants React — Elizabet Oliveira](https://www.youtube.com/watch?v=1gG8rtm-rq4&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=17)

#### Nouveautés dans Create React App 2

Create React App (CRA) est un projet de démarrage qui facilite le démarrage de nouvelles applications React ou si vous souhaitez essayer React. Joe Haddad, un mainteneur de CRA, a présenté les nouveautés de CRA 2 : support de PostCSS, [Babel Macros](https://github.com/kentcdodds/babel-plugin-macros), Sass et modules CSS, support de TypeScript. Lire plus sur le [blog React](https://reactjs.org/blog/2018/10/01/create-react-app-v2.html).

#### Liens vidéo

* [Nouveautés dans Create React App — Joe Haddad](https://www.youtube.com/watch?v=He-m9gd6WyM&index=5&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ)

#### Le Web est idéal pour créer des interfaces utilisateur complexes

GDevelop est un éditeur de jeux construit il y a de nombreuses années par Florian Rival, ingénieur chez Facebook. Il a parlé de son parcours sur la manière dont il a modernisé l'éditeur (à l'origine écrit en C++) pour le web en tirant parti de React, Electron et WebAssembly. Florian a utilisé emscripten, qui a compilé son bytecode natif au format WebAssembly et a réécrit l'UI en React en tirant parti de l'écosystème vaste de bibliothèques de composants et d'outils de React. Florian a fortement optimisé les performances en utilisant la virtualisation, le nouveau profiler React et `shouldComponentUpdate`. Les éditeurs de jeux sont des applications extrêmement complexes et il est impressionnant que Florian ait pu porter son application native vers Electron en un an avec l'aide de React et des autres outils de l'écosystème open source.

#### Liens vidéo

* [React, JavaScript et WebAssembly pour porter des applications natives héritées — Florian Rival](https://www.youtube.com/watch?v=6La7jSCnYyk&list=PLPxbbTqCLbGE5AihOSExAa4wUM-P42EIJ&index=13)

#### Réflexions finales

Au début, j'ai trouvé étrange que les Hooks React retournent des valeurs dans des tableaux à déstructurer, mais je m'y suis progressivement habitué après les avoir utilisés au travail pendant plus d'un mois maintenant. En plus des avantages des hooks mentionnés ci-dessus, il y a un autre grand avantage : la taille de construction [diminue](https://twitter.com/sebmck/status/1055695821641924609) [encore](https://twitter.com/jamiebuilds/status/1056015484364087297) car beaucoup de méthodes de classe sont supprimées. Les variables d'état, parce qu'elles sont simplement des variables locales dans un composant, peuvent maintenant être minifiées également.

Les Hooks sont géniaux, mais ils ne viennent pas sans inconvénients.

* `useEffect` s'exécute à chaque rendu. Si nous définissons l'état dans les callbacks `useEffect`, nous pourrions causer des boucles infinies. Un exemple détaillant ce piège peut être trouvé dans cette [question Stack Overflow que j'ai écrite ici](https://stackoverflow.com/q/53243203/1751946). Il est recommandé que les développeurs lisent attentivement l'API `useEffect` et la comprennent bien avant de l'utiliser.
* Les fermetures (ou le code à l'intérieur) de `useEffect` et `useCallback` pourraient référencer des `state` et `props` obsolètes. J'ai également écrit sur ce piège dans [cette question Stack Overflow](https://stackoverflow.com/q/53024496/1751946). Si vous n'êtes pas sûr de référencer des valeurs anciennes, le hook de mise à jour de l'état dispose également d'une [forme de callback](https://reactjs.org/docs/hooks-reference.html#functional-updates) où vous pouvez accéder à la valeur d'état précédente.

D'autres inconvénients peuvent être trouvés dans la RFC [ici](https://github.com/reactjs/rfcs/blob/master/text/0068-react-hooks.md#drawbacks).

J'ai utilisé les hooks au travail et nous avons implémenté une petite abstraction de saisie de formulaire qui aide à valider et à suivre les états modifiés/sales d'un formulaire. Mon équipe aime cela jusqu'à présent !

Je n'ai pas encore eu l'occasion de jouer avec React concurrent, mais d'après les démonstrations, son utilisation dans le code de production semble si fluide et facile. Je crois que React concurrent, Suspense et les fonctionnalités de profiler sont très pertinents pour améliorer l'expérience utilisateur et le bonheur des développeurs.

J'ai hâte de voir plus de bonnes choses de React dans les prochaines versions de React ! 🚀

*Si vous avez aimé cet article, n'oubliez pas de laisser un 👏. (Saviez-vous que vous pouvez applaudir plus d'une fois ? Essayez et voyez par vous-même !)*

Vous pouvez également me suivre sur [GitHub](https://github.com/yangshun) et [Twitter](https://twitter.com/yangshunz).