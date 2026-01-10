---
title: Définition SOLID – les principes SOLID de la conception orientée objet expliqués
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-04-26T21:16:00.000Z'
originalURL: https://freecodecamp.org/news/solid-principles-single-responsibility-principle-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/solid.jpg
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: solid
  slug: solid
seo_title: Définition SOLID – les principes SOLID de la conception orientée objet
  expliqués
seo_desc: "The SOLID design principles help us create maintainable, reusable, and\
  \ flexible software designs. Each letter in the acronym SOLID stands for a specific\
  \ principle. \nHere is what each letter in the acronym stands for:\n\nS: Single\
  \ responsibility princip..."
---

Les principes de conception **SOLID** nous aident à créer des conceptions logicielles maintenables, réutilisables et flexibles. Chaque lettre de l'acronyme **SOLID** représente un principe spécifique. 

Voici ce que représente chaque lettre de l'acronyme :

* **S** : Principe de responsabilité unique.
* **O** : Principe ouvert-fermé.
* **L** : Principe de substitution de Liskov.
* **I** : Principe de ségrégation des interfaces.
* **D** : Principe d'inversion des dépendances.

Dans cet article, nous commencerons par définir chaque principe, puis nous verrons quelques exemples pour vous aider à comprendre comment et pourquoi vous devriez utiliser ces principes dans votre code. 

Les exemples que nous utiliserons dans cet article seront très basiques. Nous utiliserons Java pour nos exemples.

Nous conclurons cet article en parlant des bases de la conception orientée objet.

## Le Principe de Responsabilité Unique (SRP)

L'idée derrière le SRP est que chaque classe, module ou fonction dans un programme devrait avoir une seule responsabilité/un seul but dans un programme. Selon une définition couramment utilisée, "chaque classe devrait avoir une seule raison de changer". 

Considérez l'exemple ci-dessous :

```java
public class Student {

     public void registerStudent() {
         // some logic
     }

     public void calculate_Student_Results() {
         // some logic
     }

     public void sendEmail() {
         // some logic
     }

}
```

La classe ci-dessus viole le principe de responsabilité unique. Pourquoi ?

Cette classe `Student` a trois responsabilités – inscrire les étudiants, calculer leurs résultats et envoyer des emails aux étudiants.

Le code ci-dessus fonctionnera parfaitement mais entraînera certains défis. Nous ne pouvons pas rendre ce code réutilisable pour d'autres classes ou objets. La classe contient une logique très interconnectée qui nous poserait des difficultés pour corriger les erreurs. Et à mesure que la base de code grandit, la logique aussi, rendant encore plus difficile la compréhension de ce qui se passe. 

Imaginez un nouveau développeur rejoignant une équipe avec ce type de logique dans une base de code d'environ deux mille lignes de code, toutes congestionnées dans une seule classe. 

Maintenant, corrigeons cela !

```java
public class StudentRegister {
    public void registerStudent() {
        // some logic
    }
}

```

```java
public class StudentResult {
    public void calculate_Student_Result() {
        // some logic
    }
}
```

```java
public class StudentEmails {
    public void sendEmail() {
        // some logic
    }
}

```

Maintenant, nous avons séparé chaque fonctionnalité dans notre programme. Nous pouvons appeler les classes n'importe où nous voulons les utiliser dans notre code. 

Les exemples que nous avons utilisés montrent simplement chaque classe ayant une méthode – cela est principalement pour la simplicité. Vous pouvez avoir autant de méthodes que vous voulez, mais elles doivent être liées à la responsabilité de la classe.

Maintenant que nous avons séparé la logique, notre code est plus facile à comprendre, chaque fonctionnalité principale ayant sa propre classe. Nous pouvons tester les erreurs plus efficacement.

Le code est maintenant réutilisable. Auparavant, nous ne pouvions utiliser ces fonctionnalités qu'à l'intérieur d'une seule classe, mais maintenant elles peuvent être utilisées dans n'importe quelle classe. 

Le code est également facilement maintenable et évolutif car, au lieu de lire des lignes de code interconnectées, nous avons séparé les préoccupations pour pouvoir nous concentrer sur les fonctionnalités que nous voulons développer.

## Principe Ouvert-Fermé (OCP)

Le principe ouvert-fermé stipule que les entités logicielles doivent être ouvertes à l'extension, mais fermées à la modification. 

Cela implique que ces entités – classes, fonctions, etc. – doivent être créées de manière à ce que leurs fonctionnalités principales puissent être étendues à d'autres entités sans altérer le code source de l'entité initiale. 

Dans l'exemple ci-dessous, nous allons écrire le code pour calculer l'indice de masse corporelle (IMC) d'une personne :

```java
public class Human  {
    
     public int height;
     public int weight;
     
}
```

Nous avons créé la classe `Human` qui fournit les propriétés `height` et `width` de la classe. Maintenant, calculons l'IMC de la première personne.

```java
public class CalculateBMI {

     public int CALCULATE_JOHN_BMI(Human John) {   
         
         return John.height/John.weight;
         
     }
}
```

Nous avons calculé l'IMC d'une personne nommée `John`. Nous allons continuer et calculer l'IMC pour une personne nommée `Jane`. 

```
public class CalculateBMI {

     public int CALCULATE_JOHN_BMI(Human John) {   
         
         return John.height/John.weight;
         
     }
     
     public int CALCULATE_JANE_BMI(Human Jane) {   
         
         return Jane.height/Jane.weight;
         
     }
}
```

Le problème avec cela est que nous modifions constamment le code chaque fois que nous devons calculer l'IMC d'une autre personne. 

Cela viole également le SRP car la classe a maintenant plus d'une raison de changer.

Bien que le code ci-dessus puisse fonctionner parfaitement, il n'est pas efficace. Nous modifions constamment le code, ce qui peut entraîner des bugs. Et le code ne prévoit que pour les humains. Que se passe-t-il si nous devons calculer pour un animal ou un objet ?

Résolvons le problème en utilisant le principe ouvert-fermé.

```java
public interface Entity {

     public int CalculateBMI();

}

// Entité John
public class John implements Entity {

     int height;
     int weight;

     public double CalculateBMI() {

           return John.height/John.weight;
     }
}

// Entité Jane
public class Jane implements Entity {

     int height;
     int weight;

     public double CalculateBMI() {

           return Jane.height/Jane.weight;
     }
}

// Entité Dog
public class Dog implements Entity {

     int height;
     int weight;

     public double CalculateBMI() {

           return Dog.height/Dog.weight;
     }
}
```

Dans le code ci-dessus, nous avons créé une interface appelée `Entity` avec une méthode `CalculateBMI()`. 

Chaque entité – `John`, `Jane` et `Dog` – étend la fonctionnalité de l'interface `Entity`. 

Maintenant, nous n'avons plus besoin de modifier le code existant lorsque nous créons une nouvelle entité - nous étendons simplement la fonctionnalité dont nous avons besoin et l'appliquons à la nouvelle entité. 

Ensuite, nous parlerons du Principe de Substitution de Liskov. 

## Principe de Substitution de Liskov (LSP)

Selon Barbara Liskov et Jeannette Wing, le principe de substitution de Liskov stipule que :

> _Soit _(x)_ une propriété prouvable sur les objets _x_ de type _T_. Alors _(y)_ devrait être vrai pour les objets _y_ de type _S_ où _S_ est un sous-type de _T_. (Source :_ [Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle#:~:text=Subtype%20Requirement%3A%20Let,a%20subtype%20of%20T)_)._

Ne vous inquiétez pas si vous trouvez cela confus, tout sera clair bientôt. Simplifions ce principe ci-dessous :

Le principe de substitution de Liskov implique simplement que lorsqu'une instance d'une classe est passée/étendue à une autre classe, la classe héritante doit avoir un cas d'utilisation pour toutes les propriétés et comportements de la classe héritée.

Supposons que nous avons une classe appelée `Amphibian` pour les animaux qui peuvent vivre à la fois sur terre et dans l'eau. Cette classe a deux méthodes pour montrer les caractéristiques d'un amphibien – `swim()` et `walk()`. 

```java
public class Amphibian {

    public void swim();
    public void walk();

}


```

La classe `Amphibian` peut s'étendre à une classe `Frog` car les grenouilles sont des amphibiens, donc elles peuvent hériter des propriétés de la classe `Amphibian` sans altérer la logique et le but de la classe.

```java
public class Frog extends Amphibian {
    public void swim() {
        System.out.println("The frog is swimming");
    }
    
    public void walk() {
        System.out.println("The frog is walking on land");
    }
}
```

Mais nous ne pouvons pas étendre la classe `Amphibian` à une classe `Dolphin` car les dauphins ne vivent que dans l'eau, ce qui implique que la méthode `walk()` serait sans pertinence pour la classe `Dolphin`.

Ainsi, lorsque vous étendez une classe, si certaines des propriétés de la classe initiale ne sont pas utiles pour la nouvelle classe, le principe de substitution de Liskov a été violé.

La solution à cela est simple : créer des interfaces qui correspondent aux besoins de la classe héritante.

En résumé, si une classe hérite d'une autre, elle devrait le faire de manière à ce que toutes les propriétés de la classe héritée restent pertinentes pour sa fonctionnalité.

## Principe de Ségrégation des Interfaces (ISP)

Le principe de ségrégation des interfaces stipule que l'interface d'un programme doit être divisée de manière à ce que l'utilisateur/client n'ait accès qu'aux méthodes nécessaires liées à ses besoins. 

Pour mieux comprendre cela, nous allons d'abord examiner un exemple qui viole l'ISP :

```java
public interface Teacher {

    void English();

    void Biology();

    void Chemistry();
    
    void Mathematics();

}
```

Nous avons créé une interface appelée `Teacher` qui a diverses matières comme méthodes. Étendons cette interface à notre premier enseignant. 

```java
public class Jane implements Teacher {

    @Override
    public void English() {
        System.out.println("Jane is teaching the students English language.");
    }

    @Override
    public void Biology() {
    }

    @Override
    public void Chemistry() {
    }

    @Override
    public void Mathematics() {
    }
}
```

D'après le code ci-dessus, vous pouvez voir que `Jane` est une enseignante d'anglais qui n'a rien à faire avec les autres matières. Mais ces autres méthodes sont étendues par défaut avec l'interface `Teacher`. 

Ne confondez pas le principe de substitution de Liskov et le principe de ségrégation des interfaces. Ils peuvent sembler similaires mais ne sont pas entièrement identiques.

Le principe de substitution de Liskov nous donne l'idée que lorsqu'une nouvelle classe a besoin d'hériter d'une classe existante, elle devrait le faire parce que cette nouvelle classe a besoin des méthodes que la classe existante possède.

D'autre part, le principe de ségrégation des interfaces nous fait comprendre qu'il est inutile et déraisonnable de créer une interface avec beaucoup de méthodes, car certaines de ces méthodes peuvent être sans pertinence pour les besoins d'un utilisateur particulier lorsqu'elles sont étendues.

Maintenant, corrigeons le code du dernier exemple.

```java
public interface Teacher {

    void Teach();

}
```

L'interface `Teacher` n'a maintenant qu'une seule méthode. Continuons et étendons cette interface pour supporter les différentes matières. 

```java
// Interface enseignant d'anglais

public interface EnglishTeacher extends Teacher {

    void English();

}
```

```java
// Interface enseignant de biologie

public interface BiologyTeacher extends Teacher {

    void Bilogy();

}
```

```java
// Interface enseignant de chimie

public interface ChemistryTeacher extends Teacher {

    void Chemistry();

}
```

```java
// Interface enseignant de mathématiques

public interface MathematicsTeacher extends Teacher {

    void Mathematics();

}
```

Nous avons créé différentes interfaces pour chaque matière. Maintenant, `Jane` peut enseigner l'anglais sans emporter les autres méthodes avec elle. Voici un exemple :

```java
public class Jane implements EnglishTeacher {
    
    @Override
    public void Teach() {
        System.out.println("Jane has started teaching.");
    }

    @Override
    public void English() {
        System.out.println("Jane is teaching the students English language.");
    }

}
```

## Principe d'Inversion des Dépendances (DIP)

Le principe d'inversion des dépendances stipule :

> Les modules de haut niveau ne doivent rien importer des modules de bas niveau. Les deux doivent dépendre d'abstractions (par exemple, interfaces). _(Source :_ [Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle#:~:text=Subtype%20Requirement%3A%20Let,a%20subtype%20of%20T)_)._

Et,

> Les abstractions ne doivent pas dépendre des détails. Les détails (implémentations concrètes) doivent dépendre des abstractions. _(Source :_ [Wikipedia](https://en.wikipedia.org/wiki/Liskov_substitution_principle#:~:text=Subtype%20Requirement%3A%20Let,a%20subtype%20of%20T)_)._

Utilisons un exemple concret avant d'écrire du code. 

Imaginez faire une marche d'une minute à la banque chaque fois que vous devez retirer de l'argent au guichet. Cela prend ensuite trente secondes supplémentaires pour obtenir votre argent. C'est assez efficace car très peu de temps est perdu. Nous supposerons que vous êtes le module de haut niveau et que la banque est le module de bas niveau. 

Mais que se passe-t-il lorsque la banque est fermée pour un jour férié ou une urgence ? Vous n'avez absolument aucun accès à vos fonds. Si vous vous éloignez davantage de la banque, cela devient un problème plus important car vous passeriez plus de temps à vous y rendre.

Pour résoudre ce problème, une interface est introduite – un guichet automatique (GAB) ou une application de banque mobile. Même si vous avez une relation avec la banque, vous n'êtes plus obligé d'interagir physiquement avec eux pour être servi.

Cet exemple est similaire au principe d'inversion des dépendances. Nous devons faire en sorte que nos classes dépendent des propriétés de nos interfaces au lieu de dépendre les unes des autres. 

Les implications de la violation de ce principe entraîneraient un système rigide où le test de blocs de code indépendamment serait très difficile, la réutilisation du code serait presque impossible, et l'ajout ou la suppression de code entraînerait une complexité accrue du système et introduirait des bugs.

Voici un exemple de code qui viole ce principe :

```java
public class Bank {

    public void GIVE_CUSTOMER_MONEY_OTC() {
        // some logic
    }
}
```

```java
public class Customer {
    private Bank myBank = new Bank();
    
    public void withdraw() {
        myBank.GIVE_CUSTOMER_MONEY_OTC();
    }
}
```

D'après les exemples de code ci-dessus, nous pouvons voir que la classe `Customer` importe et dépend d'une méthode de la classe `Bank`. Cette dépendance à une classe de bas niveau est contraire au DIP. 

Comme dans notre exemple concret, nous allons résoudre ce problème en introduisant une interface avec laquelle les deux classes peuvent interagir. 

Voici l'interface ATM avec laquelle nos classes `Bank` et `Customer` interagiront :

```java
public interface ATM {
    void ATM_OPERATION();
}
```

Voici la classe `Bank` qui utilise une méthode de l'interface `ATM` pour ajouter de l'argent au GAB :

```java
public class Bank implements ATM {
    @Override
    ATM_OPERATION(){
        // code to add money to ATM and increase the ATM balance
    }
}
```

Enfin, la classe `Customer` qui utilise la même interface pour retirer de l'argent :

```java
public class Customer implements ATM {
    
    @Override
    ATM_OPERATION(){
        // code to withdraw money from ATM and decrease the ATM balance
    }
}
```

## Qu'est-ce que la Conception Orientée Objet ?

La conception orientée objet est une méthodologie de conception pour construire des systèmes et des applications basés sur des objets. Cela nous permet de construire des systèmes avec une collection d'objets où chaque objet a ses propres propriétés et méthodes.

Prenons le système informatique comme exemple. Son matériel est composé de différentes parties qui constituent le système entier.

Voici quelques termes généraux associés à la conception orientée objet :

* **Objets** : Chaque unité séparée qui compose le système est un objet. Les objets peuvent avoir des propriétés et des méthodes.
* **Classes** : Les classes servent de description générale pour les objets. Ainsi, un objet est une instance d'une classe. 
* **Encapsulation** : cela aide à regrouper toutes les données pertinentes d'un objet en une seule unité. Cela aide également à restreindre l'accès à des données et méthodes spécifiques qui ne devraient se trouver que dans un seul objet.
* **Héritage** : L'héritage facilite l'extension de la fonctionnalité d'une classe à d'autres classes. De cette manière, nous ne répétons pas le processus de création de ces fonctionnalités encore et encore.
* **Abstraction** : Cela signifie montrer uniquement les attributs importants et masquer ceux qui ne le sont pas.
* **Polymorphisme** : Il s'agit de l'existence d'une interface sous diverses formes. La capacité d'étendre un objet/une interface mais avec des attributs différents ou supplémentaires.

## Conclusion

Il existe de nombreuses façons de résoudre un problème. Mais il existe également de nombreuses façons de créer des problèmes à partir d'une solution.

Plus les classes et méthodes de notre code sont rigides et couplées, plus il sera difficile de maintenir et de réutiliser notre code.

Négliger ou violer ces principes pourrait poser une sérieuse menace non seulement pour la base de code et le développeur, mais aussi pour l'organisation qui possède le produit.

Une base de code rigide et fortement couplée rend difficile l'ajout ou la suppression de fonctionnalités dans un produit, le test et la réutilisation de blocs de code, et introduit des changements potentiellement cassants avec chaque modification de code effectuée.

Les principes SOLID servent de guide pour nous aider à créer un produit flexible et dynamique, et nous avons passé en revue chaque principe dans cet article pour nous aider à comprendre comment les objets que nous créons doivent interagir les uns avec les autres.

J'espère que vous trouverez cet article utile alors que vous continuez votre voyage à travers la conception orientée objet.

Bon codage !