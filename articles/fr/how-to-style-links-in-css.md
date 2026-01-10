---
title: Comment styliser les liens en CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-02T22:53:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-links-in-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cd9740569d1a4ca3485.jpg
tags:
- name: CSS
  slug: css
- name: style
  slug: style
- name: toothbrush
  slug: toothbrush
seo_title: Comment styliser les liens en CSS
seo_desc: "Styling Links\nLinks can be styled with any CSS property, such as color,\
  \ font-family, font-size, and padding. Here is an easy example:\na {\n    color:\
  \ hotpink;\n}\n\nIn addition, links can be styled differently depending on what\
  \ state they are in.\nLinks a..."
---

## **Styliser les liens**

Les liens peuvent être stylisés avec n'importe quelle propriété CSS, comme `color`, `font-family`, `font-size` et `padding`. Voici un exemple simple :

```css
a {
    color: hotpink;
}
```

De plus, les liens peuvent être stylisés différemment selon leur état.

Les liens ont également 4 états, et de nombreux programmeurs stylisent chaque état différemment. Les quatre états sont :

* `a:link` : un lien non visité, non cliqué
* `a:visited` : un lien visité, cliqué
* `a:hover` : un lien lorsque le curseur de l'utilisateur est dessus
* `a:active` : un lien au moment où il est cliqué

La propriété `<a href="">` est responsable de la création des URLs et peut être modifiée en utilisant plusieurs propriétés de style CSS, bien qu'elle en ait quelques-unes par défaut :

1. Soulignement
2. Couleur bleue

Vous pouvez changer ces propriétés en modifiant les propriétés `color` et `text-decoration`.

```css
   color: black;
   text-decoration: none;
```

Vous pouvez également styliser le lien en fonction de l'interaction en utilisant ces propriétés, également connues sous le nom d'états de lien :

* a:link - un lien normal, non visité
* a:visited - un lien que l'utilisateur a visité
* a:hover - un lien lorsque l'utilisateur passe la souris dessus
* a:active - un lien au moment où il est cliqué

Voici un exemple de CSS utilisant les 4 états :

```css
a:link { color: red; }
a:visited { color: blue; }
a:hover { color: green; }
a:active { color: blue; }
```

**Notez** qu'il existe des _règles d'ordre_ pour la définition du style des états de lien.

* `a:hover` DOIT venir après `a:link` et `a:visited`

`a:active` DOIT venir après `a:hover`

a:link - un lien normal, non visité a:visited - un lien que l'utilisateur a visité a:hover - un lien lorsque l'utilisateur passe la souris dessus a:active - un lien au moment où il est cliqué

```css
/* lien non visité */
a:link {
    color: red;
}

/* lien visité */
a:visited {
    color: green;
}

/* survol de la souris */
a:hover {
    color: hotpink;
}

/* lien sélectionné */
a:active {
    color: blue;
} 
```

## Plus sur le style en CSS :

* [Comment styliser une balise HTML directement en CSS](https://www.freecodecamp.org/news/inline-css-guide-how-to-style-an-html-tag-directly/)
* [Comment styliser les listes avec CSS](https://www.freecodecamp.org/news/how-to-style-lists-with-css/)
* [Comment styliser les boutons avec CSS](https://www.freecodecamp.org/news/a-quick-guide-to-styling-buttons-using-css-f64d4f96337f/)