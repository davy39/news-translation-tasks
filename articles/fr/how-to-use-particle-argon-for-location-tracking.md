---
title: Comment utiliser Particle Argon pour le suivi de localisation
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-09T13:20:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-particle-argon-for-location-tracking
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/Copy-of-Copy-of-Flow.png
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: hardware
  slug: hardware
- name: particle
  slug: particle
seo_title: Comment utiliser Particle Argon pour le suivi de localisation
seo_desc: 'By Jared Wolff

  Ever want to add presence or location tracking to a project? Frustrated by the solutions
  (or lack thereof)?

  Do not worry, you''re not the only one!

  In this post you''ll learn how to implement a very basic tracking and notification
  applic...'
---

Par Jared Wolff

Vous avez déjà voulu ajouter une détection de présence ou un suivi de localisation à un projet ? Frustré par les solutions (ou leur absence) ?

Ne vous inquiétez pas, vous n'êtes pas le seul !

Dans cet article, vous apprendrez à implémenter une application très basique de suivi et de notification. Nous utiliserons un Particle Argon et un Tile Mate.

À la fin, vous serez en mesure de savoir si le Tile est présent ou non. De plus, nous utiliserons Pushover pour envoyer des notifications push aux appareils de votre choix.

C'est parti !

**Note** avant de commencer, cet article est **long**. [Vous pouvez télécharger la version PDF pour la sauvegarder et la consulter plus tard.](https://www.jaredwolff.com/files/how-to-location-tracking-using-particle-mesh-pdf/)

## Investigation initiale

L'idée d'utiliser un Tile n'était pas évidente au premier abord. Idéalement, utiliser un téléphone semblait plus logique. Malheureusement, ce n'était pas une option viable. Cela nécessiterait des recherches supplémentaires et la création d'une application Bluetooth iOS.

Ainsi, l'idée d'utiliser un téléphone a été abandonnée.

Puis je me suis dit : "Quels appareils _émettent_ tout le temps ?"

C'est ce qui m'a conduit à envisager un tracker comme Tile.

Après sa réception, j'ai effectué quelques tests habituels. Première étape, l'application Tile.

![Capture d'écran de l'application Tile](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/iphone7gold_portrait-2-2b6bcb7b-0f91-4578-a2db-034853565b09.png)

J'ai pu connecter et utiliser l'appareil. Je l'ai même fait jouer une mélodie accrocheuse. 🎵

Ensuite, je suis passé à l'utilisation d'une des applications de scan Bluetooth. J'ai parcouru tous les résultats et Bingo. Le Tile était là !

![Résultats du scan NRFConnect](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/iphone7gold_portrait-466803ef-57d9-498c-8656-2c274bf7fe8d.png)

J'ai même attendu quelques heures et vérifié à nouveau. Je voulais m'assurer qu'il ne se mettait pas en veille après un certain temps. Il s'avère qu'il émet toujours. Autant que je puisse dire, environ toutes les 8 secondes.

Tous ces tests ont conduit à une conclusion : il pourrait être facilement utilisé pour la détection de présence.

L'étape suivante du processus consistait à essayer de le faire fonctionner avec un Argon.

## Publicité

Comme nous l'avons découvert à l'étape précédente, nous savons que le Tile émet environ toutes les 8 secondes. Cela signifie qu'il devrait être facilement scannable à l'aide de n'importe quel appareil, y compris un Argon, Zenon ou Boron.

Pour cet exemple, je vous suggère d'utiliser un Argon. Cela est dû au fait que Bluetooth et Mesh partagent la même radio. Lors du scan du Tile, le Xenon connecté à Mesh manquait souvent les paquets de publicité. Cela conduisait à des faux négatifs (et à de la frustration !).

Dans la même veine, vous voudrez vous assurer que **votre Argon n'est connecté à aucun réseau mesh.** Vous pouvez le retirer en utilisant le CLI. Connectez votre appareil à votre ordinateur et exécutez la commande suivante :

```bash
particle mesh remove <nom/ID de l'appareil>

```

Assurez-vous de remplacer **<nom/ID de l'appareil>** par le nom ou l'ID de votre appareil.

Très bien, revenons aux choses sérieuses.

La publicité peut avoir plusieurs objectifs en Bluetooth. Typiquement, elle marque le début de la phase d'appariement. Ainsi, les autres appareils savent que l'appareil émetteur est disponible.

De plus, l'appareil émetteur indiquera les services qu'il propose. Nous pouvons utiliser cette connaissance pour filtrer les appareils qui ne correspondent pas.

Par exemple, voici une capture d'écran des services disponibles sur l'appareil Tile :

![Informations sur les services utilisant Light Blue](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Apple_iPhone_6s_Gold-c1f1d0da-7aba-410a-97b4-3cbebc933208.png)

Lors du scan, nous vérifierons que l'appareil auquel nous nous connectons a l'UUID de service `0xfeed`.

Avant de plonger profondément dans le monde Bluetooth, configurons notre application pour le débogage en utilisant le Logger.

## Journalisation

Dans ce tutoriel, nous utiliserons le Logger. Il vous permet d'afficher des messages de journalisation à partir de votre application en utilisant `particle serial monitor`.

L'une des fonctionnalités intéressantes du logger est l'idée de hiérarchie des messages. Cela vous permet, en tant que concepteur, de désactiver sélectivement les messages qui peuvent ne pas être nécessaires.

Par exemple, si vous avez des messages utilisés pour le débogage. Vous pourriez les supprimer ou les commenter. Ou, vous pourriez augmenter le `LOG_LEVEL` afin qu'ils soient effectivement ignorés.

Voici les niveaux de journalisation disponibles dans `logging.h` dans le dépôt device-os de Particle :

```c++
// Niveau de journalisation. Assurez-vous que log_level_name() est mis à jour pour les nouveaux niveaux ajoutés
typedef enum LogLevel {
    LOG_LEVEL_ALL = 1, // Journaliser tous les messages
    LOG_LEVEL_TRACE = 1,
    LOG_LEVEL_INFO = 30,
    LOG_LEVEL_WARN = 40,
    LOG_LEVEL_ERROR = 50,
    LOG_LEVEL_PANIC = 60,
    LOG_LEVEL_NONE = 70, // Ne pas journaliser de messages
    // Niveaux de compatibilité
    DEFAULT_LEVEL = 0,
    ALL_LEVEL = LOG_LEVEL_ALL,
    TRACE_LEVEL = LOG_LEVEL_TRACE,
    LOG_LEVEL = LOG_LEVEL_TRACE, // Déprécié
    DEBUG_LEVEL = LOG_LEVEL_TRACE, // Déprécié
    INFO_LEVEL = LOG_LEVEL_INFO,
    WARN_LEVEL = LOG_LEVEL_WARN,
    ERROR_LEVEL = LOG_LEVEL_ERROR,
    PANIC_LEVEL = LOG_LEVEL_PANIC,
    NO_LOG_LEVEL = LOG_LEVEL_NONE
} LogLevel;

```

Super, les niveaux de journalisation. Mais comment les utiliser ?

Nous pouvons les utiliser en invoquant une de ces fonctions :

`Log.trace`, `Log.info`, `Log.warn`, `Log.error`.

Par exemple :

```c++
Log.trace("Ceci est un message TRACE.");

```

Si nous définissons le niveau de journalisation à `LOG_LEVEL_INFO`, nous ne verrons que les messages de `Log.info`, `Log.warn` et `Log.error`. `LOG_LEVEL_WARN` ? Seuls `Log.warn` et `Log.error` s'afficheront. (Espérons que vous comprenez l'idée.)

Pour le configurer, nous définirons le niveau par défaut à `LOG_LEVEL_ERROR`. Nous définirons également le `LOG_LEVEL` spécifique à l'application à `LOG_LEVEL_TRACE`. Le résultat final devrait ressembler à ceci :

```c++
// Pour la journalisation
SerialLogHandler logHandler(115200, LOG_LEVEL_ERROR, {
    { "app", LOG_LEVEL_TRACE }, // activer tous les messages de l'application
});

```

Ainsi, nous ne sommes pas spammés avec les messages de journalisation de DeviceOS. De plus, nous obtenons tous les messages applicables de l'application elle-même.

Au fait, si vous souhaitez définir votre appareil à un seul `LOG_LEVEL`, vous pouvez le configurer comme ceci :

```c++
SerialLogHandler logHandler(LOG_LEVEL_INFO);

```

Alors que vous continuez votre voyage en utilisant Particle's DeviceOS, vous réaliserez bientôt à quel point cela peut être pratique. Maintenant, passons aux choses sérieuses !

## Configuration

![Page de sortie de Device-os](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-06_at_9-a04e6802-ec22-4036-8ace-6150a532979b.50.41_PM.png)

Tout d'abord, nous voulons nous assurer que nous utilisons la bonne version de DeviceOS. Toute version après 1.3 aura Bluetooth. Vous pouvez obtenir [les instructions ici](https://www.jaredwolff.com/how-to-upgrade-particle-mesh-device-os/).

Ensuite, nous voulons commencer à scanner le Tile. Nous voulons faire cela dans la fonction `loop()` à un intervalle spécifié. Nous utiliserons un minuteur `millis()` dans ce cas :

```c++
// Scanner les appareils
if( (millis() > lastSeen + TILE_RE_CHECK_MS) ){
    BLE.scan(scanResultCallback, NULL);
}

```

Assurez-vous de définir `lastSeen` en haut du fichier comme suit :

```c++
system_tick_t lastSeen = 0;

```

Nous l'utiliserons pour suivre la dernière fois que le Tile a été "vu". c'est-à-dire la dernière fois que l'Argon a vu un paquet de publicité du Tile.

`TILE_RE_CHECK_MS` peut être défini comme

```c++
#define TILE_RE_CHECK_MS 7500

```

Ainsi, nous vérifions, au minimum, toutes les 7,5 secondes les paquets de publicité.

Pour trouver l'appareil Tile, nous utiliserons `BLE.scan`. Lorsque nous l'appelons, il démarrera le processus de scan. Au fur et à mesure que les appareils sont trouvés, `scanResultCallback` sera déclenché.

Pour l'instant, nous pouvons définir `scanResultCallback` en haut du fichier :

```c++
void scanResultCallback(const BleScanResult *scanResult, void *context) {
}

```

Vous remarquez qu'il inclut un `BleScanResult`. Cela contiendra l'adresse, le RSSI et le nom de l'appareil (si disponible) et les informations de service disponibles. Cela sera utile plus tard lorsque nous chercherons notre appareil Tile !

Rappelez-vous que `BLE.scan` ne retourne pas tant que le scan n'est pas terminé. Le délai d'attente par défaut pour le scan est de 5 secondes. Vous pouvez changer cette valeur en utilisant `BLE.setScanTimeout()`. `setScanTimeout` prend des unités en incréments de 10 ms. Ainsi, pour un délai d'attente de 500 ms, il faudrait une valeur de 50.

Pour le cas de cette application, je recommande d'utiliser une valeur de 8 s (8000 ms). Vous pouvez la définir comme ceci :

```c++
BLE.setScanTimeout(800);

```

Dans ce cas, l'appareil scannera aussi longtemps qu'il faudra au Tile pour émettre. Ainsi, il est moins susceptible de manquer un paquet de publicité.

## Gestion des résultats de scan

![Toutes les définitions de constantes](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-06_at_11-fa1f684f-246c-474a-8397-e7387692e39b.05.19_PM.png)

Maintenant que nous avons `scanResultCallback`, définissons ce qui se passe à l'intérieur.

Nous voulons d'abord obtenir les informations de service dans les données de publicité. La meilleure façon est d'utiliser `scanResult->advertisingData.serviceUUID`. Nous passerons un tableau d'UUIDs qui sera copié pour notre utilisation.

```c++
BleUuid uuids[4];
int uuidsAvail = scanResult->advertisingData.serviceUUID(uuids,sizeof(uuids)/sizeof(BleUuid));

```

Cela remplira `uuids` afin que vous puissiez itérer sur eux. `uuidsAvail` sera égal au nombre d'UUIDs disponibles.

Dans notre cas, nous recherchons un UUID particulier. Nous le définirons en haut du fichier :

```c++
#define TILE_UUID 0xfeed

```

Normalement, les UUIDs sont **beaucoup** plus longs. Un UUID court comme celui-ci signifie qu'il a été réservé ou fait partie de la spécification Bluetooth. Dans les deux cas, nous le vérifierons de la même manière que nous vérifierions une version 32 bits ou 128 bits.

Pour des raisons de diagnostic, nous pouvons également imprimer les informations de l'appareil. Dans ce cas, le RSSI et l'adresse MAC de l'appareil sont pratiques :

```c++
// Imprimer les informations mac
BleAddress addr = scanResult->address;
Log.trace("MAC: %02X:%02X:%02X:%02X:%02X:%02X", addr[0], addr[1], addr[2], addr[3], addr[4], addr[5]);
Log.trace("RSSI: %dBm", scanResult->rssi);

```

Enfin, mettons en place une boucle pour voir si l'appareil trouvé a l'UUID :

```c++
// Boucle sur tous les UUIDs disponibles
// Pour les appareils Tile, il ne devrait y en avoir qu'un seul
for(int i = 0; i < uuidsAvail; i++){

    // Imprimer l'UUID que nous recherchons
    if( uuids[i].shorted() == TILE_UUID ) {
        Log.trace("UUID: %x", uuids[i].shorted());

        // Arrêter le scan
        BLE.stopScanning();

        return;
    }
}

```

Nous pouvons facilement comparer la version "shorted" de l'UUID avec `TILE_UUID`. C'est un simple entier donc aucune opération de comparaison mémoire compliquée n'est nécessaire. Ainsi, utiliser `if( uuids[i].shorted() == TILE_UUID )` fonctionne très bien.

Vous pouvez également utiliser `Log.trace` pour imprimer des informations de diagnostic. Dans ce cas, nous l'utilisons pour imprimer la version `shorted()` de l'UUID.

### Testez-le !

Testons ce que nous avons jusqu'à présent !

Programmez l'application sur votre Argon. Ouvrez le terminal et exécutez `particle serial monitor` pour voir les messages de débogage. Voici un exemple de ce que vous pourriez voir :

```
0000005825 [app] TRACE: MAC: 65:C7:B3:AF:73:5C
0000005827 [app] TRACE: RSSI: -37Bm
0000005954 [app] TRACE: MAC: B3:D9:F1:F0:5D:7E
0000005955 [app] TRACE: RSSI: -62Bm
0000006069 [app] TRACE: MAC: C5:F0:74:3D:13:77
0000006071 [app] TRACE: RSSI: -62Bm
0000006217 [app] TRACE: MAC: 65:C7:B3:AF:73:5C
0000006219 [app] TRACE: RSSI: -39Bm
0000006224 [app] TRACE: MAC: B3:D9:F1:F0:5D:7E
0000006225 [app] TRACE: RSSI: -62Bm
0000006296 [app] TRACE: MAC: D7:E7:FE:0C:A5:C0
0000006298 [app] TRACE: RSSI: -60Bm
0000006299 [app] TRACE: UUID: feed

```

Remarquez comment le message inclut `TRACE` et aussi `[app]` ? Cela signifie qu'il s'agit d'un message de trace provenant du code de l'application. Pratique, non ?

Ce code devient rapidement spammy, surtout si vous êtes dans un environnement avec beaucoup d'appareils Bluetooth émetteurs. Si votre Tile est allumé et en fonctionnement, vous verrez éventuellement un message `UUID: feed`. Cela signifie que votre Argon a trouvé le Tile !

Ensuite, nous utiliserons le bouton Mode intégré pour "programmer" l'adresse du Tile dans la mémoire. Ainsi, nous pourrons filtrer tous les appareils qui ne nous intéressent pas.

## Ajouter un appareil en appuyant sur le bouton

![Gestionnaire d'événements système](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-06_at_11-c1b2b96d-3a1b-45b5-bf5f-5fa7824c80d0.06.04_PM.png)

Tout d'abord, nous devons comprendre comment surveiller le bouton Mode. Selon la documentation, la meilleure solution est d'utiliser `System.on`.

```c++
System.on(button_click, eventHandler);

```

Le premier argument est le nom de l'événement système. Dans notre cas, c'est `button_click`. Le deuxième argument est une fonction de gestion d'événements. Nous l'appellerons `eventHandler` pour l'instant.

Maintenant, créons `eventHandler`

```c++
void eventHandler(system_event_t event, int duration, void* )
{

}

```

**Important :** vous ne pouvez pas utiliser la fonction `Log` à l'intérieur de `eventHandler`. Une façon facile de le tester est de basculer la LED sur D7. Configurons cela !

Initialisez la LED dans `setup()`

```c++
// Définir la broche de la LED
pinMode(D7,OUTPUT);

```

Ensuite, nous pouvons ajouter ceci à l'intérieur de `eventHandler`

```c++
if( event == button_click ) {
    if( digitalRead(D7) ) {
        digitalWrite(D7,LOW);
    } else {
        digitalWrite(D7,HIGH);
    }
}

```

Nous pouvons alors écrire sur D7 (la LED bleue intégrée). Nous pouvons même utiliser `digitalRead` pour lire l'état de la LED. Elle répondra avec `HIGH` ou `LOW` selon la situation.

Chargez le firmware sur l'appareil et nous aurons un bon contrôle sur la LED bleue !

Dans la section suivante, nous utiliserons le bouton Mode pour mettre l'appareil en mode "apprentissage". Cela nous permettra de faire une configuration en un seul toucher avec l'appareil Tile cible.

## Stockage de l'adresse dans l'EEPROM

![Stockage dans l'EEPROM](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-06_at_11-8cf61301-8e85-4d65-a2aa-fd37175194f5.07.24_PM.png)

Dans cette prochaine étape, nous stockerons l'adresse du Tile dans l'EEPROM. Ainsi, lorsque l'appareil est redémarré ou perd de l'énergie, nous pourrons toujours identifier le Tile plus tard.

Il reste une question en suspens. Comment faire pour qu'il enregistre l'adresse en premier lieu ?

En surveillant l'appui sur le bouton, nous pouvons mettre l'appareil en mode "apprentissage". L'appareil scannera un Tile et enregistrera l'adresse s'il en trouve un.

Tout d'abord, ajoutons une conditionnelle dans `if( uuids[i].shorted() == TILE_UUID )` :

```c++
// Si nous sommes en mode apprentissage. Enregistrer dans l'EEPROM
if( isLearningModeOn() ) {
    searchAddress = scanResult->address;
    EEPROM.put(TILE_EEPROM_ADDRESS, searchAddress);
    setLearningModeOff();
}

```

Nous utiliserons l'état de D7 comme moyen de savoir que nous sommes en "mode apprentissage". Nous faisons cela en lisant D7 en utilisant `digitalRead(D7)`. Créons une fonction qui rend cela plus clair :

```c++
bool isLearningModeOn() {
    return (digitalRead(D7) == HIGH);
}

```

Nous pouvons également remplacer `digitalWrite(D7,LOW);` et `digitalWrite(D7,HIGH);` par des fonctions similaires. Ainsi, ce que nous faisons est plus clair.

```c++
// Activer le "mode apprentissage"
void setLearningModeOn() {
    digitalWrite(D7,HIGH);
}

// Désactiver le "mode apprentissage"
void setLearningModeOff() {
    digitalWrite(D7,LOW);
}

```

Ensuite, nous attribuons une variable globale `searchAddress` comme résultat du scan. Nous configurons `searchAddress` comme ceci en haut du fichier :

```c++
BleAddress searchAddress;

```

Ensuite, nous voulons l'enregistrer dans la mémoire non volatile en utilisant `EEPROM.put`. `TILE_EEPROM_ADDRESS` est défini comme `0xa`. Vous pouvez définir `TILE_EEPROM_ADDRESS` pour utiliser l'adresse mémoire qui vous plaît. Voici la définition complète placée en haut du fichier.

```c++
#define TILE_EEPROM_ADDRESS 0xa

```

Enfin, nous éteignons la LED et le "mode apprentissage" en utilisant `setLearningModeOff()`

Chaque fois qu'un appareil est trouvé, nous utiliserons `millis()` pour définir `lastSeen`. De plus, nous pouvons suivre le dernier RSSI en utilisant `lastRSSI`. C'est un moyen économique de savoir approximativement à quelle distance se trouve l'appareil. Nous utiliserons `scanResult->rssi` pour obtenir ces informations et les définir dans la variable `lastRSSI`.

Globalement, vos modifications devraient ressembler à ceci :

```c++
...

// Imprimer l'UUID que nous recherchons
if( uuids[i].shorted() == TILE_UUID ) {
    Log.trace("UUID: %x", uuids[i].shorted());

    // Si nous sommes en mode apprentissage. Enregistrer dans l'EEPROM
    if( isLearningModeOn() ) {
        searchAddress = scanResult->address;
        EEPROM.put(TILE_EEPROM_ADDRESS, searchAddress);
        setLearningModeOff();
    }

    // Enregistrer les informations
    lastSeen = millis();
    lastRSSI = scanResult->rssi;

    // Arrêter le scan
    BLE.stopScanning();

    return;
}

```

Avant cette fonction, nous pouvons filtrer les appareils qui ne correspondent pas à notre `searchAddress`. Ajoutez ce qui suit avant `if( uuids[i].shorted() == TILE_UUID )` :

```c++
// Si l'adresse de l'appareil ne correspond pas ou si nous ne sommes pas en "mode apprentissage"
if( !(searchAddress == scanResult->address) && !isLearningModeOn() ) {
    return;
}

```

Cela ignorera les appareils qui ne correspondent pas. Il ne continuera que si l'adresse correspond ou si nous sommes en "mode apprentissage".

Maintenant, pour que nous puissions charger `searchAddress` au démarrage, nous devrons le charger depuis la mémoire flash. Ajoutez cette ligne à votre `setup():`

```c++
EEPROM.get(TILE_EEPROM_ADDRESS, searchAddress);

```

Ensuite, vérifiez que l'adresse est valide. Elle ne sera pas valide si tous les octets sont `0xFF` :

```c++
// Avertissement concernant l'adresse
if( searchAddress == BleAddress("ff:ff:ff:ff:ff:ff") ) {
    Log.warn("Placez cette carte en mode apprentissage");
    Log.warn("et gardez votre Tile à proximité.");
}

```

Nous devrions pouvoir "enseigner" à notre Argon l'adresse de notre Tile. Testons-le !

### Testez-le.

Maintenant, si nous compilons et exécutons l'application, remarquez comment il n'y a plus de sortie de journal ? Nous devons "enseigner" l'adresse du Tile à l'appareil Particle. Donc, appuyez sur le bouton mode. La LED bleue devrait s'allumer.

Une fois que votre Tile a été trouvé, la LED s'éteindra et vous verrez une sortie sur la ligne de commande. Similaire à ce que nous avons vu auparavant :

```
0000006296 [app] TRACE: MAC: D7:E7:FE:0C:A5:C0
0000006298 [app] TRACE: RSSI: -60Bm
0000006299 [app] TRACE: UUID: feed

```

L'appareil a été enregistré en mémoire !

Vous pouvez également vérifier s'il est toujours enregistré après une réinitialisation. Appuyez sur le bouton **reset** et vérifiez la même sortie que ci-dessus. Si elle s'affiche, tout est toujours bon !

## Mettre à jour le Cloud

![Publication vers le cloud Particle](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-06_at_11-34eb3433-edb7-4b57-b3ca-3be935bba026.07.53_PM.png)

Enfin, mettons en place une fonction appelée `checkTileStateChanged`. Nous l'utiliserons pour vérifier les changements d'état du Tile à intervalles réguliers.

```c++
bool checkTileStateChanged( TilePresenceType *presence ) {

}

```

Le but principal de cette fonction est de comparer la variable `lastSeen` avec la durée de "timeout". Dans notre cas, notre durée de timeout est `TILE_NOT_HERE_MS` qui doit être définie à

```c++
#define TILE_NOT_HERE_MS 30000

```

près le haut de votre programme. Il y a aussi deux autres conditions à rechercher. Une où `lastSeen` est égal à 0. Cela est généralement dû au fait que l'application n'a pas encore trouvé le Tile après le démarrage.

Le dernier cas serait si l'appareil a été vu et `lastSeen` n'est pas 0. Donc dans `checkTileStateChanged`, mettons tout ensemble.

```c++
// Vérifier s'il est ici.
if( millis() > lastSeen+TILE_NOT_HERE_MS ) {

} else if ( lastSeen == 0 ) {

} else {

}

return false;

```

Maintenant, nous voulons que cette fonction ne retourne vrai **que si l'état a changé**. Nous devons donc tirer parti du pointeur `TilePresenceType` dans l'accord.

`TilePresenceType` est simplement une énumération de tous les états possibles. Vous pouvez le placer en haut de votre fichier également. Le voici :

```c++
typedef enum {
    PresenceUnknown,
    Here,
    NotHere
} TilePresenceType;

```

Vous aurez également besoin d'une variable globale que nous pouvons passer à la fonction. Définissez cela en haut de votre fichier également :

```c++
// Statut par défaut
TilePresenceType present = PresenceUnknown;

```

Maintenant, nous pouvons comparer à chaque étape. Répond-il aux critères ? L'état est-il différent du précédent ? Si oui, retourner vrai.

Rappelez-vous, nous voudrons définir `presence` à la nouvelle valeur mise à jour. Donc chaque condition devrait mettre à jour la valeur de présence. Par exemple :

```c++
*presence = NotHere;

```

Voici à quoi ressemble la fonction entièrement développée :

```c++
bool checkTileStateChanged( TilePresenceType *presence ) {

    // Vérifier s'il est ici.
    if( millis() > lastSeen+TILE_NOT_HERE_MS ) {
        if( *presence != NotHere ) {
            *presence = NotHere;
            Log.trace("not here!");
            return true;
        }
    // Cas si nous venons de démarrer
    } else if ( lastSeen == 0 ) {
        if( *presence != PresenceUnknown ) {
            *presence = PresenceUnknown;
            Log.trace("unknown!");
            return true;
        }
    // Cas si lastSeen est < TILE_NOT_HERE_MS
    } else {
        if( *presence != Here ) {
            *presence = Here;
            Log.trace("here!");
            return true;
        }
    }

    return false;
}

```

Nous pouvons maintenant utiliser cette fonction dans la boucle principale sous le minuteur pour démarrer `Ble.scan()`. Nous pouvons l'utiliser pour envoyer une charge utile JSON. Dans ce cas, nous inclurons des informations importantes comme l'adresse Bluetooth, les données `lastSeen`, les données `lastRSSI` et un message.

```c++
// Si nous avons un changement
if( checkTileStateChanged(&present) ) {

}

```

Nous utiliserons un tableau de `char` pour obtenir notre adresse sous forme de chaîne. Vous pouvez enchaîner `toString()` avec `toCharArray` pour obtenir ce dont nous avons besoin.

```c++
// Obtenir la chaîne d'adresse
char address[18];
searchAddress.toString().toCharArray(address,sizeof(address));

```

Un exemple de chaîne de charge utile pourrait ressembler à ceci :

```c++
// Créer la charge utile
status = String::format("{\"address\":\"%s\",\"lastSeen\":%d,\"lastRSSI\":%i,\"status\":\"%s\"}",
    address, lastSeen, lastRSSI, messages[present]);

```

`status` est simplement une String définie en haut du fichier :

```c++
// La charge utile allant vers le cloud
String status;

```

Vous remarquez qu'il y a aussi une variable appelée `messages`. Il s'agit d'un tableau statique constant de chaînes. Elles sont mappées aux valeurs de `TilePresenceType`. Voici à quoi cela ressemble

```c++
const char * messages[] {
    "unknown",
    "here",
    "not here"
};

```

Ainsi, `PresenceUnknown` correspond à `"unknown"`, `Here` correspond à `"here"`, etc. C'est un moyen facile et économique d'associer une chaîne à une énumération.

Enfin, nous publierons et traiterons. Cela nous permet d'envoyer la mise à jour immédiatement.

```c++
// Publier le RSSI et les informations de l'appareil
Particle.publish("status", status, PRIVATE, WITH_ACK);

// Traiter l'événement de publication immédiatement
Particle.process();

```

La fonction globale devrait ressembler à ceci à la fin :

```c++
// Si nous avons un changement
if( checkTileStateChanged(&present) ) {

    // Obtenir la chaîne d'adresse
    char address[18];
    searchAddress.toString().toCharArray(address,sizeof(address));

    // Créer la charge utile
    status = String::format("{\"address\":\"%s\",\"lastSeen\":%d,\"lastRSSI\":%i,\"status\":\"%s\"}",
        address, lastSeen, lastRSSI, messages[present]);

    // Publier le RSSI et les informations de l'appareil
    Particle.publish("status", status, PRIVATE, WITH_ACK);

    // Traiter l'événement de publication immédiatement
    Particle.process();

}

```

Maintenant, testons-le !

### Testez-le !

![Résultats des tests dans la fenêtre du terminal](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-06_at_11-97c0bda9-1ba1-4c75-8bd7-4db655d35d51.27.35_PM.png)

Nous pouvons tester pour nous assurer que nos événements de publication se produisent sans quitter Particle Workbench. Ouvrez un nouveau terminal en allant dans **View → Terminal.** Puis utilisez la commande suivante :

```bash
particle subscribe --device <nom_de_l_appareil> <nom_de_l_événement>

```

Remplacez `<nom_de_l_appareil>` par le nom ou l'ID de votre appareil.

Remplacez `<nom_de_l_événement>` par le nom de l'événement. Dans notre cas, c'est `status`.

Vous pouvez ensuite tout tester en retirant la batterie et en attendant l'alerte "not here". Rebranchez la batterie et vous devriez recevoir une alerte "here".

Voici un exemple de la sortie

```
> particle subscribe --device hamster_turkey status

Subscribing to "status" from hamster_turkey's stream
Listening to: /v1/devices/hamster_turkey/events/status
{"name":"status","data":"{\"address\":\"C0:A5:0C:FE:E7:D7\",\"lastSeen\":40154002,\"lastRSSI\":-82,\"status\":\"not here\"}","ttl":60,"published_at":"2019-09-07T02:29:42.232Z","coreid":"e00fce68d36c42ef433428eb"}
{"name":"status","data":"{\"address\":\"C0:A5:0C:FE:E7:D7\",\"lastSeen\":40193547,\"lastRSSI\":-83,\"status\":\"here\"}","ttl":60,"published_at":"2019-09-07T02:29:50.352Z","coreid":"e00fce68d36c42ef433428eb"}

```

## Configuration du Webhook

Dans la dernière partie de ce tutoriel, nous configurerons des notifications push en utilisant un webhook. Comme mentionné précédemment, nous utiliserons Pushover et leur API pratique pour envoyer des notifications push aux appareils de votre choix.

Pushover dispose d'une API extrêmement facile à utiliser. Leur application est un couteau suisse pour les situations où vous ne voulez pas coder une application pour envoyer des notifications push.

La première chose à noter est votre **clé utilisateur.** Vous pouvez l'obtenir en vous connectant à Pushover. Note : vous devrez créer un compte d'abord si vous ne l'avez pas déjà.

Cela devrait ressembler à ceci :

![Écran principal de Pushover](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-03_at_3-e71c60fd-ef57-4e5f-a7a5-e836b36af15e.39.36_PM.png)

Si vous êtes connecté et ne voyez pas cette page, cliquez sur le **logo Pushover** et cela devrait vous ramener.

Ensuite, nous voulons créer une application. Cliquez sur **Apps & Plugins** en haut de l'écran.

![Écran Apps/Plugins dans Pushover](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-03_at_3-3144b865-133a-4778-b349-37ebb333ede7.39.42_PM.png)

Vous devriez ensuite cliquer sur **Create a New Application.** Cela nous permettra d'obtenir un **API Token** qui sera nécessaire dans la configuration du Webhook Particle.

![Créer une nouvelle application](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-05_at_11-c5628ee5-3aa9-4e82-b302-051278631a6b.49.21_AM.png)

Donnez un nom comme vous le souhaitez. Remplissez la description si vous voulez un rappel. **Cochez la case** puis cliquez sur **Create Application.**

Vous devriez passer à la page suivante. Copiez et enregistrez le **API Token/Key**, nous en aurons besoin également dans quelques étapes.

![Visualisation de l'application avec la clé API](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-03_at_3-a9e88ba1-dcb8-4b4d-8f20-a67e70e84ff5.39.50_PM.png)

Maintenant, configurons le Webhook. Rendez-vous sur [https://console.particle.io](https://console.particle.io/) et créez une nouvelle intégration.

![Console Particle créant un nouveau Webhook](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-03_at_3-ef788a5e-710f-4457-9b04-133d4ecf5f94.41.55_PM.png)

Nous définirons le **Nom de l'événement** à **status**.

L'**URL** à **[https://api.pushover.net/1/messages.json](https://api.pushover.net/1/messages.json)**

De plus, si vous souhaitez filtrer par un appareil spécifique, assurez-vous de le sélectionner dans le **menu déroulant Appareil.**

Sous **Paramètres avancés**, nous terminerons en définissant quelques champs.

![Définition du token et de la clé API dans le Webhook Particle](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Screen_Shot_2019-09-03_at_3-831e153a-bb8c-4d73-98c4-61a958c9c51a.42.01_PM.png)

Créez les champs suivants : **token**, **user**, **title** et **message**. Ensuite, définissez le token sur le **API Token** que nous avons obtenu précédemment. Faites de même pour la **User Key.**

Le **title** apparaîtra comme le titre de votre message. Faites-en ce qui a du sens pour vous.

Vous pouvez définir le **message** comme `The Tile is currently {{{status}}}. RSSI: {{{lastRSSI}}}.`

Nous utilisons ici des modèles mustache. Ils vous permettent d'utiliser les données dans la charge utile publiée et de les reformater à votre guise. Dans notre cas, nous les utilisons pour "remplir les blancs". Le **message**, une fois traité, pourrait ressembler à ceci :

`The Tile is currently here. RSSI: -77`

En aparté, je parlerai davantage de ces modèles dans [mon guide](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh/). Alors restez à l'écoute pour cela !

### Testez-le

Une fois votre intégration en place, vous pouvez tester en faisant ce que nous avons fait dans l'étape précédente. Retirez la batterie et attendez le message "not here". Remettez-la et attendez le message "here".

Voici à quoi cela pourrait ressembler sur un iPhone :

![Messages Pushover depuis le Particle Cloud](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/images/Pushover-58cbd968-ffbe-4aa5-9087-de6f98708715.png)

Comme vous pouvez le voir, je l'ai testé plusieurs fois ! 😊

Si vous êtes arrivé jusqu'ici et que tout fonctionne, excellent travail. Vous avez maintenant un tracker Tile pour votre maison, bureau ou autre.

## Le Code

Vous cherchez le code final pour cet exemple ? Je le serais aussi ! Il est [hébergé sur Github et disponible ici](https://github.com/jaredwolff/particle-bluetooth-presence-detection).

## Conclusion

Comme vous pouvez l'imaginer, les techniques et technologies utilisées dans cet article peuvent être utilisées de nombreuses manières. Résumons quelques-uns des points clés à retenir :

1. Utilisation de Bluetooth Central pour scanner et identifier un appareil Tile prêt à l'emploi
2. Stockage des informations d'identification du Tile dans l'EEPROM. Ainsi, elles peuvent être récupérées au démarrage.
3. Utilisation de notre familier `Particle.publish` pour pousser les mises à jour vers le cloud.
4. Utilisation d'un Particle Integration Webhook pour créer des notifications push lors du changement d'état.

Maintenant que vous avez tout en marche, développez-le, hackez-le et faites-en le vôtre. Oh, et n'oubliez pas de partager ! J'adorerais avoir de vos nouvelles. [hello@jaredwolff.com](mailto:hello@jaredwolff.com)

Vous aimez cet article ? Cliquez sur l'un des liens de partage ci-dessous et partagez-le avec le monde. :)

**Ceci est un article croisé de mon blog. [Vous pouvez consulter l'original ici.](https://www.jaredwolff.com/how-to-location-tracking-using-particle-mesh/)**

Intéressé à en apprendre davantage ? J'écris un guide sur la manière de tirer le meilleur parti de la plateforme Particle. [En savoir plus ici.](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh/)