---
title: Comment implémenter l'Injection de Dépendances dans votre application avec
  Dagger 2
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
seo_title: Comment implémenter l'Injection de Dépendances dans votre application avec
  Dagger 2
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 4

  Dependency injection will significantly improve your code. It makes your code more
  modular, flexible and testable. Actually its name sounds more complicated than the
  idea which stands behind it.

  In ...'
---

Par Andrius Baruckis

#### Série d'applications Kriptofolio - Partie 4

L'injection de dépendances améliorera considérablement votre code. Elle rend votre code plus modulaire, flexible et testable. En fait, son nom semble plus compliqué que l'idée qui se cache derrière.

Dans cette partie de la série, nous allons apprendre l'injection de dépendances. Nous allons ensuite l'implémenter dans l'application « Kriptofolio » (anciennement « My Crypto Coins »). Nous allons utiliser Dagger 2. Dagger 2 est le framework d'injection de dépendances open-source le plus populaire pour Android. C'est une compétence précieuse pour créer des applications modernes, même si la courbe d'apprentissage est assez difficile.

### Contenu de la série

* [Introduction : Une feuille de route pour construire une application Android moderne en 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Partie 1 : Une introduction aux principes SOLID](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* [Partie 2 : Comment commencer à construire votre application Android : création de maquettes, UI et layouts XML](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* [Partie 3 : Tout sur cette Architecture : exploration de différents modèles d'architecture et comment les utiliser dans votre application](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* Partie 4 : Comment implémenter l'Injection de Dépendances dans votre application avec Dagger 2 (vous êtes ici)
* [Partie 5 : Gérer les Services Web RESTful en utilisant Retrofit, OkHttp, Gson, Glide et Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### Qu'est-ce que l'Injection de Dépendances ?

Pour expliquer l'injection de dépendances, nous devons d'abord comprendre ce que signifie une dépendance en programmation. Une dépendance est lorsqu'un des objets dépend de l'implémentation concrète d'un autre objet. Vous pouvez identifier une dépendance dans votre code chaque fois que vous instanciez un objet dans un autre. Regardons un exemple pratique.

```kotlin
class MyAppClass() {

    private val library: MyLibrary = MyLibrary(true)
    ...
}

class MyLibrary(private val useSpecialFeature: Boolean) {
    
    ...
}
```

Comme vous pouvez le voir dans cet exemple, votre classe `MyAppClass` dépendra directement de la configuration concrète et de l'implémentation de votre classe de bibliothèque `MyLibrary`. Que faire si vous souhaitez un jour utiliser une bibliothèque tierce à la place ? Que faire si vous souhaitez avoir une autre classe où vous souhaitez utiliser exactement la même configuration de bibliothèque ? Chaque fois, vous devrez rechercher dans votre code, trouver l'endroit exact et le changer. Ce ne sont que quelques exemples.

L'idée est que ce couplage serré entre les composants de l'application rendra votre travail de développement plus difficile à mesure que votre projet grandit. Pour éviter tout problème, utilisons l'injection de dépendances pour desserrer le couplage décrit.

```kotlin
class MyAppClass(private val library: MyLibrary) {
    
    ...
}

class MyLibrary(private val useSpecialFeature: Boolean) {
    
    ...
}
```

C'est tout, c'est un exemple très primitif d'injection de dépendances. Au lieu de créer et de configurer un nouvel objet de classe `MyLibrary` à l'intérieur de votre classe `MyAppClass`, vous le passez ou l'injectez simplement dans le constructeur. Ainsi, `MyAppClass` peut être totalement irresponsable pour `MyLibrary`.

### Qu'est-ce que Dagger 2 ?

Dagger est un framework d'injection de dépendances entièrement statique, à la compilation, open-source pour Java et Android. Dans cet article, je vais parler de sa deuxième version, maintenue par Google. Square a créé sa version précédente.

Dagger 2 est considéré comme l'un des frameworks d'injection de dépendances les plus efficaces construits à ce jour. En fait, si vous comparez Dagger 1, Dagger 2 et Dagger 2.10, vous découvrirez que chaque implémentation est différente. Vous devez le réapprendre chaque fois, car il y a eu des changements significatifs apportés par les auteurs. En écrivant cet article, j'utilise la version Dagger 2.16 et nous allons nous concentrer uniquement sur celle-ci.

Comme vous comprenez maintenant l'injection de dépendances, nos classes ne doivent pas créer ou avoir de dépendances. Au lieu de cela, elles doivent tout obtenir de l'extérieur. Ainsi, lors de l'utilisation de Dagger 2, ce framework fournira toutes les dépendances nécessaires.

Il le fait en générant beaucoup de code standard pour nous. Ce code généré sera entièrement traçable et imitera le code qu'un utilisateur pourrait écrire à la main. Dagger 2 est écrit en Java et le code généré par son processeur d'annotations sera également du code Java.

Cependant, il fonctionne avec Kotlin sans aucun problème ou modification. Rappelez-vous que Kotlin est entièrement interopérable avec Java. Comparé à des frameworks similaires, Dagger 2 est moins dynamique. Il fonctionne à la compilation plutôt qu'à l'exécution avec réflexion. Il n'y a aucune utilisation de réflexion. Tout cela signifie que ce framework sera plus difficile à configurer et à apprendre. Il fournira un gain de performance avec une sécurité à la compilation.

### Injection de Dépendances manuelle sans outils

Vous avez peut-être remarqué dans le code source de l'application My Crypto Coins [de la partie précédente](https://github.com/baruckis/Kriptofolio/tree/Part-3) qu'il y a un morceau de code pour injecter des objets sans utiliser d'outils d'injection de dépendances. Cela fonctionne bien, et cette solution serait suffisamment bonne pour une application aussi petite que celle-ci. Regardez le package des utilitaires :

```kotlin
/**
 * Méthodes statiques utilisées pour injecter des classes nécessaires pour diverses activités et fragments.
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

Comme vous le voyez, cette classe fera tout le travail. Elle créera des factories de ViewModel pour les activités ou fragments qui en ont besoin.

```kotlin
/**
 * Factory pour créer un [MainViewModel] avec un constructeur qui prend un
 * [CryptocurrencyRepository].
 */
class MainViewModelFactory(private val application: Application, private val repository: CryptocurrencyRepository) : ViewModelProvider.NewInstanceFactory() {

    @Suppress("UNCHECKED_CAST")
    override fun <T : ViewModel?> create(modelClass: Class<T>): T {
        return MainViewModel(application, repository) as T
    }

}
```

Ensuite, vous utilisez la classe `InjectorUtils` comme ceci là où vous devez obtenir une factory de ViewModel spécifique :

```kotlin
/**
 * Un fragment de remplissage contenant une vue simple.
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

        // C'est l'ancienne façon dont nous injections le code avant d'utiliser Dagger.
        val factory = InjectorUtils.provideMainViewModelFactory(activity.application)

        // Obtenez ViewModel à partir de ViewModelProviders, en utilisant l'activité parente comme LifecycleOwner.
        viewModel = ViewModelProviders.of(activity, factory).get(MainViewModel::class.java)

        ...
    }

}
```

Comme vous le voyez, notre classe `MainListFragment` ne connaît même pas `CryptocurrencyRepository` ou `AppDatabase`. Elle obtient une factory correctement construite à partir de la classe InjectorUtils. En fait, c'est une façon simple de le faire. Nous allons nous en débarrasser et apprendre à configurer l'outil Dagger 2 pour une injection de dépendances avancée. Si cette application devait s'étendre en fonctionnalités et en code, je ne doute pas que nous commencerions à voir les avantages très rapidement de l'utilisation d'un framework d'injection de dépendances professionnel par rapport à une solution manuelle.

Alors, supprimons la classe `InjectorUtils` maintenant et apprenons à configurer Dagger 2 dans le code source de l'application My Crypto Coins.

### Injection de Dépendances pour MVVM avec Kotlin

#### Comment configurer Dagger 2 avec ViewModels, Activities et Fragments

Maintenant, nous allons passer par la configuration étape par étape de Dagger 2 sur le projet de l'application My Crypto Coins.

**Pour commencer, vous devez activer l'outil [Annotation Processing Tool](https://kotlinlang.org/docs/reference/kapt.html) (kapt) de Kotlin. Ensuite, ajoutez les dépendances spéciales de Dagger 2.**

Vous pouvez le faire en ajoutant ces lignes à votre fichier gradle :

```gradle
apply plugin: 'kotlin-kapt' // Pour le traitement des annotations

...

implementation "com.google.dagger:dagger:$versions.dagger"
implementation "com.google.dagger:dagger-android:$versions.dagger"
implementation "com.google.dagger:dagger-android-support:$versions.dagger"
kapt "com.google.dagger:dagger-compiler:$versions.dagger"
kapt "com.google.dagger:dagger-android-processor:$versions.dagger"
```

Le plugin Kapt permettra au compilateur de générer des classes de substitution nécessaires pour l'interopérabilité entre Java et Kotlin. Pour plus de commodité, nous allons définir la version concrète de Dagger 2 dans un fichier gradle séparé, comme nous le faisons avec toutes nos dépendances.

```gradle
def versions = [:]

versions.dagger = "2.16"

ext.versions = versions
```

Pour trouver la dernière version disponible, consultez les versions sur [le dépôt officiel de Dagger 2 sur Github](https://github.com/google/dagger).

**Maintenant, créez votre classe d'application `App`.**

Passez cette étape si vous avez déjà configuré cette classe. Une fois que vous avez terminé, nous la laisserons telle quelle pour l'instant, mais nous y reviendrons plus tard.

```kotlin
class App : Application() {

    override fun onCreate() {
        super.onCreate()
    }

}
```

Pour l'application My Crypto Coins, nous avons déjà créé la classe d'application précédemment.

**Ensuite, mettez à jour votre fichier manifest pour activer votre classe `App`.**

Passez cette étape si vous l'avez déjà fait auparavant.

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

Pour l'application My Crypto Coins, nous avons également déjà défini la classe `App` dans le manifest précédemment.

**Maintenant, créons un nouveau package appelé `dependencyinjection`.**

Ici, nous allons garder tous les fichiers liés à l'implémentation de Dagger.

**Créez le module de classe `AppModule` qui fournira des dépendances dans toute votre application.**

```kotlin
/**
 * AppModule fournira des dépendances à l'échelle de l'application pour une partie de l'application.
 * Il doit initialiser les objets utilisés dans notre application, tels que la base de données Room, Retrofit, Shared Preference, etc.
 */
@Module(includes = [ViewModelsModule::class])
class AppModule() {

    @Singleton // Annotation informe le compilateur Dagger que l'instance doit être créée une seule fois dans tout le cycle de vie de l'application.
    @Provides // Annotation informe le compilateur Dagger que cette méthode est le constructeur pour le type de retour Context.
    fun provideContext(app: App): Context = app // Utiliser provide comme préfixe est une convention courante mais pas une exigence.

    @Singleton
    @Provides
    fun provideCryptocurrencyRepository(context: Context): CryptocurrencyRepository {
        return CryptocurrencyRepository.getInstance(AppDatabase.getInstance(context).cryptocurrencyDao())
    }
}
```

Comme vous le voyez, pour créer un module Dagger, nous devons l'annoter avec l'annotation spéciale `@Module`. Les projets ont généralement plusieurs modules Dagger. Il est typique pour l'un d'eux de fournir des dépendances à l'échelle de l'application. Ce `AppModule` sera utilisé pour initialiser les objets utilisés dans notre application, tels que la base de données Room, Retrofit, Shared Preference, etc.

Par exemple, nous pourrions discuter d'un scénario très courant pour AppModule afin de fournir un objet Context au cas où nous en aurions besoin pour y accéder n'importe où dans notre application. Analysons le code pour voir comment faire cela.

Nous devons utiliser une annotation spéciale de Dagger `@Provides`. Elle indique à Dagger que la méthode fournit un type spécifique de dépendance, dans notre cas, un objet Context. Ainsi, lorsque quelque part dans l'application nous demandons à injecter un Context, AppModule est l'endroit où Dagger le trouve. Et peu importe les noms de nos méthodes, car Dagger ne se soucie que du type de retour. Il est seulement courant de nommer la méthode avec le préfixe provide, mais cela peut être n'importe quoi que vous voulez.

L'annotation `@Singleton` que vous voyez appliquée à la même méthode ne fait pas partie des annotations Dagger. Elle est contenue dans le package javax. Cette annotation indique à Dagger qu'il ne doit y avoir qu'une seule instance de cette dépendance.

Vous n'avez pas besoin d'écrire le code standard pour vérifier si une autre instance de l'objet est déjà disponible. Lors de la génération du code, Dagger gérera toute cette logique pour vous grâce à cette annotation. Remarquez que notre AppModule inclut un autre module ViewModelsModule. Créons-le maintenant.

**Créez un module de classe `ViewModelsModule`. Ce module sera responsable de la fourniture de ViewModels dans toute votre application.**

```kotlin
/**
 * Sera responsable de la fourniture de ViewModels.
 */
@Module
abstract class ViewModelsModule {

    // Nous aimerions prendre cette implémentation de la classe ViewModel et la rendre disponible dans une map injectable avec MainViewModel::class comme clé de cette map.
    @Binds
    @IntoMap
    @ViewModelKey(MainViewModel::class) // Nous utilisons une restriction sur la map multibound définie avec l'annotation @ViewModelKey, et si nous n'en avons pas besoin, nous devrions utiliser l'annotation @ClassKey fournie par Dagger.
    abstract fun bindMainViewModel(mainViewModel: MainViewModel): ViewModel

    @Binds
    @IntoMap
    @ViewModelKey(AddSearchViewModel::class)
    abstract fun bindAddSearchViewModel(addSearchViewModel: AddSearchViewModel): ViewModel

    @Binds
    abstract fun bindViewModelFactory(factory: ViewModelFactory): ViewModelProvider.Factory
}
```

Ce module utilise la fonctionnalité de map multi-bindings de Dagger 2. En l'utilisant, nous contribuons des objets de notre choix dans une map qui devient injectable n'importe où dans notre application. En utilisant la combinaison des annotations Dagger `@Binds`, `@IntoMap` et notre annotation personnalisée `@ViewModelKey` (celle que nous allons créer), nous créons une entrée dans notre map avec la clé `MainViewModel::class` et la valeur `MainViewModel` instance. Nous liaisons une factory spécifique à l'aide d'une classe commune `ViewModelFactory`. Nous devons créer cette classe.

**Créez une classe d'annotation personnalisée `ViewModelKey`.**

```kotlin
/**
 * Une classe d'annotation qui indique à dagger qu'elle peut être utilisée pour déterminer les clés dans les maps multibound.
 */
@MustBeDocumented
@Target(
        AnnotationTarget.FUNCTION,
        AnnotationTarget.PROPERTY_GETTER,
        AnnotationTarget.PROPERTY_SETTER
)
@Retention(AnnotationRetention.RUNTIME)
@MapKey
annotation class ViewModelKey(val value: KClass<out ViewModel>) // Nous pouvons utiliser uniquement les classes qui héritent de ViewModel.
```

Cette classe est utilisée pour lier les ViewModels dans le `ViewModelsModule`. L'annotation spécifique `@ViewModelKey` représente la clé de notre map. Notre clé ne peut être qu'une classe qui hérite de `ViewModel`.

**Créez la classe `ViewModelFactory`.**

```kotlin
/**
 * Factory pour auto-générer une map de Class à Provider.
 * Nous utilisons Provider<T> pour créer un objet injectable à un moment ultérieur.
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

Cette `ViewModelFactory` est une classe utilitaire qui vous aide à créer dynamiquement des ViewModels. Ici, vous fournissez la map générée comme argument. La méthode `create()` sera en mesure de choisir la bonne instance à partir de la map.

**Créez le module de classe `ActivityBuildersModule`.**

```kotlin
/**
 * Toutes les activités destinées à utiliser Dagger @Inject doivent être listées ici.
 */
@Module
abstract class ActivityBuildersModule {

    @ContributesAndroidInjector(modules = [MainListFragmetBuildersModule::class]) // Où appliquer l'injection.
    abstract fun contributeMainActivity(): MainActivity

    @ContributesAndroidInjector
    abstract fun contributeAddSearchActivity(): AddSearchActivity
}
```

Ce module est responsable de la construction de toutes vos activités. Il générera `AndroidInjector` pour toutes les activités définies dans cette classe. Ensuite, les objets peuvent être injectés dans les activités en utilisant `AndroidInjection.inject(this)` dans la fonction `onCreate` du cycle de vie de l'activité. Remarquez que ce module utilise également un autre module séparé responsable des fragments. Nous allons créer ce module ensuite.

**Créez le module de classe `MainListFragmetBuildersModule`.**

```kotlin
/**
 * Tous les fragments liés à MainActivity destinés à utiliser Dagger @Inject doivent être listés ici.
 */
@Module
abstract class MainListFragmetBuildersModule {

    @ContributesAndroidInjector() // Attache le fragment au graphe Dagger.
    abstract fun contributeMainListFragment(): MainListFragment
}
```

Ce module construira tous vos fragments liés à `MainActivity`. Il générera `AndroidInjector` pour tous les fragments définis dans cette classe. Les objets peuvent être injectés dans les fragments en utilisant `AndroidSupportInjection.inject(this)` dans la fonction `onAttach` du cycle de vie du fragment.

**Créez le composant de classe `AppComponent`.**

```kotlin
/**
 * Interface de composant singleton pour l'application. Elle lie tous les modules ensemble.
 * Le composant est utilisé pour connecter les objets à leurs dépendances.
 * Dagger auto-générera DaggerAppComponent qui est utilisé pour l'initialisation au niveau de l'Application.
 */
@Singleton
@Component(
        modules = [
            // AndroidSupportInjectionModule est une classe de Dagger et nous n'avons pas besoin de la créer.
            // Si vous voulez utiliser l'injection dans un fragment, vous devez utiliser AndroidSupportInjectionModule.class sinon utilisez AndroidInjectionModule.
            AndroidSupportInjectionModule::class,
            AppModule::class,
            ActivityBuildersModule::class
        ]
)
interface AppComponent {

    @Component.Builder // Utilisé pour l'instanciation d'un composant.
    interface Builder {

        @BindsInstance // Lie notre instance d'application à notre graphe Dagger.
        fun application(application: App): Builder

        fun build(): AppComponent
    }

    // L'application qui est autorisée à demander les dépendances déclarées par les modules
    // (au moyen de l'annotation @Inject) doit être déclarée ici avec des méthodes inject() individuelles.
    fun inject(app: App)
}
```

Le composant est une classe très importante. Il permettra à tout ce qui précède de commencer à fonctionner ensemble. Il le fait en connectant les objets à leurs dépendances. Dagger utilisera cette interface pour générer le code nécessaire à l'exécution de l'injection de dépendances.

Pour créer une classe de composant, vous devrez utiliser l'annotation Dagger `@Component`. Elle prend une liste de modules en entrée. Une autre annotation `@Component.Builder` nous permet de lier une instance au composant.

**Ensuite, générez un objet de graphe.**

À ce stade, vous avez tous vos modules et votre composant configurés. Vous pouvez générer votre objet de graphe en sélectionnant Build -> Make Module dans votre IDE Android Studio. Nous aurons besoin de cette génération pour les étapes futures.

**Maintenant, créez une interface `Injectable`.**

```kotlin
/**
 * C'est juste une interface marqueur vide, qui indique d'injecter automatiquement les activités ou fragments s'ils l'implémentent.
 */
interface Injectable
```

Cela sera également nécessaire pour les étapes futures. L'interface `Injectable` doit être implémentée par les activités ou fragments que nous voulons injecter automatiquement.

**Créez une nouvelle classe d'assistance nommée `AppInjector`.**

```kotlin
/**
 * C'est une classe d'assistance simple pour éviter d'appeler la méthode inject sur chaque activité ou fragment.
 */
object AppInjector {
    fun init(app: App) {
        // Ici nous initialisons Dagger. DaggerAppComponent est auto-généré à partir de AppComponent.
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
            // L'appel de la méthode inject() provoquera la localisation par Dagger des singletons dans le graphe de dépendances pour essayer de trouver un type de retour correspondant.
            // Si elle en trouve un, elle assigne les références aux champs respectifs.
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

Ce n'est qu'une simple classe d'assistance pour éviter d'appeler la méthode inject sur chaque activité ou fragment.

**Ensuite, configurez la classe `App` que nous avons déjà créée précédemment.**

```kotlin
class App : Application(), HasActivityInjector {

    @Inject // Il implémente la machinerie Dagger de recherche de l'injecteur factory approprié pour un type.
    lateinit var dispatchingAndroidInjector: DispatchingAndroidInjector<Activity>

    override fun onCreate() {
        super.onCreate()

        // Initialiser afin d'injecter automatiquement les activités et fragments s'ils implémentent l'interface Injectable.
        AppInjector.init(this)

        ...
    }


    // Ceci est requis par l'interface HasActivityInjector pour configurer Dagger pour Activity.
    override fun activityInjector(): AndroidInjector<Activity> = dispatchingAndroidInjector
}
```

Parce que l'application a des activités, nous devons implémenter l'interface `HasActivityInjector`. Si vous voyez une erreur signalée par Android Studio sur `DaggerAppComponent`, c'est parce que vous n'avez pas généré un nouveau fichier, comme cela a été souligné dans l'étape précédente.

**Alors, configurez `MainActivity` pour injecter la factory principale de ViewModel et ajoutez un support pour les injections de fragments.**

```kotlin
// Pour supporter l'injection de fragments qui appartiennent à cette activité, nous devons implémenter HasSupportFragmentInjector.
// Nous n'aurions pas besoin de l'implémenter si notre activité ne contenait aucun fragment ou si les fragments n'avaient pas besoin d'injecter quoi que ce soit.
class MainActivity : AppCompatActivity(), HasSupportFragmentInjector {

    @Inject
    lateinit var dispatchingAndroidInjector: DispatchingAndroidInjector<Fragment>

    @Inject
    lateinit var viewModelFactory: ViewModelProvider.Factory
    private lateinit var mainViewModel: MainViewModel


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Obtenez ViewModel à partir de ViewModelProviders, en utilisant cette activité comme LifecycleOwner.
        mainViewModel = ViewModelProviders.of(this, viewModelFactory).get(MainViewModel::class.java)

        ...
    }

    ...

    override fun supportFragmentInjector(): AndroidInjector<Fragment> = dispatchingAndroidInjector

    ...
}
```

Parce que nos activités ont des fragments enfants, nous devons implémenter l'interface `HasSupportFragmentInjector`. Nous en avons également besoin car nous prévoyons de faire des injections dans nos fragments. Notre activité ne doit pas savoir comment elle est injectée. Nous utilisons la ligne de code `AndroidInjection.inject(this)` à l'intérieur de la méthode `onCreate()` redéfinie.

L'appel de la méthode `inject()` provoquera la localisation par Dagger 2 des singletons dans le graphe de dépendances pour essayer de trouver un type de retour correspondant. Cependant, nous n'avons pas besoin d'écrire de code ici car cela est fait pour nous par la classe d'assistance `AppInjector` précédemment créée que nous avons initialisée à l'intérieur de notre classe d'application.

**Ensuite, configurez `MainListFragment` pour injecter la factory principale de ViewModel.**

```kotlin
/**
 * Un fragment de remplissage contenant une vue simple.
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

        // Obtenez ViewModel à partir de ViewModelProviders, en utilisant l'activité parente comme LifecycleOwner.
        viewModel = ViewModelProviders.of(activity, viewModelFactory).get(MainViewModel::class.java)
        
        ...

    }

}
```

De manière similaire aux activités, si nous voulons que notre fragment soit injectable, alors dans sa méthode `onAttach`, nous devrions écrire le code `AndroidSupportInjection.inject(this)`. Mais encore une fois, c'est un travail fait par l'assistant `AppInjector`, donc nous pouvons sauter cela. Remarquez simplement que nous devons ajouter l'interface `Injectable` que nous avons créée précédemment pour que l'assistant fonctionne.

Félicitations, nous avons implémenté Dagger 2 dans le projet de l'application My Crypto Coins. Bien sûr, cet article est un guide rapide pour déployer Dagger 2 dans votre application immédiatement, mais pas une couverture approfondie. Je vous recommande de continuer à rechercher ce sujet si vous vous sentez perdu sur les bases.

### Dépôt

Consultez le code source de l'application mise à jour « Kriptofolio » (anciennement « My Crypto Coins ») sur GitHub.

#### [Voir la source sur GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-4)



---

**_Ačiū! Merci d'avoir lu! J'ai initialement publié cet article pour mon blog personnel [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-4/) le 7 octobre 2018._**