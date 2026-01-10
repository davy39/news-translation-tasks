---
title: 'Apprendre Vue : un tutoriel interactif Vue JS en 3 minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-06-19T01:41:12.000Z'
originalURL: https://freecodecamp.org/news/learn-basic-vue-js-crash-course-guide-vue-tutorial-e3da361c635
coverImage: https://cdn-media-1.freecodecamp.org/images/1*S9ztlTg2A3gvRxPfUg3jTQ.png
tags:
- name: JavaScript
  slug: javascript
- name: open source
  slug: open-source
- name: General Programming
  slug: programming
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: 'Apprendre Vue : un tutoriel interactif Vue JS en 3 minutes'
seo_desc: 'By Per Harald Borgen

  Vue.js is a JavaScript library for building user interfaces. Last year, it started
  to become quite popular among web developers. It’s lightweight, relatively easy
  to learn, and powerful.

  In the three minutes that Medium says it w...'
---

Par Per Harald Borgen

Vue.js est une bibliothèque JavaScript pour construire des interfaces utilisateur. L'année dernière, elle a commencé à devenir assez populaire parmi les développeurs web. Elle est légère, relativement facile à apprendre et puissante.

En trois minutes, le temps que Medium dit qu'il vous faudra pour lire cet article, vous serez équipé pour commencer à construire des applications Vue basiques. Avec chaque segment, j'ai également inclus un screencast interactif [Scrimba](https://scrimba.com/p/pXKqta?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_in_3_minutes), où vous pouvez me regarder expliquer les concepts et jouer avec le code vous-même.

Commençons.

### Syntaxe de template et données

Au cœur de Vue.js se trouve une syntaxe de template simple qui ressemble à ceci :

```vue
<div id="myApp">  
    {{ message }}  
</div>

```

Associez cela avec le snippet JavaScript suivant :

```js
var myApp = new Vue({  
   el: '#myApp',  
   data: {  
       message: 'Bonjour le monde !'  
   }  
})

```

Et cela résultera en _Bonjour le monde !_ étant rendu sur la page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8H9M0L0bYLUo8j0GqbwFFA.png)

La partie `el: #myApp` indique à Vue de rendre l'application à l'intérieur de l'élément DOM avec l'id _myApp_. L'objet `data` est l'endroit où vous placez les données que vous souhaitez utiliser dans votre application. Nous n'avons ajouté qu'une seule clé ici, `message`, que nous référençons dans notre HTML comme ceci : `{{ message }}`.

Vue se charge de lier l'objet `data` au DOM, donc si les données changent, la page sera également mise à jour.

Cela s'appelle le rendu déclaratif. Vous spécifiez simplement _ce que_ vous voulez mettre à jour, et Vue se charge de _comment_ le faire.

Vous pouvez changer les données en faisant ceci :

```js
myApp.message = 'Une nouvelle valeur';

```

Voici un screencast qui explique ce concept exact :

### Directives

Le prochain concept que vous devez apprendre est celui des directives. Les directives sont des attributs HTML qui sont préférés avec `v-`, ce qui indique qu'ils appliquent un comportement réactif au DOM rendu.

Supposons que nous voulons rendre quelque chose uniquement si une condition est vraie, et le cacher si elle est fausse. Alors nous utiliserons `v-if`.

Dans le HTML, cela ressemble à ceci.

```vue
<div id="app">  
    <p v-if="seen">Maintenant vous me voyez</p>  
</div>

```

Et un peu de JavaScript :

```js
var app = new Vue({  
    el: '#app',  
    data: {  
        seen: true  
    }  
})

```

Cela résultera en l'affichage du paragraphe _Maintenant vous me voyez_ si `seen` dans `data` est **vrai**. Pour cacher le paragraphe, vous pouvez définir `seen` à **faux**, comme ceci :

`app.seen = false;`

Voici un screencast expliquant le même concept :

Il existe de nombreuses autres directives, comme `v-for`, `v-on`, `v-bind` et `v-model`.

### Gestion des entrées utilisateur

Une autre directive principale que vous devez apprendre est `v-on`. Elle va attacher un écouteur d'événement à l'élément DOM, afin que vous puissiez gérer les entrées utilisateur. Vous spécifiez le type d'événement après les deux-points. Ainsi, `v-on:click` écoutera les clics.

```vue
<div id="app">  
    <button v-on:click="myClickHandler">Cliquez-moi !</button>  
</div>

```

`myClickHandler` fait référence à la clé du même nom dans l'objet `methods`. Il va sans dire que c'est l'objet où vous placez les méthodes de votre application. Vous pouvez avoir autant de méthodes que vous le souhaitez.

```js
var app = new Vue({  
    el: '#app',  
    methods: {  
        myClickHandler: function () {  
            console.log('bouton cliqué !');  
        }  
    }  
})

```

Cela résultera en _bouton cliqué_ étant enregistré dans la console lorsque vous cliquez sur le bouton.

Voici un screencast expliquant le concept :

### Mettre tout ensemble

Maintenant, créons un exemple où nous utilisons à la fois `data` et `methods`, en combinant ce que nous avons appris jusqu'à présent.

```vue
<div id="app">  
    <p>{{ message }}</p>  
    <button v-on:click="changeMessage">Cliquez-moi !</button>  
</div>

```

Et le JavaScript :

```js
var app = new Vue({  
    el: '#app',  
    data: {  
        message: 'Message de départ'  
    },  
    methods: {  
        changeMessage: function () {  
            this.message = 'Le message a changé !'  
        }  
    }  
})

```

Initialement, cela affichera _Message de départ_ sur la page, mais après le clic, cela affichera _Le message a changé_ à la place.

Le mot-clé `this` fait référence à l'instance Vue, celle que nous avons appelée `app`. C'est sur cette instance que nos données vivent, donc nous pouvons faire référence aux données `message` via `this.message`.

[Regardez ce screencast expliquant le concept.](https://scrimba.com/p/playlist-38/cast-1933?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=vue_in_3_minutes)

Et avec cela, vous devriez connaître suffisamment Vue.js pour commencer à créer des applications simples.

Dans le prochain tutoriel, vous apprendrez à créer des composants Vue. Alors assurez-vous de suivre cette publication si vous avez aimé cet article.