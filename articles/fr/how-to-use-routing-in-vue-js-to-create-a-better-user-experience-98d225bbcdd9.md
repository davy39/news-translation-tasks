---
title: Comment utiliser le routage dans Vue.js pour créer une meilleure expérience
  utilisateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-28T00:03:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-routing-in-vue-js-to-create-a-better-user-experience-98d225bbcdd9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ckpJ83fx62uqbRGUcaRrkw.jpeg
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
seo_title: Comment utiliser le routage dans Vue.js pour créer une meilleure expérience
  utilisateur
seo_desc: 'By Said Hayani

  Vue.js is a great JavaScript Framework created by Evan You. It’s used to build single
  web page apps and flexible components, and it’s one of the most required skills
  in Front End Web development. You can learn more about Vue.js here.


  ...'
---

Par Said Hayani

Vue.js est un excellent Framework JavaScript créé par [Evan You](https://twitter.com/youyuxi). Il est utilisé pour construire des applications web monopage et des composants flexibles, et c'est l'une des compétences les plus demandées en développement Front End Web. Vous pouvez en apprendre plus sur Vue.js [ici](https://vuejs.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/QnEEdc6mWqtQDaulHYzeZFEHkWoLl0LgAkw4)

[Vue.js](https://vuejs.org/) fournit un ensemble de fonctionnalités qui vous permettent de construire des composants web réutilisables. Le routage est l'une de ces méthodes. Il permet à l'utilisateur de basculer entre les pages sans recharger la page. C'est ce qui rend la navigation facile et vraiment agréable dans vos applications web.

Donc, dans cet article, j'expliquerai comment fonctionnent les routeurs Vue.js en construisant un modèle Vue comme exemple.

### Installation

Commençons donc avec notre projet de Route**r** Vue.js en installant et en créant un nouveau projet [Vue.js](https://www.zeolearn.com/magazine/why-must-you-choose-vuejs-over-reactjs). Nous devons avoir Node.js installé. Nous allons utiliser [vue-cli](https://github.com/vuejs/vue-cli) pour générer un nouveau projet Vue.js. Suivez les étapes données ci-dessous :

Tapez le code suivant dans votre terminal et exécutez :

```
vue init webpack vue-router

//
cd vue-router
//
npm run dev
```

Accédez à [http://localhost:8080](http://localhost:8080)

![Image](https://cdn-media-1.freecodecamp.org/images/HckFEYSBlXmo-qMuT9SeU8zFWxRBm0RKDSlE)

Ouvrez l'application dans votre éditeur de texte. À l'intérieur du dossier des composants, ouvrez le fichier `HellowWorld.vue` et suivez ces étapes :

* Renommez `HellowWorld.vue` en `home.vue`. Supprimez tout le code et remplacez-le par ceci :

```vue
<template>
  <div class="home">
    <h1>Accueil</h1>
  </div>
</template>

<script>
export default {
  name: 'home',
  data () {
    return {
      msg: 'Bienvenue dans votre application Vue.js'
    }
  }
}
</script>

<!-- Ajoutez l'attribut "scoped" pour limiter le CSS à ce composant uniquement -->
<style scoped>

</style>
```

* Allez dans `index.js` à l'intérieur du dossier **router** et remplacez `HelloWorld` par `home` :

```vue
import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    }
  ]
})
```

Le fichier `App.vue` devrait ressembler à ceci :

```vue
<template>
  <div id="app">
    
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  
}
</style>
```

Et maintenant, écrivons notre code !

Nous allons maintenant ajouter un modèle [Bootswatch](https://bootswatch.com/). Vous pouvez choisir n'importe quel modèle que vous aimez. Je vais choisir [Cosmo](https://bootswatch.com/cosmo/). Cliquez sur Ctrl + U pour voir le code source et copiez simplement la `Navbar` (nous avons juste besoin de la navbar). Collez ce code dans le composant App.vue.

Nous y sommes ?

![Image](https://cdn-media-1.freecodecamp.org/images/43YDKXgEQvgIlHa3ff3wLUttTYDiP4JBsMOS)

Ensuite, nous allons créer trois autres composants : `Blog`, `Services` et `Contact`.

À l'intérieur du dossier des composants, créez un nouveau fichier, nommez-le `blog.vue`, et insérez ce code :

```vue
<template>
 <div class="blog">
  <h1>{{blog}}</h1>
 </div>
</template>
<script>
 export default{
  name:'blog',
  data (){
   return{
    title:'Blog'
   }
  }
 }
</script>

<style scoped>
 
</style>
```

Si vous voulez faire la même chose pour le composant service et contact, vous devez avoir ces fichiers dans votre dossier de composants :

* home.vue
* blog.vue
* services.vue
* contact.vue

### Configuration des routeurs

Maintenant, après avoir créé ces quatre composants, nous devons configurer les routeurs afin de pouvoir naviguer entre les composants.

Alors, comment pouvons-nous naviguer vers chaque composant en utilisant les routeurs ?

Nous devons apprendre les règles de routage. Maintenant, nous devons faire quelques modifications à l'intérieur du dossier du routeur, alors ouvrez `index.js`

![Image](https://cdn-media-1.freecodecamp.org/images/xwekScgLyanvWr3SCo9hgnZ4HUFqWpuELK0v)

Suivez ces étapes :

* Tout d'abord, importez vos composants dans index.js. Importez tous les composants en utilisant la méthode `import`.

```js
import home from '@/components/home'
import blog from '@/components/blog'
import services from '@/components/services'
import contact from '@/components/contact'
```

* Ensuite, importez Vue et le module router depuis le module [vue-router](https://router.vuejs.org) :

```vue
import Vue from 'vue'
import Router from 'vue-router'

// utilisez le router
Vue.use(Router)
```

Si vous avez installé Vue avec vue-cli, vous aurez le module [vue-router](https://router.vuejs.org/) importé par défaut.

* Enfin, à l'intérieur du dossier du routeur, nous devons configurer les routeurs pour les faire fonctionner. La méthode du routeur prend un tableau d'objets qui, à leur tour, prennent les propriétés de chaque composant :

```vue
export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/blog',
      name: 'blog',
      component: blog
    },
    {
      path: '/services',
      name: 'services',
      component: services
    },
    {
      path: '/contact',
      name: 'contact',
      component: contact
    }
  ]
})
```

* `path` : le chemin du composant
* `name` : le nom du composant
* `component` : la vue du composant

Pour faire de n'importe quel composant le composant par défaut, définissez une barre oblique ('/') pour la propriété path :

```vue
path:'/'
```

Dans notre exemple, nous avons défini la page d'accueil comme page par défaut. Maintenant, lorsque vous ouvrez le projet dans le navigateur, la première page qui apparaîtra est la page d'accueil.

```vue
{
  path:'/',
  name:'home',
  component:home
}
```

Le vue-router a des paramètres et des méthodes plus avancés, mais nous ne nous plongeons pas dans cette section pour le moment.

Voici la liste des propriétés et des méthodes que vous pouvez utiliser avec vue-router :

* [Routeurs imbriqués](https://router.vuejs.org/en/essentials/nested-routes.html)
* [Vue nommée](https://router.vuejs.org/en/essentials/named-views.html)
* [Redirection et Alias](https://router.vuejs.org/en/essentials/redirect-and-alias.html)
* [Garde de navigation](https://router.vuejs.org/en/advanced/navigation-guards.html)
* [Instance du routeur](https://router.vuejs.org/en/api/router-instance.html)

Maintenant, vous pouvez naviguer vers n'importe quel composant en tapant le nom du composant !

![Image](https://cdn-media-1.freecodecamp.org/images/iSIQ-ngDnOuHEJkA-CfWIzS-NCTtnPHb9qaQ)

### router-link

Maintenant, nous allons configurer la navigation à travers la Navbar que nous avons créée en utilisant l'élément router-link.

Pour ce faire, nous devons remplacer l'élément `<`/a> par `<router-link>&l`t;/router/link> comme ceci :

```vue
<li class="nav-item">
  <router-link class="nav-link" to="/blog">Blog</router-link>
</li>
<li class="nav-item">
  <router-link class="nav-link" to="/services">Services</router-link>
 </li>
<li class="nav-item">
   <router-link class="nav-link" to="/contact">contact</router-link>
 </li>
```

Le router-link prend l'attribut `to='path'` qui prend le chemin du composant comme valeur.

### Router-view

Vous trouverez la balise `<router-vi`ew> dans le fichier A`pp.vue. C'est essentiellement la vue où les composants sont rendus. C'est comme la div principale qui contient tous les composants, et elle retourne le composant qui correspond à la route actuelle. Nous discuterons de rout`e-view dans la prochaine partie lorsque nous utiliserons la transition d'animation.

### Utilisation des paramètres à l'intérieur des routeurs

À ce stade, nous allons utiliser des paramètres pour naviguer vers des composants spécifiques. Les paramètres rendent le routage dynamique.

Pour travailler avec des paramètres, nous allons créer une liste de produits et un tableau de données. Lorsque vous cliquez sur le lien d'un produit, il nous emmènera à la page des détails via un paramètre.

Dans cette situation, nous n'allons pas utiliser de base de données ou d'API pour récupérer les données des produits. Donc, ce que nous devons faire, c'est créer un tableau de produits qui agira comme une base de données.

À l'intérieur du composant `home.vue`, placez le tableau dans la méthode data() comme ceci :

```vue
export default {
  name: 'home',
  data () {
    return {
      title: 'Accueil',
      products:[
      {
        productTitle:"ABCN",
        image       : require('../assets/images/product1.png'),
        productId:1
      },
      {
        productTitle:"KARMA",
        image       : require('../assets/images/product2.png'),
        productId:2
      },
      {
        productTitle:"Tino",
        image       : require('../assets/images/product3.png'),
        productId:3
      },
      {
        productTitle:"EFG",
        image       : require('../assets/images/product4.png'),
        productId:4
      },
      {
        productTitle:"MLI",
        image       : require('../assets/images/product5.png'),
        productId:5
      },
      {
        productTitle:"Banans",
        image       : require('../assets/images/product6.png'),
        productId:6
      }
      ]
    }
  }
}
```

Ensuite, récupérez et bouclez dans le tableau des produits en utilisant la directive `v-for`.

```vue
<div class="row">
      <div class="col-md-4 col-lg4" v-for="(data,index) in products" :key="index">
        <img :src="data.image" class="img-fluid">
         <h3>{{data.productTitle}}</h3>
      </div>
    </div>
```

Le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/EHmmP-MWsUXJflne-niLX1WfrxIwn4HzQIH9)

Pour naviguer vers le composant des détails, nous devons d'abord ajouter un événement de clic :

```vue
<h3 @click="goTodetail()" >{{data.productTitle}}</h3>
```

Ensuite, ajoutez des méthodes :

```vue
methods:{
  goTodetail() {
    this.$router.push({name:'details'})
  }
```

Si vous cliquez sur le titre, il retournera undefined car nous n'avons pas encore créé le composant des détails. Alors créons-en un :

**details.vue**

```vue
<template>
 <div class="details">
  <div class="container">
   <h1 class="text-primary text-center">{{title}}</h1>
  </div>
 </div>
</template>
<script>
 export default{
  name:'details',
  data(){
   return{
    title:"details"
   }
  }
 }
</script>
```

Maintenant, nous pouvons naviguer sans obtenir d'erreur ?

![Image](https://cdn-media-1.freecodecamp.org/images/x1GAOi94gMVYSRG4SjupVR4p4hwGOSoctmcf)

Maintenant, comment pouvons-nous naviguer vers la page des détails et obtenir les données correspondantes si nous n'avons pas de base de données ?

Nous allons utiliser le même tableau de produits dans le composant des détails. Ainsi, nous pouvons faire correspondre l'id qui provient de l'URL :

```vue
products:[
      {
        productTitle:"ABCN",
        image       : require('../assets/images/product1.png'),
        productId:1
      },
      {
        productTitle:"KARMA",
        image       : require('../assets/images/product2.png'),
        productId:2
      },
      {
        productTitle:"Tino",
        image       : require('../assets/images/product3.png'),
        productId:3
      },
      {
        productTitle:"EFG",
        image       : require('../assets/images/product4.png'),
        productId:4
      },
      {
        productTitle:"MLI",
        image       : require('../assets/images/product5.png'),
        productId:5
      },
      {
        productTitle:"Banans",
        image       : require('../assets/images/product6.png'),
        productId:6
      }
      ]
```

Tout d'abord, nous devons définir l'id pour la méthode goTodetail() comme paramètre :

```
<h3 @click="goTodetail(data.productId)" >{{data.productTitle}}</h3>
```

Ensuite, ajoutez un deuxième paramètre à la méthode du routeur.

La méthode `$router` prend deux paramètres : d'abord, le `name` du composant vers lequel nous voulons naviguer, et ensuite, le paramètre `id` (ou tout autre paramètre).

```vue
this.$router.push({name:'details',params:{Pid:proId}})
```

Ajoutez Pid comme paramètre dans **index.js** à l'intérieur du dossier `router` :

```vue
{
      path: '/details/:Pid',
      name: 'details',
      component: details
    }
```

**home.vue**

```vue
methods:{
  goTodetail(prodId) {
    this.$router.push({name:'details',params:{Pid:proId}})
  }
  }
```

![Image](https://cdn-media-1.freecodecamp.org/images/n6womVRZITagD7pZOGmNvF9pQfB5NJMnGcxi)

Pour obtenir le paramètre correspondant, utilisez cette ligne de code :

```
this.$route.params.Pid
```

**details.vue**

```vue
<h2>l'id du produit est :{{this.$route.params.Pid}}</h2>
```

Ensuite, bouclez à travers le tableau des produits dans `detalils.vue` et vérifiez l'objet qui correspond au paramètre Pid et retournez ses données :

```vue
<div class="col-md-12" v-for="(product,index) in products" :key="index">
     <div v-if="proId == product.productId">
      <h1>{{product.productTitle}}</h1>
      <img :src="product.image" class="img-fluid">
     </div>
    </div>
    
///
export default{
  name:'details',
  data(){
   return{
    proId:this.$route.params.Pid,
    title:"details"
     }
}
```

Vous voyez maintenant que lorsque nous cliquons sur le lien d'un produit, il nous amène à ce produit !

![Image](https://cdn-media-1.freecodecamp.org/images/7VVd405SDvDWC3scUXaVyggyn1IsY6QNoQNd)

**detail.vue** composant :

```vue
<template>
 <div class="details">
  <div class="container">
   <div class="row">
    <div class="col-md-12" v-for="(product,index) in products" :key="index">
     <div v-if="proId == product.productId">
      <h1>{{product.productTitle}}</h1>
      <img :src="product.image" class="img-fluid">
     </div>
    </div>
   </div>
  </div>
 </div>
</template>
<script>
 export default{
  name:'details',
  data(){
   return{
    proId:this.$route.params.Pid,
    title:"details",
    products:[
    {
    productTitle:"ABCN",
    image       : require('../assets/images/product1.png'),
    productId:1
    },
    {
    productTitle:"KARMA",
    image       : require('../assets/images/product2.png'),
    productId:2
    },
    {
    productTitle:"Tino",
    image       : require('../assets/images/product3.png'),
    productId:3
    },
    {
    productTitle:"EFG",
    image       : require('../assets/images/product4.png'),
    productId:4
    },
    {
    productTitle:"MLI",
    image       : require('../assets/images/product5.png'),
    productId:5
    },
    {
    productTitle:"Banans",
    image       : require('../assets/images/product6.png'),
    productId:6
    }
    ]
     
   }
  }
 }
</script>
```

### La transition

![Image](https://cdn-media-1.freecodecamp.org/images/LF9rGJaP6F6pQriWw4xFa7DjFMvbTSYttLAw)

Dans cette partie, nous allons ajouter une transition d'animation au composant animé. Nous allons animer la transition des composants. Cela rend la navigation géniale, et cela crée une meilleure UX et UI.

Pour faire une transition d'animation, placez le "<router-view>" à l'intérieur de la balise "<transition/>".

**App.vue**

```vue
<transition name="moveInUp">
         <router-view/>
  </transition>
```

Pour animer la transition du composant lorsqu'il entre dans la vue, ajoutez `enter-active` au nom donné à la balise de transition. Ensuite, ajoutez `leave-active` et donnez-lui les propriétés de transition CSS comme ceci :

```vue
.moveInUp-enter-active{
  opacity: 0;
  transition: opacity 1s ease-in;
}
```

#### **Utilisation de l'animation CSS3**

Maintenant, nous allons animer en utilisant @keyframes en CSS3.

Lorsque le composant entre dans la vue, ajoutez un effet de fondu à la vue.

```vue
.moveInUp-enter-active{
  animation: fadeIn 1s ease-in;
}
@keyframes fadeIn{
  0%{
    opacity: 0;
  }
  50%{
    opacity: 0.5;
  }
  100%{
    opacity: 1;
  }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/FJf7dZujiqIrVYkccKmP3uSyIS4gk3n62Gxh)

Ajoutez un autre effet de fondu lorsque le composant quitte la vue.

Maintenant, nous allons faire en sorte que le composant se déplace vers l'intérieur et vers le haut lorsqu'il quitte la vue.

```vue
.moveInUp-leave-active{
  animation: moveInUp .3s ease-in;
}
@keyframes moveInUp{
 0%{
  transform: translateY(0);
 }
  100%{
  transform: translateY(-400px);
 }
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/oUTnR9ZLYHxbapDH7MjMLZn244aTtehGXrIQ)

Maintenant, vous pouvez créer vos propres animations et transitions pour vos composants.

C'est tout — nous avons terminé ! ?

Vous pouvez télécharger le code source [**ici**](https://github.com/hayanisaid/Vue-router) **.**

### Conclusion

Le routage dans Vue.js rend votre application vraiment géniale en matière de navigation. Il lui donne cette énergie de l'application web monopage, et il crée une meilleure expérience utilisateur.

Au fait...

Si vous voulez apprendre Bootstrap 4, consultez mon cours sur Skillshare avec ce [**lien de parrainage**](https://skl.sh/2ssg1nj) et obtenez 2 mois d'accès gratuit à 20 000 cours.

[_Publié à l'origine sur zeolearn.com_](https://www.zeolearn.com/magazine/understand-routing-in-vuejs-with-examples)

> Abonnez-vous à cette [mailList](http://eepurl.com/dk9OJL) pour en savoir plus sur les sujets Front End, et suivez-moi sur [Twitter](https://twitter.com/hayanisaid1995).