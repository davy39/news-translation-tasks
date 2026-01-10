---
title: "Symbole Point \x13 Puce en HTML Unicode"
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-14T00:45:10.000Z'
originalURL: https://freecodecamp.org/news/dot-symbol-bullet-point-in-html-unicode
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/bullet.png
tags:
- name: HTML
  slug: html
- name: unicode
  slug: unicode
seo_title: "Symbole Point \x13 Puce en HTML Unicode"
seo_desc: 'In your HTML documents, you''ll often need to make a list of items. And
  you can use bullet points for this purpose.

  You can show bullet points with the Unicode character (or entity) for bullet points.

  In this article, I will show you the Unicode and H...'
---

Dans vos documents HTML, vous aurez souvent besoin de créer une liste d'éléments. Et vous pouvez utiliser des puces à cet effet.

Vous pouvez afficher des puces avec le caractère Unicode (ou entité) pour les puces.

Dans cet article, je vais vous montrer les entités Unicode et HTML pour afficher des puces sur une page web.

Vers la fin de cet article, je vais également vous montrer les combinaisons de 5 touches avec lesquelles vous pouvez taper un grand symbole de point.

## Les entités Unicode et HTML pour les puces
Le caractère Unicode pour afficher le symbole de point ou la puce est `U+2022`.

Mais pour utiliser correctement ce caractère Unicode, retirez le `U+` et remplacez-le par un esperluette (`&`), un signe dièse (`#`), et `x`. Ensuite, tapez le nombre 2022, et ajoutez un point-virgule. Ainsi, cela devient `&#x2022;`.

Cela ressemblera à ceci :
```html
<h1>Langages du web</h1>
<h3>&#x2022; HTML</h3>
<h3>&#x2022; CSS</h3>
<h3>&#x2022; JavaScript</h3>
<h3>&#x2022; PHP</h3>
```
![ss1-2](https://www.freecodecamp.org/news/content/images/2022/04/ss1-2.png)

En plus du caractère Unicode `&#x2022;`, vous pouvez également utiliser les entités HTML `&bull;` et `&#8226;` pour afficher des puces ou des symboles de point sur la page web.

```html
<h1>Langages du web</h1>
<h3>&#8226; HTML</h3>
<h3>&bull; CSS</h3>
<h3>&#8226; JavaScript</h3>
<h3>&bull; PHP</h3>
```
Le résultat reste le même :
![ss2-4](https://www.freecodecamp.org/news/content/images/2022/04/ss2-4.png)

## Le raccourci clavier pour taper un symbole de point
Pour taper le symbole de point sur votre clavier, activez le pavé numérique en appuyant sur `NumLk`, maintenez `Alt` et appuyez sur les touches `0`, `1`, `4`, et `9` successivement.

Si vous ne tapez pas les nombres avec le pavé numérique, le symbole de point ne s'affichera pas.

Merci d'avoir lu !