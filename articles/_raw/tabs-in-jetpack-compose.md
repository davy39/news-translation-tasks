---
title: How to Create Tabs in Jetpack Compose
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2023-02-28T19:09:07.000Z'
originalURL: https://freecodecamp.org/news/tabs-in-jetpack-compose
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/chiara-f-MI8He1NWPWg-unsplash.jpg
tags:
- name: Jetpack Compose
  slug: jetpack-compose
seo_title: null
seo_desc: "We’ve all seen it.\nWe’ve all done it.\nAin’t nothing like good ol’ tabs\
  \ to organize content in a complex application. So how do we go about creating a\
  \ tab layout in Jetpack Compose? \nIn this tutorial, we’ll go over all of the basics,\
  \ but also show som..."
---

We’ve all seen it.

We’ve all done it.

Ain’t nothing like good ol’ tabs to organize content in a complex application. So how do we go about creating a tab layout in Jetpack Compose? 

In this tutorial, we’ll go over all of the basics, but also show some things that are more advanced.

## How to Create Simple Tabs

To create a tab layout, you need to start with a [**TabRow**](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,kotlin.Function0,kotlin.Function0)). This will be a container element that will hold your tabs.

```kotlin
@Composable
@UiComposable
fun TabRow(
    selectedTabIndex: Int,
    modifier: Modifier = Modifier,
    backgroundColor: Color = MaterialTheme.colors.primarySurface,
    contentColor: Color = contentColorFor(backgroundColor),
    indicator: @Composable @UiComposable (tabPositions: List<TabPosition>) -> Unit = @Composable { tabPositions ->
            TabRowDefaults.Indicator(
                Modifier.tabIndicatorOffset(tabPositions[selectedTabIndex])
            )
        },
    divider: @Composable @UiComposable () -> Unit = @Composable {
            TabRowDefaults.Divider()
        },
    tabs: @Composable @UiComposable () -> Unit
): Unit
```

* **selectedTabIndex** indicates the index of the tab that is currently selected
* **indicator** represents the UI that indicates which tab is currently selected
* **divider** is a composable that is drawn at the bottom of the TabRow under the indicator
* If you don’t have a need to custom style your tabs, you can use [**TabRowDefaults**](https://developer.android.com/reference/kotlin/androidx/compose/material/TabRowDefaults) as it contains the default values and implementation used for TabRow (you can see it being used inside divider)

Let’s see the usage of TabRow with an example. We will create a simple layout that will have three tabs:

1. Home
2. About
3. Settings

```kotlin
@Composable
fun TabScreen() {
    var tabIndex by remember { mutableStateOf(0) }

    val tabs = listOf("Home", "About", "Settings")

    Column(modifier = Modifier.fillMaxWidth()) {
        TabRow(selectedTabIndex = tabIndex) {
            tabs.forEachIndexed { index, title ->
                Tab(text = { Text(title) },
                    selected = tabIndex == index,
                    onClick = { tabIndex = index }
                )
            }
        }
        when (tabIndex) {
            0 -> HomeScreen()
            1 -> AboutScreen()
            2 -> SettingsScreen()
        }
    }
}
```

A couple things to pay attention to:

* The TabRow composable holds inside of itself a **Tab** composable
* After the TabRow composable, we have a when clause to handle what happens when each tab is clicked (in our specific case we are opening different screens)
* We are using a variable called tabIndex to keep track of which Tab is selected

![Image](https://www.freecodecamp.org/news/content/images/2023/02/1.jpg)

Pretty bland, right?

Let’s spice things up with icons by using the icon attribute of the Tab composable.

```kotlin
@Composable
fun TabScreen() {
    var tabIndex by remember { mutableStateOf(0) }

    val tabs = listOf("Home", "About", "Settings")

    Column(modifier = Modifier.fillMaxWidth()) {
        TabRow(selectedTabIndex = tabIndex) {
            tabs.forEachIndexed { index, title ->
                Tab(text = { Text(title) },
                    selected = tabIndex == index,
                    onClick = { tabIndex = index },
                    icon = {
                        when (index) {
                            0 -> Icon(imageVector = Icons.Default.Home, contentDescription = null)
                            1 -> Icon(imageVector = Icons.Default.Info, contentDescription = null)
                            2 -> Icon(imageVector = Icons.Default.Settings, contentDescription = null)
                        }
                    }
                )
            }
        }
        when (tabIndex) {
            0 -> HomeScreen()
            1 -> AboutScreen()
            2 -> SettingsScreen()
        }
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/1-1.jpg)

Looking better, but a question does arise: What if we have more tabs than the screen can show?

Luckily, the answer is simple.

There is an option to make our TabRow scrollable. Instead of using the TabRow element, you can use the [**ScrollableTabRow**](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#ScrollableTabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,kotlin.Function1,kotlin.Function0,kotlin.Function0)) composable.

```kotlin
@Composable
@UiComposable
fun ScrollableTabRow(
    selectedTabIndex: Int,
    modifier: Modifier = Modifier,
    backgroundColor: Color = MaterialTheme.colors.primarySurface,
    contentColor: Color = contentColorFor(backgroundColor),
    edgePadding: Dp = TabRowDefaults.ScrollableTabRowPadding,
    indicator: @Composable @UiComposable (tabPositions: List<TabPosition>) -> Unit = @Composable { tabPositions ->
            TabRowDefaults.Indicator(
                Modifier.tabIndicatorOffset(tabPositions[selectedTabIndex])
            )
        },
    divider: @Composable @UiComposable () -> Unit = @Composable {
            TabRowDefaults.Divider()
        },
    tabs: @Composable @UiComposable () -> Unit
): Unit
```

So if we convert our example from above, we will get this:

```kotlin
@Composable
fun TabScreen() {
    var tabIndex by remember { mutableStateOf(0) }

    val tabs = listOf("Home", "About", "Settings", "More", "Something", "Everything")

    Column(modifier = Modifier.fillMaxWidth()) {
        ScrollableTabRow(selectedTabIndex = tabIndex) {
            tabs.forEachIndexed { index, title ->
                Tab(text = { Text(title) },
                    selected = tabIndex == index,
                    onClick = { tabIndex = index },
                    icon = {
                        when (index) {
                            0 -> Icon(imageVector = Icons.Default.Home, contentDescription = null)
                            1 -> Icon(imageVector = Icons.Default.Info, contentDescription = null)
                            2 -> Icon(imageVector = Icons.Default.Settings, contentDescription = null)
                            3 -> Icon(imageVector = Icons.Default.Lock, contentDescription = null)
                            4 -> Icon(imageVector = Icons.Default.HeartBroken, contentDescription = null)
                            5 -> Icon(imageVector = Icons.Default.Star, contentDescription = null)
                        }
                    }
                )
            }
        }
        when (tabIndex) {
            0 -> HomeScreen()
            1 -> AboutScreen()
            2 -> SettingsScreen()
            3 -> MoreScreen()
            4 -> SomethingScreen()
            5 -> EverythingScreen()
        }
    }
}
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/2.gif)

## How to Create Tabs with Swiping Enabled

Scrollable tabs are nice, but swiping between tabs is even better. Most users will feel that it's more intuitive to swipe between the tabs rather than clicking on each one. If you look at the documentation, you will notice that there are a few options to go with:

1. The [swipeable](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#(androidx.compose.ui.Modifier).swipeable(androidx.compose.material.SwipeableState,kotlin.collections.Map,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function2,androidx.compose.material.ResistanceConfig,androidx.compose.ui.unit.Dp)) modifier
2. The [detectDragGestures](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectDragGestures(kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function2)) modifier
3. The [draggable](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).draggable(androidx.compose.foundation.gestures.DraggableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean,kotlin.coroutines.SuspendFunction2,kotlin.coroutines.SuspendFunction2,kotlin.Boolean)) modifier

Not all of these will help us in achieving our goal, each one for its own reasons. If you don’t want to go through the “hassle” of doing things yourself, there is a library from Accompanist called [pager](https://google.github.io/accompanist/pager/#usage) that you can use. It allows you to add the ability to either horizontally or vertically create a row/column that reacts to swipes.

Steps to implement it have been covered already and you can use the resources below to learn how to do it:

* [https://johncodeos.com/how-to-create-tabs-with-jetpack-compose/](https://johncodeos.com/how-to-create-tabs-with-jetpack-compose/)
* [https://www.rockandnull.com/jetpack-compose-swipe-pager/](https://www.rockandnull.com/jetpack-compose-swipe-pager/)

If you are like me and you like to do things for yourself and are up for getting your hands dirty, read on.

## Option 1: the `Swipeable` Modifier

The first thing to know about the swipeable modifier is that it is annotated with the @[**ExperimentalMaterialApi**](https://developer.android.com/reference/kotlin/androidx/compose/material/ExperimentalMaterialApi). This means that this API can change between versions of Jetpack Compose and that it isn’t stable. 

Apart from that, we need to go over the mechanism that the swipeable modifier uses. It has 3 building blocks:

1. A swipeable state – Denoting the current state and holding data about any on going swipe or swipe related animation.
2. Anchors – A map of values (Float based) restricting the swipe action from the minimum value to the maximum value. It maps anchor points to swipeable states.
3. Thresholds – A value denoting the difference between two known anchors.

```kotlin
@ExperimentalMaterialApi
fun <T : Any?> Modifier.swipeable(
    state: SwipeableState<T>,
    anchors: Map<Float, T>,
    orientation: Orientation,
    enabled: Boolean = true,
    reverseDirection: Boolean = false,
    interactionSource: MutableInteractionSource? = null,
    thresholds: (from, to) -> ThresholdConfig = { _, _ -> FixedThreshold(56.dp) },
    resistance: ResistanceConfig? = resistanceConfig(anchors.keys),
    velocityThreshold: Dp = VelocityThreshold
): Modifier
```

Regardless of this API being experimental, it just isn’t meant to be used for the swiping gesture we are seeking. 

You can. use this modifier for a switch button that the user can drag between on/off positions (as an example). But what would be our anchors in our example? How do we define the thresholds? The swipe a user performs cannot be constrained between two points. Therefore, we’ll let this one go and move on to detectDragGestures.

## Option 2: the `detectDragGestures` Modifier

As the name implies, this modifier detects the drag gesture, which can be quite similar to swiping.

```kotlin
suspend fun PointerInputScope.detectDragGestures(
    onDragStart: (Offset) -> Unit = { },
    onDragEnd: () -> Unit = { },
    onDragCancel: () -> Unit = { },
    onDrag: (change: PointerInputChange, dragAmount: Offset) -> Unit
): Unit
```

As you can see, the **onDrag** callback has two arguments:

1. `change` – of `PointerInputChange` type, denoting the change in pointer when dragging
2. `dragAmount` – of `Offset` type, denoting the amount dragged in x,y values

This callback is called when:

> _“… waits for pointer down and touch stop in any direction and then calls `onDrag` for each drag event.”_

The upside to use this modifier instead of the draggable one is that it provides you with information about the change in both x and y coordinates.

The downside of it is that it isn’t going to offer a smooth and elegant solution for swiping. This is because of the amount of times the onDrag callback is triggered. 

When a user performs a swipe gesture, the onDrag callback is triggered multiple times. This makes it harder to discern when the “drag” gesture has ended completely. 

When experimenting with this, I saw the onDrag callback being triggered three times for each swipe gesture. This won’t be a good fit for our use case so let’s check out the draggable modifier.

## Option 3: the `Draggable` Modifier

Think of this modifier as the stripped down version of the one before. This one measures changes in the UI when the user performs a drag gesture in only one orientation (vertical/horizontal). Since we only care about horizontal swipes, this can be a good option.

```kotlin
fun Modifier.draggable(
    state: DraggableState,
    orientation: Orientation,
    enabled: Boolean = true,
    interactionSource: MutableInteractionSource? = null,
    startDragImmediately: Boolean = false,
    onDragStarted: suspend CoroutineScope.(startedPosition: Offset) -> Unit = {},
    onDragStopped: suspend CoroutineScope.(velocity: Float) -> Unit = {},
    reverseDirection: Boolean = false
): Modifier
```

Here as well there is no similarity to the two other modifiers and we will point out the things to pay attention to:

* `state` – Similar to the state in the swipeable modifier, only here we are talking about a drag motion.
* `onDragStarted` – A callback triggered when the drag motion has begun.
* `onDragStopped` – A callback triggered when the drag motion has ended.

Unlike **`detectDragGestures`**, here `onDragStopped` is called once for every swipe gesture, making this modifier the best candidate for the job.

It’s implementation as a swipe gesture detector in our example is quite robust, so let’s start with some prerequisites:

1. We will be saving the index of the tab currently being viewed in a view model class
2. This index will be of `MutableLiveData` so that our composables will be able to recompose when the value is changed
3. Each of our screens will add the `draggable` modifier to its layout
4. We will need to add the runtime-livedata library as we are going to use the [`observeAsState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/livedata/package-summary#(androidx.lifecycle.LiveData).observeAsState(kotlin.Any)) method.

We will start with #4.

Go to your application’s build.gradle file and add the following dependency:

```
implementation "androidx.compose.runtime:runtime-livedata:$compose_version"
```

where **`$compose_version`** is the version of Jetpack Compose you are using.

We have also minimized our previous example to hold three screens instead of six, as the solution works for either case and there is no need to create extra boiler plate.

Below is the view model:

```kotlin
class MainViewModel(application: Application) : AndroidViewModel(application) {

    private val _tabIndex: MutableLiveData<Int> = MutableLiveData(0)
    val tabIndex: LiveData<Int> = _tabIndex
    val tabs = listOf("Home", "About", "Settings")

    fun updateTabIndexBasedOnSwipe(isSwipeToTheLeft: Boolean) {
        _tabIndex.value = when (isSwipeToTheLeft) {
            true -> Math.floorMod(_tabIndex.value!!.plus(1), tabs.size)
            false -> Math.floorMod(_tabIndex.value!!.minus(1), tabs.size)
        }
    }

    fun updateTabIndex(i: Int) {
        _tabIndex.value = i
    }

}
```

* **`tabIndex`** is in charge of holding the currently selected index.
* **`index`** is the exposed tabIndex.
* **`tabs`** is the list of tab names.
* The method **`updateTabIndexBasedOnSwipe`** is triggered when a swipe happens and performs the calculation of where to move the tabIndex to.

Each screen is made up of the same layout:

```kotlin
@Composable
fun AboutScreen(viewModel: MainViewModel) {

    var isSwipeToTheLeft by remember { mutableStateOf(false) }
    val dragState = rememberDraggableState(onDelta = { delta ->
        isSwipeToTheLeft = delta > 0
    })

    Column(modifier = Modifier.fillMaxSize().draggable(
        state = dragState,
        orientation = Orientation.Horizontal,
        onDragStarted = {  },
        onDragStopped = {
            viewModel.updateTabIndexBasedOnSwipe(isSwipeToTheLeft = isSwipeToTheLeft)
        }),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center) {
        Row(modifier = Modifier.align(Alignment.CenterHorizontally)) {
            Text(
                text = "About",
                textAlign = TextAlign.Center,
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold
            )
        }
    }
}
```

* **`isSwipeToTheLeft`** is a Boolean indicating the direction of the swipe.
* **`dragState`** holds the state of the drag being performed and updates isSwipeToTheLeft according to the delta.
* When the callback **`onDragStopped`** is called, we are calling the exposed viewModel method updateTabIndexBasedOnSwipe.

And finally, our `TabLayout`:

```kotlin
@Composable
fun TabLayout(viewModel: MainViewModel) {
    val tabIndex = viewModel.tabIndex.observeAsState()
    Column(modifier = Modifier.fillMaxWidth()) {
        TabRow(selectedTabIndex = tabIndex.value!!) {
            viewModel.tabs.forEachIndexed { index, title ->
                Tab(text = { Text(title) },
                    selected = tabIndex.value!! == index,
                    onClick = { viewModel.updateTabIndex(index) },
                    icon = {
                        when (index) {
                            0 -> Icon(imageVector = Icons.Default.Home, contentDescription = null)
                            1 -> Icon(imageVector = Icons.Default.Info, contentDescription = null)
                            2 -> Icon(imageVector = Icons.Default.Settings, contentDescription = null)
                        }
                    }
                )
            }
        }

        when (tabIndex.value) {
            0 -> HomeScreen(viewModel = viewModel)
            1 -> AboutScreen(viewModel = viewModel)
            2 -> SettingsScreen(viewModel = viewModel)
        }
    }
}
```

* Notice that when a tab is selected, we are updating the currently selected tab in the `viewModel` with **`updateTabIndex`**.

Putting it all together yields:

![Image](https://www.freecodecamp.org/news/content/images/2023/02/2-1.gif)

A few words regarding what we have accomplished. You might have noticed that there is some boilerplate we are adding for each of our screens that results in repetition. Each screen is saving the state of the drag. 

To improve on that, we can move the `draggableState` to the view model, like so:

```kotlin
class MainViewModel(application: Application) : AndroidViewModel(application) {

    private val _tabIndex: MutableLiveData<Int> = MutableLiveData(0)
    val tabIndex: LiveData<Int> = _tabIndex
    val tabs = listOf("Home", "About", "Settings")

    var isSwipeToTheLeft: Boolean = false
    private val draggableState = DraggableState { delta ->
        isSwipeToTheLeft= delta > 0
    }

    private val _dragState = MutableLiveData<DraggableState>(draggableState)
    val dragState: LiveData<DraggableState> = _dragState

    fun updateTabIndexBasedOnSwipe() {
        _tabIndex.value = when (isSwipeToTheLeft) {
            true -> Math.floorMod(_tabIndex.value!!.plus(1), tabs.size)
            false -> Math.floorMod(_tabIndex.value!!.minus(1), tabs.size)
        }
    }

    fun updateTabIndex(i: Int) {
        _tabIndex.value = i
    }

}
```

And that reduces the boilerplate a bit, since each screen now looks like:

```kotlin
@Composable
fun AboutScreen(viewModel: MainViewModel) {

    Column(modifier = Modifier.fillMaxSize().draggable(
        state = viewModel.dragState.value!!,
        orientation = Orientation.Horizontal,
        onDragStarted = {  },
        onDragStopped = {
            viewModel.updateTabIndexBasedOnSwipe()
        }),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center) {
        Row(modifier = Modifier.align(Alignment.CenterHorizontally)) {
            Text(
                text = "About",
                textAlign = TextAlign.Center,
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold
            )
        }
    }
}
```

I hope this article gave you the necessary tools to create your own tabs UI in Jetpack Compose. 

The example shown above can be found [here](https://github.com/TomerPacific/MediumArticles/tree/master/JetpackComposeTabs).

And if you would like to read other articles I have written, you can check them out [here](https://github.com/TomerPacific/MediumArticles).

References:

* [Material Design page about Tabs](https://m3.material.io/components/tabs/overview)
* [Gestures In Jetpack Compose](https://developer.android.com/jetpack/compose/touch-input/gestures)

