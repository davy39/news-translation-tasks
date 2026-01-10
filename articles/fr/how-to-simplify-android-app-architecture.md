---
title: 'Comment simplifier l''architecture de votre application Android : un guide
  détaillé avec des exemples de code'
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
seo_title: 'Comment simplifier l''architecture de votre application Android : un guide
  détaillé avec des exemples de code'
seo_desc: 'By Vitaly Kuprenko

  Individual programmers develop their mobile apps according to their vision, including
  their ideas and views on how to perform various tasks. Sometimes they might disregard
  the main principles of object oriented or functional progra...'
---

Par Vitaly Kuprenko

Les programmeurs individuels développent leurs applications mobiles selon leur vision, incluant leurs idées et vues sur la manière d'effectuer diverses tâches. Parfois, ils peuvent ignorer les principes fondamentaux de la programmation orientée objet ou fonctionnelle, ce qui peut entraîner une désorientation parmi les développeurs. 

C'est mauvais - ils ne pourront pas gérer leur code. Et le prochain développeur qui doit maintenir le projet ou le modifier peut devenir fou. Il est préférable de reconstruire de tels projets à partir de zéro, puisque la maintenance devient un processus compliqué. 

Jusqu'à ce que Google publie sa première architecture supportée, presque toutes les entreprises de développement de logiciels utilisaient leur propre architecture. Cela les aidait à rendre leur code plus clair et permettait de passer d'un projet à l'autre. Mais si un développeur changeait d'entreprise, il lui faudrait un certain temps pour apprendre cette nouvelle architecture ainsi qu'un nouveau projet.

À l'heure actuelle, il existe 16 architectures différentes pour les développeurs Android, grâce à Google : 


* 6 échantillons stables (Java) ;
* 2 échantillons stables (Kotlin) ;
* 4 échantillons externes ;
* 3 échantillons obsolètes ;
* 1 échantillon en cours.

L'architecture que vous utilisez dépend de votre objectif spécifique, de votre approche et de l'application de divers kits d'outils pour la mise en œuvre de diverses fonctionnalités. Et cela dépend du langage de programmation. 

Cependant, toutes ces architectures ont une base architecturale commune qui divise presque également la logique pour travailler avec les réseaux, les bases de données, les dépendances et le traitement des rappels.

### Outils utilisés pendant le processus

Après avoir étudié toutes ces architectures, j'ai construit une approche simplifiée et j'ai créé une architecture avec moins de couches. Je vais vous montrer comment implémenter une application Android simple qui charge une liste de nouvelles, vous permet de sauvegarder des histoires dans les Favoris, puis de les supprimer si nécessaire en utilisant mon approche.

![Image](https://lh3.googleusercontent.com/h4o-H8Gb3UK9O2m52fv_jkjTQ_jAq3CLqi4t7nGat9ZdyuqzxmxYgmmwV_zEULcO4oGonWs0z1mm4VuXS51WjFEBpcDrXSsR4mMkVhVrd51-2VHYBiUUx4Ci2JOzTYEpIievGlpX)

Voici un résumé de la technologie que j'ai utilisée :

* **Kotlin** pour développer l'application ainsi que la bibliothèque **AndroidX** 
* **Room SQLite** comme base de données 
* **Stetho** pour parcourir les données dans les bases 
* **Retrofit2** avec RxJava2 pour aider à journaliser les requêtes serveur et obtenir les réponses du serveur. 
* **Glide** pour traiter les images
* **Android Architecture Components** (LiveData, ViewModel, Room) et **ReactiveX** (RxJava2, RxKotlin et RxAndroid) pour construire des dépendances, des changements de données dynamiques et traiter l'asynchronisme.  

Donc, voici la [pile technologique de l'application mobile](https://www.cleveroad.com/blog/choosing-the-right-technology-stack-for-mobile-application) que j'ai utilisée pour mon projet. 

**Commençons**

### Premières étapes

Connectez **AndroidX**. Dans **gradle.properties** au niveau de l'application, écrivez ce qui suit :

```
android.enableJetifier=true
android.useAndroidX=true
```

Maintenant, il est nécessaire de remplacer les dépendances dans **build.gradle** au niveau du module de l'application d'Android à AndroidX. Vous devez extraire toutes les dépendances vers **ext**, comme vous pouvez le voir dans l'exemple de la version Kotlin hors de la boîte dans **build.gradle** au niveau de l'application. Et ensuite, j'ajoute la version Gradle là :

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

        // NOTE: Ne placez pas vos dépendances d'application ici ; elles appartiennent
        // dans les fichiers build.gradle des modules individuels
    }
}
```

Pour toutes les autres dépendances, je vais construire son fichier **ext**, où j'ajoute absolument toutes les dépendances incluant les versions du SDK, en divisant la version et en créant des massifs de dépendances qui seront implémentés plus loin dans **build.gradle** au niveau de l'application. Cela ressemblera à ce qui suit :

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

Le nom de la version et des massifs est implémenté aléatoirement. Après cela, nous implémenterons les dépendances dans **build.gradle** au niveau de l'application comme suit :

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

N'oubliez pas de spécifier **multiDexEnabled true** dans les configurations par défaut. Dans la plupart des cas, vous atteindrez rapidement la limite du nombre de méthodes utilisées. 

De la même manière, vous devez déclarer toutes les dépendances de l'application. Ajoutons des permissions pour connecter notre application à Internet :

```
 <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.INTERNET" />
```

Si aucun nom n'est ajouté dans le manifest, vous devez le faire puisque **Stetho** ne verra pas l'application sans nom et vous ne pourrez pas regarder dans la base de données. 

### Construction des composants de base

Il est à noter que le modèle MVVM ([Model-View-ViewModel](https://www.journaldev.com/20292/android-mvvm-design-pattern)) a été utilisé comme base pour construire cette architecture. 

Commençons le développement. La première chose à faire est de créer une classe qui héritera de Application(). Dans cette classe, nous donnerons accès au contexte de l'application pour son utilisation ultérieure.

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

La deuxième étape consiste à créer les composants de base de l'application en commençant par [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel), que j'utiliserai pour chaque Activity ou Fragment.   


```
abstract class BaseViewModel constructor(app: Application) : AndroidViewModel(app) {

    override fun onCleared() {
        super.onCleared()
    }
}
```

Cette application n'a pas de fonctionnalités compliquées. Mais dans le ViewModel de base, nous mettrons **3 principaux [LiveData](https://developer.android.com/reference/android/arch/lifecycle/MediatorLiveData)** : 

* traitement des erreurs 
* traitement du chargement avec la barre de progression affichée 
* et, puisque j'ai une application avec des listes, traitement de la réception et de la disponibilité des données dans l'adaptateur en tant que placeholder qui s'affiche en leur absence.

```
val errorLiveData = MediatorLiveData<String>()
    val isLoadingLiveData = MediatorLiveData<Boolean>()
    val isEmptyDataPlaceholderLiveData = MediatorLiveData<Boolean>()
```

Pour transférer les résultats de l'implémentation de la fonction à LiveData, j'utiliserai **[Consumer](http://reactivex.io/RxJava/javadoc/io/reactivex/functions/Consumer.html)**.

Pour traiter les erreurs à n'importe quel endroit dans l'application, vous devez créer un Consumer qui transférera la valeur **Throwable.message** à **errorLiveData**.

De plus, dans le ViewModel de base, vous devrez créer une méthode qui recevra une liste LiveData pour afficher la barre de progression pendant leur implémentation.

Notre ViewModel de base ressemblera à ceci :

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

  
Dans notre application, il n'a pas de sens de créer plusieurs Activities pour deux écrans (écran de liste de nouvelles et écran de liste des favoris). Mais puisque cet exemple montre l'implémentation d'une architecture optimale et facilement extensible, je vais créer une application de base.  

Notre application sera construite sur 1 Activity et 2 Fragments que nous allons gonfler dans l'activité Container. Le fichier XML de notre Activity sera le suivant :

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

où **include_placeholder** et **include_progressbar** ressembleront à ceci :

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

Notre BaseActivity ressemblera à ceci :

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

Implémentons comment afficher les erreurs possibles dans les processus de toutes les futures Activities. Je vais le faire sous la forme d'un simple Toast pour simplifier. 

```
protected open fun processError(error: String) = Toast.makeText(this, error, Toast.LENGTH_SHORT).show()
```

et envoyer ce texte d'erreur à la méthode d'affichage : 

```
protected open val errorObserver = Observer<String> { it?.let { processError(it) } }
```

Dans l'Activity de base, je vais commencer à suivre les changements de la valeur **errorLiveData** qui se trouve dans le ViewModel de base. La méthode **startObserveLiveData()** va muter comme suit :

```
private fun startObserveLiveData() {
        observeLiveData(viewModel)
        with(viewModel) {
            errorLiveData.observe(this@BaseActivity, errorObserver)
        }
    }
```

Maintenant, en utilisant **onErrorConsumer** du ViewModel de base comme processeur **onError**, vous verrez le message concernant l'erreur de la méthode implémentée.

Créez une méthode qui vous permet de remplacer les Fragments dans Activity avec la possibilité d'ajouter à la pile de retour.

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

Créons des interfaces pour afficher la progression et le placeholder dans les emplacements requis de l'application.

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

Implémentez-les dans l'Activity de base. J'ai créé des fonctions de définition de l'ID pour la barre de progression et le placeholder, et j'ai également initialisé ces vues.

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

Et enfin, dans la méthode **onCreate**, je définis un ID pour View :

```
if (hasProgressBar()) {
            vProgress = findViewById(progressBarId())
            vProgress?.setOnClickListener(null)
        }
        vPlaceholder = findViewById(placeholderId())
        startObserveLiveData()
```

J'ai détaillé la création du ViewModel de base et de l'Activity de base. Le Fragment de base sera créé selon le même principe. 

Lorsque vous créez chaque écran séparé, si vous envisagez une extension ultérieure et des modifications possibles, vous devez créer un Fragment séparé avec son ViewModel. 

Remarque : dans le cas où les Fragments peuvent être combinés en un seul cluster, et que la logique métier n'implique pas une complexité massive, plusieurs Fragments peuvent utiliser un seul ViewModel. 

Le passage entre les Fragments se fait grâce aux interfaces qui sont implémentées dans Activity. Pour ce faire, chaque Fragment doit avoir un **companion object{ }** avec la méthode de construction de l'objet Fragment avec la possibilité de transfert d'arguments à **Bundle** :

```
companion object {
        fun newInstance() = FavoriteFragment().apply { arguments = Bundle() }
    }
```

### Solutions d'architecture

Lorsque les composants de base sont créés, il est temps de se concentrer sur l'architecture. Schématiquement, cela ressemblera à l'architecture propre créée par le célèbre Robert C. Martin ou Uncle Bob. Mais puisque j'utilise **RxJava2**, je me suis débarrassé des interfaces **Boundaries** (comme moyen de garantir l'exécution de la **Dependency Rule**) en faveur de l'**Observable** et du **Subscriber** standard. 	

En plus de cela, en utilisant les outils **RxJava2**, j'ai intégré la conversion de données pour un travail plus flexible avec celles-ci. Cela concerne à la fois le travail avec les réponses du serveur et avec les bases de données. 

En plus du modèle principal, je vais créer un modèle de réponse du serveur et un modèle de table séparé pour **Room**. En convertissant les données entre ces deux modèles, vous pouvez apporter des modifications pendant le processus de conversion, convertir les réponses du serveur et sauvegarder les données nécessaires dans la base avant qu'elles ne s'affichent sur l'UI, etc. 

Les Fragments sont responsables de l'**UI**, et les ViewModel des Fragments sont responsables de l'exécution de la logique métier. Si la logique métier concerne toute l'activité, alors ViewModel Activity. 

Les ViewModels obtiennent les données d'un fournisseur par son initialisation via **val … by lazy{}**, si vous avez besoin d'un objet invariable, ou **lateinit var**, si c'est l'inverse. Après l'exécution de la logique métier, si vous devez transférer des données pour changer l'**UI**, vous créez un nouveau **MutableLiveData** dans le ViewModel que vous utiliserez dans la méthode **observeLiveData()** de notre Fragment. 

Cela semble assez facile. La mise en œuvre est également simple.   
Un composant essentiel de notre architecture est un convertisseur de données basé sur une conversion simple d'un type de données à un autre. Pour la conversion du flux de données **RxJava**, [**SingleTransformer**](http://reactivex.io/RxJava/javadoc/io/reactivex/SingleTransformer.html) ou [**FlowableTransformer**](http://reactivex.io/RxJava/javadoc/io/reactivex/FlowableTransformer.html) sont utilisés en fonction du type. Dans le cas de notre application, l'interface et la classe abstraite du convertisseur ressemblent à ce qui suit :

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

Dans cet exemple, j'utilise des conversions de base telles que modèle-modèle, liste de modèles - liste de modèles, et les mêmes combinaisons mais en utilisant uniquement **SingleTransformer** pour le traitement des réponses du serveur et des requêtes dans la base de données.

Commençons par le réseau - avec la méthode **RestClient.retrofitBuilder** qui sera la suivante :

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

En utilisant des API tierces, il y a toujours une chance d'obtenir une réponse nulle absolue du serveur, et il peut y avoir de nombreuses raisons à cela. C'est pourquoi un **NullOrEmptyConverterFactory** supplémentaire aidera à gérer la situation. Voici à quoi il ressemble :

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

Pour créer des modèles, il est nécessaire de se baser sur une API. En tant qu'exemple, j'utiliserai l'API gratuite pour un usage non commercial de **newsapi.org.** Elle dispose d'une liste assez extensive de fonctionnalités demandées, mais je vais utiliser une petite partie pour cet exemple. Après une inscription rapide, vous obtenez accès à l'API et à votre **clé API** qui est requise pour chaque requête. 

En tant que point de terminaison, j'utiliserai [**https://newsapi.org/v2/everything**](https://newsapi.org/v2/everything)**.** Parmi les **query** suggérées, je choisis les suivantes : **q** - requête de recherche, **from** - tri à partir de la date, **to** - tri jusqu'à la date, **sortBy** - tri selon le critère sélectionné, et la **apiKey** obligatoire.

Après la création de **RestClient**, je crée une interface API avec la Query sélectionnée pour notre application :

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

Nous recevrons cette réponse dans NewsNetworkModel :

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

Ces données de la réponse entière suffiront pour afficher une liste avec une image, un titre et une description de nouvelles. 

Pour la mise en œuvre de notre approche architecturale, créons des modèles généraux :

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

Puisque le modèle Article sera utilisé pour la connexion avec la base de données et l'affichage des données dans l'adaptateur, nous devons ajouter 2 marges que j'utiliserai pour changer les éléments de l'UI dans la liste. 

Lorsque tout est prêt pour la requête, je crée des convertisseurs pour les modèles réseau que nous utiliserons dans la requête de réception de nouvelles via NetworkModule.

Les convertisseurs sont créés dans l'ordre inverse de la imbrication, et ils convertissent dans l'ordre direct en conséquence. Donc le premier que je crée sur Article, le second sur News :

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

Comme vous pouvez le voir ci-dessus, lors de la conversion de l'objet News, la conversion de la liste des objets Article est également exécutée.

Une fois les convertisseurs pour les modèles réseau créés, procédons à la création du module (réseau de dépôt). Puisqu'il y a généralement plus d'une ou deux API d'interface, vous devez créer BaseModule, API typée, Module réseau et ConversionModel.

Voici à quoi cela ressemble :

```
abstract class BaseNetworkModule<A, NM, M>(val api: A, val dataConverter: BaseDataConverter<NM, M>)
```

En conséquence, cela sera le suivant sur NewsModule :

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

Pour cette API, la clé API est un paramètre crucial pour les requêtes par tous les points de terminaison suggérés. C'est pourquoi vous devez vous assurer que les paramètres optionnels ne seront pas spécifiés à l'avance, et vous devez les annuler par défaut.

Comme vous pouvez le voir ci-dessus, j'ai appliqué la conversion de données pendant le traitement de la réponse.

Travaillons avec la base de données. Je crée la base de données de l'application, je l'appelle **AppDatabase** et j'hérite de **RoomDatabase()**.

Pour l'initialisation de la base de données, il est nécessaire de créer **DatabaseCreator**, qui doit être initialisé dans la classe **App**.

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

Maintenant, dans la méthode **onCreate()** de la classe **App**, j'initialise **Stetho** et la base de données :

```
override fun onCreate() {
        super.onCreate()
        instance = this
        Stetho.initializeWithDefaults(this)
        DatabaseCreator.createDatabase(this)
    }
```

Lorsque la base de données est créée, je crée un Dao de base avec une seule méthode insert() à l'intérieur :

```
@Dao
interface BaseDao<in I> {

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun insert(obj: I)
}
```

Basé sur l'idée de notre application, je vais sauvegarder les nouvelles que j'aime, obtenir la liste des articles sauvegardés, supprimer les nouvelles sauvegardées par leur ID, ou supprimer toutes les nouvelles de la table. Notre **NewsDao** sera le suivant :

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

Et la table des nouvelles sera la suivante :

```
@Entity(tableName = NEWS_TABLE)
data class NewsDatabase(@PrimaryKey var id: Long?,
                        var title: String?,
                        var description: String?,
                        var urlToImage: String?)
```

Lorsque la table est créée, relions-la à une base de données :

```
@Database(entities = [NewsDatabase::class], version = DB_VERSION)
abstract class AppDatabase : RoomDatabase() {

    abstract fun newsDao(): NewsDao
}
```

Maintenant, nous pouvons travailler avec la base de données, sauvegarder et extraire des données de celle-ci.

En ce qui concerne le module (réseau de dépôt), je vais créer un convertisseur de modèle - modèle de table de base de données :

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

BaseRepository est disponible pour travailler avec diverses tables. Écrivons-le. Il ressemblera à ce qui suit dans sa version la plus simple qui est suffisante pour l'application :

```
abstract class BaseRepository<M, DBModel> {

    protected abstract val dataConverter: BaseDataConverter<M, DBModel>
    protected abstract val dao: BaseDao<DBModel>
}
```

Après la création de BaseRepository, je vais créer **NewsRepository** :

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

Lorsque les dépôt et modules permanents sont créés, les données doivent provenir d'un fournisseur d'application qui demandera des données soit à partir du réseau ou de la base de données en fonction des exigences. Un fournisseur doit combiner les deux dépôt. En tenant compte des capacités de divers modèles et dépôt, je vais créer BaseProvider :

```
abstract class BaseProvider<NM, DBR> {

    val repository: DBR = this.initRepository()

    val networkModule: NM = this.initNetworkModule()

    protected abstract fun initRepository(): DBR

    protected abstract fun initNetworkModule(): NM
}
```

  
Ensuite, **NewsProvider** ressemblera à ce qui suit :

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

Maintenant, nous obtiendrons facilement la liste des nouvelles. Dans **NewsViewModel**, nous déclarerons toutes les méthodes de notre fournisseur pour une utilisation ultérieure :

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

Ayant déclaré toutes les méthodes qui ont exécuté la logique métier dans ViewModel, nous les rappelerons depuis Fragment où dans **observeLiveData()** les résultats de chaque **LiveData** déclaré seront traités.

Pour l'implémenter facilement, dans les paramètres **SEARCH_FOR**, j'ai choisi aléatoirement **Apple**, et le tri ultérieur sera effectué par le tag **popularity**. Si nécessaire, vous pouvez ajouter une fonctionnalité minimale pour changer ces paramètres.

Puisque newsapi.org ne vous fournit pas d'ID de nouvelles, j'accepte l'index de l'élément comme ID. Le tri par le tag de popularité est également implémenté via l'API. Mais pour éviter la réécriture des données avec les mêmes ID dans la base lors du tri par popularité, je vais vérifier la disponibilité des données dans la base avant le chargement de la liste des nouvelles. Si la base est vide - la nouvelle liste est chargée, sinon - une notification est affichée. 

Appelons dans la méthode **onViewCreated()** de **NewsFragment** la méthode suivante :

```
private fun loadLikedNews() {
        viewModel.loadLikedNews()
    }
```

Puisque notre base est vide, la méthode **loadNews()** sera lancée. Dans la méthode **observeLiveData**, j'utiliserai notre LiveData de chargement - **viewModel.loadNewsSuccessLiveData.observe(..){news →}**, où nous recevrons la liste des articles de nouvelles si la requête est réussie, puis nous la transférerons à l'adaptateur :

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

Ayant lancé l'application, vous verrez le résultat suivant :

![Image](https://lh4.googleusercontent.com/SSyMu9byyX01H_baLGzU_oN7KuDnbhS4lcNnQjAbxlATJNrA8wFJyGJl1klH7LVijAu0yOD9k0M57cjprTbdjIOLpNl2SUl_A6rqqNv-IcREaaa4wIIlfRPRrDVpRza3GOl-6834)

Dans le menu de la barre d'outils sur le côté droit, vous pouvez voir 2 options - tri et favoris. Trions la liste par popularité et obtenons le résultat suivant :

![Image](https://lh3.googleusercontent.com/7BT2Por_XNJwm3mdCc4JdW0cTl8-SVOfPagn2fOklb4z9TbGDWPxb-wCAhE2V9rzUQog_ICI-I2AX4xh7NGrm50mS1BQDhafahJJwk9C_qsHcs_P3sK6T6vigj-pwcddsOmiKvq4)

Si vous allez dans Favoris, vous verrez uniquement un Placeholder, car il n'y a pas de données dans la base. L'écran des Favoris ressemblera à ceci :

![Image](https://lh4.googleusercontent.com/E2V2sR15Pb23PsfVOv1K91_Ma7eJV5DZUUbu4LPH4Dq-rvfR6iU6qTn-grnDR2HCcgiKSK0EFEAIG0GH-gX2pR06iNCM8j3ZouIf5dHPHEEPUCBZ5z6pEhfRx2NBRvwkZ4oonnkv)

Le fragment UI des Favoris a un écran pour l'affichage de la liste des nouvelles aimées et une seule option dans la barre d'outils pour le nettoyage de la base de données. Lorsque vous sauvegardez des données en cliquant sur « Like », les écrans ressembleront à ceci :

![Image](https://lh4.googleusercontent.com/4E-JQL94Qwa5GxRzfap0InOW60v-zeGUuKNFFJV_g7uyjTj1TubpKDvWsD7XgLBApzV55zJdVAHpFnDxYpPe6bL2Ntv9YAmlDhVzuFsLctFw6NJPWBz1RPnJN8CZ2wRMsPvJOrd3)

Comme je l'ai écrit ci-dessus, dans le modèle standard, 2 marges supplémentaires ont été ajoutées au modèle général, et ces marges sont utilisées pour l'affichage des données dans l'adaptateur. Maintenant, vous pouvez voir que les éléments de la liste des nouvelles sauvegardées n'ont pas d'option pour ajouter aux Favoris. 

```
var isAddedToFavorite: Boolean?
    var fragmentName: FragmentsNames?
```

Si vous cliquez à nouveau sur « Like », l'élément sauvegardé sera supprimé de la base.

### Conclusion

Ainsi, je vous ai montré une approche simple et claire pour le développement d'applications Android. Nous avons respecté les principes fondamentaux de Clean Architecture mais l'avons simplifiée autant que possible. 

Quelle est la différence entre l'architecture que je vous ai fournie et Clean Architecture de M. Martin ? Au tout début, j'ai noté que mon architecture est similaire à CA puisque elle est utilisée comme base. Voici le schéma CA ci-dessous :

![Image](https://lh4.googleusercontent.com/avSMw0B5pCLWAVWjES8gIJ5KU6OInVAG8DmYd7CIRhOx8Z4cGRLDMECv7HqHgNyTwBCe7Q0eY8VD6tw8zZWNdb5emxWrjP8IBQvMr8YGbySiygiTqG3N2BQsebB6JDFrGtRq4fax)

L'événement va à Presenter, puis à **Use Case. Use Case** demande **Repository.** Repository reçoit les données, crée **Entity,** et les transfère à **UseCase.** Ainsi, **Use Case** reçoit toutes les Entités nécessaires. Après la mise en œuvre de la logique métier, vous obtenez le résultat qui revient à **Presenter,** et celui-ci, à son tour, transfère le résultat à **UI.**  

Dans le schéma ci-dessous, **Controller** appelle des méthodes à partir de **InputPort** qui implémente **UseCase**, et l'interface **OutputPort** reçoit cette réponse et **Presenter** l'implémente. Au lieu de **UseCase** dépendant directement de **Presenter**, il dépend de l'interface dans ses couches, et cela ne contredit pas avec **Dependency Rule**, et Presenter doit implémenter cette interface.

![Image](https://lh4.googleusercontent.com/zCxRkWYDl8TKPyQUqBNvGHN45wj51N-B4hZGjn0ul6Kvj6IVERtYIQiICH6JEC5RiZQFbMWmtQllSXx0LhndE-GAm21J_-nMrfEOA4nz8paAkolm0JQidxBHc3OcF0TiDoRIU36j)

Ainsi, les processus qui sont implémentés dans la couche externe n'affectent pas les processus dans la couche interne. Qu'est-ce qu'Entity dans Clean Architecture ? En fait, c'est tout ce qui ne dépend pas d'une application spécifique, et ce sera un concept général pour de nombreuses applications. Mais dans le processus de développement mobile, Entity est les objets métier de l'application, qui contiennent des règles générales et de haut niveau (logique métier de l'application). 

Qu'en est-il des **Gateways** ? À mon avis, **Gateways** est un dépôt pour travailler avec la base de données et un module pour travailler avec un réseau. Nous nous sommes débarrassés du contrôleur puisque initialement Clean Architecture a été créée pour structurer des applications métier de haute complexité, et les convertisseurs de données remplissent ses fonctions dans mon application. Les ViewModels transfèrent les données aux Fragments pour le traitement de l'UI en remplaçant les Presenters. 

Dans mon approche, je respecte également strictement la Dependency Rule, et la logique des dépôt, modules, modèles et fournisseurs est encapsulée, et l'accès à ceux-ci est possible via des interfaces. Ainsi, les changements dans les couches externes n'affectent pas les couches internes. Et le processus de mise en œuvre utilisant **RxJava2**, **KotlinRx**, et **Kotlin LiveData** facilite les tâches du développeur, les rend plus claires, et le code devient bien lisible et facilement extensible.