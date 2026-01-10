---
title: Comment créer une barre de navigation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T22:31:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-navigation-bar
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9db9740569d1a4ca394d.jpg
tags:
- name: CSS
  slug: css
- name: toothbrush
  slug: toothbrush
seo_title: Comment créer une barre de navigation
seo_desc: 'Navigation Bars

  Navigation bars are a very important element to any website. They provide the main
  method of navigation by providing a main list of links to a user. There are many
  methods to creating a navigation bar. The easiest way to create a navi...'
---

## **Barres de navigation**

Les barres de navigation sont un élément très important pour tout site web. Elles fournissent la méthode principale de navigation en offrant une liste principale de liens à un utilisateur. Il existe de nombreuses méthodes pour créer une barre de navigation. La manière la plus simple de créer une barre de navigation est d'utiliser une liste non ordonnée et de la styliser avec CSS.

Les barres de navigation sont principalement composées de listes `<ul>` qui sont disposées horizontalement et stylisées.

Lors du stylisme des barres de navigation, il est courant de supprimer l'espacement supplémentaire créé par les balises `<ul>` et `<li>` ainsi que les puces qui sont automatiquement insérées :

```css
list-style-type: none;
margin: 0px;
padding: 0px;

```

**Exemple :**

Il y a deux parties à toute navigation : le HTML et le CSS. Ceci est juste un exemple rapide.

```html
<!-- N'importe quel élément peut être utilisé ici -->
<nav class="myNav">
  <ul>
    <li><a href="index.html">Accueil</a></li>
    <li><a href="about.html">À propos</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>

```

```css
/* Définir le bloc de navigation principal */
.myNav {
  display: block;
  height: 50px;
  line-height: 50px;
  background-color: #333;
}

/* Supprimer les puces, la marge et le remplissage */
.myNav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.myNav li {
  float: left; /* Ou vous pouvez utiliser display: inline; */
}

/* Définir le style de bloc pour les liens */
.myNav li a {
  display: inline-block;
  text-align: center;
  padding: 14px 16px;
}

/* Ceci est optionnel, cependant si vous voulez afficher le 
lien actif différemment, appliquez un fond à celui-ci */
.myNav li a.active {
  background-color: #3786e1;
}

