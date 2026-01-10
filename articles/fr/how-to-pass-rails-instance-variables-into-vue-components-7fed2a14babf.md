---
title: Comment passer des variables d'instance Rails dans des composants Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-15T09:54:26.000Z'
originalURL: https://freecodecamp.org/news/how-to-pass-rails-instance-variables-into-vue-components-7fed2a14babf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5FJEL2CTeSHvTBsCJd0YFQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Rails
  slug: rails
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment passer des variables d'instance Rails dans des composants Vue
seo_desc: 'By Gareth Fuller

  I’m currently working with a legacy Rails application. We are slowly transitioning
  the front-end from Rails views to a Vue application.

  As part of this transition, we have some elements that we want to turn into global
  Vue components...'
---

Par Gareth Fuller

Je travaille actuellement avec une application Rails héritée. Nous sommes en train de transitionner progressivement le front-end des vues Rails vers une application Vue.

Dans le cadre de cette transition, nous avons certains éléments que nous voulons transformer en composants Vue globaux. Nous voulons pouvoir utiliser ces composants dans nos vues Rails existantes et dans une application Vue sans avoir à personnaliser chaque composant pour gérer les deux situations.

Avant de partager ma solution à ce problème, voici un exemple de composant Vue en fichier unique que nous voulons pouvoir utiliser dans les deux scénarios (vue Rails et application Vue) :

```
// Payments.vue
```

```
<template lang="html">  <div id="payments">    <div class="payment" v-for="payment in payments">      {{ payment.amount }}    </div>  </div></template>
```

```
<script>export default {  name: 'payments'
```

```
  props: {    payments: { type: Array }  }}</script>
```

```
<style lang="scss" scoped></style>
```

Depuis une application Vue, ce composant est simple à utiliser, n'est-ce pas ? Par exemple :

```
// app/javascript/App.vue
```

```
<template lang="html">  <div id="app">    <payments :payments="payments" />  </div></template>
```

```
<script>import Payments from './Payments.vue'
```

```
export default {  name: 'app',
```

```
  components: { Payments },
```

```
  data () {    return {      payments: [        { amount: 123.00 },        { amount: 124.00 }      ]    }  }</script>
```

```
<style lang="scss" scoped></style>
```

Mais qu'en est-il de son utilisation dans une vue Rails ?

### Solution

Une solution pour utiliser le composant _Payments.vue_ dans Rails ressemble à ceci :

```
// app/views/payments/index.haml
```

```
.global-comp  = content_tag 'comp-wrapper', nil, data: { component: 'payments', props: { payments: @payments } }.to_json
```

Décomposons cet élément.

`.global-comp` est une div (avec la classe « global-comp ») pour monter une instance Vue très simple. Cette instance Vue nous fournit un composant wrapper à utiliser appelé _CompWrapper.vue_ (nous verrons à quoi sert CompWrapper dans un instant).

Voici l'instance Vue montée sur `.global-comp` :

```
// app/javascript/packs/global_comp.js
```

```
import Vue from 'vue/dist/vue.esm'
import CompWrapper from './CompWrapper'
```

```
document.addEventListener('DOMContentLoaded', () => {  const app = new Vue({    components: { CompWrapper }  }).$mount('.global-comp')})
```

Tout ce que cela fait est de rendre le composant (_CompWrapper.vue_) disponible pour nous dans une div avec la classe `global-comp`.

Si vous utilisez [Webpacker](https://github.com/rails/webpacker) avec Rails, vous devrez inclure ce pack dans votre layout quelque part avant la balise de fermeture du body. Par exemple :

```
// app/views/layouts/application.haml
```

```
...
```

```
= javascript_pack_tag "global_comp"
```

#### CompWrapper.vue

C'est la partie amusante. _CompWrapper.vue_ nous permet de passer :

1. Le nom du composant que nous voulons utiliser, par exemple, « payments »
2. Les props que nous voulons lui passer

Le but de ce composant wrapper est de nous permettre de passer des variables d'instance Rails comme `@payments` dans nos composants en tant que props sans avoir à gérer cela depuis chaque composant comme _Payments.vue_.

Voici donc _CompWrapper.vue_ :

```
// app/javascript/CompWrapper.vue
```

```
<template lang="html">  <component :is="data.component" v-bind="data.props"></component></template>
```

```
<script>import * as components from './components'
```

```
export default {  name: 'comp-wrapper',
```

```
  components,
```

```
  data () {    return {      data: {}    }  },
```

```
  created() {    this.data = JSON.parse(this.$attrs.data)  }}</script>
```

```
<style lang="scss" scoped></style>
```

La première chose que fait le composant CompWrapper est de prendre les attributs de données que vous avez définis sur l'élément dans la vue Rails, d'analyser le JSON et de définir un attribut de données Vue interne avec les données analysées :

```
created() {  this.data = JSON.parse(this.$attrs.data)}
```

avec `this.data` défini, nous pouvons ensuite l'utiliser pour sélectionner le composant que nous voulons utiliser et lui passer les props que nous avons fournies dans notre vue Rails en utilisant un composant dynamique Vue :

```
<component :is="data.component" v-bind="data.props"></component>
```

Et c'est tout !

Nous pouvons maintenant utiliser les composants Vue comme ils sont censés être utilisés, mais depuis nos vues Rails. 🎉