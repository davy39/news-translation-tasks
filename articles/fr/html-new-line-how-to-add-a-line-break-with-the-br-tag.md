---
title: HTML Nouvelle Ligne – Comment Ajouter un Saut de Ligne avec la Balise BR
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-12T18:00:31.000Z'
originalURL: https://freecodecamp.org/news/html-new-line-how-to-add-a-line-break-with-the-br-tag
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/line-break.png
tags:
- name: Accessibility
  slug: accessibility
- name: HTML
  slug: html
seo_title: HTML Nouvelle Ligne – Comment Ajouter un Saut de Ligne avec la Balise BR
seo_desc: 'By Dillion Megida

  In this article, I''ll explain what line breaks are and show you how to create them
  in HTML.

  What is a Line Break?

  A line break, as the name implies, is a break in line 😅. A line break in HTML is
  a point where a line ends horizontal...'
---

Par Dillion Megida

Dans cet article, je vais expliquer ce que sont les sauts de ligne et vous montrer comment les créer en HTML.

## Qu'est-ce qu'un Saut de Ligne ?

Un saut de ligne, comme son nom l'indique, est une rupture dans la ligne 😅. Un saut de ligne en HTML est un point où une ligne se termine horizontalement, et la ligne suivante commence sur une nouvelle ligne.

En HTML, lorsque vous écrivez une chaîne comme ceci :

```html
<p>
    Bonjour, je suis
    en train d'essayer de créer une
    nouvelle ligne
</p>
```

Les espaces blancs (l'espace de tabulation avant "Bonjour", l'espace entre "suis" et "en train", "une" et "nouvelle") seront ignorés. Le résultat à l'écran apparaîtra comme ceci :

```txt
Bonjour, je suis en train d'essayer de créer une nouvelle ligne
```

Une façon de corriger cela (bien que ce ne soit pas très efficace) est de créer trois balises `<p>` comme ceci :

```html
<p>Bonjour, je suis</p>
<p>en train d'essayer de créer une</p>
<p>nouvelle ligne</p>
```

Cela donnera le résultat suivant :

```txt
Bonjour, je suis
en train d'essayer de créer une
nouvelle ligne
```

Parce que les balises `p` créent des éléments de type `block`, elles occupent tout l'espace horizontal et l'élément suivant passe à la ligne suivante – comme vous pouvez le voir à partir du résultat ci-dessus.

Cette solution n'est pas efficace car vous avez créé trois paragraphes. Dans les cas où un lecteur d'écran doit interpréter cela, il le lira comme trois paragraphes au lieu d'une seule phrase. Cela peut affecter l'accessibilité du web.

Alors, comment ajouter un saut de ligne pour un élément en ligne ?


## Comment Ajouter un Saut de Ligne en HTML

HTML possède des balises pour de nombreux usages, y compris pour créer des sauts de ligne. Vous pouvez utiliser la balise `br` en HTML pour ajouter des sauts de ligne. Elle peut être placée entre des éléments en ligne pour les diviser en plusieurs parties.

Voici un exemple de paragraphe avec la balise `br` :

```html
<p>
    Bonjour, je suis
    <br />
    en train d'essayer de créer une
    <br />
    nouvelle ligne
</p>
```

La balise `br` est un **élément vide** qui n'a pas de balise de fermeture. Au lieu de cela, c'est une balise auto-fermante.

Le code ci-dessus donne ce résultat :

```txt
Bonjour, je suis
en train d'essayer de créer une
nouvelle ligne
```

Vous pouvez utiliser cette balise pour d'autres formes d'éléments en ligne comme les liens. Par exemple, regardez ce code :

```html
<div>
    <a href="https://google.com">Google</a>
    <a href="https://twitter.com">Twitter</a>
</div>
```

Les balises d'ancrage, `a`, sont des éléments en ligne, donc au lieu que le deuxième lien s'affiche sur la ligne suivante, il s'affiche sur la même ligne comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-50.png)

Vous pouvez utiliser la balise `br` entre les liens pour rompre la ligne du premier lien :

```html
<div>
    <a href="https://google.com">Google</a>
    <br />
    <a href="https://twitter.com">Twitter</a>
</div>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-51.png)

## Conclusion

La balise `br` en HTML commence l'élément suivant sur une nouvelle ligne, similaire au retour chariot `\n` dans les chaînes de caractères.

Au lieu d'utiliser des éléments de bloc pour placer des éléments sur de nouvelles lignes, vous pouvez utiliser la balise de saut de ligne : `br`.

Dans des cas comme les phrases, l'utilisation de la balise `br` sert de saut de ligne visuel et n'affecte pas l'accessibilité. Les lecteurs d'écran liront la phrase telle quelle sans pause.