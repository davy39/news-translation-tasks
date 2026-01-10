---
title: How to implement Dependency Injection in your app with Dagger 2
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-07T09:35:06.000Z'
originalURL: https://freecodecamp.org/news/kriptofolio-app-series-part-4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*CVSY-XyHRtZZJd2lDV-ZZw.png
tags:
- name: Android
  slug: android
- name: Cryptocurrency
  slug: cryptocurrency
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 4

  Dependency injection will significantly improve your code. It makes your code more
  modular, flexible and testable. Actually its name sounds more complicated than the
  idea which stands behind it.

  In ...'
---

By Andrius Baruckis

#### Kriptofolio app series - Part 4

Dependency injection will significantly improve your code. It makes your code more modular, flexible and testable. Actually its name sounds more complicated than the idea which stands behind it.

In this part of the series we are going to learn about dependency injection. We will then implement it in “Kriptofolio” (previously “My Crypto Coins”) app. We are going to use Dagger 2. Dagger 2 is the most popular open-source dependency injection framework for Android. This is a valuable skill to have for creating modern apps, even thought the learning curve is hard enough.

### Series content

* [Introduction: A roadmap to build a modern Android app in 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Part 1: An introduction to the SOLID principles](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* [Part 2: How to start building your Android app: creating Mockups, UI, and XML layouts](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* [Part 3: All about that Architecture: exploring different architecture patterns and how to use them in your app](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* Part 4: How to implement Dependency Injection in your app with Dagger 2 (you’re here)
* [Part 5: Handle RESTful Web Services using Retrofit, OkHttp, Gson, Glide and Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### What is Dependency Injection?

To explain dependency injection first we have to understand what dependency means in programming. A dependency is when one of the objects depends on the concrete implementation of another object. You can identify a dependency in your code whenever you instantiate an object within another. Let’s take a look at a practical example.

```kotlin
class MyAppClass() {

    private val library: MyLibrary = MyLibrary(true)
    ...
}

class MyLibrary(private val useSpecialFeature: Boolean) {
    
    ...
}
```

As you see from this example your class `MyAppClass` will depend directly on concrete configuration and implementation of your library class `MyLibrary`. What if you would like one day to use a third-party library instead? What if you would like to have another class where you would like to use exactly the same library configuration? Every time you will have to search through your code, find exact place and change it. It’s just a few examples.

The idea is that this tight coupling between the components of the application will make your development work harder as your project grows. To avoid any problems, let’s use dependency injection for loosening the coupling described.

```kotlin
class MyAppClass(private val library: MyLibrary) {
    
    ...
}

class MyLibrary(private val useSpecialFeature: Boolean) {
    
    ...
}
```

That’s it, that’s a very primitive dependency injection example. Instead of creating and configuring a new `MyLibrary` class object inside your class `MyAppClass`, you just pass or inject it into the constructor. So `MyAppClass` can be totally irresponsible for `MyLibrary`.

### What is Dagger 2?

Dagger is a fully static, compile-time, open-source dependency injection framework for both Java and Android. In this article I will be talking about its second version which Google maintains. Square created its earlier version.

Dagger 2 is considered to be one of the most efficient dependency injection frameworks built to date. Actually if you compare Dagger 1, Dagger 2 and Dagger 2.10 you would discover each implementation is different. You need to relearn it each time as there were significant changes done by the authors. When writing this article I am using Dagger 2.16 version and we are going to focus only on it.

As you now understand about dependency injection, our classes should not create or have dependencies. Instead they need to get everything from outside. So when using Dagger 2, this framework will provide all the dependencies needed.

It does this by generating a lot of boilerplate code for us. That generated code will be fully traceable and will mimic the code which a user may write by hand. Dagger 2 is written in Java and the code generated by its annotation processor will be Java code too.

However it works with Kotlin without any problems or modifications. Remember that Kotlin is fully interoperable with Java. If compared to similar frameworks, Dagger 2 is a less dynamic one. It works at compile time rather than at run-time with reflection. There is no reflection usage at all. All that means is that this framework will be harder to set up and to learn. It will provide performance boost with compile-time safety.

### Manual Dependency Injection without tools

You may have noticed in the My Crypto Coins app [source code from the previous part](https://github.com/baruckis/Kriptofolio/tree/Part-3) that there is a piece of code for injecting objects without using any dependency injection tools. It works fine, and this solution would be good enough for such a small app like this. Take a look at the utilities package:

```kotlin
/**
 * Static methods used to inject classes needed for various Activities and Fragments.
 */
object InjectorUtils {

    private fun getCryptocurrencyRepository(context: Context): CryptocurrencyRepository {
        return CryptocurrencyRepository.getInstance(
                AppDatabase.getInstance(context).cryptocurrencyDao())
    }

    fun provideMainViewModelFactory(
            application: Application
    ): MainViewModelFactory {
        val repository = getCryptocurrencyRepository(application)
        return MainViewModelFactory(application, repository)
    }

    fun provideAddSearchViewModelFactory(
            context: Context
    ): AddSearchViewModelFactory {
        val repository = getCryptocurrencyRepository(context)
        return AddSearchViewModelFactory(repository)
    }
}
```

As you see this class will do all the work. It will create ViewModel factories for activities or fragments that require them.

```kotlin
/**
 * Factory for creating a [MainViewModel] with a constructor that takes a
 * [CryptocurrencyRepository].
 */
class MainViewModelFactory(private val application: Application, private val repository: CryptocurrencyRepository) : ViewModelProvider.NewInstanceFactory() {

    @Suppress("UNCHECKED_CAST")
    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return MainViewModel(application, repository) as T
    }

}
```

Then you use `InjectorUtils` class like this where you need to get a specific ViewModel factory:

```kotlin
/**
 * A placeholder fragment containing a simple view.
 */
class MainListFragment : Fragment() {

    ...

    private lateinit var viewModel: MainViewModel

    ...

    override fun onActivityCreated(savedInstanceState: Bundle?) {

        super.onActivityCreated(savedInstanceState)

        setupList()
        ...
    }

    ...

    private fun subscribeUi(activity: FragmentActivity) {

        // This is the old way how we were injecting code before using Dagger.
        val factory = InjectorUtils.provideMainViewModelFactory(activity.application)

        // Obtain ViewModel from ViewModelProviders, using parent activity as LifecycleOwner.
        viewModel = ViewModelProviders.of(activity, factory).get(MainViewModel::class.java)

        ...
    }

}
```

As you see our `MainListFragment` class don’t even know about `CryptocurrencyRepository` or `AppDatabase`. It gets a successfully constructed factory from InjectorUtils class. Actually this is one simple way to do it. We are going to get rid of it and learn how to setup Dagger 2 tool for advanced dependency injection. If this app would expand in functionality and code, I don’t doubt we would start seeing benefits really fast of using a professional dependency injection framework over a manual solution.

So let’s delete `InjectorUtils` class right now and learn how to setup Dagger 2 in My Crypto Coins app source code.

### Dependency Injection for MVVM with Kotlin

#### How to setup Dagger 2 with ViewModels, Activities and Fragments

Now we’ll go through the Dagger 2 step by step setup on the My Crypto Coins app project.

**To begin, you should enable Kotlin’s own [Annotation Processing Tool](https://kotlinlang.org/docs/reference/kapt.html) (kapt). Then add special Dagger 2 dependencies.**

You can do this by adding these lines to your gradle file:

```gradle
apply plugin: 'kotlin-kapt' // For annotation processing

...

implementation "com.google.dagger:dagger:$versions.dagger"
implementation "com.google.dagger:dagger-android:$versions.dagger"
implementation "com.google.dagger:dagger-android-support:$versions.dagger"
kapt "com.google.dagger:dagger-compiler:$versions.dagger"
kapt "com.google.dagger:dagger-android-processor:$versions.dagger"
```

Kapt plugin will enable the compiler to generate stub classes required for interoperability between Java and Kotlin. For convenience we will define the concrete Dagger 2 version in a separate gradle file, as we do that with all our dependencies.

```gradle
def versions = [:]

versions.dagger = "2.16"

ext.versions = versions
```

To find the latest version available check the releases at [Dagger 2's official repository on Github](https://github.com/google/dagger).

**Now, create your application `App` class.**

Skip this if you already have this class set. After you’ve done that, we will leave it as it is for a while, but come back later.

```kotlin
class App : Application() {

    override fun onCreate() {
        super.onCreate()
    }

}
```

For My Crypto Coins app, we already have created the application class earlier.

**Next, update your manifest file to enable your `App` class.**

Skip this if you have already done that before.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.baruckis.mycryptocoins">

    <application
        android:name=".App"
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        ...
```

For My Crypto Coins app, we’ve also already set the `App` class in the manifest earlier.

**Now let’s create a new package called `dependencyinjection`.**

Here we are going to keep all the files related to Dagger implementation.

**Create `AppModule` class module which will provide dependencies all over your application.**

```kotlin
/**
 * AppModule will provide app-wide dependencies for a part of the application.
 * It should initialize objects used across our application, such as Room database, Retrofit, Shared Preference, etc.
 */
@Module(includes = [ViewModelsModule::class])
class AppModule() {

    @Singleton // Annotation informs Dagger compiler that the instance should be created only once in the entire lifecycle of the application.
    @Provides // Annotation informs Dagger compiler that this method is the constructor for the Context return type.
    fun provideContext(app: App): Context = app // Using provide as a prefix is a common convention but not a requirement.

    @Singleton
    @Provides
    fun provideCryptocurrencyRepository(context: Context): CryptocurrencyRepository {
        return CryptocurrencyRepository.getInstance(AppDatabase.getInstance(context).cryptocurrencyDao())
    }
}
```

As you see, to create a Dagger module we need to annotate it with the special `@Module` annotation. Projects usually have multiple Dagger modules. It is typical for one of them to provide app-wide dependencies. This `AppModule` will be used to initialize objects used across our application, such as Room database, Retrofit, Shared Preference, etc.

As an example, we could discuss a very common scenario for AppModule to provide a Context object in case we need it to get access to it anywhere in our app. Let’s analyze the code to see how to do that.

We need to use a special Dagger annotation `@Provides`. It tells Dagger that the method provides a specific type of dependency, in our case, a Context object. So when somewhere in the app we request to inject a Context, AppModule is the place where Dagger finds it. And it does not matter the names of our methods, as Dagger cares only about the return type. It is only common practice to name the method with provide prefix, but it can be anything you want.

The `@Singleton` annotation which you see applied to the same method is not part of the Dagger annotations. It is contained inside the javax package. This annotation tells Dagger that there should only be a single instance of that dependency.

You don’t need to write the boilerplate code to check if another instance of the object is already available. When generating the code Dagger will handle all that logic for you because of this annotation. Notice that our AppModule includes another module ViewModelsModule. Let’s create it now.

**Create a `ViewModelsModule` class module. This module will be responsible for providing ViewModels all over your application.**

```kotlin
/**
 * Will be responsible for providing ViewModels.
 */
@Module
abstract class ViewModelsModule {

    // We'd like to take this implementation of the ViewModel class and make it available in an injectable map with MainViewModel::class as a key to that map.
    @Binds
    @IntoMap
    @ViewModelKey(MainViewModel::class) // We use a restriction on multibound map defined with @ViewModelKey annotation, and if don't need any, we should use @ClassKey annotation provided by Dagger.
    abstract fun bindMainViewModel(mainViewModel: MainViewModel): ViewModel

    @Binds
    @IntoMap
    @ViewModelKey(AddSearchViewModel::class)
    abstract fun bindAddSearchViewModel(addSearchViewModel: AddSearchViewModel): ViewModel

    @Binds
    abstract fun bindViewModelFactory(factory: ViewModelFactory): ViewModelProvider.Factory
}
```

This module uses Dagger 2 feature map multi bindings. Using it, we contribute objects of our choosing into a map that becomes injectable anywhere in our app. Using the combination of Dagger annotations `@Binds`, `@IntoMap` and our custom annotation `@ViewModelKey`(this one we are going to create), we create an entry inside our map with key `MainViewModel::class` and value `MainViewModel` instance. We bind specific factory with the help of some common `ViewModelFactory` class. We need to create this class.

**Create a custom annotation class `ViewModelKey`.**

```kotlin
/**
 * An annotation class which tells dagger that it can be used to determine keys in multi bound maps.
 */
@MustBeDocumented
@Target(
        AnnotationTarget.FUNCTION,
        AnnotationTarget.PROPERTY_GETTER,
        AnnotationTarget.PROPERTY_SETTER
)
@Retention(AnnotationRetention.RUNTIME)
@MapKey
annotation class ViewModelKey(val value: KClass<out ViewModel>) // We might use only those classes which inherit from ViewModel.
```

This class is used for binding ViewModels in the `ViewModelsModule`. The specific annotation `@ViewModelKey` represents the key of our map. Our key can be only a class that inherits from `ViewModel`.

**Create the `ViewModelFactory` class.**

```kotlin
/**
 * Factory to auto-generate a Class to Provider Map.
 * We use Provider<T> to create an injectable object at a later time.
 */
@Suppress("UNCHECKED_CAST")
@Singleton
class ViewModelFactory @Inject constructor(private val viewModelsMap: Map<Class<out ViewModel>,
        @JvmSuppressWildcards Provider<ViewModel>>) : ViewModelProvider.Factory {

    override fun <T : ViewModel> create(modelClass: Class<T>): T {
        var creator: Provider<out ViewModel>? = viewModelsMap[modelClass]
        if (creator == null) {
            for (entry in viewModelsMap.entries) {
                if (modelClass.isAssignableFrom(entry.key)) {
                    creator = entry.value
                    break
                }
            }
        }
        if (creator == null) {
            throw IllegalArgumentException("Unknown model class $modelClass")
        }

        try {
            return creator.get() as T
        } catch (e: Exception) {
            throw RuntimeException(e)
        }
    }
}
```

This `ViewModelFactory` is a utility class which helps you dynamically create ViewModels. Here you provide the generated map as an argument. The `create()` method will be able to pick the right instance from the map.

**Create the `ActivityBuildersModule` class module.**

```kotlin
/**
 * All activities intended to use Dagger @Inject should be listed here.
 */
@Module
abstract class ActivityBuildersModule {

    @ContributesAndroidInjector(modules = [MainListFragmetBuildersModule::class]) // Where to apply the injection.
    abstract fun contributeMainActivity(): MainActivity

    @ContributesAndroidInjector
    abstract fun contributeAddSearchActivity(): AddSearchActivity
}
```

This module is responsible for constructing all your activities. It will generate `AndroidInjector` for all Activities defined in this class. Then objects can be injected into activities using `AndroidInjection.inject(this)` in the `onCreate` function from the activity lifecycle. Notice that this module also uses another separate module responsible for fragments. We will create this module next.

**Create the `MainListFragmetBuildersModule` class module.**

```kotlin
/**
 * All fragments related to MainActivity intended to use Dagger @Inject should be listed here.
 */
@Module
abstract class MainListFragmetBuildersModule {

    @ContributesAndroidInjector() // Attaches fragment to Dagger graph.
    abstract fun contributeMainListFragment(): MainListFragment
}
```

This module will build all your fragments related to `MainActivity`. It will generate `AndroidInjector` for all Fragments defined in this class. Objects can be injected into Fragments using `AndroidSupportInjection.inject(this)` in the `onAttach` function from the fragment lifecycle.

**Create the `AppComponent` class component.**

```kotlin
/**
 * Singleton component interface for the app. It ties all the modules together.
 * The component is used to connect objects to their dependencies.
 * Dagger will auto-generate DaggerAppComponent which is used for initialization at Application.
 */
@Singleton
@Component(
        modules = [
            // AndroidSupportInjectionModule is a class of Dagger and we don't need to create it.
            // If you want to use injection in fragment then you should use AndroidSupportInjectionModule.class else use AndroidInjectionModule.
            AndroidSupportInjectionModule::class,
            AppModule::class,
            ActivityBuildersModule::class
        ]
)
interface AppComponent {

    @Component.Builder // Used for instantiation of a component.
    interface Builder {

        @BindsInstance // Bind our application instance to our Dagger graph.
        fun application(application: App): Builder

        fun build(): AppComponent
    }

    // The application which is allowed to request the dependencies declared by the modules
    // (by means of the @Inject annotation) should be declared here with individual inject() methods.
    fun inject(app: App)
}
```

Component is a very important class. It will enable all the above to start working together. It does this by connecting objects to their dependencies. Dagger will use this interface to generate the code necessary to perform the dependency injection.

To create a component class you will need to use Dagger annotation `@Component`. It takes a list of modules as an input. Another annotation `@Component.Builder` allows us to bind some instance to component.

**Then generate a graph object.**

At this moment you have all your modules and your component setup. You can generate your graph object by selecting Build -> Make Module inside your Android Studio IDE. We will need this generation for future steps.

**Now create an `Injectable` interface.**

```kotlin
/**
 * It is just a plain empty marker interface, which tells to automatically inject activities or fragments if they implement it.
 */
interface Injectable
```

This will also be needed for future steps. `Injectable` interface should be implemented by activities or fragments which we want to be injectable automatically.

**Create a new helper class named `AppInjector`.**

```kotlin
/**
 * It is simple helper class to avoid calling inject method on each activity or fragment.
 */
object AppInjector {
    fun init(app: App) {
        // Here we initialize Dagger. DaggerAppComponent is auto-generated from AppComponent.
        DaggerAppComponent.builder().application(app).build().inject(app)

        app.registerActivityLifecycleCallbacks(object : Application.ActivityLifecycleCallbacks {
            override fun onActivityPaused(activity: Activity) {

            }

            override fun onActivityResumed(activity: Activity) {

            }

            override fun onActivityStarted(activity: Activity) {

            }

            override fun onActivityDestroyed(activity: Activity) {

            }

            override fun onActivitySaveInstanceState(activity: Activity, outState: Bundle?) {

            }

            override fun onActivityStopped(activity: Activity) {

            }

            override fun onActivityCreated(activity: Activity, savedInstanceState: Bundle?) {
                handleActivity(activity)
            }
        })
    }

    private fun handleActivity(activity: Activity) {
        if (activity is HasSupportFragmentInjector || activity is Injectable) {
            // Calling inject() method will cause Dagger to locate the singletons in the dependency graph to try to find a matching return type.
            // If it finds one, it assigns the references to the respective fields.
            AndroidInjection.inject(activity)
        }

        if (activity is FragmentActivity) {
            activity.supportFragmentManager.registerFragmentLifecycleCallbacks(object : FragmentManager.FragmentLifecycleCallbacks() {
                override fun onFragmentCreated(fragmentManager: FragmentManager, fragment: Fragment, savedInstanceState: Bundle?) {
                    if (fragment is Injectable) {
                        AndroidSupportInjection.inject(fragment)
                    }
                }
            }, true)
        }
    }

}
```

It is just a simple helper class to avoid calling the inject method on each activity or fragment.

**Next, setup the `App` class which we already created before.**

```kotlin
class App : Application(), HasActivityInjector {

    @Inject // It implements Dagger machinery of finding appropriate injector factory for a type.
    lateinit var dispatchingAndroidInjector: DispatchingAndroidInjector<Activity>

    override fun onCreate() {
        super.onCreate()

        // Initialize in order to automatically inject activities and fragments if they implement Injectable interface.
        AppInjector.init(this)

        ...
    }


    // This is required by HasActivityInjector interface to setup Dagger for Activity.
    override fun activityInjector(): AndroidInjector<Activity> = dispatchingAndroidInjector
}
```

Because the application has activities, we need to implement the `HasActivityInjector` interface. If you see an error called out by Android Studio on `DaggerAppComponent`, it is because you have not generated a new file, as was pointed out in the previous step.

**So, setup `MainActivity` to inject the main ViewModel factory and add a support for fragment injections.**

```kotlin
// To support injecting fragments which belongs to this activity we need to implement HasSupportFragmentInjector.
// We would not need to implement it, if our activity did not contain any fragments or the fragments did not need to inject anything.
class MainActivity : AppCompatActivity(), HasSupportFragmentInjector {

    @Inject
    lateinit var dispatchingAndroidInjector: DispatchingAndroidInjector<Fragment>

    @Inject
    lateinit var viewModelFactory: ViewModelProvider.Factory
    private lateinit var mainViewModel: MainViewModel


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Obtain ViewModel from ViewModelProviders, using this activity as LifecycleOwner.
        mainViewModel = ViewModelProviders.of(this, viewModelFactory).get(MainViewModel::class.java)

        ...
    }

    ...

    override fun supportFragmentInjector(): AndroidInjector<Fragment> = dispatchingAndroidInjector

    ...
}
```

Because our activities have child fragments we need to implement `HasSupportFragmentInjector` interface. We also need this because we plan to make injections into our fragments. Our activity should not know about how it is injected. We use the `AndroidInjection.inject(this)` code line inside overriding `onCreate()` method.

Calling `inject()` method will cause Dagger 2 to locate the singletons in the dependency graph to try to find a matching return type. However we don’t need to write any code here because it’s done for us by previously created `AppInjector` helper class which we initialized inside our application class.

**Then, setup `MainListFragment` to inject the main ViewModel factory.**

```kotlin
/**
 * A placeholder fragment containing a simple view.
 */
class MainListFragment : Fragment(), Injectable {

    ...

    @Inject
    lateinit var viewModelFactory: ViewModelProvider.Factory
    private lateinit var viewModel: MainViewModel

    ...

    override fun onActivityCreated(savedInstanceState: Bundle?) {
        super.onActivityCreated(savedInstanceState)

        ...
        subscribeUi(activity!!)
    }

    ...

    private fun subscribeUi(activity: FragmentActivity) {

        // Obtain ViewModel from ViewModelProviders, using parent activity as LifecycleOwner.
        viewModel = ViewModelProviders.of(activity, viewModelFactory).get(MainViewModel::class.java)
        
        ...

    }

}
```

Similar to activities, if we want our fragment to be injectable, then into its `onAttach` method we should write the code `AndroidSupportInjection.inject(this)`. But again this is a job done by the `AppInjector` helper, so we can skip that. Just notice that we need to add the `Injectable` interface which we created earlier for the helper to work.

Congratulations, we’ve implemented Dagger 2 in the My Crypto Coins app project. Of course this article is a quick guide to deploy Dagger 2 in your app straight away, but not deep coverage of it. I recommend that you continue researching this topic if you feel lost on the basics.

### Repository

Check out the source code of the updated “Kriptofolio” (previously “My Crypto Coins”) app on GitHub.

#### [View Source On GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-4)



---

**_Ačiū! Thanks for reading! I originally published this post for my personal blog [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-4/) on October 7, 2018._**

