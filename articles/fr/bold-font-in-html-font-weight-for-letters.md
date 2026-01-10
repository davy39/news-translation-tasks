---
title: Police en gras en HTML – Poids de la police pour les lettres
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-08-31T20:35:21.000Z'
originalURL: https://freecodecamp.org/news/bold-font-in-html-font-weight-for-letters
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/boldfont.png
tags:
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Police en gras en HTML – Poids de la police pour les lettres
seo_desc: "When you're building a website, you may want to place particular emphasis\
  \ on certain text to let users know that it's important. \nAnd you can do this in\
  \ HTML with various text formatting tags. \nIn this article, I will take you through\
  \ how to emphasiz..."
---

Lorsque vous construisez un site web, vous pouvez vouloir mettre l'accent sur certains textes pour indiquer aux utilisateurs qu'ils sont importants.

Et vous pouvez le faire en HTML avec diverses balises de formatage de texte.

Dans cet article, je vais vous expliquer comment mettre en évidence certains textes en les mettant en gras.

En HTML, il existe trois principales façons de mettre du texte en gras. Vous pouvez utiliser la balise `<b>`, la balise `<strong>`, ou le faire en CSS avec la propriété `font-weight`. Examinons chaque méthode plus en détail.

## Comment mettre du texte en gras avec la balise `<b>` en HTML

HTML nous donne la balise `<b>` pour mettre du texte en gras. Pour mettre du texte en gras avec cette balise, vous devez l'entourer comme ceci :

```html
<p><b>Ce texte est en gras</b>, mais ce texte ne l'est pas.</p>
```
![bold-with-b-tag](https://www.freecodecamp.org/news/content/images/2021/08/bold-with-b-tag.png)

Comme vous pouvez le voir sur l'image, la balise fait ressortir une partie du texte.

## Comment mettre du texte en gras avec la balise `<strong>` en HTML

Avec la balise `<strong>`, vous ne mettez pas seulement le texte en gras – vous attirez une attention particulière sur lui.

`<strong>` met également le texte en gras comme la balise `<b>`, mais il y a une légère différence entre les deux. J'en discuterai plus tard dans l'article.

Comme pour la balise `<b>`, vous devez entourer le texte avec la balise `<strong>` pour le mettre en gras.

```html
<p>
   Avant de payer pour apprendre la programmation, consultez
   <strong>freeCodeCamp</strong>.
</p>
```

![bold-with-strong-tag](https://www.freecodecamp.org/news/content/images/2021/08/bold-with-strong-tag.png)

Avec la balise `<strong>`, le texte `freeCodeCamp` n'est pas seulement en gras, il a une signification sémantique et une emphase.

## Comment mettre du texte en gras avec la propriété CSS `font-weight`

La propriété font-weight prend les valeurs `lighter`, `bold` et `bolder`. Elle prend également des nombres de 100 à 900. Ainsi, avec elle, vous ne mettez pas seulement le texte en gras, vous pouvez également le rendre plus léger que le texte environnant.

Pour mettre certains textes en gras avec la propriété font-weight, vous devez sélectionner le texte avec sa classe, son id (le cas échéant) ou son élément, puis appliquer les valeurs souhaitées. Voici comment cela fonctionne :

```html
<p>Ceci est un <span class="lighter">texte plus léger</span>.</p>

<p>Ceci est un <span class="bold">texte en gras</span>.</p>

<p>Ceci est un <span class="bolder">texte plus gras</span>.</p>
```

```css
 .lighter {
    font-weight: lighter;
}

.bold {
    font-weight: bold;
}

.bolder {
    font-weight: bolder;
}
```

![bold-with-fontweight](https://www.freecodecamp.org/news/content/images/2021/08/bold-with-fontweight.png)

## Doit-on utiliser `<b>`, `<strong>` ou `font-weight` pour mettre du texte en gras ?

Vous vous demandez peut-être laquelle de ces méthodes utiliser pour mettre du texte en gras – `<b>`, `<strong>` ou la propriété CSS `font-weight`.

Vous devriez généralement éviter d'utiliser `<b>` car c'est déjà un style. Lorsque vous mettez du texte en gras avec la balise `<b>`, vous dites explicitement au navigateur de mettre le texte en gras directement depuis le HTML.

`<strong>` fait également apparaître le texte en gras, mais il est sémantique. Avec lui, vous ne stylisez pas depuis le HTML (ce pour quoi HTML n'était pas destiné à l'origine), mais plutôt vous dites au navigateur de faire apparaître le texte plus fort que les autres textes environnants.

La propriété CSS `font-weight` vous donne plus de contrôle sur la légèreté ou l'audace du texte. Les valeurs `lighter`, `bold` et `bolder` sont un début, mais vous pouvez aller plus loin en appliquant des nombres/poids comme `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800` et `900` comme valeurs, ce qui donne différentes variations de légèreté et d'audace.

## Conclusion

La police en gras vous aide à mettre l'accent sur certains mots en HTML. Dans cet article, vous avez appris les 3 différentes façons de mettre du texte en gras, ainsi que celle qui est la meilleure à utiliser.

Merci d'avoir lu, et continuez à coder.