---
title: Comment styliser les listes avec CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-22T00:12:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-lists-with-css
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e8b740569d1a4ca3db4.jpg
tags:
- name: CSS
  slug: css
seo_title: Comment styliser les listes avec CSS
seo_desc: 'HTML Lists Recap

  There are two main types of lists in HTML — Ordered and Unordered.

  In Ordered lists (<ol></ol>), the order of the list items is important. The items
  may appear in order by number, roman numeral, alpha numeral, or another type of
  mark...'
---

### **Récapitulatif des listes HTML**

Il existe deux principaux types de listes en HTML — **Ordonnées** et **Non ordonnées**.

Dans les listes **Ordonnées** (`<ol></ol>`), l'ordre des éléments de la liste est important. Les éléments peuvent apparaître dans l'ordre par nombre, chiffre romain, lettre, ou un autre type de marqueur. Le marqueur par défaut pour les listes ordonnées est un nombre (ou `decimal`) :

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/ordered-list.png?raw=true)

Dans les listes **Non ordonnées** (`<ul></ul>`), l'ordre des éléments de la liste n'a pas d'importance. Les éléments apparaissent sous forme de puces. Le marqueur par défaut pour les listes non ordonnées est une puce ronde ou `disc`.

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/unordered-list.png?raw=true)

Chaque élément de liste dans une liste ordonnée ou non ordonnée est créé avec la balise `<li></li>`.

### **Styles spécifiques aux listes**

Il existe trois propriétés courantes spécifiques au style des listes : `list-style-type`, `list-style-position` et `list-style-image`. Il existe également une propriété raccourcie qui inclut les trois.

#### **`list-style-type`**

Les marqueurs (ou puces) qui apparaissent dans les listes ordonnées et non ordonnées peuvent être stylisés de diverses manières. La propriété CSS pour styliser le type de marqueur est `list-style-type`. La valeur par défaut de `list-style-type` pour une liste ordonnée est `decimal`, tandis que la valeur par défaut pour une liste non ordonnée est `disc`.

Exemple de liste ordonnée :

```css
/* css */
ol {
  list-style-type: upper-roman;
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-style-type-upper-roman.png?raw=true)

Exemple de liste non ordonnée :

```css
/* css */
ul {
  list-style-type: square;
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-style-type-square.png?raw=true)

Exemple sans marqueur :

```css
/* css */
ul {
  list-style-type: none;
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-style-type-none.png?raw=true)

Les valeurs acceptées pour la propriété `list-style-type` incluent :

_Non ordonnées :_

* disc (_par défaut_)
* circle
* square

_Ordonnées :_

* decimal (_par défaut_)
* decimal-leading-zero
* lower-roman
* upper-roman
* lower-greek
* lower-latin
* upper-latin
* armenian
* georgian
* lower-alpha
* upper-alpha

_Autres :_

* none

Note : toutes les valeurs de propriété listées ci-dessus peuvent être utilisées pour styliser à la fois les listes ordonnées et non ordonnées (ex : une liste ordonnée avec des marqueurs de liste `square`).

#### **`list-style-position`**

`list-style-position` contrôle si le marqueur de liste apparaît à l'intérieur ou à l'extérieur de chaque élément de liste (`<li></li>`). La propriété accepte deux valeurs, `outside` (par défaut) ou `inside`.

Positionnez le marqueur `outside` de l'élément de liste, et toutes les lignes de texte et sous-lignes de chaque élément de liste seront alignées verticalement :

```css
/* css */
ul {
  list-style-position: outside; /* par défaut */
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-style-position-outside.png?raw=true)

Positionnez le marqueur `inside`, et la première ligne de texte de chaque élément de liste sera indentée pour laisser de la place pour le marqueur. Toute sous-ligne du même élément de liste sera alignée avec le marqueur plutôt qu'avec la première ligne de texte :

```css
/* css */
ul {
  list-style-position: inside;
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-style-position-inside.png?raw=true)

#### **`list-style-image`**

La propriété `list-style-image` accepte une URL d'image à la place du marqueur de liste. La valeur par défaut pour cette propriété est `none`.

```css
/* css */
ul {
  list-style-image: url(https://url-to-image);
}
```

#### **Raccourci `list-style`**

`list-style` est une propriété raccourcie pour les trois propriétés de style listées ci-dessus. L'ordre des valeurs que `list-style` accepte est `list-style-type`, `list-style-position` et `list-style-image`. Si une valeur est omise, la valeur par défaut pour cette propriété sera utilisée.

Exemple :

```css
/* css */
ul {
  list-style: circle inside none;
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-style-shorthand.png?raw=true)

#### **Plus de styles spécifiques aux listes**

Les balises de liste ordonnée acceptent également des attributs qui contrôlent le flux, le compte ou des valeurs de marqueur spécifiques de ses éléments de liste. Ceux-ci incluent les attributs `start`, `reversed` et `value`. Voir les ressources MDN listées ci-dessous pour plus de détails.

### **Style général**

Le contenu des listes peut être stylisé comme d'autres éléments `p` ou `div`. `color`, `font-family`, `margin`, `padding` ou `border` ne sont que quelques exemples de propriétés qui peuvent être ajoutées aux éléments `ul`, `ol` ou `li`.

Notez que tout style ajouté à l'élément `ul` ou `ol` affectera la liste entière. Les styles ajoutés directement aux éléments `li` affecteront les éléments de liste individuels. Dans l'exemple ci-dessous, les propriétés de bordure et de couleur de fond sont stylisées différemment entre la liste et les éléments de liste :

```css
/* css */
ul {
  list-style-type: circle;
  border: 2px solid blue;
  background-color: lightblue;
}
li {
  margin: 5px;
  background-color: lightyellow;
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-styles.png?raw=true)

#### **Espacement des listes**

Vous pouvez remarquer un espacement supplémentaire devant les éléments de liste lorsque `list-style-type` est défini sur `none`. Définir `padding` sur `0` (ou l'espacement préféré) sur l'élément de liste remplacera ce remplissage par défaut.

```css
/* css */
ul {
  list-style: none;
  padding: 0;
}
li {
  padding: 5px 10px;
  background-color: #EEEEEE;
  border: 1px solid #DDDDDD;
}
```

![Image](https://github.com/kayfo23/imgs-for-fcc-guide/blob/master/list-style-padding.png?raw=true)

#### **Sources :**

Les liens ci-dessous ont été référencés pour compiler les informations trouvées dans cet article. Veuillez les consulter pour plus de détails sur ce sujet.

#### **Plus d'informations :**

[MDN - Styliser les listes](https://developer.mozilla.org/en-US/docs/Learn/CSS/Styling_text/Styling_lists)

[W3Schools - Listes CSS](https://www.w3schools.com/css/css_list.asp)

[CSS Tricks - list-style](https://css-tricks.com/almanac/properties/l/list-style/)