---
title: Angular 6 et ses nouvelles fonctionnalités — expliquées en trois minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-16T15:11:00.000Z'
originalURL: https://freecodecamp.org/news/angular-what-is-the-new-briefly-e6837348dd3a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AdGD1-LO1avzx5hNJFQoZQ.png
tags:
- name: Angular
  slug: angular
- name: angular6
  slug: angular6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Angular 6 et ses nouvelles fonctionnalités — expliquées en trois minutes
seo_desc: 'By Said Hayani

  Angular has come out with some amazing new features in version 6.0.0, especially
  in Angular-cli. Now, with Angular 6, you can easily update your old packages, create
  native web elements using Angular Elements, and many other things. Le...'
---

Par Said Hayani

[Angular](https://angular.io) est sorti avec des fonctionnalités incroyables dans la [version 6.0.0](https://angular.io/), surtout dans Angular-cli. Maintenant, avec Angular 6, vous pouvez facilement mettre à jour vos anciens packages, créer des éléments web natifs en utilisant Angular Elements, et bien d'autres choses. Regardons cela !

### ng add

![Image](https://cdn-media-1.freecodecamp.org/images/1*u8BWLIWdkabEzp0QSmMUgg.png)

`**ng add**` est une nouvelle commande dans Angular-cli qui vous aide à installer et télécharger de nouveaux packages dans vos applications Angular. Elle fonctionne de la même manière que npm, mais ne le remplace pas.

### ng update

![Image](https://cdn-media-1.freecodecamp.org/images/1*mxQPMNmblN_8t_ky1r5G8w.png)

`**ng update**` est également une nouvelle commande Angular-cli. Elle est utilisée pour mettre à jour et améliorer vos packages. Elle est vraiment utile, par exemple, lorsque vous souhaitez passer d'Angular 5 à Angular 6, ou pour tout autre package dans votre application Angular.

### Déclarer les providers à l'intérieur du service lui-même

Avant cette mise à jour, vous deviez déclarer le tableau des providers dans `**app.module.ts**`

Maintenant, avec Angular 6, vous pouvez fournir votre service à l'intérieur du superviseur lui-même en mettant la propriété `**providedIn:root**` dans le décorateur "`**@injectable"**`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3Huej4et-8LIfrAEhzY3pQ.png)

### Utiliser ng-template au lieu de la directive template

Vous pouvez utiliser `**ng-template**` pour rendre le HTML au lieu de la balise `**template**` dans la nouvelle version d'Angular. `**ng-template**` est un élément Angular, et il fonctionne lorsqu'il est utilisé avec une [directive structurelle](https://angular.io/guide/structural-directives) telle que `***ngFor**` et `***ngIf**`

![Image](https://cdn-media-1.freecodecamp.org/images/1*6RjvjuP6weX0bPrYBbjQ8Q.png)

### Angular Elements

Angular 6 nous a présenté Angular Elements. Vous êtes en mesure de rendre vos éléments Angular en tant qu'éléments web natifs, et ils sont interprétés comme des éléments HTML de confiance.

Vous pouvez ajouter des éléments Angular en exécutant la commande suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*u8BWLIWdkabEzp0QSmMUgg.png)

Importez `**createCustomElement**` dans votre composant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YP2ej1AXVAO9GURmbGnFcQ.png)

Puis créez votre élément personnalisé !

![Image](https://cdn-media-1.freecodecamp.org/images/1*F1WAYYCRzJSyfr8PSWsMRg.png)

`**MyElemComponent.ts**`

![Image](https://cdn-media-1.freecodecamp.org/images/1*S4Ib01DNgO67jh_-habKmQ.png)

Le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lgl-OcKiFKVLF7A9KdrImA.png)

**Note :** vous devez implémenter la méthode `**DomSanitizer**` depuis `@angular/platform-browser` pour faire de votre élément personnalisé une balise HTML de confiance.

Vous pouvez en apprendre plus sur les éléments Angular [ici](https://angular.io/guide/elements)

### Mise à jour vers RxJS 6.0.0

Angular 6 utilise la dernière version de la bibliothèque RxJS. Maintenant, vous pouvez profiter des nouvelles fonctionnalités de RxJS 6 dans votre application Angular :)

### Conclusion

Angular lui-même n'a pas beaucoup de changements révolutionnaires dans le cœur d'Angular, mais Angular-cli est vraiment excitant. L'équipe Angular se concentre davantage sur la performance, la création facile de PWAs, et la fourniture d'un bon environnement pour travailler avec Angular de manière simple.

Vous pouvez me trouver sur [Twitter](https://twitter.com/SaidHYN).



> Au fait, j'ai récemment travaillé avec un groupe solide d'ingénieurs logiciels pour l'une de mes applications mobiles. L'organisation était excellente, et le produit a été livré très rapidement, beaucoup plus vite que d'autres entreprises et freelancers avec lesquels j'ai travaillé, et je pense que je peux honnêtement les recommander pour d'autres projets. Envoyez-moi un email si vous souhaitez entrer en contact — [said@devsdata.com](mailto:said@devsdata.com).