---
title: 'Le manuel Vue : une introduction approfondie à Vue.js'
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2018-07-05T16:45:07.000Z'
originalURL: https://freecodecamp.org/news/the-vue-handbook-a-thorough-introduction-to-vue-js-1e86835d8446
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Nzc4LiAlVXl8ic9T6v31zw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
- name: Vuex
  slug: vuex
seo_title: 'Le manuel Vue : une introduction approfondie à Vue.js'
seo_desc: 'Get this post in PDF/ePub/MOBI format at vuehandbook.com


  Vue is a very popular JavaScript front-end framework, one that’s experiencing a
  huge amount of growth.

  It is simple, tiny (~24KB), and very performant. It feels different from all the
  other Ja...'
---

> Obtenez ce post au format PDF/ePub/MOBI sur [vuehandbook.com](https://vuehandbook.com)

Vue est un framework front-end JavaScript très populaire, qui connaît une croissance énorme.

Il est simple, minuscule (~24 Ko) et très performant. Il semble différent de tous les autres frameworks front-end JavaScript et bibliothèques de vue. Découvrons pourquoi.

### Tout d'abord, qu'est-ce qu'un framework front-end JavaScript ?

Si vous n'êtes pas sûr de ce qu'est un framework JavaScript, Vue est la première rencontre parfaite avec un framework.

Un framework JavaScript nous aide à créer des applications modernes. Les applications JavaScript modernes sont principalement utilisées sur le Web, mais alimentent également de nombreuses applications de bureau et mobiles.

Jusqu'au début des années 2000, les navigateurs n'avaient pas les capacités qu'ils ont aujourd'hui. Ils étaient beaucoup moins puissants, et la construction d'applications complexes à l'intérieur d'eux n'était pas réalisable en termes de performance. L'outil n'était même pas quelque chose auquel les gens pensaient.

Tout a changé lorsque Google a dévoilé [Google Maps](https://www.google.com/maps) et [GMail](https://www.google.com/gmail), deux applications qui fonctionnaient à l'intérieur du navigateur. [Ajax](https://developer.mozilla.org/en-US/docs/Web/Guide/AJAX/Getting_Started) a rendu les requêtes réseau asynchrones possibles. Avec le temps, les développeurs ont commencé à construire sur la plateforme Web, tandis que les ingénieurs travaillaient sur la plateforme elle-même — les navigateurs, les normes Web, les API des navigateurs et le langage JavaScript.

Des bibliothèques comme [jQuery](https://jquery.com/) et [Mootools](https://mootools.net/) étaient les premiers grands projets qui se sont construits sur JavaScript et qui étaient très populaires pendant un certain temps. Elles fournissaient essentiellement une API plus agréable pour interagir avec le navigateur et offraient des solutions de contournement pour les bugs et les incohérences entre les différents navigateurs.

Des frameworks comme [Backbone](http://backbonejs.org/), [Ember](https://www.emberjs.com/), [Knockout](http://knockoutjs.com/), et [AngularJS](https://angularjs.org/) étaient la première vague de frameworks JavaScript modernes.

La deuxième vague, qui est la vague actuelle, a [React](https://reactjs.org/), [Angular](https://angular.io/), et [Vue](https://vuejs.org/) comme principaux acteurs.

Notez que jQuery, Ember et les autres projets que j'ai mentionnés sont toujours largement utilisés, activement maintenus, et des millions de sites web dépendent d'eux.

Cela dit, les techniques et les outils évoluent, et en tant que développeur JavaScript, il est probable que vous deviez maintenant connaître React, Angular ou Vue plutôt que ces anciens frameworks.

Les frameworks abstraient l'interaction avec le navigateur et le DOM. Au lieu de manipuler les éléments en les référençant dans le DOM, nous définissons et interagissons avec eux de manière déclarative, à un niveau plus élevé.

Utiliser un framework, c'est comme utiliser le langage de programmation [C](https://en.wikipedia.org/wiki/C_(programming_language)) au lieu d'utiliser le langage [Assembleur](https://en.wikipedia.org/wiki/Assembly_language) pour écrire des programmes système. C'est comme utiliser un ordinateur pour écrire un document au lieu d'utiliser une machine à écrire. C'est comme avoir une voiture autonome au lieu de conduire la voiture soi-même.

Eh bien, pas à ce point-là, mais vous voyez l'idée. Au lieu d'utiliser les API de bas niveau offertes par le navigateur pour manipuler les éléments, et de construire des systèmes extrêmement complexes pour écrire une application, vous utilisez des outils construits par des personnes très intelligentes qui facilitent notre vie.

### La popularité de Vue

À quel point Vue.js est-il populaire ?

Vue avait :

* 7 600 étoiles sur GitHub en 2016
* 36 700 étoiles sur GitHub en 2017

et il a plus de 100 000+ étoiles sur GitHub, en juin 2018.

Son nombre de téléchargements sur [npm](https://www.npmjs.com/) augmente chaque jour, et il est maintenant à ~350 000 téléchargements par semaine.

Je dirais que Vue est très populaire, étant donné ces chiffres.

En termes relatifs, il a approximativement le même nombre d'étoiles GitHub que React, qui est né des années avant.

Les chiffres ne sont pas tout, bien sûr. L'impression que j'ai de Vue est que les développeurs **l'adorent**.

Un point clé dans la montée de Vue a été son adoption dans l'écosystème Laravel, un framework d'application web PHP très populaire. Mais depuis, il est devenu répandu parmi de nombreuses autres communautés de développement.

#### Pourquoi les développeurs adorent Vue

Tout d'abord, Vue est appelé un framework progressif.

Cela signifie qu'il s'adapte aux besoins du développeur. D'autres frameworks nécessitent un engagement complet de la part d'un développeur ou d'une équipe et veulent souvent que vous réécriviez une application existante car ils nécessitent un ensemble spécifique de conventions. Vue s'intègre facilement dans votre application avec une simple balise `script` pour commencer, et il peut grandir avec vos besoins, passant de 3 lignes à la gestion de toute votre couche de vue.

Vous n'avez pas besoin de connaître [webpack](https://webpack.js.org/), [Babel](https://babeljs.io/), npm ou quoi que ce soit pour commencer avec Vue. Mais lorsque vous êtes prêt, Vue vous permet de vous appuyer facilement sur eux.

C'est un excellent argument de vente, surtout dans l'écosystème actuel des frameworks et bibliothèques JavaScript front-end qui tendent à aliéner les nouveaux venus et aussi les développeurs expérimentés qui se sentent perdus dans l'océan de possibilités et de choix.

Vue.js est probablement le framework front-end le plus accessible. Certaines personnes appellent Vue le **nouveau jQuery**, car il s'intègre facilement dans l'application via une balise de script, et gagne progressivement de l'espace à partir de là. Considérez cela comme un compliment, puisque jQuery a dominé le Web au cours des dernières années, et il fait toujours son travail sur un grand nombre de sites.

Vue a été construit en choisissant les meilleures idées des frameworks comme Angular, React et Knockout, et en sélectionnant les meilleurs choix que ces frameworks ont faits. Et en excluant certaines moins brillantes, il a commencé comme un ensemble de "meilleures pratiques" et a grandi à partir de là.

#### Où se positionne Vue.js dans le paysage des frameworks ?

Les deux éléphants dans la pièce, lorsqu'on parle de développement web, sont React et Angular. Comment Vue se positionne-t-il par rapport à ces deux grands et populaires frameworks ?

Vue a été créé par Evan You lorsqu'il travaillait chez Google sur des applications AngularJS (Angular 1.0). Il est né d'un besoin de créer des applications plus performantes. Vue a repris une partie de la syntaxe de templating d'Angular, mais a supprimé la pile complexe et opinionnée qu'Angular nécessitait, et l'a rendu très performant.

Le nouvel Angular (Angular 2.0) a également résolu de nombreux problèmes d'AngularJS, mais de manière très différente. Il nécessite également un engagement envers [TypeScript](https://www.typescriptlang.org/) que tous les développeurs n'apprécient pas (ou ne veulent pas apprendre).

Et React ? Vue a repris de nombreuses bonnes idées de React, notamment le Virtual DOM. Mais Vue l'implémente avec une sorte de gestion automatique des dépendances. Cela suit quels composants sont affectés par un changement d'état afin que seuls ces composants soient re-rendus lorsque cette propriété d'état change.

Dans React, en revanche, lorsqu'une partie de l'état qui affecte un composant change, le composant sera re-rendu. Par défaut, tous ses enfants seront également re-rendus. Pour éviter cela, vous devez utiliser la méthode `shouldComponentUpdate` de chaque composant et déterminer si ce composant doit être re-rendu. Cela donne à Vue un léger avantage en termes de facilité d'utilisation et de gains de performance dès la sortie de la boîte.

Une grande différence avec React est [JSX](https://reactjs.org/docs/introducing-jsx.html). Bien que vous puissiez techniquement utiliser JSX dans Vue, ce n'est pas une approche populaire et à la place, le [système de templating](https://vuejs.org/v2/guide/syntax.html) est utilisé. Tout fichier HTML est un template Vue valide. JSX est très différent de HTML, et a une courbe d'apprentissage pour les personnes de l'équipe qui pourraient n'avoir besoin de travailler qu'avec la partie HTML de l'application, comme les designers.

Les templates Vue sont très similaires à [Mustache](http://mustache.github.io/) et [Handlebars](https://handlebarsjs.com/) (bien qu'ils diffèrent en termes de flexibilité). À ce titre, ils sont plus familiers aux développeurs qui ont déjà utilisé des frameworks comme Angular et Ember.

La bibliothèque officielle de gestion d'état, [Vuex](https://vuex.vuejs.org/), suit l'architecture Flux et est quelque peu similaire à [Redux](https://redux.js.org/) dans ses concepts. Encore une fois, cela fait partie des aspects positifs de Vue, qui a vu ce bon modèle dans React et l'a emprunté pour son écosystème. Et bien que vous puissiez utiliser Redux avec Vue, Vuex est spécifiquement adapté pour Vue et son fonctionnement interne.

Vue est flexible, mais le fait que l'équipe principale maintienne deux packages très importants pour toute application web (comme le routage et la gestion d'état) le rend beaucoup moins fragmenté que React. Par exemple : `vue-router` et `vuex` sont essentiels au succès de Vue.

Vous n'avez pas besoin de choisir ou de vous soucier de savoir si cette bibliothèque que vous avez choisie sera maintenue à l'avenir et suivra les mises à jour du framework. Puisqu'ils sont officiels, ils sont les bibliothèques de référence pour leur niche (mais vous pouvez choisir d'utiliser ce que vous aimez, bien sûr).

Une chose qui distingue Vue de React et Angular est que Vue est un projet **indépendant** : il n'est pas soutenu par une grande entreprise comme Facebook ou Google.

Au lieu de cela, il est entièrement soutenu par la communauté, qui favorise le développement grâce à des dons et des sponsors. Cela garantit que la feuille de route de Vue n'est pas dictée par l'agenda d'une seule entreprise.

### Votre première application Vue

Si vous n'avez jamais créé d'application Vue.js, je vais vous guider à travers la tâche de création d'une application pour que vous compreniez comment elle fonctionne.

#### Premier exemple

Tout d'abord, je vais passer par l'exemple le plus basique de l'utilisation de Vue.

Vous créez un fichier HTML qui contient :

```html
<html>
  <body>
    <div id="example">
      <p>{{ hello }}</p>
    </div>
    <script src="https://unpkg.com/vue"></script>
    <script>
        new Vue({
            el: '#example',
            data: { hello: 'Hello World!' }
        })
    </script>
  </body>
</html>
```

et vous l'ouvrez dans le navigateur. C'est votre première application Vue ! La page devrait afficher un message "Hello World !".

J'ai placé les balises script à la fin du body afin qu'elles soient exécutées dans l'ordre après le chargement du DOM.

Ce que ce code fait est d'instancier une nouvelle application Vue, liée à l'élément `#example` comme son template. Il est défini en utilisant un sélecteur CSS généralement, mais vous pouvez également passer un `HTMLElement`.

Ensuite, il associe ce template à l'objet `data`. C'est un objet spécial qui héberge les données que nous voulons que Vue rende.

Dans le template, la balise spéciale `{{ }}` indique que ceci est une partie du template qui est dynamique, et son contenu doit être recherché dans les données de l'application Vue.

Vous pouvez voir cet exemple sur [CodePen](https://codepen.io/flaviocopes/pen/YLoLOp).

CodePen est un peu différent de l'utilisation d'un fichier HTML simple, et vous devez le configurer pour qu'il pointe vers l'emplacement de la bibliothèque Vue dans les paramètres du Pen :

![Image](https://cdn-media-1.freecodecamp.org/images/Qa8s2ayB3DhhE3dRKv4SFowGd8xHDvEeSlL4)

#### Deuxième exemple : l'application par défaut de Vue CLI

Élevons un peu le niveau. La prochaine application que nous allons construire est déjà faite, et c'est l'application par défaut de Vue CLI.

Qu'est-ce que Vue CLI ? C'est un utilitaire en ligne de commande qui aide à accélérer le développement en créant une structure de squelette d'application pour vous, avec une application d'exemple en place.

Il y a deux façons d'obtenir cette application :

**Utiliser Vue CLI localement**

La première consiste à installer Vue CLI sur votre ordinateur et à exécuter la commande :

```sh
vue create <entrez le nom de l'application>
```

**Utiliser CodeSandbox**

Une manière plus simple, sans avoir à installer quoi que ce soit, est d'aller sur [CodeSandbox](https://codesandbox.io/s/vue). Le lien ouvre l'application par défaut de Vue CLI.

CodeSandbox est un éditeur de code cool qui vous permet de construire des applications dans le cloud. Vous pouvez utiliser n'importe quel package npm, et pouvez facilement vous intégrer avec [Zeit Now](https://zeit.co/now) pour un déploiement facile et avec [GitHub](https://github.com/) pour gérer le versioning.

Que vous choisissiez d'utiliser Vue CLI localement ou de passer par CodeSandbox, examinons cette application Vue en détail.

### La structure des fichiers

Outre `package.json`, qui contient la configuration, voici les fichiers contenus dans la structure initiale du projet :

* `index.html`
* `src/App.vue`
* `src/main.js`
* `src/assets/logo.png`
* `src/components/HelloWorld.vue`

#### `index.html`

Le fichier `index.html` est le fichier principal de l'application.

Dans le corps, il inclut juste un simple élément : `<div id="app">`</div>. C'est l'élément que l'application Vue utilisera pour s'attacher au DOM.

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1.0">
  <title>CodeSandbox Vue</title>
</head>

<body>
  <div id="app"></div>
  <!-- built files will be auto injected -->
</body>

</html>
```

#### `src/main.js`

C'est le fichier JavaScript principal qui pilote notre application.

Nous importons d'abord la bibliothèque Vue et le composant App depuis `App.vue`.

Nous définissons `productionTip` sur `false`, pour éviter que Vue n'affiche un conseil "vous êtes en mode développement" dans la console.

Ensuite, nous créons l'instance Vue, en l'assignant à l'élément DOM identifié par `#app`, que nous avons défini dans `index.html`, et nous lui disons d'utiliser le composant App.

```js
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
```

#### `src/App.vue`

`App.vue` est un composant mono-fichier. Il contient trois morceaux de code : HTML, CSS et JavaScript.

Cela peut sembler étrange au début, mais les composants mono-fichier sont un excellent moyen de créer des composants autonomes qui ont tout ce dont ils ont besoin dans un seul fichier.

Nous avons le balisage, le JavaScript qui va interagir avec lui, et le style qui lui est appliqué, qui peut être scopé ou non. Dans ce cas, il n'est pas scopé, et il génère simplement ce CSS qui est appliqué comme du CSS régulier à la page.

La partie intéressante se trouve dans la balise `script`.

Nous importons un composant depuis le fichier `components/HelloWorld.vue`, que nous décrirons plus tard.

Ce composant sera référencé dans notre composant. C'est une dépendance. Nous allons générer ce code

```html
<div id="app">
  <img width="25%" src="./assets/logo.png">
  <HelloWorld/>
</div>
```

à partir de ce composant, que vous voyez référence le composant `HelloWorld`. Vue insérera automatiquement ce composant à l'intérieur de ce placeholder.

```html
<template>
  <div id="app">
    <img width="25%" src="./assets/logo.png">
    <HelloWorld/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

#### `src/components/HelloWorld.vue`

Voici le composant `HelloWorld`, qui est inclus par le composant App.

Ce composant génère un ensemble de liens, ainsi qu'un message.

Rappelons que nous avons parlé de CSS dans App.vue, qui n'était pas scopé ? Le composant `HelloWorld` a un CSS scopé.

Vous pouvez facilement le déterminer en regardant la balise `style`. Si elle a l'attribut `scoped`, alors il est scopé : `<style scoped>

Cela signifie que le CSS généré ciblera le composant de manière unique, via une classe qui est appliquée par Vue de manière transparente. Vous n'avez pas besoin de vous en soucier, et vous savez que le CSS ne **fuiera** pas vers d'autres parties de la page.

Le message que le composant génère est stocké dans la propriété `data` de l'instance Vue, et est affiché dans le template comme `{{ msg }}`.

Tout ce qui est stocké dans `data` est accessible directement dans le template via son propre nom. Nous n'avons pas eu besoin de dire `data.msg`, juste `msg`.

```html
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Core Docs
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Forum
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Community Chat
        </a>
      </li>
      <li>
        <a
          href="https://twitter.com/vuejs"
          target="_blank"
        >
          Twitter
        </a>
      </li>
      <br>
      <li>
        <a
          href="http://vuejs-templates.github.io/webpack/"
          target="_blank"
        >
          Docs for This Template
        </a>
      </li>
    </ul>
    <h2>Ecosystem</h2>
    <ul>
      <li>
        <a
          href="http://router.vuejs.org/"
          target="_blank"
        >
          vue-router
        </a>
      </li>
      <li>
        <a
          href="http://vuex.vuejs.org/"
          target="_blank"
        >
          vuex
        </a>
      </li>
      <li>
        <a
          href="http://vue-loader.vuejs.org/"
          target="_blank"
        >
          vue-loader
        </a>
      </li>
      <li>
        <a
          href="https://github.com/vuejs/awesome-vue"
          target="_blank"
        >
          awesome-vue
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data() {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
```

#### Exécuter l'application

CodeSandbox dispose d'une fonctionnalité de prévisualisation très pratique. Vous pouvez exécuter l'application et modifier n'importe quoi dans le code source pour qu'il soit immédiatement reflété dans la prévisualisation.

![Image](https://cdn-media-1.freecodecamp.org/images/ZWfaVoQWEm4HzD0RNcS2osp8NpIPz-G5Vq5P)
_L'application autonome_

### Le Vue CLI

CodeSandbox est très pratique pour le codage en ligne et le travail sans avoir à configurer Vue localement. Une excellente façon de travailler localement est de configurer le Vue CLI (interface de ligne de commande). Découvrons-en plus à ce sujet.

Dans l'exemple précédent, j'ai introduit un exemple de projet basé sur le Vue CLI. Qu'est-ce que le Vue CLI exactement, et comment s'intègre-t-il dans l'écosystème Vue ? De plus, comment configurer un projet basé sur Vue CLI localement ? Découvrons-le !

**Note :** Il y a une refonte majeure du CLI en cours, passant de la version 2 à la version 3. Bien que la version 3 ne soit pas encore stable, je vais la décrire car elle représente une amélioration majeure par rapport à la version 2, et est assez différente.

#### Installation

Le Vue CLI est un utilitaire en ligne de commande, et vous l'installez globalement en utilisant npm :

```
npm install -g @vue/cli
```

ou en utilisant Yarn :

```
yarn global add @vue/cli
```

Une fois que vous l'avez fait, vous pouvez invoquer la commande `vue`.

![Image](https://cdn-media-1.freecodecamp.org/images/F1uuQW81iw1WZNOiUn0xnLOagFi637vPDUfd)

#### Que fournit le Vue CLI ?

Le CLI est essentiel pour le développement rapide de Vue.js.

Son objectif principal est de s'assurer que tous les outils dont vous avez besoin fonctionnent ensemble, pour effectuer ce dont vous avez besoin, et abstraire tous les détails de configuration fastidieux que l'utilisation de chaque outil en isolation nécessiterait.

Il peut effectuer une configuration initiale du projet et l'échafaudage.

C'est un outil flexible. Une fois que vous avez créé un projet avec le CLI, vous pouvez aller et ajuster la configuration, sans avoir à **éjecter** votre application (comme vous le feriez avec `create-react-app`).

Lorsque vous éjectez de `create-react-app`, vous pouvez mettre à jour et ajuster ce que vous voulez, mais vous ne pouvez pas compter sur les fonctionnalités cool que `create-react-app` fournit.

Vous pouvez configurer n'importe quoi et toujours être en mesure de mettre à jour facilement.

Après avoir créé et configuré l'application, il agit comme un outil de dépendance d'exécution, construit sur Webpack.

La première rencontre avec le CLI est lors de la création d'une nouvelle application Vue.

#### Comment utiliser le CLI pour créer une nouvelle application Vue

La première chose que vous allez faire avec le CLI est de créer une application Vue :

```
vue create example
```

Le point intéressant est que c'est un processus interactif. Vous devez choisir un preset. Par défaut, il y a un preset qui fournit Babel et l'intégration [ESLint](https://eslint.org/) :

![Image](https://cdn-media-1.freecodecamp.org/images/FL4mTLZqzhKkAYL2FB507Tx1Hkdtnl0y5cgu)

Je vais appuyer sur la flèche vers le bas  et choisir manuellement les fonctionnalités que je veux :

![Image](https://cdn-media-1.freecodecamp.org/images/mkF3jMMCGluqmQ3hX3bGbCxhfXcwvWVNjWLi)

Appuyez sur `espace` pour activer l'une des choses dont vous avez besoin, puis appuyez sur `entrée` pour continuer. Puisque j'ai choisi `Linter / Formatter`, Vue CLI me demande la configuration. J'ai choisi `ESLint + Prettier` puisque c'est ma configuration préférée :

![Image](https://cdn-media-1.freecodecamp.org/images/bYwN2mfgTuJNxiiHBSNjnJQADZQvFR0TErhK)

La chose suivante est de choisir comment appliquer le linting. Je choisis `Lint on save`.

![Image](https://cdn-media-1.freecodecamp.org/images/dcQmjoykCaJG7pevG5Yc-6A43eVYUkCbTxn7)

Ensuite, le testing. Vue CLI me permet de choisir entre les deux solutions de test unitaire les plus populaires : [Mocha + Chai](https://mochajs.org/) et [Jest](https://jestjs.io/).

![Image](https://cdn-media-1.freecodecamp.org/images/lIdwYkOgcllnAJRVZOoKIxZ49ikNFoQjYtSV)

Vue CLI me demande où mettre toute la configuration : dans le fichier `package.json`, ou dans des fichiers de configuration dédiés, un pour chaque outil. J'ai choisi ce dernier.

![Image](https://cdn-media-1.freecodecamp.org/images/dN4W4ZALKh7Xz1D8ac7ebXpGdTPVGpzdujcc)

Ensuite, Vue CLI me demande si je veux sauvegarder ces presets, et me permet de les choisir comme option la prochaine fois que j'utilise Vue CLI pour créer une nouvelle application. C'est une fonctionnalité très pratique, car avoir une configuration rapide avec toutes mes préférences est un soulagement de complexité :

![Image](https://cdn-media-1.freecodecamp.org/images/X6rbmBloyRnQbdwrFQwtYeChdqxzQRpOJYfl)

Vue CLI me demande ensuite si je préfère utiliser [Yarn](https://yarnpkg.com/lang/en/) ou NPM :

![Image](https://cdn-media-1.freecodecamp.org/images/vbEmq0oYaGFjDtjL9D2QaUZ6t5omf0fjZTJM)

C'est la dernière chose qu'il me demande, puis il télécharge les dépendances et crée l'application Vue :

![Image](https://cdn-media-1.freecodecamp.org/images/Q52LD-RGQm9dHXMyWikiI5fMyESB7vRJqe1h)

#### Comment démarrer la nouvelle application Vue CLI

Vue CLI a créé l'application pour nous, et nous pouvons aller dans le dossier `example` et exécuter `yarn serve` pour démarrer notre première application en mode développement :

![Image](https://cdn-media-1.freecodecamp.org/images/iegqNiWWJaunJi-KFTV93EKuODc4njdfLRuf)

Le code source de l'application d'exemple contient quelques fichiers, y compris `package.json` :

![Image](https://cdn-media-1.freecodecamp.org/images/FuI7nmJ2NAtesloTZrh3eJL-aa0ceCCr68wQ)

C'est là que toutes les commandes CLI sont définies, y compris `yarn serve`, que nous avons utilisé il y a une minute. Les autres commandes sont

* `yarn build`, pour démarrer une construction de production
* `yarn lint`, pour exécuter le linter
* `yarn test:unit`, pour exécuter les tests unitaires

Je vais décrire l'application d'exemple générée par Vue CLI dans un tutoriel séparé.

#### Dépôt Git

Remarquez le mot `master` dans le coin inférieur gauche de VS Code ? C'est parce que Vue CLI crée automatiquement un dépôt, et fait le premier commit. Ainsi, nous pouvons nous lancer, changer les choses, et nous savons ce que nous avons changé :

![Image](https://cdn-media-1.freecodecamp.org/images/4IHrGo6U-xkz4aeVXf3S06AYzIk0lAZJ6t6y)

C'est plutôt cool. Combien de fois vous plongez-vous et changez-vous les choses, pour vous rendre compte, lorsque vous voulez commiter le résultat, que vous n'avez pas commité l'état initial ?

#### Utiliser un preset depuis la ligne de commande

Vous pouvez sauter le panneau interactif et demander à Vue CLI d'utiliser un preset particulier :

```
vue create -p favourite example-2
```

#### Où sont stockés les presets

Les presets sont stockés dans le fichier `.vuejs` dans votre répertoire personnel. Voici le mien après avoir créé le premier preset "favorite" :

```json
{
  "useTaobaoRegistry": false,
  "packageManager": "yarn",
  "presets": {
    "favourite": {
      "useConfigFiles": true,
      "plugins": {
        "@vue/cli-plugin-babel": {},
        "@vue/cli-plugin-eslint": {
          "config": "prettier",
          "lintOn": [
            "save"
          ]
        },
        "@vue/cli-plugin-unit-jest": {}
      },
      "router": true,
      "vuex": true
    }
  }
}
```

#### Plugins

Comme vous pouvez le voir en lisant la configuration, un preset est essentiellement une collection de plugins, avec une configuration optionnelle.

Une fois qu'un projet est créé, vous pouvez ajouter plus de plugins en utilisant `vue add` :

```
vue add @vue/cli-plugin-babel
```

Tous ces plugins sont utilisés dans la dernière version disponible. Vous pouvez forcer Vue CLI à utiliser une version spécifique en passant la propriété de version :

```json
"@vue/cli-plugin-eslint": {
  "version": "^3.0.0"
}
```

Cela est utile si une nouvelle version a un changement de rupture ou un bug, et que vous devez attendre un peu avant de l'utiliser.

#### Stocker les presets à distance

Un preset peut être stocké dans GitHub (ou sur d'autres services) en créant un dépôt qui contient un fichier `preset.json`, qui contient une seule configuration de preset.

Extrait de ce qui précède, j'ai fait un exemple de [preset](https://github.com/flaviocopes/vue-cli-preset/blob/master/preset.json) qui contient cette configuration :

```
{  "useConfigFiles": true,  "plugins": {    "@vue/cli-plugin-babel": {},    "@vue/cli-plugin-eslint": {      "config": "prettier",      "lintOn": [        "save"      ]    },    "@vue/cli-plugin-unit-jest": {}  },  "router": true,  "vuex": true}
```

Il peut être utilisé pour démarrer une nouvelle application en utilisant :

```
vue create --preset flaviocopes/vue-cli-preset example3
```

### Une autre utilisation du Vue CLI : le prototypage rapide

Jusqu'à présent, j'ai expliqué comment utiliser le Vue CLI pour créer un nouveau projet à partir de zéro, avec toutes les fonctionnalités. Mais pour un prototypage vraiment rapide, vous pouvez créer une application Vue très simple (même une qui est auto-contenue dans un seul fichier .vue) et la servir, sans avoir à télécharger toutes les dépendances dans le dossier `node_modules`.

Comment ? Installez d'abord le package global `cli-service-global` :

```
npm install -g @vue/cli-service-global
```

```
//ou
```

```
yarn global add @vue/cli-service-global
```

Créez un fichier app.vue :

```
<template>    <div>        <h2>Hello world!</h2>        <marquee>Heyyy</marquee>    </div></template>
```

et exécutez ensuite

```
vue serve app.vue
```

![Image](https://cdn-media-1.freecodecamp.org/images/pp3QTRAMwLtOnkhazBRgRrjYKnMEbnm1CbWL)
_L'application autonome_

Vous pouvez servir des projets plus organisés, composés de fichiers JavaScript et HTML également. Vue CLI utilise par défaut `main.js / index.js` comme point d'entrée, et vous pouvez avoir un `package.json` et toute configuration d'outil configurée. `vue serve` le prendra en charge.

Puisque cela utilise des dépendances globales, ce n'est pas une approche optimale pour autre chose qu'une démonstration ou un test rapide.

L'exécution de `vue build` préparera le projet pour le déploiement dans `dist/`, et générera tout le code correspondant (également pour les dépendances du fournisseur).

#### Webpack

En interne, Vue CLI utilise Webpack, mais la configuration est abstraite et nous ne voyons même pas le fichier de configuration dans notre dossier. Vous pouvez toujours y accéder en appelant `vue inspect` :

![Image](https://cdn-media-1.freecodecamp.org/images/dGT6I8Uq75505tD1Xj8wR-h7rO9ZvRby80cH)

### Les Vue DevTools

Lorsque vous expérimentez pour la première fois avec Vue, si vous ouvrez les outils de développement du navigateur, vous trouverez ce message : "Téléchargez l'extension Vue Devtools pour une meilleure expérience de développement : [https://github.com/vuejs/vue-devtools](https://github.com/vuejs/vue-devtools)"

![Image](https://cdn-media-1.freecodecamp.org/images/J-LJE-u3DphYF8pOpMnkCX9KoNz3fGp4OPea)
_Rappel pour installer les outils de développement Vue_

C'est un rappel amical pour installer l'extension Vue DevTools. Qu'est-ce que c'est ? Tout framework populaire a sa propre extension d'outils de développement, qui ajoute généralement un nouveau panneau aux outils de développement du navigateur, beaucoup plus spécialisé que ceux fournis par défaut par le navigateur. Dans ce cas, le panneau nous permettra d'inspecter notre application Vue et d'interagir avec elle.

Cet outil sera d'une aide incroyable lors de la construction d'applications Vue. Les outils de développement ne peuvent inspecter une application Vue que lorsqu'elle est en mode développement. Cela garantit que personne ne peut les utiliser pour interagir avec votre application de production — et rendra Vue plus performant, car il n'a pas à se soucier des Dev Tools.

Installons-le !

Il y a 3 façons d'installer les Vue Dev Tools :

* sur Chrome
* sur Firefox
* en tant qu'application autonome

Safari, Edge et autres navigateurs ne sont pas pris en charge avec une extension personnalisée, mais en utilisant l'application autonome, vous pouvez déboguer une application Vue.js s'exécutant dans n'importe quel navigateur.

#### Installer sur Chrome

Allez sur cette page du Google Chrome [Store](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd) et cliquez sur `**Ajouter à Chrome**`.

![Image](https://cdn-media-1.freecodecamp.org/images/uh0CFZPRsdnKFOY-OWWvQCN3UVcnh-0KXpfh)

Passez par le processus d'installation :

![Image](https://cdn-media-1.freecodecamp.org/images/hAQZpBESrlkCeLeLJpzeiPdJs12mmFHLRq9s)

L'icône des outils de développement Vue.js apparaît dans la barre d'outils. Si la page n'a pas d'instance Vue.js en cours d'exécution, elle est grisée.

![Image](https://cdn-media-1.freecodecamp.org/images/TaZntVatyBmsqqKsMjbGKn5nIuJikKLOJJyt)

Si Vue.js est détecté, l'icône a les couleurs du logo Vue.

![Image](https://cdn-media-1.freecodecamp.org/images/xPbOBNuLCdCE28QiFevAcqFb06Oqk8tB31Zy)

L'icône ne fait rien d'autre que de nous montrer qu'il **y a** une instance Vue.js. Pour utiliser les outils de développement, nous devons ouvrir le panneau des outils de développement, en utilisant "Affichage  Développeur  Outils de développement", ou `Cmd-Alt-i`

![Image](https://cdn-media-1.freecodecamp.org/images/td1gw01JZxVxAkHLGg9FKzIHz8UFhMhvr3gG)

#### Installer sur Firefox

Vous pouvez trouver l'extension des outils de développement Firefox dans le magasin d'add-ons Mozilla [store](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/).

![Image](https://cdn-media-1.freecodecamp.org/images/y-G2Zcw62ZrkjMOe6ottwLy-z6onBxnZzOXm)

Cliquez sur "Ajouter à Firefox" et l'extension sera installée. Comme avec Chrome, une icône grisée apparaît dans la barre d'outils

![Image](https://cdn-media-1.freecodecamp.org/images/LQCCB8c2g0OsUmJZ20fYJBPbampJudlIPocv)

Et lorsque vous visitez un site qui a une instance Vue en cours d'exécution, elle deviendra verte, et lorsque nous ouvrons les outils de développement, nous verrons un panneau "Vue" :

![Image](https://cdn-media-1.freecodecamp.org/images/jFYMTGNEhrkxzzC6Grdb7zgXrnHrwuR-0AiI)

#### Installer l'application autonome

Alternativement, vous pouvez utiliser l'application autonome DevTools.

Installez-la simplement en utilisant :

```
npm install -g @vue/devtools
```

```
//ou
```

```
yarn global add @vue/devtools
```

et exécutez-la en appelant :

```
vue-devtools
```

Cela ouvrira l'application autonome basée sur Electron.

Maintenant, collez la balise de script qu'elle vous montre

```
<script src="http://localhost:8098"></script>
```

à l'intérieur du fichier `index.html` du projet, et attendez que l'application soit rechargée. Elle se connectera automatiquement à l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/ANnfWmlscUkP0RN9Pn-hSABLCOxzMJYvtuqw)

#### Comment utiliser les outils de développement

Comme mentionné, les Vue DevTools peuvent être activés en ouvrant les outils de développement dans le navigateur et en se déplaçant vers le panneau Vue.

Une autre option consiste à faire un clic droit sur n'importe quel élément de la page et à choisir "Inspecter le composant Vue" :

![Image](https://cdn-media-1.freecodecamp.org/images/r4URIzj-Mm92WTnnl9iXMK18f8cIwmyICQ0m)

Lorsque le panneau Vue DevTools est ouvert, nous pouvons naviguer dans l'arborescence des composants. Lorsque nous choisissons un composant dans la liste de gauche, le panneau de droite montre les props et les données qu'il contient :

![Image](https://cdn-media-1.freecodecamp.org/images/h55RK1azzd7gjON36Da9HdY-tpu8cuVMBs-3)

En haut, il y a quatre boutons :

* **Composants** (le panneau actuel), qui liste toutes les instances de composants en cours d'exécution dans la page actuelle. Vue peut avoir plusieurs instances en cours d'exécution en même temps. Par exemple, il peut gérer votre widget de panier d'achat et le diaporama, avec des applications légères séparées.
* **Vuex** est l'endroit où vous pouvez inspecter l'état géré via Vuex.
* **Événements** montre tous les événements émis.
* **Actualiser** recharge le panneau des outils de développement.

Remarquez le petit texte `= $vm0` à côté d'un composant ? C'est un moyen pratique d'inspecter un composant en utilisant la console. En appuyant sur la touche "échap", la console apparaît en bas des outils de développement, et vous pouvez taper `$vm0` pour accéder au composant Vue :

![Image](https://cdn-media-1.freecodecamp.org/images/9fi396qPj8ajABDLnAoB77AkjDtLEJu-2okG)

C'est très pratique pour inspecter et interagir avec les composants sans avoir à les assigner à une variable globale dans le code.

#### Filtrer les composants

Commencez à taper un nom de composant, et l'arborescence des composants filtrera ceux qui ne correspondent pas.

![Image](https://cdn-media-1.freecodecamp.org/images/IdqSWwFMpvHVN125f7uIxue0Xp0ic-HJmBzX)

#### Sélectionner un composant dans la page

Cliquez sur le bouton `**Sélectionner un composant dans la page**`.

![Image](https://cdn-media-1.freecodecamp.org/images/RE969Y8eHdDn1rqHvj2OGfnEqthwHMVy37A-)
_Sélectionner un composant dans la page_

Vous pouvez survoler n'importe quel composant dans la page avec la souris, cliquer dessus, et il s'ouvrira dans les outils de développement.

#### Formater les noms des composants

Vous pouvez choisir d'afficher les composants en camelCase ou utiliser des tirets.

#### Filtrer les données inspectées

Dans le panneau de droite, vous pouvez taper n'importe quel mot pour filtrer les propriétés qui ne correspondent pas.

#### Inspecter le DOM

Cliquez sur le bouton Inspecter le DOM pour être redirigé vers l'inspecteur d'éléments des DevTools, avec l'élément DOM généré par le composant :

![Image](https://cdn-media-1.freecodecamp.org/images/YKTlyULN-MDOAg3R1KPA3tI27IqX5Q9ckIH4)
_Inspecter le DOM_

#### Ouvrir dans l'éditeur

Tout composant utilisateur (pas les composants de niveau framework) a un bouton qui l'ouvre dans votre éditeur par défaut. Très pratique.

### Configurer VS Code pour travailler avec Vue

[Visual Studio Code](https://code.visualstudio.com/) est l'un des éditeurs de code les plus utilisés au monde en ce moment. Les éditeurs, comme de nombreux produits logiciels, ont un cycle. Autrefois, [TextMate](https://macromates.com/) était le préféré des développeurs, puis ce fut [Sublime Text](https://www.sublimetext.com/), maintenant c'est VS Code.

Le côté positif d'être populaire est que les gens consacrent beaucoup de temps à construire des plugins pour tout ce qu'ils peuvent imaginer.

L'un de ces plugins est un outil génial qui peut nous aider, nous les développeurs Vue.js.

#### Vetur

Il s'appelle Vetur, il est très populaire (plus de 3 millions de téléchargements), et vous pouvez le trouver [sur le Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=octref.vetur).

![Image](https://cdn-media-1.freecodecamp.org/images/OOfHNunbiMBxokJsrmdrvWixSoDmaDdPRzxK)

#### Installation de Vetur

Cliquer sur le bouton Installer déclenchera le panneau d'installation dans VS Code :

![Image](https://cdn-media-1.freecodecamp.org/images/hskNZD-byUAunDSOjCdPXPMIb9v3rBPSlOvf)

Vous pouvez également simplement ouvrir les Extensions dans VS Code et rechercher "vetur" :

![Image](https://cdn-media-1.freecodecamp.org/images/xbOVISLaIuAgHHvD4gKVFb0Lg9R1f5R5Jowk)

Que fournit cette extension ?

#### Surlignage de la syntaxe

Vetur fournit un surlignage de la syntaxe pour tous vos fichiers source Vue.

Sans Vetur, un fichier `.vue` sera affiché de cette manière par VS Code :

![Image](https://cdn-media-1.freecodecamp.org/images/JTZ9KScP0WTtr-4cCvjvQJKkGwlA4EW9KIf3)

avec Vetur installé :

![Image](https://cdn-media-1.freecodecamp.org/images/c5wC-aTwknyXUSjqq9gbr-EqFbSDXSewix-N)

VS Code est capable de reconnaître le type de code contenu dans un fichier à partir de son extension.

En utilisant des composants mono-fichier, vous pouvez mélanger différents types de code dans le même fichier, du CSS au JavaScript en passant par le HTML.

VS Code par défaut ne peut pas reconnaître ce type de situation, et Vetur fournit un surlignage de la syntaxe pour chaque type de code que vous utilisez.

Vetur active la prise en charge, entre autres, pour :

* HTML
* CSS
* JavaScript
* Pug
* Haml
* SCSS
* PostCSS
* Sass
* Stylus
* TypeScript

#### Extraits de code

Comme pour le surlignage de la syntaxe, puisque VS Code ne peut pas déterminer le type de code contenu dans une partie d'un fichier `.vue`, il ne peut pas fournir les extraits de code que nous aimons tous. Les extraits de code sont des morceaux de code que nous pouvons ajouter au fichier, fournis par des plugins spécialisés.

Vetur donne à VS Code la capacité d'utiliser vos extraits de code préférés dans les composants mono-fichier.

#### IntelliSense

[IntelliSense](https://code.visualstudio.com/docs/editor/intellisense) est également activé par Vetur, pour chaque langage différent, avec l'autocomplétion :

![Image](https://cdn-media-1.freecodecamp.org/images/3KtNeQR4W8HVg-JVT0kmu33sL79xlWIT0KtY)

#### Échafaudage

En plus d'activer des extraits de code personnalisés, Vetur fournit son propre ensemble d'extraits de code. Chacun crée une balise spécifique (template, script ou style) avec son propre langage :

* `scaffold`
* `template with html`
* `template with pug`
* `script with JavaScript`
* `script with TypeScript`
* `style with CSS`
* `style with CSS (scoped)`
* `style with scss`
* `style with scss (scoped)`
* `style with less`
* `style with less (scoped)`
* `style with sass`
* `style with sass (scoped)`
* `style with postcss`
* `style with postcss (scoped)`
* `style with stylus`
* `style with stylus (scoped)`

Si vous tapez `scaffold`, vous obtiendrez un pack de démarrage pour un composant mono-fichier :

```
<template>
```

```
</template>
```

```
<script>export default {
```

```
}</script>
```

```
<style>
```

```
</style>
```

Les autres sont spécifiques et créent un seul bloc de code.

**Note :** (scoped) dans la liste ci-dessus signifie qu'il s'applique uniquement au composant actuel.

#### Emmet

[Emmet](https://emmet.io/), le moteur populaire d'abréviations HTML/CSS, est pris en charge par défaut. Vous pouvez taper l'une des abréviations Emmet, et en appuyant sur `tab`, VS Code l'étendra automatiquement à l'équivalent HTML :

![Image](https://cdn-media-1.freecodecamp.org/images/R7Q4k9hsI0yzBe-xaVIMxdBMukjQWzzIw-FG)

#### Linting et vérification des erreurs

Vetur s'intègre avec ESLint via le [plugin VS Code ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint).

![Image](https://cdn-media-1.freecodecamp.org/images/j1mnYvPYhNPWM00V0lDdxCwb5ZidBzG0Djtn)

![Image](https://cdn-media-1.freecodecamp.org/images/5Z2hR9l8ARVe3uucCT4iPzTsDZRuEh0gZSs8)

#### Formatage du code

Vetur fournit un support automatique pour le formatage du code afin de formater l'ensemble du fichier lors de l'enregistrement — en combinaison avec le paramètre `"editor.formatOnSave"` de VS Code.

Vous pouvez choisir de désactiver le formatage automatique pour certains langages spécifiques en définissant `vetur.format.defaultFormatter.XXXXX` sur `none` dans les paramètres de VS Code. Pour modifier l'un de ces paramètres, commencez simplement à rechercher la chaîne, et remplacez ce que vous voulez dans les paramètres utilisateur du panneau de droite.

La plupart des langages pris en charge utilisent [Prettier](https://prettier.io/) pour le formatage automatique, un outil qui devient une norme de l'industrie. Il utilise votre configuration Prettier pour déterminer vos préférences.

### Introduction aux composants Vue

Les composants sont des unités indépendantes d'une interface. Ils peuvent avoir leur propre état, balisage et style.

#### Comment utiliser les composants

Les composants Vue peuvent être définis de quatre manières principales. Parlons en code.

La première est :

```
new Vue({  /* options */})
```

La deuxième est :

```
Vue.component('component-name', {  /* options */})
```

La troisième est en utilisant des composants locaux. Ce sont des composants qui ne sont accessibles que par un composant spécifique, et non disponibles ailleurs (idéal pour l'encapsulation).

La quatrième est dans les fichiers `.vue`, également appelés composants mono-fichier.

Plongeons dans les trois premières méthodes en détail.

L'utilisation de `new Vue()` ou `Vue.component()` est la méthode standard pour utiliser Vue lorsque vous construisez une application qui n'est pas une application monopage (SPA). Vous utilisez cette méthode, plutôt, lorsque vous utilisez simplement Vue.js dans certaines pages, comme dans un formulaire de contact ou dans le panier d'achat. Ou peut-être que Vue est utilisé dans toutes les pages, mais le serveur rend la mise en page, et vous servez le HTML au client, qui charge ensuite l'application Vue que vous construisez.

Dans une SPA, où c'est Vue qui construit le HTML, il est plus courant d'utiliser des composants mono-fichier car ils sont plus pratiques.

Vous instanciez Vue en le montant sur un élément DOM. Si vous avez une balise `<div id="app">`</div>, vous utiliserez :

```
new Vue({ el: '#app' })
```

Un composant initialisé avec `new Vue` n'a pas de nom de balise correspondant, donc c'est généralement le composant conteneur principal.

D'autres composants utilisés dans l'application sont initialisés en utilisant `Vue.component()`. Un tel composant vous permet de définir une balise — avec laquelle vous pouvez intégrer le composant plusieurs fois dans l'application — et de spécifier la sortie du composant dans la propriété `template` :

```
<div id="app">  <user-name name="Flavio"></user-name></div>
```

```
Vue.component('user-name', {  props: ['name'],  template: '<p>Hi {{ name }}</p>'})
```

```
new Vue({  el: '#app'})
```

[Voir sur JSFiddle](https://jsfiddle.net/flaviocopes/nvgedhq4/)

Que faisons-nous ? Nous initialisons un composant racine Vue sur `#app`, et à l'intérieur de celui-ci, nous utilisons le composant Vue `user-name`, qui abstrait notre salutation à l'utilisateur.

Le composant accepte une prop, qui est un attribut que nous utilisons pour transmettre des données aux composants enfants.

Dans l'appel `Vue.component()`, nous avons passé `user-name` comme premier paramètre. Cela donne un nom au composant. Vous pouvez écrire le nom de deux manières ici. La première est celle que nous avons utilisée, appelée kebab-case. La seconde est appelée PascalCase, qui est comme camelCase, mais avec la première lettre en majuscule :

```
Vue.component('UserName', {  /* ... */})
```

Vue crée automatiquement un alias interne de `user-name` à `UserName`, et vice versa, donc vous pouvez utiliser ce que vous préférez. Il est généralement préférable d'utiliser `UserName` en JavaScript, et `user-name` dans le template.

#### Composants locaux

Tout composant créé en utilisant `Vue.component()` est enregistré globalement. Vous n'avez pas besoin de l'assigner à une variable ou de le transmettre pour le réutiliser dans vos templates.

Vous pouvez encapsuler des composants localement en assignant un objet qui définit l'objet composant à une variable :

```
const Sidebar = {  template: '<aside>Sidebar</aside>'}
```

et ensuite le rendre disponible à l'intérieur d'un autre composant en utilisant la propriété `components` :

```
new Vue({  el: '#app',  components: {    Sidebar  }})
```

Vous pouvez écrire le composant dans le même fichier, mais une excellente façon de faire cela est d'utiliser des modules JavaScript :

```
import Sidebar from './Sidebar'
```

```
export default {  el: '#app',  components: {    Sidebar  }}
```

#### Réutiliser un composant

Un composant enfant peut être ajouté plusieurs fois. Chaque instance séparée est indépendante des autres :

```
<div id="app">  <user-name name="Flavio"></user-name>  <user-name name="Roger"></user-name>  <user-name name="Syd"></user-name></div>
```

```
Vue.component('user-name', {  props: ['name'],  template: '<p>Hi {{ name }}</p>'})
```

```
new Vue({  el: '#app'})
```

[Voir sur JSFiddle](https://jsfiddle.net/flaviocopes/3kebv908/)

#### Les éléments constitutifs d'un composant

Jusqu'à présent, nous avons vu comment un composant peut accepter les propriétés `el`, `props` et `template`.

* `el` n'est utilisé que dans les composants racine initialisés avec `new Vue({})`, et identifie l'élément DOM sur lequel le composant sera monté.
* `props` liste toutes les propriétés que nous pouvons transmettre à un composant enfant
* `template` est l'endroit où nous pouvons configurer le template du composant, qui sera responsable de la définition de la sortie générée par le composant.

Un composant accepte d'autres propriétés :

* `data` l'état local du composant
* `methods` : les méthodes du composant
* `computed` : les propriétés calculées associées au composant
* `watch` : les observateurs du composant

### Composants mono-fichier

Un composant Vue peut être déclaré dans un fichier JavaScript (`.js`) comme ceci :

```
Vue.component('component-name', {  /* options */})
```

ou aussi :

```
new Vue({  /* options */})
```

ou il peut être spécifié dans un fichier `.vue`.

Le fichier `.vue` est assez cool car il vous permet de définir :

* La logique JavaScript
* Le template de code HTML
* Le style CSS

tout cela dans un seul fichier. À ce titre, il a été nommé Composant Mono-Fichier.

Voici un exemple :

```
<template>  <p>{{ hello }}</p></template>
```

```
<script>export default {  data() {    return {      hello: 'Hello World!'    }  }}</script>
```

```
<style scoped>  p {    color: blue;  }</style>
```

Tout cela est possible grâce à l'utilisation de Webpack. Le Vue CLI rend cela très facile et pris en charge dès la sortie de la boîte. Les fichiers `.vue` ne peuvent pas être utilisés sans une configuration Webpack, et à ce titre, ils ne sont pas très adaptés aux applications qui utilisent simplement Vue sur une page sans être une application monopage complète (SPA).

Puisque les composants mono-fichier reposent sur Webpack, nous obtenons gratuitement la capacité d'utiliser les fonctionnalités Web modernes.

Votre CSS peut être défini en utilisant SCSS ou Stylus, le template peut être construit en utilisant Pug, et tout ce que vous avez à faire pour que cela se produise est de déclarer à Vue quel préprocesseur de langage vous allez utiliser.

La liste des préprocesseurs pris en charge comprend

* TypeScript
* SCSS
* Sass
* Less
* PostCSS
* Pug

Nous pouvons utiliser JavaScript moderne (ES678) indépendamment du navigateur cible en utilisant l'intégration de Babel, et également les modules ES, afin que nous puissions utiliser les instructions `import/export`.

Nous pouvons utiliser les modules CSS pour scopé notre CSS.

En parlant de scopé CSS, les composants mono-fichier rendent absolument facile l'écriture de CSS qui ne **fuiera** pas vers d'autres composants, en utilisant des balises `<style scop`ed>.

Si vous omettez `scoped`, le CSS que vous définissez sera global. Mais en ajoutant la balise `scoped`, Vue ajoute automatiquement une classe spécifique au composant, unique à votre application, de sorte que le CSS est garanti de ne pas fuir vers d'autres composants.

Peut-être que votre JavaScript est énorme à cause d'une logique dont vous devez vous occuper. Que faire si vous voulez utiliser un fichier séparé pour votre JavaScript ?

Vous pouvez utiliser l'attribut `src` pour l'externaliser :

```
<template>  <p>{{ hello }}</p></template><script src="./hello.js"></script>
```

Cela fonctionne également pour votre CSS :

```
<template>  <p>{{ hello }}</p></template><script src="./hello.js"></script><style src="./hello.css"></style>
```

Remarquez comment j'ai utilisé

```
export default {  data() {    return {      hello: 'Hello World!'    }  }}
```

dans le JavaScript du composant pour configurer les données.

D'autres façons courantes que vous verrez sont :

```
export default {  data: function() {    return {      name: 'Flavio'    }  }}
```

Ce qui précède est équivalent à ce que nous avons fait avant.

Ou :

```
export default {  data: () => {    return {      name: 'Flavio'    }  }}
```

Cela est différent, car il utilise une fonction fléchée. Les fonctions fléchées sont bien jusqu'à ce que nous ayons besoin d'accéder à une méthode de composant. C'est un problème si nous devons utiliser `this`, et une telle propriété n'est pas liée au composant en utilisant des fonctions fléchées. Il est donc obligatoire d'utiliser des fonctions **régulières** plutôt que des fonctions fléchées.

Vous pourriez également voir :

```
module.exports = {  data: () => {    return {      name: 'Flavio'    }  }}
```

Cela utilise la syntaxe [CommonJS](http://requirejs.org/docs/commonjs.html) et cela fonctionne également. Mais je recommande d'utiliser la syntaxe des modules ES, car c'est une norme JavaScript.

### Modèles Vue

Vue.js utilise un langage de templating qui est un sur-ensemble de HTML.

Tout HTML est un modèle Vue.js valide. En plus de cela, Vue.js fournit deux choses puissantes : l'interpolation et les directives.

Ceci est un modèle Vue.js valide :

```
<span>Bonjour !</span>
```

Ce modèle peut être placé à l'intérieur d'un composant Vue déclaré explicitement :

```
new Vue({  template: '<span>Bonjour !</span>'})
```

ou il peut être placé dans un composant mono-fichier :

```
<template>  <span>Bonjour !</span></template>
```

Ce premier exemple est très basique. L'étape suivante consiste à le faire afficher une partie de l'état du composant, par exemple, un nom.

Cela peut être fait en utilisant l'interpolation. Tout d'abord, nous ajoutons quelques données à notre composant :

```js
new Vue({  
  data: {    
    name: 'Flavio'  
  },  
  template: '<span>Bonjour !</span>'
})
```

et ensuite nous pouvons l'ajouter à notre modèle en utilisant la syntaxe des doubles crochets :

```
new Vue({  data: {    name: 'Flavio'  },  template: '<span>Bonjour {{name}} !</span>'})
```

Une chose intéressante ici. Voyez comment nous avons simplement utilisé `name` au lieu de `this.data.name` ?

C'est parce que Vue.js fait une liaison interne et permet au modèle d'utiliser la propriété comme si elle était locale. Très pratique.

Dans un composant mono-fichier, cela serait :

```
<template>  <span>Bonjour {{name}} !</span></template>
```

```
<script>export default {  data() {    return {      name: 'Flavio'    }  }}</script>
```

J'ai utilisé une fonction régulière dans mon export. Pourquoi pas une fonction fléchée ?

C'est parce que dans `data`, nous pourrions avoir besoin d'accéder à une méthode dans notre instance de composant, et nous ne pouvons pas le faire si `this` n'est pas lié au composant, donc nous ne pouvons pas utiliser une fonction fléchée.

Notez que nous pourrions utiliser une fonction fléchée, mais alors je devrais me souvenir de passer à une fonction régulière si j'utilise `this`. Mieux vaut jouer la sécurité, je pense.

Maintenant, revenons à l'interpolation.

`{{ name }}` devrait vous rappeler l'interpolation de template Mustache / Handlebars, mais ce n'est qu'un rappel visuel.

Alors que dans ces moteurs de templating ils sont "stupides", dans Vue, vous pouvez faire beaucoup plus, et c'est plus flexible.

Vous pouvez utiliser n'importe quelle expression JavaScript à l'intérieur de vos interpolations, mais vous êtes limité à une seule expression :

```
{{ name.reverse() }}
```

```
{{ name === 'Flavio' ? 'Flavio' : 'inconnu' }}
```

Vue fournit l'accès à certains objets globaux à l'intérieur des templates, y compris Math et Date, donc vous pouvez les utiliser :

```
{{ Math.sqrt(16) * Math.random() }}
```

Il est préférable d'éviter d'ajouter une logique complexe aux templates, mais le fait que Vue le permette nous donne plus de flexibilité, surtout lorsque nous essayons des choses.

Nous pouvons d'abord essayer de mettre une expression dans le template, puis la déplacer vers une propriété calculée ou une méthode plus tard.

La valeur incluse dans toute interpolation sera mise à jour lors d'un changement de l'une des propriétés de données dont elle dépend.

Vous pouvez éviter cette réactivité en utilisant la directive `v-once`.

Le résultat est toujours échappé, donc vous ne pouvez pas avoir de HTML dans la sortie.

Si vous avez besoin d'avoir un extrait HTML, vous devez utiliser la directive `v-html` à la place.

### Styliser les composants en utilisant CSS

L'option la plus simple pour ajouter du CSS à un composant Vue.js est d'utiliser la balise `style`, tout comme en HTML :

```
<template>  <p style="text-decoration: underline">Salut !</p></template>
```

```
<script>export default {  data() {    return {      decoration: 'underline'    }  }}</script>
```

C'est aussi statique que possible. Que faire si vous voulez que `underline` soit défini dans les données du composant ? Voici comment vous pouvez le faire :

```
<template>  <p :style="{'text-decoration': decoration}">Salut !</p></template>
```

```
<script>export default {  data() {    return {      decoration: 'underline'    }  }}</script>
```

`:style` est un raccourci pour `v-bind:style`. J'utiliserai ce raccourci tout au long de ce tutoriel.

Remarquez comment nous avons dû envelopper `text-decoration` dans des guillemets. Cela est dû au tiret, qui ne fait pas partie d'un identifiant JavaScript valide.

Vous pouvez éviter les guillemets en utilisant une syntaxe camelCase spéciale que Vue.js permet, et en le réécrivant en `textDecoration` :

```
<template>  <p :style="{textDecoration: decoration}">Salut !</p></template>
```

Au lieu de lier un objet à `style`, vous pouvez référencer une propriété calculée :

```
<template>  <p :style="styling">Salut !</p></template>
```

```
<script>export default {  data() {    return {      textDecoration: 'underline',      textWeight: 'bold'    }  },  computed: {    styling: function() {      return {        textDecoration: this.textDecoration,        textWeight: this.textWeight      }    }  }}</script>
```

Les composants Vue génèrent du HTML simple, donc vous pouvez choisir d'ajouter une classe à chaque élément, et d'ajouter un sélecteur CSS correspondant avec des propriétés qui le stylisent :

```
<template>  <p class="underline">Salut !</p></template>
```

```
<style>.underline { text-decoration: underline; }</style>
```

Vous pouvez utiliser SCSS comme ceci :

```
<template>  <p class="underline">Salut !</p></template>
```

```
<style lang="scss">body {  .underline { text-decoration: underline; }}</style>
```

Vous pouvez coder en dur la classe comme dans l'exemple ci-dessus. Ou vous pouvez lier la classe à une propriété de composant, pour la rendre dynamique, et ne l'appliquer que si la propriété de données est vraie :

```
<template>  <p :class="{underline: isUnderlined}">Salut !</p></template>
```

```
<script>export default {  data() {    return {      isUnderlined: true    }  }}</script>
```

```
<style>.underline { text-decoration: underline; }</style>
```

Au lieu de lier un objet à la classe, comme nous l'avons fait avec `<p :class="{text: isText}">H`i!</p>, vous pouvez directement lier une chaîne, et cela référencera une propriété de données :

```
<template>  <p :class="paragraphClass">Salut !</p></template>
```

```
<script>export default {  data() {    return {      paragraphClass: 'underline'    }  }}</script>
```

```
<style>.underline { text-decoration: underline; }</style>
```

Vous pouvez attribuer plusieurs classes, soit en ajoutant deux classes à `paragraphClass` dans ce cas, soit en utilisant un tableau :

```
<template>  <p :class="[decoration, weight]">Salut !</p></template>
```

```
<script>export default {  data() {    return {      decoration: 'underline',      weight: 'weight',    }  }}</script>
```

```
<style>.underline { text-decoration: underline; }.weight { font-weight: bold; }</style>
```

La même chose peut être faite en utilisant un objet en ligne dans la liaison de classe :

```
<template>  <p :class="{underline: isUnderlined, weight: isBold}">Salut !</p></template>
```

```
<script>export default {  data() {    return {      isUnderlined: true,      isBold: true    }  }}</script>
```

```
<style>.underline { text-decoration: underline; }.weight { font-weight: bold; }</style>
```

Et vous pouvez combiner les deux déclarations :

```
<template>  <p :class="[decoration, {weight: isBold}]">Salut !</p></template>
```

```
<script>export default {  data() {    return {      decoration: 'underline',      isBold: true    }  }}</script>
```

```
<style>.underline { text-decoration: underline; }.weight { font-weight: bold; }</style>
```

Vous pouvez également utiliser une propriété calculée qui retourne un objet, ce qui fonctionne mieux lorsque vous avez de nombreuses classes CSS à ajouter au même élément :

```
<template>  <p :class="paragraphClasses">Salut !</p></template>
```

```
<script>export default {  data() {    return {      isUnderlined: true,      isBold: true    }  },  computed: {    paragraphClasses: function() {      return {        underlined: this.isUnderlined,        bold: this.isBold      }    }  }}</script>
```

```
<style>.underlined { text-decoration: underline; }.bold { font-weight: bold; }</style>
```

Remarquez que dans la propriété calculée, vous devez référencer les données du composant en utilisant `this.[propertyName]`, tandis que dans les données du template, les propriétés sont commodément placées comme propriétés de premier niveau.

Tout CSS qui n'est pas codé en dur comme dans le premier exemple va être traité par Vue, et Vue fait le travail agréable de préfixer automatiquement le CSS pour nous. Cela nous permet d'écrire du CSS propre tout en ciblant les anciens navigateurs (ce qui signifie toujours les navigateurs que Vue supporte, donc IE9+).

### Directives

Nous avons vu dans les templates et interpolations Vue.js comment vous pouvez intégrer des données dans les templates Vue.

Cette section explique l'autre technique offerte par Vue.js dans les templates : les directives.

Les directives sont essentiellement comme des attributs HTML qui sont ajoutés à l'intérieur des templates. Ils commencent tous par `v-`, pour indiquer qu'il s'agit d'un attribut spécial de Vue.

Voyons chaque directive Vue en détail.

#### `v-text`

Au lieu d'utiliser l'interpolation, vous pouvez utiliser la directive `v-text`. Elle effectue le même travail :

```
<span v-text="name"></span>
```

#### `v-once`

Vous savez comment `{{ name }}` se lie à la propriété `name` des données du composant.

À chaque fois que `name` change dans vos données de composant, Vue va mettre à jour la valeur représentée dans le navigateur.

Sauf si vous utilisez la directive `v-once`, qui est essentiellement comme un attribut HTML :

```
<span v-once>{{ name }}</span>
```

#### `v-html`

Lorsque vous utilisez l'interpolation pour imprimer une propriété de données, le HTML est échappé. C'est une excellente façon que Vue utilise pour se protéger automatiquement des attaques XSS.

Il y a des cas, cependant, où vous voulez sortir du HTML et faire en sorte que le navigateur l'interprète. Vous pouvez utiliser la directive `v-html` :

```
<span v-html="someHtml"></span>
```

#### `v-bind`

L'interpolation ne fonctionne que dans le contenu de la balise. Vous ne pouvez pas l'utiliser sur les attributs.

Les attributs doivent utiliser `v-bind` :

```
<a v-bind:href="url">{{ linkText }}</a>
```

`v-bind` est si courant qu'il existe une syntaxe abrégée pour cela :

```
<a v-bind:href="url">{{ linkText }}</a><a :href="url">{{ linkText }}</a>
```

#### Liaison bidirectionnelle utilisant `v-model`

`v-model` nous permet de lier un élément de formulaire d'entrée par exemple, et le fait changer la propriété de données Vue lorsque l'utilisateur change le contenu du champ :

```
<input v-model="message" placeholder="Entrez un message"><p>Le message est : {{ message }}</p>
```

```
<select v-model="selected">  <option disabled value="">Choisissez un fruit</option>  <option>Pomme</option>  <option>Banane</option>  <option>Fraise</option></select><span>Fruit choisi : {{ selected }}</span>
```

#### Utilisation d'expressions

Vous pouvez utiliser n'importe quelle expression JavaScript à l'intérieur d'une directive :

```
<span v-text="'Bonjour, ' + name + '!'"></span>
```

```
<a v-bind:href="'https://' + domain + path">{{ linkText }}</a>
```

Toute variable utilisée dans une directive référence la propriété de données correspondante.

#### Conditionnelles

À l'intérieur d'une directive, vous pouvez utiliser l'opérateur ternaire pour effectuer une vérification conditionnelle, puisque c'est une expression :

```
<span v-text="name == Flavio ? 'Bonjour Flavio!' : 'Bonjour' + name + '!'"></span>
```

Il existe des directives dédiées qui vous permettent d'effectuer des conditionnelles plus organisées : `v-if`, `v-else` et `v-else-if`.

```
<p v-if="shouldShowThis">Hey!</p>
```

`shouldShowThis` est une valeur booléenne contenue dans les données du composant.

#### Boucles

`v-for` vous permet de rendre une liste d'éléments. Utilisez-le en combinaison avec `v-bind` pour définir les propriétés de chaque élément de la liste.

Vous pouvez itérer sur un simple tableau de valeurs :

```
<template>  <ul>    <li v-for="item in items">{{ item }}</li>  </ul></template>
```

```
<script>export default {  data() {    return {      items: ['car', 'bike', 'dog']    }  }}</script>
```

Ou sur un tableau d'objets :

```
<template>  <div>    <!-- en utilisant l'interpolation -->    <ul>      <li v-for="todo in todos">{{ todo.title }}</li>    </ul>    <!-- en utilisant v-text -->    <ul>      <li v-for="todo in todos" v-text="todo.title"></li>    </ul>  </div></template>
```

```
<script>export default {  data() {    return {      todos: [        { id: 1, title: 'Do something' },        { id: 2, title: 'Do something else' }      ]    }  }}</script>
```

`v-for` peut vous donner l'index en utilisant :

```
<li v-for="(todo, index) in todos"></li>
```

#### Événements

`v-on` vous permet d'écouter les événements DOM, et de déclencher une méthode lorsque l'événement se produit. Ici, nous écoutons un événement de clic :

```
<template>  <a v-on:click="handleClick">Cliquez-moi !</a></template>
```

```
<script>export default {  methods: {    handleClick: function() {      alert('test')    }  }}</script>
```

Vous pouvez passer des paramètres à n'importe quel événement :

```
<template>  <a v-on:click="handleClick('test')">Cliquez-moi !</a></template>
```

```
<script>export default {  methods: {    handleClick: function(value) {      alert(value)    }  }}</script>
```

De petits morceaux de JavaScript (une seule expression) peuvent être placés directement dans le modèle :

```
<template>  <a v-on:click="counter = counter + 1">{{counter}}</a></template>
```

```
<script>export default {  data: function() {    return {      counter: 0    }  }}</script>
```

`click` n'est qu'un type d'événement. Un événement courant est `submit`, que vous pouvez lier en utilisant `v-on:submit`.

`v-on` est si courant qu'il existe une syntaxe abrégée pour cela, `@` :

```
<a v-on:click="handleClick">Cliquez-moi !</a><a @click="handleClick">Cliquez-moi !</a>
```

#### Afficher ou masquer

Vous pouvez choisir de n'afficher un élément dans le DOM que si une propriété particulière de l'instance Vue évalue à vrai, en utilisant `v-show` :

```
<p v-show="isTrue">Quelque chose</p>
```

L'élément est toujours inséré dans le DOM, mais défini sur `display: none` si la condition n'est pas satisfaite.

#### Modificateurs de directives d'événement

Vue offre certains modificateurs d'événement optionnels que vous pouvez utiliser en association avec `v-on`, qui font automatiquement faire quelque chose à l'événement sans que vous ayez à le coder explicitement dans votre gestionnaire d'événement.

Un bon exemple est `.prevent`, qui appelle automatiquement `preventDefault()` sur l'événement.

Dans ce cas, le formulaire ne provoque pas le rechargement de la page, ce qui est le comportement par défaut :

```
<form v-on:submit.prevent="formSubmitted"></form>
```

D'autres modificateurs incluent `.stop`, `.capture`, `.self`, `.once`, `.passive` et ils sont [décrits en détail dans la documentation officielle](https://vuejs.org/v2/guide/events.html#Event-Modifiers).

#### Directives personnalisées

Les directives par défaut de Vue vous permettent déjà de faire beaucoup de travail, mais vous pouvez toujours ajouter de nouvelles directives personnalisées si vous le souhaitez.

Lisez [ici](https://vuejs.org/v2/guide/custom-directive.html) si vous êtes intéressé à en apprendre plus.

### Méthodes

#### Qu'est-ce que les méthodes Vue.js ?

Une méthode Vue est une fonction associée à l'instance Vue.

Les méthodes sont définies à l'intérieur de la propriété `methods` :

```
new Vue({  methods: {    handleClick: function() {      alert('test')    }  }})
```

ou dans le cas des composants mono-fichier :

```
<script>export default {  methods: {    handleClick: function() {      alert('test')    }  }}</script>
```

Les méthodes sont particulièrement utiles lorsque vous devez effectuer une action et que vous attachez une directive `v-on` sur un élément pour gérer les événements. Comme ceci, qui appelle `handleClick` lorsque l'élément est cliqué :

```
<template>  <a @click="handleClick">Cliquez-moi !</a></template>
```

#### Passer des paramètres aux méthodes Vue.js

Les méthodes peuvent accepter des paramètres.

Dans ce cas, vous passez simplement le paramètre dans le template :

```
<template>  <a @click="handleClick('quelque chose')">Cliquez-moi !</a></template>
```

```
new Vue({  methods: {    handleClick: function(text) {      alert(text)    }  }})
```

ou dans le cas des composants mono-fichier :

```
<script>export default {  methods: {    handleClick: function(text) {      alert(text)    }  }}</script>
```

#### Comment accéder aux données depuis une méthode

Vous pouvez accéder à n'importe quelle propriété de données du composant Vue en utilisant `this.propertyName` :

```
<template>  <a @click="handleClick()">Cliquez-moi !</a></template>
```

```
<script>export default {  data() {    return {      name: 'Flavio'    }  },  methods: {    handleClick: function() {      console.log(this.name)    }  }}</script>
```

Nous n'avons pas besoin d'utiliser `this.data.name`, juste `this.name`. Vue fournit une liaison transparente pour nous. L'utilisation de `this.data.name` générera une erreur.

Comme vous l'avez vu précédemment dans la description des **événements**, les méthodes sont étroitement liées aux événements, car elles sont utilisées comme gestionnaires d'événements. Chaque fois qu'un événement se produit, cette méthode est appelée.

### Observateurs

Un observateur est une fonctionnalité spéciale de Vue.js qui vous permet d'espionner une propriété de l'état du composant et d'exécuter une fonction lorsque la valeur de cette propriété change.

Voici un exemple. Nous avons un composant qui affiche un nom et permet de le changer en cliquant sur un bouton :

```
<template>  <p>Mon nom est {{name}}</p>  <button @click="changeName()">Changez mon nom !</button></template>
```

```
<script>export default {  data() {    return {      name: 'Flavio'    }  },  methods: {    changeName: function() {      this.name = 'Flavius'    }  }}</script>
```

Lorsque le nom change, nous voulons faire quelque chose, comme afficher un journal de la console.

Nous pouvons le faire en ajoutant à l'objet `watch` une propriété nommée comme la propriété de données que nous voulons surveiller :

```
<script>export default {  data() {    return {      name: 'Flavio'    }  },  methods: {    changeName: function() {      this.name = 'Flavius'    }  },  watch: {    name: function() {      console.log(this.name)    }  }}</script>
```

La fonction assignée à `watch.name` peut accepter optionnellement 2 paramètres. Le premier est la nouvelle valeur de la propriété. Le second est l'ancienne valeur de la propriété :

```
<script>export default {  /* ... */  watch: {    name: function(newValue, oldValue) {      console.log(newValue, oldValue)    }  }}</script>
```

Les observateurs ne peuvent pas être recherchés à partir d'un modèle comme vous pouvez le faire avec les propriétés calculées.

### Propriétés calculées

#### Qu'est-ce qu'une propriété calculée

Dans Vue.js, vous pouvez afficher n'importe quelle valeur de données en utilisant des parenthèses :

```
<template>  <p>{{ count }}</p></template>
```

```
<script>export default {  data() {    return {      count: 1    }  }}</script>
```

Cette propriété peut héberger quelques petits calculs. Par exemple :

```
<template>  {{ count * 10 }}</template>
```

Mais vous êtes limité à une seule expression JavaScript.

En plus de cette limitation technique, vous devez également considérer que les modèles ne doivent s'occuper que de l'affichage des données à l'utilisateur, et non de l'exécution de calculs logiques.

Pour faire quelque chose de plus qu'une seule expression, et pour avoir des modèles plus déclaratifs, vous utilisez une propriété calculée.

Les propriétés calculées sont définies dans la propriété `computed` du composant Vue :

```
<script>export default {  computed: {
```

```
  }}</script>
```

#### Un exemple de propriété calculée

Voici un exemple qui utilise une propriété calculée `count` pour calculer la sortie.

Remarquez :

1. Je n'ai pas eu à appeler `{{ count() }}`. Vue.js appelle automatiquement la fonction
2. J'ai utilisé une fonction régulière (et non une fonction fléchée) pour définir la propriété calculée `count`, car j'ai besoin de pouvoir accéder à l'instance du composant via `this`.

```
<template>  <p>{{ count }}</p></template>
```

```
<script>export default {  data() {    return {      items: [1, 2, 3]    }  },  computed: {    count: function() {      return 'Le compte est ' + this.items.length * 10    }  }}</script>
```

#### Propriétés calculées vs. méthodes

Si vous connaissez déjà les méthodes Vue, vous vous demandez peut-être quelle est la différence.

Tout d'abord, les méthodes doivent être appelées, pas seulement référencées, donc vous devriez faire :

```
<template>  <p>{{ count() }}</p></template>
```

```
<script>export default {  data() {    return {      items: [1, 2, 3]    }  },  methods: {    count: function() {      return 'Le compte est ' + this.items.length * 10    }  }}</script>
```

Mais la principale différence est que les propriétés calculées sont mises en cache.

Le résultat de la propriété calculée `count` est mis en cache en interne jusqu'à ce que la propriété de données `items` change.

**Important :** Les propriétés calculées ne sont mises à jour que lorsqu'une source réactive est mise à jour. Les méthodes JavaScript régulières ne sont pas réactives, donc un exemple courant est d'utiliser `Date.now()` :

```
<template>  <p>{{ now }}</p></template>
```

```
<script>export default {  computed: {    now: function () {      return Date.now()    }  }}</script>
```

Il sera rendu une fois, puis il ne sera pas mis à jour même lorsque le composant est re-rendu. Il n'est mis à jour qu'à l'actualisation de la page, lorsque le composant Vue est quitté et réinitialisé.

Dans ce cas, une méthode est mieux adaptée à vos besoins.

### Méthodes vs. Observateurs vs. Propriétés calculées

Maintenant que vous connaissez les méthodes, les observateurs et les propriétés calculées, vous vous demandez peut-être quand utiliser l'un plutôt que les autres.

Voici une analyse de cette question.

#### Quand utiliser les méthodes

* Pour réagir à un événement se produisant dans le DOM
* Pour appeler une fonction lorsque quelque chose se produit dans votre composant.
Vous pouvez appeler une méthode à partir de propriétés calculées ou d'observateurs.

#### Quand utiliser les propriétés calculées

* Vous avez besoin de composer de nouvelles données à partir de sources de données existantes
* Vous avez une variable que vous utilisez dans votre template qui est construite à partir d'une ou plusieurs propriétés de données
* Vous voulez réduire un nom de propriété compliqué et imbriqué à un nom plus lisible et facile à utiliser (mais le mettre à jour lorsque la propriété d'origine change)
* Vous avez besoin de référencer une valeur à partir du template. Dans ce cas, créer une propriété calculée est la meilleure chose, car elle est mise en cache.
* Vous avez besoin d'écouter les changements de plus d'une propriété de données

#### Quand utiliser les observateurs

* Vous voulez écouter lorsqu'une propriété de données change, et effectuer une action
* Vous voulez écouter un changement de valeur de prop
* Vous n'avez besoin d'écouter qu'une propriété spécifique (vous ne pouvez pas surveiller plusieurs propriétés en même temps)
* Vous voulez surveiller une propriété de données jusqu'à ce qu'elle atteigne une valeur spécifique et ensuite faire quelque chose

### Props : passer des données aux composants enfants

Les props sont la manière dont les composants peuvent accepter des données des composants qui les incluent (composants parents).

Lorsque qu'un composant attend une ou plusieurs props, il doit les définir dans sa propriété `props` :

```
Vue.component('user-name', {  props: ['name'],  template: '<p>Hi {{ name }}</p>'})
```

ou, dans un composant mono-fichier Vue :

```
<template>  <p>{{ name }}</p></template>
```

```
<script>export default {  props: ['name']}</script>
```

#### Accepter plusieurs props

Vous pouvez avoir plusieurs props en les ajoutant simplement au tableau :

```
Vue.component('user-name', {  props: ['firstName', 'lastName'],  template: '<p>Hi {{ firstName }} {{ lastName }}</p>'})
```

#### Définir le type de prop

Vous pouvez spécifier le type d'une prop très simplement en utilisant un objet au lieu d'un tableau, en utilisant le nom de la propriété comme clé de chaque propriété, et le type comme valeur :

```
Vue.component('user-name', {  props: {    firstName: String,    lastName: String  },  template: '<p>Hi {{ firstName }} {{ lastName }}</p>'})
```

Les types valides que vous pouvez utiliser sont :

* String
* Number
* Boolean
* Array
* Object
* Date
* Function
* Symbol

Lorsque le type ne correspond pas, Vue vous alerte (en mode développement) dans la console avec un avertissement.

Les types de props peuvent être plus articulés.

Vous pouvez autoriser plusieurs types de valeurs différentes :

```
props: {  firstName: [String, Number]}
```

#### Définir une prop comme obligatoire

Vous pouvez rendre une prop obligatoire :

```
props: {  firstName: {    type: String,    required: true  }}
```

#### Définir la valeur par défaut d'une prop

Vous pouvez spécifier une valeur par défaut :

```
props: {  firstName: {    type: String,    default: 'Unknown person'  }}
```

Pour les objets :

```
props: {  name: {    type: Object,    default: {      firstName: 'Unknown',      lastName: ''    }  }}
```

`default` peut également être une fonction qui retourne une valeur appropriée, plutôt que d'être la valeur réelle.

Vous pouvez même créer un validateur personnalisé, ce qui est cool pour les données complexes :

```
props: {  name: {    validator: name => {      return name === 'Flavio' //seuls les "Flavios" sont autorisés    }  }}
```

#### Passer des props au composant

Vous passez une prop à un composant en utilisant la syntaxe

```
<ComponentName color="white" />
```

si ce que vous passez est une valeur statique.

Si c'est une propriété de données, vous utilisez

```
<template>  <ComponentName :color=color /></template>
```

```
<script>...export default {  //...  data: function() {    return {      color: 'white'    }  },  //...}</script>
```

Vous pouvez utiliser un opérateur ternaire à l'intérieur de la valeur de la prop pour vérifier une condition vraie et passer une valeur qui en dépend :

```
<template>  <ComponentName :colored="color == 'white' ? true : false" /></template>
```

```
<script>...export default {  //...  data: function() {    return {      color: 'white'    }  },  //...}</script>
```

### Gestion des événements dans Vue

#### Qu'est-ce que les événements Vue.js ?

Vue.js nous permet d'intercepter tout événement DOM en utilisant la directive `v-on` sur un élément.

Si nous voulons faire quelque chose lorsqu'un événement de clic se produit dans cet élément :

```
<template>  <a>Cliquez-moi !</a></template>
```

nous ajoutons une directive `v-on` :

```
<template>  <a v-on:click="handleClick">Cliquez-moi !</a></template>
```

Vue offre également une syntaxe alternative très pratique pour cela :

```
<template>  <a @click="handleClick">Cliquez-moi !</a></template>
```

Vous pouvez choisir d'utiliser les parenthèses ou non. `@click="handleClick"` est équivalent à `@click="handleClick()"`.

`handleClick` est une méthode attachée au composant :

```
<script>export default {  methods: {    handleClick: function(event) {      console.log(event)    }  }}</script>
```

Ce que vous devez savoir ici, c'est que vous pouvez passer des paramètres depuis les événements : `@click="handleClick(param)"` et ils seront reçus à l'intérieur de la méthode.

#### Accéder à l'objet événement d'origine

Dans de nombreux cas, vous voudrez effectuer une action sur l'objet événement ou rechercher une propriété dans celui-ci. Comment pouvez-vous y accéder ?

Utilisez la directive spéciale `$event` :

```
<template>  <a @click="handleClick($event)">Cliquez-moi !</a></template>
```

```
<script>export default {  methods: {    handleClick: function(event) {      console.log(event)    }  }}</script>
```

et si vous passez déjà une variable :

```
<template>  <a @click="handleClick('quelque chose', $event)">Cliquez-moi !</a></template>
```

```
<script>export default {  methods: {    handleClick: function(text, event) {      console.log(text)      console.log(event)    }  }}</script>
```

À partir de là, vous pourriez appeler `event.preventDefault()`, mais il y a une meilleure façon : les modificateurs d'événement.

#### Modificateurs d'événement

Au lieu de manipuler des "choses" DOM dans vos méthodes, dites à Vue de gérer les choses pour vous :

* `@click.prevent` appelle `event.preventDefault()`
* `@click.stop` appelle `event.stopPropagation()`
* `@click.passive` utilise l'[option passive de addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener#Parameters)
* `@click.capture` utilise la capture d'événement au lieu de la remontée d'événement
* `@click.self` assure que l'événement de clic n'a pas été remonté depuis un événement enfant, mais s'est produit directement sur cet élément
* `@click.once` l'événement ne sera déclenché qu'exactement une fois

Toutes ces options peuvent être combinées en ajoutant un modificateur après l'autre.

Pour plus d'informations sur la propagation, la remontée et la capture, consultez mon [guide des événements JavaScript](https://flaviocopes.com/javascript-events).

### Injecter du contenu en utilisant des slots

Un composant peut choisir de définir entièrement son contenu, comme dans ce cas :

```
Vue.component('user-name', {  props: ['name'],  template: '<p>Hi {{ name }}</p>'})
```

Ou il peut également permettre au composant parent d'injecter n'importe quel type de contenu dans celui-ci, en utilisant des slots.

Qu'est-ce qu'un slot ?

Vous le définissez en mettant `<slot>&`lt;/slot> dans un template de composant :

```
Vue.component('user-information', {  template: '<div class="user-information"><slot></slot></div>'})
```

Lorsque vous utilisez ce composant, tout contenu ajouté entre la balise d'ouverture et de fermeture sera ajouté à l'intérieur du placeholder du slot :

```
<user-information>  <h2>Hi!</h2>  <user-name name="Flavio"></user-information>
```

Si vous mettez un contenu à côté des balises `<slot>&`lt;/slot>, cela sert de contenu par défaut au cas où rien n'est passé.

Une mise en page de composant compliquée peut nécessiter une meilleure façon d'organiser le contenu.

Entrez les **slots nommés**.

Avec un slot nommé, vous pouvez attribuer des parties d'un slot à une position spécifique dans la mise en page de votre template de composant, et vous utilisez un attribut `slot` sur n'importe quelle balise, pour attribuer du contenu à ce slot.

Tout ce qui est en dehors de toute balise de template est ajouté au `slot` principal.

Pour plus de commodité, j'utilise un composant mono-fichier `page` dans cet exemple :

```
<template>  <div>    <main>      <slot></slot>    </main>    <sidebar>      <slot name="sidebar"></slot>    </sidebar>  </div></template>
```

```
<page>  <ul slot="sidebar">    <li>Home</li>    <li>Contact</li>  </ul>
```

```
  <h2>Page title</h2>  <p>Page content</p></page>
```

### Filtres, aides pour les templates

Les filtres sont une fonctionnalité fournie par les composants Vue qui vous permettent d'appliquer un formatage et des transformations à n'importe quelle partie de vos données dynamiques de template.

Ils ne changent pas les données d'un composant ou quoi que ce soit, mais ils n'affectent que la sortie.

Supposons que vous imprimiez un nom :

```
<template>  <p>Bonjour {{ name }} !</p></template>
```

```
<script>export default {  data() {    return {      name: 'Flavio'    }  }}</script>
```

Que faire si vous voulez vérifier que `name` contient effectivement une valeur, et si ce n'est pas le cas, imprimer 'there', de sorte que notre template imprimera "Bonjour there !" ?

Entrez les filtres :

```
<template>  <p>Bonjour {{ name | fallback }} !</p></template>
```

```
<script>export default {  data() {    return {      name: 'Flavio'    }  },  filters: {    fallback: function(name) {      return name ? name : 'there'    }  }}</script>
```

Remarquez la syntaxe pour appliquer un filtre, qui est `| filterName`. Si vous êtes familier avec Unix, c'est l'opérateur de pipe Unix, qui est utilisé pour passer la sortie d'une opération comme entrée à la suivante.

La propriété `filters` du composant est un objet. Un seul filtre est une fonction qui accepte une valeur et retourne une autre valeur.

La valeur retournée est celle qui est réellement imprimée dans le template Vue.js.

Le filtre, bien sûr, a accès aux données et méthodes du composant.

Qu'est-ce qu'un bon cas d'utilisation pour les filtres ?

* transformer une chaîne, par exemple, la mettre en majuscules ou en minuscules
* formater un prix

Au-dessus, vous avez vu un exemple simple de filtre : `{{ name | fallback }}`.

Les filtres peuvent être enchaînés, en répétant la syntaxe de pipe :

```
{{ name | fallback | capitalize }}
```

Cela applique d'abord le filtre `fallback`, puis le filtre `capitalize` (que nous n'avons pas défini, mais essayez d'en créer un !).

Les filtres avancés peuvent également accepter des paramètres, en utilisant la syntaxe normale des paramètres de fonction :

```
<template>  <p>Bonjour {{ name | prepend('Dr.') }}</p></template>
```

```
<script>export default {  data() {    return {      name: 'House'    }  },  filters: {    prepend: (name, prefix) => {      return `${prefix} ${name}`    }  }}</script>
```

Si vous passez des paramètres à un filtre, le premier passé à la fonction de filtre est toujours l'élément dans l'interpolation de template (`name` dans ce cas), suivi des paramètres explicites que vous avez passés.

Vous pouvez utiliser plusieurs paramètres en les séparant par une virgule.

Remarquez que j'ai utilisé une fonction fléchée. Nous évitons les fonctions fléchées dans les méthodes et les propriétés calculées, généralement, car elles font presque toujours référence à `this` pour accéder aux données du composant. Mais dans ce cas, le filtre n'a pas besoin d'accéder à `this` mais reçoit toutes les données dont il a besoin via les paramètres, et nous pouvons utiliser en toute sécurité la syntaxe plus simple de la fonction fléchée.

[Ce package](https://www.npmjs.com/package/vue2-filters) contient de nombreux filtres pré-faits que vous pouvez utiliser directement dans les templates, qui incluent `capitalize`, `uppercase`, `lowercase`, `placeholder`, `truncate`, `currency`, `pluralize` et plus encore.

### Communication entre les composants

Les composants dans Vue peuvent communiquer de diverses manières.

#### Utilisation des Props

La première manière est en utilisant les props.

Les parents "transmettent" les données en ajoutant des arguments à la déclaration du composant :

```
<template>  <div>    <Car color="green" />  </div></template>
```

```
<script>import Car from './components/Car'
```

```
export default {  name: 'App',  components: {    Car  }}</script>
```

Les props sont à sens unique : du parent à l'enfant. Chaque fois que le parent change la prop, la nouvelle valeur est envoyée à l'enfant et re-rendue.

L'inverse n'est pas vrai, et vous ne devez jamais muter une prop à l'intérieur du composant enfant.

#### Utilisation des Événements pour communiquer des enfants au parent

Les événements permettent de communiquer des enfants vers le parent :

```
<script>export default {  name: 'Car',  methods: {    handleClick: function() {      this.$emit('clickedSomething')    }  }}</script>
```

Le parent peut intercepter cela en utilisant la directive `v-on` lors de l'inclusion du composant dans son template :

```
<template>  <div>    <Car v-on:clickedSomething="handleClickInParent" />    <!-- ou -->    <Car @clickedSomething="handleClickInParent" />  </div></template>
```

```
<script>export default {  name: 'App',  methods: {    handleClickInParent: function() {      //...    }  }}</script>
```

Vous pouvez passer des paramètres bien sûr :

```
<script>export default {  name: 'Car',  methods: {    handleClick: function() {      this.$emit('clickedSomething', param1, param2)    }  }}</script>
```

et les récupérer depuis le parent :

```
<template>  <div>    <Car v-on:clickedSomething="handleClickInParent" />    <!-- ou -->    <Car @clickedSomething="handleClickInParent" />  </div></template>
```

```
<script>export default {  name: 'App',  methods: {    handleClickInParent: function(param1, param2) {      //...    }  }}</script>
```

#### Utilisation d'un Event Bus pour communiquer entre n'importe quels composants

En utilisant des événements, vous n'êtes pas limité aux relations parent-enfant. Vous pouvez utiliser le soi-disant Event Bus.

Ci-dessus, nous avons utilisé `this.$emit` pour émettre un événement sur l'instance du composant.

Ce que nous pouvons faire à la place, c'est émettre l'événement sur un composant plus généralement accessible.

`this.$root`, le composant racine, est couramment utilisé pour cela.

Vous pouvez également créer un composant Vue dédié à ce travail, et l'importer là où vous en avez besoin.

```
<script>export default {  name: 'Car',  methods: {    handleClick: function() {      this.$root.$emit('clickedSomething')    }  }}</script>
```

N'importe quel autre composant peut écouter cet événement. Vous pouvez le faire dans le callback `mounted` :

```
<script>export default {  name: 'App',  mounted() {    this.$root.$on('clickedSomething', () => {      //...    })  }}</script>
```

C'est ce que Vue fournit dès la sortie de la boîte.

Lorsque vous dépassez cela, vous pouvez vous tourner vers Vuex ou d'autres bibliothèques tierces.

### Gérer l'état en utilisant Vuex

Vuex est la bibliothèque officielle de gestion d'état pour Vue.js.

Son travail est de partager des données entre les composants de votre application.

Les composants dans Vue.js, dès la sortie de la boîte, peuvent communiquer en utilisant

* props, pour transmettre l'état aux composants enfants depuis un parent
* événements, pour changer l'état d'un composant parent depuis un enfant, ou en utilisant le composant racine comme un bus d'événements

Parfois, les choses deviennent plus complexes que ce que ces options simples permettent.

Dans ce cas, une bonne option est de centraliser l'état dans un seul magasin. C'est ce que fait Vuex.

#### Pourquoi devriez-vous utiliser Vuex ?

Vuex n'est pas la seule option de gestion d'état que vous pouvez utiliser dans Vue (vous pouvez utiliser [Redux](https://medium.com/@quincylarson/17a99705b8e1) aussi), mais son principal avantage est qu'il est officiel, et son intégration avec Vue.js est ce qui le rend brillant.

Avec React, vous avez le problème de devoir choisir parmi les nombreuses bibliothèques disponibles, car l'écosystème est énorme et n'a pas de norme réelle. Récemment, Redux était le choix le plus populaire, avec [MobX](https://mobx.js.org/getting-started.html) suivant en termes de popularité. Avec Vue, j'irais jusqu'à dire que vous n'aurez pas besoin de chercher autre chose que Vuex, surtout lorsque vous commencez.

Vuex a emprunté beaucoup de ses idées à l'écosystème React, car c'est le modèle Flux popularisé par Redux.

Si vous connaissez déjà Flux ou Redux, Vuex vous sera très familier. Si vous ne les connaissez pas, pas de problème — je vais expliquer chaque concept à partir de zéro.

Les composants dans une application Vue peuvent avoir leur propre état. Par exemple, une boîte de saisie stockera les données saisies localement. C'est parfaitement bien, et les composants peuvent avoir un état local même lorsqu'ils utilisent Vuex.

Vous savez que vous avez besoin de quelque chose comme Vuex lorsque vous commencez à faire beaucoup de travail pour transmettre un morceau d'état.

Dans ce cas, Vuex fournit un magasin de dépôt central pour l'état, et vous modifiez l'état en demandant au magasin de le faire.

Chaque composant qui dépend d'un morceau particulier de l'état y accédera en utilisant un getter sur le magasin, ce qui garantit qu'il est mis à jour dès que cette chose change.

L'utilisation de Vuex introduira une certaine complexité dans l'application, car les choses doivent être configurées d'une certaine manière pour fonctionner correctement. Mais si cela aide à résoudre le passage de props désorganisé et le système d'événements qui pourrait se transformer en un gâchis de spaghetti s'il est trop compliqué, alors c'est un bon choix.

#### Commençons

Dans cet exemple, je pars d'une application Vue CLI. Vuex peut également être utilisé en le chargeant directement dans une balise de script. Mais, puisque Vuex est plus en phase avec les applications plus grandes, il est beaucoup plus probable que vous l'utilisiez sur une application plus structurée, comme celles que vous pouvez démarrer rapidement avec le Vue CLI.

Les exemples que j'utilise seront mis sur CodeSandbox, qui est un excellent service qui a un échantillon Vue CLI [prêt à l'emploi](https://codesandbox.io/s/vue). Je recommande de l'utiliser pour jouer avec.

![Image](https://cdn-media-1.freecodecamp.org/images/hoB1Mu8Q1Py50t5Es5EKze26BsJOApMhEWVh)

Une fois que vous y êtes, cliquez sur le bouton Ajouter une dépendance, entrez "vuex" et cliquez dessus.

Maintenant, Vuex sera listé dans les dépendances du projet.

Pour installer Vuex localement, vous pouvez simplement exécuter `npm install vuex` ou `yarn add vuex` à l'intérieur du dossier du projet.

#### Créer le magasin Vuex

Maintenant, nous sommes prêts à créer notre magasin Vuex.

Ce fichier peut être placé n'importe où. Il est généralement suggéré de le mettre dans le fichier `src/store/store.js`, donc nous allons faire cela.

Dans ce fichier, nous initialisons Vuex et disons à Vue de l'utiliser :

```
import Vue from 'vue'import Vuex from 'vuex'
```

```
Vue.use(Vuex)
```

```
export const store = new Vuex.Store({})
```

![Image](https://cdn-media-1.freecodecamp.org/images/p2kPCCKdhaHsHfXd4Nti975YVgvKMnbHbMRd)

Nous exportons un objet de magasin Vuex, que nous créons en utilisant l'API `Vuex.Store()`.

#### Un cas d'utilisation pour le magasin

Maintenant que nous avons une structure en place, trouvons une idée pour un bon cas d'utilisation de Vuex, afin que je puisse introduire ses concepts.

Par exemple, j'ai deux composants frères, l'un avec un champ de saisie, et l'autre qui imprime le contenu de ce champ de saisie.

Lorsque le champ de saisie est modifié, je veux également changer le contenu dans ce deuxième composant. Très simple, mais cela fera l'affaire pour nous.

#### Présentation des nouveaux composants dont nous avons besoin

Je supprime le composant HelloWorld et ajoute un composant Form, et un composant Display.

```
<template>  <div>    <label for="flavor">Votre parfum de glace préféré ?</label>    <input name="flavor">  </div></template>
```

```
<template>  <div>    <p>Vous avez choisi ???</p>  </div></template>
```

#### Ajouter ces composants à l'application

Nous les ajoutons au code `App.vue` au lieu du composant HelloWorld :

```
<template>  <div id="app">    <Form/>    <Display/>  </div></template>
```

```
<script>import Form from './components/Form'import Display from './components/Display'
```

```
export default {  name: 'App',  components: {    Form,    Display  }}</script>
```

#### Ajouter l'état au magasin

Avec cela en place, nous retournons au fichier store.js. Nous ajoutons une propriété au magasin appelée `state`, qui est un objet, contenant la propriété `flavor`. C'est une chaîne vide initialement.

```
import Vue from 'vue'import Vuex from 'vuex'
```

```
Vue.use(Vuex)
```

```
export const store = new Vuex.Store({  state: {    flavor: ''  }})
```

Nous le mettrons à jour lorsque l'utilisateur tape dans le champ de saisie.

#### Ajouter une mutation

L'état ne peut pas être manipulé sauf en utilisant des mutations. Nous configurons une mutation qui sera utilisée à l'intérieur du composant `Form` pour notifier le magasin que l'état doit changer.

```
import Vue from 'vue'import Vuex from 'vuex'
```

```
Vue.use(Vuex)
```

```
export const store = new Vuex.Store({  state: {    flavor: ''  },  mutations: {    change(state, flavor) {      state.flavor = flavor    }  }})
```

#### Ajouter un getter pour référencer une propriété d'état

Avec cela configuré, nous devons ajouter un moyen de regarder l'état. Nous le faisons en utilisant des getters. Nous configurons un getter pour la propriété `flavor` :

```
import Vue from 'vue'import Vuex from 'vuex'
```

```
Vue.use(Vuex)
```

```
export const store = new Vuex.Store({  state: {    flavor: ''  },  mutations: {    change(state, flavor) {      state.flavor = flavor    }  },  getters: {    flavor: state => state.flavor  }})
```

Remarquez comment `getters` est un objet. `flavor` est une propriété de cet objet, qui accepte l'état comme paramètre, et retourne la propriété `flavor` de l'état.

#### Ajouter le magasin Vuex à l'application

Maintenant, le magasin est prêt à être utilisé. Nous retournons à notre code d'application, et dans le fichier main.js, nous devons importer l'état et le rendre disponible dans notre application Vue.

Nous ajoutons

```
import { store } from './store/store'
```

et nous l'ajoutons à l'application Vue :

```
new Vue({  el: '#app',  store,  components: { App },  template: '<App/>'})
```

Une fois que nous ajoutons cela, puisque c'est le composant Vue principal, la variable `store` à l'intérieur de chaque composant Vue pointera vers le magasin Vuex.

#### Mettre à jour l'état lors d'une action de l'utilisateur en utilisant commit

Mettons à jour l'état lorsque l'utilisateur tape quelque chose.

Nous le faisons en utilisant l'API `store.commit()`.

Mais d'abord, créons une méthode qui est appelée lorsque le contenu de l'entrée change. Nous utilisons `@input` plutôt que `@change` car ce dernier n'est déclenché que lorsque le focus est retiré de la boîte de saisie, tandis que `@input` est appelé à chaque pression de touche.

```
<template>  <div>    <label for="flavor">Votre parfum de glace préféré ?</label>    <input @input="changed" name="flavor">  </div></template>
```

```
<script>export default {  methods: {    changed: function(event) {      alert(event.target.value)    }  }}</script>
```

Maintenant que nous avons la valeur de la saveur, nous utilisons l'API Vuex :

```
<script>export default {  methods: {    changed: function(event) {      this.$store.commit('change', event.target.value)    }  }}</script>
```

Voyez comment nous référençons le magasin en utilisant `this.$store` ? Cela est grâce à l'inclusion de l'objet `store` dans l'initialisation du composant Vue principal.

La méthode `commit()` accepte un nom de mutation (nous avons utilisé `change` dans le magasin Vuex) et une charge utile, qui sera passée à la mutation en tant que deuxième paramètre de sa fonction de rappel.

#### Utiliser le getter pour afficher la valeur de l'état

Maintenant, nous devons référencer le getter de cette valeur dans le template Display, en utilisant `$store.getters.flavor`. `this` peut être omis car nous sommes dans le template, et `this` est implicite.

```
<template>  <div>    <p>Vous avez choisi {{ $store.getters.flavor }}</p>  </div></template>
```

Le code source complet et fonctionnel est disponible [ici](https://codesandbox.io/s/zq7k7nkzkm).

Il manque encore de nombreux concepts dans ce puzzle :

* actions
* modules
* helpers
* plugins

Mais maintenant vous avez les bases pour aller lire à leur sujet dans la documentation officielle.

### Gérer les URL en utilisant Vue Router

Dans une application web JavaScript, un routeur est la partie qui synchronise la vue actuellement affichée avec le contenu de la barre d'adresse du navigateur.

En d'autres termes, c'est la partie qui fait changer l'URL lorsque vous cliquez sur quelque chose dans la page, et aide à afficher la vue correcte lorsque vous atteignez une URL spécifique.

Traditionnellement, le Web est construit autour des URL. Lorsque vous atteignez une certaine URL, une page spécifique est affichée.

Avec l'introduction d'applications qui s'exécutent à l'intérieur du navigateur et changent ce que l'utilisateur voit, de nombreuses applications ont rompu cette interaction, et vous deviez mettre à jour manuellement l'URL avec l'API History du navigateur.

Vous avez besoin d'un routeur lorsque vous devez synchroniser les URL avec les vues dans votre application. C'est un besoin très courant, et tous les principaux frameworks modernes permettent désormais de gérer le routage.

La bibliothèque Vue Router est la solution pour les applications Vue.js. Vue n'impose pas l'utilisation de cette bibliothèque. Vous pouvez utiliser n'importe quelle bibliothèque de routage générique que vous souhaitez, ou même créer votre propre intégration de l'API History, mais l'avantage d'utiliser Vue Router est qu'il est officiel.

Cela signifie qu'il est maintenu par les mêmes personnes qui maintiennent Vue, donc vous obtenez une intégration plus cohérente dans le framework, et la garantie qu'il sera toujours compatible à l'avenir, quoi qu'il arrive.

#### Installation

Vue Router est disponible via npm avec le package nommé `vue-router`.

Si vous utilisez Vue via une balise de script, vous pouvez inclure Vue Router en utilisant

```
<script src="https://unpkg.com/vue-router"></script>
```

[UNPKG](https://unpkg.com/#/) est un outil très pratique qui rend chaque package npm disponible dans le navigateur avec un simple lien.

Si vous utilisez le Vue CLI, installez-le en utilisant :

```
npm install vue-router
```

Une fois que vous avez installé `vue-router` et l'avez rendu disponible soit en utilisant une balise de script, soit via Vue CLI, vous pouvez maintenant l'importer dans votre application.

Vous l'importez après `vue`, et vous appelez `Vue.use(VueRouter)` pour l'**installer** à l'intérieur de l'application :

```
import Vue from 'vue'import VueRouter from 'vue-router'
```

```
Vue.use(VueRouter)
```

Après avoir appelé `Vue.use()` en passant l'objet routeur, dans n'importe quel composant de l'application, vous avez accès à ces objets :

* `this.$router` est l'objet routeur
* `this.$route` est l'objet route actuel

#### L'objet routeur

L'objet routeur, accessible en utilisant `this.$router` depuis n'importe quel composant lorsque le Vue Router est installé dans le composant racine Vue, offre de nombreuses fonctionnalités intéressantes.

Nous pouvons faire en sorte que l'application navigue vers une nouvelle route en utilisant

* `this.$router.push()`
* `this.$router.replace()`
* `this.$router.go()`

qui ressemblent aux méthodes `pushState`, `replaceState` et `go` de l'API History.

* `push()` est utilisé pour aller à une nouvelle route, en ajoutant un nouvel élément à l'historique du navigateur
* `replace()` est le même, sauf qu'il ne pousse pas un nouvel état à l'historique

Exemples d'utilisation :

```
this.$router.push('about') //route nommée, voir plus tardthis.$router.push({ path: 'about' })this.$router.push({ path: 'post', query: { post_slug: 'hello-world' } }) //en utilisant des paramètres de requête (post?post_slug=hello-world)this.$router.replace({ path: 'about' })
```

`go()` va en arrière et en avant, en acceptant un nombre qui peut être positif ou négatif pour revenir en arrière dans l'historique :

```
this.$router.go(-1) //revenir en arrière d'un pasthis.$router.go(1) //avancer d'un pas
```

#### Définir les routes

J'utilise un composant mono-fichier Vue dans cet exemple.

Dans le template, j'utilise une balise `nav` qui contient trois composants `router-link`, qui ont les libellés Accueil, Connexion et À propos. Une URL est attribuée via l'attribut `to`.

Le composant `router-view` est l'endroit où Vue Router placera le contenu qui correspond à l'URL actuelle.

```
<template>  <div id="app">    <nav>      <router-link to="/">Accueil</router-link>      <router-link to="/login">Connexion</router-link>      <router-link to="/about">À propos</router-link>    </nav>    <router-view></router-view>  </div></template>
```

Un composant `router-link` rend une balise `a` par défaut (vous pouvez changer cela). Chaque fois que la route change, soit en cliquant sur un lien, soit en changeant l'URL, une classe `router-link-active` est ajoutée à l'élément qui fait référence à la route active, vous permettant de le styliser.

Dans la partie JavaScript, nous incluons et installons d'abord le routeur, puis nous définissons trois composants de route.

Nous les passons à l'initialisation de l'objet `router`, et nous passons cet objet à l'instance racine Vue.

Voici le code :

```
<script>import Vue from 'vue'import VueRouter from 'vue-router'
```

```
Vue.use(Router)
```

```
const Home  = {  template: '<div>Accueil</div>'}
```

```
const Login = {  template: '<div>Connexion</div>'}
```

```
const About = {  template: '<div>À propos</div>'}
```

```
const router = new VueRouter({  routes: [    { path: '/', component: Home },    { path: '/login', component: Login },    { path: '/about', component: About }  ]})
```

```
new Vue({  router}).$mount('#app')</script>
```

Habituellement, dans une application Vue, vous instanciez et montez l'application racine en utilisant :

```
new Vue({  render: h => h(App)}).$mount('#app')
```

Lorsque vous utilisez le Vue Router, vous ne passez pas de propriété `render` mais à la place, vous utilisez `router`.

La syntaxe utilisée dans l'exemple ci-dessus :

```
new Vue({  router}).$mount('#app')
```

est une abréviation pour :

```
new Vue({  router: router}).$mount('#app')
```

Voyez dans l'exemple, nous passons un tableau `routes` au constructeur `VueRouter`. Chaque route dans ce tableau a des paramètres `path` et `component`.

Si vous passez également un paramètre `name`, vous avez une route nommée.

#### Utiliser des routes nommées pour passer des paramètres aux méthodes push et replace du routeur

Vous vous souvenez comment nous avons utilisé l'objet Router pour pousser un nouvel état avant ?

```
this.$router.push({ path: 'about' })
```

Avec une route nommée, nous pouvons passer des paramètres à la nouvelle route :

```
this.$router.push({ name: 'post', params: { post_slug: 'hello-world' } })
```

Il en va de même pour `replace()` :

```
this.$router.replace({ name: 'post', params: { post_slug: 'hello-world' } })
```

#### Que se passe-t-il lorsque l'utilisateur clique sur un `router-link` ?

L'application rendra le composant de route qui correspond à l'URL passée au lien.

Le nouveau composant de route qui gère l'URL est instancié et ses gardes appelés, et l'ancien composant de route sera détruit.

#### Gardes de route

Puisque nous avons mentionné les gardes, présentons-les.

Vous pouvez les considérer comme des hooks de cycle de vie ou des middlewares. Ce sont des fonctions appelées à des moments spécifiques pendant l'exécution de l'application. Vous pouvez intervenir et altérer l'exécution d'une route, en redirigeant ou en annulant simplement la demande.

Vous pouvez avoir des gardes globales en ajoutant un callback aux propriétés `beforeEach()` et `afterEach()` du routeur.

* `beforeEach()` est appelé avant que la navigation ne soit confirmée
* `beforeResolve()` est appelé lorsque `beforeEach()` est exécuté et que tous les gardes `beforeRouterEnter` et `beforeRouteUpdate` des composants sont appelés, mais avant que la navigation ne soit confirmée. La vérification finale.
* `afterEach()` est appelé après que la navigation soit confirmée

Que signifie "la navigation est confirmée" ? Nous allons le voir dans un instant. En attendant, pensez à cela comme "l'application peut aller à cette route".

L'utilisation est :

```
this.$router.beforeEach((to, from, next) => {  // ...})
```

```
this.$router.afterEach((to, from) => {  // ...})
```

`to` et `from` représentent les objets de route vers lesquels nous allons et d'où nous venons.

`beforeEach` a un paramètre supplémentaire `next` qui, si nous l'appelons avec `false` comme paramètre, bloquera la navigation et la rendra non confirmée.

Comme dans le middleware Node, si vous êtes familier, `next()` doit toujours être appelé, sinon l'exécution sera bloquée.

Les composants de route unique ont également des gardes :

* `beforeRouteEnter(from, to, next)` est appelé avant que la route actuelle ne soit confirmée
* `beforeRouteUpdate(from, to, next)` est appelé lorsque la route change mais que le composant qui la gère est toujours le même (avec le routage dynamique, voir `next`)
* `beforeRouteLeave(from, to, next)` est appelé lorsque nous nous éloignons d'ici

Nous avons mentionné la navigation. Pour déterminer si la navigation vers une route est confirmée, Vue Router effectue certaines vérifications :

* il appelle le garde `beforeRouteLeave` dans le(s) composant(s) actuel(s)
* il appelle le garde `beforeEach()` du routeur
* il appelle le `beforeRouteUpdate()` dans tout composant qui doit être réutilisé, s'il en existe
* il appelle le garde `beforeEnter()` sur l'objet de route (je ne l'ai pas mentionné mais vous pouvez regarder [ici](https://router.vuejs.org/guide/advanced/navigation-guards.html#per-route-guard))
* il appelle le `beforeRouterEnter()` dans le composant que nous devons entrer
* il appelle le garde `beforeResolve()` du routeur
* si tout va bien, la navigation est confirmée !
* il appelle le garde `afterEach()` du routeur

Vous pouvez utiliser les gardes spécifiques à la route (`beforeRouteEnter` et `beforeRouteUpdate` en cas de routage dynamique) comme des hooks de cycle de vie, afin que vous puissiez démarrer des requêtes de récupération de données par exemple.

#### Routage dynamique

L'exemple ci-dessus montre une vue différente en fonction de l'URL, en gérant les routes `/`, `/login` et `/about`.

Un besoin très courant est de gérer des routes dynamiques, comme avoir tous les articles sous `/post/`, chacun avec le nom du slug :

* `/post/first`
* `/post/another-post`
* `/post/hello-world`

Vous pouvez y parvenir en utilisant un segment dynamique.

Ceux-ci étaient des segments statiques :

```
const router = new VueRouter({  routes: [    { path: '/', component: Home },    { path: '/login', component: Login },    { path: '/about', component: About }  ]})
```

Nous ajoutons un segment dynamique pour gérer les articles de blog :

```
const router = new VueRouter({  routes: [    { path: '/', component: Home },    { path: '/post/:post_slug', component: Post },    { path: '/login', component: Login },    { path: '/about', component: About }  ]})
```

Remarquez la syntaxe `:post_slug`. Cela signifie que vous pouvez utiliser n'importe quelle chaîne, et celle-ci sera mappée au placeholder `post_slug`.

Vous n'êtes pas limité à ce type de syntaxe. Vue s'appuie sur [cette bibliothèque](https://github.com/pillarjs/path-to-regexp) pour analyser les routes dynamiques, et vous pouvez vous lâcher avec des expressions régulières.

Maintenant, à l'intérieur du composant de route Post, nous pouvons référencer la route en utilisant `$route`, et le slug de l'article en utilisant `$route.params.post_slug` :

```
const Post = {  template: '<div>Post: {{ $route.params.post_slug }}</div>'}
```

Nous pouvons utiliser ce paramètre pour charger le contenu depuis le back-end.

Vous pouvez avoir autant de segments dynamiques que vous le souhaitez, dans la même URL :

`/post/:author/:post_slug`

Vous vous souvenez lorsque nous avons parlé de ce qui se passe lorsque l'utilisateur navigue vers une nouvelle route ?

Dans le cas des routes dynamiques, ce qui se passe est un peu différent.

Pour que Vue soit plus efficace, au lieu de détruire le composant de route actuel et de le réinstancier, il réutilise l'instance actuelle.

Lorsque cela se produit, Vue appelle l'événement de cycle de vie `beforeRouteUpdate`.

Là, vous pouvez effectuer toute opération dont vous avez besoin :

```
const Post = {  template: '<div>Post: {{ $route.params.post_slug }}</div>'  beforeRouteUpdate(to, from, next) {    console.log(`Updating slug from ${from} to ${to}`)    next() //assurez-vous de toujours appeler next()  }}
```

#### Utilisation des props

Dans les exemples, j'ai utilisé `$route.params.*` pour accéder aux données de la route. Un composant ne devrait pas être si étroitement couplé avec le routeur, et au lieu de cela, nous pouvons utiliser des props :

```
const Post = {  props: ['post_slug'],  template: '<div>Post: {{ post_slug }}</div>'}
```

```
const router = new VueRouter({  routes: [    { path: '/post/:post_slug', component: Post, props: true }  ]})
```

Remarquez le `props: true` passé à l'objet de route pour activer cette fonctionnalité.

#### Routes imbriquées

Auparavant, j'ai mentionné que vous pouvez avoir autant de segments dynamiques que vous le souhaitez, dans la même URL, comme :

`/post/:author/:post_slug`

Donc, supposons que nous avons un composant Author qui s'occupe du premier segment dynamique :

```
<template>  <div id="app">    <router-view></router-view>  </div></template>
```

```
<script>import Vue from 'vue'import VueRouter from 'vue-router'
```

```
Vue.use(Router)
```

```
const Author  = {  template: '<div>Author: {{ $route.params.author}}</div>'}
```

```
const router = new VueRouter({  routes: [    { path: '/post/:author', component: Author }  ]})
```

```
new Vue({  router}).$mount('#app')</script>
```

Nous pouvons insérer une deuxième instance de composant `router-view` à l'intérieur du template Author :

```
const Author  = {  template: '<div>Author: {{ $route.params.author}}<router-view></router-view></div>'}
```

Nous ajoutons le composant Post :

```
const Post = {  template: '<div>Post: {{ $route.params.post_slug }}</div>'}
```

Ensuite, nous injecterons la route dynamique interne dans la configuration `VueRouter` :

```
const router = new VueRouter({  routes: [{    path: '/post/:author',    component: Author,    children: [      path: ':post_slug',      component: Post    ]  }]})
```

Merci d'avoir lu !

> Obtenez ce post au format PDF/ePub/Kindle sur [vuehandbook.com](https://vuehandbook.com)