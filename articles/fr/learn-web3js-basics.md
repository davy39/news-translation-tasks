---
title: Apprendre les bases de Web3.js – Développement Ethereum pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-27T22:39:24.000Z'
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: Web3
  slug: web3
originalURL: https://freecodecamp.org/news/learn-web3js-basics
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Learn-Web3.js-Basics---Ethereum-Development.png
seo_title: Apprendre les bases de Web3.js – Développement Ethereum pour débutants
---

Par Oluwatise Okuwobi

Ethereum est l'un des principaux pionniers de l'écosystème décentralisé. Et Web3.js est un outil essentiel si vous travaillez sur des projets basés sur Ethereum. 

Pour comprendre pleinement pourquoi cet outil est important, nous devons d'abord prendre une plongée plus profonde dans le développement Ethereum.

Prenez votre café, jeune passionné de Web3. Nous partons pour un voyage qui changera votre carrière Web3 pour toujours.

## Prérequis

Avant de pouvoir continuer avec ce tutoriel, vous devez comprendre les bases de JavaScript et être capable d'installer des packages npm. 

Si vous avez déjà travaillé avec JavaScript, le reste de ce tutoriel devrait être un jeu d'enfant. 

## Qu'est-ce que le développement Ethereum ?

Ethereum est une plateforme blockchain open-source décentralisée qui permet aux développeurs de construire des applications décentralisées, communément appelées dApps. Ces dApps sont construites sur la blockchain Ethereum, exploitant certaines des fonctionnalités principales du réseau Ethereum. 

Ethereum est écrit en Solidity, qui est le langage de programmation principal utilisé dans l'écosystème Ethereum. Vous pouvez utiliser Solidity pour concevoir des contrats intelligents, qui sont essentiellement des contrats auto-exécutants qui alimentent de nombreuses dApps.

Si vous souhaitez travailler dans le développement Ethereum, comprendre les contrats intelligents est extrêmement important. 

Les contrats intelligents contiennent les termes de l'accord entre l'acheteur et le vendeur qui sont directement écrits dans les lignes de code. Ce code est écrit en Solidity, qui ne peut exister que dans le réseau blockchain.

Pour devenir un développeur Ethereum, vous allez travailler principalement autour du réseau, en construisant des contrats intelligents et des dApps. 

Parlons des outils dont vous allez avoir besoin :

* Solidity
* Ether.js
* JavaScript/React pour l'interaction visuelle front-end

## Le monde de Web3.js

Maintenant que vous avez une idée de ce qu'est le développement Ethereum, nous pouvons commencer à comprendre un peu mieux Web3.js. 

Web3.js est une collection de bibliothèques qui vous permettent d'interagir avec un nœud Ethereum local ou distant, en utilisant HTTP, IPC ou Web Sockets (qui est mon préféré personnel). Il est écrit en JavaScript, et pour faire simple, il vous permet d'interagir avec la blockchain de manière plus efficace.

En lisant les données de la blockchain, vous serez en mesure de faire des transactions et de déployer des contrats intelligents en direct sur le mainnet.

## Comment installer Web3.js

Web3.js peut accéder aux informations de la blockchain à la fois depuis le back-end et le front-end pour effectuer des transactions et déployer des contrats intelligents. 

Vous allez avoir besoin de Node.js, que vous pouvez facilement [télécharger depuis le site officiel](https://nodejs.org/en/). Le processus d'installation est assez simple. 

Après avoir installé Node et npm (le gestionnaire de packages officiel pour Node) avec succès, ouvrez votre ligne de commande dans le dossier racine de votre projet et tapez la commande suivante :

```javascript
npm install web3 --save
```

Ensuite, vous pourrez importer Web3.js dans un script Node en utilisant ce code simple :

```javascript
const Web3 = require("web3")
```

Nous avons verrouillé une partie des éléments difficiles. Maintenant, nous devons simplement faire en sorte que notre projet communique directement avec la blockchain. 

Pour initier notre fournisseur Web3, nous devons instancier, ce qui signifie simplement créer une instance Web3, et passer un constructeur à l'URL du fournisseur. 

Dans ce cas, nous devrons trouver un nœud Ethereum auquel nous pouvons nous connecter et commencer à créer de la magie. 

Il existe plusieurs fournisseurs de nœuds comme Alchemy, Chainstack et Moralis, et il y a beaucoup de documentation concernant l'obtention d'un accès direct.

Vous pouvez également utiliser l'instance Ganache, qui vous aidera essentiellement à configurer l'environnement pour tout ce dont vous avez besoin pour travailler dans votre environnement local.

Pour comprendre [comment configurer Ganache](https://medium.com/coinmonks/get-started-with-building-ethereum-dapps-and-smart-contracts-d86b9f7bd1c), vous pouvez lire le guide lié qui couvre tout ce que vous devez savoir.

Vous placez simplement ce qui suit sous votre code comme ceci :

```javascript
const Web3 = require("web3")
const web3 = new Web3("http://localhost:8545")
```

Pour tester que vous avez tout configuré avec succès, vous pouvez écrire un code simple pour obtenir le numéro du dernier bloc sur la blockchain :

```javascript
var Web3 = require("web3")
const web3 = new Web3("http://localhost:8545")

web3.eth.getBlockNumber(function (error, result) {
  console.log(result)
})

```

Cette fonction accepte simplement un rappel en tant que paramètre, puis imprime le résultat sous forme d'entier. L'exécution de ceci vous donnera simplement un numéro de bloc sur votre console. 

Il existe de nombreuses autres fonctions que vous pouvez utiliser. La [documentation officielle](https://docs.web3js.org/) de web3 fournit une liste complète des fonctions que vous pouvez apprendre et essayer.

## Conclusion

Si vous souhaitez vous lancer dans le développement Ethereum, Web3.js sera une partie vitale de votre stack. Tout au long de votre parcours, vous allez interagir plus fréquemment avec le nœud Ethereum et Web3.js sera très utile.

Il existe d'autres alternatives comme Ether.js, qui s'efforcent également de fournir une bibliothèque complète capable d'interagir avec le nœud Ethereum. Mais Web3 est connu pour avoir un réseau de support plus large, une communauté de développeurs plus importante et une documentation plus mature à laquelle vous pouvez vous référer pour tout type de problème.

Espérons que cet article vous a donné toutes les informations nécessaires pour commencer votre parcours Ethereum. Je suis disponible sur [Twitter](https://www.twitter.com/tiseysoft), si vous avez des questions.