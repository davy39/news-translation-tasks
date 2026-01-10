---
title: Comment gérer l'état de l'utilisateur avec Vuex et Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-29T13:01:00.000Z'
originalURL: https://freecodecamp.org/news/managing-user-state-with-vuex-firebase-77eebc64f546
coverImage: https://cdn-media-1.freecodecamp.org/images/1*vmhxmp5jRp-4Rtfh3skrgQ.png
tags:
- name: General Programming
  slug: programming
- name: 'self-improvement '
  slug: self-improvement
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment gérer l'état de l'utilisateur avec Vuex et Firebase
seo_desc: 'By Gareth Redfern

  This tutorial walks through adding Vuex to a simple Vue.js Firebase app. We use
  Vuex to manage the logged in user state and display protected content.

  Building on top of the previous tutorial, we will now look at how we can handle
  s...'
---

Par Gareth Redfern

Ce tutoriel explique comment ajouter Vuex à une application Vue.js Firebase simple. Nous utilisons Vuex pour gérer l'état de l'utilisateur connecté et afficher du contenu protégé.

En nous basant sur le [tutoriel précédent](https://medium.freecodecamp.org/authentication-with-vue-js-firebase-5c3a82149f66), nous allons maintenant examiner comment nous pouvons gérer le stockage des utilisateurs connectés. Lorsqu'un utilisateur se connecte, nous avons besoin d'un moyen de stocker ses détails et de les vérifier depuis nos routes et composants.

Le magasin de données devra être en un seul endroit afin que toutes les routes et composants puissent recevoir les données. Lorsqu'un utilisateur se déconnecte, nous devrons transmettre cette information depuis un composant vers le magasin.

Vuex nous permet de faire ce dont nous avons besoin. Il fournit un magasin où toutes les données partagées peuvent résider. Chaque composant peut alors utiliser et mettre à jour ce magasin de données unique. Commençons par ajouter un dossier store à notre site et créons un fichier [store.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/store/store.js). Nous devrons importer la bibliothèque Vuex depuis NPM et l'utiliser dans notre application (les [fichiers du projet](https://github.com/garethredfern/vue-auth-demo) le font déjà).

Avec Vuex installé, nous l'incluons dans notre fichier [store.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/store/store.js#L2) et indiquons à Vue que nous voulons l'utiliser. Nous allons maintenant créer le magasin en utilisant `export const = new Vue.Store()`. Passez la propriété state sous forme d'objet où nous ajoutons toutes les propriétés dont notre application a besoin au niveau du magasin. Avec le magasin exporté, nous pouvons l'importer dans notre fichier [main.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/main.js#L5) et l'ajouter à l'[instance Vue](https://github.com/garethredfern/vue-auth-demo/blob/master/src/main.js#L58). Les données du magasin seront maintenant disponibles pour être utilisées dans notre application avec :

`this.$store.state.propertyName`

#### Utilisation des Getters pour obtenir l'État

Accéder directement au magasin en utilisant `this.$store.state.propertyName` n'est pas très DRY. Il serait beaucoup mieux de pouvoir appeler une méthode qui récupère nos propriétés pour nous. Vous utiliseriez également cette méthode pour effectuer des calculs supplémentaires si nécessaire. C'est là que les [getters](https://vuex.vuejs.org/en/getters.html) viennent à notre secours.

> Vuex nous permet de définir des "getters" dans le magasin. Vous pouvez les considérer comme des propriétés calculées pour les magasins. Comme les propriétés calculées, le résultat d'un getter est mis en cache en fonction de ses dépendances et ne sera réévalué que lorsque certaines de ses dépendances auront changé.

Nous ajoutons des getters à notre fichier [store.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/store/store.js#L11) dans l'instance du magasin. Ils sont définis comme des méthodes sur l'objet `getters`. Ici, nous avons accès à notre état en utilisant l'argument state :

`getUser: (state) => { return state.user; } // Fonction ES6`

Ce getter simple retourne notre propriété user depuis l'état. Nous pouvons maintenant l'utiliser dans n'importe lequel de nos composants en appelant :

`this.$store.getters.getUser;`

Bien que l'exemple ici soit très simple, il montre comment vous pouvez maintenant réutiliser ce code dans toute notre application. Si vous devez changer le fonctionnement de cette méthode, vous ne la modifiez qu'à un seul endroit.

#### Utilisation des Mutations pour changer l'État

Il est également judicieux d'avoir un seul endroit pour changer l'état de notre magasin. Ainsi, les composants peuvent manipuler l'état et mettre à jour toutes les instances.

Les [mutations](https://vuex.vuejs.org/en/mutations.html) sont ce que Vue utilise pour effectuer ces tâches. Nous ajoutons des mutations à notre fichier [store.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/store/store.js#L16) dans l'instance du magasin. Les composants exécutent ces méthodes pour mettre à jour l'état dans toute l'application. Ils peuvent ensuite écouter ces changements via les getters que nous avons définis.

Dans notre application, nous créons une mutation qui se connecte à Firebase et définit l'utilisateur actuellement connecté. Si personne n'est connecté, la méthode d'authentification Firebase retourne null.

`setUser: state => { state.user = Firebase.auth().currentUser`; }

Notre application peut maintenant avoir un seul endroit pour vérifier les utilisateurs connectés. Tous les composants peuvent utiliser cela pour accéder aux détails de l'utilisateur et charger l'interface utilisateur pertinente.

#### Utilisation des Actions pour valider les Mutations

La dernière partie de ce voyage Vuex est de comprendre comment fonctionnent les [actions](https://vuex.vuejs.org/en/actions.html). Les mutations ne peuvent s'exécuter que de manière synchrone, et c'est exactement le comportement que nous attendons d'elles. En exécutant une méthode synchrone, vous pouvez savoir de manière fiable qu'elle changera l'état lorsque vous en aurez besoin.

Supposons que nous voulons faire un appel à une API tierce, comment ferions-nous cela ? Nous ajoutons une action pour valider une mutation uniquement lorsque la méthode asynchrone est terminée. Ainsi, nous pouvons exécuter des méthodes asynchrones mais ne valider leur état qu'une fois qu'elles ont terminé.

Voyons comment nous faisons cela dans notre application.

Nous déclenchons des actions avec la méthode `store.dispatch`. Dans notre composant [App.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/App.vue#L23), lorsque l'instance Vue est créée pour la première fois, nous déclenchons la méthode `setUser`. Cela exécute ensuite l'action `this.$store.dispatch('setUser');` dans notre fichier [store.js](https://github.com/garethredfern/vue-auth-demo/blob/master/src/store/store.js#L22). Examinons maintenant l'action `setUser` qui est définie comme une méthode.

`setUser: context => { context.commit('setUser'); }`

Ici, nous passons le `context` qui est disponible depuis Vuex et nous donne accès à la méthode `commit`. La méthode commit prend ensuite la méthode de mutation que vous souhaitez exécuter. Dans notre cas, `setUser`. Notre méthode de mutation porte le même nom que l'action `setUser`, mais ce n'est pas obligatoire.

#### Mettre le tout ensemble

![Image](https://cdn-media-1.freecodecamp.org/images/4QvVu2oHF9KSw6ZArduwYtwgYP8Ad7ENTZAb)
_Image tirée de la documentation Vuex_

Le diagramme ci-dessus résume comment les 3 parties clés de Vuex fonctionnent ensemble pour servir des données à nos composants. Pour ce tutoriel, Vuex peut bien être excessif.

Cependant, il a résolu le problème de savoir quand un utilisateur est connecté afin que nous puissions afficher des liens dans la navigation. Jetez un coup d'œil au composant [Header.vue](https://github.com/garethredfern/vue-auth-demo/blob/master/src/components/Header.vue).

Ici, nous affichons des liens en fonction de si un utilisateur est connecté. Tout ce que nous avons à faire est d'ajouter `v-if="!user"` à chacun de nos composants `[router-link](https://router.vuejs.org/en/api/router-link.html)`. La variable `user` est une propriété calculée, elle retourne l'objet utilisateur ou `null` si quelqu'un est connecté ou non.

#### Lectures supplémentaires

* [Comprendre les hooks de cycle de vie de Vue](https://alligator.io/vuejs/component-lifecycle/)
* [Structure de l'application](https://vuex.vuejs.org/en/structure.html)