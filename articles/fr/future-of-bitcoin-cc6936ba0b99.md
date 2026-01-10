---
title: Ce que vous devez savoir sur l'avenir de la technologie Bitcoin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-02T21:34:27.000Z'
originalURL: https://freecodecamp.org/news/future-of-bitcoin-cc6936ba0b99
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FfRqOEiRKdgvnbuvEgQF6g.jpeg
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: business
  slug: business
- name: finance
  slug: finance
- name: technology
  slug: technology
seo_title: Ce que vous devez savoir sur l'avenir de la technologie Bitcoin
seo_desc: 'By Subhan Nadeem

  Bitcoin (BTC) recently smashed an all-time high of $11,400 USD and subsequently
  dropped to as low as $8,595 within a few hours. It’s incredibly important to not
  get lost in the pandemonium and to stay informed about how Bitcoin is pr...'
---

Par Subhan Nadeem

Bitcoin (BTC) a récemment pulvérisé un record absolu de 11 400 USD avant de chuter à 8 595 USD en quelques heures. Il est incroyablement important de ne pas se perdre dans la pandémonium et de rester informé sur la progression technologique de Bitcoin.

Toute personne envisageant d'acheter des Bitcoins devrait au moins apprendre deux choses :

1. l'histoire de la technologie derrière Bitcoin
2. et plus important encore, ce qui attend Bitcoin dans le futur.

Comme le dit l'expert Bitcoin [Andreas M. Antonopoulos](https://www.freecodecamp.org/news/future-of-bitcoin-cc6936ba0b99/undefined), « [Investissez dans l'éducation plutôt que dans la spéculation](https://www.youtube.com/watch?time_continue=328&v=6uXAbJQoZlE). »

Étant donné que Bitcoin et sa blockchain sous-jacente sont des concepts technologiques incroyablement nouveaux, il peut sembler intimidant d'essayer de rechercher et de comprendre ses détails techniques sous-jacents. Cet article est écrit dans le but de mettre en lumière le problème de scalabilité auquel Bitcoin est confronté, et quelles sont les solutions attendues ou proposées à ce problème. Il existe des solutions vraiment excitantes que cet article discute !

J'ai écrit cela alors que j'apprenais moi-même Bitcoin, pour agréger la grande quantité d'informations sur l'avenir de Bitcoin provenant de nombreuses sources. En écrivant cela, j'ai gardé à l'esprit même ceux qui ne possèdent pas de formation en programmation. Cependant, il est supposé que le lecteur a une compréhension très basique de Bitcoin en tant que monnaie et de ce qu'est une blockchain. Coindesk a un excellent article de 5 minutes qui devrait vous mettre à jour [ici](https://www.coindesk.com/information/what-is-bitcoin/) si vous débutez avec Bitcoin ou si vous avez besoin d'un rappel.

Commençons par le problème de scalabilité auquel Bitcoin est confronté.

### **Le problème de débit des transactions**

Lorsque Bitcoin a été introduit pour la première fois dans le monde, son créateur Satoshi Nakomoto a décrit Bitcoin dans le [livre blanc de Bitcoin](https://bitcoin.org/bitcoin.pdf) comme « Une version purement pair-à-pair de l'argent électronique permettrait d'envoyer des paiements en ligne directement d'une partie à une autre sans passer par une institution financière. »

L'une des valeurs fondamentales de Bitcoin était les transactions de paiement instantanées et sécurisées de pair à pair. Maintenant, plus que jamais, Bitcoin émerge comme la cryptomonnaie dominante sur le marché mondial, avec une augmentation de valeur de plus de 1 200 % au cours de la dernière année seule.

En raison de cette croissance sans précédent, le nombre de transactions sur la blockchain Bitcoin a également augmenté, avec jusqu'à [400 000 transactions par jour](https://blockchain.info/charts/n-transactions) étant effectuées. Cette augmentation rapide des transactions pose un sérieux problème de scalabilité pour la blockchain, avec [plus de 90 000 transactions](https://blockchain.info/unconfirmed-transactions) étant en attente de confirmation à l'heure actuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/m1XCF1AdMMjgWci2o6kSeZc7cbza6Jx5qqEx)
_Alors que le prix de Bitcoin s'envole, son utilisation aussi. Notez la stagnation à environ 400 000 transactions par jour_

Pour comprendre pourquoi les transactions sont en attente, les transactions Bitcoin doivent d'abord être expliquées.

Chaque fois qu'un utilisateur envoie une transaction Bitcoin de son portefeuille à un autre, la transaction est ajoutée au **memory pool** (mempool), qui est essentiellement un pool de toutes les transactions non confirmées dans le réseau Bitcoin. Ce pool est maintenu par des pools de mémoire individuels sur des machines qui détiennent également une copie du registre de la blockchain, appelés **nœuds**.

À partir du mempool, les mineurs sélectionnent les transactions qu'ils souhaitent vérifier. Une fois que les mineurs valident une transaction (c'est-à-dire confirment que l'expéditeur a effectivement assez de bitcoins à envoyer au destinataire), ils l'ajoutent à un nouveau bloc, qui est finalement publié sur la blockchain. D'autres nœuds parcourent ensuite les transactions de ce nouveau bloc publié pour s'assurer que le bloc est valide, avant d'accepter le bloc comme faisant partie de son registre.

![Image](https://cdn-media-1.freecodecamp.org/images/q66a8vy5M3q75z3HZY9r9mqhDkkVa5pY8Y6F)
_Un diagramme du cycle de vie des transactions, source : [weusecoins.com](https://www.weusecoins.com/en/questions/" rel="noopener" target="_blank" title=")_

Calculons le débit des transactions :

* La taille médiane des transactions est d'environ [250 octets](https://tradeblock.com/blog/analysis-of-bitcoin-transaction-size-trends)
* La taille d'un bloc est limitée à 1 Mo (1 000 000 octets)
* Ainsi, un bloc contient environ 4 000 transactions (1 Mo divisé par 250 octets)
* Un bloc ne peut être publié sur la blockchain qu'une fois toutes les 10 minutes en moyenne (600 secondes).
* 4 000 transactions (au maximum) sont publiées toutes les 600 secondes, à un rythme de **6,66 transactions / seconde**

Avec plus de 90 000 transactions non confirmées dans le mempool, comment un mineur sélectionne-t-il les transactions à vérifier ? Les frais de transaction ! L'expéditeur d'une transaction a la possibilité d'ajouter des frais de transaction personnalisés à sa transaction destinés au mineur, incitant un mineur à sélectionner la transaction et à la faire vérifier plus rapidement. Les mineurs sélectionneront les transactions qui ont les frais les plus élevés qui y sont attachés afin de maximiser les profits. Théoriquement, vous pouvez envoyer une transaction sans frais. Mais s'il y a des transactions qui ont des frais plus élevés que les vôtres dans le pool, pourquoi la vôtre serait-elle jamais sélectionnée ?

Alors que la base d'utilisateurs de Bitcoin grandit, les frais de transaction moyens augmentent également. Au maximum, il n'y a que 7 transactions qui sont traitées chaque seconde et tout le monde veut que sa transaction soit vérifiée en premier. À l'heure actuelle, les frais de transaction moyens sont d'environ [3,58 USD](https://bitinfocharts.com/comparison/bitcoin-median_transaction_fee.html). Ces frais ne sont certainement pas idéaux — si vous voulez envoyer à un ami quelques dollars en bitcoin, vous pourriez finir par dépenser plus en frais de transaction que la valeur de la transaction elle-même ! Là réside le problème, et si tout reste égal, les frais de transaction peuvent être amenés à augmenter en raison du goulot d'étranglement des transactions.

### **Résoudre le problème de débit**

Une solution proposée à ce goulot d'étranglement qui a suscité une grande controverse au sein de la communauté Bitcoin est de simplement augmenter la taille des blocs à partir de la limite initiale de 1 Mo, permettant ainsi plus de transactions par bloc.

Chaque fois que la taille des blocs est augmentée dans la chaîne, un **hard fork** est nécessaire, ce qui signifie qu'une nouvelle copie de la chaîne doit être créée, nécessitant donc un consensus de la communauté Bitcoin. Parce que des millions de personnes utilisent Bitcoin, obtenir un consensus est difficile et des efforts doivent être faits pour l'éviter. De plus, bien que la taille des blocs puisse être augmentée suffisamment pour accommoder l'arriéré actuel de transactions, à mesure que la base d'utilisateurs de Bitcoin continue de croître, il y aura finalement un autre arriéré de transactions non confirmées, donc une autre augmentation de la taille des blocs sera nécessaire, et ensuite un autre hard fork.

Alors pourquoi ne pas simplement rendre la taille des blocs suffisamment grande pour garantir que le débit ne sera jamais un goulot d'étranglement, peu importe le nombre de personnes qui l'utilisent ? Premièrement, les mathématiques d'une taille de bloc suffisamment grande pour gérer une adoption de masse sont impraticables et limiteront l'exploitation minière à des machines incroyablement puissantes que seules les grandes entreprises pourront maintenir, introduisant un élément de centralisation.

![Image](https://cdn-media-1.freecodecamp.org/images/ECmTOfKD1GulkUvxK75hXDY-bfSxV47U5XZS)
_Étant donné une taille de bloc suffisamment grande pour la population d'une seule ville, cela limiterait l'hébergement de nœuds et l'exploitation minière à ceux qui possèdent les machines les plus puissantes, c'est-à-dire les grandes entreprises, source : [Lightning Network](https://lightning.network/lightning-network.pdf" rel="noopener" target="_blank" title=")_

De plus, rappelez-vous que une fois qu'un bloc est miné, tous les autres nœuds doivent valider le bloc avant de l'accepter. Si la taille du bloc était incroyablement grande et que quelqu'un publiait un bloc invalide, les nœuds gaspilleraient une grande quantité de temps à tenter de valider le bloc avant de le rejeter comme invalide et de passer au bloc suivant. Une attaque par déni de service peut essentiellement être orchestrée en publiant répétitivement des blocs invalides extrêmement grands sur le réseau, empêchant les blocs valides d'être traités pendant une longue période. Comme l'a déclaré le pionnier de la blockchain Nick Szabo dans [cette interview](https://medium.com/@giftedproducts/cryptocurrencies-with-tim-ferriss-nick-szabo-and-naval-ravikant-51a99d037e04), la petite taille des blocs agit comme un paramètre de sécurité technique pour prévenir l'inondation du réseau.

Vous pouvez en lire plus sur l'impact complet d'une augmentation de la taille des blocs si Bitcoin devait prendre le contrôle du monde, dans un article que j'ai écrit [ici](https://hackernoon.com/if-we-lived-in-a-bitcoin-future-how-big-would-the-blockchain-have-to-be-bd07b282416f).

Si nous ne pouvons pas augmenter la taille des blocs, que pouvons-nous faire ? Heureusement, il existe plusieurs solutions en cours de développement qui devraient être déployées afin de résoudre ce problème.

### **Segregated Witness (SegWit)**

Segregated Witness (SegWit) a en fait déjà été implémenté dans le réseau Bitcoin, depuis août 2017. C'est un changement fondamental du réseau qui modifie le format des transactions, les rendant essentiellement plus petites en taille, et permettant à plus de transactions de tenir dans un bloc, ce qui augmente le débit. SegWit est considéré comme un **soft fork**, ce qui signifie qu'il est complètement rétrocompatible avec le protocole Bitcoin existant, bien que les nœuds et les portefeuilles doivent être mis à jour pour tirer parti de toutes les fonctionnalités de SegWit.

Chaque transaction a une signature de l'expéditeur, ou en d'autres termes, des **données de témoin** ; cela représente généralement la plus grande partie de la transaction. Ces données ne sont pas réellement nécessaires pour vérifier la transaction, et donc SegWit déplace ces données à la fin de la transaction, les _séparant_. Si cette transaction est envoyée à un nœud hérité (un nœud qui n'a pas été mis à jour vers SegWit), le nœud supprime les données de témoin de la fin de la transaction avant de l'insérer dans un bloc, réduisant ainsi la taille globale de la transaction et économisant de l'espace. L'avantage supplémentaire de cela est que les nœuds ne peuvent plus modifier les données de témoin, changeant ainsi l'expéditeur de la transaction, une capacité que les nœuds avaient auparavant. Cela ouvre la voie à l'implémentation de solutions multi-couches que nous discuterons bientôt. Les utilisateurs économisent également sur les frais de transaction, car ils sont généralement calculés par octet de transaction, et SegWit réduit la taille totale de la transaction.

![Image](https://cdn-media-1.freecodecamp.org/images/RQWDpa1anH8EhImUStwrg2um6WGO4Mybsn6w)
_SegWit déplace les données de signature à la fin de la transaction, après quoi elles sont supprimées avant d'être stockées dans un bloc, source : [Programming Blockchains](https://programmingblockchain.gitbooks.io/programmingblockchain/content/other_types_of_ownership/p2wpkh_pay_to_witness_public_key_hash.html" rel="noopener" target="_blank" title=")_

De plus, SegWit change la définition d'un bloc : au lieu qu'un bloc soit défini en termes d'octets, il est maintenant défini en termes de « poids » ; un bloc peut avoir un poids maximum de 4 000. Les transactions héritées ont un poids de 4, tandis que les transactions SegWit ont un poids de 0,25, permettant ainsi à un bloc de contenir beaucoup plus de transactions SegWit et d'avoir une taille légèrement plus élevée (environ 2 mégaoctets au maximum). Les nœuds doivent être mis à jour vers SegWit pour suivre cette définition, et les portefeuilles doivent incorporer SegWit afin d'envoyer des transactions SegWit. En conséquence, l'adoption de SegWit a été lente, représentant seulement 12 % du trafic actuel.

![Image](https://cdn-media-1.freecodecamp.org/images/RssMxAEgr5MxnLkR4SCSXEHhBi9ZuPzeU-oG)
_L'état actuel de l'adoption de SegWit oscille autour de 12 % de toutes les transactions, source : [segwit.party](http://segwit.party/charts/" rel="noopener" target="_blank" title=")_

En raison des avantages mentionnés ci-dessus de SegWit, j'encourage vivement toute personne lisant ceci à utiliser des portefeuilles qui ont incorporé SegWit pour accélérer l'adoption de SegWit. Une liste soignée d'entre eux peut être trouvée [ici](https://bitcoincore.org/en/segwit_adoption/) (mon préféré personnel est [Samourai Wallet pour Android](https://samouraiwallet.com/)). Si vous souhaitez en savoir plus sur les intrications de SegWit, [Jimmy Song](https://www.freecodecamp.org/news/future-of-bitcoin-cc6936ba0b99/undefined) a écrit un excellent article à ce sujet :

[**Comprendre la taille des blocs Segwit**](https://medium.com/@jimmysong/understanding-segwit-block-size-fd901b87c9d4)  
[_Après avoir écrit mon dernier article, j'ai été surpris par la protestation concernant la partie 2 Mo du titre (le titre a depuis été
..._medium.com](https://medium.com/@jimmysong/understanding-segwit-block-size-fd901b87c9d4)

### **Solutions multi-couches**

En l'état actuel des choses, la blockchain Bitcoin n'est pas très adaptée aux micropaiements. Si vous voulez acheter une tasse de café de 2 $, vous allez probablement payer plus de 2 $ équivalent en BTC en frais de transaction, et la transaction ne sera pas confirmée instantanément — vous devez attendre que la transaction soit publiée dans un bloc vérifié sur la chaîne, ce qui apparaîtra dans les 10 minutes au mieux.

Les solutions de deuxième et troisième couche sont des réseaux superposés à la blockchain Bitcoin qui permettent aux utilisateurs d'envoyer plusieurs transactions de petites quantités de Bitcoin presque instantanément, sans frais de transaction.

**Le Lightning Network** est ce réseau en couches actuellement en développement, censé atténuer les problèmes de scalabilité de Bitcoin. Ce réseau se compose de deux couches supplémentaires et permet aux utilisateurs d'ouvrir des canaux directs entre eux pour envoyer un nombre effectivement illimité de paiements les uns aux autres de manière instantanée.

[**Lightning Network**](https://lightning.network/)  
[_Le Lightning Network dépend de la technologie sous-jacente de la blockchain. En utilisant de vrais Bitcoin/blockchain
..._lightning.network](https://lightning.network/)

#### La deuxième couche

Un utilisateur rejoint le réseau de deuxième couche en effectuant une transaction sur la blockchain qui déclare que l'utilisateur engage une certaine quantité de bitcoin à utiliser dans le réseau en couches. L'utilisateur rejoint ensuite un groupe de nœuds interconnectés les uns aux autres, appelés **usines de canaux**. Ces nœuds maintiennent essentiellement un lobby d'individus qui souhaitent potentiellement effectuer des transactions entre eux. Les usines de canaux permettent ensuite la création d'un nombre illimité de canaux de micropaiement sur la troisième couche (d'où le nom d'usines) entre des parties individuelles.

![Image](https://cdn-media-1.freecodecamp.org/images/qAGFrJUk1ARYlpbaAplzwIhEEpBu0asvsL-c)
_D'après le [livre blanc](https://www.tik.ee.ethz.ch/file/a20a865ce40d40c8f942cf206a7cba96/Scalable_Funding_Of_Blockchain_Micropayment_Networks%20(1).pdf" rel="noopener" target="_blank" title="): les utilisateurs sont connectés à une usine de canaux lors de la connexion au réseau, qui alloue ensuite plusieurs canaux de micropaiement_

#### La troisième couche

Les canaux de micropaiement sont configurés pour garantir des paiements directs entre deux utilisateurs sur la troisième couche. Comme la blockchain n'est plus présente dans cette couche, elle ne peut pas être utilisée pour valider les transactions et garantir qu'une partie a payé l'autre. Au lieu de cela, la technologie des contrats intelligents est employée, telle que les **adresses multisig**, ce qui signifie des adresses qui peuvent être signées par plusieurs utilisateurs pour permettre le mouvement de fonds, et les **contrats à verrouillage temporel haché**, qui sont des contrats automatisés cryptographiquement sécurisés qui verrouillent les fonds pendant une certaine période pour garantir qu'une partie ne peut pas tricher avec une autre. Ces technologies éliminent le besoin de confiance entre les utilisateurs connectés dans les canaux de micropaiement.

Voici un exemple de fonctionnement d'un canal de micropaiement du Lightning Network :

1. Alice souhaite dédier 1 Bitcoin à un canal de micropaiement entre Bob. Elle déclare que ce 1 Bitcoin sera utilisé dans une **transaction d'engagement** sur la blockchain Bitcoin. Ce 1 Bitcoin est ensuite verrouillé dans une **adresse multisig** que les deux parties peuvent signer si elles souhaitent fermer le canal. Cette adresse est sécurisée avec un **contrat à verrouillage temporel haché** qui stipule : « Alice a 1 BTC et Bob a 0 BTC, à libérer dans une heure ». Cela signifie que le 1 Bitcoin d'Alice est verrouillé pendant 1 heure, après quoi il sera retourné à Alice et publié à nouveau sur la blockchain Bitcoin.
2. Alice décide ensuite de donner 0,1 BTC à Bob. Cette transaction est enregistrée avec un nouveau contrat à verrouillage temporel haché stipulant : « Alice a 0,9 BTC et Bob a 0,1 BTC, à expirer dans 50 minutes ». Ce contrat a une durée d'expiration de 50 minutes, ce qui signifie qu'il sera publié sur la blockchain avant le contrat original stipulant qu'Alice a 1 BTC. Par conséquent, Bob sait instantanément qu'il a les 0,1 BTC car ce nouveau contrat sera publié sur la blockchain avant le contrat original, rendant ainsi l'ancien contrat invalide.
3. Une fois l'heure complète écoulée, le canal de micropaiement se ferme et le solde final entre Alice et Bob est publié sur la blockchain. Si Alice et Bob souhaitent continuer à effectuer des transactions, ils peuvent prolonger la durée d'expiration de leur canal aussi longtemps qu'ils le souhaitent. Si l'un d'eux souhaite fermer le canal plus tôt, l'un d'eux doit signer l'adresse multisig originale dans laquelle le Bitcoin est stocké.

Le réseau permet aux transactions de se router elles-mêmes vers leur destination finale en utilisant d'autres utilisateurs connectés dans le canal comme intermédiaires. Cela peut se produire même si une connexion directe à l'utilisateur souhaité n'est pas possible dans le canal de micropaiement actuel. Par exemple, si Alice a un canal ouvert avec Bob, et Bob a un canal avec Mark, et Alice veut envoyer des Bitcoins à Mark, le réseau peut router le paiement à Mark via Bob, tout en garantissant qu'aucune partie n'a à faire confiance à une autre.

![Image](https://cdn-media-1.freecodecamp.org/images/eP3V3chCxIuojC--P0bztS60medVbfOkZh3u)
_Dans le réseau Lightning, les transactions sont routées via des utilisateurs intermédiaires afin d'atteindre leur destination finale_

L'implémentation des transactions du réseau Lightning et leur nature sans confiance peut devenir incroyablement complexe, et est mieux expliquée par les développeurs de Lightning dans [cette conférence](https://www.youtube.com/watch?v=8zVzw912wPo) ou dans la série suivante par [ecurrencyhodler](https://www.freecodecamp.org/news/future-of-bitcoin-cc6936ba0b99/undefined) :

[**Le Lightning Network (Partie 1)**](https://medium.com/the-litecoin-school-of-crypto/a-primer-to-the-lightning-network-part-1-be909c403bde)  
[_Adresses multisig : les blocs de construction du Lightning Network_medium.com](https://medium.com/the-litecoin-school-of-crypto/a-primer-to-the-lightning-network-part-1-be909c403bde)

Idéalement, un utilisateur ne créera qu'une transaction d'engagement vers la couche secondaire très rarement, car il ou elle restera dans le réseau en couches pendant de longues périodes pour effectuer la plupart de ses transactions quotidiennes. Une fois qu'un utilisateur souhaite quitter ce réseau multi-couches, une **transaction de règlement** est effectuée sur la blockchain, déclarant le solde final de Bitcoin de l'utilisateur après toutes les activités de la deuxième couche. Cela reconcilie leur solde total de Bitcoin sur la blockchain après comparaison avec la transaction d'engagement originale. Au total, seules deux transactions de blockchain sont effectuées afin de permettre à l'utilisateur d'effectuer un nombre illimité de transactions gratuitement sur la deuxième couche.

Comme mentionné précédemment, SegWit ouvre la voie au réseau Lightning car il supprime la capacité des nœuds à modifier les données de témoin, qui sont utilisées pour identifier l'entrée d'un utilisateur dans la deuxième couche. Si la transaction d'engagement de l'utilisateur ne peut pas être trouvée parce que les données de témoin faisant référence à l'utilisateur ont été modifiées, il y a un niveau de difficulté plus élevé impliqué lors de la tentative de réconciliation de la transaction de règlement de l'utilisateur.

La deuxième couche du réseau Lightning impliquant les usines de canaux a été très récemment introduite dans [ce livre blanc](https://www.tik.ee.ethz.ch/file/a20a865ce40d40c8f942cf206a7cba96/Scalable_Funding_Of_Blockchain_Micropayment_Networks%20(1).pdf). Elle est encore en développement intensif, donc beaucoup de ses concepts sont expliqués de manière abstraite. Cependant, le réseau est sur le point d'être lancé en 2018 et sera de loin la plus grande amélioration de la scalabilité des transactions à ce jour.

### **Signatures Schnorr**

Lorsque un utilisateur envoie une transaction Bitcoin, les entrées de la transaction (le montant que vous envoyez) sont calculées simplement en récupérant de la blockchain les montants non dépensés totaux de Bitcoin que vous avez précédemment reçus. Par exemple :

* En commençant avec un portefeuille vide, je reçois 1 Bitcoin dans la transaction #1, puis un autre 1 Bitcoin dans une transaction séparée #2
* Je veux maintenant envoyer 2 Bitcoins dans une transaction. Il y aura deux entrées pour cette transaction : la transaction #1, et la transaction #2, totalisant 2 Bitcoin

Avec l'algorithme actuel de génération de signatures (Elliptic Curve Digital Signature Algorithm), chaque entrée nécessite sa propre signature. Cela augmente la taille totale de la transaction et donc les frais de transaction.

![Image](https://cdn-media-1.freecodecamp.org/images/SXBrtQeJUNd--9Vh5s7jHj6pdOqylGDosB01)
_Actuellement, chaque entrée nécessite une signature, augmentant la taille totale de la transaction_

Les [signatures Schnorr](https://bitcoincore.org/en/2017/03/23/schnorr-signature-aggregation/) sont une alternative et une méthode plus efficace de stockage des données de signature dans les transactions. Toutes les entrées sont accumulées puis stockées sous forme de signature unique en utilisant l'algorithme Schnorr, ce qui permet d'économiser considérablement de l'espace dans une transaction et aide à augmenter le débit des transactions en permettant aux blocs de stocker plus de transactions en moyenne.

![Image](https://cdn-media-1.freecodecamp.org/images/caYd8iXKfgyxSJxDEmRIXnZ1KwZx37kZhF2Y)
_Toutes les signatures de l'expéditeur sont stockées sous forme de signature unique selon l'algorithme Schnorr_

Les signatures Schnorr peuvent également être utilisées pour aider à l'avancement de Bitcoin en matière de confidentialité en bénéficiant aux transactions CoinJoin. CoinJoin est une méthode d'introduction de l'anonymat dans les transactions Bitcoin. Elle fonctionne en regroupant les entrées de transaction avec celles d'autres personnes lors de l'envoi d'un paiement à un destinataire. Lorsque les paiements sont regroupés, il devient difficile de suivre quel utilisateur a envoyé quelle entrée, les rendant ainsi effectivement anonymes. Cependant, les transactions CoinJoin ont des frais accrus en raison d'un nombre plus élevé d'entrées dans une seule transaction, entraînant un nombre plus élevé de signatures. L'utilisation de signatures Schnorr permettrait de compresser toutes les signatures d'une transaction en une seule, économisant ainsi considérablement sur les frais de transaction et encourageant l'utilisation de CoinJoin.

De plus, Schnorr ouvre la voie à des transactions multisig complexes qui nécessitent la signature de plusieurs parties ; peu importe le nombre de signatures de parties nécessaires pour une transaction, tout ce dont la transaction a besoin est une signature Schnorr.

Les signatures Schnorr ne sont désormais possibles que grâce à l'implémentation de SegWit ; car les données de signature ne peuvent pas être modifiées par des tiers, elles peuvent désormais être utilisées pour créer efficacement une signature Schnorr.

### **MimbleWimble**

MimbleWimble est un changement radical mais incroyablement puissant proposé à l'architecture Bitcoin qui a été introduit anonymement à travers ce [livre blanc](https://download.wpsoftware.net/bitcoin/wizardry/mimblewimble.txt) en juillet 2016.

Nommé d'après le [sortilège de ligotage de langue de la série Harry Potter](http://harrypotter.wikia.com/wiki/Tongue-Tying_Curse), son objectif est de supprimer entièrement les transactions des blocs. Sous MimbleWimble, les transactions ne consistent en rien d'autre que des montants d'entrée, des montants de sortie et une signature. La signature de la transaction ne peut être décryptée que par le destinataire, et donc la vérification de la transaction est laissée au destinataire.

Par extension, les blocs ne consistent qu'en la liste de tous les montants d'entrée de transaction de toutes les transactions, tous les montants de sortie de transaction et leurs signatures correspondantes. Les blocs peuvent ensuite être fusionnés de manière transparente avec les blocs précédents, car ils ne sont rien d'autre que des paires de montants d'entrée et de sortie. Les nœuds ont alors la capacité de garantir cryptographiquement que les transactions dans les blocs ne créent pas de bitcoins supplémentaires (c'est-à-dire que leur différence nette entre les entrées et les sorties dans les blocs est de 0) sans avoir à décrypter les transactions.

Cette suppression du stockage des transactions accorde une anonymat complet à tous les utilisateurs en supprimant la capacité de générer l'historique des transactions. De plus, avec les blocs ne contenant que les **sorties de transaction non dépensées** (ce qui signifie le nombre de Bitcoins qui ont été reçus dans une adresse mais pas encore déplacés), la taille de la blockchain peut être réduite de plus de 60 % selon le livre blanc. Cette réduction de taille signifie que pour valider une blockchain MimbleWimble, les nœuds n'auront besoin de regarder que l'ensemble des sorties de transaction non dépensées au lieu de l'ensemble des transactions, ce qui augmentera exponentiellement les performances.

Les détails mathématiques de MimbleWimble sont hors de la portée de cet article, mais sont expliqués en détail dans le [livre blanc](https://scalingbitcoin.org/papers/mimblewimble.txt). Bien que MimbleWimble présente certains avantages clairs et des percées techniques, son implémentation nécessite la suppression du système de script de Bitcoin sur lequel une grande partie de l'architecture existante repose. Par conséquent, l'implémentation de MimbleWimble sur la blockchain Bitcoin n'est pas techniquement réalisable.

Cependant, il existe des propositions pour que MimbleWimble existe en tant que **sidechain**. Une sidechain est une blockchain séparée directement attachée à la blockchain Bitcoin par l'utilisation d'un ancrage à double sens. Cet ancrage permet l'échange d'actifs entre les deux chaînes et « ancrage » la valeur de l'actif de la sidechain à la valeur de Bitcoin. Dans cette configuration, les utilisateurs pourraient échanger des Bitcoins contre des pièces MimbleWimble, effectuer des transactions complètement privées et rapides sur la chaîne MimbleWimble, puis échanger leurs pièces MimbleWimble contre des Bitcoins chaque fois qu'ils le souhaitent.

![Image](https://cdn-media-1.freecodecamp.org/images/bWHCCfekdQ71xVXhKFRS5HcXxBCkUf3jFHA-)
_Les pièces de la sidechain sont ancrées à la blockchain Bitcoin, fonctionnant à ses côtés avec un taux de change fixe, source : [Blockchain.com](http://blockchain.com" rel="noopener" target="_blank" title=")_

En fait, un groupe de développeurs est déjà en train de développer MimbleWimble en tant que cryptomonnaie séparée appelée [GRIN](https://github.com/mimblewimble/grin) ; elle a récemment été déployée sur un réseau de test et pourrait être lancée dans un avenir proche.

### **Rootstock**

[**Rootstock — Smart Contracts sur la Blockchain Bitcoin**](https://medium.com/@CryptoIQ.ca/rootstock-smart-contracts-on-the-bitcoin-blockchain-e52b065421a8)  
[_En tant que concept, la plateforme Rootstock [1] est l'une de ces idées qui, une fois proposée, il est évident qu'elle est géniale
..._medium.com](https://medium.com/@CryptoIQ.ca/rootstock-smart-contracts-on-the-bitcoin-blockchain-e52b065421a8)

Rootstock est, pour une raison quelconque, l'une des avancées les moins discutées dans la technologie Bitcoin, mais elle est de loin l'une des plus cool. Rootstock est décrit comme « la première plateforme de contrats intelligents open-source avec un ancrage à double sens à Bitcoin qui récompense également les mineurs de Bitcoin via le merge-mining, leur permettant de participer activement à la révolution des Smart Contracts. »

Tout comme MimbleWimble, Rootstock est développé en tant que solution de sidechain pour la blockchain Bitcoin. Sa valeur fondamentale réside dans son accent sur les contrats intelligents. Rootstock vise à être une plateforme de contrats intelligents [Turing Complete](https://simple.wikipedia.org/wiki/Turing_complete) (complètement programmable) qui sera rétrocompatible avec la machine virtuelle d'Ethereum. Cela signifie que Rootstock sera en mesure d'exécuter tout contrat intelligent développé pour la plateforme Ethereum et d'avoir des contrats intelligents développés pour sa propre plateforme.

Rootstock vise à implémenter cette fonctionnalité de contrat intelligent polyvalente tout en tirant parti de la base d'utilisateurs et de la valeur comparativement dominante de Bitcoin en agissant comme une sidechain ancrée à double sens. Il est également conçu pour être sécurisé par le réseau minier Bitcoin existant, n'ayant donc pas besoin d'inciter les mineurs à sécuriser sa propre blockchain. Rootstock vise également à résoudre le problème de scalabilité des transactions en implémentant sa propre version d'une solution multi-couches appelée [Lumino](https://uploads.strikinglycdn.com/files/9dcb08c5-f5a9-430e-b7ba-6c35550a4e67/LuminoTransactionCompressionProtocolLTCP.pdf). Avec cela, il pourrait être en mesure d'accomplir jusqu'à 20 000 transactions par seconde.

Rootstock vise [un lancement d'ici la fin de 2017](https://www.coindesk.com/bitcoin-startup-rsk-launch-smart-contracts-sidechain-2017/). Dans l'ensemble, la plateforme vise à s'intégrer parfaitement aux côtés de Bitcoin et, si ses affirmations se révèlent vraies, elle apportera sans aucun doute une utilité sans précédent au réseau Bitcoin.

Si vous êtes arrivé jusqu'ici, félicitations ! J'espère que vous avez pu apprendre quelque chose sur l'avenir de Bitcoin et que vous êtes aussi enthousiaste à ce sujet que je le suis.

Bitcoin n'est pas parfait et est confronté à des défis que sa communauté doit travailler à résoudre. Cependant, il est soutenu par une communauté de développeurs incroyablement dédiée et florissante qui travaille jour après jour pour relever ces défis. Il y a des innovations constantes qui se produisent chaque jour, et je suis sûr qu'au moment où vous avez fini de lire ceci, une autre nouvelle et excitante proposition pour la blockchain Bitcoin a fait surface.

Cet article ne couvre en aucun cas tout ce qui existe ; si vous connaissez quelque chose que je n'ai pas mentionné, n'hésitez pas à le mentionner dans les commentaires !

**Suivez-moi sur [Twitter](https://twitter.com/SubhanNadeem19) et Medium si vous êtes intéressé par des écrits plus approfondis et informatifs comme celui-ci à l'avenir !**

_Je suis moi-même un débutant relatif en Bitcoin, donc si vous trouvez des erreurs ou si vous avez des commentaires, n'hésitez pas à me le faire savoir !_

_Adresse BTC : 3MGguJhw1bm95tDQjZ3b8ySBwZLJ77CgG1_

_Voici quelques ressources si vous êtes intéressé à en apprendre plus :_

* [_Mastering Bitcoin_](https://github.com/bitcoinbook/bitcoinbook), un livre complet écrit par [Andreas M. Antonopoulos](https://www.freecodecamp.org/news/future-of-bitcoin-cc6936ba0b99/undefined)
* [_The Bitcoin Wiki_](http://bitcoin.it)
* [_The Bitcoin whitepaper_](https://lopp.net/pdf/bitcoin.pdf)
* [_A collection of Bitcoin resources_](https://lopp.net/bitcoin.html) par [Jameson Lopp](https://www.freecodecamp.org/news/future-of-bitcoin-cc6936ba0b99/undefined)
* [_This highly informative interview with Nick Szabos_](https://www.google.ca/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&cad=rja&uact=8&ved=0ahUKEwiznZ-Oo-zXAhUW02MKHZ0aAhcQtwIILzAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D3FA3UjA0igY&usg=AOvVaw0JIy-AaKaXyDsGm8psm7Qj) menée par [Tim Ferriss](https://www.freecodecamp.org/news/future-of-bitcoin-cc6936ba0b99/undefined)
* [_Ivan on Tech on Youtube_](https://www.youtube.com/channel/UCrYmtJBtLdtm2ov84ulV-yg), qui est absolument incroyable pour décomposer les concepts techniques de Bitcoin