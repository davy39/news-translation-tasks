---
title: Comment configurer une blockchain privée Ethereum multi-nœuds sur votre Mac
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-17T02:41:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-multi-node-private-ethereum-blockchain-from-scratch-in-20-mins-or-less-e0d7e091e062
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GF6ozztlIUgBB7wY8OtxLA.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: ethereum blockchain
  slug: ethereum-blockchain
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment configurer une blockchain privée Ethereum multi-nœuds sur votre
  Mac
seo_desc: 'By Prashant Ram

  In this tutorial we will:


  Setup a blockchain with multiple nodes

  Setup mining nodes

  Connect the multiple nodes and setup the blockchain network

  Test the blockchain network by mining blocks and verifying that blocks are propagated
  to ...'
---

Par Prashant Ram

Dans ce tutoriel, nous allons :

* Configurer une blockchain avec plusieurs nœuds
* Configurer des nœuds de minage
* Connecter les multiples nœuds et configurer le réseau de blockchain
* Tester le réseau de blockchain en minant des blocs et en vérifiant que les blocs sont propagés à tous les nœuds
* Vérifier que la copie locale de la blockchain sur tous les nœuds est mise à jour

### Installation et logiciels prérequis

[Go Ethereum](https://geth.ethereum.org/) (Geth) est un outil d'interface en ligne de commande qui vous permet d'interagir avec votre blockchain privée Ethereum.

Si vous devez installer [Homebrew](https://brew.sh/) sur votre Mac, placez la ligne suivante dans votre invite de commande de terminal :

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Une fois Homebrew installé, [installez](https://github.com/ethereum/go-ethereum/wiki/Installation-Instructions-for-Mac) Geth :

```
$ brew tap ethereum/ethereum
$ brew install ethereum
```

### Configurer le bloc Genesis

Créez un nouveau répertoire de projet. À l'intérieur, créez le fichier `**genesis.json**` en utilisant l'éditeur de votre choix. J'utilise [Visual Studio Code sur Mac](https://code.visualstudio.com/docs/setup/mac), qui est un éditeur gratuit :

```
$ mkdir project3
$ cd project3
```

Copiez le JSON suivant dans votre fichier `**genesis.json**`, et sauvegardez le fichier dans votre répertoire de projet.

```
\\Fichier genesis.json
```

```
{
```

```
"config": {
```

```
"chainId": 4321,
```

```
"homesteadBlock": 0,
```

```
"eip155Block": 0,
```

```
"eip158Block": 0
```

```
},
```

```
"alloc": {},
```

```
"difficulty" : "0x20000",
```

```
"gasLimit"   : "0x8880000"
```

```
}
```

### Configurer le premier nœud (Nœud 1)

Une fois le fichier `**genesis.json**` sauvegardé, vous êtes prêt à créer votre premier nœud. Pour créer votre premier nœud, ouvrez une nouvelle fenêtre de terminal et naviguez jusqu'à votre dossier de projet, puis tapez la commande suivante :

```
$ geth --datadir blkchain1 init genesis.json
```

Cette commande initialise un nouveau nœud de blockchain en utilisant la configuration spécifiée dans le fichier `**genesis.json**`. En utilisant `--datadir`, nous spécifions le nom du répertoire où la copie locale de la blockchain sera stockée sur le nœud.

Cette commande créera un répertoire appelé `**blkchain1**` dans votre répertoire de projet. Ce répertoire contient les répertoires `**geth**` et `**keystore**`. Les données de la blockchain seront stockées dans la base de données locale dans le répertoire `**geth**`.

Vous pouvez vérifier cela en naviguant dans le répertoire `**blkchain1**` dans votre terminal de commande et en tapant `ls -l`. Naviguez également dans le sous-répertoire `**geth**` et tapez `ls -l`.

Maintenant que votre Nœud 1 est initialisé, démarrons le Nœud 1 en utilisant Geth. Dans votre fenêtre de terminal, naviguez jusqu'à votre dossier de projet (où vous avez sauvegardé votre fichier `**genesis.json**`) et tapez ce qui suit :

```
$ geth --datadir blkchain1 --nodiscover --networkid 1234 console
```

Cette commande démarrera votre premier nœud et ouvrira la console Geth, où vous pourrez taper des commandes pour interagir avec la blockchain du Nœud 1.

Vous verrez ce qui suit :

![Image](https://cdn-media-1.freecodecamp.org/images/qFQFOHhKzFjrlf9fkdB8VkXKLgZP4vwruNFq)

Décomposons cette commande "geth console" et comprenons-la :

`--datadir blkchain1` :  
spécifie le répertoire de données de la blockchain. Si vous ne spécifiez pas cela, il utilisera par défaut la blockchain principale Ethereum.

`--nodiscover` :   
désactive le mécanisme de découverte des pairs et permet l'ajout manuel de pairs.

`--networkid 1234` :   
l'identité de votre réseau Ethereum, les autres nœuds pairs auront également le même identifiant de réseau. **L'identifiant de réseau peut être n'importe quelle valeur entière aléatoire.**

Maintenant que vous êtes dans la console Geth, pour obtenir plus d'informations sur le nœud, nous utiliserons la commande **admin**. Tapez la commande suivante dans la console Geth :

```
> admin.nodeInfo
```

Cela vous donnera plus d'informations sur votre nœud :

![Image](https://cdn-media-1.freecodecamp.org/images/EQ8atvBkddL3jmQoPHHaXKesil9dIcghlS4Z)

Remarquez ce qui suit :

* par défaut, le port `listener` est 30303
* l'`enode id` est votre identifiant de nœud
* le port `discovery` est '0', puisque nous l'avons défini sur `--nodiscover`.

Pour obtenir une liste de toutes les commandes admin, tapez "admin." et appuyez sur <tab>

![Image](https://cdn-media-1.freecodecamp.org/images/laeqYYTVI8myUczhPOyCAaJUfL18KLzWWWnj)

Maintenant, configurons un compte où les [ethers minés](https://www.ethereum.org/ether) seront collectés. Tapez ce qui suit dans la console Geth :

```
> personal.newAccount()
```

![Image](https://cdn-media-1.freecodecamp.org/images/qu3VCmulyFDh9DHJeGLIXAu45c-dQe697rNj)

Vous pouvez mettre n'importe quelle phrase de passe — c'est votre mot de passe. La commande retourne l'identifiant du compte.

Pour obtenir une liste de tous les comptes :

```
> personal.listAccounts
```

![Image](https://cdn-media-1.freecodecamp.org/images/iWcJXCbvNTTtVOWtR0x5dp7nkldcdO9kY0ol)

Le Nœud 1 est maintenant prêt !

Gardez la fenêtre de terminal (avec la console Geth pour le Nœud 1) ouverte et en cours d'exécution. Nous ouvrirons une nouvelle fenêtre de terminal pour configurer le Nœud 2.

### Configurer le deuxième nœud (Nœud 2)

Maintenant, configurons un deuxième nœud dans le réseau de blockchain. Le processus sera similaire à la configuration du Nœud 1.

Ouvrez une nouvelle fenêtre de terminal et naviguez jusqu'au dossier de projet qui contient le fichier `**genesis.json**`.

Initialisez le nouveau nœud avec la commande suivante :

```
$ geth --datadir blkchain2 init genesis.json
```

**Note** : Puisque nous voulons que ce nœud fasse partie de la même blockchain, nous utilisons le même bloc genesis.

Cela créera un nouveau nœud dont les données seront stockées dans un nouveau répertoire appelé `**blkchain2**` (celui-ci contiendra la copie locale de la base de données de la blockchain pour le nœud 2).

Pour démarrer le nœud 2 avec une console Geth, tapez ce qui suit :

```
$ geth --datadir blkchain2 --nodiscover --networkid 1234 --port 30304 console
```

Cela démarrera le Nœud 2 et ouvrira la console Geth connectée au Nœud 2.

Notez les différences suivantes pour le Nœud 2 :

* nous spécifions un numéro de port 30304  
Le port par défaut 30303 est déjà utilisé par le premier nœud, donc si nous ne spécifions pas un port séparé, cela générera une erreur.
* nous donnons le même networkid que pour le nœud 1. Cela est important, puisque nous voulons que les deux nœuds fassent partie du réseau
* nous spécifions que le `--datadir` pour le nœud 2 sera dans `**blkchain2**`

Exécutez la commande `admin.nodeInfo` dans la console Geth pour le Nœud 2 :

```
> admin.nodeInfo
```

![Image](https://cdn-media-1.freecodecamp.org/images/SrPWuVNtDrPLzXnnsjXrvfS5a6GAhp85XXXP)

Remarquez que cela fournit les informations du nœud pour le Nœud 2. Vous pouvez comparer l'`enode id` en exécutant la commande `same admin.nodeInfo` dans la fenêtre de terminal exécutant la console Geth pour le Nœud 1.

![Image](https://cdn-media-1.freecodecamp.org/images/2sIy-KrePNkkxM7rzFa2y2nr9s3l-POZtDB8)
_NŒUD 1_

![Image](https://cdn-media-1.freecodecamp.org/images/MZImf8aMKy81B6yI-Xa01G2nVjKsW2Hn980q)
_NŒUD 2_

Similaire au Nœud 1, nous pouvons configurer un compte sur le Nœud 2 en tapant `personal.newAccount()` dans la console Geth pour le Nœud 2.

Vous pouvez utiliser n'importe quelle phrase de passe pour le compte.

```
> personal.newAccount()
```

Le Nœud 2 est maintenant prêt !

Gardez ouvertes les deux fenêtres de terminal, l'une exécutant la console Geth (Nœud 1) et la seconde exécutant la console Geth (Nœud 2), côte à côte.

À l'étape suivante, nous connecterons le Nœud 1 et le Nœud 2 et créerons le réseau de blockchain !

### Connecter les nœuds

Félicitations ! Vous avez deux nœuds de blockchain en cours d'exécution.

L'étape suivante consiste à les connecter l'un à l'autre et à créer un réseau. Nous allons faire cela en ajoutant l'un des nœuds à l'autre en tant que "pair".

Exécutez la commande suivante sur les consoles Geth du Nœud 1 et du Nœud 2 :

```
> admin.peers
```

Remarquez que les deux retournent un tableau vide, puisque les nœuds ne sont connectés à aucun autre nœud.

Ajoutons le Nœud 1 en tant que pair au Nœud 2.

1. Exécutez la commande `admin.nodeInfo` sur le Nœud 1

![Image](https://cdn-media-1.freecodecamp.org/images/tuXpZT0g2vBWFEevELfZq14Ht0M8WzTCp6Is)

2. Copiez l'`enode id` pour le Nœud 1 :

```
"enode://549468e6d00e135128af33e03a6d27b0ee5fda7fbd0154b2e83fe68afdfda869eb6ace6ccaefe84ed7a5b804529dcef49f0b5d64be97da87b1e28ddecfca227a@[::]:30303?discport=0"
```

3. Dans la console Geth pour le Nœud 2, ajoutez le Nœud 1 en tant que pair au Nœud 2 en utilisant la commande `admin.addPeer("//enode id")` :

```
> admin.addPeer("enode://549468e6d00e135128af33e03a6d27b0ee5fda7fbd0154b2e83fe68afdfda869eb6ace6ccaefe84ed7a5b804529dcef49f0b5d64be97da87b1e28ddecfca227a@[::]:30303?discport=0")
```

Maintenant, lorsque vous exécutez la commande `admin.peers` dans l'une des consoles Geth, vous verrez l'autre Nœud listé en tant que pair !

![Image](https://cdn-media-1.freecodecamp.org/images/WqDvQvSJMzQU-S-dPkXruPAoPVd7-L9EWfbO)

Hourra ! Vous avez maintenant un réseau de blockchain connecté !

Mais comment en être sûr ?

Mettons-le à l'épreuve, voulez-vous ? Mettons à jour quelque chose dans le Nœud 1 et voyons si ce changement est propagé à travers le réseau de blockchain au Nœud 2.

### Vérifier que vous avez une blockchain connectée et une base de données distribuée

D'accord, jusqu'à présent vous devriez avoir :

* Deux fenêtres de terminal ouvertes  
L'une exécutant la console Geth pour le Nœud 1, et la seconde exécutant la console Get pour le Nœud 2
* Le Nœud 1 sauvegarde sa copie locale de la blockchain dans le dossier `**blkchain1**`
* Le Nœud 2 sauvegarde sa copie locale de la blockchain dans le dossier `**blkchain2**`
* De plus, à l'étape précédente, vous avez connecté les deux nœuds en utilisant `admin.addPeer()`

Ainsi, si de nouveaux blocs sont minés et ajoutés dans le Nœud 1, ce nouveau bloc devrait se propager sur le réseau de blockchain, et la copie locale de la blockchain du nœud 2 devrait se mettre à jour automatiquement.

Vérifions si cela se produit.

Dans la console Geth (Nœud 1), commençons le minage :

```
> miner.start(1)
```

![Image](https://cdn-media-1.freecodecamp.org/images/dHeuhJXRCmmyY2DJnMggCUugBMw0yumw5qlr)

Pour vérifier combien de blocs ont été minés au Nœud 1 à tout moment, exécutez ce qui suit dans la console Geth (Nœud 1) :

```
> eth.blockNumber
```

Cela retournera le numéro du bloc actuel miné (ou la hauteur de la blockchain).

Après que quelques blocs aient été minés, allez dans la console Geth (Nœud 2) et exécutez la commande `eth.blockNumber`.

Vous remarquerez que la hauteur du bloc dans le Nœud 2 correspond à la hauteur du bloc dans le Nœud 1 ! Cela vérifie que les blocs qui ont été minés dans le Nœud 1 ont été propagés sur la blockchain au Nœud 2.

Pour aller plus loin, vous pouvez vérifier les données dans les blocs réels sur le Nœud 1 et le Nœud 2.

Attendez qu'environ 10 blocs aient été minés, puis exécutez la commande suivante dans la console Geth (Nœud 1) et la console Geth (Nœud 2) :

```
> eth.getBlock(3)
```

Cette commande affiche le contenu du Bloc 3 de la blockchain. Remarquez que les données affichées dans la console Geth (Nœud 1) et la console Geth (Nœud 2) sont identiques, indiquant que le Bloc 3 qui a été miné par le Nœud 1 a été propagé sur le réseau de blockchain et fait également partie des données locales de la blockchain dans le Nœud 2.

![Image](https://cdn-media-1.freecodecamp.org/images/d7QchSLFO99BhalkAiYPJBOHLQ-u0JRak8fL)
_Nœud 1_

![Image](https://cdn-media-1.freecodecamp.org/images/GGrpKsjlth7LndbiKQR3haXwTi2kGpC2csjc)
_Nœud 2_

Hourra !! Vous avez maintenant un réseau Ethereum privé multi-nœuds entièrement fonctionnel et connecté !

Bon codage !

**_Suivez-moi sur [Medium](https://medium.com/@prashantramnyc) pour les dernières mises à jour et publications !_**