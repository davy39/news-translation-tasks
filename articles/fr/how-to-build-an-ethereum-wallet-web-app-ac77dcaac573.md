---
title: Comment créer une application web de portefeuille Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T16:27:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-ethereum-wallet-web-app-ac77dcaac573
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TzOKAf_ykKIz8qC0VrJHGA.png
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment créer une application web de portefeuille Ethereum
seo_desc: 'By Paul Laux

  A review of the coolest parts of eth-hot-wallet

  This article is a technical review of the interesting parts of eth-hot-wallet, an
  Ethereum wallet web app with erc20 token native support. The source code can be
  found on GitHub (MIT Licens...'
---

Par Paul Laux

#### Une revue des parties les plus intéressantes de eth-hot-wallet

Cet article est une revue technique des parties intéressantes de **eth-hot-wallet**, une [application web de portefeuille Ethereum](http://eth-hot-wallet.com) avec support natif des tokens erc20. Le code source peut être trouvé sur [GitHub](https://github.com/PaulLaux/eth-hot-wallet) (Licence MIT).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6wrsZ2k5DdEHIpS8u-4p1A.png)
_aperçu de eth-hot-wallet_

**Table des matières :**

* Application web de portefeuille Ethereum
* La stack
* Les conteneurs de eth-hot-wallet
* Design unifié pour le portefeuille Ethereum
* Redux et Redux-Saga
* Générateur de mot de passe _sécurisé_
* eth-lightwallet et SignerProvider
* Stockage hors ligne chiffré
* Envoyer de l'Ethereum en utilisant Web3.js
* Envoyer des tokens erc20 en utilisant Web3.js
* S'abonner au cycle de vie des transactions Ethereum en utilisant Web3.js V1 et les canaux Redux-Saga
* Interroger la blockchain Ethereum et les données de prix en utilisant Redux-Saga
* Surveiller la taille du bundle
* Conclusion

### Application web de portefeuille Ethereum

Lorsque le logiciel est déployé en tant qu'application web, la large accessibilité est la première chose qui vient à l'esprit. Après tout, le web est la plateforme multi-appareils la plus largement accessible. Eth-hot-wallet est une PWA (progressive web app) qui peut être utilisée depuis n'importe quel navigateur web moderne.

De plus, [les améliorations récentes dans le support des PWA](https://medium.com/appscope/designing-native-like-progressive-web-apps-for-ios-1b3cdda1d0e8) améliorent significativement l'expérience utilisateur sur mobile.

Avantages :

* Aucun logiciel supplémentaire n'est requis
* Aucune installation de quelque sorte que ce soit n'est nécessaire
* Capacité à utiliser des outils de développement web modernes.
* Facile à déployer et à mettre à jour

Inconvénients :

* Plus sujet aux attaques de phishing.
* Les plugins de navigateur peuvent injecter du code malveillant dans la page.
* Temps de chargement élevé sur les connexions internet lentes
* Accès limité au stockage de l'appareil

Le fait que des extensions de navigateur malveillantes puissent injecter du code JavaScript dans une tentative d'extraire les clés est significatif. Pour migrer ce risque, l'utilisateur devrait être encouragé à désactiver les extensions (c'est-à-dire en utilisant le mode incognito) ou à intégrer le web avec un fournisseur web3 externe tel que MetaMask ou le navigateur Trust. Convertir l'application web en une application de bureau est également une option viable.

En ce qui concerne le phishing, l'utilisateur devrait être encouragé à mettre la page en favoris et à y accéder via la recherche Google. Il est très peu probable qu'un site de phishing se classe au-dessus du site réel dans les résultats de recherche.

**En résumé : une application web vous permettra d'atteindre le public le plus large avec un minimum de friction**. À mon avis, le web est la meilleure plateforme cible pour les nouvelles applications.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TzOKAf_ykKIz8qC0VrJHGA.png)
_logo de eth-hot-wallet_

### La stack

La majeure partie du code est dédiée au **front-end** :

Le package final se compose de nombreux packages comme on peut le voir dans [package.json](https://github.com/PaulLaux/eth-hot-wallet/blob/master/package.json).

Les composants de haut niveau incluent :

* [Eth-lightwallet](https://github.com/ConsenSys/eth-lightwallet) — Portefeuille JS léger pour Node et le navigateur pour la gestion du keystore
* React, Redux, saga.js, immutableJS et reselect enveloppés par le [react-boilerplate](https://github.com/react-boilerplate/react-boilerplate) offline-first
* [Ant design](https://github.com/ant-design/ant-design) — excellent ensemble de composants UI pour react
* [Webpack](https://webpack.github.io/) — Un bundler pour JavaScript et ses amis.

Et pour le **back-end** :

Le bundle final est déployé directement sur GitHub pages à partir d'une branche dédiée dans le dépôt. Il n'y a pas besoin de back-end dans le sens traditionnel.

Pour créer le robinet Ethereum Testnet, nous utiliserons un [framework Serverless](https://serverless.com/framework/docs/getting-started/). Il améliore significativement l'expérience du développeur lors de l'utilisation d'AWS Lambda. C'est une solution très rentable qui élimine le besoin de maintenir une infrastructure, surtout pour les applications à faible volume.

### Les conteneurs de eth-hot-wallet

![Image](https://cdn-media-1.freecodecamp.org/images/1*ufHAtmbsMCMSNwGKX63Zjg.png)
_conteneur de la page d'accueil de eth-hot-wallet_

Lorsque l'on utilise la combinaison de React, Redux, Saga.js et Reselect, chaque conteneur (peut) se composer des ingrédients suivants :

* index.js — pour rendre l'interface graphique
* actions.js
* reducer.js
* saga.js
* selectors.js
* constants.js

Comme [Dan Abramov](https://www.freecodecamp.org/news/how-to-build-an-ethereum-wallet-web-app-ac77dcaac573/undefined) l'a déclaré, il existe [plus d'une approche](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) pour décider d'utiliser un composant ou un conteneur. D'après mon expérience, si un composant a plus de ~8 attributs dans l'état de l'application, il devrait être séparé dans un nouveau conteneur. Ce n'est qu'une règle empirique. Le nombre d'attributs peut gonfler avec le temps. Avec des composants complexes, il est préférable d'avoir un conteneur unique plutôt que de regrouper l'état du conteneur principal.

Tous les conteneurs n'ont pas besoin d'avoir tous les ingrédients. Dans eth-hot-wallet, le [conteneur](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/SendToken) [sendToken](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/SendToken) n'utilise pas son propre Saga.js. Nous l'avons séparé afin de ne pas alourdir l'état du composant de la page d'accueil.

#### Le conteneur de la page d'accueil

![Image](https://cdn-media-1.freecodecamp.org/images/1*eqJKGRGa7YpBigSGKBYBQw.jpeg)
_conteneur de la page d'accueil de eth-hot-wallet_

Le conteneur principal, où la plupart de l'action se déroule, est le [conteneur de la page d'accueil](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/HomePage). Dans le conteneur de la page d'accueil, Saga.js est responsable de la gestion des effets secondaires. En plus de l'interface graphique, sa principale responsabilité sera de gérer les **opérations de keystore**.

Le package ETH-Lightwallet fournit le keystore. Toutes les opérations connexes, y compris les clés, les seeds, le chiffrement, l'importation, l'exportation, sont effectuées dans cette section.

#### Le conteneur d'en-tête

[L'en-tête](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/Header) démontre le fait qu'un conteneur est bien plus qu'un simple composant d'interface graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ckDt0s8GbB2YeynBss4Qug.jpeg)
_conteneur d'en-tête de eth-hot-wallet_

Ce conteneur peut sembler simple au premier abord avec seulement un logo et un sélecteur de réseau. A-t-il vraiment besoin d'être dans son propre conteneur ? La réponse est que dans eth-hot-wallet **toute action et gestion d'état liée à la communication réseau est effectuée dans le conteneur d'en-tête**. Plus que suffisant pour n'importe quel conteneur.

#### Le conteneur SendToken

[SendToken](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/SendToken) est une modale qui apparaît lorsque l'utilisateur sélectionne l'envoi d'Ether/tokens.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DFy9RyZievPsl3gyCTYC4A.png)
_conteneur SendToken de eth-hot-wallet_

La modale inclut une vérification de base des entrées, comme la vérification du montant et de l'adresse Ethereum. Elle n'utilise pas Saga.js pour initier des effets secondaires, mais utilise plutôt des actions fournies par les conteneurs de la page d'accueil et de l'en-tête.

**Nous l'avons séparé dans un nouveau conteneur pour réduire le regroupement de l'état du conteneur de la page d'accueil.**

#### Conteneur TokenChooser

[Token Chooser](https://github.com/PaulLaux/eth-hot-wallet/tree/master/app/containers/TokenChooser) apparaît lorsque l'utilisateur souhaite sélectionner quel token le portefeuille gérera.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XY_vFMJBjz_HFka9SpTZGA.png)
_conteneur TokenChooser de eth-hot-wallet_

Le nom `TokenChooser` a été sélectionné afin de ne pas être confondu avec le terme "selector" qui apparaît de nombreuses fois dans le code du portefeuille dans un contexte différent ([reduxjs/reselect: Bibliothèque de sélecteurs pour Redux](https://github.com/reduxjs/reselect)).

Comme pour le conteneur `SendToken`, `TokenChooser` n'utilise pas son propre fichier Saga.js mais appelle des actions du conteneur de la page d'accueil lorsque nécessaire.

### Un design unifié pour le portefeuille Ethereum

Depuis l'apparition de la norme ERC20 ([EIP20](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20-token-standard.md)), il était évident que les tokens allaient devenir une partie importante de l'écosystème Ethereum. Le portefeuille Ethereum a été conçu avec une approche de design unifié à l'esprit. **L'Ether et les tokens doivent être traités de manière égale du point de vue de l'utilisateur.**

Sous le capot, l'API pour envoyer de l'Ether et envoyer des tokens est assez différente. Il en va de même pour la vérification du solde, mais ils apparaîtront de la même manière sur l'interface graphique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2IKgDyCw0ogdCKZhWsx2_w.png)
_[Un design unifié pour le portefeuille Ethereum](https://eth-hot-wallet.com" rel="noopener" target="_blank" title=")_

Pour envoyer de l'Ether, nous devons utiliser des fonctions natives fournies par la bibliothèque web3.js, tandis que l'envoi de tokens et la vérification des soldes impliquent une interaction avec un contrat intelligent. Plus d'informations sur ce sujet plus tard.

### Redux et Redux-Saga

L'utilisation du store Redux comme source unique de vérité bénéficie grandement au portefeuille. Les actions de l'interface graphique et les flux déclenchés par l'utilisateur peuvent être relativement facilement gérés par les actions et les réducteurs fournis par Redux.

En plus de maintenir l'état de l'interface utilisateur, le store Redux contient également l'objet key-store (un objet JavaScript partiellement chiffré fourni par eth-lightwallet). Cela rend le keystore accessible dans toute l'application en utilisant un sélecteur.

[Redux-Saga](https://github.com/redux-saga/redux-saga) est ce qui fait briller l'ensemble de la configuration.

> `redux-saga` est une bibliothèque qui vise à rendre les effets secondaires de l'application (c'est-à-dire, les choses asynchrones comme la récupération de données et les choses impures comme l'accès au cache du navigateur) plus faciles à gérer, plus efficaces à exécuter, faciles à tester et meilleures pour gérer les échecs.

Saga.js utilise des générateurs pour rendre les **flux asynchrones faciles à lire et à écrire**. En faisant cela, ces flux asynchrones ressemblent à votre code JavaScript synchrone standard (un peu comme `async`/`await` mais avec plus d'options de personnalisation).

Dans le cas du portefeuille Ethereum, en utilisant Saga, nous obtenons une manière confortable de gérer les actions asynchrones telles que les appels à l'API REST, les actions de keystore, les appels à la blockchain Ethereum via web3.js, et plus encore. Toutes les requêtes sont gérées proprement en un seul endroit, sans enfer de rappels, et avec une API très intuitive.

**Exemple d'utilisation pour redux-saga :**

### Générateur de mot de passe _sécurisé_

![Image](https://cdn-media-1.freecodecamp.org/images/1*IkEbKHk8GAENsl9M3pGuog.png)
_Une seed et un mot de passe sécurisé sont générés automatiquement pour l'utilisateur_

Pour sécuriser adéquatement le keystore de l'utilisateur, nous devons le chiffrer avec un mot de passe fort. Lorsque nous utilisons eth-lightwallet, le mot de passe doit être fourni lors de l'initialisation du [hd-wallet](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=2ahUKEwiV_JvMw4_dAhWMDcAKHfGpANYQFjACegQICBAB&url=https%3A%2F%2Fethereum.stackexchange.com%2Fquestions%2F33395%2Fwhat-is-a-hd-wallet-for-ether-and-how-to-create-one-using-nodejs%3Frq%3D1&usg=AOvVaw2P31H_vW_U9Dc8tZHEcrNA).

Supposons que nous avons une fonction appelée `generateString`, qui peut fournir des chaînes vraiment aléatoires de n'importe quelle longueur.

Si l'utilisateur souhaite générer un nouveau portefeuille, nous allons produire les paramètres suivants :

Nous pouvons demander à l'utilisateur de confirmer le mot de passe et la seed ou générer un nouvel ensemble en son nom. Alternativement, nous pouvons demander à l'utilisateur sa propre seed et son mot de passe existants.

Implémentation de `generateString` : Nous allons utiliser l'API relativement nouvelle [**window.crypto API**](https://developer.mozilla.org/en-US/docs/Web/API/Window/crypto) pour obtenir des valeurs aléatoires (actuellement [prise en charge par tous les principaux navigateurs](https://caniuse.com/#feat=getrandomvalues)).

[L'implémentation de Eth-hot-wallet](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/utils/crypto.js) est basée sur le code suivant pour générer des **chaînes aléatoires mais lisibles par l'homme** :

Après que l'utilisateur a accepté le mot de passe et la seed, nous pouvons utiliser les valeurs et générer le nouveau portefeuille.

### eth-lightwallet et SignerProvider

1. LightWallet est destiné à être un fournisseur de signature pour le [fournisseur Web3 hooké](https://github.com/ConsenSys/hooked-web3-provider).
2. Le fournisseur Web3 hooké a été déprécié, et actuellement l'auteur recommande le package [ethjs-provider-signer](https://github.com/ethjs/ethjs-provider-signer/) comme alternative.
3. Au moment de l'écriture, il y a un bug dans ethjs-provider-signer qui empêche l'affichage des messages d'erreur. Le bug a été corrigé mais n'a pas été fusionné dans la branche principale. Ces messages d'erreur sont critiques pour que cette configuration fonctionne correctement.

**En résumé** : Utilisez eth-lightwallet avec cette version de ethjs-provider-signer : [https://github.com/ethjs/ethjs-provider-signer/pull/3](https://github.com/ethjs/ethjs-provider-signer/pull/3) pour gagner du temps sur les essais et erreurs.

### **Stockage hors ligne chiffré**

L'objet JSON du coffre-fort keystore de lightwallet est chiffré, et il nécessite de notre part un `passwordProvider` externe pour garder la clé de chiffrement en sécurité. L'objet keystrore est toujours chiffré. L'application est responsable de la garde sécurisée du mot de passe et le fournit avec toute action.

eth-hot-wallet utilise [Store.js](https://github.com/marcuswestin/store.js) — _Stockage multi-navigateurs pour tous les cas d'utilisation, utilisé sur le web_. Store.js nous permet de stocker facilement le keystore chiffré et de l'extraire du stockage lorsque la page web est consultée.

Lorsque le portefeuille est chargé pour la première fois, il vérifie s'il y a un keystore dans le stockage local et le charge automatiquement dans l'état Redux si c'est le cas.

À ce stade, nous pouvons lire les données publiques du keystore mais pas les clés. Pour afficher les données publiques avant que l'utilisateur ne saisisse le mot de passe de chiffrement, nous avons besoin d'un mode de fonctionnement supplémentaire : **chargé et verrouillé**. Dans ce mode, le portefeuille affichera les adresses et récupérera les soldes mais ne pourra pas effectuer d'opérations telles que l'envoi de transactions ou même la génération de nouvelles adresses. Le déclenchement de l'une de ces actions demandera le mot de passe de l'utilisateur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QICvgsfhKmpOSVMMgWbo4A.png)
_portefeuille verrouillé après le chargement depuis le stockage local_

### Envoyer de l'Ethereum en utilisant Web3.js

Lorsque l'on utilise Web3.js@0.2.x, la fonction `sendTransaction` est fournie sous la forme suivante :

`web3.eth.sendTransaction(transactionObject [, callback])`

Le callback retournera la TX comme résultat en cas de succès.

Cependant, pour l'intégrer correctement dans notre flux saga.js, nous devons envelopper la [fonction sendTransaction](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/containers/Header/saga.js#L203) [avec une promesse](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/containers/Header/saga.js#L203) :

De cette manière, nous continuons l'exécution régulière de Saga.js après que `sendTransaction` est appelé.

### Envoyer des tokens erc20 en utilisant Web3.js

La blockchain Ethereum ne fournit pas de primitives qui encapsulent la fonctionnalité des tokens, et elle ne devrait pas le faire. Chaque token déployé sur Ethereum est, en fait, un programme qui correspond à la [**spécification eip20**](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-20.md). Puisque la machine virtuelle Ethereum (EVM) est Turing complète (avec certaines restrictions), chaque token peut avoir une implémentation différente (même pour la même fonctionnalité). Ce qui unifie tous ces programmes sous le terme "token" est qu'ils fournissent la même API telle que définie par la spécification.

**Lorsque nous envoyons un token sur Ethereum, nous interagissons avec un contrat intelligent.** Pour communiquer avec un contrat intelligent, nous devons connaître son API, le format de partage de l'API du contrat appelé [Ethereum Contract ABI](https://github.com/ethereum/wiki/wiki/Ethereum-Contract-ABI).

Nous allons stocker l'[ABI erc20](https://github.com/PaulLaux/eth-hot-wallet/blob/master/app/utils/contracts/abi.js) comme partie de notre bundle JavaScript et instancier un contrat pendant l'exécution du programme :

`const erc20Contract = web3.eth.contract(erc20Abi);`

Après la configuration du contrat, nous pouvons facilement interagir avec lui de manière programmatique en utilisant l'[API de contrat Web3.js](https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcontract).

Pour chaque token, nous aurons besoin d'une instance de contrat dédiée :

`const tokenContract = erc20Contract.at(tokenContractAddress);`

Après la création de l'instance de contrat, nous pouvons accéder aux fonctions du contrat en appelant la fonction souhaitée directement depuis JavaScript :

Voir [API de contrat Web3.js](https://github.com/ethereum/wiki/wiki/JavaScript-API#web3ethcontract) pour les détails complets.

Nous allons promisifier le `tokenContract.transfer.sendTransaction` pour l'utiliser avec notre flux redux-saga :

Il est possible d'utiliser [es6-promisify](https://github.com/digitaldesignlabs/es6-promisify) ou similaire au lieu d'écrire la promesse directement, mais je préfère l'approche directe dans ce cas.

### S'abonner au cycle de vie des transactions Ethereum en utilisant Web3.js V1 et les canaux redux-saga

_eth-hot-wallet utilise web3.js v0.2.x et ne supporte pas cette fonctionnalité pour le moment_. _L'exemple est fourni par un autre projet. C'est une fonctionnalité importante et devrait être utilisée extensivement._

La nouvelle version de Web3.js (V1.0.0) est livrée avec une [nouvelle API de contrat](https://web3js.readthedocs.io/en/1.0/web3-eth-contract.html#methods-mymethod-send) qui peut nous informer des changements dans le cycle de vie des transactions.

Voici le `PromiEvent` : une [promesse combinée à un émetteur d'événements](https://web3js.readthedocs.io/en/1.0/callbacks-promises-events.html#promievent).

```
web3.eth.sendTransaction({...}).once('transactionHash', function(hash){ ... }).once('receipt', function(receipt){ ... }).on('confirmation', function(number, receipt){ ... }).on('error', function(error){ ... }).then(function(receipt){    // déclenché une fois le reçu miné});
```

`web3.eth.sendTransaction()` retournera un objet (une promesse) qui se résoudra une fois la transaction minée. Le même objet nous permettra de nous abonner aux événements `'transactionHash'`, `'receipt'`, `'confirmation'` et `'error'`.

**Cette API est bien plus informative et élégante que celle fournie avec la version 0.2.x de Web3.js**. Nous verrons comment nous pouvons l'intégrer dans notre application web avec l'aide des [canaux Saga.js](https://redux-saga.js.org/docs/advanced/Channels.html). La motivation est de mettre à jour l'état de l'application (store Redux) une fois qu'un changement dans l'état de la transaction est détecté.

Dans l'exemple suivant, nous allons créer une transaction 'commit' vers un contrat intelligent arbitraire et mettre à jour l'état de l'application lorsque nous recevons les événements `'transactionHash'`, `'receipt'` et `'error'`.

Nous devons initialiser le nouveau canal et bifurquer un gestionnaire :

Le gestionnaire attrapera tous les événements du canal et appellera le créateur d'action Redux approprié.

Une fois le canal et le gestionnaire prêts et que l'utilisateur initie la transaction, nous devons nous enregistrer aux événements générés :

En fait, nous n'avons pas besoin d'un nouveau canal pour chaque transaction et pouvons **utiliser le même canal pour tous les types de transactions.**

[Le code source complet de cet exemple](https://github.com/Monetary-Foundation/PreDistribution-DApp/blob/1003631ad6a7ca53e6ed02772f6fec6a36b7628c/app/containers/Dashboard/saga.js#L412) peut être trouvé ici.

### Interroger la blockchain Ethereum et les données de prix en utilisant redux-saga

Il existe plusieurs façons de surveiller les changements de la blockchain. Il est possible d'utiliser Web3.js pour [s'abonner aux événements](https://web3js.readthedocs.io/en/1.0/web3-eth-subscribe.html) ou nous pouvons interroger la blockchain nous-mêmes et avoir plus de contrôle sur certains aspects de l'interrogation.

Dans eth-hot-wallet, le portefeuille interroge périodiquement la blockchain pour les changements de solde et l'[API Coinmarketcap](https://api.coinmarketcap.com/v1/ticker/?convert=EUR) pour les changements de prix.

Ce modèle redux-saga nous permettra d'interroger n'importe quelle source de données ou API :

Après que l'action `CHECK_BALANCES` est vue par la saga par défaut, la fonction `checkAllBalances` est appelée. Elle peut se terminer par l'un des deux résultats possibles : `CHECK_BALANCES_SUCCESS` ou `CHECK_BALANCES_ERROR`. Chacun d'eux sera attrapé par `watchPollData()` pour attendre X secondes et appeler `checkAllBalance` à nouveau. Cette routine se poursuivra jusqu'à ce que `STOP_POLL_BALANCES` soit attrapé par `watchPollData`. Après cela, il est possible de reprendre l'interrogation en soumettant à nouveau l'action `CHECK_BALANCES`.

### Surveiller la taille du bundle

Lorsque l'on construit des applications web en utilisant JavaScript et npm, il peut être tentant d'ajouter de nouveaux packages sans analyser l'augmentation de l'empreinte. Eth-hot-wallet utilise [webpack-monitor](http://webpackmonitor.com/) pour afficher un graphique de toutes les dépendances et **les différences entre chaque build**. Il permet au développeur de voir clairement le changement de taille du bundle après chaque nouveau package ajouté.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x_Mis7ppLuj5_Q_ifDCOZQ.jpeg)
_exemple de graphique webpack-monitor_

Webpack monitor peut également aider à trouver les dépendances les plus exigeantes et peut même surprendre le développeur en **mettant en évidence les dépendances qui font peu pour l'application mais contribuent beaucoup à la taille du bundle.**

Webpack-monitor est facile à intégrer et vaut définitivement la peine d'être inclus dans toute application web basée sur webpack.

### Conclusion

Les problèmes présentés dans cet article ne sont qu'une partie des défis qui doivent être résolus lors de la création d'un portefeuille Ethereum. Cependant, surmonter ces problèmes créera une base solide et nous permettra de continuer et de créer un portefeuille réussi.

La création d'un portefeuille peut également être une excellente introduction au monde d'Ethereum, puisque la plupart des [applications décentralisées](https://github.com/ethereum/wiki/wiki/Decentralized-apps-(dapps)) (DApps) nécessitent un ensemble similaire de capacités, à la fois du point de vue du front-end et de la blockchain.

[**ETH Hot Wallet - Portefeuille Ethereum avec support ERC20**](https://eth-hot-wallet.com)
[_ETH Hot wallet est un portefeuille Ethereum avec support ERC20. Les clés sont générées à l'intérieur du navigateur et jamais envoyées... eth-hot-wallet.com](https://eth-hot-wallet.com)

En cas de questions concernant eth-hot-wallet ou tout sujet connexe, n'hésitez pas à me contacter via [Twitter](https://twitter.com/dr_laux) ou à ouvrir un [problème sur GitHub](https://github.com/PaulLaux/eth-hot-wallet).