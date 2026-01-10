---
title: Un guide des images réactives avec des modèles prêts à l'emploi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-14T19:02:10.000Z'
originalURL: https://freecodecamp.org/news/a-guide-to-responsive-images-with-ready-to-use-templates-c400bd65c433
coverImage: https://cdn-media-1.freecodecamp.org/images/1*34Fn007F_nnaX4oTvB7S8A.jpeg
tags:
- name: image
  slug: image
- name: responsive design
  slug: responsive-design
- name: software
  slug: software
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Un guide des images réactives avec des modèles prêts à l'emploi
seo_desc: 'By Maciej Nowakowski

  Why generate 12 versions of the same image when just 2 media-queries do the job?
  The users won’t notice.

  But Google will.

  Responsive images that are in the wrong format, images that are not compressed properly,
  and images that ar...'
---

Par Maciej Nowakowski

Pourquoi générer 12 versions de la même image lorsque seulement 2 requêtes média suffisent ? Les utilisateurs ne remarqueront pas.

Mais Google, oui.

Les images réactives qui sont dans le mauvais format, les images qui ne sont pas correctement compressées et les images qui sont trop grandes diminueront toutes la vitesse de la page et auront un impact sur votre SEO.

Selon [Google](https://www.seroundtable.com/google-crawl-slow-tw0-seconds-20070.html), tout ce qui dépasse 2 secondes de temps de téléchargement découragera vos utilisateurs et dissuadera les crawlers d'indexer votre site web.

J'ai appris cela à mes dépens lorsque je reconstruisais mon [site web](https://www.codecamps.com). Mon objectif était de créer un site web simple qui se télécharge en un clin d'œil. Pour ce faire, j'ai opté pour [Gatsby.js](https://www.gatsbyjs.org/) — c'est rapide et je le connais.

Après quelques jours de codage, le site web était opérationnel. Mais, à ma déception, il a obtenu un modeste 78/100 sur mobile et un désastreux 57/100 sur le bureau sur [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/). Pas bon du tout.

![Image](https://cdn-media-1.freecodecamp.org/images/u7RYr2T5fN-uTzWMuChQiLIvgwNlF1AjFnbT)

PageSpeed Insights a suggéré une solution facile au problème. Il suffit de télécharger les images compressées que l'outil a créées, et tout ira bien.

Cela a éveillé ma curiosité. Et plus je pensais aux tailles, aux formats et aux niveaux de compression, plus je me sentais submergé par l'abondance de choix. PNG, JPG, SVG, chaînes encodées en base64 en ligne… ou peut-être WebP ?

Pour m'y retrouver, je me suis plongé dans le monde des pixels, j'ai traversé les eaux troubles des conseils aléatoires sur le sujet et j'ai élaboré une approche systématique.

Et une fois que j'ai appliqué ce que j'ai appris, mon score PageSpeed est passé de 78 à 91 sur mobile et de 57 à 99 sur bureau !

![Image](https://cdn-media-1.freecodecamp.org/images/H7rCqoAEGVKILvE9kB7s7UBn0yxkpnwHYjQI)

Dans cet article, je vais vous montrer comment générer rapidement des images réactives qui fonctionnent dans tous les navigateurs et réduisent massivement vos temps de téléchargement.

### Avant de commencer

Si vous voulez optimiser une image, vous devez commencer par une image de haute qualité qui a le bon format et la bonne taille :

* Utilisez des JPG pour les photos et des PNG pour les graphiques ou autres images nécessitant de la transparence
* Utilisez des PNG-8 plus petits au lieu de PNG-24 pour les graphiques avec un nombre limité de couleurs. Pour réduire encore la taille, vous pouvez également réduire le nombre de couleurs, de 256 à 16
* Utilisez des SVG (images vectorielles) pour les icônes et les logos. Ils s'adapteront parfaitement sans augmenter la taille de votre fichier
* Utilisez des images en ligne de moins de 10 Ko sous forme de chaînes encodées en base64 (avec parcimonie)
* La largeur réelle d'une image ne doit pas dépasser la largeur du plus grand conteneur dans lequel elle sera affichée, multipliée par deux (pour les écrans rétina)

### Pixels matériels et logiciels

L'image qui prend toute la largeur de l'écran du Macbook Pro 15" est large de 1440 pixels, mais la [résolution réelle](http://pixensity.com/) de l'écran rétina est le double, soit 2880x1800. Pourquoi ? À cause de son facteur de densité de pixels de 2.

Les anciens moniteurs ont une densité de pixels de 1. Mais comme les résolutions d'écran ont augmenté ces dernières années, le pixel matériel n'est plus égal au pixel logiciel ou CSS.

La relation entre les pixels matériels et CSS est décrite par la formule suivante :

**Pixels CSS = Pixels matériels / Densité de pixels**

Par conséquent, une résolution matérielle de 2880 pixels se traduit par 1440 pixels CSS sur l'écran rétina. Cela explique également pourquoi, lorsque vous inspectez l'image en pleine largeur dans les outils de développement, vous la verrez comme large de seulement 1440 pixels au lieu des 2880 pixels d'origine.

L'écran rétina a été une avancée majeure il y a quelques années. Aujourd'hui, les appareils mobiles ont des écrans encore "plus denses" de 3 et même 4 pour le Samsung Galaxy S8+ !

Pour les besoins de mon expérience, j'ai décidé que pour être ultra-nette, l'image en pleine largeur devait avoir une largeur maximale de 2880 pixels.

Avec la hauteur de l'image réglée à 600px et la qualité à 75%, Photoshop a produit un fichier massif de 939 Ko. C'est à peine acceptable.

Après quelques expériences avec les niveaux de compression, il est devenu clair que la compression des JPG en dessous de 60% de qualité résultait en une perte de qualité visible. J'ai réglé la qualité à 60% comme point de départ et la taille de l'image est passée à 681 Ko. Toujours loin d'être décente.

### Format WebP

"WebP est un format d'image moderne qui offre une compression supérieure sans perte et avec perte pour les images sur le web," selon [Google](https://developers.google.com/speed/webp/).

Après la conversion au format WebP, mon image n'était pas seulement plus petite mais aussi plus nette ! WebP a réduit de 34% la taille du JPEG compressé. "Je suis sur la bonne voie", ai-je pensé !

Malheureusement, le format WebP est supporté par Chrome et Opera, soit environ 60% de tous les navigateurs, selon [Can I use](https://caniuse.com/#search=webp). Je savais donc que je devrais penser à des options de repli.

Enfin, les limites étaient fixées :

* Niveau de compression à 60%
* Format WebP lorsque possible

J'ai également choisi de supporter trois points de rupture : 600px et 900px ([voici pourquoi](https://medium.freecodecamp.org/the-100-correct-way-to-do-css-breakpoints-88d6a5ba1862)) et 2 densités de pixels — 1x et 2x pour les écrans rétina. Cela signifiait 6 images différentes au lieu de seulement deux. La prise en charge du format WebP a doublé le nombre.

Il existe deux façons principales de placer une image sur un site web, soit en utilisant l'élément `img` de HTML ou une `background-image` en CSS.

### Images réactives en HTML

L'élément HTML de base `img` a l'attribut `src` qui pointe vers l'URL de l'image :

```html
<img src="image.jpg" alt="description de l'image"/>
```

Mais vous pouvez aller plus loin et décider quelle image servir en fonction de la densité de pixels de l'écran avec l'attribut `srcset` :

```html
<img srcset="image_1x.jpg 1x, image_2x.jpg 2x" src="image_1x.jpg"/>
```

Ici, j'ai utilisé deux densités d'écran différentes : `1x` et `2x`. Selon la densité d'affichage réelle, le navigateur choisira la bonne. L'attribut `src` pointe vers l'option de repli.

Pour le moment, la plupart des navigateurs sauf IE, Edge et Opera Mini ont implémenté l'attribut `srcset`.

Cette solution semble être un pas dans la bonne direction. Malheureusement, votre navigateur sélectionnera toujours la même image, avec la même densité de pixels, indépendamment de la taille de l'affichage. Et la même image se retrouvera à la fois sur le bureau et sur l'appareil mobile.

Nous avons besoin de plus de contrôle. Et nous pouvons l'avoir. En plus des densités de pixels, l'attribut `scrset` accepte les unités de largeur `w`, un équivalent des pixels CSS.

L'unité de largeur permet au navigateur de choisir la bonne taille d'image pour les capacités d'affichage données.

Avec deux points de rupture (600px et 900px), nous pouvons opter pour trois tailles d'image différentes :

```html
<img
  srcset="image-sm.jpg 600w,
          image-md.jpg 900w,
          image-lg.jpg 1440w"
  src="image_1x.jpg"
/>

```

Il y a un piège ici. Lorsque le navigateur décide quelle image récupérer, il n'a aucune connaissance de notre CSS ! Le fichier CSS n'a pas encore été récupéré à ce stade. Et il suppose que l'image sera affichée à la largeur totale de la fenêtre.

Si une image en pleine largeur est ce que vous voulez, alors c'est bien. Mais que faire si vous voulez placer une image dans un conteneur qui n'est large que de `50vw` ? Voici l'attribut `sizes` qui entre en jeu. Jetons un coup d'œil :

```html
<img
  srcset="image-sm.jpg 600w,
          image-md.jpg 900w,
          image-lg.jpg 1440w"
  sizes="50vw"
  src="image_1x.jpg"
/>

```

En ajoutant l'attribut `sizes="50vw"`, vous indiquez au navigateur que l'image sera affichée à `50vw`, et sur la base de cette information, le navigateur décidera quelle image afficher.

Mais que faire si vous voulez afficher votre image à `50vw` sur un grand écran et à la largeur totale de `100vw` sur un appareil mobile ? L'attribut `sizes` accepte également les requêtes média !

Vous pouvez spécifier qu'en dessous du point de rupture mobile de `600px`, vous voulez que le navigateur affiche votre image à une largeur plein écran. Et pour la largeur supérieure au point de rupture mobile, vous voulez que le navigateur affiche votre image à `50vw`.

Vous pouvez faire cela en ajoutant la requête média :

```html
<img
  srcset="image-sm.jpg 600w,
          image-md.jpg 900w,
          image-lg.jpg 1440w"
  sizes="(max-width: 600px) 100vw, 50vw"
  src="image_1x.jpg"
/>

```

N'oubliez pas que dans la ligne de code ci-dessus, vous instruisez le navigateur sur l'image à choisir car le navigateur ne connaît pas le CSS correspondant. Vous devez toujours ajouter les points de rupture dans le CSS explicitement.

Cette solution fonctionne vraiment bien, mais nous manquons ici des densités de pixels ! Si nous nous arrêtions ici, nous enverrions la même image à la fois aux écrans avec une densité de pixels de `1x` et aux écrans rétina. Heureusement, il existe une solution facile.

### Élément Picture

Rencontrez l'élément HTML5 `picture`. Il accepte les éléments `source` et `img` comme ses enfants. Nous pouvons utiliser l'élément `source` pour lister des formats d'image supplémentaires que nous voulons servir au navigateur.

Mais avant de corriger les densités de pixels, introduisons des images plus petites et plus nettes au format WebP.

Ajoutons l'élément `source` comme première option à l'intérieur de l'élément `picture` avec votre image au format WebP suivie de l'`img` pointant vers l'image JPG régulière. Maintenant, lorsque le navigateur n'est pas prêt pour le WebP, il basculera élégamment vers l'élément `img` (par exemple, Safari).

```html
<picture>
  <source
    srcset="image.webp"
    type="image/webp"
  />
  <img
    src="image.jpg"
    type="image/jpeg"
    alt="description de l'image"
  />
</picture>

```

L'élément `source` ouvre un tout nouveau monde de possibilités. Il accepte les requêtes média !

Tout d'abord, dans l'attribut `media`, nous utilisons la requête média et ensuite, dans l'attribut `srcset`, nous plaçons l'image appropriée. Et nous pouvons utiliser autant d'éléments `source` que nous le souhaitons :

```html
<picture>
  <source
    media="(min-width: 900px)"
    srcset="image-lg.webp"
    type="image/webp"
  />
  <source
    media="(min-width: 600px)"
    srcset="image-md.webp"
    type="image/webp"
  />
  <source
    srcset="image-sm.webp"
    type="image/webp"
  />
  <img
    src="image-lg.jpg"
    type="image/jpeg"
    alt="description de l'image"
  />
</picture>

```

Ci-dessus, nous avons préparé trois images au format WebP, en fonction de la taille de l'écran, et une image JPG comme option de repli.

Le dernier secret de l'attribut `srcset` est qu'il accepte également les densités de pixels. Nous pouvons décider quelle image nous voulons servir sur quel écran et à quelle densité de pixels. L'astuce est de lister les fichiers image dans le `scrset` suivis d'un espace et du facteur de densité de pixels, par exemple : `1x`, `2x`, `3x`, ou même `4x`.

```html
<picture>
  <source
    media="(min-width: 900px)"
    srcset="image-lg_1x.webp 1x, image-lg_2x.webp 2x"
    type="image/webp" />
  <source
    media="(min-width: 601px)"
    srcset="image-md_1x.webp 1x, image-md_2x.webp 2x"
    type="image/webp" />
  <source srcset="image-sm_1x.webp 1x, image-sm_2x.webp 2x" type="image/webp" />
  <img
    srcset="image-sm_1x.jpg 600w, image-md_1x.jpg 900w, image-lg_1x.jpg 1440w"
    src="image_lg_1x.jpg"
    type="image/jpeg"
    alt="description de l'image"
  />
</picture>
...
```

Puisque nous avons trié les tailles d'écran et les densités de pixels pour le format WebP, examinons de plus près l'option de repli. Après tout, certains navigateurs ne supportent pas le format WebP.

Ici, nous devons décider si nous voulons utiliser des images avec une densité de 1 ou 2 pixels. Ci-dessous, j'ai opté pour la première option :

```html
<picture>
  <source
    media="(min-width: 900px)"
    srcset="image-lg_1x.webp 1x, image-lg_2x.webp 2x"
    type="image/webp"
  />
  <source
    media="(min-width: 601px)"
    srcset="image-md_1x.webp 1x, image-md_2x.webp 2x"
    type="image/webp"
  />
  <source srcset="image-sm_1x.webp 1x, image-sm_2x.webp 2x" type="image/webp" />
  <img
    srcset="image-sm_1x.jpg 600w, image-md_1x.jpg 900w, image-lg_1x.jpg 1440w"
    src="image_lg_1x.jpg"
    type="image/jpeg"
    alt="description de l'image"
  />
</picture>

```

Nous avons remplacé l'élément `img` par l'élément `picture`. Là où c'est possible, nous voulons livrer des images au format WebP en trois tailles différentes, selon la taille de l'écran, et en 2 densités de pixels différentes. Si le navigateur ne supporte pas l'élément `picture` ou le format WebP, il basculera vers l'élément `img` standard avec trois tailles différentes de JPG.

**Important :** Remarquez que dans l'élément `img`, l'attribut `srcset` doit être placé avant l'attribut `src`. Sinon, le navigateur téléchargera d'abord l'image `src` et ensuite, s'il trouve une meilleure image dans le `srcset`, il la téléchargera également. De cette façon, nous nous retrouverions avec deux images.

Nous pourrions aller plus loin et créer trois autres éléments `source` pour les navigateurs qui ne supportent pas le format WebP et livrer des fichiers JPG à la place.

Bien que cela fonctionne très bien pour Firefox, j'ai remarqué que Safari téléchargera les deux fichiers : le JPG listé dans le `source` **et** le JPG de l'élément `img`. Encore une fois, nous nous retrouverions avec deux images au lieu d'une.

### Images réactives en CSS

Si nous ne connaissons pas la hauteur et la largeur exactes du conteneur que nous voulons couvrir avec une image, nous pouvons utiliser des éléments génériques comme `div` avec la propriété `background-image` pointant vers l'URL de l'image :

```html
background-image: url("/images/image.jpg");
```

CSS, de manière similaire à HTML, permet l'optimisation de la taille des images.

L'`image-set` en CSS est l'équivalent du `srcset` en HTML. Pour le moment, il est implémenté dans Chrome, Chrome pour Android, Safari, iOS Safari et quelques autres navigateurs. Vous pouvez ajouter des [polyfills](https://github.com/wtfil/image-set-polyfill) pour faire fonctionner `image-set` sur d'autres navigateurs, mais étant donné que Chrome et Safari combinés sont les navigateurs de choix pour 70% des utilisateurs aujourd'hui, il y a de bonnes chances que la plupart des navigateurs implémenteront l'attribut dans un avenir proche.

Mais ne vous inquiétez pas, le `background-image` régulier comme option de repli fera l'affaire.

La structure est très similaire à ce que nous venons d'utiliser dans un attribut `srcset`.

Pour créer un élément d'image en pleine largeur avec une hauteur de 500px, nous devons commencer par l'option de repli — le premier `background-image` dans l'exemple de code ci-dessous. Ensuite, en utilisant le `-webkit-image-set`, nous devons lister les images WebP pour différentes densités de pixels. Et nous devons répéter le processus pour différents points de rupture en utilisant des requêtes média.

Une chose importante à retenir est que Chrome et Safari utilisent tous deux le moteur de mise en page WebKit, mais Safari ne supporte pas le format WebP. C'est pourquoi nous devons ajouter le dernier ensemble d'attributs `image-set` avec des images JPG (il sera utilisé par Safari même s'il ne commence pas par `-webkit`).

```css
.bg-image {
  width: 100vw;
  height: 500px;

  background-size: cover;
  background-position: center;

  background-image: url(/images/image-lg_1x.jpg);
  background-image: -webkit-image-set(
    url(/images/image-lg_1x.webp) 1x,
    url(/images/image-lg_2x.webp) 2x
  );
  background-image: image-set(
    url(/images/image-lg_1x.jpg) 1x,
    url(/images/image-lg_2x.jpg) 2x
  );
    
  @media (max-width: 900px) {
    background-image: url(/images/image-md_2x.jpg);
    background-image: -webkit-image-set(
      url(/images/image-md_1x.webp) 1x,
      url(/images/image-md_2x.webp) 2x
    );
    background-image: image-set(
      url(/images/image-md_1x.jpg) 1x,
      url(/images/image-md_2x.jpg) 2x
    );
  }
    
  @media (max-width: 600px) {
    background-image: url(/images/image-sm_2x.jpg);
    background-image: -webkit-image-set(
      url(/images/image-sm_1x.webp) 1x,
      url(/images/image-sm_2x.webp) 2x
    );
    background-image: image-set(
      url(/images/image-sm_1x.jpg) 1x,
      url(/images/image-sm_2x.jpg) 2x
    );
  }
}

```

Ici, l'image de fond est centrée dans l'élément `div` et couvre toute sa surface. En utilisant l'attribut `image-set`, nous attribuons deux images différentes à deux densités de pixels différentes.

L'option de repli avec une `url` standard prend en charge les navigateurs qui ne supportent pas l'attribut `image-set`.

Il est très important de placer l'option de repli **avant** les `background-images` avec l'attribut `image-set`. Si vous la placez après l'attribut `image-set`, par exemple, Safari téléchargera les deux, l'image de `image-set` et l'image de l'option de repli s'il trouve une image avec un nom de fichier différent.

Le reste du code suit le même schéma. Ci-dessus, j'ai ajouté des requêtes média pour les points de rupture 600px et 900px et un ensemble d'images correspondantes en tailles plus petites.

L'option de repli doit toujours utiliser le format JPG pour éviter la situation où une image ne peut pas être affichée du tout, c'est-à-dire lorsque le navigateur ne supporte pas l'attribut `image-set` ou le format WebP.

### Comment intégrer de petites images

Pour améliorer l'expérience utilisateur, nous devons non seulement compresser et servir les plus petites images possibles, mais nous devons également réduire le nombre de requêtes que nous envoyons au serveur.

Le navigateur doit envoyer une requête séparée pour chaque image. Lorsqu'elle est envoyée au serveur, la requête doit d'abord attendre dans une file d'attente, ce qui prend du temps. Plus le navigateur fait d'appels, plus l'utilisateur doit attendre.

Cela est particulièrement vrai lorsque vous devez télécharger de nombreuses petites images. Si possible, les logos et les icônes doivent être enregistrés sous forme de graphiques vectoriels (SVG). Les petites images peuvent être intégrées soit en HTML, soit directement en CSS sous forme de chaînes encodées en base64.

Au lieu de passer une URL régulière à l'attribut `src` dans l'élément `img`, nous pouvons passer l'image sous forme de chaîne :

```html
<img
  src="data:image/png;base64,encoded string"
  alt="description de l'image"
/>
```

et en CSS :

```css
.small-image {
  background-image: url(data:image/png;base64,encoded string);
}

```

Dans la plupart des cas, la chaîne générée sera environ 30% plus grande que l'image originale, mais vous gagnerez du temps sur un autre aller-retour vers le serveur.

L'argument le plus courant contre l'utilisation d'images encodées en base64 dans les fichiers CSS est que les images sont des ressources non bloquantes, contrairement aux fichiers CSS. Cela signifie que si vous intégrez trop de petites images dans votre CSS, cela augmentera la taille du fichier CSS et allongera le temps jusqu'au premier rendu du site web. Cela, à son tour, fera attendre l'utilisateur plus longtemps avant qu'il ou elle ne puisse voir du contenu.

[Voici](https://csswizardry.com/2017/02/base64-encoding-and-performance/) un excellent article sur pourquoi vous pourriez envisager d'abandonner l'idée d'utiliser des chaînes encodées pour les images entièrement.

La vérité se situe probablement quelque part au milieu, et injecter un ou deux petits fichiers sous forme de chaînes base64 dans le CSS ou le HTML ne devrait pas faire de mal.

À la fin de cet article, vous apprendrez comment les générer. Cela peut sembler étrange au début car ces chaînes font des milliers de caractères de long. Votre classe `.logo` peut ressembler à ceci, mais plus longue :

```css
.logo {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAA NSUhEUgAABqIAAAFvCAMAAAAWmCq0AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZS BJbWFnZVJlYWR5ccllPAAAA3hpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAA Dw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5U Y3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0
);
}

```

### Comment générer des images réactives

Supposons que vous venez d'enregistrer une image parfaite et que vous souhaitez créer toutes les variations pour pouvoir l'utiliser sur votre site web.

Il existe de nombreux outils qui peuvent aider. Les outils simples incluent [compressjpeg.com](http://compressjpeg.com/), [compresspng.com](http://compresspng.com/), et [tinyjpg.com](https://tinyjpg.com/). Les outils plus avancés incluent [ImageOptim](https://imageoptim.com) pour les JPEG, PNG et GIF, et [ImageAlpha](https://pngmini.com/) pour les PNG.

Dans ma quête pour prendre le contrôle total des niveaux de compression, des formats et de la mise à l'échelle, j'avais besoin d'un outil qui m'aiderait à automatiser tout le processus. Et je n'avais pas envie de glisser-déposer des dizaines d'images.

[ImageMagic](http://www.imagemagick.org/script/index.php) et [GraphicsMagick](http://www.graphicsmagick.org/) sont des logiciels gratuits et puissants qui s'associent sans douleur avec [Grunt](https://gruntjs.com/), l'exécuteur de tâches JavaScript.

Mieux encore, il existe des plugins Grunt qui simplifient encore la tâche. Plusieurs tests rapides ont montré que GraphicsMagick génère des images JPG 20% plus petites qu'ImageMagic au même niveau de compression. Le choix était donc clair.

Avant de commencer à nous frayer un chemin à travers la jungle des pixels, nous devons préparer nos outils et affûter notre hache. Téléchargez GraphicsMagick depuis [ici](http://www.graphicsmagick.org/download.html) ou utilisez [Homebrew](http://www.graphicsmagick.org/download.html) pour l'installer.

```
brew install graphicsmagick
```

Ensuite, installez l'interface en ligne de commande de Grunt globalement :

```
npm install -g grunt-cli
```

Créez un dossier séparé `responsive-images` et initialisez le projet :

```
mkdir responsive-images
cd responsive-images
npm init
```

Et enfin, installez la version locale de Grunt :

```
npm install grunt --save-dev
```

Créez deux dossiers : `src/` pour les images originales et `dest/` pour les images réactives que Grunt et GraphicsMagick généreront :

```
mkdir src
mkdir dest
```

L'image originale doit être enregistrée à une résolution égale ou supérieure à la plus grande image que vous souhaitez générer dans le dossier `src/`. J'ai enregistré la mienne en JPG à 100% de qualité et 2880 pixels de large. Elle faisait environ 2,5 Mo.

Tout d'abord, générons des images réactives en utilisant le plugin [grunt-responsive-images](http://www.andismith.com/grunt-responsive-images/). Installez-le :

```
npm install grunt-responsive-images --save-dev
```

Maintenant, dans le répertoire racine du projet, créez un fichier supplémentaire `Gruntfile.js` :

```
touch Gruntfile.js
```

C'est ici que nous devons configurer le plugin.

Copiez et collez le code dans le `Gruntfile.js` et laissez-moi vous guider à travers le code :

```js
module.exports = function (grunt) {
  grunt.initConfig({
    responsive_images: {
      dev: {
        options: {
          engine: "gm",
          sizes: [
            { name: "sm", suffix: "_1x", quality: 60, width: 600 },
            { name: "sm", suffix: "_2x", quality: 60, width: 1200 },
            { name: "md", suffix: "_1x", quality: 60, width: 900 },
            { name: "md", suffix: "_2x", quality: 60, width: 1800 },
            { name: "lg", suffix: "_1x", quality: 60, width: 1440 },
            { name: "lg", suffix: "_2x", quality: 60, width: 2880 },
          ],
        },
        files: [
          {
            expand: true,
            src: ["**/*.{jpg,png}"],
            cwd: "src/",
            dest: "dest/",
          },
        ],
      },
    },
  });
  grunt.loadNpmTasks("grunt-responsive-images");
  grunt.registerTask("default", ["responsive_images"]);
};

```

Dans `options`, nous définissons GraphicsMagick comme notre moteur de choix : `engine: "gm"`. Vous pouvez également tester ImageMagick en le changeant en `engine: "im"`.

Ensuite, dans le tableau `sizes`, nous devons spécifier les paramètres des images que nous voulons produire, tels qu'un `name` qui sera ajouté au nom original, un `suffix` qui sera également ajouté au nom, une `quality` et une `width`.

Les images résultantes auront la structure de nom suivante :

```js
original-[name]_[suffix}.jpg
```

Par exemple, en utilisant le premier objet `sizes`, Grunt générera à partir de l'original `my-image.jpg` l'image `my-image-sm_1x.jpg` à un niveau de compression de 60% et 600 pixels de large.

En dessous des options, nous devons lister les dossiers source et de destination ainsi que les motifs de noms de fichiers que nous voulons traiter.

Pour permettre la construction dynamique d'objets de fichiers, définissons l'attribut `expand` sur `true` et définissons :

* `cwd` — dossier source
* `src` — un tableau de motifs à correspondre. Dans notre cas, nous voulons correspondre à n'importe quel dossier (`**`) à l'intérieur du dossier source et tous les fichiers avec les extensions `jpg` ou `png`
* `dest` — dossier de destination

La tâche Grunt ci-dessus générera un ensemble de fichiers JPG et/ou PNG, selon les extensions de fichiers d'images sources.

Nous voulons également produire un ensemble correspondant d'images WebP.

Nous avons besoin d'un autre plugin pour faire le travail : `grunt-cwebp`. Installons-le :

```
npm install grunt-cwebp --save-dev
```

Ajoutez le Gruntfile.js avec la configuration suivante :

```js
module.exports = function (grunt) {
  grunt.initConfig({
    responsive_images: {
      ...
    },
    cwebp: {
      dynamic: {
        options: {
          q: 60,
        },
        files: [
          {
            expand: true,
            cwd: "dest/",
            src: ["**/*.{jpg,png}"],
            dest: "dest/",
          },
        ],
      },
    },
  });
  grunt.loadNpmTasks("grunt-responsive-images");
  grunt.loadNpmTasks("grunt-cwebp");
  grunt.registerTask("default", ["responsive_images", "cwebp"]);
};

```

Le plugin `grunt-cwebp` utilise le dossier `dest/` comme source d'images. Nous voulons que tous les nouveaux JPG produits aient leurs frères et sœurs WebP et nous devons les placer dans le même dossier.

Maintenant, nous pouvons traiter les images :

```
grunt
```

Pour chaque image dans le dossier `src/`, Grunt générera 12 images dans toutes les tailles nécessaires, densités de pixels et dans les formats JPG et WebP !

### Comment générer des chaînes base64

Si vous souhaitez générer des chaînes base64 pour intégrer vos images, voici comment faire.

Cette fois, utilisons le plugin Grunt : `grunt-base64`.

Créez un nouveau projet dans un dossier séparé `base64-images`. Initialisez-le avec `npm` et installez la version locale de Grunt :

```
mkdir base64-images
cd base64-images
npm init
npm install grunt --save-dev
```

Installez le plugin `grunt-base64` :

```
npm install grunt-base64 --save-dev
```

Dans le répertoire racine, créez un nouveau dossier `images/` et le `Gruntfile.js` :

```
mkdir images
touch Gruntfile.js
```

et copiez et collez le code dans le `Gruntfile.js` :

```js
module.exports = function (grunt) {
  grunt.initConfig({
    base64: {
      dev: {
        files: {
          "images/output.b64": ["images/*.{jpg,png}"],
        },
      },
    },
  });
  grunt.loadNpmTasks("grunt-base64");
  grunt.registerTask("default", ["base64"]);
};

```

Placez la petite image originale dans le dossier `images/` et exécutez Grunt :

```
grunt
```

Après la fin de la tâche, copiez tout le contenu du fichier `output.b64` — c'est la chaîne base64 que vous pouvez coller dans l'`url` de la `background-image` ou dans l'attribut `src` de l'élément `img`.

Il existe également une méthode plus simple (sur Mac OS X ou Linux) :

```
uuencode -m image-file-name remotename
```

Le `remotename` n'est pas utilisé et vous pouvez même placer `xyz` pour obtenir la chaîne base64 imprimée dans la sortie standard — dans la plupart des cas, dans la fenêtre du terminal. Vous devez utiliser l'option `-m` pour obtenir l'encodage base64.

### Conclusion

Les images réactives peuvent sembler accablantes au premier abord, mais avec Grunt et les moteurs de traitement d'images à vos côtés, vous pouvez créer un processus fluide et automatiser la plupart des tâches répétitives. Et je vous promets que cela en vaut la peine. Vous ne brillerez pas seulement dans PageSpeed Insights, mais vous réduirez également le temps jusqu'au premier rendu de votre site web.

Dans mon cas, l'image originale de 939 Ko a été réduite de 60% à 380 Ko (JPG) et de 77% à 218 Ko au format WebP.

En fin de compte, ma croisade pour les pixels a porté ses fruits — la note PageSpeed Insight pour mon site web est passée au vert.

Si vous avez aimé cet article, 👍 même 50 fois — je l'apprécierais vraiment et cela fait une énorme différence pour moi.

![Image](https://cdn-media-1.freecodecamp.org/images/5dYg5xZsBky2ymubt27EUprpi54rOuG9TZBK)

J'ai récemment publié un tutoriel React gratuit pour débutants. Si vous voulez apprendre à construire une application web à partir de zéro, c'est un excellent point de départ. Vous apprendrez à construire une application pour vous aider à trouver le meilleur film à regarder 👉 [Sweet Pumpkins](https://sweetpumpkins.codecamps.com/)