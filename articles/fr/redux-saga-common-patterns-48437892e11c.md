---
title: Cette collection de motifs courants de Redux-saga vous facilitera la vie.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-24T21:53:45.000Z'
originalURL: https://freecodecamp.org/news/redux-saga-common-patterns-48437892e11c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2o7NrAj_0G63BKySac_XuA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Cette collection de motifs courants de Redux-saga vous facilitera la vie.
seo_desc: 'By Andrés Mijares

  This is a 2-part series — feel free to check out the first part here.

  I’ve been a redux-saga user for a year now, and I still remember when I was introduced
  to the library. I remember how amazed I was (that ‘Eureka’ moment!) when I ...'
---

Par Andrés Mijares

**Il s'agit d'une série en 2 parties — n'hésitez pas à consulter la première partie [ici](https://medium.freecodecamp.org/async-operations-using-redux-saga-2ba02ae077b3).**

J'utilise Redux-saga depuis un an maintenant, et je me souviens encore du moment où j'ai été introduit à cette bibliothèque. Je me souviens à quel point j'étais émerveillé (ce moment « Eurêka » !) lorsque j'ai résolu quelques problèmes en quelques heures.

C'était si bien que j'ai eu besoin de partager toute cette génialité avec d'autres personnes — alors je me suis assis et j'ai écrit un [article](https://medium.freecodecamp.org/async-operations-using-redux-saga-2ba02ae077b3) à ce sujet. Depuis ce jour, en raison de [la malédiction de la connaissance](https://en.wikipedia.org/wiki/Curse_of_knowledge), je ne peux plus imaginer ma vie sans.

C'était si bien que maintenant je l'utilise également comme couche d'orchestration pour gérer toutes les opérations asynchrones au travail chez [Shiftgig](http://www.shiftgig.com). Donc oui, ces lignes de code aident à soutenir les opérations quotidiennes de plusieurs millions d'entreprises de capital-risque — une grande partie de notre architecture d'application repose sur cela.

Si vous êtes intéressé par cela, [cet autre](https://medium.com/shiftgig-blog/agile-front-end-architectures-with-react-redux-and-vanilla-js-23f4e5626e01) article peut vous orienter dans cette direction.

**Une note à part :** Si votre entreprise s'appuie fortement sur cela ou sur tout autre projet open source, je vous encourage vivement (vous et votre employeur) à devenir un [soutien du projet](https://opencollective.com/redux-saga#contributors). Cette petite donation peut faire une grande différence, et c'est une belle façon de faire du bon karma. ??.

### Assez avec l'introduction émotive — voyons les motifs.

Cet article suppose que vous avez une compréhension de base de la bibliothèque. Si vous avez besoin de plus d'informations sur la façon d'enregistrer une saga, ou même sur la configuration, veuillez vous référer à la première partie de la série [ici](https://medium.freecodecamp.org/async-operations-using-redux-saga-2ba02ae077b3).

Après un an de travail avec la bibliothèque et de résolution de problèmes, nous avons identifié quelques motifs que nous avons répétés encore et encore. Voyons-les un par un avec un cas d'utilisation possible pour chacun.

Avis de non-responsabilité : J'ai utilisé les noms que je connais pour ceux-ci. Mais si vous les connaissez par des noms officiels, veuillez commenter ci-dessous.

### Take et Fork

Par définition, le plus courant de ma liste. Vous vous souvenez de l'ancienne méthode lorsque vous placiez un écouteur et des observateurs partout dans votre application Angular 1 ? Eh bien, je m'en souviens un peu… ?.

Ce motif est principalement utilisé pour déclencher un processus après qu'une action est dispatchée — oui ! Comme un écouteur :

```
/* c'est la saga que vous allez enregistrer */export function* aListenerOnlySaga() {  const somePossibleData = yield take('SOME_ACTION')  yield fork(someOtherSagaProcess)}
```

```
function* someOtherSagaProcess() {    /* Tout calcul de processus dont vous avez besoin */}
```

#### Le cas d'utilisation

Il y en a beaucoup… mais restons réalistes. Dans notre application, nous devons supporter différentes branches/états qui sont nécessaires pour afficher des informations et prendre des actions basées sur la sélection actuelle.

Si je suis Martha, une secrétaire de 45 ans qui n'aime pas la technologie, je dois pouvoir sélectionner une branche dans une liste déroulante et, par magie, interroger les informations qui s'y rapportent.

```
/* Un composant React laid */class CompanyDropDown extends React.Component {   state = {      company: null,       branches: [],   }   componentDidUpdate ({company, branches}) {     this.setState(({company}) => ({company, branches}))   }   onChangeCompany (company) {      this.props.dispatch('company_change', company)   }   render () { /* omis pour plus de commodité */}}
```

```
const mapStateToProps = ({company, branches}) => ({company, branches})
```

```
export connect(mapStateToProps)(CompanyDropDown)
```

Certains détails, comme la méthode de rendu et les réducteurs, seront omis pour aller directement au but.

```
/* quelque part dans votre code... */export function* listenForChangeCompany() {   /* cette variable contient l'argument passé */   const company = yield take('company_change')   yield fork(changeCompanySaga, company)}
```

```
function* changeCompanySaga(company) {   const branchesPerCompany = yield call(getBranchesByCompany, company)   yield put({     type: 'company_change_success',     payload: branchesPerCompany,   })}
```

Maintenant, notre interface utilisateur est séparée de notre logique métier, et nous sommes heureux. Nous ajouterons plus de complexité à cela plus tard.

Le principal avantage de cela est que vous pouvez créer un catalogue de processus (plus à ce sujet plus tard) qui isole cette fonctionnalité spécifique et l'expose à votre équipe à votre discrétion.

Mais il y a un petit problème avec ce motif. Si vous l'avez remarqué, **cela ne fonctionnera qu'une seule fois.** Après avoir exécuté le processus, il ne fonctionnera plus. C'est là que le motif suivant devient utile.

### Watch et Fork

L'un des problèmes avec le motif Take et Fork est que nous limitons le nombre d'exécutions à une seule. Comme vous pouvez le voir, ce cas d'utilisation précédent ne correspond probablement pas à l'utilisation du motif. Je l'ai fait exprès, afin que nous puissions continuer à l'améliorer et à le renforcer autant que nous en avons besoin, étape par étape.

Un cas mieux adapté à l'objectif serait probablement un processus de connexion ou de déconnexion, où vous savez que vous n'en avez besoin qu'une seule fois.

En continuant avec le cas, nous devons nous assurer que notre amie Martha peut changer d'entreprise autant de fois qu'elle en a besoin, et pas seulement une fois. Nous pouvons résoudre cela avec un petit ajustement. Voyons le motif watch et fork en place, et ramenons notre saga d'écoute dans le jeu.

```
export function* listenForChangeCompany() {   while (true) {      const company = yield take('company_change')      yield fork(changeCompanySaga, company)   } } /* eh voilà ! */
```

Assez élégant, n'est-ce pas ? Si vous n'êtes pas habitué aux générateurs de fonctions, avoir un while/true autour semble probablement étrange. Mais cela remplit son objectif. Pourtant, il y a une manière encore meilleure de le faire : nous pouvons itérer davantage sur cela en utilisant un autre raccourci d'aide de bibliothèque.

```
/* Où vous enregistrez les sagas */function* rootSagas () {   yield [    takeEvery('company_change', changeCompanySaga)   ]}
```

En coulisses, l'argument company est passé à la saga changeCompanySaga. J'aime vraiment ce motif, surtout si vous devez gérer une grande application avec des centaines de processus. Vous savez simplement qu'il répond à une seule action dispatchée.

### Put et Take

Ce motif est très utile. Comme je l'ai mentionné précédemment, vous organisez vos opérations de processus en différentes sagas. Vous créez ensuite un catalogue de services que vous pouvez partager avec toutes les équipes/personnes/unités que vous nommez. Cela signifie que chacun de vos services a une fonctionnalité finie qui changera votre état. Parfois, cela suffit, tandis que d'autres fois, vous souhaitez étendre la capacité d'un seul service. Voyons un cas d'utilisation.

Imaginez qu'une des équipes de votre entreprise vous dise qu'elles ont créé ce service très complexe que vous pouvez réutiliser. Il s'appelle... `fetchDataOverFiveDifferentLocations`. C'est beaucoup de choses impératives, mais à la fin, vous aurez toutes les informations dont vous avez besoin analysées et prêtes à être consommées. Génial !

Vous et votre équipe avez convenu de certaines conventions de nommage qui se présentent comme suit : {service_name}_{microservice}_{status}. Donc, disons :

* **fetchSomeData_events** Cela démarrera la saga.
* **fetchSomeData_events_start** Cette action est dispatchée par le service dès qu'il commence.
* **fetchSomeData_events_success** Cette action est dispatchée par le service lorsqu'il se termine.
* **fetchSomeData_events_error** Cette action est dispatchée s'il y a une erreur pendant le processus.

Cela signifie que notre bibliothèque de services expose une saga qui ressemble à ceci :

```
export function* fetchDataOverFiveDifferentLocations() {    while (true) {        yield put({type: 'fetchSomeData_events_start'})       /*         calcul de choses...       */       yield put({type: 'fetchSomeData_events_success'})     }}
```

Dans votre application, vous pouvez consommer le service comme ceci :

```
function* rootSagas () {   yield [    takeEvery('fetchSomeData_events', fetchDataOverFiveDifferentLocations)   ]}
```

Et si nous devons étendre cette fonctionnalité ?

```
/* Nous créons une saga de gestion */function* fetchDataManager () {   /* nous devons démarrer le service/saga */   yield put({type: 'fetchSomeData_events'})   /* nous devons attendre/écouter quand il se termine...*/   yield take('fetchSomeData_events_success')   /*      fork un autre processus,     interroger des infos depuis l'état,     faire des choses impératives,     tout ce que vous devez faire quand la saga précédente se termine, le ciel est la limite...    */}
```

```
/* Nous créons une saga d'orchestration */function* orchestratorSaga () {   while (true) {    yield fork(fetchDataManager)   }}
```

```
/* votre saga racine ressemble alors à ceci */function* rootSagas () {   yield [    takeEvery('other_action_trigger', orchestratorSaga),   ]}
```

Probablement, certains d'entre vous pensent… qu'en est-il de la gestion des erreurs ? Gardez vos pensées, j'y reviendrai plus tard.

### For/of Collection

Celui-ci est pointilleux, car la plupart du temps nous ne résolvons pas le problème de cette manière par défaut. Mais quand vous en avez besoin, vous en avez besoin.

Disons que nous récupérons une collection depuis n'importe quelle source. Nous recevons 100 objets et nous devons appliquer une opération/service à chacun. En d'autres termes, nous devons dispatcher une ou plusieurs actions pour chaque élément. Normalement, c'est quelque chose que vous pouvez gérer dans un réducteur, mais gardons l'esprit du catalogue de services.

Le problème est que lorsque vous êtes dans une saga, vous ne pouvez pas faire quelque chose comme :

```
function* someSagaName() {   /* code omis pour plus de commodité */   const events = yield call(fetchEvents)   events.map((event) => {      /* ceci est syntaxiquement invalide */      yield put({type: 'some_action', payload: event})   })}
```

C'est là que la boucle for/of vient à la rescousse. Résolvons ce problème avant de commencer à briser nos règles de services architecturaux ??.

```
function* someSagaName() {   /* code omis pour plus de commodité */   const events = yield call(fetchEvents)   for (event of events) {     yield put({type: 'some_action', payload: event}) /* ?? */     /* ou peut-être quelque chose comme : */     yield fork(someOtherSagaOrService, event) /* ?? */   }}  
```

Le fonctionnement de la boucle for/of dépasse le cadre de cet article, mais vous pouvez en savoir plus [ici](https://developer.mozilla.org/en/docs/Web/JavaScript/Reference/Statements/for...of). De plus, il est possible de le faire en utilisant une boucle for régulière et en itérant sur le tableau — c'est à vous de choisir.

### Gestion des erreurs

Oh oui ! JavaScript n'est pas Elixir, donc nous devons toujours faire de la programmation défensive et nous protéger contre les erreurs. ??‍? Basé sur cette structure de catalogue, comment pouvons-nous nous assurer de ne pas avaler les erreurs ? Ou comment chaque erreur peut-elle être gérée correctement ? Une erreur 500 n'est pas la même qu'une erreur 401, donc nous avons toujours besoin d'une manière flexible de communiquer à l'utilisateur de manière conviviale que quelque chose s'est mal passé.

Les règles de base que nous utilisons sont simples :

* **Toutes** les erreurs sont gérées à l'intérieur des sagas.
* **La saga qui gère** le processus est responsable de la gestion de l'erreur.

Revenons à notre service de gestion d'événements :

1. Ce service est générique.
2. Si le service gère l'erreur, nous ne pouvons pas faire une erreur personnalisée. Nous sommes simplement couplés à l'erreur conventionnelle.
3. Si nous devons faire un gestionnaire personnalisé, nous devons créer un service qui gère l'erreur.

```
/* Cas 1, service qui gère l'erreur */export function* fetchDataOverFiveDifferentLocations() {    try {      while (true) {          yield put({type: 'fetchSomeData_events_start'})         /*           calcul de choses...         */         yield put({type: 'fetchSomeData_events_success'})       }    } catch (error) {      yield put({type: 'fetchSomeData_events_error', error})    }}
```

Dans ce cas, nous sommes couplés à l'erreur du service, donc nous devons créer un service qui écoute cette action :

```
function* rootSagas () {  yield [   takeEvery('fetchSomeData_events_error', yourErrorHandlerService),   /* ... */,     ]}
```

Le seul inconvénient que j'ai trouvé jusqu'à présent est la verbosité de la gestion d'une seule erreur. Mais cela vous donne aussi beaucoup de flexibilité, puisque vous décidez dans vos réducteurs si vous voulez réagir à cette erreur ou non. L'important est qu'elle a été capturée et que votre application est notifiée.

```
/* Cas 2, le gestionnaire s'occupe de l'erreur */function* fetchDataOverFiveDifferentLocations() {  while (true) {     yield put({type: 'fetchSomeData_events_start'})         /*           calcul de choses...         */    yield put({type: 'fetchSomeData_events_success'})   }}
```

```
function* fetchDataManager () {  try {     yield put('fetchSomeData_events')     /*...*/     yield take('fetchSomeData_success')  } catch (error) {    yield put('some_custom_error_action', error)  }}
```

Vous pouvez ensuite gérer l'erreur, par exemple, via un réducteur. C'est probablement un booléen. C'est à vous de décider en fonction de ce dont vous avez besoin — les deux méthodes fonctionnent vraiment bien. Cela dépendra de vos cas et de vos accords avec l'équipe. Souvenez-vous : **la convention plutôt que la configuration** est la clé.

### Conclusion

Comme vous pouvez le voir, cette bibliothèque est vraiment utile lorsque vous avez besoin d'une manière solide de partager des pratiques architecturales entre les équipes, ou peut-être lorsque vous devez créer une couche de service très descriptive. Le plus important de tout, c'est qu'il est vraiment facile de l'étendre aux autres.

Utilisez-vous d'autres motifs ? Je suis toujours heureux d'apprendre ce que les autres font et comment nous pouvons apprendre les uns des autres. Faites-moi savoir !

Enfin, n'hésitez pas à consulter mes projets open source pour le moment :

* [**React Calendar Multiday**](https://github.com/andresmijares/react-calendar-multiday)

[**the mediocre engineer**](https://www.youtube.com/channel/UCSBzbeNuDamKpX6N4Q5SaHA)  
[_Pour plus de contenu comme celui-ci, veuillez envisager de vous abonner à ma chaîne www.youtube.com_](https://www.youtube.com/channel/UCSBzbeNuDamKpX6N4Q5SaHA)