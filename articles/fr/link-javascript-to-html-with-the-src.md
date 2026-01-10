---
title: Lier JavaScript à HTML avec l'attribut script src
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-12-21T20:09:00.000Z'
originalURL: https://freecodecamp.org/news/link-javascript-to-html-with-the-src
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e93740569d1a4ca3dd8.jpg
tags:
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Lier JavaScript à HTML avec l'attribut script src
seo_desc: 'The ‘src’ attribute in a tag is the path to an external file or resource
  that you want to link to your HTML document.

  For example, if you had your own custom JavaScript file named ‘script.js’ and wanted
  to add its functionality to your HTML page, you...'
---

L'attribut 'src' dans une balise est le chemin vers un fichier ou une ressource externe que vous souhaitez lier à votre document HTML.

Par exemple, si vous aviez votre propre fichier JavaScript personnalisé nommé 'script.js' et que vous souhaitiez ajouter ses fonctionnalités à votre page HTML, vous l'ajouteriez comme ceci :

```html
<!DOCTYPE html>
<html lang="fr">
  <head>
    <title>Exemple d'attribut Script Src</title>
  </head>
  <body>

  <script src="./script.js"></script>
  </body>
</html>
```

Cela pointerait vers un fichier nommé 'script.js' qui se trouve dans le même répertoire que le fichier .html. Vous pouvez également lier à d'autres répertoires en utilisant '..' dans le chemin du fichier.

```html
<script src="../public/js/script.js"></script>
```

Cela remonte d'un niveau de répertoire, puis dans un répertoire 'public', puis dans un répertoire 'js' et enfin vers le fichier 'script.js'.

Vous pouvez également utiliser l'attribut 'src' pour lier des fichiers .js externes hébergés par un tiers. Cela est utilisé si vous ne souhaitez pas télécharger une copie locale du fichier. Notez simplement que si le lien change ou si l'accès au réseau est interrompu, le fichier externe auquel vous vous liez ne fonctionnera pas.

Cet exemple lie à un fichier jQuery.

```html
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
```

#### **Plus d'informations :**

[Article MDN sur le HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#attr-src)