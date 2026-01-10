---
title: L'injection de dépendances Angular expliquée avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-07T23:41:00.000Z'
originalURL: https://freecodecamp.org/news/angular-dependency-injection
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cb0740569d1a4ca339e.jpg
tags:
- name: Angular
  slug: angular
- name: dependency injection
  slug: dependency-injection
- name: toothbrush
  slug: toothbrush
seo_title: L'injection de dépendances Angular expliquée avec des exemples
seo_desc: 'What is Dependency Injection?

  Motivation

  Dependency Injection is often more simply referred to as DI. The paradigm exists
  throughout Angular. It keeps code flexible, testable, and mutable. Classes can inherit
  external logic without knowing how to cre...'
---

# **Qu'est-ce que l'injection de dépendances ?**

#### **Motivation**

L'injection de dépendances est souvent plus simplement appelée DI. Ce paradigme existe dans tout Angular. Il garde le code flexible, testable et mutable. Les classes peuvent hériter de la logique externe sans savoir comment la créer. Les consommateurs de ces classes n'ont pas non plus besoin de savoir quoi que ce soit.

DI évite aux classes et aux consommateurs d'avoir à savoir plus que nécessaire. Pourtant, le code est aussi modulaire qu'avant grâce aux mécanismes soutenant DI dans Angular.

Les services sont un bénéficiaire clé de DI. Ils dépendent du paradigme pour l'_injection_ dans divers consommateurs. Ces consommateurs peuvent alors tirer parti de ce que le service fournit et/ou le transmettre ailleurs.

Les services ne sont pas seuls. Les directives, les pipes, les composants, et ainsi de suite : chaque schéma dans Angular bénéficie de DI d'une manière ou d'une autre.

## Injecteurs

Les injecteurs sont des structures de données qui stockent des instructions détaillant où et comment les services se forment. Ils agissent comme intermédiaires dans le système DI d'Angular.

Les classes de modules, de directives et de composants contiennent des métadonnées spécifiques aux injecteurs. Une nouvelle instance d'injecteur accompagne chacune de ces classes. De cette manière, l'arbre de l'application reflète sa hiérarchie d'injecteurs.

Les métadonnées `providers: []` acceptent les services qui s'enregistrent ensuite avec l'injecteur de la classe. Ce champ de fournisseur ajoute les instructions nécessaires pour qu'un injecteur fonctionne. Une classe (en supposant qu'elle a des dépendances) instancie un service en prenant sa classe comme type de données. L'injecteur aligne ce type et crée une instance de ce service au nom de la classe.

Bien sûr, la classe ne peut instancier que ce pour quoi l'injecteur a des instructions. Si l'injecteur de la classe n'a pas le service enregistré, il interroge alors son parent. Et ainsi de suite jusqu'à atteindre soit un injecteur avec le service, soit la racine de l'application.

Les services peuvent s'enregistrer auprès de n'importe quel injecteur dans l'application. Les services sont placés dans le champ de métadonnées `providers: []` des modules, directives ou composants de classe. Les enfants de la classe peuvent instancier un service enregistré dans l'injecteur de la classe. Les injecteurs enfants se replient sur les injecteurs parents après tout.

## Injection de dépendances

Regardons les squelettes de chaque classe : service, module, directive et composant.

```typescript
// service

import { Injectable } from '@angular/core';

@Injectable({
  providedIn: /* injector goes here */
})
export class TemplateService {
  constructor() { }
}
```

```typescript
// module

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: [],
  providers: [ /* services go here */ ]
})
export class TemplateModule { }
```

```typescript
// directive

import { Directive } from '@angular/core';

@Directive({
  selector: '[appTemplate]',
  providers: [ /* services go here */ ]
})
export class TemplateDirective {
  constructor() { }
}
```

```typescript
//component

import { Component } from '@angular/core';

@Component({
  selector: 'app-template',
  templateUrl: './template.component.html',
  styleUrls: ['./template.component.css'],
  providers: [ /* services go here */ ]
})
export class TemplateComponent {
  // class logic ...
}
```

Chaque squelette peut enregistrer des services auprès d'un injecteur. En fait, TemplateService _est_ un service. À partir d'Angular 6, les services peuvent maintenant s'enregistrer auprès des injecteurs en utilisant les métadonnées `@Injectable`.

##### **Dans tous les cas**

Remarquez les métadonnées `providedIn: string` (`@Injectable`) et `providers: []` (`@Directive`, `@Componet` et `@Module`). Elles indiquent aux injecteurs où et comment créer un service. Sinon, les injecteurs ne sauraient pas comment instancier.

Et si un service a des dépendances ? Où iraient les résultats ? Les fournisseurs répondent à ces questions afin que les injecteurs puissent instancier correctement.

Les injecteurs forment l'épine dorsale du framework DI. Ils stockent des instructions pour instancier des services afin que les consommateurs n'aient pas à le faire. Ils reçoivent des instances de services sans avoir besoin de savoir quoi que ce soit sur la dépendance source !

Je devrais également noter que d'autres schémas sans injecteurs peuvent toujours utiliser l'injection de dépendances. Ils ne peuvent pas enregistrer de services supplémentaires mais peuvent toujours instancier à partir des injecteurs.

## Service

Les métadonnées `providedIn: string` de `@Injectable` spécifient auprès de quel injecteur s'enregistrer. En utilisant cette méthode, et selon que le service est utilisé ou non, le service peut ou non s'enregistrer auprès de l'injecteur. Angular appelle cela _tree-shaking_.

Par défaut, la valeur est définie sur `‘root’`. Cela se traduit par l'injecteur racine de l'application. En gros, définir le champ sur `‘root’` rend le service disponible partout.

##### **Note rapide**

Comme mentionné précédemment, les injecteurs enfants se replient sur leurs parents. Cette stratégie de repli garantit que les parents n'ont pas à se réenregistrer pour chaque injecteur. Consultez cet article sur [Services et Injecteurs](https://guide.freecodecamp.org/angular/services-and-injectors) pour une illustration de ce concept.

Les services enregistrés sont des _singletons_. Cela signifie que les instructions pour instancier le service existent sur un seul injecteur. Cela suppose qu'il n'a pas été explicitement enregistré ailleurs.

## Module, Directive et Composant

Les modules et les composants ont chacun leur propre instance d'injecteur. Cela est évident étant donné le champ de métadonnées `providers: []`. Ce champ prend un tableau de services et les enregistre auprès de l'injecteur du module ou de la classe de composant. Cette approche se produit dans les décorateurs `@NgModule`, `@Directive` ou `@Component`.

Cette stratégie omet le _tree-shaking_, ou la suppression optionnelle des services inutilisés des injecteurs. Les instances de services vivent sur leurs injecteurs pour la durée de vie du module ou du composant.

## Instanciation des Références

Les références au DOM peuvent être instanciées à partir de n'importe quelle classe. Gardez à l'esprit que les références sont toujours des services. Elles diffèrent des services traditionnels en représentant l'état de quelque chose d'autre. Ces services incluent des fonctions pour interagir avec leur référence.

Les directives ont constamment besoin de références au DOM. Les directives effectuent des mutations sur leurs éléments hôtes via ces références. Voir l'exemple suivant. L'injecteur de la directive instancie une référence de l'élément hôte dans le constructeur de la classe.

```typescript
// directives/highlight.directive.ts

import { Directive, ElementRef, Renderer2, Input } from '@angular/core';

@Directive({
  selector: '[appHighlight]'
})
export class HighlightDirective {
  constructor(
    private renderer: Renderer2,
    private host: ElementRef
  ) { }

  @Input() set appHighlight (color: string) {
    this.renderer.setStyle(this.host.nativeElement, 'background-color', color);
  }
}
```

```html
// app.component.html

<p [appHighlight]="'yellow'">Texte en surbrillance !</p>
```

`Renderer2` est également instancié. Quel injecteur fournit ces services ? Eh bien, le code source de chaque service provient de `@angular/core`. Ces services doivent alors s'enregistrer auprès de l'injecteur racine de l'application.

```typescript
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppComponent } from './app.component';
import { HighlightDirective } from './directives/highlight.directive';

@NgModule({
  declarations: [
    AppComponent,
    HighlightDirective
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }
```

Un tableau de fournisseurs vide ? Pas de quoi s'inquiéter. Angular enregistre de nombreux services auprès de l'injecteur racine automatiquement. Cela inclut `ElementRef` et `Renderer2`. Dans cet exemple, nous gérons l'élément hôte via son interface provenant de l'instanciation de `ElementRef`. `Renderer2` nous permet de mettre à jour le DOM via le modèle de vue d'Angular.

Vous pouvez en lire plus sur les vues à partir de [cet article](https://guide.freecodecamp.org/angular/views). Elles sont la méthode préférée pour les mises à jour DOM/vue dans les applications Angular.

Il est important de reconnaître le rôle que jouent les injecteurs dans l'exemple ci-dessus. En déclarant des types de variables dans le constructeur, la classe obtient des services précieux. Le type de données de chaque paramètre correspond à un ensemble d'instructions dans l'injecteur. Si l'injecteur a ce type, il retourne une instance dudit type.

## Instanciation des Services

L'article [Services et Injecteurs](https://guide.freecodecamp.org/angular/services-and-injectors) explique cette section dans une certaine mesure. Cependant, cette section réitère en grande partie la section précédente. Les services fourniront souvent des références à autre chose. Ils peuvent tout aussi bien fournir une interface étendant les capacités d'une classe.

Le prochain exemple définira un service de journalisation qui est ajouté à l'injecteur d'un composant via ses métadonnées `providers: []`.

```typescript
// services/logger.service.ts

import { Injectable } from '@angular/core';

@Injectable()
export class LoggerService {
  callStack: string[] = [];

  addLog(message: string): void {
    this.callStack = [message].concat(this.callStack);
    this.printHead();
  }

  clear(): void {
    this.printLog();
    this.callStack = [];
    console.log("DELETED LOG");
  }

  private printHead(): void {
    console.log(this.callStack[0] || null);
  }

  private printLog(): void {
    this.callStack.reverse().forEach((log) => console.log(message));
  }
}
```

```typescript
// app.component.ts

import { Component } from '@angular/core';
import { LoggerService } from './services/logger.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [LoggerService]
})
export class AppComponent {
  constructor(private logger: LoggerService) { }

  logMessage(event: any, message: string): void {
    event.preventDefault();
    this.logger.addLog(`Message: ${message}`);
  }

  clearLog(): void {
    this.logger.clear();
  }
}
```

```html
// app.component.html

<h1>Exemple de journalisation</h1>
<form (submit)="logMessage($event, userInput.value)">
  <input #userInput placeholder="Tapez un message...">
  <button type="submit">SOUMETTRE</button>
</form>

<h3>Supprimer les messages journalisés</h3>
<button type="button" (click)="clearLog()">EFFACER</button>
```

Concentrez-vous sur le constructeur et les métadonnées d'AppComponent. L'injecteur de composant reçoit des instructions du champ de métadonnées du fournisseur contenant LoggerService. L'injecteur sait alors quoi instancier pour LoggerService demandé dans le constructeur.

Le paramètre de constructeur `loggerService` a le type `LoggerService` que l'injecteur reconnaît. L'injecteur procède à l'instanciation comme mentionné.

## Conclusion

L'injection de dépendances (DI) est un paradigme. La manière dont elle fonctionne dans Angular est à travers une hiérarchie d'injecteurs. Une classe reçoit ses ressources sans avoir à les créer ou à les connaître. Les injecteurs reçoivent des instructions et instancient un service en fonction de celui qui a été demandé.

DI apparaît beaucoup dans Angular. La documentation officielle d'Angular explique pourquoi ce paradigme est si prévalent. Ils vont également décrire les nombreux cas d'utilisation de DI dans Angular bien au-delà de ce qui a été discuté dans cet article. Cliquez ci-dessous pour le découvrir !

## Plus sur l'injection de dépendances :

* [Intro à l'injection de dépendances Angular](https://www.freecodecamp.org/news/angular-dependency-injection-in-detail-8b6822d6457c/)
* [Intro rapide à l'injection de dépendances](https://www.freecodecamp.org/news/angular-dependency-injection/freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/)