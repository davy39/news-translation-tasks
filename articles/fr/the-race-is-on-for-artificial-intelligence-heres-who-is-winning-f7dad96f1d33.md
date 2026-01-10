---
title: La course à l'intelligence artificielle est lancée. Voici qui est en tête.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-05-08T18:23:42.000Z'
originalURL: https://freecodecamp.org/news/the-race-is-on-for-artificial-intelligence-heres-who-is-winning-f7dad96f1d33
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1cqiEqRqDuvvfvsO1M68qw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: La course à l'intelligence artificielle est lancée. Voici qui est en tête.
seo_desc: 'By Terren Peterson

  On Saturday, Louisville, Kentucky hosted the 143rd running of the Kentucky Derby.
  It was a spectacle where more than 150k people watched in person. Millions more
  followed on television and streaming media. The winner received a $1....'
---

Par Terren Peterson

Samedi, Louisville, dans le Kentucky, a accueilli la 143e édition du [Kentucky Derby](https://www.kentuckyderby.com/). Ce fut un spectacle où plus de 150 000 personnes ont assisté en personne. Des millions d'autres ont suivi à la télévision et sur les médias en streaming. Le vainqueur a reçu un prix de 1,4 million de dollars et l'opportunité de gagner davantage lors des courses ultérieures cette année.

Une course plus importante fait rage dans le secteur technologique autour de la commodification de l'apprentissage automatique en tant que service. Les modèles d'apprentissage automatique préconstruits valent des milliards de dollars. Cette compétition oppose les plus grandes entreprises technologiques de la planète.

Des événements comme le Kentucky Derby ont en réalité de nombreuses courses qui se déroulent le même jour. La course pour dominer l'apprentissage automatique est similaire. Pour cet article, je vais me concentrer uniquement sur la manière dont la course pour la reconnaissance d'images se dessine.

### Les concurrents du Cloud

Actuellement, il existe des options proposées par chacun des principaux fournisseurs de Cloud public. Amazon, Google et Microsoft occupent une position de choix grâce à leurs services d'hébergement de stockage. Leurs offres détermineront la direction du marché. La reconnaissance d'images pourrait devenir une fonctionnalité intégrée aux grands systèmes de stockage d'images basés sur le Cloud. Cette évolution éliminerait les modèles préconstruits en tant que produit distinct.

#### Tester les offres actuelles

Pour "faire courir" les fournisseurs les uns contre les autres, j'ai utilisé la photo ci-dessous provenant de [Wikipedia](https://upload.wikimedia.org/wikipedia/commons/7/7b/Horseracing_Churchill_Downs.jpg). Pour rendre l'article plus lisible, j'ai réduit la précision de chacune des réponses ci-dessous à trois chiffres.

![Image](https://cdn-media-1.freecodecamp.org/images/K27Q2AZXkFG6E01SPc-Y8Y9WYr29aofhpMHR)

#### Amazon

Amazon possède la plus grande empreinte de Cloud public dans l'industrie. Il y a six mois, ils ont lancé leur MVP de [Rekognition](https://aws.amazon.com/rekognition/). Ce service s'appuie sur leur plateforme Cloud car il s'intègre à S3 et Lambda. Voici ce que leurs modèles déterminent à partir de la photo de course.

```
[{Confidence: 98.0, Name: Animal},{Confidence: 98.0, Name: Horse},{Confidence: 98.0, Name: Mammal},{Confidence: 90.8, Name: Equestrian},{Confidence: 90.8, Name: Person},{Confidence: 52.7, Name: Colt Horse}]
```

#### Google

Google possède une grande activité Cloud, y compris le stockage d'objets. Leur historique avec la reconnaissance d'images dans la recherche est également un avantage massif. L'utilisation de leur [Cloud Vision API](https://cloud.google.com/vision/) fournit une réponse complète sur l'image de course.

```
[{ "description": "horse", "score": 0.937 },{ "description": "western riding", "score": 0.889 },{ "description": "jockey", "score": 0.881 },{ "description": "racing", "score": 0.861 },{ "description": "stallion", "score": 0.810},{ "description": "mare", "score": 0.810 },{ "description": "western pleasure", "score": 0.806 },{  "description": "sports", "score": 0.776 },{  "description": "horse racing", "score": 0.775 },{  "description": "english riding", "score": 0.731 },{  "description": "horse trainer", "score": 0.722 },{  "description": "equestrian sport", "score": 0.708 },{  "description": "equestrianism", "score": 0.705 },{  "description": "animal sports", "score": 0.685 },{  "description": "barrel racing", "score": 0.648},{  "description": "eventing", "score": 0.614},{  "description": "horse like mammal", "score": 0.590},{  "description": "reining", "score": 0.546 }]
```

Google va encore plus loin en ajoutant la reconnaissance de texte. Lors de l'analyse de l'image, il a traduit le texte du tableau de score. Voir les boîtes jaunes en haut à gauche de l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/VShdHXElPgOiLBHMPRVbNcbadHj70Getdkgj)

Google traduit ces informations dans un format lisible par machine (JSON). Il s'agit d'une fonctionnalité puissante que les autres n'offrent pas encore.

#### Microsoft

Microsoft possède également la combinaison d'un grand Cloud et d'une activité de recherche. Leur offre est sur le marché depuis plus d'un an. Leur [Cloud Vision API](https://www.microsoft.com/cognitive-services/en-us/computer-vision-api) a reconnu l'image et fourni les résultats suivants.

```
[ { name: grass, confidence: 0.999 },{ name: fence, confidence: 0.999 },{ name: outdoor, confidence: 0.995 },{ name: horse, confidence: 0.985 },{ name: ground, confidence: 0.974 },{ name: sport, confidence: 0.821 },{ name: horse racing, confidence: 0.519 }]
```

### Les outsiders

Cette course compte plus de participants que les trois principaux fournisseurs de Cloud public. IBM dispose de Watson et de solides capacités en IA. Ils ont activé cette capacité au sein de [BlueMix](https://visual-recognition-demo.mybluemix.net/). Voici ce que j'ai obtenu en tentant d'utiliser la démonstration publique avec la photo.

![Image](https://cdn-media-1.freecodecamp.org/image/not-found.jpg)

Il existe des limitations avec ce service, notamment des restrictions de taille. Cela peut constituer un écart d'utilisabilité qui décourage les clients. J'ai trouvé une [photo similaire](https://upload.wikimedia.org/wikipedia/commons/6/63/Horse-racing-4.jpg) sur Wikipedia qui était dans la limite de 2 Mo. La qualité de la reconnaissance était similaire à celle des autres.

```
[ { "class": "horse racing", "score": 0.922 },{ "class": "racing", "score": 0.928 },{ "class": "sport", "score": 0.928 },{ "class": "jockey (horse rider)", "score": 0.622 },{ "class": "traveler", "score": 0.622 },{ "class": "person", "score": 0.622 },{ "class": "racehorse", "score": 0.53 },{ "class": "mammal", "score": 0.53 },{ "class": "animal", "score": 0.53 },{ "class": "green color", "score": 0.876 }]
```

Les start-ups offrent des alternatives créatives dans cette course. Un exemple est [Clarifai](https://www.clarifai.com/demo) qui a [levé 30 millions de dollars](https://techcrunch.com/2016/10/25/clarifai-raises-30m-to-give-developers-visual-search-capabilities/) l'année dernière. Leur API a mis en évidence une reconnaissance solide en utilisant la même image que les géants de la technologie.

```
horse, 0.999equine, 0.992race, 0.990track, 0.989fast, 0.984jockey, 0.983thoroughbred, 0.981competition, 0.966gambling, 0.951filly, 0.942mare, 0.936turf, 0.924whip, 0.902best, 0.897stallion, 0.882athlete, 0.869saddle, 0.865racehorse, 0.864rider, 0.864blinker, 0.858
```

Cela met en évidence le potentiel pour un nouveau venu de percer dans cette course. La start-up pourrait emprunter les rails d'un fournisseur d'hébergement Cloud existant, lui offrant ainsi des économies d'échelle.

### Qui est le vainqueur ?

La course est très compétitive, avec Google actuellement en tête. Les développeurs de logiciels intégrant la reconnaissance d'images dans leurs produits numériques sont également des gagnants. J'ai récemment construit un jeu Alexa qui l'utilise pour jouer à une [chasse au trésor](https://medium.freecodecamp.com/how-to-make-scavenger-hunts-more-fun-with-artificial-intelligence-74a184f3db33). Cela a été fait avec seulement quelques lignes de code et sans effort pour entraîner des modèles.

Le prix actuel est d'environ 1 $/mille images. À ce niveau, la reconnaissance d'images sera intégrée dans de nombreux produits différents. La course pour devenir le service le plus consommé est lancée !