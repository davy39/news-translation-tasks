---
title: Comment fonctionnent les files d'attente de messages dans les systèmes distribués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-16T15:54:17.000Z'
originalURL: https://freecodecamp.org/news/message-queues-in-distributed-systesms
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover2.png
tags:
- name: distributed systems
  slug: distributed-systems
- name: Microservices
  slug: microservices
seo_title: Comment fonctionnent les files d'attente de messages dans les systèmes
  distribués
seo_desc: 'By Nyior Clement

  From town criers to written letters and now real-time chat applications, humanity
  has always been on the lookout for innovative ways to communicate. And we can say
  the same about computers.

  There''s an even greater need to allow compu...'
---

Par Nyior Clement

Des crieurs publics aux lettres écrites et maintenant aux applications de chat en temps réel, l'humanité a toujours été à la recherche de moyens innovants pour communiquer. Et nous pouvons en dire autant des ordinateurs.

Il y a un besoin encore plus grand de permettre aux ordinateurs de communiquer avec l'adoption croissante de l'architecture distribuée. Cela signifie également que la coordination et la gestion de la communication entre les services plus petits sont devenues plus complexes.

Mais différentes façons de permettre aux services dans une architecture distribuée de communiquer ont évolué au fil des ans. Nous pouvons classer ces différents modèles de communication en deux grandes catégories : les modes de communication **synchrones** et **asynchrones**.

Mais plus pertinent pour cet article serait d'explorer comment nous pouvons utiliser les files d'attente de messages pour implémenter une communication asynchrone dans un système distribué. Et, plus important encore, comment cela peut nous aider à réaliser une architecture plus fiable et évolutive.

Synchrone, asynchrone, files d'attente de messages, systèmes distribués — que sont tous ces termes ?

Cet article couvrira ce qu'ils sont et, plus important encore, explorera le lien entre les files d'attente de messages et les systèmes distribués. Pour commencer, examinons l'évolution des monolithes aux systèmes distribués.

**Note :** pour des raisons de brièveté, cet article utilisera indifféremment les termes systèmes distribués et microservices.

## **L'Ère des Monolithes**

Dans les premiers jours, les systèmes logiciels étaient relativement simples et petits. En conséquence, ils étaient développés et déployés en tant qu'unité fonctionnant sur un seul processus.

Par exemple, imaginons que vous travailliez sur une application qui gère l'authentification, traite les commandes et, finalement, gère les paiements. Vous regrouperiez tous ces composants, ainsi que la base de données de l'application, en une unité étroitement couplée qui est déployée en tant qu'une seule application — un **monolithe**.

![Image](https://lh6.googleusercontent.com/7-CANvceX1yRkuEpUUYcxk5SGteo3sAIfV_bsa-h-9ri6C2uWzAK6VNYGChTlQ0aY4ZIXWzh1GvU-kJED9xnpvgGp8MaUCeO4i6yPqBzXONREgaDoWcJkhpEnc5gSSSpL8N86Y7E-B6QwsxShWVoF-A)
_Illustration d'un style d'architecture monolithique_

Avec le temps, alors que de plus en plus de personnes adoptaient l'internet, ces applications monolithiques ont commencé à connaître une explosion du nombre de leurs utilisateurs — une bonne chose, n'est-ce pas ? Mais cela a révélé certaines limitations de l'architecture monolithique.

### Limitations de l'architecture monolithique

Tout d'abord, avec l'augmentation du nombre d'utilisateurs, les développeurs ont réalisé que le fait d'avoir une application et sa base de données hébergées sur la même machine n'était pas idéal. La base de données est rapidement devenue un gouffre de ressources, consommant la mémoire et la puissance de calcul du serveur.

Pour résoudre cela, les développeurs ont pensé qu'il serait judicieux que l'application et sa base de données puissent être hébergées sur des machines différentes.

![Image](https://lh3.googleusercontent.com/ZjQ6LeuuOS9rgMGhQKdHQfUG20K4k-83F80ziIqNUTaMFZ4Bk90vdXB5PY0_qhEEeiQMmfoe8js-yjX9FfA7IrRg6txGCgXvkbTt-BwgLXpVSgqQsAUw3KdIpkKc9d7Uoe3OO1E1huLcKEMEjhghTk0)
_Une application monolithique avec une base de données séparée_

Même avec cela, ils ont remarqué que le simple déplacement de la base de données vers une machine séparée n'était pas suffisant. À mesure que davantage d'utilisateurs utilisaient une application, la demande en ressources de calcul de la machine hôte augmentait également.

Alors que les utilisateurs interagissaient de plus en plus avec une application, les développeurs ont réalisé que la machine hôte était poussée à sa limite. Cela affectait négativement la rapidité avec laquelle l'application monolithique pouvait servir une requête utilisateur. Ce problème de latence s'aggravait avec l'augmentation du trafic utilisateur.

Pour corriger cela, ils ont adopté un nouveau design.

### L'architecture monolithique répliquée

Dans ce modèle de conception, la même application monolithique est dupliquée sur plusieurs serveurs — avec tous les serveurs cachés derrière un équilibreur de charge. Chacun des monolithes se connectait à la même base de données, et l'équilibreur de charge routait les requêtes vers ces instances de manière optimale afin de ne pas surcharger l'une des instances.

![Image](https://lh6.googleusercontent.com/g12JwG6ejwR-w1V5gU6UZJKvxRKLCnMozMyJst-MOMkewRGw1jTfwmgUKRqHKmENV2ShLTH2JPO3sOjYdlTPNrYP2ibam-2WUOX1hPcL4q77-kiUUuloJTzhH5GMPcBFXJz_C_RAcxrwbFWMBH_98XU)
_Architecture monolithique répliquée_

La réplication d'un monolithe sur plusieurs machines a amélioré les performances, mais à quel prix ?

Apporter des modifications à un monolithe exécutant une architecture répliquée est devenu une entreprise qui avait toutes les caractéristiques d'un cauchemar. Passons en revue certains de ces inconvénients.

### Les pièges de l'architecture monolithique répliquée

Certaines des limitations du monolithe répliqué sont, sans s'y limiter :

**1. Difficulté de mise à niveau ou de maintenance :** Par exemple, imaginez que vous deviez mettre à jour la manière dont votre application traitait les paiements — peut-être passer à un autre processeur de paiement. Des mises à jour comme celle-ci devraient être reflétées sur tous les monolithes répliqués.

Essentiellement, toutes les copies devraient être arrêtées, mises à jour, testées, puis redéployées. Globalement, l'introduction de changements ou la maintenance d'un monolithe, en général, est beaucoup plus difficile qu'elle ne devrait l'être, car tous les composants sont étroitement couplés.

**2. Mise à l'échelle horizontale inefficace :** Au-delà de la maintenance et des mises à niveau, oui, la mise à l'échelle horizontale d'un monolithe en créant des instances dupliquées peut améliorer les performances — mais la manière dont la mise à l'échelle est effectuée dans ce cas n'est pas optimale. Voyons pourquoi...

Rappelons qu'un monolithe est un ensemble de différents composants qui font différentes choses mais fonctionnent comme un seul processus. En reprenant notre exemple précédent, disons que notre monolithe a des composants d'authentification, de traitement des commandes et de paiement.

Maintenant, dans un monolithe, il est courant d'avoir certains composants qui font plus de travail (reçoivent et traitent les requêtes utilisateur) que d'autres. Par exemple, dans notre cas, tous les utilisateurs qui se connectent ou s'inscrivent ne passeront pas une commande ou ne paieront pas une commande.

Même si, dans notre cas, nous savons que c'est le composant d'authentification auquel nous devons allouer plus de ressources pour mettre à l'échelle, nous ne pouvons pas. Cela est dû au fait que tous les composants sont liés les uns aux autres et fonctionnent comme une seule unité, donc nous ne pouvons pas simplement extraire le composant d'authentification.

C'est pourquoi, pour mettre à l'échelle un monolithe horizontalement, nous devrions créer une instance dupliquée de l'ensemble de l'application plutôt que de mettre à l'échelle uniquement les composants pertinents. Cela, à son tour, entraîne une pression inutile qui pourrait être évitée sur les ressources informatiques de la machine hôte.

### Un récapitulatif des limitations de l'architecture monolithique en général

Enfin, parce que tous les composants dans un monolithe sont étroitement couplés, si un composant est défectueux, cela affectera directement la disponibilité des autres parties. Clairement, avec les monolithes, nous obtenons des systèmes fragiles.

En résumé, les applications monolithiques ont les limitations suivantes :

* Il est difficile d'introduire de nouveaux changements dans un monolithe, ainsi que de le maintenir et de le mettre à niveau au fil du temps
* La mise à l'échelle d'une application monolithique n'est généralement pas optimale
* Les applications monolithiques ne sont pas résilientes — si une partie du système tombe en panne, l'ensemble du système tombe en panne

Le désir de créer une architecture logicielle qui surmonte les inconvénients du monolithe a donné naissance à l'ère des microservices.

## **Qu'est-ce qu'un Microservice ?**

Eh bien, accablés par les limitations flagrantes du monolithe, les développeurs sont devenus analytiques et sont retournés à la vue d'ensemble. Ils se sont dit, et si nous développons les composants étroitement couplés du monolithe en tant que composants indépendants faiblement couplés ?

Cette réflexion a donné naissance à ce que nous appelons maintenant l'architecture de microservices. Contrairement à l'architecture monolithique, l'architecture de microservices décompose une application en composants plus petits et autonomes appelés services.

Chaque service est développé et déployé séparément. En conséquence, chaque service fonctionne sur un processus séparé.

En reprenant notre exemple précédent, notre monolithe sera décomposé en trois services : le service d'authentification, le service de traitement des commandes et le service de traitement des paiements, comme illustré dans l'image ci-dessous.

![Image](https://lh6.googleusercontent.com/d07AC1RCi4ek6UquoIXVNQpcf5AFMsFJFZ0eT0UPZqSO8xpWowZLAikqAMg9C09spsgC-5HvzIIKEVagVlYaal_TdpDfb3yQxbdcoqG4IA29-0aM_U7FI8jEKRYrAiEVWRGAysyad04clYkZNr3M_QE)
_Une architecture de microservices_

Même si ces services sont maintenant développés en tant que composants autonomes, ils travaillent tous ensemble et communiquent pour atteindre un objectif commun — garantir que les utilisateurs authentifiés peuvent effectuer des achats et payer.

Mais cela soulève la question : comment ces services communiquent-ils entre eux ?

### Modèles de communication dans une architecture de microservices

De manière générale, les services dans l'architecture de microservices peuvent être configurés pour communiquer de l'une des deux manières suivantes : **de manière synchrone** ou **asynchrone**.

Pour comprendre ces deux modèles de communication, poursuivons notre exemple précédent — imaginons un scénario où le **service de traitement des commandes** doit envoyer les détails d'une nouvelle commande au **service de traitement des paiements** pour que le paiement soit traité.

#### Communication synchrone

Supposons que la communication entre les deux services soit synchrone. Dans ce cas, le service de traitement des commandes effectuera un appel API au service de traitement des paiements, puis attendra une réponse de ce service avant de continuer son processus.

En conséquence, le service de traitement des commandes est bloqué jusqu'à ce qu'il reçoive la réponse à sa requête. Bien que le modèle de communication synchrone soit simple et direct, il présente certains défauts majeurs lorsqu'il est utilisé dans une architecture de microservices.

L'un des objectifs des microservices est de créer de petits services indépendants qui restent opérationnels même si un ou plusieurs services connaissent des temps d'arrêt. Cela aide à éliminer les points de défaillance uniques.

Cependant, le fait que le service de traitement des commandes doive attendre sans rien faire une réponse du service de paiement crée un niveau d'interdépendance qui nuit à l'autonomie prévue de chaque service.

Cela pose problème car :

* Si le service de traitement des paiements connaît une défaillance inattendue, le service de traitement des commandes ne pourrait pas satisfaire ses requêtes.
* Si le service de traitement des commandes rencontre une augmentation soudaine du trafic, cela affecterait également le service de paiement car il transmet directement ses requêtes au service de paiement.
* Si le service de paiement met trop de temps à répondre, le service de traitement des commandes mettra également très longtemps à envoyer une réponse à l'utilisateur final.

Comment ces problèmes peuvent-ils être résolus ? La communication asynchrone à la rescousse.

#### Communication asynchrone

Supposons que la communication entre les deux services soit asynchrone. Dans ce cas, le service de traitement des commandes initiéra une requête au service de paiement et continuera son exécution sans attendre de réponse. Au lieu de cela, il reçoit la réponse à un moment ultérieur.

Pour la communication asynchrone, plusieurs modèles sont disponibles tels que la publication/abonnements, la mise en file d'attente de messages et l'architecture pilotée par événements.

Ici, nous nous intéressons à voir comment la communication asynchrone peut être implémentée dans les microservices avec des files d'attente de messages.

## **Qu'est-ce qu'une File d'Attente de Messages ?**

Une file d'attente de messages est fondamentalement toute technologie qui agit comme un tampon de messages — elle accepte les messages et les aligne dans l'ordre où ils arrivent. Lorsque ces messages doivent être traités, ils sont à nouveau retirés dans l'ordre où ils arrivent.

Un message est toute donnée ou instruction ajoutée à la file d'attente de messages. En reprenant notre exemple, un message serait les détails d'une commande qui pourraient être ajoutés à la file d'attente de messages puis traités plus tard par le service de paiement.

L'architecture d'une file d'attente de messages est simple — les applications appelées **producteurs** créent des messages et les ajoutent à la file d'attente de messages. D'autres applications appelées **consommateurs** récupèrent ces messages et les traitent. Certains exemples de files d'attente de messages sont [Apache Kafka](https://kafka.apache.org/), [RabbitMQ](https://www.rabbitmq.com/), et [LavinMQ](https://lavinmq.com/), parmi d'autres.

Nous pouvons généralement utiliser une file d'attente de messages pour permettre aux services au sein d'un microservice de communiquer de manière asynchrone. Mais comment, pourriez-vous demander ?

### **Communication asynchrone dans les systèmes distribués avec des files d'attente de messages**

Pour démontrer comment une file d'attente de messages peut favoriser la communication asynchrone dans une architecture de microservices, revenons à l'exemple que nous avons répété dans cet article.

Rappelons que nous avons mentionné que le **service de traitement des commandes** pouvait transmettre les détails des nouvelles commandes au **service de traitement des paiements** de manière synchrone via un appel API. Nous pouvons remplacer l'API synchrone par une file d'attente de messages.

En essence, la file d'attente de messages se situera entre les deux services. Dans cette configuration, le **service de traitement des commandes** agira en tant que producteur qui produit et ajoute des messages à la file d'attente de messages. Le **service de traitement des paiements** agira ensuite en tant que consommateur qui traite les messages ajoutés à la file d'attente.

La communication asynchrone ici est inhérente au fait que lorsque le producteur (dans ce cas, le service de traitement des commandes) ajoute un message à la file d'attente de messages, il continue son exécution sans attendre de réponse.

Le consommateur pourrait alors traiter les messages de la file d'attente de messages à son propre rythme et envoyer une réponse au producteur ou à l'utilisateur final à un moment ultérieur.

Cela représente un changement radical par rapport à l'approche synchrone. Le génie du modèle de communication asynchrone avec des files d'attente de messages réside dans le fait que les services sont séparés et, par conséquent, rendus indépendants.

Cela est vrai car :

* Si le service de traitement des paiements connaît une défaillance inattendue, le service de traitement des commandes continuera à accepter les requêtes et à les placer dans la file d'attente comme si rien ne s'était produit. Les requêtes seront toujours présentes dans la file d'attente, attendant que le service de paiement les traite lorsqu'il sera de nouveau en ligne. Cela conduit à une architecture plus fiable sans point de défaillance unique.
* Le service de traitement des commandes n'a pas à attendre de réponse du consommateur, les utilisateurs finaux n'ont pas non plus à attendre longtemps — cela conduit à des performances améliorées et, par extension, à une meilleure expérience utilisateur.
* Si le service de traitement des commandes connaît une augmentation du trafic, le service de paiement ne sera pas affecté car il ne récupère les requêtes de la file d'attente de messages qu'à son propre rythme.
* Cette approche a l'avantage d'être simple à mettre à l'échelle, car elle permet d'ajouter plus de files d'attente ou de créer des copies supplémentaires du service de traitement des paiements pour traiter plus de messages plus rapidement.

## **Conclusion**

Dans cet article, nous avons appris à connaître l'architecture monolithique et les microservices. Nous nous sommes également concentrés sur l'exploration du concept des files d'attente de messages et sur la manière d'implémenter un modèle de communication asynchrone dans une architecture de microservices.

Ensuite, nous avons couvert comment l'adoption du modèle de communication asynchrone par opposition à l'approche synchrone pourrait conduire à une augmentation des performances, de la fiabilité et de la facilité de mise à l'échelle.

Nous avons à peine réussi à effleurer la surface des files d'attente de messages et ce qui peut être réalisé avec elles — par exemple, être utilisées dans une architecture distribuée n'est pas leur seul cas d'utilisation.

Pour approfondir votre compréhension des files d'attente de messages et de leurs cas d'utilisation, vous pouvez consulter ce guide détaillé en [7 parties pour débutants sur les files d'attente de messages et les microservices](https://www.cloudamqp.com/blog/microservices-and-message-queues-part-1-understanding-message-queues.html).

Ce guide approfondira le sujet et vous guidera également à travers la création d'une [application de démonstration](https://www.cloudamqp.com/blog/microservices-and-message-queues-part-4-introducing-the-demo-project.html) qui adopte l'architecture de microservices avec une file d'attente de messages. Ainsi, vous pourrez voir de première main comment utiliser une file d'attente de messages dans une architecture distribuée.