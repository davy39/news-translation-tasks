---
title: Guide de Semantic UI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-03T23:06:00.000Z'
originalURL: https://freecodecamp.org/news/semantic-ui-guide
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e39740569d1a4ca3bfd.jpg
tags:
- name: Front-end Development
  slug: front-end-development
- name: HTML
  slug: html
seo_title: Guide de Semantic UI
seo_desc: 'What is Semantic UI?

  Semantic UI is a front-end development framework similar to bootstrap designed for
  theming. It contains pre-built semantic components that helps create beautiful and
  responsive layouts using human-friendly HTML.

  According to the ...'
---

## **Qu'est-ce que Semantic UI ?**

Semantic UI est un framework de développement front-end similaire à Bootstrap, conçu pour le théming. Il contient des composants sémantiques pré-construits qui aident à créer des mises en page belles et réactives en utilisant du HTML convivial.

Selon le site web de Semantic UI, le framework utilise du HTML concis, du JavaScript intuitif et un débogage simplifié pour rendre le développement front-end une expérience amusante et agréable.

Et il s'intègre avec React, Angular, Meteor, Ember et de nombreux autres frameworks pour aider à organiser la couche UI aux côtés de la logique applicative.

### Historique des versions de Semantic UI

La première pré-version est apparue sur GitHub en septembre 2013, créée par [Jack Lukic](https://github.com/jlukic).

Semantic UI `1.x` a été publié pour la première fois en novembre 2014 avec des changements majeurs par rapport aux pré-versions précédentes.

Semantic UI `2.x` a été publié pour la première fois en juin 2015 et a introduit une nouvelle interface utilisateur, plusieurs corrections de bugs, améliorations et améliorations du thème par défaut.

### Support des navigateurs par Semantic UI

La version actuelle `2.2.x` supporte les navigateurs suivants :

* Les 2 dernières versions de FF, Chrome, Safari Mac
* IE 11+
* Android 4.4+, Chrome pour Android 44+
* iOS Safari 7+
* Microsoft Edge 12+

## Comment installer Semantic UI

Il existe plusieurs façons d'installer Semantic UI, voici quelques-unes des méthodes les plus simples :

### Via un réseau de diffusion de contenu (CDN)

C'est de loin la méthode la plus facile pour les débutants. Créez un fichier HTML comme suit :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Semantic UI</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.13/semantic.min.css">
    <!-- Ajoutez votre feuille de style personnalisée ici -->
  </head>
  <body>
  
    <!-- Écrivez votre code HTML ici -->
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.13/semantic.min.js"></script>
  </body>
</html>
```

`NOTE :` Le lien CDN ci-dessus à la ligne 5 inclura tous les composants disponibles dans Semantic UI. Si vous souhaitez installer un composant spécifique, [cliquez ici](https://cdnjs.com/libraries/semantic-ui) pour voir son lien CDN respectif.

### Utilisation des outils de construction

Cela suppose que vous utilisez le système d'exploitation Ubuntu Linux avec `node` et `npm` installés. Pour les autres systèmes d'exploitation, [cliquez ici](https://semantic-ui.com/introduction/getting-started.html).

Dans votre répertoire de projet, installez gulp globalement en utilisant npm :

```text
npm install -g gulp
```

Installez Semantic UI :

```text
npm install semantic-ui --save
cd semantic/
gulp build
```

Incluez dans le HTML :

```html
<link rel="stylesheet" type="text/css" href="semantic/dist/semantic.min.css">
<script src="https://code.jquery.com/jquery-3.1.1.min.js" integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>
<script src="semantic/dist/semantic.min.js"></script>
```

Mise à jour via npm :

```text
npm update
```

### Intégration avec d'autres frameworks

Vous pouvez intégrer Semantic UI avec d'autres frameworks de développement front-end comme React, Angular, Ember ou Meteor. [Cliquez ici](https://semantic-ui.com/introduction/integrations.html) pour plus d'informations et d'instructions d'intégration.

### Plus d'informations sur Semantic UI :

Semantic UI dispose d'une documentation complète et très bien organisée qui vous permettra de démarrer en un rien de temps. Les liens suivants seront utiles dans votre parcours avec Semantic UI.

* [Site web de Semantic UI](https://semantic-ui.com/)
* [Commencer avec Semantic UI](https://semantic-ui.com/introduction/getting-started.html)
* [Modèles Semantic UI](https://semantic-ui.com/usage/layout.html#pages)
* [Personnalisation et création de thèmes Semantic UI](http://learnsemantic.com/)