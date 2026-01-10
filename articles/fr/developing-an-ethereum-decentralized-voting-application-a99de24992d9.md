---
title: Un guide pour développer une application de vote décentralisée sur Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-07T10:24:20.000Z'
originalURL: https://freecodecamp.org/news/developing-an-ethereum-decentralized-voting-application-a99de24992d9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cQl1eHoplkcQF2dTaWo5FA.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: Web Development
  slug: web-development
seo_title: Un guide pour développer une application de vote décentralisée sur Ethereum
seo_desc: 'By Timothy Ko

  After the entire cryptocurrency market passed 700 billion dollars in market cap,
  the cryptocurrency space exploded over these last couple months. But this is just
  the beginning. As blockchain systems continue to evolve and scale, one gr...'
---

Par Timothy Ko

Après que l'ensemble du marché des cryptomonnaies a dépassé 700 milliards de dollars en capitalisation boursière, l'espace des cryptomonnaies a explosé au cours de ces derniers mois. Mais ce n'est que le début. Alors que les systèmes de blockchain continuent d'évoluer et de se développer, une excellente façon de s'immerger dans cet espace et de tirer parti de cette technologie est avec les applications décentralisées, autrement connues sous le nom de dApps.

[CryptoKitties](https://www.cryptokitties.co/), célèbre pour sa congestion de la blockchain Ethereum, est un excellent exemple de dApp, combinant de manière unique les concepts de chats élevables et collectionnables avec la blockchain. Ce jeu sensationnel n'est qu'un exemple créatif parmi un nombre virtuellement illimité d'opportunités.

Bien que cela semble très compliqué, certains frameworks et outils ont été développés pour abstraire vos interactions avec la blockchain et les contrats intelligents. Dans cet article de blog, je vais passer en revue une façon de créer une application de vote décentralisée sur Ethereum. Je vais brièvement passer en revue Ethereum, mais vous devriez probablement avoir une compréhension de celui-ci pour utiliser ce guide au maximum. De plus, je m'attends à ce que vous connaissiez Javascript.

### Pourquoi créer une application de vote décentralisée ?

Essentiellement, une grande application décentralisée utilisant la technologie blockchain vous permet d'effectuer les mêmes actions que vous feriez aujourd'hui (comme transférer de l'argent) sans tiers de confiance. Les meilleures dApps ont un cas d'utilisation spécifique dans le monde réel qui tire parti des caractéristiques uniques de la blockchain.

> En essence, la blockchain est un registre partagé, programmable, cryptographiquement sécurisé et donc de confiance, qu'aucun utilisateur unique ne contrôle et qui peut être inspecté par quiconque. - Klaus Schwab

Même si une application de vote pourrait ne pas être une grande application pour les consommateurs, j'ai choisi de l'utiliser pour ce guide parce que les principaux problèmes que la blockchain résout — transparence, sécurité, accessibilité, auditabilité — sont les principaux problèmes qui affligent les élections démocratiques actuelles.

Puisqu'une blockchain est un registre permanent des transactions (votes) qui sont distribuées, chaque vote peut être retracé de manière irréfutable exactement quand et où il a eu lieu sans révéler l'identité de l'électeur. De plus, les votes passés ne peuvent pas être changés, tandis que le présent ne peut pas être piraté, car chaque transaction est vérifiée par chaque nœud du réseau. Et tout attaquant extérieur ou intérieur doit avoir le contrôle de 51 % des nœuds pour altérer le registre.

Même si l'attaquant était capable de réaliser cela tout en entrant incorrectement les votes des utilisateurs avec leurs vraies identités sous le radar, les systèmes de vote de bout en bout pourraient permettre aux électeurs de vérifier si leur vote a été correctement enregistré dans le système, rendant le système extrêmement sûr.

### Composants principaux d'Ethereum

Je m'attends à ce que vous ayez une compréhension de [Blockchain](https://www.coindesk.com/information/what-is-blockchain-technology/) et [Ethereum](https://www.ethereum.org/) pour le reste de ce guide. [Voici](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369) un guide génial à ce sujet, et j'ai écrit un bref aperçu des composants principaux que je souhaite que vous connaissiez.

1. **Les contrats intelligents** agissent comme la logique et le stockage back-end. Un contrat est écrit en [Solidity](http://solidity.readthedocs.io/en/develop/solidity-in-depth.html), un langage de contrat intelligent, et est une collection de code et de données qui réside à une adresse spécifique sur la blockchain Ethereum. C'est très similaire à une classe en programmation orientée objet, où il inclut des fonctions et des variables d'état. Les contrats intelligents, ainsi que la blockchain, sont la base de toutes les applications décentralisées. Ils sont, comme la blockchain, immuables et distribués, ce qui signifie que les mettre à niveau sera un casse-tête s'ils sont déjà sur le réseau Ethereum. Heureusement, [voici](https://consensys.github.io/smart-contract-best-practices/software_engineering/) quelques façons de le faire.
2. **La machine virtuelle Ethereum (EVM)** gère l'état interne et le calcul de l'ensemble du réseau Ethereum. Pensez à l'EVM comme à cet énorme ordinateur décentralisé qui contient des "adresses" capables d'exécuter du code, de changer des données et d'interagir les unes avec les autres.
3. [**Web3.js**](https://github.com/ethereum/wiki/wiki/JavaScript-API) est une API Javascript qui vous permet d'interagir avec la blockchain, y compris faire des transactions et des appels aux contrats intelligents. Cette API abstrait la communication avec les clients Ethereum, permettant aux développeurs de se concentrer sur le contenu de leur application. Vous devez avoir une instance web3 intégrée dans votre navigateur pour le faire.

### Autres outils que nous utiliserons

1. [**Truffle**](http://truffleframework.com/docs/) est un framework de développement et de test populaire pour Ethereum. Il inclut une blockchain de développement, des scripts de compilation et de migration pour déployer votre contrat sur la blockchain, des tests de contrat, et ainsi de suite. Il facilite le développement !
2. [**Truffle Contracts**](https://github.com/trufflesuite/truffle-contract) est une abstraction au-dessus de l'API Javascript Web3, vous permettant de vous connecter et d'interagir facilement avec votre contrat intelligent.
3. [**Metamask**](https://metamask.io/) apporte Ethereum à votre navigateur. C'est une extension de navigateur qui fournit une instance web3 sécurisée liée à votre adresse Ethereum, vous permettant d'utiliser des applications décentralisées. Nous n'utiliserons pas Metamask dans ce tutoriel, mais c'est un moyen pour les gens d'interagir avec votre DApp en production. Au lieu de cela, nous injecterons notre propre instance web3 pendant le développement. Pour plus d'informations, consultez [ce](http://truffleframework.com/docs/advanced/truffle-with-metamask) lien.

### Commençons !

Pour simplifier, nous ne construirons pas vraiment le système de vote complet que j'ai décrit précédemment. Pour faciliter l'explication, ce sera simplement une application d'une seule page où un utilisateur peut entrer son identifiant et voter pour un candidat. Il y aura également un bouton qui compte et affiche le nombre de votes par candidat.

De cette façon, nous pourrons nous concentrer sur le processus de création et d'interaction avec les contrats intelligents au sein d'une application. Le code source de cette application entière sera dans [ce dépôt](https://github.com/tko22/eth-voting-dapp), et vous devrez avoir Node.js et npm installés.

Tout d'abord, installons Truffle globalement.

```
npm install -g truffle
```

Pour utiliser les commandes Truffle, vous devez les exécuter dans un projet existant.

```
git clone https://github.com/tko22/truffle-webpack-boilerplatecd truffle-webpack-boilerplatenpm install
```

Ce dépôt est simplement un squelette d'une Truffle Box, qui sont des modèles ou des applications exemples que vous pouvez obtenir en une commande — `truffle unbox [nom de la boîte]`. Cependant, la Truffle box avec webpack n'est pas mise à jour avec les dernières versions et inclut une application exemple. Ainsi, j'ai créé ce [dépôt](https://github.com/tko22/truffle-webpack-boilerplate) (celui lié dans les instructions ci-dessus).

#### 2. Structure du répertoire

Votre structure de répertoire devrait inclure ces éléments :

* `contracts/` — Dossier contenant tous les contrats. **NE SUPPRIMEZ PAS** `Migrations.sol`
* `migrations/` — Dossier contenant les [fichiers de migration](http://truffleframework.com/docs/getting_started/migrations), qui vous aident à déployer vos contrats intelligents sur la blockchain.
* `src/` — contient les fichiers HTML/CSS et Javascript pour l'application
* `truffle.js` — Fichier de configuration Truffle
* `build/` — Vous ne verrez pas ce dossier jusqu'à ce que vous compiliez vos contrats. Ce dossier contient les artefacts de construction, alors ne modifiez aucun de ces fichiers ! Les artefacts de construction décrivent la fonction et l'architecture de votre contrat et donnent à Truffle Contracts et web3 des informations sur la façon d'interagir avec votre contrat intelligent sur la blockchain.

### 1. Écrivez vos contrats intelligents

Assez avec la configuration et l'introduction. Plongeons dans le code ! Tout d'abord, nous allons écrire notre contrat intelligent, qui est écrit en [Solidity](http://solidity.readthedocs.io/en/develop/index.html) (les autres langages ne sont pas aussi populaires). Cela peut sembler effrayant, mais ce n'est pas le cas.

Pour toute application, **vous voulez que vos contrats intelligents soient aussi simples que possible, même stupidement simples.** N'oubliez pas que vous devez payer pour chaque calcul/transaction que vous effectuez, et vos contrats intelligents seront sur la blockchain **pour toujours.** Donc, vous voulez vraiment qu'ils fonctionnent parfaitement — ce qui signifie que plus ils sont complexes, plus il est facile de faire une erreur.

Notre contrat inclura :

1. **Variables d'état** — variables qui contiennent des valeurs qui sont stockées en permanence sur la blockchain. Nous utiliserons des variables d'état pour contenir une liste et un nombre d'électeurs et de candidats.
2. [**Fonctions**](http://solidity.readthedocs.io/en/develop/contracts.html#functions) — Les fonctions sont les exécutables des contrats intelligents. Ce sont elles que nous appellerons pour interagir avec la blockchain, et elles ont différents niveaux de visibilité, en interne et en externe. Gardez à l'esprit que chaque fois que vous voulez changer la valeur/état d'une variable, une transaction doit se produire — coûtant de l'Ether. Vous pouvez également faire des `appels` à la blockchain, qui ne coûteront pas d'Ether car les changements que vous avez apportés seront détruits (plus sur cela dans la section 3 lorsque nous ferons réellement les `transactions` et les `appels`).
3. [**Événements**](http://solidity.readthedocs.io/en/develop/contracts.html#events) — Chaque fois qu'un événement est appelé, la valeur passée dans l'événement sera enregistrée dans le journal de la transaction. Cela permet aux fonctions de rappel Javascript ou aux promesses résolues de voir la valeur certaine que vous vouliez passer après une transaction. C'est parce que chaque fois que vous faites une transaction, un journal de transaction sera retourné. Nous utiliserons un événement pour enregistrer l'ID du candidat nouvellement créé, que nous afficherons (vérifiez le premier point de la section 3).
4. [**Types de structures**](http://solidity.readthedocs.io/en/develop/types.html#structs) — Cela est très similaire à une structure C. Les structures vous permettent de contenir plusieurs variables, et sont géniales pour les choses avec plusieurs attributs. Les `Candidats` n'auront que leur nom et leur parti, mais vous pouvez définitivement ajouter plus d'attributs.
5. **Mappages** — Pensez à ceux-ci comme des tables de hachage ou des dictionnaires, où il y a une paire clé-valeur. Nous utiliserons deux mappages.

Il y a quelques autres types qui ne sont pas listés ici, mais certains d'entre eux sont un peu plus compliqués. Ces cinq types couvrent de nombreuses structures qu'un contrat intelligent utilisera généralement. Ces types sont expliqués plus en profondeur [ici](http://solidity.readthedocs.io/en/develop/structure-of-a-contract.html#).

Pour référence, voici le code du contrat intelligent. Notez que ce fichier devrait s'appeler `Voting.sol` mais je voulais que le gist Github ait un style, alors je lui ai donné une extension `.js`. Comme le reste de ce guide, je fournirai des commentaires dans le code qui expliqueront ce qu'il fait, et j'expliquerai la vue d'ensemble ensuite tout en pointant certaines mises en garde et logique.

En gros, nous avons deux structures (types qui contiennent plusieurs variables) qui décrivent un électeur et un candidat. Avec les structures, nous sommes capables de leur assigner plusieurs propriétés, comme des emails, des adresses, etc.

Pour garder une trace des électeurs et des candidats, nous les mettons dans des mappages séparés où ils sont indexés par des entiers. **L'index/clé d'un candidat ou d'un électeur — appelons-le ID — est le seul moyen pour les fonctions d'y accéder.**

Nous gardons également une trace du nombre d'électeurs et de candidats, ce qui nous aidera à les indexer. De plus, n'oubliez pas l'événement à la ligne 8, qui enregistrera l'ID du candidat lorsqu'il sera ajouté. Cet événement sera utilisé par notre interface, puisque nous devons garder une trace de l'ID d'un candidat afin de voter pour un candidat.

1. Je sais, contrairement à ce que j'ai dit plus tôt sur la simplification des contrats, j'ai rendu ce contrat un peu plus compliqué par rapport à ce que cette application fait réellement. Cependant, je l'ai fait pour qu'il soit beaucoup plus facile pour vous de faire des modifications et d'ajouter des fonctionnalités à cette application par la suite (plus sur cela à la fin). Si vous souhaitez créer une application de vote encore plus simple, le contrat intelligent pourrait fonctionner en moins de 15 lignes de code.
2. Notez que les variables d'état `numCandidates` et `numVoters` ne sont pas déclarées publiques. Par [défaut](http://solidity.readthedocs.io/en/develop/contracts.html#visibility-and-getters), ces variables ont une visibilité `interne`, ce qui signifie qu'elles ne peuvent être directement accessibles que par le contrat actuel ou les contrats dérivés (ne vous inquiétez pas, nous ne l'utiliserons pas).
3. Nous utilisons `32bytes` pour les chaînes de caractères au lieu d'utiliser le type `string`. Notre [EVM a une taille de mot de 32 octets](https://ethereum.stackexchange.com/q/2327/42), donc elle est "optimisée" pour traiter les données en blocs de 32 octets. (Les compilateurs, comme Solidity, doivent faire plus de travail et générer plus de bytecode lorsque les données ne sont pas en blocs de 32 octets, ce qui entraîne effectivement un coût de gaz plus élevé.)
4. Lorsqu'un utilisateur vote, une nouvelle structure `Voter` est créée et ajoutée au mappage. Pour compter le nombre de votes qu'un certain candidat a, vous devez parcourir tous les électeurs et compter le nombre de votes. Les candidats fonctionnent selon le même comportement. **Ainsi, ces mappages conserveront l'historique de tous les candidats et électeurs.**

### 2. Instancier web3 et les contrats

Avec notre contrat intelligent terminé, nous devons maintenant exécuter notre blockchain de test et déployer ce contrat sur la blockchain. Nous aurons également besoin d'un moyen de communiquer avec lui, ce qui se fera via web3.js.

Avant de démarrer notre blockchain de test, nous devons créer un fichier appelé `2_deploy_contracts.js` à l'intérieur du dossier `/contracts` qui lui indique d'inclure votre contrat intelligent de vote lorsque vous migrez.

Pour démarrer la blockchain de développement Ethereum, allez dans votre ligne de commande et exécutez :

```
truffle develop
```

Cela restera sur votre ligne de commande. Comme Solidity est un langage compilé, nous devons d'abord le compiler en bytecode pour que l'EVM l'exécute.

```
compile
```

Vous devriez maintenant voir un dossier `build/` dans votre répertoire. Ce dossier contient les artefacts de construction, qui sont critiques pour le fonctionnement interne de Truffle, alors ne les touchez pas !

Ensuite, nous devons migrer le contrat. [Migrations](http://truffleframework.com/docs/getting_started/migrations) est un script Truffle qui vous aide à modifier l'état du contrat de votre application au fur et à mesure que vous développez. N'oubliez pas que votre contrat est déployé à une certaine adresse sur la blockchain, donc chaque fois que vous apportez des modifications, votre contrat sera situé à une adresse différente. Les migrations vous aident à faire cela et vous aident également à déplacer des données.

```
migrate
```

Félicitations ! Votre contrat intelligent est maintenant sur la blockchain pour toujours. Eh bien, pas vraiment... parce que `truffle develop` se rafraîchit chaque fois que vous l'arrêtez.

Si vous souhaitez avoir une blockchain persistante, envisagez [Ganache](http://truffleframework.com/ganache/), qui est également développé par Truffle. Si vous utilisez Ganache, vous n'aurez pas besoin d'appeler `truffle develop`. Au lieu de cela, vous exécuterez `truffle compile` et `truffle migrate`. Pour comprendre ce qu'il faut vraiment pour déployer un contrat sans Truffle, consultez cet [article de blog](https://medium.com/@gus_tavo_guim/deploying-a-smart-contract-the-hard-way-8aae778d4f2a).

Une fois que nous avons déployé le contrat intelligent sur la blockchain, nous devrons configurer une instance web3.0 avec Javascript sur le navigateur chaque fois que l'application démarre. Ainsi, le prochain morceau de code sera placé en bas de `js/app.js`. Notez que nous utilisons la version 0.20.1 de web3.0.

Vous n'avez pas vraiment à vous soucier si vous ne comprenez pas ce code. Sachez simplement que cela sera exécuté lorsque l'application démarrera et vérifiera s'il y a déjà une instance web3 (Metamask) dans votre navigateur. Si ce n'est pas le cas, nous en créerons simplement une qui communique avec `localhost:9545`, qui est la blockchain de développement Truffle.

Si vous utilisez Ganache, vous devez changer le port en `7545`. Une fois une instance créée, nous appellerons la fonction `start` (je la définirai dans la prochaine section).

### 3. Ajouter des fonctionnalités

La dernière chose que nous devrons faire est d'écrire l'interface pour l'application. Cela implique les essentiels pour toute application web — HTML, CSS et Javascript (nous avons déjà écrit un peu de Javascript avec la création d'une instance web3). Tout d'abord, créons notre fichier HTML.

C'est une page très simple, avec un formulaire d'entrée pour l'ID de l'utilisateur, et des boutons pour voter et compter les votes. Lorsque ces boutons sont cliqués, ils appelleront des fonctions spécifiques qui votent, et trouveront le nombre de votes pour les candidats.

Il y a trois éléments div importants cependant, avec les ids : `candidate-box`, `msg`, et `vote-box`, qui contiendront des cases à cocher pour chaque candidat, un message, et le nombre de votes, respectivement. Nous importons également JQuery, Bootstrap, et `app.js`.

Maintenant, nous devons simplement interagir avec le contrat et implémenter les fonctions pour voter et compter le nombre de votes pour chaque candidat. JQuery manipulera le DOM, et nous utiliserons des promesses lorsque nous ferons des transactions ou des appels à la blockchain. Voici le code pour `app.js`.

Notez que le code que j'ai fourni dans l'étape précédente pour créer une instance web3 est également ici. Tout d'abord, nous importons les bibliothèques nécessaires et les éléments webpack, y compris web3 et [Truffle Contracts](https://github.com/trufflesuite/truffle-contract). Nous utiliserons Truffle Contracts, qui est construit sur web3 pour interagir avec la blockchain.

Pour l'utiliser, nous récupérerons les artefacts de construction qui ont été automatiquement construits lorsque nous avons compilé le contrat intelligent de vote et les utiliserons pour créer le contrat Truffle. Enfin, nous configurerons les fonctions dans la variable globale `window` pour démarrer l'application, voter pour un candidat et trouver le nombre de votes.

Pour interagir réellement avec la blockchain, nous devons créer une instance du contrat Truffle en utilisant la fonction `deployed`. Cela, à son tour, retournera une promesse avec l'instance comme valeur de retour que vous utiliserez pour appeler des fonctions à partir du contrat intelligent.

Il y a deux façons d'interagir avec ces fonctions : les transactions et les appels. **Une transaction est une opération d'écriture, et elle sera diffusée à l'ensemble du réseau et traitée par les mineurs (et donc, coûte de l'Ether).** Vous devez effectuer une transaction si vous changez une variable d'état, car elle changera l'état de la blockchain.

**Un appel est une opération de lecture, simulant une transaction mais rejetant le changement d'état. Ainsi, il ne coûtera pas d'Ether.** C'est génial pour appeler des fonctions getter (vérifiez les quatre fonctions getter que nous avons écrites précédemment dans notre contrat intelligent).

Pour faire une transaction avec Truffle Contracts, vous écrivez `instance.functionName(param1, param2)`, avec `instance` comme l'instance qui a été retournée par la fonction `deployed` (Vérifiez la ligne 36 pour un exemple). Cette transaction retournera une promesse avec les données de transaction comme valeur de retour. Ainsi, si vous retournez une valeur dans votre fonction de contrat intelligent mais que vous effectuez une transaction avec cette même fonction, elle ne retournera pas cette valeur.

C'est pourquoi nous avons un événement qui enregistrera ce que vous voulez qu'il écrive dans les données de transaction qui seront retournées. Dans le cas des lignes 36-37, nous faisons une transaction pour ajouter un candidat. Lorsque nous résolvons la promesse, nous avons les données de transaction dans `result`.

Pour obtenir le `candidateID` que nous avons enregistré avec l'événement `AddedCandidate()` (vérifiez le contrat intelligent pour le voir 0), nous devons passer par les journaux et le récupérer comme ceci : `result.logs[0].args.candidateID`.

Pour vraiment voir ce qui se passe, utilisez les outils de développement Chrome pour imprimer le `result` et parcourez sa structure de `result`.

Pour faire un appel, vous écrirez `instance.functionName.call(param1,param2)`. Cependant, si une fonction a le mot-clé `view`, alors Truffle Contracts créera automatiquement un appel et ainsi vous n'avez pas besoin d'ajouter le `.call`.

C'est pourquoi nos fonctions getter ont le mot-clé `view`. Contrairement à une transaction, la promesse retournée d'un appel aura une valeur de retour de ce qui est retourné par la fonction du contrat intelligent.

Je vais maintenant expliquer brièvement les 3 fonctions, mais cela devrait être très familier si vous avez construit des applications récupérant/modifiant des données à partir d'un magasin de données et manipulant le DOM en conséquence. Pensez à la blockchain comme à votre base de données, et aux contrats Truffle comme à l'API pour obtenir des données de votre base de données.

#### **App.start()**

Cette fonction est appelée immédiatement après que nous avons créé une instance web3. Pour que Truffle Contracts fonctionne, nous devons définir le fournisseur sur l'instance web3 créée et définir les valeurs par défaut (comme le compte que vous utilisez et la quantité de gaz que vous voulez payer pour faire une transaction).

Puisque nous sommes en mode développement, nous pouvons utiliser n'importe quelle quantité de gaz et n'importe quel compte. En production, nous prendrions le compte fourni par MetaMask et essaierions de déterminer la plus petite quantité de gaz que vous pourriez utiliser, puisque c'est de l'argent réel.

Avec tout configuré, nous allons maintenant afficher les cases à cocher pour chaque candidat pour que l'utilisateur puisse voter. Pour ce faire, nous devons créer une instance du contrat et obtenir les informations du candidat. S'il n'y a pas de candidats, nous les créerons. Pour qu'un utilisateur puisse voter pour un candidat, nous devons fournir l'ID de ce candidat. Ainsi, nous faisons en sorte que chaque élément de case à cocher ait un `id` (attribut d'élément HTML) de l'ID du candidat. De plus, nous ajouterons le nombre de candidats à une variable globale `numOfCandidates`, que nous utiliserons dans `App.findNumOfVotes()`. JQuery est utilisé pour ajouter chaque case à cocher et son nom de candidat à `.candidate-box`.

#### **App.vote()**

Cette fonction votera pour un certain candidat en fonction de la case à cocher cliquée et de son attribut `id`.

Premièrement, nous vérifierons si l'utilisateur a saisi son userID, qui est son identification. S'il ne l'a pas fait, nous affichons un message lui demandant de le faire.

Deuxièmement, nous vérifierons si l'utilisateur vote pour un candidat, en vérifiant s'il y a au moins une case à cocher qui est cochée. Si aucune des cases à cocher n'a été cochée, nous afficherons également un message leur demandant de voter pour un candidat. Si l'une des cases à cocher est cochée, nous récupérerons l'attribut `id` de cette case à cocher, qui est également l'ID du candidat lié, et l'utiliserons pour voter pour le candidat.

Une fois la transaction terminée, nous résoudrons la promesse retournée et afficherons un message "Voted".

#### **App.findNumOfVotes()**

Cette dernière fonction trouvera le nombre de votes pour chaque candidat et les affichera. Nous passerons en revue les candidats et appellerons deux fonctions de contrat intelligent, `getCandidate` et `totalVotes`. Nous résoudrons ces promesses et créerons un élément HTML pour ce candidat.

Maintenant, démarrez l'application et vous la verrez sur `http://localhost:8080/` !

```
npm run dev
```

### Ressources

Je sais, c'est beaucoup... Vous pourriez avoir cet article ouvert pendant un certain temps alors que vous développez lentement cette application et comprenez vraiment ce qui se passe. Mais c'est l'apprentissage ! Veuillez compléter ce guide avec toute la documentation d'Ethereum, Truffle, et ce que j'ai fourni ci-dessous. J'ai essayé de couvrir de nombreux points clés dans cet article, mais ce n'est qu'un bref aperçu et ces ressources aideront beaucoup.

* [**Tout sur Solidity et les contrats intelligents**](http://solidity.readthedocs.io/en/develop/index.html) — Je veux dire Tout
* [**Tout sur Truffle**](http://truffleframework.com/docs/)
* [**Documentation de Truffle Contracts**](https://github.com/trufflesuite/truffle-contract)
* [**API Javascript Web3**](https://github.com/ethereum/wiki/wiki/JavaScript-API) — cela sera génial à connaître et à référencer, mais Truffle Contracts abstrait de nombreuses parties de cela
* [**Modèles de DApp utiles**](https://github.com/ethereum/wiki/wiki/Useful-%C3%90app-Patterns)
* [**Documentation Ethereum**](https://github.com/ethereum/wiki/wiki/Ethereum-introduction) — regardez la barre latérale et il y a plein de choses
* [**Explication du code de CryptoKitties**](https://medium.com/loom-network/how-to-code-your-own-cryptokitties-style-game-on-ethereum-7c8ac86a4eb3) — L'auteur passe en revue les parties importantes du contrat intelligent de CryptoKitties
* [**Meilleures pratiques pour les contrats intelligents**](https://consensys.github.io/smart-contract-best-practices/) — une lecture incontournable

### Conclusion

Construire des applications sur Ethereum est assez similaire à une application régulière appelant un service backend. La partie la plus difficile est d'écrire un contrat intelligent robuste et complet. J'espère que ce guide vous a aidé à comprendre les connaissances de base des applications décentralisées et d'Ethereum et vous aidera à démarrer votre intérêt pour les développer.

Si vous souhaitez construire sur ce que nous avons construit, voici quelques idées. J'ai en fait écrit le contrat intelligent de manière à ce qu'il soit facilement implémenté avec tout ce que je vous ai donné dans ce guide.

* **Afficher le parti de chaque candidat.** Nous obtenons déjà le parti d'un candidat lorsque nous exécutons `getCandidate(id)`.
* **Vérifier si l'ID saisi par l'utilisateur est unique.**
* **Demander et stocker plus d'informations sur un utilisateur**, comme sa date de naissance et son adresse domicile.
* **Ajouter une option pour voir si une personne avec un ID spécifique a voté ou non.** Vous créeriez un nouveau formulaire pour entrer un ID, que vous rechercheriez ensuite pour cet utilisateur spécifique dans la blockchain.
* **Écrire une nouvelle fonction de contrat intelligent qui compte les votes pour les DEUX candidats à la fois.** Actuellement, nous devons faire deux appels séparés pour deux candidats, nécessitant que le contrat parcourt tous les utilisateurs deux fois.
* **Permettre l'ajout de nouveaux candidats.** Cela signifie ajouter un nouveau formulaire pour ajouter des candidats, mais aussi changer un peu la façon dont nous affichons et votons pour les candidats dans le frontend.
* **Exiger que les utilisateurs aient une adresse Ethereum pour voter.** Ma logique pour ne pas inclure les adresses des utilisateurs est que les électeurs ne seraient pas censés avoir Ethereum pour participer à ce processus de vote. Cependant, de nombreuses DApps nécessiteront que les utilisateurs aient une adresse Ethereum.

De plus, voici quelques conseils qui pourraient prévenir certains obstacles :

* Vérifiez deux et trois fois vos fonctions de contrat intelligent lorsque quelque chose d'étrange se produit. J'ai passé quelques heures sur un bug pour découvrir que j'avais retourné la mauvaise valeur dans l'une de mes fonctions.
* Vérifiez si votre URL et votre port sont corrects lorsque vous vous connectez à votre blockchain de développement. Souvenez-vous : `7545` est pour `truffle develop` et `9545` est pour Ganache. Ce sont des **valeurs par défaut**, donc si vous ne pouvez pas vous connecter à votre blockchain, vous les avez peut-être changées.
* Je n'ai pas abordé cela car ce guide aurait été trop long et je ferai probablement un autre article sur ce sujet — mais vous devriez [tester](http://truffleframework.com/docs/getting_started/testing) vos contrats ! Cela aidera beaucoup.
* Si vous n'êtes pas familier avec les [promesses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), passez en revue leur fonctionnement et comment les utiliser. Truffle Contracts utilise des promesses et la version bêta de web3 supportera également les promesses. Elles peuvent, si vous les utilisez mal, fausser beaucoup des données que vous récupérez.

À la vôtre pour travailler vers un internet décentralisé et sécurisé — Web 3.0 !

*J'espère que vous avez apprécié la lecture de ce guide autant que j'ai apprécié l'écrire ! Si vous avez des pensées et des commentaires, n'hésitez pas à laisser un commentaire ci-dessous ou à m'envoyer un email à tk2@illinois.edu ou [tweeter](https://twitter.com/timmykko6) (je viens d'en créer un récemment) ! N'hésitez pas à utiliser mon code et à le partager avec vos amis !*