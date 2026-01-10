---
title: Comment exécuter GETH depuis un conteneur Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-27T18:56:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-geth-from-a-docker-container-b6d30620ca74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QZk8YSNM8shw4Trn8YtvAA.png
tags:
- name: Blockchain
  slug: blockchain
- name: Docker
  slug: docker
- name: Ethereum
  slug: ethereum
- name: software
  slug: software
- name: 'tech '
  slug: tech
seo_title: Comment exécuter GETH depuis un conteneur Docker
seo_desc: 'By Vince Tabora

  Installing the Ethereum node client on a machine can be a tedious process. There
  is a simpler way this can be done using a Docker client. This is a guide for running
  the GETH (Ethereum-Go) node client from inside a Docker container. G...'
---

Par Vince Tabora

Installer le client de nœud Ethereum sur une machine peut être un processus fastidieux. Il existe une méthode plus simple pour le faire en utilisant un client Docker. Ce guide explique comment exécuter le client de nœud **GETH** (Ethereum-Go) depuis un conteneur Docker. GETH est l'implémentation en GoLang du protocole Ethereum. Il existe une image disponible à télécharger depuis le dépôt Docker Hub qui peut exécuter l'environnement.

Le site [**GoEthereum**](https://geth.ethereum.org/) liste les images disponibles suivantes avec leurs descriptions.

* `ethereum/client-go:latest` est la dernière version de développement de Geth
* `ethereum/client-go:stable` est la dernière version stable de Geth
* `ethereum/client-go:{version}` est la version stable de Geth à un numéro de version spécifique
* `ethereum/client-go:release-{version}` est la dernière version stable de Geth dans une famille de versions spécifique

Les ports suivants sont ouverts par défaut lors de l'exécution depuis le conteneur.

* `8545` TCP, utilisé par l'API JSON RPC basée sur HTTP
* `8546` TCP, utilisé par l'API JSON RPC basée sur WebSocket
* `30303` TCP et UDP, utilisé par le protocole P2P exécutant le réseau
* `30304` UDP, utilisé par la nouvelle couche de découverte de pairs du protocole P2P

Le logiciel client Docker doit être installé sur la machine à partir de laquelle vous allez exécuter le conteneur. Les conteneurs ne peuvent être exécutés que si vous avez le client Docker installé. Selon votre système d'exploitation, la version correcte du client sera nécessaire.

Il existe des versions distinctes pour Windows, Linux et MacOS. Le conteneur peut même être exécuté sur une instance Linux fonctionnant sur AWS, comme une installation Linux typique. Une fois le client Docker installé, la plateforme sous-jacente n'a pas d'importance. Les commandes seront les mêmes pour tous.

## Obtenir l'image

Ouvrez un **_terminal_** sur Linux ou MacOS, ou une **_invite de commande PowerShell_** depuis Windows. Dans l'invite de commande CLI, tapez la commande suivante :

**docker pull ethereum/client-go**

Cela télécharge l'image Docker depuis le dépôt hub où elle a été uploadée par les développeurs Ethereum. Une fois que vous avez émis cette commande, le texte suivant ou similaire devrait s'afficher :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-48.png)

J'ai déjà téléchargé l'image, donc le texte peut sembler différent. Lorsque vous émettez la commande pull, elle téléchargera toujours la dernière image disponible, ce qui est une bonne pratique.

## Exécuter le nœud

Maintenant, vous pouvez démarrer le nœud en émettant la commande suivante :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-49.png)

Nous voulons exécuter le nœud avec les options de drapeau **-i** et **-t** pour afficher les informations de notre conteneur. Le **-p** indique l'utilisation d'un numéro de port, dans ce cas 30303. De même, la commande peut être exécutée sans les drapeaux et elle utilisera simplement les ports et paramètres par défaut depuis l'intérieur du conteneur.

Les informations suivantes devraient apparaître depuis le terminal.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-51.png)

La ligne INFO qui montre la configuration révèle ce que le logiciel client de nœud a installé. Le client de nœud exécute la dernière version (au moment de la publication) du logiciel Ethereum qui est Constantinople, une fourchette dure activée par l'utilisateur à la hauteur de bloc 7280000.

Lors de l'exécution en API JSON-RPC :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-52.png)

Notez que l'exécution de l'option rpcaddr "0.0.0.0" n'est pas sécurisée, car vous ouvrez votre nœud à tout le trafic. Si votre portefeuille ETH était déverrouillé, un pirate pourrait accéder à votre nœud de cette manière et voler vos pièces. Je ne couvre pas la sécurité dans cet article, mais vous pouvez en lire plus à ce sujet [ici](https://medium.com/coinmonks/securing-your-ethereum-nodes-from-hackers-8b7d5bac8986) (sécuriser les ports RPC de votre nœud GETH). Respectez toujours les pratiques sûres et recommandées.

Si le nœud affiche ce qui suit dans la ligne INFO, il y aura un problème :

config="{ChainID: 1 Homestead: 1150000 DAO: 1920000 DAOSupport: true EIP150: 2463000 EIP155: 2675000 EIP158: 2675000 Byzantium: 4370000 Constantinople: <nil> Engine: ethash}"

Le Constantinople: <nil> indique que le logiciel n'a pas été mis à jour. Il n'y a également aucune ligne pour ConstantinopleFix, qui apparaît dans la configuration correcte.

## Données persistantes

Pour des données de blockchain persistantes, les volumes de données Docker doivent être utilisés avec l'option **-v**. Le `/path/on/host` doit être remplacé par l'emplacement que vous spécifiez. Pour cela, la commande suivante doit être utilisée :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-54.png)

## Vérification du statut du nœud

Vous pouvez vérifier le statut du conteneur en utilisant la commande suivante :

**docker ps**

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-55.png)

Cela affichera l'ID du conteneur avec le nom de l'image, le statut et les ports utilisés.

```

#Ce sont les commandes à exécuter depuis le CLI Docker pour exécuter le client de nœud Ethereum Go

#OBTENIR L'IMAGE

docker pull ethereum/client-go


#EXÉCUTER LE NŒUD

docker run -it -p 30303:30303 ethereum/client-go

#EXÉCUTER LE NŒUD EN UTILISANT L'API

docker run -it -p 8545:8545 -p 30303:30303 ethereum/client-go --rpc --rpcaddr "0.0.0.0"

#Note, avertissement concernant l'utilisation de --rpcaddr "0.0.0.0" dans un environnement en direct. C'est une manière non sécurisée d'ouvrir votre nœud.
#Il existe différentes manières de sécuriser vos ports, mais c'est une chose à noter si vous prévoyez d'utiliser l'API.


#DONNÉES PERSISTANTES

docker run -it -p 30303:30303 -v /path/on/host:/root/.ethereum ethereum/client-go
```



---

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-56.png)
_Exécuter GETH depuis un conteneur Docker_

Notez que cela ne mine pas automatiquement l'ETH. C'est un processus différent. Pour obtenir un accès rapide à la blockchain Ethereum, c'est le but de l'exécution de GETH.

Pour le code source complet, visitez : [https://github.com/Play3rZer0/GETHDocker.git](https://github.com/Play3rZer0/GETHDocker.git)