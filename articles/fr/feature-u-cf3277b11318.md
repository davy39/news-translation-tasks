---
title: feature-u (Organisation de Projet Basée sur les Fonctionnalités pour React)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-12T06:38:54.000Z'
originalURL: https://freecodecamp.org/news/feature-u-cf3277b11318
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D9PDIbwiUfWLB8zd7xPawQ.jpeg
tags:
- name: features
  slug: features
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: Redux
  slug: redux
- name: 'tech '
  slug: tech
seo_title: feature-u (Organisation de Projet Basée sur les Fonctionnalités pour React)
seo_desc: 'By Kevin Bridges

  This article is an introduction to feature-u — a library that facilitates feature-based
  project organization in your react project. This utility assists in organizing your
  project by individual features.

  Most developers would agree t...'
---

Par Kevin Bridges

Cet article est une introduction à [feature-u](https://feature-u.js.org/) — une bibliothèque qui facilite l'**organisation de projet basée sur les fonctionnalités** dans votre projet [react](https://reactjs.org/). Cet utilitaire aide à organiser votre projet par fonctionnalités individuelles.

La plupart des développeurs s'accorderaient à dire que l'organisation de votre projet par fonctionnalités est beaucoup préférable aux modèles basés sur les types. Parce que les **domaines d'application grandissent** dans le monde réel, l'organisation par type ne s'adapte tout simplement pas, elle devient ingérable !

Il existe de nombreux bons articles sur ce sujet avec des informations sur la conception et la structure basées sur les fonctionnalités (voir : [Références](#15dd) ci-dessous).

Cet article décrit mon excursion dans la composition basée sur les fonctionnalités. En travaillant sur les détails, j'ai réalisé qu'il y avait une opportunité pour une bibliothèque d'aider à gérer et à rationaliser certains des obstacles rencontrés dans ce processus. Le résultat : **feature-u** (consultez la [documentation complète](https://feature-u.js.org/), le [code source GitHub](https://github.com/KevinAst/feature-u), et le [package NPM](https://www.npmjs.com/package/feature-u)).

> **_Mise à jour_**: Le 14/08/2018, [feature-u V1](https://feature-u.js.org/1.0.0/history.html#v1_0_0) a été publié, qui a repensé la communication inter-fonctionnalités pour inclure la [Composition UI](https://feature-u.js.org/1.0.0/crossCommunication.html#ui-composition) comme une offre centrale. **Un nouvel article peut être trouvé [ici](http://bit.ly/feature-u-V1)** qui prend une approche complète pour vous introduire à toutes les fonctionnalités de **feature-u** (y compris **V1**). Nous sommes très enthousiastes à propos de cette mise à jour, car elle **promouvoit une solution unique pour toutes les collaborations entre fonctionnalités** ! Bien que la mise à niveau vers V1 nécessite quelques modifications du code client (voir [Notes de Migration V1](https://feature-u.js.org/1.0.0/migration.1.0.0.html)), cela en vaut la peine. Cet article est basé sur [feature-u V0](https://feature-u.js.org/0.1.3/history.html#v0_1_3), et utilise certaines API obsolètes (principalement `Feature.publicFace`, et l'objet `app`). Néanmoins, c'est une bonne ressource pour vous familiariser avec feature-u.

#### **_En un coup d'œil_**

[Contexte](#e4bb) — pourquoi feature-u a été créé

[Bases de feature-u](#b996) — introduction aux concepts de haut niveau de feature-u

[Application eatery-nod](#077e) — l'application exemple utilisée pour démontrer feature-u

[Avant & Après](#688e) — structure du projet **eatery-nod** avant et après les fonctionnalités

[feature-u en Action](#ecd3) — exploration des aspects de feature-u à travers des exemples concrets

[Avantages de feature-u](#3ef6) — en résumé

[Références](#15dd) — articles sur les fonctionnalités

### [Contexte](#e80d)

Commençons par chroniquer mon parcours dans ce processus

#### **Au départ…**

_Donc… j'avais décidé de restructurer mon projet par fonctionnalités_. D'un point de vue conception, il y avait un certain nombre de considérations pour déterminer les limites des fonctionnalités. J'avais lu tous les articles, et appliqué ma conception à une **nouvelle structure de répertoire basée sur les fonctionnalités**.

En général, je me sentais bien dans ma progression. Je commençais à voir des avantages concrets… **la ségrégation des fonctionnalités allait entraîner un code beaucoup plus gérable !**

#### **Les obstacles…**

Cependant, il y avait encore un certain nombre d'obstacles à résoudre…

Comment puis-je encapsuler et isoler mes fonctionnalités, tout en permettant leur collaboration ?

Comment certaines fonctionnalités peuvent-elles introduire une initialisation au démarrage (même en injectant des utilitaires à la racine du DOM), sans dépendre d'un processus de démarrage externe ?

Comment puis-je promouvoir des composants UI basés sur les fonctionnalités de manière isolée et autonome ?

Comment puis-je configurer mes frameworks choisis maintenant que mon code est si dispersé ?

Comment puis-je activer/désactiver certaines fonctionnalités qui sont soit optionnelles, soit nécessitent une mise à niveau de licence ?

En résumé, comment puis-je tout rassembler pour que mes fonctionnalités individuelles fonctionnent comme une seule application ?

#### **L'objectif _(et maintenant ?)_**

L'**objectif principal** de feature-u est double :

1. Permettre aux fonctionnalités de **fonctionner en Plug-and-Play !** Cela englobe de nombreuses choses, telles que : l'encapsulation, la communication inter-fonctionnalités, l'activation, l'initialisation, et ainsi de suite. Nous allons développer ces concepts tout au long de cet article.
2. **Automatiser le démarrage de votre application !!** Vous avez les fonctionnalités. Permettez-leur de promouvoir leurs caractéristiques, afin qu'un utilitaire central puisse **automatiquement** configurer les frameworks utilisés dans votre application, lançant ainsi votre application. Cette tâche doit être accomplie de manière extensible, car tout le monde n'utilise pas le même ensemble de frameworks.

### [Bases de feature-u](#e80d)

Le processus de base de **feature-u** est que chaque fonctionnalité promeut un objet [Feature](https://feature-u.js.org/0.1.3/api.html#Feature) qui contient divers aspects de cette fonctionnalité — des choses comme le nom de la fonctionnalité, son API publique, si elle est activée, des constructions d'initialisation, et des ressources utilisées pour configurer sa partie des frameworks utilisés.

À leur tour, ces objets Feature sont fournis à [launchApp()](https://feature-u.js.org/0.1.3/api.html#launchApp), qui configure et démarre votre application. De plus, l'objet [App](https://feature-u.js.org/0.1.3/api.html#App) retourné est exporté, afin de promouvoir l'API publique de chaque fonctionnalité.

#### aspects

Dans feature-u, « aspect » est un terme généralisé utilisé pour désigner les divers ingrédients qui (lorsqu'ils sont combinés) constituent votre application.

Les aspects peuvent prendre de nombreuses formes différentes :

* Composants UI et Routes
* Gestion d'état (actions, reducers, sélecteurs)
* Logique métier
* Code d'initialisation au démarrage
* Et ainsi de suite…

Tous les aspects ne sont pas d'intérêt pour feature-u — seulement ceux qui sont nécessaires pour configurer et lancer l'application — tous les autres sont considérés comme un détail d'implémentation interne de la fonctionnalité.

Par exemple, considérons le gestionnaire d'état redux. Bien qu'il utilise des actions, des reducers et des sélecteurs… seuls les reducers sont nécessaires pour configurer et configurer redux.

#### intégration des frameworks

Un objectif fondamental de feature-u est de **configurer automatiquement le(s) framework(s)** utilisé(s) dans votre pile d'exécution (en accumulant les ressources nécessaires à travers toutes vos fonctionnalités). Parce que tout le monde n'utilise pas les mêmes frameworks, feature-u accomplit cela à travers des **Aspects Extensibles** (vous pouvez les trouver dans des packages NPM externes, ou vous pouvez créer les vôtres).

Il est important de comprendre que l'interface avec vos frameworks choisis n'est pas altérée de quelque manière que ce soit. Vous les utilisez de la même manière que vous l'avez toujours fait (juste dans la limite de votre fonctionnalité).

feature-u fournit simplement une couche organisationnelle bien définie, où les frameworks sont automatiquement configurés en accumulant les ressources nécessaires à travers toutes vos fonctionnalités.

### [Application eatery-nod](#e80d)

[**eatery-nod**](https://github.com/KevinAst/eatery-nod/tree/after-features) est l'application où feature-u a été conçu. Il s'agit d'une application mobile [react-native](https://facebook.github.io/react-native/) [expo](https://expo.io/), et c'est l'une de mes applications de test que j'utilise pour tester les frameworks. J'aime développer des applications que je peux utiliser, mais qui ont suffisamment de exigences réelles pour les rendre intéressantes.

eatery-nod sélectionne aléatoirement un restaurant pour une "soirée en amoureux" parmi une liste de favoris. Ma femme et moi avons une "soirée en amoureux" régulière, et nous sommes toujours indécis sur lequel de nos restaurants préférés fréquenter :-) Donc eatery-nod fournit la roue tournante !

Jetez un coup d'œil au [README](https://github.com/KevinAst/eatery-nod/blob/after-features/README.md) de eatery-nod pour vous faire une idée de l'application. Des flux d'écran sont disponibles, ce qui aide vraiment à vous orienter dans le projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DDrt1xRlOmM8jywM4ABSCg.png)
_**Flux d'écran principal de eatery-nod**_

De plus, des fichiers [README](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/README.md) se trouvent dans chaque fonctionnalité, décrivant ce que chaque fonctionnalité accomplit. Prenez un peu de temps maintenant et parcourez ces ressources :

* [**device**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md) — initialise l'appareil pour une utilisation par l'application, et promeut une abstraction de l'API de l'appareil
* [**auth**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/auth/README.md) — promeut une authentification complète de l'utilisateur
* [**leftNav**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/leftNav/README.md) — promeut le Drawer/SideBar spécifique à l'application sur le côté gauche de l'application
* [**currentView**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/currentView/README.md) — maintient la currentView avec des liaisons de communication inter-fonctionnalités get/set
* [**eateries**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/eateries/README.md) — gère et promeut la vue des restaurants
* [**discovery**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/discovery/README.md) — gère et promeut la vue de découverte
* [**firebase**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/firebase/README.md) — initialise le service Google Firebase
* [**logActions**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/logActions/README.md) — journalise toutes les actions dispatchées et l'état résultant
* [**sandbox**](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/sandbox/README.md) — promeut une variété de tests interactifs, utilisés en développement, qui peuvent être facilement désactivés

### [Avant & Après](#e80d)

Quiconque me connaît vous dira que j'ai une appréciation pour une bonne analyse avant/après. Qu'il s'agisse d'une rénovation de maison ou d'un refactoring de logiciel, cela aide à chroniquer d'où vous venez, afin de quantifier les réalisations concrètes, et vous donne un sentiment d'accomplissement.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dIpbZMgqHN5DrE6S.jpg)

Jetons un coup d'œil à la structure de répertoire de eatery-nod (avant/après).

À des fins d'illustration, je n'ai développé que quelques répertoires, mais je pense que vous voyez l'idée.

**Avant** : voici mon projet [avant les fonctionnalités](https://github.com/KevinAst/eatery-nod/tree/before-features/src)…

```
eatery-nod src AVANT les fonctionnalités
src/
├── actions/        ... actions redux
│     auth.js
│     discovery.js
│     eateries.js
│     ... snip snip
├── api/            ... diverses API abstraites
│     device.js
│     discovery.js
│     ... snip snip
├── app/            ... démarrage principal **1**
│  │  ScreenRouter.js
│  │  SideBar.js
│  │  index.js
│  └── startup/
│     │  createAppStore.js
│     │  platformSetup.android.js
│     │  platformSetup.ios.js
│     └── firebase/
│           firebaseAppConfig.js
│           initFireBase.js
├── appState/       ... reducers redux
│     auth.js
│     discovery.js
│     eateries.js
│     ... snip snip
├── comp/           ... Composants UI
│     DiscoveryListScreen.js
│     EateriesListScreen.js
│     ... snip snip
├── logic/          ... modules redux-logic
│     auth.js
│     discovery.js
│     eateries.js
│     ... snip snip
└── util/           ... utilitaires communs
```

**Après** : et voici le même projet [après les fonctionnalités](https://github.com/KevinAst/eatery-nod/tree/after-features/src)…

```
eatery-nod src APRÈS les fonctionnalités
src/
│  app.js          ... lance l'application via launchApp() **2**
├── feature/
│  │  index.js     ... accumule/promeut tous les objets Feature de l'application
│  ├── auth/        ... la fonctionnalité d'autorisation de l'application
│  │  │  actions.js
│  │  │  featureName.js
│  │  │  index.js
│  │  │  logic.js
│  │  │  publicFace.js
│  │  │  route.js
│  │  │  signInFormMeta.js
│  │  │  state.js
│  │  └── comp/
│  │        SignInScreen.js
│  │        SignInVerifyScreen.js
│  ├── currentView/ ... autres fonctionnalités
│  ├── device/      ... fonctionnalité pour initialiser l'appareil
│  │  │  actions.js
│  │  │  api.js
│  │  │  appDidStart.js
│  │  │  appWillStart.js
│  │  │  featureName.js
│  │  │  index.js
│  │  │  logic.js
│  │  │  publicFace.js
│  │  │  route.js
│  │  │  state.js
│  │  └── init/
│  │        platformSetup.android.js
│  │        platformSetup.ios.js
│  ├── discovery/   ... plus de fonctionnalités
│  ├── eateries/
│  ├── firebase/
│  ├── leftNav/
│  ├── logActions/
│  └── sandbox/
└── util/           ... utilitaires communs utilisés dans toutes les fonctionnalités
```

Comme prévu, la différence dans l'organisation du projet est dramatique !

* **Avant les fonctionnalités** — vous trouvez des constructions pour une fonctionnalité donnée réparties sur de nombreux répertoires typés.
* **Après les fonctionnalités** : tous les aspects d'une fonctionnalité donnée sont contenus dans son propre répertoire isolé.
* Une différence notable est la **réduction dramatique de la complexité du processus de démarrage de l'application !** Le « avant les fonctionnalités » contenait un répertoire entier `app\` de code de démarrage (voir `[**1**](#226c)` ci-dessus), tandis que le « après les fonctionnalités » contient simplement un seul fichier de démarrage `app.js` (voir `[**2**](#f98f)` ci-dessus). **Où est passée toute la complexité ?** ... restez à l'écoute !

### [feature-u en Action](#e80d)

Pour mieux comprendre feature-u, examinons de plus près quelques exemples de eatery-nod en action.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1OHVaxVpTBYvW_ZT.jpg)

Chacune des sections suivantes introduit brièvement un nouveau sujet de feature-u, en corrélant le code exemple de eatery-nod. Des informations supplémentaires sont fournies par des liens, à la fois vers la documentation de feature-u et le code source de eatery-nod. Dans certains cas, le code exemple en ligne a été rationalisé (pour mettre l'accent sur un point focal), cependant le lien de légende vous mènera au code réel (hébergé sur GitHub).

Voici nos sujets…

1. [Démarrage Simplifié de l'Application](#5974)
2. [Plateformes React](#af00)
3. [Objet Feature](#6db0)
4. [Initialisation des Fonctionnalités](#c1a5)
5. [Collaboration entre Fonctionnalités](#1895)
6. [Intégration des Frameworks](#cfeb)
7. [Activation des Fonctionnalités](#e557)
8. [Expansion de Code Gérée](#5fab)
9. [Promotion des Composants UI](#2666)
10. [Source Unique de Vérité](#c174)

### [1. Démarrage Simplifié de l'Application](#6561)

Après avoir divisé votre application en morceaux (comme avec les fonctionnalités), comment les rassembler et démarrer votre application ? À première vue, cela peut sembler une tâche ardue. Cependant, en raison de la structure promue par feature-u, c'est en réalité un processus très simple.

Pour résoudre cela, feature-u fournit la fonction `[launchApp()](https://feature-u.js.org/0.1.3/api.html#launchApp)` (voir : [Lancement de Votre Application](https://feature-u.js.org/0.1.3/detail.html#launching-your-application)).

Voici le mainline de eatery-nod…

La première chose à noter est la simplicité et la généricité du processus de démarrage du mainline. Il n'y a pas de code spécifique à l'application… pas même d'initialisation globale !

C'est parce que feature-u fournit divers hooks qui permettent à vos fonctionnalités d'injecter leurs propres constructions spécifiques à l'application.

Le mainline accumule simplement les Aspects et les Fonctionnalités, et démarre l'application en invoquant `launchApp()`.

Voici quelques points d'intérêt importants (faites correspondre les nombres à `*n*` dans le code ci-dessus) :

1. `([*1*](#a002))` les Aspects fournis (tirés de packages NPM séparés) reflètent les frameworks de notre pile d'exécution (dans notre exemple `[redux](http://redux.js.org/)`, `[redux-logic](https://github.com/jeffbski/redux-logic)`, et `[feature-router](https://github.com/KevinAst/feature-router)`) et étendent les propriétés Feature acceptables — `Feature.reducer`, `Feature.logic`, et `Feature.route` respectivement. (Voir [Aspects extensibles](https://feature-u.js.org/0.1.3/detail.html#extendable-aspects)).
2. `([*2*](#a002))` toutes les fonctionnalités de l'application sont accumulées à partir de notre répertoire `feature/`
3. `([*3*](#a002))` en préambule à la [Collaboration entre Fonctionnalités](#1895), la valeur de retour exportée de `launchApp()` est un objet `App`, qui promeut l'API Publique accumulée de toutes les fonctionnalités.

### [2. Plateformes React](#6561)

Dans l'exemple ci-dessus (voir `[*4*](#a002)`), vous voyez que `launchApp()` utilise un hook de rappel `[registerRootAppElm()](https://feature-u.js.org/0.1.3/api.html#registerRootAppElmCB)` pour enregistrer le `rootAppElm` fourni sur la plateforme React spécifique utilisée. Parce que cet enregistrement est accompli par le code spécifique à l'application, feature-u peut fonctionner sur n'importe quelle plateforme React (voir [Enregistrement React](https://feature-u.js.org/0.1.3/detail.html#react-registration)).

Voici quelques variations de `[registerRootAppElm()](https://feature-u.js.org/0.1.3/api.html#registerRootAppElmCB)` :

[react web](https://reactjs.org/) :

[react-native](https://facebook.github.io/react-native/) :

[expo](https://expo.io/) :

### [3. Objet Feature](#6561)

Chaque fonctionnalité est située dans son propre répertoire, et promeut le contenu des aspects à travers un objet `Feature` (en utilisant `[createFeature()](https://feature-u.js.org/0.1.3/api.html#createFeature)`).

Voici un exemple de la fonctionnalité [device](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md) de eatery-nod.

Comme vous pouvez le voir, l'objet `Feature` est simplement un conteneur qui contient le contenu des aspects d'intérêt pour feature-u. Le seul but de l'objet `Feature` est de communiquer ces informations d'aspect à `launchApp()`.

Nous remplirons plus de détails un peu plus tard, mais pour l'instant, notez que la fonctionnalité transmet des reducers, des modules de logique, des routes, et effectue un certain type d'initialisation (`appWillStart`/`appDidStart`). Elle promeut également un `publicFace` qui peut être utilisé par d'autres fonctionnalités (comme l'API Publique de la fonctionnalité).

Pour plus d'informations, veuillez vous référer à [Feature & aspect content](https://feature-u.js.org/0.1.3/detail.html#feature-object-relaying-aspect-content).

### [4. Initialisation des Fonctionnalités](#6561)

Une fonctionnalité donnée ne devrait pas avoir à dépendre d'un processus de démarrage externe pour effectuer l'initialisation dont elle a besoin. Plutôt, la fonctionnalité devrait pouvoir déclencher l'initialisation dont elle dépend.

Cela pourrait être n'importe quel nombre de choses, telles que :

* initialiser une API de service
* injecter un composant react utilitaire à la racine de l'application
* dispatcher une action qui lance un processus de démarrage
* Et plus...

Pour résoudre cela, feature-u introduit deux [Hooks de Cycle de Vie de l'Application](https://feature-u.js.org/0.1.3/appLifeCycle.html), injectés à travers les aspects de fonctionnalités suivants :

1. `[Feature.appWillStart({app, curRootAppElm}): rootAppElm || falsy](https://feature-u.js.org/0.1.3/appLifeCycle.html#appwillstart)` Invoqué une fois, juste avant que l'application ne démarre. Cela peut faire n'importe quel type d'initialisation, y compris compléter l'élément racine de haut niveau de l'application (comme l'instance de `composant` React).
2. `[Feature.appDidStart({app, appState, dispatch}): void](https://feature-u.js.org/0.1.3/appLifeCycle.html#appDidStart)`   
Invoqué une fois immédiatement après que l'application a démarré. Une utilisation typique de ce hook est de dispatcher un certain type d'`action de bootstrap`.

Voici quelques exemples de eatery-nod :

Initialisation de FireBase :

Action de Bootstrap :

Injection de l'élément racine du DOM :

### [5. Collaboration entre Fonctionnalités](#6561)

Même si l'implémentation d'une fonctionnalité est encapsulée, elle doit encore interagir avec son environnement. Pour compliquer les choses, une fonctionnalité ne devrait jamais importer de ressources d'une autre fonctionnalité, car elle devrait s'efforcer d'être plug-and-play. Par conséquent, nous avons besoin d'une API Publique bien définie basée sur les fonctionnalités.

Pour résoudre cela, feature-u promeut une [Communication Inter-Fonctionnalités](https://feature-u.js.org/0.1.3/crossCommunication.html). Cela est accompli à travers la propriété `Feature.publicFace` [Aspect Intégré](https://feature-u.js.org/0.1.3/detail.html#built-in-aspects). Une fonctionnalité peut exposer ce qu'elle juge nécessaire à travers son `publicFace`. Il n'y a pas de réelles contraintes sur cette ressource. Elle est vraiment ouverte.

Généralement, cela implique de promouvoir des éléments sélectionnés :

* actions
* sélecteurs
* APIs
* Et ainsi de suite

Le `publicFace` de toutes les fonctionnalités sont accumulés et exposés à travers l'objet `App` (émis par `launchApp()`).

Il contient des nœuds de fonctionnalités nommés, comme suit :

```
App.{featureName}.{publicFace}
```

Voici un exemple de la fonctionnalité [auth](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/auth/README.md) de eatery-nod.

Parmi tous les éléments trouvés dans la fonctionnalité `auth`, seules deux actions et un sélecteur sont publics.

Voici à quoi ressemblerait l'objet `App` pour cet exemple :

```
app: {  auth: {    actions: {      userProfileChanged(userProfile),      signOut(),    },    sel: {      getUserPool(appState),    },  },  currentView: {   // autres fonctionnalités    ... snip snip  },}
```

Par conséquent, l'API publique de la fonctionnalité `auth` peut être accessible comme suit :

```
app.auth.actions.userProfileChanged(userProfile)app.auth.actions.signOut()app.auth.sel.getUserPool(appState)
```

### [6. Intégration des Frameworks](#6561)

Très probablement, votre application emploie un ou plusieurs frameworks (comme `redux` ou `[redux-logic](https://github.com/jeffbski/redux-logic)`). Comment les ressources nécessaires à ces frameworks sont-elles accumulées et configurées à travers les nombreuses fonctionnalités de votre application ?

Pour résoudre cela, feature-u introduit des [Aspects Extensibles](https://feature-u.js.org/0.1.3/detail.html#extendable-aspects). **feature-u** est [extensible](https://feature-u.js.org/0.1.3/extending.html). Il fournit des points d'intégration entre vos fonctionnalités et vos frameworks choisis.

Les Aspects Extensibles sont emballés séparément de feature-u, afin de ne pas introduire de dépendances indésirables (car tout le monde n'utilise pas les mêmes frameworks). Vous les choisissez en fonction du ou des frameworks utilisés dans votre projet (correspondant à la pile d'exécution de votre projet). Ils sont créés avec l'API extensible de feature-u, en utilisant [createAspect()](https://feature-u.js.org/0.1.3/api.html#createAspect). Vous pouvez définir votre propre Aspect, si celui dont vous avez besoin n'existe pas déjà.

Jetons un coup d'œil à un exemple redux de eatery-nod.

La fonctionnalité `device` maintient sa propre partie de l'arbre d'état.

Elle promeut son reducer à travers l'aspect `Feature.reducer` :

Parce que `Feature.reducer` est un aspect étendu (par opposition à un aspect intégré), il est seulement disponible parce que nous avons enregistré l'aspect `reducerAspect` de [feature-redux](https://github.com/KevinAst/feature-redux) à `launchApp()` (veuillez vous référer à [Démarrage Simplifié de l'Application](#5974) ci-dessus).

La chose clé à comprendre est que feature-u (à travers l'extension feature-redux) configurera automatiquement redux en accumulant tous les reducers de fonctionnalités en un seul appState global.

Voici le code du reducer…

Un reducer basé sur les fonctionnalités est simplement un reducer normal qui gère la partie de l'appState global de la fonctionnalité. La seule différence est qu'il doit être embelli avec `[slicedReducer()](https://github.com/KevinAst/feature-redux#slicedreducer)`, qui fournit des instructions sur l'endroit où l'insérer dans l'appState global de haut niveau.

Par conséquent, le reducer `device` ne maintient que l'état pertinent pour la fonctionnalité `device` (comme sa petite partie du monde) — un statut, un indicateur fontsLoaded, et l'emplacement de l'appareil.

**Barre latérale** : Nous utilisons l'utilitaire [astx-redux-util](https://astx-redux-util.js.org/) `[reducerHash()](https://astx-redux-util.js.org/1.0.0/api.html#reducerHash)` pour implémenter de manière concise le reducer de la fonctionnalité (fournissant une alternative à l'instruction switch courante). J'ai trouvé qu'en utilisant un utilitaire comme celui-ci, dans la plupart des cas, il est faisable d'implémenter tous les reducers d'une fonctionnalité dans un seul fichier (en partie grâce à la frontière plus petite d'une fonctionnalité). astx-redux-util promeut également d'autres [Higher-Order Reducers](https://medium.com/@mange_vibration/reducer-composition-with-higher-order-reducers-35c3977ed08f). Vous pourriez vouloir vérifier cela.

### [7. Activation des Fonctionnalités](#6561)

Certaines de vos fonctionnalités peuvent avoir besoin d'être activées ou désactivées dynamiquement. Par exemple, certaines fonctionnalités peuvent n'être activées qu'avec une mise à niveau de licence, ou d'autres fonctionnalités peuvent n'être utilisées qu'à des fins de diagnostic.

Pour résoudre cela, feature-u introduit l'[Activation des Fonctionnalités](https://feature-u.js.org/0.1.3/enablement.html). En utilisant l'aspect intégré `Feature.enabled` (une propriété booléenne), vous pouvez activer ou désactiver votre fonctionnalité.

Voici un exemple de la fonctionnalité [sandbox](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/sandbox/README.md) de eatery-nod :

La fonctionnalité sandbox promeut une variété de tests interactifs, utilisés en développement, qui peuvent être facilement désactivés.

Généralement, cet indicateur est basé sur une expression dynamique, mais dans ce cas, il est simplement codé en dur (à définir par un développeur).

**Barre latérale** : Lorsque d'autres fonctionnalités interagissent avec une fonctionnalité qui peut être désactivée, vous pouvez utiliser l'objet `App` pour déterminer si une fonctionnalité est présente ou non (voir : [Activation des Fonctionnalités](https://feature-u.js.org/cur/enablement.html) pour plus d'informations).

### [8. Expansion de Code Gérée](#6561)

En général, l'accès aux **ressources importées** pendant l'expansion de code en ligne peut être problématique, en raison de l'ordre dans lequel ces ressources sont développées. L'objet `App` de feature-u est une ressource si critique (parce qu'il promeut l'API Publique de toutes les fonctionnalités), **il doit être disponible même pendant l'expansion de code**. En d'autres termes, nous ne pouvons pas compter sur un "app importé" étant résolu pendant le temps d'expansion de code.

Pour résoudre cela, feature-u introduit l'[Expansion de Code Gérée](https://feature-u.js.org/0.1.3/crossCommunication.html#managed-code-expansion).

Lorsque les définitions de contenu d'aspect nécessitent l'objet `App` au moment de l'expansion de code, vous enveloppez simplement la définition dans une fonction `[managedExpansion()](https://feature-u.js.org/0.1.3/api.html#managedExpansion)`. En d'autres termes, votre contenu d'aspect peut être soit le contenu réel lui-même (comme un reducer), soit une fonction qui retourne le contenu.

Lorsque cela est fait, feature-u l'étendra en l'invoquant de manière contrôlée, en passant l'objet `App` entièrement résolu comme paramètre.

Voici un module de logique de la fonctionnalité [auth](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/auth/README.md) de eatery-nod :

Vous pouvez voir que la fonctionnalité auth utilise une action de la fonctionnalité [device](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md), nécessitant l'accès à l'objet `app` (voir `[*2*](#8030)`). Parce que l'objet `app` est nécessaire pendant l'expansion de code, nous utilisons la fonction `managedExpansion()` (voir `[*1*](#8030)`), permettant à feature-u de l'étendre de manière contrôlée, en passant l'objet `app` entièrement résolu comme paramètre.

### [9. Promotion des Composants UI](#6561)

Les fonctionnalités qui maintiennent leurs propres composants UI ont besoin d'un moyen de les promouvoir dans l'interface utilisateur globale de l'application. Parce que les fonctionnalités sont encapsulées, comment cela est-il accompli de manière autonome ?

Pour répondre à cela, feature-u recommande de considérer les [Routes Basées sur les Fonctionnalités](https://feature-u.js.org/0.1.3/featureRouter.html) via l'Aspect Extensible [feature-router](https://github.com/KevinAst/feature-router) (emballé séparément). Cette approche peut même être utilisée en conjonction avec d'autres solutions de navigation.

Les Routes de Fonctionnalités sont basées sur un concept très simple : permettre à l'état de l'application de piloter les routes ! Il fonctionne à travers une série de fonctions de routage basées sur les fonctionnalités qui raisonnent sur l'appState, et retournent soit un composant rendu, soit null pour permettre aux routes en aval la même opportunité.

Voici un exemple simple de la fonctionnalité [device](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/device/README.md).

Cette route analyse l'appState actuel, et affiche un SplashScreen jusqu'à ce que le système soit prêt :

Dans le routage basé sur les fonctionnalités, vous ne trouverez pas le catalogue de mappage typique "chemin de route vers composant", où (par exemple) une directive pseudo `route('device')` provoque l'affichage de l'écran Device, ce qui à son tour provoque l'adaptation du système à la demande en ajustant son état de manière appropriée.

Plutôt, l'appState est analysé, et si l'appareil n'est PAS prêt, aucun autre écran n'a la possibilité de se rendre... Facile !

Selon votre perspective, cette approche peut être plus naturelle, mais plus important encore, elle permet aux fonctionnalités de promouvoir leurs propres écrans de manière encapsulée et autonome.

### [10. Source Unique de Vérité](#6561)

Les implémentations de fonctionnalités (comme toutes les constructions de codage) devraient s'efforcer de suivre le principe de **source unique de vérité**. En faisant cela, une modification en une seule ligne peut se propager à de nombreuses zones de votre implémentation.

Quelles sont les **Meilleures Pratiques** pour la source unique de vérité en ce qui concerne les fonctionnalités, et comment feature-u peut-il aider ?

La section [Meilleures Pratiques](https://feature-u.js.org/0.1.3/bestPractices.html) met en lumière un certain nombre d'éléments de source unique de vérité basés sur les fonctionnalités d'intérêt. Ce sont des directives, car vous devez les implémenter dans votre code d'application (feature-u n'est pas en contrôle de cela).

Voici un exemple de la fonctionnalité [eateries](https://github.com/KevinAst/eatery-nod/blob/after-features/src/feature/eateries/README.md) :

Le `featureName` est utilisé pour spécifier l'emplacement de l'état de haut niveau de cette fonctionnalité (voir `[*1*](#d59b)`). feature-u garantit que le nom de la fonctionnalité est unique. Par conséquent, il peut être utilisé pour qualifier l'identité de plusieurs aspects de la fonctionnalité.

Par exemple :

* préfixer les types d'action avec featureName, garantissant leur unicité dans toute l'application (voir : [feature-redux](https://github.com/KevinAst/feature-redux#action-uniqueness-single-source-of-truth) docs)
* préfixer les noms des modules de logique avec featureName, identifiant où ce module réside (voir : [feature-redux-logic](https://github.com/KevinAst/feature-redux-logic#single-source-of-truth) docs)
* selon le contexte, le featureName peut être utilisé comme la racine de la forme de l'état de votre fonctionnalité (voir : [feature-redux](https://github.com/KevinAst/feature-redux#state-root-single-source-of-truth) docs)

Parce que feature-u repose sur `[slicedReducer()](https://github.com/KevinAst/feature-redux#slicedreducer)` (dans le package feature-redux), une meilleure pratique est d'utiliser le sélecteur embelli du reducer pour qualifier la racine de l'état de votre fonctionnalité dans toutes vos définitions de sélecteur. Par conséquent, la définition de la tranche est maintenue en un seul endroit (voir `[*2*](#d59b)`).

### [Avantages de feature-u](#e80d)

En résumé, les avantages de l'utilisation de feature-u incluent :

* **Encapsulation des Fonctionnalités** — isoler les implémentations des fonctionnalités améliore la gestion du code
* **Communication Inter-Fonctionnalités** — l'API publique d'une fonctionnalité est promue à travers une norme bien définie
* **Activation des Fonctionnalités** — activer/désactiver les fonctionnalités à travers un commutateur d'exécution
* **Hooks de Cycle de Vie de l'Application** — les fonctionnalités peuvent s'initialiser sans dépendre d'un processus externe
* **Source Unique de Vérité** — est facilitée de plusieurs manières au sein de l'implémentation d'une fonctionnalité
* **Intégration des Frameworks** — configurer le(s) framework(s) de votre choix (correspondant à votre pile d'exécution) en utilisant l'API extensible de feature-u
* **Promotion des Composants UI** — à travers les Routes de Fonctionnalités
* **Minimiser les Problèmes de Dépendance d'Ordre des Fonctionnalités** — même dans le code qui est développé en ligne
* **Plug-and-Play** — les fonctionnalités peuvent être ajoutées/supprimées facilement
* **Mainline Simplifié** — `launchApp()` démarre l'application en configurant les frameworks utilisés, tout cela piloté par un ensemble simple de fonctionnalités.
* **Fonctionne sur n'importe quelle Plateforme React** (y compris React Web, React Native et Expo)

Espérons que cet article vous donne une idée de la manière dont feature-u peut améliorer votre projet. Veuillez vous référer à la [documentation complète](https://feature-u.js.org/) pour plus de détails.

feature-u vous permet de concentrer votre attention sur l'« extrémité métier » de vos fonctionnalités ! Allez de l'avant et calculez !!

### [Références](#e80d)

* [Une approche basée sur les fonctionnalités pour le développement React](http://ryanlanciaux.com/blog/2017/08/20/a-feature-based-approach-to-react-development/) … Ryan Lanciaux
* [Comment mieux organiser vos applications React ?](https://medium.com/@alexmngn/how-to-better-organize-your-react-applications-2fd3ea1920f1) … Alexis Mangin
* [Comment utiliser Redux sur des applications javascript hautement évolutives ?](https://medium.com/@alexmngn/how-to-use-redux-on-highly-scalable-javascript-applications-4e4b8cb5ef38) … Alexis Mangin
* [La manière 100% correcte de structurer une application React (ou pourquoi il n'y a pas de telle chose)](https://hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed) … David Gilbertson
* [Redux pour la gestion d'état dans les grandes applications web](https://blog.mapbox.com/redux-for-state-management-in-large-web-apps-c7f3fab3ce9b) … David Clark