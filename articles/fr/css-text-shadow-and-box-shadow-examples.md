---
title: Effets d'ombre de texte et d'ombre de boîte CSS (avec exemples)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-10T19:38:00.000Z'
originalURL: https://freecodecamp.org/news/css-text-shadow-and-box-shadow-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dfe740569d1a4ca3ac9.jpg
tags:
- name: CSS
  slug: css
- name: CSS3
  slug: css3
seo_title: Effets d'ombre de texte et d'ombre de boîte CSS (avec exemples)
seo_desc: 'With CSS3 you can create two types of shadows: text-shadow (adds shadow
  to text) and box-shadow (adds shadow to other elements).

  CSS3 Text Shadow

  The text-shadow property can take up to four values:


  the horizontal shadow

  the vertical shadow

  the blur...'
---

Avec CSS3, vous pouvez créer deux types d'ombres : `text-shadow` (ajoute une ombre au texte) et `box-shadow` (ajoute une ombre à d'autres éléments).

### **Ombre de texte CSS3**

La propriété `text-shadow` peut prendre jusqu'à quatre valeurs :

* l'ombre horizontale
* l'ombre verticale
* l'effet de flou
* la couleur

##### **Exemples :**

Ombre de texte normale

```css
h1 {
  text-shadow: 2px 2px 5px crimson;
}
```

![Exemple d'ombre de texte normale](https://raw.githubusercontent.com/nawnaw7/FCC-guides-CSS3-shadows-images/master/CSS3%20Shadow%20Effects%20Images/text-shadow1.png)

Effet de texte lumineux

```css
h1 {
  text-shadow: 0 0 4px #00FF9C;
}
```

![Exemple de texte lumineux](https://raw.githubusercontent.com/nawnaw7/FCC-guides-CSS3-shadows-images/master/CSS3%20Shadow%20Effects%20Images/text-shadow2.png)

#### **Ombres multiples**

Pour y parvenir, ajoutez simplement une virgule entre deux (ou plus) ensembles de valeurs :

```css
h1 {
  color: white;
  text-shadow: 0 0 3px #F10D58, 0 0 7px #4578D5;
}
```

![Exemple d'ombres multiples avec texte blanc](https://raw.githubusercontent.com/nawnaw7/FCC-guides-CSS3-shadows-images/master/CSS3%20Shadow%20Effects%20Images/text-shadow3.png)

### **Ombre de boîte CSS3**

La propriété `box-shadow` peut prendre jusqu'à six valeurs :

* (optionnel) le mot-clé `inset` (change l'ombre en une ombre à l'intérieur du cadre)
* l'ombre horizontale
* l'ombre verticale
* l'effet de flou
* l'étalement
* la couleur

##### **Exemples :**

```css
.first-div {
  box-shadow: 1px 1px 5px 3px grey;
}

.second-div {
  box-shadow: 0 0 5px 1px lightgrey;
}

.third-div {
  box-shadow: inset 0 0 15px 5px rgba(0,0,0,0.75);
}
```

![Exemples d'ombre de boîte](https://raw.githubusercontent.com/nawnaw7/FCC-guides-CSS3-shadows-images/master/CSS3%20Shadow%20Effects%20Images/box-shadows.png)

#### **Plus d'informations :**

* [MDN web docs](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow?v=b)
* [Vérifier la compatibilité des navigateurs](https://caniuse.com/#search=box-shadow)
* [Générateur d'ombre de boîte CSS](https://www.cssmatic.com/box-shadow) (n'hésitez pas à expérimenter avec les ombres de boîte)