---
title: Comment créer un moniteur de lumière en temps réel avec Arduino et Pusher
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-30T22:09:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-realtime-light-monitor-using-arduino-and-pusher-2ec01524ec6a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xnDjT_FF-5OBCrTgHBF6aA.jpeg
tags:
- name: arduino
  slug: arduino
- name: iot
  slug: iot
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un moniteur de lumière en temps réel avec Arduino et Pusher
seo_desc: 'By Neo Ighodaro

  The Internet of Things (IoT) is changing the way we live, from wearable tech to
  smart home devices. IoT may sound complex, but in actuality it’s a fairly simple
  concept to understand. Everyday objects are constantly being transformed ...'
---

Par Neo Ighodaro

L'Internet des objets (IoT) change notre façon de vivre, des technologies portables aux appareils domestiques intelligents. L'IoT peut sembler complexe, mais en réalité, c'est un concept assez simple à comprendre. Les objets du quotidien sont constamment transformés en appareils intelligents à l'aide de capteurs et d'actionneurs.

Dans cet article, nous allons construire un moniteur de lumière ambiante Arduino en temps réel qui envoie ses lectures de capteur à une application web. Nous allons couvrir les bases de la connexion d'une carte Arduino au web et de l'envoi de données sous forme de notifications en temps réel à une application web en utilisant Pusher.

Cet article servira d'introduction à ce qui peut être réalisé avec Arduino et Pusher. Il s'adresse à ceux qui sont curieux de l'industrie du matériel et qui veulent se plonger dans le monde amusant de l'IoT.

### Conditions préalables pour construire notre intégration Arduino et Pusher

Dans ce processus, j'ai utilisé :  
 — Une carte Arduino. Carte MKR1000.  
 — [L'IDE Arduino](https://www.arduino.cc/en/Main/Software).  
 — Photocellule (disponible [ici](https://www.sparkfun.com/products/9088)).  
 — Résistance de 10k Ohm (disponible [ici](https://www.sparkfun.com/products/8374)).  
 — Plaque d'essai et fils de connexion.  
 — Une application Pusher — [Créez-en une ici](https://pusher.com/developers).  
 — Composer (disponible pour téléchargement à [https://getcomposer.org).](https://getcomposer.org).)  
 — Connaissance de PHP.

Une plaque d'essai est une carte pour le prototypage temporaire de projets matériels. Elle possède des nœuds qui conduisent le courant à travers elle.

Les fils de connexion sont utilisés pour assurer la continuité entre divers points de la plaque d'essai qui ne sont pas connectés par défaut.

### Démarrage avec Arduino

Dans cette section, nous allons configurer l'IDE Arduino et ajouter une connectivité Internet à notre carte. Nous allons découvrir comment choisir la bonne carte et ajouter une connectivité Internet.

De nombreuses cartes ne sont pas livrées avec une connectivité Internet, ce qui est quelque chose dont vous avez besoin pour créer des appareils IoT. Pour ajouter une connectivité Internet à notre carte, nous avons plusieurs options parmi lesquelles choisir : un shield, une micro-puce, ou une carte Arduino avec des capacités sans fil intégrées.

Note : un shield est essentiellement une carte d'extension qui peut être placée (montée) sur le dessus de la carte Arduino.

Il existe de nombreux types de shields :

```
1. Shield Ethernet.
```

![Image](https://cdn-media-1.freecodecamp.org/images/1FMr9efK4eZjXE0bcKcVE9tx0PsE8NH2bbjv)
_[Shield Ethernet](https://www.digikey.com/en/articles/techzone/2012/jan/networking-options-for-arduino-based-systems" rel="noopener" target="_blank" title=")_

```
2. Shield WiFi.
```

![Image](https://cdn-media-1.freecodecamp.org/images/ZIgAHwpMZ9P-IqYxcVzdzi-QyD7o17409uan)
_[Shield WiFi](https://store.arduino.cc/usa/arduino-wifi-shield" rel="noopener" target="_blank" title=")_

```
3. Shields 3G ou LTE.
```

![Image](https://cdn-media-1.freecodecamp.org/images/GwHUDbf7glVytuUviQG3yOzD7mrexSl-SoO4)
_[Shield GSM Arduino](https://store.arduino.cc/usa/arduino-gsm-shield" rel="noopener" target="_blank" title=")_

Nous allons utiliser l'[Arduino MKR1000](https://store.arduino.cc/usa/arduino-mkr1000) qui est équipé d'une puce WiFi intégrée. Cette carte est disponible dans le [magasin Arduino](https://store.arduino.cc/usa/arduino-mkr1000).

![Image](https://cdn-media-1.freecodecamp.org/images/gktBy89jXSm5YJ2pwsrSZYwauHowuenln1oG)
_[Arduino MKR1000 WIFI](https://store.arduino.cc/usa/arduino-mkr1000" rel="noopener" target="_blank" title=")_

Ensuite, téléchargez l'IDE Arduino depuis [ici](https://www.arduino.cc/en/Main/Software) et installez-le sur votre ordinateur.

Une fois l'installation terminée, procédez à l'installation de la **définition de la carte** en lançant l'IDE. Ensuite, allez dans `Outils > Cartes > Gestionnaire de cartes` où nous recherchons et installons les définitions pour le MKR1000.

![Image](https://cdn-media-1.freecodecamp.org/images/0m4FT25IL50oHvtPHAsRIGlXUanzJLXdkULq)
_Gestionnaire de cartes_

Une fois la **définition de la carte** complètement installée, allez dans `Outils | Cartes` et sélectionnez la définition de la carte nouvellement installée.

Pour connecter notre carte Arduino à Internet, nous devons installer une bibliothèque appelée `wifi101`. Pour installer la bibliothèque, allez dans `Croquis` `&`g`t; Inclure une bibliothèque` `> Gérer les bibliothèques`, puis recherchez et installez `wifi101`.

![Image](https://cdn-media-1.freecodecamp.org/images/haRKcTrKvdKLWCcZaTxS8rLhmJAOkaDnSRzH)
_Installer la bibliothèque WiFi101_

Nous pouvons tester son fonctionnement en allant dans `Fichiers > Exemples > WiFi > Conne`ctWithWpa. Cela devrait générer du code dans notre croquis. Ensuite, `modifiez` le `ssid` et le mot de passe avec le SSID et le mot de passe de votre routeur :

```
char ssid[] = "votreReseau";     //  le SSID (nom) de votre réseau    char pass[] = "motDePasseSecret";  // votre mot de passe réseau    int status = WL_IDLE_STATUS;     // le statut de la radio Wifi
```

### Construction du moniteur de lumière avec Arduino

Dans cette section, nous allons voir comment configurer le circuit et mesurer les données provenant des capteurs sur la carte MKR1000. En plus de l'Arduino MKR1000 et de la plaque d'essai et des fils de connexion habituels, nous allons avoir besoin de quelques composants supplémentaires.

* [Photocellule](https://www.sparkfun.com/products/9088)
* [Résistance de 10k Ohm](https://www.sparkfun.com/products/8374)

La photocellule est un capteur qui nous permet de détecter la lumière. Elles sont souvent considérées comme des résistances dépendantes de la lumière (LDR), des photorésistances ou des cellules CdS.

Une photocellule est essentiellement une résistance qui change sa valeur résistive (en ohms) en fonction de la quantité de lumière qui brille sur la face sinueuse.

#### **Assemblage des composants**

Tout d'abord, placez la résistance en série avec la photocellule sur la plaque d'essai, à côté de la carte Arduino.

Maintenant, connectez l'autre extrémité de la résistance à la GND sur la carte Arduino, et l'autre extrémité de la photocellule à la broche VCC de la carte Arduino.

Enfin, connectez la broche centrale entre la résistance et la photocellule à la broche analogique A0 de la carte Arduino. Le résultat final devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/osntZEkqFYLTPicQfUU5XUvlezFBbqT2Xg7I)

Une fois cela fait, nous pouvons configurer la carte pour lire les données provenant de la photocellule. Nous allons prendre les lectures de la broche analogique A0 et les imprimer sur le port série pour l'instant. Le croquis pour cette partie est vraiment facile et devrait ressembler à ceci :

Nous allons copier et coller ce croquis dans notre IDE Arduino, puis le téléverser sur la carte.

Assurez-vous que la bonne carte et les bons ports série sont sélectionnés.

```
// Broches    int sensorPin = A0;    void setup() {      // Série      Serial.begin(115200);    }
```

```
    void loop() {      // Lecture      int sensorValue = analogRead(sensorPin);      // Affichage      Serial.print("Lecture du capteur : ");      Serial.println(sensorValue);      // Attente      delay(500);    }
```

Vous pouvez **enregistrer les fichiers de croquis Arduino sur votre machine**, afin de pouvoir vous y référer plus tard. Ils peuvent être nommés comme vous le souhaitez tant qu'ils sont téléversés sur la carte Arduino.

Après avoir exécuté cela, nous ouvrons le moniteur série et observons immédiatement les lectures du capteur :

![Image](https://cdn-media-1.freecodecamp.org/images/K-OeEYRaA7PP9HZy3TAKbTohDqe6-gCVP2Oc)

Si nous mettons nos mains sur le capteur, nous verrons une diminution des valeurs mesurées par celui-ci. Concentrons-nous maintenant sur la création de l'application web.

### Configuration de l'application web

Dans cette section, nous allons créer une application web de base qui collecte les données sous forme de requête `GET` et les affiche aux utilisateurs abonnés à ce canal en temps réel. Pour l'affichage en temps réel, nous utiliserons [Pusher](http://pusher.com).

Pusher est une API hébergée simple pour intégrer rapidement, facilement et en toute sécurité des fonctionnalités bidirectionnelles en temps réel via WebSockets aux applications web et mobiles, ou à tout autre appareil connecté à Internet.

La première étape consiste à créer un compte Pusher gratuit. Si vous n'en avez pas, créez votre application sur le [tableau de bord](https://dashboard.pusher.com).

#### **Création d'une application Pusher**

Créez un compte Pusher et allez dans Vos applications > Créer une nouvelle application. Remplissez le nom de votre application, sélectionnez un cluster, choisissez JavaScript et PHP, puis nous sommes prêts à partir.

L'écran de configuration de l'application devrait ressembler à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/R5woGfHJG7bDg0AVOKuBTeXPTULtVqidi-9u)

Une fois terminé, vous recevrez vos clés d'application.

#### **Configuration de notre projet**

Nous allons créer un dossier appelé `arduino-light-monitor` dans notre répertoire racine `localhost`.

Ensuite, ouvrez votre terminal et tapez `composer require pusher/pusher-php-server`. Cela générera quelques fichiers dans notre répertoire.

Créez un fichier appelé `notification.html`. Ensuite, ajoutez le HTML et le JavaScript ci-dessous :

```
<!DOCTYPE html>    <html>    <head>      <title>Notifications du moniteur de lumière</title>      <script src="https://js.pusher.com/4.1/pusher.min.js"></script>      <script>        // Activer la journalisation Pusher - ne pas inclure cela en production        Pusher.logToConsole = true;
```

```
        // Créer une nouvelle instance de pusher avec vos identifiants        var pusher = new Pusher('APP_KEY', {            cluster: 'PUSHER_CLUSTER',// si vous avez choisi un cluster différent, remplacez-le ici            encrypted: true          });
```

```
        // s'abonner à un canal sur lequel vous écouterez        var channel = pusher.subscribe('light-monitor-channel');
```

```
        // Ce qui se passe lorsque light-readings-sent est déclenché        channel.bind('light-readings-sent', function(data){          // obtient le ul dans le dom          var ul = document.querySelector('ul');          // crée un li          var li = document.createElement('li');          // Attache les données reçues au nœud de texte          var itemText = document.createTextNode(data.value);          // Ajoute les données au li          li.appendChild(itemText);          // Ajoute le li au ul          ul.appendChild(li);        });      </script>    </head>    <body>      <ul></ul>    </body>    </html>
```

Ce qui se passe ici, c'est que nous nous abonnons à un canal appelé `light-monitor-channel`, puis nous attendons de recevoir un événement appelé `light-readings-sent`. Chaque fois que l'événement est déclenché, nous ajoutons les données reçues à notre liste.

Nous allons également créer un autre fichier appelé `index.php`. C'est le fichier qui enverra les événements au canal de notifications. Nous allons ajouter le code PHP ci-dessous au fichier :

```
<?php      require __DIR__ . '/vendor/autoload.php';
```

```
      $options = array(        'cluster' => 'PUSHER_APP_CLUSTER',        'encrypted' => true      );      $pusher = new Pusher\Pusher(        'PUSHER_APP_KEY',// remplacez par le vôtre        'PUSHER_APP_SECRET',// remplacez par le vôtre        'PUSHER_APP_ID', // remplacez par le vôtre        $options      );
```

```
      // vérifie s'il y a des données envoyées      if(isset($_GET['value'])){        $data['value'] = $_GET['value'];        // déclenche l'événement sur le canal        $pusher->trigger('light-monitor-channel', 'light-readings-sent', $data);      } else {        echo "Rien à faire";      }    ?>
```

Si vous avez besoin d'un endroit pour héberger votre contenu, vous pouvez aller sur [000webhost.com](http://000webhost.com) et créer un sous-domaine gratuit où vous pourrez téléverser le contenu de votre dossier arduino-light.

Nous allons le tester en ouvrant `notification.html` et `index.php` dans deux navigateurs différents. Lorsque nous rechargeons `index.php`, nous devrions obtenir un nouvel élément de liste ajouté avec une valeur de « Requête vide ». Si nous essayons `index.php?value=123`, nous devrions obtenir `value 123` ajouté à notre liste de notifications en temps réel.

N'est-ce pas tout simplement génial ?

### Envoi des lectures du capteur à l'application web

Enfin, nous allons voir comment envoyer les données de la carte Arduino au serveur.

En continuant à partir du croquis que nous avions auparavant, nous remplaçons simplement cela en notant les parties importantes :

```
// Broches    int sensorPin = A0;
```

```
    char ssid[] = "nom_wifi"; // votre nom wifi    char pass[] = "mot_de_passe_wifi"; // votre mot de passe wifi    int status = WL_IDLE_STATUS;
```

```
    char server[] = "votreexempleserveur.com"; // remplacez par votre localhost ou domaine
```

```
    // Créer une instance de WiFiClient    WiFiClient client;
```

```
    // Nous définissons l'intervalle auquel nous voulons envoyer les données    unsigned long lastConnectionTime = 0;    const unsigned long postingInterval = 60L * 1000L; // cela implique 60,000L, le L représente le type de données long
```

```
    void setup() {      // Série      Serial.begin(115200);
```

```
      // Tentative de connexion au réseau Wifi :      while ( status != WL_CONNECTED) {
```

```
        Serial.print("Tentative de connexion au SSID WPA : ");        Serial.println(ssid);
```

```
        // Connexion au réseau WPA/WPA2 :        status = WiFi.begin(ssid, pass);
```

```
        // Attendre 10 secondes pour la connexion :        delay(10000);      }
```

```
      // vous êtes connecté maintenant      Serial.print("Vous êtes connecté au réseau");    }
```

```
    void loop() {      if(millis() - lastConnectionTime > postingInterval) {        // Mesurer le niveau de lumière        int sensorValue = analogRead(sensorPin);
```

```
        // Envoyer la valeur au serveur        sendHTTPRequest(sensorValue);      }    }
```

```
    void sendHTTPRequest(int sensorValue){      // Fermer la connexion existante      client.stop();
```

```
      // Connexion et envoi de la requête      if (client.connect(server, 80)) {
```

```
        Serial.println("connexion...");
```

```
        // Envoyer la requête HTTP GET :        client.println("GET /light/?value=" + String(sensorValue) + " HTTP/1.1");        client.println("Host: yourexampleserver.com");        client.println("User-Agent: ArduinoWiFi/1.1");        client.println("Connection: close");        client.println();
```

```
        // Noter l'heure à laquelle la connexion a été établie :        lastConnectionTime = millis();      }      else {        // si vous n'avez pas pu établir de connexion :        Serial.println("échec de la connexion");      }    }
```

Dans le code ci-dessus, nous créons une connexion au WiFi spécifié `ssid` en utilisant une instance de `WiFiClient`. Nous allons utiliser cette connexion pour interagir avec notre serveur distant.

Dans la fonction `setup``()`, nous traitons l'initialisation de la [Série](https://www.arduino.cc/reference/en/language/functions/communication/serial/) et la connexion au réseau WiFi spécifié par les variables `ssid` et `pass` ci-dessus.

Dans la fonction `loop``()`, nous vérifions si nous sommes dans l'intervalle de publication. Ensuite, si nous y sommes, nous prenons la lecture et faisons un appel à la fonction `sendHTTPRequest` définie ci-dessous.

Dans la fonction `sendHTTPRequest``()`, nous acceptons un paramètre appelé `sensorValue`. Comme Arduino exécute le code en boucle, la première chose à faire est d'arrêter toute ouverture précédente de la connexion client avec l'instruction `client.stop()`. Cela empêchera les connexions d'être créées et les empêchera d'être rejetées après avoir été utilisées.

Ensuite, nous essayons de nous connecter au serveur défini dans la variable `server[]`. Nous vérifions si la connexion peut être établie, et si ce n'est pas le cas, nous imprimons sur la Série « échec de la connexion ». Une fois le client connecté, nous envoyons la valeur de la broche du capteur via l'URL à notre application web.

Si nous testons cela maintenant, nous aurons la lecture du capteur de lumière toutes les minutes.

![Image](https://cdn-media-1.freecodecamp.org/images/xbLXp8j2TwoE7DG3MJggHJn7H-HaQCBLBT8v)

### Conclusion

Nous avons réussi à construire un moniteur de lumière en utilisant Arduino et Pusher. Si vous avez apprécié ce tutoriel et que vous souhaitez passer de zéro à héros dans le monde de l'IoT, vous devriez consulter le livre « Internet of Things with Arduino Cookbook » de Marco Schwartz. Il contient plus de 60 recettes qui vous aideront à construire des solutions IoT intelligentes et vous surprendront avec des projets IoT captivants que vous pensiez exister uniquement dans les films de James Bond.

Si vous avez des questions ou d'autres idées sur l'intégration de l'IoT avec Pusher, n'hésitez pas à laisser un commentaire ci-dessous !

Ceci a été initialement publié sur notre [blog](https://blog.pusher.com/make-a-realtime-light-monitor-using-arduino-and-pusher/).