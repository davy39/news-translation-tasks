---
title: How to create a reusable loading-indicator for Angular projects
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
seo_title: null
seo_desc: 'By Balázs Tápai

  Reusability. A word that has crossed my mind several times recently, while working
  on an Angular project. I have decided to create my own Angular reusables and blog
  about the experience.


  _Photo by [Unsplash](https://unsplash.com/phot...'
---

By Balázs Tápai

**Reusability**. A word that has crossed my mind several times recently, while working on an Angular project. I have decided to create my own Angular reusables and blog about the experience.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hEbJvltnslRrdEzjWQ7Img.jpeg)
_Photo by [Unsplash](https://unsplash.com/photos/XJXWbfSo2f0?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Luca Bravo</a> on <a href="https://unsplash.com/search/photos/front-end?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

So, what exactly is a loading-indicator? Usually, it is a spinner of some sort with an overlay, which prevents user interactions. The UI is not clickable and focus is trapped. Therefore, the user cannot mutate the data or the application state accidentally by interacting with inputs behind the overlay.

After the loading stops, the overlay with the spinner is removed from the DOM and the previously focused element is focused again.

I started with the logic that would trigger the spinner. For that I used a simple BehaviorSubject and two decorator functions:

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

This way, we don’t need an injectable service for triggering or stopping the spinner. The two simple decorator methods just call .next() on our BehaviorSubject. The isLoading$ variable is exported as an observable.

Let’s use it in our loading-indicator component.

```js
get isLoading$(): Observable<boolean> {
  return isLoading$;
}
```

Now inside your template, you can use your isLoading$ getter with the async pipe to show/hide the whole overlay.

```html
<div class="btp-overlay" *ngIf="isLoading$ | async">
  <div class="btp-loading-indicator__container" [style.width]="indicatorSize" [style.height]="indicatorSize">
    <btp-spinner></btp-spinner>
  </div>
</div>
```

As you can see I extracted the spinner into its own component, and I have done several other things. I added some logic for focus trapping and the ability to configure the size and color of the spinner using an InjectionToken.

```js
import {LoadingIndicatorConfig} from './interfaces/loading-indicator.interfaces';
import {InjectionToken} from '@angular/core';

export const DEFAULT_CONFIG: LoadingIndicatorConfig = {
  size: 160,
  color: '#7B1FA2'
};

export const LOADING_INDICATOR_CONFIG: InjectionToken<string> = new InjectionToken('btp-li-conf');


```

Providing configuration objects using InjectionToken is a good way to provide configurable properties in the constructor.

```js
  constructor(@Inject(LOADING_INDICATOR_CONFIG)
              private config: LoadingIndicatorConfig) {
  }
```

Now we have to bundle everything up into a NgModule:

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

After building the library, and installing it into an Angular application, triggering the spinner becomes extremely easy using the two decorator methods.

First, we need to add the component to the proper place in the DOM. I usually put it to the app entry component, to the bottom of the template.

```html
<h1>Loading indicator</h1>


<button data-test-id="cy-trigger-indicator" (click)="triggerLoadingIndicator()">START LOADING</button>

<btp-loading-indicator></btp-loading-indicator>

```

As you can see, the triggerLoadingIndicator method is called when the button is clicked. That method is a decorated method:

```js
  @startLoadingIndicator
  triggerLoadingIndicator() {
    setTimeout(this.triggerLoadingIndicatorStop.bind(this), 500);
  }

  @stopLoadingIndicator
  triggerLoadingIndicatorStop() {
    console.log('stopped');
  }
```

And that is it. Of course in a real application, one could use it to decorate requests and their respective response handlers. A quick tip: decorate your error handlers as well. :)

Thank you very much for reading this blog post. If you would like to try the above-mentioned lib out, you can find the package and instructions to install it [here](https://www.npmjs.com/package/@btapai/ng-loading-indicator).

_You can also follow me on [Twitter](https://twitter.com/TapaiBalazs) or [GitHub](https://github.com/TapaiBalazs)._

