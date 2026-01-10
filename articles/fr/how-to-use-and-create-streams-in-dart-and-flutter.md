---
title: Comment utiliser et créer des flux à partir de zéro en Dart et Flutter – un
  guide pour débutants
subtitle: ''
author: Daniel Asaboro
co_authors: []
series: null
date: '2024-03-14T13:37:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-and-create-streams-in-dart-and-flutter
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/stream-controller-1.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
seo_title: Comment utiliser et créer des flux à partir de zéro en Dart et Flutter
  – un guide pour débutants
seo_desc: "Programming can be a rollercoaster ride. It catapults you from feeling\
  \ like a genius to feeling utterly clueless, and back again — all in the blink of\
  \ an eye. \nWhat's even more wild is that this cycle repeats itself countless times\
  \ throughout the day..."
---

La programmation peut être une montagne russe. Elle vous propulse de l'impression d'être un génie à celle d'être complètement perdu, et vice versa – tout cela en un clin d'œil.

Ce qui est encore plus surprenant, c'est que ce cycle se répète d'innombrables fois au cours de la journée, et pendant toute votre carrière en tant que développeur logiciel.

Outre mon expérience personnelle, une illustration parfaite de ce phénomène qui me vient à l'esprit est le cas de cet utilisateur Reddit qui a partagé ses difficultés il y a quelques mois :

![Un utilisateur Reddit partage sa frustration avec les flux Flutter, les contrôleurs de flux et les websockets et leur fonctionnement.](https://cdn.hashnode.com/res/hashnode/image/upload/v1709365581794/7085351c-088b-4c10-91ac-9ba947ca3fbd.png)
_Un utilisateur Reddit partage sa frustration avec les flux Flutter, les contrôleurs de flux et les websockets et leur fonctionnement._

**Les flux sont** l'un de ces concepts qui peuvent vous faire passer de "_Wow, je suis si intelligent 😈_" à "_Je suis si stupide 🤢, je devrais probablement être à la ferme_". De nombreux développeurs les trouvent difficiles à comprendre, en particulier les nouveaux développeurs Dart et Flutter.

Bien que les flux puissent être complexes, ils ne sont pas si compliqués qu'ils soient impossibles à apprendre. Si vous y consacrez suffisamment de dévouement et de pratique, vous pouvez les maîtriser, une compétence qui pourrait devenir nécessaire tôt ou tard.

Cela est dû au fait que les flux sont fondamentaux, et de nombreuses bibliothèques et SDK Dart basées sur Flutter (comme Firebase, les capteurs de périphériques, certaines techniques de gestion d'état, et même les isolats Dart) en dépendent fortement. Par conséquent, apprendre à utiliser les flux efficacement améliorera sans aucun doute vos compétences en développement.

## Ce que vous allez apprendre

Lorsque vous aurez terminé la lecture, vous devriez être capable de :

* Comprendre ce que sont les flux et ce qu'ils ne sont pas, reconnaître les scénarios optimaux pour les utiliser dans vos applications Dart et Flutter, et identifier les situations où d'autres approches peuvent être plus appropriées.
* Créer des flux spécifiques personnalisés en Dart et utiliser des techniques avancées pour les transformer selon les exigences de votre application et pour améliorer les performances.
* Mettre en œuvre des stratégies pour résoudre les défis de performance courants associés aux flux, garantir que vos applications fonctionnent de manière fluide dans diverses conditions, et bien plus encore.

## Prérequis : Que devez-vous savoir ?

Avant de commencer et pour une compréhension facile, vous devez avoir une compréhension de base des sujets et concepts suivants :

1. **Code asynchrone** : Familiarisez-vous avec les principes de la programmation asynchrone, comment ils diffèrent des programmes synchrones. Comprenez comment les techniques asynchrones contribuent aux performances, les concepts clés comme les futurs, async/await, les rappels et les boucles d'événements pour un langage à thread unique.
2. **Dart** : Assurez-vous d'avoir une connaissance pratique du langage de programmation Dart, y compris la syntaxe, les types de données, les variables, les fonctions, les classes et une compréhension de base de la gestion des exceptions.
3. **Framework Flutter** : Bien que ce ne soit pas strictement nécessaire, avoir une compréhension de base de Flutter et de ses composants clés peut être bénéfique. Familiarisez-vous avec les widgets Flutter, les techniques de gestion d'état, la navigation et le cycle de vie des widgets pour mieux intégrer les flux dans vos applications Flutter.

## Table des matières

Bien que je vous encourage à lire chacune des sections dans l'ordre où elles ont été écrites, n'hésitez pas à sauter à toute section qui vous intéresse si vous comprenez la section qui la précède.

* [Qu'est-ce qu'un flux en Dart ?](#heading-quest-ce-quun-flux-en-dart)
* [Applications réelles des flux](#heading-applications-reelles-des-flux)
* [Comment fonctionnent les flux](#heading-comment-fonctionnent-les-flux) ?
* [Comment travailler avec les flux en Dart](#heading-comment-travailler-avec-les-flux-en-dart)
* [Comment créer votre propre flux en Dart](#heading-comment-creer-votre-propre-flux-en-dart)
* [Et la gestion des erreurs avec les flux](#heading-et-la-gestion-des-erreurs-avec-les-flux) ?
* [Tout ce qui change n'a pas besoin d'être un flux](#heading-tout-ce-qui-change-na-pas-besoin-detre-un-flux)
* [Conclusion](#heading-il-suffit-de-commencer)
* [Défi rapide](#heading-defi-rapide)

## Qu'est-ce qu'un flux en Dart ?

Si vous lisez cet article, il y a des chances que vous compreniez les opérations asynchrones – vous savez comment utiliser les futurs avec Async-Await. Et bien que vous n'ayez peut-être pas une idée de leur fonctionnement interne ([la boucle d'événements de concurrency](https://dart.dev/language/concurrency)), vous les avez probablement utilisés pour récupérer un résultat JSON d'une API distante.

Les flux sont similaires aux futurs en ce sens qu'ils fonctionnent tous deux de manière asynchrone.

L'une des différences clés est qu'une fois qu'un futur est appelé et commence, il peut soit retourner une valeur, soit générer une erreur et puis s'arrêter. Un flux, en revanche, peut livrer une série de valeurs (données et erreurs) en continu (plus sur cela plus tard).

Il est donc techniquement correct de dire que les futurs sont des flux à valeur unique ou des opérations de flux à réponse unique. Si une méthode ou une fonction doit retourner plus d'un résultat à différents intervalles de temps, ou nécessite des mises à jour continues à traiter de la même manière, vous devriez probablement vous pencher sur les flux.

## Applications réelles des flux

Au-delà des applications évidentes comme la récupération de données depuis Firestore ou la gestion des messages Firebase dans une application de chat, envisagez des scénarios tels que la recherche de périphériques Bluetooth disponibles ou la recherche de points d'accès WiFi.

![Une capture d'écran montrant le processus de recherche de wifi pour illustrer une application réelle des flux.](https://cdn.hashnode.com/res/hashnode/image/upload/v1710138803116/9ae58be0-c0d8-47f8-ae76-668b7ac6c8e3.png)

Dans de tels cas, lorsque des données deviennent disponibles (une nouvelle connexion de point d'accès ou un périphérique disponible), un événement est émis via un flux. Ensuite, les auditeurs abonnés au flux reçoivent et traitent ces événements de manière asynchrone.

C'est similaire à écouter des chansons sur Spotify et regarder des vidéos sur des plateformes comme YouTube et Netflix. Le serveur musical de YouTube ou Spotify divise astucieusement les chansons ou les vidéos en petits morceaux gérables – un flux d'octets afin que vous n'ayez pas à attendre que l'application termine le téléchargement. D'où le nom : Streaming.

Imaginez attendre qu'une chanson se télécharge avant de pouvoir la jouer !!!

### Votre requête HTTP Get utilise des flux en interne

Dart attend simplement patiemment jusqu'à ce que le flux se termine et retourne ensuite toutes les données en une fois sous la forme d'un futur terminé.

```dart
//code précédent supprimé pour plus de concision

  client.getUrl(uri)
    .then((req) => req.close())
    .then((response) => response.transform(utf8.decoder).join())
    .then((value) => jsonDecode(value) as List<dynamic>)
    .then((json) => json.map((map) => Todo.fromJson(map)).toList())
    .then((retrievedTodos) {
      for (final todo in retrievedTodos) {
        print('Todo: ${todo.title}, Completed: ${todo.completed}');
      }
    })
    .catchError((e) {
      print('Error: $e');
    })
    .whenComplete(() {
      client.close();
    });

// section uniquement pour illustration
```

Voici une version Async-Await qui est commentée :

```dart
import 'dart:convert';
import 'dart:io';

class Todo {
  final int id;
  final String title;
  final bool completed;

  Todo({
    required this.id,
    required this.title,
    required this.completed,
  });

  factory Todo.fromJson(Map<String, dynamic> json) {
    return Todo(
      id: json['id'],
      title: json['title'],
      completed: json['completed'],
    );
  }
}

void main() async {
  final uri = Uri.parse('https://jsonplaceholder.typicode.com/todos');
  final client = HttpClient();

  try {
    final request = await client.getUrl(uri);
    final response = await request.close();

    final jsonString = await response.transform(utf8.decoder).join();
    final json = jsonDecode(jsonString) as List<dynamic>;

    final retrievedTodos = json.map((map) => Todo.fromJson(map)).toList();

    for (final todo in retrievedTodos) {
      print('Todo: ${todo.title}, Completed: ${todo.completed}');
    }
  } catch (e) {
    print('Error: $e');
  } finally {
    client.close();
  }
}

```

Il ne devrait pas être surprenant que le téléchargement d'un fichier utilise également cette technique.

Généralement, vous aurez besoin de flux lorsque vous traitez quoi que ce soit impliquant une forme de "connexion" selon Remi Rouselet, l'auteur du package Provider et Riverpod.

Si c'est clair, passons à la pratique.

## Comment fonctionnent les flux ?

Les flux fonctionnent de manière similaire aux tapis roulants que l'on voit couramment dans les aéroports.

Ils agissent comme des canaux qui transportent en douceur divers articles d'une extrémité à l'autre. Généralement, vous ajoutez des bagages ou des sacs sur un tapis roulant et ils sont transportés le long de son chemin. Vous pouvez ajouter des données ou des événements à un flux de la même manière.

L'endroit où vous mettez les articles est appelé la source.

Alors que les articles se déplacent le long du tapis roulant, les travailleurs postés le long du tapis observent et interagissent avec eux. Ces travailleurs représentent les auditeurs ou les abonnés au flux.

Ils peuvent examiner, catégoriser ou manipuler les articles en fonction de critères spécifiques.

Certains travailleurs peuvent ne s'intéresser qu'à des types spécifiques d'articles et laisser passer les autres, tandis que d'autres peuvent modifier ou combiner des articles lorsqu'ils passent par leur poste. Cela reflète le concept de filtrage, de transformation ou d'agrégation d'événements dans le flux, que nous aborderons plus tard dans cet article.

## Comment travailler avec les flux en Dart

Vous avez deux choix :

* utiliser un flux qui existe déjà, ou
* en créer un à partir de zéro.

Il est généralement plus facile d'utiliser un flux qui existe déjà plutôt que d'en créer un nouveau juste pour l'utiliser ailleurs dans votre application. Commençons donc par l'idée d'utiliser un flux de données déjà créé.

Mais d'abord, vous devez savoir qu'il existe deux types de flux :

1. Un flux à abonnement unique
2. Un flux de diffusion

### Un flux à abonnement unique est le défaut en Dart

Un abonnement unique ne permet qu'un seul auditeur/abonné pendant toute sa durée de vie. Peu importe si vous annulez un ancien abonnement – vous ne pouvez pas vous abonner à nouveau. Toute tentative de réabonnement entraînera l'erreur `Bad State` :

```dart
import 'dart:async';

void main() {
  // Créer un StreamController
  StreamController<int> streamController = StreamController<int>();

  // Écouter le flux
  StreamSubscription<int> subscription = streamController.stream.listen(
    (int data) {
      print('Données reçues : $data');
    },
  );

  // Annuler l'abonnement
  subscription.cancel();

  // Essayer d'écouter à nouveau le flux avec le même abonnement
  try {
    subscription = streamController.stream.listen(
      (int data) {
        print('Données reçues à nouveau : $data');
      },
    );
  } catch (e) {
    print('Erreur : $e'); // Gérer l'erreur
  }

  // Fermer le contrôleur de flux
  streamController.close();
}
```

![Le message d'erreur que vous recevez du flux est : "Erreur : Bad State: Stream has already been Listened to".](https://cdn.hashnode.com/res/hashnode/image/upload/v1710052410984/6a1556d2-d90c-4878-b180-c1bcf427d667.png)

Cela est utile lorsque l'ordre dans lequel les informations arrivent est critique et que tout désalignement rendra les données illisibles ou impossibles à interpréter, comme dans le cas d'une requête HTTP GET, de la lecture d'un fichier ou du traitement de messages dans une application de chat.

De plus, un flux à abonnement unique est le type de flux le plus efficace car il ne commence à générer des événements que lorsqu'il a un auditeur, et il cesse d'envoyer des événements lorsque l'auditeur se désabonne, même s'il reste encore des événements à émettre.

Mais que faire si vous voulez plus d'un seul auditeur ?

Que faire si vous devez partager le même flux de données entre plusieurs composants ou widgets dans votre application ? Que faire si une fonctionnalité collaborative implique des mises à jour en temps réel, et que diverses parties de votre application doivent réagir simultanément – que faites-vous ?

### C'est là qu'intervient le flux de diffusion

Contrairement à un flux à abonnement unique, un flux de diffusion permet un nombre quelconque d'auditeurs. Ce qui est intéressant, c'est qu'il déclenche ses événements lorsqu'ils sont prêts, sans vérifier s'il y a des auditeurs ou non.

Ce n'est pas très efficace, n'est-ce pas ? Il est donc essentiel de faire preuve de prudence avec les flux de diffusion car ils peuvent entraîner des fuites de mémoire s'ils ne sont pas gérés correctement. Après tout, ne dit-on pas que de grands pouvoirs impliquent de grandes responsabilités ?

Les flux de diffusion sont bien adaptés aux situations où chaque événement peut être traité sans dépendre des événements précédents et peut être traité par l'utilisateur dès qu'il est reçu – par exemple, les nouvelles de dernière heure, les scores sportifs ou les alertes météo.

![English Premier League Livescore utilisé pour illustrer un flux de notification qui ne dépend pas des événements précédents](https://cdn.hashnode.com/res/hashnode/image/upload/v1710138971106/3b426c19-ca45-45f8-9ddd-ead192f34e0f.png)

Il est intéressant de noter que tous les abonnés sont désabonnés une fois qu'un événement `done` est déclenché. Ensuite, tout nouvel abonné recevra simplement l'événement terminé et cessera d'écouter.

```dart
import 'dart:async';

void main() {
  // Créer un StreamController
  StreamController<int> streamController = StreamController<int>();

  // Écouter le flux
  streamController.stream.listen(
    (int data) {
      print('Données reçues : $data');
    },
    onDone: () {
      print('Le flux est terminé.');
    },
  );

  // Ajouter des données au flux
  streamController.add(1);
  streamController.add(2);

  // Fermer le contrôleur de flux
  streamController.close();

  // Essayer de s'abonner à nouveau après la fermeture du flux

  Future.delayed(Duration.zero, () {
    try {
      streamController.stream.listen(
        (int data) {
          print('Nouvel abonné a reçu des données : $data');
        },
        onDone: () {
          print('Nouvel abonné a reçu l'événement terminé.');
        },
      );
    } catch (e) {
      print(e);
      print('Le nouvel abonné n'écoute plus.');
    }
  });
}
```

![Résultat après l'exécution du code ci-dessus. D'abord 1 et 2 sont imprimés, puis le flux est marqué comme terminé. Mais si vous essayez de l'écouter à nouveau, il dira que le flux a déjà été écouté](https://cdn.hashnode.com/res/hashnode/image/upload/v1710052967862/464e7a7e-ab6d-431c-8e70-09dc629a8dfd.png)

Et si nous créions nos propres flux auxquels d'autres peuvent s'abonner ?

## Comment créer votre propre flux en Dart

Actuellement, il existe trois façons de créer un nouveau flux en Dart :

1. Transformer des flux existants
2. Utiliser un générateur asynchrone
3. Utiliser des contrôleurs de flux

### Comment créer des flux en transformant des flux existants

Je n'ai pas vraiment pensé à ces méthodes comme une méthode autonome pour créer des flux car elles nécessitent de dépendre d'un autre flux. Mais en parcourant la documentation Dart, j'ai réalisé que nous créons en fait une nouvelle entité de flux chaque fois que nous transformons un autre flux. C'est assez méta, en fait...

```dart
import 'dart:async';

void main() {
  // Créer un flux d'entiers
  final Stream<int> originalStream = Stream<int>.fromIterable([1, 2, 3, 4, 5]);

  // Transformer le flux original en utilisant map()
  final Stream<int> transformedStream = originalStream.map((int value) {
    return value * 2; // Doubler chaque entier
  });

  // Écouter le flux transformé
  final StreamSubscription<int> subscription =
      transformedStream.listen((int value) {
    print('Valeur transformée : $value');
  });

  // Fermer l'abonnement et les flux après un délai
  Future.delayed(Duration(seconds: 1), () {
    subscription.cancel();
  });
}
```

Le résultat :

![Résultat du code ci-dessus où chaque donnée de flux est multipliée par deux donnant : Valeur transformée : 2, 4, 6 etc](https://cdn.hashnode.com/res/hashnode/image/upload/v1709919319018/3fb5a20c-7dfc-4d11-bfc5-fda51ff4fd93.png)
_Résultat du code ci-dessus où chaque donnée de flux est multipliée par deux_

Cet exemple obtient un flux de données Firebase Firestore et le mappe à l'UI :

```dart


//code supprimé pour plus de concision

class FirestoreService {
  final CollectionReference _collectionReference =
      FirebaseFirestore.instance.collection('messages');

  Stream<List<Map<String, dynamic>>> getMessages() {
    return _collectionReference.snapshots().map((snapshot) =>
        snapshot.docs.map((doc) => doc.data() as Map<String,     		dynamic>).toList());
  }
  
  Future<void> addMessage(String message, String sender) async {
  // votre code...
  }
  
  // autres méthodes supprimées pour plus de concision
}

void main() {
  final firestoreService = FirestoreService();

  // Écouter les messages
  final Stream<List<Map<String, dynamic>>> messageStream =
      firestoreService.getMessages();
  messageStream.listen((messages) {
    print('Messages reçus : $messages');
  });

  // Ajouter un nouveau message
  firestoreService.addMessage('Hello Firestore!', 'Dart User');
}

// autre code pour plus de concision
```

D'autres méthodes de transformation courantes sont `take()`, `expand()`, et `where()`. Si votre application exige des transformations plus avancées (par exemple, convertir la réponse HTTP Get en utilisant le décodage UTF-8) au-delà de ces méthodes standard, explorez la [classe de transformation de flux](https://api.dart.dev/stable/3.3.0/dart-async/StreamTransformer-class.html) pour des capacités supplémentaires.

### Comment créer des flux en utilisant des générateurs

Ici, vous utilisez ce qu'on appelle la fonction générateur asynchrone.

C'est une fonction marquée avec `async *` au lieu de `async` pour la différencier des futurs. Cette fonction s'exécute de manière asynchrone et envoie une valeur chaque fois qu'elle voit un mot-clé `yield`, mais elle n'arrêtera pas l'exécution du corps de la fonction comme le ferait un `return`.

```dart
import 'dart:async';

// Définir une fonction générateur asynchrone
Stream<int> countStream(int max) async* {
  for (int i = 1; i <= max; i++) {
    // Yield chaque valeur de manière asynchrone
    await Future.delayed(Duration(seconds: 1));
    yield i;
  }
}

void main() {
  // Créer un flux en utilisant la fonction générateur asynchrone
  Stream<int> stream = countStream(6);

  // S'abonner au flux
  stream.listen((value) {
    print('Reçu : $value');
  }, onDone: () {
    print('Flux terminé');
  });
}
```

**Voici comment cela fonctionne :**

Le flux est créé lorsque vous appelez ou invoquez la fonction.

Mais il ne commence à s'exécuter que lorsque vous écoutez le flux car les flux sont chargés de manière paresseuse. Il peut émettre des événements sur le flux en utilisant des instructions `yield` ou `yield*` jusqu'à ce que la fonction retourne, puis le flux se ferme.

#### Comment un yield est-il différent d'un return et comment fonctionne-t-il ?

En Dart, "return" est utilisé pour quitter immédiatement une fonction et retourner une valeur à l'appelant. Lorsqu'une fonction rencontre une instruction return, elle termine son exécution et passe le contrôle à l'appelant, ainsi que la valeur de retour spécifiée.

Les appels ultérieurs à la fonction commenceront l'exécution depuis le début.

```dart
import 'dart:async';

// Fonction qui retourne un Future<int> après un délai
Future<int> fetchUserData() async {
  await Future.delayed(Duration(seconds: 2)); // Simuler un délai
  return 42; // Données utilisateur simulées
}

void main() async {
  print('Récupération des données utilisateur...');

  try {
    // Lancement de l'opération asynchrone et attente du résultat
    int userData = await fetchUserData();
    print('Données utilisateur reçues : $userData');
  } catch (error) {
    print('Erreur lors de la récupération des données utilisateur : $error');
  }

  print('Poursuite avec d'autres tâches...');
}
```

En revanche, lorsqu'une fonction rencontre une instruction "yield" dans un générateur asynchrone, elle suspend son exécution, retourne la valeur spécifiée par "yield" à l'appelant et préserve l'état de la fonction. Cela permet à la fonction de reprendre l'exécution là où elle s'était arrêtée lorsque la valeur suivante est demandée.

```dart
import 'dart:async';

// Fonction générateur asynchrone
Stream<int> countStream(int max) async* {
  for (int i = 1; i <= max; i++) {
    // Simuler un délai asynchrone
    await Future.delayed(Duration(seconds: 1)); 
    yield i; // Yield chaque valeur dans la séquence
  }
}

void main() async {
  // Créer un flux en utilisant la fonction générateur asynchrone
  Stream<int> stream = countStream(5);

  // S'abonner au flux en utilisant une boucle await for
  await for (int value in stream) {
    print('Reçu : $value');

    // Simuler un traitement supplémentaire
    await Future.delayed(Duration(milliseconds: 500));
  }

  print('Flux terminé');
}
```

Dans l'exemple ci-dessus, la fonction `countStream()` est une fonction générateur qui produit une séquence d'entiers de 0 à 4 de manière paresseuse en utilisant le mot-clé "yield".

Chaque fois que la fonction est appelée, elle retourne la valeur suivante dans la séquence sans générer toute la séquence à l'avance. Cela peut être utile pour économiser de la mémoire et traiter efficacement de grands ensembles de données.

Notez que le `Stream` créé par une fonction `async*` est toujours un flux à abonnement unique. Cela est dû au fait qu'une fonction `async*` est destinée à s'exécuter normalement jusqu'à ce qu'elle soit terminée, similaire au flux de contrôle normal d'une fonction unique (asynchrone).

Que faire si vous voulez un flux de diffusion – que faites-vous ?

Indice : J'ai déjà répondu à cette question dans cet article.

Enfin, une chose intéressante que la [documentation officielle](https://dart.dev/articles/libraries/creating-streams#:~:text=It's%20rare%20to%20have%20an,from%20other%20asynchronous%20event%20sources.) a soulignée, et que je n'avais pas vraiment remarquée, est que :

> Il est rare qu'une fonction `async*` construise un flux à partir de rien. Elle doit obtenir ses données de quelque part, et le plus souvent, ce quelque part est un autre flux.

Cela vous rend toujours dépendant d'autres flux. Que faire si vous devez aller plus loin et commencer à partir de zéro ? C'est là qu'intervient la classe `StreamController`.

### Comment créer des flux en utilisant des contrôleurs de flux

Les contrôleurs de flux sont bien adaptés aux situations où les événements de votre flux proviennent de différentes parties de votre programme, et/ou ne peuvent pas être obtenus à partir d'un autre flux ou futur.

Quelques exemples qui me viennent à l'esprit sont la gestion des événements d'entrée utilisateur, la manipulation de données provenant de sources diverses, ou la création d'événements personnalisés au sein de votre application comme les mises à jour d'état, les notifications de progression ou les alertes système.

Les contrôleurs de flux sont de bas niveau, comme je comprends. Ils ne vous donnent pas seulement un flux, ils vous donnent des moyens d'ajouter des événements à tout moment, y compris la [logique nécessaire pour gérer les auditeurs et la pause](https://api.dart.dev/stable/dart-async/StreamController-class.html).

```dart
import 'dart:async';

void main() {
  // Créer un contrôleur de flux pour gérer les événements d'entrée utilisateur
  StreamController<String> userInputController = StreamController<String>();

  // Écouter les événements d'entrée utilisateur
  userInputController.stream.listen((String userInput) {
    print('Entrée utilisateur : $userInput');
  });

  // Simuler des événements d'entrée utilisateur
  userInputController.add('Bonjour');
  userInputController.add('Monde');

  // Créer un contrôleur de flux personnalisé pour les notifications de progression
  StreamController<double> progressController = StreamController<double>();

  // Écouter les notifications de progression
  progressController.stream.listen((double progress) {
    print('Progression : $progress');
  });

  // Simuler des notifications de progression
  for (double i = 0; i <= 1; i += 0.2) {
    progressController.add(i);
  }

  // Créer un contrôleur de flux personnalisé pour les alertes système
  StreamController<String> systemAlertController = StreamController<String>();

  // Écouter les alertes système
  systemAlertController.stream.listen((String alert) {
    print('Alerte système : $alert');
  });

  // Simuler des alertes système
  systemAlertController.add('Surcharge système détectée !');
  systemAlertController.add('Connexion à la base de données perdue !');

  // Fermer tous les contrôleurs de flux une fois terminé
  userInputController.close();
  progressController.close();
  systemAlertController.close();
}
```

Il dispose de quatre méthodes de rappel :

1. `onListen`
2. `onCancel`
3. `onResume`
4. `onPause`

Si vous voulez savoir quand le flux a été abonné, passez un gestionnaire onListen au paramètre `onListen` lorsque vous créez le `StreamController`.

```dart
import 'dart:async';

void main() {
  // Créer un StreamController avec un rappel onListen
  StreamController<int> streamController = StreamController<int>(
    onListen: () {
      print('Le flux a été abonné.');
    },
  );

  // Écouter le flux
  streamController.stream.listen((int data) {
    print('Données reçues : $data');
  });

  // Ajouter des données au flux
  streamController.add(1);
  streamController.add(2);
  streamController.add(3);

  // Fermer le contrôleur de flux une fois terminé
  streamController.close();
}
```

Le rappel `onListen` est appelé lorsque le flux obtient son premier abonné. `onCancel`, en revanche, est déclenché lorsque le contrôleur perd son dernier abonné.

```dart
import 'dart:async';

void main() {
  // Créer un StreamController avec un rappel onCancel
  StreamController<int> streamController = StreamController<int>(
    onCancel: () {
      print('Le dernier abonné a annulé, le contrôleur de flux est maintenant inactif.');
    },
  );

  // Écouter le flux
  StreamSubscription<int> subscription = streamController.stream.listen((int data) {
    print('Données reçues : $data');
  });

  // Ajouter des données au flux
  streamController.add(1);
  streamController.add(2);

  // Annuler l'abonnement
  subscription.cancel();

  // Ajouter plus de données au flux après avoir annulé l'abonnement
  streamController.add(3);

  // Fermer le contrôleur de flux
  streamController.close();
}

//##Note: 

//Lorsque vous utilisez async* et yield*, 
//vous créez une fonction qui peut produire des valeurs de manière asynchrone,
//potentiellement en générant un nouveau flux de valeurs à chaque appel.

//Lorsque vous retournez un flux,
//vous passez une référence à un objet de flux existant sans
//nécessairement générer de nouvelles valeurs ou modifier le flux lui-même.
```

Souvenez-vous lorsque j'ai dit que les StreamControllers sont de bas niveau ?

Ce que cela signifie généralement, c'est que vous avez le contrôle sur tout. Cependant, cela vient avec la responsabilité de mettre en œuvre des fonctionnalités que les méthodes de création de flux de plus haut niveau fournissent directement.

### Une telle fonctionnalité est connue sous le nom de "respecter la pause"

Lorsque l'abonnement à un flux d'un générateur async* est mis en pause, la fonction générateur se met automatiquement en pause à une instruction yield, garantissant qu'aucun nouvel événement n'est émis jusqu'à ce que l'abonnement reprenne.

Mais avec les StreamControllers, les événements continuent d'être générés et mis en mémoire tampon pendant les pauses. Si le code produisant les événements ne respecte pas la pause, la taille du tampon peut croître indéfiniment, entraînant des problèmes de mémoire potentiels.

De plus, si l'auditeur cesse d'écouter peu après la pause, tous les efforts déployés pour créer le tampon sont gaspillés. Grossièrement inefficace, n'est-ce pas ? Imaginez une opération de longue durée.

Voici comment résoudre ce problème :

```dart
Stream<int> integerCounter(Duration interval, [int? maxCount]) {
  late StreamController<int> controller;

  void onListenHandler() {
    //code supprimé pour plus de concision;
  }
  void onPauseHandler() {
    //code supprimé pour plus de concision;
  }
  void onResumeHandler() {
    //code supprimé pour plus de concision;
  }
  void onCancelHandler() {
    //code supprimé pour plus de concision;
  }

  controller = StreamController<int>(
    onListen: onListenHandler,
    onPause: onPauseHandler,
    onResume: onResumeHandler,
    onCancel: onCancelHandler,
  );

  return controller.stream;
}
```

### Une autre est quelque chose que j'appelle "Synchronisation Pause-Abonnement"

Ce terme fait référence à la synchronisation entre l'état d'abonnement et de pause d'un StreamController. Si les états d'abonnement et de pause changent simultanément, seul le rappel `onListen` ou `onCancel` est déclenché.

C'est pourquoi il est conseillé de mettre en œuvre tous les auditeurs disponibles—`onListen`, `onCancel`, `onPause`, et `onResume`—pour atténuer les problèmes potentiels et garantir un fonctionnement correct. De cette manière, vous pouvez surveiller efficacement les changements dans l'état de pause et éviter les bugs difficiles à suivre qui peuvent survenir en raison de comportements inattendus.

Oh, et n'oubliez jamais de disposer de votre contrôleur :

```dart
import 'dart:async';

void main() {
  // Créer un StreamController
  StreamController<int> streamController = StreamController<int>();

  // Écouter le flux
  StreamSubscription<int> subscription = streamController.stream.listen((int data) {
    print('Données reçues : $data');
  });

  // Ajouter des données au flux
  streamController.add(1);
  streamController.add(2);

  // Disposer de l'abonnement et du contrôleur de flux
  subscription.cancel();
  streamController.close(); // appeler la méthode close pour disposer
}
```

## Et la gestion des erreurs dans les flux ?

Lorsque des erreurs surviennent dans un flux, le flux les gère de manière similaire à la façon dont il gère les événements de données—en informant les auditeurs par le biais d'événements d'erreur. Généralement, les flux démontrent deux comportements clairs en réaction aux erreurs :

1. Le flux notifie le premier événement d'erreur puis arrête le traitement ultérieur.
2. Le flux notifie les événements d'erreur(s) mais continue de livrer les événements suivants.

Prenons chacun à la fois.

### Arrêt après la première erreur

Dans ce scénario, le flux s'arrête après avoir rencontré la première erreur, mais il fournit des informations sur le problème initial et interrompt toute transmission d'événement ultérieure. Cela est utile lorsque l'ordre d'importance est critique et que toute pièce manquante suffit à rendre le fichier entier inutilisable.

```dart
import 'dart:async';

void main() {
  // Créer un StreamController
  StreamController<int> streamController = StreamController<int>();

  // Écouter le flux
  StreamSubscription<int> subscription = streamController.stream.listen(
    (int data) {
      print('Données reçues : $data');
    },
    onError: (error) {
      print('Erreur survenue : $error');
    },
    onDone: () {
      print('Flux terminé.');
    },
  );

  // Ajouter des données au flux
  streamController.add(1);
  streamController.add(2);
  streamController.addError('Erreur : Quelque chose a mal tourné'); // Simuler une erreur
  streamController.add(3);

  // Fermer le contrôleur de flux
  streamController.close();
}
```

D'après ce que vous avez appris, cela est particulier aux fonctions générateurs asynchrones ou aux flux à abonnement unique. Que faire si votre cas est différent, par exemple, si vous voulez continuer après avoir rencontré une erreur dans un flux, que faites-vous ?

### Continuer après la première erreur

Contrairement aux scénarios où les flux s'arrêtent après la première erreur, continuer après les erreurs permet au flux de maintenir son flux. Cela fournit des informations et des mises à jour continues aux consommateurs en aval.

Cette approche est inestimable dans les scénarios où le fonctionnement ininterrompu du flux est primordial, comme le traitement de données en temps réel ou les systèmes de surveillance continue. Les flux qui continuent après les erreurs offrent de la résilience et de l'adaptabilité, garantissant que les informations critiques ne sont pas perdues en raison d'incidents isolés.

Examinons un exemple :

```dart
import 'dart:async';

void main() async {
  // Créer un contrôleur de flux
  StreamController<int> streamController = StreamController<int>();

  // Générer des nombres de manière asynchrone avec un délai de 1 seconde
  int count = 0;
  Timer.periodic(Duration(seconds: 1), (Timer timer) {
    // Simuler des erreurs pour la démonstration
    if (count % 3 == 0) {
      streamController.addError('Erreur : Échec de la génération du nombre $count');
    } else {
      streamController.add(count);
    }
    count++;
  });

  // Écouter le flux
  streamController.stream.listen(
    (int data) {
      print('Données reçues : $data');
    },
    onError: (error) {
      print('Erreur survenue : $error');
    },
  );
}

```

## Tout ce qui change n'a pas besoin d'être un flux

Les flux offrent une grande fonctionnalité en émettant des événements (valeurs de données ou d'erreur) sans se soucier de la manière dont ils sont consommés, ce qui donne aux développeurs la flexibilité d'écrire du code avec un faible couplage et une grande extensibilité. Mais ils ne doivent pas être liés à tout ce qui change.

Selon Randal Schwartz, [la gestion d'état est un excellent exemple](https://www.reddit.com/r/FlutterDev/comments/1586sfg/whats_a_real_world_use_case_of_a_dart_stream/) de cela.

Je l'ai contacté pour être sûr de comprendre sa position, et voici ce qu'il dit :

> "La différence clé, comme Remi me l'a clarifié, est qu'il y a une place pour les flux lorsque chaque événement doit être inclus, par rapport à la gestion d'état typique, où seul l'état le plus récent (et la notification lorsqu'il change) est pertinent. Si quelque chose passe rapidement de 1 à 2 à 3, mais que vous reconstruisez ensuite en fonction de 3, c'est suffisant."

En d'autres termes, vous ne vous souciez pas des intermédiaires, seulement des plus récents.

L'état est quelque chose que vous devez gérer tout au long du cycle de vie de votre application. Si cela est mal fait, vos applications peuvent souffrir de problèmes de performance et de lag en raison de reconstructions excessives ou à grande échelle.

Minimisez donc les mises à jour inutiles et reconstruisez uniquement les composants qui ont vraiment besoin d'être reconstruits pour optimiser les performances globales. N'oubliez pas que Dart est mono-threadé.

## Il suffit de commencer

Je ne m'attends pas à ce que vous compreniez tous les détails présentés ici en une seule fois, même si j'ai consacré d'innombrables heures sur plusieurs semaines pour peaufiner ce tutoriel. Ne vous sentez donc pas sous pression.

Au lieu de cela, n'hésitez pas à marquer cette page pour lorsque vous serez prêt à continuer. Si quelque chose semble peu clair, veuillez vous référer aux crédits et aux ressources recommandées ou vous pouvez me contacter sur Twitter.

La vérité indéniable est que vous pouvez consommer des tutoriels et des vidéos sans fin, mais la vraie confiance vient lorsque vous appliquez vos connaissances à des problèmes réels et les résolvez (j'en ai trois pour vous ci-dessous).

Abordons ce tutoriel comme vous utiliseriez un flux pour gérer une grande ressource – divisez-le en morceaux plus petits et digestes et traitez-les à votre convenance. Peu importe si c'est irrégulier, assurez-vous simplement de le traiter.

Si une confusion survient, partagez-la dans les commentaires, tweetez-moi sur Twitter (maintenant X), ou contactez-moi via les messages directs. Je serai ravi de vous aider à les résoudre et à apporter quelques éclaircissements. Au revoir !

## Défi rapide

1. Comment implémenteriez-vous le style de frappe de ChatGPT avec des flux ?
2. Supposons que vous recevez une nouvelle tâche. Sur pression d'un bouton, votre application doit :  
– télécharger un fichier compressé,  
– extraire le fichier dans un   
– trouver un fichier binaire exécutable, et l'exécuter,  
– retourner une liste de répertoires qui doivent être ajoutés au PATH.

		Comment le résoudriez-vous avec ce que vous avez appris jusqu'à présent dans ce tutoriel ?

3.  Comment pouvez-vous utiliser des flux pour communiquer lorsqu'un utilisateur est en train de taper ou non ?

### Crédits :

1. [Flutter Stream Basics for Beginners](https://medium.com/flutter-community/flutter-stream-basics-for-beginners-eda23e44e32f) par Dane Mackier.
2. [Streams: Asynchronous Programming with Dart](https://ptyagicodecamp.github.io/streams-asynchronous-programming-with-dart.html) par Priyanka Tyagi
3. [Difference between `await for` and `listen`](https://stackoverflow.com/questions/42611880/difference-between-await-for-and-listen-in-) répondu sur StackOverflow.
4. [Simple Beginners Guide to Streams | Flutter and Dart Stream Basics](https://www.youtube.com/watch?v=53jIxLiCv2E) par FilledStacks [Vidéos YouTube]
5. [Streams: API documentation](https://api.flutter.dev/flutter/dart-async/Stream-class.html) sur Flutter dot Dev