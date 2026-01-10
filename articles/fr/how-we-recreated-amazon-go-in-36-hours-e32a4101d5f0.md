---
title: Comment nous avons recréé Amazon Go en 36 heures
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T20:57:41.000Z'
originalURL: https://freecodecamp.org/news/how-we-recreated-amazon-go-in-36-hours-e32a4101d5f0
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FR4dUJjxG1v5cV66.
tags:
- name: Android
  slug: android
- name: Future
  slug: future
- name: iot
  slug: iot
- name: software
  slug: software
- name: technology
  slug: technology
seo_title: Comment nous avons recréé Amazon Go en 36 heures
seo_desc: 'By Subhan Nadeem

  My colleagues and I wanted to create something that would make people go “wow” at
  our latest hackathon.

  Because imitation is the sincerest form of flattery and IoT is incredibly fun to
  work with, we decided to create our own version ...'
---

Par Subhan Nadeem

Mes collègues et moi voulions créer quelque chose qui ferait dire "wow" aux gens lors de notre dernier hackathon.

Parce que l'imitation est la forme la plus sincère de flatterie et que l'IoT est incroyablement amusant à travailler, nous avons décidé de créer notre propre version d'Amazon Go.

Avant de vous expliquer ce qu'il a fallu pour réaliser cela, voici une démonstration de 3 minutes de ce que nous avons construit !

Nous étions quatre. [Ruslan](https://www.freecodecamp.org/news/how-we-recreated-amazon-go-in-36-hours-e32a4101d5f0/undefined), un excellent développeur full-stack qui avait de l'expérience avec Python. John, un incroyable développeur iOS. Soheil, un autre excellent développeur full-stack qui avait de l'expérience avec Raspberry Pi. Et enfin, il y avait moi, à la fin d'un stage de développeur Android.

J'ai rapidement réalisé qu'il y avait beaucoup de pièces mobiles dans ce projet. Amazon Go fonctionne sur la base de capteurs de proximité en temps réel en conjonction avec une base de données en temps réel des clients et de leurs paniers.

Nous voulions également aller plus loin et rendre l'expérience d'entrée/sortie transparente. Nous voulions permettre aux gens d'entrer et de sortir du magasin sans avoir besoin de taper sur leurs téléphones.

Pour engager les utilisateurs en tant que produit grand public, notre application aurait besoin d'une interface utilisateur bien conçue, comme le vrai Amazon Go.

La veille du hackathon, j'ai préparé un pseudo-document de conception décrivant ce que nous devions faire dans le délai de 36 heures. J'ai incorporé les forces de notre équipe et l'équipement à disposition. Le document de conception complet, assemblé à la hâte, peut être vu ci-dessous.

Il y avait six composants principaux à EZShop, notre version d'Amazon Go.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eTzUuujmvx3U3foEb_lNog.png)
_Un diagramme rapide que j'ai préparé pour visualiser les composants de ce projet_

### L'API de reconnaissance faciale Kairos

L'[API de reconnaissance faciale Kairos](https://www.kairos.com/) était un composant fondamental pour nous. Elle abstraait la capacité d'identifier et de stocker des visages uniques. Elle avait deux API que nous avons utilisées : `/enroll` et `/verify`.

`/enroll` est décrit comme suit :

> Prend une photo, trouve les visages à l'intérieur et stocke les visages dans une galerie que vous créez.

Nous avons inscrit tous les nouveaux clients dans une seule galerie "EZShop". Un attribut `face_id` unique serait retourné et stocké avec le nom enregistré du client dans notre base de données en temps réel.

Lorsque nous voulions vérifier l'image d'un client potentiel, nous l'envoyions à l'endpoint `/verify`. Cela retournerait le `face_id` avec la plus haute probabilité de correspondance.

Dans une implémentation réelle, il aurait probablement été préférable d'utiliser un pipeline de reconnaissance faciale implémenté nativement avec TensorFlow plutôt qu'une API réseau. Mais étant donné nos contraintes de temps, l'API nous a très bien servis.

### **La base de données Firebase en temps réel**

La base de données Firebase était une autre pièce fondamentale de notre puzzle. Chaque autre composant interagissait avec elle en temps réel. Firebase permet de créer des écouteurs de changement personnalisés pour toute donnée dans la base de données. Cette fonctionnalité, couplée au processus de configuration facile, en a fait un choix évident.

Le schéma était incroyablement simple. La base de données stockait un tableau d'articles et un tableau d'utilisateurs. Voici un exemple de squelette JSON de notre base de données :

```
{  "items": [    {      "item_id": 1,      "item_name": "Soylent",      "item_stock": 1,      "price": 10    }  ],  "users": [    {      "face_id": 1,      "name": "Subhan Nadeem",      "in_store": false,      "cart": [        1      ]    }  ]}
```

Les nouveaux utilisateurs seraient ajoutés au tableau des utilisateurs dans notre base de données après s'être inscrits avec l'API Kairos. À l'entrée ou à la sortie, l'attribut booléen `in_store` du client serait mis à jour, ce qui serait reflété dans les interfaces utilisateur des applications du gestionnaire et personnelle.

Les clients prenant un article entraîneraient une mise à jour du stock de l'article. Après avoir reconnu quel client avait pris quel article, l'ID de l'article serait ajouté au tableau `cart` du client.

J'avais prévu un serveur Node/Flask hébergé dans le cloud qui routerait toute l'activité d'un appareil à un autre, mais l'équipe a décidé qu'il était beaucoup plus efficace (bien que plus bricolé) que tout le monde travaille directement sur la base de données Firebase.

### Les applications du gestionnaire et du client personnel

John, étant le magicien iOS qu'il est, a terminé ces applications dans les 12 premières heures du hackathon ! Il a vraiment excellé dans la conception d'applications conviviales et accessibles.

#### **L'application du gestionnaire**

![Image](https://cdn-media-1.freecodecamp.org/images/1*-mxfk-c6IMhkviUW-91isw.png)

Cette application iPad inscrivait de nouveaux clients dans notre API Kairos et notre base de données Firebase. Elle affichait également tous les clients dans le magasin et l'inventaire des articles du magasin. La capacité d'interagir directement avec la base de données Firebase et d'observer les changements apportés (par exemple, lorsque l'attribut `in_store` d'un client passe de `true` à `false`) a rendu ce processus relativement indolore. L'application était un excellent ajout grand public à notre démonstration.

#### L'application de shopping personnelle

![Image](https://cdn-media-1.freecodecamp.org/images/1*3kMsmAdlwvkbb7zfvppvsA.png)

Une fois le client inscrit, nous lui remettions un téléphone avec cette application installée. Ils se connectaient avec leur visage (Kairos les reconnaissait et les authentifiait). Toute mise à jour de leur panier serait affichée instantanément sur le téléphone. En quittant le magasin, le client recevait également une notification push sur ce téléphone indiquant le montant total qu'il avait dépensé.

### Le présentoir d'articles, les capteurs et la caméra

Soheil et Ruslan ont travaillé sans relâche pendant des heures pour perfectionner la conception de l'appareil de l'étagère d'articles et les scripts Python sous-jacents du Pi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x8ClNraW0zWDkr4lMWcpIw.png)
_L'appareil de l'étagère d'articles. Trois articles positionnés en rangées, une tour pour la caméra de sécurité et des capteurs ultrasoniques positionnés à l'arrière_

Il y avait trois articles positionnés en rangées. À la fin de deux rangées, un capteur de proximité ultrasonique était attaché. Nous n'avions que deux capteurs ultrasoniques, donc la troisième rangée avait un capteur de lumière sous les articles, qui ne fonctionnait pas aussi bien. Les capteurs ultrasoniques étaient connectés au Raspberry Pi qui traitait les lectures de la distance par rapport à l'objet le plus proche via des scripts Python simples (soit l'article le plus proche, soit la fin du présentoir). Le capteur de lumière détectait un état "sombre" ou "clair" (sombre si l'article était au-dessus, clair sinon).

Lorsque qu'un article était soulevé, la lecture du capteur changerait et déclencherait une mise à jour du stock de l'article dans la base de données. La caméra (téléphone Android) positionnée en haut de la tour détecterait ce changement et tenterait de reconnaître le client prenant l'article. L'article serait alors instantanément ajouté au panier de ce client.

### Les caméras d'entrée et de sortie

J'ai choisi d'utiliser des téléphones Android comme nos caméras de reconnaissance faciale, en raison de mon expertise relative avec Android et du couplage facile que les téléphones fournissent lors de la prise d'images et de leur traitement.

Les téléphones étaient installés des deux côtés d'un trépied de caméra, un côté à l'entrée du magasin et l'autre à la sortie du magasin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*k-WY9QPGAuQocOBCjHhrWw.png)
_Un trépied de caméra, deux téléphones et beaucoup de ruban adhésif_

Google dispose d'une API [Face API](https://developers.google.com/vision/) incroyablement utile qui implémente un pipeline natif pour détecter les visages humains et d'autres attributs utiles connexes. J'ai utilisé cette API pour gérer le travail lourd de la reconnaissance faciale.

En particulier, l'API fournissait une distance approximative d'un visage détecté par rapport à la caméra. Une fois que le visage d'un client était à une distance proche, je prenais une photo du client, la vérifiais par rapport à l'API Kairos pour m'assurer que le client existait dans notre base de données, puis mettais à jour la base de données Firebase avec le statut en magasin du client.

J'ai également ajouté une salutation personnalisée de synthèse vocale lors de la reconnaissance du client. Cela a vraiment impressionné tout le monde qui l'a utilisé.

Le résultat de cette implémentation peut être vu [ici](https://www.youtube.com/watch?v=XgtPey1TSIE) :

Une fois que le client quittait le magasin, l'état de détection de sortie de l'application Android était responsable de la récupération des articles que le client avait pris dans la base de données, du calcul du montant total que le client avait dépensé, puis de l'envoi d'une notification push à l'application personnelle du client via Firebase Cloud Messaging.

Sur les 36 heures, nous avons dormi environ 6 heures. Nous avons passé tout notre temps confinés dans une salle de classe au milieu du centre-ville de Toronto. Il y avait d'innombrables bugs frustrants et des obstacles d'implémentation que nous avons dû surmonter. Il y avait quelques bugs dans notre démonstration que vous avez probablement remarqués, comme les caméras qui ne reconnaissaient pas plusieurs personnes dans la même prise de vue.

Nous aurions également aimé implémenter des fonctionnalités supplémentaires, comme détecter les clients qui remettent des articles sur le présentoir et ajouter une plus grande variété d'articles.

Notre projet a finalement remporté la première place au hackathon. Nous avons mis en place un stand interactif pendant une heure (le château de boîtes Chipotle que l'on peut voir dans l'image de titre) et plus d'une centaine de personnes ont traversé notre magasin. Les gens s'inscrivaient avec une photo, se connectaient à l'application de shopping, entraient dans le magasin, prenaient un article, sortaient et recevaient instantanément une notification de leur facture. Pas de caissiers, pas de files d'attente, pas de reçus, et une expérience utilisateur très agréable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_J9ngCwl2XZLdLgHZeVJuA.jpeg)
_Faire visiter notre magasin à un client_

J'étais fier de la manière dont notre équipe a joué sur les forces de chaque individu et a créé un projet IoT full-stack bien assemblé en l'espace de quelques heures. C'était un sentiment incroyablement gratifiant pour tout le monde, et c'est quelque chose que j'espère reproduire dans ma carrière à l'avenir.

J'espère que cela vous a donné un aperçu de ce qui se passe derrière les scènes d'un grand projet de hackathon, rapidement prototypé et bricolé comme EZShop.

**Suivez-moi sur [Twitter](https://twitter.com/SubhanNadeem19) et [Medium](https://medium.com/@subhan_nadeem) si vous êtes intéressé par des articles plus détaillés et informatifs comme celui-ci ! Je suis toujours ouvert à me connecter et à apprendre d'autres développeurs de logiciels.**

**Le projet est open-source et peut être trouvé sur Github [ici](https://github.com/subhan-nadeem/EZShop). Attention, le code de hackathon n'est pas joli !**