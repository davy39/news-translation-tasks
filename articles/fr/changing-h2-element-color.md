---
title: Changer la couleur de l'élément H2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:14:00.000Z'
originalURL: https://freecodecamp.org/news/changing-h2-element-color
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa8740569d1a4ca26ea.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
seo_title: Changer la couleur de l'élément H2
seo_desc: 'In coding there are often many different solutions to a given problem.
  This is especially true when it comes to styling an HTML element.

  One of the easiest things to change is the color of text. But sometimes it seems
  like nothing you try is working:...'
---

En programmation, il existe souvent de nombreuses solutions différentes à un problème donné. Cela est particulièrement vrai lorsqu'il s'agit de styliser un élément HTML.

L'une des choses les plus faciles à changer est la couleur du texte. Mais parfois, il semble que rien de ce que vous essayez ne fonctionne :

```html
<style>
  h2 .red-text {
    color: red;
  }
</style>

<h2 class="red-text" color=red;>CatPhotoApp</h2>
```

Alors, comment changer la couleur de l'élément H2 en rouge ?

### Option #1 : CSS en ligne

Une solution serait d'utiliser le CSS en ligne pour styliser directement l'élément.

Comme avec les autres méthodes, le formatage est important. Regardez à nouveau le code ci-dessus :

```html
<h2 class="red-text" color=red;>CatPhotoApp</h2>
```

Pour utiliser le style en ligne, assurez-vous d'utiliser l'attribut `style`, et d'encadrer les propriétés et valeurs avec des guillemets doubles ("):

```html
<h2 class="red-text" style="color: red;">CatPhotoApp</h2>
```

### Option #2 : Utiliser des sélecteurs CSS

Plutôt que d'utiliser le style en ligne, vous pourriez séparer votre HTML, ou la structure et le contenu de la page, du style, ou CSS.

Tout d'abord, supprimez le CSS en ligne :

```html
<style>
  h2 .red-text {
    color: red;
  }
</style>

<h2 class="red-text">CatPhotoApp</h2>
```

Mais vous devez être prudent avec le sélecteur CSS que vous utilisez. Regardez l'élément `<style>` :

```css
h2 .red-text {
  color: red;
}
```

Lorsqu'il y a un espace, le sélecteur `h2 .red-text` indique au navigateur de cibler l'élément avec la classe `red-text` qui est enfant de `h2`. Cependant, l'élément H2 n'a pas d'enfant – vous essayez de styliser l'élément H2 lui-même.

Pour corriger cela, supprimez l'espace :

```css
h2.red-text {
  color: red;
}
```

Ou ciblez simplement la classe `red-text` directement :

```css
.red-text {
  color: red;
}
```