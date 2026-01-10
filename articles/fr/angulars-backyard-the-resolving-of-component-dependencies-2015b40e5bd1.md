---
title: 'L''arrière-cour d''Angular : La résolution des dépendances des composants'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-28T15:13:46.000Z'
originalURL: https://freecodecamp.org/news/angulars-backyard-the-resolving-of-component-dependencies-2015b40e5bd1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xym6BYUMOQmtTv-Pmbs4mQ.jpeg
tags:
- name: Angular
  slug: angular
- name: angular2
  slug: angular2
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: 'L''arrière-cour d''Angular : La résolution des dépendances des composants'
seo_desc: 'By Dor Moshe

  This article originally appeared on dormoshe.io

  Many of us use the Hierarchical Dependency Injection mechanism of Angular. We use
  it through a service or a component to resolve another service or provider. But,
  do we know what Angular do...'
---

Par Dor Moshe

**_Cet_ article** **_a initialement été publié sur [dormoshe.io](https://dormoshe.io/articles/angulars-backyard-the-resolving-of-components-dependencies-10)_**

Beaucoup d'entre nous utilisent le mécanisme d'Injection de Dépendances Hiérarchique d'Angular. Nous l'utilisons via un service ou un composant pour résoudre un autre service ou fournisseur. Mais, savons-nous ce qu'Angular fait pour résoudre les dépendances ? Probablement pas, car Angular s'occupe de ce dont nous avons besoin pour l'utiliser comme une boîte noire.

Dans cet article, nous allons ouvrir la boîte noire et explorer le code du mécanisme de résolution des dépendances des composants.

### Retour aux bases

L'[Injection de Dépendances](https://blog.thoughtram.io/angular/2015/05/18/dependency-injection-in-angular-2.html) (DI) est un puissant modèle pour gérer les dépendances de code. Le système DI d'Angular **crée et fournit des services dépendants** « juste à temps ». Angular a son propre framework DI, et nous ne pouvons pas construire une application Angular sans lui.

Le système DI d'Angular est en fait un système **Hiérarchique**. Ce système supporte des injecteurs imbriqués en parallèle avec l'arbre des composants. Un injecteur crée des dépendances en utilisant des fournisseurs. Nous pouvons reconfigurer les injecteurs à n'importe quel niveau de cet arbre de composants. En coulisses, chaque composant configure son **propre injecteur** avec zéro, un ou plusieurs fournisseurs définis pour ce composant lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MFEIRh2SxIjlubhqwbhVow.png)
_Un mini arbre d'injecteurs Angular_

### Ordre de résolution

Le DI hiérarchique a un ordre pour la résolution des dépendances. Lorsqu'un composant demande une dépendance, si elle existe dans le tableau `@Component.providers` (l'injecteur du composant), alors cette dépendance sera fournie.

Ailleurs, Angular continue vers l'injecteur du composant parent et vérifie à nouveau. Si Angular ne trouve pas d'ancêtre, il fournira cette dépendance via l'injecteur principal de l'application. C'est le concept central du mécanisme DI hiérarchique.

### Examinons le code

Lorsque Angular instancie un composant, il appelle la fonction `resolveDep`. La signature de cette fonction contient le conteneur de vue du composant, l'élément, la définition de la dépendance et quelques autres arguments. Nous nous concentrerons sur la vue du composant et l'objet de dépendance. L'objet de dépendance contient seulement une dépendance du composant.

Voici le squelette de la fonction `resolveDep` du dépôt GitHub d'Angular :

Le squelette de la fonction contient les concepts principaux de la résolution, sans les cas particuliers. Le code complet peut être trouvé [ici](https://github.com/angular/angular/blob/master/packages/core/src/view/provider.ts#L343). Dans les parties suivantes, nous explorerons le squelette de la fonction.

#### Pause

Le point d'exclamation est une nouvelle fonctionnalité de TypeScript 2.0. L'opérateur post-fixe `!` peut être utilisé pour affirmer que son opérande n'est ni nul ni indéfini dans des contextes où le vérificateur de type est incapable de conclure ce fait. Angular utilise fréquemment cette fonctionnalité, donc nous ne devrions pas en avoir peur.

#### Partie 1 — Préparation

Le code `const startView = view;` sauvegarde la vue originale (le conteneur de vue du composant) dans une variable car la variable de vue va bientôt changer.

Le code `const tokenKey = depDef.tokenKey;` récupère le **tokenKey** ou la clé de dépendance, par exemple, **HeroService_4**. Cette clé est construite par le nom de la dépendance et un nombre généré pour gérer la dépendance de manière unique.

#### Partie 2 — Recherche du composant source et des ancêtres

La boucle **while** implémente les étapes de vérification des `@Component.providers` sources et des composants ancêtres. Selon la clé de token de dépendance, les fournisseurs du composant source seront vérifiés aux lignes 1–3 :

Si le fournisseur existe à la ligne 4, alors le composant source satisfait la dépendance. Donc, si la dépendance a été instanciée dans le passé à la ligne 6, l'instance sera retournée par la fonction `resolveDep` à la ligne 10. Si c'est la première fois que le composant ou ses enfants demandent la dépendance, elle sera créée à la ligne 7 et sera retournée par la fonction `resolveDep` à la ligne 10.

Si la dépendance n'est pas trouvée dans l'injecteur du composant `view`, alors
`elDef = viewParentEl(view) !;` et `view = view.parent !;` seront appelés pour faire avancer la variable vers l'élément parent. La boucle `while` continuera à s'exécuter jusqu'à ce que la dépendance soit trouvée dans l'injecteur de l'ancêtre. Si la dépendance n'est toujours pas trouvée après avoir vérifié tous les ancêtres, la boucle `while` se terminera et la **troisième partie** entrera en action.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V2ffKO6UpnymY99JXBSCEw.jpeg)

#### Partie 3 — Injecteur racine

Si nous arrivons à cette partie, la dépendance ne peut pas être satisfaite par l'un des injecteurs des composants ancêtres. Ensuite, la `startView` ou le composant source sera vérifié à la ligne 1 :

Si le composant source ou l'un de ses composants ancêtres a été chargé par le Router Outlet (le composant routeur), l'injecteur **racine** est l'**Outlet Injector**. Cet injecteur fournit certaines dépendances comme le service **Router**. Sinon, l'injecteur racine est l'injecteur du composant de bootstrap.

Si la dépendance est trouvée à la ligne 3, alors la valeur sera retournée par la fonction `resolveDep`. Dans l'autre cas, la partie 4 entrera en action.

#### Partie 4 — Injecteur du module d'application

Lorsque nous arrivons à cette partie, cela signifie que la dépendance ne peut pas être satisfaite par les parties 2 et 3. C'est la dernière chance de satisfaire la dépendance. Le code de cette partie tente d'obtenir la dépendance à partir de l'injecteur du module d'application ou du module racine. Ce module contient les dépendances à l'échelle de l'application :
`return startView.root.ngModule.injector.get(depDef.token, notFoundValue);`

Cette partie termine le flux `resolveDep`. Si la dépendance n'est pas trouvée, alors Angular ne peut pas satisfaire cette dépendance et doit lever une exception.

### Conclusion

Le DI hiérarchique est une fonctionnalité centrale sur laquelle Angular s'appuie beaucoup. Parfois, le processus de résolution semble compliqué et long. Il est très pratique de laisser Angular gérer ce flux et de profiter de la facilité d'utilisation. Maintenant, après avoir exploré l'arrière-cour de la résolution des dépendances des composants, nous savons à quoi nous attendre lorsque nous l'utilisons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cA1Y2VmIvRnUJUvjUPNZ2A.png)

**_Vous pouvez me suivre sur [dormoshe.io](https://www.dormoshe.io) ou [Twitter](https://twitter.com/DorMoshe) pour lire plus d'articles sur Angular, JavaScript et le développement web._**