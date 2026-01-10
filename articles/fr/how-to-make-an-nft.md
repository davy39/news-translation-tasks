---
title: Comment créer un NFT en 14 lignes de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-10-14T17:49:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-nft
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/nft.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: NFT
  slug: nft
seo_title: Comment créer un NFT en 14 lignes de code
seo_desc: 'By Nico

  If you''re a developer who''s interested in Blockchain development, you should know
  something about NFTs, or Non-Fungible Tokens. So in this article, we''ll learn about
  the engineering behind them so you can start building your own.

  At the end o...'
---

Par Nico

Si vous êtes un développeur intéressé par le développement Blockchain, vous devriez en savoir un peu sur les NFT, ou jetons non fongibles. Dans cet article, nous allons donc apprendre l'ingénierie derrière eux afin que vous puissiez commencer à construire les vôtres.

À la fin du projet, vous aurez votre propre portefeuille Ethereum avec un nouveau NFT dedans. Ce tutoriel est adapté aux débutants et ne nécessite aucune connaissance préalable du réseau Ethereum ou des contrats intelligents. 

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-46.png)
_Le contrat NFT n'a que 14 lignes de code_

## Qu'est-ce qu'un NFT ?

NFT signifie jeton non fongible. [Cette citation d'ethereum.org](https://ethereum.org/en/nft/) l'explique bien :

> Les NFT sont des jetons que nous pouvons utiliser pour représenter la propriété d'objets uniques. Ils nous permettent de tokeniser des choses comme l'art, des objets de collection, voire des biens immobiliers. Ils ne peuvent avoir qu'un seul propriétaire officiel à la fois et sont sécurisés par la blockchain Ethereum – personne ne peut modifier l'enregistrement de propriété ou copier/coller un nouveau NFT.

## Qu'est-ce qu'une norme NFT ou ERC-721 ?

L'ERC-721 est la norme NFT la plus courante. Si votre contrat intelligent implémente certaines méthodes API standardisées, il peut être appelé un contrat de jeton non fongible ERC-721. 

Ces méthodes sont spécifiées dans [EIP-721](https://eips.ethereum.org/EIPS/eip-721). Des projets open-source comme OpenZeppelin ont simplifié le processus de développement en implémentant les normes ERC les plus courantes sous forme de bibliothèque réutilisable. 

## Qu'est-ce que le minting d'un NFT ?

En mintant un NFT, vous publiez un jeton unique sur une blockchain. Ce jeton est une instance de votre contrat intelligent. 

Chaque jeton a un tokenURI unique, qui contient les métadonnées de votre actif dans un fichier JSON conforme à un certain schéma. Les métadonnées sont l'endroit où vous stockez des informations sur votre NFT, telles que le nom, l'image, la description et d'autres attributs.

Un exemple de fichier JSON pour le "ERC721 Metadata Schema" ressemble à ceci :

```json
{
	"attributes": [
		{
			"trait_type": "Shape",
			"value": "Circle"
		},
		{
			"trait_type": "Mood",
			"value": "Sad"
		}
	],
	"description": "A sad circle.",
	"image": "https://i.imgur.com/Qkw9N0A.jpeg",
	"name": "Sad Circle"
}
```

## Comment stocker les métadonnées de mon NFT ?

Il existe trois principales façons de stocker les métadonnées d'un NFT. 

Tout d'abord, vous pouvez stocker les informations sur la chaîne. En d'autres termes, vous pouvez étendre votre ERC-721 et stocker les métadonnées sur la blockchain, ce qui peut être coûteux. 

La deuxième méthode consiste à utiliser [IPFS](https://docs.ipfs.io/concepts/what-is-ipfs/). Et la troisième façon est de simplement avoir votre API retourner le fichier JSON.

Les première et deuxième méthodes sont généralement préférées, car vous ne pouvez pas altérer le fichier JSON sous-jacent. Pour le cadre de ce projet, nous opterons pour la troisième méthode. 

Pour un bon tutoriel sur l'utilisation des NFT avec IPFS, lisez [cet article](https://docs.alchemy.com/alchemy/tutorials/how-to-create-an-nft/how-to-mint-a-nft#step-4-configure-the-metadata-for-your-nft-using-ipfs) par l'équipe d'Alchemy.

## Ce que nous allons construire

![Image](https://www.freecodecamp.org/news/content/images/2021/10/emotionalshapes.png)

Dans ce tutoriel, nous allons créer et minter notre propre NFT. Il est adapté aux débutants et ne nécessite aucune connaissance préalable du réseau Ethereum ou des contrats intelligents. Cependant, avoir une bonne compréhension de ces concepts vous aidera à comprendre ce qui se passe en coulisses. 

Dans un prochain tutoriel, nous construirons une application web React entièrement fonctionnelle où vous pourrez afficher et vendre vos NFT.

Si vous débutez dans le développement de dApp, commencez par lire [les sujets clés](https://ethereum.org/en/developers/docs/intro-to-ethereum/) et regardez ce [cours incroyable](https://www.youtube.com/watch?v=M576WGiDBdQ) de Patrick Collins.

_Ce projet est intentionnellement écrit avec un code facilement compréhensible et n'est pas adapté à une utilisation en production._

## Prérequis

### Metamask

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-32.png)

Nous avons besoin d'une adresse Ethereum pour interagir avec notre contrat intelligent. Nous utiliserons [Metamask](https://metamask.io/) comme notre portefeuille. C'est un portefeuille virtuel gratuit qui gère vos adresses Ethereum. Nous en aurons besoin pour envoyer et recevoir des transactions (en savoir plus à ce sujet [ici](https://ethereum.org/en/developers/docs/transactions/)). Par exemple, le minting d'un NFT est une transaction. 

Téléchargez leur extension Chrome et leur application mobile. Nous aurons besoin des deux car l'extension Chrome n'affiche pas vos NFT.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-34.png)

Assurez-vous de changer le réseau pour "Ropsten Test Network" à des fins de développement. Vous aurez besoin de quelques Eth pour couvrir les frais de déploiement et de minting de votre NFT. Rendez-vous sur le [Ropsten Ethereum Faucet](https://faucet.ropsten.be/) et entrez votre adresse. Vous devriez bientôt voir quelques Eth de test dans votre compte Metamask.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-35.png)

### Alchemy

Pour interagir avec le réseau Ethereum, vous devrez être connecté à un nœud Ethereum. 

Exécuter votre propre nœud et maintenir l'infrastructure est un projet en soi. Heureusement, il existe des fournisseurs de nœuds en tant que service qui hébergent l'infrastructure pour vous. Il existe de nombreux choix comme Infura, BlockDaemon et Moralis. Nous utiliserons [Alchemy](https://www.alchemy.com/) comme notre fournisseur de nœuds. 

Rendez-vous sur leur site web, créez un compte, choisissez Ethereum comme votre réseau et créez votre application. Choisissez Ropsten comme votre réseau.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-36.png)

Sur votre tableau de bord, cliquez sur "view details" sur votre application, puis cliquez sur "view key". Enregistrez votre clé http quelque part car nous en aurons besoin plus tard.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-38.png)

### NodeJS/NPM

Nous utiliserons NodeJS pour le projet. Si vous ne l'avez pas installé, [suivez ce tutoriel simple](https://www.freecodecamp.org/news/how-to-install-node-in-your-machines-macos-linux-windows/) de freeCodeCamp.

## Initialiser le projet

Dans votre terminal, exécutez cette commande pour créer un nouveau répertoire pour votre projet :

```
mkdir nft-project
cd nft-project
```

Maintenant, créons un autre répertoire, `ethereum/`, à l'intérieur de `nft-project/` et initialisons-le avec [Hardhat](https://hardhat.org/getting-started/). Hardhat est un outil de développement qui facilite le déploiement et le test de votre logiciel Ethereum.

```
mkdir ethereum
cd ethereum
npm init
```

Répondez aux questions comme vous le souhaitez. Ensuite, exécutez ces commandes pour créer un projet Hardhat :

```
npm install --save-dev hardhat
npx hardhat
```

Vous verrez cette invite :

```
888    888                      888 888               888
888    888                      888 888               888
888    888                      888 888               888
8888888888  8888b.  888d888 .d88888 88888b.   8888b.  888888
888    888     "88b 888P"  d88" 888 888 "88b     "88b 888
888    888 .d888888 888    888  888 888  888 .d888888 888
888    888 888  888 888    Y88b 888 888  888 888  888 Y88b.
888    888 "Y888888 888     "Y88888 888  888 "Y888888  "Y888

Welcome to Hardhat v2.0.8

? What do you want to do? …
  Create a sample project
✨ Create an empty hardhat.config.js
  Quit
```

Sélectionnez créer un fichier hardhat.config.js vide. Cela générera un fichier `hardhat.config.js` vide que nous mettrons à jour plus tard.

Pour l'application web, nous utiliserons [Next.js](https://nextjs.org/docs/getting-started) pour initialiser une application web entièrement fonctionnelle. Retournez au répertoire racine `nft-project/` et initialisez une application Next.js boilerplate appelée web :

```
cd ..
mkdir web
cd web
npx create-next-app@latest
```

Votre projet ressemble maintenant à ceci :

```
nft-project/
	ethereum/
	web/
```

Super ! Nous sommes prêts à plonger dans du vrai codage.

## Comment définir nos variables .env

Vous souvenez-vous de la clé Alchemy que nous avons récupérée de notre projet de test plus tôt ? Nous l'utiliserons avec les clés publique et privée de notre compte Metamask pour interagir avec la blockchain. 

Exécutez les commandes suivantes, créez un fichier appelé `.env` à l'intérieur de votre répertoire `ethereum/` et installez [dotenv](https://www.npmjs.com/package/dotenv). Nous les utiliserons plus tard.

```
cd ..
cd ethereum
touch .env
npm install dotenv --save
```

Pour votre fichier `.env`, mettez la clé que vous avez exportée d'Alchemy et [suivez ces instructions](https://metamask.zendesk.com/hc/en-us/articles/360015289632-How-to-Export-an-Account-Private-Key) pour récupérer votre clé privée Metamask.

Voici votre fichier .env :

```
DEV_API_URL = VOTRE_CLE_ALCHEMY
PRIVATE_KEY = VOTRE_CLE_PRIVEE_METAMASK
PUBLIC_KEY = VOTRE_ADRESSE_METAMASK
```

## Le contrat intelligent pour les NFT

Allez dans le dossier `ethereum/` et créez deux autres répertoires : contracts et scripts. [Un simple projet hardhat](https://hardhat.org/guides/project-setup.html) contient ces dossiers.

* `contracts/` contient les fichiers sources de vos contrats
* `scripts/` contient les scripts pour déployer et minter nos NFT

```
mkdir contracts
mkdir scripts
```

Ensuite, installez OpenZeppelin. [OpenZeppelin Contract](https://docs.openzeppelin.com/contracts/4.x/) est une bibliothèque open-source avec du code réutilisable pré-testé pour faciliter le développement de contrats intelligents.

```
npm install @openzeppelin/contracts
```

Enfin, nous allons écrire le contrat intelligent pour notre NFT. Naviguez jusqu'à votre répertoire de contrats et créez un fichier intitulé `EmotionalShapes.sol`. Vous pouvez nommer vos NFT comme vous le souhaitez.

L'extension `.sol` fait référence au langage Solidity, que nous utiliserons pour programmer notre contrat intelligent. Nous n'écriremos que 14 lignes de code avec Solidity, donc pas d'inquiétude si vous ne l'avez jamais vu auparavant. 

Commencez par [cet article](https://ethereum.org/en/developers/docs/smart-contracts/languages/) pour en savoir plus sur les langages de contrats intelligents. Vous pouvez également passer directement à cette [feuille de triche](https://reference.auditless.com/cheatsheet/) Solidity qui contient la syntaxe principale.

```
cd contracts
touch EmotionalShapes.sol
```

Voici notre contrat intelligent :

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract EmotionalShapes is ERC721 {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    constructor() ERC721("EmotionalShapes", "ESS") {}

    function _baseURI() internal pure override returns (string memory) {
        return "VOTRE_URL_API/api/erc721/";
    }

    function mint(address to)
        public returns (uint256)
    {
        require(_tokenIdCounter.current() < 3); 
        _tokenIdCounter.increment();
        _safeMint(to, _tokenIdCounter.current());

        return _tokenIdCounter.current();
    }
}
```

Passons en revue le code et comprenons ce qui se passe. 

1. En haut du fichier, nous avons spécifié quel module OpenZeppelin importer. Nous avons besoin du contrat ERC721 car il est la 'base' de notre contrat intelligent. Il a déjà implémenté toutes les méthodes spécifiées dans [EIP-721](https://eips.ethereum.org/EIPS/eip-721) afin que nous puissions l'utiliser en toute sécurité.
2. Un Counter est utile pour générer des identifiants incrémentiels pour nos NFT. Nous avons nommé la variable `_tokenIdCounter`
3. Dans le constructeur, nous avons initialisé notre ERC721 avec son nom et son symbole. J'ai choisi EmotionalShapes et ESS.
4. Nous remplaçons la fonction `_baseURI` par défaut en retournant la nôtre. Nous allons la construire dans un instant. En résumé, c'est l'URL qui sera ajoutée comme 'préfixe' à tous nos tokenURIs. Dans l'exemple ci-dessus, les métadonnées de nos NFT vivront dans un fichier JSON à `VOTRE_URL_API/[api/erc721/](https://e110-99-121-58-31.ngrok.io/api/erc721/)1`.
5. Nous implémentons la fonction 'mint'. C'est la fonction qui vous permet de publier une instance de ce contrat intelligent sur la blockchain. J'ai requis que la variable `_tokenIdCounter` soit inférieure à 3 car je ne créerai que trois instances de mon NFT. Vous pouvez supprimer cela si vous souhaitez en minter plus.
6. Enfin, à l'intérieur de la fonction mint, nous incrémentons la variable `_tokenIdCounter` de 1, donc notre id sera 1, suivi de 2, suivi de 3. Ensuite, nous appelons la fonction fournie par OpenZeppelin `_safeMint` pour publier le jeton.

Ne vous inquiétez pas si vous vous sentez perdu. Vous pouvez participer à un atelier animé par des bénévoles de freeCodeCamp, où nous invitons des développeurs de niveaux de compétence similaires à construire des choses ensemble, y compris ce projet NFT. 

Les événements sont gratuits et à distance, donc vous pouvez poser directement toutes vos questions. Vous pouvez vous inscrire [ici](https://equia.io). Les places sont limitées, donc vous serez invité aux prochains événements disponibles.

## Comment construire les métadonnées pour notre NFT

Comme mentionné précédemment, il existe trois principales façons de stocker votre tokenURI. Nous allons construire un simple endpoint API qui résout les informations de notre NFT en JSON. 

Notre projet Next.js nous donne un moyen pratique de développer des routes API. Allez dans le dossier `web/`, trouvez le dossier `api/` dans le dossier `pages/`, et créons notre route dynamique `[id].js` dans un dossier `erc721/` (lisez plus sur le routage [ici](https://www.freecodecamp.org/news/p/18513919-9e93-4ab3-9f52-2448aafa8835/develop%20API%20routes)):

```javascript
// web/pages/api/erc721/[id].js

const metadata = {
  1: {
    attributes: [
      {
        trait_type: "Shape",
        value: "Circle",
      },
      {
        trait_type: "Mood",
        value: "Sad",
      },
    ],
    description: "A sad circle.",
    image: "https://i.imgur.com/Qkw9N0A.jpeg",
    name: "Sad Circle",
  },
  2: {
    attributes: [
      {
        trait_type: "Shape",
        value: "Rectangle",
      },
      {
        trait_type: "Mood",
        value: "Angry",
      },
    ],
    description: "An angry rectangle.",
    image: "https://i.imgur.com/SMneO6k.jpeg",
    name: "Angry Rectangle",
  },
  3: {
    attributes: [
      {
        trait_type: "Shape",
        value: "Triangle",
      },
      {
        trait_type: "Mood",
        value: "Bored",
      },
    ],
    description: "An bored triangle.",
    image: "https://i.imgur.com/hMVRFoJ.jpeg",
    name: "Bored Triangle",
  },
};

export default function handler(req, res) {
  res.status(200).json(metadata[req.query.id] || {});
}
```

Pour les besoins de ce projet, j'ai rendu le code aussi facilement compréhensible que possible. Cela n'est définitivement pas adapté à la production (veuillez ne pas utiliser une URL Imgur pour votre NFT). Assurez-vous de définir les métadonnées pour tous les NFT que vous prévoyez de minter.

Maintenant, allez dans le répertoire web et démarrez votre application Next.js avec cette commande :

```
npm run dev
```

Votre application devrait fonctionner sur localhost:3000. Pour vous assurer que notre endpoint fonctionne, allez sur [http://localhost:3000/api/erc721/1](http://localhost:3000/api/erc721/1) et il devrait résoudre avec un objet JSON des métadonnées de votre premier NFT.

## Comment exposer les métadonnées de notre NFT

Puisque votre application est hébergée localement, d'autres applications ne peuvent pas y accéder. En utilisant un outil comme [ngrok](https://ngrok.com/), nous pouvons exposer notre hôte local à une URL accessible publiquement.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-39.png)

1. Allez sur [ngrok.com](https://ngrok.com/) et complétez le processus d'inscription
2. Décompressez le package téléchargé
3. Dans votre terminal, assurez-vous de vous trouver dans le dossier où vous avez décompressé votre package ngrok
4. Suivez les instructions sur votre tableau de bord et exécutez

```
./ngrok authtoken VOTRE_JETON_AUTH
```

5. Ensuite, exécutez cette commande pour créer un tunnel vers votre application web hébergée sur localhost:3000

```
./ngrok http 3000
```

6. Vous y êtes presque ! Sur votre terminal, vous devriez voir quelque chose comme ceci :

```
ngrok by @inconshreveable                                                                            (Ctrl+C to quit)
                                                                                                                     
Session Status                online                                                                                 
Account                       VOTRE_COMPTE (Plan: Free)                                                                       
Version                       2.3.40                                                                                 
Region                        United States (us)                                                                     
Web Interface                 http://127.0.0.1:4040                                                                  
Forwarding                    http://VOTRE_ADRESSE_NGROK -> http://localhost:3000                             
Forwarding                    https://VOTRE_ADRESSE_NGROK -> http://localhost:3000                             
```

Allez sur `VOTRE_ADRESSE_NGROK/api/erc721/1` pour vous assurer que votre endpoint fonctionne correctement.

## Comment déployer notre NFT

Maintenant que nous avons fait tout le travail préparatoire (ouf), retournons dans notre dossier `ethereum/` et préparons-nous à déployer notre NFT.

Changez la fonction `_baseURI` dans votre fichier `ethreum/contracts/NOM_DE_VOTRE_NFT.sol` pour qu'elle retourne votre adresse ngrok.

```
// ethereum/conrtacts/EmotionalShapes.sol

contract EmotionalShapes is ERC721 {
...
	function _baseURI() internal pure override returns (string memory) {
		return "https://VOTRE_ADRESSE_NGROK/api/erc721/";
	}
...
}
```

Pour déployer notre NFT, nous devrons d'abord [le compiler en utilisant Hardhat](https://hardhat.org/guides/compile-contracts.html). Pour faciliter le processus, nous installerons [ethers.js](https://docs.ethers.io/v5/).

```
npm install @nomiclabs/hardhat-ethers --save-dev
```

Mettons à jour notre fichier hardhat.config.js :

```
require("dotenv").config();
require("@nomiclabs/hardhat-ethers");

module.exports = {
  solidity: "0.8.0",
  defaultNetwork: "ropsten",
  networks: {
    hardhat: {},
    ropsten: {
      url: process.env.DEV_API_URL,
      accounts: [`0x${process.env.PRIVATE_KEY}`],
    },
  },
};
```

Pour en savoir plus sur le fichier de configuration hardhat, consultez leur [documentation](https://hardhat.org/config/). Nous avons configuré le réseau ropsten avec notre URL Alchemy et lui avons fourni la clé privée de votre compte metamask.

Enfin, exécutez :

```
npx hardhat compile
```

Cela permet à hardhat de générer deux fichiers par contrat compilé. Nous devrions voir un nouveau dossier `artifacts/` qui contient vos contrats compilés dans le dossier `contracts/`. Pour en savoir plus sur le fonctionnement de cela, lisez [ce tutoriel](https://hardhat.org/guides/compile-contracts.html) par l'équipe Hardhat.

Maintenant, écrivons un script pour enfin déployer notre NFT sur le réseau de test. Dans votre dossier `scripts/`, créez un fichier appelé `deploy.js`.

```javascript
// ethereum/scripts/deploy.js

async function main() {
  const EmotionalShapes = await ethers.getContractFactory("EmotionalShapes");
  const emotionalShapes = await EmotionalShapes.deploy();

  console.log("EmotionalShapes deployed:", emotionalShapes.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
```

Ce code est inspiré du [tutoriel de déploiement hardhat](https://hardhat.org/guides/deploying.html).

> Un `ContractFactory` dans ethers.js est une abstraction utilisée pour déployer de nouveaux contrats intelligents, donc `EmotionalShapes` ici est une usine pour les instances de notre contrat de jeton. Appeler `deploy()` sur un `ContractFactory` démarrera le déploiement et retournera une `Promise` qui se résout en un `Contract`. C'est l'objet qui a une méthode pour chacune de vos fonctions de contrat intelligent.

### Comment voir le NFT sur la blockchain

Exécutez le script de déploiement :

```
node ./scripts/deploy.js
```

Vous devriez voir dans votre terminal `EmotionalShapes deployed: SOME_ADDRESS`. C'est l'adresse où votre contrat intelligent est déployé sur le réseau de test ropsten.

Si vous allez sur `https://ropsten.etherscan.io/address/SOME_ADDRESS`, vous devriez voir votre NFT fraîchement déployé. Oui ! Vous l'avez fait !

Si vous êtes bloqué quelque part dans le tutoriel ou si vous vous sentez perdu, vous pouvez à nouveau [rejoindre nos ateliers en direct](https://equia.io) où nous construirons ce projet ensemble lors d'un appel Zoom. 

## Comment minter votre NFT

Maintenant que vous avez déployé votre NFT, il est temps de le minter pour vous-même ! Créez un nouveau fichier appelé `mint.js` dans votre dossier scripts/. Nous utiliserons ethers.js pour nous aider.

Commencez par ajouter le package `ethers.js` :

```
npm install --save ethers
```

Ensuite, remplissez le fichier `mint.js` :

```javascript
require("dotenv").config();
const { ethers } = require("ethers");

const contract = require("../artifacts/contracts/EmotionalShapes.sol/EmotionalShapes.json");
const contractInterface = contract.abi;

// https://docs.ethers.io/v5/api/providers
const provider = ethers.getDefaultProvider("ropsten", {
  alchemy: process.env.DEV_API_URL,
});

// https://docs.ethers.io/v5/api/signer/#Wallet
const wallet = new ethers.Wallet(process.env.PRIVATE_KEY, provider);

//https://docs.ethers.io/v5/api/contract/contract
const emotionalShapes = new ethers.Contract(
  VOTRE_ADRESSE_NFT,
  contractInterface,
  wallet
);

const main = () => {
  emotionalShapes
    .mint(process.env.PUBLIC_KEY)
    .then((transaction) => console.log(transaction))
    .catch((e) => console.log("something went wrong", e));
};

main();
```

J'ai laissé des commentaires sur les endroits où vous pouvez trouver plus d'informations sur les différentes méthodes. Nous avons d'abord récupéré l'interface du contrat (ABI). D'après ethereum.org :

> Une interface binaire d'application, ou ABI, est la manière standard d'interagir avec les [contrats](https://ethereum.org/en/glossary/#contract-account) dans l'écosystème Ethereum, à la fois depuis l'extérieur de la blockchain et pour les interactions de contrat à contrat.

Votre ABI définit comment les autres interagissent avec votre contrat. Ensuite, nous avons créé notre fournisseur avec Alchemy (souvenez-vous des nœuds en tant que service). Enfin, nous avons initialisé notre portefeuille avec notre clé privée.

La fonction `main()` appelle la méthode `mint` dans le contrat intelligent que nous venons de déployer. La méthode `mint` ne prend qu'un seul paramètre, `to`, qui indique le destinataire du jeton. Puisque nous mintons pour nous-mêmes, nous mettons l'adresse publique de notre compte Metamask.

Si tout se passe bien, vous devriez voir la transaction enregistrée dans votre terminal. Récupérez la propriété `hash` et allez sur `https://ropsten.etherscan.io/tx/VOTRE_HASH`. Vous devriez voir la transaction de minting là-bas !

## Comment voir le NFT dans votre portefeuille Metamask

Vous devez commencer par télécharger la version mobile de Metamask. Ensuite, connectez-vous à votre compte. 

Vous devriez voir un onglet NFT ainsi qu'un bouton ajouter NFT. Cliquez sur le bouton et entrez l'adresse de votre contrat intelligent ainsi que les identifiants que vous avez mintés. Si vous avez suivi le tutoriel, vous devriez commencer avec un identifiant de `1`.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/IMG_0376.jpeg)
_Voir les NFT dans votre portefeuille Metamask_

## Conclusion

Félicitations ! Vous venez de minter votre propre NFT. Dans la prochaine partie du projet, nous construirons l'application React front-end pour interagir avec notre contrat. L'objectif final est de construire une application web entièrement fonctionnelle où vous pouvez vendre vos propres NFT.

Enfin, vous pouvez [rejoindre nos ateliers en direct](https://equia.io) avec des bénévoles de freeCodeCamp où nous construirons ce projet ensemble avec d'autres développeurs. 

Les événements sont gratuits pour tout le monde dans le monde et les invitations sont envoyées selon le principe du premier arrivé, premier servi. Si vous souhaitez diriger les ateliers, envoyez-moi un DM [sur Twitter](https://twitter.com/aly4alyssa), nous serions ravis de vous avoir ! Nous organisons également d'autres types d'événements comme des salons de l'emploi et des rencontres sociales. 

Faites-moi savoir ce que vous voulez construire. Les NFT en sont encore à leurs balbutiements et les idées nouvelles sont les bienvenues. J'ai hâte de voir quelle idée folle vous avez !