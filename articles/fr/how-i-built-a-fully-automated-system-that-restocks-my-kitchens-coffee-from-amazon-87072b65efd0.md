---
title: Comment j'ai construit un système entièrement automatisé qui réapprovisionne
  mon café de cuisine depuis Amazon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-28T23:59:46.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-fully-automated-system-that-restocks-my-kitchens-coffee-from-amazon-87072b65efd0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0CIKiBzkfud1zF3g9btnQQ.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: Raspberry Pi
  slug: raspberry-pi
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment j'ai construit un système entièrement automatisé qui réapprovisionne
  mon café de cuisine depuis Amazon
seo_desc: 'By Terren Peterson

  I’ve perfected a method over the years for preparing for a grocery store run. I
  carefully open up the fridge and scan through it several times, letting out most
  of the cold air.


  I then do a similar exercise with a few other cabine...'
---

Par Terren Peterson

Au fil des ans, j'ai perfectionné une méthode pour préparer une course à l'épicerie. J'ouvre soigneusement le réfrigérateur et le scanne plusieurs fois, laissant sortir la plupart de l'air froid.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BhwVxeex2ZzHlnyFkQOhNw.jpeg)

Je fais ensuite un exercice similaire avec quelques autres armoires de la cuisine. Ensuite, je griffonne tous les articles dont j'ai besoin sur un morceau de papier.

Bien que j'aie essayé différentes applications mobiles dans un effort pour m'organiser davantage, je n'ai pas encore amélioré cette méthode simple sur papier.

Étant donné que j'adore la technologie, je suis convaincu qu'il existe une meilleure façon de remplir mes étagères, mais je n'ai pas encore vu la bonne solution. J'aime la commodité des achats en ligne sur Amazon, mais il y a encore un délai dans l'exécution qui nécessite plus de planification que je ne suis capable de faire.

C'est alors que j'ai commencé à réfléchir : peut-être que la solution réside dans une meilleure surveillance des stocks. Et c'est dans cette direction que je me suis engagé.

Puisque ma famille consomme beaucoup de café, et qu'il y a une grande sélection disponible en ligne, j'ai décidé de commencer par là.

Dans le cadre d'un concours [Hackster](https://www.freecodecamp.org/news/how-i-built-a-fully-automated-system-that-restocks-my-kitchens-coffee-from-amazon-87072b65efd0/undefined), j'ai été vraiment motivé à passer de ce concept au code, et à automatiser entièrement l'exécution de mon approvisionnement en grains de café directement à mon domicile. Une description détaillée de ma solution complète peut être trouvée [ici](https://www.hackster.io/terren/javawatch-your-coffee-bean-guardian-807ef7), avec un résumé ci-dessous.

### Service de réapprovisionnement Amazon Dash

L'un des nombreux nouveaux produits technologiques qu'Amazon a lancés s'appelle Dash. Voici une image d'un modèle programmable appelé Dash Button, et ils vendent également des modèles déjà configurés pour commander des produits sur leur site web, comme du détergent, des piles, des chips, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6-jdNVlWrhEY7PzANef-Cw.png)

La même technologie qui équipe ces boutons peut être intégrée nativement dans du matériel. Cela permet de remplacer un bouton par d'autres stimuli qui peuvent demander qu'un produit soit commandé. Après une séance de brainstorming, voici l'idée que j'ai développée.

### Comment faire fonctionner le tout

Après avoir trouvé un nom accrocheur et un concept créatif, j'ai esquissé une architecture sur la façon dont cela allait fonctionner. Entre le dispositif matériel basé sur Raspberry Pi et les API de réapprovisionnement Dash, j'ai ajouté le [Service Amazon Rekognition](https://aws.amazon.com/rekognition/) qui a été lancé il y a quelques mois. Voici comment toutes les pièces s'emboîtent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FiHh8kf3et_s0kpOKfEcgQ.png)

### Tirer parti de l'intelligence artificielle dans la cuisine

La clé pour maintenir l'approvisionnement en grains de café résidait dans l'utilisation des capacités de reconnaissance d'images d'AWS. J'ai vu quelques excellents cas d'utilisation de cette technologie pour la reconnaissance faciale, mais peut-être suis-je le premier à prendre des photos de grains de café.

Le service était simple à mettre en œuvre. La caméra Raspberry Pi capture et télécharge des photos à des intervalles prédéfinis vers le service de stockage basé sur des objets d'AWS appelé S3. Chaque objet photo obtient une adresse unique, et un appel à l'API Rekognition est effectué en passant cette adresse afin que l'IA puisse être appliquée. Par exemple, voici une photo réelle prise par l'appareil d'un bocal plein de grains.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HGR6Ouwr6SsxCO4_5-jnCQ.jpeg)

Ce qui revient dans la réponse est un tableau d'étiquettes  pensez à celles-ci comme des prédictions sur ce qui se trouve dans le champ de vision de l'image.

```
{    "Labels": [        { "Confidence": 84.64501190185547, "Name": "Bottle" },        { "Confidence": 84.64501190185547, "Name": "Jug" },        { "Confidence": 84.64501190185547, "Name": "Water Bottle" },        { "Confidence": 80.86704254150390, "Name": "Jar" },        { "Confidence": 73.33070373535156, "Name": "Bean" },        { "Confidence": 73.33070373535156, "Name": "Produce" },        { "Confidence": 73.33070373535156, "Name": "Vegetable" }    ],    "OrientationCorrection": "ROTATE_0"}
```

J'ai eu de la chance que l'IA enregistre une étiquette "Bean", et dans cette photo, elle a prédit avec une certitude de 73 % qu'il s'agissait dans l'image. Elle est également revenue avec de nombreuses autres assertions qui étaient correctes (oui, c'est aussi une bouteille, et pourrait être un produit ?) mais qui ne sont pas pertinentes pour ce que je cherche.

Alors, que se passe-t-il lorsque la réserve de grains de café est presque vide ? Voici l'image que le Raspberry Pi a capturée dans ma cuisine lorsque cela s'est produit.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y39h4fIrhvZvEXHduRhEVA.jpeg)

Et voici les étiquettes que l'IA a renvoyées en réponse.

```
{    "Labels": [        { "Confidence": 94.05787658691406, "Name": "Bottle" },        { "Confidence": 94.05787658691406, "Name": "Jug" },        { "Confidence": 94.05787658691406, "Name": "Water Bottle" },        { "Confidence": 80.77616882324219, "Name": "Jar" },        { "Confidence": 63.5648078918457, "Name": "Alcohol" },        { "Confidence": 63.5648078918457, "Name": "Beer" },        { "Confidence": 63.5648078918457, "Name": "Beer Bottle" },        { "Confidence": 63.5648078918457, "Name": "Beverage" },        { "Confidence": 63.5648078918457, "Name": "Drink" }    ],    "OrientationCorrection": "ROTATE_0"}
```

Ça a marché ! Les grains avaient disparu du champ de vision et n'apparaissaient plus dans le tableau. En analysant le tableau, j'ai obtenu suffisamment de détails pour pouvoir prendre une décision de commande afin de remplir à nouveau le bocal.

### Quel café Amazon devrait-il envoyer ?

Déterminer quel café Amazon devrait livrer était une tâche distincte, et nécessitait la mise en place d'un site web simple qui permet l'enregistrement d'un appareil avec Amazon. Ci-dessous se trouve une courte vidéo qui montre quelques captures d'écran de ce à quoi ressemble le [site](http://javawatcher.com/), et comment il s'intègre au catalogue de produits Amazon.

### Pourrait-il fonctionner pour d'autres articles ?

Une fois que j'ai fait fonctionner les choses, je les ai testées sur quelques autres articles pour voir à quel point l'IA était performante dans la cuisine.

Ketchup (énorme succès  reconnaissance à 98,6 %).

Sriracha (échec  73,1 % de probabilité qu'il s'agisse d'une boisson).

Fraises (un autre succès  reconnaissance à 85,4 %).

Myrtilles (échec partiel  la plus proche était la reconnaissance de "Nourriture" à 61,7 %).

Œufs  vue de dessus de la boîte (échec total  51,6 % de probabilité qu'il s'agisse d'un pare-chocs de voiture).

Il reste donc encore du travail pour entraîner les modèles, mais c'est un bon début et il semble raisonnable que cela ne soit pas spécifique aux grains de café.

### Qu'est-ce qui suit ?

Après avoir travaillé dessus pendant un certain temps, j'ai déterminé que j'avais peut-être trop compliqué la solution. Bien que j'adore construire avec des Raspberry Pi, la prochaine étape en termes d'expérience utilisateur est de développer cela sous forme d'application sur smartphones, en tirant parti des capacités de caméra déjà disponibles dans les poches des consommateurs.

Rendre la solution totalement portable serait une énorme victoire et élimine le coût de construction et tout composant matériel. La plupart du travail dans la solution est déjà alimenté dans le Cloud, il s'agit donc simplement de savoir comment obtenir des photos à partir de celui-ci. Le service Rekognition n'a que quelques mois, et si l'amélioration de ses modèles encourageait les achats sur Amazon.com, je parierais qu'il s'améliorerait rapidement !