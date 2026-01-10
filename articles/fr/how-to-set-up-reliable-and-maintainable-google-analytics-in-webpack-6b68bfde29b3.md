---
title: Comment configurer Google Analytics fiable et maintenable dans Webpack
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2018-08-13T14:15:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-reliable-and-maintainable-google-analytics-in-webpack-6b68bfde29b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cl_Y0G1UBK76g5vkRxOIoA.jpeg
tags:
- name: Google Analytics
  slug: google-analytics
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment configurer Google Analytics fiable et maintenable dans Webpack
seo_desc: One of the messier bits of a new app setup is trying to figure out where
  to stash your Google Analytics initialization scripts. There are some existing options
  like React Helmet to manage the head of your document. You can toss it in your monolithic
  ...
---

L'un des aspects les plus désordonnés de la configuration d'une nouvelle application est d'essayer de déterminer où placer vos scripts d'initialisation de Google Analytics. Il existe quelques options comme [React Helmet](https://github.com/nfl/react-helmet) pour gérer l'en-tête de votre document. Vous pouvez le placer dans votre fichier `index.html` monolithique.

Le problème est que ces configurations fonctionnent rarement comme vous le souhaitez. Elles finissent par être des blocs disgraciés de chaînes HTML dans votre JavaScript. Vous finissez par devoir gérer ce monolithe de fichier `index.html` dont j'ai parlé précédemment tout au long du cycle de vie de votre projet.

### Pourquoi cela compte

Au-delà de la façon dont vous gérez votre code, si l'analyse est cruciale pour vous et votre entreprise, vous voulez vous assurer que la configuration est fiable et correctement installée.

De nombreux développeurs supposent que, parce que c'est un extrait JS, la meilleure pratique est de le placer en bas de la page. Le problème avec cela est que le placer à la fin laisse un risque plus élevé que vous manquiez de suivre un hit avant qu'un utilisateur ne quitte la page, car Analytics ne s'initialisera pas avant que le reste de la page ne se charge. C'est pourquoi Google lui-même recommande [d'installer l'extrait aussi haut que possible dans l'en-tête](https://support.google.com/analytics/answer/1008080?hl=en).

Aussi important que je dise que cela est, vous pourriez ne pas vous en soucier autant si vous êtes plus détendu à ce sujet et que vous voulez avoir une idée générale de la façon dont les choses se passent sur votre site portfolio. Cependant, si vous étendez votre portée à d'autres outils comme les tests A/B avec Google Optimize, il est encore plus critique que GA reconnaisse la page et l'expérience en cours pour éviter des retards supplémentaires ou pire, un scintillement de la page. ?

![Image](https://cdn-media-1.freecodecamp.org/images/w5Vp2B34jmhaGtlwnRSkksQrrN4YlmDN2QCC)
_Scintillement de contenu indésirable lors de l'exécution d'un test_

### Comment nous allons résoudre cela

[Partials for HTML Webpack Plugin](https://github.com/colbyfayock/html-webpack-partials-plugin) est une extension de [HTML Webpack Plugin](https://github.com/jantimon/html-webpack-plugin) qui simplifie la gestion de vos partials. Son objectif est de spécifiquement essayer d'éviter la pratique de maintenir un fichier `index.html` dans les projets Webpack et de plutôt différer à des partials maintenables simplifiant votre configuration.

Pour l'instant, nous allons nous concentrer sur la configuration de Google Analytics, mais je recommande de consulter [Google Tag Manager](https://marketingplatform.google.com/about/tag-manager/) pour gérer les tags en général, ce que je couvrirai plus tard dans un article de suivi.

**TL;DR** — Si vous voulez passer directement à la solution, [vous pouvez récupérer le code ici](https://github.com/colbyfayock/html-webpack-partials-plugin/tree/master/examples/analytics).

### Pour commencer

Nous voulons commencer avec une configuration de base de Webpack avec HTML Webpack Plugin déjà configuré. Ce guide ne vous guidera pas à travers cette configuration, mais voici quelques points de départ si vous n'êtes pas familier :

* [Guide de démarrage de Webpack](https://webpack.js.org/guides/getting-started/#basic-setup)
* [Guide de Webpack pour HTML Webpack Plugin](https://webpack.js.org/plugins/html-webpack-plugin/)
* Une tonne de tutoriels excellents que vous pouvez trouver en [fouillant un peu sur Google](https://www.google.com/search?q=webpack+html+tutorial)

Enfin, si vous avez déjà un `index.html` configuré, je ne vous jugerai pas pour l'instant, mais j'espère que cela vous inspirera à aborder d'autres extraits de la même manière et à supprimer le besoin d'un fichier `index.html` géré.

#### Installation de Partials for HTML Webpack Plugin

Une fois que vous avez votre configuration de base et HTML Webpack Plugin installé, notre plugin Partials est un ajout facile :

```
yarn add html-webpack-partials-plugin -D
```

_Note : assurez-vous de configurer correctement la dépendance du package en fonction de votre configuration de projet._

#### Configuration de votre partial

Ensuite, nous voulons créer notre partial. Ma préférence pour les gérer généralement est de créer un nouveau répertoire appelé `partials` dans la racine source. Par exemple, si votre point d'entrée se trouve à `src/main.js`, votre répertoire partials serait juste à côté à `src/partials`.

![Image](https://cdn-media-1.freecodecamp.org/images/4DvDYHwNSvfIEj5lOUC5Sqg8llPLLm5HRf-H)

Une fois que vous avez votre emplacement préféré, créons un fichier `analytics.html` dans notre nouveau répertoire partials. Pour l'instant, ajoutons un peu de code de test, pour savoir qu'il fonctionne. Dans `analytics.html` :

```html
<style>
body { background-color: #5F4B8B; }
</style>
```

#### Configuration de votre partial

Ouvrez votre `webpack.config.js` et configurons le partial pour qu'il soit inclus dans notre build.

Tout d'abord, requérez le plugin en haut de votre configuration. Dans `webpack.config.js` :

```
const HtmlWebpackPartialsPlugin = require('html-webpack-partials-plugin');
```

Ensuite, et c'est très important, incluez une nouvelle instance du plugin _APRÈS_ votre instance de `HtmlWebpackPlugin()`. Dans la section plugins de `webpack.config.js` :

```
...
plugins: [
  new HtmlWebpackPlugin(),
  new HtmlWebpackPartialsPlugin({
    path: './path/to/src/partials/analytics.html',
    location: 'head',
    priority: 'high'
  })
...
```

Maintenant, décomposons d'abord cette configuration avant de continuer :

* **path** : c'est ce à quoi cela ressemble, le chemin vers le fichier partial dans notre projet. Assurez-vous de mettre à jour cela avec le bon emplacement pour que le plugin puisse le trouver.
* **location** : la balise HTML que le plugin recherche.
* **priority** : cela détermine si, au moment de la compilation, notre plugin ajoute notre partial au début de la balise `location` spécifiée ou à la fin (ouverture vs. fermeture).

Comme nous l'avons couvert précédemment, nous voulons ajouter cela aussi haut que possible dans le `<head>`. Pour la plupart des balises HTML utilisées dans `location`, Partials l'ajoute juste après la balise d'ouverture si la `priority` est `high`. Mais avec la balise `<head>`, Partials recherche votre balise meta charset et l'injecte immédiatement après, car il est important de rendre cela en premier dans le document.

#### Testons cela

Compilez Webpack, ouvrez votre projet dans votre navigateur, et vous devriez maintenant voir un bel arrière-plan ultraviolet. ?

![Image](https://cdn-media-1.freecodecamp.org/images/P0Nop8w9LQIsmhFtLCkM1gAzHJBxyMGPKsSu)

Si vous regardez le source, vous devriez voir l'extrait ajouté juste après la balise `charset` !

#### Maintenant à Analytics

Mettons à jour notre fichier `analytics.html` pour qu'il ressemble à ceci :

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXXXXX-X"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'UA-XXXXXXXX-X');
</script>
```

Assurez-vous simplement de mettre à jour les IDs (`UA-XXXXXXXX-X`) pour qu'ils correspondent à votre valeur de propriété Google Analytics. Votre extrait Analytics peut également varier en fonction de votre configuration.

Vous devriez maintenant être en mesure de recompiler Webpack et de voir votre page commencer à pinguer Google Analytics ! ?

_Note : vous devrez peut-être charger votre fichier de projet à partir d'un serveur avant que GA ne soit reconnu plutôt que directement depuis votre système de fichiers local._

### Allons un peu plus loin

C'est bien et tout, mais lorsque vous traitez avec Google Analytics, il est agréable d'avoir quelques propriétés différentes, comme une pour le développement et une pour la production. Cela aide à éviter de polluer la propriété de production avec des données de votre équipe de développement (ou vous) qui fouille dans l'application.

#### Configuration des variables de partial

Retournons à notre fichier `webpack.config.js` et configurons une variable pour passer notre ID de propriété :

```
...
plugins: [
  new HtmlWebpackPlugin(),
  new HtmlWebpackPartialsPlugin({
    path: './path/to/src/partials/analytics.html',
    location: 'head',
    priority: 'high',
    options: {
      ga_property_id: 'UA-XXXXXXXX-X'
    }
  })
...
```

Ensuite, mettez à jour votre fichier `analytics.html` pour reconnaître cette valeur. Similaire à HTML Webpack Plugin, Partials utilise [Lodash templating](https://lodash.com/docs/#template) pour faire fonctionner cela. Dans `analytics.html` :

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=<%= ga_property_id %>"></script>
<script> window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', '<%= ga_property_id %>');
</script>
```

Maintenant, compilez à nouveau et profitez !

![Image](https://cdn-media-1.freecodecamp.org/images/2Fk3qpRoO0nD5BKjjE1OItqOB6XTk66STjoT)
_Google Tag Assistant montrant une requête de pageview réussie_

Pour vérifier que votre tag est correctement configuré, je recommande de consulter [Google Tag Assistant](https://chrome.google.com/webstore/detail/tag-assistant-by-google/kejbdjndbnbjgmefkgdddjlbokphdefk?hl=en) disponible sur Chrome.

#### Configuration de cela pour différents IDs de propriété

À partir de là, vous avez quelques options quant à la façon dont vous gérez vos différents IDs de propriété. Vous pouvez :

* Configurer des [configurations Webpack de développement et de production séparées](https://webpack.js.org/guides/production/)
* Créer une configuration d'environnement (ex: `env.config.js`) qui vous permet d'importer les paramètres
* Les deux (recommandé)

Configurer cela de cette manière vous donnera l'opportunité d'exécuter les propriétés dynamiquement entre vos builds de développement local et de production. N'oubliez pas de ne pas stocker votre fichier env dans git si vous allez ajouter des données sensibles. ?

### Alors, qu'est-ce que nous obtenons de cela ?

Le scénario idéal est que vous preniez cela et que vous l'utilisiez pour le reste de votre HTML vivant dans `index.html`. Cela aide à diviser votre code en morceaux plus gérables et laisse Webpack générer le fichier pour vous plutôt que d'essayer de le remplacer et de le gérer vous-même.

Spécifiquement pour Google Analytics, nous avons quelques avantages :

* Assurer que l'extrait se charge à un emplacement fiable
* Fournir une manière plus raisonnable de maintenir l'extrait lui-même
* Gérer votre ID de propriété via votre configuration Webpack
* Et en bonus : le charger comme une variable d'environnement via votre configuration Webpack

Pour voir la solution complète avec un exemple de code, [consultez l'exemple dans le dépôt GitHub.](https://github.com/colbyfayock/html-webpack-partials-plugin/tree/master/examples/analytics)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f3a8 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e8f3fb Inscription à ma newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.colbyfayock.com/2018/08/reliable-and-maintainable-google-analytics-in-webpack](https://www.colbyfayock.com/2018/08/reliable-and-maintainable-google-analytics-in-webpack)._