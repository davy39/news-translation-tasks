---
title: Comment configurer Zigbee2MQTT avec Docker pour la domotique
subtitle: ''
author: Joyce Lin
co_authors: []
series: null
date: '2024-11-19T13:04:28.160Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-zigbee2mqtt-with-docker
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731778246828/8371f4de-6771-4f57-9e2c-9c57ad651950.png
tags:
- name: Internet of Things
  slug: internet-of-things
- name: Docker
  slug: docker
- name: iot
  slug: iot
seo_title: Comment configurer Zigbee2MQTT avec Docker pour la domotique
seo_desc: Zigbee2MQTT is an open-source tool that lets you manage all of your Zigbee
  devices locally, so you don’t need cloud services or multiple proprietary hubs.
  This gives you more control and flexibility, whether used on its own or integrated
  with platfor...
---

[Zigbee2MQTT](https://www.zigbee2mqtt.io/) est un outil open-source qui vous permet de gérer tous vos appareils [Zigbee](https://en.wikipedia.org/wiki/Zigbee) localement, sans avoir besoin de services cloud ou de plusieurs hubs propriétaires. Cela vous donne plus de contrôle et de flexibilité, que ce soit utilisé seul ou intégré avec des plateformes comme [Home Assistant](https://www.home-assistant.io/) ou [Node-RED](https://nodered.org/).

Dans ce guide, je vais vous montrer comment le configurer en utilisant [Docker](https://www.docker.com/) pour une maison intelligente rationalisée et axée sur la confidentialité. Docker offre un moyen efficace d'exécuter Zigbee2MQTT en tant que service autonome, offrant une configuration légère et modulaire - aucun Home Assistant requis.

![Diagramme montrant l'intégration des appareils Zigbee dans un réseau local utilisant Raspberry Pi](https://cdn.hashnode.com/res/hashnode/image/upload/v1731723376381/d983ba57-72ba-4e06-b994-c6b30ad36ca5.png align="center")

## Table des matières

* [Concepts clés de l'IoT dans ce tutoriel](#heading-concepts-cles-de-liot-dans-ce-tutoriel)
    
* [Ce dont vous aurez besoin](#heading-ce-dont-vous-aurez-besoin)
    
* [Ce que vous allez faire](#heading-ce-que-vous-allez-faire)
    
* [Comment préparer votre environnement](#heading-comment-preparer-votre-environnement)
    
* [Comment configurer la configuration de Zigbee2MQTT](#heading-comment-configurer-la-configuration-de-zigbee2mqtt)
    
* [Comment configurer Zigbee2MQTT et le broker MQTT dans Docker](#heading-comment-configurer-zigbee2mqtt-et-le-broker-mqtt-dans-docker)
    
* [Lancer les conteneurs](#heading-lancer-les-conteneurs)
    
* [Appairer vos appareils Zigbee](#heading-appairer-vos-appareils-zigbee)
    
* [Comment créer un script d'automatisation](#heading-comment-creer-un-script-dautomatisation)
    
* [Quelle est la suite ?](#heading-quelle-est-la-suite)
    

## Concepts clés de l'IoT dans ce tutoriel

Voici les concepts clés liés à l'Internet des objets (IoT) et aux maisons intelligentes avec lesquels vous allez travailler :

* [Zigbee](https://en.wikipedia.org/wiki/Zigbee) est un protocole de communication sans fil utilisé dans les appareils domestiques intelligents. Il repose sur un coordinateur Zigbee pour communiquer avec des appareils comme des lumières, des capteurs et des interrupteurs au sein d'un réseau maillé local. Ce réseau permet aux appareils de relayer des signaux pour étendre la couverture et la fiabilité.
    
* [MQTT (Message Queuing Telemetry Transport)](https://en.wikipedia.org/wiki/MQTT) est un protocole de messagerie léger pour les environnements à faible bande passante et à haute latence. Il utilise un broker MQTT pour gérer la communication entre les appareils en utilisant un modèle de publication/abonnements (pub/sub), où les appareils peuvent soit envoyer, soit recevoir des messages basés sur des sujets spécifiques.
    
* [Zigbee2MQTT](https://www.zigbee2mqtt.io/) est une application de pont qui connecte les appareils Zigbee à un broker MQTT. Il traduit les signaux Zigbee en messages MQTT, et vice versa. Zigbee2MQTT supporte une large gamme d'appareils de différents fabricants.
    

## **Ce dont vous aurez besoin**

1. Un coordinateur Zigbee connecté à votre réseau ou appareil. J'ai un [SLZB-06](https://smlight.tech/product/slzb-06/) (65 USD) connecté à mon réseau.
    
2. Un appareil capable d'exécuter Docker, comme un Raspberry Pi ou un serveur Linux. J'ai flashé un Raspberry Pi 4 - Modèle B.
    

## **Comment préparer votre environnement**

1. Connectez-vous en SSH à votre Pi en utilisant la commande suivante dans votre fenêtre de terminal, où `pi` est le nom d'utilisateur de votre Raspberry Pi OS et `<RaspberryPi_IP>` est l'adresse IP de votre Raspberry Pi sur votre réseau local.
    
    ```bash
    ssh pi@<RaspberryPi_IP>
    ```
    
2. Installez Docker en entrant la commande suivante à l'invite SSH.
    
    ```bash
    curl -sSL https://get.docker.com | sh
    ```
    
3. Donnez les permissions à l'utilisateur actuellement connecté. Vous devrez peut-être fermer la connexion SSH et vous reconnecter si les permissions n'ont pas encore pris effet.
    
    ```bash
    sudo usermod -aG docker $USER
    ```
    

## Comment configurer la configuration de Zigbee2MQTT

1. Créez un nouveau répertoire de projet, ainsi qu'un répertoire `/data` pour stocker les fichiers de configuration et les données de manière persistante.
    
    ```bash
    mkdir -p ~/zigbee2mqtt/data
    ```
    
2. Créez le fichier de configuration.
    
    ```bash
    touch ~/zigbee2mqtt/data/configuration.yaml
    ```
    
3. Ouvrez le fichier avec votre éditeur de texte préféré, comme `nano` montré ci-dessous.
    
    ```bash
    nano ~/zigbee2mqtt/data/configuration.yaml
    ```
    
4. Collez le code YAML suivant dans le fichier de configuration à partir de l'interface de l'éditeur de texte.
    
    ```yaml
    homeassistant: false
    permit_join: false
    mqtt:
    
0
0base_topic: zigbee2mqtt
    
0
0server: 'mqtt://mqtt:1883'
    serial:
    
0
0port: 'tcp://<IP_OF_ZIGBEE_COORDINATOR>:<PORT>'
    frontend:
    
0
0port: 8080
    ```
    
5. Mettez à jour les détails suivants dans le fichier `configuration.yaml`, et sauvegardez les modifications.
    
    * `<MQTT_BROKER_IP>` : L'IP ou le nom d'hôte de votre broker MQTT.
        
    * `port` : Cette valeur dépend de la manière dont votre coordinateur Zigbee est connecté :
        
        * Si votre coordinateur Zigbee est connecté au réseau, vous pouvez configurer le `port` en utilisant TCP/IP comme montré dans l'exemple ci-dessus, par exemple `tcp://192.168.1.xxx:6638` où le SLZB-06 est situé à `192.168.1.xxx` sur le réseau local et `6638` est le port par défaut pour ce coordinateur Zigbee.
            
        * Si le coordinateur Zigbee est connecté à votre appareil, vous pouvez trouver le port série (comme `/dev/ttyUSB0`) en exécutant `ls /dev/tty*` avant et après avoir branché l'adaptateur à votre appareil.
            

## Comment configurer Zigbee2MQTT et le broker MQTT dans Docker

1. À la racine de votre répertoire de projet, créez un fichier `docker-compose.yaml` pour configurer le [conteneur Zigbee2MQTT](https://hub.docker.com/r/koenkk/zigbee2mqtt/) et le [conteneur broker Eclipse Mosquitto](https://hub.docker.com/_/eclipse-mosquitto) pour gérer la communication entre Zigbee2MQTT et d'autres services.
    
    ```yaml
    services:
      zigbee2mqtt:
        container_name: zigbee2mqtt
        image: koenkk/zigbee2mqtt
        restart: unless-stopped
        volumes:
          - ./data:/app/data
          - /run/udev:/run/udev:ro
        ports:
          # Port du frontend
          - 8080:8080
        environment:
          - TZ=America/Los_Angeles
      mqtt:
        image: eclipse-mosquitto:2.0
        restart: unless-stopped
        volumes:
          - "./mosquitto:/mosquitto"
        ports:
          - "1883:1883"
          - "9001:9001"
        command: "mosquitto -c /mosquitto-no-auth.conf"
    ```
    
2. Mettez à jour la variable d'environnement `TZ` si vous vous trouvez dans un fuseau horaire différent, et sauvegardez les modifications.
    

## **Lancer les conteneurs**

1. Exécutez les conteneurs.
    
    ```bash
    docker compose up -d
    ```
    
2. Testez la configuration en vérifiant les logs pour confirmer que Zigbee2MQTT fonctionne sans erreurs. Recherchez les lignes indiquant une connexion réussie au broker MQTT et l'initialisation du réseau Zigbee.
    
    ```bash
    docker compose logs
    ```
    

## **Appairer vos appareils Zigbee**

1. Une fois que Zigbee2MQTT fonctionne correctement, vous pouvez accéder au frontend à l'adresse `http://<votre-IP-appareil>:8080` depuis un navigateur web pour appairer et gérer vos appareils Zigbee.
    
2. Activez l'appairage en cliquant sur **Permettre l'appairage (tous)**, puis appairez vos appareils en les mettant en mode appairage, par exemple en maintenant un bouton de réinitialisation enfoncé.
    
3. Terminez l'appairage de tous les appareils Zigbee que vous souhaitez utiliser dans une automatisation. Dans la capture d'écran ci-dessous, j'ai appairé un bouton Aqara et une prise intelligente Third Reality.
    
    ![Bouton Aqara et prise intelligente Third Reality dans le frontend de Zigbee2MQTT](https://cdn.hashnode.com/res/hashnode/image/upload/v1731775615109/616320a6-77d0-4d14-813e-7dfde9fb8f0a.png align="center")
    
4. Donnez à vos appareils un nom convivial en utilisant l'icône de crayon. Assurez-vous de choisir un nom unique pour éviter les conflits de messagerie dans les étapes suivantes. Par exemple, si vous avez 2 prises intelligentes, vous pouvez les nommer `prise-intelligente-chambre` et `prise-intelligente-bureau`.
    

Les brokers MQTT suivent un modèle de messagerie pub/sub qui implique les éléments suivants :

* **S'abonner aux sujets MQTT** comme `zigbee2mqtt/bouton-aqara` pour surveiller les états des appareils comme écouter les pressions de boutons.
    
* **Publier sur des sujets MQTT** comme `zigbee2mqtt/third-reality/set` pour envoyer des commandes aux appareils comme une prise intelligente pour allumer une lumière.
    

Un sujet tel que `zigbee2mqtt/third-reality/set` est divisé en 3 parties :

* `zigbee2mqtt` fait référence au sujet de base (par défaut pour Zigbee2MQTT est `zigbee2mqtt`).
    
* `third-reality` fait référence à un appareil ou un groupe spécifique utilisant le nom convivial affiché dans le frontend de Zigbee2MQTT.
    
* `set` vous permet de contrôler l'appareil ou le groupe en utilisant un message JSON tel que `{"state": "TOGGLE"}`.
    

1. Entrez la commande suivante pour voir les messages MQTT publiés vers Zigbee2MQTT.
    
    ```bash
    docker logs -f zigbee2mqtt
    ```
    
2. Effectuez une action sur un appareil Zigbee, par exemple en appuyant sur un bouton, et notez les sujets que vous souhaitez utiliser dans votre automatisation pour les étapes suivantes. Par exemple, dans la capture d'écran des logs ci-dessous, il y a un sujet MQTT publié appelé `zigbee2mqtt/Aqara` lorsque le bouton Aqara est pressé.
    

![Logs de la pression du bouton Aqara](https://cdn.hashnode.com/res/hashnode/image/upload/v1731550585620/2f043360-75e1-4ef8-9549-a6bfe576ceb0.png align="center")

## **Comment créer un script d'automatisation**

Pour configurer une automatisation, vous pouvez utiliser un système externe comme Home Assistant ou Node-RED, ou utiliser les [converters externes](https://www.zigbee2mqtt.io/guide/configuration/more-config-options.html#external-converters) de Zigbee2MQTT pour répondre aux messages MQTT du broker.

Vous ne ferez pas cela. Au lieu de cela, écrivons un script JavaScript pour gérer cette automatisation, afin de garder la fonctionnalité modulaire et indépendante.

1. À partir de l'invite de commande de votre fenêtre de terminal, installez le script de configuration NodeSource sur votre Raspberry Pi.
    
    ```bash
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    ```
    
2. Installez [Node.js](https://nodejs.org/en/download/package-manager) pour l'utiliser comme environnement d'exécution pour votre script.
    
    ```bash
    sudo apt install -y nodejs
    ```
    
3. Vérifiez que l'installation s'est bien passée en affichant la version installée.
    
    ```bash
    node -v
    ```
    
4. Installez [MQTT.js](https://www.npmjs.com/package/mqtt), la bibliothèque cliente MQTT pour Node.js.
    
    ```bash
    npm install mqtt
    ```
    
5. Créez un fichier appelé `automation.js` pour contenir le script d'automatisation. Dans cet exemple, vous pouvez exécuter le script sur le Raspberry Pi. Cependant, le fichier peut être placé n'importe où et n'a même pas besoin de s'exécuter sur le même appareil que le broker MQTT. Tant que le programme peut se connecter au broker MQTT via le réseau local, il fonctionnera correctement.
    
    ```bash
    touch automation.js
    ```
    
6. Ouvrez le fichier avec votre éditeur de texte préféré, comme Nano montré ici.
    
    ```bash
    nano automation.js
    ```
    
7. Collez le code suivant dans le fichier.
    
    ```javascript
    const mqtt = require('mqtt');
    
    // Détails de connexion au broker MQTT
    const MQTT_BROKER = 'mqtt://localhost'; // Remplacez par l'adresse de votre broker
    const BUTTON_TOPIC = 'zigbee2mqtt/bouton-aqara'; // Remplacez par le sujet de votre bouton
    const PLUG_TOPIC = 'zigbee2mqtt/third-reality'; // Remplacez par le sujet de votre prise
    
    // Connexion au broker MQTT
    const client = mqtt.connect(MQTT_BROKER);
    
    // Gestion des événements de connexion
    client.on('connect', () => {
        console.log('Connecté au broker MQTT');
        // Abonnement au sujet du bouton
        client.subscribe(BUTTON_TOPIC, (err) => {
            if (!err) {
                console.log(`Abonné au sujet : ${BUTTON_TOPIC}`);
            } else {
                console.error(`Échec de l'abonnement au sujet : ${BUTTON_TOPIC}`, err);
            }
        });
    });
    
    // Gestion des messages entrants
    client.on('message', (topic, message) => {
        if (topic === BUTTON_TOPIC) {
            try {
                const payload = JSON.parse(message.toString());
                console.log('Message reçu :', payload);
                const desiredAction = payload.action;
    
                // Vérification des actions possibles
                if (desiredAction === 'single') {
                    // Envoyer un message au sujet de la prise pour basculer l'interrupteur
                    client.publish(`${PLUG_TOPIC}/set`, JSON.stringify({"state": "TOGGLE"}));
                    console.log('Basculer l'interrupteur')
                } else if (desiredAction === 'double') {
                    // Envoyer un message au sujet de la prise pour éteindre l'interrupteur
                    client.publish(`${PLUG_TOPIC}/set`, JSON.stringify({ state: 'OFF' }));
                    console.log('Éteindre l'interrupteur')
                }
            } catch (err) { 
                console.error('Échec de l'analyse du message :', err.message);
            }           
    
        }
    });
    
    // Gestion des erreurs
    client.on('error', (err) => {
        console.error('Erreur MQTT :', err);
    });
    ```
    
    Ce script se connecte au broker MQTT et s'abonne au sujet du bouton (`zigbee2mqtt/bouton-aqara`). Lorsqu'un message est reçu, il examine la charge utile. Si l'action est un clic simple (`single`), le script envoie une commande de basculement (`{state: "TOGGLE"}`) au sujet de la prise (`zigbee2mqtt/third-reality/set`), basculant l'état de la prise. Une action `double` éteint la prise.
    
    ![Modèle de messagerie pub/sub MQTT](https://cdn.hashnode.com/res/hashnode/image/upload/v1731777295907/11549e51-c2f9-44cd-af73-a0ba97eeda1e.png align="center")
    
    Mettez à jour les détails de connexion du broker MQTT et les sujets en haut du script selon vos besoins pour accommoder vos propres appareils Zigbee, et sauvegardez vos modifications.
    
8. Exécutez le script à partir de l'invite de terminal.
    
    ```bash
    node automation.js
    ```
    
9. Testez la configuration en appuyant sur le bouton. Le script devrait journaliser l'action du bouton et envoyer une commande pour basculer la prise intelligente. Vérifiez les logs du broker MQTT si la lumière ne s'allume pas.
    
10. Optionnel : Une fois que le script fonctionne comme prévu, il y a quelques étapes optionnelles supplémentaires pour s'assurer que le script redémarre lors des redémarrages. Installez un gestionnaire de processus comme [PM2](https://www.npmjs.com/package/pm2) à partir de l'invite de commande du Raspberry Pi.
    
    ```bash
    sudo npm install -g pm2
    ```
    
11. Redémarrez le script.
    
    ```bash
    pm2 start automation.js
    ```
    
12. Votre application devrait maintenant être démonisée, s'exécuter en arrière-plan et être maintenue en vie indéfiniment. Générez et configurez un script de démarrage pour maintenir PM2 et vos processus en vie à chaque redémarrage du serveur.
    
    ```bash
    pm2 startup
    ```
    
13. Copiez et collez la commande exactement comme indiqué dans la sortie du terminal, et exécutez la commande suggérée.
    
14. Sauvegardez la liste des processus pour que PM2 puisse la restaurer après un redémarrage du système.
    
    ```bash
    pm2 save
    ```
    

## **Quelle est la suite ?**

Maintenant que vous avez créé une automatisation personnalisée, il existe d'autres moyens de développer votre configuration de domotique.

* **Explorez plus d'appareils Zigbee** : Zigbee2MQTT supporte [une large gamme d'appareils](https://www.zigbee2mqtt.io/supported-devices/) de divers fabricants.
    
* **Ajoutez des comportements personnalisés** : Utilisez les [converters externes](https://www.zigbee2mqtt.io/guide/configuration/more-config-options.html#external-converters) de Zigbee2MQTT pour définir des fonctionnalités uniques pour les appareils supportés et non supportés.
    
* **Développez votre configuration** : Cette configuration flexible et légère est adaptée aux débutants et aux utilisateurs avancés qui ne veulent pas être enfermés dans des plateformes de domotique propriétaires ou des services cloud.
    

Si vous avez trouvé ce tutoriel utile, n'oubliez pas de consulter [mon matériel de domotique recommandé](https://github.com/loopDelicious/home-automation/blob/main/README.md) et [mes vidéos tutoriels sur YouTube](https://www.youtube.com/@joycejetson) pour plus d'inspiration !

Vous pouvez regarder la version vidéo de cet article ici :

%[https://www.youtube.com/watch?v=mGg_9FjDKHQ]