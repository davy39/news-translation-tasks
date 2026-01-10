---
title: 'Composants Vue : Un tutoriel interactif sur Vue JS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-17T21:46:52.000Z'
originalURL: https://freecodecamp.org/news/vue-js-components-an-interactive-guide-1b8149ecc254
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ieROYZuCX-w0p9V7UswJbQ.png
tags:
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: 'Composants Vue : Un tutoriel interactif sur Vue JS'
seo_desc: 'By Per Harald Borgen

  In my previous tutorial we learned the basics of Vue.js: the Vue instance, the template
  syntax, data object, directives, methods and more. This was enough to get started
  creating with very basic Vue examples.


  Note: check out thi...'
---

Par Per Harald Borgen

Dans [mon précédent tutoriel](https://medium.freecodecamp.org/learn-basic-vue-js-crash-course-guide-vue-tutorial-e3da361c635), nous avons appris les bases de Vue.js : l'instance Vue, la syntaxe de template, l'objet data, les directives, les méthodes et plus encore. Cela était suffisant pour commencer à créer des exemples très basiques avec Vue.

> **Note :** consultez [cette playlist](https://scrimba.com/playlist/playlist-38?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) si vous êtes intéressé à regarder tous mes screencasts sur Vue.

Mais si vous voulez construire des applications propres avec Vue, vous devrez apprendre les composants. C'est l'une des fonctionnalités les plus puissantes de la bibliothèque.

![Image](https://cdn-media-1.freecodecamp.org/images/lU7kIfogtoKiBbhLmwBSdmeDhUlQUJ0Iyj-J)

Les composants rendent votre code plus réutilisable et votre balisage plus lisible.

Ils vous permettront de créer des éléments HTML personnalisés, qui se comporteront exactement comme vous le souhaitez. Pour créer un composant Vue.js, faites ce qui suit :

```vue
Vue.component('my-component', {
  template: '<div>Un composant personnalisé !</div>'
})

new Vue({
    el: '#app'
})
```

La `clé template` est l'endroit où vous écrivez votre balisage pour ce composant. Dans le même objet, vous ajouterez plus tard d'autres fonctionnalités. Vous créez une **instance** de votre composant en ajoutant `<my-component></my-component>` dans le HTML :

```vue
<div id="app">
      <my-component></my-component>
</div>
```

Cela donnera le résultat suivant sur la page :

![Image](https://cdn-media-1.freecodecamp.org/images/wOT9PJkSfHw2lU2c81dIYeOZwGu1rs01bcAi)

Voici un [screencast Scrimba](https://scrimba.com/casts/crNKWHd?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) expliquant le même concept. Il est interactif, donc vous pouvez mettre en pause le screencast et modifier le code quand vous le souhaitez.

![Image](https://cdn-media-1.freecodecamp.org/images/uAUTlrqpj7seczMdm9GIFaYMqKLrbP2gaibK)

### Props

Le composant ci-dessus ne fait pas grand-chose. Pour le rendre un peu plus utilisable, ajoutons des props :

```vue
Vue.component('my-component', {
  props: ['message'],
  template: `<div>{{ message }}</div>`,
})
```

Les props vous permettront de passer des données dans une instance de composant depuis l'extérieur de ce composant. Ou plus correctement, de passer les données d'un parent.

Le `my-component` a une prop appelée `message`, qu'il rendra. La valeur de `message` sera définie lorsque nous créerons de nouvelles instances de ce composant dans le DOM. Nous pouvons créer autant de `my-component` que nous le souhaitons, et donner à chacun d'eux des props différentes. Ainsi, nous pourrons réutiliser notre code.

Pour passer des données en tant que prop `message`, faites simplement ce qui suit :

```vue
<div id="app">
      <my-component message="Bonjour de Vue.js !"></my-component>
</div>
```

Maintenant, **Bonjour de Vue.js !** sera rendu sur la page.

Mais cela reste une solution très statique, car nous avons codé en dur la valeur de la prop dans le HTML. Une meilleure solution serait de lier cette valeur à une source de données. Ainsi, nous pourrons la changer comme nous le souhaitons plus tard, par exemple en fonction des interactions de l'utilisateur ou des réponses des API.

Lions-la à l'objet data de notre instance Vue. Tout d'abord, nous créerons l'objet data.

```vue
var app = new Vue({
    el: '#app',
    data: {
      msg: 'Bonjour de l\'instance Vue'
    }
})
```

Pour lier la prop dans `my-component` au `msg` de notre instance Vue, nous utiliserons la directive `v-bind` que nous avons apprise dans l'article précédent :

```vue
<div id="app">
      <my-component v-bind:message="msg"></my-component>
</div>
```

Maintenant, nous pouvons changer les données via `app.msg = 'De nouvelles données'` et Vue se chargera de mettre à jour le DOM avec les nouvelles données.

> **_Astuce:_** _Vous pouvez supprimer le `v-bind` de `v-bind:message` et utiliser plutôt le raccourci `:message`._

Voici un [screencast Scrimba](https://scrimba.com/casts/caPgLTP?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) expliquant le concept :

![Image](https://cdn-media-1.freecodecamp.org/images/PJ7UGwbOgARBGkj7JjkCRMmkeges8UAcnR2U)

Mais que faire si vous voulez que votre composant puisse changer son `message` ? Cela ne peut pas se produire tant que `message` est une prop, car vous ne devriez jamais muter une prop à l'intérieur d'un composant. Si vous essayez, Vue vous donnera un avertissement dans la console.

### Data

Nous aurons donc besoin d'une autre façon de gérer les données à l'intérieur du composant. C'est là que la fonction `data` entre en jeu. Elle permettra à vos composants de gérer un état interne, que vous pourrez changer comme vous le souhaitez.

La `data` du composant remplit le même rôle que l'objet `data` dans l'instance Vue. Ce sont tous deux des endroits où vous stockerez des données mutables. Mais la `data` du composant est une **fonction** et non un **objet**.

Plongeons dans le code pour le rendre moins abstrait.

```vue
Vue.component('my-component', {
  template: '<div> {{ message }} </div>',
  data: function() {
    return {
      message: 'Bonjour de Vue data !'
    }
  }
})
```

Voici un [screencast Scrimba](https://scrimba.com/casts/c2LmGU2?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) qui explique le concept.

![Image](https://cdn-media-1.freecodecamp.org/images/TwF5iKb1ozpTfkLRX6V9H7AfLwFPClUgco00)

Et c'est à peu près tout ! Il y a bien sûr beaucoup plus de choses à apprendre sur les composants Vue. Mais cela devrait être suffisant pour que vous commenciez à jouer avec par vous-même.

Si vous apprenez quelque chose de nouveau sur Vue, je vous recommande de transmettre cette connaissance aux autres également. C'est l'une des meilleures façons d'apprendre, et la raison pour laquelle des communautés comme [freeCodeCamp](https://www.freecodecamp.com/) prospèrent.

Alors, allez-y et écrivez un article (ou créez un [Scrimba](http://scrimba.com?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_components_tutorial) screencast) sur ce que vous avez appris !