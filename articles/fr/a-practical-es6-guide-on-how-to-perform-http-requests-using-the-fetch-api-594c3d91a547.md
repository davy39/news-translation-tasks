---
title: Un guide pratique ES6 sur la façon d'effectuer des requêtes HTTP en utilisant
  l'API Fetch
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-04T16:21:47.000Z'
originalURL: https://freecodecamp.org/news/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Kj2i4zLF-jKOsiLb.jpg
tags:
- name: api
  slug: api
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Un guide pratique ES6 sur la façon d'effectuer des requêtes HTTP en utilisant
  l'API Fetch
seo_desc: 'By Dler Ari

  In this guide, I’ll show you how to use the Fetch API (ES6+) to perform HTTP requests
  to an REST API with some practical examples you’ll most likely encounter.

  Want to quickly see the HTTP examples? Go to section 5. The first part describ...'
---

Par Dler Ari

Dans ce guide, je vais vous montrer comment utiliser l'API Fetch (ES6+) pour effectuer des requêtes HTTP vers une [API REST](https://jsonplaceholder.typicode.com/) avec quelques exemples pratiques que vous rencontrerez probablement.

Vous voulez voir rapidement les exemples HTTP ? Allez à la section 5. La première partie décrit la partie asynchrone de JavaScript lors de la gestion des requêtes HTTP.

> **Note** : Tous les exemples sont écrits en ES6 avec des [fonctions fléchées](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions).

Un modèle courant dans les applications web/mobiles actuelles consiste à demander ou à afficher des données du serveur (telles que des utilisateurs, des publications, des commentaires, des abonnements, des paiements, etc.) puis à les manipuler en utilisant des opérations CRUD (créer, lire, mettre à jour ou supprimer).

Pour manipuler davantage une ressource, nous utilisons souvent [ces méthodes JS](https://medium.freecodecamp.org/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f) (recommandées) telles que `.map()`, `.filter()` et `.reduce()`.

> Si vous voulez devenir un meilleur développeur web, créer votre propre entreprise, enseigner aux autres ou améliorer vos compétences en développement, je publierai des conseils et astuces hebdomadaires sur les derniers langages de développement web.

### Voici ce que nous allons aborder

1. Gérer les requêtes HTTP asynchrones de JS
2. Qu'est-ce que AJAX ?
3. Pourquoi l'API Fetch ?
4. Une rapide introduction à l'API Fetch
5. Exemples CRUD avec l'API Fetch ← le meilleur !

### 1. Gérer les requêtes HTTP asynchrones de JS

L'une des parties les plus difficiles pour comprendre comment fonctionne JavaScript (JS) est de comprendre comment gérer les requêtes asynchrones, ce qui nécessite une compréhension du fonctionnement des promesses et des rappels.

Dans la plupart des langages de programmation, nous sommes habitués à penser que les opérations se déroulent dans l'ordre (séquentiellement). La première ligne doit être exécutée avant de passer à la suivante. Cela a du sens car c'est ainsi que nous, humains, fonctionnons et accomplissons nos tâches quotidiennes.

Mais avec JS, nous avons plusieurs opérations qui s'exécutent en arrière-plan/premier plan, et nous ne pouvons pas avoir une application web qui se fige à chaque fois qu'elle attend un événement utilisateur.

> Décrire JavaScript comme asynchrone est peut-être trompeur. Il est plus précis de dire que JavaScript est synchrone et mono-thread avec divers mécanismes de rappel. [Lire plus](https://stackoverflow.com/questions/2035645/when-is-javascript-synchronous).

Néanmoins, parfois les choses doivent se produire dans l'ordre, sinon cela causera du chaos et des résultats inattendus. Pour cette raison, nous pouvons utiliser des promesses et des rappels pour structurer cela. Un exemple pourrait être la validation des identifiants de l'utilisateur avant de passer à l'opération suivante.

### 2. Qu'est-ce que AJAX

AJAX signifie Asynchronous JavaScript and XML, et il permet aux pages web d'être mises à jour de manière asynchrone en échangeant des données avec un serveur web pendant que l'application est en cours d'exécution. En bref, cela signifie essentiellement que vous pouvez mettre à jour des parties d'une page web sans recharger toute la page (l'URL reste la même).

> AJAX est un nom trompeur. Les applications AJAX peuvent utiliser XML pour transporter des données, mais il est tout aussi courant de transporter des données sous forme de texte brut ou de texte JSON.  
>  
> — w3shools.com

#### AJAX partout ?

J'ai vu que de nombreux développeurs ont tendance à s'enthousiasmer pour avoir tout dans une application monopage (SPA), et cela conduit à beaucoup de douleurs asynchrones ! Mais heureusement, nous avons des bibliothèques telles qu'Angular, VueJS et React qui rendent ce processus beaucoup plus facile et pratique.

Globalement, il est important d'avoir un équilibre entre ce qui doit recharger toute la page ou des parties de la page.

Et dans la plupart des cas, un rechargement de page fonctionne bien en termes de puissance des navigateurs. À l'époque, un rechargement de page pouvait prendre des secondes (selon l'emplacement du serveur et les capacités du navigateur). Mais les navigateurs d'aujourd'hui sont extrêmement rapides, donc décider d'effectuer AJAX ou un rechargement de page n'est pas si différent.

Mon expérience personnelle est qu'il est beaucoup plus facile et rapide de créer un moteur de recherche avec un simple bouton de recherche que de le faire sans bouton. Et dans la plupart des cas, le client ne se soucie pas si c'est une SPA ou un rechargement de page supplémentaire. Bien sûr, ne vous méprenez pas, j'adore les SPA, mais nous devons considérer quelques compromis, si nous traitons avec un budget limité et un manque de ressources, alors peut-être qu'une solution rapide est une meilleure approche.

En fin de compte, cela dépend vraiment du cas d'utilisation, mais personnellement, je pense que les SPA nécessitent plus de temps de développement et un peu de maux de tête qu'un simple rechargement de page.

### 3. Pourquoi l'API Fetch ?

Cela nous permet d'effectuer des requêtes HTTP déclaratives vers un serveur. Pour chaque requête, elle crée une `Promise` qui doit être résolue afin de définir le type de contenu et d'accéder aux données.

Maintenant, l'avantage de l'API Fetch est qu'elle est entièrement prise en charge par l'écosystème JS, et fait également partie de la [documentation MDN Mozilla](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API). Et dernier point mais non des moindres, elle fonctionne directement dans la plupart des navigateurs (sauf IE). À long terme, je suppose qu'elle deviendra la méthode standard pour appeler les API web.

> Note ! Je suis bien conscient d'autres approches HTTP telles que l'utilisation d'Observable avec RXJS, et comment elle se concentre sur la gestion de la mémoire/fuite en termes d'abonnement/désabonnement et ainsi de suite. Et peut-être que cela deviendra la nouvelle méthode standard pour effectuer des requêtes HTTP, qui sait ?  
>   
> En tout cas, dans cet article, je me concentre uniquement sur l'API Fetch, mais je pourrais écrire un article sur Observable et RXJS à l'avenir.

### 4. Une rapide introduction à l'API Fetch

La méthode `fetch()` retourne une `Promise` qui résout la `Response` de la `Request` pour montrer le statut (succès ou non). Si vous obtenez un jour ce message `promise {}` dans votre console, ne paniquez pas — cela signifie simplement que la `Promise` fonctionne, mais attend d'être résolue. Donc, pour la résoudre, nous avons besoin du gestionnaire `.then()` (rappel) pour accéder au contenu.

En bref, nous définissons d'abord le chemin (**Fetch**), ensuite nous demandons des données au serveur (**Request**), troisièmement nous définissons le type de contenu (**Body**) et enfin, nous accédons aux données (**Response**).

Si vous avez du mal à comprendre ce concept, ne vous inquiétez pas. Vous aurez une meilleure vue d'ensemble grâce aux exemples présentés ci-dessous.

```
Le chemin que nous utiliserons pour nos exemples 
https://jsonplaceholder.typicode.com/users // retourne du JSON
```

### 5. Exemples HTTP avec l'API Fetch

Si nous voulons accéder aux données, nous avons besoin de deux gestionnaires `.then()` (rappel). Mais si nous voulons manipuler la ressource, nous n'avons besoin que d'un seul gestionnaire `.then()`. Cependant, nous pouvons utiliser le second pour nous assurer que la valeur a été envoyée.

Modèle de base de l'API Fetch :

<script src="https://gist.github.com/AriPal/030365fa25e3c9260c8486e6705f9310.js"></script>

> Note ! L'exemple ci-dessus est uniquement à des fins illustratives. Le code ne fonctionnera pas si vous l'exécutez.

#### Exemples d'API Fetch

1. Afficher un utilisateur
2. Afficher une liste d'utilisateurs
3. Créer un nouvel utilisateur
4. Supprimer un utilisateur
5. Mettre à jour un utilisateur

> **Note !** La ressource ne sera pas vraiment créée sur le serveur, mais retournera un résultat fictif pour imiter un vrai serveur.

#### 1. Afficher un utilisateur

Comme mentionné précédemment, le processus d'affichage d'un seul utilisateur consiste en deux gestionnaires `.then()` (rappel), le premier pour définir l'objet, et le second pour accéder aux données.

> Remarquez qu'en lisant simplement la chaîne de requête `/users/2`, nous sommes capables de comprendre/prédire ce que fait l'API. Pour plus d'informations sur la façon d'écrire une API REST de haute qualité, consultez ces [directives](https://hackernoon.com/restful-api-designing-guidelines-the-best-practices-60e1d954e7c9) écrites par [Mahesh Haldar](https://www.freecodecamp.org/news/a-practical-es6-guide-on-how-to-perform-http-requests-using-the-fetch-api-594c3d91a547/undefined).

#### **Exemple**

<script src="https://gist.github.com/AriPal/7d80a696621a1bff97bb9516154b7e5a.js"></script>

#### 2. Afficher une liste d'utilisateurs

L'exemple est presque identique à l'exemple précédent, sauf que la chaîne de requête est `/users`, et non `/users/2`.

#### Exemple

<script src="https://gist.github.com/AriPal/83c75923f680b7a0670b812d9bad8518.js"></script>

#### 3. Créer un nouvel utilisateur

Celui-ci semble un peu différent de l'exemple précédent. Si vous n'êtes pas familier avec le protocole HTTP, il nous fournit simplement quelques méthodes pratiques telles que `POST`, `GET`, `DELETE`, `UPDATE`, `PATCH` et `PUT`. Ces méthodes sont des verbes qui décrivent simplement le type d'action à exécuter, et sont principalement utilisées pour manipuler la ressource/les données sur le serveur.

En tout cas, pour créer un nouvel utilisateur avec l'API Fetch, nous devons utiliser le verbe HTTP `POST`. Mais d'abord, nous devons le définir quelque part. Heureusement, il existe un argument optionnel `[Init](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/fetch)` que nous pouvons passer avec l'URL pour définir des paramètres personnalisés tels que le type de méthode, le corps, les identifiants, les en-têtes, etc.

> Note : Les paramètres de la méthode `fetch()` sont identiques à ceux du constructeur `[Request()](https://developer.mozilla.org/en-US/docs/Web/API/Request/Request)`.

#### Exemple

<script src="https://gist.github.com/AriPal/2731c3803e2f498a0dfc8abcda8d946c.js"></script>

#### **4. Supprimer un utilisateur**

Pour supprimer l'utilisateur, nous devons d'abord cibler l'utilisateur avec `/users/1`, puis nous définissons le type de méthode qui est `DELETE`.

#### Exemple

<script src="https://gist.github.com/AriPal/cb06ffac0c04408da74e8707e9e3dd6b.js"></script>

#### 5. Mettre à jour un utilisateur

Le verbe HTTP `PUT` est utilisé pour manipuler la ressource cible, et si vous voulez faire des changements partiels, vous devrez utiliser `PATCH`. Pour plus d'informations sur ce que font ces verbes HTTP, [consultez ceci](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

#### Exemple

<script src="https://gist.github.com/AriPal/eb46118f720d3d71800fef7ead682a70.js"></script>

### Conclusion

Maintenant, vous avez une compréhension de base de la façon de récupérer ou de manipuler une ressource du serveur en utilisant l'API Fetch de JavaScript, ainsi que de la façon de gérer les promesses. Vous pouvez utiliser cet article comme guide pour structurer vos requêtes API pour les opérations CRUD.

Personnellement, je pense que l'API Fetch est déclarative et que vous pouvez facilement comprendre ce qui se passe sans aucune expérience technique en codage.

> Tous les exemples sont montrés dans des requêtes basées sur des promesses où nous enchaînons la requête en utilisant le rappel `_.then_`. Il s'agit d'une approche standard que de nombreux développeurs connaissent, cependant, si vous voulez utiliser `_async/await_`, consultez cet [article](https://dev.to/johnpaulada/synchronous-fetch-with-asyncawait). Le concept est le même, sauf que `async/await` est plus facile à lire et à écrire.

Voici quelques articles que j'ai écrits sur l'écosystème web ainsi que des conseils et astuces de programmation personnelle.

* [Une comparaison entre Angular et React](https://www.freecodecamp.org/news/a-comparison-between-angular-and-react-and-their-core-languages-9de52f485a76/)
* [Un esprit chaotique conduit à un code chaotique](https://www.freecodecamp.org/news/a-chaotic-mind-leads-to-chaotic-code-e7d6962777c0)
* [Les développeurs qui veulent constamment apprendre de nouvelles choses](https://codeburst.io/developers-that-constantly-want-to-learn-new-things-heres-a-tip-7a16e42302e4)
* [Un guide pratique des modules ES6](https://www.freecodecamp.org/news/how-to-use-es6-modules-and-why-theyre-important-a9b20b480773)
* [Apprenez ces concepts fondamentaux du Web](https://www.freecodecamp.org/news/learn-these-core-javascript-concepts-in-just-a-few-minutes-f7a16f42c1b0/?gi=6274e9c4d599)
* [Améliorez vos compétences avec ces méthodes JavaScript importantes](https://www.freecodecamp.org/news/7-javascript-methods-that-will-boost-your-skills-in-less-than-8-minutes-4cc4c3dca03f/)
* [Programmez plus vite en créant des commandes bash personnalisées](https://codeburst.io/learn-how-to-create-custom-bash-commands-in-less-than-4-minutes-6d4ceadd9590)

Vous pouvez me trouver sur Medium où je publie chaque semaine. Ou vous pouvez me suivre sur [Twitter](http://twitter.com/dleroari), où je poste des conseils et astuces de développement web pertinents ainsi que des histoires personnelles.

_P.S. Si vous avez aimé cet article et en voulez plus comme celui-ci, applaudissez 💙 et partagez avec des amis qui pourraient en avoir besoin, c'est du bon karma._