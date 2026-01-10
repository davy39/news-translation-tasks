---
title: Comment installer TinyMCE dans votre application Rails en utilisant Webpack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-19T07:08:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-tinymce-in-your-rails-app-using-webpack-edf030915332
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5d_eDFKTmlTdYafG9dahdw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Rails
  slug: rails
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
- name: webpack
  slug: webpack
seo_title: Comment installer TinyMCE dans votre application Rails en utilisant Webpack
seo_desc: 'By Joanna Gaudyn

  The popularity of using Webpack to deal with your assets in Rails is steadily increasing.
  Getting started is really straightforward. If you are starting a new app, you simply
  run rails new my_app --webpack and Rails takes care of the...'
---

Par Joanna Gaudyn

La popularité de l'utilisation de Webpack pour gérer vos assets dans Rails ne cesse de croître. Commencer est vraiment simple. Si vous démarrez une nouvelle application, vous exécutez simplement `rails new my_app --webpack` et Rails s'occupe du reste.

Grâce au [gem webpacker](https://github.com/rails/webpacker), ajouter Webpack à votre application existante est également assez simple. Vous ajoutez le gem à votre Gemfile, faites un bundle, et enfin installez webpacker :

```
gem 'webpacker', '~> 3.5'bundlebundle exec rails webpacker:install
```

C'est plutôt génial. Maintenant, tout ce que vous avez à faire est de lier votre pack JavaScript et le CSS importé dans celui-ci dans le head de votre `application.html.haml` :

```
<%= javascript_pack_tag 'application' %> <!-- js from app/javascript/packs/application.js -->
```

```
<%= stylesheet_pack_tag 'application' %> <!-- CSS importé via Webpack -->
```

Une fois cela fait, vous êtes prêt à écrire votre code JavaScript moderne et à utiliser toutes les grandes bibliothèques disponibles.

### Qu'est-ce que TinyMCE ?

TinyMCE est un éditeur de texte riche dans le cloud. Pour faire simple, c'est comme Word qui peut être intégré dans votre application.

Le projet sur lequel je travaille l'utilise pour permettre aux administrateurs de modifier le contenu de la page d'accueil. Grâce à TinyMCE, il n'est pas nécessaire de construire une interface d'administration séparée à cet effet. Mais l'utilisation de l'éditeur peut être beaucoup plus polyvalente. Pensez, par exemple, à ce que Wordpress ou Evernote vous permet de faire grâce à leurs outils intégrés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lUWdaoq0bkq3vDCrlzn4zQ.png)
_Exemple d'utilisation de TinyMCE. Le pouvoir est maintenant entre les mains de l'utilisateur._

### Utilisation via CDN

Nous avons initialement implémenté l'éditeur via CDN (par exemple, en liant le script dans le head de notre `application.html.haml`) comme ceci :

```
!!!%html  %head    %meta ... <!-- some meta content -->    %title ... <!-- MyApp -->    = csrf_meta_tags
```

```
    %script{src: 'https://cloud.tinymce.com/stable/tinymce.min.js?apiKey=gexncjni90zx3qf0m5rr7kl8l40wd5yuly2xjza0g3kwrljt'}    = stylesheet_link_tag 'application', media: 'all'    = javascript_include_tag 'application'  %body    <!-- the usual body stuff -->
```

Cela nécessitait d'ajouter un fichier avec notre fonction personnalisée dans `app/assets/javascript/tinyMce.js`. Notez que nous utilisons également jQuery.

```
$( document ).on('turbolinks:load', function() {
```

```
    tinyMCE.init({         selector: 'textarea.tinymce',             // quelques autres paramètres, comme la hauteur, la langue,         // l'ordre des boutons sur votre barre d'outils, etc.             plugins: [            'table', 'lists' // les plugins que vous souhaitez ajouter        ]    });});
```

En plus de cela, nous avons dû inclure un [fichier de traduction](https://www.tiny.cloud/download/language-packages/) (ce qui n'est pas nécessaire si vous utilisez l'anglais dans votre application). Pour que tout s'affiche correctement en production, vous aurez également besoin d'obtenir une clé API [Tiny Cloud](https://apps.tiny.cloud/signup/) gratuite.

### Webpack et TinyMCE

Tout fonctionnait très bien pendant quelques mois, mais nous avons décidé qu'il était temps de passer à Webpack.

Webpack est censé faciliter votre vie et, couplé avec yarn, vous permet de vous concentrer sur l'essentiel. Supposons que vous souhaitiez utiliser le package A. Il se trouve que le package A dépend des packages B et C. Et le package B dépend de D, E et F. Plutôt que de passer des heures à déterminer quelles sont les dépendances et à les installer individuellement, ce que vous voulez, c'est dire `yarn add package-A`, et laisser tout cela se faire pour vous. Et c'est _presque_ le cas.

Cette transition, en ce qui concerne TinyMCE, a été bien plus douloureuse qu'elle n'aurait dû l'être. Et c'est pourquoi j'ai décidé d'écrire cet article. J'espère qu'il fera gagner du temps et éviter des frustrations à quelqu'un.

**Si vous aviez précédemment implémenté TinyMCE via CDN**, vous aimeriez vous débarrasser de certaines choses, pour repartir sur de bonnes bases. Supprimez le lien du script de `application.html.haml`. Ensuite, commentez le contenu du fichier `tinyMce.js` (et le fichier de langue si vous en utilisez un). J'ai également décidé de me débarrasser de la dépendance jQuery (dans notre cas, cela signifiait supprimer `gem 'jquery-rails'` du Gemfile, et dans le fichier `app/assets/javascripts/application.js`, supprimer `//= require jquery` et remplacer `//= require jquery_ujs` par `//= require rails-ujs`).

Note : Procédez avec prudence si vous avez d'autres bibliothèques externes dans votre projet qui dépendent de jQuery (par exemple, Bootstrap ou Select2). En fin de compte, votre objectif serait probablement de déplacer toutes ces bibliothèques vers Webpack, mais plus le projet est grand, plus cette tâche peut être complexe, alors gardez cela à l'esprit. Rien ne vous empêche de conserver votre implémentation traditionnelle en parallèle avec celle de Webpack. Dans ce cas, je recommanderais toujours de la commenter pendant l'implémentation de TinyMCE.

Toutes ces étapes garantiront que les choses que nous implémenterons à partir de maintenant fonctionnent, et que l'ancienne implémentation ne sert pas de solution de repli.

#### **Étape 1. Si vous souhaitez utiliser jQuery via Webpack**

Ajouter jQuery via Webpack est aussi simple que d'exécuter `yarn add jquery` et d'ajouter le code suivant à `config/webpack/environment.js` :

```
const { environment } = require('@rails/webpacker')const webpack = require('webpack')environment.plugins.prepend('Provide',  new webpack.ProvidePlugin({    $: 'jquery',    jQuery: 'jquery'  }))module.exports = environment
```

#### **Étape 2. Obtenez le package TinyMCE**

Cela est également assez simple : exécutez `yarn add tinymce`.

Ensuite, créez un nouveau fichier où nous placerons notre fonction. J'ai terminé avec `app/javascript/vendor/tinyMce.js` avec le contenu suivant :

```
import tinymce from 'tinymce/tinymce';import 'tinymce/themes/modern/theme';import 'tinymce/plugins/table';import 'tinymce/plugins/lists';
```

```
function tinyMce() {    tinymce.init({        selector: 'textarea.tinymce',
```

```
        // quelques autres paramètres, comme la hauteur, la langue,         // l'ordre des boutons sur votre barre d'outils, etc.
```

```
        plugins: [            'table', 'lists'        ]    });}
```

```
// si vous utilisez un fichier de langue, vous pouvez placer son contenu ici
```

```
export { tinyMce };
```

#### **Étape 3. Importez tout dans `application.js`**

Nous pouvons importer notre fonction comme suit :

`import { tinyMce } from "../vendor/tinyMce";`

et ensuite l'appeler :

```
document.addEventListener("turbolinks:load", function () {    tinyMce(); });
```

Comme vous pouvez le voir, nous avons également remplacé le code jQuery par ES6.

#### **Étape 4. Faites fonctionner le skin de TinyMCE**

Si vous exécutez votre `webpack-dev-server` et `rails s`, vous pourriez être surpris de constater que votre éditeur de texte n'est pas là. Un coup d'œil dans la console et vous verrez l'erreur suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fCntK4ZDJtVxvGobG4V0oA.png)

C'est parce que TinyMCE ne fonctionnera pas sans un skin, et le tirer via Webpack nécessite son importation explicite. Nous pouvons faire cela en incluant cette ligne dans notre fichier `tinyMce.js`, juste après les autres instructions d'importation. Le chemin est relatif au dossier `node_modules` :

```
import 'tinymce/skins/lightgray/skin.min.css';
```

**À ce stade, votre éditeur devrait fonctionner.**

Mais... si vous regardez dans la console, vous pourriez être déçu de voir que vous avez toujours 2 erreurs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*uOpqUB3N2qAIzuDH1zRNOw.png)

Ne désespérez pas ! Il existe une solution facile. Ajoutez simplement `skin: false` à votre configuration `function tinyMce()` et cela devrait faire l'affaire. Cela empêchera les fichiers par défaut de se charger.

Félicitations ! Vous venez de faire fonctionner votre TinyMCE !