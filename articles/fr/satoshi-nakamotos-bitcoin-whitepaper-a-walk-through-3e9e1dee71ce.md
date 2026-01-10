---
title: 'Le livre blanc de Bitcoin de Satoshi Nakamoto : une analyse approfondie et
  directe'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-12T19:48:13.000Z'
originalURL: https://freecodecamp.org/news/satoshi-nakamotos-bitcoin-whitepaper-a-walk-through-3e9e1dee71ce
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cZrXuxTThqjN_H-py_RbTw.jpeg
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: 'Le livre blanc de Bitcoin de Satoshi Nakamoto : une analyse approfondie
  et directe'
seo_desc: 'By Valentijn v/den Hout

  When I first read the original bitcoin whitepaper published by Satoshi Nakamoto
  (2008), it clarified a lot of fundamental questions I had regarding the cryptocurrency
  and blockchains in general. The paper, as many well-read bl...'
---

Par Valentijn v/den Hout

Lorsque j'ai lu pour la première fois le livre blanc original sur le bitcoin publié par Satoshi Nakamoto (2008), il a clarifié de nombreuses questions fondamentales que je me posais concernant les cryptomonnaies et les blockchains en général. Le document, comme le confirmeront de nombreux professionnels bien informés de la blockchain et des cryptomonnaies, est un excellent point de départ pour toute personne souhaitant en apprendre davantage sur la technologie.

L'objectif de cet article est de vous guider à travers le livre blanc tout en le rendant aussi digeste que possible pour toute personne nouvelle dans le domaine. Je vais essayer de simplifier certaines parties tout en maintenant l'exactitude du contenu.

Ne perdons plus de temps et plongeons directement dans le sujet. 👍

PDF : [Bitcoin : Un système de cash électronique de pair-à-pair.](https://bitcoin.org/bitcoin.pdf)

### Avant de commencer…

Une blockchain est un registre ou une base de données. Elle est distribuée et maintenue par un grand nombre de nœuds (ordinateurs) contrairement à une base de données détenue par une seule autorité ou partie. L'objectif de la technologie derrière les cryptomonnaies comme Bitcoin est de permettre d'atteindre un accord (consensus) sur la validité des données dans la base de données et sur celle des données à ajouter à la base de données 🤔. Les données, dans ce cas, font principalement référence aux données de transactions en ligne qui déterminent la propriété d'actifs numériques tels que les cryptomonnaies ou les tokens.

L'ensemble du registre distribué est maintenu à jour et vérifié, et tous les participants du réseau s'accordent sur sa validité. Sans plonger immédiatement dans les rouages techniques, les protocoles de blockchain tels que celui sous-jacent à Bitcoin permettent d'atteindre cet accord et cette validation sans avoir besoin d'un intermédiaire tiers, comme une banque 🏦.

Par le passé, une telle partie était nécessaire afin de vérifier la propriété de l'argent (c'est-à-dire, cette personne peut-elle dépenser cet argent). La partie s'assurait également qu'un paiement en ligne n'était dépensé qu'une seule fois. (c'est-à-dire, que cet argent particulier n'est pas utilisé dans une autre transaction). Ce dernier problème est ce à quoi l'on fait référence comme le **problème de la double dépense**.

Cela a toujours été un problème majeur pour les transactions d'actifs numériques. Il est possible de dupliquer le code qui constitue l'actif et de l'utiliser dans plusieurs transactions.

Le nom « blockchain » vient de la manière dont les données sont stockées. Les données sont collectées en blocs 📦 qui sont ajoutés à une chaîne ⛓️ de blocs précédemment validés. Avec cette introduction, plongeons directement dans le célèbre livre blanc.

![Image](https://cdn-media-1.freecodecamp.org/images/LPRtCW--yLwGP5QKh5Z1uwmysOOlu56uKgJ9)
_par Mike Alonzo via Unsplash_

### Résumé

Le résumé du livre blanc est assez technique dès le départ et sert de petit résumé du document. Ne vous inquiétez pas si cela vous dépasse initialement 👨‍💻. Nous avons déjà couvert la plupart de ce que vous devez savoir et nous ajouterons à cela dans la section suivante.

La seule conclusion ici devrait être que le document propose un système de cash électronique de pair-à-pair. Le système nous permet de faire des paiements en ligne directement entre nous. Il n'est pas nécessaire d'avoir une banque pour résoudre les problèmes de propriété et de double dépense. 💱 → 💵 → 👨‍💼 et ❌🏦 ?

> « Une version purement pair-à-pair de cash électronique permettrait d'envoyer des paiements en ligne directement d'une partie à une autre sans passer par une institution financière. »

### Introduction

> « Le commerce sur Internet en est venu à dépendre presque exclusivement des institutions financières servant de tiers de confiance pour traiter les paiements électroniques. »

Au moment de la rédaction du livre blanc de Bitcoin, les institutions financières étaient nécessaires pour vérifier la propriété et éliminer le problème de la double dépense. Cela, combiné à la nécessité pour les transactions d'être réversibles (les institutions financières doivent traiter les litiges de médiation), augmente les coûts associés à une transaction. Cela signifie qu'il existe une taille minimale de transaction nécessaire pour que ces institutions financières l'exécutent. Leurs frais doivent couvrir les coûts de transaction au moins, sinon cela n'a aucun sens. Si cela n'était pas clair auparavant : les banques aiment vraiment gagner de l'argent 💰.

> « … limitant la taille pratique minimale des transactions et supprimant la possibilité de petites transactions occasionnelles. »

Cela élimine l'option pour une grande quantité d'opportunités de transaction qui existent théoriquement mais ne sont pas réalisables en pratique. Une application incroyable qui n'est pas possible en raison de cette taille minimale de transaction est la micro-consommation de contenu en ligne, qu'il s'agisse d'articles web, de vidéos, de musique, etc. Au lieu de devoir payer un abonnement mensuel, qui peut ou non en valoir la peine en fonction de l'utilisation par le consommateur, les micro-transactions permettraient à un utilisateur de faire des paiements automatisés incroyablement petits au fur et à mesure que le contenu est consommé.

Cela changerait radicalement la manière dont nous utilisons Internet. Payer pour les articles Medium par mot, les vidéos YouTube par seconde, la musique Spotify par minute, ou même consommer la bande passante Internet par mégaoctet.

Une autre application possible serait de réaliser des micro-paiements directement entre les appareils de l'Internet des objets. Un exemple simple ici serait une voiture garée payant sa place de parking à la minute. Il existe d'innombrables applications de micro-consommation/transaction, dont beaucoup ne deviendront plus évidentes qu'à l'avenir. Cela n'est tout simplement pas possible si nous avons besoin d'un intermédiaire tiers.

> « Avec la possibilité de réversion, le besoin de confiance se propage. Les marchands doivent se méfier de leurs clients, les harcelant pour obtenir plus d'informations que nécessaire. »

![Image](https://cdn-media-1.freecodecamp.org/images/YCo5BQ0vTov-f0qtxaUlHVNCk1KT3UTEOxkQ)
_par Rawpixel via Unsplash_

Une autre raison pour laquelle le besoin de confiance n'est pas idéal lors de transactions en ligne est que, pour obtenir cette confiance, des informations personnelles doivent être collectées, que ce soit par les banques ou par les marchands via lesquels les paiements sont effectués. Ces informations sont stockées par ces organisations (souvent sur un seul serveur), leur donnant le contrôle sur les données personnelles et rendant les données sujettes à des fuites ou à des piratages 👮.

Des piratages de données incroyables ont eu lieu au cours de la dernière décennie — pensez à Yahoo et Equifax — et ils deviennent de plus en plus fréquents chaque jour. Ce que Bitcoin vise à accomplir est, d'une certaine manière, de répliquer la simplicité d'une transaction en personne dans un environnement en ligne.

Si Andy donne à Brenda un billet de 10 $ 💵, Brenda n'a pas besoin de savoir quoi que ce soit sur Andy (comme des informations personnelles, des scores de crédit, une valeur nette, etc.). La seule chose qu'elle doit savoir est que les 10 $ sont passés de la possession d'Andy à sa possession et que les 10 $ ne se sont pas magiquement dupliqués (💵 → 🧙‍♂️ → 💵💵) et qu'Andy a une autre réplique (exacte) à dépenser.

![Image](https://cdn-media-1.freecodecamp.org/images/3H2aKl5PWQEdz3Bn7k3lfRXYz1h-kapsRM0G)
_par Sharon McCutcheon via Unsplash_

> « Dans cet article, nous proposons une solution au problème de la double dépense en utilisant un serveur de timestamp distribué pair-à-pair pour générer une preuve computationnelle de l'ordre chronologique des transactions. »

Pour rendre cela possible, la personne (ou les personnes, ou la chose) sous le nom de Satoshi Nakamoto présente un système de paiement électronique qui utilise une preuve cryptographique 👨‍💻 qui permet à ses membres d'atteindre un accord (consensus) sans avoir besoin d'un intermédiaire tiers.

### 2. Transactions

> « Chaque propriétaire transfère la pièce au suivant en signant numériquement un hash de la transaction précédente et la clé publique. »

Dans le monde de Bitcoin, ceux qui possèdent des Bitcoins ont ce qu'on appelle un « portefeuille ». Cela fonctionne quelque peu de manière similaire à un portefeuille classique en ce sens qu'il « contient » votre Bitcoin. Associé au portefeuille se trouve une **clé publique**. Il s'agit d'une adresse qui peut être utilisée pour envoyer des Bitcoins, tout comme quelqu'un a une adresse e-mail ou un numéro de compte bancaire.

Il y a aussi une autre clé (TRÈS importante) qui est associée à un portefeuille et qui est appelée une **clé privée** 🔐, qui fonctionne comme un mot de passe. Signer avec cette clé privée est la seule façon pour quelqu'un de prouver sa propriété du portefeuille, et c'est ce qui lui permet d'envoyer les Bitcoins dans ce portefeuille. Si vous perdez cette clé (et selon le type de portefeuille, vos mots de graine), vous perdez vos BTC 😢.

Notez que l'ordre est en fait le suivant :

* Lorsqu'un portefeuille est configuré, ce portefeuille génère une clé privée aléatoire.
* À partir de cette clé privée (en utilisant un algorithme de signature numérique à courbe elliptique), une clé publique est générée (notez qu'il n'est pas possible de la convertir en clé privée ; c'est un algorithme à sens unique).
* À partir de cette clé publique (quelque chose que nous discuterons dans la section Vie privée), une adresse de portefeuille est générée.

Posséder des Bitcoins ne signifie pas que vous avez réellement des pièces dans votre portefeuille. Un Bitcoin n'est pas un morceau de code que vous possédez ou qui est stocké quelque part. La valeur du BTC associée à un portefeuille (appelons-le ABC123) est basée sur le nombre de transactions sur la blockchain qui disent « Adresse EXAMPLE890… envoie x montant de BTC à l'adresse ABC123 » ainsi que le nombre de transactions qui disent « Adresse ABC123… envoie x montant de BTC à l'adresse EXAMPLE453 ».

En d'autres termes, la blockchain Bitcoin stocke une quantité incroyable de données qui spécifient qui a envoyé combien à quelle adresse 📊. Ces données (qui envoie, quel montant, qui reçoit) sont stockées dans des transactions individuelles. La propriété des Bitcoins est calculée en regardant toutes les transactions entrant dans une adresse et celles qui en sortent.

Maintenant, si l'adresse ABC123 veut dépenser le BTC qui a été reçu d'une autre adresse, elle doit prouver qu'elle est autorisée à le faire en **signant la transaction avec sa clé privée** 🔑 (ces données conditionnelles — vous ne pouvez les utiliser que si elles sont signées avec la clé privée correcte — peuvent être trouvées dans la transaction précédente qui est appelée). Une nouvelle transaction est générée, le BTC est envoyé, et nous recommenceons. G_ardez à l'esprit que ceci est une version simplifiée ; certains détails seront ajoutés plus tard._

**Point clé à retenir** : Les Bitcoins ne sont pas des pièces réelles, ils sont simplement une combinaison de transactions qui prouvent que vous avez des BTC à dépenser. Les clés privées sont utilisées pour signer les transactions et vérifier la propriété.

> « Le problème, bien sûr, est que le bénéficiaire ne peut pas vérifier qu'un des propriétaires n'a pas dépensé deux fois la pièce. »

> « La seule façon de confirmer l'absence d'une transaction est d'être conscient de toutes les transactions. »

La confirmation de l'absence d'une transaction est effectuée en diffusant chaque transaction à l'ensemble du réseau 📡 et en créant un historique partagé de toutes les transactions précédentes (chronologiquement).

### 3. Serveur de timestamp

> « Un serveur de timestamp fonctionne en prenant un hash d'un bloc d'éléments à horodater et en publiant largement le hash… »

L'idée ici est de collecter les transactions qui ont été diffusées publiquement dans des blocs, de les horodater (ajouter une valeur de temps ⏱️), d'ajouter quelques données pertinentes supplémentaires (nous y viendrons plus tard) et de les faire passer par un algorithme de hachage SHA256 ⏯️.

Ce que cela fait fondamentalement, c'est convertir le bloc et ses données en une chaîne de caractères qui peut être utilisée pour identifier de manière unique ce bloc (seule cette combinaison de données vous donnera cette valeur de hash). Chaque nouveau bloc (avant d'être ajouté et passé par un SHA256) peut maintenant se référer au hash du bloc précédent dans la chaîne, créant une chaîne de blocs dans l'ordre chronologique. De cette façon, tout le monde peut voir quels blocs (et leurs transactions) ont eu lieu dans le passé et dans quel ordre.

Cette chaîne de blocs qui sont liés via leur valeur de hash est ce qui constitue la blockchain réelle (« blockchain » est souvent utilisé pour désigner des protocoles et systèmes entiers mais c'est vraiment la chaîne de blocs elle-même ; la base de données réelle).

### 4. Preuve de travail & 5. Réseau

Très bien. Cela semble génial ! Cependant, comment nous assurons-nous que les données ajoutées à la chaîne sont réellement correctes ? N'importe qui peut-il simplement ajouter des blocs avec des transactions qui n'existent pas ? 🤔

> « Pour mettre en œuvre un serveur de timestamp distribué sur une base pair-à-pair, nous aurons besoin d'utiliser un système de preuve de travail… »

Ce dont nous avons besoin est un système qui exige un certain travail avant de pouvoir ajouter ou suggérer un nouveau bloc à la blockchain. Tout comme le célèbre CAPTCHA sur le web, l'objectif est de créer une barrière où il devient plus difficile (et irréalisable) de spammer le système (ou dans le cas de Bitcoin, de suggérer de fausses données). Bitcoin fait cela comme suit.

J'ai mentionné ci-dessus que les transactions sont diffusées à l'ensemble du réseau. À ce stade, elles ne sont pas encore ajoutées à la chaîne. Les mineurs (ceux qui vont effectuer le « travail » pour ajouter le bloc à la chaîne) vont effectuer le hachage mentionné précédemment. Ils collectent ces transactions et les mettent dans un bloc (en tant que racine de Merkle, nous en discuterons plus tard) avec l'horodatage mentionné précédemment, le hash du bloc précédent, et d'autres données pertinentes comme la hauteur du bloc (quel bloc # dans la chaîne), et plus encore.

Ayant collecté toutes ces données dans un bloc, ils les font passer par l'algorithme de hachage SHA256. Encore une fois, ce que cela fait fondamentalement, c'est convertir toutes ces données en une chaîne de caractères qui identifie de manière unique ce bloc et ses données. Changez une petite chose dans les données du bloc et le hash entier change (il n'y a pas de motif connu pour cela mais ce n'est pas aléatoire ; changez-le en arrière et vous obtiendrez exactement le même hash).

Regardez comment le hash change lorsque j'ajoute le nombre « 1 » à la chaîne de caractères.

![Image](https://cdn-media-1.freecodecamp.org/images/Iez8yV275ZOaShY6KPVBAFxIDlCHjNhrFiYM)
_Hachage du titre original. [Calculateur de hash SHA256 Xorbin](https://www.xorbin.com/tools/sha256-hash-calculator" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/XmId6NlenYbSR8TGkbHb5SORgpfuccfh8FJq)
_Ajout de « 1 » au titre. [Calculateur de hash SHA256 Xorbin](https://www.xorbin.com/tools/sha256-hash-calculator" rel="noopener" target="_blank" title=")_

La blockchain Bitcoin ne demande pas seulement un hash ; elle veut un hash qui commence par (au moment de l'écriture) dix-sept 0 😱.

> Par exemple : 000000000000000006fb217d70740a895ce4966e2826325e31061bc433d7b186

Comment les mineurs obtiennent-ils ce hash ? Ils doivent ajouter un nombre aux données du bloc qui est appelé un 'nonce' (ils l'ajoutent comme j'ai ajouté le « 1 »). Personne ne sait quel nombre est nécessaire pour trouver le hash correct 🤯. La seule façon de le trouver est par essai et erreur : deviner.

> « … nous mettons en œuvre la preuve de travail en incrémentant un nonce dans le bloc jusqu'à ce qu'une valeur soit trouvée qui donne au hash du bloc les bits zéro requis. »

Ce processus, deviner le bon nonce, est ce à quoi l'on fait référence comme le 'minage' ⛏️. Les mineurs avec les plus grandes ressources CPU (plus de puissance de calcul) ont la plus grande chance d'être les premiers à trouver ce nonce correct.

Tant que plus de 51 % de la puissance CPU est entre les mains de nœuds honnêtes, il sera impossible pour un mineur malveillant de gagner constamment le processus de minage et d'ajouter de fausses données à la chaîne. La chaîne la plus longue est toujours la chaîne qui est prise comme la chaîne véridique.

> « … la difficulté de la preuve de travail est déterminée par une moyenne mobile visant un nombre moyen de blocs par heure. S'ils sont générés trop rapidement, la difficulté augmente. »

Ce processus d'ajout d'un nouveau bloc à la blockchain se produit toutes les 10 minutes environ. Cela est maintenu stable par le protocole ajustant la difficulté de minage (# de 0 initiaux) — également appelée « bombe de difficulté » 💣 — en conséquence de l'augmentation de la puissance de calcul au fil du temps.

### 6. Incitation

Pourquoi les mineurs feraient-ils tout cet effort et paieraient-ils beaucoup d'argent pour obtenir la puissance de calcul nécessaire au minage ?

Une fois que le bloc est accepté, une transaction supplémentaire est ajoutée au début du bloc (souvent appelée la 'transaction coinbase') qui alloue de nouveaux BTC à l'adresse du portefeuille du mineur gagnant, les récompensant pour le travail fourni et offrant un moyen de distribuer des pièces en circulation 💰. En plus de cela, chaque transaction dans le bloc a un petit — au moins c'était l'objectif — frais de transaction associé qui va également au mineur gagnant.

> « Une fois qu'un nombre prédéterminé de pièces ont été mises en circulation, l'incitation peut passer entièrement aux frais de transaction et être complètement sans inflation. »

Nous allons sauter les parties 7 (Récupération d'espace disque) et 8 (Vérification de paiement simplifiée) et discuterons brièvement de ces sections à la fin. Bien qu'elles soient une partie importante du fonctionnement de Bitcoin, pour comprendre le cœur du document, elles le sont moins.

### 9. Combinaison et division de valeur

> « Pour permettre à la valeur d'être divisée et combinée, les transactions contiennent plusieurs entrées et sorties. Normalement, il y aura soit une seule entrée d'une transaction précédente plus grande, soit plusieurs entrées combinant des montants plus petits, et au plus deux sorties : une pour le paiement, et une retournant la monnaie, le cas échéant, à l'expéditeur. »

Quelque chose que nous avons déjà abordé un peu plus tôt est la manière dont les transactions sont constituées et comment la valeur de l'adresse est calculée.

La valeur BTC détenue dans une adresse est essentiellement la somme de toutes ses transactions d'entrée potentielles (c'est-à-dire, la valeur de toutes les transactions vers cette adresse **qui n'ont pas été dépensées**). Lorsque le détenteur de l'adresse souhaite dépenser ses BTC, il ne peut pas simplement prendre exactement ce montant et l'envoyer. Il doit utiliser ses transactions d'entrée comme des pièces entières pour le faire (un peu comme vous devez payer avec un billet entier et ne pouvez pas le couper en morceaux pour payer). Alors, que signifie cela en pratique ?

Andy est de retour 👋 mais maintenant il a un portefeuille avec 0,5 BTC. Cette valeur provient de trois sorties de transaction non dépensées (UTXO) (ou futures transactions d'entrée ; les UTXO fonctionnent comme une référence pour la transaction d'entrée pour une nouvelle transaction) :   
a) 0,15 BTC   
b) 0,27 BTC  
c) 0,08 BTC

Andy veut envoyer 0,38 BTC à Brenda (chanceuse Brenda… 😊). Lorsqu'il génère cette transaction, le protocole Bitcoin prendra les entrées nécessaires qui ensemble sont égales ou supérieures (≥) au paiement à Brenda et les utilisera comme des pièces entières pour générer deux transactions de sortie.

Dans notre exemple, les transactions d'entrée **a** et **b** sont utilisées (0,15 + 0,27 = 0,42) pour générer la transaction de sortie de paiement de 0,38 BTC à Brenda, ainsi qu'une autre transaction de sortie à l'adresse d'Andy qui retourne la monnaie (0,42–0,38 = 0,04). Ces deux transactions de sortie peuvent fonctionner comme de nouvelles transactions d'entrée pour les futurs paiements par les détenteurs d'adresses.

_Note : Il y a aussi des frais de mineur/transaction impliqués qui sont prélevés de l'équation. Donc, la monnaie qui est retournée est un peu moins._

**Point clé à retenir** : Les transactions de sortie nécessitent des transactions d'entrée entières qui ensemble sont au moins égales ou supérieures à la valeur de sortie. Tout excédent (Entrées -(paiement+frais de mineur)) est retourné comme monnaie et peut être utilisé comme une nouvelle transaction d'entrée.

### 10. Vie privée

Nous avons déjà discuté de l'existence et de l'utilisation des portefeuilles, des clés publiques et des clés privées plus tôt. Dans la situation où un tiers stocke nos informations (comme une banque), la vie privée est obtenue en limitant l'accès à ces informations en gérant les permissions et en sécurisant les serveurs sur lesquels elles sont stockées.

Cependant, comme mentionné précédemment, ceux-ci fournissent un point de défaillance et d'attaque unique, les rendant sujettes à la perte et au piratage. Alors, comment Bitcoin fait-il pour fournir la vie privée si toutes les transactions sont ouvertement diffusées à l'ensemble du réseau ? 🤔

![Image](https://cdn-media-1.freecodecamp.org/images/5rszGA0p0dub9d8aWPvkHrcgoVBDMW3Edj2X)
_par Ryan Born via Unsplash_

> « La nécessité d'annoncer toutes les transactions publiquement exclut cette méthode, mais la vie privée peut encore être maintenue en brisant le flux d'informations à un autre endroit : en gardant les clés publiques anonymes. »

L'idée ici est de garder la clé publique anonyme 🔑. Tant que les gens ne peuvent pas associer une clé publique à une personne particulière, il n'y a aucun moyen de révéler son identité.

Une façon de faire cela qui est actuellement utilisée dans le protocole est via la génération d'adresses de portefeuille, un portefeuille pouvant contenir plusieurs adresses. Au lieu d'afficher les clés publiques dans les données de transaction, des adresses de portefeuille sont utilisées. Tout comme les clés publiques sont créées sur la base de clés privées en utilisant un algorithme à sens unique, la même chose est faite pour générer une adresse de portefeuille à partir d'une clé publique (en utilisant le SHA256 suivi d'un RIPEMD160). Ce que nous obtenons (après l'avoir passé par un BASE58CHECK pour le rendre plus lisible) est une adresse de portefeuille qui est utilisée dans les données de transaction.

> « En tant que pare-feu supplémentaire, une nouvelle paire de clés doit être utilisée pour chaque transaction afin de les empêcher d'être liées à un propriétaire commun. »

Sans entrer dans trop de détails, plusieurs adresses peuvent être générées à partir d'une seule clé privée en implémentant un compteur et en ajoutant une valeur incrémentielle afin de créer des sous-clés privées (qui peuvent être utilisées pour créer des clés publiques qui à leur tour peuvent être utilisées pour générer des adresses de portefeuille). De cette façon, une seule clé privée peut donner accès à un portefeuille qui a des transactions entrant et sortant de plusieurs adresses (cela est appelé un portefeuille déterministe).

De nombreux logiciels et services Bitcoin gèrent cette auto-création d'adresses de portefeuille lors de l'exécution d'une transaction, rendant presque impossible la révélation des identités derrière une transaction diffusée publiquement.

Nous allons brièvement passer en revue les parties restantes du livre blanc, puis conclure.

### 7. Récupération d'espace disque

> « Une fois que la dernière transaction d'une pièce est enterrée sous suffisamment de blocs, les transactions dépensées avant elle peuvent être supprimées pour économiser de l'espace disque. »

Lorsque une transaction est enterrée sous suffisamment de blocs, ce qui signifie qu'elle a été validée de manière approfondie par le système, il n'est pas nécessaire de continuer à stocker toutes les données de transaction dans le bloc. Cela est possible sans casser le hash en incluant uniquement la racine de Merkle de toutes les transactions dans le hash du bloc, et non les données de transaction individuelles. Pour plus d'informations sur les arbres de Merkle 🌲, consultez W[ikipedia.](https://en.wikipedia.org/wiki/Merkle_tree)

En bref, toutes les transactions sont hachées et ces hachages sont appariés avant d'être hachés à nouveau, et ainsi de suite jusqu'à ce que vous atteigniez le hachage parent de toutes les transactions, appelé la racine de Merkle.

### 8. Vérification de paiement simplifiée

Afin de vérifier un paiement, un utilisateur n'a besoin que de pouvoir lier la transaction à un endroit dans la chaîne en interrogeant la chaîne de blocs la plus longue et en extrayant la branche de Merkle dans laquelle la transaction existe. Si cet utilisateur peut le faire, il peut faire confiance à ce que la transaction a été valide étant donné que le réseau l'a incluse et que des blocs supplémentaires ont été construits sur elle.

### 11. Calculs

Cela plonge dans les mathématiques sous-jacentes expliquant pourquoi le réseau sera sécurisé lorsque plus de la moitié du réseau est composée de nœuds honnêtes.

En gros, tant qu'il y a plus de nœuds honnêtes que de nœuds malveillants, à mesure que la chaîne grandit, il devient de plus en plus difficile pour un attaquant de générer une chaîne alternative qui lui permet de récupérer les paiements qu'il a effectués. Plus de blocs sont ajoutés au-dessus d'une transaction particulière, plus la probabilité devient faible qu'un attaquant puisse rattraper son retard avec une chaîne alternative.

C'est pourquoi nous voyons souvent le nombre 6 lorsque nous parlons de (bloc) confirmations, qui fait essentiellement référence à 6 blocs qui sont ajoutés après que la transaction a été incluse, et fonctionne comme le seuil de confirmation complet.

### Terminé

Nous y voilà ! 👏 Nous avons couvert presque tout le livre blanc original de Bitcoin. Ce document a fonctionné comme la genèse des technologies de blockchain que nous voyons aujourd'hui. Mieux comprendre son contenu vous aidera définitivement à comprendre l'écosystème actuel de l'industrie.

J'espère vraiment que cet article vous a aidé. Si c'est le cas, des applaudissements seraient grandement appréciés et faites-moi savoir dans la section des commentaires ci-dessous ce que vous pensez de l'article. J'adorerais avoir votre avis. Toutes suggestions, corrections ou commentaires sont grandement appréciés.

Tout le meilleur,

Valentijn | [@vvdhout](https://twitter.com/vvdhout)

![Image](https://cdn-media-1.freecodecamp.org/images/-FPGy30PsLYQpav4OrIcTvFMtjW5CM4r-r-s)