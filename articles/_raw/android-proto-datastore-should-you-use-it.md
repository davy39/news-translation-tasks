---
title: Android Proto DataStore – Should You Use It?
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
seo_title: null
seo_desc: "A few years back, Google announced the DataStore, which is a replacement\
  \ for the tried and true SharedPreferences. \nIf you use or have used SharedPreferences\
  \ in your applications, you might be thinking of making the switch. But as with\
  \ everything, th..."
---

A few years back, Google announced the DataStore, which is a replacement for the tried and true SharedPreferences. 

If you use or have used SharedPreferences in your applications, you might be thinking of making the switch. But as with everything, the main question here is: what is going to be the cost in development?

[There are benefits](https://developer.android.com/codelabs/android-proto-datastore#3) for using DataStore, but only the **Proto DataStore** allows you to save objects while providing type safety. 

If you look at the [documentation](https://developer.android.com/topic/libraries/architecture/datastore#proto-datastore) for Proto DataStore, you will find that it is a bit outdated and missing some crucial steps when working with it. So that is why, in this article, we are going to go over how to integrate Proto DataStore into your application and show that it’s not that big of a hassle to use it.

## What is DataStore?

Jetpack DataStore has two variants:

* Preferences DataStore
* Proto DataStore

We won’t be discussing the first, due to it’s similarity to SharedPreferences and also the fact that is has been covered widely. So now let’s understand what the Proto in Proto DataStore means.

Proto is the name Google chose to represent [Protocol Buffers](https://protobuf.dev/). These are (Google’s) mechanism that help you serialize structured data. They are not coding language-specific and in general, you define the type of data that you wish to work with and then code is generated that helps you read and write your data.

✋ We will be using the Proto 3 version in this article.

How does that definition look like?

```proto
message MyItem {
    string itemName = 1;
    int32 itemId = 2;
}
```

First, you define an object with the message keyword. Inside it, you list the fields associated with that object. The numbers at the end of each field are used to identify the field itself and **cannot be changed once being set and the object is in use**.

But what if we wanted to have multiple objects in our .proto file? Assuming the objects are related to one another, you can do this simply by adding more message objects:

```proto
message MyItem {
    string itemName = 1;
    int32 itemId = 2;
}

message MyListOfItems {
   repeated MyItem items = 1;
}
```

Notice that above we have added another message object that relies on the MyItem object defined above. If you want to define a list of objects, you need to use the **repeated** keyword.

## How to Set Up Proto DataStore

To get started, you'll need to add the following dependencies to your application level build.gradle:

```groovy
 implementation "androidx.datastore:datastore-preferences:1.0.0"
 implementation  "com.google.protobuf:protobuf-javalite:3.18.0"
```

Then, you will need to create a proto directory inside your project. This directory needs to be a sibling of the Java folder in your project structure. 

Inside of the proto directory, you will be creating a .proto file. This file is responsible for generating the data types you wish to store in Proto DataStore.

![Image](https://www.freecodecamp.org/news/content/images/2023/12/1.jpg)

Inside the proto directory, create a file with the .proto extension. Our .proto file will hold objects representing a Todo list (what else?). So we will call our file **todo.proto** and it will look like this:

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

Notice how we defined two message objects:

1. TodoItem – that defines a todo item
2. TodoItems – that defines a list of TodoItem objects

Next, build the project so that classes will be generated for TodoItem and TodoItems.

After our data objects have been defined, we need to create a class to serialize them. This class will tell the DataStore how to read/write our objects.

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

Let’s review what we have in this class:

1. When we declare the class, we need to implement the **Serializer<T>** interface with our object as the type (T)
2. We define a default value for the serializer in case the file is not created
3. We override the readFrom/writeTo methods and we make sure to have our object as the data type there

We have our .proto file with our data types and our serializer, so the next step is to instantiate the DataStore. We do this by using the property delegate created by dataStore, which requires giving a filename where our data will be saved and our serializer class (which we defined above).

```kotlin
private const val DATA_STORE_FILE_NAME = "todo.pb"

private val Context.todoItemDatastore: DataStore<TodoItems> by dataStore(
    fileName = DATA_STORE_FILE_NAME,
    serializer = TodoItemSerializer,
)
```

This piece of code needs to reside at the top of a class of your choosing above the definition of the class itself. That is:

```kotlin
private const val DATA_STORE_FILE_NAME = "todo.pb"

private val Context.todoItemDatastore: DataStore<TodoItems> by dataStore(
    fileName = DATA_STORE_FILE_NAME,
    serializer = TodoItemSerializer,
)

class YourClassName {

}
```

To access this object in the rest of our application, we will need to use a context. An example is to use the application context in your viewmodel class:

```kotlin
class MyViewModel(application: Application): AndroidViewModel(application) {

   val todoDataStore = application.todoItemDataStore
   //...
}
```

## How to Use Kotlin Flow

Now that we have gone through setting up everything we need for our DataStore, we'll discuss how we are actually going to interact with it. We'll want to read and write data to/from it. But the way we can do so is different from what you may be familiar with from SharedPreferences.

The DataStore we defined above has a data field that exposes a Flow for the properties we defined in our DataStore.

🚰 If you are not familiar with flows, [this](https://developer.android.com/kotlin/flow) is a good place to start.

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

The code above shows how you can define a Flow that collects data from the Proto DataStore. A catch block was added in case an exception occurs. You can place this logic in the class where you defined your DataStore and use it like so in your viewmodel:

```kotlin
val todoItemsFlow: LiveData<TodoItems> = todoItemsRepository.todoItemFlow.asLiveData()

```

Notice how we converted our Flow to LiveData. We did this for two reasons:

1. Flows can stay active regardless of the activity/fragment that uses them
2. LiveData is something familiar to many developers, and I wanted to make this example as approachable as possible

To be able to do this, you need to add the following dependency to your build.gradle file:

```groovy
implementation "androidx.lifecycle:lifecycle-livedata-ktx:2.6.2"
```

In your activity/fragment class, you can observe this live data like so:

```kotlin
myViewModel.todoItemFlow.observe(LocalLifecycleOwner.current) { todoItems ->
                // Logic to access data from DataStore
            }
```

## Why and When to Use DataStore

After everything we reviewed, it’s time to talk about the elephant in the room. Should you go ahead and use DataStore (either Preferences or Proto) in your existing or next project?

In my opinion, the answer should be **Yes**. Besides the fact that Google is moving away from SharedPreferences, DataStore offers plenty of benefits to help you focus on your application and not the persistence of your data. 

It’s safe to interact with the DataStore from the UI thread (as it moves work to I/O automatically), and it forces you to use Flow (if you haven’t still) and enjoy all the benefits within. There is also an option to migrate easily from SharedPreferences to Preferences DataStore.

If you are contemplating using Room instead of Proto DataStore, well that depends on your use case. If the amount of data you are going to save (or persist) is rather small and won’t require partial updating, the Proto DataStore is the way to go. If you have a larger data set or one that may be complex, you should opt for using Room instead.

If you want to see how all this code looks like in an application, you can see it here:

%[https://github.com/TomerPacific/Todo]

If you want to read other articles I have written, you can see them here:

%[https://github.com/TomerPacific/MediumArticles]

Thanks for reading!

References:

* [Protocol Buffers Documentation (proto 3)](https://protobuf.dev/programming-guides/proto3/)
* [Working With Proto DataStore Codelab](https://developer.android.com/codelabs/android-proto-datastore#0)
* [DataStore Documentation](https://developer.android.com/topic/libraries/architecture/datastore)

