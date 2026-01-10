---
title: Qu'est-ce que l'AVIF ? Comment utiliser les images au format AV1 sur votre
  site web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T18:14:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-avif-images-on-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/how-to-start-using-images-on-your-webistes-1.png
tags:
- name: 'image optimization '
  slug: image-optimization
seo_title: Qu'est-ce que l'AVIF ? Comment utiliser les images au format AV1 sur votre
  site web
seo_desc: 'By Erisan Olasheni

  The AV1 Image format, or AVIF, is the latest image codec on earth. AVIF is an optimized
  image format which was created to make our images smaller while keeping the same
  quality (lossless). The file extension for AVIF is .avif.

  In t...'
---

Par Erisan Olasheni

Le format d'image AV1, ou AVIF, est le dernier codec d'image sur terre. AVIF est un format d'image optimisé qui a été créé pour rendre nos images plus petites tout en conservant la même qualité (sans perte). L'extension de fichier pour AVIF est `.avif`.

Dans cet article, je veux parler de ses fonctionnalités et de ses avantages, et pourquoi vous devriez commencer à utiliser AVIF. Je vais également vous montrer comment inclure en toute sécurité des images AVIF sur votre site web. 

## Qu'est-ce que l'AVIF et comment fonctionne-t-il ?

AVIF est une extraction des images clés du format vidéo désormais populaire [AV1](https://en.wikipedia.org/wiki/AV1) développé par [Alliance for Open Media (AOM)](http://aomedia.org/). 

AOM a développé AVIF dans le but de fournir des images libres de droits avec une meilleure efficacité de compression et une prise en charge de plus de fonctionnalités par rapport aux formats d'image existants. 

AVIF compte désormais des soutiens de grandes entreprises comme Google, Netflix et Apple. 


## Pourquoi l'AVIF est-il meilleur ?

Suivant ses prédécesseurs (**WebP**, **JPEG-XR**, **JPEG2000**, et **PNG**, **GIF**), AVIF est compatible avec l'imagerie à haute gamme dynamique. Il prend en charge les couleurs **10-** et **12-bit** en pleine résolution, ce qui permet d'obtenir des images jusqu'à 10 fois plus petites que les autres formats connus. 

AVIF est un bon choix pour les développeurs web car :

*   Il est libre de droits, vous pouvez donc l'utiliser gratuitement sans vous soucier des licences.
*   Il est actuellement soutenu par de nombreux grands acteurs de la technologie comme Google, Amazon, Netflix, Microsoft, et plus encore.
*   Il offre la compression la plus optimale.
*   Il dispose de plus de fonctionnalités modernes comme la transparence, le HDR, une large gamme de couleurs, et plus encore.


## Comment commencer à utiliser les images AVIF

Nous arrivons maintenant à la partie amusante de ce tutoriel. Il existe deux principales façons de commencer à utiliser les images AVIF :

1. La première consiste à convertir vos anciennes images en AVIF.
2. La seconde consiste à créer des images AVIF à l'aide d'éditeurs d'images prenant en charge l'AVIF.


### Comment convertir vos anciennes images en AVIF

Étant donné que l'AVIF est encore en phase de développement, le moyen le plus simple de créer des images au format AVIF est de convertir vos anciens formats. 

Cela peut être fait simplement en ligne, car il existe de nombreux convertisseurs d'images AVIF en ligne. Le [convertisseur AVIF en ligne](https://avif-converter.online/) est mon choix car il est plus simple et semble être le convertisseur en ligne le plus rapide disponible. 

Suivez simplement ces étapes pour convertir vos images en AVIF :

1. Visitez [le site web](https://avif-converter.online/).
2. Téléchargez vos anciennes images (peuvent être **PNG**, **JPEG**, **GIF** et autres).
3. Attendez que le site web traite la conversion.
4. Enregistrez vos nouveaux fichiers AVIF.


### Comment créer des images AVIF à l'aide d'éditeurs d'images prenant en charge l'AVIF

Les éditeurs d'images ajoutent la prise en charge de la création d'images AVIF. Ces éditeurs prennent désormais entièrement en charge les images AVIF :


*   Microsoft Paint – à partir des mises à jour ["19H1"](https://www.howto-connect.com/windows-10-1903-version-support-avif-file-type/), vous pouvez maintenant dessiner des images sur Microsoft Paint et les enregistrer en tant qu'AVIF.
*   GIMP pour Windows et Linux prend désormais en charge AVIF à partir de [la mise à jour 2.10.22](https://www.ghacks.net/2020/10/09/gimp-2-10-22-update-introduces-support-avif-and-heic-support/).
*   Les développeurs de Photoshop parlent également [de la manière de prendre en charge AVIF](https://feedback.photoshop.com/conversations/photoshop/when-will-avif-support-be-added-to-photoshop/5f5f46314b561a3d4278baf4). Espérons que cela sera bientôt pris en charge.


## Comment utiliser l'AVIF sur votre site web

AVIF est encore une technologie relativement nouvelle. Mais la plupart des navigateurs modernes prennent désormais en charge le format, ce qui signifie que vous pouvez l'utiliser directement dans la balise `<img>`. Gardez simplement à l'esprit que tous les navigateurs ne prennent pas encore entièrement en charge le format. 

La meilleure façon d'utiliser AVIF est avec la **négociation de contenu**. Nous allons utiliser le `<picture>` HTML 5 et le `<source>` qui prend en charge la négociation de contenu.

![Group-9how-to-use-avif-html--1-](https://www.freecodecamp.org/news/content/images/2020/11/Group-9how-to-use-avif-html--1-.png)

Vous pouvez essayer [l'exemple en direct ici](https://lyty.dev/diy/how-to-use-avif-on-website.html).


### Quels navigateurs prennent en charge l'AVIF

*   Le premier navigateur à prendre entièrement en charge AVIF est [Chrome 85](https://developers.google.com/web/updates/2020/08/nic85#more). 
*   Microsoft [Windows 10](https://www.howto-connect.com/windows-10-1903-version-support-avif-file-type/) a également ajouté la prise en charge dans les mises à jour "19H1".
*   Mozilla travaille toujours sur la prise en charge du format d'image dans Firefox.[155].


## Conclusion
AVIF est un changement de jeu qui deviendra bientôt le format d'image de facto dans le monde. Grâce à ses fonctionnalités potentielles, il est probable qu'il obtiendra bientôt une prise en charge complète sur toutes les plateformes. 

Contrairement à l'image **WebP** de Google, qui a pris 10 ans à Apple pour être prise en charge, AVIF a rapidement attiré l'intérêt d'Apple au point qu'ils contribuent désormais au projet. 

Êtes-vous prêt à commencer à utiliser AVIF sur vos sites web ?