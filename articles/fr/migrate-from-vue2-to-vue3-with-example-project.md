---
title: Comment migrer de Vue v.2 à Vue v.3 avec un exemple de projet simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-02T19:14:53.000Z'
originalURL: https://freecodecamp.org/news/migrate-from-vue2-to-vue3-with-example-project
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/Cover_migration_vue_2_3.jpg
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: '#vue-router'
  slug: vue-router
- name: Vue.js
  slug: vuejs
seo_title: Comment migrer de Vue v.2 à Vue v.3 avec un exemple de projet simple
seo_desc: 'By Fabio Pacific

  What is Vue.js?

  Vue.js is a progressive JavaScript frontend framework written by Evan You. It''s
  one of the most powerful and easy to learn frameworks, and it has over 9.5 million
  downloads per month.

  In September 2020, Vue 3 core was...'
---

Par Fabio Pacific

## Qu'est-ce que Vue.js ?
Vue.js est un framework frontend JavaScript progressif écrit par Evan You. C'est l'un des frameworks les plus puissants et faciles à apprendre, et il compte plus de 9,5 millions de téléchargements par mois.

En septembre 2020, le cœur de Vue 3 a été publié. La nouvelle version de Vue.js introduit quelques nouvelles fonctionnalités mais aussi quelques changements majeurs.

## Pourquoi devrais-je migrer vers Vue 3 ?
À mesure que l'industrie technologique évolue, les bibliothèques, les langages et les frameworks évoluent également. À chaque version, des bugs sont corrigés et de nouvelles fonctionnalités sont introduites. Et souvent, avec toute version majeure, votre flux de travail est amélioré. Les nouvelles fonctionnalités peuvent vous donner l'opportunité de faire des choses qui étaient fastidieuses auparavant.

Vue 3 est encore relativement nouveau. Vous n'êtes pas obligé de migrer tous vos projets, mais avec le temps, le support pour la version 2 pourrait prendre fin. Pour cette raison, il est bon de connaître les étapes que vous devrez suivre pour migrer vos projets.

Dans ce guide, je vais vous guider à travers les étapes de base que vous devrez suivre pour aborder la migration. Nous allons prendre un projet simple et le migrer vers Vue 3.

Le projet que nous allons utiliser est intentionnellement simple, afin que tout le monde puisse suivre. Plus votre projet est complexe, plus vous devrez planifier soigneusement la migration.


## Introduction

La nouvelle version de Vue.js apporte quelques changements majeurs et de nouvelles fonctionnalités. De plus, des bibliothèques populaires comme Vue Router ont été mises à jour pour supporter la nouvelle version de Vue.

Si vous connaissez déjà Vue 2, les bases sont assez similaires. Mais avant de pouvoir migrer un projet vers Vue 3, il y a des changements que vous devez prendre en compte.

Selon la taille du projet que vous souhaitez migrer, assurez-vous de considérer tous les changements introduits avec la nouvelle version afin que votre application continue de fonctionner après la migration.

Pour ce tutoriel, je vais garder les choses simples et vous montrer comment migrer un projet Vue.js qui utilise actuellement le CDN de Vue 2.

Je prends le projet de mon livre que j'ai écrit pour freeCodeCamp, que vous pouvez trouver [ici](https://www.freecodecamp.org/news/build-a-portfolio-with-vuejs/).

Dans ce projet, nous avons utilisé Vue Router, donc nous allons également examiner les changements de Vue Router dans cet article.

## Ce dont vous avez besoin pour suivre cet article

Pour suivre cet article, vous avez besoin d'une connaissance de base de Vue.js et de Vue Router. Si ce n'est pas le cas, je vous suggère de commencer par consulter mon livre disponible sur [freeCodeCamp](https://www.freecodecamp.org/news/build-a-portfolio-with-vuejs/).

Vous pouvez également trouver la playlist avec le cours complet de 8 heures disponible gratuitement sur ma [chaîne YouTube](https://www.youtube.com/playlist?list=PL-qez5yxvgfjYZE_BP7WyxZuLyVPyWrF1).

## Ce que nous allons couvrir dans cet article

Ce tutoriel est organisé en trois chapitres principaux. Tout d'abord, nous allons examiner les changements dans Vue.js v3.x, puis un aperçu rapide de Vue Router v4.x. Et enfin, nous commencerons à planifier la migration d'un projet réel.

- Aperçu de Vue v3.x
  - changements majeurs
- Aperçu de Vue Router v4.x
  - changements majeurs
- Migration du projet Portfolio
  - Cloner le dépôt
  - Mettre à jour les scripts CDN
  - Mettre à jour l'instance Vue
  - Mettre à jour l'instance Vue Router

Voici la version vidéo de cet article si vous souhaitez suivre là-bas :

%[https://youtu.be/5y8-fKSY_Lg]

Regarder la vidéo vous aidera à renforcer votre apprentissage tout en lisant les étapes ci-dessous. Ici, vous pouvez trouver le dépôt [final](https://bitbucket.org/fbhood/advanced-vuejs/src/master/) pour le projet.

## Aperçu de Vue v3.x

Vue 3 introduit quelques nouvelles fonctionnalités et un ensemble de changements majeurs. Voyons comment ces changements affecteront notre application et prenons-les en compte avant de migrer.

### Changements majeurs de Vue V3.x

Dans Vue 3, les changements majeurs se répartissent essentiellement en sept catégories :

- API Globale
(responsable du comportement de Vue) - il est très probable que vous souhaitiez examiner ces changements.
- Directives de Template
(Changements apportés au fonctionnement des directives v-) - il est très probable que vous souhaitiez examiner ces changements.
- Composants
(Changements dans le fonctionnement des composants) - si votre application utilise des composants, il est très probable que vous souhaitiez examiner ces changements
- Fonction de rendu (Permet de créer des éléments HTML de manière programmatique)
- Éléments personnalisés (Informe Vue de la création d'éléments HTML personnalisés)
- Changements mineurs (Cela peut ne pas vous affecter, mais vous voudrez tout de même examiner ces points)
- API supprimées (Fonctionnalités qui ne sont plus disponibles dans Vue 3)

Parmi tous les changements, certains d'entre eux seront utilisés par toute application, comme l'API Globale et les composants. Vous devrez donc en tenir compte si vous souhaitez commencer à utiliser la nouvelle version de Vue.

Et il est utile de mentionner les changements supplémentaires suivants :

- La manière de créer des applications Vue et des instances de composants a changé (API Globale)
- Vous devez toujours déclarer l'option data comme une fonction (changement mineur)
- Changement de priorité lors de l'utilisation de v-if et v-for sur le même élément (directives de template)
- Vous devez déclarer une option emits pour les événements de composants (composants)

Pour une liste complète des changements, vous pouvez consulter la [documentation](https://v3.vuejs.org/guide/migration/introduction.html#breaking-changes)

Examinons certains de ces changements plus en détail maintenant.

### Comment créer des instances d'application et de composants dans Vue 3

Dans Vue 3, la manière de créer une application a changé. L'application Vue utilise désormais la nouvelle méthode `.createApp()` pour créer des instances d'application.

L'application Vue est désormais considérée comme un composant racine, donc la manière de définir ses options de données a également changé.

L'élément racine HTML n'a pas changé, donc dans un fichier index.html, vous verrez toujours quelque chose comme ceci :

```html
<div id="app"></div>

```

Dans le fichier JavaScript, il y a un changement important que vous devez comprendre : vous n'utiliserez plus `new Vue()` pour créer une nouvelle instance d'application, mais vous utiliserez plutôt une nouvelle méthode appelée `createApp()` :

```js

// Syntaxe Vue 3

const app = Vue.createApp({
    // objet d'options
})
app.mounth('#app') // Instance Vue - Composant racine

// Syntaxe Vue 2
const app = new Vue({
    // objet d'options
    el: '#app'
})

```

### Comment définir un composant dans Vue 3

Pour définir un composant dans Vue 3, vous n'utilisez plus `Vue.component()`. Vous utilisez désormais le composant racine de l'application, comme suit :

```js
/* Syntaxe Vue 3 */
const app = Vue.createApp({
    // options ici
})

app.component('nom-du-composant', {
    // code du composant ici
})


/* Syntaxe Vue 2*/
Vue.component('nom-du-composant', {
    // code du composant ici
})

```

### Comment utiliser l'objet d'options de données dans Vue 3

Étant donné que l'instance principale de l'application est désormais considérée comme un composant racine, vous ne pouvez plus spécifier la propriété data comme un objet. Au lieu de cela, vous devez la définir comme une fonction qui retourne un objet, comme vous le faites habituellement dans les composants.

```js
// Vue 3
const app = Vue.createApp({
    // objet d'options
    data(){
        return {
            message: 'bonjour'
        }
    }
})
app.mounth('#app') // Instance Vue - Composant racine

// Syntaxe Vue 2
const app = new Vue({
    // objet d'options
    el: '#app'
    data: {
        message: 'bonjour'
    }
})

```

### Changement de priorité pour v-if/v-for dans Vue 3

Dans Vue 2, si vous utilisiez les deux directives sur le même élément, la directive v-for avait la priorité sur v-if. Mais dans Vue 3, v-if a toujours la priorité.

Cependant, utiliser les deux directives n'est pas une bonne idée. Assurez-vous de consulter la documentation [ici](https://v3.vuejs.org/guide/migration/v-if-v-for.html#overview) pour en savoir plus.

### Comment utiliser la propriété Emits sur les événements de composants dans Vue 3 (changement majeur/nouvelle fonctionnalité)

Similaire à la propriété `props`, dans Vue 3, il y a également une propriété `emits` qu'un composant peut utiliser pour déclarer les événements qu'il peut émettre vers le composant parent.

Je recommande fortement d'utiliser cette propriété pour éviter d'émettre des événements deux fois dans des composants qui doivent ré-émettre des événements natifs, comme un événement de clic.

Voici un exemple de la documentation officielle :

```js
<template>
  <div>
    <p>{{ text }}</p>
    <button v-on:click="$emit('accepted')">OK</button>
  </div>
</template>
<script>
  export default {
    props: ['text'],
    emits: ['accepted']
  }
</script>
```

La propriété emits peut également accepter un objet.

Je n'approfondirai pas cela pour l'instant, mais je traiterai chacune des fonctionnalités/changements dans une série de vidéos dédiée plus tard, je promets.

## Aperçu de Vue Router v4.x

Avec la nouvelle version de Vue.js, nous avons également une nouvelle version de Vue Router. La nouvelle version v4.x apporte quelques changements majeurs que vous devrez prendre en compte si vous souhaitez migrer un projet vers la nouvelle version de Vue.

### Changements majeurs de Vue Router V4

Deux changements majeurs sont particulièrement dignes de mention, car ils sont à la base d'une application Vue Router. Vous devrez les connaître pour migrer votre application plus tard.

- L'instance Vue Router a changé
- Il y a une nouvelle option d'historique

La liste complète des changements est disponible [ici](https://next.router.vuejs.org/guide/migration/index.html).

Examinons ces deux changements en détail.

### L'instance Vue Router 4 a changé

Pour créer une nouvelle instance Vue Router, vous n'utilisez plus le constructeur de fonction VueRouter.

Voici la documentation de Vue Router v.3x [documentation](https://router.vuejs.org/guide/#javascript) pour que vous puissiez comparer.

Le code change de ceci :

```js
// 3. Créer l'instance du routeur et passer l'option `routes`
// Vous pouvez passer des options supplémentaires ici, mais gardons
// cela simple pour l'instant.
const router = new VueRouter({
  routes // raccourci pour `routes: routes`
})

// 4. Créer et monter l'instance racine.
// Assurez-vous d'injecter le routeur avec l'option router pour rendre
// toute l'application consciente du routeur.
const app = new Vue({
  router
}).$mount('#app')

```

À ceci :

```js
// 3. Créer l'instance du routeur et passer l'option `routes`
// Vous pouvez passer des options supplémentaires ici, mais gardons
// cela simple pour l'instant.
const router = VueRouter.createRouter({
  // 4. Fournir l'implémentation de l'historique à utiliser. Nous utilisons l'historique de hachage pour la simplicité ici.
  history: VueRouter.createWebHashHistory(), // <-- ceci est une nouvelle propriété et elle est obligatoire !
  routes, // raccourci pour `routes: routes`
})

// 5. Créer et monter l'instance racine.
const app = Vue.createApp({})
// Assurez-vous d'_utiliser_ l'instance du routeur pour rendre
// toute l'application consciente du routeur.
app.use(router)

app.mount('#app')

```

Dans le code ci-dessus, pour créer une nouvelle instance de routeur Vue, vous devez maintenant utiliser l'objet VueRouter et appeler la méthode `createRouter()`.

De plus, la nouvelle propriété history est obligatoire — `history: VueRouter.createWebHashHistory()`. Vous devez la définir ou vous obtiendrez une erreur de console.

Ensuite, vous créerez l'instance Vue en utilisant la méthode `createApp()` et utiliserez la variable `app` pour appeler la méthode `.use()`. Vous passez l'instance du routeur créée à l'étape précédente.

Enfin, vous pouvez monter l'élément DOM racine sur l'instance de l'application en utilisant `app.mount('#app')`.

Vous pouvez lire la documentation de Vue Router v4.x [documentation](https://next.router.vuejs.org/guide/#javascript) pour plus de détails.

## Comment migrer un projet de portfolio de Vue 2 à Vue 3

Vous pouvez voir comment faire cela dans la vidéo sur [YouTube](https://youtu.be/5y8-fKSY_Lg) si vous souhaitez suivre.

En tenant compte de tout ce qui précède, et après un examen attentif des changements majeurs, essayons de mettre à niveau l'un de nos projets de mon cours Vue. J'utiliserai le Portfolio, le projet final du cours.

Nous devrons :

- Cloner le dépôt
- Mettre à jour les scripts CDN
- Mettre à jour l'instance Vue
- Mettre à jour l'instance Vue Router

Pour migrer notre application vers Vue 3, nous devrons certainement mettre à jour les éléments suivants :

- Instance d'application Vue
- Instance Vue-Router
- Liens CDN

Prenons cela étape par étape.

### Cloner le dépôt du projet

Tout d'abord, assurez-vous de cloner le dépôt dans le dossier actuel :

```sh
git clone https://bitbucket.org/fbhood/vue-folio/src/master/ vue-folio
```

Puisque notre projet utilise toujours le CDN, l'étape suivante consiste à mettre à jour ses liens.

### Mettre à jour le CDN du projet

Dans notre projet, nous utilisons à la fois le CDN de Vue et le CDN de Vue Router, alors mettons-les à jour.

Ouvrez le fichier index.html et remplacez ceci :

```html
    <!-- Version de production VueJS 3 -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2.6.12"></script>
    <!-- Vue Router -->
    <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>
```

par ceci :

```html
    <!-- VueJS 3 -->
    <script src="https://unpkg.com/vue@3"></script>

    <!-- Vue Router -->
    <script src="https://unpkg.com/vue-router@4"></script>

```

### Mettre à jour le code

Maintenant, si vous ouvrez le projet avec le serveur en direct et ouvrez l'inspecteur, vous remarquerez que l'application ne s'affiche pas et qu'il y a deux erreurs dans la console. Les deux semblent liées au routeur Vue :

```js
Vous exécutez une version de développement de Vue.
Assurez-vous d'utiliser la version de production (*.prod.js) lors du déploiement pour la production.

Uncaught TypeError: window.Vue.use is not a function
    at vue-router.js:1832
    at vue-router.js:9
    at vue-router.js:10

Uncaught ReferenceError: VueRouter is not defined
    at main.js:185
```

Vue Router ? Pourquoi ?

Eh bien, rappelez-vous que lorsque Vue a été réécrit, ses bibliothèques ont également dû mettre à jour leurs bases de code. N'oubliez donc pas ces changements majeurs liés à Vue Router, puisque notre application l'utilise.

Commençons par mettre à jour l'instance principale de Vue pour utiliser la nouvelle syntaxe. Ensuite, nous examinerons les changements que nous devons apporter pour que Vue Router fonctionne.

Mettez à jour ce code dans le fichier main.js de ceci :

```js
// créer et monter l'instance Vue

const app = new Vue({
    router
}).$mount('#app')

```

à ceci :

```js
// créer et monter l'instance Vue

const app = Vue.createApp({
    router
})
app.mount('#app')
```

### Changements de Vue Router 4

Ci-dessus, nous avons vu la nouvelle syntaxe pour définir le composant racine de l'instance Vue. Mais maintenant, puisque nous utilisons le routeur Vue, nous devons également prendre en compte ses [changements majeurs](https://next.router.vuejs.org/guide/migration/index.html).

#### La manière dont Vue Router est instancié a changé

Il est passé de ceci :

```js
// créer l'instance du routeur
const router = new VueRouter({
    routes
})

```

à ceci :

```js
// créer l'instance du routeur
const router = VueRouter.createRouter({
    // Fournir l'implémentation de l'historique à utiliser. Nous utilisons l'historique de hachage pour la simplicité ici.
    history: VueRouter.createWebHashHistory(),
    routes, // raccourci pour `routes: routes`
})

```

Le code ci-dessus traite de deux changements majeurs : `new VueRouter()` a été remplacé par `VueRouter.createRouter()`, et la nouvelle option `history` remplace désormais `mode`.

Consultez la [documentation](https://next.router.vuejs.org/guide/#html) pour Vue Router 4 pour en savoir plus.

Enfin, faisons en sorte que notre application sache que nous utilisons Vue Router. Si nous avons injecté l'instance du routeur dans l'application Vue, nous devons maintenant l'instruire d'utiliser le routeur Vue, utiliser la méthode `.use()` pour ce faire, et lui passer l'instance du routeur.

Changez de ceci :

```js
// créer et monter l'instance Vue

const app = Vue.createApp({
    router
})
app.mount('#app')
```

à ceci :

```js
// créer et monter l'instance Vue

const app = Vue.createApp({})
app.use(router)
app.mount('#app')
```

Et voilà !

## Conclusion

Peu importe à quel point votre application Vue est complexe — si vous souhaitez migrer vers une nouvelle version majeure, vous devrez toujours planifier cela, lire les notes de version et passer en revue tous les changements majeurs pour vous assurer de comprendre ce qui ne fonctionnera plus.

Plus l'application est complexe, plus vous devez planifier soigneusement votre migration.

Pour notre application simple, c'est tout ce qu'il y a à faire. Mais ce n'est pas toujours le cas. Alors, préparez-vous et planifiez à l'avance.

Si vous avez aimé ce guide, veuillez partager l'article et n'oubliez pas de vous abonner à ma [chaîne YouTube](https://youtube.com/channel/UCTuFYi0pTsR9tOaO4qjV_pQ). Merci d'avoir lu !