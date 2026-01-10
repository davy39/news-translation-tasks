---
title: 'Construction du calculateur de portée de batterie Tesla avec React (Partie
  2 : version Redux)'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-12T15:15:04.000Z'
originalURL: https://freecodecamp.org/news/building-teslas-battery-range-calculator-with-react-part-2-redux-version-2ffe29018eec
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8hlNoLDBy5XWZct5tAtPoA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: Redux
  slug: redux
- name: Web Development
  slug: web-development
seo_title: 'Construction du calculateur de portée de batterie Tesla avec React (Partie
  2 : version Redux)'
seo_desc: 'By Matthew Choi

  This tutorial is the second part of building Tesla’s battery range calculator with
  React.

  In part 1, after constructing the project through create-react-app, we implemented
  each component by subdividing the UI. We managed the state an...'
---

Par Matthew Choi

Ce tutoriel est la deuxième partie de la construction du calculateur de portée de batterie Tesla avec React.

Dans la partie 1, après avoir construit le projet via create-react-app, nous avons implémenté chaque composant en subdivisant l'interface utilisateur. Nous avons géré l'état et les événements en utilisant l'état local et les props, et avons complété l'ensemble de l'application.

Si vous ne l'avez pas encore lu, assurez-vous de consulter la Partie 1, qui se concentre sur React, [ici](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee) :

[**Construction du calculateur de portée de batterie Tesla avec React (Partie 1)**](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee)  
[_Dans cette série d'articles, je vais vous guider à travers le processus de construction du calculateur de portée de batterie Tesla avec React..._medium.freecodecamp.com](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee)

Dans cet article, nous allons introduire Redux, une solution de gestion d'état, pour voir comment nous pouvons transformer notre application en une application qui gère l'état de l'application avec Redux.

Voici l'image finale de notre application dans la partie 2 :

![Image](https://cdn-media-1.freecodecamp.org/images/Li0MK48ShwxYzOPdWJ0059b54M1Y5mesLhoj)

? Consultez la démonstration en direct de la [partie 2](http://redux-tesla-charge-calculator.surge.sh/).

Avant de voir ce qu'est Redux, voyons pourquoi nous devons utiliser Redux pour résoudre des problèmes.

### 1. Quel problème résolvons-nous ?

Redux devient la manière de facto de construire des applications React. Mais Redux doit-il être utilisé dans toutes les applications React ? Au minimum, toutes les applications n'auront pas besoin d'une solution de gestion d'état ambitieuse dès le début.

Les tendances actuelles du développement front-end sont **basées sur les composants**. Les composants peuvent avoir des états de données et des états d'interface utilisateur, et l'état qu'ils doivent gérer devient de plus en plus compliqué à mesure que votre application grandit.

Des solutions de **gestion d'état** ont émergé pour résoudre les problèmes suivants, et Redux devient populaire en tant que standard parmi d'autres solutions.

* les composants partagent l'état
* l'état doit être accessible de n'importe où
* les composants doivent muter l'état
* les composants doivent muter l'état d'autres composants

Redux est une **bibliothèque de gestion d'état**, qui est un outil qui vous permet de stocker l'état de notre application quelque part, de muter l'état et de recevoir l'état mis à jour.

En d'autres termes, avec Redux, nous avons un seul endroit où nous pouvons référencer l'état, changer l'état et obtenir l'état mis à jour.

Redux a été écrit en pensant à React, mais il est également **agnostique de framework** et peut même être utilisé avec des applications Angular ou jQuery.

> Je vous recommande de lire **Dan Abramov's** [You Might Not Need Redux](https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367#.uz11a0vkc) avant de choisir Redux.

### 2. Flux de données dans Redux

Comme vous l'avez vu dans la partie 1, dans React, les données sont transmises à travers le composant en utilisant les props. Cela s'appelle le **flux de données unidirectionnel** qui circule du parent à l'enfant.

En raison de ces caractéristiques, la communication entre les composants autres que la relation parent-enfant n'est pas claire.

![Image](https://cdn-media-1.freecodecamp.org/images/D6WWNQW1cIy98DIqBqpMbaz5cG5DGxAIAPTM)

React ne recommande pas la communication directe **composant-à-composant** comme montré ci-dessus. Il existe une manière suggérée pour cela dans React, mais vous devez l'implémenter vous-même.

Selon la **documentation React** :

> Pour la communication entre deux composants qui n'ont pas de relation parent-enfant, vous pouvez configurer votre propre système d'événements global. ... Le modèle Flux est l'une des manières possibles d'organiser cela.

![Image](https://cdn-media-1.freecodecamp.org/images/mzhkN3GbyDepg6QmY2oNVRt9-pQUVfTNPtw8)

C'est là que Redux devient pratique.

Redux fournit une solution pour gérer tout l'état de l'application dans un seul endroit appelé un `store`.

Le composant `dispatch` ensuite le changement d'état au store au lieu de le passer directement aux autres composants.

Les composants qui doivent être informés des changements d'état peuvent `s'abonner` au store.

> Redux est, en un mot, un **conteneur d'état** qui représente et gère l'état d'une application en tant qu'objet unique à partir d'une application basée sur JavaScript.

### 3. Concept de base de Redux

Redux lui-même est très simple. L'état de l'application que nous avons créée dans le dernier article peut être représenté comme un objet générique comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/r-QHkrWij0nOfDNEcqcMlGeeT0uHFoy7KlZa)

Cet objet est le même que le modèle sans setters.

Pour changer cet état dans Redux, vous devez dispatcher une `action`.

Les actions sont des objets simples décrivant **ce qui s'est passé** dans l'application, et servent de seule manière à décrire une **intention de muter les données**. C'est l'un des **choix de conception fondamentaux** de Redux.

Voici quelques exemples à implémenter dans notre application bientôt.

![Image](https://cdn-media-1.freecodecamp.org/images/i6SGgqJFAiUVMfH0MnnXKevPxQgFc3gYF3Ox)

Forcer toutes ces modifications d'état dans une action nous donnera une compréhension claire de ce qui se passe dans votre application. Lorsque quelque chose se produit, nous pouvons voir pourquoi cela s'est produit.

Maintenant, nous avons besoin d'une fonction appelée `reducer` pour lier ces états et actions ensemble. Un reducer n'est rien de plus qu'une fonction qui prend un état et une action comme arguments et retourne un **nouvel état**.

En un mot :

> **(state, action) => state**

Les actions décrivent uniquement qu'un événement s'est produit et ne spécifient pas **comment l'état de l'application change en réponse**. C'est le travail des reducers.

Voici un exemple de reducer à implémenter dans notre application :

![Image](https://cdn-media-1.freecodecamp.org/images/l9hxbT8w2vX33pXWjY9MHJhSJYsiKEwIxaPy)

### 4. Trois principes de Redux

J'ai mentionné `Flux` à plusieurs reprises. Flux est un **modèle de gestion d'état**, pas un outil téléchargeable comme Redux. Redux, en revanche, est une **implémentation pratique du modèle Flux** et a trois principes principaux.

### 4.1 Source unique de vérité

> L'état de l'ensemble de l'application est stocké dans un arbre d'objets au sein d'un **seul store**.

![Image](https://cdn-media-1.freecodecamp.org/images/msDr2OXjaSjecjp1J0LExZoeR07djQGP0LHO)

Puisque tous les états existent en un seul endroit, cela s'appelle une `source unique de vérité`.

Cette approche `un seul store` de Redux est l'une des principales différences entre lui et l'approche **Flux à plusieurs stores**.

Quels sont les avantages d'un seul arbre d'état ? Cela facilite le débogage des applications ou l'inspection interne et permet de mettre en œuvre facilement certaines fonctionnalités qui étaient auparavant difficiles à implémenter (par exemple, annuler / rétablir).

### 4.2 L'état est en lecture seule

> La seule façon de changer l'état est d'**émettre une action** qui décrit ce qui s'est passé.

En d'autres termes, l'application ne change pas directement l'état, mais exprime plutôt l'intention de transformer l'état en passant l'action.

En fait, si vous regardez l'API Redux, vous pouvez voir qu'elle se compose de seulement quatre méthodes :

```
store.dispatch(action)store.subscribe(listener)store.getState()replaceReducer(nextReducer)
```

Comme vous pouvez le voir, il n'y a pas de méthode **setState()**. Par conséquent, **passer une action** est le seul canal qui peut muter l'état de l'application.

### 4.3 Les changements sont effectués avec des fonctions pures

> Vous écrivez des reducers en tant que **fonctions pures** pour spécifier la manière concrète dont l'arbre d'état est transformé par une action.

Les reducers sont des fonctions pures qui prennent un état précédent et une action et retournent un nouvel état. Gardez à l'esprit que vous devez retourner un **nouvel objet d'état** au lieu de changer l'ancien état.

> « Étant donné les mêmes arguments, il doit calculer l'état suivant et le retourner. Pas de surprises. Pas d'effets secondaires. Pas d'appels API. Pas de mutations. Juste un calcul. » — [Documentation Redux](http://redux.js.org/docs/basics/Reducers.html)

La fonction pure a les caractéristiques suivantes :

* Elle ne fait pas d'appels réseau ou de base de données externes.
* Sa valeur de retour dépend uniquement des valeurs de ses paramètres.
* Ses arguments doivent être considérés comme « immuables », ce qui signifie qu'ils ne doivent pas être changés.
* Appeler une fonction pure avec le même ensemble d'arguments retournera toujours la même valeur.

### 5. Diviser l'application en conteneurs et composants

Maintenant, reconstruisons notre application de calculateur Tesla que nous avons faite dans la Partie 1 en version Redux.

Tout d'abord, regardons la **disposition générale de l'interface utilisateur des composants** de l'application qui sera implémentée dans cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/O2G59T0ExYs5ADbHl7lgwfc9vJgM0n12huLE)
_**disposition générale de l'interface utilisateur des composants**_

Placer la logique React et Redux à l'intérieur d'un seul composant peut être désordonné, il est donc recommandé de créer un composant `Présentation` à des fins de présentation uniquement, et un composant `Conteneur`, un composant enveloppant supérieur qui gère Redux et dispatch les actions.

Le rôle du composant parent Conteneur est de fournir des valeurs d'état aux composants de présentation, de gérer les événements et de communiquer avec Redux au nom des composants de présentation.

### 6. Liste des états et actions pour chaque composant

Référez-vous à la disposition complète des composants pour créer une liste des états et actions pour chaque composant :

```
TeslaCar Container :	state : wheels	action : N/A
```

```
TeslaStats Container :	state : carstats(array)	action : N/A	TeslaSpeedCounter Container : 	state : config.speed	action : SPEED_UP, SPEED_DOWN
```

```
TeslaTempCounter Container : 	state : config.temperature	action : TEMPERATURE_UP, TEMPERATURE_DOWN	TeslaClimate Container : 	state : config.climate	action : CHANGE_CLIMATE
```

```
TeslaWheel Container : 	state : config.wheel	action : CHANGE_WHEEL
```

### 7. Configuration du code de base du projet de la partie 1

> Si vous souhaitez passer directement à la partie 2 sans regarder la partie 1, vous devez d'abord construire la base de code en clonant le code de la [partie 1](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial).

Après le **npm start**, assurons-nous que l'application fonctionne.

* **git clone** [https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial](https://github.com/gyver98/part1-react-tesla-battery-range-calculator-tutorial)

![Image](https://cdn-media-1.freecodecamp.org/images/nZhI6ZwDG3l0rwSv6ZdW6cN4qCKxVlghhoAq)

* **npm install**

![Image](https://cdn-media-1.freecodecamp.org/images/DZNzI-OVy32CzU4Ww0w1JDCie3PB2wCGnsrY)

* **npm start**

![Image](https://cdn-media-1.freecodecamp.org/images/xtCHz-FGbWLurL5bPkPPhh23E3taWyYPLhRw)

### 8. Créer des créateurs d'actions pour chaque action

Maintenant que vous avez créé une liste d'actions, il est temps de créer des `créateurs d'actions`.

Un créateur d'action est une fonction qui crée littéralement un objet d'action. Dans Redux, les créateurs d'actions retournent simplement un objet d'action et passent la valeur d'argument si nécessaire.

**Exemple de créateur d'action changeWheel :**

```
const changeWheel = (value) => {  return {    type: 'CHANGE_WHEEL',    value  }}
```

Ces créateurs d'actions sont passés à la fonction dispatch comme valeur de résultat, et le dispatch est exécuté.

```
dispatch(changeWheel(size))
```

La fonction dispatch peut être accédée directement depuis le store via **store.dispatch()**, mais dans la plupart des cas, elle sera accédée en utilisant un helper comme `connect()` de react-redux. Nous verrons **connect** plus tard.

### 8.1 Créer Action.js

Créez un fichier index dans le répertoire src/actions et définissez les créateurs d'actions comme suit :

**src/actions/index.js**

```
import { counterDefaultVal } from '../constants/counterDefaultVal';
```

```
export const speedUp = (value) => {  return {    type: 'SPEED_UP',    value,    step: counterDefaultVal.speed.step,    maxValue: counterDefaultVal.speed.max  }}
```

```
export const speedDown = (value) => {  return {    type: 'SPEED_DOWN',    value,    step: counterDefaultVal.speed.step,    minValue: counterDefaultVal.speed.min  }}
```

```
export const temperatureUp = (value) => {  return {    type: 'TEMPERATURE_UP',    value,    step: counterDefaultVal.temperature.step,    maxValue: counterDefaultVal.temperature.max  }}
```

```
export const temperatureDown = (value) => {  return {    type: 'TEMPERATURE_DOWN',    value,    step: counterDefaultVal.temperature.step,    minValue: counterDefaultVal.temperature.min  }}
```

```
export const changeClimate = () => {  return {    type: 'CHANGE_CLIMATE'  }}
```

```
export const changeWheel = (value) => {  return {    type: 'CHANGE_WHEEL',    value  }}
```

```
export const updateStats = () => {  return {    type: 'UPDATE_STATS'  }}
```

* Consultez [index.js](https://gist.github.com/gyver98/9d088084834ec6a0f893c8576c7d9204#file-index-js)

Puisque nous avons besoin de **valeurs par défaut** basées sur le créateur d'action, nous définissons cette valeur constante dans constants/counterDefaultVal sous le répertoire src et l'importons.

**src/constants/counterDefaultVal.js**

```
export const counterDefaultVal = {  speed: {    title: "Speed",    unit: "mph",    step: 5,    min: 45,    max: 70  },  temperature: {    title: "Outside Temperature",    unit: "0",    step: 10,    min: -10,    max: 40  }}
```

* Consultez [counterDefaultVal.js](https://gist.github.com/gyver98/e560ca69057d40e0688000b94d7c0fd9#file-counterdefaultval-js)

### 9. Créer des Reducers pour chaque action

Les **Reducers** sont des fonctions qui reçoivent des objets d'état et d'action d'un store Redux et retournent un nouvel état à stocker dans Redux.

Il est important de ne pas modifier directement l'état donné ici. Les reducers doivent être des **fonctions pures** et doivent retourner un **nouvel état**.

* Les fonctions de reducer sont appelées depuis le **Container** qui sera créé lorsqu'une action utilisateur se produit.
* Lorsque le reducer retourne un état, **Redux transmet le nouvel état** à chaque composant, et **React rend chaque composant** à nouveau.

### 9.1 Structures de données immuables

* Type de données primitif JavaScript (nombre, chaîne, booléen, indéfini et null) => **immuable**
* Objet, tableau et fonction => **mutable**

Les modifications de la structure de données sont connues pour être boguées. Puisque notre store est composé d'objets et de tableaux d'état, nous devons implémenter **une stratégie pour garder l'état immuable**.

Il existe trois façons de changer l'état ici :

**ES5**

```
// Exemple Unstate.foo = '123';
```

```
// Exemple DeuxObject.assign(state, { foo: 123 });
```

```
// Exemple Troisvar newState = Object.assign({}, state, { foo: 123 });
```

Dans l'exemple ci-dessus, le premier et le deuxième mutent l'objet d'état. Le deuxième exemple mute car **Object.assign()** fusionne tous ses arguments dans le premier argument.

Le troisième exemple **ne mute pas l'état**. Il fusionne le contenu de l'état et { foo: 123 } dans un **nouvel objet vide** qui est le premier argument.

L'opérateur de propagation introduit dans **ES6** fournit un moyen plus simple de garder l'état immuable.

**ES6 (ES2015)**

```
const newState = { ...state, foo: 123 };
```

> Pour plus d'informations sur l'opérateur de propagation, voir [ici](http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html).

### 9.2 Créer un Reducer pour ChangeClimate

Tout d'abord, nous allons créer ChangeClimate via la méthode de **développement piloté par les tests**.

Dans la Partie 1, notre application a été générée via **create-react-app**, donc nous utilisons principalement `jest` comme test runner.

Jest recherche un fichier de test en utilisant l'une des conventions de nommage suivantes :

```
Fichiers avec le suffixe .js dans les dossiers __tests__Fichiers avec le suffixe .test.jsFichiers avec le suffixe .spec.js
```

Créez **teslaRangeApp.spec.js** dans src/reducers et créez un cas de test.

```
describe('test reducer', () => {  it('should handle initial stat', () => {    expect(      appReducer(undefined, {})    ).toEqual(initialState)  })})
```

Après avoir créé le test, exécutez la commande `npm test`. Vous devriez pouvoir voir le message d'échec du test suivant. Cela est dû au fait que nous n'avons pas encore écrit le **appReducer**.

![Image](https://cdn-media-1.freecodecamp.org/images/qfssmqzhC-uiewXk7Tdd9p9oSQ0RuETDUEdb)
_console npm test_

Pour que le premier test réussisse, nous devons créer **teslaRangeApp.js** dans le même répertoire reducers et écrire les fonctions **initial state et reducer**.

**src/reducers/teslaRangeApp.js**

```
const initialState = {  carstats:[    {miles:246, model:"60"},    {miles:250, model:"60D"},    {miles:297, model:"75"},    {miles:306, model:"75D"},    {miles:336, model:"90D"},    {miles:376, model:"P100D"}  ],  config: {    speed: 55,    temperature: 20,    climate: true,    wheels: 19  }}
```

```
function appReducer(state = initialState, action) {  switch (action.type) {        default:      return state   }}
```

```
export default appReducer;
```

Ensuite, importez teslaRangeApp.js depuis teslaRangeApp.spec.js et définissez initialState.

**src/reducers/teslaRangeApp.spec.js**

```
import appReducer from './teslaRangeApp';
```

```
const initialState =  {  carstats:[    {miles:246, model:"60"},    {miles:250, model:"60D"},    {miles:297, model:"75"},    {miles:306, model:"75D"},    {miles:336, model:"90D"},    {miles:376, model:"P100D"}  ],  config: {    speed: 55,    temperature: 20,    climate: true,    wheels: 19  }}
```

```
describe('test reducer', () => {  it('should handle initial stat', () => {    expect(      appReducer(undefined, {})    ).toEqual(initialState)  })})
```

Exécutez npm test à nouveau et le test réussira.

Dans le cas de test actuel, le type d'action est {}, donc l'**initialState** est retourné.

![Image](https://cdn-media-1.freecodecamp.org/images/SY4N0ajH7uQMJ3X0FiQsWaIrGbrlzWxErc8Z)

Maintenant, testons l'action **CHANGE_CLIMATE**.

Ajoutez les cas de test climateChangeState et CHANGE_CLIMATE suivants à teslaRangeApp.spec.js.

```
const climateChangeState = {  carstats:[    {miles:267, model:"60"},    {miles:273, model:"60D"},    {miles:323, model:"75"},    {miles:334, model:"75D"},    {miles:366, model:"90D"},    {miles:409, model:"P100D"}  ],  config: {    speed: 55,    temperature: 20,    climate: false,    wheels: 19  }}
```

```
it('should handle CHANGE_CLIMATE', () => {    expect(      appReducer(initialState,{        type: 'CHANGE_CLIMATE'      })    ).toEqual(climateChangeState)  })
```

Ensuite, ajoutez le cas **CHANGE_CLIMATE**, **updateStats** et les fonctions **calculateStats** à teslaRangeApp.js. Ensuite, importez **BatteryService.js** qui a été utilisé dans la partie 1.

```
import { getModelData } from '../services/BatteryService';
```

```
function updateStats(state, newState) {  return {    ...state,    config:newState.config,    carstats:calculateStats(newState)  }  }
```

```
function calculateStats(state) {  const models = ['60', '60D', '75', '75D', '90D', 'P100D'];  const dataModels = getModelData();  return models.map(model => {    const { speed, temperature, climate, wheels } = state.config;    const miles = dataModels[model][wheels][climate ? 'on' : 'off'].speed[speed][temperature];    return {      model,      miles    };  });}
```

```
function appReducer(state = initialState, action) {  switch (action.type) {    case 'CHANGE_CLIMATE': {      const newState = {        ...state,        config: {          climate: !state.config.climate,          speed: state.config.speed,          temperature: state.config.temperature,          wheels: state.config.wheels        }      };      return updateStats(state, newState);    }    default:      return state  }}
```

Si vous vérifiez les résultats des tests, vous pouvez voir que les deux cas de test sont réussis.

![Image](https://cdn-media-1.freecodecamp.org/images/lI0QvpPXhWKbgre-ziHBMqQwvFvsDnyjscmz)

Ce que nous avons implémenté jusqu'à présent, c'est que les changements dans l'état qui se produisent lorsque l'utilisateur allume et éteint la climatisation dans l'application via le test runner uniquement du **point de vue de l'Action et du Reducer** sans Redux Store ou View.

![Image](https://cdn-media-1.freecodecamp.org/images/kGJucfa76sLOk319vhcy6FzaAfZJPri80yvx)

![Image](https://cdn-media-1.freecodecamp.org/images/EFjQMINJpaW8G6YpBG4m10FfY-PzeDXj0sW3)

* Consultez [teslaRangeApp.js](https://gist.github.com/gyver98/d0749fe0280f3d471f87305993167b97#file-teslarangeapp-js) tel que nous l'avons écrit jusqu'à présent
* Consultez [teslaRangeApp.spec.js](https://gist.github.com/gyver98/f482176b8c904a9ef1c64becb87b8023#file-teslarangeapp-spec-js)

### 9.3 Créer un Reducer pour les autres

Si vous créez le reste des cas de test en vous référant à la méthode ci-dessus, vous définissez finalement le fichier **teslaRangeApp.js** dans lequel les reducers de toutes les applications sont définis et le **teslaRangeApp.spec.js** pour les tester.

Le code final peut être trouvé à :

* [teslaRangeApp.js](https://gist.github.com/gyver98/2f8c3a8e7652de29c090818f6b7999ea#file-final-teslarangeapp-js)
* [teslaRangeApp.spec.js](https://gist.github.com/gyver98/f18ce2f9d04cf2b762f5ec4c2d0f9418#file-final-teslarangeapp-spec-js)

Après avoir complété le code et les tests, un total de sept cas de test doit réussir.

![Image](https://cdn-media-1.freecodecamp.org/images/VD8dC3EQTrnKQVANDVshPxo3pB8NE75iIu4h)

### 10. Les vues : composants intelligents et stupides

Comme mentionné dans **5. Diviser l'application en conteneurs et composants**, nous allons créer des **composants de présentation** (composants stupides) à des fins de présentation et des **composants conteneurs** (composants intelligents) qui sont des composants enveloppants responsables des actions tout en communiquant avec Redux.

Les composants intelligents sont **responsables des actions**. Si un composant stupide en dessous d'eux doit déclencher une action, le composant intelligent passera une fonction via les props, et le composant stupide pourra alors la traiter comme un **callback**.

Nous avons déjà des composants stupides à des fins de présentation dans la partie 1, et nous les réutiliserons.

Ici, nous créons des composants conteneurs comme enveloppe **supérieure** autour de chaque composant stupide.

### 10.1 La liaison de la couche de vue

Redux a besoin d'aide pour connecter le store à la vue. Il a besoin de quelque chose pour lier les deux ensemble. Cela s'appelle la **liaison de la couche de vue**. Dans une application qui utilise React, c'est `react-redux`.

Techniquement, un composant conteneur est simplement un composant React qui utilise **store.subscribe()** pour lire une partie de l'arbre d'état Redux et fournir des **props** à un composant de présentation qu'il rend.

Par conséquent, nous pouvons créer manuellement des composants conteneurs, mais cela n'est pas recommandé par la documentation officielle de Redux. Cela est dû au fait que **react-redux effectue de nombreuses optimisations de performance** qui sont difficiles à réaliser manuellement.

Pour cette raison, au lieu d'écrire le composant conteneur à la main, nous l'écrivons en utilisant la fonction `connect()` fournie par react-redux.

Installons d'abord les packages nécessaires.

* **npm install --save redux**
* **npm install --save react-redux**

### 10.2 Conteneur TeslaCar

Pour utiliser **connect()**, vous devez définir une fonction spéciale appelée `mapStateToProps`. Cette fonction vous indique **comment convertir l'état actuel du store Redux en props** à passer au composant de présentation.

Le conteneur TeslaCar prend la taille des roues stockée dans le store actuel et la passe en props afin qu'elle puisse être rendue par le composant TeslaCar. Ces props seront mises à jour chaque fois que l'état est mis à jour.

![Image](https://cdn-media-1.freecodecamp.org/images/EVp01AYHe6EToIWZTXAqOb9zaglovdBBsuKp)

Après avoir défini la fonction **mapStateToProps**, nous avons défini la fonction **connect()** comme suit.

```
const TeslaCarContainer = connect(mapStateToProps, null)(TeslaCar)
```

connect() accepte `mapDispatchToProps` comme deuxième argument, qui prend la méthode dispatch du store comme premier argument. Dans le composant TeslaCar, nous n'avons pas besoin d'une action, donc nous devons passer null.

> Une autre parenthèse dans **connect()()** peut sembler étrange. Cette forme signifie en réalité deux appels de fonction, le **premier connect() retourne une autre fonction**, et la **deuxième fonction a besoin que vous passiez un composant React**. Dans ce cas, c'est notre composant TeslaCar. Ce modèle est appelé **currying** ou **application partielle** et est une forme de programmation fonctionnelle.

Créez **src/containers/TeslaCarContainer.js** et écrivez le code.

> Consultez [TeslaCarContainer.js](https://gist.github.com/gyver98/7fa2b19d0bf023200a196ff1ec26f5d5#file-teslarcarcontainer-js)

### 10.3 Conteneur TeslaStats

Comme pour le conteneur TeslaCar, définissez uniquement la fonction **mapStatToProps** et passez-la à connect() dans le conteneur TeslaStats.

![Image](https://cdn-media-1.freecodecamp.org/images/zM276HEMnRULWWykYN35qPjWAbB43dlonzD5)

Créez **src/containers/TeslaStatsContainer.js** et écrivez le code.

> Consultez [TeslaStatsContainer.js](https://gist.github.com/gyver98/065b988b03b0c823f7d8373f2235ec1e#file-teslastatscontainer-js)

### 10.4 Conteneur TeslaSpeedCounter

Le **conteneur TeslaSpeedCounter** définit une fonction supplémentaire `mapDispatchToProps` pour gérer les actions utilisateur qui se produisent dans le composant TeslaSpeedCounter.

![Image](https://cdn-media-1.freecodecamp.org/images/ODhyjWA2nlopJscvPzZHwTemDJWMM4eJ24Lu)

Créez **src/containers/TeslaSpeedCounterContainer.js** et écrivez le code.

> Consultez [TeslaSpeedCounterContainer.js](https://gist.github.com/gyver98/f1758643b7a9f3a5bcae546abda5861d#file-teslaspeedcountercontainer-js)

### 10.5 Conteneur TeslaTempCounter

Le **conteneur TeslaTempCounter** est presque identique au TeslaSpeedCounter, à l'exception de l'état et des créateurs d'action qui sont passés.

![Image](https://cdn-media-1.freecodecamp.org/images/FmQpTPZJMxHyyNLYRyXXqWv9CAU0v5kWxlaT)

Créez **src/containers/TeslaTempCounterContainer.js** et écrivez le code.

> Consultez [TeslaTempCounterContainer.js](https://gist.github.com/gyver98/0986225c521d3213875a9849bf1e9d80#file-teslatempcountercontainer-js)

### 10.6 TeslaClimateContainer

![Image](https://cdn-media-1.freecodecamp.org/images/5t-ueAA8-AS6Q1F9r2qQiMjrlJ7WwVB8mLRD)

Créez **src/containers/TeslaClimateContainer.js** et écrivez le code.

> Consultez [TeslaClimateContainer](https://gist.github.com/gyver98/bd677915a8b4ea68589497311c77eaee#file-teslaclimatecontainer-js)

### 10.7 TeslaWheelsContainer

![Image](https://cdn-media-1.freecodecamp.org/images/T-n-gUS0W7XxZ0ge0DT29ZD8wiES6rGWRHnE)

Créez **src/containers/TeslaWheelsContainer.js** et écrivez le code.

> Consultez [TeslaWheelsContainer.js](https://gist.github.com/gyver98/2bc410b7c7aa07ac4def49702ba21738#file-teslawheelscontainer-js)

Nous avons créé les composants conteneurs correspondant aux composants de présentation générés [dans la partie 1](https://medium.freecodecamp.com/building-teslas-battery-range-calculator-with-react-part-1-2cb7abd8c1ee) via connect() de react-redux.

### 11. Provider

Assemblons tout ce que nous avons fait jusqu'à présent et faisons fonctionner nos applications. Jusqu'à présent, nous avons défini des **objets d'action** et créé des **créateurs d'action** qui créent des objets d'action. Et lorsqu'une action se produit, nous avons créé des **reducers** qui traitent et retournent un nouvel état. Nous avons ensuite créé un **composant conteneur** qui connecte chacun des composants de présentation au store Redux.

Maintenant, chaque composant conteneur a besoin d'un moyen d'accéder au store, c'est ce que fait le `Provider`. Le composant Provider **enveloppe toute l'application et permet aux sous-composants de communiquer avec le store via connect()**.

Le composant de haut niveau de notre application, **App.js**, ressemble à ceci :

> Consultez [App.js](https://gist.github.com/gyver98/46b3929798503d057bf23e64a72c2011#file-app-js)

![Image](https://cdn-media-1.freecodecamp.org/images/ca1XBqUditLLYVAU33ud9lXLpBcK4std6WNz)
_bouclier du Provider_

### 12. Comment tout cela fonctionne ensemble

Enfin, toutes les pièces du puzzle ont été complétées. Maintenant, regardons l'animation suivante comme exemple lorsque toutes les pièces du puzzle sont liées ensemble et que l'utilisateur déclenche l'événement **speed up**.

![Image](https://cdn-media-1.freecodecamp.org/images/hgaIFhmOJXpOGY2bIpvh2fhpJ-V7RKLol2Qg)

Maintenant, exécutez **npm start** et il sera compilé normalement et l'application sera démarrée.

Mais il reste encore quelques choses à faire.

* Tout d'abord, copiez tout le contenu de **/containers/TeslaBattery.css** que vous avez créé dans la partie 1 et ajoutez-les à **App.css**.

> Consultez [App.css](https://gist.github.com/gyver98/fb061ac3997b055bf4628dcfdd83cb51#file-app-css)

* Ensuite, ouvrez **/components/TeslaCounter/TeslaCounter.js** et modifiez le gestionnaire d'événements **onClick** comme suit : Cela est dû au fait que la partie 2 ne gère plus la gestion des événements dans **TeslaBattery.js**.

```
onClick={(e) => props.increment(e, props.initValues.title)}-->onClick={(e) => {  e.preventDefault();  props.increment(props.currentValue)}}
```

```
onClick={(e) => props.decrement(e, props.initValues.title)}-->onClick={(e) => {  e.preventDefault();  props.decrement(props.currentValue)}}
```

* Ensuite, n'utilisons pas les props de manière répétée en utilisant la destructuration d'objets ES6.

```
const TeslaCounter = (props) => (  <p className="tesla-counter__title">{props.initValues.title}</p>  ...
```

```
-->const TeslaCounter = ({ initValues, currentValue, increment, decrement }) => (  <p className="tesla-counter__title">{initValues.title}</p>  ...
```

> Consultez [TeslaCounter.js](https://gist.github.com/gyver98/5c7f4755023643a84dc7514209f22997#file-teslacounter-js)

Enfin, notre **version Redux de l'application Tesla Battery Range Calculator** est complète !

### 13. Une chose de plus : Redux Dev Tools

L'outil **Redux Dev Tool** facilite grandement le suivi de l'état Redux et tire parti de fonctionnalités intéressantes comme le débogage de voyage dans le temps.

Nous allons l'installer sur Chrome ici.

* Extension Chrome [installation](https://www.google.com.au/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwijoqLQxdzSAhUEspQKHaEDA0AQFggZMAA&url=https%3A%2F%2Fchrome.google.com%2Fwebstore%2Fdetail%2Fredux-devtools%2Flmhkpmbekcpmknklioeibfkpmmfibljd%3Fhl%3Den&usg=AFQjCNFg4ldS78uapjCGBaNjL9NvIwZGhg&sig2=YuyPlshxe2eVaKrx0ReXfQ&bvm=bv.149760088,d.dGo)
* Ajoutez pour le store Redux

Ouvrez le fichier **App.js** et modifiez la partie **createStore** comme suit :

```
const store = createStore(appReducer);-->const store = createStore(appReducer, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());
```

* Vérifiez sur le navigateur

![Image](https://cdn-media-1.freecodecamp.org/images/rLCepIN4D6N0hkL1RprcWPGOjWbUfyTcUjk5)

### Avant de passer à la partie suivante :

* Consultez le [code final du projet](https://github.com/gyver98/redux-tesla-battery-range-calculator-tutorial)
* Consultez la [démonstration en direct](http://redux-tesla-charge-calculator.surge.sh/)

### Ressources supplémentaires :

* [Documentation Redux](http://redux.js.org/docs/introduction/)
* [Une introduction en cartoon à Redux](https://code-cartoons.com/a-cartoon-intro-to-redux-3afb775501a6#.4j7d5vz4l)
* [Monter de niveau avec React : Redux](https://css-tricks.com/learning-react-redux/)
* [Commencer avec Redux](https://egghead.io/courses/getting-started-with-redux)