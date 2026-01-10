---
title: Comment exécuter Grafana avec DeviceHive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T21:44:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-grafana-with-devicehive-b2f57fe998a8
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Vam37zski44iqI5J.gif
tags:
- name: Grafana
  slug: grafana
- name: Internet of Things
  slug: internet-of-things
- name: iot
  slug: iot
- name: open source
  slug: open-source
- name: technology
  slug: technology
seo_title: Comment exécuter Grafana avec DeviceHive
seo_desc: 'By Nikolay Khabarov

  DeviceHive is an IoT platform which has plenty of different components. The Grafana
  plugin is one of them. This plugin can gather data from a DeviceHive server and
  display it with different dashboards using the very popular tool —...'
---

Par Nikolay Khabarov

[DeviceHive](https://devicehive.com/?utm_source=medium&utm_medium=social&utm_campaign=d-spring-2018) est une plateforme IoT qui possède de nombreux composants différents. Le plugin Grafana en est un. Ce plugin peut collecter des données à partir d'un serveur DeviceHive et les afficher avec différents tableaux de bord en utilisant l'outil très populaire — Grafana. Cet article explique comment créer un tableau de bord Grafana avec DeviceHive. Par exemple, cela utilise la broche analogique de la puce ESP8266 pour visualiser la tension sur celle-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/nOECJ-zXVy1bAnBBNhEDO3mo7ZehFbSXHG6r)

### Données

Pour afficher quoi que ce soit sur un tableau de bord, nous avons besoin de données. En termes de serveur DeviceHive, les données peuvent être fournies via des 'commands' et des 'notifications'. Les commandes sont généralement utilisées pour transmettre des messages à un appareil que l'appareil doit exécuter, tandis que les 'notifications' sont l'inverse, les appareils notifient leurs abonnés de certains événements. Les 'commands' et les 'notifications' sont essentiellement des messages JSON simples.

Ces deux entités peuvent être utilisées pour tracer des graphiques, afficher du texte statique, un indicateur, un tableau ou tout autre composant Grafana. Pour cet article, nous générerons des notifications en utilisant un firmware spécial DeviceHive pour la puce ESP8266. Ce firmware permet à la puce de se connecter directement à un serveur DeviceHive en utilisant son protocole et dispose de nombreuses [commandes documentées](https://github.com/devicehive/esp8266-firmware/blob/develop/DeviceHiveESP8266.md) qui peuvent être émises depuis le côté serveur.

### Génération de notifications avec le firmware ESP8266

Les binaires pour le firmware DeviceHive sont disponibles [ici](https://github.com/devicehive/esp8266-firmware/releases). Téléchargez la dernière version et flashez ce firmware sur votre puce. L'archive de publication contient de la documentation sur la façon de procéder, mais si vous avez une carte de type 'nodemcu', vous devez simplement connecter la carte via un câble microUSB à votre ordinateur et exécuter l'utilitaire 'esp-flasher' de l'archive de publication pour votre système d'exploitation et attendre qu'il flashe la carte. Après avoir flashé la carte, il est nécessaire de configurer la puce pour qu'elle utilise un réseau Wi-Fi, un serveur DeviceHive et des identifiants. Il existe deux façons de procéder : en utilisant un terminal de type posix avec l'utilitaire 'esp-terminal' ou sans fil comme décrit [ici](https://github.com/devicehive/esp8266-firmware/blob/develop/DeviceHiveESP8266.md#wireless-configuring).

Il existe un [service de terrain de jeu gratuit](https://playground.devicehive.com/?utm_source=medium&utm_medium=social&utm_campaign=d-spring-2018), qui peut être utilisé gratuitement pour essayer un serveur DeviceHive. Après que votre puce soit connectée à votre serveur ou terrain de jeu, allez dans le panneau d'administration du serveur, trouvez votre appareil ESP8266 dans la liste des appareils et émettez la commande 'adc/int' avec les paramètres '{"0": 500}'.

![Image](https://cdn-media-1.freecodecamp.org/images/rpg8hn6zzqcOAuNC0aVxEPQmJQM2rSpD79zu)

Cette commande fait en sorte que l'esp8266 rapporte toutes les 500ms la tension sur l'entrée ADC #0 (la seule que possède l'ESP8266). Après être passé aux 'notifications', il devrait y avoir un écran comme :

![Image](https://cdn-media-1.freecodecamp.org/images/fW573XDzKshEDdhmbSvyuh6ok-uV8Vs5rkXn)

C'est la tension sur la broche d'entrée de la puce. Et ce type de données nous convient pour l'afficher avec Grafana : les notifications contiennent des données (paramètres dans notre cas), les notifications arrivent en continu, et toutes les notifications de DeviceHive ont toujours un horodatage. En ayant un capteur analogique connecté à cette broche, il est possible d'afficher ces données avec Grafana.

### Installation du plugin DeviceHive Grafana dans Grafana

Grafana peut être utilisé comme un service local ou comme un service hébergé. Pour installer Grafana localement, veuillez vous référer à la « [Documentation officielle. Installation de Grafana](http://docs.grafana.org/installation/) ».

Vous pouvez trouver comment installer les plugins dans la « [Documentation officielle. Installation des plugins](http://docs.grafana.org/plugins/installation/) ».

Pour installer la source de données DeviceHive via grafana-cli, vous pouvez utiliser la commande suivante :

`$ grafana-cli plugins install devicehive-devicehive-datasource`

Si vous souhaitez installer le plugin manuellement, vous devez effectuer les étapes suivantes :

Prérequis, ces packages doivent être installés :

* Grafana >= 4.6
* NodeJs >= 8 (optionnel)
* NPM >= 5 (optionnel)
* Grunt (`npm install -g grunt`) (optionnel)

Vous devez également avoir les permissions de copier des données dans le dossier des plugins (vous pouvez le définir dans `grafana.ini` dans `Paths->plugins`).

1. Clonez ce dépôt dans le dossier des plugins — `git clone [https://github.com/devicehive/devicehive-grafana-datasource.git](https://github.com/devicehive/devicehive-grafana-datasource.git;)`[;](https://github.com/devicehive/devicehive-grafana-datasource.git;)
2. Les étapes suivantes sont optionnelles (au cas où vous souhaitez reconstruire le code source de la source de données) :  
2.1 Allez dans le dossier — `cd devicehive-grafana-datasource`;  
2.2 Installez tous les packages — `npm install`;  
2.3 Construisez le plugin — `npm run build`;
3. Redémarrez le serveur Grafana
4. Ouvrez Grafana dans le navigateur;
5. Ouvrez le menu latéral en cliquant sur l'icône Grafana dans l'en-tête supérieur;
6. Dans le menu latéral, cliquez sur `Data Sources`;
7. Cliquez sur `+ Add data source` dans l'en-tête supérieur;
8. Sélectionnez `DeviceHive` dans le menu déroulant `Type`;
9. Configurez la source de données.

Après l'installation, vous pourrez voir le plugin de source de données DeviceHive dans la liste des plugins installés (voir l'image ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/AzonaJcVOdW9Hk3FCwUttkuiPJ9C7eWLQB1C)

### Ajout d'une source de données Grafana

Pour ajouter une source de données DeviceHive, vous devez effectuer les étapes suivantes :

1. Ouvrez le menu latéral en cliquant sur l'icône Grafana dans l'en-tête supérieur;
2. Dans le menu latéral, cliquez sur `Data Sources`;
3. Cliquez sur `+ Add data source` dans l'en-tête supérieur;
4. Sélectionnez `DeviceHive` dans le menu déroulant `Type`;

Regardez l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/qc1uOouwh6YxgGqfdsQIZEDP1eYpxl2ecySv)

Pour configurer la source de données DeviceHive, vous devez remplir les champs suivants :

URL du serveur (est le chemin vers le serveur WebSocket de DeviceHive. Pour le terrain de jeu, il s'agit de ws://playground.devicehive.com/api/websocket)  
ID de l'appareil (identifiant unique de l'appareil DeviceHive)  
Login/Mot de passe ou AccessToken — identifiants pour passer l'authentification

Vous pouvez également spécifier le RefreshToken pour le rafraîchissement automatique de l'AccessToken

Sur l'image ci-dessous, vous pouvez observer le flux de configuration :

![Image](https://cdn-media-1.freecodecamp.org/images/5gXrxTalhd08rH2yVadrRIuNobmWhTTVaSnu)

Après avoir ajouté et configuré une source de données DeviceHive, elle devrait exister dans la liste des sources de données comme dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/Axn57tNj1KkdGbqIsrstGx7Oa66jk7U7x6qL)

### Créer un nouveau tableau de bord

Pour créer un nouveau tableau de bord, il vous suffit de cliquer sur le bouton « New » dans le panneau de la barre latérale comme montré dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/UxyJ0vnK8ijGBQ3Wc2JtnQIg2GX9GqF6l0DP)

Dans cet article, nous montrerons des exemples sur le panneau Graph, donc, cliquez sur le bouton Graph :

![Image](https://cdn-media-1.freecodecamp.org/images/zRKDMidgaJZq8GeifLHTEacB2NlspwNzOxxf)

Après cela, vous pourrez voir un graphique en ligne sur votre tableau de bord :

![Image](https://cdn-media-1.freecodecamp.org/images/5jyxzmU-kWVQnXJ6ffNtKFSDWMA7n57xJCaH)

### Affichage des notifications/commandes avec le graphique de Grafana

Les notifications et les commandes sont des entités DeviceHive :  
Commande : représente un message envoyé par les clients pour les appareils  
Notification : représente un message envoyé par les appareils pour les clients

Par défaut, un message de notification ou de commande fournit le champ nommé « parameters » dans lequel un utilisateur peut transmettre ses propres données.

Au début de cet article, nous avons configuré l'appareil ESP8266 pour envoyer des notifications avec des données représentant l'état de la broche analogique #0 de la puce. Dans l'image ci-dessous, vous pouvez observer comment configurer le panneau de graphique Grafana pour qu'il affiche les données sur le graphique en ligne :

![Image](https://cdn-media-1.freecodecamp.org/images/X5Z5ZHUPRVDhfCKxt4b6hcZ8gYbuxxJJJJC3)

### Affichage des annotations sur le graphique de Grafana

Les annotations fournissent un moyen de marquer des points sur le graphique avec des événements riches. Lorsque vous survolez une annotation, vous pouvez obtenir une description de l'événement et des balises d'événement. Le champ de texte peut inclure des liens vers d'autres systèmes avec plus de détails.  
Plus d'informations sur les annotations peuvent être trouvées en suivant ce [lien](http://docs.grafana.org/reference/annotations/).

L'image ci-dessous montre comment configurer les annotations alimentées par une source de données DeviceHive.

![Image](https://cdn-media-1.freecodecamp.org/images/Lw2KYjUe7Q24ya19OuQzVxTLReW6u-Lz5EkL)

### Réglage avancé du graphique

Après avoir cliqué sur le bouton « Add converter », vous pourrez sélectionner un convertisseur.  
Un convertisseur est une fonction simple qui transforme une valeur de quelque manière.

Pour l'instant, les sources de données DeviceHive supportent les types de convertisseurs suivants :

* Scale — multiplie par une valeur donnée
* Offset — ajoute une valeur donnée
* Unit converter — convertit la valeur entre différentes unités des types de mesure mentionnés ci-dessous :
* Température ('c' — Celsius, 'f' — Fahrenheit, 'k' — Kelvin)
* Longueur ('m' — Mètre, 'mi' — Mile, 'yd' — Yard, 'ft' — Feet, 'in' — Inch)
* Poids ('kg' — Kilogramme, 'lb' — Livre, 'oz' — Ounces)
* Volume ('l' — Litre, 'gal' — Gallon, 'pt' — Pinte)

![Image](https://cdn-media-1.freecodecamp.org/images/Vtz9svdJWA6c77zySGGgT8DVarEmy1NZQXCe)

Un exemple de cette fonctionnalité est montré dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/RxgzyoJ0xAMYgNGz9WDj-RqextPoxDbGgvd0)

### Conclusion

Grafana est un outil parfait pour visualiser les données. Il est très flexible et offre de nombreuses fonctionnalités différentes pour rendre la visualisation de la manière que vous souhaitez. Grafana peut utiliser de nombreuses sources de données provenant d'une large gamme de solutions logicielles et DeviceHive en est une. L'exemple que nous avons décrit dans cet article est très simple. En utilisant ces principes, il est possible de créer des graphiques plus avancés et nous espérons que cela vous sera utile. En utilisant Grafana et DeviceHive, vous pouvez construire vos propres solutions de visualisation IoT et de plus, vous pouvez modifier les deux projets comme vous le souhaitez puisque Grafana et DeviceHive sont des logiciels open source.

_Ecrit en collaboration avec Igor Trambovetskiy, Développeur Senior chez [DeviceHive](https://devicehive.com/?utm_source=medium&utm_medium=social&utm_campaign=d-spring-2018)._