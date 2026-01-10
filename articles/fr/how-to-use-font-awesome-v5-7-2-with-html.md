---
title: Comment utiliser Font Awesome v5.7.2 avec HTML
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-02T02:14:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-font-awesome-v5-7-2-with-html
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9aa9740569d1a4ca26f1.jpg
tags:
- name: fonts
  slug: fonts
- name: HTML
  slug: html
- name: toothbrush
  slug: toothbrush
- name: typography
  slug: typography
seo_title: Comment utiliser Font Awesome v5.7.2 avec HTML
seo_desc: 'Font Awesome is one of the most popular ways to add icons to your site.
  But what if you add the CDN to the <head> element of your page and all you see are
  black rectangles?


  Here are a couple of things to keep in mind when you add Font Awesome to you...'
---

Font Awesome est l'une des façons les plus populaires d'ajouter des icônes à votre site. Mais que faire si vous ajoutez le CDN à l'élément `<head>` de votre page et que vous ne voyez que des rectangles noirs ?

![Image](https://www.freecodecamp.org/news/content/images/2020/05/6f22c59bffe7f1b87fed6d58092f69d53e3bbd15.png)

Voici quelques points à garder à l'esprit lorsque vous ajoutez Font Awesome à votre prochain projet.

### Ajouter le lien à la tête

Imaginez que vous avez le HTML suivant :

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<link rel="stylesheet" type="text/css" href="testing.css">
	<link rel="stylesheet" type="text/css" href="css/all.css">
	<meta name="viewport" content="width=device-width, initial-scale=1 user-scalable=no">
</head>
<body>
	<i class="fab fa-github-square"><a href="https://github.com/willyblackkeez" id="profile-link"></a></i>
	<i class="fab fa-facebook"></i>
</body>
</html>
```

Comme pour les autres CDN, vous devez ajouter un élément `<link>` à la `<head>`. Pour Font Awesome 5.7.2, cela ressemblera à ceci :

`<link rel="stylesheet" href="//use.fontawesome.com/releases/v5.0.7/css/all.css">`

### En ligne vs local

Si vous exécutez le code suivant dans un éditeur basé sur le web comme CodePen ou CodeSandbox, le code suivant rend les icônes correctement :

```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
    <link rel="stylesheet" href="//use.fontawesome.com/releases/v5.0.7/css/all.css">
	<link rel="stylesheet" type="text/css" href="testing.css">
	<link rel="stylesheet" type="text/css" href="css/all.css">
	<meta name="viewport" content="width=device-width, initial-scale=1 user-scalable=no">
</head>
<body>
	<i class="fab fa-github-square"><a href="https://github.com/willyblackkeez" id="profile-link"></a></i>
	<i class="fab fa-facebook"></i>
</body>
</html>
```

Mais si vous essayez d'ouvrir la page localement dans un navigateur, vous verrez toujours les rectangles noirs au lieu des icônes :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/6f22c59bffe7f1b87fed6d58092f69d53e3bbd15-1.png)

Jetez un autre coup d'œil à l'attribut `href` dans l'élément `<link>` ci-dessus. Vous le voyez ?

Le problème est que, lorsque vous chargez la page à partir de votre système de fichiers local, le navigateur essaie de trouver le fichier CSS de Font Awesome à la racine du système de fichiers.

Pour que cela fonctionne en ligne et localement, assurez-vous d'ajouter le schéma d'URL (HTTP, ou mieux, HTTPS) à l'attribut `href` :

`<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.7/css/all.css">`

### Que se passe-t-il ici ?

Lorsque vous omettez le schéma d'URL (`href="//use.fontawesome..."`), le navigateur utilise le même schéma d'URL que celui avec lequel la page a été chargée.

Ainsi, si vous exécutez la page localement en ouvrant le fichier HTML dans un navigateur, l'attribut `href` suppose que le CSS de Font Awesome est également un fichier enregistré localement (`file:`).

Assurez-vous simplement que les attributs `href` de vos éléments `<link>` pointent tous vers l'URL complète, y compris le schéma d'URL, et tout devrait bien fonctionner.