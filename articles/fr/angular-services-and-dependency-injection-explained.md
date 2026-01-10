---
title: Services Angular et Injection de Dépendances Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/angular-services-and-dependency-injection-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d5e740569d1a4ca3765.jpg
tags:
- name: Angular
  slug: angular
- name: dependency injection
  slug: dependency-injection
- name: toothbrush
  slug: toothbrush
seo_title: Services Angular et Injection de Dépendances Expliqués
seo_desc: 'Services and Injectors

  Components are responsible for the data that renders into the template. Having external
  services to draw upon can simplify this responsibility. Plus, encapsulating extraneous
  is much easier to maintain.

  Delegating too many resp...'
---

# **Services et Injecteurs**

Les composants sont responsables des données qui sont rendues dans le template. Avoir des _services_ externes sur lesquels s'appuyer peut simplifier cette responsabilité. De plus, encapsuler l'excédent est beaucoup plus facile à maintenir.

Déléguer trop de responsabilités à un seul composant peut compliquer la classe du composant. Et si ces responsabilités s'appliquaient à plusieurs composants ? Copier et coller une telle logique est une très mauvaise pratique. Toute modification future de la logique serait plus difficile à implémenter et à tester.

Angular a été conçu pour résoudre ce problème avec les services et l'injection de dépendances. Les deux concepts fonctionnent ensemble pour fournir une fonctionnalité _modulaire_.

Les composants n'ont pas besoin de fournir d'informations superflues non plus. Un service importe ce dont il a besoin pour fonctionner au nom des composants qu'il _service_. Les composants n'ont besoin que d'instancier le service. À partir de là, ils _servent_ leurs propres besoins avec l'instance de service instanciée.

En ce qui concerne les tests et les modifications futures, toute la logique est en un seul endroit. Le service est instancié à partir de sa source. Les tests et les modifications de la source s'appliquent partout où le service est injecté.

## Introduction aux Services

Un service est un type de _schéma_ disponible dans Angular. Il peut être généré par l'interface en ligne de commande (CLI) : `ng generate service [nom-du-service]`. Remplacez `[nom-du-service]` par un nom préférable. La commande CLI produit le résultat suivant.

```typescript
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoggerService {
  constructor() { }
}
```

La logique d'un service est distincte dans sa classe. Angular interprète une classe comme un service _injectable_ basé sur le décorateur `@Injectable`. Les services injectables doivent être _enregistrés_ avec un injecteur.

Le composant instancie un service tandis que l'injecteur fournit cette instance. Continuez à lire la section suivante pour en savoir plus sur les injecteurs.

Le champ de métadonnées `@Injectable` `providedIn: 'root'` cible le module racine de l'application actuelle (`app.module.ts`). Il enregistre le service avec l'injecteur du module afin qu'il puisse _injecter_ ce service dans l'un de ses enfants.

Les injecteurs sont les éléments de base du système d'injection de dépendances d'Angular. Les injecteurs sont un bon endroit pour concentrer votre attention avant de continuer avec les services.

## Injecteurs

Une application, commençant par `app.module.ts`, contient une hiérarchie d'injecteurs. Ils existent aux côtés de chaque module et composant dans l'arbre de l'application.

![Hiérarchie de l'Application](https://raw.githubusercontent.com/sosmaniac-FCC/designatedata/master/image5.png)

Les cercles verts indiquent les injecteurs. Ils fournissent des instances de service aux composants d'instanciation. Selon l'injecteur avec lequel un service est enregistré, il peut être disponible ou non pour un composant.

Les services enregistrés à la racine de l'application (`app.module.ts`) sont disponibles pour tous les composants. Un injecteur pour un composant peut ne pas avoir un certain service enregistré. Si c'est le cas et que le composant demande son instanciation, l'injecteur se reportera à son parent. Cette tendance se poursuit jusqu'à atteindre soit l'injecteur racine, soit le service est trouvé.

En regardant le diagramme, supposons qu'un service s'enregistre au niveau de l'injecteur du point B. Tous les composants au point C et en dessous ne pourront pas accéder au service enregistré au niveau de l'injecteur de B. Les injecteurs ne se reporteront jamais à leurs enfants pour une instance de service.

### Injection de Dépendances

Il existe plusieurs façons d'enregistrer un service avec les injecteurs d'une application.

Le champ de métadonnées `providedIn: 'root'` de `@Injectable` fournit l'approche la plus recommandée. Ce champ de métadonnées a été publié avec Angular 6.

Comme mentionné précédemment, `providedIn: 'root'` enregistre un service avec l'injecteur du module racine. Il est instanciable dans toute l'application en conséquence.

La nouveauté de `providedIn: 'root'` est le _tree-shaking_. Si le service n'est pas utilisé malgré son enregistrement, il est _secoué_ de l'application au moment de l'exécution. Ainsi, il ne consomme aucune ressource.

Les deux autres méthodes sont plus directes et traditionnelles. Certes, elles n'offrent pas de tree-shaking.

Un service peut s'enregistrer avec n'importe quel injecteur le long de l'arbre des composants. Vous insérez le service en tant que fournisseur dans le champ de métadonnées `@Component` : `providers: []`. Le service est disponible pour le composant et ses enfants.

Dans la troisième stratégie d'enregistrement, les métadonnées `providers: []` existent en tant que champ propre dans le décorateur `@NgModule`. Le service est instanciable à partir du module vers l'arbre des composants sous-jacents.

Rappelez-vous que, contrairement à `providedIn: 'root'`, l'enregistrement `@NgModule` n'offre pas de tree-shaking. Les deux stratégies sont par ailleurs identiques. Une fois qu'un service est enregistré avec `@NgModule`, il consomme des ressources même s'il est laissé inutilisé par l'application.

## Services Continus

Écrire un service réel vient ensuite. Pour résumer, les services gèrent certaines fonctions au nom des composants d'une application.

Les services excellent dans la gestion des opérations courantes. Ils épargnent aux composants la responsabilité en faisant cela. Cela fait gagner du temps en évitant de réécrire des opérations courantes dans plusieurs composants. C'est aussi plus testable car le code est en un seul endroit. Les modifications n'ont besoin de se faire qu'en un seul endroit sans avoir à chercher ailleurs.

## Cas d'Utilisation

Quelques exemples permettent de mieux comprendre les services.

* logs de la console
* requêtes API

Les deux sont courants dans la plupart des applications. Avoir des services pour gérer ces opérations réduira la complexité des composants.

### Logs de la Console

Cet exemple s'appuie sur le squelette de base `@Injectable`. Le squelette est disponible en exécutant la CLI (`ng generate service [nom-du-service]`).

```typescript
// services/logger.service.ts

import { Injectable } from '@angular/core';

interface LogMessage {
  message:string;
  timestamp:Date;
}

@Injectable({
  providedIn: 'root'
})
export class LoggerService {
  callStack:LogMessage[] = [];

  constructor() { }

  addLog(message:string):void {
      // préfixer le nouveau log au bas de la pile
      this.callStack = [{ message, timestamp: new Date() }].concat(this.callStack);
  }

  clear():void {
      // vider la pile
      this.callStack = [];
  }

  printHead():void {
      // imprimer le bas de la pile
      console.log(this.callStack[0] || null);
  }

  printLog():void {
      // imprimer le bas vers le haut de la pile à l'écran
      this.callStack.reverse().forEach((logMessage) => console.log(logMessage));
  }

  getLog():LogMessage[] {
      // retourner l'ensemble du log sous forme de tableau
      return this.callStack.reverse();
  }
}
```

LoggerService s'enregistre avec le module racine via les métadonnées `@Injectable`. Ainsi, il peut être instancié dans `app.component.html`.

```typescript
// app.component.ts

import { Component, OnInit } from '@angular/core';
import { LoggerService } from './services/logger.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html'
})
export class AppComponent implements OnInit {
  logs:object[] = [];

  constructor(private logger:LoggerService) { }

  updateLog():void {
      this.logger.printHead();
      this.logs = this.logger.getLog();
  }

  logMessage(event:any, message:string):void {
      event.preventDefault();

      this.logger.addLog(`Message: ${message}`);
      this.updateLog();
  }

  clearLog():void {
      this.logger.clear();
      this.logs = [];
  }

  ngOnInit():void {
      this.logger.addLog("View Initialized");
      this.updateLog();
  }
}
```

Le template HTML fournit plus d'informations sur l'utilisation de LoggerService par le composant.

```html
<!-- app.component.html -->

<h1>Exemple de Log</h1>

<form (submit)="logMessage($event, userInput.value)">
  <input #userInput placeholder="Tapez un message...">
  <button type="submit">SOUMETTRE</button>
</form>

<h3>Log Complet</h3>
<button type="button" (click)="clearLog()">EFFACER</button>
<ul>
  <li *ngFor="let log of logs; let i=index">{{ logs.length - i }} > {{ log.message }} @ {{ log.timestamp }}</li>
</ul>
```

Cela ressemble à une application ToDo. Vous pouvez enregistrer des messages et effacer le log des messages. Imaginez si toute la logique du service était entassée dans AppComponent ! Cela aurait compliqué le code. LoggerService garde le code lié au log encapsulé de la classe principale AppComponent.

### Requêtes Fetch

Voici un autre exemple qui vaut la peine d'être exploré. Cet exemple est possible grâce à [JSONPlaceholder de typicode<sup>1</sup>](https://jsonplaceholder.typicode.com/). L'API est publique et gratuite à utiliser.

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

// https://jsonplaceholder.typicode.com
// API publique créée par typicode @ https://github.com/typicode

interface Post {
  userId:number;
  id:number;
  title:string;
  body:string;
}

@Injectable({
  providedIn: 'root'
})
export class PlaceholderService {
  constructor(private http:HttpClient) { }

  getPosts():Observable<Post[]> {
      return this.http.get('https://jsonplaceholder.typicode.com/posts');
  }

  getPost(id:number):Observable<Post> {
      return this.http.get(`https://jsonplaceholder.typicode.com/posts/${id}`);
  }
}
```

Ceci est plus une pièce autonome qu'un exemple entièrement développé. Les requêtes fetch tendent à mieux fonctionner en tant que service injectable. L'alternative est un composant trop compliqué. La classe injectée s'abonne à ce que PlaceholderService préconfigure.

## Conclusion

Les services et l'injection de dépendances sont très utiles ensemble. Ils permettent aux développeurs d'encapsuler la logique commune et de l'injecter dans plusieurs composants différents. Cela seul est une commodité massive pour toute maintenance future.

Les injecteurs fonctionnent comme intermédiaires. Ils médiatisent entre les composants d'instanciation et un réservoir de services enregistrés. Les injecteurs offrent ces services instanciables à leurs enfants de branche.

Voir les liens suivants pour plus d'informations sur les services et l'injection de dépendances.

## **Ressources pour Angular**

* [Documentation Angular](https://angular.io/docs)
* [Introduction à l'injection de dépendances Angular](https://www.freecodecamp.org/news/angular-dependency-injection-in-detail-8b6822d6457c/)
* [Qu'est-ce que l'injection de dépendances et quand l'utiliser](https://www.freecodecamp.org/news/a-quick-intro-to-dependency-injection-what-it-is-and-when-to-use-it-7578c84fa88f/)
* [Meilleurs exemples de code Angular](https://www.freecodecamp.org/news/the-best-angular-examples/)
* [Dépôt GitHub Angular](https://github.com/angular/angular)
* [Injection de Dépendances](https://angular.io/guide/dependency-injection-pattern)
* [Introduction aux Services et DI](https://angular.io/guide/architecture-services)