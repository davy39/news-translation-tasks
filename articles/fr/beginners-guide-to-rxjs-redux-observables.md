---
title: Guide du débutant pour RxJS & Redux Observable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-12T23:28:22.000Z'
originalURL: https://freecodecamp.org/news/beginners-guide-to-rxjs-redux-observables
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/IMG_20181012_232217-min-1.jpg
tags:
- name: observables
  slug: observables
- name: Redux
  slug: redux
- name: RxJS
  slug: rxjs
seo_title: Guide du débutant pour RxJS & Redux Observable
seo_desc: 'By Praveen

  Redux-Observable is an RxJS-based middleware for Redux that allows developers to
  work with async actions. It''s an alternative to redux-thunk and redux-saga.

  This article covers the basics of RxJS, how to setup Redux-Observables, and some
  o...'
---

Par Praveen

[Redux-Observable](https://github.com/redux-observable/redux-observable/) est un middleware basé sur RxJS pour Redux qui permet aux développeurs de travailler avec des actions asynchrones. C'est une alternative à redux-thunk et redux-saga.

Cet article couvre les bases de RxJS, comment installer Redux-Observables, et quelques-uns de ses cas d'utilisation pratiques. Mais avant cela, nous devons comprendre le _modèle Observateur_.

## Modèle Observateur

Dans le modèle Observateur, un objet appelé "Observable" ou "Subject", maintient une collection d'abonnés appelés "Observers". Lorsque l'état du sujet change, il notifie tous ses Observers.

En JavaScript, l'exemple le plus simple serait les émetteurs d'événements et les gestionnaires d'événements.

Lorsque vous utilisez `.addEventListener`, vous ajoutez un observateur à la collection d'observateurs du sujet. Chaque fois que l'événement se produit, le sujet notifie tous les observateurs.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/observer-pattern.png)
_Modèle Observateur_

## RxJS

Selon le site officiel,

> _RxJS est l'implémentation JavaScript de [ReactiveX](http://reactivex.io/), une bibliothèque pour composer des programmes asynchrones et basés sur des événements en utilisant des séquences observables._

En termes simples, RxJS est une implémentation du modèle Observateur. Il étend également le modèle Observateur en fournissant des opérateurs qui nous permettent de composer des Observables et des Subjects de manière déclarative.

Les Observers, Observables, Operators et Subjects sont les éléments de base de RxJS. Examinons donc chacun d'eux plus en détail maintenant.

### Observers

Les Observers sont des objets qui peuvent s'abonner à des Observables et des Subjects. Après s'être abonnés, ils peuvent recevoir des notifications de trois types - next, error et complete.

Tout objet avec la structure suivante peut être utilisé comme Observer. 

```javascript
interface Observer<T> {
    closed?: boolean;
    next: (value: T) => void;
    error: (err: any) => void;
    complete: () => void;
}
```

Lorsque l'Observable envoie des notifications next, error et complete, les méthodes `.next`, `.error` et `.complete` de l'Observer sont appelées.

### Observables

Les Observables sont des objets qui peuvent émettre des données sur une période de temps. Ils peuvent être représentés à l'aide du "diagramme de billes".

![Image](https://www.freecodecamp.org/news/content/images/2020/03/observable-1.png)
_Observable terminé avec succès_

Où la ligne horizontale représente le temps, les nœuds circulaires représentent les données émises par l'Observable, et la ligne verticale indique que l'Observable s'est terminé avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/observable-with-error.png)
_Observable avec une erreur_

Les Observables peuvent rencontrer une erreur. La croix représente l'erreur émise par l'Observable.

Les états "complété" et "erreur" sont finaux. Cela signifie que les Observables ne peuvent pas émettre de données après avoir terminé avec succès ou rencontré une erreur. 

### Créer un Observable

Les Observables sont créés en utilisant le constructeur `new Observable` qui prend un argument - la fonction subscribe. Les Observables peuvent également être créés en utilisant certains opérateurs, mais nous en parlerons plus tard lorsque nous aborderons les opérateurs.

```javascript
import { Observable } from 'rxjs';

const observable = new Observable(subscriber => {
   // Fonction d'abonnement 
});
```

### S'abonner à un Observable

Les Observables peuvent être abonnés en utilisant leur méthode `.subscribe` et en passant un Observer.

```javascript
observable.subscribe({
    next: (x) => console.log(x),
    error: (x) => console.log(x),
    complete: () => console.log('terminé');
});
```

### Exécution d'un Observable

La fonction subscribe que nous avons passée au constructeur `new Observable` est exécutée chaque fois que l'Observable est abonné. 

La fonction subscribe prend un argument - le Subscriber. Le Subscriber ressemble à la structure d'un Observer, et il a les mêmes 3 méthodes : `.next`, `.error` et `.complete`.

Les Observables peuvent envoyer des données à l'Observer en utilisant la méthode `.next`. Si l'Observable s'est terminé avec succès, il peut notifier l'Observer en utilisant la méthode `.complete`. Si l'Observable a rencontré une erreur, il peut envoyer l'erreur à l'Observer en utilisant la méthode `.error`.

```javascript
// Créer un Observable
const observable = new Observable(subscriber => {
   subscriber.next('première donnée');
   subscriber.next('deuxième donnée');
   setTimeout(() => {
       subscriber.next('après 1 seconde - dernière donnée');
       subscriber.complete();
       subscriber.next('donnée après achèvement'); // <-- ignoré
   }, 1000);
   subscriber.next('troisième donnée');
});

// S'abonner à l'Observable
observable.subscribe({
    next: (x) => console.log(x),
    error: (x) => console.log(x),
    complete: () => console.log('terminé')
});

// Sorties :
//
// première donnée
// deuxième donnée
// troisième donnée
// après 1 seconde - dernière donnée
// terminé
```

### Les Observables sont Unicast

Les Observables sont _unicast_, ce qui signifie que les Observables peuvent avoir au plus un abonné. Lorsqu'un Observer s'abonne à un Observable, il obtient une copie de l'Observable qui a son propre chemin d'exécution, rendant les Observables unicast. 

C'est comme regarder une vidéo YouTube. Tous les spectateurs regardent le même contenu vidéo mais peuvent être en train de regarder différents segments de la vidéo.

**Exemple** : créons un Observable qui émet de 1 à 10 sur 10 secondes. Ensuite, abonnons-nous à l'Observable une fois immédiatement, et à nouveau après 5 secondes.

```javascript
// Créer un Observable qui émet des données chaque seconde pendant 10 secondes
const observable = new Observable(subscriber => {
	let count = 1;
    const interval = setInterval(() => {
		subscriber.next(count++);
        
        if (count > 10) {
        	clearInterval(interval);   
        }
    }, 1000);
});

// S'abonner à l'Observable
observable.subscribe({
	next: value => {
        console.log(`Observer 1: ${value}`);
    }
});

// Après 5 secondes, s'abonner à nouveau
setTimeout(() => {
    observable.subscribe({
        next: value => {
            console.log(`Observer 2: ${value}`);
        }
    });
}, 5000);

/* Sortie

Observer 1: 1
Observer 1: 2
Observer 1: 3
Observer 1: 4
Observer 1: 5
Observer 2: 1
Observer 1: 6
Observer 2: 2
Observer 1: 7
Observer 2: 3
Observer 1: 8
Observer 2: 4
Observer 1: 9
Observer 2: 5
Observer 1: 10
Observer 2: 6
Observer 2: 7
Observer 2: 8
Observer 2: 9
Observer 2: 10

*/
```

Dans la sortie, vous pouvez remarquer que le deuxième Observer a commencé à imprimer à partir de 1 même s'il s'est abonné après 5 secondes. Cela se produit parce que le deuxième Observer a reçu une copie de l'Observable dont la fonction subscribe a été invoquée à nouveau. Cela illustre le comportement unicast des Observables.

## Subjects

Un Subject est un type spécial d'Observable.

### Créer un Subject

Un Subject est créé en utilisant le constructeur `new Subject`.

```javascript
import { Subject } from 'rxjs';

// Créer un subject
const subject = new Subject();
```

### S'abonner à un Subject

S'abonner à un Subject est similaire à s'abonner à un Observable : vous utilisez la méthode `.subscribe` et passez un Observer.

```javascript
subject.subscribe({
    next: (x) => console.log(x),
    error: (x) => console.log(x),
    complete: () => console.log("terminé")
});
```

### Exécution d'un Subject

Contrairement aux Observables, un Subject appelle ses propres méthodes `.next`, `.error` et `.complete` pour envoyer des données aux Observers.

```javascript
// Envoyer des données à tous les observers
subject.next('première donnée');

// Envoyer une erreur à tous les observers
subject.error('oops quelque chose s'est mal passé');

// Terminer
subject.complete('terminé');
```

### Les Subjects sont Multicast

Les Subjects sont _multicast_ : plusieurs Observers partagent le même Subject et son chemin d'exécution. Cela signifie que toutes les notifications sont diffusées à tous les Observers. C'est comme regarder un programme en direct. Tous les téléspectateurs regardent le même segment du même contenu au même moment.

**Exemple** : créons un Subject qui émet de 1 à 10 sur 10 secondes. Ensuite, abonnons-nous à l'Observable une fois immédiatement, et à nouveau après 5 secondes.

```javascript
// Créer un subject
const subject = new Subject();

let count = 1;
const interval = setInterval(() => {
    subscriber.next(count++);
    if (count > 10) {
        clearInterval(interval);
    }
}, 1000);

// S'abonner aux subjects
subject.subscribe(data => {
    console.log(`Observer 1: ${data}`);
});

// Après 5 secondes, s'abonner à nouveau
setTimeout(() => {
    subject.subscribe(data => {
    	console.log(`Observer 2: ${data}`);
	});
}, 5000);

/* SORTIE

Observer 1: 1
Observer 1: 2
Observer 1: 3
Observer 1: 4
Observer 1: 5
Observer 2: 5
Observer 1: 6
Observer 2: 6
Observer 1: 7
Observer 2: 7
Observer 1: 8
Observer 2: 8
Observer 1: 9
Observer 2: 9
Observer 1: 10
Observer 2: 10

*/

```

Dans la sortie, vous pouvez remarquer que le deuxième Observer a commencé à imprimer à partir de 5 au lieu de commencer à partir de 1. Cela se produit parce que le deuxième Observer partage le même Subject. Puisqu'il s'est abonné après 5 secondes, le Subject a déjà fini d'émettre de 1 à 4. Cela illustre le comportement multicast d'un Subject.

### Les Subjects sont à la fois Observable et Observer

Les Subjects ont les méthodes `.next`, `.error` et `.complete`. Cela signifie qu'ils suivent la structure des Observers. Par conséquent, un Subject peut également être utilisé comme Observer et passé à la fonction `.subscribe` des Observables ou d'autres Subjects.

**Exemple** : créons un Observable et un Subject. Ensuite, abonnons-nous à l'Observable en utilisant le Subject comme Observer. Enfin, abonnons-nous au Subject. Toutes les valeurs émises par l'Observable seront envoyées au Subject, et le Subject diffusera les valeurs reçues à tous ses Observers.

```javascript
// Créer un Observable qui émet des données chaque seconde
const observable = new Observable(subscriber => {
   let count = 1;
   const interval = setInterval(() => {
       subscriber.next(count++);
       
       if (count > 5) {
        	clearInterval(interval);   
       }
   }, 1000);
});

// Créer un subject
const subject = new Subject();

// Utiliser le Subject comme Observer et s'abonner à l'Observable
observable.subscribe(subject);

// S'abonner au subject
subject.subscribe({
    next: value => console.log(value)
});

/* Sortie

1
2
3
4
5

*/
```

## Opérateurs

Les opérateurs sont ce qui rend RxJS utile. Les opérateurs sont des fonctions pures qui retournent un nouvel Observable. Ils peuvent être catégorisés en 2 catégories principales :

1. Opérateurs de création
2. Opérateurs pipables

### Opérateurs de création

Les opérateurs de création sont des fonctions qui peuvent créer un nouvel Observable. 

**Exemple** : nous pouvons créer un Observable qui émet chaque élément d'un tableau en utilisant l'opérateur `from`.

```javascript
const observable = from([2, 30, 5, 22, 60, 1]);

observable.subscribe({
    next: (value) => console.log("Reçu", value),
    error: (err) => console.log(err),
    complete: () => console.log("terminé")
});

/* SORTIES

Reçu 2
Reçu 30
Reçu 5
Reçu 22
Reçu 60
Reçu 1
terminé

*/
```

Le même peut être un Observable en utilisant le diagramme de billes.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/from-operator.png)

### Opérateurs pipables

Les opérateurs pipables sont des fonctions qui prennent un Observable en entrée et retournent un nouvel Observable avec un comportement modifié. 

**Exemple** : prenons l'Observable que nous avons créé en utilisant l'opérateur `from`. Maintenant, en utilisant cet Observable, nous pouvons créer un nouvel Observable qui émet uniquement les nombres supérieurs à 10 en utilisant l'opérateur `filter`.

```javascript
const greaterThanTen = observable.pipe(filter(x => x > 10));

greaterThanTen.subscribe(console.log, console.log, () => console.log("terminé"));

// SORTIE
// 11
// 12
// 13
// 14
// 15
```

Le même peut être représenté en utilisant le diagramme de billes.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/filter-operator.png)

Il existe de nombreux autres opérateurs utiles. Vous pouvez voir la liste complète des opérateurs avec des exemples sur la documentation officielle de RxJS [ici](https://rxjs-dev.firebaseapp.com/guide/operators). 

Il est crucial de comprendre tous les opérateurs couramment utilisés. Voici quelques opérateurs que j'utilise souvent :

1. `mergeMap`
2. `switchMap`
3. `exhaustMap`
4. `map`
5. `catchError`
6. `startWith`
7. `delay`
8. `debounce`
9. `throttle`
10. `interval`
11. `from`
12. `of`

## Redux Observables

Selon le site officiel,

> [RxJS](http://github.com/ReactiveX/RxJS)-based middleware pour [Redux](http://github.com/reactjs/redux). Composez et annulez des actions asynchrones pour créer des effets secondaires et plus.

Dans Redux, chaque fois qu'une action est dispatchée, elle passe par toutes les fonctions de réducteur et un nouvel état est retourné. 

Redux-observable prend toutes ces actions dispatchées et ces nouveaux états et crée deux observables à partir de ceux-ci - Actions observable `action$`, et States observable `state$`. 

L'observable des actions émettra toutes les actions qui sont dispatchées en utilisant `store.dispatch()`. L'observable des états émettra tous les nouveaux objets d'état retournés par le réducteur racine.

## Epics

Selon le site officiel,

> C'est une fonction qui prend un flux d'actions et retourne un flux d'actions. **Actions en entrée, actions en sortie.**

Les Epics sont des fonctions qui peuvent être utilisées pour s'abonner aux Observables d'Actions et d'États. Une fois abonnés, les epics recevront le flux d'actions et d'états en entrée, et doivent retourner un flux d'actions en sortie. _**Actions en entrée - Actions en sortie.**_

```javascript
const someEpic = (action$, state$) => { 
    return action$.pipe( // s'abonner à l'observable des actions
        map(action => { // Recevoir chaque action, Actions en entrée
            return someOtherAction(); // retourner une action, Actions en sortie
        })
    )
}
```

Il est important de comprendre que toutes les actions reçues dans l'Epic ont déjà _fini de passer par les réducteurs_.

À l'intérieur d'un Epic, nous pouvons utiliser n'importe quel motif observable de RxJS, et c'est ce qui rend redux-observables utile.

**Exemple** : nous pouvons utiliser l'opérateur `.filter` pour créer un nouvel observable intermédiaire. De même, nous pouvons créer n'importe quel nombre d'observables intermédiaires, mais la sortie finale de l'observable final doit être une action, sinon une exception sera levée par redux-observable.

```javascript
const sampleEpic = (action$, state$) => {
    return action$.pipe(
    	filter(action => action.payload.age >= 18), // peut créer des observables et flux intermédiaires
        map(value => above18(value)) // où above18 est un créateur d'action
    );
}
```

Chaque action émise par les Epics est immédiatement dispatchée en utilisant `store.dispatch()`. 

## Installation

Tout d'abord, installons les dépendances.

```shell
npm install --save rxjs redux-observable
```

Créez un dossier séparé nommé `epics` pour garder tous les epics. Créez un nouveau fichier `index.js` à l'intérieur du dossier `epics` et combinez tous les epics en utilisant la fonction `combineEpics` pour créer l'epic racine. Ensuite, exportez l'epic racine.

```javascript
import { combineEpics } from 'redux-observable';
import { epic1 } from './epic1';
import { epic2 } from './epic2';

const epic1 = (action$, state$) => {
 ...   
}
 
const epic2 = (action$, state$) => {
 ...   
}
 
export default combineEpics(epic1, epic2);
```

Créez un middleware epic en utilisant la fonction `createEpicMiddleware` et passez-le à la fonction `createStore` de Redux.

```javascript
import { createEpicMiddleware } from 'redux-observable';
import { createStore, applyMiddleware } from 'redux';
import rootEpic from './rootEpics';

const epicMiddleware = createEpicMiddlware();

const store = createStore(
    rootReducer,
    applyMiddleware(epicMiddlware)
);
```

Enfin, passez l'epic racine à la méthode `.run` du middleware epic.

```javascript
epicMiddleware.run(rootEpic);
```

## Quelques cas d'utilisation pratiques

RxJS a une courbe d'apprentissage importante, et la configuration de redux-observable aggrave le processus de configuration déjà douloureux de Redux. Tout cela fait que Redux observable semble être un surdimensionnement. Mais voici quelques cas d'utilisation pratiques qui peuvent changer votre avis.

_Tout au long de cette section, je comparerai redux-observables avec redux-thunk pour montrer comment redux-observables peut être utile dans des cas d'utilisation complexes. Je n'aime pas redux-thunk, je l'adore, et je l'utilise tous les jours !_

### 1. Faire des appels API

**Cas d'utilisation** : Faire un appel API pour récupérer les commentaires d'un post. Afficher des chargeurs lorsque l'appel API est en cours et gérer également les erreurs API.

Une implémentation redux-thunk ressemblerait à ceci,

```javascript
function getComments(postId){
    return (dispatch) => {
        dispatch(getCommentsInProgress());
        axios.get(`/v1/api/posts/${postId}/comments`).then(response => {
            dispatch(getCommentsSuccess(response.data.comments));
        }).catch(() => {
            dispatch(getCommentsFailed());
        });
    }
}
```

et cela est absolument correct. Mais le créateur d'action est gonflé.

Nous pouvons écrire un Epic pour implémenter la même chose en utilisant redux-observables.

```javascript
const getCommentsEpic = (action$, state$) => action$.pipe(
    ofType('GET_COMMENTS'),
    mergeMap((action) => from(axios.get(`/v1/api/posts/${action.payload.postId}/comments`).pipe(
        map(response => getCommentsSuccess(response.data.comments)),
        catchError(() => getCommentsFailed()),
        startWith(getCommentsInProgress())
    )
);
```

Maintenant, cela nous permet d'avoir un créateur d'action propre et simple comme ceci,

```javascript
function getComments(postId) {
    return {
        type: 'GET_COMMENTS',
        payload: {
            postId
        }
    }
}
```

### 2. Débogage des requêtes

**Cas d'utilisation** : Fournir une complétion automatique pour un champ de texte en appelant une API chaque fois que la valeur du champ de texte change. L'appel API doit être fait 1 seconde après que l'utilisateur a arrêté de taper.

Une implémentation redux-thunk ressemblerait à ceci,

```javascript
let timeout;

function valueChanged(value) {
    return dispatch => {
        dispatch(loadSuggestionsInProgress());
        dispatch({
            type: 'VALUE_CHANGED',
            payload: {
                value
            }
        });

        // Si changé à nouveau dans 1 seconde, annuler le timeout
        timeout && clearTimeout(timeout);

        // Faire un appel API après 1 seconde
        timeout = setTimeout(() => {
        	axios.get(`/suggestions?q=${value}`)
                .then(response =>
                      dispatch(loadSuggestionsSuccess(response.data.suggestions)))
                .catch(() => dispatch(loadSuggestionsFailed()))
        }, 1000, value);
    }
}
```

Il nécessite une variable globale `timeout`. Lorsque nous commençons à utiliser des variables globales, nos créateurs d'actions ne sont plus des fonctions pures. Il devient également difficile de tester unitairement les créateurs d'actions qui utilisent une variable globale.

Nous pouvons implémenter la même chose avec redux-observable en utilisant l'opérateur `.debounce`.

```javascript
const loadSuggestionsEpic = (action$, state$) => action$.pipe(
    ofType('VALUE_CHANGED'),
    debounce(1000),
    mergeMap(action => from(axios.get(`/suggestions?q=${action.payload.value}`)).pipe(
    	map(response => loadSuggestionsSuccess(response.data.suggestions)),
        catchError(() => loadSuggestionsFailed())
    )),
    startWith(loadSuggestionsInProgress())
);
```

Maintenant, nos créateurs d'actions peuvent être nettoyés, et surtout, ils peuvent être des fonctions pures à nouveau.

```javascript
function valueChanged(value) {
    return {
        type: 'VALUE_CHANGED',
        payload: {
            value
        }
    }
}
```

### 3. Annulation de requête

**Cas d'utilisation** : En continuant le cas d'utilisation précédent, supposons que l'utilisateur n'a rien tapé pendant 1 seconde, et nous avons fait notre 1er appel API pour récupérer les suggestions. 

Disons que l'API elle-même prend en moyenne 2-3 secondes pour retourner le résultat. Maintenant, si l'utilisateur tape quelque chose pendant que le 1er appel API est en cours, après 1 seconde, nous ferons notre 2ème API. Nous pouvons nous retrouver avec deux appels API en même temps, et cela peut créer une condition de course. 

Pour éviter cela, nous devons annuler le 1er appel API avant de faire le 2ème appel API.

Une implémentation redux-thunk ressemblerait à ceci,

```javascript
let timeout;
var cancelToken = axios.cancelToken;
let apiCall;

function valueChanged(value) {    
    return dispatch => {
        dispatch(loadSuggestionsInProgress());
        dispatch({
            type: 'VALUE_CHANGED',
            payload: {
                value
            }
        });

        // Si changé à nouveau dans 1 seconde, annuler le timeout
        timeout && clearTimeout(timeout);

        // Faire un appel API après 1 seconde
        timeout = setTimeout(() => {
            // Annuler l'API existante
            apiCall && apiCall.cancel('Opération annulée');
            
            // Générer un nouveau token
            apiCall = cancelToken.source();
            
            
            axios.get(`/suggestions?q=${value}`, {
                cancelToken: apiCall.token
            })
                .then(response => dispatch(loadSuggestionsSuccess(response.data.suggestions)))
                .catch(() => dispatch(loadSuggestionsFailed()))
     
        }, 1000, value);
    }
}
```

Maintenant, il nécessite une autre variable globale pour stocker le token d'annulation d'Axios. Plus de variables globales = plus de fonctions impures !

Pour implémenter la même chose en utilisant redux-observable, tout ce que nous avons à faire est de remplacer `.mergeMap` par `.switchMap`.

```javascript
const loadSuggestionsEpic = (action$, state$) => action$.pipe(
    ofType('VALUE_CHANGED'),
    throttle(1000),
    switchMap(action => from(axios.get(`/suggestions?q=${action.payload.value}`)).pipe(
    	map(response => loadSuggestionsSuccess(response.data.suggestions)),
        catchError(() => loadSuggestionsFailed())
    )),
    startWith(loadSuggestionsInProgress())
);
```

Puisqu'il ne nécessite aucun changement à nos créateurs d'actions, ils peuvent continuer à être des fonctions pures.

De même, il existe de nombreux cas d'utilisation où Redux-Observables brille réellement ! Par exemple, l'interrogation d'une API, l'affichage de barres de notification, [la gestion des connexions WebSocket](https://techinscribed.com/websocket-connection-reconnection-rxjs-redux-observable/), etc.

## Conclusion

Si vous développez une application Redux qui implique de tels cas d'utilisation complexes, il est fortement recommandé d'utiliser Redux-Observables. Après tout, les avantages de son utilisation sont directement proportionnels à la complexité de votre application, et cela est évident à partir des cas d'utilisation pratiques mentionnés ci-dessus.

Je crois fermement que l'utilisation du bon ensemble de bibliothèques nous aidera à [développer des applications beaucoup plus propres et maintenables](https://techinscribed.com/clean-react-architecture-with-redux-immer-typescript-redux-observable/), et à long terme, les avantages de leur utilisation l'emporteront sur les inconvénients.