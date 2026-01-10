---
title: Comment utiliser @Input() pour lire les paramètres de route Angular
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-10T21:18:44.000Z'
originalURL: https://freecodecamp.org/news/use-input-for-angular-route-parameters
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/thumbnail.png
tags:
- name: Angular
  slug: angular
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Comment utiliser @Input() pour lire les paramètres de route Angular
seo_desc: "By Deborah Kurata\nOne of the new features in Angular v16 is automatic\
  \ route parameter mapping using the @Input() decorator.\nWhat does that mean? Well,\
  \ you may have code that reads route parameters using the Activated Route service,\
  \ like this:\n  priva..."
---

Par Deborah Kurata

L'une des nouvelles fonctionnalités d'Angular v16 est le mappage automatique des paramètres de route à l'aide du décorateur `@Input()`.

Qu'est-ce que cela signifie ? Eh bien, vous avez peut-être du code qui lit les paramètres de route en utilisant le service Activated Route, comme ceci :

```typescript
  private route = inject(ActivatedRoute);

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    if (id) {
      console.log(this.id);
    }
  }
```

Nous injectons d'abord le service Activated Route. Ensuite, nous obtenons le paramètre de route à partir de ce snapshot de route activée, en accédant à la méthode `get()` et en passant le nom du paramètre de route.

Dans Angular v16 et versions ultérieures, notre code peut lire les paramètres de route comme ceci :

```typescript
  @Input() id = '';

  ngOnInit(): void {
    console.log(this.id);
  }
```

Ici, nous utilisons une propriété d'entrée définie avec le décorateur `@Input()`. Angular lit automatiquement le paramètre de route et l'assigne à la propriété d'entrée. Cette syntaxe est beaucoup plus courte et plus facile !

Parcourons un exemple : d'abord en utilisant le service Activated Route, puis en essayant la nouvelle syntaxe de propriété d'entrée pour lire les paramètres de route.

Vous pouvez regarder la vidéo associée ici pour une démonstration :

%[https://youtu.be/Nuwn5uY8ETw]

## **Comment configurer une route avec un paramètre**

Que nous utilisions Activated Route ou une propriété d'entrée, nous devons d'abord configurer notre route avec un paramètre.

Par exemple, supposons que nous avons un composant Product List qui affiche une liste de produits comme le montre la Figure 1. Lorsque l'utilisateur clique sur un nom de produit, nous chargeons le composant Product Detail pour afficher les détails de ce produit (Figure 2).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-53.png)
_Figure 1. Liste des produits (composant Product List)_

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-54.png)
_Figure 2. Détails du produit avec un id de 5 (composant Product Detail)_

Pour réaliser cette fonctionnalité, le composant Product List ajoute l'id du produit sélectionné à la route en tant que paramètre. Cela est montré dans la barre d'adresse de la Figure 2. Le composant Product Detail lit cet id à partir du paramètre de route et l'utilise pour afficher les détails du produit sélectionné.

La configuration pour la route de détail du produit ressemble à ceci :

```typescript
  { path: ':id', component: ProductDetailComponent }
```

Nous identifions un paramètre de route en ajoutant un deux-points avant le nom du paramètre, qui dans cet exemple est `id`. Partout où nous référençons ce paramètre, nous utiliserons ce nom.

La route de détail du produit est activée lorsque l'utilisateur clique sur un lien de produit dans le composant Product List. Le code pour ce lien utilise la directive `routerLink` pour définir le paramètre id :

```html
 <a [routerLink]="[product.id]"> {{ product.productName }} </a>  
```

Lorsque l'utilisateur clique sur ce lien, le `routerLink` ajoute l'id du produit à l'URL. Le routeur utilise la configuration de la route pour trouver un chemin de route correspondant et route vers le composant Product Detail.

Le code dans le composant Product Detail lit ensuite le paramètre à partir de l'URL et affiche les détails du produit.

## Comment lire les paramètres de route (Activated Route)

Une technique pour lire le paramètre à partir de l'URL utilise le service Activated Route d'Angular.

```typescript
import { Component, OnInit, inject } from '@angular/core';
import { ActivatedRoute } from '@angular/router';


  private route = inject(ActivatedRoute);

  ngOnInit(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    if (id) {
      this.productDetailService.setSelectedProductId(id);
    }
  }
```

Nous injectons d'abord le service Activated Route en utilisant le nouveau mot-clé `inject()` d'Angular. Alternativement, nous pourrions utiliser le constructeur pour injecter cette dépendance de service.

Pour lire le paramètre lorsque le composant Product Detail se charge pour la première fois, nous utilisons le hook de cycle de vie OnInit. Nous déclarons une constante pour le paramètre. Ensuite, nous définissons cette constante en utilisant le service Activated Route. Nous accédons à la `paramMap` du snapshot de la route, et appelons sa méthode `get()`, en passant le nom du paramètre à obtenir. Ce nom doit correspondre au nom du paramètre que nous avons défini dans la configuration de la route.

Les paramètres de route sont des chaînes de caractères, donc la méthode `get()` retourne une chaîne, ou null si le paramètre n'est pas trouvé. Dans cet exemple, les identifiants de produit sont des nombres. Nous utilisons donc le constructeur `Number()` pour créer un nombre à partir de la chaîne.

Si le code lit avec succès l'id à partir de la route, nous définissons cet id dans le service Product Detail. Le service Product Detail trouve ensuite le produit avec l'id défini. Notre composant se lie au produit résultant et affiche les détails de ce produit.

Nous pouvons simplifier ce code si nous utilisons le décorateur `@Input()` à la place.

## **Comment commencer à utiliser `@Input()` pour les paramètres de route**

La première chose que nous devons faire, et l'étape que j'oublie si souvent, est de laisser Angular savoir que nous voulons utiliser des propriétés d'entrée pour lire les paramètres de route. Nous faisons cela dans la configuration de l'application.

Comment nous faisons cela dépend du type de bootstrapping que notre application utilise.

Avec le bootstrapping de composant autonome, nous bootstrappons une application comme ceci :

```typescript
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err)); 
```

Ensuite, dans le `appConfig`, nous fournissons les routes comme ceci :

```typescript
import { ApplicationConfig } from '@angular/core';
import { provideRouter, withComponentInputBinding } from '@angular/router';

import { provideHttpClient } from '@angular/common/http';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(),
    provideRouter(routes, withComponentInputBinding())
  ]
};

```

La fonction `provideRouter()` configure les fournisseurs pour le routeur. Nous passons les routes _et_ `withComponentInputBinding()`. C'est le `withComponentInputBinding()` qui permet à Angular de savoir que nous voulons utiliser des propriétés d'entrée pour lire les paramètres de route.

Si vous utilisez plutôt le bootstrapping NgModule, le code ressemble à ceci :

```typescript
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
```

Dans cet exemple, le `AppModule` importe le `AppRoutingModule` qui ressemble à ceci :

```typescript
import { NgModule } from '@angular/core';
import { RouterModule } from '@angular/router';

import { WelcomeComponent } from './home/welcome.component';

@NgModule({
  imports: [
    RouterModule.forRoot([
      { path: 'welcome', component: WelcomeComponent },
      { path: '', redirectTo: 'welcome', pathMatch: 'full' },
      {
        path: 'products',
        loadChildren: () =>
          import('./products/product.module').then(m => m.ProductModule)
      },
      { path: '**', redirectTo: 'welcome', pathMatch: 'full' }
    ], { bindToComponentInputs: true })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }

```

Dans le `RouterModule.forRoot()`, nous définissons `bindToComponentInputs` à true pour permettre à Angular de savoir que nous voulons utiliser des propriétés d'entrée pour lire les paramètres de route.

Nous avons maintenant activé le mappage automatique des paramètres de route en utilisant des propriétés d'entrée.

## **Comment lire les paramètres de route (@Input)**

Nous ajoutons une propriété d'entrée en utilisant le décorateur `@Input()`.

```typescript
  @Input() id = '';
```

Nous pouvons nommer la propriété d'entrée de la même manière que le paramètre de route, qui dans cet exemple est `id`. Les paramètres de route sont des chaînes de caractères, donc nous définissons la valeur initiale à une chaîne vide.

Si nous voulons utiliser un nom de propriété différent, tel que `productId`, nous pouvons. Mais alors nous devons passer le nom du paramètre de route au décorateur `@Input()`, comme ceci :

```typescript
@Input('id') productId ='';
```

De cette façon, Angular peut faire correspondre le paramètre de route à la propriété d'entrée appropriée.

Nous pouvons ensuite simplifier le code du hook de cycle de vie `OnInit` comme ceci :

```typescript
  ngOnInit(): void {
    if (this.id) {
      this.productDetailService.setSelectedProductId(Number(this.id));
    }
  }
```

Puisque nous utilisons une propriété d'entrée, nous n'avons plus besoin de l'Activated Route. Nous pouvons simplement accéder directement à la propriété d'entrée. Puisque la méthode `setSelectedProductId()` attend un nombre, nous ajoutons le constructeur `Number()` autour de l'id pour le convertir en nombre.

## **Comment transformer les propriétés d'entrée**

À partir d'Angular v16.1, le décorateur `@Input()` fournit une fonction `transform`. Nous utilisons la fonction `transform` pour effectuer une transformation ou exécuter une autre logique lorsqu'une propriété d'entrée change.

Pour simplifier davantage notre code, Angular a introduit deux fonctions de transformation intégrées : `booleanAttribute` et `numberAttribute`.

Pour notre cas, nous voulons transformer la chaîne de paramètre de route en un nombre. En utilisant une fonction de transformation, notre code ressemble alors à ceci :

```typescript
 import { Component, OnInit, Input, numberAttribute } from '@angular/core';


  @Input({transform: numberAttribute}) id = 0;

  ngOnInit(): void {
    if (this.id) {
      this.productDetailService.setSelectedProductId(this.id);
    }
  }
```

Nous passons un objet au décorateur `@Input()` et définissons la fonction `transform` à `numberAttribute`. Puisque le paramètre de route de chaîne est ensuite transformé en nombre, nous changeons la valeur initiale à `0` à la place d'une chaîne vide `''`. Et maintenant que l'id résultant est un nombre, nous n'avons plus besoin de le convertir nous-mêmes avec la fonction de création `Number()`.

## **Pourquoi utiliser les paramètres de route ?**

Une question que je me pose toujours est "pourquoi". Pourquoi avons-nous besoin de paramètres de route ? Le composant Product List ne pourrait-il pas stocker l'id dans une propriété d'un service ? Ensuite, le composant Product Detail pourrait lire cet id à partir du service au lieu de la route.

Une raison clé est qu'en ajoutant l'id à l'URL, nous obtenons un **lien profond**. Le lien profond permet à l'utilisateur de sauvegarder ou de partager l'URL et d'avoir un lien direct automatique vers un produit spécifique.

Supposons que votre anniversaire approche et que vous envoyez à un ami un lien Amazon. Ce lien ne serait pas utile s'il ne navigait pas directement vers un produit spécifique.

Utilisez le lien profond chaque fois que vous voulez permettre à vos utilisateurs de sauvegarder ou d'envoyer des liens directs.

## Conclusion

À partir d'Angular v16, nous pouvons utiliser une propriété d'entrée, définie avec le décorateur `@Input()`, pour accéder aux paramètres de route. Cela nous donne une syntaxe plus courte et plus facile. Nous n'avons plus besoin de travailler avec le service Activated Route d'Angular.

Mais n'oubliez pas d'activer cette fonctionnalité !

* Si vous utilisez le bootstrapping autonome, ajoutez `withComponentInputBinding()` à `provideRouter()`.
* Pour le bootstrapping classique NgModule, définissez `bindToComponentInputs` à true dans `RouterModule.forRoot()`.

Pour voir ces concepts en action, consultez la démonstration fournie dans cette vidéo :

%[https://youtu.be/Nuwn5uY8ETw]

