---
title: 'Tutoriel CSS sur les images réactives : comment rendre les images réactives
  avec CSS'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-30T01:28:00.000Z'
originalURL: https://freecodecamp.org/news/css-responsive-image-tutorial
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9879740569d1a4ca1a40.jpg
tags:
- name: CSS
  slug: css
- name: responsive design
  slug: responsive-design
- name: responsive images
  slug: responsive-images
seo_title: 'Tutoriel CSS sur les images réactives : comment rendre les images réactives
  avec CSS'
seo_desc: 'By Cem Eygi

  The majority of today’s websites are responsive. And if you need to center and align
  image on those site, you need to learn how to make images fluid or responsive with
  CSS.

  I posted a tutorial video that explains how to make a responsive ...'
---

Par Cem Eygi

La majorité des sites web d'aujourd'hui sont réactifs. Et si vous devez [centrer et aligner une image](https://www.freecodecamp.org/news/how-to-center-an-image-in-css/) sur ces sites, vous devez apprendre à rendre les images fluides ou réactives avec CSS.

J'ai publié une vidéo tutorielle qui explique comment créer un [site web réactif étape par étape](https://youtu.be/rKtOarvKeZE) il y a quelques semaines. Dans la vidéo, nous avons rendu une image réactive. Mais dans cet article, je souhaite donner un peu plus de détails sur la façon de rendre les images réactives.

Vous apprendrez également certains des problèmes généraux qui peuvent survenir lorsque vous essayez de rendre les images réactives – et j'essaierai d'expliquer comment les résoudre.

## Comment rendre les images réactives avec CSS

### Dois-je utiliser des unités relatives ou absolues ?

Rendre une image fluide, ou réactive, est en fait assez simple. Lorsque vous téléchargez une image sur votre site web, elle a une largeur et une hauteur par défaut. Vous pouvez les modifier toutes les deux avec CSS.

Pour rendre une image réactive, vous devez donner une nouvelle valeur à sa propriété de largeur. Ensuite, la hauteur de l'image s'ajustera automatiquement.

L'important à savoir est que vous devez toujours utiliser des unités relatives pour la propriété de largeur comme le pourcentage, plutôt que des unités absolues comme les pixels.

```css
img {
  width: 500px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Animated-GIF-downsized_large.gif)

Par exemple, si vous définissez une largeur fixe de 500px, votre image ne sera pas réactive – car l'unité est absolue.

```css
img {
  width: 50%;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Animated-GIF-downsized-1-.gif)

C'est pourquoi vous devriez plutôt attribuer une unité relative comme 50%. Cette approche rendra vos images fluides et elles pourront se redimensionner automatiquement, quelle que soit la taille de l'écran.

### Dois-je utiliser des requêtes média ?

L'une des questions qu'on me pose le plus est de savoir si vous devez utiliser des requêtes média ou non.

Une requête média est une autre fonctionnalité importante de CSS qui aide à rendre un site web réactif. Je ne vais pas entrer dans les détails ici, mais vous pouvez lire [mon autre article](https://www.freecodecamp.org/news/css-media-queries-breakpoints-media-types-standard-resolutions-and-more/) plus tard pour apprendre à utiliser les requêtes média en détail.

La réponse à cette question est : « cela dépend ». Si vous voulez que votre image ait des tailles différentes d'un appareil à l'autre, alors vous devrez utiliser des requêtes média. Sinon, vous n'en aurez pas besoin.

Maintenant, pour cet exemple, votre image a une largeur de 50% pour tout type d'écran. Mais lorsque vous voulez la rendre en pleine taille pour les appareils mobiles, vous devez utiliser des requêtes média :

```css
@media only screen and (max-width: 480px) {
  img {
    width: 100%;
  }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Animated-GIF-downsized-2-.gif)

Ainsi, selon la règle de la requête média, tout appareil plus petit que 480px prendra la pleine taille de la largeur de l'écran.

Vous pouvez également regarder la version vidéo de cet article ci-dessous :

%[https://youtu.be/5MeogG-ZFs8]

### Pourquoi la propriété max-width n'est-elle pas idéale ?

Une autre façon pour les développeurs de rendre les images réactives est d'utiliser la propriété max-width. Cependant, ce n'est pas toujours la meilleure méthode à utiliser, car elle peut ne pas fonctionner pour toutes les tailles d'écran ou tous les appareils.

La première chose à comprendre avant de continuer avec un exemple est ce que fait exactement la propriété max-width.

La propriété max-width définit une largeur maximale pour un élément, ce qui ne permet pas à la largeur de cet élément d'être plus grande que sa valeur max-width (mais elle peut être plus petite).

Par exemple, si l'image a une largeur par défaut de 500px, et si la taille de votre écran n'est que de 360px, alors vous ne pourrez pas voir l'image complète, car il n'y a pas assez d'espace :

```css
img {
  max-width: 100%;
  width: 500px;  // supposons que ceci est la taille par défaut
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Animated-GIF-downsized-3-.gif)

Par conséquent, vous pouvez définir une propriété max-width pour l'image et la régler à 100%, ce qui réduit l'image de 500px à l'espace de 360px. Ainsi, vous pourrez voir l'image complète sur un écran de plus petite taille.

Le bon côté des choses est que, puisque vous utilisez une unité relative, l'image sera fluide sur tout appareil plus petit que 500px.

Malheureusement, la taille de l'écran deviendra quelque peu plus grande que 500px, mais l'image ne le sera pas car elle a une largeur par défaut de 500px. Cette approche brisera la réactivité de l'image.

Pour corriger cela, vous devez utiliser à nouveau la propriété width, ce qui rend la propriété max-width inutile.

### Et pour les hauteurs ?

Un autre problème courant que vous pouvez rencontrer concerne la propriété height. Normalement, la hauteur d'une image se redimensionne automatiquement, donc vous n'avez pas besoin d'attribuer une propriété height à vos images (car cela brise un peu l'image).

Mais dans certains cas, vous devrez peut-être travailler avec des images qui doivent avoir une hauteur fixe. Ainsi, lorsque vous attribuez une hauteur fixe à l'image, elle sera toujours réactive mais elle n'aura pas l'air bien.

```css
img {
  width: 100%;
  height: 300px;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Animated-GIF-downsized-4-.gif)

Heureusement, il existe une autre propriété que CSS offre pour résoudre ce problème...

### Solution : La propriété Object-Fit

Pour avoir plus de contrôle sur vos images, CSS fournit une autre propriété appelée object-fit. Utilisons la propriété object-fit et attribuons une valeur, ce qui rendra votre image plus belle :

```css
img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  object-position: bottom;
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Animated-GIF-downsized-5-.gif)

Si nécessaire, vous pouvez également utiliser la propriété object-position (en plus de object-fit) pour vous concentrer sur une partie spécifique de l'image. Beaucoup de gens ne connaissent pas la propriété object-fit, mais elle peut être utile pour résoudre ce genre de problèmes.

J'espère que cet article vous a aidé à comprendre et à résoudre vos problèmes avec les images réactives. Si vous souhaitez en apprendre davantage sur le développement web, n'hésitez pas à consulter ma [chaîne YouTube](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q).

Merci d'avoir lu !