---
title: Tutoriel Solidity – Comment créer des NFT avec Hardhat
subtitle: ''
author: Taisuke Mino
co_authors: []
series: null
date: '2021-05-17T14:39:55.000Z'
originalURL: https://freecodecamp.org/news/solidity-tutorial-hardhat-nfts
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/hardhat_nft-1.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: NFT
  slug: nft
- name: Smart Contracts
  slug: smart-contracts
- name: Solidity
  slug: solidity
seo_title: Tutoriel Solidity – Comment créer des NFT avec Hardhat
seo_desc: "I'm a developer who's mostly been writing JavaScript, so the Solidity development\
  \ environment was a bit hard to learn. \nAbout four months ago, I switched to Hardhat\
  \ from Truffle. This cool new kid on the block drastically improved my coding experienc..."
---

Je suis un développeur qui a principalement écrit du JavaScript, l'environnement de développement Solidity a donc été un peu difficile à apprendre. 

Il y a environ quatre mois, je suis passé de Truffle à [Hardhat](https://hardhat.org/). Ce nouvel outil tendance a considérablement amélioré mon expérience de codage. Aujourd'hui, je souhaite donc le partager avec mes collègues développeurs Solidity.

Dans cet article, je vais vous guider à travers la configuration initiale, la compilation, les tests, le débogage et enfin le déploiement.

À la fin de cet article, vous serez en mesure de comprendre comment déployer un contrat NFT sur le réseau local avec Hardhat. 

L'objectif de cet article est de vous familiariser avec Hardhat. Je ne parlerai pas de la manière d'écrire un test ou de la syntaxe Solidity. Cependant, vous devriez être capable de suivre sans aucune connaissance en Solidity si vous savez écrire du JavaScript.

Consultez [ce dépôt](https://github.com/taisukemino/hardhat-nft-tutorial) pour le code.

## Comment configurer le projet

Commençons d'abord par un projet npm :

```
npm init --yes

```

Ensuite, installez le package Hardhat :

```
npm install --save-dev hardhat

```

Super ! Vous êtes maintenant prêt à créer un nouveau projet Hardhat :

```
npx hardhat

```

Choisissez `Create an empty hardhat.config.js` :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-1.png)

Cela créera un fichier `hardhat.config.js` dans votre répertoire racine avec la version du compilateur Solidity spécifiée :

```js
/**
 * @type import('Hardhat/config').HardhatUserConfig
 */
module.exports = {
  solidity: "0.7.3",
};

```

## Comment écrire et compiler le contrat

Très bien, nous allons commencer par écrire un contrat simple, puis nous le compilerons.

Créez un nouveau fichier Solidity dans un nouveau répertoire `contracts` :

```
 mkdir contracts && cd contracts && touch MyCryptoLions.sol

```

Nous utiliserons le package OpenZeppelin pour écrire notre contrat NFT. Commencez donc par installer le package OpenZeppelin :

```
npm install --save-dev @openzeppelin/contracts

```

Voici le code du contrat que nous allons compiler :

```solidity
pragma solidity ^0.7.3;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract MyCryptoLions is ERC721 {
    constructor(string memory name, string memory symbol)
        ERC721(name, symbol)
    {}
}

```

La première chose à faire dans tout fichier Solidity est de déclarer la version du compilateur. Ensuite, nous pouvons importer le contrat ERC721 (contrat NFT) d'OpenZeppelin, tout comme vous le feriez en JavaScript.

Solidity est un langage orienté contrat. Tout comme un langage orienté objet, les contrats peuvent avoir des membres tels que des fonctions et des variables. Dans notre code, nous n'avons que le constructeur, qui sera appelé lors du déploiement de notre contrat.

Notre contrat hérite de l'ERC721 puis transmet les arguments `name` et `symbol` qui vont être passés au contrat ERC721. Ils déterminent littéralement le nom et le symbole de votre jeton NFT.

Nous passerons les valeurs que nous souhaitons pour `name` et `symbol` au moment du déploiement.

Pour le compiler, lancez :

```
npx hardhat compile

```

Vous pourriez recevoir quelques avertissements, mais nous les ignorerons pour rester simples. Vous devriez voir `Compilation finished successfully` en bas.

Vous remarquerez également que les répertoires `/artifacts` et `/cache` ont été générés. Vous n'avez pas à vous en soucier pour cet article, mais il est bon de garder à l'esprit que vous pouvez utiliser l' `abi` dans les artifacts si vous souhaitez interagir avec le contrat lors de la création du frontend.

## Comment tester le contrat

Comme les smart contracts sont principalement des applications financières – et qu'ils sont également difficiles à modifier – les tests sont essentiels.

Nous utiliserons quelques packages pour les tests. Installez-les avec la commande ci-dessous :

```
npm install --save-dev @nomiclabs/hardhat-waffle ethereum-waffle chai @nomiclabs/hardhat-ethers ethers

```

`ethereum-waffle` est un Framework de test pour les smart contracts. `chai` est une bibliothèque d'assertion. Nous écrirons des tests dans Waffle en utilisant Mocha aux côtés de Chai. `ethers.js` est un SDK JavaScript pour interagir avec la blockchain Ethereum. Les deux autres packages sont des plugins pour Hardhat.

Maintenant, créons un nouveau répertoire `test` à la racine et créons-y un nouveau fichier appelé `test.js` :

```
mkdir test && cd test && touch test.js

```

Assurez-vous d'importer `@nomiclabs/hardhat-ethers` dans le fichier `hardhat.config.js` pour le rendre disponible partout :

```
require("@nomiclabs/hardhat-ethers");

```

Voici un test simple :

```js
const { expect } = require("chai");

describe("MyCryptoLions", function () {
  it("Should return the right name and symbol", async function () {
    const MyCryptoLions = await hre.ethers.getContractFactory("MyCryptoLions");
    const myCryptoLions = await MyCryptoLions.deploy("MyCryptoLions", "MCL");

    await myCryptoLions.deployed();
    expect(await myCryptoLions.name()).to.equal("MyCryptoLions");
    expect(await myCryptoLions.symbol()).to.equal("MCL");
  });
});

```

Ce code déploie notre contrat sur le réseau local Hardhat, puis vérifie si les valeurs `name` et `symbol` sont conformes à nos attentes.

Lancez le test :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-2.png)

Génial, le test est réussi !

### Comment utiliser console.log() dans Hardhat

Voici maintenant la chose la plus cool que vous puissiez faire avec Hardhat. Vous pouvez utiliser `console.log()` tout comme vous le faites en JavaScript, ce qui n'était pas possible auparavant. `console.log()` est à lui seul une raison suffisante pour passer à Hardhat. 

Revenons à votre fichier Solidity et utilisons `console.log()`.

```
pragma solidity ^0.7.3;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "hardhat/console.sol";

contract MyCryptoLions is ERC721 {
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        console.log("name", name);
        console.log("symbol", symbol);
        console.log("msg.sender", msg.sender); // msg.sender est l'adresse qui déploie initialement un contrat
    }
}

```

Et lancez à nouveau le test avec `npx hardhat test`. La commande compilera à nouveau le contrat, puis lancera le test. Vous devriez pouvoir voir certaines valeurs enregistrées à partir du contrat.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/image-3.png)

Cela rend le débogage beaucoup plus facile pour vous.

Une mise en garde : il ne prend en charge que ces types de données :

* uint
* string
* bool
* address

Mais à part cela, vous pouvez l'utiliser comme si vous écriviez du JavaScript.

## Comment déployer le contrat

Parfait ! Maintenant, déployons notre contrat. Nous pouvons déployer notre contrat sur l'un des réseaux de test, sur le Mainnet, ou même sur une version locale miroir du Mainnet. 

Mais dans cet article, nous allons déployer sur l'instance locale en mémoire du réseau Hardhat pour rester simples. Ce réseau est lancé par défaut au démarrage.

Créez un nouveau répertoire appelé `scripts` à la racine et un fichier `deploy.js` à l'intérieur.

```
mkdir scripts && cd scripts && touch deploy.js

```

Voici le script de déploiement. Vous déployez avec les valeurs du constructeur :

```js
async function main() {
  const MyCryptoLions = await hre.ethers.getContractFactory("MyCryptoLions");
  const myCryptoLions = await MyCryptoLions.deploy("MyCryptoLions", "MCL");

  await myCryptoLions.deployed();

  console.log("MyCryptoLions deployed to:", myCryptoLions.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });

```

Vous voudrez peut-être supprimer `console.log()` avant de déployer. Ensuite, lancez ce script de déploiement avec :

```
npx hardhat run scripts/deploy.js
MyCryptoLions deployed to: 0x5FbDB2315678afecb367f032d93F642f64180aa3

```

Et voilà ! Votre contrat NFT est maintenant déployé sur le réseau local. 

Vous pouvez cibler n'importe quel réseau configuré dans le fichier `hardhat.config.js` selon vos besoins. Vous pouvez en savoir plus sur la configuration [ici](https://hardhat.org/config/).

## Conclusion

Hardhat possède d'autres fonctionnalités intéressantes comme des traces de pile (stack traces) utiles, le support de plusieurs versions du compilateur Solidity, un forking robuste du Mainnet, un excellent support de TypeScript et la vérification des contrats dans Etherscan. Mais ce sera pour une prochaine fois !