---
title: Une introduction aux principes SOLID
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-22T23:43:35.000Z'
originalURL: https://freecodecamp.org/news/kriptofolio-app-series-part-1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zl4KIqJJhbnroDJh-y3_AQ.png
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: Cryptocurrency
  slug: cryptocurrency
- name: Kotlin
  slug: kotlin
- name: 'tech '
  slug: tech
seo_title: Une introduction aux principes SOLID
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 1

  Software is always in a state of change. Each change can have a negative impact
  on a whole project. So the essential thing is to prevent damage that can be done
  while implementing all new changes.

  W...'
---

Par Andrius Baruckis

#### Série d'applications Kriptofolio - Partie 1

Le logiciel est toujours en état de changement. Chaque changement peut avoir un impact négatif sur l'ensemble du projet. L'essentiel est donc de prévenir les dommages qui peuvent être causés lors de la mise en œuvre de tous les nouveaux changements.

Avec l'application « Kriptofolio » (anciennement « My Crypto Coins »), je vais créer beaucoup de nouveau code étape par étape et je veux commencer à le faire de manière efficace. Je veux que mon projet soit de qualité solide. Tout d'abord, nous devons comprendre les principes fondamentaux de la création de logiciels modernes. Ils sont appelés principes SOLID. Un nom si accrocheur ! ?

### Contenu de la série

* [Introduction : Une feuille de route pour construire une application Android moderne en 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* Partie 1 : Une introduction aux principes SOLID (vous êtes ici)
* [Partie 2 : Comment commencer à construire votre application Android : création de maquettes, UI et mises en page XML](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* [Partie 3 : Tout sur cette architecture : exploration de différents modèles d'architecture et comment les utiliser dans votre application](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* [Partie 4 : Comment implémenter l'injection de dépendances dans votre application avec Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* [Partie 5 : Gérer les services Web RESTful en utilisant Retrofit, OkHttp, Gson, Glide et Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### Slogan des principes

**SOLID** est un acronyme mnémotechnique. Il aide à définir les cinq principes de base de la conception orientée objet :

1. **S**ingle Responsibility Principle (Principe de responsabilité unique)
2. **O**pen-Closed Principle (Principe ouvert-fermé)
3. **L**iskov Substitution Principle (Principe de substitution de Liskov)
4. **I**nterface Segregation Principle (Principe de ségrégation des interfaces)
5. **D**ependency Inversion Principle (Principe d'inversion des dépendances)

Ensuite, nous allons discuter de chacun d'eux individuellement. Pour chacun, je vais fournir des exemples de code mauvais vs bons. Ces exemples sont écrits pour Android en utilisant le langage Kotlin.

### Principe de responsabilité unique

> _Une classe ne doit avoir qu'une seule responsabilité._

Chaque classe ou module doit être responsable d'une partie de la fonctionnalité fournie par l'application. Ainsi, lorsqu'elle gère une chose, il doit y avoir une seule raison principale de la modifier. Si votre classe ou module fait plus d'une chose, alors vous devez séparer les fonctionnalités en classes distinctes.

Pour mieux comprendre ce principe, je prendrais comme exemple un couteau suisse. Ce couteau est bien connu pour ses multiples fonctions en plus de sa lame principale. Il a d'autres outils intégrés, tels que des tournevis, un ouvre-boîte, et bien d'autres.

La question naturelle ici pour vous est pourquoi je suggère ce couteau comme exemple pour une fonctionnalité unique ? Mais réfléchissez-y un moment. L'autre caractéristique principale de ce couteau est la mobilité tout en étant de taille poche. Donc, même s'il offre quelques fonctions différentes, il remplit toujours son objectif principal d'être assez petit pour l'emporter confortablement avec vous.

Les mêmes règles s'appliquent à la programmation. Lorsque vous créez votre classe ou module, elle doit avoir un objectif global principal. En même temps, vous ne pouvez pas en faire trop en essayant de simplifier trop les choses en séparant la fonctionnalité. Donc, souvenez-vous, gardez l'équilibre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m1OGuBK5fYZM1Lof6GkH3Q.jpeg)

Un exemple classique pourrait être la méthode souvent utilisée `onBindViewHolder` lors de la construction de l'adaptateur de widget RecyclerView.

? EXEMPLE DE MAUVAIS CODE :

```kotlin
class MusicVinylRecordRecyclerViewAdapter(private val vinyls: List<VinylRecord>, private val itemLayout: Int) 
 : RecyclerView.Adapter<MusicVinylRecordRecyclerViewAdapter.ViewHolder>() {
    ...
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val vinyl = vinyls[position]
        holder.itemView.tag = vinyl

        holder.title!!.text = vinyl.title
        holder.author!!.text = vinyl.author
        holder.releaseYear!!.text = vinyl.releaseYear
        holder.country!!.text = vinyl.country
        holder.condition!!.text = vinyl.condition

        /**
         * Ici, la méthode viole le Principe de Responsabilité Unique !!!
         * Malgré sa responsabilité principale et unique d'adapter un objet VinylRecord
         * à sa représentation visuelle, elle effectue également le formatage des données.
         * Elle a plusieurs raisons d'être modifiée à l'avenir, ce qui est incorrect.
         */

        var genreStr = ""
        for (genre in vinyl.genres!!) {
            genreStr += genre + ", "
        }
        genreStr = if (genreStr.isNotEmpty())
            genreStr.substring(0, genreStr.length - 2)
        else
            genreStr

        holder.genre!!.text = genreStr
    }
    ...
}
```

? EXEMPLE DE BON CODE :

```kotlin
class MusicVinylRecordRecyclerViewAdapter(private val vinyls: List<VinylRecord>, private val itemLayout: Int) 
 : RecyclerView.Adapter<MusicVinylRecordRecyclerViewAdapter.ViewHolder>() {
    ...
    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val vinyl = vinyls[position]
        holder.itemView.tag = vinyl

        holder.title!!.text = vinyl.title
        holder.author!!.text = vinyl.author
        holder.releaseYear!!.text = vinyl.releaseYear
        holder.country!!.text = vinyl.country
        holder.condition!!.text = vinyl.condition
        
        /**
         * Au lieu d'effectuer des opérations de formatage de données ici, nous déplaçons cette responsabilité
         * vers une autre classe. En fait, ici vous ne voyez qu'un appel direct à la fonction de niveau supérieur
         * convertArrayListToString - une nouvelle fonctionnalité du langage Kotlin. Cependant, ne vous trompez pas,
         * car le compilateur Kotlin derrière les scènes va toujours créer une classe Java, et
         * ensuite les fonctions de niveau supérieur individuelles seront converties en méthodes statiques. Donc une
         * responsabilité unique pour chaque classe.
         */

        holder.genre!!.text =  convertArrayListToString(vinyl.genres)
    }
    ...
}
```

Le code spécifiquement conçu avec le Principe de Responsabilité Unique à l'esprit sera proche des autres principes que nous allons discuter.

### Principe ouvert-fermé

> _Les entités logicielles doivent être ouvertes à l'extension, mais fermées à la modification._

Ce principe stipule que lorsque vous écrivez toutes les parties logicielles comme les classes, les modules et les fonctions, vous devez les rendre ouvertes à l'extension mais fermées à toute modification. Que signifie cela ?

Disons que nous créons une classe fonctionnelle. Il ne devrait pas être nécessaire de modifier cette classe si nous devons ajouter une nouvelle fonctionnalité ou effectuer certains changements. Au lieu de cela, nous devrions pouvoir étendre cette classe en créant sa nouvelle sous-classe où nous pourrions facilement ajouter toutes les nouvelles fonctionnalités nécessaires. Les fonctionnalités doivent toujours être paramétrées de manière à ce qu'une sous-classe puisse les remplacer.

Prenons un exemple où nous allons créer une classe spéciale `FeedbackManager` pour afficher un type différent de message personnalisé pour l'utilisateur.

? EXEMPLE DE MAUVAIS CODE :

```kotlin
class MainActivity : AppCompatActivity() {

    lateinit var feedbackManager: FeedbackManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        feedbackManager = FeedbackManager(findViewById(android.R.id.content));
    }

    override fun onStart() {
        super.onStart()

        feedbackManager.showToast(CustomToast())
    }
}

class FeedbackManager(var view: View) {

    // Imaginez que nous devons ajouter un nouveau type de message de feedback. Que se passerait-il ?
    // Nous devrions modifier cette classe de gestionnaire. Mais pour suivre le Principe Ouvert-Fermé, nous
    // devons écrire un code qui peut s'adapter automatiquement aux nouvelles exigences sans
    // réécrire les anciennes classes.

    fun showToast(customToast: CustomToast) {
        Toast.makeText(view.context, customToast.welcomeText, customToast.welcomeDuration).show()
    }

    fun showSnackbar(customSnackbar: CustomSnackbar) {
        Snackbar.make(view, customSnackbar.goodbyeText, customSnackbar.goodbyeDuration).show()
    }
}

class CustomToast {

    var welcomeText: String = "Hello, this is toast message!"
    var welcomeDuration: Int = Toast.LENGTH_SHORT
}

class CustomSnackbar {

    var goodbyeText: String = "Goodbye, this is snackbar message.."
    var goodbyeDuration: Int = Toast.LENGTH_LONG
}
```

? EXEMPLE DE BON CODE :

```kotlin
class MainActivity : AppCompatActivity() {

    lateinit var feedbackManager: FeedbackManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        feedbackManager = FeedbackManager(findViewById(android.R.id.content));
    }

    override fun onStart() {
        super.onStart()

        feedbackManager.showSpecialMessage(CustomToast())
    }
}

class FeedbackManager(var view: View) {

    // Encore la même situation - nous devons ajouter un nouveau type de message de feedback. Nous devons écrire un code
    // qui peut s'adapter aux nouvelles exigences sans changer l'implémentation de l'ancienne classe.
    // Ici, la solution est de se concentrer sur l'extension de la fonctionnalité en utilisant des interfaces et cela
    // suit le Principe Ouvert-Fermé.

    fun showSpecialMessage(message: Message) {
        message.showMessage(view)
    }
}

interface Message {
    fun showMessage(view: View)
}

class CustomToast: Message {

    var welcomeText: String = "Hello, this is toast message!"
    var welcomeDuration: Int = Toast.LENGTH_SHORT

    override fun showMessage(view: View) {
        Toast.makeText(view.context, welcomeText, welcomeDuration).show()
    }
}

class CustomSnackbar: Message {

    var goodbyeText: String = "Goodbye, this is snackbar message.."
    var goodbyeDuration: Int = Toast.LENGTH_LONG

    override fun showMessage(view: View) {
        Snackbar.make(view, goodbyeText, goodbyeDuration).show()
    }
}
```

Le principe ouvert-fermé résume les objectifs des deux principes suivants dont je parle ci-dessous. Alors passons à eux.

### Principe de substitution de Liskov

> _Les objets dans un programme doivent être remplaçables par des instances de leurs sous-types sans altérer la justesse de ce programme._

Ce principe porte le nom de [Barbara Liskov](https://en.wikipedia.org/wiki/Barbara_Liskov) — une informaticienne accomplie. L'idée générale de ce principe est que les objets doivent être remplaçables par des instances de leurs sous-types sans changer le comportement du programme.

Disons que dans votre application vous avez `MainClass` qui dépend de `BaseClass`, qui étend `SubClass`. En bref, pour suivre ce principe, votre code `MainClass` et votre application en général doivent fonctionner de manière transparente sans aucun problème lorsque vous décidez de changer l'instance `BaseClass` en instance `SubClass`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*72oYWBRb9y7HgiE-KkMQGw.png)

Pour mieux comprendre ce principe, laissez-moi vous donner un exemple classique et facile à comprendre avec l'héritage de `Square` et `Rectangle`.

? EXEMPLE DE MAUVAIS CODE :

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val rectangleFirst: Rectangle = Rectangle()
        rectangleFirst.width = 2
        rectangleFirst.height = 3

        textViewRectangleFirst.text = rectangleFirst.area().toString()
        // Le résultat de la première aire de rectangle est 6, ce qui est correct car 2 x 3 = 6.

        // Le Principe de Substitution de Liskov stipule qu'une sous-classe (Square) doit remplacer
        // la classe parente (Rectangle) de manière à ne pas rompre la fonctionnalité du point de vue
        // des consommateurs. Voyons cela.
        val rectangleSecond: Rectangle = Square()
        // L'utilisateur suppose que c'est un rectangle et essaie de définir la largeur et la hauteur comme d'habitude
        rectangleSecond.width = 2
        rectangleSecond.height = 3

        textViewRectangleSecond.text = rectangleSecond.area().toString()
        // Le résultat attendu du deuxième rectangle devrait être 6 à nouveau, mais au lieu de cela, il est 9.
        // Comme vous le voyez, cette approche orientée objet pour Square étendant Rectangle est incorrecte.
    }
}

open class Rectangle {

    open var width: Int = 0
    open var height: Int = 0

    open fun area(): Int {
        return width * height
    }
}

class Square : Rectangle() {

    override var width: Int
        get() = super.width
        set(width) {
            super.width = width
            super.height = width
        }

    override var height: Int
        get() = super.height
        set(height) {
            super.width = height
            super.height = height
        }
}
```

? EXEMPLE DE BON CODE :

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Ici, il est présenté une manière d'organiser ces classes Rectangle et Square pour mieux
        // respecter le Principe de Substitution de Liskov. Plus de résultat inattendu.
        val rectangleFirst: Shape = Rectangle(2,3)
        val rectangleSecond: Shape = Square(3)

        textViewRectangleFirst.text = rectangleFirst.area().toString()
        textViewRectangleSecond.text = rectangleSecond.area().toString()
    }
}

class Rectangle(var width: Int, var height: Int) : Shape() {

    override fun area(): Int {
        return width * height
    }
}

class Square(var edge: Int) : Shape() {

    override fun area(): Int {
        return edge * edge
    }
}

abstract class Shape {
    abstract fun area(): Int
}
```

Réfléchissez toujours avant d'écrire votre hiérarchie. Comme vous le voyez dans cet exemple, les objets de la vie réelle ne correspondent pas toujours aux mêmes classes OOP. Vous devez trouver une approche différente.

### Principe de ségrégation des interfaces

> _Plusieurs interfaces spécifiques au client sont meilleures qu'une interface générale._

Même le nom semble compliqué, mais le principe lui-même est assez facile à comprendre. Il stipule qu'un client ne doit jamais être forcé de dépendre de méthodes ou d'implémenter une interface qu'il n'utilise pas. Une classe doit être conçue pour avoir le moins de méthodes et d'attributs possible. Lors de la création d'une interface, essayez de ne pas la rendre trop grande. Au lieu de cela, divisez-la en interfaces plus petites afin que le client de l'interface ne connaisse que les méthodes qui sont pertinentes.

Pour comprendre l'idée de ce principe, j'ai à nouveau créé des exemples de code mauvais vs bons avec des robots papillons et humanoïdes. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*bogaw0ohgybpgEchiGSsLw.jpeg)

? EXEMPLE DE MAUVAIS CODE :

```kotlin
/**
 * Imaginons que nous créons un robot indéfini. Nous décidons de créer une interface avec toutes
 * les fonctions possibles.
 */
interface Robot {
    fun giveName(newName: String)
    fun reset()
    fun fly()
    fun talk()
}

/**
 * Tout d'abord, nous créons un robot papillon qui implémente cette interface.
 */
class ButterflyRobot : Robot {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Appelle la commande de réinitialisation pour le robot. Tout logiciel de robot doit pouvoir être réinitialisé.
        // C'est raisonnable et nous allons l'implémenter.
        TODO("not implemented")
    }

    override fun fly() {
        // Appelle la commande de vol pour le robot. Il s'agit d'une fonctionnalité spécifique de notre robot papillon.
        // Nous allons définitivement implémenter cela.
        TODO("not implemented")
    }

    override fun talk() {
        // Appelle la commande de parole pour le robot.
        // MAUVAIS !!! Notre robot papillon ne va pas parler, juste voler ! Pourquoi devons-nous implémenter cela ?
        // Ici, il y a une violation du Principe de Ségrégation des Interfaces car nous sommes forcés d'implémenter
        // une méthode que nous n'allons pas utiliser.
        TODO("???")
    }
}

/**
 * Ensuite, nous créons un robot humanoïde qui doit être capable d'effectuer des actions similaires à celles d'un humain et il
 * implémente également la même interface.
 */
class HumanoidRobot : Robot {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Appelle la commande de réinitialisation pour le robot. Tout logiciel de robot doit pouvoir être réinitialisé.
        // C'est raisonnable et nous allons l'implémenter.
        TODO("not implemented")
    }

    override fun fly() {
        // Appelle la commande de vol pour le robot.
        // C'est le problème ! Nous n'avons jamais eu l'intention que notre robot humanoïde vole.
        // Ici, il y a une violation du Principe de Ségrégation des Interfaces car nous sommes forcés d'implémenter
        // une méthode que nous n'allons pas utiliser.
        TODO("???")
    }

    override fun talk() {
        // Appelle la commande de parole pour le robot. Il s'agit d'une fonctionnalité spécifique de notre robot humanoïde.
        // Nous allons définitivement implémenter cela.
        TODO("not implemented")
    }
}
```

? EXEMPLE DE BON CODE :

```kotlin
/**
 * Imaginons que nous créons un robot indéfini. Nous devons créer une interface générique avec toutes
 * les fonctions possibles communes à tous les types de robots.
 */
interface Robot {
    fun giveName(newName: String)
    fun reset()
}

/**
 * Les robots spécifiques qui peuvent voler doivent avoir leur propre interface définie.
 */
interface Flyable {
    fun fly()
}

/**
 * Les robots spécifiques qui peuvent parler doivent avoir leur propre interface définie.
 */
interface Talkable {
    fun talk()
}

/**
 * Tout d'abord, nous créons un robot papillon qui implémente une interface générique et une interface spécifique.
 * Comme vous le voyez, nous ne sommes plus obligés d'implémenter des fonctions qui ne sont pas liées à notre robot !
 */
class ButterflyRobot : Robot, Flyable {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Appelle la commande de réinitialisation pour le robot. Tout logiciel de robot doit pouvoir être réinitialisé.
        // C'est raisonnable et nous allons l'implémenter.
        TODO("not implemented")
    }

    // Appelle la commande de vol pour le robot. Il s'agit d'une fonctionnalité spécifique de notre robot papillon.
    // Nous allons définitivement implémenter cela.
    override fun fly() {
        TODO("not implemented")
    }
}

/**
 * Ensuite, nous créons un robot humanoïde qui doit être capable d'effectuer des actions similaires à celles d'un humain et il
 * implémente également une interface générique et une interface spécifique pour son type.
 * Comme vous le voyez, nous ne sommes plus obligés d'implémenter des fonctions qui ne sont pas liées à notre robot !
 */
class HumanoidRobot : Robot, Talkable {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Appelle la commande de réinitialisation pour le robot. Tout logiciel de robot doit pouvoir être réinitialisé.
        // C'est raisonnable et nous allons l'implémenter.
        TODO("not implemented")
    }

    override fun talk() {
        // Appelle la commande de parole pour le robot. Il s'agit d'une fonctionnalité spécifique de notre robot humanoïde.
        // Nous allons définitivement implémenter cela.
        TODO("not implemented")
    }
}
```

### Principe d'inversion des dépendances

> _Il faut « dépendre des abstractions, [et non] des concretions. »_

Le dernier principe stipule que les modules de haut niveau ne doivent pas dépendre des modules de bas niveau. Les deux doivent dépendre des abstractions. Les abstractions ne doivent pas dépendre des détails. Les détails doivent dépendre des abstractions.

L'idée principale du principe est de ne pas avoir de dépendances directes entre les modules et les classes. Essayez de les rendre dépendants des abstractions (par exemple, les interfaces) à la place.

Pour simplifier encore plus, si vous utilisez une classe à l'intérieur d'une autre classe, cette classe sera dépendante de la classe injectée. Cela viole l'idée du principe et vous ne devriez pas faire cela. Vous devriez essayer de découpler toutes les classes.

? EXEMPLE DE MAUVAIS CODE :

```kotlin
class Radiator {
    var temperatureCelsius : Int = 0

    fun turnOnHeating(newTemperatureCelsius : Int) {
        temperatureCelsius  = newTemperatureCelsius
        // Pour allumer le chauffage du radiateur, nous devons effectuer des étapes spécifiques pour cet appareil.
        // Le radiateur aura sa propre procédure technique pour être allumé.
        // Procédure implémentée ici.
        TODO("not implemented")
    }
}

class AirConditioner {
    var temperatureFahrenheit: Int = 0

    fun turnOnHeating(newTemperatureFahrenheit: Int) {
        temperatureFahrenheit = newTemperatureFahrenheit
        // Pour allumer le chauffage de la climatisation, nous devons effectuer certaines étapes spécifiques
        // juste pour cet appareil, car la climatisation aura sa propre procédure technique.
        // Cette procédure est différente de celle du radiateur et sera implémentée ici.
        TODO("not implemented")
    }
}

class SmartHome {

    // À notre système de contrôle de maison intelligente, nous avons ajouté un contrôle de radiateur.
    var radiator: Radiator = Radiator()
    // Mais que se passera-t-il si plus tard nous décidons de changer notre radiateur en climatisation ?
    // var airConditioner: AirConditioner = AirConditioner()
    // Cette classe SmartHome dépend de la classe Radiator et viole le Principe d'Inversion des Dépendances.

    var recommendedTemperatureCelsius : Int = 20

    fun warmUpRoom() {
        radiator.turnOnHeating(recommendedTemperatureCelsius)
        // Si nous décidons d'ignorer le principe, certaines erreurs importantes peuvent survenir, comme celle-ci
        // par exemple. Ici, nous passons la température recommandée en Celsius, mais notre climatisation s'attend à
        // la recevoir en Fahrenheit.
        // airConditioner.turnOnHeating(recommendedTemperatureCelsius)
    }
}
```

? EXEMPLE DE BON CODE :

```kotlin
// Tout d'abord, créons une abstraction - une interface.
interface Heating {
    fun turnOnHeating(newTemperatureCelsius : Int)
}

// La classe doit implémenter l'interface Heating.
class Radiator : Heating {
    var temperatureCelsius : Int = 0

    override fun turnOnHeating(newTemperatureCelsius: Int) {
        temperatureCelsius  = newTemperatureCelsius
        // Ici, le radiateur aura sa propre procédure technique implémentée pour être allumé.
        TODO("not implemented")
    }
}

// La classe doit implémenter l'interface Heating.
class AirConditioner : Heating {
    var temperatureFahrenheit: Int = 0

    override fun turnOnHeating(newTemperatureCelsius: Int) {
        temperatureFahrenheit = newTemperatureCelsius * 9/5 + 32
        // La procédure technique d'allumage de la climatisation sera implémentée ici.
        TODO("not implemented")
    }
}

class SmartHome {

    // À notre système de contrôle de maison intelligente, nous avons ajouté un contrôle de radiateur.
    var radiator: Heating = Radiator()
    // Maintenant, nous avons une réponse à la question de savoir ce qu'il se passera si plus tard nous décidons de changer notre radiateur
    // en climatisation. Notre classe va dépendre de l'interface au lieu d'une autre
    // classe injectée.
    // var airConditioner: Heating = AirConditioner()

    var recommendedTemperatureCelsius : Int = 20

    fun warmUpRoom() {
        radiator.turnOnHeating(recommendedTemperatureCelsius)
        // Comme nous dépendons de l'interface commune, il n'y a plus de chance de faire des erreurs.
        // airConditioner.turnOnHeating(recommendedTemperatureCelsius)
    }
}
```

### Pour résumer brièvement

Si nous réfléchissons à tous ces principes, nous pouvons remarquer qu'ils sont complémentaires les uns des autres. Suivre les principes SOLID nous apportera de nombreux avantages. Ils rendront notre application réutilisable, maintenable, évolutive, testable.

Bien sûr, il n'est pas toujours possible de suivre tous ces principes complètement, car tout dépend des situations individuelles lors de l'écriture de code. Mais en tant que développeur, vous devez au moins les connaître afin de pouvoir décider quand les appliquer.

### Dépôt

Il s'agit de la première partie où nous apprenons et planifions notre projet au lieu d'écrire du nouveau code. Voici un lien vers le commit de la branche Partie 1, qui est essentiellement le code initial « Hello world » du projet.

#### [Voir la source sur GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-1)



J'espère avoir réussi à expliquer les principes SOLID. N'hésitez pas à laisser des commentaires ci-dessous.

---

**_Ačiū ! Merci d'avoir lu ! J'ai initialement publié cet article pour mon blog personnel [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-1/) le 23 février 2018._**