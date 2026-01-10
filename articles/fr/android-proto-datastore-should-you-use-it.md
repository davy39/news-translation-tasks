---
title: Android Proto DataStore – Devriez-vous l'utiliser ?
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-01-02T19:52:43.000Z'
originalURL: https://freecodecamp.org/news/android-proto-datastore-should-you-use-it
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/niklas-ohlrogge-j-0olYcaihg-unsplash.jpg
tags:
- name: Android
  slug: android
- name: protocol-buffers
  slug: protocol-buffers
seo_title: Android Proto DataStore – Devriez-vous l'utiliser ?
seo_desc: "A few years back, Google announced the DataStore, which is a replacement\
  \ for the tried and true SharedPreferences. \nIf you use or have used SharedPreferences\
  \ in your applications, you might be thinking of making the switch. But as with\
  \ everything, th..."
---

Il y a quelques années, Google a annoncé le DataStore, qui est un remplacement pour le fidèle SharedPreferences.

Si vous utilisez ou avez utilisé SharedPreferences dans vos applications, vous pourriez envisager de faire la transition. Mais comme pour tout, la question principale ici est : quel sera le coût en développement ?

[Il y a des avantages](https://developer.android.com/codelabs/android-proto-datastore#3) à utiliser DataStore, mais seul le **Proto DataStore** vous permet de sauvegarder des objets tout en fournissant une sécurité de type.

Si vous regardez la [documentation](https://developer.android.com/topic/libraries/architecture/datastore#proto-datastore) pour Proto DataStore, vous constaterez qu'elle est un peu obsolète et manque de certaines étapes cruciales lors de son utilisation. C'est pourquoi, dans cet article, nous allons passer en revue comment intégrer Proto DataStore dans votre application et montrer que ce n'est pas si compliqué à utiliser.

## Qu'est-ce que DataStore ?

Jetpack DataStore a deux variantes :

* Preferences DataStore
* Proto DataStore

Nous ne discuterons pas de la première, en raison de sa similitude avec SharedPreferences et aussi du fait qu'elle a été largement couverte. Alors maintenant, comprenons ce que signifie le Proto dans Proto DataStore.

Proto est le nom que Google a choisi pour représenter [Protocol Buffers](https://protobuf.dev/). Ce sont (les) mécanismes de Google qui vous aident à sérialiser des données structurées. Ils ne sont pas spécifiques à un langage de codage et en général, vous définissez le type de données avec lequel vous souhaitez travailler, puis un code est généré qui vous aide à lire et écrire vos données.

👋 Nous utiliserons la version Proto 3 dans cet article.

À quoi ressemble cette définition ?

```proto
message MyItem {
    string itemName = 1;
    int32 itemId = 2;
}
```

Tout d'abord, vous définissez un objet avec le mot-clé message. À l'intérieur, vous listez les champs associés à cet objet. Les nombres à la fin de chaque champ sont utilisés pour identifier le champ lui-même et **ne peuvent pas être modifiés une fois définis et l'objet est en cours d'utilisation**.

Mais que faire si nous voulions avoir plusieurs objets dans notre fichier .proto ? En supposant que les objets sont liés les uns aux autres, vous pouvez le faire simplement en ajoutant plus d'objets message :

```proto
message MyItem {
    string itemName = 1;
    int32 itemId = 2;
}

message MyListOfItems {
   repeated MyItem items = 1;
}
```

Remarquez que ci-dessus nous avons ajouté un autre objet message qui repose sur l'objet MyItem défini ci-dessus. Si vous voulez définir une liste d'objets, vous devez utiliser le mot-clé **repeated**.

## Comment installer Proto DataStore

Pour commencer, vous devrez ajouter les dépendances suivantes à votre fichier build.gradle au niveau de l'application :

```groovy
 implementation "androidx.datastore:datastore-preferences:1.0.0"
 implementation  "com.google.protobuf:protobuf-javalite:3.18.0"
```

Ensuite, vous devrez créer un répertoire proto à l'intérieur de votre projet. Ce répertoire doit être un frère du dossier Java dans la structure de votre projet.

À l'intérieur du répertoire proto, vous allez créer un fichier .proto. Ce fichier est responsable de la génération des types de données que vous souhaitez stocker dans Proto DataStore.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/1.jpg)

À l'intérieur du répertoire proto, créez un fichier avec l'extension .proto. Notre fichier .proto contiendra des objets représentant une liste de tâches (quoi d'autre ?). Nous appellerons donc notre fichier **todo.proto** et il ressemblera à ceci :

```proto
syntax = "proto3";

option java_package = "com.yourPackageName.todo";
option java_multiple_files = true;

message TodoItem {
  string itemId = 1;
  string itemDescription = 2;
}

message TodoItems {
  repeated TodoItem items = 1;
}
```

Remarquez comment nous avons défini deux objets message :

1. TodoItem – qui définit un élément de tâche
2. TodoItems – qui définit une liste d'objets TodoItem

Ensuite, construisez le projet afin que des classes soient générées pour TodoItem et TodoItems.

Après avoir défini nos objets de données, nous devons créer une classe pour les sérialiser. Cette classe indiquera au DataStore comment lire/écrire nos objets.

```kotlin
// 1
object TodoItemSerializer: Serializer<TodoItems> {
   // 2
    override val defaultValue: TodoItems = TodoItems.getDefaultInstance()
    // 3
    override suspend fun readFrom(input: InputStream): TodoItems {
        try {
            return TodoItems.parseFrom(input)
        } catch (exception: InvalidProtocolBufferException) {
            throw CorruptionException("Cannot read proto.", exception)
        }
    }
    // 3
    override suspend fun writeTo(
        t: TodoItems,
        output: OutputStream
    ) = t.writeTo(output)
}
```

Passons en revue ce que nous avons dans cette classe :

1. Lorsque nous déclarons la classe, nous devons implémenter l'interface **Serializer<T>** avec notre objet comme type (T)
2. Nous définissons une valeur par défaut pour le sérialiseur au cas où le fichier n'est pas créé
3. Nous remplaçons les méthodes readFrom/writeTo et nous nous assurons d'avoir notre objet comme type de données là

Nous avons notre fichier .proto avec nos types de données et notre sérialiseur, donc l'étape suivante est d'instancier le DataStore. Nous le faisons en utilisant le délégué de propriété créé par dataStore, ce qui nécessite de donner un nom de fichier où nos données seront sauvegardées et notre classe de sérialiseur (que nous avons définie ci-dessus).

```kotlin
private const val DATA_STORE_FILE_NAME = "todo.pb"

private val Context.todoItemDatastore: DataStore<TodoItems> by dataStore(
    fileName = DATA_STORE_FILE_NAME,
    serializer = TodoItemSerializer,
)
```

Ce morceau de code doit résider en haut d'une classe de votre choix au-dessus de la définition de la classe elle-même. C'est-à-dire :

```kotlin
private const val DATA_STORE_FILE_NAME = "todo.pb"

private val Context.todoItemDatastore: DataStore<TodoItems> by dataStore(
    fileName = DATA_STORE_FILE_NAME,
    serializer = TodoItemSerializer,
)

class YourClassName {

}
```

Pour accéder à cet objet dans le reste de notre application, nous devrons utiliser un contexte. Un exemple est d'utiliser le contexte de l'application dans votre classe viewmodel :

```kotlin
class MyViewModel(application: Application): AndroidViewModel(application) {

   val todoDataStore = application.todoItemDataStore
   //...
}
```

## Comment utiliser Kotlin Flow

Maintenant que nous avons passé en revue la configuration de tout ce dont nous avons besoin pour notre DataStore, nous allons discuter de la manière dont nous allons réellement interagir avec lui. Nous voudrons lire et écrire des données vers/depuis celui-ci. Mais la manière dont nous pouvons le faire est différente de ce à quoi vous pourriez être habitué avec SharedPreferences.

Le DataStore que nous avons défini ci-dessus a un champ de données qui expose un Flow pour les propriétés que nous avons définies dans notre DataStore.

🚀 Si vous n'êtes pas familier avec les flows, [c'est](https://developer.android.com/kotlin/flow) un bon endroit pour commencer.

```kotlin
val todoItemFlow: Flow<TodoItems> = todoItemDataStore.data
        .catch { exception ->
            if (exception is IOException) {
                emit(TodoItems.getDefaultInstance())
            } else {
                throw exception
            }
        }
```

Le code ci-dessus montre comment vous pouvez définir un Flow qui collecte des données à partir du Proto DataStore. Un bloc catch a été ajouté au cas où une exception se produirait. Vous pouvez placer cette logique dans la classe où vous avez défini votre DataStore et l'utiliser comme suit dans votre viewmodel :

```kotlin
val todoItemsFlow: LiveData<TodoItems> = todoItemsRepository.todoItemFlow.asLiveData()

```

Remarquez comment nous avons converti notre Flow en LiveData. Nous l'avons fait pour deux raisons :

1. Les Flows peuvent rester actifs indépendamment de l'activité/fragment qui les utilise
2. LiveData est quelque chose de familier pour de nombreux développeurs, et je voulais rendre cet exemple aussi accessible que possible

Pour pouvoir faire cela, vous devez ajouter la dépendance suivante à votre fichier build.gradle :

```groovy
implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.6.2"
```

Dans votre classe d'activité/fragment, vous pouvez observer ces données en direct comme suit :

```kotlin
myViewModel.todoItemFlow.observe(LocalLifecycleOwner.current) { todoItems ->
                // Logique pour accéder aux données de DataStore
            }
```

## Pourquoi et quand utiliser DataStore

Après tout ce que nous avons passé en revue, il est temps de parler de l'éléphant dans la pièce. Devriez-vous utiliser DataStore (soit Preferences soit Proto) dans votre projet existant ou prochain ?

À mon avis, la réponse devrait être **Oui**. En plus du fait que Google s'éloigne de SharedPreferences, DataStore offre de nombreux avantages pour vous aider à vous concentrer sur votre application et non sur la persistance de vos données.

Il est sûr d'interagir avec le DataStore à partir du thread UI (car il déplace le travail vers I/O automatiquement), et il vous oblige à utiliser Flow (si vous ne l'avez pas encore fait) et à profiter de tous les avantages qu'il offre. Il existe également une option pour migrer facilement de SharedPreferences vers Preferences DataStore.

Si vous envisagez d'utiliser Room au lieu de Proto DataStore, cela dépend de votre cas d'utilisation. Si la quantité de données que vous allez sauvegarder (ou persister) est plutôt petite et ne nécessitera pas de mise à jour partielle, le Proto DataStore est la voie à suivre. Si vous avez un ensemble de données plus grand ou plus complexe, vous devriez opter pour l'utilisation de Room à la place.

Si vous voulez voir à quoi ressemble tout ce code dans une application, vous pouvez le voir ici :

%[https://github.com/TomerPacific/Todo]

Si vous voulez lire d'autres articles que j'ai écrits, vous pouvez les voir ici :

%[https://github.com/TomerPacific/MediumArticles]

Merci d'avoir lu !

Références :

* [Documentation Protocol Buffers (proto 3)](https://protobuf.dev/programming-guides/proto3/)
* [Travail avec Proto DataStore Codelab](https://developer.android.com/codelabs/android-proto-datastore#0)
* [Documentation DataStore](https://developer.android.com/topic/libraries/architecture/datastore)