---
title: Créer un token Ethereum en utilisant des contrats open source (open-zeppelin)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-24T20:55:38.000Z'
originalURL: https://freecodecamp.org/news/create-an-ethereum-token-using-open-source-contracts-open-zeppelin-1e132e6233ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eE-UPqBn00vcDzo95me5Qw.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Créer un token Ethereum en utilisant des contrats open source (open-zeppelin)
seo_desc: 'By Danny

  I want to show you that creating a best practice token is a simple process. To be
  honest, we are going to be doing some coding, but it won’t be much.

  We’ll be using Solidity to create our Ethereum token. But don’t worry, there are
  a lot of o...'
---

Par Danny

Je veux vous montrer que créer un token conforme aux meilleures pratiques est un processus simple. Pour être honnête, nous allons faire un peu de codage, mais ce ne sera pas beaucoup.

Nous allons utiliser Solidity pour créer notre token Ethereum. Mais ne vous inquiétez pas, il existe de nombreuses bibliothèques et contrats open source pour nous aider dans ce processus.

Ce que nous voulons, c'est un token conforme **ERC-20**. Cela signifie que les développeurs Ethereum ont décidé d'un ensemble de fonctionnalités nécessaires pour les usages les plus courants des tokens aujourd'hui. Il existe d'autres types de normes ERC, mais nous n'allons pas nous y attarder.

**Exigences :**

* Github
* Terminal
* NodeJS
* NPM
* Metamask (Pour la création initiale du compte)

Très bien, commençons à coder ! La première chose que nous voulons faire est de télécharger `truffle` globalement. Vous pouvez visiter leur dépôt à l'adresse [truffle](https://github.com/trufflesuite/truffle) et voici le snippet suivant pour l'installation :

```
npm install -g truffle
```

***note** : assurez-vous d'avoir la dernière version de truffle si vous l'avez installé auparavant

Truffle gérera la compilation, la liaison et le déploiement des contrats intelligents pour nous. C'est une bibliothèque qui facilitera notre tâche pour cette démonstration.

Maintenant, nous devons créer un répertoire où notre projet résidera. Dans mon cas, je l'ai appelé **ethereum_token_tutorial**.

Nous avons donc deux options ici. Soit vous pouvez cloner le dépôt que j'ai créé en suivant ces instructions :

```
git clone -b initial_step https://git@github.com/danieljoonlee/ethereum_token_tutorial.git
```

Soit vous pouvez faire ceci dans votre terminal à l'intérieur de votre nouveau répertoire :

```
truffle init
```

Si vous avez suivi la deuxième option en faisant `truffle init`. Le répertoire devrait ressembler à ceci :

```
etherem_token_tutorial|___contracts| |_____ConvertLib.sol| |_____MetaCoin.sol| |_____Migrations.sol|___migrations| |_____1_initial_migrations.js| |_____2_deploy_contracts.js|___test| |_____TestMetacoin.sol| |_____metacoin.js|___truffle.js
```

Allez-y et supprimez `ConvertLib.sol`, `MetaCoin.sol`, `TestMetacoin.sol`, `metacoin.js`.

Votre répertoire devrait maintenant ressembler à ceci :

```
etherem_token_tutorial|___contracts| |_____Migrations.sol|___migrations| |_____1_initial_migrations.js| |_____2_deploy_contracts.js|___test|___truffle.js
```

Super. Maintenant, nous avançons. Truffle nous aide à compiler les contrats intelligents et à les déployer. Mais nous avons supprimé nos fichiers de contrats intelligents autres que l'aide à la migration. Ne vous inquiétez pas, c'est là qu'intervient Open-Zeppelin.

`Open-Zeppelin` est un dépôt open source où vous pouvez trouver des contrats intelligents avec généralement les meilleures pratiques, une bonne couverture de test, et très probablement audités*.

* _Un audit est lorsque vous avez des développeurs professionnels qui examinent vos contrats intelligents à la recherche de fuites, de bugs ou de possibilités d'attaques malveillantes._

Voici un lien si vous êtes intéressé par les attaques de contrats intelligents : [Lien](https://medium.com/@merunasgrincalaitis/how-to-audit-a-smart-contract-most-dangerous-attacks-in-solidity-ae402a7e7868)

Pour utiliser les contrats `Open-Zeppelin`, nous devons l'installer dans notre dépôt :

```
npm init -ynpm install -E zeppelin-solidity
```

Nous avons initialisé un package.json avec npm init -y. Nous avons également installé le package pour utiliser les contrats Open-Zeppelin.

D'accord, nous allons écrire un peu de Solidity. J'ai mentionné dans l'article plus tôt que cela ne serait pas beaucoup de code et je ne plaisantais pas !

Créez un nouveau fichier dans le dossier `contracts`. Dans mon cas, je l'ai nommé `TestToken.sol`

Maintenant, votre répertoire devrait ressembler à ceci :

```
etherem_token_tutorial|___contracts| |_____Migrations.sol| |_____TestToken.sol***(celui-ci est nouveau)|___migrations| |_____1_initial_migrations.js| |_____2_deploy_contracts.js|___test|___truffle.js
```

Dans `TestToken.sol`, nous devons avoir le code suivant :

```
// TestToken.solpragma solidity ^0.4.18;
```

```
import "zeppelin-solidity/contracts/token/ERC20/MintableToken.sol";
```

```
contract TestToken is MintableToken {    string public constant name = "Test Token";    string public constant symbol = "TT";    uint8 public constant decimals = 18;}
```

Décomposons cela puisque c'est un peu dense, même si ce n'est que quelques lignes de code.

`pragma solidity ^0.4.18;`

Il est requis en haut du fichier car il spécifie la version de Solidity que nous utilisons.

```
import "zeppelin-solidity/contracts/token/ERC20/MintableToken.sol";
```

Le snippet de code ci-dessus est la raison pour laquelle Open-Zeppelin est si utile. Si vous savez comment fonctionne l'héritage, notre contrat hérite de MintableToken. Si vous ne savez pas comment fonctionne l'héritage, MintableToken a beaucoup de fonctionnalités sauvegardées dans MintableToken.sol. Nous pouvons utiliser ces fonctionnalités pour créer notre token. Si vous visitez ce [MintableToken](https://github.com/OpenZeppelin/zeppelin-solidity/blob/master/contracts/token/ERC20/MintableToken.sol), vous remarquerez une tonne de fonctions et encore plus d'héritage. Cela peut être un peu un terrier de lapin, mais pour le but de cette démonstration, je veux que nous publiions un token dans le testnet.

Pour nous, Mintable nous permet de créer autant de tokens que nous voulons, donc nous ne commencerons pas avec une offre initiale. Dans mon prochain article, nous créerons un service nodejs qui créera de nouveaux tokens et gérera d'autres fonctionnalités standards ERC-20.

Le prochain morceau de code :

```
contract TestToken is MintableToken {    string public constant name = "Test Token";    string public constant symbol = "TT";    uint8 public constant decimals = 18;}
```

C'est là que nous pouvons personnaliser le token. Dans mon cas, je l'ai nommé "Test Token", avec le symbole "TT", et 18 décimales. Mais pourquoi 18 décimales ?

18 décimales est assez standard dans la communauté. Donc si nous avons un test token, il peut potentiellement ressembler à ceci : 1.111111111111111111.

Voilà. C'est tout le codage Solidity dont nous avons besoin pour ce token. Nous héritons de toutes les fonctionnalités principales pour un token ERC 20 standardisé à partir d'Open-Zeppelin. Après cela, nous devons définir nos constantes pour le nom, le symbole et les décimales.

Avant d'oublier, nous devons créer un compte Metamask et le financer avec de l'ether de testnet.

Allez-y et recherchez l'extension `MetaMask` pour Chrome, ou suivez ce [lien](https://chrome.google.com/webstore/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn?hl=en)

![Image](https://cdn-media-1.freecodecamp.org/images/Ku4UgJTh5NkieV0u5N0bz7DwguV7tm3haPCG)
_Extension Metamask pour Google Chrome_

Après avoir installé MetaMask, vous devriez voir une série d'étapes. Vous pouvez lire les conditions de service. Finalement, vous atteindrez :

![Image](https://cdn-media-1.freecodecamp.org/images/qL7f7xIaYPd47FVOeJSrOwjVY7UFkPtZSxiU)
_Écran de mot de passe Metamask_

Saisissez votre mot de passe et confirmez ce mot de passe. En cliquant sur créer, vous verrez un autre écran.

![Image](https://cdn-media-1.freecodecamp.org/images/xGDUdHZfmrKiwkWN4326tleb57BEnR7K3ZHf)
_Secret Metamask_

Assurez-vous de sauvegarder vos mots de passe ou de les copier dans un fichier texte. Nous aurons besoin de ces mots de passe pour déployer le token sur le testnet.

Aussi plus **important**, changez votre test de Mainnet Test Net à Ropsten Test net. C'est en haut à gauche de votre onglet MetaMask. Voici le menu déroulant :

![Image](https://cdn-media-1.freecodecamp.org/images/AIrKEnmtyT5LBg9skSuZgB-hCP1hTApLujWL)
_Liste des testnets_

La raison pour laquelle nous utilisons le réseau de test Ropsten est qu'il est le testnet/implémentation le plus proche du réseau principal Ethereum.

Ensuite, vous devrez copier votre adresse dans le presse-papiers à partir du menu `...` comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/BPKJes6P8mD8Eeq5d2R6hzh8CA7k6ELYUI6u)
_Écran de compte Metamask_

Vous devriez avoir une adresse similaire à celle-ci copiée dans votre presse-papiers :

```
address: 0x8EeF4Fe428F8E56d2202170A0bEf62AAc93989dE
```

C'est l'adresse à partir de laquelle nous allons déployer notre contrat de token. Maintenant, une chose que vous devez savoir sur le déploiement des contrats est qu'ils coûtent de l'Ethereum, plus précisément du Gas. Nous allons avoir besoin d'obtenir un peu d'Ethereum de testnet dans nos comptes.

Maintenant que vous avez votre adresse, allez à ce lien de robinet Ropsten :

[**Robinets Ethernet**](http://faucet.ropsten.be:3001/)
[_Edit description_faucet.ropsten.be](http://faucet.ropsten.be:3001/)

Copiez et collez votre adresse et bientôt vous devriez avoir 1 Ethereum dans votre portefeuille MetaMask pour votre adresse.

![Image](https://cdn-media-1.freecodecamp.org/images/qzFb76GBmq7umMUjZNksh2Nvxq5m00TuUzkv)
_Compte avec 1 ethereum_

Une dernière chose avant de commencer à coder notre processus de déploiement ! Nous allons utiliser une API gratuite appelée `Infura.io` :

[**Infura — Infrastructure Blockchain Évolutive**](https://infura.io/)
[_Accès sécurisé, fiable et évolutif aux API Ethereum et aux passerelles IPFS._infura.io](https://infura.io/)

Inscrivez-vous à leurs services. Vous devriez recevoir un email de leur part ou être redirigé vers un site avec votre clé API. Celle que nous voulons spécifiquement est celle du réseau Ropsten.

```
Test Ethereum Network (Ropsten)https://ropsten.infura.io/API_KEY
```

Copiez votre API_KEY.

Presque là ! Maintenant, commençons à travailler sur notre déploiement. Retournez dans notre code.

Tout d'abord, parlons de la sécurité. Créez un nouveau fichier dans votre répertoire racine appelé `.env`. Votre structure de fichiers devrait maintenant ressembler à ceci :

```
etherem_token_tutorial|___contracts| |_____Migrations.sol| |_____TestToken.sol|___migrations| |_____1_initial_migrations.js| |_____2_deploy_contracts.js|___test|___truffle.js|___.env**(nouveau fichier)
```

À l'intérieur de votre fichier `.env`, ajoutons quelques variables d'environnement (ce sont des variables auxquelles vous pouvez accéder n'importe où dans votre répertoire de code)

```
//.env fileINFURA_API_KEY=API_KEYMNENOMIC=MNEOMIC_FROM_METAMASK
```

Tout d'abord, ajoutez votre API_KEY que vous avez copiée dans le fichier.

Vous vous souvenez de la Mneomic (mots de passe) de l'initialisation de l'extension Chrome Metamask ? Nous en aurons besoin maintenant pour déployer les contrats. Si vous avez téléchargé ou noté votre Mneomic, notez-les maintenant dans votre fichier `.env` `MNENOMIC=SOME KEY PHRASE YOU DONT WANT THE PUBLIC TO KNOW`.

**IMPORTANT*****

Nous avons ajouté un fichier `.env` !!! Nous devons maintenant ajouter un fichier `.gitignore` pour éviter d'ajouter le `.env` à un dépôt public si vous décidez un jour de rendre le code public !

Créez un fichier `.gitignore` dans le même répertoire que votre `.env`. Maintenant, il devrait ressembler à ceci :

```
etherem_token_tutorial|___contracts| |_____Migrations.sol| |_____TestToken.sol|___migrations| |_____1_initial_migrations.js| |_____2_deploy_contracts.js|___test|___truffle.js|___.env|___.gitignore**(nouveau fichier)
```

À l'intérieur de votre fichier `.gitignore` :

```
// .gitignorenode_modules/build/.env
```

Nous voulons ignorer `node_modules/` car lorsque nous faisons `npm install`, il téléchargera les packages de notre `package.json`. Nous voulons ignorer `build` car plus tard, lorsque nous exécuterons un script, il créera ce répertoire pour nous automatiquement. Nous voulons également ignorer `.env` car il contient des informations privées que nous ne voulons pas rendre publiques.

Super ! Dans notre terminal, nous devons ajouter deux modules supplémentaires.

```
npm install --save dotenv truffle-hdwallet-provider
```

Puisque nous mettons des informations privées, nous avons besoin d'un moyen d'accéder à ces variables à partir de `.env`, et le package `dotenv` nous aidera.

Le deuxième package, truffle-hdwallet-provider, est un fournisseur de portefeuille activé. Sans cela, nous devrions télécharger tous les blocs ou utiliser un portefeuille léger pour effectuer de nouvelles transactions dans le réseau Ethereum. Avec le fournisseur de portefeuille et l'API Infura, nous pouvons déployer instantanément, en contournant également des processus douloureux.

Dans le fichier `truffle.js` de notre répertoire racine, nous devons modifier certaines configurations.

```
// truffle.jsrequire('dotenv').config();const HDWalletProvider = require("truffle-hdwallet-provider");
```

```
module.exports = {  networks: {    development: {      host: "localhost",      port: 7545,      gas: 6500000,      network_id: "5777"    },    ropsten: {        provider: new HDWalletProvider(process.env.MNENOMIC, "https://ropsten.infura.io/" + process.env.INFURA_API_KEY),        network_id: 3,        gas: 4500000    },  }};
```

La première ligne indique que nous voulons utiliser les variables `.env` dans ce dépôt. Généralement, dans la plupart des applications, vous n'avez besoin de le requérir qu'une seule fois dans le fichier de configuration de démarrage.

La plupart de cela est du code standard. La section principale sur laquelle nous voulons nous concentrer est le réseau ropsten.

```
ropsten: {        provider: new HDWalletProvider(process.env.MNENOMIC, "https://ropsten.infura.io/" + process.env.INFURA_API_KEY),        network_id: 3,        gas: 4500000    },
```

Le fournisseur est notre réseau. Dans notre cas, nous voulons déployer notre token dans le réseau `Ropsten`. En utilisant le `HDWalletProvider`, nous passons deux arguments, `process.env.MNENOMIC, "https://ropsten.infura.io/" + process.env.INFURA_API_KEY`. Nous accédons à nos variables `.env` en référençant `process.env.VARIABLE_NAME_IN_ENV`.

Nous définissons le `network_id: 3` car cela représente Ropsten. `1` est le réseau principal Ethereum et `2` est un ancien testnet.

Enfin, nous définissons `gas: 4500000`, ce qui explique pourquoi nous avions besoin de l'Ethereum à l'origine. Nous utilisons `gas/ethereum` chaque fois que nous devons modifier/ajouter quelque chose dans le réseau Ethereum.

Très bien, passons à la dernière étape avant le déploiement !

Dans notre fichier `migrations/2_deploy_contract.js`, nous devons apporter quelques modifications pour notre contrat.

```
// 2_deploy_contract.js
```

```
const TestToken = artifacts.require("./TestToken.sol");
```

```
module.exports = function(deployer) {  deployer.deploy(TestToken);};
```

Si vous avez nommé votre fichier de contrat de token autre chose, vous devez remplacer `TestToken.sol` par le nom de fichier que vous lui avez donné.

```
truffle compile
```

Cela devrait créer un nouveau dossier dans votre répertoire :

```
etherem_token_tutorial|___build| |_____contracts|    |_____BasicToken.json|    |_____ERC20.json|    |_____ERC20Basic.json|    |_____Migrations.json|    |_____MintableToken.json|    |_____Ownable.json|    |_____SafeMath.json|    |_____StandardToken.json|    |_____TestToken.json|___contracts| |_____Migrations.sol| |_____TestToken.sol|___migrations| |_____1_initial_migrations.js| |_____2_deploy_contracts.js|___test|___truffle.js|___.env|___.gitignore**(nouveau fichier)
```

Dans notre dossier build, nous avons un tas de contrats que nous avons hérités de la bibliothèque Open-Zeppelin. Si vous souhaitez en savoir plus sur les normes ERC-20, je vous invite à consulter le wiki. Si suffisamment de personnes le demandent, je peux faire un autre article de blog à ce sujet. Pour l'instant, voici le lien vers le [wiki](https://theethereum.wiki/w/index.php/ERC20_Token_Standard).

Voici le moment de vérité. Maintenant, nous devons déployer les contrats dans le réseau Ropsten. Entrez la ligne suivante dans votre terminal :

```
truffle migrate --network ropsten
```

Vous devriez obtenir une série de lignes dans votre terminal comme :

```
Using network 'ropsten'.
```

```
Running migration: 1_initial_migration.js  Deploying Migrations...  ... 0x7494ee96ad7db4a560b6f3169e0666c3938f9f54208f7972ab902feb049a7f68  Migrations: 0x254466c5b09f141ce1f93689db6257b92133f51aSaving successful migration to network...  ... 0xd6bc06b3bce3d15dee4b733e5d4b09f0adb8f93f75ad980bad078484641d36e5Saving artifacts...Running migration: 2_deploy_contracts.js  Deploying TestToken...  ... 0x7e5c1b37f1e509aea59cd297417efe93eb49fdab2c72fa5c37dd2c63a3ba67b7  TestToken: 0x02ec6cbd89d3a435f8805e60e2703ef6d3147f96Saving successful migration to network...  ... 0x2fd6d699295d371ffd24aed815a13c5a44e01b62ca7dc6c9c24e2014b088a34eSaving artifacts...
```

Cela prendra un certain temps. Une fois qu'il est entièrement déployé, copiez le dernier txid. Dans mon cas :

```
0x2fd6d699295d371ffd24aed815a13c5a44e01b62ca7dc6c9c24e2014b088a34e
```

Cela aura une adresse vers votre contrat de token. Voici un lien vers mon txid :

[**Transaction Ropsten 0x2fd6d699295d371ffd24aed815a13c5a44e01b62ca7dc6c9c24e2014b088a34e**](https://ropsten.etherscan.io/tx/0x2fd6d699295d371ffd24aed815a13c5a44e01b62ca7dc6c9c24e2014b088a34e)
[_Ropsten (ETH) detailed transaction info for 0x2fd6d699295d371ffd24aed815a13c5a44e01b62ca7dc6c9c24e2014b088a34e_ropsten.etherscan.io](https://ropsten.etherscan.io/tx/0x2fd6d699295d371ffd24aed815a13c5a44e01b62ca7dc6c9c24e2014b088a34e)

Qui a une adresse vers le contrat lui-même :

[**Comptes Ropsten, Adresse et Contrats**](https://ropsten.etherscan.io/address/0x254466c5b09f141ce1f93689db6257b92133f51a)
[_The Ethereum BlockChain Explorer, API and Analytics Platform_ropsten.etherscan.io](https://ropsten.etherscan.io/address/0x254466c5b09f141ce1f93689db6257b92133f51a)

Vous pouvez obtenir le dépôt github complet [ici](https://github.com/danieljoonlee/ethereum_token_tutorial).

Ceci est la première partie d'une série sur la création d'un token et l'interaction avec celui-ci. Dans le prochain blog, nous créerons un simple microservice node. Nous utiliserons ce service pour appeler diverses fonctions sur votre contrat intelligent de token, telles que la création de nouveaux tokens, le transfert, etc.

Si vous trouvez des erreurs ou des coquilles, faites-le moi savoir ! Je suis également toujours à la recherche de projets passionnants dans l'espace blockchain.

Si vous avez trouvé cela utile et que vous avez envie de m'offrir une bière :

BTC : 3Kxz6zPweuiaVG28W78pX9DoEZVkLhH4nT

BCH : qqwusc2peyvlh3wgl0tpt3ll4ug9zujfvy9586tgd4

ETH : 0x96Ee87e22D899BDc27EAD4fE3FCA8e9F39176B4C

LTC : MDhqUBtGgVZrDG7TYzzyK2a2b99sHyHaQQ