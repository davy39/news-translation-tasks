---
title: L'attribut HTML target de la balise <a> expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T22:47:00.000Z'
originalURL: https://freecodecamp.org/news/the-a-target-html-attribute-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e4b740569d1a4ca3c5e.jpg
tags:
- name: HTML
  slug: html
seo_title: L'attribut HTML target de la balise <a> expliqué
seo_desc: "The <a target> attribute specifies where to open the linked document in\
  \ an a (anchor) tag.\nExamples of \nA target attribute with the value of “_blank”\
  \ opens the linked document in a new window or tab.\n    <a href=\"https://www.freecodecamp.org\"\
  \ target=..."
---

L'attribut `<a target>` spécifie où ouvrir le document lié dans une balise `a` (ancre).

## Exemples de <a target>

Un attribut target avec la valeur "_blank" ouvre le document lié dans une nouvelle fenêtre ou un nouvel onglet.

```html
	<a href="https://www.freecodecamp.org" target="_blank">freeCodeCamp</a>
```

Un attribut target avec la valeur "_self" ouvre le document lié dans le même cadre que celui où il a été cliqué (c'est le comportement par défaut et il n'est généralement pas nécessaire de le spécifier).

```html
	<a href="https://www.freecodecamp.org" target="_self">freeCodeCamp</a>
```

```html
	<a href="https://www.freecodecamp.org">freeCodeCamp</a>
```

Un attribut target avec la valeur "_parent" ouvre le document lié dans le cadre parent.

```html
	<a href="https://www.freecodecamp.org" target="_parent">freeCodeCamp</a>
```

Un attribut target avec la valeur "_top" ouvre le document lié dans le corps complet de la fenêtre.

```html
	<a href="https://www.freecodecamp.org" target="_top">freeCodeCamp</a>
```

Un attribut target avec la valeur "_framename_" ouvre le document lié dans un cadre nommé spécifié.

```html
	<a href="https://www.freecodecamp.org" target="framename">freeCodeCamp</a>
```

## Liens associés :

* [L'attribut <a href>](https://guide.freecodecamp.org/html/attributes/a-href-attribute)
* [Informations générales sur les attributs HTML](https://guide.freecodecamp.org/html/attributes)