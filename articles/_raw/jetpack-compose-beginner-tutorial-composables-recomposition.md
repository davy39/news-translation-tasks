---
title: A Jetpack Compose Tutorial for Beginners – How To Understand Composables &
  Recomposition
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
seo_title: null
seo_desc: 'This tutorial will teach you a few fundamental concepts and terms related
  to the Jetpack Compose UI Library on Android.

  While this is a beginner''s guide to Compose, it will not be a beginner''s guide
  to Android – so you should have built at least an a...'
---

This tutorial will teach you a few fundamental concepts and terms related to the Jetpack Compose UI Library on Android.

While this is a beginner's guide to Compose, it will not be a beginner's guide to Android – so you should have built at least an application or two (though not in Compose, necessarily).

Before we begin, I was initially planning to write a follow up article directed towards more senior developers until I came across Leland Richardson’s [two part article series](https://medium.com/androiddevelopers/understanding-jetpack-compose-part-1-of-2-ca316fe39050). Leland is not only a Software Engineer working on the Jetpack Compose team, but I see that he is a great writer as well.

While I feel my article will stand on its own as an introduction to the basics of Jetpack Compose, I **strongly suggest** you read his articles once you have gained some practical experience with Compose (or right away if you prefer to learn that way).

%[https://youtu.be/ijwBr4oeX0I] 

### Key Terms/Concepts Explained in this article:

* A brief review of the old View System and Hierarchy
    
* Composables and how they stand in relation to Views
    
* Recomposition and how to avoid doing it very poorly!
    

# What Is A Composable?

In this section, we will discuss the most fundamental part of the Jetpack Compose library. If you are a seasoned Android developer, you may wish to skip to the sub-section titled “Are Composables Views?”

If you are not already familiar with the View system, you should read the next section as it is necessary to motivate and understand what a Composable is.

## View Hierarchy

In the context of the Android SDK (the libraries we use to make user interfaces on this platform), a View is what we use to give structure and style to our applications.

It is the most fundamental kind of building block or element of a given user interface (UI), and each of these building blocks will contain the following kinds of information (among other things):

* X and Y start and end positions which tell the computer where to draw the view on the device screen
    
* Color and alpha (transparency) values
    
* Font information, text, symbols, and images
    
* Behaviour based on events such as user interaction (clicks) or changes in the application’s data (more on that later)
    

It is important to understand that **a View can be something like a button** (commonly referred to as a “widget”), **but it can also be a container of the whole screen, part of the screen, or for other child Views**.

Such **containers** are commonly referred to as Layouts or Viewgroups depending on the context. And, while sharing most of the same kinds of information as a widget, they also contain information about how to arrange and display other Views which are **nested** within them.

With that in mind, we get to the important part of this review of the View system: The **View Hierarchy**. For Web Developers, the View Hierarchy is essentially Android’s version of the Document Object Model (DOM).

For Android Developers, you can think of the View Hierarchy as a virtual representation of all the Views which you defined either in XML files or programmatically in Java or Kotlin.

To illustrate this, let's look at such an XML file (there’s no need to study it closely, just note the names). Then, using a debugger/stepper tool, we will look at what it looks like in the memory space of the Fragment which inflates this file:

**fragment\_hour\_view.xml:**

```xml
<?xml version=”1.0" encoding=”utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android=”http://schemas.android.com/apk/res/android"
android:layout_width=”match_parent”
android:layout_height=”match_parent”
android:id=”@+id/root_hour_view_fragment”
xmlns:app=”http://schemas.android.com/apk/res-auto"
>
<androidx.compose.ui.platform.ComposeView
android:id=”@+id/tlb_hour_view”
//...
 />
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id=”@+id/vqht_one”
//...
/>
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id=”@+id/vqht_two”
//...
/>
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id=”@+id/vqht_three”
//...
/>
<com.wiseassblog.samsaradayplanner.ui.managehourview.HourToggleView
android:id=”@+id/vqht_four”
//...
/>
</androidx.constraintlayout.widget.ConstraintLayout>
```

**Memory Space of (Fragment)HourView.kt:**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-22.png align="left")

*Image of a View Hierarchy*

The debugger and stepper tools are some of my favourite ways to learn about what is going on under the hood of the code that I use from various libraries. Give it a try some time!

The purpose of showing you this XML file and what it turns into in a **process** (a process is **simply a program that is running** on a device), is to demonstrate how nested Views in an XML file translate into a nested View Hierarchy at runtime.

Hopefully, with a simple but concrete model of how the old system works, we can compare it with the new one.

## Are Composables Views?

This was one of the first questions I asked when I started working with Compose, and the answer I have arrived at is both **yes** and **no**.

**Yes**, in the sense that a Composable fulfills the **same conceptual role as a View** in the old system. A Composable can be a widget like a button, or a container such as a ConstraintLayout (it is worth noting that there is a Composable implementation of ConstraintLayout available).

**No**, in the sense that the UI is no longer represented virtually in a View Hierarchy (apart from situations involving interoperability). With that being said, compose does not use magic to virtually represent and keep track of the UI. This means that it must have its own thing which is conceptually similar to a View Hierarchy.

Let us take a very brief look at this thing. Here, we have an Activity which uses the `setContent {…}` function to bind a Composable to itself:

**ActiveGameActivity.kt:**

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
//…
}
```

**ActiveGameScreen.kt:**

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
              //content
            }
        }
    }
}
```

In Compose, the View Hierarchy is replaced with something that we can locate if we dig really deeply into the **mWindow** field of this Activity. Within that field is the conceptual replacement of the View Hierarchy: **The** `**Composer**` **and its** `**slotTable**`**.**

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-26.png align="left")

At this point, if you want a detailed overview of the `Composer` and its `slotTable`, I must again suggest that you read Leland’s article (he goes into detail in [part 2](https://medium.com/androiddevelopers/under-the-hood-of-jetpack-compose-part-2-of-2-37b2c20c6cdd)). There is more to the Compose Hierarchy than the Composer and its slotTable, but that should be sufficient to get us started.

In general terms, Jetpack Compose uses what we might call its Compose Hierarchy (which is made of, and managed by things like the Composer and its slotTable).

Again, this is the same conceptual idea as the View hierarchy, a bunch of objects in memory space which collectively represent the UI, but it is implemented very differently.

There's an important difference, though, which is tricky to understand technically, but easy to understand in principle. This is the way in which Compose handles updates to the Compose Hierarchy: **Recomposition**.

# Recomposition: How To Update Compose UI

For my ESL friends, the word Compose comes from the latin *componere*, which roughly means “to put together.” Someone who writes music is often called a “Composer,” which can be thought of as the one who puts together the notes coming from one or more instruments into a composition (song).

Putting together implies that there are individual pieces. It's important to understand that almost any good software developer makes at least some effort to break their code down into the **smallest reasonable parts**.

I mention **reasonable**, because I think principles like DRY (Don’t Repeat Yourself) should be followed only to the extent that they solve more problems than they create.

There are many benefits to applying this concept, which is often called modularity, (or as I prefer, Separation of Concerns, or SOC). I am aware that some of you reading this might think I am just copying what Leland said in his article, but I have been talking about SOC as the Golden Principle Of Software Architecture for [many years already](https://rkay301.medium.com/programming-fundamentals-part-5-separation-of-concerns-software-architecture-f04a900a7c50).

Where this plays into Compose, is the same principle which we see in the popular Javascript library **React**. When done properly, Compose will only “recompose” (redraw, re-render, update, whatever) the Composables (parts/elements of the UI) which need to be recomposed.

This is ENORMOUSLY important when it comes to the performance of an application. This is because redrawing the UI, whether in the old View system or in Compose, is costly for system resources.

In case you were not aware, the entire purpose of the old RecyclerView (which was the first thing I ever made a tutorial on back in 2016!) was to employ the ViewHolder pattern to a list of data. This avoided the need to constantly inflate (make) new Views for each list item.

My goal in this article was to focus mostly on the theory, as I will be writing plenty of practical content over the next few months. However, I will finish the article off with a story from my direct experience, which will help you to further understand how recomposition works, and **how to avoid doing it very poorly!**

# The Stopwatch Example

For my first full Compose application, I decided to build Sudoku. There are a number of reasons why, including the fact that I wanted a project which did not have an insanely complicated UI. I also wanted the chance to deep dive into Graph DS and Algos, which are quite suitable for Sudoku puzzles.

One thing I wanted was a Stopwatch which would keep track of how long it took the user to complete a puzzle:

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-27.png align="left")

*Graph Sudoku puzzle*

As is often the case in my profession, I expected this timer to be much easier to add than it really was. I messed around with Android’s Chronometer class as well as the Java Timer class, and both of them presented different but still application-breaking problems.

Eventually I took a step back and realized that I was writing in Kotlin. So I set up a Coroutine based timer in my presentation logic class (it ended up making the most sense to put it there), which would update my viewmodel each second:

```kotlin
Class ActiveGameLogic(…):…{
//…
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
//…
}
```

The ViewModel (not from AAC – I write my own VMs. But Compose already has good interoperability with AAC VMs from what I can see.) exposed references to callback functions, which is what I would use to update my Composables:

```kotlin
class ActiveGameViewModel {
    //…
    internal var subTimerState: ((Long) -> Unit)? = null
    internal var timerState: Long = 0L
    //…
    internal fun updateTimerState(){
        timerState++
        subTimerState?.invoke(timerState)
    }
//…
}
```

**Now comes the important part!** We can trigger recomposition of the Compose Hierarchy by using certain features of compose, such as the `remember` function:

```kotlin
var timerState by remember {
    mutableStateOf(“”)
}
```

If you must know, these features store the state of whatever you are remembering in the `slotTable`. In short, the word state here means the current “state” of the data, which starts out being just an empty String.

**Here is where I screwed things up**. I had pulled my simple timer composable into its own function (applied SOC), and I was passing in `timerState` as a parameter to that composable.

However, the above snippets were sitting in the parent composable of the timer, which was a container for the most complicated portion of the UI (a 9x9 Sudoku requires a large number of widgets):

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
            //…
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
            //…Sudoku board
            //Timer
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
            //…difficulty display
            //…Input buttons
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

This was causing some considerable lag and unresponsiveness. By making heavy usage of the debugger, I was able to find out why. Because my `timerState` variable was created and updated inside the parent Composable, it was triggering a recomposition of that entire portion of the UI. **Every. Single. Tick.**

After moving the appropriate code into the `TimerText` composable, things worked very smoothly:

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

Hopefully I have given you a working understanding of recomposition and one of the biggest ways to do it incorrectly.

Avoiding unnecessary recompositions is incredibly important for performance. And so far it seems that applying SOC rigorously, even to the point of keeping remember state in separate composables, should become standard practice.

# Resources & Support

If you liked this article, please share it on social media and check out my other articles on [freeCodeCamp here](https://www.freecodecamp.org/news/author/ryan-michael-kay/). I also have a [YouTube channel](https://youtube.com/wiseass) with hundreds of tutorials, and am an active writer on various platforms.

### Connect with me on social media

You can find me on [Instagram here](https://www.instagram.com/rkay301/) and on [Twitter here](https://twitter.com/wiseAss301).

Also, I want to point out the single resource I used to get started with Jetpack Compose: [Working code samples from good developers](https://github.com/android/compose-samples).
