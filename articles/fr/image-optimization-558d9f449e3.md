---
title: Comment l'optimisation des images a réduit le poids de ma page web de 62%
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-15T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/image-optimization-558d9f449e3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FPOrNnlLf9EpyBy7
tags:
- name: optimization
  slug: optimization
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment l'optimisation des images a réduit le poids de ma page web de 62%
seo_desc: 'By Ayo Isaiah

  Images are one of the most fundamental types of content that is served on the web.
  They say an image is worth a thousand words. But it can also be worth quite a few
  megabytes too, if you’re not careful.

  So although web images need to be...'
---

Par Ayo Isaiah

Les images sont l'un des types de contenu les plus fondamentaux servis sur le web. On dit qu'une image vaut mille mots. Mais elle peut aussi valoir plusieurs mégaoctets, si vous n'êtes pas prudent.

Ainsi, bien que les images web doivent être claires et nettes, elles doivent également être livrées dans des tailles gérables afin que les temps de chargement restent courts et que l'utilisation des données soit maintenue à des niveaux acceptables.

Sur mon site web, j'ai remarqué que le poids de la page d'accueil était supérieur à 1,1 Mo et que les images représentaient 88 % de ce poids. J'ai également réalisé que je servais des images plus grandes que nécessaire (en termes de résolution). Clairement, il y avait beaucoup de place pour l'amélioration.

![Image](https://cdn-media-1.freecodecamp.org/images/vEaHEInUtuxemq-A0cPhQA9yCbBVSWsBfwyJ)

J'ai commencé par lire l'excellent e-book [Essential Image Optimization](https://images.guide/) d'Addy Osmani et j'ai procédé à la mise en œuvre de ses recommandations sur mon site web. Ensuite, j'ai fait des recherches sur les images réactives et je les ai appliquées également.

Cela a réduit le poids de la page à 445 Ko. Une réduction d'environ 62 % du poids de la page !

![Image](https://cdn-media-1.freecodecamp.org/images/X6zYsxiNumBdIySf8c7m70U8bdImRgtq8Ikk)

Cet article décrit les étapes que j'ai suivies pour réduire le poids de la page d'accueil de mon site web à un niveau plus gérable.

### Qu'est-ce que la compression d'images ?

La compression d'images consiste à réduire la taille des fichiers tout en maintenant un niveau acceptable de qualité visuelle. Pour compresser les images de mon site, [imagemin](https://github.com/imagemin/imagemin) était mon outil de choix.

Pour utiliser `imagemin`, assurez-vous d'avoir [Node.js](https://nodejs.org/en/download) installé, puis ouvrez une fenêtre de terminal, accédez au dossier de votre projet avec `cd` et exécutez la commande suivante :

```
npm install imagemin
```

Ensuite, créez un nouveau fichier nommé `imagemin.js` et collez-y le contenu suivant :

```
const imagemin = require('imagemin');const PNGImages = 'assets/images/*.png';const JPEGImages = 'assets/images/*.jpg';const output = 'build/images';
```

N'hésitez pas à modifier les valeurs de `PNGImages`, `JPEGImages` et `output` pour qu'elles correspondent à la structure de votre projet.

Pour effectuer une compression, vous devez inclure quelques plugins en fonction du type d'image que vous souhaitez compresser.

### Compresser les JPEGs avec MozJPEG

Pour compresser les images JPEG, j'ai utilisé l'outil [MozJPEG](https://github.com/mozilla/mozjpeg) de Mozilla, disponible en tant que plugin Imagemin via [imagemin-mozjpeg](https://www.npmjs.com/package/imagemin-mozjpeg). Vous pouvez l'installer en exécutant la commande suivante :

```
npm install imagemin-mozjpeg
```

Ensuite, ajoutez ce qui suit à votre fichier `imagemin.js` :

```
const imageminMozjpeg = require('imagemin-mozjpeg');
```

```
const optimiseJPEGImages = () =>  imagemin([JPEGImages], output, {    plugins: [      imageminMozjpeg({        quality: 70,      }),    ]  });
```

```
optimiseJPEGImages()  .catch(error => console.log(error));
```

Vous pouvez exécuter le script en exécutant `node imagemin.js` dans le terminal. Cela traitera toutes les images JPEG et placera les versions optimisées dans le dossier `build/images`.

J'ai constaté que le réglage de `quality` à `70` produit des images suffisamment bonnes pour la plupart des cas, mais cela peut varier. Expérimentez avec cette valeur comme vous le jugez approprié.

`MozJPEG` génère des [JPEGs progressifs](https://cloudinary.com/blog/progressive_jpegs_and_green_martians) par défaut, ce qui fait que les images se chargent progressivement, de basse résolution à des résolutions plus élevées, jusqu'à ce que l'image soit entièrement chargée. Ils ont également tendance à être légèrement plus petits que les JPEGs de base en raison de leur mode d'encodage.

Vous pouvez vérifier si une image JPEG est progressive ou non en utilisant cet outil en ligne de commande pratique [command line tool](https://www.npmjs.com/package/is-progressive-cli) de Sindre Sorhus.

Les [avantages](https://images.guide/#the-advantages-of-progressive-jpegs) et les [inconvénients](https://images.guide/#the-disadvantages-of-progressive-jpegs) de l'utilisation des JPEGs progressifs ont été bien documentés par Addy Osmani. Pour moi, j'ai estimé que les avantages l'emportaient sur les inconvénients, donc j'ai conservé les paramètres par défaut.

Si vous préférez utiliser des JPEGs de base, vous pouvez définir `progressive` sur `false` dans l'objet des options. Assurez-vous également de revisiter la [page imagemin-mozjpeg](https://www.npmjs.com/package/imagemin-mozjpeg) pour voir les autres paramètres disponibles que vous pouvez ajuster.

### Optimiser les images PNG avec pngquant

[pngquant](https://pngquant.org/) est mon outil préféré pour optimiser les images PNG. Vous pouvez l'utiliser via [imagemin-pngquant](https://www.npmjs.com/package/imagemin-pngquant) :

```
npm install imagemin-pngquant
```

Ensuite, ajoutez ce qui suit à votre fichier `imagemin.js` :

```
const imageminPngquant = require('imagemin-pngquant');
```

```
const optimisePNGImages = () =>  imagemin([PNGImages], output, {    plugins: [      imageminPngquant({ quality: '65-80' })    ],  });
```

```
optimiseJPEGImages()  .then(() => optimisePNGImages())  .catch(error => console.log(error));
```

J'ai trouvé qu'un niveau de `quality` de `65-80` offre un bon compromis entre la taille du fichier et la qualité de l'image.

Avec ces paramètres, j'ai pu réduire une capture d'écran de mon site de 913 Ko à 187 Ko sans perte visible de qualité visuelle. **Une réduction impressionnante de 79 % !**

Voici les deux fichiers. Jetez un coup d'œil et jugez par vous-même :

* [Image originale](https://freshman.tech/assets/dist/images/articles/freshman-1600-original.png) (913 Ko)
* [Image optimisée](https://freshman.tech/assets/dist/images/articles/freshman-1600.png) (187 Ko)

### Servir des images WebP aux navigateurs qui les supportent

[WebP](https://developers.google.com/speed/webp/) est un format relativement nouveau introduit par Google qui vise à fournir des tailles de fichiers plus petites en encodant les images dans des formats [sans perte](https://fr.wikipedia.org/wiki/Compression_de_donn%C3%A9es#Compression_sans_perte) et [avec perte](https://fr.wikipedia.org/wiki/Compression_avec_pertes), ce qui en fait une excellente alternative aux formats JPEG et PNG.

La qualité visuelle des images WebP est souvent comparable à celle des JPEG et PNG, mais généralement avec une taille de fichier beaucoup plus réduite. Par exemple, lorsque j'ai converti la capture d'écran ci-dessus en WebP, j'ai obtenu un fichier de 88 Ko dont la qualité était comparable à l'image originale de 913 Ko. **Une diminution de 90 % !**

Jetez un coup d'œil aux trois images. Pouvez-vous voir la différence ?

* [Image PNG originale](https://freshman.tech/assets/dist/images/articles/freshman-1600-original.png) (913 Ko)
* [Image PNG optimisée](https://freshman.tech/assets/dist/images/articles/freshman-1600.png) (187 Ko)
* [Image WebP](https://freshman.tech/assets/dist/images/articles/freshman-1600.webp) (88 Ko, peut être vue dans Chrome ou Opera)

Personnellement, je pense que la qualité visuelle est comparable, et les économies réalisées sont difficiles à ignorer.

Maintenant que nous avons établi qu'il y a un intérêt à utiliser le format WebP lorsque cela est possible, il est important de noter qu'à l'heure actuelle, il ne peut pas remplacer complètement les formats JPEG et PNG, car le support de WebP dans les navigateurs n'est pas universel.

Au moment de la rédaction, Firefox, Safari et Edge sont des navigateurs notables qui ne supportent pas WebP.

![Image](https://cdn-media-1.freecodecamp.org/images/qglmcsNlDYBO1Qz6sZDRagxiBq498i3jbqRl)

Cependant, selon [caniuse.com](https://caniuse.com/#search=WebP), les navigateurs qui supportent WebP sont utilisés par plus de 70 % des utilisateurs dans le monde. Cela signifie que, en servant des images WebP, vous pourriez rendre vos pages web plus rapides pour environ 70 % de vos clients.

Examinons les étapes exactes pour servir des images WebP sur le web.

### Convertir vos JPEGs et PNGs en WebP

La conversion des images JPEG et PNG en WebP est assez facile avec le plugin [imagemin-webp](https://www.npmjs.com/package/imagemin-webp).

Installez-le en exécutant la commande suivante dans votre terminal :

```
npm install imagemin-webp
```

Ensuite, ajoutez ce qui suit à votre fichier `imagemin.js` :

```
const imageminWebp = require('imagemin-webp');
```

```
const convertPNGToWebp = () =>  imagemin([PNGImages], output, {    use: [      imageminWebp({        quality: 85,      }),    ]  });
```

```
const convertJPGToWebp = () =>  imagemin([JPGImages], output, {    use: [      imageminWebp({        quality: 75,      }),    ]  });
```

```
optimiseJPEGImages()  .then(() => optimisePNGImages())  .then(() => convertPNGToWebp())  .then(() => convertJPGToWebp())  .catch(error => console.log(error));
```

J'ai trouvé que le réglage de `quality` à `85` produit des images WebP similaires en qualité à leurs équivalents PNG, mais beaucoup plus petites. Pour les JPEGs, j'ai trouvé que le réglage de `quality` à `75` me donne un bon équilibre entre la qualité visuelle et la taille du fichier.

Pour être honnête, j'expérimente encore avec ces valeurs, alors ne les prenez pas comme une recommandation. Assurez-vous de revisiter la [page imagemin-webp](https://www.npmjs.com/package/imagemin-webp) pour voir les autres options disponibles.

### Servir des images WebP en HTML

Une fois que vous avez vos images WebP, vous pouvez utiliser le balisage suivant pour les servir aux navigateurs qui les supportent, tout en fournissant une alternative (optimisée) JPEG ou PNG pour les navigateurs qui ne supportent pas WebP.

```
<picture>    <source srcset="sample_image.webp" type="image/webp">    <source srcset="sample_image.jpg" type="image/jpg">    <img src="sample_image.jpg" alt=""></picture>
```

Avec ce balisage, les navigateurs qui comprennent le type de média `image/webp` téléchargeront la variante WebP et l'afficheront, tandis que les autres navigateurs téléchargeront la variante JPEG.

Tout navigateur qui ne comprend pas `<picture>` ignorera toutes les balises `source` et chargera ce qui est défini dans l'attribut `src` de la balise `img` en bas. Ainsi, nous avons amélioré progressivement notre page en fournissant un support pour toutes les classes de navigateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/mCVE11B4KRZOBUDJL-pWYotGbwFpfmwt1t6U)

Notez que dans tous les cas, la balise `img` est ce qui est réellement rendu sur la page, donc c'est effectivement une partie requise de la syntaxe. Si vous omettez la balise `img`, aucune image n'est rendue.

La balise `<picture>` et toutes les balises `source` définies à l'intérieur sont simplement là pour que le navigateur puisse choisir quelle variante de l'image utiliser. Une fois qu'une image source est choisie, son URL est transmise à la balise `img` et c'est ce qui est affiché.

Cela signifie que vous n'avez pas besoin de styliser la balise `<picture>` ou les balises `source`, car celles-ci ne sont pas rendues par le navigateur. Vous pouvez donc continuer à styliser uniquement la balise `img` comme avant.

### Conclusion

Comme vous pouvez le voir, le processus d'optimisation des images pour une utilisation sur le web n'est pas si compliqué et entraînera une meilleure expérience utilisateur pour vos clients en réduisant les temps de chargement des pages. Alors prenez quelques minutes aujourd'hui et effectuez une optimisation des images sur votre site web. Si vous avez d'autres recommandations, n'hésitez pas à les mentionner dans les commentaires ou sur [Twitter](https://twitter.com/ayisaiah).

Merci d'avoir lu !

Publié à l'origine sur [freshman.tech](https://freshman.tech/image-optimisation/) le 15 juillet 2018.