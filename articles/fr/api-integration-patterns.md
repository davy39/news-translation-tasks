---
title: Modèles d'intégration d'API – Les différences entre REST, RPC, GraphQL, Polling,
  WebSockets et WebHooks
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-10-09T15:14:33.000Z'
originalURL: https://freecodecamp.org/news/api-integration-patterns
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/FCC-cover--1-.png
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: REST API
  slug: rest-api
- name: webhooks
  slug: webhooks
- name: websocket
  slug: websocket
seo_title: Modèles d'intégration d'API – Les différences entre REST, RPC, GraphQL,
  Polling, WebSockets et WebHooks
seo_desc: 'API stands for Application Programming Interface. The “I” in API is the
  key part that explains its purpose.

  The interface is what the software presents to other humans or programs, allowing
  them to interact with it.

  A good analogy for an interface is...'
---

API signifie Application Programming Interface. Le « I » dans API est la partie clé qui explique son but.

L'*interface* est ce que le logiciel présente à d'autres humains ou programmes, leur permettant d'interagir avec lui.

Une bonne analogie pour une interface est une télécommande. Imaginez que vous avez une télécommande universelle qui peut contrôler votre TV, vos lumières et votre ventilateur.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28286169-80d5-49f6-b302-65c8cb10fdcb_1762x1070.png align="left")

*Image montrant une télécommande et une TV, un luminaire et un ventilateur.*

Décomposons ce qu'une télécommande universelle peut faire :

1. La télécommande a divers boutons, chacun servant un but différent. Un bouton peut changer de chaîne, tandis qu'un autre peut tamiser les lumières du lustre, et un autre peut allumer le ventilateur.
   
2. Lorsque vous appuyez sur un bouton, il envoie un signal spécifique via infrarouge, bluetooth ou wifi à l'objet que vous contrôlez, lui donnant l'instruction d'effectuer une action particulière.
   
3. L'élément clé de la télécommande est qu'elle vous permet d'interagir avec la TV, le lustre et le ventilateur sans comprendre le fonctionnement interne de ces objets. Toute cette complexité est abstraite pour vous. Vous appuyez simplement sur un bouton, et vous obtenez une réponse que vous pouvez observer immédiatement.
   

Les API fonctionnent de manière similaire.

1. Les API peuvent avoir divers endpoints, chacun conçu pour effectuer une action spécifique. Un endpoint peut récupérer des données, tandis qu'un autre les met à jour ou les supprime.
   
2. Lorsque vous envoyez une requête à un endpoint, il communique avec le serveur en utilisant des méthodes HTTP – GET, POST, PUT, DELETE pour lui donner l'instruction d'effectuer une action particulière (comme récupérer, envoyer, mettre à jour ou supprimer des données).
   
3. L'élément clé des API, comme pour les télécommandes, est que les API abstraient le fonctionnement interne du serveur et de la base de données derrière l'API. L'API permet aux utilisateurs, développeurs et applications d'interagir avec une application logicielle ou une plateforme sans avoir besoin de comprendre son code interne ou sa structure de base de données. Vous envoyez simplement une requête, le serveur la traite et fournit une réponse.
   

Cette analogie n'est valable que jusqu'à un certain point, car les API sont plus complexes qu'une télécommande. Mais les principes de base du fonctionnement entre une API et une télécommande universelle sont assez similaires.

Cet article expliquera les modèles d'intégration d'API, qui peuvent être divisés en deux grands groupes : Request-response (REST, RPC & GraphQL) et les API pilotées par événements (Polling, WebSockets & WebHooks).

## Intégration Request-Response

Dans une intégration request-response, le client initie l'action en envoyant une requête au serveur, puis attend une réponse.

Différents modèles d'intégration request-response existent, mais à un niveau élevé, ils se conforment tous à la même règle : le client initie une requête et attend une réponse du serveur.

### 1. REST

REST signifie Representational State Transfer – l'acronyme est une combinaison des premières lettres de ces trois mots. Il s'agit de la forme la plus simple et la plus populaire d'intégration request-response.

Les API REST utilisent un modèle de communication [stateless](https://lightcloud.substack.com/i/104443280/stateless-architecture), client-serveur, dans lequel chaque message contient toutes les informations nécessaires pour comprendre et traiter le message.

REST est centré sur les ressources. Les ressources sont des entités que l'API expose et qui peuvent être accessibles et manipulées en utilisant des chemins d'URL.

Pour comprendre les API REST, considérons l'analogie suivante. Imaginez que vous entrez dans un restaurant pour commander de la nourriture. Le menu est vaste et les articles sont organisés par catégories. Chaque article du menu peut être assimilé à une ressource.

D'abord, vous appelez le serveur pour attirer son attention, puis vous passez une commande. Chaque requête reçoit une réponse, avant de procéder à une autre requête, comme commander un plat.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F267e1809-4111-43dc-8c6d-aa7bdf764c54_1102x1022.png align="left")

*Analogie de restaurant pour l'API REST*

En termes d'API REST, le client initie des requêtes au serveur en spécifiant exactement ce qu'il veut en utilisant des méthodes HTTP (telles que GET, POST, PUT, DELETE) sur des URL spécifiques (les articles du menu). Chaque interaction est stateless, ce qui signifie que chaque requête du client au serveur doit contenir toutes les informations nécessaires pour comprendre et traiter la requête.

Le serveur traite ensuite la requête et retourne la réponse appropriée – dans notre analogie, en apportant l'article commandé à la table.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd86ab699-f5a2-4c93-9ac8-ee0af83df14d_1174x916.png align="left")

*Diagramme de séquence simple pour l'API REST*

### 2. RPC

RPC signifie Remote Procedure Call. Contrairement aux API REST qui sont centrées sur les ressources, RPC est centré sur les actions. Avec RPC, le client exécute un bloc de code sur le serveur.

Imaginez un restaurant sans menu. Il n'y a pas de plat que vous pouvez demander dans ce restaurant. Au lieu de cela, vous demandez une action spécifique à effectuer par le restaurant.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d9a0ce7-d263-4932-b159-a3234677cf71_1518x926.png align="left")

*Analogie de restaurant pour RPC*

Avec une API REST, le client aurait simplement demandé du poisson et des frites. Avec RPC, il doit donner des instructions sur ce qu'il veut que la cuisine prépare.

Dans le modèle RPC, le client appelle une procédure spécifique sur le serveur et attend le résultat. La procédure de préparation et ce qui est préparé sont étroitement liés. Cela peut donner au client des résultats très spécifiques et sur mesure, mais manque de la flexibilité et de la facilité d'utilisation de REST.

Il y a une raison pour laquelle la plupart des restaurants utilisent des menus, au lieu de suivre les demandes personnalisées de leurs clients. Cela explique en partie pourquoi RPC est un modèle d'intégration moins populaire comparé à REST.

### 3. GraphQL

Avec GraphQL, le client spécifie exactement les données dont il a besoin, ce qui peut inclure des champs spécifiques de diverses ressources. Le serveur traite cette requête, récupère les données exactes et les retourne au client.

Cela permet au client d'avoir un haut degré de flexibilité et de ne récupérer que les données exactes dont il a besoin. Cela nécessite également que le serveur soit capable de gérer des requêtes plus complexes et uniques.

De cette manière, GraphQL est une forme plus personnalisable de REST. Vous traitez toujours avec des ressources (contrairement aux actions dans RPC), mais vous pouvez personnaliser la manière dont vous voulez que la ressource vous soit retournée.

Imaginez un restaurant qui vous permet de personnaliser votre propre plat en spécifiant des quantités exactes ou des ingrédients que vous voulez.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9327807-033d-4e21-b649-0de8e33272bd_1518x858.png align="left")

*Analogie de restaurant pour GraphQL*

Cela peut sembler similaire au modèle RPC, mais notez que le client ne dit pas comment la nourriture doit être préparée, il personnalise simplement sa commande en supprimant certains ingrédients (pas de sel) et en réduisant le nombre de certains articles (deux morceaux de poisson au lieu de quatre).

L'un des inconvénients de GraphQL est qu'il ajoute de la complexité à l'API, car le serveur doit effectuer un traitement supplémentaire pour analyser des requêtes complexes. Cette complexité supplémentaire s'appliquerait également à l'analogie du restaurant, car chaque commande devrait être personnalisée pour le client.

GraphQL a un avantage clair sur REST et RPC. Puisque les clients peuvent spécifier exactement ce dont ils ont besoin, les tailles des charges utiles de réponse sont généralement plus petites, ce qui signifie des temps de réponse plus rapides.

## Intégration pilotée par événements

Ce modèle d'intégration est idéal pour les services avec des données changeant rapidement.

Certains de ces modèles d'intégration sont également [asynchrones](https://lightcloud.substack.com/p/synchronous-and-asynchronous-communication) et initiés par le serveur, contrairement aux modèles request-response qui sont [synchrones](https://lightcloud.substack.com/p/synchronous-and-asynchronous-communication) et initiés par le client.

### 1. Polling

Reprenons l'analogie du restaurant. Lorsque vous commandez de la nourriture, il faudra un certain temps pour qu'elle soit préparée.

Vous pouvez obtenir des mises à jour sur votre commande en demandant au serveur si elle est prête. Plus vous demandez fréquemment, plus vous serez proche d'avoir des informations en temps réel sur votre commande.

Cela, cependant, met une pression inutile sur le serveur, car il doit constamment vérifier l'état de votre commande et vous mettre à jour chaque fois que vous demandez.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F661f8761-5b3e-426f-aa55-fbadc25bd226_892x888.png align="left")

*Analogie de restaurant pour le polling*

Le polling est lorsque le client demande continuellement au serveur s'il y a de nouvelles données disponibles, avec une fréquence définie. Ce n'est pas efficace car de nombreuses requêtes peuvent ne retourner aucune nouvelle donnée, consommant ainsi inutilement des ressources.

Plus vous effectuez de polling (faire des requêtes) fréquemment, plus le client se rapproche de la communication en temps réel avec le serveur.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a8467fc-580f-46e4-b134-7dc3128f044a_1174x954.png align="left")

*Diagramme de séquence simple montrant le polling en action*

La plupart des requêtes pendant le polling sont gaspillées, car elles ne retournent quelque chose d'utile au client qu'une fois qu'il y a un changement sur le serveur.

Il existe cependant une autre version du polling appelée long polling. Avec le long polling, le serveur ne répond pas immédiatement au client sur l'état de la commande. Au lieu de cela, le serveur ne répond que s'il y a une mise à jour.

Naturellement, cela ne fonctionne que si le client et le serveur conviennent au préalable qu'une réponse lente du serveur ne signifie pas que le serveur est impoli et que le client est ignoré.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff76ea285-2629-4aea-8b89-81d500484835_892x888.png align="left")

*Analogie de restaurant pour le long polling*

Avec le long polling, le serveur ne répond pas immédiatement au client. Il attend qu'un changement se produise avant de répondre.

Tant que le client et le serveur conviennent que le serveur conservera la requête du client et que la connexion entre le client et le serveur reste ouverte, ce modèle fonctionne et peut être plus efficace que le simple polling.

Ces deux hypothèses pour le long polling peuvent être irréalistes, cependant – le serveur peut perdre la requête du client et/ou la connexion peut être rompue.

Pour répondre à ces limitations, le long polling ajoute une complexité supplémentaire au processus en nécessitant un répertoire indiquant quel serveur contient la connexion au client, qui est utilisé pour envoyer des données au client dès que le serveur est prêt.

Le polling standard, en revanche, peut rester [stateless](https://lightcloud.substack.com/i/104443280/stateless-architecture), ce qui le rend plus [tolérant aux pannes](https://lightcloud.substack.com/i/59017006/fault-tolerance) et scalable.

### 2. WebSockets

Les WebSockets fournissent un canal de communication persistant et bidirectionnel entre le client et le serveur. Une fois qu'une connexion WebSocket est établie, les deux parties peuvent communiquer librement, ce qui permet des flux de données en temps réel et est plus efficace en ressources que le polling.

En utilisant à nouveau l'analogie du restaurant, un client commande un repas, puis établit un canal de communication dédié avec le serveur afin qu'ils puissent communiquer librement dans les deux sens sur les mises à jour ou les changements de la commande jusqu'à ce que le repas soit prêt. Cela signifie que le serveur peut également initier la communication avec le client, ce qui n'est pas le cas pour les autres modèles d'intégration mentionnés jusqu'à présent.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffebdcac2-f175-4ea1-bd19-1234702def98_892x888.png align="left")

*Analogie de restaurant pour les WebSockets*

Les WebSockets sont similaires au long polling. Ils évitent tous deux les requêtes gaspillées du polling, mais les WebSockets ont l'avantage supplémentaire d'avoir une connexion persistante entre le client et le serveur.

Les WebSockets sont idéaux pour les données de streaming rapides et en direct, comme les applications de chat en temps réel. L'inconvénient des WebSockets est que la connexion persistante consomme de la bande passante, ce qui peut ne pas être idéal pour les applications mobiles ou dans les zones avec une mauvaise connectivité.

### 3. WebHooks

Les WebHooks permettent au serveur de notifier le client lorsqu'il y a de nouvelles données disponibles. Le client enregistre une URL de rappel avec le serveur et le serveur envoie un message à cette URL lorsqu'il y a des données à envoyer.

Avec les WebHooks, le client envoie des requêtes comme d'habitude, mais peut également écouter et recevoir des requêtes comme un serveur.

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d687228-bff2-45d4-a7ac-8ebe2bb07094_1458x954.png align="left")

*Diagramme de séquence simple montrant les WebHooks en action*

En utilisant l'analogie du restaurant, lorsque le client commande un repas, il donne au serveur une cloche (analogue à l'URL de rappel). Le serveur va à la cuisine et sonne la cloche dès que le repas est prêt. Cela permet au client de savoir, en temps réel, l'avancement de sa commande.

Les WebHooks sont supérieurs au polling car vous recevez des mises à jour en temps réel du serveur dès qu'un changement se produit, sans avoir à faire des requêtes fréquentes et gaspillées au serveur concernant ce changement.

Ils sont également supérieurs au long polling car le long polling peut consommer plus de ressources client et serveur, car il implique de garder les connexions ouvertes, ce qui peut entraîner de nombreuses connexions ouvertes.

## Conclusion

En conclusion, les API sont des outils cruciaux dans le développement logiciel, permettant aux utilisateurs et aux applications d'interagir avec un logiciel sans comprendre son fonctionnement interne.

Elles se présentent sous différents modèles d'intégration, tels que REST, RPC, GraphQL, Polling, WebSockets et WebHooks.

Si vous avez besoin d'une intégration request-response simple, alors REST, RPC ou GraphQL pourraient être idéaux. Pour des applications en temps réel ou quasi en temps réel, le polling, les WebSockets ou les WebHooks sont idéaux.

Comme pour tout problème de conception, le bon choix dépend du cas d'affaires et des compromis que vous êtes prêt à tolérer.