---
title: Que pourrait-il mal se passer ? Comment gérer les erreurs dans Angular
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
seo_title: Que pourrait-il mal se passer ? Comment gérer les erreurs dans Angular
seo_desc: 'By Balázs Tápai

  Approximately a year ago, I have implemented the first e2e tests on a project. It
  was a rather big application using JAVA SpringBoot on the back-end and Angular on
  the front-end. We used Protractor as a testing tool, which uses Seleni...'
---

Par Balázs Tápai

Il y a environ un an, j'ai implémenté les premiers tests e2e sur un projet. Il s'agissait d'une application plutôt grande utilisant JAVA SpringBoot en back-end et Angular en front-end. Nous avons utilisé Protractor comme outil de test, qui utilise Selenium. Dans le code front-end, il y avait un service qui avait une méthode de gestion des erreurs. Lorsque cette méthode était appelée, une boîte de dialogue modale s'affichait et l'utilisateur pouvait voir les détails des erreurs et la stack-trace.

Le problème était que, bien qu'il ait suivi chaque erreur survenue en back-end, le front-end échouait silencieusement. Les _TypeErrors_, _ReferenceErrors_ et autres exceptions non capturées étaient uniquement enregistrées dans la console. Lorsque quelque chose n'allait pas pendant les exécutions des tests e2e, la capture d'écran, qui était prise lorsque l'étape du test avait échoué, n'a montré absolument rien. Amusez-vous à déboguer cela !

Heureusement, Angular dispose d'un moyen intégré de gérer les erreurs et il est extrêmement facile à utiliser. Nous devons simplement créer notre propre service, qui implémente l'interface _ErrorHandler_ d'Angular :

```typescript
import { ErrorHandler, Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class ErrorHandlerService implements ErrorHandler{
    constructor() {}

    handleError(error: any) {
        // Implémentez votre propre façon de gérer les erreurs
    }
}
```

Bien que nous puissions facilement fournir notre service dans notre _AppModule_, il pourrait être judicieux de fournir ce service dans un module séparé. De cette façon, nous pourrions créer notre propre bibliothèque et l'utiliser dans nos futurs projets également :

```typescript
// MODULE DE GESTION DES ERREURS
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

Nous avons utilisé l'_Angular CLI_ pour générer le _ErrorHandlerModule_, donc nous avons déjà un composant généré, qui peut être le contenu de notre boîte de dialogue modale. Pour pouvoir le placer à l'intérieur d'un overlay Angular CDK, il doit être un entryComponent. C'est pourquoi nous l'avons mis dans le tableau entryComponents du _ErrorHandlerModule_.

Nous avons également ajouté quelques imports. _OverlayModule_ et _A11yModule_ proviennent du module CDK. Ils sont nécessaires pour créer notre overlay et pour piéger le focus lorsque notre boîte de dialogue d'erreur est ouverte. Comme vous pouvez le voir, nous fournissons _OverlayContainer_ en utilisant la classe _FullscreenOverlayContainer_ car si une erreur se produit, nous voulons restreindre les interactions de nos utilisateurs à notre modale d'erreur. Si nous n'avons pas un arrière-plan plein écran, les utilisateurs pourraient être en mesure d'interagir avec l'application et de causer d'autres erreurs. Ajoutons notre module nouvellement créé à notre _AppModule_ :

```typescript
// MODULE D'APPLICATION
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

Maintenant que nous avons notre `ErrorHandlerService` en place, nous pouvons commencer à implémenter la logique. Nous allons créer une boîte de dialogue modale, qui affiche l'erreur de manière claire et lisible. Cette boîte de dialogue aura un overlay/arrière-plan et sera placée dynamiquement dans le DOM avec l'aide du CDK Angular. Installons-le :

```bash
npm install @angular/cdk --save
```

Selon la [documentation](https://material.angular.io/cdk/overlay/overview), le composant _Overlay_ nécessite certains fichiers CSS pré-construits. Maintenant, si nous utilisions Angular Material dans notre projet, cela ne serait pas nécessaire, mais ce n'est pas toujours le cas. Importons le CSS de l'overlay dans notre fichier _styles.css_. Notez que si vous utilisez déjà Angular Material dans votre application, vous n'avez pas besoin d'importer ce CSS.

```css
@import '~@angular/cdk/overlay-prebuilt.css';
```

Utilisons notre méthode _handleError_ pour créer notre boîte de dialogue modale. Il est important de savoir que le service _ErrorHandler_ fait partie de la phase d'initialisation de l'application Angular. Afin d'éviter une erreur de dépendance cyclique plutôt désagréable, nous utilisons l'injecteur comme seul paramètre de son constructeur. Nous utilisons le système d'injection de dépendances d'Angular lorsque la méthode réelle est appelée. Importons l'overlay du CDK et attachons notre _ErrorHandlerComponent_ au DOM :

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

Attirons notre attention vers notre modale de gestion des erreurs. Une solution simple et fonctionnelle serait d'afficher le message d'erreur et la stacktrace. Ajoutons également un bouton 'fermer' en bas.

```typescript
// imports
export const ERROR_INJECTOR_TOKEN: InjectionToken<any> = new InjectionToken('ErrorInjectorToken');

@Component({
  selector: 'btp-error-handler',
  // TODO: template sera implémenté plus tard
  template: `${error.message}<br><button (click)="dismiss()">FERMER</button>`
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

Comme vous pouvez le voir, le composant lui-même est assez simple. Nous allons utiliser deux directives plutôt importantes dans le template, pour rendre la boîte de dialogue accessible. La première est _cdkTrapFocus_ qui piégera le focus lorsque la boîte de dialogue sera rendue. Cela signifie que l'utilisateur ne peut pas se concentrer sur les éléments derrière notre boîte de dialogue modale. La deuxième directive est _cdkTrapFocusAutoCapture_ qui se concentrera automatiquement sur le premier élément focusable à l'intérieur de notre piège de focus. De plus, elle restaurera automatiquement le focus sur l'élément précédemment focalisé, lorsque notre boîte de dialogue sera fermée.

Afin de pouvoir afficher les propriétés de l'erreur, nous devons l'injecter en utilisant le constructeur. Pour cela, nous avons besoin de notre propre _injectionToken_. Nous avons également créé une logique plutôt simple pour émettre un événement de fermeture en utilisant un sujet et la propriété _dismiss$_. Relions cela à notre méthode _handleError_ dans notre service et faisons un peu de refactoring.

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

Concentrons-nous d'abord sur la fourniture de l'erreur en tant que paramètre injecté. Comme vous pouvez le voir, la classe _ComponentPortal_ attend un paramètre obligatoire, qui est le composant lui-même. Le deuxième paramètre est un _ViewContainerRef_ qui aurait un effet sur la place logique du composant dans l'arbre des composants. Le troisième paramètre est notre méthode _createInjector_. Comme vous pouvez le voir, elle retourne une nouvelle instance de _PortalInjector_. Jetons un rapide coup d'œil à son implémentation sous-jacente :

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

Comme vous pouvez le voir, il attend un _Injector_ comme premier paramètre et une WeakMap pour les tokens personnalisés. Nous avons fait exactement cela en utilisant notre _ERROR_INJECTOR_TOKEN_ qui est associé à notre erreur elle-même. Le _PortalInjector_ créé est utilisé pour l'instanciation correcte de notre _ErrorHandlerComponent_, il garantira que l'erreur elle-même sera présente dans le composant.

Enfin, notre méthode _attachPortal_ retourne la propriété _dismiss$_ du composant nouvellement instancié. Nous nous y abonnons, et lorsqu'elle change, nous appelons _.dispose()_ sur notre _overlayRef_. Et notre boîte de dialogue modale d'erreur est fermée. Notez que nous appelons également complete sur notre sujet à l'intérieur du composant, donc nous n'avons pas besoin de nous désabonner.

---

Cela est excellent pour les erreurs qui sont levées lorsqu'il y a un problème dans le code côté client. Mais nous créons des applications web et nous utilisons des points de terminaison API. Alors, que se passe-t-il lorsqu'un point de terminaison REST retourne une erreur ?

Nous pouvons gérer chaque erreur dans son propre service, mais est-ce vraiment ce que nous voulons ? Si tout va bien, les erreurs ne seront pas levées. S'il y a des exigences spécifiques, par exemple pour gérer le [code de statut 418](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/418) avec une licorne volante, vous pourriez implémenter son gestionnaire dans son service. Mais lorsque nous sommes confrontés à des erreurs plutôt courantes, comme 404 ou 503, nous pourrions vouloir les afficher dans cette même boîte de dialogue d'erreur.

Rassemblons rapidement ce qui se passe lorsqu'une _HttpErrorResponse_ est levée. Cela se produira de manière asynchrone, donc nous allons probablement rencontrer des problèmes de détection de changement. Ce type d'erreur a des propriétés différentes de celles d'une simple erreur, donc nous pourrions avoir besoin d'une méthode de sanitisation. Maintenant, plongeons dans le vif du sujet en créant une interface plutôt simple pour _SanitisedError_ :

```typescript
export interface SanitizedError {
  message: string;
  details: string[];
}
```

Créons un template pour notre _ErrorHandlerComponent_ :

```typescript
// Imports

@Component({
  selector: 'btp-error-handler',
  template: `
    <section cdkTrapFocus [cdkTrapFocusAutoCapture]="true" class="btp-error-handler__container">
      <h2>Erreur</h2>
      <p>{{error.message}}</p>
      <div class="btp-error-handler__scrollable">
        <ng-container *ngFor="let detail of error.details">
          <div>{{detail}}</div>
        </ng-container>
      </div>
      <button class="btp-error-handler__dismiss button red" (click)="dismiss()">FERMER</button>
    </section>`,
  styleUrls: ['./error-handler.component.css'],
})
export class ErrorHandlerComponent implements OnInit {
 // ...
}
```

Nous avons enveloppé toute la modale dans une balise _<section>_ et nous y avons ajouté la directive _cdkTrapFocus_. Cette directive empêchera l'utilisateur de naviguer dans le DOM derrière notre overlay/modale. Le _[cdkTrapFocusAutoCapture]="true"_ garantit que le bouton de fermeture est immédiatement focalisé. Lorsque la modale est fermée, l'élément précédemment focalisé récupérera le focus. Nous affichons simplement le message d'erreur et les détails en utilisant _*ngFor_. Revenons à notre _ErrorHandlerService_ :

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

Avec une méthode _sanitiseError_ plutôt simple, nous créons un objet basé sur notre interface définie précédemment. Nous vérifions les types d'erreurs et remplissons les données en conséquence. La partie la plus intéressante est l'utilisation de l'injecteur pour obtenir _ngZone_. Lorsqu'une erreur se produit de manière asynchrone, elle se produit généralement en dehors de la détection de changement. Nous enveloppons notre _attachPortal_ avec _ngZone.run(/* ... */)_, donc lorsqu'une _HttpErrorResponse_ est capturée, elle est correctement rendue dans notre modale.

Bien que l'état actuel fonctionne bien, il manque toujours de personnalisation. Nous utilisons l'Overlay du module CDK, donc exposer un token d'injection pour les configurations personnalisées serait bien. Une autre lacune importante de ce module est que lorsqu'il est utilisé, un autre module ne peut pas être utilisé pour la gestion des erreurs. Par exemple, l'intégration de Sentry nécessiterait d'implémenter un module ErrorHandler similaire, mais léger. Afin de pouvoir utiliser les deux, nous devrions implémenter la possibilité d'utiliser des hooks à l'intérieur de notre gestionnaire d'erreurs. Créons d'abord notre _InjectionToken_ et notre configuration par défaut :

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

Ensuite, fournissons-le avec notre module, en utilisant notre méthode _forRoot_ existante :

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

Ensuite, intégrons cette gestion de configuration dans notre _ErrorHandlerService_ également :

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

Et nous sommes presque prêts. Intégrons un hook de gestionnaire d'erreurs tiers dans notre application :

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

Comme vous pouvez le voir, la gestion des erreurs est une partie extrêmement importante du développement logiciel, mais elle peut aussi être amusante.

Merci beaucoup d'avoir lu cet article de blog. Si vous préférez lire du code, veuillez consulter mon [dépôt git ng-reusables](https://github.com/TapaiBalazs/angular-reusables). Vous pouvez également essayer l'implémentation en utilisant ce [package npm](https://www.npmjs.com/package/@btapai/ng-error-handler).

Vous pouvez également me suivre sur [Twitter](https://twitter.com/TapaiBalazs) ou [GitHub](https://github.com/TapaiBalazs).