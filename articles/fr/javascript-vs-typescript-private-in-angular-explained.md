---
title: 'Comment masquer vos propriétés Angular – # vs private expliqué'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-20T20:39:45.000Z'
originalURL: https://freecodecamp.org/news/javascript-vs-typescript-private-in-angular-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/hash-v-private-thumbnail.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: TypeScript
  slug: typescript
seo_title: 'Comment masquer vos propriétés Angular – # vs private expliqué'
seo_desc: 'By Deborah Kurata

  Have you noticed a hash symbol showing up in Angular code samples? If not, you may
  see it soon. What is the purpose of the # and when should you use it?

  The # symbol was recently added to JavaScript to denote private class propertie...'
---

Par Deborah Kurata

Avez-vous remarqué un symbole dièse apparaître dans les exemples de code Angular ? Si ce n'est pas le cas, vous pourriez le voir bientôt. Quel est le but du `#` et quand devez-vous l'utiliser ?

Le symbole `#` a été récemment ajouté à JavaScript pour désigner les propriétés de classe privées. Rendre une variable de classe privée signifie que la variable ne peut être accessible qu'au sein de sa classe. Cela nous permet d'encapsuler les données que nous souhaitons uniquement accéder au sein d'un service.

Mais n'avons-nous pas déjà un accesseur privé pour nos champs de classe ? Oui !

Alors pourquoi avons-nous besoin de la nouvelle syntaxe de hachage ?

Examinons d'abord l'accesseur privé, puis analysons la syntaxe `#` et pourquoi elle est un meilleur choix dans nos applications Angular.

Vous pouvez regarder la vidéo associée ici pour une démonstration :

%[https://youtu.be/487iCAnhxCM]

## Le danger des propriétés de classe publiques

Commençons par créer une propriété dans un service et tentons d'y accéder depuis notre composant. Pour cet exemple, nous avons un service Product et un composant Product.

Dans le service Product, nous créons une propriété pour l'URL que nous utiliserons pour obtenir nos données de produit. Et une propriété `products` pour contenir notre tableau de produits récupéré.

```typescript
// Product Service
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  productUrl = 'api/products';
  products = [];

}
```

Pour vérifier la valeur de l'URL, créons une méthode pour la logger :

```typescript
// Product Service
logUrl() {
  console.log('Url:', this.productUrl);
}
```

Ensuite, nous appellerons cette méthode dans le constructeur du service Product :

```typescript
// Product Service
constructor() {
  this.logUrl();
}
```

Par défaut, les variables que nous définissons dans une classe sont publiques, ce qui signifie que tout autre code dans notre application peut y accéder. Nous devrions donc pouvoir accéder à nos propriétés de service Product depuis notre composant.

Essayons. Dans le composant Product, nous injectons d'abord le service. Dans cet exemple, nous utilisons la nouvelle fonction `inject` pour l'injection de dépendances au lieu du constructeur. Et nous ajoutons `inject` à l'instruction d'importation depuis `@angular/core`.

Ensuite, nous ajoutons un constructeur. Et parce que par défaut toute propriété ou méthode d'une classe est publique, nous pouvons changer l'URL que nous avons définie dans le service. Pour confirmation, nous appellerons la méthode de service pour logger l'URL.

```typescript
// Product Component
productService = inject(ProductService);

constructor() {
  this.productService.productUrl = `api/nefarious`;

  this.productService.logUrl();
}
```

Si nous exécutons l'application et ouvrons les outils de développement, nous voyons d'abord le service logger l'URL, puis nous voyons l'URL modifiée par le composant (Figure 1).

![Console log includes api/products and api/nefarious](https://www.freecodecamp.org/news/content/images/2023/06/image-191.png)
_Figure 1. Résultat de la sortie de la console._

Eh bien... ce n'est pas bon. Notre composant a pu changer l'URL définie dans notre service.

## La fonctionnalité d'accessibilité privée de TypeScript

Pour mieux protéger nos propriétés de service contre les modifications en dehors du service, nous utilisons **l'accessibilité privée**. 

L'accessibilité privée est une fonctionnalité de TypeScript. Elle marque une propriété ou une méthode de classe de sorte qu'elle ne soit accessible qu'au sein de la classe. La propriété ou la méthode n'est pas disponible depuis un autre composant ou service. 

Pour utiliser l'accessibilité privée, nous ajoutons le mot-clé `private` devant le nom de la variable.

```typescript
// Product Service
private productUrl = 'api/products';
```

Puisque nous modifions actuellement cette propriété dans le composant, le code du composant génère maintenant une erreur : `Property 'productUrl' is private and only accessible within class 'ProductService'`. Super ! Notre composant ne peut plus accéder à la propriété privée de notre service.

En ajoutant le mot-clé d'accessibilité privée de TypeScript devant une propriété dans le service, la variable n'est accessible que depuis ce service.

Mais, en revenant au composant, que se passe-t-il si nous essayons de faire quelque chose comme ceci :

```typescript
// Product Component
constructor() {
  for (let i in this.productService) {
    console.log('properties:', i);
  }

  this.productService.logUrl();
}
```

La boucle `for...in` itère sur les propriétés d'un objet. Dans cet exemple, nous affichons chaque propriété dans la console. Le résultat est montré dans la Figure 2 :

![Console log includes productUrl and products](https://www.freecodecamp.org/news/content/images/2023/06/image-192.png)
_Figure 2. Résultat de la sortie de la console_

Remarquez qu'il affiche à la fois nos propriétés publiques et privées. Maintenant que nous pouvons voir le nom de la propriété privée, nous pouvons l'utiliser pour mettre à jour cette propriété privée.

```typescript
// Product Component
constructor() {
  for (let i in this.productService) {
    console.log('properties:', i);
  }

  this.productService['productUrl']= 'api/nefarious';
  this.productService.logUrl();
}
```

Oups ! Nous avons à nouveau modifié notre propriété de service depuis notre composant. Notre propriété privée n'est pas si privée.

Pourquoi cela ? C'est parce que le mot-clé `private` fait partie de TypeScript, pas de JavaScript. Cela signifie que l'accessibilité privée n'est appliquée que pendant le développement, dans le cadre de la vérification de type, et pendant la compilation. Nous recevons des notifications pendant le développement et la compilation que nous ne pouvons pas accéder à la propriété privée depuis l'extérieur de sa classe.

Mais lorsque notre code TypeScript est transpilé en JavaScript et exécuté, le mot-clé private a disparu. Cela signifie que les constructions d'exécution JavaScript telles que notre boucle `for...in` ou une simple recherche de propriété, peuvent toujours accéder à une propriété ou une méthode définie avec le mot-clé `private`. En d'autres termes, le composant peut accéder aux propriétés privées de notre service à l'exécution. Oh là là !

## **Membres de classe privés de JavaScript (#)**

L'utilisation de la syntaxe `#` de JavaScript résout ce problème. Récemmment, JavaScript a ajouté des propriétés et méthodes de classe privées, désignées par un `#`. Puisque le `#` fait partie de JavaScript, il désigne nos propriétés et méthodes comme privées pendant le développement, la compilation et à l'exécution.

Dans le service Product, supprimons le mot-clé `private` et ajoutons `#`. Le `#` est un préfixe sur la variable elle-même, et devient partie du nom de la variable. Nous devons donc changer le nom de la variable partout où nous y accédons, comme dans notre méthode `logUrl`.

```typescript
// Product Service
@Injectable({
  providedIn: 'root'
})
export class ProductService {
  #productUrl = 'api/products';
  products = [];

  constructor() { 
    this.logUrl();
  }

  logUrl() {
    console.log('Url:',this.#productUrl);
  }
}
```

Nous voyons maintenant une erreur où nous accédons à la propriété dans le composant Product : `Property 'productUrl' does not exist on type 'ProductService'. Did you mean '#productUrl'?`

Nous pouvons essayer de changer notre code de recherche de propriété dans le composant pour inclure un `#` également.

```typescript
// Product Component
constructor() {
  for (let i in this.productService) {
    console.log('properties:', i);
  }

  this.productService['#productUrl']= 'api/nefarious';
  this.productService.logUrl();
}
```

Mais la propriété n'est toujours pas trouvée : `Property '#productUrl' does not exist on type 'ProductService'`. La propriété privée dans notre service est maintenant correctement masquée à notre composant. Nous devrons supprimer la ligne de recherche de propriété qui accède à `#productUrl` pour que notre code se compile avec succès.

En regardant la console (Figure 3), remarquez que notre boucle `for...in` trouve maintenant la propriété publique `products`, mais pas la propriété privée `productsUrl`. Notre propriété privée est privée et masquée, correctement encapsulée dans notre service.

![Console log includes products, not productUrl](https://www.freecodecamp.org/news/content/images/2023/06/image-193.png)
_Figure 3. Résultat de la sortie de la console_

## Conclusion

En tant que développeurs Angular, nous avons utilisé le mot-clé d'accessibilité `private` de TypeScript pour rendre les propriétés ou méthodes privées. Mais cela ne protège la propriété qu'au développement et à la compilation, pas à l'exécution.

Maintenant, nous pouvons utiliser la syntaxe des propriétés de classe privées de JavaScript (désignée par le symbole `#`) pour rendre les propriétés et méthodes privées vraiment privées et masquées aux autres parties de notre code.

Pour voir ces concepts en action, consultez la démonstration fournie dans cette vidéo :

%[https://youtu.be/487iCAnhxCM]