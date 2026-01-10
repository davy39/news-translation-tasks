---
title: 'Qu''est-ce que box-sizing: border-box en CSS ?'
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2024-02-05T18:26:43.000Z'
originalURL: https://freecodecamp.org/news/what-is-box-sizing-border-box-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/curology-fPSELOXfeU4-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: 'Qu''est-ce que box-sizing: border-box en CSS ?'
seo_desc: "In CSS, there is a property called box-sizing that allows you to determine\
  \ how the width and the height for an element is calculated. \nA lot of CSS resets\
  \ will change the default box model from content-box to border-box to make the layouts\
  \ easier to ..."
---

En CSS, il existe une propriété appelée `box-sizing` qui vous permet de déterminer comment la largeur et la hauteur d'un élément sont calculées. 

De nombreux [CSS resets](https://www.freecodecamp.org/news/how-i-style-my-websites-with-my-favorite-css-resets-7ace41dbc43d/) changent le modèle de boîte par défaut de `content-box` à `border-box` pour faciliter la gestion des mises en page.

Mais que fait réellement `box-sizing: border-box` ?

Dans cet article, nous allons explorer la propriété `box-sizing` et son impact sur la mise en page de vos pages web.

## Le Modèle de Boîte par Défaut

Le modèle de boîte par défaut est défini sur `content-box`. Cela signifie que la largeur et la hauteur d'un élément sont calculées en fonction du contenu à l'intérieur de l'élément.

Si vous ajoutez un remplissage (padding) ou une bordure à l'élément, ces valeurs seront ajoutées à la largeur finale de l'élément. 

Dans cet exemple, nous avons une boîte rouge qui a une largeur de 200px, une hauteur de 200px, un remplissage de 20px et une bordure noire définie à 5px.

```html
<div class="box"></div>
```

```css
.box {
  background-color: #ff0000;
  width: 200px;
  height: 200px;
  padding: 20px;
  border: 5px solid black;
}
```

%[https://codepen.io/jessica-wilkins/pen/RwdyYmq]

  
Si vous faites un clic droit sur l'élément `div` et l'inspectez dans les outils de développement, vous verrez que la largeur de la boîte est de 250px et la hauteur est de 250px. 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-04-at-9.12.12-AM.png)
_exemple de boîte définie à 250px par 250px_

Cela est dû au fait que le remplissage et la bordure sont ajoutés à la largeur et à la hauteur de la boîte. La largeur et la hauteur totales sont maintenant de 250px par 250px au lieu de 200px.   
  
Lorsque vous construisez vos mises en page, vous devez vous souvenir de calculer le remplissage et la bordure dans la largeur et la hauteur de l'élément. Cela peut être un peu fastidieux et peut entraîner des résultats inattendus.

Une façon d'éviter cela est d'utiliser la propriété `box-sizing` définie sur `border-box`.

## Comment Travailler avec `box-sizing: border-box`

Lorsque vous définissez la propriété `box-sizing` sur `border-box`, la largeur et la hauteur de l'élément sont calculées en fonction du contenu, du remplissage et de la bordure de l'élément.

Dans cet exemple révisé, nous utilisons le sélecteur `*` pour définir la propriété `box-sizing` sur `border-box` pour tous les éléments de la page. Cela est connu sous le nom de réinitialisation CSS globale.

```html
<div class="box"></div>
```

```css
*,
*:before,
*:after {
  box-sizing: border-box;
}

.box {
  background-color: #ff0000;
  width: 200px;
  height: 200px;
  padding: 20px;
  border: 5px solid black;
}
```

%[https://codepen.io/jessica-wilkins/pen/rNRvZXm?editors=1100]

Maintenant, lorsque vous inspectez l'élément de la boîte, vous verrez que la largeur et la hauteur sont définies à 200px comme nous l'avons spécifié dans la feuille de style. Le navigateur prend en compte le remplissage et la bordure ajoutés et ajuste la boîte de contenu en conséquence. 

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-04-at-9.28.29-AM.png)
_exemple des outils de développement montrant une largeur de boîte de 200px_

### Que font les sélecteurs `*`, `*:before` et `*:after` ?

La raison pour laquelle nous utilisons les sélecteurs `*`, `*:before` et `*:after` est de nous assurer que la valeur `border-box` est appliquée à tous les éléments de la page. 

Le sélecteur `*` sélectionne tous les éléments, le sélecteur `*:before` sélectionne tous les éléments avant le contenu, et le sélecteur `*:after` sélectionne tous les éléments après le contenu. 

Pour en savoir plus sur les pseudo-éléments `:before` et `:after`, consultez [cet article de freeCodeCamp](https://www.freecodecamp.org/news/css-pseudo-elements-before-and-after-selectors-explained/).

## Conclusion

Devoir se souvenir de calculer le remplissage et la bordure dans la largeur et la hauteur de vos éléments peut être fastidieux et entraîner des résultats inattendus dans vos mises en page.  

Définir la propriété `box-sizing` sur `border-box` pour tous les éléments de la page en utilisant les sélecteurs `*`, `*:before` et `*:after` vous fera gagner beaucoup de temps en débogage et en correction des problèmes de mise en page dans votre CSS.