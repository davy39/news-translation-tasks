---
title: 'Guide de survie : comment migrer de la Firebase Realtime Database vers Cloud
  Firestore'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-12T18:52:56.000Z'
originalURL: https://freecodecamp.org/news/rtdb-to-firestore-fd8da8149877
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0iVNXCyFoHREN59CVyQB5w.jpeg
tags:
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Guide de survie : comment migrer de la Firebase Realtime Database vers
  Cloud Firestore'
seo_desc: 'By Alex Saveau

  Ever since Google’s new mobile SDKs were announced two years ago at I/O, the Firebase
  empire has been ever-expanding. It now supports more and more features, such as
  Cloud Functions, phone authentication, and performance monitoring. Ho...'
---

Par Alex Saveau

Depuis que les nouveaux SDK mobiles de Google ont été [annoncés](https://firebase.googleblog.com/2016/05/firebase-expands-to-become-unified-app-platform.html) il y a deux ans lors de l'I/O, l'empire Firebase n'a cessé de s'étendre. Il prend désormais en charge de plus en plus de fonctionnalités, telles que Cloud Functions, l'authentification par téléphone et la surveillance des performances. Cependant, un SDK qui n'a pas beaucoup changé est la Firebase Realtime Database (RTDB).

La RTDB n'a pas reçu de mises à jour majeures — et ce n'est pas parce que c'était une API parfaite. Bien au contraire. Si vous avez lu l'expérience de [Pier Bover](https://medium.freecodecamp.org/firebase-the-great-the-meh-and-the-ugly-a07252fbcf15), ou si vous avez utilisé vous-même la Firebase RTDB, ces problèmes pourraient vous sembler familiers :

> Aucun moyen d'interroger vos données correctement […] et une modélisation des données stupide.

Alors, quelle est la suite ? Comment Google va-t-il résoudre ces limitations ? Au lieu de publier une version 4.0 de la RTDB, ce qui serait désordonné et douloureux pour tout le monde, Google utilise ce qu'il a appris des défauts de la Firebase Realtime Database. Et ils redessinent et réécrivent complètement à partir de zéro une nouvelle base de données : Cloud Firestore.

La RTDB ne va pas disparaître — cela provoquerait une énorme crise. Mais à l'avenir, Cloud Firestore recevra la plupart de l'attention et de l'amour.

Cet article va approfondir la refonte tant attendue de la base de données de Google, principalement du point de vue d'un développeur Android RTDB. De plus, l'article est destiné à remplacer des heures de consultation de la documentation pour construire un modèle mental du nouveau SDK.

### Contexte

Sauf si vous avez récemment rejoint la communauté Firebase, vous avez probablement entendu parler de la Google Cloud Platform (GCP). À l'exception de la RTDB, tous les autres produits serveur Firebase, comme Cloud Functions et Firebase Storage, sont généralement des rebrandings de solutions GCP existantes avec des fonctionnalités supplémentaires — plus l'intégration et la marque Firebase.

Cependant, la RTDB a été portée depuis l'époque pré-Google de Firebase. Il s'avère que la base de données était en fait un service de chat. Ils ont seulement décidé de supprimer l'interface utilisateur et de la transformer en SDK après que l'entreprise ait changé de focus. Avec le flux sans fin d'exemples d'applications de chat, on pourrait penser qu'ils sont encore un peu nostalgiques.

D'autre part, Cloud Firestore est construit à partir de Google Cloud Datastore de GCP, une base de données NoSQL avec une scalabilité quasi infinie et des capacités de requête puissantes. Le Cloud Datastore marqué Firebase ajoute les capacités de temps réel attendues et, bien sûr, l'intégration avec d'autres services Firebase tels que l'authentification et Cloud Functions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0iVNXCyFoHREN59CVyQB5w.jpeg)
_Schéma de flux pré-Firestore. Vous obtenez désormais le meilleur de Firebase et de Datastore !_

Pour les fans de bases de données, Cloud Datastore est une base de données multi-région, répliquée de manière synchrone, qui utilise des transactions ACID. Cela signifie que une fois que Google dit que votre écriture est validée, un météorite de l'âge des dinosaures pourrait détruire une région et vos données seraient toujours en sécurité, prêtes à être interrogées.

Je ne dis pas que nous, les humains, nous en sortirions aussi bien… mais au moins vos données seraient toujours solides comme un roc ! Oh, et il utilise des horloges atomiques — si ce n'est pas cool, je ne sais pas ce qui l'est !

Maintenant que vous avez une compréhension de base de pourquoi Google a décidé de créer une toute nouvelle base de données sous la marque Firebase et d'où elle vient, commençons !

Pour le reste de cet article, j'utiliserai des exemples d'applications que j'ai construites (donc pas d'exemples d'applications de chat ! 😉). Plus précisément, j'utiliserai des exemples de R[obot Scouter,](https://github.com/SUPERCILEX/Robot-Scouter) une application pour aider les équipes de la F[IRST Robotics Competition](https://www.firstinspires.org/robotics/frc) à prendre des décisions basées sur les données pendant les compétitions.

Le but de base de l'application est de permettre aux utilisateurs de collecter des données sur d'autres équipes dans des unités appelées **scouts**. Ces scouts peuvent être basés sur des **modèles** personnalisables. Les scouts et les modèles sont composés de **métriques**, qui sont différents types de données qu'un utilisateur peut collecter. Les modèles sont des objets autonomes, mais les scouts sont implicitement possédés par une équipe.

Les équipes et les modèles individuels peuvent être partagés avec d'autres utilisateurs, mais les scouts suivront une équipe partout où elle ira puisque l'équipe les possède.

### Structures de données

Commençons par examiner à quoi ressemblait la structure de données de Robot Scouter avec la RTDB. Prenez une profonde inspiration, il y a beaucoup à faire défiler :

Tout ce que nous voulions vraiment, c'était une collection `teams`, `templates` et `users`. Au lieu de cela, nous avons dû dénormaliser nos données pour accommoder les requêtes profondes par défaut de la RTDB. Rappelez-vous, si nous interrogeons un nœud avec la RTDB, nous obtenons également **tous** les nœuds enfants.

Maintenant, examinons la structure de données équivalente de Cloud Firestore :

La structure de données de Cloud Firestore est plus facile à comprendre et beaucoup plus courte que la structure RTDB. Cela est grâce aux références imbriquées par rapport à la dénormalisation forcée de tout dans la RTDB.

#### Différences de structure de données

La première différence majeure que vous remarquerez est l'absence de dénormalisation. Dans la [structure de données de Cloud Firestore](https://firebase.google.com/docs/firestore/data-model), nous déclarons notre référence `teams` et plaçons chaque équipe directement à l'intérieur de cette référence au lieu de l'aplatir. De même, nous avons fusionné les `template-indices` directement dans la référence `templates`.

Vous avez peut-être également remarqué que nos `scouts` sont maintenant directement placés à l'intérieur d'une équipe au lieu d'être dans une référence d'index séparée. Votre première réaction a peut-être été « Attendez, vous allez gaspiller toutes les données de l'utilisateur ! Ne faites pas ça ! » C'est la beauté de Cloud Firestore : **les requêtes sont « superficielles » par défaut**.

J'ai mis le mot **superficiel** entre guillemets car techniquement, vous pourriez imbriquer une énorme quantité de données dans vos documents. Mais nous parlerons plus tard de pourquoi vous ne devriez pas faire cela. Attendez une seconde, qu'est-ce qu'un document ? Cloud Firestore a deux blocs de construction de base : **collections** et **documents**.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FsC5XWRn7tsvv0xedy-6bQ.png)
_Les blocs de construction fondamentaux de Cloud Firestore_

Les collections dans Firestore sont l'équivalent d'une référence dans la RTDB avec une énorme liste de nœuds enfants qui contiennent chacun des objets. Si vous faites défiler vers le haut jusqu'à la structure de données Firestore, vous remarquerez que `teams`, `templates` et `users` sont toutes des collections. Elles contiennent chacune un tas d'objets — et dans Firestore, ces objets sont appelés documents.

Les documents seraient vos nœuds d'objets conventionnels dans la RTDB. Cependant, dans Firestore, ils sont un peu spéciaux : les documents sont explicitement possédés par une collection. Dans la RTDB, vous pouviez mettre presque n'importe quoi n'importe où. Cloud Firestore apporte un peu de bon sens et utilise un motif alterné de collections et de documents qui ressemble un peu à ceci : `collection1/document1/collection2/document2/...`.

Bien que ce motif puisse sembler contraignant au début, je l'ai trouvé utile pour me forcer à concevoir une structure de données bien organisée. Vous remarquerez que ma collection `scouts` réside maintenant correctement dans un document d'équipe. Je n'ai dû la séparer dans la RTDB que pour que mes utilisateurs n'aient pas à télécharger tous leurs scouts lorsqu'ils regardaient une équipe. Dans Cloud Firestore, les équipes ont une propriété explicite d'un ensemble de scouts sans avoir à les télécharger lors du chargement de l'équipe.

#### Un peu plus sur les documents

Dans la RTDB, vous aviez un modèle libre avec 3 types de données de base : les booléens, les chaînes et les nombres. Des choses comme les listes et les cartes étaient soit une réflexion après coup, soit simplement une partie de la manière dont vous interrogiez les données dans la RTDB.

D'autre part, avec Firestore, vous avez une structure très claire : les collections contiennent des documents, et les documents contiennent des champs et des **liens** vers une ou plusieurs **sous-collections**.

Sous-collection est juste un terme fantaisiste pour une autre liste d'objets possédés par un document — sauf que vous n'obtiendrez pas cette liste lors de l'interrogation du document. Cela est dû au fait que les documents ne contiennent pas techniquement de sous-collections. Ils se contentent de les lier. D'où le fait que nous pouvons mettre notre collection `scouts` à l'intérieur du document d'équipe — ou la lier, si vous préférez.

En plus de contenir des sous-collections, les documents dans Firestore supportent un [vaste ensemble de types de données](https://firebase.google.com/docs/firestore/manage-data/data-types) avec plus à venir. Pour l'instant, voici les types supportés :

* Booléen
* Chaîne
* Nombre
* Octets bruts (si c'est votre style 😉)
* Dates et heures
* Points géographiques
* Références
* Tableaux et cartes
* Null !

Oui, `null` est maintenant un type de données explicitement défini dans Cloud Firestore. Si vous définissez un document égal à un objet Java dont le getter retourne null, le champ apparaîtra toujours dans la console Firebase avec le type de données `null`.

Bien, alors quoi ? L'ajout du type de données `null` rend la suppression de champ explicite. Dans la RTDB, définir quelque chose à `null` est la même chose que de le supprimer. Mais dans Firestore, pour supprimer un champ, vous devez définir sa valeur à `FieldValue.delete()`. Sur une note similaire, `ServerValue.TIMESTAMP` est devenu `FieldValue.serverTimestamp()`.

De plus, le type de données `null` permet en quelque sorte les migrations. En utilisant la méthode `DocumentSnapshot#contains()`, vous pourriez vérifier si un champ existe et faire quelque chose s'il n'existe pas. Une meilleure stratégie serait d'utiliser une Cloud Function, mais cela dépasse le cadre de cet article.

Vous remarquerez que les documents supportent toujours les tableaux et les cartes, mais comment cela fonctionne-t-il si les documents ne peuvent contenir que des champs ? Rappelez-vous comment j'ai dit que vous pourriez techniquement imbriquer vos données ? Voici ce cas spécial : Firestore vous permet de stocker des tableaux et des cartes explicitement définis dans des documents, plutôt que de créer une sous-collection.

Note : il y a plusieurs [limites](https://firebase.google.com/docs/firestore/quotas) aux documents dans Firestore. Plus précisément, **il y a une limite de taille de 1 Mo, un maximum de 20 000 propriétés par document et une limite de 500 niveaux de profondeur d'imbrication d'objets**.

Les propriétés sont différentes des champs en ce sens qu'elles tiennent compte de tous les champs imbriqués, et non seulement des champs de niveau racine conventionnels. De plus, à l'heure où j'écris ces lignes, la mise à jour d'un grand tableau ou d'une grande carte réécrit l'ensemble du tableau/carte et aura des performances abyssales sur les grandes structures de données. Veuillez utiliser des sous-collections à la place !

Parce que Google aime renommer les choses, les « clés » des documents de la RTDB sont maintenant appelées **ids**. Le dernier segment de chemin d'une collection ou d'un document est appelé un id, ce qui signifie que `teams/teamId1` est un document avec l'id `teamId1` sous une collection avec l'id `teams`. Rien de révolutionnaire, mais c'est toujours bien d'être sur la même longueur d'onde en matière de terminologie.

Enfin, puisque les documents sont l'un des blocs de construction fondamentaux de Firestore, vous ne pouvez obtenir qu'un document complet. Contrairement à la RTDB où vous pouviez interroger un champ aussi spécifique que vous le souhaitiez.

### Stockage et récupération des données

Maintenant que vous avez une compréhension de base des deux blocs de construction fondamentaux de Firestore — les collections et les documents — il est temps de voir comment nous pouvons stocker puis obtenir nos données.

L'API de surface de Cloud Firestore est une **énorme** amélioration par rapport à celle de la RTDB. Vous êtes donc peu susceptible de trouver des méthodes qui ont simplement été portées (bien que certaines puissent sembler familières).

#### Stockage des données

La première distinction que vous remarquerez par rapport à la RTDB est la manière légèrement désordonnée et dispersée de créer et de mettre à jour les données. Pas de souci, tout cela aura du sens dans un instant.

Contrairement à nos animaux de compagnie, il n'y a pas de documents errants — ils doivent tous vivre sous une collection. Cela signifie que nous avons deux endroits d'où nous pouvons ajouter des données : une collection pour ajouter des documents, et un document pour ajouter, mettre à jour ou supprimer des champs.

Commençons par examiner la manière la plus simple d'ajouter des données, via les collections :

Nous disons que dans la collection `teams`, nous voulons ajouter un document avec tous les champs du POJO `Team`.

Maintenant, examinons le cas plus intéressant où nous modifions les données d'un document :

La première chose à noter est notre `scoutRef` : il crée un scout à l'intérieur de notre collection de scouts, qui à son tour existe sous un document d'équipe. En tant qu'URL, cela ressemblerait à ceci : `teams/teamId/scouts/newScoutId`.

La méthode `document()` retourne une nouvelle `DocumentReference` avec un id aléatoire. C'est un id **vraiment** aléatoire dans le sens où il n'est plus basé sur un timestamp.

Ceux qui sont familiers avec la RTDB savent que la méthode `push()` crée une clé pseudo-aléatoire en utilisant un timestamp pour le tri temporel natif. Puisque Cloud Firestore vise à s'éloigner d'être une base de données orientée chat, il n'a pas de sens pour eux d'utiliser le tri temporel comme mécanisme par défaut.

Ainsi, cela signifie que vous devrez ajouter manuellement un champ `timestamp` lorsque cela est pertinent. En théorie, vous pourriez utiliser le timestamp comme id de document pour le tri, mais cela réduit la flexibilité.

La `DocumentReference` contient une pléthore de différentes manières de définir et de mettre à jour les données, allant de l'utilisation de cartes et de POJOs à la fourniture de varargs. Il y en a pour tous les goûts ! Je vais me concentrer sur les méthodes de mise à jour de POJO et de champ spécifique, car ce sont celles que j'ai trouvées les plus utiles.

La première méthode que vous remarquerez et que vous utiliserez probablement le plus souvent est `set(Object)`. Celle-ci est assez simple : elle se comporte exactement comme la méthode `Map#set(key, value)` de Java. Si aucun document n'existe, il en créera un nouveau. Sinon, si un document existe, il sera écrasé.

Cependant, Google fournit également des `[SetOptions](https://firebase.google.com/docs/firestore/reference/android/SetOptions)` avec diverses combinaisons de fusion pour ne remplacer que certains champs. J'ai trouvé cela utile lors de la mise à jour du profil d'un utilisateur, par exemple. Je vais définir/mettre à jour leur `name`, `email` et `photoUrl`, mais pas le champ `lastLogin`, car il ne fait pas partie de mon POJO `User`.

Si vous souhaitez vous assurer qu'un document existe avant d'effectuer une mise à jour, la méthode `update(String, Object, Object)` sera l'outil adapté à la tâche. Dans ce cas, nous mettons à jour un champ spécifique avec une nouvelle valeur. Si le document n'existe pas avant d'appeler la méthode de mise à jour, la mise à jour échouera. Si vous le souhaitez, vous pouvez également mettre à jour plusieurs champs à la fois en alternant les paires clé/valeur dans les varargs. (Je préfère personnellement utiliser plusieurs mises à jour dans un `WriteBatch`, que je vais aborder plus tard.)

Que faire si vous souhaitez mettre à jour un champ imbriqué à l'intérieur d'un objet ? Pour ce cas d'utilisation, Google fournit la méthode `FieldPath#of(String)`. Chaque élément à l'intérieur du tableau varargs vous emmène plus profondément dans le chemin d'un champ imbriqué — techniquement un objet. Par exemple, `FieldPath.of("rootField", "child")` met à jour le champ suivant : `myDocument/rootField/child`.

De même, Firestore prend également en charge la syntaxe de notation par points qui vous permet de référencer ce même champ comme suit : `rootField.child`.

Cloud Firestore inclut également une nouvelle manière géniale de regrouper les écritures avec la classe `WriteBatch`. Elle est très similaire à l'`SharedPreferences.Editor` que vous trouverez sur Android. Vous pouvez ajouter ou mettre à jour des documents dans l'instance `WriteBatch`, mais ils ne seront pas visibles pour votre application jusqu'à ce que vous appeliez `WriteBatch#commit()`. J'ai créé l'amélioration standard Kotlin où le cycle de vie du batch est géré pour vous — n'hésitez pas à copier-coller.

Le dernier changement important de l'API à noter lors de la gestion des données est la manière de les supprimer. Cloud Firestore dispose d'une méthode pour supprimer un document — `DocumentReference#delete()` — mais pas de moyen facile de supprimer une collection entière. Google fournit un [exemple de code avec documentation](https://firebase.google.com/docs/firestore/manage-data/delete-data#collections) sur la manière de supprimer tous les documents d'une collection, mais ils ne l'ont pas encore intégré au SDK. Cela est dû au fait que cette méthode pourrait facilement échouer dans des conditions extrêmes lors de la tentative de suppression de milliers, voire de millions de documents enfouis dans diverses sous-collections. Mais Google dit qu'ils y travaillent.

De plus, leur exemple ne supprime pas non plus les sous-collections — seulement les documents sous la collection. Google n'a pas encore de solution claire à ce problème sur Android non plus. Néanmoins, ils fournissent une API CLI/NodeJS dans le cadre de `firebase-tools` que vous pouvez utiliser pour supprimer toutes les sous-collections manuellement ou à partir d'une Cloud Function.

Dans mon cas, je n'autorise pas les utilisateurs à créer des noms de collection aléatoires, donc je peux supprimer toutes mes sous-collections en obtenant leurs identifiants de document parent.

J'ai réécrit leur exemple avec plus de fonctionnalités et une API plus propre en Kotlin :

Ouf, nous avons couvert presque tout ce que vous devez savoir sur le stockage des données !

#### Récupération des données

La première chose à noter est que j'utilise le mot **récupération** au lieu de lecture. Cela est dû au fait que Firestore fournit deux manières très claires de récupérer des données : soit par une lecture unique (aka un **get**), soit par une série de lectures (aka un **snapshot listener**).

#### Obtention des données

Commençons par explorer les manières de lire les données une fois. Dans la RTDB, vous aviez la méthode `addListenerForSingleValueEvent()`, mais elle était pleine de bugs et de cas particuliers. Je pense que Frank van Puffelen — un Googler — l'a résumé le mieux :

> La meilleure façon de résoudre cela est de ne pas utiliser un listener de valeur unique.

Oui. Il y a définitivement un problème lorsque vous dites à vos propres utilisateurs de ne pas utiliser un produit que vous vendez.

Cloud Firestore réinvente complètement l'expérience de récupération des données avec des API meilleures et plus intuitives.

Tout d'abord, une note sur les capacités hors ligne. La RTDB n'a pas été conçue comme une base de données hors ligne en premier — les capacités hors ligne étaient plus une réflexion après coup puisque la base de données a été portée depuis l'époque pré-Google de Firebase. D'autre part, Cloud Firestore n'est pas exactement une base de données hors ligne en premier puisque elle est également conçue pour être en temps réel. Mais je considérerais ses capacités hors ligne comme des citoyens de première classe avec les fonctionnalités en temps réel.

Étant donné ces améliorations, le support hors ligne est activé par défaut (sauf pour le web), et les données sont stockées dans une base de données SQLite en utilisant les API natives d'Android. Je ne sais pas pour vous, mais je trouve plus qu'un peu ironique qu'une base de données NoSQL ait besoin d'une base de données SQL pour fonctionner.

Pour les curieux, la base de données SQL de Firestore est nommée `firestore.$firebaseAppName.$projectId.(default)`. De plus, ils la verrouillent en utilisant `PRAGMA locking_mode = EXCLUSIVE` pour améliorer les performances et empêcher l'accès multi-processus. Si vous êtes vraiment curieux, voici les tables et requêtes que j'ai trouvées jusqu'à présent :

J'ai fait quelques recherches supplémentaires et j'ai trouvé quelques autres choses. Par exemple, les développeurs GRCP [aiment vraiment les énumérations](https://github.com/grpc/grpc-java/blob/16c07ba434787f68e256fc50cece1425f421b03e/okhttp/third_party/okhttp/java/io/grpc/okhttp/internal/CipherSuite.java#L36-L357). Vous savez ce qu'on dit, « Si quelque chose est mauvais pour vous, faites-en plus ! »

![Image](https://cdn-media-1.freecodecamp.org/images/1*Hy3jjZBRgdJILyHLp6GuYQ.png)
_Il y a 95 énumérations ici — ça doit être un genre de record !_

Cela mis à part, explorons notre première méthode : `DocumentReference#get()`. Il s'agit de la manière la plus simple et la plus basique de récupérer des données : elle remplace la méthode `addListenerForSingleValueEvent()` de la RTBD avec plusieurs améliorations notables.

Tout d'abord, elle retourne un `Task<DocumentSnapsh`ot> . Cela a beaucoup plus de sens que d'utiliser la même API de modèle d'événement que vous utiliseriez pour les écouteurs de snapshot de la RTDB. Maintenant, vous pouvez utiliser toutes les API de `Task` de Play Services pour ajouter vos écouteurs de succès et d'échec. Vous pouvez même les attacher à un cycle de vie d'activité si nécessaire.

Deuxièmement, le support hors ligne a enfin du sens lorsque vous utilisez `get()`. Si l'appareil est en ligne, vous obtiendrez la copie la plus à jour de vos données directement depuis le serveur. Si l'appareil est hors ligne et dispose de données en cache, vous obtiendrez immédiatement ce cache. Et enfin, s'il n'y a pas de données en cache, vous obtiendrez immédiatement un événement d'échec avec le code d'erreur `FirebaseFirestoreException.Code#UNAVAILABLE`. En résumé : vous obtiendrez les données les plus à jour qui peuvent être récupérées dans l'état actuel du réseau de l'appareil.

Je vais plonger dans les requêtes dans un instant, mais pour l'instant, je vais simplement mentionner que la méthode `Query#get()` retournant un `Task<QuerySnapsh`ot> est également disponible avec le même comportement que décrit ci-dessus.

Dans d'autres nouvelles notables, la méthode `Query#getRef()` a été supprimée pour supporter un futur possible où une requête ne dépend pas d'une `CollectionReference`. Tout comme dans la RTDB, `CollectionReference` étend `Query` pour supporter facilement le démarrage d'une requête. Mais dans la RTDB, vous pouviez sauter d'avant en arrière entre les requêtes et les refs. Ce n'est plus le cas dans Firestore. J'ai trouvé cela être un léger inconvénient, mais rien de trop majeur.

#### Écoute des données

Bien sûr, ceci est Firebase — donc nous voulons aussi nos capacités de temps réel. La surface de l'API pour les requêtes a également été complètement réinventée pour être plus propre et plus claire.

Commençons par voir comment vous obtiendriez tous les documents dans une collection.

Vous vous souvenez de la différence entre `addValueEventListener()` et `addChildEventListener()` de la RTDB ? Et avez-vous déjà souhaité pouvoir obtenir un peu des deux mondes ? Moi aussi. Heureusement, c'est exactement ce que Google a fait avec Cloud Firestore : vous obtiendrez la liste complète des documents **et** une liste des changements **et** des exceptions possibles, le tout dans un seul rappel monolithique.

Je ne suis pas sûr d'aimer le modèle combiné données/exception, mais cela a du sens dans un monde Java 8 avec des interfaces fonctionnelles. Par exemple, voici un rappel lambdazé :

Commençons par le cas d'erreur, puisque c'est ce à quoi tous les bons développeurs devraient penser en premier, n'est-ce pas ? 😉

`FirebaseFirestoreException` est relativement simple par rapport à la RTDB. Tout d'abord, c'est en fait une exception ! Whaaat ? Une erreur qui étend réellement `Exception` — qui aurait pensé à cela ? Cela rend la génération de rapports de plantage extrêmement simple : il suffit de signaler l'exception qui inclut les [codes d'erreur](https://firebase.google.com/docs/firestore/reference/android/FirebaseFirestoreException.Code) et tout. Cela aura l'air joli et propre comme ceci :

Exception com.google.firebase.firestore.FirebaseFirestoreException: PERMISSION_DENIED: Autorisations manquantes ou insuffisantes.

Cela mis à part, passons aux choses excitantes : `[QuerySnapshot](https://firebase.google.com/docs/firestore/reference/android/QuerySnapshot)`. Il contient [les changements de document](https://firebase.google.com/docs/firestore/reference/android/DocumentChange), la liste complète des [documents](https://firebase.google.com/docs/firestore/reference/android/DocumentSnapshot), et quelques autres données que j'explorerai dans un instant.

J'ai fourni des liens vers toutes les classes pertinentes, car je vais sauter celles-ci en faveur de l'utilisation de FirebaseUI. Je vais explorer cela en profondeur plus tard lorsque nous mettrons tout ensemble.

En résumé rapide, vous pouvez différencier entre différents types de mises à jour, itérer sur le `QuerySnapshot` pour obtenir chaque `DocumentSnapshot` dans de jolies boucles for Java 5, convertir la liste entière en un tas de POJOs (non recommandé pour des raisons de performance, nous en discuterons plus tard), et convertir des documents individuels en un POJO ou accéder à des informations de champ spécifiques. Donc, essentiellement tout ce que vous attendriez d'une belle API.

Cependant, je veux explorer l'enregistrement des écouteurs et `QueryListenOptions` — une nouvelle manière d'obtenir des informations sur votre statut hors ligne.

Ces deux concepts seront plus faciles à comprendre avec un exemple de code, alors voici :

L'idée de base de cette méthode est d'attendre que les données soient reçues directement depuis le serveur.

La première chose à noter est l'enregistrement des écouteurs — c'est un peu douloureux. J'ai passé un peu de temps à y réfléchir, et je suis arrivé à la conclusion que Google a fait le bon choix. Cela **devrait** être douloureux pour vous orienter dans la bonne direction.

D'accord, faisons un peu marche arrière. Dans la RTDB, vous êtes habitué à supprimer l'instance de rappel de l'écouteur directement depuis la classe Query. C'était une belle API, mais elle vous permettait de faire des choses terribles comme fuiter accidentellement vos `Context`. La nouvelle API retourne un `ListenerRegistration` dont la seule méthode est `remove()` — assez explicite.

Cette nouvelle méthode d'enregistrement des écouteurs vous force à repenser votre approche de la récupération des données. Voici un guide simple pour choisir quelle API utiliser :

1. Si vos données ne sont pas affichées à l'utilisateur, vous devriez probablement utiliser l'une des méthodes `get()` qui utilisent le même mécanisme d'enregistrement des écouteurs en interne comme montré ci-dessus. (Google souffre pour vous 😉)
2. Si vos données sont liées à l'UI, vous devriez utiliser la variante `addSnapshotListener(Activity, ...)` qui gère automatiquement le cycle de vie pour vous en se désinscrivant dans `Activity#onStop()`.
3. Si vos données sont liées à une liste comme un `RecyclerView`, retenez vos chevaux — je vais détailler la bibliothèque FirebaseUI grandement améliorée plus tard, qui gérera automatiquement presque tout pour vous.
4. Si vous ne rentrez pas dans les catégories ci-dessus, alors vous devriez envisager d'utiliser FirebaseUI (encore !) que je détaillerai plus tard (encore !). Sinon, détournez simplement les yeux. 😉

D'accord, donc l'API d'enregistrement des écouteurs est douloureuse, mais intentionnellement pour vous orienter vers le bon outil pour le travail.

Maintenant, jetons un coup d'œil aux `QueryListenOptions`. Vous vous souvenez comment j'ai dit que Cloud Firestore considère le support hors ligne comme un citoyen de première classe ? Voici où ils abordent les derniers points de douleur que les développeurs ont rencontrés avec la RTDB. Ils n'offrent toujours pas de moyen de personnaliser la manière dont vos données sont mises en cache, mais personnellement, je ne vois aucune valeur dans ce type de personnalisation : l'API devrait être suffisamment intelligente pour gérer cela pour moi — et c'est le cas avec Firestore.

La première méthode que vous trouverez dans vos options d'écoute s'appelle `includeQueryMetadataChanges()` et la seconde s'appelle `includeDocumentMetadataChanges()`. Les deux sont liées aux `SnapshotMetadata``s `isFromCache()` et `hasPendingWrites()` respectivement.

Pour un `QuerySnapshot` donné, `isFromCache()` aura la même valeur pour les métadonnées de chaque `DocumentSnapshot` et pour les métadonnées de la requête elle-même. Cela signifie que vous pouvez découvrir si vos données sont à jour avec le serveur soit à partir d'un `QuerySnapshot` soit à partir d'un `DocumentSnapshot` — cela n'a pas d'importance. Soit l'ensemble de la requête est considéré comme étant à jour, soit non — il n'y a pas d'état intermédiaire comme l'API pourrait vous le faire croire. En théorie, l'un de vos documents pourrait en fait être à jour si un autre écouteur actif inclut ce document dans ses résultats, mais Google a opté pour la simplicité et ne surface pas cette information dans l'API.

D'autre part, `hasPendingWrites()` peut avoir une valeur différente pour chaque `DocumentSnapshot`. C'est ce à quoi vous vous attendriez, et il n'y a pas de cas particuliers ou d'astuces.

Pour résumer :

* Utilisez `includeQueryMetadataChanges()` si vous souhaitez savoir si une requête et tous ses documents sont à jour avec le serveur.
* Utilisez `includeDocumentMetadataChanges()` si vous souhaitez connaître les changements par document dans l'état d'écriture en attente.

Un dernier détail avant de passer à autre chose : toutes les méthodes `addSnapshotListener` sont également dupliquées dans `DocumentReference` afin que vous puissiez obtenir des mises à jour sur un seul document si nécessaire.

#### Interrogation des données

Ahhh… Plus de 3 000 mots plus tard, nous arrivons enfin au cœur de Cloud Firestore.

Je n'ai aucune statistique pour étayer cette affirmation, mais je pense que de loin la plus grande plainte concernant la RTDB est le manque de capacités d'interrogation appropriées. Voici une autre citation de l'article de Pier Bover :

> Vraiment ? Google fournit un service de données sans capacités de recherche ou de filtrage ? Oui. Vraiment.

Puisque Cloud Firestore est soutenu par le Cloud Datastore de GCP, les requêtes sont des citoyens de première classe.

Revenons à notre nouvelle et améliorée structure de données. Mais pour vous éviter de faire défiler agressivement vers le haut pendant une minute, la voici repostée :

Puisque nous avons une liste infinie d'équipes, comment obtenons-nous les équipes d'un utilisateur spécifique ? Dans la RTDB, nous aurions stocké les données en suivant un modèle similaire à ceci : `teams/uid1/teamKey1`. Avec Cloud Firestore, nous inversons l'id de l'utilisateur et l'id de l'équipe afin que le modèle ressemble davantage à ceci : `teams/teamKey1/owners/uid1`.

Maintenant, nous pouvons interroger les équipes de l'utilisateur comme suit :

Nous disons à Firestore de regarder le champ `owners` dans tous les documents sous la collection `teams` pour un document avec l'id `uid` égal à `true`.

Malheureusement, cette méthode ne supporte pas le tri. Nous allons donc écrire la requête suivante :

Cette requête a l'avantage de supporter le tri, mais elle vient avec des problèmes similaires à ceux de la RTDB : la mise à jour de ces valeurs de tri va être douloureuse.

Dans mon cas, les valeurs de tri sont toujours statiques : ce sont soit le numéro de l'équipe, soit le timestamp de création du document. Comme je ne vais jamais mettre à jour ces valeurs de tri, cette requête fonctionne parfaitement pour moi.

D'autre part, vous pourriez avoir différentes contraintes — rappelez-vous, j'ai besoin que mes données soient structurées de manière à supporter facilement le partage d'équipes et de modèles entre les utilisateurs. Si ce n'est pas votre cas, vous devriez jeter un coup d'œil aux [structures suggérées par Google](https://firebase.google.com/docs/firestore/manage-data/structure-data) et à leurs [solutions aux problèmes courants](https://firebase.google.com/docs/firestore/solutions/).

Puisque les requêtes que vous écrivez dépendront des contraintes spécifiques de votre application, je ne vais pas trop m'attarder sur elles. Mais je soulignerai que Cloud Firestore supporte les [requêtes composées](https://firebase.google.com/docs/firestore/query-data/queries).

Un dernier changement notable par rapport à la RTDB avant de passer à autre chose : les priorités ne sont plus une chose. Puisque Firestore supporte correctement le tri et l'interrogation, ils ont opté pour supprimer le champ `.priority` que vous pouviez trouver dans les documents RTDB de Firestore.

Cependant, si vous souhaitez toujours trier vos documents par id pour une raison quelconque, Firestore fournit la méthode `FieldPath#documentId()` exactement à cet effet.

### Règles de sécurité

Les règles de sécurité dans Firestore se sont un peu détériorées, à mon avis. Cependant, pour ceux qui sont familiers avec Firebase Storage, vous vous sentirez comme chez vous. Google a fusionné sa technologie de règles de base de données avec le reste de GCP.

D'autre part, pour ceux qui viennent d'un monde JSON avec la RTDB, la nouvelle syntaxe des règles de Firestore est un peu compliquée. Si vous déployez des règles dans votre build CI, vous devrez soit les éditer dans la console Firebase puis copier les règles dans votre éditeur local, soit les éditer dans un fichier txt. Beurk.

Voici à quoi ressemble l'ensemble de règles le plus simple possible :

Google a en fait une [documentation surprenamment bonne sur les règles de sécurité](https://firebase.google.com/docs/firestore/security/secure-data) — j'ai personnellement pu résoudre presque tous mes problèmes simplement en lisant les docs. Je vais tout de même passer en revue quelques pièges du point de vue du développeur RTDB (en supposant que vous avez au moins parcouru les docs).

Tout d'abord, le mot-clé `read` est un tableau de `get` et `list`, et le mot-clé `write` est un tableau de `create`, `update` et `delete`. Chaque mot-clé est explicite sauf pour `list` — il s'applique aux requêtes, ce qui signifie **pas** un seul « get ». Chacun de ces mots-clés peut être utilisé individuellement, mais les mots-clés `read` et `write` ont été fournis pour plus de commodité.

Sur une note connexe, vous finirez généralement par diviser vos mots-clés `write` pour permettre la suppression. Par exemple, l'utilisation de l'objet `request` pour vérifier la validité de l'écriture échoue si un utilisateur essaie de supprimer les données en question. De plus, si vous vérifiez si quelqu'un est un propriétaire, vous avez introduit une faille de sécurité. N'importe qui peut s'ajouter, puisque les nouvelles données sont vérifiées au lieu des anciennes.

Voici quelques règles d'exemple pour mettre ces mots en code :

Il y a une autre différence majeure du point de vue du développeur RTDB : l'évaluation des règles est superficielle par défaut. Cela s'aligne bien avec le modèle de (sous)collection, mais nécessite un petit changement de mentalité.

Par exemple, la variable `request` ne contient **pas** d'informations sur son document parent. Au début, je voulais vérifier à partir d'un document à l'intérieur d'une sous-collection si un document parent avait un certain champ. Mais bien sûr, cela ne fonctionne pas, car la sous-collection est juste un lien à l'intérieur du document parent.

Parce que les règles sont superficielles, vous devez être prudent lorsque vous utilisez l'opérateur double étoile (`variable=**`) puisque ses ressources ne contiendront pas d'informations sur le document parent. De plus, il y a quelques bizarreries avec la variable :

### FirebaseUI

Maintenant que vous avez une compréhension complète des capacités de Cloud Firestore ainsi que de ses différences et améliorations par rapport à la RTDB, examinons comment nous pouvons mettre tout cela ensemble pour construire une interface utilisateur.

[FirebaseUI](https://github.com/firebase/FirebaseUI-Android) se compose de plusieurs composants, y compris [auth](https://github.com/firebase/FirebaseUI-Android/blob/master/auth/README.md) et [storage](https://github.com/firebase/FirebaseUI-Android/blob/master/storage/README.md), mais nous nous concentrerons sur le module [firestore](https://github.com/firebase/FirebaseUI-Android/blob/master/firestore/README.md).

Dans la section sur les requêtes, j'ai mentionné à plusieurs reprises que FirebaseUI pourrait nous aider. Nous allons commencer par voir comment nous pouvons améliorer la méthode `toObjects()` de `QuerySnapshot`.

Il y a deux problèmes principaux avec l'utilisation de la méthode `toObjects()` :

1. Les performances vont être médiocres, surtout avec de grandes listes. À chaque mise à jour que votre `EventListener` reçoit, Firestore va recréer chaque objet — modifié ou non — en une seule fois en utilisant la réflexion. Aïe.
2. Il n'y a pas de personnalisation disponible. Par exemple, j'aime que mes objets de modèle aient un champ `ref` afin que je puisse facilement les mettre à jour plus tard. Cependant, je ne veux pas réellement stocker la référence dans la base de données car cela serait une duplication inutile.

Bien que vous puissiez penser, « eh bien, je vais simplement créer une liste et la mettre à jour chaque fois que de nouveaux objets arrivent », FirebaseUI fait exactement cela pour vous afin que vous n'ayez pas à écrire de code standard.

`FirestoreArray` — comme il est aptement nommé — est un tableau de snapshots de Firestore convertis en vos objets de modèle POJO. Son constructeur prend une `Query` Firestore, un `SnapshotParser<`;T>, et éventuellement, des options de requête. Il commence à écouter les données chaque fois que vous ajoutez un ou plusieurs `ChangeEventLi`steners et arrêtera automatiquement d'écouter lorsque le dernier écouteur est supprimé.

Le `ChangeEventListener` vous notifiera lorsque chaque objet change, lorsqu'une mise à jour complète a été traitée et lorsqu'une erreur se produit. Le `SnapshotParser<`;T> a une seule méthode — parseSn`apshot — qui est responsable de la conversion de chaque `DocumentSn`apshot en votre modèle POJO de type T.

Puisque `FirestoreArray` implémente `List<`;T> , cette configuration vous permet d'écouter facilement les mises à jour de vos objets de modèle avec un minimum de tracas.

En termes de performance, `FirestoreArray` utilise le `LruCache` natif d'Android pour analyser paresseusement les objets au besoin. Pour l'instant, nous avons défini la taille maximale du cache à `100`, mais si vous pensez avoir besoin d'une taille de cache plus grande (ou plus petite), nous aimerions connaître vos cas d'utilisation dans un [problème GitHub](https://github.com/firebase/FirebaseUI-Android/issues/new).

Puisque ceci est Firebase**UI**, nous vous permettons de mapper facilement votre `FirestoreArray` à un `RecyclerView` avec le `FirestoreRecyclerAdapter` et ses `FirestoreRecyclerOptions`.

Il y a quelques options intéressantes pour le recycleur, notamment la possibilité de passer un `LifecyleOwner` des composants d'architecture Android avec lequel nous gérerons automatiquement le cycle de vie du `FirestoreArray` pour vous.

D'accord, c'était beaucoup de mots. Voici à quoi cela ressemblerait une fois tout assemblé avec les composants d'architecture tout en prenant en compte les états d'authentification :

### Autres détails

Pour les développeurs web, Firestore est livré avec un support hors ligne complet, contrairement à la RTDB qui n'avait… rien ? Oui. Vive le support hors ligne en tant que citoyen de première classe pour toutes les plateformes mobiles !

De plus, si vous souhaitez des informations supplémentaires sur la migration de la RTDB vers Cloud Firestore, comme comment garder vos données synchronisées pendant la période de transition, vous trouverez de la documentation [ici](https://firebase.google.com/docs/firestore/firestore-for-rtdb).

### Conclusion

J'espère que vous avez apprécié cette plongée en profondeur dans la nouvelle base de données de Firebase et que vous êtes prêt à commencer à migrer vos applications. N'hésitez pas à me poser des questions ou à demander des clarifications ! Et si vous avez trouvé cet article utile, n'hésitez pas à me donner quelques applaudissements 👏.

Si vous avez apprécié les citations critiquant la RTDB, voici une dernière citation pour votre plaisir :

> Les gens ont fait fonctionner [la RTDB] pour des applications de production, mais ils forcent un carré dans un trou rond. - Eric Kryski

Aïe, ça brûle ! Bien que la RTDB ait pu être un feu de forêt incontrôlable, Cloud Firestore est une flamme puissamment puissante que vous pouvez manier avec un but pour **construire de meilleures applications** !

[**Cloud Firestore | Firebase**](https://firebase.google.com/docs/firestore/)  
[_Utilisez notre base de données NoSQL flexible et évolutive pour stocker et synchroniser des données pour le développement côté client et côté serveur._firebase.google.com](https://firebase.google.com/docs/firestore/)