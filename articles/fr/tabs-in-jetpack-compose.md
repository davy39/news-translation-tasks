---
title: Comment créer des onglets dans Jetpack Compose
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
seo_title: Comment créer des onglets dans Jetpack Compose
seo_desc: "We’ve all seen it.\nWe’ve all done it.\nAin’t nothing like good ol’ tabs\
  \ to organize content in a complex application. So how do we go about creating a\
  \ tab layout in Jetpack Compose? \nIn this tutorial, we’ll go over all of the basics,\
  \ but also show som..."
---

Nous l'avons tous vu.

Nous l'avons tous fait.

Rien de tel que de bons vieux onglets pour organiser le contenu dans une application complexe. Alors, comment créer une disposition d'onglets dans Jetpack Compose ?

Dans ce tutoriel, nous allons passer en revue toutes les bases, mais aussi montrer quelques choses plus avancées.

## Comment créer des onglets simples

Pour créer une disposition d'onglets, vous devez commencer par un [**TabRow**](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#TabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,kotlin.Function1,kotlin.Function0,kotlin.Function0)). Cela sera un élément conteneur qui contiendra vos onglets.

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

* **selectedTabIndex** indique l'index de l'onglet actuellement sélectionné
* **indicator** représente l'UI qui indique quel onglet est actuellement sélectionné
* **divider** est un composable qui est dessiné en bas du TabRow sous l'indicateur
* Si vous n'avez pas besoin de styliser vos onglets de manière personnalisée, vous pouvez utiliser [**TabRowDefaults**](https://developer.android.com/reference/kotlin/androidx/compose/material/TabRowDefaults) car il contient les valeurs par défaut et l'implémentation utilisée pour TabRow (vous pouvez le voir utilisé dans divider)

Voyons l'utilisation de TabRow avec un exemple. Nous allons créer une disposition simple qui aura trois onglets :

1. Accueil
2. À propos
3. Paramètres

```kotlin
@Composable
fun TabScreen() {
    var tabIndex by remember { mutableStateOf(0) }

    val tabs = listOf("Accueil", "À propos", "Paramètres")

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

Quelques points à surveiller :

* Le composable TabRow contient à l'intérieur de lui-même un composable **Tab**
* Après le composable TabRow, nous avons une clause when pour gérer ce qui se passe lorsque chaque onglet est cliqué (dans notre cas spécifique, nous ouvrons différents écrans)
* Nous utilisons une variable appelée tabIndex pour suivre quel Tab est sélectionné

![Image](https://www.freecodecamp.org/news/content/images/2023/02/1.jpg)

Assez fade, n'est-ce pas ?

Ajoutons des icônes en utilisant l'attribut icon du composable Tab.

```kotlin
@Composable
fun TabScreen() {
    var tabIndex by remember { mutableStateOf(0) }

    val tabs = listOf("Accueil", "À propos", "Paramètres")

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

Cela semble mieux, mais une question se pose : que faire si nous avons plus d'onglets que l'écran ne peut en afficher ?

Heureusement, la réponse est simple.

Il existe une option pour rendre notre TabRow défilable. Au lieu d'utiliser l'élément TabRow, vous pouvez utiliser le composable [**ScrollableTabRow**](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#ScrollableTabRow(kotlin.Int,androidx.compose.ui.Modifier,androidx.compose.ui.graphics.Color,androidx.compose.ui.graphics.Color,androidx.compose.ui.unit.Dp,kotlin.Function1,kotlin.Function0,kotlin.Function0)).

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

Ainsi, si nous convertissons notre exemple ci-dessus, nous obtenons ceci :

```kotlin
@Composable
fun TabScreen() {
    var tabIndex by remember { mutableStateOf(0) }

    val tabs = listOf("Accueil", "À propos", "Paramètres", "Plus", "Quelque chose", "Tout")

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

## Comment créer des onglets avec le balayage activé

Les onglets défilables sont bien, mais balayer entre les onglets est encore mieux. La plupart des utilisateurs trouveront plus intuitif de balayer entre les onglets plutôt que de cliquer sur chacun. Si vous regardez la documentation, vous remarquerez qu'il y a quelques options à considérer :

1. Le modificateur [swipeable](https://developer.android.com/reference/kotlin/androidx/compose/material/package-summary#(androidx.compose.ui.Modifier).swipeable(androidx.compose.material.SwipeableState,kotlin.collections.Map,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Function2,androidx.compose.material.ResistanceConfig,androidx.compose.ui.unit.Dp))
2. Le modificateur [detectDragGestures](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.input.pointer.PointerInputScope).detectDragGestures(kotlin.Function1,kotlin.Function0,kotlin.Function0,kotlin.Function2))
3. Le modificateur [draggable](https://developer.android.com/reference/kotlin/androidx/compose/foundation/gestures/package-summary#(androidx.compose.ui.Modifier).draggable(androidx.compose.foundation.gestures.DraggableState,androidx.compose.foundation.gestures.Orientation,kotlin.Boolean,androidx.compose.foundation.interaction.MutableInteractionSource,kotlin.Boolean,kotlin.coroutines.SuspendFunction2,kotlin.coroutines.SuspendFunction2,kotlin.Boolean))

Toutes ces options ne nous aideront pas à atteindre notre objectif, chacune pour ses propres raisons. Si vous ne voulez pas passer par le "tracas" de faire les choses vous-même, il existe une bibliothèque d'Accompanist appelée [pager](https://google.github.io/accompanist/pager/#usage) que vous pouvez utiliser. Elle vous permet d'ajouter la capacité de créer une ligne/colonne qui réagit aux balayages, soit horizontalement, soit verticalement.

Les étapes pour l'implémenter ont déjà été couvertes et vous pouvez utiliser les ressources ci-dessous pour apprendre comment le faire :

* [https://johncodeos.com/how-to-create-tabs-with-jetpack-compose/](https://johncodeos.com/how-to-create-tabs-with-jetpack-compose/)
* [https://www.rockandnull.com/jetpack-compose-swipe-pager/](https://www.rockandnull.com/jetpack-compose-swipe-pager/)

Si vous êtes comme moi et que vous aimez faire les choses vous-même et que vous êtes prêt à vous retrousser les manches, continuez à lire.

## Option 1 : le modificateur `Swipeable`

La première chose à savoir sur le modificateur swipeable est qu'il est annoté avec @[**ExperimentalMaterialApi**](https://developer.android.com/reference/kotlin/androidx/compose/material/ExperimentalMaterialApi). Cela signifie que cette API peut changer entre les versions de Jetpack Compose et qu'elle n'est pas stable.

En dehors de cela, nous devons passer en revue le mécanisme que le modificateur swipeable utilise. Il a 3 blocs de construction :

1. Un état swipeable – Indiquant l'état actuel et contenant des données sur tout balayage en cours ou animation liée au balayage.
2. Ancre – Une carte de valeurs (basée sur Float) restreignant l'action de balayage de la valeur minimale à la valeur maximale. Il mappe les points d'ancrage aux états swipeable.
3. Seuil – Une valeur indiquant la différence entre deux ancres connues.

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

Malgré le fait que cette API soit expérimentale, elle n'est tout simplement pas destinée à être utilisée pour le geste de balayage que nous recherchons.

Vous pouvez utiliser ce modificateur pour un bouton de commutation que l'utilisateur peut faire glisser entre les positions on/off (par exemple). Mais quelles seraient nos ancres dans notre exemple ? Comment définissons-nous les seuils ? Le balayage effectué par l'utilisateur ne peut pas être contraint entre deux points. Par conséquent, nous allons laisser tomber celui-ci et passer à detectDragGestures.

## Option 2 : le modificateur `detectDragGestures`

Comme son nom l'indique, ce modificateur détecte le geste de glisser, qui peut être assez similaire au balayage.

```kotlin
suspend fun PointerInputScope.detectDragGestures(
    onDragStart: (Offset) -> Unit = { },
    onDragEnd: () -> Unit = { },
    onDragCancel: () -> Unit = { },
    onDrag: (change: PointerInputChange, dragAmount: Offset) -> Unit
): Unit
```

Comme vous pouvez le voir, le callback **onDrag** a deux arguments :

1. `change` – de type `PointerInputChange`, indiquant le changement de pointeur lors du glisser
2. `dragAmount` – de type `Offset`, indiquant la quantité glissée en valeurs x,y

Ce callback est appelé lorsque :

> "... attend l'appui du pointeur et l'arrêt du toucher dans n'importe quelle direction puis appelle `onDrag` pour chaque événement de glisser."

L'avantage d'utiliser ce modificateur plutôt que le draggable est qu'il vous fournit des informations sur le changement des coordonnées x et y.

L'inconvénient est qu'il n'offrira pas une solution fluide et élégante pour le balayage. Cela est dû au nombre de fois où le callback onDrag est déclenché.

Lorsque l'utilisateur effectue un geste de balayage, le callback onDrag est déclenché plusieurs fois. Cela rend plus difficile la détermination du moment où le geste de "glisser" s'est complètement terminé.

En expérimentant avec cela, j'ai vu le callback onDrag être déclenché trois fois pour chaque geste de balayage. Cela ne sera pas adapté à notre cas d'utilisation, alors vérifions le modificateur draggable.

## Option 3 : le modificateur `Draggable`

Considérez ce modificateur comme la version simplifiée de celui précédent. Celui-ci mesure les changements dans l'UI lorsque l'utilisateur effectue un geste de glisser dans une seule orientation (verticale/horizontale). Puisque nous nous intéressons uniquement aux balayages horizontaux, cela peut être une bonne option.

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

Ici aussi, il n'y a pas de similitude avec les deux autres modificateurs et nous allons souligner les points à surveiller :

* `state` – Similaire à l'état dans le modificateur swipeable, sauf qu'ici nous parlons d'un mouvement de glisser.
* `onDragStarted` – Un callback déclenché lorsque le mouvement de glisser a commencé.
* `onDragStopped` – Un callback déclenché lorsque le mouvement de glisser s'est terminé.

Contrairement à **`detectDragGestures`**, ici `onDragStopped` est appelé une fois pour chaque geste de balayage, ce qui fait de ce modificateur le meilleur candidat pour le travail.

Son implémentation en tant que détecteur de geste de balayage dans notre exemple est assez robuste, alors commençons par quelques prérequis :

1. Nous allons sauvegarder l'index de l'onglet actuellement affiché dans une classe de modèle de vue
2. Cet index sera de type `MutableLiveData` afin que nos composables puissent se recomposer lorsque la valeur est modifiée
3. Chacun de nos écrans ajoutera le modificateur `draggable` à sa disposition
4. Nous devrons ajouter la bibliothèque runtime-livedata car nous allons utiliser la méthode [`observeAsState`](https://developer.android.com/reference/kotlin/androidx/compose/runtime/livedata/package-summary#(androidx.lifecycle.LiveData).observeAsState(kotlin.Any)).

Nous allons commencer par le point #4.

Allez dans le fichier build.gradle de votre application et ajoutez la dépendance suivante :

```
implementation "androidx.compose.runtime:runtime-livedata:$compose_version"
```

où **`$compose_version`** est la version de Jetpack Compose que vous utilisez.

Nous avons également minimisé notre exemple précédent pour contenir trois écrans au lieu de six, car la solution fonctionne pour les deux cas et il n'est pas nécessaire de créer du code supplémentaire.

Voici le modèle de vue :

```kotlin
class MainViewModel(application: Application) : AndroidViewModel(application) {

    private val _tabIndex: MutableLiveData<Int> = MutableLiveData(0)
    val tabIndex: LiveData<Int> = _tabIndex
    val tabs = listOf("Accueil", "À propos", "Paramètres")

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

* **`tabIndex`** est responsable de la conservation de l'index actuellement sélectionné.
* **`index`** est l'index tabIndex exposé.
* **`tabs`** est la liste des noms d'onglets.
* La méthode **`updateTabIndexBasedOnSwipe`** est déclenchée lorsqu'un balayage se produit et effectue le calcul de l'endroit où déplacer l'index tabIndex.

Chaque écran est composé de la même disposition :

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
                text = "À propos",
                textAlign = TextAlign.Center,
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold
            )
        }
    }
}
```

* **`isSwipeToTheLeft`** est un booléen indiquant la direction du balayage.
* **`dragState`** contient l'état du glisser en cours et met à jour isSwipeToTheLeft en fonction du delta.
* Lorsque le callback **`onDragStopped`** est appelé, nous appelons la méthode updateTabIndexBasedOnSwipe exposée par le viewModel.

Et enfin, notre `TabLayout` :

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

* Remarquez que lorsqu'un onglet est sélectionné, nous mettons à jour l'onglet actuellement sélectionné dans le `viewModel` avec **`updateTabIndex`**.

En mettant tout cela ensemble, nous obtenons :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/2-1.gif)

Quelques mots sur ce que nous avons accompli. Vous avez peut-être remarqué qu'il y a un certain code répétitif que nous ajoutons pour chacun de nos écrans, ce qui entraîne des répétitions. Chaque écran sauvegarde l'état du glisser.

Pour améliorer cela, nous pouvons déplacer le `draggableState` vers le modèle de vue, comme ceci :

```kotlin
class MainViewModel(application: Application) : AndroidViewModel(application) {

    private val _tabIndex: MutableLiveData<Int> = MutableLiveData(0)
    val tabIndex: LiveData<Int> = _tabIndex
    val tabs = listOf("Accueil", "À propos", "Paramètres")

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

Et cela réduit un peu le code répétitif, puisque chaque écran ressemble maintenant à ceci :

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
                text = "À propos",
                textAlign = TextAlign.Center,
                fontSize = 20.sp,
                fontWeight = FontWeight.Bold
            )
        }
    }
}
```

J'espère que cet article vous a donné les outils nécessaires pour créer votre propre interface d'onglets dans Jetpack Compose.

L'exemple montré ci-dessus peut être trouvé [ici](https://github.com/TomerPacific/MediumArticles/tree/master/JetpackComposeTabs).

Et si vous souhaitez lire d'autres articles que j'ai écrits, vous pouvez les consulter [ici](https://github.com/TomerPacific/MediumArticles).

Références :

* [Page Material Design sur les onglets](https://m3.material.io/components/tabs/overview)
* [Gestures In Jetpack Compose](https://developer.android.com/jetpack/compose/touch-input/gestures)