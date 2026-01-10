---
title: Comment utiliser l'API Bluetooth puissante de Particle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-15T12:39:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-particles-powerful-bluetooth-api
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Particle-Bluetooth.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: hardware
  slug: hardware
- name: particle
  slug: particle
seo_title: Comment utiliser l'API Bluetooth puissante de Particle
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  I was defeated.

  I had spent the whole night trying to get a Bluetooth Low Energy project working.
  It was painful. It was frustrating. I was ready to give up.

  That was during the early day...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/)**

J'étais vaincu.

J'avais passé toute la nuit à essayer de faire fonctionner un projet Bluetooth Low Energy. C'était douloureux. C'était frustrant. J'étais prêt à abandonner.

C'était pendant les premiers jours du Bluetooth Low Energy. Depuis, cela est devenu de plus en plus facile à développer. La bibliothèque Particle Mesh Bluetooth ne fait pas exception.

Dans ce guide, je vais vous montrer comment utiliser l'API Bluetooth de Particle. Nous allons configurer quelques LEDs et les voir changer sur tous les appareils du réseau Mesh. Nous utiliserons une carte Argon et Xenon.

Prêt ? Commençons !

P.S. cet article est long. Si vous voulez quelque chose à télécharger, [cliquez ici pour un PDF magnifiquement formaté.](https://www.jaredwolff.com/files/how-to-use-particles-powerful-bluetooth-api-pdf)

## Étape 1 : Configuration de Bluetooth

1. [Téléchargez/Installez Particle Workbench](https://www.particle.io/workbench/)
2. Créez un nouveau projet. J'ai choisi un emplacement approprié et l'ai nommé `ble_mesh`

    ![Créez un nouveau projet dans Particle Workbench](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_5-4348ea15-e220-4138-8d28-a8c5de99e9fe.32.11_PM.png)

3. Allez dans votre répertoire `/src/` et ouvrez votre fichier `<votre nom de projet>.ino`
4. Assurez-vous de changer la version de votre deviceOS pour qu'elle soit > **1.3.0**

    ![Sélectionnez la version de DeviceOS](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_5-9d20c90b-e27c-4609-9917-2ec1bb849727.40.15_PM.png)

### Écrire le code

Nous voulons configurer un service avec 3 caractéristiques. Les caractéristiques concernent l'intensité des LEDs RGB respectivement. Voici comment configurer votre Bluetooth :

1. Dans votre fonction `Setup()`, activez le contrôle de l'application sur votre LED

    ```
    RGB.control(true);
    ```

2. Configurez vos UUIDs en haut de votre fichier `.ino`

        const char* serviceUuid = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E";
        const char* red         = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E";
        const char* green       = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E";
        const char* blue        = "6E400004-B5A3-F393-E0A9-E50E24DCCA9E";

    Les UUIDs sont des identifiants ou adresses uniques. Ils sont utilisés pour différencier les différents services et caractéristiques sur un appareil.

    Les UUIDs ci-dessus sont utilisés dans des exemples précédents de Particle. Si vous souhaitez créer les vôtres, vous pouvez utiliser `uuidgen` sur la ligne de commande OSX. Vous pouvez également aller sur un site comme **[Online GUID Generator](https://www.guidgenerator.com/online-guid-generator.aspx).**

    ![Générateur de GUID en ligne](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-14_at_11-343e1df6-69e8-4560-98b9-f2f54caeb7d3.28.46_AM.png)

    Utilisez les paramètres ci-dessus pour obtenir votre propre UUID. Vous pouvez ensuite créer vos UUIDs de service et de caractéristique à partir de celui généré :

        const char* serviceUuid = "b425040**0**-fb4b-4746-b2b0-93f0e61122c6"; //service
        const char* red         = "b4250401-fb4b-4746-b2b0-93f0e61122c6"; //red char
        const char* green       = "b4250402-fb4b-4746-b2b0-93f0e61122c6"; //green char
        const char* blue        = "b4250403-fb4b-4746-b2b0-93f0e61122c6"; //blue char

    Il n'y a pas de bonne ou de mauvaise façon de faire cela. Mais vous devez être prudent et ne pas utiliser les UUIDs réservés par le Bluetooth SIG. Cela est très improbable. Si vous voulez vérifier, vous pouvez aller [ici](https://www.bluetooth.com/specifications/gatt/characteristics/) et [ici](https://www.bluetooth.com/specifications/gatt/services/).

    Pour l'instant, nous allons nous en tenir au premier ensemble d'UUIDs.

3. Dans `Setup()`, initialisez votre service.

        // Définir le service BLE RGB
        BleUuid rgbService(serviceUuid);

    C'est la première étape de l'"enregistrement" de votre service. Plus d'informations à ce sujet ci-dessous.

4. Initialisez chaque caractéristique dans `Setup()`

        BleCharacteristic redCharacteristic("red", BleCharacteristicProperty::WRITE_WO_RSP, red, serviceUuid, onDataReceived, (void*)red);
        BleCharacteristic greenCharacteristic("green", BleCharacteristicProperty::WRITE_WO_RSP, green, serviceUuid, onDataReceived, (void*)green);
        BleCharacteristic blueCharacteristic("blue", BleCharacteristicProperty::WRITE_WO_RSP, blue, serviceUuid, onDataReceived, (void*)blue);

    Pour cette configuration, nous allons utiliser la propriété `WRITE_WO_RSP`. Cela nous permet d'écrire les données et de ne pas attendre de réponse.
    J'ai référencé les UUIDs comme les deux prochains paramètres. Le premier étant l'UUID de la caractéristique. Le second étant l'UUID du service.

    Le paramètre suivant est la fonction de rappel. Lorsque des données sont écrites dans ce rappel, cette fonction sera déclenchée.

    Enfin, le dernier paramètre est le contexte. Que signifie cela exactement ? Nous utilisons le même rappel pour les trois caractéristiques. La seule façon de savoir quelle caractéristique a été écrite (dans deviceOS au moins) est de définir un contexte. Dans ce cas, nous allons utiliser les UUIDs déjà disponibles.

5. Juste après avoir défini les caractéristiques, ajoutons-les pour qu'elles apparaissent :

        // Ajouter les caractéristiques
        BLE.addCharacteristic(redCharacteristic);
        BLE.addCharacteristic(greenCharacteristic);
        BLE.addCharacteristic(blueCharacteristic);

6. Configurez la fonction de rappel.

        // Fonction statique pour gérer les rappels Bluetooth Low Energy
        static void onDataReceived(const uint8_t* data, size_t len, const BlePeerDevice& peer, void* context) {

        }

    Vous pouvez faire cela en haut du fichier (au-dessus de `Setup()`). Nous allons définir cela plus tard.

7. Enfin, pour que votre appareil soit connectable, nous devons configurer la publicité. Placez ce code à la fin de votre fonction `Setup()`

        // Données de publicité
        BleAdvertisingData advData;

        // Ajouter le service LED RGB
        advData.appendServiceUUID(rgbService);

        // Commencer la publicité !
        BLE.advertise(&advData);

    Tout d'abord, nous créons un objet `BleAdvertisingData`. Nous ajoutons le `rgbService` de l'étape 3. Enfin, nous pouvons commencer la publicité pour que notre service et nos caractéristiques soient découvrables !

### Temps de tester

À ce stade, nous avons un programme minimalement viable. Compilons-le et programmons-le sur notre matériel Particle. Cela devrait fonctionner avec n'importe quel appareil compatible Mesh. (Xenon, Argon, Boron)

1. Avant de commencer les tests, ajoutez temporairement `SYSTEM_MODE(MANUAL);` en haut de votre fichier. Cela empêchera l'appareil de se connecter au réseau mesh. Si l'appareil clignote en bleu au démarrage, vous devrez le configurer avec l'[Application Particle](https://apps.apple.com/ru/app/particle-iot/id991459054?l=en) avant de continuer.
2. [Téléchargez l'image 1.3.0-rc.1 ici.](https://github.com/particle-iot/device-os/releases/tag/v1.3.0-rc.1) Pour Xenon, vous aurez besoin de **xenon-system-part1@1.3.0-rc.1.bin.** Pour les autres, cherchez **boron-system-part1@1.3.0-rc.1.bin** et **argon-system-part1@1.3.0-rc.1.bin.** Les fichiers se trouvent en bas de la page sous **Assets**

    ![Emplacement des Assets sur la page de sortie de DeviceOS](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-14_at_11-df9b46f4-e230-484e-b69e-828526f5566e.39.39_AM.png)

3. Mettez votre appareil en mode DFU. Maintenez le **bouton Mode** enfoncé et cliquez brièvement sur le **bouton Reset**. Continuez à maintenir le **bouton Mode** enfoncé jusqu'à ce que la LED clignote en jaune.
4. Dans une fenêtre de ligne de commande, changez de répertoire pour aller là où vous avez stocké le fichier que vous avez téléchargé. Dans mon cas, la commande est `cd ~/Downloads/`
5. Ensuite, exécutez :

        particle flash --usb xenon-system-part1@1.3.0-rc.1.bin

    Cela installera le dernier système d'exploitation sur votre Xenon. Une fois terminé, il continuera à clignoter rapidement en jaune. Si vous avez un autre appareil Particle Mesh, changez le nom du fichier pour qu'il corresponde.

6. Dans Visual Code, utilisez la combinaison de touches **Command + Shift + P** pour faire apparaître le menu de commande. Sélectionnez **Particle: Compile application (local)**

    ![Choix de compilation de l'application (local)](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_10-8cb8dda2-73ae-4b0d-af5b-33892d66752e.52.19_PM.png)

7. Corrigiez les erreurs qui pourraient apparaître.
8. Ensuite, ouvrez le même menu et sélectionnez **Flash application (local)**

    ![Choix de flash de l'application (local)](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_10-4ff7bc95-58f1-497f-9edf-9eadb69e3abb.51.59_PM.png)

9. Une fois la programmation terminée, sortez votre téléphone. Ensuite, ouvrez votre application Bluetooth Low Energy préférée. Les meilleures sont **[NRF Connect](https://apps.apple.com/cn/app/nrf-connect/id1054362403?l=en)** et **[Light Blue Explorer.](https://apps.apple.com/ru/app/lightblue-explorer/id557428110?l=en)** Je vais utiliser Light Blue Explorer pour cet exemple.
10. Vérifiez si un appareil nommé **"Xenon-<ID>"** est en publicité. Insérez **<ID>** avec l'ID unique de votre appareil.

    ![Résultats de l'analyse de Light Blue Explorer](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2187-aa8b88cc-f423-4b5a-8bb0-e1f75c3b7dd9.png)

11. Trouvez votre appareil et cliquez sur le nom.
12. Regardez la liste des services et caractéristiques. Inclut-elle le service et les UUIDs des caractéristiques que nous avons définis jusqu'à présent ? Par exemple, l'UUID du service apparaît-il comme **6E400001-B5A3-F393-E0A9-E50E24DCCA9E** ?

    ![Confirmez que Light Blue Explorer a de nouveaux UUIDs de caractéristiques](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2188-d7759af0-964e-4067-9ca2-d78edd190410.png)

    Si tout apparaît comme vous l'attendez, vous êtes sur la bonne voie. Sinon, passez en revue les instructions précédentes pour vous assurer que tout correspond.

## Étape 2 : Gestion des données

La prochaine étape de notre projet consiste à traiter les événements d'écriture. Nous allons mettre à jour notre fonction `onDataReceived`.

### Écrire le code

1. Tout d'abord, créons une structure qui conservera l'état des LEDs. Cela peut être fait en haut du fichier.

        // Variables pour conserver l'état
        typedef struct {
          uint8_t red;
          uint8_t green;
          uint8_t blue;
        } led_level_t;

2. La deuxième partie consiste à créer une variable statique utilisant ce type de données

        // Suivi de niveau statique
        static led_level_t m_led_level;

    Les deux premières étapes nous permettent d'utiliser une seule variable pour représenter les trois valeurs de la LED RGB.

3. Ensuite, vérifions les erreurs de base à l'intérieur de la fonction `onDataReceive`. Par exemple, nous voulons nous assurer que nous recevons seulement un octet.

        // Nous ne cherchons qu'un seul octet
          if( len != 1 ) {
            return;
        	}

4. Ensuite, nous voulons voir de quelle caractéristique provient cet événement. Nous pouvons utiliser la variable `context` pour déterminer cela.

        // Définit le niveau global
          if( context == red ) {
            m_led_level.red = data[0];
          } else if ( context == green ) {
            m_led_level.green = data[0];
          } else if ( context == blue ) {
            m_led_level.blue = data[0];
          }

    Rappelez-vous, dans ce cas, le contexte sera égal au pointeur de l'une des chaînes UUID rouge, verte ou bleue. Vous pouvez également remarquer que nous définissons `m_led_level`. Ainsi, nous pouvons mettre à jour la LED RGB même si une seule valeur a changé.

5. Enfin, une fois défini, vous pouvez écrire dans l'objet `RGB`

        // Définir la couleur RGB
        	RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

### Tester le code

Passons par la même procédure que précédemment pour flasher l'appareil.

1. Mettez votre appareil en mode DFU. Maintenez le **bouton Mode** enfoncé et cliquez sur le **bouton Reset**. Continuez à maintenir le **bouton Mode** enfoncé jusqu'à ce que la LED clignote en jaune.
2. Ensuite, ouvrez le même menu et sélectionnez **Flash application (local)**

    ![Choix de flash de l'application (local)](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-13_at_10-4ff7bc95-58f1-497f-9edf-9eadb69e3abb.51.59_PM.png)

3. Une fois la programmation terminée, connectez-vous à l'appareil en utilisant **Light Blue Explorer**.
4. Appuyez sur la caractéristique qui s'applique à la LED rouge.
5. **Écrivez FF**. La LED rouge devrait s'allumer.

    ![Choix de la nouvelle valeur d'écriture](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2191-b8ad0693-f4f8-4828-ae99-b0a0e204cc50.jpg)

    ![Écrivez la valeur hexadécimale de 0xff](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2190-2c799875-22e5-44bc-9edc-c647cf8669f6.png)

6. **Écrivez 00**. La LED rouge devrait s'éteindre.
7. Faites de même pour les deux autres caractéristiques. Nous avons maintenant un contrôle total de la LED RGB via Bluetooth Low Energy !

## Étape 3 : Partage via Mesh

Enfin, maintenant que nous recevons avec succès les messages BLE, il est temps de les transférer à notre réseau mesh.

### Écrire le code

1. Tout d'abord, supprimons le mode MANUAL. Commentez `SYSTEM_MODE(MANUAL);`
2. En haut du fichier, ajoutons une variable que nous utiliserons pour suivre si nous devons publier

        // Suivi de quand publier vers Mesh
        static bool m_publish;

3. Ensuite, initialisez-la dans `Setup()`

        // Définir à false au début
        m_publish = false;

4. Ensuite, après avoir défini la LED RGB dans le rappel `onDataReceived`, définissons-la à true :

        // Définir la couleur RGB
        RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

        // Définir pour publier
        m_publish = true;

5. Ajoutons une condition dans la fonction `loop()`. Cela nous amènera à publier l'état de la LED sur le réseau Mesh :

        if( m_publish ) {
        	// Réinitialiser le drapeau
        	m_publish = false;

        	// Publier sur Mesh
          Mesh.publish("red", String::format("%d", m_led_level.red));
          Mesh.publish("green", String::format("%d", m_led_level.green));
          Mesh.publish("blue", String::format("%d", m_led_level.blue));
        }

    `Mesh.publish` nécessite une chaîne pour les deux entrées. Ainsi, nous utilisons `String::format` pour créer une chaîne avec nos valeurs rouge, verte et bleue.

6. Ensuite, abonnons-nous aux mêmes variables dans `Setup()`. Ainsi, un autre appareil peut faire en sorte que la LED de cet appareil se mette à jour également.

        Mesh.subscribe("red", meshHandler);
        Mesh.subscribe("green", meshHandler);
        Mesh.subscribe("blue", meshHandler);

7. Vers le haut du fichier, nous voulons créer `meshHandler`

        // Gestionnaire d'événements Mesh
        static void meshHandler(const char *event, const char *data)
        {
        }

8. Dans cette application, nous avons besoin du paramètre `event` et du paramètre `data`. Afin de les utiliser, nous devons les convertir en type `String`. Ainsi, nous pouvons utiliser les fonctions de conversion et de comparaison intégrées. Donc, à l'intérieur de la fonction `meshHandler`, ajoutez :

          // Convertir en String pour les fonctions de conversion et de comparaison utiles
          String eventString = String(event);
          String dataString = String(data);

9. Enfin, nous faisons quelques comparaisons. Nous vérifions d'abord si le nom de l'événement correspond. Ensuite, nous définissons la valeur de `dataString` au niveau de LED correspondant.

          // Déterminer quel événement nous avons reçu
          if( eventString.equals("red") ) {
            m_led_level.red = dataString.toInt();
          } else if ( eventString.equals("green") ) {
            m_led_level.green = dataString.toInt();
          } else if ( eventString.equals("blue") ) {
            m_led_level.blue = dataString.toInt();
          } else {
        		return;
        	}

          // Définir la couleur RGB
          RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

    Ensuite, à la fin, nous définissons la nouvelle couleur RGB. Remarquez comment je gère un état inconnu en ajoutant une instruction `return` dans la section `else`. Il est toujours bon de filtrer les conditions d'erreur avant qu'elles ne causent des ravages !

### Tester le code

1. Ouvrez l'application Particle sur votre téléphone
2. Configurons d'abord l'Argon. **Si elle ne clignote pas en bleu, maintenez le bouton mode enfoncé jusqu'à ce qu'elle clignote en bleu.**

    ![Particle Argon avec LED bleue](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_1216-f78725ab-a9f5-4270-b389-73d6dddb1f62.jpg)

    Note : si vous avez déjà programmé l'application, la LED sera éteinte par défaut. **Maintenez le bouton mode enfoncé pendant 5 secondes, puis continuez.**

3. Passez par le processus d'appariement. L'application vous guide à travers toutes les étapes. **Assurez-vous de vous souvenir du mot de passe Admin pour votre réseau mesh.**

    ![Choix de la carte de configuration de l'application Particle](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2194-2482aa12-082c-4786-8883-860b50b4cd53.png)

    ![Scannez l'autocollant](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2195-2d030603-e59f-4e76-9d1a-9d4f2c078a4e.png)

    ![Appariement avec votre Argon](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2198-80bb83d8-818b-4cd8-a583-9262da9b5121.png)

    ![Entrez le mot de passe wifi](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2199-e3c107dd-2704-4aa3-9781-550ad14ea7fc.png)

4. Programmez un Argon avec le dernier firmware (1.3.0) (voir **Étape 1 - Temps de tester - Étape 2** pour un rappel sur la façon de faire cela)
5. Une fois qu'il clignote rapidement en jaune, programmez l'Argon avec l'application Tinker. Vous pouvez la télécharger sur la [page de sortie](https://github.com/particle-iot/device-os/releases/tag/v1.3.0-rc.1).
6. Une fois que nous avons une belle LED Cyan solide (connectée au Particle Cloud), nous programmerons l'application. Utilisez l'option **Cloud Flash** dans le menu déroulant.

    ![Option Cloud Flash](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-15_at_9-a50458b1-ade1-4d4d-818b-ef214f3fec5d.55.19_AM.png)

    Dans la mesure où je peux le dire, Particle force tout appareil flashé localement en mode sécurisé lors de la connexion au cloud. Cela peut être dû à ma configuration. Votre expérience peut varier. Il est préférable d'utiliser **Cloud Flash**.

    Assurez-vous de sélectionner la bonne version de deviceOS (**1.3.0-rc1**), le type d'appareil (**Argon**) et le nom de l'appareil (**Ce que vous l'avez nommé pendant la configuration**)

7. Connectez-vous au Xenon en utilisant l'**application téléphone**
8. Connectez le Xenon à votre réseau Mesh en utilisant l'application téléphone
9. Flashez votre Xenon en utilisant **Cloud Flash**. Utilisez le nom que vous lui avez donné pendant la configuration de l'application téléphone. Tant que l'appareil est connecté au Particle Cloud ou en mode sécurisé (LED Pourpre), il devrait se programmer.

    ![Confirmez le type de carte, la version de deviceOS et le nom de l'appareil](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-15_at_10-2f76843b-3cee-4818-adfb-7ece4173df2d.06.32_AM.png)

    ![Option de flash cloud](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/Screen_Shot_2019-07-15_at_10-8e140009-440c-480d-838e-b83c782a8c96.08.47_AM.png)

10. Une fois connecté, passons à la partie amusante. Ouvrez **Light Blue Explorer.** Connectez-vous soit à l'**Argon**, soit au **Xenon**.

    ![Sélectionnez soit l'Argon soit le Xenon](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_2200-e1c513ba-6689-4652-b442-e5c6f916d619.png)

11. Sélectionnez l'une des caractéristiques de la LED et changez la valeur.

    ![Argon et Xenon avec les LEDs rouges allumées](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/images/IMG_0627-2db8ab26-99e1-46a2-9583-97126fbe2594.jpg)

    La LED devrait changer sur tous les appareils !

## Code final

Voici le code final avec toutes les pièces assemblées. Vous pouvez utiliser cela pour vous assurer que vous les avez placées au bon endroit !!

    /*
     * Projet ble_mesh
     * Description : Exemple Bluetooth Low Energy + Mesh
     * Auteur : Jared Wolff
     * Date : 13/07/2019
     */

    //SYSTEM_MODE(MANUAL);

    // UUIDs pour le service + caractéristiques
    const char* serviceUuid = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E";
    const char* red         = "6E400002-B5A3-F393-E0A9-E50E24DCCA9E";
    const char* green       = "6E400003-B5A3-F393-E0A9-E50E24DCCA9E";
    const char* blue        = "6E400004-B5A3-F393-E0A9-E50E24DCCA9E";

    // Définir le service BLE RGB
    BleUuid rgbService(serviceUuid);

    // Variables pour conserver l'état
    typedef struct {
      uint8_t red;
      uint8_t green;
      uint8_t blue;
    } led_level_t;

    // Suivi de niveau statique
    static led_level_t m_led_level;

    // Suivi de quand publier vers Mesh
    static bool m_publish;

    // Gestionnaire d'événements Mesh
    static void meshHandler(const char *event, const char *data)
    {

      // Convertir en String pour les fonctions de conversion et de comparaison utiles
      String eventString = String(event);
      String dataString = String(data);

      // Déterminer quel événement nous avons reçu
      if( eventString.equals("red") ) {
        m_led_level.red = dataString.toInt();
      } else if ( eventString.equals("green") ) {
        m_led_level.green = dataString.toInt();
      } else if ( eventString.equals("blue") ) {
        m_led_level.blue = dataString.toInt();
      } else {
    		return;
    	}

      // Définir la couleur RGB
      RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

    }

    // Fonction statique pour gérer les rappels Bluetooth Low Energy
    static void onDataReceived(const uint8_t* data, size_t len, const BlePeerDevice& peer, void* context) {

      // Nous ne cherchons qu'un seul octet
      if( len != 1 ) {
        return;
      }

      // Définit le niveau global
      if( context == red ) {
        m_led_level.red = data[0];
      } else if ( context == green ) {
        m_led_level.green = data[0];
      } else if ( context == blue ) {
        m_led_level.blue = data[0];
      }

      // Définir la couleur RGB
      RGB.color(m_led_level.red, m_led_level.green, m_led_level.blue);

      // Définir pour publier
      m_publish = true;

    }

    // setup() s'exécute une fois, lorsque l'appareil est allumé pour la première fois.
    void setup() {

      // Activer le contrôle de l'application sur la LED
      RGB.control(true);

      // Init niveau par défaut
      m_led_level.red = 0;
      m_led_level.green = 0;
      m_led_level.blue = 0;

      // Définir à false au début
      m_publish = false;

      // Définir l'abonnement pour les mises à jour Mesh
      Mesh.subscribe("red",meshHandler);
      Mesh.subscribe("green",meshHandler);
      Mesh.subscribe("blue",meshHandler);

      // Configurer les caractéristiques
      BleCharacteristic redCharacteristic("red", BleCharacteristicProperty::WRITE_WO_RSP, red, serviceUuid, onDataReceived, (void*)red);
      BleCharacteristic greenCharacteristic("green", BleCharacteristicProperty::WRITE_WO_RSP, green, serviceUuid, onDataReceived, (void*)green);
      BleCharacteristic blueCharacteristic("blue", BleCharacteristicProperty::WRITE_WO_RSP, blue, serviceUuid, onDataReceived, (void*)blue);

      // Ajouter les caractéristiques
      BLE.addCharacteristic(redCharacteristic);
      BLE.addCharacteristic(greenCharacteristic);
      BLE.addCharacteristic(blueCharacteristic);

      // Données de publicité
      BleAdvertisingData advData;

      // Ajouter le service LED RGB
      advData.appendServiceUUID(rgbService);

      // Commencer la publicité !
      BLE.advertise(&advData);
    }

    // loop() s'exécute encore et encore, aussi rapidement qu'il peut s'exécuter.
    void loop() {

      // Vérifie le drapeau de publication,
      // Publie dans une variable appelée "red" "green" et "blue"
      if( m_publish ) {

        // Réinitialiser le drapeau
        m_publish = false;

        // Publier sur Mesh
        Mesh.publish("red", String::format("%d", m_led_level.red));
        Mesh.publish("green", String::format("%d", m_led_level.green));
        Mesh.publish("blue", String::format("%d", m_led_level.blue));
      }

    }

## Conclusion

Dans ce tutoriel, vous avez appris comment ajouter Bluetooth à un projet Particle Mesh. Comme vous pouvez l'imaginer, les possibilités sont infinies. Par exemple, vous pouvez ajouter des applications utilisateur/administrateur à l'expérience. *C'est génial.* ?

Vous pouvez vous attendre à plus de contenu comme celui-ci dans mon prochain livre : ***Le Guide Ultime de Particle Mesh***. Abonnez-vous à ma liste pour des mises à jour et du contenu exclusif. De plus, tous les premiers abonnés bénéficient d'une réduction lors de sa sortie ! [Cliquez ici pour vous inscrire.](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh)