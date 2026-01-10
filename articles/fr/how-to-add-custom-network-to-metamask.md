---
title: Comment ajouter un réseau personnalisé à Metamask avec JavaScript
subtitle: ''
author: Joshua Omobola
co_authors: []
series: null
date: '2023-01-02T22:17:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-custom-network-to-metamask
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/Frame-1--3--1.png
tags:
- name: dapps
  slug: dapps
- name: JavaScript
  slug: javascript
seo_title: Comment ajouter un réseau personnalisé à Metamask avec JavaScript
seo_desc: 'As a developer, you can enhance the user experience of your decentralized
  applications (DApps) by allowing users to easily add your network to their Metamask
  wallet with just one click.

  This simplifies the process of onboarding users to your applicat...'
---

En tant que développeur, vous pouvez améliorer l'expérience utilisateur de vos applications décentralisées (DApps) en permettant aux utilisateurs d'ajouter facilement votre réseau à leur portefeuille Metamask avec un seul clic.

Cela simplifie le processus d'intégration des utilisateurs à votre application, car ils n'ont pas à ajouter manuellement le réseau eux-mêmes.

Dans cet article, je vais vous montrer comment utiliser JavaScript pour ajouter programmatiquement des réseaux personnalisés à Metamask. Commençons !

## Étape 1 : Vérifier si Metamask est installé

La première chose à faire est de vérifier si le plugin Metamask est installé dans le navigateur de l'utilisateur. Heureusement, Metamask facilite cela en injectant un objet `ethereum` dans les sites web qui l'ont installé.

Pour vérifier la présence de Metamask, vous pouvez simplement essayer d'accéder à l'objet `ethereum`. Vous pouvez le faire en utilisant le code suivant :

```javascript
if (typeof window.ethereum !== 'undefined') {  
 console.log("Metamask est installé")
} else {
  console.log("Metamask n'est pas installé")
}
```

## Étape 2 : Ajouter un réseau personnalisé à Metamask

Pour ajouter programmatiquement un réseau personnalisé à Metamask, vous pouvez utiliser la méthode `request` de l'objet `ethereum`, en lui passant la propriété `wallet_addEthereumChain`.

Par exemple, le code suivant montre comment ajouter le réseau Matic (Polygon) à Metamask :

```javascript
window.ethereum.request({
  method: "wallet_addEthereumChain",
  params: [{
    chainId: "0x89",
    rpcUrls: ["https://polygon-rpc.com/"],
    chainName: "Matic Mainnet",
    nativeCurrency: {
      name: "MATIC",
      symbol: "MATIC",
      decimals: 18
    },
    blockExplorerUrls: ["https://polygonscan.com/"]
  }]
});
```

La méthode `window.ethereum.request()` prend un objet comme argument avec les propriétés method et params. La propriété method doit être définie sur `wallet_addEthereumChain`, et la propriété params doit être un tableau contenant un objet avec les propriétés suivantes :

* `chainId` : L'ID de chaîne du réseau personnalisé qui est une chaîne hexadécimale préférée par 0x.
    
* `rpcUrls` : Un tableau d'URL RPC pour le réseau personnalisé.
    
* `chainName` : Le nom du réseau personnalisé.
    
* `nativeCurrency` : Un objet avec les propriétés name, symbol et decimals, représentant le nom, le symbole et le nombre de décimales de la monnaie native du réseau personnalisé.
    
* `blockExplorerUrls` : Un tableau d'URL d'explorateur de blocs pour le réseau personnalisé.
    

Ce code enverra une demande à Metamask pour ajouter le réseau Polygon (Matic) au portefeuille de l'utilisateur. Si la demande d'ajout du réseau est réussie, `window.ethereum.request()` retournera `null`. Si elle n'est pas réussie, elle retournera une erreur.

### Démo

Pour démontrer comment vous pouvez utiliser ce code, écrivons une fonction simple qui ajoute le réseau Matic lorsqu'elle est appelée.

```javascript
async function addMaticNetwork() {
  try {
    const result = await window.ethereum.request({
      method: "wallet_addEthereumChain",
      params: [{
        chainId: "0x89",
        rpcUrls: ["https://polygon-rpc.com/"],
        chainName: "Matic Mainnet",
        nativeCurrency: {
          name: "MATIC",
          symbol: "MATIC",
          decimals: 18
        },
        blockExplorerUrls: ["https://polygonscan.com/"]
      }]
    });
  } catch (error){
    console.log(error)
  }
```

La fonction `addMaticNetwork`, lorsqu'elle est appelée, invoquera la demande d'ajout du réseau matic. Cette fonction utilise la syntaxe async/await pour gérer la demande de manière asynchrone et inclut un bloc try/catch pour gérer les erreurs qui peuvent survenir.

**Note :** Il est important de noter que vous ne devez jamais inviter automatiquement l'utilisateur à ajouter un réseau sans son consentement explicite. Au lieu de cela, cette demande ne doit être faite qu'en réponse à une action directe de l'utilisateur, comme cliquer sur un bouton.

Cela garantit que l'utilisateur est pleinement conscient du changement apporté à son portefeuille et peut choisir de poursuivre ou d'annuler l'opération comme il le juge approprié.

## Conclusion

Dans cet article, vous avez appris comment ajouter programmatiquement des réseaux personnalisés à MetaMask en utilisant JavaScript.

En implémentant ces étapes dans votre propre DApp, vous pouvez offrir une expérience d'intégration transparente à vos utilisateurs et améliorer leur expérience globale avec votre application.

J'espère que cet article vous a été utile. Souvenez-vous, le monde est votre huître de code.