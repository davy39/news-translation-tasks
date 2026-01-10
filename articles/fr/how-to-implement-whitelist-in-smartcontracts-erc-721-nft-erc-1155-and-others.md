---
title: Comment implémenter une liste blanche dans les contrats intelligents (ERC-721
  NFT, ERC-1155 et autres)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-10-12T14:12:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-whitelist-in-smartcontracts-erc-721-nft-erc-1155-and-others
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/whitelist-1.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: digital-signature
  slug: digital-signature
- name: merkle tree
  slug: merkle-tree
- name: Smart Contracts
  slug: smart-contracts
- name: whitelist
  slug: whitelist
seo_title: Comment implémenter une liste blanche dans les contrats intelligents (ERC-721
  NFT, ERC-1155 et autres)
seo_desc: 'By Igor Gaponov

  In this article I will show you three ways you can create a whitelist in a smart
  contract.

  Here''s what we''ll discuss:


  On-chain whitelists

  Digital signatures

  Merkle trees


  All methods are available in the repo here.

  A whitelist is use...'
---

Par Igor Gaponov

Dans cet article, je vais vous montrer trois façons de créer une liste blanche dans un contrat intelligent.

Voici ce que nous allons discuter :

* Listes blanches sur la chaîne
* Signatures numériques
* Arbres de Merkle

Toutes les méthodes sont disponibles dans le [dépôt ici](https://github.com/gapon2401/smartcontract-whitelist).

Une liste blanche est utile si vous souhaitez restreindre l'accès à une certaine fonction ou accorder des privilèges à un certain groupe d'utilisateurs. 

Pour comparer ces méthodes, je vais utiliser des contrats intelligents très minimalistes pour réduire les dépenses inutiles de gaz. 

Plongeons-nous dans le sujet.

## Comment créer une liste blanche sur la chaîne

L'idée principale est de stocker toutes les adresses de la liste blanche dans le contrat intelligent.

Jetez un coup d'œil à ce schéma :

![Liste blanche sur la chaîne](https://www.freecodecamp.org/news/content/images/2022/10/Untitled--3-.png)
_Liste blanche sur la chaîne_

Lorsque l'utilisateur appelle la fonction du contrat intelligent, il vérifie si l'adresse est dans la liste blanche. Si c'est le cas, la fonction s'exécute. 

Si vous souhaitez ajouter ou supprimer des adresses de la liste blanche, vous pouvez le faire dans le contrat intelligent avec des fonctions `external` supplémentaires.

Avantages :

* facile à implémenter
* toutes les adresses sont stockées dans le contrat intelligent et seul le propriétaire peut les modifier

Inconvénients : 

* c'est la méthode la plus coûteuse
* vous devez dépenser du gaz pour ajouter et supprimer les adresses

Voici à quoi ressemble le contrat intelligent :

```js
contract OnChainWhitelistContract is Ownable {

    mapping(address => bool) public whitelist;

    /**
     * @notice Ajouter à la liste blanche
     */
    function addToWhitelist(address[] calldata toAddAddresses) 
    external onlyOwner
    {
        for (uint i = 0; i < toAddAddresses.length; i++) {
            whitelist[toAddAddresses[i]] = true;
        }
    }

    /**
     * @notice Retirer de la liste blanche
     */
    function removeFromWhitelist(address[] calldata toRemoveAddresses)
    external onlyOwner
    {
        for (uint i = 0; i < toRemoveAddresses.length; i++) {
            delete whitelist[toRemoveAddresses[i]];
        }
    }

    /**
     * @notice Fonction avec liste blanche
     */
    function whitelistFunc() external
    {
        require(whitelist[msg.sender], "NOT_IN_WHITELIST");

        // Faire des choses utiles
    }
}
```

Toutes les adresses seront stockées dans la variable `whitelist`.

La fonction `addToWhitelist` permet au propriétaire d'ajouter un tableau d'adresses. Gardez à l'esprit que chaque adresse de la liste coûtera environ 22904 unités de gaz. Pour appeler cette fonction, cela coûte 23994 unités de gaz.

La fonction `removeFromWhitelist` vous permet de supprimer des adresses de la liste blanche.

Et la fonction `whitelistFunc` vérifie si l'adresse appartient à la liste blanche.

Dépenses de gaz :

![Dépenses de gaz pour la liste blanche sur la chaîne](https://www.freecodecamp.org/news/content/images/2022/10/on-chain-gas.jpg)
_Dépenses de gaz pour la liste blanche sur la chaîne_

## Comment créer une liste blanche avec signature numérique

L'idée principale est de créer des signatures pour les adresses et de les vérifier à l'intérieur du contrat intelligent.

![Liste blanche avec signature numérique](https://www.freecodecamp.org/news/content/images/2022/10/Digital-signature-1.png)
_Liste blanche avec signature numérique_

Vous stockez la liste blanche sur votre serveur. Avant de faire un appel au contrat intelligent, vous devez vérifier si l'adresse est dans la liste blanche ou non. Si oui, créez une signature pour l'adresse et passez cette signature au contrat intelligent. À l'intérieur du contrat intelligent, vous devez valider cette signature.

Avantages :

* Pas de gaz pour ajouter ou supprimer des adresses de la liste blanche.
* Pas besoin d'interagir avec le contrat intelligent concernant la liste blanche

Inconvénients :

* La liste blanche est située dans une base de données qui peut être compromise. Si le public fait confiance au propriétaire du projet, alors ce n'est pas un problème
* Le prix le plus élevé pour le déploiement du contrat et la validation de la liste blanche

Voici le contrat intelligent :

```js
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract DigitalSignatureWhitelistContract is Ownable {

    using ECDSA for bytes32;

    /**
     * @notice Utilisé pour valider les adresses de la liste blanche
               Remplacez cette adresse de portefeuille par la vôtre !
     */
    address private signerAddress = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;

    /**
     * @notice Vérifier la signature
     */
    function verifyAddressSigner(bytes memory signature) private 
    view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender));
        return signerAddress == messageHash.toEthSignedMessageHash().recover(signature);
    }
    
     /**
     * @notice Fonction avec liste blanche
     */
    function whitelistFunc(bytes memory signature) external
    {
        require(verifyAddressSigner(signature), "SIGNATURE_VALIDATION_FAILED");

        // Faire des choses utiles
    }
}

```

### Comment implémenter une signature numérique

Tout d'abord, vous devrez créer une nouvelle adresse de portefeuille. Ce sera l'adresse du signataire.

ATTENTION : Ne envoyez aucun fonds à ce portefeuille. Il sera utilisé uniquement pour faire des signatures.

Supposons que l'adresse du portefeuille du signataire soit `0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266`

Spécifiez-la dans le contrat intelligent ici :

```js
address private signerAddress = 0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266;
```

À la racine de votre projet web, créez un fichier `.env` avec la clé privée de ce portefeuille :

```
SIGNER_PRIVATE_KEY=0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80
```

Spécifiez uniquement vos propres clés publiques et privées, car celles-ci sont publiques.

Ensuite, créez la base de données de la liste blanche. Elle peut être PostgreSQL, MySQL, MongoDB – n'importe laquelle que vous voulez. Vous pouvez facilement ajouter ou supprimer des adresses.

Ensuite, lorsque c'est le moment d'interagir avec le contrat intelligent, l'utilisateur clique sur un bouton de votre site web. Vous envoyez la demande à votre serveur avec l'adresse de l'utilisateur.

Si l'utilisateur est dans la liste blanche, créez la signature pour l'adresse sur votre serveur :

```js
import { ethers } from 'ethers'

export default async function handler() {
    
  // Tableau de la liste blanche de votre base de données
  const whitelist = [
    '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC',
    '0x90F79bf6EB2c4f870365E785982E1f101E93b906',
    '0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65',
    '0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc',
    '0x976EA74026E726554dB657fA54763abd0C3a0aa9',
  ]

  // Cette variable contiendra la signature dont nous avons besoin
  let signature = ''
  
  // Analyser les paramètres passés au serveur et obtenir l'adresse du portefeuille de l'utilisateur
  const userWalletAddress = ''

  if (whitelist.includes(userWalletAddress)) {
    const signer = new ethers.Wallet(process.env.SIGNER_PRIVATE_KEY!)
    const addressHash = ethers.utils.solidityKeccak256(['address'], [userWalletAddress.toLowerCase()])
    const messageBytes = ethers.utils.arrayify(addressHash)
    signature = await signer.signMessage(messageBytes)
  }

  // Retourner la signature au web
}
```

Ensuite, passez la signature à la fonction du contrat intelligent, où `verifyAddressSigner` la validera selon l'adresse de l'expéditeur. 

Dépenses de gaz :

![Dépenses de gaz pour la liste blanche avec signature numérique](https://www.freecodecamp.org/news/content/images/2022/10/digital-signature-gas.jpg)
_Dépenses de gaz pour la liste blanche avec signature numérique_

## Comment créer une liste blanche avec arbre de Merkle

Qu'est-ce que l'arbre de Merkle ?

> L'arbre de Merkle est un arbre dans lequel chaque "feuille" (nœud) est étiquetée avec le hachage cryptographique d'un bloc de données, et chaque nœud qui n'est pas une feuille (appelé branche, nœud interne ou inode) est étiqueté avec le hachage cryptographique des étiquettes de ses nœuds enfants. – [Source](https://en.wikipedia.org/wiki/Merkle_tree)

Comment cela se connecte-t-il au problème de la liste blanche ?

Nous allons l'utiliser pour hacher toutes les adresses en un seul hachage racine.

![Arbre de Merkle](https://www.freecodecamp.org/news/content/images/2022/10/Merkle-tree-structure.png)
_Arbre de Merkle_

Voici le schéma de travail :

![Liste blanche avec arbre de Merkle](https://www.freecodecamp.org/news/content/images/2022/10/Merkle-tree-1.png)
_Liste blanche avec arbre de Merkle_

Comme dans la méthode de signature numérique, vous avez besoin d'une base de données pour les adresses de la liste blanche. Lorsque vous êtes prêt à commencer la vente ou autre chose, vous devez créer le hachage racine de Merkle et l'enregistrer dans le contrat intelligent. Ce hachage validera toutes les adresses.

Lorsque l'utilisateur souhaite faire une demande au contrat intelligent, vous devez créer une preuve de Merkle pour lui, basée sur l'arbre de Merkle de toutes les adresses. Ensuite, vous devez envoyer la preuve au contrat intelligent. Vous pouvez stocker l'arbre localement. 

Après avoir modifié la liste blanche, vous devez mettre à jour le hachage racine de Merkle et le réécrire dans le contrat intelligent. Vous devez également mettre à jour l'arbre de Merkle local. 

Avantages :

* Le déploiement du contrat intelligent est beaucoup moins cher que la méthode de signature numérique
* La validation des adresses dans le contrat intelligent est également moins chère
* Pas de gaz pour ajouter ou supprimer des adresses de la liste blanche, jusqu'à ce que vous commenciez une vente

Inconvénients :

* Après le début de la vente, il sera compliqué de changer la liste blanche. Vous devrez mettre à jour le contrat intelligent et l'arbre de Merkle chaque fois. Par conséquent, du gaz sera dépensé.
* Vous devez savoir comment créer une racine de Merkle et mettre à jour le contrat intelligent. Il est impossible de changer la liste blanche sans interagir avec le contrat intelligent.

Voici le contrat intelligent :

```js
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.14;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract MerkleTreeWhitelistContract is Ownable {

    /**
     * @notice Hachage racine de Merkle pour les adresses de la liste blanche
     */
    bytes32 public merkleRoot = 0x09485889b804a49c9e383c7966a2c480ab28a13a8345c4ebe0886a7478c0b73d;

    /**
     * @notice Changer le hachage racine de Merkle
     */
    function setMerkleRoot(bytes32 merkleRootHash) external onlyOwner
    {
        merkleRoot = merkleRootHash;
    }

    /**
     * @notice Vérifier la preuve de Merkle de l'adresse
     */
    function verifyAddress(bytes32[] calldata _merkleProof) private 
    view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        return MerkleProof.verify(_merkleProof, merkleRoot, leaf);
    }

    /**
     * @notice Fonction avec liste blanche
     */
    function whitelistFunc(bytes32[] calldata _merkleProof) external
    {
        require(verifyAddress(_merkleProof), "INVALID_PROOF");

        // Faire des choses utiles
    }
}

```

### Comment implémenter un arbre de Merkle sur le web

Tout d'abord, créez la base de données de la liste blanche. Elle peut être PostgreSQL, MySQL, MongoDB ou toute autre que vous voulez. Vous pouvez facilement ajouter ou supprimer des adresses.

Lorsque c'est le moment d'interagir avec le contrat intelligent, créez un hachage racine de Merkle :

```js
import { ethers } from 'ethers'
import { MerkleTree } from 'merkletreejs'

// Votre liste blanche de la base de données
const whitelist = [
  '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC',
  '0x90F79bf6EB2c4f870365E785982E1f101E93b906',
  '0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65',
  '0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc',
  '0x976EA74026E726554dB657fA54763abd0C3a0aa9',
]

const { keccak256 } = ethers.utils
let leaves = whitelist.map((addr) => keccak256(addr))
const merkleTree = new MerkleTree(leaves, keccak256, { sortPairs: true })

// Enregistrez cette valeur dans le contrat intelligent
const merkleRootHash = merkleTree.getHexRoot()
// 0x09485889b804a49c9e383c7966a2c480ab28a13a8345c4ebe0886a7478c0b73d
```

 Ensuite, enregistrez le hachage racine de Merkle dans le contrat intelligent. 

Spécifiez-le avant le déploiement :

```js
bytes32 public merkleRoot = 0x09485889b804a49c9e383c7966a2c480ab28a13a8345c4ebe0886a7478c0b73d;
```

Ou utilisez une fonction `setMerkleRoot` pour cela :

```js
function setMerkleRoot(bytes32 merkleRootHash) external onlyOwner
{
    merkleRoot = merkleRootHash;
}
```

Lorsque l'utilisateur clique sur un bouton de votre site web, vous envoyez la demande à votre serveur avec l'adresse de l'utilisateur. Si l'utilisateur est dans la liste blanche, créez la preuve de Merkle sur votre serveur :

```js
import { ethers } from 'ethers'
import { MerkleTree } from 'merkletreejs'

export default async function handler() {
    
  // Tableau de la liste blanche de votre base de données
  const whitelist = [
    '0x3C44CdDdB6a900fa2b585dd299e03d12FA4293BC',
    '0x90F79bf6EB2c4f870365E785982E1f101E93b906',
    '0x15d34AAf54267DB7D7c367839AAf71A00a2C6A65',
    '0x9965507D1a55bcC2695C58ba16FB37d819B0A4dc',
    '0x976EA74026E726554dB657fA54763abd0C3a0aa9',
  ]

  // Cette variable contiendra la preuve dont nous avons besoin
  let proof = []

  // Analyser les paramètres passés au serveur et obtenir l'adresse du portefeuille de l'utilisateur
  const userWalletAddress = ''

  if (whitelist.includes(userWalletAddress)) {
    const { keccak256 } = ethers.utils
    let leaves = whitelist.map((addr) => keccak256(addr))
    const merkleTree = new MerkleTree(leaves, keccak256, { sortPairs: true })
    let hashedAddress = keccak256(userWalletAddress)
    proof = merkleTree.getHexProof(hashedAddress)
  }

  // Retourner la preuve au web
}

```

Ensuite, passez la preuve à la fonction du contrat intelligent, où `verifyAddress` la validera selon l'adresse de l'expéditeur. 

Dépenses de gaz :

![Dépenses de gaz pour la liste blanche avec arbre de Merkle](https://www.freecodecamp.org/news/content/images/2022/10/merkle-tree-gas.jpg)
_Dépenses de gaz pour la liste blanche avec arbre de Merkle_

## Résumé

Ci-dessous, vous trouverez un tableau comparatif des unités de gaz que ces différentes méthodes dépensent :


| Propriété                      | Sur la chaîne | Signature numérique | Arbre de Merkle |
|-------------------------------|----------|-------------------|-------------|
| Déploiement                    | 329 724  | 486 182           | 352 790     |
| Ajouter à la liste blanche 1 adresse    | 46 898   | 0                 | 28 986      |
| Ajouter à la liste blanche 10 adresses | 253 010  | 0                 | 28 986      |
| Retirer de la liste blanche         | 24 930   | 0                 | 28 986      |
| Appeler la fonction avec la liste blanche  | 23 443   | 29 365            | 26 065      |

En bref :

* Une liste blanche sur la chaîne est facile à implémenter, mais coûteuse à utiliser. Je ne recommanderais pas de l'utiliser.
* Une liste blanche avec signature numérique est un outil universel qui ne nécessite pas d'interactions supplémentaires avec le contrat intelligent. Vous pouvez facilement modifier la liste blanche à tout moment. Mais vous devez payer pour la polyvalence. Le déploiement et la fonction avec la liste blanche sont les plus coûteux. Si vos adresses changent fréquemment, alors utilisez la signature numérique. 
* L'arbre de Merkle est la meilleure option si vos adresses de liste blanche ne changeront pas après le début de la prévente ou autre chose que vous souhaitez. Par exemple, cela ne coûte rien de collecter des adresses et de les modifier dans votre base de données. Lorsque la vente commence, vous arrêtez de modifier la liste blanche, créez le hachage racine, enregistrez-le dans le contrat intelligent et c'est tout. Dans ce cas, l'arbre de Merkle est meilleur que la signature numérique. 

 Ce qu'il faut utiliser exactement dépend de vous !

Enfin, je veux vous montrer comment calculer le prix du gaz.

### Comment calculer le prix du gaz

Utilisez la formule suivante :

```
(unités de gaz) * (prix du gaz par unité) = frais de gaz en gwei
```

Utilisez [https://ethgasstation.info/](https://ethgasstation.info/) ou tout autre site web pour trouver le prix du gaz par unité. Au moment de la rédaction de cet article, le prix du gaz est de 22.

![Prix du gaz par unité](https://www.freecodecamp.org/news/content/images/2022/10/gas-price.jpg)
_Prix du gaz par unité_

La valeur peut changer en fonction de l'heure de la journée.

Calculons combien cela coûtera pour déployer un contrat intelligent avec signature numérique.

```js
Déploiement = 486 182 * 22 = 10 696 004 gwei = 0,010696004 ETH
```

Maintenant, puisque le prix ETH/USD est de 1 324 $, cela signifie que le déploiement sur le Mainnet coûtera environ 14 $.

Peut-être souhaitez-vous convertir le tableau de comparaison en USD ?  
 `Prix du gaz par unité` = 22, `ETH` = 1 324 $


| Propriété                      | Sur la chaîne | Signature numérique | Arbre de Merkle |
|-------------------------------|----------|-------------------|-------------|
| Déploiement                    | 9,60 $     | 14,16 $            | 10,28 $      |
| Ajouter à la liste blanche 1 adresse    | 1,37 $    | 0                 | 0,84 $       |
| Ajouter à la liste blanche 10 adresses | 7,37 $    | 0                 | 0,84 $       |
| Retirer de la liste blanche         | 0,73 $    | 0                 | 0,84 $       |
| Appeler la fonction avec la liste blanche  | 0,68 $    | 0,86 $             | 0,76 $       |



Merci d'avoir lu ! ❤