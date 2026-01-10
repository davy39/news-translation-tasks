---
title: Visualisation de données avec 1 milliard de reconnaissances musicales Shazam
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-18T13:28:29.000Z'
originalURL: https://freecodecamp.org/news/data-visualisation-with-1-billion-shazam-music-recognitions-90728df3a8c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZQmAY-kW0ihq1d8bRG3UFA.png
tags:
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Visualisation de données avec 1 milliard de reconnaissances musicales Shazam
seo_desc: 'By Umar Hansa

  While at university, I joined Shazam as part time web developer. I stayed at Shazam
  for 5 enjoyable years. This post is about one hackday project I worked on. The project
  involves plotting one billion Shazam recognitions onto a blank ca...'
---

Par Umar Hansa

Pendant mes études universitaires, j'ai rejoint Shazam en tant que développeur web à temps partiel. Je suis resté chez Shazam pendant 5 années agréables. Cet article parle d'un projet sur lequel j'ai travaillé lors d'un [hackday](https://en.wikipedia.org/wiki/Hackathon). Le projet consiste à tracer un milliard de reconnaissances Shazam sur une toile vierge, puis à observer le résultat.

Cet article aborde également le processus que j'ai utilisé pour créer les visuels.

### Qu'est-ce qu'une « reconnaissance Shazam »

Imaginez une reconnaissance Shazam comme ceci. Vous ouvrez Shazam, l'application mobile, et la faites « écouter » un morceau de musique qui joue en arrière-plan. Une reconnaissance est l'identification réussie de la chanson.

### Données de localisation

Un utilisateur peut choisir de partager ses données de localisation avec Shazam. Shazam rend alors **certaines** des données de localisation **anonymisées** (latitude et longitude) disponibles pour les employés, selon leur cas d'utilisation.

Avoir des données de localisation **anonymisées** à visualiser était une expérience passionnante. Cela m'a beaucoup appris sur le traitement de grands ensembles de données, les visualisations qui racontent une histoire, et les visualisations qui sont jolies mais ne font rien d'autre.

### La visualisation

Une chose que vous devez savoir : toutes les visualisations suivent cette idée : Un point représente une reconnaissance réussie. Les points sont tracés sur un système de coordonnées géographiques. Ce n'est pas la même chose que de prendre une carte Google et d'y placer des marqueurs de localisation.

![Image](https://cdn-media-1.freecodecamp.org/images/MOPm9tBV2ZkBNkWKeoXEoqwHGEzkS4DGIoIX)

![Image](https://cdn-media-1.freecodecamp.org/images/bIXoEP7zmxx19xtyrxxrSzMmrpYRFV9aHUi2)

![Image](https://cdn-media-1.freecodecamp.org/images/hW5KfzsUta-1OTWVPYeZzZPzj2Ff-mnUsbib)

![Image](https://cdn-media-1.freecodecamp.org/images/63eDAdqvdhk63Fm28SBxqlclgApLTUVvFPzf)
_Chicago, Londres, New York, Monde entier_

![Image](https://cdn-media-1.freecodecamp.org/images/NI9UTNais5MSz5mbmF-7uUZODALTGbmixl9c)
_Zoom sur New York_

J'ai utilisé la couleur pour différencier Android et iOS. Pouvez-vous deviner lequel est lequel ? Indice : Regardez les grandes villes. Quel type d'appareil pensez-vous être prévalent là-bas ?

* **Android** : Rouge
* **iOS** : Bleu

Si vous regardez de près les cartes de points, vous pouvez remarquer des définitions claires pour les routes. Cela peut s'expliquer par les passagers qui utilisent Shazam pour identifier la musique diffusée par les haut-parleurs de la voiture.

J'ai également créé des cartes avec des schémas de couleurs alternatifs.

![Image](https://cdn-media-1.freecodecamp.org/images/kHThP5IR0N1sBQmC9mNzjaFttFYVCpylKQm2)

![Image](https://cdn-media-1.freecodecamp.org/images/PjnVi3nO44GPHKFO1WcahEfmLkkp3oAHjwN6)

![Image](https://cdn-media-1.freecodecamp.org/images/Sw-JtjFkfBUhxH5BoOAPiyaT0Vi9vj6M7NHN)

![Image](https://cdn-media-1.freecodecamp.org/images/1PKNHGtNNgbFSXIiQD4vem-HDzGddNwkcRso)
_Chicago, Los Angeles, New York, Royaume-Uni_

### Cartes interactives

J'ai pensé qu'il serait amusant de visualiser la carte de manière interactive. De la même manière que vous faites glisser/zoomez sur une carte Google, que se passerait-il si vous pouviez également faire glisser/zoomer une carte Shazam ? Cet élément d'interactivité est ce qui encourage les gens à utiliser, explorer et apprendre à partir des cartes. Plutôt que d'être simplement quelque chose de statique que vous ne revisitez jamais.

![Image](https://cdn-media-1.freecodecamp.org/images/PyjkZ9HV7MuRAxZVUyAP5ShnyZkIhCKFIWdp)

Pour ce faire, j'ai dû générer des millions de "tuiles" de carte. Par exemple, voici quelques tuiles de Londres, prises à partir de Google Maps.

![Image](https://cdn-media-1.freecodecamp.org/images/yVIpcBFTs7RTTNIHoeGPuO0u4jFwR8S7NbyY)

Chaque tuile est une image séparée. Notez les différents niveaux de zoom. Comme vous pouvez l'imaginer, lorsque vous faites glisser et zoomez sur une carte Google, elle vous présente de nombreuses images différentes, les images sont appelées tuiles de carte.

Voici les tuiles de la carte Shazam.

![Image](https://cdn-media-1.freecodecamp.org/images/pmYW9OvBxNK6f-kSjVygq6QQqDfvlTgIK478)

Au total, j'ai créé plus de 40 Go de données de tuiles. Cela est dû au niveau de zoom que j'avais spécifié. Un niveau de zoom élevé signifie que ceux qui visualisent la carte peuvent zoomer à un niveau plus élevé.

En examinant les visualisations avec des collègues, nous nous demandions constamment : Quel "endroit" se trouvait à l'emplacement des grands clusters. Par exemple, était-ce un lieu de musique où les gens utiliseraient fréquemment Shazam ?

Pour aider à répondre à cette question, j'ai eu une idée : Et si j'utilisais un service de localisation pour déterminer quels lieux sont actuellement présents. Pour ce faire, j'ai utilisé l'[API Google Maps Places](https://developers.google.com/maps/documentation/javascript/places). Chaque fois que vous faites défiler vers un nouvel emplacement, j'interroge l'API Google Maps pour poser la question : Quels lieux se trouvent dans cet emplacement ?

![Image](https://cdn-media-1.freecodecamp.org/images/-ZI1Gapw1EgoYg38K7oOq9At4j-DUiGtmbVg)

En utilisant cette fonctionnalité, nous avons commencé à réaliser que les clusters de points étaient généralement le résultat de : cafés, boîtes de nuit, centres commerciaux, magasins de proximité et autres.

J'ai également synchronisé une carte [Mapbox](https://www.mapbox.com/) (similaire à Google Maps) de sorte que lorsque vous faites glisser et zoomez dans la carte Shazam, l'autre carte "normale" se déplace également. Cela vous permet d'identifier rapidement l'emplacement géographique que vous regardez actuellement.

### Le code

Comme pour tout ce que je fais, je ne bénéficie que du travail acharné des autres dans notre communauté. Tout le crédit revient à [Eric Fischer](https://github.com/ericfischer) pour leur excellent travail sur [datamaps](https://github.com/ericfischer/datamaps). Si vous suivez les instructions de ce dépôt Github, vous serez en mesure de créer vos propres visualisations. Vous aurez besoin d'un ensemble de données constitué de points de longitude et de latitude, vous pourriez trouver quelque chose sur Github, par exemple, [awesome-public-datasets](https://github.com/caesar0301/awesome-public-datasets).

Si vous essayez de le faire : voici quelques notes que j'ai prises pour moi-même et qui pourraient vous être utiles.

Tout d'abord, vous avez besoin d'une longue liste de latitudes et de longitudes. Cependant, pour obtenir ces données, vous devrez peut-être faire un travail supplémentaire. Dans mon cas, je les ai obtenues à partir d'une API interne de Shazam. J'ai utilisé un module Node appelé [fast-csv](https://github.com/C2FO/fast-csv) pour analyser les données. L'utilisation de flux de cette manière rend l'analyse de grandes quantités de données (plusieurs gigaoctets) simple à faire.

```
csv.fromStream(stream,{headers : true}).on('data', handleRecord);
```

La fonction _handleRecord_ fait ceci :

```
function handleRecord(record) {   const location = tag.location.latitude + ',' + tag.location.longitude;   console.log(location);}
```

La sortie ressemble à ceci :

```
lat,lon
```

```
-22.1028,166.1833
```

```
29.8075,-95.4113
```

```
51.2168,-0.8045
```

```
27.3007,-82.5221
```

```
20.5743,-100.3793
```

```
-36.0451,146.9267
```

```
26.7554,-81.4237
```

À ce stade, vous pouvez commencer à l'intégrer dans les cartes de données (il y a des instructions détaillées dans la documentation du projet).

En suivant la documentation suffisamment longtemps, je suis arrivé à un point où je pouvais créer l'image finale. Pour créer une carte de données de Londres, spécifiez la boîte de délimitation en tant que coordonnées de localisation que vous souhaitez capturer :

```
./render -A -- output 14 51.641353 -0.447693 51.333508 0.260925 > london.png
```

Parce que j'ai créé les mêmes cartes statiques si souvent (lors de l'expérimentation avec les couleurs par exemple), j'ai décidé de scripter tout le processus. Étant un développeur web, j'ai tout fait en Node.js, mais un simple script Bash aurait été suffisant. Tout d'abord, j'ai fait un objet contenant toutes les cartes que je voulais rendre.

![Image](https://cdn-media-1.freecodecamp.org/images/4J0vVDjTrg5pXHXlJS5hncdA1axc1Gm2PkNv)
_Structure de données pour rendre toutes les cartes_

Ensuite, il s'agissait de construire la commande que vous avez vue précédemment, mais pour chaque entrée de localisation dans ce bloc JSON que vous voyez dans l'image ci-dessus.

### Présentation

Chez Shazam, il y avait plusieurs jours de hackathon. Ensuite, après quelques mois, il y avait un jour de démonstration. Vous présentiez votre travail de hackathon lors du jour de démonstration. Montrer ce projet particulier aux gens a été bien reçu.

Pour les développeurs créant des applications en ligne de commande ou partant à l'aventure du refactoring de code lors des jours de hackathon, considérez qu'un public de jour de démonstration peut préférer des démonstrations plus visuelles, plutôt que techniques (c'est mon expérience). Une façon de contourner cela est : bloguer sur ce que vous avez fait et partager les ressources après, en sautant une démonstration en direct entièrement. Ou encore mieux, trouvez comment distiller des concepts techniques à un public non technique, introduisez plus de visuels, et continuez à donner votre démonstration à un public en direct. C'est plus difficile, mais plus gratifiant.

### Images haute résolution des cartes de données

Remarque : Vous pouvez zoomer sur ces images avec l'interface Google Photos

* [Monde](https://photos.app.goo.gl/tIm9mmst7qU1aH242) — Remarquez quels pays/villes ont une utilisation élevée d'iOS
* [Royaume-Uni](https://photos.app.goo.gl/EEkLzfrpjKmKYm7j1) — Remarquez les villes
* [Toronto](https://photos.app.goo.gl/CQlMePnEUXHN6eqF2)
* [San Francisco](https://photos.app.goo.gl/Mnn5fcDGrUElXjCO2)
* [Paris](https://photos.app.goo.gl/IwXHWw9ve3DGufc82)

### Conclusion

Je suis reconnaissant à Shazam de nous avoir encouragés à apprendre de nouvelles compétences et technologies. Merci également à Eric Fischer pour avoir développé le projet datamaps en premier lieu ! Si vous avez accès à des données de localisation, envisagez les nombreuses façons intéressantes de les visualiser. Vous pourriez également essayer d'utiliser des Tweets de l'API Twitter, assurez-vous simplement qu'ils ont des données de localisation attachées.

### Vous voulez voir plus de choses comme ça ?

Suivez-moi sur Twitter : [@umaar](https://twitter.com/umaar) et faites-le-moi savoir ! J'essaie de tweeter beaucoup de ressources de développement web.

Veuillez aimer et partager si vous avez aimé lire mon article et laissez un commentaire avec vos expériences en visualisation de données.