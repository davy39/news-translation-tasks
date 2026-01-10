---
title: Comment (et pourquoi) utiliser le Cake Pattern avec Swinject
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-22T07:01:01.000Z'
originalURL: https://freecodecamp.org/news/the-cake-pattern-with-swinject-4357c4d2bd0b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AhTCkEaoe0JVpI8zJAxSTg.png
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: Comment (et pourquoi) utiliser le Cake Pattern avec Swinject
seo_desc: 'By Peter-John Welcome

  In my previous article, I showed how we can use the Cake Pattern to do dependency
  injection without any libraries. I got a lot of awesome feedback from many people
  suggesting alternative methods, which indicates that there is lo...'
---

Par Peter-John Welcome

Dans mon [article précédent](https://medium.com/swift-programming/dependency-injection-with-the-cake-pattern-3cf87f9e97af), j'ai montré comment nous pouvons utiliser le Cake Pattern pour faire de l'injection de dépendances sans aucune bibliothèque. J'ai reçu beaucoup de retours géniaux de la part de nombreuses personnes suggérant des méthodes alternatives, ce qui indique qu'il y a beaucoup d'intérêt pour ce sujet.

L'une des questions qu'on m'a posées, et qui est très importante, était de savoir comment remplacer notre implémentation par un mock pour les tests.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o8JOg5rpHYKVQ5DfjCvvMA.png)

Dans les commentaires, j'ai fait quelques suggestions. L'une d'entre elles était d'utiliser un conteneur de dépendances.

[Swinject](https://github.com/Swinject/Swinject), qui est un framework, est l'un des frameworks d'injection de dépendances qui implémente un modèle de conteneur de dépendances.

Vous vous demandez peut-être : pourquoi aurions-nous besoin du cake pattern si nous pouvons simplement utiliser [Swinject](https://github.com/Swinject/Swinject) ? Ou pourquoi essayer de les utiliser ensemble ? Eh bien, cela dépend des préférences personnelles. Mais j'aimerais montrer comment nous pouvons utiliser ces deux ensemble.

### **Installation**

Pour utiliser [Swinject](https://github.com/Swinject/Swinject) dans notre projet, nous devons installer le pod.

```
pod 'Swinject'
```

Une fois notre pod installé, nous commencerons par créer deux protocoles. Le premier sera un protocole Registrable qui aura une méthode register prenant trois paramètres.

1. Dependency — il s'agit du type que nous enregistrons sur le conteneur.
2. Implementation — L'implémentation de la dépendance que nous voulons qu'il résolve.
3. ObjectScope — La portée dans laquelle nous voulons que cette dépendance vive. (Optionnel)

Notre deuxième protocole sera le protocole Resolvable qui aura deux méthodes. La première est une méthode resolve, qui prendra un type de dépendance et retournera une implémentation concrète de ce type. La seconde est une méthode reset qui réinitialisera le Resolvable pour nous (utile pour les tests).

Nous allons maintenant créer une classe de conteneur de dépendances qui se conformera à ces protocoles.

Nous allons créer un conteneur Swinject et une instance statique sur notre classe de conteneur de dépendances.

**Avertissement : Ce code est écrit en Swift 4, où private peut être utilisé dans les extensions (contrairement à Swift 3, où fileprivate était nécessaire).**

Tout d'abord, nous allons nous conformer au protocole Registrable et utiliser le conteneur Swinject que nous avons créé pour enregistrer nos dépendances avec leurs implémentations respectives. Nous spécifierons également l'objectScope comme étant graph par défaut.

Swinject fournit quatre portées intégrées différentes. Veuillez consulter le lien ci-dessous vers la documentation où cela est excellemment expliqué.

[**Swinject/Swinject**](https://github.com/Swinject/Swinject/blob/master/Documentation/ObjectScopes.md)  
[_Swinject - Dependency injection framework for Swift with iOS/macOS/Linux_github.com](https://github.com/Swinject/Swinject/blob/master/Documentation/ObjectScopes.md)

Ensuite, nous nous conformons au protocole Resolvable et utilisons à nouveau le même conteneur Swinject pour résoudre les dépendances. Nous réinitialiserons le conteneur dans la méthode reset en supprimant toutes les dépendances enregistrées sur le conteneur.

Nous avons maintenant un conteneur de dépendances — Hourra !! Mais comment utilisons-nous ce conteneur pour résoudre nos dépendances ?

Nous allons créer une usine Resolver qui s'en chargera pour nous. Elle aura d'abord une propriété container de type Resolvable, et celle-ci sera initialisée avec l'instance de la classe de conteneur de dépendances. Nous faisons en sorte que ce conteneur soit de type Resolvable afin que nous puissions le remplacer par toute instance de conteneur de dépendances qui se conforme à ce protocole.

Nous allons maintenant créer deux méthodes statiques qui résoudront et réinitialiseront notre conteneur lors de l'utilisation de notre conteneur Resolvable.

Nous avons créé cette usine Resolver, et maintenant il est temps de l'utiliser.

Lors de la création de notre extension de protocole (où nous résolvions notre implémentation dans l'article précédent), nous pouvons maintenant utiliser notre usine Resolver.

Nous devons également nous rappeler que nous devrons maintenant enregistrer notre dépendance sur notre conteneur.

Nous y voilà, nous avons le cake pattern avec Swinject comme notre conteneur de dépendances.

### **Avantages**

Les avantages de cette approche sont que nous découplons les composants de notre application et fournissons une source unique de résolution pour ces composants. Cela facilite également grandement le remplacement des implémentations par des mocks pour les tests.

Cela nous donne la possibilité de partager des composants n'importe où dans notre application, car nous pourrons résoudre toute dépendance à tout moment avec nos extensions de protocole injectables.

### **Tests unitaires**

Comment tester cela ? Eh bien, tout ce que nous avons à faire est d'appeler reset sur le Resolver, puis d'enregistrer les dépendances avec des implémentations mock.

Nous avons maintenant nos mocks qui sont injectés. On dirait que nous avons terminé.

Allez essayer ! Faites-moi savoir ce que vous en pensez.

Swinject est très puissant, et cet article ne démontre que ses fonctionnalités de base. Si vous souhaitez que j'explore davantage ses fonctionnalités, faites-le-moi savoir dans les commentaires ci-dessous.

Restez en contact !

Pour l'exemple complet, vous pouvez le trouver sur mon Github.

[**pjwelcome/CakePatternWithSwinject**](https://github.com/pjwelcome/CakePatternWithSwinject)  
[_CakePatternWithSwinject - Cake pattern with Swinject as a dependency container_github.com](https://github.com/pjwelcome/CakePatternWithSwinject)[**Peter-John (@pjapplez) | Twitter**](https://twitter.com/pjapplez)  
[_The latest Tweets from Peter-John (@pjapplez). Mobile App Developer, Technology Explorer, Photographer, Co-Founder…_twitter.com](https://twitter.com/pjapplez)

[**Peter John Welcome — Google+**](https://plus.google.com/u/0/+PeterJohnWelcome)

Merci à [Ashton Welcome](https://plus.google.com/111778165757216259863) et [Keegan Rush](https://medium.com/@RushKeegan) pour avoir révisé cet article.