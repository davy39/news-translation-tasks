---
title: 'Un autre gros problème avec les modèles de tokens : les tokens « Moyen d''Échange
  » et le problème de vélocité'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-22T14:07:33.000Z'
originalURL: https://freecodecamp.org/news/single-biggest-problem-with-token-models-part-2-52c0eca2115c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dOLz3DK9K1LUHuFK.jpg
tags:
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: Investment
  slug: investment
- name: 'tech '
  slug: tech
- name: token economy
  slug: token-economy
seo_title: 'Un autre gros problème avec les modèles de tokens : les tokens « Moyen
  d''Échange » et le problème de vélocité'
seo_desc: 'By Jose Maria Macedo

  As an analyst at Amazix, I spend a large portion of my time reading through hundreds
  of projects’ whitepapers and analyzing their token economic models to discern whether
  or not they’re adequately capturing the value created by t...'
---

Par Jose Maria Macedo

En tant qu'analyste chez [Amazix](https://www.amazix.com/), je passe une grande partie de mon temps à lire des centaines de livres blancs de projets et à analyser leurs modèles économiques de tokens pour discerner si ils capturent adéquatement la valeur créée par le projet.

Ceci est extrêmement important car la valeur capturée par un token est essentiellement son utilité ou sa valeur intrinsèque, ce qui garantit également que le prix du token croît parallèlement à l'adoption/au succès du projet sous-jacent. Un token manquant d'utilité verra son prix soutenu uniquement par la spéculation et est très susceptible d'échouer à long terme.

Pour plus d'informations à ce sujet, voir mon [blog précédent](https://medium.com/@zemacedo/token-valuation-the-misunderstood-importance-of-token-economics-or-why-xrp-is-worthless-6b1b9ce5605f), dans lequel j'ai discuté de l'importance des modèles économiques de tokens pour garantir la valeur à long terme d'un token.

Dans [la partie 1 de cette série](https://medium.freecodecamp.org/the-single-biggest-problem-with-token-models-part-i-8f9bcb3bab50), j'ai abordé le problème des incitations mal alignées causées par des projets qui ont à la fois des actions et des tokens, suggérant qu'il existe une relation inverse entre la valeur des actions d'un projet et la valeur de son token, en ce sens qu'ils sont effectivement en concurrence pour capturer la valeur créée par le projet. J'ai également suggéré quelques solutions potentielles à ce problème.

Dans ce blog, je vais discuter du deuxième problème le plus courant que nous voyons avec les modèles économiques de tokens : le problème de vélocité auquel sont confrontés les tokens « Moyen d'Échange ». Je commencerai par donner un bref aperçu de ce qu'est l'économie des tokens avant de décrire ce qu'est le problème de vélocité, pourquoi il est important et quelques-unes des solutions que nous recommandons à nos clients.

![Image](https://cdn-media-1.freecodecamp.org/images/AaXmsMRKJbeixIkkpXWJtu1QQMyDyfTlVVBr)

### Qu'est-ce qu'un modèle économique de token et pourquoi est-ce important ?

Si vous êtes un investisseur crypto expérimenté ou si vous comprenez ce qu'est un modèle économique de token, n'hésitez pas à sauter cette partie.

Avant de commencer à parler des modèles économiques de tokens, il peut être judicieux de commencer par le début : qu'est-ce qu'un token et qu'est-ce qui constitue sa valeur.

Un token est une unité de compte crypto-économique qui représente ou interagit avec un actif sous-jacent générateur de valeur. La valeur d'un token est constituée de sa valeur intrinsèque, le pourcentage de la valeur du token qui dérive de la demande pour l'actif sous-jacent, et de sa valeur spéculative, le pourcentage de la valeur des tokens qui dérive de la demande due à une attente d'augmentation future des prix. Bien que la spéculation soit agréable, elle est difficile à contrôler/prédire et place les projets à la merci des investisseurs orientés à court terme, comme notre ami ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/3y3eqaNZaPfZ67xy-gMHyX-xdx8tCn3HCUK6)

Plutôt que de se concentrer sur la valeur spéculative, nous recommandons aux investisseurs de se concentrer sur la valeur intrinsèque. La valeur intrinsèque d'un token dépend de deux facteurs : la valeur créée par l'actif sous-jacent _et_ le pourcentage de cette valeur qui est capturée par le token.

Le modèle économique de token est ce qui détermine ce dernier point — combien de la valeur créée par la plateforme est capturée par le token. À ce titre, c'est l'un des principaux déterminants de la valeur utilitaire d'un projet et de son succès à long terme.

### Tokens de Moyen d'Échange et le problème de vélocité

Un token de Moyen d'Échange pur est un token dont l'utilisation unique ou au moins principale est le paiement pour une certaine utilité sur la plateforme ou le protocole du projet. Il existe diverses incarnations de cela, des places de marché telles que [Signals Network](https://signals.network/) où le token est la seule monnaie utilisée pour acheter des services sur la plateforme, aux projets de type SaaS comme [BitStation](http://bitstation.co/) où les clients ne peuvent accéder à l'utilité de la plateforme qu'en payant à l'entreprise des frais dans le token natif.

Le problème général avec les tokens MoE est qu'ils souffrent d'une vélocité extrêmement élevée. Cela a été bien documenté par beaucoup, y compris [Vitalik](https://vitalik.ca/general/2017/10/17/moe.html), [James Kilroe](https://medium.com/newtown-partners/velocity-of-tokens-26b313303b77) et [Kyle Samani](https://www.coindesk.com/blockchain-token-velocity-problem/).

En gros, étant donné que l'unique utilisation du token MoE est le paiement pour un service sur la plateforme, il n'y a aucune incitation à détenir des tokens et à encourir un risque de prix par rapport au FIAT.

Les acheteurs de l'utilité de la plateforme acquerront simplement des tokens à des fins de transaction spécifique (les détenant pendant le moins de temps possible). D'autre part, les vendeurs de l'utilité de la plateforme (qu'il s'agisse d'utilisateurs sur un marché comme dans le cas de Signals ou de l'entreprise derrière le projet dans le cas de Bitstation) vendront instantanément les tokens qu'ils reçoivent pour du FIAT plutôt que d'encourir un risque de prix par rapport au FIAT.

Cela entraînera une vélocité élevée pour le token, car l'augmentation de la demande entraînée par les acheteurs acquérant des tokens sera toujours rapidement compensée par une augmentation correspondante de l'offre de la part des vendeurs convertissant ces tokens en FIAT.

Effectivement, une vélocité élevée agit comme une augmentation de l'offre en circulation et est donc inversement proportionnelle à la valeur du token (bien qu'un certain niveau de base de vélocité soit nécessaire pour que le token ait une quelconque valeur, [comme le souligne James Kilroe](https://medium.com/newtown-partners/velocity-of-tokens-26b313303b77)). Nous pouvons voir comment cela fonctionne en utilisant l'[Équation d'Échange](https://www.investopedia.com/terms/e/equation_of_exchange.asp), qui a été célèbre adaptée à la crypto par Chris Burniske et Vitalik.

Pour utiliser la définition de Burniske :

MV=PQ

Où :   
_M_= taille de la base d'actifs   
_V_= vélocité de l'actif (le nombre de fois qu'une pièce moyenne change de mains chaque jour)   
_P_= prix de la ressource numérique fournie. Il ne s'agit pas du prix de la cryptomonnaie mais plutôt de la ressource fournie par le réseau (c'est-à-dire le prix en $ par Go de stockage dans le cas de Filecoin)  
_Q_= quantité de la ressource numérique fournie (Go de stockage fournis)

Comme nous le dit Burniske, afin de valoriser la pièce, nous résolvons pour M, où :

M = PQ/V.

M est la taille de la base monétaire nécessaire pour soutenir une cryptéconomie de taille PQ, à la vélocité V. Afin de trouver le prix du token, nous divisons simplement M par l'offre totale de tokens. Comme nous pouvons le voir, plus la vélocité est élevée, plus la valeur de la pièce est faible.

Ou, si nous préférons utiliser la définition de Vitalik :

Vitalik prend MV=PT et, afin de simplifier l'analyse des cryptomonnaies, la reformule en MC=TH, où :

_M_= offre monétaire totale (ou nombre total de pièces)   
_C_= prix de la cryptomonnaie (ou _1/P_, avec _P_ étant le niveau de prix)   
_T_= volume de transactions (la valeur économique des transactions par temps)   
_H= 1/V_ (le temps moyen qu'un utilisateur détient une pièce avant de l'utiliser pour effectuer une transaction)

Par conséquent, la partie gauche de l'équation (MC) est simplement la capitalisation boursière (offre totale*prix) tandis que la partie droite est la valeur économique transigée par période de temps (T) multipliée par le temps moyen qu'un utilisateur détient une pièce (H).

Pour résoudre le prix du token, il faut donc résoudre pour C :

_C=TH/M_

Une fois de plus, nous pouvons voir que plus la vélocité est élevée (ou plus le temps de détention H est faible), plus le prix du token est faible.

![Image](https://cdn-media-1.freecodecamp.org/images/pdcCegPgrx4ceZkSDwRkENIKHTs956dP9L2B)
_Vitalik impressionné_

Dans les définitions de Burniske et de Vitalik, il est évident que la vélocité de la pièce est inversement proportionnelle à la valeur du token. C'est-à-dire, plus les gens détiennent le token longtemps, plus le prix de chaque token est élevé. Comme nous le dit James Kilroy :

> _« Cela est intuitif, car si l'activité transactionnelle d'une économie est de 100 milliards de dollars (pour l'année) et que les pièces circulent 10 fois chacune au cours de l'année, alors la valeur collective des pièces est de 10 milliards de dollars. Si elles circulent 100 fois, alors les pièces collectives valent 1 milliard de dollars. Ainsi, comprendre et calculer la vélocité dans toute économie de tokens est extrêmement important. »_

Pour voir les effets drastiques que la vélocité peut avoir sur la capture de valeur et la capitalisation boursière d'un token, voir l'analyse suivante [des effets de la vélocité sur la capitalisation boursière d'Ethereum par John Pfeffer :](https://medium.com/@john_pfeffer/hi-johnny-8411ec5d266)

> _« Dans un monde de protocoles où l'utilisation des protocoles est gérée par des bots intelligents optimisant l'efficacité du capital (ce qui semble probable), supposons pour simplifier que le plancher absolu sur 1/V est le temps de bloc de la chaîne en question. Prenons ensuite ETH avec un temps de bloc de 2,5 minutes comme exemple (hautement théorique, juste pour faire un point mathématique simple). Cela implique que chaque token pourrait être utilisé (en supposant des temps de bloc fixes, qui en fait vont probablement raccourcir) 210 240 fois par an. Buterin, Choi, etc. parlent de, disons, 10 % d'ETH étant mis en jeu (supposons que les tokens mis en jeu ne bougent jamais). Cela ramènerait V à 189 216 par an. Supposons 50 %, alors V=105 120. Multipliez ce dernier nombre par 50 milliards de dollars de valeur de réseau (c'est-à-dire, ETH maintient simplement sa valeur actuelle, et vous auriez besoin de 5,25 quadrillions d'activité économique libellée en ETH (c'est-à-dire, excluant toute activité économique libellée en ERC20/ERC721), c'est-à-dire 65 fois le PIB mondial actuel de 80 billions. Ces chiffres sont tous simplement des nuances de ridicule. C'est le point. Tant que certains de vos tokens circulent à une V élevée, votre V globale est élevée. »_

### **Solutions au problème de vélocité**

Les solutions les plus couramment utilisées à ce problème impliquent toutes la conception de modèles économiques de tokens qui fournissent des incitations aux gens à détenir le token — le transformant essentiellement en un actif (ou « Réserve de Valeur ») plutôt qu'en une monnaie. Cela peut être fait de plusieurs manières :

#### (1) Assurez-vous que le modèle de token a un « puits »

Cela a été initialement suggéré par Vitalik et a été largement adopté depuis. En gros, cela implique de concevoir des modèles de tokens avec des mécanismes « d'achat et de destruction » dans lesquels le projet facture des frais de transaction et utilise ensuite une partie ou la totalité des flux de trésorerie générés par sa plateforme pour acheter ses propres tokens et les détruire. La diminution de l'offre augmente la valeur de tous les tokens restants du pourcentage de l'offre totale détruite. Effectivement, le projet distribue ses flux de trésorerie à ses détenteurs de tokens, très similaire à la manière dont les actions distribuent les flux de trésorerie à ses actionnaires par le biais d'un dividende.

Un exemple de cela est Iconomi, une plateforme de gestion d'actifs numériques qui [détruit des pourcentages prédéfinis de tous les frais collectés](https://iconomi.zendesk.com/hc/en-us/articles/360001428854-Repayment-Programme-Buybacks-Token-Burn) et produit également des rapports trimestriels détaillant le nombre de tokens brûlés (rapports de gains trimestriels crypto).

Puisque, comme nous l'avons mentionné précédemment, la vélocité agit comme une augmentation de l'offre en circulation, ce qui réduit la valeur capturée par le token, un mécanisme d'achat et de destruction a l'effet inverse de garantir que chaque transaction supplémentaire (c'est-à-dire une augmentation de la vélocité) sur la plateforme réduit l'offre totale de tokens, contrant ainsi l'augmentation de la vélocité avec une force déflationniste.

Cela devrait également réduire la vélocité en donnant aux gens une raison de détenir le token, à savoir l'attente qu'il sera plus précieux à l'avenir en raison de la force déflationniste créée par la destruction de tokens.

![Image](https://cdn-media-1.freecodecamp.org/images/4xvIyYR8SJlQ7BkY8LMyp81y935fNtYHlvK-)
_Le Joker réduisant la vélocité du $_

#### (2) Mettre en place un « partage des bénéfices »

Cela a été initialement [suggéré par Kyle Samani de Multicoin](https://multicoin.capital/2017/12/08/understanding-token-velocity/). C'est très similaire dans l'esprit à l'« achat et destruction » en ce sens qu'il fournit au token un rendement et le transforme en un actif qui génère des flux de trésorerie.

Un exemple de cela est Augur qui paie les détenteurs de REP pour le travail effectué pour le réseau. Les tokens REP sont comme des médaillons de taxi : vous devez payer pour le droit de travailler pour le réseau. Plus précisément, les détenteurs de REP doivent signaler les résultats des événements pour résoudre les marchés de prédiction. D'autres exemples de tokens à « partage des bénéfices » incluent [FOAM](https://foam.space/), [Sharpe Capital](https://sharpe.capital/) et également Ethereum une fois qu'il aura basculé vers la Preuve d'Enjeu.

Une fois de plus, un partage des bénéfices réduit la vélocité des tokens en obligeant les gens à détenir le token afin d'avoir le droit de générer des flux de trésorerie en fournissant du travail au réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/vrdFC-TozgbVmvYVmqlkK3yPMTW2A3YrMJHo)

#### (3) Encourager les utilisateurs à bloquer les tokens

Cela peut être fait par des mécanismes tels que la [Preuve d'Enjeu](https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQ) qui encouragent les utilisateurs à bloquer une certaine quantité de tokens, à vérifier les transactions et à recevoir un rendement en retour (ceci a également l'avantage supplémentaire d'agir comme un partage des bénéfices). DASH, NEO et Navcoin sont tous des exemples de pièces qui ont mis en œuvre des modèles de preuve d'enjeu.

Les utilisateurs peuvent également être encouragés à bloquer les tokens par une gamification intelligente — en fournissant aux utilisateurs des récompenses (financières ou autres) pour le blocage des tokens. Par exemple, Alluma, une bourse crypto ciblant les marchés asiatiques, offre différents niveaux d'adhésion et des réductions de frais en fonction des utilisateurs misant différentes quantités de tokens :

* Les adhésions Gold offrent 35 % de réduction en échange de la mise de 2500 LUMA pendant 30 jours, et
* Les adhésions Platinum offrent 50 % de réduction en échange de la mise de 10 000 LUMA pendant 90 jours ([source : page 28 du livre blanc d'Alluma](https://cdn2.hubspot.net/hubfs/4077694/whitepaper%20languages/Alluma%20Whitepaper.pdf?__hssc=147911272.3.1531961915300&__hstc=147911272.bf36623eb62b5916dee4146a67129a0e.1531961915299.1531961915299.1531961915299.1&__hsfp=2747456470&hsCtaTracking=8aed7630-08c6-4c61-8bd1-6db116fa6876%7C50cad1a6-1dbf-4b3e-9f82-a8dd851584c5)).

Pour un autre exemple, nous pouvons regarder YouNow, une application de streaming en direct qui permet aux utilisateurs de donner des pourboires aux créateurs de contenu dans son token natif PROPS.

Bien que les créateurs de contenu puissent immédiatement convertir les PROPS en FIAT, ils sont incités à les conserver car leur contenu est mieux classé par l'algorithme de YouNow en fonction du nombre de tokens qu'ils détiennent. Puisque la découvrabilité conduit directement à plus de pourboires, YouNow transforme effectivement les PROPS en un actif en s'assurant que les utilisateurs qui les détiennent sont capables de générer des flux de trésorerie.

![Image](https://cdn-media-1.freecodecamp.org/images/HHs-7B9WUn3SVSULp62cIeO8FbpXYO8kvSFk)
_Masternode de Donald Duck_

### Conclusion

La conception de modèles économiques de tokens est un domaine extrêmement important et sous-estimé pour les investisseurs et les fondateurs de projets de cryptomonnaies. Un projet avec un modèle économique de tokens faible peut voir son prix de token échouer, même si le projet lui-même réussit, simplement parce que le token ne capture aucune de la valeur créée par le projet.

La vélocité est l'un des plus grands problèmes des modèles économiques de tokens actuels et de nombreux projets établis tels que [Civic](https://www.newtownpartners.com/how-civics-updated-token-model-decentralizes-trust/), [Storj](https://www.coindesk.com/300-million-lockup-storj-clarifies-token-economics-surprise-reveal/) et Po.et ont récemment revu leurs modèles de tokens pour résoudre ce problème. Si vous pensez que votre projet peut également souffrir d'une vélocité élevée et que vous êtes intéressé à faire auditer votre économie de tokens ou à discuter de cela plus avant, n'hésitez pas à me contacter ici ou sur [Twitter.](https://twitter.com/zemariamacedo)