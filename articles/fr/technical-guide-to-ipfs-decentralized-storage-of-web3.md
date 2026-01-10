---
title: Un guide technique sur IPFS – le stockage décentralisé du Web3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-21T16:38:36.000Z'
originalURL: https://freecodecamp.org/news/technical-guide-to-ipfs-decentralized-storage-of-web3
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/tech_guide_ipfs_web3coach_banner-1.png
tags:
- name: Blockchain
  slug: blockchain
- name: decentralization
  slug: decentralisation
- name: ipfs
  slug: ipfs
- name: Web3
  slug: web3
seo_title: null
seo_desc: 'Par Lukas Lukac

  Lorsque vous pensez au développement d''une application décentralisée, une blockchain comme Ethereum
  vous vient probablement à l''esprit.

  La blockchain est fantastique pour gérer l''état, automatiser les processus via des Smart Contracts,
  et échanger de la valeur économique.

  Vous po...'
---

Par Lukas Lukac

Lorsque vous pensez au développement d'une application décentralisée, une blockchain comme Ethereum vous vient probablement à l'esprit.

La blockchain est fantastique pour gérer l'état, automatiser les processus via des Smart Contracts, et échanger de la valeur économique.

Vous pouvez [suivre ce tutoriel pour apprendre la blockchain en en créant une vous-même à partir de zéro](https://www.freecodecamp.org/news/build-a-blockchain-in-golang-from-scratch/) si vous souhaitez en savoir plus.

**Mais où stockez-vous le contenu de votre application ?** Les images ? Les vidéos ? Le front-end du site web de l'application composé de tous les fichiers HTML, CSS et JS ? Votre application et le contenu de vos utilisateurs sont-ils chargés depuis un serveur AWS centralisé ?

Stocker le contenu sur la blockchain serait coûteux et inefficace.

Votre application blockchain a besoin d'un stockage décentralisé !

Dans ce tutoriel, je vais vous présenter l'InterPlanetary File System, ou IPFS. Vous apprendrez :

1.  Comment stocker et récupérer du contenu depuis un stockage décentralisé
2.  Comment faire tourner votre nœud IPFS
3.  Tout sur les rouages internes de bas niveau du protocole IPFS
4.  Et nous lirons un site Wikipedia stocké sur IPFS

Prêt ? C'est parti.

## Table des matières

*   [Qu'est-ce que IPFS ?](#heading-quest-ce-que-ipfs)
*   [Comment installer un nœud IPFS](#heading-comment-installer-un-noeud-ipfs)
*   [Comment stocker et récupérer du contenu IPFS en utilisant la CLI et HTTP](#heading-comment-utiliser-ipfs)
*   [Qu'est-ce que le CID – l'identifiant basé sur le contenu IPFS](#heading-comment-fonctionne-ladressage-de-contenu-ipfs)
*   [Comment faire de la rétro-ingénierie sur le datastore IPFS](#heading-comment-ipfs-stocke-le-contenu-sur-le-systeme-de-fichiers)
*   [Comment connecter un nœud IPFS à un réseau décentralisé](#heading-comment-connecter-un-noeud-ipfs-au-reseau-p2p)
*   [Comment échanger des données en utilisant le protocole pair-à-pair Bitswap](#heading-comment-les-noeuds-echangent-des-donnees-via-le-protocole-bitswap)
*   [Comment persister le contenu du réseau pair-à-pair](#heading-comment-persister-le-contenu-du-reseau-p2p)

## Qu'est-ce que IPFS ?

L'InterPlanetary File System, ou IPFS pour faire court, est un protocole hypermédia pair-à-pair conçu pour rendre le web plus rapide, plus sûr et plus ouvert.

**IPFS est un protocole pour stocker et partager du contenu.** Comme dans le monde de la blockchain, chaque utilisateur fait tourner son nœud (serveur). Les nœuds peuvent communiquer entre eux et échanger des fichiers.

### Qu'est-ce qui rend IPFS unique ?

Tout d'abord, **IPFS est décentralisé** car il charge le contenu depuis des milliers de pairs au lieu d'un serveur centralisé unique. Chaque morceau de donnée est haché cryptographiquement, résultant en un **identifiant de contenu** unique et sûr : le CID.

Stockez votre site web sur IPFS pour éviter la censure et un point de défaillance unique. Votre nœud IPFS personnel est hors ligne ? Ne vous inquiétez pas, le site web se chargera toujours depuis d'autres nœuds à travers le monde qui le servent.

Par exemple, supposez que votre gouvernement bannisse Wikipedia. Dans ce cas, vous pouvez toujours accéder à une version décentralisée de Wikipedia indexée le 17 avril en la chargeant depuis le réseau pair-à-pair IPFS persisté sous le CID :

> **"**QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX"

Deuxièmement, l'intégrité du **contenu IPFS peut être vérifiée cryptographiquement.**

Et enfin, **le contenu IPFS est dédupliqué.** Si vous essayiez de stocker deux fichiers identiques de 1 Mo dans le même nœud IPFS, ils ne seraient stockés qu'une seule fois, éliminant la duplication, car leur hachage produirait un **CID** identique.

## Comment installer un nœud IPFS

### Installer IPFS

Ouvrez la page d'installation de la [documentation officielle IPFS](https://docs.ipfs.io/install/) et suivez les instructions selon votre système d'exploitation (Windows, macOS, Linux). Je documenterai le processus d'installation Ubuntu ci-dessous.

%[https://docs.ipfs.io/install/command-line/#official-distributions]

Je préfère compiler le dépôt [ipfs/go-ipfs](http://github.com/ipfs/go-ipfs) à partir de zéro pour déboguer le code si nécessaire, et soyons honnêtes : GoLang déchire.

#### Compiler la base de code en Go

Clonez le dépôt et exécutez le script d'installation dans le Makefile.

```
git clone https://github.com/ipfs/go-ipfs.git
cd go-ipfs
git checkout v0.8.0-rc2
make install
```

Ou téléchargez IPFS pré-compilé :

```
sudo snap install ipfs
```

### Valider l'installation

Soyons honnêtes. Go est incroyable et compiler la base de code soi-même est classe et décentralisé. Le binaire résultant sera créé dans votre `$GOPATH`.

```
which ipfs
> /home/web3coach/go/bin/ipfs

ipfs version
> ipfs version 0.8.0-rc2
```

### Initialiser un nouveau nœud

Exécutez `ipfs init` pour créer votre nouveau nœud. Par défaut, il créera un dossier et stockera toutes les données dans `~/.ipfs`. Vous pouvez ajuster cela en configurant la variable d'environnement `IPFS_PATH`.

```
IPFS_PATH=/home/web3coach/.ipfs_tutorial ipfs init

> generating ED25519 keypair...done
> peer identity: 12D3Koo...dNs
> initializing IPFS node at /home/web3coach/.ipfs_tutorial
```

Votre nœud est maintenant entièrement initialisé, attendant votre contenu.

## Comment utiliser IPFS

### Ajouter du contenu

IPFS peut gérer toutes sortes de types de données différents – des simples chaînes de caractères aux images, vidéos et sites web.

Commencez par stocker un court message `hello IPFS world by Web3Coach` :

```
echo "hello IPFS world by Web3Coach. BTW: Ethereum FTW" | ipfs add
```

Le contenu est maintenant stocké et **indexé par une fonction de hachage cryptographique** retournant son identifiant de contenu unique (CID) :

```
> added QmRBkKi1PnthqaBaiZnXML6fH6PNqCFdpcBxGYXoUQfp6z
> 49 B / 49 B [========] 100%
```

Votre nœud IPFS générera le même CID sur votre système de fichiers local que dans ce tutoriel. C'est parce qu'IPFS hache le contenu et retourne son empreinte unique, et comme nous le savons, une fonction de hachage sécurisée retournera toujours la même sortie pour une même entrée donnée.

### Épingler (Pin) du contenu

Lorsque vous faites `add` (ajouter) du contenu, vous l'ajoutez UNIQUEMENT à votre nœud local. Le **contenu ne se réplique PAS automatiquement** à travers tout le réseau – c'est une confusion courante chez les utilisateurs et développeurs IPFS.

Lorsque vous stockez du contenu via la commande `add`, IPFS exécutera également la commande `pin` par défaut :

```
ipfs pin add QmRBkKi1PnthqaBaiZnXML6fH6PNqCFdpcBxGYXoUQfp6z
```

Pour répliquer le contenu, **vous devez mettre votre nœud en ligne, rejoindre le réseau p2p, et `pin` (épingler) le CID spécifique depuis un autre nœud.** Vous apprendrez comment faire cela plus loin dans le tutoriel et découvrirez ce qui se passe en arrière-plan.

### Lire du contenu

Copiez-collez le **CID** dans la commande IPFS `cat` pour le lire depuis le disque :

```
ipfs cat QmRBkKi1PnthqaBaiZnXML6fH6PNqCFdpcBxGYXoUQfp6z
> hello IPFS world by Web3Coach. BTW: Ethereum FTW
```

Les commandes `add`, `pin` et `cat` sont les fonctions IPFS les plus significatives, et vous venez de les apprendre. Félicitations, bien joué !

## Comment fonctionne l'adressage de contenu IPFS

Qu'est-ce que QmRBkKi1PnthqaBaiZnXML6fH6PNqCFdpcBxGYXoUQfp6z ?

C'est un identifiant basé sur le contenu auto-descriptif.

Que signifie réellement "auto-descriptif" ? Cela signifie qu'en découpant la chaîne selon la spécification IPFS, vous saurez tout ce que vous avez besoin de savoir sur les données qu'elle indexe.

*   quelle est la version du CID
*   comment lire la chaîne du CID (base32 ? base58 ? hex ?)
*   comment les données sont encodées
*   quelle fonction de hachage a créé l'empreinte des données
*   la longueur de la fonction de hachage

L'équipe IPFS a construit un [site web](https://cid.ipfs.io/) pratique pour analyser un CID :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/cid_analyse.png)

En analysant le CID **QmRBkKi1P…p6z**, vous découvrez :

*   le CID suit la spécification version 0 car il commence par **Qm**
*   la chaîne **QmRBkKi1P…p6z** est encodée en utilisant `base58btc`
*   les données "**hello IPFS world by Web3Coach. BTW: Ethereum FTW**" ont été encodées comme **DAG Protobuf** sous un codec **0x70** avant d'être stockées sur le disque
*   le code de hachage **0x12** signale l'empreinte des données obtenue en utilisant la fonction de hachage `sha256`, produisant un digest unique de 32 octets de long

"Légèrement plus compliqué" qu'un simple INT auto-incrémenté dans une table MySQL... mais extraordinairement puissant et pérenne. Laissez-moi expliquer.

### Versions de CID

Il y a actuellement deux versions de CID : **v0** et **v1**.

**Le CID v0** n'est pas flexible et est limité à :

*   commencer par les caractères "Qm"
*   la chaîne CID est encodée en utilisant base58btc
*   les données sont encodées avec dag-pb par défaut
*   peut être converti en CID version 1, mais pas l'inverse

**Le CID v1** exploite plusieurs préfixes pour une interopérabilité maximale :

> CID v1 = Multibase + Multicodec + Multihash

En d'autres termes, l'analyse du binaire en une chaîne CID v1 suit cette spécification :

`<base><codec><fonction-de-hachage><longueur-du-hachage><digest-du-hachage>`

### Multihash

Pour être pérenne et permettre différents algorithmes de hachage, IPFS a créé le standard suivant :

CODE : TAILLE : DIGEST

```go
type DecodedMultihash struct {
   Code   uint64 // 0x12
   Name   string // sha2-256
   Length int    // 32 octets
   Digest []byte // Digest contient les octets bruts du multihash
}
```

Multihash a de nombreux avantages. Lorsque les ordinateurs seront plus puissants dans 5 ans, vous pourrez utiliser une fonction de hachage plus forte comme `sha3-512` tant que vous configurez le code `0x13` correspondant comme Multihash dans le préfixe du CID – le protocole sera prêt à le gérer.

### Multicodec

L'attribut `Code` vous dit **comment les données sont encodées** avant d'être stockées sur le disque, afin que vous sachiez **comment les décoder** lorsque l'utilisateur veut les lire. Cela pourrait être n'importe quoi : CBOR, Protobuf, JSON…

IPFS maintient une liste publique de tous les [codecs possibles](https://github.com/multiformats/multicodec/blob/master/table.csv). Les codecs les plus courants sont :

```
raw       | ipld      | 0x55 | binaire brut
dag-pb    | ipld      | 0x70 | MerkleDAG protobuf
dag-cbor  | ipld      | 0x71 | MerkleDAG cbor

// mais vous pourriez aussi encoder des blocs Ethereum sur IPFS !
eth-block | ipld      | 0x90 | Bloc Ethereum (RLP)
```

### Multibase

Le problème avec le CID v0 et l'encodage `base58btc` est le manque d'interopérabilité entre les environnements. Un préfixe multibase ajoute le support pour différents encodages comme `base32` pour obtenir des noms compatibles DNS.

[Un tableau avec tous les encodages Multibase](https://github.com/multiformats/multibase/blob/master/multibase.csv) :

```
encoding  | code
base32    | b
base58btc | z
base64    | m
```

Vous repérez un encodage Multibase basé sur le premier caractère :

**Q**mRBkKi1PnthqaBaiZnXML6fH6PNqCFdpcBxGYXoUQfp6z

*   est un CID `v0`
*   la chaîne CID est encodée avec `base58btc`

**b**afybeibkjmxftowv4lki46nad4arescoqc7kdzfnjkqux257i4jonk44w4

*   CID `v1`
*   la chaîne CID est encodée avec `base32`

Les deux versions de CID peuvent récupérer le même contenu car après avoir retiré l'encodage, c'est le **Multihash** qui indexe les blocs au niveau du datastore. En revanche, Multibase est seulement utilisé pour passer le CID correctement dans différents environnements (CLI, URL, DNS).

```
ipfs cat QmRBkKi1PnthqaBaiZnXML6fH6PNqCFdpcBxGYXoUQfp6z
> hello IPFS world by Web3Coach. BTW: Ethereum FTW

// équivalent à
ipfs cat bafybeibkjmxftowv4lki46nad4arescoqc7kdzfnjkqux257i4jonk44w4
> hello IPFS world by Web3Coach. BTW: Ethereum FTW
```

Ouf. Les choses sont devenues "légèrement complexes" très rapidement.

En parlant de sujets compliqués, IPFS est puissant car il ne traite pas le contenu juste comme des "données" mais comme des **structures de données** – spécifiquement la structure **InterPlanetary Linked Data** : [IPLD](https://docs.ipld.io/#what-is-ipld). En bref, vous pouvez implémenter n'importe quel système de fichiers, base de données ou structure par-dessus IPLD.

Par exemple, vous pouvez stocker tous les blocs Ethereum sur IPFS tant que vous définissez les codecs `eth-block` et `eth-tx` et enregistrez un Décodeur approprié lors du travail avec le graphe IPLD.

Creusons un peu et explorons la structure IPLD par défaut avec le codec DAG Protobuf.

## Comment IPFS stocke le contenu sur le système de fichiers

“La commande `ipfs add` créera un **Merkle DAG** à partir des données suivant le [format de données UnixFS](https://github.com/ipfs/go-unixfs/blob/master/pb/unixfs.proto). Votre contenu est découpé en **blocs** à l'aide d'un **Chunker**, puis arrangé dans une **structure arborescente utilisant des 'nœuds de lien'** pour les relier ensemble. Le CID retourné est le hachage du nœud racine dans le DAG.”

Confus ?

Revenons aux bases.

### Explorons le répertoire de données du nœud

Au début de ce tutoriel, lorsque vous avez initialisé votre nœud IPFS avec la commande `ipfs init`, vous avez généré le répertoire suivant :

```
export IPFS_PATH=/home/web3coach/.ipfs_tutorial
cd $IPFS_PATH
~/.ipfs_tutorial  tree

.
├── blocks
│   ├── 6Y
│   │   └── CIQA4XCGRCRTCCHV7XSGAZPZJOAOHLPOI6IQR3H6YQ.data
├── config
├── datastore
│   ├── 000002.ldb
│   ├── 000003.log
│   ├── CURRENT
│   ├── CURRENT.bak
│   ├── LOCK
│   ├── LOG
│   └── MANIFEST-000004
├── datastore_spec
├── keystore
└── version
```

D'un point de vue de très **haut niveau :**

*   `blocks` — IPFS stocke toutes les données découpées (chunked) ici, bien que les interfaces flexibles de `go-ipfs` **vous permettent d'échanger l'implémentation de stockage** pour une base de données différente
*   `config` — Paramètres du nœud (système de fichiers, identité, specs, réseau)
*   `datastore` — Indexation et autre logique

Ne me croyez pas sur parole. Créez un nouveau fichier avec le contenu suivant sur votre système de fichiers local et ajoutez-le ensuite à IPFS :

```
hello IPFS world by Web3Coach. Testing DAGs
hello IPFS world by Web3Coach. Testing DAGs
hello IPFS world by Web3Coach. Testing DAGs

ls -la hello_world.txt
> 131 bytes hello_world.txt

ipfs add hello_world.txt
> added QmNtQtxeavDXTjCiWAAaxnhKK3LBYfFfpXUXjdMDYXwKtH
```

En faisant de la rétro-ingénierie sur la base de code `go-ipfs`, voici ce qui se passe en coulisses :

![Image](https://www.freecodecamp.org/news/content/images/2021/06/IPFS_UNIX_FS_Protobuf.png)
_IPFS UnixFS ajoutant un nouveau fichier et le convertissant en un bloc_

Validez le processus de persistance en inspectant le répertoire blocks. Vous trouverez que le contenu a été écrit sous la Clé Multihash Datastore en utilisant l'**encodage DAG Protobuf** (131 octets + encodage extra Protobuf).

```
ls -la blocks/PV/
> 142 CIQAQIXXW2OAQSKZ6AQ2SDEYRZXWPDZNJUAFR3YORYN75I5CQ3LHPVQ.data

vim blocks/PV/CIQA...
<8b>^A^H^B^R<83>^Ahello IPFS world by Web3Coach. Testing DAGs
hello IPFS world by Web3Coach. Testing DAGs
hello IPFS world by Web3Coach. Testing DAGs^X<83>^A
```

Pour interagir avec votre contenu brut, utilisez la commande `ipfs object`.

```
ipfs object get QmNtQtxeavDXTjCiWAAaxnhKK3LBYfFfpXUXjdMDYXwKtH | jq
```

```json
{
  "Links": [],
  "Data": "\b\u0002\u0012\u0001hello IPFS world by Web3Coach. Testing DAGs\nhello IPFS world by Web3Coach. Testing DAGs\nhello IPFS world by Web3Coach. Testing DAGs\u0018\u0001"
}
```

*   Parce que le contenu fait seulement 131 octets, il tient dans un seul Nœud DAG
*   Le Nœud DAG est persisté comme un seul Bloc sur le disque
*   Le Nœud DAG a zéro lien vers d'autres Nœuds

Il est temps d'expérimenter.

Ajoutez le même fichier à nouveau, mais configurez le Chunker à 64 octets (ou utilisez un fichier plus gros, mais un Chunker plus petit démontrera mieux le concept).

```
ipfs add --chunker=size-64 hello_world.txt

> 131 bytes QmTwtTQgrTaait2qWXYjTsEZiF4sT7CD4U87VqQ27Wnsn8
```

**Vous obtenez un nouveau CID !**

IPFS a divisé le contenu en 4 Nœuds DAG et a écrit 4 Blocs avec les données encodées au format DAG Protobuf sur le disque.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/ipfs_chunker_4.png)
_IPFS divise un fichier en plusieurs morceaux (Nœuds DAG + Blocs)_

```
ipfs object get QmTwtTQgrTaait2qWXYjTsEZiF4sT7CD4U87VqQ27Wnsn8 | jq
```

```json
{
  "Links": [
    {
      "Name": "",
      "Hash": "QmTbsuUYzy3nT6NApb5t7VUq3iQKZXrJJJY2j1miMVgaJU",
      "Size": 72
    },
    {
      "Name": "",
      "Hash": "QmNy9iFF8uU1Cn7trxpSgqxMsjmi4zQ7xgyEgsWff5rnfH",
      "Size": 72
    },
    {
      "Name": "",
      "Hash": "QmdEitCfYgBNxLhxTNvdLaDmTypSAWkGErjw33VZxUbWK3",
      "Size": 11
    }
  ],
  "Data": "\b\u0002\u0018\u0001 @ @ \u0003"
}

```

Le test ultime est de récupérer les données de chaque Nœud DAG et de vérifier que le texte est divisé en trois morceaux :

**Nœud DAG Protobuf 1 :**

```
ipfs object get QmTbsuUYzy3nT6NApb5t7VUq3iQKZXrJJJY2j1miMVgaJU | jq
```

```json
{
  "Links": [],
  "Data": "\b\u0002\u0012@hello IPFS world by Web3Coach. Testing DAGs\nhello IPFS world by \u0018@"
}
```

**Nœud DAG Protobuf 2 :**

```
ipfs object get QmNy9iFF8uU1Cn7trxpSgqxMsjmi4zQ7xgyEgsWff5rnfH | jq
```

```json
{
  "Links": [],
  "Data": "\b\u0002\u0012@Web3Coach. Testing DAGs\nhello IPFS world by Web3Coach. Testing D\u0018@"
}
```

**Nœud DAG Protobuf 3 :**

```
ipfs object get QmdEitCfYgBNxLhxTNvdLaDmTypSAWkGErjw33VZxUbWK3 | jq
```

```json
{
  "Links": [],
  "Data": "\b\u0002\u0012\u0003AGs\u0018\u0003"
}
```

### Quel est l'avantage de diviser le contenu en plusieurs morceaux et d'utiliser l'adressage de contenu et les CIDs ?

*   Déduplication des données
*   Décentralisation

La prochaine fois que vous voudrez stocker un fichier qui partagerait une partie du contenu avec un autre fichier, IPFS ne stockerait pas un bloc dupliqué ! Il ferait plutôt un lien vers un Nœud DAG déjà existant et ne stockerait que les nouveaux morceaux uniques.

Convertir le contenu en un graphe orienté acyclique avec de nombreux nœuds aide également à charger le contenu en parallèle. Par exemple, un article de blog, une image, un site Wikipedia entier peuvent se charger depuis plusieurs nœuds pairs IPFS. Votre nœud vérifie ensuite l'intégrité des blocs reçus en re-hachant tout le contenu des données et en affirmant le CID construit.

Vous avez maintenant appris le B.A.-BA d'IPFS – excellent progrès !

Il reste un composant critique : le **Réseau**.

## Comment connecter un nœud IPFS au réseau p2p

Chaque nœud a son fichier `config` généré durant l'exécution de `ipfs init`.

Ouvrez-le.

```
vim $IPFS_PATH/config
```

Autres paramètres mis à part, vous trouvez l'**Identité (PeerID + Clé Privée) de votre nœud :**

```
"Identity": {
    "PeerID": "12D3KooWCBmDtsvFwDHEr...",
    "PrivKey": "CAESQCj..."
  },
```

Et une liste d'**adresses d'amorçage (Bootstrap) :**

```json
"Bootstrap": [
    "/dnsaddr/bootstrap.libp2p.io/p2p/QmcZf59b...gU1ZjYZcYW3dwt",
    "/ip4/104.131.131.82/tcp/4001/p2p/QmaCpDMG...UtfsmvsqQLuvuJ",
    "/ip4/104.131.131.82/udp/4001/quic/p2p/Qma...UtfsmvsqQLuvuJ",
    "/dnsaddr/bootstrap.libp2p.io/p2p/QmNnooD5...BMjTezGAJN",
    "/dnsaddr/bootstrap.libp2p.io/p2p/QmQCU2Ec...J16u19uLTa",
    "/dnsaddr/bootstrap.libp2p.io/p2p/QmbLHAnM...Ucqanj75Nb"
  ],
```

Vous vous connectez à d'autres pairs dans le réseau IPFS en exécutant la commande `ipfs daemon`. Votre nœud établira d'abord une connexion p2p avec les nœuds d'amorçage de Protocol Labs (l'entreprise derrière IPFS), et à travers ces nœuds d'amorçage, vous trouverez ensuite des centaines d'autres pairs.

```
ipfs daemon 

> Initializing daemon...

Swarm listening on /ip4/127.0.0.1/tcp/4001
Swarm listening on /ip4/127.0.0.1/udp/4001/quic
Swarm listening on /ip4/172.17.0.1/tcp/4001
Swarm listening on /ip4/172.17.0.1/udp/4001/quic
Swarm listening on /ip4/192.168.0.142/tcp/4001
Swarm listening on /ip4/192.168.0.142/udp/4001/quic
Swarm listening on /ip6/::1/tcp/4001
Swarm listening on /ip6/::1/udp/4001/quic
Swarm listening on /p2p-circuit
Swarm announcing /ip4/127.0.0.1/tcp/4001
Swarm announcing /ip4/127.0.0.1/udp/4001/quic
Swarm announcing /ip4/192.168.0.142/tcp/4001
Swarm announcing /ip4/192.168.0.142/udp/4001/quic
Swarm announcing /ip4/88.212.40.160/udp/4001/quic
Swarm announcing /ip6/::1/tcp/4001
Swarm announcing /ip6/::1/udp/4001/quic

API server listening on /ip4/127.0.0.1/tcp/5001
WebUI: http://127.0.0.1:5001/webui

Gateway (readonly) server listening on /ip4/127.0.0.1/tcp/8080
Daemon is ready!
```

Gardez à l'esprit qu'en exécutant le **Démon IPFS** :

1.  Votre nœud se connecte au réseau p2p et peut **échanger des blocs avec d'autres nœuds**
2.  **D'autres pairs peuvent accéder au contenu sur votre nœud** – tant qu'ils connaissent les CIDs
3.  Les pairs vous parleront via TCP, UDP sur le port : **4001**
4.  Si vous avez une application, commencez à stocker et consommer le contenu de votre nœud via l'API HTTP écoutant sur le port : **5001**.

Pour le développement d'applications, je recommande la bibliothèque officielle [ipfs-http-client](https://www.npmjs.com/package/ipfs-http-client) en JS exposant toutes les commandes principales – add, cat, object et autres. Cela accélérera votre progression en code.

J'utiliserai `curl` pour interagir avec l'API pour garder ce tutoriel "court".

### Comment utiliser l'API HTTP IPFS :

**Ajouter du contenu :** :5001/api/v0/add

```
curl -X POST -F file=@/home/web3coach/go/src/github.com/ipfs/go-ipfs/hello_world.txt "http://127.0.0.1:5001/api/v0/add"
```

```json
{"Name":"hello_world.txt","Hash":"QmNtQtxeavDXTjCiWAAaxnhKK3LBYfFfpXUXjdMDYXwKtH","Size":"142"}
```

**Lire du contenu :** :5001/api/v0/cat

```
curl -X POST "http://127.0.0.1:5001/api/v0/cat?arg=QmNtQtxeavDXTjCiWAAaxnhKK3LBYfFfpXUXjdMDYXwKtH"
 
hello IPFS world by Web3Coach. Testing DAGs
hello IPFS world by Web3Coach. Testing DAGs
hello IPFS world by Web3Coach. Testing DAGs
```

Voir la [documentation officielle de l'API HTTP](https://docs.ipfs.io/reference/http/api/#getting-started) pour la liste complète des commandes disponibles.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/Screenshot-from-2021-05-26-19-54-49.png)

### Comment s'appairer avec d'autres nœuds IPFS

Expérience amusante. Utilisez la commande `ipfs swarm` et vérifiez combien de nœuds vous avez déjà découverts :

```
ipfs swarm peers

> 
/ip4/85.70.151.37/tcp/4001/p2p/QmSuCtR...aPq6h4AczBPZaoej
/ip4/91.121.168.96/udp/54001/quic/p2p/QmeC7H...8j2TQ99esS
...
...
...

ipfs swarm peers | wc -l
> 186
```

Bravo ! Vous êtes connecté à 186 pairs formant un web pair-à-pair inarrêtable.

### Qu'en est-il de la confidentialité ?

Les autres pairs peuvent accéder à tout le contenu que vous ajoutez à votre nœud IPFS. Il n'y a **aucun mécanisme de confidentialité intégré, donc n'ajoutez jamais de contenu non chiffré, sensible/personnel** à IPFS !

## Comment les nœuds échangent des données via le protocole Bitswap

Jusqu'à présent, vous avez seulement interagi avec votre contenu local. Imaginez que vous vivez dans un endroit où le gouvernement local a décidé de bloquer l'accès à Wikipedia. Pas cool.

Heureusement, parce que quelqu'un a ajouté tout le contenu de Wikipedia à IPFS, vous pouvez faire tourner votre nœud et accéder à ses connaissances en demandant le contenu à des pairs à travers le monde.

[http://localhost:8080/ipfs/QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX/wiki/Anasayfa.html](http://localhost:8080/ipfs/QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX/wiki/Anasayfa.html)

Le Service DAG vérifiera les blocs dans votre datastore, mais il n'en trouvera aucun pour QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX.

Le nœud créera donc une requête réseau vers ses pairs en utilisant le protocole Bitswap via le composant `exchange` :

```go
func getBlock(ctx context.Context, c cid.Cid, bs blockstore.Blockstore, fget func() exchange.Fetcher) (blocks.Block, error) {
   err := verifcid.ValidateCid(c) // sécurité du hachage
   if err != nil {
      return nil, err
   }

   block, err := bs.Get(c)
   if err == nil {
      return block, nil
   }

   if err == blockstore.ErrNotFound && fget != nil {
      f := fget() // Ne pas charger l'échange tant que ce n'est pas nécessaire

      log.Debug("Blockservice: Searching bitswap")
      blk, err := f.GetBlock(ctx, c)
```

En interne, le CID est ajouté à une `Wantlist` :

```go
// Wantlist est une liste brute de blocs désirés et leurs priorités
type Wantlist struct {
   set map[cid.Cid]Entry
}

// Entry est une entrée dans une liste de souhaits, composée d'un cid et de sa priorité
type Entry struct {
   Cid      cid.Cid
   Priority int32
   WantType pb.Message_Wantlist_WantType
}
```

Et le `PeerManager` itérera sur les pairs connus et leurs pairs jusqu'à ce qu'il trouve un nœud en ligne capable de fournir le Bloc désiré :

```go
// PeerManager gère un pool de pairs et envoie des messages aux pairs du pool.
type PeerManager struct {
   pqLk sync.RWMutex
   
   peerQueues map[peer.ID]PeerQueue
   pwm        *peerWantManager

   createPeerQueue PeerQueueFactory
   ctx             context.Context

   psLk         sync.RWMutex
   sessions     map[uint64]Session
   peerSessions map[peer.ID]map[uint64]struct{}

   self peer.ID
}
```

Le résultat ?

Vous pouvez consommer les fruits défendus de Wikipedia directement depuis **localhost:8080** :

![Image](https://www.freecodecamp.org/news/content/images/2021/05/wikipedia_local_ipfs.png)
_IPFS chargeant Wikipedia sur votre nœud local_

Stockage incensurable et décentralisé :)

## Comment persister le contenu du réseau p2p

Vous devez savoir une chose cruciale à propos d'IPFS : le contenu auquel vous accédez depuis le réseau sera nettoyé par le ramasse-miettes (Garbage Collector) à moins que vous ne l'**épingliez (pin)**.

### Épinglage et Garbage Collection

Au début de l'article, vous avez appris que le contenu ajouté à votre nœud via la commande `ipfs add` ou son équivalent HTTP est épinglé par défaut.

```
ipfs pin ls | grep QmNtQtxeavDXTjCiWAAaxnhKK3LBYfFfpXUXjdMDYXwKtH
> QmNtQtxeavDXTjCiWAAaxnhKK3LBYfFfpXUXjdMDYXwKtH recursive
```

**Les blocs épinglés sont marqués comme NE DEVANT PAS ÊTRE SUPPRIMÉS** lorsque le Garbage Collection s'exécute.

Pourquoi le Garbage Collection supprimerait-il certains blocs ? Pour garder votre nœud en bonne santé en contrôlant sa taille de stockage.

En lisant Wikipedia ou en accédant à tout autre contenu du réseau p2p, IPFS télécharge ses blocs. À mesure que le datastore du nœud grandit en taille, un processus périodique de garbage collection élaguera les blocs non épinglés, afin que vous ne manquiez pas d'espace disque.

Si vous voulez que votre contenu soit accessible 24/7 sur le réseau IPFS, je vous recommande d'utiliser un fournisseur distant fiable pour l'épingler : **[Infura](https://infura.io/docs/ipfs?utm_source=web3coach&utm_medium=article) -** est le moyen le plus simple de commencer, et vous obtenez 5 Go de stockage décentralisé gratuit.

![Image](https://www.freecodecamp.org/news/content/images/2021/06/Screenshot-from-2021-06-16-09-24-58.png)

Suivez la [documentation de démarrage.](https://infura.io/docs/ipfs?utm_source=web3coach&utm_medium=article)

### Comment épingler Wikipedia localement

Vérifiez que le CID de niveau racine de Wikipedia (le nœud DAG le plus haut) n'est pas encore épinglé sur votre nœud :

```
ipfs pin ls | grep QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX
> no output, not pinned
```

IPFS stocke des versions spécifiques de Wikipedia sous la forme d'un DAG. Je recommande d'inspecter son graphe avant d'épingler :

```
ipfs object get QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX | jq
```

```json
{
  "Links": [
    {
      "Name": "0C-",
      "Hash": "QmSEwJo8Z5bqVX3AhocyimJzPWetr7HgbWbwCg6zbp43AP",
      "Size": 1248085
    },
    {
      "Name": "43I",
      "Hash": "QmPW3kRjncDj145bP9DVNc791FowLPwYHnqbTzfe3whdyZ",
      "Size": 2611324931
    },
    {
      "Name": "58wiki",
      "Hash": "QmRNXpMRzsTHdRrKvwmWisgaojGKLPqHxzQfrXdfNkettC",
      "Size": 12295304394
    },
    {
      "Name": "92M",
      "Hash": "Qmbcvk7jpBTUKdgex139Nvv7BrKocE3pQVKhNJtTU77Qv5",
      "Size": 793
    },
    {
      "Name": "A0index.html",
      "Hash": "QmNqbYogAxH4mmt5WhuKN7NFEUDZ9V3Scxh7QbLwTKBJDk",
      "Size": 191
    }
  ],
  "Data": "\b\u0005\u0012\u0015\u0001\u0000\u0004\u0000\u0000\u0000\u0000\u0000\u0000\u0001\u0000\u0000\b\u0000\u0000\u0000\u0000\u0000\u0000\u0010\u0000(\"0\u0002"
}
```

L'objet DAG racine a cinq liens. Quatre liens sont relativement petits, mais **un lien pointe vers un nœud DAG avec une taille totale de 12 Go.** Si vous inspectez ce nœud DAG, vous verrez 256 liens supplémentaires et une taille cumulative (récursive) totale de 12 Go.

```
ipfs object stat QmRNXpMRzsTHdRrKvwmWisgaojGKLPqHxzQfrXdfNkettC

NumLinks:       256
BlockSize:      12075
LinksSize:      12034
DataSize:       41
CumulativeSize: 12295304394
```

Chaque nœud avec un article important épinglé, une vidéo, un documentaire ou un mème de chat rend le web plus accessible, antifragile, décentralisé et robuste.

```
ipfs pin add QmT5NvUtoM5nWFfrQdVrFtvGfKFmG7AHE8P34isapyhCxX
```

Le processus d'épinglage traversera récursivement le nœud DAG entier, récupérera tous ses liens depuis le protocole Bitswap et épinglera ensuite chaque Bloc unique sur votre datastore local.

Félicitations ! Dans cet article, vous avez appris comment le stockage décentralisé fonctionne en coulisses.

### J'ai travaillé 47 heures pour écrire cet article de blog… mais vous pouvez le re-tweeter en juste 5 secondes :

%[https://twitter.com/Web3Coach/status/1406997483281174528]