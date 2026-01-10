---
title: Comment gérer les événements UI dans Jetpack Compose
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2021-03-16T18:22:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-ui-events-in-jetpack-compose
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/cat-4793068_1280-5.jpg
tags:
- name: Android
  slug: android
- name: Android Studio
  slug: android-studio
- name: Jetpack Compose
  slug: jetpack-compose
- name: Kotlin
  slug: kotlin
- name: UI
  slug: ui
- name: User Interface
  slug: user-interface
seo_title: Comment gérer les événements UI dans Jetpack Compose
seo_desc: 'In this short and practical article, we will talk about how to handle UI
  events in Jetpack Compose.

  In the old system, we used OnClickListeners and other interfaces. In Compose, we
  can take full advantage of Kotlin’s Sealed Classes, Function Types an...'
---

Dans cet article court et pratique, nous allons parler de la façon de gérer les événements UI dans Jetpack Compose.

Dans l'ancien système, nous utilisions des OnClickListeners et d'autres interfaces. Dans Compose, nous pouvons tirer pleinement parti des **classes scellées** de Kotlin, des **types de fonction** et des **expressions lambda**.

Si vous ne savez pas ce qu'est un composable, envisagez de lire [cet article qui explique les fondamentaux](https://www.freecodecamp.org/news/jetpack-compose-beginner-tutorial-composables-recomposition/).

%[https://youtu.be/LrNPw1LQHEw]

## Comment modéliser les événements UI avec une classe scellée

Tout d'abord, nous devons apprendre ce que l'on entend par événements UI et comment les modéliser avec des classes scellées.

J'ai décrit ce même processus pour [Java et Kotlin](https://medium.com/swlh/simplify-your-ui-interactions-with-events-java-kotlin-any-language-5062c1b1e0e4) (avec l'ancien système de vue) auparavant, donc je vais garder cela bref.

### Le processus

Pour chaque écran ou sous-écran de votre UI, posez-vous cette question : Quelles sont toutes les différentes façons dont l'utilisateur peut interagir avec lui ?

Prenons un exemple de ma première application construite entièrement en compose, [Graph Sudoku](https://play.google.com/store/apps/details?id=com.bracketcove.graphsudoku) :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/graph_sudoku_small_screen.png align="left")

*Capture d'écran d'une application Android Sudoku*

La classe scellée que j'utilise pour représenter les interactions UI de cet écran ressemble à ceci :

```kotlin
sealed class ActiveGameEvent {
    data class OnInput(val input: Int) : ActiveGameEvent()
    data class OnTileFocused(val x: Int, 
    val y: Int) : ActiveGameEvent()
    object OnNewGameClicked : ActiveGameEvent()
    object OnStart : ActiveGameEvent()
    object OnStop : ActiveGameEvent()
}
```

Pour expliquer brièvement :

* OnInput représente un utilisateur touchant un bouton d'entrée (comme 0, 1, 2, 3, 4)

* OnTileFocused représente un utilisateur sélectionnant une tuile (comme celle en surbrillance ambrée)

* OnNewGameClicked est auto-explicatif

* OnStart et OnStop sont des événements de cycle de vie dont mes composables ne se soucient pas, mais ils sont utilisés dans l'Activity qui agit comme un conteneur pour les composables

Une fois que vous avez votre classe scellée configurée, vous pouvez maintenant gérer une grande variété d'événements en utilisant une seule fonction de gestionnaire d'événements. Parfois, il peut être plus judicieux d'avoir plusieurs fonctions de gestionnaire d'événements, alors gardez à l'esprit que **cette approche doit être adaptée aux exigences spécifiques de votre projet**.

## Comment connecter votre architecture logicielle

Ce que vous avez pour gérer ces événements dépend entièrement de vous. Certaines personnes pensent que MVVM est le standard d'excellence des architectures logicielles, mais il semble que de plus en plus de personnes réalisent que **il n'y a pas une seule architecture qui fonctionne mieux pour chaque situation**.

Pour Android avec Compose, mon approche actuelle est d'utiliser une approche minimaliste très tierce qui a généralement ces éléments dans chaque fonctionnalité (écran) :

* Une classe de logique (Présentation) **en tant que gestionnaire d'événements**

* Un ViewModel pour stocker les données nécessaires au rendu de la vue (comme le nom l'indique)

* Une Activity qui agit comme un conteneur (pas un objet dieu)

* Des composables pour former la vue

![Image](https://www.freecodecamp.org/news/content/images/2021/03/model_view_whatever-3.png align="left")

*Modèle-Vue-Quoi que ce soit*

Je ne me soucie pas de ce que vous utilisez tant que vous appliquez la [séparation des préoccupations](https://youtu.be/B_C41SF0KbI). C'est ainsi que je suis arrivé à cette architecture, simplement en me demandant ce qui devrait et ne devrait pas être mis ensemble dans la même classe.

Que vous souhaitiez que votre ViewModel, un Fragment ou une Activity soit votre gestionnaire d'événements, tous peuvent être configurés de la même manière : **Types de fonction !**

Au sein de votre classe de choix, configurez une fonction de gestionnaire d'événements qui accepte votre classe scellée comme argument :

```kotlin
class ActiveGameLogic(
    private val container: ActiveGameContainer?,
    private val viewModel: ActiveGameViewModel,
    private val gameRepo: IGameRepository,
    private val statsRepo: IStatisticsRepository,
    dispatcher: DispatcherProvider
) : BaseLogic<ActiveGameEvent>(dispatcher),
    CoroutineScope {
    //...
    override fun onEvent(event: ActiveGameEvent) {
        when (event) {
            is ActiveGameEvent.OnInput -> onInput(
                event.input,
                viewModel.timerState
            )
            ActiveGameEvent.OnNewGameClicked -> onNewGameClicked()
            ActiveGameEvent.OnStart -> onStart()
            ActiveGameEvent.OnStop -> onStop()
            is ActiveGameEvent.OnTileFocused -> onTileFocused(event.x, event.y)
        }
    }
    //...
}
```

Cette approche est très organisée et facilite le test de chaque unité dans cette classe libre de bibliothèque tierce à travers un seul point d'entrée.

Cependant, nous n'avons pas encore terminé. Naturellement, nous avons besoin d'un moyen d'obtenir une référence à cette fonction de gestionnaire d'événements, `onEvent`, pour nos composables. Nous pouvons le faire en utilisant une **référence de fonction** :

```kotlin
class ActiveGameActivity : AppCompatActivity(), ActiveGameContainer {
    private lateinit var logic: ActiveGameLogic

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        val viewModel = ActiveGameViewModel()

        setContent {
            ActiveGameScreen(
                onEventHandler = logic::onEvent,
                viewModel
            )
        }

        logic = buildActiveGameLogic(this, viewModel, applicationContext)
    }

  	//...
}
```

Je suis sûr que certains d'entre vous se demandent pourquoi j'utilise une Activity. Vous pouvez me demander pendant un [Q&A en direct pour une réponse détaillée](https://youtu.be/-xV8k-4UW50).

En bref, les Fragments semblent être un peu inutiles avec Compose avec mon approche d'architecture (je n'utilise pas Jetpack Navigation), et il n'y a rien de mal à utiliser des Activities comme un conteneur spécifique à une fonctionnalité. **Évitez simplement d'écrire des activités dieu, c'est tout.**

Pour être précis, la façon dont vous faites référence à une fonction en Kotlin est en fournissant le **nom de la classe/interface** (ou **sautez cela si c'est une fonction de niveau supérieur**), suivi de **deux points**, et le **nom de la fonction sans aucun argument ou parenthèses** :

```pgsql
onEventHandler = logic::onEvent
```

## Comment remplacer onClickListener par le modificateur onClick de Jetpack Compose

Avec cela prêt, nous pouvons voir comment cela fonctionne dans le composable. Naturellement, votre composable racine aura besoin de la fonction de gestionnaire d'événements comme paramètre :

```kotlin
@Composable
fun ActiveGameScreen(
    onEventHandler: (ActiveGameEvent) -> Unit,
    viewModel: ActiveGameViewModel
) {
//...
}
```

Il peut être un peu délicat d'obtenir la syntaxe du type de fonction correctement, mais comprenez que cela **est vraiment une référence à une fonction**, ce qui n'est pas si différent d'une référence à une classe.

Tout comme vous ne devriez pas construire des objets dieu, vous ne devriez pas construire des composables géants :

1. Décomposez votre UI en les **plus petites parties raisonnables**

2. Enveloppez-les dans une fonction composable

3. Pour chaque composable qui a une interaction UI associée, **il doit être donné une référence à votre fonction de gestionnaire d'événements**

Voici un composable qui représente les boutons d'entrée de l'application Sudoku, auquel est donnée la référence du gestionnaire d'événements :

```kotlin
@Composable
fun SudokuInputButton(
    onEventHandler: (ActiveGameEvent) -> Unit,
    number: Int
) {
    Button(
        onClick = { onEventHandler.invoke(ActiveGameEvent.OnInput(number)) },
        modifier = Modifier
            .requiredSize(56.dp)
            .padding(2.dp)
    ) {
        Text(
            text = number.toString(),
            style = inputButton.copy(color = MaterialTheme.colors.onPrimary),
            modifier = Modifier.fillMaxSize()
        )
    }
}
```

Pour transmettre réellement l'événement à la classe de logique, nous devons utiliser la fonction `invoke`, qui acceptera les arguments selon la définition du type de fonction (qui accepte un `ActiveGameEvent` dans ce cas).

À ce stade, vous êtes prêt à gérer les événements d'interaction UI en Kotlin (compose ou non) en tirant pleinement parti de ce langage de programmation moderne et magnifique.

Si vous avez aimé cet article, partagez-le sur les réseaux sociaux et envisagez de consulter les ressources ci-dessous pour soutenir un programmeur indépendant et créateur de contenu.

### Social

Vous pouvez me trouver sur [Instagram ici](https://www.instagram.com/rkay301/) et sur [Twitter ici](https://twitter.com/wiseAss301).

### Voici quelques-uns de mes tutoriels et cours

[https://youtube.com/wiseass](https://www.youtube.com/channel/UCSwuCetC3YlO1Y7bqVW5GHg) [https://www.freecodecamp.org/news/author/ryan-michael-kay/](https://www.freecodecamp.org/news/author/ryan-michael-kay/) [https://skl.sh/35IdKsj](https://skl.sh/35IdKsj) (introduction à Android avec Android Studio)