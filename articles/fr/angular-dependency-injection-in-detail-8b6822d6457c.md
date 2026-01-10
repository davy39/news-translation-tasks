---
title: Une introduction à l'injection de dépendances dans Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T21:14:06.000Z'
originalURL: https://freecodecamp.org/news/angular-dependency-injection-in-detail-8b6822d6457c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xQW9Spiz8U0tNEuX_m2blw.jpeg
tags:
- name: Angular
  slug: angular
- name: dependency injection
  slug: dependency-injection
seo_title: Une introduction à l'injection de dépendances dans Angular
seo_desc: 'By Neeraj Dana

  In this article, we will see how the dependency injection of Angular works internally.
  Suppose we have a component named appcomponent which has a basic and simple structure
  as follows:

  import { Component, OnInit } from "@angular/core";...'
---

Par Neeraj Dana

Dans cet article, nous allons voir comment fonctionne l'injection de dépendances d'Angular en interne. Supposons que nous avons un composant nommé appcomponent qui a une structure de base et simple comme suit :

```
import { Component, OnInit } from "@angular/core";@Component({  selector: "my-root",  templateUrl: "app.component.html",  styleUrls: ["app.component.css"]})export class AppComponent implements OnInit {  ngOnInit(): void {      }}
```

Et nous avons une classe de service nommée GreetingService avec une fonction `sayHello` qui prend un nom comme paramètre et retourne le nom avec « Hello » devant.

```
export class GreetingService{  sayHello(name){    return `Hello ${name}` ;  }}
```

Il existe deux façons d'utiliser la classe de service dans le composant : premièrement, nous pouvons créer manuellement une instance du service dans le composant (c'est la mauvaise façon et elle n'est jamais recommandée).

Et l'autre façon est de laisser Angular créer l'instance de notre service et de passer cette instance à notre composant en interne. C'est la manière commune et recommandée de le faire.

#### Injection de notre service dans le système d'injection de dépendances d'Angular

```
Import {Component} from '@angular/core';Import {GreetingService} from '. /greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ]})export class AppComponent  {
```

```
constructor(private greetingService : GreetingService){   console.log(this.greetingService.sayHello());  }}
```

Maintenant, si vous exécutez ce projet, vous obtiendrez l'erreur « No provider for GreetingService! »

![Image](https://cdn-media-1.freecodecamp.org/images/PA66RsT3fdnjttQROpVulvpDU6QGWfYoCxyl)

Donc, essentiellement, Angular se plaint de ne pas avoir trouvé de fournisseur pour créer une instance du service de salutation ou de ne pas savoir comment créer une instance. Afin de permettre au framework de savoir comment l'instance doit être créée, nous devons passer un objet fournisseur à la propriété providers dans le décorateur de composant montré ci-dessous :

```
import { Component } from '@angular/core';import {GreetingService} from './greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{      }]})export class AppComponent  {
```

```
constructor(private greetingService : GreetingService){   console.log(this.greetingService.sayHello());  }  }
```

Dans cet objet fournisseur, nous avons de nombreuses propriétés, alors comprenons-les une par une.

#### Usine personnalisée

use factory : cela indiquera au framework quelle usine sera utilisée lors de la création de l'objet du service. Dans notre cas, nous n'avons pas d'usine, alors créons-en une.

L'usine sera une fonction qui sera responsable de la création et du retour de l'objet du service.

```
export function greetingFactory(){   return  new GreetingService()};
```

```
Ou une manière plus courte
```

```
export const greetingFactory= () =>  new GreetingService ();
```

#### Jeton d'injection personnalisé

La prochaine chose est de créer une propriété dont la valeur sera une instance de Injection Token. En utilisant cette propriété, le framework identifiera de manière unique notre service et injectera la bonne instance du service.

```
var greetingTokken = new InjectionToken<GreetingService>("GREET_TOKEN");
```

Donc, dans l'extrait ci-dessus, nous créons une instance de la classe InjectionToken et elle est générique. Dans notre cas, l'instance de GreetingService sera injectée lorsque quelqu'un demandera l'injection avec le nom greetingToken.

Jusqu'à présent, notre code ressemblera à ceci :

```
import { Component ,InjectionToken} from '@angular/core';import {GreetingService} from './greetingService';
```

```
export const greetingTokken = new InjectionToken<GreetingService>("GREET_TOKEN");export const greetingFactory=()=>  new GreetingService();@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{    provide  : greetingTokken,    useFactory : greetingFactory,     }]})export class AppComponent  {
```

```
constructor(private greetingService : GreetingService){   console.log(this.greetingService.sayHello());  }  name = 'Angular';}
```

Mais alors nous aurons toujours la même erreur :

![Image](https://cdn-media-1.freecodecamp.org/images/yOKshbzOHxjiPigdOXBK8p-IUkH7wOc8wnf8)

C'est parce que dans le constructeur, où nous demandons l'instance de notre service, nous devons lui indiquer la chaîne unique de notre jeton d'injection, c'est-à-dire `greetingToken`.

Alors mettons à jour notre code :

```
export class AppComponent  {
```

```
constructor(@Inject(greetingTokken) private greetingService : GreetingService){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

Et maintenant nous aurons le résultat qui nous permet de passer avec succès un service depuis l'injection de dépendances d'Angular.

![Image](https://cdn-media-1.freecodecamp.org/images/Z0y7nt8qPli6OdjGSse2dEhxJV11Mk-yQ4kz)

Maintenant, supposons que vous avez des dépendances imbriquées comme ceci :

```
import{DomSanitizer} from '@angular/platform-browser';
```

```
export class GreetingService{  constructor (private domSanitizer:DomSanitizer){      }  sayHello(name){    return `Hello ${name}`  }}
```

Donc, dans ce cas, nous devons passer une propriété supplémentaire à l'objet du fournisseur (c'est-à-dire deps) qui est le tableau de toutes les dépendances :

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{    provide  : greetingTokken,    useFactory : greetingFactory,    deps:[DomSanitizer]     }]})export class AppComponent  {
```

```
constructor(@Inject(greetingTokken) private greetingService : GreetingService  ){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

> **_Jusqu'à maintenant, tout ce que nous avons fait n'a été que pour des fins d'apprentissage. Il n'est pas recommandé de créer des fournisseurs manuels sauf s'il y a un besoin._**

Donc, c'est tout le travail difficile fait par Angular en coulisses pour nous. Nous n'avons pas à faire tout cela pour enregistrer notre service. Nous pouvons en fait réduire le code, et au lieu de passer la factory et le token manuellement, nous pouvons demander au framework de le faire pour nous dans ce cas.

La propriété provide, qui est le jeton d'injection, sera le nom du service et Angular créera interne un jeton d'injection et une factory pour nous.

Nous devons passer une propriété supplémentaire (use-class) qui indique au framework quelle classe nous devons utiliser :

```
import { Component ,InjectionToken,Inject} from '@angular/core';
```

```
import {GreetingService} from './greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[{    provide  : GreetingService,    useClass :GreetingService     }]})export class AppComponent  {
```

```
constructor( private greetingService : GreetingService  ){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

Donc maintenant notre code semble beaucoup plus propre et nous pouvons le réduire davantage en passant simplement le nom du service. Ensuite, Angular sous le capot créera l'objet provide, la factory et le jeton d'injection pour nous et rendra l'instance disponible lorsque nécessaire.

```
import { Component } from '@angular/core';
```

```
import {GreetingService} from './greetingService';
```

```
@Component({  selector: 'my-app',  templateUrl: './app.component.html',  styleUrls: [ './app.component.css' ],  providers:[GreetingService]})export class AppComponent  {
```

```
constructor( private greetingService : GreetingService  ){   console.log(this.greetingService.sayHello('Neeraj'));  }  name = 'Angular';}
```

Donc, à la fin, notre code semble très familier. Maintenant, à l'avenir, chaque fois que vous créerez un service, vous saurez exactement quelles étapes sont impliquées pour obtenir cette instance disponible.

Si vous aimez cet article, suivez-moi pour obtenir plus de ce genre de contenu.

![Image](https://cdn-media-1.freecodecamp.org/images/GHJHXu-n2p6nfjIZmNgTMyNt-MBPTvPRLTkt)

Visitez [Smartcodehub](https://www.smartcodehub.com/)