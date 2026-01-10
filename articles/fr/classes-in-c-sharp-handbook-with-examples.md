---
title: Le guide des classes C# – Les types de classes avec exemples de code
date: '2024-12-20T16:20:41.910Z'
author: Isaiah Clifford Opoku
authorURL: https://www.freecodecamp.org/news/author/Clifftech/
originalURL: https://freecodecamp.org/news/classes-in-c-sharp-handbook-with-examples
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1734711601436/b4de90be-1d93-4d8d-a4ed-ae09b192ef5c.png
tags:
- name: C#
  slug: csharp
- name: dotnet
  slug: dotnet
- name: classes
  slug: classes
- name: handbook
  slug: handbook
seo_desc: 'Classes are the fundamental building blocks of object-oriented programming
  in C#. They allow you to create reusable and modular code by grouping related data
  and functions.

  Different types of classes serve various purposes. For instance, organizing y...'
---


Les classes sont les briques fondamentales de la programmation orientée objet en C#. Elles vous permettent de créer un code réutilisable et modulaire en regroupant des données et des fonctions liées.

<!-- more -->

Différents types de classes répondent à divers besoins. Par exemple, organiser votre logique pour rendre votre code plus facile à parcourir est utile lors de la construction d'une application.

Vous pouvez regrouper ou séparer votre code en classes et, grâce à l'héritage, vous pouvez utiliser différentes classes selon vos besoins. Les classes aident à encapsuler votre code, vous permettant de réutiliser votre logique dans d'autres parties de l'application. Les classes possèdent de nombreuses fonctionnalités, et nous en explorerons certaines en détail.

Dans ce guide, nous explorerons les différents types de classes en C# et comment vous pouvez les utiliser pour créer un code efficace et maintenable.

## **Prérequis**

Avant de continuer, vous devriez avoir les éléments suivants :

1.  **Connaissances de base en C#** : vous devez comprendre la syntaxe C# et les constructions de programmation de base comme les variables, les boucles et les conditionnels.
    
2.  **Familiarité avec les concepts de Programmation Orientée Objet (POO)** : vous devez savoir comment travailler avec les classes, les objets, l'héritage, le polymorphisme, l'encapsulation et l'abstraction.
    
3.  **Familiarité avec les modificateurs d'accès** : vous devez comprendre les modificateurs d'accès public, private, internal et protected.
    
4.  **Expérience avec un IDE/Environnement C#** : vous devriez être capable d'écrire et d'exécuter des programmes C# en utilisant un IDE comme Visual Studio.
    

Si vous souhaitez en savoir plus sur le C#, vous pouvez consulter ma chaîne YouTube : [CliffTech][1].

## Table des matières

-   [Classes statiques en C#][2]
    
-   [Classes scellées en C#][3]
    
-   [Classes concrètes en C#][4]
    
-   [Classes abstraites en C#][5]
    
-   [Classes Singleton en C#][6]
    
-   [Classes génériques en C#][7]
    
-   [Classes internes en C#][8]
    
-   [Classes imbriquées en C#][9]
    
-   [Classes partielles en C#][10]
    
-   [Conclusion][11]
    

Le premier type de classe dont nous allons discuter est la classe statique. Plongeons dedans.

## Classes statiques en C#

Les classes statiques sont un type spécial de classe en C# conçu pour fournir une collection de méthodes utilitaires et de propriétés liées qui ne dépendent pas des données d'instance.

Les classes statiques en C# sont un type unique de classe conçu pour héberger une collection de méthodes utilitaires et de propriétés liées qui ne dépendent pas des données d'instance.

Contrairement aux classes régulières, les classes statiques ne peuvent pas être instanciées et elles contiennent exclusivement des membres statiques. Cette caractéristique signifie qu'elles ne peuvent pas être héritées, ce qui les rend parfaites pour organiser des méthodes sans état (stateless) qui ne nécessitent pas les fonctionnalités de la programmation orientée objet.

En essence, lorsque nous parlons de regroupement sans état, cela implique qu'il n'est pas nécessaire de créer une instance pour appeler une méthode statique – vous pouvez simplement utiliser le nom de la classe ou de la méthode directement. Cette approche offre un moyen clair et efficace de gérer les fonctions utilitaires, améliorant l'organisation du code et l'accessibilité.

### Exemple d'une classe statique en C#

Voici un exemple de classe statique en C# :

```
namespace StaticClasses
{
// Define a static class
    public static class MathUtils
    {
        // Static method to add two numbers
        public static int Add(int a, int b)
        {
            return a + b;
        }

        // Static method to subtract two numbers
        public static int Subtract(int a, int b)
        {
            return a - b;
        }

       // Static method to multiply two numbers
        public static int Multiply(int a, int b)
        {
            return a * b;
        }
    }
}
```

Dans cet exemple :

-   La classe `MathUtils` est définie comme `static`, ce qui signifie qu'elle ne peut pas être instanciée.
    
-   Elle contient trois méthodes statiques : `Add`, `Subtract`, et `Multiply`.
    
-   Ces méthodes peuvent être appelées directement sur la classe `MathUtils` sans créer d'instance.
    

Avant de pouvoir l'utiliser, vous devez l'appeler dans votre `Program.cs`. Lorsque vous créez une application C#, le point d'entrée est `Program.cs`. Vous devrez vous y rendre et vous assurer d'appeler ces classes afin de pouvoir les exécuter. C'est ce que nous ferons pour le reste de cette section.

### Comment utiliser les méthodes statiques dans `Program.cs`

Vous pouvez maintenant utiliser les méthodes statiques définies dans la classe `MathUtils` comme suit :

```

 // program.cs
namespace StaticClasses
{
    class Program
    {
        static void Main(string[] args)
        {
             // Call static methods from the MathUtils class
            int sum = MathUtils.Add(5, 3);
            // Call the static method Subtract from the MathUtils class
            int difference = MathUtils.Subtract(5, 3);

            // Call the static method Multiply from the MathUtils class
            int product = MathUtils.Multiply(5, 3);

            // Display the results of the sum method
            Console.WriteLine($"Sum: {sum}"); // Output: 8
            // Display the results of the difference method
            Console.WriteLine($"Difference: {difference}"); // Output: 2
            // Display the results of the product method
            Console.WriteLine($"Product: {product}");  // Output: 15
        }
    }
}
```

### Quand utiliser des classes statiques vs des méthodes statiques

Pour décider quand utiliser des classes ou des méthodes statiques en C#, considérez les directives suivantes :

1.  **Utilisez des classes statiques quand :**
    
    -   Vous avez besoin d'une collection de méthodes utilitaires ou d'aide (helpers) qui ne nécessitent aucune donnée d'instance.
        
    -   Les méthodes et propriétés sont sans état et peuvent être accédées globalement sans créer d'objet.
        
    -   Vous voulez regrouper des fonctions liées qui ne sont pas liées à un état d'objet spécifique.
        
    -   Vous devez garantir que la classe ne peut être ni instanciée ni héritée.
        
2.  **Utilisez des méthodes statiques quand :**
    
    -   Vous avez une classe qui est principalement basée sur l'instance, mais vous avez besoin de quelques méthodes qui ne dépendent pas des données d'instance.
        
    -   La méthode effectue une tâche indépendante de tout état d'objet et peut être exécutée sans instance.
        
    -   Vous voulez fournir une fonction utilitaire au sein d'une classe qui peut être accédée sans créer d'objet de cette classe.
        

En utilisant les classes et méthodes statiques de manière appropriée, vous pouvez améliorer l'organisation du code, augmenter les performances en évitant la création d'objets inutiles et garantir que certaines fonctionnalités sont facilement accessibles dans toute votre application.

### Points clés à retenir sur les classes statiques en C#

-   **Ne peut pas être instanciée** : Vous ne pouvez pas créer d'objets à partir d'une classe statique.
    
-   **Membres statiques uniquement** : Les classes statiques ne peuvent avoir que des membres statiques. Elles ne supportent pas les méthodes ou champs d'instance.
    
-   **Scellée par défaut** : Les classes statiques sont automatiquement scellées (sealed), elles ne peuvent donc pas être héritées.
    
-   **Méthodes utilitaires et d'aide** : Les classes statiques sont généralement utilisées pour regrouper des méthodes utilitaires ou d'aide liées qui n'ont pas besoin d'un état d'objet.
    

Les classes statiques aident à organiser et à accéder aux méthodes et propriétés utilitaires de manière claire et simple, ce qui les rend importantes pour créer un code efficace et maintenable.

## Classes scellées en C#

Les classes scellées (sealed classes) sont un type spécial de classe en C# qui ne peut pas être héritée. Vous pouvez les utiliser pour empêcher d'autres classes de dériver d'elles, ce qui peut être utile pour créer des types immuables ou garantir que le comportement d'une classe reste inchangé.

En scellant une classe, vous garantissez qu'elle ne peut pas être modifiée ou étendue, ce qui la rend utile pour les scénarios où vous souhaitez fournir une implémentation spécifique sans permettre d'altérations ultérieures.

### Exemple d'une classe scellée en C#

Voici un exemple de classe scellée en C# :

```
namespace SealedClasses
{

    // Define an abstract class
    public abstract class Shape
    {
        // Abstract method to calculate the area
        public abstract double CalculateArea();
    }

     // Define a sealed class
    public sealed class Rectangle : Shape
    {

        //  Properties
        public double Width { get; }
        public double Height { get; }

        // Constructor
        public Rectangle(double width, double height)
        {
            Width = width;
            Height = height;
        }

       // Implement the CalculateArea method
        public override double CalculateArea()
        {
            return Width * Height;
        }
    }
}
```

Dans cet exemple :

-   La classe `Shape` est une classe de base abstraite avec une méthode abstraite `CalculateArea()`.
    
-   La classe `Rectangle` hérite de `Shape` et fournit une implémentation pour `CalculateArea()`.
    
-   La classe `Rectangle` est scellée (`sealed`), ce qui signifie qu'on ne peut pas en hériter. Cela garantit que l'implémentation de la classe ne peut être ni modifiée ni étendue.
    

### Comment utiliser la classe scellée Rectangle dans le Program.cs

Voici comment vous pouvez utiliser la classe `Rectangle` dans un fichier `Program.cs` :

```
namespace SealedClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            Rectangle rectangle = new Rectangle(5, 3);
            double area = rectangle.CalculateArea();

            Console.WriteLine($"Area of the rectangle: {area}"); // Output: Area of the rectangle: 15
        }
    }
}
```

Dans cet exemple, la classe `Rectangle` est scellée pour garantir que son comportement ne peut pas être modifié par héritage. Cela garantit que l'implémentation de `CalculateArea()` de la classe `Rectangle` reste la même, ce qui aide à maintenir un comportement cohérent.

### Quand utiliser des classes scellées

Les classes scellées sont particulièrement utiles dans les contextes suivants :

1.  **Développement de frameworks** : Lors du développement de frameworks ou de bibliothèques, vous pourriez utiliser des classes scellées pour verrouiller certaines classes qui ne sont pas destinées à être étendues par les utilisateurs. Cela aide à garder le contrôle sur le comportement du framework et garantit que les utilisateurs ne peuvent pas introduire de bugs ou d'incohérences en étendant ces classes.
    
2.  **Empêcher l'héritage** : Si une classe est conçue pour être une implémentation spécifique sans besoin de personnalisation ou d'extension supplémentaire, la sceller empêche d'autres développeurs de créer des sous-classes qui pourraient altérer sa fonctionnalité prévue.
    
3.  **Finaliser la conception d'une classe** : Lorsqu'une classe a atteint un point où sa conception est considérée comme complète et qu'aucun changement ou extension n'est anticipé, la sceller peut signaler aux autres développeurs que la classe doit être utilisée telle quelle.
    
4.  **Éviter la redéfinition (overriding)** : Dans les scénarios où la redéfinition de méthodes pourrait conduire à un comportement incorrect ou à des problèmes de sécurité, sceller la classe garantit que ses méthodes ne peuvent pas être redéfinies, préservant la logique et la fonctionnalité originales.
    

### Points clés à retenir sur les classes scellées

-   **Pas d'héritage** : Les classes scellées ne peuvent pas être héritées, garantissant que leur comportement reste le même.
    
-   **Empêcher la modification** : Elles empêchent tout héritage ultérieur, évitant les changements ou extensions accidentels.
    
-   **Immuables et spécifiques** : Les classes scellées sont utiles pour créer des classes immuables ou lorsque vous avez besoin d'une implémentation spécifique et inchangeable.
    

### Classes scellées vs Classes statiques

Vous pourriez vous demander pourquoi nous avons besoin de classes scellées si les classes statiques sont déjà scellées. Les différences clés sont :

-   **Les classes statiques** sont scellées et ne peuvent pas être instanciées. Elles sont utilisées pour regrouper des méthodes et propriétés statiques.
    
-   **Les classes scellées** peuvent être instanciées mais ne peuvent pas être héritées. Cela permet de créer des objets qui sont protégés contre toute sous-classification ultérieure.
    

Les classes scellées offrent une flexibilité dans la création de classes qui peuvent être utilisées directement sans risque de modification par héritage.

## Classes concrètes en C#

Les classes concrètes sont essentielles dans la programmation orientée objet en C#. Ce sont des classes entièrement implémentées que vous pouvez utiliser pour créer des objets directement.

Contrairement aux `classes abstraites` ou aux `interfaces`, les classes concrètes possèdent des implémentations complètes de toutes leurs méthodes et propriétés, ce qui les rend polyvalentes et fondamentales pour la plupart des applications C#.

Une classe concrète n'est pas abstraite. Elle inclut des implémentations complètes de tous ses membres — méthodes, propriétés, champs, etc. — et peut être utilisée pour créer des objets. Ces classes représentent des entités ou des concepts du monde réel dans votre application, encapsulant à la fois les données (stockées dans des champs ou propriétés) et le comportement (défini par des méthodes).

### Exemple : Définir une classe concrète en C#

Voici un exemple simple de classe concrète en C# :

```


// Define a concrete class
public class Animal
{
    public void Speak()
    {
        Console.WriteLine("The animal makes a sound.");
    }
}

// Define a derived class that inherits from the Animal class
public class Dog : Animal
{
    public void Bark()
    {
        Console.WriteLine("The dog barks.");
    }
}
```

Dans cet exemple, la classe `Animal` est une classe concrète avec une méthode `Speak` qui représente un son générique émis par n'importe quel animal. La classe `Dog` hérite d' `Animal` et ajoute une méthode `Bark` pour représenter un son spécifique aux chiens. `Animal` et `Dog` sont toutes deux des classes concrètes car elles peuvent être instanciées et utilisées pour créer des objets.

### Comment instancier et utiliser des classes concrètes

Voici comment vous pouvez utiliser la classe `Dog` dans un fichier `Program.cs` :

```

// program.cs
class Program
{
    static void Main(string[] args)
    {
        // Create an instance of the Dog class
        Dog myDog = new Dog();

        // Call the inherited method
        myDog.Speak(); // Output: The animal makes a sound.

        // Call the method defined in the Dog class
        myDog.Bark();  // Output: The dog barks.
    }
}
```

Dans cet exemple, nous créons une instance de la classe `Dog` appelée `myDog`. Nous appelons d'abord la méthode `Speak`, qui est héritée de la classe `Animal`, puis la méthode `Bark` de la classe `Dog`. Cela montre comment les classes concrètes peuvent inclure à la fois des comportements hérités et uniques.

### Exemple concret : Classe concrète pour un produit

Pour illustrer l'application pratique des classes concrètes, considérons l'exemple suivant d'une classe `Product` :

```
// Define a concrete class for a product
public class Product
{
    // Data properties
    public string Name { get; set; }
    public decimal Price { get; set; }

    // Method to display product information
    public void DisplayInfo()
    {
        Console.WriteLine($"Product: {Name}, Price: {Price:C}");
    }
}
```

Cette classe `Product` est une classe concrète avec des propriétés `Name` et `Price` pour stocker des informations sur un produit. La méthode `DisplayInfo` fournit un moyen d'afficher les détails du produit.

#### Comment utiliser la classe `Product`

Voici comment vous pouvez utiliser la classe `Product` :

```
class Program
{
    static void Main(string[] args)
    {
        // Create an instance of the Product class
        Product product = new Product
        {
            Name = "Laptop",
            Price = 1299.99m
        };

        // Display product information
        product.DisplayInfo(); // Output: Product: Laptop, Price: $1,299.99
    }
}
```

Dans ce scénario, la classe `Product` est utilisée pour créer un objet `product`. La méthode `DisplayInfo` est appelée pour montrer le nom et le prix du produit. Cela démontre comment les classes concrètes sont utilisées pour modéliser et travailler avec des données du monde réel.

### Points clés à retenir sur les classes concrètes

-   **Instanciables** : Les classes concrètes peuvent être instanciées, vous permettant de créer des objets qui représentent des entités ou des concepts spécifiques dans votre application.
    
-   **Implémentation complète** : Les classes concrètes fournissent des implémentations complètes de toutes les méthodes et propriétés, contrairement aux classes abstraites ou aux interfaces.
    
-   **Usage courant** : Elles sont le type de classe le plus courant en C#, utilisées pour définir des objets avec un comportement et des données spécifiques.
    

Les classes concrètes sont essentielles pour le développement en C#, vous permettant de définir et de travailler avec des objets qui modélisent des entités du monde réel au sein de vos applications. Comprendre comment utiliser efficacement les classes concrètes est crucial pour construire des logiciels robustes et orientés objet.

## Classes abstraites en C#

En C#, les classes abstraites sont une fonctionnalité puissante qui vous permet de définir un modèle pour d'autres classes sans fournir d'implémentations complètes. Elles servent de classes de base qui ne peuvent pas être instanciées directement, mais peuvent être héritées par d'autres classes qui fourniront des implémentations spécifiques pour les méthodes abstraites définies en leur sein. Cette conception aide à imposer une cohérence entre des classes liées tout en permettant une flexibilité dans la manière dont certains comportements sont implémentés.

### Que signifie "Instancié" ?

Avant d'explorer les classes abstraites, clarifions ce que signifie instancier une classe. L'instanciation est le processus de création d'un objet à partir d'une classe. Lorsque vous utilisez le mot-clé `new` en C#, vous créez une instance (ou objet) de cette classe.

Mais les classes abstraites ne peuvent pas être instanciées directement. Elles doivent être héritées par une classe non abstraite (concrète) qui fournit des implémentations pour les méthodes abstraites.

### Comprendre les classes abstraites et les méthodes abstraites

**Les classes abstraites** sont des classes à partir desquelles vous ne pouvez pas créer d'objets directement. Elles agissent comme des modèles pour d'autres classes. Elles peuvent avoir à la fois des méthodes complètes et des méthodes sans corps (méthodes abstraites). Les classes abstraites aident à mettre en place une interface commune et un comportement partagé pour des classes liées.

**Les méthodes abstraites**, quant à elles, sont des méthodes dans une classe abstraite qui n'ont pas de corps. Toute classe non abstraite qui hérite de la classe abstraite doit fournir un corps pour ces méthodes. Cela garantit que toutes les sous-classes ont une interface cohérente.

### Exemple concret : Gestion de comptes bancaires

Explorons un exemple concret pour illustrer le concept de classes abstraites et de méthodes abstraites en C#.

```
using System;

// define an abstract class
namespace AbstractClasses
{
    // Abstract class
    public abstract class BankAccount
    {
        // Properties
        public string AccountNumber { get; private set; }
        public decimal Balance { get; protected set; }

        // Constructor
        public BankAccount(string accountNumber, decimal initialBalance)
        {
            AccountNumber = accountNumber;
            Balance = initialBalance;
        }

        // Abstract methods
        public abstract void Deposit(decimal amount);
        public abstract void Withdraw(decimal amount);
        public abstract void DisplayAccountInfo();
    }

    // Derived class: SavingsAccount
    public class SavingsAccount : BankAccount
    {
        private decimal interestRate;

        public SavingsAccount(string accountNumber, decimal initialBalance, decimal interestRate)
            : base(accountNumber, initialBalance)
        {
            this.interestRate = interestRate;
        }

        // Implementing abstract methods
        public override void Deposit(decimal amount)
        {
            Balance += amount;
            Console.WriteLine($"Deposited {amount} to Savings Account {AccountNumber}. New Balance: {Balance}");
        }

        public override void Withdraw(decimal amount)
        {
            if (amount > Balance)
            {
                throw new InvalidOperationException("Insufficient funds.");
            }
            Balance -= amount;
            Console.WriteLine($"Withdrew {amount} from Savings Account {AccountNumber}. New Balance: {Balance}");
        }

        public override void DisplayAccountInfo()
        {
            Console.WriteLine($"Savings Account {AccountNumber} - Balance: {Balance}, Interest Rate: {interestRate}%");
        }
    }

    // Derived class: CheckingAccount
    public class CheckingAccount : BankAccount
    {
        private decimal overdraftLimit;

        public CheckingAccount(string accountNumber, decimal initialBalance, decimal overdraftLimit)
            : base(accountNumber, initialBalance)
        {
            this.overdraftLimit = overdraftLimit;
        }

        // Implementing abstract methods
        public override void Deposit(decimal amount)
        {
            Balance += amount;
            Console.WriteLine($"Deposited {amount} to Checking Account {AccountNumber}. New Balance: {Balance}");
        }

        public override void Withdraw(decimal amount)
        {
            if (amount > Balance + overdraftLimit)
            {
                throw new InvalidOperationException("Overdraft limit exceeded.");
            }
            Balance -= amount;
            Console.WriteLine($"Withdrew {amount} from Checking Account {AccountNumber}. New Balance: {Balance}");
        }

        public override void DisplayAccountInfo()
        {
            Console.WriteLine($"Checking Account {AccountNumber} - Balance: {Balance}, Overdraft Limit: {overdraftLimit}");
        }
    }
}
```

Dans cet exemple, la classe `BankAccount` est une classe abstraite qui définit une interface commune pour différents types de comptes bancaires. Elle inclut des méthodes abstraites comme `Deposit`, `Withdraw`, et `DisplayAccountInfo`, qui doivent être implémentées par toute classe héritant de `BankAccount`.

Les classes `SavingsAccount` et `CheckingAccount` héritent de `BankAccount` et fournissent des implémentations spécifiques pour ces méthodes abstraites. Cette conception impose que chaque type de compte bancaire implémente les fonctions de dépôt, de retrait et d'affichage, tout en permettant à chaque type de compte d'implémenter ces fonctions d'une manière qui a du sens pour ce type spécifique.

### Comment utiliser des classes abstraites dans un programme

Voyons comment nous pouvons utiliser les classes `SavingsAccount` et `CheckingAccount` dans un fichier `Program.cs`.

```
namespace AbstractClasses
{
    class Program
    {
        static void Main(string[] args)
        {
            // Create a savings account
            BankAccount savings = new SavingsAccount("SA123", 1000, 1.5m);
            // Create a checking account
            BankAccount checking = new CheckingAccount("CA123", 500, 200);

            // Deposit and withdraw from the savings account
            savings.DisplayAccountInfo();

           // Deposit and withdraw from the checking account
            savings.Deposit(200);

            savings.Withdraw(100);
            // Display the updated account information
            savings.DisplayAccountInfo();

            checking.DisplayAccountInfo();

             // Deposit and withdraw from the checking account
            checking.Deposit(300);

            checking.Withdraw(600);

            // Display the updated account information
            checking.DisplayAccountInfo();

            try
            {
                checking.Withdraw(200);
            }
            catch (InvalidOperationException ex)
            {
                Console.WriteLine($"Error: {ex.Message}");
            }

            checking.DisplayAccountInfo();
        }
    }
}
```

Ce programme produira la sortie suivante :

```
Savings Account SA123 - Balance: 1000, Interest Rate: 1.5%
Deposited 200 to Savings Account SA123. New Balance: 1200
Withdrew 100 from Savings Account SA123. New Balance: 1100
Savings Account SA123 - Balance: 1100, Interest Rate: 1.5%
Checking Account CA123 - Balance: 500, Overdraft Limit: 200
Deposited 300 to Checking Account CA123. New Balance: 800
Withdrew 600 from Checking Account CA123. New Balance: 200
Checking Account CA123 - Balance: 200, Overdraft Limit: 200
Withdrew 200 from Checking Account CA123. New Balance: 0
Checking Account CA123 - Balance: 0, Overdraft Limit: 200
```

Dans cet exemple, les objets `SavingsAccount` et `CheckingAccount` sont créés, et les méthodes abstraites `Deposit`, `Withdraw`, et `DisplayAccountInfo` sont appelées. La classe abstraite `BankAccount` garantit que les deux types de comptes possèdent ces méthodes, tandis que les classes dérivées fournissent la fonctionnalité spécifique.

### Points clés à retenir sur les classes abstraites

-   **Ne peuvent pas être instanciées** : Vous ne pouvez pas créer une instance d'une classe abstraite directement. Une sous-classe doit en hériter et fournir les implémentations pour les méthodes abstraites.
    
-   **Contiennent des méthodes abstraites** : Les méthodes abstraites dans une classe abstraite n'ont pas de corps. Toute classe non abstraite héritant de la classe abstraite doit implémenter ces méthodes.
    
-   **Définissent des interfaces communes** : Les classes abstraites fixent une interface commune pour des classes liées, garantissant leur cohérence tout en permettant différentes implémentations.
    

Les classes abstraites sont importantes en C#. Elles aident à imposer une structure à travers des classes liées tout en permettant des détails spécifiques. En utilisant des classes abstraites, vous pouvez rendre votre code plus organisé, plus facile à maintenir et à étendre.

## Classes Singleton en C#

Les classes Singleton sont un patron de conception (design pattern) qui restreint l'instanciation d'une classe à une seule et unique instance. C'est particulièrement utile lorsque vous avez besoin d'une ressource unique et partagée dans toute votre application, comme un gestionnaire de configuration, un service de journalisation (logging) ou une connexion à une base de données.

### Pourquoi utiliser des classes Singleton en C# ?

Imaginez que vous ayez une classe responsable de la gestion d'une connexion à une base de données. Vous ne voulez pas que plusieurs instances de cette classe circulent, causant potentiellement des problèmes de gestion des ressources ou des données incohérentes. Une classe Singleton garantit qu'une seule instance est créée et fournit un point d'accès global à celle-ci.

### Exemple : Définir une classe Singleton

Voyons maintenant comment vous pouvez implémenter une classe Singleton en C# :

```
// Define a singleton class
public class Singleton
{
    private static Singleton instance;
    private static readonly object lockObject = new object();

    // Private constructor prevents instantiation from outside the class
    private Singleton()
    {
    }

    // Public property to access the single instance of the class
    public static Singleton Instance
    {
        get
        {
            // Ensure thread safety
            lock (lockObject)
            {
                if (instance == null)
                {
                    instance = new Singleton();
                }
            }
            return instance;
        }
    }

    // Example method to demonstrate the singleton instance
    public void PrintMessage()
    {
        Console.WriteLine("Hello, I am a singleton class.");
    }
}
```

Dans cet exemple, la classe `Singleton` est définie avec un constructeur privé, ce qui empêche d'autres classes de créer de nouvelles instances. La propriété statique `Instance` retourne l'instance unique de la classe, en la créant si elle n'existe pas déjà. Le `lockObject` garantit que la classe est "thread-safe", ce qui signifie que même dans un environnement multi-thread, une seule instance sera créée.

La méthode `PrintMessage` est juste un exemple simple pour montrer que l'instance Singleton peut être utilisée comme n'importe quelle autre instance de classe.

### Comment utiliser la classe Singleton dans `Program.cs`

Voyons maintenant comment vous pouvez utiliser cette classe Singleton dans votre application :

```
class Program
{
    static void Main(string[] args)
    {
        // Retrieve the single instance of the Singleton class
        Singleton singleton1 = Singleton.Instance;
        singleton1.PrintMessage(); // Output: Hello, I am a singleton class.

        // Retrieve the instance again
        Singleton singleton2 = Singleton.Instance;

        // Check if both instances are the same
        Console.WriteLine(singleton1 == singleton2); // Output: True
    }
}
```

Dans cet exemple, nous récupérons l'instance Singleton deux fois. Comme la classe est un Singleton, `singleton1` et `singleton2` se réfèrent tous deux à la même instance. L'opérateur `==` le confirme en retournant `true`.

### Comment étendre l'exemple Singleton

Vous pouvez étendre le patron Singleton pour gérer des scénarios plus complexes. Par exemple, vous pourriez initialiser l'instance Singleton avec des données de configuration :

```
public class ConfigurationManager
{
    private static ConfigurationManager instance;
    private readonly Dictionary<string, string> settings = new Dictionary<string, string>();

    private ConfigurationManager()
    {
        // Simulate loading settings from a configuration file
        settings["AppName"] = "MyApplication";
        settings["Version"] = "1.0.0";
    }

    public static ConfigurationManager Instance
    {
        get
        {
            if (instance == null)
            {
                instance = new ConfigurationManager();
            }
            return instance;
        }
    }

    public string GetSetting(string key)
    {
        return settings.ContainsKey(key) ? settings[key] : null;
    }
}
```

Ici, `ConfigurationManager` est une classe Singleton qui charge et gère les paramètres de l'application. La méthode `GetSetting` vous permet de récupérer des valeurs de configuration spécifiques, garantissant que toutes les parties de votre application utilisent les mêmes paramètres.

### Points clés à retenir sur les classes Singleton

-   **Instance unique** : Les classes Singleton garantissent qu'une seule instance de la classe existe dans l'application.
    
-   **Accès global** : Le Singleton fournit un point d'accès global à l'instance, ce qui la rend facile à utiliser dans différentes parties de votre application.
    
-   **Sécurité des threads (Thread safety)** : Dans des environnements multi-thread, assurez-vous que votre Singleton est thread-safe pour éviter de créer plusieurs instances.
    
-   **Cas d'utilisation** : Les cas d'utilisation courants pour le Singleton incluent la gestion des configurations, les services de journalisation et les connexions aux bases de données.
    

Les classes Singleton sont un patron de conception fondamental en génie logiciel, offrant un moyen simple mais puissant de gérer des ressources partagées. Comprendre et implémenter correctement les Singletons peut vous aider à écrire un code plus efficace et plus facile à maintenir.

## Classes génériques en C#

Les classes génériques en C# offrent un moyen puissant de créer un code réutilisable et sûr au niveau du type (type-safe). En utilisant des classes génériques, vous pouvez concevoir une classe unique qui fonctionne avec n'importe quel type de données, éliminant ainsi le besoin d'implémentations spécifiques à chaque type. Cela rend votre code plus flexible et réduit la redondance.

### Pourquoi utiliser des classes génériques ?

Imaginez que vous deviez implémenter une pile (stack) qui stocke des entiers. Plus tard, vous pourriez avoir besoin d'une autre pile pour stocker des chaînes de caractères.

Au lieu d'écrire deux classes distinctes, vous pouvez écrire une seule classe de pile générique capable de gérer les deux types de données — et n'importe quel autre dont vous pourriez avoir besoin. Les classes génériques vous aident à éviter la duplication de code et rendent votre base de code plus facile à maintenir.

### Exemple : Définir une classe générique

Jetons un coup d'œil à une implémentation simple d'une classe de pile générique :

```
// Define a generic class
public class Stack<T>
{
    private List<T> items = new List<T>();

    public void Push(T item)
    {
        items.Add(item);
    }

    public T Pop()
    {
        if (items.Count == 0)
        {
            throw new InvalidOperationException("The stack is empty.");
        }
        T item = items[items.Count - 1];
        items.RemoveAt(items.Count - 1);
        return item;
    }

    public T Peek()
    {
        if (items.Count == 0)
        {
            throw new InvalidOperationException("The stack is empty.");
        }
        return items[items.Count - 1];
    }

    public bool IsEmpty()
    {
        return items.Count == 0;
    }
}
```

Dans cet exemple, la classe `Stack<T>` est définie avec un paramètre de type `T`. Ce paramètre de type est un espace réservé (placeholder) qui représente le type de données que la pile va stocker. La classe inclut des méthodes comme `Push` pour ajouter un élément à la pile, `Pop` pour retirer et retourner l'élément supérieur, `Peek` pour voir l'élément supérieur sans le retirer, et `IsEmpty` pour vérifier si la pile est vide.

Parce que `Stack<T>` est générique, vous pouvez l'utiliser avec n'importe quel type de données, qu'il s'agisse d'un `int`, d'une `string`, ou même d'une classe personnalisée.

### Comment utiliser la classe Stack dans `Program.cs`

Voyons comment cette classe générique `Stack` peut être utilisée dans un programme :

```
class Program
{
    static void Main(string[] args)
    {
        // Stack for integers
        Stack<int> intStack = new Stack<int>();
        intStack.Push(10);
        intStack.Push(20);
        Console.WriteLine(intStack.Pop()); // Output: 20
        Console.WriteLine(intStack.Peek()); // Output: 10

        // Stack for strings
        Stack<string> stringStack = new Stack<string>();
        stringStack.Push("Hello");
        stringStack.Push("World");
        Console.WriteLine(stringStack.Pop()); // Output: World
        Console.WriteLine(stringStack.Peek()); // Output: Hello
    }
}
```

Dans cet exemple, nous créons deux instances de la classe `Stack` : une qui stocke des entiers et une autre qui stocke des chaînes de caractères. La flexibilité des génériques nous permet d'utiliser la même classe pour travailler avec différents types de données, rendant notre code plus réutilisable et concis.

### Comment étendre la classe générique

Allons un peu plus loin et étendons notre classe `Stack` pour inclure une méthode qui retourne tous les éléments sous forme de tableau :

```
public T[] ToArray()
{
    return items.ToArray();
}
```

Maintenant, vous pouvez facilement convertir les éléments de la pile en un tableau :

```
int[] intArray = intStack.ToArray();
string[] stringArray = stringStack.ToArray();
```

Cette extension démontre davantage la puissance des génériques, permettant à la même méthode de fonctionner de manière transparente avec différents types de données.

### Points clés à retenir sur les classes génériques

-   **Flexibilité** : Les classes génériques peuvent gérer n'importe quel type de données, ce qui les rend adaptables et réutilisables.
    
-   **Sécurité de typage** : L'utilisation de paramètres de type garantit que votre code est sûr au niveau du type, capturant les erreurs lors de la compilation plutôt qu'à l'exécution.
    
-   **Réutilisation du code** : Les génériques suppriment le besoin de dupliquer le code pour différents types de données, ce qui donne un code plus propre et plus facile à maintenir.
    
-   **Paramètres de type** : Les classes génériques utilisent des paramètres de type comme espaces réservés pour les types de données réels que vous utiliserez lors de la création d'une instance de la classe.
    

Les classes génériques sont cruciales en C# pour construire un code flexible, réutilisable et sûr au niveau du type. En apprenant et en utilisant les génériques, vous pouvez créer des applications plus fiables et maintenables.

## Classes internes en C#

Les classes internes (internal classes) en C# sont un moyen puissant d'encapsuler les détails d'implémentation au sein d'un assembly. En utilisant le modificateur d'accès `internal`, vous pouvez restreindre l'accès à certaines classes, garantissant qu'elles ne sont accessibles qu'au sein du même assembly.

C'est particulièrement utile pour cacher une logique complexe ou des classes utilitaires qui ne sont pas destinées à être exposées à l'API publique de votre bibliothèque ou application.

### Pourquoi utiliser des classes internes ?

Dans une grande application, vous pouvez avoir des classes qui ne devraient être utilisées qu'en interne par votre code et non par des consommateurs externes. Par exemple, des classes d'aide, des fonctions utilitaires ou des composants d'un système plus vaste qui n'ont pas besoin d'être exposés en dehors de l'assembly peuvent être marqués comme `internal`. Cela garantit que votre API publique reste propre et ciblée tout en permettant une fonctionnalité complète au sein de l'assembly.

### Exemple : Définir une classe interne

Considérons un scénario où vous avez une bibliothèque qui traite des commandes. Vous pourriez avoir une classe qui gère la logique complexe du calcul des remises, mais vous ne voulez pas que cette classe soit accessible aux utilisateurs de votre bibliothèque. Au lieu de cela, vous n'exposez que la classe principale `OrderProcessor`, en gardant la logique de remise cachée avec une classe interne.

```
// Define a public class that uses an internal class
public class OrderProcessor
{
    public void ProcessOrder(int orderId)
    {
        // Internal class is used here
        DiscountCalculator calculator = new DiscountCalculator();
        decimal discount = calculator.CalculateDiscount(orderId);
        Console.WriteLine($"Order {orderId} processed with a discount of {discount:C}");
    }

    // Internal class that handles discount calculations
    internal class DiscountCalculator
    {
        public decimal CalculateDiscount(int orderId)
        {
            // Complex discount calculation logic
            return orderId * 0.05m;
        }
    }
}
```

Dans cet exemple, la classe `DiscountCalculator` est marquée comme `internal`, ce qui signifie qu'elle n'est accessible qu'au sein de l'assembly. La classe `OrderProcessor`, qui est `public`, utilise cette classe interne pour traiter les commandes. Les utilisateurs externes de la bibliothèque peuvent appeler `ProcessOrder` sans avoir besoin de connaître ou d'interagir avec la classe `DiscountCalculator`.

### Comment utiliser la classe interne dans `Program.cs`

Voyons maintenant comment cela fonctionne en pratique :

```
class Program
{
    static void Main(string[] args)
    {
        OrderProcessor processor = new OrderProcessor();
        processor.ProcessOrder(12345); // Output: Order 12345 processed with a discount of $617.25
    }
}
```

Dans cet exemple, la méthode `ProcessOrder` est accessible publiquement, mais les rouages internes du calcul de remise restent cachés, offrant une API propre et sécurisée.

### Points clés à retenir sur les classes internes

-   **Accès limité** : Les classes internes ne peuvent être accédées qu'au sein du même assembly, ce qui aide à garder votre API publique simple et ciblée.
    
-   **Encapsulation** : Elles sont utilisées pour cacher les détails d'implémentation, comme les fonctions d'aide ou la logique complexe, qui ne devraient pas être visibles publiquement.
    
-   **Contrôle de la visibilité** : Le modificateur d'accès `internal` vous permet de contrôler quelles classes et quels membres sont visibles, garantissant que seules les parties nécessaires de votre code sont accessibles aux autres assemblies.
    

Les classes internes sont importantes pour gérer des applications complexes, vous permettant de contrôler quelles parties de votre code peuvent être accédées depuis l'extérieur de votre assembly. En cachant les détails et en limitant l'accès, vous pouvez garder votre base de code propre, facile à maintenir et sécurisée.

## Classes imbriquées en C#

Les classes imbriquées (nested classes) en C# sont définies à l'intérieur d'une autre classe. Cette structure est utile pour regrouper des classes liées et encapsuler les détails d'implémentation. Les classes imbriquées peuvent être soit statiques, soit non statiques, et elles ont un accès direct aux membres privés de leur classe englobante.

### Pourquoi utiliser des classes imbriquées ?

Les classes imbriquées sont particulièrement utiles lorsqu'une classe est étroitement liée à la logique d'une autre classe et n'est pas destinée à être utilisée indépendamment. Elles vous permettent d'encapsuler des classes d'aide, de les cacher des autres parties du programme et de garder le code lié ensemble. Cela peut mener à une base de code plus propre et mieux organisée.

### Exemple : Définir une classe imbriquée

Considérons un scénario où nous avons une classe qui représente une voiture (`Car`) et une autre classe qui représente un moteur (`Engine`). Comme la classe `Engine` est étroitement liée à la classe `Car` et n'a pas beaucoup de sens seule, nous pouvons la définir comme une classe imbriquée au sein de `Car`.

```
// Define a class with a nested class
public class Car
{
    // Define private fields
    private string model;
    private Engine carEngine;

   // Constructor
    public Car(string model)
    {
        this.model = model;
        carEngine = new Engine();
    }


    // Method to start the car
    public void StartCar()
    {
        carEngine.StartEngine();
        Console.WriteLine($"{model} is starting...");
    }

    // Nested class
    public class Engine
    {
        public void StartEngine()
        {
            Console.WriteLine("Engine started.");
        }
    }
}
```

Dans cet exemple, la classe `Car` possède un champ privé `model` et une méthode `StartCar` qui démarre la voiture. La classe `Engine` est imbriquée dans la classe `Car` et contient une méthode `StartEngine`. En imbriquant `Engine` dans `Car`, nous exprimons la relation étroite entre les deux.

### Comment utiliser la classe imbriquée dans `Program.cs`

Voyons comment nous pouvons utiliser la classe `Car` et sa classe imbriquée `Engine` dans un programme :

```
class Program
{
    static void Main(string[] args)
    {
        Car myCar = new Car("Toyota");
        myCar.StartCar(); // Output: Engine started. Toyota is starting...

        // Although you can create an instance of the nested class separately, it usually makes sense to use it through the outer class
        Car.Engine engine = new Car.Engine();
        engine.StartEngine(); // Output: Engine started.
    }
}
```

Dans cet exemple, nous créons une instance de la classe `Car` et appelons la méthode `StartCar`, qui appelle en interne la méthode `StartEngine` de la classe imbriquée `Engine`. Bien qu'il soit possible d'instancier la classe imbriquée séparément, il est plus courant d'y accéder via la classe externe, soulignant la relation entre les deux.

### Points clés à retenir sur les classes imbriquées

-   **Encapsulation** : Les classes imbriquées cachent les détails qui ne devraient pas être vus en dehors de la classe principale.
    
-   **Accès aux membres privés** : Les classes imbriquées peuvent accéder aux parties privées de la classe principale, ce qui les rend idéales pour les classes d'aide qui doivent travailler avec les composants internes de la classe principale.
    
-   **Organisation** : Utilisez des classes imbriquées pour garder les classes liées ensemble, ce qui rend le code plus propre et mieux organisé.
    
-   **Statique ou non statique** : Les classes imbriquées peuvent être statiques ou non statiques. Les classes imbriquées statiques ne peuvent pas accéder directement aux membres d'instance de la classe principale, contrairement aux classes imbriquées non statiques.
    

Les classes imbriquées sont un moyen utile d'organiser votre code, en particulier pour les objets complexes ayant des parties étroitement liées. Garder les classes liées ensemble facilite la gestion et la maintenance de votre code.

## Classes partielles en C#

Les classes partielles (partial classes) en C# vous permettent de diviser la définition d'une classe sur plusieurs fichiers. Cette fonctionnalité est particulièrement utile dans les grands projets, où il peut être bénéfique de diviser une classe complexe en sections plus petites et plus gérables.

En utilisant le mot-clé `partial`, vous pouvez mieux organiser votre code, surtout lorsque vous travaillez avec du code généré ou que vous collaborez au sein d'une équipe.

### Pourquoi utiliser des classes partielles ?

Imaginez que vous travailliez sur une grande application où une seule classe contient des centaines de lignes de code. Cela peut devenir difficile à gérer et à maintenir. En utilisant des classes partielles, vous pouvez diviser la classe en parties logiques, chacune résidant dans un fichier séparé. Cela rend non seulement le code plus lisible, mais permet également à plusieurs développeurs de travailler simultanément sur différentes parties de la classe sans provoquer de conflits de fusion (merge conflicts).

### Exemple : Définir une classe partielle en C#

Supposons que nous ayons une classe qui gère diverses opérations pour un système de gestion d'employés. Au lieu de mettre toutes les méthodes dans un seul fichier, nous pouvons les diviser sur plusieurs fichiers en utilisant des classes partielles.

**Fichier 1 :** `PartialClass_Methods1.cs`

```
// Define a partial class
public partial class EmployeeOperations
{
    public void AddEmployee(string name)
    {
        Console.WriteLine($"Employee {name} added.");
    }
}
```

**Fichier 2 :** `PartialClass_Methods2.cs`

```
// Define the other part of the partial class
public partial class EmployeeOperations
{
    public void RemoveEmployee(string name)
    {
        Console.WriteLine($"Employee {name} removed.");
    }
}
```

Dans ces exemples, la classe `EmployeeOperations` est divisée en deux fichiers, chacun contenant une partie de la classe. Le premier fichier gère l'ajout d'employés, tandis que le second gère leur suppression.

### Comment utiliser la classe partielle dans `Program.cs`

Maintenant, utilisons la classe `EmployeeOperations` dans notre fichier `Program.cs` :

```
class Program
{
    static void Main(string[] args)
    {
        EmployeeOperations operations = new EmployeeOperations();

        operations.AddEmployee("John Doe");    // Output: Employee John Doe added.
        operations.RemoveEmployee("John Doe"); // Output: Employee John Doe removed.
    }
}
```

Dans cet exemple, la classe `EmployeeOperations`, bien que définie dans plusieurs fichiers, se comporte comme une classe unique. Les méthodes `AddEmployee` et `RemoveEmployee` sont combinées de manière transparente, offrant un moyen propre et organisé de gérer les opérations.

### Points clés à retenir sur les classes partielles

-   **Organisation du code** : Les classes partielles aident à garder les grandes classes organisées en les divisant en sections plus petites et ciblées.
    
-   **Collaboration en équipe** : Plusieurs développeurs peuvent travailler sur différentes parties de la même classe sans interférer avec le code des autres.
    
-   **Code généré** : Souvent utilisées avec du code auto-généré, où une partie de la classe est générée par un outil et le reste est écrit manuellement.
    

Les classes partielles sont une fonctionnalité puissante en C# qui permet une meilleure gestion du code, en particulier dans les applications à grande échelle. En décomposant une classe en composants logiques, vous pouvez maintenir un code propre, lisible et facile à entretenir.

## Conclusion

Les classes sont les briques de base de la programmation orientée objet en C#. En comprenant les différents types de classes — abstraites, statiques, scellées, concrètes et singleton — vous pouvez créer un code bien structuré, maintenable et efficace.

Que vous conceviez des classes utilitaires, définissiez des interfaces abstraites ou encapsuliez une logique complexe, les classes jouent un rôle crucial dans le façonnement de l'architecture de votre application.

[1]: https://www.youtube.com/@CliffTech
[2]: #heading-classes-statiques-en-c-sharp
[3]: #heading-classes-scellees-en-c-sharp
[4]: #heading-classes-concretes-en-c-sharp
[5]: #heading-classes-abstraites-en-c-sharp
[6]: #heading-classes-singleton-en-c-sharp
[7]: #heading-classes-generiques-en-c-sharp
[8]: #heading-classes-internes-en-c-sharp
[9]: #heading-classes-imbriquees-en-c-sharp
[10]: #heading-classes-partielles-en-c-sharp
[11]: #heading-conclusion