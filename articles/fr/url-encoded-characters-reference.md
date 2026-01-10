---
title: Référence des caractères encodés en URL HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T21:50:00.000Z'
originalURL: https://freecodecamp.org/news/url-encoded-characters-reference
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d67740569d1a4ca3792.jpg
tags:
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
- name: url
  slug: url
seo_title: Référence des caractères encodés en URL HTML
seo_desc: 'A URL is an address for a website. Just like postal addresses have to follow
  a specific format to be understood by the postman, URLS have to follow a format
  to be understood and get you to the right location.

  There are only certain characters that ar...'
---

Une URL est une adresse pour un site web. Tout comme les adresses postales doivent suivre un format spécifique pour être comprises par le facteur, les URL doivent suivre un format pour être comprises et vous amener au bon endroit.

Il n'y a que certains caractères qui sont autorisés dans la chaîne d'URL, les caractères alphabétiques, les chiffres et quelques caractères `; , / ? : @ & = + $ - _ . ! ~ * ' ( ) #` qui peuvent avoir des significations spéciales.

## Caractères réservés

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.55.13-PM.png)

## Encodage

Tout caractère qui n'est pas un caractère alphabétique, un nombre ou un caractère réservé utilisé doit être encodé.

Les URL utilisent le jeu de caractères ASCII ("American Standard Code for Information Interchange") et donc l'encodage doit être dans un format ASCII valide.

Il existe des fonctions dans la plupart des langages web pour effectuer cet encodage pour vous, par exemple en JavaScript `encodeURI()` et en PHP `rawurlencode()`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.57.33-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.57.53-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.06-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.18-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.32-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.43-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.58.57-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.07-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.18-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.27-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.46-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-25-at-1.59.55-PM.png)

### Exemple :

```js
encodeURI("Free Code Camp");
// Free%20Code%20Camp
```