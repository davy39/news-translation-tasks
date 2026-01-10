---
title: Comment créer votre premier composant Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-12T20:46:51.000Z'
originalURL: https://freecodecamp.org/news/build-your-first-vue-js-component-2dc204bca514
coverImage: https://cdn-media-1.freecodecamp.org/images/1*-v3_fcCBOked8nrk2MfJEQ.gif
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
- name: Web Development
  slug: web-development
seo_title: Comment créer votre premier composant Vue.js
seo_desc: 'By Sarah Dayan

  I remember when I picked up CakePHP back in the day. I loved how easy it was to
  get started with it. Not only were the docs well-structured and exhaustive, but
  they were also user-friendly. Years later, this is exactly what I found wit...'
---

Par Sarah Dayan

Je me souviens quand j'ai commencé avec CakePHP à l'époque. J'adorais la facilité avec laquelle on pouvait commencer. Non seulement la documentation était bien structurée et exhaustive, mais elle était aussi conviviale. Des années plus tard, c'est exactement ce que j'ai trouvé avec Vue.js. Pourtant, il y a une chose que la documentation de Vue n'a pas encore par rapport à Cake : **un tutoriel de projet réel**.

Peu importe à quel point un framework est bien documenté, ce n'est pas suffisant pour tout le monde. Lire des concepts ne vous aide pas toujours à voir le tableau d'ensemble ou à comprendre comment vous pouvez les utiliser pour réellement _créer quelque chose_. Si vous êtes comme moi, vous apprenez mieux en faisant, et vous vous référez à la documentation pendant que vous codez, au fur et à mesure de vos besoins.

Dans ce tutoriel, nous allons créer un composant de **système de notation par étoiles**. Nous aborderons plusieurs concepts de Vue.js **quand nous en aurons besoin**, et nous couvrirons _pourquoi_ nous les utilisons.

![Image](https://cdn-media-1.freecodecamp.org/images/t4rMUcp4X4JvqdOVy60fxWKrmap6LoWXSWvk)

**_TL;DR_**_: cet article approfondit le comment et le pourquoi. Il est conçu pour vous aider à comprendre certains concepts fondamentaux de Vue.js et vous apprendre à prendre des décisions de conception pour vos futurs projets. Si vous voulez comprendre tout le processus de réflexion, continuez à lire. Sinon, vous pouvez consulter le code final sur [CodeSandbox](https://codesandbox.io/s/38k1y8x375)._

### Installation

Vue.js (à juste titre) se vante d'être exécutable en tant que simple inclusion de script, mais les choses sont un peu différentes lorsque vous souhaitez utiliser des [composants mono-fichier](https://vuejs.org/v2/guide/single-file-components.html). Maintenant, vous n'êtes pas _obligé_ de construire des composants de cette manière. Vous pouvez facilement vous en sortir en définissant un composant global avec `Vue.component`.

Le problème est que cela implique des compromis comme l'utilisation de modèles de chaînes, aucun support CSS scopé, et aucune étape de construction (donc, pas de préprocesseurs). Pourtant, nous voulons aller plus loin et apprendre à construire un composant réel que vous pourriez utiliser dans un projet réel. Pour ces raisons, nous allons opter pour une configuration réelle, alimentée par Webpack.

Pour garder les choses simples et réduire le temps de configuration, nous allons utiliser [vue-cli](https://github.com/vuejs/vue-cli) et le modèle [webpack-simple](https://github.com/vuejs-templates/webpack-simple) de Vue.js.

Tout d'abord, vous devez installer vue-cli globalement. Lancez votre terminal et tapez ce qui suit :

```
npm install -g vue-cli
```

Vous pouvez maintenant générer des modèles Vue.js prêts à l'emploi en quelques touches. Allez-y et tapez :

```
vue init webpack-simple chemin/vers/mon-projet
```

On vous posera quelques questions. Choisissez les valeurs par défaut pour toutes sauf « Use sass » à laquelle vous devez répondre oui (`y`). Ensuite, vue-cli initialisera le projet et créera le fichier `package.json`. Une fois terminé, vous pouvez naviguer vers le répertoire du projet, installer les dépendances et exécuter le projet :

```
cd chemin/vers/mon-projetnpm installnpm run dev
```

C'est tout ! Webpack commencera à servir votre projet sur le port `8080` (si disponible) et l'ouvrira dans votre navigateur. Si tout s'est bien passé, vous devriez voir une page de bienvenue comme celle-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/6Ul4wAVDccnjTOObnYxNuBSJb4-BTXtLyZFZ)

### Sommes-nous arrivés ?

Presque ! Pour déboguer correctement votre composant Vue.js, vous avez besoin des bons outils. Allez-y et installez l'extension de navigateur Vue.js devtools ([Firefox](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools)/[Chrome](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)/[Safari](https://github.com/vuejs/vue-devtools/blob/master/docs/workaround-for-safari.md)).

### Votre premier composant

L'une des meilleures fonctionnalités de Vue.js sont les **composants mono-fichier** (SFC). Ils vous permettent de définir la structure, le style et le comportement d'un composant dans un seul fichier, sans les inconvénients habituels de mélanger HTML, CSS et JavaScript.

Les SFC se terminent par une extension `.vue` et ont la structure suivante :

```
<template>  <!-- Votre HTML va ici --></template>
```

```
<script>  /* Votre JS va ici */<;/script>
```

```
<style>  /* Votre CSS va ici */&lt;/style>
```

Allons-y et créons notre premier composant : créez un fichier `Rating.vue` dans `/src/components`, et copiez/collez le code ci-dessus. Ensuite, ouvrez `/src/main.js` et adaptez le code existant :

```
import Vue from 'vue'import Rating from './components/Rating'
```

```
new Vue({  el: '#app',  template: '<Rating/>',  components: { Rating }})
```

Enfin, ajoutez un peu de HTML à votre `Rating.vue` :

```
<template>  <ul>    <li>Un</li>    <li>Deux</li>    <li>Trois</li>  </ul></template>
```

Maintenant, regardez la page dans votre navigateur, et vous devriez voir la liste ! Vue.js a attaché votre composant `<Rating>` à l'élément #app dans index.html. Si vous inspectez le HTML, vous ne devriez voir aucun signe de l'élément #app : Vue.js l'a remplacé par le composant.

**Note** : avez-vous remarqué que vous n'avez même pas eu besoin de recharger la page ? C'est parce que le [vue-loader](https://github.com/vuejs/vue-loader) de Webpack vient avec une fonctionnalité de _rechargement à chaud_. Contrairement au _rechargement en direct_ ou à la _synchronisation du navigateur_, le _rechargement à chaud_ ne rafraîchit pas la page chaque fois que vous modifiez un fichier. Au lieu de cela, il surveille les changements de composants et ne les rafraîchit que, en gardant l'état intact.

Maintenant, nous avons passé du temps à configurer les choses, mais il est temps d'écrire du code significatif.

### Le template

Nous allons utiliser [vue-awesome](https://www.npmjs.com/package/vue-awesome), un composant d'icônes SVG pour Vue.js construit avec [Font Awesome icons](http://fontawesome.io/). Cela nous permet de charger uniquement les icônes dont nous avons besoin. Allez-y et installez-le avec npm (ou Yarn) :

```
npm install vue-awesome
```

Ensuite, modifiez votre composant comme suit :

```
<template>  <div>    <ul>      <li><icon name="star"/></li>      <li><icon name="star"/></li>      <li><icon name="star"/></li>      <li><icon name="star-o"/></li>      <li><icon name="star-o"/></li>    </ul>    <span>3 sur 5</span>  </div></template>
```

```
<script>import 'vue-awesome/icons/star'import 'vue-awesome/icons/star-o'
```

```
import Icon from 'vue-awesome/components/Icon'
```

```
export default {  components: { Icon }}</script>
```

D'accord, **ralentissons un moment** et expliquons tout cela ?

Vue.js utilise des modules ES6 natifs pour gérer les dépendances et exporter des composants. Les deux premières lignes dans le bloc `<script>` importent des icônes individuellement, afin que vous ne vous retrouviez pas avec des icônes dont vous n'avez pas besoin dans votre bundle final. La troisième importe le composant `Icon` de `vue-awesome` afin que vous puissiez l'utiliser dans le vôtre.

`Icon` est un SFC Vue.js, comme celui que nous construisons. Si vous ouvrez le fichier, vous verrez qu'il a exactement la même structure que le nôtre.

Le bloc `export default` exporte un littéral d'objet comme modèle de vue de notre composant. Nous avons enregistré le composant `Icon` dans la propriété `components` afin de pouvoir l'utiliser localement dans le nôtre.

Enfin, nous avons utilisé `Icon` dans notre HTML `<template>` et lui avons passé une propriété `name` pour définir quelle icône nous voulons. Les composants peuvent être utilisés comme des balises HTML personnalisées en les convertissant en kebab-case (par exemple : `MyComponent` devient `<my-component>`). Nous n'avons pas besoin de nester quoi que ce soit à l'intérieur du composant, donc nous avons utilisé une balise auto-fermante.

**Note** : avez-vous remarqué que nous avons ajouté une balise `<div>` autour du HTML ? C'est parce que nous avons également ajouté un compteur dans une balise `<span>` au niveau racine, et les templates de composants dans Vue.js n'acceptent qu'un seul élément racine. Si vous ne respectez pas cela, vous obtiendrez une erreur de compilation.

### Le style

Si vous avez travaillé avec CSS pendant un certain temps, vous savez que l'un des principaux défis est de devoir gérer sa nature globale. L'imbrication a longtemps été considérée comme la solution à ce problème. Maintenant, nous savons qu'elle peut rapidement conduire à des problèmes de spécificité, rendant les styles difficiles à remplacer, impossibles à réutiliser et un cauchemar à mettre à l'échelle.

Des méthodologies comme [BEM](http://getbem.com/) ont été inventées pour contourner ce problème et maintenir une faible spécificité, en utilisant des espaces de noms pour les classes. Pendant un certain temps, cela a été la manière idéale d'écrire du CSS propre et évolutif. Ensuite, des frameworks et bibliothèques comme Vue.js ou React sont arrivés et ont apporté le **style scopé** à la table.

React a des composants stylés, Vue.js a le **CSS scopé aux composants**. Cela vous permet d'écrire du CSS spécifique aux composants sans avoir à inventer des astuces pour le garder contenu. Vous écrivez du CSS régulier avec des noms de classes « normaux », et Vue.js gère le scoping en attribuant des attributs de données aux éléments HTML et en les ajoutant aux styles compilés.

Ajoutons quelques classes simples au composant :

```
<template>  <div class="rating">    <ul class="list">      <li class="star active"><icon name="star"/></li>      <li class="star active"><icon name="star"/></li>      <li class="star active"><icon name="star"/></li>      <li class="star"><icon name="star-o"/></li>      <li class="star"><icon name="star-o"/></li>    </ul>    <span>3 sur 5</span>  </div></template>
```

Et stylisons-le :

```
<style scoped>  .rating {    font-family: 'Avenir', Helvetica, Arial, sans-serif;    font-size: 14px;    color: #a7a8a8;  }  .list {    margin: 0 0 5px 0;    padding: 0;    list-style-type: none;  }  .list:hover .star {    color: #f3d23e;  }  .star {    display: inline-block;    cursor: pointer;  }  .star:hover ~ .star:not(.active) {    color: inherit;  }  .active {    color: #f3d23e;  }&lt;/style>
```

Avez-vous vu cet attribut _scoped_ là-haut ? C'est ce qui indique à Vue.js de scopé les styles, afin qu'ils ne fuient nulle part ailleurs. Si vous copiez/collez le code HTML directement dans le `index.html`, vous remarquerez que vos styles ne s'appliqueront pas : c'est parce qu'ils sont scopés au composant ! ?

#### Et les préprocesseurs ?

Vue.js rend le passage du CSS simple à votre préprocesseur préféré très facile. Tout ce dont vous avez besoin est le bon loader Webpack et un simple attribut sur le bloc `<style>`. Nous avons dit « oui » à « Use sass » lors de la génération du projet, donc vue-cli a déjà installé et configuré [sass-loader](https://github.com/webpack-contrib/sass-loader) pour nous. Maintenant, tout ce que nous avons à faire est d'ajouter `lang="scss"` à la balise `<style>` d'ouverture.

Nous pouvons maintenant utiliser Sass pour écrire des styles au niveau des composants, importer des partials comme des variables, des définitions de couleurs ou des mixins, etc. Si vous préférez la syntaxe indentée (ou notation « sass »), il suffit de remplacer `scss` par `sass` dans l'attribut `lang`.

### Le comportement

Maintenant que notre composant a bonne apparence, il est temps de le faire fonctionner. Actuellement, nous avons un template codé en dur. Configurons un état initial simulé et ajustons le template pour qu'il le reflète :

```
<script>  ...  export default {    components: { Icon },    data() {      return {        stars: 3,        maxStars: 5      }    }  }<;/script>
```

```
/* ... */
```

```
<template>  <div class="rating">    <ul class="list">      <li v-for="star in maxStars" :class="{ 'active': star <= stars }" class="star">        <icon :name="star <= stars ? 'star' : 'star-o'"/>      </li>    </ul>    <span>3 sur 5</span>  </div></template>
```

Ce que nous avons fait ici, c'est utiliser `data` de Vue pour configurer l'état du composant. Chaque propriété que vous définissez dans `data` devient **réactive** : si elle change, elle sera reflétée dans la vue.

Nous créons un composant réutilisable, donc `data` doit être une fonction de fabrique au lieu d'un littéral d'objet. De cette façon, nous obtenons un nouvel objet au lieu d'une référence à un objet existant qui serait partagé entre plusieurs composants.

Notre fonction `data` retourne deux propriétés : `stars`, le nombre actuel d'étoiles « actives », et `maxStars`, le nombre total d'étoiles pour le composant. À partir de celles-ci, nous avons adapté notre template pour qu'il reflète l'état réel du composant. Vue.js vient avec un ensemble de directives qui vous permettent d'ajouter une logique de présentation à votre template sans la mélanger avec du JavaScript pur. La directive `v-for` parcourt n'importe quel objet itérable (tableaux, littéraux d'objets, maps, etc.). Elle peut également prendre un nombre comme une plage à répéter _x_ fois. C'est ce que nous avons fait avec `v-for="star in maxStars"`, afin d'avoir un `<li>` pour chaque étoile dans le composant.

Vous avez peut-être remarqué que certaines propriétés sont préfixées par un deux-points : il s'agit d'une abréviation pour la directive `v-bind`, qui lie dynamiquement les attributs à une expression. Nous aurions pu l'écrire sous sa forme longue, `v-bind:class`.

Nous devons ajouter la classe `active` aux éléments `<li>` lorsque l'étoile est active. Dans notre cas, cela signifie que chaque `<li>` dont l'index est inférieur à `stars` doit avoir la classe active. Nous avons utilisé une expression dans la directive `:class` pour n'ajouter `active` que lorsque l'étoile actuelle est inférieure à `stars`. Nous avons utilisé la même condition, cette fois avec un opérateur ternaire, pour définir quelle icône utiliser avec le composant `Icon` : `star` ou `star-o`.

#### Et le compteur ?

Maintenant que notre liste d'étoiles est liée à des données réelles, il est temps de faire de même pour le compteur. La manière la plus simple de faire cela est d'utiliser l'interpolation de texte avec la syntaxe des doubles accolades :

```
<span>{{ stars }} sur {{ maxStars }}&lt;/span>
```

Assez simple, n'est-ce pas ? Maintenant, dans notre cas, cela fait l'affaire. Mais si nous avions besoin d'une expression JavaScript plus complexe, il serait préférable de l'abstraire dans une **propriété calculée**.

```
export default {  ...  computed: {    counter() {      return `${this.stars} sur ${this.maxStars}`    }  }}
```

```
/* ... */
```

```
<span>{{ counter }}&lt;/span>
```

Ici, **c'est exagéré**. Nous pouvons nous en sortir avec des expressions dans le template et garder les choses lisibles. Pourtant, gardez à l'esprit les propriétés calculées pour lorsque vous devez gérer une logique plus complexe.

Une autre chose que nous devons faire est de fournir un moyen de masquer le compteur si nous ne le voulons pas. La manière la plus simple de faire cela est d'utiliser la directive `v-if` avec un booléen.

```
<span v-if="hasCounter">{{ stars }} sur {{ maxStars }}&lt;/span>
```

```
/* ... */
```

```
export default {  ...  data() {    return {      stars: 3,      maxStars: 5,      hasCounter: true    }  }}
```

#### Interactivité

Nous avons presque terminé, mais nous devons encore implémenter la partie la plus intéressante de notre composant : **la réactivité**. Nous allons utiliser `v-on`, la directive Vue.js qui gère les événements, et `methods`, une propriété Vue.js à laquelle vous pouvez attacher toutes vos méthodes.

```
<template>  ...  <li @click="rate(star)" ...>  ...</template>
```

```
/* ... */
```

```
export default {  ...  methods: {    rate(star) {      // faire des trucs    }  }}
```

Nous avons ajouté un attribut `@click` sur le `<li>`, qui est une abréviation pour `v-on:click`. Cette directive contient un appel à la méthode `rate` que nous avons définie dans la propriété `methods` du composant.

**_Attendez une minute, cela ressemble étrangement à l'attribut `onclick` de HTML. N'est-ce pas censé être une pratique obsolète et mauvaise d'utiliser du JavaScript en ligne dans HTML ?_**

En effet, mais même si la syntaxe ressemble beaucoup à `onclick`, comparer les deux serait une erreur. Lorsque vous construisez un composant Vue.js, vous ne devriez pas le considérer comme du HTML/CSS/JS séparé, mais plutôt comme un composant qui utilise plusieurs langages. Lorsque le projet est servi dans le navigateur ou compilé pour la production, tout le HTML et les directives sont compilés en JavaScript pur. Si vous inspectez le HTML rendu, vous ne verrez aucun signe de vos directives, ni aucun attribut `onclick`. Vue.js a compilé votre composant et créé des liaisons appropriées.

C'est aussi pourquoi vous avez accès au contexte du composant directement depuis votre template : parce que les directives sont liées au modèle de vue. Contrairement à un projet traditionnel avec du HTML séparé, le template fait partie intégrante du composant.

Revenons à notre méthode `rate`. Nous devons muter `stars` à l'index de l'élément cliqué, donc nous passons l'index depuis la directive `@click`, et nous pouvons faire ce qui suit :

```
export default {  ...  methods: {    rate(star) {      this.stars = star    }  }}
```

Allez vérifier la page dans votre navigateur et essayez de cliquer sur les étoiles : **ça marche !**

Si vous ouvrez le panneau Vue dans les outils de développement de votre navigateur et sélectionnez le composant `<Rating>`, vous verrez les données changer lorsque vous cliquez sur les étoiles. Cela vous montre que votre propriété `stars` est **réactive** : lorsque vous la mutez, elle envoie ses changements à la vue. Ce concept est appelé **liaison de données**, avec lequel vous devriez être familier si vous avez déjà utilisé des frameworks comme Backbone.js ou Knockout. La différence est que Vue.js, comme React, le fait dans une seule direction : cela s'appelle la **liaison de données unidirectionnelle**. Mais ce sujet mérite un article à part entière ?

À ce stade, nous pourrions dire que c'est terminé — mais il y a encore un peu de travail que nous pourrions faire pour améliorer l'expérience utilisateur.

Actuellement, nous ne pouvons pas vraiment donner une note de zéro, car cliquer sur une étoile définit la note à son index. Ce qui serait mieux, c'est de recliquer sur la même étoile et de faire basculer son état actuel au lieu de rester active.

```
export default {  ...  methods: {    rate(star) {      this.stars = this.stars === star ? star - 1 : star    }  }}
```

Maintenant, si l'index de l'étoile cliquée est égal à la valeur actuelle de `stars`, nous décrémentons sa valeur. Sinon, nous lui attribuons la valeur de `star`.

Si nous voulons être complets, nous devrions également ajouter une couche de contrôles pour nous assurer que `stars` ne reçoit jamais une valeur qui n'a pas de sens. Nous devons nous assurer que `stars` n'est jamais inférieur à `0`, jamais supérieur à `maxStars`, et que c'est un nombre valide.

```
export default {  ...  methods: {    rate(star) {      if (typeof star === 'number' && star <= this.maxStars && star >= 0) {        this.stars = this.stars === star ? star - 1 : star      }    }  }}
```

#### Passage de props

Actuellement, les données du composant sont codées en dur dans la propriété `data`. Si nous voulons que notre composant soit réellement utilisable, nous devons pouvoir lui passer des données personnalisées depuis ses instances. Dans Vue.js, nous faisons cela avec des **props**.

```
export default {  props: ['grade', 'maxStars', 'hasCounter'],  data() {    return {      stars: this.grade    }  },  ...}
```

Et dans `main.js` :

```
new Vue({  el: '#app',  template: '<Rating :grade="3" :maxStars="5" :hasCounter="true"/>',  components: { Rating }})
```

Il y a trois choses à observer ici :

Tout d'abord, nous avons utilisé la syntaxe raccourcie de `v-bind` pour passer des props depuis l'instance du composant : c'est ce que Vue.js appelle la **syntaxe dynamique**. Vous n'en avez pas besoin lorsque vous voulez passer une valeur de chaîne, pour laquelle la syntaxe littérale (attribut normal sans `v-bind`) fonctionnera. Mais dans notre cas, puisque nous passons des nombres et des booléens, il est important de le faire.

Les propriétés `props` et `data` sont fusionnées au moment de la compilation, donc nous n'avons pas besoin de changer la façon dont nous appelons les propriétés soit dans le modèle de vue soit dans le template. Mais pour la même raison, nous ne pouvons pas utiliser les mêmes noms pour les propriétés `props` et `data`.

Enfin, nous avons défini une prop `grade` et l'avons passée comme valeur à `stars` dans la propriété `data`. La raison pour laquelle nous avons fait cela au lieu d'utiliser la prop `grade` directement est que la valeur sera mutée lorsque nous changerons la note. Dans Vue.js, les props sont passées des parents aux enfants, et non l'inverse, afin que vous ne mutiez pas accidentellement l'état du parent. Cela irait à l'encontre du principe de [flux de données unidirectionnel](https://vuejs.org/v2/guide/components.html#One-Way-Data-Flow) et rendrait les choses plus difficiles à déboguer. C'est pourquoi vous ne devriez **pas** essayer de muter une prop à l'intérieur d'un composant enfant. Au lieu de cela, définissez une propriété `data` locale qui utilise la valeur initiale de la prop comme sa propre valeur.

#### Dernières retouches

Avant de conclure, il y a une dernière fonctionnalité de Vue.js que nous devrions explorer : **la validation des props**.

Vue.js vous permet de contrôler les props avant qu'elles ne soient passées au composant. Vous pouvez effectuer quatre choses principales : **vérifier le type**, **exiger qu'une prop soit définie**, **configurer des valeurs par défaut**, et **effectuer une validation personnalisée**.

```
export default {  props: {    grade: {      type: Number,      required: true    },    maxStars: {      type: Number,      default: 5    },    hasCounter: {      type: Boolean,      default: true    }  },  ...}
```

Nous avons utilisé la vérification de type pour nous assurer que le bon type de données est passé au composant. Cela sera particulièrement utile si nous oublions d'utiliser la syntaxe dynamique pour passer des valeurs non-chaines. Nous nous sommes également assurés que la prop `grade` était passée en l'exigeant. Pour les autres props, nous avons défini des valeurs par défaut afin que le composant fonctionne même si aucune donnée personnalisée n'est passée.

Maintenant, nous pouvons instancier le composant simplement en faisant ce qui suit :

```
<Rating :grade="3"/>
```

Et c'est tout ! Vous venez de créer votre premier composant Vue.js, et exploré de nombreux concepts incluant la génération d'un projet boilerplate avec [vue-cli](https://github.com/vuejs/vue-cli), les [composants mono-fichier](https://vuejs.org/v2/guide/single-file-components.html), l'importation de composants dans des composants, le [style scopé](https://vuejs.org/v2/guide/comparison.html#Component-Scoped-CSS), les [directives](https://vuejs.org/v2/guide/syntax.html#Directives), les [gestionnaires d'événements](https://vuejs.org/v2/guide/events.html#Method-Event-Handlers), les [propriétés calculées](https://vuejs.org/v2/guide/computed.html#Computed-Properties), les [méthodes personnalisées](https://vuejs.org/v2/guide/instance.html#Data-and-Methods), le [flux de données unidirectionnel](https://vuejs.org/v2/guide/components.html#One-Way-Data-Flow), les [props](https://vuejs.org/v2/guide/components.html#Props) et la [validation des props](https://vuejs.org/v2/guide/components.html#Prop-Validation). Et ce n'est qu'effleurer la surface de ce que Vue.js a à offrir !

C'est un tutoriel assez dense, donc ne vous inquiétez pas si vous n'avez pas tout compris. Relisez-le, faites des pauses entre les sections, explorez et [jouez avec le code sur CodeSandbox](https://codesandbox.io/s/38k1y8x375). Et si vous avez des questions ou des remarques sur le tutoriel, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/frontstuff_io) !

_Publié à l'origine sur [frontstuff.io](https://frontstuff.io/build-your-first-vue-js-component).