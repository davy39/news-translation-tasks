---
title: 'Angular 2 versus React : Il y aura du sang'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-01-03T20:49:44.000Z'
originalURL: https://freecodecamp.org/news/angular-2-versus-react-there-will-be-blood-66595faafd51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MRPl_SNuRGJchb6eOAnkSA.jpeg
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: 'Angular 2 versus React : Il y aura du sang'
seo_desc: 'By Cory House

  Angular 2 has reached Beta and appears poised to become the hot new framework of
  2016. It’s time for a showdown. Let’s see how it stacks up against 2015’s darling:
  React.

  Disclaimer: I enjoyed working in Angular 1 but switched to React ...'
---

Par Cory House

[Angular 2 a atteint la version Bêta](https://angular.io) et semble prêt à devenir le nouveau framework à la mode de 2016. Il est temps pour un affrontement. Voyons comment il se mesure face au chouchou de 2015 : [React](https://facebook.github.io/react/).

**Avertissement :** J'ai apprécié travailler avec Angular 1 mais je suis passé à React en 2015. J'ai publié des cours Pluralsight sur [React et Flux](https://www.pluralsight.com/courses/react-flux-building-applications) et [React et Redux en ES6](https://app.pluralsight.com/library/courses/react-flux-building-applications) ([essai gratuit](http://app.pluralsight.com/signup)). Donc **oui, je suis partial. Mais je critique les deux côtés.**

Très bien, commençons. Il y aura du sang.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MRPl_SNuRGJchb6eOAnkSA.jpeg)
_Crédit photo : [@jwcarrol](https://twitter.com/jwcarroll" rel="noopener" target="_blank" title=")_

### Vous comparez des pommes et des orangs-outans !

Soupir. Oui, Angular est un framework, React est une bibliothèque. Certains disent que cette différence rend leur comparaison illogique. Pas du tout !

> Choisir entre Angular et React, c'est comme choisir entre acheter un ordinateur prêt à l'emploi et en construire un soi-même avec des pièces détachées.

Cet article examine les mérites de ces deux approches. Je compare la syntaxe et le modèle de composants de React à ceux d'Angular. C'est comme comparer le CPU d'un ordinateur prêt à l'emploi à un CPU brut. Des pommes avec des pommes.

### Avantages d'Angular 2

Commençons par examiner les avantages d'Angular 2 par rapport à React.

#### **Faible fatigue décisionnelle**

Puisqu'Angular est un framework, il fournit significativement plus d'opinions et de fonctionnalités dès la sortie de la boîte. Avec React, vous devez généralement sélectionner un certain nombre d'autres bibliothèques pour construire une vraie application. Vous voudrez probablement des bibliothèques pour le routage, l'application de flux unidirectionnels, les appels d'API web, les tests, la gestion des dépendances, et ainsi de suite. Le nombre de décisions est assez écrasant. C'est pourquoi React a tant de kits de démarrage (j'en ai [publié](https://github.com/coryhouse/react-flux-starter-kit) [deux](https://github.com/coryhouse/react-slingshot)).

Angular offre plus d'opinions dès la sortie de la boîte, ce qui vous aide à démarrer plus rapidement sans être intimidé par les décisions. Cette cohérence imposée aide également les nouvelles recrues à se sentir plus rapidement à l'aise et rend le passage des développeurs entre les équipes plus pratique.

J'admire la manière dont l'équipe principale d'Angular a adopté TypeScript, ce qui conduit à l'avantage suivant...

#### TypeScript = Chemin clair

Certes, TypeScript n'est pas aimé de tous, mais l'approche opinionnée d'Angular 2 sur la saveur de JavaScript à utiliser est une grande victoire. Les exemples React sur le web sont frustrants d'incohérence — il est présenté en ES5 et ES6 en nombres à peu près égaux, et il offre actuellement [trois façons différentes de déclarer des composants](http://jamesknelson.com/should-i-use-react-createclass-es6-classes-or-stateless-functional-components/). Cela crée de la confusion pour les nouveaux venus. (Angular adopte également les décorateurs au lieu de extends — beaucoup considéreraient cela comme un plus également).

Bien qu'Angular 2 n'exige pas TypeScript, l'équipe principale d'Angular l'embrasse certainement et utilise par défaut TypeScript dans la documentation. Cela signifie que les exemples connexes et les projets open source sont plus susceptibles de sembler familiers et cohérents. Angular fournit déjà [des exemples clairs qui montrent comment utiliser le compilateur TypeScript](https://angular.io/docs/ts/latest/quickstart.html). (bien que, admettons-le, [tout le monde n'embrasse pas encore TypeScript](http://angularjs.blogspot.com/2015/09/angular-2-survey-results.html), mais je soupçonne que peu après le lancement, il deviendra la norme de facto). Cette cohérence devrait aider à éviter la confusion et la surcharge décisionnelle qui accompagnent le démarrage avec React.

#### Réduction du churn

2015 a été l'année de la [fatigue JavaScript](https://medium.com/@ericclemmons/javascript-fatigue-48d4011b6fc4#.559iqxb39). Bien que React lui-même soit attendu pour être assez stable avec [la version 15 à venir](https://facebook.github.io/react/blog/), l'écosystème de React a connu un churn à un rythme rapide, en particulier autour de la [longue liste de saveurs Flux](https://github.com/kriasoft/react-starter-kit/issues/22) et du [routage](https://github.com/rackt/react-router). Donc tout ce que vous écrivez dans React aujourd'hui peut sembler obsolète ou nécessiter des changements majeurs à l'avenir si vous vous appuyez sur l'une des nombreuses bibliothèques connexes.

En revanche, Angular 2 est une réinvention minutieuse et méthodique d'un framework mature et complet. Ainsi, Angular est moins susceptible de connaître un churn douloureux après sa sortie. Et en tant que framework complet, lorsque vous choisissez Angular, vous pouvez faire confiance à une seule équipe pour prendre des décisions prudentes concernant l'avenir. Avec React, c'est à vous de rassembler un ensemble de bibliothèques open-source disparates et en rapide évolution en un tout cohérent qui fonctionne bien ensemble. C'est chronophage, frustrant et un travail sans fin.

#### **Large support d'outils**

Comme vous le verrez ci-dessous, je considère le JSX de React comme une grande victoire. Cependant, vous devez sélectionner des outils qui supportent le JSX. React est devenu si populaire que le support d'outils est rarement un problème aujourd'hui, mais les nouveaux outils tels que les IDE et les linters sont peu susceptibles de supporter le JSX dès le premier jour. Les templates d'Angular 2 stockent le balisage dans une chaîne ou dans des fichiers HTML séparés, donc il n'a pas besoin de support d'outils spécial (bien qu'il semble que des outils pour analyser intelligemment les templates de chaînes d'Angular soient en route).

#### Compatible avec les Web Components

La conception d'Angular 2 embrasse la norme des web components. Minus, je suis embarrassé d'avoir oublié de mentionner cela initialement — j'ai récemment publié un [cours sur les web components](https://www.pluralsight.com/courses/web-components-shadow-dom)! En bref, les composants que vous construisez dans Angular 2 devraient être beaucoup plus faciles à convertir en web components natifs que les composants de React. Certes, [le support des navigateurs est encore faible](http://jonrimmer.github.io/are-we-componentized-yet/), mais cela pourrait être une grande victoire à long terme.

L'approche d'Angular vient avec son propre ensemble de pièges, ce qui est une bonne transition pour discuter des avantages de React...

### Avantages de React

Très bien, considérons ce qui distingue React.

#### **JSX**

JSX est une syntaxe similaire à HTML qui se compile en JavaScript. Le balisage et le code sont composés dans le même fichier. Cela signifie que la complétion de code vous aide lorsque vous tapez des références aux fonctions et variables de votre composant. En revanche, les templates basés sur des chaînes d'Angular viennent avec les inconvénients habituels : pas de coloration de code dans de nombreux éditeurs, support limité de complétion de code, et des échecs à l'exécution. Vous vous attendriez normalement à des messages d'erreur médiocres également, mais l'équipe Angular [a créé son propre analyseur HTML pour corriger cela](https://github.com/angular/angular/issues/4417). (Bravo!)

Si vous n'aimez pas les templates basés sur des chaînes d'Angular, vous pouvez déplacer les templates vers un fichier séparé, mais alors vous revenez à ce que j'appelle « les vieux jours » : relier les deux fichiers dans votre tête, sans support de complétion de code ou vérification à la compilation pour vous aider. Cela ne semble pas être un gros problème jusqu'à ce que vous ayez profité de la vie dans React. Composer des composants dans un seul fichier **vérifié à la compilation** est l'une des grandes raisons pour lesquelles JSX est si spécial.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ivDnyMP63YJBBGKCNyRUzQ.png)
_Contraste de la manière dont Angular 2 et React gèrent une balise de fermeture manquante_

Pour plus d'informations sur pourquoi JSX est une si grande victoire, voir [JSX : L'autre côté de la pièce](https://medium.com/@housecor/react-s-jsx-the-other-side-of-the-coin-2ace7ab62b98#.5007n49wq).

#### **React échoue rapidement et explicitement**

Lorsque vous faites une faute de frappe dans le JSX de React, il ne se compile pas. C'est une belle chose. Cela signifie que vous savez immédiatement exactement quelle ligne contient une erreur. Il vous indique immédiatement lorsque vous oubliez de fermer une balise ou de référencer une propriété qui n'existe pas. En fait, **le compilateur JSX spécifie le numéro de ligne où la faute de frappe s'est produite**. Ce comportement accélère radicalement le développement.

En revanche, lorsque vous faites une faute de frappe dans une référence de variable dans Angular 2, rien ne se passe du tout. **Angular 2 échoue silencieusement à l'exécution au lieu de la compilation**. Il échoue _lentement_. Je charge l'application et me demande pourquoi mes données ne s'affichent pas. Pas amusant.

#### **React est centré sur JavaScript**

Voici. C'est la différence fondamentale entre React et Angular. **Malheureusement, Angular 2 reste centré sur HTML plutôt que sur JavaScript**. Angular 2 n'a pas résolu son problème de conception le plus fondamental :

> Angular 2 continue à mettre du « JS » dans le HTML. React met du « HTML » dans le JS.

Je ne peux pas assez insister sur l'impact de ce schisme. Il affecte fondamentalement l'expérience de développement. La conception centrée sur HTML d'Angular reste sa plus grande faiblesse. Comme je le couvre dans « [JSX : L'autre côté de la pièce](https://medium.com/@housecor/react-s-jsx-the-other-side-of-the-coin-2ace7ab62b98#.jqh5kkxlk) », JavaScript est bien plus puissant que HTML. Ainsi, **il est plus logique d'améliorer JavaScript pour supporter le balisage que d'améliorer HTML pour supporter la logique**. HTML et JavaScript doivent être collés ensemble d'une manière ou d'une autre, et l'approche centrée sur JavaScript de React est fondamentalement supérieure à celle centrée sur HTML d'Angular, Ember et Knockout.

Voici pourquoi...

#### La conception centrée sur JavaScript de React = simplicité

Angular 2 continue l'approche d'Angular 1 qui consiste à essayer de rendre HTML plus puissant. Vous devez donc utiliser la syntaxe unique d'Angular 2 pour des tâches simples comme les boucles et les conditionnelles. Par exemple, Angular 2 offre à la fois une liaison unidirectionnelle et bidirectionnelle via deux syntaxes qui sont malheureusement assez différentes :

```js
{{myVar}} // Liaison unidirectionnelle
ngModel="myVar" // Liaison bidirectionnelle
```

Dans React, la liaison du balisage ne change pas en fonction de cette décision (elle est gérée ailleurs, comme je l'argumenterais). Dans tous les cas, cela ressemble à ceci :

```js
{myVar}
```

Angular 2 supporte les templates maîtres en ligne en utilisant cette syntaxe :

```js
<ul>
  <li *ngFor="#hero of heroes">
    {{hero.name}}
  </li>
</ul>
```

Le snippet ci-dessus boucle sur un tableau de héros. J'ai plusieurs préoccupations :

* Déclarer un « template maître » via un astérisque précédent est cryptique.
* Le signe dièse devant hero déclare une variable de template locale. Ce concept clé ressemble à du bruit inutile (si vous préférez, vous pouvez utiliser `var`).
* Le ngFor ajoute une sémantique de boucle au HTML via un attribut spécifique à Angular.

Contrastez la syntaxe d'Angular 2 ci-dessus avec le JS pur de React* : (admettons que la propriété key ci-dessous est spécifique à React)

```js
<ul>
  { heroes.map(hero =>
    <li key={hero.id}>{hero.name}</li>
  )}
</ul>
```

Puisque JS supporte les boucles nativement, le JSX de React peut simplement tirer parti de toute la puissance de JS pour de telles choses et faire beaucoup plus avec map, filter, etc.

Lisez simplement la [Feuille de triche Angular 2](https://angular.io/docs/ts/latest/guide/cheatsheet.html). Ce n'est pas du HTML. Ce n'est pas du JavaScript. C'est **_Angular_**.

> **Pour lire Angular :** Apprenez une longue liste de syntaxe spécifique à Angular.  
>   
> Pour lire React : Apprenez JavaScript.

React est unique dans sa simplicité syntaxique et conceptuelle. Considérez l'itération dans les frameworks/bibliothèques JS populaires d'aujourd'hui :

```
Ember: {{# each}}
Angular 1: ng-repeat
Angular 2: ngFor
Knockout: data-bind="foreach"
React: UTILISEZ SIMPLEMENT JS. :)
```

Tous sauf React utilisent des remplacements spécifiques au framework pour quelque chose qui est natif et trivial en JavaScript : **une boucle**. C'est la beauté de React. Il embrasse la puissance de JavaScript pour gérer le balisage, donc aucune syntaxe étrange n'est requise.

Les bizarreries syntaxiques d'Angular 2 continuent avec la liaison de clic :

```js
(click)=onSelect(hero)"
```

En revanche, React utilise à nouveau du JavaScript classique :

```js
onClick={this.onSelect.bind(this, hero)}
```

Et puisque React inclut un système d'événements synthétique (comme Angular 2), vous n'avez pas à vous soucier des implications de performance de la déclaration de gestionnaires d'événements en ligne comme ceci.

Pourquoi remplir votre tête avec une syntaxe unique de framework si vous n'avez pas à le faire ? Pourquoi ne pas simplement embrasser la puissance de JS ?

#### Expérience de développement luxueuse

Le support de complétion de code de JSX, les vérifications à la compilation et les messages d'erreur riches créent déjà une excellente expérience de développement qui économise à la fois la frappe et le temps. Mais combinez tout cela avec le rechargement à chaud avec voyage dans le temps et vous avez une expérience de développement rapide comme aucune autre.

%[https://www.youtube.com/watch?v=xsSnOQynTHs]

#### Préoccupations concernant la taille

Voici les tailles de certains frameworks et bibliothèques populaires, minifiés ([source](https://gist.github.com/Restuta/cda69e50a853aa64912d)) :

**Angular 2 :** 566k (766k avec RxJS)  
**Ember :** 435k  
**[Angular 1](https://ajax.googleapis.com/ajax/libs/angularjs/1.4.8/angular.min.js) :** 143k  
**React + Redux :** 139k

**Modification :** Désolé, j'avais des chiffres incorrects plus tôt qui étaient pour des applications ToDoMVC simples au lieu des frameworks bruts. De plus, le chiffre d'Angular 2 devrait baisser pour la version finale. Les tailles listées sont pour le framework, minifiées, dans le navigateur (aucun gzip n'est pris en compte ici).

Pour faire une comparaison réelle, j'ai construit l'application Tour des Héros d'Angular 2 à la fois en Angular 2 et en React (j'ai utilisé le nouveau [kit de démarrage React Slingshot](https://github.com/coryhouse/react-slingshot)). Le résultat ?

[**Angular 2**](https://github.com/coryhouse/angular-2-tour-of-heroes/tree/master)**:** 764k minifiés  
[**React + Redux**](https://github.com/coryhouse/react-tour-of-heroes)**:** 151k minifiés

Ainsi, **Angular 2 est actuellement plus de quatre fois la taille d'une application React + Redux de simplicité comparable**. (Encore une fois, Angular 2 devrait perdre du poids avant la version finale).

Cela dit, j'admets que les préoccupations concernant la taille des frameworks peuvent être exagérées :

> Les grandes applications ont tendance à avoir un minimum de plusieurs centaines de kilo-octets de code — souvent plus — qu'elles soient construites avec un framework ou non. Les développeurs ont besoin d'abstractions pour construire des logiciels complexes, et qu'elles proviennent d'un framework ou soient écrites à la main, elles impactent négativement les performances des applications.  
>   
> Même si vous deviez éliminer complètement les frameworks, de nombreuses applications auraient encore des centaines de kilo-octets de JavaScript. — Tom Dale dans [JavaScript Frameworks and Mobile Performance](http://tomdale.net/2015/11/javascript-frameworks-and-mobile-performance/)

Tom a raison. Des frameworks comme Angular et Ember sont plus gros parce qu'ils offrent beaucoup plus de fonctionnalités dès la sortie de la boîte.

Cependant, ma préoccupation est la suivante : de nombreuses applications n'ont pas besoin de tout ce que ces grands frameworks mettent dans la boîte. Dans un monde qui adopte de plus en plus les microservices, les micro-applications et les [paquets à responsabilité unique](http://www.npmjs.com), **React vous donne le pouvoir de « dimensionner correctement » votre application en sélectionnant soigneusement uniquement ce qui est nécessaire**. Dans un monde avec [plus de 200 000 modules npm](http://www.modulecounts.com), c'est une position puissante.

#### React embrasse [la philosophie Unix](https://en.wikipedia.org/wiki/Unix_philosophy).

React est une bibliothèque. C'est précisément la philosophie opposée des grands frameworks complets comme Angular et Ember. Donc lorsque vous sélectionnez React, vous êtes libre de choisir des bibliothèques modernes de pointe qui résolvent votre problème au mieux. JavaScript évolue rapidement, et React vous permet d'échanger de petites parties de votre application contre de meilleures bibliothèques au lieu d'attendre et d'espérer que votre framework innove.

Unix a résisté à l'épreuve du temps. Voici pourquoi :

> La philosophie des petits outils composables à usage unique ne se démode jamais.

React est un outil ciblé, composable et à usage unique utilisé par [certains des plus grands sites web au monde](https://github.com/facebook/react/wiki/Sites-Using-React). Cela augure bien pour son avenir (Cela dit, Angular est [utilisé par de nombreux grands noms](https://www.madewithangular.com/#/) également).

#### Résumé de l'affrontement

Angular 2 est une énorme amélioration par rapport à la version 1. Le nouveau modèle de composant est plus simple à comprendre que les directives de la v1, il supporte le rendu isomorphe/universel, et il utilise un DOM virtuel offrant des améliorations de performance de 3 à 10 fois. Ces changements rendent Angular 2 très compétitif avec React. Il est indéniable que sa nature complète et opinionnée offre certains avantages clairs en réduisant la « fatigue JavaScript ».

Cependant, la taille et la syntaxe d'Angular 2 me donnent à réfléchir. L'engagement d'Angular envers une conception centrée sur HTML le rend complexe par rapport au modèle plus simple centré sur JavaScript de React. Dans React, vous n'apprenez pas de shims HTML spécifiques au framework comme ngWhatever. Vous passez votre temps à écrire du JavaScript classique. C'est l'avenir auquel je crois.

Commentaires ? Participez sur [Reddit](https://www.reddit.com/r/javascript/comments/3zbo90/angular_2_versus_react_there_will_be_blood/) ou [Hacker News](https://news.ycombinator.com/item?id=10836236).

**_Cory House_** est l'auteur de « [Building Applications with React and Flux](https://www.pluralsight.com/courses/react-flux-building-applications) », « [Clean Code: Writing Code for Humans](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiK1pXx89nJAhUujoMKHeuWAEUQFggcMAA&url=https%3A%2F%2Fwww.pluralsight.com%2Fcourses%2Fwriting-clean-code-humans&usg=AFQjCNEBfkBoN-IgCn_1jFUqWDAUIxcmAw&sig2=Ub9Wup4k4mrw_ffPgYu3tA) » et de plusieurs autres cours sur Pluralsight. Il est architecte logiciel chez VinSolutions et [forme des développeurs logiciels à l'international](http://www.bitnative.com/training/) sur des pratiques logicielles comme le développement front-end et le code propre. Cory est un MVP Microsoft, un expert développeur Telerik et le fondateur de [outlierdeveloper.com](http://www.outlierdeveloper.com).