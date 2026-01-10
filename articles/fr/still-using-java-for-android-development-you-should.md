---
title: Vous utilisez toujours Java pour développer vos applications Android ? Essayez
  Kotlin à la place.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T17:12:27.000Z'
originalURL: https://freecodecamp.org/news/still-using-java-for-android-development-you-should
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/photo-1509803874385-db7c23652552.jpeg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
seo_title: Vous utilisez toujours Java pour développer vos applications Android ?
  Essayez Kotlin à la place.
seo_desc: 'By Pramono Winata

  Kotlin has been a huge breakthrough for the last 2 years, it has been a trending
  topic everywhere and its popularity is still rising. And it is also official that
  Google has pushed Kotlin to become the official language for Android ...'
---

Par Pramono Winata

Kotlin a été une énorme percée au cours des deux dernières années, c'est un sujet tendance partout et sa popularité ne cesse de croître. Et il est également officiel que Google a poussé Kotlin à devenir le langage officiel pour le développement d'applications Android.

Mais même alors, beaucoup de gens préfèrent encore Java à Kotlin pour le développement Android, pourquoi ? L'une des principales raisons est que les gens ne sont toujours pas à l'aise pour changer leur langage principal de Java à Kotlin, les gens ont peur de changer pour de nouvelles choses.

## Commencez à utiliser Kotlin maintenant, la manière facile

En réalité, il est très facile de passer à Kotlin depuis Java, étant un langage très flexible, vous pouvez facilement coder en Kotlin mais idiomatiquement, c'est Java !

![Image](https://www.freecodecamp.org/news/content/images/2019/07/meme.jpeg)
_Cela ressemble à Kotlin, mais en fait c'est Java. Mais je vous assure, tout va bien se passer !!_

Alors maintenant, voici plusieurs choses à noter lors du passage à Kotlin depuis Java :

**1. Interopérabilité Java**  
Kotlin est entièrement interopérable avec Java et aussi, dans l'autre sens. Qu'est-ce que cela signifie, cela signifie que votre Kotlin peut appeler votre code Java, cela rend les choses très faciles pour la migration d'applications, vous avez déjà codé à moitié avec Java ? Peu importe, codez en Kotlin quand même.

**2. Plus de types de données primitifs**  
Vous souvenez-vous quand choisir entre utiliser **int** ou **Int** en Java vous prenait une demi-journée ? Il n'y a plus de types de données primitifs maintenant en Kotlin, tout a été enveloppé dans Object à la place.

**3. Syntaxe légèrement modifiée (Mais ne vous inquiétez pas, c'est facile à rattraper)**  
Plusieurs syntaxes comme la déclaration de variable, de fonction et de classe ont été légèrement modifiées, mais si vous venez d'un background OOP comme Java, cela ne sera pas un problème. Et aussi, le mot-clé void et le point-virgule (';') ont été supprimés, merci Kotlin pour cette suppression de point-virgule !!  
Je vais vous présenter les exemples de base avec une classe Android : 

```kotlin
//L'héritage et l'implémentation utilisent ':' maintenant
class BasicActivity : AppCompatActivity() {
    //la déclaration des variables est maintenant le nom de la variable d'abord puis le type
    var a :Int = 10 //var est pour mutable
    val b :Int = 15 //val est pour immutable

    /*le mot-clé lateinit doit être ajouté pour l'initialisation des types non-
    primitifs sans valeur initiale en Kotlin*/
    lateinit var someTextView:TextView

    //Aussi, plus de mot-clé new ici
    var gameList:List<Integer> = ArrayList()

    //le remplacement utilise le mot-clé au lieu de 
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_basic)
    }
}

```

4. **Inférence de type**  
Kotlin rendra la vie plus facile en fournissant l'inférence de type pour les variables :

```kotlin
var a = 5 //inférera automatiquement cela comme entier
var b = "John" //inférera automatiquement cela comme String

```

5. **Vérifications de [sécurité null](https://kotlinlang.org/docs/reference/null-safety.html)**  
Kotlin a fourni des vérifications de sécurité null afin d'éviter les exceptions de pointeur null. Chaque variable qui pourrait retourner une valeur null sera marquée (et doit être marquée) avec le signe `?`. 

```kotlin
var a:String? = null
var b:String = null //non autorisé 
```

Il fournit également un appel de sécurité null afin d'éviter l'exception Null-Pointer (Erreurs de milliard de dollars de Java)

```
//non autorisé, a pourrait être null
a.function() 

//ci-dessous ne lancera pas de pointeur null, mais continuera le flux
a?.function()

//forcer l'appel de fonction, peut causer NPE, à utiliser uniquement si 100% sûr que cette valeur ne sera pas null
a!!.function()
```

6. **Plus de mot-clé static**  
Le mot-clé static a maintenant été remplacé par le mot-clé [Object](https://kotlinlang.org/docs/reference/object-declarations.html), à la fois pour les classes et les méthodes, plus spécifiquement [Companion Object](https://kotlinlang.org/docs/tutorials/kotlin-for-py/objects-and-companion-objects.html) pour les méthodes.  
  
7. **Switch case modifié**  
Switch case a maintenant été modifié en un nouveau mot-clé, appelé [when](https://kotlinlang.org/docs/reference/control-flow.html). Ce qui semble plus propre et plus flexible :

```kotlin
when (x) {
    1 -> println("One")
    2 -> print("Two")
	else -> print("Others")
}
```

8. **Plus d'[exception vérifiée](https://www.geeksforgeeks.org/checked-vs-unchecked-exceptions-in-java/)**  
Vous souvenez-vous quand vous faisiez certaines opérations ou castings en Java, et que cet avertissement rouge apparaissait et vous disait d'ajouter une vérification d'exception ? Cela a été supprimé maintenant en Kotlin. Maintenant, votre IDE ne vous forcer plus à faire des exceptions !

C'est tout pour la partie où vous devez commencer à développer en Kotlin, mais idiomatiquement Java.  
Ce n'est pas difficile de se mettre à Kotlin maintenant, n'est-ce pas ? Maintenant, Kotlin ne semble pas si différent de Java.

---

## Fonctionnalités fournies par Kotlin

![Image](https://www.freecodecamp.org/news/content/images/2019/07/download.png)

Maintenant, après avoir vu comment Kotlin et Java diffèrent, nous devons également examiner les fonctionnalités fournies par Kotlin et comment commencer lentement à faire du Kotlin, à la manière Kotlin :

**1. Flexibilité**   
L'une des principales raisons de mon amour pour Kotlin est la flexibilité du langage. Êtes-vous puriste OOP ? Avez-vous envie d'essayer la [Programmation Fonctionnelle](https://en.wikipedia.org/wiki/Functional_programming) qui est actuellement le sujet à la mode ? Et pour l'amour du dieu du _codage_, vous pouvez faire les deux en Kotlin ! Malgré le fait de ne pas fournir toutes les fonctionnalités de la PF, c'est assez bon pour la supporter. 

**2. [Support Lambda](https://kotlinlang.org/docs/reference/lambdas.html)**  
Oui, je sais que Java 8 supporte lambda, mais Kotlin est arrivé le premier et fait un très bon travail. Bien sûr, la transition vers l'utilisation des fonctions Lambda sera difficile au début, mais comme indiqué, Kotlin est vraiment flexible sur ce point. Alors, c'est à vous de choisir !  
Certaines des bibliothèques Android ont également activé le support Lambda, par exemple `View.OnClickListener` (Si vous venez d'un background Android, je suis certain que cette méthode vous est déjà très familière) :

```kotlin
val randomButton : Button

//utilisation de la fonction lambda comme argument
randomButton.setOnClickListener{v -> doRandomStuff(v) }
```

**3. [Data Class](https://kotlinlang.org/docs/reference/data-classes.html)**  
Kotlin a fourni un substitut pour les classes Model/Entity, appelé classe [Data](https://kotlinlang.org/docs/reference/data-classes.html). Elle supprime le besoin de setter et getter redondants et dispose également d'une méthode equal intégrée et d'une fonction toString sans que vous ayez à en créer une. C'est aussi très facile à utiliser : 

```kotlin
data class Person(
    val id:String,
    val name:String = "John Doe" //Valeur par défaut
)

//Bloc d'initialisation
var person = Person("id","Not John")
```

4. **[Fonctions d'extension](https://kotlinlang.org/docs/reference/extensions.html)**  
Kotlin permet l'utilisation de fonctions d'extension, ce qui rend le code plus lisible. De plus, cela vous permettra de donner une fonctionnalité à une classe sans modifier la classe elle-même :

```kotlin
fun Int.superOperation(anotherInt:Int):Int {
    val superNumber = this * anotherInt + anotherInt
    return superNumber
}

//vous pouvez maintenant appeler les fonctions
val someNumber = 5
val superNumber = someNumber.superOperation(10) //65
```

5. **[Arguments nommés et par défaut](https://kotlinlang.org/docs/reference/functions.html)**  
Comme C#, Kotlin supporte également les paramètres nommés et par défaut pour ses méthodes. Cela supprime complètement le besoin de passer des valeurs dans chaque argument. Vous pouvez sélectionner quelle valeur vous voulez modifier, et voilà ! Plus de tracas à passer la même valeur particulière pour 10 de vos appels de fonction !

```kotlin
//déclaration de variable
fun someOperations(var x: Int, var y:Int, var z:Int = 1){
	return x+y+z
}

someOperations(1,2) //retourne 4
someOpeartions(y = 1, x = 1) //retourne 3
```

6. **[Égalité référentielle](https://kotlinlang.org/docs/reference/equality.html)**  
Kotlin dispose également de l'égalité référentielle ('==='), elle vérifie si deux variables font actuellement référence au même objet.

```kotlin
var a = 10
var b = 10
a == b //vrai
a === b //vrai aussi, l'équation d'objet de type primitif ne vérifie que sa valeur

data class Person (val name: String)

val p1 = Person("John")
val p2 = Person("John")

p1 == p2 //vrai
p1 === p2 //faux
```

7. **[Casting intelligent](https://kotlinlang.org/docs/reference/typecasts.html)**  
Au lieu d'utiliser instance of, Kotlin fournit maintenant une syntaxe plus facile et plus lisible pour le casting ou la vérification de type :

```kotlin
//vérification de type
//le mécanisme de smart cast de Kotlin changera également automatiquement l'objet en type correspondant s'il passe la vérification de type
if (shape is Circle) {
    println("it's a Circle")
    shape.radius //automatiquement casté comme Circle
} else if (shapeObject is Square) {
    println("it's a Square")
} else if (shapeObject is Rectangle) {
    print("it's a Rectangle")
}
```

Kotlin dispose également du mot-clé `as` pour permettre le casting explicite :

```kotlin
//C'est considéré comme non sécurisé car il se comporte de manière similaire au casting statique
var anotherShape = shape as Circle

//Ceci peut être utilisé à la place pour un casting sécurisé
var safeShape = shape as? Circle
```

8. **[Coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html)**  
Les appels asynchrones ont toujours été un casse-tête en Java. La création de Thread prend beaucoup de place dans le code et rend le code illisible. Les coroutines ont été créées pour remplacer les opérations de thread traditionnelles, offrant un code propre et robuste :

```kotlin
import kotlinx.coroutines.*

fun main() {
    // lancer une nouvelle coroutine en arrière-plan et continuer
    GlobalScope.launch { 
        // délai non bloquant d'une seconde (l'unité de temps par défaut est ms)
        delay(1000L) 
        
        // imprimer après le délai
        println("World!") 
    }
    // le thread principal continue pendant que la coroutine est en délai
    println("Hello,") 
    
    // bloquer le thread principal pendant 2 secondes pour garder la JVM en vie
    Thread.sleep(2000L) 
}
```

Les coroutines supportent également des opérations plus complexes telles que Job Joining, Channel, Contexte partagé et Parents. Les détails et plus d'utilisations peuvent être lus [ici](https://kotlinlang.org/docs/reference/coroutines/coroutines-guide.html).

## Conclusion

En résumé, il est très facile de **commencer à utiliser Kotlin, vous pouvez coder en Kotlin très similaire à la façon dont vous codez en Java.** Et aussi, **Kotlin a fourni plusieurs fonctionnalités qui peuvent vous donner des avantages par rapport à l'utilisation de Java.**

Bien sûr, Java est toujours en pleine forme en ce moment. Mais il n'est jamais faux de commencer à apprendre quelque chose de nouveau. Nous, en tant que programmeurs, devons adopter l'apprentissage tout au long de la vie et ne jamais cesser d'apprendre. La meilleure chose à propos de Kotlin est la facilité avec laquelle il est possible de migrer depuis Java.

Merci d'avoir lu. J'espère que vous avez apprécié et que cela sera utile ! Bonne chance dans l'exploration de Kotlin, et à la prochaine.