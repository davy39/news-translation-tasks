---
title: Balises HTML Span VS Div – Quelle est la différence ?
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-08T21:08:38.000Z'
originalURL: https://freecodecamp.org/news/span-vs-div-html-tags-what-is-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/spanvdiv.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Balises HTML Span VS Div – Quelle est la différence ?
seo_desc: 'If you inspect a web page with your browser''s developer tools, you''ll
  likely see a bunch of nested div tags, and possibly some content wrapped in a span
  tag.

  Similar content is usually grouped together by these two container elements – span
  and div. ...'
---

Si vous inspectez une page web avec les outils de développement de votre navigateur, vous verrez probablement un ensemble de balises `div` imbriquées, et peut-être du contenu enveloppé dans une balise `span`.

Un contenu similaire est généralement regroupé par ces deux éléments conteneurs – `span` et `div`. Vous pouvez les utiliser tous les deux comme conteneurs, mais ils ne fonctionnent pas tout à fait de la même manière.

Dans ce tutoriel, je vais vous montrer les différences entre span et div afin que vous ne soyez plus confus lorsque vous devrez les utiliser.

## Les différences clés entre les balises `span` et `div`

Vous pouvez utiliser les balises `span` et `div` comme conteneur si vous souhaitez rendre une partie particulière de la page web distincte et la styliser différemment. Mais encore une fois, elles ne servent pas exactement le même but.

### La balise HTML div

La balise div est un élément générique de niveau bloc utilisé pour associer et regrouper une grande partie d'une page web – généralement une section telle qu'un en-tête, un pied de page, le contenu principal, etc.

Dans l'exemple ci-dessous, je regroupe l'en-tête d'une page web avec la balise `div` et je l'ai stylisé en utilisant CSS.

```html
<div class="header">
      <h2 class="logo">freeCodeCamp</h2>

      <ul class="nav">
        <li><a href="">Accueil</a></li>
        <li><a href="">À propos</a></li>
        <li><a href="">Services</a></li>
        <li><a href="">Contact</a></li>
      </ul>
</div>
```

Dans le CSS ci-dessous, j'ai disposé l'en-tête et la barre de navigation avec CSS Flexbox. J'ai également supprimé la marge et le remplissage par défaut attribués aux éléments par les navigateurs.

```css
* {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

.header {
      padding: 0 70px;
      display: flex;
      align-content: center;
      justify-content: space-between;
      margin-top: 20px;
      margin-bottom: 20px;
      color: crimson;
    }

.nav {
      display: flex;
      align-content: center;
      justify-content: center;
      gap: 60px;
      list-style-type: none;
    }

.nav li a {
      text-decoration: none;
      font-size: 1.2rem;
      color: crimson;
    }
```

![header-with-div](https://www.freecodecamp.org/news/content/images/2021/09/header-with-div.png)

De plus, vous pouvez utiliser la balise div pour regrouper du contenu similaire ensemble. Cela peut être du texte, des images, des vidéos, etc. Ainsi, vous pouvez toujours imbriquer des divs dans des divs, et leur attacher des classes ou des identifiants uniques pour ne pas vous perdre.

### La balise HTML `span`

La balise `span` est un élément en ligne que vous utilisez pour faire ressortir une petite partie de contenu avec CSS ou JavaScript. Vous ne devriez pas imbriquer de span sauf si vous savez parfaitement ce que vous faites – mais vous pouvez placer plusieurs balises span dans un élément de niveau bloc.

Dans l'exemple ci-dessous, j'ai fait ressortir certains mots en les enveloppant avec des balises span et en les stylisant différemment.

```html
<p>
      Ceci est un <span class="crimson">texte crimson</span> parmi des textes noirs.
      Ceci est un <span class="indigo">texte indigo</span> parmi d'autres, et ceci
      est un <span class="orange">texte orange</span> parmi d'autres textes.
</p>
```

```css
body {
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 900px;
    margin: 0 auto;
    height: 100vh;
  }

p {
    font-size: 2.5rem;
  }

.font-style {
    font-style: italic;
  }

.crimson {
    color: crimson;
  }

.indigo {
    color: indigo;
  }

.orange {
    color: orange;
  }
```

![span-in-action](https://www.freecodecamp.org/news/content/images/2021/09/span-in-action.png)

Vous pouvez voir les différences les plus importantes entre les balises `span` et `div` dans le tableau ci-dessous :

| Balise `span`      | Balise `div` |
| ----------- | ----------- |
| Élément de niveau en ligne      | Élément de niveau bloc       |
| Utilisé pour regrouper de petits morceaux de texte   | Utilisé pour regrouper de grands morceaux de texte ensemble        |
| Ne doit pas être imbriqué pour éviter la confusion   | Généralement imbriqué        |


## Quand utiliser `span` ou `div` ?

Vous devriez utiliser `span` lorsque vous souhaitez styliser une partie particulière de votre contenu différemment ou la manipuler avec JavaScript. Vous pouvez également l'utiliser comme conteneur pour des éléments en ligne.

Vous devriez utiliser la balise `div`, en revanche, si vous souhaitez regrouper de grandes parties de contenu ensemble, et lorsque vous souhaitez disposer des éléments sur la page web.

## Conclusion

Dans ce tutoriel, vous avez appris les différences entre les balises span et div.

Ces balises sont essentielles pour le style et les mises en page. Gardez à l'esprit que HTML5 a introduit des éléments sémantiques tels que `section`, `header`, `nav`, `footer`, et autres. Donc, en général, vous devriez utiliser soit `span` soit `div` uniquement lorsque les éléments sémantiques ne correspondent pas à ce que vous voulez faire.

Merci d'avoir lu, et continuez à coder.