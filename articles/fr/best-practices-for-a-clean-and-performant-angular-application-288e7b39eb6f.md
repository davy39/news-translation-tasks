---
title: Meilleures pratiques pour une application Angular propre et performante
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-03T22:45:55.000Z'
originalURL: https://freecodecamp.org/news/best-practices-for-a-clean-and-performant-angular-application-288e7b39eb6f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*q3-4kypImPD0VDPg.jpg
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Meilleures pratiques pour une application Angular propre et performante
seo_desc: 'By Vamsi Vempati

  I have been working on a large scale Angular application at Trade Me, New Zealand
  for a couple of years now. Over the past few years, our team has been refining our
  application both in terms of coding standards and performance to mak...'
---

Par Vamsi Vempati

Je travaille sur une application Angular à grande échelle chez [Trade Me](https://trademe.nz) en Nouvelle-Zélande depuis quelques années. Au cours des dernières années, notre équipe a affiné notre application à la fois en termes de normes de codage et de performance pour la rendre dans son meilleur état possible.

Cet article décrit les pratiques que nous utilisons dans notre application et est lié à Angular, Typescript, RxJs et @ngrx/store. Nous allons également passer en revue quelques directives de codage générales pour aider à rendre l'application plus propre.

#### **1) trackBy**

Lorsque vous utilisez `ngFor` pour boucler sur un tableau dans les templates, utilisez-le avec une fonction `trackBy` qui retournera un identifiant unique pour chaque élément.

**Pourquoi ?**

Lorsque un tableau change, Angular ré-exécute tout l'arbre DOM. Mais si vous utilisez `trackBy`, Angular saura quel élément a changé et ne fera des changements DOM que pour cet élément particulier.

Pour une explication détaillée sur ce sujet, veuillez vous référer à [cet article](https://netbasal.com/angular-2-improve-performance-with-trackby-cc147b5104e5) de [Netanel Basal](https://www.freecodecamp.org/news/best-practices-for-a-clean-and-performant-angular-application-288e7b39eb6f/undefined).

**Avant**

```ts
<li *ngFor="let item of items;">{{ item }}</li>
```

**Après**

```ts
// dans le template

<li *ngFor="let item of items; trackBy: trackByFn">{{ item }}</li>

// dans le composant

trackByFn(index, item) {    
   return item.id; // identifiant unique correspondant à l'élément
}
```

#### **2) const vs let**

Lorsque vous déclarez des variables, utilisez const lorsque la valeur ne sera pas réassignée.

**Pourquoi ?**

Utiliser `let` et `const` de manière appropriée rend l'intention des déclarations plus claire. Cela aidera également à identifier les problèmes lorsque une valeur est réassignée à une constante accidentellement en lançant une erreur de compilation. Cela améliore également la lisibilité du code.

**Avant**

```ts
let car = 'ludicrous car';

let myCar = `My ${car}`;
let yourCar = `Your ${car};

if (iHaveMoreThanOneCar) {
   myCar = `${myCar}s`;
}

if (youHaveMoreThanOneCar) {
   yourCar = `${youCar}s`;
}
```

**Après**

```ts
// la valeur de car n'est pas réassignée, donc nous pouvons en faire une const
const car = 'ludicrous car';

let myCar = `My ${car}`;
let yourCar = `Your ${car};

if (iHaveMoreThanOneCar) {
   myCar = `${myCar}s`;
}

if (youHaveMoreThanOneCar) {
   yourCar = `${youCar}s`;
}
```

#### 3) Opérateurs pipeables

Utilisez des opérateurs pipeables lorsque vous utilisez des opérateurs RxJs.

**Pourquoi ?**

Les opérateurs pipeables sont tree-shakeable, ce qui signifie que seul le code dont nous avons besoin pour l'exécution sera inclus lorsqu'ils sont importés.

Cela facilite également l'identification des opérateurs inutilisés dans les fichiers.

_Note:_ Cela nécessite Angular version 5.5+.

**Avant**

```ts
import 'rxjs/add/operator/map';
import 'rxjs/add/operator/take';

iAmAnObservable
    .map(value => value.item)
    .take(1);
```

**Après**

```ts
import { map, take } from 'rxjs/operators';

iAmAnObservable
    .pipe(
       map(value => value.item),
       take(1)
     );
```

#### 4) Isoler les hacks API

Toutes les API ne sont pas infaillibles — parfois nous devons ajouter une logique dans le code pour compenser les bugs dans les API. Au lieu d'avoir les hacks dans les composants où ils sont nécessaires, il est préférable de les isoler en un seul endroit — comme dans un service et utiliser le service depuis le composant.

**Pourquoi ?**

Cela aide à garder les hacks « plus proches de l'API », donc aussi proches que possible de l'endroit où la requête réseau est faite. De cette façon, moins de votre code traite avec le code non hacké. De plus, c'est un endroit où tous les hacks vivent et il est plus facile de les trouver. Lorsque vous corrigez les bugs dans les API, il est plus facile de les chercher dans un seul fichier plutôt que de chercher les hacks qui pourraient être répartis dans la base de code.

Vous pouvez également créer des tags personnalisés comme API_FIX similaires à TODO et taguer les corrections avec pour qu'il soit plus facile de les trouver.

#### 5) Souscrire dans le template

Évitez de souscrire aux observables depuis les composants et souscrivez plutôt aux observables depuis le template.

**Pourquoi ?**

Les pipes `async` se désabonnent automatiquement et simplifient le code en éliminant le besoin de gérer manuellement les abonnements. Cela réduit également le risque d'oublier accidentellement de se désabonner d'un abonnement dans le composant, ce qui causerait une fuite de mémoire. Ce risque peut également être atténué en utilisant une règle de lint pour détecter les observables non désabonnés.

Cela empêche également les composants d'être stateful et d'introduire des bugs où les données sont mutées en dehors de l'abonnement.

**Avant**

```
// // template

<p>{{ textToDisplay }}</p>

// composant

iAmAnObservable
    .pipe(
       map(value => value.item),
       takeUntil(this._destroyed$)
     )
    .subscribe(item => this.textToDisplay = item);
```

**Après**

```ts
// template

<p>{{ textToDisplay$ | async }}</p>

// composant

this.textToDisplay$ = iAmAnObservable
    .pipe(
       map(value => value.item)
     );
```

#### **6) Nettoyer les abonnements**

Lorsque vous vous abonnez à des observables, assurez-vous toujours de vous désabonner d'eux de manière appropriée en utilisant des opérateurs comme `take`, `takeUntil`, etc.

**Pourquoi ?**

Ne pas se désabonner des observables entraînera des fuites de mémoire indésirables car le flux observable reste ouvert, potentiellement même après qu'un composant a été détruit / l'utilisateur a navigué vers une autre page.

Mieux encore, créez une règle de lint pour détecter les observables qui ne sont pas désabonnés.

**Avant**

```
iAmAnObservable
    .pipe(
       map(value => value.item)     
     )
    .subscribe(item => this.textToDisplay = item);
```

**Après**

Utilisation de `takeUntil` lorsque vous souhaitez écouter les changements jusqu'à ce qu'un autre observable émette une valeur :

```
private _destroyed$ = new Subject();

public ngOnInit (): void {
    iAmAnObservable
    .pipe(
       map(value => value.item)
      // Nous voulons écouter iAmAnObservable jusqu'à ce que le composant soit détruit,
       takeUntil(this._destroyed$)
     )
    .subscribe(item => this.textToDisplay = item);
}

public ngOnDestroy (): void {
    this._destroyed$.next();
    this._destroyed$.complete();
}
```

L'utilisation d'un sujet privé comme celui-ci est un modèle pour gérer le désabonnement de nombreux observables dans le composant.

Utilisation de `take` lorsque vous voulez uniquement la première valeur émise par l'observable :

```ts
iAmAnObservable
    .pipe(
       map(value => value.item),
       take(1),
       takeUntil(this._destroyed$)
    )
    .subscribe(item => this.textToDisplay = item);
```

Notez l'utilisation de `takeUntil` avec `take` ici. Cela permet d'éviter les fuites de mémoire causées lorsque l'abonnement n'a pas reçu de valeur avant que le composant ne soit détruit. Sans `takeUntil` ici, l'abonnement resterait en attente jusqu'à ce qu'il obtienne la première valeur, mais comme le composant a déjà été détruit, il ne recevra jamais de valeur — ce qui entraînerait une fuite de mémoire.

#### 7) Utiliser des opérateurs appropriés

Lorsque vous utilisez des opérateurs d'aplatissement avec vos observables, utilisez l'opérateur approprié pour la situation.

_switchMap:_ lorsque vous souhaitez ignorer les émissions précédentes lorsqu'il y a une nouvelle émission

_mergeMap:_ lorsque vous souhaitez gérer simultanément toutes les émissions

_concatMap:_ lorsque vous souhaitez gérer les émissions les unes après les autres au fur et à mesure qu'elles sont émises

_exhaustMap:_ lorsque vous souhaitez annuler toutes les nouvelles émissions pendant le traitement d'une émission précédente

Pour une explication plus détaillée sur ce sujet, veuillez vous référer à [cet article](https://blog.angularindepth.com/switchmap-bugs-b6de69155524) de [Nicholas Jamieson](https://www.freecodecamp.org/news/best-practices-for-a-clean-and-performant-angular-application-288e7b39eb6f/undefined).

**Pourquoi ?**

L'utilisation d'un seul opérateur lorsque cela est possible au lieu d'enchaîner plusieurs autres opérateurs pour obtenir le même effet peut réduire la quantité de code envoyée à l'utilisateur. L'utilisation de mauvais opérateurs peut entraîner un comportement indésirable, car différents opérateurs gèrent les observables de différentes manières.

#### 8) Chargement paresseux

Lorsque cela est possible, essayez de charger paresseusement les modules dans votre application Angular. Le chargement paresseux consiste à charger quelque chose uniquement lorsqu'il est utilisé, par exemple, charger un composant uniquement lorsqu'il doit être vu.

**Pourquoi ?**

Cela réduira la taille de l'application à charger et peut améliorer le temps de démarrage de l'application en ne chargeant pas les modules qui ne sont pas utilisés.

**Avant**

```
// app.routing.ts

{ path: 'not-lazy-loaded', component: NotLazyLoadedComponent }
```

**Après**

```ts
// app.routing.ts

{ 
  path: 'lazy-load',
  loadChildren: 'lazy-load.module#LazyLoadModule' 
}

// lazy-load.module.ts
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { LazyLoadComponent }   from './lazy-load.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild([
         { 
             path: '',
             component: LazyLoadComponent 
         }
    ])
  ],
  declarations: [
    LazyLoadComponent
  ]
})
export class LazyModule {}
```

#### 9) Éviter d'avoir des abonnements dans des abonnements

Parfois, vous pouvez vouloir des valeurs de plus d'un observable pour effectuer une action. Dans ce cas, évitez de vous abonner à un observable dans le bloc d'abonnement d'un autre observable. Au lieu de cela, utilisez des opérateurs de chaînage appropriés. Les opérateurs de chaînage s'exécutent sur des observables de l'opérateur précédent. Certains opérateurs de chaînage sont : `withLatestFrom`, `combineLatest`, etc.

**Avant**

```
firstObservable$.pipe(
   take(1)
)
.subscribe(firstValue => {
    secondObservable$.pipe(
        take(1)
    )
    .subscribe(secondValue => {
        console.log(`Combined values are: ${firstValue} & ${secondValue}`);
    });
});
```

**Après**

```ts
firstObservable$.pipe(
    withLatestFrom(secondObservable$),
    first()
)
.subscribe(([firstValue, secondValue]) => {
    console.log(`Combined values are: ${firstValue} & ${secondValue}`);
});
```

**Pourquoi ?**

_Mauvaise odeur/lisibilité/complexité_ : Ne pas utiliser RxJs à son plein potentiel, suggère que le développeur n'est pas familier avec la surface de l'API RxJs.

_Performance_ : Si les observables sont froids, il s'abonnera à firstObservable, attendra qu'il se termine, puis commencera le travail du second observable. Si ce étaient des requêtes réseau, cela apparaîtrait comme synchrone/en cascade.

#### 10) Éviter any; tout typer;

Déclarez toujours les variables ou constantes avec un type autre que `any`.

**Pourquoi ?**

Lorsque vous déclarez des variables ou des constantes en Typescript sans typage, le typage de la variable/constante sera déduit par la valeur qui lui est assignée. Cela causera des problèmes non intentionnels. Un exemple classique est :

```
const x = 1;
const y = 'a';
const z = x + y;

console.log(`Value of z is: ${z}`

// Output
Value of z is 1a
```

Cela peut causer des problèmes indésirables lorsque vous attendez que y soit également un nombre. Ces problèmes peuvent être évités en typant les variables de manière appropriée.

```
const x: number = 1;
const y: number = 'a';
const z: number = x + y;

// Cela donnera une erreur de compilation disant :

Type '"a"' is not assignable to type 'number'.

const y:number
```

De cette façon, nous pouvons éviter les bugs causés par des types manquants.

Un autre avantage d'avoir de bons typages dans votre application est que cela facilite et sécurise le refactoring.

Considérez cet exemple :

```
public ngOnInit (): void {
    let myFlashObject = {
        name: 'My cool name',
        age: 'My cool age',
        loc: 'My cool location'
    }
    this.processObject(myFlashObject);
}

public processObject(myObject: any): void {
    console.log(`Name: ${myObject.name}`);
    console.log(`Age: ${myObject.age}`);
    console.log(`Location: ${myObject.loc}`);
}

// Output
Name: My cool name
Age: My cool age
Location: My cool location
```

Supposons que nous voulons renommer la propriété `loc` en `location` dans `myFlashObject` :

```
public ngOnInit (): void {
    let myFlashObject = {
        name: 'My cool name',
        age: 'My cool age',
        location: 'My cool location'
    }
    this.processObject(myFlashObject);
}

public processObject(myObject: any): void {
    console.log(`Name: ${myObject.name}`);
    console.log(`Age: ${myObject.age}`);
    console.log(`Location: ${myObject.loc}`);
}

// Output
Name: My cool name
Age: My cool age
Location: undefined
```

Si nous n'avons pas de typage sur `myFlashObject`, il pense que la propriété `loc` sur `myFlashObject` est simplement indéfinie plutôt que de ne pas être une propriété valide.

Si nous avions un typage pour `myFlashObject`, nous obtiendrions une belle erreur de compilation comme montré ci-dessous :

```
type FlashObject = {
    name: string,
    age: string,
    location: string
}

public ngOnInit (): void {
    let myFlashObject: FlashObject = {
        name: 'My cool name',
        age: 'My cool age',
        // Erreur de compilation
        Type '{ name: string; age: string; loc: string; }' is not assignable to type 'FlashObjectType'.
        Object literal may only specify known properties, and 'loc' does not exist in type 'FlashObjectType'.
        loc: 'My cool location'
    }
    this.processObject(myFlashObject);
}

public processObject(myObject: FlashObject): void {
    console.log(`Name: ${myObject.name}`);
    console.log(`Age: ${myObject.age}`)
    // Erreur de compilation
    Property 'loc' does not exist on type 'FlashObjectType'.
    console.log(`Location: ${myObject.loc}`);
}
```

Si vous commencez un nouveau projet, il vaut la peine de définir `strict:true` dans le fichier `tsconfig.json` pour activer toutes les options de vérification de type strict.

#### 11) Utiliser des règles de lint

`[tslint](https://palantir.github.io/tslint/)` a diverses options intégrées comme `[no-any](https://palantir.github.io/tslint/rules/no-any)`, `[no-magic-numbers](https://palantir.github.io/tslint/rules/no-magic-numbers)`, `[no-console](https://palantir.github.io/tslint/rules/no-console)`, etc. que vous pouvez configurer dans votre `tslint.json` pour imposer certaines règles dans votre base de code.

**Pourquoi ?**

Avoir des règles de lint en place signifie que vous obtiendrez une belle erreur lorsque vous faites quelque chose que vous ne devriez pas faire. Cela imposera la cohérence dans votre application et la lisibilité. Veuillez vous référer [ici](https://palantir.github.io/tslint/rules/) pour plus de règles que vous pouvez configurer.

Certaines règles de lint viennent même avec des correctifs pour résoudre l'erreur de lint. Si vous souhaitez configurer votre propre règle de lint personnalisée, vous pouvez le faire également. Veuillez vous référer à [cet article](https://medium.com/@phenomnominal/custom-typescript-lint-rules-with-tsquery-and-tslint-144184b6ff2d) de [Craig Spence](https://www.freecodecamp.org/news/best-practices-for-a-clean-and-performant-angular-application-288e7b39eb6f/undefined) sur la façon d'écrire vos propres règles de lint personnalisées en utilisant [TSQuery](https://github.com/phenomnomnominal/tsquery).

**Avant**

```
public ngOnInit (): void {
    console.log('I am a naughty console log message');
    console.warn('I am a naughty console warning message');
    console.error('I am a naughty console error message');
}

// Output
No errors, prints the below on console window:
I am a naughty console message
I am a naughty console warning message
I am a naughty console error message
```

**Après**

```
// tslint.json
{
    "rules": {
        .......
        "no-console": [
             true,
             "log",    // no console.log allowed
             "warn"    // no console.warn allowed
        ]
   }
}

// ..component.ts

public ngOnInit (): void {
    console.log('I am a naughty console log message');
    console.warn('I am a naughty console warning message');
    console.error('I am a naughty console error message');
}

// Output
Lint errors for console.log and console.warn statements and no error for console.error as it is not mentioned in the config

Calls to 'console.log' are not allowed.
Calls to 'console.warn' are not allowed.
```

#### 12) Petits composants réutilisables

Extrayez les morceaux qui peuvent être réutilisés dans un composant et faites-en un nouveau. Rendez le composant aussi simple que possible, car cela le rendra fonctionnel dans plus de scénarios. Rendre un composant simple signifie que le composant n'a aucune logique spéciale et fonctionne purement sur la base des entrées et sorties qui lui sont fournies.

En règle générale, le dernier enfant dans l'arbre des composants sera le plus simple de tous.

**Pourquoi ?**

Les composants réutilisables réduisent la duplication de code, ce qui les rend plus faciles à maintenir et à modifier.

Les composants simples sont plus faciles, donc ils sont moins susceptibles d'avoir des bugs. Les composants simples vous font réfléchir plus dur sur l'API publique du composant, et aident à détecter les préoccupations mélangées.

#### 13) Les composants ne doivent traiter que la logique d'affichage

Évitez d'avoir une logique autre que la logique d'affichage dans votre composant chaque fois que vous le pouvez et faites en sorte que le composant ne traite que la logique d'affichage.

**Pourquoi ?**

Les composants sont conçus à des fins de présentation et contrôlent ce que la vue doit faire. Toute logique métier doit être extraite dans ses propres méthodes/services lorsque cela est approprié, en séparant la logique métier de la logique de vue.

La logique métier est généralement plus facile à tester unitairement lorsqu'elle est extraite dans un service, et peut être réutilisée par d'autres composants qui ont besoin de la même logique métier appliquée.

#### 14) Éviter les méthodes longues

Les méthodes longues indiquent généralement qu'elles font trop de choses. Essayez d'utiliser le principe de responsabilité unique. La méthode dans son ensemble peut faire une chose, mais à l'intérieur, il peut y avoir quelques autres opérations qui pourraient se produire. Nous pouvons extraire ces méthodes dans leur propre méthode et leur faire faire une chose chacune et les utiliser à la place.

**Pourquoi ?**

Les méthodes longues sont difficiles à lire, à comprendre et à maintenir. Elles sont également sujettes aux bugs, car changer une chose peut affecter beaucoup d'autres choses dans cette méthode. Elles rendent également le refactoring (qui est une chose clé dans toute application) difficile.

Cela est parfois mesuré comme « [complexité cyclomatique](https://en.wikipedia.org/wiki/Cyclomatic_complexity) ». Il existe également certaines [règles TSLint](https://www.npmjs.com/package/tslint-sonarts) pour détecter la complexité cyclomatique/cognitive, que vous pourriez utiliser dans votre projet pour éviter les bugs et détecter les mauvaises odeurs de code et les problèmes de maintenabilité.

#### 15) DRY

Ne vous répétez pas. Assurez-vous de ne pas avoir le même code copié à différents endroits dans la base de code. Extrayez le code répétitif et utilisez-le à la place du code dupliqué.

**Pourquoi ?**

Avoir le même code à plusieurs endroits signifie que si nous voulons apporter une modification à la logique de ce code, nous devons le faire à plusieurs endroits. Cela rend la maintenance difficile et est également sujet aux bugs où nous pourrions oublier de le mettre à jour dans toutes les occurrences. Cela prend plus de temps pour apporter des modifications à la logique et le tester est également un processus long.

Dans ces cas, extrayez le code répétitif et utilisez-le à la place. Cela signifie un seul endroit à changer et une seule chose à tester. Avoir moins de code dupliqué envoyé aux utilisateurs signifie que l'application sera plus rapide.

#### 16) Ajouter des mécanismes de cache

Lorsque vous effectuez des appels API, les réponses de certaines d'entre elles ne changent pas souvent. Dans ces cas, vous pouvez ajouter un mécanisme de cache et stocker la valeur de l'API. Lorsqu'une autre requête à la même API est faite, vérifiez s'il y a une valeur pour celle-ci dans le cache et, si oui, utilisez-la. Sinon, effectuez l'appel API et mettez le résultat en cache.

Si les valeurs changent mais pas fréquemment, vous pouvez introduire un temps de cache où vous pouvez vérifier quand il a été mis en cache pour la dernière fois et décider si vous appelez l'API ou non.

**Pourquoi ?**

Avoir un mécanisme de cache signifie éviter les appels API indésirables. En ne faisant les appels API que lorsque cela est nécessaire et en évitant la duplication, la vitesse de l'application s'améliore car nous n'avons pas à attendre le réseau. Cela signifie également que nous ne téléchargeons pas les mêmes informations encore et encore.

#### 17) Éviter la logique dans les templates

Si vous avez une logique dans vos templates, même si c'est une simple clause `&&`, il est bon de l'extraire dans son composant.

**Pourquoi ?**

Avoir de la logique dans le template signifie qu'il n'est pas possible de le tester unitairement et donc il est plus sujet aux bugs lors de la modification du code du template.

**Avant**

```
// template
<p *ngIf="role==='developer'"> Status: Developer </p>

// composant
public ngOnInit (): void {
    this.role = 'developer';
}
```

**Après**

```ts
// template
<p *ngIf="showDeveloperStatus"> Status: Developer </p>

// composant
public ngOnInit (): void {
    this.role = 'developer';
    this.showDeveloperStatus = true;
}
```

#### 18) Les chaînes de caractères doivent être sûres

Si vous avez une variable de type chaîne de caractères qui ne peut avoir qu'un ensemble de valeurs, au lieu de la déclarer comme un type chaîne de caractères, vous pouvez déclarer la liste des valeurs possibles comme le type.

**Pourquoi ?**

En déclarant le type de la variable de manière appropriée, nous pouvons éviter les bugs lors de l'écriture du code au moment de la compilation plutôt qu'au moment de l'exécution.

**Avant**

```
private myStringValue: string;

if (itShouldHaveFirstValue) {
   myStringValue = 'First';
} else {
   myStringValue = 'Second'
}
```

**Après**

```ts
private myStringValue: 'First' | 'Second';

if (itShouldHaveFirstValue) {
   myStringValue = 'First';
} else {
   myStringValue = 'Other'
}

// Cela donnera l'erreur ci-dessous
Type '"Other"' is not assignable to type '"First" | "Second"'
(property) AppComponent.myValue: "First" | "Second"
```

### **Vue d'ensemble**

#### Gestion d'état

Envisagez d'utiliser [@ngrx/store](https://github.com/ngrx/platform) pour maintenir l'état de votre application et [@ngrx/effects](https://github.com/ngrx/effects) comme modèle d'effet secondaire pour le store. Les changements d'état sont décrits par les actions et les changements sont effectués par des fonctions pures appelées réducteurs.

**Pourquoi ?**

_@ngrx/store_ isole toute la logique liée à l'état en un seul endroit et la rend cohérente dans toute l'application. Il dispose également d'un mécanisme de mémoisation en place lors de l'accès aux informations dans le store, ce qui conduit à une application plus performante. _@ngrx/store_ combiné avec la stratégie de détection des changements d'Angular conduit à une application plus rapide.

#### État immutable

Lorsque vous utilisez _@ngrx/store_, envisagez d'utiliser [ngrx-store-freeze](https://github.com/brandonroberts/ngrx-store-freeze) pour rendre l'état immutable. _ngrx-store-freeze_ empêche l'état d'être muté en lançant une exception. Cela évite la mutation accidentelle de l'état, ce qui entraîne des conséquences indésirables.

**Pourquoi ?**

La mutation de l'état dans les composants conduit à ce que l'application se comporte de manière incohérente en fonction de l'ordre de chargement des composants. Cela brise le modèle mental du motif redux. Les changements peuvent finir par être écrasés si l'état du store change et ré-émet. Séparation des préoccupations — les composants sont la couche de vue, ils ne devraient pas savoir comment changer l'état.

#### Jest

[Jest](https://jestjs.io/) est le framework de test unitaire de Facebook pour JavaScript. Il rend les tests unitaires plus rapides en parallélisant les exécutions de tests dans la base de code. Avec son mode watch, seuls les tests liés aux changements effectués sont exécutés, ce qui rend la boucle de feedback pour les tests beaucoup plus courte. Jest fournit également une couverture de code des tests et est supporté sur VS Code et Webstorm.

Vous pourriez utiliser un [préréglage](https://github.com/thymikee/jest-preset-angular) pour Jest qui fera la majeure partie du travail pour vous lors de la configuration de Jest dans votre projet.

#### Karma

[Karma](https://karma-runner.github.io/2.0/index.html) est un exécuteur de tests développé par l'équipe AngularJS. Il nécessite un vrai navigateur/DOM pour exécuter les tests. Il peut également s'exécuter sur différents navigateurs. Jest n'a pas besoin de chrome headless/phantomjs pour exécuter les tests et il s'exécute en pur Node.

#### Universal

Si vous n'avez pas encore rendu votre application _Universal_, c'est le bon moment pour le faire. [Angular Universal](https://angular.io/guide/universal) vous permet d'exécuter votre application Angular sur le serveur et effectue un rendu côté serveur (SSR) qui sert des pages HTML pré-rendues statiques. Cela rend l'application super rapide car elle affiche le contenu à l'écran presque instantanément, sans avoir à attendre le chargement et l'analyse des bundles JS, ou le démarrage d'Angular.

Il est également SEO friendly, car Angular Universal génère du contenu statique et facilite l'indexation de l'application par les robots d'indexation et la rend recherchable sans exécuter JavaScript.

**Pourquoi ?**

Universal améliore considérablement les performances de votre application. Nous avons récemment mis à jour notre application pour effectuer un rendu côté serveur et le temps de chargement du site est passé de plusieurs secondes à quelques millisecondes !!

Il permet également à votre site de s'afficher correctement dans les extraits de prévisualisation des réseaux sociaux. La première peinture significative est vraiment rapide et rend le contenu visible pour les utilisateurs sans aucun délai indésirable.

### Conclusion

La construction d'applications est un voyage constant, et il y a toujours place à l'amélioration. Cette liste d'optimisations est un bon point de départ, et l'application cohérente de ces modèles rendra votre équipe heureuse. Vos utilisateurs vous aimeront également pour la belle expérience avec votre application moins boguée et performante.

_Merci d'avoir lu ! Si vous avez aimé cet article, n'hésitez pas à_ ? _et aidez les autres à le trouver. N'hésitez pas à partager vos pensées dans la section des commentaires ci-dessous. Suivez-moi sur [Medium](https://medium.com/@vamsivempati) ou [Twitter](https://twitter.com/_VamsiVempati_) pour plus d'articles. Bon codage les gars !! ?_ f495f3fb