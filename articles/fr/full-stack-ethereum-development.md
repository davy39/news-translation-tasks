---
title: Le guide complet du développement Ethereum Full Stack
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-17T20:45:00.000Z'
originalURL: https://freecodecamp.org/news/full-stack-ethereum-development
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/full-stack-ethereum-article.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: ethereum blockchain
  slug: ethereum-blockchain
seo_title: Le guide complet du développement Ethereum Full Stack
seo_desc: 'By Nader Dabit

  In this article, you''ll learn how to build full stack dApps with React, Ethers.js,
  Solidity, and Hardhat.

  You can find the code for this project here. The video course for this tutorial
  is here.

  I recently joined Edge & Node as a Devel...'
---

Par Nader Dabit

Dans cet article, vous apprendrez à créer des dApps full stack avec React, Ethers.js, Solidity et Hardhat.

Vous pouvez trouver le code de ce projet [ici](https://github.com/dabit3/full-stack-ethereum). Le cours vidéo pour ce tutoriel est [ici](https://www.youtube.com/watch?v=a0osIaAOFSE).

J'ai récemment rejoint [Edge & Node](https://twitter.com/edgeandnode) en tant qu'ingénieur en relations développeurs (Developer Relations Engineer) et j'ai approfondi le développement de smart contracts avec Ethereum. J'ai opté pour ce que je considère être la meilleure stack pour construire des dApps full stack avec Solidity :

* Framework Client – **React**
* Environnement de développement Ethereum – [**Hardhat**](https://hardhat.org/)
* Bibliothèque client Web Ethereum – [**Ethers.js**](https://docs.ethers.io/v5/)
* Couche API – [The Graph Protocol](https://thegraph.com/)

Mais j'ai rencontré un problème en essayant de comprendre tout cela. Bien qu'il existe une assez bonne documentation pour chacun de ces outils individuellement, il n'y a pas grand-chose pour vous aider à les assembler et à comprendre comment ils fonctionnent les uns avec les autres.

Il existe d'excellents boilerplates comme [scaffold-eth](https://github.com/austintgriffith/scaffold-eth) (qui inclut également Ethers, Hardhat et The Graph), mais ils peuvent être un peu trop complexes pour les personnes qui débutent.

Je voulais un guide de bout en bout pour me montrer comment construire des applications Ethereum full stack en utilisant les ressources, bibliothèques et outils les plus récents.

Voici ce qui m'intéressait :

1. Comment créer, déployer et tester des smart contracts Ethereum sur des réseaux locaux, de test et mainnet.
2. Comment basculer entre les environnements / réseaux de développement local, de test et de production.
3. Comment se connecter et interagir avec les contrats en utilisant divers environnements à partir d'un front-end comme React, Vue, Svelte ou Angular.

Après avoir passé du temps à comprendre tout cela, j'ai finalement réussi à mettre en place la stack dont je suis vraiment satisfait. J'ai alors pensé qu'il serait utile de rédiger un guide sur la construction et le test d'une application Ethereum full stack avec cette stack.

J'espère que ce guide sera utile non seulement pour d'autres personnes intéressées par cette stack, mais aussi pour moi-même comme référence future. Voici cette référence.

## Les technologies que nous utiliserons

Passons en revue les éléments principaux que nous utiliserons et comment ils s'intègrent dans la stack.

### 1. Environnement de développement Ethereum

Lors de la création de smart contracts, vous aurez besoin d'un moyen de déployer vos contrats, d'exécuter des tests et de déboguer le code Solidity sans avoir à gérer des environnements réels.

Vous aurez également besoin d'un moyen de compiler votre code Solidity en un code pouvant être exécuté dans une application côté client – dans notre cas, une application React. Nous en apprendrons davantage sur ce fonctionnement un peu plus tard.

Hardhat est un environnement de développement Ethereum et un framework conçu pour le développement full stack, et c'est le framework que j'utiliserai pour ce tutoriel.

D'autres outils similaires dans l'écosystème sont [Ganache](https://www.trufflesuite.com/ganache) et [Truffle](https://www.trufflesuite.com/).

### 2. Bibliothèque client Web Ethereum

Dans notre application React, nous aurons besoin d'un moyen d'interagir avec les smart contracts qui ont été déployés. Nous aurons besoin d'un moyen de lire des données ainsi que d'envoyer de nouvelles transactions.

[ethers.js](https://docs.ethers.io/v5/) vise à être une bibliothèque complète et compacte pour interagir avec la blockchain Ethereum et son écosystème à partir d'applications JavaScript côté client comme React, Vue, Angular ou Svelte. C'est la bibliothèque que nous utiliserons.

Une autre option populaire dans l'écosystème est [web3.js](https://web3js.readthedocs.io/en/v1.3.4/)

### 3. Metamask

[Metamask](https://metamask.io/download.html) vous aide à gérer les comptes et à connecter l'utilisateur actuel à la blockchain. MetaMask permet aux utilisateurs de gérer leurs comptes et leurs clés de différentes manières tout en les isolant du contexte du site.

Une fois qu'un utilisateur a connecté son portefeuille MetaMask, vous, en tant que développeur, pouvez interagir avec l'API Ethereum disponible globalement (`window.ethereum`) qui identifie les utilisateurs de navigateurs compatibles web3 (comme les utilisateurs de MetaMask). Chaque fois que vous demandez une signature de transaction, MetaMask sollicitera l'utilisateur de manière compréhensible.

### 4. React

React est une bibliothèque JavaScript front-end pour la création d'applications Web, d'interfaces utilisateur et de composants UI. Elle est maintenue par Facebook et de nombreux développeurs et entreprises individuels.

React et son vaste écosystème de méta-frameworks comme [Next.js](https://nextjs.org/), [Gatsby](https://www.gatsbyjs.com/), [Redwood](https://redwoodjs.com/), [Blitz.js](https://blitzjs.com/) et d'autres permettent tous types de cibles de déploiement, y compris les SPA traditionnelles, les générateurs de sites statiques, le rendu côté serveur et une combinaison des trois.

React semble continuer à dominer l'espace front-end, et je pense qu'il continuera à le faire dans un avenir proche et peut-être au-delà.

### 5. The Graph

Pour la plupart des applications construites sur des blockchains comme Ethereum, il est difficile et chronophage de lire les données directement depuis la chaîne. Par le passé, on voyait donc des personnes et des entreprises construire leur propre serveur d'indexation centralisé et servir les requêtes API à partir de ces serveurs. Cela nécessite beaucoup de ressources d'ingénierie et de matériel, et brise les propriétés de sécurité requises pour la décentralisation.

The Graph est un protocole d'indexation pour interroger les données de la blockchain qui vous permet de créer des applications entièrement décentralisées. Il résout ce problème en exposant une couche de requête GraphQL riche que les applications peuvent consommer.

Dans ce guide, nous ne construirons pas de subgraph pour notre application, mais nous le ferons dans un futur tutoriel.

## Ce que nous allons construire

Dans ce tutoriel, nous allons construire, déployer et nous connecter à quelques smart contracts de base :

1. Un contrat pour créer et mettre à jour un message sur la blockchain Ethereum.
2. Un contrat pour minter des jetons (tokens), qui permet au propriétaire du contrat d'envoyer des jetons à d'autres et de lire les soldes de jetons, et permet aux propriétaires des nouveaux jetons de les envoyer également à d'autres.

Nous construirons également un front-end React qui permettra à un utilisateur de :

1. Lire le message (greeting) du contrat déployé sur la blockchain.
2. Mettre à jour le message.
3. Envoyer les jetons nouvellement mintés de leur adresse vers une autre adresse.
4. Une fois que quelqu'un a reçu des jetons, lui permettre de les envoyer également à quelqu'un d'autre.
5. Lire le solde de jetons du contrat déployé sur la blockchain.

### Prérequis

1. Node.js installé sur votre machine locale.
2. Extension Chrome [MetaMask](https://metamask.io/) installée dans votre navigateur.

Vous n'avez pas besoin de posséder d'Ethereum pour ce guide car nous utiliserons de l'Ether factice / de test sur un réseau de test pendant tout le tutoriel.

## Comment démarrer avec create-react-app

Pour commencer, nous allons créer une nouvelle application React :

```sh
npx create-react-app react-dapp

```

Ensuite, déplacez-vous dans le nouveau répertoire et installez [`ethers.js`](https://docs.ethers.io/v5/) et [`hardhat`](https://github.com/nomiclabs/hardhat) en utilisant soit **NPM**, soit **Yarn** :

```
npm install ethers hardhat @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers

```

## Comment installer et configurer un environnement de développement Ethereum

Ensuite, initialisez un nouvel environnement de développement Ethereum avec Hardhat :

```sh
npx hardhat

? What do you want to do? Create a sample project
? Hardhat project root: <Choisissez le chemin par défaut>

```

Vous devriez maintenant voir les artefacts suivants créés pour vous dans votre répertoire racine :

* **hardhat.config.js** – L'intégralité de votre configuration Hardhat (c'est-à-dire votre configuration, vos plugins et vos tâches personnalisées) est contenue dans ce fichier.
* **scripts** – Un dossier contenant un script nommé **sample-script.js** qui déploiera votre smart contract lors de son exécution.
* **test** – Un dossier contenant un exemple de script de test.
* **contracts** – Un dossier contenant un exemple de smart contract Ethereum.

En raison d'un [problème de configuration de MetaMask](https://hardhat.org/metamask-issue.html), nous devons mettre à jour l'ID de chaîne (chain ID) dans notre configuration HardHat à **1337**. Nous devons également mettre à jour l'emplacement des [artefacts](https://hardhat.org/guides/compile-contracts.html#artifacts) pour nos contrats compilés afin qu'ils se trouvent dans le répertoire **src** de notre application React.

Pour effectuer ces mises à jour, ouvrez **hardhat.config.js** et mettez à jour le `module.exports` comme ceci :

```javascript
module.exports = {
  solidity: "0.8.3",
  paths: {
    artifacts: './src/artifacts',
  },
  networks: {
    hardhat: {
      chainId: 1337
    }
  }
};

```

## Notre smart contract

Ensuite, jetons un coup d'œil à l'exemple de contrat que nous avons dans **contracts/Greeter.sol** :

```solidity
//SPDX-License-Identifier: MIT
pragma solidity ^0.7.0;

import "hardhat/console.sol";


contract Greeter {
  string greeting;

  constructor(string memory _greeting) {
    console.log("Déploiement d'un Greeter avec le message :", _greeting);
    greeting = _greeting;
  }

  function greet() public view returns (string memory) {
    return greeting;
  }

  function setGreeting(string memory _greeting) public {
    console.log("Changement du message de '%s' à '%s'", greeting, _greeting);
    greeting = _greeting;
  }
}

```

Il s'agit d'un smart contract très basique. Une fois déployé, il définit une variable `greeting` et expose une fonction (`greet`) qui peut être appelée pour renvoyer le message.

Il expose également une fonction qui permet à un utilisateur de mettre à jour le message (`setGreeting`). Lorsqu'ils seront déployés sur la blockchain Ethereum, ces méthodes seront disponibles pour qu'un utilisateur puisse interagir avec elles.

Apportons une petite modification au smart contract. Puisque nous avons défini la version Solidity de notre compilateur à `0.8.3` dans **hardhat.config.js**, assurons-nous également de mettre à jour notre contrat pour utiliser la même version de Solidity :

```solidity
// contracts/Greeter.sol
pragma solidity ^0.8.3;

```

### Comment lire et écrire sur la blockchain Ethereum

Il existe deux façons d'interagir avec un smart contract : la lecture ou l'écriture / transactions. Dans notre contrat, `greet` peut être considéré comme une lecture, et `setGreeting` peut être considéré comme une écriture / transactionnelle.

Lors de l'écriture ou de l'initialisation d'une transaction, vous devez payer pour que la transaction soit inscrite sur la blockchain. Pour ce faire, vous devez payer du [gas](https://www.investopedia.com/terms/g/gas-ethereum.asp#:~:text=What%20Is%20Gas%20(Ethereum)%3F,on%20the%20Ethereum%20blockchain%20platform), qui est le frais ou le prix requis pour mener à bien une transaction et exécuter un contrat sur la blockchain Ethereum.

Tant que vous ne faites que lire la blockchain et que vous ne changez ou ne mettez rien à jour, vous n'avez pas besoin d'effectuer une transaction et il n'y aura aucun frais de gas. La fonction que vous appelez est alors exécutée uniquement par le nœud auquel vous êtes connecté, vous n'avez donc pas besoin de payer de gas et la lecture est gratuite.

Depuis notre application React, nous interagirons avec le smart contract en utilisant une combinaison de la bibliothèque `ethers.js`, de l'adresse du contrat et de l'interface [ABI](https://docs.soliditylang.org/en/v0.5.3/abi-spec.html) qui sera créée à partir du contrat par Hardhat.

Qu'est-ce qu'une ABI ? ABI signifie Application Binary Interface (interface binaire d'application). Vous pouvez la considérer comme l'interface entre votre application côté client et la blockchain Ethereum où le smart contract avec lequel vous allez interagir est déployé.

Les ABI sont généralement compilées à partir de smart contracts Solidity par un framework de développement comme Hardhat. Vous pouvez également souvent trouver les ABI d'un smart contract sur [Etherscan](https://etherscan.io/)

### Comment compiler l'ABI

Maintenant que nous avons passé en revue le smart contract de base et que nous savons ce que sont les ABI, compilons une ABI pour notre projet.

Pour ce faire, allez dans la ligne de commande et exécutez la commande suivante :

```sh
npx hardhat compile

```

Maintenant, vous devriez voir un nouveau dossier nommé **artifacts** dans le répertoire **src**. Le fichier **artifacts/contracts/Greeter.json** contient l'ABI comme l'une de ses propriétés. Lorsque nous aurons besoin d'utiliser l'ABI, nous pourrons l'importer depuis notre fichier JavaScript :

```javascript
import Greeter from './artifacts/contracts/Greeter.sol/Greeter.json'

```

Nous pouvons ensuite référencer l'ABI comme ceci :

```
console.log("ABI du Greeter : ", Greeter.abi)

```

> Notez qu'Ethers.js permet également des [ABI lisibles par l'homme](https://blog.ricmoo.com/human-readable-contract-abis-in-ethers-js-141902f4d917), mais nous n'aborderons pas cela dans ce tutoriel.

### Comment déployer et utiliser un réseau local / une blockchain

Ensuite, déployons notre smart contract sur une blockchain locale afin de pouvoir le tester.

Pour déployer sur le réseau local, vous devez d'abord démarrer le nœud de test local. Pour ce faire, ouvrez le terminal et exécutez la commande suivante :

```sh
npx hardhat node

```

Lorsque nous exécutons cette commande, vous devriez voir une liste d'adresses et de clés privées.

![Adresses des nœuds Hardhat](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/e176nc82ik77hei3a48s.jpg)

Il s'agit de 20 comptes et adresses de test créés pour nous que nous pouvons utiliser pour déployer et tester nos smart contracts. Chaque compte est également crédité de 10 000 Ether factices. Dans un instant, nous apprendrons comment importer le compte de test dans MetaMask afin de pouvoir l'utiliser.

Ensuite, nous devons déployer le contrat sur le réseau de test. Mettez d'abord à jour le nom de **scripts/sample-script.js** en **scripts/deploy.js**.

Nous pouvons maintenant exécuter le script de déploiement et indiquer au terminal que nous souhaitons déployer sur notre réseau local :

```sh
npx hardhat run scripts/deploy.js --network localhost

```

Une fois ce script exécuté, le smart contract devrait être déployé sur le réseau de test local et nous devrions alors pouvoir commencer à interagir avec lui.

> Lorsque le contrat a été déployé, il a utilisé le premier compte créé lors du démarrage du réseau local.

Si vous regardez la sortie du terminal, vous devriez voir quelque chose comme ceci :

```sh
Greeter deployed to: 0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0

```

Cette adresse est celle que nous utiliserons dans notre application client pour communiquer avec le smart contract. Gardez cette adresse à portée de main car nous en aurons besoin lors de la connexion depuis l'application client.

Pour envoyer des transactions au smart contract, nous devrons connecter notre portefeuille MetaMask en utilisant l'un des comptes créés lors de l'exécution de `npx hardhat node`. Dans la liste des contrats affichée par le terminal, vous devriez voir à la fois un **numéro de compte** (Account number) et une **clé privée** (Private Key) :

```bash
➜  react-defi-stack git:(main) npx hardhat node
Started HTTP and WebSocket JSON-RPC server at http://127.0.0.1:8545/

Accounts
========
Account #0: 0xf39fd6e51aad88f6f4ce6ab8827279cfffb92266 (10000 ETH)
Private Key: 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80

...

```

Nous pouvons importer ce compte dans MetaMask afin de commencer à utiliser une partie de l'Ether factice disponible. Pour ce faire, ouvrez d'abord MetaMask et mettez à jour le réseau pour qu'il soit Localhost 8545 :

![MetaMask Localhost](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qnbsbcm4y1md6cwjttpx.jpg)

Ensuite, dans MetaMask, cliquez sur **Importer un compte** (Import Account) dans le menu des comptes :

![Importer un compte](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/n7vbzlov869gwk9rtwl1.jpg)

Copiez puis collez l'une des **clés privées** affichées par le terminal et cliquez sur **Importer**. Une fois le compte importé, vous devriez voir l'Ether sur le compte :

![Compte importé](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/x5lob4yug3jznhy9z0qt.jpg)

Maintenant que nous avons déployé notre smart contract et configuré notre compte, nous pouvons commencer à interagir avec lui depuis l'application React.

### Comment connecter le client React

Dans ce tutoriel, nous n'allons pas nous soucier de construire une belle interface utilisateur avec CSS et tout le reste – nous nous concentrons à 100 % sur les fonctionnalités de base pour vous permettre d'être opérationnel. À partir de là, vous pourrez l'améliorer visuellement si vous le souhaitez.

Ceci étant dit, passons en revue les deux objectifs que nous attendons de notre application React :

1. Récupérer la valeur actuelle de `greeting` depuis le smart contract.
2. Permettre à un utilisateur de mettre à jour la valeur de `greeting`.

Alors, comment accomplir cela ? Voici les étapes à suivre :

1. Créer un champ de saisie et un état local pour gérer la valeur de la saisie (pour mettre à jour le `greeting`).
2. Permettre à l'application de se connecter au compte MetaMask de l'utilisateur pour signer les transactions.
3. Créer des fonctions pour lire et écrire dans le smart contract.

Pour ce faire, ouvrez `src/App.js` et mettez-le à jour avec le code suivant, en définissant la valeur de `greeterAddress` avec l'adresse de votre smart contract :

```js
import './App.css';
import { useState } from 'react';
import { ethers } from 'ethers'
import Greeter from './artifacts/contracts/Greeter.sol/Greeter.json'

// Mettre à jour avec l'adresse du contrat affichée dans le terminal lors du déploiement 
const greeterAddress = "votre-adresse-de-contrat"

function App() {
  // stocker le message dans l'état local
  const [greeting, setGreetingValue] = useState()

  // demander l'accès au compte MetaMask de l'utilisateur
  async function requestAccount() {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
  }

  // appeler le smart contract, lire la valeur actuelle du message
  async function fetchGreeting() {
    if (typeof window.ethereum !== 'undefined') {
      const provider = new ethers.providers.Web3Provider(window.ethereum)
      const contract = new ethers.Contract(greeterAddress, Greeter.abi, provider)
      try {
        const data = await contract.greet()
        console.log('data: ', data)
      } catch (err) {
        console.log("Erreur : ", err)
      }
    }    
  }

  // appeler le smart contract, envoyer une mise à jour
  async function setGreeting() {
    if (!greeting) return
    if (typeof window.ethereum !== 'undefined') {
      await requestAccount()
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner()
      const contract = new ethers.Contract(greeterAddress, Greeter.abi, signer)
      const transaction = await contract.setGreeting(greeting)
      await transaction.wait()
      fetchGreeting()
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={fetchGreeting}>Récupérer le message</button>
        <button onClick={setGreeting}>Définir le message</button>
        <input onChange={e => setGreetingValue(e.target.value)} placeholder="Définir le message" />
      </header>
    </div>
  );
}

export default App;

```

Pour tester, lancez le serveur React :

```sh
npm start

```

Lorsque l'application se charge, vous devriez pouvoir récupérer le message actuel et l'afficher dans la console. Vous devriez également pouvoir mettre à jour le message en signant le contrat avec votre portefeuille MetaMask et en dépensant l'Ether factice.

![Définition et récupération de la valeur du message](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/9a57jbzrwylr2l0rujxm.png)

### Comment déployer et utiliser un réseau de test en direct

Il existe plusieurs réseaux de test Ethereum comme Ropsten, Rinkeby ou Kovan sur lesquels nous pouvons également déployer afin d'avoir une version publiquement accessible de notre contrat sans avoir à le déployer sur le mainnet.

Dans ce tutoriel, nous déploierons sur le réseau de test **Ropsten**.

Pour commencer, mettez d'abord à jour votre portefeuille MetaMask pour vous connecter au réseau Ropsten.

![Réseau Ropsten](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/k85gplgp26wp58l95bhr.jpg)

Ensuite, envoyez-vous de l'Ether de test à utiliser pendant le reste de ce tutoriel en visitant [ce faucet de test](https://faucet.ropsten.be/).

Nous pouvons accéder à Ropsten (ou à n'importe quel autre réseau de test) en nous inscrivant à un service comme [Infura](https://infura.io/dashboard/ethereum/cbdf7c5eee8b4e2b91e76b77ffd34533/settings) ou [Alchemy](https://www.alchemyapi.io/) (j'utilise Infura pour ce tutoriel).

Une fois que vous avez créé l'application dans Infura ou Alchemy, vous recevrez un point de terminaison (endpoint) qui ressemble à ceci :

```
https://ropsten.infura.io/v3/votre-id-de-projet

```

Assurez-vous de configurer les **ADRESSES ETHEREUM EN LISTE D'AUTORISATION** (ALLOWLIST) dans la configuration de l'application Infura ou Alchemy pour inclure l'adresse du portefeuille à partir duquel vous allez déployer.

Pour déployer sur le réseau de test, nous devons mettre à jour notre configuration Hardhat avec quelques informations réseau supplémentaires. L'une des choses que nous devons définir est la clé privée du portefeuille à partir duquel nous allons déployer.

Pour obtenir la clé privée, vous pouvez l'exporter depuis MetaMask.

![Exporter la clé privée](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/deod3d6qix8us12t17i4.jpg)

> Je suggère de ne pas coder cette valeur en dur dans votre application, mais de la définir plutôt comme une variable d'environnement.

Ensuite, ajoutez une propriété `networks` avec la configuration suivante :

```js
module.exports = {
  defaultNetwork: "hardhat",
  paths: {
    artifacts: './src/artifacts',
  },
  networks: {
    hardhat: {},
    ropsten: {
      url: "https://ropsten.infura.io/v3/votre-id-de-projet",
      accounts: [`0x${votre-cle-privee}`]
    }
  },
  solidity: "0.7.3",
};

```

Pour déployer, exécutez le script suivant :

```sh
npx hardhat run scripts/deploy.js --network ropsten

```

Une fois votre contrat déployé, vous devriez pouvoir commencer à interagir avec lui. Vous devriez maintenant pouvoir voir le contrat en direct sur l'[explorateur de testnet Etherscan Ropsten](https://ropsten.etherscan.io/)

## Comment minter des jetons

L'un des cas d'utilisation les plus courants des smart contracts est la création de jetons (tokens). Voyons comment nous pouvons faire cela. Puisque nous en savons un peu plus sur le fonctionnement de tout cela, nous irons un peu plus vite.

Dans le répertoire principal **contracts**, créez un nouveau fichier nommé **Token.sol**.

Ensuite, mettez à jour **Token.sol** avec le smart contract suivant :

```solidity
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

import "hardhat/console.sol";

contract Token {
  string public name = "Nader Dabit Token";
  string public symbol = "NDT";
  uint public totalSupply = 1000000;
  mapping(address => uint) balances;

  constructor() {
    balances[msg.sender] = totalSupply;
  }

  function transfer(address to, uint amount) external {
    require(balances[msg.sender] >= amount, "Pas assez de jetons");
    balances[msg.sender] -= amount;
    balances[to] += amount;
  }

  function balanceOf(address account) external view returns (uint) {
    return balances[account];
  }
}

```

> Notez que ce contrat de jeton est uniquement à des fins de démonstration et n'est pas conforme à la norme [ERC20](https://eips.ethereum.org/EIPS/eip-20). Nous aborderons les jetons ERC20 plus tard.

Ce contrat créera un nouveau jeton appelé "Nader Dabit Token" et fixera l'offre à 1 000 000.

Ensuite, compilez ce contrat :

```sh
npx hardhat compile

```

Maintenant, mettez à jour le script de déploiement dans **scripts/deploy.js** pour inclure ce nouveau contrat Token :

```javascript
const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();

  console.log(
    "Déploiement des contrats avec le compte :",
    deployer.address
  );
  
  const Greeter = await hre.ethers.getContractFactory("Greeter");
  const greeter = await Greeter.deploy("Hello, World!");

  const Token = await hre.ethers.getContractFactory("Token");
  const token = await Token.deploy();
  
  await greeter.deployed();
  await token.deployed();

  console.log("Greeter déployé à :", greeter.address);
  console.log("Token déployé à :", token.address);
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error(error);
    process.exit(1);
  });

```

Maintenant, nous pouvons déployer ce nouveau contrat sur le réseau local ou Ropsten :

```sh
npx hardhat run scripts/deploy.js --network localhost

```

Une fois le contrat déployé, vous pouvez commencer à envoyer ces jetons à d'autres adresses.

Pour ce faire, mettons à jour le code client dont nous aurons besoin pour faire fonctionner cela :

```javascript
import './App.css';
import { useState } from 'react';
import { ethers } from 'ethers'
import Greeter from './artifacts/contracts/Greeter.sol/Greeter.json'
import Token from './artifacts/contracts/Token.sol/Token.json'

const greeterAddress = "votre-adresse-de-contrat"
const tokenAddress = "votre-adresse-de-contrat"

function App() {
  const [greeting, setGreetingValue] = useState()
  const [userAccount, setUserAccount] = useState()
  const [amount, setAmount] = useState()

  async function requestAccount() {
    await window.ethereum.request({ method: 'eth_requestAccounts' });
  }

  async function fetchGreeting() {
    if (typeof window.ethereum !== 'undefined') {
      const provider = new ethers.providers.Web3Provider(window.ethereum)
      console.log({ provider })
      const contract = new ethers.Contract(greeterAddress, Greeter.abi, provider)
      try {
        const data = await contract.greet()
        console.log('data: ', data)
      } catch (err) {
        console.log("Erreur : ", err)
      }
    }    
  }

  async function getBalance() {
    if (typeof window.ethereum !== 'undefined') {
      const [account] = await window.ethereum.request({ method: 'eth_requestAccounts' })
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const contract = new ethers.Contract(tokenAddress, Token.abi, provider)
      const balance = await contract.balanceOf(account);
      console.log("Solde : ", balance.toString());
    }
  }

  async function setGreeting() {
    if (!greeting) return
    if (typeof window.ethereum !== 'undefined') {
      await requestAccount()
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      console.log({ provider })
      const signer = provider.getSigner()
      const contract = new ethers.Contract(greeterAddress, Greeter.abi, signer)
      const transaction = await contract.setGreeting(greeting)
      await transaction.wait()
      fetchGreeting()
    }
  }

  async function sendCoins() {
    if (typeof window.ethereum !== 'undefined') {
      await requestAccount()
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const contract = new ethers.Contract(tokenAddress, Token.abi, signer);
      const transaction = await contract.transfer(userAccount, amount);
      await transaction.wait();
      console.log(`${amount} jetons envoyés avec succès à ${userAccount}`);
    }
  }

  return (
    <div className="App">
      <header className="App-header">
        <button onClick={fetchGreeting}>Récupérer le message</button>
        <button onClick={setGreeting}>Définir le message</button>
        <input onChange={e => setGreetingValue(e.target.value)} placeholder="Définir le message" />

        <br />
        <button onClick={getBalance}>Obtenir le solde</button>
        <button onClick={sendCoins}>Envoyer des jetons</button>
        <input onChange={e => setUserAccount(e.target.value)} placeholder="ID du compte" />
        <input onChange={e => setAmount(e.target.value)} placeholder="Montant" />
      </header>
    </div>
  );
}

export default App;

```

Ensuite, lancez l'application :

```sh
npm start

```

Nous devrions pouvoir cliquer sur **Obtenir le solde** (Get Balance) et voir que nous avons 1 000 000 de jetons dans notre compte affiché dans la console.

Vous devriez également pouvoir les voir dans MetaMask en cliquant sur **Ajouter un jeton** (Add Token) :

![Ajouter un jeton](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0t2ip26i5d2ltjc9j2a6.jpg)

Cliquez ensuite sur **Jeton personnalisé** (Custom Token) et saisissez l'adresse du contrat du jeton, puis sur **Ajouter un jeton**. Désormais, les jetons devraient être disponibles dans votre portefeuille :

![NDT](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5op32iqbeszizri72qc0.jpg)

Ensuite, essayons d'envoyer ces jetons à une autre adresse.

Pour ce faire, copiez l'adresse d'un autre compte et envoyez-les à cette adresse en utilisant l'interface React mise à jour. Lorsque vous vérifiez le montant des jetons, il devrait être égal au montant d'origine moins le montant que vous avez envoyé à l'adresse.

## Comment créer un jeton ERC20

La [norme de jeton ERC20](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/) définit un ensemble de règles qui s'appliquent à tous les jetons ERC20, ce qui leur permet d'interagir facilement les uns avec les autres. L'ERC20 permet à quiconque de minter très facilement ses propres jetons qui seront interopérables avec d'autres sur la blockchain Ethereum.

Voyons comment nous pouvons construire notre propre jeton en utilisant la norme ERC20.

Tout d'abord, installez la bibliothèque de smart contracts [OpenZeppelin](https://github.com/OpenZeppelin/openzeppelin-contracts) à partir de laquelle nous importerons le jeton `ERC20` de base :

```sh
npm install @openzeppelin/contracts

```

Ensuite, nous allons créer notre jeton en étendant (ou en héritant de) le contrat `ERC20` :

```solidity
//SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract NDToken is ERC20 {
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        _mint(msg.sender, 100000 * (10 ** 18));
    }
}

```

Le constructeur vous permet de définir le nom et le symbole du jeton, et la fonction `_mint` vous permet de minter les jetons et de définir le montant.

Par défaut, l'ERC20 fixe le nombre de décimales à 18, donc dans notre fonction `_mint`, nous multiplions 100 000 par 10 à la puissance 18 pour minter un total de 100 000 jetons, chacun avec 18 décimales (de la même manière qu'un 1 Eth est composé de 10 à la puissance 18 [wei](https://www.investopedia.com/terms/w/wei.asp)).

Pour déployer, nous devons passer les valeurs du constructeur (`name` et `symbol`), nous pourrions donc faire quelque chose comme ceci dans notre script de déploiement :

```javascript
const NDToken = await hre.ethers.getContractFactory("NDToken");
const ndToken = await NDToken.deploy("Nader Dabit Token", "NDT");

```

En étendant le jeton ERC20 original, votre jeton héritera de toutes les fonctions et fonctionnalités suivantes :

```solidity
function name() public view returns (string)
function symbol() public view returns (string)
function decimals() public view returns (uint8)
function totalSupply() public view returns (uint256)
function balanceOf(address _owner) public view returns (uint256 balance)
function transfer(address _to, uint256 _value) public returns (bool success)
function transferFrom(address _from, address _to, uint256 _value) public returns (bool success)
function approve(address _spender, uint256 _value) public returns (bool success)
function allowance(address _owner, address _spender) public view returns (uint256 remaining)

```

Une fois déployé, vous pouvez utiliser n'importe laquelle de ces fonctions pour interagir avec le nouveau smart contract. Pour un autre exemple de jeton ERC20, consultez Solidity by example ici : [https://solidity-by-example.org/app/erc20/](https://solidity-by-example.org/app/erc20/).

## Conclusion

Nous avons couvert beaucoup de choses dans cet article. Mais pour moi, c'est en quelque sorte l'essentiel pour bien démarrer avec cette stack.

C'est ce que j'aurais aimé avoir, non seulement en tant que personne apprenant tout cela, mais aussi pour le futur si jamais j'ai besoin de me référer à quoi que ce soit. J'espère que vous avez beaucoup appris.

Si vous souhaitez prendre en charge plusieurs portefeuilles en plus de MetaMask, consultez [Web3Modal](https://github.com/Web3Modal/web3modal) qui facilite l'implémentation de la prise en charge de plusieurs fournisseurs dans votre application avec une configuration assez simple et personnalisable.

Dans mes futurs tutoriels et guides, j'approfondirai le développement de smart contracts plus complexes et j'expliquerai également comment les déployer en tant que [subgraphs](https://thegraph.com/docs/define-a-subgraph) pour exposer une API GraphQL par-dessus et implémenter des fonctionnalités telles que la pagination et la recherche plein texte.

J'aborderai également l'utilisation de technologies telles que l'IPFS et les bases de données Web3 pour stocker des données de manière décentralisée.

Si vous avez des questions ou des suggestions pour de futurs tutoriels, n'hésitez pas à m'en faire part.