---
title: CSS Text Align – Exemple de style de texte centré, justifié, aligné à droite
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-28T17:30:39.000Z'
originalURL: https://freecodecamp.org/news/css-text-align-centered-justified-right-aligned-text-style-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/cssTextAlign.png
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: CSS Text Align – Exemple de style de texte centré, justifié, aligné à droite
seo_desc: "We use the CSS text-align property to align content inside a block-level\
  \ element. \nExamples of block-level elements are paragraphs (<p>...</p>), divs\
  \ (<div>...</div>), sections (<section>...</section>), articles (<article>...</article>),\
  \ and so on.\nT..."
---

Nous utilisons la propriété CSS `text-align` pour aligner le contenu à l'intérieur d'un élément de niveau bloc. 

Les exemples d'éléments de niveau bloc sont les paragraphes (`<p>...</p>`), les divs (`<div>...</div>`), les sections (`<section>...</section>`), les articles (`<article>...</article>`), et ainsi de suite.

Cet alignement n'affecte que l'axe horizontal. Ainsi, la propriété `text-align` est différente de la propriété `vertical-align` que nous utilisons pour définir l'alignement vertical d'un élément.

## Table des matières
- [Syntaxe de base](#heading-syntaxe-de-base)
- [Valeurs de la propriété `text-align`](#heading-valeurs-de-la-propriete-text-align)
- [La valeur `left`](#heading-la-valeur-left)
- [La valeur `center`](#heading-la-valeur-center)
- [La valeur `right`](#heading-la-valeur-right)
- [La valeur `justify`](#heading-la-valeur-justify)
- [La valeur `inherit`](#heading-la-valeur-inherit)
- [Conclusion](#heading-conclusion)

## Syntaxe de base 

Voici la syntaxe de base pour la propriété `text-align` :

```css
block-level-element {
      text-align: value;
    }
```

Nous allons maintenant examiner les différentes valeurs qu'elle peut prendre pour vous aider à positionner les éléments sur la page.

## Valeurs de la propriété `text-align`

La propriété `text-align` accepte les valeurs `left`, `center`, `right`, `justify` et `inherit`.

Nous allons examiner ces valeurs une par une.

Avant de plonger dans les valeurs et leur apparence dans le navigateur, jetons un coup d'œil au CSS ci-dessous. J'ai défini ces styles pour une meilleure visibilité, afin que vous puissiez voir les choses plus clairement :

```css
   body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
    }

    div {
      background-color: #adadad;
      width: 40rem;
      height: 4rem;
      padding: 3rem 0.5rem;
    }
```

### La valeur `left`

La valeur `left` de la propriété `text-align` est celle par défaut. Ainsi, tout le contenu à l'intérieur d'un élément de niveau bloc est aligné à gauche par défaut.

```css
 div {
      text-align: left;
    }
```
![ss-1-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-3.png)

Si vous souhaitez que le contenu à l'intérieur d'un élément de niveau bloc soit aligné à gauche, vous n'avez pas besoin de lui attribuer une valeur `text-align` de `left`. Si vous le faites, vous dupliquez simplement ce qui est déjà la valeur par défaut.

### La valeur `center`

Avec la valeur `center`, des espaces sont créés à gauche et à droite, de sorte que tout est poussé vers le centre. 

Si vous souhaitez aligner le contenu à l'intérieur d'un élément de niveau bloc au centre, la valeur `center` est votre meilleur choix. 

```css
  div {
      text-align: center;
    }
```
![ss-2-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-3.png)

### La valeur `right`

Attribuer une valeur `right` à la propriété `text-align` pousse le contenu à l'intérieur d'un élément de niveau bloc vers la droite.

```css
  div {
      text-align: right;
    }
```
![ss-3-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-4.png)

### La valeur `justify`

La valeur `justify` de la propriété `text-align` aligne le contenu sur les bords gauche et droit de l'élément de niveau bloc (la boîte). Si la dernière ligne n'est pas une ligne complète, elle la laisse telle quelle. Il est plus facile de voir comment cela fonctionne dans l'image ci-dessous : 

```css
 div {
      text-align: justify;
    }
```
![ss-4-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-4.png)

### La valeur `inherit`

La valeur `inherit` de la propriété `text-align` se comporte comme son nom l'indique. Un élément dont la valeur `text-align` est définie sur `inherit` hérite de la valeur `text-align` de son parent direct.

```css
 div {
      text-align: inherit;
    }
```
![ss-5-5](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-5.png)

Dans ce cas, notre `div` hérite de la valeur `text-align` du body, qui est `left` par défaut.

Si la valeur `text-align` du `body` est définie sur `right`, et que celle du `div` est laissée à `inherit`, le texte à l'intérieur du `div` s'aligne à droite.

```css
 body {
      text-align: right;
    }

    div {
      text-align: inherit;
    }
```
![ss-6-1](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-1.png)

## Conclusion

Dans cet article, vous avez appris la propriété CSS `text-align` et ses valeurs. 

Les exemples que nous avons examinés ici pour voir comment les valeurs se comportent contenaient uniquement du texte, vous vous demandez donc peut-être si les valeurs fonctionnent également sur les images. Eh bien, oui, c'est le cas.

Ci-dessous se trouve une image à l'intérieur d'une div avec `text-align` défini sur center :

```html
 <div>
      <img
        src="coming-soon.jpg"
        alt="coming_soon"
        width="74px"
        height="54px"
      />
</div>
```
```css
 div {
      text-align: center;
    }
```
![ss-7-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-7-2.png)

Merci d'avoir lu.