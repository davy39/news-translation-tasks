---
title: 'Comment centrer une image en utilisant Text Align: Center'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-30T21:11:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-center-an-image-using-text-align
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e5e740569d1a4ca3cbb.jpg
tags:
- name: CSS
  slug: css
seo_title: 'Comment centrer une image en utilisant Text Align: Center'
seo_desc: 'An <img> element is an inline element (display value of inline-block).
  It can be easily centered by adding the text-align: center; CSS property to the
  parent element that contains it.

  To center an image using text-align: center; you must place the <i...'
---

Un élément `<img>` est un élément en ligne (valeur d'affichage `inline-block`). Il peut être facilement centré en ajoutant la propriété CSS `text-align: center;` à l'élément parent qui le contient.

Pour centrer une image en utilisant `text-align: center;` vous devez placer le `<img>` à l'intérieur d'un élément de niveau bloc tel qu'un `div`. Puisque la propriété `text-align` ne s'applique qu'aux éléments de niveau bloc, vous placez `text-align: center;` sur l'élément de niveau bloc enveloppant pour obtenir un `<img>` centré horizontalement.

### **Exemple**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Centrer une image en utilisant text align center</title>
    <style>
      .img-container {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div class="img-container"> <!-- Élément parent de bloc -->
      <img src="user.png" alt="John Doe">
    </div>
  </body>
</html>
```

**Note :** L'élément parent doit être un élément de bloc. S'il ne s'agit pas d'un élément de bloc, vous devez ajouter la propriété CSS `display: block;` avec la propriété `text-align`.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Centrer une image en utilisant text align center</title>
    <style>
      .img-container {
        text-align: center;
        display: block;
      }
    </style>
  </head>
  <body>
    <span class="img-container"> <!-- Élément parent en ligne -->
      <img src="user.png" alt="">
    </span>
  </body>
</html>
```

**Démonstration :** [Codepen](https://codepen.io/aravindio/pen/PJMXbp)

## Object Fit

Une fois votre image centrée, vous pourriez vouloir la redimensionner. La propriété `object-fit` spécifie comment un élément répond à la largeur / hauteur de sa boîte parente.

Cette propriété peut être utilisée pour les images, les vidéos ou tout autre média. Elle peut également être utilisée avec la propriété `object-position` pour obtenir plus de contrôle sur la manière dont le média est affiché.

En général, nous utilisons la propriété `object-fit` pour définir comment un média en ligne est étiré ou compressé.

### Syntaxe

```css
.element {
    object-fit: fill || contain || cover || none || scale-down;
}
```

### Valeurs

* `fill` : **Il s'agit de la valeur par défaut**. Redimensionne le contenu pour qu'il corresponde à sa boîte parente, indépendamment du rapport d'aspect.
* `contain` : Redimensionne le contenu pour remplir sa boîte parente en utilisant le bon rapport d'aspect.
* `cover` : Similaire à `contain` mais souvent en rognant le contenu.
* `none` : Affiche l'image dans sa taille d'origine.
* `scale-down` : Compare la différence entre `none` et `contain` pour trouver la plus petite taille d'objet concrète.

### Compatibilité des navigateurs

La propriété `object-fit` est supportée par la plupart des navigateurs modernes. Pour les informations les plus récentes sur la compatibilité, vous pouvez consulter [http://caniuse.com/#search=object-fit](http://caniuse.com/#search=object-fit).

## **Documentation**

* [**text-align**](https://developer.mozilla.org/en-US/docs/Web/CSS/text-align) - MDN
* [**object-fit** - MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/object-fit)
* [**<img>**](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img) - MDN