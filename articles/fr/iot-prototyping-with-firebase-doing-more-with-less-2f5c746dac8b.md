---
title: 'Prototypage IoT avec Firebase : comment faire plus avec moins'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-19T13:23:15.000Z'
originalURL: https://freecodecamp.org/news/iot-prototyping-with-firebase-doing-more-with-less-2f5c746dac8b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ttEuxmPhOI8obezR7bn6tg.jpeg
tags:
- name: arduino
  slug: arduino
- name: Firebase
  slug: firebase
- name: Internet of Things
  slug: internet-of-things
- name: iot
  slug: iot
- name: platformio
  slug: platformio
seo_title: 'Prototypage IoT avec Firebase : comment faire plus avec moins'
seo_desc: 'By Bayrem Gharssellaoui

  IoT is all about connecting devices, or “things” as you may call them, to the internet
  and then analyzing data collected from these devices in order to extract an added
  value. In this article you’ll discover how to benefit fro...'
---

Par Bayrem Gharssellaoui

L'IoT consiste à connecter des appareils, ou des "choses" comme vous pourriez les appeler, à Internet, puis à analyser les données collectées à partir de ces appareils afin d'en extraire une valeur ajoutée. Dans cet article, vous découvrirez comment bénéficier de [Firebase](https://firebase.google.com/) lors de la réalisation d'un projet IoT et comment il peut vous aider à développer des prototypes IoT beaucoup plus rapidement et plus facilement que les méthodes traditionnelles. Vous développerez également votre propre projet IoT et l'hébergerez dans Firebase.

### Avant Firebase Realtime Database

La plupart de [mes projets IoT](http://kaizoku.azurewebsites.net/) nécessitent un moyen de communication entre les différents points de terminaison. Ces points de terminaison peuvent être n'importe quoi, des appareils et services aux applications, et finalement les données doivent être stockées quelque part pour un traitement et une analyse ultérieurs.

Donc, supposons que vous souhaitez construire un système IoT où un appareil mesurera les valeurs de température et d'humidité à partir de capteurs et les enverra à un service de base de données pour les stocker. Ensuite, vous souhaitez avoir une application web qui récupérera ces valeurs et les affichera dans un tableau de bord. Assez simple, n'est-ce pas ?

La manière facile et légère de procéder est de configurer un courtier [MQTT](https://www.hivemq.com/mqtt-essentials/) qui agira comme un hub et redirigera tous les messages entrants **publiés** par l'appareil vers tous les clients **abonnés**, comme l'application web dans ce cas.

Maintenant, la question ici est : comment l'application web peut-elle afficher les données ? Cela signifie-t-il qu'elle affichera les messages provenant directement du courtier ou qu'elle récupérera les données à partir d'un service de base de données ?

Supposons que vous souhaitiez que l'application fasse les deux choses : afficher les données provenant du courtier en temps réel **et** récupérer les données à partir de la base de données. Dans ce cas, vous pouvez penser à 2 façons (en fait, il existe de nombreuses façons différentes) d'y parvenir :

**Première solution :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*5NM__yb36ftzOmIvLtBc-A.png)

En utilisant cette architecture, l'appareil publiera d'abord ses données vers le courtier, puis il enverra une requête HTTP au service web de la base de données pour sauvegarder les données. Pour cette solution, l'appareil doit implémenter 2 clients : un client MQTT et un client HTTP.

**Deuxième solution :**

![Image](https://cdn-media-1.freecodecamp.org/images/1*qOsO6-Hupd-Eidwdw66X-Q.png)

L'autre façon de procéder est que l'appareil enverra ou publiera ses données vers le courtier, puis le courtier (comme prévu) redirigera ce message vers tous les abonnés connectés, comme l'application web. Mais cette fois, il y a un autre abonné connecté qui représente un moteur d'API qui acceptera ces données et les enverra au service web de la base de données pour qu'elles soient stockées.

Comme vous l'avez peut-être remarqué dans cette solution, le client HTTP est découplé de l'appareil et implémenté comme un service backend. Ainsi, vous rendez le programme de l'appareil beaucoup plus léger. C'est une chose importante à garder à l'esprit lors du développement sur des appareils IoT contraints où les ressources comme le CPU et la mémoire sont limitées.

Néanmoins, cette solution nécessite un travail supplémentaire pour développer le service backend qui agira comme une couche de persistance.

Y a-t-il une manière beaucoup plus facile de faire cela ?

### Firebase à la rescousse

![Image](https://cdn-media-1.freecodecamp.org/images/1*dFAUA_U6XtcCVDSDrd1eIQ.gif)

Comme vous l'avez peut-être vu ci-dessus, les choses peuvent devenir assez complexes assez facilement. Pour quelqu'un comme moi qui veut se lancer rapidement lors de la réalisation d'un prototype, cela peut prendre un peu de temps supplémentaire. C'est pourquoi, dans cette partie de l'article, vous verrez comment Firebase peut vous faciliter la vie et vous faire gagner beaucoup de temps lors du développement d'un prototype IoT.

Firebase offre de nombreux services cloud qui vont de l'authentification, au stockage, en passant par les fonctions cloud et l'hébergement de votre application web. Dans cet article, vous utiliserez 2 services : Realtime Database et Hosting.

Commençons par **Firebase Realtime Database**. La première chose qui vient à l'esprit en lisant ce nom de service est : d'accord, donc je sais ce qu'est une base de données, mais que signifie être en temps réel ici ?

Eh bien, selon Wikipedia :

> Une **base de données en temps réel** est un système de base de données qui utilise le [traitement en temps réel](https://en.wikipedia.org/wiki/Real-time_computing) pour gérer des charges de travail dont l'état change constamment. Cela diffère des bases de données traditionnelles contenant des données persistantes, principalement non affectées par le temps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uWzVNx2DCXbVc0xnxbSYwg.gif)

Dans le cas de Firebase Realtime Database, les clients seront connectés à la base de données et maintiendront une connexion bidirectionnelle ouverte via des [websockets](https://blog.teamtreehouse.com/an-introduction-to-websockets). Ensuite, si un client envoie des données à la base de données, cela sera déclenché et (dans ce cas) informera tous les clients connectés qu'il a été modifié en leur envoyant les nouvelles données sauvegardées.

Cette manière de travailler peut vous rappeler le courtier MQTT et la façon dont il réagit lorsqu'il reçoit un message d'un éditeur et l'envoie à tous les abonnés. La différence cette fois est l'ajout de la partie de persistance des données, qui est la base de données. Ainsi, comme vous pouvez le voir ici, vous n'avez pas besoin de router les messages vous-même en utilisant d'autres protocoles — Firebase Realtime Database s'en chargera, en plus de sa fonction normale de base de données. N'est-ce pas incroyable ?

En revenant au système IoT mentionné précédemment, vous pouvez maintenant connecter l'appareil à Firebase Realtime Database et le faire envoyer des données périodiquement à la base de données. De l'autre côté du système, vous avez une application web qui sera connectée au même service que l'appareil et recevra de nouvelles données chaque fois qu'il y a un changement dans la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zyS---O8Po4Gz1tVUYS4QQ.png)

Mais qu'en est-il de l'**hébergement** de l'application web ?

Firebase offre un service d'hébergement que vous pouvez utiliser pour héberger votre application plutôt que de gérer votre propre serveur web et de traiter les configurations de déploiement et de réseau. Le bon côté est qu'il est gratuit (mais limité) et assez facile à utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VESaHfq7jgk8aeDyH2kFgg.png)

Maintenant, pour la partie que vous attendez tous. Dans cette démonstration, vous utiliserez l'exemple discuté tout au long de cet article et le mettrez en vie.

Si vous vous souvenez, le système IoT est composé de **2 points de terminaison** : le premier est l'**appareil IoT** qui est responsable de l'envoi des données de température et d'humidité à Firebase Realtime Database. Celui-ci communiquera à son tour avec le deuxième point de terminaison — l'**application web** — qui lira les données et les affichera sur un beau tableau de bord.

Je vais diviser ce projet en **3 étapes** pour qu'il soit plus facile à suivre.

### 1. Configuration de Firebase Realtime Database

Il n'y a rien de spécial dans cette étape. Vous devez simplement aller dans votre [console Firebase](https://console.firebase.google.com/) et créer un nouveau projet. Une fois votre projet prêt, allez dans la section de la base de données et assurez-vous de créer une base de données Realtime Database **et non une base de données Cloud Firestore**. Sélectionnez le mode test et procédez, car vous utiliserez cette base de données uniquement pour les tests et le prototypage, et non pour les solutions de production (vous pouvez donc ignorer l'avertissement rouge). Maintenant, la base de données devrait être prête à l'emploi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E-ny9SQDLjUGOiEn1ows8w.png)

### 2. Développement de l'application de l'appareil IoT

![Image](https://cdn-media-1.freecodecamp.org/images/1*ttEuxmPhOI8obezR7bn6tg.jpeg)

Lorsque l'on parle de développement de systèmes embarqués, on entend souvent des termes comme programmation bas niveau, assembleur, registres, gestion de la mémoire, etc. Ces termes et concepts sont liés aux spécificités matérielles avec lesquelles vous travaillez et peuvent changer d'un appareil à l'autre.

C'est pourquoi, lors du prototypage d'idées, vous n'avez pas le temps de vous plonger profondément dans ces spécificités et de les étudier en détail, car vous traiterez en même temps avec d'autres langages de haut niveau et donc d'autres façons de penser le code. Au lieu de cela, vous devriez avoir une idée générale claire de l'architecture et des caractéristiques de l'appareil et de la manière de les utiliser.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YQyb-Sopev0IYL9nRv1J-Q.gif)

Heureusement pour vous, il existe une plateforme spécialement conçue pour le prototypage et l'abstraction de toutes les fonctionnalités bas niveau du matériel. Oui, je parle de la célèbre **Arduino**.

[**Arduino - Accueil**](https://www.arduino.cc/)  
[_Plateforme de prototypage électronique open-source permettant aux utilisateurs de créer des objets électroniques interactifs._www.arduino.cc](https://www.arduino.cc/)

Notez ici que lorsque je parle d'Arduino, je fais référence au **Framework Arduino** avec son IDE, ses compilateurs et ses bibliothèques — et non à la carte.

Ainsi, vous utiliserez Arduino pour programmer la carte, mais quelle carte, demandez-vous ? Eh bien, vous avez besoin d'une carte capable d'interfacer avec des capteurs et de mesurer des valeurs physiques comme la température. Elle doit également être capable de se connecter à Internet afin d'envoyer ces données à la base de données. Enfin, elle doit pouvoir être programmée en utilisant le framework Arduino.

Il existe une variété de cartes sur le marché qui peuvent accomplir ces tâches. Certaines d'entre elles sont des cartes Arduino et d'autres sont des cartes compatibles Arduino.

Dans cette démonstration, vous utiliserez le célèbre **NodeMCU**, une carte compatible Arduino. Elle est basée sur le **ESP8266** SoC, une puce produite par le fabricant chinois basé à Shanghai, Espressif Systems. Cette carte est attrayante pour les développeurs, car des unités individuelles peuvent être achetées pour aussi peu que 3 $.

#### Notre équipement

Bien que la plateforme Arduino offre un IDE pour la programmation et le téléchargement de code sur les cartes, il n'est pas très convivial pour les développeurs car il ne fournit aucune fonctionnalité d'intelliSense ou de débogage. C'est pourquoi, pour la plupart de mes projets IoT, j'utilise un environnement appelé **PlatformIO**.

[**PlatformIO : Un écosystème open source pour le développement IoT**](https://platformio.org/)  
[_Système de construction multiplateforme et gestionnaire de bibliothèques. IDE multiplateforme et débogueur unifié. Tests unitaires à distance et
2026_platformio.org](https://platformio.org/)

C'est un écosystème open source pour le développement IoT, et devinez quoi ? Il supporte le Framework Arduino. Ainsi, vous pouvez l'utiliser pour écrire du code Arduino, le compiler et le télécharger sur la carte. Enfin, le côté cool de PlatformIO est qu'il vient comme une **extension** que vous pouvez utiliser dans **Atom** ou **VScode**, afin que vous puissiez l'utiliser aux côtés des autres fonctionnalités de votre IDE (Atom ou VScode). Je vous recommande vivement de regarder ces 2 tutoriels vidéo YouTube pour configurer et vous familiariser avec l'environnement.

Assez parlé — commençons :

#### Développement du Firmware pour NodeMCU

[**kaizoku-619/firebase_nodemcu**](https://github.com/kaizoku-619/firebase_nodemcu)  
[_Client Arduino Firebase Nodemcu développé pour envoyer des données DHT11 à Firebase Realtime Database 
2026_github.com](https://github.com/kaizoku-619/firebase_nodemcu)

Avant de plonger dans le développement du firmware, parlons de la configuration électronique.

Si vous vous souvenez de l'exemple précédent, l'appareil IoT mesurera les valeurs de température et d'humidité à partir d'un capteur et les enverra au cloud. Dans ce cas, cela signifie que le **NodeMCU** lira les valeurs de température et d'humidité à partir du module capteur **DHT11** et les enverra à Firebase. Le module **DHT11** sera utilisé ici car il est bon marché et ne nécessite aucun composant électronique supplémentaire pour fonctionner.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B6nyhGw-sarcmZgLA2etXg.png)
_Schéma de câblage_

Comme vous pouvez le voir sur le schéma de câblage ci-dessus, le DHT11 est connecté à la carte avec 3 fils **GND**, **3.3V** et **Signal de données** au milieu. Connectez la broche de données à l'une des broches **Dx** sur la carte et vous avez terminé le câblage.

Maintenant que le câblage est terminé, vous pouvez commencer à coder le firmware en utilisant PlatformIO.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DIOV2vSxZKjRO6WgP2nzjA.gif)
_Nous n'écrivons pas en Go mais j'aime le GIF_

Mais avant de vous lancer directement dans l'écriture de code, arrêtons-nous un moment et réfléchissons à ce que le programme doit faire.

Ainsi, la première chose que l'appareil doit faire est de se connecter à Internet. Pour cela, il doit **se connecter au point d'accès WiFi**. Une fois en ligne, il doit **ouvrir une connexion avec Firebase**. Après cela, l'appareil **lira les valeurs de température et d'humidité** à partir du capteur et enfin **publiera les données**.

Voici une liste ordonnée des tâches :

_(Notez que le terme **tâche** est utilisé ici pour désigner une fonctionnalité d'un bloc de code et non une tâche dans un système d'exploitation temps réel comme les tâches FreeRTOS.)_

**1. Se connecter au WiFi**  
**2. Ouvrir une connexion avec Firebase**  
**3. Lire les valeurs du capteur**  
**4. Publier les valeurs sur Firebase**

Commençons par la première tâche :

* **Se connecter au WiFi :**

Cette fonction commence par imprimer le **SSID** (nom du point d'accès) et mettre le NodeMCU en mode station plutôt qu'en mode point d'accès. Ensuite, il continue de charger jusqu'à ce qu'il se connecte au point d'accès. Le SSID et le **MOT DE PASSE** sont deux constantes définies dans un autre fichier comme vous le verrez plus tard.

* **Ouvrir une connexion avec Firebase :**

Cette fonction est très simple : elle prend 2 paramètres **FIREBASE_HOST** et **FIREBASE_AUTH**. Ce sont également deux constantes définies dans un autre fichier.

* **Lire les valeurs du capteur :**

Vous commencez par définir 2 constantes pour le **type de capteur DHT** et la broche. Après cela, vous créez un objet DHT en passant ces 2 constantes au constructeur DHT. Enfin, vous utilisez les méthodes de l'objet **readHumidity()** et **readTemperature()** pour lire l'humidité et la température respectivement.

* **Publier les valeurs sur Firebase :**

Ici, la méthode **pushInt()** de la classe Firebase est utilisée pour envoyer un entier à Firebase et, en cas d'erreur, l'imprimer.

Et maintenant, vous avez terminé les tâches ! Il ne reste plus qu'à rassembler ces tâches dans un croquis Arduino propre.

Commencez par créer un nouveau projet dans PlatformIO comme montré ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*xwXxvU1FbJBSS6yypAiKHA.png)

Ensuite, vous devez **installer les bibliothèques** nécessaires pour le projet. Notez que dans ce cas, vous installerez les bibliothèques **localement**, ce qui signifie qu'elles ne sont disponibles que pour ce projet. C'est une bonne pratique si vous décidez un jour d'utiliser une autre version de la bibliothèque dans un autre projet.

Allez à la page d'accueil de PlatformIO → Bibliothèques et recherchez firebase. FirebaseArduino apparaîtra, cliquez dessus. Mais **ne cliquez pas sur le bouton installer**, cliquez plutôt sur le **
2026** à côté d'installer et choisissez le projet dans lequel installer la bibliothèque. Ensuite, cliquez enfin sur installer. Répétez ce processus pour la bibliothèque **DHT**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gyXxo1VKPLWcqfHlkV_oLQ.png)

Copiez ce code dans le fichier **main.cpp** :

Vous souvenez-vous du fichier contenant les identifiants pour le WiFi et Firebase ? Allez dans le dossier include et créez un nouveau fichier **Creds.h** et copiez ce code dedans. N'oubliez pas de **changer** le code selon **vos identifiants**.

Et voilà ! Téléchargez le firmware sur **NodeMCU** et votre appareil devrait être capable d'envoyer des données à **Firebase Realtime Database**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dx4qV5dLbGQoNYcwYifa5w.png)

### 3. Développement et hébergement de l'application web

[**kaizoku-619/firebase_iot_web**](https://github.com/kaizoku-619/firebase_iot_web)  
[_Client d'application web Firebase connecté à la base de données en temps réel Firebase récupérant les valeurs des capteurs 
2026_github.com](https://github.com/kaizoku-619/firebase_iot_web)

Maintenant que l'appareil IoT est prêt et envoie des données à la base de données en temps réel, vous pouvez passer à l'autre point de terminaison du système, l'application web. Elle recevra les données de Firebase et les affichera sur un tableau de bord.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rjf3-ZGcqjg_TUPOPmllOw.png)

Vous commencerez par développer l'application localement et finirez par la déployer.

Commencez par configurer le projet.

#### **Installation de Firebase CLI :**

L'**interface de ligne de commande Firebase** (CLI) nécessite **Node.js** et **npm** (le gestionnaire de paquets Node). Une fois qu'ils sont installés, vous procédez à l'installation de Firebase CLI en utilisant npm en exécutant :

```
npm install -g firebase-tools
```

Vous pouvez suivre la vidéo pour compléter la configuration du projet.

Une fois la configuration du projet terminée, votre répertoire devrait ressembler à ceci :

```

251c
2500
2500 database.rules.json
251c
2500
2500 firebase.json
2514
2500
2500 public   
251c
2500
2500 404.html   
2514
2500
2500 index.html
```

Commencez par construire l'**interface utilisateur du tableau de bord**. Ce sera le fichier **index.html**. Ouvrez le fichier et modifiez-le pour qu'il ressemble à ceci :

Il s'agit d'une simple page **HTML** conçue à l'aide de [Bootstrap Material Design](https://fezvrasta.github.io/bootstrap-material-design/). Elle se compose de **2 éléments Card**, l'un pour afficher l'humidité et l'autre pour afficher la température.

En ce qui concerne la partie Firebase ici, vous commencez par importer la dépendance firebase dans la balise script à l'intérieur de la balise head. Enfin, lorsque la page a fini de charger, elle appelle **app.js**.

Maintenant que l'interface utilisateur du tableau de bord est prête, vous pouvez passer à **app.js** où vous implémentez la connexion firebase et votre logique métier. Dans le même répertoire, créez un nouveau fichier appelé **app.js** et copiez ce code :

Le script commence par créer un objet de configuration. La meilleure façon est de le copier directement depuis le projet firebase dans la console firebase. Pour ce faire, accédez à votre console firebase et allez dans les paramètres du projet firebase. Ensuite, faites défiler vers le bas et cliquez sur l'icône **<**;/> comme montré ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UOd3xtXrWw291dCIP2I1zw.gif)

Je pense que le reste du code est auto-explicatif avec les commentaires.

Maintenant, votre application devrait être prête et vous pouvez la tester localement avec la commande suivante :

```
firebase serve
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZGnT6vNho7_lNuQNvcokBw.gif)

Notez qu'au démarrage, l'application récupérera les dernières valeurs de température et d'humidité de la base de données. Super ! L'application fonctionne localement, mais jusqu'à présent, elle ne fonctionne que dans votre localhost et ne peut pas être accessible depuis l'extérieur. Cela signifie qu'il est temps de l'héberger sur le web en utilisant **Firebase Hosting**.

Mais avant de la déployer, il y a une dernière chose que vous devez faire. Allez dans le fichier **database.rules.json** et changez les règles de lecture et d'écriture en "**true**". Cette méthode n'est pas conseillée pour la production, car elle n'est pas sécurisée, mais elle convient à des fins de démonstration ici.

Avec cela fait, vous êtes prêt pour le déploiement :

```
firebase deploy
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*RUWH_VUFf_EJ2JVeUk6xWA.gif)

Et voilà ! Si vous êtes arrivé jusqu'ici, vous devriez maintenant avoir une application web en direct déployée et opérationnelle.

### Mettre tout ensemble

![Image](https://cdn-media-1.freecodecamp.org/images/1*NRl95CtTxUi8Os7D_WKgAA.gif)

Il est temps de tout rassembler et de tester le système. Branchez le **NodeMCU** à votre PC et téléchargez le croquis si vous ne l'avez pas déjà fait :

![Image](https://cdn-media-1.freecodecamp.org/images/1*neyIQF00mBE02W9aOw4ptg.gif)

Ouvrez l'application web et la base de données firebase et regardez-la changer en temps réel avec les valeurs envoyées par l'appareil.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1JIi7SbvkC6LAePZiuRtjA.gif)

Maintenant, ouvrez le **moniteur série** et regardez les données envoyées de l'appareil à l'application web. Notez que vous pouvez ouvrir la console dans le navigateur pour voir les valeurs reçues. Ici, j'utilise [Gtk Serial port terminal](https://linux.die.net/man/1/gtkterm) avec un débit de 115200 bps, mais vous pouvez utiliser le **PlatformIO** intégré Serial Monitor ou tout autre outil de votre choix.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oPKH60n5_9kQfIIdtx_Hjg.gif)

### Dépannage

J'ai rencontré un problème lors du développement de l'application sur l'**ESP8266** (et cela m'a pris un certain temps pour le comprendre). Même lorsque tout était configuré correctement (connexion WiFi, hôte Firebase, clé secrète), l'**ESP8266 ne pouvait pas se connecter à Firebase**. Cela était dû à la **mauvaise empreinte digitale** dans le fichier **FirebaseHttpClient.h** de la bibliothèque Firebase. Vous devez la remplacer par votre propre empreinte digitale. Si vous avez installé la bibliothèque localement en utilisant **PlatformIO**, vous pouvez trouver le fichier dans ce chemin :

```
votre_dossier_de_projet/.piolibdeps/FirebaseArduino_ID1259/src/
```

Pour **générer** une empreinte digitale, allez sur ce site web et copiez votre lien d'hôte Firebase sans la partie https et cliquez sur Fingerprint Site (le mien est :   
medium-iot-project.firebaseio.com) :

[**GRC | Empreintes digitales des certificats de serveur web SSL TLS HTTPS**](https://www.grc.com/fingerprints.htm)  
[_Service d'empreintes digitales des certificats de serveur web HTTPS de GRC_www.grc.com](https://www.grc.com/fingerprints.htm)

Cela générera une empreinte digitale pour votre site, alors allez-y et copiez-la à la place de l'ancienne valeur **kFirebaseFingerprint[]** à l'intérieur du fichier **FirebaseHttpClient.h**. Cela devrait résoudre le problème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TuJignt5v3mYTnybtktJnw.gif)

### Conclusion

![Image](https://cdn-media-1.freecodecamp.org/images/1*HC62qJvM12Ey_u_CKA3uNQ.gif)

Félicitations si vous êtes arrivé jusqu'ici !

Nous n'avons fait qu'effleurer la surface ici. L'Internet des objets est une question d'expérimentation et d'exploration, alors je vous encourage à ne pas vous arrêter ici et à continuer à apprendre en faisant des erreurs et en trouvant des bugs dans votre code. Mais par-dessus tout, n'oubliez pas de vous amuser tout au long de votre parcours d'apprentissage.

### Références

[**Firebase Realtime Database | Firebase Realtime Database | Firebase**](https://firebase.google.com/docs/database/)  
[_Stockez et synchronisez des données avec notre base de données cloud NoSQL. Les données sont synchronisées sur tous les clients en temps réel et restent disponibles
2026_firebase.google.com](https://firebase.google.com/docs/database/)[**PlatformIO : Un écosystème open source pour le développement IoT**](https://platformio.org/)  
[_Système de construction multiplateforme et gestionnaire de bibliothèques. IDE multiplateforme et débogueur unifié. Tests unitaires à distance et
2026_platformio.org](https://platformio.org/)[**Arduino - Accueil**](https://www.arduino.cc/)  
[_Plateforme de prototypage électronique open-source permettant aux utilisateurs de créer des objets électroniques interactifs._www.arduino.cc](https://www.arduino.cc/)[**Bootstrap Material Design**](https://fezvrasta.github.io/bootstrap-material-design/)  
[_La bibliothèque Material Design HTML, CSS et JS la plus populaire au monde._fezvrasta.github.io](https://fezvrasta.github.io/bootstrap-material-design/)[**esp8266/Arduino**](https://github.com/esp8266/Arduino)  
[_Noyau ESP8266 pour Arduino. Contribuez au développement de esp8266/Arduino en créant un compte sur GitHub._github.com](https://github.com/esp8266/Arduino)[**FirebaseExtended/firebase-arduino**](https://github.com/FirebaseExtended/firebase-arduino)  
[_Exemples Arduino pour Firebase. Contribuez au développement de FirebaseExtended/firebase-arduino en créant un compte sur
2026_github.com](https://github.com/FirebaseExtended/firebase-arduino)[**GRC | Empreintes digitales des certificats de serveur web SSL TLS HTTPS**](https://www.grc.com/fingerprints.htm)  
[_Service d'empreintes digitales des certificats de serveur web HTTPS de GRC_www.grc.com](https://www.grc.com/fingerprints.htm)