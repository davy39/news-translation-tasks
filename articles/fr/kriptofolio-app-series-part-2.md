---
title: 'Comment commencer à construire votre application Android : création de maquettes,
  d''UI et de mises en page XML'
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
seo_title: 'Comment commencer à construire votre application Android : création de
  maquettes, d''UI et de mises en page XML'
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 2

  So how do you actually start to build a new app? What should be your first move?
  If you think we just need to launch Android Studio and jump directly to the code,
  think again. That’s exactly the thi...'
---

Par Andrius Baruckis

#### Série d'applications Kriptofolio - Partie 2

Alors, comment commencez-vous réellement à construire une nouvelle application ? Quel devrait être votre premier geste ? Si vous pensez que nous devons simplement lancer Android Studio et sauter directement dans le code, réfléchissez à nouveau. C'est exactement ce que je vous conseillerais de ne pas faire, car cela peut faire plus de mal que de bien. Mais il est si tentant de commencer à écrire vos premières lignes de code dès que possible.

Au lieu de cela, je suggérerais de se concentrer sur l'élaboration d'un plan judicieux avec des maquettes d'UI. N'oubliez pas que chaque bon nouveau projet d'application devrait commencer par cela. Avec cette approche, vous ne perdrez pas beaucoup de temps et serez en mesure de construire des produits de haute qualité dès le début.

Ainsi, dans cette partie de la série, je vais présenter l'application « Kriptofolio » (anciennement « My Crypto Coins ») et discuter de la manière de créer des maquettes. Nous allons également construire toutes les mises en page de l'UI. Ces mises en page deviendront notre fondation solide indiquant clairement ce qu'il faut coder. Enfin, nous allons localiser notre application dans différentes langues et apprendre à gérer celles qui sont écrites de droite à gauche.

### Contenu de la série

* [Introduction : Une feuille de route pour construire une application Android moderne en 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* [Partie 1 : Une introduction aux principes SOLID](https://www.freecodecamp.org/news/kriptofolio-app-series-part-1)
* Partie 2 : Comment commencer à construire votre application Android : création de maquettes, d'UI et de mises en page XML (vous êtes ici)
* [Partie 3 : Tout sur cette architecture : exploration de différents modèles d'architecture et comment les utiliser dans votre application](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* [Partie 4 : Comment implémenter l'injection de dépendances dans votre application avec Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* [Partie 5 : Gérer les services Web RESTful en utilisant Retrofit, OkHttp, Gson, Glide et Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### Maquettes

Il existe diverses façons de créer des maquettes pour votre projet. La plus simple consiste à prendre un crayon et une feuille de papier et à commencer à dessiner dessus. Le meilleur aspect est que cette méthode ne vous coûte rien et vous pouvez commencer immédiatement. Oh, et j'ai presque oublié, vous devriez également vous procurer une gomme car il n'y aura pas de fonction annuler. ?

Si vous, comme moi, sentez que vous avez besoin de plus de fonctionnalités, envisagez alors d'utiliser un logiciel spécial pour créer des maquettes détaillées. Je préfère utiliser un logiciel plutôt que le crayon et le papier, même si cela nécessite d'investir de l'argent pour l'acheter et du temps pour apprendre à l'utiliser.

Il existe diverses options logicielles sur le marché parmi lesquelles choisir. Vous devrez faire votre propre enquête pour déterminer celle qui répond le mieux à tous vos besoins. Pour toutes les maquettes de mes projets actuellement, j'utilise [Balsamiq](https://balsamiq.com/) Mockups pour l'application de bureau. Balsamiq est un logiciel de wireframing rapide, efficace et très facile à utiliser. Comme je suis plutôt satisfait, je le recommande pour créer des applications Android, alors n'hésitez pas à l'essayer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*G5TA06Hy-zj-uaxxcb1zyw.jpeg)

J'ai commencé le projet d'application My Crypto Coins en créant des maquettes bien réfléchies et très détaillées. Je me suis dit que si je créais tout de manière très détaillée, j'éviterais les erreurs. Je ne gaspillerais également pas de temps à changer soudainement la fonctionnalité pendant le processus de développement. Si vous mettez beaucoup d'efforts dans la création de bonnes maquettes, alors, avec un peu d'imagination, vous pouvez voir et ressentir le produit final.

Mon objectif était d'avoir tout défini dans les maquettes comme cela devrait apparaître dans le produit final. Pour cela, j'ai essayé de ne pas me précipiter mais de passer autant de temps que nécessaire. Voici mes maquettes finales pour l'application My Crypto Coins :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ciWyOJ2Lftb7hiXLNYNl9Q.png)
_Maquette de l'application My Crypto Coins réalisée avec le logiciel Balsamiq Mockups_

### Design standard — Material

Une autre chose importante à aborder est le design visuel de l'application. Au moment de la rédaction de cet article, [Material Design](https://en.wikipedia.org/wiki/Material_Design) est le design visuel standard recommandé par Google pour toutes les applications Android. Et devinez quoi — vous ne pouvez pas vous tromper avec le design standard.

Pour l'application My Crypto Coins, nous allons utiliser Material Design. L'application suit les meilleures pratiques définies dans les directives en ligne détaillées.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0kyrt1pJA8XaUSKE9j1INg.jpeg)

[Material.io/guidelines](https://material.io/guidelines) — document officiel des spécifications vivantes du material design qui sera nos directives de conception pour ce projet.

### Mises en page

Maintenant que nous avons déjà préparé les wireframes de notre application, il est temps de construire une véritable UI. Encore une fois, nous pourrions nous lancer dans l'écriture de code, mais pourquoi se précipiter ? Au lieu de cela, je recommanderais de se concentrer sur la construction de toutes vos mises en page XML. Mon conseil ici serait que plus vous arrivez à mettre dans XML, moins vous aurez de code à écrire.

L'équipe Android améliore constamment la manière dont vous pouvez construire votre UI en ajoutant de nouvelles fonctionnalités aux mises en page XML. Parfois, il est si tentant d'écrire quelques lignes de code pour obtenir l'apparence souhaitée. Mais il est préférable d'approfondir le sujet pour trouver s'il est possible de le faire sans code. Rappelez-vous : moins de code rend votre projet plus propre. Il sera également plus compréhensible pour les autres développeurs et plus facile à maintenir.

Enfin, lorsque vous avez créé toutes vos mises en page XML, vous aurez l'impression d'avoir votre application terminée. Vous pourrez la lancer et voir comment elle se comporte pour l'utilisateur final. Peu importe qu'elle affiche des données factices et ne fasse rien. Maintenant, vous avez une dernière chance d'apporter des changements drastiques.

Si vous construisez une application pour quelqu'un d'autre, c'est le moment idéal pour la présenter. Peut-être qu'on vous demandera d'apporter des changements surprenants de dernière minute. Ainsi, vous éviterez d'écrire du code pour une fonctionnalité qui ne sera jamais utilisée. Beaucoup de gens n'ont pas assez d'imagination et ils doivent voir et toucher d'abord pour décider si c'est ce qu'ils veulent. Alors ne laissez pas vos mises en page pour la dernière étape de votre processus de travail.

Pour cette application, j'utiliserai divers composants courants dans toutes les applications Android modernes :

* [CoordinatorLayout](https://developer.android.com/reference/android/support/design/widget/CoordinatorLayout) — un FrameLayout super-puissant, dont l'attrait principal est sa capacité à coordonner les animations et les transitions des vues qu'il contient.
* [AppBarLayout](https://developer.android.com/reference/android/support/design/widget/AppBarLayout) — un LinearLayout vertical qui implémente de nombreuses fonctionnalités du concept de barre d'application du material design, notamment les gestes de défilement.
* [Toolbar](https://developer.android.com/reference/android/support/v7/widget/Toolbar) — une généralisation des barres d'action pour une utilisation dans les mises en page d'application.
* [CollapsingToolbarLayout](https://developer.android.com/reference/android/support/design/widget/CollapsingToolbarLayout) — un wrapper pour Toolbar qui implémente une barre d'application repliable. Il est conçu pour être utilisé comme enfant direct d'un AppBarLayout.
* [ConstraintLayout](https://developer.android.com/reference/android/support/constraint/ConstraintLayout) — un ViewGroup qui vous permet de positionner et de dimensionner les widgets de manière flexible. Imaginez un RelativeLayout sur stéroïdes.
* [SwipeRefreshLayout](https://developer.android.com/reference/android/support/v4/widget/SwipeRefreshLayout) — le widget qui permet de mettre en œuvre entièrement le modèle d'interface utilisateur de balayage pour actualiser. Il détecte le balayage vertical, affiche une barre de progression distinctive et déclenche des méthodes de rappel dans votre application.
* [FloatingActionButton](https://developer.android.com/reference/android/support/design/widget/FloatingActionButton) — un bouton circulaire qui déclenche l'action principale dans l'UI de votre application.

Pour l'écran principal, nous utiliserons une combinaison de tous ces composants pour créer une belle UI/UX. Les utilisateurs peuvent développer et réduire la partie supérieure de la mise en page pour trouver la valeur totale de leur portefeuille de cryptomonnaies. Ils peuvent vérifier tout changement de valeur au cours des dernières 24 heures et changer la devise fiduciaire sélectionnée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j3GzRC56EjaWxMvhE8O2cQ.png)
_Création de la mise en page de l'écran principal_

Bien sûr, il existe d'autres composants en plus de ces neuf. Il est très important de maîtriser toute la palette de composants pour savoir lequel utiliser dans chaque cas particulier. Avec les tendances mobiles changeant de temps en temps, la palette s'étendra également.

Je ne vais pas parler de chaque composant, mais mon conseil est de les étudier par vous-même. Pour moi, la meilleure façon de les comprendre est d'essayer de construire des mises en page XML manuellement au lieu d'utiliser les outils de glisser-déposer automatiques dans Android Studio.

### Styles, Couleurs, Dimensions, Chaînes, Icônes

À première vue, les éléments mentionnés dans le titre de cette section peuvent sembler ne pas être importants. Cependant, je vous demande de faire un effort lorsque vous les créez dans une application si vous voulez la rendre moderne et exclusive. Rappelez-vous que cette série de blogues est sur la construction d'une application Android MODERNE ! Peu importe à quel point c'est faux, les gens jugeront généralement votre application par son apparence d'abord, et non par sa fonctionnalité.

Alors voici une chance parfaite de gagner l'amour des nouveaux utilisateurs dès le début. Voici mes conseils :

* Lorsque vous construisez vos fichiers de mise en page XML, vous devriez reconnaître où vous répétez certains attributs communs pour les vues. Déplacez-les pour les définir comme des styles XML séparés. Ainsi, vous aurez des fichiers de mise en page XML plus courts. Vous pouvez contrôler tous les aspects du style de l'application à partir d'un endroit séparé. Imaginez les avantages que cela vous apportera. Par exemple, vous pourriez permettre à l'utilisateur de choisir le thème de l'application (clair, sombre, etc.).
* Définissez toutes les couleurs de votre application dans un fichier séparé également, et profitez de la capacité à expérimenter avec l'apparence en les changeant immédiatement. Parfois, le même produit peut être redonné une nouvelle vie et engager à nouveau les utilisateurs en se rafraîchissant simplement avec de nouvelles couleurs. Il existe quelques sites web qui peuvent vous aider à choisir de belles couleurs, mais mon préféré est [MaterialPalette.com](https://www.materialpalette.com/), alors jetez un coup d'œil.
* Définissez les dimensions de votre application dans un fichier séparé. Cela vous permettra d'ajuster votre application pour qu'elle ait une belle apparence sur des écrans de différentes tailles.
* Toutes vos chaînes ne doivent pas être codées en dur, et Android Studio vous informera si vous oubliez. Ne l'ignorez pas. Le meilleur aspect lorsque vos chaînes sont séparées est que vous pouvez traduire votre application dans différentes langues.
* Lorsque vous utilisez des icônes pour votre application, préférez toujours le format de dessin vectoriel XML. C'est le nouveau standard recommandé et une manière intelligente de procéder pour éviter toute pixelisation. Pour trouver de nombreuses icônes de style material design faites professionnellement par la communauté, veuillez consulter [MaterialDesignIcons.com](https://materialdesignicons.com/). J'ai utilisé ce site web pour obtenir des icônes pour l'application My Crypto Coins.

### RecyclerView

L'écran principal de l'application My Crypto Coins sera constitué d'une liste de cryptomonnaies que l'utilisateur possède. À cette fin, le widget RecyclerView est le plus adapté. C'est un widget qui affiche une liste déroulante d'éléments basée sur de grands ensembles de données (ou des données qui changent fréquemment).

En raison de ses avantages, RecyclerView est le composant recommandé pour créer tout écran de liste. C'est une version plus avancée et flexible du composant ListView plus simple. Nous en parlerons également plus tard. Dans cette partie, nous créons simplement des mises en page. Nous ne nous concentrons pas sur le codage.

Pour voir notre application visuellement, nous devrons implémenter RecyclerView en écrivant un peu de code. Voici les étapes pour implémenter RecyclerView :

#### 1. Ajouter un composant RecyclerView.

Notre mise en page `MainActivity` est `activity_main.xml`. Cette mise en page inclut la mise en page `content_main.xml` qui est un fragment. Cette mise en page `MainActivityListFragment` gonfle `fragment_main_list.xml`. Vous devez donc ajouter le composant RecyclerView ici.

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

Comme vous le voyez, nous configurons notre RecyclerView pour laisser un peu d'espace de remplissage en bas. Nous faisons cela pour éviter de couvrir le dernier élément de la liste avec le FloatingActionButton. Nous activons également la barre de défilement verticale pour qu'elle soit disponible.

#### 2. Créer la mise en page des lignes de RecyclerView.

Pour notre objectif initial, nous allons simplement définir le nom de l'élément pour chaque ligne. Notre mise en page simplifiée devrait ressembler à ceci.

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

#### 3. Créer une classe d'adaptateur de données.

Notre adaptateur pour l'instant acceptera des données de type chaîne. Plus tard, nous devrons créer une classe de modèle de données séparée. Nous devrons passer plus d'informations qu'une seule chaîne.

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

#### 4. Connecter RecyclerView à l'adaptateur personnalisé.

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

Terminé ! Maintenant, notre écran principal ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1WVQXLqwxuXb910bQcc54Q.png)
_Écran principal_

### ListView

Dans ce projet, nous allons utiliser ListView pour l'écran où vous pouvez ajouter des cryptomonnaies que vous possédez déjà. En raison de ses lacunes ces dernières années, il est à peine utilisé.

Je suppose donc que beaucoup d'entre vous se demandent pourquoi j'ai décidé de l'utiliser dans l'application My Crypto Coins alors que nous aurions pu créer la même fonctionnalité facilement avec RecyclerView.

N'oubliez pas, cependant, que ce projet a été créé à des fins de formation en premier lieu. J'ai pensé qu'il serait bénéfique de comprendre ListView et son fonctionnement. Tout développeur peut rencontrer ListView dans du code hérité, et il est préférable de savoir comment travailler avec. De plus, la liste que nous allons créer est si simple que les limitations techniques de ListView ne nous poseront aucun problème.

Suivons les étapes très similaires nécessaires pour implémenter ListView :

#### 1. Ajouter un composant ListView.

La première chose à faire est d'ajouter un ListView à `AddSearchActivity`. Ouvrez le fichier de mise en page de l'activité `activity_add_search.xml` et vous verrez qu'il inclut `content_add_search.xml`. C'est là que nous ajouterons le composant ListView.

```xml
...
<ListView
    android:id="@+id/listview_activity_add_search"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:scrollbars="vertical" />
...
```

#### 2. Créer la mise en page des lignes de ListView.

Comme précédemment, juste pour des besoins initiaux, nous allons simplement définir le nom de l'élément pour chaque ligne. Voici la mise en page simplifiée :

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

#### 3. Créer une classe d'adaptateur de données.

Comme pour RecyclerView, notre adaptateur ListView acceptera pour l'instant uniquement des données de type chaîne pour obtenir le nom de l'élément et l'afficher à l'écran. Plus tard, nous utiliserons un modèle de données de classe séparé. Pour cette partie, nous voulons construire une liste très simple affichant uniquement les titres des cryptomonnaies. Au lieu de créer notre propre adaptateur, nous pourrions utiliser celui par défaut, ArrayAdapter.

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

Comme vous le voyez dans le code de l'adaptateur, en créant l'objet `CustomViewHolder`, j'utilise le modèle ViewHolder. Il stocke les références des vues des lignes de la liste. L'appel de la méthode `findViewById()` ne se produit que quelques fois. Cela nous permet de rendre le défilement de notre liste fluide et efficace.

ListView ne nous oblige pas à utiliser le modèle ViewHolder. L'adaptateur de RecyclerView nous offre ce type de protection par défaut, car il nous force à l'utiliser.

#### 4. Connecter ListView à l'adaptateur personnalisé.

Avec l'ArrayAdapter par défaut, cela pourrait ressembler à `val adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, data)`. C'est la beauté du composant ListView. Si vous le souhaitez, vous pouvez créer une liste simple très rapidement sans construire votre propre adaptateur ou mise en page de ligne (sautez les étapes 2 et 3).

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

La configuration de ListView est prête !

![Image](https://cdn-media-1.freecodecamp.org/images/1*6lpfmyzidzGQju_YmPHekQ.png)
_Écran d'ajout de cryptomonnaie(s)_

### SearchView

Dans le même écran où toutes les cryptomonnaies sont listées, nous devons également ajouter SearchView. La recherche sera une fonctionnalité utile pour tout utilisateur qui souhaite trouver une cryptomonnaie spécifique en tapant son nom. Pour cette partie, nous ne construirons pas entièrement la fonctionnalité, mais nous implémenterons simplement sa partie visuelle. Suivez ces étapes pour ajouter SearchView au projet :

#### 1. Déclarer la configuration de recherche en XML.

Le fichier de configuration de recherche doit être ajouté dans votre répertoire res nommé xml. Ici, vous pouvez spécifier les attributs de votre composant SearchView qui définissent son comportement.

```xml
<searchable
    xmlns:android="http://schemas.android.com/apk/res/android"
    android:label="@string/app_name"
    android:hint="@string/search_hint">
</searchable>
```

#### 2. Créer une nouvelle activité qui deviendra notre activité de recherche.

Nous allons créer une nouvelle activité vide qui étend `AppCompatActivity()`. Nous la nommerons `AddSearchActivity`.

#### 3. Spécifier la nouvelle activité créée dans le fichier manifest Android pour qu'elle soit recherchable.

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

Nous allons laisser le système Android gérer le processus de recherche. C'est pourquoi nous ajoutons l'action de recherche d'intention et les métadonnées dans l'élément d'activité de `AddSearchActivity`. Les métadonnées ont un nom et une ressource qui est liée au fichier de configuration de recherche situé dans le dossier res/xml.

#### 4. Créer un menu de recherche.

Dans le dossier res/menu, nous allons créer un fichier de ressource de menu.

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

#### 5. Ajouter le menu de recherche à l'activité.

Nous allons ajouter le widget de recherche Android comme vue d'action de menu.

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

Maintenant, SearchView est ajouté à l'activité. Cependant, la fonctionnalité de recherche ne fonctionne pas encore. Mais nous l'avons implémentée comme nous le voulions pour cette partie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H04EuFhD3r1vrIHSD_tbJg.png)
_Écran d'ajout de cryptomonnaie(s) — fonctionnalité de recherche_

### Paramètres

Si vous souhaitez créer une application Android moderne, je vous recommande d'inclure un écran de paramètres et de donner accès aux paramètres de l'application pour l'utilisateur. Inclure des paramètres dans votre application donne à vos utilisateurs le pouvoir de contrôler certaines fonctionnalités de votre application, ce qui les rend plus heureux. Ils sont maintenant en contrôle du comportement de l'application. Nous allons donc créer un écran de paramètres pour l'application My Crypto Coins également.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m6NnpRpwZnrsAeKW6rybqA.png)
_Nouvelle activité de paramètres à partir du modèle de galerie_

Vous pouvez créer un écran de paramètres avec le modèle Android Studio et il générera tout le code dont vous avez besoin. Par défaut, au moment de la rédaction de cet article, l'activité de paramètres est générée avec des en-têtes de préférence. Ce n'est pas ce que nous voulons pour une si petite application où nous prévoyons d'avoir seulement quelques paramètres au début.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Kdlb-ZQKonUu-9xeTe0Nbw.png)
_Modèle de paramètres par défaut avec des en-têtes de préférence_

Par conséquent, nous allons tout construire manuellement. L'écran de paramètres est conçu avec une mise en page de type XML. Allons étape par étape pour créer à nouveau uniquement la partie visuelle pour cet article de blog :

#### 1. Créer un fichier XML d'écran de préférences.

Nous allons créer le fichier XML de l'écran de préférences qui doit être placé dans le répertoire res/xml.

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

#### 2. Créer un fragment de préférences.

Ensuite, nous devons créer un fragment vide simple — `SettingsFragment`, qui doit étendre `PreferenceFragment()`. Ce fragment créera des préférences à partir de la ressource XML que nous avons créée. À l'avenir, ce fragment contiendra toutes les méthodes nécessaires pour gonfler les paramètres XML. Il fournira également des rappels lorsque les paramètres seront modifiés.

```kotlin
class SettingsFragment : PreferenceFragment() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        addPreferencesFromResource(R.xml.pref_main);
    }
}
```

#### 3. Créer une activité de préférences.

Avec le fragment de paramètres prêt, créons une nouvelle activité — `AppCompatPreferenceActivity`, qui étend `PreferenceActivity()`. Cette classe fournit une compatibilité sur tous les appareils et versions.

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

#### 4. Créer une activité de paramètres.

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

#### 5. Ajouter un élément de paramètres au menu principal.

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

#### 6. Lancer la nouvelle activité de paramètres lorsque les paramètres sont sélectionnés dans le menu de débordement.

```kotlin
class MainActivity : AppCompatActivity() {
    ...
    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Gonfler le menu ; cela ajoute des éléments à la barre d'action si elle est présente.
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

#### 7. Spécifier la nouvelle activité de paramètres créée dans le fichier manifest Android.

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

Félicitations, vous pouvez enfin lancer les paramètres à partir de l'élément de menu de la barre d'outils.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IuIa3QSVU-XkIJhvvFHKWg.png)
_Écran des paramètres_

### Utilisation de bibliothèques tierces — Bouton-vue circulaire à bascule style Gmail

D'accord, il existe diverses opinions sur l'utilisation de bibliothèques tierces — du code créé par un développeur autre que le fournisseur original de la plateforme de développement. Certaines personnes les évitent car il n'est jamais clair combien de temps et combien bien elles seront supportées. Pendant ce temps, d'autres les utilisent car elles peuvent accélérer le processus de développement.

Votre décision de les utiliser devrait dépendre de votre cas particulier. Vous devriez faire votre propre investigation sur la bibliothèque et déterminer si elle est suffisamment flexible pour répondre à toutes vos exigences.

Pour l'application My Crypto Coins, il y a une situation où j'aimerais créer une vue d'image circulaire. Cette image devrait montrer une icône de cryptomonnaie spécifique à l'intérieur d'une forme circulaire. Mais si l'icône n'existe pas, alors j'aimerais montrer les trois premières lettres du code de la cryptomonnaie.

En plus de tout cela, j'aimerais pouvoir sélectionner des images en cliquant dessus. La sélection devrait être présentée comme une courte animation de vue de bascule.

Tout ce UX que j'ai décrit n'a pas été inventé par moi. Vous pouvez trouver un comportement similaire sur l'application Gmail et cela a l'air vraiment bien.

![Image](https://cdn-media-1.freecodecamp.org/images/0*26bbM1htoeIKiGs9.gif)
_Animation de vue circulaire à bascule de l'application Gmail_

Mais comment la créer ? En fait, la vue d'image circulaire n'est même pas un composant par défaut que vous pouvez trouver dans la palette de composants d'Android Studio.

Vous pourriez prendre le chemin difficile et essayer de tout créer vous-même, mais cela pourrait gaspiller du temps et de l'énergie. Au lieu de cela, vous pourriez choisir d'implémenter l'une des nombreuses bibliothèques open source créées particulièrement pour cela.

Pour mon exigence UI/UX, j'ai trouvé une bibliothèque sur GitHub [davideas/FlipView](https://github.com/davideas/FlipView). Après une certaine investigation, j'ai décidé qu'elle était vraiment faite professionnellement. Elle est facile à implémenter et supportée depuis suffisamment longtemps pour lui donner une chance. Alors pour commencer à l'utiliser, nous allons suivre ces étapes faciles :

#### 1. Ajouter une dépendance.

Importez la bibliothèque dans votre projet.

```gradle
dependencies {
  implementation 'eu.davidea:flipview:1.1.3'
}
```

#### 2. L'utiliser.

Configurez FlipView avec les attributs habituels d'Android et les attributs personnalisés de l'application. N'est-ce pas facile ?

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

Alors ne réinventez pas la roue. Envisagez toujours d'utiliser une bibliothèque d'abord pour livrer des résultats plus rapidement. Et si votre projet devient désordonné, ce ne sont pas les anciennes bibliothèques à blâmer, mais la façon dont vous structurez votre code. Si votre projet est suffisamment modulaire, il n'y aura pas de problèmes. Mais c'est un sujet séparé et je vais parler de l'architecture du projet dans les prochains articles de blog.

![Image](https://cdn-media-1.freecodecamp.org/images/0*x4Nx1fwI4iwck8-c.gif)
_Vue Flip utilisée dans la liste de l'écran principal_

### Localisation avec support RTL

Lorsque j'ai décidé de créer cette application, je me suis fixé un objectif non seulement de la créer avec une UI par défaut en anglais, mais aussi de la traduire dans ma langue maternelle, le lituanien, dès le début du développement.

Cet objectif m'a conduit à apprendre la localisation dans Android. Ce que j'ai découvert, c'est que l'ajout de la prise en charge de plusieurs langues est très facile. Comme je l'ai mentionné précédemment, vous devez d'abord séparer toutes vos chaînes dans le fichier strings.xml. Ensuite, vous pouvez lancer l'outil Translations Editor à l'intérieur d'Android Studio. Cela vous permettra d'ajouter la prise en charge de nouvelles langues.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n2hzxAC2dDSMnqlyF4VHCw.png)

Vous verrez que l'interface est très intuitive. Maintenant, vous devez traduire chaque chaîne de votre fichier strings.xml dans une nouvelle langue. Un nouveau fichier sera généré par l'IDE dans un répertoire séparé. Par exemple, pour la langue lituanienne, c'est `values-lt/strings.xml`. C'est tout ! ?

Si vous changez la langue du système de votre appareil Android pour celle que vous venez de traduire, puis exécutez votre application, toute l'UI sera automatiquement mise à jour avec vos traductions. De plus, pour l'application My Crypto Coins, je prévois d'ajouter plus tard la possibilité de changer de langue à l'exécution. C'est pourquoi vous remarquerez le sélecteur de langue à l'intérieur de l'écran des paramètres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Wa3BEirdnfg21PB-IRwYXA.png)
_Écran des paramètres — langue lituanienne_

Traduire votre application dans différentes langues élargira définitivement votre audience. Pourquoi ne pas aller plus loin en ajoutant la prise en charge de quelques langues spéciales qui sont écrites de droite à gauche (RTL) — comme l'arabe, l'hébreu ou le persan.

![Image](https://cdn-media-1.freecodecamp.org/images/1*COi5U81UK015BfLSsoQtPg.png)

En fait, ajouter la prise en charge RTL n'est pas difficile du tout. Il suffit d'ajouter l'attribut de prise en charge à votre fichier manifest :

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

Félicitations, votre application prend maintenant en charge RTL. Cependant, vous ne pouvez pas faire confiance aveuglément au fait que tout fonctionnera correctement immédiatement. Vous devez vérifier vous-même à quel point elle est bien supportée. Pour cela, sélectionnez l'une des langues RTL comme langue principale de votre appareil.

Quelques conseils pour RTL :

* Dans toutes vos mises en page, vous devrez remplacer toutes les propriétés de mise en page `Left` et `Right` par les équivalents `Start` et `End`. Par exemple, `android:paddingLeft` doit être remplacé par `android:paddingStart`.
* Si vous n'avez pas de dessin spécial pour RTL, peut-être aimeriez-vous miroir vos dessins actuels avec un attribut spécial `autoMirrored`.

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

* Si vous avez certains endroits où vous devez avoir LTR au lieu de RTL, vous pouvez le faire aussi. Par exemple, pour forcer une mise en page à LTR, ajoutez simplement `android:layoutDirection="ltr"` à cette vue. Si vous devez forcer la direction du texte à l'intérieur d'une vue de texte, utilisez `android:textDirection="ltr"`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V-zeS7WGF8Af0sua5MyhuA.png)

D'ailleurs, lors de l'utilisation de l'éditeur de traductions, il y a une fonction très utile pour commander un service de traduction professionnel. Même si je ne connais personnellement rien à la langue hébraïque, je me suis tout de même fixé pour objectif d'ajouter la prise en charge de celle-ci en tant qu'exemple de langue RTL pour le projet My Crypto Coins. Cette fonction semblait donc être une très bonne idée à essayer. J'ai commandé la traduction avec succès de l'anglais vers l'hébreu directement depuis l'IDE avec seulement quelques clics.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1or1qQdqMBR-crfmkGe3Wg.png)
_Commander un service de traduction_

### Réflexions finales

Dans cette deuxième partie de la série, nous avons créé toutes les mises en page de l'UI avec un peu de code initial basé sur des maquettes détaillées. Je ne voulais pas entrer dans trop de détails sur chaque sujet afin de ne pas vous confondre. Mon objectif était de vous montrer comment voir une image plus grande, comment se concentrer sur les petits détails d'abord et éviter des erreurs coûteuses plus tard.

Si vous trouvez quelque chose qui n'est pas suffisamment couvert, utilisez-le comme point de départ pour faire vos propres recherches. Il y a toujours beaucoup de bonnes ressources sur le web pour apprendre. ?

### Dépôt

Vous pouvez trouver toutes les mises en page XML et le code créés pour cette partie ici :

#### [Voir la source sur GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-2)



---

**_Ačiū ! Merci d'avoir lu ! J'ai initialement publié cet article pour mon blog personnel [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-2/) le 14 mai 2018._**