---
title: Comment styliser et thématiser une application avec Jetpack Compose
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
seo_title: Comment styliser et thématiser une application avec Jetpack Compose
seo_desc: 'In this article, we will learn how to style and theme an application in
  Jetpack Compose.

  Compose is a new UI framework for Android (though Desktop and Web support is being
  developed), which replaces the old XML-based View system.

  While still in beta ...'
---

Dans cet article, nous allons apprendre comment styliser et thématiser une application dans Jetpack Compose.

Compose est un nouveau framework d'interface utilisateur pour Android (bien que le support pour Desktop et Web soit en développement), qui remplace l'ancien système de vues basé sur XML.

Bien qu'encore en version bêta au moment de la rédaction de cet article, je ne m'attends pas à ce que cette partie particulière de la bibliothèque change radicalement pour la version stable.

Les sujets abordés incluent :

* Un bref rappel de l'approche XML

* Comment migrer depuis le système de couleurs, thèmes et typographie (police) basé sur XML

* Comment configurer des thèmes clairs et sombres pour vos applications en seulement quelques lignes de code

* Comment utiliser vos nouvelles informations de style basées sur Kotlin dans vos composables

* Comment styliser spécifiquement les composables Text

Avant de continuer, il est important que vous compreniez ce qu'est un composable. Je ne m'arrêterai pas pour expliquer ce concept ici, car je l'ai déjà fait dans [cet article](https://www.freecodecamp.org/news/jetpack-compose-beginner-tutorial-composables-recomposition/).

%[https://youtu.be/81r-vwPxlaw]

## Comment nous stylisions les applications Android en utilisant les ressources XML

Comme d'habitude, j'aime partager avec vous les motivations et un peu d'histoire sur ces sujets. Si cela ne vous intéresse pas, n'hésitez pas à passer à la section suivante où nous entrons dans le vif du sujet.

### Ressources Android

Le système de ressources des applications Android est quelque chose pour lequel l'équipe Android mérite une tape dans le dos, du moins à mon avis. Mais comme toute décision de conception, une fonctionnalité dans une situation devient un défaut dans une autre situation.

Pour être précis, l'un des plus grands défis pour les développeurs de plateformes et d'applications est de créer ce que j'appellerai des **ressources localisées**. Je fais référence au défi de construire des applications qui :

* Affichent du texte et des graphiques dans une variété de langues et d'alphabets différents

* Ont une apparence et une sensation proportionnées à une grande variété de facteurs de forme (dimensions, densités, etc.)

Ce ne sont là que deux exemples courants – il y en a beaucoup d'autres. Le système de ressources nous donne un endroit où les développeurs d'applications peuvent fournir des ressources localisées que la plateforme peut sélectionner au moment de la compilation. Cela nous évite d'avoir à écrire nous-mêmes ce code boilerplate.

### Fonctionnalité ou défaut ?

Bien que je ne veuille jamais gérer moi-même le code boilerplate nécessaire pour les ressources de chaînes localisées, cela ne signifie pas que j'aime écrire du XML.

En fait, **il y a très peu de choses que je préférerais faire en XML** plutôt que dans un langage moderne, idiomatique et élégant comme Kotlin ou Swift. Mis à part les préférences personnelles, il y a une raison plus technique pour laquelle les ressources XML ne sont pas toujours idéales.

Veuillez noter que cela n'est pas destiné à être une critique des développeurs/ingénieurs de la plateforme. Il s'agit simplement d'une observation sur la manière dont les décisions de conception ont toujours des avantages et des coûts.

Afin d'intégrer nos ressources basées sur XML dans notre code d'application basé sur la JVM, nous devons nécessairement avoir des **couches de traduction** (compilation) et des **ponts de plateforme** (API). Cela peut présenter des difficultés pour les développeurs de plateformes et d'applications.

Deux problèmes courants que j'ai rencontrés étaient :

* Je veux accéder à une ressource dans un endroit où je ne veux pas de couplage serré avec les API de la plateforme qui fournissent la ressource

* Je dois écrire un code boilerplate ridicule juste pour changer l'apparence d'une vue (c'est-à-dire remplacer quelque chose défini dans les styles et thèmes de ressources)

Le **problème racine** pour tous les concernés est le **couplage serré** avec le système de vues et le système de ressources Android (qui sont eux-mêmes étroitement couplés ensemble).

Pour les développeurs de plateformes, cela signifie qu'ils doivent construire sur ou contourner des bases de code gigantesques et anciennes. Ajoutez à cela qu'ils doivent également essayer de faire fonctionner de nouvelles fonctionnalités sur des versions plus anciennes du système d'exploitation Android, et cela devient un travail très ingrat.

Le résultat pour nous, développeurs d'applications, est le plus souvent beaucoup de **code boilerplate**, quelques **contournements** pour des choses qui intuitivement semblent être des one-liners. Sans parler du fait que l'API principale pour obtenir ces ressources est `Context`, qui est une classe que vous ne voulez vraiment pas fuiter en mémoire.

**Entrez Jetpack Compose.**

## Comment configurer les thèmes, les couleurs et les polices avec Jetpack Compose

Notre revue de l'ancien système étant terminée, explorons une méthode beaucoup plus belle et simple pour styliser et thématiser une application Android. J'ai dit que je garderais cela pratique, mais permettez-moi un point.

Puisque nous allons faire ce travail en Kotlin, cela signifie une chose très importante : nous et les développeurs de la plateforme sommes beaucoup moins liés par la traduction (compilation) et les ponts d'API (`R` class et `Context` d'Android) entre XML et la JVM.

En termes simples, cela signifie **beaucoup moins de code boilerplate**, et **beaucoup plus de contrôle à l'exécution**.

Pour la partie pratique de cet article, ma suggestion est de suivre ce processus dans l'ordre où je l'explique. Je l'ai structuré dans l'ordre que je suis lorsque j'écris ce code dans une nouvelle application.

### Comment remplacer les ressources Colors.xml par Kotlin Compose

Si vous n'avez pas encore décidé d'une palette de couleurs pour votre application, je vous suggère d'utiliser les diverses ressources disponibles sur le site officiel de Material Design. Essayez :

* Les [palettes de couleurs](https://material.io/design/color/the-color-system.html#tools-for-picking-colors)

* L'[outil de couleur](https://material.io/resources/color/)

Si vous prévoyez de supporter des thèmes d'application clairs et sombres (expliqué bientôt), essayez de sélectionner une palette de couleurs qui supporte le texte blanc et une palette de couleurs qui supporte le texte noir.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/color_text_palettes.png align="left")

*Exemple de palettes de couleurs claires et sombres.*

Créez un fichier appelé quelque chose comme [Color.kt](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/Color.kt) (le nom n'a pas d'importance) et remplissez-le avec des valeurs immuables **val** :

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

Vous pouvez soit utiliser une valeur prédéfinie comme `Color.Black` soit fournir votre propre valeur Hex ARGB.

Puisque ARGB Hex est juste un jargon pour décrire ce que diantre "`0XFF00bc00`" signifie, permettez-moi de traduire :

* Les deux premiers caractères `0x` indiquent au compilateur que ceci est un nombre hexadécimal

* Les deux caractères suivants, "`FF`" ou "`DC`", représentent la Transparence/Opacité/**A**lpha en Hex

* Les six paires de caractères restantes représentent le **R**ouge, le **V**ert et le **B**leu

### Comment ajouter des polices et remplacer l'attribut `fontFamily`

La typographie (polices) est également très facile à gérer. C'est le genre de chose où les [arguments par défaut](https://kotlinlang.org/docs/functions.html#default-arguments) de Kotlin sont très utiles.

Créez un fichier appelé quelque chose comme [Type.kt](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/Type.kt) (le nom n'a toujours pas d'importance) et créez une classe `Typography`...

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

...et quelques classes `TextStyle` :

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

Que vous fournissiez des fonctions ou des valeurs publiques (je déconseille d'utiliser `**var**` ici) dépend de vos préférences individuelles et de vos exigences actuelles.

### Comment créer un thème d'application dans Jetpack Compose

La dernière chose que vous devez configurer avant d'utiliser votre thème dans vos composables est un `MaterialTheme @Composable`. J'ai le mien, ainsi que mes palettes de couleurs claires et sombres dans un fichier appelé [GraphSudokuTheme](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/GraphSudokuTheme.kt) :

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
    //couleur de fond principale
    primary = primaryCharcoal,
    //utilisée pour la couleur du texte
    secondary = textColorDark,
    //fond du plateau sudoku
    surface = lightGreyAlpha,
    //lignes de grille du plateau sudoku
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

Puisque vous devriez déjà être familier avec ce qu'est un composable (je vous ai prévenu), la seule nouvelle chose ici est `darkTheme: Boolean = isSystemInDarkTheme()`.

Pour donner une explication simplifiée, `isSystemInDarkTheme()` est un appel qui demande à tout appareil Android compatible la préférence de l'utilisateur pour un thème clair ou sombre.

Il **retourne une valeur booléenne** que nous pouvons utiliser dans une expression d'affectation ternaire (conditionnelle) telle que `colors = if (darkTheme) DarkColorPalette else LightColorPalette`.

C'est tout. Couleurs, polices et deux thèmes définis en quelques minutes.

## Comment utiliser un thème dans Compose

Il est maintenant temps d'utiliser ce thème dans votre application. Dans cette application, qui ne contient que deux écrans principaux, j'utilise simplement une [Activity](https://github.com/BracketCove/GraphSudokuOpen/blob/master/app/src/main/java/com/bracketcove/graphsudoku/ui/activegame/ActiveGameActivity.kt) comme **conteneur** pour mes composables :

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

Où que vous trouviez à appeler `setContent {}`, ma suggestion pour les débutants est de placer immédiatement votre composable Theme à l'intérieur. Cela fera en sorte que les informations de style **cascadent/héritent à chaque composable imbriqué**.

Vous avez terminé ! Presque.

## Comment remplacer les styles et les thèmes

Si vous le pouvez, essayez d'inclure toutes les couleurs que vous voudrez dans vos palettes claires et sombres. Ainsi, lorsque vous appelez `MaterialTheme.colors.<Color>`, le système gérera la logique conditionnelle nécessaire pour choisir la palette appropriée :

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

Cependant, parfois il est plus approprié d'écrire votre propre logique conditionnelle... ou je suis juste devenu paresseux. Heureusement, Compose rend de nombreuses configurations disponibles en tant que propriétés :

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

`MaterialTheme.Colors.isLight` retourne un booléen indiquant le mode dans lequel ils se trouvent, puis nous pouvons utiliser une autre affectation ternaire à partir de là.

### Comment styliser un composable Text

Il suffit de définir l'argument `style` égal à l'un de vos styles de texte (qu'il provienne de `MaterialTheme` ou de l'un des styles dans `Type.kt`) :

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

`TextStyle` a sa propre fonction `copy` prête à l'emploi si vous devez remplacer quoi que ce soit.

Et c'est tout ! Vous savez maintenant comment styliser et thématiser une application en utilisant Jetpack Compose. Merci d'avoir lu :)

### **Social**

Vous pouvez me trouver sur [Instagram ici](https://www.instagram.com/rkay301/) et sur [Twitter ici](https://twitter.com/wiseAss301).

### **Voici quelques-uns de mes tutoriels et cours**

[https://youtube.com/wiseass](https://www.youtube.com/channel/UCSwuCetC3YlO1Y7bqVW5GHg) [https://www.freecodecamp.org/news/author/ryan-michael-kay/](https://www.freecodecamp.org/news/author/ryan-michael-kay/) [https://skl.sh/35IdKsj](https://skl.sh/35IdKsj) (introduction à Android avec Android Studio)