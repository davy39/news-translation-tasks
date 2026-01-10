---
title: Comment créer un menu de surlignage de type Medium dans Vue
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-19T17:57:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-medium-like-highlight-menu-in-vue-dc515f2dddef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gL6zqT6rsqYsl8-evfS2vg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Comment créer un menu de surlignage de type Medium dans Vue
seo_desc: 'By Taha Shashtari

  A cool feature in Medium is the highlight menu that pops up when you select some
  text. This menu contains buttons that allow you to perform certain actions on the
  selected text like highlight and share.

  If you like this feature and ...'
---

Par Taha Shashtari

Une fonctionnalité intéressante dans [Medium](https://medium.com/) est le menu de surlignage qui apparaît lorsque vous sélectionnez du texte. Ce menu contient des boutons qui permettent d'effectuer certaines actions sur le texte sélectionné comme le surligner et le partager.

Si vous aimez cette fonctionnalité et que vous souhaitez l'avoir sur votre site, je vais vous montrer comment créer un composant réutilisable qui active ce comportement sur le texte qu'il contient.

Vous pouvez essayer une démonstration en direct sur CodePen :

_Voir le CodePen [ici](https://codepen.io/tahazsh/pen/WYywXW)._

### Création d'un nouveau projet avec Vue CLI 3

Avec l'[instant prototyping](https://cli.vuejs.org/guide/prototyping.html#vue-serve) de Vue CLI 3, nous pouvons exécuter rapidement une application Vue avec un seul fichier `*.vue`.

Notez que cela n'est utilisé que pour créer des prototypes, pas pour la production.

Tout d'abord, assurez-vous d'avoir installé cela globalement :

`npm install -g @vue/cli-service-global`

Dans cette application, nous n'aurons besoin que de deux fichiers : _App.vue_ et _Highlightable.vue_.

_Highlightable.vue_ est notre composant de menu de surlignage réutilisable. Et _App.vue_ est le composant principal de la page.

Créez les deux fichiers dans le répertoire de votre choix ; puis exécutez `vue serve` sur _App.vue_.

```
vue serve App.vue
```

### Implémentation de App.vue

Dans _App.vue_, nous allons ajouter deux paragraphes. L'un qui peut être surligné, et l'autre qui ne le peut pas.

Nous allons également importer et utiliser _Highlightable.vue_ avant même de le créer. (Cela est utile pour voir comment nous allons l'utiliser.)

Voici à quoi cela devrait ressembler à la fin :

```
<template>  <div class="app">    <highlightable      @share="onShare"      @highlight="onHighlight"    >      <p>        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet at debitis deserunt, optio rem eaque obcaecati non possimus nisi assumenda architecto exercitationem dolore quo praesentium, deleniti reiciendis sed ab nihil!      </p>    </highlightable>    <p>      <strong>Ce paragraphe ne peut pas être surligné.</strong> Lorem ipsum dolor sit amet, consectetur adipisicing elit. Labore ipsam repellat, fugiat aut ex incidunt ut quisquam quasi consequatur ducimus quo in, cum soluta eos dolores tempore unde voluptate modi.    </p>  </div></template><script>import Highlightable from './Highlightable'export default {  components: { Highlightable },  methods: {    onShare (text) {      console.log('share:', text)    },    onHighlight (text) {      console.log('highlight:', text)    }  }}</script><style scoped>* {  box-sizing: border-box;}.app {  width: 800px;  margin: 40px auto;  padding: 10px;  font-family: Verdana;  color: #333;  width: 100%;}p {  line-height: 1.5;}</style>
```

Comme vous pouvez le voir ci-dessus, nous gérons deux événements de _Highlightable_. Ces deux événements sont les actions des boutons dans le menu de surlignage. Ce ne sont que des exemples. Vous pouvez les modifier comme vous le souhaitez.

### Implémentation de Highlightable.vue

La section template se compose de deux parties : l'élément de menu avec les boutons et `<slot/>` pour afficher le texte.

Commençons par ce code dans le _template_ :

```
<template>  <div>    <div      v-show="showMenu"      class="menu"    >      <span class="item">        Partager      </span>      <span class="item">        Surligner      </span>      <!-- Vous pouvez ajouter plus de boutons ici -->    </div>    <!-- Le texte inséré doit être affiché ici -->    <slot/>  </div></template>
```

Notez que nous utilisons `showMenu`, que nous n'avons pas encore créé, pour déterminer si nous devons afficher le menu.

Passons maintenant à la partie stylisation.

Ajoutez le CSS suivant à la section `<style>` :

```
<style scoped>.menu {  height: 30px;  padding: 5px 10px;  background: #333;  border-radius: 3px;  position: absolute;  top: 0;  left: 0;  transform: translate(-50%, -100%);  transition: 0.2s all;  display: flex;  justify-content: center;  align-items: center;}.menu:after {  content: '';  position: absolute;  left: 50%;  bottom: -5px;  transform: translateX(-50%);  width: 0;  height: 0;  border-left: 6px solid transparent;  border-right: 6px solid transparent;  border-top: 6px solid #333;}.item {  color: #FFF;  cursor: pointer;}.item:hover {  color: #1199ff;}.item + .item {  margin-left: 10px;}</style>
```

Rien de trop complexe ici. `.menu` est pour le menu de surlignage. `menu:after` est pour le petit triangle (flèche) au centre inférieur du menu.

Une chose importante à noter ici est que `.menu` a une position `absolute`. Nous en avons besoin pour le positionner au-dessus du texte sélectionné.

Enfin, passons à la section `<script>`.

Commençons par les _data_.

```
export default {  data () {    return {      x: 0,      y: 0,      showMenu: false,      selectedText: ''    }  }}
```

* `x` et `y` sont pour positionner le menu.
* `showMenu` pour afficher/masquer le menu.
* `selectedText` contiendra le contenu réel du texte sélectionné.

Passons maintenant à _computed_.

```
computed: {  highlightableEl () {    return this.$slots.default[0].elm  }}
```

Nous n'avons qu'une seule propriété calculée qui retourne l'élément utilisé dans la section slot de _Highlightable_. Dans notre exemple, ce serait la balise `<p>` entre `<highlightable>` et `</highlightable>`.

Ensuite, ajoutons les fonctions de hook `mounted` et `beforeDestroy`.

```
mounted () {  window.addEventListener('mouseup', this.onMouseup)},beforeDestroy () {  window.removeEventListener('mouseup', this.onMouseup)}
```

Nous les utilisons pour écouter l'événement `mouseup`, que nous gérons dans la méthode `onMouseup`.

Maintenant, créons la méthode `onMouseup`.

```
methods: {  onMouseup () {    const selection = window.getSelection()    const selectionRange = selection.getRangeAt(0)    // startNode est l'élément dans lequel la sélection commence    const startNode = selectionRange.startContainer.parentNode    // endNode est l'élément dans lequel la sélection se termine    const endNode = selectionRange.endContainer.parentNode    // si le texte sélectionné ne fait pas partie de highlightableEl (c'est-à-dire <p>)    // OU    // si startNode !== endNode (c'est-à-dire que l'utilisateur a sélectionné plusieurs paragraphes)    // Alors    // Ne pas afficher le menu (cette sélection est invalide)    if (!startNode.isSameNode(this.highlightableEl) || !startNode.isSameNode(endNode)) {      this.showMenu = false      return    }    // Obtenir les x, y, et width de la sélection    const { x, y, width } = selectionRange.getBoundingClientRect()    // Si width === 0 (c'est-à-dire aucune sélection)    // Alors, masquer le menu    if (!width) {      this.showMenu = false      return    }    // Enfin, si la sélection est valide,    // définir la position de l'élément de menu,    // définir selectedText au contenu de la sélection    // puis, afficher le menu    this.x = x + (width / 2)    this.y = y + window.scrollY - 10    this.selectedText = selection.toString()    this.showMenu = true  }}
```

Maintenant, mettons à jour le template de _Highlightable.vue_ pour refléter les nouvelles modifications.

```
<template>  <div>    <div      v-show="showMenu"      class="menu"      :style="{        left: `${x}px`,        top: `${y}px`      }"      @mousedown.prevent=""    >      <span        class="item"        @mousedown.prevent="handleAction('share')"      >        Partager      </span>      <span        class="item"        @mousedown.prevent="handleAction('highlight')"      >        Surligner      </span>      <!-- Vous pouvez ajouter plus de boutons ici -->    </div>    <!-- Le texte inséré doit être affiché ici -->    <slot/>  </div></template>
```

Les modifications sont :

* Appliqué les positions à l'élément de menu.
* Ajouté `@mousedown.prevent=""` à l'élément de menu pour empêcher le menu de se fermer lorsque l'on clique à l'intérieur.
* Ajouté `@mousedown.prevent="handleAction('share')"` sur le bouton de partage pour gérer l'action cliquée. Il en va de même pour l'action de surlignage.

Notez que nous utilisons l'événement `mousedown` au lieu de `click` pour empêcher le texte de se désélectionner, ce qui ferait fermer le menu.

La dernière chose que nous devons faire est d'ajouter la méthode `handleAction`.

```
handleAction (action) {  this.$emit(action, this.selectedText)}
```

Cette méthode émet l'événement `action` et passe le texte sélectionné avec lui. (Nous avons utilisé cet événement dans _App.vue_, vous vous souvenez ?)

Avec cela, nous avons terminé ! Vous avez maintenant un composant réutilisable que vous pouvez utiliser pour afficher un menu de surlignage pour le texte sélectionné, tout comme Medium le fait.

_Merci d'avoir lu ! Au fait, j'écris un livre sur la façon de construire une application monopage complète à partir de zéro en utilisant Vue. Consultez la page de destination du livre si vous êtes intéressé à en savoir plus sur ce que le livre couvrira :_

![Image](https://cdn-media-1.freecodecamp.org/images/1*L2FgqLU76lIbry3RZYFY8g.png)