---
title: Tutoriel Blockchain pour débutants – Apprendre à coder des contrats intelligents
  avec JavaScript et Solidity
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-11-17T21:42:46.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-blockchain
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-archie-binamira-705075.jpg
tags:
- name: beginners guide
  slug: beginners-guide
- name: Blockchain
  slug: blockchain
- name: Smart Contracts
  slug: smart-contracts
- name: Solidity
  slug: solidity
- name: Web3
  slug: web3
seo_title: Tutoriel Blockchain pour débutants – Apprendre à coder des contrats intelligents
  avec JavaScript et Solidity
seo_desc: "By Njoku Samson Ebere\nThe first time I tried to learn blockchain development,\
  \ I felt overwhelmed. \nThis tutorial you're reading is what I wish I could send\
  \ back in time to myself. \nThis will give you a strong foundation in blockchain\
  \ development, and..."
---

Par Njoku Samson Ebere

La première fois que j'ai essayé d'apprendre le développement blockchain, je me suis senti submergé. 

Ce tutoriel que vous lisez est ce que j'aurais aimé envoyer dans le passé à moi-même. 

Cela vous donnera une base solide en développement blockchain et vous préparera à réussir dans la programmation de vos propres contrats intelligents.

En plus de mes explications et exemples de code, j'ai inclus de nombreuses vidéos que vous pouvez utiliser pour compléter votre apprentissage.

## Prérequis

Ce tutoriel suppose que vous comprenez certains concepts de codage fondamentaux. L'un de ceux qui sera particulièrement utile est le concept de programmation orientée objet (POO).

## Qu'est-ce que la Blockchain ?

La Blockchain est un réseau de transactions ou d'actifs appelés blocs où chaque bloc est connecté aux autres. Tout le monde ici a un accès égal aux données circulant dans le réseau.

%[https://youtu.be/GvmRSS0vKxE]

Vous pouvez voir la blockchain comme un document qui contient les détails des transactions effectuées par un groupe de personnes où chacun possède une copie. Tout le monde doit être d'accord sur les mises à jour avant qu'elles ne soient acceptées. 

Quiconque tente de falsifier son document sans le consentement des autres est considéré comme frauduleux et subira des conséquences prédéfinies.

Par exemple, imaginez qu'un groupe d'amis (Njoku, Samson et Ebere) décide de créer un compte d'épargne pair-à-pair qui doit fonctionner pendant une certaine période avant qu'un retrait ne soit possible. Les trois conviennent que personne ne sera le patron, et chaque personne aura un accès égal au compte pour garantir la confiance. Ils ouvrent donc un compte. 

Chaque fois que l'un d'eux dépose de l'argent, tout le monde reçoit un nouveau document d'historique de compte par e-mail. Chaque fois qu'ils décident d'ajouter un nouveau membre, la personne devient partie des signataires et reçoit une copie de l'historique du compte. 

Tout le monde doit consentir avant qu'un retrait ne se produise en dehors de la date proposée. Le non-respect de ces termes entraînera des conséquences telles que la perte de toutes les économies d'une personne ou le départ de l'association après avoir payé une amende.

La blockchain est connue comme une technologie décentralisée puisque les données et l'autorité sont partagées également entre tous les membres du réseau. Elle diffère des applications centralisées où l'entreprise possède les données, et les consommateurs espèrent simplement que leurs données ne seront pas mal utilisées. 

Des exemples d'applications décentralisées incluent Bitcoin et Ethereum, tandis que les applications centralisées incluent Facebook et Google.

La technologie blockchain appartient à la catégorie du **Web 3** simplement parce qu'elle est la troisième phase de l'internet dans laquelle les utilisateurs peuvent **lire, écrire et posséder des données**. Le Web 1 était l'étape où les utilisateurs ne pouvaient que **lire des données**. Le **Web 2** est apparu vers le début des années 2000 et est la phase dans laquelle les utilisateurs peuvent **lire et écrire des données**.

## Comment fonctionne la Blockchain

Dans cette section, je vais expliquer ce qui se passe dans une application blockchain en coulisses. 

Nous commencerons par examiner comment cela fonctionne en théorie, puis comment nous pouvons le reproduire en utilisant un langage de programmation que de nombreux développeurs connaissent déjà – JavaScript.

%[https://youtu.be/jWXH-49BAPU]

### Théorie derrière la Blockchain

Une blockchain est une connexion de nombreux blocs. Elle commence donc par un bloc appelé **bloc genesis**. Parmi d'autres choses, un bloc contient un hash, le hash du bloc précédent et au moins une transaction.

Chaque bloc de la blockchain conserve un enregistrement de son hash et du hash du bloc précédent pour protéger le réseau des pirates.

Cela implique que pour qu'un pirate accède et brise le réseau, il doit générer les hashs et les faire correspondre au bon bloc sans briser les autres blocs. Maintenant, cela semble vraiment stressant et presque impossible. C'est ainsi que les blockchains sont sécurisées.

Ensuite, tout utilisateur du réseau peut effectuer au moins une transaction. Si l'utilisateur a terminé un ensemble de transactions dont il a besoin à un moment donné, il peut utiliser ces transactions pour créer un bloc. Le bloc peut maintenant être ajouté aux autres. 

L'ensemble du processus d'ajout d'un nouveau bloc est connu sous le nom de **minage**. Le processus sécurise et vérifie les transactions contenues dans un bloc.

Le hash d'un bloc est généré lors du minage. Le processus de calcul du hash est connu sous le nom de **preuve de travail**.

### Blockchain en pratique

Utilisons la programmation orientée objet JavaScript pour démontrer comment fonctionne la blockchain. Nous utilisons la méthode OOP car la programmation blockchain utilise le même modèle. 

Mais avant de commencer à construire, apprenons comment générer le hash pour chaque bloc dans une blockchain.

#### Comment générer le hash d'un bloc

Il existe de nombreuses bibliothèques pour générer le hash d'un bloc. Mais nous utiliserons la bibliothèque [SHA256](https://www.npmjs.com/package/sha256) pour ce tutoriel. SHA256 est la plus populaire et est utilisée par de nombreuses entreprises renommées.

La bibliothèque SHA256 prend toute donnée qui lui est donnée et retourne une chaîne de 64 caractères. Chaque chaîne passée à la bibliothèque SHA256 retournera toujours la même chaîne de 64 caractères à chaque fois. 

Vous pouvez consulter [https://emn178.github.io/online-tools/sha256.html](https://emn178.github.io/online-tools/sha256.html) et jouer avec l'interface utilisateur pour voir comment cela fonctionne.

Les blockchains n'utilisent pas n'importe quel hash généré pour des raisons de sécurité. Elles spécifient à quoi doivent ressembler les premiers caractères pour que le hash soit accepté. Cela signifie que le hash devra être généré plusieurs fois, et un enregistrement des changements à chaque itération sera conservé à des fins de référence.

Par exemple, une blockchain peut spécifier que le seul hash acceptable doit contenir trois zéros au début. 

Pour calculer le hash, nous devons ajouter un nombre connu sous le nom de `nonce` à la chaîne à hacher. Le `nonce` commence généralement à zéro et est incrémenté chaque fois que le hash est généré jusqu'à ce qu'un hash commençant par trois zéros soit trouvé. Ensuite, le hash et le `nonce` seront stockés à des fins de référence.

Le code ci-dessous calculera le hash pour "man" :

```javascript
SHA256("man").toString()
```

Cependant, nous pouvons exécuter la fonction plusieurs fois pour obtenir une chaîne avec trois zéros au début. Puisque la fonction retournera toujours le même résultat, nous devons ajouter un nombre à la chaîne et l'incrémenter jusqu'à ce que nous obtenions le hash souhaité.

Le code que nous utiliserions pour cela ressemblerait à ceci :

```javascript
let hash = "";
let nonce = 0;

while (hash.substring(0, 3) !== "000") {
  nonce++;
  hash = SHA256("man" + nonce).toString();
}

console.log(nonce);
console.log(hash);
```

Ce code produira `000d6575d4670dae39df9944e54c27dc4837beab1db23e2de264a7c1a3f38b1a` après `5707` tentatives au lieu de `48b676e2b107da679512b793d5fd4cc4329f0c7c17a97cf6e0e3d1005b600b03`.

Ce niveau de mesures de sécurité prises pour construire des applications blockchain les rend très fiables et acceptables.

Maintenant que nous comprenons comment un hash est généré dans la blockchain, revenons à la démonstration de son fonctionnement.

### Comment fonctionne la Blockchain en utilisant JavaScript

Tout d'abord, créez un répertoire appelé **intro_to_blockchain**. Ensuite, ouvrez le répertoire dans un terminal.

Exécutez la commande suivante et appuyez sur Entrée pour toutes les invites afin d'initialiser le projet :

```
npm init
```

Créez 2 fichiers : `blockchain.js` et `test.js` :

```
touch blockchain.js test.js
```

Nous utiliserons le fichier `blockchain.js` pour écrire le code qui émule le fonctionnement de la blockchain et utiliserons `test.js` pour tester le code et voir le résultat.

Dans le fichier `blockchain.js`, entrez le code suivant :

```javascript
class Blockchain {
    constructor () {
        this.chain = [this.createGenesisBlock()];
        this.pendingTransactions = [];   
    }
}
```

Le code ci-dessus déclare une classe nommée `Blockchain`. La fonction `constructor` est utilisée pour initialiser le tableau `chain` et le tableau `pendingTransactions`. 

Le tableau `chain` contiendra chaque bloc ou groupe de transactions ajouté au réseau. Le tableau `pendingTransactions` contiendra toutes les transactions qui n'ont pas encore été ajoutées à un bloc.

Rappelez-vous qu'une blockchain commence par un bloc genesis. C'est pourquoi le tableau `chain` est initialisé avec un tableau contenant une fonction qui crée le bloc genesis. Vous pouvez également coder en dur le bloc genesis dans le tableau chain.

Nous devons maintenant construire la fonction `createGenesisBlock`. Utilisez le code ci-dessous :

```javascript
  createGenesisBlock() {
    return {
      index: 1,
      timestamp: Date.now(),
      transactions: [],
      nonce: 0,
      hash: "hash",
      previousBlockHash: "previousBlockHash",
    };
  }
```

La fonction ne s'exécutera qu'une seule fois car la fonction `constructor` ne s'exécute qu'une seule fois – au début du programme. 

C'est également la seule fois où un hash non calculé ou un previousBlockHash aléatoire est utilisé car c'est le premier bloc de la chaîne et il ne contient aucune transaction.

La prochaine chose à faire est de créer une fonction pour obtenir le dernier bloc. Utilisez le code ci-dessous :

```javascript
  getLastBlock() {
    return this.chain[this.chain.length - 1];
  };
```

Ce code nous permettra d'accéder aux détails du bloc le plus récent ajouté. Rappelez-vous que nous devons garder une trace du hash du bloc précédent.

Ajoutons maintenant le code pour calculer le hash d'un bloc.

```javascript
  
generateHash(previousBlockHash, timestamp, pendingTransactions) {
    let hash = "";
    let nonce = 0;

    while (hash.substring(0, 3) !== "000") {
      nonce++;
      hash = SHA256(
        previousBlockHash +
          timestamp +
          JSON.stringify(pendingTransactions) +
          nonce
      ).toString();
    }

    return { hash, nonce };
  }
```

Pour vous assurer que cela fonctionne, installez la bibliothèque `SHA256` en utilisant la commande suivante :

```
npm i sha256
```

Importez-la en haut de votre fichier `blockchain.js` comme ceci :

```javascript
const SHA256 = require("sha256");
```

Nous allons maintenant ajouter une fonction qui crée nos transactions et les ajoute à la liste des transactions en attente. Entrez le code suivant :

```javascript
  createNewTransaction(amount, sender, recipient) {
    const newTransaction = {
      amount,
      sender,
      recipient,
    };

    this.pendingTransactions.push(newTransaction);
  }
```

Le moment est maintenant venu de construire la dernière fonction – `createNewBlock`. Elle nous permettra d'ajouter les transactions en attente à un bloc, de calculer le hash et d'ajouter le bloc à la `chain`. Tapez le code ci-dessous :

```javascript
  createNewBlock() {
    const timestamp = Date.now();
    const transactions = this.pendingTransactions;
    const previousBlockHash = this.getLastBlock().hash;
    const generateHash = this.generateHash(
      previousBlockHash,
      timestamp,
      transactions
    );

    const newBlock = {
      index: this.chain.length + 1,
      timestamp,
      transactions,
      nonce: generateHash.nonce,
      hash: generateHash.hash,
      previousBlockHash,
    };

    this.pendingTransactions = [];
    this.chain.push(newBlock);

    return newBlock;
  }
```

Le code ci-dessus utilise la fonction `getLastBlock` pour accéder au hash du bloc précédent. Il calcule le hash du bloc actuel, ajoute tous les détails du nouveau bloc dans un objet, efface le tableau `pendingTransactions` et pousse le nouveau bloc dans la `chain`.

Exportons la classe `Blockchain` pour pouvoir y accéder en dehors du fichier :

```javascript
module.exports = Blockchain;

```

#### Comment tester le code

Nous voulons tester le code que nous avons écrit jusqu'à présent et voir s'il fonctionne comme prévu. Nous allons naviguer vers le fichier `test.js` et commencer par importer la classe `Blockchain` que nous avons exportée il y a un instant comme ceci :

```javascript
const Blockchain = require("./blockchain");
```

Maintenant que nous avons la classe ici, nous pouvons créer une instance de celle-ci et la nommer `bitcoin` :

```javascript
let bitcoin = new Blockchain();

```

Vous pouvez l'appeler comme vous le souhaitez, mais j'utiliserai `bitcoin` car c'est populaire.

Voyons maintenant ce que nous avons dans `bitcoin` par défaut. Pour ce faire, nous allons le logger dans la console comme ceci :

```javascript
console.log(bitcoin);

```

Nous allons maintenant ouvrir le projet dans un terminal et exécuter la commande suivante :

```
node test
```

Il devrait afficher ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-12.21.35.png)
_Sortie par défaut_

Dans la sortie ci-dessus, nous avons le tableau `chain` contenant le bloc genesis et le tableau `pendingTransactions` ne contenant rien. 

Vous vous souviendrez que la fonction `constructor` contient toutes ces données et qu'elle s'exécute une fois au début du programme.

Pour ajouter une nouvelle transaction, utilisez le code ci-dessous :

```javascript
bitcoin.createNewTransaction(
  "100",
  "0xBcd4042DE499D14e55001CcbB24a551F3b954096",
  "0xa0Ee7A142d267C1f36714E4a8F75612F20a79720"
);
```

Le premier paramètre est le `amount`, le deuxième est le `sender`, et le troisième est le `recipient` comme nous l'avons spécifié lors de la création de la fonction.

Si vous exécutez `node test` à nouveau, vous devriez avoir un élément dans le tableau `pendingTransactions` comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-12.31.46.png)
_Une transaction en attente ajoutée_

Pour créer ou miner un bloc, entrez le code suivant :

```javascript
bitcoin.createNewBlock();

```

Vous devriez obtenir la sortie ci-dessous cette fois :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-12.38.30.png)

Vous remarquerez qu'il y a maintenant deux (2) blocs dans la chaîne et plus de transactions dans le tableau `pendingTransactions`.

Certaines choses à noter dans le deuxième bloc sont le `nonce` et le `hash`. Le `nonce` est `1404`. Cela signifie qu'il a fallu 1404 itérations pour obtenir le `hash` correct pour ce bloc.

Pour voir les transactions dans le deuxième bloc, nous utilisons le code suivant :

```javascript
console.log("\n");
console.log("Second Block Transactions", bitcoin.chain[1].transactions);
```

Maintenant, nous avons le résultat ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-12.49.08.png)

Cela a l'air bien ! Cela montre que toutes nos fonctions fonctionnent comme prévu. Et c'est ce qui se passe en coulisses de nombreuses applications blockchain.

Vous venez d'apprendre comment fonctionne la blockchain. Mais vous ne devriez pas construire une application blockchain uniquement sur cette idée de programme. Il y a beaucoup plus à apprendre pour vous permettre de construire des DApp réelles. Cependant, ce que nous avons fait jusqu'à présent vous aidera à plonger plus profondément dans l'apprentissage du web3.

L'une des choses que vous devez apprendre est un langage de programmation blockchain tel que Solidity et d'autres bibliothèques frontend blockchain telles que Web3js et Etherjs.

Je vais maintenant vous introduire aux contrats intelligents en utilisant Solidity.

## Comment écrire un contrat intelligent

Dans cette section, nous allons couvrir tout ce que vous devez savoir sur les contrats intelligents et le langage de programmation Solidity.

%[https://youtu.be/5P-ntj1MVDY]

### Qu'est-ce qu'un contrat intelligent ?

Un contrat intelligent est un programme stocké sur la blockchain. Il contient certaines conditions qui doivent être remplies avant son exécution. 

Les contrats intelligents s'inspirent des contrats traditionnels. Mais ils sont différents car ils sont exécutés automatiquement par un ordinateur lorsque les termes prédéfinis sont remplis. 

### Qu'est-ce que Solidity ?

Solidity est le principal langage de programmation utilisé pour construire la plupart des contrats intelligents car il est spécifiquement conçu à cet effet. Il suit le modèle OOP que nous avons démontré en utilisant JavaScript et emprunte la nature typée de TypeScript. Ainsi, bien que certaines syntaxes puissent différer de ce que vous connaissez déjà, ce n'est pas trop tiré par les cheveux à saisir.

Nous allons apprendre les bases de Solidity en l'utilisant pour construire un contrat intelligent qui permet aux utilisateurs d'envoyer des fonds les uns aux autres. 

Ne vous inquiétez pas, vous n'aurez pas à configurer un autre projet. Nous allons utiliser le [remix playground](https://remix.ethereum.org/) pour tout faire – écrire le code, compiler, déboguer et tester.

Rendons-nous maintenant sur [https://remix.ethereum.org/](https://remix.ethereum.org/). Vous devriez avoir l'écran suivant qui vous fixe pendant un moment :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-21.54.11-1.png)
_Page d'accueil de Remix_

Remix prépare tout pour vous. Soyez patient 😊

Lorsque c'est terminé, vous devriez avoir l'écran suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-21.59.30.png)

Ce terrain de jeu nous fournit tout ce dont nous avons besoin pour écrire notre premier contrat intelligent.

Commençons par supprimer le fichier créé pour nous par défaut. Pour ce faire, cliquez sur la première icône sous le logo remix.

Faites un clic droit sur le nom du fichier dans la section de l'explorateur et sélectionnez `delete` :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-22.08.37.png)

Cliquez sur `OK` dans le menu pop-up.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-22.10.36.png)

Nous allons maintenant créer un nouveau fichier nommé `Blockchain.sol` en cliquant sur l'icône de document marquée en rouge dans l'image ci-dessous et en tapant le nom du fichier dans l'espace prévu :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-10-at-22.15.47.png)

`.sol` est l'extension utilisée pour les fichiers solidity. L'espace vide est où nous taperons notre code.

Le code Solidity commence toujours par la ligne ci-dessous :

```javascript
// SPDX-License-Identifier: UNLICENSED
```

Sans ce code, vous obtiendrez une erreur. C'est comme dire que vous acceptez les termes et conditions d'écriture de Solidity.

La prochaine chose à faire est de préciser la version de Solidity que vous souhaitez utiliser. J'utiliserai le code suivant :

```javascript
pragma solidity ^0.8.7;

```

Le signe circonflexe (^) indique que le programme sera compatible avec les versions supérieures de solidity. Nous pouvons maintenant démarrer le programme.

La première chose à faire est de définir une `Classe` nommée `Blockchain`. Cependant, le mot-clé pour `Classe` en solidity est `contract`. Nous avons donc :

```javascript
contract Blockchain {

}
```

À l'intérieur du contrat ci-dessus, nous allons créer un type de données appelé `BlockStruck` avec le code ci-dessous :

```javascript
struct BlockStruck {
    uint256 index;
    uint256 timestamp;
    uint256 amount;
    address sender;
    address recipient;
}
```

Solidity nous permet de créer n'importe quel type de données que nous jugeons approprié en utilisant le mot-clé `struct`, qui est l'abréviation de **structure.** 

Nous définissons toutes les clés pour lesquelles nous attendons une valeur dans le struct. Puisque solidity est un langage fortement typé, nous avons spécifié un type de données avant chaque clé. Le `struct` est similaire à `Object` en JavaScript.

`uint` indique qu'une variable est un entier. L'ajout d'un nombre après celui-ci (tel que `uint256` ou `uint18`) spécifie la taille maximale qu'il doit prendre, mais `uint` suppose `uint256` par défaut. 

`address`, en revanche, indique qu'une variable est une adresse de portefeuille. Il existe également le type de données `string`.

La prochaine chose que nous voulons définir est un `event`. Un `event` est généralement déclenché à la fin de l'exécution d'une fonction pour envoyer des données au frontend. Vous pouvez le voir comme `console.log`. Certaines personnes l'utilisent également comme un moyen peu coûteux de stockage.

Nous voulons définir un `BlockEvent` que nous déclencherons après avoir ajouté un bloc à la chaîne. Entrez le code suivant sous le `BlockStruct` :

```javascript

event BlockEvent(uint256 amount, address sender, address recipient);
```

Contrairement à `struct`, des accolades circulaires sont utilisées pour un `event`, et leurs clés sont séparées par des virgules (,). De plus, remarquez que `struct` ne se termine pas par un point-virgule, mais `event` oui.

Maintenant que nous avons défini la structure des blocs, utilisons-la pour configurer un tableau de blocs appelé `chain` comme ceci :

```javascvript
BlockStruck[] chain;

```

Le code ci-dessus définit la `chain` comme un tableau de `BlockStruct`. Comme toujours, nous spécifions le type de données avant le nom de la variable.

Ensuite, définissez une variable pour garder une trace du nombre de blocs dans la `chain` :

```javascript
uint256 chainCount;
```

Vous pouvez choisir de lui attribuer une valeur sur la même ligne (`uint256 chainCount = 0 ;`) ou le faire dans la fonction `constructor` comme ceci :

```javascript
constructor() {
    chainCount = 0;
}
```

Nous allons maintenant définir trois (3) fonctions : `addBlockToChain` (pour ajouter des blocs à la chaîne), `getChain` (pour retourner tous les blocs ajoutés à la chaîne), et `getChainCount` (pour obtenir le nombre de blocs ajoutés à la chaîne).

#### Fonction addBlockToChain

Le code ci-dessous commence la fonction :

```javascript

function addBlockToChain(uint256 amount, address payable recipient) public {

}
```

Comme les fonctions que vous connaissez déjà, elle commence par le mot-clé `function` suivi du nom de la `function`, et de l'argument qu'elle attend entre accolades. 

L'un des arguments (`recipient`) a un drapeau appelé `payable`, indiquant que l'adresse du portefeuille est éligible pour recevoir des fonds. À côté se trouve le drapeau de visibilité de la fonction (`public`). 

La visibilité définit qui peut appeler une fonction ou une variable. Elle peut être `public`, `private`, `internal`, ou `external`. 

1. Une fonction `public` peut être appelée par n'importe quel contrat.
2. Les fonctions `private` ne peuvent être appelées qu'à l'intérieur du contrat où elles sont définies.
3. Seuls les contrats qui héritent des fonctions `internal` peuvent les appeler.
4. Les fonctions `external` ne sont accessibles que par d'autres contrats.

Dans `addBlockToChain`, nous commençons par incrémenter `chainCount` de un comme ceci :

```javascript
chainCount += 1;
```

Ensuite, ajoutez le bloc d'une transaction à la chaîne comme ceci :

```javascript
        chain.push(
            BlockStruck(
                chainCount,
                block.timestamp,
                amount,
                msg.sender,
                recipient
            )
        );
```

Le `BlockStruct` prend des valeurs correspondant aux clés définies lors de la définition du `struct`. Il est ensuite ajouté au tableau `chain` en utilisant la méthode `.push`. Nous avons maintenant un nouveau bloc dans la `chain`.

Enfin, nous déclenchons le `BlockEvent` que nous avons créé il y a un moment :

```javascript
emit BlockEvent(amount, msg.sender, recipient);
```

`emit` est le mot-clé utilisé pour appeler un événement. Comme avec le `BlockStruct`, le `BlockEvent` prend les valeurs telles qu'elles correspondent aux clés définies lors de sa définition.

La fonction `addBlockToChain` ressemble maintenant à ceci :

```javascript
    
    function addBlockToChain(uint256 amount, address payable recipient) public {
        chainCount += 1;

        chain.push(
            BlockStruck(
                chainCount,
                block.timestamp,
                amount,
                msg.sender,
                recipient
            )
        );

        emit BlockEvent(amount, msg.sender, recipient);
    }
```

#### Fonction getChain

Cette fonction ne prend aucun argument mais retourne un `BlockStruct`. Nous utiliserons le code suivant :

```javascript
    
    function getChain() public view returns (BlockStruck[] memory) {
        return chain;
    }
```

Le programme retourne la `chain`, un tableau de tous les blocs.

Une chose à noter dans la fonction ci-dessus est que nous avons utilisé `view` pour montrer que cette fonction retourne une valeur. Nous avons également indiqué le type de données que nous attendons en retour (`returns (BlockStruck[] memory)`) et le type de stockage à utiliser (`memory`).

Il existe deux principaux types de stockage dans solidity : `Storage` et `Memory`. `Storage` est le type de stockage par défaut utilisé pour conserver les données de manière permanente pour un programme tandis que `Memory` est temporaire et moins coûteux en termes de gaz.

Le gaz est une commission payée pour exécuter des contrats intelligents. Ne vous inquiétez pas de cela. Nous avons un gaz factice qui nous permettra de tester notre programme.

#### Fonction getChainCount

Comme `getChain`, cette fonction ne prend également aucun argument. Elle retourne le nombre de blocs ajoutés à la `chain` jusqu'à présent. Voir le code ci-dessous :

```javascript
    
    function getChainCount() public view returns (uint256) {
        return chainCount;
    }
```

Cela complète le contrat intelligent que nous avions l'intention de créer. Maintenant, le code ressemble à ceci :

```javascript
// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.7;

contract Blockchain {
    struct BlockStruck {
        uint256 index;
        uint256 timestamp;
        uint256 amount;
        address sender;
        address recipient;
    }

    event BlockEvent(uint256 amount, address sender, address recipient);

    BlockStruck[] chain;
    uint256 chainCount;

    constructor() {
        chainCount = 0;
    }

    function addBlockToChain(uint256 amount, address payable recipient) public {
        chainCount += 1;

        chain.push(
            BlockStruck(
                chainCount,
                block.timestamp,
                amount,
                msg.sender,
                recipient
            )
        );

        emit BlockEvent(amount, msg.sender, recipient);
    }

    function getChain() public view returns (BlockStruck[] memory) {
        return chain;
    }

    function getChainCount() public view returns (uint256) {
        return chainCount;
    }
}

```

### Comment compiler le contrat intelligent

Nous devons compiler le code pour vérifier s'il y a des erreurs que nous devons corriger. Les étapes ci-dessous nous aideront à faire cela.

Cliquez sur la troisième icône du menu de gauche de l'IDE remix :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-11.07.34.png)

Assurez-vous que la version de solidity sélectionnée correspond à celle que vous avez spécifiée au début du contrat intelligent. Ensuite, cliquez sur le bouton `Compile` :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-11.18.36.png)

La compilation a réussi puisque nous n'avons pas d'erreurs. Magnifique 🥰.

### Comment déployer le contrat intelligent

Maintenant que la compilation est réussie, déployons le contrat.

Cliquez sur la quatrième icône du menu latéral :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-11.27.27-1.png)

Sélectionnez `Remix VM (London)` pour l'`ENVIRONMENT`. Il dispose de dix (10) comptes avec 100 ethers factices chacun que vous pouvez utiliser à des fins de test. Ensuite, cliquez sur le bouton `Deploy` :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-11.33.30.png)

Maintenant, lorsque vous faites défiler vers le bas, vous trouverez le contrat `Blockchain` sous **Deployed Contracts.** Cliquez sur la flèche à côté du nom du contrat déployé pour voir les fonctions du contrat avec lesquelles vous pouvez interagir.

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-11.46.28.png)

Il y a trois (3) fonctions dans l'image ci-dessus qui correspondent aux trois (3) fonctions que nous avons définies dans notre contrat intelligent. Remix crée automatiquement une interface utilisateur pour vous tester vos contrats dès que vous les déployez.

### Comment tester le contrat intelligent 

Nous allons maintenant tester les fonctions que nous avons créées pour voir comment elles répondent.

#### Comment tester la fonction addBlockToChain

Pour tester la fonction `addBlockToChain`, cliquez sur l'icône caret (^) à côté du bouton de la fonction et de la zone de saisie. Cela fait apparaître un formulaire. Remplissez `10` pour le `amount`, et remplissez l'une des dix adresses de compte pour le `recipient` :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-11.56.31.png)

Cliquez sur le bouton `transact`.

Notez que vous ne pouvez pas envoyer de fonds à la même adresse que vous avez utilisée pour déployer le contrat. Vous devez choisir un compte différent.

#### Comment tester la fonction getChain

Cliquez sur le bouton `getChain` pour révéler les blocs dans la chaîne jusqu'à présent :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-12.02.10.png)

Il retourne un `tuple`, qui est une sorte de `array`. Rappelez-vous que `chain` est censé être un `array` contenant une liste de blocs.

#### Comment tester la fonction getChainCount

Pour obtenir le nombre de blocs ajoutés, cliquez sur le bouton `getChainCount` :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot-2022-11-11-at-12.08.25.png)

Et comme nous l'avons défini, il retourne un `uint`. Il n'y a qu'un seul élément dans la `chain` pour l'instant, mais à mesure que vous continuez à ajouter plus de blocs, le nombre augmentera.

Walah ! Sommes-nous arrivés aussi loin ? 😳 Comment c'est génial 😍.

Félicitations pour être resté jusqu'à la fin de ce tutoriel !

Vous êtes maintenant prêt à explorer tout ce que vous pouvez faire avec la blockchain.

## Conclusion

La blockchain redéfinit l'internet et est là pour rester. La difficulté que j'ai rencontrée en essayant d'apprendre les ficelles de cette nouvelle technologie m'a poussé à documenter ce guide convivial pour débutants. J'espère qu'il aidera tous ceux qui luttent encore.

Dans ce tutoriel, vous avez appris ce qu'est la blockchain, comment elle fonctionne et ce qui se passe en coulisses. Nous avons démontré comment elle fonctionne en utilisant le modèle OOP de JavaScript et conclu avec une brève introduction sur la façon de construire des contrats intelligents en utilisant le langage de programmation Solidity et l'IDE remix.

Je recommande que vous continuiez à apprendre et à vous améliorer dans la construction d'applications blockchain en créant les projets suivants dans l'ordre où ils sont listés (par difficulté croissante) :

```javascript
Hello World
Simple Storage
Voting Smart Contract
Ether Wallets
Multi Send
Time Lock Smart Contract
ERC20 Token
Token Wallet
Air Drop
ICO
```

Ces projets vous défieront de faire des recherches et d'aiguiser votre compétence en blockchain.

Bonne chaîne !