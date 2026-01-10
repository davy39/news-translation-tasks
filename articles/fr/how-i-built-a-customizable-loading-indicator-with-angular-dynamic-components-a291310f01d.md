---
title: Comment j'ai créé un indicateur de chargement personnalisable avec les composants
  dynamiques d'Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-06T17:27:13.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-customizable-loading-indicator-with-angular-dynamic-components-a291310f01d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1yD1jhrSV5Kmd7Ee4OMxPg.jpeg
tags:
- name: Angular
  slug: angular
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai créé un indicateur de chargement personnalisable avec les
  composants dynamiques d'Angular
seo_desc: 'By Balázs Tápai

  Recently, I wrote a blog post about creating a reusable loading-indicator component
  for Angular projects. The next step is making the indicator part customizable. But
  how exactly do you insert your component into the overlay? That is ...'
---

Par Balázs Tápai

Récemment, j'ai écrit un [article de blog](https://medium.com/@balazs.tapai1990/how-to-create-reusable-loading-indicator-for-angular-projects-d0a11f4631e0?source=friends_link&sk=9022f72306ac9adf2aea163dfa15fb05) sur la création d'un composant d'indicateur de chargement réutilisable pour les projets Angular. L'étape suivante consiste à rendre la partie indicateur personnalisable. Mais comment insérez-vous exactement votre composant dans la superposition ? C'est là que les composants dynamiques peuvent nous aider.

**_Note:_** _Depuis mon précédent article de blog, j'ai refactorisé certaines parties de la bibliothèque. N'hésitez pas à consulter le [dépôt git](https://github.com/TapaiBalazs/angular-reusables)._

Le cas d'utilisation est que nous avons un indicateur de chargement très facile à utiliser. Par défaut, il a un spinner, et il peut être déclenché en utilisant les méthodes de décorateur de la bibliothèque. Cependant, notre utilisateur final veut uniquement afficher "Chargement..." sur la superposition. Nous pouvons copier la logique et remplacer le spinner par le texte lui-même, mais cela serait plutôt redondant.

Pour pouvoir utiliser des composants dynamiques, nous devons d'abord implémenter un décorateur simple. Ce décorateur permet d'injecter notre propre composant dans le template.

```typescript
import { Directive, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[btpIndicatorHost]',
})
export class IndicatorHostDirective {
  constructor(public viewContainerRef: ViewContainerRef) { }
}
```

Nous devons ajouter cette directive au NgModule de notre bibliothèque. Ensuite, remplacer le composant spinner à l'intérieur du template de l'indicateur de chargement par ce qui suit :

```html
<btp-overlay>
  <div class="btp-loading-indicator__container" [style.width]="indicatorSize" [style.height]="indicatorSize">
    <ng-template btpIndicatorHost></ng-template>
  </div>
</btp-overlay>
```

Maintenant que nous avons ce template, nous devons faire 3 choses dans le composant de l'indicateur de chargement.

1. Injecter le ComponentFactoryResolver dans le composant.
2. Utiliser le décorateur @ViewChild pour obtenir notre hôte d'indicateur.
3. Charger le composant fourni.

```typescript
import {Component, ComponentFactoryResolver, ComponentRef, Inject, OnDestroy, OnInit, ViewChild} from '@angular/core';
import {LOADING_INDICATOR_CONFIG} from '../loading-indicator.config';
import {LoadingIndicatorConfig} from '../interfaces/loading-indicator.interfaces';
import {IndicatorHostDirective} from '../directives/indicator-host.directive';
import {SpinnerComponent} from '../spinner/spinner.component';
import {DEFAULT_SIZE, INDICATOR_COLOR} from '../constants/indicator.constants';

@Component({
  selector: 'btp-loading-indicator',
  templateUrl: './loading-indicator.component.html',
  styleUrls: ['./loading-indicator.component.css']
})
export class LoadingIndicatorComponent implements OnInit, OnDestroy {
  @ViewChild(IndicatorHostDirective)
  host: IndicatorHostDirective;

  constructor(@Inject(LOADING_INDICATOR_CONFIG)
              private config: LoadingIndicatorConfig,
              private componentFactoryResolver: ComponentFactoryResolver) {
  }

  get indicatorSize(): string {
    return `${this.config.size}px`;
  }

  ngOnInit(): void {
    this.loadComponent();
  }

  ngOnDestroy(): void {
    this.host.viewContainerRef.clear();
  }

  private loadComponent() {
    const component = this.config.indicatorComponent || SpinnerComponent;
    const componentFactory = this.componentFactoryResolver.resolveComponentFactory(component as any);
    const viewContainerRef = this.host.viewContainerRef;
    viewContainerRef.clear();
    const componentRef: ComponentRef<any> = viewContainerRef.createComponent(componentFactory);
    componentRef.instance.color = this.config.color || INDICATOR_COLOR;
    componentRef.instance.size = this.config.size || DEFAULT_SIZE;
  }
}
```

Nous devons charger le composant dans le hook de cycle de vie OnInit. Le hook OnInit s'exécute après le premier ngOnChanges(), et il n'est appelé qu'une seule fois. C'est l'endroit idéal pour charger un composant dynamiquement dans le DOM. Nous devons également vider la référence viewContainer lors de la destruction du composant.

```typescript
  ngOnInit(): void {
    this.loadComponent();
  }

  ngOnDestroy(): void {
    this.host.viewContainerRef.clear();
  }
```

Examinons un peu plus en détail notre méthode 'loadComponent'. Nous voulons fournir nos composants personnalisés en utilisant notre logique de configuration. Lorsqu'un composant personnalisé n'est pas fourni dans la configuration, notre indicateur sera le composant spinner par défaut.

```typescript
  private loadComponent() {
    const component = this.config.indicatorComponent || SpinnerComponent;
    const componentFactory = this.componentFactoryResolver.resolveComponentFactory(component as any);
    const viewContainerRef = this.host.viewContainerRef;
    viewContainerRef.clear();
    const componentRef: ComponentRef<any> = viewContainerRef.createComponent(componentFactory);
    componentRef.instance.color = this.config.color || INDICATOR_COLOR;
    componentRef.instance.size = this.config.size || DEFAULT_SIZE;
  }
```

Ensuite, nous utilisons le componentFactoryResolver pour obtenir la factory du composant. Pour être sûr, nous vidons d'abord notre ViewContainerRef. Ensuite, nous créons le composant en utilisant la factory résolue, et nous définissons nos valeurs de configuration sur l'instance créée.

Notre utilisateur final veut uniquement un petit texte au lieu d'un spinner fantaisiste. Un composant plutôt simple ressemblerait à ce qui suit :

```typescript
import {Component} from '@angular/core';

@Component({
  selector: 'app-loading-message',
  template: `<h1>Chargement...</h1>`,
  styles: [``]
})
export class LoadingMessageComponent {
}
```

Nous le fournissons dans le module principal de notre application, où nous configurons notre bibliothèque. L'ajout du composant dans le tableau 'entryComponents' garantit que sa factory peut être résolue pendant le chargement.

Désormais, nous pouvons remplacer le composant indicateur dans n'importe quel projet Angular, sans avoir à réimplémenter la majeure partie de la logique encore et encore.

```typescript
@NgModule({
  declarations: [AppComponent, LoadingMessageComponent],
  imports: [
    CommonModule,
    AppRoutingModule,
    LoadingIndicatorModule.forRoot(),
  ],
  providers: [
    {
      provide: LOADING_INDICATOR_CONFIG,
      useValue: {
        indicatorComponent: LoadingMessageComponent
      }
    }
  ],
  entryComponents: [LoadingMessageComponent]
})
export class AppModule {
}
```

_Si vous souhaitez en savoir plus sur les composants dynamiques, je vous recommande de lire : [Voici ce que vous devez savoir sur les composants dynamiques dans Angular](https://blog.angularindepth.com/here-is-what-you-need-to-know-about-dynamic-components-in-angular-ac1e96167f9e) par [**Max Koretskyi**](https://twitter.com/maxkoretskyi)_

Je vous remercie beaucoup d'avoir lu cet article de blog. Si vous souhaitez essayer la bibliothèque mentionnée ci-dessus, vous pouvez trouver le package et les instructions pour l'installer [ici](https://www.npmjs.com/package/@btapai/ng-loading-indicator).

_Vous pouvez également me suivre sur [Twitter](https://twitter.com/TapaiBalazs) ou [GitHub](https://github.com/TapaiBalazs)._