---
title: Comment gérer les services web RESTful en utilisant Retrofit, OkHttp, Gson,
  Glide et les Coroutines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-11T08:26:24.000Z'
originalURL: https://freecodecamp.org/news/kriptofolio-app-series-part-5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*F9gJTRqiq_YPvga0sPu_qw.png
tags:
- name: Android
  slug: android
- name: Cryptocurrency
  slug: cryptocurrency
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: web services
  slug: web-services
seo_title: Comment gérer les services web RESTful en utilisant Retrofit, OkHttp, Gson,
  Glide et les Coroutines
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series — Part 5

  These days almost every Android app connects to internet to get/send data. You should
  definitely learn how to handle RESTful Web Services, as their correct implementation
  is the core knowledge while...'
---

Par Andrius Baruckis

#### Série d'applications Kriptofolio — Partie 5

De nos jours, presque toutes les applications Android se connectent à Internet pour obtenir/envoyer des données. Vous devriez définitivement apprendre à gérer les services web RESTful, car leur implémentation correcte est la connaissance centrale lors de la création d'applications modernes.

Cette partie va être compliquée. Nous allons combiner plusieurs bibliothèques à la fois pour obtenir un résultat fonctionnel. Je ne vais pas parler de la manière native Android de gérer les requêtes Internet, car dans le monde réel, personne ne l'utilise. Chaque bonne application n'essaie pas de réinventer la roue mais utilise plutôt les bibliothèques tierces les plus populaires pour résoudre les problèmes courants. Il serait trop compliqué de recréer la fonctionnalité que ces bibliothèques bien conçues ont à offrir.

### Contenu de la série

* [Introduction : Une feuille de route pour construire une application Android moderne en 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Partie 1 : Une introduction aux principes SOLID](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* [Partie 2 : Comment commencer à construire votre application Android : création de maquettes, UI et mises en page XML](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* [Partie 3 : Tout sur cette architecture : exploration de différents modèles d'architecture et comment les utiliser dans votre application](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* [Partie 4 : Comment implémenter l'injection de dépendances dans votre application avec Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* Partie 5 : Gérer les services web RESTful en utilisant Retrofit, OkHttp, Gson, Glide et les Coroutines (vous êtes ici)

### Qu'est-ce que Retrofit, OkHttp et Gson ?

Retrofit est un client REST pour Java et Android. Cette bibliothèque, à mon avis, est la plus importante à apprendre, car elle fera le travail principal. Elle facilite relativement la récupération et le téléchargement de JSON (ou d'autres données structurées) via un service web basé sur REST.

Dans Retrofit, vous configurez quel convertisseur est utilisé pour la sérialisation des données. Typiquement, pour sérialiser et désérialiser des objets en JSON, vous utilisez une bibliothèque Java open-source — Gson. De plus, si nécessaire, vous pouvez ajouter des convertisseurs personnalisés à Retrofit pour traiter XML ou d'autres protocoles.

Pour effectuer des requêtes HTTP, Retrofit utilise la bibliothèque OkHttp. OkHttp est un client HTTP/SPDY pur responsable de toute opération réseau de bas niveau, de la mise en cache, de la manipulation des requêtes et des réponses. En revanche, Retrofit est une abstraction REST de haut niveau construite sur OkHttp. Retrofit est fortement couplé avec OkHttp et en fait un usage intensif.

Maintenant que vous savez que tout est étroitement lié, nous allons utiliser ces 3 bibliothèques à la fois. Notre premier objectif est d'obtenir la liste de toutes les cryptomonnaies en utilisant Retrofit depuis Internet. Nous utiliserons une classe d'intercepteur OkHttp spéciale pour l'authentification de l'API CoinMarketCap lors de l'appel au serveur. Nous obtiendrons un résultat de données JSON et le convertirons ensuite en utilisant la bibliothèque Gson.

### Configuration rapide de Retrofit 2 pour l'essayer d'abord

Lorsque j'apprends quelque chose de nouveau, j'aime le mettre en pratique dès que possible. Nous allons appliquer une approche similaire avec Retrofit 2 pour que vous le compreniez mieux plus rapidement. Ne vous inquiétez pas pour l'instant de la qualité du code ou de tout principe de programmation ou d'optimisations — nous allons simplement écrire du code pour faire fonctionner Retrofit 2 dans notre projet et discuter de ce qu'il fait.

Suivez ces étapes pour configurer Retrofit 2 sur le projet d'application My Crypto Coins :

#### **Tout d'abord, donnez la permission INTERNET à l'application**

Nous allons exécuter des requêtes HTTP sur un serveur accessible via Internet. Donnez cette permission en ajoutant ces lignes à votre fichier Manifest :

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.baruckis.mycryptocoins">

    <uses-permission android:name="android.permission.INTERNET" />
    ...
</manifest>
```

#### **Ensuite, vous devez ajouter les dépendances de bibliothèque**

Trouvez la dernière [version de Retrofit](https://square.github.io/retrofit/). Vous devez également savoir que Retrofit ne dispose pas d'un convertisseur JSON intégré. Puisque nous allons obtenir des réponses au format JSON, nous devons inclure le convertisseur manuellement dans les dépendances également. Nous allons utiliser la dernière version du convertisseur JSON de Google [Gson](https://github.com/google/gson). Ajoutons ces lignes à votre fichier gradle :

```gradle
// 3rd party
// HTTP client - Retrofit avec OkHttp
implementation "com.squareup.retrofit2:retrofit:$versions.retrofit"
// Convertisseur JSON Gson pour le mappage d'objets JSON vers Java
implementation "com.squareup.retrofit2:converter-gson:$versions.retrofit"
```

Comme vous l'avez remarqué dans mon commentaire, la dépendance OkHttp est déjà incluse avec la dépendance Retrofit 2. Versions est simplement un fichier gradle séparé pour plus de commodité :

```gradle
def versions = [:]

versions.retrofit = "2.4.0"

ext.versions = versions
```

#### **Ensuite, configurez l'interface Retrofit**

C'est une interface qui déclare nos requêtes et leurs types. Ici, nous définissons l'API côté client.

```kotlin
/**
 * Points d'accès à l'API REST.
 */
interface ApiService {

    // L'annotation @GET indique à retrofit que cette requête est de type get.
    // La valeur de la chaîne indique à retrofit que le chemin de cette requête est
    // baseUrl + v1/cryptocurrency/listings/latest + paramètre de requête.
    @GET("v1/cryptocurrency/listings/latest")
    // L'annotation @Query est utilisée pour définir le paramètre de requête pour la requête. Enfin, l'URL de la requête ressemblera à cela https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=EUR.
    fun getAllCryptocurrencies(@Query("convert") currency: String): Call<CryptocurrenciesLatest>
    // Le type de retour pour cette fonction est Call avec son type CryptocurrenciesLatest.
}
```

#### **Et configurez la classe de données**

Les classes de données sont des POJO (Plain Old Java Objects) qui représentent les réponses des appels API que nous allons effectuer.

```kotlin
/**
 * Classe de données pour gérer la réponse du serveur.
 */
data class CryptocurrenciesLatest(
        val status: Status,
        val data: List<Data>
) {

    data class Data(
            val id: Int,
            val name: String,
            val symbol: String,
            val slug: String,
            // L'annotation sur une propriété de modèle vous permet de passer le nom sérialisé et désérialisé
            // sous forme de chaîne. Cela est utile si vous ne voulez pas que votre classe de modèle et le JSON
            // aient une nomenclature identique.
            @SerializedName("circulating_supply")
            val circulatingSupply: Double,
            @SerializedName("total_supply")
            val totalSupply: Double,
            @SerializedName("max_supply")
            val maxSupply: Double,
            @SerializedName("date_added")
            val dateAdded: String,
            @SerializedName("num_market_pairs")
            val numMarketPairs: Int,
            @SerializedName("cmc_rank")
            val cmcRank: Int,
            @SerializedName("last_updated")
            val lastUpdated: String,
            val quote: Quote
    ) {

        data class Quote(
                // Pour une option supplémentaire lors de la désérialisation, vous pouvez spécifier une valeur ou des valeurs alternatives.
                // Gson vérifie le JSON pour tous les noms que nous spécifions et essaie d'en trouver un à
                // mapper à la propriété annotée.
                @SerializedName(value = "USD", alternate = ["AUD", "BRL", "CAD", "CHF", "CLP",
                    "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY",
                    "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD",
                    "THB", "TRY", "TWD", "ZAR"])
                val currency: Currency
        ) {

            data class Currency(
                    val price: Double,
                    @SerializedName("volume_24h")
                    val volume24h: Double,
                    @SerializedName("percent_change_1h")
                    val percentChange1h: Double,
                    @SerializedName("percent_change_24h")
                    val percentChange24h: Double,
                    @SerializedName("percent_change_7d")
                    val percentChange7d: Double,
                    @SerializedName("market_cap")
                    val marketCap: Double,
                    @SerializedName("last_updated")
                    val lastUpdated: String
            )
        }
    }

    data class Status(
            val timestamp: String,
            @SerializedName("error_code")
            val errorCode: Int,
            @SerializedName("error_message")
            val errorMessage: String,
            val elapsed: Int,
            @SerializedName("credit_count")
            val creditCount: Int
    )
}
```

#### **Créez une classe d'intercepteur spéciale pour l'authentification lors de l'appel au serveur**

C'est le cas particulier pour toute API qui nécessite une authentification pour obtenir une réponse réussie. Les intercepteurs sont un moyen puissant de personnaliser vos requêtes. Nous allons intercepter la requête réelle et ajouter des en-têtes de requête individuels, qui valideront l'appel avec une clé API fournie par le [Portail des développeurs de l'API professionnelle CoinMarketCap](https://pro.coinmarketcap.com). Pour obtenir la vôtre, vous devez vous y inscrire.

```kotlin
/**
 * Intercepteur utilisé pour intercepter la requête réelle et
 * fournir votre clé API dans les appels d'API REST via un en-tête personnalisé.
 */
class AuthenticationInterceptor : Interceptor {

    override fun intercept(chain: Interceptor.Chain): Response {

        val newRequest = chain.request().newBuilder()
                // TODO: Utilisez votre clé API fournie par le Portail des développeurs de l'API professionnelle CoinMarketCap.
                .addHeader("X-CMC_PRO_API_KEY", "CMC_PRO_API_KEY")
                .build()

        return chain.proceed(newRequest)
    }
}
```

#### **Enfin, ajoutez ce code à notre activité pour voir Retrofit fonctionner**

Je voulais vous faire mettre la main à la pâte le plus rapidement possible, donc j'ai tout mis au même endroit. Ce n'est pas la bonne façon de faire, mais c'est la plus rapide pour voir un résultat visuel rapidement.

```kotlin
class AddSearchActivity : AppCompatActivity(), Injectable {

    private lateinit var listView: ListView
    private lateinit var listAdapter: AddSearchListAdapter

    ...

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        ...

        // Plus tard, nous configurerons Retrofit correctement, mais pour l'instant, nous faisons tout en un seul endroit pour un démarrage rapide.
        setupRetrofitTemporarily()
    }

    ...

    private fun setupRetrofitTemporarily() {

        // Nous devons préparer un client OkHttp personnalisé car nous devons utiliser notre intercepteur d'appel personnalisé.
        // pour pouvoir authentifier nos requêtes.
        val builder = OkHttpClient.Builder()
        // Nous ajoutons l'intercepteur à OkHttpClient.
        // Il ajoutera des en-têtes d'authentification à chaque appel que nous faisons.
        builder.interceptors().add(AuthenticationInterceptor())
        val client = builder.build()


        val api = Retrofit.Builder() // Créez le constructeur retrofit.
                .baseUrl("https://sandbox-api.coinmarketcap.com/") // L'URL de base pour l'API doit se terminer par un slash.
                .addConverterFactory(GsonConverterFactory.create()) // Utilisez le convertisseur GSON pour le mappage d'objets JSON vers POJO.
                .client(client) // Ici, nous définissons le client OkHttp personnalisé que nous venons de créer.
                .build().create(ApiService::class.java) // Nous créons une API en utilisant l'interface que nous avons définie.


        val adapterData: MutableList<Cryptocurrency> = ArrayList<Cryptocurrency>()

        val currentFiatCurrencyCode = "EUR"

        // Faisons une requête réseau asynchrone pour obtenir toutes les dernières cryptomonnaies du serveur.
        // Pour le paramètre de requête, nous passons "EUR" car nous voulons obtenir les prix en euros.
        val call = api.getAllCryptocurrencies("EUR")
        val result = call.enqueue(object : Callback<CryptocurrenciesLatest> {

            // Vous obtiendrez toujours une réponse même si quelque chose ne va pas du côté du serveur.
            override fun onFailure(call: Call<CryptocurrenciesLatest>, t: Throwable) {

                Snackbar.make(findViewById(android.R.id.content),
                        // Throwable nous permettra de trouver l'erreur si l'appel a échoué.
                        "L'appel a échoué ! " + t.localizedMessage,
                        Snackbar.LENGTH_INDEFINITE).show()
            }

            override fun onResponse(call: Call<CryptocurrenciesLatest>, response: Response<CryptocurrenciesLatest>) {

                // Vérifiez si la réponse est réussie, ce qui signifie que la requête a été reçue, comprise, acceptée et a retourné un code dans la plage [200..300).
                if (response.isSuccessful) {

                    // Si tout est OK, informez l'utilisateur.
                    Toast.makeText(this@AddSearchActivity, "Appel OK.", Toast.LENGTH_LONG).show();

                    // Ensuite, mappez rapidement les données de réponse du serveur vers l'adaptateur ListView.
                    val cryptocurrenciesLatest: CryptocurrenciesLatest? = response.body()
                    cryptocurrenciesLatest!!.data.forEach {
                        val cryptocurrency = Cryptocurrency(it.name, it.cmcRank.toShort(),
                                0.0, it.symbol, currentFiatCurrencyCode, it.quote.currency.price,
                                0.0, it.quote.currency.percentChange1h,
                                it.quote.currency.percentChange7d, it.quote.currency.percentChange24h,
                                0.0)
                        adapterData.add(cryptocurrency)
                    }

                    listView.visibility = View.VISIBLE
                    listAdapter.setData(adapterData)

                }
                // Sinon, si la réponse n'est pas réussie, elle sera définie par un code d'erreur HTTP spécial, que nous pouvons afficher à l'utilisateur.
                else Snackbar.make(findViewById(android.R.id.content),
                        "Erreur d'appel avec le code d'état HTTP " + response.code() + "!",
                        Snackbar.LENGTH_INDEFINITE).show()

            }

        })

    }

   ...
}
```

Vous pouvez explorer le code [ici](https://github.com/baruckis/Kriptofolio/tree/4d7946705b8c4dc2db3775bcc000d2918f8f1b73). N'oubliez pas que ceci n'est qu'une version simplifiée initiale pour vous donner une meilleure idée.

### Configuration finale correcte pour Retrofit 2 avec OkHttp 3 et Gson

D'accord, après une expérience rapide, il est temps de faire passer cette implémentation Retrofit au niveau supérieur. Nous avons déjà obtenu les données avec succès mais pas correctement. Il nous manque les états comme le chargement, l'erreur et le succès. Notre code est mélangé sans séparation des préoccupations. C'est une erreur courante d'écrire tout votre code dans une activité ou un fragment. Notre classe d'activité est basée sur l'UI et ne doit contenir que la logique qui gère les interactions UI et du système d'exploitation.

En fait, après cette configuration rapide, j'ai beaucoup travaillé et apporté de nombreuses modifications. Il n'y a pas lieu de mettre tout le code qui a été modifié dans l'article. Il est préférable que vous parcouriez le dépôt de code final de la partie 5 [ici](https://github.com/baruckis/Kriptofolio/tree/Part-5). J'ai tout commenté très bien et mon code devrait être clair pour vous. Mais je vais parler des choses les plus importantes que j'ai faites et pourquoi je les ai faites.

La première étape pour améliorer était de commencer à utiliser l'injection de dépendances. Rappelez-vous de la [partie précédente](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4), nous avons déjà Dagger 2 implémenté correctement à l'intérieur du projet. Donc je l'ai utilisé pour la configuration de Retrofit.

```kotlin
/**
 * AppModule fournira des dépendances pour toute l'application pour une partie de l'application.
 * Il doit initialiser les objets utilisés dans notre application, tels que la base de données Room, Retrofit, Shared Preference, etc.
 */
@Module(includes = [ViewModelsModule::class])
class AppModule() {
    ...

    @Provides
    @Singleton
    fun provideHttpClient(): OkHttpClient {
        // Nous devons préparer un client OkHttp personnalisé car nous devons utiliser notre intercepteur d'appel personnalisé.
        // pour pouvoir authentifier nos requêtes.
        val builder = OkHttpClient.Builder()
        // Nous ajoutons l'intercepteur à OkHttpClient.
        // Il ajoutera des en-têtes d'authentification à chaque appel que nous faisons.
        builder.interceptors().add(AuthenticationInterceptor())

        // Configurez ce client pour ne pas réessayer lorsqu'un problème de connectivité est rencontré.
        builder.retryOnConnectionFailure(false)

        // Journalisez les requêtes et les réponses.
        // Ajoutez la journalisation comme dernier intercepteur, car cela journalisera également les informations que
        // vous avez ajoutées ou manipulées avec les intercepteurs précédents dans votre requête.
        builder.interceptors().add(HttpLoggingInterceptor().apply {
            // Pour l'environnement de production afin d'améliorer les performances des applications, nous allons sauter toute
            // opération de journalisation. Nous allons montrer les journaux uniquement pour les builds de débogage.
            level = if (BuildConfig.DEBUG) HttpLoggingInterceptor.Level.BODY else HttpLoggingInterceptor.Level.NONE
        })
        return builder.build()
    }

    @Provides
    @Singleton
    fun provideApiService(httpClient: OkHttpClient): ApiService {
        return Retrofit.Builder() // Créez le constructeur retrofit.
                .baseUrl(API_SERVICE_BASE_URL) // L'URL de base pour l'API doit se terminer par un slash.
                .addConverterFactory(GsonConverterFactory.create()) // Utilisez le convertisseur GSON pour le mappage d'objets JSON vers POJO.
                .addCallAdapterFactory(LiveDataCallAdapterFactory())
                .client(httpClient) // Ici, nous définissons le client OkHttp personnalisé que nous venons de créer.
                .build().create(ApiService::class.java) // Nous créons une API en utilisant l'interface que nous avons définie.
    }

    ...
}
```

Maintenant, comme vous le voyez, Retrofit est séparé de la classe d'activité comme il se doit. Il ne sera initialisé qu'une seule fois et utilisé dans toute l'application.

Comme vous l'avez peut-être remarqué lors de la création de l'instance du constructeur Retrofit, nous avons ajouté un adaptateur d'appels Retrofit spécial en utilisant `addCallAdapterFactory`. Par défaut, Retrofit retourne un `Call<T>`, mais pour notre projet, nous exigeons qu'il retourne un type `LiveData<T>`. Pour ce faire, nous devons ajouter `LiveDataCallAdapter` en utilisant `LiveDataCallAdapterFactory`.

```kotlin
/**
 * Un adaptateur Retrofit qui convertit le Call en un LiveData de ApiResponse.
 * @param <R>
</R> */
class LiveDataCallAdapter<R>(private val responseType: Type) :
        CallAdapter<R, LiveData<ApiResponse<R>>> {

    override fun responseType() = responseType

    override fun adapt(call: Call<R>): LiveData<ApiResponse<R>> {
        return object : LiveData<ApiResponse<R>>() {
            private var started = AtomicBoolean(false)
            override fun onActive() {
                super.onActive()
                if (started.compareAndSet(false, true)) {
                    call.enqueue(object : Callback<R> {
                        override fun onResponse(call: Call<R>, response: Response<R>) {
                            postValue(ApiResponse.create(response))
                        }

                        override fun onFailure(call: Call<R>, throwable: Throwable) {
                            postValue(ApiResponse.create(throwable))
                        }
                    })
                }
            }
        }
    }
}
```

```kotlin
class LiveDataCallAdapterFactory : CallAdapter.Factory() {
    override fun get(
            returnType: Type,
            annotations: Array<Annotation>,
            retrofit: Retrofit
    ): CallAdapter<*, *>? {
        if (CallAdapter.Factory.getRawType(returnType) != LiveData::class.java) {
            return null
        }
        val observableType = CallAdapter.Factory.getParameterUpperBound(0, returnType as ParameterizedType)
        val rawObservableType = CallAdapter.Factory.getRawType(observableType)
        if (rawObservableType != ApiResponse::class.java) {
            throw IllegalArgumentException("type must be a resource")
        }
        if (observableType !is ParameterizedType) {
            throw IllegalArgumentException("resource must be parameterized")
        }
        val bodyType = CallAdapter.Factory.getParameterUpperBound(0, observableType)
        return LiveDataCallAdapter<Any>(bodyType)
    }
}
```

Maintenant, nous obtiendrons `LiveData<T>` au lieu de `Call<T>` comme type de retour des méthodes de service Retrofit définies dans l'interface `ApiService`.

Une autre étape importante à faire est de commencer à utiliser le modèle Repository. J'en ai parlé dans la [Partie 3](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3). Consultez notre schéma d'architecture MVVM de cet article pour vous rappeler où il se place.

![Image](https://cdn-media-1.freecodecamp.org/images/qlI48NPPMqMbOeV47Cpkxop4nhW8RhgfTtjO)

Comme vous le voyez sur l'image, Repository est une couche séparée pour les données. C'est notre source unique de contact pour obtenir ou envoyer des données. Lorsque nous utilisons Repository, nous suivons le principe de séparation des préoccupations. Nous pouvons avoir différentes sources de données (comme dans notre cas, des données persistantes d'une base de données SQLite et des données de services web), mais Repository sera toujours la source unique de vérité pour toutes les données de l'application.

Au lieu de communiquer directement avec notre implémentation Retrofit, nous allons utiliser Repository pour cela. Pour chaque type d'entité, nous allons avoir un Repository séparé.

```kotlin
/**
 * La classe pour gérer plusieurs sources de données.
 */
@Singleton
class CryptocurrencyRepository @Inject constructor(
        private val context: Context,
        private val appExecutors: AppExecutors,
        private val myCryptocurrencyDao: MyCryptocurrencyDao,
        private val cryptocurrencyDao: CryptocurrencyDao,
        private val api: ApiService,
        private val sharedPreferences: SharedPreferences
) {

    // Juste une variable d'aide simple pour stocker le code de devise fiduciaire sélectionné pendant le cycle de vie de l'application.
    // Il est nécessaire pour le spinner de devise de l'écran principal. Nous le définissons pour qu'il soit le même que dans les préférences partagées.
    var selectedFiatCurrencyCode: String = getCurrentFiatCurrencyCode()


    ...
  

    // L'encapsulation de Resource de LiveData est utile pour mettre à jour l'UI en fonction de l'état.
    fun getAllCryptocurrencyLiveDataResourceList(fiatCurrencyCode: String, shouldFetch: Boolean = false, callDelay: Long = 0): LiveData<Resource<List<Cryptocurrency>>> {
        return object : NetworkBoundResource<List<Cryptocurrency>, CoinMarketCap<List<CryptocurrencyLatest>>>(appExecutors) {

            // Ici, nous sauvegardons les données récupérées du service web.
            override fun saveCallResult(item: CoinMarketCap<List<CryptocurrencyLatest>>) {

                val list = getCryptocurrencyListFromResponse(fiatCurrencyCode, item.data, item.status?.timestamp)

                cryptocurrencyDao.reloadCryptocurrencyList(list)
                myCryptocurrencyDao.reloadMyCryptocurrencyList(list)
            }

            // Retourne un booléen indiquant si les données doivent être récupérées depuis le web ou non, true signifie récupérer les données depuis le web.
            override fun shouldFetch(data: List<Cryptocurrency>?): Boolean {
                return data == null || shouldFetch
            }

            override fun fetchDelayMillis(): Long {
                return callDelay
            }

            // Contient la logique pour obtenir les données de la base de données Room.
            override fun loadFromDb(): LiveData<List<Cryptocurrency>> {

                return Transformations.switchMap(cryptocurrencyDao.getAllCryptocurrencyLiveDataList()) { data ->
                    if (data.isEmpty()) {
                        AbsentLiveData.create()
                    } else {
                        cryptocurrencyDao.getAllCryptocurrencyLiveDataList()
                    }
                }
            }

            // Contient la logique pour obtenir les données du service web en utilisant Retrofit.
            override fun createCall(): LiveData<ApiResponse<CoinMarketCap<List<CryptocurrencyLatest>>>> = api.getAllCryptocurrencies(fiatCurrencyCode)

        }.asLiveData()
    }


    ...


    fun getCurrentFiatCurrencyCode(): String {
        return sharedPreferences.getString(context.resources.getString(R.string.pref_fiat_currency_key), context.resources.getString(R.string.pref_default_fiat_currency_value))
                ?: context.resources.getString(R.string.pref_default_fiat_currency_value)
    }


    ...


    private fun getCryptocurrencyListFromResponse(fiatCurrencyCode: String, responseList: List<CryptocurrencyLatest>?, timestamp: Date?): ArrayList<Cryptocurrency> {

        val cryptocurrencyList: MutableList<Cryptocurrency> = ArrayList()

        responseList?.forEach {
            val cryptocurrency = Cryptocurrency(it.id, it.name, it.cmcRank.toShort(),
                    it.symbol, fiatCurrencyCode, it.quote.currency.price,
                    it.quote.currency.percentChange1h,
                    it.quote.currency.percentChange7d, it.quote.currency.percentChange24h, timestamp)
            cryptocurrencyList.add(cryptocurrency)
        }

        return cryptocurrencyList as ArrayList<Cryptocurrency>
    }

}
```

Comme vous le remarquez dans le code de la classe `CryptocurrencyRepository`, j'utilise la classe abstraite `NetworkBoundResource`. Qu'est-ce que c'est et pourquoi en avons-nous besoin ?

`NetworkBoundResource` est une petite mais très importante classe d'assistance qui nous permettra de maintenir une synchronisation entre la base de données locale et le service web. Notre objectif est de construire une application moderne qui fonctionnera en douceur même lorsque notre appareil est hors ligne. De plus, avec l'aide de cette classe, nous pourrons présenter différents états du réseau comme les erreurs ou le chargement pour l'utilisateur de manière visuelle.

`NetworkBoundResource` commence par observer la base de données pour la ressource. Lorsque l'entrée est chargée depuis la base de données pour la première fois, elle vérifie si le résultat est suffisamment bon pour être diffusé ou s'il doit être récupéré à nouveau depuis le réseau. Notez que ces deux situations peuvent se produire en même temps, étant donné que vous souhaitez probablement afficher les données mises en cache tout en les mettant à jour depuis le réseau.

Si l'appel réseau se termine avec succès, il sauvegarde la réponse dans la base de données et réinitialise le flux. Si la requête réseau échoue, `NetworkBoundResource` diffuse un échec directement.

```kotlin
/**
 * Une classe générique qui peut fournir une ressource soutenue à la fois par la base de données sqlite et le réseau.
 *
 *
 * Vous pouvez en lire plus à ce sujet dans le [Guide
 * d'architecture](https://developer.android.com/arch).
 * @param <ResultType> - Type pour les données de la ressource.
 * @param <RequestType> - Type pour la réponse de l'API.
</RequestType></ResultType> */

// Il définit deux paramètres de type, ResultType et RequestType,
// car le type de données retourné par l'API peut ne pas correspondre au type de données utilisé localement.
abstract class NetworkBoundResource<ResultType, RequestType>
@MainThread constructor(private val appExecutors: AppExecutors) {

    // Le résultat final LiveData.
    private val result = MediatorLiveData<Resource<ResultType>>()

    init {
        // Envoyer l'état de chargement à l'UI.
        result.value = Resource.loading(null)
        @Suppress("LeakingThis")
        val dbSource = loadFromDb()
        result.addSource(dbSource) { data ->
            result.removeSource(dbSource)
            if (shouldFetch(data)) {
                fetchFromNetwork(dbSource)
            } else {
                result.addSource(dbSource) { newData ->
                    setValue(Resource.successDb(newData))
                }
            }
        }
    }

    @MainThread
    private fun setValue(newValue: Resource<ResultType>) {
        if (result.value != newValue) {
            result.value = newValue
        }
    }

    // Récupérer les données du réseau et les persister dans la base de données puis les renvoyer à l'UI.
    private fun fetchFromNetwork(dbSource: LiveData<ResultType>) {
        val apiResponse = createCall()
        // Nous réattachons dbSource comme une nouvelle source, elle diffusera rapidement sa dernière valeur.
        result.addSource(dbSource) { newData ->
            setValue(Resource.loading(newData))
        }

        // Créer une fonction interne car nous voulons la retarder.
        fun fetch() {
            result.addSource(apiResponse) { response ->
                result.removeSource(apiResponse)
                result.removeSource(dbSource)
                when (response) {
                    is ApiSuccessResponse -> {
                        appExecutors.diskIO().execute {
                            saveCallResult(processResponse(response))
                            appExecutors.mainThread().execute {
                                // Nous demandons spécifiquement une nouvelle donnée en direct,
                                // sinon nous obtiendrons immédiatement la dernière valeur mise en cache,
                                // qui peut ne pas être mise à jour avec les derniers résultats reçus du réseau.
                                result.addSource(loadFromDb()) { newData ->
                                    setValue(Resource.successNetwork(newData))
                                }
                            }
                        }
                    }
                    is ApiEmptyResponse -> {
                        appExecutors.mainThread().execute {
                            // recharger depuis le disque ce que nous avions
                            result.addSource(loadFromDb()) { newData ->
                                setValue(Resource.successDb(newData))
                            }
                        }
                    }
                    is ApiErrorResponse -> {
                        onFetchFailed()
                        result.addSource(dbSource) { newData ->
                            setValue(Resource.error(response.errorMessage, newData))
                        }
                    }
                }
            }
        }

        // Ajouter un délai avant l'appel si nécessaire.
        val delay = fetchDelayMillis()
        if (delay > 0) {
            Handler().postDelayed({ fetch() }, delay)
        } else fetch()

    }

    // Appelé lorsque la récupération échoue. La classe enfant peut vouloir réinitialiser les composants
    // comme le limiteur de débit.
    protected open fun onFetchFailed() {}

    // Retourne un objet LiveData qui représente la ressource qui est implémentée
    // dans la classe de base.
    fun asLiveData() = result as LiveData<Resource<ResultType>>

    @WorkerThread
    protected open fun processResponse(response: ApiSuccessResponse<RequestType>) = response.body

    // Appelé pour sauvegarder le résultat de la réponse de l'API dans la base de données.
    @WorkerThread
    protected abstract fun saveCallResult(item: RequestType)

    // Appelé avec les données dans la base de données pour décider si les données doivent être récupérées
    // potentiellement mises à jour depuis le réseau.
    @MainThread
    protected abstract fun shouldFetch(data: ResultType?): Boolean

    // Faire un appel au serveur après un certain délai pour une meilleure expérience utilisateur.
    protected open fun fetchDelayMillis(): Long = 0

    // Appelé pour obtenir les données mises en cache de la base de données.
    @MainThread
    protected abstract fun loadFromDb(): LiveData<ResultType>

    // Appelé pour créer l'appel API.
    @MainThread
    protected abstract fun createCall(): LiveData<ApiResponse<RequestType>>
}
```

Sous le capot, la classe `NetworkBoundResource` est faite en utilisant MediatorLiveData et sa capacité à observer plusieurs sources LiveData à la fois. Ici, nous avons deux sources LiveData : la base de données et la réponse de l'appel réseau. Ces deux LiveData sont enveloppées dans un seul MediatorLiveData qui est exposé par `NetworkBoundResource`.

![Image](https://cdn-media-1.freecodecamp.org/images/qbNZeVc-RHe54xa9LSZMOfzmmrBA9rXzhGYo)
_NetworkBoundResource_

Prenons un regard plus attentif sur la façon dont `NetworkBoundResource` fonctionnera dans notre application. Imaginez que l'utilisateur lancera l'application et cliquera sur un bouton d'action flottant dans le coin inférieur droit. L'application lancera l'écran d'ajout de cryptomonnaies. Maintenant, nous pouvons analyser l'utilisation de `NetworkBoundResource` à l'intérieur.

Si l'application est fraîchement installée et qu'il s'agit de son premier lancement, alors il n'y aura aucune donnée stockée dans la base de données locale. Comme il n'y a pas de données à afficher, une UI de barre de progression de chargement sera affichée. Pendant ce temps, l'application va faire une requête d'appel au serveur via un service web pour obtenir la liste de toutes les cryptomonnaies.

Si la réponse n'est pas réussie, alors l'UI de message d'erreur sera affichée avec la possibilité de réessayer un appel en appuyant sur un bouton. Lorsqu'un appel de requête est enfin réussi, alors les données de réponse seront sauvegardées dans une base de données SQLite locale.

Si nous revenons au même écran la prochaine fois, l'application chargera les données depuis la base de données au lieu de faire un appel à Internet à nouveau. Mais l'utilisateur peut demander une nouvelle mise à jour des données en implémentant la fonctionnalité de pull-to-refresh. Les anciennes informations de données seront affichées pendant que l'appel réseau est en cours. Tout cela est fait avec l'aide de `NetworkBoundResource`.

Une autre classe utilisée dans notre Repository et `LiveDataCallAdapter` où toute la "magie" se produit est `ApiResponse`. En fait, `ApiResponse` est juste un simple wrapper commun autour de la classe `Retrofit2.Response` qui convertit chaque réponse en une instance de LiveData.

```kotlin
/**
 * Classe commune utilisée par les réponses de l'API. ApiResponse est un simple wrapper autour de Retrofit2.Call
 * classe qui convertit les réponses en instances de LiveData.
 * @param <CoinMarketCapType> le type de l'objet de réponse
</T> */
@Suppress("unused") // T est utilisé dans les classes étendues
sealed class ApiResponse<CoinMarketCapType> {
    companion object {
        fun <CoinMarketCapType> create(error: Throwable): ApiErrorResponse<CoinMarketCapType> {
            return ApiErrorResponse(error.message ?: "Erreur inconnue.")
        }

        fun <CoinMarketCapType> create(response: Response<CoinMarketCapType>): ApiResponse<CoinMarketCapType> {
            return if (response.isSuccessful) {
                val body = response.body()
                if (body == null || response.code() == 204) {
                    ApiEmptyResponse()
                } else {
                    ApiSuccessResponse(body = body)
                }
            } else {

                // Convertir la réponse d'erreur en objet JSON.
                val gson = Gson()
                val type = object : TypeToken<CoinMarketCap<CoinMarketCapType>>() {}.type
                val errorResponse: CoinMarketCap<CoinMarketCapType> = gson.fromJson(response.errorBody()!!.charStream(), type)

                val msg = errorResponse.status?.errorMessage ?: errorResponse.message
                val errorMsg = if (msg.isNullOrEmpty()) {
                    response.message()
                } else {
                    msg
                }
                ApiErrorResponse(errorMsg ?: "Erreur inconnue.")
            }
        }
    }
}

/**
 * Classe séparée pour les réponses HTTP 204 afin que nous puissions rendre le corps de ApiSuccessResponse non nul.
 */
class ApiEmptyResponse<CoinMarketCapType> : ApiResponse<CoinMarketCapType>()

data class ApiSuccessResponse<CoinMarketCapType>(val body: CoinMarketCapType) : ApiResponse<CoinMarketCapType>()

data class ApiErrorResponse<CoinMarketCapType>(val errorMessage: String) : ApiResponse<CoinMarketCapType>()
```

À l'intérieur de cette classe wrapper, si notre réponse contient une erreur, nous utilisons la bibliothèque Gson pour convertir l'erreur en un objet JSON. Cependant, si la réponse était réussie, alors le convertisseur Gson pour le mappage d'objets JSON vers POJO est utilisé. Nous l'avons déjà ajouté lors de la création de l'instance du constructeur retrofit avec `GsonConverterFactory` à l'intérieur de la fonction Dagger `AppModule` `provideApiService`.

### Glide pour le chargement des images

[Qu'est-ce que Glide](https://github.com/huyn/glide) ? D'après la documentation :

> Glide est un framework de gestion de médias et de chargement d'images rapide et efficace pour Android qui enveloppe le décodage de médias, la mise en cache en mémoire et sur disque, et le regroupement de ressources dans une interface simple et facile à utiliser.

> L'objectif principal de Glide est de rendre le défilement de tout type de liste d'images aussi fluide et rapide que possible, mais il est également efficace pour presque tous les cas où vous devez récupérer, redimensionner et afficher une image distante.

Cela ressemble à une bibliothèque compliquée qui offre de nombreuses fonctionnalités utiles que vous ne voudriez pas développer vous-même. Dans l'application My Crypto Coins, nous avons plusieurs écrans de liste où nous devons afficher plusieurs logos de cryptomonnaies — des images prises sur Internet toutes à la fois — et garantir une expérience de défilement fluide pour l'utilisateur. Cette bibliothèque répond donc parfaitement à nos besoins. De plus, cette bibliothèque est très populaire parmi les développeurs Android.

Étapes pour configurer Glide sur le projet d'application My Crypto Coins :

#### **Déclarer les dépendances**

Obtenez la dernière [version de Glide](https://bumptech.github.io/glide). Encore une fois, les versions sont un fichier séparé `versions.gradle` pour le projet.

```gradle
// Glide
implementation "com.github.bumptech.glide:glide:$versions.glide"
kapt "com.github.bumptech.glide:compiler:$versions.glide"
// Intégration OkHttp3 de Glide.
implementation "com.github.bumptech.glide:okhttp3-integration:$versions.glide"+"@aar"
```

Parce que nous voulons utiliser la bibliothèque de mise en réseau OkHttp dans notre projet pour toutes les opérations réseau, nous devons inclure l'intégration spécifique de Glide pour celle-ci au lieu de celle par défaut. De plus, puisque Glide va effectuer une requête réseau pour charger des images via Internet, nous devons inclure la permission `INTERNET` dans notre fichier `AndroidManifest.xml` — mais nous l'avons déjà fait avec la configuration de Retrofit.

#### **Créer AppGlideModule**

Glide v4, que nous allons utiliser, offre une API générée pour les applications. Il utilisera un processeur d'annotations pour générer une API qui permet aux applications d'étendre l'API de Glide et d'inclure des composants fournis par les bibliothèques d'intégration. Pour qu'une application accède à l'API générée de Glide, nous devons inclure une implémentation `AppGlideModule` annotée de manière appropriée. Il ne peut y avoir qu'une seule implémentation de l'API générée et un seul `AppGlideModule` par application.

Créons une classe étendant `AppGlideModule` quelque part dans votre projet d'application :

```kotlin
/**
 * Glide v4 utilise un processeur d'annotations pour générer une API qui permet aux applications d'accéder à toutes
 * les options dans RequestBuilder, RequestOptions et toute bibliothèque d'intégration incluse dans une seule
 * API fluide.
 *
 * L'API générée sert deux objectifs :
 * Les bibliothèques d'intégration peuvent étendre l'API de Glide avec des options personnalisées.
 * Les applications peuvent étendre l'API de Glide en ajoutant des méthodes qui regroupent des options couramment utilisées.
 *
 * Bien que ces deux tâches puissent être accomplies manuellement en écrivant des sous-classes personnalisées de
 * RequestOptions, le faire est difficile et produit une API moins fluide.
 */
@GlideModule
class AppGlideModule : AppGlideModule()
```

Même si notre application ne modifie aucun paramètre supplémentaire ou n'implémente aucune méthode dans `AppGlideModule`, nous devons toujours avoir son implémentation pour utiliser Glide. Vous n'êtes pas obligé d'implémenter l'une des méthodes dans `AppGlideModule` pour que l'API soit générée. Vous pouvez laisser la classe vide tant qu'elle étend `AppGlideModule` et est annotée avec `@GlideModule`.

#### **Utiliser l'API générée par Glide**

Lorsque vous utilisez `AppGlideModule`, les applications peuvent utiliser l'API en commençant tous les chargements avec `GlideApp.with()`. Voici le code qui montre comment j'ai utilisé Glide pour charger et afficher les logos de cryptomonnaies dans l'écran d'ajout de cryptomonnaies, la liste de toutes les cryptomonnaies.

```kotlin
class AddSearchListAdapter(val context: Context, private val cryptocurrencyClickCallback: ((Cryptocurrency) -> Unit)?) : BaseAdapter() {

    ...

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        ...

        val itemBinding: ActivityAddSearchListItemBinding

        ...

        // Nous créons un Uri de l'image que nous devons charger. Le nom unique de chaque image est son id.
        val imageUri = Uri.parse(CRYPTOCURRENCY_IMAGE_URL).buildUpon()
                .appendPath(CRYPTOCURRENCY_IMAGE_SIZE_PX)
                .appendPath(cryptocurrency.id.toString() + CRYPTOCURRENCY_IMAGE_FILE)
                .build()

        // API générée par Glide à partir de AppGlideModule.
        GlideApp
                // Nous devons fournir un contexte pour faire un appel.
                .with(itemBinding.root)
                // Ici, vous spécifiez quelle image doit être chargée en fournissant un Uri.
                .load(imageUri)
                // La manière dont vous combinez et exécutez plusieurs transformations.
                // WhiteBackground est notre propre transformation personnalisée implémentée.
                // CircleCrop est une transformation par défaut que Glide fournit.
                .transform(MultiTransformation(WhiteBackground(), CircleCrop()))
                // L'ImageView cible où votre image est censée être affichée.
                .into(itemBinding.itemImageIcon.imageview_front)

        ...

        return itemBinding.root
    }

    ...

}
```

Comme vous le voyez, vous pouvez commencer à utiliser Glide avec seulement quelques lignes de code et le laisser faire tout le travail difficile pour vous. C'est assez simple.

### Coroutines Kotlin

Lors de la construction de cette application, nous allons rencontrer des situations où nous exécuterons des tâches chronophages telles que l'écriture de données dans une base de données ou la lecture depuis celle-ci, la récupération de données depuis le réseau et autres. Toutes ces tâches courantes prennent plus de temps à s'exécuter que ce que permet le thread principal du framework Android.

Le thread principal est un thread unique qui gère toutes les mises à jour de l'UI. Les développeurs sont tenus de ne pas le bloquer pour éviter que l'application ne gèle ou ne plante avec une boîte de dialogue "Application non répondante". Les coroutines Kotlin vont résoudre ce problème pour nous en introduisant la sécurité du thread principal. C'est la dernière pièce manquante que nous voulons ajouter pour l'application My Crypto Coins.

Les coroutines sont une fonctionnalité de Kotlin qui convertit les rappels asynchrones pour les tâches de longue durée, telles que l'accès à la base de données ou au réseau, en code séquentiel. Avec les coroutines, vous pouvez écrire du code asynchrone, qui était traditionnellement écrit en utilisant le modèle de rappel, en utilisant un style synchrone. La valeur de retour d'une fonction fournira le résultat de l'appel asynchrone. Le code écrit de manière séquentielle est généralement plus facile à lire et peut même utiliser des fonctionnalités du langage telles que les exceptions.

Nous allons donc utiliser des coroutines partout dans cette application où nous devons attendre qu'un résultat soit disponible à partir d'une tâche de longue durée, puis continuer l'exécution. Regardons une implémentation exacte pour notre ViewModel où nous allons réessayer d'obtenir les dernières données du serveur pour nos cryptomonnaies présentées sur l'écran principal.

Tout d'abord, ajoutez les coroutines au projet :

```gradle
// Bibliothèques de support pour les coroutines Kotlin.

// Dépendances pour les coroutines.
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:$versions.coroutines"

// Dépendance pour le contexte UI spécial qui peut être passé aux constructeurs de coroutines qui utilisent
// le dispatcher du thread principal pour dispatcher les événements sur le thread principal.
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:$versions.coroutines"
```

Ensuite, nous allons créer une classe abstraite qui deviendra la classe de base à utiliser pour tout ViewModel ayant besoin de fonctionnalités communes comme les coroutines dans notre cas :

```kotlin
abstract class BaseViewModel : ViewModel() {

    // En Kotlin, toutes les coroutines s'exécutent dans un CoroutineScope.
    // Un scope contrôle la durée de vie des coroutines via son travail.
    private val viewModelJob = Job()
    // Puisque uiScope a un dispatcher par défaut de Dispatchers.Main, cette coroutine sera lancée
    // dans le thread principal.
    val uiScope = CoroutineScope(Dispatchers.Main + viewModelJob)


    // onCleared est appelé lorsque le ViewModel n'est plus utilisé et sera détruit.
    // Cela se produit généralement lorsque l'utilisateur navigue loin de l'Activity ou du Fragment qui utilisait
    // le ViewModel.
    override fun onCleared() {
        super.onCleared()
        // Lorsque vous annulez le travail d'un scope, il annule toutes les coroutines démarrées dans ce scope.
        // Il est important d'annuler toutes les coroutines qui ne sont plus nécessaires pour éviter un travail inutile
        // et des fuites de mémoire.
        viewModelJob.cancel()
    }
}
```

Ici, nous créons un scope de coroutine spécifique, qui contrôlera la durée de vie des coroutines via son travail. Comme vous le voyez, le scope vous permet de spécifier un dispatcher par défaut qui contrôle quel thread exécute une coroutine. Lorsque le ViewModel n'est plus utilisé, nous annulons `viewModelJob` et avec cela, chaque coroutine démarrée par `uiScope` sera également annulée.

Enfin, implémentez la fonctionnalité de réessai :

```kotlin
/**
 * La classe ViewModel est conçue pour stocker et gérer les données liées à l'UI de manière consciente du cycle de vie.
 * La classe ViewModel permet aux données de survivre aux changements de configuration tels que les rotations d'écran.
 */

// ViewModel nécessitera un CryptocurrencyRepository donc nous ajoutons le code @Inject dans le constructeur de ViewModel.
class MainViewModel @Inject constructor(val context: Context, val cryptocurrencyRepository: CryptocurrencyRepository) : BaseViewModel() {

    ...

    val mediatorLiveDataMyCryptocurrencyResourceList = MediatorLiveData<Resource<List<MyCryptocurrency>>>()
    private var liveDataMyCryptocurrencyResourceList: LiveData<Resource<List<MyCryptocurrency>>>
    private val liveDataMyCryptocurrencyList: LiveData<List<MyCryptocurrency>>

    ...

    // Ceci est une variable d'aide supplémentaire pour gérer correctement le spinner de devise et la préférence.
    // Elle est conservée à l'intérieur du viewmodel pour ne pas être perdue à cause de la recréation de fragment/activité.
    var newSelectedFiatCurrencyCode: String? = null

    // Variable d'aide pour stocker l'état de la disposition de rafraîchissement par glissement.
    var isSwipeRefreshing: Boolean = false


    init {
        ...

        // Définir une valeur de ressource pour une liste de cryptomonnaies que l'utilisateur possède.
        liveDataMyCryptocurrencyResourceList = cryptocurrencyRepository.getMyCryptocurrencyLiveDataResourceList(cryptocurrencyRepository.getCurrentFiatCurrencyCode())


        // Déclarer une variable supplémentaire pour pouvoir recharger les données à la demande.
        mediatorLiveDataMyCryptocurrencyResourceList.addSource(liveDataMyCryptocurrencyResourceList) {
            mediatorLiveDataMyCryptocurrencyResourceList.value = it
        }

        ...
    }

   ...

    /**
     * Lors d'une nouvelle tentative, nous devons exécuter un code séquentiel. D'abord, nous devons obtenir les identifiants des pièces de cryptomonnaie détenues depuis
     * la base de données locale, attendre la réponse et seulement après cela, utiliser ces identifiants pour faire un appel avec
     * retrofit afin d'obtenir les valeurs mises à jour des cryptomonnaies détenues. Cela peut être fait en utilisant les coroutines Kotlin.
     */
    fun retry(newFiatCurrencyCode: String? = null) {

        // Ici, nous stockons la nouvelle devise sélectionnée comme variable supplémentaire ou la réinitialisons.
        // Plus tard, si l'appel au serveur est infructueux, nous la réutiliserons pour la fonctionnalité de nouvelle tentative.
        newSelectedFiatCurrencyCode = newFiatCurrencyCode

        // Lancer une coroutine dans uiScope.
        uiScope.launch {
            // Faire un appel au serveur après un certain délai pour une meilleure expérience utilisateur.
            updateMyCryptocurrencyList(newFiatCurrencyCode, SERVER_CALL_DELAY_MILLISECONDS)
        }
    }

    // Rafraîchir les données depuis la base de données locale.
    fun refreshMyCryptocurrencyResourceList() {
        refreshMyCryptocurrencyResourceList(cryptocurrencyRepository.getMyCryptocurrencyLiveDataResourceList(cryptocurrencyRepository.getCurrentFiatCurrencyCode()))
    }

    // Pour implémenter un rafraîchissement manuel sans modifier votre logique LiveData existante.
    private fun refreshMyCryptocurrencyResourceList(liveData: LiveData<Resource<List<MyCryptocurrency>>>) {
        mediatorLiveDataMyCryptocurrencyResourceList.removeSource(liveDataMyCryptocurrencyResourceList)
        liveDataMyCryptocurrencyResourceList = liveData
        mediatorLiveDataMyCryptocurrencyResourceList.addSource(liveDataMyCryptocurrencyResourceList)
        { mediatorLiveDataMyCryptocurrencyResourceList.value = it }
    }

    private suspend fun updateMyCryptocurrencyList(newFiatCurrencyCode: String? = null, callDelay: Long = 0) {

        val fiatCurrencyCode: String = newFiatCurrencyCode
                ?: cryptocurrencyRepository.getCurrentFiatCurrencyCode()

        isSwipeRefreshing = true

        // La fonction withContext est une fonction suspendue. withContext déplace immédiatement
        // l'exécution du bloc dans un thread différent à l'intérieur du bloc, et revient lorsqu'il
        // est terminé. Le dispatcher IO est adapté pour l'exécution des requêtes réseau dans le thread IO.
        val myCryptocurrencyIds = withContext(Dispatchers.IO) {
            // Suspendre jusqu'à ce que getMyCryptocurrencyIds() retourne un résultat.
            cryptocurrencyRepository.getMyCryptocurrencyIds()
        }

        // Ici, nous revenons au thread principal. Dès que myCryptocurrencyIds a un résultat
        // et que le looper principal est disponible, la coroutine reprend sur le thread principal, et
        // [getMyCryptocurrencyLiveDataResourceList] est appelée.
        // Nous attendons que les opérations en arrière-plan se terminent, sans bloquer le thread d'origine.
        refreshMyCryptocurrencyResourceList(
                cryptocurrencyRepository.getMyCryptocurrencyLiveDataResourceList
                (fiatCurrencyCode, true, myCryptocurrencyIds, callDelay))
    }

    ...
}
```

Ici, nous appelons une fonction marquée avec un mot-clé spécial Kotlin `suspend` pour les coroutines. Cela signifie que la fonction suspend l'exécution jusqu'à ce que le résultat soit prêt, puis elle reprend là où elle s'était arrêtée avec le résultat. Pendant qu'elle est suspendue en attendant un résultat, elle débloque le thread sur lequel elle s'exécute.

De plus, dans une fonction suspendue, nous pouvons appeler une autre fonction suspendue. Comme vous le voyez, nous le faisons en appelant une nouvelle fonction suspendue marquée `withContext` qui est exécutée sur un thread différent.

L'idée de tout ce code est que nous pouvons combiner plusieurs appels pour former un code séquentiel agréable. D'abord, nous demandons à obtenir les identifiants des cryptomonnaies que nous possédons à partir de la base de données locale et nous attendons la réponse. Ce n'est qu'après l'avoir obtenue que nous utilisons les identifiants de réponse pour faire un nouvel appel avec Retrofit afin d'obtenir ces valeurs de cryptomonnaie mises à jour. C'est notre fonctionnalité de réessai.

### Nous avons réussi ! Réflexions finales, dépôt, application et présentation

Félicitations, je suis heureux si vous avez réussi à atteindre la fin. Tous les points les plus significatifs pour créer cette application ont été couverts. Il y avait beaucoup de nouvelles choses faites dans cette partie et beaucoup de cela n'est pas couvert par cet article, mais j'ai commenté mon code partout très bien donc vous ne devriez pas vous perdre dedans. Consultez le code final pour cette partie 5 ici sur GitHub :

[Voir la source sur GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-5).

Le plus grand défi pour moi personnellement n'a pas été d'apprendre de nouvelles technologies, ni de développer l'application, mais d'écrire tous ces articles. En fait, je suis très heureux de moi d'avoir relevé ce défi. Apprendre et développer est facile comparé à enseigner aux autres, mais c'est là que vous pouvez comprendre le sujet encore mieux. Mon conseil si vous cherchez la meilleure façon d'apprendre de nouvelles choses est de commencer à créer quelque chose vous-même immédiatement. Je vous promets que vous apprendrez beaucoup et rapidement.

Tous ces articles sont basés sur la version 1.0.0 de l'application « Kriptofolio » (anciennement « My Crypto Coins ») que vous pouvez télécharger en tant que fichier APK séparé [ici](https://github.com/baruckis/Kriptofolio/releases). Mais je serai très heureux si vous installez et notez la dernière version de l'application directement depuis le magasin :

#### [Disponible sur Google Play](https://play.google.com/store/apps/details?id=com.baruckis.kriptofolio)



N'hésitez pas également à visiter ce site de présentation simple que j'ai créé pour ce projet :

#### [Kriptofolio.app](https://kriptofolio.app)

![Image](https://cdn-media-1.freecodecamp.org/images/xeMQGQ5yGL06eNvYuuDFjGw0cmNBU85dBjXE)

---

**_Ačiū ! Merci d'avoir lu ! J'ai initialement publié cet article pour mon blog personnel [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-5/) le 11 mai 2019._**