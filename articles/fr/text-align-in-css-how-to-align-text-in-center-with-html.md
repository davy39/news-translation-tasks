---
title: Alignement du texte en CSS – Comment centrer du texte avec HTML
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-04-26T19:08:29.000Z'
originalURL: https://freecodecamp.org/news/text-align-in-css-how-to-align-text-in-center-with-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/nick-karvounis-TkZYCXmrKK4-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Alignement du texte en CSS – Comment centrer du texte avec HTML
seo_desc: 'There will be many times where you will need to center some text using
  HTML and CSS. But what is the best way to go about that?

  In this article, I will show you how to use the text-align property in CSS and show
  you how to vertically align text using...'
---

Il y aura de nombreuses occasions où vous devrez centrer du texte en utilisant HTML et CSS. Mais quelle est la meilleure façon de procéder ?

Dans cet article, je vais vous montrer comment utiliser la propriété `text-align` en CSS et vous montrer comment aligner verticalement du texte en utilisant CSS Flexbox. Je vais également parler de la balise `<center>` et pourquoi vous ne devriez pas l'utiliser pour centrer du texte.

## Comment utiliser la propriété `text-align` en CSS

Lorsque vous travaillez avec des balises d'en-tête ou de paragraphe, le style par défaut en HTML positionnera le texte sur le côté gauche de la page.

Dans cet exemple, nous avons un `<h1>` qui est placé dans le coin supérieur gauche de la page.

```html
<h1 class="title">Apprenons à centrer du texte</h1>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-11.41.12-AM.png)

Si nous voulons centrer horizontalement ce texte sur la page, nous pouvons utiliser la propriété `text-align`.

```css
.title {
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-11.42.48-AM.png)

Si vous voulez centrer horizontalement tout le texte de la page, vous pouvez utiliser la propriété `text-align` dans le sélecteur body.

Dans cet exemple suivant, nous avons plus de texte dans notre HTML.

```html
<h1>freeCodeCamp est génial</h1>
<section>
  <h2>J'adore apprendre le HTML</h2>
  <p>Voici mon premier paragraphe</p>
</section>

<section>
  <h2>J'adore apprendre le CSS</h2>
  <p>Voici mon deuxième paragraphe</p>
</section>
```

Sans aucun style, cela ressemble actuellement à ceci sur la page.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.30.14-PM.png)

Dans notre CSS, nous pouvons cibler le sélecteur `body` et utiliser la propriété `text-align`.

```css
body {
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.29.56-PM.png)

## Comment centrer du texte horizontalement et verticalement

La propriété `text-align` est utilisée pour centrer horizontalement du texte sur la page. Mais nous pouvons également utiliser CSS Flexbox pour centrer verticalement le texte.

Dans cet exemple, nous avons du texte dans notre HTML :

```html
<h2 class="title">Apprenons à centrer du texte verticalement et horizontalement</h2>

<div class="flex-container">
  <p>Flexbox est génial !!!</p>
</div>
```

Voici à quoi cela ressemble actuellement sans aucun style.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.35.30-PM.png)

Nous pouvons centrer le `<h2>` en utilisant la propriété `text-align`.

```css
.title {
  text-align: center;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.42.49-PM.png)

Nous pouvons ensuite centrer horizontalement et verticalement le paragraphe à l'intérieur de la div `flex-container` en utilisant Flexbox.

```css
.flex-container {
  display: flex;

  /*ci-ce centre le texte horizontalement*/
  justify-content: center;

  /*ci-ce centre le texte verticalement*/
  align-items: center;

  height: 200px;
  color: #fff;
  font-size: 1.2rem;
  background: #00008b;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.58.57-PM.png)

## Devriez-vous utiliser la balise center ?

Dans les anciennes versions de HTML, la balise `<center>` était utilisée pour centrer horizontalement du texte sur la page.

```html
<center>J'utilise des balises center pour centrer mon texte
  <p>Ce paragraphe est également centré</p>
</center>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.14.09-PM.png)

Beaucoup de nouveaux développeurs utilisent encore cette balise car elle affiche les résultats corrects. Cependant, la balise `<center>` a été dépréciée dans HTML 4 car la meilleure pratique est d'utiliser la propriété CSS `text-align` à la place.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Screen-Shot-2022-04-24-at-12.16.58-PM.png)
_Ceci est l'avertissement de dépréciation des [docs MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/center)_

Il est important de se rappeler que HTML est pour le contenu tandis que CSS est pour le style. Il est préférable de séparer ces deux préoccupations et de ne pas utiliser HTML à des fins de style.

J'espère que vous avez apprécié cet article sur la façon de centrer du texte en utilisant HTML et CSS.