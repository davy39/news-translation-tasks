---
title: 'All about that architecture: exploring different architecture patterns and
  how to use them in your app'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-22T14:10:55.000Z'
originalURL: https://freecodecamp.org/news/kriptofolio-app-series-part-3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xtjCi9Hfi8W4ye54HM2Y0w.png
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: Architecture Components
  slug: architecture-components
- name: Cryptocurrency
  slug: cryptocurrency
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 3

  The most important thing to focus on when starting to build a new app is architecture.
  The biggest mistake you can make is to go with no architecture style at all.

  The topic of architecture choice h...'
---

By Andrius Baruckis

#### Kriptofolio app series - Part 3

The most important thing to focus on when starting to build a new app is architecture. The biggest mistake you can make is to go with no architecture style at all.

The topic of architecture choice has been quite controversial for the Android community in recent years. Even Google decided to get involved. In 2017 they proposed their own approach of standardized architecture by releasing Android Architecture Components. It was intended to make developers’ lives easier.

In this post, I am first going to discuss why we need to architect our apps. We will cover what options we have. Then we are going to learn how to do that. Rather than reinventing the wheel, we will use guidelines provided by the Android team.

This post was the hardest one for me to write because of my own lack of knowledge about it. First I had to study the topic of architecture really well to see the bigger picture. Now I am ready to share my findings with you.

### Series content

* [Introduction: A roadmap to build a modern Android app in 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Part 1: An introduction to the SOLID principles](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* [Part 2: How to start building your Android app: creating Mockups, UI, and XML layouts](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* Part 3: All about that architecture: exploring different architecture patterns and how to use them in your app (you’re here)
* [Part 4: How to implement Dependency Injection in your app with Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* [Part 5: Handle RESTful Web Services using Retrofit, OkHttp, Gson, Glide and Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### Why should you care about app architecture?

Usually when you start working with Android you end up writing most of the core business logic in activities or fragments. This happens to all new Android developers, including myself. All short tutorials and all samples suggest doing that. And actually, for small apps created for explanation, that works good enough.

However, try to do that on a real app which is constantly changing according to the users’ needs and expanding it with new features. Soon you will see that your coding experience is getting more and more painful. Everything becomes managed by so-called “God Classes” like activities or fragments. These have so many lines of code that you get lost easily.

Basically all your code starts to look like spaghetti where everything is mixed up. All the parts depend on each other. Then when new changes are required by the business, you are left with no choice but to rebuild the entire project. Also that’s the point where architecture questions start to appear.

### Is there a better way to structure your code?

Of course there is! The key for high quality code is to follow the SOLID principles. I talked about this in my previous post (not without a reason). You should also apply some architecture pattern for separation of concerns. In fact, separation of concerns should be your ultimate goal. It is the most significant point which indicates code quality. There are quite a few patterns out there for app architectures. The most well known are the classic three tier architectures such as:

* MVC: Model-View-Controller
* MVP: Model-View-Presenter
* MVVM: Model-View-ViewModel

All these patterns represent the main similar idea — to structure your project’s code in a way that it is separated by the different generic layers. Every layer has its own responsibility. That’s why your project becomes modular: separated code parts are more testable, and your app is flexible enough for continuous changes.

If we talk about each pattern individually, the topic becomes too broad. I am only going to introduce you to each one just so you can understand main differences.

### The Model-View-Controller (MVC) pattern

This pattern was the first iteration Android app architecture took back in the old times. It suggests that you separate your code to 3 different layers:

Model — the data layer. Responsible for handling the business logic and communication with the network and database layers.

View — the user interface (UI) layer. It’s a simple visualization of the data from the Model.

Controller — the logic layer, gets notified of the user behavior and updates the Model as needed.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DU4N6tj30K-cdILm.png)

This is the MVC schema. In it we can see that both the Controller and the View depend on the Model. The Controller updates the data. The View gets the data. However, the Model is separated and could be tested independently of the UI.

There are a few approaches of how to apply the MVC pattern. It’s quite confusing.

One is when activities and fragments act like the Controller. They are in charge of processing the data and updating the views. The problem with this architecture approach is that activities and fragments can become quite large and very difficult to test.

Another approach which seems more logical (and correct) is where activities and fragments should be the Views in the MVC world. The Controllers should be separate classes that don’t extend or use any Android class. Same for the Models.

Anyway if you investigate more about MVC, you will find out that when applied to an Android project, even in the correct way the code layers depend on each other. That’s why I would not recommend that you use it anymore for your next Android app.

### The Model-View-Presenter (MVP) pattern

After the first approach, which didn’t work, Android developers moved on and tried to use one of the most popular architectural patterns — MVP. This pattern represents a second iteration of architecture choice. This pattern became widely used and is still a recommended one. For anybody who starts Android development, it is easy to learn. Let’s have a look at its 3 separate layers roles:

Model — the data layer, which is the same as on MVC pattern. Responsible for handling the business logic and communication with the network and database layers.

View — the user interface (UI) layer. Displays the data and notifies the Presenter about user actions.

Presenter — retrieves the data from the Model, applies the UI logic and manages the state of the View, decides what to display, and reacts to user input notifications from the View. This is essentially the controller from MVC except that it is not at all tied to the View, just an interface.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-FvjLCU4hd5O1mjn.png)

MVP schema shows that the View and the Presenter are closely related. They need to have a reference to one another. Their relationship is defined in a `Contract` interface class.

This pattern has one significant but controllable disadvantage. The Presenter tends to expand to a huge all-knowing class if you are not careful enough and don’t break your code according to single responsibility principle. However, generally speaking, the MVP pattern offers a very good separation of concerns. It could be your main choice for your project.

### The Model-View-ViewModel (MVVM) pattern

MVVM pattern is the third iteration of the approach. It became the architecture pattern recommended by Android team with Android Architecture Components’ release. That’s why we will be focusing on learning this pattern most of all. Also I will be using it for “My Crypto Coins” app. As before, let’s take a look at its separate code layers:

Model — abstracts the data source. The ViewModel works with the Model to get and save the data.

View — that informs the ViewModel about the users’ actions.

ViewModel — exposes streams of data relevant to the View.

The difference compared to MVP pattern is that, in MVVM, the ViewModel does not hold a reference to the View as it is with the Presenter. In MVVM, the ViewModel exposes a stream of events to which various Views can bind. On the other hand, in the MVP case, the Presenter directly tells the View what to display. Let’s take a look at the MVVM schema:

![Image](https://cdn-media-1.freecodecamp.org/images/0*wgul-7f3_G5PcN8T.png)

In MVVM the View has a reference to ViewModel. ViewModel has no information about the View. There is a many-to-one relationship between View and ViewModel.

#### Comparison of MVC vs MVP vs MVVM

Here is a table which sums up all the patterns I talked about:

![Image](https://cdn-media-1.freecodecamp.org/images/0*IOIlEBcHQcJrTUks.png)

As you may have noticed, MVC is not so good compared to MVP and MVVM when building a modular and testable modern app. But each pattern has its own advantages and disadvantages. It is a good choice if it exactly fits your needs. I suggest that you investigate and learn more about all these patterns as it is worth it.

In the meantime, I will continue my project with the trending pattern in 2018, which is also pushed by Google — MVVM.

### Android Architecture Components

If you’re familiar with the Android application lifecycle, you know what a headache it can be to build an app that avoids all data flow problems and persistence and stability issues which usually appear during configuration change.

In 2017, the Android team decided we’d struggled enough. They assumed responsibility and introduced the Android Architecture Components framework. This finally lets you solve all these issues without complicating your code or even applying hacks to it.

Android Architecture Components is a collection of libraries that helps you design robust, testable, and maintainable apps. At the current moment when I am writing this blog post, it consists of these components:

* [Data Binding](https://developer.android.com/topic/libraries/data-binding) — declaratively bind observable data to UI elements
* [Lifecycles](https://developer.android.com/topic/libraries/architecture/lifecycle) — manage your activity and fragment lifecycles
* [LiveData](https://developer.android.com/topic/libraries/architecture/livedata) — notify views when underlying database changes
* [Navigation](https://developer.android.com/topic/libraries/architecture/navigation) — handle everything needed for in-app navigation
* [Paging](https://developer.android.com/topic/libraries/architecture/paging) — gradually load information on demand from your data source
* [Room](https://developer.android.com/topic/libraries/architecture/room) — fluent SQLite database access
* [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel) — manage UI-related data in a lifecycle-conscious way
* [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager) — manage your Android background jobs

With the help of the Android Architecture Components we are going to implement MVVM architecture pattern in My Crypto Coins app following this diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/1*0-hsCQF-Ry0cV2332YE3Aw.png)

It’s a recommended architecture by Google. It shows how all the modules should interact with one another. Next we’ll be covering only the specific Android Architecture Components that we will use in our project.

### Organizing your source files

Before starting development we should consider how we should organize our project’s source files. We can not leave this question unanswered, as later we would have a messy structure hard to understand and modify.

There are several ways to do it. One is to organize by component category. For example, all activities goes to their own folder, all adapters go to their folder and so on.

Another way would be to organize everything by app features. For example, search and add crypto in all crypto currencies list feature goes to its own `addsearchlist` folder. The main idea is that you need to do it in some specific way instead of having everything placed randomly. I use some kind of mix of both of these.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iP8HHiXOtxWesHowvjhvUQ.png)
_My Crypto Coins app folder structure_

Besides the project’s folder structure, you should consider applying some rules for naming project files. For example, when naming Android classes you should define the class purpose clearly in the name.

### ViewModel

For the start of our app architecture development, first we are going to create the ViewModel. View models are objects that provide data for UI components and survive configuration changes.

You can use a ViewModel to retain data across the entire lifecycle of an activity or a fragment. Activities and fragments are short-lived objects. They are created and destroyed frequently as a user interacts with an app. A ViewModel is also better suited to managing tasks related to network communication, as well as data manipulation and persistence.

As example now lets create a ViewModel for `MainListFragment` to separate the UI data from it.

```kotlin
class MainViewModel : ViewModel() {
    ...
}
```

Then obtain the ViewModel with single line of code.

```kotlin
class MainListFragment : Fragment() {
    ...
    private lateinit var viewModel: MainViewModel
    ...
    override fun onActivityCreated(savedInstanceState: Bundle?) {

        super.onActivityCreated(savedInstanceState)

        setupList()

        // Obtain ViewModel from ViewModelProviders, using this fragment as LifecycleOwner.
        viewModel = ViewModelProviders.of(this).get(MainViewModel::class.java)
        ...
    }
    ...
}
```

Basically that’s it, congratulations! ? Let’s move on.

### LiveData

LiveData is an observable data holder class. It follows the [observer pattern](https://en.wikipedia.org/wiki/Observer_pattern). LiveData is lifecycle-aware. This means that it only updates app component (activity, fragment, etc.) observers that are in an active lifecycle state.

LiveData class returns the latest value of the data. When data changes it returns the updated value. LiveData is best suited with ViewModel.

We will use LiveData together with ViewModel like this:

```kotlin
...
class MainViewModel : ViewModel() {

    private val liveData = MutableLiveData<ArrayList<Cryptocurrency>>()
    val data: LiveData<ArrayList<Cryptocurrency>>
        get() = liveData

    init {
        val tempData = ArrayList<Cryptocurrency>()

        val btc:Cryptocurrency = Cryptocurrency("Bitcoin", 1, 0.56822348, "BTC", 8328.77, 4732.60, 0.19, -10.60, 0.44, 20.82)
        val eth:Cryptocurrency = Cryptocurrency("Etherium", 2, 6.0, "ETH", 702.99, 4217.94, 0.13, -7.38, 0.79, 33.32)

        tempData.add(btc)
        tempData.add(eth)

        liveData.value = tempData
    }
}
```

Observe data on the ViewModel, exposed as LiveData:

```kotlin
...
class MainListFragment : Fragment() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var recyclerAdapter: MainRecyclerViewAdapter

    private lateinit var viewModel: MainViewModel

    ...

    override fun onActivityCreated(savedInstanceState: Bundle?) {

        super.onActivityCreated(savedInstanceState)

        setupList()

        // Obtain ViewModel from ViewModelProviders, using this fragment as LifecycleOwner.
        viewModel = ViewModelProviders.of(this).get(MainViewModel::class.java)

        // Observe data on the ViewModel, exposed as a LiveData
        viewModel.data.observe(this, Observer { data ->
            // Set the data exposed by the LiveData
            if (data != null) {
                recyclerAdapter.setData(data)
            }
        })
    }
    ...
}
```

Browse the repository at this point in the history [here](https://github.com/baruckis/MyCryptoCoinsApp-Android/tree/622cf980c4fb68efab546eeddf31c4bf5aee7ba1).

### Data Binding

Data Binding Library was created to remove boilerplate code needed to connect to XML layouts.

To use Data Binding in your Kotlin projects, you will need to turn on support for annotation processors with the kapt compiler plugin. Also add data binding block to the Android configuration gradle file:

```gradle
...
apply plugin: 'kotlin-kapt'

android {
    ...
    dataBinding {
        enabled = true
    }
}
...
```

To use data binding generated classes, we need to put all the view code in `<layo`ut> tags. The most powerful concept of data binding is that we can bind some data class to an xml layout and item properties to fields directly.

```xml
<layout xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools">

    <data>

        <variable
            name="cryptocurrency"
            type="com.baruckis.mycryptocoins.data.Cryptocurrency" />
    </data>
  
    ...      

            <android.support.v7.widget.AppCompatTextView
                android:id="@+id/item_name"
                style="@style/MainListItemPrimeText"
                android:layout_marginEnd="@dimen/main_cardview_list_item_text_between_margin"
                android:layout_marginStart="@dimen/main_cardview_list_item_inner_margin"
                android:text="@{cryptocurrency.name}"
                android:textAlignment="viewStart"
                app:layout_constraintBottom_toTopOf="@+id/item_amount_symbol"
                app:layout_constraintEnd_toStartOf="@+id/guideline1_percent"
                app:layout_constraintStart_toEndOf="@+id/item_image_icon"
                app:layout_constraintTop_toTopOf="parent"
                app:layout_constraintVertical_chainStyle="spread"
                tools:text="@string/sample_text_item_name" />

     ...
</layout>
```

RecyclerView adapter with data biding will look like this:

```kotlin
class MainRecyclerViewAdapter() : RecyclerView.Adapter<MainRecyclerViewAdapter.BindingViewHolder>() {

    private lateinit var dataList: ArrayList<Cryptocurrency>

    fun setData(newDataList: ArrayList<Cryptocurrency>) {
        dataList = newDataList
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): BindingViewHolder {
        val inflater = LayoutInflater.from(parent.context)
        val binding = FragmentMainListItemBinding.inflate(inflater, parent, false)

        return BindingViewHolder(binding)
    }

    override fun onBindViewHolder(holder: BindingViewHolder, position: Int) = holder.bind(dataList[position])

    override fun getItemCount(): Int = dataList.size

    ...

    inner class BindingViewHolder(var binding: FragmentMainListItemBinding) : RecyclerView.ViewHolder(binding.root) {
        fun bind(cryptocurrency: Cryptocurrency) {
            binding.cryptocurrency = cryptocurrency

            binding.itemRanking.text = String.format("${cryptocurrency.rank}")
            ...
            binding.executePendingBindings()
        }
    }
}
```

At last no more writing `findViewById` ? Browse the repository at this point in the history [here](https://github.com/baruckis/Kriptofolio/tree/05a05e0cbc1cac0aefc7a0030fd77779da213214).

### Room

Our app needs to store persistent data of different cryptocurrencies that the user holds. This should be stored inside the local database that is kept inside the Android device privately.

For storing structured data in a private database we will use a SQLite database. This is often the best choice.

In order to create the SQLite database for our app we will use Room. Room is a persistence library made by the Android team which is a wrapper above SQLite. It is an abstraction layer that removes much of the boilerplate code you need to interact with SQLite. It also adds compile-time checking of your SQL queries.

The best way to think of it is as an ORM (Object Relational Mapper) tool designed to automatically generate glue code to map between your object instances and rows in your database.

There are basically 3 major components in Room:

1. Entity — this component represents a class that holds a database row. For each entity, a database table is created to hold the items.
2. DAO (Data Access Object) — the main component which is responsible for defining the methods that access the database.
3. Database — a component which is a holder class that uses annotation to define the list of entities, the list of DAOs, and database version and serves as the main access point for the underlying connection.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jT94pc71uD_A2TPN_E2ulg.png)

Let’s follow these simple steps to setup Room in our My Crypto Coins app:

1. Create an Entity.

```kotlin
@Entity
data class Cryptocurrency(val name: String,
                          val rank: Short,
                          val amount: Double,
                          @PrimaryKey
                          val symbol: String,
                          val price: Double,
                          val amountFiat: Double,
                          val pricePercentChange1h: Double,
                          val pricePercentChange7d: Double,
                          val pricePercentChange24h: Double,
                          val amountFiatChange24h: Double)
```

Add some extra information to tell Room about its structure in the database.

2. Create the DAO.

```kotlin
@Dao
interface MyCryptocurrencyDao {

    @Query("SELECT * FROM Cryptocurrency")
    fun getMyCryptocurrencyLiveDataList(): LiveData<List<Cryptocurrency>>

    @Insert
    fun insertDataToMyCryptocurrencyList(data: List<Cryptocurrency>)
}
```

For the start, we are going to create a DAO which only allows us to retrieve records from the table that we have created with Entity and also to insert some sample data.

3. Create and setup the Database.

It is important to say that the Database instance should ideally be built only once per session. The one way to achieve this would be to use a Singleton pattern.

```kotlin
@Database(entities = [Cryptocurrency::class], version = 1, exportSchema = false)
abstract class AppDatabase : RoomDatabase() {

    abstract fun myCryptocurrencyDao(): MyCryptocurrencyDao


    // The AppDatabase a singleton to prevent having multiple instances of the database opened at the same time.
    companion object {

        // Marks the JVM backing field of the annotated property as volatile, meaning that writes to this field are immediately made visible to other threads.
        @Volatile
        private var instance: AppDatabase? = null

        // For Singleton instantiation.
        fun getInstance(context: Context): AppDatabase {
            return instance ?: synchronized(this) {
                instance ?: buildDatabase(context).also { instance = it }
            }
        }

        // Creates and pre-populates the database.
        private fun buildDatabase(context: Context): AppDatabase {
            return Room.databaseBuilder(context, AppDatabase::class.java, DATABASE_NAME)
                    // Prepopulate the database after onCreate was called.
                    .addCallback(object : Callback() {
                        override fun onCreate(db: SupportSQLiteDatabase) {
                            super.onCreate(db)
                            // Insert the data on the IO Thread.
                            ioThread {
                                getInstance(context).myCryptocurrencyDao().insertDataToMyCryptocurrencyList(PREPOPULATE_DATA)
                            }
                        }
                    })
                    .build()
        }

        // Sample data.
        val btc: Cryptocurrency = Cryptocurrency("Bitcoin", 1, 0.56822348, "BTC", 8328.77, 4732.60, 0.19, -10.60, 0.44, 20.82)
        val eth: Cryptocurrency = Cryptocurrency("Etherium", 2, 6.0, "ETH", 702.99, 4217.94, 0.13, -7.38, 0.79, 33.32)

        val PREPOPULATE_DATA = listOf(btc, eth)

    }

}
```

```kotlin
private val IO_EXECUTOR = Executors.newSingleThreadExecutor()

// Utility method to run blocks on a dedicated background thread, used for io/database work.
fun ioThread(f : () -> Unit) {
    IO_EXECUTOR.execute(f)
}
```

As you see on initial run, the database will be prepopulated with some sample data just for testing purposes.

4. **EXTRA step.** Create the Repository.

The Repository is not part of the Architecture Components libraries. It is a suggested best practice for code separation and architecture.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_A8UbQDjX8YjzVZ3T7bhNw.png)

It stands as a single source of truth for all app data in case you have to manage multiple data sources.

```kotlin
class MyCryptocurrencyRepository private constructor(
        private val myCryptocurrencyDao: MyCryptocurrencyDao
) {

    fun getMyCryptocurrencyLiveDataList(): LiveData<List<Cryptocurrency>> {
        return myCryptocurrencyDao.getMyCryptocurrencyLiveDataList()
    }

    companion object {

        // Marks the JVM backing field of the annotated property as volatile, meaning that writes to this field are immediately made visible to other threads.
        @Volatile
        private var instance: MyCryptocurrencyRepository? = null

        // For Singleton instantiation.
        fun getInstance(myCryptocurrencyDao: MyCryptocurrencyDao) =
                instance ?: synchronized(this) {
                    instance
                            ?: MyCryptocurrencyRepository(myCryptocurrencyDao).also { instance = it }
                }
    }
}
```

We are going to use this repository in our ViewModel.

```kotlin
class MainViewModel(myCryptocurrencyRepository: MyCryptocurrencyRepository) : ViewModel() {

    val liveData = myCryptocurrencyRepository.getMyCryptocurrencyLiveDataList()
}
```

Our Fragment code also evolves.

```kotlin
class MainListFragment : Fragment() {

    ...

    private lateinit var viewModel: MainViewModel

    ...

    override fun onActivityCreated(savedInstanceState: Bundle?) {

        super.onActivityCreated(savedInstanceState)

        setupList()
        subscribeUi()
    }

    ...

    private fun subscribeUi() {

        val factory = InjectorUtils.provideMainViewModelFactory(requireContext())
        // Obtain ViewModel from ViewModelProviders, using this fragment as LifecycleOwner.
        viewModel = ViewModelProviders.of(this, factory).get(MainViewModel::class.java)

        // Update the list when the data changes by observing data on the ViewModel, exposed as a LiveData.
        viewModel.liveData.observe(this, Observer<List<Cryptocurrency>> { data ->
            if (data != null && data.isNotEmpty()) {
                emptyListView.visibility = View.GONE
                recyclerView.visibility = View.VISIBLE
                recyclerAdapter.setData(data)
            } else {
                recyclerView.visibility = View.GONE
                emptyListView.visibility = View.VISIBLE
            }
        })

    }

}
```

Because our ViewModel class now has a constructor which is not empty anymore, we need to implement a provider factory pattern. This will be passed to the `ViewModelProviders.of()` method as the second parameter.

```kotlin
object InjectorUtils {

    fun provideMainViewModelFactory(
            context: Context
    ): MainViewModelFactory {
        val repository = getMyCryptocurrencyRepository(context)
        return MainViewModelFactory(repository)
    }

    private fun getMyCryptocurrencyRepository(context: Context): MyCryptocurrencyRepository {
        return MyCryptocurrencyRepository.getInstance(
                AppDatabase.getInstance(context).myCryptocurrencyDao())
    }
}
```

```kotlin
class MainViewModelFactory(private val repository: MyCryptocurrencyRepository) : ViewModelProvider.NewInstanceFactory() {

    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return MainViewModel(repository) as T
    }
}
```

Browse the repository at this point in the history [here](https://github.com/baruckis/Kriptofolio/tree/b555fd9e2319bd4580122036d71066860fa82589).

### Final thoughts

Design architectures, that we discussed in this part, should be used as informed guidelines but not a hard rules. I did not wanted to go too much into detail on each topic. With Android Architecture Components we had a look at the coding process. Have in mind that there is lot more to learn on each component individually and I advise you to do that.

Let’s summarize everything that we manage to make already:

* In My Crypto Coins app, every separate screen has its own ViewModel. This will survive any configuration change and protect the user from any data loss.
* The App’s user interface is a reactive type. This means it will update immediately when the data changes in the back-end. That is done with the help of LiveData.
* Our project have less code as we bind to the variables in our code directly using Data Binding.
* Finally, our app stores user data locally inside the device as a SQLite database. The database was created conveniently with the Room component. The App’s code is structured by features and all project architecture is MVVM — a recommended pattern by Android team.

### Repository

Now, as you’re seeing the “Kriptofolio” (previously “My Crypto Coins”) app is really starting to take shape. With the latest repository commit for this part 3, you can find it nicely showing prepopulated database data for the user with the total holdings portfolio value calculated correctly.

#### [View Source On GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-3)



---

**_Ačiū! Thanks for reading! I originally published this post for my personal blog [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-3/) on August 22, 2018._**

