---
title: 'MISE À JOUR : Améliorez Votre Projet Bluetooth Avec Cet Outil Précieux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T15:05:54.000Z'
originalURL: https://freecodecamp.org/news/improve-your-bluetooth-project-with-this-valueable-tool
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/protobuf.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: protocol-buffers
  slug: protocol-buffers
seo_title: 'MISE À JOUR : Améliorez Votre Projet Bluetooth Avec Cet Outil Précieux'
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  One of the most confusing things about Bluetooth Low Energy is how data is moved
  around. Depending on your application, your device state may be fairly complex.
  That means having an indiv...'
---

Par Jared Wolff

**Cet article provient à l'origine de [www.jaredwolff.com](https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf/)**

L'une des choses les plus déroutantes à propos de Bluetooth Low Energy est la manière dont les données sont transférées. Selon votre application, l'état de votre appareil peut être assez complexe. Cela signifie que disposer d'un point de terminaison individuel pour chaque morceau de données est un suicide par Bluetooth.

Alors, quelle est la solution ?

[Protocol Buffers.](https://developers.google.com/protocol-buffers/)

Un protocol buffer est une méthode programmatique pour encoder/décoder des données structurées optimisées. Ils peuvent être partagés et manipulés sur presque toutes les plateformes. Nordic utilise en fait une variante de celui-ci pour leur service DFU.

Il y avait beaucoup de mots à la mode dans les premières phrases. Espérons qu'à la fin de cet article, vous comprendrez exactement de quoi je parle.

Dans ce tutoriel, j'inclurai un exemple de code entièrement développé que vous pouvez cloner et commencer à utiliser immédiatement. Tout ce dont vous avez besoin est l'un de ceux-ci :

![Kit de Développement NRF52](https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf/images/DSC01544.jpg)

Alors, comment utilisez-vous ce logiciel magique ?

Lisez la suite !

P.S. cet article est long. Si vous voulez quelque chose à télécharger, [cliquez ici pour un PDF magnifiquement formaté.](https://www.jaredwolff.com/files/how-to-define-a-protocol-buffer-ble-service-pdf/) (Bonus supplémentaire, le PDF contient les trois parties de cette série !)


## Installation
La première partie du processus consiste à s'assurer que vous avez installé tous les utilitaires corrects. Selon le langage de programmation que vous utilisez, cela déterminera ce que vous installez et utilisez. Dans ce cas, je vais décrire les utilitaires que j'ai utilisés pour plusieurs projets dans le passé en utilisant C, Go et Javascript.

`protoc` est l'utilitaire le plus important que vous devrez installer ici. C'est le "compilateur" Protobuf qui prend vos fichiers `.proto` et `.options` et les transforme en code statique.

1. Pour Mac, téléchargez la version appropriée [ici](https://github.com/google/protobuf/releases).
2. Décompressez le dossier
3. Exécutez `./autogen.sh && ./configure && make` dans le dossier
4. Si vous obtenez une erreur `autoreconf: failed to run aclocal: No such file or directory`, installez `autoconf` en utilisant Homebrew :

`brew install autoconf && brew install automake`

Puis, relancez l'étape 3.
1. Ensuite, exécutez :

```
make check
sudo make install
which protoc
```

Considérez `protoc` comme le compilateur pour Protocol Buffers. Il peut soit produire des fichiers bruts, soit des bibliothèques directement. C'est parce qu'il a un support Go intégré.

Ces données brutes peuvent également être utilisées pour générer des bibliothèques statiques pour d'autres langages. Cela nécessite généralement un utilitaire supplémentaire (ou des utilitaires). Je décris les deux que le projet Dondi Lib a utilisés ci-dessous.

2. `nanopb` est un script Python utilisé pour créer des bibliothèques C qui encodent/décodent vos données structurées.
  Il peut être installé en naviguant vers le [dépôt git nanopb](https://github.com/nanopb/nanopb) et en téléchargeant les fichiers appropriés. Les pièces les plus importantes à inclure :

1. `pb_encode.c`, `pb_decode.c` et `pb_common.c`
2. `/generator/nanopb_generator.py`
3. Et le répertoire `/generator/nanopb/` co-localisé avec `nanopb_generator.py`

    `nanopb` est destiné au déploiement sur des plateformes embarquées. Il est différent de `protoc-c` (la variante C régulière) car il est optimisé pour les systèmes à ressources limitées comme les processeurs embarqués. Les tampons ont des tailles finies. Il n'y a pas d'allocation de mémoire ! Selon qu'il y ait une communication bidirectionnelle, vous ne pouvez importer et utiliser que la fonctionnalité d'encodage ou de décodage.

4. `pbjs` utilise la sortie de `protoc` pour générer une bibliothèque JavaScript statique. Cela est puissant car vous pouvez ensuite l'utiliser dans n'importe quelle application JavaScript. La meilleure façon d'installer `pbjs` est d'exécuter :

      ```
      npm install -g protobufjs
      ```

J'ai simplifié un peu cette étape dans l'exemple de code. [Commencez par cloner les dépôts ici.](https://www.jaredwolff.com/files/protobuf/)

## Configuration du Protocol Buffer

Créez un fichier appelé `command.proto`. Vous pouvez faire en sorte que le contenu de ce fichier soit ce qui suit :

```
syntax = "proto3";

message event {
  enum event_type {
    command = 0;
    response = 1;
  }
  event_type type = 1;
  string message = 2;
}
```

Cela peut sembler étrange au premier abord, mais une fois que vous regardez de plus près, ce n'est pas si différent d'une structure C standard ou d'une table de hachage.

J'utilise deux types de données dans cet exemple : une `string` et un `enum` comme type. Il y en a en fait quelques autres que vous pouvez lire dans la [documentation](https://developers.google.com/protocol-buffers/docs/proto). Une fois compilé, la structure C équivalente ressemble à :

```
/* Définitions de structure */
typedef struct _event {
    event_event_type type;
    char message[64];
/* @@protoc_insertion_point(struct:event) */
} event;
```

Où `event_event_type` est

```
/* Définitions d'énumération */
typedef enum _event_event_type {
    event_event_type_command = 0,
    event_event_type_response = 1
} event_event_type;
```

Vous pouvez imbriquer autant de messages les uns dans les autres que vous le souhaitez. Cependant, généralement, un message est aussi petit que possible pour que la transmission des données soit aussi efficace que possible. Cela est particulièrement important pour les systèmes à ressources limitées ou les déploiements LTE où vous êtes facturé pour *chaque* mégaoctet utilisé. **Note :** lorsque les éléments ne sont pas utilisés ou définis, ils ne sont généralement *pas* inclus dans la charge utile du Protocol Buffer encodé.

Normalement, lorsque vous créez un message générique comme celui-ci, il n'y a pas de limite à la taille de la chaîne `message`. Cette option peut être définie dans le fichier `.options` :

```
event.message	max_size:64
```

De cette façon, la mémoire peut être allouée statiquement dans mon code de microprocesseur au moment de la compilation. Si la taille du message est supérieure à 64 octets, il sera tronqué dans le code (ou vous obtiendrez simplement une erreur lors du décodage). C'est à vous, l'ingénieur logiciel, de déterminer la quantité absolue maximale d'octets (ou de caractères) dont vous pourriez avoir besoin pour ce type de données.

Vous pouvez consulter plus de fonctionnalités liées à `nanopb` dans [leur documentation](https://jpa.kapsi.fi/nanopb/docs/concepts.html).

## Génération des bibliothèques statiques appropriées
Afin de rendre cela aussi simple que possible, j'ai mis tout le code suivant dans un Makefile. Lorsque vous apportez une modification au Protocol Buffer, chaque bibliothèque pour chaque langage utilisé est générée.

Si nous voulons générer un fichier Go statique, la commande ressemble à ceci :

```bash
protoc -I<répertoire avec .proto> --go_out=<répertoire de sortie> command.proto
```

Si vous avez installé le plugin nanopb, vous pouvez faire quelque chose de similaire pour générer du code C :

```bash
protoc -I<répertoire avec .proto> -ocommand.pb command.proto
<chemin>/<vers>/protogen/nanopb_generator.py -I<répertoire avec .proto> command
```

Le premier fichier crée un fichier "objet" générique. Le second crée en fait la bibliothèque C statique.

Pour JavaScript :

```bash
pbjs -t static-module -p<répertoire avec .proto> command.proto > command.pb.js
```

Vous pouvez tester chacune de ces commandes avec les exemples de fichiers `.proto` et `.options` ci-dessus. J'ai également intégré ce processus manuel en une seule commande dans le dépôt d'exemple. [Obtenez l'accès ici.](https://www.jaredwolff.com/files/protobuf/)

## Encodage et Décodage

![Encodage](https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf/images/data-3432628_1920.jpg)

Dans les exemples ci-dessous, je vous montre comment utiliser votre code statique fraîchement compilé ! C'est là que le plaisir commence.

### Encodage en utilisant JavaScript
Voici un flux typique que vous pouvez suivre lorsque vous utilisez une bibliothèque JavaScript générée statiquement. Tout d'abord, initialisez la bibliothèque.

```
// Importer le message de configuration
var protobuf  = require('./command.pb.js');
```

Ensuite, créez une instance de `event` :

```
// configurer la commande
var event = protobuf.event.create();
event.type = protobuf.event.event_type.command;
event.message = "Ceci est";
```

Ensuite, compilez la charge utile. c'est-à-dire, transformez le JSON lisible par l'homme en binaire bien emballé. Voir ci-dessous.

```
// assurez-vous qu'il est valide
var err = protobuf.event.verify(event);
if( err != null ) {
   console.log("vérification échouée : " + err);
   return;
}
```

Vous obtiendrez des erreurs lors de cette étape si votre objet est mal formé ou si des éléments `requis` sont manquants. Je ne recommande pas d'utiliser le préfixe `required` lors de la définition de votre fichier `.proto`. Toute vérification des éléments requis peut être facilement effectuée dans votre code d'application.

Enfin, la dernière étape consiste à encoder et à le transformer en octets bruts :

```
// encoder en octets bruts
var payload = protobuf.event.encode(event).finish();
```

Vous pouvez ensuite utiliser la charge utile et l'envoyer via BLE, HTTP ou autre. Si un protocole de communication existe, vous pouvez envoyer ce tampon via celui-ci !

### Décodage en C
Une fois les données reçues, elles sont décodées à l'extrémité embarquée. `nanopb` est déroutant. Mais heureusement, j'ai ici un code qui fonctionnera pour vous :

```
// Configuration des données du protocol buffer
event evt;

// Lire le tampon
pb_istream_t istream = pb_istream_from_buffer((pb_byte_t *)data, data_len);

if (!pb_decode(&istream, event_fields, &evt)) {
   NRF_LOG_ERROR("Impossible de décoder : %s", PB_GET_ERROR(&istream));
   return;
}

// Valider le code et le type
if( evt.type != event_event_type_command ) {
   return;
}
```

Tout d'abord, vous créez un flux d'entrée basé sur les données brutes et la taille des données.

Ensuite, vous utilisez la fonction `pb_decode`. Vous pointez le premier argument vers le flux d'entrée. Le second vers la définition de notre Protocol Buffer avec lequel nous avons travaillé. Il se trouve dans le fichier `command.pb.h`.

```
/* Définitions pour la compatibilité ascendante avec le code écrit avant nanopb-0.4.0 */
#define event_fields &event_msg
```

Le dernier argument est un pointeur vers la structure pour mettre les données décodées. (Dans ce cas, il s'agit de `evt` défini juste avant `pb_istream_from_buffer` ci-dessus).

### Encodage en C

Disons maintenant que nous allons répondre au message qui vient d'être décodé ci-dessus. Nous devons donc maintenant créer des données, les encoder et les renvoyer. Voici le processus :

```
// Encoder la valeur
pb_byte_t output[event_size];

// Tampon de sortie
pb_ostream_t ostream = pb_ostream_from_buffer(output,sizeof(output));

if (!pb_encode(&ostream, event_fields, &evt)) {
   NRF_LOG_ERROR("Impossible d'encoder : %s", PB_GET_ERROR(&ostream));
   return;
}
```

Tout d'abord, créez un tampon qui contient la quantité maximale d'octets que votre Protocol Buffer occupe. Cela est également défini dans votre `command.pb.h`. Dans ce cas, `event_size` est défini à `67`. Ensuite, de manière similaire à la commande de décodage, vous créez un flux et le connectez à votre tampon. Enfin, encodez les données en pointant votre structure `evt` ainsi que le flux et `event_fields`.

Tant que `pb_encode` retourne sans erreur, les données encodées ont été écrites dans `output` ! La structure peut être de longueur variable, donc la meilleure façon de la gérer lors de l'envoi est d'obtenir les `bytes_written` de `ostream` :

```
NRF_LOG_INFO("octets écrits %d",ostream.bytes_written);
```

## Conclusion

Bien joué, vous avez réussi ! J'espère que vous commencez à saisir la puissance des Protocol Buffers. Ne vous inquiétez pas, il m'a fallu un certain temps pour tout comprendre. *Vous aussi pouvez devenir un maître des Protocol Buffers !* 💡

Si vous n'êtes pas trop enthousiaste à propos des Protocol Buffers, il existe d'autres alternatives. J'ai utilisé [MessagePack](https://msgpack.org) avec un certain succès sur des produits précédents. C'est simple et dispose d'un support pour la majorité des langages de programmation.

Si vous êtes intéressé par la manière d'intégrer cela dans un projet Bluetooth Low Energy, restez à l'écoute pour la Partie Deux. Dans la Partie Deux, je vous montrerai comment configurer un Service Bluetooth et une Caractéristique très simples qui seront utilisés pour transférer nos données fraîchement encodées dans les deux sens.

De plus, si vous voulez voir tout le code en action, [vous pouvez tout télécharger ici.](https://www.jaredwolff.com/files/protobuf/)