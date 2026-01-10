---
title: Comment utiliser la programmation orientée objet en C# – Expliqué avec des
  exemples
subtitle: ''
author: Isaiah Clifford Opoku
co_authors: []
series: null
date: '2024-05-01T12:14:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-oop-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Attractive-1.png
tags:
- name: C
  slug: c
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Comment utiliser la programmation orientée objet en C# – Expliqué avec
  des exemples
seo_desc: 'Welcome to this comprehensive guide on object-oriented programming (OOP)
  using C#. This article will delve into the four fundamental pillars of OOP:


  Inheritance

  Encapsulation

  Polymorphism

  Abstraction


  Whether you''re a seasoned programmer or a beginn...'
---

Bienvenue dans ce guide complet sur la programmation orientée objet (POO) en utilisant C#. Cet article explorera les quatre piliers fondamentaux de la POO :

- Héritage
- Encapsulation
- Polymorphisme
- Abstraction

Que vous soyez un programmeur expérimenté ou un débutant entrant dans le monde de C#, cet article vise à améliorer votre compréhension des concepts de la POO et de leur mise en œuvre en C#.

Si vous êtes nouveau dans C#, envisagez de suivre le cours de certification gratuit sur [freeCodeCamp](https://www.freecodecamp.org/learn/foundational-c-sharp-with-microsoft/) ou le cours gratuit sur [Microsoft Learn](https://learn.microsoft.com/en-us/courses/browse/?term=c%23&resource_type=learning%20path) pour vous familiariser avec le langage.

N'oubliez pas que les principes de la POO sont universels et s'appliquent à la plupart des langages de programmation orientés objet. Par conséquent, les connaissances que vous acquerrez grâce à cet article peuvent être appliquées à l'apprentissage de la POO dans n'importe quel langage.

Commençons !
# Table des matières
2. [Qu'est-ce que la programmation orientée objet (POO)](#heading-quest-ce-que-la-programmation-orientee-objet-poo)

3. [Pourquoi utiliser la programmation orientée objet ?](#pourquoi-utiliser-la-programmation-orientee-objet)

4. [Les quatre piliers de la programmation orientée objet](#heading-les-quatre-piliers-de-la-programmation-orientee-objet)

5. [Héritage](#heading-heritage)

6. [Types d'héritage](#types-dheritage)

7. [Encapsulation](#heading-encapsulation)

8. [Polymorphisme](#heading-polymorphisme)

9. [Abstraction](#heading-abstraction)

10. [Résumé](#heading-resume)

<h1 id="quest-ce-que-la-programmation-orientee-objet-poo">Qu'est-ce que la programmation orientée objet (POO)</h1>

La programmation orientée objet (POO) est un paradigme de programmation qui utilise des `objets` et des `classes` pour concevoir et développer des applications logicielles. Elle est basée sur le concept d'objets, qui peuvent contenir des données sous forme de champs (attributs ou propriétés) et du code sous forme de procédures (méthodes ou fonctions).

La programmation orientée objet offre plusieurs avantages, notamment :

- **Modularité** : La POO favorise la modularité en décomposant les systèmes complexes en parties plus petites et gérables (objets). Cela facilite la maintenance et la mise à jour du code.

- **Réutilisabilité** : La POO vous permet de réutiliser le code existant en créant de nouveaux objets basés sur des objets existants. Cela permet de gagner du temps et des efforts dans le développement de nouvelles applications.

- **Flexibilité** : La POO offre de la flexibilité dans la conception et la mise en œuvre de systèmes logiciels. Vous pouvez facilement modifier et étendre la fonctionnalité des objets sans affecter d'autres parties du système.

- **Évolutivité** : La POO soutient l'évolutivité en permettant d'ajouter de nouveaux objets et classes à mesure que le système grandit. Cela facilite l'accommodation des changements et des améliorations dans le logiciel.

Comme vous pouvez le voir, la POO offre plusieurs avantages qui en font un choix populaire pour le développement d'applications logicielles. Explorons les quatre piliers fondamentaux de la POO plus en détail.

<h1 id="les-quatre-piliers-de-la-programmation-orientee-objet">Les quatre piliers de la programmation orientée objet</h1>

![Add-a-heading](https://www.freecodecamp.org/news/content/images/2024/04/Add-a-heading.png)

Les quatre piliers de la programmation orientée objet sont :

1. **Héritage**
2. **Encapsulation**
3. **Polymorphisme**
4. **Abstraction**

Ces piliers forment la base de la POO et sont des concepts essentiels à comprendre lorsque l'on travaille avec des langages de programmation orientés objet comme C#.

Approfondissons chacun des piliers de la POO dans les sections suivantes.

Commençons par le premier pilier de la POO : `Héritage`.

<h1 id="heritage">Héritage</h1>

L'héritage est un concept utilisé dans la plupart des langages de programmation et est quelque chose que vous ne pouvez pas éviter lorsque vous travaillez avec la programmation orientée objet. Des langages de programmation comme `C#` et Java sont quelques-uns des langages qui supportent l'héritage. Dans cet article, nous allons examiner l'héritage en `C#` et comment l'utiliser dans votre application.

#### Qu'est-ce que l'héritage ?

Imaginez que vous avez un arbre généalogique, où chaque génération représente une classe en C#. La première génération est la `classe de base`, qui est la classe fondamentale qui fournit la structure et les propriétés de base. Cela pourrait être comparé au patriarche de la famille, qui établit les valeurs et caractéristiques fondamentales de la famille.

À mesure que l'arbre généalogique progresse, chaque génération suivante hérite des traits et caractéristiques de la génération précédente, mais les modifie également pour refléter son identité unique. Ces générations suivantes peuvent être considérées comme des classes `dérivées` en C#, qui héritent de la classe `de base` mais introduisent également leurs propres caractéristiques ou modifications uniques.

Par exemple, le patriarche pourrait avoir établi l'amour de la famille pour le jardinage, qui devient un trait fondamental transmis à travers les générations. Cependant, à mesure que l'arbre généalogique évolue, certains membres pourraient développer un intérêt particulier pour la culture de plantes exotiques, tandis que d'autres pourraient se concentrer sur le jardinage biologique. Ces intérêts particuliers représentent les caractéristiques uniques des classes dérivées, qui héritent de l'amour de base pour le jardinage de la classe de base mais introduisent également leurs propres caractéristiques uniques.

Dans cette analogie, la classe `de base` est le patriarche, qui représente la classe fondamentale avec ses propriétés et caractéristiques de base. Les classes `dérivées` sont les générations suivantes, chacune avec leurs caractéristiques ou modifications uniques, héritant des traits de base de la classe de base mais ajoutant également leurs propres aspects uniques. Ce processus d'héritage permet la création d'un arbre généalogique riche et varié, où chaque génération s'appuie sur la précédente, introduisant de nouveaux traits et affinant les traits existants.

L'héritage est un mécanisme qui vous permet de définir une nouvelle `classe` basée sur une classe existante. La nouvelle classe hérite de tous les membres (champs, propriétés et méthodes) de la classe existante. La classe existante est connue sous le nom de classe `de base`, et la nouvelle classe est connue sous le nom de classe `dérivée`.

Syntaxe de base de l'héritage en C# :

```csharp

class BaseClass
{
    // Membres de la classe de base
}

class DerivedClass : BaseClass
{
    // Membres de la classe dérivée
}

```

Dans l'extrait de code ci-dessus, `BaseClass` est la classe de base, et `DerivedClass` est la classe dérivée. La `DerivedClass` hérite de tous les membres de la `BaseClass`. Le deux-points `(:)` est utilisé pour indiquer que la `DerivedClass` est dérivée de la `BaseClass`.

Si vous êtes nouveau dans `C#` et que vous ne savez pas ce qu'est une classe, ne vous inquiétez pas, je vais vous l'expliquer. Une classe est un plan pour créer des objets. Elle définit les propriétés et méthodes qu'un objet de la classe aura. Voici un exemple de classe en `C#` :

```csharp

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public void Display()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}");
    }
}

```

Dans l'extrait de code ci-dessus, la classe `Person` a deux propriétés (`Name` et `Age`) et une méthode (`Display`). Les propriétés représentent l'état de l'objet, et la méthode représente le comportement de l'objet. Vous pouvez créer un objet de la classe `Person` et définir ses propriétés comme ceci :

```csharp

Person person = new Person();
person.Name = "John";
person.Age = 30;

```

Vous pouvez appeler la méthode `Display` sur l'objet `person` pour afficher le nom et l'âge de la personne :

```csharp

person.Display(); // Output: Name: John, Age: 30

```

Avant de continuer avec l'article, examinons quelques mots-clés que vous allez rencontrer souvent : `base class`, `Abstract class`, `derived class`, `parent class`, et `child class`.

Permettez-moi de vous les expliquer.

- **Base class** : Il s'agit de la classe dont les membres sont hérités par une autre classe. Elle est également connue sous le nom de classe parente.

```csharp

public class BaseClass
{
    public void Display()
    {
        Console.WriteLine("This is a base class");
    }
}

```

- **Abstract class** : Il s'agit d'une classe qui ne peut pas être instanciée. Elle est utilisée pour fournir une base commune à toutes les classes dérivées. Elle peut contenir à la fois des méthodes abstraites et non abstraites.

```csharp

public abstract class AbstractClass
{
    public abstract void Display();
}

```

- **Derived class** : Il s'agit de la classe qui hérite des membres de la classe de base. Elle est également connue sous le nom de classe enfant.

```csharp

public class DerivedClass : BaseClass

{
    public void Show()
    {
        Console.WriteLine("This is a derived class");
    }
}

```
Maintenant que vous savez ce que signifient ces mots-clés, passons à la section suivante.

#### Types d'héritage
L'héritage peut être classé en différents types en fonction de la manière dont les classes sont dérivées. Voici les types d'héritage :

- **Héritage simple** : L'héritage simple est un concept fondamental en programmation orientée objet où une classe, connue sous le nom de `classe dérivée`, est basée sur une autre classe, connue sous le nom de `classe de base`. Il s'agit de la forme la plus simple d'héritage.

Pour illustrer cela, considérons une analogie du monde réel. Imaginez que vous êtes l'enfant unique de votre père. Dans ce scénario, vous héritez des caractéristiques de votre père. Cela est similaire à l'héritage simple en programmation.

Regardons un exemple en `C#` :

```csharp
public class Father
{
    public void Display()
    {
        Console.WriteLine("This is the father class");
    }
}
```

Dans le code ci-dessus, `Father` est la classe de base avec une méthode `Display`.

Maintenant, créons une classe dérivée `Child` qui hérite de la classe `Father` :

```csharp
public class Child : Father
{
    public void Show()
    {
        Console.WriteLine("This is the child class");
    }
}
```

Dans cet extrait de code, la classe `Child` est dérivée de la classe `Father`. La classe `Child` hérite de la méthode `Display` de la classe `Father`.

Vous pouvez créer un objet de la classe `Child` et appeler la méthode `Display`. Cela démontre que la classe `Child` peut accéder à la méthode `Display` de la classe `Father`.

```csharp
Child child = new Child();
child.Display(); // Output: This is the father class
```

- **Héritage multilevel** : L'héritage multilevel est un concept en programmation orientée objet où une classe est dérivée d'une autre classe dérivée, créant une chaîne d'héritage.

Pour mieux comprendre cela, considérons une analogie avec un arbre généalogique. Supposons que vous êtes l'`enfant` de votre `père`, et que votre `père` est l'`enfant` de votre `grand-père`. Dans ce scénario, vous héritez des caractéristiques de votre père et de votre grand-père. Cela est similaire à l'héritage multilevel en programmation.

Explorons ce concept avec un exemple en `C#` :

```csharp
public class Grandfather
{
    public void Display()
    {
        Console.WriteLine("This is the grandfather class");
    }
}
```

Dans le code ci-dessus, `Grandfather` est la classe de base avec une méthode `Display`.

Ensuite, nous avons créé une classe dérivée `Father` qui hérite de la classe `Grandfather` :

```csharp
public class Father : Grandfather
{
    public void Show()
    {
        Console.WriteLine("This is the father class");
    }
}
```

Ici, la classe `Father` est dérivée de la classe `Grandfather` et hérite de la méthode `Display` de celle-ci.

Enfin, nous avons créé une autre classe dérivée `Child` qui hérite de la classe `Father` :

```csharp
public class Child : Father
{
    public void DisplayChild()
    {
        Console.WriteLine("This is the child class");
    }
}
```

Dans cet extrait de code, la classe `Child` est dérivée de la classe `Father`. La classe `Child` hérite des méthodes `Display` et `Show` de la classe `Father`.

Nous pouvons créer un objet de la classe `Child` et appeler les méthodes `Display` et `Show`. Cela démontre que la classe `Child` peut accéder aux méthodes `Display` et `Show` de la classe `Father`.

```csharp
Child child = new Child();
child.Display(); // Output: This is the grandfather class
child.Show(); // Output: This is the father class
child.DisplayChild(); // Output: This is the child class
```

- **Héritage hiérarchique** : L'héritage hiérarchique est un concept en programmation orientée objet où plusieurs classes sont dérivées d'une `seule classe de base`, formant une `structure en forme d'arbre`.

Pour illustrer cela, considérons une analogie du monde réel. Supposons que vous et vos `frères et sœurs` partagez le `même parent`. Dans ce scénario, vous héritez tous des caractéristiques du même parent. Cela est similaire à l'héritage hiérarchique en programmation.

Explorons ce concept avec un exemple en `C#` :

```csharp
public class Parent
{
    public void Display()
    {
        Console.WriteLine("This is the parent class");
    }
}
```

Dans le code ci-dessus, `Parent` est la classe de base avec une méthode `Display`.

Ensuite, nous avons créé deux classes dérivées `Child1` et `Child2` qui héritent de la classe `Parent` :

```csharp
public class Child1 : Parent
{
    public void Show1()
    {
        Console.WriteLine("This is the first child class");
    }
}

public class Child2 : Parent
{
    public void Show2()
    {
        Console.WriteLine("This is the second child class");
    }
}
```

Dans cet extrait de code, les classes `Child1` et `Child2` sont dérivées de la classe `Parent`. Les deux classes héritent de la méthode `Display` de la classe `Parent`.

Nous pouvons créer des objets des classes `Child1` et `Child2` et appeler les méthodes `Display`, `Show1` et `Show2`. Cela démontre que les classes `Child1` et `Child2` peuvent accéder à la méthode `Display` de la classe `Parent`.

```csharp
Child1 child1 = new Child1();
child1.Display(); // Output: This is the parent class
child1.Show1(); // Output: This is the first child class

Child2 child2 = new Child2();
child2.Display(); // Output: This is the parent class
child2.Show2(); // Output: This is the second child class
```

Félicitations, vous avez appris les bases de l'héritage en C#, passons à la section suivante `Encapsulation`.

#### Comprendre l'encapsulation et les propriétés en C#

Alors que nous continuons notre voyage à travers les piliers de la POO, nous arrivons maintenant à `Encapsulation`. Avant de plonger dans `Encapsulation`, il est crucial de comprendre un concept courant en C# appelé `propriétés`.

Les propriétés en C# sont des membres d'une classe qui fournissent un mécanisme flexible pour lire, écrire ou calculer la valeur d'un champ privé. Elles peuvent être utilisées comme si elles étaient des membres de données publics, mais ce sont en réalité des méthodes spéciales appelées accesseurs. Ces accesseurs sont utilisés pour obtenir et définir les valeurs des champs privés.

Si vous êtes nouveau dans ce concept, ne vous inquiétez pas. Décomposons-le avec un exemple :

```csharp
public class Person
{
    private string name;

    public string Name
    {
        get { return name; }
        set { name = value; }
    }
}
```

Dans l'extrait de code ci-dessus, la classe `Person` a un champ privé `name` et une propriété `Name`. La propriété `Name` a deux accesseurs : un accesseur `get` pour récupérer la valeur du champ `name`, et un accesseur `set` pour définir la valeur du champ `name`.

Comprendre les propriétés est essentiel pour saisir le concept d'`Encapsulation`, que nous explorerons dans la section suivante.

<h1 id="encapsulation">Encapsulation</h1>

Pour comprendre `Encapsulation`, utilisons une analogie. Considérons une `boîte à cadeaux` qui contient un `cadeau`. La `boîte à cadeaux` agit comme un conteneur qui encapsule le `cadeau`. Le `cadeau` est caché du monde extérieur et ne peut être accessible que par l'intermédiaire de la `boîte à cadeaux`. Cela est similaire à `Encapsulation` en programmation orientée objet.

`Encapsulation` est le principe de regrouper les données (champs) et les méthodes (fonctions) qui opèrent sur les données en une seule unité, connue sous le nom de `classe`. Il restreint l'accès direct à certains composants d'un objet et permet l'accès uniquement par l'intermédiaire des méthodes de la classe. En essence, `Encapsulation` dissimule l'état interne d'un objet et n'expose que les informations nécessaires au monde extérieur.

Regardons un exemple en C# :

```csharp
public class Person
{
    private string name;
    private int age;

    public string Name
    {
        get { return name; }
        set { name = value; }
    }

    public int Age
    {
        get { return age; }
        set { age = value; }
    }

    public void Display()
    {
        Console.WriteLine($"Name: {Name}, Age: {Age}");
    }
}
```

Dans l'extrait de code ci-dessus, la classe `Person` encapsule les données (champs `name` et `age`) et les méthodes (`Display`) en une seule unité. Les champs `name` et `age` sont privés, ce qui signifie qu'ils ne peuvent pas être accessibles directement depuis l'extérieur de la classe. Les propriétés `Name` et `Age` fournissent un accès contrôlé aux champs privés en utilisant les accesseurs `get` et `set`.

Ajoutons un autre exemple pour illustrer davantage ce concept :

```csharp
public class BankAccount
{
    private double balance;

    public double Balance
    {
        get { return balance; }
        private set { balance = value; }
    }

    public void Deposit(double amount)
    {
        if (amount > 0)
        {
            Balance += amount;
        }
    }

    public void Withdraw(double amount)
    {
        if (amount > 0 && Balance >= amount)
        {
            Balance -= amount;
        }
    }

    public void DisplayBalance()
    {
        Console.WriteLine($"Balance: {Balance}");
    }
}
```

Dans cet exemple, la classe `BankAccount` encapsule le champ `balance` et les méthodes qui opèrent sur celui-ci (`Deposit`, `Withdraw`, `DisplayBalance`). Le champ `balance` est privé et ne peut être accessible que par l'intermédiaire de la propriété `Balance` et des méthodes de la classe. Cela garantit que le solde ne peut pas être manipulé directement depuis l'extérieur de la classe, offrant une manière sécurisée de gérer un compte bancaire.

Félicitations ! Vous avez appris à connaître `Encapsulation` et comment il est mis en œuvre en C#. Passons à la section suivante, `Polymorphisme`.

#### Comprendre le polymorphisme en C#

Alors que nous approfondissons les quatre piliers de la POO, nous rencontrons maintenant `Polymorphisme`. Le terme `Polymorphisme` provient des mots grecs `poly` (plusieurs) et `morphos` (formes), signifiant "plusieurs formes". Dans le domaine de la programmation orientée objet, `Polymorphisme` désigne la capacité d'un objet à prendre plusieurs formes.

Pour comprendre `Polymorphisme`, considérons un `lecteur de musique`. Il peut lire divers types de fichiers musicaux, tels que `MP3`, `WAV` ou `AAC`. Chacun de ces types de fichiers est différent, mais notre lecteur de musique peut tous les gérer. Cela est similaire à `Polymorphisme` en programmation orientée objet.

<h1 id="polymorphisme">Polymorphisme</h1>

`Polymorphisme` est un concept central en programmation orientée objet qui permet aux objets de différentes classes d'être traités comme des objets d'une superclasse commune. Il fournit une interface unique pour représenter plusieurs formes sous-jacentes (classes) et permet aux objets d'être traités de manière générique.

En C#, il existe deux types de `Polymorphisme` :

1. **Polymorphisme à la compilation (Surcharge de méthode)**
2. **Polymorphisme à l'exécution (Redéfinition de méthode)**

### Polymorphisme à la compilation (Surcharge de méthode)

`Polymorphisme à la compilation`, également connu sous le nom de `Surcharge de méthode`, permet à une classe d'avoir plusieurs méthodes avec le même nom mais des paramètres différents. Le compilateur détermine quelle méthode invoquer en fonction du nombre et des types d'arguments.

Voici un exemple de `Surcharge de méthode` en C# :

```csharp
public class Printer
{
    public void Print(string message)
    {
        Console.WriteLine($"Printing string: {message}");
    }

    public void Print(int number)
    {
        Console.WriteLine($"Printing number: {number}");
    }

    public void Print(string message, int copies)
    {
        for (int i = 0; i < copies; i++)
        {
            Console.WriteLine($"Printing string: {message}");
        }
    }
}
```

Dans cet exemple, la classe `Printer` a trois méthodes `Print` avec le même nom mais des paramètres différents. Cela est un exemple de `Surcharge de méthode` en C#.

### Polymorphisme à l'exécution (Redéfinition de méthode)

`Polymorphisme à l'exécution`, également connu sous le nom de `Redéfinition de méthode`, permet à une sous-classe de fournir une implémentation spécifique d'une méthode qui est déjà fournie par sa superclasse.

Voici un exemple de `Redéfinition de méthode` en C# :

```csharp
public class MusicPlayer
{
    public virtual void Play()
    {
        Console.WriteLine("Playing music");
    }
}

public class Mp3Player : MusicPlayer
{
    public override void Play()
    {
        Console.WriteLine("Playing MP3 music");
    }
}

public class WavPlayer : MusicPlayer
{
    public override void Play()
    {
        Console.WriteLine("Playing WAV music");
    }
}
```

Dans cet exemple, la classe `MusicPlayer` a une méthode virtuelle `Play`. Les classes `Mp3Player` et `WavPlayer` redéfinissent la méthode `Play` avec des implémentations spécifiques pour jouer de la musique MP3 et WAV, respectivement. Cela est un exemple de `Redéfinition de méthode` en C#.

Voyons comment `Polymorphisme` peut être utilisé dans un programme :

```csharp
MusicPlayer player = new Mp3Player();
player.Play(); // Output: Playing MP3 music

player = new WavPlayer();
player.Play(); // Output: Playing WAV music
```

Dans cet extrait de code, nous avons créé un objet de la classe `Mp3Player` et l'avons assigné à une variable de type `MusicPlayer`. Nous avons ensuite appelé la méthode `Play` sur l'objet `player`, qui invoque la méthode `Play` redéfinie dans la classe `Mp3Player`. Nous avons ensuite créé un objet de la classe `WavPlayer` et l'avons assigné à la variable `player`. Lorsque nous appelons la méthode `Play` à nouveau, elle invoque la méthode `Play` redéfinie dans la classe `WavPlayer`.

Félicitations ! Vous avez appris à connaître `Polymorphisme` et comment il est mis en œuvre en C#. Passons au dernier pilier de la POO, `Abstraction`.

#### Comprendre l'abstraction en C#

Alors que nous plongeons dans le dernier pilier de la POO, nous rencontrons `Abstraction`. `Abstraction` est le processus de masquer les détails complexes de l'implémentation et d'exposer uniquement les caractéristiques essentielles d'un objet. Il met l'accent sur ce qu'un objet fait plutôt que sur la manière dont il le fait.

Pour comprendre `Abstraction`, considérons un `smartphone`. Lorsque vous utilisez un smartphone, vous n'avez pas besoin de comprendre les intrications de la manière dont les composants internes comme le `processeur` ou la `mémoire` fonctionnent. Vous avez seulement besoin de savoir comment interagir avec l'interface utilisateur pour passer des appels, envoyer des messages ou utiliser des applications. Cela est similaire à `Abstraction` en programmation orientée objet.

<h2 id="abstraction">Abstraction</h2>

`Abstraction` est un concept clé en programmation orientée objet qui vous permet de créer un plan pour une classe avec certaines méthodes abstraites qui doivent être implémentées par les classes dérivées. Il vous permet de définir la structure d'une classe sans fournir les détails de l'implémentation.

En C#, `Abstraction` peut être réalisée en utilisant des classes `abstraites` et des `interfaces`. Explorons les deux concepts :

### Classes abstraites

Une classe `abstraite` est une classe qui ne peut pas être instanciée et peut contenir à la fois des méthodes abstraites et non abstraites. Une méthode abstraite est une méthode sans corps qui doit être implémentée par les classes dérivées.

Voici un exemple de classe `abstraite` en C# :

```csharp
public abstract class Animal
{
    public abstract void Speak();
}

public class Dog : Animal
{
    public override void Speak()
    {
        Console.WriteLine("The dog barks");
    }
}

public class Cat : Animal
{
    public override void Speak()
    {
        Console.WriteLine("The cat meows");
    }
}
```

Dans cet exemple, la classe `Animal` est une classe abstraite avec une méthode abstraite `Speak`. Les classes `Dog` et `Cat` héritent de la classe `Animal` et fournissent des implémentations spécifiques pour la méthode `Speak`. Cela est un exemple d'`Abstraction` utilisant des classes abstraites en C#.

### Interfaces

Une `interface` est un type de référence en C# qui définit un contrat pour les classes à implémenter. Elle contient uniquement la déclaration des méthodes, propriétés, événements ou indexeurs, sans fournir l'implémentation.

Voici un exemple d'`interface` en C# :

```csharp
public interface IFlyable
{
    void Fly();
}

public class Bird : IFlyable
{
    public void Fly()
    {
        Console.WriteLine("The bird flies");
    }
}

public class Airplane : IFlyable
{
    public void Fly()
    {
        Console.WriteLine("The airplane flies");
    }
}
```

Dans cet exemple, l'interface `IFlyable` définit un contrat avec une méthode `Fly`. Les classes `Bird` et `Airplane` implémentent l'interface `IFlyable` et fournissent des implémentations spécifiques pour la méthode `Fly`. Cela est un exemple d'`Abstraction` utilisant des interfaces en C#.

Félicitations ! Vous avez maintenant appris à connaître `Abstraction` et comment il est mis en œuvre en C#. Le point clé à retenir est que `Abstraction` nous permet de masquer la complexité du système et d'exposer uniquement les détails nécessaires à l'utilisateur.

<h1 id="resume">Résumé</h1>

Dans cet article, nous avons exploré les quatre piliers fondamentaux de la programmation orientée objet (POO) en C# : `Héritage`, `Encapsulation`, `Polymorphisme` et `Abstraction`.

Ces piliers forment la base de la POO et sont des concepts essentiels à comprendre lorsque l'on travaille avec des langages de programmation orientés objet comme C#. Les connaissances acquises grâce à cet article vous aideront à améliorer votre compréhension des concepts de la POO et de leur mise en œuvre en C#.

Merci d'avoir lu cet article, j'espère que vous le trouverez utile. Si vous avez des questions ou des commentaires, n'hésitez pas à me contacter. Bon codage !