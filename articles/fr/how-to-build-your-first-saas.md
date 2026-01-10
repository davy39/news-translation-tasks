---
title: Le manuel SaaS – Comment construire votre premier produit logiciel en tant
  que service étape par étape
subtitle: ''
author: kyw
co_authors: []
series: null
date: '2020-06-30T15:52:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-your-first-saas
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/The-SaaS-Handbook-Book-Cover--1-.png
tags:
- name: SaaS
  slug: saas
seo_title: Le manuel SaaS – Comment construire votre premier produit logiciel en tant
  que service étape par étape
seo_desc: 'In this extensive write-up, I''ll cover how all the main pieces came together
  for the first SaaS I ever launched.

  From implementing favicon to deploying to a cloud platform, I will share everything
  I learned. I''ll also share extensive code snippets, b...'
---

Dans cet article détaillé, je vais expliquer comment toutes les pièces principales se sont assemblées pour le premier SaaS que j'ai jamais lancé.

De l'implémentation de la favicon au déploiement sur une plateforme cloud, je vais partager tout ce que j'ai appris. Je vais également partager des extraits de code détaillés, des meilleures pratiques, des leçons, des guides et des ressources clés. 

J'espère que quelque chose ici vous sera utile. Merci de lire. ❤️

## Table des matières

- <a href="#introduction">Introduction</a>
- <a href="#trouverdesidees">Trouver des idées</a>
- <a href="#lapiletechnologique">La pile technologique</a>
- <a href="#depot">Dépôt</a>
  - <a href="#demarrerledéveloppementfullstacklocalement">Démarrer le développement full-stack localement</a>
- <a href="#client">Client</a>
  - <a href="#scriptsnpmclient">Script Npm</a>
  - <a href="#variablesdenvironnement">Variables d'environnement</a>
  - <a href="#webpacketbabel">Webpack & Babel</a>
  - <a href="#performancesweb">Performances Web</a>
  - <a href="#servicedifférentiel">Service différentiel</a>
  - <a href="#polices">Polices</a>
  - <a href="#icones">Icônes</a>
  - <a href="#favicon">Favicon</a>
  - <a href="#appelsapi">Appels API</a>
  - <a href="#testerlaversiondeproductionlocalement">Tester la version de production localement</a>
  - <a href="#securite">Sécurité</a>
- <a href="#design">Design</a>
  - <a href="#echellesmodulaires">Échelles modulaires</a>
  - <a href="#couleurs">Couleurs</a>
  - <a href="#remiseaceroCSS">Remise à zéro CSS</a>
  - <a href="#unepraiquedestyling">Une pratique de styling</a>
  - <a href="#miseenpage">Mise en page</a>
- <a href="#serveur">Serveur</a>
  - <a href="#structuredesfichiers">Structure des fichiers</a>
  - <a href="#scriptsnpmserveur">Script Npm</a>
  - <a href="#basededonnees">Base de données</a>
  - <a href="#creationdesschemasdetables">Création des schémas de tables</a>
  - <a href="#suppressiondunebasededonnees">Suppression d'une base de données</a>
  - <a href="#conceptionrequetesSQL">Conception de requêtes SQL</a>
  - <a href="#redis">Redis</a>
  - <a href="#gestiondeserreursetjournalisation">Gestion des erreurs & Journalisation</a>
  - <a href="#lienpermanentpourpartagedurl">Lien permanent pour partage d'URL</a>
- <a href="#systemedauthentificationutilisateur">Système d'authentification utilisateur</a>
- <a href="#email">Email</a>
  - <a href="#implementation">Implémentation</a>
  - <a href="#modelesdemail">Modèles d'email</a>
  - <a href="#commentobtenirlunedeceshi@examplecom">Comment obtenir l'un de ces <code><strong>hi@example.com</strong></code></a>
- <a href="#tenancy">Tenancy</a>
- <a href="#nomdedomaine">Nom de domaine</a>
  - <a href="#commentobtenirlunedecesappexamplecom">Comment obtenir l'un de ces <code><strong>app.example.com</strong></code></a>
- <a href="#deploiement">Déploiement</a>
  - <a href="#deploynodejs">Déployer Nodejs</a>
  - <a href="#deploypostgresql">Déployer Postgresql</a>
  - <a href="#configurerschemasdansbasededonneesdeproduction">Configurer les schémas dans la base de données de production</a>
  - <a href="#deployredis">Déployer Redis</a>
  - <a href="#stockagedefichiers">Stockage de fichiers</a>
  - <a href="#deployernouvellesmodificationsdansbackend">Déployer de nouvelles modifications dans le back-end</a>
- <a href="#hebergervotrespa">Héberger votre SPA</a>
  - <a href="#deployernouvellesmodificationsdansfrontend">Déployer de nouvelles modifications dans le front-end</a>
- <a href="#editeurderichtext">Éditeur de rich-text</a>
- <a href="#cors">CORS</a>
- <a href="#paiementetsouscription">Paiement & Souscription</a>
- <a href="#pageaccueil">Page d'accueil</a>
- <a href="#termesetconditions">Termes et conditions</a>
- <a href="#marketing">Marketing</a>
- <a href="#bienetre">Bien-être</a>

## Introduction

J'ai changé de carrière pour le développement web en 2013. Je l'ai fait pour deux raisons. 

Premièrement, j'ai remarqué que je pouvais me perdre dans la construction de produits orientés client parmi toutes les couleurs et les possibilités infinies d'interactivité. Donc, tout en étant rappelé du cliché "_Trouvez un travail que vous aimez faire, et vous n'aurez jamais à travailler un jour de votre vie_", je me suis dit "_Pourquoi ne pas en faire un travail ?_" 

Et deuxièmement, je voulais faire quelque chose de moi-même, ayant passé mon adolescence inspiré par le Web 2.0 (Digg.com vers 2005 m'a ouvert le monde !). Le plan était de travailler sur ce dernier tout en travaillant sur le premier.

Il s'avère, cependant, que le travail et la 'fatigue JavaScript' ont suivi et m'ont complètement consumé. Cela n'a pas aidé non plus que j'étais imprudent dans ma poursuite de mon ambition, après avoir été influencé par la rhétorique de 'Silicon Valley'. J'ai lu _Hackers & Painters_ de Paul Graham et _Zero to One_ de Peter Thiel. Je me suis dit, je suis bien motivé ! Je me démène. Je peux le faire aussi !

Mais non, je ne pouvais pas. Du moins pas seul. J'étais toujours épuisé après le travail. Je ne pouvais pas trouver une équipe qui partageait mes rêves et mes valeurs. 

Donc, entre-temps, j'ai répété et réitéré des projets à moitié cuits pendant mon temps libre. J'étais chroniquement anxieux et déprimé. Je me suis calmé au fil des années. Et j'ai commencé à cultiver une philosophie personnelle sur l'entrepreneuriat et la technologie qui s'alignait mieux avec ma personnalité et mes circonstances de vie – jusqu'en septembre 2019.

Le brouillard sur le chemin devant moi s'est enfin dissipé. Je suis devenu assez bon – le travail est devenu moins exigeant, et j'avais maîtrisé ma 'fatigue JavaScript'. Pendant très longtemps, j'ai eu l'énergie mentale, le temps et l'état d'esprit qui m'ont permis de mener à bien un projet parallèle. Et cette fois, j'ai commencé petit. Je croyais que j'avais ça !

Je me trompais.

Puisque j'avais été développeur front-end pendant toute ma carrière, je ne pouvais aller que jusqu'à nommer les choses dont j'imaginais avoir besoin – un 'serveur', une 'base de données', un système 'd'authentification', un 'hôte', un 'nom de domaine', mais _comment_... _où_... et _quoi_..._je..je ne..je ne sais même pas_... ?

Maintenant, je savais que ma vie aurait été plus facile si j'avais décidé d'utiliser l'un de ces outils abstraits comme 'create-react-app', 'firebase SDK', 'ORM', et les services de 'déploiement en un clic'. L'ode de '_Ne réinventez pas la roue. Itérez rapidement_'. 

Mais il y avait quelques qualifications que je voulais que mes décisions remplissent :

- Pas de verrouillage de fournisseur &mdash; Cela excluait l'utilisation du SDK Firebase dans tout mon code. Cela incluait 'create-react-app', car l'éjection de celui-ci m'obligeait à hériter et à maintenir son infrastructure d'outils massive.
- Simple & Minimaliste &mdash; Éviter d'avoir à apprendre une nouvelle syntaxe et des motifs opiniâtres. Cela excluait 1) Les générateurs de projets qui produisent une architecture complexe et des couches de code boilerplate, 2) L'utilisation de bibliothèques tierces telles que 'knex.js' ou l'ORM 'sequelize'.
- Pay-as-you-need &mdash; Je voulais garder mes coûts opérationnels proportionnels au niveau d'utilisation. Cela excluait les services tels que le 'déploiement en un clic'.

Pour être honnête, j'avais les éléments suivants en ma faveur :

- Je construisais un SaaS simple.
- Je n'étais pas anxieux de scalabilité, de domination, de disruption, etc.
- Je conservais toujours mon emploi de jour.
- J'avais accepté mes chances d'échec. ?

Gardez également à l'esprit que :

- C'était un spectacle d'un seul homme&mdash;design, développement, maintenance, marketing, etc.
- Je ne suis pas un programmeur full-stack rockstar 10x.

**Plus important encore**, je voulais suivre un principe directeur : Construire des choses [_de manière responsable_](https://alistapart.com/article/responsible-javascript-part-1/). Bien que, sans surprise, cela ait eu un impact significatif sur ma vitesse de développement, et cela m'a forcé à clarifier mes motivations :

- Si je devais livrer quelque chose le plus rapidement possible, à moins que ce ne soit une question de vie ou de mort, alors je ne résolvais probablement pas un problème unique et difficile. Dans ce cas&mdash;en supposant que j'étais toujours à mon emploi de jour et que je n'avais aucune dette&mdash; Quelle était la précipitation ?
- Et se remettre en question du point de vue éthique : Était-ce même un problème qui devait être résolu ? Quelles seraient les conséquences de second ordre si je le résolvais ? Mes bonnes intentions pourraient-elles être mieux dirigées ailleurs ?

Donc, ce qui suit dans cet article est tout ce que j'ai appris en développant le premier projet que j'ai jamais lancé appelé **Sametable** qui aide à [gérer votre travail dans des feuilles de calcul](https://www.sametable.app). 

Commençons.

## Trouver des idées

Eh bien, tout d'abord, vous devez savoir ce que vous voulez construire. Je perdais le sommeil à ce sujet, en pensant et en remixant des idées, en espérant des moments eureka, jusqu'à ce que je commence à regarder vers l'intérieur :

- Construisez des choses qui résolvent des problèmes que vous rencontrez et qui vous énervent fréquemment.
- Résolvez les soi-disant 'points de douleur' ou 'frictions'. Sortez, ne cessez pas d'écouter les gens et apprenez d'eux.
- Soyez un expert dans votre domaine. Ressentez ses douleurs. Peut-être en résoudre une. Il me semble que beaucoup de fondateurs ont créé une entreprise liée à leur domaine sur lequel ils ont construit leur carrière et leur réseau social.

## La pile technologique

L'apparence de votre pile technologique dépendra de la manière dont vous souhaitez rendre votre application. Voici une [discussion complète](https://developers.google.com/web/updates/2019/02/rendering-on-the-web#wrapup) à ce sujet, mais en résumé :

- **Rendu côté client (CSR) ; SPA ; API JSON** &mdash;
  C'est peut-être l'approche la plus populaire. C'est idéal pour construire des applications web interactives. Mais [soyez conscient](https://macwright.org/2020/05/10/spa-fatigue.html) de ses inconvénients et des étapes pour les atténuer. C'est l'approche que j'ai prise, donc nous en parlerons en détail.

- **Hybride CSR ; Rendu côté client et côté serveur (SSR)** &mdash;
  Avec cette approche, vous construisez toujours votre SPA. Mais lorsqu'un utilisateur demande votre application, par exemple, la page d'accueil, vous rendez le composant de la page d'accueil dans son HTML statique **dans votre serveur** et vous le servez à l'utilisateur. Ensuite, dans le navigateur de l'utilisateur, [l'hydratation](https://reactjs.org/docs/react-dom.html#hydrate) aura lieu pour que tout cela devienne la SPA prévue.

Les principaux avantages de cette approche sont que vous obtenez un bon référencement et que les utilisateurs peuvent voir vos contenus plus rapidement (plus rapide 'First Meaningful Paint'). 

Mais il y a aussi des inconvénients. En plus des coûts de maintenance supplémentaires, nous devrons télécharger la même charge utile deux fois&mdash;D'abord, le HTML, et ensuite, son équivalent Javascript pour l''hydratation' qui exercera un travail significatif sur le thread principal du navigateur. Cela prolonge le 'First time to interactive', et diminue ainsi les avantages obtenus d'un 'First meaningful paint' plus rapide.

  Les technologies adoptées pour cette approche sont [NextJs](https://nextjs.org/), [NuxtJs](https://nuxtjs.org/), et [GatsbyJs](https://www.gatsbyjs.org/).

- **Rendu côté serveur et 'saupoudrez-le de Javascript'**
  &mdash; C'était l'ancienne méthode de construction sur le web !&mdash;Utilisez PHP pour construire vos templates avec des données dans votre serveur, puis liez les gestionnaires d'événements au DOM avec jQuery dans le navigateur. Cette approche aurait pu être mal adaptée pour construire les applications de plus en plus complexes que les entreprises ont demandées sur le web, mais certaines technologies ont émergé pour justifier une réévaluation :

  - [https://stimulusjs.org/](https://stimulusjs.org/)
  - [https://github.com/turbolinks/turbolinks](https://github.com/turbolinks/turbolinks)
  - [https://github.com/phoenixframework/phoenix_live_view](https://github.com/phoenixframework/phoenix_live_view)
  - Pour plus, consultez ce [fil twitter](https://mobile.twitter.com/nateberkopec/status/1260602209475198976)

Pour être honnête, si j'avais été plus patient avec moi-même, je serais allé dans cette voie. Cette approche fait un retour en lumière de l'excès de Javascript sur ce web moderne.

Le fond du problème est : Choisissez n'importe quelle approche avec laquelle vous êtes déjà compétent. Mais soyez conscient des inconvénients associés, et essayez de les atténuer avant de livrer à vos utilisateurs.

Avec cela, voici la pile technologique ennuyeuse de Sametable :

### Front-end

- Webpack, Babel
- **Preact**

### Back-end

- **Node** &mdash; Serveur API avec ExpressJS
- **Postgresql** &mdash; Base de données
- **Redis** &mdash; Stocker les données de session des utilisateurs et mettre en cache les résultats des requêtes.

### Hébergement

- **Google Cloud Platform** &mdash; GAE pour héberger Nodejs, GCE pour héberger Redis.
- **Firebase** &mdash; Pour héberger mon SPA.

<img loading="lazy" src="https://i.imgur.com/CA88ijh.png" alt="Architecture de Sametable" />

## Dépôt

[https://github.com/kilgarenone/boileroom](https://github.com/kilgarenone/boileroom)

Ce dépôt contient la structure que j'utilise pour développer mon SaaS. J'ai un dossier pour les trucs **client**, et un autre pour les trucs **serveur** :

```json
- client
    - src
      - components
      - index.html
      - index.js
    - package.json
    - webpack.config.js
    -.env
    -.env.development
- server
    - server.js
    - package.json
    - .env
- package.json
- .gitignore
- .eslintrc.js
- .prettierrc.js
- .stylelintrc.js

```

La structure de fichiers vise toujours à être plate, cohésive et aussi linéaire que possible à naviguer. Chaque 'composant' est autonome dans un dossier avec tous ses fichiers constituants (html|css|js). Par exemple, dans un dossier de 'route' 'Login' :

```xml
- client
   - src
     - routes
       - Login
         - Login.js
         - Login.scss
         - Login.redux.js
```

Je l'ai appris du [guide de style Angular2](https://angular.io/guide/styleguide#angular-coding-style-guide) qui contient beaucoup d'autres bonnes choses que vous pouvez prendre. Très recommandé.

### Démarrer le développement full-stack localement

Le `package.json` à la racine contient un **script npm** que je vais exécuter pour démarrer **à la fois** mon client et mon serveur pour commencer mon développement local :

```json
"scripts": {
    "client": "cd client && npm run dev",
    "server": "cd server && npm run dev",
    "dev": "npm-run-all --parallel server client"
}
```

Exécutez ce qui suit dans un terminal à la racine de votre projet :

```json
npm run dev
```

## Client

```json
- client
    - src
      - components
      - index.html
      - index.js
    - package.json
    - webpack.config.js
    -.env
    -.env.development
```

La structure de fichiers du 'client' est assez similaire à celle de 'create-react-app'. Le cœur de votre code d'application se trouve dans le dossier `src` qui contient un dossier `components` pour vos composants React fonctionnels ; `index.html` est votre [modèle personnalisé](https://github.com/kilgarenone/boileroom/blob/master/client/config/webpack.development.js#L41-L43) fourni au [`html-webpack-plugin`](https://github.com/jantimon/html-webpack-plugin#options) ; [`index.js`](https://github.com/kilgarenone/boileroom/blob/master/client/src/index.js) est un fichier en tant que [point d'entrée](https://github.com/kilgarenone/boileroom/blob/master/client/config/webpack.common.js#L12-L15) pour Webpack.

<aside class="info">
<p><strong>Note :</strong> J'ai depuis restructuré mon environnement de construction pour atteindre le <a href="#servicedifferentiel">service différentiel</a>. Webpack et Babel ont été organisés différemment, et les scripts npm ont changé un peu. Tout le reste reste le même.</p>
</aside>

### Script Npm (Client)

Le fichier `package.json` du client contient deux scripts npm les plus importants : 1) `dev` pour démarrer le développement, 2) `build` pour bundler pour la production.

```json
"scripts": {
    "dev": "cross-env NODE_ENV=development webpack-dev-server",
    "build": "cross-env NODE_ENV=production node_modules/.bin/webpack"
}
```

### Variables d'environnement

Il est bon de pratique d'avoir un fichier `.env` où vous définissez vos valeurs sensibles telles que les clés API et les identifiants de la base de données :

```json
SQL_PASSWORD=admin
STRIPE_API_KEY=1234567890
```

Une bibliothèque appelée [dotenv](https://www.npmjs.com/package/dotenv) est généralement utilisée pour charger ces variables dans notre code d'application pour consommation. Cependant, dans le contexte de Webpack, nous utiliserons [dotenv_webpack](https://www.npmjs.com/package/dotenv-webpack) pour le faire pendant la compilation et le build [comme montré ici](https://github.com/kilgarenone/boileroom/blob/master/config/webpack.common.js#L33-L37). Les variables seront alors accessibles dans l'objet `process.env` dans votre code :

```js
// payment.jsx

if (process.env.STRIPE_API_KEY) {
  // faire des trucs
}
```

### Webpack & Babel

Webpack est utilisé pour regrouper tous mes composants UI et leurs dépendances (bibliothèques npm, fichiers comme images, polices, SVG) dans des fichiers appropriés comme `.js`, `.css`, `.png`. Pendant le bundling, Webpack exécutera ma [configuration babel](https://github.com/kilgarenone/boileroom/blob/master/client/config/webpack.production.js#L19-L57), et, si nécessaire, transpilera le JavaScript que j'ai écrit en une version plus ancienne (par exemple, es5) pour supporter mes [navigateurs ciblés](https://github.com/kilgarenone/boileroom/blob/master/client/package.json#L13-L27).

Lorsque Webpack a terminé son travail, il aura généré un (ou [plusieurs](https://webpack.js.org/concepts/entry-points/#multi-page-application)) fichier `.js` et `.css`. Ensuite, en [utilisant](https://github.com/kilgarenone/boileroom/blob/master/client/config/webpack.production.js#L189-L202) un plugin webpack appelé ['html-webpack-plugin'](https://github.com/jantimon/html-webpack-plugin), les références à ces fichiers JS et CSS sont automatiquement (comportement par défaut) injectées respectivement en tant que `<script>` et `<link` dans votre `index.html`. Ensuite, lorsqu'un utilisateur demande votre application dans un navigateur, le 'index.html' est récupéré et analysé. Lorsqu'il voit `<script>` et `<link>`, il récupérera et exécutera les actifs référencés, et enfin votre application est [rendue](https://preactjs.com/guide/v10/api-reference/#render) (c'est-à-dire le rendu côté client) dans toute sa gloire à l'utilisateur.

Si vous êtes nouveau dans Webpack/Babel, je vous suggère de les apprendre à partir de leurs premiers principes pour construire lentement votre configuration au lieu de copier/coller des morceaux du web. Rien de mal à cela, mais je trouve que cela a plus de sens de le faire une fois que j'ai les modèles mentaux de comment les choses fonctionnent.

J'ai écrit sur les bases ici :

- <strong>[Webpack](https://medium.com/@kilgarenone/minimal-webpack-setup-a5f32c5f8960)</strong>

Une fois que j'ai compris les bases, j'ai commencé à [me référer à cette ressource](https://github.com/nystudio107/annotated-webpack-4-config) pour une configuration plus avancée.

- <strong>[Babel](https://medium.com/@kilgarenone/minimal-babel-setup-b12b563ee2ca)</strong>

### Performances Web

Pour faire simple, une application web qui performe bien est bonne pour vos [utilisateurs et votre entreprise](https://developers.google.com/web/fundamentals/performance/why-performance-matters).

Bien que les performances web soient un sujet vaste qui est [bien documenté](https://web.dev/fast/), j'aimerais parler de quelques-unes des choses les plus impactantes que je fais pour les performances web (à part [l'optimisation des images](https://images.guide/) qui peut représenter plus de 50% du poids d'une page).

#### Chemin de rendu critique

L'objectif d'optimiser le 'chemin de rendu critique' dans votre page est de la rendre et de la rendre interactive le plus rapidement possible pour vos utilisateurs. Faisons cela.

Nous avons mentionné précédemment que 'html-webpack-plugin' injecte automatiquement les références de tous les fichiers `.js` et `.css` générés par Webpack pour nous dans notre `index.html`. Mais nous ne voulons pas faire cela maintenant pour avoir un contrôle total sur leur placement et l'application des [indications de ressource](https://developer.mozilla.org/en-US/docs/Web/HTML/Preloading_content), tous deux étant un facteur dans l'efficacité avec laquelle un navigateur découvre et les télécharge comme chroniqué [dans cet article](https://timkadlec.com/remembers/2020-02-13-when-css-blocks/).

Maintenant, il existe des plugins Webpack [plugins](https://github.com/jantimon/html-webpack-plugin#plugins) qui semblent nous aider à cet égard, mais :

- Il n'y avait pas de moyen intuitif de contrôler l'ordre de mes `<script`. Eh bien, il y a [cette méthode](https://github.com/jantimon/html-webpack-plugin/issues/140#issuecomment-376316414), mais qu'en est-il de l'ordre parmi mes `<link>` aussi ?
- Il n'y avait pas de plugin qui `preload` mon CSS de la manière dont je le voulais comme nous le verrons plus tard. Eh bien, il y a [celui-ci](https://github.com/GoogleChrome/preload-webpack-plugin) (aucun contrôle sur les attributs), [celui-ci](https://github.com/jantimon/resource-hints-webpack-plugin) (même chose), et [celui-ci](https://github.com/numical/style-ext-html-webpack-plugin) (aucun support clair pour MiniCssExtractPlugin).

Même si j'aurais pu les bidouiller ensemble, j'aurais décidé contre en un clin d'œil si j'avais su que je pouvais le faire de manière intuitive et contrôlée. Et je l'ai fait.

Alors, allez-y et désactivez l'injection automatique :

```javascript
// webpack.production.js
plugins: [
  new HtmlWebpackPlugin({
    template: settings.templatePath,
    filename: "index.html",
    inject: false, // nous allons injecter nous-mêmes
    mode: process.env.NODE_ENV,
  }),
];
```

Et sachant que nous pouvons récupérer les actifs générés par Webpack à partir de l'objet [`htmlWebpackPlugin.files`](https://github.com/jantimon/html-webpack-plugin#writing-your-own-templates) à l'intérieur de notre `index.html` :

```json
// exemple de ce que vous verriez si vous
// console.log(htmlWebpackPlugin.files)

{
  "publicPath": "/",
  "js": [
    "/js/runtime.a201e1a.js",
    "/vendors~app.d8e8c.js",
    "/app.f8fb511.js",
    "/components.3811eb.js"
  ],
  "css": ["/app.5597.css", "/components.b49d382.css"]
}
```

Nous injectons nos actifs dans `index.html` nous-mêmes :

```html
<% if (htmlWebpackPlugin.options.mode === 'production') { %>

<script
  defer
  src="<%= htmlWebpackPlugin.files.js.filter(e => /^\/vendors/.test(e))[0] %>"
></script>
<script
  defer
  src="<%= htmlWebpackPlugin.files.js.filter(e => /^\/app/.test(e))[0] %>"
></script>
<link
  rel="stylesheet"
  href="<%= htmlWebpackPlugin.files.css.filter(e => /app/.test(e))[0] %>"
/>

<% } %>
```

Note :

- Nous ne faisons cela que lors de la construction pour la production ; nous laissons `webpack-dev-server` injecter pour nous pendant le développement local.
- Nous appliquons l'attribut `defer` sur notre `<script>` afin que le navigateur les récupère _pendant_ l'analyse de notre HTML, et n'exécute le JS qu'une fois le HTML analysé.

  <figure>
  <img src="https://i.imgur.com/cF7jPjB.png" alt="diagramme de defer" loading="lazy"/>
  <figcaption><a href="https://hacks.mozilla.org/2017/09/building-the-dom-faster-speculative-parsing-async-defer-and-preload/">source</a></figcaption>
  </figure>

#### Inlining CSS et JS

Si vous [avez réussi](https://web.dev/extract-critical-css/#overview-of-tools) à séparer votre CSS _critique_ ou si vous avez un petit script JS, vous pourriez envisager de les inliner dans `<style>` et `<script>`. 

'Inlining' signifie placer le contenu brut correspondant dans HTML. Cela économise des allers-retours réseau, bien que l'impossibilité de les mettre en cache soit une préoccupation à prendre en compte.

Inlinons le `runtime.js` généré par Webpack comme suggéré [ici](https://developers.google.com/web/fundamentals/performance/webpack/use-long-term-caching#inline_webpack_runtime_to_save_an_extra_http_request). Retour dans le `index.html` ci-dessus, ajoutez ce snippet :

```html
<!-- plus de <link> et <script> -->

<script>
  <%= compilation.assets[htmlWebpackPlugin.files.js.filter(e => /runtime/.test(e))[0].substr(htmlWebpackPlugin.files.publicPath.length)].source() %>
</script>
```

La clé était `compilation.assets[<ASSET_FILE_NAME>].source()` :

> - compilation : l'objet de compilation webpack [compilation object](https://webpack.js.org/api/compilation-object/). Cela peut être utilisé, par exemple, pour obtenir le contenu des actifs traités et les inliner directement dans la page, via `compilation.assets[...].source()` (voir [l'exemple de template inline](https://github.com/jantimon/html-webpack-plugin/blob/master/examples/inline/template.pug)). ([source](https://github.com/jantimon/html-webpack-plugin#writing-your-own-templates))

Vous pouvez utiliser cette méthode pour inliner votre CSS critique également :

```html
<style>
  <%= compilation.assets[htmlwebpackplugin.files.css.filter(e => /app/.test(e)) [0].substr(htmlWebpackPlugin.files.publicPath.length) ].source() %>
</style>
```

Pour le CSS non critique, vous pouvez envisager de le 'pré-charger'.

#### Pré-charger le CSS non critique

En bref :

```html
<link
  rel="stylesheet"
  href="/path/to/my.css"
  media="print"
  onload="this.media='all'"
/>
```

[source](https://timkadlec.com/remembers/2020-02-13-when-css-blocks/)

Mais voyons comment faire cela avec Webpack.

J'ai donc mon CSS non critique contenu dans un fichier CSS, que je spécifie comme son propre point d'entrée dans Webpack :

```javascript
// webpack.config.js
module.exports = {
  entry: {
    app: "index.js",
    components: path.resolve(__dirname, "../src/css/components.scss"),
  },
};
```

Enfin, je l'injecte au-dessus de mon CSS critique :

```html
<!-- Pré-chargement du CSS non critique -->
<link
  rel="stylesheet"
  href="<%= htmlWebpackPlugin.files.css.filter(e => /components/.test(e))[0] %>"
  media="print"
  onload="this.media='all'"
/>

<!-- CSS critique en ligne -->
<style>
  <%= compilation.assets[htmlwebpackplugin.files.css.filter(e => /app/.test(e)) [0].substr(htmlWebpackPlugin.files.publicPath.length) ].source() %>
</style>
```

Mesurons si, après tout cela, nous avons réellement fait quelque chose de bien. Mesurer la page d'inscription de Sametable [signup page](https://web.sametable.app/signup) :

**AVANT**
<img src="https://i.imgur.com/rfy7og8.png" loading="lazy"/>

**APRÈS**
<img src="https://i.imgur.com/n5llJWx.png" loading="lazy"/>

Il semble que nous avons amélioré presque toutes les métriques importantes centrées sur l'utilisateur (je ne suis pas sûr du First Input Delay..) ! ?

Voici un [bon tutoriel vidéo](https://www.youtube.com/watch?v=j9LW94EN7n4) sur la mesure des performances web dans l'outil de développement Chrome.

#### Fractionnement de code

Plutôt que de regrouper tous les composants, routes et bibliothèques tierces de votre application dans un seul fichier `.js`, vous devez les diviser et les charger à la demande en fonction de l'action d'un utilisateur au moment de l'exécution. 

Cela réduira **drastiquement** la taille du bundle de votre SPA et réduira les coûts de traitement initial de JavaScript. Cela améliore les métriques comme 'First interactive time' et 'First meaningful paint'.

Le fractionnement de code est effectué avec les ['importations dynamiques'](https://webpack.js.org/guides/code-splitting/#dynamic-imports) :

```javascript
// Editor.jsx

// CHARGEMENT PARESSEUX D'UNE BIBLIOTHÈQUE TIERCE GIGANTESQUE
componentDidMount() {
  const { default: MarkdownIt } = await import(
    /* webpackChunkName: "markdown-it" */
    "markdown-it"
  );
  new MarkdownIt({ html: true }).render(/* stuff */);
}

// OU CHARGEMENT PARESSEUX D'UN COMPOSANT BASÉ SUR L'ACTION DE L'UTILISATEUR
checkout = () => {
  const { default: CheckoutModal } = await import(
    /* webpackChunkName: "checkoutModal" */
    "../routes/CheckoutModal"
  );
}
```

Un autre cas d'utilisation pour le fractionnement de code est de **charger conditionnellement un polyfill** pour une API Web dans un navigateur qui ne la supporte pas. Cela évite aux autres qui la supportent de payer le coût du polyfill.

Par exemple, si `IntersectionObserver` n'est pas supporté, nous allons le polyfiller avec la bibliothèque ['intersection-observer'](https://www.npmjs.com/package/intersection-observer) :

```js
// InfiniteScroll.jsx

componentDidMount() {
  (window.IntersectionObserver ? Promise.resolve() : import("intersection-observer")).then(() => {
    this.io = new window.IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        // faire des trucs
      });
    }, { threshold: 0.5 });

    this.io.observe(/* DOM element */);
  });
}
```

##### Guide

- [https://medium.com/@kilgarenone/pragmatic-code-splitting-with-preact-and-webpack-a3d3b19f86a3](https://medium.com/@kilgarenone/pragmatic-code-splitting-with-preact-and-webpack-a3d3b19f86a3)

### Service différentiel

Vous avez probablement configuré votre Webpack pour construire votre application en ciblant à la fois les navigateurs modernes et anciens comme IE11, tout en servant tous les utilisateurs avec la même charge utile. Cela force ces utilisateurs qui sont sur des navigateurs modernes à payer le coût (analyse/compilation/exécution) des polyfills inutiles et des codes transformés superflus qui sont destinés à supporter les utilisateurs sur les navigateurs anciens.

Le 'service différentiel' servira, d'une part, un code beaucoup plus léger aux utilisateurs sur les navigateurs modernes. Et d'autre part, il servira un code correctement polyfillé et transformé pour supporter les utilisateurs sur les navigateurs anciens tels que IE11.

Bien que cette approche rende la configuration de build encore plus complexe et ne soit pas sans quelques [inconvénients](https://philipwalton.com/articles/deploying-es2015-code-in-production-today/#double-download-issue), les avantages obtenus (que vous pouvez trouver dans les ressources ci-dessous) l'emportent certainement sur les coûts. À moins que la majorité de votre base d'utilisateurs soit sur IE11. Dans ce cas, vous pouvez probablement sauter cela. Mais même ainsi, cette approche est future-proof car les navigateurs anciens sont en voie de disparition.

#### Dépôt

[https://github.com/kilgarenone/differential-serving](https://github.com/kilgarenone/differential-serving)

#### Ressources

- [https://jasonformat.com/modern-script-loading/#option1loaddynamically](https://jasonformat.com/modern-script-loading/#option1loaddynamically) &mdash; Un très bon aperçu des différentes approches du service différentiel. Sametable est sur l'Option-1.
- [https://github.com/firsttris/html-webpack-multi-build-plugin](https://github.com/firsttris/html-webpack-multi-build-plugin) &mdash; Ce plugin Webpack transmet le manifeste (c'est-à-dire la référence des actifs) de vos scripts modernes et hérités à 'html-webpack-plugin' afin que vous puissiez y accéder dans votre 'index.html'.
- [https://calendar.perfplanet.com/2018/doing-differential-serving-in-2019/](https://calendar.perfplanet.com/2018/doing-differential-serving-in-2019/) &mdash; J'ai appris ici à structurer ma configuration babel avec sa méthode 'babel.config.js'.
- [https://github.com/nystudio107/annotated-webpack-4-config](https://github.com/nystudio107/annotated-webpack-4-config) &mdash; J'ai appris beaucoup ici sur la structuration de mes configurations Webpack.

### Polices

Les fichiers de polices peuvent être coûteux. Prenons ma police préférée [Inter](https://rsms.me/inter/) par exemple : Si j'utilise 3 de ses styles de police, la taille totale pourrait atteindre 300 Ko, exacerbant les situations de FOUT et FOIT, en particulier sur les appareils bas de gamme.

Pour répondre à mes besoins en polices dans mes projets, j'utilise généralement les 'polices système' qui accompagnent les machines :

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
}

code {
  font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono",
    "Courier New";
}
```

Mais si vous devez utiliser des polices web personnalisées, envisagez de le faire correctement :

- Vous devriez les [héberger](https://kevq.uk/how-to-self-host-your-web-fonts/) [vous-même](https://www.tunetheweb.com/blog/should-you-self-host-google-fonts/).
- ['Sous-ensemble de polices'](https://medium.com/@kilgarenone/subsetting-your-fonts-in-windows-10-using-wsl-bae4fafa35fc) pour réduire considérablement la taille du fichier de police.
- Passez par cette [liste de contrôle](https://www.zachleat.com/web/font-checklist/).

### Icônes

Les icônes dans Sametable sont en SVG. Il existe différentes façons de procéder :

- Copiez et collez le balisage d'une icône SVG où vous en avez besoin. L'inconvénient est qu'il alourdira le HTML et entraînera des coûts d'analyse, en particulier sur mobile.
- Demandez vos icônes SVG via le réseau : `<img src="./tick.svg" />`. À moins qu'un SVG ne soit énorme (> 5 Ko), faire une demande pour chacun d'eux semble un peu excessif.
- Rendez une icône réutilisable sous la forme d'un [composant React](https://medium.com/@david.gilbertson/icons-as-react-components-de3e33cb8792). L'inconvénient est qu'il introduit inutilement du JavaScript et ses coûts associés.

Au lieu de cela, la solution que j'ai choisie pour mes icônes est '**SVG sprites**', qui est plus proche de la nature du SVG lui-même ( [`<use>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/use) et [`<symbol>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Element/symbol)).

Voyons comment.

Supposons qu'il y a de nombreux endroits qui utiliseront deux de nos icônes SVG. Dans votre `index.html` :

```html
<body>
  <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
    <symbol id="pin-it" viewBox="0 0 96 96">
      <title>Donnez-lui un titre</title>
      <desc>Donnez-lui une description pour l'accessibilité</desc>
      <path d="M67.7 40.3c-.3 2.7-2" />
    </symbol>
    <symbol id="unpin-it" viewBox="0 0 96 96">
      <title>Désépingler cette entité</title>
      <desc>Cliquez pour désépingler cette entité</desc>
      <path d="M67.7 40.3c-.3 2.7-2" />
    </symbol>
  </svg>
</body>
```

1. Masquez l'élément SVG parent `style="display: none"`.
2. Donnez à chaque symbole SVG un identifiant unique `<symbol id="unique-id"`.
3. Assurez-vous de définir le `viewBox` (généralement déjà fourni), mais sautez la `width` et la `height`.
4. Donnez-lui `title` et `desc` pour l'accessibilité.
5. Et bien sûr, les données `path` d'une icône.

Et enfin, voici comment vous pouvez les utiliser dans vos composants :

```javascript
// example.jsx

render() {
  <svg
    xmlns="http://www.w3.org/2000/svg"
    xmlnsXlink="http://www.w3.org/1999/xlink"
    width="24"
    height="24"
  >
    <use xlinkHref="#pin-it" />
  </svg>

}
```

1. Définissez la `width` et la `height` comme souhaité.
2. Spécifiez l'`id` du `<symbol>` : `<use xlinkHref="#pin-it" />`.

#### Chargement paresseux des sprites SVG

Plutôt que d'avoir vos symboles SVG dans le `index.html`, vous pouvez les mettre dans un fichier `.svg` qui n'est chargé que lorsque nécessaire :

```html
<svg xmlns="http://www.w3.org/2000/svg">
  <symbol id="header-1" viewBox="0 0 26 24">
    <title>En-tête 1</title>
    <desc>Basculer un en-tête h1</desc>
    <text x="0" y="20" font-weight="600">H1</text>
  </symbol>
  <symbol id="header-2" viewBox="0 0 26 24">
    <title>En-tête 2</title>
    <desc>Basculer un en-tête h2</desc>
    <text x="0" y="20" font-weight="600">H2</text>
  </symbol>
</svg>
```

Placez ce fichier dans `client/src/assets` :

```xml
- client
  - src
    - assets
      - svg-sprites.svg
```

Enfin, pour utiliser l'un des symboles dans le fichier :

```javascript
// Editor.js

import svgSprites from "../../assets/svg-sprites.svg";

/* composant */

render() {
  return (
    <button type="button">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        xmlnsXlink="http://www.w3.org/1999/xlink"
        width="24"
        height="24"
      >
        <use xlinkHref={`${svgSprites}#header-1`} />
      </svg>
    </button>
  )
}
```

Et un navigateur, pendant l'exécution, récupérera le fichier `.svg` s'il ne l'a pas déjà fait.

Et voilà ! Plus besoin de coller ces longues données `path` partout.

#### Sources d'icônes

- [https://material.io/resources/icons/?style=baseline](https://material.io/resources/icons/?style=baseline)
- [https://logomakr.com/](https://logomakr.com/)
- [https://github.com/wmira/react-icons-kit#bundled-icon-sets](https://github.com/wmira/react-icons-kit#bundled-icon-sets) (a une belle liste de sources)

#### Références

- [https://css-tricks.com/mega-list-svg-information/#svg-icons](https://css-tricks.com/mega-list-svg-information/#svg-icons)

### Favicon

Si je n'avais pas désactivé l'option `inject` de 'html-webpack-plugin', j'aurais utilisé un plugin appelé ['favicons-webpack-plugin'](https://github.com/jantimon/favicons-webpack-plugin) qui génère automatiquement tous les types de favicons (attention - il y en a beaucoup !), et les injecte dans mon `index.html` :

```javascript
// webpack.config.js

plugins: [
  new HtmlWebpackPlugin(), // 'inject' est vrai par défaut
  // doit venir après html-webpack-plugin
  new FaviconsWebpackPlugin({
    logo: path.resolve(__dirname, "../src/assets/logo.svg"),
    prefix: "icons-[hash]/",
    persistentCache: true,
    inject: true,
    favicons: {
      appName: "Sametable",
      appDescription: "Gérez vos tâches dans des feuilles de calcul",
      developerName: "Kheoh Yee Wei",
      developerURL: "https://kheohyeewei.com", // empêcher la récupération depuis le package.json le plus proche
      theme_color: "#fcbdaa",
      // spécifiez les fournisseurs pour lesquels vous voulez une favicon
      icons: {
        coast: false,
        yandex: false,
      },
    },
  }),
];
```

Mais puisque j'ai désactivé l'injection automatique, voici comment je gère ma favicon :

1. Allez sur [https://realfavicongenerator.net/](https://realfavicongenerator.net/)

   - Fournissez votre logo au format SVG.
   - Sélectionnez l'option 'Version/Actualiser' pour activer le cache-busting de votre favicon dans le navigateur de vos utilisateurs.
   - Suivez les instructions à la fin. Vous pouvez stocker vos favicons dans n'importe quel dossier de votre projet.

2. Utilisez ['copy-webpack-plugin'](https://webpack.js.org/plugins/copy-webpack-plugin/) pour copier tous vos actifs de favicon générés à l'étape 1, du dossier où vous les stockez (dans mon cas, `src/assets/favicon`) vers le [chemin](https://github.com/kilgarenone/boileroom/blob/master/client/config/webpack.production.js#L140) de sortie de Webpack ([comportement par défaut](https://github.com/webpack-contrib/copy-webpack-plugin#to)), afin qu'ils soient accessibles depuis la racine (c'est-à-dire https://example.com/favicon.ico).

   ```javascript
   // webpack.config.js
   const CopyWebpackPlugin = require("copy-webpack-plugin");

   plugins: [new CopyWebpackPlugin([{ from: "src/assets/favicon" }])];
   ```

Et c'est tout !

### Appels API

Un client doit communiquer avec un serveur pour effectuer des opérations 'CRUD' - Create, Read, Update, et Delete :

<img src="https://i.imgur.com/VjAWItp.png" alt="diagramme de communication client-serveur" loading="lazy"/>

Voici mon `api.js` que j'espère facile à comprendre :

<details>
  <summary>API WRAPPER</summary>

```javascript
import { route } from "preact-router";

function checkStatus(response) {
  const responseCode = response.status;

  if (responseCode >= 200 && responseCode < 300) {
    return response;
  }

  // gérer le scénario où l'utilisateur n'est pas autorisé
  if (responseCode === 401) {
    response
      .json()
      .then((json) =>
        route(`/signin${json.refererUri ? `?dest=${json.refererUri}` : ""}`)
      );
    return;
  }

  // transmettre la réponse d'erreur au bloc 'catch' de votre bloc try & catch async/await
  return response.json().then((json) => {
    return Promise.reject({
      status: responseCode,
      ok: false,
      statusText: response.statusText,
      body: json,
    });
  });
}

function handleError(error) {
  error.response = {
    status: 0,
    statusText:
      "Impossible de se connecter. Veuillez vous assurer que vous êtes connecté à Internet.",
  };
  throw error;
}

function parseJSON(response) {
  if (response.status === 204 || response.status === 205) {
    return null;
  }
  return response.json();
}

function request(url, options) {
  return fetch(url, options)
    .catch(handleError) // gérer les problèmes de réseau
    .then(checkStatus)
    .then(parseJSON)
    .catch((e) => {
      throw e;
    });
}

export function api(endPoint, userOptions = {}) {
  const url = process.env.API_BASE_URL + endPoint;

  // pour transmettre notre cookie d'authentification au serveur
  userOptions.credentials = "include";

  const defaultHeaders = {
    "Content-Type": "application/json",
    Accept: "application/json",
  };

  if (userOptions.body instanceof File) {
    const formData = new FormData();
    formData.append("file", userOptions.body);
    userOptions.body = formData;
    // laisser le navigateur définir le content-type en multipart/etc.
    delete defaultHeaders["Content-Type"];
  }

  if (userOptions.body instanceof FormData) {
    // laisser le navigateur définir le content-type en multipart
    delete defaultHeaders["Content-Type"];
  }

  const options = {
    ...userOptions,
    headers: {
      ...defaultHeaders,
      ...userOptions.headers,
    },
  };

  return request(url, options);
}
```

</details>

Il n'y a presque rien de nouveau à apprendre pour commencer à utiliser ce module API si vous avez déjà utilisé le [`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) natif.

#### Utilisation

```javascript
// Home.jsx
import { api } from "../lib/api";

async componentDidMount() {
  try {
    // POST-ing data
    const response = await api(
      '/projects/save/121212121',
      {
        method: 'PUT',
        body: JSON.stringify(dataObject)
      }
    )

    // ou GET-ting data
    const { myWorkspaces } = await api('/users/home');

  } catch (err) {
    // gérer Promise.reject passé depuis api.js
  }
}
```

Mais si vous préférez utiliser une bibliothèque pour gérer vos appels HTTP, je recommande ['redaxios'](https://github.com/developit/redaxios). Il partage non seulement une API avec le populaire [axios](https://www.npmjs.com/package/axios), mais il est aussi beaucoup plus léger.

### Tester la version de production localement

Je construis toujours mon application cliente localement pour la tester et la mesurer dans mon navigateur avant de la déployer sur le cloud.

J'ai un script npm (`npm run test-build`) dans le `package.json` du dossier 'client' qui construira et servira sur un serveur web local. De cette façon, je peux jouer avec dans mon navigateur à l'adresse http://localhost:5000 :

```json
"scripts": {
    "test-build": "cross-env NODE_ENV=production TEST_RUN=true node_modules/.bin/webpack && npm run serve",
    "serve": "ws --spa index.html --directory dist --port 5000 --hostname localhost"
  }
```

L'application est servie en utilisant un outil appelé ['local-web-server'](https://www.npmjs.com/package/local-web-server). C'est jusqu'à présent le seul que j'ai trouvé qui fonctionne parfaitement pour une SPA.

### Sécurité

Envisagez d'ajouter les en-têtes de sécurité [CSP](https://developers.google.com/web/fundamentals/security/csp/).

Pour ajouter des en-têtes dans firebase : [https://firebase.google.com/docs/hosting/full-config#headers](https://firebase.google.com/docs/hosting/full-config#headers)

Exemple d'en-têtes CSP dans votre `firebase.json` :

```json
{
  "source": "**",
  "headers": [
    {
      "key": "Strict-Transport-Security",
      "value": "max-age=63072000; includeSubdomains; preload"
    },
    {
      "key": "Content-Security-Policy",
      "value": "default-src 'none'; img-src 'self'; script-src 'self'; style-src 'self'; object-src 'none'"
    },
    { "key": "X-Content-Type-Options", "value": "nosniff" },
    { "key": "X-Frame-Options", "value": "DENY" },
    { "key": "X-XSS-Protection", "value": "1; mode=block" },
    { "key": "Referrer-Policy", "value": "same-origin" }
  ]
}
```

Si vous utilisez Stripe, assurez-vous d'ajouter également leurs directives CSP :
[https://stripe.com/docs/security/guide#content-security-policy](https://stripe.com/docs/security/guide#content-security-policy)

Enfin, assurez-vous d'obtenir un **A** [ici](https://observatory.mozilla.org/) et tapez-vous sur l'épaule !

## Design

Avant de commencer à coder quoi que ce soit, je voulais avoir une bobine mentale de la manière dont je voulais **intégrer** un nouvel utilisateur à mon application. Ensuite, je ferais des croquis sur un carnet de ce à quoi cela pourrait ressembler, et je réitérerais les croquis en jouant et en révisant la bobine dans ma tête. 

Pour mon tout premier 'sprint', je construirais principalement un 'cadre UI/UX' sur lequel j'ajouterais des pièces au fil du temps. Cependant, il est important de se rappeler que chaque décision que vous prenez pendant ce processus doit être ouverte et facile à annuler. 
    
De cette façon, une décision 'petite'&mdash; mais prudente&mdash;ne signera pas votre perte lorsque vous vous laisserez emporter par des convictions trop confiantes et romantiques.

Je ne suis pas sûr que cela ait du sens, mais explorons quelques concepts qui ont aidé à structurer mon design pour qu'il soit cohérent en pratique.

### Échelles modulaires

Votre design aura plus de sens pour vos utilisateurs lorsqu'il s'écoulera selon une 'échelle modulaire'. Cette échelle doit spécifier une échelle d'espaces ou de tailles qui augmentent chacune avec un certain ratio.

<figure>
<img src="https://i.imgur.com/WWl6KuB.png" loading="lazy" alt="illustration de l'échelle modulaire" />
<figcaption><em>Figure : Échelle modulaire</em></figcaption>
</figure>

Une façon de créer une échelle est avec les ['Propriétés Personnalisées'](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_custom_properties) CSS (crédits à view-source [every-layout.dev](https://every-layout.dev/)) :

```css
:root {
  --ratio: 1.414;
  --s-3: calc(var(--s0) / var(--ratio) / var(--ratio) / var(--ratio));
  --s-2: calc(var(--s0) / var(--ratio) / var(--ratio));
  --s-1: calc(var(--s0) / var(--ratio));
  --s0: 1rem;
  --s1: calc(var(--s0) * var(--ratio));
  --s2: calc(var(--s0) * var(--ratio) * var(--ratio));
  --s3: calc(var(--s0) * var(--ratio) * var(--ratio) * var(--ratio));
}
```

Si vous ne savez pas quelle échelle utiliser, choisissez simplement une [échelle](https://www.modularscale.com/) qui correspond le mieux à votre design et **restez-y**.

Ensuite, créez un ensemble de classes utilitaires, chacune associée à une échelle, dans un fichier appelé `spacing.scss`. Je les utiliserai pour espacer mes éléments UI dans un projet :

```css
.mb-1 {
  margin-bottom: var(--s1);
}
.mb-2 {
  margin-bottom: var(--s2);
}
.mr-1 {
  margin-right: var(--s1);
}
.mr--1 {
  margin-right: var(--s-1);
}
```

Remarquez que j'essaie de définir l'espacement uniquement dans les directions `right` et `bottom` comme [suggéré ici](https://csswizardry.com/2012/06/single-direction-margin-declarations/).

Dans mon expérience, il est préférable de ne pas intégrer de définitions d'espacement dans vos composants UI :

**NE PAS FAIRE**

```javascript
// Button.scss
.btn {
  margin: 10px; // un espacement par défaut ; ennuyeux dans la plupart des cas
  font-style: normal;
  border: 0;
  background-color: transparent;
}

// Button.jsx
import s from './Button.scss';

export function Button({children, ...props}) {
  return (
    <button class={s.btn} {...props}>{children}</button>
  )
}

// Utilisation
<Button />
```

**FAIRE**

```javascript
// Button.scss
.btn {
  font-style: normal;
  border: 0;
  background-color: transparent;
}

// Button.jsx
import s from './Button.scss';

export function Button({children, className, ...props}) {
  return (
    <button class={`${s.btn} ${className}`} {...props}>{children}</button>
  )
}

// Utilisation
// Passez vos classes utilitaires d'espacement lors de la construction de vos pages
<Button className="mr-1 pb-1">Sign Up</Button>
```

### Couleurs

Il existe de nombreux outils de palette de couleurs. Mais celui de [Material](https://material.io/design/color/the-color-system.html#tools-for-picking-colors) est celui que j'utilise toujours pour mes couleurs simplement parce qu'elles sont présentées dans toute leur gloire ! ?

Ensuite, je les définis comme des propriétés personnalisées CSS :

```css
:root {
  --black-100: #0b0c0c;
  --black-80: #424242;
  --black-60: #555759;
  --black-50: #626a6e;

  font-size: 105%;
  color: var(--black-100);
}
```

### Remise à zéro CSS

Le but d'une 'remise à zéro CSS' est de supprimer le style par défaut des navigateurs courants.

Il existe plusieurs de ces outils. Attention, certains peuvent être assez opiniâtres et potentiellement vous donner plus de maux de tête qu'ils n'en valent. En voici un populaire : [https://meyerweb.com/eric/tools/css/reset/reset.css](https://meyerweb.com/eric/tools/css/reset/reset.css)

Voici le mien :

```css
*,
*::before,
*::after {
  box-sizing: border-box;
  overflow-wrap: break-word;
  margin: 0;
  padding: 0;
  border: 0 solid;
  font-family: inherit;
  color: inherit;
}

/* Définir les valeurs par défaut du corps */
body {
  scroll-behavior: smooth;
  text-rendering: optimizeLegibility;
}

/* Rendre les images plus faciles à utiliser */
img {
  max-width: 100%;
}

/* Hériter des polices pour les inputs et les boutons */
button,
input,
textarea,
select {
  color: inherit;
  font: inherit;
}
```

Vous pourriez également envisager d'utiliser [postcss-normalize](https://github.com/csstools/postcss-normalize) qui en génère un selon vos navigateurs ciblés.

### Une pratique de styling

J'essaie toujours de styliser au niveau de la **balise** d'abord avant de sortir l'artillerie lourde si nécessaire, dans mon cas, ['CSS Modules'](https://github.com/css-modules/css-modules), pour encapsuler les styles par composant :

```xml
- src
  - routes
    - SignIn
      - SignIn.js
      - SignIn.scss
```

Le `SignIn.scss` contient le CSS qui concerne uniquement le composant `<SignIn />`.

De plus, je n'utilise pas les bibliothèques CSS populaires dans l'écosystème React telles que 'styled-components' et 'emotion'. J'essaie d'**utiliser du HTML et du CSS purs chaque fois que je le peux, et de ne laisser Preact gérer que les mises à jour du DOM et de l'état** pour moi.

Par exemple, pour l'élément `<input/>` :

```css
// index.scss

label {
  display: block;
  color: var(--black-100);
  font-weight: 600;
}

input {
  width: 100%;
  font-weight: 400;
  font-style: normal;
  border: 2px solid var(--black-100);
  box-shadow: none;
  outline: none;
  appearance: none;
}

input:focus {
  box-shadow: inset 0 0 0 2px;
  outline: 3px solid #fd0;
  outline-offset: 0;
}
```

Puis l'utiliser dans un fichier JSX avec sa balise vanilla :

```javascript
// SignIn.js

render() {
  return (
    <div class="form-control">
      <label htmlFor="email">
        Email&nbsp;
        <strong>
          <abbr title="Ce champ est obligatoire">*</abbr>
        </strong>
      </label>
      <input
        required
        value={this.email}
        type="email"
        id="email"
        name="email"
        placeholder="e.g. sara@widgetco.com"
      />
    </div>
  )
}
```

### Mise en page

J'utilise **CSS Flexbox** pour les travaux de mise en page dans Sametable. Je n'avais pas besoin de frameworks CSS. Apprenez CSS Flexbox à partir de ses premiers principes pour faire plus avec moins de code. De plus, dans de nombreux cas, le résultat sera déjà réactif grâce aux algorithmes de mise en page, économisant ces requêtes `@media`.

Voyons comment construire une mise en page courante en Flexbox avec une quantité minimale de CSS :

<img src="https://i.imgur.com/PTCrd0K.png" alt="mise en page de la barre latérale et du contenu" loading="lazy"/>

<p class="codepen" data-height="265" data-theme-id="light" data-default-tab="css,result" data-user="kilgarenone" data-slug-hash="mdeLwvx" data-preview="true" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Sidebar/Content layout">
  <span>Voir le Pen <a href="https://codepen.io/kilgarenone/pen/mdeLwvx">
  Sidebar/Content layout</a>
  sur <a href="https://codepen.io">CodePen</a>.</span>
</p>

#### Ressources

- [Flexbox froggy](https://flexboxfroggy.com/)
- [Tout ce que vous devez savoir sur flexbox](https://www.freecodecamp.org/news/understanding-flexbox-everything-you-need-to-know-b4013d4dc9af/)

## Serveur

```json
- server
  - server.js
  - package.json
  - .env
```

Le [serveur](https://github.com/kilgarenone/boileroom/tree/master/server) fonctionne sur NodeJS (framework ExpressJS) pour servir tous mes points de terminaison **API**.

```javascript
// Exemple de point de terminaison : https://example.com/api/tasks/save/12345
router.put("/save/:taskId", (req, res, next) => {});
```

Le [`server.js`](https://github.com/kilgarenone/boileroom/blob/master/server/server.js) contient les codes [familiers](https://expressjs.com/en/starter/hello-world.html) pour démarrer un serveur Nodejs.

### Structure des fichiers

Je suis reconnaissant pour ce guide [digeste](https://node-postgres.com/guides/project-structure) sur la structure du projet, qui m'a permis de me concentrer et de construire rapidement mon API.

### Script Npm (Serveur)

Dans le `package.json` à l'intérieur du dossier 'server', il y a un script npm qui démarrera votre serveur pour vous :

```json
"scripts": {
  "dev": "nodemon -r dotenv/config server.js",
  "start": "node server.js"
}
```

- Le script `dev` ['pré-charge'](https://www.npmjs.com/package/dotenv#preload) dotenv comme suggéré [ici](https://medium.com/the-node-js-collection/making-your-node-js-work-everywhere-with-environment-variables-2da8cdf6e786#b1af). Et c'est tout&mdash; Vous aurez accès aux variables d'environnement définies dans le fichier `.env` à partir de l'objet `process.env`.

- Le script `start` est utilisé pour démarrer notre serveur Nodejs en production. Dans mon cas, GCP exécutera ce script pour démarrer mon Nodejs.

### Base de données

J'utilise **Postgresql** comme base de données. Ensuite, j'utilise la bibliothèque ['node-postgres'](https://node-postgres.com/)(a.k.a `pg`) pour connecter mon Nodejs à la base de données. Une fois cela fait, je peux effectuer des opérations CRUD entre mes points de terminaison API et la base de données.

#### Configuration

Pour le développement local :

1. Téléchargez [Postgresql ici](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads). Obtenez la dernière version. Laissez tout comme c'est. Rappelez-vous le mot de passe que vous avez défini. Ensuite,

   - Ouvrez 'pgAdmin'. C'est une application navigateur.
   - Créez une base de données pour votre application :
     <img src="https://i.imgur.com/trcAaSi.png" loading="lazy"/>

2. Définissez un ensemble de variables d'environnement dans le fichier `.env` :

   ```json
   DB_HOST='localhost'
   DB_USER=postgres
   DB_NAME=<YOUR_CUSTOM_DATABASE_NAME_HERE>
   DB_PASSWORD=<YOUR_MASTER_PASSWORD>
   DB_PORT=5432
   ```

3. Ensuite, nous allons [connecter](https://node-postgres.com/features/connecting) un nouveau client via un [pool de connexions](https://node-postgres.com/features/pooling) à notre base de données Postgresql depuis notre Nodejs. Je le fais dans `server/db/index.js` :

   <a href="#db-wrapper" id="db-wrapper">#</a>

   ```javascript
   const { Pool } = require("pg");

   const pool = new Pool({
     user: process.env.DB_USER,
     host: process.env.DB_HOST,
     port: process.env.DB_PORT,
     database: process.env.DB_NAME,
     password: process.env.DB_PASSWORD,
   });

   // TRANSACTION
   // https://github.com/brianc/node-postgres/issues/1252#issuecomment-293899088
   const tx = async (callback, errCallback) => {
     const client = await pool.connect();
     try {
       await client.query("BEGIN");
       await callback(client);
       await client.query("COMMIT");
     } catch (err) {
       console.log(("DB ERROR:", err));
       await client.query("ROLLBACK");
       errCallback && errCallback(err);
     } finally {
       client.release();
     }
   };
   // le pool émettra une erreur au nom de tout client inactif
   // qu'il contient si une erreur de backend ou une partition réseau se produit
   pool.on("error", (err) => {
     process.exit(-1);
   });

   pool.on("connect", () => {
     console.log("❤️ Connexion à la base de données ❤️");
   });

   module.exports = {
     query: (text, params, callback) => pool.query(text, params, callback),
     tx,
     pool,
   };
   ```

   - J'utiliserai la fonction `tx` dans une API si je dois appeler **plusieurs** requêtes qui dépendent les unes des autres.
   - Si je fais une **seule** requête, j'utiliserai la fonction `query`.

Et c'est tout ! Maintenant, vous avez une base de données avec laquelle travailler pour votre développement local ?

#### Utilisation

Je vais avouer : J'ai **conçu à la main** toutes les requêtes pour Sametable.

À mon avis, SQL est déjà un langage déclaratif qui n'a pas besoin d'abstraction supplémentaire&mdash;il est facile à lire, à comprendre et à écrire. Il peut être maintenable si vous séparez bien vos points de terminaison API. 
    
Si vous saviez que vous construisiez une application à l'échelle de Facebook, il serait peut-être judicieux d'utiliser un ORM. Mais je suis juste un [gars normal de tous les jours](https://www.youtube.com/watch?v=5PsnxDQvQpw) qui construit un SaaS très étroitement défini tout seul. 
    
Donc, je devais éviter les frais généraux et la complexité tout en tenant compte de facteurs tels que la facilité d'intégration, les performances, la facilité de réitération et la durée de vie potentielle des connaissances. 

Cela me rappelle qu'on m'a incité à apprendre le JavaScript vanilla avant de sauter sur le train d'un framework front-end populaire. Parce que vous pourriez vous rendre compte : C'est tout ce dont vous avez besoin pour ce que vous avez entrepris d'accomplir pour atteindre votre 1000ème client.

Pour être honnête, cependant, lorsque j'ai décidé de suivre cette voie, j'avais des expériences modestes en écriture MySQL. Donc, si vous ne savez rien de SQL et que vous êtes pressé de le livrer, vous pourriez envisager une bibliothèque comme [knex.js](http://knexjs.org/).

##### Exemple

```javascript
// server/routes/projects.js

const express = require("express");
const asyncHandler = require("express-async-handler");
const db = require("../db");

const router = express.Router();

module.exports = router;

// [POST] api/projects/create
router.post(
  "/create",
  express.json(),
  asyncHandler(async (req, res, next) => {
    const { title, project_id } = req.body;

    db.tx(async (client) => {
      const {
        rows,
      } = await client.query(
        `INSERT INTO tasks (title) VALUES ($1) RETURNING mask_id(task_id) as masked_task_id, task_id`,
        [title]
      );

      res.json({ id: rows[0].masked_task_id });
    }, next);
  })
);
```

- Le [`express-async-handler`](https://github.com/Abazhenov/express-async-handler/blob/master/index.js) est principalement utilisé pour gérer les erreurs async dans mes gestionnaires de routes. Il ne sera plus nécessaire lorsque Express 5 sortira.

* Importez le module `db` pour utiliser la méthode `tx`. Passez vos requêtes SQL conçues à la main et [paramètres](https://node-postgres.com/features/queries).

C'est tout !

### Création de schémas de tables

Avant de pouvoir commencer à interroger une base de données, vous devez créer des tables. Chaque table contient des informations sur une entité. 
    
Mais nous ne regroupons pas toutes les informations sur une entité dans la même table. Nous devons organiser les informations de manière à promouvoir les performances des requêtes et la maintenabilité des données. Et ce qui m'a aidé dans cet exercice est un concept appelé [**dénormalisation**](https://firebase.google.com/docs/database/web/structure-data). 
    
Comme mentionné, nous ne voulons pas stocker toutes les informations sur une entité dans la même table. Par exemple, disons, nous avons une table `users` stockant `fullname`, `password` et `email`. C'est bien jusqu'à présent. 
    
Mais le problème survient lorsque nous stockons également les identifiants de tous les projets attribués à un utilisateur particulier dans une colonne séparée de la même table. Au lieu de cela, je vais les diviser en tables séparées :

1. Créez la table `users`. Remarquez qu'elle ne stocke aucune donnée liée aux 'projects' :

   ```sql
   CREATE TABLE users(
     user_id BIGSERIAL PRIMARY KEY,
     fullname TEXT NOT NULL,
     pwd TEXT NOT NULL,
     email TEXT UNIQUE NOT NULL,
   );
   ```

2. Créez une table `projects` pour stocker les données uniquement sur les détails d'un projet :

   ```sql
   CREATE TABLE projects(
     project_id BIGSERIAL PRIMARY KEY,
     title TEXT,
     content TEXT,
     due_date TIMESTAMPTZ,
     status SMALLINT,
     created_on TIMESTAMPTZ NOT NULL DEFAULT now()
   );
   ```

3. Créez une table 'bridge' sur les propriétés des projets en associant l'ID d'un utilisateur avec l'ID d'un projet qu'il possède :

   ```sql
   CREATE TABLE project_ownerships(
     project_id BIGINT REFERENCES projects ON DELETE CASCADE,
     user_id BIGINT REFERENCES users ON DELETE CASCADE,
     PRIMARY KEY (project_id, user_id),
     CONSTRAINT project_user_unique UNIQUE (user_id, project_id)
   );
   ```

4. Enfin, pour obtenir tous les projets qui sont attribués à un utilisateur particulier, nous ferons ce que les bases de données relationnelles font de mieux : [`join`](https://www.postgresqltutorial.com/postgresql-joins/).

Je mettrai tous mes schémas dans un fichier `.sql` à la racine de mon projet <a href="#schemas-file" id="schemas-file">#</a> :

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE users(
  user_id BIGSERIAL PRIMARY KEY,
  fullname TEXT NOT NULL,
  pwd TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  created_on TIMESTAMPTZ NOT NULL DEFAULT now()
);
```

Ensuite, je copierai, collerai et exécuterai dans pgAdmin :

<img src="https://i.imgur.com/gm9YFZF.png" alt="créer des schémas de table dans pgadmin" loading="lazy" />

Il ne fait aucun doute qu'il existe des moyens plus avancés de faire cela, donc c'est à vous de voir si vous voulez explorer ce que vous aimez.

### Suppression d'une base de données

Supprimer une base de données entière pour commencer avec un nouvel ensemble de schémas était quelque chose que j'ai dû faire très souvent au début.

Le truc est : Eh bien, vous copiez, collez et exécutez la commande ci-dessous dans l'éditeur de requêtes de la base de données dans pgAdmin :

```sql
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO public;
COMMENT ON SCHEMA public IS 'standard public schema';
```

### Conception de requêtes SQL

J'écris mes requêtes SQL dans **pgAdmin** pour obtenir les données que je veux à partir d'un point de terminaison API.

Pour donner une direction à cela dans pgAdmin :
<img src="https://i.imgur.com/54tIRzc.png" alt="écriture de requêtes SQL dans l'éditeur pgadmin" loading="lazy" />

#### Expressions de Table Commun (CTEs)

Je suis tombé sur un motif appelé [**CTEs**](https://www.postgresql.org/docs/9.1/queries-with.html) lorsque j'explorais comment j'allais obtenir les données que je voulais à partir de tables disparates et les structurer comme je le souhaitais, sans faire beaucoup de requêtes de base de données séparées et de boucles for.

Le fonctionnement des CTE est assez simple, même s'il semble intimidant : Vous écrivez vos requêtes. Chaque requête reçoit un nom d'alias (`q`, `q1`, `q3`). Et une requête suivante peut accéder aux résultats de toute requête précédente par leur nom d'alias (`q1.workspace_id`) :

```sql
WITH q AS (SELECT * FROM projects_tasks WHERE task_id=$1)
, q1 AS (SELECT wp.workspace_id, wp.project_id, q.task_id FROM workspaces_projects wp, q WHERE wp.project_id = q.project_id)
, q3 AS (SELECT q1.workspace_id AS workspace_id, wp.name AS workspace_title, mask_id(q1.project_id) AS project_id, p.title AS project_title, mask_id(t.task_id) AS task_id, t.title, t.content, t.due_date, t.priority, t.status)

SELECT * FROM q3;
```

Presque toutes les requêtes dans Sametable sont écrites de cette manière.

### Redis

Redis est une base de données NoSQL qui stocke les données en mémoire. Dans Sametable, j'ai utilisé Redis pour deux objectifs :

1. Stocker les données de session d'un utilisateur et les informations de base de la table `users`&mdash;nom, email, et un drapeau qui indique si l'utilisateur est un abonné ou non&mdash;une fois qu'ils se sont connectés.
2. Mettre en cache les résultats de certaines de mes requêtes Postgresql pour éviter d'avoir à interroger la base de données si le cache est encore frais.

#### Installation

Je suis sur une machine Windows 10 avec le sous-système Windows pour Linux (WSL) installé. C'est le seul guide que j'ai suivi pour installer Redis sur ma machine :

[https://redislabs.com/blog/redis-on-windows-10/](https://redislabs.com/blog/redis-on-windows-10/)

Suivez le guide pour installer WSL si vous ne l'avez pas déjà.

Ensuite, je vais démarrer mon serveur Redis local dans le bash WSL :

1. Appuyez sur <kbd>Win</kbd> + <kbd>R</kbd>.
2. Tapez `bash` et entrez.
3. Dans le terminal, exécutez `sudo service redis-server start`

Maintenant, installez le package npm [`redis`](https://www.npmjs.com/package/redis) :

```json
cd server

npm i redis
```

Assurez-vous de l'installer dans le `package.json` du `server`, d'où le `cd server`.

Ensuite, je crée un fichier nommé `redis.js` sous `server/db` :

```javascript
// server/db/redis.js

const redis = require("redis");
const { promisify } = require("util");

const redisClient = redis.createClient(
  NODE_ENV === "production"
    ? {
        host: process.env.REDISHOST,
        no_ready_check: true,
        auth_pass: process.env.REDIS_PASSWORD,
      }
    : {}
);

redisClient.on("error", (err) => console.error("ERR:REDIS:", err));

const redisGetAsync = promisify(redisClient.get).bind(redisClient);
const redisSetExAsync = promisify(redisClient.setex).bind(redisClient);
const redisDelAsync = promisify(redisClient.del).bind(redisClient);

// Expiration de 1 jour
const REDIS_EXPIRATION = 7 * 86400; // secondes

module.exports = {
  redisGetAsync,
  redisSetExAsync,
  redisDelAsync,
  REDIS_EXPIRATION,
  redisClient,
};
```

- Par [défaut](https://www.npmjs.com/package/redis#options-object-properties), `node-redis` se connectera à `localhost` au port `6379`. Mais ce ne sera peut-être pas le cas en production si vous hébergez votre Redis dans une VM. Je fournis donc cet objet si c'est en mode production :

  ```js
  {
     host: process.env.REDISHOST,
     no_ready_check: true,
     auth_pass: process.env.REDIS_PASSWORD,
   }
  ```

  - TBH, je ne suis pas tout à fait sûr du `no_ready_check`. Je l'ai obtenu de ce tutoriel officiel [tutoriel](https://docs.redislabs.com/latest/rs/references/client_references/client_nodejs/).
  - Le `auth_pass` et `host` sont fournis comme personnalisés puisque j'héberge mon Redis dans une VM GCE où j'ai défini un mot de passe sur mon Redis.

* J'ai [promisifié](https://www.npmjs.com/package/redis#promises) les méthodes Redis que j'utiliserai pour les rendre asynchrones afin d'éviter de bloquer le thread unique de NodeJS.

Et maintenant vous avez Redis pour votre développement local !

### Gestion des erreurs & Journalisation

#### Gestion des erreurs

La gestion des erreurs dans Nodejs a un paradigme que nous allons explorer dans 3 contextes différents.

Pour poser le décor, nous avons besoin de deux choses en place d'abord :

1. Un package npm appelé [http-errors](https://www.npmjs.com/package/http-errors) qui nous donnera une structure de données d'erreur standard à utiliser, surtout côté client.

   ```json
   npm install http-errors
   ```

2. Nous créons un gestionnaire d'erreurs personnalisé au niveau global pour capturer **toutes** les erreurs propagées depuis les routes ou les blocs `catch` via `next(err)` :

   ```javascript
   // app.js
   const express = require("express");
   const app = express();
   const createError = require("http-errors");

   // notre gestionnaire d'erreurs personnalisé central
   // NOTE : NE RETIREZ PAS le 'next' même si eslint se plaint qu'il n'est pas utilisé !!!
   app.use(function (err, req, res, next) {
     // les erreurs enveloppées par http-errors auront la propriété 'status' définie. Sinon, c'est une erreur inattendue générique
     const error = err.status
       ? err
       : createError(500, "Something went wrong. Notified dev.");

     res.status(error.status).json(error);
   });
   ```

   Comme vous le verrez, le schéma général de la gestion des erreurs dans Nodejs tourne autour de la chaîne de 'middleware' et du paramètre `next` :

   > Les appels à next() et next(err) indiquent que le gestionnaire actuel est terminé et dans quel état. next(err) ignorera tous les gestionnaires restants dans la chaîne sauf ceux qui sont configurés pour gérer les erreurs . . . [source](https://expressjs.com/en/guide/error-handling.html)

   Notez que bien que ce soit un schéma courant de gestion des erreurs dans Express, vous pourriez envisager une [autre méthode](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/errorhandling/centralizedhandling.md) qui est, cependant, plus compliquée.

##### Gérer les erreurs de validation des entrées

C'est une [bonne pratique](https://github.com/goldbergyoni/nodebestpractices#-610-validate-incoming-json-schemas) de valider les entrées de l'utilisateur à la fois côté client et côté serveur. 
    
Côté serveur, j'utilise une bibliothèque appelée ['express-validator'](https://express-validator.github.io/docs/) pour faire le travail. Si une entrée est invalide, je la gérerai en répondant avec un code HTTP et un message d'erreur pour informer l'utilisateur.

Par exemple, lorsqu'un email fourni par un utilisateur est invalide, nous quitterons tôt en créant un objet d'erreur avec la bibliothèque 'http-errors', puis nous le passerons à la fonction `next` :

```javascript
const { body, validationResult } = require("express-validator");

router.post(
  "/login",
  upload.none(),
  [body("email", "Format d'email invalide").isEmail()],
  asyncHandler(async (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return next(createError(422, errors.mapped()));
    }

    res.json({});
  })
);
```

La réponse suivante sera envoyée au client :

```json
{
  "message": "Entité non traitée",
  "email": {
    "value": "hello@mail.com232",
    "msg": "Format d'email invalide",
    "param": "email",
    "location": "body"
  }
}
```

Ensuite, c'est à vous de décider ce que vous voulez en faire. Par exemple, vous pouvez accéder à la propriété `email.msg` pour afficher le message d'erreur sous le champ de saisie de l'email.

##### Gérer les erreurs de la logique métier

Supposons que nous avons une situation où un utilisateur a saisi un email qui n'existe pas dans la base de données. Dans ce cas, nous devons dire à l'utilisateur de réessayer :

```javascript
router.post(
  "/login",
  upload.none(),
  asyncHandler(async (req, res, next) => {
    const { email, password } = req.body;

    const { rowCount } = await db.query(
      `SELECT * FROM users WHERE email=($1)`,
      [email]
    );

    if (rowCount === 0) {
      // émettre une erreur avec un message générique
      return next(
        createError(422, "Veuillez entrer un email et un mot de passe corrects")
      );
    }

    res.json({});
  })
);
```

Rappelez-vous, tout objet d'erreur passé à 'next'(`next(err)`) sera capturé par le gestionnaire d'erreurs personnalisé que nous avons défini ci-dessus.

##### Gérer les erreurs inattendues de la base de données

Je passe le paramètre `next` de mon gestionnaire de route à ma fonction wrapper de <a href="#db-wrapper">transaction</a> de ma base de données pour gérer toute erreur inattendue.

```javascript
router.post(
  "/invite",
  async (req, res, next) => {
    db.tx(async (client) => {
          const {
            rows,
            rowCount,
          } = await client.query(
            `SELECT mask_id(user_id) AS user_id, status FROM users WHERE users.email=$1`,
            [email]
          );
    }, next)
)
```

#### Journalisation

Lorsqu'une erreur se produit, il est courant de 1) la journaliser dans un système pour les enregistrements, et 2) de vous notifier automatiquement à ce sujet.

Il existe de nombreux outils dans ce domaine. Mais j'ai fini par en utiliser deux :

- [**Sentry**](https://sentry.io/welcome/) pour stocker les détails (par exemple, les traces de pile) de mes erreurs, et les afficher sur leur tableau de bord basé sur le web.
- [**pino**](https://github.com/pinojs/pino) pour activer la journalisation dans mon Nodejs.

**Pourquoi Sentry** ? Eh bien, il a été recommandé par de nombreux développeurs et petites startups. Il offre 5000 erreurs que vous pouvez envoyer par mois gratuitement. Pour mettre cela en perspective, si vous gérez un petit projet parallèle et que vous êtes prudent à ce sujet, je dirais que cela durera jusqu'à ce que vous puissiez vous offrir un fournisseur ou un plan plus luxueux. 
    
Une autre option à explorer est [honeybadger.io](https://www.honeybadger.io/) avec un niveau gratuit plus généreux mais sans [transport pino](https://getpino.io/#/docs/transports).

**Pourquoi Pino** - Pourquoi pas le SDK officiel fourni par Sentry ? Parce que Pino a une ['faible surcharge'](https://github.com/pinojs/pino#low-overhead), alors que le SDK Sentry, bien qu'il vous donne une image plus complète d'une erreur, semblait avoir un problème de [mémoire complexe](https://github.com/getsentry/sentry-javascript/issues/1762) que je ne pouvais pas contourner.

Avec cela, voici comment le système de journalisation est configuré dans Sametable :

```javascript
// server/lib/logger.js

// installer les packages manquants
const pino = require("pino");
const { createWriteStream } = require("pino-sentry");
const expressPino = require("express-pino-logger");

const options = { name: "sametable", level: "error" };

// SENTRY_DSN est fourni par Sentry. Stockez-le comme variable d'environnement dans le fichier .env.
const stream = createWriteStream({ dsn: process.env.SENTRY_DSN });

const logger = pino(options, stream);
const expressLogger = expressPino({ logger });

module.exports = {
  expressLogger, // utilisez-le comme app.use(expressLogger) -> req.log.info('haha)
  logger,
};
```

Plutôt que d'attacher le logger (`expressLogger`) en tant que middleware en haut de la chaîne (`app.use(expressLogger)`), j'utilise l'objet `logger` uniquement là où je veux journaliser une erreur.

Par exemple, le gestionnaire d'erreurs global personnalisé utilise l'objet `logger` :

```javascript
app.use(function (err, req, res, next) {
  const error = err.status
    ? err
    : createError(500, "Something went wrong. Notified dev.");

  if (isProduction) {
    // LOG THIS ERROR IN MY SENTRY DASHBOARD
    logger.error(error);
  } else {
    console.log("Custom error handler:", error);
  }

  res.status(error.status).json(error);
});
```

C'est tout ! Et n'oubliez pas d'activer la notification par **email** dans votre tableau de bord Sentry pour recevoir une alerte lorsque votre Sentry reçoit une erreur ! ❤️

### Lien permanent pour le partage d'URL

Nous avons vu des URL composées de chaînes alphanumériques cryptiques comme celles sur YouTube : `https://youtube.com/watch?v=upyjlOLBv5o`. Cette URL pointe vers une vidéo spécifique, qui peut être partagée avec quelqu'un en partageant l'URL. Le composant clé de l'URL représentant la vidéo est l'ID unique à la fin : `upyjlOLBv5o`. 
    
Nous voyons ce type d'ID sur d'autres sites aussi : `vimeo.com/259411563` et l'ID de l'abonnement dans Stripe `sub_aH2s332nm04`.

Pour autant que je sache, il y a trois façons d'atteindre ce résultat :

1. [Générer l'ID lors de l'insertion de données dans votre base de données](https://stackoverflow.com/a/41988979/73323). L'ID généré sera l'ID dans votre colonne `id` plutôt que ceux à incrémentation automatique :

   | id         | title        |
   | ---------- | ------------ |
   | owmCAx552Q | Comment pleurer   |
   | ZIofD6l3X9 | Comment sourire |

Ensuite, vous exposerez ces ID dans les URL publiques : `https://example.com/task/owmCAx552Q`. Étant donné cette URL à votre backend, vous pouvez récupérer la ressource respective de la base de données :

   ```javascript
   router.get("/task/:taskId", (req, res, next) => {
     const { taskId } = req.params;
     // SELECT * FROM tasks WHERE id=<taskId>
   });
   ```

Les inconvénients de cette méthode que je connais sont :

   - Les ID peuvent être des informations sensibles à exposer publiquement comme cela.
   - Ces ID sont préjudiciables à la performance de l'indexation et de la 'jonction' sur vos tables.

2. Vous gardez l'incrémentation automatique de vos ID dans vos tables, mais vous les représenterez en [générant leur équivalent alphanumérique lors des opérations de base de données](https://hashids.org/postgresql/) :

   ```sql
     SELECT hash_encode(123, 'this is my salt', 10); -- Résultat : 4xpAYDx0mQ
     SELECT hash_decode('4xpAYDx0mQ', 'this is my salt', 10); -- Résultat : 123
   ```

   J'ai eu des problèmes à intégrer cette bibliothèque sur ma machine Windows. Donc je suis passé à l'option suivante.

3. [Similaire à la deuxième option ci-dessus mais approche différente](https://old.reddit.com/r/PostgreSQL/comments/6gw866/best_practice_for_id_system_that_is_obscure_for/diu8cr1/). Cela générera un ID numérique : `https://example.com/task/2013732563294762`

## Système d'authentification utilisateur

Un système d'authentification utilisateur peut devenir très compliqué si vous devez supporter des choses comme le SSO et les fournisseurs OAuth tiers. C'est pourquoi nous avons des outils tiers tels que Auth0, Okta et PassportJS pour nous abstraire cela. Mais ces outils coûtent : verrouillage du fournisseur, plus de charge utile JavaScript et surcharge cognitive.

Je dirais que si vous commencez et avez juste besoin d'un _certain_ _type_ de système d'authentification pour pouvoir passer à d'autres parties de votre application, et en même temps, submergé par tous les tutoriels obsolètes qui traitent de choses que vous n'utilisez pas, eh bien, il y a de fortes chances que tout ce dont vous avez besoin est la bonne vieille méthode d'authentification : **Cookie de session** avec **email** et **mot de passe** ! Et nous ne parlons pas de 'JWT' non plus ! Aucun de cela.

### Guide

[Voici un guide](https://medium.com/@kilgarenone/easily-implements-user-authentication-in-nodejs-b22bdb6f15bc) que j'ai fini par écrire. Suivez-le et vous aurez un système d'authentification utilisateur !

## Email

Actuellement, dans Sametable, les seuls emails qu'il envoie sont de type 'transactionnel' comme l'envoi d'un email de réinitialisation de mot de passe lorsque les utilisateurs réinitialisent leur mot de passe.

Il existe deux façons d'envoyer des emails dans Nodejs :

1. **Créez le vôtre** avec [Nodemailer](https://nodemailer.com/about/).

   Je ne suivrais pas cette voie car, bien que l'envoi d'un email puisse sembler une tâche triviale, le faire 'à grande échelle' est difficile ; chaque email doit être envoyé avec succès ; et ils ne doivent pas finir dans le dossier de spam d'un utilisateur ; et d'autres choses dont je ne suis pas conscient.

2. Choisissez l'un des **fournisseurs de services d'email**.

De nombreux services d'email offrent un plan gratuit offrant un nombre limité d'emails que vous pouvez envoyer par mois/jour gratuitement. Lorsque j'ai commencé à explorer cet espace pour Sametable en octobre 2019, Mailgun s'est avéré être un choix évident&mdash;Il offre 10 000 emails gratuitement par mois ! 
    
Mais, malheureusement, alors que je faisais des recherches pour la rédaction de cette section, j'ai appris qu'il n'offre plus cela. Malgré cela, je resterais tout de même avec Mailgun, sur leur plan [pay-as-you-go](https://www.mailgun.com/pricing) : 1000 emails envoyés vous coûteront 80 cents.

Si vous préférez ne pas payer un centime pour une raison quelconque, voici deux options que j'ai pu trouver pour vous :

   - [https://www.mailjet.com/pricing/](https://www.mailjet.com/pricing/)
   - [https://www.sendinblue.com/pricing/](https://www.sendinblue.com/pricing/)

Mais allez dans cette voie en étant conscient qu'il n'y a aucune garantie que ces plans gratuits resteront ainsi pour toujours comme ce fut le cas avec Mailgun.

### Implémentation

#### Fichier wrapper

```javascript
// server/lib/email.js

// Exécutez 'npm install mailgun-js' dans votre dossier 'server'
const mailgun = require("mailgun-js");

const DOMAIN = "mail.sametable.app";

const mg = mailgun({
  apiKey: process.env.MAILGUN_API_KEY,
  domain: DOMAIN,
});

function send(data) {
  mg.messages().send(data, function (error) {
    if (!error) return;
    console.log("Erreur d'envoi d'email :", error);
  });
}

module.exports = {
  send,
};
```

#### Utilisation

```javascript
const mailer = require("../lib/email");

// Simplifié pour les éléments liés à l'email uniquement
router.post(
  "/resetPassword",
  upload.none(),
  (req, res, next) => {
    const { email } = req.body;
    const data = {
      from: "Sametable <feedback@sametable.app>",
      to: email,
      subject: "Réinitialisez votre mot de passe",
      text: `Cliquez sur ce lien pour réinitialiser votre mot de passe : https://example.com?token=1234`,
    };
    mailer.send(data);
    res.json({});
  })
);
```

### Modèles d'email

Chaque type d'email que vous envoyez pourrait avoir son propre modèle d'email dont le contenu peut être varié avec des valeurs dynamiques que vous pouvez fournir.

#### Outil

[**mjml**](https://mjml.io/) est l'outil que j'utilise pour construire mes modèles d'email. Bien sûr, il existe de nombreux constructeurs d'email par glisser-déposer qui ne vous intimident pas avec la vue de 'codes'. Mais si vous connaissez juste le React/HTML/CSS de base, mjml vous offrira une grande utilité et une flexibilité maximale.

Il est facile de [commencer](https://mjml.io/getting-started/1). Comme les constructeurs d'email, vous composez un modèle avec un ensemble de composants réutilisables, et vous les personnalisez en fournissant des valeurs à leurs props.

Voici les endroits où j'écrirais mes modèles :

- Cette [extension VSCode](https://marketplace.visualstudio.com/items?itemName=attilabuti.vscode-mjml)
- [Éditeur de code en direct](https://mjml.io/try-it-live)

#### Exemple de modèle

<details>
  <summary>Modèle d'email</summary>

```html
<mjml>
  <mj-head>
    <mj-attributes>
      <mj-class
        name="font-family"
        font-family="-apple-system,system-ui,BlinkMacSystemFont,'Segoe UI',sans-serif"
      />
      <mj-class name="fw-600" font-weight="600" />
    </mj-attributes>
  </mj-head>
  <mj-body>
    <mj-section>
      <mj-column>
        <mj-image
          width="150px"
          src="https://www.dl.dropboxusercontent.com/s/pgtwrnfa3lqkf5r/sametable_logo_with_text.png"
        />
      </mj-column>
    </mj-section>
    <mj-section>
      <mj-column>
        <mj-text align="center" font-size="20px" mj-class="font-family"
          >{{assigner_name}} vous a assigné un projet</mj-text
        >
        <mj-spacer height="10px" />
        <mj-text align="center" font-size="25px" mj-class="font-family fw-600"
          >{{project_title}}</mj-text
        >
        <mj-spacer height="25px" />
        <mj-button
          font-size="16px"
          mj-class="font-family fw-600"
          background-color="#000"
          color="white"
          href="{{invite_link}}"
          >Voir le projet</mj-button
        >
      </mj-column>
    </mj-section>
    <mj-spacer height="55px" />
    <mj-section background-color="#EEEBE7" padding="25px 40px">
      <mj-column>
        <mj-text
          align="center"
          color="#45495d"
          font-size="15px"
          line-height="14px"
        >
          Problèmes ou questions ? N'hésitez pas à répondre à cet email.
        </mj-text>
        <mj-text padding="30px 0 0 0" align="center" font-size="16px">
          Made with ❤️ by
          <a href="https://twitter.com/kheohyeewei">@kheohyeewei</a>
        </mj-text>
      </mj-column>
    </mj-section>
  </mj-body>
</mjml>
```

</details>

##### Résultat

<img width="400px" src="https://i.imgur.com/JnaSDYJ.png" loading="lazy" />

Remarquez les noms de placeholders qui sont enveloppés dans des doubles accolades comme `{{project_title}}`. Ils seront remplacés par leur valeur correspondante par, dans mon cas, Mailgun, avant d'être envoyés.

#### Intégration avec Mailgun

Tout d'abord, générez du HTML à partir de vos modèles mjml. Vous pouvez le faire avec l'extension VSCode ou l'éditeur de code basé sur le web :

<img src="https://i.imgur.com/O9mnBvN.png" alt="générer du html dans l'éditeur de code mjml en ligne" loading="lazy" />

Ensuite, créez un nouveau modèle sur votre tableau de bord Mailgun :

<img src="https://i.imgur.com/OkvLxiT.png" alt="créer un modèle de message sur le tableau de bord mailgun" loading="lazy" />

#### Envoyer un email avec Mailgun dans Nodejs

À l'intérieur d'une route :

```javascript
const data = {
  from: "Sametable <feedback@sametable.app>",
  to: email,
  subject: `Bonjour`,
  template: "invite_project", // le nom du modèle que vous avez donné lors de sa création dans mailgun
  "v:invite_link": inviteLink,
  "v:assigner_name": fullname,
  "v:project_title": title,
};

mailer.send(data);
```

Remarquez que, pour associer une valeur à un nom de placeholder dans un modèle : `"v:project_title":'Project Mario'`.

### Comment obtenir l'un de ces `hi@example.com`

C'est une adresse email que les gens utilisent pour vous contacter concernant votre SaaS, plutôt qu'avec un `lola887@hotmail.com`.

Il y a trois options sur mon radar :

1. Si vous êtes sur Mailgun, suivez [ce guide](https://renzo.lucioni.xyz/mail-forwarding-with-mailgun/). Cependant, le nouveau niveau pay-as-you-go a exclu la fonctionnalité (`Inbound Email Routing`) qui rend cela possible. Donc peut-être l'option suivante ;
2. Si je me fais un jour exclure de mon niveau '10,000' gratuit chez Mailgun, j'essaierais cela https://forwardemail.net/en
3. Si tout le reste échoue, payez pour ['Gmail sur G Suite'](https://gsuite.google.com.my/intl/en_my/products/gmail/).

## Tenancy

Lorsque qu'une organisation, par exemple Acme Inc., s'inscrit sur votre SaaS, elle est considérée comme un 'locataire' &mdash; Ils 'occupent' une place sur votre service.

Bien que j'aie entendu le terme 'multi-tenancy' associé à un SaaS auparavant, je n'avais pas la moindre idée de sa mise en œuvre. Je pensais toujours que cela impliquerait des manœuvres cryptiques de type informatique que je n'aurais jamais pu comprendre tout seul.

Heureusement, il existe une manière facile de faire du 'multi-tenancy' :

> Une seule base de données ; tous les clients partagent les mêmes tables ; chaque client a un `tenant_id` ; interroge la base de données selon une requête API par `WHERE tenant_id = $ID`.

Donc ne vous inquiétez pas&mdash;Si vous connaissez le SQL de base (ce qui indique à nouveau l'importance de maîtriser les bases dans tout ce que vous faites !), vous devriez avoir une image claire des étapes nécessaires pour mettre cela en œuvre.

Voici trois ressources instrumentales sur le 'multi-tenancy' que j'ai marquées auparavant :

- [https://stackoverflow.com/a/47783180/73323](https://stackoverflow.com/a/47783180/73323)
- [https://stackoverflow.com/a/44530588/73323](https://stackoverflow.com/a/44530588/73323)
- [https://blog.checklyhq.com/building-a-multi-tenant-saas-data-model/](https://blog.checklyhq.com/building-a-multi-tenant-saas-data-model/)

## Nom de domaine

Le domaine Sametable.app et tous ses enregistrements DNS sont hébergés chez [**NameCheap**](https://www.namecheap.com/). J'étais auparavant sur [hover](https://www.hover.com/) (il héberge toujours le domaine de mon site personnel). Mais j'ai rencontré une limitation là-bas lorsque j'ai essayé d'entrer ma valeur DKIM de Mailgun. Namecheap a également des prix plus compétitifs selon mon expérience.

À quel stade du développement de votre SaaS devriez-vous obtenir un nom de domaine ? Eh bien, je dirais pas avant que le manque d'un registraire DNS ne bloque votre développement. Dans mon cas, je l'ai différé jusqu'à ce que j'aie dû intégrer Mailgun, ce qui nécessite la création d'un ensemble d'enregistrements DNS dans un domaine.

### Comment obtenir l'un de ces `app.example.com`

Vous connaissez ces URL qui ont un `app` devant comme `app.example.io` ? Oui, c'est un 'domaine personnalisé' avec 'app' comme 'sous-domaine'. Et tout a commencé avec l'obtention d'un nom de domaine. 
    
Alors, allez-y et obtenez-en un chez Namecheap ou autre. Ensuite, dans mon cas avec Firebase, suivez simplement [ce tutoriel](https://firebase.google.com/docs/hosting/custom-domain) et tout ira bien.

## Déploiement

Ugh. C'était une étape où j'ai lutté pendant très longtemps ?. Ce fut un voyage infernal où je me suis retrouvé à m'engager sur une plateforme cloud pour finalement abandonner en découvrant leurs inconvénients pour optimiser l'expérience développeur, les coûts, le quota et les performances (latence).

Le voyage a commencé avec moi plongeant tête la première (mauvaise idée) dans Digital Ocean puisque je l'ai vu recommandé beaucoup dans le forum IndieHackers. Et effectivement, j'ai réussi à faire fonctionner mon Nodejs dans une VM en suivant [de près](https://coderrocketfuel.com/article/create-and-deploy-an-express-rest-api-to-a-digitalocean-server#configure-and-deploy-your-node-js-app) les [tutoriels](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-node-js-application-for-production-on-ubuntu-18-04). 
    
Ensuite, j'ai découvert que le [DO Space](https://www.digitalocean.com/products/spaces/) n'était pas exactement AWS S3&mdash;Il [ne peut pas](https://ideas.digitalocean.com/ideas/DO-I-318) héberger mon SPA. 
    
Bien que j'aurais [pu](https://coderrocketfuel.com/article/deploy-a-create-react-app-website-to-digitalocean) l'héberger dans mon droplet et [connecter](https://www.youtube.com/watch?v=2X_Tp_G7aTs) un CDN tiers comme CloudFlare au droplet, cela me semblait inutilement compliqué par rapport à la configuration S3+Cloudfront. J'utilisais également une base de données gérée par DO (Postgresql) parce que je ne voulais pas gérer ma base de données et tweaker les fichiers `*.config` moi-même. Cela coûte un fixe de 15$/mois.

Ensuite, j'ai appris l'existence de [AWS Lightsail](https://aws.amazon.com/lightsail/) qui est une image miroir de DO, mais à ma surprise, avec un [quota](https://aws.amazon.com/lightsail/pricing/) plus compétitif à un point de prix donné :

**VM à 5$/mois**

| AWS Lightsail      | Digital Ocean    |
| ------------------ | ---------------- |
| 1 Go de mémoire        | 1 Go de mémoire      |
| 1 processeur        | 1 processeur |
| **40 Go** de disque SSD | 25 Go de disque SSD   |
| **2 To** de transfert  | 1 To de transfert    |

**Base de données gérée à 15$/mois**

| AWS Lightsail      | Digital Ocean    |
| ------------------ | ---------------- |
| 1 Go de mémoire        | 1 Go de mémoire      |
| 1 processeur        | 1 processeur |
| **40 Go** de disque SSD | 10 Go de disque SSD   |

J'ai donc commencé à parier sur Lightsail à la place. Mais, le 15$/mois pour une base de données gérée dans Lightsail m'a atteint à un moment donné. Je ne voulais pas avoir à payer cet argent alors que je n'étais même pas sûr que j'aurais un jour des clients payants.

À ce stade, j'ai supposé que je devais me salir les mains pour optimiser le facteur coût. J'ai donc commencé à regarder comment configurer AWS EC2, RDS, etc. Mais il y avait simplement trop de choses spécifiques à AWS que je devais apprendre, et la documentation AWS n'était pas exactement utile non plus&mdash;C'est un trou de lapin après l'autre juste pour faire une chose parce que j'avais juste besoin de quelque chose pour héberger mon SPA et Nodejs pour l'amour du ciel !

Ensuite, j'ai vérifié IndieHacker pour une vérification de santé mentale, et je suis tombé sur [render.com](https://render.com/). Cela semblait parfait ! C'est l'un de ces outils qui ont pour mission '_pour que vous puissiez vous concentrer sur la construction de votre application_'. Les tutoriels étaient courts et vous mettaient en route en un rien de temps. Et voici le '_mais_'&mdash;C'était [cher](https://render.com/pricing) :

**Comparaison de Lightsail et Render à leur point de prix le plus bas**

| AWS Lightsail (3,50 $/mois) | Render (7 $/mois)                               |
| ------------------------ | -------------------------------------------- |
| 512 Go de mémoire            | 512 Mo de mémoire                                |
| 1 processeur                | Processeur partagé                             |
| 20 Go de disque SSD           | 0,25 $/Go/mois de disque SSD (20 Go = 5 $/mois)           |
| 1 To de transfert            | 100 Go/mois. 0,10 $/Go au-dessus de cela (1 To = 90 $/mois) |

Et c'est juste pour héberger mon Nodejs !

Alors, que faire maintenant ?! Dois-je simplement dire _f\*\*\* it_ et faire tout ce qu'il faut pour 'le livrer' ?

Mais j'ai tenu bon. J'ai revisité AWS. Je croyais toujours qu'AWS était la réponse parce que tout le monde chante ses louanges. Je dois manquer quelque chose ! 
    
Cette fois, j'ai considéré leurs outils de plus haut niveau comme AWS AppSync et Amplify. Mais je ne pouvais pas ignorer le fait que les deux m'obligent à travailler complètement selon leurs normes et leur bibliothèque. À ce stade, j'en avais assez d'AWS et je me suis tourné vers une autre... plateforme : **Google Cloud Platform (GCP)**.

Le Nodejs, Redis et Postgresql de Sametable sont hébergés sur **GCP**.

Ce qui m'a attiré vers GCP, c'est sa documentation&mdash;Elle est beaucoup plus linéaire ; des extraits de code partout pour votre langage spécifique ; des guides étape par étape sur les choses courantes que vous feriez pour une application web. De plus, c'est serverless ! Ce qui signifie que votre coût est proportionnel à votre utilisation.

### Déployer Nodejs

L'environnement ['standard'](https://cloud.google.com/appengine/docs/the-appengine-environments) de GAE héberge mon Nodejs.

#### Coût

L'environnement standard de GAE a un [quota gratuit](https://cloud.google.com/free/docs/gcp-free-tier#always-free-usage-limits) contrairement à l'environnement 'flexible'. Au-delà de cela, vous ne paierez que si quelqu'un utilise votre SaaS ?.

#### Guide

C'était le _seul_ guide sur lequel je me suis appuyé. C'était mon étoile polaire. Il couvre Nodejs, Postgresql, Redis, le stockage de fichiers, et plus encore :

> [https://cloud.google.com/appengine/docs/standard/nodejs](https://cloud.google.com/appengine/docs/standard/nodejs)

Commencez par le tutoriel ['Quick Start'](https://cloud.google.com/appengine/docs/standard/nodejs/quickstart) car il vous configurera avec le `gcloud cli` dont vous aurez besoin lorsque vous suivrez le reste des guides, où vous trouverez des commandes que vous pouvez exécuter pour suivre.
    
Si vous n'êtes pas à l'aise avec l'environnement CLI, les guides fourniront des étapes alternatives pour atteindre le même objectif sur le tableau de bord GCP. J'adore ça.

J'ai remarqué qu'en parcourant la documentation GCP, je n'ai jamais eu à ouvrir plus de 4 onglets dans mon navigateur. C'était tout le contraire avec la documentation AWS&mdash;Mon navigateur serait _rempli_ de celle-ci.

### Déployer Postgresql

#### Guide

[https://cloud.google.com/sql/docs/postgres/connect-app-engine-standard](https://cloud.google.com/sql/docs/postgres/connect-app-engine-standard)

Suivez-le simplement et tout ira bien.

#### Coût

Une instance de Cloud SQL exécute une machine virtuelle complète. Et une fois qu'une VM a été provisionnée, elle ne s'éteindra pas automatiquement lorsque, par exemple, elle n'a pas vu d'utilisation pendant 15 minutes. Vous serez donc facturé pour chaque heure qu'une instance est en cours d'exécution pendant un mois entier, sauf si elle a été arrêtée manuellement.

Le facteur principal qui affectera votre coût ici, particulièrement dans les premiers jours, est le grade du [type de machine](https://cloud.google.com/sql/pricing#2nd-gen-instance-pricing). Le type de machine par défaut pour un Cloud SQL est un `db-n1-standard-1`, et le moins cher que vous pouvez obtenir est un `db-f1-micro` :

| db-n1-standard-1                                                                                    | db-f1-micro                                                                | Digital Ocean Managed DB |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------ |
| 1 vCPU                                                                                              | 1 vCPU partagé                                                              | 1 vCPU                   |
| 3,75 Go de mémoire                                                                                       | 0,6 Go de mémoire                                                               | 1 Go de mémoire               |
| 10 Go de stockage SSD                                                                                    | 10 Go de stockage SSD                                                           | 10 Go de stockage SSD         |
| [~USD 51,01](https://cloud.google.com/products/calculator/#id=c0040a15-933d-4dc3-8022-1428fc210050) | [~USD 9,37](https://cloud.google.com/sql/pricing#2nd-gen-instance-pricing) | [USD 15.00](https://www.digitalocean.com/pricing/#managed-databases)                |

Les deux autres facteurs de coût sont le [stockage et la sortie réseau](https://cloud.google.com/sql/pricing#pg-storage-networking-prices). Mais ils sont facturés mensuellement, donc ils n'auront probablement pas un impact aussi important sur la facture de votre SaaS naissant.

Si vous trouvez les prix trop élevés à votre goût, gardez à l'esprit qu'il s'agit d'une base de données _gérée_. Vous payez pour tout le temps et l'anxiété économisés en faisant du devops sur votre base de données. Pour moi, cela en vaut la peine.

### Configurer les schémas dans la base de données de production

Maintenant que j'ai une base de données déployée pour la production, il est temps de l'habiller avec tous mes schémas du fichier `.sql` <a href="#schemas-file">fichier</a>. Pour cela, je dois me connecter à la base de données depuis pgAdmin :

1. [https://cloud.google.com/sql/docs/postgres/external-connection-methods](https://cloud.google.com/sql/docs/postgres/external-connection-methods)
2. Vous y trouverez un tableau avec une liste d'options pour vous connecter depuis une application externe. J'ai choisi la première : **Adresse IP publique avec SSL**. Suivez tous les guides dans la colonne 'Plus d'informations' et vous aurez toutes les informations nécessaires pour créer un serveur dans votre pgAdmin. Vous serez bien. Si ce n'est pas le cas, <a href="mailto:oldjoy@protonmail.com">envoyez-moi un email</a> et je vous fournirai de l'assistance.

### Déployer Redis

Si vous suiviez le guide principal sur Nodejs, vous ne pouvez pas manquer [ce guide](https://cloud.google.com/appengine/docs/standard/nodejs/using-memorystore) sur la configuration de votre Redis dans MemoryStore. Mais j'ai pensé qu'il serait plus rentable d'**héberger mon Redis dans un Google Compute Engine** (GCE) qui, contrairement à MemoryStore, a un quota gratuit dans certains aspects. ([Voir ceci](https://github.com/ripienaar/free-for-dev#major-cloud-providers) pour une comparaison des quotas gratuits entre différentes plateformes cloud)

#### Guide

1. [Configurer](https://cloud.google.com/community/tutorials/setting-up-redis) Redis dans une VM.

2) [Configurer](https://cloud.google.com/appengine/docs/standard/python/connecting-vpc) VPC :

   > Serverless VPC Access vous permet de vous connecter directement depuis votre application App Engine à votre réseau VPC, **permettant l'accès aux instances de VM Compute Engine**, aux instances Memorystore et à toute autre ressource avec une adresse IP interne.

3. Dans votre fichier `app.yaml` :

   ```yaml
   vpc_access_connector:
     name: "<YOURS_HERE>"

   env_variables:
     REDIS_PASSWORD: "<PASSWORD_YOU_SET_IN_A_GUIDE_ABOVE>"
     REDISHOST: "<INTERNAL_IP_OF_YOUR_VM>"
     REDISPORT: "6379" # port par défaut lors de l'installation de redis
   ```

   <figure>
    <img src="https://i.imgur.com/N4bqhcT.png" alt="ip interne d'une vm GCE" loading="lazy" />
    <figcaption>
        <small>IP interne d'une GCE</small>
    </figcaption>
   </figure>

4. Enfin, dans `lib/redis.js` :

   ```js
   const redis = require("redis");

   const redisClient = redis.createClient(
     NODE_ENV === "production"
       ? {
           host: process.env.REDISHOST,
           port: process.env.REDISPORT, // par défaut à 6379 si non défini
           no_ready_check: true,
           auth_pass: process.env.REDIS_PASSWORD,
         }
       : {} // utilisez simplement les valeurs par défaut : localhost et ports
   );

   module.exports = {
     redisClient,
   };
   ```

### Stockage de fichiers

[Cloud Storage](https://cloud.google.com/storage/docs) est ce dont vous avez besoin pour que vos utilisateurs puissent télécharger leurs fichiers tels que des images dont ils auront besoin pour les récupérer et éventuellement les afficher plus tard.

#### Coût

Il existe également un [niveau gratuit](https://cloud.google.com/free/docs/gcp-free-tier#always-free-usage-limits) pour Cloud Storage.

#### Guide

- Vous serez bien :
  [https://cloud.google.com/appengine/docs/standard/nodejs/using-cloud-storage](https://cloud.google.com/appengine/docs/standard/nodejs/using-cloud-storage)

### Déployer de nouvelles modifications dans le back-end

J'ai un script npm dans le `package.json` de la racine pour publier de nouvelles modifications dans mon back-end vers GCP :

```json
"scripts": {
    "deploy-server": "gcloud app deploy ./server/app.yaml"
}
```

Ensuite, exécutez-le dans un terminal à la racine de votre projet :

```json
npm run deploy-server
```

## Héberger votre SPA

Lorsque j'étais encore sur Lightsail, mon SPA était [hébergé](https://medium.com/@kilgarenone/deploy-spa-to-aws-9302796acd88) sur S3+Cloudfront car je supposais que c'était mieux de les garder sous la même plateforme pour une meilleure latence. Ensuite, j'ai trouvé GCP. 
    
En tant que réfugié battu d'AWS atterrissant dans GCP, j'ai d'abord exploré le 'Cloud Storage' pour héberger mon SPA, et il s'avère que ce n'était pas idéal pour SPA. C'est plutôt compliqué. Donc vous pouvez sauter cela.

Ensuite, j'ai essayé d'héberger mon SPA dans [**Firebase**](https://firebase.google.com/docs/hosting/quickstart). Facilement fait en quelques minutes même si c'était ma première fois là-bas. J'adore ça.

Une autre option que vous pouvez considérer est [Netlify](https://netlify.com) qui est super facile à démarrer aussi.

### Déployer de nouvelles modifications dans le front-end

De manière similaire au déploiement des modifications du back-end, j'ai un autre script npm dans le `package.json` de la racine pour publier de nouvelles modifications dans mon front-end vers Firebase :

```json
"scripts": {
    "deploy-client": "npm run build-client && firebase deploy",
    "build-client": "npm run test && cd client && npm i && npm run build",
    "test": "npm run lint",
    "lint": "npm run lint:js && npm run lint:css",
    "lint:js": "eslint 'client/src/**/*.js' --fix",
    "lint:css": "stylelint '**/*.{scss,css}' '!client/dist/**/*'"
}
```

_"Whoa attendez, d'où vient tout ce truc ??"_

Ils sont une chaîne de scripts qui s'exécutent séquentiellement une fois déclenchés par le script `deploy-client`. Le caractère `&&` est ce qui les colle ensemble.

Tenons-nous la main et parcourons-le du début à la fin :

1. D'abord, nous faisons `npm run deploy-client`,
2. qui exécute `build-client` en premier,
3. qui exécute `test` en premier, (vous voyez, nous suivons simplement où un script et son `&&` nous mènent, ce qui explique pourquoi `firebase deploy` ne s'exécutera pas tout de suite)
4. qui exécute `lint`,
5. qui nous amène à `lint:js` en premier, puis à `lint:css`,
6. puis de retour à `cd client`, suivi de `npm i` et `npm run build`,
7. et enfin, c'est au tour de `firebase deploy` de s'exécuter.

**Astuce** : Si les modifications que vous avez apportées concernent le full-stack, vous pourriez avoir un script qui déploie 'client' et 'server' ensemble :

```json
"scripts": {
    "deploy-all": "npm run deploy-server && npm run deploy-client",
}
```

## Éditeur de texte enrichi

La construction de l'éditeur de texte enrichi dans Sametable a été la deuxième chose la plus difficile pour moi. J'ai réalisé que j'aurais pu l'avoir facilement avec ces éditeurs prêts à l'emploi comme CKEditor et TinyMCE, mais je voulais pouvoir façonner l'expérience d'écriture dans l'éditeur, et rien ne peut faire cela mieux que [**ProseMirror**](https://prosemirror.net/). Bien sûr, j'avais d'autres options aussi, que j'ai écartées pour plusieurs raisons :

1. [Quilljs](https://quilljs.com/)
   - Semblait avoir de nombreux problèmes [non résolus](https://github.com/quilljs/quill/issues).
   - Façonné spécifiquement par un groupe d'intérêt spécial.
   - Implique des solutions de contournement bidouillées une fois que vous vous aventurez hors de l'ensemble des cas d'utilisation standard.
2. [Draftjs](https://draftjs.org/)
   - Ils sont étroitement couplés avec React.
   - Avec la surcharge du DOM virtuel, ils ne performeront pas aussi bien que Prosemirror.
3. [trix](https://trix-editor.org/)
   - Basé sur Web Component. J'ai eu des problèmes à l'intégrer dans Preact.
   - Il n'était pas flexible pour construire une expérience d'édition personnalisée.

**Prosemirror** est sans aucun doute une bibliothèque _impeccable_. Mais l'apprendre n'était pas pour les âmes sensibles, du moins à mon avis. 
    
J'ai échoué à construire des modèles mentaux complets de celui-ci même après avoir lu le [guide](https://prosemirror.net/docs/guide/) plusieurs fois. La seule façon dont je pouvais progresser à partir de là était en croisant les exemples de code existants et le [manuel](https://prosemirror.net/docs/ref/), et en procédant par essais et erreurs. Et si j'épuisais cela aussi, alors je demanderais dans le forum et c'était toujours répondu. Je ne me donnerais pas la peine avec StackOverflow sauf peut-être pour le populaire Quilljs.

Voici les endroits où je suis allé chercher des exemples de code :

- Les [exemples officiels](https://prosemirror.net/examples/)
- Recherchez dans le [forum](https://discuss.prosemirror.net/)
- 'Fork' [prosemirror-example-setup](https://github.com/prosemirror/prosemirror-example-setup)
- Un éditeur appelé [tiptap](https://tiptap.scrumpy.io/) qui est basé sur Prosemirror mais construit pour Vuejs. La base de code contient en fait très peu de bits de Vuejs. Vous pouvez donc trouver beaucoup de snippets spécifiques à Prosemirror utiles là-bas (merci les gars !).

Dans l'esprit de ce voyage d'apprentissage, j'ai extrait l'éditeur de texte enrichi de Sametable dans un CodeSandBox :

[https://codesandbox.io/s/compassionate-montalcini-gcgwc](https://codesandbox.io/s/compassionate-montalcini-gcgwc)

?

(**Note** : Prosemirror est indépendant du framework ; la démonstration CodeSandBox n'utilise que 'create-react-app' pour le bundling des modules ES6.)

## CORS

Pour empêcher votre navigateur de se plaindre des problèmes CORS, c'est [tout à propos](https://medium.com/@kilgarenone/deploy-your-nodejs-app-to-digital-ocean-1de40797666f#4aa4) de faire en sorte que votre backend envoie ces en-têtes `Access-Control-Allow-*` en retour par requête. (Des excuses pour la simplification excessive sont de mise)

Mais, corrigez-moi si je me trompe, il n'y a [aucun moyen](https://stackoverflow.com/a/60502433/73323) de configurer CORS dans GAE lui-même. J'ai donc dû le faire avec le package npm [cors](https://www.npmjs.com/package/cors) :

```js
const express = require("express");
const app = express();
const cors = require("cors");

const ALLOWED_ORIGINS = [
  "http://localhost:8008",
  "https://web.sametable.app", // votre domaine SPA
];

app.use(
  cors({
    credentials: true, // inclure Access-Control-Allow-Credentials: true. rappelez-vous de définir xhr.withCredentials = true;
    origin(origin, callback) {
      // autoriser les requêtes sans origine
      // (comme les applications mobiles ou les requêtes curl)
      if (!origin) return callback(null, true);
      if (ALLOWED_ORIGINS.indexOf(origin) === -1) {
        const msg =
          "La politique CORS pour ce site ne " +
          "permet pas l'accès depuis l'origine spécifiée.";
        return callback(new Error(msg), false);
      }
      return callback(null, true);
    },
  })
);
```

## Paiement & Abonnement

Un SaaS permet généralement aux utilisateurs de payer et de s'abonner pour accéder aux fonctionnalités payantes que vous avez désignées.

Pour permettre cette possibilité dans Sametable, j'utilise **Stripe** pour gérer à la fois les flux de paiement et d'abonnement.

### Guide

Il existe deux façons de les implémenter :

1. [Très pratique](https://stripe.com/docs/billing/subscriptions/fixed-price) qui est idéal pour personnaliser votre interface utilisateur.
2. [**Checkout**](https://stripe.com/docs/payments/checkout/set-up-a-subscription). Le plus rapide à implémenter. C'est ce que j'ai fait.

### Webhook

Le dernier composant clé dont j'avais besoin pour cette partie était un 'webhook' qui est essentiellement juste un point de terminaison typique dans votre Nodejs qui peut être appelé par un tiers comme Stripe.

J'ai créé un webhook qui sera appelé lorsqu'un paiement aura été facturé avec succès pour signifier dans l'enregistrement de l'utilisateur qui correspond au payeur en tant qu'utilisateur PRO dans Sametable à partir de ce moment-là :

```javascript
router.post(
  "/webhook/payment_success",
  bodyParser.raw({ type: "application/json" }),
  asyncHandler(async (req, res, next) => {
    const sig = req.headers["stripe-signature"];

    let event;

    try {
      event = stripe.webhooks.constructEvent(req.body, sig, webhookSecret);
    } catch (err) {
      return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    // Gérer l'événement checkout.session.completed
    if (event.type === "checkout.session.completed") {
      // 'session' doc : https://stripe.com/docs/api/checkout/sessions/object
      const session = event.data.object;

      // ici vous pouvez interroger votre base de données pour, par exemple,
      // mettre à jour l'enregistrement d'un utilisateur/locataire particulier

      // Retourner une réponse pour accuser réception de l'événement
      res.json({ received: true });
    } else {
      res.status(400);
    }
  })
);
```

#### Référence

Voici un extrait de code d'un webhook :
[https://stripe.com/docs/webhooks/signatures#verify-official-libraries](https://stripe.com/docs/webhooks/signatures#verify-official-libraries)

#### Guide

- [https://stripe.com/docs/webhooks](https://stripe.com/docs/webhooks)

## Page d'accueil

### Construction

J'utilise [**Eleventy**](https://www.11ty.dev/) pour construire la page d'accueil de Sametable. Je [ne recommanderais pas](https://twitter.com/devongovett/status/1222953655722110981) Gatsby ou Nextjs. Ils sont surdimensionnés pour ce travail.

J'ai commencé avec l'un des [projets de démarrage](https://www.11ty.dev/docs/starter/) car j'étais impatient de faire décoller ma page. Mais j'ai eu du mal à travailler avec eux. 
    
Bien qu'Eleventy se présente comme un SSG simple, il y a en fait plusieurs concepts à comprendre si vous êtes nouveau dans les [générateurs de sites statiques](https://www.staticgen.com/)(SSG). Couplé aux outils introduits par les kits de démarrage, les choses peuvent devenir complexes. J'ai donc décidé de partir de zéro et de prendre mon temps pour lire la documentation du début à la fin, en construisant lentement. Calme et facile.

#### Guides

- **Version longue**
  - [https://tatianamac.com/posts/beginner-eleventy-tutorial-parti/](https://tatianamac.com/posts/beginner-eleventy-tutorial-parti/)
  - [https://www.11ty.dev/docs/](https://www.11ty.dev/docs/)
- **Version courte** : [https://github.com/kilgarenone/personal-website](https://github.com/kilgarenone/personal-website) (le premier site web que j'ai construit comme site personnel tout en apprenant 11ty. Il a une page d'accueil et des articles de blog. Très peu de concepts introduits ici. Vous pourriez commencer avec ce 'projet de démarrage')

### Hébergement

J'utilise [**Netlify**](https://www.netlify.com/) pour héberger la page d'accueil. Il y a aussi [surge.sh](https://surge.sh/) et [Vercel](https://vercel.com). Vous serez bien ici.

## Termes et conditions

Les T&C rendent votre SaaS légitime. Pour autant que je sache, voici vos options pour les établir :

1. Écrivez les vôtres [https://pinboard.in/tos/](https://pinboard.in/tos/).
2. Copiez et collez ceux des autres. Changez en conséquence. Jamais facile selon mon expérience.
3. Faites appel à un avocat.
4. Générez-les dans [**getterms.io**](https://getterms.io/).

## Marketing

Il ne manque pas de publications sur le marketing disant que c'était une mauvaise idée de "_Laisser le produit parler de lui-même_". Eh bien, sauf si vous essayiez de 'pirater la croissance' pour gagner la partie.

Ce qui suit est la trajectoire d'existence que j'ai en tête pour Sametable :

1. Construisez quelque chose qui prétend résoudre un problème.
2. Faites votre SEO. Écrivez les articles de blog. Toute personne affectée par le problème que vous avez résolu recherchera ou en entendra parler par le bouche-à-oreille.
3. Si cela ne décolle toujours pas, eh bien, il y a des chances que vous ne résolviez pas un énorme problème réel, ou que suffisamment de personnes l'aient déjà résolu. Dans ce cas, soyez simplement reconnaissant pour tout succès qui vient à vous sur le long terme.

### Ressources

- [https://stripe.com/en-my/atlas/guides/starting-sales](https://stripe.com/en-my/atlas/guides/starting-sales)
- [https://www.coryzue.com/writing/seo-for-developers/](https://github.com/LisaDziuba/Marketing-for-Engineers)

## Bien-être

Il est facile de s'asseoir et de se perdre dans notre travail contemporain. Et nous le faisons en accumulant des dettes sur l'avenir. L'une de ces dettes est notre **santé** personnelle.

Voici comment j'essaie de rester au top de ma dette de santé :

- **Installez** [**Workrave**](https://workrave.org/). Vous pouvez le régler pour verrouiller votre écran après qu'un intervalle se soit écoulé. Plus important encore, il peut montrer quelques exercices que vous pouvez effectuer derrière votre ordinateur !
- Procurez-vous un bureau **debout** réglable si vous pouvez vous le permettre. J'ai le mien chez IKEA.
- Faites des [**burpees**](https://www.youtube.com/watch?v=Kjhl-8yU6hI). Étirez ces articulations. Maintenez une bonne posture. Le [planking](https://www.youtube.com/watch?v=59MaNHq8UDo) aide.
- **Méditez** pour rester sain d'esprit. J'utilise [Medito](https://meditofoundation.org/).

??

Merci de lire. Assurez-vous de consulter mon propre outil SaaS **Sametable** pour [gérer votre travail dans des feuilles de calcul](https://www.sametable.app).