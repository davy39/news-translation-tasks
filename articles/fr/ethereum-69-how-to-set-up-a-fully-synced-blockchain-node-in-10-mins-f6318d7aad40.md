---
title: 'Ethereum 69 : Comment configurer un nœud blockchain entièrement synchronisé
  en 10 minutes'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-16T23:18:46.000Z'
originalURL: https://freecodecamp.org/news/ethereum-69-how-to-set-up-a-fully-synced-blockchain-node-in-10-mins-f6318d7aad40
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oS4hnBtXtJ5h0hIJ0LHnyg.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: 'Ethereum 69 : Comment configurer un nœud blockchain entièrement synchronisé
  en 10 minutes'
seo_desc: 'By Lukas Lukac

  Welcome in the first article of our new go-ethereum series!

  In the next 10 mins you will:


  Learn the first blockchain glossary without any necessary prior ecosystem knowledge

  Setup your fully synced testing node (“client/server”) in un...'
---

Par Lukas Lukac

Bienvenue dans le premier article de notre nouvelle série go-ethereum !

Dans les 10 prochaines minutes, vous allez :

* Apprendre le premier glossaire blockchain sans aucune connaissance préalable de l'écosystème
* **Configurer votre nœud de test entièrement synchronisé** ("client/serveur") **en moins de 10 minutes**
* **Créer votre compte** et recevoir une transaction de 8 ETH de la part de la fondation Ethereum GRATUITEMENT

Notre devise est : la pratique avant la théorie — alors plongeons directement dans l'installation d'un nœud de test Ethereum entièrement synchronisé connecté au réseau de test Rinkeby !

### Geth

`Geth` est une interface en ligne de commande (CLI), un binaire compilé, un programme et un client pour exécuter un nœud Ethereum complet implémenté en Go.

Nous allons utiliser **Geth** pour :

* exécuter un nœud Ethereum entièrement synchronisé pour se connecter à un réseau de test appelé Rinkeby
* créer un nouveau compte pour pouvoir envoyer et recevoir des transactions
* lire l'état de l'EVM, par exemple vérifier le solde de n'importe quel compte (vous voulez savoir combien d'argent a votre petite amie, petit ami, femme, voisin ? Quelle transparence !)

### Installation de Geth

Nous pouvons l'installer directement depuis les dépôts :

**Mac**

```
brew tap ethereum/ethereum
brew install ethereum
```

**Linux**

```
sudo apt-get install software-properties-common
sudo add-apt-repository -y ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install ethereum
```

**Windows**

```
Bonne chance :)
```

**Vérifier l'installation :**

```
which geth
> /usr/local/bin/geth
```

```
geth version
> Geth
> Version: 1.8.20-stable
```

Assurez-vous d'exécuter la même version afin de pouvoir effectuer une synchronisation complète du réseau Rinkeby, comme décrit dans les prochaines étapes, car Rinkeby a mis en œuvre un hardfork Constantinople pris en charge par Geth 1.8.20.

### Exécution d'un nœud blockchain

Eh bien, le diable est dans les détails… mais commencer est en fait simple. Merci aux développeurs Ethereum.

Configurons un nouveau nœud **Rinkeby** (réseau de test Ethereum utilisant le protocole Clique PoA) entièrement synchronisé.

L'implémentation PoA de Rinkeby est beaucoup plus rapide mais significativement moins sécurisée. Elle est plus centralisée que le consensus PoW du mainnet, ce qui est parfaitement acceptable pour un réseau de test. Rinkeby parvient à approuver un nouveau bloc avec un ensemble de transactions toutes les 15 secondes.

D'accord, d'accord, d'accord... Que signifient réellement ces mots ?

* **Rinkeby** : nom du réseau de test Proof of Authority
* **Nœud** : essentiellement un serveur traditionnel exécutant le client/serveur Ethereum
* **Consensus** : un algorithme définissant comment les transactions seront validées, ajoutées et persistées dans la base de données sur chaque nœud
* **Bloc** : un ensemble de transactions dans un tableau complexe diffusé sur le réseau entre tous les nœuds toutes les 15 secondes
* **Transaction** : ne pensez pas à une transaction bancaire. Une transaction blockchain est un **changement d'état**. Renommer le propriétaire d'un contrat intelligent d'Alice à Bob ? Changer le solde de votre compte de 1 ETH à 5 ETH ? Définir la valeur de la variable "foo" à "foo_value_123" dans votre contrat intelligent ? C'est une transaction.

Vous pouvez en savoir plus sur la proposition Rinkeby PoA ici : [https://github.com/ethereum/EIPs/issues/225](https://github.com/ethereum/EIPs/issues/225)

```
geth --rinkeby --datadir=~/.gophersland_ethereum_r1 --port=30304 --cache=2048 --rpc --rpcport=8546 --rpcapi=eth,web3,net,personal --syncmode=fast
```

La commande ci-dessus va :

* initialiser un nouveau répertoire où toutes les données seront stockées dans `~/.gophersland_ethereum_r1`. Le répertoire par défaut serait : `~/.ethereum`
* commencer à télécharger l'historique Ethereum nécessaire pour devenir un nouveau nœud entièrement valide et synchronisé du réseau
* la communication se fera via le port 30304
* le cache, une sorte de tampon, sera défini à 2 Go pour accélérer le processus de synchronisation
* une API RPC supplémentaire sera lancée afin que nous puissions communiquer avec notre nœud via des consoles, une belle interface graphique sur le port 8546, plus tard

![Image](https://cdn-media-1.freecodecamp.org/images/1*vABGraHKLDKTR5jWoVYsoA.png)

Attendez quelques heures jusqu'à ce que la blockchain soit entièrement synchronisée.

Le numéro de bloc actuel au 24 septembre est : 3039786. Sur mon AMD Ryzen 5 2600, 3,4 GHz, le processus de synchronisation a pris 3 heures. Oh oui, j'ai un nouveau PC de gaming !

Pendant ce temps, vous pouvez [suivre Web3Coach sur Twitter](https://twitter.com/Web3Coach) ou préparer le dîner, probablement le petit-déjeuner aussi, aller à la salle de sport… disons simplement que la blockchain n'est pas la base de données la plus rapide :)

Finalement, le message imprimé sera :

* INFO [<time>] Imported new chain segment count=1
* INFO [<time>] Imported new chain segment count=1
* INFO [<time>] Imported new chain segment count=1
* INFO [<time>] Imported new chain segment count=1

**Félicitations, vous faites maintenant partie de la révolution blockchain en moins de 10 minutes !!!**

### Création de votre premier compte blockchain

#### Keystore

Tous les comptes Ethereum et leurs clés sont stockés dans un répertoire appelé "keystore". Le répertoire est vide par défaut car nous n'avons pas encore créé notre propre compte !

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/
```

```
drwx------  4 enchanter enchanter 4096 sep 24 15:26 .
drwxr-xr-x 18 enchanter enchanter 4096 sep 24 11:51 ..
drwx------  4 enchanter enchanter 4096 sep 24 15:26 geth
srw-------  1 enchanter enchanter    0 sep 24 15:26 geth.ipc
drwx------  2 enchanter enchanter 4096 sep 23 09:54 keystore
```

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/keystore/
```

```
drwx------ 2 enchanter enchanter 4096 sep 23 09:54 .
drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..
```

#### Compte

Pour créer un nouveau compte, exécutez la commande suivante, déjà familière, **geth**.

```
geth --datadir=~/.gophersland_ethereum_r1 account new
```

Vous serez invité à entrer une phrase de passe (c'est votre MOT DE PASSE SUPER SECRET). Cela est nécessaire pour déchiffrer votre nouvelle clé privée associée à votre nouvelle adresse Ethereum, car cela vous permet de l'utiliser plus tard pour signer des transactions sur la blockchain. Notez-la quelque part, car nous en aurons besoin plus tard. Mais ne vous inquiétez pas si vous l'oubliez, ce n'est qu'un réseau de test de toute façon.

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/keystore/
```

```
drwx------ 2 enchanter enchanter 4096 sep 23 09:54 .
drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..
```

```
enchanter@lukas-gaming:~$ geth --datadir=~/.gophersland_ethereum_r1 account new
```

```
INFO [09-24|15:36:33.566] Maximum peer count                       ETH=25 LES=0 total=25
```

```
Your new account is locked with a password. Please give a password. Do not forget this password.
```

```
Passphrase: Repeat passphrase:
```

```
Address: {ceee57f2b700c2f37d1476a7974965e149fce2d4}
```

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/keystore/
```

```
drwx------ 2 enchanter enchanter 4096 sep 24 15:36 .
drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..
-rw------- 1 enchanter enchanter  491 sep 24 15:36 
```

```
UTC--2018-09-24T13-36-43.069452577Z--ceee57f2b700c2f37d1476a7974965e149fce2d4
```

**Youpi ! Mon nouvelle adresse Ethereum est active :** `ceee57f2b700c2f37d1476a7974965e149fce2d4`.

Vous rencontrerez normalement cette adresse préfixée par "**0x**" pour indiquer le codage de l'adresse, **HEX**.

Le nouveau format des fichiers de clés est : `UTC--<created_at UTC ISO8601>-<votre adresse en hex` encoding>. L'ordre des comptes lors de la liste est lexicographique, mais en raison du format de l'horodatage, il est en fait dans l'ordre de création.

Si vous êtes curieux de savoir ce qu'il y a à l'intérieur du fichier, n'hésitez pas à l'ouvrir ! Vous verrez :

* **Adresse** : votre nouvelle adresse hex
* **Crypto** : un ensemble de variables mathématiques responsables de la représentation de votre clé privée sous forme chiffrée, ne vous inquiétez pas de cette magie pour l'instant

**Note intéressante :** la génération de compte se fait en mode hors ligne et ne nécessite pas un nœud blockchain synchronisé. Vous vous demandez comment il est possible de générer une adresse unique en mode hors ligne d'un point de vue technique ? Nous examinerons le code source de **go-ethereum** lui-même dans le prochain article.

**Spoiler :** c'est parce que l'adresse est un hachage de votre clé publique qui est basée sur votre clé privée unique.

D'accord, j'ai un nouveau compte Ethereum brillant, quel est mon solde et comment puis-je déposer un peu d'**Ether** de test ?

En parlant d'Ether… qu'est-ce que c'est exactement ?

#### Ether

L'Ether est la cryptomonnaie alimentant le réseau Ethereum. Il est utilisé comme unité de valeur et pour payer les mineurs pour la validation, l'ajout et la persistance des transactions dans la base de données collective. Mais principalement, c'est une technique pour prévenir le SPAM car les mineurs sont récompensés par 5 (depuis le mois dernier "seulement" 3) ETH pour chaque bloc miné avec succès. Oui, cela représente 600 $ au prix actuel du 24 septembre, toutes les 15 secondes. Pas une mauvaise affaire.

### Comment recevoir une transaction de 8 ETH de la fondation Ethereum GRATUITEMENT

#### Vérification du solde du compte

Assurons-nous d'abord que le solde de notre compte est à 0, sauf si quelqu'un a déjà réussi à envoyer un peu d'Ether par la bonté de son cœur.

**Geth** fournit une console JavaScript qui peut être attachée au binaire exécutable pour interagir commodément avec la blockchain. Nous pouvons nous y connecter en spécifiant un fichier socket qui est exposé une fois que **Geth** démarre. Les fichiers socket sont très utiles pour la "communication inter-processus sur la même machine", aka IPC.

Vous pouvez localiser ce fichier dans le répertoire de données par défaut pendant que le programme Geth est en cours d'exécution :

```
enchanter@lukas-gaming:~$ ls -la ~/.gophersland_ethereum_r1/
```

```
drwx------  4 enchanter enchanter 4096 Sep 24 15:44 .
drwxr-xr-x 18 enchanter enchanter 4096 Sep 24 15:47 ..
drwx------  4 enchanter enchanter 4096 Sep 24 15:44 geth
srw-------  1 enchanter enchanter    0 Sep 24 15:44 geth.ipc
drwx------  2 enchanter enchanter 4096 Sep 24 15:47 keystore
```

Interagissons avec le réseau Rinkeby en utilisant la commande "**geth attach**" dans un autre terminal pendant que votre nœud blockchain est toujours en cours d'exécution. Assurez-vous de passer le chemin absolu vers le fichier IPC, sinon vous obtiendrez une erreur.

```
enchanter@lukas-gaming:~$ geth attach ipc:/home/enchanter/.gophersland_ethereum_r1/geth.ipc
```

```
Welcome to the Geth JavaScript console!
```

```
instance: Geth/v1.8.15-stable-89451f7c/linux-amd64/go1.10.1
coinbase: 0xceee57f2b700c2f37d1476a7974965e149fce2d4
at block: 3044891 (Mon, 24 Sep 2018 16:42:36 CEST)
```

```
datadir: /home/enchanter/.gophersland_ethereum_r1
modules: admin:1.0 clique:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0
```

```
> eth.accounts["0xceee57f2b700c2f37d1476a7974965e149fce2d4"]
```

```
> eth.syncing
false
```

```
> eth.getBalance("0xceee57f2b700c2f37d1476a7974965e149fce2d4")
0
```

#### Requête blockchain :

**eth.accounts** : pour vérifier vos comptes actuellement disponibles

**eth.syncing** : pour s'assurer que notre état, la base de données, est entièrement à jour avec le reste du réseau afin de garantir que la réponse getBalance sera basée sur le dernier état

**eth.getBalance("<votre adresse>")** : pour interroger la base de données.

#### Recevoir une transaction de 8 ETH de la fondation Ethereum GRATUITEMENT

La fondation Ethereum dispose d'un programme très pratique appelé "**Faucet**" disponible en ligne pour attribuer de l'Ether aux comptes qui en font la demande en temps réel.

Demander de l'Ether :

1. Publiez l'adresse de votre compte sur l'un des réseaux sociaux publics
2. Par exemple, publiez un tweet contenant votre adresse Ethereum n'importe où dans le tweet comme celui-ci [https://twitter.com/EnchanterIO/status/1044238559224483841](https://twitter.com/EnchanterIO/status/1044238559224483841), assurez-vous de mentionner [@Web3Coach](https://twitter.com/Web3Coach) et [@freeCodeCamp](https://twitter.com/freecodecamp) et faites-nous savoir si vous aimez le tutoriel !
3. Ouvrez [https://www.rinkeby.io/#faucet](https://www.rinkeby.io/#faucet) et collez l'URL du tweet
4. Cliquez sur "Give me Ether", choisissez entre 3, 7,5 ou 18,75 Ether
5. Attendez quelques secondes
6. Interrogez à nouveau le solde de votre compte

![Image](https://cdn-media-1.freecodecamp.org/images/0*Zd4RuYRAIiyqy8Jf)
_Rinkeby Faucet_

![Image](https://cdn-media-1.freecodecamp.org/images/0*TM_yQ3hRp8c8tyf8)

### Voilà

Vous êtes riche… dans un réseau de test. Félicitations pour être arrivé aussi loin.

Vous pouvez continuer à développer vos compétences en blockchain en [construisant une blockchain à partir de zéro en Go !](https://www.freecodecamp.org/news/build-a-blockchain-in-golang-from-scratch/)