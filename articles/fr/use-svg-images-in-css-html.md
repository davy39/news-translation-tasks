---
title: Comment utiliser les images SVG en CSS et HTML – Un tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-16T22:44:20.000Z'
originalURL: https://freecodecamp.org/news/use-svg-images-in-css-html
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Screen-Shot-2020-11-15-at-3.59.07-PM.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: image
  slug: image
- name: 'image optimization '
  slug: image-optimization
- name: SVG
  slug: svg
- name: xml
  slug: xml
seo_title: Comment utiliser les images SVG en CSS et HTML – Un tutoriel pour débutants
seo_desc: 'By Edidiong Asikpo

  SVG stands for Scalable Vector Graphics. It is a unique type of image format for
  vector-based graphics written in Extensible Markup Language (XML).

  In this tutorial, I will explain why you''d want to use SVG images and how you can
  u...'
---

Par Edidiong Asikpo

SVG signifie Scalable Vector Graphics. C'est un type unique de format d'image pour les graphiques vectoriels écrits en Extensible Markup Language (XML).

Dans ce tutoriel, je vais expliquer pourquoi vous voudriez utiliser des images SVG et comment vous pouvez les utiliser en CSS et HTML.

## Pourquoi devriez-vous utiliser des images SVG ?

Il y a plusieurs raisons d'utiliser des images SVG, parmi lesquelles :

* Les images SVG ne perdent pas leur qualité lorsqu'elles sont zoomées ou redimensionnées.

* Elles peuvent être créées et éditées avec un IDE ou un éditeur de texte.

* Elles sont accessibles et animables.

* Elles ont une petite taille de fichier et sont hautement scalables.

* Et elles peuvent être recherchées, indexées, scriptées et compressées.

Maintenant, voyons comment vous pouvez réellement travailler avec des images SVG.

## Comment télécharger l'image SVG utilisée dans ce tutoriel

Si vous souhaitez travailler avec l'image SVG que j'ai utilisée dans ce tutoriel, suivez les étapes (et le diagramme) ci-dessous pour la télécharger.

* Allez sur [unDraw](https://undraw.co).

* Changez la couleur de fond en jaune.

* Dans la barre de recherche, recherchez le mot **happy**.

![Page d'accueil d'unDraw](https://i.imgur.com/ncSY7Rn.png align="left")

* Cliquez sur l'image nommée **Happy news**.

* Dans la fenêtre pop-up, cliquez sur le bouton **Download SVG to your projects**.

![Télécharger le fichier SVG](https://i.imgur.com/qGrT73n.png align="left")

Si vous avez suivi les étapes ci-dessus correctement, l'image SVG devrait maintenant être sur votre ordinateur.

![Image](https://i.imgur.com/3uCGy6B.png align="left")

Maintenant, ouvrez l'image SVG dans votre IDE ou éditeur de texte préféré. Renommez-la en **happy.svg** ou avec le nom que vous préférez.

## Comment utiliser les images SVG en CSS et HTML

Il existe plusieurs façons différentes d'utiliser les images SVG en CSS et HTML. Nous allons explorer six méthodes différentes dans ce tutoriel.

### 1. Comment utiliser un SVG comme `<img>`

Cette méthode est la manière la plus simple d'ajouter des images SVG à une page web. Pour utiliser cette méthode, ajoutez l'élément `<img>` à votre document HTML et référencez-le dans l'attribut `src`, comme ceci :

```html
<img src="happy.svg" alt="Mon SVG Heureux"/>
```

En supposant que vous avez téléchargé l'image SVG depuis unDraw et que vous l'avez renommée en **happy.svg**, vous pouvez ajouter l'extrait de code ci-dessus dans votre document HTML.

Si vous avez tout fait correctement, votre page web devrait ressembler exactement à la démonstration ci-dessous. 👀

<iframe src="https://codesandbox.io/embed/svg-demo-mppxs?fontsize=14&hidenavigation=1&theme=dark" style="width:100%;height:500px;border:0;border-radius:4px;overflow:hidden" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"></iframe>

Lorsque vous ajoutez une image SVG en utilisant la balise `<img>` sans spécifier la taille, elle prend la taille du fichier SVG original.

Par exemple, dans la démonstration ci-dessus, je n'ai pas modifié la taille de l'image SVG, donc elle a pris sa taille originale (qui était une largeur de `915.11162px` et une hauteur de `600.53015px`).

**Note :** pour changer la taille originale, vous devez spécifier la `width` et la `height` avec CSS comme vous pouvez le voir dans la démonstration ci-dessous. Vous pouvez également mettre à jour la `width` et la `height` originales directement.

<iframe src="https://codesandbox.io/embed/svg-demo-1-ey5me?fontsize=14&hidenavigation=1&theme=dark" style="width:100%;height:500px;border:0;border-radius:4px;overflow:hidden" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"></iframe>

Même si nous pouvons changer la taille des images SVG ajoutées via la balise `<img>`, il y a encore quelques restrictions si vous voulez apporter des modifications de style majeures à l'image SVG.

### 2. Comment utiliser un SVG comme `background-image` en CSS

Cela ressemble à l'ajout d'un SVG à un document HTML en utilisant la balise `<img>`. Mais cette fois, nous le faisons avec CSS au lieu de HTML comme vous pouvez le voir dans l'extrait de code ci-dessous.

```bash
body {
  background-image: url(happy.svg);
}
```

Lorsque vous utilisez un SVG comme image de fond CSS, il a des limitations similaires à l'utilisation de `<img>`. Cependant, il permet un peu plus de personnalisation.

Consultez la démonstration ci-dessous et n'hésitez pas à y apporter des modifications en utilisant CSS.

<iframe src="https://codesandbox.io/embed/svg-demo-2-ftn6n?fontsize=14&hidenavigation=1&theme=dark" style="width:100%;height:500px;border:0;border-radius:4px;overflow:hidden" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"></iframe>

### 3. Comment utiliser des images SVG en ligne

Les images SVG peuvent être écrites directement dans le document HTML en utilisant la balise `<svg> </svg>`.

Pour ce faire, ouvrez l'image SVG dans VS Code ou votre IDE préféré, copiez le code et collez-le à l'intérieur de l'élément `<body>` dans votre document HTML.

```bash
<body>
 // Collez le code SVG ici.
</body>
```

Si vous avez tout fait correctement, votre page web devrait ressembler exactement à la démonstration ci-dessous.

<iframe src="https://codesandbox.io/embed/svg-demo-3-zunkd?fontsize=14&hidenavigation=1&theme=dark" style="width:100%;height:500px;border:0;border-radius:4px;overflow:hidden" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"></iframe>

Lorsque vous utilisez SVG en ligne dans le document HTML, cela réduit le temps de chargement car il sert de requête HTTP.

L'utilisation de cette méthode vous permet d'effectuer plus de personnalisation par rapport à l'utilisation de la balise `<img>` ou de la méthode `background-image`.

### 4. Comment utiliser un SVG comme `<object>`

Vous pouvez également utiliser un élément HTML `<object>` pour ajouter des images SVG à une page web en utilisant la syntaxe de code ci-dessous :

```bash
<object data="happy.svg" width="300" height="300"> </object>
```

Vous utilisez l'attribut `data` pour spécifier l'URL de la ressource que vous allez utiliser par l'objet, qui est l'image SVG dans notre cas.

Vous utilisez `width` et `height` pour spécifier la taille de l'image SVG.

Encore une fois, voici une démonstration pour vous explorer. 😃

<iframe src="https://codesandbox.io/embed/svg-demo-4-3ge0n?fontsize=14&hidenavigation=1&theme=dark" style="width:100%;height:500px;border:0;border-radius:4px;overflow:hidden" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"></iframe>

L'utilisation de `<object>` est supportée dans tous les navigateurs qui supportent SVG.

### 5. Comment utiliser un SVG comme `<iframe>`

Bien que cela ne soit pas conseillé, vous pouvez également ajouter une image SVG en utilisant un `<iframe>` comme le montre la démonstration ci-dessous.

<iframe src="https://codesandbox.io/embed/svg-demo-5-co3hg?fontsize=14&hidenavigation=1&theme=dark" style="width:100%;height:500px;border:0;border-radius:4px;overflow:hidden" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"></iframe>

Gardez simplement à l'esprit que les `<iframe>` peuvent être difficiles à maintenir et seront mauvais pour le référencement (SEO) de votre site.

L'utilisation de `<iframe>` contredit également le but du *Scalable* dans le nom *Scalable Vector Graphics* car les images SVG ajoutées avec ce format ne sont pas scalables.

### 6. Comment utiliser un SVG comme `<embed>`

L'élément HTML `<embed>` est une autre façon d'utiliser une image SVG en HTML et CSS en utilisant cette syntaxe : `<embed src="happy.svg" />`.

Gardez à l'esprit, cependant, que cette méthode a également des limitations. Selon MDN, la plupart des navigateurs modernes ont obsolète et supprimé le support des plug-ins de navigateur. Cela signifie que compter sur `<embed>` n'est généralement pas judicieux si vous voulez que votre site soit utilisable sur le navigateur de l'utilisateur moyen.

Ci-dessous se trouve une démonstration de l'utilisation de l'élément HTML `<embed>` pour ajouter une image SVG.

<iframe src="https://codesandbox.io/embed/svg-demo-6-iwy0s?fontsize=14&hidenavigation=1&theme=dark" style="width:100%;height:500px;border:0;border-radius:4px;overflow:hidden" sandbox="allow-forms allow-modals allow-popups allow-presentation allow-same-origin allow-scripts"></iframe>

## Conclusion

J'espère que vous avez pu apprendre les différentes façons d'utiliser les images SVG en CSS et HTML. Cela devrait vous guider vers le choix de la bonne méthode lors de l'ajout d'images SVG à un site web.

Si vous avez des questions, vous pouvez m'envoyer un [message sur Twitter](https://twitter.com/Didicodes), et je serai heureux de répondre à chacune d'entre elles.