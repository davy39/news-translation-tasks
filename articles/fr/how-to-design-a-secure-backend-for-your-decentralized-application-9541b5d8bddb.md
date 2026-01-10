---
title: 'Architecture des Applications Décentralisées : Back End, Sécurité et Modèles
  de Conception'
subtitle: ''
author: Nikita Savchenko
co_authors: []
series: null
date: '2019-04-02T15:51:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-design-a-secure-backend-for-your-decentralized-application-9541b5d8bddb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sd62aH6GGS1RoCR9t4QNyQ.png
tags:
- name: Blockchain
  slug: blockchain
- name: crypto
  slug: crypto
- name: Ethereum
  slug: ethereum
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: 'Architecture des Applications Décentralisées : Back End, Sécurité et Modèles
  de Conception'
seo_desc: Decentralized applications, or ÐApps, require a special system design to
  achieve high security and reliability. In this article I am going to cover several
  main principles of how to properly design and implement back end and smart contracts
  for decen...
---

[Applications décentralisées](https://en.wikipedia.org/wiki/Decentralized_application), ou ÐApps, nécessitent une conception système spéciale pour atteindre une sécurité et une fiabilité élevées. Dans cet article, je vais couvrir plusieurs principes principaux sur la manière de concevoir et d'implémenter correctement le back end et les contrats intelligents pour les applications décentralisées, en prenant [Ethereum](https://www.ethereum.org/) comme exemple principal, bien que beaucoup de ces principes s'appliquent également à [EOS](https://eos.io/), [Tron](https://tron.network/) et d'autres plateformes de données décentralisées.

**Points forts de l'article** :

* Comment stocker les clés privées sur le back end sans préoccupations de sécurité
* Comment concevoir correctement les contrats intelligents et quoi « décentraliser »
* Exemples d'architecture d'applications décentralisées et semi-centralisées
* Comment gérer les aspects de bas niveau comme la charge du réseau et les pannes

Ce sera long, commençons !

### Programmes Décentralisés et Blockchain

Malgré le fait que la blockchain soit confrontée à de nombreuses difficultés d'adoption et de régulation aujourd'hui, c'est une technologie qui est là pour rester, qu'il s'agisse de la blockchain, de [hashgraph](https://en.wikipedia.org/wiki/Hashgraph), de [tempo](https://www.radixdlt.com/) ou de toute autre technologie de registre distribué encore à venir, indépendamment de l'algorithme.

> La principale valeur que la blockchain et d'autres technologies similaires apportent peut être généralisée comme suit : elles permettent aux gens d'écrire et d'exécuter des programmes qui, pratiquement, ne peuvent pas être modifiés après leur création ni altérés pendant leur exécution. En d'autres termes, ces programmes s'exécutent toujours comme prévu, et aucune partie unique ne peut influencer leur comportement.

Cette définition est valable pour _de nombreuses_ cryptomonnaies qui existent aujourd'hui si nous les considérons comme des programmes qui définissent comment les pièces peuvent être transférées d'un côté à l'autre. Cela explique également pourquoi les cryptomonnaies et de nombreux types de jetons ont une valeur réelle : ils ne peuvent pas être générés à partir de rien, selon leurs programmes « sous-jacents » définis.

Les plateformes Ethereum/EOS/Tron/…, contrairement à Bitcoin, implémentent une couche de programme plus complexe, qui à son tour implémente l'environnement d'exécution permettant à quiconque d'écrire ses propres programmes décentralisés sur la plateforme. Ces programmes définis par l'utilisateur s'exécutent toujours comme prévu, sans aucune exception, et leur sécurité est garantie par la plateforme.

### Applications Décentralisées

Ces programmes sécurisés et immuables s'exécutant sur un réseau décentralisé en combinaison avec les technologies traditionnelles de front-end et de back-end sont ce que nous appelons **applications décentralisées** (ÐApps) aujourd'hui. Bien que certaines d'entre elles puissent être semi-centralisées, une grande partie des activités dans une application véritablement décentralisée doit se dérouler hors du contrôle d'une partie centrale.

![Image](https://cdn-media-1.freecodecamp.org/images/a0d9mC2p5qPHjMfIXw8Oq0XHCy9CQdLOAWmG)
*Si quelqu'un me demandait de dessiner comment les DApps fonctionnent aujourd'hui, je dessinerais probablement cela*

Pour imaginer ce que nous appelons les applications décentralisées aujourd'hui, prenez n'importe quelle ressource web centralisée existante comme [_YouTube_](https://www.youtube.com/c/NikitaSavchenko) ou [_Instagram_](https://instagram.com/nikitaeverywhere/) comme exemple et imaginez qu'au lieu d'un compte centralisé protégé par mot de passe, vous avez votre « **identité crypto** » liée à la ressource web/mobile.

C'est ce que [Wallet Software](https://metamask.io/) vous fournit. La [clé privée](https://en.wikipedia.org/wiki/Public-key_cryptography) de cette identité (un secret, ayant lequel, vous pouvez agir au nom de cette identité) est stockée sur votre appareil local et ne va jamais en ligne, rendant impossible pour quiconque de contrôler cette identité sauf vous. Avec cette identité, vous pouvez effectuer différentes actions dans les réseaux _centralisés_ (ressource web contrôlée par une autorité centrale) et _décentralisés_ (qui est un réseau différent du www traditionnel, dont le but est d'éliminer l'autorité centrale) _réseaux_, en utilisant le site web comme point d'accès et/ou comme interface graphique utilisateur. Le but de cette « identité crypto » est que vos actions sont cryptographiquement sécurisées, et personne ne peut changer ce que vous avez signé ni votre signature.

Aujourd'hui, les capacités de calcul et de stockage des réseaux décentralisés tolérants aux pannes comme [Ethereum](https://www.ethereum.org/), [EOS](https://eos.io/) ou [Tron](https://tron.network/) sont limitées. Si elles étaient scalables, nous pourrions utiliser des réseaux décentralisés pour stocker l'application décentralisée entière, y compris son interface graphique utilisateur, ses données et sa logique métier. Dans ce cas, nous appellerions ces applications véritablement décentralisées/distribuées.

Cependant, parce que ces réseaux ne sont pas scalables aujourd'hui, nous combinons différentes approches pour atteindre le niveau de décentralisation maximum pour nos applications. Le back end « traditionnel » tel que nous le connaissons n'est pas prêt de disparaître. Par exemple :

* Nous utilisons le back end pour héberger le front end d'une application décentralisée.
* Nous utilisons le back end pour les intégrations avec toute autre technologie et service existants. Les applications de classe mondiale ne peuvent pas vivre dans un environnement isolé.
* Nous utilisons le back end pour stocker et traiter tout ce qui est trop volumineux pour un réseau décentralisé (la blockchain en particulier). Pratiquement, l'application entière et sa logique métier sont stockées quelque part dans le monde, à l'exception de la partie blockchain uniquement. Sans parler, [IPFS](https://ipfs.io/) et des couches de stockage similaires [ne peuvent pas garantir](https://github.com/ipfs/faq/issues/93) l'accessibilité des fichiers, donc nous ne pouvons pas nous fier à eux sans héberger les fichiers nous-mêmes. En d'autres termes, il y a toujours besoin d'un serveur dédié en cours d'exécution.

Il n'y a aucun moyen de construire une application sécurisée et partiellement décentralisée sans utiliser un back end solide à ce jour, et le but de cet article est d'expliquer comment faire cela correctement.

### (Dé)centralisation et Jetons

Il se trouve que presque toutes les applications décentralisées aujourd'hui sont construites autour de ce que l'on appelle des [jetons](https://coinmarketcap.com/tokens/) — des cryptomonnaies sur mesure (ou simplement clonées) qui alimentent une application décentralisée particulière. Les jetons sont simplement une monnaie ou des actifs programmables, c'est tout.

![Image](https://cdn-media-1.freecodecamp.org/images/b-Ok08iucXB0n6VwiLcPzbW8BAWfTe7YRBxD)
*Alors que les contrats intelligents de jetons déterminent comment les utilisateurs peuvent transférer des jetons, les contrats intelligents d'application peuvent étendre tout ce qui manque dans les contrats intelligents de jetons. Les deux contrats intelligents s'exécutent sur des réseaux décentralisés*

Habituellement, un jeton est un « contrat intelligent » (un programme personnalisé) écrit sur la plateforme décentralisée comme Ethereum. En possédant certains jetons, vous êtes essentiellement en mesure d'obtenir différents services sur une ressource web ou une application mobile, et d'échanger ce jeton contre autre chose. Le point clé ici est que le jeton vit par lui-même et n'est pas contrôlé par une autorité centrale.

> Il existe de nombreux exemples d'applications construites autour de jetons : des nombreux jeux de collection comme [CryptoKitties](https://www.cryptokitties.co/) (jetons ERC721) à des applications plus orientées services comme [LOOM Network](https://loomx.io/purchase/), ou même des navigateurs comme [Brave](https://brave.com/download) et des plateformes de jeu comme [DreamTeam](https://dreamteam.gg/) (jetons compatibles ERC20).

Les développeurs eux-mêmes déterminent et décident combien de contrôle ils auront (ou n'auront pas) sur leurs applications. Ils peuvent construire toute la logique métier de l'application sur des contrats intelligents (comme [CryptoKitties](https://www.cryptokitties.co/) l'a fait), ou ils peuvent ne pas utiliser du tout de contrats intelligents, centralisant tout sur leurs serveurs. Cependant, la meilleure approche est quelque part entre les deux.

### Back End pour les Réseaux Décentralisés

D'un point de vue technique, il doit y avoir un pont qui relie les jetons et autres contrats intelligents à l'application web/mobile.

Dans les applications entièrement décentralisées d'aujourd'hui, où les clients interagissent directement avec les contrats intelligents, ce pont est réduit aux capacités de l'[API JSON RPC](https://github.com/ethereum/wiki/wiki/JSON-RPC) des [API publiques ou des pools de nœuds comme Infura](https://infura.io), qui à leur tour sont forcés d'exister en raison du fait que chaque appareil ne peut pas exécuter et supporter son propre nœud de réseau. Cependant, cette API ne fournit qu'un ensemble de fonctions de base et très restreint, qui permet à peine de faire des requêtes simples ni d'agréger efficacement les données. À cause de cela, finalement, un back end personnalisé intervient, rendant l'application semi-centralisée.

Toute l'interaction avec le réseau décentralisé peut être réduite à seulement un ou deux points, selon les besoins de l'application :

1. **Écouter les événements du réseau** (comme les transferts de jetons) / **lire l'état du réseau**.
2. **Publier des transactions** (invoquer des fonctions de contrat intelligent changeant l'état comme le transfert de jetons).

La mise en œuvre de ces deux points est assez délicate, surtout si nous voulons construire une solution back-end sécurisée et fiable. Voici les principaux points que nous allons détailler ci-dessous :

* Tout d'abord, dans Ethereum, la récupération des événements n'est pas prête pour la production dès la sortie de la boîte. Pour plusieurs raisons : les nœuds du réseau peuvent échouer lors de la récupération d'un grand nombre d'événements, les événements peuvent disparaître ou changer en raison des fourches du réseau, etc. Nous devons construire une couche d'abstraction pour synchroniser les événements à partir du réseau et garantir leur livraison fiable.
* Il en va de même pour la publication des transactions, nous devons abstraire les aspects de bas niveau d'Ethereum comme les compteurs de nonce et les estimations de gaz, ainsi que la republication des transactions, en fournissant une interface fiable et stable. De plus, la publication des transactions implique l'utilisation de clés privées, ce qui nécessite une sécurité avancée du back-end.
* Sécurité. Nous allons la prendre au sérieux et faire face au fait qu'il est impossible de garantir que les clés privées ne seront jamais compromises sur un back end. Heureusement, il existe une approche pour concevoir une application décentralisée sans même **le besoin** pour les comptes back-end d'être hautement sécurisés.

Dans notre pratique, tout cela nous a amenés à créer une solution back-end robuste pour Ethereum que nous appelons **Ethereum Gateway**. Elle abstrait d'autres microservices des particularités d'Ethereum et fournit une API fiable pour travailler avec.

En tant que [startup en croissance rapide](https://dreamteam.gg/), nous ne pouvons pas divulguer la solution complète (pas encore) pour des raisons évidentes, mais je vais partager tout ce que vous devez savoir pour faire fonctionner votre application décentralisée sans faille. Cependant, si vous avez des questions ou des demandes spécifiques, n'hésitez pas à me contacter [ici](https://nikita.tk/). Les commentaires sur cet article sont également très appréciés !

![Image](https://cdn-media-1.freecodecamp.org/images/aR03aGoFHc3EZ5ZCBVBPn6gqQEYYWFArNVy0)
*Surveillance du Back End pour Ethereum. Le moniteur démontre les activités principalement concernant notre [fonctionnalité de facturation récurrente](https://github.com/dreamteam-gg/smart-contracts/blob/master/contracts/token/TokenRecurringBilling.md" rel="noopener" target="_blank" title=") (bien que vous puissiez voir des pics se produire chaque heure).*

### Architecture des Applications Décentralisées

Cette partie de l'article dépend fortement des besoins d'une application décentralisée particulière, mais nous allons essayer de trier certains modèles d'interaction de base sur lesquels ces applications sont construites (ÐPlatform = Plateforme Décentralisée = Ethereum/EOS/Tron/Autre) :

#### **Client ↔ ÐPlatform** : **_applications entièrement décentralisées_**.

Le client (navigateur ou application mobile) communique directement avec la plateforme décentralisée à l'aide du logiciel « wallet » Ethereum comme [Metamask](https://metamask.io), [Trust](https://trustwallet.com/) ou des portefeuilles matériels comme [Trezor](https://trezor.io/) ou [Ledger](https://www.ledger.com/). Des exemples de DApps construites de cette manière sont [CryptoKitties](https://www.cryptokitties.co/), [Delegated Call](https://delegatecall.com/) de [Loom](https://loomx.io/), les portefeuilles crypto eux-mêmes ([Metamask](https://metamask.io/), [Trust](https://trustwallet.com/), [Tron Wallet](https://tron.network/wallet?lng=en), autres), les échanges crypto décentralisés comme [Etherdelta](http://etherdelta.com) et ainsi de suite.

#### **ÐPlatform ↔ Client ↔ Back End ↔ ÐPlatform** : **_applications centralisées ou semi-centralisées_**.

L'interaction du client avec la plateforme décentralisée et le serveur a peu en commun. Un bon exemple de cela est n'importe quel échange crypto (**_centralisé_**) aujourd'hui, comme [BitFinex](https://www.bitfinex.com/) ou [Poloniex](https://poloniex.com) : les devises que vous échangez sur les échanges sont simplement enregistrées dans la base de données traditionnelle. Vous pouvez « recharger » votre solde de base de données en envoyant des actifs à une adresse spécifique (ÐPlatform ↔ Client) et ensuite retirer des actifs après certaines actions dans l'application (Back End ↔ ÐPlatform), cependant, tout ce que vous faites en termes de « ÐApp » elle-même (Client ↔ Back End) n'implique pas votre interaction directe avec la ÐPlatform.

Un autre exemple est [Etherscan.io](https://etherscan.io/), qui utilise une approche **_semi-centralisée_** : vous pouvez effectuer toutes les actions décentralisées utiles là-bas, mais l'application elle-même n'a tout simplement pas de sens sans leur back end complet (Etherscan synchronise en continu les transactions, analyse les données et les stocke, fournissant finalement une API/UI complète).

#### **Quelque chose entre les deux : _toujours des applications centralisées ou semi-centralisées_**.

Les approches ci-dessus combinées. Par exemple, nous pouvons avoir une application qui fournit divers services en échange de crypto, vous permettant de vous connecter et de signer des informations avec votre identité crypto.

Espérons que le modèle d'interaction des applications entièrement décentralisées (Client ↔ ÐPlatform) ne soulève aucune question. En s'appuyant sur des services incroyables comme [Infura](https://infura.io/) ou [Trongrid](https://www.trongrid.io/), on peut simplement construire une application qui n'a pas besoin de serveur du tout. Presque toutes les bibliothèques côté client comme [Ethers.js](https://github.com/ethers-io/ethers.js/) pour Ethereum ou [Tron-Web](https://github.com/tronprotocol/tron-web) pour Tron peuvent se connecter à ces services publics et communiquer avec le réseau. Cependant, pour des requêtes et des tâches plus complexes, vous devrez peut-être allouer votre propre serveur de toute façon.

Le reste des modèles d'interaction qui impliquent le back end rendent les choses plus intéressantes et complexes. Pour mettre tout cela en image, imaginons un cas où notre back end réagit à un événement dans le réseau. Par exemple, l'utilisateur publie une transaction d'autorisation qui nous donne la permission de les facturer. Pour effectuer une facturation, nous devons publier la transaction de facturation en réponse à l'événement d'autorisation émis :

![Image](https://cdn-media-1.freecodecamp.org/images/86mjnQ0gwUrAbrBL4t8LFCXbC4HyckEsmFYQ)
*Un exemple de flux de réaction du serveur à l'action de l'utilisateur dans le réseau décentralisé*

Du point de vue du back end, voici ce qui se passe :

1. Nous écoutons un événement réseau particulier en interrogeant en continu le réseau.
2. Une fois que nous obtenons un événement, nous effectuons une logique métier puis décidons de publier une transaction en réponse.
3. Avant de publier la transaction, nous voulons nous assurer qu'elle sera probablement minée (dans Ethereum, l'estimation réussie du gaz de la transaction signifie qu'il n'y a pas d'erreurs contre l'_état actuel du réseau_). Cependant, nous ne pouvons pas garantir que la transaction sera minée avec _succès_.
4. En utilisant une clé privée, nous signons et publions la transaction. Dans Ethereum, nous devons également déterminer le prix du gaz et la limite de gaz de la transaction.
5. Après avoir publié la transaction, nous interrogeons en continu le réseau pour connaître son statut.
6. Si cela prend trop de temps et que nous ne pouvons pas obtenir le statut de la transaction, nous devons la republier ou déclencher un scénario d'échec. Les transactions peuvent être perdues pour diverses raisons : congestion du réseau, abandon des pairs, augmentation de la charge du réseau, etc. Dans Ethereum, vous pouvez également envisager de resigner une transaction avec un prix de gaz différent (actuel).
7. Après avoir finalement obtenu notre transaction minée, nous pouvons effectuer plus de logique métier si nécessaire. Par exemple, nous pouvons notifier d'autres services back end du fait que la transaction est terminée. De plus, envisagez d'attendre quelques confirmations avant de prendre des décisions finales concernant la transaction : le réseau est distribué et donc le résultat peut changer en quelques secondes.

Comme vous pouvez le voir, il se passe beaucoup de choses ! Cependant, votre application peut ne pas nécessiter certaines de ces étapes, selon ce que vous essayez d'accomplir. Mais, la construction d'un back end robuste et stable nécessite d'avoir une solution pour tous les problèmes mentionnés ci-dessus. Décomposons cela.

### Back End des Applications Décentralisées

Ici, je veux souligner certains des points qui posent le plus de questions, à savoir :

* Écouter les événements du réseau et lire les données à partir du réseau
* Publier des transactions et comment le faire de manière sécurisée

#### Écouter les Événements du Réseau

Dans Ethereum, ainsi que dans d'autres réseaux décentralisés, un concept de [événements de contrat intelligent (ou journaux d'événements, ou simplement journaux)](https://media.consensys.net/technical-introduction-to-events-and-logs-in-ethereum-a074d65dd61e) permet aux applications hors chaîne d'être informées de ce qui se passe dans la blockchain. Ces événements peuvent être créés par les développeurs de contrats intelligents à n'importe quel point du code du contrat intelligent.

Par exemple, dans la norme de jeton [ERC20](https://en.wikipedia.org/wiki/ERC-20) bien connue, chaque transfert de jeton [doit journaliser l'événement Transfer](https://etherscan.io/tx/0xe7186ec76b164e44212dda60fdace62bef67cf7dc017d2e6318d517daa9b01c9#eventlog), permettant ainsi aux applications hors chaîne de savoir qu'un transfert de jeton a eu lieu. En « écoutant » ces événements, nous pouvons effectuer des (ré)actions. Par exemple, certains portefeuilles crypto mobiles vous envoient une notification push/email lorsque des jetons sont transférés à votre adresse.

En fait, il n'existe pas de solution fiable pour écouter les événements du réseau dès la sortie de la boîte. Différentes bibliothèques vous permettent de suivre/écouter les événements, cependant, il existe de nombreux cas où quelque chose peut mal se passer, entraînant des événements perdus ou non traités. Pour éviter de perdre des événements, nous devons construire un back end personnalisé, qui maintiendra le processus de synchronisation des événements.

Selon vos besoins, la mise en œuvre peut varier. Mais pour vous donner une idée, voici l'une des options de la manière dont vous pouvez construire une livraison fiable des événements Ethereum en termes d'architecture de microservices :

![Image](https://cdn-media-1.freecodecamp.org/images/1I5pP5C6HTNGeXpSNO1TpQeFDvxRZnDzZDnt)
*Livraison fiable des événements Ethereum à tous les services back end*

Ces composants fonctionnent de la manière suivante :

1. Le service back end de synchronisation des événements interroge constamment le réseau, essayant de récupérer de nouveaux événements. Une fois que de nouveaux événements sont disponibles, il envoie ces événements au bus de messages. Après la soumission réussie de l'événement au bus de messages, comme pour la blockchain, nous pouvons enregistrer le dernier bloc de l'événement afin de demander de nouveaux événements à partir de ce bloc la prochaine fois. Gardez à l'esprit que la récupération de trop d'événements à la fois peut entraîner des requêtes toujours en échec, vous devez donc limiter le nombre d'événements/blocs que vous demandez au réseau.
2. Le bus de messages (par exemple, [Rabbit MQ](https://www.rabbitmq.com/)) achemine l'événement vers chaque file d'attente qui a été configurée individuellement pour chaque service back end. Avant la publication de l'événement, le service back end de synchronisation des événements spécifie la clé de routage (par exemple, une adresse de contrat intelligent + un [sujet](https://codeburst.io/deep-dive-into-ethereum-logs-a8d2047c7371) d'événement), tandis que les consommateurs (autres services back end) créent des files d'attente qui sont abonnées à des événements particuliers uniquement.

En résultat, chaque service back end reçoit uniquement les événements dont il a besoin. De plus, le bus de messages garantit la livraison de tous les événements une fois qu'ils sont publiés.

Bien sûr, vous pouvez utiliser autre chose à la place du bus de messages : des rappels HTTP, des sockets, etc. Dans ce cas, vous devrez trouver comment garantir la livraison des rappels vous-même : gérer les nouvelles tentatives de rappel exponentielles/personnalisées, implémenter une surveillance personnalisée, etc.

#### **Publication des Transactions**

Il y a quelques étapes que nous devons effectuer pour publier une transaction sur le réseau décentralisé :

1. Préparer la transaction. En plus des données de la transaction, cette étape implique de demander l'état du réseau afin de savoir si cette transaction est valide et va être minée (estimation du gaz dans Ethereum) et le numéro séquentiel de la transaction (nonce dans Ethereum). Certaines bibliothèques [essaient de faire cela sous le capot](https://github.com/ethers-io/ethers.js/issues/331), cependant, ces étapes sont importantes.
2. Signer la transaction. Cette étape implique l'utilisation de la clé privée. Très probablement, ici vous voudrez intégrer la solution d'assemblage de clé privée personnalisée ([par exemple](https://github.com/immutability-io/vault-ethereum)).
3. Publier et _republier_ la transaction. L'un des points clés ici est que votre transaction publiée a toujours une chance d'être perdue ou abandonnée par le réseau décentralisé. Par exemple, dans Ethereum, la transaction publiée peut être abandonnée si le [prix du gaz](https://ethgasstation.info/) du réseau augmente soudainement. Dans ce cas, vous devez republier la transaction. De plus, vous pouvez vouloir republier la transaction avec d'autres paramètres (au moins avec un prix de gaz plus élevé) afin de la faire miner le plus rapidement possible. Ainsi, la republication de la transaction peut impliquer sa resignature, si la transaction de remplacement n'a pas été pré-signée auparavant (avec différents paramètres).

![Image](https://cdn-media-1.freecodecamp.org/images/ZFZYOVlaW-CDPFpzwutxZTCVdeM4ifLqpsK8)
*Les points ci-dessus concernant la publication de transactions Ethereum visualisés*

En utilisant les approches ci-dessus, vous pouvez finir par construire quelque chose de similaire à ce qui est présenté dans le diagramme de séquence ci-dessous. Dans ce diagramme de séquence particulier, je démontre (en général !) comment fonctionne la [facturation récurrente sur blockchain](https://hackernoon.com/payments-of-tomorrow-decentralized-recurring-billing-47d126d895fd) (il y a plus dans l'article lié) :

1. L'utilisateur exécute une fonction dans un contrat intelligent, ce qui permet finalement au back end d'effectuer une transaction de facturation réussie.
2. Un service back end responsable d'une tâche particulière écoute l'événement d'autorisation de facturation et publie une transaction de facturation.
3. Une fois la transaction de facturation minée, ce service back end responsable d'une tâche particulière reçoit un événement du réseau Ethereum et effectue une logique (y compris la définition de la prochaine date de facturation).

![Image](https://cdn-media-1.freecodecamp.org/images/oNsxhuB9bVacGDh7pJyMjjk25gyipzS70lJg)
*Le diagramme de séquence général de la manière dont fonctionne la [facturation récurrente sur blockchain](https://hackernoon.com/payments-of-tomorrow-decentralized-recurring-billing-47d126d895fd" rel="noopener" target="_blank" title="), démontrant l'interaction entre les services back-end et le réseau Ethereum*

### Sécurité du Back End et Contrats Intelligents

La publication de transactions implique toujours l'utilisation d'une **clé privée**. Vous vous demandez peut-être s'il est possible de garder les clés privées en sécurité. Eh bien, oui et non. [Il existe](https://en.wikipedia.org/wiki/Threshold_cryptosystem) [de nombreuses](https://medium.com/gemini/cold-storage-keys-crypto-how-gemini-keeps-assets-safe-a732addcd13b) [stratégies complexes](https://www.coinbase.com/security) et [différents types de logiciels](https://www.vaultproject.io/) qui permettent de stocker les clés privées sur le back end de manière assez sécurisée. Certaines solutions de stockage de clés privées utilisent des bases de données géo-distribuées, tandis que d'autres suggèrent même l'utilisation de matériel spécial. Cependant, dans tous les cas, le point le plus vulnérable d'une application semi-centralisée est l'endroit où la clé privée est assemblée et utilisée pour signer une transaction (ou, dans le cas de matériel spécial, un point de déclenchement d'une procédure de signature de transaction). Par conséquent, théoriquement, il n'existe pas de solution fiable à 100 % qui permettra une protection infaillible contre la compromission des clés privées stockées.

Maintenant, réfléchissez de cette manière. Dans de nombreux cas, vous n'avez même pas besoin de sécuriser les clés privées sur le back end si souvent. Au lieu de cela, **vous pouvez concevoir des contrats intelligents et l'application entière de manière à ce qu'une fuite de clé privée n'affecte pas leur comportement habituel**. Avec cette approche, peu importe comment les comptes autorisés interagissent avec le contrat intelligent. Ils ne font que « déclencher » un contrat intelligent pour qu'il fasse son travail habituel, et le contrat intelligent lui-même effectue toute validation requise. Je l'appelle le modèle « comptes opérationnels ».

![Image](https://cdn-media-1.freecodecamp.org/images/Vl3V0DAGGdqi07BnffXkqRsl-0YROdAkgCG6)
*Modèle de comptes opérationnels pour les applications décentralisées, où vous n'avez pas besoin d'une sécurité de niveau militaire pour vos comptes back-end*

De cette manière, en cas d'urgence :

* La seule chose que l'attaquant peut voler est une petite quantité d'Ether (dans le cas d'Ethereum) déposée sur les comptes opérationnels pour la publication de transactions
* L'attaquant ne pourra pas nuire à la logique du contrat intelligent ni à quiconque est impliqué dans le processus
* Les comptes opérationnels compromis peuvent être rapidement remplacés par d'autres, cependant, cela nécessite soit le remplacement manuel (génération de nouveaux comptes, et réautorisation des comptes dans tous les contrats intelligents) soit le développement d'une solution supplémentaire qui fera toute la magie avec une seule transaction à partir d'un compte maître super-sécurisé (matériel ou [multi-sig](https://medium.com/@yenthanh/list-of-multisig-wallet-smart-contracts-on-ethereum-3824d528b95e)).

Par exemple, dans notre solution de [facturation récurrente pour Ethereum](https://hackernoon.com/payments-of-tomorrow-decentralized-recurring-billing-47d126d895fd), peu importe ce qui se passe sur un back end, le contrat intelligent de facturation récurrente est conçu de manière à ce que nous ayons un mois entier pour remplacer les comptes compromis si l'un d'eux est compromis.

Mais encore, si vous voulez que le stockage des clés privées de votre back end soit aussi sécurisé que possible, vous pouvez essayer d'utiliser [Vault](https://www.vaultproject.io/) avec un [excellent plugin pour Ethereum](https://github.com/dreamteam-gg) qui stocke et gère les comptes Ethereum (également, gardez un œil sur nos [modules open-source](https://github.com/dreamteam-gg) — nous sommes sur le point de publier quelque chose de similaire bientôt). Je ne vais pas entrer dans les détails ici, bien que vous puissiez visiter les projets liés et apprendre par vous-même.

Ce n'est même pas tout ce que j'ai à dire. Cependant, cet article s'est avéré beaucoup plus long que je ne l'avais prévu, donc je dois m'arrêter. Abonnez-vous à mon [Medium](https://medium.com/@zitro) / [autres réseaux](https://nikita.tk/) si vous êtes intéressé par le logiciel, la crypto, les [conseils de voyage](https://instagram.com/nikitaeverywhere/) ou si vous voulez simplement suivre quelque chose d'intéressant. J'espère avoir fourni un grand morceau d'information précieux et que vous le trouverez utile. N'hésitez pas à commenter et à partager cet article !