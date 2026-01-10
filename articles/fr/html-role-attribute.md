---
title: Attribut Role HTML Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-13T20:05:00.000Z'
originalURL: https://freecodecamp.org/news/html-role-attribute
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9de7740569d1a4ca3a4b.jpg
tags:
- name: HTML
  slug: html
seo_title: Attribut Role HTML Expliqué
seo_desc: 'The role attribute describes the role of an element in programs that can
  make use of it, such as screen readers or magnifiers.

  Usage Example:

  <a href="#" role="button">Button Link</a>


  Screen Readers will read this element as “button” instead of “lin...'
---

L'attribut `role` décrit le rôle d'un élément dans les programmes qui peuvent l'utiliser, tels que les lecteurs d'écran ou les loupes.

Exemple d'utilisation :

```html
<a href="#" role="button">Lien Bouton</a>
```

Les lecteurs d'écran liront cet élément comme « bouton » au lieu de « lien ».

Il existe quatre catégories de rôles :

* Rôles Abstraits
* Rôles de Widget
* Rôles de Structure de Document
* Rôles de Repère

## Plus d'informations sur les attributs HTML :

[Attribut <script src>](https://guide.freecodecamp.org/html/attributes/script-src-attribute/)

[Attribut <a href>](https://guide.freecodecamp.org/html/attributes/a-href-attribute/)

[Attribut <a target>](https://guide.freecodecamp.org/html/attributes/a-target-attribute/)

[Attribut <body background>](https://guide.freecodecamp.org/html/attributes/body-background-attribute/)

[Attribut <p align>](https://guide.freecodecamp.org/html/attributes/p-align-attribute/)

[Attribut <img src>](https://guide.freecodecamp.org/html/attributes/img-src-attribute/)

[Attribut <font>](https://guide.freecodecamp.org/html/attributes/font-color-attribute/)

## Plus d'informations sur les attributs HTML

Les éléments HTML peuvent avoir des attributs, qui contiennent des informations supplémentaires sur l'élément.

Les attributs HTML viennent généralement en paires nom-valeur et se placent toujours dans la balise d'ouverture d'un élément. Le nom de l'attribut indique le type d'information que vous fournissez sur l'élément, et la valeur de l'attribut est l'information réelle.

Par exemple, un élément d'ancrage (`<a>`) dans un document HTML crée des liens vers d'autres pages ou d'autres parties de la page. Vous utilisez l'attribut `href` dans la balise d'ouverture `<a>` pour indiquer au navigateur où le lien envoie un utilisateur.

Voici un exemple de lien qui envoie les utilisateurs vers la page d'accueil de freeCodeCamp :

```html
<a href="www.freecodecamp.org">Cliquez ici pour aller à freeCodeCamp !</a>
```

Remarquez que le nom de l'attribut (`href`) et la valeur (« www.freecodecamp.org ») sont séparés par un signe égal, et des guillemets entourent la valeur.

Il existe de nombreux attributs HTML différents, mais la plupart ne fonctionnent que sur certains éléments HTML. Par exemple, l'attribut `href` ne fonctionnera pas s'il est placé dans une balise d'ouverture `<h1>`.

Dans l'exemple ci-dessus, la valeur fournie à l'attribut `href` pourrait être n'importe quel lien valide. Cependant, certains attributs n'ont qu'un ensemble d'options valides que vous pouvez utiliser, ou les valeurs doivent être dans un format spécifique. L'attribut `lang` indique au navigateur la langue par défaut du contenu dans un élément HTML. Les valeurs pour l'attribut `lang` doivent utiliser des codes de langue ou de pays standard, tels que `en` pour l'anglais ou `it` pour l'italien.

## **Attributs Booléens**

Certains attributs HTML n'ont pas besoin de valeur car ils n'ont qu'une seule option. Ce sont les attributs booléens. La présence de l'attribut dans une balise l'appliquera à cet élément HTML. Cependant, il est possible d'écrire le nom de l'attribut et de le définir égal à la seule option de la valeur. Dans ce cas, la valeur est généralement la même que le nom de l'attribut.

Par exemple, l'élément `<input>` dans un formulaire peut avoir un attribut `required`. Cela oblige les utilisateurs à remplir cet élément avant de pouvoir soumettre le formulaire.

Voici des exemples qui font la même chose :

```html
<input type="text" required >
<input type="text" required="required" >
```