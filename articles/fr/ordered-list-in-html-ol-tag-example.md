---
title: Liste ordonnée en HTML – Exemple de balise OL
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-01-31T18:34:40.000Z'
originalURL: https://freecodecamp.org/news/ordered-list-in-html-ol-tag-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/oltag--1-.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Liste ordonnée en HTML – Exemple de balise OL
seo_desc: 'An ordered list is a list in which the items are numbered and the order
  matters.

  This is as opposed to an unordered list where the items are bulleted by default
  (and the order doesn''t matter).

  Basic Syntax of the <ol> tag

  The <ol> tag defines ordered...'
---

Une liste ordonnée est une liste dans laquelle les éléments sont numérotés et l'ordre compte.

Cela s'oppose à une liste non ordonnée où les éléments sont précédés de puces par défaut (et l'ordre n'a pas d'importance).

## Syntaxe de base de la balise `<ol>`

La balise `<ol>` définit les listes ordonnées en HTML. Et les éléments de la liste sont définis par la balise `<li>`.

La balise `<ol>` n'est pas un élément vide, donc elle a une balise de fermeture en `</ol>`
```html
<ol>
      <li>...</li>
      <li>...</li>
      <li>...</li>
</ol>
```

Dans les navigateurs, les listes ordonnées apparaissent comme des listes numérotées, comme ceci :
```html
<ol>
   <li>HTML</li>
   <li>CSS</li>
   <li>JavaScript</li>
   <li>Tailwind</li>
   <li>React</li>
   <li>Mongo DB</li>
   <li>React</li>
</ol>
```
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-4.png)

Si vous vous demandez pourquoi les éléments de la liste sont centrés sur la page, ce CSS l'a rendu possible :
```css
body {
      display: grid;
      place-items: center;
      height: 100vh;
    }
```

## Attributs de la balise `<ol>`

La balise `<ol>` accepte `start`, `type` et `reversed` comme attributs.

### L'attribut `type`

L'attribut `type` est utilisé pour spécifier quel type de numérotation vous souhaitez utiliser pour la liste.

Par défaut, ce sont des chiffres arabes.

Les types de listes qui peuvent être utilisés sont :

- `1` pour les chiffres arabes (par défaut)

```html
<ol type="1">
   <li>HTML</li>
   <li>CSS</li>
   <li>JavaScript</li>
   <li>Tailwind</li>
   <li>React</li>
   <li>Mongo DB</li>
   <li>React</li>
</ol>
```
![ss-1-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-1-4.png)

**P.S. :** Si vous utiliserez des chiffres arabes comme type de numérotation, vous n'avez pas besoin de le spécifier car c'est le type par défaut.

- `A` pour les lettres majuscules

```html
<ol type="A">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-2-4](https://www.freecodecamp.org/news/content/images/2022/01/ss-2-4.png)

- `a` pour les lettres minuscules

```html
<ol type="a">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-3-5](https://www.freecodecamp.org/news/content/images/2022/01/ss-3-5.png)

- `i` pour les chiffres romains minuscules

```html
<ol type="i">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-4-5](https://www.freecodecamp.org/news/content/images/2022/01/ss-4-5.png)

- `I` pour les chiffres romains majuscules

```html
<ol type="I">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-5-6](https://www.freecodecamp.org/news/content/images/2022/01/ss-5-6.png)

### L'attribut `start`

L'attribut start peut être utilisé pour spécifier à quel numéro commencer la liste. Il accepte donc un entier comme valeur. La valeur par défaut est 1.

Si vous spécifiez un nombre comme 22, l'élément de liste suivant prend le numéro suivant 23, et ainsi de suite...

```html
<ol start="22">
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-6-2](https://www.freecodecamp.org/news/content/images/2022/01/ss-6-2.png)

### L'attribut `reversed`

Lorsque vous utilisez l'attribut `reversed` sur une liste ordonnée, les éléments de la liste sont rendus dans l'ordre inverse. C'est-à-dire, du nombre le plus élevé au plus bas.

Vous n'avez pas besoin de spécifier une valeur pour l'attribut `reversed` car toute valeur que vous spécifiez sera ignorée.

```html
<ol reversed>
  <li>HTML</li>
  <li>CSS</li>
  <li>JavaScript</li>
  <li>Tailwind</li>
  <li>React</li>
  <li>Mongo DB</li>
  <li>React</li>
</ol>
```
![ss-7-3](https://www.freecodecamp.org/news/content/images/2022/01/ss-7-3.png)

## Conclusion

Dans cet article, vous avez appris à propos de la balise `<ol>` et de ses attributs, afin d'avoir plus de contrôle sur celle-ci dans vos projets.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.