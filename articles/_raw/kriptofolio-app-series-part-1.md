---
title: An introduction to the SOLID principles
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
seo_title: null
seo_desc: 'By Andrius Baruckis

  Kriptofolio app series - Part 1

  Software is always in a state of change. Each change can have a negative impact
  on a whole project. So the essential thing is to prevent damage that can be done
  while implementing all new changes.

  W...'
---

By Andrius Baruckis

#### Kriptofolio app series - Part 1

Software is always in a state of change. Each change can have a negative impact on a whole project. So the essential thing is to prevent damage that can be done while implementing all new changes.

With “Kriptofolio” (previously “My Crypto Coins”) app, I will be creating a lot of new code step by step and I want to start doing that in a good way. I want my project to be solid quality. First we need to understand the foundation principles of creating modern software. They are called SOLID principles. Such a catchy name! ?

### Series content

* [Introduction: A roadmap to build a modern Android app in 2018–2019](https://www.freecodecamp.org/news/kriptofolio-app-series)
* Part 1: An introduction to the SOLID principles (you’re here)
* [Part 2: How to start building your Android app: creating Mockups, UI, and XML layouts](https://www.freecodecamp.org/news/kriptofolio-app-series-part-2)
* [Part 3: All about that Architecture: exploring different architecture patterns and how to use them in your app](https://www.freecodecamp.org/news/kriptofolio-app-series-part-3)
* [Part 4: How to implement Dependency Injection in your app with Dagger 2](https://www.freecodecamp.org/news/kriptofolio-app-series-part-4)
* [Part 5: Handle RESTful Web Services using Retrofit, OkHttp, Gson, Glide and Coroutines](https://www.freecodecamp.org/news/kriptofolio-app-series-part-5)

### Principles slogan

**SOLID** is a mnemonic acronym. It helps to define the five basic object-oriented design principles:

1. **S**ingle Responsibility Principle
2. **O**pen-Closed Principle
3. **L**iskov Substitution Principle
4. **I**nterface Segregation Principle
5. **D**ependency Inversion Principle

Next we are going to discuss each of them individually. For each, I am going to provide bad vs good code examples. These examples are written for Android using the Kotlin language.

### Single Responsibility Principle

> _A class should have only a single responsibility._

Each class or module should be responsible for one part of the functionality provided by the app. So when it handles one thing, there should be only one main reason to change it. If your class or module does more than one thing, then you should split the functionalities in separate ones.

For a better understanding of this principle, I would take as an example a Swiss Army knife. This knife is well known for its multiple functions besides its main blade. It has other tools integrated inside, such as screwdrivers, a can opener, and many others.

The natural question here for you is why am I suggesting this knife as an example for single functionality? But just think about it one moment. The other main feature of this knife is mobility while being pocket size. So even if it offers a few different functions it still fits its main purpose to be small enough to take it with you comfortably.

The same rules go with programming. When you create your class or module, it has to have some main global purpose. At the same time you can’t overplay when trying to simplify everything too much by separating functionality. So remember, keep the balance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m1OGuBK5fYZM1Lof6GkH3Q.jpeg)

A classic example could be the often used method `onBindViewHolder` when building RecyclerView widget adapter.

? BAD CODE EXAMPLE:

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
         *  Here method violates the Single Responsibility Principle!!!
         *  Despite its main and only responsibility to be adapting a VinylRecord object
         *  to its view representation, it is also performing data formatting as well.
         *  It has multiple reasons to be changed in the future, which is wrong.
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

? GOOD CODE EXAMPLE:

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
         * Instead of performing data formatting operations here, we move that responsibility to
         * other class. Actually here you see only direct call of top-level function
         * convertArrayListToString - new Kotlin language feature. However don't be mistaken,
         * because Kotlin compiler behind the scenes still is going to create a Java class, and
         * than the individual top-level functions will be converted to static methods. So single
         * responsibility for each class.
         */

        holder.genre!!.text =  convertArrayListToString(vinyl.genres)
    }
    ...
}
```

Code specifically designed with the Single Responsibility Principle in mind will be close to the other principles that we are going to discuss.

### Open-Closed Principle

> _Software entities should be open for extension, but closed for modification._

This principle states that when you write all the software parts like classes, modules, and functions, you should make them open for extension but closed for any modification. What does that mean?

Let’s say we create a working class. There should be no need to tweak that class if we need to add new functionality or do some changes. Instead we should be able to extend that class by creating its new subclass where we could easily add all new necessary features. Features should always be parameterized in a way that a subclass can override.

Let’s take a look at an example where we will create a special `FeedbackManager` class to show a different type of custom message for the user.

? BAD CODE EXAMPLE:

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

    // Imagine that we need to add new type feedback message. What would happen?
    // We would need to modify this manager class. But to follow Open Closed Principle we
    // need to write a code that can be adapted automatically to the new requirements without
    // rewriting the old classes.

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

? GOOD CODE EXAMPLE:

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

    // Again the same situation - we need to add new type feedback message. We have to write code
    // that can be adapted to new requirements without changing the old class implementation.
    // Here the solution is to focus on extending the functionality by using interfaces and it
    // follows the Open Closed Principle.

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

The open-closed principle summarizes the goals of the next two principles that I talk about below. So let’s move on to them.

### Liskov Substitution Principle

> _Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program._

This principle is named after [Barbara Liskov](https://en.wikipedia.org/wiki/Barbara_Liskov) — an accomplished computer scientist. The general idea of this principle is that objects should be replaceable by instances of their subtypes without changing the behavior of the program.

Let’s say in your app you have `MainClass` which depends on `BaseClass`, which extends `SubClass`. In short, to follow this principle, your `MainClass` code and your app in general should work seamlessly without any problems when you decide to change `BaseClass` instance to the `SubClass` instance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*72oYWBRb9y7HgiE-KkMQGw.png)

To understand this principle even better, let me give you a classical, easy to understand example with `Square` and `Rectangle` inheritance.

? BAD CODE EXAMPLE:

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val rectangleFirst: Rectangle = Rectangle()
        rectangleFirst.width = 2
        rectangleFirst.height = 3

        textViewRectangleFirst.text = rectangleFirst.area().toString()
        // The result of the first rectangle area is 6, which is correct as 2 x 3 = 6.

        // The Liskov Substitution Principle states that a subclass (Square) should override
        // the parent class (Rectangle) in a way that does not break functionality from a
        // consumers’s point of view. Let's see.
        val rectangleSecond: Rectangle = Square()
        // The user assumes that it is a rectangle and try to set the width and the height as usual
        rectangleSecond.width = 2
        rectangleSecond.height = 3

        textViewRectangleSecond.text = rectangleSecond.area().toString()
        // The expected result of the second rectangle should be 6 again, but instead it is 9.
        // So as you see this object oriented approach for Square extending Rectangle is wrong.
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

? GOOD CODE EXAMPLE:

```kotlin
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Here it is presented a way how to organize these Rectangle and Square classes better to
        // meet the Liskov Substitution Principle. No more unexpected result.
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

Always think before writing down your hierarchy. As you see in this example, real-life objects do not always map to the same OOP classes. You need to find a different approach.

### Interface Segregation Principle

> _Many client-specific interfaces are better than one general-purpose interface._

Even the name sounds complicated, but the principle itself is rather easy to understand. It states that a client should never be forced to depend on methods or implement an interface that it doesn’t use. A class needs to be designed to have the fewest methods and attributes. When creating an interface try not to make it too big. Instead split it into smaller interfaces so that client of the interface will only know about the methods that are relevant.

To get the idea of this principle I have created again bad vs good code examples with butterfly and humanoid robots. ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*bogaw0ohgybpgEchiGSsLw.jpeg)

? BAD CODE EXAMPLE:

```kotlin
/**
 * Let's imagine we are creating some undefined robot. We decide to create an interface with all
 * possible functions to it.
 */
interface Robot {
    fun giveName(newName: String)
    fun reset()
    fun fly()
    fun talk()
}

/**
 * First we are creating butterfly robot which implements that interface.
 */
class ButterflyRobot : Robot {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Calls reset command for the robot. Any robot's software should be possible to reset.
        // That is reasonable and we will implement this.
        TODO("not implemented")
    }

    override fun fly() {
        // Calls fly command for the robot. This is specific functionality of our butterfly robot.
        // We will definitely implement this.
        TODO("not implemented")
    }

    override fun talk() {
        // Calls talk command for the robot.
        // WRONG!!! Our butterfly robot is not going to talk, just fly! Why we need implement this?
        // Here it is a violation of Interface Segregation Principle as we are forced to implement
        // a method that we are not going to use.
        TODO("???")
    }
}

/**
 * Next we are creating humanoid robot which should be able to do similar actions as human and it
 * also implements same interface.
 */
class HumanoidRobot : Robot {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Calls reset command for the robot. Any robot's software should be possible to reset.
        // That is reasonable and we will implement this.
        TODO("not implemented")
    }

    override fun fly() {
        // Calls fly command for the robot.
        // That the problem! We have never had any intentions for our humanoid robot to fly.
        // Here it is a violation of Interface Segregation Principle as we are forced to implement
        // a method that we are not going to use.
        TODO("???")
    }

    override fun talk() {
        // Calls talk command for the robot. This is specific functionality of our humanoid robot.
        // We will definitely implement this.
        TODO("not implemented")
    }
}
```

? GOOD CODE EXAMPLE:

```kotlin
/**
 * Let's imagine we are creating some undefined robot. We should create a generic interface with all
 * possible functions common to all types of robots.
 */
interface Robot {
    fun giveName(newName: String)
    fun reset()
}

/**
 * Specific robots which can fly should have their own interface defined.
 */
interface Flyable {
    fun fly()
}

/**
 * Specific robots which can talk should have their own interface defined.
 */
interface Talkable {
    fun talk()
}

/**
 * First we are creating butterfly robot which implements a generic interface and a specific one.
 * As you see we are not required anymore to implement functions which are not related to our robot!
 */
class ButterflyRobot : Robot, Flyable {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Calls reset command for the robot. Any robot's software should be possible to reset.
        // That is reasonable and we will implement this.
        TODO("not implemented")
    }

    // Calls fly command for the robot. This is specific functionality of our butterfly robot.
    // We will definitely implement this.
    override fun fly() {
        TODO("not implemented")
    }
}

/**
 * Next we are creating humanoid robot which should be able to do similar actions as human and it
 * also implements generic interface and specific one for it's type.
 * As you see we are not required anymore to implement functions which are not related to our robot!
 */
class HumanoidRobot : Robot, Talkable {
    var name: String = ""

    override fun giveName(newName: String) {
        name = newName
    }

    override fun reset() {
        // Calls reset command for the robot. Any robot's software should be possible to reset.
        // That is reasonable and we will implement this.
        TODO("not implemented")
    }

    override fun talk() {
        // Calls talk command for the robot. This is specific functionality of our humanoid robot.
        // We will definitely implement this.
        TODO("not implemented")
    }
}
```

### Dependency Inversion Principle

> _One should “depend upon abstractions, [not] concretions.”_

The last principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. Abstractions should not depend on details. Details should depend on abstractions.

The main idea of the principle is not to have direct dependencies between the modules and classes. Try to make them dependent on the abstractions (e.g. interfaces) instead.

To simplify it even more, if you use a class inside another class, this class will be dependent on the class injected. This violates the principle’s idea and you should not do that. You should try to decouple all classes.

? BAD CODE EXAMPLE:

```kotlin
class Radiator {
    var temperatureCelsius : Int = 0

    fun turnOnHeating(newTemperatureCelsius : Int) {
        temperatureCelsius  = newTemperatureCelsius
        // To turn on heating for the radiator we will have to do specific steps for this device.
        // Radiator will have it's own technical procedure of how it will be turned on.
        // Procedure implemented here.
        TODO("not implemented")
    }
}

class AirConditioner {
    var temperatureFahrenheit: Int = 0

    fun turnOnHeating(newTemperatureFahrenheit: Int) {
        temperatureFahrenheit = newTemperatureFahrenheit
        // To turn on heating for air conditioner we will have to do some specific steps
        // just for this device, as air conditioner will have it's own technical procedure.
        // This procedure is different compared to radiator and will be implemented here.
        TODO("not implemented")
    }
}

class SmartHome {

    // To our smart home control system we added a radiator control.
    var radiator: Radiator = Radiator()
    // But what will be if later we decide to change our radiator to air conditioner instead?
    // var airConditioner: AirConditioner = AirConditioner()
    // This SmartHome class is dependent of the class Radiator and violates Dependency Inversion Principle.

    var recommendedTemperatureCelsius : Int = 20

    fun warmUpRoom() {
        radiator.turnOnHeating(recommendedTemperatureCelsius)
        // If we decide to ignore the principle there may occur some important mistakes, like this
        // one. Here we pass recommended temperature in celsius but our air conditioner expects to
        // get it in Fahrenheit.
        // airConditioner.turnOnHeating(recommendedTemperatureCelsius)
    }
}
```

? GOOD CODE EXAMPLE:

```kotlin
// First let's create an abstraction - interface.
interface Heating {
    fun turnOnHeating(newTemperatureCelsius : Int)
}

// Class should implement the Heating interface.
class Radiator : Heating {
    var temperatureCelsius : Int = 0

    override fun turnOnHeating(newTemperatureCelsius: Int) {
        temperatureCelsius  = newTemperatureCelsius
        // Here radiator will have it's own technical procedure implemented of how it will be turned on.
        TODO("not implemented")
    }
}

// Class should implement the Heating interface.
class AirConditioner : Heating {
    var temperatureFahrenheit: Int = 0

    override fun turnOnHeating(newTemperatureCelsius: Int) {
        temperatureFahrenheit = newTemperatureCelsius * 9/5 + 32
        // Air conditioner's turning on technical procedure will be implemented here.
        TODO("not implemented")
    }
}

class SmartHome {

    // To our smart home control system we added a radiator control.
    var radiator: Heating = Radiator()
    // Now we have an answer to the question what will be if later we decide to change our radiator
    // to air conditioner. Our class is going to depend on the interface instead of another
    // injected class.
    // var airConditioner: Heating = AirConditioner()

    var recommendedTemperatureCelsius : Int = 20

    fun warmUpRoom() {
        radiator.turnOnHeating(recommendedTemperatureCelsius)
        // As we depend on the common interface, there is no more chance for mistakes.
        // airConditioner.turnOnHeating(recommendedTemperatureCelsius)
    }
}
```

### To sum up briefly

If we think about all these principles, we can notice that they are complementary to each other. Following the SOLID principles will give us many benefits. They will make our app reusable, maintainable, scalable, testable.

Of course it is not always possible to follow all these principles completely, as everything depends on individual situations when writing code. But as a developer you should at least know them so you can decide when to apply them.

### Repository

This is the first part where we learn and plan our project instead of writing new code. Here is a link to Part 1 branch commit, which basically is “Hello world” initial code of the project.

#### [View Source On GitHub](https://github.com/baruckis/Kriptofolio/tree/Part-1)



I hope I managed to explain SOLID principles well. Feel free to leave comments below.

---

**_Ačiū! Thanks for reading! I originally published this post for my personal blog [www.baruckis.com](https://www.baruckis.com/android/kriptofolio-app-series-part-1/) on February 23, 2018._**

