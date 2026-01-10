---
title: 'Transactions Ethereum déléguées universelles : plus de frais de transaction'
subtitle: ''
author: Nikita Savchenko
co_authors: []
series: null
date: '2019-09-30T15:53:22.000Z'
originalURL: https://freecodecamp.org/news/universal-ethereum-delegated-transactions-no-more-ethereum-fees
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/you-need-some-ether-1.png
tags:
- name: Blockchain
  slug: blockchain
- name: crypto
  slug: crypto
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: ethereum blockchain
  slug: ethereum-blockchain
- name: token economy
  slug: token-economy
- name: Tokenization
  slug: tokenization
seo_title: 'Transactions Ethereum déléguées universelles : plus de frais de transaction'
seo_desc: 'TL;DR Check this back end and front end solutions for delegated transactions.
  It is universal for any token which supports the delegation of its functions. Read
  more below.


  This mostly technical article provides a universal framework and a working s...'
---

> TL;DR Vérifiez ces solutions [back end](https://github.com/ZitRos/ethereum-delegated-tx-service) et [front end](https://zitros.github.io/ethereum-delegated-tx-widget/) pour les transactions déléguées. Elles sont universelles pour tout token qui supporte la délégation de ses fonctions. Lisez la suite pour plus d'informations.

Cet article principalement technique fournit un **framework universel** et une **solution fonctionnelle** pour les tokens Ethereum et les applications qui éliminent le besoin de payer des frais en Ether, un problème qui tue pratiquement l'expérience utilisateur de nombreuses applications blockchain.

> _Imaginez dépenser des dollars et ensuite devoir également donner quelques_ [_Hryvnias_](https://en.wikipedia.org/wiki/Ukrainian_hryvnia) _en tant que frais de transaction. C'est ainsi que fonctionnent les tokens Ethereum jusqu'à présent._

En d'autres termes, par exemple, pour transférer un token Ethereum (comme [Tether](https://coinmarketcap.com/currencies/tether/), [DAI](https://coinmarketcap.com/currencies/dai/), [BAT](https://coinmarketcap.com/currencies/basic-attention-token/), [DREAM](https://token.dreamteam.gg/), etc.), l'utilisateur doit également dépenser un peu d'[Ether](http://ethereum.org/use/#_2-what-is-eth-and-how-do-i-get-it) (la monnaie interne de la plateforme Ethereum). Cela introduit une grande inconvenance qui empêche l'adoption massive des DApps : les utilisateurs doivent acheter plusieurs devises au lieu d'une seule pour interagir avec le réseau blockchain.

# Le Problème

Les tokens, tels que nous les imaginons aujourd'hui, ne sont que du carburant pour les applications et services sur les réseaux blockchain. Les organisations créent leurs propres tokens (en utilisant des ICO, IEO, etc.) et exécutent des services/applications qui les utilisent, introduisant leur propre micro-économie (largement connue sous le nom de [token economy](https://medium.com/@pentremont/token-economy-101-or-why-blockchain-powered-decentralized-networks-are-important-310de1cc8bac)). Mais presque tous les tokens s'avèrent être des devises assez complexes en eux-mêmes. Par conception de la manière dont les réseaux blockchain fonctionnent, pour faire quelque chose avec vos tokens, vous avez également besoin d'une autre devise — souvent de l'Ether (pour Ethereum) — pour pouvoir transférer des tokens.

Pour illustrer le problème, examinons comment les utilisateurs en viennent à utiliser différents services et applications alimentés par la blockchain comme :

* [Trickle](https://trickle.gg/) - où vous créez des contrats sécurisés et basés sur l'heure avec une partie non fiable dans n'importe quel token
* [Loom](https://loomx.io/) - où vous utilisez des tokens Loom pour créer des sidechains dans le réseau Loom
* [Cryptokitties.co](https://www.cryptokitties.co/) - où vous élevez, échangez et transférez des kitties (tokens ERC721)
* [Autres](https://www.stateofthedapps.com/) (il y en a beaucoup !)

Toutes ces applications utilisent des tokens, ainsi qu'elles vous obligent à acheter de l'Ether. La complexité de l'utilisation des tokens cryptographiques tels que nous les connaissons aujourd'hui est l'une des plus grandes raisons pour lesquelles 99 % des startups crypto échouent (ou évitent d'adopter de vrais crypto, par exemple, en les remplaçant par des pièces virtuelles).

Comme vous le savez peut-être déjà, plus il est difficile d'utiliser l'application, moins elle aura d'utilisateurs dès le début. C'est quelque chose de connu sous le nom de [The User Onboarding Funnel](https://www.appcues.com/blog/user-onboarding-funnel-amplitude), qui reste un gros problème pour les applications et services alimentés par la blockchain :

![Image](https://lh3.googleusercontent.com/XJyaZoGARI3TF4DOjODJerEUNwn3qFm2D8WSZBrxwYE81oSHaw5h3MOweymV5VV9Jby-2OBUE7o1FGkVqZxWvONW0GLuoezAKqt8HmB-N-vPwHL_ouohPO2whDyS1jiXHLIQv9am)
_L'entonnoir typique d'intégration des utilisateurs d'une application décentralisée basée sur la blockchain_

Pour comprendre pourquoi j'ai mis 0,001 % d'utilisateurs avant l'utilisation du service, voyons ce que signifie exactement acheter un peu d'Ether :

* Créer un portefeuille crypto
* S'inscrire sur un échange (et apprendre toutes les règles de l'échange, y compris les politiques des pays !)
* Passer le KYC (bien que cela devienne plus facile, de nombreux pays ont encore un accès limité aux échanges)
* Acheter un montant minimum autorisé d'Ether (généralement, c'est [un énorme 50 $](https://changelly.com/widget-settings) alors que vous n'avez besoin que de près de 0,05 $ pour effectuer une ou deux transactions)
* Retirer l'Ether vers votre portefeuille
* Sans parler de la lecture de guides détaillés sur la manière d'effectuer toutes ces étapes correctement

Au lieu de simplement :

* Créer un portefeuille crypto

Bien sûr, cela dépend beaucoup de la manière dont l'application ou le service est conçu. Mais, jusqu'à présent, il n'y avait pas de meilleure simplification du flux d'intégration que de simplement supprimer les tokens crypto de celui-ci, ou de les rendre faux, une "devise" virtuelle avec une fonction de dépôt et de retrait. Malheureusement, cette dernière approche est désormais la plus courante parmi toutes les startups et entreprises adoptant les crypto, pour de nombreuses bonnes raisons. Une autre raison pourrait être une stratégie de monétisation, mais c'est une autre grande histoire qui mérite un article dédié (Intéressé ? Commentez !).

Revenant au problème des frais de transaction, nous pouvons affirmer ce qui suit, ce qui est difficile à contester.

> _Il est naturel pour l'utilisateur d'acheter **uniquement** la cryptomonnaie dont il a vraiment besoin (par exemple, des tokens :_ [_Tether_](https://coinmarketcap.com/currencies/tether/)_,_ [_DAI_](https://coinmarketcap.com/currencies/dai/)_,_ [_BAT_](https://coinmarketcap.com/currencies/basic-attention-token/)_,_ [_DREAM_](https://token.dreamteam.gg/)_, etc.), et il s'attendrait normalement à payer tous les frais de transaction **dans cette cryptomonnaie**._

Alors pourquoi ne pas simplement leur permettre de le faire ? Parce que c'est en effet assez complexe. Voyons pourquoi, et comment cela vient de devenir plus facile avec notre solution open-source (au moins pour Ethereum).

# Approches Existantes

Dès le début de l'existence de la blockchain, il y avait quelques solutions qui pouvaient simplifier le flux d'intégration des utilisateurs pour le flux représenté ci-dessous, évitant l'étape d'achat d'une devise intermédiaire comme l'Ether. Cependant, créer un portefeuille blockchain n'est pas une étape facile, mais certains utilisateurs qui comprennent la valeur de l'application/service franchissent cette étape assez bien.

![Image](https://lh3.googleusercontent.com/B_D585TaVcYR9qXA-0q3MfvAv1DjGzAulIup0XT1X8Va3eeekX32jAtayKbFCmKoISotoBk_WOyq9jGAdqJzfAnz5q61foOPjgxeVbcfq8bXlA9X25iqzKczy6qmjPvZJgBYsRrL)
_L'entonnoir d'intégration des utilisateurs avec des transactions déléguées_

La solution qui permet d'éviter l'utilisation de devises intermédiaires (Ether pour Ethereum) est appelée "transactions déléguées", ou "méta-transactions".

> _En bref, une transaction déléguée, ou "méta-transaction" dans la blockchain, est le type de transaction qui effectue une action prévue au nom d'un compte, tandis qu'elle est menée (publiée) par un autre compte (délégué), qui paie effectivement les frais pour la transaction._

Il existe [plusieurs](https://medium.com/@austin_48503/ethereum-meta-transactions-90ccf0859e84) [approches](https://fravoll.github.io/solidity-patterns/proxy_delegate.html) [autour](https://medium.com/@e2toe4/ethereum-meta-transactions-36f10448619) [du](https://github.com/ethereum/EIPs/issues/1035) [internet](https://github.com/ethereum/EIPs/issues/1228) du concept généralisé de transactions déléguées que je présente dans cet article. Mais il semble que aucune d'entre elles ne soit encore largement adoptée, car ces approches sont assez complexes par nature, très spécifiques en ce qui concerne la mise en œuvre, et certaines d'entre elles sont **assez complexes à standardiser**. Pour être plus constructif, les approches existantes peuvent être divisées en 3-4 groupes : celles qui utilisent des contrats intelligents proxy, celles qui intègrent la délégation dans un contrat intelligent lui-même et, théoriquement, il y a une opportunité pour la mise en œuvre native de la blockchain (par exemple, Ethereum 2.0).

## 1. Approches de transactions déléguées utilisant des contrats proxy

Les contrats proxy, ou dans ce contexte, les contrats d'identité, sont de petits contrats déployés pour remplacer le compte utilisateur qui souhaite éviter de payer des frais. Ce contrat intelligent est programmé pour agir comme un portefeuille, ainsi que comme un "caller" (expéditeur) des fonctions d'autres contrats intelligents. L'essentiel est qu'il s'agit d'un compte délégué qui déclenche toutes les actions, tandis que le vrai "propriétaire" de ce contrat intelligent est un autre utilisateur. L'utilisateur génère simplement des signatures correctes afin de contrôler ses fonds stockés sur une adresse de contrat intelligent (= dans son portefeuille).

![Image](https://lh3.googleusercontent.com/BqoXbK-n6UmpKY-nu8_GuibFbfA3a2Lrghc_fHSoJOzMqv_MYL2BNzIUzyZPgT1aSM00WC0fJoyErLQKc0Dtu3D92NRdYB3Cm4bJ8vZAnbfHVaSe4pCxrEsI8rvEiNCbQriStqfx)
_Une visualisation de l'apparence des contrats d'identité_

**Avantages de cette approche :**

* Elle fonctionne avec tous les tokens et contrats déjà déployés sur le réseau

**Inconvénients de cette approche :**

* Les utilisateurs ne voient pas les tokens dans leur portefeuille, car ils sont physiquement sur un contrat intelligent d'identité
* Par conséquent, un besoin de développer des interfaces utilisateur personnalisées et des outils/portefeuilles personnalisés
* Déploiement du contrat intelligent d'identité et attribution des frais initiaux, contrairement à l'absence totale de frais
* Nécessite une norme complète pour être largement adoptée

## 2. Transactions semi-déléguées via le modèle "Operator" ([ERC777](https://eips.ethereum.org/EIPS/eip-777))

Il existe une norme de token qui décrit cette approche — [ERC777](https://eips.ethereum.org/EIPS/eip-777). En bref, tout détenteur de token peut autoriser tout autre compte à gérer librement ses tokens. Je ne l'appellerai pas des transactions déléguées, mais néanmoins, je dois mentionner cela, car ici nous déléguons quelque peu le contrôle de vos tokens à d'autres comptes.

![Image](https://lh6.googleusercontent.com/Sf3WEbL4fRfefAZLZIBzxD8nAhLnFt75uIZUSO0SjifRwqbiIwSOUnWf4QkN6v6kmWXBazs05bGnG6w1AOTNZIEXwuVUf6GIPdBNtD60mAwiU5r7Oe4MMlNEGLy5htCrk51zsfwi)
_Une visualisation du modèle "operator" de la norme ERC777_

**Avantages de cette approche :**

* Standardisée

**Inconvénients de cette approche :**

* Très centralisée autour des comptes "operator"
* Sécurité faible en raison du contrôle à 100 % des tokens par les opérateurs
* Frais initiaux pour la transaction d'approbation
* Nécessite un développement supplémentaire d'interfaces utilisateur/outils

## 3. Transactions déléguées intégrées directement dans un contrat intelligent (de token)

Tout comme il est possible de mettre en œuvre des frais personnalisés dans un contrat intelligent proxy, le paiement des frais en tokens peut être mis en œuvre directement dans un contrat intelligent de token. Par exemple, en utilisant l'approche que j'ai décrite dans [mon article précédent](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1), il est possible de mettre en œuvre une fonction dans un contrat intelligent, qui transférera des tokens en acceptant la signature de l'utilisateur, au lieu de demander à l'utilisateur d'appeler directement cette fonction. Nous avons mis en œuvre cette approche dans notre [DREAM Token](https://token.dreamteam.gg/), qui est utilisé sur notre plateforme [dreamteam.gg](https://dreamteam.gg/).

![Image](https://lh3.googleusercontent.com/NTd44yatekkdfGEOfSDdsXi1S8cmtRdkQLXmUKSIm-nFzMMQdOM1Rox1nML6Y2Z8gYh9t_sMIsPvr7L7AHxTPlYXp0ENnVWQBLf5g85Cue-CiR2zb1Xw4Ym4G407MQOhCUUnSrrQ)
_Une visualisation de l'intégration de la délégation dans le contrat de token_

Comme vous pouvez le remarquer, contrairement à l'approche précédente, il n'y a plus de contrat d'identité, et il y a un moyen facultatif d'appeler d'autres contrats intelligents directement depuis le contrat de token.

**Avantages de cette approche :**

* Les utilisateurs voient leurs tokens comme d'habitude sur le solde de leur portefeuille
* Aucun frais initial pour l'initialisation du compte
* Peut ne pas nécessiter de norme (continuez à lire)

**Inconvénients de cette approche :**

* Si vous avez un contrat intelligent (de token) déjà déployé sur le réseau, vous ne pouvez pas appliquer cette approche directement. Bien que vous puissiez toujours déployer un nouveau token et, par exemple, un utilitaire de "migration", qui permettra aux autres utilisateurs d'échanger des tokens (brûler l'ancien token et en frapper un nouveau)
* Parce qu'une norme pour cette approche n'est pas encore bien définie, la mise en œuvre peut varier considérablement
* Un besoin de développer une interface utilisateur/des outils personnalisés pour les transactions déléguées (continuez à lire — résolu !)

## 4. Transactions déléguées au niveau de la plateforme (blockchain)

C'est de loin la meilleure de toutes les approches décrites ci-dessus, mais aussi celle **qui n'est pas encore mise en œuvre nulle part** (par nulle part, je veux dire les plateformes blockchain les plus populaires). Il y a un espoir que son support arrive avec la sortie d'Ethereum 2.0, ou du moins j'ai entendu de Vitalik qu'ils sont en train de faire quelque chose de cool là-bas.

Théoriquement, nous pouvons imaginer cette approche comme étant capable de faire une signature "hors ligne" de deux transactions à la fois : une qui fait quelque chose d'utile pour le compte signataire qui souhaite éviter de payer des frais (par exemple, transférer des tokens) et une autre qui fait quelque chose d'utile pour le délégué (par exemple, payer des frais en tokens au compte qui exécute ces deux transactions).

![Image](https://lh5.googleusercontent.com/R1S5_YVazRlh2mfzuMLaKAnix8GmXJy4swBQyxzWFzhIZhE5nDTZ4gfOLp9G51dx-ydW7sLQCsWkic6k_nVj_1CD8JkHjGjRYSMwt17wGSLAG58Vs2ve02KS3L5m5L2oTCMWfxlG)
_Une visualisation de l'apparence des transactions déléguées natives de la plateforme_

Mais le problème est, concernant Ethereum 2.0, cette fonctionnalité a une chance d'arriver seulement en 2022 ou même plus tard. Je suppose également que cette fonctionnalité nécessitera toujours un back end dédié (similaire à celui qui est introduit dans cet article), car il est difficile d'imaginer comment les mineurs accepteront les frais en tokens. En termes simples, si certains d'entre eux refusent d'accepter les frais en tokens, cela a peu de sens de le faire au niveau "minage" du tout, sans parler de la difficulté à suivre tous les prix et volumes des tokens sur les échanges, de manière décentralisée.

**Avantages de cette approche :**

* Pas besoin de modifier les contrats intelligents déjà déployés
* Aucun frais initial pour l'initialisation du compte
* Peut ne pas nécessiter d'interface utilisateur/outils personnalisés si standardisé

**Inconvénients de cette approche :**

* Très probablement, nécessitera toujours un back end centralisé (le "délégué")
* Pas encore mis en œuvre au niveau de la plateforme (en 2019)

# La Solution

Parmi les quatre approches ci-dessus, à l'exception de l'approche au niveau de la plateforme qui doit encore être mise en œuvre et standardisée en 2022+, la plus attrayante est **la troisième approche**, où nous intégrons les fonctions déléguées directement dans le contrat intelligent de token. Ainsi, nous préservons le paradigme standard des tokens, permettant aux portefeuilles de fonctionner normalement avec le contrat intelligent et n'avons pas besoin d'attendre que les transactions déléguées soient nativement intégrées dans l'une des principales plateformes blockchain. Nous allons nous en tenir à cette approche et la rendre **universelle** juste en dessous.

Le support des transactions déléguées programmé directement dans le contrat intelligent de token est génial. Mais comment gérer ses inconvénients ? En fait, le seul problème qui est difficile à gérer (car vous ne pouvez pas modifier les contrats intelligents existants), **vous devrez déployer un nouveau contrat intelligent de token si vous l'avez déjà déployé sans fonctions déléguées** (par exemple, des tokens ERC20 ou ERC721 standard). L'étape suivante, dans ce cas, serait d'ajouter un moyen de migrer les tokens d'un contrat intelligent à un autre. Par exemple, vous pouvez décider de mettre en œuvre une fonction supplémentaire dans le nouveau contrat intelligent qui permettra aux détenteurs de tokens de migrer leurs actifs depuis l'ancien contrat intelligent.

La mise en œuvre de la fonction de migration de tokens peut varier, en commençant par la mise en œuvre de _receiveApproval_ dans le nouveau token, si le token précédent supporte _approveAndCall_, ou en terminant par l'utilisation du framework _approve_ + _transferFrom_ si vous avez un ERC20 minimal (l'utilisateur _approuve_ les tokens à l'adresse du nouveau contrat de token et appelle ensuite une fonction dans le nouveau contrat qui brûle les anciens tokens et en frappe de nouveaux — mais cela nécessite un frais standard pour l'utilisateur pour la transaction d'approbation). En fait, il y a plus : vous pouvez décider de ne pas brûler les anciens tokens mais de les "verrouiller" sur un nouveau contrat intelligent de token, en frappant de nouveaux tokens — cela ouvre une opportunité de mettre en œuvre une **migration de tokens à double sens**, ce qui est génial — **vous n'aurez pas besoin de lister le token "nouveau" sur l'échange**, tandis que les utilisateurs pourront toujours envoyer l'ancien token aux échanges sans frais en Ether ! Si vous êtes intéressé, veuillez remplir le problème [ici](https://github.com/ZitRos/ethereum-delegated-tx-service/issues) si vous souhaitez connaître plus de détails sur la manière de le faire, car cette approche mérite un tout nouvel article.

Dans mon [article précédent](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1), j'ai fourni un exemple de contrat intelligent de token qui supporte la délégation de fonctions telles que _transfer_, _transferFrom_, _approve_ et _approveAndCall_. Exactement ces fonctions "déléguées" permettent aux utilisateurs de payer les frais en tokens, au lieu d'Ether.

![Image](https://lh6.googleusercontent.com/K95psDr4YlNLWPFIByI6HmE5DOz-uIGmD9xfNODmhfj6oRfkIlGJwkZLPYBEVof4MwitQe5Li6SbUNptplVKL2MfERLbVHLJru5jJkTpCVDnDaQbpMd24wtbWOTp81hX7CHtiRtR)
_Comment fonctionne la délégation dans Ethereum, en bref. Lisez plus dans [cet article](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1)._

Mais cela ne suffisait pas pour commencer l'adoption de masse. Dans cet article, je fournis une solution [back end universelle complète](https://github.com/ZitRos/ethereum-delegated-tx-service) (Transaction Publisher dans l'image ci-dessus), ainsi qu'un [widget configurable](https://github.com/ZitRos/ethereum-delegated-tx-widget) ([vérifiez-le ici](https://zitros.github.io/ethereum-delegated-tx-widget/)), qui vous permet de remplacer les frais en Ether par des frais en tokens dès aujourd'hui.

Quelques points clés avant de plonger dans le sujet :

* Ce back end de transactions déléguées est conçu pour être universel, ou **sans norme**, ce qui signifie que vous pouvez avoir **n'importe quelle implémentation** de fonctions déléguées et **utiliser n'importe quelle norme de signature** dans votre token. Du point de vue du back end, vous devez simplement écrire un fichier manifest pour votre token, décrivant son utilisation.
* Actuellement, la conversion des frais collectés en tokens en Ether est une action manuelle sur les échanges. Mais cela pourrait être une amélioration potentielle pour l'automatisation à l'avenir (si nécessaire).

# Le Concept Derrière la Solution Universelle

Que signifie le fait que le token supporte les transactions déléguées ? Examinons cela en utilisant le token standard ERC20 comme exemple.

## Contrat Intelligent

En ce qui concerne le contrat intelligent de token, l'approche est assez simple. En plus de chaque méthode comme **transfer(to, value)** que nous voulons être "déléguable", nous ajoutons une fonction compagne qui, au lieu d'inspecter **msg.sender**, accepte la signature d'un utilisateur et fait la même chose que ce que la fonction originale était censée faire en validant cette signature à l'intérieur du contrat intelligent. Ainsi, par exemple, pour la fonction **transfer(to, value)**, nous pouvons ajouter la fonction **transferViaSignature(to, value, ...aditionalParams)**. Comme vous le savez de la [cryptographie à clé publique](https://en.wikipedia.org/wiki/Public-key_cryptography), personne ne peut créer une signature valide sauf le propriétaire de la clé privée, c'est pourquoi cette approche est aussi sécurisée qu'Ethereum lui-même.

Et la partie la plus cool est que la mise en œuvre de la fonction déléguée, ainsi que sa signature, n'ont pas beaucoup d'importance, du point de vue du back end délégué. Vous pouvez même décider de mettre en œuvre une fonction "call by signature" pour toutes les autres fonctions que le contrat intelligent supporte. Le back end délégué a juste besoin de savoir **comment** appeler cette fonction, ce qui est résolu en fournissant un manifest de contrat hors chaîne pour le back end délégué. Par exemple, l'argument _additionalParams_ dans **transferViaSignature** peut varier et peut inclure n'importe quoi de cette liste, si ce n'est plus : frais, adresse du destinataire des frais, timestamp d'expiration, une norme de signature utilisée, une signature elle-même, un numéro de nonce ou tout autre identifiant unique de transaction déléguée, etc. En ce qui concerne la conception du contrat intelligent, afin de comprendre pourquoi exactement ces arguments, lisez mon [article précédent](https://hackernoon.com/you-dont-need-ether-to-transfer-tokens-f3ae373606e1).

Nous voulons également permettre aux "délégués" de gagner quelque chose afin de couvrir leurs dépenses en Ether, ainsi que d'être rentables. Ainsi, nous devons ajouter des frais, mais des frais beaucoup plus naturels que l'Ether : des frais dans le token lui-même. Ainsi, par exemple, si vous devez transférer 100 tokens, vous payez 3 tokens supplémentaires au délégué en fonction de son prix et des conditions du réseau pour effectuer un transfert, et cela doit être préservé dans la logique du contrat intelligent.

## Back End

Très bien, maintenant nous avons un token qui permet de transférer les tokens de quelqu'un d'autre en utilisant leur signature. Maintenant, la partie cruciale est d'automatiser le processus de demande et de publication de telles transactions. Et c'est là que notre back end open-source (et un front end) entre en jeu.

Ci-dessous se trouve le diagramme de séquence décrivant comment le front end (client) communique avec le back end, de la demande de transaction déléguée à sa publication sur le réseau :

1. (caché sur le diagramme) Le client demande des informations au back end délégué pour comprendre quels contrats il supporte, ainsi que quelles fonctions il peut déléguer.
2. Le client demande qu'une fonction particulière d'un contrat intelligent soit déléguée. Plus important encore, le back end retourne les frais qu'il facture et les données à signer par le client.
3. Le client signe les données dans son portefeuille. La signature est une opération gratuite, contrairement à la publication de la transaction sur le réseau.
4. Le client envoie sa signature en retour, confirmant ainsi son intention d'effectuer cette transaction déléguée particulière. Le back end valide cette transaction par rapport au réseau actuel.
5. Enfin, le back end publie une transaction sur le réseau.
6. (caché sur le diagramme) Le client interroge constamment le back end pour connaître l'état de la demande déléguée jusqu'à ce qu'il reçoive un état miné. Remarque : il est important d'interroger le back end au lieu d'utiliser un hachage de transaction pour comprendre quand la transaction est minée. Il est très courant que le prix du gaz augmente soudainement, et, afin que la transaction soit minée rapidement, le back end peut la republier avec un prix du gaz plus élevé. Bien que cela ne soit pas encore mis en œuvre, il est très probable que cela le soit bientôt.

![Image](https://lh5.googleusercontent.com/X2SADmcB2aMcJoUgN291XXPdk73sVNi4ebruRwN6TCcDgVWi7ILZs02Mlz0WSR4ufOnzXqxrHIdTSJyijeSKsTw1Z89vB0zjwD8dvQ3Jop6Z4xPKET1TWBnNDBad5QDlD8y0jptG)
_Diagramme de séquence représentant le flux simplifié de la manière dont une transaction déléguée est livrée au réseau_

Cette approche est universelle et ne nécessite que le fichier manifest pour que le back end comprenne comment calculer les frais et quelle norme de signature utiliser du côté client. Voici une autre visualisation des composants du système et de leur séquence d'interaction :

![Image](https://lh4.googleusercontent.com/EmfRndRu7BJyU9UTYVGt_rKlQIE83v21s7UywoeTeZQ3Y832Z85KgYRQgmB4o9bqUS7OExMGy2ace6kc3v7QEL-t0bcsvsg9xu9zqLdKDUrzHWXrhHnwoOQWUkd8GBAOWwLww5e8)
_Diagramme des composants_

Nous avons fourni une [documentation](https://github.com/dreamteam-gg/ethereum-delegated-tx-service#delegated-transactions-concept) complète pour cette solution. Vous pouvez vérifier comment l'API du back end est [structurée](https://github.com/dreamteam-gg/ethereum-delegated-tx-service#api), ainsi que trouver le fichier [manifest du token](https://github.com/dreamteam-gg/ethereum-delegated-tx-service/blob/master/config/contracts/mainnet/0x82f4ded9cec9b5750fbff5c2185aee35afc16587/manifest.js) qui décrit comment travailler avec un [contrat de token particulier](https://etherscan.io/address/0x82f4ded9cec9b5750fbff5c2185aee35afc16587#code). Nous vous encourageons à contribuer avec vos propres tokens !

Et vous n'avez pas besoin de beaucoup de configuration : elle est déjà là avec le front end universel !

## Front End

La [partie front end open-source](https://github.com/dreamteam-gg/ethereum-delegated-tx-widget) des transactions déléguées est l'interface utilisateur qui est **configurée pour chaque token** : il suffit d'exécuter votre back end de transactions déléguées et vous êtes prêt à partir !

![Image](https://lh4.googleusercontent.com/8TagMGFbuyXbiIEe8_x7cmBycjrAxcpE8zyURXmDIF1cQET-K64NchEmK0lWfNpwR5mzcJIQ5YLp--hLSCksLlMflOAPBbDCf2frPrF4xm6cEZ92GNXH-QDA3MBKpokX4O2tZoUq)
_À quoi [il](https://send-token.dreamteam.gg) ressemble_

Il est conçu pour être un widget intégrable, qui guidera l'utilisateur à travers la procédure d'envoi de tokens. Vous pouvez brancher n'importe quel back end, token ou appeler n'importe quelle fonction de token avec lui en utilisant des [paramètres d'URL supplémentaires](https://github.com/dreamteam-gg/ethereum-delegated-tx-widget#embedding) que vous pouvez spécifier.

En utilisant ce widget, et en mettant en œuvre quelque chose de similaire à la fonction largement utilisée mais non standardisée _**approveAndCall**_ dans votre contrat intelligent de token, vous serez en mesure d'appeler d'autres contrats intelligents avec des données arbitraires en payant des frais en tokens !

Voici un guide rapide pour vous si vous souhaitez jouer avec cette interface utilisateur vous-même :

1. Accédez au widget via [ce lien](https://zitros.github.io/ethereum-delegated-tx-widget/?contractAddress=0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa).
2. Il vous demandera de passer au réseau de test Kovan.
3. Obtenez un peu d'Ether de test en utilisant [n'importe quel robinet Kovan disponible](https://www.google.com/search?q=ethereum+kovan+faucet).
4. Utilisez l'Ether de test pour frapper quelques [tokens de test](https://kovan.etherscan.io/address/0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa#writeContract) : appelez la fonction [mintTokens](https://kovan.etherscan.io/dapp/0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa#writeContract) dans un contrat intelligent de token qui vous donnera 10 tokens de test.
5. Maintenant, retournez à [le widget](https://zitros.github.io/ethereum-delegated-tx-widget/?contractAddress=0xcc7e25e30b065ea61814bec6ecdb17edb0f891aa) et essayez de transférer ces tokens !

Si vous ouvrez les outils de développement du navigateur, vous remarquerez qu'il y a quelques back ends connectés par défaut — ils fournissent au front end toutes les informations nécessaires pour effectuer une demande déléguée selon les paramètres d'URL du widget donnés. Tous les backends sont demandés pendant le chargement du widget et, si l'un d'eux peut fournir une délégation pour une fonction particulière d'un contrat, alors le widget demande des informations supplémentaires : frais, signatures supportées, etc. Si plusieurs back ends peuvent déléguer la même fonction de contrat, ils sont tous demandés et le back end qui fournit les meilleurs frais sera utilisé pour la transaction.

Le temps de minage des transactions semble fixe, mais il peut varier en raison des conditions du réseau. Le back end utilise des frais de réseau réels lors du calcul des frais de token, cependant, ils peuvent changer avant que l'utilisateur ne décide d'exécuter la transaction. Ainsi, la transaction "sous-évaluée" est soumise au réseau et peut être en attente pendant un certain temps. Bien que le back end ne soit actuellement pas programmé pour gérer ce cas, il pourrait être mis en œuvre à l'avenir — les transactions seront republées avec des frais de gaz plus élevés en cas d'augmentation des frais de réseau. Mais nous devrons également en tenir compte dans les frais de token.

## Normes de Signature

La dernière question que vous vous posez peut-être est — quelle norme de signature utiliser pour votre token. Il en existe plusieurs disponibles : _eth_sign_ (obsolète), _eth_personalSign_ (notez que les anciens [Trezor](https://trezor.io/) et [Ledger](https://www.ledger.com/) produisent des signatures différentes en raison de l'ambiguïté dans une norme, vous pouvez donc vouloir inclure les deux), _eth_signTypedData_ (obsolète), [_eth_signTypedData_v3_](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26) et ainsi de suite. Je recommanderais de supporter au moins deux : l'intemporel _eth_personalSign_ et le nouveau [_eth_signTypedData_v3_](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26) (en 2019).

![Image](https://lh3.googleusercontent.com/TZhSpdfJF_035M1uCARZVYixZC4W8hsiG1jbs2zTyYZQC5fpwJUR3W7x14WaLofyklmEaR9O4Cgt7EkKb7MCb1RHK6geJfxKb-oGVVxlOXBOu6dh5c6nRtNwblF5B0sZ07Gf6mV7)
_Comparaison des normes de signature — ce que l'utilisateur voit_

Le front end est programmé pour toujours préférer la norme lisible par l'utilisateur comme [eth_signTypedData_v3](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26) à toute autre eth_personalSign. Donc si votre token supporte de nombreuses normes de signature, et que vous les avez toutes ajoutées au [fichier manifest](https://github.com/dreamteam-gg/ethereum-delegated-tx-service/blob/master/config/contracts/mainnet/0x82f4ded9cec9b5750fbff5c2185aee35afc16587/manifest.js) de votre token, il affichera d'abord l'invite [eth_signTypedData_v3](https://medium.com/metamask/eip712-is-coming-what-to-expect-and-how-to-use-it-bb92fd1a7a26).

# Conclusion

Les transactions déléguées sont géniales : elles résolvent l'un des plus grands problèmes de l'adoption des applications blockchain, ce qui facilite l'adoption massive des cryptomonnaies en général. Je vais mettre quelques thèses en format Q&A ici pour répondre aux dernières questions que vous pourriez encore avoir après avoir lu cet article :

* Notre solution open-source est gratuite et prête pour la production, n'hésitez pas à l'appliquer à vos applications ou tokens !
* L'approche décrite ne compromet ni la sécurité ni la centralisation. Pensez ainsi : le back end centralisé n'est qu'un assistant pour quelqu'un qui souhaite transférer des tokens sans frais en Ether. Si le back end est piraté, ou s'il est simplement indisponible, il n'y a aucun problème à interagir avec le réseau comme avant, en payant des frais en Ether. De même, le back end ne peut pas nuire ou tromper l'utilisateur pour voler ses tokens lorsqu'une norme de signature appropriée est utilisée (c'est à votre implémentation de token de le garantir).
* Il existe un moyen de supporter les transactions déléguées pour les tokens existants, déjà déployés. Cependant, cela nécessite une étape supplémentaire consommant de l'Ether pour migrer les tokens existants vers un nouveau contrat de token. Et, en programmant correctement un nouveau contrat de token, ainsi qu'en concevant votre application pour qu'elle fonctionne avec les deux tokens, vous pouvez même éviter le besoin de lister un nouveau token sur les échanges.
* En utilisant [les tokens existants comme exemple](https://github.com/zitros/ethereum-delegated-tx-service/blob/master/config/contracts/mainnet/0x82f4ded9cec9b5750fbff5c2185aee35afc16587/manifest.js), qui est disponible dans les dépôts de transactions déléguées [back end](https://github.com/zitros/ethereum-delegated-tx-service) et [front end](https://github.com/zitros/ethereum-delegated-tx-widget), vous pouvez produire votre propre manifest pour votre propre token.
* [Lisez les instructions](https://github.com/zitros/ethereum-delegated-tx-service#setup) sur la manière de configurer votre propre back end pour un token, puis ajoutez-le à l'URL de votre widget (ou commitez-le dans le dépôt open-source).
* Vous avez un token qui supporte déjà les transactions déléguées ? Intégrez-le dans [notre UI](https://zitros.github.io/ethereum-delegated-tx-widget) avec ces trois étapes assez simples : (1) créez un manifest pour votre token et placez votre fichier abi de token lors de la configuration du back end délégué, (2) exécutez ce back end, en exposant une URL d'API publique et (3) utilisez les paramètres d'URL dans un widget pour référencer votre back end ou commitez-le directement dans notre dépôt open-source. Lisez plus à ce sujet dans le fichier readme de GitHub.

J'espère que cela a été une information vraiment utile pour tous les chercheurs de l'incroyable. N'hésitez pas à me contacter [ici](https://nikita.tk/) ou à remplir le problème [ici](https://github.com/ZitRos/ethereum-delegated-tx-service/issues) si j'ai manqué quelque chose. Amusez-vous, que l'économie des tokens soit simple !