---
title: Un protocole pour les contrats intelligents vendables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-23T19:04:34.000Z'
originalURL: https://freecodecamp.org/news/a-protocol-for-sellable-smart-contracts-829bc2ce02b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DTkbYDqroiSzJ3k5c_x5Zg.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: Smart Contracts
  slug: smart-contracts
- name: Solidity
  slug: solidity
seo_title: Un protocole pour les contrats intelligents vendables
seo_desc: 'By Pablo Ruiz

  Ethereum doesn’t have the concept of smart contract ownership built into it.Even
  though the creation and deployment of a smart contract is done by an account — be
  it an External Owned Account (EOA) or another contract — being the creato...'
---

Par Pablo Ruiz

Ethereum n'intègre pas nativement le concept de propriété de contrat intelligent (smart contract).  
Même si la création et le déploiement d'un contrat intelligent sont effectués par un compte — qu'il s'agisse d'un compte externe (EOA) ou d'un autre contrat — le fait d'être le créateur du contrat intelligent ne donne au compte aucun privilège spécial sur le contrat qu'il a déployé.

La plupart des cas d'utilisation des contrats intelligents nécessitent que quelqu'un possède les contrats. Ce « propriétaire » se voit attribuer des privilèges — et des responsabilités — sur le contrat intelligent.

Dans un contrat de crowdsale, il peut être chargé de gérer l'ensemble du processus et de mettre la vente en pause en cas de problème.

Dans une Dapp de loterie ou de tirage au sort, il peut être chargé d'exécuter le tirage des numéros.

Dans tout contrat détenant des fonds, il peut être désigné comme bénéficiaire lors de la destruction du contrat.

![Image](https://cdn-media-1.freecodecamp.org/images/BXe8PzvTK9LjO7-H1962DwtjrlaAXfNmD8kC)
_Photo de [Unsplash](https://unsplash.com/photos/OvitgXQeN0Q?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ricardo Resende</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Un modèle courant utilisé par de nombreux contrats intelligents consiste à définir le propriétaire comme le compte déployant le contrat, comme ceci :

```
pragma solidity 0.4.19;
```

```
contract MyContract {  address owner;
```

```
  function MyContract(){    owner = msg.sender;  }}
```

Ensuite, en ajoutant un modificateur :

```
modifier onlyOwner {  require(msg.sender == owner);  _;    }
```

Et enfin, en utilisant ce modificateur pour garantir que les opérations critiques ne peuvent être effectuées que par le propriétaire du contrat :

```
// Détruire le contrat et transférer les fonds au propriétaire // Uniquement accessible au propriétaire, pour des raisons évidentes.
```

```
function destroyContract() public onlyOwner {  selfdestruct(owner);}
```

### Le problème du changement de propriété d'un contrat

Certaines situations peuvent nécessiter que la propriété d'un contrat soit cédée à quelqu'un d'autre. Pour n'en citer que quelques-unes :

* La personne qui a déployé le contrat l'a fait pour le compte de quelqu'un d'autre. Un développeur ou un consultant effectuant un travail contractuel pour une entreprise.
* Une entreprise souhaite liquider / vendre ses actifs, qui incluent des contrats intelligents. Lesquels peuvent ou non avoir un solde en ether.
* Le propriétaire du contrat intelligent veut le donner, en faire don ou simplement le revendre pour réaliser un profit.

![Image](https://cdn-media-1.freecodecamp.org/images/NFbHtRcIE62fv8DdiE144boi720LyXmFMp7I)
_Photo de [Unsplash](https://unsplash.com/photos/5x8kipLwVug?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel.com</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Certains contrats, mais malheureusement peu, incluent une fonction pour céder la propriété du contrat à un autre compte. Et certains d'entre eux incluent également une autre fonction pour que cette personne accepte la propriété qui lui a été conférée.

```
function changeOwner(address _newOwner)public onlyOwner {  ownerCandidate = _newOwner;}
```

```
function acceptOwnership()public {  require(msg.sender == ownerCandidate);    owner = ownerCandidate;}
```

Or, les situations mentionnées ci-dessus partagent quelques problèmes communs que ces fonctions `changeOwner()` et `acceptOwnership()`, peu utilisées, ne résolvent pas :

* Comment l'acheteur du contrat peut-il être certain qu'une fois qu'il aura payé pour la propriété du contrat, le vendeur exécutera réellement la fonction `changeOwner()` correspondante ?
* Cela peut arriver dans l'autre sens. Comment le vendeur du contrat peut-il être certain d'être payé s'il cède la propriété en premier ?
* Comment l'acheteur du contrat peut-il être certain que le propriétaire actuel du contrat ne le modifiera pas (enfin, ses données) avant d'en céder la propriété ?

### Le protocole de contrat vendable

La solution que je propose consiste à implémenter une série de fonctions qui permettraient au propriétaire d'un contrat intelligent de le vendre en échange d'ether à quelqu'un de son choix, ou simplement de le mettre en vente pour que n'importe qui puisse l'acheter au prix demandé, selon le principe du premier arrivé, premier servi. Cela pourrait être étendu pour permettre différentes méthodes de vente utilisant différents styles d'enchères.

Les détails du protocole peuvent être lus — et discutés — [sur l'EIP correspondant](https://github.com/ethereum/EIPs/issues/798).

Dans les paragraphes suivants, je vais passer en revue un exemple d'implémentation, disponible sur mon [dépôt GitHub.](https://github.com/pabloruiz55/Saleable)

#### Gestion de la propriété

La gestion de la propriété du contrat est assez basique. Comme on le fait généralement, nous définissons le propriétaire du contrat déployé sur `msg.sender` lors de l'initialisation :

```
function Sellable() public {        owner = msg.sender;        Transfer(now,address(0),owner,0);    }
```

Ensuite, nous ajoutons le modificateur `onlyOwner`, qui sera utilisé sur chaque fonction que nous voulons rendre exécutable uniquement par la personne possédant actuellement le contrat :

```
modifier onlyOwner {        require(msg.sender == owner);        _;
    }
```

Ce que nous voudrons que notre contrat fasse, c'est permettre au `owner` d'être modifié sous certaines conditions.

#### Mettre le contrat en vente

Le propriétaire du contrat peut le mettre en vente en appelant la fonction suivante :

```
function initiateSale(uint _price, address _to) onlyOwner public {        require(_to != address(this) && _to != owner);        require(!selling);                selling = true;                // Définir l'acheteur cible, si spécifié.
        sellingTo = _to;                askingPrice = _price;    }
```

`initiateSale()` prend deux paramètres :

* **uint _price** : qui est le prix auquel le propriétaire souhaite vendre le contrat.
* **address _to** : qui est facultatif et correspond à la personne à qui le propriétaire souhaite vendre le contrat.

Lors de la mise en vente du contrat, le propriétaire a deux options : il peut choisir l'acheteur, auquel cas la vente a été arrangée au préalable. Ou il peut simplement « annoncer » que le contrat est à vendre et la première personne à le réclamer (et à payer son prix) l'obtient.

De plus, le prix demandé peut être fixé à 0. Cela signifie que le propriétaire du contrat est autorisé à offrir, donner ou céder le contrat.

Il y a une autre chose importante à noter : il y a un modificateur `ifNotLocked` qui peut être ajouté aux fonctions du contrat pour empêcher leur exécution si le contrat est dans un processus de vente. S'il est utilisé correctement, cela empêche les données du contrat d'être modifiées juste avant son achat.

Enfin, il y a la fonction `cancelSale()` qui permet au propriétaire d'annuler la vente avant que quelqu'un ne la finalise.

```
function cancelSale() onlyOwner public {        require(selling);                // Réinitialiser les variables de vente
        resetSale();    }
```

#### Acheter le contrat

Une fois le contrat en vente, il suffit à l'acheteur (s'il a été spécifié) ou à n'importe qui (si aucun acheteur particulier n'a été spécifié) d'appeler la fonction suivante :

```
function completeSale() public payable {        require(selling);        require(msg.sender != owner);        require(msg.sender == sellingTo || sellingTo == address(0));        require(msg.value == askingPrice);                // Échanger la propriété
        address prevOwner = owner;        address newOwner = msg.sender;        uint salePrice = askingPrice;                owner = newOwner;                // Nettoyage de la transaction
        resetSale();                prevOwner.transfer(salePrice);                Transfer(now,prevOwner,newOwner,salePrice);    }
```

La fonction `completeSale()` est une fonction `payable` qui nécessite l'envoi d'ether. Le montant à envoyer doit être exactement le même que celui fixé par le propriétaire comme prix demandé.

Lorsque `completeSale()` est exécutée, l'ether sera transféré au propriétaire, puis la propriété sera transférée à l'acheteur. Cela termine la transaction et nettoie le contrat pour le nouveau propriétaire, qui peut désormais l'utiliser normalement, ou même le remettre en vente.

#### Un exemple de cas d'utilisation

Voici un exemple très simple de la façon dont ce contrat de base pourrait être utilisé :

```
contract Kitty is Sellable {        string public name;    uint public kittyValue = 0;        function Kitty(string _name) public {        name = _name;    }        function findNewOwner() public onlyOwner {        kittyValue = kittyValue + 1 ether;           super.initiateSale(kittyValue,address(0));    }        function renameKitty(string newName) ifNotLocked public onlyOwner {        name = newName;    }        function buyKitty() public payable {        require(msg.value == kittyValue);        super.completeSale();    }}
```

Nous avons un contrat qui représente un CryptoKitty ?. Le propriétaire peut appeler `findNewOwner()` pour le mettre en vente. Chaque fois que le kitty est acheté, sa valeur augmente de 1 ether. Le propriétaire du kitty peut changer son nom, tant qu'il n'est pas en cours de vente, en implémentant le modificateur `ifNotLocked` dans `renameKitty`.

#### **C'est tout !**

Si vous avez d'autres suggestions pour améliorer ce protocole Sellable, n'hésitez pas à ajouter vos commentaires, bugs ou suggestions [dans l'EIP que j'ai créé.](https://github.com/ethereum/EIPs/issues/798)

![Image](https://cdn-media-1.freecodecamp.org/images/4T98AkZfQPTp94yyrhpXDLhgsJ76RIWbt1FH)
_Photo de [Unsplash](https://unsplash.com/photos/xulIYVIbYIc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jonas Vincent</a> sur <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_