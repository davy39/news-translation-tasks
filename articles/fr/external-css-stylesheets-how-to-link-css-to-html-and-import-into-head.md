---
title: Feuilles de style CSS externes – Comment lier CSS à HTML et l'importer dans
  Head
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-08-24T15:44:49.000Z'
originalURL: https://freecodecamp.org/news/external-css-stylesheets-how-to-link-css-to-html-and-import-into-head
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-martin-damboldt-814499.jpg
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Development
  slug: web-development
seo_title: Feuilles de style CSS externes – Comment lier CSS à HTML et l'importer
  dans Head
seo_desc: 'It is considered a best practice to have your CSS stylesheets in an external
  file. So how can you link that CSS to your HTML file?

  Linking to an external CSS file is an important part of any HTML page boilerplate.
  And in this article, we''ll learn how...'
---

Il est considéré comme une bonne pratique d'avoir vos feuilles de style CSS dans un fichier externe. Alors, comment pouvez-vous lier ce CSS à votre fichier HTML ?

Lier à un fichier CSS externe est une partie importante de tout [modèle de page HTML](https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/). Et dans cet article, nous allons apprendre comment le faire.

## **Comment lier un fichier CSS à un fichier HTML**

Vous pouvez lier votre fichier CSS à votre fichier HTML en ajoutant un élément `link` à l'intérieur de l'élément `head` de votre fichier HTML, comme ceci :

```html
<!DOCTYPE html>
  <html>
    <head>
      <link rel="stylesheet" href="style.css">
    </head>
    <body>
    
    </body>
</html>
```

L'élément `link` a de nombreuses utilisations, et il est important de spécifier les bons attributs afin de pouvoir l'utiliser pour importer une feuille de style CSS externe. Nous allons examiner quelques attributs importants maintenant.

## **L'attribut `rel`**

Le premier des deux attributs indispensables est l'attribut `rel`. Vous utiliserez cet attribut pour indiquer au navigateur quelle est la relation avec le fichier importé.

Vous écrirez `rel="stylesheet"` pour indiquer au navigateur que vous importez une feuille de style.

## **L'attribut `href`**

Le deuxième attribut indispensable est l'attribut `href`, qui spécifie le fichier à importer.

Une situation courante est que le fichier CSS et le fichier HTML se trouvent dans le même dossier. Dans ce cas, vous pouvez écrire `href="style.css"`.

Si le fichier CSS et le fichier HTML se trouvent dans des dossiers différents, vous devez écrire le chemin correct qui doit aller du fichier HTML au fichier CSS.

Par exemple, une situation courante est que le fichier CSS se trouve dans un dossier frère du fichier HTML, comme ceci :

```
project --- index.html
            css ---------- style.css
```

Dans ce cas, vous devriez écrire un chemin comme `"css/styles.css"`.

## **L'attribut `type`**

```html
<link rel="stylesheet" href="style.css" type="text/css">
```

Vous utilisez l'attribut `type` pour définir le type du contenu que vous liez. Pour une feuille de style, ce serait `text/css`. Mais puisque `css` est le seul langage de feuille de style utilisé sur le web, il n'est pas seulement facultatif, mais il est même une bonne pratique de ne pas l'inclure.

## **L'attribut `media`**

```html
<link rel="stylesheet" href="style.css" media="screen and (max-width: 600px)">
```

L'attribut media n'est pas visible dans l'exemple. Il s'agit d'un attribut facultatif que vous pouvez utiliser pour spécifier quand importer une certaine feuille de style. Sa valeur doit être un type de média / une requête média.

Cela peut être utile si vous souhaitez séparer les styles pour différents appareils et tailles d'écran dans différents fichiers. Vous devrez importer chaque fichier CSS avec son propre élément `link`.

Vous pouvez consulter ces articles (ou d'autres sources) sur les requêtes média pour en savoir plus sur ce que vous pouvez écrire comme valeur d'attribut :

* [Comment utiliser les requêtes média CSS pour créer des sites Web réactifs](https://www.freecodecamp.org/news/how-to-use-css-media-queries-to-create-responsive-websites/)
* [Comment définir des plages de largeur pour vos requêtes média CSS](https://www.freecodecamp.org/news/media-queries-width-ranges/)
* [Tutoriel CSS sur les requêtes média – Résolutions standard, points d'arrêt CSS et ciblage des tailles de téléphone](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/)

# **Conclusion**

Dans cet article, vous avez appris comment ajouter une feuille de style externe à votre page web en utilisant l'élément `link` et les attributs `href` et `rel`.

Vous avez également appris que vous pouvez importer plusieurs feuilles de style et utiliser l'attribut `media` pour déterminer quand chacune doit être appliquée.

Amusez-vous à créer des pages web !