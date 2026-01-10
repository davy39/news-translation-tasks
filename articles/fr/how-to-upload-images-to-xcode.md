---
title: Comment télécharger des images vers Xcode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-01T06:54:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-upload-images-to-xcode
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca08f740569d1a4ca4969.jpg
tags:
- name: Swift
  slug: swift
- name: Xcode
  slug: xcode
seo_title: Comment télécharger des images vers Xcode
seo_desc: 'By Ai-Lyn Tang

  To use images in Xcode, you need to upload them to Assets.xcassets, located in the
  Supporting Files folder. There are two options you can go with: bitmaps (aka .png
  files) or vectors (aka .pdf files). The first step is deciding which f...'
---

Par Ai-Lyn Tang

Pour utiliser des images dans Xcode, vous devez les télécharger dans `Assets.xcassets`, situé dans le dossier `Supporting Files`. Il existe deux options : les bitmaps (c'est-à-dire les fichiers `.png`) ou les vecteurs (c'est-à-dire les fichiers `.pdf`). La première étape consiste à décider quel type de fichier vous souhaitez utiliser.

# La différence entre les bitmaps et les actifs vectoriels

La plupart des tutoriels en ligne utilisent des actifs bitmap, qui sont des fichiers `.png`. Cela nécessite de glisser-déposer 3 copies de l'image dans Xcode.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_PP9k-oGBon0-R_1XW3DHjg.png)
_Glissez et déposez les trois copies de vos images .png ici_

Cependant, il existe une école de pensée qui croit que les actifs vectoriels sont supérieurs. [Cet article](https://support.goanimate.com/hc/en-us/articles/203029524-Vector-vs-Bitmap-Images-How-to-Get-The-Best-Results-in-GoAnimate) offre une excellente explication de pourquoi c'est le cas. Les actifs vectoriels sont des fichiers `.svg` (ou `.pdf` pour Xcode). Si vous choisissez d'utiliser des actifs vectoriels, vous n'avez besoin de télécharger qu'une seule version de l'image dans Xcode.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_05iKsfSZqTVZh8w3t8ZWFA.png)
_Glissez et déposez votre fichier .pdf ici_

Voici ce que j'ai entendu de la part de ceux qui sont beaucoup plus sages que moi : les téléphones Android utilisent des algorithmes à partir de l'actif vectoriel pour générer l'image dans n'importe quelle taille requise. Cela a du sens étant donné la large gamme de dispositifs et de tailles d'écran pour Android.

Cependant, les actifs vectoriels dans les iPhones ne s'adaptent pas réellement avec des algorithmes (apparemment). Vous n'obtenez donc pas des images de meilleure qualité en utilisant des vecteurs plutôt que des bitmaps. Au lieu de cela, vous obtenez la même qualité que les bitmaps. L'iPhone prend simplement l'actif "vectoriel" et le convertit en trois tailles de bitmap.

Outre la logique algorithmique ci-dessus, il existe quelques autres avantages objectifs à utiliser des actifs vectoriels pour les iPhones.

1. **Réduit la probabilité d'erreur humaine.** Actuellement, il existe trois tailles de bitmap (1x, 2x, 3x). Cela signifie que vous devez télécharger trois images dans vos actifs. Cela représente trois occasions de glisser-déposer accidentellement la mauvaise image. Lorsque vous utilisez des actifs vectoriels (qui apparaissent comme universels dans Xcode), vous n'avez besoin de télécharger qu'une seule image au lieu de trois. Il y a moins de risques de télécharger la mauvaise taille ou image.
2. **Vitesse.** Même raison que #1. Si vous utilisez beaucoup d'images dans votre application, l'utilisation d'actifs vectoriels réduit le nombre d'images que vous devez télécharger d'un tiers.
3. **Preuve pour l'avenir.** L'iPhone utilise actuellement seulement trois tailles d'image (1x, 2x, 3x). Cela est lié à la qualité rétina accrue des écrans. Lorsque Apple a introduit les écrans rétina haute résolution il y a quelques années, le nombre de pixels par point a augmenté pour une image plus nette. 
Il semble extrêmement probable que des augmentations technologiques similaires continueront de se produire. À l'avenir, nous pourrions avoir besoin de télécharger des images 4x, 5x et 6x. Si nous utilisons un actif vectoriel, l'application redimensionnera l'image pour nous. Cela nous évite d'ajouter les nouvelles tailles de l'actif bitmap. 
Bien que je doive admettre que je suis un peu confus à ce sujet, étant donné que les actifs vectoriels de l'iPhone ne semblent pas réellement fonctionner avec des algorithmes. Je ne suis donc pas sûr de la manière dont ils s'adapteront automatiquement à des tailles plus grandes. Mais mon mentor sage m'a expliqué cela et je lui fais confiance !

Le seul grand inconvénient de l'utilisation d'actifs vectoriels dans Xcode est que la plupart des endroits ne fournissent pas le fichier `.pdf`. Vous devez le convertir vous-même à partir de `.svg`.

_Mise à jour du 18 juin 2017_ : Apple a annoncé lors de la WWDC que iOS supporte désormais les images scalaires vraies ! Ou du moins, c'est ce que je pense qu'ils ont annoncé. Maintenant, il y a encore plus de raisons d'utiliser une seule échelle.

# Comment télécharger un actif vectoriel

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_L-LclRKD3SRLmhnjbG1d2w.png)
_Options pour télécharger un actif vectoriel_

Rendez-vous dans le menu des attributs. Changez les échelles en "échelle unique", et cochez la case de redimensionnement pour "conserver les données vectorielles". Cela changera l'option de téléchargement en "toutes" au lieu de 1x, 2x, 3x.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_05iKsfSZqTVZh8w3t8ZWFA-1.png)
_Glissez et déposez votre fichier .pdf ici_

Ensuite, vous glissez et déposez votre fichier `.pdf` dans l'unique emplacement. Je ne suis pas encore tout à fait sûr de la manière de convertir `.svg` en `.pdf`, mais j'imagine que c'est assez facile avec Preview.

# Comment télécharger des fichiers .png

Si vous décidez d'utiliser `.png`, vous devrez télécharger trois versions de votre fichier. Cela permet de couvrir les différentes résolutions d'écran des différents iPhones.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_GnT-kK2SC9E42YsI2k13EQ.png)
_Options pour les actifs bitmap_

Tout d'abord, assurez-vous que l'option "échelles" dans le menu des attributs est définie sur "échelles individuelles". Il s'agit de l'option par défaut, et elle vous montrera trois emplacements que vous devez remplir :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_05iKsfSZqTVZh8w3t8ZWFA-2.png)
_Glissez et déposez vos trois copies de votre image ici_

Ensuite, trouvez une image que vous souhaitez utiliser dans votre application. Supposons qu'il s'agit de [cette icône](https://www.flaticon.com/free-icon/stones_1209405#term=zen&page=1&position=25) :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_fxICo0KKb-KBcfmpOYPuuA.png)
_Icônes d'une tour de trois pierres et d'une bougie_

Wow, c'est grand. C'est parce que j'ai téléchargé la version 512 pixels du site. Cependant, je veux que l'image soit de 20 x 20 pixels dans mon application. Pour convertir l'image en 20 pixels, je vais la redimensionner dans Preview.

Faites trois copies de l'image originale. Les noms de votre image doivent ressembler à ceci : `zen.png`, `zen@2x.png`, `zen@3x.png`. L'important est que les fichiers aient tous le même nom (ici j'utilise `zen`), et que deux d'entre eux se terminent par `@2x` et `@3x`. Lorsque vous utilisez cette convention de nommage, Xcode pourra automatiquement trouver la taille correcte en fonction du type de dispositif.

Ensuite, ouvrez l'image dans Preview et allez dans Outils > Ajuster la taille pour faire apparaître le menu ci-dessous. Spécifiez 20 x 20 pixels. Appuyez sur OK et enregistrez la modification. Il s'agit de votre image de base, `zen.png`.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_zi8aQZLqJkeerb2OgVETbg.png)

Faites la même chose pour `zen@2x.png`. Seulement, celle-ci doit être de 40 x 40 pixels. Une fois de plus pour `zen@3x.png`. Celle-ci sera de 60 x 60 pixels.

Maintenant, vous pouvez glisser et déposer les images dans les cases correctes dans Xcode. C'est fait !