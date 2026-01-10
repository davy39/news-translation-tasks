---
title: How to Handle UI Events in Jetpack Compose
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
seo_title: null
seo_desc: 'In this short and practical article, we will talk about how to handle UI
  events in Jetpack Compose.

  In the old system, we used OnClickListeners and other interfaces. In Compose, we
  can take full advantage of Kotlin’s Sealed Classes, Function Types an...'
---

In this short and practical article, we will talk about how to handle UI events in Jetpack Compose.

In the old system, we used OnClickListeners and other interfaces. In Compose, we can take full advantage of Kotlin’s **Sealed Classes**, **Function Types** and **Lambda Expressions**.

If you do not know what a composable is, consider reading [this article which explains the fundamentals](https://www.freecodecamp.org/news/jetpack-compose-beginner-tutorial-composables-recomposition/).

%[https://youtu.be/LrNPw1LQHEw] 

## How to Model UI Events with a Sealed Class

First, we must learn what is meant by UI Events and how to model them with Sealed Classes.

I have described this same process for [Java and Kotlin](https://medium.com/swlh/simplify-your-ui-interactions-with-events-java-kotlin-any-language-5062c1b1e0e4) (with the old view system) before, so I will keep this brief.

### The Process

For each screen or sub-screen of your UI, ask yourself this question: What are all the different ways which the user can interact with it?

Let's take an example from my first app built fully in compose, [Graph Sudoku](https://play.google.com/store/apps/details?id=com.bracketcove.graphsudoku):

![Image](https://www.freecodecamp.org/news/content/images/2021/03/graph_sudoku_small_screen.png align="left")

*Screenshot of a Sudoku Android App*

The sealed class I use to represent the UI interactions of this screen looks like this:

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

To explain briefly:

* OnInput represents a user touching an input button (like 0, 1, 2, 3, 4)
    
* OnTileFocused represents a user selecting a tile (like the amber highlighted one)
    
* OnNewGameClicked is self-explanatory
    
* OnStart and OnStop are lifecycle events which my composables do not care about, but they are used in the Activity which acts as a Container for the composables
    

Once you have your sealed class set up, you can now handle a wide variety of events using a single event handler function. Sometimes it might make more sense to have multiple event handler functions, so keep in mind that **this approach must be adapted to your project's specific requirements**.

## How to Connect Your Software Architecture

What you have handling these events is totally up to you. Some people think that MVVM is the golden standard of software architectures, but it seems like more and more people are realizing that **there is no single architecture which works best for every situation**.

For Android with Compose, my current approach is to use a very 3rd party minimalist approach which typically has these things in each feature (screen):

* A (Presentation) Logic class **as an event handler**
    
* A ViewModel to store the data necessary to render the View (as the name implies)
    
* An Activity which acts as a Container (not a god object)
    
* Composables to form the View
    

![Image](https://www.freecodecamp.org/news/content/images/2021/03/model_view_whatever-3.png align="left")

*Model-View-Whatever*

I do not care what you use as long as you are applying [separation of concerns](https://youtu.be/B_C41SF0KbI). This is how I arrived at this architecture, by simply asking what should and should not be put together in the same class.

Whether you want your ViewModel, a Fragment, or an Activity to be your event handler, all of them can be set up the same way: **Function Types!**

Within your class of choice, set up an event handler function which accepts your sealed class as its argument:

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

This approach is very organized and makes it easy to test every Unit in this 3rd party library free class through a single entry point.

However, we are not done yet. Naturally, we need a way to get a reference to this event handler function, `onEvent`, to our Composables. We can do this using a **function reference**:

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

I am sure some of you are wondering why I am using an Activity. You can ask me during a [livestream Q&A sometime for a detailed answer](https://youtu.be/-xV8k-4UW50).

In short, Fragments appear to be a bit pointless with Compose with my approach to architecture (I do not use Jetpack Navigation), and there is nothing wrong with using Activities as a feature specific container. **Just avoid writing god activities, basically.**

To be specific, the way you make a reference to a function in Kotlin, is by providing the **class/interface name** (or **skip that if it is a Top-Level function**), followed by **two colons**, and the **name of the function without any arguments or brackets**:

```pgsql
onEventHandler = logic::onEvent
```

## How to Replace onClickListener With Jetpack Compose onClick Modifier

With that stuff ready, we can look at how this works within the composable. Naturally, your root composable will need the event handler function as a parameter:

```kotlin
@Composable
fun ActiveGameScreen(
    onEventHandler: (ActiveGameEvent) -> Unit,
    viewModel: ActiveGameViewModel
) {
//...
}
```

It can be a bit tricky to get function type syntax correctly, but understand that this **really is a reference to a function,** which is not so different from a reference to a class.

Just as you should not build god objects, you should not build giant composables:

1. Break your UI down into the **smallest reasonable parts**
    
2. Wrap them in a composable function
    
3. For each composable which has a UI interaction associated with it, **it must be given a reference to your event handler function**
    

Here is a composable which represents the input buttons of the Sudoku app, which is given the event handler by reference:

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

To actually pass the event to the logic class, we must use the `invoke` function, which will accept arguments as per the function type definition (which accepts an `ActiveGameEvent` in this case).

At this point, you are ready to handle UI interaction events in Kotlin (compose or not) by taking full advantage of this beautiful and modern programming language.

If you liked this article, share it on social media and consider checking out the resources below to support an independent programmer and content creator.

### Social

You can find me on [Instagram here](https://www.instagram.com/rkay301/) and on [Twitter here](https://twitter.com/wiseAss301).

### Here are some of my tutorials & courses

[https://youtube.com/wiseass](https://www.youtube.com/channel/UCSwuCetC3YlO1Y7bqVW5GHg) [https://www.freecodecamp.org/news/author/ryan-michael-kay/](https://www.freecodecamp.org/news/author/ryan-michael-kay/) [https://skl.sh/35IdKsj](https://skl.sh/35IdKsj) (introduction to Android with Android Studio)
