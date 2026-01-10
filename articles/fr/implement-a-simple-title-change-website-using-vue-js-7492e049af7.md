---
title: Comment implémenter une application simple de changement de titre en utilisant
  Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-27T14:31:48.000Z'
originalURL: https://freecodecamp.org/news/implement-a-simple-title-change-website-using-vue-js-7492e049af7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zyNSb0UXhP8TfxYbj-GNWg.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Comment implémenter une application simple de changement de titre en utilisant
  Vue.js
seo_desc: 'By Anoob Bava

  Vue.js is a progressive JavaScript framework. It has a lot of features including
  components, rendering, and routing. The Vue vs React argument is competitive in
  nature. They both have pros and cons in their field.

  I created a simple Jav...'
---

Par Anoob Bava

Vue.js est un framework JavaScript progressif. Il possède de nombreuses fonctionnalités, y compris des composants, le rendu et le routage. L'argument Vue vs React est de nature compétitive. Ils ont tous deux des avantages et des inconvénients dans leur domaine.

J'ai créé une application JavaScript simple dans Vue en utilisant un CDN (réseau de diffusion de contenu). L'application a un titre qui se convertira en majuscules en cliquant sur un bouton. Je sais que c'est une application simple. Mais nous pouvons apprendre beaucoup de choses simples à travers elle, comme :

* CDN pour Vue
* Objets Vue
* Lier un attribut à l'objet Vue
* Définir une propriété de données
* Définir une méthode en utilisant Vue
* Appeler la méthode Vue via des écouteurs

D'accord, mettons-nous au travail !

Je suis un grand fan de diviser la méthode en morceaux, alors nous suivrons la même approche ici.

1. Créer un fichier HTML et lier Vue via CDN.
2. Créer un objet Vue.
3. Lier le modèle HTML à l'objet Vue.
4. Créer une propriété de données.
5. Créer une méthode dans l'objet Vue.
6. Changer les données lors du clic sur un bouton.

#### 1. Créer un fichier HTML et lier Vue via CDN

Tout d'abord, créez un fichier appelé **index.html**. C'est notre joueur principal. Le fichier index.html contient à la fois la partie modèle HTML et l'objet Vue.

J'utilise Visual Studio Code ici.

![Image](https://cdn-media-1.freecodecamp.org/images/Vne3w5FAeTV7vb9-Vs4IKCNltCqYeirJ-LDP)

Maintenant, ajoutez le CDN à l'index.html. Nous pouvons utiliser soit la version de développement ou de production. Mais il sera bon d'utiliser la version de développement pour les avertissements et les erreurs. L'entrée pour la version de développement du CDN est actuellement :

```
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
```

#### 2. Créer un objet Vue

Maintenant, ce que nous devons créer est l'objet Vue à l'intérieur du fichier index.html. Il est créé sous la balise script <script></script>.

Il peut être créé par :

```
new Vue();
```

La syntaxe complète est ci-dessous :

```
<script>new Vue({el: ,
```

```
data: {
```

```
},
```

```
methods: {
```

```
}
```

```
});</script>
```

`new Vue` est une instance de Vue. Nous pouvons accéder à des propriétés comme el, data, methods etc pour être avec Vue. Les propriétés seront expliquées ci-dessous.

#### 3. Lier le modèle HTML à l'objet Vue

Comme nous le savons, Vue a une propriété appelée "el". Cette propriété lie le modèle HTML à l'objet Vue. Pour ce faire, tous les modèles HTML doivent être sous une seule div avec un id. Pour cette démonstration, nous pouvons utiliser un id de `app`. Nous avons ajouté ce qui suit au fichier index.html :

```
<div id='app'>
```

```
<h3> Bienvenue dans le changeur de titre</h3>
```

```
</div>
```

Maintenant, ajoutez l'id de l'application à l'objet Vue.

```
new Vue({
```

```
el: '#app',
```

```
});
```

Ainsi, le lien sera un succès.

#### 4. Créer une propriété de données

Maintenant, nous ne voulons pas que l'en-tête "Bienvenue dans le changeur de titre" soit un texte statique. Nous devons pouvoir afficher la valeur de la propriété de données Vue. Pour ce faire, Vue a une propriété intégrée appelée "data". Nous devons l'enregistrer ici et utiliser le nom dans le HTML comme ci-dessous :

```
new Vue({
```

```
el: '#app',
```

```
data: {
```

```
title: 'Bienvenue dans le changeur de titre'
```

```
},
```

```
});
```

Maintenant, dans la balise <h3>, peut être mise à jour avec les doubles accolades comme interpolation en Ruby. La valeur sera :

```
{{title}}
```

![Image](https://cdn-media-1.freecodecamp.org/images/SG2hAWsjA7L39a56BTzsmt6c7NM7vCowW-i9)

#### 5. Créer une méthode dans l'objet Vue

Vue a une propriété intégrée appelée "methods". Cette propriété prendra en charge les méthodes à déclarer à l'intérieur des objets Vue.

Nous pouvons utiliser la syntaxe ES6 également. Laissez-moi vous expliquer les deux ici.

```
methods: {
```

```
  changeTitle: function() {
```

```
      this.title = this.title.toUpperCase();
```

```
      return this.title;
```

```
   }
```

```
}
```

Le format ES6 est :

```
methods: {
```

```
    changeTitle() {
```

```
        this.title = this.title.toUpperCase();
```

```
        return this.title;
```

```
    }
```

```
}
```

`toUpperCase()` est simplement une méthode JavaScript qui convertira une chaîne en lettres majuscules. Un point important à noter ici est que nous pouvons accéder à la propriété de données en utilisant le mot-clé `this`. Ainsi, la valeur qui est déclarée dans la propriété de données peut être accessible en utilisant `this` dans les méthodes.

#### 6. Changer les données lors du clic sur un bouton

Maintenant, ce que nous faisons est simplement appeler la méthode en cliquant sur un bouton. Simple comme cela.

Pour ce faire, nous devons créer une balise bouton.

```
<button>cliquez pour changer en majuscules</button>
```

Pour lier le bouton à la méthode, nous devons utiliser un gestionnaire d'événements lors du clic sur le bouton. Vue fournit un écouteur intégré appelé `**v-on**`**.**

Voici la syntaxe :

```
v-on:click="call Action or Method"
```

Nous pouvons combiner avec :

```
<button v-on:click="changeTitle">cliquez pour changer en majuscules</button>
```

Ou **nous pouvons utiliser une syntaxe abrégée comme ci-dessous :**

```
<button @click="changeTitle">cliquez pour changer en majuscules</button>
```

C'est tout. Tout est fait.

Avant de cliquer sur le bouton, l'en-tête HTML est ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/wrxsJfTfPdMx7khAWwAdvtJHj98kOvXbnGv6)

Après avoir cliqué, il est converti en majuscules.

![Image](https://cdn-media-1.freecodecamp.org/images/l7mtoWPLJJdMNRTxP9yBGwJVTp7zBFJQeTfA)

C'est tout. Commentez si vous avez des problèmes ou des questions. J'ai joint les détails du dépôt ci-dessous.

[lien github](https://github.com/anoobbava/title_changer). Je mettrai à jour avec quelques fonctionnalités avancées dans Vue dans les prochaines leçons.