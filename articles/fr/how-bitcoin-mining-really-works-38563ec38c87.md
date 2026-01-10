---
title: Comment le minage de Bitcoin fonctionne vraiment
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-31T17:10:07.000Z'
originalURL: https://freecodecamp.org/news/how-bitcoin-mining-really-works-38563ec38c87
coverImage: https://cdn-media-1.freecodecamp.org/images/0*A8uxgOGZV8XlHg8s.jpg
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
seo_title: Comment le minage de Bitcoin fonctionne vraiment
seo_desc: 'By Subhan Nadeem

  As Bitcoin approaches mainstream adoption and recognition, its fundamental security
  model, characterized as mining, is being put under the spotlight and scrutinized
  more and more everyday.

  People are increasingly concerned about and ...'
---

Par Subhan Nadeem

Alors que Bitcoin approche de l'adoption et de la reconnaissance grand public, son modèle de sécurité fondamental, caractérisé comme le minage, est mis sous les projecteurs et scruté de plus en plus chaque jour.

Les gens sont de plus en plus préoccupés et intéressés par l'impact environnemental du minage de Bitcoin, la sécurité et le degré de décentralisation du modèle sous-jacent, et même l'impact potentiel d'une percée en informatique quantique sur l'avenir de Bitcoin et d'autres cryptomonnaies.

Souvent, la preuve de travail est décrite comme une "énigme cryptographique", mais quelle est cette énigme, vraiment ?

Pour vraiment comprendre ces questions (et toute réponse possible), vous devez avoir une compréhension fondamentale du minage de Bitcoin lui-même et de son évolution.

Cet article explorera tous les composants techniques et les éléments mobiles de la preuve de travail, et comment ils se synchronisent de manière transparente les uns avec les autres pour permettre à Bitcoin d'être la plateforme décentralisée qu'elle est aujourd'hui.

### Pourquoi le minage fonctionne : le hachage cryptographique à sens unique

La blockchain Bitcoin est souvent décrite comme une base de données qui est cryptographiquement sécurisée et, par conséquent, immuable. La technologie sous-jacente qui alimente cette immuabilité et cette sécurité est le **hachage cryptographique**.

Une fonction de hachage cryptographique est une fonction mathématique qui, simplement dit, prend n'importe quelle entrée et la mappe à une chaîne de taille fixe.

Cependant, il y a quatre propriétés spéciales de ces fonctions qui les rendent inestimables pour le réseau Bitcoin. Elles sont :

1. **Déterministe** — pour toute entrée dans la fonction de hachage cryptographique, le résultat sera toujours le même.
2. **Rapide** — Calculer la sortie de la fonction de hachage, étant donné n'importe quelle entrée, est un processus relativement rapide (n'a pas besoin de calculs lourds)
3. **Unique** — Chaque entrée dans la fonction doit résulter en une sortie complètement aléatoire et unique (en d'autres termes, aucune deux entrées ne résultent en la même sortie)
4. **Irréversible** — Étant donné une sortie d'une fonction de hachage, l'entrée originale ne peut pas être obtenue

Ces règles fournissent la fondation qui permet au minage de Bitcoin de sécuriser le réseau.

En particulier, le créateur du protocole Bitcoin, Satoshi Nakomoto, a choisi d'utiliser la [fonction de hachage SHA-256](https://en.wikipedia.org/wiki/SHA-2) comme base pour le minage de Bitcoin. Il s'agit d'une fonction de hachage cryptographique spécifique qui a été mathématiquement prouvée pour posséder les propriétés ci-dessus. Elle produit toujours un **nombre de 256 bits** (l'unité de calcul la plus basique), qui est généralement représenté dans le système de nombres hexadécimaux avec 64 caractères pour la lisibilité humaine.

La sortie de la fonction SHA-256 est généralement appelée le **hachage** de son entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/1iObT23KZMg-OPHVKyPW3Fp-12cFhc2oaMdI)
_Une entrée de fonction de hachage résulte en une sortie complètement unique_

Voici un exemple d'entrée et de sortie de la fonction SHA-256 (vous pouvez l'essayer vous-même [ici](http://www.xorbin.com/tools/sha256-hash-calculator)):

```
Entrée pour SHA-256 :
<Transaction Bitcoin>
Sortie pour SHA-256 :
77077b1f4c3ad44c83dc0bdb8d937e9b71c0ef07a35c2664bb7da85be738eacf
```

De manière intéressante, dans la majorité des endroits où le hachage est utilisé dans le protocole Bitcoin, le **double hachage** est utilisé. Cela signifie que la sortie de la fonction SHA-256 originale est ensuite remise directement dans la fonction SHA-256 pour obtenir une autre sortie. Voici à quoi ressemble ce processus :

```
Entrée pour SHA-256 (premier tour) :
<Transaction Bitcoin>
Sortie (premier tour) :
77077b1f4c3ad44c83dc0bdb8d937e9b71c0ef07a35c2664bb7da85be738eacf

Entrée pour SHA-256 (deuxième tour) :
77077b1f4c3ad44c83dc0bdb8d937e9b71c0ef07a35c2664bb7da85be738eacf
Sortie (deuxième tour et résultat final) :
3c6c55b0e4b607b672b50f04e028a6951aed6dc97b91e103fb0f348c3f1dfa00
```

Le double hachage est utilisé pour se prémunir contre les attaques par anniversaire. Une attaque par anniversaire est un scénario où un attaquant est capable de produire le même hachage qu'une autre entrée en utilisant une entrée complètement différente (appelée une **collision**). Cela brise la troisième propriété de **l'unicité**. Sans cela, deux blocs Bitcoin complètement différents pourraient être représentés par le même hachage, permettant aux attaquants de potentiellement échanger des blocs.

Avec la fonction SHA-256, la probabilité que cette attaque se produise est infiniment petite. Si ce n'était pas presque impossible, SHA-256 serait considéré comme brisé.

Cependant, d'autres fonctions de hachage ont été "brisées" dans le passé. Afin de se prémunir contre cela arrivant à SHA-256 à l'avenir (et brisant effectivement le modèle de sécurité de Bitcoin), il est préférable de **hacher le hachage**. Cela réduit de moitié la probabilité qu'une collision se produise, rendant le protocole d'autant plus sécurisé.

À un niveau très élevé, le minage de Bitcoin est un système dans lequel toutes les transactions Bitcoin sont envoyées aux mineurs de Bitcoin. Les mineurs sélectionnent un mégaoctet de transactions, les regroupent en une entrée dans la fonction SHA-256, et tentent de trouver une sortie spécifique que le réseau accepte. Le premier mineur à trouver cette sortie et à publier le bloc sur le réseau reçoit une récompense sous forme de frais de transaction et de la création de nouveaux Bitcoins.

Allons plus loin et plongeons dans la blockchain Bitcoin elle-même pour voir ce que font exactement les mineurs pour sécuriser le réseau.

### Minage de Bitcoin : une introduction technique

Le minage a été introduit comme solution au problème de la double dépense. Si j'ai 1 Bitcoin et que je l'envoie à Bob, puis que j'essaie d'envoyer ce même Bitcoin à Alice, le réseau garantit qu'une seule transaction sera acceptée. Il le fait grâce au processus bien connu appelé minage.

Avant de plonger dans les détails techniques, il est important de comprendre pourquoi le minage est nécessaire pour sécuriser le réseau. Comme la [monnaie fiduciaire](https://www.investopedia.com/terms/f/fiatmoney.asp) existe maintenant, la monnaie que nous détenons est créée et validée par une réserve fédérale. Parce que Bitcoin fonctionne sous l'hypothèse rigide de la décentralisation et du consensus, aucune autorité centrale ne peut exister pour valider et horodater l'émission de cette monnaie et la validation de toute transaction qui se produit avec cette monnaie.

Satoshi Nakamoto a proposé la seule solution connue à l'époque pour résoudre ce problème de validation dans un système orienté consensus. Intitulé dans le livre blanc de Bitcoin comme **preuve de travail**, ce schéma justifie élégamment que les transactions sont validées par ceux qui sont prêts à dépenser suffisamment d'énergie et de temps de calcul physique pour le faire, tout en introduisant simultanément un incitatif pour induire une compétition sur le marché. Cette compétition permet à la propriété de décentralisation d'émerger et de prospérer organiquement au sein de l'écosystème.

### Un regard à l'intérieur d'un bloc

Un bloc Bitcoin se compose principalement de deux composants :

#### 1. Les transactions, sous la forme d'un **arbre de Merkle**

Les ordinateurs de minage collectent suffisamment de transactions pour remplir un bloc et les regroupent dans un arbre de Merkle.

Un arbre de Merkle est un concept relativement simple : les transactions se trouvent au bas de l'arbre en tant que feuilles et sont hachées en utilisant la fonction SHA-256. La combinaison de deux transactions feuilles est hachée à nouveau en utilisant la fonction SHA-256 pour former un parent des feuilles. Ce parent est continuellement haché vers le haut en combinaison avec d'autres parents de transactions hachées, jusqu'à ce qu'une seule **racine** soit créée. Le hachage de cette racine est effectivement une représentation unique des transactions qui se trouvent en dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/3Y5SmuCwRz8GnPlpMVo9SUG0n3mg95o4fwoP)
_Une visualisation de la construction d'un arbre de Merkle — les feuilles tout en bas de l'arbre sont des transactions_

La racine de l'arbre de Merkle est une combinaison des hachages de chaque transaction dans l'arbre.

Rappelons que pour toute entrée dans une fonction de hachage, la sortie est entièrement **unique**. Par conséquent, une fois que la plupart des nœuds sur le réseau reçoivent un bloc miné, le hachage de la racine de l'arbre de Merkle agit comme un résumé immuable de toutes les transactions dans ce bloc donné.

Si un acteur malveillant tentait de changer le contenu d'une transaction dans un bloc, son hachage serait modifié. Ce changement de hachage se propagerait vers le haut de l'arbre de Merkle de la transaction jusqu'à ce que le hachage de la racine soit modifié. Tout nœud peut alors rapidement détecter cet acte malveillant en comparant la racine de l'arbre de Merkle du bloc modifié à celle d'un bloc valide.

#### 2. L'en-tête de bloc

L'en-tête de bloc est un résumé du contenu du bloc lui-même. Il contient les six composants suivants :

* La version du logiciel que le client Bitcoin exécute
* L'horodatage du bloc
* La racine de l'arbre de Merkle contenant les transactions
* Le hachage du bloc précédent
* Un **nonce**
* La **cible**

Rappelons que la racine de l'arbre de Merkle des transactions agit comme un résumé efficace de chaque transaction dans le bloc sans avoir à regarder chaque transaction.

Le hachage du bloc précédent permet au réseau de placer correctement le bloc dans l'ordre chronologique. C'est de là que vient le terme **blockchain** — chaque bloc est enchaîné à un bloc précédent.

Le **nonce** et la **cible** sont ce qui fait fonctionner le minage. Ils sont la base pour résoudre l'énigme SHA-256 que les mineurs doivent résoudre.

Veuillez noter que toutes ces données dans l'en-tête de bloc sont compressées en 80 octets en utilisant une notation appelée [little-endian](https://bitcoin.stackexchange.com/questions/2063/why-does-the-bitcoin-protocol-use-the-little-endian-notation), rendant le transfert des en-têtes de bloc entre les nœuds un processus trivialement efficace. Pour les besoins de cette explication, nous ignorerons cette compression et supposerons que les données sont dans leur forme originale.

### Explication du problème de minage

La **cible** stockée dans l'en-tête de bloc est simplement une valeur numérique stockée en bits. En notation décimale traditionnelle, cette cible varie de 0 à quelque part dans la plage de 2²²⁴ (un nombre de **67+ chiffres**), selon le nombre de mineurs qui tentent de résoudre ce problème en même temps.

Rappelons que la sortie de SHA-256 est simplement un nombre. Le but d'un mineur est de prendre l'en-tête du bloc actuel, d'y ajouter un nombre aléatoire appelé **nonce**, et de calculer son hachage. Cette valeur numérique du hachage doit être inférieure à la valeur cible.

C'est tout ce qu'il y a à faire. Mais c'est beaucoup plus facile à dire qu'à faire.

Rappelons la première propriété de SHA-256 : une entrée dans une fonction de hachage donnera toujours le même résultat. Par conséquent, si le mineur prenait l'en-tête de bloc, le hachait, et réalisait que la valeur de hachage n'était pas inférieure à la cible, il devrait changer l'entrée d'une manière ou d'une autre afin d'essayer de trouver un hachage en dessous de la valeur cible.

C'est là que le **nonce** entre en jeu.

Le mineur ajoute un nombre (en commençant par 0), appelé **nonce**, à l'en-tête de bloc, et hache cette valeur. Si la valeur de hachage n'est pas inférieure à la cible, le mineur incrémentera le nonce de 1, l'ajoutera à nouveau à l'en-tête de bloc, et hachera cette valeur modifiée. Ce processus est répété en continu jusqu'à ce qu'un hachage inférieur à la valeur cible soit trouvé.

#### Un exemple de minage

Voici une approximation de ce qui composait le premier en-tête de bloc :

* La racine de Merkle de la transaction dans le bloc Genesis :

```
Racine de Merkle :
4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b
```

* La première version connue de Bitcoin : `0.1.0`
* L'horodatage du bloc : `2009-01-03 18:15:05`
* La cible (c'est aussi la cible la plus élevée qui existera jamais) :

```
Cible :
0x00000000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
```

* Aucun hachage de bloc précédent — c'était le premier bloc, et donc c'est un cas unique

L'en-tête de bloc final après avoir ajouté ses composants ensemble :

![Image](https://cdn-media-1.freecodecamp.org/images/RgFYX1FSetNk-EJF91HSNTcVhqIYyDziZJkD)
_Les données du bloc Genesis (cela inclut le nonce, mais faisons semblant que non), source : [bitcointalk](https://bitcointalk.org/index.php?topic=52706" rel="noopener" target="_blank" title=")_

Prenons cet en-tête et calculons le double-hachage :

```
SHA-256 de l'en-tête :
7d80bd12dfdccbdde2c41c9f406edfc05afb3320f5affc4f510b05a3394e1c91

SHA-256 du résultat précédent (résultat final) :
c5aa3150f61b752c8fb39525f911981e2f9982c8b9bc907c73914585ad2ef12b
```

La cible et le hachage de sortie sont des nombres incroyablement grands lorsqu'ils sont convertis en base 10 (rappelez-vous, plus de 67 chiffres de long). Au lieu d'essayer de démontrer la comparaison des deux ici, la fonction Python suivante gère la comparaison à la place :

```
def isBlockHashLessThanTarget(blockHash, target):
    return int(blockHash, 16) < int(target, 16)
```

Vrai est retourné si le hachage est inférieur à la cible, faux sinon.

Voici le résultat avec notre cible et notre hachage de bloc :

![Image](https://cdn-media-1.freecodecamp.org/images/mI97AvtxoLFh08Qy99YmpOesirwiyS3a6iLj)

Maintenant, nous prenons la valeur hexadécimale originale du bloc et ajoutons 1. Voici le résultat suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/M7hXm9TXd9CFp3vmZ4sOUHxyvuzMHowjTifh)
_Remarquez comment le dernier chiffre est maintenant 1, en raison de l'addition du nonce_

Nous exécutons ensuite le même algorithme de hachage et la comparaison sur ces données modifiées. Si ce n'est pas en dessous de la cible, continuez à répéter.

Une fois qu'un hachage réussi est trouvé, le dernier nonce utilisé pour trouver cette solution est enregistré dans le bloc.

[Le nonce listé sur le bloc Genesis](https://blockchain.info/block-index/14849) est 2 083 236 893.

Cela signifie que Satoshi Nakomoto a itéré ce processus plus de 2 milliards de fois avant de trouver un hachage acceptable.

J'ai écrit une petite implémentation Python de ce processus de minage du bloc Genesis qui peut être trouvée sur mon [GitHub](http://github.com/subhan-nadeem/bitcoin-mining-python).

[**subhan-nadeem/bitcoin-mining-python**](http://github.com/subhan-nadeem/bitcoin-mining-python)
[_bitcoin-mining-python - Une implémentation Python de l'algorithme de minage de Bitcoin_](http://github.com/subhan-nadeem/bitcoin-mining-python)
[github.com](http://github.com/subhan-nadeem/bitcoin-mining-python)

Voyez combien de temps il vous faudrait pour miner avec succès le bloc Genesis !

#### Une mise en garde : `extraNonce`

La valeur du nonce dans un en-tête de bloc est stockée sous forme de nombre de 32 bits. Cela signifie que le nonce le plus élevé que quiconque peut atteindre est **2³²** (environ 4 milliards). Après 4 milliards d'itérations, le nonce est épuisé, et si une solution n'est pas trouvée, les mineurs sont à nouveau bloqués.

La solution à cela est d'ajouter un champ à la **coinbase** (le contenu des transactions d'un bloc, stocké sous forme d'arbre de Merkle) appelé **extraNonce**. La taille de cet extraNonce est uniquement limitée par la taille du bloc lui-même, et peut donc être aussi grande que les mineurs le souhaitent tant que la taille du bloc est dans les limites du protocole.

Si toutes les 4 milliards de valeurs possibles du nonce sont épuisées, l'**extraNonce** est ajouté et incrémenté à la **coinbase**. Une nouvelle racine de Merkle et, par conséquent, un nouvel en-tête de bloc sont calculés, et le **nonce** est itéré une fois de plus. Ce processus est répété jusqu'à ce qu'un hachage suffisant soit trouvé.

Il est préférable d'éviter d'ajouter l'**extraNonce** jusqu'à ce que le **nonce** soit épuisé, car tout changement de l'extraNonce modifie l'arbre de Merkle. Cela nécessite un calcul supplémentaire afin de propager le changement vers le haut jusqu'à ce qu'une nouvelle racine de l'arbre de Merkle soit calculée.

#### La récompense du mineur

Un mineur qui publie un bloc le plus rapidement reçoit de nouveaux Bitcoins, créés à partir de rien. Cette récompense [s'élève actuellement](http://www.bitcoinblockhalf.com/) à 12,5 BTC. Comment ces Bitcoins entrent-ils en existence ?

Chaque mineur ajoute simplement une nouvelle transaction de sortie à leur bloc qui attribue 12,5 Bitcoins à eux-mêmes avant de commencer à miner le bloc. Le protocole du réseau acceptera cette transaction spéciale comme valide lors de la réception d'un bloc nouvellement validé. Cette transaction spéciale est appelée une **transaction de génération**.

C'est la responsabilité du mineur d'ajouter cette transaction dans le bloc avant de le miner. Il y a eu [au moins un cas](https://www.reddit.com/r/Bitcoin/comments/7n1ie5/someone_destroyed_125_newly_mined_bitcoins/) où les mineurs ont oublié d'ajouter la récompense à la transaction avant de miner un bloc, détruisant effectivement 12,5 BTC !

### Validation de la preuve de travail

Disons que notre mineur a trouvé un hachage qui est inférieur à la cible. Tout ce que ce mineur a à faire est de publier le bloc miné avec les six composants originaux à n'importe quel nœud connecté.

Ce nœud recevant le bloc vérifiera d'abord l'ensemble des transactions, en s'assurant que toutes les transactions sont valides (par exemple, toutes les transactions sont correctement signées, et les pièces ne sont pas dépensées deux fois et/ou créées à partir de rien).

Il **double-hachera** simplement l'en-tête de bloc et s'assurera que la valeur est inférieure à la valeur cible incluse dans le bloc. Une fois le bloc jugé valide, le nouveau nœud continuera à propager ce bloc à travers le réseau jusqu'à ce que chaque nœud ait un registre à jour.

Comme vous pouvez le voir, les nouveaux blocs publiés peuvent facilement être vérifiés par n'importe quel nœud donné. Cependant, la publication d'un bloc valide sur le réseau nécessite une quantité incroyablement grande de puissance de calcul (donc, d'électricité et de temps). Cette asymétrie est ce qui permet au réseau d'être sécurisé tout en permettant simultanément aux individus qui souhaitent mener des activités économiques sur le réseau de le faire de manière relativement transparente.

### Le temps de bloc et l'ajustement de la cible

Alors que les premiers mineurs ont commencé à miner, ils ont chacun surveillé le **temps de bloc**. Chaque bloc Bitcoin a un temps de bloc fixé à 10 minutes. Cela signifie que, étant donné le niveau actuel de puissance de calcul (**taux de hachage du réseau**) sur le réseau, les nœuds s'attendront toujours à ce que de nouveaux blocs validés soient produits toutes les 10 minutes en moyenne.

Nous pouvons raisonnablement nous attendre à ce que les blocs soient produits en 10 minutes car la probabilité de trouver un bloc, étant donné le taux de hachage du réseau, est connue.

Par exemple, prenons la cible la plus facile qui ait jamais existé dans Bitcoin : le bloc genesis. La probabilité qu'un seul hachage soit inférieur à la cible la plus facile est de 1 sur 2³². C'est une chance sur plus de quatre milliards. Par conséquent, nous pouvons raisonnablement nous attendre à ce que quelqu'un exécute 2³² itérations du problème de minage afin de trouver un hachage approprié. Les nœuds du réseau s'attendaient à ce que quatre milliards de ces itérations soient exécutées sur **tous** les mineurs du réseau toutes les 10 minutes.

Si, sur un grand échantillon de blocs, les blocs commencent à apparaître plus rapidement que toutes les 10 minutes, c'est une indication assez claire que les nœuds du réseau itèrent à travers quatre milliards de hachages beaucoup plus rapidement que toutes les 10 minutes. Cette situation incite chaque nœud à ajuster la cible proportionnellement en fonction de l'augmentation (ou de la diminution) de la puissance du réseau pour s'assurer que les blocs continuent à être produits toutes les 10 minutes.

En réalité, les nœuds du réseau surveillent le temps de bloc sur **2016** blocs, ce qui correspond exactement à deux semaines. Toutes les deux semaines, le temps total de bloc est comparé au temps de bloc attendu (qui est de 20160 minutes).

Pour obtenir la nouvelle cible, il suffit de multiplier la cible existante par le rapport du temps total de bloc réel sur les deux dernières semaines pour obtenir le temps de bloc attendu. Cela ajustera la cible proportionnellement à la quantité de puissance de calcul entrant ou sortant du réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/M3-52KmmkeyZCRECDfzfdACTrILXpveYlDn5)
_La formule pour calculer la nouvelle cible, exécutée toutes les 20160 minutes (deux semaines) par chaque nœud Bitcoin_

Le temps de bloc et la capacité de calculer facilement la probabilité de trouver un bloc valide permettent aux nœuds de surveiller et de déterminer facilement la puissance de hachage totale sur le réseau et d'ajuster le réseau. Peu importe la quantité de puissance de calcul ajoutée au réseau ou la rapidité avec laquelle elle est ajoutée, en moyenne, le temps de bloc restera toujours à 10 minutes.

Le taux de hachage total actuel sur le réseau est de 28,27 exahash par seconde. Cela représente **_28,27 x 10¹⁸_** hachages exécutés chaque seconde sur tous les ordinateurs du réseau.

![Image](https://cdn-media-1.freecodecamp.org/images/d9dUC5kBAfoDhYFAhuUIF-49pjPT-risoGxB)

### En résumé

Nous avons maintenant couvert de manière exhaustive les points suivants :

* Pourquoi le hachage cryptographique à sens unique est vital pour la preuve de travail
* Une décomposition de la construction d'un bloc Bitcoin
* Le processus de minage réel et l'itération elle-même
* Comment les nœuds peuvent facilement valider d'autres blocs
* Comment le réseau parvient à maintenir l'algorithme et la compétitivité en surveillant le temps de bloc et en ajustant la cible

Vous devriez maintenant être en mesure de comprendre et d'expliquer comment la preuve de travail fonctionne réellement et pourquoi elle est considérée comme un algorithme entièrement sécurisé qui permet la décentralisation et le consensus !

**Suivez-moi sur [Twitter](https://twitter.com/SubhanNadeem19) et Medium si vous êtes intéressé par des articles plus approfondis et informatifs comme celui-ci à l'avenir !**