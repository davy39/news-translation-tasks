---
title: Unités CSS – Quand utiliser rem, em, px, et plus encore
date: '2024-01-25T00:58:27.000Z'
author: Esther Christopher
authorURL: https://www.freecodecamp.org/news/author/EstherChristopher/
originalURL: https://freecodecamp.org/news/css-units-when-to-use-each-one
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/pexels-adonyi-ga-bor-1409216.jpg
tags:
- name: CSS
  slug: css
seo_desc: 'CSS units allow you to measure and specify different property values. You
  use them to modify CSS properties such as margins, padding, height, and width to
  make them compatible with devices of all screen sizes.

  CSS units have two basic types:


  Absolut...'
---


Les unités CSS vous permettent de mesurer et de spécifier différentes valeurs de propriétés. Vous les utilisez pour modifier des propriétés CSS telles que les marges, le remplissage (padding), la hauteur et la largeur afin de les rendre compatibles avec des appareils de toutes tailles d'écran.

<!-- more -->

Les unités CSS se divisent en deux types fondamentaux :

-   Les unités absolues
-   Les unités relatives

Les unités absolues sont fixes et ne dépendent pas de la taille de l'élément parent ou de la fenêtre d'affichage (viewport). Des exemples d'unités absolues sont les pixels (px), les points (pt) et les centimètres (cm).

Les unités relatives, en revanche, sont flexibles – et comme leur nom l'indique, elles sont relatives à la taille de l'élément parent, à la taille de la fenêtre d'affichage ou à la taille de la police de l'élément racine.

Puisqu'il existe de nombreux types d'unités CSS, vous pourriez avoir du mal à décider laquelle utiliser pour une mesure particulière. Cet article présentera les meilleurs cas d'utilisation pour chacune de ces unités. Nous nous concentrerons ici sur les unités CSS les plus importantes et les plus fréquemment utilisées : `rem`, `em`, `vh`, `vw`, `%`, et l'unité absolue bien connue – `px`.

## Table des matières :

1.  [Rem (`rem`)][1]
2.  [Em (`em`)][2]
3.  [Pourcentages (`%`)][3]
4.  [Hauteur de la fenêtre d'affichage (`vh`)][4]
5.  [Largeur de la fenêtre d'affichage (`vw`)][5]
6.  `[ch](#heading-ch)`
7.  [Pixels (`px`)][6]

## Rem (`rem`)

L'unité `rem` en CSS signifie "root `em`" (em racine). C'est une unité de mesure relative qui se rapporte à la taille de la police de l'élément racine. Un `rem` est égal à la taille de la police de l'élément racine. L'élément racine est défini par défaut à `16px` dans de nombreux navigateurs, donc `1rem` est égal à `16px`.

Regardons un exemple pour voir comment utiliser `rem` :

```
    <div class="container">
      <h1>Best Practices for CSS units</h1>
      <p>This is a paragraph with font size set to 2rem</p>
    </div>
```

```
html {
    font-size: 16px;
}
.container {
   margin: 20px;
   padding: 20px;
   border: 1px solid #ddd;
}
h1 {
    font-size: 2rem;
    color: #0077cc;
}
p {
    font-size: 1rem;
    color: #0077cc;
}
```

L'élément `h1` est défini à `2rem`, ce qui signifie qu'il fait deux fois la taille de l'élément racine (l'élément html). 2 x `16px` = 32, donc l'élément `h1` fait `32px`.

Voici l'élément racine à `16px` :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/4AF00C2B-DB5A-463D-836F-8EF72530EB04_4_5005_c-2.jpeg) _La taille de la police lorsque l'élément racine est à 16px_

Ensuite, dans l'image ci-dessous, l'élément racine a été défini à `20px`, donc les `2rem` de l'élément `h1` valent 2 x `20px`, ce qui donne un texte `h1` de `40px`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/4A7E8EE7-683F-4F83-A5C0-1D2FF4872DBD_4_5005_c-1.jpeg) _La taille de la police lorsque l'élément racine est à 20px_

Dans votre éditeur de code, à mesure que vous modifiez la taille de police de base dans le sélecteur HTML du fichier CSS, vous pouvez voir comment les tailles de police définies en unités rem s'ajustent également de manière proportionnelle.

En utilisant les unités `rem`, vous pouvez facilement mettre à l'échelle la taille de la police des éléments du corps du texte proportionnellement à la taille de la police HTML.

C'est une bonne idée d'utiliser `rem` pour définir les tailles de police car cette unité est conçue pour s'adapter aux préférences du navigateur de l'utilisateur. Cela favorise l'accessibilité. C'est également excellent pour une mise à l'échelle cohérente, car la modification de la taille de la police HTML affectera tous les éléments utilisant des unités rem.

L'utilisation de `rem` ou `em` pour le padding ou la marge offre également des avantages en termes de conception évolutive et maintenable. Lorsque vous modifiez la taille de la police au niveau supérieur, toutes les valeurs `rem` sont automatiquement mises à jour et s'ajustent en fonction de la taille de police de base. `rem` ou `em` doivent être utilisés pour les marges ou le padding selon que vous souhaitez que l'élément soit relatif à l'élément racine ou au parent.

## Em (`em`)

Tout comme `rem`, `em` est une unité de mesure relative. Mais contrairement à `rem`, `em` est relatif à la taille de la police de l'élément parent ou à la taille de la police du parent le plus proche ayant une taille de police définie.

Regardons un exemple :

```
    <div class="container">
      <p>This is a paragraph with the font size set to 2em</p>
    </div>
```

```
body {
     font-size: 20px;
}
.container {
   margin: 20px;
   padding: 20px;
   border: 1px solid #ddd;
}
p {
    font-size: 2em;
    color: #0077cc;
}
```

L'élément `p` est défini à `2em`, ce qui signifie qu'il fait 2 fois la taille de la police de l'élément parent. 2 x 20 font `40px`, donc l'élément p fait `40px`.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/A8CF43A8-8685-476A-A566-2C9E60836CAC_4_5005_c.jpeg) _La taille de la police de l'élément paragraphe définie à 2em_

Regardons un autre exemple :

```
    <div class="parent-element">
      This is the nearest parent
      <div class="child-element">
        <p>This is the child</p>
      </div>
    </div>
```

```
.parent-element {
  font-size: 20px;
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
}
p {
  font-size: 2em;
  color: #0077cc;
}
```

Ici, la taille de la police de `child-element` est définie à 2 fois celle de l'élément `parent-element`. Cela donne `40px` (2 x 20).

![Image](https://www.freecodecamp.org/news/content/images/2024/01/AFF1051E-8AFF-43DE-A90B-DD49CE020AA4_4_5005_c.jpeg) _La taille de la police de l'élément enfant à 2em de l'élément parent_

Si vous avez besoin de mettre un élément à l'échelle pour qu'il soit cohérent avec son parent, alors `em` est la bonne direction à prendre. `em` est idéal pour créer des designs évolutifs et responsives.

Il est recommandé d'utiliser `em` pour définir les marges et le padding. Lorsque vous utilisez em pour les marges et le padding, ils s'ajustent en fonction de la taille de la police de l'élément parent. Cela crée un design cohérent, surtout lorsque les utilisateurs ajustent la taille de police par défaut de leur navigateur. Lorsque vous définissez une marge ou un padding avec em, les mises en page deviennent également plus flexibles et adaptables, et les éléments peuvent se mettre à l'échelle proportionnellement.

`em` est également important pour les media queries afin d'améliorer la réactivité et l'adaptabilité.

## Pourcentages (`%`)

Les pourcentages sont des unités relatives qui effectuent le rendu d'un élément par rapport à la taille de l'élément parent. Ils servent de pourcentage de leur bloc conteneur et sont toujours relatifs à leur parent le plus proche.

Voici un exemple :

```
<div class="container">
    <div class="box"></div>
</div>
```

```
.container {
  width: 80%;
  height: 80%;
  margin: auto;
  position: absolute;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #000000;
}
.box {
  width: 50%;
  height: 50%;
  background-color: #0077cc;
}
```

Ici, l'élément box représente `50%` de la largeur et de la hauteur du conteneur parent, il occupe donc la moitié du conteneur.

Le conteneur représente `80%` de la fenêtre d'affichage en largeur et en hauteur. Si vous essayez de redimensionner le navigateur, vous remarquerez que le pourcentage est maintenu. De même, la boîte à l'intérieur du conteneur reste à `50%` du conteneur en largeur et en hauteur.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/B73FE4D6-BFF6-410D-8713-848BD92BFD3F_1_201_a.jpeg) _L'élément box à 50% de son élément conteneur_

Lorsque vous voulez qu'un élément occupe une certaine partie du bloc conteneur, vous devriez opter pour les pourcentages.

Les pourcentages peuvent être utilisés pour positionner des éléments par rapport à leur élément conteneur. Cela s'avère utile lors de la création de mises en page où les éléments doivent être positionnés sur la base d'un pourcentage du parent.

Définir les largeurs et les hauteurs en pourcentages permet également aux éléments de se mettre à l'échelle par rapport à leur élément conteneur.

## Hauteur de la fenêtre d'affichage (`vh`)

`vh` est une unité de mesure relative qui représente la zone de hauteur visible de la fenêtre du navigateur.

Voici un exemple de son fonctionnement :

```
 <div class="viewport-height">
```

```
.viewport-height {
    height: 100vh;
    background-color: bisque;
}
```

Cet extrait de code montre l'élément `viewport-height` défini à `100vh`, il couvre donc toute la hauteur de la fenêtre d'affichage.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/191234F1-D770-46AB-837B-3C0FFCD338C3_1_201_a.jpeg) _La zone de la fenêtre d'affichage couverte par 100vh_

```
.box {
  width: 50vw;
  height: 30vh;
  background-color: antiquewhite;
}
```

Modifions-le légèrement :

```
<div class="relative-height"></div>
```

```
.relative-height {
    height: 40vh;
    background-color: bisque;
}
```

Dans l'exemple ci-dessus, l'élément `relative-height` est défini à `40vh`, il couvre donc cette fraction de la hauteur de la fenêtre d'affichage.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/F45DD133-6DC6-4869-A3A7-844737B7F18F_1_201_a.jpeg) _La zone de la fenêtre d'affichage couverte par 40vh_

L'utilisation de `vh` pour la hauteur permet aux éléments de maintenir la hauteur définie de la fenêtre d'affichage. C'est particulièrement utile lorsque vous voulez qu'un élément occupe un certain pourcentage de la hauteur de l'écran.

`vh` peut également être utilisé pour définir des tailles de police qui répondent à la hauteur de la fenêtre d'affichage. C'est utile pour la typographie responsive. Lorsque vous ne voulez pas qu'un élément soit relatif au parent, vous pouvez utiliser `vh`.

Il peut y avoir des incohérences dans la manière dont les appareils interprètent l'unité `vh` en raison des variations entre les navigateurs, assurez-vous donc de l'utiliser avec précaution pour éviter les problèmes.

## Largeur de la fenêtre d'affichage (`vw`)

`vw` est similaire à `vh`, mais `vw` se réfère à la largeur de la fenêtre du navigateur. Il est utilisé pour définir des éléments basés sur l'axe horizontal de la fenêtre du navigateur.

Voici un exemple :

```
  <body>
    <div class="box"></div>
  </body>
```

Ici, la `box` est spécifiée à `50vw` de la largeur totale de la fenêtre d'affichage. À mesure que le navigateur rétrécit ou s'agrandit, observez comment la boîte s'ajuste pour maintenir la largeur spécifiée.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/EE2681DC-B4DB-4D9F-84E7-B7CBC435684B_1_201_a.jpeg) _L'élément box occupant 50% de la largeur de la fenêtre d'affichage_

`vw` est particulièrement utile et encouragé lorsque vous voulez qu'un élément occupe une certaine largeur de la fenêtre d'affichage. `vw` est également utilisé pour les tailles de police dans les media queries pour la typographie responsive.

## ch

`ch` est une unité relative qui se met à l'échelle en fonction de la largeur des caractères. `1ch` est égal à la largeur du caractère "0" dans la police actuelle.

```
    <div>
      <p>Some text specified with ch unit</p>
    </div>
```

```
body {
  font-family: 'Courier New', monospace; 
  margin: 0;
}
p {
    font-size: 2ch; 
    line-height: 1.5; 
  }
```

La taille de la police du texte à l'intérieur de l'élément `<p>` est définie pour être égale à deux fois la largeur du caractère "0" dans la police actuelle.

`ch` est particulièrement utile pour définir la longueur maximale de caractères sur une seule ligne. Il fournit une taille relative à la largeur des caractères, ce qui le rend flexible, adaptable et améliore la lisibilité. Il vous permet de définir une largeur maximale (`max-width`) pour les conteneurs de texte en fonction de la largeur des caractères.

## Pixels (`px`)

`px` est une unité de mesure absolue utilisée pour spécifier la longueur et les tailles. `px` est une unité fixe et doit être utilisée avec parcimonie et prudence pour le design responsive.

```
    <div class="container">
      <p>This element has a fixed size using px units.</p>
    </div>
```

```
.container {
    width: 300px; 
    padding: 20px;
    background-color: #f0f0f0;
  }

  p {
    font-size: 16px;
    color: #333;
  }
```

Dans cet extrait, la taille du texte `<p>` reste identique. Elle reste fixée à `16px` et ne change pas, que la taille du navigateur change ou non.

Lorsque vous redimensionnez le navigateur, vous observerez que le conteneur ne se met pas à l'échelle en fonction de la fenêtre d'affichage, et le texte ne se met pas non plus à l'échelle en fonction du conteneur.

La raison principale pour laquelle l'utilisation de `px` n'est pas toujours recommandée pour le design responsive réside dans sa nature fixe. Contrairement aux unités relatives, telles que les pourcentages, `em`, `rem` et les unités de fenêtre d'affichage (`vw`, `vh`), `px` ne s'ajuste pas en fonction des préférences de l'utilisateur ou de la taille de la fenêtre d'affichage.

`px` est utile lorsque vous souhaitez spécifier une taille fixe pour un élément, comme la taille d'une bordure ou d'une image.

Un exemple :

```
img {
    width: 200px;
    height: 150px;
}
```

## Conclusion

Ce sont les unités les plus fréquemment utilisées en CSS, il est donc important de savoir quand les utiliser.

Pour définir les tailles de police, vous utiliserez couramment `rem` ou `ch`. Pour la largeur, les pourcentages sont souvent recommandés. Vous pouvez également envisager d'utiliser `vw` et `ch`. Pour la hauteur, pensez à utiliser `%`, `rem` ou `vh`.

Pour le padding ou la marge, vous utiliserez typiquement `rem` ou `em` selon vos besoins spécifiques.

N'hésitez pas à vous référer à cet article chaque fois que vous avez besoin de conseils sur les meilleures unités pour définir des mesures ou des longueurs.

Merci de votre lecture !

[1]: #heading-rem-rem
[2]: #heading-em-em
[3]: #heading-pourcentages
[4]: #heading-hauteur-de-la-fenetre-daffichage-vh
[5]: #heading-largeur-de-la-fenetre-daffichage-vw
[6]: #heading-pixels-px