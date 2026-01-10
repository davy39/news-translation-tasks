---
title: Comment créer des hyperliens HTML en utilisant l'attribut HREF sur les balises
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-21T11:15:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-html-hyperlinks-using-the-href-attribute-on-tags
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/coverfcc.png
tags:
- name: HTML
  slug: html
seo_title: Comment créer des hyperliens HTML en utilisant l'attribut HREF sur les
  balises
seo_desc: "By Ibrahima Ndaw\nA website is a collection of web pages. And these pages\
  \ need to be linked or connected by something. And to do so, we need to use a tag\
  \ provided by HTML: the a tag. \nThis tag defines a hyperlink, which is used to\
  \ link from one page t..."
---

Par Ibrahima Ndaw

Un site web est une collection de pages web. Et ces pages doivent être liées ou connectées par quelque chose. Pour ce faire, nous devons utiliser une balise fournie par HTML : la balise `a`.

Cette balise définit un hyperlien, qui est utilisé pour lier une page à une autre. Et l'attribut le plus important de l'élément `a` est l'attribut `href`, qui indique la destination du lien.

Dans ce guide, je vais vous montrer comment créer des hyperliens HTML en utilisant l'attribut `href` sur la balise `a`.

* [Qu'est-ce qu'un lien ?](#heading-qu-est-ce-qu-un-lien)
* [Comment créer des liens internes](#heading-comment-creer-des-liens-internes)
* [Naviguer vers des pages au même niveau](#heading-naviguer-vers-des-pages-au-meme-niveau)
* [Naviguer vers des pages situées dans un autre dossier](#heading-naviguer-vers-des-pages-situees-dans-un-autre-dossier)
* [Naviguer depuis une page située dans un dossier vers la racine](#heading-naviguer-depuis-une-page-situee-dans-un-dossier-vers-la-racine)
* [Comment créer des liens externes](#heading-comment-creer-des-liens-externes)
* [Comment créer des liens d'ancrage](#heading-comment-creer-des-liens-d-ancrage)
* [Naviguer sur la même page](#heading-naviguer-sur-la-meme-page)
* [Naviguer sur une autre page](#heading-naviguer-sur-une-autre-page)
* [Conclusion](#heading-conclusion)

## Qu'est-ce qu'un lien ?

Un lien est un texte cliquable qui permet de naviguer d'une page à une autre, ou vers une partie différente de la même page.

En développement web, il existe plusieurs façons de créer des liens, mais la plus courante est d'utiliser la balise `a` et l'attribut `href`. C'est ici que nous spécifions l'adresse de destination du lien.

La balise `a` nous aide à créer trois principaux types de liens : un lien interne, un lien externe et un lien d'ancrage. Cela dit, nous pouvons maintenant plonger dans la création d'un lien interne dans la section suivante.

## Comment créer des liens internes

Lorsqu'il s'agit de construire un site web, il est logique d'avoir une connexion entre les pages. Et tant que ces liens nous permettent de naviguer de la page A à la page B, cela s'appelle un lien interne (puisqu'il est toujours dans le même nom de domaine ou sur le même site web). Ainsi, un lien interne est un lien qui permet de naviguer vers une autre page d'un site web.

Maintenant, en supposant que notre dossier est structuré comme suit :

```
├── folder1
│   └── page2.html
├── page1.html
├── index.html

```

Ici, nous avons trois cas d'utilisation, et pour chacun, nous créerons un exemple.

### Naviguer vers des pages au même niveau

* `index.html`

```html
<a href="page1.html">Aller à la Page 1</a>

```

Comme vous pouvez le voir, la page `page1.html` est au même niveau, donc le chemin de l'attribut `href` est simplement le nom de la page.

### Naviguer vers des pages situées dans un autre dossier

* `page1.html`

```html
<a href="./folder1/page2.html">Aller à la Page 2</a>

```

Ici, nous avons un cas d'utilisation différent puisque la page que nous voulons visiter n'est plus au même niveau. Et pour pouvoir naviguer vers cette page, nous devons spécifier le chemin complet du fichier, y compris le dossier.

Super ! Plongeons maintenant dans le dernier cas d'utilisation.

### Naviguer depuis une page située dans un dossier vers la racine

* `page2.html`

```html
<a href="../index.html">Aller à la Page d'Accueil</a>

```

Maintenant, ici, pour naviguer vers la page `index.html`, nous devons d'abord remonter d'un niveau avant de pouvoir accéder à cette page.

Nous avons maintenant couvert les liens internes, alors passons à la suite et introduisons comment naviguer vers des liens externes.

## Comment créer des liens externes

Il est toujours utile d'avoir la possibilité de naviguer vers des sites web externes également.

```html
<a href="https://www.google.com/">Aller sur Google</a>

```

Comme vous pouvez le voir ici, pour naviguer vers Google, nous devons spécifier son URL à l'attribut `href`.

Les liens externes et internes sont utilisés pour naviguer de la page A à la page B. Cependant, parfois nous voulons rester sur la même page et naviguer vers une partie spécifique. Et pour ce faire, nous devons utiliser ce qu'on appelle un lien d'ancrage, plongeons dedans dans la section suivante.

## Comment créer des liens d'ancrage

Un lien d'ancrage est un peu plus spécifique : il nous permet de naviguer du point A au point B tout en restant sur la même page. Il peut également être utilisé pour aller vers une partie d'une autre page.

### Naviguer sur la même page

```html
<a href="#about">Aller à l'ancre</a>
<h1 id="about"></h1>

```

Comparé aux autres, celui-ci est un peu différent. En effet, il fonctionne toujours de la même manière.

Ici, au lieu d'un lien de page, nous avons une référence à un élément. Lorsque nous cliquons sur le lien, il recherchera un élément avec le même nom sans le hashtag (`about`). S'il trouve cet id, il naviguera vers cette partie.

### Naviguer sur une autre page

```html
<a href="page1.html#about">Aller à l'ancre</a>

```

Cela est presque identique à l'exemple précédent, sauf que nous devons définir la page dans laquelle nous voulons naviguer et y ajouter l'ancre.

## Conclusion

L'attribut `href` est l'attribut le plus important de la balise `a`. Il nous permet de naviguer entre les pages ou simplement vers une partie spécifique d'une page. Espérons que ce guide vous aidera à construire un site web avec de nombreux liens.

Merci d'avoir lu.

_N'hésitez pas à me contacter !_

[TWITTER](https://twitter.com/ibrahima92_)   [BLOG](https://www.ibrahima-ndaw.com/)  [NEWSLETTER](https://ibrahima-ndaw.us5.list-manage.com/subscribe?u=8dedf5d07c7326802dd81a866&id=5d7bcd5b75)  [GITHUB](https://github.com/ibrahima92)  [LINKEDIN](https://www.linkedin.com/in/ibrahima-ndaw/)  [CODEPEN](https://codepen.io/ibrahima92)  [DEV](https://dev.to/ibrahima92)

Photo par [JJ Ying](https://unsplash.com/@jjying?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/s/photos/link?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)