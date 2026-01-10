---
title: 'Comment fonctionnent les appareils Bluetooth Low Energy : Explication des
  services et caractéristiques GATT'
author: Nikheel Vishwas Savant
date: '2025-12-03T17:57:50.353Z'
originalURL: https://freecodecamp.org/news/how-bluetooth-low-energy-devices-work-gatt-services-and-characteristics-explained
description: 'Every time you check your smartwatch for heart rate, read the battery
  level of wireless earbuds, unlock a Bluetooth smart lock, or watch sensor data stream
  into an app, you are experiencing the result of GATT working quietly in the background.

  GATT i...'
subtitle: ''
seo_title: 'Comment fonctionnent les appareils Bluetooth Low Energy : Explication
  des services et caractéristiques GATT'
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1764781967963/2ccd66f7-3a5f-490f-af66-e1091ef4e34d.png
tags:
- name: Bluetooth GATT
  slug: bluetooth-gatt
- name: bluetooth
  slug: bluetooth
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: sensors
  slug: sensors
- name: handbook
  slug: handbook
seo_desc: 'Every time you check your smartwatch for heart rate, read the battery level
  of wireless earbuds, unlock a Bluetooth smart lock, or watch sensor data stream
  into an app, you are experiencing the result of GATT working quietly in the background.

  GATT i...'
---


Chaque fois que vous consultez votre montre connectée pour votre fréquence cardiaque, lisez le niveau de batterie d'écouteurs sans fil, déverrouillez une serrure intelligente Bluetooth ou regardez des données de capteurs défiler dans une application, vous faites l'expérience du travail silencieux du GATT en arrière-plan.

GATT signifie Generic Attribute Profile (Profil d'attribut générique). Il fournit la structure qui permet aux appareils Bluetooth Low Energy (BLE) d'échanger des informations significatives. Sans le GATT, les radios Bluetooth se contenteraient de déplacer des bits d'avant en arrière sans format ni interprétation convenus. Avec le GATT, les appareils peuvent communiquer dans un langage prévisible et compréhensible.

Imaginez les radios Bluetooth comme deux personnes se parlant dans une pièce. Les ondes radio leur permettent de discuter, mais sans langue commune, l'échange est inutile. Le GATT fournit cette langue commune. Il définit le vocabulaire, la grammaire et la structure des phrases. Au lieu d'un binaire aléatoire, nous obtenons des messages clairs comme Fréquence Cardiaque égale 78 bpm, Batterie égale 92 % ou Interrupteur égal ON.

Grâce au GATT, les appareils de différents fabricants peuvent interopérer. Une ceinture cardio Polar peut se connecter à un vélo Peloton. Un téléphone Samsung peut lire la température d'un capteur médical. Une Apple Watch peut contrôler des ampoules intelligentes Philips Hue. Ces appareils ne partagent ni matériel, ni entreprise, ni système d'exploitation, mais ils peuvent coopérer car le GATT définit une structure universelle pour exposer et accéder aux données.

Une fois que vous comprenez le GATT, le Bluetooth devient beaucoup moins mystérieux. La communication devient une question de lecture ou d'écriture de valeurs dans une petite base de données structurée. Le débogage devient logique. Le développement d'applications BLE devient simple. Et construire votre propre appareil IoT devient réalisable, même pour les débutants.

Dans cet article, nous explorerons le GATT en profondeur. Vous apprendrez comment les appareils organisent les données en services et caractéristiques, comment les téléphones découvrent et lisent les valeurs, comment les notifications fournissent des mises à jour en temps réel, et comment le code embarqué et Android interagissent avec le GATT. À la fin, vous serez capable de concevoir une base de données GATT, de comprendre les journaux BLE et de créer des applications BLE en toute confiance.

## Prérequis

Avant de continuer, vous devriez avoir une compréhension de base de :

* Ce qu'est le Bluetooth à haut niveau (aucune connaissance approfondie du protocole n'est requise)
    
* Comment les applications mobiles se connectent à des appareils externes (Android, iOS ou embarqué)
    
* Les concepts de programmation très basiques (variables, fonctions, objets)
    

Vous aurez également besoin de :

* Un smartphone ou un ordinateur portable prenant en charge le Bluetooth Low Energy
    
* Une carte de développement ou un appareil compatible BLE (optionnel, mais utile pour essayer les exemples de code)
    
* Une application de débogage/scan BLE telle que nRF Connect, LightBlue ou BLE Scanner
    

Si vous êtes totalement novice en BLE, ne vous inquiétez pas : cet article détaille chaque concept étape par étape.

## Table des matières

* [Qu'est-ce que le GATT](#heading-qu-est-ce-que-le-gatt)?
    
* [Que sont les services et pourquoi sont-ils importants ?](#heading-que-sont-les-services-et-pourquoi-sont-ils-importants)
    
* [Que sont les caractéristiques et comment fonctionnent-elles](#heading-que-sont-les-caracteristiques-et-comment-fonctionnent-elles)?
    
* [Comment concevoir un profil GATT pour un moniteur de plante intelligent](#heading-comment-concevoir-un-profil-gatt-pour-un-moniteur-de-plante-intelligent)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que le GATT ?

GATT signifie Generic Attribute Profile. C'est le modèle de communication structuré utilisé par les appareils Bluetooth Low Energy pour échanger des données dans un format clair et organisé.

Le GATT définit comment les données sont stockées, formatées, consultées, mises à jour et transmises via des connexions BLE. Sans le GATT, les appareils Bluetooth n'échangeraient que des informations binaires non structurées sans signification cohérente. Avec le GATT, les appareils peuvent partager des valeurs telles que le pourcentage de batterie, la fréquence cardiaque, les relevés de température et les commandes d'état de manière bien définie.

### Rôles Client et Serveur GATT

Toute communication en BLE se produit entre deux rôles. Le Serveur GATT possède et expose les données. Le Client GATT demande, lit, écrit ou s'abonne à ces données. Le Serveur détient une base de données de valeurs avec lesquelles le Client interagit. Une montre connectée agit généralement comme un Serveur GATT car elle détient des valeurs de capteurs. Un smartphone agit généralement comme un Client GATT car il récupère ces informations.

Ces rôles peuvent changer selon la tâche. Par exemple, lors d'une mise à jour du firmware, le téléphone agit comme le Serveur GATT fournissant les blocs de firmware et l'appareil portable agit comme le Client GATT les demandant.

### Services, Caractéristiques et UUID

Le Serveur GATT stocke ses données dans une base de données structurée composée de Services et de Caractéristiques. Un Service est un conteneur qui regroupe des informations connexes. Une Caractéristique est une valeur de donnée unique à l'intérieur d'un service.

Par exemple, le Service de Batterie contient la caractéristique Niveau de Batterie. Le Service de Fréquence Cardiaque contient la caractéristique Mesure de la Fréquence Cardiaque.

Tous les services et caractéristiques sont identifiés à l'aide de valeurs UUID afin que chaque appareil sache comment les localiser. Les services standard définis par le Bluetooth SIG, tels que la Fréquence Cardiaque et la Batterie, utilisent des UUID 16 bits. Les fonctionnalités propriétaires personnalisées utilisent des UUID 128 bits.

### Exemple de structure de base de données GATT

Voici une décomposition conceptuelle d'une structure simple de base de données GATT :

```typescript
Service: Battery Service (UUID 0x180F)
    Characteristic: Battery Level (UUID 0x2A19)
    Example value: 92 percent
```

### Exemple : Lecture d'une caractéristique GATT depuis Android

Lorsqu'un téléphone se connecte à un appareil BLE et agit en tant que client, il effectue une séquence d'étapes. Il se connecte à l'appareil, découvre les services, trouve la caractéristique d'intérêt, et lit ou s'abonne à sa valeur.

L'exemple Java complet suivant montre une application Android agissant comme un **Client GATT**, découvrant les services et lisant le niveau de batterie.

```typescript
public class BleGattClientManager {

    private BluetoothGatt bluetoothGatt;

    private final BluetoothGattCallback gattCallback = new BluetoothGattCallback() {

        @Override
        public void onConnectionStateChange(BluetoothGatt gatt, int status, int newState) {
            if (newState == BluetoothProfile.STATE_CONNECTED) {
                Log.d(TAG, "Connected to device. Discovering services.");
                gatt.discoverServices();
            }
        }

        @Override
        public void onServicesDiscovered(BluetoothGatt gatt, int status) {
            UUID BATTERY_SERVICE_UUID =
                    UUID.fromString("0000180F-0000-1000-8000-00805F9B34FB");
            UUID BATTERY_LEVEL_UUID =
                    UUID.fromString("00002A19-0000-1000-8000-00805F9B34FB");

            BluetoothGattService service = gatt.getService(BATTERY_SERVICE_UUID);
            if (service != null) {
                BluetoothGattCharacteristic characteristic =
                        service.getCharacteristic(BATTERY_LEVEL_UUID);
                if (characteristic != null) {
                    gatt.readCharacteristic(characteristic);
                }
            }
        }

        @Override
        public void onCharacteristicRead(BluetoothGatt gatt,
                                         BluetoothGattCharacteristic characteristic,
                                         int status) {
            if (status == BluetoothGatt.GATT_SUCCESS) {
                int batteryValue = characteristic.getIntValue(
                        BluetoothGattCharacteristic.FORMAT_UINT8, 0);
                Log.d(TAG, "Battery Level: " + batteryValue + " percent");
            }
        }
    };

    public void connect(Context context, BluetoothDevice device) {
        bluetoothGatt = device.connectGatt(context, false, gattCallback);
    }
}
```

Cette classe Java représente un client GATT Bluetooth Low Energy qui se connecte à un appareil BLE et lit la caractéristique du niveau de batterie. La classe détient un objet `BluetoothGatt` qui représente la connexion BLE active. Le `BluetoothGattCallback` gère les événements pendant le cycle de vie de la connexion.

Lorsque l'état de connexion de l'appareil change et que le nouvel état indique que l'appareil est connecté, le rappel déclenche la découverte des services en appelant `gatt.discoverServices()`.

Une fois les services découverts, le rappel reçoit `onServicesDiscovered`, où deux UUID standards sont définis : le Service de Batterie avec l'UUID `0000180F-0000-1000-8000-00805F9B34FB` et la caractéristique Niveau de Batterie avec l'UUID `00002A19-0000-1000-8000-00805F9B34FB`. Le client récupère le Service de Batterie via `gatt.getService`, puis récupère la caractéristique Niveau de Batterie via `getCharacteristic`.

Si les deux objets sont trouvés, le client appelle `gatt.readCharacteristic`, ce qui envoie une requête de lecture au serveur. Lorsque le serveur répond, `onCharacteristicRead` est invoqué. Si la réponse est positive, la valeur de la caractéristique est extraite à l'aide de `getIntValue` sous forme d'entier non signé de 8 bits à l'offset zéro, produisant un pourcentage de zéro à cent. Cette valeur est affichée dans les journaux.

La méthode `connect` initie la connexion en appelant `device.connectGatt`, ce qui commence la communication et lie tous les rappels.

En résumé, le flux est simple : se connecter à l'appareil, découvrir les services, localiser le Service de Batterie, lire la caractéristique Niveau de Batterie et afficher le résultat. Ce code montre le modèle de base de l'interaction d'un client BLE avec un serveur GATT pour demander des informations.

### Android en tant que Serveur GATT

L'appareil Android peut également agir en tant que **Serveur GATT**. C'est utile lorsque le téléphone doit exposer ses propres caractéristiques que d'autres appareils BLE lisent ou écrivent, comme des informations de configuration, des commandes ou des données de paramétrage.

Voici un exemple complet d'un Serveur GATT personnalisé écrit en Java. Il expose un service personnalisé et une caractéristique personnalisée qui permet à un client BLE de lire et d'écrire des valeurs.

```typescript
public class BleGattServerManager {

    private BluetoothGattServer gattServer;

    private final UUID SERVICE_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abcdef0");

    private final UUID CHARACTERISTIC_UUID =
            UUID.fromString("abcdef01-1234-5678-1234-56789abcdef0");

    private final BluetoothGattServerCallback serverCallback =
            new BluetoothGattServerCallback() {

        @Override
        public void onConnectionStateChange(BluetoothDevice device,
                                            int status,
                                            int newState) {
            Log.d(TAG, "Device connected: " + device.getAddress());
        }

        @Override
        public void onCharacteristicReadRequest(BluetoothDevice device,
                                                int requestId,
                                                int offset,
                                                BluetoothGattCharacteristic characteristic) {

            byte[] value = "HELLO_ANDROID_SERVER".getBytes(StandardCharsets.UTF_8);
            gattServer.sendResponse(device, requestId,
                    BluetoothGatt.GATT_SUCCESS, offset, value);
        }

        @Override
        public void onCharacteristicWriteRequest(BluetoothDevice device,
                                                 int requestId,
                                                 BluetoothGattCharacteristic characteristic,
                                                 boolean preparedWrite,
                                                 boolean responseNeeded,
                                                 int offset,
                                                 byte[] value) {

            String received = new String(value, StandardCharsets.UTF_8);
            Log.d(TAG, "Client wrote value: " + received);

            gattServer.sendResponse(device, requestId,
                    BluetoothGatt.GATT_SUCCESS, offset, value);
        }
    };

    public void startServer(Context context) {
        BluetoothManager bluetoothManager =
                (BluetoothManager) context.getSystemService(Context.BLUETOOTH_SERVICE);

        gattServer = bluetoothManager.openGattServer(context, serverCallback);

        BluetoothGattService customService =
                new BluetoothGattService(SERVICE_UUID,
                        BluetoothGattService.SERVICE_TYPE_PRIMARY);

        BluetoothGattCharacteristic customCharacteristic =
                new BluetoothGattCharacteristic(
                        CHARACTERISTIC_UUID,
                        BluetoothGattCharacteristic.PROPERTY_READ |
                        BluetoothGattCharacteristic.PROPERTY_WRITE,
                        BluetoothGattCharacteristic.PERMISSION_READ |
                        BluetoothGattCharacteristic.PERMISSION_WRITE
                );

        customService.addCharacteristic(customCharacteristic);
        gattServer.addService(customService);
    }
}
```

Cette classe Java implémente un Serveur GATT Bluetooth Low Energy sur Android, ce qui signifie qu'elle expose un service et une caractéristique qu'un autre appareil BLE peut lire ou écrire.

La classe détient une instance de `BluetoothGattServer` qui est créée au démarrage du serveur. Deux UUID sont définis, un pour le service personnalisé et un pour la caractéristique personnalisée. Le `BluetoothGattServerCallback` gère les événements entrants de tout client BLE distant qui se connecte à ce serveur.

Lorsqu'un appareil se connecte, `onConnectionStateChange` enregistre la connexion. Lorsqu'un client envoie une requête de lecture sur la caractéristique, `onCharacteristicReadRequest` répond en renvoyant une valeur de chaîne statique, dans ce cas les octets du texte `HELLO_ANDROID_SERVER`, en utilisant `sendResponse` avec un statut de succès.

Lorsque le client écrit des données dans la caractéristique, `onCharacteristicWriteRequest` convertit le tableau d'octets entrant en chaîne de caractères, enregistre ce qui a été écrit et renvoie une réponse de succès pour confirmer que le serveur a accepté la nouvelle valeur.

La méthode `startServer` initialise le Serveur GATT en demandant le `BluetoothManager`, en ouvrant le serveur, en créant un service primaire personnalisé et en ajoutant une caractéristique à ce service avec des propriétés et des permissions de lecture et d'écriture. Le service est ensuite enregistré sur le serveur via `addService`, ce qui le rend disponible pour tout client BLE qui se connecte.

En résumé, ce code démontre comment un appareil Android peut se comporter comme un périphérique BLE et exposer une caractéristique personnalisée lisible et scriptable avec laquelle d'autres appareils peuvent interagir. Cela constitue la base de fonctionnalités telles que la configuration, le provisionnement, les commandes de contrôle à distance ou la communication d'appareil à appareil.

Cet exemple montre que le GATT est simplement une base de données structurée de valeurs lisibles et scriptables qui représentent un comportement applicatif significatif. Que la tâche soit le rapport du niveau de batterie, la surveillance de la santé en temps réel, le contrôle à distance d'appareils intelligents ou le provisionnement sécurisé, l'échange suit toujours ce même modèle.

Comprendre le GATT à ce niveau est le fondement de toute l'ingénierie et de la résolution de problèmes en Bluetooth Low Energy.

## Que sont les services et pourquoi sont-ils importants ?

### Les services comme conteneurs de capacités

Un Service dans le GATT est un conteneur logique qui regroupe des données connexes. Un seul appareil Bluetooth peut exposer de nombreux services, et chaque service se concentre sur une capacité ou une catégorie fonctionnelle.

Par exemple, une montre connectée peut exposer un Service de Fréquence Cardiaque, un Service de Batterie, un Service d'Heure Actuelle et un Service d'Information sur l'Appareil. Une ampoule intelligente peut exposer un Service de Contrôle d'Éclairage avec des caractéristiques pour changer la luminosité et la couleur. Un thermomètre médical peut exposer un Service de Thermomètre de Santé qui diffuse en continu des valeurs de température.

Les services existent pour séparer les différentes catégories d'informations afin que tout appareil client puisse immédiatement comprendre quelles fonctions sont disponibles et comment interagir avec elles.

Un service ne détient pas de valeurs brutes lui-même. Au lieu de cela, il organise des caractéristiques, qui contiennent les éléments de données réels. Le service définit uniquement le regroupement et le type de comportement associé à ce groupe. Cette conception rend la communication BLE extrêmement évolutive. Les applications n'ont qu'à savoir quel service cibler, puis elles peuvent découvrir et manipuler les caractéristiques qu'il contient.

### Services standards vs services personnalisés

Le Bluetooth SIG définit de nombreux services standards pour l'interopérabilité. Par exemple, le Service de Batterie expose le niveau de batterie dans une caractéristique appelée Niveau de Batterie. Le Service de Fréquence Cardiaque expose les valeurs de fréquence cardiaque afin que n'importe quelle application de fitness puisse s'y abonner. Ces services standards permettent à des appareils de différents fabricants de fonctionner ensemble sans intégration personnalisée.

Toute personne construisant un appareil personnalisé peut également définir son propre service original en utilisant un UUID 128 bits. La structure est la même, qu'il soit standard ou personnalisé.

### Exemple : Un appareil avec plusieurs services

Voici une représentation d'un exemple d'appareil qui expose deux services en même temps :

```java
Service: Battery Service (UUID 0x180F)
    Characteristic: Battery Level (UUID 0x2A19)
    Current value: 92 percent

Service: Heart Rate Service (UUID 0x180D)
    Characteristic: Heart Rate Measurement (UUID 0x2A37)
    Current value: 78 bpm
```

Un téléphone Android agissant comme client peut découvrir ces services puis interagir avec les caractéristiques qu'ils contiennent. La découverte est toujours la première étape après l'établissement d'une connexion BLE.

### Découverte des services dans Android

L'exemple suivant montre comment lister tous les services disponibles et les enregistrer dans les journaux en Java.

```java
@Override
public void onServicesDiscovered(BluetoothGatt gatt, int status) {
    for (BluetoothGattService service : gatt.getServices()) {
        Log.d(TAG, "Service discovered: " + service.getUuid().toString());
    }
}
```

Cette méthode est appelée automatiquement une fois que le client BLE a fini de découvrir tous les services exposés par le serveur GATT distant. Lorsqu'une connexion est établie, le client initie une procédure de découverte de services, et une fois que le serveur répond avec la liste complète des services disponibles, la pile Android déclenche `onServicesDiscovered`.

À l'intérieur de ce rappel, le code parcourt chaque `BluetoothGattService` renvoyé par `gatt.getServices()`, qui représente tous les services implémentés par l'appareil connecté. Pour chaque service de cette liste, le code affiche son UUID dans le journal. Cette sortie aide les développeurs à inspecter les services existants sur l'appareil, à confirmer que les services attendus tels que la Fréquence Cardiaque, la Batterie ou un service personnalisé sont présents, et à identifier les UUID corrects nécessaires pour lire ou écrire des caractéristiques plus tard.

Cette méthode est particulièrement utile pendant le développement ou le débogage, car elle vous permet de vérifier qu'un appareil expose correctement sa base de données GATT et que le client peut accéder à la liste des services avant de tenter d'interagir avec des caractéristiques.

### Notifications pour les données changeant continuellement

Une fois le service trouvé, l'étape suivante consiste à lire ou à s'abonner à ses caractéristiques. Certaines caractéristiques contiennent des valeurs statiques ou changeant rarement, ce qui rend les lectures directes appropriées. D'autres, comme la fréquence cardiaque ou la température, changent continuellement et devraient utiliser des notifications.

#### Pourquoi les notifications sont importantes dans les services

Les notifications permettent à un appareil de recevoir des mises à jour automatiquement chaque fois que la valeur change, au lieu de lire la caractéristique de manière répétée. Cela réduit la consommation d'énergie et la latence, ce qui est essentiel pour les appareils portables et les capteurs.

Voici un exemple Java montrant comment activer les notifications pour la caractéristique Mesure de la Fréquence Cardiaque :

```java
private void enableHeartRateNotifications(BluetoothGatt gatt) {

    UUID HEART_RATE_SERVICE_UUID =
            UUID.fromString("0000180D-0000-1000-8000-00805F9B34FB");
    UUID HEART_RATE_MEASUREMENT_UUID =
            UUID.fromString("00002A37-0000-1000-8000-00805F9B34FB");

    BluetoothGattService service = gatt.getService(HEART_RATE_SERVICE_UUID);
    if (service != null) {
        BluetoothGattCharacteristic characteristic =
                service.getCharacteristic(HEART_RATE_MEASUREMENT_UUID);

        if (characteristic != null) {
            gatt.setCharacteristicNotification(characteristic, true);

            BluetoothGattDescriptor descriptor =
                    characteristic.getDescriptor(
                            UUID.fromString("00002902-0000-1000-8000-00805F9B34FB")
                    );

            if (descriptor != null) {
                descriptor.setValue(BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE);
                gatt.writeDescriptor(descriptor);
            }
        }
    }
}
```

#### Activation des notifications dans Android

Cette méthode active les notifications pour la caractéristique Mesure de la Fréquence Cardiaque afin que l'appareil puisse envoyer de nouvelles valeurs automatiquement chaque fois que la fréquence cardiaque change.

Elle commence par définir les UUID pour le Service de Fréquence Cardiaque et la caractéristique Mesure de la Fréquence Cardiaque. En utilisant `gatt.getService`, elle récupère le Service de Fréquence Cardiaque de l'appareil connecté. Si ce service existe, elle localise la caractéristique Mesure de la Fréquence Cardiaque en son sein. Une fois la caractéristique trouvée, la méthode active la gestion locale des notifications du côté Android en utilisant `setCharacteristicNotification`, ce qui prépare le client à recevoir des mises à jour asynchrones.

Mais activer les notifications locales ne suffit pas. La spécification BLE exige d'écrire dans un descripteur spécial appelé Client Characteristic Configuration Descriptor (CCCD), identifié par l'UUID `00002902-0000-1000-8000-00805F9B34FB`, afin que l'appareil distant sache également que le client souhaite des mises à jour. La méthode récupère ce descripteur, définit sa valeur sur `ENABLE_NOTIFICATION_VALUE`, et l'écrit en utilisant `writeDescriptor`, ce qui envoie une requête par les ondes au serveur lui demandant de commencer à envoyer des notifications.

Une fois cette séquence terminée, les mises à jour commencent à arriver automatiquement dans le rappel `onCharacteristicChanged` chaque fois que la fréquence cardiaque change, sans avoir besoin de requêtes de lecture répétées.

C'est le modèle BLE préféré pour les données de capteurs continues telles que la fréquence cardiaque, la température, le nombre de pas ou les valeurs de mouvement, car il économise de l'énergie et offre une réactivité en temps réel.

Lorsque l'appareil commence à envoyer des notifications, les mises à jour sont reçues dans le rappel ci-dessous. Les valeurs arrivent dès qu'elles changent, ce qui rend ce système très efficace pour le streaming.

```java
@Override
public void onCharacteristicChanged(BluetoothGatt gatt,
                                    BluetoothGattCharacteristic characteristic) {

    UUID HEART_RATE_MEASUREMENT_UUID =
            UUID.fromString("00002A37-0000-1000-8000-00805F9B34FB");

    if (characteristic.getUuid().equals(HEART_RATE_MEASUREMENT_UUID)) {
        int flag = characteristic.getProperties();
        int format;
        if ((flag & 0x01) != 0) {
            format = BluetoothGattCharacteristic.FORMAT_UINT16;
        } else {
            format = BluetoothGattCharacteristic.FORMAT_UINT8;
        }
        int heartRate = characteristic.getIntValue(format, 1);
        Log.d(TAG, "Heart Rate: " + heartRate + " bpm");
    }
}
```

Cette méthode est appelée automatiquement chaque fois que l'appareil Bluetooth envoie une notification indiquant que la valeur d'une caractéristique a changé.

Dans cet exemple, la méthode gère les mises à jour de la caractéristique Mesure de la Fréquence Cardiaque. Le code vérifie d'abord si la caractéristique qui a déclenché le rappel correspond à l'UUID de Mesure de la Fréquence Cardiaque `00002A37-0000-1000-8000-00805F9B34FB`, garantissant que seules les mises à jour pertinentes sont traitées.

Les données de fréquence cardiaque peuvent être encodées sur un ou deux octets, selon les drapeaux (flags) définis dans les propriétés de la caractéristique. La méthode lit ces drapeaux et détermine le format correct à utiliser lors du décodage de la valeur de la fréquence cardiaque. Si le bit le moins significatif est activé, la fréquence cardiaque utilise un format 16 bits. Sinon, elle utilise un format unique de 8 bits.

Après avoir sélectionné le format approprié, la méthode extrait la valeur de la fréquence cardiaque à l'aide de `getIntValue`, en commençant à l'offset 1 car l'octet 0 contient les drapeaux.

Enfin, la valeur est affichée dans le journal en battements par minute. Cette méthode est généralement appelée de manière répétée, par exemple une fois par seconde, de sorte que le journal reçoit des mises à jour de la fréquence cardiaque en direct et en temps réel.

Cette approche démontre comment les notifications fournissent des données de capteurs continues sans interroger l'appareil de manière répétée, ce qui réduit la latence et la consommation d'énergie pour le client et le serveur.

Cet exemple montre comment le client récupère des données de capteurs en temps réel par abonnement plutôt que par interrogation (polling). Le même mécanisme est utilisé pour les capteurs de qualité de l'air, les notifications de luminosité de l'éclairage domestique intelligent, les moniteurs de température industriels, et plus encore.

Pour résumer cette section, un Service est un conteneur structuré qui organise des données connexes et est essentiel pour exposer des capacités et des fonctionnalités via BLE. Comprendre comment découvrir et interagir avec les services est la première étape majeure vers la création ou le débogage d'applications Bluetooth réelles.

## Que sont les caractéristiques et comment fonctionnent-elles ?

### Le rôle d'une caractéristique

Si un Service est un dossier, alors une Caractéristique est un fichier à l'intérieur de ce dossier qui contient réellement le contenu. Dans le GATT, la Caractéristique est l'endroit où vivent les données réelles. Presque tout ce qui intéresse votre application sera finalement lu, écrit ou faire l'objet d'un abonnement sur une caractéristique.

### Les quatre parties d'une caractéristique

Une caractéristique est plus qu'un simple nombre. Elle comporte quatre parties importantes. Premièrement, elle possède un UUID qui identifie ce qu'elle représente. Elle possède également une valeur qui stocke les octets réels. Ensuite, elle possède des propriétés qui décrivent les opérations autorisées, telles que la lecture (read), l'écriture (write) ou la notification (notify). Et enfin, elle possède des permissions qui contrôlent qui peut y accéder et sous quel niveau de sécurité. Comprendre ces éléments est la clé pour travailler sereinement avec le BLE.

L'UUID vous indique quel type de données se trouve à l'intérieur de la caractéristique. Par exemple, une caractéristique standard de Niveau de Batterie utilise l'UUID 0x2A19 et contient toujours un seul octet représentant un pourcentage de zéro à cent. Une caractéristique de Mesure de la Fréquence Cardiaque utilise l'UUID 0x2A37 et regroupe la fréquence cardiaque et des drapeaux dans un format structuré. Les caractéristiques personnalisées utilisent des UUID 128 bits que les développeurs définissent eux-mêmes.

La valeur est simplement une séquence d'octets. Sur le fil, le Bluetooth ne connaît pas les entiers, les flottants ou les chaînes de caractères. Il ne voit que des octets. Du côté Android, la classe `BluetoothGattCharacteristic` aide à interpréter ces octets comme différents types. Elle fournit des méthodes utilitaires telles que `getIntValue`, `getFloatValue` et `getStringValue` afin que vous puissiez décoder les données plus facilement.

Les propriétés d'une caractéristique décrivent le type d'opérations que le client peut effectuer. Les propriétés les plus courantes sont Read, Write, Notify et Indicate.

Read signifie qu'un client peut demander au serveur de renvoyer la valeur actuelle. Write signifie qu'un client peut envoyer une nouvelle valeur au serveur. Notify signifie que le serveur peut envoyer des mises à jour au client chaque fois que la valeur change. Indicate est similaire à Notify, mais avec une confirmation supplémentaire. Une caractéristique peut avoir une ou plusieurs propriétés combinées.

Les permissions sont liées mais légèrement différentes. Elles se concentrent sur le contrôle d'accès et la sécurité. Par exemple, une caractéristique peut nécessiter un cryptage ou un appairage authentifié avant de pouvoir être lue ou écrite. L'objet Android `BluetoothGattCharacteristic` contient ces drapeaux de permission afin que la pile les applique correctement.

### Exemple : Définition d'une caractéristique LED personnalisée

Prenons un exemple concret. Imaginez un appareil personnalisé qui expose une caractéristique pour contrôler l'état d'une LED. La LED doit être soit ON, soit OFF. La caractéristique doit prendre en charge à la fois la lecture et l'écriture, car le client peut vouloir lire l'état actuel et également le modifier.

Du côté du Serveur GATT Android, vous définiriez une telle caractéristique comme ceci :

```java
UUID SERVICE_UUID =
        UUID.fromString("12345678-1234-5678-1234-56789abcdef0");
UUID LED_CHAR_UUID =
        UUID.fromString("abcdef01-1234-5678-1234-56789abcdef0");

BluetoothGattService ledService =
        new BluetoothGattService(SERVICE_UUID,
                BluetoothGattService.SERVICE_TYPE_PRIMARY);

BluetoothGattCharacteristic ledCharacteristic =
        new BluetoothGattCharacteristic(
                LED_CHAR_UUID,
                BluetoothGattCharacteristic.PROPERTY_READ |
                BluetoothGattCharacteristic.PROPERTY_WRITE,
                BluetoothGattCharacteristic.PERMISSION_READ |
                BluetoothGattCharacteristic.PERMISSION_WRITE
        );

// Initial value
ledCharacteristic.setValue("OFF".getBytes(StandardCharsets.UTF_8));
ledService.addCharacteristic(ledCharacteristic);
gattServer.addService(ledService);
```

Ce code définit un Service GATT personnalisé et une Caractéristique GATT personnalisée sur un appareil Android agissant comme un Serveur GATT Bluetooth Low Energy.

Deux UUID sont créés à l'aide de `UUID.fromString`, l'un représentant le service personnalisé et l'autre représentant la caractéristique qui appartient à ce service. Une nouvelle instance de `BluetoothGattService` est ensuite créée, marquée comme service primaire pour indiquer qu'il s'agit d'un composant fonctionnel principal plutôt que d'un service d'aide secondaire.

À l'intérieur de ce service, un objet `BluetoothGattCharacteristic` est créé à l'aide du second UUID, et il est configuré pour autoriser à la fois les lectures et les écritures par un client BLE distant. Les drapeaux de propriété indiquent qu'un client peut demander la valeur actuelle et peut également envoyer des mises à jour, et les drapeaux de permission définissent que les deux opérations sont autorisées.

La caractéristique reçoit une valeur initiale de la chaîne `"OFF"` encodée en octets, qui pourrait représenter l'état actuel d'une LED contrôlée à distance, un mode d'appareil ou tout autre paramètre de configuration.

La caractéristique est ensuite ajoutée au service, et enfin le service entièrement défini est ajouté au serveur GATT à l'aide de `gattServer.addService`, le rendant visible pour tout client BLE qui se connecte.

À ce stade, un autre appareil peut lire la valeur `"OFF"` ou écrire une nouvelle valeur telle que `"ON"`, que le serveur pourrait ensuite utiliser pour déclencher un comportement réel, comme basculer un matériel physique.

### Gestion des lectures et écritures sur le serveur

#### Gestionnaires côté serveur

Du côté du Serveur GATT, vous devez également répondre aux requêtes de lecture et d'écriture. Cela se passe à l'intérieur de `BluetoothGattServerCallback`.

```java
private final BluetoothGattServerCallback serverCallback =
        new BluetoothGattServerCallback() {

    @Override
    public void onCharacteristicReadRequest(BluetoothDevice device,
                                            int requestId,
                                            int offset,
                                            BluetoothGattCharacteristic characteristic) {

        byte[] currentValue = characteristic.getValue();
        gattServer.sendResponse(device,
                requestId,
                BluetoothGatt.GATT_SUCCESS,
                offset,
                currentValue);
    }

    @Override
    public void onCharacteristicWriteRequest(BluetoothDevice device,
                                             int requestId,
                                             BluetoothGattCharacteristic characteristic,
                                             boolean preparedWrite,
                                             boolean responseNeeded,
                                             int offset,
                                             byte[] value) {

        String received = new String(value, StandardCharsets.UTF_8);
        Log.d(TAG, "LED characteristic write: " + received);

        characteristic.setValue(value);

        if ("ON".equalsIgnoreCase(received)) {
            turnLedOn();
        } else if ("OFF".equalsIgnoreCase(received)) {
            turnLedOff();
        } else {
            Log.e(TAG, "Unhandled case!");
            return;
        }

        if (responseNeeded) {
            gattServer.sendResponse(device,
                    requestId,
                    BluetoothGatt.GATT_SUCCESS,
                    offset,
                    value);
        }
    }
};
```

Ce rappel gère les requêtes de lecture et d'écriture provenant d'un client BLE distant interagissant avec la caractéristique LED personnalisée sur le Serveur GATT.

Lorsqu'un client effectue une opération de lecture, `onCharacteristicReadRequest` est déclenché. La méthode récupère la valeur actuelle stockée dans la caractéristique à l'aide de `getValue()` et la renvoie au client en appelant `sendResponse` avec un statut de succès. Cela signifie que la dernière valeur définie, telle que `"ON"` ou `"OFF"`, est renvoyée à l'appareil demandeur.

Lorsqu'un client effectue une opération d'écriture, `onCharacteristicWriteRequest` est appelé. La méthode convertit le tableau d'octets entrant en chaîne de caractères afin que le serveur puisse interpréter la commande. Elle enregistre le texte reçu, définit la nouvelle valeur dans la caractéristique à l'aide de `setValue`, puis vérifie si la chaîne est égale à `"ON"` ou `"OFF"`. Selon la valeur, elle appelle soit `turnLedOn()`, soit `turnLedOff()`, ce qui contrôlerait généralement un matériel réel ou déclencherait une action à l'intérieur de l'application.

Si le client a demandé une réponse, le serveur renvoie une confirmation en appelant `sendResponse` avec `GATT_SUCCESS`, reconnaissant que l'écriture s'est terminée avec succès. Ce rappel démontre comment fonctionne le contrôle BLE interactif : le serveur reçoit une commande, met à jour l'état interne, effectue une action réelle et rapporte l'état au client.

Ici, le serveur lit la valeur stockée dans la caractéristique lors d'une requête de lecture et la renvoie au client. Lorsque le client écrit une nouvelle valeur, le serveur décode les octets sous forme de chaîne et met à jour l'état interne, y compris le comportement physique comme le basculement de la LED.

### Lecture et écriture depuis le client

#### Gestionnaires côté client

Du côté client, une application Android typique doit lire et écrire dans cette même caractéristique. Le code pour le client ressemble à ce que nous avons vu dans les sections précédentes, mais il utilise maintenant les UUID personnalisés.

### Lecture d'une caractéristique personnalisée (Client)

Lecture de l'état de la LED depuis le client :

```java
public void readLedState(BluetoothGatt gatt) {
    UUID SERVICE_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abcdef0");
    UUID LED_CHAR_UUID =
            UUID.fromString("abcdef01-1234-5678-1234-56789abcdef0");

    BluetoothGattService service = gatt.getService(SERVICE_UUID);
    if (service != null) {
        BluetoothGattCharacteristic ledChar = service.getCharacteristic(LED_CHAR_UUID);
        if (ledChar != null) {
            gatt.readCharacteristic(ledChar);
        }
    }
}

@Override
public void onCharacteristicRead(BluetoothGatt gatt,
                                 BluetoothGattCharacteristic characteristic,
                                 int status) {
    if (status == BluetoothGatt.GATT_SUCCESS) {
        UUID LED_CHAR_UUID =
                UUID.fromString("abcdef01-1234-5678-1234-56789abcdef0");
        if (LED_CHAR_UUID.equals(characteristic.getUuid())) {
            String value = new String(characteristic.getValue(), StandardCharsets.UTF_8);
            Log.d(TAG, "LED state is: " + value);
        }
    }
}
```

Ce code montre comment un client Bluetooth Low Energy lit l'état actuel d'une caractéristique LED personnalisée à partir d'un serveur GATT. La méthode `readLedState` commence par définir les UUID pour le service personnalisé et la caractéristique LED afin que le client sache exactement où chercher dans la base de données GATT du serveur.

Elle récupère le service à l'aide de `gatt.getService`, et si le service existe, elle récupère la caractéristique LED à l'aide de `getCharacteristic`. Si cette caractéristique est trouvée, le client appelle `readCharacteristic`, ce qui envoie une requête de lecture à l'appareil distant via BLE. Une fois que le serveur répond, la méthode de rappel `onCharacteristicRead` est déclenchée.

Cette méthode vérifie d'abord que la lecture a réussi en confirmant que le statut est égal à `GATT_SUCCESS`. Elle vérifie ensuite que la caractéristique lue est bien la caractéristique LED en comparant les UUID. Si elle correspond, le code convertit le tableau d'octets de la caractéristique en une chaîne de caractères, qui contient soit `"ON"`, soit `"OFF"`, et enregistre l'état actuel.

Ce flux démontre comment un client BLE lit les valeurs stockées d'un appareil périphérique et répond lorsque le serveur renvoie les données, formant la base des interactions réelles telles que la vérification de l'état d'une lumière intelligente, d'un interrupteur ou de toute valeur de capteur exposée via une caractéristique personnalisée.

### Écriture dans une caractéristique personnalisée (Client)

Écriture d'un nouvel état de LED depuis le client :

```java
public void writeLedState(BluetoothGatt gatt, String newState) {
    UUID SERVICE_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abcdef0");
    UUID LED_CHAR_UUID =
            UUID.fromString("abcdef01-1234-5678-1234-56789abcdef0");

    BluetoothGattService service = gatt.getService(SERVICE_UUID);
    if (service != null) {
        BluetoothGattCharacteristic ledChar = service.getCharacteristic(LED_CHAR_UUID);
        if (ledChar != null) {
            ledChar.setValue(newState.getBytes(StandardCharsets.UTF_8));
            gatt.writeCharacteristic(ledChar);
        }
    }
}

@Override
public void onCharacteristicWrite(BluetoothGatt gatt,
                                  BluetoothGattCharacteristic characteristic,
                                  int status) {
    if (status == BluetoothGatt.GATT_SUCCESS) {
        Log.d(TAG, "LED state write completed");
    }
}
```

Ce code démontre comment un client Bluetooth Low Energy envoie une commande pour mettre à jour l'état de la LED sur un appareil serveur GATT.

La méthode `writeLedState` commence par définir les UUID pour le service personnalisé et la caractéristique LED, puis récupère le service du serveur GATT connecté. Si le service est trouvé, elle accède à la caractéristique LED à l'intérieur de celui-ci.

Une fois la caractéristique obtenue, le nouvel état de la LED, qui sera généralement la chaîne `"ON"` ou `"OFF"`, est converti en un tableau d'octets et placé dans la caractéristique avec `setValue`. La méthode appelle ensuite `writeCharacteristic`, qui envoie une requête d'écriture à l'appareil distant pour mettre à jour la valeur stockée.

Lorsque le serveur traite l'écriture et renvoie une réponse, la méthode de rappel `onCharacteristicWrite` s'exécute. Si le statut indique un succès, le code enregistre que l'écriture est terminée. À ce stade, le code du serveur de l'autre côté peut agir en fonction du nouvel état, comme allumer ou éteindre une LED réelle.

Ce flux illustre comment les clients modifient les valeurs sur un périphérique BLE et comment l'accusé de réception est géré une fois l'opération terminée, constituant un exemple typique de contrôle d'appareil via le GATT.

Cette combinaison de définitions de serveur et d'interactions client montre comment les caractéristiques sont les véritables bêtes de somme du GATT. Chaque donnée significative passe par elles. Les lectures, les écritures et les notifications opèrent toutes au niveau de la caractéristique.

### Notifications et CCCD

Les notifications sont simplement une propriété spéciale sur une caractéristique. Lorsqu'elles sont activées, le serveur peut pousser de nouvelles valeurs vers le client sans que celui-ci ne les demande à chaque fois. Pour prendre en charge les notifications, une caractéristique a besoin de la propriété Notify et généralement d'un descripteur appelé Client Characteristic Configuration Descriptor, souvent appelé CCCD, avec l'UUID 0x2902.

Du côté serveur, vous mettriez à jour la valeur et appelleriez `notifyCharacteristicChanged`. Du côté client, vous définissez la notification de caractéristique sur true et écrivez le descripteur avec `ENABLE_NOTIFICATION_VALUE`. Le modèle de code est presque identique quel que soit le type de données, ce qui le rend facile à réutiliser une fois que vous l'avez compris.

À ce stade, vous pouvez voir qu'une caractéristique n'est pas seulement un champ statique. C'est une unité complète de comportement. Elle définit quelles données existent, comment elles sont représentées, qui peut y accéder et comment elles se mettent à jour. Une fois que vous êtes à l'aise avec la conception de caractéristiques et leur manipulation en Java, vous êtes très proche de maîtriser le développement BLE pratique.

## Comment concevoir un profil GATT pour un moniteur de plante intelligent

Pour rendre le GATT concret, concevons un profil complet pour un appareil simple mais réaliste : un moniteur de plante intelligent.

Imaginez un petit capteur BLE que vous plantez dans un pot de fleurs. Il mesure l'humidité du sol, rapporte son propre niveau de batterie et vous permet de configurer la fréquence à laquelle il envoie des mises à jour. Une application mobile s'y connecte, lit le niveau d'humidité actuel, affiche le pourcentage de batterie et permet à l'utilisateur d'ajuster l'intervalle de rapport.

Nous allons concevoir les deux côtés en termes de GATT. Tout d'abord, nous déciderons des services et caractéristiques dont nous avons besoin. Ensuite, nous verrons comment un appareil Android peut agir en tant que client. À des fins pédagogiques, nous montrerons également comment Android pourrait agir en tant que serveur, bien que dans un produit réel, le moniteur de plante soit normalement un appareil embarqué.

### Conception du profil GATT

Nous avons besoin de trois éléments d'information logiques :

1. Pourcentage d'humidité du sol – il s'agit de données de capteur dynamiques.
    
2. Niveau de batterie – c'est standard, nous pouvons donc réutiliser le Service de Batterie.
    
3. Configuration de l'intervalle de rapport – c'est un paramètre que le client écrit et que l'appareil utilise.
    

Nous pouvons exprimer cela avec un service personnalisé plus le Service de Batterie standard.

**Plan du profil :**

```java
Custom Service: Plant Monitor Service
    UUID: 12345678-1234-5678-1234-56789abc0001

    Characteristic: Soil Moisture
        UUID: 12345678-1234-5678-1234-56789abc0002
        Properties: Read, Notify
        Permissions: Read
        Format: uint8 (0 to 100 percentage)

    Characteristic: Reporting Interval
        UUID: 12345678-1234-5678-1234-56789abc0003
        Properties: Read, Write
        Permissions: Read, Write
        Format: uint16 (seconds)

Standard Service: Battery Service
    UUID: 0000180F-0000-1000-8000-00805F9B34FB

    Characteristic: Battery Level
        UUID: 00002A19-0000-1000-8000-00805F9B34FB
        Properties: Read, Notify (optional)
        Permissions: Read
        Format: uint8 (0 to 100 percentage)
```

Maintenant, nous savons exactement ce qui existe à l'intérieur de l'appareil. Un client peut se connecter, rechercher le Service de Moniteur de Plante et le Service de Batterie, puis interagir avec ces trois caractéristiques.

### Implémentation du Serveur GATT

Dans un produit matériel réel, le moniteur de plante serait écrit en C ou C++ embarqué. Mais pour l'apprentissage, nous pouvons simuler le serveur sur Android lui-même. Cela vous aidera à comprendre comment fonctionne le côté serveur.

Tout d'abord, nous allons créer les services et les caractéristiques.

```java
public class PlantMonitorGattServer {

    private BluetoothGattServer gattServer;

    private final UUID PLANT_SERVICE_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abc0001");
    private final UUID MOISTURE_CHAR_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abc0002");
    private final UUID INTERVAL_CHAR_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abc0003");

    private final UUID BATTERY_SERVICE_UUID =
            UUID.fromString("0000180F-0000-1000-8000-00805F9B34FB");
    private final UUID BATTERY_LEVEL_UUID =
            UUID.fromString("00002A19-0000-1000-8000-00805F9B34FB");

    // Simulated state
    private int currentMoisture = 55;      // percentage
    private int reportingIntervalSec = 60; // seconds
    private int batteryLevel = 87;         // percentage

    private BluetoothGattCharacteristic moistureCharacteristic;
    private BluetoothGattCharacteristic intervalCharacteristic;
    private BluetoothGattCharacteristic batteryLevelCharacteristic;
```

Cette classe représente un Serveur GATT Bluetooth Low Energy qui simule un appareil de surveillance de plante intelligent. Elle détient une instance de `BluetoothGattServer` qui exposera des services et des caractéristiques à tout client BLE qui se connecte.

Plusieurs UUID sont définis pour identifier le Service de Moniteur de Plante personnalisé et ses caractéristiques, ainsi que le Service de Batterie standard et sa caractéristique de Niveau de Batterie.

Le Service de Moniteur de Plante personnalisé possède deux caractéristiques : une pour l'humidité du sol et une pour l'intervalle de rapport. Le Service de Batterie utilise les UUID standards définis par le Bluetooth SIG afin que n'importe quel client puisse le reconnaître et l'analyser.

La classe conserve également un état interne simulé : `currentMoisture` commence à 55 %, `reportingIntervalSec` est réglé sur 60 secondes et `batteryLevel` est réglé sur 87 %. Ces valeurs agissent comme des relevés de capteurs et des configurations stockées à l'intérieur de l'appareil.

Enfin, elle déclare trois champs `BluetoothGattCharacteristic` qui pointeront plus tard vers les caractéristiques réelles d'humidité, d'intervalle et de niveau de batterie une fois qu'elles seront créées et ajoutées à leurs services respectifs.

Ces champs permettent au serveur de mettre à jour facilement les valeurs et d'envoyer des notifications plus tard – par exemple, lorsque l'humidité change ou lorsque le niveau de batterie baisse.

Ensuite, nous allons configurer le serveur et définir les services et caractéristiques.

```java
    public void startServer(Context context) {
        BluetoothManager bluetoothManager =
                (BluetoothManager) context.getSystemService(Context.BLUETOOTH_SERVICE);

        gattServer = bluetoothManager.openGattServer(context, serverCallback);

        // Plant Monitor Service
        BluetoothGattService plantService =
                new BluetoothGattService(
                        PLANT_SERVICE_UUID,
                        BluetoothGattService.SERVICE_TYPE_PRIMARY
                );

        moistureCharacteristic = new BluetoothGattCharacteristic(
                MOISTURE_CHAR_UUID,
                BluetoothGattCharacteristic.PROPERTY_READ |
                BluetoothGattCharacteristic.PROPERTY_NOTIFY,
                BluetoothGattCharacteristic.PERMISSION_READ
        );

        intervalCharacteristic = new BluetoothGattCharacteristic(
                INTERVAL_CHAR_UUID,
                BluetoothGattCharacteristic.PROPERTY_READ |
                BluetoothGattCharacteristic.PROPERTY_WRITE,
                BluetoothGattCharacteristic.PERMISSION_READ |
                BluetoothGattCharacteristic.PERMISSION_WRITE
        );

        // Set initial values
        moistureCharacteristic.setValue(new byte[]{(byte) currentMoisture});
        intervalCharacteristic.setValue(intToTwoBytes(reportingIntervalSec));

        // For notifications, add CCCD descriptor
        BluetoothGattDescriptor moistureCccd = new BluetoothGattDescriptor(
                UUID.fromString("00002902-0000-1000-8000-00805F9B34FB"),
                BluetoothGattDescriptor.PERMISSION_READ |
                BluetoothGattDescriptor.PERMISSION_WRITE
        );
        moistureCharacteristic.addDescriptor(moistureCccd);

        plantService.addCharacteristic(moistureCharacteristic);
        plantService.addCharacteristic(intervalCharacteristic);

        // Battery Service
        BluetoothGattService batteryService =
                new BluetoothGattService(
                        BATTERY_SERVICE_UUID,
                        BluetoothGattService.SERVICE_TYPE_PRIMARY
                );

        batteryLevelCharacteristic = new BluetoothGattCharacteristic(
                BATTERY_LEVEL_UUID,
                BluetoothGattCharacteristic.PROPERTY_READ |
                BluetoothGattCharacteristic.PROPERTY_NOTIFY,
                BluetoothGattCharacteristic.PERMISSION_READ
        );

        batteryLevelCharacteristic.setValue(new byte[]{(byte) batteryLevel});

        BluetoothGattDescriptor batteryCccd = new BluetoothGattDescriptor(
                UUID.fromString("00002902-0000-1000-8000-00805F9B34FB"),
                BluetoothGattDescriptor.PERMISSION_READ |
                BluetoothGattDescriptor.PERMISSION_WRITE
        );
        batteryLevelCharacteristic.addDescriptor(batteryCccd);

        batteryService.addCharacteristic(batteryLevelCharacteristic);

        gattServer.addService(plantService);
        gattServer.addService(batteryService);
    }

    private byte[] intToTwoBytes(int value) {
        byte[] data = new byte[2];
        data[0] = (byte) (value & 0xFF);
        data[1] = (byte) ((value >> 8) & 0xFF);
        return data;
    }
```

Cette méthode démarre le serveur GATT Bluetooth Low Energy et construit la base de données GATT complète pour le moniteur de plante intelligent.

Elle obtient d'abord le `BluetoothManager` du système Android et l'utilise pour ouvrir un `BluetoothGattServer`, en passant un rappel qui gérera les événements de lecture, d'écriture et de notification des clients connectés.

Ensuite, elle crée le Service de Moniteur de Plante personnalisé en utilisant le `PLANT_SERVICE_UUID` et le marque comme service primaire.

À l'intérieur de ce service, elle définit deux caractéristiques. La caractéristique d'humidité est créée avec le `MOISTURE_CHAR_UUID` et reçoit les propriétés Read et Notify, ce qui signifie qu'un client peut lire l'humidité actuelle du sol et également s'abonner aux notifications lorsqu'elle change. Elle est en lecture seule, elle utilise donc une permission de lecture. La caractéristique d'intervalle de rapport est créée avec l'UUID `INTERVAL_CHAR_UUID` et utilise les propriétés Read et Write afin qu'un client puisse vérifier l'intervalle actuel et le mettre à jour. Elle utilise les permissions de lecture et d'écriture.

Le code définit les valeurs initiales de ces caractéristiques : la caractéristique d'humidité reçoit le pourcentage d'humidité actuel stocké sous forme d'un seul octet, et la caractéristique d'intervalle reçoit une représentation sur deux octets de l'intervalle de rapport à l'aide de la méthode utilitaire `intToTwoBytes`, qui divise un entier de 16 bits en octets de poids faible et de poids fort.

Pour autoriser les notifications d'humidité, elle ajoute un descripteur de configuration de caractéristique client (CCCD) avec un UUID standard `0x2902` et des permissions de lecture ou d'écriture, puis attache ce descripteur à la caractéristique d'humidité. Les deux caractéristiques sont ajoutées au service de plante.

Ensuite, la méthode crée le Service de Batterie standard comme un autre service primaire en utilisant l'UUID de batterie bien connu. Elle définit la caractéristique Niveau de Batterie avec les propriétés de lecture et de notification et la permission de lecture.

Le niveau de batterie initial est stocké sous forme d'un seul octet. Tout comme pour l'humidité, elle ajoute un descripteur CCCD pour prendre en charge les notifications et l'attache à la caractéristique de batterie. La caractéristique de batterie est ensuite ajoutée au service de batterie.

Enfin, la méthode enregistre à la fois le service de plante et le service de batterie auprès du serveur GATT à l'aide de `addService`, ce qui les rend visibles pour tout client BLE qui se connecte. En tant que petit utilitaire, la méthode `intToTwoBytes` à la fin convertit un entier de 16 bits en un tableau d'octets à deux éléments avec l'octet le moins significatif en premier, ce qui est une manière courante d'encoder des entiers dans les caractéristiques BLE.

Maintenant, nous allons implémenter le rappel pour gérer la logique de lecture, d'écriture et de notification.

```java
    private final BluetoothGattServerCallback serverCallback =
            new BluetoothGattServerCallback() {

        @Override
        public void onConnectionStateChange(BluetoothDevice device,
                                            int status,
                                            int newState) {
            Log.d(TAG, "Device connection state: " + newState);
        }

        @Override
        public void onCharacteristicReadRequest(BluetoothDevice device,
                                                int requestId,
                                                int offset,
                                                BluetoothGattCharacteristic characteristic) {

            if (characteristic.getUuid().equals(MOISTURE_CHAR_UUID)) {
                moistureCharacteristic.setValue(new byte[]{(byte) currentMoisture});
                gattServer.sendResponse(device, requestId,
                        BluetoothGatt.GATT_SUCCESS, offset,
                        moistureCharacteristic.getValue());
            } else if (characteristic.getUuid().equals(INTERVAL_CHAR_UUID)) {
                intervalCharacteristic.setValue(intToTwoBytes(reportingIntervalSec));
                gattServer.sendResponse(device, requestId,
                        BluetoothGatt.GATT_SUCCESS, offset,
                        intervalCharacteristic.getValue());
            } else if (characteristic.getUuid().equals(BATTERY_LEVEL_UUID)) {
                batteryLevelCharacteristic.setValue(new byte[]{(byte) batteryLevel});
                gattServer.sendResponse(device, requestId,
                        BluetoothGatt.GATT_SUCCESS, offset,
                        batteryLevelCharacteristic.getValue());
            } else {
                gattServer.sendResponse(device, requestId,
                        BluetoothGatt.GATT_FAILURE, offset, null);
            }
        }

        @Override
        public void onCharacteristicWriteRequest(BluetoothDevice device,
                                                 int requestId,
                                                 BluetoothGattCharacteristic characteristic,
                                                 boolean preparedWrite,
                                                 boolean responseNeeded,
                                                 int offset,
                                                 byte[] value) {

            if (characteristic.getUuid().equals(INTERVAL_CHAR_UUID)) {
                int newInterval = ((value[1] & 0xFF) << 8) | (value[0] & 0xFF);
                reportingIntervalSec = newInterval;
                Log.d(TAG, "New reporting interval: " + reportingIntervalSec + " sec");

                intervalCharacteristic.setValue(value);
            }

            if (responseNeeded) {
                gattServer.sendResponse(device, requestId,
                        BluetoothGatt.GATT_SUCCESS, offset, value);
            }
        }

        @Override
        public void onDescriptorWriteRequest(BluetoothDevice device,
                                             int requestId,
                                             BluetoothGattDescriptor descriptor,
                                             boolean preparedWrite,
                                             boolean responseNeeded,
                                             int offset,
                                             byte[] value) {

            if (descriptor.getCharacteristic().getUuid().equals(MOISTURE_CHAR_UUID)) {
                Log.d(TAG, "Moisture notifications enabled");
            } else if (descriptor.getCharacteristic().getUuid().equals(BATTERY_LEVEL_UUID)) {
                Log.d(TAG, "Battery notifications enabled");
            }

            if (responseNeeded) {
                gattServer.sendResponse(device, requestId,
                        BluetoothGatt.GATT_SUCCESS, offset, value);
            }
        }
    };
}
```

Ce rappel gère tous les événements importants côté serveur pour le Serveur GATT du moniteur de plante intelligent, y compris les changements de connexion, les lectures et écritures de caractéristiques, et les écritures de descripteurs pour les notifications.

Lorsqu'un appareil se connecte ou se déconnecte, `onConnectionStateChange` est appelé et enregistre simplement le nouvel état de connexion afin que vous puissiez voir quand un client apparaît ou disparaît. La logique principale réside dans `onCharacteristicReadRequest`, qui est invoquée chaque fois qu'un client BLE effectue une lecture sur l'une des caractéristiques du serveur.

La méthode vérifie quelle caractéristique est lue en comparant son UUID. S'il s'agit de la caractéristique d'humidité, elle rafraîchit la valeur de la caractéristique avec le pourcentage d'humidité actuel, puis répond avec `GATT_SUCCESS` et la valeur encodée. S'il s'agit de la caractéristique d'intervalle, elle encode l'intervalle de rapport actuel en deux octets à l'aide de `intToTwoBytes` et renvoie cela. S'il s'agit de la caractéristique de niveau de batterie, elle encode le pourcentage de batterie actuel en un seul octet et le renvoie. Si l'UUID ne correspond à aucune caractéristique connue, le serveur répond avec `GATT_FAILURE`, ce qui indique au client que la requête n'a pas pu être satisfaite.

La méthode `onCharacteristicWriteRequest` gère les écritures du client. Dans cette implémentation, seule la caractéristique d'intervalle de rapport est scriptable. Lorsqu'une écriture cible cette caractéristique, le code décode la valeur de deux octets envoyée par le client en un entier en la reconstruisant à partir des octets de poids faible et de poids fort. Il met à jour le champ interne `reportingIntervalSec`, enregistre le nouvel intervalle et stocke les octets reçus dans la caractéristique afin que les futures lectures renvoient la valeur mise à jour. Si le client a demandé une réponse, le serveur renvoie un statut de succès et fait écho à la valeur écrite.

Enfin, `onDescriptorWriteRequest` est appelé lorsqu'un client écrit dans un descripteur, généralement le Client Characteristic Configuration Descriptor qui contrôle les notifications. Le code vérifie si le descripteur appartient à la caractéristique d'humidité ou de batterie et enregistre que les notifications ont été activées pour la source de données correspondante. Si une réponse est nécessaire, il renvoie `GATT_SUCCESS`.

Ensemble, ce rappel transforme le serveur en un moniteur de plante en direct capable de répondre aux requêtes de lecture en temps réel, d'accepter les mises à jour de configuration et d'honorer les abonnements aux notifications pour l'humidité et le niveau de batterie.

Nous avons maintenant un Serveur GATT pleinement fonctionnel qui prend en charge les opérations de lecture et d'écriture, et peut également envoyer des notifications pour l'humidité et la batterie si nécessaire.

Pour simuler des notifications, le serveur peut périodiquement mettre à jour les valeurs et appeler `notifyCharacteristicChanged` :

```java
public void simulateSensorUpdate(BluetoothDevice device) {
    // Simulate moisture dropping slightly
    currentMoisture = Math.max(0, currentMoisture - 1);
    moistureCharacteristic.setValue(new byte[]{(byte) currentMoisture});
    gattServer.notifyCharacteristicChanged(device, moistureCharacteristic, false);
}
```

Cette méthode simule une mise à jour en direct du capteur d'humidité du sol et démontre comment un Serveur GATT envoie des notifications à un client BLE connecté.

Elle diminue la lecture d'humidité actuelle d'un pour cent, en s'assurant que la valeur ne tombe jamais en dessous de zéro à l'aide de `Math.max`. Après avoir ajusté la valeur simulée, la méthode stocke la valeur d'humidité mise à jour à l'intérieur de la caractéristique d'humidité à l'aide de `setValue`, ce qui prépare les nouvelles données à être transmises.

Elle appelle ensuite `notifyCharacteristicChanged`, qui envoie un paquet de notification BLE à l'appareil connecté spécifié, indiquant au client que la valeur de la caractéristique a changé et délivrant immédiatement la nouvelle lecture d'humidité.

Le paramètre final `false` indique qu'il s'agit d'une notification plutôt que d'une indication, ce qui signifie que le serveur ne nécessite pas d'accusé de réception de la part du client. Cette méthode serait généralement appelée par un minuteur ou déclenchée par un matériel de capteur réel, permettant à l'application cliente de recevoir des mises à jour continues en temps réel sans interroger le serveur de manière répétée.

### Implémentation du Client GATT en Java

Du côté du client Android, nous nous connectons au moniteur de plante, découvrons les services, puis interagissons avec les trois caractéristiques.

Tout d'abord, nous allons découvrir les services et stocker les références.

```java
public class PlantMonitorClient {

    private BluetoothGatt bluetoothGatt;

    private final UUID PLANT_SERVICE_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abc0001");
    private final UUID MOISTURE_CHAR_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abc0002");
    private final UUID INTERVAL_CHAR_UUID =
            UUID.fromString("12345678-1234-5678-1234-56789abc0003");

    private final UUID BATTERY_SERVICE_UUID =
            UUID.fromString("0000180F-0000-1000-8000-00805F9B34FB");
    private final UUID BATTERY_LEVEL_UUID =
            UUID.fromString("00002A19-0000-1000-8000-00805F9B34FB");

    public void connect(Context context, BluetoothDevice device) {
        bluetoothGatt = device.connectGatt(context, false, gattCallback);
    }

    private final BluetoothGattCallback gattCallback = new BluetoothGattCallback() {

        @Override
        public void onConnectionStateChange(BluetoothGatt gatt,
                                            int status,
                                            int newState) {
            if (newState == BluetoothProfile.STATE_CONNECTED) {
                Log.d(TAG, "Connected. Discovering services.");
                gatt.discoverServices();
            }
        }

        @Override
        public void onServicesDiscovered(BluetoothGatt gatt, int status) {
            Log.d(TAG, "Services discovered.");

            // Read current moisture and battery once
            readMoisture(gatt);
            readBatteryLevel(gatt);

            // Enable notifications
            enableMoistureNotifications(gatt);
        }
```

Cette classe représente le côté client Bluetooth Low Energy de l'exemple du moniteur de plante intelligent. Elle détient une référence `BluetoothGatt` qui représente la connexion active à l'appareil serveur BLE.

Plusieurs constantes UUID sont définies afin que le client sache comment trouver le Service de Moniteur de Plante et ses caractéristiques pour l'humidité et l'intervalle de rapport, ainsi que le Service de Batterie standard et sa caractéristique de Niveau de Batterie.

La méthode `connect` démarre la connexion BLE en appelant `device.connectGatt`, en passant le `Context` Android, un drapeau indiquant l'absence de reconnexion automatique, et une instance de `BluetoothGattCallback` qui recevra les événements de connexion et de données.

À l'intérieur du rappel, `onConnectionStateChange` est appelé chaque fois que l'état de la connexion change. Lorsque le nouvel état indique que l'appareil est connecté, le client enregistre cela et appelle `discoverServices` pour demander la liste complète des services GATT au serveur.

Une fois la procédure de découverte des services terminée, `onServicesDiscovered` est déclenché. Dans cette méthode, le client enregistre que les services ont été découverts, puis lit immédiatement les valeurs actuelles de l'humidité et du niveau de batterie à l'aide des méthodes utilitaires `readMoisture` et `readBatteryLevel`, et enfin active les notifications pour les mises à jour d'humidité à l'aide de `enableMoistureNotifications`.

Ensemble, ces étapes signifient que dès que le client se connecte à un appareil de surveillance de plante, il apprend quels services sont disponibles, récupère des instantanés uniques des valeurs importantes et s'abonne aux mises à jour en temps réel pour le capteur le plus important – qui est dans ce cas l'humidité du sol.

Maintenant, nous allons définir les méthodes pour lire l'humidité et la batterie.

```java
        private void readMoisture(BluetoothGatt gatt) {
            BluetoothGattService service = gatt.getService(PLANT_SERVICE_UUID);
            if (service != null) {
                BluetoothGattCharacteristic ch =
                        service.getCharacteristic(MOISTURE_CHAR_UUID);
                if (ch != null) {
                    gatt.readCharacteristic(ch);
                }
            }
        }

        private void readBatteryLevel(BluetoothGatt gatt) {
            BluetoothGattService service = gatt.getService(BATTERY_SERVICE_UUID);
            if (service != null) {
                BluetoothGattCharacteristic ch =
                        service.getCharacteristic(BATTERY_LEVEL_UUID);
                if (ch != null) {
                    gatt.readCharacteristic(ch);
                }
            }
        }

        @Override
        public void onCharacteristicRead(BluetoothGatt gatt,
                                         BluetoothGattCharacteristic characteristic,
                                         int status) {
            if (status == BluetoothGatt.GATT_SUCCESS) {
                if (MOISTURE_CHAR_UUID.equals(characteristic.getUuid())) {
                    int moisture = characteristic.getIntValue(
                            BluetoothGattCharacteristic.FORMAT_UINT8, 0);
                    Log.d(TAG, "Soil moisture: " + moisture + " percent");
                } else if (BATTERY_LEVEL_UUID.equals(characteristic.getUuid())) {
                    int battery = characteristic.getIntValue(
                            BluetoothGattCharacteristic.FORMAT_UINT8, 0);
                    Log.d(TAG, "Battery level: " + battery + " percent");
                } else if (INTERVAL_CHAR_UUID.equals(characteristic.getUuid())) {
                    int interval = characteristic.getIntValue(
                            BluetoothGattCharacteristic.FORMAT_UINT16, 0);
                    Log.d(TAG, "Reporting interval: " + interval + " sec");
                }
            }
        }
```

Ces méthodes gèrent la lecture des valeurs du Serveur GATT du moniteur de plante intelligent. La méthode `readMoisture` récupère le Service de Moniteur de Plante à l'aide de son UUID, puis recherche la caractéristique d'humidité du sol à l'intérieur. Si la caractéristique est trouvée, elle envoie une requête de lecture à l'aide de `gatt.readCharacteristic`, qui demande au serveur de renvoyer la valeur d'humidité actuelle.

La méthode `readBatteryLevel` se comporte de la même manière mais cible le Service de Batterie standard et la caractéristique Niveau de Batterie. Lorsque le serveur répond à l'une ou l'autre des requêtes de lecture, le rappel `onCharacteristicRead` est déclenché. La méthode vérifie d'abord si la lecture a réussi en confirmant que le statut est égal à `GATT_SUCCESS`. Elle détermine ensuite quelle caractéristique a été lue en comparant les UUID.

Si la réponse concerne la caractéristique d'humidité, elle décode la valeur d'un seul octet en un pourcentage entier et l'enregistre. S'il s'agit de la caractéristique de batterie, elle extrait de la même manière le pourcentage de batterie sur un seul octet et enregistre cette valeur. Si la caractéristique d'intervalle a été lue, elle décode deux octets en un entier de 16 bits et enregistre l'intervalle de rapport en secondes.

Ce flux de lecture fournit au client un instantané des valeurs actuelles du capteur et de la configuration immédiatement après la connexion, avant de surveiller les changements via les notifications.

Ensuite, nous allons activer les notifications pour l'humidité afin que l'application reçoive des mises à jour lorsqu'elle change.

```java
        private void enableMoistureNotifications(BluetoothGatt gatt) {
            BluetoothGattService service = gatt.getService(PLANT_SERVICE_UUID);
            if (service != null) {
                BluetoothGattCharacteristic ch =
                        service.getCharacteristic(MOISTURE_CHAR_UUID);
                if (ch != null) {
                    gatt.setCharacteristicNotification(ch, true);

                    BluetoothGattDescriptor descriptor =
                            ch.getDescriptor(UUID.fromString(
                                    "00002902-0000-1000-8000-00805F9B34FB"));

                    if (descriptor != null) {
                        descriptor.setValue(
                                BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE);
                        gatt.writeDescriptor(descriptor);
                    }
                }
            }
        }

        @Override
        public void onCharacteristicChanged(BluetoothGatt gatt,
                                            BluetoothGattCharacteristic characteristic) {
            if (MOISTURE_CHAR_UUID.equals(characteristic.getUuid())) {
                int moisture = characteristic.getIntValue(
                        BluetoothGattCharacteristic.FORMAT_UINT8, 0);
                Log.d(TAG,
                        "Soil moisture update: " + moisture + " percent");
            }
        }
    };
```

Ce code active les mises à jour d'humidité en direct via des notifications et les gère lorsqu'elles arrivent.

La méthode `enableMoistureNotifications` récupère d'abord le Service de Moniteur de Plante, puis obtient la caractéristique d'humidité à l'aide de son UUID. Si la caractéristique est disponible, elle appelle `setCharacteristicNotification` avec `true`, ce qui indique à la pile BLE Android de commencer à écouter les notifications sur cette caractéristique.

Mais activer localement la prise en charge des notifications ne suffit pas car la spécification GATT exige que le client écrive également dans le descripteur associé connu sous le nom de Client Characteristic Configuration Descriptor, ou CCCD, identifié par l'UUID standard `0x2902`. La méthode récupère ce descripteur, définit sa valeur sur `ENABLE_NOTIFICATION_VALUE`, et l'écrit à l'aide de `writeDescriptor`, ce qui envoie une requête par les ondes au serveur pour activer les notifications du côté de l'appareil. Une fois cette configuration terminée, les mises à jour sont délivrées chaque fois que la valeur de la caractéristique change.

Le rappel `onCharacteristicChanged` est déclenché automatiquement chaque fois que le serveur pousse une nouvelle lecture d'humidité. La méthode vérifie que la caractéristique modifiée est bien la caractéristique d'humidité en comparant les UUID, extrait le pourcentage d'humidité du sol d'un seul octet à l'aide de `getIntValue`, et enregistre la valeur mise à jour. Cela permet à l'application cliente de recevoir des relevés de capteurs en temps réel sans interroger constamment le serveur, ce qui économise de l'énergie et améliore la réactivité pour des applications telles que les tableaux de bord de surveillance de plantes ou les alertes de notification.

Enfin, le client peut écrire un nouvel intervalle de rapport, par exemple en passant de 60 secondes à 30 secondes.

```java
    public void writeReportingInterval(int newIntervalSec) {
        if (bluetoothGatt == null) return;

        BluetoothGattService service =
                bluetoothGatt.getService(PLANT_SERVICE_UUID);
        if (service != null) {
            BluetoothGattCharacteristic ch =
                    service.getCharacteristic(INTERVAL_CHAR_UUID);
            if (ch != null) {
                byte[] data = new byte[2];
                data[0] = (byte) (newIntervalSec & 0xFF);
                data[1] = (byte) ((newIntervalSec >> 8) & 0xFF);
                ch.setValue(data);
                bluetoothGatt.writeCharacteristic(ch);
            }
        }
    }
}
```

Cette méthode permet au client BLE de mettre à jour le paramètre d'intervalle de rapport sur le moniteur de plante intelligent en écrivant une nouvelle valeur dans la caractéristique d'intervalle sur le Serveur GATT.

Elle vérifie d'abord si l'objet `bluetoothGatt` est valide, car aucune écriture ne peut se produire avant qu'une connexion ne soit établie. Elle récupère le Service de Moniteur de Plante à l'aide de son UUID, puis recherche la caractéristique d'intervalle de rapport à l'intérieur de ce service.

Si la caractéristique existe, la méthode convertit la nouvelle valeur d'intervalle d'un entier en un tableau de deux octets, en plaçant l'octet le moins significatif en premier et l'octet le plus significatif en second, ce qui est le format little-endian courant utilisé dans les caractéristiques Bluetooth. Elle définit ce tableau d'octets comme la nouvelle valeur de la caractéristique, puis appelle `writeCharacteristic`, qui envoie une requête d'écriture par les ondes au serveur. Lorsque le serveur traite la commande dans son gestionnaire de requête d'écriture correspondant, il mettra à jour sa valeur d'intervalle interne et accusera réception du changement.

Cette méthode démontre comment les paramètres de configuration sont écrits d'un client BLE vers un appareil BLE, permettant un contrôle interactif du comportement au lieu de se contenter de lire les valeurs des capteurs.

Avec cette conception, notre système de moniteur de plante intelligent est complet. Le Serveur GATT expose des services et des caractéristiques bien définis. Le client Android se connecte, découvre, lit, écrit et s'abonne aux notifications. Le concept est toujours le même : les services regroupent les fonctionnalités. Les caractéristiques détiennent les données et le comportement. Les clients manipulent les caractéristiques. Les serveurs les stockent et les protègent.

Une fois que vous pouvez concevoir et coder un tel profil de bout en bout, vous utilisez effectivement le GATT comme le font les produits réels. Le même modèle s'applique à des appareils complexes tels que les moniteurs de glucose, les serrures intelligentes, les lunettes connectées et les capteurs industriels.

## Conclusion

Le GATT est le fondement qui rend la communication Bluetooth Low Energy compréhensible et fiable. Il transforme les signaux radio bruts en informations structurées significatives grâce à l'utilisation de services et de caractéristiques. Une fois que vous avez compris que chaque appareil BLE expose une base de données de valeurs qu'un client peut lire, écrire ou s'abonner, tout le système devient logique au lieu d'être mystérieux.

Que vous lisiez la fréquence cardiaque d'une montre connectée, vérifiiez le niveau de batterie d'écouteurs sans fil, contrôliez une ampoule intelligente ou configuriez un capteur industriel, l'interaction se produit toujours via des caractéristiques GATT à l'intérieur de services.

En examinant les deux côtés de la communication, le Serveur GATT et le Client GATT, et en parcourant des exemples de code Java réels pour la lecture, l'écriture et la réception de notifications, vous disposez désormais des connaissances pratiques nécessaires pour construire et déboguer des applications BLE réelles. Vous avez vu comment définir des services et des caractéristiques personnalisés, comment interpréter les formats de données, comment activer les notifications pour les mises à jour dynamiques des capteurs et comment organiser un profil d'appareil complet à l'aide d'un exemple réaliste dans le projet de moniteur de plante.

Tout dans le développement Bluetooth Low Energy commence par la compréhension du GATT à ce niveau. Une fois que vous êtes à l'aise avec la conception et l'interaction avec les services et les caractéristiques, vous pouvez passer en toute confiance à des sujets plus avancés tels que l'appairage et la liaison sécurisés, l'optimisation du débit à l'aide du MTU et de l'intervalle de connexion, l'optimisation de la puissance, les mises à jour du firmware OTA, et des outils comme nRF Connect et l'analyse des journaux HCI.

La meilleure façon de renforcer ce que vous avez appris est de construire quelque chose de concret. Même un simple projet de test de lecture et d'écriture aidera ces concepts à devenir intuitifs.

Maîtriser le GATT est la première étape majeure vers le développement Bluetooth professionnel. Chaque système complexe construit avec le BLE, des wearables grand public aux dispositifs médicaux et à la domotique intelligente, repose sur cette technologie. Maintenant que vous comprenez la structure et le modèle de communication, vous êtes prêt à explorer des capacités plus sophistiquées et à créer vos propres applications en toute confiance.