---
title: Mises à jour Angular qui amélioreront votre expérience de développeur
subtitle: ''
author: Brenda Chepkorir
co_authors: []
series: null
date: '2023-05-17T23:40:59.000Z'
originalURL: https://freecodecamp.org/news/angular-upgrades-to-improve-developer-experience
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-thisisengineering-3861958.jpg
tags:
- name: Angular
  slug: angular
seo_title: Mises à jour Angular qui amélioreront votre expérience de développeur
seo_desc: "When we talk about the Developer Experience, we're referring to the level\
  \ of difficulty a developer faces when completing essential tasks. \nFactors like\
  \ the complexity of a development framework or the absence of syntactic sugar in\
  \ a programming lang..."
---

Lorsque nous parlons de l'[Expérience Développeur](https://microsoft.github.io/code-with-engineering-playbook/developer-experience/), nous faisons référence au niveau de difficulté qu'un développeur rencontre lors de l'exécution de tâches essentielles. 

Des facteurs comme la complexité d'un framework de développement ou l'absence de [sucre syntaxique](https://www.techopedia.com/definition/10212/syntactic-sugar) dans un langage de programmation peuvent l'impacter négativement.

Un framework moderne robuste peut être complexe. Mais Angular ne serait pas si apprécié s'il ne devenait pas plus facile à utiliser avec chaque nouvelle version. 

Les versions 14, 15 et 16 comportent de nombreuses améliorations que vous ne connaissez peut-être pas et que vous pourriez vouloir utiliser lors de la migration d'une version à l'autre. 

Ces améliorations incluent :

* des messages d'erreur concis et tree-shakable
* de la magie automatique dans les templates
* des inputs requis
* le titre de page dans les options de route
* des données de route liées aux composants
* la complétion CLI

Examinons chacune de ces fonctionnalités plus en détail afin que vous puissiez les utiliser dans vos applications Angular.

## Messages d'erreur [Tree-Shakable](https://developer.mozilla.org/en-US/docs/Glossary/Tree_shaking) concis

Le tree-shaking élimine principalement le code inutilisé d'un bundle. Dans ce cas, il fait référence à la suppression des messages d'erreur d'exécution en production. 

Les messages et codes d'erreur d'exécution dans Angular ne sont pas nouveaux. Ce qui est nouveau, ce sont les messages d'erreur de production moins verbeux. 

Dans la version 14, au lieu de longs messages, vous obtenez leurs codes d'erreur associés. Et vous pouvez rapidement rechercher ces codes dans la [documentation Angular](https://angular.io/errors) pour le débogage. Vous pouvez consulter les messages détaillés plus longs en développement pour un débogage plus approfondi.

## [Template](https://angular.io/guide/template-syntax) Auto-Magique

Dans la version 16, les balises auto-fermantes des templates aident les développeurs à éviter d'ajouter des balises de fermeture aux sélecteurs de composants dans les templates. Cela est similaire à l'élément HTML `input` omniprésent qui n'a pas besoin de balise de fermeture. Par exemple : 

```html
<!--Avant-->

<app-root></app-root>

<!--Après-->

<app-root />
```

De plus, les mises à jour du service de langage Angular dans la version 16 permettent les imports automatiques de pipes et de composants autonomes dans les templates. Comme les imports automatiques de classes dans les composants. La plupart des éditeurs de code, comme VS Code, [utilisent les services de langage](https://code.visualstudio.com/docs/editor/intellisense#_intellisense-features) pour supporter les imports automatiques via des _corrections rapides_.

En outre, la version 14 a introduit une option supplémentaire de compilation de template, [une configuration TypeScript](https://angular.io/guide/angular-compiler-options), appelée `[extendedDiagnostics](https://angular.io/extended-diagnostics)` pour compléter les insights des templates. Cette configuration aide le compilateur à trouver les pièges courants des templates comme une chaîne optionnelle lorsqu'une valeur ne sera jamais `null`. Si elle est `null`, c'est soit un bug, soit une valeur mal typée. 

Ces types d'erreurs de syntaxe sont généralement plus difficiles à repérer car elles ne cassent pas toujours l'application.

## [Inputs](https://angular.io/api/core/Input) requis

Les inputs dans Angular sont vitaux pour le partage de données des composants parents aux composants enfants. Ils spécifient quelles valeurs sont passées à l'enfant. La version 16 a introduit des [inputs requis](https://angular.io/api/core/Input#required) pour aider les développeurs à se souvenir de passer ces données lors de l'utilisation de composants enfants. 

Les données manquantes assignées à des inputs requis déclencheront des erreurs de compilation.

```typescript
export class ChildComponent {
	@Input({ required: true }) someList: unknown[];
}
```

```html
<!--Dans le template parent-->

<child-one  /> <!--déclenche une erreur de compilation-->

<child-one [someList]="list" /> <!--pas d'erreur de compilation-->
```

Peut-être que de futures mises à jour des inputs requis aideront à retarder le rendu des composants enfants tant que les données sont encore `falsy`. 

## Titre de page dans les options de route

Les titres de page sont importants. Encore plus pour l'[Arbre d'Accessibilité](https://web.dev/the-accessibility-tree/). Vous pouvez les voir dans les onglets du navigateur des pages, comme les titres. L'Arbre d'Accessibilité est le [DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction) que les outils d'accessibilité, comme les lecteurs d'écran, utilisent pour naviguer à travers la page web.

Les titres de page résument le contenu pour les utilisateurs, ce qui est utile pour la navigation. Il peut être facile d'oublier de les définir, surtout si les définir semble un peu contre-intuitif en développement.

La version 14 a introduit une option `title` à l'interface `[Route](https://angular.io/api/router/Route)` que vous pouvez utiliser pour configurer les routes de l'application. Cela permet à chaque route de définir son propre titre de page. De plus, cette option peut être configurée comme une `string` ou une fonction qui résout une chaîne pour des titres plus dynamiques.

```typescript
const appRoutes: Route[] = [
{
    path: '/customers',
    component: CustomersComponent,
    title: 'Customers',
    children: [{
    	path: ':id/customer',
    	component: CustomerComponent,
        title: (route: ActivatedRouteSnapshot, state: 	RouterStateSnapshot) => this.getRouteTitleForCustomer()
  	}]
}
];
```

## Données de route liées aux composants

Bien que les inputs aient toujours été utilisés pour le partage de données entre les composants dans les relations parent-enfant, vous pouvez également les utiliser pour le partage de données entre les composants routés dans la version 16.

Certains scénarios de routage d'application nécessitent de passer des données, comme des IDs, aux composants vers lesquels on route. Cela était possible grâce à l'utilisation de la classe injectable `[ActivatedRoute](https://angular.io/api/router/ActivatedRoute)` dans les composants ayant besoin des données.

Les développeurs peuvent maintenant obtenir ces données via les inputs des composants, qu'elles proviennent des résolveurs de route ou des paramètres de chemin et de requête. Ces valeurs de données sont liées aux inputs des composants avec des noms correspondants. Ainsi, une valeur de donnée `customerId` de la route correspondra à un input `customerId` dans le composant. 

```typescript
export class CustomerComponent {
	@Input() customerId: string;
}

```

```typescript
const appRoutes: Route[] = [
{
    path: '/customers',
    component: CustomersComponent,
    title: 'Customers',
    children: [{
    	path: ':id/customer',
    	component: CustomerComponent,
        title: 'Customer',
        resolve: { customerId: (route: ActivatedRouteSnapshot, state: 	RouterStateSnapshot) => this.getCustomerId()
  		}
  	}]
}
];
```

Assurez-vous d'[activer la liaison de composant via le routeur](https://angular.io/guide/router#getting-route-information).

## [Complétion CLI](https://angular.io/cli/completion)

Pour les codeurs [impératifs](https://dev.to/ruizb/declarative-vs-imperative-4a7l) et les amateurs de terminal, la version 14 a apporté la complétion automatique des commandes via `ng completion`. Cela permet aux développeurs d'obtenir des références intuitives rapides pour les commandes et leurs options applicables avec une pression sur la touche `tab` dans le terminal. Cela rend l'utilisation de la CLI plus facile et plus rapide.

## Conclusion

Les dernières versions d'Angular 14, 15 et 16 contiennent de nombreuses autres modifications demandées qui non seulement améliorent l'Expérience Développeur, mais traitent également de nombreux problèmes de framework. 

Le [Blog Angular](https://blog.angular.io/) et la [documentation](https://angular.io/docs) fournissent plus de détails sur toutes ces modifications avec des exemples spécifiques.