---
title: Comment dynamiser votre site web avec Vue.js et un effort minimal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-02T11:01:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-power-up-your-website-with-vue-js-and-minimal-effort-dc8042cc383c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FNK6FHUsWkMumrfEmHAt0A@2x.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Vue.js
  slug: vuejs
seo_title: Comment dynamiser votre site web avec Vue.js et un effort minimal
seo_desc: 'By Ondřej Polesný

  You have a static website and you know which framework fits you and your project
  the best. But how do you integrate the framework into the website? How do you split
  the design into components? How do you handle routing between pages...'
---

Par Ondřej Polesný

Vous avez un site web statique et vous savez quel framework vous convient le mieux, à vous et à votre projet. Mais comment intégrer le framework dans le site web ? Comment diviser le design en composants ? Comment gérer le routage entre les pages ? Comment définir où les pages enfants doivent afficher leur contenu spécifique ?

Rendre un site web dynamique est une étape très excitante dans son développement. Cela ressemble à l'installation d'un jeu et à son premier lancement, ou à l'achat d'un nouveau téléphone et à son déballage. Vue.js vous aide à atteindre ce moment très rapidement. Créer des composants et les assembler est comme construire votre site web avec des pièces Lego. Commençons et amusons-nous !

### Intégration de Vue.js

Ayant choisi le bon framework pour mon site web, je peux commencer à intégrer toutes les parties ensemble. Quelles sont ces parties ?

* Modèle HTML — balisage
* Logique du site web — Vue.js et ses composants
* Contenu pour tous les composants — tous les services fournissant des données via leurs API

Avez-vous déjà entendu parler de [JAMstack](https://jamstack.org/) ? C'est une architecture moderne de développement web basée sur ces trois parties que j'ai décrites ci-dessus. Il y a quelques bonnes pratiques supplémentaires sur leur site web, mais nous y viendrons plus tard.

Commençons le développement du site web. Tout d'abord, nous devons ajouter la bibliothèque Vue.js dans notre modèle HTML principal. Si vous prévoyez d'avoir plusieurs pages, vous aurez également besoin du routeur Vue.js. Ajoutez les deux avant la fin de la balise Head.

```
...  <! — version de développement, inclut des avertissements de console utiles →  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>  <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script></head>...
```

Deuxièmement, nous devons choisir un élément qui englobe toute la fonctionnalité de Vue.js. Vue.js n'a pas nécessairement besoin de contrôler tout votre site web, mais seulement une petite partie de celui-ci. Cependant, dans notre cas, nous voulons que Vue.js contrôle toute la page. Par conséquent, nous pouvons choisir l'élément le plus haut et lui attribuer un ID s'il n'en a pas encore.

```
...<body class="is-preload">  <div id="page-wrapper">    <header id="header" class="alt">...
```

Bon travail ! Nous avons maintenant la page principale prête pour les composants Vue.js.

### Disposition des composants

Lorsque vous commencez à découper votre site web en petits morceaux, le processus est dans une certaine mesure toujours le même, indépendamment de la technologie ou du framework utilisé. Il y a toujours des parties de la page qui seront affichées sur toutes les pages, comme le menu principal et le pied de page. Ceux-ci forment votre page maître, ou dans notre cas le modèle maître. Jetons un coup d'œil à l'apparence de ces parties sur mon design.

![Image](https://cdn-media-1.freecodecamp.org/images/B5bClcS18GrM20zcQt0nnugKZ29-0TY61gjl)

1. En-tête incluant le menu principal
2. Pied de page incluant le formulaire de contact

Tout le reste qui se trouve entre les deux est interchangeable en fonction du contexte de la page. En d'autres termes, les parties surlignées restent toujours les mêmes. C'est le milieu qui change en fonction de l'URL.

Tout d'abord, créons deux fichiers vides :

* app.js
* components.js

Placez-les dans le dossier `assets/js` (vous pouvez choisir un autre dossier si vous préférez) et référencez-les dans le site web. Ajoutez ces assets avant la fin de la balise Body. Si vous avez d'autres fonctionnalités JavaScript, assurez-vous d'inclure ces fichiers avant tout autre qui pourrait modifier le balisage HTML.

```
...<script src="assets/js/components.js"></script><script src="assets/js/app.js"></script>...
```

Sur mon site web, il y a 3 pages, donc au total j'aurai 3 URL et 3 composants principaux sur ma page :

* / - Page d'accueil
* /blog - Page de blog
* /about - Page À propos de moi

### Modèle maître

Le fichier HTML principal sera utilisé comme modèle maître pour l'ensemble du site web. Par conséquent, nous devons supprimer tout le contenu spécifique à la page. Nous ne laissons que les éléments qui seront affichés sur toutes les pages du site web. Lorsque je fais cela et que j'ouvre la page dans le navigateur, je vois ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/Vgayc-byp00ZPFvEdC0Qvzxqv7hhF7zxMN8l)

Il y a un en-tête avec le menu (1), un formulaire de contact avec le pied de page (2) et l'espace jaune vide est l'endroit où le contenu de toutes mes pages enfants apparaîtra. Rappelez-vous que nous avons inclus le routeur Vue.js avec la bibliothèque principale du framework Vue.js ? Le routeur va gérer toute la navigation pour nous. Il garantira que chaque page enfant est rendue dans ce modèle maître. Nous devons dire au routeur où les rendre. Dans votre code HTML, trouvez un endroit marqué par la bande jaune et ajoutez le composant suivant là :

```
...<router-view></router-view>...
```

Cela indique au routeur d'utiliser cet endroit pour rendre les pages enfants et leurs composants. Nous devons également ajuster les liens dans la navigation principale des balises `a` habituelles aux liens du routeur. Voici mon implémentation :

```
... <li><router-link to="/">Accueil</router-link></li> <li><router-link to="/blog">Blog</router-link></li> <li><router-link to="/about">À propos</router-link></li>...
```

Si vous avez d'autres paramètres sur vos balises `a`, vous pouvez les utiliser avec les balises router-link également. Le routeur Vue.js s'assurera qu'ils apparaissent dans le code HTML final.

Félicitations, votre modèle maître est terminé.

### Pages enfants

Parce que mon site web est petit et que nous visons une implémentation facile, les pages enfants n'auront pas leur interprétation physique. Cependant, si vous avez beaucoup de pages et que vous souhaitez les séparer en utilisant des fichiers physiques, c'est possible. Dans ce cas, je suggère d'utiliser un compilateur pour générer un fichier JavaScript final minimisé de votre implémentation.

Tout d'abord, initialisons notre application Vue.js et les routes dans le fichier `app.js`. Les routes proviennent directement de la liste des pages ci-dessus. L'implémentation devrait ressembler à ceci :

```
const router = new VueRouter({ routes: [  { path: '/', component: Home },  { path: '/blog', component: Blog },  { path: '/about', component: About } ]})const app = new Vue({ el: '#page-wrapper', router})
```

Nous créons l'instance du routeur et lui passons les URL de toutes nos pages et les noms des composants. Nous n'avons pas encore ces composants, donc j'ai simplement utilisé les noms des pages correspondantes. Nous créerons des composants avec les mêmes noms plus tard.

Chaque application Vue.js est mise en vie en créant une instance de la classe Vue et en la connectant à un élément. Dans mon cas, il s'agit d'une div avec l'id `page-wrapper` — l'élément de niveau supérieur juste sous la balise body. L'instance doit également savoir que nous voulons utiliser le routeur Vue.js. C'est pourquoi l'instance du routeur est passée dans l'instance principale.

La dernière chose que nous devons faire est de définir les composants pour chaque page. Notez que nous devons les créer avant la définition de l'application Vue, sinon ils ne seront pas connus de Vue.js.

Vous vous souvenez du code supprimé du modèle maître ? C'est le contenu de notre composant de page d'accueil. Définissons-le :

```
const Home = { template: `  <div>   <section id="banner">    <div class="inner">     <div class="logo">     ...     </div>     <h2>Ondrej Polesny</h2>     <p>Developer Evangelist + dog lover + freelance bus driver</p>    </div>   </section>   <section id="wrapper">    <div>     <section id="one" class="wrapper spotlight style1">      <div class="inner">       <router-link to="/about" class="image"><img src="images/pic01.png" alt="" /></router-link>       <div class="content">        <h2 class="major">Kentico</h2>        <p>...</p>        <router-link to="/about" class="special">Continue</router-link>       </div>      </div>     </section>     <section id="two" class="wrapper alt spotlight style2">     ...     </section>     <section id="three" class="wrapper spotlight style3">     ...     </section>     <section id="four" class="wrapper alt style1">     ...     </section>     <div class="inner">      <div>       <h2 class="major">Latest blog posts</h2>       <p>...</p>       ... <!-- list of blogs -->      </div>     </div>     <ul class="actions">      <li><a href="/blog" class="button">See all</a></li>     </ul>    </div>   </section>  </div>`}
```

Vous voyez que c'est beaucoup de balisage HTML et cela rend notre fichier `app.js` assez grand et illisible. De plus, certains contenus sont également affichés sur d'autres pages. Par exemple, la liste des articles de blog ou les textes à mon sujet.

### Composants

C'est là que les composants entrent en jeu. Les composants représentent des morceaux de contenu réutilisables qui peuvent être séparés. Ils peuvent également contenir des fonctionnalités. Des exemples sont la collecte de contenu à partir de services externes ou la réécriture de contenu basée sur les actions de l'utilisateur. Ils peuvent également effectuer certains calculs. Jetons un coup d'œil à la manière dont j'ai optimisé la page d'accueil pour utiliser des composants :

```
const Home = { template: `  <div>   <banner></banner>   <section id="wrapper">    <about-overview></about-overview>    <section id="four" class="wrapper alt style1">     <div class="inner">      <div>       <h2 class="major">Latest blog posts</h2>       <p>...</p>       <blog-list limit="4"></blog-list>       <ul class="actions">        <li><a href="/blog" class="button">See all</a></li>       </ul>      </div>     </div>    </section>   </section>  </div>`}
```

Il est important d'identifier correctement les composants. Ils doivent être indépendants et couvrir une fonctionnalité ou un balisage spécifique. Jetons un coup d'œil à la manière dont je les ai séparés :

![Image](https://cdn-media-1.freecodecamp.org/images/j2whyBT5pzhObo8-R5XkYC0hoLM7vNnJndhg)

J'ai identifié 3 composants :

* Bannière (1)
* Aperçu à propos (2)
* Liste de blog (3)

Notez que certains contrôles sont à l'extérieur des zones jaunes qui marquent les composants respectifs. Par exemple, regardez le composant Liste de blog. Vous voyez que le bouton « See all », le paragraphe introduisant la section et son en-tête sont exclus du composant. La raison est que le composant Liste de blog sera également utilisé sur la page Blog. Ces textes seront différents et le bouton « See all » ne sera pas affiché du tout. Par conséquent, le composant doit inclure uniquement des morceaux de contenu et de balisage réutilisables.

J'ai ajouté les définitions de ces composants au fichier `components.js`. Ils peuvent être utilisés indépendamment, donc si vous voulez les séparer davantage, vous pouvez.

La bannière est le plus simple de ces composants. Elle ne contient aucune fonctionnalité, juste du balisage HTML. Voyez à quoi elle ressemble ci-dessous :

```
Vue.component('banner', { template: `  <section id="banner">   <div class="inner">    <div class="logo">     <span class="icon">      <img src="images/profile-picture.jpg" alt="" />     </span>    </div>    <h2>Ondrej Polesny</h2>    <p>Developer Evangelist + dog lover + freelance bus driver</p>   </div>  </section>` })
```

Chaque composant doit avoir un nom unique (banner) et un modèle, qui est simplement du balisage HTML. Habituellement, les composants contiennent également des données et d'autres fonctions dont ils ont besoin pour leur fonctionnalité. Jetons un coup d'œil au composant Liste de blog :

```
Vue.component('blog-list', { props: ['limit'], data: function(){  return {   articles: [    {     url: 'https://medium.com',     header: 'How to start creating an impressive website for the first time',     image: 'https://cdn-media-1.freecodecamp.org/images/1*dVlw9tLq4lVaXrGG0gZc8Q@2x.png',     teaser: `OK, so you know you want to build a website. You have an idea how it should look like and what content it should display. You are sure that it should be fast, eye-pleasing, gain a lot of traction, and attract many visitors. But how do you create that? What are the trends around building websites these days? How are others building successful websites and where should YOU start? Let's give you a head start!`    },    …   ]  } }, template: `  <section class="features">   <article v-for="article in articles">    <a :href="article.url" class="image"><img :src="article.image" alt="" /></a>    <h3 class="major">{{article.header}}</h3>    <p>{{article.teaser}}</p>    <a :href="article.url" class="special">Continue reading</a>   </article>  </section>`})
```

Dans le cadre du composant Liste de blog, je veux lister les derniers articles de blog. Je veux également pouvoir limiter le nombre d'articles affichés sur la page d'accueil aux 4 derniers articles uniquement. Ainsi, j'ai introduit une propriété _limit_. Je l'utiliserai plus tard lorsque le contenu proviendra du service de contenu. La limite sera définie dans le balisage lors de l'utilisation du composant : `<blog-list limit="4">.

Dans le modèle (balisage), il y a un simple cycle `v-for` qui itère sur un tableau d'articles. Le deux-points `:href` avant tout attribut signifie qu'il sera résolu par Vue.js vers une variable spécifiée, par exemple l'URL de l'article. Les accolades `{{article.teaser}}` ont le même effet.

Les articles sont définis dans la propriété `data` au sein d'un objet. Plus tard, je vous montrerai comment stocker ce contenu en dehors d'un composant, dans un CMS headless. Il s'agit d'un service de contenu dans le cloud. Mais ne vous inquiétez pas, aucun argent ne sera dépensé car nous utiliserons le plan gratuit du CMS headless [Kentico Cloud](http://bit.ly/2QzUALM).

Le dernier composant « Aperçu à propos » ressemble beaucoup. Alors, passons-le pour l'instant. Jetons un coup d'œil à la manière de coller les composants et les pages ensemble et de créer deux pages encore manquantes — À propos et Blog.

### Création d'autres pages

Ces deux pages — À propos et Blog — seront créées de la même manière que nous avons créé la page d'accueil. Notez que nous ne créons pas vraiment des composants, mais des pages. Par conséquent, il n'y aura pas de définition `Vue.component()`, mais un simple objet avec une propriété — template. Ces objets iront dans le fichier `app.js`. Jetons un coup d'œil à la page Blog :

```
const Blog = { template: `  <section id="wrapper">   <header>    <div class="inner">     <h2>Blog posts</h2>     <p>Here you can see list of all blog posts that I published.</p>    </div>   </header>   <div class="wrapper">    <div class="inner">     <blog-list></blog-list>    </div>   </div>  </section>`}
```

Vous voyez, cette page est devenue très simple car le composant Liste de blog a pu être réutilisé.

Vous vous souvenez lorsque nous créions des routes pour le routeur Vue.js auparavant ? Nous avons connecté chaque route avec un identifiant non existant décrit comme un composant.

```
const router = new VueRouter({ routes: [  { path: '/', component: Home },  { path: '/blog', component: Blog },  { path: '/about', component: About } ]})
```

En réalité, ces composants sont des pages. Des pages que nous venons de créer comme des objets simples et que nous avons assignées à des constantes. Notez que le nom de ces constantes doit correspondre aux noms des composants des routes respectives. Par exemple, une page sur la route `/blog` doit être définie comme un objet dans la constante `Blog`.

### Finalisation

Lorsque vous avez défini tous vos composants et pages, ouvrez votre modèle maître et voyez les résultats. Le site web est dynamique même si nous n'avons pas utilisé de technologie de rendu côté serveur. Le routage et le rendu des composants sont effectués par Vue.js.

Un dernier conseil : si vous voyez un site web incomplet, il est probable que vous ayez une faute de frappe dans l'un des fichiers JavaScript. Ouvrez la console de votre navigateur en appuyant sur `F12` (ou `CTRL+SHIFT+C`) et passez à l'onglet Console. Vous y verrez la cause de l'erreur.

Félicitations ! Vous venez de rendre votre site web dynamique. Dans le prochain article, je vous montrerai comment séparer le contenu des composants et créer une véritable architecture de microservices avec un [CMS headless](http://bit.ly/2QzUALM).

#### Autres articles de la série :

1. [How to start creating an impressive website for the first time](http://bit.ly/2Duglu1)
2. [How to decide on the best technology for your website?](http://bit.ly/2N0kXY4)
3. **Comment dynamiser votre site web avec Vue.js et un effort minimal**
4. [How to Mix Headless CMS with a Vue.js Website and Pay Zero](http://bit.ly/2CyDnhX)
5. [How to Make Form Submissions Secure on an API Website](http://bit.ly/2P0gidP)
6. [Building a super-fast and secure website with a CMS is no big deal. Or is it?](http://bit.ly/2QVSm9a)
7. [How to generate a static website with Vue.js in no time](http://bit.ly/2PN46Jy)
8. [How to quickly set up a build process for a static site](http://bit.ly/2Dv2UGS)