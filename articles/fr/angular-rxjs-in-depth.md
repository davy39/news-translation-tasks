---
title: Angular RxJS En Profondeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-22T21:34:20.000Z'
originalURL: https://freecodecamp.org/news/angular-rxjs-in-depth
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549534749_use-reactive-programming-you-must.jpg
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: Angular RxJS En Profondeur
seo_desc: 'By Ahmed Bouchefra

  In this tutorial, we''ll learn to use the RxJS 6 library with Angular 6 or Angular
  7. We''ll learn about:


  How to import the Observable class and the other operators.

  How to subscribe and unsubscribe from Observables.

  How to import a...'
---

Par Ahmed Bouchefra

Dans ce tutoriel, nous allons apprendre à utiliser la bibliothèque RxJS 6 avec Angular 6 ou Angular 7. Nous allons apprendre :

* Comment importer la classe Observable et les autres opérateurs.
* Comment s'abonner et se désabonner des Observables.
* Comment importer et appeler des opérateurs et les chaîner avec la fonction `pipe()`.
* Nous verrons également comment utiliser le pipe async pour s'abonner aux Observables depuis les templates Angular.
* Enfin, nous verrons comment utiliser certains opérateurs populaires comme `tap()`, `map()` et `filter()` ainsi que leurs nouveaux chemins d'importation dans RxJS 6.

**Note** : Ce tutoriel fonctionne avec Angular 6 et Angular 7.

Tout au long de ce tutoriel, nous commencerons par examiner ce que sont la programmation réactive, les opérations asynchrones et les flux de données, et comment ils sont liés à la bibliothèque RxJS. Nous verrons ensuite le concept d'un `Observable` RxJS avec des exemples, les différents types d'Observables tels que :

* `Subject`,
* `BehaviorSubject` et `ReplaySubject`,
* Observables unicast et multicast,
* Observables cold et hot, etc.

Ensuite, nous verrons ce que sont les opérateurs RxJS et des exemples de certains opérateurs populaires tels que `tap()`, `map()`, `filter()`, `share()`, etc. Et enfin, nous verrons comment Angular utilise l'Observable RxJS pour faire de la programmation asynchrone.

## Qu'est-ce que la Programmation Réactive

![Qu'est-ce que la Programmation Réactive](https://d2mxuefqeaa7sj.cloudfront.net/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549534749_use-reactive-programming-you-must.jpg)

Voyons la définition de la programmation réactive selon différentes sources.

Voici comment André Staltz, le créateur de [cycle.js](https://cycle.js.org/) (Un framework JavaScript fonctionnel et réactif pour un code prévisible) la définit :

La programmation réactive est la programmation avec des flux de données asynchrones

Cela signifie que lorsque vous écrivez du code qui traite des opérations asynchrones et des flux de données, vous faites de la programmation réactive.

Maintenant, voici la définition de [Wikipedia](https://en.wikipedia.org/wiki/Reactive_programming) qui est plus approfondie :

En informatique, la programmation réactive est un paradigme de programmation déclarative concerné par les flux de données et la propagation du changement.

Cela signifie que la programmation réactive est un style de programmation déclaratif (par opposition à procédural) qui fonctionne sur des flux de données.

Pour un guide détaillé sur la programmation réactive et les flux de données, consultez : [The introduction to Reactive Programming you've been missing](https://gist.github.com/staltz/868e7e9bc2a7b8c1f754).

**Qu'est-ce qu'un Stream**

Un stream est un concept essentiel en programmation réactive, il est donc utile de voir la définition avant de continuer.

![Qu'est-ce qu'un stream](https://d2mxuefqeaa7sj.cloudfront.net/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549589200_687474703a2f2f692e696d6775722e636f6d2f4149696d5138432e6a7067.jpeg)

Dans toutes les définitions que nous avons vues, le mot **stream** apparaît.

Alors, qu'est-ce qu'un stream ?

Simplement :

Un stream fait référence à des valeurs de données au fil du temps.

Nous verrons plus tard que les Observables et les streams sont des concepts très liés.

## Qu'est-ce que RxJS

Maintenant que nous avons vu les concepts de programmation réactive et de flux de données, voyons ce qu'est RxJS.

![Qu'est-ce que RxJS](https://d2mxuefqeaa7sj.cloudfront.net/s_98CC91BB1D7ABCD50AC04362B7F541F3549A631A6219D02FE7AED5645CF1CAA7_1549549625485_what-if-reactive-programming-is-just-a-myth-and-facebook-and-netflix-dont-exist.jpg)

[RxJS](https://github.com/ReactiveX/rxjs) est une bibliothèque populaire parmi les développeurs web. Elle fournit des modèles de programmation fonctionnelle et réactive pour travailler avec des événements et des flux de données et a été intégrée dans de nombreuses bibliothèques et frameworks de développement web tels qu'Angular.

RxJS facilite l'écriture de code asynchrone pour les développeurs JavaScript en utilisant des Observables composables au lieu de callbacks et de Promesses.

RxJS signifie Reactive Extensions pour JavaScript et il existe des implémentations dans d'autres langages de programmation tels que Java, Python, Ruby, et PHP, etc. Il est également disponible pour des plateformes telles qu'Android. Consultez la [liste complète des langages et plateformes supportés](http://reactivex.io/languages.html).

RxJS v6 est actuellement la version stable de RxJS et elle comporte de nombreuses modifications majeures par rapport à RxJS v5. Vous pouvez consulter plus d'informations sur les changements et comment migrer depuis l'ancienne version à partir de ce guide officiel de [migration](https://github.com/ReactiveX/rxjs/blob/master/docs_app/content/guide/v6/migration.md).

RxJS 6 présente de nombreux avantages par rapport à la version précédente RxJS 5, tels que :

* La taille du bundle de la bibliothèque est plus petite,
* Les performances de la dernière version sont meilleures,
* RxJS 6 Observable suit la [proposition de spécification Observable](https://github.com/zenparsing/es-observable),
* La dernière version offre une meilleure débogabilité,
* Une meilleure architecture modulaire,
* Il est rétrocompatible.

## Comment Installer et Utiliser RxJS

RxJS est une bibliothèque JavaScript, ce qui signifie que vous pouvez l'installer de la même manière que vous installez d'autres bibliothèques :

**Utilisation de RxJS avec ES6 via npm**

Dans votre projet, vous pouvez exécuter la commande suivante pour installer RxJS :

```
$ npm install rxjs

```

Vous pouvez ensuite importer les symboles que vous souhaitez utiliser depuis le package `rxjs` ou un sous-package tel que `rxjs/operators` :

```
import { Observable, Subscriber } from 'rxjs';
import { tap, map, filter } from 'rxjs/operators';

```

Nous avons importé les symboles `Observable` et `Subscriber` depuis `rxjs` et les opérateurs `tap`, `map` et `filter` depuis `rxjs/operators`.

Nous verrons plus tard ce que sont ces symboles et comment les utiliser dans votre application Angular.

**Utilisation de RxJS depuis un CDN**

Vous pouvez également utiliser RxJS depuis un [CDN](https://unpkg.com/rxjs/bundles/rxjs.umd.min.js) en utilisant une balise `<script>` dans votre document HTML :

```
<script src="https://unpkg.com/rxjs/bundles/rxjs.umd.min.js"></script>

```

**Note** : Veuillez noter que dans Angular 6 & 7, RxJS 6 est déjà inclus dans votre projet, vous n'avez donc pas besoin de l'installer manuellement.

## Qu'est-ce qu'un Observable, Observer et Subscription dans RxJS 6

RxJS utilise le concept d'Observables pour gérer et travailler avec du code asynchrone et basé sur des événements.

Le mot asynchrone vient de l'asynchronisme. En programmation informatique, voici la définition de l'asynchronisme selon [Wikipedia](https://en.wikipedia.org/wiki/Asynchrony_(computer_programming)) :

L'asynchronisme, en programmation informatique, fait référence à l'occurrence d'événements indépendants du flux principal du programme et aux moyens de traiter de tels événements. Ceux-ci peuvent être des événements "externes" tels que l'arrivée de signaux, ou des actions initiées par un programme qui se produisent simultanément avec l'exécution du programme, sans que le programme ne bloque pour attendre les résultats.

Après avoir lu cette définition, vous avez peut-être conclu à quel point l'asynchronisme est important pour les ordinateurs et la programmation !

Rendons cela simple !

Le code **asynchrone** est l'inverse du code **synchrone** qui est la manière originale de penser à votre code lorsque vous êtes initié à la programmation.

Votre code est synchrone lorsqu'il s'exécute en séquences, c'est-à-dire instruction par instruction dans l'ordre où elles apparaissent dans le code source.

Par exemple, considérons ce simple code JavaScript :

```
const foo = "foo" //1
const bar = "bar" //2
const foobar = foo  +  bar //3
console.log(foobar) //4

```

Le navigateur exécutera ce code synchrone ligne par ligne de la ligne 1 à 4, en commençant par assigner les variables `foo` et `bar`, en les concaténant et en affichant la variable `foobar` dans la console.

JavaScript supporte également l'approche **asynchrone** d'écriture de code, ce qui est logique, puisque vous devez répondre aux événements utilisateur dans le navigateur, mais vous ne savez pas réellement quand l'utilisateur interagit avec votre application (et dans quel ordre) lorsque vous écrivez du code.

Cela était initialement réalisé en utilisant des callbacks que vous devez définir dans votre code et spécifier quand ils seront appelés.

Par exemple, le code asynchrone suivant affichera **Vous avez cliqué sur le bouton !** lorsque l'utilisateur clique sur le bouton identifié par l'identifiant `mybutton` :

```
document.getElementById('mybutton').addEventListener('click', () => {
  console.log("Vous avez cliqué sur le bouton !")
})

```

Le deuxième argument de la méthode `addEventListener()` est le callback.

Vous pouvez également utiliser des callbacks pour gérer des opérations asynchrones qui n'impliquent pas le DOM. Par exemple, le code suivant peut être utilisé pour envoyer une requête HTTP POST à un serveur web :

```
const xhr = new XMLHttpRequest()
xhr.onreadystatechange = () => {
  if (xhr.readyState === 4) {
    xhr.status === 200 ? console.log(xhr.responseText) : console.error('erreur')
  }
}
xhr.open('POST', 'your.server.com')
xhr.send()

```

C'est ainsi que vous effectuez les fameuses appels Ajax en JavaScript.

En fait, [Ajax](https://en.wikipedia.org/wiki/Ajax_(programming)) lui-même signifie **A**synchronous **J**avaScript **a**nd **X**ML.

**Note** : L'envoi de requêtes HTTP (qui est une opération courante dans les applications web) est une opération asynchrone par nature, car la requête prendra du temps pour atteindre le serveur qui enverra ensuite une réponse à votre application cliente. Pendant ce temps, l'application doit répondre à d'autres actions et effectuer d'autres tâches et ne traiter la réponse du serveur que lorsqu'elle est reçue.

Si vous avez déjà travaillé de manière extensive avec des callbacks, vous remarquerez un problème avec eux. Ils sont difficiles à suivre !

Lorsque vous écrivez des applications complexes, vous finissez généralement par écrire des callbacks imbriqués (des callbacks dans des callbacks) avec plusieurs niveaux d'imbrication. C'est ce qu'on appelle l'[enfer des callbacks](https://stackoverflow.com/questions/25098066/what-is-callback-hell-and-how-and-why-rx-solves-it).

Le JavaScript moderne a introduit d'autres approches ou abstractions pour traiter les opérations asynchrones (sans utiliser trop de callbacks) telles que les Promesses et Async/Await.

Les Promesses ont été introduites dans [ES6](https://www.ecma-international.org/ecma-262/6.0/) (JS 2015).

Async/await a été introduit dans ES8 (JS 2017) et c'est en fait un sucre syntaxique sur le dessus des Promesses qui aide les développeurs à écrire du code asynchrone avec des Promesses d'une manière qui semble synchrone.

Mais les Promesses sont en fait similaires aux callbacks et ont le même problème d'imbrication à un certain degré.

Puisque les développeurs recherchent toujours de meilleures solutions, nous avons maintenant des Observables qui utilisent le [modèle d'observateur](https://en.wikipedia.org/wiki/Observer_pattern).

Le modèle d'observateur est un modèle de conception logicielle dans lequel un objet, appelé le sujet, maintient une liste de ses dépendants, appelés observateurs, et les notifie automatiquement de tout changement d'état, généralement en appelant l'une de leurs méthodes. [Modèle d'observateur](https://en.wikipedia.org/wiki/Observer_pattern).

Les Observables sont implémentés dans le projet [ReactiveX](http://reactivex.io/) qui a des implémentations dans divers langages. RxJS est l'implémentation JavaScript.

**Note** : Les Observables sont implémentés dans de nombreuses autres bibliothèques telles que [zen-observable](https://github.com/zenparsing/zen-observable) et [xstream](https://github.com/staltz/xstream), mais les Observables RxJS sont les plus populaires en JavaScript.

Les Observables ne sont pas encore une fonctionnalité intégrée de JavaScript, mais il existe une [proposition](https://tc39.github.io/proposal-observable/) pour les ajouter dans EcmaScript.

Maintenant, qu'est-ce qu'un Observable RxJS ?

Un Observable est une entité qui émet (ou publie) plusieurs valeurs de données (flux de données) au fil du temps et de manière asynchrone.

C'est la définition d'un Observable selon la [documentation RxJS](https://rxjs.dev/guide/overview)

Observable représente l'idée d'une collection invocable de valeurs ou d'événements futurs.

**Observers et Subscriptions**

Il existe également des concepts liés avec lesquels vous travaillerez lorsque vous utiliserez des Observables, qui sont les **Observers** et les **Subscriptions**. 

Les Observers sont également appelés listeners (ou consommateurs) car ils peuvent écouter ou s'abonner pour obtenir les données observées.

Selon la documentation RxJS :

Observer est une collection de callbacks qui sait comment écouter les valeurs délivrées par l'Observable.

Les [Subscriptions](http://reactivex.io/rxjs/class/es6/Subscription.js~Subscription.html) sont des objets qui sont retournés lorsque vous vous abonnez à un Observable. Ils contiennent de nombreuses méthodes telles que la méthode `unsubscribe()` que vous pouvez appeler pour vous désabonner de la réception des valeurs publiées par l'Observable.

Selon la documentation officielle :

Subscription représente l'exécution d'un Observable, est principalement utile pour annuler l'exécution.

## Qu'est-ce qu'un Subject dans RxJS

Un [Subject](https://rxjs-dev.firebaseapp.com/guide/subject) est un type spécial d'Observable auquel les observateurs peuvent également s'abonner pour recevoir des valeurs publiées, mais avec une différence : **Les valeurs sont multidiffusées à de nombreux Observers**. 

**Note** : Par défaut, un Observable RxJS est unicast.

Unicast signifie simplement que chaque observateur abonné a une exécution indépendante de l'Observable, tandis que multicast signifie que l'exécution de l'Observable est partagée par plusieurs Observers.

**Note** : Les Subjects sont similaires aux EventEmitters d'Angular.

Ainsi, lorsque vous utilisez des Subjects au lieu de simples Observables, tous les Observers abonnés recevront les mêmes valeurs des données émises.

**Note** : Les Subjects sont également des Observers, c'est-à-dire qu'ils peuvent également s'abonner à d'autres Observables et écouter les données publiées.

**Observables Hot et Cold**

Contrairement aux Observables réguliers, les Subjects sont appelés **hot**. Un Observable hot commence à émettre des événements même avant qu'un observateur ne s'y abonne, ce qui signifie que les observateurs peuvent perdre des valeurs émises précédemment s'ils ne s'abonnent pas au bon moment, tandis que les Observables **cold** commencent à émettre des valeurs lorsqu'au moins un observateur est abonné.

**Note** : Vous pouvez utiliser la méthode `asObservable()` pour convertir un subject en un simple Observable.

## `BehaviorSubject` et `ReplaySubject` de RxJS

RxJS fournit deux autres types de Subjects : `BehaviorSubject` et `ReplaySubject`.

Avec un Subject normal, les Observers qui s'abonnent à un moment ultérieur ne recevront pas les valeurs de données émises avant leurs abonnements. Dans de nombreuses situations, ce n'est pas le comportement souhaité que nous voulons implémenter. Cela peut être résolu en utilisant `BehaviorSubject` et `ReplaySubject`.

`ReplaySubject` fonctionne en utilisant un tampon qui conserve les valeurs émises et les réémet lorsque de nouveaux Observers s'abonnent.

`BehaviorSubject` fonctionne comme `ReplaySubject` mais ne réémet que la dernière valeur émise.

## Comment Créer un Observable RxJS

Vous pouvez créer un Observable RxJS en utilisant la méthode `Observable.create()` qui prend une fonction avec un argument `observer`. Vous pouvez ensuite vous abonner à l'instance d'Observable retournée.

Il existe de nombreuses autres méthodes pour créer des Observables en plus de la méthode statique `create()` :

* La méthode d'instance `lift()` qui crée un nouvel Observable à partir de l'instance (la source) sur laquelle elle est appelée,
* L'opérateur `of([])` qui crée un Observable d'une seule valeur. Nous verrons un exemple ensuite,
* L'opérateur `interval(interval)` qui crée un Observable qui émet une séquence infinie de nombres. Chaque nombre est émis à un intervalle de temps constant en secondes,
* L'opérateur [timer()](http://reactivex.io/documentation/operators/timer.html) qui retourne un Observable qui, après une durée spécifiée, émet des nombres en séquence à chaque durée spécifiée,
* La méthode `from()` qui crée un Observable à partir d'une Promesse ou d'un tableau de valeurs,
* La méthode `fromEvent()` qui crée un Observable à partir d'un événement DOM,
* La méthode `ajax()` qui crée un Observable qui envoie une requête Ajax.

Nous verrons ces méthodes de création par exemple plus tard.

### Comment S'abonner à un Observable RxJS

Après avoir créé un `Observable`, vous pouvez vous y abonner en utilisant la méthode `subscribe()` sur l'instance, qui retourne une instance de `Subscription`.

### Un Exemple Simple de l'Observable RxJS

Voyons maintenant un exemple simple de création et de travail avec un Observable.

Commençons par créer un Observable :

```
let ob$ = Observable.create((observer) => {
    observer.next("Une nouvelle valeur !");
});

```

Nous créons un Observable `ob$` et nous définissons la logique que notre Observable est censé faire dans le corps de la méthode passée.

Dans cet exemple, l'Observable émettra simplement la valeur **Une nouvelle valeur !** à l'Observer abonné.

**Note** : Le signe dollar est juste une convention pour nommer les variables qui contiennent une instance d'Observables.

Nous appelons la méthode `next()` de l'objet observer pour l'informer des valeurs disponibles.

**Note** : Tous les objets observer doivent avoir une collection de méthodes telles que `next()`, `complete()` et `error()`. Cela permet aux Observables de communiquer avec eux.

La méthode `next()` est utilisée par l'Observable pour passer des valeurs (publier des valeurs) à l'Observer abonné.

Ensuite, créons un objet observer :

```
let observer = {
    next: data => console.log( 'Données reçues : ', data),
    complete: data => console.log('Complété'),
};

```

Un observer est un objet JavaScript simple qui contient des méthodes telles que `next()`, `complete()` et `error()`. Cela signifie qu'il sait comment être notifié par l'Observable.

**Note** : Vous pouvez également ajouter d'autres attributs et méthodes personnalisés aux objets Observer en plus de `next()`, `complete()` et `error()`.

Enfin, abonnons-nous à notre Observable `ob$` et retournons une `Subscription` :

```
let subscription = ob$.subscribe(observer);

```

Une fois que vous vous êtes abonné à l'Observable `ob$`, vous obtiendrez la sortie suivante dans la console :

```
Données reçues : Une nouvelle valeur ! 

```

## Opérateurs RxJS

RxJS fournit l'implémentation du concept d'Observable mais également une variété d'opérateurs qui vous permettent de composer des Observables.

Les opérateurs offrent une manière déclarative d'effectuer des opérations asynchrones complexes avec des Observables.

Un opérateur fonctionne sur un Observable source en observant ses valeurs émises et en appliquant la transformation souhaitée sur elles, puis retourne un nouvel Observable avec les valeurs modifiées.

Il existe de nombreux opérateurs RxJS tels que :

* `tap()`,
* `map()`,
* `filter()`,
* `concat()`,
* `share()`,
* `retry()`,
* `catchError()`,
* `switchMap()`,
* et `flatMap()`, etc.

## Pipes : Combinaison de Plusieurs Opérateurs

RxJS fournit deux versions de la fonction `pipe()` : une fonction autonome et une méthode sur l'interface `Observable`.

Vous pouvez utiliser la fonction/méthode `pipe()` pour combiner plusieurs opérateurs. Par exemple :

```
import { filter, map } from 'rxjs/operators';
const squareOf2 = of(1, 2, 3, 4, 5,6)
  .pipe(
    filter(num => num % 2 === 0),
    map(num => num * num)
  );
squareOf2.subscribe( (num) => console.log(num));

```

La méthode `of()` créera et retournera un Observable à partir des nombres `1, 2, 3, 4, 5,6` et la méthode `pipe()` appliquera les opérateurs `filter()` et `map()` sur chaque valeur émise.

## Comment les Observables sont Utilisés dans Angular

Angular utilise l'Observable RxJS comme type intégré pour de nombreuses API, telles que :

* Les méthodes `HttpClient` retournent des Observables et les requêtes réelles ne sont envoyées que lorsque vous vous abonnez à l'Observable retourné.
* Le Routeur utilise des Observables à plusieurs endroits tels que :
* les `[events](https://angular.io/api/router/Router#events)` de l'instance du Routeur est un Observable pour écouter les événements sur le routeur.
* De plus, `ActivatedRoute` (qui contient des informations sur la route associée au composant actuellement chargé sur le routeur) a de nombreuses propriétés Observable telles que `params` et `paramMap` pour les paramètres de la route.

Supposons que vous avez un composant Angular et le service Router injecté en tant que `router`. Cet exemple de [StackOverflow](https://stackoverflow.com/questions/33520043/how-to-detect-a-route-change-in-angular) vous montre comment vous pouvez vous abonner aux événements du routeur pour détecter un changement de route :

```
import { Component } from '@angular/core'; 
import { Router, Event, NavigationStart, NavigationEnd, NavigationError } from '@angular/router';
@Component({
    selector: 'app-root',
    template: `<router-outlet></router-outlet>`
})
export class AppComponent {
    constructor(private router: Router) {
        this.router.events.subscribe((event: Event) => {
            if (event instanceof NavigationStart) {
                console.log("Navigation démarrée");
            }
            if (event instanceof NavigationEnd) {
                console.log("Navigation terminée");
            }
            if (event instanceof NavigationError) {

                console.log(event.error);
            }
        });
   }
}     

```

* Le Module Reactive Forms utilise la programmation réactive et les Observables pour écouter les entrées utilisateur.
* Le décorateur `@output()` dans un composant prend une instance d'`EventEmitter`. `EventEmitter` est une sous-classe de l'Observable RxJS.

## Comment Utiliser l'Observable RxJS 6 dans Votre Code Angular

Angular utilise des Observables (implémentés avec la bibliothèque RxJS) pour tous les événements asynchrones. Si vous utilisez Angular CLI 6|7, RxJS 6 sera installé par défaut sur votre projet.

Sinon, vous pouvez l'installer via npm en utilisant :

```
$ npm install rxjs --save 

```

Pour pouvoir utiliser le symbole Observable dans votre code, vous devez d'abord l'importer :

```
import { Observable } from 'rxjs';

```

C'est le nouveau chemin d'importation dans RxJS 6 qui est différent de RxJS 5.

## Travailler avec le Module HttpClient et les Observables

Le nouveau `HttpClient` d'Angular fonctionne avec des Observables par défaut. Les méthodes telles que `get()`, `post()`, `put()` et `delete()` retournent une instance de l'interface Observable.

Les requêtes HTTP ne sont envoyées que lorsque nous nous abonnons à l'Observable.

Voici un exemple de réalisation d'une requête HTTP :

```
getItems(): Observable<Item[]> {
   return this.httpClient.get<Item[]>(this.itemUrl);
}

```

Nous supposons que vous avez injecté le service `HttpClient` en tant que _httpClient_.

## Utilisation de `Observable` avec `AsyncPipe`

Le `AsyncPipe` d'Angular s'abonne à un Observable et retourne les données émises. Par exemple, supposons que nous avons cette méthode :

```
getItems(): Observable {
  this.items$ = this.httpClient.get(this.itemUrl);
}

```

La variable `items$` est de type Observable<Item[]>`.

Après avoir appelé la méthode `getItems()` sur le composant, nous pouvons utiliser le pipe `async` dans le template du composant pour nous abonner à l'Observable retourné :

## S'abonner aux Observables

Les Observables sont utilisés pour une meilleure prise en charge de la gestion des événements, de la programmation asynchrone et de la gestion de plusieurs valeurs. Lorsque vous définissez un Observable pour publier certaines valeurs pour un consommateur, les valeurs ne sont pas émises tant que vous ne vous abonnez pas réellement à l'Observable.

Le consommateur qui s'abonne à l'Observable continue de recevoir des valeurs jusqu'à ce que l'Observable soit complété ou que le consommateur se désabonne de l'Observable.

Commençons par définir un Observable qui fournit un flux de mises à jour

## Utilisation de l'opérateur `map()`

L'opérateur `map()` est similaire à la méthode `Array.map()`. Il vous permet de mapper les réponses de l'Observable à d'autres valeurs. Par exemple :

```
import { Observable} from 'rxjs';
import { map } from 'rxjs/operators';
getItems(): Observable> {
  return this.aService.getItems().pipe(map(response => response.data));
}

```

La méthode `getItems()` retourne un Observable. Nous utilisons l'opérateur `map()` pour retourner la propriété `data` de l'objet de réponse.

L'opérateur nous permet de mapper la réponse du flux Observable à la valeur `data`.

Nous importons l'opérateur `map()` depuis le package `rxjs/operators` et nous utilisons la méthode `pipe()` (qui prend un nombre variable d'opérateurs) pour envelopper l'opérateur.

## Utilisation de l'opérateur `filter()`

L'opérateur `filter()` est similaire à la méthode `Array.filter()`. Il vous permet de filtrer le flux Observable et retourne un autre Observable. Par exemple :

```
import { Observable} from 'rxjs';
import { filter } from 'rxjs/operators';

filter(): Observable<Array<any>> {
  
  return this.aService.getItems()
    .pipe(
      filter(response => response.code === 200));
}

```

Nous utilisons l'opérateur `filter()` pour n'émettre une notification aux observateurs du flux Observable que lorsque le code de statut de la réponse HTTP est 200.

## Conclusion



Dans ce tutoriel, vous avez été introduit à la programmation réactive, aux flux de données et à RxJS 6.

Vous avez appris que la programmation réactive consiste à coder avec des flux de données asynchrones et que RxJS est l'implémentation la plus populaire qui implémente les Observables et le modèle d'observateur.

Vous avez appris ce qu'est un Observable — Un objet qui émet ou publie des valeurs au fil du temps et de manière asynchrone.

Vous avez appris les concepts liés aux Observables tels que les Observers et les Subscriptions — Les Observers sont des objets qui écoutent et consomment les valeurs publiées par un Observable et les Subscriptions sont les objets retournés par la méthode `subscribe()` (ils sont généralement utilisés pour désabonner l'Observer de l'Observable).

Vous avez également appris les types spéciaux d'Observables tels que les Subjects, les behavior Subjects (`BehaviorSubject`) et les replay Subjects (`ReplaySubject`) ainsi que la différence entre les Observables unicast et multicast. Pour rappel, un Observable multicast partage son exécution entre tous ses Observers.

Vous avez appris les Observables cold et hot — hot fait référence à lorsque l'Observable commence à publier des valeurs lorsqu'il est créé, même avant d'obtenir des abonnements.

Vous avez appris les opérateurs RxJS qui sont des méthodes utilisées pour composer des Observables et travailler sur leurs flux de données.

Enfin, vous avez appris qu'Angular 6 & 7 utilise RxJS v6 pour travailler avec des opérations asynchrones et des API (au lieu de callbacks ou de Promesses) dans de nombreux modules couramment utilisés tels que `HttpClient`, `Router` et `ReactiveForms`.

Cet [article](https://www.techiediaries.com/angular-rxjs-tutorial/) a été initialement publié dans [techiediaries](https://www.techiediaries.com/).