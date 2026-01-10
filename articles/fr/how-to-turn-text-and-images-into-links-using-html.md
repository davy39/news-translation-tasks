---
title: HTML Link – Comment transformer une image en lien et imbriquer des liens dans
  des paragraphes
subtitle: ''
author: Jessica Wilkins
co_authors: []
series: null
date: '2022-06-06T13:52:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-turn-text-and-images-into-links-using-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/markus-spiske--dbOrdtrR1A-unsplash.jpg
tags:
- name: HTML
  slug: html
seo_title: HTML Link – Comment transformer une image en lien et imbriquer des liens
  dans des paragraphes
seo_desc: 'There will be times where you will want to nest links inside paragraphs
  or turn an image into a link. But how do you go about doing that in HTML?

  In this article, I will show you how to nest links inside paragraphs and how to
  turn an image into a lin...'
---

Il y aura des moments où vous voudrez imbriquer des liens dans des paragraphes ou transformer une image en lien. Mais comment faire cela en HTML ?

Dans cet article, je vais vous montrer comment imbriquer des liens dans des paragraphes et comment transformer une image en lien en utilisant des exemples de code.

## **Comment imbriquer des balises d'ancrage dans des balises de paragraphe**

Si vous souhaitez inclure des liens dans vos paragraphes, vous pouvez imbriquer des balises d'ancrage dans les balises de paragraphe.

Dans ce premier exemple, nous avons le texte "J'adore freeCodeCamp".

```html
<p>J'adore freeCodeCamp</p>
```

Si je veux transformer le mot freeCodeCamp en lien, je l'enveloppe dans une paire de balises d'ancrage.

```html
<p>J'adore <a href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

Nous pouvons également ajouter l'attribut `target="_blank"` pour que ce lien s'ouvre dans un nouvel onglet.

```html
<p>J'adore <a target="_blank" href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

Lorsque vous passez votre souris sur le mot freeCodeCamp, vous remarquerez qu'il s'agit d'un lien sur lequel vous pouvez maintenant cliquer et qui vous dirigera vers le site web.

%[https://codepen.io/jessica-wilkins/pen/BaYVREm]

Imbriquer des liens dans des balises de paragraphe est utile lorsque vous souhaitez diriger vos utilisateurs vers des informations supplémentaires concernant le contenu principal de la page.

Dans cet exemple suivant, j'ai un paragraphe parlant des cours disponibles sur freeCodeCamp.

```html
<p>J'ai commencé à apprendre à coder en utilisant freeCodeCamp. J'ai vraiment apprécié leur cours de Responsive Web Design. J'ai hâte de commencer bientôt le cours de JavaScript.</p>
```

Je veux d'abord transformer le mot freeCodeCamp en lien pour diriger les gens vers le site web.

```html
<p>J'ai commencé à apprendre à coder en utilisant <a href="https://www.freecodecamp.org/">freeCodeCamp</a>. J'ai vraiment apprécié leur cours de Responsive Web Design. J'ai hâte de commencer bientôt le cours de JavaScript.</p>
```

Maintenant, je vais ajouter un autre lien pour "cours de Responsive Web Design" qui dirigera les gens vers le programme basé sur des projets.

```html
<p>J'ai commencé à apprendre à coder en utilisant <a href="https://www.freecodecamp.org/">freeCodeCamp</a>. J'ai vraiment apprécié leur <a href="https://www.freecodecamp.org/learn/2022/responsive-web-design/">cours de Responsive Web Design</a>. J'ai hâte de commencer bientôt le cours de JavaScript.</p>
```

Enfin, je vais ajouter un lien pour le cours de JavaScript, qui dirigera les utilisateurs vers le programme de JavaScript.

```html
<p>J'ai commencé à apprendre à coder en utilisant <a href="https://www.freecodecamp.org/">freeCodeCamp</a>. J'ai vraiment apprécié leur <a href="https://www.freecodecamp.org/learn/2022/responsive-web-design/">cours de Responsive Web Design</a>. J'ai hâte de commencer bientôt le <a href="https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/">cours de JavaScript</a>.</p>
```

Voici à quoi ressemblerait le résultat final dans un navigateur web :

%[https://codepen.io/jessica-wilkins/pen/ExQRmqY]

## Comment transformer une image en lien

En HTML, nous pouvons utiliser l'élément `<img>` pour ajouter des images sur la page. Dans cet exemple, nous ajoutons une image de cinq chats.

```html
<img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Cinq chats regardant autour d'un champ."/>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/06/Screen-Shot-2022-06-02-at-10.39.02-PM.png)

Si nous voulons faire de cette image un lien cliquable, nous pouvons la placer à l'intérieur d'une paire de balises d'ancrage.

```html
<a href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Cinq chats regardant autour d'un champ."/></a>
```

Nous pouvons également ajouter l'attribut `target="_blank"` pour que ce lien s'ouvre dans un nouvel onglet.

```html
<a target="_blank" href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Cinq chats regardant autour d'un champ."/></a>
```

Lorsque vous passez votre souris sur l'image, vous verrez le curseur de la souris indiquant qu'il s'agit d'un lien vous dirigeant vers un article sur les chats.

%[https://codepen.io/jessica-wilkins/pen/XWZYRgy?editors=1000]

## **Conclusion**

Dans cet article, nous avons appris comment imbriquer des balises d'ancrage dans des paragraphes et comment transformer des images en liens.

Pour ajouter des liens dans des paragraphes, nous pouvons imbriquer des balises d'ancrage dans des balises de paragraphe.

```html
<p>J'adore <a href="https://www.freecodecamp.org/">freeCodeCamp</a></p>
```

Pour transformer une image en lien, nous pouvons imbriquer un élément `img` dans des balises d'ancrage.

```html
<a href="https://en.wikipedia.org/wiki/Cat"><img src="https://cdn.freecodecamp.org/curriculum/cat-photo-app/cats.jpg" alt="Cinq chats regardant autour d'un champ."/></a>
```

J'espère que vous avez apprécié cet article et je vous souhaite bonne chance dans votre parcours de programmation.