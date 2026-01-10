---
title: Comment ajouter JavaScript à votre application Rails 6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-10T16:04:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-javascript-to-your-rails-6-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/carl-heyerdahl-KE0nC8-58MQ-unsplash--1-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Rails
  slug: rails
seo_title: Comment ajouter JavaScript à votre application Rails 6
seo_desc: "By Daniel Wesego\nAs a junior Full-Stack developer, my main focus was the\
  \ backend. I wanted to learn how to program my backend server to serve my web application.\
  \ \nBut after learning the basics of the the backend, I learned that the frontend\
  \ was just ..."
---

Par Daniel Wesego

En tant que développeur Full-Stack junior, mon principal objectif était le backend. Je voulais apprendre à programmer mon serveur backend pour servir mon application web. 

Mais après avoir appris les bases du backend, j'ai compris que le frontend était tout aussi important que le backend. Et une façon d'augmenter l'interactivité de votre application web est d'ajouter JavaScript.

JavaScript est essentiel pour ajouter de l'interactivité à votre application web. Bien sûr, il est devenu bien plus que cela maintenant. C'est un langage de programmation que les navigateurs web exécutent. De nombreux sites web que vous avez visités utilisent du code JavaScript dans leur frontend. 

Vous avez peut-être commencé à utiliser Ruby on Rails pour construire votre application web et vous vous êtes demandé comment ajouter JavaScript à votre code. Dans cet article, je vais vous montrer comment ajouter du code JavaScript à votre application Rails.

## Pourquoi JavaScript ?

Vous vous demandez peut-être pourquoi vous avez besoin de JavaScript dans votre application web en premier lieu. En bref, si vous n'incluez aucun JS, alors l'expérience utilisateur de votre application web ne sera pas bonne.

Supposons que vous avez un formulaire qu'un utilisateur remplit et que vous souhaitez faire une validation de formulaire. Si l'utilisateur soumet le formulaire sans remplir les valeurs appropriées, la page du formulaire doit se recharger, ce qui sollicite le serveur et revient pour l'utilisateur. Cela prend beaucoup de temps et risque de frustrer l'utilisateur.

Bien sûr, vous pouvez parfois vous en sortir avec la validation de formulaire HTML, mais ce n'est pas toujours possible. Ajouter un simple script qui vérifie les entrées de l'utilisateur et les informe qu'ils doivent saisir les informations correctes est bien mieux.

Bien sûr, cela ne signifie pas que vous pouvez ignorer la validation côté serveur, mais c'est pour un autre article.

Un autre cas d'utilisation est le chargement de fichiers de manière asynchrone, que vous pouvez faire en JavaScript sans recharger toute la page. Vous avez peut-être utilisé certaines applications web qui chargent plus d'images et d'articles à mesure que vous faites défiler vers le bas sans avoir à actualiser ou changer de page encore et encore.

Ces cas d'utilisation et d'autres sont de bonnes raisons d'utiliser JavaScript dans votre application. En fait, la demande pour JavaScript a été en augmentation. Vous pouvez même l'utiliser pour écrire votre backend. 

Mais nous aimons Rails, alors nous allons continuer à l'utiliser pendant un certain temps. 

## Ce que nous allons couvrir ici

Au moment de la rédaction, la dernière version du framework est Rails 6, et elle a apporté quelques changements à la façon dont vous interagissez avec JavaScript. 

Avant Rails 6, nous avions l'asset pipeline pour gérer les fichiers CSS et JavaScript. Mais à partir de Rails 6, Webpacker est le compilateur par défaut pour JavaScript. CSS est toujours géré par l'asset pipeline, mais vous pouvez également utiliser Webpack pour compiler CSS. 

Vous ne trouverez pas votre dossier JavaScript au même endroit que dans Rails 5. La structure de répertoire pour JavaScript a changé pour le dossier **app/javascript/packs/**.

Dans ce dossier, vous trouverez le fichier **application.js**, qui est similaire au fichier **application.css**. Il sera importé par défaut dans le fichier **application.html.erb** lorsque vous créerez votre nouvelle application Rails. 

Le fichier **application.html.erb** sera utilisé par toutes les vues. 

## Ajout d'un script qui sera utilisé par toutes les vues

Si vous souhaitez que votre JavaScript soit disponible dans toutes les vues ou pages, vous pouvez simplement le mettre dans le fichier **application.js** :

```js
require("@rails/ujs").start()
require("turbolinks").start()
require("@rails/activestorage").start()
require("channels")

console.log('Bonjour depuis application.js')
```

Les quatre premières lignes sont là par défaut. J'ai ajouté une instruction `console.log` pour vous montrer que le JavaScript sera disponible partout. 

Vous pouvez tester cela en visualisant n'importe quelle page de votre application et en ouvrant la console de développement. 

Mais vous ne voulez peut-être pas que votre code JavaScript soit chargé sur chaque page. Au lieu de cela, vous pouvez rendre le script disponible uniquement lors de la visite d'une page spécifique.

## Ajout d'un script qui sera utilisé par un fichier spécifique

Si vous souhaitez que votre JavaScript soit disponible pour une vue spécifique uniquement, vous pouvez utiliser **javascript_pack_tag** pour importer ce fichier spécifique :

```html.erb
<h1 class='text-center'>Je veux mon JS ici uniquement</h1>

<%= javascript_pack_tag 'my_js' %>

```

```js
console.log('Bonjour depuis Mon JS')
```

N'oubliez pas que vous devez ajouter le fichier dans le répertoire **packs**. Le **javascript_pack_tag** doit également faire référence au nom du fichier JavaScript que vous avez créé. 

Maintenant, le script ne s'exécutera que lorsque la vue spécifique qui inclut le **javascript_pack_tag** sera chargée dans le navigateur.

## Conclusion

J'espère que cet article aide à clarifier toute confusion que vous pourriez avoir lors de la mise à jour de votre application vers Rails 6, ou si vous venez de commencer avec Rails. 

Vous pouvez me suivre sur [Github](https://github.com/DanielMitiku) si vous souhaitez en apprendre davantage.