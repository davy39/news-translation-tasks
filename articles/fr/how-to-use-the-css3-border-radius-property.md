---
title: Comment utiliser la propriété Border Radius de CSS3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-04T00:42:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-css3-border-radius-property
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/joel-fulgencio-VSrHD079L78-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: toothbrush
  slug: toothbrush
seo_title: Comment utiliser la propriété Border Radius de CSS3
seo_desc: "With CSS3, you can give any element “rounded corners” by using the border-radius\
  \ property. The value can be in any valid CSS length unit.\n  .rounded-corners {\n\
  \    border-radius: 20px;\n  }\n\n  .circle {\n    border-radius: 50%;\n  }\n\n\n\
  Note: The border-ra..."
---

Avec CSS3, vous pouvez donner à n'importe quel élément des "coins arrondis" en utilisant la propriété `border-radius`. La valeur peut être dans n'importe quelle unité de longueur CSS valide.

```css
  .rounded-corners {
    border-radius: 20px;
  }

  .circle {
    border-radius: 50%;
  }
```

![exemples](https://github.com/kaithrendyle/guide-photos/blob/master/rounded-circle.png?raw=true)

**Note :** La propriété `border-radius` est en fait une propriété raccourcie pour les propriétés `border-top-left-radius`, `border-top-right-radius`, `border-bottom-right-radius` et `border-bottom-left-radius`.

Si une seule valeur est fournie, le border-radius sera le même pour les quatre coins, comme dans les exemples ci-dessus. Mais vous avez également la possibilité de spécifier différentes valeurs pour chaque coin.

```css
.new-shape {
  border-radius: 20px 50px 5px 0; /* haut gauche, haut droite, bas droite, bas gauche */
}
```

Si seulement deux valeurs sont fournies, la première valeur s'applique au coin haut-gauche et bas-droite, et la deuxième valeur s'applique au coin haut-droite et bas-gauche.

```css
.leaf-shape {
  border-radius: 0 50%;
}
```

Si trois valeurs sont définies, la première s'applique à nouveau au rayon haut-gauche, la deuxième valeur indique haut-droite et bas-gauche, laissant la troisième valeur indiquer le coin bas-droite.

```css
.odd-shape {
  border-radius: 0 20px 50%;
}
```

![exemples](https://github.com/kaithrendyle/guide-photos/blob/master/odd-shapes.png?raw=true)

L'arrondi d'un coin n'a pas besoin d'être parfaitement symétrique. Vous pouvez spécifier à la fois les rayons horizontal et vertical en utilisant une barre oblique (" /") pour obtenir un coin avec une forme elliptique.

```css
.elliptical-1 {
  border-radius: 50px/10px; /* rayon horizontal / rayon vertical */
}
.elliptical-2 {
  border-radius: 10px/50px; 
}
```

![exemples](https://github.com/kaithrendyle/guide-photos/blob/master/elliptical-basic.png?raw=true)

Puisqu'un seul couple de valeurs est donné dans les exemples ci-dessus, les quatre coins sont identiques. Mais, bien sûr, si vous voulez une forme plus complexe, vous pouvez fournir jusqu'à quatre valeurs pour les rayons horizontaux et quatre pour les rayons verticaux.

```css
.elliptical-3 {
  border-radius: 50px 20px 50px 20px/20px 50px 20px 50px; /* horizontal haut-gauche, horizontal haut-droite, horizontal bas-droite, horizontal bas-gauche / vertical haut-gauche, vertical haut-droite, vertical bas-droite, vertical bas-gauche */
}
```

Remarquez comment le raccourci ci-dessus produit le même résultat que la spécification des propriétés individuelles ci-dessous. Soyez conscient que lorsque les coins sont définis individuellement, les valeurs sont séparées par des espaces au lieu d'être séparées par des barres obliques.

```css
.elliptical-4 {
  border-top-left-radius: 50px 20px; /* rayon horizontal, rayon vertical */
  border-top-right-radius: 20px 50px;
  border-bottom-right-radius: 50px 20px;
  border-bottom-left-radius: 20px 50px;
}
```

![exemples](https://github.com/kaithrendyle/guide-photos/blob/master/elliptical-advance.png?raw=true)

## Plus d'informations sur la propriété border radius de CSS :

* [Apprenez à utiliser la propriété CSS border radius en construisant une calculatrice](https://www.freecodecamp.org/news/learn-css-border-radius-property-by-building-a-calculator-53497cd8071d/)