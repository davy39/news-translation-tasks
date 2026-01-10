---
title: Un tutoriel Jetpack Compose pour débutants – Comment comprendre les Composables
  et la Recomposition
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2021-03-08T21:19:42.000Z'
originalURL: https://freecodecamp.org/news/jetpack-compose-beginner-tutorial-composables-recomposition
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6042c692a7946308b7682cbb.jpg
tags:
- name: Android
  slug: android
- name: UI
  slug: ui
seo_title: Un tutoriel Jetpack Compose pour débutants – Comment comprendre les Composables
  et la Recomposition
seo_desc: 'This tutorial will teach you a few fundamental concepts and terms related
  to the Jetpack Compose UI Library on Android.

  While this is a beginner''s guide to Compose, it will not be a beginner''s guide
  to Android – so you should have built at least an a...'
---

Ce tutoriel vous enseignera quelques concepts et termes fondamentaux liés à la bibliothèque d'interface utilisateur Jetpack Compose sur Android.

Bien que ce soit un guide pour débutants sur Compose, ce ne sera pas un guide pour débutants sur Android – vous devriez donc avoir construit au moins une ou deux applications (bien que pas nécessairement en Compose).

Avant de commencer, j'avais initialement prévu d'écrire un article de suivi destiné aux développeurs plus expérimentés jusqu'à ce que je tombe sur la série d'articles en deux parties de Leland Richardson [two part article series](https://medium.com/androiddevelopers/understanding-jetpack-compose-part-1-of-2-ca316fe39050). Leland n'est pas seulement un ingénieur logiciel travaillant sur l'équipe Jetpack Compose, mais je vois aussi qu'il est un excellent écrivain.

Bien que je pense que mon article se suffira à lui-même comme introduction aux bases de Jetpack Compose, je vous **recommande fortement** de lire ses articles une fois que vous aurez acquis une certaine expérience pratique avec Compose (ou tout de suite si vous préférez apprendre de cette manière).

%[https://youtu.be/ijwBr4oeX0I]

### Concepts/Termes clés expliqués dans cet article :

* Un bref rappel de l'ancien système de vues et de la hiérarchie

* Les Composables et leur relation avec les Vues

* La Recomposition et comment éviter de la faire très mal !

# Qu'est-ce qu'un Composable ?

Dans cette section, nous allons discuter de la partie la plus fondamentale de la bibliothèque Jetpack Compose. Si vous êtes un développeur Android expérimenté, vous pouvez sauter à la sous-section intitulée « Les Composables sont-ils des Vues ? »

Si vous n'êtes pas déjà familier avec le système de Vues, vous devriez lire la section suivante car elle est nécessaire pour comprendre ce qu'est un Composable.

## Hiérarchie des Vues

Dans le contexte du SDK Android (les bibliothèques que nous utilisons pour créer des interfaces utilisateur sur cette plateforme), une Vue est ce que nous utilisons pour donner une structure et un style à nos applications.

C'est le type de bloc de construction ou d'élément le plus fondamental d'une interface utilisateur (UI) donnée, et chacun de ces blocs de construction contiendra les types d'informations suivants (entre autres) :

* Les positions de début et de fin X et Y qui indiquent à l'ordinateur où dessiner la vue sur l'écran de l'appareil

* Les valeurs de couleur et d'alpha (transparence)

* Les informations de police, le texte, les symboles et les images

* Le comportement basé sur des événements tels que l'interaction de l'utilisateur (clics) ou les changements dans les données de l'application (nous y reviendrons plus tard)

Il est important de comprendre qu'**une Vue peut être quelque chose comme un bouton** (communément appelé « widget »), **mais elle peut aussi être un conteneur de tout l'écran, d'une partie de l'écran, ou pour d'autres Vues enfants**.

Ces **conteneurs** sont communément appelés Layouts ou ViewGroups selon le contexte. Et, bien qu'ils partagent la plupart des mêmes types d'informations qu'un widget, ils contiennent également des informations sur la manière d'organiser et d'afficher d'autres Vues qui sont **imbriquées** à l'intérieur.

Cela dit, nous arrivons à la partie importante de cette revue du système de Vues : la **Hiérarchie des Vues**. Pour les développeurs Web, la Hiérarchie des Vues est essentiellement la version Android du Document Object Model (DOM).

Pour les développeurs Android, vous pouvez penser à la Hiérarchie des Vues comme une représentation virtuelle de toutes les Vues que vous avez définies soit dans des fichiers XML, soit programmatiquement en Java ou Kotlin.

Pour illustrer cela, regardons un tel fichier XML (il n'est pas nécessaire de l'étudier de près, notez simplement les noms). Ensuite, en utilisant un outil de débogage/pas à pas, nous allons voir à quoi il ressemble dans l'espace mémoire du Fragment qui gonfle ce fichier :

**fragment_hour_view.xml :**

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
android:layout_width="match_parent"
android:layout_height="match_parent"
android:id="@+id/root_hour_view_fragment"
xmlns:app="http://schemas.android.com/apk/res-auto"
>
<androidx.compose.ui.platform.ComposeView
android:id="@+id/tlb_hour_view"
//...
 />
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id="@+id/vqht_one"
//...
/>
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id="@+id/vqht_two"
//...
/>
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id="@+id/vqht_three"
//...
/>
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id="@+id/vqht_four"
//...
/>
</androidx.constraintlayout.widget.ConstraintLayout>
```

**Espace mémoire de (Fragment)HourView.kt :**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-22.png align="left")

*Image d'une Hiérarchie de Vues*

Les outils de débogage et de pas à pas sont parmi mes façons préférées d'apprendre ce qui se passe sous le capot du code que j'utilise à partir de diverses bibliothèques. Essayez-les un jour !

Le but de vous montrer ce fichier XML et ce qu'il devient dans un **processus** (un processus est **simplement un programme qui s'exécute** sur un appareil), est de démontrer comment les Vues imbriquées dans un fichier XML se traduisent par une Hiérarchie de Vues imbriquée à l'exécution.

Espérons qu'avec un modèle simple mais concret de la manière dont l'ancien système fonctionne, nous pouvons le comparer avec le nouveau.

## Les Composables sont-ils des Vues ?

C'était l'une des premières questions que je me suis posée lorsque j'ai commencé à travailler avec Compose, et la réponse à laquelle je suis parvenue est à la fois **oui** et **non**.

**Oui**, dans le sens où un Composable remplit le **même rôle conceptuel qu'une Vue** dans l'ancien système. Un Composable peut être un widget comme un bouton, ou un conteneur tel qu'un ConstraintLayout (il est intéressant de noter qu'il existe une implémentation Composable de ConstraintLayout disponible).

**Non**, dans le sens où l'interface utilisateur n'est plus représentée virtuellement dans une Hiérarchie de Vues (à part dans les situations impliquant l'interopérabilité). Cela dit, Compose n'utilise pas de magie pour représenter et suivre virtuellement l'interface utilisateur. Cela signifie qu'il doit avoir sa propre chose qui est conceptuellement similaire à une Hiérarchie de Vues.

Examinons brièvement cette chose. Ici, nous avons une Activité qui utilise la fonction `setContent {...}` pour lier un Composable à elle-même :

**ActiveGameActivity.kt :**

```kotlin
class ActiveGameActivity : AppCompatActivity(), ActiveGameContainer {
private lateinit var logic: ActiveGameLogic
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    val viewModel = ActiveGameViewModel()
    setContent {
        ActiveGameScreen(
            onEventHandler = {
                logic.onEvent(it)
            },
            viewModel
        )
    }
    logic = buildActiveGameLogic(this, viewModel, applicationContext)
}
//...
}
```

**ActiveGameScreen.kt :**

```kotlin
@Composable
fun ActiveGameScreen(
    onEventHandler: ((ActiveGameEvent) -> Unit),
    viewModel: ActiveGameViewModel
) {
    //...

    GraphSudokuTheme {
        Column(
            Modifier
                .background(MaterialTheme.colors.primary)
                .fillMaxHeight()
        ) {
            ActiveGameToolbar(
                clickHandler = {
                    onEventHandler.invoke(
                        ActiveGameEvent.OnNewGameClicked
                    )
                }
            )

            Box {
              //contenu
            }
        }
    }
}
```

Dans Compose, la Hiérarchie des Vues est remplacée par quelque chose que nous pouvons localiser si nous creusons profondément dans le champ **mWindow** de cette Activité. Dans ce champ se trouve le remplacement conceptuel de la Hiérarchie des Vues : **Le** `**Composer**` **et sa** `**slotTable**`**.**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-26.png align="left")

À ce stade, si vous souhaitez un aperçu détaillé du `Composer` et de sa `slotTable`, je dois à nouveau vous suggérer de lire l'article de Leland (il entre dans les détails dans la [partie 2](https://medium.com/androiddevelopers/under-the-hood-of-jetpack-compose-part-2-of-2-37b2c20c6cdd)). Il y a plus dans la Hiérarchie Compose que le Composer et sa slotTable, mais cela devrait être suffisant pour nous lancer.

En termes généraux, Jetpack Compose utilise ce que nous pourrions appeler sa Hiérarchie Compose (qui est composée et gérée par des choses comme le Composer et sa slotTable).

Encore une fois, c'est la même idée conceptuelle que la hiérarchie des vues, un ensemble d'objets dans l'espace mémoire qui représentent collectivement l'interface utilisateur, mais elle est implémentée très différemment.

Il y a une différence importante, cependant, qui est difficile à comprendre techniquement, mais facile à comprendre en principe. Il s'agit de la manière dont Compose gère les mises à jour de la Hiérarchie Compose : **la Recomposition**.

# Recomposition : Comment mettre à jour l'interface utilisateur Compose

Pour mes amis ESL, le mot Compose vient du latin *componere*, qui signifie approximativement « mettre ensemble ». Une personne qui écrit de la musique est souvent appelée un « Compositeur », ce qui peut être considéré comme celui qui met ensemble les notes provenant d'un ou plusieurs instruments dans une composition (chanson).

Mettre ensemble implique qu'il y a des pièces individuelles. Il est important de comprendre que presque tous les bons développeurs de logiciels font au moins un effort pour décomposer leur code en les **plus petites parties raisonnables**.

Je mentionne **raisonnable**, car je pense que des principes comme DRY (Don't Repeat Yourself) ne doivent être suivis que dans la mesure où ils résolvent plus de problèmes qu'ils n'en créent.

Il y a de nombreux avantages à appliquer ce concept, qui est souvent appelé modularité (ou comme je préfère, Séparation des Préoccupations, ou SOC). Je suis conscient que certains d'entre vous qui lisez ceci pourraient penser que je copie simplement ce que Leland a dit dans son article, mais je parle de SOC comme du Principe d'Or de l'Architecture Logicielle depuis [de nombreuses années déjà](https://rkay301.medium.com/programming-fundamentals-part-5-separation-of-concerns-software-architecture-f04a900a7c50).

Là où cela intervient dans Compose, c'est le même principe que nous voyons dans la bibliothèque Javascript populaire **React**. Lorsqu'elle est bien faite, Compose ne « recomposera » (redessiner, réafficher, mettre à jour, peu importe) que les Composables (parties/éléments de l'interface utilisateur) qui doivent être recomposés.

Cela est EXTRÊMEMENT important en ce qui concerne les performances d'une application. Cela est dû au fait que redessiner l'interface utilisateur, qu'il s'agisse de l'ancien système de Vues ou de Compose, est coûteux en ressources système.

Au cas où vous ne le sauriez pas, le but entier de l'ancien RecyclerView (qui était la première chose pour laquelle j'ai jamais fait un tutoriel en 2016 !) était d'employer le modèle ViewHolder pour une liste de données. Cela évitait le besoin de constamment gonfler (créer) de nouvelles Vues pour chaque élément de la liste.

Mon objectif dans cet article était de me concentrer principalement sur la théorie, car j'écrirai beaucoup de contenu pratique au cours des prochains mois. Cependant, je terminerai l'article par une histoire tirée de mon expérience directe, qui vous aidera à mieux comprendre comment fonctionne la recomposition, et **comment éviter de la faire très mal !**

# L'exemple du chronomètre

Pour ma première application complète Compose, j'ai décidé de construire Sudoku. Il y a plusieurs raisons à cela, y compris le fait que je voulais un projet qui n'avait pas une interface utilisateur incroyablement compliquée. Je voulais aussi l'occasion de plonger profondément dans les structures de données de graphes et les algorithmes, qui sont assez adaptés aux puzzles Sudoku.

Une chose que je voulais était un chronomètre qui garderait une trace du temps qu'il fallait à l'utilisateur pour compléter un puzzle :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-27.png align="left")

*Puzzle Graph Sudoku*

Comme c'est souvent le cas dans ma profession, je m'attendais à ce que ce chronomètre soit beaucoup plus facile à ajouter qu'il ne l'était réellement. J'ai bidouillé avec la classe Chronometer d'Android ainsi qu'avec la classe Timer de Java, et les deux présentaient des problèmes différents mais toujours des problèmes qui cassaient l'application.

Finalement, j'ai fait un pas en arrière et j'ai réalisé que j'écrivais en Kotlin. J'ai donc mis en place un chronomètre basé sur des coroutines dans ma classe de logique de présentation (c'est là que cela avait le plus de sens), qui mettrait à jour mon viewmodel chaque seconde :

```kotlin
Class ActiveGameLogic(...) : ...{
//...
inline fun startCoroutineTimer(
    delayMillis: Long = 0,
    repeatMillis: Long = 1000,
    crossinline action: () -> Unit
) = launch {
    delay(delayMillis)
    if (repeatMillis > 0) {
        while (true) {
            action()
            delay(repeatMillis)
        }
    } else {
        action()
    }
}
private fun onStart() =
launch {
    gameRepo.getCurrentGame(
    { puzzle, isComplete ->
        viewModel.initializeBoardState(
            puzzle,
            isComplete
    )
        if (!isComplete) timerTracker = startCoroutineTimer {
            viewModel.updateTimerState()
        }
    },{
        container?.onNewGameClick()
    })
}
//...
}
```

Le ViewModel (non de AAC – j'écris mes propres VM. Mais Compose a déjà une bonne interopérabilité avec les VM AAC d'après ce que je peux voir.) exposait des références à des fonctions de rappel, que j'utiliserais pour mettre à jour mes Composables :

```kotlin
class ActiveGameViewModel {
    //...
    internal var subTimerState: ((Long) -> Unit)? = null
    internal var timerState: Long = 0L
    //...
    internal fun updateTimerState(){
        timerState++
        subTimerState?.invoke(timerState)
    }
//...
}
```

**Voici la partie importante !** Nous pouvons déclencher la recomposition de la Hiérarchie Compose en utilisant certaines fonctionnalités de compose, comme la fonction `remember` :

```kotlin
var timerState by remember {
    mutableStateOf("")
}
```

Si vous devez le savoir, ces fonctionnalités stockent l'état de ce que vous retenez dans la `slotTable`. En bref, le mot état ici signifie l'état actuel des données, qui commence par être simplement une chaîne vide.

**C'est là que j'ai tout gâché**. J'avais extrait mon simple composable de chronomètre dans sa propre fonction (appliqué SOC), et je passais `timerState` en tant que paramètre à ce composable.

Cependant, les extraits ci-dessus se trouvaient dans le composable parent du chronomètre, qui était un conteneur pour la partie la plus compliquée de l'interface utilisateur (un Sudoku 9x9 nécessite un grand nombre de widgets) :

```kotlin
@Composable
fun GameContent(
    onEventHandler: (ActiveGameEvent) -> Unit,
    viewModel: ActiveGameViewModel
) {
    Surface(
        Modifier
            .wrapContentHeight()
            .fillMaxWidth()
    ) {
        BoxWithConstraints(Modifier.background(MaterialTheme.colors.primary)) {
            //...
            ConstraintLayout {
                val (board, timer, diff, inputs) = createRefs()
                var isComplete by remember {
                    mutableStateOf(false)
                }
                var timerState by remember {
                    mutableStateOf("")
                }
                viewModel.subTimerState = {
                    timerState = it.toTime()
                }
                viewModel.subIsCompleteState = { isComplete = it }
            //...Plateau Sudoku
            //Chronomètre
                Box(Modifier
                    .wrapContentSize()
                    .constrainAs(timer) {
                        top.linkTo(board.bottom)
                        start.linkTo(parent.start)
                    }
                    .padding(start = 16.dp))
                {
                    TimerText(timerState)
                }
            //...affichage de la difficulté
            //...boutons d'entrée
            }
        }
    }
}
@Composable
fun TimerText(timerState: String) {
    Text(
        text = timerState,
        style = activeGameSubtitle.copy(color = MaterialTheme.colors.secondary)
    )
}
```

Cela causait un lag et une non-réactivité considérables. En utilisant abondamment le débogueur, j'ai pu découvrir pourquoi. Parce que ma variable `timerState` était créée et mise à jour à l'intérieur du Composable parent, elle déclenchait une recomposition de cette partie entière de l'interface utilisateur. **À chaque. Seconde. Tick.**

Après avoir déplacé le code approprié dans le composable `TimerText`, tout a fonctionné très doucement :

```kotlin
@Composable
fun TimerText(viewModel: ActiveGameViewModel) {
    var timerState by remember {
        mutableStateOf("")
    }

    viewModel.subTimerState = {
        timerState = it.toTime()
    }

    Text(
        text = timerState,
        style = activeGameSubtitle.copy(color = MaterialTheme.colors.secondary)
    )
}
```

Espérons que je vous ai donné une compréhension fonctionnelle de la recomposition et de l'une des plus grandes façons de la faire incorrectement.

Éviter les recompositions inutiles est incroyablement important pour les performances. Et jusqu'à présent, il semble que l'application rigoureuse de la SOC, même au point de garder l'état de rappel dans des composables séparés, devrait devenir une pratique standard.

# Ressources et Support

Si vous avez aimé cet article, veuillez le partager sur les réseaux sociaux et consulter mes autres articles sur [freeCodeCamp ici](https://www.freecodecamp.org/news/author/ryan-michael-kay/). J'ai aussi une [chaîne YouTube](https://youtube.com/wiseass) avec des centaines de tutoriels, et je suis un écrivain actif sur diverses plateformes.

### Connectez-vous avec moi sur les réseaux sociaux

Vous pouvez me trouver sur [Instagram ici](https://www.instagram.com/rkay301/) et sur [Twitter ici](https://twitter.com/wiseAss301).

De plus, je veux souligner la seule ressource que j'ai utilisée pour commencer avec Jetpack Compose : [Des exemples de code fonctionnel de bons développeurs](https://github.com/android/compose-samples).