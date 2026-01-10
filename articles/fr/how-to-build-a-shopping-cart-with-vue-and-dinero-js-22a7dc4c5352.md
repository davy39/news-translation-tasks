---
title: Comment créer un panier d'achat avec Vue et Dinero.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-09T17:50:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-shopping-cart-with-vue-and-dinero-js-22a7dc4c5352
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zXIPhALV594QhOVSEBVRGA.jpeg
tags:
- name: money
  slug: money
- name: payments
  slug: payments
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Comment créer un panier d'achat avec Vue et Dinero.js
seo_desc: 'By Sarah Dayan

  My friend Cory and I chat almost every day, so you can bet he knows about everything
  going on in my life. But as we were talking the other day, I realized he had no
  idea how Dinero.js, my latest project, actually works. Like, what you ...'
---

Par Sarah Dayan

Mon ami [Cory](https://twitter.com/corydhmiller) et moi discutons presque tous les jours, alors vous pouvez parier qu'il sait tout ce qui se passe dans ma vie. Mais alors que nous parlions l'autre jour, je me suis rendu compte **qu'il n'avait aucune idée de la manière dont [Dinero.js](https://github.com/sarahdayan/dinero.js), mon dernier projet, fonctionne réellement**. Comme, ce que vous pouvez faire avec.

J'ai fait une pause et réalisé que cela n'était peut-être pas _si_ évident. C'est plus facile, quel que soit votre niveau de compétence, de comprendre ce qu'un plugin de défilement fluide fait plutôt que ce qu'une bibliothèque monétaire a à offrir.

> « Voyez-vous en JavaScript comment vous pouvez utiliser un constructeur de Date pour stocker une date et la formater plus tard ? Ou vous utilisez Moment.js pour créer des objets moment et comment c'est mieux que de stocker des dates sous forme de chaînes ou de tout autre type ?

> Eh bien, **Dinero.js est comme Moment, mais pour l'argent**. Il n'y a pas de moyen natif de gérer l'argent, et si vous essayez de le faire avec des types `Number`, vous allez rencontrer des problèmes. C'est ce que Dinero.js vous aide à éviter. Il sécurise vos valeurs monétaires dans des objets et vous permet de faire tout ce dont vous avez besoin avec eux. »

J'étais heureuse de mon explication, car Cory a commencé à _« a-ha »_-er. Mais je me suis rendu compte qu'une chose avait manqué depuis le début. Quelque chose qui en dirait long et aiderait quiconque à comprendre les avantages de Dinero.js : un **exemple concret**.

Dans ce tutoriel, nous allons construire un **panier d'achat**. Nous utiliserons Vue.js pour construire le composant, puis intégrer Dinero.js pour gérer tout ce qui concerne l'argent.

**_TL;DR :_** _cet article approfondit le comment et le pourquoi. Il est conçu pour vous aider à saisir les concepts de base de Dinero.js. Si vous voulez comprendre tout le processus de réflexion, continuez à lire. Sinon, vous pouvez consulter le code final sur [CodeSandbox](https://codesandbox.io/s/ojvmp7ryk5)._

Cet article suppose que vous avez des connaissances de base sur Vue.js. Si ce n'est pas le cas, consultez d'abord mon tutoriel [« Construisez votre premier composant Vue.js »](https://frontstuff.io/build-your-first-vue-js-component). Il vous fournira tout ce dont vous avez besoin pour aller plus loin.

### Mise en route

Pour ce projet, nous utiliserons [vue-cli](https://github.com/vuejs/vue-cli) et le modèle Vue.js [webpack-simple](https://github.com/vuejs-templates/webpack-simple). Si vous n'avez pas installé vue-cli globalement sur votre machine, lancez votre terminal et tapez ce qui suit :

```
npm install -g vue-cli
```

Ensuite :

```
vue init webpack-simple chemin/vers/mon-projet
```

Vous pouvez conserver les options par défaut pour toutes les questions. Une fois terminé, naviguez vers le nouveau répertoire, installez les dépendances et exécutez le projet :

```
cd chemin/vers/mon-projet npm install npm run dev
```

Webpack commencera à servir votre projet sur le port `8080` (si disponible) et l'ouvrira dans votre navigateur.

### Configuration du HTML/CSS

**Je ne vais pas entrer dans la structure de la page et le style dans ce tutoriel**, alors je vous invite à copier/coller le code. Ouvrez le fichier `App.vue`, et collez les extraits suivants.

Cela va entre les balises `<template>` :

```
<div id="app">  <div class="cart">    <h1 class="title">Commande</h1>    <ul class="items">      <li class="item">        <div class="item-preview">          <img src="" alt="" class="item-thumbnail">          <div>            <h2 class="item-title"></h2>            <p class="item-description"></p>          </div>        </div>        <div>          <input type="text" class="item-quantity">          <span class="item-price"></span>        </div>      </li>    </ul>    <h3 class="cart-line">      Sous-total <span class="cart-price"></span>    </h3>    <h3 class="cart-line">      Livraison <span class="cart-price"></span>    </h3>    <h3 class="cart-line">      Total <span class="cart-price cart-total"></span>    </h3>  </div></div>
```

Et cela entre les balises `<style>` :

```
body {  margin: 0;  background: #fdca40;  padding: 30px;}
```

```
.title {  display: flex;  justify-content: space-between;  align-items: center;  margin: 0;  text-transform: uppercase;  font-size: 110%;  font-weight: normal;}
```

```
.items {  margin: 0;  padding: 0;  list-style: none;}
```

```
.cart {  background: #fff;  font-family: 'Helvetica Neue', Arial, sans-serif;  font-size: 16px;  color: #333a45;  border-radius: 3px;  padding: 30px;}.cart-line {  display: flex;  justify-content: space-between;  align-items: center;  margin: 20px 0 0 0;  font-size: inherit;  font-weight: normal;  color: rgba(51, 58, 69, 0.8);}.cart-price {  color: #333a45;}.cart-total {  font-size: 130%;}
```

```
.item {  display: flex;  justify-content: space-between;  align-items: center;  padding: 15px 0;  border-bottom: 2px solid rgba(51, 58, 69, 0.1);}.item-preview {  display: flex;  align-items: center;}.item-thumbnail {  margin-right: 20px;  border-radius: 3px;}.item-title {  margin: 0 0 10px 0;  font-size: inherit;}.item-description {  margin: 0;  color: rgba(51, 58, 69, 0.6);}.item-quantity {  max-width: 30px;  padding: 8px 12px;  font-size: inherit;  color: rgba(51, 58, 69, 0.8);  border: 2px solid rgba(51, 58, 69, 0.1);  border-radius: 3px;  text-align: center;}.item-price {  margin-left: 20px;}
```

### Ajout de données

Lorsque vous traitez des produits, vous récupérez généralement des données brutes à partir d'une base de données ou d'une API. Nous pouvons nous en approcher en les représentant dans un fichier JSON séparé, puis en les important de manière asynchrone comme si nous interrogions une API.

Créons un fichier `products.json` dans `assets/` et ajoutons ce qui suit :

```
{  "items": [    {      "title": "Article 1",      "description": "Un produit merveilleux",      "thumbnail": "https://fakeimg.pl/80x80",      "quantity": 1,      "price": 20    },    {      "title": "Article 2",      "description": "Un produit merveilleux",      "thumbnail": "https://fakeimg.pl/80x80",      "quantity": 1,      "price": 15    },    {      "title": "Article 3",      "description": "Un produit merveilleux",      "thumbnail": "https://fakeimg.pl/80x80",      "quantity": 2,      "price": 10    }  ],  "shippingPrice": 20}
```

**Cela ressemble beaucoup à ce que nous obtiendrions d'une vraie API** : des données sous forme de collection, avec des titres et du texte sous forme de chaînes, et des quantités et des prix sous forme de nombres.

Nous pouvons revenir à `App.vue` et définir des valeurs vides dans `data`. Cela permettra au modèle de s'initialiser pendant que les données réelles sont en cours de récupération.

```
data() {  return {    data: {      items: [],      shippingPrice: 0    }  }}
```

Enfin, nous pouvons récupérer les données de `products.json` avec une requête asynchrone, et mettre à jour la propriété `data` lorsqu'elles sont prêtes :

```
export default {  ...  created() {    fetch('./src/assets/products.json')      .then(response => response.json())      .then(json => (this.data = json))  }}
```

Maintenant, remplissons notre modèle avec ces données :

```
<ul class="items">  <li :key="item.id" v-for="item in data.items" class="item">    <div class="item-preview">      <img :src="item.thumbnail" :alt="item.title" class="item-thumbnail">      <div>        <h2 class="item-title">{{ item.title }}</h2>        <p class="item-description">{{ item.description }}</p>      </div>    </div>    <div>      <input type="text" class="item-quantity" v-model="item.quantity">      <span class="item-price">{{ item.price }}</span>    </div>  </li></ul>...<h3 class="cart-line">  Livraison  <span class="cart-price">{{ data.shippingPrice }}</span></h3>...
```

**Vous devriez voir tous les articles dans votre panier.** Maintenant, ajoutons quelques propriétés calculées pour calculer le sous-total et le total :

```
export default {  ...  computed: {    getSubtotal() {      return this.data.items.reduce(        (a, b) => a + b.price * b.quantity,        0      )    },    getTotal() {      return (        this.getSubtotal + this.data.shippingPrice      )    }  }}
```

Et ajoutons-les à notre modèle :

```
<h3 class="cart-line">  Sous-total  <span class="cart-price">{{ getSubtotal }}</span></h3>...<h3 class="cart-line">  Total  <span class="cart-price cart-total">{{ getTotal }}</span></h3>
```

Nous y voilà ! Essayez de changer les quantités — vous devriez voir les montants du sous-total et du total changer en conséquence.

**Nous avons maintenant quelques problèmes ici.** Tout d'abord, nous n'affichons que les montants, pas les devises. Bien sûr, nous pourrions les coder en dur dans le modèle à côté des montants réactifs. Mais que faire si nous voulons créer un site web multilingue ? Toutes les langues ne formatent pas l'argent de la même manière.

Et si nous voulons afficher tous les montants avec deux décimales, pour un meilleur alignement ? Vous pourriez essayer de garder tous les montants initiaux sous forme de flottants en utilisant la méthode `toFixed`, mais vous travailleriez alors avec des types `String` qui sont beaucoup plus difficiles et moins performants lorsqu'il s'agit de faire des maths. De plus, cela signifierait changer les données à des fins purement présentationnelles, ce qui n'est jamais une bonne idée. Et si vous avez besoin des mêmes données pour d'autres fins et qu'elles nécessitent un format différent ?

Enfin, la solution actuelle repose sur les maths en virgule flottante, **ce qui est une [mauvaise idée lorsqu'il s'agit de gérer de l'argent](https://frontstuff.io/how-to-handle-monetary-values-in-javascript)**. Essayez de changer quelques montants :

```
{  "items": [    {      ...      "price": 20.01    },    {      ...      "price": 15.03    },    ...  ]}
```

Maintenant, regardez à quel point votre panier d'achat est cassé ? Ce n'est pas un comportement buggé de JavaScript, mais une **limitation de la manière dont nous pouvons représenter notre système de numération décimale avec des machines binaires.** Si vous faites des maths avec des flottants, vous rencontrerez tôt ou tard ces inexactitudes.

La bonne nouvelle est que **nous n'avons pas à utiliser des flottants pour stocker de l'argent**. C'est exactement là que Dinero.js entre en jeu.

### Dinero.js, un wrapper pour l'argent

**Dinero.js est à l'argent ce que Moment.js est aux dates.** C'est une bibliothèque qui vous permet de créer des [objets de valeur](https://fr.wikipedia.org/wiki/Value_object) monétaires, de les manipuler, de leur poser des questions et de les formater. Elle repose sur le [modèle de monnaie](https://martinfowler.com/eaaCatalog/money.html) de Martin Fowler et vous aide à résoudre tous les problèmes courants causés par les flottants, principalement en stockant les montants en unités de monnaie mineures, sous forme d'entiers.

Ouvrez votre terminal et installez Dinero.js :

```
npm install dinero.js --save
```

Puis importez-le dans `App.vue` :

```
import Dinero from 'dinero.js'
```

```
export default {  ...}
```

Vous pouvez maintenant créer des objets Dinero ?

```
// retourne un objet Dinero avec un montant de 50 $Dinero({ amount: 500, currency: 'USD' })
```

```
// retourne 4 000,00 $Dinero({ amount: 500 })  .add(Dinero({ amount: 500 }))  .multiply(4)  .toFormat()
```

Créons une méthode de fabrication pour transformer nos propriétés `price` en objets Dinero à la demande. Nous avons des flottants avec jusqu'à deux décimales. Cela signifie que si nous voulons les transformer en leurs équivalents en unités de monnaie mineures (dans notre cas, des dollars), **nous devons les multiplier par 10 à la puissance de 2**.

Nous passons le `factor` comme argument avec une valeur par défaut, afin de pouvoir utiliser la méthode avec des devises ayant différents [exposants](https://fr.wikipedia.org/wiki/ISO_4217#Traitement_des_unit%C3%A9s_de_monnaie_mineures_.28l.27exposant.29).

```
export default {  ...  methods: {    toPrice(amount, factor = Math.pow(10, 2)) {      return Dinero({ amount: amount * factor })    }  }}
```

Les dollars sont la devise par défaut, donc nous n'avons pas besoin de la spécifier.

Parce que nous faisons des maths en virgule flottante pendant la conversion, certains calculs peuvent aboutir à des flottants légèrement inexacts. C'est facile à corriger en arrondissant le résultat à l'entier le plus proche.

```
toPrice(amount, factor = Math.pow(10, 2)) {  return Dinero({ amount: Math.round(amount * factor) })}
```

Maintenant, nous pouvons utiliser `toPrice` dans nos propriétés calculées :

```
export default {  ...  computed: {    getShippingPrice() {      return this.toPrice(this.data.shippingPrice)    },    getSubtotal() {      return this.data.items.reduce(        (a, b) =>          a.add(            this.toPrice(b.price).multiply(b.quantity)          ),        Dinero()      )    },    getTotal() {      return this.getSubtotal.add(this.getShippingPrice)    }  }}
```

Et dans notre modèle :

```
<ul class="items">  <li :key="item.id" v-for="item in data.items" class="item">    <div class="item-preview">      <img :src="item.thumbnail" :alt="item.title" class="item-thumbnail">      <div>        <h2 class="item-title">{{ item.title }}</h2>        <p class="item-description">{{ item.description }}</p>      </div>    </div>    <div>      <input type="text" class="item-quantity" v-model="item.quantity">      <span class="item-price">{{ toPrice(item.price) }}</span>    </div>  </li></ul><h3 class="cart-line">  Sous-total  <span class="cart-price">{{ getSubtotal }}</span></h3><h3 class="cart-line">  Livraison  <span class="cart-price">{{ getShippingPrice }}</span></h3><h3 class="cart-line">  Total  <span class="cart-price cart-total">{{ getTotal }}</span></h3>
```

Si vous regardez votre panier d'achat, vous verrez `{}` à la place des prix. C'est parce que nous essayons d'afficher un objet. Au lieu de cela, **nous devons les formater pour qu'ils puissent afficher les prix avec la bonne syntaxe**, aux côtés de leur symbole de devise.

Nous pouvons y parvenir avec la méthode `[toFormat](https://sarahdayan.github.io/dinero.js/module-Dinero.html#~toFormat)` de Dinero.

```
<ul class="items">  <li :key="item.id" v-for="item in data.items" class="item">    ...    <div>      ...      <span class="item-price">        {{ toPrice(item.price).toFormat() }}      </span>    </div>  </li></ul><h3 class="cart-line">  Sous-total  <span class="cart-price">    {{ getSubtotal.toFormat() }}  </span></h3><h3 class="cart-line">  Livraison  <span class="cart-price">    {{ getShippingPrice.toFormat() }}  </span></h3><h3 class="cart-line">  Total  <span class="cart-price cart-total">    {{ getTotal.toFormat() }}  </span></h3>
```

Regardez dans votre navigateur : **vous avez maintenant un panier d'achat bien formaté et entièrement fonctionnel** ?

### Aller plus loin

Maintenant que vous avez une bonne compréhension des bases de Dinero.js, il est temps d'élever un peu la barre.

#### Présentation

Changeons `shippingPrice` en `0` dans le fichier JSON. Votre panier devrait maintenant afficher _« Livraison : 0,00 $ »_, ce qui est exact mais pas très convivial. Ne serait-il pas plus agréable qu'il affiche _« Gratuit »_ ?

Heureusement, Dinero.js dispose de nombreuses méthodes pratiques pour poser des questions à vos instances. Dans notre cas, la méthode `[isZero](https://sarahdayan.github.io/dinero.js/module-Dinero.html#~isZero)` est exactement ce dont nous avons besoin.

Dans le modèle, vous pouvez afficher du texte au lieu d'un objet Dinero formaté chaque fois qu'il représente zéro :

```
<h3 class="cart-line">  Livraison  <span class="cart-price">    {{      getShippingPrice.isZero() ?      'Gratuit' :      getShippingPrice.setLocale(getLocale).toFormat()    }}  </span></h3>
```

Bien sûr, vous pouvez généraliser ce comportement en l'enveloppant dans une méthode. Elle prendrait un objet Dinero comme argument et retournerait une `String`. De cette façon, vous pourriez afficher _« Gratuit »_ chaque fois que vous essayez d'afficher un montant nul.

#### Changement de locale

Imaginez que vous créez un site web de commerce électronique. Vous voulez accommoder votre public international, alors vous traduisez le contenu et ajoutez un sélecteur de langue. Pourtant, il y a un détail qui pourrait échapper à votre attention : **le formatage de l'argent change également en fonction de la langue**. Par exemple, 10,00 € en anglais américain se traduit par 10,00 € en français.

Dinero.js prend en charge le formatage international via l'[API I18n](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Objets_globaux/Intl). Cela vous permet d'afficher les montants avec un formatage localisé.

Dinero.js est immutable, donc nous ne pouvons pas compter sur le changement de `[Dinero.globalLocale](https://sarahdayan.github.io/dinero.js/global.html#Globals)` pour reformater toutes les instances existantes. Au lieu de cela, nous devons utiliser la méthode `[setLocale](https://sarahdayan.github.io/dinero.js/module-Dinero.html#~setLocale)`.

Tout d'abord, nous ajoutons une nouvelle propriété `language` dans `data` et la définissons à une valeur par défaut. Pour les locales, vous devez utiliser une [balise de langue BCP 47](http://tools.ietf.org/html/rfc5646) telle que `fr-FR`.

```
data() {  return {    data: {      ...    },    language: 'fr-FR'  }}
```

Maintenant, nous pouvons utiliser `setLocale` directement sur les objets Dinero. Lorsque `language` change, le formatage changera également.

```
export default {  ...  methods: {    toPrice(amount, factor = Math.pow(10, 2)) {      return Dinero({ amount: Math.round(amount * factor) })        .setLocale(this.language)    }  },  computed: {    ...    getSubtotal() {      return this.data.items.reduce(        (a, b) =>          a.add(            this.toPrice(b.price).multiply(b.quantity)          ),        Dinero().setLocale(this.language)      )    },    ...  }}
```

Tout ce dont nous avons besoin est d'ajouter `setLocale` dans `toPrice` et `getSubtotal`, les seuls endroits où nous créons des objets Dinero.

Maintenant, nous pouvons ajouter notre sélecteur de langue :

```
// HTML<h1 class="title">  Commande  <span>    <span class="language" @click="language = 'en-US'">Anglais</span>    <span class="language" @click="language = 'fr-FR'">Français</span>  </span></h1>
```

```
// CSS.language {  margin: 0 2px;  font-size: 60%;  color: rgba(#333a45, 0.6);  text-decoration: underline;  cursor: pointer;}
```

Lorsque vous cliquez sur le sélecteur, il réassigne `language`, ce qui change la manière dont les objets sont formatés. Parce que la bibliothèque est immutable, cela retournera de nouveaux objets au lieu de changer ceux existants. Cela signifie que si vous créez un objet Dinero et décidez de l'afficher quelque part, puis le référencez ailleurs et appliquez un `setLocale` dessus, **votre instance initiale ne sera pas affectée**. Pas d'effets secondaires gênants !

#### Toutes taxes comprises

Il est courant de voir une ligne de taxe sur les paniers d'achat. Vous pouvez en ajouter une avec Dinero.js, en utilisant la méthode `[percentage](https://sarahdayan.github.io/dinero.js/module-Dinero.html#~percentage)`.

Tout d'abord, ajoutons une propriété `vatRate` dans le fichier JSON :

```
{  ...  "vatRate": 20}
```

Et une valeur initiale dans `data` :

```
data() {  return {    data: {      ...      vatRate: 0    }  }}
```

Maintenant, nous pouvons utiliser cette valeur pour calculer le total de notre panier avec la taxe. Tout d'abord, nous devons créer une propriété calculée `getTaxAmount`. Nous pouvons ensuite l'ajouter à `getTotal` également.

```
export default {  ...  computed: {    getTaxAmount() {      return this.getSubtotal.percentage(this.data.vatRate)    },    getTotal() {      return this.getSubtotal        .add(this.getTaxAmount)        .add(this.getShippingPrice)    }  }}
```

Le panier d'achat montre maintenant le total avec la taxe. Nous pouvons également ajouter une ligne pour montrer le montant de la taxe :

```
<h3 class="cart-line">  TVA ({{ data.vatRate }}%)  <span class="cart-price">{{ getTaxAmount.toFormat() }}</span></h3>
```

Et nous avons terminé ! Nous avons exploré plusieurs concepts de Dinero.js, mais ce n'est qu'effleurer la surface de ce qu'il a à offrir. Vous pouvez [lire la documentation](https://sarahdayan.github.io/dinero.js) et consulter le projet sur [GitHub](https://github.com/sarahdayan/dinero.js). Étoilez-le, fork-le, envoyez-moi des commentaires, ou même ouvrez une pull request ! J'ai un petit [guide de contribution](https://github.com/sarahdayan/dinero.js/blob/master/CONTRIBUTING.md) pour vous aider à commencer.

Vous pouvez également consulter le code final sur [CodeSandbox](https://codesandbox.io/s/ojvmp7ryk5).

Je travaille actuellement sur l'ajout d'une méthode `convert` à Dinero.js, ainsi que sur une meilleure prise en charge de toutes les [devises ISO 4217](https://fr.wikipedia.org/wiki/ISO_4217) et des cryptomonnaies. Vous pouvez rester informé en me suivant sur [Twitter](https://twitter.com/frontstuff_io).

Bon codage ! ???

_Publié à l'origine sur [frontstuff.io](https://frontstuff.io/build-a-shopping-cart-with-vue-and-dinerojs).