---
title: Comment utiliser Protocol Buffer avec un service Bluetooth Low Energy - Partie
  3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T16:02:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-protocol-buffer-bluetooth-low-energy-service-part-3
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Protocol-Buffers-Part-2-2.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: protocol-buffers
  slug: protocol-buffers
- name: Tutorial
  slug: tutorial
seo_title: Comment utiliser Protocol Buffer avec un service Bluetooth Low Energy -
  Partie 3
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  In Part 1 we’ve learned the anatomy of a Protocol Buffer. In Part 2 we’ve learned
  how a Bluetooth Low Energy Service gets pieced together on the Nordic NRF52 SDK.
  This final post brings t...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/)**

Dans la [Partie 1][part1], nous avons appris l'anatomie d'un Protocol Buffer. Dans la [Partie 2][part2], nous avons vu comment un service Bluetooth Low Energy est assemblé sur le SDK Nordic NRF52. Ce dernier article rassemble tous les éléments dans un exemple fonctionnel de bout en bout.

Commençons !

P.S. : cet article est long. Si vous voulez quelque chose à télécharger, [cliquez ici pour un PDF magnifiquement formaté](https://www.jaredwolff.com/files/how-to-define-a-protocol-buffer-ble-service-pdf/). (Bonus supplémentaire : le PDF contient les trois parties de cette série !)

## Installation

![Attaque d'oie](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-6880beab-c5c2-4184-9012-4a6e68bcebc8.png)

Consultez le fichier `Readme.md` dans chacun des dépôts d'exemples. (Vous devrez cloner les dépôts, [inscrivez-vous ici pour obtenir le code][code]).

J'ai rendu l'installation du firmware très simple. Pour la partie JavaScript, c'est un peu plus complexe mais faisable ! Je vais également inclure les instructions ici :

### Configuration du firmware (pour Mac)

1. Initialisez le dépôt complet (il y a des sous-modules !) : `git submodule update --init`
2. Installez `protoc` en utilisant Homebrew : `brew install protobuf`
3. Exécutez `make sdk`. Cela téléchargera les fichiers du SDK.
4. Exécutez `make tools_osx`. Cela téléchargera votre toolchain ARMGCC (pour Mac). Pour d'autres environnements, voir ci-dessous.
5. Exécutez `make gen_key` une fois (et une seule fois) ! Cela configura votre clé pour le DFU.
6. Exécutez `make` et cela construira votre bootloader et votre application principale.

**Note :** Vous n'avez à faire les étapes 1 à 5 qu'une seule fois.

### Configuration de l'application JavaScript (pour Mac)

**Prérequis :** vous aurez besoin des outils de ligne de commande Xcode. Vous pouvez les obtenir [ici](https://developer.apple.com/download/more/).

1. Clonez ce dépôt à un endroit sur votre ordinateur
2. Assurez-vous d'avoir [nvm installé](https://github.com/nvm-sh/nvm/blob/master/README.md)
3. Exécutez `nvm install v8.0.0`
4. Exécutez `nvm install v10.15.3`
5. Exécutez `nvm use v8.0.0`
6. Exécutez `yarn` (si vous n'avez pas yarn `npm install yarn -g`)
7. Une fois installé, exécutez `nvm use v10.15.3`
8. Ensuite, exécutez `node index.js` pour démarrer l'exemple

L'utilisation de NVM aide à atténuer un problème de compilation avec la bibliothèque Bluetooth. Votre expérience peut varier sur ce point.

## Comment cela fonctionne-t-il ?

Dans ce projet, le Protocol Buffer a deux fonctions. La première en tant que "commande" à l'appareil Bluetooth. Deuxièmement, une "réponse" à cette commande de l'appareil.

Notre exemple d'application JavaScript utilise "This is" comme charge utile. Avec la puissance de certaines opérations sur les chaînes de caractères, faisons-en une phrase complète !

La série d'événements ressemble à ceci :

1. L'application de test se connecte et envoie ces données en utilisant notre service Bluetooth Low Energy.
2. Le firmware décode le message.
3. Le firmware modifie les données originales en ajoutant " cool." Résultat : "This is cool"
4. Le firmware encode la charge utile et rend les données disponibles pour la lecture.
5. L'application lit enfin la caractéristique, décode et affiche le résultat !

Cela semble compliqué, mais il y a des avantages à cela :

1. Dans les Protocol Buffers, les structures de données sont bien définies. Cela signifie qu'ils ont de grandes capacités de vérification des erreurs. Si vous utilisez un type de structure de données, vous devrez peut-être coder votre propre validation de données.
2. L'encodage et le décodage sont simples et directs. Vous pouvez encoder les mêmes données sur différentes plateformes et toujours obtenir le même résultat décodé.

Vous voulez faire fonctionner l'exemple ? Après tout, voir, c'est croire. Faisons cela.

## Cela fonctionne-t-il ?

![Téléphone en main exécutant NRF connect](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-c72fcf71-f0db-49e5-92d7-44fe601e75fa.png)

Une fois que vous avez terminé l'installation (ci-dessus), programmons ce firmware ! Heureusement pour vous, ce n'est que deux étapes rapides !

1. Branchez votre carte NRF52 DK
2. Exécutez `make flash_all`. (Cela compile et flashe *tout* le code du projet.)

Une fois flashé, le moyen le plus simple de savoir si tout fonctionne est lorsque la LED 1 clignote. Cela signifie qu'elle est en mode publicité et prête pour une connexion.

![NRF52 DK](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-6c58e8c5-d005-4b61-a32b-29eea61b1ce7.png)

Assurons-nous qu'elle est bien en mode publicité. Vous pouvez utiliser un outil comme NRF Connect pour [iOS](https://itunes.apple.com/cn/app/nrf-connect/id1054362403?l=en) ou Android. Ou vous pouvez utiliser LightBlue. (Disponible également pour [iOS](https://apps.apple.com/ru/app/lightblue-explorer/id557428110?l=en) et Android)

Ouvrez l'une des applications et recherchez les appareils en mode publicité. Vous chercherez **Nordic_Buttonless**.

![Applications BLE en cours de scan](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-062f5e84-ec22-4525-a591-4330a55fe30f.png)

Maintenant, connectons-nous et vérifions nos services et caractéristiques connectables :

![Applications BLE montrant les services](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-0466566a-1d8a-4e8b-a1c9-f2f76faa116b.png)

Comme vous pouvez le voir, il y a deux services. L'un est le service DFU de Nordic. L'autre est notre service Protocol Buffer !

Vous pouvez comparer `PROTOBUF_UUID_BASE` dans `ble_protobuf.h` avec l'UUID du service "Inconnu". Les puces de Nordic sont en format Little Endian tandis que les données ici sont en format Big Endian. (c'est-à-dire que vous devrez inverser les octets pour voir qu'ils sont identiques !)

Vous pouvez même cliquer pour voir les caractéristiques dans NRF Connect. Dans le cas de LightBlue, les UUID des caractéristiques sont déjà affichés.

## Utilisation de l'application JavaScript

Une fois que nous sommes en mode publicité, il est temps de lancer l'application.

![Résultats de l'application JavaScript Bluetooth](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-7e92193a-4dbe-4e08-9ebe-ee41be501580.png)

Changez simplement de répertoire pour `ble-protobuf-js` et exécutez `node index.js`

Si vous avez tout installé correctement, vous devriez commencer à voir une sortie comme :

    exemple démarré
    scanning
    périphérique avec ID 06f9b62ec5334454875b9f53d2f3fa74 trouvé avec le nom : Nordic_Buttonles

Il devrait ensuite se connecter immédiatement et envoyer des données à l'appareil. Il devrait recevoir la réponse immédiatement et l'afficher à l'écran.

    connecté à Nordic_Buttonles
    Envoyé : This is
    Reçu : This is cool.

Bingo !

## Vous l'avez fait !

? Félicitations si vous êtes arrivé jusqu'ici dans le tutoriel. Vous devriez maintenant vous sentir suffisamment confiant pour commencer à jouer avec le code logiciel. Peut-être allez-vous créer quelque chose de cool ?

Voici des liens vers quelques ressources que vous pourriez trouver utiles.

- [Documentation Protocol Buffer](https://developers.google.com/protocol-buffers)
- [NanoPB](https://www.github.com/nanopb/nanopb) - (l'implémentation des Protocol Buffers que nous avons utilisée pour ce projet)
- [Documentation du SDK Nordic](https://www.nordicsemi.com/DocLib/Content/SDK_Doc/nRF5_SDK/v15-2-0/index)
- Encore une fois, voici les liens vers la [Partie 1][part1] et la [Partie 2][part2]
- Si vous ne l'avez pas déjà fait, [obtenez tout le code de ce projet][code]

## Conclusion

Les Protocol Buffers sont assez polyvalents et pratiques. Les utiliser avec un service Bluetooth Low Energy est l'une des façons dont vous pouvez en tirer parti. Alors que le monde connecté de l'IoT continue de s'étendre, je n'ai aucun doute que nous verrons plus de cas d'utilisation à l'avenir !

J'espère que cela vous a inspiré à incorporer les Protocol Buffers dans vos propres projets. Assurez-vous de [télécharger le code d'exemple][code] et commencez dès maintenant.

Ce tutoriel vous a-t-il été utile ? Faites-moi savoir ce que vous en pensez.

[code]: https://www.jaredwolff.com/files/protobuf
[part1]: https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf
[part2]: https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2