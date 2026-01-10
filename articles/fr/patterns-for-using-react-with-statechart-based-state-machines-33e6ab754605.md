---
title: Modèles pour utiliser React avec des machines à états basées sur les Statecharts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-01T21:50:47.000Z'
originalURL: https://freecodecamp.org/news/patterns-for-using-react-with-statechart-based-state-machines-33e6ab754605
coverImage: https://cdn-media-1.freecodecamp.org/images/1*m3KYQevuZRrlEgP684bk_Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Statecharts
  slug: statecharts
- name: technology
  slug: technology
seo_title: Modèles pour utiliser React avec des machines à états basées sur les Statecharts
seo_desc: 'By Shawn McKay

  Statecharts and state machines offer a promising path for designing and managing
  complex state in apps. For more on why statecharts rock, see the first article of
  this series.

  But if statecharts are such an excellent solution for manag...'
---

Par Shawn McKay

Les Statecharts et les machines à états offrent une voie prometteuse pour concevoir et gérer les états complexes dans les applications. Pour en savoir plus sur pourquoi les Statecharts sont formidables, consultez [le premier article](https://medium.freecodecamp.org/how-to-visually-design-state-in-javascript-3a6a1aadab2b) de cette série.

**Mais si les Statecharts sont une solution si excellente pour gérer l'UI et l'état en JavaScript (JS), pourquoi n'y a-t-il pas plus d'élan derrière eux ?**

L'une des principales raisons pour lesquelles les Statecharts n'ont pas gagné en popularité dans le monde du front-end est que les meilleures pratiques ne sont pas encore établies. Il n'est pas clairement établi comment utiliser les machines à états avec des bibliothèques UI populaires basées sur les composants comme React, Vue ou Angular.

Bien qu'il soit peut-être trop tôt pour déclarer les meilleures pratiques pour les Statecharts en JS, nous pouvons explorer certains modèles utilisés par les bibliothèques d'intégration de machines à états existantes.

### Machine à états Statechart

Les Statecharts fonctionnent à la fois pour la conception visuelle et comme code sous-jacent pour une machine à états basée sur un graphe.

Gardez à l'esprit que nous en sommes aux premiers jours de l'utilisation des Statecharts avec JS, et qu'il peut être intéressant d'expérimenter avec une variété de bibliothèques ou même de développer la vôtre. Cela dit, [XState](https://github.com/davidkpiano/xstate) est actuellement en tête des bibliothèques de machines à états Statechart en JS.

![Image](https://cdn-media-1.freecodecamp.org/images/7jucyNQr2bs02ta20zRnBRj-uUQ0DvKFoLLk)
_[https://gist.github.com/ShMcK/769a179f89f1d7db1f83363cc2e42399](https://gist.github.com/ShMcK/769a179f89f1d7db1f83363cc2e42399" rel="noopener" target="_blank" title=")_

Le code de la machine à états ci-dessus peut générer un diagramme Statechart beaucoup plus lisible lorsqu'il est passé en JSON au [Visualiseur XState](https://github.com/davidkpiano/xstate#visualizer).

![Image](https://cdn-media-1.freecodecamp.org/images/eUlLxIJzgceeXmtnFNwZVl9ZdPtOJm5GUFAx)

Vous pouvez même travailler dans l'autre sens, en commençant par concevoir visuellement puis en exportant vers une configuration XState en utilisant [sketch.systems](http://sketch.systems). Nous n'avons pas encore toutes les pièces au même endroit, mais il n'y a pas de sérieux obstacles techniques à une solution open source.

![Image](https://cdn-media-1.freecodecamp.org/images/q3OYT9hd3E2M93-qLHciSoHceVwcC5ELrs7e)

Maintenant que nous avons une idée de ce que fait XState, voyons ce qu'il ne fait pas.

> Slogan de XState : « machines à états finis sans état et Statecharts ».

Alors, que signifie pour une machine à états d'être **sans état** ?

### Machines sans état

Les machines sans état offrent un **plan** non opinionné pour la gestion de l'état — une sorte de solution « faites-le vous-même » qui ne dicte pas où ou comment l'état dans votre application est stocké.

Tout comme un composant de présentation, une machine sans état est composée de fonctions pures, est immutable et ne maintient aucun état. Elle ne suit aucun passé, présent ou futur — mais elle peut être utilisée pour vous aider à calculer chacun d'eux.

Gérer votre état peut être aussi simple que de le stocker dans une variable d'état locale.

![Image](https://cdn-media-1.freecodecamp.org/images/kAqxO0cq9qT-nMGfnhlsFaSxINVkpP233WSb)

Les machines sans état ne vous donnent pas grand-chose dès la sortie de la boîte. Pour déclencher une transition, nous devons toujours passer le nœud d'état actuel pour trouver le suivant. XState peut vous indiquer quelles actions doivent être déclenchées à chaque changement d'état, mais vous devrez trouver un moyen de gérer les actions vous-même.

Si vous êtes intéressé par une solution plus complète, envisagez de rendre votre machine à états **stateful**.

### Machines à états

Une machine à états suit votre position de nœud sur le graphe d'état et gère le déclenchement des actions. Il n'est pas nécessaire de passer l'état actuel lors des transitions — elle suit votre nœud d'état actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/D1FxAQN9JgcjK9TwGl1TxXHUewyTFZBAIvn9)

En résumé, l'instance de la machine à états ci-dessus :

* détermine la position de l'état vert à « Ringing »
* limite les événements de transition actifs violets possibles à `CANCEL` ou `SNOOZE`
* déclenche l'action `startRing` à l'entrée
* déclenche l'action `stopRing` en quittant l'état

Bien sûr, il existe plus d'une façon de créer une machine à états. Nous revenons à la question de savoir où gérer l'état :

* dans l'état du composant existant ?
* dans une machine à états connectée ?

Explorons quelques modèles de conception avec des exemples, en commençant par les **composants à états**.

### Composants à états

Un composant à états, comme vous pouvez l'imaginer, gère l'état dans le composant, ou dans un composant d'ordre supérieur enveloppant. Dans React, ce serait en tant que `state`. Stocker l'état dans une bibliothèque UI garantit que les changements ne seront pas manqués et déclencheront des re-rendus.

C'est l'approche d'une bibliothèque appelée [React-Automata](https://github.com/MicheleBertoli/react-automata) qui utilise un composant d'ordre supérieur initié par `withStatechart`.

![Image](https://cdn-media-1.freecodecamp.org/images/6hX-DEHCmfZZbMsyp8bE4MyZgqmKr-BmqfR3)

React-Automata offre plusieurs modèles pour utiliser les Statecharts avec des composants :

* état depuis les props
* rendu conditionnel depuis un contexte
* état depuis les actions

Nous passerons en revue chaque modèle et considérerons les avantages et les inconvénients.

#### **État depuis les Props**

Passer l'état directement dans les composants semble être la solution la plus évidente.

![Image](https://cdn-media-1.freecodecamp.org/images/CfqmdxiglBKlVIBCSOBMrKoSnnjvqYuwsBtD)

Dans React-Automata, l'état peut être passé en y accédant sur la prop `machineState` — une référence à la machine à états réelle.

![Image](https://cdn-media-1.freecodecamp.org/images/Gr113rIoWhqeyyCvUT3GSjebtKN4y14VtQCg)

Mais méfiez-vous, **ceci n'est en aucun cas une meilleure pratique**. Dans l'exemple ci-dessus, l'intégration a **couplé** le Statechart au composant, conduisant à une mauvaise séparation des préoccupations.

Considérez que le Statechart et les composants peuvent permettre une division propre car ils résolvent des problèmes différents :

* Statecharts : **quand** les choses se produisent, par exemple, entrer dans l'état, actions déclenchées
* composants : **comment** et **quoi** se produit, par exemple, la vue, les interactions utilisateur

Alternativement, vous pourriez découpler le composant de la machine à états en rendant conditionnellement avec un rendu par défaut de non-rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/FzXtUh2ITWYn0AePrsqZZ3Tme-8hcrwfnwhh)

Certes, il doit y avoir un moyen plus naturel de configurer le rendu conditionnel sans avoir à transformer tous vos rendus en instructions `if/else` et `switch`.

### **Rendu conditionnel depuis un contexte**

L'état accessible par un contexte n'a pas besoin d'être passé directement.

![Image](https://cdn-media-1.freecodecamp.org/images/I4yIlaK9q13fHzI7H20RN7XcyM0KbCgtgO6d)

React-Automata fournit un modèle pour le rendu conditionnel des composants enfants en utilisant le contexte de React et un composant `<State>`. Notez que la propriété `value` peut correspondre à une chaîne, un tableau de chaînes, ou même un motif basé sur des globs.

![Image](https://cdn-media-1.freecodecamp.org/images/9g7rEjSlDp5DZtsunVJMkr4lnLQzBzglx3k4)

Si la valeur de l'état correspond à `Ringing`, les enfants à l'intérieur du composant `State` seront rendus. Sinon, rien.

L'état depuis le contexte peut aider à clarifier le nombre de combinaisons possibles de vues d'états finis. Comme dans le cas ci-dessus, il est clair qu'il n'y a que deux configurations possibles.

Si les configurations de vue commencent à devenir ingérables, React-Automata offre un modèle de prop de rendu qui passe un booléen basé sur la valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/JR-iT393EkkGzs5vqgMcMdI1LnAbiE9Bze3-)

De même, il est possible de rendre conditionnellement basé sur les actions du contexte.

![Image](https://cdn-media-1.freecodecamp.org/images/EVHZhlEFxplZquVI9C9pihSIEW1jQHhsYTkl)

Le rendu conditionnel basé sur l'état ou les actions maintient un couplage entre le Statechart et les composants, mais de manière moins explicite à travers le contexte. Comment pourriez-vous donner aux composants leur état isolé à part des Statecharts ?

#### **État depuis les actions**

Il est possible d'utiliser les Statecharts pour mettre à jour l'état interne d'un composant lié en utilisant des actions comme déclencheurs.

![Image](https://cdn-media-1.freecodecamp.org/images/xe2pZXijfRO5YUV19NX1LBZfMdUONssLBqnY)

React-automata vérifie les méthodes sur un composant et appelle les fonctions si les noms correspondent aux actions déclenchées.

Par exemple, l'action onEntry `startRing` est déclenchée lorsque la machine à états entre dans `Ringing`, provoquant le changement de l'état `AlarmClock` à `ringing`. En quittant l'état `Ringing`, `stopRing` est déclenchée, et `ringing` est défini à `false`.

![Image](https://cdn-media-1.freecodecamp.org/images/mrkROREfV5flyHGYngYrWHyFSWVHSNS-vrdq)

Notez que, bien que ces méthodes soient appelées avec des paramètres, les méthodes ont déjà accès à tout ce dont elles ont besoin depuis `machineState` via les props.

L'utilisation de l'état interne du composant géré via des actions conduit à un fort découplage des composants des Statecharts. Cependant, cela peut également créer un certain degré de désordre ou de confusion dans les composants. Il n'est pas explicitement clair comment ou quand les méthodes seront appelées sans examiner les noms des actions dans le Statechart. Pour cette raison, j'appelle souvent mes actions et méthodes `enterX` ou `exitX` afin de rendre explicitement clair pourquoi et où elles sont déclenchées.

### Machines à états externes

Une autre option à considérer est de stocker l'état en dehors de votre framework UI. Comme avec d'autres bibliothèques de gestion d'état comme Redux, les composants peuvent être connectés à une machine à états externe et mis à jour avec des événements « on state change » et « on action ».

![Image](https://cdn-media-1.freecodecamp.org/images/Cpdc3lKa2eFWX82Vu7SoPHXmcb4mWTpKAY9b)

Par exemple, [XStateful](https://github.com/avaragado/xstateful) est un wrapper autour de XState qui gère l'état, les transitions, l'émission d'événements, le déclenchement d'actions, et plus encore.

![Image](https://cdn-media-1.freecodecamp.org/images/8KMPv6PSbvRMQXebFnVL6PQKY6nlJn40TUHC)

XStateful fonctionne bien avec un connecteur React appelé [XStateful-React](https://github.com/avaragado/xstateful-react).

![Image](https://cdn-media-1.freecodecamp.org/images/FBxnxH0x9tzYnBpMJvtyLgndKtMlhZxCgPrw)

XStateful-React a beaucoup en commun avec React-Automata. Mais il y a au moins une différence significative — l'instance de la machine à états n'est pas gérée dans un composant.

![Image](https://cdn-media-1.freecodecamp.org/images/vjYPif3blpUKKDprAMfUigXfz5r1vpyPqzfG)

Alors, comment fonctionne l'état externe depuis les reducers dans XStateful ?

### État et données

Les applications nécessitent souvent plus que simplement le nœud d'état dans un graphe d'état — elles nécessitent également des données. Souvent, ces données doivent être synchronisées entre les composants, de manière à pouvoir être frustrées si elles doivent être passées depuis le parent partagé le plus haut.

Il existe des solutions populaires existantes pour synchroniser les données, telles que Redux, ou [mon wrapper de gestion d'état pour Redux](https://github.com/rematch/rematch). Malheureusement, celles-ci ne fonctionnent pas bien avec de nombreux wrappers d'état tels que React-Automata en raison d'un problème ouvert avec le passage des refs dans React Redux (voir ce [problème ouvert avec connect() et React.forwardRef](https://github.com/reduxjs/react-redux/issues/914)).

**Une solution d'état complète devrait gérer à la fois l'état et les données.**

XStateful offre justement une telle solution d'état et de données en utilisant un [modèle de réducteur d'état](https://blog.kentcdodds.com/the-state-reducer-pattern-%EF%B8%8F-b40316cfac57), similaire à Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/8xMXiOZdWjR-P3ctNVeMB4LE4v7ZvPTUuybt)

Les abonnés de la machine à états écoutent et mettent à jour les changements basés sur les actions émises par la machine à états. Notez que XState fait référence aux données en tant qu'**état étendu**, ou `extstate`.

![Image](https://cdn-media-1.freecodecamp.org/images/hdrk3HqBbfBkNfd2gWC1VEKHSj1Py-isMhIA)

Ce modèle de réducteur particulier peut sembler peu familier, cependant, il est largement utilisé dans des projets tels que [ReasonReact](https://reasonml.github.io/reason-react/docs/en/state-actions-reducer.html).

Les données peuvent également être accessibles dans les rendus conditionnels sur la propriété `cond`.

![Image](https://cdn-media-1.freecodecamp.org/images/4jrU5i-bzBirWwqhn3ojmLpGkk3peLjRY8BW)

**Faites attention** à l'utilisation de l'état pour rendre conditionnellement les composants, car cela crée un ensemble non déterministe d'états possibles. Vous n'êtes plus limité au nombre d'états, mais maintenant au nombre de combinaisons d'états et de données. Vous perdez les fonctionnalités déterministes, discutées plus tard dans la section sur les tests.

Ces données peuvent être passées dans votre composant en utilisant un modèle de prop de rendu.

![Image](https://cdn-media-1.freecodecamp.org/images/r63dar8rwDffa7lnxUoUjYpeUlY0gGfl8YTT)

Il y a moins besoin d'outils de gestion d'état comme Redux si les données peuvent être stockées dans un outil de machine à états complet comme XStateful.

### Tests

Les machines à états offrent également un meilleur chemin pour les tests front-end.

**La nature déterministe des machines à états crée la possibilité de tests front-end simplifiés.**

Dans React-Automata, vous pouvez générer automatiquement des tests de snapshot en utilisant `testStatechart`, une méthode qui prend la configuration XState et le composant.

![Image](https://cdn-media-1.freecodecamp.org/images/32aHtwD8mghMTy8m1zwteefbxEX8wSSDhWgl)

`testStatechart` parcourt le graphe d'état et crée un [test de snapshot Jest](https://jestjs.io/docs/en/snapshot-testing) pour chaque configuration possible du composant. Il activera et désactivera vos divers composants `<State />`, `<Action />`, conduisant à un enregistrement de toutes les combinaisons possibles de rendus conditionnels.

### Devtools

Les Devtools jouent un rôle actif dans ce qui rend une bibliothèque conviviale pour les développeurs — le débogage peut être la partie la plus difficile ou la plus simple de votre travail.

À cet égard, React-Automata offre une intégration utile via Redux Devtools. Chaque composant connecté devient une instance nommée dans les devtools, et chaque transition et action sont affichées chronologiquement lorsque les actions sont présentées dans les devtools Redux.

![Image](https://cdn-media-1.freecodecamp.org/images/q9HFedJVnw4i1qaVE26n3x9lB03JgZ0jfBfE)

XState offre un ensemble entièrement nouveau de variables à suivre. Considérez l'exemple suivant [par Erik Mogensen](https://codepen.io/mogsie/pen/YapZjZ) sur les types d'informations qu'un débogueur XState peut suivre.

![Image](https://cdn-media-1.freecodecamp.org/images/culeh91to9lyS13adQMF0gyawStWoPWeAmpR)

Cela ne signifie pas que les devtools des machines à états doivent ressembler à nos devtools existants. Les devtools des machines à états présentent une opportunité pour une expérience de débogage plus visuelle.

### Conclusion

Bien que nous en soyons encore aux premiers jours des Statecharts en JS, il existe suffisamment d'options disponibles pour commencer à développer des applications sur XState. Nous pouvons apprendre de ces modèles de développement pour améliorer les bibliothèques disponibles et créer des outils pour soutenir le potentiel énorme de la programmation basée sur le visuel.

Ayant développé des applications avec des Statecharts au cours des trois derniers mois, j'ai personnellement trouvé ces nouveaux modèles être un bol d'air frais. La collaboration est devenue beaucoup plus confortable, car les membres de l'équipe peuvent saisir visuellement la logique sous-jacente d'un système important et en croissance.

Mon espoir est que cet article aidera les autres à trouver le développement basé sur les Statecharts plus accessible. Si vous l'avez trouvé utile, donnez un applaudissement et partagez-le 😊