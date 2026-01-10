---
title: 'Apprendre par la pratique : une introduction simple et agréable à l''InterPlanetary
  File System'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-21T09:44:26.000Z'
originalURL: https://freecodecamp.org/news/ipfs-101-understand-by-doing-it-9f5622c4d4ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IbSEzAzdoh3aOvsG0fyiGA.png
tags:
- name: code
  slug: code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Tutorial
  slug: tutorial
seo_title: 'Apprendre par la pratique : une introduction simple et agréable à l''InterPlanetary
  File System'
seo_desc: 'By Niharika Singh

  Primer on IPFS

  IPFS is short for Inter Planetary File System. It is a peer-to-peer, distributed
  file system to make the web faster, safer, and more open. To shift from the present
  version of the web to a distributed version of the w...'
---

Par Niharika Singh

### Introduction à l'IPFS

IPFS est l'abréviation de InterPlanetary File System. C'est un système de fichiers distribué en peer-to-peer conçu pour rendre le [web plus rapide, plus sûr et plus ouvert.](https://ipfs.io/) Pour passer de la version actuelle du web à une version distribuée, nous avons besoin de l'IPFS. Essentiellement, l'objectif est de remplacer le HTTP.

**Il n'y a AUCUN serveur centralisé. Tout est décentralisé.** Voyons comment cela fonctionne en pratiquant.

_J'ai écrit un article sur la façon dont l'IPFS utilise MerkleDAG, qui peut être trouvé [ici](https://hackernoon.com/ipfs-and-merkle-forest-a6b7f15f3537)._

### ÉTAPE 1 : Installer l'IPFS

La version alpha de l'IPFS est écrite en GoLang. Vous devrez la télécharger pour votre plateforme à partir de [ce lien](https://ipfs.io/docs/install/).

Pour vérifier que vous avez correctement installé l'IPFS, ouvrez la console de commande et entrez la commande suivante.

```
$ ipfs help
```

Si vous voyez quelque chose qui commence comme ceci :

```
USAGE
```

```
ipfs - Global p2p merkle-dag filesystem.
```

```
ipfs [--config=<config> | -c] [--debug=<debug> | -D] [--help=<help>] [-h=<h>] [--local=<local> | -L] [--api=<api>] <command> ...
```

Alors vous êtes prêt !

![Image](https://cdn-media-1.freecodecamp.org/images/yDjQnIwZUm2seDD83k1bYg9Gd6yEK4Ak7fWQ)

### Étape 2 : Initialiser le nœud IPFS

Pour initialiser votre machine locale en tant que nœud IPFS, exécutez la commande suivante :

```
$ ipfs init
```

Cette commande initialise les fichiers de configuration IPFS et génère une nouvelle paire de clés utilisant RSA 2048 bits. Cela produira votre **identité de pair (peer identity)** en sortie.

Vous verrez quelque chose comme ceci :

```
initializing IPFS node at /Users/niharikasingh/.ipfs
```

```
generating 2048-bit RSA keypair...done
```

```
peer identity: QmTo1oMgGEH6Ym3H1xF55U7q4bexd5288YmEJjubDqVmKn
```

```
to get started, enter:
```

```
ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme
```

**Vous aurez une identité de pair différente de la mienne.**

Maintenant, exécutez la commande suivante pour voir le message de bienvenue :

```
$ ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme
```

Vous verrez un résultat qui ressemble à ceci :

```
Hello and Welcome to IPFS!
```

```
██╗██████╗ ███████╗███████╗
```

```
██║██╔══██╗██╔════╝██╔════╝
```

```
██║██████╔╝█████╗  ███████╗
```

```
██║██╔═══╝ ██╔══╝  ╚════██║
```

```
██║██║     ██║     ███████║
```

```
╚═╝╚═╝     ╚═╝     ╚══════╝
```

```
If you're seeing this, you have successfully installed
```

```
IPFS and are now interfacing with the ipfs merkledag!
```

```
-------------------------------------------------------
```

```
| Warning:                                              |
```

```
|   This is alpha software. Use at your own discretion! |
```

```
|   Much is missing or lacking polish. There are bugs.  |
```

```
|   Not yet secure. Read the security notes for more.   |
```

```
-------------------------------------------------------
```

```
Check out some of the other files in this directory:
```

```
./about
```

```
./help
```

```
./quick-start     <-- usage examples
```

```
./readme          <-- this file
```

```
./security-notes
```

**Voilà !**

### Étape 3 : Ajouter des fichiers à l'IPFS

Créez un dossier de démonstration n'importe où sur votre machine et ajoutez-y quelques fichiers. N'importe quel type de fichiers : images, vidéos, musique… littéralement n'importe quoi. Vous pouvez même ajouter un autre dossier à l'intérieur de ce dossier.

![Image](https://cdn-media-1.freecodecamp.org/images/U1AAtYHLUIf2v6R6zKfdkx6ruHdul0tIQuuA)
_Voici à quoi ressemble mon dossier de démonstration._

Supposons que le dossier soit nommé **"test-ipfs"**. Pour envoyer ces fichiers, naviguez d'abord dans ce dossier sur votre ligne de commande, puis exécutez la commande suivante :

```
$ ipfs add -r .
```

Cette commande ajoute tous les fichiers/répertoires présents dans le dossier à l'IPFS de manière récursive pour créer le MerkleDAG IPFS. Vous pouvez même ajouter un seul fichier en utilisant la commande suivante : `$ ipfs add <nom_du_fichier.extension>`

Cela crée la sortie suivante :

```
added QmSTuTEThyESvDgmYdao2HK6kurXe2pqjA1KHPD8wSHVy7 test-ipfs/donut.jpeg
```

```
added QmSR9MJ5resQLjwqy7kEVVKJwTvDG53Npt9i1c6jZeZDtW test-ipfs/purse.jpeg
```

```
added QmUNLLsPACCz1vLxQVkXqqLX5R1X345qqfHbsf67hvA3Nn test-ipfs/folder1
```

```
added QmaKZ3dnc9ejBdGgEDCRtsLFNRxcY67HLjk6gXUnk9sdM9 test-ipfs
```

Vous remarquerez que cette longue chaîne est le hachage unique de ce fichier particulier. Tous les fichiers et répertoires, ainsi que le dossier parent, auront leur propre hachage unique.

```
$ ipfs ls QmaKZ3dnc9ejBdGgEDCRtsLFNRxcY67HLjk6gXUnk9sdM9
```

Cela fonctionne **exactement** comme le système de fichiers UNIX. La sortie attendue affichera ce qui suit :

```
QmSTuTEThyESvDgmYdao2HK6kurXe2pqjA1KHPD8wSHVy7 219859 donut.jpeg
```

```
QmUNLLsPACCz1vLxQVkXqqLX5R1X345qqfHbsf67hvA3Nn 4      folder1/
```

```
QmSR9MJ5resQLjwqy7kEVVKJwTvDG53Npt9i1c6jZeZDtW 110254 purse.jpeg
```

La taille du fichier est indiquée à la fin de la chaîne de hachage. Par exemple, 219859 est la taille du fichier donut.jpeg.

### Étape 4 : Accéder aux fichiers en ligne

Pour accéder aux fichiers en ligne, nous devons d'abord connecter notre nœud au réseau IPFS. Pour ce faire, nous devons lancer le démon (daemon) IPFS.

```
$ ipfs daemon
```

Cela produira la sortie suivante :

```
Initializing daemon...
```

```
Successfully raised file descriptor limit to 2048.
```

```
Swarm listening on /ip4/127.0.0.1/tcp/4001
```

```
Swarm listening on /ip4/169.254.100.132/tcp/4001
```

```
Swarm listening on /ip4/192.168.1.3/tcp/4001
```

```
Swarm listening on /ip6/::1/tcp/4001
```

```
Swarm listening on /p2p-circuit/ipfs/QmTo1oMgGEH6Ym3H1xF55U7q4bexd5288YmEJjubDqVmKn
```

```
Swarm announcing /ip4/127.0.0.1/tcp/4001
```

```
Swarm announcing /ip4/169.254.100.132/tcp/4001
```

```
Swarm announcing /ip4/192.168.1.3/tcp/4001
```

```
Swarm announcing /ip6/::1/tcp/4001
```

```
API server listening on /ip4/127.0.0.1/tcp/5001
```

```
Gateway (readonly) server listening on /ip4/127.0.0.1/tcp/8080
```

```
Daemon is ready
```

Maintenant que vous avez envoyé les fichiers sur l'IPFS, voyons comment vous pouvez y accéder.

```
localhost:8080/ipfs/hashDuFichierQueVousVoulezOuvrir
```

Supposons que je souhaite ouvrir purse.jpeg. Je vais copier le hachage de purse.jpeg et accéder à l'adresse dans le navigateur avec la syntaxe ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/KadAfb5SZMNkJwsx-DuPTFqgTlWwCWQTLcNj)

De même, vous pouvez même écouter votre musique, regarder vos vidéos, et ainsi de suite.

Vous pouvez même accéder à votre contenu en utilisant la passerelle (gateway) IPFS :

```
gateway.ipfs.io/ipfs/hashDuFichier
```

![Image](https://cdn-media-1.freecodecamp.org/images/odk2-x4N9Ae1PD05hO9-695FG6dVTP9wTfuQ)

![Image](https://cdn-media-1.freecodecamp.org/images/GvoWuiYohw98UJYL9EHpEHFU367obEpLsg8Z)

**Vous allez voir de la vraie magie maintenant !**

Pointez votre navigateur vers :

```
127.0.0.1:5001/webui
```

Vous verrez cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/QCO1qZsohtn6LiKPOV3ombnRFCbf-2Sp1lqL)

N'hésitez pas à explorer.

**Connections :** Vous montrera vos pairs partout dans le monde.

![Image](https://cdn-media-1.freecodecamp.org/images/9LrR9rpOaxqh2BAIk4Tm65Of5Hr3dOiWUH7r)
_C'est pas génial, ça !_

**Files :** Vous pouvez envoyer des fichiers en utilisant l'interface Web (webUI).

![Image](https://cdn-media-1.freecodecamp.org/images/azl0Ef-ZLdXN5k9m-FK-ikvKAiUENjGgHY8Z)

**DAG :** Vous montrera le MerkleDAG et affichera les informations relatives au fichier lorsque son hachage est saisi.

![Image](https://cdn-media-1.freecodecamp.org/images/ZYgOHsZByxyGx5SnbCfL1AYJtuXaxX8SV28n)

**Config :** Cela vous montrera les configurations de votre propre machine.

![Image](https://cdn-media-1.freecodecamp.org/images/zkgoHOaUu5GHtvWGHgxkKzPI459R3acpblV3)

### Étape 5 : Accéder aux fichiers de vos pairs

L'IPFS promet qu'il n'y a pas de serveur central qui vous fournit les fichiers. Alors, et si je vous disais que vous pouvez visionner une vidéo depuis mon ordinateur portable même si le démon IPFS ne tourne pas sur mon ordinateur ?

J'ai mis en ligne la vidéo Roar de Katy Perry. Vous pouvez y accéder via mon nœud plutôt que d'aller sur YouTube.

Allez sur :

```
localhost:8080/ipfs/QmWPCbXCK4NGXKac1QoKHdW7Qqud481T5FLHzu7RnSRDGR/
```

Et **profitez-en** !

Vous diffuserez cette vidéo sur l'IPFS.

You pouvez même utiliser VLC Media Player pour cela.

URL utilisée :

```
http://localhost:8080/ipfs/QmWPCbXCK4NGXKac1QoKHdW7Qqud481T5FLHzu7RnSRDGR/Katy%20Perry%20-%20Roar%20%28Official%29.mp4
```

![Image](https://cdn-media-1.freecodecamp.org/images/5qSQK6IMz3JUD5gVYINaK7soOWmMxMPXVSwv)

![Image](https://cdn-media-1.freecodecamp.org/images/kZNXalAycR1zhatzYGMkZzWcViABcSRdN9f7)

N'hésitez pas à expérimenter avec l'IPFS. C'était un aperçu très bref. Mais j'espère que vous avez une idée de base de ce qu'est l'IPFS !