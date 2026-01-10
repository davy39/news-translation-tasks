---
title: Rencontrez Pyrinas - un Kit de Développement IoT pour votre Particle Xenon
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-11T13:49:35.000Z'
originalURL: https://freecodecamp.org/news/meet-pyrinas-an-iot-development-kit-for-your-particle-xenon
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Copy-of-Particle-Mesh-App-Updates.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: embedded systems
  slug: embedded-systems
- name: iot
  slug: iot
- name: particle
  slug: particle
seo_title: Rencontrez Pyrinas - un Kit de Développement IoT pour votre Particle Xenon
seo_desc: 'By Jared Wolff

  This post is a bit lengthy. If you prefer, signup to get the full PDF here. ?

  After Particle''s Mesh deprecation announcement, many have been left to figure out
  how to deploy their low power sensor networks. There was always the option ...'
---

Par Jared Wolff

Cet article est un peu long. Si vous préférez, [inscrivez-vous pour obtenir le PDF complet ici](https://www.jaredwolff.com/files/pyrinas-intro/).

Après [l'annonce de dépréciation de Particle Mesh](https://www.jaredwolff.com/particle-mesh-deprecation-livestream/), beaucoup se sont retrouvés à devoir trouver comment déployer leurs réseaux de capteurs à faible consommation. Il y avait toujours l'option d'utiliser [la pile Bluetooth intégrée de Particle](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/), mais à ce jour, elle n'est pas sécurisée.

Précédemment, j'avais aidé à former un déploiement IoT très simple basé sur le SDK nRF, en mode hub et spoke. Malheureusement, il était closed source et l'entreprise n'existe plus.

Alors, que faire ?

En construire un autre et le rendre *open* (sous licence BSD pour être précis !). Open et gratuit pour que chacun puisse l'utiliser, l'adopter et l'améliorer. De plus, si vous construisez un produit utilisant ce code, **vous n'avez pas à partager vos améliorations ou votre code propriétaire avec qui que ce soit**.

Dans cet article, je vais parler de la manière de commencer avec Pyrinas. Il utilise le SDK éprouvé de Nordic comme base pour le noyau du système. Le concept principal de Pyrinas est d'abstraire autant que possible les détails techniques de l'IoT afin que vous puissiez vous concentrer sur votre application.

Alors, sans plus attendre, parlons de ce qu'est Pyrinas et de ce qu'il n'est pas.

## Ce qu'est Pyrinas

- Un "noyau" embarqué, écrit en C. C'est un environnement de développement IoT ouvert et permissif que vous pouvez utiliser pour tout ce que vous voulez. Sérieusement. Il est sous licence BSD et peut être utilisé dans des applications closed source.
- En utilisant la puissance du Bluetooth 5.0 Long Range, Pyrinas vous permet de communiquer avec de nombreux périphériques à la fois. Actuellement, Pyrinas a été testé avec 3 connexions périphériques simultanées. Théoriquement, il peut supporter jusqu'à 20 connexions simultanées. (Grâce au [Softdevice S140 de Nordic](https://cm.nordicsemi.com//Software-and-tools/Software/Bluetooth-Software))
- Pyrinas transporte ses données de deux manières
  - Dans un format de chaîne familier utilisé par Particle
  - Un Protocol Buffer personnalisé pour la transmission de données brutes.

  Ainsi, vous avez un **choix** sur la manière dont vous souhaitez traiter et publier vos données !

## Ce que Pyrinas n'est pas

- Pyrinas n'est pas un RTOS (système d'exploitation temps réel). Si vous avez besoin d'exécuter des applications multithreads sur des systèmes embarqués, Pyrinas n'est pas fait pour vous.
- Pyrinas, à ce jour, ne supporte pas le Mesh.
- Un OS pour chaque type de SoC Bluetooth sur le marché. En raison du couplage étroit avec le SDK nRF de Nordic, Pyrinas ne fonctionne qu'avec les SoC de Nordic.
- Une solution clé en main pour l'IoT. Pyrinas en est encore à ses débuts dans son processus de développement. L'objectif est qu'il devienne une option viable pour que chacun puisse développer et publier des applications IoT *de la manière dont il le souhaite*. Il n'y a pas de verrouillage par le fournisseur. Il n'y a pas de surprises.

## Ce dont vous aurez besoin

Il y a quelques choses dont vous aurez besoin pour commencer avec Pyrinas.

- Au moins 2 Particle Xenon
- Au moins 1 carte de développement nRF ou un programmeur J-link
- Les câbles USB associés

## Commencer avec un exemple

Pour commencer avec Pyrinas, vous aurez besoin de deux dépôts.

- [Le dépôt du système d'exploitation](https://github.com/pyrinas-iot/pyrinas-os)
- [Le modèle](https://github.com/pyrinas-iot/pyrinas-template)

Le dépôt du système d'exploitation contient toutes les sources, les dépendances du SDK et la chaîne d'outils dont vous avez besoin pour utiliser Pyrinas.

Le modèle est l'endroit où vous ajoutez tout votre code d'application. Le modèle fournit un point de départ pour vous et votre projet.

Voici comment tout s'assemble :

Clonez le dépôt du système d'exploitation à un endroit sur votre machine :

```shell
git clone https://github.com/pyrinas-iot/pyrinas-os.git --recurse-submodules
```

Une fois terminé, changez de répertoire pour `pyrinas-os` et exécutez `make setup`

```shell
cd pyrinas-os
make setup
```

Cela téléchargera votre chaîne d'outils et les dépendances du SDK.

Pour utiliser l'OTA DFU, vous devrez également générer la clé DFU pour le processus :

```shell
make gen_key
```

Les fichiers générés par ce processus seront utilisés plus tard.

Ensuite, nous voudrons utiliser le modèle pour créer deux nouveaux projets. Dans cet exemple, nous aurons un "hub" et un "capteur". Naviguez simplement vers le [dépôt du modèle](https://github.com/pyrinas-iot/pyrinas-template) et cliquez sur le bouton **Utiliser ce modèle**.

![https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Screen_Shot_2020-03-09_at_5.12.21_PM.png](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Screen_Shot_2020-03-09_at_5.12.21_PM.png)

Puis nommez votre nouveau dépôt. Cliquez sur le bouton **Créer un dépôt à partir du modèle** lorsque vous êtes satisfait de tout.

![https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Screen_Shot_2020-03-09_at_5.20.15_PM.png](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Screen_Shot_2020-03-09_at_5.20.15_PM.png)

Puis clonez votre dépôt dans le même répertoire que `pyrinas-os`. Assurez-vous de remplacer `<votre nom d'utilisateur>` et `<nom du dépôt>` par les vôtres.

```shell
cd ..
git clone https://github.com/<votre nom d'utilisateur>/<nom du dépôt>.git hub
```

Après cela, retournez et créez un nouveau dépôt à partir du modèle. Nous utiliserons celui-ci pour le nœud *capteur*.

![https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Screen_Shot_2020-03-09_at_5.24.15_PM.png](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Screen_Shot_2020-03-09_at_5.24.15_PM.png)

Clonez ce dépôt une fois que vous avez terminé sa configuration au même endroit que vos dépôts `hub` et `pyrinas-os`.

Maintenant que nous avons tous nos dépôts, commençons par notre nœud capteur.

### Configuration du dépôt du nœud capteur

Ouvrez le dépôt du capteur en utilisant un programme comme Microsoft VS Code. Si vous avez les raccourcis de ligne de commande, vous pouvez utiliser `code` pour l'ouvrir depuis le terminal :

```shell
code sensor
```

Avant de faire quoi que ce soit, nous devrons configurer le lien symbolique vers `pyrinas-os`. Assurez-vous d'être dans le répertoire `sensor` puis exécutez `ln -s ../pyrinas-os/` en utilisant le terminal.

```shell
cd sensor
ln -s ../pyrinas-os/ .
```

Cela permet à votre projet d'utiliser tout le code, le SDK et les chaînes d'outils dans le dépôt `pyrinas-os` ! En bonus, vous pouvez faire cela autant de fois que vous le souhaitez. Avez-vous plusieurs projets Pyrinas ? Aucun problème.

Très bien ! Maintenant, examinons le Makefile. Vous voudrez personnaliser certaines des définitions dans le fichier :

```makefile
# Début : Votre configuration !

# Définissez ceci sur le répertoire de pyrinas-os
# Si vous avez utilisé un lien symbolique, cela pointe vers
# le dossier `pyrinas-os` dans ce dépôt
OS_DIR := pyrinas-os

# Ceci doit être le numéro de série de votre programmeur Jlink.
# Pour le trouver, exécutez simplement `jlinkexe`
PROG_SERIAL=1234678

# Ceci est votre port de débogage pour le RTT de Jlink. Si vous
# en avez plusieurs, vous devrez changer ceci pour chaque application
# que vous utilisez
PROG_PORT=19021

# Ici, vous définissez votre type de carte. Voici les cartes supportées :
# xenon - Particle Xenon
BOARD=xenon

# Ici, vous pouvez nommer votre application. Soyez spécifique
APP_FILENAME=pyrinas-template

# Ceci détermine si vous utilisez le mode débogage ou non
# Commentez ceci ou changez en false
DEBUG=true

# Fin : Votre Configuration
```

Par exemple, vous pouvez vouloir configurer le numéro de série de votre programmeur. Cela vous permet d'utiliser plusieurs programmeurs en même temps. (Très utile pour déboguer les deux appareils en même temps) Pour obtenir le numéro de série de votre programmeur, branchez votre carte de développement et exécutez `jlinkexe`.

    jlinkexe
    SEGGER J-Link Commander V6.62a (Compilé le 31 janv. 2020 12:59:22)
    Version DLL V6.62a, compilée le 31 janv. 2020 12:59:05

    Connexion à J-Link via USB...OK.
    Micrologiciel : J-Link OB-SAM3U128-V2-NordicSemi compilé le 21 janv. 2020 17:30:48
    Version matérielle : V1.00
    N° de série : 581758669
    Licence(s) : RDI, FlashBP, FlashDL, JFlash, GDB
    VTref=3.300V


    Tapez "connect" pour établir une connexion cible, '?' pour l'aide
    J-Link>

Trouvez la zone **N° de série**. C'est votre numéro de série !

Alternativement, vous pouvez regarder l'autocollant sur votre kit de développement. Il contiendra le numéro de série de votre appareil.

Pour le `PROG_PORT`, vous voulez utiliser différents ports pour chaque appareil que vous déboguez simultanément. J'ai trouvé que **19021** et **19020** sont de bonnes options pour la plupart des sessions de débogage à deux appareils.

Le Makefile inclut également la possibilité de choisir une carte. Dans notre cas, il n'y a qu'une seule option : `xenon`. Les futures révisions de Pyrinas auront plusieurs options.

`APP_FILENAME` est le nom de votre application. Nous renommerons la nôtre en `pyrinas-sensor`

Enfin, `DEBUG` est utilisé pour arrêter l'exécution soit sur une erreur, soit pour redémarrer. Pour la production, cela doit être commenté ou défini sur `false`. Nous pouvons le laisser tel quel pour l'instant.

Le Makefile est également la source de certaines des commandes les plus importantes dont vous aurez besoin pendant le développement :

- `make build` - construit votre application.
- `make clean` - nettoie tous les vestiges de votre application.
- `make debug` - ouvre la console de débogage `jlinkexe`.
- `make erase` - efface la puce connectée à votre programmeur.
- `make flash` - flashe l'application actuelle sur votre appareil connecté.
- `make flash_softdevice` - flashe le soft_device
- `make rtt` - ouvre la console de débogage.
- `make ota` - génère un fichier zip utilisé pour le DFU BLE

### Code de base du nœud capteur

![https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Copy_of_Particle_Mesh_App_Updates-3.jpg](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Copy_of_Particle_Mesh_App_Updates-3.jpg)

Maintenant que nous avons couvert certaines des bases, créons une application très simple qui publie à intervalles réguliers. Si vous regardez `app.c`, vous verrez du code dans la fonction `setup()`. Supprimons tout le code commenté. (Nous l'utiliserons plus tard pour le hub)

Votre code devrait maintenant ressembler à ceci :

```c
#include "app.h"

void setup()
{
  BLE_STACK_PERIPH_DEF(init);

  // Configuration pour la pile ble
  ble_stack_init(&init);

  // Démarrer la publicité
  advertising_start();
}

void loop()
{
}
```

Maintenant, créons un timer que nous utiliserons pour publier à intervalles réguliers. Sous `#include "app.h"`, créez un nouveau timer :

```c
#include "app.h"

timer_define(m_sensor_timer);
```

Nous devons également le configurer dans la fonction `setup()` :

```c
// Timer du capteur
timer_create(&m_sensor_timer, TIMER_REPEATED, sensor_timer_evt);
```

Vous remarquerez que `timer_create` fait référence à un rappel d'événement appelé `sensor_timer_evt`. Nous devons également créer ce dernier :

```c
static void sensor_timer_evt() {
	// Nous reviendrons dans une seconde
}
```

La dernière chose est de démarrer le timer. Faisons cela sous `timer_create` :

```c
// Démarrer
timer_start(&m_sensor_timer, 1000);
```

Cela démarrera notre timer répétitif sur un intervalle de 1 seconde. (`timer_start` est configuré en utilisant des millisecondes)

Maintenant, à l'intérieur de `sensor_timer_evt`, nous publierons quelques données. Mais d'abord, nous devons nous assurer que Bluetooth est connecté en utilisant `ble_is_connected`.

```c
static void sensor_timer_evt
{
  // Vérifier si nous sommes connectés
  if (ble_is_connected())
  {
    // Envoie "ping" avec le nom d'événement "data"
    ble_publish("data", "ping");
  }
}
```

À l'intérieur de l'instruction if, nous utiliserons `ble_publish`. Le premier argument est le nom de l'événement et le second est la valeur.

Ensuite, pour recevoir des messages de l'autre extrémité, nous devrons configurer un rappel :

```c
// Configuration pour la pile ble
ble_stack_init(&init);

// Configuration du rappel BLE
ble_subscribe("data", ble_evt);
```

Nous définirons `ble_evt` en haut du fichier :

```c
static void ble_evt(char *name, char *data)
{
  NRF_LOG_INFO("%s: %s", name, data);
}
```

Dans ce cas, nous utiliserons `NRF_LOG_INFO` pour imprimer le message du hub.

Enfin, pour obtenir l'adresse MAC facilement, nous devrons ajouter un appel pour l'imprimer dans `setup()`.

```c
// Imprimer l'adresse
util_print_device_address();
```

À la fin, votre fichier devrait ressembler à ceci :

```c
#include "app.h"

timer_define(m_sensor_timer);

// Capturer les événements envoyés via Bluetooth
static void ble_evt(char *name, char *data)
{
  NRF_LOG_INFO("%s: %s", name, data);
}

static void sensor_timer_evt()
{
  // Vérifier si nous sommes connectés
  if (ble_is_connected())
  {
    // Envoie "ping" avec le nom d'événement "data"
    ble_publish("data", "ping");
  }
}

void setup()
{
  BLE_STACK_PERIPH_DEF(init);

  // Configuration pour la pile ble
  ble_stack_init(&init);

  // Configuration du rappel BLE
  ble_subscribe("data", ble_evt);

  // Démarrer la publicité
  advertising_start();

  // Timer du capteur.
  timer_create(&m_sensor_timer, TIMER_REPEATED, sensor_timer_evt);

  // Démarrer
  timer_start(&m_sensor_timer, 1000);

  // Imprimer l'adresse
  util_print_device_address();
}

void loop()
{
}
```

Ensuite, nous allons le programmer sur du matériel !

### Flashage du code de base du capteur :

Pour cette étape, vous aurez besoin d'un Xenon à portée de main. Vous aurez également besoin d'un programmeur, d'un câble de programmation et de deux câbles USB Micro-B. Voici une photo de tout connecté :

![https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//IMG_4586.jpg](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//IMG_4586.jpg)

Une fois connecté et alimenté, exécutez ces commandes :

```shell
make erase
make flash_softdevice
make flash
make debug
```

Puis dans une fenêtre de terminal séparée, exécutez

```shell
make rtt
```

`make debug` et `make rtt` créeront une session de débogage. Vous pouvez émettre des commandes dans le terminal `make debug` pour contrôler l'appareil également. Par exemple, `r` suivi de `Enter` redémarrera l'appareil. (De loin mon cas d'utilisation le plus courant).

Si vous avez flashé tout avec succès, votre appareil devrait commencer à clignoter en vert. C'est un bon signe !

De plus, si vous regardez le côté `make rtt`, votre sortie devrait être similaire à ceci :


    ###RTT Client: Connexion au serveur RTT J-Link via localhost:19021 ...
    ###RTT Client: Connecté.

    SEGGER J-Link V6.62a - Sortie du terminal en temps réel
    J-Link OB-SAM3U128-V2-NordicSemi compilé le 21 janv. 2020 17:30:48 V1.0, SN=581758669
    Processus : JLinkExe
    <info> app_timer: RTC: initialisé.
    <info> app: Compte de démarrage: 4
    <info> app: Pyrinas démarré.
    <info> app: Adresse: 11:22:33:44:55:66

Prenez note de l'adresse affichée ci-dessus. Nous en aurons besoin pour le code du hub !

### Configuration du dépôt du hub

![https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Copy_of_Particle_Mesh_App_Updates-2.jpg](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Copy_of_Particle_Mesh_App_Updates-2.jpg)

Si vous ne l'avez pas déjà fait, clonez votre dépôt hub localement. Nous voudrons faire certaines des mêmes étapes que nous avons faites avec le dépôt du capteur comme :

- Configuration du lien symbolique
- Mise à jour du Makefile
    - Définition de votre `PROG_SERIAL`
    - Définition de `PROG_PORT` sur un port non utilisé par la configuration du capteur. `19020` dans ce cas est correct.
    - Définition de `APP_FILENAME` sur `pyrinas-hub`

Si vous avez besoin d'un rappel sur la manière dont ces étapes fonctionnent, revenez en arrière et passez en revue la section précédente.

Ensuite, nous voudrons ouvrir `app.c` et décommenter le code basé sur le hub/central. De plus, vous voudrez supprimer le code décommenté par défaut. Votre `setup()` devrait ressembler à ceci :

```c
void setup()
{
  // Configuration par défaut pour le mode central
  BLE_STACK_CENTRAL_DEF(init);

  // Ajouter une adresse à scanner
  ble_gap_addr_t first = {
      .addr_type = BLE_GAP_ADDR_TYPE_RANDOM_STATIC,
      .addr = {0x81, 0x64, 0x4C, 0xAD, 0x7D, 0xC0}};
  init.config.devices[0] = first;

  ble_gap_addr_t second = {
      .addr_type = BLE_GAP_ADDR_TYPE_RANDOM_STATIC,
      .addr = {0x7c, 0x84, 0x9d, 0x32, 0x8d, 0xe4}};
  init.config.devices[1] = second;

  // Incrémenter le compteur de périphériques
  init.config.device_count = 2;

  // Configuration pour la pile ble
  ble_stack_init(&init);

  // Démarrer le scan.
  scan_start();
}
```

Vous remarquerez immédiatement qu'il y a deux clients/appareils définis ici. Supprimons le second. Si, à l'avenir, vous souhaitez connecter plus d'appareils, voici un exemple de la manière de procéder.

**Rappel :** assurez-vous également de changer `init.config.device_count` en `1`.

Ensuite, vous voudrez mettre à jour le champ `.addr` dans `ble_gap_addr_t first` pour qu'il corresponde à l'adresse que nous avons obtenue précédemment de `make rtt` :

```c
// Ajouter une adresse à scanner
ble_gap_addr_t first = {
    .addr_type = BLE_GAP_ADDR_TYPE_RANDOM_STATIC,
    .addr = {0x11,0x22,0x33,0x44,0x55,0x66}};
init.config.devices[0] = first;
```

Le champ d'adresse utilise des octets bruts, il doit donc être représenté de cette manière. Supprimez les `:` et placez `0x` devant chaque octet. Nous passons de `11:22:33:44:55:66` à `{0x11,0x22,0x33,0x44,0x55,0x66}`

Maintenant, avant de flasher quoi que ce soit, configurons également le gestionnaire d'événements Bluetooth. Comme précédemment, nous utiliserons `ble_subscribe` pour attacher un gestionnaire d'événements :

```c
// Configuration du rappel BLE
ble_subscribe("data", ble_evt);

Puis placez la fonction en haut du fichier :

// Capturer les événements envoyés via Bluetooth
static void ble_evt(char *name, char *data)
{
  NRF_LOG_INFO("%s: %s", name, data);

  ble_publish("data", "pong");
}
```

Vous remarquerez que nous imprimons le message en utilisant `NRF_LOG_INFO`. Nous envoyons également un message *en retour* au capteur sous la forme de `ble_publish("data","pong");` En d'autres termes, nous jouons à un jeu de ping-pong entre les deux appareils !

À la fin, votre code devrait ressembler à ceci :

```c
#include "app.h"

// Capturer les événements envoyés via Bluetooth
static void ble_evt(char *name, char *data)
{
  NRF_LOG_INFO("%s: %s", name, data);

  ble_publish("data", "pong");
}

void setup()
{
  // Configuration par défaut pour le mode central
  BLE_STACK_CENTRAL_DEF(init);

  // Ajouter une adresse à scanner
  ble_gap_addr_t first = {
      .addr_type = BLE_GAP_ADDR_TYPE_RANDOM_STATIC,
      .addr = {0x11, 0x22, 0x33, 0x44, 0x55, 0x66}};
  init.config.devices[0] = first;

  // Incrémenter le compteur de périphériques
  init.config.device_count = 1;

  // Configuration pour la pile ble
  ble_stack_init(&init);

  // Configuration du rappel BLE
  ble_subscribe("data", ble_evt);

  // Démarrer le scan.
  scan_start();
}

void loop()
{
}
```
**Rappel :** assurez-vous de définir `ble_gap_addr_t first` ou les deux appareils ne se connecteront pas !

Pour programmer, connectez le Xenon à programmer comme vous l'avez fait auparavant. Nous allons le flasher en utilisant les mêmes méthodes que précédemment :

```shell
make erase
make flash_softdevice
make flash
make debug
```

Puis dans une fenêtre de terminal séparée, exécutez

```shell
make rtt
```

Puis regardez chacun des écrans `make rtt`. Il devrait y avoir une sortie ! Pour le hub, cela devrait ressembler à ceci :

    Processus : JLinkExe
    <info> app: Compte de démarrage: 4
    <info> app: Pyrinas démarré.
    <info> ble_m_central: Connecté au handle 0x0
    <info> ble_m_central: Service Protobuf découvert
    <info> app: data: ping
    <info> app: data: ping

Et le côté capteur comme ceci :

    Processus : JLinkExe
    <info> app_timer: RTC: initialisé.
    <info> app: Compte de démarrage: 4
    <info> app: Pyrinas démarré.
    <info> app: Adresse: 11:22:33:44:55:66
    <info> ble_m_periph: Notifications activées !
    <info> app: data: pong
    <info> app: data: pong

Les messages ping et pong devraient continuer jusqu'à ce que vous les arrêtiez. Super ! Si vous obtenez des avertissements comme celui-ci :

    Impossible d'écrire. Les notifications ne sont pas activées !

Utilisez le bouton de réinitialisation sur l'un des appareils. Cela devrait résoudre le problème.

**Note de côté :** le processus d'appariement pour Bluetooth est intrinsèquement ***non sécurisé***. Une fois le processus d'appariement terminé, les appareils sont sécurisés. (Avec la réserve que personne n'a espionné le processus d'appariement !) Il pourrait y avoir des améliorations en matière de sécurité à l'avenir.

**Félicitations ! ?** Si vous êtes arrivé jusqu'ici, vous avez déployé votre premier hub et client capteur Pyrinas !

Pour plus d'informations sur ce que Pyrinas peut faire, vous devriez consulter les fichiers d'en-tête sous `pyrinas-os/include/`. De plus, Pyrinas peut faire tout ce que vous pourriez normalement faire avec le SDK de Nordic. [Le centre d'information de Nordic](https://infocenter.nordicsemi.com/topic/struct_sdk/struct/sdk_nrf5_latest.html?cp=7_1) est une excellente ressource pour en savoir plus sur ce que le SDK a à offrir.

## Que réserve l'avenir pour Pyrinas ?

![https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Copy_of_Particle_Mesh_App_Updates-5.jpg](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/images//Copy_of_Particle_Mesh_App_Updates-5.jpg)

Toutes les tâches futures pour Pyrinas sont partagées ouvertement sur le [dépôt Github](https://github.com/pyrinas-iot/pyrinas-os/projects). Voici quelques-unes des améliorations de haut niveau sur la feuille de route :

- Prise en charge du Particle Boron + LTE - C'est vrai ! La connectivité cellulaire arrive sur Pyrinas. À l'heure où nous écrivons ces lignes, la première carte à supporter le LTE de Pyrinas sera le Boron de Particle.
- Prise en charge de MQTT (sur TLS) et HTTPS - Une fois que nous aurons la connectivité cellulaire, nous aurons besoin de quelque chose pour communiquer. C'est là que MQTT et HTTPS entrent en jeu. Ce sont certains des protocoles les plus populaires pour l'IoT aujourd'hui.
- Prise en charge intégrée de l'OTA à distance - À l'heure actuelle, les appareils programmés avec Pyrinas utilisent le chargeur de démarrage sécurisé de Nordic. Cela signifie qu'ils peuvent être mis à jour par voie herzienne par un ordinateur ou un téléphone à proximité. Ce n'est pas durable pour les déploiements à long terme !
À la place, vous pourrez pousser des mises à jour vers les appareils Pyrinas via le Cloud. Oui. Aucune raison de quitter votre canapé, vous pouvez déployer vos mises à jour de n'importe où.
- Configuration et gestion dynamiques - ajouter et supprimer des appareils d'un système Pyrinas nécessite actuellement quelques efforts. Dans les futures révisions, il sera plus facile d'ajouter et de supprimer des appareils à la volée. Cela permet une gestion à distance des appareils sans aucun casse-tête.
- Prise en charge des modules pré-certifiés et d'autres cartes de développement basées sur le nRF52840 de Nordic. Actuellement, le Xenon est la seule carte supportée. Les cartes de développement ne sont pas idéales pour une production complète. Restez à l'écoute pour la prise en charge des modules pré-certifiés de fournisseurs comme [Fanstel](https://www.fanstel.com/bluenor-summaries) et plus encore...
- Prise en charge de plus d'environnements de développement. Actuellement, Pyrinas supporte uniquement Mac.

### Étoiler et Surveiller !

Ce n'est que le début ! Restez à l'écoute pour plus de mises à jour et assurez-vous d'étoiler et de surveiller [le dépôt](https://github.com/pyrinas-iot/pyrinas-os).

Ou mieux encore, vous cherchez à aider ? Les contributions sont les bienvenues !

**Vous pouvez lire d'autres articles sur mon blog, [jaredwolff.com](https://www.jaredwolff.com/meet-pyrinas-a-new-way-to-use-your-xenon/)**