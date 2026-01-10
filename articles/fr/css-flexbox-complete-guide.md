---
title: CSS Flexbox Expliqué – Guide Complet des Conteneurs Flexibles et des Éléments
  Flexibles
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2022-10-28T14:28:24.000Z'
originalURL: https://freecodecamp.org/news/css-flexbox-complete-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/css-flexbox-complete-guide-codesweetly-pexels-chris-f-6664375.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: CSS Flexbox Expliqué – Guide Complet des Conteneurs Flexibles et des Éléments
  Flexibles
seo_desc: 'CSS Flexbox gives you the tools to create basic and advanced website layouts
  in flexible and responsive ways.

  This tutorial discusses everything you need to know to use Flexbox like a pro.

  Table of Contents


  What Is Flexbox?

  Flex Container vs. Flex I...'
---

CSS Flexbox vous donne les outils pour créer des mises en page de sites web basiques et avancées de manière flexible et réactive.

Ce tutoriel aborde tout ce que vous devez savoir pour utiliser Flexbox comme un pro.

## Table des Matières

1. [Qu'est-ce que Flexbox ?](#heading-qu-est-ce-que-flexbox)
2. [Conteneur Flexible vs. Élément Flexible : Quelle est la Différence ?](#heading-conteneur-flexible-vs-element-flexible-quelle-est-la-difference)
3. [Qu'est-ce qu'une valeur `flex` en CSS ?](#heading-qu-est-ce-qu-une-valeur-flex-en-css)
4. [Qu'est-ce qu'une valeur `inline-flex` en CSS ?](#heading-qu-est-ce-qu-une-valeur-inline-flex-en-css)
5. [Propriétés pour Spécifier la Mise en Page de Flexbox](#heading-proprietes-pour-specifier-la-mise-en-page-de-flexbox)
6. [Quelles sont les Propriétés des Conteneurs Flexibles ?](#heading-quelles-sont-les-proprietes-des-conteneurs-flexibles)
7. [Qu'est-ce que la Propriété `flex-direction` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-flex-direction-de-flexbox)
8. [Qu'est-ce que la Propriété `flex-wrap` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-flex-wrap-de-flexbox)
9. [Qu'est-ce que la Propriété `flex-flow` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-flex-flow-de-flexbox)
10. [Qu'est-ce que la Propriété `justify-content` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-justify-content-de-flexbox)
11. [Qu'est-ce que la Propriété `align-items` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-align-items-de-flexbox)
12. [Qu'est-ce que la Propriété `align-content` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-align-content-de-flexbox)
13. [Quelles sont les Propriétés des Éléments Flexibles ?](#heading-quelles-sont-les-proprietes-des-elements-flexibles)
14. [Qu'est-ce que la Propriété `align-self` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-align-self-de-flexbox)
15. [Qu'est-ce que la Propriété `order` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-order-de-flexbox)
16. [Qu'est-ce que la Propriété `flex-grow` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-flex-grow-de-flexbox)
17. [Qu'est-ce que la Propriété `flex-shrink` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-flex-shrink-de-flexbox)
18. [Qu'est-ce que la Propriété `flex-basis` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-flex-basis-de-flexbox)
19. [Qu'est-ce que la Propriété `flex` de Flexbox ?](#heading-qu-est-ce-que-la-propriete-flex-de-flexbox)
20. [Comment Centrer des Éléments Horizontalement avec Flexbox](#heading-comment-centrer-des-elements-horizontalement-avec-flexbox)
21. [Comment Centrer des Éléments Verticalement avec Flexbox](#heading-comment-centrer-des-elements-verticalement-avec-flexbox)
22. [Comment Centrer des Éléments Horizontalement et Verticalement avec Flexbox](#heading-comment-centrer-des-elements-horizontalement-et-verticalement-avec-flexbox)
23. [Aperçu](#heading-aperçu)

Alors, sans plus attendre, comprenons ce qu'est Flexbox.

## Qu'est-ce que Flexbox ?

**Flexbox** permet aux navigateurs d'afficher les éléments HTML sélectionnés comme des modèles de boîte flexibles.

Flexbox permet un redimensionnement et un repositionnement faciles d'un conteneur flexible et de ses éléments de manière unidimensionnelle.

**Note :**

* "Unidimensionnelle" signifie que Flexbox permet de disposer les modèles de boîte en ligne ou en colonne à la fois. En d'autres termes, Flexbox ne peut pas disposer les modèles de boîte en ligne et en colonne en même temps.
* Flexbox est parfois appelé un module de disposition de boîte flexible.
* Utilisez le [module de disposition de grille](https://codesweetly.com/css-grid-explained) si vous devez redimensionner et repositionner des éléments de manière bidimensionnelle.

## Conteneur Flexible vs. Élément Flexible : Quelle est la Différence ?

Un **conteneur flexible** est un [élément HTML](https://codesweetly.com/web-tech-terms-h#html-element) dont la valeur de la propriété [`display`](https://codesweetly.com/css-display-property) est `flex` ou `inline-flex`.

Les **éléments flexibles** sont les enfants directs d'un conteneur flexible.

![Illustration d'un conteneur flexible et d'un élément flexible](https://www.freecodecamp.org/news/content/images/2022/10/css-flex-container-flex-item-illustration-codesweetly.png)
_Un conteneur flexible (la grande zone jaune dans l'image) est un élément HTML dont la valeur de la propriété display est flex ou inline-flex. Les éléments flexibles (les petites boîtes dans le conteneur jaune) sont les enfants directs d'un conteneur flexible._

## Qu'est-ce qu'une valeur `flex` en CSS ?

`flex` indique aux navigateurs d'afficher l'élément HTML sélectionné comme un modèle de boîte flexible de niveau bloc.

En d'autres termes, définir la valeur de la propriété `display` d'un élément sur `flex` transforme le modèle de boîte en une [boîte flexible de niveau bloc](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements).

**Voici un exemple :**

```css
section {
  display: flex;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-gctvuc?file=style.css)

L'extrait ci-dessus a utilisé la valeur `flex` pour convertir les éléments `<section>` du document HTML de nœuds `<section>` réguliers en modèles de boîte flexibles de niveau bloc.

**Note :**

* Convertir un nœud HTML en un modèle de boîte flexible fait des enfants directs de l'élément des éléments flexibles.
* La directive `display: flex` n'affecte qu'un modèle de boîte et ses enfants directs. Elle n'affecte pas les nœuds petits-enfants.

Discutons maintenant de `inline-flex`.

## Qu'est-ce qu'une valeur `inline-flex` en CSS ?

`inline-flex` indique aux navigateurs d'afficher l'élément HTML sélectionné comme un modèle de boîte flexible de niveau en ligne.

En d'autres termes, définir la valeur de la propriété `display` d'un élément sur `inline-flex` transforme le modèle de boîte en une [boîte flexible de niveau en ligne](https://developer.mozilla.org/en-US/docs/Web/HTML/Inline_elements).

**Voici un exemple :**

```css
section {
  display: inline-flex;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ksagv8?file=style.css)

L'extrait ci-dessus a utilisé la valeur `inline-flex` pour convertir les éléments `<section>` du document HTML de nœuds `<section>` réguliers en modèles de boîte flexibles de niveau en ligne.

**Note :**

* Convertir un nœud HTML en un modèle de boîte flexible fait des enfants directs de l'élément des éléments flexibles.
* La directive `display: inline-flex` n'affecte qu'un modèle de boîte et ses enfants directs. Elle n'affecte pas les nœuds petits-enfants.

## Propriétés pour Spécifier la Mise en Page de Flexbox

En convertissant un élément HTML régulier en un modèle de boîte `flex` (ou `inline-flex`), Flexbox fournit deux catégories de propriétés pour positionner la boîte flexible et ses enfants directs :

* Propriétés des conteneurs flexibles
* Propriétés des éléments flexibles

## Quelles sont les Propriétés des Conteneurs Flexibles ?

Les propriétés d'un conteneur flexible spécifient comment les navigateurs doivent disposer les éléments à l'intérieur du modèle de boîte flexible.

**Note :** Nous définissons une propriété de conteneur flexible sur le conteneur flexible, pas sur ses éléments.

Les six (6) types de propriétés de conteneur flexible sont :

* `flex-direction`
* `flex-wrap`
* `flex-flow`
* `justify-content`
* `align-items`
* `align-content`

Discutons maintenant des six types.

## Qu'est-ce que la Propriété `flex-direction` de Flexbox ?

**flex-direction** indique aux navigateurs la direction spécifique (ligne ou colonne) dans laquelle ils doivent disposer les enfants directs d'un conteneur flexible.

En d'autres termes, `flex-direction` définit l'[axe principal](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference) d'une boîte flexible.

![Illustration de l'axe principal et de l'axe transversal d'une boîte flexible](https://www.freecodecamp.org/news/content/images/2022/10/css-flexbox-main-axis-cross-axis-illustration-codesweetly.png)
_L'axe principal d'une boîte flexible est l'orientation de la disposition définie par une propriété flex-direction. Son axe transversal est l'orientation perpendiculaire à l'axe principal._

**Voici un exemple :**

```css
section {
  display: flex;
  flex-direction: column;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-jtpqir?file=style.css)

L'extrait ci-dessus a organisé les éléments des conteneurs `<section>` flexibles dans la direction de la colonne de la langue par défaut de votre navigateur.

**Astuce :** Utilisez `flex-direction: column-reverse` (ou `flex-direction: row-reverse`) pour inverser la direction de la disposition du navigateur.

## Qu'est-ce que la Propriété `flex-wrap` de Flexbox ?

**flex-wrap** spécifie si les navigateurs doivent envelopper les éléments flexibles débordants sur plusieurs lignes.

La propriété `flex-wrap` accepte les valeurs suivantes :

* `nowrap`
* `wrap`
* `wrap-reverse`

Discutons des trois valeurs.

### Qu'est-ce que `flex-wrap: nowrap` dans Flexbox CSS ?

`nowrap` est la valeur par défaut de `flex-wrap`. Elle force tous les éléments à l'intérieur d'un conteneur flexible sur une seule ligne (c'est-à-dire, direction en ligne ou en colonne).

En d'autres termes, `nowrap` indique aux navigateurs de _ne pas_ envelopper les éléments d'un conteneur flexible.

**Note :** Supposons que la largeur totale (ou la hauteur) de tous les éléments dans un conteneur flexible est supérieure à la largeur (ou la hauteur) de la boîte flexible. Dans un tel cas, `nowrap` provoquera le débordement des éléments hors du conteneur.

**Voici un exemple :**

```css
section {
  width: 130px;
  display: flex;
  flex-wrap: nowrap;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-yn6yw8?file=style.css)

L'extrait ci-dessus a utilisé `nowrap` pour forcer les navigateurs à disposer les éléments des conteneurs flexibles sur une seule ligne.

### Qu'est-ce que `flex-wrap: wrap` dans Flexbox CSS ?

`wrap` déplace tous les éléments débordants à l'intérieur d'un conteneur flexible vers la ligne suivante.

En d'autres termes, `wrap` indique aux navigateurs d'envelopper les éléments débordants d'un conteneur flexible.

**Voici un exemple :**

```css
section {
  width: 130px;
  display: flex;
  flex-wrap: wrap;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-78ez1m?file=style.css)

Nous avons utilisé `wrap` pour envelopper les éléments débordants des conteneurs flexibles vers la ligne suivante.

### Qu'est-ce que `flex-wrap: wrap-reverse` dans Flexbox CSS ?

`wrap-reverse` déplace tous les éléments débordants à l'intérieur d'un conteneur flexible vers la ligne suivante dans l'ordre inverse.

**Note :** `wrap-reverse` fait la même chose que `wrap`—mais dans l'ordre inverse.

**Voici un exemple :**

```css
section {
  width: 130px;
  display: flex;
  flex-wrap: wrap-reverse;
  background-color: orange;
  margin: 10px;
  padding: 7px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-eyqxtf?file=style.css)

Nous avons utilisé `wrap-reverse` pour envelopper les éléments débordants des conteneurs flexibles vers la ligne suivante dans l'ordre inverse.

## Qu'est-ce que la Propriété `flex-flow` de Flexbox ?

**flex-flow** est une abréviation pour les propriétés `flex-direction` et `flex-wrap`.

En d'autres termes, au lieu d'écrire :

```css
section {
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}
```

Vous pouvez alternativement utiliser la propriété `flex-flow` pour raccourcir votre code comme suit :

```css
section {
  display: flex;
  flex-flow: column wrap;
}
```

## Qu'est-ce que la Propriété `justify-content` de Flexbox ?

**justify-content** spécifie comment les navigateurs doivent positionner les éléments d'un conteneur flexible le long de l'[axe principal](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference) de la boîte flexible.

La propriété `justify-content` accepte les valeurs suivantes :

* `flex-start`
* `center`
* `flex-end`
* `space-between`
* `space-around`
* `space-evenly`

Discutons de ces six valeurs.

### Qu'est-ce que `justify-content: flex-start` dans Flexbox CSS ?

`flex-start` est la valeur par défaut de `justify-content`. Elle aligne les éléments d'un conteneur flexible avec le bord principal de l'axe principal de la boîte flexible.

![Illustration de la valeur flex-start de justify-content](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-flex-start-illustration-codesweetly.png)
_flex-start aligne les éléments d'un conteneur flexible avec le côté principal de l'axe principal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: flex-start;
  background-color: orange;
  margin: 10px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ma7svj?file=style.css)

L'extrait ci-dessus a utilisé la valeur `flex-start` pour aligner les éléments du conteneur flexible avec le bord principal de la boîte flexible.

### Qu'est-ce que `justify-content: center` dans Flexbox CSS ?

`center` aligne les éléments d'un conteneur flexible au centre de l'axe principal de la boîte flexible.

![Illustration de la valeur center de justify-content](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-center-illustration-codesweetly.png)
_center aligne les éléments d'un conteneur flexible au centre de l'axe principal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: center;
  background-color: orange;
  margin: 10px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-jfzcwc?file=style.css)

Nous avons utilisé la valeur `center` pour aligner les éléments du conteneur flexible au centre de la boîte flexible.

### Qu'est-ce que `justify-content: flex-end` dans Flexbox CSS ?

`flex-end` aligne les éléments d'un conteneur flexible avec le côté final de l'axe principal de la boîte flexible.

![Illustration de la valeur flex-end de justify-content](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-flex-end-illustration-codesweetly.png)
_flex-end aligne les éléments d'un conteneur flexible avec le côté final de l'axe principal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: flex-end;
  background-color: orange;
  margin: 10px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-iyhlbr?file=style.css)

Nous avons utilisé la valeur `flex-end` pour aligner les éléments du conteneur flexible avec le côté final de la boîte flexible.

### Qu'est-ce que `justify-content: space-between` dans Flexbox CSS ?

`space-between` fait ce qui suit :

* Il aligne le premier élément d'un conteneur flexible avec le bord principal de l'axe principal de la boîte flexible.
* Il aligne le dernier élément du conteneur avec le bord final de l'axe principal de la boîte flexible.
* Il crée un espacement uniforme entre chaque paire d'éléments entre le premier et le dernier élément.

![Illustration de la valeur space-between de justify-content](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-space-between-illustration-codesweetly.png)
_space-between crée un espacement uniforme entre chaque paire d'éléments entre le premier et le dernier élément._

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: space-between;
  background-color: orange;
  margin: 10px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-dylovp?file=style.css)

L'extrait ci-dessus a utilisé la valeur `space-between` pour créer un espacement uniforme entre chaque paire d'éléments entre le premier et le dernier élément flexible.

### Qu'est-ce que `justify-content: space-around` dans Flexbox CSS ?

`space-around` attribue un espacement égal à chaque côté des éléments d'un conteneur flexible.

Par conséquent, l'espace avant le premier élément et après le dernier élément est la moitié de la largeur de l'espace entre chaque paire d'éléments.

![Illustration de la valeur space-around de justify-content](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-space-around-illustration-codesweetly.png)
_space-around attribue un espacement égal à chaque côté des éléments d'un conteneur flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: space-around;
  background-color: orange;
  margin: 10px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-t6wpcj?file=style.css)

L'extrait ci-dessus a utilisé la valeur `space-around` pour attribuer un espacement égal à chaque côté des éléments du conteneur flexible.

### Qu'est-ce que `justify-content: space-evenly` dans Flexbox CSS ?

`space-evenly` attribue un espacement uniforme aux deux extrémités d'un conteneur flexible et entre ses éléments.

![Illustration de la valeur space-evenly de justify-content](https://www.freecodecamp.org/news/content/images/2022/10/css-justify-content-space-evenly-illustration-codesweetly.png)
_space-evenly attribue un espacement uniforme aux deux extrémités d'un conteneur flexible et entre ses éléments._

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: space-evenly;
  background-color: orange;
  margin: 10px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-p67eh8?file=style.css)

Nous avons utilisé la valeur `space-evenly` pour attribuer un espacement uniforme aux deux extrémités de la boîte flexible et entre ses éléments.

Discutons maintenant du cinquième type de propriété de conteneur flexible.

## Qu'est-ce que la Propriété `align-items` de Flexbox ?

**align-items** spécifie comment les navigateurs doivent positionner les éléments d'un conteneur flexible le long de l'[axe transversal](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference) de la boîte flexible.

La propriété `align-items` accepte les valeurs suivantes :

* `stretch`
* `flex-start`
* `center`
* `flex-end`
* `baseline`

Discutons des cinq valeurs.

### Qu'est-ce que `align-items: stretch` dans Flexbox CSS ?

`stretch` est la valeur par défaut de `align-items`. Elle étire les éléments d'un conteneur flexible pour remplir l'axe transversal de la boîte flexible.

![Illustration de la valeur stretch de align-items](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-stretch-illustration-codesweetly.png)
_stretch étire les éléments d'un conteneur flexible pour remplir l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  align-items: stretch;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ezugee?file=style.css)

L'extrait ci-dessus a utilisé la valeur `stretch` pour étirer les éléments flexibles afin de remplir l'axe transversal de `<section>`.

### Qu'est-ce que `align-items: flex-start` dans Flexbox CSS ?

`flex-start` aligne les éléments d'un conteneur flexible avec le bord de départ transversal de l'axe transversal de la boîte flexible.

![Illustration de la valeur flex-start de align-items](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-flex-start-illustration-codesweetly.png)
_flex-start aligne les éléments d'un conteneur flexible avec le bord de départ transversal de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  align-items: flex-start;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-cjzhj2?file=style.css)

Nous avons utilisé la valeur `flex-start` pour aligner les éléments flexibles avec le bord de départ transversal de l'axe transversal de `<section>`.

### Qu'est-ce que `align-items: center` dans Flexbox CSS ?

`center` aligne les éléments d'un conteneur flexible au centre de l'axe transversal de la boîte flexible.

![Illustration de la valeur center de align-items](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-center-illustration-codesweetly.png)
_center aligne les éléments d'un conteneur flexible au centre de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  align-items: center;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ywexqr?file=style.css)

L'extrait ci-dessus a utilisé la valeur `center` pour aligner les éléments flexibles au centre de l'axe transversal de `<section>`.

### Qu'est-ce que `align-items: flex-end` dans Flexbox CSS ?

`flex-end` aligne les éléments d'un conteneur flexible avec le bord final transversal de l'axe transversal de la boîte flexible.

![Illustration de la valeur flex-end de align-items](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-flex-end-illustration-codesweetly.png)
_flex-end aligne les éléments d'un conteneur flexible avec le bord final transversal de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  align-items: flex-end;
  background-color: orange;
  margin: 10px;
  height: 300px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-bwdeyz?file=style.css)

Nous avons utilisé la valeur `flex-end` pour aligner les éléments flexibles avec le bord final transversal de l'axe transversal de `<section>`.

### Qu'est-ce que `align-items: baseline` dans Flexbox CSS ?

`baseline` aligne les éléments d'un conteneur flexible avec la [ligne de base](https://stackoverflow.com/a/34611670/11841906) de l'axe transversal de la boîte flexible.

![Illustration de la valeur baseline de align-items](https://www.freecodecamp.org/news/content/images/2022/10/css-align-items-baseline-illustration-codesweetly.png)
_baseline aligne les éléments d'un conteneur flexible avec la ligne de base de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  align-items: baseline;
  background-color: orange;
  margin: 10px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-xxvj57?file=style.css)

L'extrait ci-dessus a utilisé la valeur `baseline` pour aligner les éléments flexibles avec la ligne de base de `<section>`.

Maintenant, parlons du sixième type de propriété de conteneur flexible CSS.

## Qu'est-ce que la Propriété `align-content` de Flexbox ?

**align-content** spécifie comment les navigateurs doivent positionner les lignes d'un conteneur flexible le long de l'[axe transversal](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference) de la boîte flexible.

**Note :** La propriété `align-content` n'affecte pas une boîte flexible avec une seule ligne—par exemple, un conteneur flexible avec `flex-wrap: nowrap`. En d'autres termes, `align-content` fonctionne uniquement sur les boîtes flexibles avec plusieurs lignes.

La propriété `align-content` accepte les valeurs suivantes :

* `stretch`
* `flex-start`
* `center`
* `flex-end`
* `space-between`
* `space-around`
* `space-evenly`

Discutons des sept valeurs.

### Qu'est-ce que `align-content: stretch` dans Flexbox CSS ?

`stretch` est la valeur par défaut de `align-content`. Elle étire les lignes du conteneur flexible pour remplir l'axe transversal de la boîte flexible.

![Illustration de la valeur stretch de align-content](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-stretch-illustration-codesweetly.png)
_stretch étire les lignes du conteneur flexible pour remplir l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: stretch;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-dway6n?file=style.css)

L'extrait ci-dessus a utilisé la valeur `stretch` pour étirer les lignes de la boîte flexible afin de remplir l'axe transversal de `<section>`.

### Qu'est-ce que `align-content: flex-start` dans Flexbox CSS ?

`flex-start` aligne les lignes d'un conteneur flexible avec le bord de départ transversal de l'axe transversal de la boîte flexible.

![Illustration de la valeur flex-start de align-content](https://www.freecodecamp.org/news/content/images/2022/10/css-content-flex-start-illustration-codesweetly.png)
_flex-start aligne les lignes d'un conteneur flexible avec le bord de départ transversal de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-c9pzbc?file=style.css)

L'extrait ci-dessus a utilisé la valeur `flex-start` pour aligner les lignes de la boîte flexible avec le bord de départ transversal de l'axe transversal de `<section>`.

### Qu'est-ce que `align-content: center` dans Flexbox CSS ?

`center` aligne les lignes d'un conteneur flexible au centre de l'axe transversal de la boîte flexible.

![Illustration de la valeur center de align-content](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-center-illustration-codesweetly.png)
_center aligne les lignes d'un conteneur flexible au centre de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-j3poyu?file=style.css)

Nous avons utilisé la valeur `center` pour aligner les lignes de la boîte flexible au centre de l'axe transversal de `<section>`.

### Qu'est-ce que `align-content: flex-end` dans Flexbox CSS ?

`flex-end` aligne les lignes d'un conteneur flexible avec le bord final transversal de l'axe transversal de la boîte flexible.

![Illustration de la valeur flex-end de align-content](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-flex-end-illustration-codesweetly.png)
_flex-end aligne les lignes d'un conteneur flexible avec le bord final transversal de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-end;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-cmaz6z?file=style.css)

Nous avons utilisé la valeur `flex-end` pour aligner les lignes de la boîte flexible avec le bord final transversal de l'axe transversal de `<section>`.

### Qu'est-ce que `align-content: space-between` dans Flexbox CSS ?

`space-between` fait ce qui suit :

* Il aligne la première ligne de la boîte flexible avec le bord de départ principal de l'axe principal du conteneur flexible.
* Il aligne la dernière ligne de la boîte flexible avec le côté final principal de l'axe principal du conteneur flexible.
* Il crée un espacement égal entre chaque paire de lignes entre la première et la dernière ligne.

![Illustration de la valeur space-between de align-content](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-space-between-illustration-codesweetly.png)
_space-between crée un espacement égal entre chaque paire de lignes entre la première et la dernière ligne_

**Voici un exemple :**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: space-between;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-kltdwx?file=style.css)

L'extrait ci-dessus a utilisé la valeur `space-between` pour créer un espacement égal entre chaque paire de lignes entre la première et la dernière ligne.

### Qu'est-ce que `align-content: space-around` dans Flexbox CSS ?

`space-around` attribue un espacement égal à chaque côté des lignes d'un conteneur flexible.

Par conséquent, l'espace avant la première ligne et après la dernière est la moitié de la largeur de l'espace entre chaque paire de lignes.

![Illustration de la valeur space-around de align-content](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-space-around-illustration-codesweetly.png)
_space-around attribue un espacement égal à chaque côté des lignes d'un conteneur flexible._

**Voici un exemple :**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: space-around;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-kx9gdy?file=style.css)

L'extrait ci-dessus a utilisé la valeur `space-around` pour attribuer un espacement égal à chaque côté des lignes du conteneur flexible.

### Qu'est-ce que `align-content: space-evenly` dans Flexbox CSS ?

`space-evenly` attribue un espacement uniforme aux deux extrémités d'un conteneur flexible et entre ses lignes.

![Illustration de la valeur space-evenly de align-content](https://www.freecodecamp.org/news/content/images/2022/10/css-align-content-space-evenly-illustration-codesweetly.png)
_space-evenly attribue un espacement uniforme aux deux extrémités d'un conteneur flexible et entre ses lignes._

**Voici un exemple :**

```css
section {
  display: flex;
  flex-wrap: wrap;
  align-content: space-evenly;
  background-color: orange;
  margin: 10px;
  width: 90px;
  height: 500px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-eevqoj?file=style.css)

Nous avons utilisé la valeur `space-evenly` pour attribuer un espacement uniforme aux deux extrémités de la boîte flexible et entre ses lignes.

Maintenant que nous connaissons les types de propriétés de conteneur flexible CSS, nous pouvons discuter des propriétés des éléments flexibles.

## Quelles sont les Propriétés des Éléments Flexibles ?

Les propriétés d'un élément flexible spécifient comment les navigateurs doivent disposer un élément spécifié à l'intérieur du modèle de boîte flexible.

**Note :** Nous définissons une propriété d'élément flexible sur l'élément flexible, pas sur son conteneur.

Les six (6) types de propriétés d'élément flexible sont :

* `align-self`
* `order`
* `flex-grow`
* `flex-shrink`
* `flex-basis`
* `flex`

Discutons des six types maintenant.

## Qu'est-ce que la Propriété `align-self` de Flexbox ?

**align-self** spécifie comment les navigateurs doivent positionner les éléments flexibles sélectionnés le long de l'[axe transversal](https://codesweetly.com/css-flex-direction-property#main-axis-vs-cross-axis-whats-the-difference) de la boîte flexible.

**Note :**

* `align-self` n'affecte que l'élément flexible sélectionné—pas tous les éléments de la boîte flexible.
* `align-self` remplace la propriété `align-items`.

La propriété `align-self` accepte les valeurs suivantes :

* `stretch`
* `flex-start`
* `center`
* `flex-end`
* `baseline`

Discutons des cinq valeurs.

### Qu'est-ce que `align-self: stretch` dans Flexbox CSS ?

`stretch` étire les éléments flexibles sélectionnés pour remplir l'axe transversal de la boîte flexible.

![Illustration de la valeur stretch de align-self](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-stretch-illustration-codesweetly.png)
_stretch étire le(s) élément(s) flexible(s) sélectionné(s) pour remplir l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
.flex-item2 {
  align-self: stretch;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-o5qr62?file=style.css)

Nous avons utilisé la valeur `stretch` pour étirer `flex-item2` afin de remplir l'axe transversal de son conteneur.

### Qu'est-ce que `align-self: flex-start` dans Flexbox CSS ?

`flex-start` aligne les éléments flexibles sélectionnés avec le bord de départ transversal de l'axe transversal de la boîte flexible.

![Illustration de la valeur flex-start de align-self](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-flex-start-illustration-codesweetly.png)
_flex-start aligne le(s) élément(s) flexible(s) sélectionné(s) avec le bord de départ transversal de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
.flex-item2 {
  align-self: flex-start;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-6uianm?file=style.css)

L'extrait ci-dessus a utilisé la valeur `flex-start` pour aligner `flex-item2` avec le bord de départ transversal de l'axe transversal de son conteneur.

### Qu'est-ce que `align-self: center` dans Flexbox CSS ?

`center` aligne les éléments flexibles sélectionnés au centre de l'axe transversal de la boîte flexible.

![Illustration de la valeur center de align-self](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-center-illustration-codesweetly.png)
_center aligne le(s) élément(s) flexible(s) sélectionné(s) au centre de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
.flex-item2 {
  align-self: center;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-tazf2p?file=style.css)

L'extrait ci-dessus a utilisé la valeur `center` pour aligner `flex-item2` au centre de l'axe transversal de son conteneur.

### Qu'est-ce que `align-self: flex-end` dans Flexbox CSS ?

`flex-end` aligne les éléments flexibles sélectionnés avec le bord final transversal de l'axe transversal de la boîte flexible.

![Illustration de la valeur flex-end de align-self](https://www.freecodecamp.org/news/content/images/2022/10/css-align-self-flex-end-illustration-codesweetly.png)
_flex-end aligne le(s) élément(s) flexible(s) sélectionné(s) avec le bord final transversal de l'axe transversal de la boîte flexible._

**Voici un exemple :**

```css
.flex-item2 {
  align-self: flex-end;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-7bec4q?file=style.css)

L'extrait ci-dessus a utilisé la valeur `flex-end` pour aligner `flex-item2` avec le bord final transversal de l'axe transversal de son conteneur.

### Qu'est-ce que `align-self: baseline` dans Flexbox CSS ?

`baseline` aligne les éléments flexibles sélectionnés avec la [ligne de base](https://stackoverflow.com/a/34611670/11841906) de l'axe transversal de la boîte flexible.

**Voici un exemple :**

```css
.flex-item2 {
  font-size: 3rem;
  align-self: baseline;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-wmawek?file=style.css)

Nous avons utilisé la valeur `baseline` pour aligner `flex-item2` avec la ligne de base de son conteneur.

Discutons maintenant du deuxième type de propriété d'élément flexible.

## Qu'est-ce que la Propriété `order` de Flexbox ?

**order** change l'ordre par défaut (l'arrangement) d'un élément flexible.

En d'autres termes, `order` vous permet de repositionner un élément d'une boîte flexible sans modifier la disposition du code HTML.

**Voici un exemple :**

```html
<ul style="display: flex; flex-direction: column">
  <li style="order: 6">1</li>
  <li style="order: 4">2</li>
  <li style="order: 1">3</li>
  <li style="order: 7">4</li>
  <li style="order: 2">5</li>
  <li style="order: 5">6</li>
  <li style="order: 3">7</li>
</ul>
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-hmz9my?file=index.html)

L'extrait HTML ci-dessus a utilisé la propriété `order` pour changer l'arrangement de la liste non ordonnée.

Ainsi, au lieu de l'ordre suivant :

* 1
* 2
* 3
* 4
* 5
* 6
* 7

Le navigateur affichera ceci :

* 3
* 5
* 7
* 2
* 6
* 1
* 4

Utilisez la propriété `order` avec prudence, car elle empêche les lecteurs d'écran d'accéder à l'ordre de lecture correct d'un document HTML. Utilisez-la uniquement si c'est super important d'utiliser CSS pour changer la disposition du code HTML.

Mais dans la plupart des cas, il est préférable de réorganiser directement le code HTML plutôt que d'utiliser CSS.

**Note :** La syntaxe `style="value"`, dans l'extrait HTML ci-dessus, est la technique [CSS en ligne](https://codesweetly.com/inline-vs-internal-vs-external-css#what-is-an-inline-css) pour styliser les éléments HTML.

## Qu'est-ce que la Propriété `flex-grow` de Flexbox ?

**flex-grow** indique aux navigateurs combien de l'espace restant de la boîte flexible ils doivent ajouter à la taille de l'élément flexible sélectionné.

**Note :** Un espace restant fait référence à l'espace restant après que les navigateurs ont déduit la somme des tailles de tous les éléments flexibles de la taille de la boîte flexible.

**Voici un exemple :**

```css
.flex-item3 {
  flex-grow: 0.5;
}
```

```html
<section>
  <div class="flex-item1">1</div>
  <div class="flex-item2">2</div>
  <div class="flex-item3">3</div>
  <div class="flex-item4">4</div>
</section>
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-grtdo1?file=style.css)

Nous avons utilisé la propriété `flex-grow` pour faire en sorte que les navigateurs ajoutent la moitié de l'espace restant de `<section>` à la taille de `flex-item3`.

**Note :** La valeur par défaut de `flex-grow` est `0`.

## Qu'est-ce que la Propriété `flex-shrink` de Flexbox ?

**flex-shrink** indique aux navigateurs combien l'élément flexible spécifié doit rétrécir lorsque la somme des tailles de tous les éléments dépasse la taille de la boîte flexible.

En d'autres termes, supposons que la taille de la boîte flexible est insuffisante pour contenir les éléments flexibles. Dans ce cas, les navigateurs rétréciront les éléments pour les adapter au conteneur.

Par conséquent, `flex-shrink` vous permet de spécifier le facteur de rétrécissement d'un élément flexible.

**Voici un exemple :**

```css
.flex-item3 {
  flex-shrink: 0;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-h2numw?file=style.css)

Nous avons utilisé la propriété `flex-shrink` pour empêcher les navigateurs de rétrécir `flex-item3`.

**Note :**

* Les navigateurs ne rétréciront pas les éléments flexibles avec une valeur `flex-shrink` de `0`.
* La valeur par défaut de `flex-shrink` est `1`.

## Qu'est-ce que la Propriété `flex-basis` de Flexbox ?

**flex-basis** définit la longueur initiale d'un élément flexible.

**Voici un exemple :**

```css
.flex-item3 {
  flex-basis: 100px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-kwcche?file=style.css)

Nous avons utilisé la propriété `flex-basis` pour définir la longueur initiale de `flex-item3` à `100px`.

**Notez ce qui suit :**

* `auto` est la valeur par défaut de `flex-basis`.
* Une valeur `flex-basis` (autre que `auto`) a une spécificité plus élevée que `width` (ou `height`). Par conséquent, supposons que vous définissez les deux pour un élément flexible. Dans ce cas, les navigateurs utiliseront `flex-basis`.
* La propriété `flex-basis` définit la largeur initiale de la [boîte de contenu](https://codesweetly.com/css-box-model#what-is-a-content-box). Mais vous pouvez utiliser la propriété [box-sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) pour qu'elle définisse la largeur de la [boîte de bordure](https://codesweetly.com/css-box-model#what-is-a-border-box) à la place.

## Qu'est-ce que la Propriété `flex` de Flexbox ?

**flex** est une abréviation pour les propriétés `flex-grow`, `flex-shrink` et `flex-basis`.

En d'autres termes, au lieu d'écrire :

```css
.flex-item3 {
  flex-grow: 0.5;
  flex-shrink: 0;
  flex-basis: 100px;
}
```

Vous pouvez alternativement utiliser la propriété `flex` pour raccourcir votre code comme suit :

```css
.flex-item3 {
  flex: 0.5 0 100px;
}
```

**Notez ce qui suit :**

* `flex: auto` est équivalent à `flex: 1 1 auto`.
* `flex: none` est équivalent à `flex: 0 0 auto`.
* `flex: initial` définit la propriété `flex` à sa valeur par défaut. Il est équivalent à `flex: 0 1 auto`.
* `flex: inherit` hérite des valeurs de la propriété `flex` de son élément parent.

Maintenant que nous connaissons les propriétés de Flexbox que les développeurs utilisent pour disposer les boîtes flexibles et leurs enfants directs, nous pouvons discuter de la manière de centrer les éléments avec Flexbox.

## Comment Centrer des Éléments Horizontalement avec Flexbox

Vous pouvez centrer n'importe quel élément horizontalement dans son conteneur en :

* Définissant sa propriété `display` du conteneur sur `flex`
* Définissant la propriété `justify-content` du conteneur flexible sur `center`

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: center;
  background-color: orange;
  width: 100%;
  height: 400px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-trl46e?file=style.css)

## Comment Centrer des Éléments Verticalement avec Flexbox

Vous pouvez centrer n'importe quel élément verticalement dans son conteneur en :

* Définissant sa propriété `display` du conteneur sur `flex`
* Définissant la propriété `align-items` du conteneur flexible sur `center`

**Voici un exemple :**

```css
section {
  display: flex;
  align-items: center;
  background-color: orange;
  width: 100%;
  height: 400px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-tm1don?file=style.css)

## Comment Centrer des Éléments Horizontalement et Verticalement avec Flexbox

Vous pouvez centrer n'importe quel élément HTML horizontalement et verticalement dans son conteneur en :

* Définissant sa propriété `display` du conteneur sur `flex`
* Définissant les propriétés `justify-content` et `align-items` du conteneur flexible sur `center`

**Voici un exemple :**

```css
section {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: orange;
  width: 100%;
  height: 400px;
}
```

[**Essayez-le sur StackBlitz**](https://stackblitz.com/edit/js-ryzwmq?file=style.css)

## Aperçu

Dans cet article, nous avons discuté de tous les outils Flexbox dont vous avez besoin pour créer des mises en page de sites web basiques et avancées de manière flexible et réactive.

### Merci d'avoir lu !

Si vous aimez les images que j'ai utilisées dans ce tutoriel, vous pouvez toutes les obtenir dans [ce livret](https://store.codesweetly.com/l/css-flexbox-explained-visually).

### Et voici une ressource utile sur ReactJS :

J'ai écrit un livre sur React !

* Il est adapté aux débutants ✅
* Il contient des extraits de code en direct ✅
* Il contient des projets évolutifs ✅
* Il contient de nombreux exemples faciles à comprendre ✅

Le livre [React Explained Clearly](https://www.amazon.com/dp/B09KYGDQYW) est tout ce dont vous avez besoin pour comprendre ReactJS.

[![Livre React Explained Clearly Disponible Maintenant sur Amazon](https://www.freecodecamp.org/news/content/images/2022/01/Twitter-React_Explained_Clearly-CodeSweetly-Oluwatobi_Sofela.jpg)](https://www.amazon.com/dp/B09KYGDQYW)