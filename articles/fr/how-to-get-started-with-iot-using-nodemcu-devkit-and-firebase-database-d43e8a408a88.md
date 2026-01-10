---
title: Comment commencer avec l'IoT en utilisant NodeMCU Devkit et la base de données
  Firebase
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-24T16:21:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-started-with-iot-using-nodemcu-devkit-and-firebase-database-d43e8a408a88
coverImage: https://cdn-media-1.freecodecamp.org/images/1*St_hPlFBBczBVkmPtB0RqQ.jpeg
tags:
- name: internet
  slug: internet
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: projects
  slug: projects
- name: technology
  slug: technology
seo_title: Comment commencer avec l'IoT en utilisant NodeMCU Devkit et la base de
  données Firebase
seo_desc: 'By Jibin Thomas


  “The Internet will disappear. There will be so many IP addresses, so many devices,
  sensors, things that you are wearing, things that you are interacting with, that
  you won’t even sense it. It will be part of your presence all the tim...'
---

Par Jibin Thomas

> **_L'Internet va disparaître. Il y aura tellement d'adresses IP, tellement d'appareils, de capteurs, de choses que vous portez, de choses avec lesquelles vous interagissez, que vous ne le sentirez même pas. Cela fera partie de votre présence tout le temps. Imaginez que vous entrez dans une pièce, et la pièce est dynamique. Et avec votre permission et tout cela, vous interagissez avec les choses qui se passent dans la pièce._**

De nos jours, de nombreux appareils que nous utilisons quotidiennement sont connectés à Internet comme les téléviseurs, les enceintes intelligentes, les réfrigérateurs, etc. Ces appareils étendent leurs fonctions principales, ce qui leur permet d'interagir avec d'autres appareils sur Internet et d'être contrôlés à distance.

Vous pouvez construire vos propres appareils IoT en utilisant quelques capteurs et microcontrôleurs. Il existe de nombreuses cartes de développement qui vous aideront à commencer avec l'IoT comme Arduino, NodeMCU, Raspberry Pi, etc. Vous pouvez automatiser votre maison en construisant à partir de ces appareils.

Dans cet article, nous allons utiliser le kit de développement NodeMCU et Firebase pour allumer et éteindre une LED à distance. Le kit de développement NodeMCU et Firebase sont les meilleures combinaisons pour commencer à construire des projets IoT. NodeMCU est bon marché et dispose d'un wifi intégré pour la connectivité Internet, et le plan gratuit de Firebase est plus que suffisant.

### Configuration de l'environnement de développement

1. Nous allons utiliser l'IDE Arduino pour écrire du code et nous allons flasher le code sur l'appareil. Téléchargez la dernière version de l'IDE [ici](https://www.arduino.cc/en/main/software).

2. Puisque nous utilisons NodeMCU qui n'est pas officiellement supporté par l'IDE Arduino, nous devons ajouter le fichier JSON de l'appareil. Dans l'IDE Arduino, ajoutez cette URL dans

> Fichier > Préférences > URLs de gestion de cartes supplémentaires

> [http://arduino.esp8266.com/stable/package_esp8266com_index.json](http://arduino.esp8266.com/stable/package_esp8266com_index.json)

3. Sélectionnez votre carte dans

> Outils > Carte > NodeMCU 1.0

4. Pour utiliser la base de données Firebase dans NodeMCU, vous devez télécharger la bibliothèque firebase-arduino qui abstrait l'API REST de Firebase. [Téléchargez firebase-arduino ici](https://github.com/FirebaseExtended/firebase-arduino.git).

5. Incluez le fichier zip téléchargé dans l'IDE Arduino.

> Croquis > Inclure une bibliothèque > Ajouter une bibliothèque .ZIP > Sélectionnez le fichier zip

6. Vous devez également installer la bibliothèque ArduinoJson qui peut être téléchargée depuis l'IDE Arduino lui-même.

Note : La version de la bibliothèque ne doit pas être 6.x.x — utilisez la dernière version 5.x.x

> Croquis > Inclure une bibliothèque > Gérer les bibliothèques > Recherchez ArduinoJson par Benoit Blanchon

### Configuration de la base de données Firebase

7. Créez un nouveau projet Firebase depuis la [console](https://console.firebase.google.com/) et dirigez-vous vers la section de la base de données. Sélectionnez la base de données en temps réel Firebase.

8. Copiez le secret de la base de données pour l'authentification depuis le Panneau des paramètres > Comptes de service.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PQUqPFsKYw4XFWX3cFV-LA.png)
_Secret de la base de données_

9. Ajoutez un nœud led à la base de données Firebase. Cette valeur décidera d'allumer ou d'éteindre la LED.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cpN78XVvwFe6O0AcoCBHiA.png)

### Configuration de l'IDE Arduino et de la base de données Firebase pour qu'ils fonctionnent ensemble

Maintenant que toutes les procédures de configuration sont terminées, commençons à coder.

Vous devez créer une macro pour l'URL de votre base de données et le secret Firebase que vous avez copié à l'étape 8.

> #define FIREBASE_HOST "votrebasefirebase.firebaseio.com"

> #define FIREBASE_AUTH "*****"

Pour simplifier, nous allons écrire un code simple pour allumer et éteindre une LED à distance

10. La borne positive de la LED doit être connectée à la broche D1 et la borne négative à la broche de masse de NodeMCU.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lTdcYh-7O5uECpw8MczYow.png)

11. Téléchargez votre code depuis l'IDE Arduino.

> Croquis > Télécharger

12. Essayez maintenant de changer la valeur de la base de données en vrai ou faux. La LED devrait maintenant commencer à s'allumer et à s'éteindre. De plus, vous pouvez étendre ce projet en créant une application web qui basculera la LED au lieu de changer manuellement la valeur dans la base de données.

Maintenant que vous comprenez les bases de la connexion de NodeMCU à Internet et de son contrôle à distance, commencez à bidouiller de nouveaux projets avec celui-ci.