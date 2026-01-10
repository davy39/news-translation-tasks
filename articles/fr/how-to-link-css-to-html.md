---
title: Comment lier CSS à HTML – Liaison de fichiers de feuilles de style
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-14T16:22:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-link-css-to-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/linkHTMLCSS.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Comment lier CSS à HTML – Liaison de fichiers de feuilles de style
seo_desc: 'HTML is the markup language that helps you define the structure of a web
  page. CSS is the stylesheet language you use to make the structure presentable and
  nicely laid out.

  To make the stylings you implement with CSS reflect in the HTML, you have to ...'
---

HTML est le langage de balisage qui vous aide à définir la structure d'une page web. CSS est le langage de feuille de style que vous utilisez pour rendre la structure présentable et bien organisée.

Pour que les styles que vous implémentez avec CSS se reflètent dans le HTML, vous devez trouver un moyen de lier le CSS au HTML.

Vous pouvez effectuer la liaison en écrivant du CSS en ligne, du CSS interne ou du CSS externe.

Il est considéré comme une bonne pratique de garder votre CSS séparé de votre HTML, donc cet article se concentre sur la manière de lier ce CSS externe à votre HTML.

## Comment lier CSS à HTML

Pour lier votre CSS à votre HTML, vous devez utiliser la balise link avec certains attributs pertinents.

La balise link est une balise auto-fermante que vous devez placer dans la section head de votre HTML.

Pour lier CSS à HTML avec celle-ci, voici comment procéder :
```css
<link rel="stylesheet" type="text/css" href="styles.css" />
```

Placez la balise link dans la section head de votre HTML comme montré ci-dessous :

```html
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="styles.css" /> 
    <title>Lier CSS à HTML</title>
</head>
```

## Attributs de la balise Link

### L'attribut `rel`

`rel` est la relation entre le fichier externe et le fichier actuel. Pour CSS, vous utilisez `stylesheet`. Par exemple, `rel="stylesheet"`.

### L'attribut `type`

`type` est le type du document que vous liez au HTML. Pour CSS, c'est `text/css`. Par exemple `type="text/css"`.

### L'attribut `href`

`href` signifie "hypertext reference". Vous l'utilisez pour spécifier l'emplacement du fichier CSS et le nom du fichier. C'est un lien cliquable, donc vous pouvez également maintenir `CTRL` et cliquer dessus pour afficher le fichier CSS.

Par exemple, `href="styles.css"` si le fichier CSS est situé dans le même dossier que le fichier HTML. Ou `href="folder/styles.css"` si le fichier CSS est situé dans un autre dossier.


## Réflexions finales

Cet article vous a montré comment lier correctement un fichier CSS externe à HTML avec la balise `link` et les attributs nécessaires.

Nous avons également examiné ce que signifie chacun des attributs, afin que vous ne les utilisiez pas sans savoir comment ils fonctionnent.

Continuez à coder…