---
title: HTML Vidéo – Comment intégrer un lecteur vidéo avec la balise HTML 5 Video
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-02-08T16:59:19.000Z'
originalURL: https://freecodecamp.org/news/html-video-how-to-embed-a-video-player-with-the-html-5-video-tag
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/pexels-donald-tong-66134.jpg
tags:
- name: HTML
  slug: html
- name: video
  slug: video
seo_title: HTML Vidéo – Comment intégrer un lecteur vidéo avec la balise HTML 5 Video
seo_desc: 'Before the advent of HTML 5, web developers had to embed video on a web
  page with a plugin like Adobe flash player.

  Today, you can easily embed videos in an HTML document with the <video> tag.

  In this article, we''ll see how the <video> tag works in H...'
---

Avant l'avènement de HTML 5, les développeurs web devaient intégrer des vidéos sur une page web avec un plugin comme Adobe Flash Player.

Aujourd'hui, vous pouvez facilement intégrer des vidéos dans un document HTML avec la balise `<video>`.

Dans cet article, nous verrons comment la balise `<video>` fonctionne en HTML.

## Table des matières
- [Syntaxe de base](#heading-syntaxe-de-base)
- [Attributs de la balise `<video>`](#heading-attributs-de-la-balise)
- [L'attribut `src`](#heading-lattribut-src)
- [L'attribut `poster`](#heading-lattribut-poster)
- [L'attribut `controls`](#heading-lattribut-controls)
- [L'attribut `loop`](#heading-lattribut-loop)
- [L'attribut `autoplay`](#heading-lattribut-autoplay)
- [Les attributs `width` et `height`](#heading-les-attributs-width-et-height)
- [L'attribut `muted`](#heading-lattribut-muted)
- [L'attribut `preload`](#heading-lattribut-preload)
- [Conclusion](#heading-conclusion)

## Syntaxe de base

Tout comme la balise `<img>`, `<video>` prend un attribut `src` avec lequel vous devez spécifier la source de la vidéo.

```html
<video src="weekend.mp4"></video>
```

Par défaut, elle est affichée comme une image dans le navigateur :
![ss-1-2](https://www.freecodecamp.org/news/content/images/2022/02/ss-1-2.png)

Ce CSS centre tout dans la page web et change la couleur de fond :
```css
 body {
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      background-color: #d3d3d3;
    }
```

De plus, vous pouvez spécifier plusieurs sources vidéo pour la balise `<video>` avec la balise `<source>`. Cette balise `<source>` doit également porter son propre attribut `src`.

Vous pouvez utiliser plusieurs balises `<source>` pour rendre disponibles différents formats de la même vidéo. Le navigateur jouera alors le format qu'il supporte.
```html
<video controls>
   <source src="weekend.mp4" />
   <source src="weekend.ogg" />
   <source src="weekend.webm" />
</video>
```
## Attributs de la balise `<video>`

La balise `<video>` supporte les attributs globaux tels que `id`, `class`, `style`, et ainsi de suite.

Si vous vous demandez ce que sont les attributs globaux, ce sont des attributs supportés par toutes les balises HTML.

Les attributs spécifiques supportés par la balise `<video>` incluent `src`, `poster`, `controls`, `loop`, `autoplay`, `width`, `height`, `muted`, `preload`, et autres.

### L'attribut `src`

L'attribut src est utilisé pour spécifier la source de la vidéo. Il peut s'agir d'un chemin relatif vers la vidéo sur votre machine locale ou d'un lien vers une vidéo en direct sur Internet.
```html
<video src="weekend.mp4"></video>
```
Il est facultatif car vous pouvez utiliser la balise `<source>` à la place.

### L'attribut `poster`

Avec l'attribut poster, vous pouvez incorporer une image à afficher avant que la vidéo ne commence à jouer ou pendant son téléchargement.
```html
<video src="weekend.mp4" poster="benefits-of-coding.jpg"></video>
```

Au lieu de l'image de la première scène de la vidéo, le navigateur affichera cette image :
![ss-2-2](https://www.freecodecamp.org/news/content/images/2022/02/ss-2-2.png)

### L'attribut `controls`

Lorsque vous utilisez control, cela permet au navigateur d'afficher des contrôles de lecture tels que play et pause, volume, recherche, etc.
```html
<video
      controls
      src="weekend.mp4"
      poster="benefits-of-coding.jpg"
></video>
```
![ss-3-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-3-1.png)

### L'attribut `loop`

Avec l'attribut loop, vous pouvez faire en sorte que la vidéo se répète automatiquement. C'est-à-dire, la faire redémarrer chaque fois qu'elle s'arrête.
```html
<video
      controls
      loop
      src="weekend.mp4"
      poster="benefits-of-coding.jpg"
></video>
```

### L'attribut `autoplay`

L'attribut `autoplay` permet de faire démarrer la vidéo automatiquement immédiatement après le chargement de la page.
```html
<video
      controls
      loop
      autoplay
      src="weekend.mp4"
      poster="benefits-of-coding.jpg"
></video>
```

### Les attributs `width` et `height`

Vous pouvez utiliser les attributs width et height pour spécifier une largeur et une hauteur pour la vidéo en pixels. Il n'accepte que des valeurs absolues, par exemple, des pixels.
```html
<video
      controls
      loop
      autoplay
      src="weekend.mp4"
      width="350px"
      height="250px"
      poster="benefits-of-coding.jpg"
></video>
```
![ss-4-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-4-1.png)

### L'attribut `muted`

Vous pouvez utiliser l'attribut muted pour indiquer au navigateur de ne pas jouer de son associé à la vidéo lorsqu'elle commence à jouer.
```html
<video
      controls
      loop
      autoplay
      muted
      src="weekend.mp4"
      width="350px"
      height="250px"
      poster="benefits-of-coding.jpg"
></video>
```
![ss-5-1](https://www.freecodecamp.org/news/content/images/2022/02/ss-5-1.png)

Si l'attribut `controls` est spécifié, l'utilisateur peut cliquer sur le bouton de volume pour réactiver le son.

### L'attribut `preload`

Avec l'attribut preload, vous pouvez donner une indication au navigateur sur le fait de télécharger ou non la vidéo lorsque la page se charge.

Cet attribut est crucial pour l'expérience utilisateur.

Vous pouvez utiliser 3 valeurs avec l'attribut preload :
- none : spécifie que la vidéo ne se chargera pas jusqu'à ce que l'utilisateur appuie sur play

- auto : spécifie que la vidéo doit être téléchargée même si l'utilisateur n'appuie pas sur play

- metadata : spécifie que le navigateur doit collecter des métadonnées telles que la longueur, la taille, la durée, etc.

```html
<video
      controls
      loop
      autoplay
      muted="true"
      preload="metadata"
      src="weekend.mp4"
      width="350px"
      height="250px"
      poster="benefits-of-coding.jpg"
></video>
```

## Conclusion

Dans cet article, vous avez appris à propos de la balise HTML5 `<video>` et de ses attributs, afin de pouvoir l'utiliser correctement dans vos projets.

Puisque l'audio est une partie importante d'une vidéo complète, vous pouvez également utiliser la balise `<video>` pour mettre un fichier audio sur une page web. Mais dans la plupart des cas, vous devriez utiliser la balise `<audio>` à cette fin pour une expérience utilisateur appropriée.

Si vous trouvez cet article utile, partagez-le avec vos amis et votre famille afin qu'il puisse atteindre plus de personnes qui pourraient en avoir besoin.