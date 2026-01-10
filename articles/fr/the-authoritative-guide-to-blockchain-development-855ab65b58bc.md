---
title: Le guide de référence pour le développement blockchain
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-28T00:18:36.000Z'
originalURL: https://freecodecamp.org/news/the-authoritative-guide-to-blockchain-development-855ab65b58bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yv83BoA58zpiWCvBzWh7gA.png
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Le guide de référence pour le développement blockchain
seo_desc: 'By Haseeb Qureshi

  Cryptocurrencies, ICOs, magic internet money — it’s all so damn exciting, and you,
  the eager developer, want to get in on the madness. Where do you start?

  I’m glad you’re excited about this space. I am too. But you’ll probably find ...'
---

Par Haseeb Qureshi

Cryptomonnaies, ICO, argent magique d'internet — tout cela est si excitant, et vous, développeur enthousiaste, voulez participer à cette folie. Par où commencer ?

Je suis heureux que vous soyez excité par ce domaine. Moi aussi. Mais vous allez probablement trouver qu'il n'est pas clair où commencer. La blockchain évolue à une vitesse folle, mais il n'y a pas de voie claire pour apprendre tout cela.

Depuis que j'ai quitté Airbnb pour travailler à plein temps sur la blockchain, beaucoup de gens m'ont demandé comment entrer dans l'espace blockchain à plein temps. Considérez ceci comme mon guide de référence (et inévitablement incomplet) sur la façon de se lancer dans l'ingénierie blockchain.

Ce guide se déroulera en dix parties :

1. **Pourquoi devriez-vous apprendre le développement blockchain ?**
2. **Prérequis**
3. **Les fondements théoriques de Bitcoin**
4. **Construire une blockchain vous-même**
5. **Ethereum et la programmation de contrats intelligents**
6. **Sécurité des contrats intelligents**
7. **Enlever les roues d'entraînement**
8. **Construire vos propres projets**
9. **Naviguer dans la communauté blockchain**
10. **Trouver un emploi**

### Pourquoi devriez-vous apprendre le développement blockchain ?

Avant de répondre à cette question, laissez-moi d'abord noter : la blockchain est un espace massivement surévalué en ce moment. Ces prix ne sont pas durables, et un krach est définitivement en route. Cela s'est déjà produit par le passé, et cela se reproduira probablement. Mais si vous travaillez à long terme dans ce domaine, vous apprendrez à ignorer les prix. Comme le dit Emin Gun Sirer — les prix sont la partie la moins intéressante des cryptomonnaies. Ce sont des technologies massivement importantes, et elles vont changer irrévocablement le monde.

Si vous n'êtes pas sûr, je ne peux pas vous dire si vous devriez sauter le pas. Mais je peux vous donner cinq raisons qui m'ont convaincu de faire le saut :

1. **C'est encore tôt.**

Bitcoin a été inventé il y a 10 ans, mais le rythme de l'innovation n'a atteint un niveau frénétique que ces dernières années, surtout avec le lancement d'Ethereum en 2015. La plupart des nouvelles entreprises et idées dans ce domaine ont été construites sur Ethereum, qui est encore très immature.

Même si vous commencez maintenant, vous pouvez réalistement devenir un expert de classe mondiale en quelques années. La plupart des gens n'ont pas fait cela depuis si longtemps, et ce ne sera pas si difficile de rattraper. Commencer maintenant serait analogue aux experts en apprentissage profond qui ont commencé à étudier le sujet à la fin des années 2000.

**2. Ce domaine n'a pas encore de fort vivier de talents.**

La plupart des meilleurs et plus brillants étudiants des universités se concentrent sur l'apprentissage automatique, la programmation web ou le développement de jeux. Bien sûr, les blockchains deviennent plus sexy dans le discours public, mais elles restent un sujet étrange et subversif sur lequel miser sa carrière.

Au début, la blockchain était exclusivement le domaine des cypherpunks, des paranoïaques et des marginaux. Cela n'a commencé à changer que récemment. En étant simplement un développeur curieux et ouvert d'esprit, vous apporterez beaucoup de valeur à ce domaine.

**3. Une grande partie de l'innovation se fait en dehors du milieu universitaire.**

Satoshi Nakamoto n'était pas un universitaire, autant que nous le sachions. Il n'y a pas d'université ou d'institution qui offre une concentration cohérente sur la blockchain pour l'instant. La plupart de l'innovation ici a été menée par des passionnés, des entrepreneurs et des chercheurs indépendants. Presque tout ce que vous devez savoir se trouve dans des livres blancs, des articles de blog, des chaînes Slack publiques et des logiciels open source. Il suffit de retrousser ses manches et de se lancer dans la mêlée.

**4. La demande de talents dépasse de loin l'offre.**

Il n'y a tout simplement pas assez de développeurs dans ce domaine, et ils ne peuvent pas être formés assez rapidement. Tout le monde se dispute pour embaucher des talents blockchain, et les projets ressentent la pénurie de talents. Beaucoup des meilleures entreprises ne peuvent pas payer leurs employés assez pour les garder parce qu'ils ont trop d'opportunités. Si vous acquérez quelques compétences, il sera facile de trouver un emploi.

**5. Les cryptomonnaies sont vraiment très cool.**

Où ailleurs pouvez-vous construire des trucs de science-fiction comme de l'argent décentralisé et sécurisé cryptographiquement ? C'est le Far West en ce moment — et cela apporte du bon et du mauvais. Le domaine pourrait utiliser plus de transparence, et la régulation viendra éventuellement. Mais sans aucun doute, les cryptomonnaies sont l'un des domaines les plus innovants dans lesquels vous pouvez travailler en ce moment.

Naval Ravikant [a dit dans une récente interview](https://www.pscp.tv/w/1eaKbqrWloRxX) : la clé du succès est de donner à la société des choses qu'elle veut, mais qu'elle ne sait pas comment obtenir par elle-même. Vous ne pouvez pas aller à l'école pour de telles choses ; si vous le pouviez, le monde aurait déjà un approvisionnement régulier.

Alors construisez quelque chose que personne d'autre ne sait construire. En ce moment, les blockchains sont toutes nouvelles et il y a tant de choses à découvrir. Si vous réussissez à construire l'avenir de la technologie décentralisée, le monde vous récompensera grassement.

Donc, disons que vous voulez vous lancer. Que devez-vous savoir avant d'entrer dans l'arène ?

### Prérequis

Je recommande de renforcer votre compréhension des fondamentaux avant de plonger plus loin. Les blockchains sont construites sur des décennies de recherche en informatique, cryptographie et économie. Satoshi Nakamoto était un renégat, mais il connaissait bien l'histoire qui l'avait précédé. Pour comprendre pourquoi les blockchains fonctionnent, vous devez comprendre leurs éléments de base — ce qui existait avant les blockchains, et pourquoi ces choses ne fonctionnaient pas.

Voici quelques bons prérequis à connaître, par ordre d'importance.

Notez que ces liens ne sont qu'un point de départ, vous voudrez probablement approfondir beaucoup de ces sujets.

### Informatique

#### Structures de données

Vous voudrez être familier avec les caractéristiques et les garanties de complexité des principales structures de données : [listes chaînées](https://en.wikipedia.org/wiki/Linked_list), [arbres binaires de recherche](https://en.wikipedia.org/wiki/Binary_search_tree), [tables de hachage](https://en.wikipedia.org/wiki/Hash_table) et [graphes](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)) (spécifiquement, [graphes acycliques dirigés](https://en.wikipedia.org/wiki/Directed_acyclic_graph) qui jouent un rôle important dans les blockchains). Il est utile de les avoir construits à partir de zéro pour mieux comprendre leur fonctionnement et leurs propriétés.

#### Cryptographie

La cryptographie est l'homonyme et le socle des cryptomonnaies. Toutes les cryptomonnaies utilisent la [cryptographie à clé publique/privée](https://en.wikipedia.org/wiki/Public-key_cryptography) comme base pour l'identité et l'authentification. Je recommande d'étudier [RSA](https://www.youtube.com/watch?v=vgTtHV04xRI) (c'est facile à apprendre et ne nécessite pas un fort bagage mathématique), puis de regarder [ECDSA](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/). La cryptographie à courbe elliptique nécessite des mathématiques significativement plus abstraites — il n'est pas important de comprendre tous les détails, mais sachez que c'est la cryptographie utilisée dans la plupart des cryptomonnaies, y compris Bitcoin.

L'autre primitive cryptographique importante est la [fonction de hachage cryptographique](https://en.wikipedia.org/wiki/Cryptographic_hash_function). Celles-ci peuvent être utilisées pour construire des [schémas d'engagement](https://en.wikipedia.org/wiki/Commitment_scheme), et sont les éléments de base des [arbres de Merkle](https://en.wikipedia.org/wiki/Merkle_tree). Les arbres de Merkle permettent les [preuves de Merkle](https://indigoframework.com/documentation/v0.1.0/references/proof-of-existence/), l'une des optimisations clés que les blockchains utilisent pour la scalabilité.

#### Systèmes distribués

Il existe quelques [bons manuels](https://dataintensive.net/) sur les systèmes distribués, mais c'est un domaine d'étude vaste et difficile. Les systèmes distribués sont absolument essentiels pour raisonner sur les blockchains, vous devez donc construire une base ici avant de vous attaquer à la programmation blockchain.

Une fois que vous ne vivez plus sur une seule machine, vous devez commencer à raisonner sur la [cohérence](https://en.wikipedia.org/wiki/Consistency_model) et le [consensus](https://en.wikipedia.org/wiki/Consensus_(computer_science)). Vous voudrez connaître la différence entre les modèles de [linéarisation](https://en.wikipedia.org/wiki/Linearizability) et de [cohérence éventuelle](https://en.wikipedia.org/wiki/Eventual_consistency). Vous voudrez également apprendre les garanties des algorithmes de consensus [tolérants aux pannes](https://en.wikipedia.org/wiki/Fault_tolerance), tels que [Paxos](https://en.wikipedia.org/wiki/Paxos_(computer_science)) et [RAFT](https://en.wikipedia.org/wiki/Raft_(computer_science)). [Connaître les difficultés de raisonnement sur le temps dans un système distribué](https://www.youtube.com/watch?v=BRvj8PykSc4). Appréciez les compromis entre [sécurité et vivacité](http://www.bailis.org/blog/safety-and-liveness-eventual-consistency-is-not-safe/).

Avec cette base, vous serez en mesure de comprendre les difficultés autour du [consensus tolérant aux pannes byzantines](https://en.wikipedia.org/wiki/Byzantine_fault_tolerance), la principale exigence de sécurité des blockchains publiques. Vous voudrez en savoir plus sur [PBFT](https://blog.acolyer.org/2015/05/18/practical-byzantine-fault-tolerance/), l'un des premiers algorithmes évolutifs à fournir un consensus tolérant aux pannes byzantines. PBFT est la base de nombreux algorithmes de consensus de blockchain non basés sur la preuve de travail. Encore une fois, vous n'avez pas besoin de comprendre les détails de la façon dont et pourquoi PBFT est correct, mais obtenez l'idée générale et ses garanties de sécurité.

Il est également très utile de comprendre les [méthodes traditionnelles de distribution des bases de données](https://en.wikipedia.org/wiki/Distributed_database) (après tout, les blockchains sont des bases de données au cœur). Apprenez le [sharding](https://en.wikipedia.org/wiki/Shard_(database_architecture)) (comme via le [hachage cohérent](https://en.wikipedia.org/wiki/Consistent_hashing)), la [réplication leader-suiveur](https://en.wikipedia.org/wiki/Replication_(computing)), et les [commits basés sur le quorum](https://en.wikipedia.org/wiki/Quorum_(distributed_computing)). Regardez les [tables de hachage distribuées (DHT)](https://en.wikipedia.org/wiki/Distributed_hash_table), comme [Chord](https://en.wikipedia.org/wiki/Chord_(peer-to-peer)) ou [Kademlia](https://en.wikipedia.org/wiki/Kademlia).

#### Réseautage

La décentralisation des blockchains provient en grande partie de leur topologie de réseau pair-à-pair. À ce titre, les blockchains sont des descendants directs des anciens réseaux P2P.

Pour comprendre le modèle de communication blockchain, vous devez comprendre les bases du [réseautage informatique](https://en.wikipedia.org/wiki/Computer_network) : cela signifie comprendre [TCP vs UDP](https://www.diffen.com/difference/TCP_vs_UDP), [le modèle de paquet, à quoi ressemblent les paquets IP](https://en.wikipedia.org/wiki/Network_packet), et à peu près comment fonctionne le [routage Internet](https://en.wikipedia.org/wiki/Routing).

Les blockchains publiques tendent à diffuser des messages via des [protocoles de commérages](https://en.wikipedia.org/wiki/Gossip_protocol) utilisant l'[inondation](https://en.wikipedia.org/wiki/Flooding_(computer_networking)). Il est instructif d'apprendre l'histoire de la [conception de réseaux P2P](https://en.wikipedia.org/wiki/Peer-to-peer), de [Napster à Gnutella](http://www.springer.com/cda/content/document/cda_downloaddocument/9783642035135-c2.pdf?SGWID=0-0-45-855488-p173920223), [BitTorrent](https://en.wikipedia.org/wiki/BitTorrent) et [Tor](https://en.wikipedia.org/wiki/Tor_(anonymity_network)). Les blockchains ont leur propre place, mais elles s'inspirent des leçons de ces réseaux et de la manière dont ils ont été conçus.

### Économie

Les cryptomonnaies sont intrinsèquement multidisciplinaires — c'est ce qui les rend si fascinantes et radicales. En plus de l'informatique, de la cryptographie et du réseautage, elles sont également profondément liées à l'économie. Les cryptomonnaies peuvent tirer de nombreuses propriétés de sécurité de leurs structures économiques, ce qui est souvent appelé _cryptoeconomie_. À ce titre, l'économie est essentielle pour comprendre les cryptomonnaies.

#### Théorie des jeux

La branche la plus importante de l'économie qui joue dans les cryptomonnaies est la [théorie des jeux](https://en.wikipedia.org/wiki/Game_theory), l'étude des gains et des incitations parmi plusieurs agents. Vous n'avez pas besoin d'aller _extrêmement_ loin ici, mais vous devez comprendre les outils de base de l'analyse de la théorie des jeux et comment vous pouvez les utiliser pour analyser les incitations dans les jeux à une seule étape et les jeux itératifs.

Deux concepts clés dans votre répertoire devraient être les [équilibres de Nash](https://en.wikipedia.org/wiki/Nash_equilibrium) et les [points de Schelling](https://en.wikipedia.org/wiki/Focal_point_(game_theory)), car ils jouent un rôle important dans l'analyse cryptoeconomique.

#### Macroeconomie

Les cryptomonnaies ne sont pas seulement des protocoles, ce sont aussi des formes d'argent. À ce titre, elles répondent aux lois de la [macroeconomie](https://en.wikipedia.org/wiki/Macroeconomics) (si elles peuvent être appelées lois). Les cryptomonnaies sont soumises à différentes [politiques monétaires](https://en.wikipedia.org/wiki/Monetary_policy), et répondent de manière prévisible à l'[inflation](https://en.wikipedia.org/wiki/Inflation) et à la [déflation](https://en.wikipedia.org/wiki/Deflation). Vous devriez comprendre ces processus et les effets qu'ils ont sur les dépenses, l'épargne, etc.

Un autre concept économique précieux est la [vitesse de la monnaie](https://en.wikipedia.org/wiki/Velocity_of_money), en particulier en ce qui concerne l'évaluation d'une monnaie.

#### Microéconomie

Les cryptomonnaies sont également profondément liées aux marchés, ce qui nécessite une compréhension de la [microéconomie](https://en.wikipedia.org/wiki/Microeconomics). Vous aurez besoin d'une forte intuition pour les [courbes d'offre et de demande](https://en.wikipedia.org/wiki/Supply_and_demand). Vous devriez être capable de raisonner sur la concurrence et les [coûts d'opportunité](https://en.wikipedia.org/wiki/Opportunity_cost) (ils s'appliqueront fréquemment à l'exploitation minière de cryptomonnaies). Pour de nombreuses distributions de pièces et systèmes cryptoeconomiques, la [théorie des enchères](https://www.youtube.com/watch?v=4kWuxfVbIaU) joue un rôle important.

Je m'attends à ce que vous soyez déjà familier avec certains de ces sujets. Si c'est le cas, n'hésitez pas à les parcourir ou à les sauter entièrement.

D'accord, à ce stade, vous avez parcouru et renforcé vos fondamentaux (ou peut-être en avez-vous sauté beaucoup, qui compte ?), alors maintenant que vous avez votre théorie en ordre, commençons le développement blockchain.

### Les fondements théoriques de Bitcoin

En octobre 2008, Satoshi Nakamoto a publié un livre blanc dans lequel il décrivait un protocole pour une monnaie numérique décentralisée. Il a appelé ce protocole Bitcoin.

Avant de pouvoir comprendre les grandes idées derrière les blockchains, vous devez commencer par Bitcoin et saisir l'idée originale de Satoshi.

Tout d'abord, je recommande de construire vos intuitions sur la preuve de travail et la règle de choix de fourche (également connue sous le nom de consensus Nakamoto). Commencez ici :

Je recommande de regarder plus d'une explication vidéo pour bien comprendre l'idée :

Bien. Maintenant que vous avez construit votre intuition, [cet article](https://www.igvita.com/2014/05/05/minimum-viable-block-chain/) fournira une exposition plus approfondie de bout en bout des composants critiques du fonctionnement de Bitcoin.

### Construire une blockchain vous-même

Maintenant que vous avez l'intuition de haut niveau, il est temps de construire votre propre blockchain basée sur la preuve de travail. Ne vous inquiétez pas, c'est plus facile que cela n'y paraît. Voici quelques bonnes ressources.

Tout d'abord, j'ai une conférence vidéo où je montre exactement comment faire cela en Ruby (je recommande de regarder même si vous n'êtes pas un programmeur Ruby) :

[Source et diapositives ici.](https://github.com/Haseeb-Qureshi/lets-build-a-blockchain)

Il existe également d'autres [implémentations de blockchain](https://github.com/openblockchains/awesome-blockchains) que vous pouvez trouver, écrites dans divers langages de programmation. Allez-y et construisez la vôtre, et assurez-vous qu'elle est principalement fonctionnelle.

Une fois que vous êtes arrivé à ce stade, vous devriez avoir une bonne compréhension de la façon d'implémenter une application de paiement simple sur une blockchain (c'est-à-dire, Bitcoin). Vous devriez également avoir assez de connaissances pour lire et comprendre le [livre blanc original de Bitcoin](https://bitcoin.org/bitcoin.pdf).

Pour comprendre l'économie et la mécanique de l'exploitation minière de Bitcoin, je recommande de regarder la [conférence sur l'exploitation minière de Bitcoin](https://www.youtube.com/watch?v=jXerV3f5jN8) dans le cours Bitcoin et Cryptomonnaies de Princeton.

Si vous êtes arrivé à ce stade, vous devriez comprendre Bitcoin suffisamment bien pour [parcourir un en-tête de bloc Bitcoin](https://www.youtube.com/watch?v=gUwXCt1qkBU) et comprendre ce que chacun de ses composants signifie. Vous devriez également être capable de jouer avec un [explorateur de blocs Bitcoin](https://blockchain.info/) et de naviguer dans des transactions Bitcoin brutes.

Maintenant est un bon moment pour étudier l'histoire de Bitcoin et des cryptomonnaies. La vidéo ci-dessous, offerte par un Decal de l'UC Berkeley, donne un bon aperçu.

Quelques ressources supplémentaires pour le crédit supplémentaire :

* [Précurseurs académiques de Bitcoin](https://queue.acm.org/detail.cfm?id=3136559)
* Mécanique de Bitcoin : [UTXOs et script Bitcoin](https://www.youtube.com/watch?v=q5GWwTgRIT4) (le script Bitcoin n'est pas super important, sachez simplement à peu près ce qu'il peut faire)
* [Court guide des fourches Bitcoin](https://www.coindesk.com/short-guide-bitcoin-forks-explained/)
* [Soft forks et signalisation des mineurs](https://en.bitcoin.it/wiki/Softfork)
* [Dépenses doubles, attaques à 51%, et minage égoïste](https://www.youtube.com/watch?v=UPxaCj8ZsEU)
* [Attaques par relecture](https://bitcointechtalk.com/how-to-protect-against-replay-attacks-7a00bd2fe52f)
* [Problèmes de scalabilité de Bitcoin](https://en.wikipedia.org/wiki/Bitcoin_scalability_problem), qui est la source de la plupart des contentieux dans l'écosystème Bitcoin. Vous devriez avoir une idée de pourquoi les gens de Bitcoin se disputent tant sur la taille des blocs.
* [Segregated witness, alias SegWit](https://en.wikipedia.org/wiki/SegWit), pas essentiel mais cela revient souvent.
* [Lightning Network](https://lightning.network/), l'une des solutions de mise à l'échelle les plus importantes pour Bitcoin, qui se généralise également à d'autres blockchains
* [Nœuds complets Bitcoin](https://bitnodes.earn.com/), [statistiques des frais Bitcoin](https://bitcoinfees.earn.com/), [graphiques](https://blockchain.info/charts), [graphiques](https://coin.dance/stats) et [plus de graphiques](https://bitcointicker.co/networkstats/)
* [Indice de consommation d'énergie de Bitcoin](https://digiconomist.net/bitcoin-energy-consumption) (au moment de la publication, l'exploitation minière de Bitcoin consomme autant d'énergie que tout le Pérou)
* [Essai perspicace de Gwern](https://www.gwern.net/Bitcoin-is-Worse-is-Better) sur l'inefficacité rustique de Bitcoin
* Jameson Lopp a une [richesse d'autres ressources](https://lopp.net/bitcoin.html) sur Bitcoin si vous voulez aller plus loin dans le terrier du lapin.

### Ethereum et la programmation de contrats intelligents

Maintenant que vous avez construit une blockchain et compris la dynamique de Bitcoin, il est temps de plonger dans Ethereum.

Vous comprenez comment les blockchains et la preuve de travail peuvent atteindre un consensus distribué, tolérant aux pannes byzantines au sein d'un réseau pair-à-pair. Mais un réseau de paiement n'est qu'une seule application que vous pouvez exécuter sur une telle blockchain. En 2013, Vitalik Buterin, le créateur d'Ethereum, a demandé : et si vous utilisiez une blockchain pour implémenter un ordinateur décentralisé ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*Mx3AZWrwFc6KP6Fr.png)

Dans Ethereum, vous payez les mineurs pour exécuter vos programmes sur cette machine virtuelle distribuée. Cela signifie que vous pouvez effectuer des calculs arbitraires, en utilisant un langage de programmation Turing-complet (contrairement au script Bitcoin). Évidemment, cela inclut les applications liées aux paiements, donc Ethereum permet un sur-ensemble des fonctionnalités de Bitcoin et a donné naissance à une renaissance de l'innovation.

Cela nous amène aux contrats intelligents — le nom des programmes qui s'exécutent sur une telle machine virtuelle. Un contrat intelligent peut interagir directement avec la cryptomonnaie de la blockchain conformément à l'exécution d'un programme. En d'autres termes, vous pouvez créer des contrats financiers qui s'appliquent automatiquement. C'est une idée folle, et toutes sortes de trucs futuristes de science-fiction que vous pouvez faire une fois que vous adoptez ce modèle de programmation.

Ethereum a permis la vague des ICO et des développeurs construisant sur la blockchain. C'est la deuxième plus grande cryptomonnaie derrière Bitcoin, elle a [plus de 10 fois](https://media.consensys.net/andrew-keys-ethereum-has-30-times-more-devs-than-the-next-blockchain-community-27980a5ddc09) le nombre de développeurs de la plateforme suivante la plus populaire, elle a la meilleure équipe de développeurs, les outils les plus matures, et la majorité des ICO et des projets sur elle. Elle a également le plus de [soutien de l'industrie](https://entethalliance.org/members/), ce qui compte beaucoup. Dans tous les cas, si vous faites du développement blockchain, vous écriverez probablement du code pour les contrats intelligents Ethereum. (Même si vous ne le faites pas, c'est essentiel pour comprendre ce qui se passe dans ce domaine.)

Tout d'abord, une explication plus détaillée de haut niveau d'Ethereum :

Les idées derrière Ethereum ont également engendré une vague d'innovation en [cryptoeconomie](https://www.youtube.com/watch?v=sbd4xe9OHJg). Vous devriez vous initier aux idées autour des [DAOs](https://en.wikipedia.org/wiki/Decentralized_autonomous_organization), et à tous les rêves de science-fiction qu'elles suggèrent.

D'accord, assez de fantaisie, plongeons dans la technologie.

Voici [un bon aperçu du livre jaune Ethereum et de ses internes](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369), par Preethi Kasireddy. Ethereum utilise un [modèle de compte](https://ethereum.stackexchange.com/questions/326/what-are-the-pros-and-cons-of-ethereum-balances-vs-utxos) plutôt que le modèle UTXO de Bitcoin — vous verrez bientôt pourquoi cela facilite l'écriture de contrats intelligents.

Comme pour toute technologie, la meilleure façon de se familiariser avec Ethereum est de construire quelques petits projets.

Le langage de programmation dominant pour Ethereum est Solidity, qui est un langage statique de type JavaScript. C'est un langage avec [beaucoup de verrues](https://news.ycombinator.com/item?id=14691212), et de nombreux choix de conception discutables. Des langages plus robustes comme [Viper](https://github.com/ethereum/vyper) pourraient le remplacer une fois qu'ils seront prêts pour la production, mais pour l'instant Solidity est la lingua franca de la programmation de contrats intelligents. C'est essentiellement le JavaScript d'Ethereum, donc vous devrez l'apprendre (et [ses pièges](https://medium.com/@aidobreen/how-and-why-developing-for-ethereum-sucks-1ff1a9873527)).

Pour votre première exposition au développement Solidity, je recommande de travailler sur l'ensemble du [tutoriel CryptoZombies](https://cryptozombies.io/). C'est un tutoriel de type Codecademy, agréable et de haute qualité, qui vous enseignera les bases de la programmation Solidity.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PIONSi0wfLn84tLh.png)

Maintenant que vous avez aiguisé votre appétit, il est temps de développer par vous-même.

Le "hello world" d'Ethereum est de construire un [jeton conforme ERC-20](https://medium.com/@james_3093/ethereum-erc20-tokens-explained-9f7f304055df). Je recommande [ce guide](https://enlight.nyc/ethereum-token) comme premier tutoriel pour vous guider à travers le processus.

[Remix](https://remix.ethereum.org/) est un éditeur et compilateur Solidity dans le navigateur — c'est essentiellement les roues d'entraînement du développement Ethereum, donc je recommande de continuer le reste de votre pratique dans Remix. Mais il est également utile de configurer une blockchain locale et de se familiariser avec les outils Ethereum. [Ce tutoriel](https://codeburst.io/build-your-first-ethereum-smart-contract-with-solidity-tutorial-94171d6b1c4b) fait un bon travail en vous guidant à travers une pile blockchain de bout en bout et en expliquant les pièces au fur et à mesure.

Ensuite, je recommande de construire un système de vote. J'appellerais cela le Todo App d'Ethereum. Karl Floersch a un [excellent tutoriel](https://karl.tech/learning-solidity-part-2-voting/) où il montre comment construire un système de vote sécurisé avec engagement et révélation.

Bien, maintenant pour votre examen de mi-parcours : construisez un jeu de pile ou face sécurisé, où deux joueurs peuvent parier en toute sécurité sur le lancer de pièce. Pas de tutoriel cette fois, faites-le par vous-même. Pensez aux attaques possibles — comment les joueurs peuvent-ils tricher ? Pouvez-vous vous assurer qu'ils jouent honnêtement ? [Voici quelques indices](https://gist.github.com/Haseeb-Qureshi/8261d70c4fb8ad8cdf1776f55bdcd4c2).

### Sécurité des contrats intelligents

La sécurité est absolument essentielle au développement blockchain. Les contrats intelligents ont été frappés par des piratages désastreux, y compris le [piratage de la DAO](http://hackingdistributed.com/2016/06/18/analysis-of-the-dao-exploit/), le [piratage du portefeuille Parity](https://medium.freecodecamp.org/a-hacker-stole-31m-of-ether-how-it-happened-and-what-it-means-for-ethereum-9e5dc29e33ce), et le [piratage du portefeuille Parity 2](https://hackernoon.com/parity-wallet-hack-2-electric-boogaloo-e493f2365303) (maintenant avec son propre [T-shirt](https://cryptoshirt.io/products/devops199-quote-i-accidentally-killed-it-tee)). Vous devez absolument lire les analyses de ces trois piratages si vous allez écrire des contrats intelligents de production.

La vérité est que **les contrats intelligents sont extrêmement difficiles à réussir**. Bien que la chaîne d'outils de programmation s'améliorera pour rendre ces attaques exactes plus difficiles, elles étaient finalement toutes dues à des erreurs de programmation. Il existe également de nombreux bugs plus subtils qui proviennent de la programmation de contrats intelligents, tels que le [frontrunning](https://hackernoon.com/front-running-bancor-in-150-lines-of-python-with-ethereum-api-d5e2bfd0d798) ou la [génération sécurisée d'aléatoire](http://www.swende.se/blog/Breaking_the_house.html).

En tant que développeur de contrats intelligents, vous devez traiter la sécurité comme primordiale. Il n'y a pas de "move fast and break things" dans la programmation de contrats intelligents. Cela signifie que tout code qui gère des flux importants d'argent doit être passé à travers des analyseurs statiques comme [Oyente](https://github.com/melonproject/oyente) ou [Securify](https://securify.ch/), testé minutieusement, puis audité par un auditeur expérimenté de contrats intelligents. Vous devriez également essayer de vous appuyer sur des composants pré-audités, tels que les [contrats open source d'OpenZeppelin](https://github.com/OpenZeppelin/zeppelin-solidity).

Pour renforcer vos compétences en sécurité, je recommande de travailler sur [The Ethernaut](https://ethernaut.zeppelin.solutions/) d'OpenZeppelin, un jeu où vous trouvez et attaquez des vulnérabilités dans les contrats intelligents. Beaucoup d'entre eux vous font reproduire des attaques réelles contre des contrats intelligents qui se sont produites dans la nature.

Phil Daian a également un excellent ensemble de défis de piratage de contrats intelligents appelés [Hack This Contract](http://hackthiscontract.io/).

Une fois que vous avez passé cela, je recommande fortement de lire l'intégralité des [Meilleures pratiques pour les contrats intelligents](https://consensys.github.io/smart-contract-best-practices/), compilées par ConsenSys. Prévoyez de revisiter ce document de nombreuses fois au cours de votre carrière de programmation de contrats intelligents. La [bibliographie](https://consensys.github.io/smart-contract-best-practices/bibliography/) vaut également la peine d'être explorée pour des lectures supplémentaires par des experts en sécurité.

### Enlever les roues d'entraînement

Si vous êtes arrivé à ce stade, vous devriez maintenant être prêt à passer de Remix et à commencer à utiliser une pile de développement Solidity sérieuse.

La plupart des développeurs recommandent VSCode ou Atom pour votre éditeur de texte, car ils ont de bons plugins Solidity. Pour interagir avec une blockchain locale, vous voudrez utiliser [Ganache](https://github.com/trufflesuite/ganache-cli) (anciennement TestRPC), et vous voudrez utiliser le [framework Truffle](https://github.com/trufflesuite/truffle) pour vos tests (basés sur JS) et configurer votre pipeline de construction.

Maintenant est un bon moment pour regarder [IPFS](https://ipfs.io/), que vous pouvez utiliser comme un magasin de fichiers entièrement décentralisé à un coût beaucoup moins élevé que la blockchain Ethereum. Voici un bref explicatif par le créateur, Juan Benet :

Pour interagir avec les nœuds complets Ethereum et [IPFS](https://ipfs.io/), [Infura](https://infura.io/) est ce que la plupart des développeurs recommandent. [Etherscan](https://etherscan.io/charts) et [ETH Gas Station](https://ethgasstation.info/) fournissent des statistiques en temps réel utiles sur le réseau Ethereum.

Une fois que vous avez configuré votre pile [Web3](https://blockchainhub.net/web3-decentralized-web/) complète, essayez de déployer une Dapp (application décentralisée) de bout en bout. [Ce tutoriel](https://happyfuncorp.com/whitepapers/webthereum) fournit un bon aperçu de la pile complète en utilisant Node et Postgres pour le backend, et [ce tutoriel](https://medium.com/@merunasgrincalaitis/the-ultimate-end-to-end-tutorial-to-create-and-deploy-a-fully-descentralized-dapp-in-ethereum-18f0cf6d7e0e) vous montrera comment créer une application entièrement décentralisée, en utilisant IPFS comme votre couche de persistance.

### Construire vos propres projets

Vous devriez maintenant être à l'aise avec la plupart de la technologie — ce qu'il reste, c'est de commencer à construire des choses et à aller plus loin dans la communauté blockchain.

Tout d'abord, commencez à construire vos propres projets. Si vous avez une idée géniale qui vous enthousiasme, allez la construire et convainquez les autres de travailler dessus avec vous ! Si vous n'avez pas encore d'idée ou si vous n'êtes pas à l'aise de vous salir les mains, il existe de nombreux projets open source de haute qualité qui accueillent les contributions. [OpenZeppelin](https://github.com/OpenZeppelin/zeppelin-solidity/issues) pourrait être un bon point de départ pour les contrats intelligents.

Mieux encore, je recommande de commencer par trouver un projet en développement actif dont vous êtes fan. Rejoignez leur Slack ou Rocketchat — les développeurs sont généralement facilement accessibles. Dites-leur que vous aimeriez contribuer et demandez quelques petites tâches (ou trouvez des problèmes non résolus sur leur Github).

Notez que bien que je me sois concentré sur les protocoles et le développement de contrats intelligents, les entreprises de blockchain ont besoin de développeurs web pour construire leurs fonctionnalités principales. Ces rôles nécessiteront souvent d'interagir avec les blockchains, il est donc essentiel d'avoir un bon modèle mental de leur fonctionnement — mais pour de nombreux ingénieurs dans les startups de blockchain, la majeure partie de votre travail consistera à construire un serveur web Python ou à concevoir un frontend React, et l'interaction avec la blockchain peut n'être qu'une petite partie de ce travail. Vous n'avez pas à vous spécialiser dans le développement de contrats intelligents — en réalité, ce n'est qu'une partie d'une pile blockchain fonctionnelle.

Au-delà des contributions open source, il y a aussi [de nombreux hackathons blockchain](https://www.hackathon.com/theme/blockchain) qui apparaissent constamment. La plupart des projets ont un Slack public gratuit que vous pouvez rejoindre, et il y a un [canal Gitter](https://gitter.im/ethereum/home) très actif pour Ethereum lui-même où beaucoup de développeurs traînent. À mesure que vous approfondissez le domaine, vous finirez par trouver votre groupe de pairs, que ce soit dans un canal Slack, un groupe Telegram ou un canal Gitter. Où que ce soit, trouvez vos gens et continuez à apprendre.

### Naviguer dans la communauté blockchain

La meilleure façon de vraiment comprendre le monde de la blockchain est de s'y immerger. Lisez et écoutez les personnes les plus intelligentes, surtout ce qu'elles ont écrit dans le passé. Cela a toujours été ma stratégie lorsque j'ai essayé d'apprendre un nouveau domaine, et cela m'a bien servi.

Il y a beaucoup de bon contenu blockchain, mais il y a aussi beaucoup de mauvais. Voici le régime d'information que je recommande.

#### Médias

Les trois excellents podcasts que je recommande sont les [interviews Blockchain de Software Engineering Daily](https://itunes.apple.com/us/podcast/blockchain-software-engineering-daily/id1230807219?mt=2), qui fournissent de bonnes introductions techniques à de nombreux sujets et cryptomonnaies. De là, je recommande [Epicenter](https://itunes.apple.com/us/podcast/epicenter-podcast-on-blockchain-ethereum-bitcoin-distributed/id792338939?mt=2) et [Unchained](https://itunes.apple.com/us/podcast/unchained-big-ideas-from-worlds-blockchain-cryptocurrency/id1123922160?mt=2) — vous voudrez revenir en arrière et écouter beaucoup des anciens épisodes. Un autre podcast technique intéressant et émergent est [Conspiratus](https://itunes.apple.com/us/podcast/conspiratus/id1335928646?mt=2). Je recommande de s'abonner à chacun d'eux.

Il y a quelques bonnes chaînes YouTube (bien qu'il y ait beaucoup de déchets sur YouTube). Abonnez-vous à la [Fondation Ethereum](https://www.youtube.com/channel/UCNOfzGXD_C9YMYmnefmPH0g/videos) et regardez les présentations de Devcon3. [Blockchain at Berkeley](https://www.youtube.com/channel/UC5sgoRfoSp3jeX4DEqKLwKg/videos) enregistre beaucoup de leurs conférences, dont la plupart sont d'excellents aperçus techniques. [Decypher Media](https://www.youtube.com/channel/UC8CB0ZkvogP7tnCTDR-zV7g/videos) publie également des discours, des revues de livres blancs et des tutoriels. [Jackson Palmer](https://www.youtube.com/channel/UCTOzxu_HvuJfZtTJ6AZ7rkA) propose des aperçus hebdomadaires engageants, ceux-ci sont moins techniques mais très bien présentés.

#### Lecture en ligne

Pour les discussions en temps réel sur la blockchain, elles se déroulent principalement en deux endroits : Reddit et Twitter. Pour Reddit, la plupart des subreddits sont de très mauvaise qualité et dominés par le bruit. [r/Ethereum](https://reddit.com/r/ethereum) est de qualité constamment décente (et il y a quelques subreddits corrects pour des cryptomonnaies spécifiques). La plupart des subreddits sont principalement dominés par des spéculateurs et ne sont pas une bonne utilisation de votre attention. Éloignez-vous des subreddits liés à Bitcoin. Bitcoin a notoirement l'une des communautés les plus toxiques, et Reddit ne fait qu'amplifier cela.

Twitter est un mélange plus varié. Pour le meilleur ou pour le pire, la plupart des gens de la blockchain vivent sur Twitter. Twitter Blockchain était un mystère pour moi au début, mais finalement j'ai développé une ontologie informelle des personnes de la blockchain sur Twitter. D'après mon expérience, il y a cinq types de personnalités de la blockchain : les constructeurs, les entrepreneurs, les journalistes, les traders et les "leaders d'opinion".

Évitez les "leaders d'opinion" comme la peste. Les entrepreneurs peuvent être corrects, bien qu'ils agissent principalement comme des hommes de hype ou tweetent sur leurs propres projets. Les investisseurs tweetent principalement sur les prix et les projets hypés, donc si c'est votre truc, c'est votre truc. Les journalistes ont tendance à tweeter sur les principaux événements de l'actualité — je recommande de rester à l'écart sauf si vous avez besoin d'une analyse en temps réel, ce qui n'est probablement pas le cas. Si vous êtes un trader actif, cela peut être important, mais si vous essayez de construire sur la blockchain, la plupart des choses en temps réel sont une distraction.

Accordez le plus d'attention aux constructeurs. Ce sont les personnes qui comptent le plus en ce moment, et qui font avancer la technologie.

Quelques représentants de chaque catégorie (faites une recherche en largeur de qui ces personnes suivent si vous voulez remplir votre fil Twitter) :

#### Constructeurs

* [Vitalik Buterin](https://twitter.com/VitalikButerin), Ethereum
* [Zooko Wilcox](https://twitter.com/zooko), ZCash
* [Nick Szabo](https://twitter.com/NickSzabo4), inventeur des contrats intelligents
* [Vlad Zamfir](https://twitter.com/VladZamfir), Ethereum
* [Marco Santori](https://twitter.com/msantoriESQ), Cooley LLP
* [Riccardo "fluffypony" Spagni](https://twitter.com/fluffypony), Monero
* [Matt Liston](https://twitter.com/malloc8), Gnosis

#### Entrepreneurs

* [Balaji Srinivasan](https://twitter.com/balajis), Earn.com
* [Erik Voorhees](https://twitter.com/ErikVoorhees), Shapeshift

#### Investisseurs

* [Naval Ravikant](https://twitter.com/naval), MetaStable
* [Ari Paul](https://twitter.com/AriDavidPaul), Blocktower Capital
* [Linda Xie](https://twitter.com/ljxie), Scalar Capital
* [Chris Burniske](https://twitter.com/cburniske), Placeholder

#### Journalistes

* [Tuur Demeester](https://twitter.com/TuurDemeester), Adamant Research
* [Laura Shin](https://twitter.com/laurashin), Forbes

(Vous devriez aussi [me suivre](https://twitter.com/hosseeb), bien que je ne mérite définitivement pas d'être sur cette liste.)

Tout cela dit, je recommande de minimiser votre exposition à Twitter et Reddit. Si vous n'êtes pas journaliste ou daytrader, il y a des chances que vous n'ayez pas besoin d'un flux continu de discussions en temps réel. Les informations importantes vous parviendront de manière asynchrone. Il existe plusieurs bonnes synthèses d'actualités qui résumeront les nouvelles les plus importantes du jour/de la semaine que vous pouvez consulter à votre propre rythme sans être à la merci des marchés de l'attention.

Je recommande de s'abonner à [Inside Bitcoin](https://inside.com/bitcoin) pour des synthèses quotidiennes des articles crypto les plus importants (il couvre plus que juste Bitcoin). Pour les projets de jetons, [Token Economy](https://tokeneconomy.co/tagged/token-economy-weekly?gi=2b9bd960ffe3) propose d'excellents comptes rendus hebdomadaires, et [Week in Ethereum](http://www.weekinethereum.com/) propose de bonnes synthèses des événements axés sur les développeurs dans l'écosystème Ethereum.

Au-delà de cela, vous n'avez probablement pas besoin de surveiller les actualités en temps réel. Concentrez-vous sur la construction de choses et l'apprentissage.

Vous voudrez suivre les meilleurs blogs. Le contenu long format tend à être le meilleur rapport qualité-prix. Je recommande de suivre ceux-ci :

* [Vitalik Buterin](http://vitalik.ca/) pour d'excellentes analyses blockchain et cryptoeconomiques (lisez tous ses [anciens articles de blog](https://blog.ethereum.org/author/vitalik-buterin/) également, Vitalik est largement considéré comme un penseur d'une génération)
* [Hacking, Distributed](http://hackingdistributed.com/) pour les analyses de sécurité blockchain par des chercheurs de Cornell
* [Unenumerated](http://unenumerated.blogspot.com/), le blog lumineux de Nick Szabo avec des essais stimulants et éclectiques sur le rôle des cryptomonnaies dans la société
* [Money Stuff](https://www.bloomberg.com/view/topics/money-stuff), la syndication Bloomberg de Matt Levine, avec des analyses tranchantes et perspicaces qui touchent à l'intersection des marchés, de la finance et des nouvelles blockchain
* [Vlad Zamfir](https://medium.com/@Vlad_Zamfir) pour des perspectives tempérées et prudentes sur l'état et les blockchains publiques
* [Chris Burniske](https://medium.com/@cburniske) pour une série d'excellents articles de blog sur la façon d'évaluer les actifs crypto
* [Jameson Lopp](https://lopp.net/articles.html) pour ses excellents articles techniques du point de vue d'un ingénieur logiciel construisant pour l'écosystème blockchain
* [Great Wall of Numbers](http://www.ofnumbers.com/) par Tim Swanson, pour sa déconstruction sobre et sans compromis de la frénésie blockchain, en particulier dans l'espace entreprise

([Vous devriez aussi lire mon blog](https://medium.com/@hosseeb), bien que, encore une fois, je ne mérite pas vraiment d'être sur cette liste.)

#### Livres et cours

Si vous voulez une approche plus structurée pour apprendre ce matériel, il existe quelques livres et cours de haute qualité (et beaucoup de mauvaise qualité).

Le meilleur manuel global pour les blockchains est [Bitcoin and Cryptocurrency Technologies](https://www.amazon.com/Bitcoin-Cryptocurrency-Technologies-Comprehensive-Introduction-ebook/dp/B01GGQJ2XW) (qui accompagne le cours Coursera de Princeton). Les seuls autres livres que je recommande dans ce domaine sont [Mastering Bitcoin](https://www.amazon.com/Mastering-Bitcoin-Unlocking-Digital-Cryptocurrencies/dp/1449374042) d'Andreas Antonopoulos, et son prochain [Mastering Ethereum](https://www.amazon.com/dp/1491971940/ref=sspa_dk_detail_4?psc=1&pd_rd_i=1491971940&pd_rd_wg=H2ulM&pd_rd_r=ZPCG322TAK47SRYV69QP&pd_rd_w=fqSI4), co-écrit par le cofondateur d'Ethereum Gavin Wood (tous deux publiés par O'Reilly). Le seul livre non technique que je recommande est [Digital Gold](https://www.amazon.com/Digital-Gold-Bitcoin-Millionaires-Reinvent/dp/B00UVY508W) de Nathaniel Popper. Pratiquement tout le reste qui vaut la peine d'être lu se trouvera dans des blogs, pas dans des livres — ce domaine évolue si rapidement que les figures les plus importantes ont rarement le temps d'écrire des livres, et les livres sont souvent obsolètes au moment où ils sont publiés.

Si vous voulez une approche plus structurée pour apprendre ce matériel, il existe quelques cours de haute qualité (et beaucoup de mauvaise qualité). J'ai déjà lié quelques conférences du [Cours Coursera de Princeton](https://www.coursera.org/learn/cryptocurrency) (les vidéos sont [sur Youtube](https://www.youtube.com/channel/UCNcSSleedtfyDuhBvOQzFzQ) également), et le [Decal de l'UC Berkeley](https://www.youtube.com/watch?v=ZWE3qFnSbMc&list=PLSONl1AVlZNX_JBggqZV40rDIGGB0FNHW). J'ai également entendu de bonnes choses sur [Consensys Academy](https://consensys.net/academy/) pour les personnes qui veulent se lancer dans le développement de contrats intelligents.

**Je donne également un [séminaire de 4 semaines sur les cryptomonnaies](https://bradfieldcs.com/courses/cryptocurrencies/) pour les développeurs de logiciels à la Bradfield School of Computer Science à SF.** Le cours est en personne uniquement à SF et les places sont limitées, car il s'agit d'une petite classe de type séminaire approfondi. Mais si vous êtes un ingénieur logiciel à SF et que vous souhaitez en savoir plus sur la théorie et la pratique derrière les cryptomonnaies, cela pourrait être un bon choix pour vous.

### Trouver un emploi

Comme je l'ai dit auparavant, les startups de blockchain embauchent comme des folles. Si vous êtes réellement arrivé à ce stade et que vous avez fait même la moitié des choses que j'ai suggérées, vous êtes probablement déjà employable dans ce domaine. AngelList a fait un [excellent article](https://angel.co/talent-hacks/how-to-get-a-job-at-a-crypto-startup) sur la façon d'obtenir un emploi dans l'espace crypto.

Il existe plusieurs bons agrégateurs pour les offres d'emploi liées à la blockchain :

* [Startups crypto sur AngelList](https://angel.co/bitcoin/jobs)
* [BlockchainJobz](http://blockchainjobz.com/)
* [Emplois Ethereum](https://jobs.ethercasts.com/)
* [Be in Crypto](https://beincrypto.com/)
* [Tableau d'affichage des emplois Blockchain](http://www.blockchainjobboard.org/)
* [Liste des emplois Crypto](https://cryptojobslist.com/)
* [Emplois Google (requête de recherche blockchain)](https://www.google.com/search?q=blockchain+jobs&ibp=htl;jobs#fpstate=tldetail)
* [Emplois ConsenSys](https://new.consensys.net/careers/) (studio de capital-risque Ethereum avec de nombreux projets sous leur égide)

Quelques startups blockchain particulièrement prometteuses que je connais et qui embauchent des développeurs :

* [0x](https://angel.co/0xproject/jobs)
* [Dharma Labs](https://angel.co/dharma-labs)
* [Civic](https://angel.co/civic/jobs)

Il y a aussi un certain nombre de grandes entreprises sur le marché pour les développeurs crypto :

* [Coinbase](https://www.coinbase.com/careers), le Google de la crypto, embauche toujours comme des folles
* [Stellar](https://jobs.lever.co/stellar) et [Ripple](https://ripple.com/company/careers/all-jobs/) si vous voulez travailler directement sur des cryptomonnaies plus adaptées aux entreprises
* [Square](https://squareup.com/careers/jobs) a intégré une certaine blockchain, bien que je ne sois pas sûr s'ils embauchent en externe
* [IBM](https://www.glassdoor.com/Jobs/IBM-blockchain-Jobs-EI_IE354.0,3_KO4,14.htm), [Visa](https://jobs.smartrecruiters.com/Visa/743999653819658-blockchain-engineer), ou [JP Morgan](https://lensa.com/software-engineer-for-blockchain-distributed-ledger-technology-jobs/jersey-city/jd/7280746400698a76062d0e6f31e57256) si vous voulez rester à l'ancienne école

(Notez que cette liste spécifique d'entreprises est très centrée sur la région de la Baie, car c'est là que je vis, donc votre expérience peut varier. Les agrégateurs d'emplois sont plus globaux.)

Mais à mon avis, la meilleure façon de s'impliquer dans une entreprise est de trouver un projet qui vous enthousiasme et de les contacter directement. La plupart des équipes de blockchain sont prêtes à embaucher à distance pour le bon talent. De nombreux développeurs sont facilement accessibles sur Twitter, Github ou sur leurs chaînes Slack publiques. Si vous avez un portfolio solide et pouvez démontrer des compétences techniques, la plupart des gens seront impressionnés si vous montrez un peu d'initiative.

Et c'est aussi loin que je peux vous emmener. Si vous avez fait tout ce qui précède, vous devriez être prêt, et vous serez probablement encore plus avancé que moi avant longtemps.

### Le terrier du lapin

Ce que je vous ai montré n'est que le début. Les cryptomonnaies en sont encore à leurs balbutiements, et je crois vraiment que c'est l'espace évoluant le plus rapidement dans lequel vous pouvez travailler. Je suis sûr que ce guide sera obsolète dans un an, et il y a tant de projets incroyables dont je n'ai pas eu l'occasion de parler. Mais si vous entrez dans cet espace, vous les trouverez en temps voulu.

Continuez à explorer. Continuez à vous améliorer. Continuez à apprendre.

Et j'espère vous voir nous rejoindre.

_Haseeb_