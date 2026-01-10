---
title: Structure du code d'application universelle dans Nuxt.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-15T02:50:30.000Z'
originalURL: https://freecodecamp.org/news/universal-application-code-structure-in-nuxt-js-4cd014cc0baa
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lwIEF0F3eDlMKR1hKZic7Q.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: vue
  slug: vue
- name: Vue.js
  slug: vuejs
seo_title: Structure du code d'application universelle dans Nuxt.js
seo_desc: 'By Krutie Patel

  A brief summary of source code structure in Nuxt.js

  Are you new to the Nuxt.js framework and totally overwhelmed by the number of folders
  it comes with? Are you also surprised that most of them are empty with just the
  readme file in t...'
---

Par Krutie Patel

#### Un bref résumé de la structure du code source dans Nuxt.js

Êtes-vous nouveau dans le framework Nuxt.js et totalement submergé par le nombre de dossiers qu'il contient ? Êtes-vous également surpris que la plupart d'entre eux soient vides avec juste le fichier readme à l'intérieur ? Eh bien, c'est là où j'en étais il y a un peu plus d'un an. Depuis, j'ai toujours voulu apprendre et documenter la magie que chaque dossier apportait au projet Nuxt.

Et maintenant, après avoir implémenté quelques projets avec ce framework, j'ai documenté ma compréhension de la manière dont ces dossiers fonctionnent ensemble pour donner vie à l'application Vue rendue côté serveur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lwIEF0F3eDlMKR1hKZic7Q.jpeg)

Le diagramme ci-dessus est basé sur le [guide Vue SSR](https://ssr.vuejs.org/guide/structure.html#introducing-a-build-step), et étendu avec Nuxt.js à l'esprit. À première vue, vous voyez différents dossiers dans la section _Votre code d'application universelle_, et comment le code est ensuite empaqueté par Nuxt et bundlé par Webpack.

Cet article n'est ni un tutoriel ni un guide complet de Nuxt SSR. Il montre plutôt ce qui entre dans une application universelle.

Bien que vous voyiez les modules, serverMiddleware et plugins en haut du diagramme, commençons d'abord par le _Store_.

### Vuex Store (/store)

Nuxt est pré-empaqueté avec Vuex, mais il n'est pas activé à moins que vous ne créiez un store Vuex dans le répertoire _/store_ et que vous créiez le store.

Il s'agit d'un répertoire très spécial pour tout projet piloté par les données. C'est ici que vous pouvez créer un data-store, ainsi que définir l'action _nuxtServerInit_. Cela se trouve être également le tout premier hook de cycle de vie !

```
const createStore = () => {  return new Vuex.Store({     ...  })}
```

Lorsque l'utilisateur accède initialement à votre application, cela aide à remplir/mettre à jour le store. Il maintient également l'état de vos données dans toute l'application.

### Route Middleware (/middleware)

Il existe trois types différents de route middleware disponibles dans Nuxt. Ils sont tous définis en un seul endroit central — dans le répertoire _/middleware_.

À partir de là, vous pouvez les utiliser de les manières suivantes :

* Middleware global — (entrée via la configuration Nuxt et affecte toutes les routes)

```
// nuxt.config.js 
```

```
export default {  router: {    middleware: 'authenticated'  },}
```

* Middleware de layout (entrée via les layouts et affecte un groupe de routes correspondantes, c'est-à-dire certaines pages à voir/accéder uniquement par les utilisateurs authentifiés)

```
// layouts/default.vue
```

```
export default {  middleware: 'authenticated-basic-plan-user'}
```

* Middleware de page (entrée via le composant de page et affecte une seule route)

```
// pages/index.vue
```

```
export default {   middleware: 'subscribed'}
```

Les middlewares ci-dessus sont traités dans cet ordre exact — ce qui signifie que leurs priorités sont non négociables. Vous devez donc réfléchir et planifier soigneusement votre application pour en tirer le meilleur parti.

### Composants Vue

Il existe trois répertoires où les fichiers _.vue_ sont créés dans un projet Nuxt.

#### **1. Composants de page ? (/pages)**

Il s'agit du répertoire le plus important de tous qui abrite les vues et les routes de l'application. Les composants Vue.js créés ici sont directement convertis en routes d'application.

La véritable puissance des composants de page réside dans les routes dynamiques. Vous pouvez les utiliser pour générer des URL SEO friendly et orientées données. Les routes dynamiques sont générées en fonction de votre structure de répertoires sous _/pages_.

En outre, Nuxt ajoute trois méthodes spéciales aux composants de page qui ne sont disponibles nulle part ailleurs. Il s'agit de _validate()_, _asyncData()_ et _fetch()_.

```
// pages/index.vue 
```

```
export default {
```

```
  validate() {     // valide les paramètres d'URL dynamiques     // vérifie la disponibilité des données  },   asyncData() {     // définit les données du composant  },
```

```
  fetch() {    // ne définit pas les données du composant, mais     // récupère d'autres données contextuelles  }
```

```
}
```

#### **2. Composants de layout (/layouts)**

Les composants de layout alimentent les aspects structurels de votre application. Les composants communs trouvés sur toutes les pages sont créés ici (comme le menu principal, le menu secondaire, l'en-tête, le pied de page, etc.). Ils sont situés dans le répertoire _/layouts_.

Vous pouvez être aussi créatif que vous le souhaitez ici, après tout, ce sont des composants Vue.js. N'oubliez pas d'ajouter _<nux_t/> dans la zone de contenu principale du layout.

```
<template>  &lt;div>     <nuxt/>  </div></template>
```

Incorporez le _route-middleware_ et l'état des données du _store_ avec le composant de layout pour construire des fonctionnalités parfaites de _qui-voit-quoi_ pour tout nombre de types d'utilisateurs avec des scénarios variés. Vous pouvez obtenir un peu plus que juste avec une interface utilisateur personnalisée.

#### **3. Composants Vue.js (/components)**

Ce sont des composants Vue réguliers, mais polyvalents. Ils sont créés sous le répertoire _/components_. Ils ne sont pas superchargés avec des méthodes spéciales comme les composants de page.

Mais ils vous permettent de structurer et d'organiser votre logique métier. Ils cachent également le balisage lourd des composants **page** et **layout**. Cela rend votre base de code plus gérable.

Maintenant, regardez de près — pouvez-vous voir la structure partielle des dossiers dans ce diagramme de cycle de vie de Nuxt ?  
**Indice :** Store (nuxtServerInit), Route Middleware et composants de page (méthodes validate, asyncData et fetch)

### Assets

#### **Assets Webpack (/assets)**

Les assets tels que les fichiers JavaScript, les polices personnalisées et les fichiers CSS sont traités par Webpack à l'aide de chargeurs spécifiques (css-loader, file-loader, url-loader, etc.) selon les types de fichiers. Par exemple, si vous écrivez votre CSS au format _.scss_ ou _.less_, Webpack traitera ces fichiers à l'aide d'un chargeur spécifique et produira un fichier _.css_ compilé qui peut être utilisé par le navigateur.

Vous pouvez même personnaliser votre _nuxt.config.js_ pour instruire Webpack de minifier et d'optimiser les images dans le dossier des assets dans le cadre de votre processus de construction. Après que Webpack ait traité les fichiers, il attache un code de hachage — _par exemple, index.4258e3668a44556dd767.js_ — aux éléments traités, ce qui aide au cache à long terme des assets dynamiques et au cache-busting.

#### **Assets statiques (/static)**

Pour les assets qui ne changeront pas, vous pouvez les mettre en toute sécurité dans le dossier _static_. Webpack ignore le dossier static et ne traitera rien dedans.

### Modules, serverMiddleware et plugins

Ils sont tous définis (par leur chemin) dans la configuration Nuxt. Ils sont accessibles globalement dans l'application Nuxt.

#### **Modules (/modules)**

Une nouvelle application Nuxt est pré-empaquetée avec Vue, Vue Router, Vuex, Vue Server Rendered et Vue Meta par défaut.

Mais vous pouvez vous demander, qu'en est-il des fonctionnalités comme Sitemap, Google Analytics, Progressive Web Apps, ou plus ? Si vous pensez à utiliser des modules, alors oui, vous avez raison, c'est là que la puissance des modules Nuxt entre en jeu.

#### **serverMiddleware (c'est-à-dire /api)**

serverMiddleware peut être considéré comme un point d'extension pour votre application. Ils sont spéciaux car ils ont accès à l'instance sous-jacente du framework connect.

Puisque Nuxt utilise **connect** pour livrer l'application, il permet à des fonctions personnalisées d'être accrochées à la pipeline de requête sous-jacente en tant que middleware.

Vous pouvez utiliser serverMiddleware pour :

* Créer un point de terminaison API pour se connecter à des applications externes.
* Créer un point de terminaison API pour envoyer des emails aux utilisateurs depuis votre application Nuxt.
* Accéder et modifier la requête de n'importe quelle manière, même avant qu'elle n'atteigne Nuxt.

Notez que vous n'avez aucun dossier vide pré-rempli pour serverMiddleware et modules. Vous les créez lorsque cela est nécessaire.

#### **Plugins (/plugins)**

Vous pouvez faire en sorte que vos mixins, filtres ou directives Vue existants travaillent plus dur simplement en les convertissant en plugins Nuxt. Vous les placez dans le répertoire _/plugins_ qui accompagne une nouvelle installation de Nuxt.

Mais la plupart du temps, vous finirez par ajouter des packages externes ou des bibliothèques Vue en tant que plugins Nuxt. Vous les incorporez dans Nuxt en utilisant simplement la syntaxe _Vue.use()_. Certains des plugins de base que j'utilise toujours dans mon implémentation Nuxt sont Vue Bootstrap, la validation de formulaire, l'ensemble d'icônes font-awesome et axios.

Ce n'est pas la fin des plugins. Vous pouvez écrire des plugins personnalisés et les ajouter à la racine de l'application. Ils sont disponibles globalement dans votre application Nuxt. C'est ma manière préférée d'ajouter des transitions GreenSock ou Scroll-Magic personnalisées au projet, et de les utiliser dans les composants Vue _(/components)_ et Page _(/pages)_.

#### Aperçu de haut niveau des modules, serverMiddleware et plugins

### Package, bundle et livraison

Une fois que vous avez les fonctionnalités souhaitées en place, vous construisez votre application en utilisant _npm run build_. Nuxt package votre application.

Comme le montre le diagramme ci-dessous, _index.js_ est le point d'entrée principal, qui importe _app.js_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5K1HLp5zxlKfwlM7X2BdZw.jpeg)
_Nuxt package votre code — Webpack bundle et livre votre code_

_App.js_ définit l'instance racine Vue. Si vous regardez de près dans _.nuxt/App.js_, ce n'est rien d'autre qu'un composant Vue.

Une fois cette instance racine Vue définie, l'entrée client (_client.js_) crée une nouvelle instance basée sur celle-ci et la monte sur l'élément DOM. Les utilisateurs finaux voient une nouvelle instance d'une application dans leurs navigateurs. Pendant ce temps, l'entrée serveur (_server.js_) crée une nouvelle instance d'application pour chaque requête.

Et enfin, Webpack bundle votre application afin que le code s'exécute à la fois côté client et côté serveur. Le bundle serveur rend le côté serveur, et le bundle client hydrate le balisage HTML statique dans le navigateur. Il le transforme en un DOM dynamique qui peut réagir aux changements de données côté client.

Nuxt fait tout cela pour nous, directement, donc vous n'avez pas à écrire cette configuration manuellement. Beaucoup de complexité entre dans les deux dernières étapes — l'empaquetage et le bundling. Mais Nuxt cache tout cela pour vous. Vous pouvez vous concentrer sur le code de l'application qui livre finalement l'application finale.

### Conclusion

J'espère que cet aperçu de haut niveau de la structure du code de l'application vous fait avancer d'un pas dans votre parcours d'apprentissage du framework Nuxt.

Ceci est l'une des nombreuses perspectives alternatives pour vous aider à comprendre comment tout s'assemble dans une application Nuxt.

Pour moi personnellement, ce petit exercice m'aide à :

* cartographier les exigences du projet par rapport aux fonctionnalités Nuxt prêtes à l'emploi
* lister les modules et plugins communautaires pertinents qui sont déjà disponibles, et
* identifier les éléments restants/complexes qui nécessitent un développement personnalisé.

#### **Liens vers les diagrammes avec des versions haute résolution des diagrammes utilisés ci-dessus**

1. [Hooks de cycle de vie de Nuxt Js](http://bit.ly/2xv6PDV)
2. [Comprendre les modules, serverMiddleware et plugins](http://bit.ly/2sHNieo)
3. [Code d'application universelle dans Nuxt.js](http://bit.ly/2MFl23s)

N'hésitez pas à nous faire part de vos commentaires, retours ou même suggestions pour de nouvelles idées de diagrammes que vous aimeriez voir — dans la section des commentaires ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IslxntaSDwDHfcKEieqDng.jpeg)
_[https://www.pariksha.io/](https://www.pariksha.io/" rel="noopener" target="_blank" title=")_

Si vous êtes nouveau dans Nuxt, vous pourriez vouloir consulter mon article précédent sur ce sujet « [Pourquoi Nuxt Js est le framework parfait pour votre page de destination ?](https://codeburst.io/why-nuxt-js-is-perfect-framework-for-your-landing-page-53e214649b88) Cela vous donnera un aperçu plus profond des détails de développement d'applications avec Nuxt.

### Êtes-vous Nuxt ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*xV6a7Pxle-OrI10wcbCCeQ.jpeg)

Lorsque [@_achopin](https://twitter.com/_achopin) a demandé à [@vuejsamsterdam](https://twitter.com/vuejsamsterdam), « Êtes-vous Nuxt ? » J'ai pensé, hey… Je suis Nuxt.

Et j'ai créé ces [autocollants Nuxt](https://www.etsy.com/au/shop/CrewShopDesigns) — imprimés professionnellement par Moo Printing et prêts à être expédiés si vous êtes intéressé. Alternativement, vous pouvez les commander sur [RedBubble](https://www.redbubble.com/people/krutie?asc=u) également.