---
title: Comment créer un indicateur de chargement réutilisable pour les projets Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-14T07:53:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-reusable-loading-indicator-for-angular-projects-d0a11f4631e0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hEbJvltnslRrdEzjWQ7Img.jpeg
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
seo_title: Comment créer un indicateur de chargement réutilisable pour les projets
  Angular
seo_desc: 'By Balázs Tápai

  Reusability. A word that has crossed my mind several times recently, while working
  on an Angular project. I have decided to create my own Angular reusables and blog
  about the experience.


  _Photo by [Unsplash](https://unsplash.com/phot...'
---

Par Balázs Tápai

**Réutilisabilité**. Un mot qui m'a traversé l'esprit plusieurs fois récemment, tout en travaillant sur un projet Angular. J'ai décidé de créer mes propres composants réutilisables Angular et de bloguer sur cette expérience.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hEbJvltnslRrdEzjWQ7Img.jpeg)
_Photo par [Unsplash](https://unsplash.com/photos/XJXWbfSo2f0?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Luca Bravo</a> sur <a href="https://unsplash.com/search/photos/front-end?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Alors, qu'est-ce qu'un indicateur de chargement exactement ? Habituellement, il s'agit d'un spinner avec un calque superposé qui empêche les interactions de l'utilisateur. L'interface utilisateur n'est pas cliquable et le focus est piégé. Ainsi, l'utilisateur ne peut pas modifier les données ou l'état de l'application accidentellement en interagissant avec les éléments derrière le calque.

Une fois le chargement terminé, le calque avec le spinner est retiré du DOM et l'élément précédemment focalisé est à nouveau focalisé.

J'ai commencé par la logique qui déclencherait le spinner. Pour cela, j'ai utilisé un simple BehaviorSubject et deux fonctions décorateurs :

```js
import {BehaviorSubject} from 'rxjs';
import {distinctUntilChanged} from 'rxjs/operators';

const indicatorSubject = new BehaviorSubject<boolean>(false);

export const isLoading$ = indicatorSubject.asObservable().pipe(distinctUntilChanged());

export function startLoadingIndicator(target: any, propertyKey: string | symbol, propertyDescriptor: PropertyDescriptor): any {
  const original = propertyDescriptor.value;
  propertyDescriptor.value = (...args) => {
    indicatorSubject.next(true);
    const result = original.call(target, ...args);
    return result;
  };
  return propertyDescriptor;
}

export function stopLoadingIndicator(target: any, propertyKey: string, propertyDescriptor: PropertyDescriptor): any {
  const original = propertyDescriptor.value;
  propertyDescriptor.value = (...args) => {
    indicatorSubject.next(false);
    const result = original.call(target, ...args);
    return result;
  };
  return propertyDescriptor;
}

```

De cette manière, nous n'avons pas besoin d'un service injectable pour déclencher ou arrêter le spinner. Les deux méthodes décorateurs simples appellent simplement .next() sur notre BehaviorSubject. La variable isLoading$ est exportée en tant qu'observable.

Utilisons-la dans notre composant d'indicateur de chargement.

```js
get isLoading$(): Observable<boolean> {
  return isLoading$;
}
```

Maintenant, dans votre template, vous pouvez utiliser votre getter isLoading$ avec le pipe async pour afficher/masquer le calque entier.

```html
<div class="btp-overlay" *ngIf="isLoading$ | async">
  <div class="btp-loading-indicator__container" [style.width]="indicatorSize" [style.height]="indicatorSize">
    <btp-spinner></btp-spinner>
  </div>
</div>
```

Comme vous pouvez le voir, j'ai extrait le spinner dans son propre composant, et j'ai fait plusieurs autres choses. J'ai ajouté une logique pour piéger le focus et la possibilité de configurer la taille et la couleur du spinner en utilisant un InjectionToken.

```js
import {LoadingIndicatorConfig} from './interfaces/loading-indicator.interfaces';
import {InjectionToken} from '@angular/core';

export const DEFAULT_CONFIG: LoadingIndicatorConfig = {
  size: 160,
  color: '#7B1FA2'
};

export const LOADING_INDICATOR_CONFIG: InjectionToken<string> = new InjectionToken('btp-li-conf');


```

Fournir des objets de configuration en utilisant InjectionToken est une bonne manière de fournir des propriétés configurables dans le constructeur.

```js
  constructor(@Inject(LOADING_INDICATOR_CONFIG)
              private config: LoadingIndicatorConfig) {
  }
```

Maintenant, nous devons regrouper tout cela dans un NgModule :

```js
import {ModuleWithProviders, NgModule} from '@angular/core';
import {LoadingIndicatorComponent} from './loading-indicator/loading-indicator.component';
import {CommonModule} from '@angular/common';
import {SpinnerComponent} from './spinner/spinner.component';
import {DEFAULT_CONFIG, LOADING_INDICATOR_CONFIG} from './loading-indicator.config';

@NgModule({
  declarations: [LoadingIndicatorComponent, SpinnerComponent],
  imports: [
    CommonModule
  ],
  exports: [LoadingIndicatorComponent]
})
export class LoadingIndicatorModule {
  static forRoot(): ModuleWithProviders {
    return {
      ngModule: LoadingIndicatorModule,
      providers: [{provide: LOADING_INDICATOR_CONFIG, useValue: DEFAULT_CONFIG}]
    };
  }
}
```

Après avoir construit la bibliothèque et l'avoir installée dans une application Angular, déclencher le spinner devient extrêmement facile en utilisant les deux méthodes décorateurs.

Tout d'abord, nous devons ajouter le composant au bon endroit dans le DOM. Je le place généralement dans le composant d'entrée de l'application, en bas du template.

```html
<h1>Indicateur de chargement</h1>


<button data-test-id="cy-trigger-indicator" (click)="triggerLoadingIndicator()">DÉMARRER LE CHARGEMENT</button>

<btp-loading-indicator></btp-loading-indicator>

```

Comme vous pouvez le voir, la méthode triggerLoadingIndicator est appelée lorsque le bouton est cliqué. Cette méthode est une méthode décorée :

```js
  @startLoadingIndicator
  triggerLoadingIndicator() {
    setTimeout(this.triggerLoadingIndicatorStop.bind(this), 500);
  }

  @stopLoadingIndicator
  triggerLoadingIndicatorStop() {
    console.log('arrêté');
  }
```

Et c'est tout. Bien sûr, dans une application réelle, on pourrait l'utiliser pour décorer les requêtes et leurs gestionnaires de réponse respectifs. Un petit conseil : décorez également vos gestionnaires d'erreurs. :)

Merci beaucoup d'avoir lu cet article de blog. Si vous souhaitez essayer la bibliothèque mentionnée ci-dessus, vous pouvez trouver le package et les instructions pour l'installer [ici](https://www.npmjs.com/package/@btapai/ng-loading-indicator).

_Vous pouvez également me suivre sur [Twitter](https://twitter.com/TapaiBalazs) ou [GitHub](https://github.com/TapaiBalazs)._