---
title: Comment synchroniser un nœud Ethereum sans faire les erreurs que j'ai faites
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-26T19:38:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-sync-an-ethereum-node-using-geth-and-ethereum-wallet-81423d42a583
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Tw_7C1Xuh7G7zMoxHNwpHQ.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: Comment synchroniser un nœud Ethereum sans faire les erreurs que j'ai faites
seo_desc: 'By Zack

  When I first started developing on the Ethereum platform, syncing a node was one
  of the first few things I did. With no one to hold my hand and nowhere to consolidate
  all the common errors I encountered, I wasted weeks just syncing a node. It...'
---

Par Zack

Lorsque j'ai commencé à développer sur la plateforme Ethereum, la synchronisation d'un nœud était l'une des premières choses que j'ai faites. Sans personne pour me guider et sans endroit où consolider toutes les erreurs courantes que j'ai rencontrées, j'ai perdu des semaines juste à synchroniser un nœud. C'était un tel casse-tête que j'ai presque abandonné.

Ne pas connaître la terminologie n'a fait qu'aggraver les choses.

Ainsi, dans cet article, je souhaite consolider toutes les erreurs courantes que vous pourriez rencontrer et expliquer les raisons derrière chaque étape lors de la synchronisation d'un nœud. Espérons que vous n'aurez pas une aussi mauvaise expérience précoce que moi.

### Une rapide introduction

Dans Ethereum, les développeurs créent des morceaux d'une application qui s'exécutent sur le réseau. Ce sont ce qu'on appelle les **contrats intelligents**. Bien que vous puissiez les déployer manuellement sans synchronisation avec un nœud Ethereum, à long terme, il est plus pratique pour le processus de développement de synchroniser (surtout lorsque nous voulons utiliser des frameworks de développement comme [Truffle](http://truffleframework.com/)).

Pour synchroniser un nœud Ethereum, nous aurons besoin des logiciels suivants :

* Geth — Client pour un nœud Ethereum.
* Ethereum Wallet — Interface utilisateur pour un nœud Ethereum.

Commençons.

### Installer Geth

Pour télécharger Geth, allez [ici](https://geth.ethereum.org/downloads/) pour les utilisateurs de Windows. Ensuite, cliquez sur le bouton « Geth pour Windows ».

![Image](https://cdn-media-1.freecodecamp.org/images/fnSKoLWe6RsDwH7GWm0HzodzM1SA7aeXYXOM)

Pour les utilisateurs de MacOS, je recommande de télécharger en utilisant homebrew. Vous pouvez le faire avec les commandes suivantes :

```
brew tap ethereum/ethereum
brew install ethereum
```

Consultez les [instructions de Geth](https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-Mac) pour plus de détails.

Vérifiez que Geth est installé correctement en tapant `geth version` dans le terminal (MacOS) ou PowerShell (Windows).

### Installer Ethereum Wallet

Nous appelons l'interface graphique qui interagit avec le réseau le « wallet ». Vous pouvez trouver de nombreux portefeuilles différents pour Ethereum avec une rapide recherche Google (comme Parity, Jaxx et MyEtherWallet). Personnellement, j'aime utiliser Ethereum Wallet. Il a une interface conviviale, et je suis aussi un peu partial car il est développé par Ethereum lui-même.

Vous pouvez trouver l'installateur [ici](https://github.com/ethereum/mist/releases/latest).

Note : Je préfère **Ethereum Wallet** à **Mist**. Mist est essentiellement un navigateur qui rend les applications décentralisées (dApps) et les sites web.

Pour le développement d'un contrat intelligent, nous n'aurons besoin que d'Ethereum Wallet.

### Mainnet vs Testnet

Dans Ethereum, il existe deux réseaux principaux : le mainnet et le testnet.

Le mainnet est utilisé pour transiger de l'Ether réel. La valeur de l'Ether est liée à la monnaie fiduciaire réelle via les échanges de cryptomonnaies.

En tant que développeurs, nous ne voulons pas exécuter des tests d'application avec de l'argent réel. C'est pour cela que le testnet existe.

Nous appelons le testnet **Ropsten**.

### Exécuter Geth et Ethereum Wallet

Lorsque vous développez un contrat intelligent, vous devriez d'abord synchroniser le testnet. Nous n'aurons besoin de synchroniser le mainnet que lorsque nous serons prêts à déployer.

Vous aurez besoin d'environ **30 Go** d'espace de stockage pour synchroniser un testnet. Comme il y a plus de transactions dans le mainnet, vous aurez besoin d'environ **100 Go** pour synchroniser un mainnet.

Note : certains disent que vous avez besoin d'un stockage SSD pour une écriture rapide afin que la synchronisation puisse rattraper le dernier bloc. Personnellement, je trouve que le stockage HDD est correct. Cependant, si j'avais le choix, j'utiliserais définitivement un stockage SSD.

#### **Pour les utilisateurs de Windows**

Pour un accès facile, je recommande de créer un dossier pour stocker la blockchain. Par exemple, « C:\EthereumTestnet ».

Après avoir créé le dossier, essayez d'exécuter la commande suivante :

```
geth --testnet --data-dir="C:\EthereumTestnet" --rpc --rpcapi eth,web3,net,personal
```

_Édition : Il semble que certains arguments aient changé. Si vous rencontrez une erreur comme « flag provided but not defined: -data-dir », essayez de changer le nom de l'argument en --datadir au lieu de data-dir._

L'argument `--testnet` spécifie que nous voulons synchroniser avec le réseau Ropsten. Ainsi, pour synchroniser le mainnet, vous devez simplement supprimer l'argument `--testnet` et changer le répertoire de données. Par exemple :

`geth --data-dir="C:\EthereumMainnet" --rpc --rpcapi eth,web3,net,personal`

L'argument `--rpc` active le serveur HTTP-RPC. Cela nous permet d'utiliser certains services, comme ceux indiqués dans `--rpcapi eth,web3,net,personal`.

Après avoir entré la commande, vous devriez voir quelque chose comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/SPf0RV1q1D0K0i0xwtnAl3Dc1y9KbzGHmSoD)
_Geth en cours de démarrage._

Pour ne pas corrompre la blockchain, surtout après de nombreuses heures de synchronisation, vous ne devez **PAS** fermer l'invite de commande abruptement. Arrêtez toujours la synchronisation en appuyant sur **Ctrl + C** et attendez que Geth ferme le programme pour vous.

![Image](https://cdn-media-1.freecodecamp.org/images/WaIidVusyhviJMr2FRsXWPb1kpeQS7V7TCh1)
_Après avoir appuyé sur Ctrl + C, Geth s'arrête._

Cependant, il est difficile de se souvenir de toutes les commandes et des services RPC dont vous avez besoin. C'est pourquoi je suggère de créer un raccourci ou un fichier batch pour vous aider.

Il suffit de créer un fichier avec n'importe quel éditeur de texte et de l'enregistrer en tant que fichier **.bat**. Par exemple, _RunGethTestnet.bat_ (le nom n'est pas important). Copiez et collez la commande dans le fichier et enregistrez-le. La prochaine fois que vous aurez besoin d'exécuter Geth pour Ropsten, il vous suffira de double-cliquer sur le fichier.

Après avoir exécuté Geth, nous devons exécuter Ethereum Wallet. Comme nous voulons que l'interface localise l'emplacement exact où nous avons synchronisé nos fichiers avec Geth, nous l'exécutons à partir de la console.

De manière similaire à Geth, j'ai également enregistré un fichier batch pour cela avec une commande d'exemple, comme celle ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/oJVB33zdplMlBzKGqVlJvLUTHH5VTdTO4cUU)

Notez que votre commande peut être légèrement différente de la mienne, car vous pouvez stocker votre application dans un répertoire différent.

Alternativement, vous pouvez ajouter l'application à votre chemin d'accès.

L'argument `--node-datadir="C:\EthereumTestnet"` indique où j'ai stocké mes données de chaîne, qui est exactement le même que celui que j'ai spécifié pour Geth.

#### **Pour les utilisateurs de Mac**

C'est légèrement plus simple pour MacOS, car les données de chaîne sont téléchargées automatiquement dans la bibliothèque et ne sont pas cachées. Ainsi, nous n'aurons pas besoin de spécifier le répertoire de données.

Néanmoins, je recommande de créer un fichier de script pour faciliter l'exécution de Geth et d'Ethereum Wallet.

![Image](https://cdn-media-1.freecodecamp.org/images/UpneIcjqnia6pTXOqQqzAkBQ7zgGl3KNIEmD)
_Commande Geth pour le testnet_

![Image](https://cdn-media-1.freecodecamp.org/images/jS0TKBaz-kKx0kN6pC3fbqbsmlbXkbwKpPtM)
_Commande pour exécuter Ethereum Wallet_

Note : **Geth doit s'exécuter avant Ethereum Wallet**.

L'exécution d'Ethereum Wallet seul démarrera automatiquement le processus de synchronisation car il exécutera automatiquement un client Geth en arrière-plan. C'est convivial, mais cela n'active pas les services RPC que nous voulons utiliser. Ainsi, nous voulons nous assurer que RPC est activé à la fois dans notre exécution de Geth et d'Ethereum Wallet.

#### Quelques notes

1. Le processus de synchronisation est très long et peut prendre jusqu'à 2-3 jours. Soyez patient et envisagez de laisser votre ordinateur allumé toute la nuit.
2. La vitesse de synchronisation dépend de votre vitesse Internet, du nombre de pairs et de la vitesse d'écriture de votre disque de stockage.
3. Comme les données sont stockées dans des blocs et liés ensemble, la corruption d'un bloc peut corrompre toute la chaîne de données. Cela peut potentiellement gaspiller vos efforts d'attente de jours pour la synchronisation du nœud. Par conséquent, il est très important d'arrêter correctement votre Geth. Dans certains cas, vous pourriez vouloir [revenir en arrière](https://github.com/ethereumproject/go-ethereum/pull/206). Mais la prévention est meilleure que la cure ici.
4. La barre de progression sur votre Ethereum Wallet n'est **PAS** précise. Se fier à elle vous donnera beaucoup d'anxiété et de frustration.
5. Geth s'exécute sur le port 30303 pour l'écoute externe.
6. Le port par défaut utilisé pour la communication interne, par exemple entre votre portefeuille et Geth, est 8545.

### Assurez-vous que votre port vers le client Geth est ouvert

Il est vraiment important de s'assurer que la connexion à votre client Geth n'est pas limitée. Un gros casse-tête que j'ai rencontré était de laisser mon pare-feu limiter le nombre de connexions que je pouvais avoir via le client Geth.

Vous pouvez repérer ce problème en regardant le **nombre de pairs**. S'il reste constamment bas à environ 1-3 pairs (pendant au moins une demi-heure), il y a de bonnes chances que votre connexion soit limitée. Une plage saine est supérieure à 5 pairs.

#### **Utilisateurs de MacOS**

Lorsque vous exécutez Geth, il devrait y avoir une notification vous demandant d'autoriser la connexion. Eh bien, bien sûr, cliquez sur « Autoriser ».

Pour vérifier, allez dans Préférences Système > Sécurité et Confidentialité.

Sous l'onglet **Pare-feu**, cliquez sur **Options de pare-feu**.

![Image](https://cdn-media-1.freecodecamp.org/images/8KMRVnoiExu52vU1KMe37GdTLLf31qRSm8H-)

#### **Utilisateurs de Windows**

Pour ouvrir votre port, allez dans Panneau de configuration > Système et sécurité > Pare-feu Windows Defender.

Cliquez sur **Paramètres avancés**. Dans le panneau latéral, cliquez sur **Règles entrantes**.

![Image](https://cdn-media-1.freecodecamp.org/images/L8rwzz5b5RnDj9NrNzbUYFDxVWZUAkmsYm45)

![Image](https://cdn-media-1.freecodecamp.org/images/LGmZGE7ILFS22HZ7Vn7WXzlR0wi06a6m4bD5)

Les ports entrants que vous souhaitez ouvrir sont TCP et UDP 30303. J'ai donc créé une règle pour TCP 30303 et une autre pour UDP 30303.

Vous devrez peut-être ouvrir vos ports sortants pour TCP 30303 également.

Notez que tout pare-feu/anti-virus tiers peut également limiter vos connexions, alors assurez-vous de le configurer en conséquence.

### Se connecter à Geth

Pour récupérer plus d'informations sur votre nœud, vous pouvez vous connecter au client Geth et exécuter des commandes avec lui en utilisant les services RPC.

Voici une méthode simple pour vérifier votre statut de synchronisation : connectez-vous au client en entrant la commande suivante dans un terminal/console séparé.

`geth attach [http://127.0.0.1:8545](http://127.0.0.1:8545)`

Encore une fois, vous pourriez vouloir le stocker dans un fichier batch/script pour votre propre commodité.

Après avoir exécuté la commande, vous devriez voir quelque chose comme ceci.

![Image](https://cdn-media-1.freecodecamp.org/images/7uWtIMqSbpdOAmw7BZfG1DKvx-BRafBLhkj5)

Tapez `web3.eth` et vous devriez voir beaucoup d'informations. Pour récupérer des informations spécifiques sur la synchronisation, tapez `web3.eth.syncing` à la place.

![Image](https://cdn-media-1.freecodecamp.org/images/AWbDTgfiHY6BUWLoNCn8Rij2oikEOggIBtDb)

Comme vous pouvez le voir, la barre de progression trouvée en haut de l'Ethereum Wallet est simplement une comparaison entre le **highestBlock** et le **currentBlock**. Comme le **highestBlock** connu de votre ordinateur peut ne pas être le bloc le plus élevé réel, la barre de progression peut ne pas refléter le progrès réel.

En fait, le **highestBlock** et le **knownStates** continueront d'augmenter à mesure que vous synchronisez vos nœuds.

### Quelques points finaux

Comme la technologie évolue rapidement, utilisez toujours la version stable du client et du portefeuille pour éviter de vous donner plus de maux de tête.

De plus, notez qu'il y a toujours une solution de contournement pour tous les problèmes que vous rencontrez. Lorsque vous rencontrez un problème de synchronisation, vous pouvez essayer de rechercher des solutions car vous n'êtes probablement pas le premier à rencontrer le même problème.

Et rappelez-vous toujours que vous n'avez pas besoin de synchroniser un nœud pour développer un contrat intelligent. Faire cela aide seulement à faciliter votre compréhension de l'environnement ainsi que votre processus de développement. Alors, ne vous en voulez pas trop si vous rencontrez des problèmes si tôt dans le processus de développement.

_Pour plus d'articles comme celui-ci, [suivez-moi](https://medium.com/@zack.learns) ou visitez mon site — [A developer's perspective](https://developerperspective.com/)._