---
title: 48 réponses sur StackOverflow aux questions les plus populaires sur Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-11T12:13:18.000Z'
originalURL: https://freecodecamp.org/news/48-answers-on-stack-overflow-to-the-most-popular-angular-questions-52f9eb430ab0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TtrtAMfn2PATB_nD8YpeAA.png
tags:
- name: Angular
  slug: angular
- name: General Programming
  slug: programming
- name: Stack Overflow
  slug: stackoverflow
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 48 réponses sur StackOverflow aux questions les plus populaires sur Angular
seo_desc: 'By Shlomi Levi

  I gathered the most common questions and answers from Stackoverflow. These questions
  were chosen by the highest score received. Whether you are an expert or a beginner,
  you can learn from others’ experiences.

  Table of Contents


  Angular...'
---

Par Shlomi Levi

J'ai rassemblé les questions et réponses les plus courantes de Stackoverflow. Ces questions ont été choisies en fonction du score le plus élevé reçu. Que vous soyez un expert ou un débutant, vous pouvez apprendre des expériences des autres.

### Table des matières

* [Angular — Promise vs Observable](#heading-promesse-vs-observable)
* [Différence entre Constructor et ngOnInit](#heading-différence-entre-constructeur-et-ngoninit)
* [Impossible de lier à 'ngModel' car ce n'est pas une propriété connue de 'input'](#heading-impossible-de-lier-à-ngmodel-car-ce-nest-pas-une-propriété-connue-de-input)
* [Liaison HTML Angular](#heading-liaison-html-angular)
* [Angular/RxJs Quand dois-je me désabonner de `Subscription`](#heading-angularrxjs-quand-dois-je-me-désabonner-de-subscription)
* [Comment puis-je sélectionner un élément dans un modèle de composant ?](#heading-comment-puis-je-sélectionner-un-élément-dans-un-modèle-de-composant)
* [Quelle est l'équivalent de ngShow et ngHide dans Angular ?](#heading-quelle-est-léquivalent-de-ngshow-et-nghide-dans-angular)
* [Comment regrouper une application Angular pour la production](#heading-comment-regrouper-une-application-angular-pour-la-production)
* [BehaviorSubject vs Observable ?](#heading-behaviorsubject-vs-observable)
* [@Directive v/s @Component dans Angular](#heading-directive-vs-component-dans-angular)
* [Angular HTTP GET avec l'erreur TypeScript http.get(...).map n'est pas une fonction dans [null]](#heading-angular-http-get-avec-lerreur-typescript-httpgetmap-nest-pas-une-fonction-dans-null)
* [Comment utiliser jQuery avec Angular ?](#heading-comment-utiliser-jquery-avec-angular)
* [Angular EXCEPTION : Aucun fournisseur pour Http](#heading-angular-exception-aucun-fournisseur-pour-http)
* [Impossible de lier à 'formGroup' car ce n'est pas une propriété connue de 'form'](#heading-impossible-de-lier-à-formgroup-car-ce-nest-pas-une-propriété-connue-de-form)
* [Erreur DI Angular — EXCEPTION : Impossible de résoudre tous les paramètres](#heading-erreur-di-angular-exception-impossible-de-résoudre-tous-les-paramètres)
* [Angular — Définir les en-têtes pour chaque requête](#heading-angular-définir-les-en-têtes-pour-chaque-requête)
* [Comment utiliser *ngIf else dans Angular ?](#heading-comment-utiliser-ngif-else-dans-angular)
* [Angular aucun fournisseur pour NameService](#heading-angular-aucun-fournisseur-pour-nameservice)
* [Liaison de l'élément select à l'objet dans Angular](#heading-liaison-de-lélément-select-à-lobjet-dans-angular)
* [Quelle est la différence entre declarations, providers et import dans NgModule](#heading-quelle-est-la-différence-entre-declarations-providers-et-import-dans-ngmodule)
* [Dans Angular, comment déterminer la route active ?](#heading-dans-angular-comment-déterminer-la-route-active)
* [Options SASS de l'interface de ligne de commande Angular](#heading-options-sass-de-linterface-de-ligne-de-commande-angular)
* [Déclenchement de la détection de changement manuellement dans Angular](#heading-déclenchement-de-la-détection-de-changement-manuellement-dans-angular)
* [Angular et Typescript : Impossible de trouver les noms](#heading-angular-et-typescript-impossible-de-trouver-les-noms)
* [Angular — Que signifient module.id dans le composant ?](#heading-angular-que-signifient-moduleid-dans-le-composant)
* [Comment puis-je obtenir une nouvelle sélection dans « select » dans Angular 2 ?](#heading-comment-puis-je-obtenir-une-nouvelle-sélection-dans-select-dans-angular-2)
* [Exception Angular : Impossible de lier à 'ngForIn' car ce n'est pas une propriété native connue](#heading-exception-angular-impossible-de-lier-à-ngforin-car-ce-nest-pas-une-propriété-native-connue)
* [*ngIf et *ngFor sur le même élément provoquant une erreur](#heading-ngif-et-ngfor-sur-le-même-élément-provoquant-une-erreur)
* [Quelle est l'équivalent Angular à un $watch AngularJS ?](#heading-quelle-est-léquivalent-angular-à-un-watch-angularjs)
* [Importation de lodash dans une application angular2 + typescript](#heading-importation-de-lodash-dans-une-application-angular2-typescript)
* [Comment détecter un changement de route dans Angular ?](#heading-comment-détecter-un-changement-de-route-dans-angular)
* [Événements globaux dans Angular](#heading-événements-globaux-dans-angular)
* [Quelles sont les différences entre SystemJS et Webpack ?](#heading-quelles-sont-les-différences-entre-systemjs-et-webpack)
* [Angular : Impossible de trouver Promise, Map, Set et Iterator](#heading-angular-impossible-de-trouver-promise-map-set-et-iterator)
* [Angular RC4 — Angular ^2.0.0 avec Typescript 2.0.0](#heading-angular-rc4-angular-200-avec-typescript-200)
* [Comment détecter lorsqu'une valeur @Input() change dans Angular ?](#heading-comment-détecter-lorsquune-valeur-input-change-dans-angular)
* [Comment passer des arguments d'URL (chaîne de requête) à une requête HTTP sur Angular](#heading-comment-passer-des-arguments-durl-chaîne-de-requête-à-une-requête-http-sur-angular)
* [Comment déployez-vous des applications Angular ?](#heading-comment-déployez-vous-des-applications-angular)
* [ngFor avec index comme valeur dans l'attribut](#heading-ngfor-avec-index-comme-valeur-dans-lattribut)
* [Définir des constantes globales dans Angular 2](#heading-définir-des-constantes-globales-dans-angular-2)
* [Angular — Utiliser des pipes dans les services et les composants](#heading-angular-utiliser-des-pipes-dans-les-services-et-les-composants)
* [Exception Angular2 : Impossible de lier à 'routerLink' car ce n'est pas une propriété native connue](#heading-exception-angular2-impossible-de-lier-à-routerlink-car-ce-nest-pas-une-propriété-native-connue)
* [Angular 2 onglets dynamiques avec des composants choisis par l'utilisateur](#heading-angular-2-onglets-dynamiques-avec-des-composants-choisis-par-lutilisateur)
* [Délégation : EventEmitter ou Observable dans Angular](#heading-délégation-eventemitter-ou-observable-dans-angular)
* [Comment ajouter bootstrap à un projet angular-cli](#heading-comment-ajouter-bootstrap-à-un-projet-angular-cli)
* [accéder à la clé et à la valeur de l'objet en utilisant *ngFor](#heading-accéder-à-la-clé-et-à-la-valeur-de-lobjet-en-utilisant-ngfor)
* [Exception Angular : Impossible de lier à 'ngFor' car ce n'est pas une propriété native connue](#heading-exception-angular-impossible-de-lier-à-ngfor-car-ce-nest-pas-une-propriété-native-connue)
* [Comment ajouter font-awesome à un projet Angular 2 + CLI](#heading-comment-ajouter-font-awesome-à-un-projet-angular-2-cli)
* [Différence entre HTTP et HTTPClient dans angular 4 ?](#heading-différence-entre-http-et-httpclient-dans-angular-4)

**Profitez-en !**

### Angular — Promise vs Observable

> 551+ points _? 1_50,497+ vues   
> _**[Rohit](https://stackoverflow.com/users/6364715/rohit) a demandé,**_

Quelqu'un peut-il expliquer la différence entre `Promise` et `Observable` dans Angular ?

Un exemple pour chaque serait utile pour comprendre les deux cas. Dans quel scénario peut-on utiliser chaque cas ?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (686+ points)_**

**Promise**

Une `Promise` gère un **événement unique** lorsqu'une opération asynchrone se termine ou échoue.

Note : Il existe des bibliothèques `Promise` qui supportent l'annulation, mais ES6 `Promise` ne le fait pas pour l'instant.

**Observable**

Un `Observable` est comme un `**Stream**` (dans de nombreux langages) et permet de passer zéro ou plusieurs événements où la fonction de rappel est appelée pour chaque événement.

Souvent, `Observable` est préféré à `Promise` car il fournit les fonctionnalités de `Promise` et plus encore. Avec `Observable`, peu importe si vous voulez gérer 0, 1 ou plusieurs événements. Vous pouvez utiliser la même API dans chaque cas.

`Observable` a également l'avantage sur `Promise` d'être **annulable**. Si le résultat d'une requête HTTP à un serveur ou d'une autre opération asynchrone coûteuse n'est plus nécessaire, la `Subscription` d'un `Observable` permet d'annuler l'abonnement, tandis qu'une `Promise` appellera éventuellement la fonction de rappel de succès ou d'échec même lorsque vous n'avez plus besoin de la notification ou du résultat qu'elle fournit.

Observable fournit des **opérateurs** comme `map`, `forEach`, `reduce`, ... similaires à un tableau

Il existe également des opérateurs puissants comme `retry()`, ou `replay()`, ... qui sont souvent très pratiques.

[**Source**](https://stackoverflow.com/questions/37364973)  
**[Haut](#599b)**

### Différence entre Constructor et ngOnInit

> 444+ points _? 1_90,166+ vues   
> _**[Haseena P A](https://stackoverflow.com/users/4029338/haseena-p-a) a demandé,**_

Angular fournit le hook de cycle de vie `ngOnInit` par défaut.

Pourquoi devrait-on utiliser `ngOnInit`, si nous avons déjà un `constructor` ?

> [**_Pardeep Jain_**](https://stackoverflow.com/users/5043867) **_a répondu, (512+ points)_**

Le `Constructor` est une méthode par défaut de la classe qui est exécutée lorsque la classe est instanciée et assure l'initialisation correcte des champs dans la classe et ses sous-classes. Angular ou mieux l'injecteur de dépendances (DI) analyse les paramètres du constructeur et lorsqu'il crée une nouvelle instance en appelant `new MyClass()` il essaie de trouver des fournisseurs qui correspondent aux types des paramètres du constructeur, les résout et les passe au constructeur comme

```js
new MyClass(someArg);
```

`ngOnInit` est un hook de cycle de vie appelé par Angular2 pour indiquer qu'Angular a terminé la création du composant.

Nous devons importer `OnInit` afin de l'utiliser comme ceci (en fait, l'implémentation de `OnInit` n'est pas obligatoire mais considérée comme une bonne pratique) :

```js
import {Component, OnInit} from '@angular/core';
```

puis pour utiliser la méthode de `OnInit`, nous devons l'implémenter dans la classe comme ceci.

```js
export class App implements OnInit{
  constructor(){
     // appelé la première fois avant le ngOnInit()
  }
  
  ngOnInit(){
     // appelé après le constructeur et appelé après le premier ngOnChanges() 
  }
}
```

`Implémentez cette interface pour exécuter une logique d'initialisation personnalisée après que les propriétés liées aux données de votre directive ont été initialisées. ngOnInit est appelé juste après que les propriétés liées aux données de la directive ont été vérifiées pour la première fois, et avant que l'un de ses enfants ait été vérifié. Il est invoqué une seule fois lorsque la directive est instanciée.`

La plupart du temps, nous utilisons `ngOnInit` pour toutes les initialisations/déclarations et évitons de faire des choses dans le constructeur. Le constructeur ne doit être utilisé que pour initialiser les membres de la classe mais ne doit pas faire de "travail" réel.

Ainsi, vous devriez utiliser `constructor()` pour configurer l'injection de dépendances et pas grand-chose d'autre. ngOnInit() est un meilleur endroit pour "démarrer" - c'est là/quand les liaisons des composants sont résolues.

Pour plus d'informations, consultez ici :

* [https://angular.io/api/core/OnInit](https://angular.io/api/core/OnInit)
* [Angular 2 Component Constructor Vs OnInit](https://stackoverflow.com/a/35846307/5043867)

[**Source**](https://stackoverflow.com/questions/35763730)  
**[Haut](#599b)**

### Impossible de lier à 'ngModel' car ce n'est pas une propriété connue de 'input'

> 442+ points _? 2_46,901+ vues   
> _**[abreneliere](https://stackoverflow.com/users/3433751/anthony-breneli%C3%A8re) a demandé,**_

J'ai l'erreur suivante lors du lancement de mon application Angular, même si le composant n'est pas affiché.

Je dois commenter le code pour que mon application fonctionne.

```bash
zone.js:461 Unhandled Promise rejection: Template parse errors:
Can't bind to 'ngModel' since it isn't a known property of 'input'. ("
    <div>
        <label>Created:</label>
        <input  type="text" [ERROR ->][(ngModel)]="test" placeholder="foo" />
    </div>
</div>"): InterventionDetails@4:28 ; Zone: <root> ; Task: Promise.then ; Value:
```

Je regarde le Hero plucker mais je ne vois aucune différence.

Voici le fichier du composant :

```js
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Intervention } from '../../model/intervention';

@Component({
    selector: 'intervention-details',
    templateUrl: 'app/intervention/details/intervention.details.html',
    styleUrls: ['app/intervention/details/intervention.details.css']
})

export class InterventionDetails
{
    @Input() intervention: Intervention;
    public test : string = "toto";
}
```

> [**_abreneliere_**](https://stackoverflow.com/users/3433751) **_a répondu, (674+ points)_**

Oui, c'est ça, dans le fichier app.module.ts, j'ai simplement ajouté :

```js
import { FormsModule } from '@angular/forms';

[...]

@NgModule({
  imports: [
    [...]
    FormsModule
  ],
  [...]
})
```

[**Source**](https://stackoverflow.com/questions/38892771)  
**[Haut](#599b)**

### Liaison HTML Angular

> 385+ points _? 2_27,115+ vues   
> _**[Aviad P.](https://stackoverflow.com/users/3433751/anthony-breneli%C3%A8re) a demandé,**_

Je développe une application Angular et j'ai une réponse HTML que je souhaite afficher. Comment faire ? Si j'utilise simplement la syntaxe de liaison `{{myVal}}`, elle encode tous les caractères HTML (bien sûr).

J'ai besoin de lier le HTML interne d'une div à la valeur de la variable.

> [**_prolink007_**](https://stackoverflow.com/users/427763) **_a répondu, (691+ points)_**

La syntaxe correcte est maintenant la suivante :

```html
<div [innerHTML]="theHtmlString"></div>
```

Fonctionne dans la version `5.2.6`

[Référence de la documentation](https://angular.io/docs/ts/latest/guide/template-syntax.html#!#property-binding-or-interpolation-)

[**Source**](https://stackoverflow.com/questions/31548311)  
**[Haut](#599b)**

### Angular/RxJs Quand dois-je me désabonner de `Subscription`

> 320+ points _? 6_9,606+ vues   
> _**[Sergey Tihon](https://stackoverflow.com/users/1429493/sergey-tihon) a demandé,**_

Quand dois-je stocker les instances de `Subscription` et invoquer `unsubscribe()` pendant le cycle de vie NgOnDestroy et quand puis-je simplement les ignorer ?

Enregistrer toutes les subscriptions introduit beaucoup de désordre dans le code du composant.

[Guide du client HTTP](https://angular.io/docs/ts/latest/guide/server-communication.html) ignore les subscriptions comme ceci :

```js
getHeroes() {
  this.heroService.getHeroes()
                   .subscribe(
                     heroes => this.heroes = heroes,
                     error =>  this.errorMessage = <any>error);
}
```

En même temps, le [Guide de routage et de navigation](https://angular.io/docs/ts/latest/guide/router.html) dit que :

`Eventuellement, nous naviguerons ailleurs. Le routeur supprimera ce composant du DOM et le détruira. Nous devons nettoyer après nous avant que cela ne se produise. Plus précisément, nous devons nous désabonner avant qu'Angular ne détruise le composant. Ne pas le faire pourrait créer une fuite de mémoire.`

`Nous nous désabonnons de notre Observable dans la méthode ngOnDestroy.`

```js
private sub: any;

ngOnInit() {
  this.sub = this.route.params.subscribe(params => {
     let id = +params['id']; // (+) convertit la chaîne 'id' en un nombre
     this.service.getHero(id).then(hero => this.hero = hero);
   });
}

ngOnDestroy() {
  this.sub.unsubscribe();
}
```

> [**_seangwright_**](https://stackoverflow.com/users/939634) **_a répondu, (508+ points)_**

####   Edit 3  La solution Officielle (2017/04/09)

J'ai parlé avec Ward Bell de cette question à NGConf (je lui ai même montré cette réponse qu'il a dit être correcte) mais il m'a dit que l'équipe de documentation pour Angular avait une solution à cette question qui n'est pas publiée (bien qu'ils travaillent à obtenir son approbation). Il m'a également dit que je pouvais mettre à jour ma réponse SO avec la recommandation officielle à venir.

La solution que nous devrions tous utiliser à l'avenir est d'ajouter un champ `private ngUnsubscribe: Subject = new Subject();` à tous les composants qui ont des appels `.subscribe()` à des `Observable` dans leur code de classe.

Nous appelons ensuite `this.ngUnsubscribe.next(); this.ngUnsubscribe.complete();` dans nos méthodes `ngOnDestroy()`.

Le secret (comme déjà noté par [@metamaker](https://stackoverflow.com/a/42695571/939634)) est d'appeler `.takeUntil(this.ngUnsubscribe)` avant chacun de nos appels `.subscribe()` ce qui garantira que toutes les subscriptions seront nettoyées lorsque le composant sera détruit.

Exemple :

```js
import { Component, OnDestroy, OnInit } from '@angular/core';
import 'rxjs/add/operator/takeUntil';
// import { takeUntil } from 'rxjs/operators'; // pour les opérateurs rxjs ^5.5.0 lettable
import { Subject } from 'rxjs/Subject';

import { MyThingService } from '../my-thing.service';

@Component({
    selector: 'my-thing',
    templateUrl: './my-thing.component.html'
})
export class MyThingComponent implements OnDestroy, OnInit {
    private ngUnsubscribe: Subject = new Subject();
    
    constructor(
        private myThingService: MyThingService,
    ) { }
    
    ngOnInit() {
        this.myThingService.getThings()
            .takeUntil(this.ngUnsubscribe)
            .subscribe(things => console.log(things));
            
        /* si vous utilisez des opérateurs lettable dans rxjs ^5.5.0
        this.myThingService.getThings()
            .pipe(takeUntil(this.ngUnsubscribe))
            .subscribe(things => console.log(things));
        */
        
        this.myThingService.getOtherThings()
            .takeUntil(this.ngUnsubscribe)
            .subscribe(things => console.log(things));
            
    }
    
    ngOnDestroy() {
        this.ngUnsubscribe.next();
        this.ngUnsubscribe.complete();
    }
}
```

####   Edit 2 (2016/12/28)

**Source 5**

Le didacticiel Angular, le chapitre Routing indique maintenant ce qui suit : « Le routeur gère les observables qu'il fournit et localise les abonnements. Les abonnements sont nettoyés lorsque le composant est détruit, protégeant contre les fuites de mémoire, donc nous n'avons pas besoin de nous désabonner de l'Observable des paramètres de route. » — [Mark Rajcok](https://stackoverflow.com/questions/38008334/angular2-rxjs-when-should-i-unsubscribe-from-subscription/41177163?noredirect=1#comment69909721_41177163)

Voici une [discussion](https://github.com/angular/angular.io/issues/3003#issuecomment-268429065) sur les problèmes GitHub pour la documentation Angular concernant les Observables du routeur où Ward Bell mentionne que la clarification pour tout cela est en cours.

####   Edit 1

**Source 4**

Dans cette [vidéo de NgEurope](https://youtu.be/WWR9nxVx1ec?t=20m32s), Rob Wormald dit également que vous n'avez pas besoin de vous désabonner des Observables du routeur. Il mentionne également le service `http` et `ActivatedRoute.params` dans cette [vidéo de novembre 2016](https://youtu.be/VLGCCpOWFFw?t=33m37s).

####   Réponse originale

**TLDR :**

Pour cette question, il existe (2) types d'`Observables` - **valeur finie** et **valeur infinie**.

Les `Observables` `http` produisent des valeurs **finies** (1) et quelque chose comme un écouteur d'événements DOM `Observables` produit des valeurs **infinies**.

Si vous appelez manuellement `subscribe` (sans utiliser le pipe async), alors `unsubscribe` des `Observables` **infinis**.

Ne vous inquiétez pas pour les **finis**, `RxJs` s'en occupera.

**Source 1**

J'ai suivi une réponse de Rob Wormald dans le Gitter d'Angular [ici](https://gitter.im/angular/angular?at=5681e8fa3c68940269251fa5).

Il déclare (j'ai réorganisé pour plus de clarté et l'emphase est la mienne)

`si c'est **une séquence à valeur unique** (comme une requête http), le **nettoyage manuel est inutile** (en supposant que vous vous abonnez manuellement dans le contrôleur)`

`je devrais dire "si c'est une **séquence qui se termine**" (dont les séquences à valeur unique, à la http, font partie)`

`**si c'est une séquence infinie**, **vous devez vous désabonner** ce que le pipe async fait pour vous`

De plus, il mentionne dans cette [vidéo youtube](https://youtu.be/UHI0AzD_WfY?t=26m42s) sur les Observables qu'ils nettoient après eux-mêmes... dans le contexte des Observables qui se `complètent` (comme les Promesses, qui se complètent toujours car elles produisent toujours 1 valeur et se terminent - nous ne nous sommes jamais inquiétés de nous désabonner des Promesses pour nous assurer qu'elles nettoient les écouteurs d'événements `xhr`, n'est-ce pas ?).

**Source 2**

De plus, dans le [Guide Rangle pour Angular 2](https://angular-2-training-book.rangle.io/handout/observables/disposing_subscriptions_and_releasing_resources.html), on peut lire

`Dans la plupart des cas, nous n'aurons pas besoin d'appeler explicitement la méthode unsubscribe sauf si nous voulons annuler tôt ou si notre Observable a une durée de vie plus longue que notre abonnement. Le comportement par défaut des opérateurs Observable est de disposer de l'abonnement dès que les messages .complete() ou .error() sont publiés. Gardez à l'esprit que RxJS a été conçu pour être utilisé de manière "fire and forget" la plupart du temps.`

Quand la phrase `notre Observable a une durée de vie plus longue que notre abonnement` s'applique-t-elle ?

Elle s'applique lorsqu'un abonnement est créé à l'intérieur d'un composant qui est détruit avant (ou pas "longtemps" avant) que l'`Observable` se termine.

Je comprends cela comme signifiant que si nous nous abonnons à une requête `http` ou à un observable qui émet 10 valeurs et que notre composant est détruit avant que cette requête `http` ne retourne ou que les 10 valeurs n'aient été émises, nous sommes toujours en sécurité !

Lorsque la requête retourne ou que la 10ème valeur est finalement émise, l'`Observable` se terminera et toutes les ressources seront nettoyées.

**Source 3**

Si nous regardons [cet exemple](https://angular-2-training-book.rangle.io/handout/routing/routeparams.html) du même guide Rangle, nous pouvons voir que l'`Abonnement` à `route.params` nécessite bien un `unsubscribe()` car nous ne savons pas quand ces `params` cesseront de changer (émettre de nouvelles valeurs).

Le composant pourrait être détruit en naviguant ailleurs, auquel cas les paramètres de route changeront probablement encore (ils pourraient techniquement changer jusqu'à la fin de l'application) et les ressources allouées dans l'abonnement seraient toujours allouées car il n'y a pas eu de `complétion`.

[**Source**](https://stackoverflow.com/questions/38008334)  
**[Haut](#599b)**

### Comment puis-je sélectionner un élément dans un modèle de composant ?

> 263+ points _? 2_65,966+ vues   
> _**[Aman Gupta](https://stackoverflow.com/users/2748475/aman-gupta) a demandé,**_

Quelqu'un sait-il comment obtenir un élément défini dans un modèle de composant ? Polymer le rend vraiment facile avec `$` et `$$`.

Je me demandais simplement comment faire avec Angular.

Prenons l'exemple du didacticiel :

```js
import {Component} from '@angular/core'

@Component({
    selector:'display'
    template:`
     <input #myname(input)="updateName(myname.value)"/>
     <p>My name : {{myName}}</p>
    `
    
})
export class DisplayComponent {
    myName: string = "Aman";
    updateName(input: String) {
        this.myName = input;
    }
}
```

Comment puis-je obtenir une référence à l'élément `p` ou `input` à partir de la définition de la classe ?

> [**_Brocco_**](https://stackoverflow.com/users/1413538) **_a répondu, (149+ points)_**

Vous pouvez obtenir une référence à l'élément DOM via `ElementRef` en l'injectant dans le constructeur de votre composant :

```js
constructor(myElement: ElementRef) { ... }
```

Docs : [https://angular.io/docs/ts/latest/api/core/index/ElementRef-class.html](https://angular.io/docs/ts/latest/api/core/index/ElementRef-class.html)

[**Source**](https://stackoverflow.com/questions/32693061)  
**[Haut](#599b)**

### Quelle est l'équivalent de ngShow et ngHide dans Angular ?

> 261+ points _? 2_06,651+ vues   
> **[Mihai Răducanu](https://stackoverflow.com/users/2870735/mihai-r%C4%83ducanu)** _**a demandé,**_

J'ai un certain nombre d'éléments que je souhaite rendre visibles sous certaines conditions.

Dans AngularJS, j'écrirais

```html
<div ng-show="myVar">stuff</div>
```

Comment puis-je faire cela dans Angular ?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (445+ points)_**

Il suffit de lier à la propriété `hidden`

```html
[hidden]="!myVar"
```

Voir aussi

* [https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/hidden)

**problèmes**

`hidden` a quelques problèmes car il peut entrer en conflit avec le CSS pour la propriété `display`.

Voir comment `some` dans [**Exemple Plunker**](https://plnkr.co/edit/SO3c3UUT3LBvhNAeriCz?p=preview) ne se cache pas car il a un style

```css
:host {display: block;}
```

défini. (Cela peut se comporter différemment dans d'autres navigateurs — j'ai testé avec Chrome 50)

**solution de contournement**

Vous pouvez le corriger en ajoutant

```css
[hidden] { display: none !important;}
```

À un style global dans `index.html`.

**un autre piège**

```html
hidden="false"
hidden="{{false}}"
hidden="{{isHidden}}" // isHidden = false;
```

sont les mêmes que

```html
hidden="true"
```

et ne montreront pas l'élément.

`hidden="false"` assignera la chaîne `"false"` qui est considérée comme vraie.  
Seule la valeur `false` ou la suppression de l'attribut rendra réellement l'élément visible.

L'utilisation de `{{}}` convertit également l'expression en une chaîne et ne fonctionnera pas comme prévu.

Seule la liaison avec `[]` fonctionnera comme prévu car ce `false` est assigné comme `false` au lieu de `"false"`.

`***ngIf**` **vs `[hidden]`**

`*ngIf` supprime effectivement son contenu du DOM tandis que `[hidden]` modifie la propriété `display` et indique simplement au navigateur de ne pas afficher le contenu, mais le DOM le contient toujours.

[**Source**](https://stackoverflow.com/questions/35578083)  
**[Haut](#599b)**

### Comment regrouper une application Angular pour la production

> 258+ points _? 1_11,603+ vues   
> _**[Pat M](https://stackoverflow.com/users/4155124/pat-m) a demandé,**_

Je souhaite suivre et mettre à jour dans ce fil la meilleure méthode (et espérons la plus simple) pour regrouper Angular (version 2, 4, ...) pour la production sur un serveur web en direct.

Veuillez inclure la version d'Angular dans les réponses afin que nous puissions mieux suivre les versions ultérieures.

> [**_Nicolas Henneaux_**](https://stackoverflow.com/users/1630604) **_a répondu, (267+ points)_**

#### `2.x, 4.x, 5.x` (TypeScript) avec Angular CLI

#### Configuration initiale

* `npm install -g @angular/cli`
* `ng new projectFolder` crée une nouvelle application

#### Étape de regroupement

* `ng build --prod` (exécuter en ligne de commande lorsque le répertoire est `projectFolder`)
* _le flag `prod` regroupe pour la production (voir la [documentation Angular](https://github.com/angular/angular-cli/wiki/build#--dev-vs---prod-builds) pour la liste des options incluses avec le flag de production)._
* Compresser en utilisant la [compression Brotli](https://en.wikipedia.org/wiki/Brotli) les ressources en utilisant la commande suivante `for i in dist/*; do brotli $i; done`

_les regroupements sont générés par défaut dans **projectFolder/dist/**_

#### Sortie

_Tailles avec Angular `5.2.8` avec CLI `1.7.2`_

* `dist/main.[hash].bundle.js` Votre application regroupée [ taille : 151 KB pour une nouvelle application Angular CLI vide, **36 KB** compressée].
* `dist/polyfill.[hash].bundle.js` les dépendances polyfill (@angular, RxJS...) regroupées [ taille : 58 KB pour une nouvelle application Angular CLI vide, **17 KB** compressée].
* `dist/index.html` point d'entrée de votre application.
* `dist/inline.[hash].bundle.js` chargeur webpack
* `dist/style.[hash].bundle.css` les définitions de style
* `dist/assets` ressources copiées à partir de la configuration des assets de l'interface de ligne de commande Angular

#### Déploiement

Vous pouvez obtenir un aperçu de votre application en utilisant la commande `ng serve --prod` qui démarre un serveur HTTP local de sorte que l'application avec les fichiers de production soit accessible en utilisant [http://localhost:4200](http://localhost:4200).

Pour une utilisation en production, vous devez déployer tous les fichiers du dossier `dist` dans le serveur HTTP de votre choix.

[**Source**](https://stackoverflow.com/questions/37631098)  
**[Haut](#599b)**

### BehaviorSubject vs Observable ?

> 250+ points _? 1_22,248+ vues   
> _**[Kevin Mark](https://stackoverflow.com/users/6620551/kevin-mark) a demandé,**_

Je m'intéresse aux motifs Angular RxJs et je ne comprends pas la différence entre un BehaviorSubject et un Observable.

D'après ma compréhension, un BehaviorSubject est une valeur qui peut changer au fil du temps (peut être souscrite et les abonnés peuvent recevoir des résultats mis à jour). Cela semble être exactement le même objectif qu'un Observable.

Quand utiliseriez-vous un Observable par rapport à un BehaviorSubject ? Y a-t-il des avantages à utiliser un BehaviorSubject plutôt qu'un Observable ou vice versa ?

> [**_Shantanu Bhadoria_**](https://stackoverflow.com/users/3070452) **_a répondu, (425+ points)_**

BehaviorSubject est un type de sujet, un sujet est un type spécial d'observable donc vous pouvez vous abonner aux messages comme tout autre observable. Les caractéristiques uniques de BehaviorSubject sont :

* Il a besoin d'une valeur initiale car il doit toujours retourner une valeur lors de l'abonnement même s'il n'a pas reçu de `next()`
* Lors de l'abonnement, il retourne la dernière valeur du sujet. Un observable régulier ne se déclenche que lorsqu'il reçoit un `onnext`
* à tout moment, vous pouvez récupérer la dernière valeur du sujet dans un code non observable en utilisant la méthode `getValue()`.

Caractéristiques uniques d'un sujet par rapport à un observable :

* Il est un observateur en plus d'être un observable, donc vous pouvez également envoyer des valeurs à un sujet en plus de vous y abonner.

De plus, vous pouvez obtenir un observable à partir d'un sujet de comportement en utilisant la méthode `asobservable()` sur BehaviorSubject.

Observable est un générique, et BehaviorSubject est techniquement un sous-type d'Observable car BehaviorSubject est un observable avec des qualités spécifiques.

Exemple avec BehaviorSubject :

```js
// Behavior Subject

// a est une valeur initiale. si il y a un abonnement 
// après cela, il obtiendrait immédiatement la valeur "a"
let bSubject = new BehaviorSubject("a"); 

bSubject.next("b");

bSubject.subscribe((value) => {
  console.log("Subscription got", value); // Subscription got b, 
                                          // ^ Cela ne se produirait pas 
                                          // pour un observable générique 
                                          // ou un sujet générique par défaut
});

bSubject.next("c"); // Subscription got c
bSubject.next("d"); // Subscription got d
```

Exemple 2 avec un sujet régulier :

```js
// Regular Subject

let subject = new Subject(); 

subject.next("b");

subject.subscribe((value) => {
  console.log("Subscription got", value); // Subscription wont get 
                                          // anything at this point
});

subject.next("c"); // Subscription got c
subject.next("d"); // Subscription got d
```

Un observable peut être créé à partir de Subject et BehaviorSubject en utilisant `subject.asobservable()`. La seule différence étant que vous ne pouvez pas envoyer de valeurs à un observable en utilisant la méthode `next()`.

Dans les services Angular, j'utiliserais BehaviorSubject pour un service de données car un service angular s'initialise souvent avant le composant et behavior subject garantit que le composant consommant le service reçoit les dernières données mises à jour même s'il n'y a pas de nouvelles mises à jour depuis l'abonnement du composant à ces données.

[**Source**](https://stackoverflow.com/questions/39494058)  
**[Haut](#599b)**

### @Directive v/s @Component dans Angular

> 239+ points _? 6_1,582+ vues   
> _[**Prasanjit Dey**](https://stackoverflow.com/users/4917853/prasanjit-dey) **a demandé,**_

Quelle est la différence entre `@Component` et `@Directive` dans Angular ? Les deux semblent faire la même tâche et avoir les mêmes attributs.

Quels sont les cas d'utilisation et quand préférer l'un à l'autre ?

> [**_jaker_**](https://stackoverflow.com/users/1771017) **_a répondu, (327+ points)_**

**Une @Component nécessite une vue alors qu'une @Directive n'en a pas besoin.**

### Directives

Je compare une @Directive à une directive Angular 1.0 avec l'option `restrict: 'A'` (Les directives ne sont pas limitées à l'utilisation d'attributs.) Les directives ajoutent un comportement à un élément DOM existant ou à une instance de composant existante. Un cas d'utilisation exemple pour une directive serait de journaliser un clic sur un élément.

```js
import {Directive} from '@angular/core';

@Directive({
    selector: "[logOnClick]",
    hostListeners: {
        'click': 'onClick()',
    },
})

class LogOnClick {
    constructor() {}
    onClick() { console.log('Element clicked!'); }
}
```

Qui serait utilisé comme ceci :

```js
<button logOnClick>I log when clicked!<;/button>
```

### Composants

Un composant, plutôt que d'ajouter/modifier un comportement, crée en fait sa propre vue (hiérarchie d'éléments DOM) avec un comportement attaché. Un cas d'utilisation exemple pour cela pourrait être un composant de carte de contact :

```js
import {Component, View} from '@angular/core';

@Component({
  selector: 'contact-card',
  template: `
    <div>
      <h1>{{name}}</h1>
      <p>{{city}}</p>
    </div>
  `
})
class ContactCard {
  @Input() name: string
  @Input() city: string
  constructor() {}
}
```

Qui serait utilisé comme ceci :

```js
<contact-card [name]="'foo'" [city]="'bar'"></contact-card>
```

`ContactCard` est un composant d'interface utilisateur réutilisable que nous pourrions utiliser n'importe où dans notre application, même dans d'autres composants. Ce sont essentiellement les blocs de construction de l'interface utilisateur de nos applications.

### En résumé

Écrivez un composant lorsque vous voulez créer un ensemble réutilisable d'éléments DOM d'interface utilisateur avec un comportement personnalisé. Écrivez une directive lorsque vous voulez écrire un comportement réutilisable pour compléter les éléments DOM existants.

Sources :

* [Documentation @Directive](https://angular.io/api/core/Directive)
* [Documentation @Component](https://angular.io/api/core/Component)
* [Article de blog utile](http://blog.codeleak.pl/2015/06/angular2hello-world.html)

[**Source**](https://stackoverflow.com/questions/32680244)  
**[Haut](#599b)**

### Angular HTTP GET avec l'erreur TypeScript http.get(...).map n'est pas une fonction dans [null]

> 233+ points _? 1_41,917+ vues   
> _[**Claudiu**](https://stackoverflow.com/users/4834129/claudiu) **a demandé,**_

J'ai un problème avec HTTP dans Angular.

Je veux simplement `GET` une liste `JSON` et l'afficher dans la vue.

#### Classe de service

```js
import {Injectable} from "angular2/core";
import {Hall} from "./hall";
import {Http} from "angular2/http";
@Injectable()
export class HallService {
    public http:Http;
    public static PATH:string = 'app/backend/' 
    
    constructor(http:Http) {
        this.http=http;
    }
    
    getHalls() {
           return this.http.get(HallService.PATH + 'hall.json').map((res:Response) => res.json());
    }
}
```

Et dans le `HallListComponent`, j'appelle la méthode `getHalls` du service :

```js
export class HallListComponent implements OnInit {
    public halls:Hall[];
    public _selectedId:number;
    
    constructor(private _router:Router,
                private _routeParams:RouteParams,
                private _service:HallService) {
        this._selectedId = +_routeParams.get('id');
    }
    
    ngOnInit() {
        this._service.getHalls().subscribe((halls:Hall[])=>{ 
            this.halls=halls;
        });
    }
}
```

Cependant, j'ai obtenu une exception :

`TypeError: this.http.get(...).map is not a function in [null]`

#### hall-center.component

```js
import {Component} from "angular2/core";
import {RouterOutlet} from "angular2/router";
import {HallService} from "./hall.service";
import {RouteConfig} from "angular2/router";
import {HallListComponent} from "./hall-list.component";
import {HallDetailComponent} from "./hall-detail.component";
@Component({
    template:`
        <h2>my app</h2>
        <router-outlet></router-outlet>
    `,
    directives: [RouterOutlet],
    providers: [HallService]
})

@RouteConfig([
    {path: '/',         name: 'HallCenter', component:HallListComponent, useAsDefault:true},
    {path: '/hall-list', name: 'HallList', component:HallListComponent}
])

export class HallCenterComponent{}
```

#### app.component

```js
import {Component} from 'angular2/core';
import {ROUTER_DIRECTIVES} from "angular2/router";
import {RouteConfig} from "angular2/router";
import {HallCenterComponent} from "./hall/hall-center.component";
@Component({
    selector: 'my-app',
    template: `
        <h1>Examenopdracht Factory</h1>
        <a [routerLink]="['HallCenter']">Hall overview</a>
        <router-outlet></router-outlet>
    `,
    directives: [ROUTER_DIRECTIVES]
})

@RouteConfig([
    {path: '/hall-center/...', name:'HallCenter',component:HallCenterComponent,useAsDefault:true}
])
export class AppComponent { }
```

#### tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES5",
    "module": "system",
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "removeComments": false,
    "noImplicitAny": false
  },
  "exclude": [
    "node_modules"
  ]
}
```

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_a répondu, (416+ points)_**

Je pense que vous devez importer ceci :

```js
import 'rxjs/add/operator/map'
```

Ou plus généralement ceci si vous voulez avoir plus de méthodes pour les observables. **ATTENTION : Cela importera tous les 50+ opérateurs et les ajoutera à votre application, affectant ainsi la taille de votre bundle et les temps de chargement.**

```js
import 'rxjs/Rx';
```

Voir [ce problème](https://github.com/angular/angular/issues/5632#issuecomment-167026172) pour plus de détails.

[**Source**](https://stackoverflow.com/questions/34515173)  
**[Haut](#599b)**

### Comment utiliser jQuery avec Angular ?

> 233+ points _? 2_46,869+ vues   
> _**[Waog](https://stackoverflow.com/users/2398523/waog) a demandé,**_

Quelqu'un peut-il me dire comment utiliser **jQuery** avec **Angular** ?

```js
class MyComponent {
    constructor() {
        // comment interroger l'élément DOM à partir d'ici ?
    }
}
```

Je suis conscient qu'il existe des solutions de contournement comme manipuler la _classe_ ou _id_ de l'élément DOM au préalable, mais j'espère une méthode plus propre pour le faire.

> [**_werenskjold_**](https://stackoverflow.com/users/2881743) **_a répondu, (258+ points)_**

Utiliser jQuery à partir d'Angular2 est une brise par rapport à ng1. Si vous utilisez TypeScript, vous pourriez d'abord référencer la définition TypeScript de jQuery.

```bash
tsd install jquery --save
ou
typings install dt~jquery --global --save
```

Les définitions TypeScript ne sont pas requises puisque vous pourriez simplement utiliser `any` comme type pour `$` ou `jQuery`

Dans votre composant Angular, vous devriez référencer un élément DOM à partir du modèle en utilisant `@ViewChild()`. Après que la vue ait été initialisée, vous pouvez utiliser la propriété `nativeElement` de cet objet et la passer à jQuery.

Déclarer `$` (ou `jQuery`) comme JQueryStatic vous donnera une référence typée à jQuery.

```ts
import {bootstrap}    from '@angular/platform-browser-dynamic';
import {Component, ViewChild, ElementRef, AfterViewInit} from '@angular/core';
declare var $:JQueryStatic;

@Component({
    selector: 'ng-chosen',
    template: `<select #selectElem>
        <option *ngFor="#item of items" [value]="item" [selected]="item === selectedValue">{{item}} option</option>
        </select>
        <h4> {{selectedValue}}</h4>`
})
export class NgChosenComponent implements AfterViewInit {
    @ViewChild('selectElem') el:ElementRef;
    items = ['First', 'Second', 'Third'];
    selectedValue = 'Second';
    
    ngAfterViewInit() {
        $(this.el.nativeElement)
            .chosen()
            .on('change', (e, args) => {
                this.selectedValue = args.selected;
            });
    }
}

bootstrap(NgChosenComponent);
```

Cet exemple est disponible sur plunker : [http://plnkr.co/edit/Nq9LnK?p=preview](http://plnkr.co/edit/Nq9LnK?p=preview)

tslint se plaindra que `chosen` n'est pas une propriété de $, pour corriger cela, vous pouvez ajouter une définition à l'interface JQuery dans votre fichier *.d.ts personnalisé

```js
interface JQuery {
    chosen(options?:any):JQuery;
}
```

[**Source**](https://stackoverflow.com/questions/30623825)  
**[Haut](#599b)**

### Angular EXCEPTION : Aucun fournisseur pour Http

> 230+ points _? 1_42,976+ vues   
> _**[daniel](https://stackoverflow.com/users/516389/daniel) a demandé,**_

Je reçois l'erreur `EXCEPTION: No provider for Http!` dans mon application Angular. Qu'est-ce que je fais de mal ?

```ts
import {Http, Headers} from 'angular2/http';
import {Injectable} from 'angular2/core'

@Component({
    selector: 'greetings-ac-app2',
    providers: [],
    templateUrl: 'app/greetings-ac2.html',
    directives: [NgFor, NgModel, NgIf, FORM_DIRECTIVES],
    pipes: []
})
export class GreetingsAcApp2 {
    private str:any;
    
    constructor(http: Http) {
    
        this.str = {str:'test'};
        http.post('http://localhost:18937/account/registeruiduser/',
            JSON.stringify(this.str),
            {
                headers: new Headers({
                    'Content-Type': 'application/json'
                })
            });
```

> [**_Philip Miglinci_**](https://stackoverflow.com/users/2083492) **_a répondu, (381+ points)_**

Importer le HttpModule

```ts
import { HttpModule } from '@angular/http';

@NgModule({
    imports: [ BrowserModule, HttpModule ],
    providers: [],
    declarations: [ AppComponent ],
    bootstrap: [ AppComponent ]
})
export default class AppModule { }

platformBrowserDynamic().bootstrapModule(AppModule);
```

Idéalement, vous divisez ce code en deux fichiers séparés. Pour plus d'informations, lisez :

* [https://angular.io/docs/ts/latest/cookbook/rc4-to-rc5.html](https://angular.io/docs/ts/latest/cookbook/rc4-to-rc5.html)
* [https://angular.io/docs/ts/latest/guide/ngmodule.html](https://angular.io/docs/ts/latest/guide/ngmodule.html)

[**Source**](https://stackoverflow.com/questions/33721276)  
**[Haut](#599b)**

### Impossible de lier à 'formGroup' car ce n'est pas une propriété connue de 'form'

> 227+ points _? 1_27,130+ vues   
> _**[johnnyfittizio](https://stackoverflow.com/users/2433664/francescomussi) a demandé,**_

**LA SITUATION :**

Aidez-moi s'il vous plaît ! J'essaie de créer ce qui devrait être un formulaire très simple dans mon application Angular2 mais peu importe ce que je fais, cela ne fonctionne jamais.

**VERSION ANGULAR :**

Angular 2.0.0 Rc5

**L'ERREUR :**

```
Can't bind to 'formGroup' since it isn't a known property of 'form'
```

![Image](https://cdn-media-1.freecodecamp.org/images/SP8f73A8L3lPs6fS9frNubiN5UEniPY2yj3p)

**LE CODE :**

La vue :

```html
<form [formGroup]="newTaskForm" (submit)="createNewTask()">
    <div class="form-group">
        <label for="name">Name</label>
        <input type="text" name="name" required>
    </div>
     <button type="submit" class="btn btn-default">Submit</button>
</form>
```

Le contrôleur :

```ts
import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder }  from '@angular/forms';
import {FormsModule,ReactiveFormsModule} from '@angular/forms';
import { Task } from './task';

@Component({
    selector: 'task-add',
    templateUrl: 'app/task-add.component.html'
    
})

export class TaskAddComponent {

    newTaskForm: FormGroup;
    
    constructor(fb: FormBuilder) 
    {
        this.newTaskForm = fb.group({
            name: ["", Validators.required]
        });
    }
    
    createNewTask()
    {
        console.log(this.newTaskForm.value)
    }
    
}
```

Le ngModule :

```ts
import { NgModule }      from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule }   from '@angular/forms';

import { routing }        from './app.routing';
import { AppComponent }  from './app.component';
import { TaskService } from './task.service'

@NgModule({
    imports: [ 
        BrowserModule,
        routing,
        FormsModule
    ],
    declarations: [ AppComponent ],
    providers: [
        TaskService
    ],
    bootstrap: [ AppComponent ]
})

export class AppModule { }
```

**LA QUESTION :**

Pourquoi est-ce que je reçois cette erreur ?

Est-ce que j'ai oublié quelque chose ?

> [**_Stefan Svrkota_**](https://stackoverflow.com/users/6677986) **_a répondu, (465+ points)_**

**CORRECTION RC5**

Vous devez `importer { REACTIVE_FORM_DIRECTIVES } depuis '@angular/forms'` dans votre contrôleur et l'ajouter à `directives` dans `@Component`. Cela résoudra le problème.

Après avoir corrigé cela, vous obtiendrez probablement une autre erreur car vous n'avez pas ajouté `formControlName="name"` à votre input dans le formulaire.

**CORRECTION RC6/RC7/Version finale**

Pour corriger cette erreur, vous devez simplement importer `ReactiveFormsModule` depuis `@angular/forms` dans votre module. Voici un exemple de module de base avec l'importation de `ReactiveFormsModule` :

```ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppComponent }  from './app.component';

@NgModule({
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule
    ],
    declarations: [
        AppComponent
    ],
    bootstrap: [AppComponent]
})

export class AppModule { }
```

Pour expliquer davantage, `formGroup` est un sélecteur pour une directive nommée `FormGroupDirective` qui fait partie de `ReactiveFormsModule`, d'où la nécessité de l'importer. Il est utilisé pour lier un `FormGroup` existant à un élément DOM. Vous pouvez en lire plus à ce sujet sur la [page de documentation officielle d'Angular](https://angular.io/docs/ts/latest/api/forms/index/FormGroupDirective-directive.html).

[**Source**](https://stackoverflow.com/questions/39152071)  
**[Haut](#599b)**

### Erreur DI Angular — EXCEPTION : Impossible de résoudre tous les paramètres

> 221+ points _? 1_42,497+ vues   
> _**[Keith Otto](https://stackoverflow.com/users/4321757/keith-otto) a demandé,**_

J'ai construit une application basique dans Angular, mais j'ai rencontré un problème étrange où je ne peux pas injecter un service dans l'un de mes composants. Il s'injecte bien dans les trois autres composants que j'ai créés cependant.

Pour commencer, voici le service :

```ts
import { Injectable } from '@angular/core';

@Injectable()
export class MobileService {
  screenWidth: number;
  screenHeight: number;
  
  constructor() {
    this.screenWidth = window.outerWidth;
    this.screenHeight = window.outerHeight;
    
    window.addEventListener("resize", this.onWindowResize.bind(this) )
  }
  
  onWindowResize(ev: Event) {
    var win = (ev.currentTarget as Window);
    this.screenWidth = win.outerWidth;
    this.screenHeight = win.outerHeight;
  }
  
}
```

Et le composant avec lequel il refuse de fonctionner :

```ts
import { Component, } from '@angular/core';
import { NgClass } from '@angular/common';
import { ROUTER_DIRECTIVES } from '@angular/router';

import {MobileService} from '../';

@Component({
  moduleId: module.id,
  selector: 'pm-header',
  templateUrl: 'header.component.html',
  styleUrls: ['header.component.css'],
  directives: [ROUTER_DIRECTIVES, NgClass],
})
export class HeaderComponent {
  mobileNav: boolean = false;
  
  constructor(public ms: MobileService) {
    console.log(ms);
  }
  
}
```

L'erreur que j'obtiens dans la console du navigateur est la suivante :

`EXCEPTION: Can't resolve all parameters for HeaderComponent: (?).`

J'ai le service dans la fonction de démarrage donc il a un fournisseur. Et il semble que je puisse l'injecter dans le constructeur de n'importe lequel de mes autres composants sans problème.

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (272+ points)_**

Importez-le directement depuis le fichier où il est déclaré au lieu du baril.

Je ne sais pas exactement ce qui cause le problème mais je l'ai vu mentionné plusieurs fois (probablement une sorte de dépendance circulaire).

Cela devrait également être corrigé en changeant l'ordre des exports dans le baril (je ne connais pas les détails, mais cela a également été mentionné)

[**Source**](https://stackoverflow.com/questions/37997824)  
**[Haut](#599b)**

### Angular — Définir les en-têtes pour chaque requête

> 209+ points _? 2_05,557+ vues   
> _**[Avijit Gupta](https://stackoverflow.com/users/4135178/avijit-gupta) a demandé,**_

J'ai besoin de définir certains en-têtes d'autorisation après que l'utilisateur s'est connecté, pour chaque requête suivante.

Pour définir les en-têtes pour une requête particulière,

```ts
import {Headers} from 'angular2/http';
var headers = new Headers();
headers.append(headerName, value);

// HTTP POST utilisant ces en-têtes
this.http.post(url, data, {
  headers: headers
})
// faire quelque chose avec la réponse
```

[Référence](https://auth0.com/blog/2015/10/15/angular-2-series-part-3-using-http/)

Mais il ne serait pas faisable de définir manuellement les en-têtes de requête pour chaque requête de cette manière.

Comment puis-je définir les en-têtes une fois que l'utilisateur s'est connecté, et également les supprimer lors de la déconnexion ?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_a répondu, (283+ points)_**

Pour répondre à votre question, vous pourriez fournir un service qui enveloppe l'objet `Http` original d'Angular. Quelque chose comme décrit ci-dessous.

```ts
import {Injectable} from '@angular/core';
import {Http, Headers} from '@angular/http';

@Injectable()
export class HttpClient {

  constructor(private http: Http) {}
  
  createAuthorizationHeader(headers: Headers) {
    headers.append('Authorization', 'Basic ' +
      btoa('username:password')); 
  }
  
  get(url) {
    let headers = new Headers();
    this.createAuthorizationHeader(headers);
    return this.http.get(url, {
      headers: headers
    });
  }
  
  post(url, data) {
    let headers = new Headers();
    this.createAuthorizationHeader(headers);
    return this.http.post(url, data, {
      headers: headers
    });
  }
}
```

Et au lieu d'injecter l'objet `Http`, vous pourriez injecter celui-ci (`HttpClient`).

```ts
import { HttpClient } from './http-client';

export class MyComponent {
  // Remarquez que nous injectons "notre" HttpClient ici, en le nommant Http pour que ce soit plus facile
  constructor(http: HttpClient) {
    this.http = httpClient;
  }
  
  handleSomething() {
    this.http.post(url, data).subscribe(result => {
        // console.log( result );
    });
  }
}
```

Je pense également que quelque chose pourrait être fait en utilisant des fournisseurs multiples pour la classe `Http` en fournissant votre propre classe étendant la classe `Http`... Voir ce lien : [http://blog.thoughtram.io/angular2/2015/11/23/multi-providers-in-angular-2.html](http://blog.thoughtram.io/angular2/2015/11/23/multi-providers-in-angular-2.html).

[**Source**](https://stackoverflow.com/questions/34464108)  
**[Haut](#599b)**

### Comment utiliser *ngIf else dans Angular ?

> 205+ points _? 2_03,768+ vues   
> _[**kawli norman**](https://stackoverflow.com/users/5486494/kawli-norman) **a demandé,**_

J'utilise Angular et je veux utiliser `*ngIf else` (disponible depuis la version 4) dans cet exemple :

```
<div *ngIf="isValid">
  content here ...
</div>

<div *ngIf="!isValid">
 other content here...
</div>
```

Comment puis-je obtenir le même comportement avec `ngIf else` ?

> [**_Bougarfaoui El houcine_**](https://stackoverflow.com/users/7273246) **_a répondu, (384+ points)_**

**Angular 4 et 5 :**

en utilisant `else` :

```html
<div *ngIf="isValid;else other_content">
    content here ...
</div>

<ng-template #other_content>other content here...</ng-template>
```

you can also use `then else` :

```html
<div *ngIf="isValid;then content else other_content">here is ignored</div>

<ng-template #content>content here...</ng-template>
<ng-template #other_content>other content here...</ng-template>
```

ou `then` seul :

```html
<div *ngIf="isValid;then content"></div>

<ng-template #content>content here...</ng-template>
```

**Démo :**

[**Plunker**](https://plnkr.co/edit/XD5vLvmwTApcaHJ66Is1)

**Détails :**

`<ng-template>` : est l'implémentation propre à Angular de la balise `<template>` qui est [selon MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template) :

`L'élément HTML <template> est un mécanisme pour contenir du contenu côté client qui ne doit pas être rendu lorsque la page est chargée mais peut être instancié ultérieurement pendant l'exécution en utilisant JavaS`cript.

[**Source**](https://stackoverflow.com/questions/43006550)  
**[Haut](#599b)**

### Angular aucun fournisseur pour NameService

> 196+ points _? 1_86,526+ vues   
> _**[M.Svrcek](https://stackoverflow.com/users/2667885/m-svrcek) a demandé,**_

J'ai un problème avec le chargement de la classe dans le composant Angular. J'essaie de résoudre cela depuis longtemps, j'ai même essayé de l'ajouter à un seul fichier. Ce que j'ai est :

**Application.ts**

```ts
/// <reference path="../typings/angular2/angular2.d.ts" />

import {Component,View,bootstrap,NgFor} from "angular2/angular2";
import {NameService} from "./services/NameService";

@Component({
    selector:'my-app',
    injectables: [NameService]
})
@View({
    template:'<h1>Hi {{name}}</h1>' +
    '<p>Friends</p>' +
    '<ul>' +
    '   <li *ng-for="#name of names">{{name}}</li>' +
    '</ul>',
    directives:[NgFor]
})

class MyAppComponent
{
    name:string;
    names:Array<string>;
    
    constructor(nameService:NameService)
    {
        this.name = 'Michal';
        this.names = nameService.getNames();
    }
}
bootstrap(MyAppComponent);
```

**services/NameService.ts**

```ts
export class NameService {
    names: Array<string>;
    constructor() {
        this.names = ["Alice", "Aarav", "Martín", "Shannon", "Ariana", "Kai"];
    }
    getNames()
    {
        return this.names;
    }
}
```

Tout le temps, j'obtiens un message d'erreur disant "No provider for NameService"...

Quelqu'un peut-il m'aider à repérer ce petit problème avec mon code ?

> [**_Klas Mellbourn_**](https://stackoverflow.com/users/46194) **_a répondu, (309+ points)_**

Vous devez utiliser `providers` au lieu de `injectables`

```ts
@Component({
    selector: 'my-app',
    providers: [NameService]
})
```

[Code complet ici](https://github.com/Mellbourn/angular2-step-by-step-guide).

[**Source**](https://stackoverflow.com/questions/30580083)  
**[Haut](#599b)**

### Liaison de l'élément select à l'objet dans Angular

> 194+ points _? 1_97,048+ vues   
> _[**RHarris**](https://stackoverflow.com/users/372296/rharris) **a demandé,**_

Je suis nouveau dans Angular et j'essaie de me mettre à niveau avec la nouvelle façon de faire les choses.

J'aimerais lier un élément select à une liste d'objets — ce qui est assez facile :

```ts
@Component({
   selector: 'myApp',
   template: `<h1>My Application</h1>
              <select [(ngModel)]="selectedValue">
                 <option *ngFor="#c of countries" value="c.id">{{c.name}}</option>
              </select>`
})
export class AppComponent{
    countries = [
       {id: 1, name: "United States"},
       {id: 2, name: "Australia"}
       {id: 3, name: "Canada"}
       {id: 4, name: "Brazil"}
       {id: 5, name: "England"}
     ];
    selectedValue = null;
}
```

Dans ce cas, il semble que selectedValue serait un nombre — l'id de l'élément sélectionné.

Cependant, j'aimerais en fait lier à l'objet country lui-même afin que selectedValue soit l'objet plutôt que simplement l'id. J'ai essayé de changer la valeur de l'option comme ceci :

```ts
<option *ngFor="#c of countries" value="c">{{c.name}}<;/option>
```

mais cela ne semble pas fonctionner. Il semble placer un objet dans ma selectedValue — mais pas l'objet auquel je m'attends. Vous pouvez [voir cela dans mon exemple Plunker](http://plnkr.co/edit/HGRGv33EFwxDsSnELofk?p=preview).

J'ai également essayé de lier à l'événement de changement afin de pouvoir définir l'objet moi-même en fonction de l'id sélectionné ; cependant, il semble que l'événement de changement se déclenche avant que le ngModel lié ne soit mis à jour — ce qui signifie que je n'ai pas accès à la nouvelle valeur sélectionnée à ce moment-là.

Y a-t-il un moyen propre de lier un élément select à un objet avec Angular 2 ?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (361+ points)_**

```ts
<h1>My Application</h1>
<select [(ngModel)]="selectedValue">
  <option *ngFor="let c of countries" [ngValue]="c">{{c.name}}</option>
</select>
```

[**Exemple Plunker**](https://plnkr.co/edit/njGlIV?p=preview)

REMARQUE : vous pouvez utiliser `[ngValue]="c"` au lieu de `[ngValue]="c.id"` où c est l'objet country complet.

`[value]="..."` ne supporte que les valeurs de chaîne  
`[ngValue]="..."` supporte n'importe quel type

**mise à jour**

Si la `value` est un objet, l'instance présélectionnée doit être identique à l'une des valeurs.

Voir aussi la comparaison personnalisée récemment ajoutée [https://github.com/angular/angular/issues/13268](https://github.com/angular/angular/issues/13268) **disponible depuis 4.0.0-beta.7**

```ts
<select [compareWith]="compareFn" ...
```

Faites attention si vous souhaitez accéder à `this` dans `compareFn`.

```ts
compareFn = this._compareFn.bind(this);

// ou 
// compareFn = (a, b) => this._compareFn(a, b);

_comareFn((a, b) {
   if(this.x ...) {
     ...
}
```

[**Source**](https://stackoverflow.com/questions/35945001)  
**[Haut](#599b)**

### Quelle est la différence entre declarations, providers et import dans NgModule

> 188+ points _? 5_5,432+ vues   
> _[**Ramesh Papaganti**](https://stackoverflow.com/users/2822252/ramesh-papaganti) **a demandé,**_

J'essaie de comprendre Angular (parfois appelé Angular2+), puis je suis tombé sur @Module

1. Imports
2. Declarations
3. Providers

En suivant [Angularjs-2 quick start](https://angular.io/guide/quickstart)

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (277+ points)_**

**Concepts Angular**

* `imports` rend les déclarations exportées d'autres modules disponibles dans le module actuel
* `declarations` sont pour rendre les directives (y compris les composants et les pipes) du module actuel disponibles pour d'autres directives dans le module actuel. Les sélecteurs de directives, de composants ou de pipes ne sont correspondants au HTML que s'ils sont déclarés ou importés.
* `providers` sont pour faire connaître les services et les valeurs au DI. Ils sont ajoutés à la portée racine et ils sont injectés dans d'autres services ou directives qui les ont comme dépendance.

Un cas spécial pour `providers` sont les modules chargés paresseusement qui obtiennent leur propre injecteur enfant. `providers` d'un module chargé paresseusement ne sont fournis qu'à ce module chargé paresseusement par défaut (pas toute l'application comme c'est le cas avec les autres modules).

Pour plus de détails sur les modules, voir aussi [https://angular.io/docs/ts/latest/guide/ngmodule.html](https://angular.io/docs/ts/latest/guide/ngmodule.html)

* `exports` rend les composants, directives et pipes disponibles dans les modules qui ajoutent ce module à `imports`. `exports` peut également être utilisé pour ré-exporter des modules tels que CommonModule et FormsModule, ce qui est souvent fait dans les modules partagés.
* `entryComponents` enregistre les composants pour la compilation hors ligne afin qu'ils puissent être utilisés avec `ViewContainerRef.createComponent()`. Les composants utilisés dans les configurations de routeur sont ajoutés implicitement.

**Imports TypeScript (ES2015)**

`import ... from 'foo/bar'` (qui [peut résoudre vers un `index.ts`](https://stackoverflow.com/a/38158884/1175496)) sont pour les imports TypeScript. Vous en avez besoin chaque fois que vous utilisez un identifiant dans un fichier typescript qui est déclaré dans un autre fichier typescript.

Les `@NgModule()` `imports` d'Angular et les `import` TypeScript sont des _concepts entièrement différents_.

Voir aussi [jDriven — Syntaxe d'import TypeScript et ES6](https://blog.jdriven.com/2017/06/typescript-and-es6-import-syntax/)

`La plupart d'entre eux sont en fait une syntaxe de module ECMAScript 2015 (ES6) simple que TypeScript utilise également.`

[**Source**](https://stackoverflow.com/questions/39062930)  
**[Haut](#599b)**

### Dans Angular, comment déterminer la route active ?

> 187+ points _? 1_00,870+ vues   
> _[**Michael Oryl**](https://stackoverflow.com/users/1480995/michael-oryl) **a demandé,**_

**NOTE :** _Il y a de nombreuses réponses différentes ici, et la plupart ont été valides à un moment ou à un autre. Le fait est que ce qui fonctionne a changé plusieurs fois au fur et à mesure que l'équipe Angular a modifié son routeur. La version 3.0 du routeur qui deviendra éventuellement **le** routeur dans Angular casse beaucoup de ces solutions, mais offre une solution très simple. À partir de la RC.3, la solution préférée est d'utiliser `[routerLinkActive]` comme montré dans [cette réponse](https://stackoverflow.com/a/37947435/1480995)._

Dans une application Angular (actuelle dans la version 2.0.0-beta.0 au moment où j'écris ceci), comment déterminer quelle est la route actuellement active ?

Je travaille sur une application qui utilise Bootstrap 4 et j'ai besoin d'un moyen de marquer les liens/boutons de navigation comme actifs lorsque leur composant associé est affiché dans une balise `<router-outp`ut>.

Je me rends compte que je pourrais maintenir l'état moi-même lorsqu'un des boutons est cliqué, mais cela ne couvrirait pas le cas d'avoir plusieurs chemins vers la même route (par exemple un menu de navigation principal ainsi qu'un menu local dans le composant principal).

Toute suggestion ou lien serait apprécié. Merci.

> [**_jessepinho_**](https://stackoverflow.com/users/974981) **_a répondu, (229+ points)_**

Avec le nouveau [routeur Angular](https://github.com/angular/vladivostok), vous pouvez ajouter un attribut `[routerLinkActive]="['your-class-name']"` à tous vos liens :

```
<a [routerLink]="['/home']" [routerLinkActive]="['is-active']">Home</a>
```

Ou le format non-tableau simplifié si une seule classe est nécessaire :

```
<a [routerLink]="['/home']" [routerLinkActive]="'is-active'">Home</a>
```

Voir la [directive `routerLinkActive` mal documentée](https://github.com/angular/angular/blob/ae75e3640a2d9eb1e897a0771d92b976c5a42c75/modules/%40angular/router/src/directives/router_link_active.ts) pour plus d'informations. (Je l'ai surtout compris par essais et erreurs.)

MISE À JOUR : Une meilleure documentation pour la directive `routerLinkActive` peut maintenant être trouvée [ici](https://angular.io/docs/ts/latest/api/router/index/RouterLinkActive-directive.html). (Merci à @Victor Hugo Arango A. dans les commentaires ci-dessous.)

[**Source**](https://stackoverflow.com/questions/34323480)  
**[Haut](#599b)**

### Options SASS de l'interface de ligne de commande Angular

> 187+ points _? 1_06,289+ vues   
> _[**JDillon522**](https://stackoverflow.com/users/2109585/jdillon522) **a demandé,**_

Je suis nouveau dans Angular et je viens de la communauté Ember. J'essaie d'utiliser la nouvelle Angular-CLI basée sur Ember-CLI.

J'ai besoin de savoir la meilleure façon de gérer SASS dans un nouveau projet Angular. J'ai essayé d'utiliser le dépôt [ember-cli-sass](https://github.com/aexmachina/ember-cli-sass) pour voir s'il fonctionnerait puisque plusieurs composants principaux de l'Angular-CLI sont exécutés à partir de modules Ember-CLI.

Cela n'a pas fonctionné mais je ne suis pas sûr si j'ai simplement mal configuré quelque chose.

De plus, quelle est la meilleure façon d'organiser les styles dans un nouveau projet Angular ? Ce serait bien d'avoir le fichier sass dans le même dossier que le composant.

> [**_Mertcan Diken_**](https://stackoverflow.com/users/6265549) **_a répondu, (323+ points)_**

Lorsque vous créez votre projet avec angular cli, essayez ceci :

```bash
ng new My_New_Project --style=sass
```

Cela génère tous vos composants avec des fichiers sass prédéfinis.

Si vous voulez la syntaxe scss, créez votre projet avec :

```bash
ng new My_New_Project --style=scss
```

Si vous changez votre style existant dans votre projet

```bash
ng set defaults.styleExt scss
```

Cli gère le reste.

[**Source**](https://stackoverflow.com/questions/36220256)  
**[Haut](#599b)**

### Déclenchement de la détection de changement manuellement dans Angular

> 186+ points _? 1_02,556+ vues   
> _[**jz87**](https://stackoverflow.com/users/515279/jz87) **a demandé,**_

Je développe un composant Angular qui possède une propriété `Mode(): string`. J'aimerais pouvoir définir cette propriété de manière programmatique, non en réponse à un événement. Le problème est qu'en l'absence d'un événement de navigateur, une liaison de modèle `{{Mode}}` ne se met pas à jour. Existe-t-il un moyen de déclencher cette détection de changement manuellement ?

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_a répondu, (345+ points)_**

Essayez l'une de ces méthodes :

* `[ApplicationRef.tick()](https://angular.io/docs/ts/latest/api/core/index/ApplicationRef-class.html#!#tick-anchor)` - similaire à `$rootScope.$digest()` d'AngularJS -- c'est-à-dire, vérifie l'arbre complet des composants
* `[NgZone.run(callback)](https://angular.io/docs/ts/latest/api/core/index/NgZone-class.html#!#run-anchor)` - similaire à `$rootScope.$apply(callback)` -- c'est-à-dire, évalue la fonction de rappel à l'intérieur de la zone Angular. Je pense, mais je ne suis pas sûr, que cela finit par vérifier l'arbre complet des composants après avoir exécuté la fonction de rappel.
* `[ChangeDetectorRef.detectChanges()](https://angular.io/docs/ts/latest/api/core/index/ChangeDetectorRef-class.html#!#detectChanges-anchor)` - similaire à `$scope.$digest()` -- c'est-à-dire, vérifie uniquement ce composant et ses enfants

Vous pouvez injecter `ApplicationRef`, `NgZone`, ou `ChangeDetectorRef` dans votre composant.

[**Source**](https://stackoverflow.com/questions/34827334)  
**[Haut](#599b)**

### Angular et Typescript : Impossible de trouver les noms

> 184+ points _? 1_81,472+ vues   
> _[**user233232**](https://stackoverflow.com/users/4997649/user233232) **a demandé,**_

J'utilise Angular (version 2) avec TypeScript (version 1.6) et lorsque je compile le code, j'obtiens ces erreurs :

```bash
Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/change_detection/parser/locals.d.ts(4,42): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(1,25): Error TS2304: Cannot find name 'MapConstructor'.
    node_modules/angular2/src/core/facade/collection.d.ts(2,25): Error TS2304: Cannot find name 'SetConstructor'.
    node_modules/angular2/src/core/facade/collection.d.ts(4,27): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(4,39): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(7,9): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(8,30): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(11,43): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(12,27): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(14,23): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(15,25): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/collection.d.ts(94,41): Error TS2304: Cannot find name 'Set'.
    node_modules/angular2/src/core/facade/collection.d.ts(95,22): Error TS2304: Cannot find name 'Set'.
    node_modules/angular2/src/core/facade/collection.d.ts(96,25): Error TS2304: Cannot find name 'Set'.
    node_modules/angular2/src/core/facade/lang.d.ts(1,22): Error TS2304: Cannot find name 'BrowserNodeGlobal'.
    node_modules/angular2/src/core/facade/lang.d.ts(33,59): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/facade/promise.d.ts(1,10): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(3,14): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(8,32): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(9,38): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(10,35): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(10,93): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(11,34): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(12,32): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(12,149): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/facade/promise.d.ts(13,43): Error TS2304: Cannot find name 'Promise'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(72,32): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(74,17): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(78,184): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(83,182): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/element_injector.d.ts(107,37): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/proto_view_factory.d.ts(27,146): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(52,144): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(76,79): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(77,73): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(94,31): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(97,18): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(100,24): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(103,142): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/linker/view.d.ts(104,160): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/render/api.d.ts(281,74): Error TS2304: Cannot find name 'Map'.
    node_modules/angular2/src/core/zone/ng_zone.d.ts(1,37): Error TS2304: Cannot find name 'Zone'.
```

Voici le code :

```ts
import 'reflect-metadata';
import {bootstrap, Component, CORE_DIRECTIVES, FORM_DIRECTIVES} from 'angular2/core';
@Component({
  selector: 'my-app',
  template: '<input type="text" [(ng-model)]="title" /><h1>{{title}}</h1>',
  directives: [ CORE_DIRECTIVES ]
})
class AppComponent {
  title :string;
  
  constructor() {
    this.title = 'hello angular 2';
  }
}
bootstrap(AppComponent);
```

> [**_basarat_**](https://stackoverflow.com/users/390330) **_a répondu, (50+ points)_**

Un problème connu : [https://github.com/angular/angular/issues/4902](https://github.com/angular/angular/issues/4902)

Raison principale : le fichier `.d.ts` implicitement inclus par TypeScript varie avec la cible de compilation, donc il faut avoir plus de déclarations ambiantes lors du ciblage de `es5` même si les choses sont réellement présentes dans les environnements d'exécution (par exemple, chrome). Plus sur `[lib.d.ts](https://basarat.gitbooks.io/typescript/content/docs/types/lib.d.ts.html)`

[**Source**](https://stackoverflow.com/questions/33332394)  
**[Haut](#599b)**

### Angular — Que signifient module.id dans le composant ?

> 181+ points _? 5_4,337+ vues   
> _[**Nishchit Dhanani**](https://stackoverflow.com/users/2837412/nishchit-dhanani) **a demandé,**_

Dans une application Angular, j'ai vu que `@Component` a la propriété `moduleId`. Que signifie-t-elle ?

Et lorsque `module.id` n'est défini nulle part, l'application fonctionne toujours. Comment peut-elle encore fonctionner ?

```ts
@Component({
  moduleId: module.id,
  selector: 'ng-app',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.css'],
  directives: [AppComponent]
});
```

> [**_Nishchit Dhanani_**](https://stackoverflow.com/users/2837412) **_a répondu, (145+ points)_**

La version bêta d'Angular (depuis la version 2-alpha.51) supporte les actifs relatifs pour les composants, comme **templateUrl** et **styleUrls** dans le décorateur `@Component`.

`module.id` fonctionne lors de l'utilisation de CommonJS. Vous n'avez pas à vous soucier de son fonctionnement.

`**Rappel** : définir moduleId: module.id dans le décorateur @Component est la clé ici. Si vous ne l'avez pas, Angular 2 recherchera vos fichiers au niveau racine.`

Source de [l'article de Justin Schwartzenberger](http://schwarty.com/2015/12/22/angular2-relative-paths-for-templateurl-and-styleurls/), merci à [@Pradeep Jain](https://stackoverflow.com/users/5043867/pardeep-jain)

**Mise à jour le 16 septembre 2016 :**

`Si vous utilisez **webpack** pour le bundling, vous n'avez pas besoin de module.id dans le décorateur. Les plugins webpack gèrent automatiquement (l'ajout de) module.id dans le bundle final`

[**Source**](https://stackoverflow.com/questions/37178192)  
**[Haut](#599b)**

### Comment puis-je obtenir une nouvelle sélection dans « select » dans Angular 2 ?

> 175+ points _? 2_03,064+ vues   
> _[**Hongbo Miao**](https://stackoverflow.com/users/2000548/hongbo-miao) **a demandé,**_

J'utilise Angular 2 (TypeScript).

Je veux faire quelque chose pour la nouvelle sélection, mais ce que j'obtiens dans onChange() est toujours la dernière sélection. Comment puis-je obtenir la nouvelle sélection ?

```ts
<select [(ngModel)]="selectedDevice" (change)="onChange($event)">
    <option *ngFor="#i of devices">{{i}}</option>
</select>

onChange($event) {
    console.log(this.selectedDevice);
    // Je veux faire quelque chose ici pour le nouveau selectedDevice, mais ce que j'
    // obtiens ici est toujours la dernière sélection, pas celle que je viens de sélectionner.
}
```

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_a répondu, (370+ points)_**

Si vous n'avez pas besoin de liaison de données bidirectionnelle :

```ts
<select (change)="onChange($event.target.value)">
    <option *ngFor="let i of devices">{{i}}</option>
</select>

onChange(deviceValue) {
    console.log(deviceValue);
}
```

Pour la liaison de données bidirectionnelle, séparez les liaisons d'événements et de propriétés :

```ts
<select [ngModel]="selectedDevice" (ngModelChange)="onChange($event)" name="sel2">
    <option [value]="i" *ngFor="let i of devices">{{i}}</option>
</select>

export class AppComponent {
  devices = 'one two three'.split(' ');
  selectedDevice = 'two';
  onChange(newValue) {
    console.log(newValue);
    this.selectedDevice = newValue;
    // ... faire d'autres choses ici ...
}
```

Si `devices` est un tableau d'objets, liez à `ngValue` au lieu de `value` :

```ts
<select [ngModel]="selectedDeviceObj" (ngModelChange)="onChangeObj($event)" name="sel3">
  <option [ngValue]="i" *ngFor="let i of deviceObjects">{{i.name}}</option>
</select>
{{selectedDeviceObj | json}}

export class AppComponent {
  deviceObjects = [{name: 1}, {name: 2}, {name: 3}];
  selectedDeviceObj = this.deviceObjects[1];
  onChangeObj(newObj) {
    console.log(newObj);
    this.selectedDeviceObj = newObj;
    // ... faire d'autres choses ici ...
  }
}
```

[Plunker](http://plnkr.co/edit/VbJUBkqAlS8UPVgh4bqV?p=preview) — n'utilise pas `<form>`  
[Plunker](http://plnkr.co/edit/pv5j4b1NFyTGFkxHUSga?p=preview) - utilise `<form>` et utilise la nouvelle API de formulaires

[**Source**](https://stackoverflow.com/questions/33700266)  
**[Haut](#599b)**

### Exception Angular : Impossible de lier à 'ngForIn' car ce n'est pas une propriété native connue

> 172+ points _? 4_8,252+ vues   
> _[**Mark Rajcok**](https://stackoverflow.com/users/215945/mark-rajcok) **a demandé,**_

Qu'est-ce que je fais de mal ?

```ts
import {bootstrap, Component} from 'angular2/angular2'

@Component({
  selector: 'conf-talks',
  template: `<div *ngFor="let talk in talks">
     {{talk.title}} by {{talk.speaker}}
     <p>{{talk.description}}
   </div>`
})
class ConfTalks {
  talks = [ {title: 't1', speaker: 'Brian', description: 'talk 1'},
            {title: 't2', speaker: 'Julie', description: 'talk 2'}];
}
@Component({
  selector: 'my-app',
  directives: [ConfTalks],
  template: '<conf-talks></conf-talks>'
})
class App {}
bootstrap(App, [])
```

L'erreur est

```bash
EXCEPTION: Template parse errors:
Can't bind to 'ngForIn' since it isn't a known native property
("<div [ERROR ->]*ngFor="let talk in talks">
```

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_a répondu, (403+ points)_**

Puisque c'est au moins la troisième fois que j'ai perdu plus de 5 min sur ce problème, j'ai pensé que je posterais la Q & A. J'espère que cela aidera quelqu'un d'autre sur la route... probablement moi !

J'ai tapé `in` au lieu de `of` dans l'expression ngFor.

**Avant la version 2-beta.17**, cela devrait être :

```
<div *ngFor="#talk of talks">
```

_À partir de la version beta.17, utilisez la syntaxe `let` au lieu de `#`. Voir la MISE À JOUR plus bas pour plus d'informations._

Notez que la syntaxe ngFor se "désucre" en ce qui suit :

```ts
<template ngFor #talk [ngForOf]="talks">
  <div>...</div>
</template>
```

Si nous utilisons `in` à la place, cela devient

```ts
<template ngFor #talk [ngForIn]="talks">
  <div>...</div>
</template>
```

Puisque `ngForIn` n'est pas une directive d'attribut avec une propriété d'entrée du même nom (comme `ngIf`), Angular essaie alors de voir si c'est une propriété (native connue) de l'élément `template`, et ce n'est pas le cas, d'où l'erreur.

**MISE À JOUR** — à partir de la version 2-beta.17, utilisez la syntaxe `let` au lieu de `#`. Cela se met à jour comme suit :

```
<div *ngFor="let talk of talks">
```

Notez que la syntaxe ngFor se "désucre" en ce qui suit :

```ts
<template ngFor let-talk [ngForOf]="talks">
  <div>...</div>
</template>
```

Si nous utilisons `in` à la place, cela devient

```ts
<template ngFor let-talk [ngForIn]="talks">
  <div>...</div>
</template>
```

[**Source**](https://stackoverflow.com/questions/34561168)  
**[Haut](#599b)**

### *ngIf et *ngFor sur le même élément provoquant une erreur

> 171+ points _? 8_5,728+ vues   
> _**[garethdn](https://stackoverflow.com/users/1128290/garethdn) a demandé,**_

J'ai un problème avec l'utilisation de `*ngFor` et `*ngFor` de Angular sur le même élément.

Lorsque j'essaie de parcourir la collection dans `*ngFor`, la collection est considérée comme `null` et échoue par conséquent lorsque j'essaie d'accéder à ses propriétés dans le modèle.

```ts
@Component({
  selector: 'shell',
  template: `
    <h3>Shell</h3><button (click)="toggle()">Toggle!</button>
    
    <div *ngIf="show" *ngFor="let thing of stuff">
      {{log(thing)}}
      <span>{{thing.name}}</span>
    </div>
  `
})

export class ShellComponent implements OnInit {

  public stuff:any[] = [];
  public show:boolean = false;
  
  constructor() {}
  
  ngOnInit() {
    this.stuff = [
      { name: 'abc', id: 1 },
      { name: 'huo', id: 2 },
      { name: 'bar', id: 3 },
      { name: 'foo', id: 4 },
      { name: 'thing', id: 5 },
      { name: 'other', id: 6 },
    ]
  }
  
  toggle() {
    this.show = !this.show;
  }
  
  log(thing) {
    console.log(thing);
  }
  
}
```

Je sais que la solution facile est de déplacer `*ngIf` d'un niveau, mais pour des scénarios comme la boucle sur les éléments de liste dans un `ul`, je finirais par avoir soit un `li` vide si la collection est vide, soit mes `li` enveloppés dans des éléments conteneurs redondants.

Exemple à cette [plnkr](http://plnkr.co/edit/C5tZ8mD3iWczVvWkWycH?p=preview).

Notez l'erreur de la console :

`EXCEPTION: TypeError: Cannot read property 'name' of null in [{{thing.name}} in ShellComponent@5:12]`

Est-ce que je fais quelque chose de mal ou est-ce un bug ?

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (284+ points)_**

Angular2 ne supporte pas plus d'une directive structurelle sur le même élément.  
En tant que solution de contournement, utilisez l'élément `**<ng-container>**` qui vous permet d'utiliser des éléments séparés pour chaque directive structurelle, mais **il n'est pas estampillé dans le DOM**.

```ts
<ng-container *ngIf="show">
  <div *ngFor="let thing of stuff">
    {{log(thing)}}
    <span>{{thing.name}}</span>
  </div>
</ng-container>
```

`<ng-template>` (`<template>` avant Angular4) permet de faire la même chose mais avec une syntaxe différente qui est confuse et n'est plus recommandée

```ts
<ng-template [ngIf]="show">
  <div *ngFor="let thing of stuff">
    {{log(thing)}}
    <span>{{thing.name}}</span>
  </div>
</ng-template>
```

[**Source**](https://stackoverflow.com/questions/34657821)  
**[Haut](#599b)**

### Quelle est l'équivalent Angular à un $watch AngularJS ?

> 169+ points _? 9_5,029+ vues   
> _[**Erwin**](https://stackoverflow.com/users/1716567/erwin) **a demandé,**_

Dans AngularJS, vous pouviez spécifier des observateurs pour observer les changements dans les variables de portée en utilisant la fonction `$watch` de `$scope`. Quel est l'équivalent pour observer les changements de variables (dans, par exemple, les variables de composant) dans Angular ?

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_a répondu, (226+ points)_**

Dans Angular 2, la détection des changements est automatique... `$scope.$watch()` et `$scope.$digest()` R.I.P.

Malheureusement, la section Détection des changements du guide de développement n'est pas encore écrite (il y a un espace réservé près du bas de la page [Aperçu de l'architecture](https://angular.io/docs/ts/latest/guide/architecture.html), dans la section « Les autres trucs »).

Voici ma compréhension de la façon dont la détection des changements fonctionne :

* Zone.js « patch le monde » — il intercepte toutes les API asynchrones dans le navigateur (lorsque Angular s'exécute). C'est pourquoi nous pouvons utiliser `setTimeout()` à l'intérieur de nos composants plutôt que quelque chose comme `$timeout`... parce que `setTimeout()` est patché.
* Angular construit et maintient un arbre de « détecteurs de changements ». Il y a un tel détecteur de changements (classe) par composant/directive. (Vous pouvez obtenir l'accès à cet objet en injectant `[ChangeDetectorRef](https://angular.io/docs/ts/latest/api/core/index/ChangeDetectorRef-class.html)`.) Ces détecteurs de changements sont créés lorsque Angular crée des composants. Ils gardent une trace de l'état de toutes vos liaisons, pour la vérification des modifications. Ceux-ci sont, en un sens, similaires aux `$watches()` automatiques que Angular 1 mettrait en place pour les liaisons de modèle de template `{{}}`.  
Contrairement à Angular 1, le graphe de détection de changement est un arbre dirigé et ne peut pas avoir de cycles (ce qui rend Angular 2 beaucoup plus performant, comme nous le verrons ci-dessous).
* Lorsqu'un événement se déclenche (à l'intérieur de la zone Angular), le code que nous avons écrit (la fonction de rappel du gestionnaire d'événements) s'exécute. Il peut mettre à jour les données qu'il veut — le modèle/état de l'application partagé et/ou l'état de la vue du composant.
* Après cela, grâce aux hooks ajoutés par Zone.js, il exécute ensuite l'algorithme de détection de changement d'Angular. Par défaut (c'est-à-dire, si vous n'utilisez pas la stratégie de détection de changement `onPush` sur l'un de vos composants), chaque composant de l'arbre est examiné une fois (TTL=1)... de haut en bas, dans l'ordre de profondeur. (Eh bien, si vous êtes en mode dev, la détection de changement s'exécute deux fois (TTL=2). Voir [ApplicationRef.tick()](https://angular.io/docs/ts/latest/api/core/index/ApplicationRef-class.html#!#tick-anchor) pour plus d'informations à ce sujet.) Il effectue une vérification des modifications sur toutes vos liaisons, en utilisant ces objets détecteurs de changement.
* Les hooks de cycle de vie sont appelés dans le cadre de la détection de changement.   
Si les données du composant que vous souhaitez observer sont une propriété d'entrée primitive (String, booléen, nombre), vous pouvez implémenter `ngOnChanges()` pour être notifié des changements.   
Si la propriété d'entrée est un type de référence (objet, tableau, etc.), mais que la référence n'a pas changé (par exemple, vous avez ajouté un élément à un tableau existant), vous devrez implémenter `ngDoCheck()` (voir [cette réponse SO](https://stackoverflow.com/a/34298708/215945) pour plus d'informations à ce sujet).   
Vous ne devriez modifier que les propriétés du composant et/ou les propriétés des composants descendants (en raison de l'implémentation de l'arbre à parcours unique — c'est-à-dire, flux de données unidirectionnel). Voici [un plunker](http://plnkr.co/edit/XWBSvE0NoQlRuOsXuOm0?p=preview) qui viole cela. Les pipes avec état peuvent également [vous tromper](https://stackoverflow.com/questions/34456430/ngfor-doesnt-update-data-with-pipe-in-angular2/34497504#34497504) ici.
* Pour tout changement de liaison trouvé, les composants sont mis à jour, puis le DOM est mis à jour. La détection de changement est maintenant terminée.
* Le navigateur remarque les changements de DOM et met à jour l'écran.

Autres références pour en savoir plus :

* [Le $digest d'Angular renaît dans la nouvelle version d'Angular](https://blog.angularindepth.com/angulars-digest-is-reborn-in-the-newer-version-of-angular-718a961ebd3e) — explique comment les idées d'AngularJS sont mappées à Angular
* [Tout ce que vous devez savoir sur la détection de changement dans Angular](https://blog.angularindepth.com/everything-you-need-to-know-about-change-detection-in-angular-8006c51d206f) — explique en détail comment la détection de changement fonctionne sous le capot
* [Détection de changement expliquée](http://blog.thoughtram.io/angular/2016/02/22/angular-2-change-detection-explained.html) — Blog Thoughtram du 22 février 2016 — probablement la meilleure référence disponible
* Vidéo de Savkin [Détection de changement réinventée](https://www.youtube.com/watch?v=jvKGQSFQf10) — à regarder absolument
* [Comment fonctionne vraiment la détection de changement dans Angular 2 ?](http://blog.jhades.org/how-does-angular-2-change-detection-really-work/)- blog de jhade du 24 février 2016
* [Vidéo de Brian](https://www.youtube.com/watch?v=3IqtmUscE_U) et [vidéo de Miško](https://www.youtube.com/watch?v=V9Bbp6Hh2YE) sur Zone.js. Celle de Brian parle de Zone.js. Celle de Miško parle de la façon dont Angular 2 utilise Zone.js pour implémenter la détection de changement. Il parle également de la détection de changement en général, et un peu de `onPush`.
* Articles de blog de Victor Savkins : [Détection de changement dans Angular 2](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2), [Deux phases des applications Angular 2](http://victorsavkin.com/post/114168430846/two-phases-of-angular-2-applications), [Angular, Immuabilité et Encapsulation](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2). Il couvre beaucoup de terrain rapidement, mais il peut être parfois concis, et vous vous retrouvez à vous gratter la tête, vous demandant quelles sont les pièces manquantes.
* [Détection de changement ultra rapide](https://docs.google.com/document/d/1QKTbyVNPyRW-otJJVauON4TFMHpl0zNBPkJcTcfPJWg/edit) (document Google) — très technique, très concis, mais il décrit/esquisse les classes ChangeDetection qui sont construites dans le cadre de l'arbre

[**Source**](https://stackoverflow.com/questions/34569094)  
**[Haut](#599b)**

### Importation de lodash dans une application angular2 + typescript

> 167+ points _? 1_04,431+ vues   
> _[**Davy**](https://stackoverflow.com/users/1854793/davy) **a demandé,**_

J'ai du mal à importer les modules lodash. J'ai configuré mon projet en utilisant npm+gulp, et je continue à rencontrer le même problème. J'ai essayé le lodash régulier, mais aussi lodash-es.

Le package npm lodash : (a un fichier index.js dans le dossier racine du package)

```ts
import * as _ from 'lodash';
```

Résultat :

```
error TS2307: Cannot find module 'lodash'.
```

Le package npm lodash-es : (a une exportation par défaut dans lodash.js dans le dossier racine du package)

```
import * as _ from 'lodash-es/lodash';
```

Résultat :

```
error TS2307: Cannot find module 'lodash-es'.
```

Gulp et Webstorm signalent tous deux le même problème.

Fait amusant, ceci ne retourne aucune erreur :

```ts
import 'lodash-es/lodash';
```

... mais bien sûr, il n'y a pas de "_"...

Mon fichier tsconfig.json :

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "system",
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "removeComments": false,
    "noImplicitAny": false
  },
  "exclude": [
    "node_modules"
  ]
}
```

Mon fichier gulpfile.js :

```json
var gulp = require('gulp'),
    ts = require('gulp-typescript'),
    uglify = require('gulp-uglify'),
    sourcemaps = require('gulp-sourcemaps'),
    tsPath = 'app/**/*.ts';
    
gulp.task('ts', function () {
    var tscConfig = require('./tsconfig.json');
    
    gulp.src([tsPath])
        .pipe(sourcemaps.init())
        .pipe(ts(tscConfig.compilerOptions))
        .pipe(sourcemaps.write('./../js'));
});

gulp.task('watch', function() {
    gulp.watch([tsPath], ['ts']);
});

gulp.task('default', ['ts', 'watch']);
```

Si je comprends bien, moduleResolution:'node' dans mon tsconfig devrait pointer les instructions d'importation vers le dossier node_modules, où lodash et lodash-es sont installés. J'ai également essayé de nombreuses façons différentes d'importer : chemins absolus, chemins relatifs, mais rien ne semble fonctionner. Des idées ?

Si nécessaire, je peux fournir un petit fichier zip pour illustrer le problème.

> [**_Taytay_**](https://stackoverflow.com/users/544130) **_a répondu, (293+ points)_**

Voici comment faire cela à partir de Typescript 2.0 : (tsd et typings sont en cours de dépréciation au profit de ce qui suit) :

```bash
$ npm install --save lodash

# C'est la nouvelle partie ici : 
$ npm install --save @types/lodash
```

Ensuite, dans votre fichier .ts :

Soit :

```ts
import * as _ from "lodash";
```

Ou (comme suggéré par @Naitik) :

```ts
import _ from "lodash";
```

Je ne suis pas sûr de la différence. Nous utilisons et préférons la première syntaxe. Cependant, certains rapportent que la première syntaxe ne fonctionne pas pour eux, et quelqu'un d'autre a commenté que la syntaxe suivante est incompatible avec les modules webpack chargés paresseusement. YMMV.

Édition du 27 février 2017 :

Selon @Koert ci-dessous, `import * as _ from "lodash";` est la seule syntaxe fonctionnelle à partir de Typescript 2.2.1, lodash 4.17.4, et @types/lodash 4.14.53. Il dit que l'autre syntaxe d'importation suggérée donne l'erreur "has no default export".

[**Source**](https://stackoverflow.com/questions/34660265)  
**[Haut](#599b)**

### Comment détecter un changement de route dans Angular ?

> 160+ points _? 1_08,593+ vues   
> _[**AngularM**](https://stackoverflow.com/users/1590389/angularm) **a demandé,**_

Je cherche à détecter un changement de route dans mon `AppComponent`.

Ensuite, je vérifierai le jeton utilisateur global pour voir s'il est connecté. Ensuite, je pourrai rediriger l'utilisateur s'il n'est pas connecté.

> [**_Ludohen_**](https://stackoverflow.com/users/1048274) **_a répondu, (223+ points)_**

Dans Angular 2, vous pouvez vous `abonner` (événement Rx) à une instance de Router. Vous pouvez donc faire des choses comme

```ts
class MyClass {
  constructor(private router: Router) {
    router.subscribe((val) => /*whatever*/)
  }
}
```

**Édition** (depuis rc.1)

```ts
class MyClass {
  constructor(private router: Router) {
    router.changes.subscribe((val) => /*whatever*/)
  }
}
```

**Édition 2** (depuis 2.0.0)

voir aussi : [Doc Router.events](https://angular.io/api/router/RouterEvent)

```ts
class MyClass {
  constructor(private router: Router) {
    router.events.subscribe((val) => {
        // voir aussi 
        console.log(val instanceof NavigationEnd) 
    });
  }
}
```

[**Source**](https://stackoverflow.com/questions/33520043)  
**[Haut](#599b)**

### Événements globaux dans Angular

> 157+ points _? 8_3,980+ vues   
> _[**skovmand**](https://stackoverflow.com/users/3368477/skovmand) **a demandé,**_

N'y a-t-il pas d'équivalent à `$scope.emit()` ou `$scope.broadcast()` dans Angular ?

Je connais la fonctionnalité `EventEmitter`, mais autant que je sache, elle ne fait qu'émettre un événement vers l'élément HTML parent.

Que faire si je dois communiquer entre des frères ou entre un composant à la racine du DOM et un élément imbriqué à plusieurs niveaux de profondeur ?

> [**_pixelbits_**](https://stackoverflow.com/users/3661630) **_a répondu, (304+ points)_**

Il n'y a pas d'équivalent à `$scope.emit()` ou `$scope.broadcast()` d'AngularJS. EventEmitter à l'intérieur d'un composant s'en approche, mais comme vous l'avez mentionné, il ne fait qu'émettre un événement vers le composant parent immédiat.

Dans Angular, il existe d'autres alternatives que j'essaierai d'expliquer ci-dessous.

Les liaisons @Input() permettent au modèle de l'application d'être connecté dans un graphe d'objets dirigé (de la racine aux feuilles). Le comportement par défaut de la stratégie de détection de changement d'un composant est de propager toutes les modifications à un modèle d'application pour toutes les liaisons de n'importe quel composant connecté.

À part : Il existe deux types de modèles : les modèles de vue et les modèles d'application. Un modèle d'application est connecté via des liaisons @Input(). Un modèle de vue est simplement une propriété de composant (non décorée avec @Input()) qui est liée dans le modèle du composant.

Pour répondre à vos questions :

Que faire si je dois communiquer entre des composants frères ?

1. **Modèle d'application partagé** : Les frères peuvent communiquer via un modèle d'application partagé (comme dans angular 1). Par exemple, lorsqu'un frère apporte une modification à un modèle, l'autre frère qui a des liaisons au même modèle est automatiquement mis à jour.
2. **Événements de composant** : Les composants enfants peuvent émettre un événement vers le composant parent en utilisant des liaisons @Output(). Le composant parent peut gérer l'événement et manipuler le modèle d'application ou son propre modèle de vue. Les modifications apportées au modèle d'application sont automatiquement propagées à tous les composants qui se lient directement ou indirectement au même modèle.
3. **Événements de service** : Les composants peuvent s'abonner aux événements de service. Par exemple, deux composants frères peuvent s'abonner au même événement de service et répondre en modifiant leurs modèles respectifs. Plus d'informations à ce sujet ci-dessous.

Comment puis-je communiquer entre un composant racine et un composant imbriqué à plusieurs niveaux de profondeur ?

1. **Modèle d'application partagé** : Le modèle d'application peut être passé du composant racine aux sous-composants profondément imbriqués via des liaisons @Input(). Les modifications apportées à un modèle par n'importe quel composant seront automatiquement propagées à tous les composants qui partagent le même modèle.
2. **Événements de service** : Vous pouvez également déplacer l'EventEmitter vers un service partagé, ce qui permet à n'importe quel composant d'injecter le service et de s'abonner à l'événement. Ainsi, un composant racine peut appeler une méthode de service (généralement en mutant le modèle), qui à son tour émet un événement. Plusieurs niveaux plus bas, un composant petit-enfant qui a également injecté le service et s'est abonné au même événement peut le gérer. Tout gestionnaire d'événements qui modifie un modèle d'application partagé sera automatiquement propagé à tous les composants qui en dépendent. C'est probablement l'équivalent le plus proche de `$scope.broadcast()` d'Angular 1. La section suivante décrit cette idée plus en détail.

**Exemple d'un service observable qui utilise les événements de service pour propager les changements**

Voici un exemple de service observable qui utilise les événements de service pour propager les changements. Lorsqu'un TodoItem est ajouté, le service émet un événement notifiant ses abonnés de composants.

```ts
export class TodoItem {
    constructor(public name: string, public done: boolean) {
    }
}
export class TodoService {
    public itemAdded$: EventEmitter<TodoItem>;
    private todoList: TodoItem[] = [];
    
    constructor() {
        this.itemAdded$ = new EventEmitter();
    }
    
    public list(): TodoItem[] {
        return this.todoList;
    }
    
    public add(item: TodoItem): void {
        this.todoList.push(item);
        this.itemAdded$.emit(item);
    }
}
```

Voici comment un composant racine s'abonnerait à l'événement :

```ts
export class RootComponent {
    private addedItem: TodoItem;
    constructor(todoService: TodoService) {
        todoService.itemAdded$.subscribe(item => this.onItemAdded(item));
    }
    
    private onItemAdded(item: TodoItem): void {
        // faire quelque chose avec l'élément ajouté
        this.addedItem = item;
    }
}
```

Un composant enfant imbriqué à plusieurs niveaux de profondeur s'abonnerait à l'événement de la même manière :

```ts
export class GrandChildComponent {
    private addedItem: TodoItem;
    constructor(todoService: TodoService) {
        todoService.itemAdded$.subscribe(item => this.onItemAdded(item));
    }
    
    private onItemAdded(item: TodoItem): void {
        // faire quelque chose avec l'élément ajouté
        this.addedItem = item;
    }
}
```

Voici le composant qui appelle le service pour déclencher l'événement (il peut résider n'importe où dans l'arbre des composants) :

```ts
@Component({
    selector: 'todo-list',
    template: `
         <ul>
            <li *ngFor="#item of model"> {{ item.name }}
            </li>
         </ul>
        <br />
        Add Item <input type="text" #txt /> <button (click)="add(txt.value); txt.value='';">Add</button>
    `
})
export class TriggeringComponent{
    private model: TodoItem[];
    
    constructor(private todoService: TodoService) {
        this.model = todoService.list();
    }
    
    add(value: string) {
        this.todoService.add(new TodoItem(value, false));
    }
}
```

Référence : [Détection de changement dans Angular](http://victorsavkin.com/post/110170125256/change-detection-in-angular-2)

[**Source**](https://stackoverflow.com/questions/34700438)  
**[Haut](#599b)**

### Quelles sont les différences entre SystemJS et Webpack ?

> 155+ points _? 6_0,183+ vues   
> _[**smartmouse**](https://stackoverflow.com/users/2516399/smartmouse) **a demandé,**_

Je crée ma première application Angular et je voudrais comprendre le rôle des chargeurs de modules. Pourquoi en avons-nous besoin ? J'ai essayé de chercher et de chercher sur Google et je ne comprends pas pourquoi nous devons en installer un pour exécuter notre application ?

Ne pourrait-on pas se contenter d'utiliser `import` pour charger des éléments depuis les modules node ?

J'ai suivi [ce tutoriel](https://angular.io/docs/ts/latest/quickstart.html#!#systemjs) (qui utilise SystemJS) et il me fait utiliser le fichier `systemjs.config.js` :

```js
/**
 * Configuration du système pour les exemples Angular
 * Ajustez si nécessaire pour les besoins de votre application.
 */
(function(global) {
  // map indique au chargeur System où chercher les choses
  var map = {
    'app':                        'transpiled', // 'dist',
    '@angular':                   'node_modules/@angular',
    'angular2-in-memory-web-api': 'node_modules/angular2-in-memory-web-api',
    'rxjs':                       'node_modules/rxjs'
  };
  // packages indique au chargeur System comment charger lorsqu'il n'y a pas de nom de fichier et/ou pas d'extension
  var packages = {
    'app':                        { main: 'main.js',  defaultExtension: 'js' },
    'rxjs':                       { defaultExtension: 'js' },
    'angular2-in-memory-web-api': { main: 'index.js', defaultExtension: 'js' },
  };
  var ngPackageNames = [
    'common',
    'compiler',
    'core',
    'forms',
    'http',
    'platform-browser',
    'platform-browser-dynamic',
    'router',
    'router-deprecated',
    'upgrade',
  ];
  // Fichiers individuels (~300 requêtes) :
  function packIndex(pkgName) {
    packages['@angular/'+pkgName] = { main: 'index.js', defaultExtension: 'js' };
  }
  // Bundled (~40 requêtes) :
  function packUmd(pkgName) {
    packages['@angular/'+pkgName] = { main: '/bundles/' + pkgName + '.umd.js', defaultExtension: 'js' };
  }
  // La plupart des environnements devraient utiliser UMD ; certains (Karma) ont besoin des fichiers index individuels
  var setPackageConfig = System.packageWithIndex ? packIndex : packUmd;
  // Ajouter des entrées de package pour les packages angular
  ngPackageNames.forEach(setPackageConfig);
  var config = {
    map: map,
    packages: packages
  };
  System.config(config);
})(this);
```

Pourquoi avons-nous besoin de ce fichier de configuration ?  
Pourquoi avons-nous besoin de SystemJS (ou WebPack ou autres) ?  
Enfin, selon vous, quel est le meilleur ?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_a répondu, (97+ points)_**

Si vous allez sur la page GitHub de SystemJS, vous verrez la description de l'outil :

`Chargeur de module dynamique universel - charge les modules ES6, AMD, CommonJS et les scripts globaux dans le navigateur et NodeJS.`

Parce que vous utilisez des modules en TypeScript ou ES6, vous avez besoin d'un chargeur de module. Dans le cas de SystemJS, le `systemjs.config.js` nous permet de configurer la manière dont les noms des modules sont associés à leurs fichiers correspondants.

Ce fichier de configuration (et SystemJS) est nécessaire si vous l'utilisez explicitement pour importer le module principal de votre application :

```html
<script>
  System.import('app').catch(function(err){ console.error(err); });
</script>
```

Lorsque vous utilisez TypeScript et configurez le compilateur pour le module `commonjs`, le compilateur crée du code qui n'est plus basé sur SystemJS. Dans cet exemple, le fichier de configuration du compilateur typescript ressemblerait à ceci :

```json
{
  "compilerOptions": {
    "target": "es5",
    "module": "commonjs", // <------
    "moduleResolution": "node",
    "sourceMap": true,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "removeComments": false,
    "noImplicitAny": false
  }
}
```

Webpack est un bundler de modules flexible. Cela signifie qu'il va plus loin et ne gère pas seulement les modules mais fournit également un moyen de packager votre application (concaténer les fichiers, uglifier les fichiers, …). Il fournit également un serveur de développement avec rechargement pour le développement

SystemJS et Webpack sont différents mais avec SystemJS, vous avez encore du travail à faire (avec [Gulp](http://gulpjs.com/) ou [SystemJS builder](https://github.com/systemjs/builder) par exemple) pour packager votre application Angular2 pour la production.

[**Source**](https://stackoverflow.com/questions/38263406)  
**[Haut](#599b)**

### Angular : Impossible de trouver Promise, Map, Set et Iterator

> 154+ points _? 9_0,201+ vues   
> _[**Stav Alfi**](https://stackoverflow.com/users/806963/stav-alfi) **a demandé,**_

Après avoir installé Angular, le compilateur Typescript continue à obtenir des erreurs concernant l'impossibilité de trouver `Promise`, `Map`, `Set` et `Iterator`.

Jusqu'à présent, je les ai ignorées, mais maintenant j'ai besoin de `Promise` pour que mon code fonctionne.

```ts
import {Component} from 'angular2/core';
@Component({
    selector: 'greeting-cmp',
    template: `<div>{{ asyncGreeting | async}}</div>`
})
export class GreetingCmp {
    asyncGreeting: Promise<string> = new Promise(resolve => {
// après 1 seconde, la promesse sera résolue
        window.setTimeout(() => resolve('hello'), 1000);
    });
}

Informations supplémentaires :
npm -v est 2.14.12
node -v est v4.3.1
typescript v est 1.6
```

**Les erreurs :**

```bash
................ERROS OF MY CODE.................
    C:\Users\armyTik\Desktop\angular2\greeting_cmp.ts
    Error:(7, 20) TS2304: Cannot find name 'Promise'.
    Error:(7, 42) TS2304: Cannot find name 'Promise'.
    .........................................
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\platform\browser.d.ts
    Error:(77, 90) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\application_ref.d.ts
    Error:(83, 60) TS2304: Cannot find name 'Promise'.
    Error:(83, 146) TS2304: Cannot find name 'Promise'.
    Error:(96, 51) TS2304: Cannot find name 'Promise'.
    Error:(96, 147) TS2304: Cannot find name 'Promise'.
    Error:(133, 90) TS2304: Cannot find name 'Promise'.
    Error:(171, 81) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\change_detection\parser\locals.d.ts
    Error:(3, 14) TS2304: Cannot find name 'Map'.
    Error:(4, 42) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\debug\debug_node.d.ts
    Error:(14, 13) TS2304: Cannot find name 'Map'.
    Error:(24, 17) TS2304: Cannot find name 'Map'.
    Error:(25, 17) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\di\provider.d.ts
    Error:(436, 103) TS2304: Cannot find name 'Map'.
    Error:(436, 135) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\linker\compiler.d.ts
    Error:(12, 50) TS2304: Cannot find name 'Promise'.
    Error:(16, 41) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\linker\dynamic_component_loader.d.ts
    Error:(108, 136) TS2304: Cannot find name 'Promise'.
    Error:(156, 150) TS2304: Cannot find name 'Promise'.
    Error:(197, 128) TS2304: Cannot find name 'Promise'.
    Error:(203, 127) TS2304: Cannot find name 'Promise'.
    Error:(204, 141) TS2304: Cannot find name 'Promise'.
    Error:(205, 119) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\core\render\api.d.ts
    Error:(13, 13) TS2304: Cannot find name 'Map'.
    Error:(14, 84) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\async.d.ts
    Error:(27, 33) TS2304: Cannot find name 'Promise'.
    Error:(28, 45) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\collection.d.ts
    Error:(1, 25) TS2304: Cannot find name 'MapConstructor'.
    Error:(2, 25) TS2304: Cannot find name 'SetConstructor'.
    Error:(4, 27) TS2304: Cannot find name 'Map'.
    Error:(4, 39) TS2304: Cannot find name 'Map'.
    Error:(7, 9) TS2304: Cannot find name 'Map'.
    Error:(8, 30) TS2304: Cannot find name 'Map'.
    Error:(11, 43) TS2304: Cannot find name 'Map'.
    Error:(12, 27) TS2304: Cannot find name 'Map'.
    Error:(14, 23) TS2304: Cannot find name 'Map'.
    Error:(15, 25) TS2304: Cannot find name 'Map'.
    Error:(95, 41) TS2304: Cannot find name 'Set'.
    Error:(96, 22) TS2304: Cannot find name 'Set'.
    Error:(97, 25) TS2304: Cannot find name 'Set'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\lang.d.ts
    Error:(13, 17) TS2304: Cannot find name 'Map'.
    Error:(14, 17) TS2304: Cannot find name 'Set'.
    Error:(78, 59) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\facade\promise.d.ts
    Error:(2, 14) TS2304: Cannot find name 'Promise'.
    Error:(7, 32) TS2304: Cannot find name 'Promise'.
    Error:(8, 38) TS2304: Cannot find name 'Promise'.
    Error:(9, 35) TS2304: Cannot find name 'Promise'.
    Error:(9, 93) TS2304: Cannot find name 'Promise'.
    Error:(10, 34) TS2304: Cannot find name 'Promise'.
    Error:(11, 32) TS2304: Cannot find name 'Promise'.
    Error:(11, 149) TS2304: Cannot find name 'Promise'.
    Error:(12, 43) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\http\headers.d.ts
    Error:(43, 59) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\http\url_search_params.d.ts
    Error:(11, 16) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\platform\browser\browser_adapter.d.ts
    Error:(75, 33) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\angular2\src\platform\dom\dom_adapter.d.ts
    Error:(85, 42) TS2304: Cannot find name 'Map'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\CoreOperators.d.ts
    Error:(35, 67) TS2304: Cannot find name 'Promise'.
    Error:(50, 66) TS2304: Cannot find name 'Promise'.
    Error:(89, 67) TS2304: Cannot find name 'Promise'.
    Error:(94, 38) TS2304: Cannot find name 'Promise'.
    Error:(94, 50) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\Observable.d.ts
    Error:(46, 62) TS2304: Cannot find name 'Promise'.
    Error:(47, 42) TS2304: Cannot find name 'Iterator'.
    Error:(103, 74) TS2304: Cannot find name 'Promise'.
    Error:(103, 84) TS2304: Cannot find name 'Promise'.
    Error:(143, 66) TS2304: Cannot find name 'Promise'.
    Error:(158, 65) TS2304: Cannot find name 'Promise'.
    Error:(201, 66) TS2304: Cannot find name 'Promise'.
    Error:(206, 38) TS2304: Cannot find name 'Promise'.
    Error:(206, 50) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\observable\ForkJoinObservable.d.ts
    Error:(6, 50) TS2304: Cannot find name 'Promise'.
    Error:(7, 58) TS2304: Cannot find name 'Promise'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\observable\FromObservable.d.ts
    Error:(7, 38) TS2304: Cannot find name 'Promise'.
    Error:(7, 51) TS2304: Cannot find name 'Iterator'.
    C:\Users\armyTik\Desktop\angular2\node_modules\rxjs\observable\PromiseObservable.d.ts
    Error:(9, 31) TS2304: Cannot find name 'Promise'.
    Error:(10, 26) TS2304: Cannot find name 'Promise'.
```

> [**_Kris Hollenbeck_**](https://stackoverflow.com/users/1949099) **_a répondu, (162+ points)_**

#### Angular RC4 — Angular ^2.0.0 avec Typescript 2.0.0

_Mis à jour le 19/09/2016_

Pour faire fonctionner cela avec typescript 2.0.0, j'ai fait ce qui suit.

`npm install --save-dev @types/core-js`

**tsconfig.json**

```json
"compilerOptions": {
    "declaration": false,
    "emitDecoratorMetadata": true,
    "experimentalDecorators": true,
    "mapRoot": "./",
    "module": "es6",
    "moduleResolution": "node",
    "noEmitOnError": true,
    "noImplicitAny": false,
    "outDir": "../dist/out-tsc",
    "sourceMap": true,
    "target": "es5",
    "typeRoots": [
      "../node_modules/@types"
    ],
    "types": [
      "core-js"
    ]
  }
```

**Plus d'informations sur @types avec typescript 2.0.0.**

1. [https://blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/](https://blogs.msdn.microsoft.com/typescript/2016/06/15/the-future-of-declaration-files/)
2. [https://www.npmjs.com/~types](https://www.npmjs.com/~types)

Exemple d'installation :

```
npm install --save-dev @types/core-js
```

**Erreurs d'identificateur en double**

Cela est probablement dû au fait que des typages ecmascript 6 en double sont déjà importés depuis un autre endroit, probablement un ancien es6-shim.

Vérifiez deux fois `typings.d.ts` pour vous assurer qu'il n'y a pas de références à `es6`. Supprimez toute référence à `es6` de votre répertoire typings si vous en avez un.

**Par exemple :**

Cela entrera en conflit avec `types:['core-js']` dans typings.json.

```json
{
  "globalDependencies": {
    "core-js": "registry:dt/core-js#0.0.0+20160602141332" 
    // es6-shim entrera également en conflit
  }
}
```

L'inclusion de `core-js` dans le tableau des types dans `tsconfig.json` devrait être le seul endroit où il est importé.

**Angular CLI 1.0.0-beta.30**

Si vous utilisez l'Angular-CLI, supprimez le tableau lib dans `typings.json`. Cela semble entrer en conflit avec la déclaration de core-js dans les types.

```json
"compilerOptions" : {
  ...
  // supprimé "lib": ["es6", dom"],
  ...
},
"types" : ["core-js"]
```

**Utilisateurs de Webstorm/Intellij utilisant l'Angular CLI**

Assurez-vous que le compilateur typescript intégré est désactivé. Cela entrera en conflit avec le CLI. Pour compiler votre typescript avec le CLI, vous pouvez configurer une configuration `ng serve`.

![Image](https://cdn-media-1.freecodecamp.org/images/YG2jiM4rYeIBDbXVSaDe3VOIdHlSAH1Z7hmN)

**Options du compilateur Tsconfig lib vs types**

Si vous préférez ne pas installer les définitions de types core js, il existe certaines bibliothèques es6 qui sont incluses avec typescript. Celles-ci sont utilisées via la propriété `lib: []` dans tsconfig.

Voir ici pour exemple : [https://www.typescriptlang.org/docs/handbook/compiler-options.html](https://www.typescriptlang.org/docs/handbook/compiler-options.html)

`Note : Si --lib n'est pas spécifié, une bibliothèque par défaut est injectée. La bibliothèque par défaut injectée est : ? Pour --target ES5 : DOM,ES5,ScriptHost ? Pour --target ES6 : DOM,ES6,DOM.Iterable,ScriptHost`

**tl;dr**

Réponse courte, soit `"lib": [ "es6", "dom" ]` soit `"types": ["core-js"]` peut être utilisé pour résoudre `can't find Promise,Map, Set and Iterator`. Cependant, utiliser les deux provoquera des erreurs d'identificateur en double.

[**Source**](https://stackoverflow.com/questions/35660498)  
**[Haut](#599b)**

### Comment détecter lorsqu'une valeur @Input() change dans Angular ?

> 154+ points _? 8_9,893+ vues   
> _[**Jon Catmull**](https://stackoverflow.com/users/3604283/jon-catmull) **a demandé,**_

J'ai un composant parent (**CategoryComponent**), un composant enfant (**videoListComponent**) et un ApiService.

J'ai réussi à faire fonctionner la plupart de cela, c'est-à-dire que chaque composant peut accéder à l'API json et obtenir ses données pertinentes via des observables.

Actuellement, le composant de liste vidéo obtient simplement toutes les vidéos, j'aimerais filtrer cela pour ne garder que les vidéos d'une catégorie particulière, j'ai réussi à le faire en passant le categoryId à l'enfant via `@Input()`.

CategoryComponent.html

```ts
<video-list *ngIf="category" [categoryId]="category.id"></video-list>
```

Cela fonctionne et lorsque la catégorie du composant parent CategoryComponent change, la valeur categoryId est transmise via `@Input()`, mais je dois ensuite détecter cela dans VideoListComponent et redemander le tableau des vidéos via APIService (avec le nouveau categoryId).

Dans AngularJS, j'aurais fait un `$watch` sur la variable. Quelle est la meilleure façon de gérer cela ?

> [**_Alan C. S._**](https://stackoverflow.com/users/2107767) **_a répondu, (181+ points)_**

**En fait, il existe deux façons de détecter et d'agir lorsque la valeur d'une entrée change dans le composant enfant dans angular2+ :**

1. Vous pouvez utiliser la méthode de cycle de vie **ngOnChanges()** comme mentionné dans les anciennes réponses :   
`@Input() categoryId: string; ngOnChanges(changes: SimpleChanges) { this.doSomething(changes.categoryId.currentValue); // Vous pouvez également utiliser categoryId.previousValue et // categoryId.firstChange pour comparer les anciennes et nouvelles valeurs }`
2. Liens de documentation : [ngOnChanges,](https://angular.io/api/core/OnChanges) [SimpleChanges,](https://angular.io/api/core/SimpleChanges) [SimpleChange](https://angular.io/api/core/SimpleChange)  
Exemple de démonstration : Regardez [ce plunker](https://plnkr.co/edit/LUr2bMQRhhAeuLN3R5B6?p=preview)
3. Alternativement, vous pouvez également utiliser un **setter de propriété d'entrée** comme suit :  
`private _categoryId: string; @Input() set categoryId(value: string) { this._categoryId = value; this.doSomething(this._categoryId); } get categoryId(): string { return this._categoryId; }`
4. Lien de documentation : Regardez [ici](https://angular.io/guide/component-interaction#intercept-input-property-changes-with-a-setter).
5. Exemple de démonstration : Regardez [ce plunker](https://plnkr.co/edit/EsolgwJVuvOUx6rKk8d4?p=preview).

**QUELLE APPROCHE DEVEZ-VOUS UTILISER ?**

Si votre composant a plusieurs entrées, alors, si vous utilisez ngOnChanges(), vous obtiendrez tous les changements pour toutes les entrées en une seule fois dans ngOnChanges(). En utilisant cette approche, vous pouvez également comparer les valeurs actuelles et précédentes de l'entrée qui a changé et prendre des mesures en conséquence.

Cependant, si vous voulez faire quelque chose lorsqu'une seule entrée particulière change (et vous ne vous souciez pas des autres entrées), alors il peut être plus simple d'utiliser un setter de propriété d'entrée. Cependant, cette approche ne fournit pas de moyen intégré pour comparer les valeurs précédentes et actuelles de l'entrée modifiée (ce que vous pouvez faire facilement avec la méthode de cycle de vie ngOnChanges).

**ÉDITION 2017-07-25 : LA DÉTECTION DE CHANGEMENT ANGULAR PEUT NE PAS SE DÉCLENCHER DANS CERTAINES CIRCONSTANCES**

Normalement, la détection de changement pour le setter et ngOnChanges se déclenchera chaque fois que le composant parent modifie les données qu'il transmet à l'enfant, **à condition que les données soient un type de données primitif JS (chaîne, nombre, booléen)**. Cependant, dans les scénarios suivants, elle ne se déclenchera pas et vous devrez prendre des mesures supplémentaires pour la faire fonctionner.

1. Si vous utilisez un objet ou un tableau imbriqué (au lieu d'un type de données primitif JS) pour transmettre des données du parent à l'enfant, la détection de changement (en utilisant le setter ou ngchanges) peut ne pas se déclencher, comme mentionné dans la réponse de l'utilisateur : muetzerich. Pour des solutions, regardez [ici](https://stackoverflow.com/questions/34796901/angular2-change-detection-ngonchanges-not-firing-for-nested-object).
2. Si vous mutiez des données en dehors du contexte angular (c'est-à-dire, externement), alors angular ne sera pas au courant des changements. Vous devrez peut-être utiliser ChangeDetectorRef ou NgZone dans votre composant pour rendre angular conscient des changements externes et ainsi déclencher la détection de changement. Référez-vous à [ceci](https://stackoverflow.com/questions/42971865/angular2-zone-run-vs-changedetectorref-detectchanges).

[**Source**](https://stackoverflow.com/questions/38571812)  
**[Haut](#599b)**

### Comment passer des arguments d'URL (chaîne de requête) à une requête HTTP sur Angular

> 154+ points _? 1_57,619+ vues   
> _[**Miguel Lattuada**](https://stackoverflow.com/users/3276721/miguel-lattuada) **a demandé,**_

Salut les gars, je crée une requête HTTP sur Angular, mais je ne sais pas comment ajouter des arguments d'URL (chaîne de requête) à celle-ci.

```ts
this.http.get(StaticSettings.BASE_URL).subscribe(
  (response) => this.onGetForecastResult(response.json()),
  (error) => this.onGetForecastError(error.json()),
  () => this.onGetForecastComplete()
);
```

Maintenant, mon StaticSettings.BASE_URL est quelque chose comme une URL sans chaîne de requête comme : [http://atsomeplace.com/](http://atsomeplace.com/) mais je veux qu'elle soit [http://atsomeplace.com/?var1=val1&var2=val2](http://atsomeplace.com/?var1=val1&var2=val2)

Où var1 et var2 s'insèrent-ils dans mon objet de requête Http ? Je veux les ajouter comme un objet.

```json
{
  query: {
    var1: val1,
    var2: val2
  }
}
```

et ensuite laisser le module Http faire le travail pour les analyser en chaîne de requête URL.

> [**_toskv_**](https://stackoverflow.com/users/5152732) **_a répondu, (216+ points)_**

Les méthodes [**HttpClient**](https://angular.io/api/common/http/HttpClient) permettent de définir les **params** dans ses options.

Vous pouvez le configurer en important le [**HttpClientModule**](https://angular.io/api/common/http) depuis le package @angular/common/http.

```ts
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  imports: [ BrowserModule, HttpClientModule ],
  declarations: [ App ],
  bootstrap: [ App ]
})
export class AppModule {}
```

Après cela, vous pouvez injecter le **HttpClient** et l'utiliser pour effectuer la requête.

```ts
import {HttpClient} from '@angular/common/http'
```

```ts
import {HttpClient} from '@angular/common/http'

@Component({
  selector: 'my-app',
  template: `
    <div>
      <h2>Hello {{name}}</h2>
    </div>
  `,
})
export class App {
  name:string;
  constructor(private httpClient: HttpClient) {
    this.httpClient.get('/url', {
      params: {
        appid: 'id1234',
        cnt: '5'
      },
      observe: 'response'
    })
    .toPromise()
    .then(response => {
      console.log(response);
    })
    .catch(console.log);
  }
}
```

Vous pouvez trouver un exemple fonctionnel [ici](https://plnkr.co/edit/G4mczOLOHfVYKpuaWee3?p=preview).

Pour les versions d'angular antérieures à la version 4, vous pouvez faire de même en utilisant le service **Http**.

La méthode **Http.get** prend un objet qui implémente [RequestOptionsArgs](https://angular.io/docs/ts/latest/api/http/index/RequestOptionsArgs-interface.html) comme deuxième paramètre.

Le champ **search** de cet objet peut être utilisé pour définir une chaîne ou un objet [URLSearchParams](https://angular.io/docs/ts/latest/api/http/index/URLSearchParams-class.html).

Un exemple :

```ts
// Objet de paramètres-
 let params: URLSearchParams = new URLSearchParams();
 params.set('appid', StaticSettings.API_KEY);
 params.set('cnt', days.toString());
 
 // Requête Http-
 return this.http.get(StaticSettings.BASE_URL, {
   search: params
 }).subscribe(
   (response) => this.onGetForecastResult(response.json()), 
   (error) => this.onGetForecastError(error.json()), 
   () => this.onGetForecastComplete()
 );
```

La documentation pour la classe **Http** contient plus de détails. Elle peut être trouvée [ici](https://angular.io/docs/ts/latest/api/http/index/Http-class.html) et un exemple fonctionnel [ici](https://plnkr.co/edit/pKdztZBHr0wr1YLmmI8P?p=preview).

[**Source**](https://stackoverflow.com/questions/34475523)  
**[Haut](#599b)**

### Comment déployez-vous des applications Angular ?

> 153+ points _? 8_9,991+ vues   
> _[**Joseph Assem Sobhy**](https://stackoverflow.com/users/1362355/joseph-girgis) **a demandé,**_

Comment déployez-vous des applications Angular une fois qu'elles atteignent la phase de production ?

Tous les guides que j'ai vus jusqu'à présent (même sur [angular.io](https://angular.io/)) comptent sur un lite-server pour servir et browserSync pour refléter les changements — mais lorsque vous avez terminé le développement, comment pouvez-vous publier l'application ?

Dois-je importer tous les fichiers `.js` compilés dans la page `index.html` ou dois-je les minifier en utilisant gulp ? Vont-ils fonctionner ? Ai-je besoin de SystemJS dans la version de production ?

> [**_Amid_**](https://stackoverflow.com/users/1035889) **_a répondu, (74+ points)_**

Vous touchez en fait ici deux questions en une. La première est de savoir comment héberger votre application. Et comme l'a mentionné @toskv, c'est une question beaucoup trop large pour être répondue et dépend de nombreuses choses différentes. La seconde est plus spécifique — comment préparez-vous la version de déploiement de l'application. Vous avez plusieurs options ici :

1. Déployer tel quel. Juste ça — pas de minification, de concaténation, de mangling de noms, etc. Transpilez tout votre projet ts, copiez toutes vos sources js/css/… résultantes + dépendances sur le serveur d'hébergement et vous êtes prêt à partir.
2. Déployer en utilisant des outils de bundling spécifiques. Comme webpack ou systemjs builder. Ils viennent avec toutes les possibilités qui manquent dans #1. Vous pouvez packager tout le code de votre application en seulement quelques fichiers js/css/… que vous référencez dans votre html. Systemjs builder permet même de se débarrasser du besoin d'inclure systemjs dans le cadre de votre package de déploiement.

Oui, vous devrez probablement déployer systemjs et un ensemble d'autres bibliothèques externes dans le cadre de votre package. Et oui, vous pourrez les regrouper en seulement quelques fichiers js que vous référencez depuis votre page html. Vous n'avez pas à référencer tous vos fichiers js compilés depuis la page — systemjs en tant que chargeur de module s'en occupera.

Je sais que cela semble flou — pour vous aider à démarrer avec le #2, voici deux exemples d'applications vraiment bons :

SystemJS builder : [angular2 seed](https://github.com/mgechev/angular2-seed)

WebPack : [angular2 webpack starter](https://github.com/AngularClass/angular2-webpack-starter)

Regardez comment ils font — et espérons que cela vous aidera à trouver votre façon de regrouper les applications que vous faites.

[**Source**](https://stackoverflow.com/questions/35539622)  
**[Haut](#599b)**

### ngFor avec index comme valeur dans l'attribut

> 149+ points _? 1_95,294+ vues   
> _[**Vivendi**](https://stackoverflow.com/users/1175327/vivendi) **a demandé,**_

J'ai une simple boucle `ngFor` qui suit également l'`index` actuel. Je veux stocker cette valeur `index` dans un attribut pour pouvoir l'imprimer. Mais je n'arrive pas à comprendre comment cela fonctionne.

J'ai essentiellement ceci :

```ts
<ul *ngFor="#item of items; #i = index" data-index="#i">
    <li>{{item}}</li>
</ul>
```

Je veux stocker la valeur de `#i` dans l'attribut `data-index`. J'ai essayé plusieurs méthodes mais aucune n'a fonctionné.

J'ai une démo ici : [http://plnkr.co/edit/EXpOKAEIFlI9QwuRcZqp?p=preview](http://plnkr.co/edit/EXpOKAEIFlI9QwuRcZqp?p=preview)

Comment puis-je stocker la valeur `index` dans l'attribut `data-index` ?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_a répondu, (284+ points)_**

J'utiliserais cette syntaxe pour définir la valeur de l'index dans un attribut de l'élément HTML :

```ts
<ul>
    <li *ngFor="#item of items; #i = index" [attr.data-index]="i">
        {{item}}
    </li>
</ul>
```

Voici le plunkr mis à jour : [http://plnkr.co/edit/LiCeyKGUapS5JKkRWnUJ?p=preview](http://plnkr.co/edit/LiCeyKGUapS5JKkRWnUJ?p=preview).

**Mise à jour pour les versions récentes d'Angular 2** Vous devez utiliser `let` pour déclarer la valeur plutôt que `#`.

```ts
<ul>
    <li *ngFor="let item of items; let i = index" [attr.data-index]="i">
        {{item}}
    </li>
</ul>
```

[**Source**](https://stackoverflow.com/questions/35405618)  
**[Haut](#599b)**

### Définir des constantes globales dans Angular 2

> 149+ points _? 1_28,101+ vues   
> _[**AndreFeijo**](https://stackoverflow.com/users/2946773/andrefeijo) **a demandé,**_

Dans Angular 1.x, vous pouvez définir des constantes comme ceci :

```ts
angular.module('mainApp.config', [])
.constant('API_ENDPOINT', 'http://127.0.0.1:6666/api/')
```

Quel serait l'équivalent dans Angular2 (avec Typescript) ? Je ne veux simplement pas répéter l'URL de base de l'API encore et encore dans tous mes services.

> [**_AndreFeijo_**](https://stackoverflow.com/users/2946773) **_a répondu, (159+ points)_**

**Les modifications ci-dessous fonctionnent pour moi sur la version finale d'Angular 2 :**

```ts
export class AppSettings {
   public static API_ENDPOINT='http://127.0.0.1:6666/api/';
}
```

**Et ensuite dans le service :**

```ts
import {Http} from 'angular2/http';
import {Message} from '../models/message';
import {Injectable} from 'angular2/core';
import {Observable} from 'rxjs/Observable';
import {AppSettings} from '../appSettings';
import 'rxjs/add/operator/map';

@Injectable()
export class MessageService {

    constructor(private http: Http) { }
    
    getMessages(): Observable<Message[]> {
        return this.http.get(AppSettings.API_ENDPOINT+'/messages')
            .map(response => response.json())
            .map((messages: Object[]) => {
                return messages.map(message => this.parseData(message));
            });
    }
    
    private parseData(data): Message {
        return new Message(data);
    }
}
```

[**Source**](https://stackoverflow.com/questions/34986922)  
**[Haut](#599b)**

### Angular — Utiliser des pipes dans les services et les composants

> 148+ points _? 7_5,716+ vues   
> _[**POSIX-compliant**](https://stackoverflow.com/users/4602586/posix-compliant) **a demandé,**_

Dans AngularJS, je suis capable d'utiliser des filtres (pipes) à l'intérieur des services et des contrôleurs en utilisant une syntaxe similaire à celle-ci :

```ts
$filter('date')(myDate, 'yyyy-MM-dd');
```

Est-il possible d'utiliser des pipes dans les services/composants comme ceci dans Angular ?

> [**_cexbrayat_**](https://stackoverflow.com/users/971121) **_a répondu, (271+ points)_**

Comme d'habitude dans Angular, vous pouvez compter sur l'injection de dépendances :

```ts
import { DatePipe } from '@angular/common';
class MyService {

  constructor(private datePipe: DatePipe) {}
  
  transformDate(date) {
    this.datePipe.transform(myDate, 'yyyy-MM-dd');
  }
}
```

Ajoutez `DatePipe` à votre liste de fournisseurs dans votre module ; si vous oubliez de le faire, vous obtiendrez une erreur `no provider for DatePipe` :

```
providers: [DatePipe,...]
```

Soyez averti cependant que le `DatePipe` s'appuyait sur l'API Intl jusqu'à la version 5, qui n'est pas supportée par tous les navigateurs (consultez le [tableau de compatibilité](http://kangax.github.io/compat-table/esintl/)).

Si vous utilisez des versions plus anciennes d'Angular, vous devriez ajouter le polyfill `Intl` à votre projet pour éviter tout problème. Voir cette [question connexe](https://stackoverflow.com/questions/35017800/ionic-2-using-angular-2-pipe-breaks-on-ios-cant-find-variable-intl/35018352#35018352) pour une réponse plus détaillée.

[**Source**](https://stackoverflow.com/questions/35144821)  
**[Haut](#599b)**

### Exception Angular2 : Impossible de lier à 'routerLink' car ce n'est pas une propriété native connue

> 144+ points _? 8_3,326+ vues   
> _[**Lester Burnham**](https://stackoverflow.com/users/1798547/lester-burnham) **a demandé,**_

Évidemment, la bêta pour Angular2 est plus récente que nouvelle, donc il n'y a pas beaucoup d'informations là-bas, mais j'essaie de faire ce que je pense être un routage assez basique.

En bidouillant avec le code de démarrage rapide et d'autres extraits du site [https://angular.io](https://angular.io), j'ai obtenu la structure de fichiers suivante :

```
angular-testapp/
    app/
        app.component.ts
        boot.ts
        routing-test.component.ts
    index.html
```

Avec les fichiers remplis comme suit :

**index.html**

```html
<html>

  <head>
    <base href="/">
    <title>Angular 2 QuickStart</title>
    <link href="../css/bootstrap.css" rel="stylesheet">
    
    <!-- 1. Charger les bibliothèques -->
    <script src="node_modules/angular2/bundles/angular2-polyfills.js"></script>
    <script src="node_modules/systemjs/dist/system.src.js"></script>
    <script src="node_modules/rxjs/bundles/Rx.js"></script>
    <script src="node_modules/angular2/bundles/angular2.dev.js"></script>
    <script src="node_modules/angular2/bundles/router.dev.js"></script>
    
    <!-- 2. Configurer SystemJS -->
    <script>
      System.config({
        packages: {        
          app: {
            format: 'register',
            defaultExtension: 'js'
          }
        }
      });
      System.import('app/boot')
            .then(null, console.error.bind(console));
    </script>
    
  </head>
  
  <!-- 3. Afficher l'application -->
  <body>
    <my-app>Loading...</my-app>
  </body>
  
</html>
```

**boot.ts**

```ts
import {bootstrap}    from 'angular2/platform/browser'
import {ROUTER_PROVIDERS} from 'angular2/router';

import {AppComponent} from './app.component'

bootstrap(AppComponent, [
    ROUTER_PROVIDERS
]);
```

**app.component.ts**

```ts
import {Component} from 'angular2/core';
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS, LocationStrategy, HashLocationStrategy} from 'angular2/router';

import {RoutingTestComponent} from './routing-test.component';

@Component({
    selector: 'my-app',
    template: `
        <h1>Component Router</h1>
        <a [routerLink]="['RoutingTest']">Routing Test</a>
        <router-outlet></router-outlet>
        `
})

@RouteConfig([
    {path:'/routing-test', name: 'RoutingTest', component: RoutingTestComponent, useAsDefault: true},
])

export class AppComponent { }
```

**routing-test.component.ts**

```ts
import {Component} from 'angular2/core';
import {Router} from 'angular2/router';

@Component({
    template: `
        <h2>Routing Test</h2>
        <p>Interesting stuff goes here!</p>
        `
})
export class RoutingTestComponent { }
```

En essayant d'exécuter ce code, l'erreur suivante est produite :

```bash
EXCEPTION: Template parse errors:
Can't bind to 'routerLink' since it isn't a known native property ("
        <h1>Component Router</h1>
        <a [ERROR ->][routerLink]="['RoutingTest']">Routing Test</a>
        <router-outlet></router-outlet>
        "): AppComponent@2:11
```

J'ai trouvé un problème vaguement lié ici ; [router-link directives broken after upgrading to angular2.0.0-beta.0](https://stackoverflow.com/questions/34304115/router-link-directives-broken-after-upgrading-to-angular2-0-0-beta-0). Cependant, le « working example » dans l'une des réponses est basé sur du code pré-bêta — qui peut bien encore fonctionner, mais j'aimerais savoir pourquoi le code que j'ai créé ne fonctionne pas.

Toute indication serait grandement appréciée !

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (220+ points)_**

**>=R**C.5

importer le `RouterModule` Voir aussi [https://angular.io/docs/ts/latest/guide/router.html](https://angular.io/docs/ts/latest/guide/router.html)

```ts
@NgModule({ 
  imports: [RouterModule],
  ...
})
```

**>=R**C.2

**app.routes.ts**

```ts
import { provideRouter, RouterConfig } from '@angular/router';

export const routes: RouterConfig = [
  ...
];

export const APP_ROUTER_PROVIDERS = [provideRouter(routes)];
```

**main.ts**

```
import { bootstrap } from '@angular/platform-browser-dynamic';
import { APP_ROUTER_PROVIDERS } from './app.routes';

bootstrap(AppComponent, [APP_ROUTER_PROVIDERS]);
```

**<=RC.1**

Votre code manque de

```ts
@Component({
    ...
    directives: [ROUTER_DIRECTIVES],
    ...)}
```

Vous ne pouvez pas utiliser de directives comme `routerLink` ou `router-outlet` sans les rendre connues à votre composant.

Alors que les noms des directives ont été modifiés pour être sensibles à la casse dans Angular2, les éléments utilisent toujours `-` dans le nom comme `<router-outl`et> pour être compatibles avec la spécification des web-components qui requi`i`rent un - dans le nom des éléments personnalisés.

**enregistrer globalement**

Pour rendre `ROUTER_DIRECTIVES` globalement disponible, ajoutez ce fournisseur à `bootstrap(...)` :

```
provide(PLATFORM_DIRECTIVES, {useValue: [ROUTER_DIRECTIVES], multi: true})
```

ensuite il n'est plus nécessaire d'ajouter `ROUTER_DIRECTIVES` à chaque composant.

[**Source**](https://stackoverflow.com/questions/34317044)  
**[Haut](#599b)**

### Angular 2 onglets dynamiques avec des composants choisis par l'utilisateur

> 143+ points _? 8_0,735+ vues   
> _[**Cuel**](https://stackoverflow.com/users/2951897/cuel) **a demandé,**_

J'essaie de mettre en place un système d'onglets qui permet aux composants de s'enregistrer eux-mêmes (avec un titre). Le premier onglet est comme une boîte de réception, il y a beaucoup d'actions/liens pour que les utilisateurs choisissent, et chacun de ces clics devrait pouvoir instancier un nouveau composant, au clic. Les actions/liens proviennent de JSON.

Le composant instancié s'enregistrera ensuite comme un nouvel onglet.

Je ne suis pas sûr si c'est la meilleure approche ? Jusqu'à présent, les seuls guides que j'ai vus sont pour des onglets statiques, ce qui n'aide pas.

Jusqu'à présent, j'ai seulement le service d'onglets qui est démarré dans main pour persister dans toute l'application, cela ressemble à quelque chose comme ceci.

```ts
export interface ITab { title: string; }

@Injectable()
export class TabsService {
    private tabs = new Set<ITab>();
    
    addTab(title: string): ITab {
        let tab: ITab = { title };
        this.tabs.add(tab);
        return tab;
    }
    
    removeTab(tab: ITab) {
        this.tabs.delete(tab);
    }
}
```

Questions :

1) Comment puis-je avoir une liste dynamique dans la boîte de réception qui crée de nouveaux onglets (différents) ? Je suppose que le DynamicComponentBuilder serait utilisé ?

2) Comment les composants créés à partir de la boîte de réception (au clic) peuvent-ils s'enregistrer eux-mêmes en tant qu'onglets et également être affichés ? Je suppose ng-content mais je ne trouve pas beaucoup d'informations sur la façon de l'utiliser

Édition : Essayer de clarifier

Pensez à la boîte de réception comme une boîte de réception de courrier, les éléments sont récupérés en tant que JSON et affichent plusieurs éléments. Une fois qu'un des éléments est cliqué, un nouvel onglet est créé avec le type d'action de cet élément. Le type est alors un composant

Édition2 : Image

[http://i.imgur.com/yzfMOXJ.png](http://i.imgur.com/yzfMOXJ.png)

> [**_Günter Zöchbauer_**](https://stackoverflow.com/users/217408) **_a répondu, (190+ points)_**

**mise à jour**

[**Exemple Angular 5 StackBlitz**](https://stackblitz.com/edit/angular-ygz3jg)

**mise à jour**

`ngComponentOutlet` a été ajouté à 4.0.0-beta.3

**mise à jour**

Il y a un `NgComponentOutlet` en cours de développement qui fait quelque chose de similaire [https://github.com/angular/angular/pull/11235](https://github.com/angular/angular/pull/11235)

**RC.7**

[**Exemple Plunker RC.7**](http://plnkr.co/edit/UGzoPTCHlXKWrn4p8gd1?p=preview)

```ts
// Composant d'aide pour ajouter des composants dynamiques
@Component({
  selector: 'dcl-wrapper',
  template: `<div #target></div>`
})
export class DclWrapper {
  @ViewChild('target', {read: ViewContainerRef}) target: ViewContainerRef;
  @Input() type: Type<Component>;
  cmpRef: ComponentRef<Component>;
  private isViewInitialized:boolean = false;
  
  constructor(private componentFactoryResolver: ComponentFactoryResolver, private compiler: Compiler) {}
  
  updateComponent() {
    if(!this.isViewInitialized) {
      return;
    }
    if(this.cmpRef) {
      // lorsque l'entrée `type` change, nous détruisons un composant créé précédemment 
      // avant d'en créer un nouveau
      this.cmpRef.destroy();
    }
    
    let factory = this.componentFactoryResolver.resolveComponentFactory(this.type);
    this.cmpRef = this.target.createComponent(factory)
    // pour accéder à l'instance créée, utilisez
    // this.compRef.instance.someProperty = 'someValue';
    // this.compRef.instance.someOutput.subscribe(val => doSomething());
  }
  
  ngOnChanges() {
    this.updateComponent();
  }
  
  ngAfterViewInit() {
    this.isViewInitialized = true;
    this.updateComponent();  
  }
  
  ngOnDestroy() {
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }    
  }
}
```

Exemple d'utilisation

```ts
// Utiliser le composant dcl-wrapper
@Component({
  selector: 'my-tabs',
  template: `
  <h2>Tabs</h2>
  <div *ngFor="let tab of tabs">
    <dcl-wrapper [type]="tab"></dcl-wrapper>
  </div>
`
})
export class Tabs {
  @Input() tabs;
}

@Component({
  selector: 'my-app',
  template: `
  <h2>Hello {{name}}</h2>
  <my-tabs [tabs]="types"></my-tabs>
`
})
export class App {
  // La liste des composants pour créer des onglets
  types = [C3, C1, C2, C3, C3, C1, C1];
}

@NgModule({
  imports: [ BrowserModule ],
  declarations: [ App, DclWrapper, Tabs, C1, C2, C3],
  entryComponents: [C1, C2, C3],
  bootstrap: [ App ]
})
export class AppModule {}
```

Voir aussi [angular.io DYNAMIC COMPONENT LOADER](https://angular.io/docs/ts/latest/cookbook/dynamic-component-loader.html)

**anciennes versions** **xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx**

Cela a changé à nouveau dans Angular2 RC.5

Je vais mettre à jour l'exemple ci-dessous mais c'est le dernier jour avant les vacances.

Cet [exemple Plunker](http://plnkr.co/edit/3dzkMVXe4AGSRhk11TXG?p=preview) démontre comment créer dynamiquement des composants dans RC.5

**Mise à jour — utiliser [ViewContainerRef](https://angular.io/docs/ts/latest/api/core/index/ViewContainerRef-class.html).createComponent()**

Parce que `DynamicComponentLoader` est obsolète, l'approche doit être mise à jour à nouveau.

```ts
@Component({
  selector: 'dcl-wrapper',
  template: `<div #target></div>`
})
export class DclWrapper {
  @ViewChild('target', {read: ViewContainerRef}) target;
  @Input() type;
  cmpRef:ComponentRef;
  private isViewInitialized:boolean = false;
  
  constructor(private resolver: ComponentResolver) {}
  
  updateComponent() {
    if(!this.isViewInitialized) {
      return;
    }
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }
   this.resolver.resolveComponent(this.type).then((factory:ComponentFactory<any>) => {
      this.cmpRef = this.target.createComponent(factory)
      // pour accéder à l'instance créée, utilisez
      // this.compRef.instance.someProperty = 'someValue';
      // this.compRef.instance.someOutput.subscribe(val => doSomething());
    });
  }
  
  ngOnChanges() {
    this.updateComponent();
  }
  
  ngAfterViewInit() {
    this.isViewInitialized = true;
    this.updateComponent();  
  }
  ngOnDestroy() {
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }    
  }
}
```

[**Exemple Plunker RC.4**](http://plnkr.co/edit/GJTLrnQdRDBvZenX59PZ?p=preview)  
[**Exemple Plunker beta.17**](https://plnkr.co/edit/PpgMvS?p=preview)

**Mise à jour — utiliser loadNextToLocation**

```ts
export class DclWrapper {
  @ViewChild('target', {read: ViewContainerRef}) target;
  @Input() type;
  cmpRef:ComponentRef;
  private isViewInitialized:boolean = false;
  
  constructor(private dcl:DynamicComponentLoader) {}
  
  updateComponent() {
    // devrait être exécuté chaque fois que `type` change mais pas avant que `ngAfterViewInit()` ait été appelé 
    // pour avoir `target` initialisé
    if(!this.isViewInitialized) {
      return;
    }
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }
    this.dcl.loadNextToLocation(this.type, this.target).then((cmpRef) => {
      this.cmpRef = cmpRef;
    });
  }
  
  ngOnChanges() {
    this.updateComponent();
  }
  
  ngAfterViewInit() {
    this.isViewInitialized = true;
    this.updateComponent();  
  }
  
  ngOnDestroy() {
    if(this.cmpRef) {
      this.cmpRef.destroy();
    }    
  }
}
```

[**Exemple Plunker beta.17**](https://plnkr.co/edit/kc2Bgg?p=preview)

**original**

Pas tout à fait sûr de vos exigences à partir de votre question, mais je pense que cela devrait faire ce que vous voulez.

Le composant `Tabs` reçoit un tableau de types passé et il crée des "onglets" pour chaque élément du tableau.

```ts
@Component({
  selector: 'dcl-wrapper',
  template: `<div #target></div>`
})
export class DclWrapper {
  constructor(private elRef:ElementRef, private dcl:DynamicComponentLoader) {}
  @Input() type;
  
  ngOnChanges() {
    if(this.cmpRef) {
      this.cmpRef.dispose();
    }
    this.dcl.loadIntoLocation(this.type, this.elRef, 'target').then((cmpRef) => {
      this.cmpRef = cmpRef;
    });
  }
}

@Component({
  selector: 'c1',
  template: `<h2>c1</h2>`
  
})
export class C1 {
}

@Component({
  selector: 'c2',
  template: `<h2>c2</h2>`
})
export class C2 {
}
@Component({
  selector: 'c3',
  template: `<h2>c3</h2>`
  
})
export class C3 {
}

@Component({
  selector: 'my-tabs',
  directives: [DclWrapper],
  template: `
  <h2>Tabs</h2>
  <div *ngFor="let tab of tabs">
    <dcl-wrapper [type]="tab"></dcl-wrapper>
  </div>
`
})
export class Tabs {
  @Input() tabs;
}

@Component({
  selector: 'my-app',
  directives: [Tabs]
  template: `
  <h2>Hello {{name}}</h2>
  <my-tabs [tabs]="types"></my-tabs>
`
})
export class App {
  types = [C3, C1, C2, C3, C3, C1, C1];
}
```

[**Exemple Plunker beta.15**](https://plnkr.co/edit/kc2Bgg?p=preview) (non basé sur votre Plunker)

Il existe également un moyen de transmettre des données qui peuvent être transmises au composant créé dynamiquement comme (`someData` devrait être transmis comme `type`)

```ts
this.dcl.loadIntoLocation(this.type, this.elRef, 'target').then((cmpRef) => {
  cmpRef.instance.someProperty = someData;
  this.cmpRef = cmpRef;
});
```

Il existe également un certain support pour utiliser l'injection de dépendances avec des services partagés.

Pour plus de détails, voir [https://angular.io/docs/ts/latest/cookbook/dynamic-component-loader.html](https://angular.io/docs/ts/latest/cookbook/dynamic-component-loader.html)

[**Source**](https://stackoverflow.com/questions/36325212)  
**[Haut](#599b)**

### Délégation : EventEmitter ou Observable dans Angular

> 141+ points _? 7_8,505+ vues   
> _[**the_critic**](https://stackoverflow.com/users/1066899/the-critic) **a demandé,**_

J'essaie de mettre en œuvre quelque chose comme un modèle de délégation dans Angular. Lorsque l'utilisateur clique sur un `nav-item`, j'aimerais appeler une fonction qui émet ensuite un événement qui devrait être géré par un autre composant à l'écoute de l'événement.

Voici le scénario : J'ai un composant `Navigation` :

```ts
import {Component, Output, EventEmitter} from 'angular2/core';

@Component({
    // autres propriétés omises pour plus de concision
    events : ['navchange'], 
    template:`
      <div class="nav-item" (click)="selectedNavItem(1)"></div>
    `
})

export class Navigation {

    @Output() navchange: EventEmitter<number> = new EventEmitter();
    
    selectedNavItem(item: number) {
        console.log('selected nav item ' + item);
        this.navchange.emit(item)
    }
    
}
```

Voici le composant observateur :

```ts
export class ObservingComponent {

  // Comment puis-je observer l'événement ? 
  // <----------Observe/Register Event ?-------->
  
  public selectedNavItem(item: number) {
    console.log('item index changed!');
  }
  
}
```

La question clé est, comment puis-je faire en sorte que le composant observateur observe l'événement en question ?

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_a répondu, (306+ points)_**

**Mise à jour 2016-06-27 :** au lieu d'utiliser des Observables, utilisez soit

* un BehaviorSubject, comme recommandé par @Abdulrahman dans un commentaire, ou
* un ReplaySubject, comme recommandé par @Jason Goemaat dans un commentaire

Un [Subject](http://reactivex.io/rxjs/manual/overview.html#subject) est à la fois un Observable (donc nous pouvons nous `subscribe()` à celui-ci) et un Observer (donc nous pouvons appeler `next()` sur celui-ci pour émettre une nouvelle valeur). Nous exploitons cette fonctionnalité. Un Subject permet de diffuser des valeurs à de nombreux Observers. Nous n'exploitons pas cette fonctionnalité (nous n'avons qu'un seul Observer).

[BehaviorSubject](http://reactivex.io/rxjs/manual/overview.html#behaviorsubject) est une variante de Subject. Il a la notion de « valeur actuelle ». Nous exploitons cela : chaque fois que nous créons un ObservingComponent, il obtient la valeur actuelle de l'élément de navigation à partir du BehaviorSubject automatiquement.

Le code ci-dessous et le [plunker](http://plnkr.co/edit/XqwwUM44NQEpxQVFFxNW?p=preview) utilisent BehaviorSubject.

[ReplaySubject](http://reactivex.io/rxjs/manual/overview.html#replaysubject) est une autre variante de Subject. Si vous souhaitez attendre qu'une valeur soit réellement produite, utilisez `ReplaySubject(1)`. Alors qu'un BehaviorSubject nécessite une valeur initiale (qui sera fournie immédiatement), ReplaySubject ne le fait pas. ReplaySubject fournira toujours la valeur la plus récente, mais comme il n'a pas de valeur initiale requise, le service peut effectuer une opération asynchrone avant de retourner sa première valeur. Il se déclenchera toujours immédiatement lors des appels suivants avec la valeur la plus récente. Si vous voulez simplement une valeur, utilisez `first()` sur l'abonnement. Vous n'avez pas besoin de vous désabonner si vous utilisez `first()`.

```ts
import {Injectable}      from '@angular/core'
import {BehaviorSubject} from 'rxjs/BehaviorSubject';

@Injectable()
export class NavService {
  // Observable navItem source
  private _navItemSource = new BehaviorSubject<number>(0);
  // Observable navItem stream
  navItem$ = this._navItemSource.asObservable();
  // service command
  changeNav(number) {
    this._navItemSource.next(number);
  }
}

import {Component}    from '@angular/core';
import {NavService}   from './nav.service';
import {Subscription} from 'rxjs/Subscription';

@Component({
  selector: 'obs-comp',
  template: `obs component, item: {{item}}`
})
export class ObservingComponent {
  item: number;
  subscription:Subscription;
  constructor(private _navService:NavService) {}
  ngOnInit() {
    this.subscription = this._navService.navItem$
       .subscribe(item => this.item = item)
  }
  ngOnDestroy() {
    // prevent memory leak when component is destroyed
    this.subscription.unsubscribe();
  }
}

@Component({
  selector: 'my-nav',
  template:`
    <div class="nav-item" (click)="selectedNavItem(1)">nav 1 (click me)</div>
    <div class="nav-item" (click)="selectedNavItem(2)">nav 2 (click me)</div>`
})
export class Navigation {
  item = 1;
  constructor(private _navService:NavService) {}
  selectedNavItem(item: number) {
    console.log('selected nav item ' + item);
    this._navService.changeNav(item);
  }
}
```

[Plunker](http://plnkr.co/edit/XqwwUM44NQEpxQVFFxNW?p=preview)

**Réponse originale utilisant un Observable :** (elle nécessite plus de code et de logique que l'utilisation d'un BehaviorSubject, donc je ne la recommande pas, mais elle peut être instructive)

Voici une implémentation qui utilise un Observable [au lieu d'un EventEmitter](https://stackoverflow.com/a/34402436/215945). Contrairement à mon implémentation EventEmitter, cette implémentation stocke également le `navItem` actuellement sélectionné dans le service, de sorte que lorsqu'un composant observateur est créé, il peut récupérer la valeur actuelle via l'appel d'API `navItem()`, puis être notifié des changements via l'Observable `navChange$`.

```ts
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/share';
import {Observer} from 'rxjs/Observer';

export class NavService {
  private _navItem = 0;
  navChange$: Observable<number>;
  private _observer: Observer;
  constructor() {
    this.navChange$ = new Observable(observer =>
      this._observer = observer).share();
    // share() permet plusieurs abonnés
  }
  changeNav(number) {
    this._navItem = number;
    this._observer.next(number);
  }
  navItem() {
    return this._navItem;
  }
}

@Component({
  selector: 'obs-comp',
  template: `obs component, item: {{item}}`
})
export class ObservingComponent {
  item: number;
  subscription: any;
  constructor(private _navService:NavService) {}
  ngOnInit() {
    this.item = this._navService.navItem();
    this.subscription = this._navService.navChange$.subscribe(
      item => this.selectedNavItem(item));
  }
  selectedNavItem(item: number) {
    this.item = item;
  }
  ngOnDestroy() {
    this.subscription.unsubscribe();
  }
}

@Component({
  selector: 'my-nav',
  template:`
    <div class="nav-item" (click)="selectedNavItem(1)">nav 1 (click me)</div>
    <div class="nav-item" (click)="selectedNavItem(2)">nav 2 (click me)</div>
  `,
})
export class Navigation {
  item:number;
  constructor(private _navService:NavService) {}
  selectedNavItem(item: number) {
    console.log('selected nav item ' + item);
    this._navService.changeNav(item);
  }
}
```

[Plunker](http://plnkr.co/edit/vL76b0UjrAav3Ao7kF4W?p=preview)

Voir aussi l'exemple [Component Interaction Cookbook](https://angular.io/docs/ts/latest/cookbook/component-communication.html#!#bidirectional-service), qui utilise un `Subject` en plus des observables. Bien que l'exemple soit « communication parent et enfants », la même technique est applicable pour des composants non apparentés.

[**Source**](https://stackoverflow.com/questions/34376854)  
**[Haut](#599b)**

### Comment ajouter bootstrap à un projet angular-cli

> 140+ points _? 1_66,741+ vues   
> _[**Jerome**](https://stackoverflow.com/users/811865/jerome) **a demandé,**_

Nous voulons utiliser bootstrap 4 (4.0.0-alpha.2) dans notre application générée avec angular-cli 1.0.0-beta.5 (avec node v6.1.0).

Après avoir obtenu bootstrap et ses dépendances avec npm, notre première approche consistait à les ajouter dans `angular-cli-build.js` :

```js
'bootstrap/dist/**/*.min.+(js|css)',  
  'jquery/dist/jquery.min.+(js|map)',  
  'tether/dist/**/*.min.+(js|css)',
```

et les importer dans notre `index.html`

```html
<script src="vendor/jquery/dist/jquery.min.js"></script>
  <script src="vendor/tether/dist/js/tether.min.js"></script>
  <link rel="stylesheet" type="text/css" href="vendor/bootstrap/dist/css/bootstrap.min.css">
  <script src="vendor/bootstrap/dist/js/bootstrap.min.js"></script>
```

Cela fonctionnait bien avec `ng serve` mais dès que nous avons produit une build avec le flag `-prod`, toutes ces dépendances ont disparu de `dist/vendor` (surprise !).

**Comment devons-nous gérer un tel scénario (c'est-à-dire le chargement des scripts bootstrap) dans un projet généré avec angular-cli ?**

Nous avons eu les réflexions suivantes mais nous ne savons pas vraiment quelle voie prendre...

* utiliser un CDN ? mais nous préférerions servir ces fichiers pour garantir qu'ils seront disponibles
* copier les dépendances dans `dist/vendor` après notre `ng build -prod` ? Mais cela semble être quelque chose que angular-cli devrait fournir puisque cela 'prend en charge' la partie build ?
* ajouter jquery, bootstrap et tether dans src/system-config.ts et d'une manière ou d'une autre les intégrer dans notre bundle dans main.ts ? Mais cela semblait incorrect étant donné que nous n'allons pas les utiliser explicitement dans le code de notre application (contrairement à moment.js ou quelque chose comme lodash, par exemple)

> [**_pd farhad_**](https://stackoverflow.com/users/1417742) **_a répondu, (202+ points)_**

**MISE À JOUR IMPORTANTE : ng2-bootstrap est maintenant remplacé par [ngx-bootstrap](https://github.com/valor-software/ngx-bootstrap) **

ngx-bootstrap supporte à la fois angular 3 et 4.

**Mise à jour :** `**1.0.0-beta.11-webpack**` **ou versions supérieures**

Tout d'abord, vérifiez votre version d'angular-cli avec la commande suivante dans le terminal : `ng -v`

Si votre version d'angular-cli est supérieure à `1.0.0-beta.11-webpack`, vous devez suivre ces étapes :

1. installer **ngx-bootstrap** et **bootstrap** :  
`npm install ngx-bootstrap bootstrap --save`

Cette ligne installe bootstrap 3 de nos jours, mais peut installer bootstrap 4 à l'avenir. Gardez à l'esprit que ngx-bootstrap supporte les deux versions.

1. ouvrir **src/app/app.module.ts** et ajouter  
`import { AlertModule } from 'ngx-bootstrap'; ... @NgModule({ ... imports: [AlertModule.forRoot(), ... ], ... })`
2. ouvrir **angular-cli.json** et insérer une nouvelle entrée dans le tableau styles  
`"styles": [ "styles.css", "../node_modules/bootstrap/dist/css/bootstrap.min.css" ],`
3. ouvrir **src/app/app.component.html** et ajouter  
`<alert type="success">hello&l`t;/alert>

**1.0.0-beta.10 ou versions inférieures :**

Et, si votre version d'angular-cli est 1.0.0-beta.10 ou une version inférieure, vous pouvez utiliser les étapes ci-dessous.

Tout d'abord, allez dans le répertoire du projet et tapez

```
npm install ngx-bootstrap --save
```

ensuite, ouvrez votre **angular-cli-build.js** et ajoutez cette ligne

```js
vendorNpmFiles: [
   ..................
   'ngx-bootstrap/**/*.js',
    ....................
  ]
```

maintenant, ouvrez votre **src/system-config.ts**, écrivez

```ts
const map:any = {
     ..................
   'ngx-bootstrap': 'vendor/ngx-bootstrap',
    ....................
}
```

et

```ts
const packages: any = {
  'ngx-bootstrap': {
    format: 'cjs',
    defaultExtension: 'js',
    main: 'ngx-bootstrap.js'
  }
};
```

[**Source**](https://stackoverflow.com/questions/37649164)  
**[Haut](#599b)**

### accéder à la clé et à la valeur de l'objet en utilisant *ngFor

> 136+ points _? 1_39,816+ vues   
> _[**Pardeep Jain**](https://stackoverflow.com/users/5043867/pardeep-jain) **a demandé,**_

Un peu confus sur la façon d'obtenir `Key and Value` d'un objet dans angular2 tout en utilisant *ngFor pour itérer sur l'objet. Je sais que dans angular 1.x il y a une syntaxe comme

```ts
ng-repeat="(key, value) in demo"
```

mais dans angular2 je ne sais pas, j'ai essayé la même chose mais je n'ai pas réussi. J'ai essayé le code ci-dessous mais il n'a pas fonctionné, s'il vous plaît dites-moi où je me trompe.

```ts
<ul>
  <li *ngFor='#key of demo'>{{key}}</li>
</ul>

demo = {
    'key1': [{'key11':'value11'}, {'key12':'value12'}],
    'key2': [{'key21':'value21'}, {'key22':'value22'}],
  }
```

voici plnkr où j'ai essayé la même chose : [http://plnkr.co/edit/mIj619FncOpfdwrR0KeG?p=preview](http://plnkr.co/edit/mIj619FncOpfdwrR0KeG?p=preview)

Je veux obtenir `key1` et `key2` dynamiquement en utilisant *ngFor. Comment faire ? J'ai beaucoup cherché, j'ai trouvé l'idée d'utiliser un pipe mais je ne sais pas comment l'utiliser. Y a-t-il un pipe intégré pour faire la même chose dans angular2 ?

> [**_Thierry Templier_**](https://stackoverflow.com/users/1873365) **_a répondu, (134+ points)_**

Vous pourriez créer un pipe personnalisé pour retourner la liste des clés pour chaque élément. Quelque chose comme ça :

```ts
import { PipeTransform, Pipe } from '@angular/core';

@Pipe({name: 'keys'})
export class KeysPipe implements PipeTransform {
  transform(value, args:string[]) : any {
    let keys = [];
    for (let key in value) {
      keys.push(key);
    }
    return keys;
  }
}
```

et l'utiliser comme ça :

```ts
<tr *ngFor="let c of content">           
  <td *ngFor="let key of c | keys">{{key}}: {{c[key]}}</td>
</tr>
```

**Édition**

Vous pourriez également retourner une entrée contenant à la fois la clé et la valeur :

```ts
@Pipe({name: 'keys'})
export class KeysPipe implements PipeTransform {
  transform(value, args:string[]) : any {
    let keys = [];
    for (let key in value) {
      keys.push({key: key, value: value[key]});
    }
    return keys;
  }
}
```

et l'utiliser comme ça :

```ts
<span *ngFor="let entry of content | keys">           
  Key: {{entry.key}}, value: {{entry.value}}
</span>
```

[**Source**](https://stackoverflow.com/questions/35534959)  
**[Haut](#599b)**

### Exception Angular : Impossible de lier à 'ngFor' car ce n'est pas une propriété native connue

> 134+ points _? 6_3,054+ vues   
> _[**Mark Rajcok**](https://stackoverflow.com/users/215945/mark-rajcok) **a demandé,**_

Qu'est-ce que je fais de mal ?

```ts
import {bootstrap, Component} from 'angular2/angular2'

@Component({
  selector: 'conf-talks',
  template: `<div *ngFor="talk of talks">
     {{talk.title}} by {{talk.speaker}}
     <p>{{talk.description}}
   </div>`
})
class ConfTalks {
  talks = [ {title: 't1', speaker: 'Brian', description: 'talk 1'},
            {title: 't2', speaker: 'Julie', description: 'talk 2'}];
}
@Component({
  selector: 'my-app',
  directives: [ConfTalks],
  template: '<conf-talks></conf-talks>'
})
class App {}
bootstrap(App, [])
```

L'erreur est

```bash
EXCEPTION: Template parse errors:
Can't bind to 'ngFor' since it isn't a known native property
("<div [ERROR ->]*ngFor="talk of talks">
```

> [**_Mark Rajcok_**](https://stackoverflow.com/users/215945) **_a répondu, (325+ points)_**

J'ai oublié `let` devant `talk` :

```ts
<div *ngFor="let talk of talks">
```

Notez que [à partir de la version beta.17](https://github.com/angular/angular/blob/master/CHANGELOG.md#200-beta17-2016-04-28), l'utilisation de `#...` pour déclarer des variables locales à l'intérieur de directives structurelles comme NgFor est obsolète. Utilisez `let` à la place.   
`<div *ngFor="#talk of talk`s"> devient maintenant <div *ngFor="let talk o`f talks">

Réponse originale :

J'ai oublié `#` devant `talk` :

```ts
<div *ngFor="#talk of talks">
```

Il est si facile d'oublier ce `#`. J'aimerais que le message d'erreur d'exception Angular dise plutôt :  
`vous avez oublié ce # encore`.

[**Source**](https://stackoverflow.com/questions/34012291)  
**[Haut](#599b)**

### Comment ajouter font-awesome à un projet Angular 2 + CLI

> 132+ points _? 7_1,934+ vues   
> _[**Nik**](https://stackoverflow.com/users/1394625/nik) **a demandé,**_

J'utilise Angular 2+ et Angular CLI.

Comment puis-je ajouter font-awesome à mon projet ?

> [**_AIon_**](https://stackoverflow.com/users/5904566) **_a répondu, (285+ points)_**

Après la sortie finale d'Angular 2.0, **la structure du projet Angular2 CLI a été modifiée** — vous n'avez pas besoin de fichiers vendeur, pas de system.js — seulement webpack. Donc vous faites :

1. `npm install font-awesome --save`
2. Dans le fichier angular-cli.json, localisez le tableau `styles[]` et ajoutez les références du répertoire font-awesome ici, comme ci-dessous :   
`apps: [ { root: src, outDir: dist, styles: [ styles.css, ../node_modules/bootstrap/dist/css/bootstrap.css, ../node_modules/font-awesome/css/font-awesome.css // -ici webpack construira automatiquement un élément de lien css à partir de ceci!? ], ... } ] ]`
3. Placez quelques icônes font-awesome dans n'importe quel fichier html que vous voulez :   
`<i class=fa fa-american-sign-language-interpreting fa-5x aria-hidden=true> </i>`
4. Exécutez `ng build` et `ng serve` à nouveau — car les observateurs ne sont que pour le dossier src et angular-cli.json n'est pas observé pour les changements.
5. Profitez de vos icônes awesomes !

[**Source**](https://stackoverflow.com/questions/38796541)  
**[Haut](#599b)**

### Différence entre HTTP et HTTPClient dans angular 4 ?

> 130+ points _? 4_7,082+ vues   
> _[**Aioub Amini**](https://stackoverflow.com/users/3551590/aiyoub-amini) **a demandé,**_

Je veux savoir lequel utiliser pour construire un service web mock afin de tester le programme Angular ?

> [**_AngularInDepth.com_**](https://stackoverflow.com/users/2545680) **_a répondu, (208+ points)_**

Utilisez la classe `HttpClient` du module `HttpClientModule` si vous utilisez Angular 4.3.x et versions supérieures :

```ts
import { HttpClientModule } from '@angular/common/http';

@NgModule({
 imports: [
   BrowserModule,
   HttpClientModule
 ],
 ...
 
 class MyService() {
    constructor(http: HttpClient) {...}
```

C'est une version améliorée de `http` du module `@angular/http` avec les améliorations suivantes :

* Les intercepteurs permettent d'insérer une logique middleware dans le pipeline
* Les objets de requête/réponse immutables
* Les événements de progression pour le téléchargement de la requête et de la réponse

Vous pouvez lire comment cela fonctionne dans [Insider's guide into interceptors and HttpClient mechanics in Angular](https://blog.angularindepth.com/insiders-guide-into-interceptors-and-httpclient-mechanics-in-angular-103fbdb397bf).

* L'accès au corps de la réponse typé et synchrone, y compris le support des types de corps JSON
* JSON est une hypothèse par défaut et n'a plus besoin d'être explicitement analysé
* La vérification post-requête et le framework de test basé sur le flush

À l'avenir, l'ancien client http sera obsolète. Voici les liens vers le [message de commit](https://github.com/angular/angular/commit/37797e2) et la [documentation officielle](https://angular.io/guide/http).

Faites également attention au fait que l'ancien http était injecté en utilisant le jeton de classe `Http` au lieu du nouveau `HttpClient` :

```ts
import { HttpModule } from '@angular/http';

@NgModule({
 imports: [
   BrowserModule,
   HttpModule
 ],
 ...
 
 class MyService() {
    constructor(http: Http) {...}
```

De plus, le nouveau `HttpClient` semble nécessiter `tslib` à l'exécution, vous devez donc l'installer `npm i tslib` et mettre à jour `system.config.js` si vous utilisez `SystemJS` :

```ts
map: {
     ...
    'tslib': 'npm:tslib/tslib.js',
```

Et vous devez ajouter une autre correspondance si vous utilisez SystemJS :

```
'@angular/common/http': 'npm:@angular/common/bundles/common-http.umd.js',
```

[**Source**](https://stackoverflow.com/questions/45129790)  
**[Haut](#599b)**

**C'est tout pour aujourd'hui. Si vous avez trouvé cet article utile, aidez-moi à le partager.** ? ? ?

**Suivez-moi sur [Medium](http://medium.com/wizardnet972) ou [Twitter](https://twitter.com/wizardnet972) pour lire plus sur angular, webpack, typescript, nodejs et javascript! ? ? ?**