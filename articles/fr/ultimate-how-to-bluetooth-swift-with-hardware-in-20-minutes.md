---
title: 'Le guide ultime : Créer une application Bluetooth Swift avec du matériel en
  20 minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-13T14:15:00.000Z'
originalURL: https://freecodecamp.org/news/ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/main.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: iOS
  slug: ios
- name: particle
  slug: particle
- name: Swift
  slug: swift
- name: Swift Programming
  slug: swift-programming
seo_title: 'Le guide ultime : Créer une application Bluetooth Swift avec du matériel
  en 20 minutes'
seo_desc: 'By Jared Wolff

  In a previous tutorial, you learned how to add Bluetooth to a Particle Xenon application.
  That way you could control the onboard RGB LED from a test app like nRF Connect
  or Light Blue Explorer.

  In this post, we''re going to take it one ...'
---

Par Jared Wolff

Dans un [tutoriel précédent](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/), vous avez appris comment ajouter le Bluetooth à une application Particle Xenon. Ainsi, vous pouviez contrôler la LED RGB intégrée à partir d'une application de test comme nRF Connect ou Light Blue Explorer.

Dans cet article, nous allons aller plus loin. Nous allons développer une application Swift pour contrôler une LED RGB Particle Mesh. Si tout se passe bien, vous devriez avoir une application fonctionnelle en environ 20 minutes !

Commençons.

### Vous n'avez pas le temps de lire l'article complet ?

[Téléchargez la version PDF ici.](https://www.jaredwolff.com/files/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/)

## Installation

* Installez Xcode. [Vous pouvez le télécharger depuis l'App Store ici.](https://developer.apple.com/xcode/resources/)
* Vous aurez également besoin d'un identifiant Apple. J'utilise mon email iCloud. Vous pouvez créer un nouveau compte dans Xcode si vous n'en avez pas encore.
* Installez le [code exemple RGB](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/#final-code) sur une carte Particle Mesh.

## Créer le projet

Une fois tout installé, passons aux choses sérieuses !

Ouvrez Xcode et allez dans **Fichier → Nouveau Projet.**

![Nouveau Projet Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_3-7ef4de80-050c-4fc3-9cf2-8581e16ffe18.10.57_PM.png)

Sélectionnez **Application à Vue Unique.**

![Informations du Nouveau Projet](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_3-ef953954-312b-4320-be30-5da186d0902e.11.14_PM.png)

Ensuite, mettez à jour le **Nom du Projet** selon vos préférences. J'ai également changé mon identifiant d'organisation en `com.jaredwolff`. Modifiez-le comme vous le souhaitez !

Sélectionnez un emplacement pour l'enregistrer.

Ensuite, trouvez votre **Info.plist.**

![Info.plist dans Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_3-27439ca7-68c5-4890-902d-6c2ee7f31829.13.26_PM.png)

Mettez à jour `info.plist` en ajoutant `Privacy - Bluetooth Peripheral Usage Description`

La description que j'ai utilisée est `L'application utilise le Bluetooth pour se connecter à l'exemple RGB Particle Xenon`

Cela vous permet d'utiliser le Bluetooth dans votre application si vous souhaitez un jour la publier.

Maintenant, rendons tout cela minimalement fonctionnel !

## Minimalement fonctionnel

![Nouvelle image de section](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Copy_of_Flow-5e62bf38-b399-4bca-9b5b-c63f9716af33.jpg)

Ensuite, nous allons obtenir une application minimalement fonctionnelle pour se connecter et effectuer une découverte de services. La plupart de l'action se déroulera dans le `ViewController.swift`.

Commençons par importer `CoreBluetooth`

```swift
    import CoreBluetooth

```

Cela nous permet de contrôler la fonctionnalité Bluetooth Low Energy dans iOS. Ensuite, ajoutons à la fois `CBPeripheralDelegate` et `CBCentralManagerDelegate` à la classe `ViewController`.

```swift
    class ViewController: UIViewController, CBPeripheralDelegate, CBCentralManagerDelegate {

```

Créons maintenant des variables locales privées pour stocker le gestionnaire central et le périphérique. Nous les configurerons plus en détail sous peu.

```swift
    // Propriétés
    private var centralManager: CBCentralManager!
    private var peripheral: CBPeripheral!

```

Dans votre fonction `viewDidLoad`, initialisons le `centralManager`

```swift
    centralManager = CBCentralManager(delegate: self, queue: nil)

```

Définir `delegate: self` est important. Sinon, l'état central ne change jamais au démarrage.

Avant d'aller plus loin, créons un fichier séparé et appelons-le `ParticlePeripheral.swift`. Il peut être placé n'importe où, mais je l'ai placé dans un groupe séparé appelé **Modèles** pour plus tard.

À l'intérieur, nous allons créer quelques variables publiques qui contiennent les UUID pour notre carte Particle. Ils devraient vous être familiers !

```swift
    import UIKit
    import CoreBluetooth

    class ParticlePeripheral: NSObject {

        /// MARK: - Identifiants des services et caractéristiques de la LED Particle

        public static let particleLEDServiceUUID     = CBUUID.init(string: "b4250400-fb4b-4746-b2b0-93f0e61122c6")
        public static let redLEDCharacteristicUUID   = CBUUID.init(string: "b4250401-fb4b-4746-b2b0-93f0e61122c6")
        public static let greenLEDCharacteristicUUID = CBUUID.init(string: "b4250402-fb4b-4746-b2b0-93f0e61122c6")
        public static let blueLEDCharacteristicUUID  = CBUUID.init(string: "b4250403-fb4b-4746-b2b0-93f0e61122c6")

    }

```

De retour dans `ViewController.swift`, assemblons les éléments Bluetooth.

### Éléments Bluetooth

![Diagramme de flux pour Bluetooth Swift dans iOS](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Flow-3cb1d250-f9d5-4757-a244-be29bed9dcf6.jpg)

Tout ce qui concerne Bluetooth est basé sur des événements. Nous allons définir plusieurs fonctions qui gèrent ces événements. Voici les plus importantes :

`centralManagerDidUpdateState` est mis à jour lorsque le périphérique Bluetooth est activé ou désactivé. Il se déclenche lorsque l'application démarre pour la première fois, afin que vous connaissiez l'état du Bluetooth. Nous commençons également le scan ici.

L'événement `centralManager` `didDiscover` se produit lorsque vous recevez des résultats de scan. Nous allons utiliser cela pour démarrer une connexion.

L'événement `centralManager` `didConnect` se déclenche une fois que le périphérique est connecté. Nous allons démarrer la découverte du périphérique ici. **Note :** La découverte du périphérique est le moyen par lequel nous déterminons quels services et caractéristiques sont disponibles. C'est un bon moyen de confirmer à quel type de périphérique nous sommes connectés.

L'événement `peripheral` `didDiscoverServices` se déclenche une fois que tous les services ont été découverts. Remarquez que nous sommes passés de `centralManager` à `peripheral` maintenant que nous sommes connectés. Nous allons démarrer la découverte des caractéristiques ici. Nous allons utiliser l'UUID du service RGB comme cible.

L'événement `peripheral` `didDiscoverCharacteristicsFor` fournira toutes les caractéristiques en utilisant l'UUID du service fourni. C'est la dernière étape de la chaîne pour effectuer une découverte complète du périphérique. C'est compliqué, mais cela ne doit être fait qu'une seule fois pendant la phase de connexion !

### Définition de toutes les fonctions Bluetooth.

Maintenant que nous connaissons les événements des fonctions qui sont déclenchés. Nous allons les définir dans l'ordre logique dans lequel ils se produisent pendant un cycle de connexion.

Tout d'abord, nous allons définir `centralManagerDidUpdateState` pour commencer à scanner un périphérique avec notre service Particle RGB LED. Si le Bluetooth n'est pas activé, il ne fera rien.

```swift
    // Si nous sommes sous tension, commençons le scan
        func centralManagerDidUpdateState(_ central: CBCentralManager) {
            print("Mise à jour de l'état central")
            if central.state != .poweredOn {
                print("Le central n'est pas sous tension")
            } else {
                print("Scan central pour", ParticlePeripheral.particleLEDServiceUUID);
                centralManager.scanForPeripherals(withServices: [ParticlePeripheral.particleLEDServiceUUID],
                                                  options: [CBCentralManagerScanOptionAllowDuplicatesKey : true])
            }
        }

```

Définir le `centralManager` `didDiscover` est notre prochaine étape dans le processus. Nous savons que nous avons trouvé un périphérique si cet événement s'est produit.

```swift
    // Gère le résultat du scan
        func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {

            // Nous l'avons trouvé, donc arrêtons le scan
            self.centralManager.stopScan()

            // Copiez l'instance du périphérique
            self.peripheral = peripheral
            self.peripheral.delegate = self

            // Connectez-vous !
            self.centralManager.connect(self.peripheral, options: nil)

        }

```

Ainsi, nous arrêtons le scan en utilisant `self.centralManager.stopScan()`. Nous définissons le `peripheral` pour qu'il persiste à travers l'application. Ensuite, nous nous connectons à ce périphérique en utilisant `self.centralManager.connect`

Une fois connecté, nous devons vérifier si nous travaillons avec le bon périphérique.

```swift
    // Le gestionnaire si nous nous connectons avec succès
        func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
            if peripheral == self.peripheral {
                print("Connecté à votre carte Particle")
                peripheral.discoverServices([ParticlePeripheral.particleLEDServiceUUID])
            }
        }

```

En comparant les deux périphériques, nous saurons qu'il s'agit du périphérique que nous avons trouvé précédemment. Nous lancerons une découverte de services en utilisant `peripheral.discoverService`. Nous pouvons utiliser `ParticlePeripheral.particleLEDServiceUUID` comme paramètre. Ainsi, nous ne captons pas les services qui ne nous intéressent pas.

Une fois que nous avons terminé la découverte des services, nous recevrons un événement `didDiscoverServices`. Nous itérons à travers tous les services "disponibles". (Bien qu'il n'y en aura qu'un !)

```swift
    // Gère l'événement de découverte
        func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
            if let services = peripheral.services {
                for service in services {
                    if service.uuid == ParticlePeripheral.particleLEDServiceUUID {
                        print("Service LED trouvé")
                        // Maintenant, lancez la découverte des caractéristiques
                        peripheral.discoverCharacteristics([ParticlePeripheral.redLEDCharacteristicUUID,
                                                                 ParticlePeripheral.greenLEDCharacteristicUUID,
                                                                 ParticlePeripheral.blueLEDCharacteristicUUID], for: service)
                        return
                    }
                }
            }
        }

```

À ce stade, c'est la troisième fois que nous vérifions que nous avons le bon service. Cela devient plus utile plus tard lorsqu'il y a de nombreuses caractéristiques et de nombreux services.

Nous appelons `peripheral.discoverCharacteristics` avec un tableau d'UUID pour les caractéristiques que nous recherchons. Ce sont tous les UUID que nous avons définis dans `ParticlePeripheral.swift`.

Enfin, nous gérons l'événement `didDiscoverCharacteriscsFor`. Nous itérons à travers toutes les caractéristiques disponibles. Au fur et à mesure que nous itérons, nous comparons avec celles que nous recherchons.

```swift
    // Gestion de la découverte des caractéristiques
        func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
            if let characteristics = service.characteristics {
                for characteristic in characteristics {
                    if characteristic.uuid == ParticlePeripheral.redLEDCharacteristicUUID {
                        print("Caractéristique LED rouge trouvée")
                    } else if characteristic.uuid == ParticlePeripheral.greenLEDCharacteristicUUID {
                        print("Caractéristique LED verte trouvée")
                    } else if characteristic.uuid == ParticlePeripheral.blueLEDCharacteristicUUID {
                        print("Caractéristique LED bleue trouvée");
                    }
                }
            }
        }

```

À ce stade, nous sommes prêts à effectuer une découverte complète du périphérique Particle Mesh. Dans la section suivante, nous testerons ce que nous avons pour nous assurer que tout fonctionne correctement.

## Tester notre exemple minimal

![Image de section sur les tests](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Flow-6-744bf855-fd7c-403b-b07f-dfc0c191b6af.jpg)

Avant de commencer, si vous rencontrez des problèmes, j'ai mis quelques étapes de dépannage dans les [notes de bas de page](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/#troubleshooting).

**Pour tester, vous devez avoir un iPhone avec Bluetooth Low Energy.** La plupart des iPhones modernes en sont équipés. Le dernier iPhone à ne pas en avoir, je crois, était soit l'iPhone 4 ou le 3Gs. (donc vous êtes probablement bon)

Tout d'abord, branchez-le à votre ordinateur.

Allez en haut près des boutons de lecture et d'arrêt. Sélectionnez votre appareil cible. Dans mon cas, j'ai choisi mon téléphone (**iPhone de Jared**). Vous pouvez également utiliser un iPad.

![Sélectionner le type d'appareil](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-09_at_4-d04de709-6000-4161-bd12-7347a70d6e1e.37.27_PM.png)

Ensuite, vous pouvez appuyer sur **Command + R** ou sur le bouton **Lecture** pour charger l'application sur votre téléphone.

Assurez-vous d'avoir votre onglet de journal ouvert. Activez-le en cliquant sur le bouton du panneau inférieur dans le coin supérieur droit.

![Panneau inférieur dans Xcode pour les journaux](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-09_at_4-8b83ea0a-274f-4a41-a5ff-e80717b41977.38.57_PM.png)

Assurez-vous d'avoir un appareil mesh configuré et exécutant le code exemple. Vous pouvez vous rendre sur [cette page](https://www.jaredwolff.com/how-to-use-particles-powerful-bluetooth-api/#final-code) pour l'obtenir. N'oubliez pas que votre carte Particle Mesh doit exécuter le système d'exploitation de l'appareil 1.3.0 ou supérieur pour que le Bluetooth fonctionne !

Une fois que le firmware et l'application sont chargés, vérifions la sortie du journal.

Cela devrait ressembler à ceci :

```
Vue chargée
Mise à jour de l'état central
Scan central pour B4250400-FB4B-4746-B2B0-93F0E61122C6
Connecté à votre carte Particle
Service LED trouvé
Caractéristique LED rouge trouvée
Caractéristique LED verte trouvée
Caractéristique LED bleue trouvée

```

Cela signifie que votre téléphone s'est connecté et a trouvé le service LED ! La découverte des caractéristiques est également importante ici. Sans celles-ci, nous ne pourrions pas envoyer de données à l'appareil mesh.

L'étape suivante consiste à créer des curseurs afin que nous puissions mettre à jour les valeurs RGB à la volée.

## Glissez vers la gauche. Glissez vers la droite.

Ensuite, nous allons ajouter quelques éléments à notre `Main.storyboard`. Ouvrez `Main.storyboard` et cliquez sur la **Vue** sous **View Controller.**

![Mise à jour de la vue dans Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-7919e3c2-cb72-4297-b9e0-06139a064fec.57.37_PM.png)

Ensuite, cliquez sur le bouton **Bibliothèque**. (Il ressemble à l'ancienne art d'Apple utilisé pour le bouton d'accueil)

![Bouton Bibliothèque dans Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-895d247a-6706-4c39-be04-0bda41195ca6.58.02_PM.png)

Vous obtiendrez une fenêtre contextuelle avec tous les choix que vous pouvez insérer dans votre application.

![Panneau Bibliothèque dans Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-8b531053-621e-4c14-8086-2ac0ef6e52de.58.31_PM.png)

Faites glisser trois **Labels** et copiez trois **Sliders** dans votre vue.

![Glisser les Labels vers la Vue Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-9c8c6167-2279-4cb7-a37b-c24b8cdd275d.59.39_PM.png)

Vous pouvez double-cliquer sur les labels et les renommer au fur et à mesure.

![Glisser le Slider vers la Vue Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_1-72573a66-1201-4d08-902d-ea905c91b2bb.59.57_PM.png)

Si vous cliquez et maintenez, des outils d'alignement pratiques apparaîtront. Ils s'aligneront même au centre !

![Outils d'alignement dans Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-4c7b1627-c55e-4eba-b29a-32915ba41867.00.17_PM.png)

Vous pouvez également les sélectionner tous et les déplacer ensemble. Nous allons les aligner verticalement et horizontalement.

Pour qu'ils restent au milieu, supprimons la propriété de redimensionnement automatique. Cliquez sur l'**icône Règle** en haut à droite. Ensuite, cliquez sur chacune des **barres rouges**. Cela garantira que vos labels et curseurs restent à l'écran !

![Panneau Règle dans Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-f207fae8-7292-4e38-9985-c97444ab4e55.09.39_PM.png)

Ensuite, cliquons sur le bouton **Afficher l'éditeur assistant**. (Ressemble à un diagramme de Venn)

![Bouton Afficher l'éditeur assistant dans Xcode](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-c52c52b8-70b3-426b-9cbe-9df1042f5fb1.00.59_PM.png)

**Note :** assurez-vous que **ViewController.swift** est ouvert dans votre éditeur assistant.

![Option automatique dans l'éditeur assistant](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-655a4468-4da8-4841-a2dc-1cf8706592e7.17.35_PM.png)

Ensuite, sous la section `/properties`, **Contrôle-cliquez et faites glisser** **le curseur rouge** dans votre code.

![Glisser le curseur vers le code](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-39480e58-fd92-4ec7-a2db-9e8524019755.01.43_PM.png)

Répétez avec tous les autres. Assurez-vous de leur donner des noms différents. Votre code devrait ressembler à ceci lorsque vous aurez terminé :

```swift
        // Propriétés
        private var centralManager: CBCentralManager!
        private var peripheral: CBPeripheral!

        // Curseurs
        @IBOutlet weak var redSlider: UISlider!
        @IBOutlet weak var greenSlider: UISlider!
        @IBOutlet weak var blueSlider: UISlider!

```

Cela nous permet d'accéder à la valeur des curseurs.

Ensuite, attachons l'événement **Value Changed** à chacun des curseurs. **Cliquez avec le bouton droit** sur le **curseur rouge dans la vue du dossier.**

![Glisser l'événement value changed vers le code](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-b2ffe0a6-709e-433d-9d4c-0f8028bd096c.03.44_PM.png)

Il devrait vous donner quelques options pour les événements. Cliquez et faites glisser l'événement **Value Changed** vers votre code. Assurez-vous de lui donner un nom qui a du sens. J'ai utilisé **RedSliderChanged** pour le curseur rouge.

Répétez deux fois de plus. Votre code devrait ressembler à ceci à la fin de cette étape :

```swift
        @IBAction func RedSliderChanged(_ sender: Any) {
        }

        @IBAction func GreenSliderChanged(_ sender: Any) {
        }

        @IBAction func BlueSliderChanged(_ sender: Any) {
        }

```

J'ai également sélectionné chacun des curseurs et **désactivé l'option Activé**. Ainsi, vous ne pouvez pas les déplacer. Nous les activerons plus tard dans le code.

![Désactiver le curseur par défaut](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-e7e0aca9-224c-4bfb-b482-1d9e58b37947.21.21_PM.png)

De plus, c'est le moment idéal pour changer la **valeur maximale à 255**. Définissez également la valeur par défaut **de 0,5 à 0.**

![Définir la valeur par défaut et la valeur maximale du curseur](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Screen_Shot_2019-08-11_at_2-9bf5618b-f6ac-4aea-9888-7f93a8c75414.55.38_PM.png)

En haut du fichier, créons quelques variables locales pour chacune des caractéristiques. Nous les utiliserons pour écrire les valeurs des curseurs sur la carte Particle Mesh.

```swift
        // Caractéristiques
        private var redChar: CBCharacteristic?
        private var greenChar: CBCharacteristic?
        private var blueChar: CBCharacteristic?

```

Maintenant, attachons tout ensemble !

Dans la fonction de rappel `didDiscoverCharacteristicsFor`, attribuons ces caractéristiques. Par exemple :

```swift
    if characteristic.uuid == ParticlePeripheral.redLEDCharacteristicUUID {
        print("Caractéristique LED rouge trouvée")
        redChar = characteristic

```

Au fur et à mesure que nous trouvons chaque caractéristique, nous pouvons également activer chacun des curseurs au même endroit.

```swift
    		// Activer le curseur rouge
    		redSlider.isEnabled = true

```

À la fin, votre `didDiscoverCharacteristicsFor` devrait ressembler à ceci :

```swift
    // Gestion de la découverte des caractéristiques
        func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
            if let characteristics = service.characteristics {
                for characteristic in characteristics {
                    if characteristic.uuid == ParticlePeripheral.redLEDCharacteristicUUID {
                        print("Caractéristique LED rouge trouvée")

                        redChar = characteristic
                        redSlider.isEnabled = true
                    } else if characteristic.uuid == ParticlePeripheral.greenLEDCharacteristicUUID {
                        print("Caractéristique LED verte trouvée")

                        greenChar = characteristic
                        greenSlider.isEnabled = true
                    } else if characteristic.uuid == ParticlePeripheral.blueLEDCharacteristicUUID {
                        print("Caractéristique LED bleue trouvée")

                        blueChar = characteristic
                        blueSlider.isEnabled = true
                    }
                }
            }
        }

```

Maintenant, mettons à jour les fonctions `RedSliderChanged`, `GreenSliderChanged` et `BlueSliderChanged`. Ce que nous voulons faire ici, c'est mettre à jour la caractéristique associée à la fonction `Changed`. J'ai créé une fonction séparée appelée `writeLEDValueToChar`. Nous allons passer la caractéristique et les données.

```swift
    private func writeLEDValueToChar( withCharacteristic characteristic: CBCharacteristic, withValue value: Data) {

            // Vérifier si elle a la propriété d'écriture
            if characteristic.properties.contains(.writeWithoutResponse) && peripheral != nil {

                peripheral.writeValue(value, for: characteristic, type: .withoutResponse)

            }

        }

```

Maintenant, ajoutez un appel à `writeLEDValueToChar` à chacune des fonctions `Changed`. Vous devrez convertir la valeur en `Uint8`. (L'appareil Particle Mesh attend un nombre non signé sur 8 bits.)

```swift
    		@IBAction func RedSliderChanged(_ sender: Any) {
            print("rouge:",redSlider.value);
            let slider:UInt8 = UInt8(redSlider.value)
            writeLEDValueToChar( withCharacteristic: redChar!, withValue: Data([slider]))

        }

```

Répétez cela pour `GreenSliderChanged` et `BlueSliderChanged`. Assurez-vous de changer `red` en `green` et `blue` pour chacun !

Enfin, pour garder les choses propres, j'ai également ajouté une fonction qui gère les déconnexions Bluetooth.

```swift
    func centralManager(_ central: CBCentralManager, didDisconnectPeripheral peripheral: CBPeripheral, error: Error?) {

```

À l'intérieur, nous devons réinitialiser l'état des curseurs à 0 et les désactiver.

```swift
            if peripheral == self.peripheral {
                print("Déconnecté")

                redSlider.isEnabled = false
                greenSlider.isEnabled = false
                blueSlider.isEnabled = false

                redSlider.value = 0
                greenSlider.value = 0
                blueSlider.value = 0

```

Il est bon de réinitialiser `self.peripheral` à nil pour ne pas essayer d'écrire sur un appareil fantôme.

```swift
                self.peripheral = nil

```

Enfin, parce que nous avons été déconnectés, recommencez à scanner !

```swift
                // Commencez à scanner à nouveau
                print("Scan central pour", ParticlePeripheral.particleLEDServiceUUID);
                centralManager.scanForPeripherals(withServices: [ParticlePeripheral.particleLEDServiceUUID],
                                                  options: [CBCentralManagerScanOptionAllowDuplicatesKey : true])
            }

```

D'accord ! Nous sommes presque prêts à tester. Passons à l'étape suivante (et finale).

## Testez les curseurs.

![Prochaine section de test !](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/Flow-5-3af7db2e-8bf7-4561-98c2-a1b7ab0c685b.jpg)

Le travail difficile est terminé. Maintenant, c'est le moment de jouer !

Le moyen le plus simple de tout tester est de **cliquer sur le bouton Lecture** en haut à gauche ou d'utiliser le raccourci clavier **Command + R**. Xcode chargera l'application sur votre téléphone. Vous devriez voir un écran blanc suivi d'un écran avec vos curseurs !

Les curseurs doivent rester grisés jusqu'à ce qu'ils soient connectés à votre carte Particle Mesh. Vous pouvez vérifier la sortie du journal si la connexion a été établie.

```
Vue chargée
Mise à jour de l'état central
Scan central pour B4250400-FB4B-4746-B2B0-93F0E61122C6
Connecté à votre carte Particle
Service LED trouvé
Caractéristique LED rouge trouvée
Caractéristique LED verte trouvée
Caractéristique LED bleue trouvée

```

(Ça vous dit quelque chose ? Nous sommes connectés !)

Si vous avez suivi tout à la perfection, vous devriez pouvoir déplacer les curseurs. Mieux encore, la LED RGB sur la carte Particle Mesh devrait changer de couleur.

![Résultats finaux des tests](https://www.jaredwolff.com/the-ultimate-how-to-bluetooth-swift-with-hardware-in-20-minutes/images/DSC01556-1fda5018-f1f5-4855-8705-f7d344ce3d78.jpeg)

## Conclusion

Dans cet article, vous avez appris comment connecter votre carte Particle Mesh et votre appareil iOS via Bluetooth. Nous avons appris comment nous connecter à chacune des caractéristiques disponibles. De plus, par-dessus tout, créer une interface propre pour tout faire.

Comme vous pouvez l'imaginer, vous pouvez descendre dans le terrier du lapin avec Bluetooth sur iOS. Il y a plus à venir dans mon prochain guide : **Le Guide Ultime de Particle Mesh.** Les abonnés à ma liste obtiennent un accès au contenu pré-lancement et une réduction à sa sortie ! [Cliquez ici pour vous inscrire.](https://www.jaredwolff.com/the-ultimate-guide-to-particle-mesh/)

## Code

Le code source complet est disponible sur [Github.](https://github.com/jaredwolff/swift-bluetooth-particle-rgb) Si vous le trouvez utile, cliquez sur le bouton étoile. ⭐️