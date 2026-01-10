---
title: Le Guide Définitif d'OmiseGO pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-03T19:08:40.000Z'
originalURL: https://freecodecamp.org/news/the-definitive-omisego-beginners-guide-f95dcdf8635c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kzvOj2G61olA6bEHY98H3Q.jpeg
tags:
- name: Omisego
  slug: omisego
- name: Blockchain
  slug: blockchain
- name: crypto
  slug: crypto
- name: Cryptocurrency
  slug: cryptocurrency
- name: 'tech '
  slug: tech
seo_title: Le Guide Définitif d'OmiseGO pour Débutants
seo_desc: 'By Jérémie Grandsenne

  As the interest for blockchain projects and cryptocurrencies is exponentially growing,
  OmiseGO appears to be one of the strongest and most exciting projects out there.
  Still, as it involves fairly complex notions, it is hard for...'
---

Par Jérémie Grandsenne

Alors que l'intérêt pour les projets blockchain et les cryptomonnaies croît de manière exponentielle, [**OmiseGO**](http://omg.omise.co/) semble être l'un des projets les plus solides et les plus passionnants. Cependant, comme il implique des notions assez complexes, il est difficile pour un débutant à la recherche d'une introduction de trouver un **guide clair et complet** : le site web d'OmiseGO fournit tous les documents nécessaires, et surtout le « [livre blanc](https://cdn.omise.co/omg/whitepaper.pdf) », une explication approfondie de l'ensemble du système, mais bien qu'il s'agisse d'un document extrêmement bien pensé et précis, il serait mentir de prétendre qu'il est facile à lire au premier abord.

Il existe également quelques revues de bonne qualité, mais bien qu'elles puissent être très utiles, elles se concentrent généralement sur un point spécifique du sujet, comme les partenariats commerciaux, sans prendre le temps d'introduire l'ensemble du projet à quelqu'un qui serait complètement nouveau dans ce domaine.

J'ai donc décidé d'écrire le guide complet qui prendrait tout depuis le début et serait **clair pour tout le monde à lire**, tout en exposant tout de la manière la plus précise et exacte possible, afin de donner à ce projet très ambitieux le large public et la compréhension qu'il mérite.

Comme je reprends les choses depuis les bases, si vous pensez être déjà clair sur certains points, n'hésitez pas à les sauter et à passer directement aux points qui vous intéressent. J'ai essayé de donner une architecture claire à cet article, des titres clairs et un résumé introductif, afin que vous puissiez naviguer facilement à travers ce guide si vous ne souhaitez pas le lire du début à la fin.

Veuillez noter que, quoi que vous lisiez dans ce guide, il est fait uniquement à des fins explicatives, et n'est en aucun cas un conseil en investissement : je ne suis pas habilité à cela, je ne le souhaite pas, et le choix que l'on fait avec son propre argent est son propre choix. Investir dans n'importe quel projet et surtout dans le monde crypto est toujours une opération à haut risque, et je n'ai aucune recommandation à faire à ce sujet. Même la partie intitulée « Pourquoi investir dans OmiseGO » doit être considérée comme une simple exposition de ce qui peut être les raisons d'investir dans le projet si l'on choisit de le faire, mais pas comme un conseil prétendant que vous devriez, ou ne devriez pas.

Je tente simplement d'expliquer clairement ce qu'est OmiseGO, ce qu'il construit, et ce qu'il peut être dans le futur, tout en répondant dans un même article à de nombreuses questions que j'ai vues et auxquelles j'ai répondu séparément sur des forums dédiés.

Cet article couvrira les points suivants :

**1) L'entreprise**  
Qu'est-ce qu'Omise ?  
Qu'est-ce qu'OmiseGO ?  
Qui est l'équipe ?  
Comment Omise a-t-elle lancé OmiseGO ?

**2) Le projet**  
**A. Bases : Blockchain / Ethereum**  
Comment fonctionnent les services internet sans blockchain ?  
Quels sont les problèmes avec le modèle traditionnel ?  
Qu'est-ce qu'une blockchain ?  
Qu'est-ce qu'Ethereum ?  
**B. OmiseGO**  
Quel problème réel OmiseGO veut-il résoudre ?  
Quels clients OmiseGO cible-t-il ?  
Que construit OmiseGO ?  
Qu'est-ce que la blockchain OmiseGO ?  
Qu'est-ce que le Decentralized Exchange (DEX) ?  
Qu'est-ce que le portefeuille OmiseGO ?  
Qu'est-ce que le SDK de portefeuille white-label ?  
À quoi sert le token OMG ?  
**C. Interactions avec d'autres projets**  
Comment Ethereum et OmiseGO interagiront-ils ?  
Qu'est-ce que Plasma ?

**3) Partenaires et investisseurs**  
**A. Pays et Banques**  
1. Thaïlande  
2. Japon  
3. Singapour et Thaïlande  
**B. Partenaires privés et investisseurs**  
1. TrueMoney  
2. McDonald's Thaïlande   
3. Toppan Printing  
4. Global Brain  
5. Phase de discussion : Greylock Partners  
 **C. Adopteurs d'OmiseGO**

**4) Le futur**  
**A. Le futur d'OmiseGO**  
Que se passera-t-il entre Omise et OmiseGO ?  
Quelle est la feuille de route d'OmiseGO ?  
 **B. Pourquoi investir dans OmiseGO**

**5) Questions Fréquemment Posées**  
Quel sera le montant des frais du réseau ?  
Quel sera le montant minimum de tokens OMG requis pour le staking ?  
OMG est-il un token ERC20 ?  
Le token OMG sera-t-il remplacé par un autre token dans le futur ?  
Où stocker les tokens OMG ?  
Où acheter OMG ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*_rySePd_USd4yehzD_6UJA.png)

### **1) L'entreprise**

**_Qu'est-ce qu'Omise ?_**

Omise est une entreprise réelle établie depuis 2013 en Thaïlande, au Japon, à Singapour et en Indonésie. Elle fournit une solution de paiement en ligne déjà utilisée par des milliers de clients : ces clients sont des marchands, utilisant la solution de paiement Omise pour vendre leurs produits ou services à leurs propres clients.

Omise a été mise en avant en 2016 par Forbes Thaïlande comme « Fintech rockstars », et a été récompensée « Startup numérique de l'année » par le Premier ministre thaïlandais.

![Image](https://cdn-media-1.freecodecamp.org/images/1*98iqoHOJepLEk42mItTCOQ.jpeg)

**_Qu'est-ce qu'OmiseGO ?_**

OmiseGO est une extension d'Omise, née en 2017 pour tirer parti de la technologie blockchain afin de proposer un système complet visant à révolutionner la manière dont les gens prennent le contrôle de leurs actifs financiers et précieux et les échangent entre eux, en fournissant un moyen sécurisé et complètement ouvert de le faire sans frontières et sans dépendre d'un tiers.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gaUuNIO7FfalE151mbqF1g.png)

**_Qui est l'équipe ?_**

Jun Hasegawa est le PDG d'Omise et d'OmiseGO, et Donnie Harinsut est le COO d'Omise et d'OmiseGO. Joseph Poon, qui est co-auteur du Lightning Network et co-auteur de Plasma, est l'auteur principal d'OmiseGO, et les membres notables de l'équipe des conseillers incluent Vitalik Buterin, fondateur d'Ethereum, et co-auteur de Plasma, Gavin Wood, co-fondateur d'Ethereum, Jae Kwon, créateur de Tendermint et Cosmos Network, Vlad Zamfir, responsable de la recherche Casper d'Ethereum, Julian Zawitowski, fondateur de Golem, et Thomas Greco, membre d'Ethereum, du Cosmos Network et de Streamr.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WKbzOobPkcFUEVKgB7NEUA.jpeg)
_Thomas Greco, Vansa Chatikavanij, Gavin Wood, Vitalik Buterin, Donnie Harinsut, Jun Hasegawa_

**_Comment Omise a-t-elle lancé OmiseGO ?_**

Omise avait prévu une ICO pour lancer leur projet OmiseGO. Une ICO est une Offre Initiale de Pièces, un type de levée de fonds typiquement utilisé pour les projets blockchain, où une entreprise ou un projet vend des pièces pour une durée limitée à un prix très spécial, ce qui est un incitatif pour les investisseurs qui croient en le projet et s'attendent à ce qu'il prenne de la valeur dans le futur, et permet à l'entreprise de lever des fonds.

Habituellement, une ICO s'arrête lorsque l'entreprise atteint son plafond, qui est le montant maximum d'argent qu'ils veulent lever via l'ICO, ou pour le dire autrement, le montant maximum de tokens qu'ils veulent vendre via l'ICO. Mais les ICO sont généralement précédées par une vente privée pour des investisseurs sélectionnés, également à un prix spécial, et OmiseGO est célèbre pour avoir atteint leur plafond de 25 millions de dollars USD via la vente privée, ce qui signifie qu'il n'y a même pas eu d'ICO publique. Ils auraient pu faire une ICO de toute façon pour lever plus de fonds, et avaient plus de 100 millions de dollars USD d'intérêt pour la vente pré-ICO seulement, mais ils ont décidé de s'arrêter une fois les fonds nécessaires pour le projet atteints. Ce qui, en passant, peut être considéré comme un geste équitable et un signe de confiance.

### **2) Le projet**

#### **A. Bases : Blockchain / Ethereum**

**_Comment fonctionnent les services internet sans blockchain ?_**

La manière traditionnelle dont les choses fonctionnent sans blockchain est le **modèle de base de données centralisée**. Une entreprise possède une base de données privée, qui est une bibliothèque de données, stockée sur un ordinateur ou sur plusieurs ordinateurs appelés serveurs. Cette entreprise fournit également un site web public, auquel les gens peuvent accéder via internet, grâce au protocole TCP/IP, qui permet à un ordinateur de se connecter à un serveur spécifique (ou une collection de serveurs) lorsqu'il tape une certaine adresse. Par exemple, taper [http://www.facebook.com](http://www.facebook.com) vous emmènera sur le site web de Facebook, ce qui signifie que grâce au protocole TCP/IP, votre ordinateur se connectera aux serveurs de Facebook, et uniquement à ces serveurs, lorsque vous tapez l'adresse http de Facebook.

Et lorsque l'utilisateur demande une action sur une certaine interface de site web via son navigateur, par exemple lorsqu'il clique sur un lien ou remplit un formulaire, le site web recherchera les informations pertinentes (par exemple : le contenu de la page suivante) sur son serveur, en d'autres termes, à l'intérieur de sa base de données privée, et livrera ces informations sur l'écran de l'utilisateur. Et si nécessaire, le site web mettra également à jour les informations de sa base de données en fonction des actions de l'utilisateur, par exemple dans le cas de la création, de l'édition ou de la suppression d'un profil utilisateur.

Dans ce modèle, l'entreprise possède une base de données, qui est à la fois, premièrement, la collection d'instructions programmatiques qui sont la matrice technique de ce que les utilisateurs voient sur leur écran, en d'autres termes les règles qui définissent les actions autorisées par le site web, et deuxièmement, la bibliothèque contenant toutes les données utilisées par le site web, par exemple les images utilisées sur le site web, et toutes les données que les utilisateurs pourraient entrer dans le site web telles que leurs informations d'identité, photo de profil, historique de recherche et de navigation, informations de paiement, et toute information que vous pourriez donner en utilisant un certain site web.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UZIkQDHIH2hLeVVD9QsehQ.gif)
_Source de l'image [Infomotions.com](http://infomotions.com/musings/waves/clientservercomputing.html" rel="noopener" target="_blank" title=")_

**_Quels sont les problèmes avec le modèle traditionnel ?_**

Il y a 3 problèmes principaux avec le modèle traditionnel de base de données centralisée :

- Le premier problème est la **sécurité** : si un pirate réussit à briser la sécurité de la base de données (et parfois ils y parviennent), beaucoup de contenu sensible peut fuir et compromettre la sécurité ou la vie privée des utilisateurs.

- Le deuxième problème est la **vie privée**, ce qui signifie l'utilisation que le site web fait des données personnelles des gens : bien que cela dépende de la politique de chaque site web, un site web contenant des informations sur les utilisateurs sur ses serveurs peut vendre ces informations à des tiers, soit de manière anonyme (big data) soit de manière nominative, que les informations seront utilisées pour du marketing personnalisé direct (le plus couramment), ou pour de l'espionnage personnel ou industriel.

- Enfin, le troisième problème, qui inclut les deux premiers et va également au-delà, est que, quel que soit le fournisseur de services, comme une entreprise commerciale, une banque, un bureau gouvernemental, et quelle que soit la manière dont ils ont l'intention de traiter les données des gens, une chose qui est commune à toutes ces structures lors de l'utilisation de leurs services, est le besoin de **confiance** : les utilisateurs leur font confiance, ils leur donnent des informations sensibles, en supposant et en espérant que le service ne fera rien avec leurs données qu'ils ne voudraient pas, et qui compromettrait leur vie privée ou les mettrait en danger. Cela s'applique à l'entreprise dans son ensemble (vous faites confiance à l'entreprise), et cela s'applique aux travailleurs de l'entreprise : vous faites confiance à ce qu'aucun individu malveillant ne fait partie de l'équipe de l'entreprise et n'a accès à vos données.

Ce système de confiance signifie également que l'utilisateur n'a pas le **contrôle** sur ses propres données, et au lieu de cela, délègue ce contrôle à un tiers (l'entreprise, la banque ou le service), auquel il décide de faire suffisamment confiance pour utiliser (un marché en ligne), ou que la société incite fortement à utiliser (une banque).

**_Qu'est-ce qu'une blockchain ?_**

En deux mots, **une blockchain est une base de données décentralisée qui est aussi un réseau.**

Qu'est-ce que cela signifie ?

Le système traditionnel est essentiellement composé de 2 entités : le client de l'utilisateur (son ordinateur et son navigateur internet ou son application connectée), et le serveur / la base de données du site web qui communique avec le client.

Et si 10 000 utilisateurs se connectent au même site web, vous avez toujours, 10 000 clients d'un côté, et 1 base de données de l'autre côté (ou une collection de nombreuses bases de données lorsque le site web est grand, mais elles équivalent toujours à une base de données centralisée à la fin). Et l'information (les données) se déplace de 2 manières binaires : d'un client vers le serveur, ou du serveur vers un client.

Maintenant, imaginez que le site web ne possède pas de base de données privée, et que, au lieu de cela, chacun des 10 000 clients, en plus d'être un client (un utilisateur), possède également une copie identique de la base de données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3hyWN8UhcrL7P0Opbu7IQg.jpeg)
_Source de l'image [Seats2meet.com](https://magazine.seats2meet.com/more-about-blockchain/" rel="noopener" target="_blank" title=")_

Imaginez que si un pirate se cache parmi ces 10 000 utilisateurs et veut supprimer, ajouter ou modifier de manière fallacieuse une information dans la base de données à son propre profit (par exemple : ajouter un transfert d'argent d'un compte d'utilisateur victime à son propre compte), sa propre copie deviendra différente des 9999 autres copies, donc sa copie de la base de données sera automatiquement rejetée et sa tentative de fraude sera également rejetée.

Imaginez également que la base de données n'est plus composée de lignes et de colonnes et d'entrées, où vous pouvez modifier les entrées, comme dans une base de données traditionnelle, mais de blocs d'informations qui s'alignent verticalement et s'ajoutent les uns aux autres au fil du temps, et qu'une fois confirmés et mis dans la ligne de blocs (la chaîne de blocs), aucun bloc ne peut jamais être modifié ou effacé dans le futur.

Enfin, imaginez que pour ajouter un nouveau bloc à la chaîne afin de le valider, il doit être accepté à la fois horizontalement, ce qui signifie qu'il doit être confirmé par tous les utilisateurs qui possèdent une copie de la base de données (ou un nombre suffisant d'utilisateurs aléatoires), et également verticalement, ce qui signifie que pour être confirmé comme bloc 3456 de la chaîne, il doit fournir une preuve cryptographique extrêmement compliquée, sans laquelle il ne pourra pas s'accrocher au bloc 3455, et ne pourra pas être ajouté à la chaîne.

Ceci est **la blockchain en tant que base de données décentralisée** : la base de données est maintenant identiquement partagée par des milliers d'ordinateurs, et pas une seule ligne ne peut être effacée ou changée dans la base de données (jamais), et pas une seule ligne ne peut être ajoutée sans fournir une preuve très spécifique et l'avoir confirmée par ces milliers d'ordinateurs qui vérifieront également qu'elle correspond verticalement à leur bloc précédent. Le résultat est que le pirate qui avait la capacité de briser la sécurité d'une base de données centralisée et de voler son contenu sensible, devrait maintenant briser des barrières cryptographiques extrêmement compliquées mais aussi briser les portes de milliers d'ordinateurs au même moment, pour modifier chacune des milliers de copies existantes de la base de données : c'est pourquoi la blockchain est considérée comme virtuellement inviolable. Pour approfondir ce sujet et en apprendre davantage sur les hachages et les nonces, vous pouvez regarder cette vidéo très claire et intéressante d'Anders Brownworth [ici](https://anders.com/blockchain/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*flMWR1oSK--wozLYmEn8XA.png)
_Regardez la [vidéo](https://anders.com/blockchain/" rel="noopener" target="_blank" title=") d'Anders Brownworth et donnez un sens à ces boîtes et nombres colorés_

Et **la blockchain en tant que réseau** signifie simplement que tous ces ordinateurs possédant leur propre copie identique de la base de données décentralisée, exécutent également tous une certaine application, grâce à laquelle ils sont tous liés ensemble, et constituent un grand réseau. Chaque point de ce réseau, ce qui signifie chaque ordinateur possédant cette copie de la base de données et exécutant cette application, est appelé un nœud, car, comme dans un filet ou une toile physique, il agit comme le lien et le point nodal où plusieurs lignes se rencontrent. Et grâce à cette architecture horizontale de nœuds et de lignes, où tout nœud est virtuellement lié à tout autre nœud, l'information (les données) peut voyager, maintenant non seulement de manière binaire d'un serveur à un client ou d'un client à un serveur, mais, comme tout le monde est maintenant à la fois client et serveur, de tout nœud à tout nœud. Ces données peuvent être de tout type d'information que vous pouvez imaginer, et cette structure de réseau, où tout type d'information peut voyager de tout nœud à tout autre nœud, est la blockchain en tant que réseau.

Ensuite, les utilisateurs peuvent également utiliser des applications exécutées sur ce réseau sans exécuter un nœud eux-mêmes, et sans posséder leur propre copie de la base de données.

**_Qu'est-ce qu'Ethereum ?_**

Au-dessus du protocole blockchain, le terme Ethereum fait référence à la fois à la **blockchain Ethereum** et à la **couche d'application Ethereum** exécutée sur cette blockchain. La blockchain Ethereum est une certaine blockchain, ce qui signifie un certain réseau composé de milliers d'ordinateurs agissant comme des nœuds Ethereum. Et, exécutée sur la blockchain Ethereum, le terme Ethereum fait également référence à une couche de protocole d'application supplémentaire, que les développeurs peuvent utiliser pour développer leurs propres applications sur le réseau Ethereum.

Ethereum a également popularisé le concept de **contrats intelligents**, qui définissent des règles entre 2 participants, et grâce auxquels une certaine transaction se produit lorsque et seulement lorsque les paramètres acceptés par les deux participants sont remplis, sans permettre à l'un des 2 participants de changer les termes du contrat sans l'accord de l'autre : ce qui est une garantie de transparence technique et légale. Le contrat peut être financier, ou se produire à tout autre niveau. En même temps, le protocole Ethereum inclut également son propre token, Ether (ETH).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZPirVdiYDAF6IxQywTs2Vg.png)
_Image par Maria Kuznetsov, source [Coindesk.com](https://www.coindesk.com/information/what-is-ethereum/" rel="noopener" target="_blank" title=")_

En d'autres termes, le terme blockchain fait référence à la fois à un certain type de **protocole** et de processus entre ordinateurs, et à un **réseau** particulier existant qui est construit sur la base du protocole blockchain. Et pour développer une application blockchain (parce que vous voulez que votre application tire parti des avantages du protocole blockchain tels que la décentralisation, la sécurité et la confidentialité), vous devez créer une certaine blockchain, et vous devez développer une application sur celle-ci. Les deux sont des opérations compliquées et coûteuses, car l'écosystème et le développement de la blockchain sont encore une sorte de « **Far West cognitif** ». Dans ce Far West, Ethereum vient prendre tout le monde par la main, en fournissant une blockchain utilisable et efficace, et une certaine suite d'outils de développement pour construire : un langage de programmation inspiré de JavaScript appelé Solidity, et un framework de développement basé sur Solidity, que les développeurs peuvent utiliser pour développer et exécuter leurs applications sur la blockchain Ethereum.

La raison de la popularité d'Ethereum réside dans la robustesse et la qualité de la blockchain Ethereum, dans le développement du processus de contrats intelligents, et dans le fait qu'Ethereum en tant que couche d'application permet aux développeurs de développer tout type d'application qu'ils souhaitent, en sautant le processus de construction de la blockchain, ouvrant la porte à un monde entièrement nouveau d'applications basées sur la blockchain avec un coût de développement réduit et une courbe d'apprentissage. Ethereum est déjà actif (première version en juillet 2015) et toujours en développement, et de nombreux observateurs considèrent qu'il pourrait apporter un changement de paradigme considérable, et changer la manière dont nous connaissons le monde et interagissons avec les autres de la même manière que l'internet l'a changé il y a quelques décennies. Il fait également partie de la culture informatique et blockchain de savoir qu'Ethereum a été fondé par le jeune Vitalik Buterin.

#### **B. OmiseGO**

**_Quels problèmes réels OmiseGO veut-il résoudre ?_**

OmiseGO s'attaque à 2 types de problèmes :

- Le premier problème ou fait est que des centaines de millions de personnes en Asie, et 2 milliards de personnes dans le monde, sont **non bancarisées**. Elles n'ont pas accès à un compte bancaire, et ne peuvent pas non plus utiliser un compte bancaire dans leur vie quotidienne, ni envoyer ou recevoir de l'argent à distance facilement, sauf en utilisant des solutions coûteuses (ce qui peut souvent être un problème pour les travailleurs immigrés visant à envoyer de l'argent à leur famille). D'autre part, l'Asie montre un taux de pénétration d'internet exceptionnel : beaucoup de personnes non bancarisées, mais de plus en plus de personnes connectées.

OmiseGO souhaite fournir aux personnes non bancarisées une solution facile et ouverte leur permettant de posséder, d'envoyer et de recevoir de l'argent sous forme dématérialisée, quelle que soit la monnaie ou l'actif qu'ils souhaitent envoyer, et à un coût minimal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7_KeebuC2P_mq3OXOmyQHA.png)
_Carte de 2016. Source [PaymentsCardsAndMobile.com](http://www.paymentscardsandmobile.com/addressing-unbanked-developing-countries/" rel="noopener" target="_blank" title=")_

- Le deuxième problème est ce qu'OmiseGO définit comme un problème fondamental de « **coordination** parmi les processeurs de paiement, les passerelles et les institutions financières » : ce qui signifie que le monde économique et financier est rempli de réseaux fermés, où il est possible d'envoyer de l'argent à l'intérieur d'un même réseau, mais beaucoup plus difficile ou coûteux d'envoyer de l'argent ou des valeurs entre réseaux.

OmiseGO souhaite fournir aux utilisateurs et aux marchands une **solution universelle et décentralisée**, rendant facile et sans coût l'envoi d'argent d'un réseau à un autre, de manière agnostique parmi les devises ou les types d'actifs, et les pays et juridictions.

Comme effet secondaire, un tel réseau qui, par conception, permet également d'échanger de l'argent fiduciaire (argent émis par les nations), des cryptomonnaies (argent numérique créé par ordinateur), sur n'importe quel actif ou valeur (points de fidélité) via un réseau sécurisé par blockchain, facile à utiliser et à coût minimal, devrait également augmenter l'utilisation des cryptomonnaies dans la vie quotidienne des gens.

**_Quels clients OmiseGO cible-t-il ?_**

OmiseGO cible 2 types de clients :

- Le premier type est constitué des **utilisateurs individuels**, et surtout au début en Asie du Sud-Est, pour leur fournir une solution quotidienne facile qui peut agir comme un substitut positif à un compte bancaire, leur permettant de garder, d'envoyer, de recevoir de l'argent, facilement, en toute sécurité, rapidement et à moindre coût, sur un réseau ouvert, sans dépendre de l'acceptation des banques, et sans s'appuyer sur une banque comme tiers de confiance, leur permettant de prendre le contrôle de leur propre autonomie financière.

- Le deuxième type est constitué des marchands et des fournisseurs de portefeuilles, et plus généralement des **fournisseurs de paiement électronique** (EPP), leur permettant de proposer des solutions avec lesquelles leurs clients peuvent conserver, envoyer, recevoir et échanger tout type de valeurs d'un réseau à un autre, leur donnant beaucoup plus de liberté que ce qu'ils ont actuellement, et à un coût beaucoup plus faible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dc1m99-AlLG4cSiYhwmGVA.jpeg)
_Si vous n'avez rien de mieux à faire sur l'île de Panglao aux Philippines, vous pouvez utiliser votre portefeuille OmiseGO / Photo Reinhard Dirscherl, Getty, source [Travel + Leisure](http://www.travelandleisure.com/slideshows/best-secret-beaches-on-earth#panglao-island-phillippines" rel="noopener" target="_blank" title=")_

**_Que construit OmiseGO ?_**

OmiseGO construit **un système entièrement décentralisé pour permettre l'échange de valeurs en temps réel et en pair-à-pair sur une blockchain basée sur Ethereum**, quelle que soit le type de valeur (argent fiduciaire, cryptomonnaie, tout actif ou toute valeur comptable telle que le kilométrage ou les points de fidélité), et de manière agnostique à travers les juridictions.

- Ce système complet prendra place sur la **blockchain** OmiseGO (réseau), et inclura sur cette blockchain :

- Un **échange décentralisé** (DEX), un mécanisme de fournisseur de liquidité, un réseau de messagerie de chambre de compensation et une passerelle blockchain soutenue par des actifs.

- Le **portefeuille** OmiseGO.

- Un **kit de développement logiciel** (SDK) de portefeuille white-label.

- Le token propre au réseau OmiseGO : le **token OMG**.

**_Qu'est-ce que la blockchain OmiseGO ?_**

OmiseGO construit son propre réseau, la blockchain OmiseGO. La blockchain OmiseGO ne sera pas la propriété de la société OmiseGO en tant que propriété exclusive, mais sera un réseau ouvert et sans permission appartenant à tous ceux qui l'utilisent. Les opérations se déroulant à l'aide des produits OmiseGO (ces produits sont le DEX, le portefeuille OmiseGO et les portefeuilles ou applications construits avec le SDK OmiseGO) se dérouleront en partie sur la blockchain OmiseGO, et en partie sur la blockchain Ethereum. La manière dont les opérations seront distribuées entre ces 2 réseaux est expliquée ci-dessous dans « Comment Ethereum et OmiseGO interagiront-ils ? ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*CsA7WUSJTEVLrlFLFhhmgA.png)
_Source [OmiseGO](https://omg.omise.co/" rel="noopener" target="_blank" title=")_

**_Qu'est-ce que le Decentralized Exchange (DEX) ?_**

Afin de pouvoir envoyer et recevoir toute devise ou actif sur le réseau, la blockchain OmiseGO inclura un échange décentralisé (DEX) permettant aux valeurs d'être échangées en temps réel contre d'autres valeurs.

De cette manière, les fournisseurs de paiement électronique utilisant le réseau OmiseGO peuvent permettre à leurs clients d'envoyer et de recevoir des paiements non seulement à l'intérieur du réseau propre du fournisseur de paiement électronique, mais également **inter-réseaux** : la blockchain OmiseGO n'agira pas seulement comme une blockchain en soi, mais également comme un **hub** auquel d'autres blockchains peuvent se connecter, et qui peut se connecter à d'autres blockchains, brisant les frontières traditionnelles entre divers canaux de paiement. En d'autres termes, OmiseGO permettra **l'interchangeabilité des portefeuilles électroniques**, tandis que la blockchain OmiseGO tiendra un registre du solde actuel de chaque service de portefeuille électronique.

La blockchain OmiseGO inclura également un carnet d'ordres décentralisé et un moteur de trading. Les croisements directs entre les différentes devises fiduciaires propres aux portefeuilles électroniques peuvent être trop nombreux pour être traités suffisamment rapidement en utilisant la blockchain : c'est pourquoi il est prévu que les fournisseurs de paiement électronique détiendront un certain pool de liquidités pour les transferts de petits montants vers leurs destinations les plus populaires. Et pour les transferts de montants plus élevés, qui sont le véritable objectif et avantage du réseau OmiseGO, afin de créer un **marché liquide** et de permettre des transactions et transferts rapides, certains ETH seront liés dans un contrat intelligent sur la chaîne OmiseGO (ou des tokens de type Bitcoin seront liés dans des chambres de compensation liées), ce qui permettra à toute monnaie fiduciaire ou cryptomonnaie d'être échangée avec de l'ETH.

Cela signifie que, par exemple, si A veut envoyer des yens à B, mais que B veut recevoir des dollars, A enverra des yens, les yens seront échangés contre de l'ETH, puis l'ETH sera échangé contre des dollars, et des dollars arriveront à B.

Cependant, l'utilisation de l'ETH comme monnaie de référence pour le trading n'est pas obligatoire, mais il sera plus efficace et plus rapide d'utiliser des cryptomonnaies comme monnaies de référence des paires.

Afin de **mettre à l'échelle** le réseau, et pour empêcher les pools de liquidités de créer une centralisation (les pools de liquidités sont des liquidités fournies par les utilisateurs au réseau, pour créer un réseau liquide et des transactions rapides, donc si les utilisateurs possèdent une énorme quantité de liquidités, ils pourraient en venir à prendre trop de pouvoir sur le réseau), une construction de style [Lightning Network](http://lightning.network/), appelée **Plasma** et actuellement en développement, permettra de décharger un grand nombre d'opérations hors chaîne : chaque fournisseur de paiement électronique (EPP) établira un canal dans un contrat intelligent ETH pour les petits transferts, lui permettant de fournir des liquidités sur son propre réseau centralisé hors chaîne, sans surcharger le réseau de blockchain décentralisé OmiseGO avec un nombre trop élevé de petites transactions.

Il doit enfin être souligné que le réseau OmiseGO n'est pas conçu dans le but d'être un réseau à faible valeur et à haut volume, pour gérer un très grand volume de micro-transactions, mais avec l'objectif d'être « **la plateforme d'échange et de règlement de haute valeur prééminente** ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*3k2cQq97D1uEwCjDUr37Qw.png)
_Source [OmiseGO](https://omg.omise.co/" rel="noopener" target="_blank" title=")_

**_Qu'est-ce que le portefeuille OmiseGO ?_**

Un portefeuille est essentiellement une application avec laquelle vous pouvez stocker, envoyer, recevoir de l'argent et des actifs de valeur.

Sur la blockchain OmiseGO, ainsi que sur divers projets de blockchain, un portefeuille, lorsqu'il est ouvert (c'est-à-dire lorsque l'application est lancée), est également ce qui fait de votre ordinateur un **nœud** de la blockchain. Une autre façon de le dire, est qu'une blockchain est un réseau de portefeuilles ouverts, fonctionnant sur des ordinateurs.

**_Qu'est-ce que le SDK de portefeuille white-label ?_**

Un SDK est un Kit de Développement Logiciel, également appelé **framework de programmation**. Si vous connaissez React, Angular, Ruby on Rails, ce sont aussi des frameworks. Un SDK est une collection de fonctions de programmation prédéfinies pour une certaine collection de finalités, permettant aux développeurs de développer des applications de manière beaucoup plus rapide et efficace que s'ils devaient tout coder à partir de zéro. Par exemple, le SDK fournit une certaine fonction « faire-ceci » : derrière cette fonction se trouvent 1000 lignes de code, que le programmeur utilisant le SDK n'aura pas à écrire, car il utilisera simplement l'instruction « faire-ceci » du SDK. Les SDK fournissent de nombreuses fonctions « faire-ceci », chacune d'entre elles économisant du temps et des coûts aux développeurs et aux entreprises.

Le SDK de portefeuille white-label construit par OmiseGO sera, comme son nom l'indique, un framework pour les développeurs et les entreprises afin de développer rapidement et efficacement des portefeuilles pour leurs propres clients, et sans aucune obligation de design ou de mention d'OmiseGO sur le produit final, car le SDK ne sera qu'un ensemble de fonctions de programmation (de nombreuses fonctions « faire-ceci »). Tout développeur peut développer et concevoir son propre produit, en utilisant simplement le SDK pour accélérer le processus, économiser de l'argent et du temps, et éviter le processus douloureux de construction de sa propre blockchain et la courbe d'apprentissage douloureuse de la compréhension complète du modèle complexe de la blockchain.

![Image](https://cdn-media-1.freecodecamp.org/images/1*vHz1i_6BD-8RrZPK9atwPw.png)
_Source [OmiseGO](https://omg.omise.co/" rel="noopener" target="_blank" title=")_

Le SDK de portefeuille white-label d'OmiseGO sera **gratuit** à utiliser pour tout le monde, et chaque transaction se déroulant via des applications développées avec le SDK se déroulera automatiquement **sur la blockchain OmiseGO**.

La déclaration d'OmiseGO est que les principaux acteurs déjà existants auront un intérêt à développer leur propre blockchain et leurs propres portefeuilles, mais qu'il existe une longue traîne de fournisseurs de portefeuilles de taille moyenne et petite arrivant bientôt sur le marché des transferts financiers et de valeur, qui bénéficieraient grandement du SDK d'OmiseGO. Ce qui accélérerait également par conséquent l'adoption de la blockchain et des portefeuilles basés sur la blockchain par un large public.

**_À quoi sert le token OMG ?_**

L'application de portefeuille OmiseGO ne servira pas seulement à envoyer et recevoir de l'argent.

Dans la blockchain, lorsqu'une transaction se produit (par exemple, A veut envoyer de l'argent à B), la transaction est incluse dans un « bloc », une collection de transactions, et pour que le bloc soit valide et ajouté à la chaîne de blocs, il doit être confirmé par les acteurs du réseau, en d'autres termes, par des nœuds, en d'autres termes, par des ordinateurs ayant leur portefeuille ouvert.

Mais il ne suffit pas d'avoir un portefeuille ouvert : si votre portefeuille est vide, vous ne pourrez pas confirmer de bloc. Alors, comment cela fonctionne-t-il ?

Garder une certaine quantité de tokens OMG sur votre portefeuille **vous donne le droit de confirmer des blocs**. (En passant, pour augmenter la sécurité du réseau, il sera requis que les validateurs OMG exécutent également un nœud complet du réseau Ethereum, qui fonctionne en utilisant le même processus de validation.)

Maintenant, pourquoi voudriez-vous avoir ce droit ?

Parce que la blockchain OmiseGO fonctionnera selon le système **Proof of Stake** (PoS), ce qui signifie que chaque transaction se produisant sur la blockchain OmiseGO générera de petits frais (dont le montant reste à déterminer), et de nombreuses transactions généreront de nombreux petits **frais**. Si le nombre de transactions est suffisant, une immense quantité de petits frais peut se transformer en un montant global très important. Garder vos tokens sur votre portefeuille est appelé les staker, et le système Proof of Stake signifie que :

- Les frais générés par le réseau seront distribués parmi les détenteurs de tokens (stakers).

- Plus vous **stakez** de pièces (plus vous possédez de pièces sur votre portefeuille), plus vous recevrez de frais proportionnellement aux autres stakers. Un staker avec 2000 OMG sur son portefeuille recevra deux fois le montant reçu par un staker avec 1000 OMG.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rBYcKS1YiknBcaJfvVLi-w.jpeg)
_Revenu passif / Crédit Don Rosa, Disney, Glénat_

- Si vous êtes pris en train de faire un mauvais usage du réseau (en trichant de quelque manière que ce soit, probablement pour votre propre bénéfice), tous les tokens que vous stakiez sont **brûlés**, ce qui signifie détruits, ce qui signifie : vous perdez de l'argent. Vous perdez le montant que vous aviez payé pour acquérir ces tokens OMG, vous perdez la valeur qu'ils avaient à ce moment-là, et bien sûr vous perdez la capacité de recevoir des frais du réseau.

Donc, la raison pour laquelle vous êtes payé plus si vous stakez plus de pièces, est parce que vous prenez un plus grand risque, si vous vouliez attaquer le système, et donc il est considéré que vous ne voudrez pas l'attaquer : le token agit comme une **obligation**. Plus vous stakez, plus vous pouvez perdre si vous trichez, donc plus vous pouvez être considéré comme un nœud de confiance, et plus vous recevez de compensation financière pour votre activité de confirmation de blocs.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_YbE-dX915E4r01C3e0Ljg.jpeg)
_Les hackers se sont fait prendre, les tokens ont été réduits / Crédit Don Rosa, Disney_

Mais si vous connaissez le système Proof of Work (PoW), qui est utilisé pour Bitcoin, et actuellement sur Ethereum aussi avant que leur système Proof of Stake soit prêt, il est important de noter que contrairement à Proof of Work, dans le protocole Proof of Stake, savoir quel nœud (quel utilisateur) confirme un bloc, n'a aucune influence sur qui reçoit les frais. Seule la quantité de pièces que l'on stake compte. (Ce qui rend également le système Proof of Stake un système beaucoup moins coûteux écologiquement que le système Proof of Work, où chaque machine dépense d'énormes quantités d'énergie en compétition pour être celle qui confirmera la transaction.)

Cette **incitation économique** est la raison pour laquelle plus il y aura de transactions sur le réseau OmiseGO, plus il y aura de revenus passifs pour les détenteurs d'OMG, et donc plus le token OMG prendra de la valeur.

De plus, le token OMG pourra être utilisé comme token de paiement auprès des marchands qui l'acceptent.

#### **C. Interactions avec d'autres projets**

**_Comment Ethereum et OmiseGO interagiront-ils ?_**

Comme mentionné ci-dessus, OmiseGO construit sa propre blockchain, mais en réalité, toutes les opérations ne se dérouleront pas sur la blockchain OmiseGO : tout ce qui relève du suivi des règles OMG pour décider où va l'argent et quels ordres de trading sont exécutés de quelle manière, se passe sur la blockchain OmiseGO, mais la livraison finale se fait sur la blockchain Ethereum. En d'autres termes, toutes les opérations décisionnelles (compensation et règlement) se déroulent sur la chaîne OmiseGO, tandis que le transfert d'argent final réel est délégué à la blockchain Ethereum.

**_Qu'est-ce que Plasma ?_**

Bien que la blockchain présente de nombreux aspects très positifs par rapport au modèle traditionnel de base de données centralisée, elle présente toujours un problème de **scalabilité** qui doit être résolu : un nombre trop élevé de transactions ne peut pas se produire très rapidement en même temps. Plasma est une solution co-développée par Joseph Poon et Vitalik Buterin, tous deux conseillers clés du projet OmiseGO, qui permet une scalabilité extrême, potentiellement des milliards de mises à jour d'état par seconde, « état » étant une sorte de « capture de la situation des données ». En anglais simple, cela rendra possible la **gestion très rapide d'une quantité extrêmement élevée de transactions**, rendant l'efficacité du réseau OmiseGO comparable à l'efficacité du réseau Visa.

OmiseGO sera le premier projet à implémenter la technologie Plasma, mais comme Plasma est actuellement en développement, il est bon de noter qu'OmiseGO pourra commencer sans utiliser Plasma au début, et utilisera le **Cosmos Network** à la même fin avec une scalabilité intermédiaire dans une première phase, où le réseau OmiseGO ne sera pas encore entièrement public (voir ci-dessous « Quelle est la feuille de route d'OmiseGO ? » pour plus de détails).

![Image](https://cdn-media-1.freecodecamp.org/images/1*o8RBc2Uyi-wVdV0fdDsLXA.png)
_Logo du Cosmos Network. Source [Cosmos Network](https://cosmos.network/" rel="noopener" target="_blank" title=")._

### **3) Partenaires et investisseurs**

#### **A. Pays et Banques**

**1. Thaïlande**

Omise est une entreprise fortement implantée en Thaïlande, et tout naturellement, de nombreuses choses se passent entre la Thaïlande et sa « Startup numérique de l'année 2016 ».

- Tout d'abord, il est important de souligner que le ministère des Finances de Thaïlande a lancé un plan directeur national de paiement électronique pour promouvoir le paiement électronique, avec pour objectif de **créer une société sans argent liquide**. Ce n'est que de la spéculation pour l'instant de penser que cela est lié au fait qu'Omise et Vitalik Buterin ont eu une réunion avec la **Banque centrale de Thaïlande**, mais que cela soit lié ou non et comment, ce qui compte, c'est que le pays d'implantation principal d'Omise et d'OmiseGO a annoncé cet objectif, qu'OmiseGO peut être un excellent fournisseur de solutions dans cette perspective, et que le ministère des Finances de Thaïlande et l'entreprise semblent en très bons termes.

Et, sur un plan plus concret, le ministère thaïlandais des Finances a lancé avec succès l'utilisation de la **technologie FacePay d'Omise**, permettant les paiements par reconnaissance faciale.

- La Thaïlande a également lancé **PromptPay**, un nouveau système de paiement mobile interbancaire « pour permettre les transferts d'argent » entre des comptes de différentes banques avec une solution « moins chère et plus facile que celles offertes par les banques conventionnelles ». L'autorisation de participation à PromptPay est donnée par le ministère des Finances, et l'un des deux consortiums bancaires qui ont reçu cette autorisation est le Thai Alliance Payment System, qui inclut la **Bank of Ayudhya** (communément appelée Krungsri), qui a récemment effectué un **investissement stratégique de 30 millions de dollars dans OmiseGO**.

Il est utile de rappeler qu'un « investissement stratégique » effectué par une entreprise A dans une entreprise B, est différent d'un simple « investissement ». Un investissement régulier signifie que l'entreprise A prévoit la croissance de l'entreprise B, et s'attend à recevoir des dividendes de cette croissance. Mais un investissement stratégique signifie que l'entreprise A prévoit une croissance personnelle, en tant qu'entreprise, grâce à la croissance de l'entreprise B. Ce qui signifie ici que la Bank of Ayudhya a investi dans OmiseGO parce que la Bank of Ayudhya s'attend à ce que, grâce à OmiseGO, la Bank of Ayudhya elle-même se développe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JCaj6msrTOz6DbBoOFQX2Q.jpeg)
_Jun Hasegawa, PDG d'Omise, Sam Tanskul, directeur général de Krungsri Finnovate, Donnie Harinsut, COO et co-fondateur d'Omise. Source [Digital News Asia](https://www.digitalnewsasia.com/startups/krungsri-finnovate-leads-latest-funding-round-omise" rel="noopener" target="_blank" title=")_

Il est, par conséquent, à ce moment-là encore de la spéculation mais une spéculation significative, de s'attendre à ce que la Bank of Ayudhya, qui a une capitalisation boursière de 7 milliards de dollars (voir la revue Forbes [ici](https://www.forbes.com/companies/bank-of-ayudhya/)), puisse fournir à leurs utilisateurs à l'avenir des applications financières fonctionnant sur le réseau OmiseGO. Et encore une fois, toute transaction se déroulant sur le réseau OmiseGO, par exemple via une application fournie par une banque à ses clients, générera des frais qui seront distribués entre les détenteurs de pièces OMG.

Il peut également être noté, bien que cela ait un impact potentiel moins important, que les 4 autres banques constituant le Thai Alliance Payment System autorisées à rejoindre le système de paiement mobile interbancaire PromptPay, sont également toutes soutenues par le système de paiement en ligne actuel d'Omise.

**2. Japon**

Avec la Thaïlande, le Japon est l'autre pays principal d'implantation d'Omise et maintenant d'OmiseGO, car leur PDG et COO sont respectivement japonais (Jun Hasegawa) et thaïlandais (Donnie Harinsut). Et comme la Thaïlande, le Japon envisage sérieusement de passer à une société plus sans argent liquide, et surtout de lancer une monnaie numérique avant les Jeux Olympiques de 2020. Mais il y a des informations plus concrètes :

- La Krungsri Bank of Ayudhya, investisseur stratégique d'OMG, appartient au plus grand groupe financier du Japon, Mitsubishi UFJ, également appelé **MUFG**. (J et G ne sont pas des fautes de frappe.) MUFG détient des actifs d'environ 2,4 billions de dollars USD, ce qui en fait la 5e plus grande banque du monde en termes d'actifs totaux, et la 2e plus grande société holding bancaire du monde avec 1,8 billion de dollars USD en dépôts.

- **SMBC**, la deuxième plus grande banque du Japon, était un investisseur précoce dans OmiseGO.

- OmiseGO s'associe à **Credit Saison**, la troisième plus grande société de cartes de crédit au Japon, affiliée à **Mizuho**, la troisième plus grande banque du Japon.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dzP5vJVjb6iHc_iWZWzzIw.jpeg)
_Siège de MUFG. Photo [Wikipedia](https://commons.wikimedia.org/wiki/User:Kakidai" rel="noopener" target="_blank" title="">Kakidai</a>, Source MUFG <a href="https://en.wikipedia.org/wiki/Mitsubishi_UFJ_Financial_Group" rel="noopener" target="_blank" title=")_

**3. Singapour et Thaïlande**

Selon un article de Bloomberg [article](https://www.bloomberg.com/news/articles/2017-10-04/singapore-thailand-discuss-e-payment-alliance-for-digital-push), « Singapour et la Thaïlande sont en discussions pour connecter leurs systèmes de paiement numérique nationaux afin de forger une alliance régionale sans précédent, alors que les responsables intensifient leurs efforts pour réduire l'utilisation de l'argent liquide. Le lien réunirait les premières plateformes de paiement numérique d'Asie du Sud-Est, PayNow de Singapour et PromptPay de Thaïlande, a déclaré Naphongthawat Phothikit, directeur de la politique des systèmes de paiement à la Banque de Thaïlande. »

Comme mentionné ci-dessus, PromptPay est le système de paiement mobile interbancaire de Thaïlande via des banques autorisées sélectionnées, y compris la Krungsri Bank of Ayudhya, qui a récemment effectué cet investissement stratégique de 30 millions de dollars dans OmiseGO.

#### **B. Partenaires privés et investisseurs**

**1. TrueMoney**

- En Thaïlande, les 3 plus grands services de paiement électronique sont Paysbuy, AIS (mPAY) et TrueMoney. Omise a récemment acquis Paysbuy, et TrueMoney est un partenaire et actionnaire d'OmiseGO.

Le document de vente groupée d'OmiseGO indique : « En s'intégrant avec OmiseGO, les clients finaux du portefeuille numérique TrueMoney pourront effectuer des transferts d'argent en temps réel à faible coût, des envois de fonds transfrontaliers, des paiements de détail et de factures. Ils pourront également interagir avec d'autres fournisseurs de portefeuilles numériques (« marques ») qui souscrivent au réseau OmiseGO. »

Qu'est-ce que TrueMoney :

- TrueMoney est une marque de technologie financière fournissant des **services de paiement électronique en Asie du Sud-Est** (ASEAN), et ayant **Google** et **Alipay** comme plateformes de paiement partenaires. Ils ont des bureaux en Thaïlande, au Vietnam, au Cambodge, au Myanmar, en Indonésie et aux Philippines, et des licences pour exploiter de l'argent électronique dans presque tous les pays d'Asie du Sud-Est. En Thaïlande, la plateforme comprend TrueMoney Wallet, WeCard avec **MasterCard**, TrueMoney Cash Card, Kiosk, Express, Payment Gateway et Remittance.

- TrueMoney est également connecté au système de paiement mobile interbancaire thaïlandais PromptPay expliqué ci-dessus, via la **Siam Commercial Bank** (SCB). Grâce à ce partenariat TrueMoney / SCB, « davantage de membres du public peuvent profiter d'un accès facile et pratique aux services financiers via PromptPay, qui jusqu'à présent n'était disponible que via un compte bancaire », et SCB permettra aux 3 millions de clients de TrueMoney de charger leur portefeuille électronique PromptPay via les services SCB : SCB Easy App, SCB Easy Net et les distributeurs automatiques.

- Fondée en 2003, TrueMoney appartient désormais au groupe **Ascend Group**, basé en Thaïlande, qui est une scission de True Corporation et appartient au groupe **CP Group**, également basé en Thaïlande, qui est, en Thaïlande, le seul exploitant de plus de 9000 des magasins **7/11** qui permettent l'utilisation de TrueMoney. Il s'agit, encore une fois, de spéculation mais de spéculation significative, de supposer que le partenaire d'OmiseGO, TrueMoney, pourrait, à un moment donné, fournir à leurs très nombreux utilisateurs un service pratique exploitant la technologie OmiseGO et générant des frais sur le réseau OmiseGO.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LrAAcrSDTnHzdtS3FsKapA.png)

- **Ant Financial**, la société chinoise propriétaire du géant du paiement numérique chinois **Alipay**, et appartenant au **groupe Alibaba**, a récemment investi dans Ascend Money du groupe Ascend, qui est, selon les propres mots du PDG d'OmiseGO, Jun, « [l']investisseur / partenaire / soutien [d'OmiseGO] ».

Alipay compte déjà plus de 500 millions d'utilisateurs, commence à cibler les États-Unis, et a déjà réussi jusqu'à 1 milliard de transactions par jour.

**2. McDonald's Thaïlande**

OmiseGO a annoncé une relation formelle avec McDonald's Thaïlande. Aucun détail supplémentaire n'a encore été donné, mais cela peut probablement signifier que les clients de McDonald's pourront payer leurs commandes en utilisant le portefeuille OmiseGO dans les restaurants thaïlandais.

**3. Toppan Printing**

OmiseGO collabore avec Toppan Printing pour commencer à offrir un nouveau type de publicité et de processus d'achat, grâce auquel la numérisation d'un **code QR** sur un support publicitaire, par exemple un magazine, permettra automatiquement au client de commander le produit annoncé.

**4. Global Brain**

OmiseGO prévoit de lancer un [programme d'accélération](https://www.ethnews.com/omisego-global-brain-and-digix-global-to-establish-blockchain-accelerator) en collaboration avec la société de capital-risque japonaise Global Brain, ainsi que plusieurs laboratoires blockchain.

**5. Phase de discussion : Greylock Partners**

OmiseGO a récemment rencontré Greylock Partners, une société de capital-risque de premier plan de la Silicon Valley gérant 3,5 milliards de dollars USD, et travaillant avec des entreprises telles que Facebook, Instagram, AirBnB et Coinbase.

#### **C. Adopteurs d'OmiseGO**

**Hubii Network**, un marché de contenu décentralisé comptant 50 millions d'utilisateurs, a [annoncé](https://medium.com/@jacobotoll/hubii-network-to-use-omisego-for-payments-81d5d7313b3e) qu'ils avaient choisi OmiseGO comme solution évidente pour leur système de paiement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*onc9YkhHvn56b165hv2dcg.png)
_[hubii network](http://hubii.network/" rel="noopener" target="_blank" title=")_

### **4) Le futur**

#### **A. Le futur d'OmiseGO**

**_Que se passera-t-il entre Omise et OmiseGO ?_**

Finalement, toutes les transactions utilisant la solution hors blockchain d'Omise passeront à la blockchain OmiseGO.

**_Quelle est la feuille de route d'OmiseGO ?_**

Comme expliqué ci-dessus, OmiseGO n'est pas une seule application ou service, mais un projet entier, que l'équipe a divisé en 3 couches, qui seront développées au fil du temps, de la plus cruciale à la plus sophistiquée. OmiseGO a commencé à publier des articles de blog décrivant leur feuille de route selon les termes du jeu de Go.

- **Couche 1 : Couche d'acceptation des paiements Omise.**

Le réseau Omise accepte déjà les paiements.

L'étape suivante pour compléter la couche d'acceptation des paiements est la sortie du SDK de portefeuille white-label.

Le prototype du SDK sera publié pour des tests au quatrième trimestre 2017, et la sortie publique est prévue pour le premier trimestre 2018.

**- Couche 2 : Réseau d'échange décentralisé OmiseGO (DEX)**

La sortie publique de la blockchain, incluant le moteur DEX et permettant le staking via le système Proof of Stake, est prévue pour le deuxième trimestre 2018. Jusqu'à présent, et jusqu'à la sortie de Plasma, un environnement de scalabilité intermédiaire sera mis en place, limité au réseau Omise (pas le réseau public OmiseGO entier), utilisant le Cosmos Network. Cela introduira les stakers OMG au protocole PoS et leur permettra déjà de valider des transactions. Cela devrait se produire au quatrième trimestre 2017,

**- Couche 3 : Point de contact décentralisé pour l'entrée/sortie d'argent**

Cette couche permettra aux utilisateurs de numériser de l'argent physique en monnaie numérique (entrée d'argent), et de transformer les monnaies numériques en argent qu'ils peuvent retirer (sortie d'argent). La solution pour cela sera révélée fin 2017, et la date de sortie n'a pas encore été rendue publique.

**- Horizon : DEX compatible multi-chaînes massivement scalable et réseau sans permission permettant les paiements et transferts**

L'état final du réseau OmiseGO nécessitera la sortie de Plasma, dont la date n'a pas encore été annoncée.

#### **B. Pourquoi investir dans OmiseGO**

Tout d'abord, il faut absolument insister à nouveau sur le fait que **_l'auteur de cette revue n'est en aucun cas habilité à donner des conseils en investissement à quiconque_**. Les investissements sont toujours très risqués, et les investissements dans le monde crypto sont encore plus risqués. Donc, comme dans tout autre projet, investir dans OmiseGO est un **risque**, et si vous décidez de prendre ce risque, vous ne devriez jamais investir plus que ce que vous pouvez vous permettre de perdre complètement. Et rien de ce qui est écrit dans cette revue ne réfute ce fait, que vous ne devriez jamais oublier si vous envisagez de mettre de l'argent dans OMG ou dans tout autre projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NmZg-mwemwcdsysMBaKUMg.jpeg)
_L'investissement est risqué / Donald Duck par Don Rosa, Crédit Disney_

Cela dit, le modèle économique de l'investisseur repose sur l'idée que le réseau OmiseGO traitera un très grand nombre de transactions, que ces transactions généreront un montant très élevé de frais, et que, ces frais étant distribués aux stakers OMG, plus vous détiendrez et stakerez d'OMG, plus vous recevrez de montant par an, ce qui, si le projet tient ses promesses, peut se transformer en un revenu passif très rentable.

Il y a 2 raisons principales de croire que le réseau OmiseGO traitera un très grand nombre de transactions :

**1 - Les partenariats**

Les partenariats exposés ci-dessous entre OmiseGO et les banques ou les entreprises privées montrent que potentiellement des millions d'utilisateurs ou plus peuvent se retrouver à utiliser des applications financières fonctionnant sur le réseau OmiseGO, et générer une énorme quantité de frais (bien que chacun soit très faible) à partager entre les stakers OMG.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fSEeeOYL1Ix9GDpWcO1IiQ.jpeg)
_Jeu de Go / Source OmiseGO [blog](https://blog.omisego.network/omisego-roadmap-v-1-40bfca386e25" rel="noopener" target="_blank" title=")_

**2 - Le SDK**

OmiseGO fournit un framework de programmation que toute entreprise ou banque peut utiliser pour créer sa propre application financière (ou d'échange de valeur autre que la valeur financière) pour son propre marché et ses propres utilisateurs, et ces applications créées avec le SDK OmiseGO fonctionneront également sur le réseau OmiseGO, et généreront également une grande quantité de frais. Et encore une fois, le framework de programmation n'obligera en aucune manière les entreprises qui l'utilisent à avoir un logo OmiseGO sur leur application, ni aucune obligation graphique de quelque nature que ce soit. Le SDK ne sera qu'une certaine collection de fonctions programmatiques, afin de : économiser du temps et des coûts de développement de blockchain, en utilisant la blockchain fiable d'OmiseGO, et en utilisant le kit de développement logiciel fiable d'OmiseGO.

En d'autres termes, le SDK OmiseGO peut être vu comme une **passerelle gratuite et facile vers la technologie blockchain et ses applications financières potentielles**, faisant en retour que **toute entreprise ou institution l'utilisant, devient virtuellement un partenaire d'OmiseGO** : si l'entreprise C fournit à ses utilisateurs un portefeuille et une application développés avec le kit de développement logiciel OmiseGO, et a une base d'utilisateurs de 10 000 ou 1 million de personnes, dès qu'ils effectuent des transactions en utilisant l'application fournie par l'entreprise C, ces 10 000 ou 1 million de personnes deviennent **des utilisateurs du réseau OmiseGO**.

Et donc, ces 10 000 ou 1 million de personnes, multipliées par le nombre d'entreprises, de banques ou de services qui utiliseront le SDK OmiseGO, génèrent des frais sur le réseau OmiseGO, distribués entre les investisseurs OmiseGO, appelés stakers ou détenteurs de pièces.

![Image](https://cdn-media-1.freecodecamp.org/images/1*O5aX1AQuN1h5pUkyQphxMg.jpeg)
_Source OmiseGO [blog](https://blog.omisego.network/omisego-roadmap-v-1-40bfca386e25" rel="noopener" target="_blank" title=")_

### **5) Questions Fréquemment Posées**

**_Quel sera le montant des frais du réseau ?_**

Cela n'a pas encore été décidé, sauf que le PDG Jun a déclaré dans un post qu'ils devraient être suffisamment élevés pour représenter un véritable incitatif pour les stakers et ainsi sécuriser le réseau avec un nombre suffisant de nœuds, et suffisamment bas pour en faire un véritable avantage pour les utilisateurs et les entreprises d'utiliser le réseau OmiseGO.

**_Quel sera le montant minimum de pièces OMG requis pour le staking ?_**

Cette information n'a pas encore été publiée.

**_OMG est-il un token ERC20 ?_**

Oui.

**_Le token OMG sera-t-il remplacé par un autre token dans le futur ?_**

Non. Certains autres projets ont remplacé leur token original par un deuxième token à un certain moment de leur développement, mais OmiseGO ne le fera pas. L'OMG que vous possédez maintenant sera l'OMG que vous posséderez dans le futur, il n'y aura aucun changement de token.

**_Où stocker les tokens OMG ?_**

Tout portefeuille compatible ERC20 convient. Une solution populaire est [www.myetherwallet.com](http://www.myetherwallet.com) (attention à taper la bonne URL car des copies miroirs SCAM du site existent), et la solution considérée comme la plus sécurisée est un portefeuille matériel tel que [Ledger](http://ledgerwallet.com/) ou [Trezor](http://trezor.io/). Notez que cet article ne vous donne aucune garantie quant à la sécurité de vos pièces si vous utilisez ces solutions, mais affiche simplement quelques solutions couramment utilisées à des fins d'information.

**_Où acheter OMG ?_**

Vous pouvez acheter OMG sur des plateformes d'échange. Toutes les plateformes d'échange n'acceptent pas les résidents de tous les pays, vous devriez donc vérifier quel site vous pouvez utiliser, et également vérifier la réputation du site sur des forums spécialisés. Actuellement, vous devez d'abord acheter du Bitcoin, du Litecoin ou de l'Ether, puis les échanger contre de l'OMG. Les plateformes d'échange populaires pour acheter OMG incluent Bittrex, Binance ou Bitfinex. Les plateformes d'échange populaires pour acheter du Bitcoin incluent Kraken ou Coinbase. Aucune de ces mentions ne doit être considérée comme un conseil ou une recommandation de quelque sorte que ce soit. Comme toujours lorsque vous faites ce que vous voulez avec votre argent, votre ordinateur et vos informations personnelles, soyez prudent et **faites vos propres recherches**. Et n'oubliez pas de **ne jamais** donner vos clés privées de portefeuille à qui que ce soit ou à un site web sans vérifier trois fois qu'il s'agit de votre fournisseur de portefeuille habituel, comme myetherwallet.com par exemple, et vérifier trois fois l'URL : ajoutez l'URL sécurisée une fois pour toutes en tant que favori dans votre navigateur, et **ne** cliquez **jamais** sur un lien d'un autre site prétendant vous y rediriger, même s'il semble régulier. N'oubliez pas que le monde crypto est rempli de tentatives de piratage, et qu'elles peuvent réussir lorsque les gens ne sont pas assez prudents. **Soyez heureux mais soyez prudent.**

#### **Liens :**

Site web d'Omise : [http://omise.co/](http://omg.omise.co/)  
**Site web d'OmiseGO** : [http://omg.omise.co/](http://omg.omise.co/)  
Note : tout autre site web prétendant être Omise ou OmiseGO est une arnaque. Ne le visitez pas.

**Twitter d'OmiseGO** : [http://twitter.com/omise_go](http://twitter.com/omise_go)  
Twitter de Jun : [https://twitter.com/JUN_Omise](https://twitter.com/JUN_Omise)  
Medium de Jun : [https://medium.com/@jun_omise](https://medium.com/@jun_omise)  
Twitter de Donnie Harinsut : [https://twitter.com/ruxperience](https://twitter.com/ruxperience)

Twitter de Joseph Poon : [https://twitter.com/jcp](https://twitter.com/jcp)  
Twitter de Vitalik Buterin : [https://twitter.com/VitalikButerin](https://twitter.com/VitalikButerin)

**OmiseGO sur Reddit** : [https://www.reddit.com/r/omise_go/](https://www.reddit.com/r/omise_go/)  
OmiseGO sur Slack : [https://omisego.slack.com/](https://omisego.slack.com/)

Site web de Plasma : [http://plasma.io/](http://plasma.io/)  
Site web du Cosmos Network : [https://cosmos.network/](https://cosmos.network/)