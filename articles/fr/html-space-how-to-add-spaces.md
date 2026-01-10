---
title: Espace HTML – Comment ajouter des espaces en HTML
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2022-05-29T00:47:27.000Z'
originalURL: https://freecodecamp.org/news/html-space-how-to-add-spaces
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/jeremy-thomas-E0AHdsENmDg-unsplash.jpg
tags:
- name: HTML
  slug: html
seo_title: Espace HTML – Comment ajouter des espaces en HTML
seo_desc: "Adding a space to your HTML can be deceptively difficult. And there are\
  \ at least 5 of ways to go about doing this. \nThis tutorial will show you several\
  \ examples. It will also show you how to use fancy versions of space, too.\nYou\
  \ can do all this in ra..."
---

Ajouter un espace à votre HTML peut être trompeusement difficile. Et il existe au moins 5 façons de procéder.

Ce tutoriel vous montrera plusieurs exemples. Il vous montrera également comment utiliser des versions fantaisistes d'espace, aussi.

Vous pouvez tout faire cela en HTML brut, sans avoir besoin de CSS. Mais sachez que CSS est la méthode préférée pour ajouter de l'espace à votre HTML. Et freeCodeCamp a une tonne de tutoriels sur la façon d'y parvenir en utilisant [le modèle de boîte CSS](https://www.freecodecamp.org/news/css-box-model-explained-with-examples/).

## Quel est le caractère ASCII pour un espace ?

Le code de caractère ASCII pour un espace est 20. Mais ce n'est que la méthode standard. Il existe plusieurs

Il existe 5 types d'espaces en HTML que vous pouvez utiliser. À l'œil nu, ils semblent identiques mais ils servent des objectifs légèrement différents.

Et il y a aussi le caractère de tabulation, qui représente l'appui sur la touche de tabulation de votre clavier. Et le caractère de retour chariot, qui représente l'appui sur la touche Entrée de votre clavier.

```
+---------------------+-----------+
|      Caractère      | Code HTML |
+---------------------+-----------+
| Espace insécable   | &nbsp;    |
| Espace en          | &ensp;    |
| Espace em          | &emsp;    |
| Espace fin         | &thinsp;  |
| Espace standard    | &#20;     |
| Nouvelle ligne     | &#13;     |
| Caractère tab      | &#09;     |
+---------------------+-----------+
```

## Quelle est la largeur d'un caractère d'espace ?

Il existe quatre largeurs courantes pour les caractères d'espace :

1. Espace de largeur standard. Cela s'appelle aussi "espace sans saut de ligne" car il ne provoquera pas de saut de ligne (AKA retour chariot).
2. Espace em. Cela s'appelle "Em" car il est aussi large que la lettre M dans la police que vous utilisez. (Si vous avez entendu le terme tiret em, c'est un tiret aussi large que la lettre M.)
3. Espace en. Cela s'appelle "En" car il est aussi large que la lettre n dans votre police.
4. Et enfin, il y a "Espace fin", qui est le plus mince de tous les espaces.

## Quel est le symbole pour l'espace en HTML ?

L'entité HTML la plus couramment utilisée est `&#20;`

Vous pouvez essayer de jeter ce texte pour forcer le rendu d'un espace.

Par exemple, disons que vous voulez mettre deux espaces après une phrase, mais que quelque chose d'autre dans le moteur de rendu du site supprime automatiquement l'un des espaces. Vous pouvez taper `&#20;&#20;` pour ajouter deux espaces.

## L'espace est-il un caractère non-ASCII ?

Non. L'espace est un caractère ASCII. Sa valeur ASCII est 20, et vous pouvez le taper comme ceci : `&#20;`

## Comment faire un espace blanc en HTML ?

Vous pouvez vouloir utiliser CSS pour centrer vos éléments HTML au lieu de coder des espaces en dur.

Mais si vous voulez simplement une méthode rapide et sale pour créer un espace blanc et pousser du texte, vous pouvez utiliser le même caractère d'espace encore et encore comme ceci :

```html
[Le texte auquel vous voulez ajouter un espace blanc final]&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;[le texte auquel vous voulez ajouter un espace blanc final]
```

## Quel caractère ressemble à un espace mais ne l'est pas ?

Il existe deux caractères qui ressemblent à des espaces mais ne le sont pas :

1. Le caractère de nouvelle ligne – également connu sous le nom de "retour chariot". Le code HTML pour le caractère de nouvelle ligne est : `&#13;`
2. Le caractère de tabulation, que vous obtenez lorsque vous appuyez sur le bouton de tabulation dans un champ de texte. Le code HTML pour le caractère de tabulation est : `&#09;`

J'espère que ce tutoriel vous a été utile. Allez de l'avant et faites de l'espace. 🚀