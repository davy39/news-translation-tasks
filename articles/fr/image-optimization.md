---
title: Une introduction de base à l'optimisation des images pour le Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-30T07:00:00.000Z'
originalURL: https://freecodecamp.org/news/image-optimization
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/image-breakpoints-2.png
tags:
- name: 'image optimization '
  slug: image-optimization
- name: Web Development
  slug: web-development
- name: web performance
  slug: web-performance
seo_title: Une introduction de base à l'optimisation des images pour le Web
seo_desc: 'By Anton Garcia Diaz

  Images are an essential ingredient of most websites. The visual quality of pictures
  has a direct impact on the brand image and the message those images convey. And
  the weight of images usually accounts for a 40-60% of the data tr...'
---

Par Anton Garcia Diaz

Les images sont un ingrédient essentiel de la plupart des sites web. La qualité visuelle des images a un impact direct sur l'image de marque et le message que ces images transmettent. Et le poids des images représente généralement 40 à 60 % des données transférées sur le web. 

Cela a généralement le plus grand impact sur le temps de chargement par rapport à d'autres ressources comme JavaScript. Ainsi, que nous créions ou gérions un site web, nous devrions mettre en place un pipeline de transformation et d'optimisation des images.

Il existe de nombreuses options pour cela, allant des développements internes basés sur des bibliothèques et suites open source – comme ImageMagick – aux outils et API basés sur le cloud. 

Quel que soit l'outil que nous utilisons dans notre déploiement, il y a quatre tâches principales que, au minimum, tout pipeline devrait accomplir.

### Redimensionner les images. 

Le redimensionnement des images est la première et la plus importante étape. Il a un grand impact sur le poids sans pénalité sur la qualité visuelle, tant que nous ne le rendons pas plus petit que la résolution d'affichage. 

Nous devrions toujours définir et appliquer une résolution maximale d'image sur notre site web, par exemple 2000 px de largeur. Idéalement, nous rendrions notre site web réactif en définissant différents points de rupture et en livrant des images qui s'adaptent aux écrans de nos utilisateurs. 

Si vous avez besoin d'aide pour choisir vos points de rupture, consultez cet article sur les [meilleures tailles d'image pour le web](https://abraia.me/docs/best-image-sizes-for-web/).

### Convertir au bon format. 

Le JPEG est le format par défaut sur le web. Le PNG peut mieux fonctionner avec des designs graphiques présentant des couleurs solides, mais dans ces cas, il peut donner un poids inférieur avec une meilleure qualité. 

Vous pouvez envisager d'offrir le WEBP pour les utilisateurs de Chrome, Edge, Firefox et Android, en gardant le JPEG comme solution de repli pour Safari et iOS. Cela peut économiser 10 à 30 % du poids de l'image avec une qualité très similaire, peut-être un peu plus de flou et moins de ringing. 

Pour une révision à jour, vous pouvez consulter cet article sur les [formats d'image pour le web](https://abraia.me/docs/best-image-formats-for-web/).

### Compresser correctement les images. 

Nous pouvons le faire avec une suite open source puissante comme [ImageMagick](https://imagemagick.org/index.php) et simplement définir un facteur de qualité (généralement 75 à 85) pour les images JPEG (et WEBP). Vous pouvez toujours utiliser une métrique perceptuelle pour mieux protéger la qualité et réduire davantage le poids – cette option est disponible dans certains outils d'optimisation d'image basés sur le cloud [image optimization tools](https://abraia.me/docs/image-optimization/#automatic-image-optimization-for-web).

### Se débarrasser des métadonnées. 

De la prise de vue à l'édition, les images accumulent des métadonnées, comme les [données exif](https://abraia.me/docs/exif-data-orientation/). Bien qu'elles puissent être utiles pour l'édition et la gestion, elles n'ont aucun impact sur la manière dont les images s'affichent sur notre site web. Leur poids peut facilement atteindre 20 Ko ou plus par image. 

Nous devrions nous débarrasser des métadonnées avant de publier sur le web. Nous devons simplement nous assurer que les images sont codées avec la bonne orientation et avec un profil sRGB, en adhérant aux bonnes pratiques de [gestion des couleurs](https://abraia.me/docs/color-management-for-web/).