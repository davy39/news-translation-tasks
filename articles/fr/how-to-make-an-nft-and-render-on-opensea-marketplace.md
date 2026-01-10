---
title: Comment créer un NFT et le rendre sur le marché OpenSea
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-01T17:05:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-nft-and-render-on-opensea-marketplace
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Advanced-NFT-Deployment
seo_title: Comment créer un NFT et le rendre sur le marché OpenSea
---

1-.png
étiquettes:
- nom: Art
  slug: art
- nom: Blockchain
  slug: blockchain
- nom: décentralisation
  slug: decentralization
- nom: NFT
  slug: nft
seo_title: null
seo_desc: 'Par Patrick Collins

Dans cet article, je vais vous montrer comment créer un NFT sans compétences en ingénierie logicielle. Ensuite, nous apprendrons à créer des NFT personnalisables illimités avec Brownie, Python et Chainlink. Et nous verrons comment rendre et vendre notre création...'
---

Par Patrick Collins

Dans cet article, je vais vous montrer comment créer un NFT sans compétences en ingénierie logicielle. Ensuite, nous apprendrons à créer des NFT personnalisables illimités avec [Brownie](https://eth-brownie.readthedocs.io/en/stable/), [Python](https://www.python.org/), et [Chainlink](https://docs.chain.link/docs). Et nous verrons comment rendre et vendre notre création sur le marché [OpenSea](https://opensea.io/) NFT.

Si vous cherchez un tutoriel qui utilise Truffle, JavaScript et des personnages médiévaux amusants, consultez comment [Créer, Déployer et Vendre votre NFT ici](https://blog.chain.link/build-deploy-and-sell-your-own-dynamic-nft/).

## Qu'est-ce qu'un NFT ?

Les [NFT](https://eips.ethereum.org/EIPS/eip-721) (Non-Fungible Tokens) peuvent être résumés en un mot : "unique". Ce sont des contrats intelligents déployés sur une blockchain qui représentent quelque chose d'unique.

### ERC20 vs ERC721

Les NFT sont un standard de jeton blockchain similaire à l'[ERC20](https://www.investopedia.com/news/what-erc20-and-what-does-it-mean-ethereum/), comme AAVE, SNX et LINK (techniquement un ERC677). Les ERC20 sont des jetons "fongibles", ce qui signifie "remplaçables" ou "interchangeables".

Par exemple, votre billet de dollar vaudra 1 $ peu importe quel billet de dollar vous utilisez. Le numéro de série sur le billet de dollar peut être différent, mais les billets sont interchangeables et ils vaudront 1 $ peu importe quoi.

Les NFT, en revanche, sont "non fongibles", et ils suivent leur propre standard de jeton, l'[ERC721](https://eips.ethereum.org/EIPS/eip-721). Par exemple, la Joconde est "non fongible". Même si quelqu'un peut en faire une copie, il n'y aura toujours qu'une seule Joconde. Si la Joconde était créée sur une blockchain, ce serait un NFT.

![Créer un NFT](https://www.freecodecamp.org/news/content/images/2021/03/image-145.png)
_Image originale de [Wikipedia](https://en.wikipedia.org/wiki/Mona_Lisa)_

## À quoi servent les NFT ?

Les NFT apportent de la valeur aux créateurs, artistes, concepteurs de jeux et plus encore en ayant un historique permanent de déploiement stocké sur la chaîne.

Vous saurez toujours qui a créé le NFT, qui possédait le NFT, d'où il vient, et plus encore, ce qui leur donne beaucoup de valeur par rapport à l'art traditionnel. Dans l'art traditionnel, il peut être difficile de comprendre ce qu'est un "faux", alors que sur la chaîne, l'historique est facilement traçable.

Et puisque les contrats intelligents et les NFT sont 100 % programmables, les NFT peuvent également avoir des royalties intégrées et toute autre fonctionnalité. Compenser les artistes a toujours été un problème, car souvent le travail d'un artiste est diffusé sans aucune attribution.

De plus en plus d'artistes et d'ingénieurs se lancent dans cette valeur ajoutée massive, car c'est enfin un excellent moyen pour les artistes d'être récompensés pour leur travail. Et plus que cela, les NFT sont un moyen amusant de montrer votre créativité et de devenir collectionneur dans un monde numérique.

### La Valeur des NFT

Les NFT ont parcouru un long chemin, et nous continuons à voir des ventes record de NFT, comme "Everydays: The First 5,000 Days" vendu pour 69,3 millions de dollars.

![Créer un NFT](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-31-at-9.48.19-AM.png)
_Image de [Twitter](https://twitter.com/ChristiesInc/status/1361670588608176128)_

Il y a donc beaucoup de valeur ici, et c'est aussi une manière amusante, dynamique et engageante de créer de l'art dans le monde numérique et d'apprendre la création de contrats intelligents. Alors maintenant, je vais vous enseigner tout ce que vous devez savoir sur la création de NFT.

## Comment créer un NFT

### Ce que nous ne allons pas couvrir

Maintenant, la manière la plus simple de créer un NFT est de se rendre sur une plateforme comme [Opensea](https://opensea.io/), [Rarible](https://rarible.com/), ou [Mintible](https://mintable.app/) et de suivre leur guide étape par étape pour déployer sur leur plateforme.

Vous pouvez 100 % prendre cette route, cependant vous pourriez être lié à la plateforme, et vous êtes limité à la fonctionnalité que la plateforme a. Vous ne pouvez pas atteindre la personnalisation illimitée, ou vraiment utiliser aucun des avantages des NFT. Mais si vous êtes un ingénieur logiciel débutant, ou pas très technique, c'est la route pour vous.

Si vous cherchez à devenir un ingénieur logiciel plus fort, apprendre un peu de solidité, et avoir le pouvoir de créer quelque chose avec une créativité illimitée, alors lisez la suite !

Si vous êtes nouveau en solidité, ne vous inquiétez pas, nous passerons en revue les bases également.

## Comment créer un NFT avec une personnalisation illimitée

Je vais vous faire démarrer avec ce [NFT Brownie Mix](https://github.com/PatrickAlphaC/nft-mix). Il s'agit d'un dépôt de travail avec beaucoup de code standard.

### Prérequis

Nous avons besoin de quelques éléments installés pour commencer :

* [Python](https://www.python.org/downloads/)
* [Nodejs](https://nodejs.org/en/download/) et npm
* [Metamask](https://metamask.io/)

Si vous n'êtes pas familier avec Metamask, vous pouvez [suivre ce tutoriel](https://docs.chain.link/docs/install-metamask) pour le configurer.

### Rinkeby Testnet ETH et LINK

Nous travaillerons également sur le testnet Rinkeby Ethereum, donc nous déployerons nos contrats sur une vraie blockchain, gratuitement !

Les testnets sont d'excellents moyens de tester comment nos contrats intelligents se comportent dans le monde réel. Nous avons besoin de Rinkeby ETH et Rinkeby LINK, que nous pouvons obtenir gratuitement à partir des liens vers les derniers robinets de la [documentation Chainlink](https://docs.chain.link/docs/link-token-contracts#rinkeby).

Nous devrons également ajouter le jeton LINK rinkeby à notre metamask, ce que nous pouvons faire en suivant la [documentation sur l'acquisition de LINK](https://docs.chain.link/docs/acquire-link).

Si vous êtes encore confus, [vous pouvez suivre cette vidéo](https://www.youtube.com/watch?v=4ZgFijd02Jo), assurez-vous simplement d'utiliser Rinkeby au lieu de Ropsten.

Lorsque vous travaillez avec une plateforme de contrats intelligents comme Ethereum, nous devons payer un peu d'ETH, et lorsque nous obtenons des données hors chaîne, nous devons payer un peu de LINK. C'est pourquoi nous avons besoin du LINK et de l'ETH de testnet.

Super, plongeons-nous. Voici [le NFT que nous allons déployer sur OpenSea](https://testnets.opensea.io/assets/0x8acb7ca932892eb83e4411b59309d44dddbc4cdf/0).

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-31-at-10.58.35-AM.png)

### Démarrage rapide

```bash
git clone https://github.com/PatrickAlphaC/nft-mix
cd nft-mix
```

Super ! Maintenant, nous devons installer `ganache-cli` et `eth-brownie`.

```
pip install eth-brownie
npm install -g ganache-cli
```

Maintenant, nous pouvons [définir nos variables d'environnement](https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html). Si vous n'êtes pas familier avec les variables d'environnement, vous pouvez simplement les ajouter dans votre fichier `.env`, puis exécuter :

`source .env`

Un exemple de `.env` devrait être dans le dépôt que vous venez de cloner avec les variables d'environnement commentées. Décommentez-les pour les utiliser !

Vous aurez besoin d'un `WEB3_INFURA_PROJECT_ID` et d'une `PRIVATE_KEY`. Le `WEB3_INFURA_PROJECT_ID` peut être trouvé en vous inscrivant pour un compte [Infura](https://infura.io/) gratuit. Cela nous donnera un moyen d'envoyer des transactions à la blockchain.

Nous aurons également besoin d'une clé privée, que vous pouvez obtenir à partir de votre Metamask. Cliquez sur les 3 petits points, puis sur `Détails du compte` et `Exporter la clé privée`. Veuillez NE PAS partager cette clé avec qui que ce soit si vous y mettez de l'argent réel !

```
export PRIVATE_KEY=VOTRE_CLE_ICI
export WEB3_INFURA_PROJECT_ID=VOTRE_ID_DE_PROJET_ICI
```

Maintenant, nous pouvons déployer notre contrat NFT et créer notre premier objet de collection avec les deux commandes suivantes.

```
brownie run scripts/simple_collectible/deploy_simple.py --network rinkeby
brownie run scripts/simple_collectible/create_collectible.py --network rinkeby
```

Le premier script déploie notre contrat NFT sur la blockchain Rinkeby, et le second crée notre premier objet de collection.

Vous venez de déployer votre premier contrat intelligent !

Il ne fait pas grand-chose du tout, mais ne vous inquiétez pas – je vais vous montrer comment le rendre sur OpenSea dans la partie avancée de ce tutoriel. Mais d'abord, regardons le standard de jeton ERC721.

## Le Standard de Jeton ERC721

Examinons le contrat que nous venons de déployer, dans le fichier `SimpleCollectible.sol`.

```javascript
// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleCollectible is ERC721 {
    uint256 public tokenCounter;
    constructor () public ERC721 ("Dogie", "DOG"){
        tokenCounter = 0;
    }

    function createCollectible(string memory tokenURI) public returns (uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newItemId;
    }

}

```

Nous utilisons le package [OpenZepplin](https://github.com/OpenZeppelin/openzeppelin-contracts) pour le jeton ERC721. Ce package que nous avons importé nous permet d'utiliser toutes les fonctions d'un jeton ERC721 typique. Cela définit toute la fonctionnalité que nos jetons vont avoir, comme `transfer` qui déplace les jetons vers de nouveaux utilisateurs, `safeMint` qui crée de nouveaux jetons, et plus encore.

Vous pouvez trouver toutes les fonctions qui sont données à notre contrat en consultant le [contrat de jeton ERC721 OpenZepplin](https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/token/ERC721/ERC721.sol). Notre contrat hérite de ces fonctions sur cette ligne :

```
contract SimpleCollectible is ERC721 {
```

C'est ainsi que Solidity gère l'héritage. Lorsque nous déployons un contrat, le `constructeur` est automatiquement appelé, et il prend quelques paramètres.

```
constructor () public ERC721 ("Dogie", "DOG"){
        tokenCounter = 0;
    }
```

Nous utilisons également le constructeur de l'`ERC721`, dans notre constructeur, et nous devons simplement lui donner un nom et un symbole. Dans notre cas, c'est "Dogie" et "DOG". Cela signifie que chaque NFT que nous créons sera de type Dogie/DOG.

C'est comme si chaque carte Pokémon était toujours un pokémon, ou chaque joueur de baseball sur une carte d'échange était toujours un joueur de baseball. Chaque joueur de baseball est unique, mais ils sont tous des joueurs de baseball. Nous utilisons simplement le type `DOG`.

Nous avons `tokenCounter` en haut qui compte combien de NFT nous avons créés de ce type. Chaque nouveau jeton obtient un `tokenId` basé sur le `tokenCounter` actuel.

Nous pouvons en fait créer un NFT avec la fonction `createCollectible`. C'est ce que nous appelons dans notre script `create_collectible.py`.

```
function createCollectible(string memory tokenURI) public returns (uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenCounter = tokenCounter + 1;
        return newItemId;
    }
```

La fonction `_safeMint` crée le nouveau NFT, et l'assigne à celui qui a appelé `createdCollectible`, aka le `msg.sender`, avec un `newItemId` dérivé du `tokenCounter`. C'est ainsi que nous pouvons garder une trace de qui possède quoi, en vérifiant le propriétaire du `tokenId`.

Vous remarquerez que nous appelons également `_setTokenURI`. Parlons-en.

## Qu'est-ce que les Métadonnées NFT et TokenURI ?

Lorsque les contrats intelligents étaient créés, et que les NFT étaient créés, les gens ont rapidement réalisé qu'il était vraiment très coûteux de déployer beaucoup de données sur la blockchain. Des images aussi petites qu'un KB peuvent facilement [coûter plus de 1M $ à stocker](https://ethereum.stackexchange.com/a/896/57451).

C'est clairement un problème pour les NFT, car avoir de l'art créatif signifie que vous devez stocker ces informations quelque part. Ils voulaient également une manière légère de stocker des attributs concernant un NFT – et c'est là que le tokenURI et les métadonnées entrent en jeu.

### TokenURI

Le `tokenURI` d'un NFT est un identifiant unique de ce à quoi le jeton "ressemble". Un URI pourrait être un appel d'API sur HTTPS, un hachage IPFS, ou [n'importe quoi d'autre](https://danielmiessler.com/study/difference-between-uri-url/) unique.

Ils suivent un standard de présentation des métadonnées qui ressemble à ceci :

```json
{
    "name": "nom",
    "description": "description",
    "image": "https://ipfs.io/ipfs/QmTgqnhFBMkfT9s8PHKcdXBn1f5bG3Q5hmBaR4U6hoTvb1?filename=Chainlink_Elf.png",
    "attributes": [
        {
            "trait_type": "trait",
            "value": 100
        }
    ]
}
```

Cela montre à quoi ressemble un NFT, et ses attributs. La section `image` pointe vers un autre URI de ce à quoi ressemble le NFT. Cela facilite le rendu des NFT sur leurs plateformes pour les plateformes NFT comme Opensea, Rarible et Mintable, puisque elles recherchent toutes ces métadonnées.

### Métadonnées Hors-Chaîne vs Métadonnées Sur-Chaîne

Maintenant, vous pourriez penser "attendez... si les métadonnées ne sont pas sur la chaîne, cela signifie-t-il que mon NFT pourrait disparaître à un moment donné" ? Et vous auriez raison.

Vous auriez également raison de penser que les métadonnées hors chaîne signifient que vous ne pouvez pas utiliser ces métadonnées pour faire interagir vos contrats intelligents entre eux.

C'est pourquoi nous voulons nous concentrer sur les métadonnées sur chaîne, afin que nous puissions programmer nos NFT pour qu'ils interagissent entre eux.

Nous avons toujours besoin de la partie `image` des métadonnées hors chaîne, cependant, puisque nous n'avons pas un bon moyen de stocker de grandes images sur la chaîne. Mais ne vous inquiétez pas, nous pouvons le faire gratuitement sur un réseau décentralisé en utilisant [IPFS](https://ipfs.io/).

Voici un exemple d'imageURI provenant d'IPFS qui montre le [Chainlink Elf](https://opensea.io/assets/0x8d78277bc2c63f07efc2c0c8a8512de4ad459a05/1) créé dans le [tutoriel Dungeons and Dragons](https://blog.chain.link/build-deploy-and-sell-your-own-dynamic-nft/).

![Créer un NFT](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-31-at-12.15.22-PM.png)
_Le Chainlink Elf_

Nous n'avons pas défini de tokenURI pour le NFT simple car nous voulions simplement montrer un exemple basique.

Passons maintenant au NFT avancé, afin que nous puissions voir certaines des fonctionnalités incroyables que nous pouvons faire avec les métadonnées sur chaîne, faire en sorte que le NFT soit rendu sur opensea, et faire lever notre Dogie !

Si vous voulez une vidéo de révision sur la section que nous venons de parcourir, suivez le [déploiement d'un NFT simple vidéo](https://www.youtube.com/watch?v=ZH_7nEIJDUY).

## NFT Dynamiques et Avancés

Les [NFT Dynamiques](https://blog.chain.link/build-deploy-and-sell-your-own-dynamic-nft/) sont des NFT qui peuvent changer au fil du temps, ou avoir des fonctionnalités sur chaîne que nous pouvons utiliser pour interagir entre eux. Ce sont les NFT qui ont la personnalisation illimitée pour nous permettre de créer des jeux entiers, des mondes, ou de l'art interactif de quelque sorte. Passons à la section avancée.

### Démarrage Rapide Avancé

Assurez-vous d'avoir suffisamment d'ETH et de LINK de testnet dans votre metamask, puis exécutez ce qui suit :

```
brownie run scripts/advanced_collectible/deploy_advanced.py --network rinkeby
brownie run scripts/advanced_collectible/create_collectible.py --network rinkeby
```

Notre objet de collection ici est une race de chien aléatoire retournée par le [Chainlink VRF](https://docs.chain.link/docs/chainlink-vrf). Chainlink VRF est un moyen d'obtenir des nombres aléatoires prouvables, et donc une véritable rareté dans nos NFT. Nous voulons ensuite créer ses métadonnées.

```
brownie run scripts/advanced_collectible/create_metadata.py --network rinkeby
```

Nous pouvons ensuite télécharger ces données sur IPFS afin d'avoir un tokenURI. Je vous montrerai comment faire cela plus tard. Pour l'instant, nous allons simplement utiliser l'exemple de tokenURI suivant :

```
https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=1-PUG.json
```

Si vous téléchargez [IPFS Companion](https://chrome.google.com/webstore/detail/ipfs-companion/nibjojkomfdiaoajekhjakgkdhaomnch?hl=en) dans votre navigateur, vous pouvez utiliser cette URL pour voir ce que l'URI retourne. Cela ressemblera à ceci :

```json
{
    "name": "PUG",
    "description": "Un adorable chiot PUG !",
    "image": "https://ipfs.io/ipfs/QmSsYRx3LpDAb1GZQm7zZ1AuHZjfbPkD6J7s9r41xu1mf8?filename=pug.png",
    "attributes": [
        {
            "trait_type": "mignonnerie",
            "value": 100
        }
    ]
}
```

Ensuite, nous pouvons exécuter notre script `set_tokenuri.py` :

```
brownie run scripts/advanced_collectible/set_tokenuri.py --network rinkeby
```

Et nous obtiendrons une sortie comme celle-ci :

```
Exécution de 'scripts/advanced_collectible/set_tokenuri.py::main'...
Travail sur rinkeby
Transaction envoyée : 0x8a83a446c306d6255952880c0ca35fa420248a84ba7484c3798d8bbad421f88e
  Prix du gaz : 1.0 gwei   Limite de gaz : 44601   Nonce : 354
  AdvancedCollectible.setTokenURI confirmé - Bloc : 8331653   Gaz utilisé : 40547 (90.91%)

Super ! Vous pouvez voir votre NFT à l'adresse https://testnets.opensea.io/assets/0x679c5f9adC630663a6e63Fa27153B215fe021b34/0
Veuillez patienter jusqu'à 20 minutes, et cliquez sur le bouton "rafraîchir les métadonnées"
```

Et nous pouvons cliquer sur le lien donné pour voir à quoi il ressemble sur Opensea ! Vous devrez peut-être cliquer sur le bouton `rafraîchir les métadonnées` et attendre quelques minutes.

![Créer un NFT](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-31-at-12.33.42-PM.png)
_Rafraîchir les Métadonnées_

## La Race Aléatoire

Parlons de ce que nous venons de faire. Voici notre `AdvancedCollectible.sol` :

```
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract AdvancedCollectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    enum Breed{PUG, SHIBA_INU, BRENARD}
    // ajouter d'autres choses
    mapping(bytes32 => address) public requestIdToSender;
    mapping(bytes32 => string) public requestIdToTokenURI;
    mapping(uint256 => Breed) public tokenIdToBreed;
    mapping(bytes32 => uint256) public requestIdToTokenId;
    event requestedCollectible(bytes32 indexed requestId); 


    bytes32 internal keyHash;
    uint256 internal fee;
    uint256 public randomResult;
    constructor(address _VRFCoordinator, address _LinkToken, bytes32 _keyhash)
    public 
    VRFConsumerBase(_VRFCoordinator, _LinkToken)
    ERC721("Dogie", "DOG")
    {
        tokenCounter = 0;
        keyHash = _keyhash;
        fee = 0.1 * 10 ** 18;
    }

    function createCollectible(string memory tokenURI, uint256 userProvidedSeed) 
        public returns (bytes32){
            bytes32 requestId = requestRandomness(keyHash, fee, userProvidedSeed);
            requestIdToSender[requestId] = msg.sender;
            requestIdToTokenURI[requestId] = tokenURI;
            emit requestedCollectible(requestId);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        address dogOwner = requestIdToSender[requestId];
        string memory tokenURI = requestIdToTokenURI[requestId];
        uint256 newItemId = tokenCounter;
        _safeMint(dogOwner, newItemId);
        _setTokenURI(newItemId, tokenURI);
        Breed breed = Breed(randomNumber % 3); 
        tokenIdToBreed[newItemId] = breed;
        requestIdToTokenId[requestId] = newItemId;
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "ERC721: transfer caller is not owner nor approved"
        );
        _setTokenURI(tokenId, _tokenURI);
    }
}

```

Nous utilisons le Chainlink VRF pour créer une race aléatoire à partir d'une liste de `PUG, SHIBA_INU, BRENARD`. Lorsque nous appelons `createCollectible` cette fois, nous avons en fait lancé une demande au nœud Chainlink VRF hors chaîne, et nous avons obtenu un nombre aléatoire pour créer le NFT avec l'une de ces 3 races.

Utiliser une véritable aléatoire dans vos NFT est un excellent moyen de créer une véritable rareté, et utiliser un nombre aléatoire d'oracle Chainlink signifie que votre nombre est prouvablement aléatoire, et ne peut pas être influencé par les mineurs.

Vous pouvez en savoir plus sur [Chainlink VRF dans la documentation](https://docs.chain.link/docs/chainlink-vrf).

Le nœud Chainlink répond en appelant la fonction `fulfillRandomness`, et crée l'objet de collection en fonction du nombre aléatoire. Nous devons encore appeler `_setTokenURI` pour donner à notre NFT l'apparence dont il a besoin.

Nous n'avons pas donné d'attributs à notre NFT ici, mais les attributs sont un excellent moyen de faire combattre et interagir nos NFT. Vous pouvez voir un excellent exemple de NFT avec des attributs dans cet [exemple Dungeons and Dragons](https://github.com/PatrickAlphaC/dungeons-and-dragons-nft).

### Métadonnées depuis IPFS

Nous utilisons IPFS pour stocker deux fichiers :

1. L'image du NFT (l'image du pug)
2. Le fichier tokenURI (le fichier JSON qui inclut également le lien de l'image)

Nous utilisons IPFS car c'est une plateforme décentralisée gratuite. Nous pouvons ajouter nos tokenURIs et images à IPFS en téléchargeant [IPFS desktop](https://docs.ipfs.io/install/ipfs-desktop/), et en cliquant sur le bouton `importer`.

![Créer un NFT](https://www.freecodecamp.org/news/content/images/2021/03/Screen-Shot-2021-03-31-at-12.43.13-PM.png)
_IPFS ajouter un fichier_

Ensuite, nous pouvons partager l'URI en cliquant sur les 3 points à côté du fichier que nous voulons partager, en cliquant sur `partager le lien` et en copiant le lien donné. Nous pouvons ensuite ajouter ce lien dans notre fichier `set_tokenuri.py` pour changer le token URI que nous voulons utiliser.

### Persistance

Cependant, si le tokenURI est uniquement sur notre nœud, cela signifie que lorsque notre nœud est hors ligne, personne d'autre ne peut le voir. Nous voulons donc que d'autres personnes `épinglent` notre NFT. Nous pouvons utiliser un service d'épinglage comme [Pinata](https://pinata.cloud/) pour aider à garder nos données en vie même lorsque notre nœud IPFS est hors ligne.

J'imagine qu'à l'avenir, de plus en plus de métadonnées seront stockées sur IPFS et des plateformes de stockage décentralisées. Les serveurs centralisés peuvent tomber en panne, et cela signifierait que l'art sur ces NFT est perdu à jamais. Assurez-vous de vérifier où se trouve le tokenURI du NFT que vous utilisez !

Je m'attends également à ce que, à l'avenir, plus de personnes utilisent des plateformes dStorage comme [Filecoin](https://docs.filecoin.io/), car l'utilisation d'un service d'épinglage n'est pas aussi décentralisée qu'elle devrait l'être.

## Aller de l'avant

Si vous souhaitez une visite vidéo de l'NFT avancé, vous pouvez regarder la [vidéo NFT avancée](https://www.youtube.com/watch?v=tCR7b9p9GiM).

Maintenant, vous avez les compétences pour créer de beaux NFT amusants, personnalisables, interactifs, et les rendre sur un marché.

Les NFT sont des moyens amusants et puissants pour que les artistes soient récompensés pour tout le travail acharné qu'ils font. Bonne chance, et n'oubliez pas de vous amuser !