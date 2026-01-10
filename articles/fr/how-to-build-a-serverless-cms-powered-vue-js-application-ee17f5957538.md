---
title: Comment créer une application Vue.js alimentée par un CMS sans serveur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-31T08:08:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-serverless-cms-powered-vue-js-application-ee17f5957538
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hK_Y0DWvpFcT01FFtUp7fQ.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer une application Vue.js alimentée par un CMS sans serveur
seo_desc: 'By Jake Lumetta

  Vue.js is getting a lot of love and exploding in popularity for good reason. As
  a progressively adoptable framework, it’s lightweight, reactive, and component-based,
  allowing you to create pluggable components you can add to any proje...'
---

Par Jake Lumetta

Vue.js reçoit beaucoup d'amour et explose en popularité pour de bonnes raisons. En tant que framework adoptable progressivement, il est léger, réactif et basé sur les composants, vous permettant de créer des composants pluggables que vous pouvez ajouter à n'importe quel projet.

Le framework progressif de Vue.js est bien adapté aux architectures d'applications sans serveur. Les développeurs se tournent de plus en plus vers les architectures sans serveur, car le sans serveur leur permet de créer et d'ajuster des produits plus rapidement sans avoir à supporter les fardeaux (maintenance du serveur, pannes et goulots d'étranglement de mise à l'échelle) de l'architecture traditionnelle basée sur un serveur.

Vue.js et son adoptabilité incrémentielle emblématique vous permettent d'essayer Vue sans mettre votre base de code existante en danger.

Dans cet article, vous apprendrez à créer une application [Vue.js](https://vuejs.org/v2/guide/) sans serveur en utilisant ButterCMS. ButterCMS est une [plateforme de CMS et de blogging sans tête](https://buttercms.com/api-first-cms/) qui vous permet de créer des applications alimentées par un CMS en utilisant n'importe quel langage de programmation. Ce tutoriel vous montrera comment ajouter des API de contenu performantes à votre application Vue.js. Ces API sont faciles à naviguer même pour les membres non techniques de votre équipe, vous permettant de profiter d'une gestion de contenu agile sans avoir à lancer et maintenir votre propre infrastructure de CMS.

Plus précisément, nous couvrirons trois cas d'utilisation : les pages marketing, le blogging et les bases de connaissances avec des exemples de code. Le code final pour ce tutoriel est disponible sur [GitHub](https://github.com/ButterCMS/buttercms-vue-tutorial).

### Installation

Tout d'abord, installez le SDK JS de ButterCMS. Nous l'utiliserons pour interroger l'API de contenu.

`npm install buttercms --save`

Une fois installé, vous pouvez suivre les tutoriels ci-dessous pour créer trois types de contenu : les pages marketing, le blogging et les bases de connaissances (par exemple, une FAQ).

### Ajouter des pages marketing

Supposons que vous souhaitiez permettre à une personne non technique de votre équipe d'ajouter des pages d'études de cas clients à votre site marketing. Pour ce faire, nous allons créer une page d'étude de cas comme exemple. En utilisant le tableau de bord de ButterCMS, vous pouvez créer un "type de page" intitulé "Étude de cas client" et définir les champs.

![Image](https://cdn-media-1.freecodecamp.org/images/GMhXSxeSjG0xWjQCklBRTlk0L95gvRhmoACg)

Une fois cela fait, vous pouvez créer votre première page. Spécifiez le nom et l'URL de la page en utilisant le tableau de bord de Butter et remplissez le contenu de la page. Une fois tout cela fait, l'API de ButterCMS retournera votre page définie au format JSON. Cela devrait ressembler à ceci :

```
{ "data": {   "slug": "acme-co",   "fields": {     "facebook_open_graph_title": "Acme Co loves ButterCMS",     "seo_title": "Acme Co Customer Case Study",     "headline": "Acme Co saved 200% on Anvil costs with ButterCMS",     "testimonial": "<p>We’ve been able to make anvils faster than ever before! — <em>Chief Anvil Maker</em></p>\r\n<p><img src=\"https://cdn.buttercms.com/NiA3IIP3Ssurz5eNJ15a\" alt=\"\" caption=\"false\" width=\"249\" height=\"249\" /></p>",     "customer_logo": "https://cdn.buttercms.com/c8oSTGcwQDC5I58km5WV",    }  }}
```

Ensuite, ouvrez votre éditeur de code et créez un fichier appelé `buttercms.js` dans votre répertoire `/src`.

Si vous n'avez pas de projet existant, créez-en un en entrant ce qui suit :

```
vue init webpack buttercms-project
cd buttercms-project
npm install
npm i -S buttercms
npm run dev
```

Ensuite, dans `src/buttercms.js` :

```
import Butter from 'buttercms';
```

```
const butter = Butter('your_api_token');
```

Maintenant, mettez à jour les routes dans votre application. Accédez à `router/index.js` et

```
import Vue from 'vue'
import Router from 'vue-router'
import CustomersHome from '@/components/CustomersHome'
import CustomerPage from '@/components/CustomerPage'
```

```
Vue.use(Router)
```

```
export default new Router({  mode: 'history',  routes: [      {        path: '/customers/',        name: 'customers-home',        component: CustomersHome      },      {        path: '/customers/:slug',        name: 'customer-page',        component: CustomerPage      }    ]  })
```

Maintenant, pour configurer une page "customers" afin de lister tous vos clients, nous allons définir une méthode `getpages()` pour obtenir toutes les pages clients. Dans le fichier `components/CustomersHome.vue`, nous ajoutons ce qui suit :

```
<script>  // import ButterCMS from  import { butter } from '@/buttercms'  export default {    name: 'customers-home',    data() {      return {      page_title: 'Customers',      // Create array to hold the pages from ButterCMS API      pages: []    }  },  methods: {    // Get List of Customer Pages    getPages() {      butter.page.list('customer_case_study')        .then((res) => {          // console.log(res.data.data)          // Check the results in the console         this.pages = res.data.data      })    }  },created() {  // Fire on page creation  this.getPages()    }  }</script>
```

Afficher les résultats :

```
<template>  <div id="customers-home">    <h1>{{ page_title }}</h1>    <div v-for="(page,index) in pages" :key="page.slug + '_' + index">      <router-link :to="'/customers/' + page.slug">        <div>          <img :src="page.fields.customer_logo" alt="">          <h2>{{ page.fields.headline }}</h2>        </div>      </router-link>    </div>  </div></template>
```

![Image](https://cdn-media-1.freecodecamp.org/images/9AgAa7mEf-ClV924vr6009jjc3A1aVA1o5ao)
_Exemple de quelque chose de proche de ce que vous avez jusqu'à présent après avoir publié une étude de cas_

Maintenant, nous allons configurer la page client pour afficher un seul client. Pour ce faire, dans `components/CustomerPage.vue`, nous définissons une méthode `getPage()` pour obtenir une page client particulière en fonction de son slug :

```
<script>  import { butter } from '@/buttercms'  export default {    name: 'customer-page',    data() {      return {      slug: this.$route.params.slug,      page: {        slug: '',        fields: {}      }    }  },  methods: {    getPage() {      butter.page.retrieve('customer_case_study', this.slug)        .then((res) => {        console.log(res.data.data)        this.page = res.data.data      }).catch((res) => {        console.log(res)      })    }  },  created() {    this.getPage()    }  }</script>
```

Lorsque vous affichez le résultat, vous devriez obtenir :

```
<template>  <div id="customer-page">    <figure>      <img :src="page.fields.customer_logo">    </figure>    <h1>{{ page.fields.headline }}</h1>    <h3>Testimonials</h3>    <div v-html="page.fields.testimonial"></div>    <div v-html="page.fields.body"></div>  </div></template>
```

![Image](https://cdn-media-1.freecodecamp.org/images/vf7fKxt3xSesNmIpsyRH9rxo1a3iUF8ypkel)
_Vous venez de créer quelque chose comme ceci_

Succès ! Maintenant, vous pouvez naviguer vers la page client que vous avez créée dans votre tableau de bord Butter via la liste de toutes les pages clients ou directement via l'URL.

### Ajouter une base de connaissances

Le tutoriel ci-dessous vous guidera à travers la création d'une base de connaissances pour votre application Vue.js. Nous utiliserons les "Content Fields" de ButterCMS pour cela. Les champs de contenu sont simplement des morceaux de contenu globaux qui peuvent être gérés par votre équipe. Ce contenu peut s'étendre sur plusieurs pages et chaque champ de contenu a un identifiant unique qui peut être interrogé, comme vous le verrez ci-dessous.

### Configurer les champs de contenu

Tout d'abord, vous devrez configurer certains champs de contenu personnalisés. En utilisant le tableau de bord, vous pouvez configurer un espace de travail pour organiser les champs de contenu. Les espaces de travail permettront aux éditeurs de contenu de curater le contenu sans affecter le développement ou l'API.

![Image](https://cdn-media-1.freecodecamp.org/images/cmUx8ENPpMDOGxy0PkwpDn-Ro4DPMCqLLoff)

Une fois dans un espace de travail, cliquez sur le bouton pour créer un nouveau champ de contenu. Choisissez le type "Object" et nommez le champ "FAQ Headline". Il aura un slug API de "faq_headline".

![Image](https://cdn-media-1.freecodecamp.org/images/8rJmYAZ9riqhFy0A3BJCbEdi6s6L6UOuMpAd)

Après avoir enregistré, ajoutez un autre champ — mais cette fois choisissez le type "Collection" et nommez le champ FAQ Items. Il aura un slug API de "faq_items". À l'écran suivant, configurez deux propriétés pour les éléments de la collection. Maintenant, retournez à votre espace de travail et mettez à jour votre titre et ajoutez quelques éléments FAQ.

### Intégration de votre application

Maintenant que vous avez créé du contenu dynamique, il est temps d'afficher le contenu dynamique dans votre application. Pour ce faire, vous allez récupérer les champs avec un appel API et les référencer dans votre vue. Tout d'abord, configurez une route vers votre page FAQ :

Nous allons ajouter les routes FAQ dans `router/index.js` :

```
import Vue from 'vue'
import Router from 'vue-router'
```

```
import FAQ from '@/components/FAQ'
```

```
Vue.use(Router)
```

```
export default new Router({  mode: 'history',  routes: [    {      path: '/faq',      name: 'faq',      component: FAQ    }  ]})
```

Ensuite, créez `components/FAQ.vue` avec un appel pour obtenir les FAQ depuis l'API :

```
<script>  import { butter } from '@/buttercms'  export default {    name: 'faq',    data() {      return {        page_title: 'FAQ',        faq_items: []    }  },  methods: {    getFaqs() {      butter.content.retrieve(['faq_headline', 'faq_items'])        .then((res) => {        console.log(res.data.data)        this.page_title = res.data.data.faq_headline        this.faq_items = res.data.data.faq_items      })    }  },  created() {    this.getFaqs()    }  }</script>
```

Remarquez que nous avons prédéfini `page_title` comme "FAQ" puis l'avons mis à jour avec l'appel API à "Foire aux questions".

```
<template>  <div id="faq">    <h1>{{ page_title }}</h1>    <div v-for="(faq, index) in faq_items" :key="index">      <p>{{ faq.question }}</p>      <p>{{ faq.answer }}</p>    </div>  </div></template>
```

Votre résultat affiché devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/v6UCEaryIPeuqMhdM3QZr0zV9TY2j8udSuz1)

Maintenant, votre équipe peut mettre à jour les valeurs depuis le tableau de bord Butter, et le contenu correspondant dans votre application sera automatiquement mis à jour.

### Moteur de blog

Enfin, nous allons aborder l'ajout d'un moteur de blog. Vous pouvez rapidement créer un blog alimenté par un CMS en utilisant Vue.js.

#### Affichage des articles

Nous allons commencer par créer une route de blog en utilisant `vue-router`. Pour afficher les articles, nous créons une route simple `/blog` dans notre application et récupérons les articles de blog, ainsi qu'une route `/blog/:slug` pour gérer les articles individuels.

Dans `router/index.js` :

```
import Vue from 'vue'
import Router from 'vue-router'
import BlogHome from '@/components/BlogHome'
import BlogPost from '@/components/BlogPost'
```

```
Vue.use(Router)
```

```
export default new Router({  mode: 'history',  routes: [    {      path: '/blog/',      name: 'blog-home',      component: BlogHome    },    {      path: '/blog/:slug',      name: 'blog-post',      component: BlogPost    }  ]})
```

Pour créer votre page d'accueil de blog qui affichera vos articles les plus récents, vous allez créer `components/BlogHome.vue` :

```
<script>  import { butter } from '@/buttercms'  export default {    name: 'blog-home',    data() {      return {        page_title: 'Blog',        posts: []      }    },    methods: {      getPosts() {        butter.post.list({          page: 1,          page_size: 10        }).then((res) => {          // console.log(res.data)          this.posts = res.data.data        })      }    },    created() {      this.getPosts()    }  }</script>
```

Vous devez afficher le contenu en définissant le template et en appelant les champs dans le même fichier de composant :

```
<template>  <div id="blog-home">    <h1>{{ page_title }}</h1>
```

```
// Create v-for and apply a key for Vue. Example is using a combination of the slug and index
```

```
    <div v-for="(post,index) in posts" :key="post.slug + '_' + index">      <router-link :to="'/blog/' + post.slug">        <article class="media">          <figure>
```

```
// Bind results using a ':' 
```

```
// Use a v-if/else if their is a featured_image 
```

```
          <img v-if="post.featured_image" :src="post.featured_image" alt="">          <img v-else src="http://via.placeholder.com/250x250" alt="">          </figure>          <h2>{{ post.title }}</h2>          <p>{{ post.summary }}</p>        </article>      </router-link>    </div>  </div></template>
```

![Image](https://cdn-media-1.freecodecamp.org/images/yjoDoCoG3CgEy8xYE-c1eUbLApYPPqF1wjAP)
_Votre page d'accueil de blog ressemblera à ceci, en supposant que vos champs correspondent à l'exemple_

Ensuite, créez `components/BlogPost.vue` qui sera votre page d'article de blog pour lister un seul article.

```
<script>  import { butter } from '@/buttercms'  export default {    name: 'blog-post',    data() {      return {        post: {}      }    },    methods: {      getPost() {        butter.post.retrieve(this.$route.params.slug)          .then((res) => {            // console.log(res.data)            this.post = res.data          }).catch((res) => {            console.log(res)          })      }    },    created() {      this.getPost()    }  }</script>
```

Vous devez maintenant définir le template et faire un appel aux champs de contenu de l'article de blog :

```
<template>  <div id="blog-post">    <h1>{{ post.data.title }}</h1>    <h4>{{ post.data.author.first_name }} {{ post.data.author.last_name }}</h4>    <div v-html="post.data.body"></div>
```

```
    <router-link v-if="post.meta.previous_post" :to="'/blog/' + post.meta.previous_post.slug" class="button">      {{ post.meta.previous_post.title }}    </router-link>    <router-link v-if="post.meta.next_post" :to="'/blog/' + post.meta.next_post.slug" class="button">      {{ post.meta.next_post.title }}    </router-link>  </div></template>
```

![Image](https://cdn-media-1.freecodecamp.org/images/n0YDcljSBaMJKwbXMTpNdIBLGB03BXEvpsSv)
_Votre résultat devrait ressembler à ceci_

À ce stade, votre application récupère tous les articles de blog, vous permettant de naviguer vers des articles individuels. Mais vous remarquerez que les boutons suivant/précédent ne fonctionnent pas. Pourquoi ? Lorsque vous utilisez des routes avec `params`, lorsque l'utilisateur navigue de `/blog/foo` à `/blog/bar`, la même instance de composant sera réutilisée.

Puisque les deux routes rendent le même composant, cela est plus efficace que de détruire l'ancienne instance et d'en créer une nouvelle. Mais cela signifie également que les hooks de cycle de vie du composant ne seront pas appelés.

Il existe une solution pour cela. Nous devons surveiller l'objet `$route` et appeler `getPost()` lorsque la route change. Pour ce faire, vous devez mettre à jour la section script dans `components/BlogPost.vue` :

```
<script>  import { butter } from '@/buttercms'  export default {    name: 'blog-post',    data() {      return {        post: {}      }    },    methods: {      getPost() {        butter.post.retrieve(this.$route.params.slug)          .then((res) => {            // console.log(res.data)            this.post = res.data          }).catch((res) => {            console.log(res)          })    }  },  watch: {    $route(to, from) {      this.getPost()    }  },  created() {    this.getPost()  }}</script>
```

À ce stade, votre application dispose d'un blog fonctionnel qui peut être mis à jour facilement depuis le tableau de bord du CMS.

Vous pouvez également utiliser des API pour filtrer et mettre en avant du contenu sur votre blog avec des catégories, des tags et des auteurs. En fait, il y a beaucoup de choses que vous pouvez faire avec une API en termes de gestion de différents aspects de votre blog, y compris le balisage RSS, Atom et Sitemap, et le style de contenu via CSS.

### Conclusion

Félicitations ! Vous avez créé une application Vue.js sans serveur avec des API de contenu performantes. Votre équipe de développement peut se concentrer sur le codage, et les membres non techniques de votre équipe disposent désormais d'un moyen facile de gérer le contenu sans entrer dans les détails du codage. Et vous avez créé une application réactive qui adoptera sans effort les changements de votre site web.