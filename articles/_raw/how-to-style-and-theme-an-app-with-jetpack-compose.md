---
title: How to Style and Theme an App With Jetpack Compose
subtitle: ''
author: Ryan Michael Kay
co_authors: []
series: null
date: '2021-03-22T13:48:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-style-and-theme-an-app-with-jetpack-compose
coverImage: https://cdn-media-2.freecodecamp.org/w1280/6054c45f687d62084bf67e41.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Kotlin
  slug: kotlin
- name: UI Design
  slug: ui-design
- name: User Interface
  slug: user-interface
seo_title: null
seo_desc: 'In this article, we will learn how to style and theme an application in
  Jetpack Compose.

  Compose is a new UI framework for Android (though Desktop and Web support is being
  developed), which replaces the old XML-based View system.

  While still in beta ...'
---

In this article, we will learn how to style and theme an application in Jetpack Compose.

Compose is a new UI framework for Android (though Desktop and Web support is being developed), which replaces the old XML-based View system.

While still in beta release as of writing this article, I do not expect this particular part of the library to change drastically for the stable release.

Topics include:

* A brief recap of the XML approach
    
* How to migrate from the XML-based colors, themes, and typography (font) system
    
* How to set up light and dark themes for your apps in only a few lines of code
    
* How to use your new Kotlin-based style information in your composables
    
* How to style Text Composables specifically
    

Before proceeding, it is important that you understand what a composable is. I will not be stopping to explain that concept here, as I already have in [this article](https://www.freecodecamp.org/news/jetpack-compose-beginner-tutorial-composables-recomposition/).

%[https://youtu.be/81r-vwPxlaw] 

## How We Used to Style Android Apps Using XML Resources

As usual, I like to share with you the motivations behind, and a bit of history on, these topics. In case you do not care, feel free to skip to the next section where we get into the practical stuff.

### Android Resources

The Android app resources system is something which the Android team deserves a high five for, at least in my opinion. But like every design decision, a feature in one situation becomes a flaw in another situation.

To be specific, one of the greatest challenges for both platform and application developers alike is to create what I will call **localized resources**. I am referring to the challenge of building apps which:

* Display text and graphics in a variety of different languages and alphabets
    
* Look and feel proportionate to a wide variety of form factors (dimensions, densities, and so on.)
    

Those are just two common examples – there are plenty more. The resource system gives us a place where app developers can provide localized resources which the platform can select for at compile time. This saves us having to write that boilerplate code ourselves.

### Feature or Flaw?

While I would never want to manage the boilerplate code necessary for localized string resources myself, that does not mean I enjoy writing XML.

In fact, **there are very few things I would prefer to do in XML** over a modern, idiomatic, and elegant language such as Kotlin or Swift. Personal preference aside, there is a more technical reason why XML resources are not always ideal.

Please note that this is not meant as a criticism of the platform developers/engineers. It is merely an observation of how design decisions always have benefits and costs.

In order to integrate our XML-based resources into our JVM-based application code, we must necessarily have **layers of translation** (compilation) and **platform bridges** (APIs). This can present difficulties for both platform and application developers.

Two common problems I ran into were:

* I want access to a resource in a place where I do not want tight coupling to the platform APIs which provide the resource
    
* I have to write some ridiculous boilerplate code just to change the look of a View (that is, override something defined within resource styles and themes)
    

The **root problem** for everyone involved is **tight coupling** to the View system and the Android resource system (which are themselves tightly coupled together).

For the platform developers, this means they have to build on top of, or work around gigantic and old codebases. Add that they must also try to have new features work on older Android OS versions, and that becomes a very thankless job.

The result for us application developers is most often a lot of **boilerplate code,** some **hacky workarounds** for things which intuitively seem like they should be one-liners. Not to mention the main API for getting these resources is `Context`, which is a class you really do not want to leak in memory.

**Enter Jetpack Compose.**

## How to Set Up Themes, Colors, and Fonts with Jetpack Compose

With our review of the old system out of the way, let's explore a much prettier and simpler way to style and theme an Android application. I said I would keep this practical, but allow one point.

Since we will be doing that work in Kotlin, it means one very important thing: Both we and the platform developers are much less bound by translation (compilation) and API bridges (Android's `R` class and `Context`) between XML and the JVM.

In simple terms, this means **much less boilerplate code**, and **much more control at runtime**.

For the practical part of this article, my suggestion to you is to follow this process in the order I explain it. I have structured it in the order I follow when writing this code in a new App.

### How to Replace Colors.xml Resources with Kotlin Compose

If you have not already decided upon a color scheme for your application, I suggest that you use the various resources available on the official Material Design website. Try out:

* The [color palettes](https://material.io/design/color/the-color-system.html#tools-for-picking-colors)
    
* The [color tool](https://material.io/resources/color/)
    

If you plan to support light and dark app themes (explained shortly), try to select a color scheme which supports white text and a color scheme which supports black text.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/color_text_palettes.png align="left")

*Example of light and dark color schemes.*

Create a file called something like [Color.kt](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/Color.kt) (the name does not matter) and fill it with immutable **val**ues:

```kotlin
import androidx.compose.ui.graphics.Color

val primaryGreen = Color(0XFF00bc00)
val primaryCharcoal = Color(0xFF2b2b2b)
val accentAmber = Color(0xFFffe400)

val textColorLight = Color(0xDCFFFFFF)
val textColorDark = Color(0xFFf3f3f3)
val gridLineColorLight = Color.Black
//...
```

You can either use a predefined value like `Color.Black` or supply your own ARGB Hex value.

Since ARGB Hex is just a bunch of jargon to describe what the heck "`0XFF00bc00`" means, let me translate:

* First two characters `0x` tell the compiler that this is a hexadecimal number
    
* Second two characters , "`FF`" or "`DC`", represent Transparency/Opaqueness/**A**lpha in Hex
    
* The remaining six character pairs represent **R**ed, **G**reen, and **B**lue
    

### How to Add Fonts and Replace the `fontFamily` Attribute

Typography (fonts) is also very easy to manage. This is the kind of thing where Kotlin's [default arguments](https://kotlinlang.org/docs/functions.html#default-arguments) are very useful.

Create a file called something like [Type.kt](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/Type.kt) (the name still does not matter) and create `Typography` class...:

```kotlin
val typography = Typography(
    body1 = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp
    ),

    button = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Bold,
        fontSize = 32.sp
    ),

    caption = TextStyle(
        fontFamily = FontFamily.Default,
        fontWeight = FontWeight.Normal,
        fontSize = 12.sp
    )
)
//...
```

...and some `TextStyle` classes:

```kotlin
//...
val mainTitle = TextStyle(
    fontFamily = FontFamily.Default,
    fontWeight = FontWeight.Light,
    fontSize = 48.sp,
    textAlign = TextAlign.Center
)

fun dropdownText(color: Color) = TextStyle(
    fontFamily = FontFamily.Default,
    fontWeight = FontWeight.Normal,
    fontSize = 32.sp,
    textAlign = TextAlign.Center,
    color = color
)
//...
```

Whether you provide public functions or values (I advise against using `**var**` here) is up to your individual preference and current requirements.

### How to Create an App Theme in Jetpack Compose

The last thing you need to configure before using your theme in your composables is a `MaterialTheme @Composable`. I have mine, and along with my light and dark color palettes in a file called [GraphSudokuTheme](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/GraphSudokuTheme.kt):

```kotlin
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material.MaterialTheme
import androidx.compose.material.darkColors
import androidx.compose.material.lightColors
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val LightColorPalette = lightColors(
    primary = primaryGreen,
    secondary = textColorLight,
    surface = lightGrey,
    primaryVariant = gridLineColorLight,
    onPrimary = accentAmber,
    onSurface = accentAmber
)

private val DarkColorPalette = darkColors(
    //main background color
    primary = primaryCharcoal,
    //used for text color
    secondary = textColorDark,
    //background of sudoku board
    surface = lightGreyAlpha,
    //grid lines of sudoku board
    primaryVariant = gridLineColorLight,
    onPrimary = accentAmber,

    onSurface = accentAmber

)

@Composable
fun GraphSudokuTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {

    MaterialTheme(
        colors = if (darkTheme) DarkColorPalette else LightColorPalette,
        typography = typography,
        shapes = shapes,
        content = content
    )
}
```

Since you should already be familiar with what a composable is (I gave you fair warning), the only new thing here is `darkTheme: Boolean = isSystemInDarkTheme()`.

To give a simplified explanation, `isSystemInDarkTheme()` is a call which asks any compatible Android device for the user's preference of a light or dark theme.

It **returns a boolean value** which we can use in a Ternary (Conditional) Assignment expression such as `colors = if (darkTheme) DarkColorPalette else LightColorPalette`.

That is actually it. Colors, Fonts, and two Themes defined in a few minutes.

## How to Use a Theme in Compose

It is now time to use this Theme in your app. In this app, which only has two primary screens, I just use an [Activity](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/activegame/ActiveGameActivity.kt) as a **container** for my composables:

```pgsql
class NewGameActivity : AppCompatActivity(), NewGameContainer {
	//...
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
		//...

        setContent {
            GraphSudokuTheme {
                NewGameScreen(
                    onEventHandler = logic::onEvent,
                    viewModel
                )
            }
        }
		//...
    }
```

Wherever you find yourself calling `setContent {}`, my suggestion for beginners is to immediately place your Theme composable inside of it. Doing so will cause the style information to **cascade/inherit to each nested composable**.

You are done! Almost.

## How to Override Styles and Themes

If you can help it, try to include any colors you will want in your light and dark palettes. This way, when you call `MaterialTheme.colors.<Color>`, the system will handle the conditional logic necessary to pick the appropriate palette:

```pgsql
@Composable
fun NewGameContent(
    onEventHandler: (NewGameEvent) -> Unit,
    viewModel: NewGameViewModel
) {
    Surface(
        Modifier
            .wrapContentHeight()
            .fillMaxWidth()
    ) {
        ConstraintLayout(Modifier.background(MaterialTheme.colors.primary)) { 
        	//...
        }
        //...
      }
}
```

However, sometimes it is more suitable to write your own conditional logic...or I just got lazy. Fortunately Compose makes many such configurations available as properties:

```pgsql
@Composable
fun DoneIcon(onEventHandler: (NewGameEvent) -> Unit) {
    Icon(
        imageVector = Icons.Filled.Done,
        tint = if (MaterialTheme.colors.isLight) textColorLight 
        else textColorDark,
        contentDescription = null,
        modifier = Modifier
            .clickable(
            //...
            )
    )
}
```

`MaterialTheme.Colors.isLight` returns a boolean indicating what mode they are in, then we can use another Ternary Assignment from there.

### How to Style a Text Composable

Just set the `style` argument equal to one of your text styles (whether it comes from `MaterialTheme` or one of the styles within `Type.kt`):

```kotlin
Text(
    text = stat.toTime(),
    style = statsLabel.copy(
        color = if (isZero) Color.White
        else MaterialTheme.colors.onPrimary,
    fontWeight = FontWeight.Normal
    ),
    modifier = Modifier
        .wrapContentSize()
        .padding(end = 2.dp, bottom = 4.dp),
        textAlign = TextAlign.End
)
```

`TextStyle` has its own `copy` function ready to go should you need to overwrite anything.

And that's it! You now know how to style and theme an application using Jetpack Compose. Thanks for reading :)

### **Social**

You can find me on [Instagram here](https://www.instagram.com/rkay301/) and on [Twitter here](https://twitter.com/wiseAss301).

### **Here are some of my tutorials & courses**

[https://youtube.com/wiseass](https://www.youtube.com/channel/UCSwuCetC3YlO1Y7bqVW5GHg) [https://www.freecodecamp.org/news/author/ryan-michael-kay/](https://www.freecodecamp.org/news/author/ryan-michael-kay/) [https://skl.sh/35IdKsj](https://skl.sh/35IdKsj) (introduction to Android with Android Studio)
