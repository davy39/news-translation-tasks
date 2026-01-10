---
title: Tutoriel sur le polymorphisme en Java – Avec exemple de code de programmation
  orientée objet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T00:57:14.000Z'
originalURL: https://freecodecamp.org/news/polymorphism-in-java-tutorial-with-object-oriented-programming-example-code
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/banner-1.jpg
tags:
- name: Java
  slug: java
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Tutoriel sur le polymorphisme en Java – Avec exemple de code de programmation
  orientée objet
seo_desc: 'By Rob O''Leary

  Polymorphism allows objects to be treated in a substitutable way. This reduces duplication
  of code when you want the same actions to be performed on different types of objects.
  Polymorphism literally means “many forms”.

  Let''s explain w...'
---

Par Rob O'Leary

Le polymorphisme permet de traiter les objets de manière interchangeable. Cela réduit la duplication de code lorsque vous souhaitez effectuer les mêmes actions sur différents types d'objets. Polymorphisme signifie littéralement « *plusieurs formes* ».

Expliquons exactement ce que nous entendons par là.

## Explication du polymorphisme par analogie

Si vous avez déjà voyagé à l'international, un élément de votre liste de préparation est probablement un adaptateur de prise électrique. Sinon, vous ne pourrez peut-être pas charger votre téléphone et autres appareils.

![packing.jpg](https://www.freecodecamp.org/news/content/images/2020/10/call-me-fred-nBfTARHPxiU-unsplash-1-.jpg)
_Photo par [Call Me Fred](https://unsplash.com/@callmefred?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText)_

Bizarrement, il existe environ 16 types différents de prises électriques dans le monde. Certaines ont 2 broches, d'autres en ont 3, certaines broches sont circulaires, d'autres rectangulaires, et la configuration des broches varie.

La solution que la plupart des gens adoptent est d'acheter un adaptateur universel.

Pour voir le problème sous un autre angle, généralement le problème est que nous avons une interface de prise qui n'accepte qu'un seul type d'objet de prise ! Les prises ne sont pas polymorphes.

La vie serait beaucoup plus facile pour tout le monde si nous avions des prises qui pourraient accepter de nombreux types différents de fiches. Nous pouvons rendre l'interface de la prise polymorphe en créant différentes formes de fentes. Vous pouvez voir dans l'image ci-dessous comment cela a été fait.

![socket-metaphor](https://www.freecodecamp.org/news/content/images/2020/10/socket-metaphor.svg)

Le polymorphisme nous aide à créer des interfaces plus universelles.

## Explication avec du code

Tout objet qui a une relation EST-UN est considéré comme polymorphe. Vous avez une relation EST-UN par héritage (en utilisant le mot-clé *extends* dans la signature de la classe), ou par interfaces (en utilisant le mot-clé *implements* dans la signature de la classe).

Pour comprendre complètement le polymorphisme, vous devez également comprendre l'héritage et les interfaces.

```java
class Dog extends Animal implements Canine{
 // ... some code here
}
```

Sur la base de l'extrait ci-dessus, un `Dog` a les relations EST-UN suivantes : `Animal`, `Canine`, et `Object` (toutes les classes héritent implicitement de la classe [Object](https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html), ce qui semble un peu ridicule !).

Donnons un exemple simple (et un peu bête) pour illustrer comment nous pouvons utiliser le polymorphisme pour simplifier notre code. Nous voulons créer une application avec un interrogateur qui peut convaincre n'importe quel animal de parler.

![interrogation](https://www.freecodecamp.org/news/content/images/2020/11/interrogation-1.png)

Nous allons créer une classe `Interrogator` responsable de convaincre les animaux de parler. Nous ne voulons pas écrire une méthode pour chaque type d'animal : `convinceDogToTalk(Dog dog)`, `convinceCatToTalk(Cat cat)`, et ainsi de suite.

Nous préférerions une méthode générale qui accepterait n'importe quel animal. Comment pouvons-nous faire cela ?

```java
class Interrogator{
    public static void convinceToTalk(Animal subject) {
        subject.talk();
    }
}

// Nous ne voulons pas que quelqu'un crée un objet animal !
abstract class Animal {
    public abstract void talk();
}

class Dog extends Animal {
    public void talk() {
        System.out.println("Woof!");
    }
}

class Cat extends Animal {
    public void talk() {
        System.out.println("Meow!");
    }
}

public class App {
    public static void main(String[] args){
        Dog dog = new Dog();
        Cat cat = new Cat();
        Animal animal = new Dog();
        
        Interrogator.convinceToTalk(dog); // imprime "Woof!"
        Interrogator.convinceToTalk(cat); // imprime "Meow!"
        Interrogator.convinceToTalk(animal); // imprime "Woof!"
    }
}
```

Nous créons la méthode `convinceToTalk` pour accepter un objet `Animal` comme paramètre. À l'intérieur de la méthode, nous appelons la méthode `talk` de cet objet. Tant que le type de l'objet est un `Animal` ou une sous-classe de `Animal`, le compilateur est satisfait.

La machine virtuelle Java (JVM) décide à l'exécution quelle méthode sera appelée en fonction de la classe de l'objet. Si l'objet est de type `Dog`, la JVM invoque l'implémentation qui dit "Woof!" .

Cela présente deux avantages :

1. Nous n'avons besoin d'écrire qu'une seule méthode générale. Nous n'avons pas besoin de faire de vérification de type.
2. À l'avenir, si nous créons un nouveau type d'animal, nous n'avons pas besoin de modifier la classe `Interrogator`.

Ce type de polymorphisme est appelé le remplacement (overriding).

## Remplacement (Overriding)

L'exemple que nous avons discuté a déjà couvert le concept général du remplacement. Donnons une définition formelle et plus de détails.

Le remplacement est lorsque vous créez une implémentation différente de la **méthode d'instance exactement identique** (signature de méthode identique) dans une classe apparentée.

À l'exécution, la méthode du **type d'objet** est choisie. C'est pourquoi le remplacement est également appelé polymorphisme d'exécution.

Le remplacement est réalisé en fournissant une implémentation différente d'une méthode dans une classe enfant (sous-classe), qui est définie dans sa classe parente (superclasse).

![overriding inheritance](https://www.freecodecamp.org/news/content/images/2020/10/overriding-inheritance.png)

Le remplacement est également réalisé en fournissant différentes implémentations d'une méthode définie dans une interface.

![overriding interface](https://www.freecodecamp.org/news/content/images/2020/10/overriding-interface.png)

Règles pour remplacer une méthode :
1. Elle doit être une méthode définie par une relation EST-UN (par `extends` ou `implements`). C'est pourquoi vous pouvez la trouver appelée polymorphisme de sous-type.
2. Elle doit avoir la même liste d'arguments que la définition de méthode originale.
3. Elle doit avoir le même type de retour, ou un type de retour qui est une sous-classe du type de retour de la définition de méthode originale.
4. Elle ne peut pas avoir un modificateur d'accès plus restrictif.
5. Elle peut avoir un modificateur d'accès moins restrictif.
6. Elle ne doit *pas* lancer une nouvelle exception vérifiée ou plus large.
7. Elle peut lancer des exceptions vérifiées plus étroites, moins nombreuses ou aucune, par exemple une méthode qui déclare une *IOException* peut être remplacée par une méthode qui déclare une *FileNotFoundException* (parce qu'elle est une sous-classe de *IOException*).
8. La méthode de remplacement peut lancer n'importe quelle exception non vérifiée, indépendamment du fait que la méthode remplacée déclare l'exception.

> Recommandation : Utilisez l'annotation *@override* lors du remplacement de méthodes. Elle fournit une vérification des erreurs à la compilation sur la signature de la méthode. Cela vous aidera à éviter de violer les règles énumérées ci-dessus.

![override annotation](https://www.freecodecamp.org/news/content/images/2020/11/override-annotation.png)

### Interdire le remplacement

Si vous ne voulez pas qu'une méthode soit remplacée, déclarez-la comme finale.

```java
class Account {
    public final void withdraw(double amount) {
        double newBalance = balance - amount;
        
        if(newBalance > 0){
        	balance = newBalance;
        }
    }
}
```

### Méthodes statiques

**Vous ne pouvez pas remplacer une méthode statique**. Vous créez vraiment une définition *indépendante* de la méthode dans une classe apparentée.

```java
class A {
    public static void print() {
        System.out.println("in A");
    }
}

class B extends A {
    public static void print() {
        System.out.println("in B");
    }
}

class Test {
    public static void main(String[] args) {
        A myObject = new B();
        myObject.print(); // imprime "in A"
    }
}
```

L'exécution de la classe `Test` dans l'exemple ci-dessus imprimera "in A". Cela démontre que le remplacement ne se produit pas ici.

Si vous changez la méthode `print` dans les classes `A` et `B` pour en faire une méthode d'instance en supprimant `static` de la signature de la méthode, et que vous exécutez à nouveau la classe `Test`, elle imprimera "in B" à la place ! Le remplacement se produit maintenant.

**Rappelez-vous, le remplacement choisit la méthode en fonction du type de l'objet, et non du type de la variable.** 🧠

## Surcharge (polymorphisme fonctionnel)

La surcharge est lorsque vous créez différentes versions de la même méthode.

Le nom de la méthode doit être le même, mais nous pouvons changer les paramètres et le type de retour.

Dans la classe [Math](https://docs.oracle.com/javase/8/docs/api/java/lang/Math.html) de Java, vous trouverez de nombreux exemples de méthodes surchargées. La méthode `max` est surchargée pour différents types. Dans tous les cas, elle retourne le nombre avec la valeur la plus élevée parmi les 2 valeurs fournies, mais elle le fait pour différents types de nombres (non apparentés).

![overloading-max-example](https://www.freecodecamp.org/news/content/images/2020/10/overloading-max-example.png)

Le type de la variable (de référence) est ce qui détermine quelle méthode surchargée sera choisie. La surcharge est effectuée au moment de la compilation.

Les méthodes surchargées offrent plus de flexibilité aux personnes utilisant votre classe. Les personnes utilisant votre classe peuvent avoir des données dans différents formats, ou peuvent avoir différentes données disponibles selon différentes situations dans leur application.

Par exemple, la classe [List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html) surcharge la méthode `remove`. Une List est une collection ordonnée d'objets. Vous pouvez donc vouloir supprimer un objet à une position particulière (index) dans une liste. Ou vous ne connaissez peut-être pas la position et souhaitez simplement supprimer l'objet où qu'il soit. C'est pourquoi elle a 2 versions.

![list-overloaded-methods](https://www.freecodecamp.org/news/content/images/2020/10/list-overloaded-methods.png)

Les constructeurs peuvent également être surchargés.

Par exemple, la classe [Scanner](https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html) a de nombreuses entrées différentes qui peuvent être fournies pour créer un objet. Ci-dessous se trouve un petit aperçu des constructeurs qui répondent à cela.

![constructor](https://www.freecodecamp.org/news/content/images/2020/10/constructor.png)

Règles pour surcharger une méthode :

1. Elle doit avoir une liste d'arguments différente.
2. Elle peut avoir un type de retour différent.
3. Elle peut avoir des modificateurs d'accès différents.
4. Elle peut lancer des exceptions différentes.
5. Les méthodes d'une superclasse peuvent être surchargées dans une sous-classe.

## Différences entre le remplacement et la surcharge

1. Le remplacement doit être basé sur une méthode d'une relation EST-UN, la surcharge n'a pas besoin de l'être. La surcharge peut se produire au sein d'une seule classe.
2. Les méthodes remplacées sont choisies en fonction du type de l'objet, tandis que les méthodes surchargées sont choisies en fonction du type de la variable (de référence).
3. Le remplacement se produit à l'exécution, tandis que la surcharge se produit à la compilation.

## Polymorphisme paramétrique

Le polymorphisme paramétrique est réalisé grâce aux [génériques](https://docs.oracle.com/javase/tutorial/extra/generics/index.html) en Java.

Les génériques ont été ajoutés au langage dans la version 5.0. Ils ont été conçus pour étendre le système de types de Java afin de permettre « à un type ou une méthode de fonctionner sur des objets de divers types tout en fournissant une sécurité de type à la compilation ».

En gros, une forme générique d'une classe ou d'une méthode peut avoir tous ses types remplacés.

Un exemple simple est [ArrayList](https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html). La définition de la classe contient un générique, et il est signifié par `<E>`. Certaines des méthodes d'instance telles que `add` utilisent ce type générique dans leurs signatures.

![arraylist class definition](https://www.freecodecamp.org/news/content/images/2020/10/arraylist-definition-2.png)
    
![arraylist definition add methods](https://www.freecodecamp.org/news/content/images/2020/10/arraylist-definition-methods.png)
    
En fournissant un type entre crochets lorsque nous créons un objet `ArrayList`, nous remplissons les références génériques définies dans toute la classe. Donc, si nous créons un `ArrayList` avec le type générique `Dog`, la méthode `add` n'acceptera qu'un objet `Dog` comme argument.

![arraylist dog method signature](https://www.freecodecamp.org/news/content/images/2020/10/arraylist-dog-method-signature-1.png)
    
Il y a une erreur de compilation si vous essayez d'ajouter autre chose qu'un `Dog` ! Si vous utilisez un éditeur de code tel qu'IntelliJ, vous obtiendrez la ligne rouge ondulée pour mettre en évidence votre infraction (comme ci-dessous).
    
![arraylist type checking](https://www.freecodecamp.org/news/content/images/2020/10/arraylist-type-checking-1.png)   

## Mots de la fin

Le polymorphisme est un sujet délicat à maîtriser, surtout lorsque vous êtes nouveau en programmation. Il faut un certain temps pour identifier les bonnes situations pour l'utiliser dans votre code.

Mais une fois que vous vous sentez à l'aise avec cela, vous trouverez qu'il améliore beaucoup votre code.

## Attribution des photos

Photo de bannière par [Markus Spiske](https://unsplash.com/@markusspiske?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) sur Unsplash.