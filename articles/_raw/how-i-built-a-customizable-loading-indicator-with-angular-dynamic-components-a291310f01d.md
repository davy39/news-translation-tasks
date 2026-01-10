---
title: How I built a customizable loading-indicator with Angular dynamic components
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
seo_title: null
seo_desc: 'By Balázs Tápai

  Recently, I wrote a blog post about creating a reusable loading-indicator component
  for Angular projects. The next step is making the indicator part customizable. But
  how exactly do you insert your component into the overlay? That is ...'
---

By Balázs Tápai

Recently, I wrote a [blog post](https://medium.com/@balazs.tapai1990/how-to-create-reusable-loading-indicator-for-angular-projects-d0a11f4631e0?source=friends_link&sk=9022f72306ac9adf2aea163dfa15fb05) about creating a reusable loading-indicator component for Angular projects. The next step is making the indicator part customizable. But how exactly do you insert your component into the overlay? That is where dynamic components can help us.

**_Note:_** _Since my previous blog post, I have refactored some parts of the library. Feel free to check out the [git repository](https://github.com/TapaiBalazs/angular-reusables)._

The use-case is that we have a really easy to use loading-indicator. By default, it has a spinner, and it can be triggered using the library’s decorator methods. However, our end user wants only “Loading…” displayed on the overlay. We can copy the logic and then replace the spinner with the text itself, but that would be rather redundant.

In order to be able to use dynamic components, first, we need a simple decorator implemented. This decorator makes it possible to inject our own component into the template.

```typescript
import { Directive, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[btpIndicatorHost]',
})
export class IndicatorHostDirective {
  constructor(public viewContainerRef: ViewContainerRef) { }
}
```

We have to add this directive to our library’s NgModule. Then replace the spinner component inside the loading-indicator template with the following:

```html
<btp-overlay>
  <div class="btp-loading-indicator__container" [style.width]="indicatorSize" [style.height]="indicatorSize">
    <ng-template btpIndicatorHost></ng-template>
  </div>
</btp-overlay>
```

Now that we have this template, we need to do 3 things in the loading-indicator component.

1. Inject the ComponentFactoryResolver into the component.
2. Use the @ViewChild decorator to get our indicator-host.
3. Load the provided component.

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

We need to load the component in the OnInit lifecycle hook. The OnInit hook runs after the first ngOnChanges(), and it is called only once. It is the ideal place to load a component dynamically into the DOM. We also need to clear the viewContainer reference during component destroy.

```typescript
  ngOnInit(): void {
    this.loadComponent();
  }

  ngOnDestroy(): void {
    this.host.viewContainerRef.clear();
  }
```

Let’s examine our ‘loadComponent’ method a little bit further. We want to provide our custom components using our configuration logic. When a custom component is not provided in the config, our indicator will be the default spinner component.

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

Then we use the componentFactoryResolver, to get the component’s factory. To be on the safe side, we clear our ViewContainerRef first. Then we create the component using the resolved factory, and we set our config values on the created instance.

Our end-user wants only a small text instead of a fancy spinner. A rather simple component would look like the following:

```typescript
import {Component} from '@angular/core';

@Component({
  selector: 'app-loading-message',
  template: `<h1>Loading...</h1>`,
  styles: [``]
})
export class LoadingMessageComponent {
}
```

We provide it in our app’s main module, where we set up and configure our library. Adding the component into the ‘entryComponents’ array makes it sure that its factory can be resolved during loading.

From now on, we can replace the indicator component in any of our Angular projects, without the hustle of reimplementing most of the logic over and over again.

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

_If you would like to learn more about Dynamic components, I recommend you to read: [Here is what you need to know about dynamic components in Angular](https://blog.angularindepth.com/here-is-what-you-need-to-know-about-dynamic-components-in-angular-ac1e96167f9e) by [**Max Koretskyi**](https://twitter.com/maxkoretskyi)_

Thank you very much for reading this blog post. If you would like to try the above-mentioned lib out, you can find the package and instructions to install it [here](https://www.npmjs.com/package/@btapai/ng-loading-indicator).

_You can also follow me on [Twitter](https://twitter.com/TapaiBalazs) or [GitHub](https://github.com/TapaiBalazs)._

