---
title: Meilleures pratiques de codage en C# - Conventions de codage avec exemples
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-01-13T16:31:30.000Z'
originalURL: https://freecodecamp.org/news/coding-best-practices-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/kevin-ku-w7ZyuGYNpRQ-unsplash.jpg
tags:
- name: best practices
  slug: best-practices
- name: C
  slug: c
seo_title: Meilleures pratiques de codage en C# - Conventions de codage avec exemples
seo_desc: "Coding conventions ensure that your code is consistent, readable, understandable,\
  \ and maintainable. \nWhen it comes to writing clean and quality code, there are\
  \ conventions developers should follow to make this possible. \nThere are a few\
  \ things you sh..."
---

Les conventions de codage garantissent que votre code est cohérent, lisible, compréhensible et maintenable. 

Lorsqu'il s'agit d'écrire du code propre et de qualité, il existe des conventions que les développeurs doivent suivre pour y parvenir. 

Il y a quelques points à garder à l'esprit lors de l'écriture de votre code. Dans cet article, nous allons apprendre les meilleures pratiques de codage que tout développeur C# devrait connaître.

## Conventions de nommage en C#

Il existe diverses conventions de nommage que vous devriez utiliser lorsque vous suivez les meilleures pratiques de codage en C#. 

L'utilisation de conventions de nommage cohérentes dans une base de code peut faciliter la compréhension et la navigation dans le code pour les développeurs, et peut aider à prévenir les conflits de nommage et la confusion. 

Les conventions de nommage suivantes sont généralement observées en programmation C#.

### Quand utiliser le Pascal case

Lors du nommage d'une **classe**, **structure, méthode**, **propriété,** ou **champ constant**, le Pascal casing est généralement préféré.

```cs
namespace ExampleApp
{

    class ClassNamingConvention
    {
        public const string ConstantFieldNamingConvention = "C#";
        public string PropertiesNamingConvention { get; set; }

        public void MethodNamingConvention()
        {
            //type something here
        }
    }
}
```

Lors du nommage d'une interface, elle est généralement préférée avec la lettre majuscule **I**. Vous pouvez également utiliser le Pascal case lors du nommage d'une interface.

```cs
public interface IInterfaceNamingConvention
{
        //type something here
}
```

### Quand utiliser le Camel case

Les Camel cases sont utilisés lors du nommage des **arguments de méthode, champs privés,** et **variables locales.** Les champs privés sont généralement préférés avec _.

```cs
private string _fieldsNamingConvention;

public void MethodNamingConvention(string methodArgsNamingConvention)
{
     string localVariables = "string here ...";            
}

```

### Utiliser des noms significatifs pour les classes, méthodes et propriétés

Utilisez toujours des noms significatifs et auto-explicatifs pour vos classes, méthodes et propriétés. Il est bon de nommer les propriétés, méthodes et classes avec ce qu'elles font. De cette façon, simplement en lisant le nom, vous pouvez facilement savoir ce qu'elles font exactement.

```cs
class AppNotification
    {
        private string _appStatus;
        public string AppStatus
        {
            get { return _appStatus; }
            set { _appStatus = value; }
        }

        public static void SendNotification()
        {
            //type something here . . .
        }
    }

```

### Utiliser des noms significatifs pour les variables de requête LINQ

Utilisez toujours des noms significatifs et auto-explicatifs pour vos variables de requête LINQ, comme le montre l'exemple ci-dessous.

```cs
public void QueryRacers()
{
     var racersInItaly = from racer in racers
                         where racer.City == "Lazio"
                         select racer.Name;
}

```

##   
Dispositions de code C# et commentaires

### Comment déclarer les variables membres et les champs

Déclarez toujours toutes vos variables membres et champs en haut d'une classe. Lorsque les champs sont déclarés en haut d'une classe, il est facile de voir toutes les variables que la classe utilise et de comprendre l'état général de la classe. 

Il est également important de déclarer les champs en haut d'une classe en C# car cela rend le code plus organisé et lisible, surtout lorsque vous travaillez avec de grandes classes ou lorsque vous travaillez en équipe. Cela facilite la compréhension du code et les modifications pour les autres.

```cs
    class Car
    {
        private int _carSpeed;
        public int CarSpeed
        {
            get { return _carSpeed; }
            set { _carSpeed = value; }
        }

        public static void GetMaxSpeed()
        {
            //...
        }

        public static void GetMaxAcceleration()
        {
            //...
        }
    }

```

### Formater et indenté correctement votre code

En ce qui concerne la disposition du code, il est important de formater et d'indenter correctement votre code pour la lisibilité et l'organisation propre du code. 

Il est bon de n'écrire qu'une seule instruction par ligne. Par exemple:

```cs
public void Numbers(int number)
{
       //Bonne pratique
      if (number > 0)
      {
           Console.WriteLine(number);
       }

       //Mauvaise pratique
      if (
            number 
              < 0
          )
          {
              Console.WriteLine(number);
          }
  }

```

### Comment écrire des commentaires

Il est bon de commencer vos commentaires par un texte en majuscule et de les terminer par un point. 

Écrire des commentaires est utile pour toute l'équipe. Cela rend le code plus lisible, maintenable et compréhensible. Il est bon de placer les commentaires sur une nouvelle ligne, pas à la fin de votre code. Par exemple:

```cs
    class Car
    {
        public string Name { get; set; }
        //Nous plaçons les commentaires ici.       
        //Et nous terminons par un point.

        public void Move()
        {
            //...
        }
    }

```

## Bonnes pratiques générales de codage en C#

### Comment comparer une valeur à une chaîne vide

Au lieu de " ", essayez `String.Empty` lorsque vous comparez une valeur à une chaîne vide. L'utilisation de String.Empty améliore la lisibilité du code et rend clair que la comparaison est destinée à être avec une chaîne vide. Cela facilite la compréhension et la maintenance du code à l'avenir.

```cs
public void NameCheck(string name)
{
     if(name == String.Empty)
     {

      }
 }

```

### Utiliser la gestion des exceptions

Utilisez la gestion des exceptions pour gérer élégamment les erreurs et les exceptions. Cela aide à prévenir les plantages de votre code et le rend plus robuste. Il est bon d'utiliser une instruction try-catch pour la plupart des gestions d'exceptions.

```cs
  public void NameCheck(string name)
    {
        try
        {
            //type code here
        }
        catch (Exception exception) { }
        {
            //type code here
        }
    }
```

### Utiliser `&&` et `||` pour de meilleures performances

Pour augmenter les performances de votre application, il est bon d'utiliser **&&** au lieu de **&** et **||** au lieu de **|** lorsque vous effectuez des comparaisons, comme le montre l'exemple suivant.

```cs
public void Numbers(int number)
{
   if (number > 2 && number < 4)
   {
       Console.WriteLine(number);
   }   
}
```

Cela est dû au fait que les opérateurs `&&` et `||` sont connus sous le nom d'opérateurs "**court-circuit**". Cela signifie que si le premier opérande d'une opération `&&` est faux, le deuxième opérande ne sera pas évalué car l'expression globale doit être fausse.

De même, si le premier opérande d'une opération `||` est vrai, le deuxième opérande ne sera pas évalué car l'expression globale doit être vraie. 

Cela augmente à son tour la performance de votre programme.

### Limiter les méthodes à une seule fonctionnalité

Il est préférable de limiter vos méthodes à une seule fonctionnalité. N'essayez pas de combiner plusieurs fonctionnalités d'une classe en une seule méthode. Cela garantit la lisibilité du code et vous aide à éviter d'écrire du "code spaghetti".

```cs
    class AppNotification
    {        
        public void SendNotification()
        {
            //. . .
        }

        public void ReceiveNotification()
        {
            //. . .
        }

        public void MuteNotification()
        {
            //. . .
        }
    }

```

### Utiliser des enums pour les valeurs discrètes

Utilisez des [enums](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/enum) au lieu d'utiliser des nombres et des chaînes pour indiquer des valeurs discrètes. Les enums fournissent un moyen d'améliorer la qualité de votre code en le rendant plus lisible, sécurisé et efficace. Ils fournissent également un moyen de définir un ensemble de constantes intégrales nommées.

```cs
 class Car
    {
        public enum LoggerType
        {
            NewCars,
            UsedCars,
            Database
        }
        public void DisplayException(string message, LoggerType loggerType)
        {
            switch (loggerType)
            {
                case LoggerType.NewCars:
                    Console.WriteLine(LoggerType.NewCars);
                    break;

                case LoggerType.UsedCars:
                    Console.WriteLine(LoggerType.UsedCars);
                    break;

                case LoggerType.Database:
                    Console.WriteLine(LoggerType.Database);
                    break;

                default:
                    Console.WriteLine(message);
                    break;
            }
        }
    }

```

### Comment comparer les variables de chaîne avec l'entrée utilisateur

Il est bon de toujours convertir les variables de chaîne en majuscules ou en minuscules avant de les comparer avec l'entrée utilisateur. 

Cela garantit que la comparaison est insensible à la casse. Cela rend votre code plus lisible et maintenable car il élimine le besoin de logique de gestion de casse.

```cs
  class Car
    {
        public void DisplayTransactions()
        {
            string name = Console.ReadLine();

            if(name.ToLower() == "Joe")
            {
                //...
            }

            //Ou.

            if (name.ToUpper() == "Joe")
            {
                //...
            }
        }
    }

```

## Conclusion

Les conventions de codage garantissent la lisibilité et la cohérence dans la base de code de l'équipe et de l'entreprise.

Il existe de nombreuses conventions de codage en C# qui aident à garantir la qualité du code. Vous pouvez consulter la documentation Microsoft .NET [documentation](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) pour en savoir plus sur les conventions de codage.

J'espère que vous avez appris beaucoup de choses à travers ce tutoriel.

Bon codage !