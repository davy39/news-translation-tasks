---
title: Comment transférer des fonds sur le réseau Ethereum en utilisant le CLI GETH
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-08T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-transfer-funds-on-the-ethereum-network-using-the-geth-cli-b7eac16aa3a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eS0bXFKKeapljk0Ep3tw4A.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Comment transférer des fonds sur le réseau Ethereum en utilisant le CLI
  GETH
seo_desc: 'By Lukas Lukac

  In my previous article, you learned how to set up a fully synced blockchain node
  in 10 mins. It’s now time to learn how to perform a transaction on the Ethereum
  network using the GETH CLI.

  To be on the same page, go through all the ste...'
---

Par Lukas Lukac

Dans mon [article précédent](https://medium.freecodecamp.org/ethereum-69-how-to-set-up-a-fully-synced-blockchain-node-in-10-mins-f6318d7aad40), vous avez appris comment configurer un nœud blockchain entièrement synchronisé en 10 minutes. Il est maintenant temps d'apprendre comment effectuer une transaction sur le réseau Ethereum en utilisant le CLI GETH.

Pour être sur la même longueur d'onde, suivez toutes les étapes de l'[article précédent](https://medium.freecodecamp.org/ethereum-69-how-to-set-up-a-fully-synced-blockchain-node-in-10-mins-f6318d7aad40) d'abord.

Terminé ? Parfait.

À ce stade, vous savez :

* comment exécuter un nœud blockchain Ethereum entièrement synchronisé
* comment attacher la `console GETH`
* comment interroger le solde d'un compte Ethereum

```
geth attach ipc:/home/enchanter/.gophersland_ethereum_r1/geth.ipc 
```

```
eth.getBalance("0xceee57f2b700c2f37d1476a7974965e149fce2d4")
```

```
> 7500000000000000000
```

Je le fais, pourriez-vous penser, mais attendez une seconde Lukas... pourquoi `7.5 ETH` est affiché comme `7500000000000000000` dans la `console Geth` ?

### Ether vs Wei

La machine virtuelle Ethereum ne supporte pas les décimales ou les nombres à virgule. Apparemment, les calculs en finance sont plus faciles avec des entiers.

Par conséquent, pour pouvoir envoyer une fraction de 1 ETH, la fondation Ethereum a décidé de créer son propre système métrique où la plus petite unité serait 1 Wei, et 1 Ether est 1e18 Wei.

Mais ne vous inquiétez pas, il existe des outils qui peuvent faciliter votre vie. Par exemple, je recommande vivement le convertisseur en ligne Ether to Wei :

[https://etherconverter.online](https://etherconverter.online/)

Afin d'envoyer 15 $ d'Ether, où 1 ETH == 200 $ (le bon vieux temps...), vous effectueriez une transaction en envoyant 0.0740 ETH qui serait, et doit être représenté en Wei comme, 74000000000000000.

**Convertisseur en ligne Ether to Wei :**

![Image](https://cdn-media-1.freecodecamp.org/images/-X6USQnRm1wGPZSS-YeRAmi7DB83wPZatPzN)

**Aperçu du système métrique Ethereum :**

![Image](https://cdn-media-1.freecodecamp.org/images/QZtIr5o2rsnE7fSADFwq0m-GnMaAqUg8Wsqe)

La pratique mène à la maîtrise. Envoyons réellement 74000000000000000 Wei (15 $) à un autre compte.

### Envoyer de l'Ether à un autre compte en utilisant le CLI GETH

Dans un terminal, n'oubliez pas d'exécuter un nœud blockchain entièrement synchronisé :

```
geth --rinkeby --datadir=~/.gophersland_ethereum_r1 --port=30304 --cache=2048 --rpc --rpcport=8546 --rpcapi=eth,web3,net,personal --syncmode=fast
```

Dans un autre terminal, nous allons créer notre deuxième compte Ethereum, exactement comme dans la partie 1.

```
ls -la ~/.gophersland_ethereum_r1/keystore/> drwx------ 2 enchanter enchanter 4096 sep 24 15:36 .> drwx------ 4 enchanter enchanter 4096 sep 24 15:26 ..> -rw------- 1 enchanter enchanter  491 sep 24 15:36 
```

```
UTC--2018-09-24T13-36-43.069452577Z--ceee57f2b700c2f37d1476a7974965e149fce2d4geth --datadir=~/.gophersland_ethereum_r1 account new> INFO [09-24|15:36:33.566] Maximum peer count ETH=25 LES=0 total=25> Votre nouveau compte est verrouillé avec un mot de passe. Veuillez donner un mot de passe. N'oubliez pas ce mot de passe.
```

```
> Phrase de passe : > Répéter la phrase de passe : > Adresse : {7aa4a14286a25e3a275d7a122c23dc3c107a636a}ls -la ~/.gophersland_ethereum_r1/keystore/> drwx------ 2 enchanter enchanter 4096 oct 25 20:14 .> drwx------ 4 enchanter enchanter 4096 oct 25 19:48 ..> -rw------- 1 enchanter enchanter  491 sep 24 15:36 
```

```
UTC--2018-09-24T13-36-43.069452577Z--ceee57f2b700c2f37d1476a7974965e149fce2d4
```

Maintenant, attachons la console Geth au nœud blockchain actuellement en cours d'exécution comme nous l'avons fait dans l'article précédent afin de transférer 15 $ à ce compte nouvellement créé en exécutant la commande `eth.sendTransaction`.

```
geth attach ipc:/home/enchanter/.gophersland_ethereum_r1/geth.ipc 
```

```
eth.sendTransaction({from: "0xceee57f2b700c2f37d1476a7974965e149fce2d4",to: "0x7aa4a14286a25e3a275d7a122c23dc3c107a636a", value: "74000000000000000"})
```

**Erreur : authentification nécessaire : mot de passe ou déverrouillage.**

Vous devriez obtenir une erreur. Cela est dû au fait que l'envoi d'Ether est une "transaction", et une transaction change d'état, coûte du gaz et dépense des fonds. Ce qui signifie qu'elle doit être signée avec notre clé privée qui est stockée dans le **Keystore**. Afin de déchiffrer la clé, nous devons fournir un mot de passe, ou en d'autres termes, déverrouiller le compte.

Exécutez la commande suivante pour déverrouiller votre compte pour les 60 prochaines secondes, puis exécutez à nouveau la commande sendTransaction.

```
web3.personal.unlockAccount(web3.personal.listAccounts[0], null, 60) 
```

```
eth.sendTransaction({from: "0xceee57f2b700c2f37d1476a7974965e149fce2d4", to: "0x7aa4a14286a25e3a275d7a122c23dc3c107a636a", value: "74000000000000000"})
```

Nous aurions également pu passer le mot de passe comme deuxième argument au lieu de null. Mais cette méthode est plus sûre car votre mot de passe n'est que dans un tampon et n'est pas stocké dans un journal ou visible à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/LrxhDzbd71gAsfm-Jl545xh0Goc06CATzgmL)

**Cette fois, la commande a réussi et un reçu de hachage de transaction a été retourné ! Oh yeah !**

Comme nous sommes connectés au réseau Rinkeby, nous pouvons tirer parti de l'explorateur GUI Rinkeby pour vérifier l'état de cette transaction, le gaz dépensé, le prix du gaz, etc.

1. Ouvrez l'[explorateur](https://www.rinkeby.io/#explorer)
2. Collez le hachage du reçu de transaction dans la barre de recherche
3. Terminé, nous avons dépensé 21 000 de Gas (standard pour l'envoi de fonds) et la transaction a réussi !

![Image](https://cdn-media-1.freecodecamp.org/images/LC9XhANCXPxhEUGnp4kNCj7SSxc3JbBeRTiK)

Vous pouvez maintenant interroger les soldes des deux comptes et voir l'état modifié :

```
eth.getBalance("0xceee57f2b700c2f37d1476a7974965e149fce2d4") > 7425979000000000000 
```

```
eth.getBalance("0x7aa4a14286a25e3a275d7a122c23dc3c107a636a") > 74000000000000000
```

**Fonctionne à merveille.**

Félicitations ! Vous avez :

* appris la différence entre Ether et Wei et comment les convertir
* soumis votre première transaction sur le réseau de test global Ethereum, Rinkeby

Vous pouvez continuer à développer vos compétences en blockchain en [construisant une blockchain à partir de zéro en Go !](https://www.freecodecamp.org/news/build-a-blockchain-in-golang-from-scratch/)