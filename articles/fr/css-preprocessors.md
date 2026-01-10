---
title: Les préprocesseurs CSS expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-17T20:55:00.000Z'
originalURL: https://freecodecamp.org/news/css-preprocessors
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dce740569d1a4ca39bd.jpg
tags:
- name: CSS
  slug: css
- name: Sass
  slug: sass
- name: toothbrush
  slug: toothbrush
seo_title: Les préprocesseurs CSS expliqués
seo_desc: CSS Preprocessors are increasingly becoming a mainstay in the workflow of
  front end web developers. CSS is an incredibly complicated and nuanced language,
  and in an effort to make it’s usage easier, developers often turn to using preprocessors
  such a...
---

Les préprocesseurs CSS deviennent de plus en plus un élément incontournable dans le flux de travail des développeurs web front-end. Le CSS est un langage incroyablement compliqué et nuancé, et dans un effort pour faciliter son utilisation, les développeurs se tournent souvent vers l'utilisation de préprocesseurs tels que SASS ou LESS.

Les préprocesseurs CSS compilent le code qui est écrit en utilisant un compilateur spécial. Ils l'utilisent ensuite pour créer un fichier CSS, qui peut ensuite être référencé par le document HTML principal.

Lorsque vous utilisez un préprocesseur CSS, vous pourrez programmer en CSS normal comme vous le feriez si le préprocesseur n'était pas en place. Le bon côté, c'est que vous avez également plus d'options disponibles. Certains, comme SASS, ont des normes de style spécifiques destinées à faciliter encore plus la rédaction du document, comme la liberté d'omettre les accolades si vous le souhaitez.

Bien sûr, les préprocesseurs CSS offrent également d'autres fonctionnalités. Beaucoup des fonctionnalités offertes sont incroyablement similaires entre les préprocesseurs, avec seulement de légères variations de syntaxe. Ainsi, vous pouvez choisir pratiquement n'importe lequel que vous souhaitez, et vous serez en mesure de réaliser les mêmes choses. Certaines des fonctionnalités les plus utiles sont :

### **Variables**

L'un des éléments les plus couramment utilisés dans tout langage de programmation est la variable, quelque chose que le CSS manque notablement. En ayant des variables à votre disposition, vous pouvez définir une valeur une fois et la réutiliser dans tout le programme. Un exemple de cela en SASS serait :

```sass
$yourcolor: #000056
.yourDiv {
  color: $yourcolor;
}
```

En déclarant la variable `SASS yourcolor` une fois, il est maintenant possible de réutiliser cette même couleur exacte dans tout le document sans jamais avoir à retaper la définition.

### **Boucles**

Un autre élément courant dans les langages sont les boucles, quelque chose d'autre que le CSS manque. Les boucles peuvent être utilisées pour répéter les mêmes instructions plusieurs fois sans avoir à les réentrer plusieurs fois. Un exemple avec SASS serait :

```sass
@for $vfoo from 35px to 85px {
  .margin-#{$vfoo} {
    margin: $vfoo 10px;
  }
}
```

Cette boucle nous évite d'avoir à écrire le même code plusieurs fois pour changer la taille de la marge.

### **Instructions If/Else**

Une autre fonctionnalité que le CSS manque sont les instructions If/Else. Celles-ci exécuteront un ensemble d'instructions uniquement si une condition donnée est vraie. Un exemple de cela en SASS serait :

```sass
@if width(body) > 500px {
  background-color: blue;
} @else {
  background-color: white;
}
```

Ici, la couleur de fond changera en fonction de la largeur du corps de la page.

Ce ne sont là que quelques-unes des principales fonctions des préprocesseurs CSS. Comme vous pouvez le voir, les préprocesseurs CSS sont des outils incroyablement utiles et polyvalents. De nombreux développeurs web les utilisent, et il est fortement recommandé d'en apprendre au moins un.

#### **Plus d'informations :**

* [Les meilleurs tutoriels CSS](https://www.freecodecamp.org/news/best-css-and-css3-tutorial/)
* Documentation SASS : [http://sass-lang.com/](http://sass-lang.com/)
* [SASS, un préprocesseur pour vos garnitures web](https://www.freecodecamp.org/news/give-more-oompf-to-your-web-garnishes-with-preprocessors-in-sass-bd379226a114/)
* Documentation LESS : [http://lesscss.org/](http://lesscss.org/)
* Documentation Stylus : [http://stylus-lang.com/](http://stylus-lang.com/)