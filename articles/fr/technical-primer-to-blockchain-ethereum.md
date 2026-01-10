---
title: Primer technique sur la Blockchain et Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-23T06:30:00.000Z'
originalURL: https://freecodecamp.org/news/technical-primer-to-blockchain-ethereum
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca14a740569d1a4ca4dc5.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: ethereum blockchain
  slug: ethereum-blockchain
seo_title: Primer technique sur la Blockchain et Ethereum
seo_desc: 'By Srinivasan C

  I attended a talk on Ethereum sometime back and was fascinated by the possibilities
  it provided and started exploring the ecosystem. It is a pretty nascent ecosystem
  that is catching up fast among the developer community. In this post...'
---

Par Srinivasan C

J'ai assisté à une conférence sur Ethereum il y a quelque temps et j'ai été fasciné par les possibilités qu'il offrait et j'ai commencé à explorer l'écosystème. Il s'agit d'un écosystème assez naissant qui se développe rapidement au sein de la communauté des développeurs. Dans cet article, je vais expliquer la technologie derrière Ethereum afin que nous puissions commencer à développer avec Ethereum. Cela suppose que vous avez un background technique et une compréhension de base de la blockchain afin que nous puissions discuter de l'implémentation d'Ethereum.

## Premières choses d'abord

La blockchain fournit un réseau **décentralisé**, **pair à pair** où les actifs numériques peuvent être transférés d'un pair à un autre. Le principal problème auquel nous sommes confrontés dans un réseau décentralisé est de savoir qui va vérifier la validité de toutes les **transactions** qui ont lieu ? La réponse courte est **tout le monde.**

Imaginez un document avec certaines informations. Chaque personne dans le réseau conserve une copie du même document. Si une mise à jour est effectuée dans le document, elle est propagée à travers le réseau et tout le monde met à jour sa propre copie du document. Supposons qu'une nouvelle personne arrive avec un contenu différent dans le document, alors tous les autres peuvent vérifier leur copie et détecter que la nouvelle personne ment et l'exclure du réseau. C'est ainsi que fonctionne une blockchain.

Tout d'abord, nous devons comprendre quelques termes de base pour commencer.

### Hash

Nous pouvons utiliser une fonction de hachage cryptographique (SHA256) pour convertir n'importe quelle chaîne en son hachage équivalent. Le hachage a deux propriétés uniques :

1. Le hachage produit a une **correspondance un à un** avec la chaîne d'entrée. La même entrée produit toujours le même hachage unique et aucune autre entrée ne peut avoir le même hachage.
2. Même un **petit changement** dans la chaîne d'entrée entraînera un **grand changement** dans le hachage de sortie et ainsi l'entrée peut être facilement validée.

### Transaction

Le processus par lequel les actifs sont transférés d'une partie à une autre dans le réseau est appelé Transaction. Toutes les transactions sont enregistrées et stockées de manière permanente. Supposons que A souhaite transférer 5 Ether à B. Alors cela constitue une transaction dans le réseau.

### Bloc

De nombreuses transactions sont combinées pour former un bloc. Chaque bloc contient un **hachage** unique qui l'identifie dans le réseau. Un bloc est enchaîné au bloc précédent en utilisant le hachage du bloc précédent.

### Bloc Genesis

Le bloc initial ou l'état initial de la blockchain sur lequel tous les nœuds du réseau sont d'accord.

### Blockchain

À mesure que les transactions sont ajoutées, de nombreux blocs sont créés, puis ils sont enchaînés ensemble en utilisant leurs hachages pour former le réseau blockchain.

### Preuve de travail

Une **preuve de travail** est une pièce de données qui est difficile (coûteuse, chronophage) à produire mais facile à vérifier pour les autres et qui satisfait certaines exigences. Lorsqu'il y a une transaction dans le réseau, tout nœud qui tente de traiter la transaction doit résoudre une énigme cryptographique pour qu'elle soit acceptée dans le bloc. Cela est connu sous le nom de preuve de travail. Le travail à effectuer ne peut être fait que par essai et erreur et cela doit être effectué pour toute transaction valide dans le réseau avant qu'elle ne puisse faire partie de la blockchain.

### Minage

Le processus de traitement d'une transaction et de son ajout au bloc en effectuant la preuve de travail est appelé minage. Les mineurs (nœuds) reçoivent les récompenses de la transaction une fois que la transaction est acceptée comme faisant partie de la blockchain.

### Arbre de Merkle

Un **arbre de Merkle** est un arbre dans lequel chaque nœud non-feuille est étiqueté avec le hachage des étiquettes de ses nœuds enfants. Nous pouvons vérifier que les blocs de données reçus d'autres nœuds sont reçus intacts et non altérés, et même vérifier que les autres nœuds ne mentent pas et n'envoient pas de faux blocs.

### Fonctionnement

Nous pouvons maintenant passer au fonctionnement de base d'une blockchain.

1. Chaque nœud commence avec le bloc genesis et construit son chemin jusqu'à l'état "actuel" de la blockchain. Lorsqu'il reçoit un nouveau bloc, chaque nœud vérifie son hachage et valide ainsi s'il s'agit d'un bloc valide ou non et continue de construire la chaîne.
2. Une fois qu'il y a une transaction dans le réseau, le mineur la mine en générant la preuve de travail requise. Ensuite, le mineur l'ajoute à sa copie du réseau et **propage** le changement aux nœuds voisins.
3. Tous les nœuds qui le reçoivent valideront la preuve de travail et l'ajouteront ensuite à leurs copies respectives. Si elle n'est pas valide, le bloc n'est pas ajouté à la chaîne.
4. En cas de conflit dans le réseau, la règle de la "chaîne la plus longue" est appliquée pour le résoudre. Supposons que deux mineurs revendiquent le même bloc et que les deux ont une preuve de travail valide. Ensuite, la règle de la chaîne la plus longue est appliquée, ce qui signifie que le mineur qui a la chaîne de blocs la plus longue sera considéré comme le gagnant et celle-ci sera ajoutée à la blockchain.

## Ethereum

![Image](https://cdn-media-1.freecodecamp.org/images/1*AReX8uZOZKpGcvuUjogh0g.png)

Maintenant que vous avez compris la blockchain, passons à Ethereum. Ethereum est une **plateforme décentralisée** qui nous permet d'écrire des applications qui s'exécutent exactement comme programmées sans possibilité de temps d'arrêt, de censure, de fraude ou d'interférence de tiers. Elle comprend la machine virtuelle Ethereum (EVM) qui fournit le conteneur dans lequel tous les contrats intelligents peuvent être exécutés.

### Contrats intelligents

Ethereum nous permet d'écrire des applications sur la blockchain et ces applications sont appelées contrats intelligents. Ces contrats intelligents résident sur la blockchain et sont **immutables**, c'est-à-dire que le code ne peut pas être supprimé ou modifié dans la blockchain une fois qu'il est déployé. Cela peut être écrit en utilisant Solidity ou d'autres langages, mais le plus préféré est Solidity. C'est un langage Turing complet.

### Ether

L'Ether est la cryptomonnaie utilisée dans la blockchain Ethereum.

### Comptes

Dans Ethereum, l'état est constitué d'objets appelés "comptes", chaque compte ayant une adresse de 20 octets et les transitions d'état étant des transferts directs de valeur et d'informations entre les comptes. Il existe deux types de comptes dans Ethereum :

* **Comptes détenus par des tiers :** Ces comptes sont détenus par des utilisateurs, contrôlés par des clés privées. Un compte détenu par un tiers n'a pas de code, et l'on peut envoyer des messages depuis un compte détenu par un tiers en créant et en signant une transaction.
* **Comptes de contrat :** Ces comptes sont détenus par le code du contrat. Dans un compte de contrat, chaque fois que le compte de contrat reçoit un message, son code s'active, lui permettant de lire et d'écrire dans le stockage interne et d'envoyer d'autres messages ou de créer des contrats à son tour.

### Gaz

Comme les contrats intelligents sont Turing complets, toute boucle infinie ou autre code peut être écrit et la blockchain peut être crashée. Pour prévenir de telles attaques, Ethereum utilise un concept appelé gaz. Le gaz n'est rien d'autre qu'un coût de transaction qui est payé pour exécuter la transaction en utilisant de l'Ether (monnaie de base dans la chaîne Ethereum). Chaque instruction nécessite une certaine quantité de gaz pour être exécutée et le gaz est envoyé avec tout appel qui doit modifier la blockchain.

### DAPPS

Ce sont des applications distribuées qui peuvent être construites en utilisant les contrats intelligents et en fournissant une interface pour les utilisateurs (comptes). Différents types d'applications peuvent être développés qui interagiront avec les contrats intelligents résidant dans la blockchain.

### Flux de travail de base utilisant Ethereum

Nous pouvons discuter d'un flux de travail de base dans le réseau Ethereum pour une meilleure compréhension de la manière dont tous ces concepts fonctionnent ensemble en harmonie.

1. Nous pouvons écrire des contrats intelligents et les déployer sur le réseau Ethereum. Une fois déployés, ces contrats ne peuvent pas être modifiés.
2. Tout compte ou un autre contrat intelligent dans le réseau peut exécuter les fonctions de ces contrats intelligents par le biais de transactions.
3. Les contrats intelligents peuvent être appelés et exécutés en envoyant des transactions au contrat. Ces transactions coûtent du **gaz** et une certaine quantité de gaz doit également être envoyée avec la transaction.
4. Parfois, nous devons simplement connaître l'état d'un contrat sans modifier la blockchain. Cela est connu sous le nom de **calls et ils ne coûtent aucun gaz.**
5. Nous pouvons construire diverses Dapps en exécutant les contrats intelligents en utilisant des transactions et des appels, permettant ainsi à l'utilisateur d'interagir directement avec le contrat intelligent de différentes manières.

Je crois que cet article fournit une compréhension de base de la blockchain et d'Ethereum. Dans mon prochain article, je fournirai un guide détaillé pour commencer à construire des Dapps en utilisant Ethereum.

*Si vous avez aimé cette histoire, n'hésitez pas à me contacter à l'adresse suivante : [https://kaizencoder.com/](https://kaizencoder.com/contact)*