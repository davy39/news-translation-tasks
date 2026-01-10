---
title: 'Crochets de cycle de vie Angular : ngOnChanges, ngOnInit et plus'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T21:53:00.000Z'
originalURL: https://freecodecamp.org/news/angular-lifecycle-hooks
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d66740569d1a4ca378c.jpg
tags:
- name: Angular
  slug: angular
- name: hooks
  slug: hooks
seo_title: 'Crochets de cycle de vie Angular : ngOnChanges, ngOnInit et plus'
seo_desc: 'Why do we need lifecycle hooks?

  Modern front-end frameworks move the application from state to state. Data fuels
  these updates. These technologies interact with the data which in turn transitions
  the state. With every state change, there are many spe...'
---

### Pourquoi avons-nous besoin des crochets de cycle de vie ?

Les frameworks front-end modernes font passer l'application d'un état à un autre. Les données alimentent ces mises à jour. Ces technologies interagissent avec les données qui, à leur tour, font évoluer l'état. Avec chaque changement d'état, il y a de nombreux moments spécifiques où certaines ressources deviennent disponibles.

À un moment donné, le template peut être prêt, à un autre, les données auront fini de se charger. Coder pour chaque instance nécessite un moyen de détection. Les crochets de cycle de vie répondent à ce besoin. Les frameworks front-end modernes s'accompagnent d'une variété de crochets de cycle de vie. Angular ne fait pas exception.

## Explication des crochets de cycle de vie

Les crochets de cycle de vie sont des méthodes temporisées. Ils diffèrent par le moment et la raison de leur exécution. La détection des changements déclenche ces méthodes. Elles s'exécutent en fonction des conditions du cycle actuel. Angular exécute constamment la détection des changements sur ses données. Les crochets de cycle de vie aident à gérer ses effets.

Un aspect important de ces crochets est leur ordre d'exécution. Il ne dévie jamais. Ils s'exécutent en fonction d'une série prévisible d'événements de chargement produits par un cycle de détection. Cela les rend prévisibles.

Certaines ressources ne sont disponibles qu'après l'exécution d'un certain crochet. Bien sûr, un crochet ne s'exécute que sous certaines conditions définies dans le cycle actuel de détection des changements.

Cet article présente les crochets de cycle de vie dans l'ordre de leur exécution (s'ils s'exécutent tous). Certaines conditions méritent l'activation d'un crochet. Il y en a quelques-uns qui ne s'exécutent qu'une seule fois après l'initialisation du composant.

Toutes les méthodes de cycle de vie sont disponibles depuis `@angular/core`. Bien que non obligatoire, Angular [recommande d'implémenter chaque crochet](https://angular.io/guide/lifecycle-hooks#interfaces-are-optional-technically). Cette pratique conduit à de meilleurs messages d'erreur concernant le composant.

## Ordre d'exécution des crochets de cycle de vie

### ngOnChanges

`ngOnChanges` se déclenche après la modification des membres de classe liés par `@Input`. Les données liées par le décorateur `@Input()` proviennent d'une source externe. Lorsque la source externe modifie ces données de manière détectable, elles passent à nouveau par la propriété `@Input`.

Avec cette mise à jour, `ngOnChanges` se déclenche immédiatement. Il se déclenche également lors de l'initialisation des données d'entrée. Le crochet reçoit un paramètre optionnel de type `SimpleChanges`. Cette valeur contient des informations sur les propriétés liées en entrée modifiées.

```typescript
import { Component, Input, OnChanges } from '@angular/core';

@Component({
  selector: 'app-child',
  template: `
  <h3>Composant Enfant</h3>
  <p>TICKS : {{ lifecycleTicks }}</p>
  <p>DONNÉES : {{ data }}</p>
  `
})
export class ChildComponent implements OnChanges {
  @Input() data: string;
  lifecycleTicks: number = 0;

  ngOnChanges() {
    this.lifecycleTicks++;
  }
}

@Component({
  selector: 'app-parent',
  template: `
  <h1>Exemple ngOnChanges</h1>
  <app-child [data]="arbitraryData"></app-child>
  `
})
export class ParentComponent {
  arbitraryData: string = 'initial';

  constructor() {
    setTimeout(() => {
      this.arbitraryData = 'final';
    }, 5000);
  }
}
```

**Résumé :** ParentComponent lie les données d'entrée au ChildComponent. Le composant reçoit ces données via sa propriété `@Input`. `ngOnChanges` se déclenche. Après cinq secondes, le callback `setTimeout` se déclenche. ParentComponent modifie la source de données de la propriété liée en entrée de ChildComponent. Les nouvelles données circulent via la propriété d'entrée. `ngOnChanges` se déclenche à nouveau.

### ngOnInit

`ngOnInit` se déclenche une fois lors de l'initialisation des propriétés liées en entrée (`@Input`) d'un composant. L'exemple suivant sera similaire au précédent. Le crochet ne se déclenche pas lorsque ChildComponent reçoit les données d'entrée. Il se déclenche plutôt juste après que les données sont rendues dans le template de ChildComponent.

```typescript
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-child',
  template: `
  <h3>Composant Enfant</h3>
  <p>TICKS : {{ lifecycleTicks }}</p>
  <p>DONNÉES : {{ data }}</p>
  `
})
export class ChildComponent implements OnInit {
  @Input() data: string;
  lifecycleTicks: number = 0;

  ngOnInit() {
    this.lifecycleTicks++;
  }
}

@Component({
  selector: 'app-parent',
  template: `
  <h1>Exemple ngOnInit</h1>
  <app-child [data]="arbitraryData"></app-child>
  `
})
export class ParentComponent {
  arbitraryData: string = 'initial';

  constructor() {
    setTimeout(() => {
      this.arbitraryData = 'final';
    }, 5000);
  }
}
```

**Résumé :** ParentComponent lie les données d'entrée au ChildComponent. ChildComponent reçoit ces données via sa propriété `@Input`. Les données sont rendues dans le template. `ngOnInit` se déclenche. Après cinq secondes, le callback `setTimeout` se déclenche. ParentComponent modifie la source de données de la propriété liée en entrée de ChildComponent. ngOnInit **NE SE DÉCLENCHE PAS**.

`ngOnInit` est un crochet unique. L'initialisation est sa seule préoccupation.

### ngDoCheck

`ngDoCheck` se déclenche à chaque cycle de détection des changements. Angular exécute fréquemment la détection des changements. Effectuer une action quelconque provoquera un cycle. `ngDoCheck` se déclenche avec ces cycles. Utilisez-le avec prudence. Il peut créer des problèmes de performance s'il est mal implémenté.

`ngDoCheck` permet aux développeurs de vérifier leurs données manuellement. Ils peuvent déclencher une nouvelle condition de date d'application de manière conditionnelle. En conjonction avec `ChangeDetectorRef`, les développeurs peuvent créer leurs propres vérifications pour la détection des changements.

```typescript
import { Component, DoCheck, ChangeDetectorRef } from '@angular/core';

@Component({
  selector: 'app-example',
  template: `
  <h1>Exemple ngDoCheck</h1>
  <p>DONNÉES : {{ data[data.length - 1] }}</p>
  `
})
export class ExampleComponent implements DoCheck {
  lifecycleTicks: number = 0;
  oldTheData: string;
  data: string[] = ['initial'];

  constructor(private changeDetector: ChangeDetectorRef) {
    this.changeDetector.detach(); // permet à la classe d'effectuer sa propre détection des changements

    setTimeout(() => {
      this.oldTheData = 'final'; // erreur intentionnelle
      this.data.push('intermédiaire');
    }, 3000);

    setTimeout(() => {
      this.data.push('final');
      this.changeDetector.markForCheck();
    }, 6000);
  }

  ngDoCheck() {
    console.log(++this.lifecycleTicks);

    if (this.data[this.data.length - 1] !== this.oldTheData) {
      this.changeDetector.detectChanges();
    }
  }
}
```

Faites attention à la console par rapport à l'affichage. Les données progressent jusqu'à 'intermédiaire' avant de se figer. Trois cycles de détection des changements se produisent sur cette période comme indiqué dans la console. Un autre cycle de détection des changements se produit lorsque 'final' est poussé à la fin de `this.data`. Un dernier cycle de détection des changements se produit alors. L'évaluation de l'instruction if détermine qu'aucune mise à jour de la vue n'est nécessaire.

**Résumé :** La classe s'instancie après deux cycles de détection des changements. Le constructeur de la classe initie `setTimeout` deux fois. Après trois secondes, le premier `setTimeout` déclenche la détection des changements. `ngDoCheck` marque l'affichage pour une mise à jour. Trois secondes plus tard, le second `setTimeout` déclenche la détection des changements. Aucune mise à jour de la vue nécessaire selon l'évaluation de `ngDoCheck`.

### Avertissement

Avant de continuer, apprenez la différence entre le DOM de contenu et le DOM de vue (DOM signifie Document Object Model).

Le DOM de contenu définit le innerHTML des éléments de directive. Inversement, le DOM de vue est un template de composant excluant tout HTML de template imbriqué dans une directive. Pour une meilleure compréhension, référez-vous à [cet article de blog](http://blog.mgechev.com/2016/01/23/angular2-viewchildren-contentchildren-difference-viewproviders).

### ngAfterContentInit

`ngAfterContentInit` se déclenche après l'initialisation du DOM de contenu du composant (chargement pour la première fois). Attendre les requêtes `@ContentChild(ren)` est le cas d'utilisation principal de ce crochet.

Les requêtes `@ContentChild(ren)` fournissent des références d'éléments pour le DOM de contenu. En tant que telles, elles ne sont pas disponibles avant que le DOM de contenu ne soit chargé. C'est pourquoi `ngAfterContentInit` et son homologue `ngAfterContentChecked` sont utilisés.

```typescript
import { Component, ContentChild, AfterContentInit, ElementRef, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-c',
  template: `
  <p>Je suis C.</p>
  <p>Bonjour le monde !</p>
  `
})
export class CComponent { }

@Component({
  selector: 'app-b',
  template: `
  <p>Je suis B.</p>
  <ng-content></ng-content>
  `
})
export class BComponent implements AfterContentInit {
  @ContentChild("BHeader", { read: ElementRef }) hRef: ElementRef;
  @ContentChild(CComponent, { read: ElementRef }) cRef: ElementRef;

  constructor(private renderer: Renderer2) { }

  ngAfterContentInit() {
    this.renderer.setStyle(this.hRef.nativeElement, 'background-color', 'yellow')

    this.renderer.setStyle(this.cRef.nativeElement.children.item(0), 'background-color', 'pink');
    this.renderer.setStyle(this.cRef.nativeElement.children.item(1), 'background-color', 'red');
  }
}

@Component({
  selector: 'app-a',
  template: `
  <h1>Exemple ngAfterContentInit</h1>
  <p>Je suis A.</p>
  <app-b>
    <h3 #BHeader>DOM de contenu de BComponent</h3>
    <app-c></app-c>
  </app-b>
  `
})
export class AComponent { }
```

Les résultats de la requête `@ContentChild` sont disponibles depuis `ngAfterContentInit`. `Renderer2` met à jour le DOM de contenu de BComponent contenant une balise `h3` et CComponent. C'est un exemple courant de [projection de contenu](https://alligator.io/angular/content-projection-angular).

**Résumé :** Le rendu commence avec AComponent. Pour qu'il se termine, AComponent doit rendre BComponent. BComponent projette le contenu imbriqué dans son élément via l'élément `<ng-content></ng-content>`. CComponent fait partie du contenu projeté. Le contenu projeté termine le rendu. `ngAfterContentInit` se déclenche. BComponent termine le rendu. AComponent termine le rendu. `ngAfterContentInit` ne se déclenchera plus.

### ngAfterContentChecked

`ngAfterContentChecked` se déclenche après chaque cycle de détection des changements ciblant le DOM de contenu. Cela permet aux développeurs de faciliter la réaction du DOM de contenu à la détection des changements. `ngAfterContentChecked` peut se déclencher fréquemment et causer des problèmes de performance s'il est mal implémenté.

`ngAfterContentChecked` se déclenche également pendant les phases d'initialisation d'un composant. Il vient juste après `ngAfterContentInit`.

```typescript
import { Component, ContentChild, AfterContentChecked, ElementRef, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-c',
  template: `
  <p>Je suis C.</p>
  <p>Bonjour le monde !</p>
  `
})
export class CComponent { }

@Component({
  selector: 'app-b',
  template: `
  <p>Je suis B.</p>
  <button (click)="$event">CLIQUER</button>
  <ng-content></ng-content>
  `
})
export class BComponent implements AfterContentChecked {
  @ContentChild("BHeader", { read: ElementRef }) hRef: ElementRef;
  @ContentChild(CComponent, { read: ElementRef }) cRef: ElementRef;

  constructor(private renderer: Renderer2) { }

  randomRGB(): string {
    return `rgb(${Math.floor(Math.random() * 256)},
    ${Math.floor(Math.random() * 256)},
    ${Math.floor(Math.random() * 256)})`;
  }

  ngAfterContentChecked() {
    this.renderer.setStyle(this.hRef.nativeElement, 'background-color', this.randomRGB());
    this.renderer.setStyle(this.cRef.nativeElement.children.item(0), 'background-color', this.randomRGB());
    this.renderer.setStyle(this.cRef.nativeElement.children.item(1), 'background-color', this.randomRGB());
  }
}

@Component({
  selector: 'app-a',
  template: `
  <h1>Exemple ngAfterContentChecked</h1>
  <p>Je suis A.</p>
  <app-b>
    <h3 #BHeader>DOM de contenu de BComponent</h3>
    <app-c></app-c>
  </app-b>
  `
})
export class AComponent { }
```

Cela diffère à peine de `ngAfterContentInit`. Un simple `<button></button>` a été ajouté à BComponent. Cliquer dessus provoque une boucle de détection des changements. Cela active le crochet comme indiqué par la randomisation de `background-color`.

**Résumé :** Le rendu commence avec AComponent. Pour qu'il se termine, AComponent doit rendre BComponent. BComponent projette le contenu imbriqué dans son élément via l'élément `<ng-content></ng-content>`. CComponent fait partie du contenu projeté. Le contenu projeté termine le rendu. `ngAfterContentChecked` se déclenche. BComponent termine le rendu. AComponent termine le rendu. `ngAfterContentChecked` peut se déclencher à nouveau via la détection des changements.

### ngAfterViewInit

`ngAfterViewInit` se déclenche une fois après que le DOM de vue a terminé son initialisation. La vue se charge toujours juste après le contenu. `ngAfterViewInit` attend que les requêtes `@ViewChild(ren)` se résolvent. Ces éléments sont interrogés depuis la même vue du composant.

Dans l'exemple ci-dessous, l'en-tête `h3` de BComponent est interrogé. `ngAfterViewInit` s'exécute dès que les résultats de la requête sont disponibles.

```typescript
import { Component, ViewChild, AfterViewInit, ElementRef, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-c',
  template: `
  <p>Je suis C.</p>
  <p>Bonjour le monde !</p>
  `
})
export class CComponent { }

@Component({
  selector: 'app-b',
  template: `
  <p #BStatement>Je suis B.</p>
  <ng-content></ng-content>
  `
})
export class BComponent implements AfterViewInit {
  @ViewChild("BStatement", { read: ElementRef }) pStmt: ElementRef;

  constructor(private renderer: Renderer2) { }

  ngAfterViewInit() {
    this.renderer.setStyle(this.pStmt.nativeElement, 'background-color', 'yellow');
  }
}

@Component({
  selector: 'app-a',
  template: `
  <h1>Exemple ngAfterViewInit</h1>
  <p>Je suis A.</p>
  <app-b>
    <h3>DOM de contenu de BComponent</h3>
    <app-c></app-c>
  </app-b>
  `
})
export class AComponent { }
```

`Renderer2` change la couleur de fond de l'en-tête de BComponent. Cela indique que l'élément de vue a été interrogé avec succès grâce à `ngAfterViewInit`.

**Résumé :** Le rendu commence avec AComponent. Pour qu'il se termine, AComponent doit rendre BComponent. BComponent projette le contenu imbriqué dans son élément via l'élément `<ng-content></ng-content>`. CComponent fait partie du contenu projeté. Le contenu projeté termine le rendu. BComponent termine le rendu. `ngAfterViewInit` se déclenche. AComponent termine le rendu. `ngAfterViewInit` ne se déclenchera plus.

### ngAfterViewChecked

`ngAfterViewChecked` se déclenche après tout cycle de détection des changements ciblant la vue du composant. Le crochet `ngAfterViewChecked` permet aux développeurs de faciliter l'impact de la détection des changements sur le DOM de vue.

```typescript
import { Component, ViewChild, AfterViewChecked, ElementRef, Renderer2 } from '@angular/core';

@Component({
  selector: 'app-c',
  template: `
  <p>Je suis C.</p>
  <p>Bonjour le monde !</p>
  `
})
export class CComponent { }

@Component({
  selector: 'app-b',
  template: `
  <p #BStatement>Je suis B.</p>
  <button (click)="$event">CLIQUER</button>
  <ng-content></ng-content>
  `
})
export class BComponent implements AfterViewChecked {
  @ViewChild("BStatement", { read: ElementRef }) pStmt: ElementRef;

  constructor(private renderer: Renderer2) { }

  randomRGB(): string {
    return `rgb(${Math.floor(Math.random() * 256)},
    ${Math.floor(Math.random() * 256)},
    ${Math.floor(Math.random() * 256)})`;
  }

  ngAfterViewChecked() {
    this.renderer.setStyle(this.pStmt.nativeElement, 'background-color', this.randomRGB());
  }
}

@Component({
  selector: 'app-a',
  template: `
  <h1>Exemple ngAfterViewChecked</h1>
  <p>Je suis A.</p>
  <app-b>
    <h3>DOM de contenu de BComponent</h3>
    <app-c></app-c>
  </app-b>
  `
})
export class AComponent { }
```

**Résumé :** Le rendu commence avec AComponent. Pour qu'il se termine, AComponent doit rendre BComponent. BComponent projette le contenu imbriqué dans son élément via l'élément `<ng-content></ng-content>`. CComponent fait partie du contenu projeté. Le contenu projeté termine le rendu. BComponent termine le rendu. `ngAfterViewChecked` se déclenche. AComponent termine le rendu. `ngAfterViewChecked` peut se déclencher à nouveau via la détection des changements.

Cliquer sur l'élément `<button></button>` initie un cycle de détection des changements. `ngAfterContentChecked` se déclenche et randomise la `background-color` des éléments interrogés à chaque clic sur le bouton.

### ngOnDestroy

`ngOnDestroy` se déclenche lors de la suppression d'un composant de la vue et du DOM ultérieur. Ce crochet offre une chance de nettoyer les extrémités avant la suppression d'un composant.

```typescript
import { Directive, Component, OnDestroy } from '@angular/core';

@Directive({
  selector: '[appDestroyListener]'
})
export class DestroyListenerDirective implements OnDestroy {
  ngOnDestroy() {
    console.log("Au revoir le monde !");
  }
}

@Component({
  selector: 'app-example',
  template: `
  <h1>Exemple ngOnDestroy</h1>
  <button (click)="toggleDestroy()">TOGGLE DESTROY</button>
  <p appDestroyListener *ngIf="destroy">Je peux être détruit !</p>
  `
})
export class ExampleComponent {
  destroy: boolean = true;

  toggleDestroy() {
    this.destroy = !this.destroy;
  }
}
```

**Résumé :** Le bouton est cliqué. Le membre `destroy` de ExampleComponent bascule sur false. La directive structurelle `*ngIf` évalue à false. `ngOnDestroy` se déclenche. `*ngIf` supprime son hôte `<p></p>`. Ce processus se répète un nombre quelconque de fois en cliquant sur le bouton pour basculer `destroy` sur false.

## Conclusion

Rappelez-vous que certaines conditions doivent être remplies pour chaque crochet. Ils s'exécuteront toujours dans l'ordre les uns par rapport aux autres. Cela rend les crochets suffisamment prévisibles pour travailler avec, même si certains ne s'exécutent pas.

Avec les crochets de cycle de vie, le timing de l'exécution d'une classe est facile. Ils permettent aux développeurs de suivre où la détection des changements se produit et comment l'application doit réagir. Ils attendent le code qui nécessite des dépendances basées sur le chargement disponibles seulement après un certain temps.

Le cycle de vie des composants caractérise les frameworks front-end modernes. Angular expose son cycle de vie en fournissant les crochets mentionnés ci-dessus.

## **Sources**

* [Angular Team. « Lifecycle Hooks ». Google. Consulté le 2 juin 2018](https://angular.io/guide/lifecycle-hooks)
* [Gechev, Minko. « ViewChildren and ContentChildren in Angular ». Consulté le 2 juin 2018](http://blog.mgechev.com/2016/01/23/angular2-viewchildren-contentchildren-difference-viewproviders)

## **Ressources**

* [Documentation Angular](https://angular.io/docs)
* [Dépôt GitHub Angular](https://github.com/angular/angular)
* [Crochets de cycle de vie en profondeur](https://angular.io/guide/lifecycle-hooks)