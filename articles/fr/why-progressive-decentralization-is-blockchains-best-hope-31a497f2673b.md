---
title: Pourquoi la décentralisation progressive est le meilleur espoir de la blockchain
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T19:36:48.000Z'
originalURL: https://freecodecamp.org/news/why-progressive-decentralization-is-blockchains-best-hope-31a497f2673b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qgm9rHxUeF-oy6NxHnXv_A.png
tags:
- name: Apps
  slug: apps-tag
- name: Blockchain
  slug: blockchain
- name: decentralization
  slug: decentralization
- name: Ethereum
  slug: ethereum
- name: 'tech '
  slug: tech
seo_title: Pourquoi la décentralisation progressive est le meilleur espoir de la blockchain
seo_desc: 'By Arthur Camara

  Immutability is blockchain’s greatest strength and biggest barrier. Progressive
  decentralization could be the answer.


  When we released CryptoKitties a year ago, we opted not to fund it up front with
  an ICO but instead build it on a ...'
---

Par Arthur Camara

#### L'immuabilité est à la fois la plus grande force et le plus grand obstacle de la blockchain. La décentralisation progressive pourrait être la solution.

![Image](https://cdn-media-1.freecodecamp.org/images/4RiJaG98m8kPcAYjnVLTCKifqTzhXEys5TD-)

Lorsque nous avons lancé [CryptoKitties](https://www.cryptokitties.co) il y a un an, nous avons choisi de ne pas le financer d'emblée avec un ICO, mais plutôt de le construire sur un modèle de revenus durable. Ce modèle est le suivant : nous prélevons des frais de 3,75 % sur chaque transaction dans le jeu. Étant donné que nous ne pourrions pas changer les frais une fois lancés — CryptoKitties est construit sur la blockchain Ethereum — les gens demandent souvent comment nous avons arrivé à ce chiffre.

Cela semble être un choix intelligent et bien réfléchi. Je pourrais raconter une histoire convaincante sur la façon dont nous avons exécuté des simulations avec des modèles de prédiction avancés pour trouver les frais qui donneraient des rendements optimaux.

Mais ce n'est pas vrai.

La vérité est que nous avons fait une estimation éclairée. Nous avons choisi un nombre qui nous semblait équitable et nous nous y sommes engagés.

### L'immuabilité est à la fois géniale et effrayante

Nous aurions facilement pu faire le mauvais choix, et comme vous ne pouvez pas changer quelque chose une fois que vous l'avez ajouté à la blockchain, cela aurait été _cat-astrophique_. Heureusement pour CryptoKitties, notre communauté est si passionnée et les Kitties sont si adorables que 3,75 % ont très bien fonctionné.

L'immuabilité, l'incapacité à être éditée, est à la fois la plus grande force de la blockchain et son plus grand obstacle à une adoption significative. Les pressions du code immortel paralysent les développeurs : vous pouvez bricoler dans un environnement de test pour toujours, mais il y aura toujours des variables du monde réel que vous ne pouvez pas anticiper. Se lancer les yeux fermés n'est pas une façon de faire des percées. Cela est plus susceptible de produire des pannes.

Nos frais n'étaient qu'une décision parmi tant d'autres : combien de temps devrait prendre l'élevage d'un Kitty ? À quel rythme leurs temps de récupération d'élevage devraient-ils ralentir ? Combien devrait coûter un chat Gen 0 ? Sur la blockchain, même un choix apparemment mineur peut poser des conséquences sérieuses, voire critiques.

La décentralisation offre aux gens des avantages immenses : l'équité des règles permanentes et universelles et la transparence du code et du comportement qui, combinés, créent la sécurité. Cependant, parce qu'elle est souvent mise en œuvre avec une immuabilité du tout ou rien, la blockchain rend le développement agile impossible et ralentit les équipes à un rythme de tortue.

L'agilité nécessite l'itération. Itérer rapidement est la clé pour construire les meilleurs produits, et les meilleurs produits déclenchent une adoption massive.

### Voici la décentralisation progressive

Nous avons rencontré ces obstacles nous-mêmes en construisant CryptoKitties, ce qui nous a forcés à négocier l'inclusion de fonctionnalités décentralisées tout en construisant quelque chose qui, vous savez, fonctionne. Depuis, nous avons commencé à explorer la décentralisation progressive dans le développement, une idée que nous avons brièvement introduite [il y a un certain temps](https://medium.com/dapperlabs/how-we-launched-cryptokitties-latest-feature-6318ecceba9f).

Plongeons plus profondément maintenant.

Simplement dit, la décentralisation progressive préconise de s'engager dans la décentralisation par étapes plutôt que de plonger tête la première. Ce à quoi cela ressemble, c'est de construire des mécanismes dans les contrats intelligents qui confèrent des pouvoirs spéciaux aux créateurs au départ, puis de verrouiller progressivement ces pouvoirs de manière transparente et systématique.

La condition critique est que les mécanismes de verrouillage doivent être publics et immuables dès le départ. Le créateur ne peut pas décider de modifier les termes plus tard et de prolonger indéfiniment son pouvoir. Cet équilibre est vital : bien fait, la décentralisation progressive permet aux créateurs la flexibilité de réparer leur code sans compromettre les fonctionnalités décentralisées du contrat.

### La décentralisation progressive peut prendre de nombreuses formes

Il n'y a pas une seule bonne façon de mettre en œuvre la décentralisation progressive. Il y a des dizaines de variables à considérer, et la meilleure approche variera d'un projet à l'autre.

Voici quelques façons dont les développeurs pourraient aborder la décentralisation progressive :

1. Rédiger plusieurs contrats avec une séparation appropriée des préoccupations et la capacité de remplacer certains de ces contrats. Certaines applications décentralisées ("dapps") comme [Decentraland](https://decentraland.org/), qui propose des contrats améliorables, utilisent déjà cela.
2. Variables configurables et permissions pour changer ces valeurs indépendamment. [Etheremon](https://www.etheremon.com/), par exemple, [accorde des permissions spéciales](https://github.com/Etheremon/smartcontract/blob/master/EtheremonERC721.sol#L125) à des groupes d'utilisateurs qui deviennent modérateurs.
3. Incorporer un ensemble prédéfini de niveaux ascendants dans le contrat, chacun permettant aux créateurs certaines capacités. Les niveaux ne peuvent être augmentés, jamais diminués, donc le retour en arrière n'est pas une option. Au niveau 1, par exemple, les propriétaires du contrat peuvent jouer avec toutes les variables de gameplay. Au niveau 2, leur capacité à modifier les variables principales prend fin. Au niveau final, le contrat révoque tous leurs privilèges spéciaux.

Pour les décentralistes intransigeants, certaines de ces idées sonnent probablement trop centralisées. Mais ce n'est que le point de départ. Il existe d'autres mesures pour équilibrer la décentralisation avec l'itération. La solution combine la transparence du but et des conditions et contraintes dans les contrats. Ces contraintes pourraient inclure :

1. **Sélection** : Tout ne peut pas être modifié, seulement les éléments spécifiques que nous devons itérer.
2. **Plage** : Pour beaucoup de questions autour des économies de jeu, nous pouvons avoir une idée générale mais ne pas connaître la réponse précise. Limiter la configuration à une certaine plage garantit aux utilisateurs que l'itération atterrira dans un cadre raisonnable.
3. **Direction** : Similaire au concept de "niveaux" ci-dessus, permettre à certaines variables de se déplacer uniquement dans une direction, en diminuant ou en augmentant mais jamais en revenant en arrière.

### Tenir les créateurs responsables

Tout cela semble génial en théorie. Mais comment pouvons-nous nous assurer que les créateurs restent fidèles à leur feuille de route et atteignent la version entièrement décentralisée de leurs contrats ? Comment les utilisateurs peuvent-ils adhérer tôt avec la garantie que le système est une application de la décentralisation progressive ? Comment pouvons-nous savoir que nous n'aboutirons pas à un autre système défectueux et centralisé ?

La décentralisation progressive inclut des principes pour tenir les créateurs responsables :

#### **_Maturité basée sur le temps ou les blocs_**

Verrouiller certaines valeurs de configuration, révoquer les capacités du propriétaire ou passer au niveau de maturité suivant après un certain temps ou numéro de bloc. Une fois ce point atteint, le contrat change automatiquement.

Imaginez, par exemple, que CryptoKitties avait une période de 360 000 blocs (environ 60 jours) à partir du moment de son lancement pour ajuster les variables de _cooldown_ d'élevage des Kitties. Nous aurions pu ajuster les mécanismes de cooldown jusqu'à ce point, nous donnant la marge de manœuvre pour perfectionner l'équilibre, tout en garantissant aux joueurs que nous n'aurions pas ce pouvoir indéfiniment.

#### **_Maturité basée sur l'utilisation_**

Verrouiller ces capacités une fois qu'un certain nombre d'utilisateurs ou de transactions sont complétés. Cette option doit être soigneusement réfléchie pour éviter les exploits, mais nous aurions pu, par exemple, intégrer des frais configurables dans CryptoKitties qui se verrouilleraient après 10 000 transactions.

#### **_Incitation économique_**

Aligner les incitations du créateur avec une décentralisation accrue. Dans ce scénario, les créateurs profitent davantage lorsque le contrat devient plus décentralisé. Peut-être que les frais augmentent à chaque niveau que le développeur atteint, se verrouillant aux frais maximum lorsqu'ils atteignent la pleine décentralisation. Ou, alternativement, peut-être qu'ils ne gagnent aucun argent du tout jusqu'à ce que la pleine décentralisation soit en place. Cette récompense financière motive le développeur à atteindre la décentralisation à un rythme raisonnable.

### Il n'y a pas de meilleure approche pour construire sur la blockchain

La "décentralisation progressive" est vraiment un terme générique englobant de nombreuses stratégies, mécanismes et outils pour rendre la construction sur la blockchain plus viable. La meilleure façon d'appliquer la décentralisation progressive dépendra toujours du projet et utilisera un mélange des concepts décrits ci-dessus.

La décentralisation progressive n'est pas parfaite. Le contrat intelligent idéal est simple et direct, et ces mesures ajoutent de la complexité. Comment et combien l'incorporer est un compromis qui doit être évalué au cas par cas.

Bien que cela puisse mettre en colère les décentralistes intransigeants, nous croyons que la décentralisation progressive est bien meilleure pour les utilisateurs à long terme : en donnant aux développeurs la flexibilité de s'adapter, le consommateur obtient un produit plus utile. Cela signifie qu'ils l'utiliseront réellement, et une fois qu'il apportera de la valeur à leur vie, ils en feront l'éloge aux gens autour d'eux. C'est ainsi que commence l'adoption massive.

_Auteurs : [Arthur Camara](https://medium.com/@arthur_camara), [Dieter Shirley](https://medium.com/@dete73), et Grady Mitchell_