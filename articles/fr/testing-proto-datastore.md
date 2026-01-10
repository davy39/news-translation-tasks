---
title: Comment tester Proto DataStore
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-04-08T20:54:23.000Z'
originalURL: https://freecodecamp.org/news/testing-proto-datastore
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/alexander-schimmeck-QX0SWFpB2ho-unsplash.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
seo_title: Comment tester Proto DataStore
seo_desc: 'In a previous article, I described how you can use Proto DataStore in your
  application. I wrote that article as part of my experience in using Proto DataStore
  in one of my applications.

  Following that, I wanted to see what it would be like to write t...'
---

[Dans un article précédent](https://medium.com/proandroiddev/android-proto-datastore-should-you-use-it-36ae997d00f2), j'ai décrit comment vous pouvez utiliser Proto DataStore dans votre application. J'ai écrit cet article dans le cadre de mon expérience d'utilisation de Proto DataStore dans [l'une de mes applications](https://play.google.com/store/apps/details?id=com.tomerpacific.todo).

Par la suite, je voulais voir à quoi ressemblerait l'écriture de tests pour le Proto DataStore dans cette application en utilisant les connaissances que j'ai acquises.

La recherche en ligne pour obtenir des conseils n'a pas fourni beaucoup de soulagement, alors j'ai pensé que je partagerais mes connaissances pour ceux qui pourraient être à la recherche de cela. Dans le pire des cas, ce serait pour ma progéniture.

Dans ma recherche, j'ai trouvé [cet article](https://medium.com/androiddevelopers/datastore-and-testing-edf7ae8df3d8), mais il se concentre principalement sur le test du Preferences DataStore et non sur le Proto DataStore. Il indique cependant que :

> « Cependant, gardez à l'esprit que vous pouvez utiliser ce matériel pour configurer les tests de [**Proto DataStore**](https://developer.android.com/codelabs/android-proto-datastore#0), car cela serait très similaire aux Preferences. »

Mais après l'avoir suivi, j'ai découvert qu'en dehors des dépendances, il n'y a pas beaucoup de similitudes ici et vous devez introduire une logique séparée pour tester votre propre Proto DataStore.

## Installation

Dans le fichier build.gradle de votre application, ajoutez les dépendances suivantes :

```groovy
dependencies {
  ///.....
  androidTestImplementation "androidx.compose.ui:ui-test-junit4:$compose_version"
  debugImplementation "androidx.compose.ui:ui-test-manifest:$compose_version"
}
```

**`$compose_version`** est la variable que vous avez définie dans votre fichier build.gradle au niveau du projet.

Ensuite, allez dans votre répertoire **`androidTest`** et créez un nouveau fichier. Généralement, vous aurez une classe de repository qui interagit avec votre Proto DataStore, vous pouvez donc nommer ce fichier comme YourRepositoryClassNameTest. Nous utiliserons le nom **`MyRepositoryTest`**.

Avant de nous plonger dans le test du Proto DataStore lui-même, nous devons l'instancier. Si vous cherchez en ligne une quelconque documentation à ce sujet, elle est plutôt rare.

L'instanciation d'un Proto DataStore est utilisée avec le Context global comme suit (lorsqu'elle n'est pas utilisée dans un scénario de test) :

```kotlin
private val Context.myDataStore: DataStore<MyItem> by dataStore(
                 fileName = DATA_STORE_FILE_NAME,
                 serializer = MyItemSerializer
 )
```

Eh bien, vous ne pouvez pas faire cela à l'intérieur d'une classe de test, car, bien que vous puissiez copier-coller le code ci-dessus, **vous ne pourrez pas accéder** à l'objet DataStore. Vous pouvez obtenir le contexte de l'application comme ceci :

```kotlin
ApplicationProvider.getApplicationContext()
```

mais notre objet `myDataStore` ne sera pas disponible à travers lui.

Alors, que pouvons-nous faire ?

Dans l'article lié ci-dessus, il y a un exemple de la façon dont nous pouvons créer un Preference DataStore en utilisant la méthode [PreferenceDataStoreFactory.create](https://developer.android.com/reference/kotlin/androidx/datastore/preferences/core/PreferenceDataStoreFactory#create(androidx.datastore.core.handlers.ReplaceFileCorruptionHandler,kotlin.collections.List,kotlinx.coroutines.CoroutineScope,kotlin.Function0)).

```kotlin
fun create(    
            corruptionHandler: ReplaceFileCorruptionHandler<Preferences>? = null,    
            migrations: List<DataMigration<Preferences>> = listOf(),
            scope: CoroutineScope = CoroutineScope(Dispatchers.IO + SupervisorJob()),    
            produceFile: () -> File): DataStore<Preferences>
```

Mais puisque nous n'utilisons pas un Preference DataStore, cela ne fonctionnera pas pour nous. Ce qui fonctionnera, c'est d'utiliser la méthode [DataStoreFactory.create](https://developer.android.com/reference/kotlin/androidx/datastore/core/DataStoreFactory#create(androidx.datastore.core.Serializer,androidx.datastore.core.handlers.ReplaceFileCorruptionHandler,kotlin.collections.List,kotlinx.coroutines.CoroutineScope,kotlin.Function0)) comme ceci :

```kotlin
fun <T : Any?> create(    
	serializer: Serializer<T>,   
	corruptionHandler: ReplaceFileCorruptionHandler<T>? = null,    
	migrations: List<DataMigration<T>> = listOf(),    
	scope: CoroutineScope = CoroutineScope(Dispatchers.IO + SupervisorJob()),     produceFile: () -> File): DataStore<T>
```

Il y a plusieurs arguments pour cette méthode (et certains ont des valeurs par défaut), mais nous n'avons pas besoin de tous les passer. Nous allons passer :

* Notre classe de serializer
* Une méthode lambda pour créer le fichier pour notre Proto DataStore

```kotlin
dataStore = DataStoreFactory.create(   
		produceFile = {                	
        	testContext.dataStoreFile(TEST_DATA_STORE_FILE_NAME)            		},            
        serializer = MyItemSerializer 
      )
```

Nous obtenons le `testContext` par :

```kotlin
private val testContext: Context = ApplicationProvider.getApplicationContext()
```

## Comment tester le DataStore

Ayant créé notre Proto DataStore avec succès, nous pouvons passer à l'écriture de quelques tests pour celui-ci. Gardez à l'esprit que vous avez une classe de repository qui reçoit l'instance du Proto DataStore en tant que dépendance, donc après avoir créé le Proto DataStore, nous devons créer une instance de notre classe de repository.

```kotlin
 private val repository = MyRepository(datastore)
```

Tout d'abord, créons un test pour vérifier l'état initial de notre Proto DataStore. Le Proto DataStore lui-même expose un flux que nous pouvons utiliser.

```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
    @Test
    fun repository_testFetchInitialState() {
        runTest {
            testScope.launch {
                val dataStoreObject = repository.myFlow.first()
                // Insérez ici ce que nous voulons vérifier à partir de notre
                // Proto DataStore. Par exemple, un flag dont la valeur initiale est false
                assert(dataStoreObject.myFlag == false)  
            }
        }
    }
```

⚠️ Vous avez peut-être remarqué cela plus tôt, mais nous utilisons une **annotation OptIn** ici. Cela est dû au fait que (actuellement) les API que nous utilisons sont expérimentales et doivent être marquées comme telles lorsque nous les utilisons.

Puisque nous accédons au flux de notre `DataStore`, nous devons l'envelopper dans notre `testScope`. `TestScope` est créé en faisant :

```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
private val dispatcher = TestCoroutineDispatcher()
@OptIn(ExperimentalCoroutinesApi::class)
private val testScope = TestCoroutineScope(dispatcher)
```

Exécutez-le et profitez de votre premier test Proto DataStore.

C'était amusant pendant environ deux secondes.

Faisons quelque chose de plus significatif.

Imaginez que notre Proto DataStore contient une liste d'objets et que nous voulons tester son état lorsque nous ajoutons un élément.

```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
    @Test
    fun repository_testAdditionOfItem() {
        runTest {
            testScope.launch {
              //1
               val item: MyItem = MyItem.newBuilder().setItemId(UUID.randomUUID().toString())
                    .setItemDescription(TEST_ITEM_DESCRIPTION).build()
                //2
                repository.updateItem(item)

                //3
                val items = repository.myFlow.first().itemsList
                assert(items.size == 1)

                //4
                assert(items[0].itemDescription.equals(TEST_ITEM_DESCRIPTION))
            }
        }
    }
```

1. Nous créons un élément de test en utilisant l'API exposée par le protobuff
2. Nous ajoutons cet élément au Proto DataStore en utilisant une méthode que nous avons exposée sur la classe MyRepository
3. Nous récupérons la liste des éléments à partir du flux exposé par le Proto DataStore
4. Nous nous assurons que l'élément trouvé dans le Proto DataStore correspond à l'élément que nous avons créé précédemment

## Votre DataStore a une fuite

Si vous essayez d'exécuter les tests ci-dessus en une seule fois, vous recevrez bientôt une erreur pendant l'exécution :

> Il y a plusieurs DataStores actifs pour le même fichier : /data/user/0/com.example.app/files/datastore/dataStore_filename.pb. Vous devez soit maintenir votre DataStore comme un singleton, soit confirmer qu'il n'y a pas deux DataStores actifs sur le même fichier (en confirmant que la portée est annulée).

Cela pose problème. Nous n'avons créé qu'une seule instance de DataStore dans notre classe de test.

Que se passe-t-il ici ?

Parce que nous n'utilisons pas [le délégué de propriété](https://developer.android.com/topic/libraries/architecture/datastore#preferences-create) pour créer notre DataStore (ce qui signifie Context.datastore), il n'est pas garanti que notre objet DataStore soit un singleton chaque fois que nous y accédons.

Pour contourner ce scénario, j'ai découvert qu'une approche consiste à supprimer et à recréer le DataStore pour chaque cas de test. Pour supprimer le DataStore, nous pouvons faire ceci :

```kotlin
@After
fun cleanup() {
  File(testContext.filesDir, "datastore").deleteRecursively()
}
```

et avant chaque test, nous le recréons :

```kotlin
@Before
 fun setup() {
    dataStore = DataStoreFactory.create(
        produceFile = {
            testContext.dataStoreFile(TEST_DATA_STORE_FILE_NAME)
        },
        serializer = MyItemSerializer
    )
 }
```

Pour voir un exemple complet, vous pouvez aller [ici](https://github.com/TomerPacific/Todo/blob/master/app/src/androidTest/java/com/tomerpacific/todo/TodoItesmRepositoryTest.kt).

Dans cet article, je voulais montrer les grandes lignes de la façon dont un Proto DataStore peut être testé.

Bien que j'aie passé en revue deux cas de test, selon votre DataStore et les types que vous y avez configurés, il pourrait y avoir plus de cas de test et de scénarios à écrire. Les blocs de construction sont là, vous devez simplement les adapter à vos besoins.