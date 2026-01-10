---
title: Erreurs courantes à éviter lors de l'utilisation de Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-04T12:22:43.000Z'
originalURL: https://freecodecamp.org/news/common-mistakes-to-avoid-while-working-with-vue-js-10e0b130925b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CtOATbW-ewf3UHbrZVi7Iw.jpeg
tags:
- name: development
  slug: development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Erreurs courantes à éviter lors de l'utilisation de Vue.js
seo_desc: 'By Jérémy Bardon

  Looking for a front-end framework to try out, I started with React and then tried
  Vue.js.

  Unfortunately, I encountered a lot of issues with Vue.js at the very beginning.
  In this article, I’d like to share a few common issues that you...'
---

Par Jérémy Bardon

À la recherche d'un framework front-end à essayer, j'ai commencé avec React puis j'ai essayé Vue.js.

Malheureusement, j'ai rencontré beaucoup de problèmes avec Vue.js dès le début. Dans cet article, je souhaite partager quelques problèmes courants que vous pourriez rencontrer lors de l'utilisation de Vue.js. Certains de ces problèmes peuvent sembler évidents, mais je pense que partager mon expérience pourrait aider quelqu'un.

### Inclure le compilateur de template

Mon premier problème était assez basique. La première chose à faire pour utiliser Vue.js est de l'importer. Si vous suivez le [guide officiel](https://vuejs.org/v2/guide/#Composing-with-Components) et utilisez un template inline pour votre composant, vous obtiendrez une page blanche.

```js
import Vue from 'vue';
var vm = new Vue({
  el: '#vm',
  template: '<div>Hello World</div>',
});
```

Notez que ce problème ne se produit pas lorsque vous définissez des templates avec la fonction render ou SFC ([Single File Component](https://vuejs.org/v2/guide/single-file-components.html#ad)).

En réalité, il existe de nombreuses [versions de Vue](https://vuejs.org/v2/guide/installation.html#Explanation-of-Different-Builds). La version par défaut exportée par le package NPM est la version **runtime-only**. Elle ne contient pas le compilateur de template.

Pour quelques informations de contexte, le compilateur de template fonctionne exactement comme [JSX pour React](https://reactjs.org/docs/introducing-jsx.html). Il remplace les chaînes de template par des appels de fonction pour créer un nœud de DOM virtuel.

```js
// #1: importer la version complète dans un fichier JavaScript
import Vue from 'vue/dist/vue.js';

// OU #2: créer un alias dans la configuration de webpack
config.resolve: {
  alias: { vue: 'vue/dist/vue.js' }
}

// OU #3: utiliser directement la fonction render
var vm = new Vue({
  el: '#vm',
  render: function(createElement) {
    return createElement('div', 'Hello world');
  }
});
```

Avec les SFC, ce problème ne se produit pas. Les outils **vue-loader** et **vueify** sont utilisés pour gérer les SFC. Ils génèrent des composants JavaScript simples en utilisant la fonction render pour définir le template.

Pour utiliser des templates sous forme de chaînes dans les composants, utilisez une version complète de Vue.js.

En résumé, pour résoudre ce problème, spécifiez la bonne version lors de l'import, ou créez un alias pour Vue dans la configuration de votre bundler.

Vous devez noter que l'utilisation de templates sous forme de chaînes réduit les performances de votre application, car la compilation se produit à l'exécution.

Il existe de nombreuses autres façons de définir un template de composant, alors [consultez cet article](https://vuejsdevelopers.com/2017/03/24/vue-js-component-templates/). De plus, je recommande d'utiliser la [fonction render dans l'instance Vue](https://vuejsdevelopers.com/2017/09/17/vue-js-avoid-dom-templates/).

### Maintenir la réactivité des propriétés

Si vous utilisez React, vous savez probablement que sa réactivité repose sur l'appel de la fonction `setState` pour mettre à jour la valeur des propriétés.

La réactivité avec Vue.js est un peu différente. Elle est basée sur la proxyfication des propriétés du composant. Les fonctions [Getter et Setter](https://vuejs.org/v2/guide/reactivity.html#How-Changes-Are-Tracked) seront remplacées et notifieront les mises à jour au DOM virtuel.

```js
var vm = new Vue({
  el: '#vm',
  template: `<div>{{ item.count }}<input type="button" value="Click" @click="updateCount"/></div>`,
  data: {
    item: {}
  },
  beforeMount () {
    this.$data.item.count = 0;
  },
  methods: {
    updateCount () {
      // L'objet JavaScript est mis à jour mais
      // le template du composant n'est pas rendu à nouveau
      this.$data.item.count++;
    }
  }
});
```

Dans l'extrait de code ci-dessus, l'instance Vue a une propriété appelée `item` (définie dans data). Cette propriété contient un objet littéral vide.

Lors de l'initialisation du composant, Vue crée un proxy sous les fonctions `get` et `set` attachées à la propriété `item`. Ainsi, le framework surveillera les changements de valeur et réagira éventuellement.

Cependant, la propriété `count` n'est pas réactive, car elle n'a pas été déclarée au moment de l'initialisation.

En réalité, la proxyfication ne se produit qu'au moment de l'initialisation du composant, et la fonction de cycle de vie `beforeMount` se déclenche plus tard.

De plus, le setter de `item` n'est pas appelé lors de la définition de `count`. Ainsi, le proxy ne se déclenchera pas et la propriété `count` n'aura pas de surveillance.

```js
beforeMount () {
  // #1: Appeler le setter parent
  // le setter de item est appelé donc la proxyfication est propagée
  this.$data.item = {
    count: 0
  };
  
  // OU #2: demander explicitement une surveillance
  // item.count obtient ses getter et setter proxyfiés
  this.$set(this.$data.item, 'count', 0);
  
  // "Raccourci" pour:
  Vue.set(this.$data.item, 'count', 0);
}
```

Si vous gardez l'affectation `item.count` dans `beforeMount`, l'appel à `Vue.set` plus tard ne créera pas de surveillance.

Le même problème exact se produit également avec les tableaux lors de l'utilisation d'affectations directes sur des index inconnus. Dans de tels cas, vous devriez préférer les [fonctions proxyfiées de tableau](https://vuejs.org/v2/guide/list.html#Array-Change-Detection) telles que `push` et `slice`.

De plus, vous pouvez lire [cet article](https://vuejsdevelopers.com/2017/03/05/vue-js-reactivity/) du site des développeurs Vue.js.

### Faites attention aux exports des SFC

Vous pouvez utiliser Vue régulièrement dans des fichiers JavaScript, mais vous pouvez également utiliser des [Single File Components](https://vuejs.org/v2/guide/single-file-components.html#ad). Cela aide à regrouper le code JavaScript, HTML et CSS dans un seul fichier.

Avec les SFC, le code du composant est la balise script d'un fichier `.vue`. Toujours écrit en JavaScript, il doit exporter le composant.

Il existe de nombreuses façons d'exporter une variable/composant. Souvent, nous utilisons des exports directs, nommés ou par défaut. Les exports nommés empêcheront les utilisateurs de renommer le composant. Il sera également éligible pour le [tree-shaking](https://en.wikipedia.org/wiki/Tree_shaking).

```js
/* Fichier: user.vue */
<template>
  <div>{{ user.name }}</div>
</template>

<script>
  const User = {
    data: () => ({
      user: {
        name: 'John Doe'
      }
    })
  };
  export User; // Ne fonctionne pas
  export default User; // Fonctionne
</script>

/* Fichier: app.js */
import {User} from 'user.vue'; // Ne fonctionne pas
import User from 'user.vue'; // Fonctionne (" .vue " est requis)
```

L'utilisation d'exports nommés n'est pas compatible avec les SFC, soyez attentif à cela !

En résumé, exporter une variable nommée par défaut pourrait être une bonne idée. De cette façon, vous obtiendrez des messages de débogage plus explicites.

### Ne mélangez pas les composants SFC

Mettre le code, le template et le style ensemble est une bonne idée. De plus, selon vos contraintes et opinions, vous pourriez vouloir garder la [séparation des préoccupations](https://en.wikipedia.org/wiki/Separation_of_concerns).

Comme décrit dans la [documentation Vue](https://vuejs.org/v2/guide/single-file-components.html#What-About-Separation-of-Concerns), cela est compatible avec les SFC.

Par la suite, une idée m'est venue à l'esprit. Utiliser le même code JavaScript et l'inclure dans différents templates. Vous pourriez le considérer comme une mauvaise pratique, mais cela garde les choses simples.

Par exemple, un composant peut avoir à la fois un mode lecture seule et lecture-écriture et garder la même implémentation.

```js
/* Fichier: user.js */
const User = {
  data: () => ({
    user: {
      name: 'John Doe'
    }
  })
};
export default User;

/* Fichier: user-read-only.vue */
<template><div>{{ user.name }}</div></template>
<script src="./user.js"></script>

/* Fichier: user-read-write.vue */
<template><input v-model="user.name"/></template>
<script src="./user.js"></script>
```

Dans cet extrait, les templates lecture seule et lecture-écriture utilisent le même composant utilisateur JavaScript.

Une fois que vous importez les deux composants, vous constaterez que cela ne fonctionne pas comme prévu.

```js
// La dernière importation l'emporte
import UserReadWrite from './user-read-write.vue';
import UserReadOnly from './user-read-only.vue';

Vue.component('UserReadOnly', UserReadOnly);
Vue.component('UserReadWrite', UserReadWrite);

// Affiche deux fois un UserReadOnly
var vm = new Vue({
  el: '#vm',
  template: `<div><UserReadOnly/><UserReadWrite/></div>`
});
```

Le composant défini dans `user.js` ne peut être utilisé que dans un seul SFC. Sinon, le dernier SFC importé qui l'utilise écrasera le précédent.

> Les SFC permettent de diviser le code en fichiers séparés. Mais vous ne pouvez pas importer ces fichiers dans plusieurs composants Vue.

Pour faire simple, ne réutilisez pas le code de composant JavaScript dans plusieurs composants SFC. La fonctionnalité de code séparé est une syntaxe pratique, pas un modèle de conception.

Merci d'avoir lu, j'espère que mon expérience vous a été utile pour éviter les erreurs que j'ai commises.

**Si cela vous a été utile, veuillez cliquer sur le bouton** ? **plusieurs fois pour aider les autres à trouver l'article et montrer votre soutien ! ?**

**N'oubliez pas de me suivre pour être notifié de mes prochains articles** ?

### Consultez mes [autres](https://medium.com/@jbardon/latest) articles

#### ➡ JavaScript

* [Comment améliorer vos compétences en JavaScript en écrivant votre propre framework de développement web ?](https://www.freecodecamp.org/news/how-to-improve-your-javascript-skills-by-writing-your-own-web-development-framework-eed2226f190/)
* [Arrêtez le débogage douloureux de JavaScript et adoptez Intellij avec Source Map](https://medium.com/dailyjs/stop-painful-javascript-debug-and-embrace-intellij-with-source-map-6fe68eda8555)

#### ➡ Série React pour débutants

* [Commencez avec le premier article](https://www.freecodecamp.org/news/a-quick-guide-to-learn-react-and-how-its-virtual-dom-works-c869d788cd44/)
* [Obtenez le guide des bonnes pratiques](https://www.freecodecamp.org/news/the-beginners-collection-of-powerful-tips-and-tricks-for-react-f2e3833c6f12/)