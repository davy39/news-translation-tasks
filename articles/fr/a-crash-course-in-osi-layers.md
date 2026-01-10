---
title: Un cours accéléré sur les couches OSI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/a-crash-course-in-osi-layers
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d21740569d1a4ca360e.jpg
tags:
- name: computer networking
  slug: computer-networking
- name: networking
  slug: networking
- name: toothbrush
  slug: toothbrush
seo_title: Un cours accéléré sur les couches OSI
seo_desc: 'Introduction

  Have you ever wondered how data is sent through the network from one machine to
  another? If yes, then the Open System Interconnected model is what you are looking
  for.

  The OSI model is used to help standardize and characterize how data s...'
---

### **Introduction**

Vous êtes-vous déjà demandé comment les données sont envoyées à travers le réseau d'une machine à une autre ? Si oui, alors le modèle Open System Interconnected est ce que vous cherchez.

Le modèle OSI est utilisé pour aider à standardiser et caractériser comment les données doivent circuler de l'expéditeur au destinataire sans prendre en considération la structure interne sous-jacente du point final (expéditeur, destinataire).

L'organisation qui a élaboré ce modèle est l'**Organisation internationale de normalisation** et donc ce modèle est formellement appelé **ISO - OSI**.

### **Architecture**

Comme le montre la figure ci-dessous, le modèle divise le réseau en **7 couches**. La communication de données dans le modèle OSI commence par la couche supérieure (couche Application) de la pile du côté de l'expéditeur, descend la pile jusqu'à la couche la plus basse de l'expéditeur (couche Physique), traverse ensuite la connexion réseau physique jusqu'à la couche inférieure du côté du destinataire, et remonte sa pile de modèle OSI.

Nous optons pour une approche en couches car il est facile de concevoir des couches indépendantes avec des fonctions dédiées qui interagissent les unes avec les autres par rapport à un modèle complexe unique.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/33828192-2773b920-de91-11e7-8804-08dbfaf0143a.jpg)

### **Observations importantes**

* _**Couches de bout en bout :**_ Dans le diagramme ci-dessus, vous remarquerez que les couches supérieures du protocole (Application - Transport), les couches de l'expéditeur et du destinataire sont directement connectées via des flèches. Cela est dû au fait que ces couches ne sont pas conscientes des dispositifs intermédiaires utilisés pour transporter les données (tels que les commutateurs et les routeurs). Ces couches semblent communiquer directement entre elles.
* _**Unité de données :**_ Dans le diagramme ci-dessus, à l'extrême gauche se trouve l'unité de données utilisée dans chacune des couches. La couche transport (et les couches en dessous) ont un nom unique pour l'unité de données transférée de l'expéditeur au destinataire.

### **Fonctions des couches**

* **_Couche 1 - Couche Physique_** : La couche physique est la plus basse des couches OSI et la plus complexe. Cela est dû aux technologies matérielles sous-jacentes utilisées. La fonction de cette couche est de définir comment le flux de bits sera transmis plutôt que le paquet de données logique. Elle traite de la définition de la fréquence à laquelle le bit sera transmis, du type de modulation qui sera utilisé, de la manière dont les bits seront regroupés et d'autres paramètres physiques de bas niveau nécessaires à la transmission des bits.
* **_Couche 2 - Couche de Liaison de Données_** : La couche de liaison de données est responsable du transfert de données vers les dispositifs adjacents sur le même réseau local (LAN). Cette couche dispose également de dispositions pour s'assurer que les données sans erreur sont transmises aux couches supérieures depuis la couche physique. Elle contient donc des mécanismes de détection et de correction d'erreurs pour garantir que l'intégrité des données est maintenue.
* **_Couche 3 - Couche Réseau_** : La couche réseau est responsable de l'acheminement des paquets vers d'autres réseaux. Habituellement, un réseau est divisé en plusieurs sous-réseaux et la couche réseau, à l'aide de routeurs, achemine les paquets entre de tels réseaux pour établir un réseau étendu (WAN).
* **_Couche 4 - Couche Transport_** : La couche transport garantit que les messages sont livrés sans erreur, dans l'ordre, et sans pertes ni duplication. Elle soulage les protocoles de couche supérieure de toute préoccupation concernant le transfert de données entre eux et leurs pairs.
* **_Couche 5 - Couche Session_** : La couche session permet l'établissement de sessions entre les processus s'exécutant sur différentes stations.
* **_Couche 6 - Couche Présentation_** : La couche présentation formate les données à présenter à la couche application.
* **_Couche 7 - Couche Application_** : La couche application sert de fenêtre pour les utilisateurs et les processus d'application afin d'accéder aux services réseau.