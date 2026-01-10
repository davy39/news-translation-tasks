---
title: Éléments de bloc et éléments en ligne en HTML - Explications
date: '2020-02-08T23:08:00.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/inline-elements-and-block-elements-in-html-explained
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cad740569d1a4ca338e.jpg
tags:
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: toothbrush
  slug: toothbrush
seo_desc: 'Block and Inline Elements

  Let''s understand block and inline elements using the below examples:

  Code Sample with Output:


  Block-Level Element:

  A Block-level element occupies the entire space of the parent (container) such as
  <div> and <p> in the examp...'
---


## **Éléments de bloc et éléments en ligne**

<!-- more -->

Comprenons les éléments de bloc et les éléments en ligne à l'aide des exemples ci-dessous :

#### **Exemple de code avec rendu :**

![Block Output](https://user-images.githubusercontent.com/16048167/31070017-6f2cf0a2-a77c-11e7-9de6-110b9d0b488d.PNG)

### Élément de niveau bloc :

Un élément de niveau bloc occupe tout l'espace du parent (conteneur), comme `<div>` et `<p>` dans l'exemple.

Notez que `<div>` et `<p>` commencent tous deux sur une nouvelle ligne à chaque fois, formant une structure **en forme de bloc**. Les éléments de niveau bloc commencent sur de nouvelles lignes.

Les **éléments de niveau bloc** courants sont `<div>`, `<p>`, `<article>`, `<section>`, `<figure>`, `<footer>`, etc.

### Élément en ligne :

« En ligne » (*inline*), comme son nom l'indique, signifie « inclus dans le texte principal et non comme une section séparée ». Les éléments en ligne occupent l'espace nécessaire à l'intérieur de l'espace défini par l'élément principal. Contrairement aux éléments de niveau bloc, ils ne commencent pas sur de nouvelles lignes.

Certains des **éléments en ligne** sont `<a>`, `<span>`, `<img>`, `<code>`, `<cite>`, `<button>`, `<input>`, etc.

### Exemple de code avec rendu :

![Inline Output](https://user-images.githubusercontent.com/16048167/31069389-e1e3fc10-a779-11e7-86d2-6685e0061f52.png)

**_Note_** : Les éléments de niveau bloc peuvent contenir d'autres éléments de niveau bloc ou des éléments en ligne. Les éléments en ligne **ne peuvent pas** contenir d'éléments de niveau bloc.

### Changements dans HTML5

Bien que la compréhension des éléments de bloc et en ligne soit toujours pertinente, sachez que ces termes ont été définis dans les versions antérieures de la spécification HTML.

Dans HTML5, un ensemble plus complexe de « catégories de contenu » remplace les éléments de niveau bloc et en ligne. Les éléments de niveau bloc sont largement placés dans la catégorie « flow content » (contenu de flux) dans HTML5, tandis que les éléments en ligne correspondent à la catégorie « phrasing content » (contenu de phrasé).

Pour plus d'informations sur les nouvelles catégories de contenu dans HTML5, y compris le contenu de flux et le contenu de phrasé, consultez la [page sur les catégories de contenu sur le Mozilla Developer Network.][1]

En savoir plus sur le HTML [ici][2].

[1]: https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Content_categories
[2]: https://guide.freecodecamp.org/html