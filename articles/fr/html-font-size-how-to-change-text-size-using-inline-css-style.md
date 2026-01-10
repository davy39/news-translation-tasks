---
title: Taille de police HTML – Comment changer la taille du texte avec le style CSS
  en ligne
date: '2021-09-22T18:02:22.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/html-font-size-how-to-change-text-size-using-inline-css-style
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/fontsize-.png
tags:
- name: CSS
  slug: css
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
seo_desc: "In HTML, the font you choose will play a major role in the look and feel\
  \ of your web pages. \nYou get to pick the font's color, weight, size, and so on.\
  \ And all these features make your websites and apps look better and more presentable\
  \ to the user.\nW..."
---


En HTML, la police que vous choisissez joue un rôle majeur dans l'apparence et le ressenti de vos pages web.

<!-- more -->

Vous pouvez choisir la couleur, la graisse, la taille de la police, et ainsi de suite. Toutes ces caractéristiques permettent à vos sites et applications d'être plus esthétiques et plus présentables pour l'utilisateur.

Avec la propriété `font-size` en CSS, vous pouvez modifier la taille du texte sur la page web. Vous pouvez utiliser cette propriété dans n'importe quel type de CSS – externe, interne ou en ligne (inline).

Dans cet article, je vais vous montrer comment changer la taille du texte avec la propriété `font-size` en CSS en ligne.

## Qu'est-ce que le CSS en ligne ?

Le CSS en ligne est l'une des trois méthodes différentes que vous pouvez utiliser pour styliser n'importe quel élément HTML.

Au lieu de cibler l'élément avec un attribut `class` ou `id`, ou d'utiliser l'élément lui-même comme sélecteur pour le styliser, vous placez tous les styles CSS directement dans la balise ouvrante.

De plus, vous devez vous assurer que toutes les propriétés et valeurs de vos styles se trouvent à l'intérieur de l'attribut `style`. Cet attribut `style` est l'un des nombreux attributs acceptés par toutes les balises HTML.

Dans l'exemple ci-dessous, je change la couleur d'arrière-plan du texte en `crimson`, la couleur du texte en `#f1f1f1` (gris clair), et la graisse de la police en `bold` avec du CSS en ligne.

```
<p style="background-color: crimson; color: #f1f1f1; font-weight: bold">
      Hello Campers...
</p>
```

![exemple-style-en-ligne](https://www.freecodecamp.org/news/content/images/2021/09/inline-styling-example.png)

Au passage, mon navigateur est zoomé à un niveau de 400 %, c'est pourquoi tout paraît si grand. Je n'ai appliqué aucun style supplémentaire pour obtenir ce résultat :)

## Comment changer la taille du texte en utilisant le CSS en ligne

Pour modifier la taille de votre texte avec du CSS en ligne, vous devez utiliser l'attribut `style`. Vous renseignez la propriété `font-size`, puis vous lui attribuez une valeur.

Il existe des valeurs prédéfinies telles que `large`, `larger`, `medium`, `small`, `x-large`, etc. : ![proprietes-integrees](https://www.freecodecamp.org/news/content/images/2021/09/inbuilt-properties.png)

Dans l'extrait de code ci-dessous, je change la taille du texte "Hello Campers..." en `x-large`, l'une des valeurs intégrées de la propriété `font-size`.

```
<p style="font-size: x-large">Hello Campers...</p>
```

![style-police-avec-valeur-integree](https://www.freecodecamp.org/news/content/images/2021/09/font-style-with-inbuilt-value.png)

Vous pouvez également définir la valeur de la propriété `font-size` en utilisant un nombre avec n'importe quelle unité telle que les pixels (`px`), le `rem` ou l' `em`.

Il est préférable d'opter pour des valeurs chiffrées car elles vous donnent plus de liberté pour choisir la taille de police exacte que vous souhaitez.

Dans l'extrait de code ci-dessous, j'ai modifié la taille du texte à `30px` avec du CSS en ligne :

```
<p style="font-size: 30px">Hello Campers...</p>
```

![style-police-avec-valeur-chiffree](https://www.freecodecamp.org/news/content/images/2021/09/font-style-with-numbered-value.png)

## Conclusion

Dans cet article, vous avez appris comment changer la taille du texte avec le CSS en ligne et la propriété `font-size`. Vous avez également vu comment attribuer des valeurs à cette propriété.

Un petit avertissement cependant : le CSS en ligne est pratique pour le stylisage ponctuel, mais vous ne devriez pas vous reposer exclusivement dessus car il rend votre HTML difficile à lire, surtout si vous travaillez en équipe. Vous ne voulez pas être le seul capable de relire votre propre code.

Sachez également qu'il surcharge (override) tout style défini avec du CSS interne ou externe. Vous devriez privilégier le style externe ou interne, car ils permettent de séparer vos codes HTML et CSS, ce qui est préférable pour la lisibilité.

Lors de l'attribution de valeurs à la propriété `font-size`, il est préférable d'utiliser l'unité `rem` plutôt que le `px`, par exemple. En effet, lorsque vous utilisez le `rem`, le navigateur est capable d'ajuster la taille de la police lorsque l'utilisateur effectue un zoom avant ou arrière, ce qui n'est pas le cas avec le `px`.

Merci de m'avoir lu, et bon code !