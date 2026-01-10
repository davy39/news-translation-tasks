---
title: Une introduction au rendu dynamique de listes dans Vue.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-01T15:32:32.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-dynamic-list-rendering-in-vue-js-a70eea3e321
coverImage: https://cdn-media-1.freecodecamp.org/images/1*smV1EYFRTT4wGha020XFIA.png
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
- name: Web Development
  slug: web-development
seo_title: Une introduction au rendu dynamique de listes dans Vue.js
seo_desc: 'By Hassan Djirdeh

  List rendering is one of the most commonly used practices in front-end web development.
  Dynamic list rendering is often used to present a series of similarly grouped information
  in a concise and friendly format to the user. In almos...'
---

Par Hassan Djirdeh

Le rendu de listes est l'une des pratiques les plus couramment utilisées dans le développement web front-end. Le rendu dynamique de listes est souvent utilisé pour présenter une série d'informations regroupées de manière similaire dans un format concis et convivial pour l'utilisateur. Dans presque toutes les applications web que nous utilisons, nous pouvons voir des **listes** de contenu dans de nombreuses zones de l'application.

Dans cet article, nous allons comprendre la directive `v-for` de Vue pour générer des listes dynamiques. Nous allons également passer en revue quelques exemples de pourquoi l'attribut `key` doit être utilisé lorsque nous le faisons.

Puisque nous allons expliquer les choses en détail alors que nous commençons à écrire du code, cet article suppose que vous aurez peu ou pas de connaissances avec Vue (et/ou d'autres frameworks JavaScript).

### Étude de cas : Twitter

Nous allons utiliser [Twitter](https://twitter.com/) comme étude de cas pour cet article.

Lorsque nous sommes connectés et sur la route d'index principale de Twitter, nous sommes présentés avec une vue similaire à celle-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*yAgKZT2NuFjBWWbC.png)

Sur la page d'accueil, nous avons l'habitude de voir une liste de tendances, une liste de tweets, une liste de followers potentiels, et ainsi de suite. Le contenu affiché dans ces listes dépend d'une multitude de facteurs — notre historique Twitter, les personnes que nous suivons, nos likes, et ainsi de suite. Par conséquent, nous pouvons dire que toutes ces données sont **dynamiques**.

Bien que ces données soient obtenues dynamiquement, la **manière** dont ces données sont affichées reste la même. Cela est en partie dû à l'utilisation de **composants web réutilisables**.

Par exemple, nous pouvons voir la liste de tweets comme une liste de simples éléments `tweet-component`. Nous pouvons penser à `tweet-component` comme une coquille qui prend des données de sorts, telles que le nom d'utilisateur, le handle, le tweet et l'avatar, parmi d'autres morceaux, et affiche simplement ces morceaux dans un balisage cohérent.

![Image](https://cdn-media-1.freecodecamp.org/images/0*BdB3OeyWDWHuMNiN.png)

Disons que nous voulons rendre une liste de composants (comme une liste d'éléments `tweet-component`) basée sur une grande source de données obtenue à partir d'un serveur. Dans Vue, la première chose qui devrait venir à l'esprit pour accomplir cela est la directive `**v-for**`.

### La directive v-for

La directive `v-for` est utilisée pour rendre une liste d'éléments basée sur une source de données. La directive peut être utilisée sur un élément de modèle et nécessite une syntaxe spécifique du genre :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Z1iUt5OO46Ari1uK.png)

Voyons un exemple de cela en pratique. Tout d'abord, nous allons supposer que nous avons déjà obtenu une collection de données de tweets :

```js
const tweets = [
  {
    id: 1,
    name: 'James',
    handle: '@jokerjames',
    img: 'https://semantic-ui.com/images/avatar2/large/matthew.png',
    tweet: "Si vous ne réussissez pas, secouez-vous et réessayez.",
    likes: 10,
  },
  { 
    id: 2,
    name: 'Fatima',
    handle: '@fantasticfatima',
    img: 'https://semantic-ui.com/images/avatar2/large/molly.png',
    tweet: 'Mieux vaut tard que jamais, mais jamais en retard est mieux.',
    likes: 12,
  },
  {
    id: 3,
    name: 'Xin',
    handle: '@xeroxin',
    img: 'https://semantic-ui.com/images/avatar2/large/elyse.png',
    tweet: 'La beauté dans la lutte, la laideur dans le succès.',
    likes: 18,
  }
]
```

`tweets` est une collection d'objets `tweet`, chaque `tweet` contenant des détails de ce tweet particulier — un identifiant unique, le nom/handle du compte, le message du tweet, et ainsi de suite. Essayons maintenant d'utiliser la directive `v-for` pour rendre une liste de composants de tweets basée sur ces données.

Tout d'abord, nous allons créer l'instance Vue — le cœur de l'application Vue. Nous allons monter/attacher notre instance à un élément DOM avec l'id `app` et assigner la collection `tweets` comme partie de l'objet de données de l'instance.

```js
new Vue({
  el: '#app',
  data: {
    tweets
  }
});
```

Nous allons maintenant créer un `tweet-component` que notre directive `v-for` utilisera pour rendre une liste. Nous allons utiliser le constructeur global `Vue.component` pour créer un composant nommé `tweet-component` :

```js
Vue.component('tweet-component', {
  template: `  
    <div class="tweet">
      <div class="box">
        <article class="media">
          <div class="media-left">
            <figure class="image is-64x64">
              <img :src="tweet.img" alt="Image">
            </figure>
          </div>
          <div class="media-content">
            <div class="content">
              <p>
                <strong>{{tweet.name}}</strong> <small>{{tweet.handle}}</small>
                <br>
                {{tweet.tweet}}
              </p>
            </div>
              <div class="level-left">
                <a class="level-item">
                  <span class="icon is-small"><i class="fas fa-heart"></i></span>
                  <span class="likes">{{tweet.likes}}</span>
                </a>
              </div>
          </div>
        </article>
      </div>
    </div>  
  `,
  props: {
    tweet: Object
  }
});
```

Quelques points intéressants à noter ici :

1. Le `tweet-component` attend un prop d'objet `tweet` comme vu dans l'exigence de validation des props (`props: {tweet: Object}`). Si le composant est rendu avec un prop `tweet` qui n'est **pas un objet**, Vue émettra des avertissements.
2. Nous liaisons les propriétés de l'objet tweet prop au modèle de composant à l'aide de la syntaxe Mustache : `{{ }}`.
3. Le balisage du composant adopte l'élément [Box de Bulma](https://bulma.io/documentation/elements/box/) car il représente une bonne ressemblance à un tweet.

Dans le modèle HTML, nous devons créer le balisage où notre application Vue sera montée (c'est-à-dire l'élément avec l'id `app`). Dans ce balisage, nous utiliserons la directive `v-for` pour rendre une liste de tweets.

Puisque `tweets` est la collection de données que nous allons itérer, `tweet` sera un alias approprié à utiliser dans la directive. Dans chaque `tweet-component` rendu, nous **passerons également** l'objet `tweet` itéré en tant que props pour qu'il soit accessible dans le composant.

```js
<div id="app" class="columns">
  <div class="column">
    <tweet-component v-for="tweet in tweets" :tweet="tweet"/>
  </div>
</div>
```

Peu importe **combien** d'objets de tweets supplémentaires seraient introduits dans la collection, ou comment ils changeront avec le temps — notre configuration rendra toujours tous les tweets de la collection dans le balisage que nous attendons.

Avec l'aide de quelques CSS personnalisés, notre application ressemblera à quelque chose comme ceci :

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="Simple Twitter Feed #1" src="//codepen.io/itslit/embed/xWjZKy/?height=265&theme-id=0&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/itslit/pen/xWjZKy/'>Simple Twitter Feed #1</a> by Hassan Dj
  (<a href='https://codepen.io/itslit'>@itslit</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

Bien que tout fonctionne comme prévu, nous pouvons être invités avec un conseil Vue dans notre console de navigateur :

```
[Vue tip]: <tweet-component v-for="tweet in tweets">: component lists rendered with v-for should have explicit keys...
```

**Note :** Vous ne pourrez peut-être pas voir l'avertissement dans la console du navigateur lorsque vous exécutez le code via CodePen.

Pourquoi Vue nous dit-il de spécifier des clés explicites dans notre liste alors que tout fonctionne comme prévu ?

### L'attribut key

Il est courant de spécifier un attribut key pour chaque élément itéré dans une liste rendue `v-for`. Cela est dû au fait que Vue utilise l'attribut `key` pour créer des **liaisons uniques pour l'identité de chaque nœud**.

Expliquons cela un peu plus — si des changements dynamiques d'interface utilisateur se produisent dans notre liste (par exemple, l'ordre des éléments de la liste est mélangé), Vue optera pour changer les données dans chaque élément **au lieu** de déplacer les éléments DOM en conséquence. Cela ne posera pas de problème dans la plupart des cas. Cependant, dans certains cas où notre liste `v-for` dépend de l'état du DOM et/ou de l'état des composants enfants, cela peut provoquer un comportement non intentionnel.

Voyons un exemple de cela. Que se passe-t-il si notre simple composant de tweet contient maintenant un champ de saisie qui permettra à l'utilisateur de répondre directement au message du tweet ? Nous ignorerons comment cette réponse pourrait être soumise et nous adresserons simplement le nouveau champ de saisie lui-même :

![Image](https://cdn-media-1.freecodecamp.org/images/0*X3dVBOFq76PJQFGC.png)

Nous inclurons ce nouveau champ de saisie dans le modèle de `tweet-component` :

```js
Vue.component('tweet-component', {
  template: `
    <div class="tweet">
      <div class="box">
        // ...
      </div>
      <div class="control has-icons-left has-icons-right">
        <input class="input is-small" placeholder="Tweetez votre réponse..." />
        <span class="icon is-small is-left">
          <i class="fas fa-envelope"></i>
        </span>
      </div>
    </div>
  `,
  props: {
    tweet: Object
  }
});
```

Supposons que nous voulons introduire une autre nouvelle fonctionnalité dans notre application. Cette fonctionnalité permettrait à l'utilisateur de mélanger aléatoirement une liste de tweets.

Pour ce faire, nous pouvons d'abord inclure un bouton "Shuffle!" dans notre modèle HTML :

```html
<div id="app" class="columns">
  <div class="column">
    <button class="is-primary button" @click="shuffle">
      Shuffle!
    </button>
    <tweet-component v-for="tweet in tweets" :tweet="tweet"/>
  </div>
</div>
```

Nous avons attaché un écouteur d'événement de clic sur l'élément bouton pour appeler une méthode `shuffle` lorsqu'il est déclenché. Dans notre instance Vue, nous allons créer la méthode `shuffle` responsable du mélange aléatoire de la collection `tweets` dans l'instance. Nous allons utiliser la méthode [_shuffle](https://lodash.com/docs/4.17.5#shuffle) de lodash pour y parvenir :

```js
new Vue({
  el: '#app',
  data: {
    tweets
  },
  methods: {
    shuffle() {
      this.tweets = _.shuffle(this.tweets)
    }
  }
});
```

Essayons cela ! Si nous cliquons sur shuffle quelques fois, nous remarquerons que nos éléments de tweets sont triés aléatoirement à chaque clic.

<iframe height="500" width="500" style="width: 100%;" scrolling="no" title="Simple Twitter Feed #2" src="//codepen.io/itslit/embed/LdmGmP/?height=265&theme-id=0&default-tab=js,result" frameborder="no" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/itslit/pen/LdmGmP/'>Simple Twitter Feed #2</a> by Hassan Dj
  (<a href='https://codepen.io/itslit'>@itslit</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

Cependant, si nous tapons quelques informations dans la saisie de chaque composant et que nous cliquons ensuite sur shuffle, nous remarquerons quelque chose de particulier qui se produit :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1PN7mevBsMNhS03dt6-7qA.gif)

Puisque nous n'avons pas choisi d'utiliser l'attribut `**key**`, Vue n'a pas créé de liaisons uniques pour chaque nœud de tweet. Par conséquent, lorsque nous cherchons à réorganiser les tweets, Vue prend l'approche plus performante consistant à simplement **changer** **(ou corriger)** les données dans chaque élément. Puisque l'état temporaire du DOM (c'est-à-dire le texte saisi) reste en place, nous subissons cette inadéquation non intentionnelle.

Voici un diagramme qui nous montre les données qui sont corrigées sur chaque élément et l'état du DOM qui reste en place :

![Image](https://cdn-media-1.freecodecamp.org/images/1*IKwgNEwHYMwzRq8nOiBjog.png)

Pour éviter cela, nous devons assigner une **key** unique à chaque `tweet-component` rendu dans la liste.

Nous utiliserons l'`id` d'un `tweet` comme identifiant unique puisque nous pouvons dire en toute sécurité qu'un `id` de tweet ne devrait pas être égal à celui d'un autre. Parce que nous utilisons des valeurs dynamiques, nous utiliserons la directive `v-bind` pour lier notre key à `tweet.id` :

```html
<div id="app" class="columns">
  <div class="column">
    <button class="is-primary button" @click="shuffle">
      Shuffle!
    </button>
    <tweet-component
      v-for="tweet in tweets"
      :tweet="tweet"
      :key="tweet.id"
    />
  </div>
</div>
```

Maintenant, Vue reconnaît l'identité de chaque nœud de tweet, donc il **réorganisera** les composants lorsque nous avons l'intention de mélanger la liste.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GXx_K3xLDHF8PZRTILoW_Q.gif)

### Transitions

Puisque chaque composant de tweet est maintenant déplacé correctement, nous pouvons aller plus loin et utiliser `transition-group` de Vue pour **montrer** comment les éléments sont réorganisés.

Pour ce faire, nous allons ajouter l'élément [`transition-group`](https://vuejs.org/v2/guide/transitions.html#List-Transitions) comme enveloppe pour la liste `v-for`. Nous allons spécifier un nom de transition `tweets` et déclarer que le groupe de transition doit être rendu comme un élément `div`.

```html
<div id="app" class="columns">
  <div class="column">
    <button class="is-primary button" @click="shuffle">
      Shuffle!
    </button>
    <transition-group name="tweets" tag="div">
      <tweet-component
         v-for="tweet in tweets"
         :tweet="tweet"
         :key="tweet.id"
      />
    </transition-group>
  </div>
</div>
```

En fonction du nom de la transition, Vue reconnaîtra automatiquement si des transitions/animations CSS ont été spécifiées. Puisque nous visons à invoquer une transition pour le **mouvement** des éléments dans la liste, Vue recherchera une transition CSS spécifiée du genre `tweets-move` (où `tweets` est le nom donné à notre groupe de transition).

Par conséquent, nous allons introduire manuellement une classe `.tweets-move` qui a un type et une durée de transition spécifiés :

```css
#app .tweets-move {
  transition: transform 1s;
}
```

**Note :** Ceci est un aperçu très bref de l'application des transitions de liste. Assurez-vous de consulter la [documentation Vue](https://vuejs.org/v2/guide/transitions.html) pour des informations détaillées sur tous les différents types de transitions qui peuvent être appliqués !

Nos éléments `tweet-component` vont maintenant **transitionner** de manière appropriée entre les emplacements lorsqu'un shuffle est invoqué. Essayez-le ! Tapez quelques informations dans les champs de saisie et cliquez sur "Shuffle!" quelques fois.

Assez cool, n'est-ce pas ? Sans l'attribut `key`, **l'élément transition-group ne peut pas être utilisé pour créer des transitions de liste** puisque les éléments sont **corrigés en place** au lieu d'être réorganisés.

L'attribut `key` doit-il toujours être utilisé ? **C'est recommandé**. La [documentation Vue](https://vuejs.org/v2/guide/list.html#key) spécifie que l'attribut key ne doit être omis que si :

* Nous voulons intentionnellement la manière par défaut de corriger les éléments en place pour des raisons de performance.
* Le contenu du DOM est suffisamment simple.

### Conclusion

Et voilà ! Espérons que cet article court a montré à quel point la directive `v-for` est utile ainsi que fourni un peu plus de contexte sur pourquoi l'attribut `key` est souvent utilisé. Faites-moi savoir si vous avez des questions/réflexions quelconques !

Si vous avez aimé mon style d'écriture et que vous êtes potentiellement intéressé à apprendre à construire des applications réelles avec Vue, vous pourriez aimer le livre **Fullstack Vue: The Complete Guide to Vue.js** que j'ai aidé à publier ! Le livre couvre de nombreux aspects de Vue, y compris le routage, la gestion d'état simple, la gestion des formulaires, Vuex, la persistance du serveur et les tests, parmi d'autres sujets. Si vous êtes intéressé et/ou souhaitez essayer un chapitre d'exemple, vous pouvez obtenir plus d'informations sur notre site web [**https://fullstack.io/vue**](https://www.fullstack.io/vue/)**!**

Si vous avez des questions/réflexions/opinions, vous êtes plus que bienvenu pour me contacter à tout moment [@djirdehh](https://twitter.com/djirdehh) !