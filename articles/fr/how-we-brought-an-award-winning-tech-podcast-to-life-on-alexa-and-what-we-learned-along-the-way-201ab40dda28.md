---
title: Comment ACG a donné vie à un podcast technologique primé sur Alexa, et ce que
  nous avons appris en cours de route
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-04T20:55:33.000Z'
originalURL: https://freecodecamp.org/news/how-we-brought-an-award-winning-tech-podcast-to-life-on-alexa-and-what-we-learned-along-the-way-201ab40dda28
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RVhVxj_vPrV5qeH7WUrwcA.png
tags:
- name: AWS
  slug: aws
- name: podcast
  slug: podcast
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment ACG a donné vie à un podcast technologique primé sur Alexa, et
  ce que nous avons appris en cours de route
seo_desc: 'By Drew Firment

  Podcasts are even better when controlled by a voice-first interface.

  Every month, 67 million Americans listen to podcasts, with the average podcast fan
  listening to 5 shows per week.

  Audio podcasts are popular for good reason. Within ...'
---

Par Drew Firment

#### Les podcasts sont encore meilleurs lorsqu'ils sont contrôlés par une interface vocale.

Chaque mois, 67 millions d'Américains écoutent des podcasts, avec en moyenne 5 émissions par semaine pour les fans de podcasts.

Les podcasts audio sont populaires pour de bonnes raisons. En l'espace de 30 minutes, un auditeur peut être inspiré et éduqué par un contenu influent — sans interference des écrans.

En écoutant un épisode, vous pouvez rattraper vos emails, faire de l'exercice, vous déplacer ou vous détendre sur la terrasse. L'expérience purement auditive d'un podcast libère vos autres sens — offrant aux auditeurs une opportunité de multitâche.

Dans un récent article, Forbes a mis en avant _l'épuisement par les écrans_ comme l'un des principaux contributeurs à la popularité des podcasts, entraînant une croissance de 11 % du nombre d'auditeurs au cours de l'année passée.

> « Excitants au début, les écrans sont devenus épuisants pour de nombreux utilisateurs, et les podcasts représentent une alternative rafraîchissante. Plutôt que d'utiliser vos yeux, vous utilisez vos oreilles ; il y a des silences, des pauses et des voix humaines authentiques plutôt que des mots et des images sur un écran. »

Malheureusement, les avantages complets d'une expérience de podcast sont souvent réduits par la friction des interfaces graphiques. Pour consommer le contenu auditif, un auditeur doit cliquer sur des contrôles et naviguer sur des écrans de ses appareils.

Les podcasts sont mieux servis sans écran — en utilisant une interface vocale pour contrôler l'expérience qui élimine l'interférence et l'épuisement. Plutôt que de naviguer sur des écrans pour trouver des épisodes passés, contrôler la lecture ou ajuster le volume — demandez simplement à Alexa.

> Alexa, joue The Cloudcast.   
> Alexa, avance.  
> Alexa, pause.

C'est précisément pour cette raison que tant de podcasts de premier plan créent des compétences personnalisées spécialement conçues pour Alexa. En demandant simplement à Alexa, les auditeurs peuvent maintenant écouter 325 podcasts diffusés à partir d'émissions populaires telles que NPR ou TED Talks.

Et maintenant, les auditeurs avertis en technologie peuvent profiter d'un podcast primé sur tout ce qui concerne le cloud computing. Depuis 2011, Aaron Delp et Brian Gracely ont produit plus de 300 épisodes de [The Cloudcast](https://acloud.guru/cloudcast) depuis leurs studios à Raleigh, en Caroline du Nord — accumulant un taux d'écoute impressionnant de 1 million en 2017.

![Image](https://cdn-media-1.freecodecamp.org/images/o1JdQZKVEZU4NF6trSQXAsUBL8R7FQuDqG0c)

#### Alors, que faut-il pour publier un podcast sur Alexa ?

Un bon point de départ est l'un des [plusieurs modèles de podcast](https://github.com/search?q=alexa+podcast&type=) disponibles pour les développeurs sur GitHub — tous utilisant l'[Interface AudioPlayer](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/custom-audioplayer-interface-reference#valid-response-types-4) d'Amazon. De nombreux modèles nécessitent que chaque épisode soit téléchargé manuellement dans un bucket S3, tandis que d'autres modèles s'appuient sur le flux RSS d'un podcast.

Pour développer une compétence de podcast de haute qualité pour The Cloudcast, nous avons collaboré avec une nouvelle startup spécialisée dans les podcasts Alexa — [Fourthcast](https://www.fourthcast.com/). Notre équipe a appris leur service unique _Podcast as a Service_ à partir d'un article sur les [leçons utilisant AWS Lambda pour héberger des compétences Alexa](https://read.acloud.guru/lambda-for-alexa-skills-7-tips-from-the-trenches-684c963e6ad1).

En collaborant avec Fourthcast, nous avons eu l'occasion d'explorer ce qu'il faut pour développer une solution d'hébergement pour une compétence de podcast Alexa qui délivre un million d'écoutes. Voici quelques-unes des perspectives de notre expérience.

#### **_Les podcasts sont des cibles mouvantes._**

À mesure que de nouveaux épisodes sont publiés, une compétence doit détecter automatiquement les mises à jour pour qu'elles soient immédiatement disponibles pour les auditeurs. Pour la compétence The Cloudcast, une fonction Lambda distincte est utilisée pour vérifier fréquemment la disponibilité de nouveaux épisodes. Les résultats de la fonction sont mis en cache dans S3 — où une fonction Lambda séparée examine le statut. Cette approche garantit que nous avons toujours les derniers épisodes disponibles pour les auditeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/clsudurPRHSWyCvAsjClyk-Lg6fYF7Dw2OAd)

#### **_Performance_**

Pour éviter les problèmes de latence avec le streaming audio, les auditeurs s'appuient souvent sur une application _podcatcher_ — comme le client Apple iTunes. Ces applications sont utilisées pour s'abonner à des podcasts et télécharger automatiquement de nouveaux épisodes pour un stockage et une lecture locaux.

Contrairement aux appareils traditionnels, un Amazon Echo n'a pas la capacité de mettre en cache localement les épisodes — s'appuyant exclusivement sur le streaming en temps réel. Par conséquent, la qualité d'un flux de podcast Alexa vers un appareil Echo dépend fortement de la qualité de la solution d'hébergement.

Pour de nombreux podcasts, leur solution d'hébergement actuelle n'est tout simplement pas assez rapide pour supporter les exigences de streaming en temps réel d'Alexa. Dans ces cas, Fourthcast utilise un bucket S3 comme _podcatcher_ pour télécharger et mettre en cache le contenu actuel. Pour améliorer les performances de streaming des grands fichiers MP3, les enregistrements sont automatiquement ré-encodés en fichiers de qualité de streaming plus petits à l'aide d'[Elastic Transcoder](https://aws.amazon.com/elastictranscoder/).

#### **_Le protocole HTTPS_**

La plupart des flux RSS de podcasts utilisent une URL HTTP pour référencer un épisode — alors que les compétences de podcast Alexa nécessitent l'utilisation de HTTPS. Heureusement, la majorité des services de podcasts supportent HTTPS — ce qui signifie que vous pouvez vous en sortir en modifiant simplement l'URL référencée vers le protocole HTTPS.

Dans les rares cas où cela ne fonctionne pas, créez simplement un proxy CloudFront qui utilise HTTPS du côté de la requête et HTTP du côté de l'origine.

![Image](https://cdn-media-1.freecodecamp.org/images/VcvdhajWEoERoKAXv0K2EmFzoA3an2i3XyDp)

#### Une base de données

_Tout podcast digne de ce nom aura besoin d'une base de données_. Cela est essentiel pour quelques raisons clés — suivre la progression de l'utilisateur 1) _à travers les épisodes_ et _2) au sein des épisodes_. En utilisant une base de données, une session de podcast peut être reprise à l'endroit précis d'un épisode inachevé. DynamoDB est le choix naturel pour ce travail — en raison de sa connexion à faible latence avec Lambda.

En rassemblant tous ces éléments, on obtient une expérience de podcast de meilleure qualité — et avec de nouvelles fonctionnalités comme l'[API de Notifications](https://developer.amazon.com/blogs/alexa/post/8cc45487-d5fb-413b-b6c7-eeea4794d10c/amazon-announces-notifications-for-alexa-feature-is-coming-soon-sign-up-to-stay-tuned), nous avons hâte d'intégrer plus d'éléments qui rendront les podcasts sur Alexa encore meilleurs.

[**The Cloudcast, présenté par A Cloud Guru**](https://acloud.guru/cloudcast)  
[_Un podcast primé sur le cloud computing, présenté par A Cloud Guru._acloud.guru](https://acloud.guru/cloudcast)

Maintenant que vous avez appris ce qu'il faut pour donner vie à un podcast sur Alexa, nous espérons que vous apprécierez le dernier épisode de [A Cloud Guru Presents The Cloudcast](https://acloud.guru/cloudcast) !