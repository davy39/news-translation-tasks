---
title: Apprendre Vuex en 5 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-28T20:37:58.000Z'
originalURL: https://freecodecamp.org/news/learn-vuex-in-5-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/learn-vuex.png
tags:
- name: vue
  slug: vue
- name: Vuex
  slug: vuex
seo_title: Apprendre Vuex en 5 minutes
seo_desc: 'By Per Harald Borgen

  This tutorial will give you a basic understanding of Vuex by building a plan-making
  application. A user can type in activities and then vote how much they like/dislike
  them.

  Once you''ve read this tutorial, you can check out our f...'
---

Par Per Harald Borgen

Ce tutoriel vous donnera une compréhension de base de Vuex en construisant une application de planification. Un utilisateur peut taper des activités et ensuite voter pour indiquer à quel point il les aime ou les déteste.

Une fois que vous aurez lu ce tutoriel, vous pourrez consulter notre [cours gratuit sur Vuex sur Scrimba](https://scrimba.com/g/gvuex), si vous êtes intéressé à en apprendre davantage.

Qu'est-ce que Vuex ? D'après [la documentation officielle de Vue](https://vuex.vuejs.org)

```
Vuex est un modèle de gestion d'état + une bibliothèque pour les applications Vue.js.
Il sert de magasin centralisé pour tous les composants d'une application, avec des règles garantissant que l'état ne peut être muté que de manière prévisible.

```

Ce cours suppose que vous êtes quelque peu familier avec Vue et nous aborderons brièvement des fonctionnalités comme `props`, les composants et les bindings, mais nous ne les passerons pas en revue en détail. Si vous souhaitez un rapide aperçu de Vue, n'hésitez pas à [consulter ce cours sur Scrimba](https://scrimba.com/p/pXKqta).

# L'installation

Chez Scrimba, les configurations compliquées ne sont pas notre truc.  
Pour ce tutoriel, nous avons créé un simple fichier HTML où tout peut être écrit. N'hésitez pas à écrire votre propre CSS ou à le copier depuis [ce terrain de jeu](https://scrimba.com/c/c66qG4uG)

Les bibliothèques Vue et Vuex sont importées via CDN en utilisant des balises `<script>` :

```html
<!DOCTYPE html>
<html lang="en">

 <head>


 
 <title>Voteur d'activités</title>


 
 <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

 
 <script src="https://cdn.jsdelivr.net/npm/vuex/dist/vuex.js"></script>

 
 <style>

 
 
 /*

 
 
 
 AJOUTER LE CSS ICI

 
 
 */

 
 </style>

 </head>

 <body>

 
 <div id="app"></div>

 </body>


 <script>

 
 /*

 
 
 AJOUTER LE CODE VUE ICI

 
 */

 </script>
</html>

```

Alternativement, vous pouvez également expérimenter avec le code dans [ce terrain de jeu Vue Scrimba](https://scrimba.com/c/cqRNMEcG). N'oubliez pas de **relier le terrain de jeu à votre propre compte**.

# Plan de l'application

Nous allons construire une application de vote, qui fonctionne particulièrement bien lorsque vous êtes dans un groupe d'amis ne sachant pas quoi faire et que vous devez considérer toutes les options.

La fonctionnalité consistera en un utilisateur pouvant taper une activité et ensuite chaque activité aura un bouton de vote positif et négatif pour compter les totaux.

# Commencer

Tout d'abord, créons rapidement une maquette de notre application en HTML. Nous utiliserons cette mise en page pour ensuite l'extraire dans un composant séparé et nous ajouterons la fonctionnalité pour que la mise en page prenne vie.

```html
<div id="app">

 <h1>Voteur d'activités</h1>

 <form>

 
 <input type="text" placeholder="Ajouter une activité" />

 
 <button id="button">Ajouter une activité</button>

 </form>

 <ul>

 
 <li>

 
 
 <span>
Aller faire du snowboard</span>
<span>?</span>

 
 
 
 <button>?</button>

 
 
 
 5

 
 
 
 <button>?</button>

 
 
 </span>

 
 </li>

 </ul>
</div>

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/42ixhwdzkncbibp1m210.png)

# Ajouter le magasin Vuex avec quelques données de base

Vuex commence avec le magasin. Le magasin est l'endroit où nous conservons (stoccons) notre état.

```html
<script>

 Vue.use(Vuex);


 const store = new Vuex.Store({


 });


 new Vue({

 
 el: "#app",

 
 store

 });
</script>


```

Ajoutons également quelques données codées en dur au magasin, qui incluront une activité et un tableau avec un emoji pour afficher nos sentiments envers l'activité.

```html
<script>

 Vue.use(Vuex);


 const store = new Vuex.Store({

 
 state: {

 
 
 activities: [{ name: "aller faire du snowboard", rating: 5 }],

 
 
 emojis: ["?"]

 
 }

 });


 new Vue({

 
 el: "#app",

 
 store

 });
</script>


```

Pour permettre à notre état de changer de manière réactive, nous pouvons utiliser `mapState` de Vuex pour gérer les propriétés d'état calculées pour nous.

```js

 new Vue({

 
 el: "#app",

 
 store,

 
 computed: Vuex.mapState(["activities", "emojis"])

 });


```

# Ajouter un composant

Maintenant, nous avons des activités dans notre état. Affichons un composant séparé pour chacune de ces activités. Chacun aura besoin des `activity` et `emojis` props.

```js
Vue.component("activity-item", {

 props: ["activity", "emojis"],

 template: `

 
 <li>

 
 
 <span>{{ activity.name }}

 
 
 
 <span>{{ emojis[0] }}</span>

 
 
 
 <button>?</button>

 
 
 
 {{activity.rating}}

 
 
 
 <button>?</button>

 
 
 </span>

 
 </li>

 
 `
});

```

À l'intérieur de `app`, nous pouvons maintenant utiliser notre nouveau composant avec toutes les liaisons appropriées pour `activity` et emojis. Pour rappel, si nous voulons parcourir un tableau et afficher un composant pour chaque élément d'un tableau, dans Vue, nous pouvons utiliser la liaison `v-for`.

```html
<div id="app">

 <h1>Voteur d'activités</h1>

 <form>

 
 <input type="text" placeholder="Ajouter une activité" />

 
 <button id="button">Ajouter une activité</button>

 </form>

 <ul>

 
 <activity-item

 
 
 v-for="item in activities"

 
 
 v-bind:activity="item"

 
 
 v-bind:emojis="emojis"

 
 
 v-bind:key="item.name">
</activity-item>

</ul>
</div>

```

![Image](https://thepracticaldev.s3.amazonaws.com/i/42ixhwdzkncbibp1m210.png)

# Ajouter des mutations au magasin

Si nous voulons mettre à jour le magasin dans Vuex, nous pouvons utiliser des mutations. Pour l'instant, nous allons simplement `console.log` qu'une mutation s'est produite et nous l'implémenterons ensuite.

```js
const store = new Vuex.Store({

 state: {

 
 activities: [

 
 
 { name: "aller faire du snowboard", rating: 5 },

 
 ],

 
 emojis: ["?"]

 },

 mutations: {

 
 increment(state, activityName) {

 
 
 console.log('increment');

 
 },

 
 decrement(state, activityName) {

 
 
 console.log('decrement');

 
 },

 }
});

```

Comment déclencher une mutation ? Nous appelons une fonction `commit` sur `$store` avec le nom des mutations que nous voulons exécuter. Tout argument après le nom d'une mutation est traité comme un argument pour une mutation commise.

```js
new Vue({

 el: "#app",

 store,

 data() {

 
 return {

 
 
 activityName: ""

 
 };

 },

 computed: Vuex.mapState(["activities", "emojis"]),

 methods: {

 
 increment(activityName) {

 
 
 this.$store.commit("increment", activityName);

 
 },

 
 decrement(activityName) {

 
 
 this.$store.commit("decrement", activityName);

 
 }

 }
});

```

# Ajouter une fonctionnalité au composant

Chaque `activity-item` a des boutons de vote qui doivent `increment` et `decrement` au clic d'un bouton. Nous pouvons passer ces fonctions en tant que props. Attachons maintenant nos méthodes aux props.

```html
<activity-item

 v-for="item in activities"

 v-bind:increment="increment"

 v-bind:decrement="decrement"

 v-bind:activity="item"

 v-bind:emojis="emojis"

 v-bind:key="item.name">
</activity-item>


```

N'oublions pas non plus de fournir `activity.name` comme argument aux deux.

```js
Vue.component("activity-item", {

 props: ["activity", "emojis", "increment", "decrement"],

 template: `

 
 <li>

 
 
 <span>{{ activity.name }}

 
 
 
 
 <span>{{ emojis[0] }}</span>

 
 
 
 
 <button @click="decrement(activity.name)">?</button>

 
 
 
 
 {{activity.rating}}

 
 
 
 
 <button @click="increment(activity.name)">?</button>

 
 
 </span>

 
 </li>

 
 `
});

```

Et voilà ! Le flux fonctionne. Nous pouvons voir l'instruction `console.log` dans la console.  


![Image](https://thepracticaldev.s3.amazonaws.com/i/2spr4ea73npem7pyv05h.png)

# Implémenter le compteur

Implémentons le compteur. Tout d'abord, nous devons trouver une activité par son nom, puis mettre à jour sa note.

```js

 mutations: {

 
 increment(state, activityName) {

 
 
 state.activities

 
 
 
 .filter(activity => activity.name === `${activityName}`)

 
 
 
 .map(activity => activity.rating++);

 
 },

 
 decrement(state, activityName) {

 
 
 state.activities

 
 
 
 .filter(activity => activity.name === `${activityName}`)

 
 
 
 .map(activity => activity.rating--);

 
 }

 }

```

Parfait, nous pouvons maintenant voter pour les activités.  


![Image](https://thepracticaldev.s3.amazonaws.com/i/eh23lvlqaszxq0rxmkel.png)

# Utiliser l'entrée du formulaire pour ajouter une activité

Mais bien sûr, nous devons également pouvoir ajouter des activités.

Créons une mutation pour le magasin, qui ajouterait une activité à la liste des activités existantes, avec un nom que nous obtiendrons plus tard depuis l'entrée et une note par défaut de 0.

```js

 mutations: {

 
 ...

 
 addActivity(state, name) {

 
 
 state.activities.push({ name, rating: 0 });

 
 }

 }

```

À l'intérieur des méthodes, nous pouvons commiter une nouvelle activité au magasin.

```js
methods: {

 
 ...

 
 addActivity(activityName) {

 
 
 this.$store.commit("addActivity", activityName);

 
 }

 }

```

# Implémenter la soumission du formulaire

Connectons la fonction de soumission à notre formulaire HTML.

```html
<form @submit="onSubmit">

 <input type="text" placeholder="Ajouter une activité" v-model="activityName" />

 <button id="button">Ajouter une activité</button>
</form>

```

Nous pouvons maintenant ajouter notre fonction de soumission aux méthodes. À l'intérieur, nous allons utiliser notre méthode `addActivity` existante et à la fin, réinitialiser `activityName` dans le champ d'entrée à une chaîne vide.

```js
methods: {

 
 ...

 
 onSubmit(e) {

 
 
 e.preventDefault();

 
 
 this.addActivity(this.activityName);

 
 
 this.activityName = "";

 
 }

 }

```

Nous appelons `e.preventDefault()` pour éviter que le formulaire ne se recharge à chaque ajout d'une nouvelle activité.

![Image](https://thepracticaldev.s3.amazonaws.com/i/qsnc185pcchj71c6878i.png)

Tous les compteurs fonctionnent maintenant et le champ est mis à jour. Il semble un peu étrange que nous n'ayons qu'une seule émotion pour toutes les activités, peu importe leur note.

Réécrivons les emojis en un objet avec une description de ce que les humeurs sont censées refléter et nettoyons l'état existant, afin que nous commençons sans activités.

```js
state: {

 
 activities: [],

 
 emojis: { yay: "?", nice: "?", meh: "?", argh: "?", hateIt: "?"}
},
...

```

Et en guise de touche finale, nous pouvons afficher différents emojis en fonction de la note qu'une activité a.

```js
Vue.component("activity-item", {

 props: ["activity", "emojis", "increment", "decrement"],

 template: `

 
 <li>

 
 
 <span>{{ activity.name }}

 
 
 
 <span v-if="activity.rating <= -5">{{ emojis.hateIt }}</span>

 
 
 
 <span v-else-if="activity.rating <= -3">{{ emojis.argh }}</span>

 
 
 
 <span v-else-if="activity.rating < 3">{{ emojis.meh }}</span>

 
 
 
 <span v-else-if="activity.rating < 5">{{ emojis.nice }}</span>

 
 
 
 <span v-else>{{ emojis.yay }}</span>

 
 
 
 <button @click="decrement(activity.name)">?</button>

 
 
 
 
 {{activity.rating}}

 
 
 
 <button @click="increment(activity.name)">?</button>

 
 
 </span>

 
 </li>

 
 `
});

```

Nous commençons avec une application vide, ce qui est ce que nous voulions.  


![Image](https://thepracticaldev.s3.amazonaws.com/i/7izt1gxbmnje90fiv9gq.png)

Et maintenant, si nous ajoutons les deux activités que nous avions dans l'application, votons sur les notes, nous avons des emojis qui reflètent ce que nous ressentons à propos des activités !  


![Image](https://thepracticaldev.s3.amazonaws.com/i/hclj6218rr3pxe5pnv19.png)

Vous pouvez consulter le code complet [ici](https://gist.github.com/perborgen/ce11d4f36cfb97f2ddb15ae73bfa10dd).