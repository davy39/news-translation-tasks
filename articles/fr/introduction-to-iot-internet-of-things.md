---
title: Une introduction à l'Internet des objets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-26T17:08:40.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-iot-internet-of-things
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/internet_of_things_iot.jpg
tags:
- name: Internet of Things
  slug: internet-of-things
- name: Machine Learning
  slug: machine-learning
seo_title: Une introduction à l'Internet des objets
seo_desc: 'By Pier Paolo Ippolito

  Introduction

  During the last few years, Internet of Things (IoT) devices have started becoming
  a more and more important component in our daily lives. Some common applications
  for IoT devices are:


  Smart Home (eg. smart lamps)

  ...'
---

Par Pier Paolo Ippolito

## Introduction

Au cours des dernières années, les appareils de l'Internet des objets (IoT) ont commencé à devenir un composant de plus en plus important dans notre vie quotidienne. Certaines applications courantes pour les appareils IoT sont :

* Maison intelligente (par exemple, lampes intelligentes)
* Objets connectés (par exemple, montres intelligentes)
* Véhicules autonomes
* Villes intelligentes
* Commerce intelligent

Selon Wikipedia, les appareils IoT sont définis comme :

> "L'**Internet des objets** (**IoT**) est l'extension de la connectivité Internet aux appareils physiques et aux objets du quotidien. Équipés d'électronique, de connectivité Internet et d'autres formes de matériel (tels que des capteurs), ces appareils peuvent communiquer et interagir avec d'autres via Internet, et ils peuvent être surveillés et contrôlés à distance." — Wikipedia [1]

L'une des caractéristiques les plus intéressantes des appareils IoT est qu'ils sont capables de produire de grandes quantités de données. Cela peut être particulièrement utile dans des applications telles que l'intelligence artificielle et le machine learning.

La plupart des appareils IoT peuvent en effet produire une grande variété de données de séries temporelles qui sont d'un grand intérêt pour l'intelligence artificielle.

Selon une étude réalisée par [Global Data](https://www.globaldata.com/), le marché de l'IoT devrait atteindre 318 milliards de dollars de nouvelle valeur d'ici 2023 (en constante augmentation par rapport aux années précédentes).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/IoT-grow-chart.png)
_Figure 1 : Projections des marchés de l'IoT [2]._

Ces projections sont confirmées par l'intérêt accru des entreprises telles que Google et Microsoft à investir dans les plateformes cloud IoT.

## Comment fonctionnent les appareils IoT ?

Un système IoT est composé de quatre principaux composants :

1. **Capteurs** : permettent aux appareils de collecter des données à partir de l'environnement entourant l'appareil (par exemple, vitesse, coordonnées GPS, température, etc.).
2. **Connectivité** : les données collectées sont ensuite envoyées au cloud (via une connexion WiFi ou Bluetooth).
3. **Traitement des données** : une fois les données reçues par l'infrastructure cloud, elles peuvent alors être traitées (par exemple, vérifier si les données reçues répondent aux exigences et, si ce n'est pas le cas, alerter l'utilisateur).
4. **Interface utilisateur** : une fois les données traitées, les résultats sont ensuite donnés à l'utilisateur.

Prenons un exemple simple de flux de travail : considérons un système de sécurité dans une maison.

Notre appareil IoT vérifiera s'il y a des intrus dans notre maison à l'aide d'un système de vision par ordinateur (**Capteurs**). Les enregistrements vidéo de la maison sont ensuite envoyés au cloud pour voir s'il y a des intrus ou non (**Connectivité**). Ensuite, les données sont traitées dans le cloud (**Traitement des données**) et si des intrus sont détectés, nous sommes alertés (**Interface utilisateur**).

Un système IoT pourrait être en mesure de nous alerter de nombreuses manières différentes (par exemple, appel/téléphonie ou notification d'application) et dans certains cas, nous pourrions être en mesure de contrôler à distance le système lui-même (par exemple, verrouiller les portes de la maison).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/how-iot-works-summary.001.png)
_Figure 2 : Principaux composants d'un système IoT [3]_

## Plateformes cloud de l'Internet des objets

Je vais maintenant vous présenter certaines des plateformes cloud IoT les plus intéressantes qui peuvent être utilisées pour analyser et contrôler les appareils IoT.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/1_go7sTFOGN2fJGgYrI3E-FA.png)
_Figure 3 : Plateformes cloud IoT [4]_

### Google Cloud Internet of Things

Google Cloud est actuellement l'un des principaux fournisseurs de solutions cloud sur le marché. Certains des packages proposés par Google Cloud pour les implémentations IoT sont :

* **Cloud IoT Core** : utilisé pour configurer le ou les appareils et établir une connexion sécurisée entre eux.
* **Cloud Machine Learning Engine** : permet aux utilisateurs de créer des modèles de Machine Learning à partir des données collectées par les appareils IoT afin d'augmenter et de surveiller les performances.
* **Cloud Pub/Sub** : fournit des analyses en temps réel des appareils IoT.

### Azure Internet of Things

Microsoft Azure est un autre fournisseur de services cloud très important. Azure est capable de fournir des solutions pré-personnalisées et entièrement personnalisables. De cette manière, Azure est en mesure de fournir des solutions pour les débutants et les experts en IoT. Microsoft Azure permet de mettre facilement à l'échelle les systèmes IoT pour inclure des appareils de différents fabricants et fournit également un support pour les services d'analyse et de Machine Learning.

### Amazon Web Services (AWS)

AWS est l'une des solutions les plus populaires pour les services basés sur le cloud. AWS peut permettre de réaliser des projets IoT de bout en bout et en utilisant les quatre packages suivants :

* **AWS IoT Core** : est le package de base qui peut être utilisé pour configurer les appareils IoT. En utilisant IoT Core, nous pouvons intégrer différents appareils pour qu'ils communiquent entre eux via une connexion sécurisée, rendant possible l'échange de données via le stockage cloud.
* **AWS IoT Analytics** : est utilisé pour traiter et analyser toutes les données produites par les appareils IoT. Une fois toutes les données stockées à l'aide d'un format semi-structuré (par exemple, JSON, CSV), elles peuvent ensuite être utilisées à des fins de Machine Learning (par exemple, surveiller et optimiser l'interaction entre les appareils IoT).
* **AWS IoT Device Defender** : est utilisé pour construire et personnaliser les mécanismes de sécurité des appareils IoT (tels que le choix de l'authentification des appareils et du chiffrement des données).
* **AWS IoT Device Management** : permet d'intégrer facilement de nouveaux appareils IoT à un environnement et de surveiller/mettre à jour leurs fonctionnalités.

## Conclusion

Les appareils de l'Internet des objets vont définitivement jouer un rôle très important dans les avancées technologiques futures. Bien qu'il reste encore des problèmes à résoudre. En fait, l'une des principales préoccupations concernant les appareils IoT peut être la cybersécurité.

Parce que la plupart des appareils IoT utilisent un centre cloud pour stocker leurs données et collecter des informations utiles sur Internet, cela les rend vulnérables aux attaques des pirates (créant un point de défaillance unique).

Pour résoudre ce problème, il pourrait être possible soit d'augmenter les normes de chiffrement (ralentissant le transfert de données), soit d'utiliser des techniques de sécurité alimentées par l'intelligence artificielle telles que la [Differential Privacy and Federated Learning](https://towardsdatascience.com/ai-differential-privacy-and-federated-learning-523146d46b85).

Dans le cas où un pirate serait en mesure d'accéder au contrôle d'un appareil IoT (ou d'un groupe entier), il y aurait deux principaux risques associés :

* Le pirate serait en mesure d'accéder et de voler des données sensibles des utilisateurs de l'appareil IoT.
* Le pirate pourrait être en mesure de prendre le contrôle à distance de l'appareil lui-même.

En plus des services cloud fournis précédemment, les suivants peuvent également être considérés comme une alternative valable : [SAP](https://cloudplatform.sap.com/capabilities/product-info.SAP-Cloud-Platform-Internet-of-Things.48b79cfa-3d49-4a42-9249-e589696691ae.html), [Oracle Internet of Things](https://www.oracle.com/uk/internet-of-things/), [Cisco IoT Cloud Connect](https://www.cisco.com/c/en/us/solutions/service-provider/iot-cloud-connect/index.html), [IBM Watson Internet of Things](https://www.ibm.com/uk-en/internet-of-things), etc...

## Contacts

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-uns de mes détails de contact :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site web personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)

Photo de couverture [de cet article](https://foreignpolicyi.org/blockchain-and-cryptocrypto-solution/).

## Bibliographie

[1] Wikipedia, Internet des objets. Consulté à l'adresse : [https://en.wikipedia.org/wiki/Internet_of_things](https://en.wikipedia.org/wiki/Internet_of_things)

[2] Le marché mondial de l'IoT devrait atteindre 318 milliards de dollars d'ici 2023, selon GlobalData. Michelle Froese, Windpower Engineering & Development. Consulté à l'adresse : [https://www.windpowerengineering.com/business-news-projects/global-iot-market-to-reach-318-billion-by-2023-says-globaldata/](https://www.windpowerengineering.com/business-news-projects/global-iot-market-to-reach-318-billion-by-2023-says-globaldata/)

[3] Anni Junnila, COMMENT FONCTIONNE L'IOT – RÉSUMÉ – BLOG TRACKINNO. Consulté à l'adresse : [https://trackinno.com/2018/08/09/how-iot-works-part-4-user-interface/how-iot-works-summary-001/](https://trackinno.com/2018/08/09/how-iot-works-part-4-user-interface/how-iot-works-summary-001/)

[4] Aperçu des meilleures plateformes IOT. Conseils pour sélectionner la bonne solution cloud en 2019. Anna Davydova, Edsson. Consulté à l'adresse : [https://www.edsson.com/en/blog/article?id=iot-platforms](https://www.edsson.com/en/blog/article?id=iot-platforms)