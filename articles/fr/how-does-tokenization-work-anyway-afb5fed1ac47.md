---
title: Comment fonctionne la tokenisation, au fait ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-20T13:06:04.000Z'
originalURL: https://freecodecamp.org/news/how-does-tokenization-work-anyway-afb5fed1ac47
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7pMYW1axSFq7uO09x3UoqA.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Ethereum
  slug: ethereum
- name: Tokenization
  slug: tokenization
seo_title: Comment fonctionne la tokenisation, au fait ?
seo_desc: 'By Albert Ho

  Not everything will be tokenized, but that which can be will be.


  2017 saw the hype of utility tokens and ICOs. 2018 marks the hyped start of asset
  tokenization and the launch of securities tokens/platforms. This trend is notably
  huge in...'
---

Par Albert Ho

#### **Tout ne sera pas tokenisé, mais ce qui peut l'être le sera.**

![Image](https://cdn-media-1.freecodecamp.org/images/3S1xyeWzGYjjVeZp5EGSY1S6gFYFUEyYLl12)

2017 a vu l'engouement pour les tokens utilitaires et les ICO. 2018 marque le début hypé de la tokenisation d'actifs et le lancement de tokens/plateformes de titres. Cette tendance est particulièrement importante aux États-Unis, étant donné comment A16z et GGV Capital ont investi dans des plateformes de tokenisation comme [TrustToken](https://blog.trusttoken.com/trusttoken-raises-20-million-usd-in-strategic-round-88912d1dbc71), [Harbor](https://techcrunch.com/2018/04/17/harbor-securities-tokenization/), et [Polymath](https://www.businessinsider.sg/a-startup-raised-59-million-in-a-token-sale-to-usher-in-the-next-generation-of-crypto-2018-2/?r=US&IR=T).

En Asie, la tendance commence également à se développer. Par exemple, [Rate3 Network](https://rate3.network) a été financé par divers VC asiatiques notables, dont Matrix Partners China et Fenbushi Capital.

Conceptuellement, la tokenisation _peut sembler_ facile : émettre un token ERC-20 (ou tout autre token blockchain), imputer des droits juridiques et des droits de propriété dans les tokens, et vous pouvez les échanger facilement. Cependant, cela mérite un examen beaucoup plus approfondi : comment distingue-t-on les droits de réclamation et les droits de propriété ? Quelles sont les différences de tokenisation entre les différentes classes d'actifs ? Qu'est-ce qui entrave l'adoption de la tokenisation ?

Penser de manière exhaustive à la tokenisation nécessite une compréhension des blockchains et des smart contracts, du juridique, de la finance et de l'économie. Il y a déjà eu des recherches approfondies sur chacun de ces composants.

Dans cet article, je souhaite donner une introduction complète à la tokenisation en utilisant l'immobilier comme exemple principal. Voici ce que nous allons discuter :

* [Qu'est-ce que la tokenisation _exactement_ ?](#questceque) _(N'est-ce pas simplement de la titrisation ?)_
* [Quels sont les _vrais_ avantages de la tokenisation ?](#avantages) _(Pourquoi s'en soucier ?)_
* [Quels sont certains des _problèmes_ plus difficiles à considérer ?](#problemes) _(Comment poser les bonnes questions ?)_
* [Quels sont les _défis_ pour la tokenisation ?](#defis) _(Qu'est-ce qui bloque l'adoption ?)_
* [À quoi ressemblera l'avenir _tokenisé_ ?](#avenir) _(Quels sont certains éléments ?)_

**Commençons !**

### Qu'est-ce que la tokenisation ?

#### La tokenisation n'est-elle pas simplement de la titrisation ?

Pour les professionnels de la finance structurée, la tokenisation _peut_ sembler être de la titrisation. En résumé, la titrisation consiste en quelques étapes :

1. L'originateur (propriétaire des actifs) collecte les actifs dans un pool et transfère le pool à une entité légale (généralement un véhicule à usage spécial). Grâce à cette structure légale, les actifs ne sont pas exposés aux risques de contrepartie ou au risque de faillite de la banque originatrice.
2. Le SPV structure les actifs au sein du pool en plusieurs tranches, selon différents niveaux de risque et caractéristiques généralement. Des titres sont émis, et garantis par les flux de trésorerie générés par les actifs sous-jacents.
3. Après l'émission des titres, le SPV vend les titres aux investisseurs, tout en transférant les produits à l'originateur par la suite.

#### **La titrisation** présente divers défauts.

Le processus classique de **titrisation** est extrêmement coûteux et prend beaucoup de temps. L'ensemble du processus peut coûter jusqu'à des millions de dollars et prendre jusqu'à un an. Le processus de titrisation nécessite des accords avec diverses parties dans des conditions d'information asymétrique, ainsi qu'une structure hétéroclite des données d'actifs.

De plus, il peut y avoir un manque de transparence totale dans les diverses étapes de la titrisation, ce qui entrave l'audit et la notation des actifs sous-jacents. Dans la crise des subprimes, il n'y a pas de transparence sur le pool de crédits ni sur le processus d'audit qui a conduit aux défauts sur les obligations émises.

#### Clairement, tokenisation ≠ titrisation

La tokenisation — dans sa définition la plus simple — fait référence à la conversion d'un actif en un token numérique sur le système blockchain. La plus grande différence entre la tokenisation et la titrisation réside dans la manière dont la programmabilité est introduite dans l'actif tokenisé. Ainsi, la logique métier peut être introduite, réduisant le besoin de règlements manuels. Les smart contracts peuvent avoir des fonctions pour les transactions automatiques, des formules pour calculer les prix des actifs et d'autres caractéristiques spécifiques.

### Quels sont les vrais avantages de la tokenisation ?

![Image](https://cdn-media-1.freecodecamp.org/images/-W6AlP3OdocdH7XlQG3vxR6Ki2ifpbdwyCfS)
_Photo par @sanfrancisco, Unsplash_

De nombreuses recherches ont parlé des divers avantages de la tokenisation, mais ces divers avantages peuvent être catégorisés en trois principes fondamentaux : 1) **liquidité**, 2) **programmabilité** et 3) **preuve immuable de propriété**.

#### Principe clé 1 : Liquidité

Le [World Economic Forum](http://www3.weforum.org/docs/WEF_GAC15_Technological_Tipping_Points_report_2015.pdf) prédit que, au cours des dix prochaines années, 10 % du PIB mondial sera stocké dans des actifs cryptographiques, soit 10 000 milliards de dollars. Cela est principalement dû à l'augmentation de la propriété fractionnée et au déverrouillage des primes de liquidité.

En supposant qu'il n'y ait pas de barrières juridiques et réglementaires, la tokenisation permet une augmentation de la propriété fractionnée. La plupart des tokens peuvent être divisés en 18 décimales, contre 0,01 $ pour la monnaie fiduciaire. La propriété fractionnée abaisse les barrières à l'entrée pour les nouveaux investisseurs. Par exemple, au lieu de payer 1 million de dollars pour un nouvel appartement, je peux payer 50 000 dollars pour une fraction tokenisée de l'immobilier. Pour les investisseurs, la propriété fractionnée et les barrières plus basses les aident à augmenter la diversification de leur portefeuille et à construire un portefeuille de marché plus "vrai".

L'augmentation de la liquidité aide à déverrouiller de la valeur pour les marchés grâce aux primes de liquidité. Lorsque les actifs illiquides deviennent plus liquides, une [prime de liquidité](http://people.stern.nyu.edu/adamodar/pdfiles/country/illiquidity.pdf) d'environ ~20–30 % est déverrouillée. Un exemple est l'immobilier : même une amélioration fractionnée du prix de vente de tels investissements pourrait entraîner des milliers de milliards de dollars de nouvelle valeur pour les émetteurs et les revendeurs.

#### Principe clé 2 : Programmabilité intégrée aux tokens

La programmabilité fait référence à la capacité d'introduire _certaines_ logiques métier dans les smart contracts, permettant à des événements automatisés de se produire. La tokenisation peut également conduire à une gestion plus facile des investisseurs et de leurs droits. Les transactions secondaires peuvent être facilement suivies en collaborant avec des bourses tierces, permettant aux investisseurs de recevoir des distributions et d'exercer leurs autres droits (par exemple, le vote) via la blockchain.

La programmabilité est particulièrement utile pour augmenter la vitesse des règlements. Dans la finance traditionnelle, les règlements font référence au processus de documentation du transfert de propriété d'actifs avant que la propriété des actifs ne change réellement de mains. La conformité peut être programmée dans les tokens, si tous les participants ont une identité numérique qui a subi les vérifications de conformité/KYC/AML pertinentes.

#### Principe clé 3 : Preuve immuable de propriété

Les blockchains sont immuables et conservent une trace publique de chaque transfert et propriétaire. Cette trace numérique des transactions prouve non seulement l'historique de la propriété, mais aide également à réduire la fraude. La structure immuable rend impossible pour un détenteur de token de "double-vendre" un token — accepter un transfert pour le même token à deux sources différentes. Cela aide à rassurer les investisseurs que personne ne peut falsifier les transactions après qu'elles aient eu lieu.

### Approfondissons la tokenisation.

_La tokenisation est le processus de stockage numérique des droits de propriété sur un bien de valeur (actif) sur une blockchain ou un registre distribué, de sorte que la propriété puisse être transférée via le protocole de la blockchain. Quels sont les autres défis ?_

#### Problème #1 : Quelles sont les exigences pour que la tokenisation ait lieu ?

Il y a 3 exigences fondamentales :

1. **Les droits sur un actif peuvent être stockés numériquement sur une blockchain**

Revenons à l'exemple de l'immobilier. Si je veux tokeniser ma maison, je dois pouvoir enregistrer ma propriété sur un token lui-même. Cela signifie que pour les autorités de réglementation, détenir un token représente un droit de propriété ou un droit de réclamation sur la maison elle-même. _(Nous aborderons ces droits dans un instant.)_

**2. Ces droits peuvent être légalement transférés via les blockchains**

Bien que je puisse documenter mes droits sur ma maison de manière légalement reconnue, je devrais pouvoir transférer ces droits à qui je veux et cette personne aura la propriété légale de ma maison, en supposant que mes tokens soient imbués de droits de propriété.

**3. Les tokens peuvent être facilement échangés contre de la valeur, donnant aux actifs une "valeur"**

Enfin, comme pour tout titre, je dois pouvoir échanger mon token immobilier contre de la valeur facilement — pour que je puisse souscrire de la valeur à l'actif.

#### Problème #2 : Quels sont les autres problèmes juridiques à considérer ?

Outre les 3 exigences, ce qui est plus crucial à noter est l'actif exact que vous tokenisez : le token représente-t-il une réclamation sur l'actif ou le token représente-t-il la propriété réelle de l'actif lui-même ? Les investisseurs et les émetteurs de tokens doivent réfléchir soigneusement à ce que représente exactement un token.

**La vérité est : cela dépend de ce que vous voulez tokeniser. La tokenisation est flexible.** En utilisant à nouveau l'immobilier comme exemple, ce qui peut être tokenisé pourrait être la propriété directe de l'immobilier (être un propriétaire partiel en capital), le droit aux revenus locatifs, ou même le droit d'utiliser un actif (louer l'appartement).

Ainsi, un token pourrait représenter la _propriété_ de l'actif réel sous-jacent, un _intérêt dans une dette_ garantie par l'actif, un _intérêt en capital_ dans une entité légale qui possède cet actif, ou un _droit au flux de trésorerie_ de l'actif.

### Il y a 3 catégories de base de droits à comprendre.

Les droits conférés par les titres tokenisés (ou jetons de sécurité) peuvent être très complexes à comprendre. Cependant, les titres tokenisés peuvent inclure des réclamations sur les actifs (et généralement les flux de trésorerie résultants), des droits de propriété directs, des droits de gouvernance ou une combinaison de tout cela.

1. **Droits de réclamation** : Réclamations pour seulement certaines utilisations spécifiques (et réclamations) de l'actif
2. **Droits de propriété** : Propriété en capital et contrôle de l'actif
3. **Gouvernance** : Système par lequel un groupe de personnes peut parvenir à des décisions unifiées

#### Illustrons cela à nouveau avec l'immobilier, avec quelques exemples sur les droits des détenteurs de tokens :

1. **Droits de réclamation, mais pas de droits de propriété** : Les détenteurs de tokens ont droit aux flux de trésorerie des baux en cours, mais ils n'ont pas de "capital" et de "propriété" de l'immobilier sous-jacent.
2. **Droits de réclamation, ET droits de propriété** : Les détenteurs de tokens sont les "propriétaires" de l'immobilier sous-jacent avec des droits sur les flux de trésorerie. Ils peuvent prendre des décisions directement : combien facturer pour le loyer, les investissements faits pour maintenir l'immobilier, l'embauche de personnel et les produits de la vente de l'immobilier.
3. **Uniquement des droits de propriété** : Cet exemple est rarement le cas, mais cela signifie que les détenteurs de tokens sont maintenant les "propriétaires en capital" de l'immobilier.

#### Quels sont les défis qui découlent de ces différents droits ?

Il est possible qu'il y ait une séparation des droits de réclamation et des droits de propriété, et cela crée des incitations désalignées entre les deux parties.

**Et si... les tokens ont des droits de propriété pour les détenteurs de tokens ?** Comment 1 000 détenteurs de tokens prennent-ils des décisions collectivement pour le meilleur des actifs ? Y a-t-il besoin de vote délégué ou de prise de décision ?

**Et si... les tokens n'imbuent que des droits de réclamation pour les détenteurs de tokens ?** Les émetteurs de tokens (propriétaires) peuvent réduire les profits et les flux de trésorerie pour les détenteurs de tokens, en réinvestissant les profits. Cela sera au détriment des détenteurs de tokens qui regardaient initialement vers le flux de trésorerie futur.

Le passionné de smart contracts pourrait demander : _ne peut-on pas automatiser toute cette logique dans les smart contracts ?_

### Non, les smart contracts ne peuvent pas résoudre tous ces problèmes.

![Image](https://cdn-media-1.freecodecamp.org/images/lP3pwrUqO9p3X0gH66HrJVmelSsIPHUmAh18)

Les contrats et les smart contracts sont **_incomplets_** :

1. _Les contrats ne sont exécutoires que lorsque les événements et les actions peuvent être vérifiés par une tierce partie_

C'est le problème de longue date des **_oracles_** dans la tokenisation. Il y a certains événements qui peuvent être capturés en code, mais presque impossibles pour tout arbitre de déterminer s'ils se sont réellement produits.

Par exemple, j'ai émis des tokens immobiliers aux détenteurs afin qu'ils puissent recevoir une partie des revenus locatifs. Cependant, il est possible que je ne documente pas tous les accords de location de sorte que les détenteurs de tokens ne savent pas quel est le montant réel des revenus locatifs. Si cela ne peut pas être appliqué efficacement, il n'y a aucune raison rationnelle pour que les parties se conforment au smart contract.

_2. Il est presque impossible d'écrire un contrat qui contient toutes les conditions et événements possibles, atteignant ainsi la "complétude"_

Le problème avec les contrats n'est pas ce qui s'y trouve, mais ce qui n'y est pas. Il est très coûteux et opérationnellement difficile d'écrire chaque condition et événement. De plus, les événements et les conditions changent dans la vie réelle — et les contrats doivent s'adapter à ces changements de la vie réelle.

Étant donné les limitations des smart contracts en tant qu'incomplets par nature, certains types d'actifs ne devraient pas être tokenisés.

### Qu'est-ce qui ne devrait pas être tokenisé ?

1. **Lorsque la blockchain ne peut pas capturer pleinement le changement de propriété des actifs**

Il existe certains actifs sur les marchés où je peux vendre l'actif physique en dehors du protocole directement, malgré sa tokenisation. Par exemple, je peux tokeniser un bien immobilier et transférer le token (avec des droits de propriété) à vous, mais il est possible que je puisse également vendre légalement le même bien immobilier à une autre personne.

Il existe également d'autres cas où je peux échanger des tokens, mais sans garantie que je puisse vérifier l'authenticité de l'actif sous-jacent. Dans le cas de l'immobilier, il est plus facile de vérifier, mais d'autres exemples incluent les lingots d'or. Si cela prend beaucoup de coûts et de ressources pour vérifier l'authenticité, la tokenisation pourrait ne pas être une solution viable.

**2. Lorsque l'utilisation des prix empêche le protocole d'atteindre ses objectifs**

Il existe certaines situations dans lesquelles nous ne _voulons_ pas que les prix déterminent qui obtient quoi. Parfois, les prix ne capturent pas les bénéfices et coûts sociétaux externes, et pourraient ne pas être le moyen le plus équitable d'allouer les ressources. Les exemples incluent les biens sociaux, par exemple.

**3. Parfois, nous ne _voulons_ tout simplement pas tokeniser certains "actifs" et droits**

Par exemple, les droits aux actes de naissance ou aux dossiers scolaires ne devraient pas être tokenisés puisqu'ils représentent un droit _unique_. Nous ne devons pas, et ne devrions pas, tokeniser ces "actifs".

Clairement, il existe certaines classes d'actifs qui _ne devraient pas_ être tokenisées, étant donné les limitations de la vie réelle.

### Comment tokeniser vraiment ?

Nous avons passé en revue le _quoi_ et le _pourquoi_ de la tokenisation, parlons maintenant un peu du _comment_ de la tokenisation.

Il existe quelques catégories d'actifs qui ont été tokenisés :

* **Monnaies fiduciaires**

La tokenisation des monnaies fiduciaires a donné naissance aux stablecoins. [Tether](https://tether.to) est le premier exemple, créant l'USDT. Cependant, il existe des défis inhérents avec Tether. Pour un bon résumé mis à jour sur les stablecoins, je suggère ceci :

[**Les stablecoins sont maintenant officiellement à la mode à nouveau**](https://blog.goodaudience.com/stablecoins-are-now-officially-in-vogue-again-131383ab8db9)  
[_Avec apparemment un nouveau projet dévoilant un financement de plusieurs millions de dollars toutes les deux semaines, personne ne vous blâmera pour..._blog.goodaudience.com](https://blog.goodaudience.com/stablecoins-are-now-officially-in-vogue-again-131383ab8db9)

* **Or**

Un exemple de projet de tokenisation de l'or est [Digix](https://digix.global/dgx/).

Chaque token DGX est garanti à 1:1 par de l'or, et 1 token représente 1 gramme d'or à 99,99 % de la London Bullion Market Association, avec de l'or stocké dans le coffre-fort The Safehouse. L'achat de 1 token DGX équivaut à l'achat d'or réel.

* **Immobilier**

Mon intérêt principal réside dans l'immobilier, étant donné l'analogie entre les REITs et l'immobilier tokenisé. Quelques exemples intéressants sont [comment un bien immobilier de Manhattan a été récemment tokenisé](https://www.forbes.com/sites/rachelwolfson/2018/10/03/a-first-for-manhattan-30m-real-estate-property-tokenized-with-blockchain/#537f78784895), ou [comment une partie du St. Regis Aspen est tokenisée](https://venturebeat.com/2018/10/09/elevated-returns-gets-18-million-for-st-regis-aspen-resort-tokenized-real-estate/). Dans le cas du St. Regis Aspen, chaque token Aspen représente un intérêt de propriété indirect dans une action ordinaire du St. Regis Aspen REIT. Selon Elevated Returns, le "REIT fournit une structure fiscalement efficace tandis que la blockchain fournit des investissements de pair à pair et des transactions transfrontalières simplifiées pour les investisseurs."

### Clairement, il y a de nombreux défis associés à la tokenisation.

#### 1. Manque de normes de tokenisation et d'infrastructure juridique

La tokenisation n'est pas simplement la création d'un token — tout développeur Solidity peut le faire. Au lieu de cela, il s'agit de la conception de l'ensemble du système, y compris la compréhension des divers droits et problèmes dont nous avons parlé précédemment.

Comment les normes de tokenisation répondent-elles à ces problèmes :

* Incitations (droits de réclamation, droits de propriété, gouvernance)
* Privilèges des utilisateurs et des administrateurs système (qui exploitent les contrats de tokens)
* Gestion du cycle de vie d'un actif (émission, paiements, retrait)
* Gestion de la sécurité
* Intégration des exigences KYC/AML à travers différentes juridictions
* Intégration avec les bourses
* Interopérabilité entre différentes chaînes publiques

Dans le cas de l'interopérabilité inter-chaînes, nous voyons différentes chaînes avec différentes caractéristiques naissantes. Par exemple, Ethereum a des problèmes de scalabilité mais permet des smart contracts Turing-complets plus complexes. Qu'en est-il des autres réseaux blockchain publics comme Stellar, IOST ou Zilliqa ?

_Comment les actifs tokenisés (sous forme de tokens) peuvent-ils être interopérables à travers ces différentes chaînes ?_

#### 2. Identité numérique globalement et légalement reconnue

D'un point de vue réglementaire, c'est un cauchemar réglementaire pour les actifs d'être émis et transférés entre des citoyens de différentes juridictions légales.

Supposons que je sois un résident de l'UE cherchant à tokeniser mon bien immobilier et que le token n'imbue que des droits de réclamation. Comment puis-je transférer ce token à des personnes aux États-Unis, tout en tenant compte de leur identité, des problèmes KYC/AML, des réglementations américaines, des taxes et de tous les autres problèmes ?

_Comment puis-je raisonnablement et facilement traiter avec une personne américaine vérifiée et attestée de manière légalement conforme pour nos juridictions nationales respectives ?_

#### 3. La tokenisation ne signifie pas une liquidité instantanée

La liquidité est le plus grand défi dans l'espace des tokens de sécurité et elle ne se produit pas de manière organique. L'histoire nous a donné divers exemples de marchés financiers et d'instruments qui n'ont pas encore atteint des niveaux significatifs de liquidité. Aider à créer de la liquidité en permettant aux investisseurs institutionnels ou aux investisseurs de détail accrédités — par le biais de solutions de garde — sera clé. Bien sûr, l'actif sous-jacent doit être utile.

_Comment introduisons-nous des solutions durables à long terme pour les grands investisseurs institutionnels — les teneurs de marché — pour créer et maintenir la liquidité ?_

### À quoi ressemble un avenir tokenisé ?

![Image](https://cdn-media-1.freecodecamp.org/images/VROVXufGdaPXFsGlBxX3mnk1zyqtHrnrX0Wi)

Je suis généralement optimiste quant à un avenir tokenisé : un monde plus juste et plus équitable avec des barrières d'entrée et des exigences de capital plus faibles pour les individus ou les entreprises.

En capturant la valeur dans des actifs tokenisés, nous pouvons recréer toute la sophistication du monde financier et opérationnel existant dans lequel nous vivons, avec beaucoup moins de coûts opérationnels et de complexités. En combinant la tokenisation avec une logique métier raisonnablement complexe activée par des smart contracts, nous pouvons représenter des interactions commerciales complexes de manière fidèle et plus efficace.

#### Il y aura de l'interopérabilité, grâce à la standardisation

**ERC 20 pour les normes de tokens, comme exemple**

Si l'écosystème des actifs mondiaux devient interopérable, cela signifie que nous pouvons détenir des droits de propriété sur un bâtiment commercial, des actions en phase de démarrage, des obligations d'entreprise, un bon du Trésor, une résidence unifamiliale et un réseau décentralisé sur la même plateforme.

Différents actifs peuvent se référencer mutuellement de manière contractuelle et interagir de manière automatisée. Cela signifie une liquidité accrue pour tous (les classes d'actifs tokenisés).

**ERC 725 pour l'identité, comme autre exemple**

[Fabian Vogelstellar](https://twitter.com/feindura?lang=en) — créateur de la norme ERC 20 — mène la charge pour une identité décentralisée unique pour les "humains, groupes, objets et machines". En citant directement le Github ERC 725 lui-même, "Cette identité peut détenir des clés pour signer des actions (transactions, documents, connexions, accès, etc.), et des réclamations, qui sont attestées par des tiers (émetteurs) et auto-attestées ([#ERC735](https://github.com/ethereum/EIPs/issues/735)), ainsi qu'une fonction de proxy pour agir directement sur la blockchain".

Vous pouvez en lire plus ici sur _ERC 725_ ici :

[**ERC : Identité · Problème #725 · ethereum/EIPs**](https://github.com/ethereum/EIPs/issues/725)  
[_eip : titre : ERC-725 Identité auteur : Fabian Vogelsteller (@frozeman) discussions-to..._github.com](https://github.com/ethereum/EIPs/issues/725)

Il y a des projets notables qui ont travaillé sur la mise en œuvre des contrats d'identité ERC 725. Quelques exemples sont : [Origin Protocol](https://www.originprotocol.com/en) et [Rate3 Network](https://rate3.network).

[**Gérer l'identité avec une UI pour ERC 725**](https://medium.com/originprotocol/managing-identity-with-a-ui-for-erc-725-5c7422b38c09)  
[_Chez Origin, nous construisons une plateforme pour des marchés décentralisés, pair-à-pair. Vous pouvez imaginer un futur Airbnb-like..._medium.com](https://medium.com/originprotocol/managing-identity-with-a-ui-for-erc-725-5c7422b38c09)[**Protocole d'identité inter-chaînes Rate3 — Identité et Réclamations (ERC 725, ERC735)**](https://medium.com/official-rate3/rate3-cross-chain-identity-protocol-identity-and-claims-erc-725-erc735-c6e51f422e7b)  
[_Chez Rate3, nous voulions initialement construire un réseau de règlement et de compensation basé sur la blockchain pour les entreprises. Nous..._medium.com](https://medium.com/official-rate3/rate3-cross-chain-identity-protocol-identity-and-claims-erc-725-erc735-c6e51f422e7b)

### L'avenir de la tokenisation n'est pas encore là (encore), mais il arrivera plus tôt que nous le pensons

Nous sommes optimistes et enthousiastes quant à l'avenir de la tokenisation et des titres tokenisés. Il y a de nombreux éléments de l'avenir tokenisé envisagé que nous observons aujourd'hui :

1. **Les gouvernements s'associent de plus en plus avec des entreprises privées pour créer des solutions infrastructurelles**

Un exemple est la collaboration entre _NASDAQ_, _Monetary Authority of Singapore_ (la banque centrale de Singapour) et _Singapore Exchange_ (la principale bourse de Singapour) pour développer des capacités de livraison contre paiement pour le règlement d'actifs tokenisés sur différentes plateformes blockchain afin d'améliorer l'efficacité opérationnelle et de réduire les risques de règlement.

[**MAS et SGX s'associent à Anquan Deloitte et Nasdaq pour exploiter la technologie blockchain**](http://www.mas.gov.sg/News-and-Publications/Media-Releases/2018/MAS-and-SGX-partner-Anquan-Deloitte-and-Nasdaq-to-harness-blockchain-technology.aspx)  
[_Singapour, 24 août 2018... La Monetary Authority of Singapore (MAS) et Singapore Exchange (SGX) ont annoncé aujourd'hui une..._www.mas.gov.sg](http://www.mas.gov.sg/News-and-Publications/Media-Releases/2018/MAS-and-SGX-partner-Anquan-Deloitte-and-Nasdaq-to-harness-blockchain-technology.aspx)

2. **Les projets ont reconnu le besoin de conformité et créent des solutions qui ciblent la conformité automatisée et l'AML/KYC**

Nous avons abordé la nécessité de fusionner les exigences légales du monde réel dans l'espace blockchain. Il existe divers projets qui font cela à l'échelle mondiale :

1. [**Harbor**](https://harbor.com/) : _Une plateforme et un protocole de conformité pour garantir que les titres tokenisés se conforment aux lois existantes sur les titres à l'émission et à chaque transaction, partout dans le monde._
2. [**Rate3 Network**](https://rate3.network) : _Un protocole qui gère la tokenisation d'actifs et la gestion d'identité à travers les blockchains Ethereum et Stellar._
3. [**Polymath**](https://polymath.network/) : _Une plateforme de tokens de sécurité sur laquelle des tokens conformes à la réglementation peuvent être construits._

Je remarque que de plus en plus de projets blockchain construisent des solutions de tokenisation ciblant différentes classes d'actifs, différentes façons de modéliser la finance structurée en émettant à la fois des tokens de dette et d'équité, par exemple. Plus important encore, ces solutions savent que travailler directement avec les autorités de réglementation, collaborer avec les banques centrales et d'autres projets aidera à améliorer l'écosystème global.

Assurer la conception légalement conforme de l'ensemble du système est clé.

**3. Les "chemins de moindre résistance" aideront tout le monde à relier les exemples réels existants aux projets de tokenisation à venir**

L'immobilier a toujours été cité comme un exemple pour les projets de tokenisation. Cela est dû à la structure des fonds de placement immobilier (REITs), à laquelle on pourrait plus facilement relier les structures tokenisées.

L'immobilier tokenisé n'est _pas_ des REITs, mais il existe divers principes que nous pouvons utiliser pour nous aider à comprendre, relier et mieux penser : droits de propriété, économie des REITs par exemple.

_Tout ne sera pas tokenisé, mais ce qui peut l'être le sera._

_Déclaration : Je travaille chez [Rate3 Network](https://www.rate3.network/), un protocole double qui gère la tokenisation d'actifs et la gestion d'identité à travers les blockchains Ethereum et Stellar._