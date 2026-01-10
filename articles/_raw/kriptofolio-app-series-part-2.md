---
title: 'How to start building your Android app: creating Mockups, UI, and XML layouts'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-14T12:39:30.000Z'
originalURL: https://freecodecamp.org/news/kriptofolio-app-series-part-2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tewVfnzAfO8iuqskpoIdow.png
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: Cryptocurrency
  slug: cryptocurrency
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
seo_title: null
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 2

  So how do you actually start to build a new app? What should be your first move?
  If you think we just need to launch Android Studio and jump directly to the code,
  think again. That’s exactly the thi...'
---

By Andrius Baruckis

#### Kriptofolio app series - Part 2

So how do you actually start to build a new app? What should be your first move? If you think we just need to launch Android Studio and jump directly to the code, think again. That’s exactly the thing I would advise not to do as it can do more damage than good. But it is so tempting to start writing your first lines of code as soon as possible.

Instead I would suggest focusing on making a wise plan with UI mockups. Remember that every good new app project should start with that. With this approach you will not loose a lot of time and will be able to build high quality products from the beginning.

So in this part of the series, I will present “Kriptofolio” (previously “My Crypto Coins”) app mockups and discuss how to create them. Also we are going to build all the UI layouts. These layouts will become our solid foundation indicating clearly what to code. Finally we will localize our app to different languages and learn how to handle the ones which are written from right to left.

### Series content

* [Introduction: A roadmap to build a modern Android app in 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Part 1: An introduction to the SOLID principles](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* Part 2: How to start building your Android app: creating Mockups, UI, and XML layouts (you’re here)
* [Part 3: All about that Architecture: exploring different architecture patterns and how to use them in your app](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* [Part 4: How to implement Dependency Injection in your app with Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* [Part 5: Handle RESTful Web Services using Retrofit, OkHttp, Gson, Glide and Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### Mockups

There are various ways you can create your project mockups. The simplest one is to take a pencil and a sheet of paper and start drawing on it. The best part is this way doesn’t cost you anything and you can start immediately. Oh and I almost forgot, you should also get yourself an eraser as there will not be any undo function. ?

If you, like I, feel that you need more functionality, then consider using special software for creating detailed mockups. I prefer using software instead of pencil & paper, even if it requires you to invest your money to buy it and your time to learn how to use it.

There are various software options on the market to choose from. You will have to do your own investigation into which one best fits all your needs. For all my projects mockups right now I am using [Balsamiq](https://balsamiq.com/) Mockups for Desktop app. Balsamiq is rapid, effective and very easy to use wire framing software. As I am rather happy with it, I recommend it for creating Android apps, so please feel free to try.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G5TA06Hy-zj-uaxxcb1zyw.jpeg)

I started My Crypto Coins app project by creating well thought-out and very detailed mockups. I thought to myself that if I create everything in a very detailed way, than I will avoid mistakes. I will also not waste time for suddenly changing functionality during the development process. If you put a lot of effort in creating good mockups, than, with a little bit of imagination, you can see and feel the final product.

My goal was to have everything defined in the mockups like it should look in the end product. For that I tried not to rush but to spend as much time as I needed. Here are my final mockups for My Crypto Coins app:

![Image](https://cdn-media-1.freecodecamp.org/images/1*ciWyOJ2Lftb7hiXLNYNl9Q.png)
_Mockup of My Crypto Coins app made with Balsamiq Mockups software_

### Stock design — Material

Another important thing to talk about is the app’s visual design. At the time of this writing, [Material Design](https://en.wikipedia.org/wiki/Material_Design) is the stock visual design recommended by Google for all Android apps. And guess what — you can’t go wrong with stock design.

For My Crypto Coins app we will be using Material Design. The app follows the best practices defined in the detailed online guidelines.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0kyrt1pJA8XaUSKE9j1INg.jpeg)

[Material.io/guidelines](https://material.io/guidelines) — official material design living specs document which will be our design guidelines for this project.

### Layouts

Now when we already have wireframes of our app prepared, it’s time to build real UI. Again we could jump into writing code, but why rush? Instead I would recommend concentrating on building all your XML layouts. My advice here would be that the more you manage to put into XML the less code you will need to write.

The Android team constantly improves the way you can build your UI by adding new features to XML layouts. Sometimes it’s so tempting to write few lines of code to reach a desired look. But it’s better to investigate the topic more deeply to find if it is possible to do without code. Remember: less code makes your project look cleaner. It will also be more understandable for other developers and easier to maintain.

Finally when you create all your XML layouts, you will feel like you have your app made. You will be able to launch it and see how it feels for the end user. It doesn’t matter that it is showing some fake data and does nothing. Now you have the last chance to make some drastic changes.

If you are building an app for somebody else, it’s such a good time to present it. Maybe you will be asked to make some surprising last minute changes. That way you will avoid writing code for functionality that will never be used. A lot of people don’t have enough imagination and they need to see and touch first to decide if it is what they want. So don’t leave your layouts for the last step in your work process.

For this app I will be using various components that are common in all modern Android apps:

* [CoordinatorLayout](https://developer.android.com/reference/android/support/design/widget/CoordinatorLayout) — a super-powered FrameLayout, the main appeal of which is its ability to coordinate the animations and transitions of the views within it.
* [AppBarLayout](https://developer.android.com/reference/android/support/design/widget/AppBarLayout) — a vertical LinearLayout which implements many of the features of material design’s app bar concept, namely scrolling gestures.
* [Toolbar](https://developer.android.com/reference/android/support/v7/widget/Toolbar) — a generalization of action bars for use within application layouts.
* [CollapsingToolbarLayout](https://developer.android.com/reference/android/support/design/widget/CollapsingToolbarLayout) — a wrapper for Toolbar which implements a collapsing app bar. It is designed to be used as a direct child of a AppBarLayout.
* [ConstraintLayout](https://developer.android.com/reference/android/support/constraint/ConstraintLayout) — a ViewGroup which allows you to position and size widgets in a flexible way. Imagine a RelativeLayout on steroids.
* [SwipeRefreshLayout](https://developer.android.com/reference/android/support/v4/widget/SwipeRefreshLayout) — the widget which allows the swipe-to-refresh user interface pattern to be implemented entirely. It detects the vertical swipe, displays a distinctive progress bar, and triggers callback methods in your app.
* [FloatingActionButton](https://developer.android.com/reference/android/support/design/widget/FloatingActionButton) — a circular button that triggers the primary action in your app’s UI.

For the main screen we will use a combination of all these components to create nice UI/UX. Users can expand and collapse the top part of the layout to find the total value of all their cryptocurrency portfolio. They can check any change in value during the last 24 hours and change selected fiat currency.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j3GzRC56EjaWxMvhE8O2cQ.png)
_Main screen layout creation_

Of course there are other components besides these nine. It is very important to master the whole component palette to know which one to use in any particular case. With the mobile trends changing from time to time the palette will expand too.

I am not going to talk about every component, but my advice is to investigate that on your own. For me the best way to understand them is by trying to build XML layouts manually instead of using automatic drag & drop tools in Android Studio.

### Styles, Colors, Dimensions, Strings, Icons

At first glance, the things mentioned in this section title may appear not to be important ones. However, I ask that you to put in effort when creating them in any app if you want to make it modern and exclusive. Remember this blog posts series is how to build a MODERN Android app! No matter how wrong it is, people will usually judge your app by its looks first, not its functionality.

So here is a perfect chance to earn new users love from the beginning. These are my tips:

* When building your XML layout files, you should recognize where you repeat some common attributes for the views. Move them to be defined as separate XML styles. That way you will have shorter XML layout files. You can control all the app styling aspects from a separate place. Imagine what benefit it will give you. For example, you could allow the user to choose the app skin (bright, dark, etc.).
* Define all your app colors in a separate file too, and enjoy ability to experiment with the look by changing them immediately. Sometimes the same product can be given new life and engage users again by simply refreshing with new colors. There are quite a few websites that can help you choose nice colors, but my favorite one is [MaterialPalette.com](https://www.materialpalette.com/), so take a look.
* Define your app dimensions in a separate file. This will allow you to adjust your app to look good on different size screens.
* All your strings should not be hard-coded, and Android Studio will inform you if you forget. Do not ignore that. The best part when your strings are separated is you can translate your app to different languages.
* When using icons for your app, always prefer an XML vector drawable format. That’s the new recommended standard and a clever way to go to avoid any pixelation. To find many professionally made material design style icons from the community, please check out [MaterialDesignIcons.com](https://materialdesignicons.com/). I used this website to get icons for My Crypto Coins app.

### RecyclerView

The main screen of My Crypto Coins app will consist of a list of cryptocurrencies that the user holds. For this purpose the RecyclerView widget is the best fit. It is a widget that displays a scrolling list of elements based on large data sets (or data that frequently changes).

Because of its advantages, RecyclerView is the recommended component for creating any list screen. It is a more advanced and flexible version of the simpler ListView component. We will talk about it later too. In this part we are creating just layouts. We are not concentrating on coding.

To see our app visually, we will have to implement RecyclerView by writing some code. These are the steps to implement RecyclerView:

#### 1. Add a RecyclerView component.

Our `MainActivity` layout is `activity_main.xml`. This layout includes `content_main.xml` layout which is a fragment. This `MainActivityListFragment` layout inflates `fragment_main_list.xml`. So you should add RecyclerView component here.

```xml
...
<android.support.v7.widget.RecyclerView
    android:id="@+id/recyclerview_fragment_main_list"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:background="@color/colorForMainListBackground"
    android:clipToPadding="false"
    android:paddingBottom="72dp"
    android:paddingTop="5dp"
    android:scrollbarStyle="outsideOverlay"
    android:scrollbars="vertical" />
...
```

As you see we configure our RecyclerView to leave some padding space at the bottom. We do this to avoid covering the last list item with the FloatingActionButton. Also we turn on the vertical scrollbar so it’s available.

#### 2. Create RecyclerView row layout.

For our initial purpose we will only set the item name for each row. Our simplified layout should look like this.

```xml
<android.support.v7.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginBottom="@dimen/main_cardview_list_item_outer_top_bottom_margin"
    android:layout_marginEnd="@dimen/main_cardview_list_item_outer_start_end_margin"
    android:layout_marginStart="@dimen/main_cardview_list_item_outer_start_end_margin"
    android:layout_marginTop="@dimen/main_cardview_list_item_outer_top_bottom_margin"
    android:foreground="?android:attr/selectableItemBackground"
    android:clickable="true"
    android:focusable="true"
    app:cardBackgroundColor="@color/colorForMainListItemBackground">

    <android.support.constraint.ConstraintLayout
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:padding="@dimen/main_cardview_list_item_inner_margin">
        ...
        <android.support.v7.widget.AppCompatTextView
            android:id="@+id/item_name"
            style="@style/MainListItemPrimeText"
            android:layout_marginEnd="@dimen/main_cardview_list_item_text_between_margin"
            android:layout_marginStart="@dimen/main_cardview_list_item_inner_margin"
            app:layout_constraintBottom_toTopOf="@+id/item_amount_symbol"
            app:layout_constraintEnd_toStartOf="@+id/guideline1_percent"
            app:layout_constraintStart_toEndOf="@+id/item_image_icon"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintVertical_chainStyle="spread"
            tools:text="@string/sample_text_item_name" />
        ...
    </android.support.constraint.ConstraintLayout>

</android.support.v7.widget.CardView>
```

#### 3. Create data adapter class.

Our adapter for now will accept string data. Later we will need to create a separate class data model. We will need to pass more information than only one string.

```kotlin
class MainRecyclerViewAdapter(val dataList: ArrayList<String>) : RecyclerView.Adapter<MainRecyclerViewAdapter.CustomViewHolder>() {

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomViewHolder {
        val v = LayoutInflater.from(parent.context).inflate(R.layout.fragment_main_list_item, parent, false)
        return CustomViewHolder(v)
    }

    override fun onBindViewHolder(holder: CustomViewHolder, position: Int) {
        holder.txtName?.text = dataList[position]
    }

    override fun getItemCount(): Int {
        return dataList.size
    }


    inner class CustomViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        val txtName = itemView.findViewById<TextView>(R.id.item_name)
    }
}
```

#### 4. Connect RecyclerView to custom adapter.

```kotlin
class MainActivityListFragment : Fragment() {

    private lateinit var recyclerView: RecyclerView
    private lateinit var recyclerAdapter: MainRecyclerViewAdapter

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?,
                              savedInstanceState: Bundle?): View? {
        val v: View = inflater.inflate(R.layout.fragment_main_list, container, false)

        recyclerView = v.findViewById(R.id.recyclerview_fragment_main_list)

        return v
    }

    override fun onActivityCreated(savedInstanceState: Bundle?) {

        super.onActivityCreated(savedInstanceState)

        setupList()
    }

    private fun setupList() {

        val data = ArrayList<String>()
        data.add("Bitcoin")
        data.add("Etherium")
        data.add("Ripple")
        data.add("Bitcoin Cash")
        data.add("Litecoin")
        data.add("NEO")
        data.add("Stellar")
        data.add("EOS")
        data.add("Cardano")
        data.add("Stellar")
        data.add("IOTA")
        data.add("Dash")
        data.add("Monero")
        data.add("TRON")
        data.add("NEM")
        data.add("ICON")
        data.add("Bitcoin Gold")
        data.add("Zcash")
        data.add("Verge")

        recyclerView.layoutManager = LinearLayoutManager(activity)
        recyclerAdapter = MainRecyclerViewAdapter(data)
        recyclerView.adapter = recyclerAdapter
    }
}
```

Done! Now our main screen looks like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1WVQXLqwxuXb910bQcc54Q.png)
_Main screen_

### ListView

In this project, we will use ListView for the screen where you can add crypto coin(s) which you already hold. Because of its shortcomings in recent years it is hardly used anymore.

So I guess a lot of you at this moment are wondering why I decided to use it in My Crypto Coins app when we could create the same functionality easily with RecyclerView.

Remember, though, that this project was created for training purposes first. I thought it would be beneficial to gain insights into ListView and how it works. Any developer may run into ListView in legacy code, and it’s best to know how to work with it. Besides, the list we will be creating is so simple that ListView’s technical limitations won’t cause us any problems.

Let’s follow the very similar steps needed to implement ListView:

#### 1. Add a ListView component.

The first thing to do is to add a ListView to `AddSearchActivity`. Open the activity layout file `activity_add_search.xml` and you will see that it includes `content_add_search.xml`. There we will add the ListView component.

```xml
...
<ListView
    android:id="@+id/listview_activity_add_search"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:scrollbars="vertical" />
...
```

#### 2. Create ListView row layout.

As before, just for initial purposes, we will only set the item name for each row. Here is the simplified layout:

```xml
<android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="@dimen/add_search_list_item_inner_margin">
    ...
    <android.support.v7.widget.AppCompatTextView
        android:id="@+id/item_name"
        style="@style/AddSearchListItemPrimeText"
        android:layout_marginEnd="@dimen/add_search_list_item_text_between_margin_2x"
        android:layout_marginStart="@dimen/add_search_list_item_text_between_margin"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toStartOf="@+id/item_symbol"
        app:layout_constraintStart_toEndOf="@+id/item_image_icon"
        app:layout_constraintTop_toTopOf="parent"
        tools:text="@string/sample_text_item_name" />
    ...
</android.support.constraint.ConstraintLayout>
```

#### 3. Create data adapter class.

Like RecyclerView our ListView adapter for now will accept only string data to get the item name and show it on screen. Later we will use a separate class data model. As for this part, we want to build a very simple list displaying only cryptocurrency titles. Instead of creating our custom adapter we could use the default, ArrayAdapter.

```kotlin
class AddSearchListAdapter(context: Context, private val dataSource: ArrayList<String>) : BaseAdapter() {

    private val inflater: LayoutInflater = context.getSystemService(Context.LAYOUT_INFLATER_SERVICE) as LayoutInflater

    override fun getView(position: Int, convertView: View?, parent: ViewGroup?): View {
        val view: View
        val holder: CustomViewHolder

        if (convertView == null) {

            view = inflater.inflate(R.layout.activity_add_search_list_item, parent, false)

            holder = CustomViewHolder()
            holder.nameTextView = view.findViewById(R.id.item_name)

            view.tag = holder

        } else {

            view = convertView
            holder = convertView.tag as CustomViewHolder
        }

        val nameTextView = holder.nameTextView

        nameTextView.text = getItem(position) as String

        return view
    }

    override fun getItem(position: Int): Any {
        return dataSource[position]
    }

    override fun getItemId(position: Int): Long {
        return position.toLong();
    }

    override fun getCount(): Int {
        return dataSource.size
    }


    inner class CustomViewHolder {
        lateinit var nameTextView: AppCompatTextView
    }

}
```

As you see in the adapter code, by creating `CustomViewHolder` object I use the ViewHolder pattern. It stores list row view references. Calling the `findViewById()` method only occurs a couple of times. It allows us to make our list scrolling act smoothly and efficiently.

The ListView doesn’t require us to use the ViewHolder pattern. The RecyclerView’s adapter gives us that kind of protection by default, as it forces us to use it.

#### 4. Connect ListView to custom adapter.

With default ArrayAdapter it could look like `val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, data)`. That’s the beauty of the ListView component. If you want, you can create a simple list really fast without building your own adapter or row layout (skip steps 2 and 3).

```kotlin
class AddSearchActivity : AppCompatActivity() {

    private lateinit var listView: ListView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_add_search)
        setSupportActionBar(toolbar2)
        supportActionBar?.setDisplayHomeAsUpEnabled(true)

        val data = ArrayList<String>()
        data.add("Bitcoin")
        data.add("Etherium")
        data.add("Ripple")
        data.add("Bitcoin Cash")
        data.add("Litecoin")
        data.add("NEO")
        data.add("Stellar")
        data.add("EOS")
        data.add("Cardano")
        data.add("Stellar")
        data.add("IOTA")
        data.add("Dash")
        data.add("Monero")
        data.add("TRON")
        data.add("NEM")
        data.add("ICON")
        data.add("Bitcoin Gold")
        data.add("Zcash")
        data.add("Verge")

        val adapter = AddSearchListAdapter(this, data)

        listView = findViewById(R.id.listview_activity_add_search)
        listView.adapter = adapter

    }
    ...
}
```

ListView setup is ready!

![Image](https://cdn-media-1.freecodecamp.org/images/1*6lpfmyzidzGQju_YmPHekQ.png)
_Add crypto coin(-s) screen_

### SearchView

In the same screen with all cryptocurrencies listed, we also need to add SearchView. Search will be a useful functionality to have for any user who wants to find a specific cryptocurrency by typing its name. For this part we will not build functionality fully but just implement its visual part. Follow these steps to add SearchView to the project:

#### 1. Declare the searchable configuration in XML.

The searchable configuration file should be added in your res directory named xml. Here you can specify attributes for your SearchView component which define how it behaves.

```xml
<searchable
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/app_name"
    android:hint="@string/search_hint">
</searchable>
```

#### 2. Create new activity which will become our searchable activity.

We are going to create new blank activity which extends `AppCompatActivity()`. We will name it `AddSearchActivity`.

#### 3. Specify newly created activity in Android manifest file to be searchable.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.baruckis.mycryptocoins">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        ...
        <activity
            android:name=".AddSearchList.AddSearchActivity"
            android:launchMode="singleTop"
            android:parentActivityName=".MainList.MainActivity"
            android:theme="@style/AppTheme.NoActionBar">
            <intent-filter>
                <action android:name="android.intent.action.SEARCH" />
            </intent-filter>
            <meta-data
                android:name="android.app.searchable"
                android:resource="@xml/searchable" />
        </activity>
        ...
    </application>

</manifest>
```

We will let the Android system handle the search process. That’s why we add the intent action search and meta-data in the activity element of the `AddSearchActivity`. The meta-data has name and resource which is linked to the searchable configuration file located in the res/xml folder.

#### 4. Create search menu.

Inside the res/menu folder we are going to create a menu resource file.

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">
    <item
        android:id="@+id/search"
        android:icon="@drawable/ic_search"
        android:title="@string/action_search"
        app:actionViewClass="android.support.v7.widget.SearchView"
        app:showAsAction="ifRoom|collapseActionView" />
</menu>
```

#### 5. Add search menu to activity.

We will add the Android search widget as a menu action view.

```kotlin
class AddSearchActivity : AppCompatActivity() {
    ...
    override fun onCreateOptionsMenu(menu: Menu?): Boolean {

        menuInflater.inflate(R.menu.menu_search, menu)

        val searchManager = getSystemService(Context.SEARCH_SERVICE) as SearchManager
        val searchView = menu?.findItem(R.id.search)?.actionView as SearchView
        searchView.setSearchableInfo(searchManager.getSearchableInfo(componentName))
        searchView.maxWidth = Integer.MAX_VALUE

        return true
    }
}
```

Now the SearchView is added to the activity. Still the search functionality is not working. But we have it implemented as we wanted for this part.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H04EuFhD3r1vrIHSD_tbJg.png)
_Add crypto coin(-s) screen — search functionality_

### Settings

If you want to create a modern Android app, I recommend that you include a settings screen and give access to app settings for the user. Including settings in your app gives your users the power to control some of the functionality of your app which makes them happier. They are now in control of how the app behaves. So we are going to create a settings screen for My Crypto Coins app too.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m6NnpRpwZnrsAeKW6rybqA.png)
_New Settings Activity from gallery template_

You can create a settings screen with Android Studio template and it will generate all the code you need. By default at the time of writing this blog post, settings activity is generated with preference headers. That’s not what we want for such a small app where we plan to have only few settings at first.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kdlb-ZQKonUu-9xeTe0Nbw.png)
_Default settings template with preference headers_

Therefore we are going to build everything manually. Settings screen is designed with an XML-like layout. Let’s go step by step to create again only the visual part for this blog post:

#### 1. Create preferences screen XML file.

We are going to create the preferences screen XML file which should be placed in the res/xml directory.

```xml
<PreferenceScreen xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <PreferenceCategory android:title="@string/pref_general_category_title">
        <ListPreference
            android:defaultValue="@string/pref_default_language_value"
            android:entries="@array/pref_language_list_entries"
            android:entryValues="@array/pref_language_list_values"
            android:icon="@drawable/ic_translate"
            android:key="language_list"
            android:summary="@string/pref_default_language_entry"
            android:title="@string/pref_language_title"
            tools:summary="@string/pref_default_language_entry" />

        <ListPreference
            android:defaultValue="@string/pref_default_fiat_currency_value"
            android:entries="@array/pref_fiat_currency_list_entries"
            android:entryValues="@array/pref_fiat_currency_list_values"
            android:icon="@drawable/ic_cash"
            android:key="fiat_currency_list"
            android:summary="@string/pref_default_fiat_currency_entry"
            android:title="@string/pref_fiat_currency_title"
            tools:summary="@string/pref_default_fiat_currency_entry" />

        <ListPreference
            android:defaultValue="@string/pref_default_date_format_value"
            android:entries="@array/pref_date_format_list_entries"
            android:entryValues="@array/pref_date_format_list_values"
            android:icon="@drawable/ic_date_range"
            android:key="date_format_list"
            android:summary="@string/pref_default_date_format_entry"
            android:title="@string/pref_date_format_title"
            tools:summary="@string/pref_default_date_format_entry" />

        <SwitchPreference
            android:defaultValue="true"
            android:icon="@drawable/ic_calendar_clock"
            android:key="24h_switch"
            android:summary="@string/pref_24h_switch_summary"
            android:title="@string/pref_24h_switch_title" />

    </PreferenceCategory>

    <PreferenceCategory android:title="@string/pref_support_category_title">

        <Preference
            android:icon="@drawable/ic_star"
            android:title="@string/pref_rate_app_title" />

        <Preference
            android:icon="@drawable/ic_share"
            android:title="@string/pref_share_app_title" />

        <Preference
            android:icon="@drawable/ic_attach_money"
            android:summary="@string/pref_donate_view_summary"
            android:title="@string/pref_donate_view_title" />

        <Preference
            android:icon="@drawable/ic_currency_btc"
            android:summary="@string/pref_donate_crypto_summary"
            android:title="@string/pref_donate_crypto_title" />

    </PreferenceCategory>

    <PreferenceCategory android:title="@string/pref_support_about_title">

        <Preference
            android:icon="@drawable/ic_web"
            android:summary="@string/pref_website_summary"
            android:title="@string/pref_website_title" />

        <Preference
            android:icon="@drawable/ic_human_greeting"
            android:summary="@string/pref_author_summary"
            android:title="@string/pref_author_title" />

        <Preference
            android:icon="@drawable/ic_github_circle"
            android:summary="@string/pref_source_summary"
            android:title="@string/pref_source_title" />

        <Preference
            android:icon="@drawable/ic_file_multiple"
            android:title="@string/pref_open_source_title" />

        <Preference
            android:icon="@drawable/ic_copyright"
            android:summary="@string/pref_license_summary"
            android:title="@string/pref_license_title" />

        <Preference
            android:icon="@drawable/ic_info_outline"
            android:summary="@string/pref_app_summary"
            android:title="@string/pref_app_title" />

    </PreferenceCategory>

</PreferenceScreen>
```

#### 2. Create preferences fragment.

Then we should create a simple blank fragment — `SettingsFragment`, which should extend `PreferenceFragment()`. This fragment will create preferences from the XML resource that we created. In the future this fragment will contain all the necessary methods to inflate the XML settings. It will also provide callbacks when the settings are changed.

```kotlin
class SettingsFragment : PreferenceFragment() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        addPreferencesFromResource(R.xml.pref_main);
    }
}
```

#### 3. Create preferences activity.

With the settings fragment ready let’s create new activity — `AppCompatPreferenceActivity`, which extends `PreferenceActivity()`. This class provides compatibility across all the devices and versions.

```kotlin
abstract class AppCompatPreferenceActivity : PreferenceActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        delegate.installViewFactory()
        delegate.onCreate(savedInstanceState)
        super.onCreate(savedInstanceState)
    }

    override fun onPostCreate(savedInstanceState: Bundle?) {
        super.onPostCreate(savedInstanceState)
        delegate.onPostCreate(savedInstanceState)
    }

    val supportActionBar: ActionBar?
        get() = delegate.supportActionBar

    fun setSupportActionBar(toolbar: Toolbar?) {
        delegate.setSupportActionBar(toolbar)
    }

    override fun getMenuInflater(): MenuInflater {
        return delegate.menuInflater
    }

    override fun setContentView(@LayoutRes layoutResID: Int) {
        delegate.setContentView(layoutResID)
    }

    override fun setContentView(view: View) {
        delegate.setContentView(view)
    }

    override fun setContentView(view: View, params: ViewGroup.LayoutParams) {
        delegate.setContentView(view, params)
    }

    override fun addContentView(view: View, params: ViewGroup.LayoutParams) {
        delegate.addContentView(view, params)
    }

    override fun onPostResume() {
        super.onPostResume()
        delegate.onPostResume()
    }

    override fun onTitleChanged(title: CharSequence, color: Int) {
        super.onTitleChanged(title, color)
        delegate.setTitle(title)
    }

    override fun onConfigurationChanged(newConfig: Configuration) {
        super.onConfigurationChanged(newConfig)
        delegate.onConfigurationChanged(newConfig)
    }

    override fun onStop() {
        super.onStop()
        delegate.onStop()
    }

    override fun onDestroy() {
        super.onDestroy()
        delegate.onDestroy()
    }

    override fun invalidateOptionsMenu() {
        delegate.invalidateOptionsMenu()
    }

    private val delegate: AppCompatDelegate by lazy {
        AppCompatDelegate.create(this, null)
    }
}
```

#### 4. Create settings activity.

```kotlin
class SettingsActivity : AppCompatPreferenceActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setupActionBar()

        fragmentManager.beginTransaction().replace(android.R.id.content, SettingsFragment()).commit()
    }

    private fun setupActionBar() {
        supportActionBar?.setDisplayHomeAsUpEnabled(true)
    }

    override fun onMenuItemSelected(featureId: Int, item: MenuItem): Boolean {
        val id = item.itemId
        if (id == android.R.id.home) {
            if (!super.onMenuItemSelected(featureId, item)) {
                NavUtils.navigateUpFromSameTask(this)
            }
            return true
        }
        return super.onMenuItemSelected(featureId, item)
    }
}
```

#### 5. Add settings item to main menu.

```xml
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    tools:context="com.baruckis.mycryptocoins.MainList.MainActivity">
    <item
        android:id="@+id/action_settings"
        android:orderInCategory="100"
        android:title="@string/action_settings"
        app:showAsAction="never" />
</menu>
```

#### 6. Launch newly created settings activity when the settings is selected from overflow menu.

```kotlin
class MainActivity : AppCompatActivity() {
    ...
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        return when (item.itemId) {
            R.id.action_settings -> {
                startActivity(Intent(this@MainActivity, SettingsActivity::class.java));
                return true
            }
            else -> super.onOptionsItemSelected(item)
        }
    }
}
```

#### 7. Specify newly created settings activity in Android manifest file.

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.baruckis.mycryptocoins">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        ...
        <activity
            android:name=".Settings.SettingsActivity"
            android:label="@string/title_activity_settings"
            android:parentActivityName=".MainList.MainActivity">
            <meta-data
                android:name="android.support.PARENT_ACTIVITY"
                android:value="com.baruckis.mycryptocoins.MainList.MainActivity" />
        </activity>
    </application>

</manifest>
```

Congratulations, you can finally launch the settings from the toolbar’s menu item.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IuIa3QSVU-XkIJhvvFHKWg.png)
_Settings screen_

### Using 3rd party libraries — Gmail style flip circle button-view

OK, there are various opinions about using 3rd party libraries — code created by a developer other than the original vendor of the development platform. Some people avoid them as it is never clear how long and how well they will be supported. Meanwhile others use them as they can accelerate the development process.

Your decision to use them should depend on your particular case. You should do your own investigation of the library and determine if it flexible enough to fit all your requirements.

For My Crypto Coins app, there is a situation where I would like to create a circle image view. This image should show a specific cryptocurrency icon inside a circle shape. But if the icon doesn’t exist, then I would like to show the first three letters of the cryptocurrency code.

Besides all that I would like to be able to select images by clicking them. Selection should be presented as a short flip view animation.

All this UX that I described was not originally invented by me. You can find similar behavior on the Gmail app and it looks really good.

![Image](https://cdn-media-1.freecodecamp.org/images/0*26bbM1htoeIKiGs9.gif)
_Gmail app flip circle view animation_

But how do we create it? In fact, circle image view is not even a default component which you can find in the Android Studio components palette.

You could go the hard way and try to create everything yourself, but this could waste time and energy. Instead, you could choose to implement one of the many open source libraries created particularly for that.

For my UI/UX requirement, I found a library on GitHub [davideas/FlipView](https://github.com/davideas/FlipView). After some investigation I decided that it was really professionally made. It is easy to implement and supported long enough to give it a try. So to start using it, we’ll follow these easy steps:

#### 1. Add dependency.

Import the library into your project.

```gradle
dependencies {
  implementation 'eu.davidea:flipview:1.1.3'
}
```

#### 2. Use it.

Configure FlipView with Android’s usual and custom app attributes. Isn’t that easy?

```xml
<android.support.v7.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    ...
        <eu.davidea.flipview.FlipView
            android:id="@+id/item_image_icon"
            style="@style/FlipView"
            android:clickable="true"
            android:focusable="true"
            app:layout_constraintBottom_toTopOf="@+id/item_ranking"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toTopOf="parent" />
    ...
</android.support.v7.widget.CardView>
```

So don’t reinvent the wheel. Always consider using some library first to deliver results faster. And if you project becomes messy, it’s not the old libraries to blame but how well you structure your code. If your project is modular enough there won’t be problems. But that’s a separate topic and I am going to talk about project architecture in later blog posts.

![Image](https://cdn-media-1.freecodecamp.org/images/0*x4Nx1fwI4iwck8-c.gif)
_Flip View used inside main screen list_

### Localization with RTL support

When I decided to create this app, I set myself a goal not only to create it with a default English UI, but also to translate it to my mother tongue, Lithuanian, from the start of development.

This goal lead me to learn about localization in Android. What I have found is that to add support for multiple languages is very easy. As I mentioned before, first you need to separate all your strings to the strings.xml file. Then you can launch the Translations Editor tool inside Android Studio. This will allow you to add new languages support.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n2hzxAC2dDSMnqlyF4VHCw.png)

You will see that the interface is very intuitive. Now you need to translate each string from your strings.xml file to a new language. A new file will be generated by the IDE in separate directory. For example, for Lithuanian language, it’s `values-lt/strings.xml`. That’s it! ?

If you switch your Android device system language to the one you just translated to and then run your app, all the UI will be automatically updated to your translations. Moreover, for My Crypto Coins app, later I plan to add the ability to switch languages at run-time. That’s why you will notice the language switcher inside the settings screen.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wa3BEirdnfg21PB-IRwYXA.png)
_Settings screen — language Lithuanian_

Translating your app to different languages will definitely widen your audience. Why not go further by adding support for a few special languages that are written from Right to Left (RTL) — like Arabic, Hebrew or Persian.

![Image](https://cdn-media-1.freecodecamp.org/images/1*COi5U81UK015BfLSsoQtPg.png)

Actually to add RTL support is not difficult at all. Just add the support attribute to your manifest file:

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.baruckis.mycryptocoins">

    <application
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">
        ...
    </application>

</manifest>
```

Congratulations, your app now supports RTL. However you can’t trust blindly that everything will work correctly straightaway. You should check how well it is supported yourself. To do that select one of the RTL languages as your primary device language.

A few tips for RTL:

* In all your layouts you will need to replace all `Left` and `Right` layout properties with `Start` and `End` equivalent. For example `android:paddingLeft` should be replaced with `android:paddingStart`.
* If you don’t have a special drawable for RTL, perhaps you would like to mirror your current ones with a special `autoMirrored` attribute.

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:autoMirrored="true"
    android:tint="@color/colorForPreferenceIcon"
    android:viewportHeight="24.0"
    android:viewportWidth="24.0">
    <path
        android:fillColor="#FF000000"
        android:pathData="M1.5,4V5.5C1.5,9.65 3.71,13.28 7,15.3V20H22V18C22,15.34 16.67,14 14,14C14,14 13.83,14 13.75,14C9,14 5,10 5,5.5V4M14,4A4,4 0 0,0 10,8A4,4 0 0,0 14,12A4,4 0 0,0 18,8A4,4 0 0,0 14,4Z" />
</vector>
```

* If there are certain places where you need to have LTR instead of RTL, you can do that too. For example to force any layout to LTR just add `android:layoutDirection="ltr"` to that view. If you need to force text direction inside text view than use `android:textDirection="ltr"`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V-zeS7WGF8Af0sua5MyhuA.png)

By the way, when using Translations Editor, there is a very useful feature to order a professional translation service. Even if I personally don’t know anything about the Hebrew language, I still set myself a goal to add support for it as an example RTL language for My Crypto Coins project. So this feature seemed like a really good idea to try. I ordered the translation successfully from English to Hebrew directly from the IDE with just a few clicks.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1or1qQdqMBR-crfmkGe3Wg.png)
_Order a translation service_

### Final thoughts

In this second part of the series, we created all the UI layouts with some initial code based on detailed mockups. I did not want to go into too much detail on each topic so as not to confuse you. My goal was to show you how to see a bigger picture, how to focus on small details first, and avoid costly mistakes later.

If you find something not covered well enough, use it as a jumping off point to do your own research. There are always plenty of good resources around the web to learn from. ?

### Repository

You can find all the XML layouts and code created for this part here:

#### [View Source On GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-2)



---

**_Ačiū! Thanks for reading! I originally published this post for my personal blog [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-2/) on May 14, 2018._**

