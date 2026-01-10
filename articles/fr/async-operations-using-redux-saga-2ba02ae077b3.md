---
title: Opérations asynchrones avec redux-saga
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-09T14:09:37.000Z'
originalURL: https://freecodecamp.org/news/async-operations-using-redux-saga-2ba02ae077b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gbEYdLgV3eZ-tuqYlMeUhQ.png
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
seo_title: Opérations asynchrones avec redux-saga
seo_desc: 'By Andrés Mijares

  UPDATE August/2017:


  I published a second part of this article, Redux-saga common patterns


  UPDATE April/2017:


  Thanks Eduardo for translating this article to Portuguese, find it here.

  Also this unknown guy for translating this arti...'
---

Par Andrés Mijares

**MISE À JOUR Août/2017 :**

* J'ai publié une deuxième partie de cet article, [Redux-saga common patterns](https://medium.com/shiftgig-blog/redux-saga-common-patterns-48437892e11c)

**MISE À JOUR Avril/2017 :**

* Merci à [Eduardo](https://medium.com/@oieduardorabelo) pour avoir traduit cet article en **portugais**, [le trouver ici](https://medium.com/@oieduardorabelo/redux-saga-voc%C3%AA-no-controle-das-opera%C3%A7%C3%B5es-ass%C3%ADncronas-71c9e6b3aabc).
* Merci également à cet inconnu pour avoir traduit cet article en **chinois**, [le trouver ici](http://www.jianshu.com/p/ea1647712df0).

Il y a quelques jours, mon collègue a donné une conférence sur la gestion des opérations asynchrones. Il utilisait plusieurs outils pour étendre les capacités de Redux. L'écouter a vraiment mis en lumière les réalités de la [Fatigue JavaScript](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4#.1ol2mk46u).

Admettons-le : si vous êtes habitué à faire votre travail et à utiliser des technologies basées sur vos besoins — et non pour la technologie elle-même — configurer un écosystème React peut s'avérer frustrant et chronophage.

J'ai passé les deux dernières années à travailler sur des projets Angular et à profiter de l'état de l'art du modèle Model-View-Controller. Et je dois dire que — même si la courbe d'apprentissage était un problème venant d'un background Backbone.js — apprendre Angular a vraiment porté ses fruits. J'ai obtenu un meilleur emploi, et j'ai également eu l'occasion de collaborer sur des projets intéressants. J'ai beaucoup appris de la communauté supportive d'Angular.

C'étaient des jours vraiment cool, mais, eh bien, *La Fatigue Doit Continuer* (marque déposée en attente), et je passe à la mode : React, Redux, et Sagas.

Il y a quelques années, je suis tombé sur un article intitulé [Flattening Promise Chains](http://solutionoptimist.com/2013/12/27/javascript-promise-chains-2/) par [Thomas Burleson](https://twitter.com/thomasburleson). J'ai beaucoup appris en le lisant. Même deux ans plus tard, je me souviens encore de beaucoup de ces idées.

Ces jours-ci, je migre vers React et j'ai trouvé beaucoup de puissance dans Redux et l'utilisation de sagas pour gérer les opérations asynchrones. Je vais donc écrire ceci pour m'inspirer de l'article de Thomas et créer une approche similaire en utilisant [redux-saga](https://github.com/yelouafi/redux-saga). J'espère que cela rendra la pareille à l'univers et aidera certaines personnes à comprendre comment ces technologies importantes fonctionnent.

*Avertissement : Je vais travailler avec le même scénario et l'étendre, j'espère (si j'ai de la chance) créer une discussion sur les deux approches. Je vais supposer que le lecteur a une compréhension de base des Promesses, React, Redux et (oh !)... JavaScript.*

### D'abord les bases.

Selon [Yassine Elouafi](https://twitter.com/yassineelouafi2), créateur de redux-saga :

> redux-saga est une bibliothèque qui vise à rendre les effets secondaires (c'est-à-dire les choses asynchrones comme la récupération de données et les choses impures comme l'accès au cache du navigateur) dans les applications React/Redux plus faciles et meilleures.

En gros, une bibliothèque d'assistance qui nous permet d'organiser toutes les opérations asynchrones et distribuées basées sur les Sagas et les Générateurs de Fonctions ES6. Si vous voulez en savoir plus sur le modèle Saga lui-même, [Caitie McCaffrey](https://twitter.com/caitie?lang=en) a fait un excellent travail dans cette [vidéo](https://www.youtube.com/watch?v=xDuwrtwYHu8) et plus sur les Générateurs de Fonctions. Vérifiez cette vidéo gratuite d'Egghead [vidéo](https://egghead.io/lessons/ecmascript-6-generators) (au moins elle était gratuite lorsque j'ai posté cet article).

### Le cas du tableau de bord de vol

Thomas a établi un cas que nous allons recréer. Le code final est [ici](https://github.com/andresmijares/async-redux-saga), et la démo est [ici](http://async-redux-saga.surge.sh/).

Le scénario se présente comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/0HvwzuUjccxemGZ1MxcNI1D5tua1WyBflMDQ)
_Image par Thomas Burleson_

Comme nous pouvons le voir, une séquence de trois appels d'API : getDeparture -> getFlight -> getForecast, donc notre classe de service API ressemble à ceci :

```
class TravelServiceApi {
```

```
 static getUser() {   return new Promise((resolve) => {     setTimeout(() => {       resolve({            email : "somemockemail@email.com",            repository: "http://github.com/username"       });     }, 3000);   }); }
```

```
 static getDeparture(user) {  return new Promise((resolve) => {   setTimeout(() => {    resolve({      userID : user.email,      flightID : "AR1973",      date : "10/27/2016 16:00PM"     });    }, 2500);   }); }
```

```
 static getForecast(date) {  return new Promise((resolve) => {      setTimeout(() => {        resolve({            date: date,            forecast: "rain"        });      }, 2000);   });  }
```

```
}
```

Il s'agit d'une API directe avec certaines informations simulées qui nous permettront de définir le scénario. Tout d'abord, nous devons avoir un utilisateur. Ensuite, avec ces informations, nous obtiendrons le départ, le vol et la prévision afin de créer plusieurs panneaux de tableau de bord peu esthétiques, qui ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/or52I8TAFakZasKjYCaiW8FBxgTInoCEeMfw)

Les composants React peuvent être trouvés [ici](https://github.com/andresmijares/async-redux-saga/blob/master/src/components/Dashboard.js). Ce sont trois composants différents avec une représentation dans le magasin redux donnée par trois réducteurs, qui ressemblent à ceci :

```
const dashboard = (state = {}, action) => { switch(action.type) {  case 'FETCH_DASHBOARD_SUCCESS':  return Object.assign({}, state, action.payload);  default :  return state; }};
```

Nous utilisons un réducteur différent pour chaque panneau, avec trois scénarios différents, qui donnent au composant l'accès à la partie de l'utilisateur en utilisant la fonction redux _StateToProps_ :

```
const mapStateToProps =(state) => ({ user : state.user, dashboard : state.dashboard});
```

Après que tout soit configuré (oui, je sais que je n'ai pas expliqué beaucoup de choses, mais je veux me concentrer uniquement sur les sagas...), nous sommes prêts à jouer !

### Montrez-moi les Sagas

William Deming a dit un jour :

> Si vous ne pouvez pas décrire ce que vous faites comme un processus, alors vous ne savez pas ce que vous faites.

D'accord, créons un processus étape par étape de comment travailler avec Redux Saga.

#### 1. Enregistrer les Sagas

J'utiliserai mes propres mots pour décrire quelles méthodes sont exposées par l'API. Si vous avez besoin de plus de détails techniques, n'hésitez pas à vous référer à la documentation [ici](https://yelouafi.github.io/redux-saga/docs/api/index.html).

Tout d'abord, nous devons créer notre générateur de saga et les enregistrer :

```
function* rootSaga() {  yield[    fork(loadUser),    takeLatest('LOAD_DASHBOARD', loadDashboardSequenced)  ];}
```

Redux saga expose plusieurs méthodes appelées **_Effets_**, nous allons en définir plusieurs :

* **Fork** effectue une opération non bloquante sur la fonction passée.
* **Take** pause jusqu'à ce que l'action soit reçue.
* **Race** exécute les effets simultanément, puis les annule tous une fois qu'un est terminé.
* **Call** exécute une fonction. Si elle retourne une promesse, pause la saga jusqu'à ce que la promesse soit résolue.
* **Put** envoie une action.
* **Select** Exécute une fonction de sélection pour obtenir des données de l'état
* **takeLatest** signifie que nous allons exécuter les opérations, puis retourner uniquement les résultats du dernier appel. Si nous déclenchons plusieurs cas, il va ignorer tous sauf le dernier.
* **takeEvery** retournera les résultats pour tous les appels déclenchés.

Nous venons d'enregistrer deux sagas différentes. Nous allons les définir plus tard. Pour l'instant, nous prenons une pour l'utilisateur en utilisant **fork** et une autre **takeLatest**, qui attendra qu'une action appelée "**LOAD_DASHBOARD**" soit exécutée. Plus d'informations à l'étape 3.

#### 2. Injecter le Middleware Saga dans le magasin Redux.

Lorsque nous définissons le magasin Redux et l'initialisons, la plupart du temps, il ressemblera à ceci :

```
const sagaMiddleware = createSagaMiddleware();const store = createStore(rootReducer, [], compose(      applyMiddleware(sagaMiddleware)  );sagaMiddleware.run(rootSaga); /* injecter nos sagas dans le middleware*/
```

#### 3. Créer les Sagas.

Tout d'abord, nous allons définir la séquence de la Saga **loadUser** :

```
function* loadUser() {  try {   //1ère étape    const user = yield call(getUser);   //2ème étape    yield put({type: 'FETCH_USER_SUCCESS', payload: user});
```

```
  } catch(error) {    yield put({type: 'FETCH_FAILED', error});  }}
```

Nous pouvons le lire comme suit :

* Tout d'abord, appelez une fonction appelée **getUser**, et attribuez le résultat à la const **user**.
* Plus tard, envoyez une action appelée **FETCH_USER_SUCCESS** et passez la valeur de **user** pour être consommée par le magasin.
* Si quelque chose ne va pas, envoyez une action appelée **FETCH_FAILED**.

Comme vous pouvez le voir, c'est vraiment cool que nous puissions ajouter le résultat d'une opération yield à une variable.

Maintenant, nous allons créer la saga séquencée :

```
function* loadDashboardSequenced() {
```

```
 try {    yield take('FETCH_USER_SUCCESS');
```

```
  const user = yield select(state => state.user);    const departure = yield call(loadDeparture, user);
```

```
  const flight = yield call(loadFlight, departure.flightID);
```

```
  const forecast = yield call(loadForecast, departure.date);
```

```
  yield put({type: 'FETCH_DASHBOARD_SUCCESS', payload: {forecast,  flight, departure} });
```

```
  } catch(error) {    yield put({type: 'FETCH_FAILED', error: error.message});  }
```

```
}
```

Nous pouvons lire la saga comme suit :

* Attendez que l'action **FETCH_USER_SUCCESS** soit envoyée. Cela sera essentiellement en attente jusqu'à ce qu'un événement la déclenche. Nous utilisons l'effet **take** pour cela.
* Nous prenons une valeur du magasin. L'effet **select** reçoit une fonction qui a accès au magasin. Nous attribuons les informations de l'utilisateur à la constante user.
* Nous exécutons une opération asynchrone pour charger les informations de départ, et passons l'utilisateur comme paramètre en utilisant l'effet **call**.
* Après que **loadDeparture** soit terminé, nous exécutons **loadFlight** avec l'objet departure récupéré dans l'opération précédente.
* Il en sera de même pour la prévision, nous devons attendre que le vol soit chargé pour exécuter l'effet **call** suivant.
* Enfin, une fois toutes les opérations terminées, nous utilisons l'effet **put** pour envoyer une action au magasin et envoyer tous les arguments en utilisant les informations chargées pendant toute la saga.

Comme vous pouvez le voir, une saga est une collection d'étapes qui attendent des actions précédentes pour modifier leurs comportements. Une fois terminées, toutes les informations sont prêtes à être consommées dans le magasin.

Plutôt bien, hein ?

Maintenant, vérifions un cas différent. Considérons que **getFlight** et **getForecast** peuvent être déclenchés en même temps. Ils n'ont pas besoin que l'un se termine pour que l'autre commence, nous pouvons donc créer un panneau différent pour ce cas.

![Image](https://cdn-media-1.freecodecamp.org/images/uH5fIjkHsv66XHL1ZDxMD-EuO1Ld1FjBRG3D)
_Image par Thomas Burleson_

#### Saga non bloquante

Pour exécuter deux opérations non bloquantes, nous devons apporter une petite modification à notre saga précédente :

```
function* loadDashboardNonSequenced() {  try {    //Attendre que l'utilisateur soit chargé    yield take('FETCH_USER_SUCCESS');
```

```
    //Prendre les informations de l'utilisateur du magasin    const user = yield select(getUserFromState);
```

```
    //Obtenir les informations de départ    const departure = yield call(loadDeparture, user);
```

```
    //C'est là que la magie opère    const [flight, forecast] = yield [call(loadFlight, departure.flightID), call(loadForecast, departure.date)];
```

```
    //Dire au magasin que nous sommes prêts à être affichés    yield put({type: 'FETCH_DASHBOARD2_SUCCESS', payload: {departure, flight, forecast}});
```

```
} catch(error) {    yield put({type: 'FETCH_FAILED', error: error.message});  }}
```

Nous devons enregistrer le yield comme un tableau :

```
const [flight, forecast] = yield [call(loadFlight, departure.flightID), call(loadForecast, departure.date)];
```

Ainsi, les deux opérations sont appelées en parallèle, mais à la fin de la journée, nous attendrons que les deux se terminent pour mettre à jour l'UI si nécessaire.

Ensuite, nous devons enregistrer la saga dans la rootSaga :

```
function* rootSaga() {  yield[    fork(loadUser),    takeLatest('LOAD_DASHBOARD', loadDashboardSequenced),    takeLatest('LOAD_DASHBOARD2', loadDashboardNonSequenced)
```

```
  ];}
```

Et si nous devons mettre à jour l'UI dès qu'une opération est terminée ?

Ne vous inquiétez pas — je vous couvre.

#### **Sagas non séquencées et non bloquantes**

Nous pouvons également isoler nos sagas et les combiner, ce qui signifie qu'elles peuvent fonctionner indépendamment. C'est exactement ce dont nous avons besoin. Jetons un coup d'œil.

**Étape #1** : Nous isolons la Saga Forecast et la Saga Flight. Elles dépendent toutes deux de departure.

```
/* **************Flight Saga************** */function* isolatedFlight() {  try {    /* departure prendra la valeur de l'objet passé par le put*/    const departure = yield take('FETCH_DEPARTURE3_SUCCESS');     const flight = yield call(loadFlight, departure.flightID);     yield put({type: 'FETCH_DASHBOARD3_SUCCESS', payload: {flight}});
```

```
  } catch (error) {    yield put({type: 'FETCH_FAILED', error: error.message});  }}
```

```
/* **************Forecast Saga************** */function* isolatedForecast() {    try {      /* departure prendra la valeur de l'objet passé par le put*/     const departure = yield take('FETCH_DEPARTURE3_SUCCESS');
```

```
     const forecast = yield call(loadForecast, departure.date);          yield put({type: 'FETCH_DASHBOARD3_SUCCESS', payload: { forecast, }});
```

```
} catch(error) {      yield put({type: 'FETCH_FAILED', error: error.message});    }}
```

Remarquez quelque chose de très important ici ? C'est ainsi que nous architecturons nos sagas :

* Elles attendent toutes deux le même **Événement d'Action** (FETCH_DEPARTURE3_SUCCESS) pour commencer.
* Elles recevront une valeur lorsque cet événement sera déclenché. Plus de détails à ce sujet à l'étape suivante.
* Elles exécuteront leur opération asynchrone en utilisant l'**Effet Call** et déclencheront toutes deux le même événement après achèvement. Mais elles envoient toutes deux des données différentes au magasin. Grâce à la puissance de Redux, nous pouvons faire cela sans aucune modification de notre réducteur.

**Étape #2** : Apportons les modifications à la séquence de départ et assurons-nous qu'elle envoie une valeur de départ avec deux autres sagas :

```
function* loadDashboardNonSequencedNonBlocking() {  try {    //Attendre que l'action commence    yield take('FETCH_USER_SUCCESS');
```

```
    //Prendre les informations de l'utilisateur du magasin    const user = yield select(getUserFromState);
```

```
    //Obtenir les informations de départ    const departure = yield call(loadDeparture, user);
```

```
    //Mettre à jour le magasin pour que l'UI soit mise à jour    yield put({type: 'FETCH_DASHBOARD3_SUCCESS', payload: { departure, }});
```

```
    //déclencher des actions pour Forecast et Flight pour commencer...    //Nous pouvons passer un objet dans l'instruction put    yield put({type: 'FETCH_DEPARTURE3_SUCCESS', departure});
```

```
  } catch(error) {    yield put({type: 'FETCH_FAILED', error: error.message});  }}
```

Rien de différent ici jusqu'à ce que nous arrivions à l'**Effet Put**. Nous pouvons passer un objet aux actions et il sera attribué à la const departure dans la saga de départ et de vol. J'adore ça.

N'hésitez pas à voir la [démo](http://async-redux-saga.surge.sh), et remarquez comment le troisième panneau charge la prévision avant le vol parce que le délai est plus élevé, pour simuler une requête plus lente.

Dans une application de production, je ferais probablement les choses un peu différemment. Je voulais juste souligner que vous pouvez passer des valeurs lorsque vous utilisez l'effet **put**.

#### Et les tests ?

> Vous testez votre code... n'est-ce pas ?

Les Sagas sont faciles à tester, mais elles sont couplées avec vos étapes, sont définies dans la séquence en raison de la nature des générateurs. Voyons un exemple. (Et n'hésitez pas à vérifier tous les tests dans le [dépôt](https://github.com/andresmijares/async-redux-saga) dans le dossier sagas) :

```
describe('Sequenced Saga', () => {  const saga = loadDashboardSequenced();  let output = null;
```

```
it('should take fetch users success', () => {      output = saga.next().value;      let expected = take('FETCH_USER_SUCCESS');      expect(output).toEqual(expected);  });
```

```
it('should select the state from store', () => {      output = saga.next().value;      let expected = select(getUserFromState);      expect(output).toEqual(expected);  });
```

```
it('should call LoadDeparture with the user obj', (done) => {    output = saga.next(user).value;    let expected = call(loadDeparture, user);    done();    expect(output).toEqual(expected);  });
```

```
it('should Load the flight with the flightId', (done) => {    let output = saga.next(departure).value;    let expected = call(loadFlight, departure.flightID);    done();    expect(output).toEqual(expected);  });
```

```
it('should load the forecast with the departure date', (done) => {      output = saga.next(flight).value;      let expected = call(loadForecast, departure.date);      done();      expect(output).toEqual(expected);    });
```

```
it('should put Fetch dashboard success', (done) => {       output = saga.next(forecast, departure, flight ).value;       let expected = put({type: 'FETCH_DASHBOARD_SUCCESS', payload: {forecast, flight, departure}});       const finished = saga.next().done;       done();       expect(finished).toEqual(true);       expect(output).toEqual(expected);    });});
```

1. Assurez-vous d'importer tous les effets et les fonctions helpers que vous allez tester.
2. Lorsque vous stockez une valeur sur le yield, vous devez passer les données mockées à la fonction next. Remarquez le troisième, quatrième et cinquième test.
3. Derrière la scène, chaque générateur passe à la ligne suivante après un yield lorsque la méthode next est appelée. C'est pourquoi nous utilisons **saga.next().value** ici.
4. Cette séquence est gravée dans le marbre. Si vous changez les étapes dans la saga, le test ne passera pas.

### **Conclusion.**

J'aime vraiment tester de nouvelles technologies et dans le développement front-end, nous trouvons de nouvelles choses presque quotidiennement. C'est comme une mode : une fois que quelque chose est accepté par la communauté, c'est comme si tout le monde voulait l'utiliser. Parfois, je trouve beaucoup de valeur dans ces choses, mais il est toujours important de s'asseoir et de vérifier si nous avons vraiment besoin de quelque chose.

J'ai trouvé les _thunks_ plus faciles à implémenter et à maintenir. Mais pour des opérations plus complexes, Redux-Saga fait vraiment un excellent travail.

Une fois de plus, je remercie Thomas pour l'inspiration de cet article. J'espère que quelqu'un trouvera autant d'inspiration dans cet article que j'en ai trouvé dans le sien :).

Si vous avez des questions, n'hésitez pas à [me tweeter](http://twitter.com/andresmijares25). Je suis heureux de vous aider.

Si vous êtes plus intéressé par ce sujet, n'hésitez pas à consulter la deuxième partie de cette série [Redux-saga common patterns.](https://medium.com/shiftgig-blog/redux-saga-common-patterns-48437892e11c)

[**the mediocre engineer**](https://www.youtube.com/channel/UCSBzbeNuDamKpX6N4Q5SaHA)  
[_Pour plus de contenu comme celui-ci, veuillez envisager de vous abonner à ma chaîne www.youtube.com_](https://www.youtube.com/channel/UCSBzbeNuDamKpX6N4Q5SaHA)

Enfin, n'hésitez pas à consulter mes projets open source du moment :

* [**React Calendar Multiday**](https://github.com/sgrepo/react-calendar-multiday)