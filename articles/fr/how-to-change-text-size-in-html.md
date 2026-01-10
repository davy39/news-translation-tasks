---
title: Taille de la police HTML – Comment changer la taille du texte avec une balise
  HTML
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-08-04T14:52:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-text-size-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/cover-template--6-.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
seo_title: Taille de la police HTML – Comment changer la taille du texte avec une
  balise HTML
seo_desc: 'When you add text to your HTML file with an HTML tag, you won''t always
  want the text to remain the default size. You''ll want to be able to adjust how
  the text displays in the browser.

  In this article, you will learn how to change the text size with a...'
---

Lorsque vous ajoutez du texte à votre fichier HTML avec une balise HTML, vous ne voudrez pas toujours que le texte reste de la taille par défaut. Vous voudrez pouvoir ajuster la manière dont le texte s'affiche dans le navigateur.

Dans cet article, vous apprendrez comment changer la taille du texte avec une balise HTML.

Avant de continuer, il est essentiel de savoir qu'il n'y a qu'une seule façon de faire cela : via la propriété `font-size` de CSS. Nous pouvons utiliser la propriété `font-size` via un style en ligne, interne ou externe.

Dans le passé, nous pouvions ajuster la taille du texte dans notre balise HTML sans utiliser CSS. Mais c'était avant HTML5. Ensuite, nous avons ajouté du texte en utilisant la balise `<font>`, qui peut prendre un attribut de taille comme vu ci-dessous :

```HTML
<font size="5">  
    Bonjour le monde 
</font>
```

Cet attribut de taille peut prendre une valeur de 1 à 7, où la taille du texte augmente de 1 à 7. Mais comme je l'ai dit, cela est obsolète depuis longtemps, et la plupart des gens ne savent même pas que cela existait.

Au cas où vous seriez pressé de voir comment vous pouvez changer la taille de votre texte, alors le voici :

```HTML
// Utilisation du CSS en ligne
<h1 style="font-size: valeur;"> Bonjour le monde ! </h1>

// Utilisation du CSS interne/externe
sélecteur {
    font-size: valeur;
}
```

Supposons que vous n'êtes pas pressé. Plongeons brièvement dans le sujet.

## Comment changer la taille du texte avec le CSS en ligne

Le CSS en ligne vous permet d'appliquer des styles à des éléments HTML spécifiques. Cela signifie que nous mettons du CSS directement dans une balise HTML. Nous utilisons l'attribut style, qui contient maintenant tous nos styles.

```HTML
<h1 style="...">Bonjour le monde!</h1>
```

Nous utilisons la propriété `font-size` avec notre valeur pour changer la taille du texte en utilisant le CSS en ligne. Cette valeur peut utiliser n'importe laquelle de vos unités CSS préférées telles que em, px, rem, etc.

```HTML
<h1 style="font-size:4em; "> Bonjour le monde ! </h1>
<p style="font-size:14px; "> Tout texte dont nous voulons changer la police </p>
```

Une syntaxe parfaite serait :

```HTML
<BALISE-TEXTE style="font-size:valeur;"> ... </BALISE-TEXTE>
```

## Comment changer la taille du texte avec le CSS interne ou externe

L'approche que vous utilisez pour changer la taille du texte dans le style CSS interne et externe est similaire, puisque vous utilisez un sélecteur. La syntaxe générale pour cela est :

```CSS
sélecteur {
    font-size: valeur;
}
```

Le sélecteur peut être notre balise HTML ou peut-être une classe ou un ID. Par exemple :

```HTML
// HTML
<p> Tout texte dont nous voulons changer la police </p>

// CSS
p {
    font-size: 14px;
}
```

Ou nous pourrions utiliser une classe :

```HTML
// HTML
<p class="mon-paragraphe" > Tout texte dont nous voulons changer la police </p>

// CSS
.mon-paragraphe {
    font-size: 14px;
}
```

## Conclusion

Dans cet article, vous avez appris comment changer la taille de la police/du texte d'un élément HTML en utilisant CSS. Vous avez également vu comment les développeurs le faisaient avant l'introduction de HTML5.

De plus, gardez à l'esprit qu'il est toujours préférable de styliser vos éléments HTML en utilisant un style interne ou externe, car cela offre beaucoup plus de flexibilité par rapport au style en ligne.

Par exemple, vous pouvez utiliser une seule classe CSS pour tous vos éléments de paragraphe plutôt que d'avoir à ajouter des styles en ligne à tous vos éléments de paragraphe.

L'utilisation de styles en ligne n'est pas considérée comme une meilleure pratique car elle entraîne beaucoup de répétition – vous ne pouvez pas réutiliser les styles ailleurs. Pour en savoir plus, vous pouvez lire [mon article sur le style en ligne en HTML](https://www.freecodecamp.org/news/inline-style-in-html/).

J'espère que ce tutoriel vous donne les connaissances pour changer la taille de votre texte HTML afin que vous puissiez le rendre plus beau.

Amusez-vous bien à coder !