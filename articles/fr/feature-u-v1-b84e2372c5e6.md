---
title: Libérez le pouvoir du développement JavaScript basé sur les fonctionnalités
  — avec feature-u V1
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-22T00:31:55.000Z'
originalURL: https://freecodecamp.org/news/feature-u-v1-b84e2372c5e6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*79altp9cNA9V31OonG_pSA.jpeg
tags:
- name: features
  slug: features
- name: JavaScript
  slug: javascript
- name: Libraries
  slug: libraries
- name: React
  slug: react
- name: Utilities
  slug: utilities
seo_title: Libérez le pouvoir du développement JavaScript basé sur les fonctionnalités
  — avec feature-u V1
seo_desc: 'By Kevin Bridges

  This article is an introduction to a new JS library called feature-u, that facilitates
  feature-based development in your React project.


  Note_: On 8/14/2018 feature-u V1 was released, that re-designed Cross Feature Communication
  to i...'
---

Par Kevin Bridges

Cet article est une introduction à une nouvelle bibliothèque JS appelée [feature-u](https://feature-u.js.org/), qui _facilite le développement basé sur les fonctionnalités dans votre projet [React](https://reactjs.org/)_.

> **_Note_**_: Le 14/08/2018, [**feature-u V1**](https://feature-u.js.org/1.0.0/history.html#v1_0_0) a été publié, redessinant la [Communication Inter-Fonctionnalités](https://feature-u.js.org/1.0.1/crossCommunication.html) pour inclure la [Composition UI](https://feature-u.js.org/1.0.1/crossCommunication.html#ui-composition) comme une offre centrale. Cet article couvre la version V1. Le premier article, basé sur [feature-u V0](https://feature-u.js.org/0.1.3/history.html#v0_1_3), peut être trouvé [ici](http://bit.ly/feature-u). Nous sommes très enthousiastes à propos de cette mise à jour car elle **promouvoit une solution unique pour toutes les collaborations entre fonctionnalités**!_

La plupart des développeurs s'accorderaient à dire que l'organisation de votre projet par fonctionnalité est bien préférable aux modèles basés sur les types. Parce que **les domaines d'application grandissent** dans le monde réel, l'organisation par type **ne s'adapte tout simplement pas**, _elle devient tout simplement ingérable_!

Il existe un certain nombre de bons articles qui discutent de ce sujet avec des informations sur la conception et la structure basées sur les fonctionnalités (voir : [Références](#8e25) ci-dessous). Cependant, en ce qui concerne la mise en œuvre, vous êtes plus ou moins livré à vous-même.

[**feature-u**](https://feature-u.js.org/) est une bibliothèque utilitaire qui gère et rationalise ce processus. Elle automatise les détails fastidieux de la gestion des fonctionnalités et aide à promouvoir des fonctionnalités qui sont vraiment **plug-and-play**.

Cet article fournit une base des concepts et de la terminologie de [**feature-u**](https://feature-u.js.org/), en développant des informations sur la manière dont vous pouvez promouvoir des fonctionnalités individuelles **plug-and-play** dans votre projet. Il explique pourquoi **feature-u** a été développé et vous donne une meilleure compréhension de ses avantages.

Consultez la [documentation complète](https://feature-u.js.org/), le [code source](https://github.com/KevinAst/feature-u) et le [package npm](https://www.npmjs.com/package/feature-u).

[**feature-u**](https://feature-u.js.org/) ouvre de nouvelles portes vers le monde passionnant du développement basé sur les fonctionnalités. Il vous libère pour **concentrer votre attention sur l'aspect "business" de vos fonctionnalités**!

### En un coup d'œil

Pour votre commodité, cette **Table des Matières** (TOC) contient des liens directs vers **chaque section. Notez également que chaque titre de section contient un lien vers la TOC**.

```
Développement Basé sur les Fonctionnalités  Séparation des Fonctionnalités  Objectifs des Fonctionnalités    Consolidation des Fonctionnalités à l'Exécution    Collaboration entre FonctionnalitésLa Solution feature-u  launchApp()  Objet Feature  aspects  Exécution de l'Application    Initialisation de l'Application    Configuration du Framework    Lancement de Votre Application  Communication Inter-Fonctionnalités  Composition UI Basée sur les Fonctionnalités    Contrats de Ressources  Activation des FonctionnalitésEn RésuméAvantagesRéférences
```

> _Veuillez **m'aider à faire connaître** **feature-u**. Vos applaudissements déterminent la distribution/promotion de cet article. Si vous pensez que **feature-u** a du potentiel, veuillez applaudir plusieurs fois cet article :-)_

### [Développement Basé sur les Fonctionnalités](#e98c)

À une vue d'ensemble, le développement basé sur les fonctionnalités (comme dans la plupart des logiciels) consiste à diviser les problèmes complexes en morceaux plus petits. Même lorsque j'ai commencé ma carrière _(dans les années 70)_, c'était une citation proéminente :

> "Tous les problèmes en informatique peuvent être résolus par un autre niveau d'indirection." **David Wheeler**

En divisant votre application en fonctionnalités, chaque fonctionnalité peut se concentrer sur un ensemble de tâches plus spécifique et isolé. **Dans une certaine mesure, vous pouvez penser à une fonctionnalité comme une "mini-application"**!

![Image](https://cdn-media-1.freecodecamp.org/images/1*50bxcswJEzugLESSDiFW7w.jpeg)

Il existe de nombreuses considérations de conception dans la définition des limites de vos fonctionnalités. Vous pouvez trouver plusieurs articles sur ce sujet qui fournissent des informations sur la conception basée sur les fonctionnalités.

Pour la plupart, ces considérations font partie de la conception de chaque projet individuel. Bien que **feature-u** ne dicte pas les considérations de conception globales, il facilite les bons principes basés sur les fonctionnalités (comme l'encapsulation). _Cela sera le focus de cet article_.

### [Séparation des Fonctionnalités](#e98c)

Si vous êtes comme moi, lorsque vous pensez au développement basé sur les fonctionnalités, la première chose qui vient à l'esprit est d'isoler votre code dans des répertoires de fonctionnalités.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8GHt18xe1e1tG9VQOXTMRQ.png)

En faisant cela, votre code est organisé par ce qu'il accomplit (c'est-à-dire des fonctionnalités), plutôt que par ce qu'il est (c'est-à-dire des composants, des routes, de la logique, des actions, des réducteurs, des sélecteurs, etc.).

En séparant vos fonctionnalités dans des répertoires individuels, il y a une apparence d'isolement.

### [Objectifs des Fonctionnalités](#e98c)

Notre objectif est d'**encapsuler chaque fonctionnalité** de manière à les rendre vraiment **plug-and-play**. _Mais comment cela est-il accompli_?

La structure des répertoires n'est qu'un début. Il y a **plusieurs obstacles** qui doivent être surmontés pour réaliser notre objectif...

* Comment encapsuler et isoler nos fonctionnalités, tout en permettant qu'elles collaborent entre elles ?
* Comment certaines fonctionnalités peuvent-elles introduire une initialisation au démarrage (même en injectant des utilitaires au niveau du DOM racine), sans dépendre d'un processus de démarrage externe ?
* Comment la composition UI basée sur les fonctionnalités peut-elle être accomplie de manière isolée et autonome ?
* Comment configurer nos frameworks choisis maintenant que notre code est si dispersé ?
* Comment activer/désactiver certaines fonctionnalités qui sont soit optionnelles, soit nécessitent une mise à niveau de licence ?

**En bref**, comment obtenir une application fonctionnelle à partir de ces fonctionnalités isolées ?

En résumé, il y a **deux caractéristiques principales** qui doivent être accomplies pour atteindre nos objectifs :

1. `[**Consolidation des Fonctionnalités à l'Exécution**](#c8d1)` : _regrouper nos fonctionnalités en une seule application fonctionnelle_
2. `[**Collaboration entre Fonctionnalités**](#abbc)` : _fournir un mécanisme par lequel nos fonctionnalités peuvent interagir entre elles_

Il s'avère que _tout le reste est un sous-produit de ces deux artefacts_. Examinons de plus près chacun de ces éléments.

### [Consolidation des Fonctionnalités à l'Exécution](#e98c)

Maintenant que nous avons isolé nos fonctionnalités en entités séparées, comment les regrouper pour qu'elles fonctionnent comme **une seule application** ? Nous devons pouvoir extraire et configurer divers aspects de nos fonctionnalités individuelles, et les "lancer" comme une seule application homogène en cours d'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/0*k1La5g-6jXlOCIP-.png)

Cette préoccupation peut être divisée en deux sous-préoccupations :

* `[Initialisation de l'Application](#d44a)`  
Certaines fonctionnalités peuvent nécessiter une initialisation spécifique au démarrage. Par exemple, une fonctionnalité qui encapsule une certaine abstraction de base de données reposera sur une configuration d'exécution d'un service de base de données.  
Certes, nous ne voulons pas dépendre d'une logique d'application globale pour accomplir cela _(une fois de plus, nous voulons que nos fonctionnalités soient encapsulées et autonomes)_.
* `[Configuration du Framework](#c339)`  
Si votre application repose sur d'autres frameworks, il est probable qu'il y ait des ressources contenues dans chaque fonctionnalité qui doivent être accumulées et alimentées dans le processus de configuration du framework.  
Comment cela est-il accompli ?

### [Collaboration entre Fonctionnalités](#e98c)

La deuxième caractéristique (mentionnée ci-dessus) est la **Collaboration entre Fonctionnalités** — _fournir un mécanisme par lequel nos fonctionnalités peuvent interagir entre elles_.

Une **bonne pratique** du développement basé sur les fonctionnalités _(dans la mesure du possible)_ est de **traiter chaque fonctionnalité comme une implémentation isolée**. La plupart des aspects d'une fonctionnalité sont internes à l'implémentation de cette fonctionnalité _(par exemple, les actions sont généralement créées et consommées exclusivement par la logique/les réducteurs/les composants qui sont internes à cette fonctionnalité)_.

De cette perspective, vous pouvez penser à chaque fonctionnalité comme à sa **propre mini-application isolée**.

Cela dit, cependant, nous savons que _"**aucun homme n'est une île**"_! Toute fonctionnalité donnée existe finalement comme partie d'une application plus large. Il existe des cas où une fonctionnalité doit promouvoir un sous-ensemble limité de ses aspects à d'autres fonctionnalités. Par exemple, une fonctionnalité peut avoir besoin de :

* être informée d'un état externe (via un sélecteur)
* émettre ou surveiller les actions d'autres fonctionnalités
* consolider les ressources de composants d'autres fonctionnalités — comme dans la **Composition UI**
* invoquer l'API d'autres fonctionnalités
* etc. etc. etc.

Ces éléments forment la base de pourquoi la `[**Communication Inter-Fonctionnalités**](#5369)` et la `[**Composition UI Basée sur les Fonctionnalités**](#a480)` sont nécessaires.

![Image](https://cdn-media-1.freecodecamp.org/images/0*S6DWAwYUVlWsTR5Q.png)

Pour compliquer les choses, en règle générale, **les imports JS ne doivent pas traverser les limites des fonctionnalités**. La raison en est que cette communication inter-fonctionnalités doit être **limitée aux points d'accès publics** — aidant à **faciliter le vrai plug-and-play**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*rUqXNI_dmUnyaPQn.png)

Étant donné tout cela, **comment la Communication Inter-Fonctionnalités est-elle réalisée** _de manière à ne pas rompre l'encapsulation_?

Les fonctionnalités ont besoin d'un moyen de promouvoir leur **Interface Publique** auprès d'autres fonctionnalités, et de consommer les **Actifs Publics** d'autres fonctionnalités.

### [La Solution feature-u](#e98c)

Examinons la solution que **feature-u** fournit pour tous ces objectifs. Les sections suivantes construiront les concepts de **feature-u** de manière incrémentielle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GBSlbLZegIq6vN-6tPY02A.jpeg)

### [launchApp()](#e98c)

`[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` est un utilitaire essentiel dans **feature-u**. C'est un agent, travaillant en votre nom, qui fournit la fondation qui **accomplit tous les objectifs** de **feature-u**! Il facilite à la fois la `[**Consolidation des Fonctionnalités à l'Exécution**](#c8d1)` et la `[**Collaboration entre Fonctionnalités**](#abbc)`.

Avec cet utilitaire, **votre processus de démarrage principal est extrêmement simple**... il invoque simplement `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`, et c'est tout!

![Image](https://cdn-media-1.freecodecamp.org/images/0*73_25clr2UP2Vbqb.png)

La fonction `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` démarre réellement votre application, employant divers hooks qui pilotent à la fois l'**Initialisation de l'Application** et la **Configuration du Framework**!

Vous pouvez trouver des exemples de `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` dans la section `[Usage](https://feature-u.js.org/1.0.1/usage.html#launchapp)`, et `[Lancement de Votre Application](https://feature-u.js.org/1.0.1/detail.html#launching-your-application)`.

**Comment cela fonctionne-t-il ? Quels sont les liens avec `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`**? ... _approfondissons un peu plus_...

### [Objet Feature](#e98c)

Pour accomplir cela, chaque fonctionnalité promeut un objet `[Feature](https://feature-u.js.org/1.0.1/api.html#Feature)` _(en utilisant `[createFeature()](https://feature-u.js.org/1.0.1/api.html#createFeature)`)_, qui catalogue les aspects d'intérêt pour **feature-u**.

C'est l'entrée principale de `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5vyM9ekRX_AYaaXw.png)

### [aspects](#e98c)

Dans **feature-u**, "aspect" _(petit "a")_ est un terme généralisé utilisé pour désigner les divers ingrédients qui (lorsqu'ils sont combinés) constituent votre application. Les aspects peuvent prendre de nombreuses formes différentes : **Composants UI** • **Routes** • **Gestion d'État**_(actions, réducteurs, sélecteurs)_ • **Logique Métier** • **Code d'Initialisation de Démarrage** • _etc. etc. etc._

**Tous les aspects ne sont pas d'intérêt pour feature-u**... _seuls ceux qui sont nécessaires pour configurer et lancer l'application_... tous les autres sont considérés comme un détail d'implémentation interne de la fonctionnalité. Par exemple, considérons le gestionnaire d'état Redux : bien qu'il utilise des actions, des réducteurs et des sélecteurs... seuls les réducteurs sont nécessaires pour configurer et configurer Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/0*fCOFHW2dFyYYSrd-.png)

L'objet `[Feature](https://feature-u.js.org/1.0.1/api.html#Feature)` est simplement un conteneur léger qui contient les aspects d'intérêt pour **feature-u**. Ces aspects peuvent être soit des `[Aspects Intégrés](https://feature-u.js.org/1.0.1/detail.html#built-in-aspects)` _(provenant du noyau **feature-u**)_, soit des `[Aspects Extensibles](https://feature-u.js.org/1.0.1/detail.html#extendable-aspects)` _(provenant d'extensions de plugins)_.

### [Exécution de l'Application](#e98c)

Voyons comment `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` accommode les deux sous-objectifs de l'exécution de l'application :

* `[Initialisation de l'Application](#d44a)`
* `[Configuration du Framework](#c339)`

### [Initialisation de l'Application](#e98c)

Parce que `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` contrôle le démarrage de l'application, il peut introduire des `[Hooks de Cycle de Vie de l'Application](https://feature-u.js.org/1.0.1/appLifeCycle.html)`.

Cela permet à chaque fonctionnalité d'effectuer une initialisation spécifique à l'application, et même d'injecter des composants dans la racine de l'application.

Il y a deux hooks :

1. `[Feature.appWillStart()](https://feature-u.js.org/1.0.1/appLifeCycle.html#appwillstart)` - invoqué une fois au démarrage de l'application
2. `[Feature.appDidStart()](https://feature-u.js.org/1.0.1/appLifeCycle.html#appdidstart)` - invoqué une fois immédiatement après le démarrage de l'application

![Image](https://cdn-media-1.freecodecamp.org/images/0*9EzmrTLQ-pglIoek.png)

Les `[Hooks de Cycle de Vie de l'Application](https://feature-u.js.org/1.0.1/appLifeCycle.html)` **simplifient grandement le processus de démarrage principal de votre application**, car _l'initialisation spécifique à une fonctionnalité donnée peut être encapsulée dans cette fonctionnalité_.

### [Configuration du Framework](#e98c)

Un objectif fondamental de **feature-u** est de **configurer automatiquement le(s) framework(s)** utilisé(s) dans votre pile d'exécution _(en accumulant les ressources nécessaires à travers toutes vos fonctionnalités)_. Cela réduit considérablement le code standard dans votre application.

Comment cela peut-il être accompli alors qu'il existe tant de frameworks... et que chaque projet utilise un mélange différent ?

**feature-u** est extensible ! Il fonctionne dans une architecture ouverte et plugable où les **Aspects Extensibles** intègrent **feature-u** à d'autres frameworks, correspondant à votre pile d'exécution spécifique. **C'est bien**, _car tout le monde n'utilise pas les mêmes frameworks_!

Les **Aspects Extensibles** peuvent être trouvés dans des packages NPM externes _(le cas normal)_, ou vous pouvez créer les vôtres en utilisant `[createAspect()](https://feature-u.js.org/1.0.1/api.html#createAspect)` _(un sujet plus avancé)_.

![Image](https://cdn-media-1.freecodecamp.org/images/0*be_uSLWT5KxyCiTD.png)

L'objet `[Aspect](https://feature-u.js.org/1.0.1/api.html#Aspect)` contient une série de `[Hooks de Cycle de Vie de l'Aspect](https://feature-u.js.org/1.0.1/extending.html#aspect-life-cycle-methods)` qui sont invoqués sous le contrôle de **feature-u** (`[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`). En général, la responsabilité d'un Aspect est de :

* accumuler le `[AspectContent](https://feature-u.js.org/1.0.1/api.html#AspectContent)` à travers toutes les fonctionnalités
* effectuer une configuration et une installation souhaitées
* exposer sa fonctionnalité de quelque manière (typiquement une intégration de framework)

Un `[Aspect](https://feature-u.js.org/1.0.1/api.html#Aspect)` étend automatiquement l'objet `[Feature](https://feature-u.js.org/1.0.1/api.html#Feature)` en permettant à son `[AspectContent](https://feature-u.js.org/1.0.1/api.html#AspectContent)` d'être **"catalogué"** dans le `Feature` en utilisant `Aspect.name` comme clé. Dans le diagramme ci-dessus, vous pouvez voir que

* l'`reducerAspect` (`Aspect.name: 'reducer'`) permet une construction `Feature.reducer: reducerContent`
* et le `logicAspect` (`Aspect.name: 'logic'`) permet une construction `Feature.logic: logicContent`

Il est important de comprendre que l'interface avec vos frameworks choisis n'est pas altérée de quelque manière que ce soit. Vous les utilisez de la même manière que vous l'avez toujours fait _(juste dans la limite de votre fonctionnalité)_. **feature-u** fournit simplement une couche organisationnelle bien définie, où les frameworks sont automatiquement configurés et configurés en accumulant les ressources nécessaires à travers toutes vos fonctionnalités.

### [Lancement de Votre Application](#e98c)

Dans **feature-u**, le mainline de l'application est très simple et générique. Il n'y a pas de vrai code spécifique à l'application dedans... **pas même d'initialisation globale**! C'est parce que **chaque fonctionnalité peut injecter ses propres constructions spécifiques à l'application**!! Le mainline accumule simplement les `[Aspects](https://feature-u.js.org/1.0.1/api.html#Aspect)` et les `[Features](https://feature-u.js.org/1.0.1/api.html#Feature)`, et démarre l'application en invoquant `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`:

Voici quelques **points d'intérêt importants** _(faites correspondre les nombres à `*n*` dans le code ci-dessus)_:

1. les `[Aspects](https://feature-u.js.org/1.0.1/api.html#Aspect)` fournis _(tirés de packages npm séparés)_ reflètent les frameworks de notre pile d'exécution _(dans notre exemple `[redux](http://redux.js.org/)`, `[redux-logic](https://github.com/jeffbski/redux-logic)`, et `[feature-router](https://github.com/KevinAst/feature-router)`)_ et étendent les propriétés Feature acceptables _(`Feature.reducer`, `Feature.logic`, et `Feature.route` respectivement)_... **_voir:_** `[Aspects Extensibles](https://feature-u.js.org/1.0.1/detail.html#extendable-aspects)`
2. toutes les fonctionnalités de notre application sont fournies (accumulées à partir du répertoire `features/`)
3. un callback `[registerRootAppElm()](https://feature-u.js.org/1.0.1/api.html#registerRootAppElmCB)` est utilisé pour cataloguer l'`rootAppElm` fourni à la plateforme React spécifique utilisée. Parce que cet enregistrement est accompli par le code spécifique à votre application, **feature-u** peut fonctionner sur n'importe quelle plateforme React, telle que : `[react-web](https://reactjs.org/)`, `[react-native](https://facebook.github.io/react-native/)`, et `[expo](https://expo.io/)`... **_voir:_** `[Enregistrement React](https://feature-u.js.org/1.0.1/detail.html#react-registration)`
4. _en guise d'aperçu_, la valeur de retour de `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)` est un objet `[Fassets](https://feature-u.js.org/1.0.1/api.html#Fassets)`, qui promeut le Visage Public accumulé de toutes les fonctionnalités, et est exporté pour fournir la `[Communication Inter-Fonctionnalités](https://feature-u.js.org/1.0.1/crossCommunication.html)`.

### [Communication Inter-Fonctionnalités](#e98c)

En soutien à la **Collaboration entre Fonctionnalités** _qui ne rompt pas l'encapsulation_, **feature-u** promeut les ressources basées sur les fonctionnalités à travers quelque chose appelé `fassets` (feature assets). C'est ainsi que toute la **Communication Inter-Fonctionnalités** est accomplie. Vous pouvez penser à cela comme le **Visage Public** d'une fonctionnalité.

**Note de bas de page** : Le terme `fassets` est un jeu de mots. Bien qu'il se prononce "facet" _et soit vaguement lié à ce terme_, il s'écrit fassets (c'est-à-dire feature assets).

Une fonctionnalité peut exposer ce qu'elle juge nécessaire à travers l'aspect intégré `[Feature.fassets](https://feature-u.js.org/1.0.1/api.html#fassets)`. Il n'y a pas de réelle contrainte sur cette ressource. Elle est vraiment ouverte.

![Image](https://cdn-media-1.freecodecamp.org/images/0*TbIrHeN2HxFwFzhY.png)

L'aspect `[fassets](https://feature-u.js.org/1.0.1/api.html#fassets)` a une directive `define` où les ressources sont cataloguées.

Voici un exemple simple de la manière dont les `fassets` sont définis :

**feature-u** accumule les `fassets` de toutes les fonctionnalités actives, et les promeut à travers l'objet `[Fassets](https://feature-u.js.org/1.0.1/api.html#Fassets)` _(émis par `[launchApp()](https://feature-u.js.org/1.0.1/api.html#launchApp)`)_.

**Note de bas de page** : Il existe plusieurs façons d'obtenir l'accès à l'objet `Fassets` _(voir `[Obtenir l'objet fassets](https://feature-u.js.org/1.0.1/crossCommunication.html#obtaining-fassets-object)`)_.

Pour référencer une ressource `fassets`, il suffit de la déréférencer comme toute autre référence d'objet. Il existe également une méthode `[Fassets.get()](https://feature-u.js.org/1.0.1/api.html#Fassets_get)` qui peut être fournie avec des `[Wildcards](https://feature-u.js.org/1.0.1/crossCommunication.html#wildcards-adding-dynamics)`, retournant un tableau de ressources.

Ceci est un exemple de philosophie **push**. Ici, le fournisseur promeut simplement publiquement une ressource pour que d'autres fonctionnalités l'utilisent **(prenez-la ou laissez-la)**. Le fournisseur dit simplement : _"voici mon Visage Public"_.

Vous pouvez trouver plus d'informations sur ce sujet dans `[Communication Inter-Fonctionnalités](https://feature-u.js.org/1.0.1/crossCommunication.html)`.

### [Composition UI Basée sur les Fonctionnalités](#e98c)

Il est courant qu'un composant UI soit une accumulation de sous-composants qui s'étendent sur plusieurs fonctionnalités. Par conséquent, **la Composition UI est une partie très importante de la Communication Inter-Fonctionnalités**.

En soutien à cela, **feature-u** introduit le composant d'ordre supérieur (HoC) `[withFassets()](https://feature-u.js.org/1.0.1/api.html#withFassets)` qui connecte automatiquement les propriétés fasset à un composant. C'est un modèle courant popularisé par Redux `connect()` _(simplifiant l'accès des composants à l'état de l'application)_.

Voici comment un composant accéderait à un `company.logo` _(définis par une autre fonctionnalité)_:

Le HoC `[withFassets()](https://feature-u.js.org/1.0.1/api.html#withFassets)` connecte automatiquement les actifs de fonctionnalités nommés en tant que propriétés de composant via le hook `[mapFassetsToPropsStruct](https://feature-u.js.org/1.0.1/api.html#mapFassetsToPropsStruct)`. Dans cet exemple, parce que la propriété `Logo` est un composant, `MyComponent` peut simplement la référencer en utilisant JSX.

Vous pouvez trouver plus d'informations sur ce sujet dans `[Composition UI](https://feature-u.js.org/1.0.1/crossCommunication.html#ui-composition)`.

### [Contrats de Ressources](#e98c)

Il est courant que la Composition UI soit représentée comme un contrat, où un composant dans une fonctionnalité a une série de besoins d'injection qui doivent être fournis par d'autres fonctionnalités.

L'aspect `[fassets](https://feature-u.js.org/1.0.1/api.html#fassets)` a des constructions supplémentaires pour faciliter cet arrangement contractuel, permettant à **feature-u** de fournir plus de validation dans le processus.

Plutôt que de simplement définir des ressources dans une fonctionnalité et de les utiliser dans une autre :

* Une fonctionnalité donnée peut spécifier une série de besoins d'injection en utilisant la directive `fassets.use`. Cela identifie un ensemble de **clés d'injection** qui identifient de manière unique ces ressources.
* D'autres fonctionnalités fourniront ce contenu en utilisant la directive `fassets.defineUse`, en référençant ces mêmes **clés d'injection**.

Cela représente davantage une philosophie **pull**. Cela donne à **feature-u** plus de connaissances sur le processus, lui permettant de vérifier que les ressources fournies sont correctes.

Les wildcards (`*`) peuvent être utilisés pour ajouter des dynamiques supplémentaires au processus, permettant aux fonctionnalités d'injecter leur contenu de manière autonome.

Voici une fonctionnalité `main` qui tire une série de sous-composants _(liens et corps)_ d'autres fonctionnalités :

**fonctionnalité main** :

Parce que notre spécification inclut des wildcards, une série de définitions correspondra !

Voici le composant `MainPage` qui remplit le contrat d'utilisation :

Lorsque `[withFassets()](https://feature-u.js.org/1.0.1/api.html#withFassets)` rencontre des wildcards (`*`), il accumule simplement toutes les définitions correspondantes, et les promeut comme des tableaux.

Grâce à cette implémentation, **toute fonctionnalité peut s'injecter dynamiquement dans le processus de manière autonome**! De plus, cette dynamique gère implicitement le cas où une fonctionnalité est dynamiquement désactivée **(très cool en effet)**!!

Les extraits suivants sont tirés d'autres fonctionnalités qui fournissent les définitions pour le contenu à injecter :

**fonctionnalité panier**

**fonctionnalité recherche**

Deux fonctionnalités externes (**panier** et **recherche**) définissent le contenu qui est demandé par la fonctionnalité **main**.

La directive `fassets.defineUse` exige que les clés de ressource correspondent à une demande de fonctionnalité `fassets.use`. C'est le contrat qui fournit à **feature-u** des informations lors de l'application de sa validation.

**Note de bas de page** : Parce que nous traitons également de la navigation, nous introduisons `[react-router](https://reacttraining.com/react-router/)` dans le mélange (avec les composants `Link` et `Route`). En raison de la conception V4 de RR, nos routes sont également gérées par composition de composants _(voir `[Routes Basées sur les Fonctionnalités](https://feature-u.js.org/1.0.1/featureRouter.html)` pour plus d'informations)_.

Vous pouvez trouver plus d'informations sur ce sujet dans `[Composition UI](https://feature-u.js.org/1.0.1/crossCommunication.html#ui-composition)`.

### [Activation des Fonctionnalités](#e98c)

Les fonctionnalités peuvent être dynamiquement désactivées en définissant la propriété booléenne `Feature.enabled` _(faisant partie des `[Aspects Intégrés](https://feature-u.js.org/1.0.1/detail.html#built-in-aspects)`)_:

Dans cet exemple, c'est comme si la fonctionnalité `sandbox` n'existait pas. En d'autres termes, **elle a été logiquement supprimée**.

Typiquement, cet indicateur est basé sur une expression d'exécution, permettant au code packagé d'être activé/désactivé dynamiquement pendant le processus de démarrage de l'application :

Cette dynamique est utile dans un certain nombre de situations différentes. Par exemple :

* certaines fonctionnalités peuvent nécessiter une mise à niveau de licence
* d'autres fonctionnalités peuvent être utilisées uniquement à des fins de diagnostic, et sont désactivées par défaut

Vous pouvez trouver plus d'informations sur ce sujet dans `[Activation des Fonctionnalités](https://feature-u.js.org/1.0.1/enablement.html)`.

### [En Résumé](#e98c)

Le diagramme suivant résume les **Concepts de Base** de **feature-u** _(comme discuté ci-dessus)_:

![Image](https://cdn-media-1.freecodecamp.org/images/1*qsohsNr9SgLca22xW6r1eQ.png)

### [Avantages](#e98c)

Il y a de nombreux avantages à utiliser **feature-u**!

![Image](https://cdn-media-1.freecodecamp.org/images/1*SJ-3bETYSjbchI28hEXlUw.jpeg)

Les deux artefacts fondamentaux dont sont dérivés la plupart des avantages sont :

* Un moyen formel par lequel les fonctionnalités peuvent collaborer entre elles _(`[Communication Inter-Fonctionnalités](http://localhost:4000/crossCommunication.html)`)_, les rendant vraiment **plug-and-play**  
Cela inclut la capacité pour la `[Composition UI](http://localhost:4000/crossCommunication.html#ui-composition)` de traverser les limites des fonctionnalités. Cela permet même au contenu UI d'être injecté de manière autonome. C'est quelque chose qui doit être vu... cela montre très bien **feature-u**.
* Une réduction significative du code standard à travers :  
Configuration automatique des frameworks utilisés _(via des extensions de plugins — `[Aspects Extensibles](http://localhost:4000/detail.html#extendable-aspects)`)_  
Initialisation du démarrage qui est encapsulée dans les fonctionnalités _(via `[Hooks de Cycle de Vie de l'Application](http://localhost:4000/appLifeCycle.html)`)_

La liste suivante d'avantages peut être directement corrélée aux considérations qui ont formé la base de pourquoi **feature-u** a été développé _(voir : `[Pourquoi feature-u ?](http://localhost:4000/why.html)`)_.

1. **Encapsulation des Fonctionnalités** : _isoler les limites des fonctionnalités améliore la gestion du code_
2. **Collaboration entre Fonctionnalités** : _promouvoir la **Communication Inter-Fonctionnalités** à travers une Interface Publique basée sur les fonctionnalités bien définie_
3. **Composition UI Basée sur les Fonctionnalités** : _faciliter la **composition de composants inter-fonctionnalités** transparente_
4. **Hooks de Cycle de Vie de l'Application** : _les fonctionnalités peuvent s'initialiser elles-mêmes sans dépendre d'un processus externe_
5. **Activation des Fonctionnalités** : _activer/désactiver les fonctionnalités via un interrupteur d'exécution_
6. **Minimiser les Problèmes de Dépendance d'Ordre des Fonctionnalités** _pendant l'expansion du code en ligne_
7. **Intégration des Frameworks** : _configurer automatiquement le(s) framework(s) utilisé(s) (correspondant à la pile d'exécution de l'application) en accumulant tous les aspects des fonctionnalités (employant une API extensible)_
8. **Promotion des Composants UI** : _les fonctionnalités peuvent promouvoir de manière autonome leurs composants UI à travers la Gestion des Routes Basée sur les Fonctionnalités_
9. **Source Unique de Vérité** : _est facilitée de plusieurs manières au sein de l'implémentation d'une fonctionnalité_
10. **Démarrage Simplifié de l'Application** : _lancer une application peut être accompli par une seule ligne de code exécutable !_
11. **Fonctionne sur n'importe quelle Plateforme React** _React Web, React Native, Expo, etc._
12. **Plug-and-Play** : _les fonctionnalités peuvent être plus facilement ajoutées ou supprimées_

**feature-u** vous permet de **concentrer votre attention sur l'aspect "business" de vos fonctionnalités !**

_Allez de l'avant et calculez !!_

### [Références](#e98c)

* [Une approche basée sur les fonctionnalités pour le développement React](http://ryanlanciaux.com/blog/2017/08/20/a-feature-based-approach-to-react-development/) _... Ryan Lanciaux_
* [Comment mieux organiser vos applications React ?](https://medium.com/@alexmngn/how-to-better-organize-your-react-applications-2fd3ea1920f1) _... Alexis Mangin_
* [Comment utiliser Redux dans des applications JavaScript hautement scalables ?](https://medium.com/@alexmngn/how-to-use-redux-on-highly-scalable-javascript-applications-4e4b8cb5ef38) _... Alexis Mangin_
* [La manière 100% correcte de structurer une application React (ou pourquoi il n'y a pas de telle chose)](https://hackernoon.com/the-100-correct-way-to-structure-a-react-app-or-why-theres-no-such-thing-3ede534ef1ed) _... David Gilbertson_
* [Redux pour la gestion d'état dans les grandes applications web](https://blog.mapbox.com/redux-for-state-management-in-large-web-apps-c7f3fab3ce9b) _... David Clark_