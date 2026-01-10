---
title: Kotlin VS Java – Quel langage de programmation devriez-vous apprendre ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T19:10:12.000Z'
originalURL: https://freecodecamp.org/news/kotlin-vs-java-which-language-to-learn-in-2020
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9987740569d1a4ca2041.jpg
tags:
- name: Java
  slug: java
- name: Kotlin
  slug: kotlin
- name: programming languages
  slug: programming-languages
seo_title: Kotlin VS Java – Quel langage de programmation devriez-vous apprendre ?
seo_desc: 'By Pramono Winata

  It has been several years since Kotlin came out, and it has been doing well. Since
  it was created specifically to replace Java, Kotlin has naturally been compared
  with Java in many respects.

  To help you decide which of the two langu...'
---

Par Pramono Winata

Plusieurs années se sont écoulées depuis la sortie de Kotlin, et il s'en sort bien. Puisqu'il a été créé spécifiquement pour remplacer Java, Kotlin a naturellement été comparé à Java à bien des égards.

Pour vous aider à décider quel langage apprendre, je vais comparer certaines des principales caractéristiques de chaque langage afin que vous puissiez choisir celui que vous souhaitez apprendre.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/asa-1-1.jpg align="left")

Voici les 8 points que je vais aborder dans cet article :

* Syntaxe
    
* Expressions Lambda
    
* Gestion des null
    
* Classes de modèle
    
* Variables globales
    
* Concurrence
    
* Fonctions d'extension
    
* Communauté
    

## Comparaison de la syntaxe

Pour commencer, faisons une comparaison de base de la syntaxe. Beaucoup d'entre vous qui lisez ceci ont peut-être déjà quelques connaissances sur Java et/ou Kotlin, mais je vais donner un exemple de base ci-dessous afin que nous puissions les comparer directement :

### Java

```java
public class HelloClass { 

	public void FullName(String firstName, String lastName) {
    	String fullName = firstName + " " + lastName;
		System.out.println("My name is : " + fullName); 
	} 
    
    	public void Age() { 
		int age = 21;
		System.out.println("My age is : " + age); 
	} 

	public static void main(String args[]) { 
		HelloClass hello = new HelloClass(); 
		hello.FullName("John","Doe");
        hello.Age();
	} 
}
```

### Kotlin

```kotlin
class NameClass {
    fun FullName(firstName: String, lastName:String) {
        var fullName = "$firstName $lastName"
        println("My Name is : $fullName")
    }
}

fun Age() {
	var age : Int
    age = 21
    println("My age is: $age")
}

fun main(args: Array<String>) {
    NameClass().FullName("John","Doe")
    Age()
}
```

La sensation du code n'est pas si différente, à part quelques petits changements de syntaxe dans les méthodes et les classes.

Mais la vraie différence ici est que Kotlin supporte l'inférence de type où le type de variable n'a pas besoin d'être déclaré. De plus, nous n'avons plus besoin de points-virgules (`;`).

Nous pouvons également noter que Kotlin n'impose pas strictement la POO comme Java où tout doit être contenu dans une classe. Regardez `fun Age` et `fun main` dans l'exemple où ils ne sont pas contenus dans une classe.

Kotlin a également généralement moins de lignes de code, tandis que Java adhère davantage à une approche traditionnelle en rendant tout verbeux.

Un avantage de Kotlin sur Java est sa flexibilité – il peut choisir de tout faire dans l'approche traditionnelle de la POO ou il peut prendre une autre direction.

## Expressions Lambda

Si nous parlons de Java et Kotlin, nous devons bien sûr parler de la célèbre expression lambda. Kotlin supporte nativement les lambdas (et l'a toujours fait), tandis que les lambdas ont été introduites pour la première fois dans Java 8.

Voyons à quoi elles ressemblent.

### Java

```java
//syntaxes
parameter -> expression
(parameter1, parameter2) -> { code }

//sample usage
ArrayList<Integer> numbers = new ArrayList<Integer>();
numbers.add(5);
numbers.add(9);
numbers.forEach( (n) -> { System.out.println(n); } );
```

### Kotlin

```kotlin
//syntax
{ parameter1, parameter2 -> code }

//sample usage
max(strings, { a, b -> a.length < b.length })
```

En Java, les parenthèses sont plus souples : si un seul paramètre existe, il n'est pas nécessaire de mettre des parenthèses. Mais en Kotlin, les crochets sont toujours requis. Cependant, il n'y a pas beaucoup de différences en dehors de la syntaxe.

À mon avis, les fonctions lambda ne seront pas beaucoup utilisées en dehors de leur utilisation comme méthodes de rappel. Même si les fonctions lambda ont beaucoup plus d'utilisations, les problèmes de **lisibilité** les rendent moins désirables. Elles rendront votre code plus court, mais comprendre le code plus tard sera beaucoup plus difficile.

C'est juste une question de préférence, mais je pense qu'il est utile que Kotlin impose les crochets obligatoires pour aider à la lisibilité.

## Gestion des null

Dans un langage orienté objet, les valeurs de type null ont toujours été un problème. Ce problème se présente sous la forme d'une Null Pointer Exception (NPE) lorsque vous essayez d'utiliser le contenu d'une valeur null.

Puisque les NPE ont toujours été un problème, Java et Kotlin ont chacun leur propre façon de gérer les objets null, comme je vais le montrer ci-dessous.

### Java

```java
Object object = objServ.getObject();

//approche traditionnelle de vérification de null
if(object!=null){
    System.out.println(object.getValue());
}

//Optional a été introduit dans Java 8 pour aider davantage avec les valeurs null

//Optional nullable permettra un objet null
Optional<Object> objectOptional = Optional.ofNullable(objServ.getObject());

//Optional.of - lance NullPointerException si le paramètre passé est null
Optional<Object> objectNotNull = Optional.of(anotherObj);

if(objectOptional.isPresent()){
    Object object = objectOptional.get();
    System.out.println(object.getValue());
}

System.out.println(objectNotNull.getValue());
```

### Kotlin

```kotlin
//Kotlin utilise un mécanisme de sécurité null
var a: String = "abc" // Initialisation régulière signifie non-null par défaut
a = null // erreur de compilation

//autoriser null seulement si Nullable est défini
var b: String? = "abc" // peut être défini comme null
b = null // ok
print(b)
```

Pour autant que je me souvienne, Java a toujours utilisé la vérification traditionnelle de null, qui est sujette aux erreurs humaines. Ensuite, Java 8 est sorti avec des classes optionnelles qui permettent une vérification de null plus robuste, surtout du côté API/Serveur.

Kotlin, en revanche, fournit des variables de sécurité null où la variable doit être nullable si la valeur peut être null.

Je n'ai pas vraiment utilisé la classe optionnelle pour l'instant, mais le mécanisme et le but semblent assez similaires à la sécurité null de Kotlin. Les deux vous aident à identifier quelle variable peut être null et vous aident à vous assurer que la vérification correcte est implémentée.

Parfois, dans le code, il peut y avoir trop de variables et trop à vérifier. Mais ajouter des vérifications partout rend notre base de code laide, et personne n'aime ça, n'est-ce pas ?

À mon avis, cependant, l'utilisation de l'optionnel de Java semble un peu désordonnée à cause de la quantité de code qui doit être ajoutée pour les vérifications. Pendant ce temps, en Kotlin, vous pouvez simplement ajouter une petite quantité de code pour faire la vérification de null pour vous.

## Classe de modèle

Certaines personnes pourraient aussi appeler cela la classe Entité. Ci-dessous, vous pouvez voir comment les deux classes sont utilisées comme classes de modèle dans chaque langage.

### Java

```java
public class Student {

     private String name;
     private Integer age;
     
     // Constructeur par défaut
  	 public Student() { }

     public void setName(String name) {
         this.name = name;
     }

     public String getName() {
         return name;
     }
     
     public void setAge(Integer age) {
         this.age = age;
     }

     public Integer getAge() {
         return age;
     }
}
```

### Kotlin

```kotlin
//Classe de données Kotlin
data class Student(var name: String = "", var age: Int = 0)

//Utilisation
var student: Student = Student("John Doe", 21)
```

En Java, les propriétés sont déclarées comme privées, suivant la pratique de l'encapsulation. Lors de l'accès à ces propriétés, Java utilise des Getters et Setters, ainsi que les méthodes isEqual ou toString lorsque cela est nécessaire.

Du côté Kotlin, les [classes de données](https://kotlinlang.org/docs/reference/data-classes.html) sont introduites à des fins spéciales pour les classes de modèle. Les classes de données permettent d'accéder directement aux propriétés. Elles fournissent également plusieurs méthodes utilitaires intégrées telles que equals(), toString() et copy().

Pour moi, les classes de données sont l'une des meilleures choses que Kotlin offre. Elles visent à réduire la quantité de code standard dont vous avez besoin pour les classes de modèle régulières, et elles font vraiment du bon travail.

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-164.png align="left")

*Image aléatoire parce que vous êtes à moitié là ! Photo par [Unsplash](https://unsplash.com/@dinoreichmuth?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit"&gt;Dino Reichmuth / &lt;a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)*

## Variables globales

Parfois, votre code peut avoir besoin d'une variable accessible partout dans votre base de code. C'est à cela que servent les variables globales. Kotlin et Java ont chacun leur propre façon de gérer cela.

### Java

```java
public class SomeClass {
	public static int globalNumber = 10;
}

//peut être appelé sans initialiser la classe
SomeClass.globalNumber;
```

### Kotlin

```kotlin
class SomeClass {
    companion object {
        val globalNumber = 10
    }
}

//appelé exactement de la même manière que d'habitude
SomeClass.globalNumber
```

Certains d'entre vous pourraient déjà être familiers avec le mot-clé [static](https://www.javatpoint.com/static-keyword-in-java) ici puisqu'il est également utilisé dans d'autres langages comme C++. Il est initialisé au début de l'exécution d'un programme et est utilisé par Java pour fournir des variables globales puisqu'il n'est pas contenu comme un objet. Cela signifie qu'il peut être accessible n'importe où sans initialiser la classe comme un objet.

Kotlin utilise une approche assez différente ici : il supprime le mot-clé static et le remplace par un [companion object](https://kotlinlang.org/docs/tutorials/kotlin-for-py/objects-and-companion-objects.html) qui est assez similaire à un singleton. Il vous permet d'implémenter des fonctionnalités avancées telles que les extensions et l'interfaçage.

Le manque du mot-clé static en Kotlin a été assez surprenant pour moi. On pourrait argumenter que l'utilisation du mot-clé static pourrait ne pas être une bonne pratique en raison de sa nature et parce qu'il est difficile à tester. Et bien sûr, le companion object de Kotlin peut facilement le remplacer.

Même alors, utiliser static pour une variable globale devrait être assez simple. Si nous sommes prudents avec cela et que nous n'en faisons pas une habitude de rendre chaque chose globale, nous devrions être bons.

Le companion object pourrait également nous donner une certaine flexibilité avec l'interfaçage et autres, mais à quelle fréquence allons-nous interfacer des classes singleton ?

Je pense que les mots-clés static nous aident à garder les choses courtes et propres pour les variables globales.

## Concurrence

De nos jours, la concurrence est un sujet brûlant. Parfois, la capacité d'un langage de programmation à exécuter plusieurs tâches simultanément peut vous aider à décider si ce sera votre langage de choix.

Voyons comment les deux langages abordent cela.

### Java

```java

// Code Java pour la création de threads en étendant 
// la classe Thread 
class MultithreadingDemo extends Thread 
{ 
    public void run() 
    { 
        try
        { 
            // Affichage du thread en cours d'exécution 
            System.out.println ("Thread " + 
                  Thread.currentThread().getId() + 
                  " is running"); 
  
        } 
        catch (Exception e) 
        { 
            // Lancement d'une exception 
            System.out.println ("Exception is caught"); 
        } 
    } 
} 
  
// Classe principale 
public class Multithread 
{ 
    public static void main(String[] args) 
    { 
        int n = 8; // Nombre de threads 
        for (int i=0; i<n; i++) 
        { 
            MultithreadingDemo object = new MultithreadingDemo(); 
            object.start(); 
        } 
    } 
}
```

### Kotlin

```kotlin
for (i in 1..1000)
    GlobalScope.launch {
        println(i)
    }
```

Java utilise principalement des [threads](https://docs.oracle.com/javase/7/docs/api/java/lang/Thread.html) pour supporter la concurrence. En Java, faire un thread nécessite de créer une classe qui étend la classe thread intégrée de Java. Le reste de son utilisation devrait être assez simple.

Bien que les threads soient également disponibles en Kotlin, vous devriez plutôt utiliser ses [coroutines](https://kotlinlang.org/docs/reference/coroutines-overview.html). Les coroutines sont essentiellement des threads légers qui excellent dans les tâches courtes non bloquantes.

La concurrence a toujours été un concept difficile à saisir (et aussi, à tester). Le threading est utilisé depuis longtemps et certaines personnes pourraient déjà être à l'aise avec cela.

Les coroutines sont devenues plus populaires récemment avec des langages comme Kotlin et Go (Go a de manière similaire des goroutines). Le concept diffère légèrement des threads traditionnels – [les coroutines sont séquentielles tandis que les threads peuvent fonctionner en parallèle](https://stackoverflow.com/a/1934718/6065825).

Essayer les coroutines, cependant, devrait être assez facile puisque Kotlin fait un très bon travail pour les expliquer dans leur [docs](https://kotlinlang.org/docs/reference/coroutines-overview.html). Et un bonus pour Kotlin sur Java est la quantité de code standard qui peut être supprimée en Kotlin.

## Fonctions d'extension

Vous vous demandez peut-être pourquoi je parle de cela puisque Java lui-même n'a même pas cette fonctionnalité.

Mais je ne peux m'empêcher de le mentionner, car les fonctions d'extension sont une fonctionnalité très utile qui a été introduite dans Kotlin.

```kotlin
fun Int.plusOne(): Int {
	return this + 1
}

fun main(args: Array<String>) {
    var number = 1
    var result = number.plusOne()
    println("Result is: $result")
}
```

Elles permettent à une classe d'avoir de nouvelles fonctionnalités sans l'étendre dans la classe ou utiliser l'un des modèles de conception sophistiqués. Cela vous permet même d'ajouter des fonctionnalités aux classes de variables Kotlin.

Vous pouvez pratiquement dire adieu à ces méthodes de bibliothèque qui vous obligent à passer tout dans vos paramètres.

## Communauté

Enfin, mais non des moindres, parlons de quelque chose de non technique. D'abord, jetons un coup d'œil à cette enquête montrant les langages de programmation les plus couramment utilisés en 2020.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot-from-2020-07-24-23-05-40.png align="left")

*tiré de* [*stack overflow survey*](https://insights.stackoverflow.com/survey/2020#development-environments-and-tools)

Nous pouvons voir que Java est l'un des langages les plus couramment utilisés. Et bien que Kotlin soit encore en forte croissance en popularité, la communauté Java reste plusieurs fois plus grande que celle de Kotlin et cela ne changera probablement pas de sitôt.

Alors, pourquoi est-ce important ? En fait, c'est très important. Avec le nombre de personnes dans la communauté Java, il est beaucoup plus facile de trouver des références et d'obtenir de l'aide lorsque vous en avez besoin, à la fois sur Internet et dans le monde réel.

De nombreuses entreprises utilisent encore Java comme base et cela ne changera probablement pas de sitôt, même avec l'interopérabilité de Kotlin avec Java. Et généralement, faire une migration ne sert aucun but commercial à moins que l'entreprise n'ait des raisons vraiment très importantes pour cela.

## Conclusion

Pour ceux qui font défiler pour le résumé, voici ce que nous avons discuté :

* Syntaxe : les motifs ne diffèrent pas beaucoup à part quelques différences de syntaxe, mais Kotlin est plus flexible à plusieurs égards.
    
* Expressions Lambda : la syntaxe est presque la même, mais Kotlin utilise des crochets pour aider à la lisibilité.
    
* Gestion des null : Java utilise une classe pour aider à la gestion des null tandis que Kotlin utilise des variables de sécurité null intégrées.
    
* Classes de modèle : Java utilise des classes avec des variables privées et des setters/getters tandis que Kotlin les supporte avec des classes de données.
    
* Variables globales : Java utilise le mot-clé static tandis que Kotlin utilise quelque chose de similaire à des sous-classes.
    
* Concurrence : Java utilise le multithreading tandis que Kotlin utilise des coroutines (qui sont généralement plus légères).
    
* Fonctions d'extension : une nouvelle fonctionnalité introduite par Kotlin pour donner facilement des fonctionnalités aux classes sans les étendre.
    
* Communauté : Java règne toujours en maître dans l'aspect communautaire, ce qui le rend plus facile à apprendre et à obtenir de l'aide.
    

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-165.png align="left")

*Photo par [Unsplash](https://unsplash.com/@glenncarstenspeters?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit"&gt;Glenn Carstens-Peters / &lt;a href="https://unsplash.com/?utm_source=ghost&utm_medium=referral&utm_campaign=api-credit)*

Il y a beaucoup plus de fonctionnalités que nous pourrions comparer entre Java et Kotlin. Mais ce que j'ai discuté ici sont, à mon avis, certaines des plus importantes.

Je pense que Kotlin vaut bien la peine d'être appris en ce moment. Du côté du développement, il vous aide à supprimer le code standard long et à garder tout propre et court. Si vous êtes déjà un programmeur Java, apprendre Kotlin ne devrait pas être trop difficile et il est bon de prendre votre temps.

Merci d'avoir lu ! J'espère que cet article vous aidera à décider quel langage de programmation apprendre, Java ou Kotlin. Et pour tout ce que j'ai manqué, n'hésitez pas à me laisser un retour, cela sera grandement apprécié.