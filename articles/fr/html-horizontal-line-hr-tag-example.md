---
title: Ligne horizontale HTML – Exemple de balise HR
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-26T18:36:53.000Z'
originalURL: https://freecodecamp.org/news/html-horizontal-line-hr-tag-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/hr.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Ligne horizontale HTML – Exemple de balise HR
seo_desc: "You can use the HTML <hr> tag to separate out different topics on a page.\n\
  We often use this tag when we want to create a thematic break or separate items\
  \ on an HTML page. \nIn this article, you'll learn how to use this tag in your HTML\
  \ code.\nTable of ..."
---

Vous pouvez utiliser la balise HTML `<hr>` pour séparer différents sujets sur une page.

Nous utilisons souvent cette balise lorsque nous voulons créer une rupture thématique ou séparer des éléments sur une page HTML.

Dans cet article, vous apprendrez à utiliser cette balise dans votre code HTML.

## Table des matières
- [Syntaxe de base](#heading-syntaxe-de-base)
- [Attributs de la balise `<hr />`](#heading-attributs-de-la-balise)
- [L'attribut Width](#heading-lattribut-width)
- [L'attribut Color](#heading-lattribut-color)
- [L'attribut Size](#heading-lattribut-size)
- [L'attribut Align](#heading-lattribut-align)
- [Conclusion](#heading-conclusion)

## Syntaxe de base

La balise `<hr>` est un élément vide. Cela signifie qu'elle n'a qu'une balise ouvrante, `<hr>`.

À partir de HTML5, nous devons maintenant attacher une barre oblique à la balise d'un élément vide. Ainsi, au lieu d'avoir simplement `<hr>`, vous devez l'écrire `<hr />`.

Dans les navigateurs, la balise `<hr />` est affichée comme une règle ou une ligne horizontale, comme ceci :
![ss-1-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-2.png)


## Attributs de la balise `<hr />`

La balise `<hr />` accepte des attributs tels que `width`, `color`, `size` et `align`.

Avant de vous montrer comment les attributs individuels apparaissent et fonctionnent, je vais centrer tout le contenu du body avec ce code CSS :

```css
body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }
```

### L'attribut Width

L'attribut `width` est utilisé pour spécifier une largeur pour la balise `<hr />`. Il prend des pixels ou des pourcentages comme valeur.

```html
<hr width="50%" />
```
![ss-2-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-2.png)

### L'attribut Color

L'attribut `color` est utilisé pour spécifier une couleur pour la balise `<hr />`.

```html
    <hr width="50%" color="green" />
```

Voici à quoi cela ressemblerait si nous définissons une couleur verte pour la balise `<hr />` :
![ss-3-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-3.png)

### L'attribut Size

Vous pouvez définir une hauteur pour la balise `<hr />` avec l'attribut `size`. La valeur doit être définie en pixels.

```html
<hr width="50%" color="green" size="50px" />
```

Une hauteur de `50px` ressemble à la capture d'écran ci-dessous :
![ss-4-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-3.png)

### L'attribut Align

L'attribut `align` est utilisé pour définir un alignement pour la balise `<hr />`. Il prend les valeurs `left`, `center` et `right`.

Par défaut, l'alignement est à gauche – ce qui signifie que si un alignement n'est pas défini, la balise `<hr />` s'aligne automatiquement à gauche.

```html
    <hr width="50%" color="green" size="50px" align="right" />
```

Définir un alignement à `right` pour la balise `<hr />` ressemble à ceci :
![ss-5-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-4.png)

## Conclusion

Cet article vous montre à quoi ressemble la balise `<hr />`, à quoi elle sert et les attributs qu'elle accepte.

Puisque la balise `<hr />` apparaît comme une règle horizontale dans les navigateurs, vous pourriez penser à l'utiliser pour dessiner une ligne.

Mais vous ne devriez pas faire cela car la règle horizontale n'apparaît que de manière présentative, pas sémantique. Au lieu de cela, vous devriez dessiner une ligne avec un `div` ou un `span` selon le cas.

Si vous trouvez cet article utile, partagez-le avec vos amis et votre famille.