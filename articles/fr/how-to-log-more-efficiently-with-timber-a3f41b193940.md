---
title: Comment journaliser plus efficacement avec Timber
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-19T16:01:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-log-more-efficiently-with-timber-a3f41b193940
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jwVV3w-tjti4a_a9QhMOcg.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment journaliser plus efficacement avec Timber
seo_desc: 'By Ayusch Jain

  Logging is one of the most used utilities in the Android framework. It is really
  helpful in debugging your code when debugging by break-point just won''t work.

  It is generally a good practice to place Log statements in your code. These ...'
---

Par Ayusch Jain

La journalisation est l'une des utilités les plus utilisées dans le **framework Android**. Elle est vraiment utile pour déboguer votre code lorsque le débogage par point d'arrêt ne fonctionne tout simplement pas.

Il est généralement une bonne pratique de placer des instructions de journalisation dans votre code. Ces instructions vous aident à suivre le contrôle de flux dans votre application. De même, il n'est pas recommandé d'avoir des instructions de journalisation dans votre code prêt pour la release, car ces instructions de journalisation peuvent être lues par quiconque connecte son téléphone à un PC. Ainsi, lors de la publication de votre application sur le Play Store, il est recommandé de supprimer toutes les instructions de journalisation de votre code.

Mais cela peut être un vrai casse-tête. Il y a tellement d'instructions de journalisation partout dans votre code. Maintenant, vous devez trouver chacune d'entre elles et la supprimer de votre code pour la version de release.

Un autre problème avec le mécanisme de journalisation par défaut est que vous devez passer le TAG à chaque fois que vous écrivez une instruction de journalisation.

Ne serait-ce pas merveilleux si les instructions de journalisation se désactivaient automatiquement en production ? Ne serait-ce pas génial si les instructions de journalisation récupéraient automatiquement le **TAG**/nom de classe lors de la journalisation et que vous puissiez vous concentrer uniquement sur l'écriture d'un meilleur code ?

Eh bien, des problèmes tels que ceux-ci et bien d'autres sont résolus par une meilleure bibliothèque de journalisation sur Android, appelée **Timber** (par Jake Wharton).

Il s'agit d'une bibliothèque légère et facile à utiliser. Elle prend en charge la plupart de la maintenance que vous devez effectuer lors de la journalisation afin que vous puissiez vous concentrer davantage sur l'écriture d'un excellent code et moins sur les tâches de maintenance.

Allons-y et créons une application d'exemple pour voir comment vous pouvez inclure **Timber** dans votre **application Android** et faciliter votre vie de journalisation.

### Mise en route

Nous allons créer une simple application Android avec 4 boutons. Chaque bouton imprimera une instruction de journalisation de priorité différente sur la console.

Créez un nouveau projet dans Android et ajoutez une dépendance pour Timber dans votre fichier build.gradle au niveau de l'application. Au moment de la rédaction de cet article, voici la dernière version de dépendance pour Timber :

```
implementation 'com.jakewharton.timber:timber:4.7.1'
```

### Initialisation de Timber

Avec la dépendance téléchargée, il est maintenant temps d'initialiser la bibliothèque Timber. Le meilleur endroit pour initialiser Timber est dans la classe Application qui sera active pendant toute la durée de vie de l'application. Alors, créons une classe d'application personnalisée et initialisons notre **bibliothèque Timber** dans celle-ci :

```
class MainApplication : Application() {    override fun onCreate() {        super.onCreate()        if(BuildConfig.DEBUG){            Timber.plant(Timber.DebugTree())        }    }}
```

### Création de MainActivity

Créons maintenant notre MainActivity en ajoutant 4 boutons et en définissant des écouteurs de clics pour chacun d'eux. Voici mon fichier activity_main.xml. J'utilise ConstraintLayout comme layout racine et j'inclus 4 boutons, chacun pour différents niveaux de journalisation.

```
<?xml version="1.0" encoding="utf-8"?><android.support.constraint.ConstraintLayout        xmlns:android="http://schemas.android.com/apk/res/android"        xmlns:tools="http://schemas.android.com/tools"        xmlns:app="http://schemas.android.com/apk/res-auto"        android:layout_width="match_parent"        android:layout_height="match_parent"        tools:context=".MainActivity">
```

```
    <Button            android:text="Journal d'erreur"            android:layout_width="wrap_content"            android:layout_height="wrap_content"            android:id="@+id/btn_error" app:layout_constraintStart_toStartOf="parent" android:layout_marginStart="8dp"            app:layout_constraintEnd_toEndOf="parent" android:layout_marginEnd="8dp" android:layout_marginTop="108dp"            app:layout_constraintTop_toTopOf="parent" app:layout_constraintHorizontal_bias="0.498"/>    <Button            android:text="Journal d'info"            android:layout_width="wrap_content"            android:layout_height="wrap_content"            android:id="@+id/btn_info" android:layout_marginTop="64dp"            app:layout_constraintTop_toBottomOf="@+id/btn_error" app:layout_constraintStart_toStartOf="parent"            android:layout_marginStart="8dp" app:layout_constraintEnd_toEndOf="parent" android:layout_marginEnd="8dp"            app:layout_constraintHorizontal_bias="0.498"/>    <Button            android:text="Journal de débogage"            android:layout_width="wrap_content"            android:layout_height="wrap_content"            android:id="@+id/btn_debug" android:layout_marginTop="72dp"            app:layout_constraintTop_toBottomOf="@+id/btn_info" app:layout_constraintStart_toStartOf="parent"            android:layout_marginStart="8dp" app:layout_constraintEnd_toEndOf="parent" android:layout_marginEnd="8dp"    />    <Button            android:text="Journal détaillé"            android:layout_width="wrap_content"            android:layout_height="wrap_content"            android:id="@+id/btn_verbose" android:layout_marginTop="68dp"            app:layout_constraintTop_toBottomOf="@+id/btn_debug" app:layout_constraintStart_toStartOf="parent"            android:layout_marginStart="8dp" app:layout_constraintEnd_toEndOf="parent" android:layout_marginEnd="8dp"            android:layout_marginBottom="8dp"            app:layout_constraintBottom_toBottomOf="parent" app:layout_constraintVertical_bias="0.061"/></android.support.constraint.ConstraintLayout>
```

Il est maintenant temps de définir des écouteurs de clics pour ces boutons et d'imprimer une instruction de journalisation à chaque fois qu'un bouton est cliqué. J'utilise les liaisons synthétiques de Kotlin au lieu des appels findViewById réguliers ou Butterknife. Voici mon fichier **MainActivity.kt** :

```
class MainActivity : AppCompatActivity() {
```

```
    override fun onCreate(savedInstanceState: Bundle?) {        super.onCreate(savedInstanceState)        setContentView(R.layout.activity_main)
```

```
        btn_error.setOnClickListener {            onClickedError()        }
```

```
        btn_info.setOnClickListener {            onInfoClicked()        }
```

```
        btn_debug.setOnClickListener {            onDebugClicked()        }
```

```
        btn_verbose.setOnClickListener {            onVerboseClicked()        }    }
```

```
    private fun onVerboseClicked() {        Timber.v("On Verbose Clicked")    }
```

```
    private fun onDebugClicked() {        Timber.d("On Debug Clicked.")    }
```

```
    private fun onInfoClicked() {        Timber.i("On Info clicked.")    }
```

```
    private fun onClickedError() {        Timber.e("On Error Clicked.")    }
```

```
}
```

Remarquez comment nous n'avons pas eu besoin d'initialiser de variable TAG dans notre classe, Timber le fait automatiquement pour vous.

### Personnalisation de Timber pour le débogage et la release

Maintenant, **c'est là que Timber brille vraiment**. Ce que nous avons fait jusqu'à présent n'était pas grand-chose, juste l'impression des instructions de journalisation lors des clics sur les boutons. Mais comme vous le savez, la journalisation en production n'est pas une bonne idée. Nous allons écrire du code pour désactiver les logs pour la production tout en les gardant activés pendant le mode débogage.

Nous allons écrire un bloc if pour vérifier si notre application est en mode débogage et activer la journalisation pour cela. Sinon, nous voulons initialiser Timber en utilisant un **arbre personnalisé**.

Voici la classe **MainApplication.kt** modifiée :

```
class MainApplication : Application() {    override fun onCreate() {        super.onCreate()        if (BuildConfig.DEBUG) {            Timber.plant(object : Timber.DebugTree() {                override fun createStackElementTag(element: StackTraceElement): String? {                    return String.format(                        "Classe:%s: Ligne: %s, Méthode: %s",                        super.createStackElementTag(element),                        element.lineNumber,                        element.methodName                    )                }            })        } else {            Timber.plant(ReleaseTree())        }    }}
```

Comme vous pouvez le voir, nous avons initialisé Timber en utilisant un **ReleaseTree** personnalisé en mode release. Maintenant, allons-y et créons notre propre arbre de release.

### Création d'un arbre personnalisé

Créer un arbre de release est assez simple. Créez une nouvelle classe Kotlin et étendez-la à partir de Timber.Tree. Implémentez toutes les fonctions abstraites et vous êtes prêt à partir.

Voici mon **ReleaseTree.kt** :

```
class ReleaseTree : @NotNull Timber.Tree() {    override fun log(priority: Int, tag: String?, message: String, t: Throwable?) {        if (priority == Log.ERROR || priority == Log.WARN){            //ENVOYER DES RAPPORTS D'ERREURS À VOTRE Crashlytics.        }    }
```

```
}
```

Comme vous pouvez le voir, chaque fois qu'il y a une erreur, nous pouvons envoyer le **log** à un service en ligne tel que **Firebase CrashAnalytics ou Crashlytics** et ne pas journaliser en production.

### Résultat

![Image](https://cdn-media-1.freecodecamp.org/images/xRCI296sls6A8gFqAj6d2PLArZ2XviazZ-0n)
_source : https://ayusch.com_

### Avantages de l'utilisation de Timber vs Android Logging

Examinons quelques-uns des avantages de l'utilisation de la bibliothèque Timber au lieu de l'utilitaire Log par défaut du SDK Android.

* **Pas besoin de s'inquiéter des TAGS** : Timber génère les TAGS automatiquement pour vous, donc vous n'avez pas à vous soucier d'inclure un TAG global dans chaque classe.
* **Pas besoin de supprimer manuellement les instructions Log** : Comme déjà montré, il est vraiment facile de désactiver la journalisation pour les applications de release. Ainsi, vous n'avez plus à parcourir tout votre code et à supprimer manuellement tous les logs.
* **Comportement personnalisé en production** : Dans les versions de production, vous ne voulez pas journaliser, bien que vous souhaitiez certainement journaliser les plantages qui pourraient survenir. Vous pouvez implémenter cela en utilisant un arbre de débogage personnalisé (comme montré ci-dessus) qui, au lieu de journaliser dans le logcat, envoie les logs à votre service Crashlytics.
* **Métadonnées personnalisées** : Vous pouvez inclure des métadonnées personnalisées avec vos instructions de journalisation. Par exemple, j'ai ajouté le nom de la classe, le numéro de ligne et le nom de la méthode à partir desquels l'instruction de journalisation est imprimée dans l'implémentation ci-dessus. Avoir ces données à votre disposition peut faciliter le débogage.
* **Léger** : N'augmente pas beaucoup la taille de votre application/nombre de méthodes. Bibliothèque vraiment légère car elle n'est qu'un wrapper sur l'utilitaire de journalisation déjà existant.

### Conclusion

Pendant longtemps, j'ai ignoré l'utilisation des instructions de journalisation et l'impression de meilleurs logs. À mesure que mon code devenait plus volumineux et que les problèmes devenaient plus complexes, j'ai réalisé que je devais adopter de meilleures et plus efficaces routines de débogage. Ainsi, l'utilisation de Timber est une étape dans la bonne direction.

> **_*Important*_** : J'ai créé un espace de travail [**SLACK**](https://join.slack.com/t/androidvillespace/shared_invite/enQtNTQxOTY4NjI4NjE0LTA3ZGFiZjViNGRjZDdjNThhZjRlNjM0MTZlYzRlZWM0YTYxY2EwMzU0ZDdhNmRkMjJhYzBiZTA3Y2NjZTc4ZmU) pour les développeurs mobiles où nous pouvons partager nos apprentissages sur tout ce qui est nouveau dans la technologie, en particulier dans **le développement Android, RxJava, Kotlin, Flutter, et le développement mobile en général**._

> [**Cliquez sur ce lien pour rejoindre l'espace de travail Slack. C'est absolument gratuit !**](https://join.slack.com/t/androidvillespace/shared_invite/enQtNTk4NzUzMDk3Nzk2LTUwNWU2OTNiYWU3YjBiOWQ0NzY3Y2I5ZjVlOTFkOWFjN2FmOGRhM2JmZDhjY2Q0YmI1YjFkODMwMjViMDg4MGU)

> _Cet article a été initialement publié à l'adresse [https://ayusch.com/timber-for-android](https://ayusch.com/timber-for-android)_

_Aimez ce que vous lisez ? N'oubliez pas de partager cet article sur [**Facebook**](https://www.facebook.com/AndroidVille), **WhatsApp**, et **LinkedIn**._

_Vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), et [Instagram](https://www.instagram.com/androidville/) où je **réponds** aux questions liées au **développement mobile, en particulier Android et Flutter**._