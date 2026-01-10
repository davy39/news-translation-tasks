---
title: Comment fonctionne l'héritage en C# – avec des exemples de code
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-11-29T20:04:11.000Z'
originalURL: https://freecodecamp.org/news/inheritance-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/caspar-camille-rubin-fPkvU7RDmCo-unsplash.jpg
tags:
- name: C
  slug: c
- name: inheritance
  slug: inheritance
- name: object oriented
  slug: object-oriented
- name: Object Oriented Programming
  slug: object-oriented-programming
seo_title: Comment fonctionne l'héritage en C# – avec des exemples de code
seo_desc: "Inheritance is a branch of object-oriented programming that helps you write\
  \ reusable code. It allows you to extend the content of a class to another class.\
  \ \nOther pillars of object-oriented programming include encapsulation, polymorphism,\
  \ and abstrac..."
---

L'héritage est une branche de la programmation orientée objet qui vous aide à écrire du code réutilisable. Il vous permet d'étendre le contenu d'une classe à une autre classe. 

[Les autres piliers de la programmation orientée objet](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/) incluent l'encapsulation, le polymorphisme et l'abstraction. 

Dans cet article, nous allons apprendre l'héritage en C# et les différents types d'héritage que nous avons en POO.

## Qu'est-ce que l'héritage ?

L'héritage est l'une des caractéristiques clés de la programmation orientée objet (POO). Il s'agit simplement du processus par lequel une classe (la classe enfant ou dérivée) acquiert les propriétés, méthodes et champs d'une autre classe (la classe de base, parent ou super classe).

L'héritage en programmation orientée objet signifie que vous créez des classes qui peuvent transmettre leurs propriétés à d'autres classes sans avoir à définir explicitement les propriétés dans les nouvelles classes. 

L'héritage ne garantit pas seulement la réutilisabilité de la base de code, mais il réduit également la complexité de votre code.

## Types d'héritage en C#

L'héritage vous permet de construire des familles de classes apparentées. La classe de base/parent définit les données communes pour que la classe enfant les hérite. Vous utilisez l'opérateur deux-points (:) pour montrer l'héritage entre deux classes.

```cs
using System;

namespace LearningInheritance
{
    class ParentClass
    {
        //...
    }
    class ChildClass:ParentClass
    {
        //..
    }
}
 

```

Il existe différents types d'héritage en C#. Nous allons les discuter maintenant.

### Héritage simple en C#

L'héritage simple se produit généralement entre deux classes – la classe de base et la classe dérivée. Il se produit lorsqu'une classe hérite d'une seule classe parent. 

Voici un exemple de code qui montre l'héritage simple en C# :

```cs
using System;

namespace LearningInheritance
{
    class ParentClass
    {
        public string name;
        public int Id = 9;

        public void displayParentClassDetails()
        {
            Console.WriteLine($"Je suis {name}");
            Console.WriteLine($"ID : {Id}");
        }
    }

    class ChildClass : ParentClass
    {
        public void getIdFromParentClass()
        {
            Console.WriteLine($"Voici mon ID : {Id}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //accès aux membres hérités depuis la classe enfant
            ChildClass child = new ChildClass();
            child.getIdFromParentClass();
        }
    }
}


```

Dans le code ci-dessus, nous avons dérivé une sous-classe (ChildClass) d'une super classe (ParentClass). La ChildClass a maintenant accès aux champs et propriétés de la ParentClass grâce à l'héritage. Nous avons pu accéder facilement aux membres hérités depuis la ChildClass comme on le voit ci-dessus.

### Héritage hiérarchique en C#

L'héritage hiérarchique se produit lorsqu'il y a plus d'une classe dérivée créée à partir d'une seule classe parent.

```cs
namespace LearningInheritance
{
    class ParentClass
    {
        public string name;
        public int Id = 9;

        public void displayParentClassDetails()
        {
            Console.WriteLine($"Je suis {name}");
            Console.WriteLine($"ID : {Id}");
        }
    }

    class ChildClass : ParentClass
    {
        public void getIdFromParentClass()
        {
            Console.WriteLine("Affichage depuis ma classe enfant");
            Console.WriteLine($"Voici mon ID : {Id}.");
        }
    }

    class AnotherChildClass : ParentClass
    {
        public void getIdFromParentClass()
        {
            Console.WriteLine("Affichage depuis mon autre classe enfant");
            Console.WriteLine($"Voici mon ID : {Id}");
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //accès aux membres hérités dans la classe parent (depuis la classe enfant)
            ChildClass child = new ChildClass();
            child.getIdFromParentClass();

            //accès aux membres hérités dans la classe parent (depuis l'autre classe enfant)
            AnotherChildClass anotherChild = new AnotherChildClass();
            anotherChild.getIdFromParentClass();
        }
    }
}
```

Dans le code ci-dessus, nous avons montré que nous pouvons dériver plus d'une classe enfant à partir d'une seule classe parent. 

La ChildClass et AnotherChildClass héritent toutes deux des champs et méthodes de la classe de base, ParentClass. Cela s'appelle l'héritage hiérarchique. Les deux classes enfants peuvent donc accéder aux champs et méthodes de la classe parent.

### Héritage multi-niveaux en C#

L'héritage multi-niveaux se produit lorsqu'une classe est dérivée d'une autre classe dérivée. Il s'agit simplement d'une situation où une classe dérivée est créée et utilisée comme classe de base pour une autre classe.

```cs
namespace LearningInheritance
{
    class ParentClass
    {
        public string name;
        public int Id = 9;

        //...
    }

    class ChildClass : ParentClass
    {
        //...
        //La classe Child est la classe dérivée dans ce cas
    }

    class ThirdClass : ChildClass
    {
        //...
        //La ChildClass est la classe de base pour la ThirdClass
    }

    class Program
    {
        static void Main(string[] args)
        {
            //...
        }
    }
}
```

Dans le code ci-dessus, nous avons également dérivé une sous-classe (ChildClass) d'une super classe (ParentClass). La ChildClass agit ensuite comme une classe de base pour une sous-classe enfant qui a été nommée ThirdClass.

### Héritage multiple – Interfaces en C#

L'héritage multiple n'est pas supporté en C#. Mais vous pouvez l'atteindre en utilisant des _interfaces_. 

L'héritage multiple permet à une classe dérivée d'hériter de plusieurs classes parent. Vous pouvez voir un exemple de la façon dont une classe enfant peut hériter de plusieurs interfaces qui agissent comme une classe parent ci-dessous :

```cs
namespace LearningInheritance
{    
    class Program
    {
        interface InterfaceA
        {
            //...
        }

        interface InterfaceB
        {
            //...
        }     
        
        class NewClass: InterfaceA, InterfaceB
        {
            //...            
        }
        
        static void Main(string[] args)
        {
            //...
        }
    }
}
```

## Conclusion

L'héritage est important car il aide à garder votre code propre. Il facilite la construction de familles de classes apparentées. La classe enfant peut hériter de tous les champs, propriétés et méthodes contenus dans la classe parent, sauf celles qui sont déclarées comme une classe privée. 

À travers cet article, j'espère que vous avez acquis quelques connaissances sur l'héritage en C#.

Bon codage.