---
title: Filtrage en C# – Comment filtrer une liste avec des exemples de code
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2022-12-21T21:45:12.000Z'
originalURL: https://freecodecamp.org/news/filtering-in-csharp-how-to-filter-a-list-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/ferenc-almasi-tvHtIGbbjMo-unsplash.jpg
tags:
- name: C
  slug: c
seo_title: Filtrage en C# – Comment filtrer une liste avec des exemples de code
seo_desc: "Filtering through a data set is one of the most basic operations a developer\
  \ should know how to perform. \nFiltering refers to the process of restricting the\
  \ result set to contain only those elements that satisfy a specified condition.\
  \ It is also know..."
---

Le filtrage d'un ensemble de données est l'une des opérations les plus basiques qu'un développeur doit savoir effectuer. 

Le [filtrage](https://learn.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/filtering-data) fait référence au processus de restriction de l'ensemble de résultats pour qu'il ne contienne que les éléments qui satisfont une condition spécifiée. Il est également connu sous le nom de sélection. 

Pour être concret, imaginez essayer de chercher et de collecter des oranges dans un panier de fruits. C'est du **filtrage**. 

Dans cet article, nous verrons différentes façons de filtrer une classe List<T>. 

Avant de commencer à filtrer la collection List, nous allons créer une classe publique appelée **Employee** qui contient les détails des employés. 

La classe Employee est comme un plan qui contient les détails de chaque employé. Elle a des champs privés pour le _nom_, l'_id_ et le _département_ de chaque employé. 

La classe **Employee** a également des méthodes _getter_ et _setter_ pour pouvoir définir et obtenir la valeur de chaque champ privé. 

Voici le code qui démontre ce que je viens d'expliquer ci-dessus :

```cs
    public class Employee
    {
        private string _name;
        private int _id;
        private string _department;
        
        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        public int Id
        {
            get { return _id; }
            set { _id = value; }
        }

        public string Department
        {
            get { return _department; }
            set { _department = value; }
        }
    }

```

À l'intérieur de la classe Program, créons une méthode qui contiendra une liste utilisant la classe **Employee** déjà créée ci-dessus. Chaque employé aura un ID, un nom et un département. 

```program.cs
 public static void ListOperations()
 {
 	List<Employee> employees = new List<Employee>()
    {
		new Employee(){ Id=1, Name="John Doe", Department="Software"},
        new Employee(){ Id=2, Name="Angela Su", Department="Sales"},
        new Employee(){ Id=3, Name="Frank Kelvin", Department="Marketing"},
        new Employee(){ Id=4, Name="Joe Dustin", Department="Sales"},
        new Employee(){ Id=5, Name="Glory GG", Department="Software"},
        new Employee(){ Id=6, Name="Antonella Cruz", Department="Marketing"},
        new Employee(){ Id=5, Name="Andrew Logan", Department="Software"},
        new Employee(){ Id=6, Name="Billy Cruz", Department="Marketing"},
        new Employee(){ Id=5, Name="Sally Jane", Department="Software"},
        new Employee(){ Id=4, Name="Jon Snow", Department="Sales"},
    };
}

```

Le code ci-dessus est la déclaration d'une liste d'employés dans la **méthode ListOperations**. Notre objectif est de filtrer la liste pour obtenir les employés qui travaillent dans le département logiciel. 

Il existe plusieurs façons de filtrer une liste en C#. Examinons-les maintenant :

## Comment filtrer une liste en utilisant la méthode itérative

Dans cette méthode, vous parcourez une liste et cherchez le membre de chaque itération qui passe la condition. Voici un exemple de code qui utilise la méthode itérative :

```program.cs
Console.WriteLine("Filtrage de la liste des employés en utilisant la " +
                    "méthode itérative");
//objectif : Filtrer la liste pour obtenir les employés du département logiciel de l'entreprise
           
foreach (var employee in employees)
{
	if(employee.Department == "Software")
    {
    	Console.WriteLine(employee.Name);
    }
}

```

## Comment filtrer une liste en utilisant la syntaxe de requête LINQ (clause Where)

Language-Integrated Query (LINQ) est un moyen puissant de récupérer des données à partir de sources de données en C#. Cette méthode filtre la collection de listes et retourne une nouvelle collection basée sur un critère donné. 

```program.cs
Console.WriteLine("\nClause Where - Syntaxe de requête LINQ ");
var filteredResults = from employee in employees
						where employee.Department == "Software"
                        select employee.Name;
            
//Parcourir vos résultats filtrés
foreach(var result in filteredResults)
{
	Console.WriteLine(result);
}

```

Dans le code ci-dessus, la **syntaxe de requête LINQ** utilise l'opérateur **where** pour filtrer les employés qui travaillent dans le département **Software** à partir de la liste **employees**. Nous parcourons ensuite les résultats filtrés pour imprimer nos résultats sur la console. 

## Comment filtrer une liste en utilisant la syntaxe de méthode LINQ (clause Where)

Contrairement à la syntaxe de requête ci-dessus, la **méthode d'extension LINQ** utilise l'expression lambda. L'expression lambda est passée en tant que prédicat. C'est en effet un raccourci vers la syntaxe de requête LINQ ci-dessus. 

Voici un exemple de code qui utilise la **syntaxe de méthode LINQ**. 

```program.cs
Console.WriteLine("\nClause Where - Syntaxe de méthode LINQ ");

var filteredResultsTwo = employees.Where(employee => employee.Department == "Software");

//Parcourir vos résultats filtrés
foreach(var employee in filteredResultsTwo)
{
	Console.WriteLine(employee.Name);
}
```

Dans le code ci-dessus, la **syntaxe de méthode LINQ** est utilisée pour filtrer la liste **employees** et retourner une nouvelle liste d'employés qui travaillent dans le département **Software**. Elle utilise une expression lambda comme fonction prédicat. Nous parcourons ensuite les résultats filtrés pour imprimer nos résultats sur la console.         

Le code complet pour diverses méthodes de filtrage d'une liste est fourni ci-dessous :

```program.cs
namespace Linq
{
    public class Employee
    {
        private string _name;
        private int _id;
        private string _department;
         
        public string Name
        {
            get { return _name; }
            set { _name = value; }
        }

        public int Id
        {
            get { return _id; }
            set { _id = value; }
        }

        public string Department
        {
            get { return _department; }
            set { _department = value; }
        }
    }


    internal class Program
    {
        //OBJECTIF : Notre objectif est de filtrer la liste pour obtenir les employés
        //qui travaillent dans le département logiciel.

        public static void ListOperations()
        {
           List<Employee> employees = new List<Employee>()
           {
            new Employee(){ Id=1, Name="John Doe", Department="Software"},
            new Employee(){ Id=2, Name="Angela Su", Department="Sales"},
            new Employee(){ Id=3, Name="Frank Kelvin", Department="Marketing"},
           new Employee(){ Id=4, Name="Joe Dustin", Department="Sales"},
           new Employee(){ Id=5, Name="Glory GG", Department="Software"},
           new Employee(){ Id=6, Name="Antonella Cruz", Department="Marketing"},
           new Employee(){ Id=5, Name="Andrew Logan", Department="Software"},
           new Employee(){ Id=6, Name="Billy Cruz", Department="Marketing"},
           new Employee(){ Id=5, Name="Sally Jane", Department="Software"},
           new Employee(){ Id=4, Name="Jon Snow", Department="Sales"},
           };
            

         //1: Méthode itérative
       Console.WriteLine("Filtrage de la liste des employés en utilisant la " +
                    "méthode itérative");            
            foreach (var employee in employees)
            {
                if(employee.Department == "Software")
                {
                    Console.WriteLine(employee.Name);
                }
            }


       //2: Syntaxe de requête LINQ (en utilisant la clause Where)            
          Console.WriteLine("\nClause Where - Syntaxe de requête LINQ ");
            var filteredResults = from employee in employees
                                  where employee.Department == "Software"
                                  select employee.Name;
                    
            foreach(var result in filteredResults)
            {
                Console.WriteLine(result);
            }


       //3: Syntaxe de méthode LINQ (en utilisant la clause Where)            
         Console.WriteLine("\nClause Where - Syntaxe de méthode LINQ ");
         var filteredResultsTwo = employees.Where(employee => employee.Department == "Software");
            foreach(var employee in filteredResultsTwo)
            {
                Console.WriteLine(employee.Name);
            }

        }

        static void Main(string[] args)
        {
            ListOperations();           
        }

    }
}


```

## Conclusion

Le filtrage vous permet de sélectionner uniquement les éléments qui répondent à une condition particulière. Dans cet article, nous avons montré comment filtrer une liste en C# en utilisant diverses méthodes. 

J'espère que cet article vous a donné suffisamment d'informations pour filtrer facilement les collections List<T>. 

**Bon codage !**