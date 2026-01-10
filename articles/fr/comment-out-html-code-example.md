---
title: Commenter du HTML – Exemple de code
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-28T23:26:26.000Z'
originalURL: https://freecodecamp.org/news/comment-out-html-code-example
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/arrow-g4f0266a9e_1280.png
tags:
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Commenter du HTML – Exemple de code
seo_desc: 'Adding comments in your code is a good practice, as it makes your code
  more readable and understandable.

  Comments don’t run because they are ignored by compilers and interpreters.

  In this article, I will show you how you can comment out your HTML cod...'
---

Ajouter des commentaires dans votre code est une bonne pratique, car cela rend votre code plus lisible et compréhensible.

Les commentaires ne s'exécutent pas car ils sont ignorés par les compilateurs et les interpréteurs.

Dans cet article, je vais vous montrer comment commenter votre code HTML, afin de vous aider, vous et les membres de votre équipe, à comprendre ce que vous faites avec.

## Comment commenter du code HTML

Contrairement à d'autres langages de programmation qui ont différents symboles pour faire des commentaires multi-lignes et mono-ligne, vous utilisez les mêmes symboles pour les commentaires multi-lignes et mono-ligne en HTML.

Pour commenter du code HTML, utilisez le symbole inférieur à (`<`) suivi d'un point d'exclamation (`!`), de deux traits d'union (`--`), du commentaire, de deux traits d'union (`--`), et du symbole supérieur à (`>`).

La syntaxe pour commenter du HTML ressemble à ceci :

```html
<!-- commentaires ici -->
```

Vous pouvez utiliser ceci pour les commentaires mono-ligne :
```html
    <!-- Ceci est un commentaire mono-ligne -->
    <section class="about" id="about">
      <h3>Regardez les Jabs</h3>
      <p>
        Notre objectif principal est d'apporter des matchs de boxe en direct aux fans du monde entier
      </p>

      <h3>Ce n'est pas seulement les combats !</h3>
      <p>
        Nous diffusons également des documentaires spécialement conçus pour les grands, le mode de vie
        des boxeurs, les nouvelles, et plus encore.
      </p>
    </section>
```

Vous pouvez également l'utiliser pour les commentaires multi-lignes :

```html
    <section class="about" id="about">
      <h3>Regardez les Jabs</h3>
      <p>
        Notre objectif principal est d'apporter des matchs de boxe en direct aux fans du monde entier
      </p>
      <!-- Ceci est un 
        commentaire 
        multi-ligne -->
      <h3>Ce n'est pas seulement les combats !</h3>
      <p>
        Nous diffusons également des documentaires spécialement conçus pour les grands, le mode de vie
        des boxeurs, les nouvelles, et plus encore.
      </p>
    </section>
```

Vous pouvez également insérer le commentaire où vous le souhaitez, tant qu'il n'est pas à l'intérieur d'une balise :

```html
    <section class="about" id="about">
      <h3>Regardez les Jabs</h3>
      <p>
        Notre objectif principal est d'apporter des matchs de boxe en direct aux fans du monde entier
      </p>
      <h3>Ce n'est pas seulement les combats !</h3>
      <p>
        Nous diffusons également
        <!-- Ceci est un commentaire au milieu d'un texte -->
        des documentaires spécialement conçus pour les grands, le mode de vie des boxeurs, les nouvelles,
        et plus encore.
      </p>
    </section>
```

Et voilà – vous pouvez maintenant commenter votre code HTML correctement et en toute sécurité.

Merci d'avoir lu.