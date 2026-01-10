---
title: Comment créer un composant de navigation Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2020-05-04T22:10:00.000Z'
originalURL: https://freecodecamp.org/news/android-navigation-component
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b43740569d1a4ca2ac3.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Java
  slug: java
seo_title: Comment créer un composant de navigation Android
seo_desc: 'Designing an application tends to be cumbersome and more often than not,
  there is a whiteboard with arrows pointing from various points to others.

  What you initially thought would be an application with one or two activities, suddenly
  appears to have...'
---

Concevoir une application a tendance à être fastidieux et, le plus souvent, on se retrouve devant un tableau blanc avec des flèches pointant de divers points vers d'autres.

Ce que vous pensiez initialement être une application avec une ou deux activités semble soudainement comporter plusieurs flux, des fragments et une large gamme d'interactions utilisateur. Ne serait-il pas agréable de pouvoir prendre ce qui se trouve sur ce tableau blanc et de le reproduire facilement dans le code ?

Dites bonjour au [Navigation Component](https://www.youtube.com/watch?v=Y0Cs2MQxyIs).

Pour ceux qui ne le connaissent pas, le Navigation Component n'est pas une autre classe d'interface utilisateur que l'on place à la place d'une mise en page pour votre activité/fragment. Considérez-le comme une carte où, au lieu de continents, vous avez vos fragments, et vous aurez besoin de **_directions_** (orientations) pour aller de continent en continent. Il présente vos fragments et les connexions entre eux de manière descendante. Dans cet article, nous passerons en revue les principaux aspects de ce composant et apprendrons comment l'intégrer dans nos applications.

Prêt à mettre les voiles ? ⛵

## Apprendre les bases

Le composant Navigation est disponible à partir d'Android Studio 3.3 et versions ultérieures. Pour l'utiliser, ajoutez les dépendances suivantes à votre projet :

```gradle
android {
    ...
}

dependencies {
    implementation 'androidx.navigation:navigation-fragment-ktx:2.0.0'
    implementation 'androidx.navigation:navigation-ui-ktx:2.0.0'
}
```

Afin d'avoir une base de travail, imaginons que nous ayons conçu une application avec la structure suivante :

* Start Fragment
* Fragment A
* Fragment B

L'utilisateur peut soit aller au Fragment A, soit au Fragment B depuis le fragment Start.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_HUnrog-RHe4bjhboo_24ig.png)
_Notre application_

Si nous voulons faire tout cela sans le Navigation Component, nous devrions ajouter le code trop familier d'ouverture d'un fragment lorsqu'un des boutons est cliqué.

```kt
val myFragment : MyFragment = MyFragment()
supportFragmentManager.beginTransaction().add(R.id.container, myFragment).commit()
```

Dans notre petit exemple, cela représente quelques lignes courtes et est plutôt simple, mais je pense que nous pouvons tous convenir que cela ne passerait pas à l'échelle de manière appropriée si notre application était plus grande et présentait des flux d'utilisateurs plus complexes.

## Tous à bord

Pour commencer à utiliser le Navigation Component, nous devons créer un graphe de navigation. Ce graphe servira de carte, décrivant le flux utilisateur dans notre application. Pour en créer un, faites un clic droit sur le dossier res et créez un nouveau fichier de ressources. Nous nommerons le nôtre : **_user_flow_graph.xml_**. Assurez-vous de définir le type du fichier comme Navigation.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_yQ207tKoQqFMH55h5axE7Q.png)
_Création d'un nouveau fichier de ressources_

Chaque voyage commence à partir d'une base et le nôtre n'est pas différent. Notre base s'appelle un **_NavHost_**. Il servira d'espace réservé pour les destinations à interchanger lorsqu'un utilisateur interagit avec notre interface utilisateur. Nous devons ajouter le NavHost à la mise en page principale de notre activité :

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    tools:context=".MainActivity">

    <fragment
        android:id="@+id/nav_host_fragment"
        android:name="androidx.navigation.fragment.NavHostFragment"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintBottom_toBottomOf="parent"
        app:defaultNavHost="true"
        app:navGraph="@navigation/user_flow_graph" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

Nous avons ajouté un élément fragment qui accueillera l'endroit où nos fragments seront affichés et échangés. Portez une attention particulière à l'attribut **_navGraph_**, que nous avons lié à notre fichier XML précédemment créé.

Maintenant, nous devons ajouter une destination de départ, car notre application ne compilera pas si nous ne le faisons pas.

Avec le fichier user_flow_graph.xml ouvert, nous devons cliquer sur la petite icône plus dans l'Éditeur de Navigation :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_XqXtr0RPslpXd3MGHrinNQ.png)
_Ajouter une destination_

Vous pouvez voir dans le menu qui s'affiche que nous pouvons soit créer un espace réservé qui devra être rempli plus tard, soit choisir parmi n'importe quel fragment existant :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_0uRzLRsllNjeRM2FWC8yNQ.png)
_Nos choix de destination_

Notre flux utilisateur commence par notre Start Fragment, choisissons-le donc en premier.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_b1rlufocmmW_M6mfpK-buA.jpeg)
_Notre base (notez la petite icône ?)_

Ajoutons nos deux autres fragments, fragment A et fragment B.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_U58A5A6N8Id37xx63GCWXw.png)
_Toutes nos destinations_

Nous connectons deux destinations en cliquant sur le point qui apparaît lorsque nous survolons une destination et en le faisant glisser vers une autre.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/giphy--1-.gif)
_Plutôt sympa, non ?_

Ce que nous venons de créer entre le fragment Start et les fragments A et B sont des **_actions_**.

## Mille sabords

Vous vous êtes peut-être demandé si, en connectant simplement les destinations, notre travail s'arrêtait là et si, par magie, tout fonctionnerait.

Eh bien, non.

Nous devons dire à notre code de naviguer vers une destination. Alors, comment faire ? Un peu de magie est impliquée dans le processus.

La première chose que nous allons faire est d'ajouter un plugin Gradle appelé **_Safe Args_**. Il garantira la sécurité des types lors de la navigation entre nos destinations.

```gradle

buildscript {
   /...
    }
    dependencies {
        ...
        classpath "androidx.navigation:navigation-safe-args-gradle-plugin:2.0.0"
        
    }
}
```

Nous devrons également ajouter le plugin suivant au fichier build.gradle de notre application :

```gradle
apply plugin: "androidx.navigation.safeargs.kotlin"

```

Assurez-vous également que **_android.useAndroidX=true_** figure dans votre fichier gradle.properties.

Avant d'aller plus loin, comprenons pourquoi nous avons dû ajouter toutes ces configurations. Fondamentalement, lorsque nous avons créé des actions plus tôt, Android Studio a généré en coulisses du code que nous utiliserons pour activer ces actions. Ce code se compose de méthodes et de classes représentant chaque action. Prenons notre fragment Start comme exemple. Le code généré pour les actions que nous avons déclarées comportera une classe nommée **_StartFragmentDirections_**. Les méthodes de cette classe représentent les actions créées précédemment. Ainsi, pour nos deux fragments, nous obtiendrons :

* StartFragmentDirections.actionStartFragmentToFragmentA()
* StartFragmentDirections.actionStartFragmentToFragmentB()

Maintenant que nos actions ont été traduites en code, utilisons-les :

```kt
val action = StartFragmentDirections.actionStartFragmentToFragmentA()

```

La dernière étape de ce processus nous oblige à utiliser le [NavController](https://developer.android.com/reference/androidx/navigation/NavController). Cet objet est chargé de gérer la navigation au sein de notre NavHost. Vous pouvez y accéder via l'une de ces trois méthodes :

* Fragment.findNavController()
* View.findNavController()
* Activity.findNavController(viewId: Int)

Ainsi, une fois assemblé, nous aurons :

```kt
fragmentABtn.setOnClickListener { button ->
    val action = StartFragmentDirections.actionStartFragmentToFragmentA()
    button.findNavController().navigate(action)
}
```

## Ajustez vos voiles

Et si nous voulions passer des données entre nos destinations ? Imaginez un scénario où, si l'utilisateur clique sur un certain élément, nous voulons effectuer une action avec cet élément dans notre prochaine destination. Pour cela, nous avons les arguments de destination. Ouvrez notre fichier user_flow_graph.xml et cliquez sur le Fragment A. Vous remarquerez sur le côté droit un menu détaillant les divers attributs du Fragment A. L'un de ces attributs sera Arguments.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_G2zT0FkL8nNhE42g-g99eA.png)

Pour ajouter un argument, cliquez simplement sur l'icône ➕. Une fenêtre contextuelle s'ouvre, nous permettant de configurer notre argument. Vous pouvez lui donner un nom, choisir son type et ajouter une valeur par défaut. Ajoutons un argument de type String au Fragment A, qui sera le message transmis depuis le fragment Start.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_6oFcTwG7HSAeKs7C4Y2p7Q.png)

Dans notre fragment Start, là où nous avons défini notre action et appelons la méthode générée, nous allons passer notre argument.

```kt
fragmentABtn.setOnClickListener { button ->
    val action = StartFragmentDirections.actionStartFragmentToFragmentA("Bonjour depuis le fragment Start")
    button.findNavController().navigate(action)
}
```

Pour y accéder dans le Fragment A, nous devrons soit :

* accéder au bundle et récupérer la valeur de notre message

```kt
class FragmentA: Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val bundle = arguments
        val root = inflater.inflate(R.layout.fragment_a, container, false)
        val textView : TextView = root.findViewById(R.id.textView)
        textView.text = bundle?.getString("message")
        return root
    }
}
```

* utiliser navArgs si nous utilisons les dépendances -ktx

```kt
class FragmentA: Fragment() {

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val args : FragmentAArgs by navArgs()
        val root = inflater.inflate(R.layout.fragment_a, container, false)
        val textView : TextView = root.findViewById(R.id.textView)
        textView.text = args.message
        return root
    }
}
```

✋ lors de l'utilisation de navArgs, vous devrez ajouter le [support pour Java8](https://developer.android.com/studio/write/java8-support) dans votre fichier build.gradle.

Vous pouvez trouver tout le code présenté ici [dans ce dépôt GitHub](https://github.com/TomerPacific/MediumArticles/tree/master/NavigationComponent).