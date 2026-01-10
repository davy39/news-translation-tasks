---
title: Comment changer la couleur de fond avec JavaScript - Couleur de fond en JS
  et HTML
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2024-06-28T16:21:26.464Z'
originalURL: https://freecodecamp.org/news/how-to-change-background-color-with-javascript
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/_t-l5FFH8VA/upload/7dac186ffa0ba7f32d72ccf06d1d5baf.jpeg
tags:
- name: HTML
  slug: html
seo_title: Comment changer la couleur de fond avec JavaScript - Couleur de fond en
  JS et HTML
seo_desc: 'You can style elements with JavaScript using the element''s style property.
  In this article, you''ll learn how to change background color using JavaScript.

  Here''s what the mini project you''ll build looks like:


  In the image above, each button changes t...'
---

Vous pouvez styliser des éléments avec JavaScript en utilisant la propriété `style` de l'élément. Dans cet article, vous apprendrez comment changer la couleur de fond en utilisant JavaScript.

Voici à quoi ressemble le mini-projet que vous allez construire :

![image montrant cinq boutons qui changent chacun la couleur de fond d'une page](https://cdn.hashnode.com/res/hashnode/image/upload/v1719585559018/23123259-9540-40c6-8f1f-3f444c154b2c.png align="center")

Dans l'image ci-dessus, chaque bouton change la couleur de fond de la page pour une couleur spécifique.

Vous pouvez obtenir les fichiers de démarrage du projet [ici](https://github.com/ihechikara/change-bg-color-with-js/tree/main).

Il y a cinq boutons dans le fichier **index.html**, et chacun d'eux change la couleur de fond pour une valeur spécifique :

```xml
<!DOCTYPE html>
<html lang="en">
<head>
 
 
<meta charset="UTF-8">
 
 
<meta name="viewport" content="width=device-width, initial-scale=1.0">
 
 
<link rel="stylesheet" href="style.css">
 
 
<title>Changer la couleur de fond avec JS</title>
</head>
<body>
 
 
<h1>Choisir la couleur de fond</h1>
 
 
<button>Rouge</button>
 
 
<button>Bleu</button>
 
 
<button>Vert</button>
 
 
<button>Jaune</button>
 
 
<button>Réinitialiser</button>

 
 
<script src="script.js"></script>
</body>
</html>

```

Vous ne ferez aucune modification au fichier **style.css**. Son but est de centrer les éléments sur la page et de styliser les boutons pour qu'ils aient la même taille.

Pour l'instant, rien ne se passe lorsque vous cliquez sur les boutons. Écrivons la logique pour cela dans le fichier **script.js**.

## Comment changer la couleur de fond avec JavaScript

Pour changer la couleur de fond d'un élément avec JavaScript, vous pouvez utiliser la propriété `style` de l'élément :

Voici comment :

```javascript
function setBgGreen() {
 
 
document.body.style.backgroundColor = 'green';
}

function setBgRed() {
 
 
document.body.style.backgroundColor = 'red';
}

function setBgBlue() {
 
 
document.body.style.backgroundColor = 'blue';
}

function setBgYellow() {
 
 
document.body.style.backgroundColor = 'yellow';
}

function defaultBgColor() {
 
 
document.body.style.backgroundColor = 'white';
}
```

Dans le code ci-dessus, nous avons créé cinq fonctions : `setBgGreen()`, `setBgRed()`, `setBgBlue()`, `setBgYellow()`, et `defaultBgColor()`.

Chaque fonction a un point commun : elles ciblent toutes le `body`. À travers l'élément `body` (qui représente la page web), nous avons accédé à la propriété `style.backgroundColor`. Cette propriété retourne ou définit la couleur de fond d'un élément.

Ainsi :

* `document.body.style.backgroundColor = 'green';` dans la fonction `setBgGreen()` définit la couleur de fond du `body` en vert.

* `document.body.style.backgroundColor = 'red';` dans la fonction `setBgRed()` définit la couleur de fond du `body` en rouge.

* `document.body.style.backgroundColor = 'blue';` dans la fonction `setBgBlue()` définit la couleur de fond du `body` en bleu.

* `document.body.style.backgroundColor = 'yellow';` dans la fonction `setBgYellow()` définit la couleur de fond du `body` en jaune.

* `document.body.style.backgroundColor = 'white';` dans la fonction `defaultBgColor()` définit la couleur de fond du `body` en blanc.

Ensuite, vous allez assigner chaque fonction à leur bouton respectif en utilisant l'attribut `onclick` dans votre fichier HTML. Voici à quoi devrait ressembler votre fichier **index.html** après cela :

```xml
<!DOCTYPE html>
<html lang="en">
<head>
 
 
<meta charset="UTF-8">
 
 
<meta name="viewport" content="width=device-width, initial-scale=1.0">
 
 
<link rel="stylesheet" href="style.css">
 
 
<title>Changer la couleur de fond avec JS</title>
</head>
<body>
 
 
<h1>Choisir la couleur de fond</h1>
 
 
<button onclick="setBgRed()">Rouge</button>
 
 
<button onclick="setBgBlue()">Bleu</button>
 
 
<button onclick="setBgGreen()">Vert</button>
 
 
<button onclick="setBgYellow()">Jaune</button>
 
 
<button onclick="defaultBgColor()">Réinitialiser</button>

 
 
<script src="script.js"></script>
</body>
</html>
```

Lorsque vous cliquez sur les boutons, vous devriez voir la couleur de fond de la page changer pour la couleur assignée au bouton.

Notez que cela n'est pas applicable uniquement à l'élément `body`. Vous pouvez faire cela pour des parties spécifiques de votre page également.

Par exemple, la couleur de fond d'un `div` avec un `id` de `container` peut être changée en utilisant `container.style.backgroundColor = "red"`.

## Conclusion

Dans cet article, vous avez appris comment changer la couleur de fond avec JavaScript en utilisant la propriété `style` d'un élément.

Vous pouvez trouver le code complet du projet [ici](https://github.com/ihechikara/change-bg-color-with-js/tree/feat/change-bg-color).

Bon codage !