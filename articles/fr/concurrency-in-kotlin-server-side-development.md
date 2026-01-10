---
title: Concurrency in Kotlin Server-Side Development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-01-05T23:59:00.000Z'
originalURL: https://freecodecamp.org/news/concurrency-in-kotlin-server-side-development
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/concurrency.jpg
tags:
- name: concurrency
  slug: concurrency
- name: Kotlin
  slug: kotlin
seo_title: Concurrency in Kotlin Server-Side Development
seo_desc: 'By Faith Oyama

  Imagine you''re running a bustling restaurant. Orders fly in, dishes need cooking,
  tables require clearing, and happy customers demand attention. How can you handle
  all this chaos without everything turning into a total disaster? This i...'
---

Par Faith Oyama

Imaginez que vous gérez un restaurant animé. Les commandes affluent, les plats doivent être cuisinés, les tables doivent être débarrassées et les clients satisfaits demandent de l'attention. Comment pouvez-vous gérer tout ce chaos sans que tout ne tourne au désastre total ? C'est là que la concurrency intervient.

Dans le monde du développement côté serveur, les choses peuvent devenir tout aussi mouvementées. Les utilisateurs envoient des requêtes, les bases de données doivent être interrogées, les calculs doivent être effectués, et tout cela doit se faire de manière fluide et efficace. Sans la concurrency, c'est comme avoir un seul chef surmené qui essaie de tout faire.

Mais avec la concurrency, c'est comme ajouter une équipe entière de multitâches qualifiés à votre cuisine. Vous avez des "coroutines" spécialisées qui gèrent différentes tâches - l'une prend les commandes, une autre cuisine, une autre lave la vaisselle, et ainsi de suite. Chacune travaille simultanément, mais de manière coordonnée, assurant que vos clients reçoivent leurs délicieux repas rapidement et avec un sourire.

## Exemples de Concurrency

Voici quelques exemples concrets de la manière dont la concurrency fonctionne dans le développement côté serveur :

**Servir plusieurs utilisateurs à la fois :** Imaginez que votre site web est submergé par des acheteurs impatients lors d'une vente flash. Sans la concurrency, chaque requête utilisateur devrait attendre son tour, entraînant des temps de chargement frustrants.

Mais avec les coroutines, plusieurs requêtes peuvent être traitées simultanément, gardant tout le monde heureux et faisant leurs achats en toute simplicité.

**Traitement des pipelines de données :** Travailler avec de très grands ensembles de données ? La concurrency peut les décomposer et les analyser bit par bit.

**Gestion des requêtes asynchrones :** Pensez aux appels API, aux requêtes de base de données ou aux téléchargements de fichiers. Ceux-ci prennent souvent du temps à se compléter. Avec la concurrency, votre programme principal n'a pas besoin de s'asseoir et d'attendre. Il peut lancer des coroutines séparées pour gérer ces requêtes et revenir à d'autres tâches, gardant tout en marche de manière fluide.

La concurrency n'est pas seulement un mot à la mode fantaisiste - c'est un outil puissant qui vous permet de gérer les demandes toujours croissantes du développement côté serveur avec facilité et efficacité.

Maintenant, nous allons plonger plus profondément dans les différences entre les threads et les coroutines, les blocs de construction fondamentaux de la programmation concurrente en Kotlin.

## Threads vs. Coroutines

Maintenant, parlons des deux principaux acteurs de cette équipe : les threads et les coroutines.

### Qu'est-ce que les Threads ?

Les threads sont puissants et capables de gérer des tâches complexes - mais ils sont aussi un peu gourmands en ressources. Chaque thread nécessite son propre espace mémoire et l'attention du système d'exploitation.

Cela peut être idéal pour des tâches exigeantes comme la décomposition de grands nombres ou l'envoi d'e-mails critiques, mais si vous avez trop de threads en cours d'exécution, votre serveur commence à être submergé, entraînant des ralentissements et même des plantages.

### Qu'est-ce que les Coroutines ?

Les coroutines sont légères, flexibles et capables de basculer entre les tâches en un clin d'œil. Elles n'ont pas besoin de leurs tables dédiées, elles partagent les ressources de manière efficace et peuvent même mettre leur travail en pause de manière élégante si quelque chose d'autre nécessite une attention immédiate.

Pensez à elles comme prenant les commandes, vérifiant les tables et nettoyant la vaisselle - toujours en train de contribuer, mais de manière légère et adaptable.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/kotin.PNG)
_Tableau montrant les différences entre les threads et les coroutines._

Alors, lequel devez-vous choisir ? Eh bien, cela dépend ! Pour les tâches lourdes, les threads sont forts et fiables. Mais pour le travail quotidien, les coroutines sont vos amis agiles.

Kotlin favorise les coroutines pour la programmation concurrente car elles sont plus efficaces et plus faciles à gérer, surtout lorsqu'il s'agit de nombreuses tâches asynchrones.

## Comment lancer des Coroutines

Dans votre code côté serveur, il existe deux principales façons de lancer des coroutines.

### Lancer et oublier : Utiliser le mot-clé `launch`

Cela lance une nouvelle coroutine et l'envoie à sa tâche assignée, mais n'attend pas qu'elle se termine.

Voici à quoi cela ressemble en code :

```kotlin
fun updateCustomerOrder(
  orderId: Int,
  newDish: String
) {
  launch {
    updateOrderInDatabase(orderId, newDish)
  }
  sendConfirmationEmail(orderId)
}
```

Cela est idéal pour les tâches qui n'ont pas besoin de retour immédiat. Vous pouvez lancer plusieurs coroutines comme celle-ci sans surcharger votre serveur, car elles travaillent indépendamment et partagent les ressources de manière efficace.

### Attendre et recevoir : Le mot-clé `async`

Maintenant, disons que vous devez connaître la facture totale avant de pouvoir régler avec le client. C'est là que `async` intervient. C'est comme envoyer un assistant pour calculer la facture et attendre patiemment qu'il revienne avec la réponse.

Voici comment cela fonctionne :

```kotlin
fun calculateBill(orderId: Int): Double {
  val billResult = async {
    calculateBillFromDatabase(orderId)
  }
  val totalBill = billResult.await()
  return totalBill
}
```

Cela est utile pour les tâches où vous avez besoin du résultat avant de continuer. Le mot-clé `async` crée une coroutine qui calcule la facture en arrière-plan (effectue la tâche), mais le programme principal met en pause et attend jusqu'à ce que le résultat soit prêt.

## Canaux : Lignes de communication

Les canaux permettent aux coroutines d'envoyer et de recevoir des messages de manière sûre et organisée, même lorsque les choses deviennent folles. Voici comment ils fonctionnent :

### Sens unique : Canaux d'envoi

Un canal d'envoi permet à une coroutine d'envoyer un message qu'une autre coroutine peut recevoir à l'autre extrémité. Un seul sens, comme une rue à sens unique.

### Ponts bidirectionnels : Canaux de réception

Les canaux de réception permettent à une coroutine d'attendre et de recevoir un message qui a été envoyé sur le canal d'envoi correspondant. Communication bidirectionnelle, comme un pont dans les deux sens.

### Mettre les canaux au travail :

Voici un exemple d'utilisation de canaux pour mettre à jour les commandes des clients :

```kotlin
val orderUpdatesChannel = Channel<Pair<Int, String>>()

fun updateCustomerOrder(orderId: Int, newDish: String) {
  launch {
    updateOrderInDatabase(orderId, newDish)
    orderUpdatesChannel.send(orderId to newDish)
  }
}

fun sendOrderConfirmationEmails() {
  while (true) {
    val orderUpdate = orderUpdatesChannel.receive()
    val (updatedOrderId, newDish) = orderUpdate
    sendConfirmationEmail(updatedOrderId)
  }
}
```

Dans ce cas, la coroutine `updateCustomerOrder` envoie les détails de la commande mise à jour via le `orderUpdatesChannel`. La coroutine `sendOrderConfirmationEmails` attend constamment sur le canal, recevant les mises à jour une par une et envoyant des e-mails de confirmation.

## Structured Concurrency

Pensez à la concurrency structurée comme à l'attribution de rôles et de responsabilités dans votre cuisine. Cela vous aide à :

1. **Définir la portée :** Vous pouvez créer des contextes de coroutine qui fournissent des ressources spécifiques et des limites dans lesquelles vos coroutines peuvent travailler. Cela garde les choses organisées et empêche les coroutines voyous de tout gâcher.
2. **Annulation :** Imaginez un client changeant sa commande en cours de cuisson. La concurrency structurée vous permet d'annuler facilement le mauvais plat et de commencer à préparer le nouveau, sans que tout ne s'effondre en un désastre gras.
3. **Supervision :** La concurrency structurée vous permet de mettre en place des superviseurs qui surveillent leurs coroutines "enfants", s'assurant qu'elles terminent leurs tâches correctement ou gèrent les erreurs de manière élégante.

### Outils clés pour la concurrency structurée :

**Dispatchers :** Ils contrôlent où et comment vos coroutines s'exécutent, comme les assigner à des threads ou des pools spécifiques.

**Jobs :** Pensez à eux comme les tâches elles-mêmes, assignées à des coroutines spécifiques dans un contexte. Vous pouvez suivre leur progression, les annuler si nécessaire, et garder les choses organisées.

**Supervisor Jobs :** Ils supervisent les jobs enfants, gèrent les échecs et les propagent correctement, empêchant les erreurs de se propager et de ruiner tout le repas.

Différents types de tâches dans votre code côté serveur demandent différents environnements. C'est là que les différents types de dispatchers interviennent :

1. **Le Main Dispatcher :** Pensez à lui comme la partie avant de la maison, gérant les mises à jour de l'UI et interagissant directement avec le client (utilisateur). C'est un seul thread, assurant des interactions fluides et réactives sans multitâche chaotique.
2. **Le Default Dispatcher :** C'est le cheval de bataille pour les tâches de calcul général. Il utilise un pool de threads, assignant des coroutines aux threads disponibles. Idéal pour les calculs intensifs en CPU, le traitement de base de données et autres tâches lourdes.
3. **Le IO Dispatcher :** Ce dispatcher gère les opérations d'E/S bloquantes comme les appels réseau, l'accès aux fichiers ou les requêtes de base de données.
4. **Custom Dispatchers :** Vous pouvez créer des dispatchers personnalisés avec des pools de threads spécifiques ou même des threads uniques, les adaptant aux besoins de vos tâches uniques.

Choisir le bon dispatcher est très important pour optimiser les performances et éviter la congestion. Voici quelques conseils :

* Utilisez le main dispatcher uniquement pour les mises à jour de l'UI et l'interaction utilisateur.
* Default dispatcher pour la plupart des tâches intensives en CPU.
* IO dispatcher pour toute opération d'E/S bloquante.
* Envisagez des dispatchers personnalisés pour des tâches spécifiques à haut volume ou sensibles.

## Flows

Imaginez que votre restaurant est en plein essor, les commandes affluent plus vite que les chefs ne peuvent cuisiner. Comment gérez-vous ce déluge de données sans que tout ne tourne en un désastre détrempé ?

Pensez aux Flows comme des flux de données traversant votre code côté serveur, comme le flux continu de commandes provenant des tables. Au lieu de traiter chaque plat individuellement, les Flows vous permettent de gérer les données en continu, en vous adaptant au rythme et en les transformant à la volée.

Voici pourquoi les Flows sont un changement de jeu :

* Plus besoin d'attendre que les données arrivent. Les Flows vous permettent de lancer des coroutines pour gérer le flux de manière asynchrone, gardant votre programme principal libre de continuer à prendre des commandes et à gérer l'expérience globale.
* Les Flows vous permettent d'extraire des insights, de générer des rapports ou de déclencher des actions en temps réel.
* Les Flows ajustent automatiquement leur rythme en fonction des capacités de traitement en aval, empêchant les arriérés et assurant un flux de données fluide à travers votre système.
* Les erreurs sont gérées délicatement avec les flows, qui les transmettent sans faire tomber l'ensemble du service.

Voici un exemple d'utilisation des Flows pour traiter un flux de lectures de capteurs :

```kotlin
val sensorReadingsFlow = sensorManager.readings()
    .filter { reading -> reading.temperature > 80 } 
    .map { reading -> "Alert! Sensor ${reading.id} at ${reading.temperature} degrees!" }    
    .launchIn(Dispatchers.IO) 
    .onEach { message -> logger.warn(message) } 
    .collectLatest { message -> sendPushNotification(message) }
```

Ce Flow lit les lectures des capteurs en continu, filtre les températures élevées, les transforme en messages d'alerte et les envoie aux utilisateurs, le tout de manière non bloquante et résiliente.

Les Flows sont un outil puissant pour le développement côté serveur moderne. Ils vous permettent d'embrasser le monde du traitement de données asynchrone avec grâce et efficacité, gardant votre code réactif, scalable et prêt à gérer tout banquet de données que vos utilisateurs vous lancent.

## Tester votre configuration de Concurrency

Vous avez donc construit votre cuisine côté serveur avec des coroutines agiles, des canaux de communication fluides et des dispatchers efficaces. Vos données circulent comme un ruisseau impétueux, et vos clients (utilisateurs) chantent vos louanges. Mais avant d'accrocher définitivement l'enseigne "Ouvert", il y a une étape cruciale : tester votre magie de concurrency.

Les tests vous aident à découvrir les cas limites, à prévenir les plantages et à garantir que tout fonctionne de manière fluide même sous charge élevée.

Voici quelques points clés pour tester le code concurrent :

* **Se concentrer sur l'isolement :** Testez les coroutines et les canaux individuels en isolation pour identifier les problèmes dans des composants spécifiques. Vous pouvez utiliser des bibliothèques comme kotlinx-coroutines-test pour contrôler le temps et simuler le comportement asynchrone.
* **Mock des dépendances :** Les dépendances externes comme les bases de données ou les API peuvent ajouter de la complexité. Le mock de ces dépendances vous permet de vous concentrer sur le comportement des coroutines sans introduire d'incertitudes du monde réel.
* **Vérifier les changements d'état :** Assurez-vous que les coroutines mettent à jour les structures de données et les drapeaux correctement lors de leur exécution. Assert les valeurs attendues à différents points du flux d'exécution.
* **Test de stress de performance :** Poussez votre code à ses limites avec un volume élevé ou des scénarios complexes. Cela vous aide à identifier les goulots d'étranglement et à garantir que votre système scale de manière élégante.

Rappelez-vous, tester le code concurrent n'est pas toujours simple. Soyez patient, expérimentez avec différentes méthodes et n'ayez pas peur de demander de l'aide à des développeurs expérimentés et à des frameworks de test.

## Conclusion

Nous avons exploré les coroutines agiles dansant à travers les tâches, les canaux efficaces les gardant synchronisés, et les dispatchers intelligents dirigeant le flux. Nous avons vu comment les Flows gèrent de manière transparente les flux de données, et nous avons appris l'importance des tests robustes pour garantir que tout fonctionne de manière fluide.

Maintenant, avec cette connaissance, vous devriez comprendre le concept de concurrency dans vos applications Kotlin. Embrassez-le, utilisez-le avec sagesse, et regardez vos applications s'élever à de nouveaux sommets de réactivité, de scalabilité et d'efficacité.