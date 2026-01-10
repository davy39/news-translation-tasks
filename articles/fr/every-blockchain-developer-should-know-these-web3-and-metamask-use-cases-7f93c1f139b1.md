---
title: Chaque développeur blockchain devrait connaître ces cas d'utilisation de Web3
  et Metamask
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-15T19:00:24.000Z'
originalURL: https://freecodecamp.org/news/every-blockchain-developer-should-know-these-web3-and-metamask-use-cases-7f93c1f139b1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JVmq6javfae3gzTA.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web3
  slug: web3
seo_title: Chaque développeur blockchain devrait connaître ces cas d'utilisation de
  Web3 et Metamask
seo_desc: 'By Igor Yalovoy

  Update

  On November 2nd MetaMask and other dapp browsers will stop exposing user accounts
  by default. This will make some code from this paper to break. I will publish updated
  version with web3 1.0 and new MetaMask interface.

  Metamask ...'
---

Par Igor Yalovoy

### Mise à jour

Le [2 novembre](https://medium.com/metamask/https-medium-com-metamask-breaking-change-injecting-web3-7722797916a8), MetaMask et d'autres navigateurs dapps cesseront d'exposer les comptes utilisateurs par défaut. Cela rendra certains codes de cet article obsolètes. Je publierai une version mise à jour avec web3 1.0 et la nouvelle interface MetaMask.

[Metamask](https://ylv.io/10-web3-metamask-use-cases-ever-blockchain-developer-needs/Metamask.io) est le standard de facto pour les dApps sur le web. Il injecte une instance Web3 dans l'objet window, la rendant disponible pour le code JavaScript.

Nous allons utiliser la version Web3 0.20, et non Web3 1.0. Le code pour Web3 1.0 serait différent.

Chaque dApp a sa mission, mais la manière dont elles interagissent avec Metamask est similaire. Dans cet article, nous allons couvrir les dix pratiques les plus courantes pour gérer les interactions Web3/Metamask.

### #1. Détecter Metamask et instancier Web3

Selon la [documentation](https://github.com/MetaMask/faq/blob/master/DEVELOPERS.md#partly_sunny-web3---ethereum-browser-environment-check), voici la meilleure façon de procéder.

Que se passe-t-il ici ? Tout d'abord, nous vérifions si Web3 a été injecté. Si c'est le cas, nous créons une nouvelle instance en utilisant le fournisseur injecté. Pourquoi ? Parce que nous voulons utiliser notre version de bibliothèque, et non celle injectée par Metamask.

Si Web3 n'est pas présent, nous essayons de nous connecter à un fournisseur localhost, comme [ganache](https://truffleframework.com/ganache).

### #2. Vérifier si Metamask est verrouillé

Metamask peut être installé mais verrouillé. Pour interagir avec un compte utilisateur et envoyer des transactions, l'utilisateur doit déverrouiller Metamask.

### #3. Vérifier le réseau actuel

Il existe de nombreux réseaux de test au-delà du réseau principal. Typiquement, votre contrat est déployé sur un certain réseau. Vous voulez être sûr que l'utilisateur exécute Metamask sur le même réseau.

### #4. Obtenir le compte actuel

Un utilisateur peut avoir plusieurs comptes sur Metamask, mais il s'attend à ce que la dApp interagisse avec celui actuellement sélectionné.

Vous devez toujours récupérer le compte à partir de l'instance Web3. Ne le conservez pas et ne le réutilisez pas, car l'utilisateur peut changer de compte à tout moment.

### #5. Obtenir le solde du compte actuel

Ici, nous utilisons la fonction `getAccount` de #4 et appelons `getBalance`. Simple.

### #6. Détecter que le compte actuel a changé

Un utilisateur peut changer de compte à tout moment. Votre dApp doit être prête pour cela et réagir correctement.

### #7. Détecter si Metamask est verrouillé/déverrouillé

Similaire à #6. Un utilisateur peut verrouiller/déverrouiller à tout moment. Votre dApp doit le gérer correctement.

### #8. Gérer l'annulation/confirmation

Une fois qu'un utilisateur interagit avec votre dApp, vous devez envoyer une transaction en utilisant l'API Web3. Un utilisateur peut appuyer sur le bouton annuler ou confirmer dans la fenêtre contextuelle de Metamask. Cela peut entraîner une incohérence de l'interface utilisateur si ce n'est pas géré correctement.

Pour retourner instantanément avec le hash de la transaction, appelez `contract.methodName.sendTransaction`.

### #9. Obtenir le reçu de transaction

Une fois que votre transaction dApp est minée, un reçu de transaction devient disponible. Cependant, il n'y a pas d'événement/notification, donc nous devons implémenter un mécanisme de sondage.

### #10. Écouter les événements Web3

Les événements Solidity sont géniaux. Ils permettent de passer d'un mécanisme de sondage peu élégant à un simple mécanisme de push, à condition que votre contrat implémente tous les événements nécessaires. Vous pouvez complètement éviter le sondage et simplement réagir aux événements. Le rappel d'événement [retourne](https://github.com/ethereum/wiki/wiki/JavaScript-API#callback-return) beaucoup de données, mais nous nous intéressons principalement à `args`.

### Résumé

Quelle que soit la mission de votre dApp, elle doit toujours effectuer des tâches courantes, telles que détecter Web3, obtenir l'état du compte et le solde, reconnaître le réseau actuel, et gérer les transactions et les événements. Nous avons passé en revue comment cela peut être fait en utilisant dix extraits de code.

### P.S.

Beaucoup d'exemples ici utilisent des méthodes qui peuvent générer une erreur en raison de l'état de Metamask ou de certaines variables étant indéfinies au moment de l'appel. Vous devez les envelopper dans `try/catch` dans un environnement de production.  
 Async/await a été utilisé ici pour simplifier. Il peut être remplacé par Promise then/catch.

### Social

* Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/ylv-io/).
* Suivez-moi sur [twitter](https://twitter.com/ylv_io).

### Voulez-vous en savoir plus ?

[**Comment créer et déployer votre propre token EOS**](https://hackernoon.com/how-to-create-and-deploy-your-own-eos-token-1f4c9cc0eca1)  
[_Nous allons découvrir ce qu'est un token EOS et comment vous pouvez en créer et en déployer un vous-même._hackernoon.com](https://hackernoon.com/how-to-create-and-deploy-your-own-eos-token-1f4c9cc0eca1)[**Combien coûte l'exécution d'une DApp en 2018**](https://hackernoon.com/how-much-does-it-costs-to-run-dapp-in-2018-87ee11fe1d5d)  
[_Vous pensez que votre facture AWS ou Digital Ocean pour votre site web est en train de vous ruiner ?_hackernoon.com](https://hackernoon.com/how-much-does-it-costs-to-run-dapp-in-2018-87ee11fe1d5d)[**Différence entre les tokens Ethereum et EOS**](https://medium.com/coinmonks/difference-between-ethereum-and-eos-tokens-f2399051c0b6)  
[_Ethereum a le token ERC-20 et EOS a EOSIO.Token. Ils servent le même but, mais sont-ils identiques ?_medium.com](https://medium.com/coinmonks/difference-between-ethereum-and-eos-tokens-f2399051c0b6)

_Publié à l'origine sur [ylv.io](https://ylv.io/10-web3-metamask-use-cases-ever-blockchain-developer-needs/) le 15 octobre 2018._