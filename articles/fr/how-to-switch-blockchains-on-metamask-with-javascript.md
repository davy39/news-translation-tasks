---
title: Comment changer de blockchains sur MetaMask avec JavaScript
subtitle: ''
author: Joshua Omobola
co_authors: []
series: null
date: '2023-01-26T23:15:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-switch-blockchains-on-metamask-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Custom-Network--1-.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: JavaScript
  slug: javascript
seo_title: Comment changer de blockchains sur MetaMask avec JavaScript
seo_desc: 'With over 10,000 blockchains currently operating, there are endless possibilities
  for deploying your smart contracts.

  For anybody to be able to use your Decentralized Application (DApp), they need to
  be connected to the blockchain where you''ve deploy...'
---

Avec plus de 10 000 blockchains actuellement en fonctionnement, les possibilités de déployer vos contrats intelligents sont infinies.

Pour que quiconque puisse utiliser votre application décentralisée (DApp), il doit être connecté à la blockchain où vous avez déployé votre contrat intelligent.

Cet article vous montrera comment inviter vos utilisateurs à basculer vers votre blockchain préférée en utilisant JavaScript.

Ce guide nécessite que vous ayez l'extension MetaMask installée. De plus, je suppose que vous avez un peu d'expérience avec la connexion à MetaMask, peut-être avez-vous déjà construit une DApp. Si vous avez besoin d'une introduction rapide, [consultez cet excellent article de MetaMask pour commencer](https://docs.metamask.io/guide/create-dapp.html#basic-action-part-1).

Très bien, commençons !

## Étape 1 – Vérifier si l'utilisateur a installé MetaMask

La première chose à faire est de vérifier si l'utilisateur a installé l'extension MetaMask.

S'il a un autre portefeuille installé en plus de MetaMask, le changement de réseau en utilisant la méthode que nous allons apprendre pourrait ne pas fonctionner. Il est donc bon de vérifier d'abord.

Vérifions si le contexte `ethereum` a été injecté dans le navigateur. L'exemple de code ci-dessous montre comment faire :

```javascript
const { ethereum } = window;

if (typeof ethereum !== 'undefined' && ethereum.isMetaMask) {  
 console.log("MetaMask est installé")
} else {
  console.log("MetaMask n'est pas installé")
}
```

Voici ce que nous faisons :

À `const { ethereum } = window;` nous déstructurons la propriété `ethereum` de l'objet window et l'assignons à une variable du même nom.

Si vous n'êtes pas familier avec cette syntaxe, la déstructuration consiste simplement à extraire le contenu d'un objet ou d'un tableau et à l'assigner à une variable. [Lisez cet article pour en savoir plus sur la déstructuration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

Ensuite, nous vérifions si `ethereum` existe réellement en utilisant l'instruction if. De plus, dans la même condition, nous voulons vérifier si le portefeuille installé est MetaMask.

Bien ! Passons à l'étape suivante.

## Étape 2 – Comment changer la blockchain active

Une fois que nous avons vérifié que l'utilisateur a installé MetaMask, la prochaine chose à faire est de déclencher la méthode RPC pour changer la blockchain active de MetaMask. Le code ressemble à ceci :

```javascript
// Documentation MetaMask
try {
  await ethereum.request({
    method: 'wallet_switchEthereumChain',
    params: [{ chainId: '0xf00' }],
  });
} catch (switchError) {
// Ce code d'erreur indique que la chaîne n'a pas été ajoutée à MetaMask.
  if (switchError.code === 4902) {
  	// Faire quelque chose
  }
}
```

Voici ce que nous faisons :

Nous invoquons la méthode `ethereum.request`, en lui passant un objet avec deux propriétés.

Dans la propriété method, nous spécifions la méthode RPC `wallet_switchEthereumChain`, qui permet aux applications Ethereum (DApps) de demander à MetaMask de changer sa chaîne Ethereum active.

Ensuite, la propriété params est un tableau qui prend un objet avec l'ID de chaîne de la blockchain à laquelle basculer. `chainId` doit être en hexadécimal, d'où le 0x dans le code exemple.

Nous enveloppons notre demande dans un bloc try/catch pour gérer les erreurs.

`null` est retourné si la chaîne active est changée.

Si la chaîne demandée n'existe pas dans le portefeuille de l'utilisateur, la demande génère un code d'erreur `error.code` de `4902`. Si cela se produit, vous pouvez demander à ajouter la chaîne au portefeuille.

Vous pouvez suivre ce guide pour voir [comment ajouter une nouvelle chaîne à MetaMask en utilisant JavaScript](https://www.freecodecamp.org/news/how-to-add-custom-network-to-metamask/).

Super ! C'est tout ce qu'il faut pour changer la chaîne active sur MetaMask avec JavaScript.

Faisons une rapide démonstration dans la section suivante.

## Démo

Pour cet exemple, écrivons une fonction qui, lorsqu'elle est invoquée, demandera aux utilisateurs de basculer vers la chaîne Polygon.

```javascript
const SwitchChainToPolygon = () => {
	const { ethereum } = window;
    if (typeof ethereum !== 'undefined' && ethereum.isMetaMask) return;
    
    try {
      await ethereum.request({
        method: 'wallet_switchEthereumChain',
        params: [{ chainId: '0x89' }],
      });
    } catch (switchError) {
      if (switchError.code === 4902) {
        // Vous pouvez faire une demande pour ajouter la chaîne au portefeuille ici
        console.log('La chaîne Polygon n\'a pas été ajoutée au portefeuille !')
      }
    }
}
```

Dans la fonction `SwitchChainToPolygon` ci-dessus, nous avons déstructuré `ethereum` de l'objet window, comme nous l'avons appris dans l'Étape 1.

Ensuite, nous avons vérifié si `ethereum` existe ou non. Si `ethereum` n'est pas disponible, c'est-à-dire si MetaMask n'est pas installé, la fonction se terminera.

Si `ethereum` existe, nous appelons la méthode `ethereum.request` pour faire un appel RPC. Pour la propriété `method`, nous lui donnons une valeur de `wallet_switchEthereumChain`. Pour les `params`, `chainId` aura la valeur de `0x89` ( `167` en décimal) qui est le chainId pour la blockchain polygon.

C'est tout, les amis !

## Conclusion

Dans cet article, vous avez appris comment changer de blockchains sur MetaMask avec JavaScript. Cela vous aidera à offrir une expérience utilisateur sans friction pour vos utilisateurs.

Merci d'avoir pris le temps de lire ceci. J'espère que vous l'avez trouvé utile. N'hésitez pas à me contacter et à discuter avec moi sur [Twitter](https://twitter.com/kohawithstuff) et [YouTube](https://youtube.com/@kohawithstuff). À bientôt dans mon prochain article !