---
title: Comment changer la police avec HTML
date: '2022-06-07T16:41:40.000Z'
author: Kolade Chris
authorURL: https://www.freecodecamp.org/news/author/koladechris/
originalURL: https://freecodecamp.org/news/how-to-change-font-with-html
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/abc-3523454_1280.jpg
tags:
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
seo_desc: 'Back in the days of HTML4, there was a <font> tag you could use to change
  the font size, font family, and the color of a text.

  But with HTML5, the <font> tag has been deprecated. So if you want to change anything
  related to the font, you have to do i...'
---


À l'époque de l'HTML4, il existait une balise `<font>` que vous pouviez utiliser pour modifier la taille, la famille de polices et la couleur d'un texte.

<!-- more -->

Mais avec l'HTML5, la balise `<font>` a été dépréciée. Par conséquent, si vous souhaitez modifier quoi que ce soit de relatif à la police, vous devez le faire avec CSS.

Dans cet article, je vais vous montrer comment changer la taille de la police, la graisse (font-weight), le style de police et la famille de polices d'un texte en utilisant CSS.

## Comment changer la taille de la police du texte

La taille de la police d'un texte représente la dimension de ce texte.

Pour modifier la taille de la police d'un texte, vous devez utiliser la propriété `font-size` puis spécifier la valeur en pixels (`px`), `rem` ou `em`.

Vous pouvez le faire en utilisant du CSS en ligne (inline) comme ceci :

```
<h1 style="font-size: 4rem">freeCodeCamp</h1>
```

Vous pouvez également le faire dans du CSS intégré ou interne :

```
<style>
    h1 {
        font-size: 4rem;
    }
</style>
```

Et enfin, vous pouvez le faire dans un fichier CSS externe :

```
    h1 {
        font-size: 4rem;
    }
```

Pour supprimer l'arrière-plan blanc par défaut et centrer le texte horizontalement et verticalement, j'ai écrit ce CSS :

```
  body {
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100vh;
      background-color: #f1f1f1;
    }
```

Dans le navigateur, le résultat est le suivant : ![ss1-2](https://www.freecodecamp.org/news/content/images/2022/06/ss1-2.png)

## Comment changer la graisse (font-weight) du texte

La graisse (font-weight) est la propriété qui permet de définir si un texte spécifique sera gras ou léger.

Vous pouvez utiliser `font-weight` pour modifier la légèreté ou l'épaisseur du texte, puis lui donner une valeur telle que `normal`, `lighter`, `bold` ou `bolder`. Vous pouvez également utiliser des valeurs numériques comme 100, 200, 500, et ainsi de suite.

Tout comme pour la taille de la police, vous pouvez modifier la graisse en CSS en ligne, interne ou externe.

```
<span>
   <h1 style="font-weight: lighter">freeCodeCamp Lighter</h1>
   <h1 style="font-weight: normal">freeCodeCamp Normal</h1>
   <h1 class="bold" style="font-weight: bold">freeCodeCamp Bold</h1>
   <h1 style="font-weight: bolder">freeCodeCamp Bolder</h1>
</span>
```

```
<style>
    .lighter {
      font-weight: lighter;
    }

    .normal {
      font-weight: normal;
    }

    .bold {
      font-weight: bold;
    }

    .bolder {
      font-weight: bolder;
    }
</style>
```

```
.lighter {
      font-weight: lighter;
    }

    .normal {
      font-weight: normal;
    }

    .bold {
      font-weight: bold;
    }

    .bolder {
      font-weight: bolder;
    }
```

![ss2-2](https://www.freecodecamp.org/news/content/images/2022/06/ss2-2.png)

## Comment changer le style de police du texte

Le style de police est la variation de la police de caractères du texte. Cette variation peut être `normal`, `bold` ou `italic`.

Pour changer le style de police, vous avez besoin de la propriété `font-style` avec une valeur de `normal`, `oblique` ou `italic`.

`normal` est le style par défaut, vous n'avez donc pas besoin de le spécifier à moins de devoir surcharger une autre règle.

Comme d'habitude, vous pouvez modifier le style de police en CSS en ligne, interne ou externe.

```
<span>
      <h1>freeCodeCamp Normal</h1>
      <h1 style="font-style: oblique">freeCodeCamp Oblique</h1>
      <h1 style="font-style: italic">freeCodeCamp Italic</h1>
</span>
```

```
<style>
    .oblique {
      font-style: oblique;
    }

    .italic {
      font-style: italic;
    }
</style>
```

```
    .oblique {
      font-style: oblique;
    }

    .italic {
      font-style: italic;
    }
```

Voici le rendu dans le navigateur : ![ss3-2](https://www.freecodecamp.org/news/content/images/2022/06/ss3-2.png)

## Comment changer la famille de polices du texte

Une famille de polices représente une collection de polices qui partagent le même design et la même typographie.

Pour changer la famille de polices d'un texte, vous devez utiliser la propriété CSS `font-family`.

Vous pouvez ensuite choisir de le faire avec du CSS en ligne, du CSS interne ou du CSS externe.

L'extrait de code ci-dessous montre comment changer la `font-family` en CSS en ligne :

````
<h1 style="font-family: Verdana, Geneva, Tahoma, sans-serif">
      freeCodeCamp
</h1>


Vous pouvez changer la font-family en CSS intégré ou interne de cette manière :

```css
<style>
    h1 {
      font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
</style>
````

Dans un fichier CSS externe, vous pouvez changer la famille de polices comme ceci :

```
h1 {
      font-family: Verdana, Geneva, Tahoma, sans-serif;
    }
```

Assurez-vous que le fichier CSS externe est bien lié au fichier HTML, sinon cela ne fonctionnera pas.

La famille de polices Verdana ressemble à ceci dans le navigateur Google Chrome : ![ss4-1](https://www.freecodecamp.org/news/content/images/2022/06/ss4-1.png)

Vous avez peut-être remarqué qu'il y a d'autres familles de polices dans la valeur – Geneva, Tahoma et sans-serif.

Ce sont des solutions de repli (fallbacks) que le navigateur peut utiliser au cas où Verdana ne serait pas disponible sur l'appareil de l'utilisateur.

Si vous n'aimez pas les polices intégrées à votre appareil, vous pouvez en obtenir d'autres via Google Fonts.

Recherchez votre police préférée et copiez le lien correspondant, puis collez ce lien dans la section `<head>` de votre HTML afin d'y avoir accès dans votre feuille de style ![ss5-1](https://www.freecodecamp.org/news/content/images/2022/06/ss5-1.png)

Dans mon cas, j'ai utilisé la police Roboto comme ceci :

```
 h1 {
      font-family: Roboto, sans-serif;
    }
```

Et voici comment cela apparaît dans le navigateur : ![ss6-1](https://www.freecodecamp.org/news/content/images/2022/06/ss6-1.png)

## Conclusion

Cet article vous a présenté comment changer la taille de la police, la graisse, le style et la famille de polices d'un texte en CSS en ligne, interne ou externe.

Vous vous demandez peut-être quelle méthode est la meilleure entre le CSS en ligne, interne ou externe.

Si vous travaillez sur un petit projet, vous pouvez utiliser du CSS interne ou intégré, mais si vous travaillez sur un projet important ou en équipe, vous ne devriez pas utiliser de CSS interne.

C'est parce qu'il est considéré comme une bonne pratique de séparer votre CSS de votre HTML.

Le CSS en ligne est à proscrire dans la plupart des situations car il peut nuire à la lisibilité de votre HTML.

Il a également été suggéré que le CSS en ligne peut affecter négativement le SEO d'un site web.

Merci de votre lecture.