---
title: Comment utiliser le sélecteur :has() en CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-22T14:34:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-the-has-selector-in-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/pexels-alizee-marchand-947457.jpg
tags:
- name: CSS
  slug: css
- name: Web Development
  slug: web-development
seo_title: Comment utiliser le sélecteur :has() en CSS
seo_desc: "By James Charlesworth\nFor most of the history of CSS, selectors have been\
  \ limited to targeting elements based on their parents in the DOM tree. Consider\
  \ this HTML structure:\n<div>\n    <p>Paragraph 1</p>\n<div>\n<main>\n    <div>\n\
  \        <p>Paragraph 2</..."
---

Par James Charlesworth

Pendant la majeure partie de l'histoire de CSS, les sélecteurs ont été limités à cibler des éléments en fonction de leurs _parents_ dans l'arborescence DOM. Considérez cette structure HTML :

```html
<div>
    <p>Paragraphe 1</p>
<div>
<main>
    <div>
    	<p>Paragraphe 2</p>
    </div>
 <main>
```

Appliquer des styles au paragraphe 2 en CSS est trivial, car il peut être ciblé par le nœud parent `<main>`.

```css
main p {
    color: blue;
}
```

Cela stylisera _Paragraphe 2_ mais pas _Paragraphe 1_, car le deuxième paragraphe est contenu dans l'élément `<main>`.

Ce qui n'a pas été historiquement simple, cependant, était de styliser le nœud `<main>` en fonction de la présence de la balise `<p>` en dessous.

```html
<main>
    Ne pas styliser ceci
</main>
<main>
    <p>Styliser ceci</p>
</main>
```

En regardant vers le haut dans l'arborescence DOM, il n'y avait aucun moyen d'appliquer des styles uniquement au deuxième élément `<main>` et non au premier (sans utiliser de classes ou d'IDs, bien sûr).

## Introduction au sélecteur :has()

À sa base, le sélecteur `:has()` est une [pseudo-classe](https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes) relationnelle. Cela signifie qu'il permet de sélectionner un élément en fonction de sa relation avec d'autres éléments. Plus précisément, il sélectionne un élément s'il contient un autre élément qui correspond à un sélecteur donné.

Dans l'exemple ci-dessus, nous pouvons maintenant faire ce qui suit :

```css
main:has(p) {
    color: blue;
}
```

Cela ouvre de nombreuses possibilités pour styliser vos pages web de manière plus efficace et avec moins de code.

## Exemple 1 – Mettre en évidence les articles avec des images

Considérez une page web qui affiche une liste d'articles, chacun enfermé dans une balise `<article>`. Si nous voulons mettre en évidence les articles qui contiennent des images, le sélecteur `:has()` offre une solution simple :

```css
article:has(img) {
  border: 2px solid blue;
}
```

%[https://codepen.io/jcharlesworthuk/pen/gOEyGEM]

Cette règle CSS applique une bordure bleue autour de toute balise `<article>` qui contient un élément `<img>`, distinguant visuellement les articles avec images de ceux sans.

## Exemple 2 – Styliser les menus de navigation avec sous-menus

Voici un autre exemple. Dans cet exemple, le sélecteur `:has()` est utilisé pour ajouter un pseudo-élément `:before()` à tout élément de menu qui a des sous-menus – c'est-à-dire tout élément `<li>` qui contient un élément enfant avec la classe `.sub-menu`.

```css
.main-menu > li:has(.sub-menu):before {
  content: "▼";
  margin-left: 5px;
  font-size: 0.75em;
}
```

%[https://codepen.io/jcharlesworthuk/pen/LYavOOG]

## Support des navigateurs

En mars 2024, le sélecteur `:has()` est supporté par environ [92 % des navigateurs web dans le monde](https://caniuse.com/css-has), y compris tous les navigateurs modernes les plus courants tels que les dernières versions de Chrome, Firefox, Safari et Edge. Pour les navigateurs non supportés, envisagez d'utiliser des bibliothèques de détection de fonctionnalités comme [Modernizr](https://modernizr.com/docs/) pour appliquer des styles alternatifs.

Il est également judicieux de concevoir votre CSS pour qu'il se dégrade élégamment, en veillant à ce que vos pages web restent au moins fonctionnelles et visuellement acceptables dans les navigateurs qui ne supportent pas le sélecteur `:has()`.

## Prêt à être utilisé dès aujourd'hui

Le sélecteur `:has()` offre un nouveau niveau de flexibilité et de puissance en CSS, vous permettant d'écrire des feuilles de style plus propres et plus efficaces. En sélectionnant des éléments en fonction de leur contenu, le sélecteur `:has()` simplifie de nombreux défis de style courants, de la mise en évidence des articles avec images à la stylisation des mises en page réactives.

Alors que le support des navigateurs continue de croître, 2024 est l'année parfaite pour commencer à incorporer le sélecteur `:has()` dans votre CSS.

Bonne stylisation – et n'hésitez pas à essayer de mettre votre CSS en action dans l'un des projets pour débutants sur [https://traintocode.com/projects](https://traintocode.com/projects).