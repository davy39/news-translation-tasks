---
title: Comment remplacer jQuery par Vue.js dans les applications Ruby on Rails
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T19:21:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-replace-jquery-with-vue-js-in-ruby-on-rails-apps-b4f4af192635
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VIrASrMWiySHstjaQwF4GA.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Ruby on Rails
  slug: ruby-on-rails
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment remplacer jQuery par Vue.js dans les applications Ruby on Rails
seo_desc: 'By Igor Petrov

  If you are a Ruby on Rails developer and have been for several years, you’re probably
  used to using jQuery as the default option for developing the front end. Several
  versions ago, core Rails developers offered it as a standard, and in...'
---

Par Igor Petrov

Si vous êtes un développeur **Ruby on Rails** depuis plusieurs années, vous êtes probablement habitué à utiliser **jQuery** comme option par défaut pour développer le front-end. Il y a plusieurs versions de cela, les développeurs principaux de **Rails** l'ont proposé comme standard, et avec le temps, il est devenu le standard. **jQuery** était la bibliothèque **JavaScript** n°1, et il était très pratique de l'utiliser.

Depuis lors, beaucoup de temps a passé, mais **jQuery** reste l'option par défaut. Cependant, vous avez maintenant besoin de quelque chose de différent en raison de la complexité croissante du code côté client. Vous pourriez essayer React, Angular.js ou Vue.js, mais vous ne pouvez utiliser facilement qu'un seul de ceux-ci tout en faisant le moins d'efforts pour l'intégrer dans une application existante ou nouvelle.

J'ai utilisé **jQuery** pendant longtemps et cela est devenu une habitude : si vous commencez une nouvelle application **Rails**, **jQuery** est déjà là. Vous le connaissez déjà, alors vous commencez à l'utiliser immédiatement.

Il y a plusieurs années, j'ai découvert que j'aimais **Angular 1**, car il était très simple de commencer. Mais il avait encore une configuration redondante avec l'initialisation de l'application, l'écriture de contrôleurs et l'injection de dépendances.

C'est génial pour architecturer votre application avec une approche MVC (MVVM).

Mais disons que vous avez une application existante avec beaucoup de code de manipulation DOM **jQuery**, et que vous voulez commencer à remplacer ce désordre par quelque chose de plus supportable. Quelque chose comme ce qui suit (qui pourrait être optimisé, bien sûr — mais c'est pour l'exemple) :

```
$(document).ready(function(){
```

```
   ...   $('#some-radio-button1').on('click', function(){     if ($(this).is(':checked')) {       // suppression des classes "active", masquage de certains blocs       // affichage du bloc lié
```

```
     } else {
```

```
       // opposé à ci-dessus     }   });
```

```
});
```

### Pourquoi Vue.js ?

Alors, pourquoi recommandé-je de remplacer le code **jQuery** par **Vue.js** ? Parce que **Vue.js** n'est pas seulement utile pour écrire des applications **JavaScript** complexes. Vous pouvez également l'utiliser pour une seule tâche simple, comme la manipulation du DOM. Si c'est tout ce dont vous avez besoin, il serait bon d'opter pour **Vue**. Et vous pouvez aller plus loin avec lui si vous devez résoudre des tâches plus complexes comme le routage, la gestion d'état, etc.

Donc, si vous avez déjà un projet avec beaucoup de code **jQuery** et que vous souhaitez vous débarrasser de ces gestionnaires d'événements désordonnés, vous devriez définitivement essayer **Vue.js**.

#### Pour commencer

Si vous êtes un développeur RoR de la vieille école et que vous gérez toujours les assets via **Sprockets**, téléchargez simplement et placez `vue.js` dans votre dossier `vendor/assets/javascripts`.

Ensuite, requérez-le depuis votre fichier manifest principal **JavaScript** (par exemple, `application.js`) :

```
//= require jquery//= require jquery_ujs//= require bootstrap//= require vue
```

Ensuite, vous devez instancier une instance **Vue** et l'attacher à un élément dans votre code **HTML**. À cette fin, vous pourriez créer un fichier `vue_app.js` (ou .coffee) séparé à l'intérieur de `app/assets/javascripts` :

```
window.vueApp = new Vue  el: '.off-canvas-container'  data:    ...
```

C'est tout, maintenant vous pouvez utiliser **Vue.js** !

### Aller plus loin

Maintenant, vous pouvez ajouter des données à la section `data` de votre instance **Vue** et écrire quelques gestionnaires dans la section `methods`. Mais il est préférable d'utiliser une unité principale de **Vue.js** : les composants.

La manière la plus simple de continuer avec **Vue.js** est d'utiliser vos vues **Rails** existantes et d'envelopper certains morceaux de **HTML** dans des composants. Voyons comment y parvenir.

Par exemple, j'ai `app/views/sellers/print_labels/new.html.erb` et un certain code **jQuery** associé à cette page :

![Image](https://cdn-media-1.freecodecamp.org/images/oby6k46mOkZzmsrhymr5Z3AMPwop2tCmKNiW)

![Image](https://cdn-media-1.freecodecamp.org/images/YDQsGEOpcQdAEpWCJQaJVPWKjkzUQbbwKCFx)

Il s'agit d'un formulaire d'adresse de livraison avec des champs désactivés par défaut. Une fois que l'utilisateur clique sur l'icône "crayon", les champs du formulaire deviennent des entrées accessibles et le bouton "Enregistrer" est affiché. Une fois "Enregistrer" cliqué, le formulaire revient à son état initial.

Pour remplacer ce code **jQuery** par des composants **Vue.js** simples, je crée `app/assets/javascripts/components/print_labels.coffee` avec quelque chose comme ce qui suit (mais n'oubliez pas de requérir votre dossier `components` depuis `application.js`) :

```
Vue.component 'print-labels',  data: ->    isEditingAddress: false
```

Et ensuite, je l'utilise dans ma vue **Rails** :

![Image](https://cdn-media-1.freecodecamp.org/images/83yq--rKhJDGBRFhsqy8LHTbZ3G2FRrG3Zcp)

Plusieurs choses à noter :

* Si vous souhaitez conserver le modèle de composant à l'intérieur des vues ou des partials Rails, vous devez utiliser l'option `inline-template`.
* L'option `v-cloak` est nécessaire pour afficher le composant après qu'il a été initialisé et rendu.
* Nous utilisons `@click` pour attacher les gestionnaires d'événements `onclick` (vous pouvez extraire le code complexe vers les `methods` du composant).

Maintenant, nous pouvons nous débarrasser du code **jQuery** car nous l'avons remplacé par un petit composant **Vue.js** (avec seulement une variable de données !).

Maintenant, c'est à vous ! Allez-y avec cette approche, et j'espère que vous vous retrouverez bientôt heureux avec **Vue.js**.

*Si vous avez aimé cet article, cliquez sur* 👋 *pour le partager.*