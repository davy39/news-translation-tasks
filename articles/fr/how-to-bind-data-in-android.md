---
title: Comment lier des données dans Android
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2020-02-23T17:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-bind-data-in-android
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/robert-bye-u2B-xZhoNaE-unsplash.jpg
tags:
- name: Binding Data
  slug: binding-data
- name: Android
  slug: android
- name: coding
  slug: coding
- name: Kotlin
  slug: kotlin
- name: 'tech '
  slug: tech
seo_title: Comment lier des données dans Android
seo_desc: "Data binding is a technique used when you want to glue pieces of information\
  \ (your data) to some visual user input elements. In this process, whenever the\
  \ input gets updated, the data behind it gets updated as well. \nThis is far from\
  \ a new concept, a..."
---

La liaison de données est une technique utilisée lorsque vous souhaitez associer des morceaux d'informations (vos données) à certains éléments visuels de saisie utilisateur. Dans ce processus, chaque fois que la saisie est mise à jour, les données derrière elle sont également mises à jour. 

Ce n'est pas un concept nouveau, et il existe une pléthore de frameworks qui ont intégré cela dans leur conception (comme AngularJS/React/Vue). 

Notre attention dans cet article n'est pas sur les frameworks front-end mais plutôt sur le développement mobile. Google a introduit la [Bibliothèque de liaison de données](https://developer.android.com/topic/libraries/data-binding) dans Android, qui fait partie de [Android Jetpack](https://developer.android.com/jetpack).

Si vous n'êtes pas familier avec la suite de bibliothèques Jetpack, cela peut être dû au fait que [Google a annoncé](https://developer.android.com/topic/libraries/support-library) qu'il abandonnerait le développement de ses bibliothèques de support. Au lieu de cela, il passera à la prise en charge des bibliothèques AndroidX (qui sont la nouvelle version des bibliothèques de support).

Je suis conscient qu'il existe de nombreux articles expliquant comment utiliser la liaison de données avec un adaptateur, mais cet article ne se concentrera pas sur cela. Au lieu de cela, je vais montrer une approche minimale et basique de la liaison de données qui peut vous faire gagner du temps en minimisant la quantité de code que vous devez écrire.

# Pourquoi utiliser la liaison de données ?

Si vous n'êtes pas encore convaincu, prenons quelques minutes pour expliquer les avantages de l'utilisation de la liaison de données en montrant un exemple. Supposons que vous avez un menu avec trois boutons personnalisés, où chaque bouton est une mise en page en soi.

![Image](https://miro.medium.com/max/438/1*DSKPtz7x8bn2NUVPhdMU4A.png)
_Notre mise en page_

Une façon de générer tout cela est d'utiliser quatre différentes mises en page XML : une pour la mise en page principale et une pour chacun des trois boutons.

Vous devez faire cela puisque chaque bouton dirigera l'utilisateur vers une partie différente de votre application et nécessite donc un texte différent et une image différente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_gravity="center_horizontal"
    android:layout_height="wrap_content"
    android:layout_width="wrap_content">


    <ImageView
        android:id="@+id/imageView"
        android:layout_height="100dp"
        android:layout_width="100dp"
        android:src="@drawable/image_name"
        android:adjustViewBounds="true"
        android:scaleType="centerInside"
        />

    <TextView
        android:id="@+id/textView"
        android:gravity="center_horizontal"
        android:layout_height="wrap_content"
        android:layout_width="match_parent"
        android:text="Image Text"
        android:textSize="16sp" />

</LinearLayout>
```

Certes, ce n'est pas beaucoup de duplication de code puisque nous ne gérons que trois mises en page. Mais si vous y réfléchissez, c'est assez une perte de temps de traiter tout ce code. Si vous prenez en compte une application qui a une mise en page plus compliquée, une qui pourrait présenter des produits et leurs images, cela peut conduire à beaucoup de réplication de code fastidieuse.

Avec la liaison de données, nous allons réussir à créer une seule mise en page XML qui sera utilisée par tous nos boutons.

# Par où commençons-nous ?

Nous devons permettre à notre projet d'activer la liaison de données. Pour cela, nous devons ajouter l'élément `dataBinding` dans notre fichier `build.gradle` de l'application :

```
android {
    compileSdkVersion 29
    buildToolsVersion "29.0.2"
    defaultConfig {
        applicationId "com.tomerpacific.example"
        minSdkVersion 15
        targetSdkVersion 29
        versionCode 1
        versionName "1.0"
        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
        dataBinding {              //<-------
          enabled = true
        }
    }
    buildTypes {
        release {
            minifyEnabled false
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}
```

Après avoir synchronisé notre projet, nous allons créer notre classe de données, que nous utiliserons pour lier la mise en page.

```kotlin
package com.tomerpacific.example

import android.graphics.drawable.Drawable

data class ButtonData(val buttonText: String, val buttonImageSrc : Drawable)

```

Faites attention au fait que nous avons deux champs dans notre classe `ButtonData` :

* `buttonText` — C'est le texte qui apparaîtra sous notre image.
* `buttonImageSrc` — Cela est responsable de l'image du bouton.

Si nous voulions plus de données, nous ajouterions simplement plus de champs à notre classe de données.

# La liaison réelle

Ensuite, nous devons déclarer une propriété de variable dans notre mise en page afin qu'elle puisse être utilisée. Cette variable sera liée à la classe de données que nous avons créée. Pour cela, il y a deux choses que nous devons faire :

* Envelopper notre élément de mise en page racine dans une balise de mise en page.
* Ajouter une balise de données qui contiendra la déclaration de notre variable (`buttonData`).

```xml
<?xml version="1.0" encoding="utf-8"?>
<layout xmlns:android="http://schemas.android.com/apk/res/android">  // <---- 1
                                                                              
    <data>
        <variable name="buttonData" type="com.tomerpacific.example.ButtonData"/> // <---- 2
    </data>
    
    <androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto"
        android:layout_width="match_parent"
        android:layout_height="match_parent">


        <TextView
            android:id="@+id/textView2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Example"
            android:textSize="30dp"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"
            app:layout_constraintTop_toTopOf="parent" />

        <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:orientation="vertical"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toStartOf="@+id/linearLayout3"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/textView2">

            <ImageButton
                android:layout_width="100dp"
                android:layout_height="100dp"
                android:adjustViewBounds="true"
                android:scaleType="centerInside"
                android:src="@drawable/android">

            </ImageButton>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_horizontal"
                android:text="Image Text"
                android:textSize="16sp" />

        </LinearLayout>

        <LinearLayout
            android:id="@+id/linearLayout3"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:orientation="vertical"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/textView2"
            app:layout_constraintVertical_bias="0.504">

            <ImageButton
                android:layout_width="100dp"
                android:layout_height="100dp"
                android:adjustViewBounds="true"
                android:scaleType="centerInside"
                android:src="@drawable/android_p_logo">

            </ImageButton>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_horizontal"
                android:text="Image Text"
                android:textSize="16sp" />

        </LinearLayout>

        <LinearLayout
            android:id="@+id/linearLayout2"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:orientation="vertical"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toEndOf="parent"
            app:layout_constraintHorizontal_bias="0.200"
            app:layout_constraintStart_toEndOf="@+id/linearLayout3"
            app:layout_constraintTop_toBottomOf="@+id/textView2"
            app:layout_constraintVertical_bias="0.504">

            <ImageButton
                android:layout_width="100dp"
                android:layout_height="100dp"
                android:adjustViewBounds="true"
                android:scaleType="centerInside"
                android:src="@drawable/android_studio_icon">

            </ImageButton>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_horizontal"
                android:text="Image Text"
                android:textSize="16sp" />

        </LinearLayout>


    </androidx.constraintlayout.widget.ConstraintLayout>
    
</layout>
```

Remarquez que nous pouvons supprimer le schéma de notre précédente mise en page principale car il a été déplacé vers la balise de mise en page racine. De plus, la variable que nous avons ajoutée est directement liée à notre classe de données.

Dans notre fichier `MainActivity`, nous devons ajouter du code pour gérer la liaison :

```kotlin
package com.tomerpacific.example

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.databinding.DataBindingUtil
import com.tomerpacific.example.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val binding: ActivityMainBinding = DataBindingUtil.setContentView(
            this, R.layout.activity_main)

        binding.buttonData = ButtonData("First", resources.getDrawable(R.drawable.android))
    }
}
```

Chaque fois que vous créez une variable à l'intérieur d'une mise en page, une classe de liaison est générée automatiquement pour cette mise en page. Dans notre cas, notre mise en page s'appelle `activity_main`, donc la classe de liaison s'appellera `ActivityMainBinding`.

La convention est toujours le nom de la mise en page avec _Binding_ ajouté à la fin.

Puisque nous avons déclaré `buttonData` comme notre variable dans la mise en page, elle est ajoutée à l'objet de liaison et nous pouvons lui assigner une nouvelle instance de notre classe `ButtonData`.

Après avoir fait tout cela, nous pouvons enfin utiliser les données que nous venons de lier dans notre mise en page.

```xml
<LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:orientation="vertical"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toStartOf="@+id/linearLayout3"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/textView2">

            <ImageButton
                android:layout_width="100dp"
                android:layout_height="100dp"
                android:adjustViewBounds="true"
                android:scaleType="centerInside"
                android:src="@{buttonData.buttonImageSrc}">  // <----

            </ImageButton>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_horizontal"
                android:text="@{buttonData.buttonText}"   // <----
                android:textSize="16sp" />
```

Et le résultat est :

![Image](https://miro.medium.com/max/438/1*fpchbTcVUnKWKcQQTBvkmg.png)
_Assez fluide, hein ?_

# Attendez une seconde...

Nous avons trois boutons et notre classe de données ne peut être utilisée que pour un bouton, alors comment faisons-nous pour passer outre cela ?

```kotlin
package com.tomerpacific.example

data class ButtonsData(val buttonsData : List<ButtonData>) {

    fun get(index: Int) : ButtonData {
        return buttonsData.get(index)
    }
}
```

Nous avons dû remplacer la méthode `get` car elle doit être reconnue lorsque nous l'utilisons dans notre mise en page.

Ensuite, nous devons changer les références dans notre `activity_main.xml` :

```xml
 <data>
        <variable name="buttonsData" type="com.tomerpacific.example.ButtonsData"/>
 </data>
```

Et nous devons créer une nouvelle liaison à la nouvelle classe de données :

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val binding: ActivityMainBinding = DataBindingUtil.setContentView(
            this, R.layout.activity_main)

        val firstButton : ButtonData = ButtonData("First", resources.getDrawable(R.drawable.android))

        val secondButton : ButtonData = ButtonData("Second", resources.getDrawable(R.drawable.android_p_logo))

        val thirdButton : ButtonData = ButtonData("Third", resources.getDrawable(R.drawable.android_studio_icon))

        val buttonsData : ButtonsData = ButtonsData(listOf(firstButton, secondButton, thirdButton))

        binding.buttonsData = buttonsData
    }
```

Nous créons trois instances de la classe `ButtonData`. Ensuite, nous instancions un objet `ButtonsData` et l'attachons à notre objet de liaison.

Enfin, nous pouvons maintenant utiliser correctement notre classe de données dans notre mise en page :

```xml
 <LinearLayout
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:layout_gravity="center_horizontal"
            android:orientation="vertical"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintEnd_toStartOf="@+id/linearLayout3"
            app:layout_constraintStart_toStartOf="parent"
            app:layout_constraintTop_toBottomOf="@+id/textView2">

            <ImageButton
                android:layout_width="100dp"
                android:layout_height="100dp"
                android:adjustViewBounds="true"
                android:scaleType="centerInside"
                android:src="@{buttonsData.get(0).buttonImageSrc}">   // <-------

            </ImageButton>

            <TextView
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:gravity="center_horizontal"
                android:text="@{buttonsData.get(0).buttonText}"       // <--------
                android:textSize="16sp" />

        </LinearLayout>
```

![Image](https://miro.medium.com/max/438/1*IKBNh860MfZ4xj7Og6osKw.png)
_Fonctionne comme un charme_

Cet article a été écrit grâce à mon expérience de développement de l'application suivante :

(On ne sait jamais, cela pourrait être utile)

%[https://play.google.com/store/apps/details?id=com.tomerpacific.laundry]

Vous pouvez voir le code source complet ici :

%[https://github.com/TomerPacific/LaundrySymbols]