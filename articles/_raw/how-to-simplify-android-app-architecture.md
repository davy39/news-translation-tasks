---
title: 'How to Simplify Your Android App''s Architecture: a Detailed Guide With Code
  Samples'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-06T16:54:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-simplify-android-app-architecture
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca07a740569d1a4ca48ea.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
seo_title: null
seo_desc: 'By Vitaly Kuprenko

  Individual programmers develop their mobile apps according to their vision, including
  their ideas and views on how to perform various tasks. Sometimes they might disregard
  the main principles of object oriented or functional progra...'
---

By Vitaly Kuprenko

Individual programmers develop their mobile apps according to their vision, including their ideas and views on how to perform various tasks. Sometimes they might disregard the main principles of object oriented or functional programming, which can lead to disorientation among the developers. 

This is bad - they won’t be able to deal with their code. And the next developer who needs to maintain the project or modify it may go crazy. It is better to rebuild such projects from scratch, since maintenance becomes a complicated process. 

Until Google released its first supported architecture, almost every software development company used its own architecture. This helped them make their code clearer and made it possible to switch between projects. But if a developer changed companies, it would take them some time to learn that new architecture along with a new project.

At the moment, there are 16 different [architectures](https://github.com/googlesamples/android-architecture) for Android developers, thanks to Google:  


* 6 stable samples (Java);
* 2 stable samples (Kotlin):
* 4 external samples;
* 3 deprecated samples;
* 1 sample in progress. 

Whichever architecture you use depends on your specific purpose, approach, and application of various toolkits for the implementation various functionalities. And it depends on the programming language. 

However, all these architectures have one common architectural foundation that almost equally divides the logic for working with networks, databases, dependencies, and processing callbacks.

### Tools used during the process

After studying all these architectures, I built a simplified approach and came up with an architecture with fewer layers. I will show you how to implement a simple Android app that loads a news list, allows you to save stories to Favorites, and then delete if necessary using my approach.

![Image](https://lh3.googleusercontent.com/h4o-H8Gb3UK9O2m52fv_jkjTQ_jAq3CLqi4t7nGat9ZdyuqzxmxYgmmwV_zEULcO4oGonWs0z1mm4VuXS51WjFEBpcDrXSsR4mMkVhVrd51-2VHYBiUUx4Ci2JOzTYEpIievGlpX)

Here is a summary of the tech I used:

* **Kotlin** to develop the app along with the **AndroidX** library 
* **Room SQLite** as a database 
* **Stetho** to browse the data in bases 
* **Retrofit2** along with RxJava2 to help log server requests and get server responses. 
* **Glide** to process images
* **Android Architecture Components** (LiveData, ViewModel, Room) and **ReactiveX** (RxJava2, RxKotlin и RxAndroid) for building dependencies, dynamic data changes, and processing asynchrony.  

So this is the [mobile app technology stack](https://www.cleveroad.com/blog/choosing-the-right-technology-stack-for-mobile-application) I used for my project. 

**Let’s get started**

### First steps

Connect **AndroidX**. In **gradle.properties** at the app level, write the following:

```
android.enableJetifier=true
android.useAndroidX=true
```

Now it is necessary to replace the dependencies in **build.gradle** at the app module level from Android to AndroidX. You should extract all dependencies to **ext,** as you can see in the example of Kotlin out-of-the-box versioning in **build.gradle** at the app level. And then I add the Gradle versioning there:

```
buildscript {
    ext.kotlin_version = '1.3.0'
    ext.gradle_version = '3.2.1'

    repositories {
        google()
        jcenter()
        maven { url 'https://jitpack.io' }
        mavenCentral()
    }
    dependencies {
        classpath "com.android.tools.build:gradle:$gradle_version"
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"

        // NOTE: Do not place your application dependencies here; they belong
        // in the individual module build.gradle files
    }
}
```

For all other dependencies, I will build its **ext** file, where I add absolutely all dependencies including SDK versions, dividing versioning and creating dependencies massifs which will be implemented further in **build.gradle** at the app level. It will look like the following:

```
ext {
    compileSdkVersion = 28
    minSdkVersion = 22
    buildToolsVersion = '28.0.3'
    targetSdkVersion = 28

    appcompatVersion = '1.0.2'
    supportVersion = '1.0.0'
    supportLifecycleExtensionsVersion = '2.0.0'
    constraintlayoutVersion = '1.1.3'
    multiDexVersion = "2.0.0"

    testJunitVersion = '4.12'
    testRunnerVersion = '1.1.1'
    testEspressoCoreVersion = '3.1.1'

    testDependencies = [
            junit       : "junit:junit:$testJunitVersion",
            runner      : "androidx.test:runner:$testRunnerVersion",
            espressoCore: "androidx.test.espresso:espresso-core:$testEspressoCoreVersion"
    ]

    supportDependencies = [
            kotlin            : "org.jetbrains.kotlin:kotlin-stdlib-jdk7:$kotlin_version",
            appCompat         : "androidx.appcompat:appcompat:$appcompatVersion",
            recyclerView      : "androidx.recyclerview:recyclerview:$supportVersion",
            design            : "com.google.android.material:material:$supportVersion",
            lifecycleExtension: "androidx.lifecycle:lifecycle-extensions:$supportLifecycleExtensionsVersion",
            constraintlayout  : "androidx.constraintlayout:constraintlayout:$constraintlayoutVersion",
            multiDex          : "androidx.multidex:multidex:$multiDexVersion"
    ]
}
```

The version and massif names are implemented randomly. After that, we'll implement dependencies in **build.gradle** at the app level as follows:

```
apply plugin: 'com.android.application'
apply plugin: 'kotlin-android'
apply plugin: 'kotlin-android-extensions'
apply plugin: 'kotlin-kapt'

android {
    compileSdkVersion rootProject.ext.compileSdkVersion as Integer
    buildToolsVersion rootProject.ext.buildToolsVersion as String
```

```
dependencies {
    implementation fileTree(dir: 'libs', include: ['*.jar'])

    //Test
    testImplementation testDependencies.junit
    androidTestImplementation testDependencies.runner
    androidTestImplementation testDependencies.espressoCore

    //Support
    implementation supportDependencies.kotlin
    implementation supportDependencies.appCompat
    implementation supportDependencies.recyclerView
    implementation supportDependencies.design
    implementation supportDependencies.lifecycleExtension
    implementation supportDependencies.constraintlayout
    implementation supportDependencies.multiDex
```

Don’t forget to specify **multiDexEnabled true** in the default configs. In most cases, you'll reach the limit for the number of methods used quickly. 

In the same way, you need to declare all dependencies of the app. Let’s add permissions to connect our app with the Internet:

```
 <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.INTERNET" />
```

If there is no name added in the manifest, you should do it since **Stetho** won’t see the nameless app and you won’t be able to look into the database. 

### Basic components building

It is worth noting that the MVVM ([Model-View-ViewModel](https://www.journaldev.com/20292/android-mvvm-design-pattern)) pattern was used as the basis for building this architecture. 

Let’s start the development. The first thing you need to do is to create a class which will inherit Application(). In this class, we will give access to the app context for its further use.

```
@SuppressWarnings("all")
class App : Application() {

    companion object {
        lateinit var instance: App
            private set
    }

    override fun onCreate() {
        super.onCreate()
        instance = this
        Stetho.initializeWithDefaults(this)
        DatabaseCreator.createDatabase(this)
    }
}
```

The second step is to create basic app components starting with [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel), which I will use for each Activity or Fragment.   


```
abstract class BaseViewModel constructor(app: Application) : AndroidViewModel(app) {

    override fun onCleared() {
        super.onCleared()
    }
}
```

This app doesn't have complicated functionality. But in the basic ViewModel we will put **3 main [LiveData](https://developer.android.com/reference/android/arch/lifecycle/MediatorLiveData)**: 

* error processing 
* loading processing with the progress bar displayed 
* and, since I have an app with lists, processing the receipt and data availability in the adapter as a placeholder that displays in their absence.

```
val errorLiveData = MediatorLiveData<String>()
    val isLoadingLiveData = MediatorLiveData<Boolean>()
    val isEmptyDataPlaceholderLiveData = MediatorLiveData<Boolean>()
```

To transfer the results of the function implementation to LiveData I will use  **[Consumer](http://reactivex.io/RxJava/javadoc/io/reactivex/functions/Consumer.html)**.

To process errors in any place in the app, you need to create a Consumer that will transfer **Throwable.message** value to **errorLiveData**.

Also, in the basic VewModel, you will need to create a method that will receive a LiveData list to display the progress bar during their implementation.

Our basic ViewModel will look like this:

```
abstract class BaseViewModel constructor(app: Application) : AndroidViewModel(app) {

    val errorLiveData = MediatorLiveData<String>()
    val isLoadingLiveData = MediatorLiveData<Boolean>()
    val isEmptyDataPlaceholderLiveData = MediatorLiveData<Boolean>()

    private var compositeDisposable: CompositeDisposable? = null

    protected open val onErrorConsumer = Consumer<Throwable> {
        errorLiveData.value = it.message
    }

    fun setLoadingLiveData(vararg mutableLiveData: MutableLiveData<*>) {
        mutableLiveData.forEach { liveData ->
            isLoadingLiveData.apply {
                this.removeSource(liveData)
                this.addSource(liveData) { this.value = false }
            }
        }
    }

    override fun onCleared() {
        isLoadingLiveData.value = false
        isEmptyDataPlaceholderLiveData.value = false
        clearSubscription()
        super.onCleared()
    }

    private fun clearSubscription() {
        compositeDisposable?.apply {
            if (!isDisposed) dispose()
            compositeDisposable = null
        }
    }
}
```

  
In our app it doesn't make sense to create a few Activities for two screens (news list screen and favorites list screen). But since this sample shows the implementation of optimal and easily extensible architecture, I will create a basic app.  

Our app will be built on 1 Activity and 2 Fragments which we will inflate in Container activity. The XML file of our Activity will be the following:

```
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <FrameLayout
        android:id="@+id/flContainer"
        android:layout_width="match_parent"
        android:layout_height="match_parent" />

    <include layout="@layout/include_placeholder"/>

    <include layout="@layout/include_progress_bar" />
</FrameLayout>
```

where **include_placeholder** and **include_progressbar** will look like this:

```
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/flProgress"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_black_40">

    <ProgressBar
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:background="@color/transparent" />
</FrameLayout>
```

```
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/flPlaceholder"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="@color/bg_transparent">

    <ImageView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:background="@color/transparent"
        android:src="@drawable/ic_business_light_blue_800_24dp" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_gravity="center"
        android:layout_marginTop="40dp"
        android:text="@string/empty_data"
        android:textColor="@color/colorPrimary"
        android:textStyle="bold" />
</FrameLayout>
```

Our BaseActivity will look like this:

```
abstract class BaseActivity<T : BaseViewModel> : AppCompatActivity(), BackPressedCallback,
        ProgressViewCallback, EmptyDataPlaceholderCallback {

    protected abstract val viewModelClass: Class<T>
    protected abstract val layoutId: Int
    protected abstract val containerId: Int

    protected open val viewModel: T by lazy(LazyThreadSafetyMode.NONE) { ViewModelProviders.of(this).get(viewModelClass) }

    protected abstract fun observeLiveData(viewModel: T)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(layoutId)
        startObserveLiveData()
    }
    
    private fun startObserveLiveData() {
        observeLiveData(viewModel)
    }
}
```

Let’s implement how to display possible errors in the processes of all future Activities. I will do it in the form of usual Toast for simplicity. 

```
protected open fun processError(error: String) = Toast.makeText(this, error, Toast.LENGTH_SHORT).show()
```

and send this error text to the display method: 

```
protected open val errorObserver = Observer<String> { it?.let { processError(it) } }
```

In the basic Activity I will start keep up with the changes of **errorLiveData** value that is located in the basic View Model. The **startObserveLiveData()** method will mutate as follows:

```
private fun startObserveLiveData() {
        observeLiveData(viewModel)
        with(viewModel) {
            errorLiveData.observe(this@BaseActivity, errorObserver)
        }
    }
```

Now using **onErrorConsumer** of the basic ViewModel as the **onError** processor, you will see the message about the implemented method error.

Create a method that allows you to replace Fragments in Activity with the ability to add to Back Stack.

```
protected open fun replaceFragment(fragment: Fragment, needToAddToBackStack: Boolean = true) {
        val name = fragment.javaClass.simpleName
        with(supportFragmentManager.beginTransaction()) {
            replace(containerId, fragment, name)
            if (needToAddToBackStack) {
                addToBackStack(name)
            }
            commit()
        }
    }
```

Let’s create interfaces for displaying progress and placeholder in the required app spots.

```
interface EmptyDataPlaceholderCallback {

    fun onShowPlaceholder()

    fun onHidePlaceholder()
}
```

```
interface ProgressViewCallback {

    fun onShowProgress()

    fun onHideProgress()
}
```

Implement them in basic Activity. I created functions of the ID setting to the progress bar and placeholder, and also initialized these Views.

```
protected open fun hasProgressBar(): Boolean = false

    protected abstract fun progressBarId(): Int

    protected abstract fun placeholderId(): Int

    private var vProgress: View? = null
    private var vPlaceholder: View? = null
```

```
override fun onShowProgress() {
        vProgress?.visibility = View.VISIBLE
    }

    override fun onHideProgress() {
        vProgress?.visibility = View.GONE
    }

    override fun onShowPlaceholder() {
        vPlaceholder?.visibility = View.VISIBLE
    }

    override fun onHidePlaceholder() {
        vPlaceholder?.visibility = View.INVISIBLE
    }

    public override fun onStop() {
        super.onStop()
        onHideProgress()
    }
```

And finally in the **onCreate** method I set an ID for View:

```
if (hasProgressBar()) {
            vProgress = findViewById(progressBarId())
            vProgress?.setOnClickListener(null)
        }
        vPlaceholder = findViewById(placeholderId())
        startObserveLiveData()
```

I have spelled out the creation of the basic ViewModel and Basic Activity. The Basic Fragment will be created following the same principle. 

When you create each separate screen, if you're considering further extension and possible changes, you need to create a separate Fragment with its ViewModel. 

Note: in the case when Fragments can be combined in one cluster, and business logic doesn’t imply a massive complexity, several Fragments may use one ViewModel. 

Switching between Fragments happens because of interfaces that are implemented in Activity. To do this, each Fragment should have a **companion object{ }** with the method of Fragment object building with the ability of arguments transfer to **Bundle**:

```
companion object {
        fun newInstance() = FavoriteFragment().apply { arguments = Bundle() }
    }
```

### Architecture solutions

When basic components are created, it is time to focus on architecture. Schematically it will look like the clean architecture made by the famous Robert C. Martin or Uncle Bob. But since I use **RxJava2**, I got rid of the **Boundaries** interfaces (as the way to ensure the **Dependency Rule** execution) in favor of the standard **Observable** and **Subscriber**. 	

Apart from this, using **RxJava2** tools I have integrated data conversion for more flexible work with it. It concerns both working with server responses and with databases. 

In addition to the primary model, I will create a server response model and separate table model for **Room**. Converting data between these two models, you can make any changes during the conversion process, convert server responses, and save the necessary data to the base before it displays on the UI and so on. 

Fragments are responsible for the **UI**, and ViewModel Fragments are responsible for business logic execution. If business logic concerns the whole activity, then ViewModel Activity. 

ViewModels get data from a provider by its initialization via **val … by lazy{},** if you need an invariable object, or **lateinit var,** if vice versa. After the business logic's execution, if you need to transfer data to change the **UI,** you create new **MutableLiveData** in the ViewModel that you will use in the **observeLiveData()** method of our Fragment. 

It sounds quite easy. Implementation is straightforward as well.   
An essential component of our architecture is a data converter based on a simple conversion from one data type to another. For conversion of **RxJava** data stream, [**SingleTransformer**](http://reactivex.io/RxJava/javadoc/io/reactivex/SingleTransformer.html) or [**FlowableTransformer**](http://reactivex.io/RxJava/javadoc/io/reactivex/FlowableTransformer.html) are used depending on the type. In the case of our app, interface and abstract class of converter look like the following:

```
interface BaseDataConverter<IN, OUT> {

    fun convertInToOut(inObject: IN): OUT

    fun convertOutToIn(outObject: OUT): IN

    fun convertListInToOut(inObjects: List<IN>?): List<OUT>?

    fun convertListOutToIn(outObjects: List<OUT>?): List<IN>?

    fun convertOUTtoINSingleTransformer(): SingleTransformer<IN?, OUT>

    fun convertListINtoOUTSingleTransformer(): SingleTransformer<List<OUT>, List<IN>>
}

abstract class BaseDataConverterImpl<IN, OUT> : BaseDataConverter<IN, OUT> {

    override fun convertInToOut(inObject: IN): OUT = processConvertInToOut(inObject)

    override fun convertOutToIn(outObject: OUT): IN = processConvertOutToIn(outObject)

    override fun convertListInToOut(inObjects: List<IN>?): List<OUT> =
            inObjects?.map { convertInToOut(it) } ?: listOf()

    override fun convertListOutToIn(outObjects: List<OUT>?): List<IN> =
            outObjects?.map { convertOutToIn(it) } ?: listOf()

    override fun convertOUTtoINSingleTransformer() =
            SingleTransformer<IN?, OUT> { it.map { convertInToOut(it) } }

    override fun convertListINtoOUTSingleTransformer() =
            SingleTransformer<List<OUT>, List<IN>> { it.map { convertListOutToIn(it) } }

    protected abstract fun processConvertInToOut(inObject: IN): OUT

    protected abstract fun processConvertOutToIn(outObject: OUT): IN
}
```

In this example, I use basic conversions such as model-model, list of models - list of models, and the same combinations but only using **SingleTransformer** for processing of server responses and requests in the database.

Let’s start with network - with **RestClient. retrofitBuilder** method will be the following:

```
fun retrofitBuilder(): Retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addCallAdapterFactory(RxJava2CallAdapterFactory.create())
            .addConverterFactory(NullOrEmptyConverterFactory().converterFactory())
            .addConverterFactory(GsonConverterFactory.create(createGsonBuilder()))
            .client(createHttpClient())
            .build()
```

```
//base url
    const val BASE_URL = "https://newsapi.org"
```

Using third-party APIs, there is always a chance to get an absolute null response from the server, and there may be plenty of reasons for it. That is why an additional **NullOrEmptyConverterFactory** will help handle the situation. This is how it looks:

```
class NullOrEmptyConverterFactory : Converter.Factory() {

    fun converterFactory() = this

    override fun responseBodyConverter(type: Type?,
                                       annotations: Array<Annotation>,
                                       retrofit: Retrofit): Converter<ResponseBody, Any>? {
        return Converter { responseBody ->
            if (responseBody.contentLength() == 0L) {
                null
            } else {
                type?.let {
                    retrofit.nextResponseBodyConverter<Any>(this, it, annotations)?.convert(responseBody) }
            }
        }
    }
}
```

To create models, it is necessary to build on an API. As an example, I will use the free of charge APU for non-commercial use from **newsapi.org.** It has a rather extensive list of requested functionality, but I will use a small part for this example. After a quick registration, you get access to the API and your **api key** which is required for each request. 

As the endpoint, I will use [**https://newsapi.org/v2/everything**](https://newsapi.org/v2/everything)**.** From the suggested **query** I choose the following: **q** - search query, **from** - sorting from date, **to** - sorting to date, **sortBy** - sorting by selected criterion, and must-have **apiKey.**

After **RestClient** creation, I create an API interface with the selected Query for our app:

```
interface NewsApi {
    @GET(ENDPOINT_EVERYTHING)
    fun getNews(@Query("q") searchFor: String?,
                @Query("from") fromDate: String?,
                @Query("to") toDate: String?,
                @Query("sortBy") sortBy: String?,
                @Query("apiKey") apiKey: String?): Single<NewsNetworkModel>
}
```

```
//endpoints
    const val ENDPOINT_EVERYTHING = "/v2/everything"
```

We will receive this response in NewsNetworkModel:

```
data class NewsNetworkModel(@SerializedName("articles")
                            var articles: List<ArticlesNetworkModel>? = listOf())
```

```
data class ArticlesNetworkModel(@SerializedName("title")
                                var title: String? = null,
                                @SerializedName("description")
                                var description: String? = null,
                                @SerializedName("urlToImage")
                                var urlToImage: String? = null)
```

These data from the whole response will be enough to display a list with a picture, title and news description. 

For the implementation of our architectural approach, let’s create general models:

```
interface News {
    var articles: List<Article>?
}

class NewsModel(override var articles: List<Article>? = null) : News
```

```
interface Article {
    var id: Long?
    var title: String?
    var description: String?
    var urlToImage: String?
    var isAddedToFavorite: Boolean?
    var fragmentName: FragmentsNames?
}

class ArticleModel(override var id: Long? = null,
                   override var title: String? = null,
                   override var description: String? = null,
                   override var urlToImage: String? = null,
                   override var isAddedToFavorite: Boolean? = null,
                   override var fragmentName: FragmentsNames? = null) : Article
```

Since the Article model will be used for the connection with the database and data displaying in the adapter, we need to add 2 margins that I will use for changing the UI elements in the list. 

When everything is ready for the request, I create converters for network models that we will use in the query of news receiving via NetworkModule.

Converters are created in reverse order from nesting, and they convert in direct order accordingly. So the first one I create on Article, the second one on News:

```
interface ArticlesBeanConverter

class ArticlesBeanDataConverterImpl : BaseDataConverterImpl<ArticlesNetworkModel, Article>(), ArticlesBeanConverter {

    override fun processConvertInToOut(inObject: ArticlesNetworkModel): Article = inObject.run {
        ArticleModel(null, title, description, urlToImage, false, FragmentsNames.NEWS)
    }

    override fun processConvertOutToIn(outObject: Article): ArticlesNetworkModel = outObject.run {
        ArticlesNetworkModel(title, description, urlToImage)
    }
}
```

```
interface NewsBeanConverter

class NewsBeanDataConverterImpl : BaseDataConverterImpl<NewsNetworkModel, News>(), NewsBeanConverter {

    private val articlesConverter by lazy { ArticlesBeanDataConverterImpl() }

    override fun processConvertInToOut(inObject: NewsNetworkModel): News = inObject.run {
        NewsModel(articles?.let { articlesConverter.convertListInToOut(it) })
    }

    override fun processConvertOutToIn(outObject: News): NewsNetworkModel = outObject.run {
        NewsNetworkModel(articles?.let { articlesConverter.convertListOutToIn(it) })
    }
}
```

As you can see above, during the News object conversion, the conversion of the Article objects list is also executed.

Once converters for network models are created, let’s proceed to the creation of the module (repository network). Since there are usually more than 1 or 2 interface APIs, you need to create BaseModule, typed API, Network Module, and ConversionModel.

This is how it looks:

```
abstract class BaseNetworkModule<A, NM, M>(val api: A, val dataConverter: BaseDataConverter<NM, M>)
```

Accordingly, it will be the following on NewsModule:

```
interface NewsModule {

    fun getNews(fromDate: String? = null, toDate: String? = null, sortBy: String? = null): Single<News>
}

class NewsModuleImpl(api: NewsApi) : BaseNetworkModule<NewsApi, NewsNetworkModel, News>(api, NewsBeanDataConverterImpl()), NewsModule {

    override fun getNews(fromDate: String?, toDate: String?, sortBy: String?): Single<News> =
            api.getNews(searchFor = SEARCH_FOR, fromDate = fromDate, toDate = toDate, sortBy = sortBy, apiKey = API_KEY)
                    .compose(dataConverter.convertOUTtoINSingleTransformer())
                    .onErrorResumeNext(NetworkErrorUtils.rxParseError())
}
```

For this API, the API key is a crucial parameter for requesting by any suggested endpoints. That is why you need to make sure that optional parameters won’t be specified beforehand, and you need to nullify them by default.

As you can see above, I applied the data conversion during response processing.

Let’s work with the database. I create the app database, call it **AppDatabase** and inherit from **RoomDatabase()**.

For database initialization, it is necessary to create **DatabaseCreator**, which should be initialized in **App** class.

```
object DatabaseCreator {

    lateinit var database: AppDatabase
    private val isDatabaseCreated = MutableLiveData<Boolean>()
    private val mInitializing = AtomicBoolean(true)

    @SuppressWarnings("CheckResult")
    fun createDatabase(context: Context) {
        if (mInitializing.compareAndSet(true, false).not()) return
        isDatabaseCreated.value = false
        Completable.fromAction { database = Room.databaseBuilder(context, AppDatabase::class.java, DB_NAME).build() }
                .compose { completableToMain(it) }
                .subscribe({ isDatabaseCreated.value = true }, { it.printStackTrace() })
    }
}
```

Now in the **onCreate()** method of the **App** class I initialize **Stetho** and database:

```
override fun onCreate() {
        super.onCreate()
        instance = this
        Stetho.initializeWithDefaults(this)
        DatabaseCreator.createDatabase(this)
    }
```

When the database is created, I create a basic Dao with a single insert() method inside:

```
@Dao
interface BaseDao<in I> {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insert(obj: I)
}
```

Based on the idea of our app, I will save news I like, get the list of saved articles, delete saved news by its ID, or delete all news from the table. Our **NewsDao** will be the following:

```
@Dao
interface NewsDao : BaseDao<NewsDatabase> {

    @Query("SELECT * FROM $NEWS_TABLE")
    fun getNews(): Single<List<NewsDatabase>>

    @Query("DELETE FROM $NEWS_TABLE WHERE id = :id")
    fun deleteNewsById(id: Long)

    @Query("DELETE FROM $NEWS_TABLE")
    fun deleteFavoriteNews()
}
```

And news table will be the following:

```
@Entity(tableName = NEWS_TABLE)
data class NewsDatabase(@PrimaryKey var id: Long?,
                        var title: String?,
                        var description: String?,
                        var urlToImage: String?)
```

When the table is created, let’s link it with a database:

```
@Database(entities = [NewsDatabase::class], version = DB_VERSION)
abstract class AppDatabase : RoomDatabase() {

    abstract fun newsDao(): NewsDao
}
```

Now we can work with the database, save and extract data from it.

As for the module (repository network), I will create a model converter - database table model:

```
interface NewsDatabaseConverter

class NewsDatabaseDataConverterImpl : BaseDataConverterImpl<Article, NewsDatabase>(), NewsDatabaseConverter {

    override fun processConvertInToOut(inObject: Article): NewsDatabase =
            inObject.run {
                NewsDatabase(id, title, description, urlToImage)
            }

    override fun processConvertOutToIn(outObject: NewsDatabase): Article =
            outObject.run {
                ArticleModel(id, title, description, urlToImage, true, FragmentsNames.FAVORITES)
            }
}
```

BaseRepository is available for working with various tables. Let’s write it. It will look like the following in its simplest version which is enough for the app:

```
abstract class BaseRepository<M, DBModel> {

    protected abstract val dataConverter: BaseDataConverter<M, DBModel>
    protected abstract val dao: BaseDao<DBModel>
}
```

After creating BaseRepository, I will create **NewsRepository**:

```
interface NewsRepository {

    fun saveNew(article: Article): Single<Article>

    fun getSavedNews(): Single<List<Article>>

    fun deleteNewsById(id: Long): Single<Unit>

    fun deleteAll(): Single<Unit>
}

object NewsRepositoryImpl : BaseRepository<Article, NewsDatabase>(), NewsRepository {

    override val dataConverter by lazy { NewsDatabaseDataConverterImpl() }
    override val dao by lazy { DatabaseCreator.database.newsDao() }

    override fun saveNew(article: Article): Single<Article> =
            Single.just(article)
                    .map { dao.insert(dataConverter.convertInToOut(it)) }
                    .map { article }

    override fun getSavedNews(): Single<List<Article>> =
            dao.getNews().compose(dataConverter.convertListINtoOUTSingleTransformer())

    override fun deleteNewsById(id: Long): Single<Unit> =
            Single.just(dao.deleteNewsById(id))

    override fun deleteAll(): Single<Unit> =
            Single.just(dao.deleteFavoriteNews())
}
```

When permanent repositories and modules are created, data should flow from an app provider that will request data either from the network or database depending on the requirements. A provider should combine both repositories. Considering the capabilities of various models and repositories, I will create BaseProvider:

```
abstract class BaseProvider<NM, DBR> {

    val repository: DBR = this.initRepository()

    val networkModule: NM = this.initNetworkModule()

    protected abstract fun initRepository(): DBR

    protected abstract fun initNetworkModule(): NM
}
```

  
Then **NewsProvider** will look like the following:

```
interface NewsProvider {

    fun loadNewsFromServer(fromDate: String? = null, toDate: String? = null, sortBy: String? = null): Single<News>

    fun saveNewToDB(article: Article): Single<Article>

    fun getSavedNewsFromDB(): Single<List<Article>>

    fun deleteNewsByIdFromDB(id: Long): Single<Unit>

    fun deleteNewsFromDB(): Single<Unit>
}

object NewsProviderImpl : BaseProvider<NewsModule, NewsRepositoryImpl>(), NewsProvider {

    override fun initRepository() = NewsRepositoryImpl

    override fun initNetworkModule() = NewsModuleImpl(RestClient.retrofitBuilder().create(NewsApi::class.java))

    override fun loadNewsFromServer(fromDate: String?, toDate: String?, sortBy: String?) = networkModule.getNews(fromDate, toDate, sortBy)

    override fun saveNewToDB(article: Article) = repository.saveNew(article)

    override fun getSavedNewsFromDB() = repository.getSavedNews()

    override fun deleteNewsByIdFromDB(id: Long) = repository.deleteNewsById(id)

    override fun deleteNewsFromDB() = repository.deleteAll()
}
```

Now we will get the list of news easily. In **NewsViewModel** we will declare all methods of our provider for further use:

```
val loadNewsSuccessLiveData = MutableLiveData<News>()
    val loadLikedNewsSuccessLiveData = MutableLiveData<List<Article>>()
    val deleteLikedNewsSuccessLiveData = MutableLiveData<Boolean>()

    private val loadNewsSuccessConsumer = Consumer<News> { loadNewsSuccessLiveData.value = it }
    private val loadLikedNewsSuccessConsumer = Consumer<List<Article>> { loadLikedNewsSuccessLiveData.value = it }
    private val deleteLikedNewsSuccessConsumer = Consumer<Unit> { deleteLikedNewsSuccessLiveData.value = true }

    private val dataProvider by lazy { NewsProviderImpl }

    init {
        isLoadingLiveData.apply { addSource(loadNewsSuccessLiveData) { value = false } }
```

```
@SuppressLint("CheckResult")
    fun loadNews(fromDate: String? = null, toDate: String? = null, sortBy: String? = null) {
        isLoadingLiveData.value = true
        isEmptyDataPlaceholderLiveData.value = false
        dataProvider.loadNewsFromServer(fromDate, toDate, sortBy)
                .compose(RxUtils.ioToMainTransformer())
                .subscribe(loadNewsSuccessConsumer, onErrorConsumer)

    }

    @SuppressLint("CheckResult")
    fun saveLikedNew(article: Article) {
        Single.fromCallable { Unit }
                .flatMap { dataProvider.saveNewToDB(article) }
                .compose(RxUtils.ioToMainTransformerSingle())
                .subscribe({}, { onErrorConsumer })
    }

    @SuppressLint("CheckResult")
    fun removeLikedNew(id: Long) {
        Single.fromCallable { Unit }
                .flatMap { dataProvider.deleteNewsByIdFromDB(id) }
                .compose(RxUtils.ioToMainTransformerSingle())
                .subscribe({}, { onErrorConsumer })
    }

    @SuppressLint("CheckResult")
    fun loadLikedNews() {
        Single.fromCallable { Unit }
                .flatMap { dataProvider.getSavedNewsFromDB() }
                .compose(RxUtils.ioToMainTransformerSingle())
                .subscribe(loadLikedNewsSuccessConsumer, onErrorConsumer)
    }

    @SuppressLint("CheckResult")
    fun removeLikedNews() {
        Single.fromCallable { Unit }
                .flatMap { dataProvider.deleteNewsFromDB() }
                .compose(RxUtils.ioToMainTransformerSingle())
                .subscribe(deleteLikedNewsSuccessConsumer, onErrorConsumer)
    }
```

Having declared all methods which executed business logic in ViewModel, we will call them back from Fragment where in **observeLiveData()** results of each declared **LiveData** will be processed.

To implement it easily, in **SEARCH_FOR** parameters I randomly chose **Apple,** and further sorting will be performed by the **popularity** tag. If necessary, you can add minimum functionality for changing these parameters.

Since newsapi.org doesn’t provide you with a news ID, I accept the element index as ID. Sorting by popularity tag is also implemented via the API. But to avoid data rewriting with the same IDs in the base during sorting by popularity, I will verify data availability in the base before news list loading. If the base is empty - the new list is loading, if not - notification is shown. 

Let’s call in the **onViewCreated()** method of **NewsFragment** the following method:

```
private fun loadLikedNews() {
        viewModel.loadLikedNews()
    }
```

Since our base is empty, method **loadNews()** will be launched. In the **observeLiveData** method I will use our loading LiveData - **viewModel.loadNewsSuccessLiveData.observe(..){news →},** where we will receive the list of news articles if the request is successful, and then transfer it to the adapter:

```
isEmptyDataPlaceholderLiveData.value = news.articles?.isEmpty()
                with(newsAdapter) {
                    news.articles?.toMutableList()?.let {
                        clear()
                        addAll(it)
                    }
                    notifyDataSetChanged()
                }
                loadNewsSuccessLiveData.value = null
```

Having launched the app, you will see the following result:

![Image](https://lh4.googleusercontent.com/SSyMu9byyX01H_baLGzU_oN7KuDnbhS4lcNnQjAbxlATJNrA8wFJyGJl1klH7LVijAu0yOD9k0M57cjprTbdjIOLpNl2SUl_A6rqqNv-IcREaaa4wIIlfRPRrDVpRza3GOl-6834)

In the toolbar menu on the right side, you can see 2 options - sorting and favorites. Let’s sort the list by popularity and get the following result:

![Image](https://lh3.googleusercontent.com/7BT2Por_XNJwm3mdCc4JdW0cTl8-SVOfPagn2fOklb4z9TbGDWPxb-wCAhE2V9rzUQog_ICI-I2AX4xh7NGrm50mS1BQDhafahJJwk9C_qsHcs_P3sK6T6vigj-pwcddsOmiKvq4)

If you go to Favorites, you will see a Placeholder only, since there is no data in the base. The Favorites screen will look like the following:

![Image](https://lh4.googleusercontent.com/E2V2sR15Pb23PsfVOv1K91_Ma7eJV5DZUUbu4LPH4Dq-rvfR6iU6qTn-grnDR2HCcgiKSK0EFEAIG0GH-gX2pR06iNCM8j3ZouIf5dHPHEEPUCBZ5z6pEhfRx2NBRvwkZ4oonnkv)

UI fragment of Favorites has a screen for the displaying of the list of liked news and only one option in the toolbar for database cleaning. When you save data clicking on “Like”, screens will look like the following:

![Image](https://lh4.googleusercontent.com/4E-JQL94Qwa5GxRzfap0InOW60v-zeGUuKNFFJV_g7uyjTj1TubpKDvWsD7XgLBApzV55zJdVAHpFnDxYpPe6bL2Ntv9YAmlDhVzuFsLctFw6NJPWBz1RPnJN8CZ2wRMsPvJOrd3)

As I wrote above, in the standard model 2 additional margins were added to the general model, and these margins are used for data displaying in the adapter. Now you can see that elements of saved news lisst have no option to add to Favorites. 

```
var isAddedToFavorite: Boolean?
    var fragmentName: FragmentsNames?
```

If you click “Like” again, the saved element will be removed from the base.

### Wrapping up

Thus, I showed you a simple and clear approach to Android app development. We kept up with the main principles of Clean Architecture but simplified it as much as possible. 

What is the difference between the architecture I provided you with and Clean Architecture from Mr. Martin? In the very beginning, I have noted that my architecture is similar to CA since it is used as the basis. Here is the CA scheme below:

![Image](https://lh4.googleusercontent.com/avSMw0B5pCLWAVWjES8gIJ5KU6OInVAG8DmYd7CIRhOx8Z4cGRLDMECv7HqHgNyTwBCe7Q0eY8VD6tw8zZWNdb5emxWrjP8IBQvMr8YGbySiygiTqG3N2BQsebB6JDFrGtRq4fax)

The event goes to Presenter, and then to **Use Case. Use Case** requests **Repository.** Repository receives data, created **Entity,** and transfers it to **UseCase.** Thus, **Use Case** receives all the necessary Entities. After the implementation of business logic, you get the result that comes back to **Presenter,** and it, in turn, transfers the result to **UI.**  

In the scheme below, **Controller** calls methods from **InputPort** that implements **UseCase**, and the **OutputPort** interface receives this response and **Presenter** implements it. Instead of **UseCase** direct depending on **Presenter,** it depends on the interface in its layers, and it doesn’t contradict with **Dependency Rule,** and Presenter should implement this interface.

![Image](https://lh4.googleusercontent.com/zCxRkWYDl8TKPyQUqBNvGHN45wj51N-B4hZGjn0ul6Kvj6IVERtYIQiICH6JEC5RiZQFbMWmtQllSXx0LhndE-GAm21J_-nMrfEOA4nz8paAkolm0JQidxBHc3OcF0TiDoRIU36j)

Thus, processes that are implemented in the the external layer don’t affect processes in the internal layer. What is Entity in Clean Architecture? In fact, it is everything that doesn’t depend on a specific app, and it will be a general concept for many apps. But in the mobile development process Entity is business objects of the app, which contain general and high-level rules (app business logic). 

What about **Gateways?** As I see it, **Gateways** is a repository for working with the database and a module for working with a network. We got rid of the controller since initially Clean Architecture was created for structuring business apps of high complexity, and data converters perform its functions in my app. ViewModels transfer data to Fragments for UI processing replacing Presenters. 

In my approach, I also keep up with Dependency Rule strictly, and the logic of repositories, modules, models, and providers is encapsulated, and access to them is possible via interfaces. Thus, changes in external layers don’t affect internal layers. And the implementation process using **RxJava2**, **KotlinRx**, and **Kotlin LiveData** makes the developer’s tasks easier, clearer, and code becomes well-read and easily extensible.

