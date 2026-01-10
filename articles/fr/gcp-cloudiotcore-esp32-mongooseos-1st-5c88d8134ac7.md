---
title: Comment vérifier la météo en utilisant GCP-Cloud IoT Core avec ESP32 et Mongoose
  OS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-28T22:07:21.000Z'
originalURL: https://freecodecamp.org/news/gcp-cloudiotcore-esp32-mongooseos-1st-5c88d8134ac7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GGNvAgxLJXeagpiyQnlHvQ.jpeg
tags:
- name: Firebase
  slug: firebase
- name: google cloud
  slug: google-cloud
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment vérifier la météo en utilisant GCP-Cloud IoT Core avec ESP32 et
  Mongoose OS
seo_desc: 'By Olivier LOURME

  This post on freecodecamp.org is not maintained. The most up to date version is
  on Medium: https://medium.com/free-code-camp/gcp-cloudiotcore-esp32-mongooseos-1st-5c88d8134ac7

  This post is a step-by-step tutorial for newbies to Goog...'
---

Par Olivier LOURME

Cet article sur freecodecamp.org n'est pas maintenu. La version la plus à jour se trouve sur Medium : [https://medium.com/free-code-camp/gcp-cloudiotcore-esp32-mongooseos-1st-5c88d8134ac7](https://medium.com/free-code-camp/gcp-cloudiotcore-esp32-mongooseos-1st-5c88d8134ac7)

Cet article est un tutoriel pas à pas pour les débutants sur **Google Cloud Platform-Cloud IoT Core**. Les appareils sont des **puces Wifi ESP32** exécutant **Mongoose OS**. Pour suivre ce tutoriel, les concepts puis la configuration d'un simple **système IoT** **mesurant les données météorologiques** sont décrits.

**Démonstration en direct ici :** [https://hello-cloud-iot-core.firebaseapp.com/](https://hello-cloud-iot-core.firebaseapp.com/)

**GitHub pour la dernière section** _(Journalisation, stockage et visualisation des données météorologiques avec Firebase) **est ici :**_ [https://github.com/olivierlourme/iot-store-display](https://github.com/olivierlourme/iot-store-display)

**Cet article est complété par un second :** voir [ici](https://medium.com/@o.lourme/gcp-cloudiotcore-esp32-mongooseos-2nd-config-state-encrypt-7c5e937e5be9).

### Introduction

#### 1) Historique

Dans une série précédente de 3 articles [[lien](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-1-a07db495ac5f), [lien](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-2-14b0609d3f5e), [lien](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-3-644048e90ca4)], nous avons utilisé une **puce Wifi ESP8266** pour mesurer régulièrement la luminosité et alimenter une base de données avec les données obtenues. L'ensemble de données a finalement été tracé en direct sur une application web (voir le tracé en direct ici : [[lien](https://esp8266-rocks.firebaseapp.com/)]). Nous avons massivement utilisé les **produits Firebase** (Realtime Database, Cloud Functions, SDK et Hosting) pour atteindre nos objectifs.

Ce projet fonctionne bien, il consomme très peu d'énergie et nous avons apprécié le développer — mais :

* **Ce projet était adapté pour gérer seulement quelques capteurs connectés**. La configuration d'un ensemble de cent capteurs nécessiterait beaucoup d'interventions manuelles (rigoureuses) et leur surveillance serait également difficile. En effet, il n'y a pas d'endroit central où nous pouvons gérer notre système.
* **Arduino IDE** et **Arduino core pour ESP8266** étaient excellents pour découvrir ESP8266 mais ils sont **rapidement insuffisants** : La gestion des fichiers de l'IDE est vraiment basique, il n'y a qu'un seul programme dans la puce, et **il n'y a pas de système d'exploitation** **fournissant des APIs utiles pour l'IoT**.
* **FirebaseArduino** **library**, permettant à un ESP8266 de pousser des données vers une Firebase Realtime Database, **était expérimentale**. Certaines fonctionnalités comme l'authentification devraient être améliorées. Pour l'instant, le type d'authentification "secret" que nous avons utilisé donne à ESP8266 des droits d'administrateur sur toute la base de données !
* Finalement, **la mémoire flash SPI ESP8266 n'a pas été conçue pour être chiffrée**. Dans notre premier article [[lien](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-1-a07db495ac5f)], nous avons montré à quel point il était facile de récupérer un mot de passe Wifi en lisant cette mémoire.

> En un mot, ce projet passé ne pouvait pas être utilisé dans un contexte industriel. C'était plus un prototype pour une preuve de concept. Nous avons beaucoup appris avec, mais aujourd'hui **nous aimerions développer une solution professionnelle et entièrement sécurisée capable de gérer simplement un grand nombre de capteurs connectés**.

C'est pourquoi nous avons décidé de :

* **étudier Google Cloud Platform-Cloud IoT Core** [[lien](https://cloud.google.com/iot-core/)] pour gérer notre système : configuration des appareils, provisionnement, authentification et surveillance ;
* **passer de ESP8266 à ESP32**, qui offre le chiffrement de la mémoire ;
* **exécuter Mongoose OS** [[lien](https://mongoose-os.com/)] dans nos ESP32. Ce système d'exploitation accepte les programmes écrits en Javascript (JS) et fournit de nombreuses APIs pour gérer le temps, le protocole MQTT, les capteurs, le provisionnement, etc. Il est facile de l'interfacer avec les principales plateformes IoT, y compris Google Cloud Platform-Cloud IoT Core.

#### **2) Un mot sur la puce Wifi ESP32**

La puce Wifi ESP32 est la successeur de la célèbre ESP8266 que nous avons décrite ici : [[lien](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-1-a07db495ac5f)]. Comparée à celle-ci, chaque fonctionnalité est améliorée (vitesse jusqu'à 240 MHz, deux cœurs, 520 kiB de RAM, nombre de GPIOs, variété de périphériques, etc.) et il y a de nouvelles fonctionnalités (Bluetooth : legacy/BLE, **capacité de chiffrement de la mémoire flash de 4 MiB**, **accélération matérielle cryptographique** : AES, SHA-2, RSA, ECC, RNG). Il existe de nombreuses ressources sur le web concernant ESP32. La suivante traite de la **carte de développement ESP32 DEVKIT V1** que nous allons utiliser et donne son brochage : [[lien](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)].

Il y a aussi cette ressource extensive concernant la grande variété de puces ESP32 et de kits de développement : [http://esp32.net/](http://esp32.net/) . Sur leur page d'accueil, en recherchant "ESP32 DevKit" ou "GeekCreit", on trouve un lien vers le [schéma](https://github.com/SmartArduino/ESP/blob/master/SchematicsforESP32.pdf) de notre ESP32 DEVKIT V1. Cette carte de développement intègre une puce officielle Espressif ESP32-WROOM-32 et coûte environ 6€ chez Banggood.

### Concepts de base de l'IoT expliqués à travers notre cas d'utilisation

Alors, quel sera notre terrain de jeu pour tester tous ces nouveaux outils ?

> Pour illustrer les concepts de l'IoT à travers Cloud IoT Core, nous avons choisi de construire **une station météo** **rapportant l'humidité et la température de différents endroits**.

Pour simplifier, nous ne gérerons que 2 endroits : à l'intérieur de notre maison ("intérieur") et à l'extérieur de notre maison ("extérieur"). C'est à vous de gérer beaucoup plus d'endroits.

#### 1) Matériel du projet : ESP32 & DHT22

À chacun de ces endroits, nous installerons un capteur connecté ("un appareil") constitué d'un **capteur d'humidité/température DHT22** (description : [[lien](https://learn.adafruit.com/dht)], fiche technique : [[lien](https://cdn-shop.adafruit.com/datasheets/Digital+humidity+and+temperature+sensor+AM2302.pdf)], 4€ chez Banggood) connecté à une **carte de développement ESP32 DEVKIT V1**. Le DHT22 observe un type de protocole "1-Wire". Chaque ESP32 hébergera **Mongoose OS** comme système d'exploitation. Son installation sur un ESP32, un Hello, World! et un test avec un DHT22 sont donnés dans la section suivante ci-dessous.

Juste en dessous sont données les spécifications du DHT22. Ensuite, nous pensons que les chiffres de précision sont un peu optimistes, mais ce n'est pas notre préoccupation aujourd'hui.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WIxEy4NLdDr_2SVhcjmv0g.png)
_Caractéristiques du capteur DHT22 ([[lien](https://learn.adafruit.com/dht/overview" rel="noopener" target="_blank" title=")])_

Nous pouvons déjà construire l'assemblage suivant deux fois (un pour l'intérieur et un pour l'extérieur). Pour l'instant, l'alimentation proviendra du connecteur USB connecté à notre machine hôte. En production, l'alimentation peut provenir d'une batterie externe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*tFxxVtWwVH9gFajtrCWQ0w.png)
_Diagramme d'assemblage — ESP32 DEVKIT V1 et capteur DHT22 constituent un "appareil". Le brochage est ici : [[lien](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/" rel="noopener" target="_blank" title=")]_

C'est tout pour le matériel ! Le reste du projet utilise des **solutions serverless** de Google. Nous les décrivons maintenant...

#### 2) Architecture du projet : Cloud IoT Core & Firebase

Toute cette section "Architecture du projet" est théorique, il n'y a pas d'étape à effectuer. Son but est d'introduire le vocabulaire et les notions liés à l'IoT, plus spécifiquement lorsque ce domaine implique des solutions Google Cloud.

Voici l'architecture générale de notre projet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*PttQxTGMbDHCGwzCsWlZvA.png)
_Architecture du projet_

_Note :_ Il n'y a pas de **passerelle** entre nos appareils et Cloud IoT Core car ils "parlent" MQTT.

_Note :_ Les appareils peuvent également communiquer avec Cloud IoT Core via son **pont HTTP**. Comme il est moins performant que le **pont MQTT** (voir une comparaison : [[lien](https://cloud.google.com/iot/docs/concepts/protocols)]), nous allons désactiver cette communication plus tard lors de la configuration du registre. Limiter l'accès à ce qui est nécessaire est une bonne pratique.

Expliquons cette architecture en trois sections :

* "Des appareils à Cloud Pub/Sub" décrit l'architecture IoT classique de Google.
* "De Cloud Pub/Sub au stockage et à la visualisation des données" décrit les choix que nous avons faits pour exploiter les données.
* "Configuration et sujets d'état supplémentaires" complète cette présentation de l'architecture.

**Des appareils à Cloud Pub/Sub**

* Cloud IoT Core

**Cloud IoT Core** est le service Google Cloud Platform auquel chacun de nos **appareils enregistrés** enverra les données de température/humidité. Lorsqu'une telle donnée est envoyée, nous disons que **l'appareil publie un événement de télémétrie** (parfois également appelé un "message de télémétrie").

_Note :_ Les tarifs sont détaillés ici : [[lien](https://cloud.google.com/iot/pricing)]. Pour les petits projets avec quelques appareils, il y a peu de chances que vous soyez facturé.

* _MQTT_

Cette publication est effectuée via une **connexion MQTT**. MQTT est un protocole de messagerie basé sur la publication/abonnements ; la plupart du temps, il repose sur TCP [[lien](https://en.wikipedia.org/wiki/MQTT)] (ou mieux : sur TLS, lui-même reposant sur TCP). Le message de télémétrie doit être publié par l'appareil (un client MQTT) vers le "pont MQTT" de Cloud Iot Core (un serveur MQTT) dans un **sujet MQTT** dont le nom respecte impérativement ce format :

```
/devices/{device-id}/events
```

_Note :_ Les sous-dossiers dans le nom du sujet sont possibles. Nous n'aurons pas besoin de cette fonctionnalité ici, mais voir [[lien](https://cloud.google.com/iot/docs/how-tos/mqtt-bridge#publishing_telemetry_events)], car elle peut parfois être utile.

`{device-id}` est unique pour chaque appareil. Dans notre cas, Mongoose OS le crée à partir des 3 derniers octets de l'adresse MAC de l'ESP32. Par exemple, il pourrait être `esp32_ABB3B4`.

* _Qualité de Service (QoS)_

La spécification MQTT décrit trois **niveaux de Qualité de Service (QoS)**, lors de la publication dans un sujet ([[lien](https://cloud.google.com/iot/docs/how-tos/mqtt-bridge#quality_of_service_qos)]) :

> QoS 0, le message est livré au plus une fois ;

> QoS 1, le message est livré au moins une fois ;

> QoS 2, le message est livré exactement une fois.

Cloud IoT Core ne supporte pas QoS 2. Et QoS 1 est meilleur que QoS 0. Donc **QoS 1 est celui que nous allons adopter**. Mongoose OS peut le faire.

* _Sécurité_

Concernant la **sécurité**, dans notre contexte Mongoose OS/Cloud IoT Core, les communications MQTT sont faites via **TLS** ([[lien](https://cloud.google.com/iot/docs/how-tos/mqtt-bridge#mqtt_server)]), donc (1) l'appareil est assuré d'être connecté au serveur MQTT de Cloud IoT Core (les certificats de l'AC sont stockés dans le fichier `ca.pem` de Mongoose OS), (2) l'échange de données sera privé et (3) l'intégrité des données sera vérifiée. D'un autre côté, **l'authentification de l'appareil** ([[lien](https://cloud.google.com/iot/docs/how-tos/mqtt-bridge#device_authentication)]) avec Cloud IoT Core est effectuée avec une authentification par clé publique/privée par appareil utilisant des **JSON Web Tokens (JWT)**. L'appareil effectue la partie signature du JWT avec sa clé privée et Cloud IoT Core la valide en utilisant la clé publique associée. Les outils Mongoose OS gèrent cette génération et distribution de clés, nous verrons cela bientôt dans la section appelée "Enregistrement de l'appareil dans le projet Cloud IoT Core" située quelques paragraphes plus bas. Dans cette section, nous verrons également comment stocker en toute sécurité la clé privée sur l'appareil en effectuant un chiffrement de la mémoire (empêchant également l'ingénierie inverse).

_Note :_ Au-delà de l'authentification JWT de l'appareil, pour une sécurité supplémentaire, il est possible d'imposer TLS de Cloud IoT Core aux appareils (donc chaque appareil a également un certificat de clé publique, etc.). C'est une option que nous n'utiliserons pas, mais elle est décrite [ici](https://mongoose-os.com/docs/mongoose-os/api/net/mqtt.md) pour le côté Mongoose OS (voir "mutual TLS") et [ici](https://cloud.google.com/iot/docs/how-tos/credentials/verifying-credentials) pour le côté Cloud Iot Core. Il est bon de savoir que AWS IoT impose ce mutual TLS, sans condition ([[lien](https://docs.aws.amazon.com/iot/latest/developerguide/iot-security-identity.html)]).

* _Registre_

Les appareils partageant le même objectif sont regroupés au sein d'un **registre**.

* _Cloud Pub/Sub_

**Les données de télémétrie de tous les appareils appartenant au même registre sont ensuite _transmises_ à un sujet Cloud Pub/Sub** (Cloud Pub/Sub est un produit GCP [[lien](https://cloud.google.com/pubsub/)], pas spécifiquement un produit Cloud IoT Core). Le nom du sujet Cloud Pub/Sub suit ce modèle :

```
projects/id-of-google-cloud-project/topics/name-of-telemetry-topic
```

Donc, si nous appelons notre projet Google Cloud `hello-cloud-iot-core`, si nous choisissons `weather-telemetry-topic` pour le nom de notre sujet de télémétrie Pub/Sub et si enfin notre registre s'appelle `weather-devices-registry`, nous obtiendrons tôt ou tard ce genre de vue dans **Google Cloud Console** :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BeVR0exU6l-rXg8LqJvfeQ.jpeg)
_ID du projet, ID du registre et nom du sujet Pub/Sub de télémétrie dans Google Cloud Console_

Mais pas de stress, tout sera expliqué étape par étape pour atteindre cela.

_Note :_ Comme il est dit ici ([[lien](https://cloud.google.com/iot/docs/how-tos/mqtt-bridge#publishing_telemetry_events)]), chaque message dans le sujet Cloud Pub/Sub contient une copie du message de télémétrie publié par l'appareil mais aussi certains **attributs de message**, le plus important étant probablement `deviceID`, nous permettant de faire correspondre certaines données reçues avec l'appareil qui les a publiées.

_Note :_ Nous parlons beaucoup de **Pub(lish)**, mais où est le **Sub(scribe)** ? En fait, nous allons créer rapidement avec l'interface de ligne de commande Google Cloud une abonnement Cloud Pub/Sub (un "pull") afin de voir les messages publiés sur le sujet de télémétrie. Plus tard dans cet article, nous allons créer une fonction Firebase Cloud Function réagissant à chaque publication et cela créera automatiquement un autre abonnement (un "push" cette fois).

**De Cloud Pub/Sub au stockage et à la visualisation des données**

Nous suivons la partie droite du diagramme d'architecture du projet donné au début de cet article :

![Image](https://cdn-media-1.freecodecamp.org/images/1*aN_fNiSZXWfgoNrHPmNXeQ.png)
_Architecture du projet — Stockage et visualisation des données météorologiques_

Une publication sur le sujet Cloud Pub/Sub **déclenchera une fonction Firebase Cloud Function** qui remplira elle-même une **Firebase Realtime Database** avec les nouvelles données. Une application web hébergée par **Firebase Hosting** tracera en direct les données de la Firebase Realtime Database, de la même manière que nous l'avons fait dans un article précédent : [[lien](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-3-644048e90ca4)].

Il existe d'autres options dans l'écosystème Google pour stocker/traiter/visualiser les données. L'excellent article d'[Alvaro Viebrantz](https://www.freecodecamp.org/news/gcp-cloudiotcore-esp32-mongooseos-1st-5c88d8134ac7/undefined) [[lien](https://medium.com/google-cloud/build-a-weather-station-using-google-cloud-iot-core-and-mongooseos-7a78b69822c5)] qui nous a aidés utilise **Big Query** ([[lien](https://cloud.google.com/bigquery/)]) et **Data Studio** ([[lien](https://datastudio.google.com)]).

**Sujets supplémentaires "config" et "state"**

Sur le diagramme d'architecture du projet donné au début de cet article, nous voyons, outre la télémétrie, deux autres flux de données : **Config** ([[lien](https://cloud.google.com/iot/docs/how-tos/config/configuring-devices)]) et **State** ([[lien](https://cloud.google.com/iot/docs/how-tos/config/getting-state)]) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kBpmaNkEksBh_SAju-XpxA.png)
_Flux de données Config et State_

En effet, le service Cloud IoT Core peut publier des **messages de mise à jour de configuration** sur un sujet spécial auquel l'appareil s'est abonné ([[lien](https://cloud.google.com/iot/docs/how-tos/config/configuring-devices)]). Cela est utile lorsque nous avons besoin que l'appareil passe à un nouvel état, par exemple en mettant à jour un paramètre de son capteur associé, en changeant une période de veille profonde, en déplaçant un servomoteur, etc.

Pour des raisons d'efficacité, il ne devrait pas y avoir plus d'un message de ce type par seconde et par appareil. Un tel message est un blob défini arbitrairement par l'utilisateur (nous utiliserons JSON), jusqu'à 64 kiB. Enfin, le nom de ce sujet MQTT spécial est impérativement :

```
/devices/{device-id}/config
```

D'autre part, un appareil peut publier sur un sujet spécial — auquel Cloud IoT Core s'est automatiquement abonné — **des messages concernant son état** ([[lien](https://cloud.google.com/iot/docs/how-tos/config/getting-state)]), par exemple la quantité de RAM disponible, l'état d'un bouton, etc. Cela est souvent utilisé pour voir si le message de configuration précédent envoyé à l'appareil a eu l'effet souhaité.

Pour des raisons d'efficacité, ce type de publication ne doit pas être effectué plus d'une fois par seconde et par appareil. Un tel message est un blob défini arbitrairement par l'utilisateur (nous utiliserons JSON), jusqu'à 64 kiB. Enfin, le sujet auquel l'appareil publie ses données d'état a impérativement ce nom :

```
/devices/{device-id}/state
```

_Note :_ L'envoi de **commandes** aux appareils est également possible depuis Cloud IoT Core : voir [[lien](https://cloud.google.com/iot/docs/how-tos/commands)] mais nous ne l'illustrerons pas.

> Mais pour l'instant, nous allons nous concentrer sur la télémétrie. Après ce voyage, dans un article "à venir" nous montrerons comment gérer les sujets spéciaux `_config_` et `_state_`.

MISE À JOUR 29 mars 2019 : Cet article sur les sujets spéciaux `config` et `state` est sorti : [[lien](https://medium.com/@o.lourme/gcp-cloudiotcore-esp32-mongooseos-2nd-config-state-encrypt-7c5e937e5be9)].

### **Installation de Mongoose OS sur les appareils**

#### 1) Une brève description de Mongoose OS

**Mongoose OS** ([[lien](https://mongoose-os.com/)], [[lien](https://lwn.net/Articles/733297/)]) est un système d'exploitation intelligent orienté IoT, exécutable sur plusieurs puces, y compris ESP8266 et ESP32. Mongoose OS est en partenariat avec les principaux acteurs de l'IoT ([[lien](https://mongoose-os.com/about.html)]). Il est livré avec un outil de développement appelé **mos**, fonctionnant soit dans une interface utilisateur, soit avec un terminal de ligne de commande (comme `cmd.exe` sous Windows). Dans les deux cas, nous écrivons des commandes `mos`. Il existe également une application de gestion des appareils appelée mDash, mais nous ne l'avons pas essayée. **De nombreuses APIs traitant de la plupart des protocoles réseau et de capteurs sont fournies.** Les programmes peuvent être écrits en C/C++ et en JS.

Enfin, il existe une série de 12 tutoriels sur YouTube, vraiment utile :

%[https://youtu.be/bDsqR6HBseY?list=PLNOffh-6mSoRfxD4wTvRziUDUiSLSyJKE]

_Note :_ Nous avons utilisé Mongoose OS Community Edition, qui est gratuit, sous licence Apache 2.0.

#### 2) Installation de Mongoose OS sur ESP32

Cette installation doit être effectuée sur chaque appareil.

Nous nous rendons dans la **section développeurs** du site web de Mongoose OS ([[lien](https://mongoose-os.com/docs/quickstart/setup.md)]) afin d'effectuer les **sept premières étapes** de la liste donnée dans cette ressource :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LZbBhMBqdngkZwdJrmtANg.png)
_Étapes de configuration de Mongoose OS_

**Étape #1**, **Étape #2** et **Étape #3** sont triviales. À l'étape #3, n'oubliez pas de connecter l'appareil à la machine hôte via un câble USB.

Pour l'**Étape #4** "Créer une nouvelle application", nous choisissons d'appeler l'application `app1`. Lorsque `mos clone https://github.com/mongoose-os-apps/demo-js app1` indiqué sur le site web est terminé, l'outil mos passe automatiquement au dossier `app1/` nouvellement créé.

Dans le dossier `app1/fs/`, il y a un fichier source appelé `init.js`. C'est un fichier de démonstration capable de communiquer avec différentes plateformes IoT (si elles sont configurées, bien sûr). Nous allons le tester et bientôt le simplifier pour nos besoins.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5GYs7d1Ws_km6oDnWPaa6Q.png)
_Outil **mos** lancé dans une interface utilisateur ; ESP32 sélectionné ; La console série (à droite) est par défaut à 115200 bds, la vitesse par défaut de l'ESP32._

**Étape #5** "Construire le firmware de l'application" est lancée avec la commande `mos build` (ajoutez `--arch esp32` à cette commande si vous la lancez depuis un terminal de ligne de commande, et non depuis l'outil mos). Cela peut prendre un certain temps, mais normalement, nous devons effectuer cette construction une seule fois. Après cela, nous avons beaucoup plus de fichiers. Un fichier appelé `app1/build/fw.zip` contient les binaires du système d'exploitation et `init.js`. Il sera flashé sur l'ESP32 à l'étape suivante.

**Étape #6** "Flashing du firmware" est lancée avec la commande `mos flash`. Normalement, cela doit être fait une seule fois. Même si nous modifions certains fichiers (comme `init.js` par exemple), nous utiliserons une commande `mos put` pour télécharger un fichier de la machine hôte vers le **système de fichiers local de l'appareil**. Bien sûr, cette commande n'est disponible qu'après le processus de flash.

_Note :_ L'étape de flashage du firmware peut être délicate avec un ESP32 tout neuf. Avec notre ESP32 DEVKIT V1, nous avons eu des messages dans la console (c'est un premier bon point !) signalant des problèmes de connexion à la ROM ESP32. Réessayer de flasher en appuyant sur le bouton BOOT (fermé près du connecteur USB) a finalement abouti à un flashage réussi. Cependant, soyez prêt à attendre une minute ou deux.

Ensuite, l'appareil redémarre automatiquement et exécute `init.js`. Nous avons obtenu toutes les secondes les informations suivantes dans la console mos (ou dans n'importe quel terminal série @115200 bds) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0i3bn3fhEkAolrkfvBjQVg.png)
_Console après le flashage initial du firmware ESP32 avec Mongoose OS_

Dans l'**Étape #7**, nous connectons l'ESP32 à notre réseau wifi (nous utilisons l'outil mos) :

```
mos wifi WIFI_NETWORK_NAME WIFI_PASSWORD
```

L'appareil redémarrera automatiquement après avoir obtenu une adresse IP et synchronisé l'heure en contactant un serveur SNTP. Nous pingons ensuite notre appareil pour vérifier sa connexion internet.

_Note :_ Nous obtenons des informations sur l'appareil (adresse IP par exemple) en appuyant sur **CTRL+i** dans l'outil mos, ou en tapant `mos call Sys.GetInfo`.

_Note :_ Nous réinitialisons l'appareil en appuyant sur **CTRL+u** dans l'outil mos, ou en tapant `mos call Sys.Reboot`.

_Note :_ Les étapes #5, #6 et #7 pourraient être le début d'un "script de provisionnement", utile si nous avons de nombreux appareils à configurer. Il est facultatif de relancer l'étape #5 si tous les appareils sont identiques, par exemple uniquement ESP32.

#### 3) Programme "Hello, World!" ESP32 avec Mongoose OS

Pour nous habituer au style de programmation JS de Mongoose OS et à l'outil mos, écrivons un petit programme dont le but est de faire clignoter la LED bleue intégrée et d'imprimer des messages sur la console. **Cette LED est connectée à la broche GPIO2** de l'ESP32 DEVKIT V1 (voir le diagramme d'assemblage au début de cet article). Sur notre machine hôte, remplaçons le contenu de `app1/fs/init.js` par celui-ci :

```js
/*
 ESP32 DEVKIT V1 - Mongoose OS
 Clignotement de la LED intégrée et journalisation de la console
 Cette LED bleue est connectée à la broche GPIO2.
 Voir :
 - https://mongoose-os.com/docs/mos/api/core/mgos_timers.h.md
*/

load('api_config.js');
load('api_gpio.js');
load('api_timer.js');

let pin = 2;

GPIO.set_mode(pin, GPIO.MODE_OUTPUT);

// Appeler toutes les 2 secondes
Timer.set(2000, Timer.REPEAT, function() {
  let value = GPIO.toggle(pin);
  print(value ? 'Tick' : 'Tock');
}, null);
```

Depuis l'outil mos ou depuis un terminal de ligne de commande, nous téléchargeons ce fichier vers le système de fichiers Mongoose OS et enfin nous redémarrons l'appareil :

```
mos put fs/init.js
mos call Sys.Reboot
```

La LED bleue devrait clignoter et nous devrions voir alternativement `Tick` et `Tock` imprimés sur la console.

#### 4) Test DHT22 avec Mongoose OS

Au début de cet article, il y a un diagramme d'assemblage montrant comment connecter le capteur DHT22 avec l'ESP32 DEVKIT V1. Nous avons choisi de connecter la **broche de données DHT22** **à la broche GPIO0 de l'ESP32 DEVKIT V1**.

Voici donc un autre court programme `init.js`. Celui-ci imprime périodiquement sur la console série les mesures du DHT22 (température et humidité - sous forme d'objet en JSON, pas encore de publication MQTT) :

```js
/*
 ESP32 DEVKIT V1 - Mongoose OS
 Les mesures du capteur DHT22 sont envoyées à la console.
 La broche de données DHT22 est connectée à la broche GPIO0.
 Voir :
 - https://mongoose-os.com/docs/quickstart/develop-in-js.md
 - https://mongoose-os.com/docs/mos/api/drivers/dht.md
*/

load('api_config.js');
load('api_dht.js');
load('api_timer.js');

let pin = 0;
let dht = DHT.create(pin, DHT.DHT22);

Timer.set(5000, true, function() { // période du timer est en ms
  let msg = JSON.stringify({temperature: dht.getTemp(), humidity: dht.getHumidity()});
  print(msg);
}, null);
```

Ensuite :

```
mos put fs/init.js
mos call Sys.Reboot
```

Et voici la console associée que nous obtenons après avoir téléchargé le programme `init.js` et redémarré l'appareil. L'humidité est en % et la température est en degrés Celsius :

![Image](https://cdn-media-1.freecodecamp.org/images/1*2xr980fPqZCYC84iUq4qEw.png)
_Mesures DHT22 telles qu'imprimées sur la console. Un peu trop précises, n'est-ce pas ?_

Les nombres semblent avoir une longue partie décimale, mais cela sera corrigé plus tard dans une fonction Cloud.

_Note :_ À des fins pédagogiques, nous avons choisi dans cet article des noms de clés explicites et longs comme `temperature` ou `humidity`. Cela aura des conséquences sur le volume de données stockées plus tard dans une base de données NoSQL (Firebase Realtime Database) car ces clés seront répétées pour chaque mesure. Des noms de clés plus courts pourraient être une bonne idée.

#### 5) Publions les données sur le sujet de télémétrie MQTT

**C'est notre dernier programme, celui prêt à fonctionner avec Cloud IoT Core !** Sur le programme précédent, nous ajoutons simplement une publication sur le sujet de télémétrie dont nous avons déjà parlé : `/devices/{device-id}/events`.

Notez que les messages sont publiés en JSON car cela facilitera plus tard la récupération de leur contenu avec la fonction Firebase Cloud Function réagissant à la publication des messages.

```js
/*
 ESP32 DEVKIT V1 - Mongoose OS
 Les mesures du capteur DHT22 sont envoyées à la console.
 La broche de données DHT22 est connectée à la broche GPIO0.
 Publie les données météorologiques sur le sujet approprié.
 
 Voir :
 - https://mongoose-os.com/docs/quickstart/develop-in-js.md
 - https://mongoose-os.com/docs/mos/api/drivers/dht.md
 - https://mongoose-os.com/docs/mos/api/net/mqtt.md
*/

load('api_config.js');
load('api_dht.js');
load('api_timer.js');
load('api_mqtt.js');

// Le sujet de télémétrie doit avoir ce nom :
let topic = '/devices/' + Cfg.get('device.id') + '/events';

let pin = 0;
let dht = DHT.create(pin, DHT.DHT22);

Timer.set(5000, true, function() { // période du timer est en ms
  let msg = JSON.stringify({temperature: dht.getTemp(), humidity: dht.getHumidity()});
  // Publier le message avec un QoS 1
  // MQTT.pub() retourne 1 en cas de succès, 0 sinon.
  let ok = MQTT.pub(topic, msg, 1); 
  print(ok, msg);
}, null);
```

Nous nommons ce fichier `init.js`, le téléchargeons vers le système de fichiers Mongoose, puis provoquons un reset :

```
mos put fs/init.js
mos call Sys.Reboot
```

_Note :_ Ces commandes pourraient être ajoutées au "script de provisionnement" que nous avons mentionné précédemment.

Lors de l'exécution, ce dernier programme imprime les données sur la console mais échoue à publier les données sur le pont MQTT de Cloud IoT Core (`MQTT.pub()` retourne 0) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q-FIqugYuMQGd5rjjeu56Q.png)
_Les données de télémétrie ne peuvent toujours pas être publiées car nous n'avons pas encore configuré de projet Google Cloud._

En effet, nous n'avons pas encore configuré de projet Google Cloud, ni _a fortiori_ enregistré un seul appareil. Faisons-le maintenant !

### Configuration du projet Cloud IoT Core

#### 1) Installation du SDK Google Cloud

Tout d'abord, nous devons **installer le SDK Google Cloud** car nous devrons taper certaines commandes `**gcloud**` dans un terminal de ligne de commande. Au moment de la rédaction, il nécessite Python 2.7. Cela ne fonctionnera pas avec Python 3.5. La page de téléchargement du SDK Google Cloud ([[lien](https://cloud.google.com/sdk/downloads)]) propose des versions du SDK avec Python intégré (si vous êtes sûr de ne pas avoir Python déjà installé et de ne pas vouloir gérer ce point Python).

Ensuite, Cloud IoT Core nécessite certaines **versions bêta des commandes `gcloud`**. Donc, dans un terminal de ligne de commande, depuis n'importe quel dossier, nous tapons :

```
gcloud components install beta
```

Ces deux étapes précédentes doivent être effectuées une seule fois !

_Note :_ La plupart des actions suivantes sur Google IoT Core peuvent être effectuées de trois manières :

* avec **Google Cloud Console** (sur le web)
* avec **certaines APIs** dans différents langages, et
* avec **l'interface de ligne de commande** dans un terminal, en tapant des commandes `gcloud`.

Nous utiliserons cette dernière pour configurer les choses et nous vérifierons les faits avec Google Cloud Console (sur le web).

#### 2) Configuration du projet Google Cloud

Nous suivons maintenant ce guide du site web de Mongoose OS : [[lien](https://mongoose-os.com/docs/quickstart/cloud/google.md)].

```
# Les commandes indiquées dans ce cadre gris doivent être effectuées une seule fois pour configurer le projet Google Cloud ! Elles peuvent être effectuées depuis n'importe quel dossier.

# Authentification avec Google Cloud
gcloud auth login

# Création du projet cloud. Nous avons choisi hello-cloud-iot-core comme PROJECT_ID
gcloud projects create hello-cloud-iot-core

# Donner à Cloud IoT Core la permission de publier sur les sujets Pub/Sub
gcloud projects add-iam-policy-binding hello-cloud-iot-core --member=serviceAccount:cloud-iot@system.gserviceaccount.com --role=roles/pubsub.publisher

# Définir le projet par défaut pour gcloud
gcloud config set project hello-cloud-iot-core

# Création du sujet Pub/Sub pour la télémétrie des appareils
gcloud beta pubsub topics create weather-telemetry-topic

# Création d'un abonnement Pub/Sub au sujet nouvellement créé
gcloud beta pubsub subscriptions create --topic weather-telemetry-topic weather-telemetry-subscription

# Création du registre des appareils (nous l'appelons weather-devices-registry)

# Préciser le nom du sujet Pub/Sub pour les notifications d'événements

# Désactiver les connexions des appareils au pont HTTP
gcloud beta iot registries create weather-devices-registry --region europe-west1 --no-enable-http-config --event-notification-config=topic=weather-telemetry-topic

# Dire 'oui' pour activer l'API (si demandé).

# Mais la dernière commande peut ne pas fonctionner

# si vous n'activez pas la facturation.

# Donc, suivez le lien pour activer la facturation et réessayez la dernière commande.

# Cela devrait se terminer par "Created registry [weather-devices-registry]."
```

#### 3) Enregistrement de l'appareil dans le projet Cloud IoT Core

Enregistrons maintenant les appareils dans le projet ! Un à la fois, bien sûr. **L'outil mos est vraiment utile pour cette tâche.** Depuis l'outil mos lancé dans son interface utilisateur ou depuis un terminal de ligne de commande, placé dans notre dossier `app1`, nous tapons la commande suivante (l'ID du projet et le nom du registre sont impliqués, comme vous le voyez) :

```
# Enregistrement de l'appareil avec Cloud IoT Core (à faire pour chaque appareil !)
mos gcp-iot-setup --gcp-project hello-cloud-iot-core --gcp-region europe-west1 --gcp-registry weather-devices-registry
```

_Note :_ Cette commande pourrait être la dernière du "script de provisionnement" que nous avons mentionné déjà deux fois.

Cette commande est une commande `mos` qui utilisera elle-même des commandes `gcloud`. L'appareil sur le point d'être enregistré doit être connecté via le port série à notre ordinateur hôte car certaines informations seront téléchargées, comme les clés, l'adresse du pont MQTT, etc.

En effet, nous voyons sur la console mos que **deux clés (une privée, une publique) sont générées**. Nous pouvons les inspecter dans le dossier du projet `app1`. La clé privée est pour l'ESP32 et la clé publique est pour Google IoT Core. Elles sont utilisées lors du processus d'authentification impliquant le JSON Web Token que nous avons mentionné précédemment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iVJ-dbpnqmQJqwuGFC917A.png)
_Paire de clés nouvellement générée (privée et publique)_

_Note concernant la sécurité :_ **La clé privée ne doit pas être stockée en texte clair dans la mémoire flash de l'ESP32**. C'est pourquoi nous décrivons dans l'article suivant celui-ci ([[lien](https://medium.com/@o.lourme/gcp-cloudiotcore-esp32-mongooseos-2nd-config-state-encrypt-7c5e937e5be9)]) comment chiffrer cette mémoire. De plus, **le fichier de la clé privée ne doit pas être stocké en texte clair sur l'ordinateur de développement hôte**. Au moins, protégez l'accès à son contenu avec un mot de passe.

Lorsque l'appareil redémarre, nous voyons dans la console qu'il se connecte avec succès au pont MQTT de Google et publie des messages de télémétrie (`MQTT.pub()` retourne 1) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*H9T-zF4B-HwYgO_ZdratEw.png)
_Publications vers le pont MQTT réussies. Bon travail !_

#### 4) Vérification de la configuration du projet dans Google Cloud Console

Nous nous rendons sur [https://console.cloud.google.com/iot/](https://console.cloud.google.com/iot/) pour vérifier que tout a été bien configuré :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BeVR0exU6l-rXg8LqJvfeQ.jpeg)
_ID du projet, ID du registre et nom du sujet Pub/Sub de télémétrie dans Google Cloud Console_

En cliquant sur l'**ID du registre** `weather-devices-registry`, nous accédons à un autre écran. En cliquant sur "Appareils" sur cet nouvel écran, nous listons les appareils provisionnés et obtenons des détails comme la dernière fois qu'ils ont été vus (mais ce n'est pas une mise à jour en direct, nous devons actualiser la page) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*sfa7ErglL4OqCsk2jIZqUA.png)
_Vue des appareils dans Google Cloud Console_

En cliquant sur le nom du **sujet Pub/Sub de télémétrie**, nous accédons à la **console Pub/Sub** pour afficher l'abonnement que nous avons créé précédemment, c'est-à-dire celui lié au sujet de télémétrie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*EQ1r5SozuzjM5Jrbl4vdVg.png)
_Google Cloud Console (Pub/Sub) — noms du sujet et de l'abonnement associé_

#### 5) Visualisation enfin de certaines données de télémétrie

Maintenant, il serait bien de voir les données que les appareils publient. Pour cela, nous avons l'abonnement que nous avons déjà créé. Depuis n'importe quel dossier de l'ordinateur hôte, nous tapons :

```
gcloud beta pubsub subscriptions pull --auto-ack weather-telemetry-subscription --limit=2
```

Cette commande ([[lien](https://cloud.google.com/sdk/gcloud/reference/beta/pubsub/subscriptions/pull)]) extrait jusqu'à **_2_** messages Pub/Sub de notre abonnement `weather-telemetry-subscription`. Nous pouvons voir les données en JSON, les identifiants des messages et une liste d'attributs pour chaque message. Parmi eux, l'attribut `deviceId` est présent. Malheureusement, il n'y a pas de timestamps, nous verrons comment les obtenir plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1*78OYVPPUeKZWRRvlWdI4Mg.png)
_Résultat de l'extraction des messages de télémétrie d'un abonnement_

> Si vous avez atteint cette étape, félicitations ! Nous sommes maintenant prêts à écrire une fonction Firebase Cloud Function réagissant à chaque publication sur le sujet de télémétrie Pub/Sub !

### Journalisation, stockage et visualisation des données météorologiques avec Firebase

#### 1) Introduction

Nous abordons maintenant cette partie du projet :

![Image](https://cdn-media-1.freecodecamp.org/images/1*UwR_qn8GX1b2CkMA62kT3w.png)
_La partie que nous étudions maintenant_

Sur ce diagramme, nous voyons que notre projet nécessite 3 produits Firebase :

Une **Firebase Cloud Function** (plus exactement "une Cloud Function pour Firebase") doit réagir à toute publication sur le sujet de télémétrie afin de stocker les données météorologiques de cette publication dans une **Firebase Realtime Database**. Ce stockage permet la persistance des données météorologiques et est utilisé pour alimenter une application web hébergée par **Firebase Hosting**. Cette application web trace en direct les données météorologiques au fil du temps.

La bonne nouvelle est qu'il est possible de configurer tous ces produits avec une seule commande.

#### **2) Configuration de Firebase, dépôt GitHub**

Nous travaillons toujours sur le même projet Google Cloud appelé `hello-cloud-iot-core`. Firebase va simplement "améliorer" ce projet avec ses produits.

Nous avons créé un dépôt GitHub pour les aspects Firebase de notre projet :

[**olivierlourme/iot-store-display**](https://github.com/olivierlourme/iot-store-display)
[_Contribuez au développement de olivierlourme/iot-store-display en créant un compte sur GitHub._github.com](https://github.com/olivierlourme/iot-store-display)

Clonez ce dépôt dans votre dossier de développement préféré et accédez au répertoire nouvellement créé :

```
c:\_app>git clone https://github.com/olivierlourme/iot-store-display
c:\_app>cd iot-store-display
```

**Configuration globale de Firebase**

_Note :_ Nous supposons que vous avez **Firebase tools** installé (_c'est-à-dire_ Node.js installé et `npm install -g firebase-tools` a été exécuté, voir [[lien](https://firebase.google.com/docs/functions/get-started)] pour plus de détails).

Effectuons les initialisations Firebase :

```
c:\_app\iot-store-display>firebase init 
```

La première étape consiste à choisir les produits Firebase que nous voulons utiliser :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FYoZkLMMrQBQDflK8Z46fQ.png)
_Choix des produits Firebase_

On nous demande ensuite d'associer le répertoire actuel (`iot-store-display`) à l'un des projets Firebase listés. Le problème est que notre projet `hello-cloud-iot-core` n'apparaît pas dans la liste car avant d'être un projet Firebase, c'est aussi un projet Google Cloud ! Lisez les articles de [Doug Stevenson](https://www.freecodecamp.org/news/gcp-cloudiotcore-esp32-mongooseos-1st-5c88d8134ac7/undefined) sur les relations entre Firebase et Google Cloud : [[lien](https://medium.com/google-developers/whats-the-relationship-between-firebase-and-google-cloud-57e268a7ff6f)] et [[lien](https://medium.com/google-developers/firebase-google-cloud-whats-different-with-cloud-functions-612d9e1e89cb)].

Pour surmonter cela, nous appuyons d'abord sur CTRL+C pour arrêter ce processus d'initialisation, puis nous allons dans la **console Firebase** à l'adresse [https://console.firebase.google.com](https://console.firebase.google.com). Nous choisissons "Ajouter un projet" :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nOcFfL_ZwGUKGe-PDnsZUQ.png)
_Console Firebase — Ajouter un projet_

Et nous pouvons voir notre projet (avec le logo Google Cloud) et le choisir :

![Image](https://cdn-media-1.freecodecamp.org/images/1*QqI3k8bH5P348eAInetTOQ.png)
_Console Firebase — Même les projets Google Cloud sont listés._

_Note :_ Vous pourriez être invité à confirmer le plan de facturation Firebase si le projet Google Cloud lui-même a un plan de facturation.

Super ! Nous redémarrons l'initialisation Firebase avec la commande `firebase init` et cette fois notre projet Google Cloud `hello-cloud-iot-core` est listé. Nous le choisissons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*qr4CKgpdnEG9UorzVv3yrw.png)
_Notre répertoire `**iot-store-display**` est associé au projet **hello-cloud-iot-core**._

_Note :_ Si vous ne voyez toujours pas votre projet, vous êtes peut-être connecté à Firebase sans le bon compte Google. Dans ce cas, tapez `firebase logout` suivi de `firebase login`.

**Configuration de la base de données en temps réel**

Ensuite, l'assistant pose une seule question sur la base de données en temps réel et ses règles : le nom du fichier où elles seront sauvegardées. Nous conservons le nom par défaut. Il est plus pratique d'avoir ces règles dans un fichier situé dans le répertoire du projet que d'aller dans la console Firebase comme nous l'avons fait dans les articles précédents. Nous détaillerons ces règles plus tard.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YtlGoKNyjspvirVxSoXYNg.png)
_Nom du fichier stockant les règles de la base de données en temps réel_

**Configuration des fonctions Cloud**

Voici les réponses que nous avons faites à l'assistant concernant la configuration des fonctions :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ml7Pc1OSEgqi6dRsy5J_aA.png)
_Configuration des fonctions Cloud_

Bien sûr, nous choisissons de ne pas écraser le fichier `functions/index.js` obtenu depuis [GitHub](https://github.com/olivierlourme/iot-store-display).

**Configuration de l'hébergement Firebase**

Et voici les réponses que nous avons faites à l'assistant concernant la configuration de l'hébergement :

![Image](https://cdn-media-1.freecodecamp.org/images/1*F_7qI1Norg4qjQfPhouCWw.png)
_Configuration de l'hébergement_

Bien sûr, nous choisissons de ne pas écraser le fichier `public/index.html` obtenu depuis [GitHub](https://github.com/olivierlourme/iot-store-display).

**Déploiement (pas maintenant !)**

Plus tard, si nous voulons déployer certaines mises à jour que nous avons apportées à nos 3 produits, nous pouvons taper globalement :

```
c:\_app\iot-store-display>firebase deploy
```

Mais si nous voulons déployer uniquement, respectivement :

* les règles de la base de données mises à jour,
* les fonctions cloud mises à jour,
* l'application web mise à jour,

nous tapons, respectivement :

```
firebase deploy --only database
firebase deploy --only functions
firebase serve --only hosting (déploiement local) OU firebase deploy --only hosting (déploiement distant)
```

#### 3) Fonction Cloud déclenchée par Pub/Sub

**Introduction**

Dans un article précédent, nous avons expliqué que nous pouvions écrire des **fonctions Firebase Cloud** déclenchées par certains événements survenant sur certains des produits Google.

[**Article 2 sur 3. Notre voyage IoT à travers ESP8266, Firebase et Plotly.js**](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-2-14b0609d3f5e)
[_Une fonction Firebase Cloud Function ajoute un timestamp à chaque valeur poussée vers une base de données Firebase Realtime._medium.com](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-2-14b0609d3f5e)

**Cloud Pub/Sub** est l'un de ces produits et il est donc possible de déclencher une fonction chaque fois qu'un message est publié sur un sujet Pub/Sub : [[lien](https://firebase.google.com/docs/functions/pubsub-events)].

Ainsi, si la fonction Firebase Cloud est déclenchée à chaque publication sur le sujet `weather-telemetry-topic`, la surveillance de son journal nous permettra de surveiller l'activité du sujet de télémétrie.

Le code de la fonction Cloud doit stocker chaque nouvelle donnée publiée dans la base de données Firebase Realtime associée à notre projet.

**Code source de la fonction Cloud**

Le début du code source ressemble à ceci :

```
exports.detectTelemetryEvents = functions.pubsub.topic('weather-telemetry-topic').onPublish(
    (message, context) => {...
```

Le code source complet de la fonction Cloud se trouve dans le fichier nommé `index.js`. Ce fichier se trouve dans le dossier `functions` de notre répertoire `iot-store-display` sur [GitHub](https://github.com/olivierlourme/iot-store-display). Il est entièrement commenté, alors exécutez-le et étudiez-le, il est court et pas compliqué.

**Déploiement de la fonction Cloud**

Il est temps de déployer la fonction Cloud :

```
c:\_app\iot-store-display>firebase deploy --only functions
```

**Validation de la fonction Cloud**

Une fois la fonction Cloud déployée, nous pouvons surveiller les journaux de la fonction Cloud et, entre autres, nous verrons les résultats du `console.log(`Device=${deviceId}...)` que nous avons écrit à la fin de `index.js`.

Où voir ces journaux ? Nous avons deux opportunités :

* dans la console Firebase ([https://console.firebase.google.com](https://console.firebase.google.com)) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*SH9086pyf8yyuEnyCDu0UQ.png)
_Console Firebase — Journaux des fonctions Cloud Firebase_

* dans la console Google Cloud ([https://console.cloud.google.com/functions/](https://console.cloud.google.com/functions/)) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*D3QmCuAsqE5jUkuIyPTB-w.png)
_Console Google Cloud — Accès aux **journaux des fonctions Cloud** et à la **suppression des fonctions Cloud**_

Nous préférons cette dernière solution, car les journaux sont plus clairs :

![Image](https://cdn-media-1.freecodecamp.org/images/1*kgpwdupeMVLKQ2msHpO4cQ.png)
_Console Google Cloud - Journaux des fonctions Cloud_

Concernant le stockage, voici ce qui se trouve dans la base de données Firebase Realtime après que chaque appareil a effectué 2 publications de données de télémétrie. Les données sont bien sûr triées par appareil comme nous l'avons spécifié dans `index.js` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*gJX7raPOkRvRZzAHhQC14Q.png)
_Console Firebase — Base de données en temps réel après 2 publications de données de télémétrie par appareil_

_Note :_ N'oubliez pas de **supprimer votre fonction Cloud** sur les serveurs Google si vous ne l'utilisez pas, sinon vous pourriez atteindre le quota d'invocations ou payer pour un service que vous n'utilisez pas, comme indiqué ici : [[lien](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-2-14b0609d3f5e)]. La suppression de la fonction doit être effectuée sur la console Google Cloud (voir "Delete", 3 captures d'écran ci-dessus).

_Note :_ La fonction Cloud a des droits d'administrateur sur la base de données, quel que soit le contenu du fichier `database.rules.json`. À cette étape, le fichier `database.rules.json` peut encore être très restrictif. N'oubliez pas de les déployer, une fois édités.

```js
{
  "rules": {
    ".read": false,
    ".write": false
  }
}
```

#### 4) Une application web utilisant Firebase et plotlys.js pour visualiser les données météorologiques

**Introduction**

_Note :_ Nous construisons maintenant une solution de visualisation de données "maison" (et satisfaisante). Pour une interface utilisateur améliorée (tableau de bord, etc.), vous devriez peut-être explorer Data Studio que nous avons déjà mentionné ailleurs dans cet article.

Nous nous concentrons sur la **construction d'une petite application web**, hébergée par **Firebase Hosting**. Cette application web **trace en direct** les données stockées dans la base de données Firebase Realtime. Nous avons utilisé [plotly](https://www.freecodecamp.org/news/gcp-cloudiotcore-esp32-mongooseos-1st-5c88d8134ac7/undefined) ([https://plot.ly/javascript/](https://plot.ly/javascript/)) pour la bibliothèque de traçage. Nous sommes familiers avec ce travail car nous avons déjà entrepris un travail similaire dans un article précédent :

[**Article 3 sur 3. Notre voyage IoT à travers ESP8266, Firebase et Plotly.js**](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-3-644048e90ca4)
[_Une application web hébergée par Firebase Hosting s'abonne au flux de données provenant d'une base de données Firebase Realtime et trace..._medium.com](https://medium.com/@o.lourme/our-iot-journey-through-esp8266-firebase-angular-and-plotly-js-part-3-644048e90ca4)

Ce qui est différent aujourd'hui, c'est que nous devons :

* tracer plusieurs graphiques : température _vs_ temps et humidité _vs_ temps,
* dans chaque graphique, nous avons un tracé par appareil.

**Règles de la base de données & nœud devices-ids**

Concernant les règles de la base de données, que devrait être maintenant le fichier `database.rules.json` ? Le nœud `device-telemetry` doit être **lu** par l'application web. Et si vous avez regardé attentivement la capture d'écran de la base de données en temps réel donnée quelques captures d'écran plus tôt, il y a un autre nœud appelé `devices-ids`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Si6-O12MUJXpzN3qyZyBVg.png)
_Console Firebase — Détail du nœud devices-ids dans la base de données en temps réel_

Vous devez créer **manuellement dans la console Firebase** ce nœud `devices-ids` et le remplir de manière appropriée pour que l'application web fonctionne correctement. C'est un moyen simple de déclarer à l'application web les appareils pour lesquels nous voulons des tracés et aussi de donner des alias aux appareils. Son rôle et sa nécessité sont entièrement expliqués dans les commentaires du fichier `public/script.js` donné dans [GitHub](https://github.com/olivierlourme/iot-store-display).

_Note :_ Une amélioration pourrait être un formulaire (accédé via une authentification) qui, une fois rempli, appelle un script pour générer ce nœud `devices-ids`.

Ce nœud `devices-ids` doit également être lu par l'application web. Donc le fichier `database.rules.json` devrait finalement devenir :

```js
{
  "rules": {
    "devices-ids": {
      ".read": true,
      ".write": false
    },
    "devices-telemetry": {
      ".read": true,
      ".write": false
    }
  }
}
```

Ces nouvelles règles, une fois éditées et sauvegardées, doivent être déployées avec :

```
c:\_app\iot-store-display>firebase deploy --only database
```

**Code source de l'application web**

Le code source de l'application web se trouve dans le répertoire `public` de notre dossier `hello-cloud-iot-core` ou sur [GitHub](https://github.com/olivierlourme/iot-store-display). Le contenu du dossier, en particulier `script.js`, est entièrement commenté pour que vous sachiez où l'étudier (et l'améliorer !).

_Note :_ nous n'avons que deux appareils pour cette démonstration, mais le code source est adapté pour _x_ appareils tant que vous les déclarez dans le nœud `devices-ids`.

**Déploiement et validation locaux de l'application web**

À des fins de test, Firebase Hosting peut lancer un serveur local en direct :

```
c:\_app\iot-store-display>firebase serve --only hosting
```

Nous nous rendons sur `http://localhost:5000` et nous sommes heureux d'obtenir ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*02UfatBLkuqCD12-JNBgjw.gif)
_Enfin les graphiques que nous voulions !_

**Déploiement distant de l'application web**

Enfin, Firebase nous offre l'hébergement de notre application web et un accès via https :

```
c:\_app\iot-store-display>firebase deploy --only hosting
```

Nous obtenons rapidement l'URL publique de notre application web : [https://hello-cloud-iot-core.firebaseapp.com](https://hello-cloud-iot-core.firebaseapp.com)

![Image](https://cdn-media-1.freecodecamp.org/images/1*EZjq0siYgb0K6sMaFHlk4Q.png)
_Le déploiement de l'application web est complet !_

_Note :_ Si vous avez votre propre domaine, vous pouvez connecter votre application web Firebase à celui-ci. Voir [[lien](https://firebase.google.com/docs/hosting/custom-domain)].

### Conclusion

Dans cet article, nous avons découvert comment combiner **ESP32**, **Mongoose OS** et **Cloud IoT Core**, obtenant un projet IoT sérieux, sécurisé et **professionnel**. Maintenant que nous savons, cela peut aller très vite pour provisionner 10, 100... 1000 appareils acquérant des données météorologiques dans une zone, tant qu'ils peuvent obtenir une connexion Wifi. Maintenant, les appareils sont gérés centralement, il est facile de les provisionner et de les surveiller. Mais nous pouvons aller plus loin !

En effet, en plus de cet article, il y en a un second ([[lien](https://medium.com/@o.lourme/gcp-cloudiotcore-esp32-mongooseos-2nd-config-state-encrypt-7c5e937e5be9)]). À l'intérieur :

* Nous nous concentrerons sur le **chiffrement de la mémoire flash ESP32**, pour obtenir un système entièrement sécurisé.
* Nous verrons comment utiliser le sujet spécial `config`, nous permettant de **déclencher une action sur l'appareil depuis la console Google Cloud**.
* Nous verrons comment utiliser le sujet spécial `state`, permettant **à l'appareil de communiquer à la console Google Cloud des informations sur son état actuel**.

Nous espérons que vous avez apprécié cet article vraiment long et que vous avez appris quelque chose ! N'hésitez pas à me contacter si vous avez des questions ou des suggestions d'amélioration...