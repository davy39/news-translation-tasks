---
title: Comment utiliser Standard avec VSCode
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-06-14T04:58:21.000Z'
originalURL: https://freecodecamp.org/news/https-zellwk-com-blog-standard-with-vscode
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca207740569d1a4ca5214.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Visual Studio Code
  slug: vscode
seo_title: Comment utiliser Standard avec VSCode
seo_desc: "I use Visual Studio Code as my text editor. When I write JavaScript, I\
  \ follow JavaScript Standard Style.  \nThere's an easy way to integrate Standard\
  \ in VS Code—with the vscode-standardjs plugin. I made a video for this some time\
  \ ago if you're interes..."
---

J'utilise [Visual Studio Code](https://code.visualstudio.com/) comme éditeur de texte. Lorsque j'écris du JavaScript, je suis [JavaScript Standard Style](https://standardjs.com).

Il existe un moyen simple d'intégrer Standard dans VS Code — avec le plugin [vscode-standardjs](https://marketplace.visualstudio.com/items?itemName=chenxsan.vscode-standardjs). J'ai fait une [vidéo](https://youtu.be/Hv8FgxJyI9Y) à ce sujet il y a quelque temps si vous êtes intéressé par son installation.

Mais, si vous suivez les instructions de la vidéo (ou du fichier readme de vscode-standardjs), vous remarquerez qu'il y a un petit détail à régler.

Essayez d'écrire une `function` de l'ancienne manière, et enregistrez-la à plusieurs reprises. VS Code alternera entre avoir et ne pas avoir d'espace avant la parenthèse gauche de la fonction.

<figure><img src="https://zellwk.com/images/2019/vscode-standard/functions.gif" alt="VS Code alterne entre avoir et ne pas avoir d'espace avant '('."></figure>

Vous rencontrez le même problème lorsque vous écrivez des méthodes avec les raccourcis de méthode ES6 :

<figure><img src="https://zellwk.com/images/2019/vscode-standard/methods.gif" alt="Le même problème se produit lorsque vous créez des méthodes avec les raccourcis de méthode ES6."></figure>

Il existe un moyen rapide de résoudre ce problème. Ce que vous devez faire, c'est définir `javascript.format.enable` sur `false`. Cela désactive le formateur JavaScript par défaut de VS Code (et laisse vscode-standardjs faire le travail de formatage).

La configuration minimale dont vous avez besoin pour faire fonctionner Standard et VS Code ensemble est donc :

```
{
  // Empêche VS Code de formater JavaScript avec le linter par défaut
  "javascript.format.enable": false,

  // Empêche VS Code de linting JavaScript avec le linter par défaut
  "javascript.validate.enable": false,

  // Linting avec Standard JS
  "standard.enable": true,

  // Formater les fichiers avec Standard à chaque sauvegarde du fichier
  "standard.autoFixOnSave": true,

  // Fichiers à valider avec Standard JS
  "standard.validate": [
    "javascript",
    "javascriptreact"
  ]
}

```

---

_Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/standard-with-vscode)._
_Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend._