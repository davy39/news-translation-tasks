---
title: 'Tout sur cette architecture : exploration des différents modèles d''architecture
  et comment les utiliser dans votre application'
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
seo_title: 'Tout sur cette architecture : exploration des différents modèles d''architecture
  et comment les utiliser dans votre application'
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 3

  The most important thing to focus on when starting to build a new app is architecture.
  The biggest mistake you can make is to go with no architecture style at all.

  The topic of architecture choice h...'
---

Par Andrius Baruckis

#### Série d'applications Kriptofolio - Partie 3

La chose la plus importante sur laquelle se concentrer lorsque vous commencez à construire une nouvelle application est l'architecture. La plus grande erreur que vous puissiez faire est de ne pas avoir de style d'architecture du tout.

Le sujet du choix de l'architecture a été assez controversé pour la communauté Android ces dernières années. Même Google a décidé de s'impliquer. En 2017, ils ont proposé leur propre approche d'architecture standardisée en publiant les Android Architecture Components. Cela était destiné à faciliter la vie des développeurs.

Dans cet article, je vais d'abord discuter de la raison pour laquelle nous devons architecturer nos applications. Nous verrons quelles options nous avons. Ensuite, nous allons apprendre comment faire cela. Plutôt que de réinventer la roue, nous allons utiliser les directives fournies par l'équipe Android.

Cet article a été le plus difficile à écrire pour moi en raison de mon propre manque de connaissances sur le sujet. J'ai d'abord dû étudier le sujet de l'architecture vraiment bien pour voir le tableau d'ensemble. Maintenant, je suis prêt à partager mes découvertes avec vous.

### Contenu de la série

* [Introduction : Une feuille de route pour construire une application Android moderne en 20182019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Partie 1 : Une introduction aux principes SOLID](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* [Partie 2 : Comment commencer à construire votre application Android : création de maquettes, UI et mises en page XML](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* Partie 3 : Tout sur cette architecture : exploration des différents modèles d'architecture et comment les utiliser dans votre application (vous êtes ici)
* [Partie 4 : Comment implémenter l'injection de dépendances dans votre application avec Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* [Partie 5 : Gérer les services Web RESTful en utilisant Retrofit, OkHttp, Gson, Glide et Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### Pourquoi devriez-vous vous soucier de l'architecture de l'application ?

Habituellement, lorsque vous commencez à travailler avec Android, vous finissez par écrire la plupart de la logique métier principale dans les activités ou les fragments. Cela arrive à tous les nouveaux développeurs Android, y compris moi-même. Tous les tutoriels courts et tous les exemples suggèrent de faire cela. Et en fait, pour les petites applications créées à des fins d'explication, cela fonctionne assez bien.

Cependant, essayez de faire cela sur une vraie application qui change constamment selon les besoins des utilisateurs et qui s'étend avec de nouvelles fonctionnalités. Vous verrez bientôt que votre expérience de codage devient de plus en plus douloureuse. Tout est géré par les soi-disant "classes Dieu" comme les activités ou les fragments. Ceux-ci ont tant de lignes de code que vous vous perdez facilement.

En gros, tout votre code commence à ressembler à des spaghettis où tout est mélangé. Toutes les parties dépendent les unes des autres. Ensuite, lorsque de nouveaux changements sont requis par l'entreprise, vous n'avez pas d'autre choix que de reconstruire l'ensemble du projet. C'est aussi le moment où les questions d'architecture commencent à apparaître.

### Existe-t-il une meilleure façon de structurer votre code ?

Bien sûr que oui ! La clé pour un code de haute qualité est de suivre les principes SOLID. J'en ai parlé dans mon précédent article (pas sans raison). Vous devriez également appliquer un modèle d'architecture pour la séparation des préoccupations. En fait, la séparation des préoccupations devrait être votre objectif ultime. C'est le point le plus significatif qui indique la qualité du code. Il existe plusieurs modèles pour les architectures d'applications. Les plus connus sont les architectures classiques à trois niveaux telles que :

* MVC : Modèle-Vue-Contrôleur
* MVP : Modèle-Vue-Présentateur
* MVVM : Modèle-Vue-ViewModel

Tous ces modèles représentent la même idée principale  structurer le code de votre projet de manière à ce qu'il soit séparé par les différentes couches génériques. Chaque couche a sa propre responsabilité. C'est pourquoi votre projet devient modulaire : les parties de code séparées sont plus testables, et votre application est suffisamment flexible pour des changements continus.

Si nous parlons de chaque modèle individuellement, le sujet devient trop large. Je vais seulement vous introduire à chacun d'eux pour que vous puissiez comprendre les principales différences.

### Le modèle Modèle-Vue-Contrôleur (MVC)

Ce modèle était la première itération de l'architecture des applications Android à l'époque. Il suggère que vous sépariez votre code en 3 couches différentes :

Modèle  la couche de données. Responsable de la gestion de la logique métier et de la communication avec les couches réseau et base de données.

Vue  la couche d'interface utilisateur (UI). C'est une simple visualisation des données du Modèle.

Contrôleur  la couche logique, est notifié du comportement de l'utilisateur et met à jour le Modèle selon les besoins.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DU4N6tj30K-cdILm.png)

C'est le schéma MVC. On peut voir que le Contrôleur et la Vue dépendent tous deux du Modèle. Le Contrôleur met à jour les données. La Vue obtient les données. Cependant, le Modèle est séparé et pourrait être testé indépendamment de l'UI.

Il existe plusieurs approches pour appliquer le modèle MVC. C'est assez confus.

L'une d'elles est lorsque les activités et les fragments agissent comme le Contrôleur. Ils sont responsables du traitement des données et de la mise à jour des vues. Le problème avec cette approche architecturale est que les activités et les fragments peuvent devenir assez grands et très difficiles à tester.

Une autre approche qui semble plus logique (et correcte) est celle où les activités et les fragments devraient être les Vues dans le monde MVC. Les Contrôleurs devraient être des classes séparées qui n'étendent ou n'utilisent aucune classe Android. Même chose pour les Modèles.

Quoi qu'il en soit, si vous enquêtez davantage sur MVC, vous découvrirez que lorsqu'il est appliqué à un projet Android, même de la manière correcte, les couches de code dépendent les unes des autres. C'est pourquoi je ne vous recommanderais pas de l'utiliser pour votre prochaine application Android.

### Le modèle Modèle-Vue-Présentateur (MVP)

Après la première approche, qui n'a pas fonctionné, les développeurs Android ont continué et ont essayé d'utiliser l'un des modèles architecturaux les plus populaires  MVP. Ce modèle représente une deuxième itération du choix de l'architecture. Ce modèle est devenu largement utilisé et est toujours recommandé. Pour toute personne qui commence le développement Android, il est facile à apprendre. Examinons les rôles de ses 3 couches séparées :

Modèle  la couche de données, qui est la même que dans le modèle MVC. Responsable de la gestion de la logique métier et de la communication avec les couches réseau et base de données.

Vue  la couche d'interface utilisateur (UI). Affiche les données et notifie le Présentateur des actions de l'utilisateur.

Présentateur  récupère les données du Modèle, applique la logique de l'UI et gère l'état de la Vue, décide quoi afficher et réagit aux notifications d'entrée de l'utilisateur de la Vue. C'est essentiellement le contrôleur du MVC sauf qu'il n'est pas du tout lié à la Vue, juste une interface.

![Image](https://cdn-media-1.freecodecamp.org/images/0*-FvjLCU4hd5O1mjn.png)

Le schéma MVP montre que la Vue et le Présentateur sont étroitement liés. Ils doivent avoir une référence l'un à l'autre. Leur relation est définie dans une classe d'interface `Contract`.

Ce modèle a un inconvénient significatif mais contrôlable. Le Présentateur tend à s'étendre à une classe omnisciente énorme si vous n'êtes pas assez prudent et ne divisez pas votre code selon le principe de responsabilité unique. Cependant, en général, le modèle MVP offre une très bonne séparation des préoccupations. Il pourrait être votre choix principal pour votre projet.

### Le modèle Modèle-Vue-ViewModel (MVVM)

Le modèle MVVM est la troisième itération de l'approche. Il est devenu le modèle d'architecture recommandé par l'équipe Android avec la sortie des Android Architecture Components. C'est pourquoi nous allons nous concentrer sur l'apprentissage de ce modèle plus que tout. De plus, je vais l'utiliser pour l'application "My Crypto Coins". Comme avant, examinons ses couches de code séparées :

Modèle  abstrait la source de données. Le ViewModel travaille avec le Modèle pour obtenir et sauvegarder les données.

Vue  informe le ViewModel des actions des utilisateurs.

ViewModel  expose des flux de données pertinents pour la Vue.

La différence par rapport au modèle MVP est que, dans MVVM, le ViewModel ne détient pas de référence à la Vue comme c'est le cas avec le Présentateur. Dans MVVM, le ViewModel expose un flux d'événements auquel diverses Vues peuvent se lier. D'autre part, dans le cas du MVP, le Présentateur dit directement à la Vue quoi afficher. Examinons le schéma MVVM :

![Image](https://cdn-media-1.freecodecamp.org/images/0*wgul-7f3_G5PcN8T.png)

Dans MVVM, la Vue a une référence au ViewModel. Le ViewModel n'a aucune information sur la Vue. Il y a une relation plusieurs-à-un entre la Vue et le ViewModel.

#### Comparaison de MVC vs MVP vs MVVM

Voici un tableau qui résume tous les modèles dont j'ai parlé :

![Image](https://cdn-media-1.freecodecamp.org/images/0*IOIlEBcHQcJrTUks.png)

Comme vous l'avez peut-être remarqué, MVC n'est pas aussi bon que MVP et MVVM lors de la construction d'une application moderne modulaire et testable. Mais chaque modèle a ses propres avantages et inconvénients. C'est un bon choix si cela correspond exactement à vos besoins. Je vous suggère d'enquêter et d'apprendre davantage sur tous ces modèles car cela en vaut la peine.

En attendant, je vais continuer mon projet avec le modèle tendance en 2018, qui est également poussé par Google  MVVM.

### Android Architecture Components

Si vous êtes familier avec le cycle de vie des applications Android, vous savez quel casse-tête cela peut être de construire une application qui évite tous les problèmes de flux de données et les problèmes de persistance et de stabilité qui apparaissent généralement lors des changements de configuration.

En 2017, l'équipe Android a décidé que nous avions assez lutté. Ils ont pris la responsabilité et introduit le framework Android Architecture Components. Cela vous permet enfin de résoudre tous ces problèmes sans compliquer votre code ou même appliquer des hacks.

Android Architecture Components est une collection de bibliothèques qui vous aide à concevoir des applications robustes, testables et maintenables. Au moment où j'écris cet article, il se compose de ces composants :

* [Data Binding](https://developer.android.com/topic/libraries/data-binding)  lie de manière déclarative les données observables aux éléments de l'UI
* [Lifecycles](https://developer.android.com/topic/libraries/architecture/lifecycle)  gère les cycles de vie de vos activités et fragments
* [LiveData](https://developer.android.com/topic/libraries/architecture/livedata)  notifie les vues lorsque la base de données sous-jacente change
* [Navigation](https://developer.android.com/topic/libraries/architecture/navigation)  gère tout ce qui est nécessaire pour la navigation dans l'application
* [Paging](https://developer.android.com/topic/libraries/architecture/paging)  charge progressivement les informations à la demande à partir de votre source de données
* [Room](https://developer.android.com/topic/libraries/architecture/room)  accès fluide à la base de données SQLite
* [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel)  gère les données liées à l'UI de manière consciente du cycle de vie
* [WorkManager](https://developer.android.com/topic/libraries/architecture/workmanager)  gère vos tâches en arrière-plan Android

Avec l'aide des Android Architecture Components, nous allons implémenter le modèle d'architecture MVVM dans l'application My Crypto Coins en suivant ce diagramme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*0-hsCQF-Ry0cV2332YE3Aw.png)

C'est une architecture recommandée par Google. Elle montre comment tous les modules doivent interagir les uns avec les autres. Ensuite, nous allons couvrir uniquement les composants spécifiques des Android Architecture Components que nous allons utiliser dans notre projet.

### Organiser vos fichiers sources

Avant de commencer le développement, nous devons considérer comment organiser les fichiers sources de notre projet. Nous ne pouvons pas laisser cette question sans réponse, car plus tard nous aurions une structure désordonnée difficile à comprendre et à modifier.

Il existe plusieurs façons de le faire. L'une consiste à organiser par catégorie de composant. Par exemple, toutes les activités vont dans leur propre dossier, tous les adaptateurs vont dans leur dossier, etc.

Une autre façon serait d'organiser tout par fonctionnalités de l'application. Par exemple, la recherche et l'ajout de crypto dans la liste de toutes les cryptomonnaies va dans son propre dossier `addsearchlist`. L'idée principale est que vous devez le faire d'une manière spécifique au lieu d'avoir tout placé aléatoirement. J'utilise une sorte de mélange des deux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iP8HHiXOtxWesHowvjhvUQ.png)
_Structure des dossiers de l'application My Crypto Coins_

En plus de la structure des dossiers du projet, vous devriez envisager d'appliquer certaines règles pour nommer les fichiers du projet. Par exemple, lors du nommage des classes Android, vous devriez définir clairement le but de la classe dans le nom.

### ViewModel

Pour commencer le développement de l'architecture de notre application, nous allons d'abord créer le ViewModel. Les ViewModels sont des objets qui fournissent des données pour les composants de l'UI et survivent aux changements de configuration.

Vous pouvez utiliser un ViewModel pour conserver les données pendant tout le cycle de vie d'une activité ou d'un fragment. Les activités et les fragments sont des objets de courte durée. Ils sont créés et détruits fréquemment lorsque l'utilisateur interagit avec une application. Un ViewModel est également mieux adapté à la gestion des tâches liées à la communication réseau, ainsi qu'à la manipulation et à la persistance des données.

Par exemple, créons maintenant un ViewModel pour `MainListFragment` pour séparer les données de l'UI.

```kotlin
class MainViewModel : ViewModel() {
    ...
}
```

Ensuite, obtenez le ViewModel avec une seule ligne de code.

```kotlin
class MainListFragment : Fragment() {
    ...
    private lateinit var viewModel: MainViewModel
    ...
    override fun onActivityCreated(savedInstanceState: Bundle?) {

        super.onActivityCreated(savedInstanceState)

        setupList()

        // Obtenez ViewModel à partir de ViewModelProviders, en utilisant ce fragment comme LifecycleOwner.
        viewModel = ViewModelProviders.of(this).get(MainViewModel::class.java)
        ...
    }
    ...
}
```

En gros, c'est tout, félicitations ! ? Passons à la suite.

### LiveData

LiveData est une classe de détention de données observable. Elle suit le [modèle d'observateur](https://en.wikipedia.org/wiki/Observer_pattern). LiveData est conscient du cycle de vie. Cela signifie qu'elle ne met à jour que les observateurs des composants de l'application (activité, fragment, etc.) qui sont dans un état de cycle de vie actif.

La classe LiveData retourne la dernière valeur des données. Lorsque les données changent, elle retourne la valeur mise à jour. LiveData est mieux adaptée avec ViewModel.

Nous allons utiliser LiveData avec ViewModel comme ceci :

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

Observez les données sur le ViewModel, exposées comme LiveData :

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

        // Obtenez ViewModel à partir de ViewModelProviders, en utilisant ce fragment comme LifecycleOwner.
        viewModel = ViewModelProviders.of(this).get(MainViewModel::class.java)

        // Observez les données sur le ViewModel, exposées comme LiveData
        viewModel.data.observe(this, Observer { data ->
            // Définissez les données exposées par LiveData
            if (data != null) {
                recyclerAdapter.setData(data)
            }
        })
    }
    ...
}
```

Parcourez le dépôt à ce stade de l'historique [ici](https://github.com/baruckis/MyCryptoCoinsApp-Android/tree/622cf980c4fb68efab546eeddf31c4bf5aee7ba1).

### Data Binding

La bibliothèque Data Binding a été créée pour supprimer le code standard nécessaire pour se connecter aux mises en page XML.

Pour utiliser Data Binding dans vos projets Kotlin, vous devrez activer la prise en charge des processeurs d'annotations avec le plugin de compilateur kapt. Ajoutez également le bloc de liaison de données à la configuration gradle Android :

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

Pour utiliser les classes générées par la liaison de données, nous devons mettre tout le code de vue dans des balises `<layout>`. Le concept le plus puissant de la liaison de données est que nous pouvons lier une classe de données à une mise en page XML et les propriétés des éléments directement aux champs.

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

L'adaptateur RecyclerView avec liaison de données ressemblera à ceci :

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

Enfin, plus besoin d'écrire `findViewById` ? Parcourez le dépôt à ce stade de l'historique [ici](https://github.com/baruckis/Kriptofolio/tree/05a05e0cbc1cac0aefc7a0030fd77779da213214).

### Room

Notre application doit stocker des données persistantes de différentes cryptomonnaies que l'utilisateur possède. Cela doit être stocké à l'intérieur de la base de données locale qui est conservée à l'intérieur de l'appareil Android de manière privée.

Pour stocker des données structurées dans une base de données privée, nous allons utiliser une base de données SQLite. C'est souvent le meilleur choix.

Afin de créer la base de données SQLite pour notre application, nous allons utiliser Room. Room est une bibliothèque de persistance créée par l'équipe Android qui est un wrapper au-dessus de SQLite. C'est une couche d'abstraction qui supprime une grande partie du code standard dont vous avez besoin pour interagir avec SQLite. Elle ajoute également une vérification au moment de la compilation de vos requêtes SQL.

La meilleure façon de la considérer est comme un outil ORM (Object Relational Mapper) conçu pour générer automatiquement du code de liaison pour mapper entre vos instances d'objets et les lignes de votre base de données.

Il y a essentiellement 3 composants majeurs dans Room :

1. Entité  ce composant représente une classe qui contient une ligne de base de données. Pour chaque entité, une table de base de données est créée pour contenir les éléments.
2. DAO (Data Access Object)  le composant principal qui est responsable de la définition des méthodes qui accèdent à la base de données.
3. Base de données  un composant qui est une classe de détention qui utilise des annotations pour définir la liste des entités, la liste des DAO, la version de la base de données et sert de point d'accès principal pour la connexion sous-jacente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jT94pc71uD_A2TPN_E2ulg.png)

Suivons ces étapes simples pour configurer Room dans notre application My Crypto Coins :

1. Créez une Entité.

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

Ajoutez quelques informations supplémentaires pour informer Room de sa structure dans la base de données.

2. Créez le DAO.

```kotlin
@Dao
interface MyCryptocurrencyDao {

    @Query("SELECT * FROM Cryptocurrency")
    fun getMyCryptocurrencyLiveDataList(): LiveData<List<Cryptocurrency>>

    @Insert
    fun insertDataToMyCryptocurrencyList(data: List<Cryptocurrency>)
}
```

Pour commencer, nous allons créer un DAO qui nous permet uniquement de récupérer des enregistrements de la table que nous avons créée avec Entity et également d'insérer des données d'exemple.

3. Créez et configurez la Base de données.

Il est important de dire que l'instance de la Base de données devrait idéalement être construite une seule fois par session. Une façon d'y parvenir serait d'utiliser un modèle Singleton.

```kotlin
@Database(entities = [Cryptocurrency::class], version = 1, exportSchema = false)
abstract class AppDatabase : RoomDatabase() {

    abstract fun myCryptocurrencyDao(): MyCryptocurrencyDao


    // La AppDatabase est un singleton pour éviter d'avoir plusieurs instances de la base de données ouvertes en même temps.
    companion object {

        // Marque le champ de support JVM de la propriété annotée comme volatile, ce qui signifie que les écritures dans ce champ sont immédiatement visibles par les autres threads.
        @Volatile
        private var instance: AppDatabase? = null

        // Pour l'instanciation Singleton.
        fun getInstance(context: Context): AppDatabase {
            return instance ?: synchronized(this) {
                instance ?: buildDatabase(context).also { instance = it }
            }
        }

        // Crée et pré-remplit la base de données.
        private fun buildDatabase(context: Context): AppDatabase {
            return Room.databaseBuilder(context, AppDatabase::class.java, DATABASE_NAME)
                    // Pré-remplit la base de données après que onCreate a été appelé.
                    .addCallback(object : Callback() {
                        override fun onCreate(db: SupportSQLiteDatabase) {
                            super.onCreate(db)
                            // Insère les données sur le thread IO.
                            ioThread {
                                getInstance(context).myCryptocurrencyDao().insertDataToMyCryptocurrencyList(PREPOPULATE_DATA)
                            }
                        }
                    })
                    .build()
        }

        // Données d'exemple.
        val btc: Cryptocurrency = Cryptocurrency("Bitcoin", 1, 0.56822348, "BTC", 8328.77, 4732.60, 0.19, -10.60, 0.44, 20.82)
        val eth: Cryptocurrency = Cryptocurrency("Etherium", 2, 6.0, "ETH", 702.99, 4217.94, 0.13, -7.38, 0.79, 33.32)

        val PREPOPULATE_DATA = listOf(btc, eth)

    }

}
```

```kotlin
private val IO_EXECUTOR = Executors.newSingleThreadExecutor()

// Méthode utilitaire pour exécuter des blocs sur un thread d'arrière-plan dédié, utilisé pour le travail io/base de données.
fun ioThread(f : () -> Unit) {
    IO_EXECUTOR.execute(f)
}
```

Comme vous le voyez, au premier lancement, la base de données sera pré-remplie avec des données d'exemple à des fins de test.

4. **Étape supplémentaire.** Créez le Repository.

Le Repository ne fait pas partie des bibliothèques Architecture Components. C'est une meilleure pratique suggérée pour la séparation du code et l'architecture.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_A8UbQDjX8YjzVZ3T7bhNw.png)

Il sert de source unique de vérité pour toutes les données de l'application au cas où vous devriez gérer plusieurs sources de données.

```kotlin
class MyCryptocurrencyRepository private constructor(
        private val myCryptocurrencyDao: MyCryptocurrencyDao
) {

    fun getMyCryptocurrencyLiveDataList(): LiveData<List<Cryptocurrency>> {
        return myCryptocurrencyDao.getMyCryptocurrencyLiveDataList()
    }

    companion object {

        // Marque le champ de support JVM de la propriété annotée comme volatile, ce qui signifie que les écritures dans ce champ sont immédiatement visibles par les autres threads.
        @Volatile
        private var instance: MyCryptocurrencyRepository? = null

        // Pour l'instanciation Singleton.
        fun getInstance(myCryptocurrencyDao: MyCryptocurrencyDao) =
                instance ?: synchronized(this) {
                    instance
                            ?: MyCryptocurrencyRepository(myCryptocurrencyDao).also { instance = it }
                }
    }
}
```

Nous allons utiliser ce repository dans notre ViewModel.

```kotlin
class MainViewModel(myCryptocurrencyRepository: MyCryptocurrencyRepository) : ViewModel() {

    val liveData = myCryptocurrencyRepository.getMyCryptocurrencyLiveDataList()
}
```

Notre code de Fragment évolue également.

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
        // Obtenez ViewModel à partir de ViewModelProviders, en utilisant ce fragment comme LifecycleOwner.
        viewModel = ViewModelProviders.of(this, factory).get(MainViewModel::class.java)

        // Mettez à jour la liste lorsque les données changent en observant les données sur le ViewModel, exposées comme LiveData.
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

Parce que notre classe ViewModel a maintenant un constructeur qui n'est plus vide, nous devons implémenter un modèle de fournisseur d'usine. Cela sera passé à la méthode `ViewModelProviders.of()` comme deuxième paramètre.

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

Parcourez le dépôt à ce stade de l'historique [ici](https://github.com/baruckis/Kriptofolio/tree/b555fd9e2319bd4580122036d71066860fa82589).

### Réflexions finales

Les architectures de conception, dont nous avons discuté dans cette partie, doivent être utilisées comme des directives informées mais pas comme des règles strictes. Je ne voulais pas entrer trop dans les détails sur chaque sujet. Avec les Android Architecture Components, nous avons examiné le processus de codage. Gardez à l'esprit qu'il y a beaucoup plus à apprendre sur chaque composant individuellement et je vous conseille de le faire.

Faisons un résumé de tout ce que nous avons réussi à faire déjà :

* Dans l'application My Crypto Coins, chaque écran séparé a son propre ViewModel. Cela survivra à tout changement de configuration et protégera l'utilisateur de toute perte de données.
* L'interface utilisateur de l'application est de type réactive. Cela signifie qu'elle se mettra à jour immédiatement lorsque les données changeront dans le back-end. Cela est fait avec l'aide de LiveData.
* Notre projet a moins de code car nous nous lions directement aux variables dans notre code en utilisant Data Binding.
* Enfin, notre application stocke les données utilisateur localement à l'intérieur de l'appareil sous forme de base de données SQLite. La base de données a été créée commodément avec le composant Room. Le code de l'application est structuré par fonctionnalités et toute l'architecture du projet est MVVM  un modèle recommandé par l'équipe Android.

### Dépôt

Maintenant, comme vous le voyez, l'application "Kriptofolio" (anciennement "My Crypto Coins") commence vraiment à prendre forme. Avec le dernier commit du dépôt pour cette partie 3, vous pouvez la trouver montrant joliment les données de la base de données pré-remplie pour l'utilisateur avec la valeur totale du portefeuille de détentions calculée correctement.

#### [Voir la source sur GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-3)



---

**_Ačiū! Merci d'avoir lu ! J'ai initialement publié cet article pour mon blog personnel [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-3/) le 22 août 2018._**