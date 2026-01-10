---
title: Comment construire un système IIoT en utilisant Apache NiFi, MiNiFi, C2 Server,
  MQTT et Raspberry Pi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-27T19:29:34.000Z'
originalURL: https://freecodecamp.org/news/building-an-iiot-system-using-apache-nifi-mqtt-and-raspberry-pi-ce1d6ed565bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*3VQlvDAxQimCkjdcSzhteg.png
tags:
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment construire un système IIoT en utilisant Apache NiFi, MiNiFi, C2
  Server, MQTT et Raspberry Pi
seo_desc: 'By Abdelkrim Hadjidj

  How long do you think it takes to build an advanced Industrial IoT prototype that
  can:


  Collect data from sensors to a gateway at every factory

  Move sensors data from one or several factories to the Cloud or the Data Center

  Autom...'
---

Par Abdelkrim Hadjidj

Combien de temps pensez-vous qu'il faut pour construire un prototype IoT industriel avancé qui peut :

* Collecter des données à partir de capteurs vers une passerelle dans chaque usine
* Transférer les données des capteurs d'une ou plusieurs usines vers le Cloud ou le Centre de Données
* Déployer automatiquement de nouvelles configurations à tous les appareils de périphérie
* Prendre en charge un grand volume de données et une sécurité de bout en bout

Avec le bon outil, vous pouvez construire un tel système en moins d'une heure ! Dans cet article de blog, je vais vous montrer comment implémenter un prototype IIoT avancé en utilisant du matériel Raspberry Pi et des logiciels open source (broker MQTT, Apache NiFi, MiNiFi et MiNiFi C2 Server). Je me concentrerai sur l'architecture, la connectivité, la collecte de données et la reconfiguration automatique.

Cet article est destiné à être le début d'une série d'articles sur l'IoT. Le traitement en périphérie et l'analyse des données seront les sujets des articles suivants, alors restez à l'écoute :)

### Architecture IoT industrielle

Il existe de nombreuses architectures de référence IoT. Souvent, dans les environnements industriels, vous n'avez pas un accès direct aux capteurs et aux systèmes de contrôle. Une passerelle est utilisée pour faire le pont entre le monde OT et le monde IT. Pour cette raison, l'architecture IIoT inclut souvent des appareils de périphérie, des passerelles, des hubs régionaux et enfin des systèmes de stockage/traitement.

L'image suivante montre l'architecture globale de notre système et les outils logiciels que nous utiliserons à chaque niveau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3VQlvDAxQimCkjdcSzhteg.png)
_Architecture IIoT_

**Au niveau de la périphérie**, les capteurs collectent des informations sur le monde numérique et les envoient à une passerelle via une variété de protocoles filaires et sans fil (Serial, RS-485, MODBUS, CAN bus, OPC UA, BLE, WiFi, etc.). Dans notre exemple, nous utiliserons divers capteurs (lumière, température, caméras, accéléromètres, etc.) qui envoient des données à la passerelle via WiFi.

**La passerelle** est un Raspberry Pi exécutant un broker Mosquitto et un agent MiNiFi. [Mosquitto](https://mosquitto.org/) est un broker de messagerie open source et léger que nous utilisons pour exposer les données des capteurs via le protocole MQTT. MQTT a une empreinte minimale, ce qui le rend adapté aux applications IoT et aux matériels à ressources limitées, tels que les téléphones ou les microcontrôleurs.

Apache MiNiFi — un sous-projet d'Apache NiFi — est un agent léger qui implémente les fonctionnalités principales d'Apache NiFi, en se concentrant sur la collecte de données à la périphérie.

Les objectifs de conception de MiNiFi sont : une petite taille et une faible consommation de ressources, une gestion centrale des agents et une intelligence de périphérie. MiNiFi peut être facilement intégré avec NiFi via le protocole Site-to-Site (S2S) pour construire une solution de gestion de flux de bout en bout qui est scalable, sécurisée et fournit une chaîne de traçabilité complète des informations (provenance).

Dans notre système, MiNiFi s'abonnera à tous les sujets du broker Mosquitto et transférera chaque nouveau message à NiFi au niveau régional. Nous pouvons également l'utiliser pour nous connecter à un système SCADA ou à tout autre fournisseur de données OT.

**Au niveau régional**, nous avons deux composants :

[Apache NiFi](https://nifi.apache.org/) est une plateforme de flux de données puissante avec plus de 200 connecteurs prêts à l'emploi. Grâce à son interface utilisateur, la conception des flux de données devient rapide et facile.

NiFi ne sacrifie pas la puissance pour la simplicité. En effet, c'est un système distribué hautement scalable avec une livraison garantie, une contre-pression et une distribution de charge. Ces fonctionnalités font de NiFi un excellent outil pour les applications IoT où la qualité du réseau peut être difficile.

Dans notre système, NiFi joue le rôle central de collecte des données de chaque usine et de leur acheminement vers plusieurs systèmes et applications (HDFS, HBase, Kafka, S3, etc.).

[MiNiFi C2 Server (MiNiFi Commande & Control)](https://cwiki.apache.org/confluence/display/MINIFI/C2+Design+Proposal) est un autre sous-projet d'Apache NiFi actuellement en développement. Son rôle est de fournir un point central de configuration pour des centaines ou des milliers d'agents MiNiFi dans la nature. Le serveur C2 gère des classes d'applications versionnées (configurations de flux MiNiFi) et les expose via une API Rest. Les agents MiNiFi peuvent se connecter à cette API à une fréquence définie pour mettre à jour leur configuration.

Une fois les données arrivées sur les serveurs de l'entreprise, dans **le Cloud ou au Centre de Données**, il existe un large éventail d'applications qui peuvent être implémentées. La surveillance en temps réel, l'analyse et l'optimisation des processus, ou la maintenance prédictive en sont quelques exemples. Le traitement des données et la mise en œuvre des cas d'utilisation seront discutés dans un futur article.

### Implémentation du système

Commençons à construire notre prototype.

#### Préparation du Raspberry Pi : MQTT et MiNiFi

Pour installer le broker MQTT Mosquitto et l'agent MiNiFi, exécutez les commandes suivantes sur votre Raspberry Pi.

Pour avoir une petite taille, MiNiFi est livré avec un ensemble minimal de processeurs par défaut. Il est possible d'ajouter n'importe quel processeur NiFi en déployant le NAR (NiFi Archive) dans le répertoire lib. Dans la dernière commande du bloc ci-dessous, j'ajoute le NAR du processeur MQTT.

```
sudo apt-get update#installer et exécuter le broker Mosquitto sur le port par défaut 1883sudo apt-get install mosquittomosquitto#installer et préparer l'agent MiNiFiwget http://apache.crihan.fr/dist/nifi/minifi/0.4.0/minifi-0.4.0-bin.tar.gztar -xvf minifi-0.4.0-bin.tar.gzcd minifi-0.4.0#ajouter le processeur mqttwget https://github.com/ahadjidj-hw/NiFi/raw/master/nifi-mqtt-nar-1.5.0.nar -P ./lib/
```

Par défaut, la configuration d'un agent MiNiFi nécessite l'édition du fichier ./conf/config.yml pour inclure la liste des processeurs utilisés et leurs configurations. La configuration peut être écrite manuellement ou conçue à l'aide de l'interface utilisateur de NiFi et exportée sous forme de modèle. Le modèle est un fichier XML que nous devons convertir en fichier YML avec le [MiNiFi toolkit](https://nifi.apache.org/minifi/minifi-toolkit.html). Voici un exemple de [fichier de configuration](https://github.com/apache/nifi-minifi/blob/master/minifi-bootstrap/src/test/resources/config.yml) qui suit un fichier et envoie chaque ligne à un NiFi distant via S2S.

Pour notre projet, nous n'utiliserons pas ces étapes manuelles. Avec de nombreux agents MiNiFi fonctionnant dans des usines géographiquement distribuées, il n'est pas possible d'arrêter manuellement, d'éditer le config.yml, puis de redémarrer chaque agent chaque fois que leur configuration doit changer.

MiNiFi utilise un « Change Ingestor » par lequel l'agent est notifié d'une nouvelle configuration potentielle. Les change ingestors sont des modules pluggables, et actuellement trois ingestors sont supportés OOTB :

* FileChangeIngestor
* RestChangeIngestor
* PullHttpChangeIngestor

Nous utiliserons un PullHttpChangeIngestor pour interroger un serveur C2 à chaque période de temps et télécharger toute nouvelle configuration disponible. Pour configurer cet ingestor, éditez le fichier ./conf/bootstrap.conf, décommentez les lignes correspondantes et définissez les propriétés de l'ingestor comme suit :

```
nifi.minifi.notifier.ingestors=org.apache.nifi.minifi.bootstrap.configuration.ingestors.PullHttpChangeIngestor
```

```
# Nom d'hôte à partir duquel récupérer les configurations
```

```
nifi.minifi.notifier.ingestors.pull.http.hostname=c2-server
```

```
# Port à partir duquel récupérer les configurations
```

```
nifi.minifi.notifier.ingestors.pull.http.port=10080
```

```
# Chemin pour récupérer les configurations
```

```
nifi.minifi.notifier.ingestors.pull.http.path=/c2/config
```

```
# Chaîne de requête pour récupérer les configurations
```

```
nifi.minifi.notifier.ingestors.pull.http.query=class=iot-minifi-raspberry-agent
```

```
# Période à laquelle récupérer les configurations, par défaut 5 minutes si commenté
```

```
nifi.minifi.notifier.ingestors.pull.http.period.ms=60000
```

Avec cette configuration, chaque agent MiNiFi interrogera l'API REST du serveur C2 à l'adresse [http://c2-server:10080/c2/config](http://nifi-dev:10080/c2/config) toutes les 1 minute et demandera la dernière configuration pour la classe « iot-minifi-raspberry-agent ».

Note : la fréquence de 1 minute est uniquement à des fins de démonstration. Vous ne mettrez pas à jour vos agents aussi fréquemment.

Ne démarrez pas votre agent maintenant, et passons au niveau régional pour configurer le serveur MiNiFi C2 et NiFi.

#### Installation et configuration du serveur MiNiFi C2

Installez le serveur MiNiFi C2 sur un serveur public accessible depuis les agents MiNiFi. Vous pouvez utiliser un déploiement C2 hiérarchique pour les applications à réseau contraint comme décrit quelques lignes plus bas. Exécutez la commande suivante pour installer le serveur C2 :

```
wget http://apache.crihan.fr/dist/nifi/minifi/0.4.0/minifi-c2-0.4.0-bin.tar.gztar -xvf minifi-c2-0.4.0-bin.tar.gzcd minifi-c2-0.4.0
```

Le serveur C2 expose les applications MiNiFi via une API REST organisée par classes. C2 supporte des « Configuration Providers » pluggables et supporte actuellement :

* Le **CacheConfigurationProvider**, qui regarde le répertoire sur le système de fichiers ou sur S3
* Le **DelegatingConfigurationProvider**, qui délègue à un autre serveur C2 pour permettre des structures C2 hiérarchiques
* Le **NiFiRestConfigurationProvider**, qui récupère les modèles à partir d'une instance NiFi via son API REST

Configurez le serveur C2 pour utiliser NiFi comme fournisseur de configuration. Éditez le fichier ./conf/minifi-c2-context.xml et fournissez l'adresse du serveur NiFi [http://nifi-dev:8080](http://nifi-dev:8080)

#### Installation et configuration du serveur NiFi

Installez NiFi sur un serveur accessible depuis le serveur C2 et exécutez-le.

```
wget http://apache.crihan.fr/dist/nifi/1.6.0/nifi-1.6.0-bin.tar.gztar -xvf nifi-1.6.0-bin.tar.gzcd nifi-1.6.0./bin/nifi.sh start
```

Connectons-nous à l'interface utilisateur de NiFi à l'adresse [http://nifi-dev:8080/nifi/](http://nifi-dev:8080/nifi/) et créons le flux qui s'exécutera dans les agents MiNiFi. Mais avant cela, ajoutez un port d'entrée au canevas racine et nommez-le « from Raspberry MiNiFi ». C'est ici que NiFi recevra les fichiers de flux de MiNiFi.

Ajoutez un processeur consumeMQTT pour vous abonner au broker Mosquitto et vous abonner à tous les sujets sous _iot/sensors_. Notez que tcp://raspberrypi:1883 ici est équivalent à tcp://localhost:1883, puisque ce flux s'exécutera sur le Raspberry Pi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_2o7XYaLQis3B_K7UeMlNA.png)

Utilisez un processeur UpdateAttribute pour ajouter un attribut « version » que nous utiliserons pour montrer la fonctionnalité de reconfiguration. Vous pouvez ajouter n'importe quel attribut que vous voulez : horodatage, nom de l'agent, emplacement, etc.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AlovfoMCxTmo8fwIY_T9Jg.png)

Et enfin, ajoutez un Remote Process Group (RPG) pour envoyer les événements consommés à NiFi. Connectez ces trois processeurs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pipjKZaixzgo6mx61D4ioA.png)

Votre flux ressemble maintenant à la capture d'écran ci-dessous. Le flux de gauche s'exécutera dans NiFi pour recevoir les données de MiNiFi. Le flux de droite ici est uniquement pour la conception et s'exécutera effectivement sur chaque Raspberry Pi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8qMAq8mrVgwbY3MM4G6WZg.png)

Enregistrez le flux de droite sous forme de modèle sous le nom « iot-minifi-raspberry-agent.v1 ». La convention de nommage ici est très importante. Nous devons utiliser le même nom que le nom de classe utilisé dans la configuration de bootstrap de MiNiFi.

### Déploiement et démarrage de l'application

Avant de démarrer les agents MiNiFi sur le Raspberry Pi, vérifions si le serveur C2 est bien configuré. Ouvrez l'URL suivante dans votre navigateur web : [http://c2-server:10080/c2/config?class=iot-minifi-raspberry-agent&version=1](http://c2-server:10080/c2/config?class=iot-minifi-raspberry-agent&version=1). Le serveur C2 répond avec un fichier contenant la configuration du modèle que nous avons construit, au format YML. C'est génial.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dswF9vj5b8f8arb5dOAqAg.png)
_Résultats de l'appel à l'API Rest C2_

Si vous regardez les logs du C2, vous pouvez voir que le serveur a reçu une requête avec les paramètres {class=[iot-minifi-raspberry-agent], version=[1]}

![Image](https://cdn-media-1.freecodecamp.org/images/1*bGTZK8FAhk1lZyksark5Zw.png)
_Logs du serveur C2 après l'appel à l'API Rest_

Maintenant que la communication entre les différents composants de l'architecture (MQTT, MiNiFi, NiFi et C2) fonctionne, démarrez l'agent MiNiFi sur le Raspberry Pi avec la commande :

```
./bin/minifi.sh start
```

Après quelques secondes, vous voyez les logs suivants du serveur C2. L'hôte 192.168.1.50 (il s'agit de l'adresse IP du Raspberry Pi) a demandé au serveur C2 de lui donner la dernière version de la classe « iot-minifi-raspberry-agent ». Comparé à notre précédent appel avec le navigateur web, vous remarquerez que l'agent MiNiFi n'a pas spécifié de version. Si vous ouvrez maintenant la configuration de l'agent MiNiFi à l'adresse ./conf/config.yml, vous trouverez le même fichier de configuration que nous avons récupéré de l'API Rest C2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7Q4mCfsw_eUUVhJflVvs4g.png)
_Logs du serveur C2_

De plus, MQTT montre que l'agent MiNiFi s'est connecté au broker et s'est abonné aux sujets iot/sensors/#

![Image](https://cdn-media-1.freecodecamp.org/images/1*nKnkdcvyDHg9V3mkX5j57Q.png)
_Logs MQTT après le démarrage de l'agent MiNiFi_

Parfait ! Le système IIoT fonctionne à merveille. Maintenant, démarrons nos capteurs pour générer des données et les publier dans MQTT. MiNiFi commencera alors à consommer les données et à les envoyer à NiFi comme le montre la capture d'écran suivante où nous avons reçu 196 messages.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_3ePgulNqJI5y7bf8PuV8g.png)

Maintenant, inspectons l'un de ces messages avec la fonctionnalité de provenance de NiFi. Ces données proviennent du capteur de lumière « iot/sensors/LightIntensity/z » et la version de l'application est 1.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J3H9LUSHv-0_0o65xE3PrA.png)

### Redéploiement automatique à chaud

Maintenant que notre IIoT fonctionne et que les données circulent de chaque usine vers notre centre de données, déployons une nouvelle application. Pour notre test, nous apporterons une modification mineure à la configuration de notre agent MiNiFi. Allez dans l'interface utilisateur web de NiFi et éditez le processeur updateAttribute. Définissez l'attribut « version » à 2 au lieu de 1 et enregistrez le flux dans un nouveau modèle « iot-minifi-raspberry-agent.v2 ». C'est tout ! La nouvelle application sera déployée automatiquement.

Vous pouvez voir les logs du serveur C2 ci-dessous montrant qu'une nouvelle version V2 a été détectée. Le serveur C2 ne possède pas cette version dans son cache et commence un processus de téléchargement et de conversion.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m3jNaye1W-hWBIdvKsxK8w.png)
_Réaction du serveur C2 à un nouveau modèle_

Ensuite, les agents MiNiFi détectent la nouvelle configuration, sauvegardent la configuration précédente, déployent la nouvelle et redémarrent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CpLj2Fvhyw7J3KPjPsSU-A.png)

Maintenant, regardons les données provenant des agents. Comme vous pouvez le voir dans l'interface utilisateur de provenance ci-dessous, ces données proviennent d'un gyroscope et ont une version d'application 2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*143i4FJ_vk6jkZQywxzxig.png)

### Conclusions

Apache NiFi et son écosystème (MiNiFi et C2 server) sont des outils puissants pour la gestion de données IoT de bout en bout. Ils peuvent être utilisés pour construire facilement et rapidement des applications IoT avancées avec des architectures flexibles et des fonctionnalités avancées (déploiement automatique à chaud, provenance des données, contre-pression, etc.).

Dans les futurs articles, je vous montrerai comment utiliser ces données, sécuriser la plateforme et implémenter des scénarios de traitement avancés en périphérie. En attendant, vous pouvez lire [cet article](https://medium.com/@abdelkrim.hadjidj/best-practices-for-using-apache-nifi-in-real-world-projects-3-takeaways-1fe6912101db) sur la manière dont Renault, un constructeur automobile multinational, utilise Apache NiFi dans les projets IIoT et quelles sont les meilleures pratiques qu'ils ont adoptées.

Merci d'avoir lu. Comme toujours, les commentaires et suggestions sont les bienvenus.

Si vous avez trouvé cet article utile, alors donnez-lui quelques applaudissements et suivez-moi pour plus d'articles sur le Big Data et l'IoT !

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZEb8WxL62ot7Wv5nRuinbQ.gif)
_Applaudissements et abonnement_