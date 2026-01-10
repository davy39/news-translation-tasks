---
title: Comment le traitement de flux sans serveur facilitera la prise de décision
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-09T19:08:22.000Z'
originalURL: https://freecodecamp.org/news/how-serverless-stream-processing-will-make-decision-making-easier-d929502b43c8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0FKhwNV-o-OEiuFqSz_tSQ.jpeg
tags:
- name: analytics
  slug: analytics
- name: big data
  slug: big-data
- name: Productivity
  slug: productivity
- name: serverless
  slug: serverless
- name: technology
  slug: technology
seo_title: Comment le traitement de flux sans serveur facilitera la prise de décision
seo_desc: 'By Chamath Kirinde

  About a year ago, we started being a part of the digital transformation with the
  first ever cloud-based IDE for serverless development. It was no cakewalk — we’ve
  been burning the candle at both ends trying to cover the majority fr...'
---

Par Chamath Kirinde

Il y a environ [un an](https://globenewswire.com/news-release/2018/02/06/1333797/0/en/SLAppForge-Announces-Sigma-a-Cloud-IDE-for-Serverless-Computing.html), nous avons commencé à faire partie de la transformation numérique avec le premier environnement de développement intégré (IDE) basé sur le cloud pour le développement sans serveur. Ce ne fut pas une partie de plaisir — nous avons travaillé sans relâche pour couvrir la majorité de la pile sans serveur d'AWS. Travailler avec AWS Kinesis m'a fait réaliser la beauté du sans serveur — bien sûr, l'exposition aux données de streaming avec Kafka m'a fait gagner du temps pour comprendre les rudiments.

![Image](https://cdn-media-1.freecodecamp.org/images/IBLdvoo4R41bu17WA8x0Wy7gia9EtFjG4BzO)
_Prise de décision rationnelle : Photo par [Unsplash](https://unsplash.com/photos/o4c2zoVhjSw?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Raj Eiamworakul</a> sur <a href="https://unsplash.com/search/photos/rational-decisions?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### TL;DR

Vous êtes-vous déjà demandé...

* Comment **"Google Search"** vous suggère des choses lorsque vous êtes en train de taper votre requête ?
* Comment **"Cheapest Airlines"** commence à apparaître partout après avoir recherché un pays ?
* Comment les jeux de rôle en ligne s'adaptent selon vos décisions ?
* Comment les sites de paris prédisent les cotes d'un jeu en direct ?
* Pourquoi [Curry et Thompson ont été mis sur le banc](https://www.cbssports.com/nba/news/warriors-wearable-weapon-devices-to-monitor-players-while-on-the-court/) alors que Portland infligeait aux Warriors leur pire défaite lors d'une saison NBA à 73 victoires ?

![Image](https://cdn-media-1.freecodecamp.org/images/4vE1DrCz1W1TQwQIWA3IwAsGTeVgcT9Nh-7k)
_L'autocomplétion de requête de Google (parfois si agaçante)_

Le pouvoir de l'analyse des données de streaming en temps réel est effectivement impressionnant. Maintenant que la technologie sans serveur gagne en popularité, peut-être que vous n'aurez plus à vous soucier de prendre des décisions risquées tout seul. Cet article couvre les bases du "traitement de données de streaming sans serveur" et comment il deviendra un composant influent de notre prise de décision dans le futur.

### Des données, partout

La vie est une série sans fin d'événements. La technologie qui nous entoure en a fait un flux d'actions numériques émettant des flux de données. Si vous regardez en arrière et examinez votre vie très attentivement, vous verrez la chaîne sans fin de données que vous avez générée avec chacune de vos actions numériques. Cela peut être difficile à digérer au début, mais explorons quelques scénarios et essayons de trouver ce qui s'applique à vous et à moi.

* Banque en ligne et capacités d'achat e-commerce pratiques
* Covoiturage, voyages et transports modernes
* Équipements industriels et cas d'utilisation agricoles comme les machines surveillées, les tracteurs autonomes et l'agriculture de précision
* Génération d'énergie automatisée et réseaux intelligents, bâtiments à énergie nette zéro, comptage intelligent
* Recommandations immobilières basées sur la géolocalisation, maintenance prédictive
* Rencontres en ligne et mise en relation reposant sur des modèles de personnalité complexes et la distribution d'attributs

![Image](https://cdn-media-1.freecodecamp.org/images/UoE9uNA5mdznpmW5aFLsmjQZkO4K5JibcOSh)
_Romance rationnelle : Serez-vous mon Valentin ?_

* Trading financier selon les changements en temps réel du marché boursier, gestion des risques analytique
* Films, chansons et autres médias numériques avec une meilleure expérience en fonction des données démographiques, des préférences et des émotions
* Expérience améliorée des applications web et mobiles basée sur l'utilisation
* Expériences dynamiques et personnalisées dans les jeux en ligne
* Expériences améliorées sur les réseaux sociaux avec une hyper-personnalisation et une analyse prédictive
* Télémétrie des appareils connectés, ou centres de données distants pour des services géospatiaux ou spatiaux comme la météo, l'évaluation des ressources
* Analyse sportive pour améliorer les performances des joueurs en réduisant les risques pour la santé

![Image](https://cdn-media-1.freecodecamp.org/images/VuM87-7-xwLq12dD8IBIKTsxcwY18TqGwyfH)
_Bienvenue dans l'analyse_

Tous ces événements produisent des données — beaucoup de données. En raison de la fréquence de cette émission de données, cela est devenu un fardeau croissant pour l'espace numérique.

### Qu'est-ce que les données de streaming ?

Dans une [enquête](https://www.domo.com/learn/data-never-sleeps-6) menée l'année dernière sur les données, il est estimé qu'avec le rythme actuel de génération de données,

> 1,7 Mo de données seront créés chaque seconde pour chaque personne sur terre d'ici 2020

Les données qui sont émises en continu par une multitude de sources chaque seconde sont devenues un fait que nous ne pouvons plus ignorer. La discipline du Big Data a été une révélation pour le monde technologique afin d'appliquer ces données autrefois irritantes à quelque chose d'utile. Ces mêmes données ennuyeuses sont collectées et analysées par une nouvelle espèce, à savoir les scientifiques des données 🧑‍🔬. En raison de leur nature continue et souvent de petite taille (de l'ordre du kilooctet), ces flux de données — généralement appelés données de streaming — sont collectés simultanément sous forme d'enregistrements et envoyés pour un traitement ultérieur.

### Du traitement de flux à la prise de décision intelligente

Une structure de traitement de données de streaming est généralement composée de deux couches — une couche de stockage et une couche de traitement. La première est responsable de l'ordonnancement de grands flux d'enregistrements et facilite la persistance et l'accessibilité à grande vitesse. La couche de traitement s'occupe de la consommation des données, de l'exécution des calculs et de la notification à la couche de stockage pour se débarrasser des enregistrements déjà traités. Le traitement des données est effectué pour chaque enregistrement de manière incrémentielle ou en correspondant à des fenêtres de temps glissantes. Les données traitées sont ensuite soumises à des opérations d'analyse de streaming et les informations dérivées sont utilisées pour prendre des décisions basées sur le contexte.

Par exemple, les entreprises peuvent suivre les changements de sentiment public sur leurs produits en analysant en continu les flux des réseaux sociaux. Les nations les plus influentes du monde peuvent [intervenir dans des événements décisifs](https://www.bbc.com/news/technology-46590890) comme les élections présidentielles dans d'autres pays puissants. Et les applications mobiles peuvent offrir des recommandations personnalisées pour des produits basées sur la géolocalisation des appareils et les émotions des utilisateurs.

![Image](https://cdn-media-1.freecodecamp.org/images/QxndNC2SRx15iRq02C8qQBWHEAqe5v01WemR)
_Mauvaise analyse de données — Mauvaises décisions_

La plupart des applications collectent une partie de leurs données au départ pour produire des rapports de synthèse simples et prendre des décisions simples telles que le déclenchement d'alarmes ou le calcul d'une valeur moyenne mobile. Avec le temps, celles-ci deviennent de plus en plus sophistiquées, et les entreprises peuvent vouloir accéder à des informations approfondies pour effectuer des activités complexes à leur tour avec l'aide d'algorithmes d'apprentissage automatique et de techniques d'analyse de données.

La croissance continue des données a fait travailler les scientifiques des données jour et nuit pour proposer des solutions innovantes afin d'utiliser autant de données que possible pour fabriquer des futurs alternatifs avec de meilleures décisions.

### Facilitateurs de services

L'adoption du fournisseur de cloud idéal pour répondre aux exigences organisationnelles peut être écrasante. Cependant, tous les principaux fournisseurs de services cloud sont équipés d'options compétitives pour accommoder le traitement de flux en raison de son impact omniprésent. Voici une liste des services sans serveur couramment utilisés pour renforcer les applications de niveau entreprise, reposant fortement sur les données de streaming.

![Image](https://cdn-media-1.freecodecamp.org/images/5cstIiKD2o7dl82UVruDBBvv8NmqHTqI0rRE)
_Infographie : Composants de traitement de flux sans serveur_

### Exemples concrets

De nombreuses entreprises utilisent les informations issues de l'analyse de flux pour améliorer la visibilité de leurs activités. Cela leur permet d'offrir à leurs clients une expérience personnalisée. De plus, la transparence en temps quasi réel donne à ces entreprises la flexibilité nécessaire pour répondre rapidement aux urgences.

L'architecture sans serveur émergente a poussé toutes les principales plateformes de services cloud à présenter des solutions complémentaires. Le traitement de flux a été rendu disponible pour le développement d'applications sans serveur avec des services entièrement gérés, basés sur le cloud, pour le traitement de données en temps réel sur de grands flux de données distribuées.

#### 1. Télévision hyper-personnalisée

![Image](https://cdn-media-1.freecodecamp.org/images/3tdMjLGeH4Oaf2zq84AKbmJvm1H-ejVMEK0H)
_Netflix : Photo par [Unsplash](https://unsplash.com/@jenskreuter?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Jens Kreuter</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Netflix, le principal réseau de télévision en ligne au monde, a développé une solution qui centralise leurs journaux de flux [en utilisant Amazon Kinesis Streams](https://aws.amazon.com/solutions/case-studies/netflix-kinesis-streams/). En tant que système traitant des milliards de flux de trafic chaque jour, cela élimine beaucoup de complexité pour eux en raison de l'absence de base de données dans l'architecture. Grâce à la haute scalabilité et à la vitesse fulgurante, ils peuvent découvrir et résoudre les problèmes dès qu'ils surviennent, et surveiller l'application à grande échelle.

Avec l'algorithme de recommandation amélioré, le transcodage vidéo et l'acquisition de médias populaires, cela offre ensuite une expérience transparente aux abonnés. Avec la croissance exponentielle des abonnés, les responsabilités de l'entreprise augmentent de jour en jour. Cependant, rien ne semble être un problème pour Netflix puisqu'ils sont considérés comme ayant un [modèle de prise de décision solide](https://www.forbes.com/sites/danpontefract/2019/02/04/the-netflix-decision-making-model-is-why-theyre-so-successful/#11a4e67273bc).

#### 2. Améliorer les décisions des décideurs

En tant que principale source d'informations intégrées et intelligentes pour les entreprises et les professionnels, Thomson Reuters fournit ses services aux décideurs dans un large éventail de domaines comme la finance et le risque, la science, le juridique, la technologie. Cette entreprise a construit un moteur d'analyse interne pour prendre le contrôle total des données et a migré vers AWS car ils étaient familiers avec ses capacités et son échelle.

Le nouveau pipeline en temps réel [attaché à Amazon Kinesis](https://aws.amazon.com/solutions/case-studies/thomson-reuters/) produit de meilleurs résultats en termes d'expérience client perceptive avec des prévisions économiques précises, des tendances financières pour les bénéficiaires, y compris une gamme d'activités gouvernementales.

#### 3. Unicorn : une solution à la congestion du trafic

![Image](https://cdn-media-1.freecodecamp.org/images/Pz294qBcYfaEhKVPStwmt7eBxJ2YYAqVJsnL)
_Unicorn : Photo par [Unsplash](https://unsplash.com/@boudewijn_huysmans?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Boudewijn Huysmans</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Jakarta est devenue une ville très congestionnée où la moto a été jugée comme le mode de transport le plus efficace. Pour exploiter cette opportunité commerciale, GO-JEK — l'une des rares entreprises licornes en Asie du Sud-Est — a commencé comme un centre d'appels pour les réservations de taxis moto. Cependant, pour répondre à la demande en dépassant les attentes, l'entreprise a dû envisager une expansion. Maintenant, avec le soutien des services professionnels de Google Cloud, l'architecture commerciale construite sur Cloud Dataflow pour l'inférence de flux leur permet de prédire efficacement les changements de demande.

Il existe de nombreuses autres histoires sur la manière dont les plateformes cloud comme [AWS](https://aws.amazon.com/lambda/resources/customer-case-studies/), [Google](https://cloud.google.com/customers/#/products=Big_Data_Analytics,Marketing_Analytics), [Microsoft Azure](https://azure.microsoft.com/en-us/case-studies/?service=stream-analytics%7Cevent-hubs&solution=serverless), et [IBM Cloud](https://console.bluemix.net/docs/openwhisk/openwhisk_use_cases.html#openwhisk_event_processing) sont exploitées par les entreprises pour améliorer et sécuriser la vie de leurs clients.

### Limites du traitement de flux sans serveur

Le traitement de flux sans serveur devient de plus en plus une partie vitale des moteurs de prise de décision. Cependant, avec l'ensemble actuel de fonctionnalités, ce n'est pas la solution idéale pour certains scénarios. La mise en œuvre d'analyses en temps réel pour des fenêtres glissantes et des motifs d'événements temporels n'est pas une tâche pour les âmes sensibles.

La meilleure façon d'assimiler des données sans fin de cette ampleur est par le biais de tableaux de bord en temps réel, ce qui nécessite une organisation supplémentaire des données et leur persistance. Ces manœuvres introduisent une latence indésirable et des problèmes de gestion des données dans le contexte. Cependant, la technologie évolue et tente de rattraper les vitesses avec l'intégration de techniques avancées de gestion des données cloud pour produire des vues matérialisées.

![Image](https://cdn-media-1.freecodecamp.org/images/nT-vi3LfbSp5CwbMKlR-teyFq5br9oem6MYu)
_Sécurité : Une préoccupation majeure_

Le traitement de flux utilise souvent une fenêtre basée sur le temps ou sur les enregistrements à traiter, contrairement au traitement par lots, ce qui peut poser des défis dans les cas d'utilisation nécessitant une réexécution de requêtes.

De nos jours, les exigences des applications vont au-delà des analyses agrégées. Augmenter la taille de la fenêtre semble être une solution temporaire appropriée, mais cela développe un autre problème insoluble — la gestion de la mémoire. Les solutions modernes fournissent généralement des techniques avancées de gestion de la mémoire et de planification pour surmonter cela, mais le monde verra des améliorations supplémentaires.

### Conclusion

En somme, il est évident que le traitement de flux sans serveur a joué un rôle prominent autour de nous sans même que nous le sachions. Avec la puissance du traitement de flux de données sans serveur, les applications peuvent évoluer du traitement par lots traditionnel à l'analyse en temps réel. La révélation d'informations profondes entraînera une prise de décision efficace sans avoir à gérer l'infrastructure.

Même aujourd'hui, de nombreuses organisations pratiquent des stratégies de prise de décision orthodoxes basées sur les analyses dérivées des clusters de big data appartenant au **PASSÉ**. De nouveaux horizons sans serveur et de traitement de données en temps réel sont désormais équipés de la puissance nécessaire pour prendre des décisions efficaces et créer un monde plus productif, pertinent et, surtout, sécurisé autour de vous.

Le traitement de flux sans serveur rendra-t-il la prise de décision émotionnelle obsolète et le jugement rationnel informatisé la norme ?

Qu'en pensez-vous ?

### Que devriez-vous faire maintenant ?

* **Applaudissez.** Appréciez et laissez les autres trouver cet article.
* **Commentez.** Partagez vos pensées.
* **Suivez-moi.** [Chamath Kirinde](https://medium.com/@jchamath) pour recevoir des mises à jour sur des articles comme celui-ci.
* **Restez en contact.** [LinkedIn](https://www.linkedin.com/in/jchamath/), [Twitter](https://twitter.com/JChamath), [Chummy Charms](https://chummycharms.blogspot.com)
* **Pensez sans serveur.** [SLAppForge](https://slappforge.com/blog)

_Publié à l'origine sur [chummycharms.blogspot.com](https://chummycharms.blogspot.com/2019/03/serverless-stream-processing.html)._