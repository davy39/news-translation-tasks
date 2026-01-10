---
title: How to handle RESTful web Services using Retrofit, OkHttp, Gson, Glide and
  Coroutines
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
seo_title: null
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series — Part 5

  These days almost every Android app connects to internet to get/send data. You should
  definitely learn how to handle RESTful Web Services, as their correct implementation
  is the core knowledge while...'
---

By Andrius Baruckis

#### Kriptofolio app series — Part 5

These days almost every Android app connects to internet to get/send data. You should definitely learn how to handle RESTful Web Services, as their correct implementation is the core knowledge while creating modern apps.

This part is going to be complicated. We are going to combine multiple libraries at once to get a working result. I am not going to talk about the native Android way to handle internet requests, because in the real world nobody uses it. Every good app does not try to reinvent the wheel but instead uses the most popular third party libraries to solve common problems. It would be too complicated to recreate the functionality that these well-made libraries have to offer.

### Series content

* [Introduction: A roadmap to build a modern Android app in 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Part 1: An introduction to the SOLID principles](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* [Part 2: How to start building your Android app: creating Mockups, UI, and XML layouts](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* [Part 3: All about that Architecture: exploring different architecture patterns and how to use them in your app](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* [Part 4: How to implement Dependency Injection in your app with Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* Part 5: Handle RESTful Web Services using Retrofit, OkHttp, Gson, Glide and Coroutines (you’re here)

### What is Retrofit, OkHttp and Gson?

Retrofit is a REST Client for Java and Android. This library, in my opinion, is the most important one to learn, as it will do the main job. It makes it relatively easy to retrieve and upload JSON (or other structured data) via a REST based webservice.

In Retrofit you configure which converter is used for the data serialization. Typically to serialize and deserialize objects to and from JSON you use an open-source Java library — Gson. Also if you need, you can add custom converters to Retrofit to process XML or other protocols.

For making HTTP requests Retrofit uses the OkHttp library. OkHttp is a pure HTTP/SPDY client responsible for any low-level network operations, caching, requests and responses manipulation. In contrast, Retrofit is a high-level REST abstraction build on top of OkHttp. Retrofit is strongly coupled with OkHttp and makes intensive use of it.

Now that you know that everything is closely related, we are going to use all these 3 libraries at once. Our first goal is to get all the cryptocurrencies list using Retrofit from the Internet. We will use a special OkHttp interceptor class for CoinMarketCap API authentication when making a call to the server. We will get back a JSON data result and then convert it using the Gson library.

### Quick setup for Retrofit 2 just to try it first

When learning something new, I like to try it out in practice as soon as I can. We will apply a similar approach with Retrofit 2 for you to understand it better more quickly. Don’t worry right now about code quality or any programming principles or optimizations — we’ll just write some code to make Retrofit 2 work in our project and discuss what it does.

Follow these steps to set up Retrofit 2 on My Crypto Coins app project:

#### **First, give INTERNET permission for the app**

We are going to execute HTTP requests on a server accessible via the Internet. Give this permission by adding these lines to your Manifest file:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.baruckis.mycryptocoins">

    <uses-permission android:name="android.permission.INTERNET" />
    ...
</manifest>
```

#### **Then you should add library dependencies**

Find the latest [Retrofit version](https://square.github.io/retrofit/). Also you should know that Retrofit doesn’t ship with an integrated JSON converter. Since we will get responses in JSON format, we need to include the converter manually in the dependencies too. We are going to use latest Google’s JSON converter [Gson version](https://github.com/google/gson). Let’s add these lines to your gradle file:

```gradle
// 3rd party
// HTTP client - Retrofit with OkHttp
implementation "com.squareup.retrofit2:retrofit:$versions.retrofit"
// JSON converter Gson for JSON to Java object mapping
implementation "com.squareup.retrofit2:converter-gson:$versions.retrofit"
```

As you noticed from my comment, the OkHttp dependency is already shipped with the Retrofit 2 dependency. Versions is just a separate gradle file for convenience:

```gradle
def versions = [:]

versions.retrofit = "2.4.0"

ext.versions = versions
```

#### **Next set up the Retrofit interface**

It’s an interface that declares our requests and their types. Here we define the API on the client side.

```kotlin
/**
 * REST API access points.
 */
interface ApiService {

    // The @GET annotation tells retrofit that this request is a get type request.
    // The string value tells retrofit that the path of this request is
    // baseUrl + v1/cryptocurrency/listings/latest + query parameter.
    @GET("v1/cryptocurrency/listings/latest")
    // Annotation @Query is used to define query parameter for request. Finally the request url will
    // look like that https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?convert=EUR.
    fun getAllCryptocurrencies(@Query("convert") currency: String): Call<CryptocurrenciesLatest>
    // The return type for this function is Call with its type CryptocurrenciesLatest.
}
```

#### **And set up the data class**

Data classes are POJOs (Plain Old Java Objects) that represent the responses of the API calls we’re going to make.

```kotlin
/**
 * Data class to handle the response from the server.
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
            // The annotation to a model property lets you pass the serialized and deserialized
            // name as a string. This is useful if you don't want your model class and the JSON
            // to have identical naming.
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
                // For additional option during deserialization you can specify value or alternative
                // values. Gson will check the JSON for all names we specify and try to find one to
                // map it to the annotated property.
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

#### **Create a special interceptor class for authentication when making a call to the server**

This is the case particular for any API that requires authentication to get a successful response. Interceptors are a powerful way to customize your requests. We are going to intercept the actual request and to add individual request headers, which will validate the call with an API Key provided by [CoinMarketCap Professional API Developer Portal](https://pro.coinmarketcap.com). To get yours, you need to register there.

```kotlin
/**
 * Interceptor used to intercept the actual request and
 * to supply your API Key in REST API calls via a custom header.
 */
class AuthenticationInterceptor : Interceptor {

    override fun intercept(chain: Interceptor.Chain): Response {

        val newRequest = chain.request().newBuilder()
                // TODO: Use your API Key provided by CoinMarketCap Professional API Developer Portal.
                .addHeader("X-CMC_PRO_API_KEY", "CMC_PRO_API_KEY")
                .build()

        return chain.proceed(newRequest)
    }
}
```

#### **Finally, add this code to our activity to see Retrofit working**

I wanted to get your hands dirty as soon as possible, so I put everything in one place. This is not the correct way, but it’s the fastest instead just to see a visual result quickly.

```kotlin
class AddSearchActivity : AppCompatActivity(), Injectable {

    private lateinit var listView: ListView
    private lateinit var listAdapter: AddSearchListAdapter

    ...

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        ...

        // Later we will setup Retrofit correctly, but for now we do all in one place just for quick start.
        setupRetrofitTemporarily()
    }

    ...

    private fun setupRetrofitTemporarily() {

        // We need to prepare a custom OkHttp client because need to use our custom call interceptor.
        // to be able to authenticate our requests.
        val builder = OkHttpClient.Builder()
        // We add the interceptor to OkHttpClient.
        // It will add authentication headers to every call we make.
        builder.interceptors().add(AuthenticationInterceptor())
        val client = builder.build()


        val api = Retrofit.Builder() // Create retrofit builder.
                .baseUrl("https://sandbox-api.coinmarketcap.com/") // Base url for the api has to end with a slash.
                .addConverterFactory(GsonConverterFactory.create()) // Use GSON converter for JSON to POJO object mapping.
                .client(client) // Here we set the custom OkHttp client we just created.
                .build().create(ApiService::class.java) // We create an API using the interface we defined.


        val adapterData: MutableList<Cryptocurrency> = ArrayList<Cryptocurrency>()

        val currentFiatCurrencyCode = "EUR"

        // Let's make asynchronous network request to get all latest cryptocurrencies from the server.
        // For query parameter we pass "EUR" as we want to get prices in euros.
        val call = api.getAllCryptocurrencies("EUR")
        val result = call.enqueue(object : Callback<CryptocurrenciesLatest> {

            // You will always get a response even if something wrong went from the server.
            override fun onFailure(call: Call<CryptocurrenciesLatest>, t: Throwable) {

                Snackbar.make(findViewById(android.R.id.content),
                        // Throwable will let us find the error if the call failed.
                        "Call failed! " + t.localizedMessage,
                        Snackbar.LENGTH_INDEFINITE).show()
            }

            override fun onResponse(call: Call<CryptocurrenciesLatest>, response: Response<CryptocurrenciesLatest>) {

                // Check if the response is successful, which means the request was successfully
                // received, understood, accepted and returned code in range [200..300).
                if (response.isSuccessful) {

                    // If everything is OK, let the user know that.
                    Toast.makeText(this@AddSearchActivity, "Call OK.", Toast.LENGTH_LONG).show();

                    // Than quickly map server response data to the ListView adapter.
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
                // Else if the response is unsuccessful it will be defined by some special HTTP
                // error code, which we can show for the user.
                else Snackbar.make(findViewById(android.R.id.content),
                        "Call error with HTTP status code " + response.code() + "!",
                        Snackbar.LENGTH_INDEFINITE).show()

            }

        })

    }

   ...
}
```

You can explore the code [here](https://github.com/baruckis/Kriptofolio/tree/4d7946705b8c4dc2db3775bcc000d2918f8f1b73). Remember this is only an initial simplified implementation version for you to get the idea better.

### Final correct setup for Retrofit 2 with OkHttp 3 and Gson

Ok after a quick experiment, it is time to bring this Retrofit implementation to the next level. We already got the data successfully but not correctly. We are missing the states like loading, error and success. Our code is mixed without separation of concerns. It’s a common mistake to write all your code in an activity or a fragment. Our activity class is UI based and should only contain logic that handles UI and operating system interactions.

Actually, after this quick setup, I worked a lot and made many changes. There is no point to put all the code that was changed in the article. Better instead you should browse the final Part 5 code repo [here](https://github.com/baruckis/Kriptofolio/tree/Part-5). I have commented everything very well and my code should be clear for you to understand. But I am going to talk about most important things I have done and why I did them.

The first step to improve was to start using Dependency Injection. Remember from the [previous part](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4) we already have Dagger 2 implemented inside the project correctly. So I used it for the Retrofit setup.

```kotlin
/**
 * AppModule will provide app-wide dependencies for a part of the application.
 * It should initialize objects used across our application, such as Room database, Retrofit, Shared Preference, etc.
 */
@Module(includes = [ViewModelsModule::class])
class AppModule() {
    ...

    @Provides
    @Singleton
    fun provideHttpClient(): OkHttpClient {
        // We need to prepare a custom OkHttp client because need to use our custom call interceptor.
        // to be able to authenticate our requests.
        val builder = OkHttpClient.Builder()
        // We add the interceptor to OkHttpClient.
        // It will add authentication headers to every call we make.
        builder.interceptors().add(AuthenticationInterceptor())

        // Configure this client not to retry when a connectivity problem is encountered.
        builder.retryOnConnectionFailure(false)

        // Log requests and responses.
        // Add logging as the last interceptor, because this will also log the information which
        // you added or manipulated with previous interceptors to your request.
        builder.interceptors().add(HttpLoggingInterceptor().apply {
            // For production environment to enhance apps performance we will be skipping any
            // logging operation. We will show logs just for debug builds.
            level = if (BuildConfig.DEBUG) HttpLoggingInterceptor.Level.BODY else HttpLoggingInterceptor.Level.NONE
        })
        return builder.build()
    }

    @Provides
    @Singleton
    fun provideApiService(httpClient: OkHttpClient): ApiService {
        return Retrofit.Builder() // Create retrofit builder.
                .baseUrl(API_SERVICE_BASE_URL) // Base url for the api has to end with a slash.
                .addConverterFactory(GsonConverterFactory.create()) // Use GSON converter for JSON to POJO object mapping.
                .addCallAdapterFactory(LiveDataCallAdapterFactory())
                .client(httpClient) // Here we set the custom OkHttp client we just created.
                .build().create(ApiService::class.java) // We create an API using the interface we defined.
    }

    ...
}
```

Now as you see, Retrofit is separated from the activity class as it should be. It will be initialized only once and used app-wide.

As you may have noticed while creating the Retrofit builder instance, we added a special Retrofit calls adapter using `addCallAdapterFactory`. By default, Retrofit returns a `Call<T>`, but for our project we require it to return a `LiveData<T>` type. In order to do that we need to add `LiveDataCallAdapter` by using `LiveDataCallAdapterFactory`.

```kotlin
/**
 * A Retrofit adapter that converts the Call into a LiveData of ApiResponse.
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

Now we will get `LiveData<T>` instead of `Call<T>` as the return type from Retrofit service methods defined in the `ApiService` interface.

Another important step to make is to start using the Repository pattern. I have talked about it in [Part 3](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3). Check out our MVVM architecture schema from that post to remember where it goes.

![Image](https://cdn-media-1.freecodecamp.org/images/qlI48NPPMqMbOeV47Cpkxop4nhW8RhgfTtjO)

As you see in the picture, Repository is a separate layer for the data. It’s our single source of contact for getting or sending data. When we use Repository, we are following the separation of concerns principle. We can have different data sources (like in our case persistent data from an SQLite database and data from web services), but Repository is always going to be single source of truth for all app data.

Instead of communicating with our Retrofit implementation directly, we are going to use Repository for that. For each kind of entity, we are going to have a separate Repository.

```kotlin
/**
 * The class for managing multiple data sources.
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

    // Just a simple helper variable to store selected fiat currency code during app lifecycle.
    // It is needed for main screen currency spinner. We set it to be same as in shared preferences.
    var selectedFiatCurrencyCode: String = getCurrentFiatCurrencyCode()


    ...
  

    // The Resource wrapping of LiveData is useful to update the UI based upon the state.
    fun getAllCryptocurrencyLiveDataResourceList(fiatCurrencyCode: String, shouldFetch: Boolean = false, callDelay: Long = 0): LiveData<Resource<List<Cryptocurrency>>> {
        return object : NetworkBoundResource<List<Cryptocurrency>, CoinMarketCap<List<CryptocurrencyLatest>>>(appExecutors) {

            // Here we save the data fetched from web-service.
            override fun saveCallResult(item: CoinMarketCap<List<CryptocurrencyLatest>>) {

                val list = getCryptocurrencyListFromResponse(fiatCurrencyCode, item.data, item.status?.timestamp)

                cryptocurrencyDao.reloadCryptocurrencyList(list)
                myCryptocurrencyDao.reloadMyCryptocurrencyList(list)
            }

            // Returns boolean indicating if to fetch data from web or not, true means fetch the data from web.
            override fun shouldFetch(data: List<Cryptocurrency>?): Boolean {
                return data == null || shouldFetch
            }

            override fun fetchDelayMillis(): Long {
                return callDelay
            }

            // Contains the logic to get data from the Room database.
            override fun loadFromDb(): LiveData<List<Cryptocurrency>> {

                return Transformations.switchMap(cryptocurrencyDao.getAllCryptocurrencyLiveDataList()) { data ->
                    if (data.isEmpty()) {
                        AbsentLiveData.create()
                    } else {
                        cryptocurrencyDao.getAllCryptocurrencyLiveDataList()
                    }
                }
            }

            // Contains the logic to get data from web-service using Retrofit.
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

As you notice in the `CryptocurrencyRepository` class code, I am using the `NetworkBoundResource` abstract class. What is it and why do we need it?

`NetworkBoundResource` is a small but very important helper class that will allow us to maintain a synchronization between the local database and the web service. Our goal is to build a modern application that will work smoothly even when our device is offline. Also with the help of this class we will be able to present different network states like errors or loading for the user visually.

`NetworkBoundResource` starts by observing the database for the resource. When the entry is loaded from the database for the first time, it checks whether the result is good enough to be dispatched or if it should be re-fetched from the network. Note that both of these situations can happen at the same time, given that you probably want to show cached data while updating it from the network.

If the network call completes successfully, it saves the response into the database and re-initializes the stream. If the network request fails, the `NetworkBoundResource` dispatches a failure directly.

```kotlin
/**
 * A generic class that can provide a resource backed by both the sqlite database and the network.
 *
 *
 * You can read more about it in the [Architecture
 * Guide](https://developer.android.com/arch).
 * @param <ResultType> - Type for the Resource data.
 * @param <RequestType> - Type for the API response.
</RequestType></ResultType> */

// It defines two type parameters, ResultType and RequestType,
// because the data type returned from the API might not match the data type used locally.
abstract class NetworkBoundResource<ResultType, RequestType>
@MainThread constructor(private val appExecutors: AppExecutors) {

    // The final result LiveData.
    private val result = MediatorLiveData<Resource<ResultType>>()

    init {
        // Send loading state to UI.
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

    // Fetch the data from network and persist into DB and then send it back to UI.
    private fun fetchFromNetwork(dbSource: LiveData<ResultType>) {
        val apiResponse = createCall()
        // We re-attach dbSource as a new source, it will dispatch its latest value quickly.
        result.addSource(dbSource) { newData ->
            setValue(Resource.loading(newData))
        }

        // Create inner function as we want to delay it.
        fun fetch() {
            result.addSource(apiResponse) { response ->
                result.removeSource(apiResponse)
                result.removeSource(dbSource)
                when (response) {
                    is ApiSuccessResponse -> {
                        appExecutors.diskIO().execute {
                            saveCallResult(processResponse(response))
                            appExecutors.mainThread().execute {
                                // We specially request a new live data,
                                // otherwise we will get immediately last cached value,
                                // which may not be updated with latest results received from network.
                                result.addSource(loadFromDb()) { newData ->
                                    setValue(Resource.successNetwork(newData))
                                }
                            }
                        }
                    }
                    is ApiEmptyResponse -> {
                        appExecutors.mainThread().execute {
                            // reload from disk whatever we had
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

        // Add delay before call if needed.
        val delay = fetchDelayMillis()
        if (delay > 0) {
            Handler().postDelayed({ fetch() }, delay)
        } else fetch()

    }

    // Called when the fetch fails. The child class may want to reset components
    // like rate limiter.
    protected open fun onFetchFailed() {}

    // Returns a LiveData object that represents the resource that's implemented
    // in the base class.
    fun asLiveData() = result as LiveData<Resource<ResultType>>

    @WorkerThread
    protected open fun processResponse(response: ApiSuccessResponse<RequestType>) = response.body

    // Called to save the result of the API response into the database.
    @WorkerThread
    protected abstract fun saveCallResult(item: RequestType)

    // Called with the data in the database to decide whether to fetch
    // potentially updated data from the network.
    @MainThread
    protected abstract fun shouldFetch(data: ResultType?): Boolean

    // Make a call to the server after some delay for better user experience.
    protected open fun fetchDelayMillis(): Long = 0

    // Called to get the cached data from the database.
    @MainThread
    protected abstract fun loadFromDb(): LiveData<ResultType>

    // Called to create the API call.
    @MainThread
    protected abstract fun createCall(): LiveData<ApiResponse<RequestType>>
}
```

Under the hood, the `NetworkBoundResource` class is made by using MediatorLiveData and its ability to observe multiple LiveData sources at once. Here we have two LiveData sources: the database and the network call response. Both of those LiveData are wrapped into one MediatorLiveData which is exposed by `NetworkBoundResource`.

![Image](https://cdn-media-1.freecodecamp.org/images/qbNZeVc-RHe54xa9LSZMOfzmmrBA9rXzhGYo)
_NetworkBoundResource_

Let’s take a closer look how the `NetworkBoundResource` will work in our app. Imagine the user will launch the app and click on a floating action button on the bottom right corner. The app will launch the add crypto coins screen. Now we can analyze `NetworkBoundResource`'s usage inside it.

If the app is freshly installed and it is its first launch, then there will not be any data stored inside the local database. Because there is no data to show, a loading progress bar UI will be shown. Meanwhile the app is going to make a request call to the server via a web service to get all the cryptocurrencies list.

If the response is unsuccessful then the error message UI will be shown with the ability to retry a call by pressing a button. When a request call is successful at last, then the response data will be saved to a local SQLite database.

If we come back to the same screen the next time, the app will load data from the database instead of making a call to the internet again. But the user can ask for a new data update by implementing pull-to-refresh functionality. Old data information will be shown whilst the network call is happening. All this is done with the help of `NetworkBoundResource`.

Another class used in our Repository and `LiveDataCallAdapter` where all the "magic" happens is `ApiResponse`. Actually `ApiResponse` is just a simple common wrapper around the `Retrofit2.Response` class that converts each response to an instance of LiveData.

```kotlin
/**
 * Common class used by API responses. ApiResponse is a simple wrapper around the Retrofit2.Call
 * class that convert responses to instances of LiveData.
 * @param <CoinMarketCapType> the type of the response object
</T> */
@Suppress("unused") // T is used in extending classes
sealed class ApiResponse<CoinMarketCapType> {
    companion object {
        fun <CoinMarketCapType> create(error: Throwable): ApiErrorResponse<CoinMarketCapType> {
            return ApiErrorResponse(error.message ?: "Unknown error.")
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

                // Convert error response to JSON object.
                val gson = Gson()
                val type = object : TypeToken<CoinMarketCap<CoinMarketCapType>>() {}.type
                val errorResponse: CoinMarketCap<CoinMarketCapType> = gson.fromJson(response.errorBody()!!.charStream(), type)

                val msg = errorResponse.status?.errorMessage ?: errorResponse.message
                val errorMsg = if (msg.isNullOrEmpty()) {
                    response.message()
                } else {
                    msg
                }
                ApiErrorResponse(errorMsg ?: "Unknown error.")
            }
        }
    }
}

/**
 * Separate class for HTTP 204 resposes so that we can make ApiSuccessResponse's body non-null.
 */
class ApiEmptyResponse<CoinMarketCapType> : ApiResponse<CoinMarketCapType>()

data class ApiSuccessResponse<CoinMarketCapType>(val body: CoinMarketCapType) : ApiResponse<CoinMarketCapType>()

data class ApiErrorResponse<CoinMarketCapType>(val errorMessage: String) : ApiResponse<CoinMarketCapType>()
```

Inside this wrapper class, if our response has an error, we use the Gson library to convert the error to a JSON object. However, if the response was successful, then the Gson converter for JSON to POJO object mapping is used. We already added it when creating the retrofit builder instance with `GsonConverterFactory` inside the Dagger `AppModule` function `provideApiService`.

### Glide for image loading

[What is Glide](https://github.com/huyn/glide)? From the docs:

> Glide is a fast and efficient open source media management and image loading framework for Android that wraps media decoding, memory and disk caching, and resource pooling into a simple and easy to use interface.

> Glide’s primary focus is on making scrolling any kind of a list of images as smooth and fast as possible, but it is also effective for almost any case where you need to fetch, resize, and display a remote image.

Sounds like a complicated library which offers many useful features that you would not want to develop all by yourself. In My Crypto Coins app, we have several list screens where we need to show multiple cryptocurrency logos — pictures taken from the internet all at once — and still ensure a smooth scrolling experience for the user. So this library fits our needs perfectly. Also this library is very popular among Android developers.

Steps to setup Glide on My Crypto Coins app project:

#### **Declare dependencies**

Get the latest [Glide version](https://bumptech.github.io/glide). Again versions is a separate file `versions.gradle` for the project.

```gradle
// Glide
implementation "com.github.bumptech.glide:glide:$versions.glide"
kapt "com.github.bumptech.glide:compiler:$versions.glide"
// Glide's OkHttp3 integration.
implementation "com.github.bumptech.glide:okhttp3-integration:$versions.glide"+"@aar"
```

Because we want to use the networking library OkHttp in our project for all network operations, we need to include the specific Glide integration for it instead of the default one. Also since Glide is going to perform a network request to load images via the internet, we need to include the permission `INTERNET` in our `AndroidManifest.xml` file — but we already did that with the Retrofit setup.

#### **Create AppGlideModule**

Glide v4, which we will be using, offers a generated API for Applications. It will use an annotation processor to generate an API that allows applications to extend Glide’s API and include components provided by integration libraries. For any app to access the generated Glide API we need to include an appropriately annotated `AppGlideModule` implementation. There can be only a single implementation of the generated API and only one `AppGlideModule` per application.

Let’s create a class extending `AppGlideModule` somewhere in your app project:

```kotlin
/**
 * Glide v4 uses an annotation processor to generate an API that allows applications to access all
 * options in RequestBuilder, RequestOptions and any included integration libraries in a single
 * fluent API.
 *
 * The generated API serves two purposes:
 * Integration libraries can extend Glide’s API with custom options.
 * Applications can extend Glide’s API by adding methods that bundle commonly used options.
 *
 * Although both of these tasks can be accomplished by hand by writing custom subclasses of
 * RequestOptions, doing so is challenging and produces a less fluent API.
 */
@GlideModule
class AppGlideModule : AppGlideModule()
```

Even if our application is not changing any additional settings or implementing any methods in `AppGlideModule`, we still need to have its implementation to use Glide. You're not required to implement any of the methods in `AppGlideModule` for the API to be generated. You can leave the class blank as long as it extends `AppGlideModule` and is annotated with `@GlideModule`.

#### **Use Glide-generated API**

When using `AppGlideModule`, applications can use the API by starting all loads with `GlideApp.with()`. This is the code that shows how I have used Glide to load and show cryptocurrency logos in the add crypto coins screen all cryptocurrencies list.

```kotlin
class AddSearchListAdapter(val context: Context, private val cryptocurrencyClickCallback: ((Cryptocurrency) -> Unit)?) : BaseAdapter() {

    ...

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        ...

        val itemBinding: ActivityAddSearchListItemBinding

        ...

        // We make an Uri of image that we need to load. Every image unique name is its id.
        val imageUri = Uri.parse(CRYPTOCURRENCY_IMAGE_URL).buildUpon()
                .appendPath(CRYPTOCURRENCY_IMAGE_SIZE_PX)
                .appendPath(cryptocurrency.id.toString() + CRYPTOCURRENCY_IMAGE_FILE)
                .build()

        // Glide generated API from AppGlideModule.
        GlideApp
                // We need to provide context to make a call.
                .with(itemBinding.root)
                // Here you specify which image should be loaded by providing Uri.
                .load(imageUri)
                // The way you combine and execute multiple transformations.
                // WhiteBackground is our own implemented custom transformation.
                // CircleCrop is default transformation that Glide ships with.
                .transform(MultiTransformation(WhiteBackground(), CircleCrop()))
                // The target ImageView your image is supposed to get displayed in.
                .into(itemBinding.itemImageIcon.imageview_front)

        ...

        return itemBinding.root
    }

    ...

}
```

As you see, you can start using Glide with just few lines of code and let it do all the hard work for you. It is pretty straightforward.

### Kotlin Coroutines

While building this app, we are going to face situations when we will run time consuming tasks such as writing data to a database or reading from it, fetching data from the network and other. All these common tasks take longer to complete than allowed by the Android framework’s main thread.

The main thread is a single thread that handles all updates to the UI. Developers are required not to block it to avoid the app freezing or even crashing with an Application Not Responding dialog. Kotlin coroutines is going to solve this problem for us by introducing main thread safety. It is the last missing piece that we want to add for My Crypto Coins app.

Coroutines are a Kotlin feature that convert async callbacks for long-running tasks, such as database or network access, into sequential code. With coroutines, you can write asynchronous code, which was traditionally written using the Callback pattern, using a synchronous style. The return value of a function will provide the result of the asynchronous call. Code written sequentially is typically easier to read, and can even use language features such as exceptions.

So we are going to use coroutines everywhere in this app where we need to wait until a result is available from a long-running task and than continue execution. Let’s see one exact implementation for our ViewModel where we will retry getting the latest data from the server for our cryptocurrencies presented on the main screen.

First add coroutines to the project:

```gradle
// Coroutines support libraries for Kotlin.

// Dependencies for coroutines.
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-core:$versions.coroutines"

// Dependency is for the special UI context that can be passed to coroutine builders that use
// the main thread dispatcher to dispatch events on the main thread.
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:$versions.coroutines"
```

Then we will create abstract class which will become the base class to be used for any ViewModel that needs to have common functionality like coroutines in our case:

```kotlin
abstract class BaseViewModel : ViewModel() {

    // In Kotlin, all coroutines run inside a CoroutineScope.
    // A scope controls the lifetime of coroutines through its job.
    private val viewModelJob = Job()
    // Since uiScope has a default dispatcher of Dispatchers.Main, this coroutine will be launched
    // in the main thread.
    val uiScope = CoroutineScope(Dispatchers.Main + viewModelJob)


    // onCleared is called when the ViewModel is no longer used and will be destroyed.
    // This typically happens when the user navigates away from the Activity or Fragment that was
    // using the ViewModel.
    override fun onCleared() {
        super.onCleared()
        // When you cancel the job of a scope, it cancels all coroutines started in that scope.
        // It's important to cancel any coroutines that are no longer required to avoid unnecessary
        // work and memory leaks.
        viewModelJob.cancel()
    }
}
```

Here we create specific coroutine scope, which will control the lifetime of coroutines through its job. As you see, scope allows you to specify a default dispatcher that controls which thread runs a coroutine. When the ViewModel is no longer used, we cancel `viewModelJob` and with that every coroutine started by `uiScope` will be cancelled as well.

Finally, implement the retry functionality:

```kotlin
/**
 * The ViewModel class is designed to store and manage UI-related data in a lifecycle conscious way.
 * The ViewModel class allows data to survive configuration changes such as screen rotations.
 */

// ViewModel will require a CryptocurrencyRepository so we add @Inject code into ViewModel constructor.
class MainViewModel @Inject constructor(val context: Context, val cryptocurrencyRepository: CryptocurrencyRepository) : BaseViewModel() {

    ...

    val mediatorLiveDataMyCryptocurrencyResourceList = MediatorLiveData<Resource<List<MyCryptocurrency>>>()
    private var liveDataMyCryptocurrencyResourceList: LiveData<Resource<List<MyCryptocurrency>>>
    private val liveDataMyCryptocurrencyList: LiveData<List<MyCryptocurrency>>

    ...

    // This is additional helper variable to deal correctly with currency spinner and preference.
    // It is kept inside viewmodel not to be lost because of fragment/activity recreation.
    var newSelectedFiatCurrencyCode: String? = null

    // Helper variable to store state of swipe refresh layout.
    var isSwipeRefreshing: Boolean = false


    init {
        ...

        // Set a resource value for a list of cryptocurrencies that user owns.
        liveDataMyCryptocurrencyResourceList = cryptocurrencyRepository.getMyCryptocurrencyLiveDataResourceList(cryptocurrencyRepository.getCurrentFiatCurrencyCode())


        // Declare additional variable to be able to reload data on demand.
        mediatorLiveDataMyCryptocurrencyResourceList.addSource(liveDataMyCryptocurrencyResourceList) {
            mediatorLiveDataMyCryptocurrencyResourceList.value = it
        }

        ...
    }

   ...

    /**
     * On retry we need to run sequential code. First we need to get owned crypto coins ids from
     * local database, wait for response and only after it use these ids to make a call with
     * retrofit to get updated owned crypto values. This can be done using Kotlin Coroutines.
     */
    fun retry(newFiatCurrencyCode: String? = null) {

        // Here we store new selected currency as additional variable or reset it.
        // Later if call to server is unsuccessful we will reuse it for retry functionality.
        newSelectedFiatCurrencyCode = newFiatCurrencyCode

        // Launch a coroutine in uiScope.
        uiScope.launch {
            // Make a call to the server after some delay for better user experience.
            updateMyCryptocurrencyList(newFiatCurrencyCode, SERVER_CALL_DELAY_MILLISECONDS)
        }
    }

    // Refresh the data from local database.
    fun refreshMyCryptocurrencyResourceList() {
        refreshMyCryptocurrencyResourceList(cryptocurrencyRepository.getMyCryptocurrencyLiveDataResourceList(cryptocurrencyRepository.getCurrentFiatCurrencyCode()))
    }

    // To implement a manual refresh without modifying your existing LiveData logic.
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

        // The function withContext is a suspend function. The withContext immediately shifts
        // execution of the block into different thread inside the block, and back when it
        // completes. IO dispatcher is suitable for execution the network requests in IO thread.
        val myCryptocurrencyIds = withContext(Dispatchers.IO) {
            // Suspend until getMyCryptocurrencyIds() returns a result.
            cryptocurrencyRepository.getMyCryptocurrencyIds()
        }

        // Here we come back to main worker thread. As soon as myCryptocurrencyIds has a result
        // and main looper is available, coroutine resumes on main thread, and
        // [getMyCryptocurrencyLiveDataResourceList] is called.
        // We wait for background operations to complete, without blocking the original thread.
        refreshMyCryptocurrencyResourceList(
                cryptocurrencyRepository.getMyCryptocurrencyLiveDataResourceList
                (fiatCurrencyCode, true, myCryptocurrencyIds, callDelay))
    }

    ...
}
```

Here we call a function marked with a special Kotlin keyword `suspend` for coroutines. This means that the function suspends execution until the result is ready, then it resumes where it left off with the result. While it is suspended waiting for a result, it unblocks the thread that it is running on.

Also, in one suspend function we can call another suspend function. As you see we do that by calling new suspend function marked `withContext` that is executed on different thread.

The idea of all this code is that we can combine multiple calls to form nice-looking sequential code. First we request to get the ids of the cryptocurrencies we own from the local database and wait for the response. Only after we get it do we use the response ids to make a new call with Retrofit to get those updated cryptocurrency values. That is our retry functionality.

### We made it! Final thoughts, repository, app & presentation

Congratulations, I am happy if you managed to reach to the end. All the most significant points for creating this app have been covered. There was plenty of new stuff done in this part and a lot of that is not covered by this article, but I commented my code everywhere very well so you should not get lost in it. Check out final code for this part 5 here on GitHub:

[View Source On GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-5).

The biggest challenge for me personally was not to learn new technologies, not to develop the app, but to write all these articles. Actually I am very happy with myself that I completed this challenge. Learning and developing is easy compared to teaching others, but that is where you can understand the topic even better. My advice if you are looking for the best way to learn new things is to start creating something yourself immediately. I promise you will learn a lot and quickly.

All these articles are based on version 1.0.0 of “Kriptofolio” (previously “My Crypto Coins”) app which you can download as a separate APK file [here](https://github.com/baruckis/Kriptofolio/releases). But I will be very happy if you install and rate the latest app version from the store directly:

#### [Get It On Google Play](https://play.google.com/store/apps/details?id=com.baruckis.kriptofolio)



Also please feel free to visit this simple presentation website that I made for this project:

#### [Kriptofolio.app](https://kriptofolio.app)

![Image](https://cdn-media-1.freecodecamp.org/images/xeMQGQ5yGL06eNvYuuDFjGw0cmNBU85dBjXE)

---

**_Ačiū! Thanks for reading! I originally published this post for my personal blog [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-5/) on May 11, 2019._**

