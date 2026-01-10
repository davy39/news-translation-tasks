---
title: Comment écrire et déployer votre premier smart contract
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T00:58:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-and-deploy-your-first-smart-contract-341d5e2ffb35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZnxSoYqZH9IOH3G5WUposA.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: Smart Contracts
  slug: smart-contracts
- name: 'tech '
  slug: tech
seo_title: Comment écrire et déployer votre premier smart contract
seo_desc: 'By Avadhoot Kulkarni

  Ever since Ethereum graced the crypto space with its presence in mid-2015, the revolutionary
  invention by Canadian-Russian Programmer Vitalik Buterin has given birth to many
  new decentralised applications (dApps). Along with the ...'
---

Par Avadhoot Kulkarni

Depuis qu'[Ethereum](https://ethereum.org) a fait son apparition dans l'espace crypto à la mi-2015, l'invention révolutionnaire du programmeur canado-russe Vitalik Buterin a donné naissance à de nombreuses nouvelles applications décentralisées (dApps). En plus de la myriade de dApps en cours de développement, le succès d'Ethereum est principalement attribué à sa mise en œuvre de smart contracts.

Il est intéressant de noter que l'invention des smart contracts remonte à 1996. Le scientifique informatique Nick Szabo a élaboré le terme « smart contracts » et les explique comme suit :

> « Je appelle ces nouveaux contrats « intelligents », car ils sont bien plus fonctionnels que leurs ancêtres inanimés sur papier. Aucune utilisation de l'intelligence artificielle n'est impliquée. Un smart contract est un ensemble de promesses, spécifiées sous forme numérique, incluant des protocoles dans lesquels les parties exécutent ces promesses »
>   
> — [Nick Szabo](http://www.fon.hum.uva.nl/rob/Courses/InformationInSpeech/CDROM/Literature/LOTwinterschool2006/szabo.best.vwh.net/smart_contracts_2.html), 1996

Son travail a ensuite inspiré de nombreux autres chercheurs et scientifiques, y compris Vitalik, qui a créé Ethereum.

### Informations de base

Avant d'aller plus loin dans le guide, il est important de comprendre deux concepts importants.

La première chose que nous devons comprendre est ce qu'est la Machine Virtuelle Ethereum (**EVM**). Son seul but est d'agir comme un environnement d'exécution pour les smart contracts basés sur Ethereum. Pensez-y comme un super ordinateur global qui exécute tous les smart contracts. Comme son nom l'indique, l'EVM est virtuelle et non une machine physique. Vous pouvez [en savoir plus sur l'EVM ici](https://themerkle.com/what-is-the-ethereum-virtual-machine/).

Le deuxième concept que nous devons comprendre est ce qu'est le **gas**. Dans l'EVM, le gas est une unité de mesure utilisée pour attribuer des frais à chaque transaction avec un smart contract. Chaque calcul qui se produit dans l'EVM nécessite du gas. Plus c'est complexe et fastidieux, plus il faut de gas pour exécuter le smart contract.

Chaque transaction spécifie le prix du gas qu'elle est prête à payer en ether pour chaque unité de gas, permettant au marché de décider de la relation entre le prix de l'ether et le coût des opérations de calcul (mesuré en gas). C'est la combinaison des deux, le gas total utilisé multiplié par le prix du gas payé, qui résulte en les frais totaux payés par une transaction.

```
Frais pour la transaction = Gas total utilisé * prix du gas;
```

En savoir plus sur le gas [ici](https://ethereum.stackexchange.com/questions/3/what-is-meant-by-the-term-gas).

Maintenant que vous avez des connaissances de base sur ce qu'est un smart contract et comment il s'exécute, nous pouvons passer directement à la création de notre propre smart contract !

### Installation

Nous allons utiliser un outil pour cela : Pragma. C'est une plateforme facile à utiliser pour créer et déployer des smart contracts. [Inscrivez-vous ici](https://www.withpragma.com/) et allez à l'éditeur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*eyY1_mE0Kw250gdZ0B0AOg.jpeg)

Connectez-vous à MetaMask. Si vous n'avez pas encore installé MetaMask, [vous pouvez commencer ici](https://help.indorse.io/hc/en-us/articles/360001815251-Using-MetaMask-on-Indorse).

Passez au réseau de test Kovan à la fois dans Pragma et MetaMask.  
Juste pour vous donner un bref aperçu des testnets, consultez [cet article](https://karl.tech/intro-guide-to-ethereum-testnets/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*X-yIFMaU0inr5_32wo6d9w.jpeg)

Le mainnet Ethereum est le réseau Ethereum officiel. Il est plus sécurisé et utilise de l'Ether, qui a une valeur monétaire réelle.

Les testnets sont des réseaux Ethereum de test dans lesquels l'Ether est convenu de n'avoir aucune valeur monétaire. Les développeurs utilisent ces environnements de test pour tester les applications avant de les déployer sur le mainnet pour leurs utilisateurs.

Pour basculer entre ces réseaux, cliquez sur le nom du réseau à côté de l'icône MetaMask et sélectionnez le réseau. Pour ce tutoriel, veuillez choisir **Kovan**.

### Écriture du smart contract

Le contrat suivant implémentera la forme la plus simple d'une cryptomonnaie. Il est possible de générer des pièces à partir de rien, mais seule la personne qui a créé le contrat est capable de le faire (il est trivial d'implémenter un schéma d'émission différent). De plus, n'importe qui peut envoyer des pièces à d'autres sans avoir besoin de s'enregistrer avec un nom d'utilisateur et un mot de passe. Tout ce dont vous avez besoin est une paire de clés Ethereum.

```
pragma solidity ^0.4.21; // indique que le code source est écrit pour la version Solidity 0.4.21 ou toute version plus récente qui ne casse pas la fonctionnalité


contract yourToken {
    // Le mot-clé "public" rend ces variables lisibles depuis l'extérieur.
    
    address public minter;
    
    // Les événements permettent aux clients légers de réagir aux changements de manière efficace.
    mapping (address => uint) public balances;
    
    // Ceci est le constructeur dont le code est exécuté uniquement lorsque le contrat est créé
    event Sent(address from, address to, uint amount);
    
    function yourToken() public {
        
        minter = msg.sender;
        
    }
    
    function mint(address receiver, uint amount) public {
        
        if(msg.sender != minter) return;
        balances[receiver]+=amount;
        
    }
    
    function send(address receiver, uint amount) public {
        if(balances[msg.sender] < amount) return;
        balances[msg.sender]-=amount;
        balances[receiver]+=amount;
        emit Sent(msg.sender, receiver, amount);
        
    }
    
    
}
```

Ce code vous permet essentiellement de créer et d'envoyer des tokens à d'autres comptes.

Passons-le en revue ligne par ligne :

```
pragma solidity ^0.4.21;
```

Cela indique que le code source est écrit pour la version Solidity 0.4.21 ou toute version plus récente qui ne casse pas la fonctionnalité. Cela est pour s'assurer que le code ne se comporte pas différemment avec les nouvelles versions du compilateur.

```
contract yourToken
```

Tout ce qui est lié à yourToken va à l'intérieur de ce contrat. Essentiellement, un contrat en solidity est la collection de fonctions et d'états (code et données) situés à une adresse sur la blockchain Ethereum.

```
address public minter;
```

Ceci est l'adresse du minter. Le mot-clé « public » rend ces variables lisibles depuis l'extérieur.

```
event Sent(address from, address to, uint amount);
```

Les événements permettent aux clients légers (UI) de réagir aux changements de manière efficace.

```
function yourToken() public {
  minter = msg.sender;
}

```

Définissons votre adresse Ethereum comme minter du contrat. Vous devrez accéder au contrat via votre MetaMask pour pouvoir créer des tokens. Nous passerons à nouveau par cela après avoir déployé le contrat.

```
function mint(address receiver, uint amount) public {
  if(msg.sender != minter) return;
  balances[receiver]+=amount;
}

```

Cette fonction vous permet de créer la quantité de pièces que vous souhaitez. Vous pouvez créer autant de tokens que vous le souhaitez. La condition if indique au système d'arrêter l'exécution si vous n'êtes pas le minter, qui est défini dans la fonction yourToken.

Si vous êtes effectivement le minter, cela vous permet de créer les tokens.

```
function send(address receiver, uint amount) public {
  if(balances[msg.sender] < amount) return;
  balances[msg.sender]-=amount;
  balances[receiver]+=amount;
  emit Sent(msg.sender, receiver, amount);
}
```

Ceci est une fonction qui permet à une adresse d'envoyer des tokens à une autre adresse. Elle prend deux paramètres : receiver et amount. Elle réduit le montant de l'adresse de l'expéditeur et ajoute le même montant à l'adresse du destinataire. L'événement Sent, que nous avons déclaré précédemment, est maintenant utilisé pour effectuer le transfert. Actuellement, nous avons gardé l'expéditeur comme msg.sender, qui est le minter, car nous ne voulons pas compliquer le contrat.

C'est tout. Votre contrat est maintenant prêt, alors compilons-le.

### Compilation et déploiement du smart contract

![Image](https://cdn-media-1.freecodecamp.org/images/1*FAUfzAPntHXqVNR5rpy3Yw.jpeg)

Une fois le contrat compilé, déployons-le sur la blockchain. Comme mentionné précédemment, nous utiliserons le testnet Kovan pour déployer le contrat.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5OA2_s3vB2LP21UBkjaNSg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ne5LsQuTlRr3sl5iFqB1Ng.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*G0PBdUtSixgVxrxIJNOG9g.jpeg)

Vérifiez si le smart contract est déployé.

Pour le contrat que j'ai déployé pour ce tutoriel, [voici la transaction](https://kovan.etherscan.io/tx/0x96a3b24fedd12e79a6e16adf0dd05970e0a011510f302fdadc9d1559ad90a8fc). Vous pouvez également le voir dans Pragma sous vos contrats.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vtsp6UMTFbCgJAs8mGzrwg.jpeg)

### Interagir avec le smart contract dans Pragma

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vtsp6UMTFbCgJAs8mGzrwg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Py8LRkKzZblALzT_hCHI3g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*NVpHZwOZN0-8lzwpW1tm5A.jpeg)
_Créons 1000000 tokens !_

![Image](https://cdn-media-1.freecodecamp.org/images/1*QJRNPSNpnvYa9LX02WB-6g.jpeg)
_Signature de la transaction_

![Image](https://cdn-media-1.freecodecamp.org/images/1*pEs1g4LSvT9ufNv_ki9Big.jpeg)
_Yay !_

Vous y êtes. Votre premier smart contract, déployé sur la blockchain. :)

Beaucoup de nouveaux concepts ont été introduits ainsi que quelques outils incroyablement utiles. Cela peut être un peu écrasant, et c'est normal ! Essayez simplement de comprendre les concepts et ensuite lancez-vous.

Avez-vous créé des smart contracts simples mais intéressants ? Postez-les dans les commentaires et je les ajouterai dans l'article pour référence.

Vous avez des questions ? Ajoutez-les dans les commentaires ou rejoignez notre groupe Telegram et [parlez-nous directement](https://t.me/indorseio).