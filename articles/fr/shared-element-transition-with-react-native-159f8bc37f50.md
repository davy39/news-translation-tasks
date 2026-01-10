---
title: Transition d'élément partagé avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-14T14:45:29.000Z'
originalURL: https://freecodecamp.org/news/shared-element-transition-with-react-native-159f8bc37f50
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XjqvwLtPW_Gwu8dtlubs7Q.png
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
- name: UX
  slug: ux
seo_title: Transition d'élément partagé avec React Native
seo_desc: 'By Narendra N Shetty

  In this post I will be talking about how to achieve Shared Element Transition with
  React Native for both iOS and Android.

  I have posted the code on GitHub and you can take a look if you want to jump right
  into it.

  Intent

  Lets tak...'
---

Par Narendra N Shetty

Dans cet article, je vais parler de la manière d'atteindre une transition d'élément partagé avec React Native pour iOS et Android.

J'ai posté le code sur [GitHub](https://github.com/narendrashetty/photo-gallery-RN) et vous pouvez y jeter un coup d'œil si vous voulez plonger directement dedans.

### Intention

Regardons ce que nous allons construire. Ci-dessous se trouve un exemple de grille photo où nous ajouterons une transition d'élément partagé. Ainsi, nous pouvons effectuer une transition fluide entre une grille et la page de détails pour une photo que nous sélectionnons.

![Image](https://cdn-media-1.freecodecamp.org/images/ZFx3Y2ZbOyPA2C6sM-GcnUcBYAmGywCLVdcg)

C'est une expérience beaucoup plus fluide et continue.

### Approche

Avant de construire cela, laissez-moi vous expliquer comment le système fonctionne en coulisses. Puisque React Native ne supporte pas les vrais éléments partagés, lorsque nous disons que nous effectuons une transition d'élément partagé entre deux écrans, nous ne partageons techniquement aucun élément. Au lieu de cela, chaque écran a son propre élément individuel.

![Image](https://cdn-media-1.freecodecamp.org/images/bGX-qwWTtkSs5V5u8-02ldcXmz1rqZTS7I2k)

Ce que je fais, c'est transmettre les informations sur l'élément partagé — telles que sa position et sa taille — entre ces deux éléments.

![Image](https://cdn-media-1.freecodecamp.org/images/kYlMlrL69TVmnl05mbdzD15rBoYCuzmBirYl)

Lorsque l'écran de détails se lance, son arrière-plan est défini comme transparent, et il masque tous ses éléments. Il modifie ensuite les attributs de l'élément partagé à ceux transmis, puis le rend visible. Il anime ensuite lui-même vers sa position naturelle. Au fur et à mesure que la transition progresse, l'arrière-plan de la fenêtre et le reste des éléments non partagés s'estompent lentement jusqu'à ce qu'ils soient totalement opaques.

Ainsi, bien que l'élément ne soit pas techniquement partagé, ce tour astucieux de fumée et de miroir donne l'impression qu'ils le sont.

Maintenant que nous comprenons comment ce processus fonctionne, allons étape par étape pour comprendre comment l'élément fictif a été partagé, et comment nous pouvons contrôler les animations.

#### Étape 1 : Animation d'entrée et de sortie

J'ai deux écrans ici : Grille et Détails. À partir de l'écran Grille, nous pouvons lancer l'écran Détails en cliquant sur l'une des images de la grille. Ensuite, nous pouvons revenir à l'écran de grille en appuyant sur le bouton retour.

![Image](https://cdn-media-1.freecodecamp.org/images/Pl0Q1HzBuRyzczRY9nr0pdpM6oNvXyKkVa3P)

Lorsque nous passons de l'écran Grille à l'écran Détails, nous avons l'opportunité d'exécuter deux ensembles d'animations de transition — la transition de sortie pour l'écran Grille, et la transition d'entrée pour l'écran Détails.

![Image](https://cdn-media-1.freecodecamp.org/images/XcGZR2W0yZxivXxgvtqNDYwkWgdMvJgFOkpo)

Voyons comment nous implémentons cela.

Sans aucune transition, voici à quoi ressemble l'application. Cliquer sur l'image individuelle vous emmène à un écran de détail.

![Image](https://cdn-media-1.freecodecamp.org/images/MaVm33kp41KI5dqxVTXt9qqSL3tb0nLLmzDw)

Ajoutons une transition de sortie au premier écran de grille. Ici, nous utilisons une simple transition de fondu avec l'API `Animated`, qui interpole l'attribut d'opacité du conteneur de l'écran de grille de 1 à 0.

![Image](https://cdn-media-1.freecodecamp.org/images/Mp3343DgX5cx1FwUyIiPlmBvychD3jvsHSCV)

Maintenant que nous avons fait cela, voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/CQYSnNoG9QDBSWoSCSBBgUGnjxHq90SWXT1w)

Pas trop mal. Nous voyons que la grille s'estompe lorsque nous passons à l'écran de détails.

Ajoutons maintenant une autre transition au contenu de l'écran de détail lorsqu'il arrive. Faisons glisser le texte en place depuis le bas.

Cela est fait en attribuant une valeur `Animated` interpolée à la propriété `translateY` du conteneur de texte.

![Image](https://cdn-media-1.freecodecamp.org/images/kAniu9N72G8oW5JQ8t89Rv54fWDAX0Oha1pU)

Et voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/X0YkE34bdPvzpf-0NhO83UVqvmStSjdCLYbU)

Le titre et la description glissent très bien, mais l'image apparaît brusquement. Cela est dû au fait que notre transition ne cible pas spécifiquement l'image. Nous allons corriger cela sous peu.

#### Étape 2 : Couche de transition pour l'élément partagé

Nous ajoutons maintenant une couche de transition qui apparaît pendant la transition et ne contient que l'élément partagé.

Cette couche est déclenchée lorsque l'image dans la grille est cliquée. Elle reçoit des informations sur l'élément partagé, telles que sa position et sa taille, à la fois de l'écran Grille et de l'écran Détails.

![Image](https://cdn-media-1.freecodecamp.org/images/pcenEA9bbx0zTzDUENkZcqOMExDp-5kM5S7x)

#### Étape 3 : Animation dans la couche de transition

Nous avons les informations dans la couche de transition sur la position source et de destination de l'élément partagé. Nous devons simplement les animer.

Commençons par définir l'élément en fonction de la position et de la taille de la source, puis animons-le vers l'emplacement de destination. Cela peut être fait de deux manières. Regardons les deux.

#### En interpolant sur la largeur, la hauteur, le haut et la gauche

C'est une approche directe. Si nous voulons qu'un élément change d'une taille à une autre, et d'une position à une autre, nous modifions les propriétés de style de largeur, hauteur, haut et gauche de l'élément.

![Image](https://cdn-media-1.freecodecamp.org/images/eOQgovymgQ41um3qq6l6beKw6WCGQvauibKR)

Et voici à quoi cela ressemble :

![Image](https://cdn-media-1.freecodecamp.org/images/q7yNP2uN-IAHdH9mayvgoObVAQtGZuZ8JkgE)

### **Analyse des performances**

Lorsque nous utilisons Animated, nous déclarons un graphe de nœuds qui représentent les animations que nous voulons effectuer, puis nous utilisons un pilote pour mettre à jour une valeur Animated en utilisant une courbe prédéfinie.

Voici une ventilation des étapes pour une animation et où cela se produit :

![Image](https://cdn-media-1.freecodecamp.org/images/dRi4Q2MoujdxMhx3lhc1xuOxT76QlfrYfwvw)
_[https://facebook.github.io/react-native/blog/2017/02/14/using-native-driver-for-animated.html](https://facebook.github.io/react-native/blog/2017/02/14/using-native-driver-for-animated.html" rel="noopener" target="_blank" title=")_

* JavaScript : Le pilote d'animation utilise `requestAnimationFrame` pour s'exécuter à chaque frame et mettre à jour la valeur qu'il pilote en utilisant la nouvelle valeur qu'il calcule en fonction de la courbe d'animation.
* JavaScript : Les valeurs intermédiaires sont calculées et passées à un nœud de props qui est attaché à une `View`.
* JavaScript : La `View` est mise à jour en utilisant `setNativeProps`.
* Pont JavaScript vers Native.
* Native : La `UIView` ou `android.View` est mise à jour.

Comme vous pouvez le voir, la plupart du travail se fait sur le thread JavaScript. Si celui-ci est bloqué, l'animation sautera des frames. Il doit également passer par le pont JavaScript vers Native à chaque frame pour mettre à jour les vues natives.

Ce problème peut être résolu en utilisant `useNativeDriver`. Cela déplace toutes ces étapes vers le natif.

Puisque Animated produit un graphe de nœuds animés, il peut être sérialisé et envoyé au natif une seule fois lorsque l'animation commence. Cela élimine le besoin de rappeler le thread JavaScript. Le code natif peut prendre en charge la mise à jour des vues directement sur le thread UI à chaque frame.

La principale limitation est que nous ne pouvons animer que les propriétés non liées à la mise en page. Des choses comme `transform` et `opacity` fonctionneront, mais les propriétés de flexbox et de position comme celles utilisées ci-dessus ne fonctionneront pas.

#### Interpolation sur la transformation et utilisation de useNativeDriver

Animons maintenant en utilisant la transformation. Cela nécessitera quelques calculs pour déterminer l'échelle, la position x et y.

Avec cette implémentation, si nous redimensionnons d'une image plus petite à une plus grande, l'image se pixelisera. Nous allons donc rendre l'image plus grande, puis la redimensionner à sa taille de départ, puis l'animer jusqu'à la taille naturelle.

Nous pouvons obtenir la valeur d'échelle de départ avec une ligne de JavaScript comme celle-ci :

```
openingScale = sourceDimension.width / destinationDimension.width;
```

![Image](https://cdn-media-1.freecodecamp.org/images/Uu8Zc1iNN--BSiIfdCTqojt0luL8BHAR-egU)

Vous voyez que l'image redimensionnée et l'image originale ne se ressemblent pas, car le rapport d'aspect de l'image source et de l'image de destination sont différents. Pour résoudre cela, nous allons rendre l'image avec le rapport d'aspect source basé sur la dimension de destination.

```
const sourceAspectRatio = source.width / source.height;const destAspectRatio = destination.width / destination.height;
```

```
if (aspectRatio - destAspectRatio > 0) {  // Image paysage  const newWidth = aspectRatio * destination.height;  openingScale = source.width / newWidth;} else {  // Image portrait  const newHeight = destination.width / aspectRatio;  openingScale = source.height / newHeight;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/tBaj-bwjbgJF7fAMylwSI6UV8uYAb1N1iKWq)

Maintenant que l'échelle est correcte, nous devons obtenir la nouvelle position basée sur l'image de destination. Cela peut être calculé par la position de destination moins la moitié de la différence entre l'ancienne dimension et la nouvelle dimension. Ce qui équivaudrait à :

```
if (aspectRatio - destAspectRatio > 0) {  // Image paysage  destination.pageX -= (newWidth - destinationWidth) / 2;} else {  // Image portrait  destination.pageY -= (newHeight - destinationHeight) / 2;}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1yeIZSVuZHDO1iz1MEvCKNjuATAg4V6Rhg6F)

C'est parfait ! Nous avons maintenant la bonne dimension et position pour l'image en transition.

Maintenant, nous devons calculer la position de translation à partir de laquelle animer l'image. Nous allons redimensionner l'image à partir du centre, nous devons donc appliquer notre translation en considérant que nous déplaçons simplement le centre de la photo. Nous allons donc faire quelques calculs relativement simples, en prenant la position source plus la moitié de la dimension source. Cela équivaudrait à ceci :

```
const translateInitX = source.pageX + source.width / 2;const translateInitY = source.pageY + source.height / 2;
```

```
const translateDestX = destination.pageX + destination.width / 2;const translateDestY = destination.pageY + destination.height / 2;
```

Nous pouvons maintenant calculer la position de translation par la différence entre le centre de l'image source et l'image de destination

```
const openingInitTranslateX = translateInitX - translateDestX;const openingInitTranslateY = translateInitY - translateDestY;
```

Avec ces valeurs d'échelle et de translation de départ trouvées, nous pouvons animer en utilisant l'API `Animated`.

![Image](https://cdn-media-1.freecodecamp.org/images/hOkwzd1c6IZMipdXM8CIb-uweTyeyi5Ayfxr)

![Image](https://cdn-media-1.freecodecamp.org/images/fBxxGcefWRGBUWg79GrsjQ-skEesabpXAyqF)

C'est tout. Nous avons maintenant une transition qui fonctionne. Nous pouvons maintenant utiliser `useNativeDriver` puisque nous animons uniquement des propriétés non liées à la mise en page.

#### Étape 4 : Masquer l'image source et de destination pendant la transition

Dans le gif précédent, nous avons vu que pendant la transition, l'image cliquée était toujours à la même position, et l'image de destination est apparue avant que la transition ne soit terminée.

Masquons l'image source et de destination pendant la transition, afin qu'il semble que l'image cliquée soit celle qui s'anime vers l'écran de détail.

![Image](https://cdn-media-1.freecodecamp.org/images/WYts4q5v-eE1cKe0LdmknhyqSWRjlMSMl-lU)

![Image](https://cdn-media-1.freecodecamp.org/images/d274Oc2ajmFOkxqMYrZ5j8prjGX8wpDOkte4)

Regardons maintenant le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/MMgWH7b2mCuu3dHlRiVaYARZw3qxVNANjjQz)

#### Étape 5 : Gérer le bouton retour

Pendant la transition vers l'écran de détail en utilisant `Animated.timing()`, nous changeons la `AnimatedValue` de 0 à 1. Donc, lorsque le bouton retour est cliqué, nous devons simplement changer la `AnimatedValue` de 1 à 0.

![Image](https://cdn-media-1.freecodecamp.org/images/Sv5VtAXjEHDtjBkMmesIIig4aBpyUvL0Db0r)

![Image](https://cdn-media-1.freecodecamp.org/images/n-zn4mWQDo3SblEHj9gfUQwk5pVq5rwwcrty)

C'est tout. Vous pouvez consulter le code sur [GitHub](https://github.com/narendrashetty/photo-gallery-RN) et essayer la démo sur [Expo](https://expo.io/@narendrashetty/photo-gallery).

[**narendrashetty/photo-gallery-RN**](https://github.com/narendrashetty/photo-gallery-RN)
[_Contribuez au développement de photo-gallery-RN en créant un compte sur GitHub._github.com](https://github.com/narendrashetty/photo-gallery-RN)[**photo-gallery sur Expo**](https://expo.io/@narendrashetty/photo-gallery)
[_Un nouveau projet vide_expo.io](https://expo.io/@narendrashetty/photo-gallery)

Consultez également la [diffusion d'Eric Vicenti](https://www.freecodecamp.org/news/shared-element-transition-with-react-native-159f8bc37f50/undefined) sur la [transition d'élément partagé](https://www.twitch.tv/ericvicenti).

Merci d'avoir pris le temps de lire cet article. Si vous l'avez trouvé utile, applaudissez et partagez-le. Vous pouvez me suivre sur Twitter [@narendra_shetty](https://twitter.com/narendra_shetty).