---
title: What could go wrong? How to handle errors in Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-01T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/global-error-handling-in-angular-with-the-help-of-the-cdk
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Screenshot-2019-07-01-at-11.01.20.png
tags:
- name: Angular
  slug: angular
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: null
seo_desc: 'By Balázs Tápai

  Approximately a year ago, I have implemented the first e2e tests on a project. It
  was a rather big application using JAVA SpringBoot on the back-end and Angular on
  the front-end. We used Protractor as a testing tool, which uses Seleni...'
---

By Balázs Tápai

Approximately a year ago, I have implemented the first e2e tests on a project. It was a rather big application using JAVA SpringBoot on the back-end and Angular on the front-end. We used Protractor as a testing tool, which uses Selenium. In the front-end code there was a service, which had an error handler method. When that method was called, a modal dialog popped up and the user could see the details of the errors and the stack-trace.

The problem was that while it has tracked every error that happened on the back-end, the front-end failed silently. _TypeErrors_, _ReferenceErrors_ and other uncaught exceptions were logged only to the console. When something went wrong during e2e test runs the screenshot, which was taken when the test step has failed, has shown absolutely nothing. Have fun debugging that!

Luckily Angular has a built-in way of handling errors and it is extremely easy to use. We just have to create our own service, which implements Angular's _ErrorHandler_ interface:

```typescript
import { ErrorHandler, Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class ErrorHandlerService implements ErrorHandler{
    constructor() {}

    handleError(error: any) {
        // Implement your own way of handling errors
    }
}
```

While we could easily provide our service in our _AppModule_, it might be a good idea to provide this service in a separate module. This way we could create our own library and use it in our future projects as well:

```typescript
// ERROR HANDLER MODULE
import {ErrorHandler, ModuleWithProviders, NgModule} from '@angular/core';
import {ErrorHandlerComponent} from './components/error-handler.component';
import {FullscreenOverlayContainer, OverlayContainer, OverlayModule} from '@angular/cdk/overlay';
import {ErrorHandlerService} from './error-handler.service';
import {A11yModule} from '@angular/cdk/a11y';

@NgModule({
  declarations: [ErrorHandlerComponent],
  imports: [CommonModule, OverlayModule, A11yModule],
  entryComponents: [ErrorHandlerComponent]
})
export class ErrorHandlerModule {
  public static forRoot(): ModuleWithProviders {
    return {
      ngModule: ErrorHandlerModule,
      providers: [
        {provide: ErrorHandler, useClass: ErrorHandlerService},
        {provide: OverlayContainer, useClass: FullscreenOverlayContainer},
      ]
    };
  }
}
```

We used the _Angular CLI_ for generating the _ErrorHandlerModule_, so we already have a component generated, which can be our modal dialog's content. In order for us to be able to put it inside an Angular CDK overlay, it needs to be an entryComponent. That is why we have put it into the _ErrorHandlerModule_'s entryComponents array.

We also added some imports. _OverlayModule_ and _A11yModule_ comes from the CDK module. They are needed for creating our overlay and to trap focus when our error dialog is opened. As you can see, we provide _OverlayContainer_ using the _FullscreenOverlayContainer_ class because if an error occurs, we want to restrict our users' interactions to our error modal. If we don't have a fullscreen backdrop, the users might be able to interact with the application and cause further errors. Let's add our newly created module to our _AppModule_:

```typescript
// APP MODULE
import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {MainComponent} from './main/main.component';
import {ErrorHandlerModule} from '@btapai/ng-error-handler';
import {HttpClientModule} from '@angular/common/http';

@NgModule({
  declarations: [ AppComponent, MainComponent ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ErrorHandlerModule.forRoot(),
    AppRoutingModule,
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
```

Now that we have our `ErrorHandlerService` in place, we can start implementing the logic. We are going to create a modal dialog, which displays the error in a clean, readable way. This dialog will have an overlay/backdrop and it will be dynamically placed into the DOM with the help of the Angular CDK. Let's install it:

```bash
npm install @angular/cdk --save
```

According to the [documentation](https://material.angular.io/cdk/overlay/overview), the _Overlay_ component needs some pre-built css files. Now if we would use Angular Material in our project it wouldn't be necessary, but that is not always the case. Let's import the overlay css in our _styles.css_ file. Note, that if you already use Angular Material in your app, you don't need to import this css.

```css
@import '~@angular/cdk/overlay-prebuilt.css';
```

Let's use our _handleError_ method to create our modal dialog. It is important to know, that the _ErrorHandler_ service is part of the application initialisation phase of Angular. In order to avoid a rather nasty [cyclic dependency error](https://stackoverflow.com/a/39767492), we use the injector as its only constructor parameter. We use Angular's dependency injection system when the actual method is called. Let's import the overlay from the CDK and attach our _ErrorHandlerComponent_ into the DOM:

 ```typescript
// ... imports

@Injectable({
    providedIn: 'root'
})
export class ErrorHandlerService implements ErrorHandler {
    constructor(private injector: Injector) {}

    handleError(error: any) {
        const overlay: Overlay = this.injector.get(Overlay);
        const overlayRef: OverlayRef = overlay.create();
        const ErrorHandlerPortal: ComponentPortal<ErrorHandlerComponent> = new ComponentPortal(ErrorHandlerComponent);
        const compRef: ComponentRef<ErrorHandlerComponent> = overlayRef.attach(ErrorHandlerPortal);
    }
}
```

Let's turn our attention towards our error handler modal. A pretty simple working solution would be displaying the error message and the stacktrace. Let's also add a 'dismiss' button to the bottom.

```typescript
// imports
export const ERROR_INJECTOR_TOKEN: InjectionToken<any> = new InjectionToken('ErrorInjectorToken');

@Component({
  selector: 'btp-error-handler',
  // TODO: template will be implemented later
  template: `${error.message}<br><button (click)="dismiss()">DISMISS</button>`
  styleUrls: ['./error-handler.component.css'],
})
export class ErrorHandlerComponent {
  private isVisible = new Subject();
  dismiss$: Observable<{}> = this.isVisible.asObservable();

  constructor(@Inject(ERROR_INJECTOR_TOKEN) public error) {
  }

  dismiss() {
    this.isVisible.next();
    this.isVisible.complete();
  }
}
```

As you can see, the component itself is pretty simple. We are going to use two rather important directives in the template, to make the dialog accessible. The first one is the _cdkTrapFocus_ which will trap the focus when the dialog is rendered. This means that the user cannot focus elements behind our modal dialog. The second directive is the _cdkTrapFocusAutoCapture_ which will automatically focus the first focusable element inside our focus trap. Also, it will automatically restore the focus to the previously focused element, when our dialog is closed.

In order to be able to display the error's properties, we need to inject it using the constructor. For that, we need our own _injectionToken_. We also created a rather simple logic for emitting a dismiss event using a subject and the _dismiss$_ property. Let's connect this with our _handleError_ method in our service and do some refactoring.

```typescript
// imports
export const DEFAULT_OVERLAY_CONFIG: OverlayConfig = {
  hasBackdrop: true,
};

@Injectable({
  providedIn: 'root'
})
export class ErrorHandlerService implements ErrorHandler {

  private overlay: Overlay;

  constructor(private injector: Injector) {
    this.overlay = this.injector.get(Overlay);
  }

  handleError(error: any): void {
    const overlayRef = this.overlay.create(DEFAULT_OVERLAY_CONFIG);
    this.attachPortal(overlayRef, error).subscribe(() => {
      overlayRef.dispose();
    });
  }

  private attachPortal(overlayRef: OverlayRef, error: any): Observable<{}> {
    const ErrorHandlerPortal: ComponentPortal<ErrorHandlerComponent> = new ComponentPortal(
      ErrorHandlerComponent,
      null,
      this.createInjector(error)
    );
    const compRef: ComponentRef<ErrorHandlerComponent> = overlayRef.attach(ErrorHandlerPortal);
    return compRef.instance.dismiss$;
  }

  private createInjector(error: any): PortalInjector {
    const injectorTokens = new WeakMap<any, any>([
      [ERROR_INJECTOR_TOKEN, error]
    ]);

    return new PortalInjector(this.injector, injectorTokens);
  }
}
```

Let's focus on providing the error as an injected parameter first. As you can see, the _ComponentPortal_ class expects one must-have parameter, which is the component itself. The second parameter is a _ViewContainerRef_ which would have an effect of the component's logical place of the component tree. The third parameter is our _createInejctor_ method. As you can see it returns a new _PortalInjector_ instance. Let's take a quick look at its underlying implementation:

```typescript
export class PortalInjector implements Injector {
 constructor(
   private _parentInjector: Injector,
   private _customTokens: WeakMap<any, any>) { }

 get(token: any, notFoundValue?: any): any {
   const value = this._customTokens.get(token);

   if (typeof value !== 'undefined') {
     return value;
   }

   return this._parentInjector.get<any>(token, notFoundValue);
 }
}
```

As you can see, it expects an _Injector_ as a first parameter and a WeakMap for custom tokens. We did exactly that using our _ERROR_INJECTOR_TOKEN_ which is associated with our error itself. The created _PortalInjector_ is used for the proper instantiation of our _ErrorHandlerComponent_, it will make sure that the error itself will be present in the component.

At last, our _attachPortal_ method returns the recently instantiated component's _dismiss$_ property. We subscribe to it, and when it changes we call the _.dispose()_ on our _overlayRef_. And our error modal dialog is dismissed. Note, that we also call complete on our subject inside the component, therefore, we don't need to unsubscribe from it.

---

Now, this is excellent for errors that are thrown when there's an issue in the clinet side code. But we are creating web applications and we use API endpoints. So what happens when a REST endpint gives back an error?

We can handle every error in its own service, but do we really want to? If everything is alright errors won't be thrown. If there are specific requirements, for example to handle [418 status code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418) with a flying unicorn you could implement its handler in its service. But when we face rather common errors, like 404 or 503 we might want to display that in this same error dialog.

Let's just quickly gather what happens when an _HttpErrorResponse_ is thrown. It is going to happen async, so probably we are going to face some change detection issues. This error type has different properties than a simple error, therefore, we might need a sanitiser method. Now let's get into it by creating a rather simple interface for the _SanitisedError_:

```typescript
export interface SanitizedError {
  message: string;
  details: string[];
}
```

Let's create a template for our _ErrorHandlerComponent_:

```typescript
// Imports

@Component({
  selector: 'btp-error-handler',
  template: `
    <section cdkTrapFocus [cdkTrapFocusAutoCapture]="true" class="btp-error-handler__container">
      <h2>Error</h2>
      <p>{{error.message}}</p>
      <div class="btp-error-handler__scrollable">
        <ng-container *ngFor="let detail of error.details">
          <div>{{detail}}</div>
        </ng-container>
      </div>
      <button class="btp-error-handler__dismiss button red" (click)="dismiss()">DISMISS</button>
    </section>`,
  styleUrls: ['./error-handler.component.css'],
})
export class ErrorHandlerComponent implements OnInit {
 // ...
}
```

We wrapped the whole modal into a _<section>_ and we added the _cdkTrapFocus_ directive to it. This directive will prevent the user from navigating in the DOM behind our overlay/modal. The _[cdkTrapFocusAutoCapture]="true"_ makes sure that the dismiss button is focused immediately. When the modal is closed the previously focused element will get back the focus. We simply display the error message and the details using _*ngFor_. Let's jump back into our _ErrorHandlerService_:

```typescript
// Imports

@Injectable({
  providedIn: 'root'
})
export class ErrorHandlerService implements ErrorHandler {
  // Constructor

  handleError(error: any): void {
    const sanitised = this.sanitiseError(error);
    const ngZone = this.injector.get(NgZone);
    const overlayRef = this.overlay.create(DEFAULT_OVERLAY_CONFIG);

    ngZone.run(() => {
      this.attachPortal(overlayRef, sanitised).subscribe(() => {
        overlayRef.dispose();
      });
    });
  }
  
  // ...

  private sanitiseError(error: Error | HttpErrorResponse): SanitizedError {
    const sanitisedError: SanitizedError = {
      message: error.message,
      details: []
    };
    if (error instanceof Error) {
      sanitisedError.details.push(error.stack);
    } else if (error instanceof HttpErrorResponse) {
      sanitisedError.details = Object.keys(error)
        .map((key: string) => `${key}: ${error[key]}`);
    } else {
      sanitisedError.details.push(JSON.stringify(error));
    }
    return sanitisedError;
  }
  // ...
}
```

With a rather simple _sanitiseError_ method we create an object which is based on our previously defined interface. We check for error types and populate the data accordingly. The more interesting part is using the injector to get _ngZone_. When an error happens asynchronously, it usually happens outside change detection. We wrap our _attachPortal_ with _ngZone.run(/* ... */)_, so when an _HttpErrorResponse_ is caught, it is rendered properly in our modal.

While the current state works nicely, it still lacks customisation. We use the Overlay from the CDK module, so exposing an injection token for custom configurations would be nice. Another important shortcoming of this module is that when this module is used, another module can't be used for error handling. For example, integrating Sentry would require you to implement a similar, but lightweight ErrorHandler module. In order to be able to use both, we should implement the possibility of using hooks inside our error handler. First, let's create our _InjectionToken_ and our default configuration:

```typescript
import {InjectionToken} from '@angular/core';
import {DEFAULT_OVERLAY_CONFIG} from './constants/error-handler.constants';
import {ErrorHandlerConfig} from './interfaces/error-handler.interfaces';

export const DEFAULT_ERROR_HANDLER_CONFIG: ErrorHandlerConfig = {
  overlayConfig: DEFAULT_OVERLAY_CONFIG,
  errorHandlerHooks: []
};

export const ERROR_HANDLER_CONFIG: InjectionToken<ErrorHandlerConfig> = new InjectionToken('btp-eh-conf');
```

Then provide it with our module, using our existing _forRoot_ method:

```typescript
@NgModule({
  declarations: [ErrorHandlerComponent],
  imports: [CommonModule, OverlayModule, A11yModule],
  entryComponents: [ErrorHandlerComponent]
})
export class ErrorHandlerModule {

  public static forRoot(): ModuleWithProviders {
    return {
      ngModule: ErrorHandlerModule,
      providers: [
        {provide: ErrorHandler, useClass: ErrorHandlerService},
        {provide: OverlayContainer, useClass: FullscreenOverlayContainer},
        {provide: ERROR_HANDLER_CONFIG, useValue: DEFAULT_ERROR_HANDLER_CONFIG}
      ]
    };
  }
}
```

Then integrate this config handling into our _ErrorHandlerService_ as well:

```typescript
// Imports
@Injectable({
  providedIn: 'root'
})
export class ErrorHandlerService implements ErrorHandler {
  // ...

  handleError(error: any): void {
    const sanitised = this.sanitiseError(error);
    const {overlayConfig, errorHandlerHooks} = this.injector.get(ERROR_HANDLER_CONFIG);
    const ngZone = this.injector.get(NgZone);

    this.runHooks(errorHandlerHooks, error);
    const overlayRef = this.createOverlayReference(overlayConfig);
    ngZone.run(() => {
      this.attachPortal(overlayRef, sanitised).subscribe(() => {
        overlayRef.dispose();
      });
    });
  }
  // ...
  private runHooks(errorHandlerHooks: Array<(error: any) => void> = [], error): void {
    errorHandlerHooks.forEach((hook) => hook(error));
  }

  private createOverlayReference(overlayConfig: OverlayConfig): OverlayRef {
    const overlaySettings: OverlayConfig = {...DEFAULT_OVERLAY_CONFIG, ...overlayConfig};
    return this.overlay.create(overlaySettings);
  }
  // ...
}
```

And we are almost ready. Let's integrate a third-party error handler hook into our application:

```typescript
// Imports
const CustomErrorHandlerConfig: ErrorHandlerConfig = {
  errorHandlerHooks: [
    ThirdPartyErrorLogger.logErrorMessage,
    LoadingIndicatorControl.stopLoadingIndicator,
  ]
};

@NgModule({
  declarations: [
    AppComponent,
    MainComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ErrorHandlerModule.forRoot(),
    AppRoutingModule,
  ],
  providers: [
    {provide: ERROR_HANDLER_CONFIG, useValue: CustomErrorHandlerConfig}
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}
```

As you can see, handling errors is an extremely important part of software development, but it can also be fun.

Thank you very much for reading this blog post. If you prefer reading code, please check out my [ng-reusables git repository](https://github.com/TapaiBalazs/angular-reusables). You can also try out the implementation using this [npm package](https://www.npmjs.com/package/@btapai/ng-error-handler).

You can also follow me on [Twitter](https://twitter.com/TapaiBalazs) or [GitHub](https://github.com/TapaiBalazs).

