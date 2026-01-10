---
title: Comment générer un site web statique avec Vue.js en un rien de temps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-18T17:33:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-generate-a-static-website-with-vue-js-in-no-time-e74e7073b7b8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LLjrzVGPTIotAeil7DiXyA@2x.png
tags:
- name: JavaScript
  slug: javascript
- name: Nuxt.js
  slug: nuxtjs
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Vue.js
  slug: vuejs
seo_title: Comment générer un site web statique avec Vue.js en un rien de temps
seo_desc: 'By Ondřej Polesný

  You have decided to build a static site, but where do you start? How do you select
  the right tool for the job without previous experience? How can you ensure that
  you succeed the first time, while avoiding tools that won’t help you ...'
---

Par Ondřej Polesný

Vous avez décidé de créer un site statique, mais par où commencer ? Comment choisir le bon outil pour le travail sans expérience préalable ? Comment pouvez-vous garantir que vous réussissez du premier coup, tout en évitant les outils qui ne vous aideront pas à la fin ?

Dans cet article, vous apprendrez comment ajuster un site web Vue.js pour qu'il soit automatiquement généré comme un site statique.

### Introduction

J'ai résumé les différences clés entre un site web basé sur une API et les sites statiques dans mon [article précédent](http://bit.ly/2QVSm9a). Pour rappel, les sites statiques sont :

* Extrêmement rapides
* Sécurisés (car ils ne sont qu'un ensemble de pages statiques)
* Régénérés chaque fois que les éditeurs mettent à jour le contenu
* Compatibles avec des fonctionnalités dynamiques supplémentaires

#### Qu'est-ce qu'un générateur de site statique ?

Un générateur de site statique est un outil qui génère un site web statique à partir de l'implémentation et du contenu d'un site web.

Le contenu peut provenir d'un système de gestion de contenu sans tête, via une API REST. L'implémentation du site web utilise l'un des frameworks JavaScript comme Vue.js ou React. Le résultat d'un générateur de site statique est un ensemble de fichiers statiques qui forment le site web.

![Image](https://cdn-media-1.freecodecamp.org/images/0VwMHb8tn3Cn8aNcazzqntftAKyRki4svRCc)

#### Implémentation d'un site statique

J'ai choisi Vue.js comme framework JavaScript à utiliser. Par conséquent, je travaillerai avec [Nuxt.js](http://bit.ly/2Aiaggm), qui est un générateur de site statique pour Vue.js.

Si vous utilisez un autre framework, recherchez un générateur de site statique construit sur ce framework (par exemple [Gatsby](http://bit.ly/2ypBwZ7) pour [React.js](http://bit.ly/2PGeCTL)).

Essentiellement, Nuxt est une combinaison de plusieurs outils qui ensemble vous permettent de créer des sites statiques. Les outils incluent :

* Vue2 — Bibliothèque principale de Vue.js.
* Vue Router — Gère le routage des URL pour les pages du site web.
* Vuex — Magasin de mémoire pour les données partagées par les composants.
* Vue Server Renderer — Permet le rendu côté serveur des pages avant la génération des fichiers statiques.
* Vue-Meta — Gère les métadonnées des pages.

Nuxt définit également comment le site web doit être construit pour générer des fichiers statiques.

#### Installation

Pour commencer à créer des sites web avec Nuxt, vous devez l'installer. Voir les instructions d'installation détaillées sur la [page web de Nuxt.js](http://bit.ly/2R0LTJH). En résumé, vous avez besoin de `npx` (fournis avec NPM par défaut) installé et exécutez :

```
npx create-nuxt-app <nom-du-site>
```

Vous pouvez simplement utiliser les sélections par défaut, sauf si vous avez des préférences contraires.

#### Composants

Dans [l'un de mes articles précédents](http://bit.ly/2zLRE8a), j'ai expliqué comment créer une mise en page de modèle et des composants. Tous étaient définis dans un seul fichier `components.js`. Cela doit être changé avec Nuxt. Tous les composants doivent être extraits du fichier `components.js` en fichiers séparés dans le dossier `components`. Jetez un œil à mon composant `blog-list` et son implémentation précédente :

```
Vue.component('blog-list', { props: ['limit'], data: function(){  return {   articles: null  } },
```

```
 created: function(){  var query = deliveryClient   .items()   .type('blog_post')   .elementsParameter(['link', 'title', 'image_url', 'image', 'teaser'])   .orderParameter('elements.published', SortOrder.desc);   if (this.limit){   query = query.limitParameter(this.limit);  }  query   .getPromise()   .then(response =>    this.$data.articles = response.items.map(item => ({     url: item.link.value,     header: item.title.value,     image: item.image_url.value != '' ? item.image_url.value : item.image.assets[0].url,     teaser: item.teaser.value    }))   ); },
```

```
 template: `  <section class="features">   <article v-for="article in articles">    ...   </article>  </section> ` });
```

Pour le séparer, vous devez également changer la syntaxe du composant pour correspondre au modèle suivant :

```
<template> HTML du composant</template><script> export default {  code Vue.js }</script>
```

Par conséquent, mon composant `Blog-list` ajusté ressemble à ceci :

```
<template> <section class="features">  <article v-for="article in blogPosts">   ...  </article> </section></template><script> export default {  props: ['limit'],  computed: {   blogPosts: function(){    return this.$store.state.blogPosts && this.limit && this.$store.state.blogPosts.length > this.limit ? this.$store.state.blogPosts.slice(0, this.limit) : this.$store.state.blogPosts;   }  } }</script>
```

Vous voyez que le modèle est resté le même. Ce qui a changé, c'est l'implémentation qui est maintenant dans la section `export default`. De plus, il y avait une fonction qui récupérait les données du CMS sans tête Kentico Cloud.

Ce contenu est maintenant stocké dans le magasin Vuex. J'expliquerai cette partie plus tard. Convertissez tous vos composants de cette manière, pour contenir le modèle dans les balises `<template>` et l'implémentation dans les balises `<script>`. Vous devriez obtenir une structure de fichiers similaire à la mienne :

![Image](https://cdn-media-1.freecodecamp.org/images/cZ4HD2jJIJ0bTeTi5ZGwFYRTMYr2p6L0HQzL)

Notez que j'ai deux nouveaux composants ici — Menu et Header. Comme mon objectif était également d'améliorer les performances, j'ai décidé de supprimer jQuery de mon site web. jQuery est une bibliothèque assez grande et lourde qui était utilisée uniquement pour de petits effets UI. J'ai pu les recréer en utilisant uniquement Vue.js. Par conséquent, j'ai converti le HTML statique représentant l'en-tête en composant. J'ai également ajouté la fonctionnalité liée à l'UI dans la fonction `mounted` de ce composant.

```
mounted: function(){ window.addEventListener('scroll', this.scroll); ...},methods: { scroll: function(){  ... }}
```

### Gestion des événements Vue.js avec Nuxt

J'utilisais les événements Vue dans mon site web. La principale raison était le contrôle reCaptcha utilisé pour la validation de formulaire. Lorsqu'il était initialisé, il diffusait l'événement afin que le composant de formulaire puisse déverrouiller le bouton de soumission du formulaire de contact.

Avec Nuxt, je n'utilise plus les fichiers `app.js` ou `components.js`. Par conséquent, j'ai créé un nouveau fichier `recaptcha.js` qui contient une fonction simple émettant l'événement lorsque reCaptcha est prêt. Notez que, au lieu de créer une nouvelle instance Vue.js uniquement pour les événements (`let bus = new Vue();` dans mon ancien code), il est possible d'utiliser simplement `this.$nuxt` de la même manière.

```
var recaptchaLoaded = function(){ this.$nuxt.$emit('recaptchaLoaded');}
```

### Mise en page et pages

Le cadre principal de la page était `index.html`, et chaque page définissait sa propre mise en page dans des constantes qui étaient transmises au routeur Vue.

Avec Nuxt, le cadre principal incluant la balise `<html>`, les balises meta et autres éléments essentiels de toute page HTML sont gérés par Nuxt. L'implémentation réelle du site web ne gère que le contenu dans les balises `<body>`. Déplacez la mise en page commune à toutes vos pages dans `layouts/default.vue` et respectez le même modèle que pour les composants. Ma mise en page ressemble à ceci :

```
<template> <div>  <Menu></Menu>  <div id="page-wrapper">   <Header></Header>   <nuxt/>   <section id="footer">    <div class="inner">     ...     <ContactForm></ContactForm>     ...    </div>   </section>  </div> </div></template><script> import ContactForm from '~/components/Contact-form.vue' import Menu from '~/components/Menu.vue' import Header from '~/components/Header.vue'  export default {  components: {   ContactForm,   Menu,   Header  } } </script>
```

La mise en page est essentiellement le balisage HTML de mon ancien `index.html`. Cependant, notez la section `<script>`. Tous les composants que je souhaite utiliser dans ce modèle de mise en page doivent être importés depuis leur emplacement et spécifiés dans l'objet exporté.

![Image](https://cdn-media-1.freecodecamp.org/images/FwQ-P1izN6Qai74S7TrMPcJGJ2SOL-7K93X-)

Les composants de page étaient précédemment définis dans `app.js` comme des constantes. Jetez un œil à ma ancienne page d'accueil par exemple :

```
const Home = { template: `  <div>   <banner></banner>   <section id="wrapper">    <about-overview></about-overview>    ...    <blog-list limit="4"></blog-list>    <ul class="actions">     <li><a href="/blog" class="button">Voir tout</a></li>    </ul>    ...   </section>  </div> `}
```

Toutes ces pages doivent être définies dans des fichiers séparés dans le dossier `pages`. La page principale est toujours appelée `index.vue`. Voici à quoi ressemble ma nouvelle `pages/index.vue` (ma page d'accueil) :

```
<template> <div>  <Banner></Banner>  <section id="wrapper">   <AboutOverview></AboutOverview>   ...   <BlogList limit="4"></BlogList>   <ul class="actions">    <li><a href="/blog" class="button">Voir tout</a></li>   </ul>   ...  </section> </div></template><script> import Banner from '~/components/Banner.vue' import AboutOverview from '~/components/About-overview.vue' import BlogList from '~/components/Blog-list.vue'  export default {  components: {   Banner,   AboutOverview,   BlogList  }, }</script>
```

### Où stocker les ressources

Sur chaque site web, il y a des ressources comme des feuilles de style CSS, des images, des logos et des JavaScripts. Avec Nuxt, tous ces fichiers statiques doivent être stockés dans le dossier static. La structure du dossier ressemble actuellement à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/pez1-XpfChKIX8aOVP0vP-2BH2cz28MCsFlM)

Lorsque vous référencez des ressources depuis des feuilles de style CSS comme des polices ou des images, vous devez utiliser le dossier static comme racine :

```
background-image: url("~/assets/images/bg.jpg");
```

### Obtenir le contenu

Avec tous les composants et pages en place, nous y arrivons enfin : obtenir le contenu dans les composants.

Obtenir le contenu avec Nuxt est un peu différent de ce qu'il était. L'aspect important de ce processus lors de l'utilisation d'un générateur de site statique est que le contenu doit être rassemblé avant que toutes les pages ne soient générées. Sinon, vous vous retrouverez avec un site web statique, mais les requêtes de contenu seraient toujours dynamiques, atteignant le CMS sans tête depuis le navigateur de chaque visiteur et vous perdriez le principal avantage.

Nuxt contient deux méthodes spéciales qui gèrent la récupération de données asynchrones au bon moment, c'est-à-dire avant que les pages ne soient générées. Ces méthodes sont `asyncData` et `fetch`. Elles sont disponibles uniquement pour les composants de page (c'est-à-dire les fichiers dans le dossier `pages`) et leur but est le même, mais `asyncData` stockera automatiquement les données reçues dans l'ensemble de données du composant.

Cela peut être bénéfique si vous avez de nombreux composants sur une seule page utilisant le même ensemble de données. Dans mon cas, j'ai même plusieurs pages avec de nombreux composants qui doivent partager les mêmes données. Par conséquent, je devrais soit demander les mêmes données sur chaque page, soit utiliser un espace partagé auquel toutes les pages et composants pourraient accéder.

J'ai choisi cette dernière option. Nuxt nous facilite grandement la tâche. Il inclut automatiquement le magasin Vuex qui permet à nos composants et pages d'accéder à toutes les données qui se trouvent dans le magasin. Pour commencer à utiliser le magasin, tout ce que vous avez à faire est de créer un fichier `index.js` dans le dossier `store`.

```
import Vuex from 'vuex'
```

```
const createStore = () => { return new Vuex.Store({  state: () => ({}),  mutations: {},  actions: {}, })}export default createStore
```

Vous voyez que l'instance a quelques propriétés :

* **State**  
L'état est similaire aux données dans les composants. Il contient la définition des champs de données utilisés pour stocker les données.
* **Mutations**  
Les mutations sont des fonctions spéciales autorisées à modifier les données dans l'état (muter l'état).
* **Actions**  
Les actions sont des méthodes simples qui vous permettent, par exemple, d'implémenter la logique de collecte de contenu.

Revenons au composant `Blog-list`. Ce composant a besoin d'un tableau d'articles de blog pour rendre son balisage. Par conséquent, les articles de blog doivent être stockés dans le magasin Vuex :

```
...const createStore = () => { return new Vuex.Store({  state: () => ({   blogPosts: null  }),  mutations: {   setBlogPosts(state, blogPosts){    state.blogPosts = blogPosts;   }  },  actions: {   getBlogPosts (context) {    logique pour obtenir le contenu de Kentico Cloud   }  }, })}
```

Après avoir ajusté le magasin Vuex de cette manière, le composant `Blog-list` peut utiliser ses données :

```
<article v-for="article in $store.state.blogPosts"> ...</article>
```

J'ai déjà partagé l'implémentation complète de ce composant ci-dessus. Si vous l'avez remarqué, il utilise la fonction `computed` comme une couche intermédiaire entre le balisage du composant et le magasin Vuex. Cette couche intermédiaire garantit que le composant affiche uniquement un nombre spécifique d'articles comme configuré dans le champ `limit`.

### Interrogation du CMS sans tête

Peut-être vous souvenez-vous que `deliveryClient` était utilisé pour obtenir des données de [Kentico Cloud](http://bit.ly/2QzUALM) dans les composants.

_Avis de non-responsabilité : Je travaille pour Kentico, un fournisseur de CMS qui propose à la fois un CMS traditionnel (couplé) et un nouveau CMS sans tête basé sur le cloud — Kentico Cloud._

La même logique peut être utilisée ici dans les actions du magasin Vuex avec un petit ajustement. Kentico Cloud dispose d'un [module pour Nuxt.js](http://bit.ly/2Qiovur), installez-le en utilisant la commande suivante :

```
npm i kenticocloud-nuxt-module --savenpm i rxjs --save
```

Avec ce module, vous pouvez continuer à utiliser `deliveryClient` comme avant, simplement avec un préfixe `$`. Donc, dans mon cas, la logique pour obtenir les articles de blog ressemble à ceci :

```
...getBlogPosts (context) { return this.$deliveryClient  .items()  ...  .orderParameter('elements.published', SortOrder.desc)  .getPromise()  .then(response => {   context.commit('setBlogPosts', response.items.map(item => ({    url: item.link.value,    header: item.title.value,    image: item.image_url.value != '' ? item.image_url.value : item.image.assets[0].url,    teaser: item.teaser.value   })))  }); },...
```

Si vous souhaitez utiliser le tri avec `orderParameter`, vous devrez peut-être inclure une autre importation dans le fichier `store/index.js` :

```
import { SortOrder } from 'kentico-cloud-delivery'
```

Maintenant que la logique de collecte de contenu est implémentée, il est temps d'utiliser la fonction asynchrone spéciale fetch dont j'ai parlé précédemment. Voici mon implémentation dans la page `index.vue` :

```
async fetch ({store, params}) { await store.dispatch('getBlogPosts')}
```

L'appel à `store.dispatch` invoque automatiquement l'action `getBlogPosts`. Dans l'implémentation de `getBlogPosts`, notez l'appel à `context.commit`. `context` fait référence au magasin Vuex et `commit` transmettra les données des articles de blog à la mutation `setBlogPosts`. La mise à jour de l'ensemble de données avec les articles de blog modifie l'état du magasin (le mute). Et nous avons presque terminé !

#### Autres options de stockage de contenu

J'ai utilisé le CMS sans tête [Kentico Cloud](http://bit.ly/2QzUALM) et son API ici, car je l'utilise dans tous les articles de cette série. Si vous souhaitez également explorer d'autres options, vous pouvez trouver une liste indépendante de CMS sans tête et de leurs fonctionnalités sur [headlesscms.org](http://bit.ly/2S8gxSi).

Si vous ne souhaitez pas utiliser un CMS sans tête et son API, vous pouvez décider de stocker votre contenu d'une autre manière — généralement sous forme d'ensemble de fichiers markdown directement stockés dans votre projet ou dépôt Git. Vous pouvez trouver un bel exemple de cette approche dans le [dépôt GitHub nuxt-markdown-example](http://bit.ly/2R5PQAo).

### Configuration de Nuxt

L'ensemble de l'application doit être correctement configuré à l'aide du fichier `Nuxt.config.js`. Ce fichier contient des informations sur les modules utilisés, leur configuration et les éléments essentiels du site comme le titre ou les balises SEO. La configuration de mon site web ressemble à ceci :

```
export default { head: {  title: 'Ondrej Polesny',  meta: [   { charset: 'utf-8' },   ...   { hid: 'description', name: 'description', content: 'Ondrej Polesny — Developer Evangelist + dog lover + freelance bus driver' }  ],  script: [   { src: 'https://www.google.com/recaptcha/api.js?onload=recaptchaLoaded', type: "text/javascript" },   { src: 'assets/js/recaptcha.js', type: "text/javascript" }  ], }, modules: [  'kenticocloud-nuxt-module' ], kenticocloud: {  projectId: '*KenticoCloud projectId*',  enableAdvancedLogging: false,  previewApiKey: '' }, css: [  {src: 'static/assets/css/main.css'}, ], build: {  extractCSS: {   allChunks: true  } }}
```

La section head décrit les éléments essentiels du site web comme le `title` et les balises `meta` que vous souhaitez inclure dans l'en-tête.

Notez la configuration des `modules` et de `kenticocloud`. La première liste tous les modules dont dépend votre application et la seconde est une configuration spécifique au module. C'est ici que vous devez mettre votre clé API de projet.

Pour voir toutes les options des balises meta, veuillez vous référer à [https://github.com/declandewet/vue-meta](http://  https://github.com/declandewet/vue-meta)

### Exécution et génération

Les sites statiques doivent être générés avant que quiconque puisse y accéder ou les télécharger sur un serveur FTP. Cependant, il serait très chronophage de régénérer le site chaque fois qu'un changement a été apporté pendant la phase de développement. Par conséquent, vous pouvez exécuter l'application localement en utilisant :

```
npm run dev
```

Cela créera un serveur de développement pour vous et vous permettra d'accéder à votre site web sur http://localhost:8000 (ou similaire). Tant que vous gardez votre console en cours d'exécution de cette commande, chaque changement que vous apportez à vos scripts aura un effet immédiat sur le site web.

Pour générer un vrai site statique, exécutez la commande suivante :

```
npx nuxt generate
```

Le résultat, c'est-à-dire votre site statique, sera dans le dossier `dist`. N'hésitez pas à ouvrir n'importe quelle page dans votre éditeur de texte préféré et vérifiez si le code source contient du contenu provenant du CMS sans tête. Si c'est le cas, il a été récupéré avec succès.

### Conclusion

Avoir un site statique généré améliorera grandement les performances du site web. Comparé aux sites traditionnels, le serveur web n'a pas besoin d'effectuer d'opérations CPU lourdes. Il sert uniquement des fichiers statiques.

Comparé aux sites web basés sur une API, les clients reçoivent les données demandées instantanément avec la toute première réponse. C'est ce qui les rend si rapides — ils n'ont pas besoin d'attendre que le contenu externe soit livré via des requêtes asynchrones supplémentaires. Le contenu est déjà là dans la première réponse du serveur. Cela améliore considérablement l'expérience utilisateur.

Convertir le site de l'implémentation Vue.js aux définitions Nuxt est très simple et ne nécessite pas de connaissances approfondies de tous les composants et packages utilisés.

Avez-vous réussi à créer votre premier site statique ? Avez-vous rencontré des difficultés ? Veuillez laisser un commentaire.

Dans le prochain article, je me concentrerai sur la régénération automatisée des sites statiques et sur l'endroit où les héberger, alors restez à l'écoute.

#### Autres articles de la série :

1. [Comment commencer à créer un site web impressionnant pour la première fois](http://bit.ly/2Duglu1)
2. [Comment décider de la meilleure technologie pour votre site web ?](http://bit.ly/2N0kXY4)
3. [Comment booster votre site web avec Vue.js et un effort minimal](http://bit.ly/2zLRE8a)
4. [Comment mélanger un CMS sans tête avec un site web Vue.js et payer zéro](http://bit.ly/2CyDnhX)
5. [Comment sécuriser les soumissions de formulaires sur un site web API](http://bit.ly/2P0gidP)
6. [Créer un site web super rapide et sécurisé avec un CMS n'est pas un gros problème. Ou l'est-il ?](http://bit.ly/2QVSm9a)
7. **Comment générer un site web statique avec Vue.js en un rien de temps**
8. [Comment configurer rapidement un processus de construction pour un site statique](http://bit.ly/2Dv2UGS)