---
title: Qu'est-ce que gRPC ? Protocol Buffers, Streaming et Architecture Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-09T21:33:37.000Z'
originalURL: https://freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fa0296d49c47664ed8187bf.jpg
tags:
- name: communication
  slug: communication
- name: performance
  slug: performance
- name: protocol-buffers
  slug: protocol-buffers
- name: software architecture
  slug: software-architecture
seo_title: Qu'est-ce que gRPC ? Protocol Buffers, Streaming et Architecture Expliqués
seo_desc: 'By Pramono Winata

  gRPC is a powerful framework for working with Remote Procedure Calls. RPCs allow
  you to write code as though it will be run on a local computer, even though it may
  be executed on another computer.

  These past few days I have been div...'
---

Par Pramono Winata

gRPC est un framework puissant pour travailler avec les Appels de Procédure à Distance (RPC). Les RPC vous permettent d'écrire du code comme s'il devait être exécuté sur un ordinateur local, même s'il peut être exécuté sur un autre ordinateur.

Ces derniers jours, j'ai plongé profondément dans gRPC. Je vais partager certaines de mes grandes découvertes ici dans cet article.

Notez que je me concentrerai davantage sur les concepts que sur les détails d'implémentation. Vous apprendrez l'architecture centrale de gRPC lui-même. Vous apprendrez également :

* Pourquoi gRPC est si largement utilisé par les développeurs
* Comment il performe si bien
* Et comment tout cela fonctionne sous le capot.

## Revenons un peu en arrière

Avant de nous précipiter dans gRPC, nous devrions examiner ce que sont les **Appels de Procédure à Distance**.

Un RPC est une forme de communication client-serveur qui utilise un appel de fonction plutôt qu'un appel HTTP habituel.

Il utilise IDL (Interface Definition Language) comme forme de contrat sur les fonctions à appeler et sur le type de données.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/operating-system-remote-call-procedure-working.png)
_Architecture RPC_

Si vous ne l'avez pas encore réalisé, le RPC dans gRPC signifie Remote Procedure Call. Et oui, gRPC reproduit ce style architectural de communication client-serveur, via des appels de fonction.

Donc, gRPC n'est pas techniquement un nouveau concept. Il a plutôt été adopté à partir de cette ancienne technique et amélioré, ce qui l'a rendu très populaire en seulement cinq ans.

## Aperçu de gRPC

![Image](https://www.freecodecamp.org/news/content/images/2020/11/index.png)

En 2015, Google a ouvert le code source de leur projet qui fini par être appelé gRPC. Mais que signifie le "g" dans gRPC ?

Beaucoup de gens pourraient penser qu'il signifie Google parce que Google l'a créé, mais ce n'est pas le cas.

Google change la signification du "g" pour chaque version au point où ils ont même créé un [README](https://github.com/grpc/grpc/blob/master/doc/g_stands_for.md) pour lister toutes les significations.

Depuis que gRPC a été introduit, il a gagné beaucoup de popularité et de nombreuses entreprises l'utilisent.

### Qu'est-ce qui rend gRPC si populaire ?

Il y a plusieurs raisons pour lesquelles gRPC est si populaire :

* L'abstraction est facile (c'est un appel de fonction)
* Il est supporté dans de nombreux langages
* Il est très performant
* Les appels HTTP sont souvent confus, donc cela simplifie les choses

Et en plus de toutes les raisons ci-dessus, gRPC est populaire parce que les microservices sont très populaires.

Les microservices exécuteront souvent plusieurs services dans différents langages de programmation. Ils auront également souvent beaucoup d'interactions entre services.

C'est là que gRPC aide le plus en fournissant le support et la capacité de résoudre les problèmes typiques qui surviennent dans ces situations.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/index.jpeg)
_Microservices_

gRPC est très populaire dans les appels de service à service, car souvent les appels HTTP sont plus difficiles à comprendre au premier regard.

Les fonctions gRPC sont beaucoup plus faciles à comprendre, donc les développeurs n'ont pas à s'inquiéter d'écrire beaucoup de documentation car le code lui-même devrait tout expliquer.

Certains des services peuvent également être écrits dans différents langages et gRPC vient avec plusieurs bibliothèques pour supporter cela.

La performance est la cerise sur le gâteau – et c'est une grosse cerise.

## Architecture de gRPC

![Image](https://www.freecodecamp.org/news/content/images/2020/11/landing-2.png)
_L'architecture approximative de gRPC. Elle est plus ou moins la même que celle d'un RPC régulier._

J'ai mentionné plusieurs fois que les performances de gRPC sont très bonnes, mais vous vous demandez peut-être ce qui les rend si bonnes ? Qu'est-ce qui rend gRPC si meilleur que RPC alors que leurs designs sont assez similaires ?

Voici quelques différences clés qui rendent gRPC si performant.

### HTTP/2

HTTP est avec nous depuis longtemps. Maintenant, presque tous les services backend utilisent ce protocole.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/HTTP2-graphic.png)
_Histoire de HTTP_

Comme le montre l'image ci-dessus, HTTP/1.1 est resté pertinent pendant longtemps.

Ensuite, en 2015, HTTP/2 est sorti et a essentiellement remplacé HTTP/1.1 comme protocole de transport le plus populaire sur Internet.

Si vous vous souvenez que 2015 était aussi l'année où gRPC est sorti, ce n'était pas du tout une coïncidence. HTTP/2 a également été créé par Google pour être utilisé par gRPC dans son architecture.

HTTP/2 est l'une des grandes raisons pour lesquelles gRPC peut performer si bien. Et dans la section suivante, vous verrez pourquoi.

### Multiplexage des Requêtes/Réponses

Dans un protocole HTTP traditionnel, il n'est pas possible d'envoyer plusieurs requêtes ou d'obtenir plusieurs réponses ensemble dans une seule connexion. Une nouvelle connexion devra être créée pour chacune d'elles.

Ce type de multiplexage des requêtes/réponses est rendu possible dans HTTP/2 avec l'introduction d'une nouvelle couche HTTP/2 appelée binary framing.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-from-2020-10-03-15-46-01.png)

Cette couche binaire encapsule et encode les données. Dans cette couche, la requête/réponse HTTP est décomposée en trames.

La trame d'en-tête contient les informations typiques des en-têtes HTTP, et la trame de données contient la charge utile. En utilisant ce mécanisme, il est possible d'avoir des données de plusieurs requêtes dans une seule connexion.

Cela permet des charges utiles de plusieurs requêtes avec le même en-tête, identifiant ainsi une seule requête.

### Compression des En-têtes

Vous avez peut-être rencontré de nombreux cas où les en-têtes HTTP sont même plus gros que la charge utile. Et HTTP/2 a une stratégie très intéressante appelée HPack pour gérer cela.

Pour commencer, tout dans HTTP/2 est encodé avant d'être envoyé, y compris les en-têtes. Cela aide à la performance, mais ce n'est pas la chose la plus importante à propos de la compression des en-têtes.

HTTP/2 mappe l'en-tête à la fois du côté client et du côté serveur. À partir de cela, HTTP/2 est capable de savoir si l'en-tête contient la même valeur et n'envoie la valeur de l'en-tête que si elle est différente de l'en-tête précédent.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/Screenshot-from-2020-11-04-22-32-12-1.png)

Comme on peut le voir dans l'image ci-dessus, la Requête #2 n'enverra que le chemin puisque les autres valeurs sont exactement les mêmes. Et oui, cela réduit beaucoup la taille de la charge utile, et à son tour, améliore encore plus les performances de HTTP/2.

### Protocol Buffer, alias Protobuf

![Image](https://www.freecodecamp.org/news/content/images/2020/11/protobuf.png)
_Protocol Buffer_

Protobuf est l'IDL (Interface Definition Language) le plus couramment utilisé pour gRPC. C'est là que vous stockez essentiellement vos données et vos contrats de fonction sous la forme d'un fichier proto.

```proto
message Person {
    required string name = 1;
    required int32 id = 2;
    optional string email = 3;
}
```

Puisque cela est sous la forme d'un contrat, à la fois le client et le serveur doivent avoir le même fichier proto. Le fichier proto agit comme le contrat intermédiaire pour que le client appelle toute fonction disponible du serveur.

Protobuf a également ses propres mécanismes, contrairement à une API REST habituelle qui envoie simplement des chaînes de JSON sous forme de bytes. Ces mécanismes permettent à la charge utile d'être beaucoup plus petite et permettent des performances plus rapides.

La méthode d'encodage utilisée par Protobuf est assez compliquée. Si vous voulez plonger profondément dans son fonctionnement, consultez cette [documentation complète](https://developers.google.com/protocol-buffers/docs/encoding).

## Que propose d'autre gRPC ?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-257.png)
_Photo par [Unsplash](https://unsplash.com/@kyledevaras?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Kyle Gregory Devaras</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Maintenant, vous devriez avoir une compréhension de base de l'architecture de gRPC, de son fonctionnement et de ses capacités.

Mais voici quelques autres choses intéressantes que gRPC nous offre.

### Métadonnées

Au lieu d'utiliser un en-tête de requête HTTP habituel, gRPC a quelque chose appelé métadonnées. Les métadonnées sont un type de données clé-valeur qui peuvent être définies à partir du client ou du serveur.

`Header` peut être assigné du côté client, tandis que les serveurs peuvent assigner `Header` et `Trailers` tant qu'ils sont tous deux sous forme de métadonnées.

### Streaming

Le streaming est l'un des concepts clés de gRPC où plusieurs choses peuvent se produire dans une seule requête. Cela est rendu possible par la capacité de multiplexage de HTTP/2 mentionnée précédemment.

Il existe plusieurs types de streaming :

* **Server Streaming RPC** : Où le client envoie une seule requête et le serveur peut envoyer plusieurs réponses. Par exemple, lorsque le client envoie une requête pour une page d'accueil qui contient une liste de plusieurs éléments, le serveur peut envoyer des réponses séparément, permettant au client d'utiliser le chargement paresseux.
* **Client Streaming RPC** : Où le client envoie plusieurs requêtes et le serveur n'envoie qu'une seule réponse. Par exemple, un fichier zip/chunk téléchargé par le client.
* **Bidirectional Streaming RPC** : Où le client et le serveur s'envoient des messages mutuellement en même temps sans attendre de réponse.

### Intercepteurs

gRPC supporte l'utilisation d'intercepteurs pour ses requêtes/réponses. Les intercepteurs, eh bien, interceptent les messages et vous permettent de les modifier.

Cela vous semble familier ? Si vous avez joué avec des processus HTTP sur une API REST, les intercepteurs sont très similaires aux middlewares.

Les bibliothèques gRPC supportent généralement les intercepteurs et permettent une implémentation facile. Les intercepteurs sont généralement utilisés pour :

* Modifier la requête/réponse avant qu'elle ne soit transmise. Il peut être utilisé pour fournir des informations obligatoires avant d'être envoyé au client/serveur.
* Vous permettre de manipuler chaque appel de fonction tel que l'ajout de journalisation supplémentaire pour suivre le temps de réponse.

### Équilibrage de Charge

Si vous n'êtes pas déjà familier avec l'équilibrage de charge, c'est un mécanisme qui permet de répartir les requêtes des clients sur plusieurs serveurs.

Mais l'équilibrage de charge est généralement effectué au niveau du proxy (par exemple, NGINX). Alors pourquoi en parler ici ?

Il s'avère que gRPC supporte une méthode d'équilibrage de charge par le client. Elle est déjà implémentée dans la bibliothèque Golang et peut être utilisée avec facilité.

Bien que cela puisse sembler une sorte de magie folle, ce n'en est pas. Il y a une sorte de résolution DNS pour obtenir une liste d'IP et un algorithme d'équilibrage de charge sous le capot.

### Annulation d'Appel

Les clients gRPC sont capables d'annuler un appel gRPC lorsqu'ils n'ont plus besoin de réponse. Le rollback du côté serveur n'est pas possible, cependant.

Cette fonctionnalité est particulièrement utile pour le streaming côté serveur où plusieurs requêtes serveur peuvent arriver. La bibliothèque gRPC est équipée d'un motif de méthode observateur pour savoir si une requête est annulée et permettre d'annuler plusieurs requêtes correspondantes à la fois.

## Conclusion

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-258.png)
_Photo par [Unsplash](https://unsplash.com/@rcrazy?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Ricardo Rocha</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Tout ce que j'ai partagé aujourd'hui ne fait qu'effleurer la surface de ce qu'est gRPC, de ce dont il est capable et de son fonctionnement approximatif.

J'espère vraiment que cet article vous a aidé à comprendre davantage sur gRPC. Mais il y a encore beaucoup plus à apprendre, alors ne vous arrêtez pas ici ! Continuez à creuser.

Merci d'avoir lu !