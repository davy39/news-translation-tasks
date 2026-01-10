---
title: How to Test Proto DataStore
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
seo_title: null
seo_desc: 'In a previous article, I described how you can use Proto DataStore in your
  application. I wrote that article as part of my experience in using Proto DataStore
  in one of my applications.

  Following that, I wanted to see what it would be like to write t...'
---

[In a previous article](https://medium.com/proandroiddev/android-proto-datastore-should-you-use-it-36ae997d00f2), I described how you can use Proto DataStore in your application. I wrote that article as part of my experience in using Proto DataStore in [one of my applications](https://play.google.com/store/apps/details?id=com.tomerpacific.todo).

Following that, I wanted to see what it would be like to write tests for the Proto DataStore in that application using the knowledge I gained. 

Searching online for guidance didn’t provide much relief, so I figured I would share my knowledge for those that might be looking for it. In the worst case, it would be for my progeny.

In my search, I did find [this article](https://medium.com/androiddevelopers/datastore-and-testing-edf7ae8df3d8), but that focuses mostly on testing the Preferences DataStore and not the Proto DataStore. It does state that:

> “However, keep in mind you can use this material for setting up [**Proto DataStore**](https://developer.android.com/codelabs/android-proto-datastore#0) testing, as it would be very similar to Preferences.”

But having followed it, I found out that besides the dependencies, there aren’t many similarities here and you need to introduce separate logic to test your own Proto DataStore.

## Setting Things Up

In your application’s build.gradle file, add the following dependencies:

```groovy
dependencies {
  ///.....
  androidTestImplementation "androidx.compose.ui:ui-test-junit4:$compose_version"
  debugImplementation "androidx.compose.ui:ui-test-manifest:$compose_version"
}
```

**`$compose_version`** is the variable you defined in your project level build.gradle file.

Then, go to your **`androidTest`** directory and create a new file. Usually, you would have a repository class that interacts with your Proto DataStore, so you can name this file as YourRepositoryClassNameTest. We will use the name **`MyRepositoryTest`**.

Before we delve into testing the Proto DataStore itself, we need to instantiate it. If you go online to find any documentation on this, it is kind of sparse. 

Instantiating a Proto DataStore is used with the global Context like so (when not used in a testing scenario):

```kotlin
private val Context.myDataStore: DataStore<MyItem> by dataStore(
                 fileName = DATA_STORE_FILE_NAME,
                 serializer = MyItemSerializer
 )
```

Well, you can't do this inside of a test class, because, while you can copy-paste the above code, **you won’t be able to** **access** the DataStore object. You can get the application context like this:

```kotlin
ApplicationProvider.getApplicationContext()
```

but our `myDataStore` object won’t be available through it.

So, what can we do?

In the article linked above, there is an example of how we can create a Preference DataStore using the [PreferenceDataStoreFactory.create](https://developer.android.com/reference/kotlin/androidx/datastore/preferences/core/PreferenceDataStoreFactory#create(androidx.datastore.core.handlers.ReplaceFileCorruptionHandler,kotlin.collections.List,kotlinx.coroutines.CoroutineScope,kotlin.Function0)) method.

```kotlin
fun create(    
            corruptionHandler: ReplaceFileCorruptionHandler<Preferences>? = null,    
            migrations: List<DataMigration<Preferences>> = listOf(),
            scope: CoroutineScope = CoroutineScope(Dispatchers.IO + SupervisorJob()),    
            produceFile: () -> File): DataStore<Preferences>
```

But since we are not using a Preference DataStore, that won’t work for us. What will work is using the [DataStoreFactory.create](https://developer.android.com/reference/kotlin/androidx/datastore/core/DataStoreFactory#create(androidx.datastore.core.Serializer,androidx.datastore.core.handlers.ReplaceFileCorruptionHandler,kotlin.collections.List,kotlinx.coroutines.CoroutineScope,kotlin.Function0)) method like this:

```kotlin
fun <T : Any?> create(    
	serializer: Serializer<T>,   
	corruptionHandler: ReplaceFileCorruptionHandler<T>? = null,    
	migrations: List<DataMigration<T>> = listOf(),    
	scope: CoroutineScope = CoroutineScope(Dispatchers.IO + SupervisorJob()),     produceFile: () -> File): DataStore<T>
```

There are several arguments for this method (and some have default values), but we don’t need to pass all of them in. We will be passing:

* Our serializer class
* A lambda method for creating the file for our Proto DataStore

```kotlin
dataStore = DataStoreFactory.create(   
		produceFile = {                	
        	testContext.dataStoreFile(TEST_DATA_STORE_FILE_NAME)            		},            
        serializer = MyItemSerializer 
      )
```

We get the `testContext` by:

```kotlin
private val testContext: Context = ApplicationProvider.getApplicationContext()
```

## How to Test the DataStore

Having created our Proto DataStore successfully, we can move on to writing some tests for it. Keep in mind that you have a repository class that receives the instance of the Proto DataStore as a dependency, so after creating the Proto DataStore, we need to create an instance of our repository class.

```kotlin
 private val repository = MyRepository(datastore)
```

First, let’s create a test to check our initial Proto DataStore state. The Proto DataStore itself exposes a flow which we can use.

```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
    @Test
    fun repository_testFetchInitialState() {
        runTest {
            testScope.launch {
                val dataStoreObject = repository.myFlow.first()
                // Insert here whatever we want to assert from our
                // Proto DataStore. I.E. a flag whose initial value is false
                assert(dataStoreObject.myFlag == false)  
            }
        }
    }
```

☝️ You may have noticed this earlier, but we are using a **OptIn annotation** here. This is because (currently) the APIs which we are using are experimental and must be marked so when we use them.

Since we are accessing the flow of our `DataStore`, we need to wrap it in our `testScope`. `TestScope` is created by doing:

```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
private val dispatcher = TestCoroutineDispatcher()
@OptIn(ExperimentalCoroutinesApi::class)
private val testScope = TestCoroutineScope(dispatcher)
```

Run it and enjoy your first Proto DataStore test.

That was fun for about two seconds.

Let’s do something more meaningful.

Imagine our Proto DataStore has a list of objects inside of it and we want to test the state of it when we add an item to it.

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

1. We create a test item using the exposed API from the protobuff
2. We add this item to the Proto DataStore using a method we exposed on the MyRepository class
3. We grab the list of items from the flow the Proto DataStore exposes
4. We make sure that the item found in the Proto DataStore matches the item we created earlier

## Your DataStore Has a Leak in it

If you try to run the tests above in one go, you will soon receive an error during runtime:

> There are multiple DataStores active for the same file: /data/user/0/com.example.app/files/datastore/dataStore_filename.pb. You should either maintain your DataStore as a singleton or confirm that there is no two DataStore’s active on the same file (by confirming that the scope is cancelled).

Well, that is problematic. We only created one DataStore instance in our test class.

What is going on here?

Because we are not using [the property delegate](https://developer.android.com/topic/libraries/architecture/datastore#preferences-create) to create our DataStore (meaning Context.datastore), it isn’t ensured that our DataStore object is a singleton whenever we access it.

To circumvent this scenario, I have found out that one approach is to delete and recreate the DataStore for each test case. To delete the DataStore, we can do this:

```kotlin
@After
fun cleanup() {
  File(testContext.filesDir, "datastore").deleteRecursively()
}
```

and before every test, we recreate it:

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

To see a full example, you can go [here](https://github.com/TomerPacific/Todo/blob/master/app/src/androidTest/java/com/tomerpacific/todo/TodoItesmRepositoryTest.kt).

In this article, I wanted to show the outline of a how a Proto DataStore can be tested. 

While I went over two test cases, depending on your DataStore and the types you configured there, there could be more test cases and scenarios to write. The building blocks are there, you just have to adapt it to your needs.

