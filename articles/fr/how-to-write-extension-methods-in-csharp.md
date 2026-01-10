---
title: Comment écrire des méthodes d'extension en C#
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-10-31T03:01:42.549Z'
originalURL: https://freecodecamp.org/news/how-to-write-extension-methods-in-csharp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730322390431/42cfe64d-0fce-4f36-a4f7-25e1e56267a4.png
tags:
- name: C#
  slug: csharp
seo_title: Comment écrire des méthodes d'extension en C#
seo_desc: 'Extension methods are a fundamental part of C# and Object Oriented Programming
  (OOP). Extension methods in C# allow you to "extend" existing types, including classes,
  interfaces, or structs, without modifying their original code.

  This is particularly...'
---

Les méthodes d'extension sont une partie fondamentale de C# et de la programmation orientée objet (POO). Les méthodes d'extension en C# vous permettent d'"étendre" des types existants, y compris des classes, des interfaces ou des structures, sans modifier leur code original.

Cela est particulièrement utile lorsque vous souhaitez ajouter une nouvelle fonctionnalité à un type que vous ne possédez pas ou que vous ne pouvez pas modifier, comme les types provenant de bibliothèques tierces ou les types .NET intégrés tels que `string`, `List<T>`, et ainsi de suite.

Dans cet article, vous apprendrez comment ajouter des méthodes d'extension à vos classes, ainsi qu'aux classes tierces et système.

## Table des matières

* [Comment créer des méthodes d'extension DateTime](#heading-comment-creer-des-methodes-dextension-datetime)
    
* [Comment enchaîner des méthodes d'extension de même type](#heading-comment-enchainer-des-methodes-dextension-de-meme-type)
    
* [Pourquoi ne puis-je pas simplement ajouter ces méthodes à ma classe ?](#heading-pourquoi-ne-puis-je-pas-simplement-ajouter-ces-methodes-a-ma-classe)
    
* [Quand utiliser les extensions](#heading-quand-utiliser-les-extensions)
    
* [Quand ne pas utiliser les méthodes d'extension](#heading-quand-ne-pas-utiliser-les-methodes-dextension)
    
* [Éléments à considérer lors de la conception d'extensions](#heading-elements-a-considerer-lors-de-la-conception-dextensions)
    
* [Conclusion](#heading-conclusion)
    

## Comment créer des méthodes d'extension DateTime

Supposons que nous voulons certaines méthodes qui peuvent être utilisées avec la classe `DateTime` existante, peut-être une méthode qui retourne si l'objet `DateTime` donné est un week-end ou autre chose.

Les méthodes d'extension doivent être définies dans une classe statique car elles sont essentiellement du sucre syntaxique qui vous permet d'appeler une méthode statique comme si elle était une méthode d'instance sur le type que vous étendez.

Les méthodes d'extension doivent être dans une classe statique car :

1. **Aucun objet nécessaire :** Vous n'avez pas besoin de créer un objet pour utiliser une méthode d'extension. Puisque la méthode ajoute une nouvelle fonctionnalité à un type existant (comme `string`), elle peut fonctionner sans avoir besoin d'une instance de la classe.
    
2. **Code organisé :** Placer les méthodes d'extension dans une classe statique garde les choses bien rangées. Cela vous permet de regrouper les méthodes connexes, et vous pouvez facilement les inclure dans votre code en utilisant l'espace de noms approprié.
    

Ainsi, en utilisant une classe statique, vous pouvez ajouter des méthodes utiles aux types existants sans changer leur code original, et vous n'avez pas besoin d'un objet pour les appeler.

Tout d'abord, créons une classe statique `DateTimeExtensions`.

```csharp
public static class DateTimeExtensions {

}
```

Cela englobera toutes les extensions `DateTime` que nous voulons créer.

```csharp
public static bool IsWeekend(this DateTime date)
{
    return date.DayOfWeek is DayOfWeek.Saturday or DayOfWeek.Sunday;
}
```

**Explication :**

`public static bool IsWeekend` : Cela définit qu'il s'agit d'une méthode statique appelée `IsWeekend` qui retournera une valeur `bool` (vrai/faux).

`this DateTime date` : Le mot-clé `this` en tant qu'argument de méthode indique que cette méthode est une méthode d'extension. Cela signifie que la méthode sera une extension de la classe `DateTime`.

## Comment enchaîner des méthodes d'extension de même type

Pour qu'une méthode d'extension puisse être enchaînée avec d'autres, elle doit généralement retourner le même type que celui qu'elle étend (ou un type compatible). Cela permet à une autre méthode d'être appelée sur le résultat de la précédente.

```csharp
using System.Globalization;

public static string ToTitleCase(this string str)
{
    return CultureInfo.CurrentCulture.TextInfo.ToTitleCase(str.ToLower());
}

public static string TrimAndAppend(this string str, string toAppend)
{
    return str.Trim() + toAppend;
}
```

Dans l'exemple ci-dessus, les méthodes `ToTitleCase` et `TrimAndAppend` retournent une valeur de type string, ce qui signifie que nous pouvons enchaîner les méthodes d'extension comme ci-dessous, ce qui convertira la chaîne en casse titre avant de supprimer tous les espaces blancs et d'ajouter la chaîne fournie.

Remarquez que nous n'avons fourni que le deuxième paramètre à la méthode `TrimAndAppend`, car le premier paramètre est la chaîne à laquelle la méthode d'extension est appliquée (comme expliqué précédemment, désigné par le mot-clé `this`).

```csharp
var title = "hello world   "
    .ToTitleCase()
    .TrimAndAppend("!!");

//Sortie:
// Hello World!!
```

Si la méthode d'extension retourne un type différent (pas l'original ou un type compatible), vous ne pouvez pas l'enchaîner. Par exemple :

```csharp
var date = new DateTime();
date.IsWeekend().AddDays(1);
```

Pour des raisons moins évidentes, cela ne fonctionnera pas. Lorsque vous enchaînez des méthodes, elles ne s'enchaînent pas à partir de la variable originale—elles s'enchaînent à partir du type de retour de l'appel de méthode précédent.  
  
Ici, nous avons une date appelée `IsWeekend()` qui retourne un booléen. Nous avons ensuite tenté d'appeler `AddDays(1)` sur une valeur booléenne qui n'existe pas, car il s'agit d'une extension `DateTime`. Le compilateur de code échouera à la construction, soulevant une erreur vous informant de cela.

### Comment retourner l'instance pour l'enchaînement

Dans certaines méthodes d'extension, en particulier celles pour la configuration (comme l'injection de dépendances), vous retournez la même instance pour permettre l'enchaînement des méthodes. Cela vous permet de continuer à travailler avec l'objet original ou son état modifié à travers plusieurs appels, permettant une interface fluide.

Prenons l'exemple d'une liste de voitures.

```csharp
public static List<T> RemoveDuplicates<T>(this List<T> list)
{
    // Utiliser Distinct pour supprimer les doublons et mettre à jour la liste
    list = list.Distinct().ToList();
        
    // Retourner la liste modifiée pour permettre l'enchaînement des méthodes
    return list;
}

public static List<T> AddRangeOfItems<T>(this List<T> list, IEnumerable<T> items)
{
    // Ajouter une série d'éléments à la liste
    list.AddRange(items);

    // Retourner la liste modifiée pour permettre l'enchaînement des méthodes
    return list;  
}
```

Maintenant que nous avons retourné la liste à partir de ces méthodes d'extension, nous pouvons enchaîner des méthodes supplémentaires sur la même liste. Par exemple, après avoir supprimé les doublons avec `RemoveDuplicates()`, nous pouvons immédiatement appeler `AddRangeOfItems()` sur la même liste.

Nous pouvons donc faire quelque chose comme :

```csharp
var existingStock = new List<string> { "Ford", "Jaguar", "Ferrari", "Ford", "Renault" };

var availableBrands = existingStock
    .RemoveDuplicates()
    .AddRangeOfItems(new[] { "Lamborghini" }); // nouveau stock disponible

Console.WriteLine("Marques disponibles maintenant : " + string.Join(", ", availableBrands));

// Sortie : Marques disponibles maintenant : Ford, Jaguar, Ferrari, Renault, Lamborghini
```

Nous avons supprimé les doublons d'une liste de marques de voitures et ajouté un nouveau stock à la même liste. Cela fonctionne parce que `RemoveDuplicates` retourne la liste, nous permettant de l'enchaîner avec `AddRangeOfItems`.

Si `RemoveDuplicates` retournait `void` au lieu de la liste, nous ne pourrions pas enchaîner les méthodes. Cela supprimerait toujours les doublons, mais des actions supplémentaires comme l'ajout de nouveau stock ne seraient pas possibles dans la même expression.

Nous devrions également mettre à jour `RemoveDuplicates` pour mettre à jour l'argument de liste passé, car `Distinct()` retourne une nouvelle liste qui n'est pas retournée comme montré ci-dessous, ce qui, je pense, vous serez d'accord, est beaucoup plus verbeux.

```csharp
public static void RemoveDuplicates<T>(this List<T> list)
{
    // Obtenir les éléments distincts et vider la liste originale
    var distinctItems = list.Distinct().ToList();
    list.Clear(); 
    
    // Ajouter les éléments distincts à la liste originale
    list.AddRange(distinctItems);
}
```

## Pourquoi ne puis-je pas simplement ajouter ces méthodes à ma classe ?

Si la méthode n'est pas une partie centrale de la fonctionnalité de la classe, la placer dans une méthode d'extension peut aider à garder la classe concentrée et maintenable.

**Séparation des préoccupations :** L'utilisation de méthodes d'extension garde votre code plus propre et aide à réduire la complexité. Cela aide à éviter d'alourdir la classe avec des méthodes qui peuvent ne pas être utilisées fréquemment.

**Amélioration des bibliothèques externes :** Si vous utilisez une bibliothèque ou un framework où vous ne pouvez pas modifier le code source, les méthodes d'extension vous permettent d'ajouter des fonctionnalités à ces types sans altérer leurs définitions.

Supposons que vous utilisez la classe `FileInfo` de l'espace de noms [`System.IO`](http://System.IO) pour travailler avec des fichiers. Vous pouvez vouloir ajouter une méthode pour vérifier facilement si un fichier est trop grand (par exemple, plus de 1 Go), mais vous ne pouvez pas modifier directement la classe `FileInfo` car elle appartient à l'espace de noms System.IO (c'est-à-dire qu'elle est intégrée à .Net).

**Sans extension :**

```csharp
var fileInfo = new FileInfo("myFile.txt");

if (fileInfo.Length > 1024 * 1024 * 1024) // la taille du fichier est supérieure à 1 Go
{
    Console.WriteLine("Le fichier est trop volumineux.");
}
else
{
    Console.WriteLine("La taille du fichier est acceptable.");
}
```

**Avec méthode d'extension :**

Vous pouvez rendre cela plus réutilisable en ajoutant une méthode d'extension qui vérifie si le fichier est plus grand que 1 Go.

```csharp
public static class FileInfoExtensions
{
    // méthode d'extension, avec une taille de fichier par défaut de 1 Go (peut être remplacée)
    public static bool IsFileTooLarge(this FileInfo fileInfo, long sizeInBytes = 1024 * 1024 * 1024)
    {
        return fileInfo.Length > sizeInBytes;
    }
}
```

Maintenant, vous pouvez utiliser la méthode `IsFileTooLarge` directement sur les objets `FileInfo`, rendant votre code plus propre :

```csharp
csharpCopy codevar fileInfo = new FileInfo("myFile.txt");

if (fileInfo.IsFileTooLarge())
{
    Console.WriteLine("Le fichier est trop volumineux.");
}
else
{
    Console.WriteLine("La taille du fichier est acceptable.");
}
```

L'extension des bibliothèques et packages tiers peut rendre votre code beaucoup plus compatible.

**Meilleure organisation et lisibilité :** Vous pouvez organiser les méthodes d'extension dans des classes statiques basées sur la fonctionnalité ou le contexte, ce qui facilite leur recherche et leur utilisation. Cela est certainement amélioré en permettant l'enchaînement des méthodes d'extension.

## Quand utiliser les extensions

* **Pour les méthodes utilitaires :** Si vous avez des méthodes utilitaires qui sont utiles pour un type mais qui n'appartiennent pas directement au type lui-même (par exemple, formatage, validation).
    
* **Pour améliorer les types intégrés :** Si vous souhaitez ajouter des fonctionnalités aux types intégrés (comme `string` ou `DateTime`) sans les modifier.
    
* **Lorsque vous souhaitez garder les méthodes optionnelles :** Si vous souhaitez fournir des méthodes supplémentaires que les utilisateurs peuvent choisir d'utiliser sans les forcer à les incorporer dans la conception de la classe principale.
    

### **Scénario d'exemple**

Imaginez que vous avez une classe `Person`, et que vous souhaitez ajouter une méthode pour formater le nom de la personne de manière élégante :

```csharp
public class Person
{
    public string FirstName { get; set; }
    public string LastName { get; set; }
}

// Méthode d'extension dans une classe statique
public static class PersonExtensions
{
    public static string GetFullName(this Person person)
    {
        return $"{person.FirstName} {person.LastName}";
    }
}
```

En utilisant une méthode d'extension pour `GetFullName`, vous pouvez garder la classe `Person` simple et concentrée sur ses responsabilités principales, tout en fournissant une fonctionnalité utile.

## Quand ne pas utiliser les méthodes d'extension

* **Pour la fonctionnalité principale :** Si une méthode est essentielle au comportement principal d'une classe, elle doit faire partie de la classe elle-même, et non d'une extension.
    
* **Pour un couplage serré :** Si la méthode d'extension nécessite une connaissance intime de l'état privé de la classe ou a besoin d'un accès régulier à sa logique interne.
    
* **Pour les API publiques :** Lors de la conception d'une bibliothèque ou d'une API publique, il est souvent préférable d'inclure les méthodes nécessaires directement dans la classe plutôt que de forcer les utilisateurs à trouver ou à créer leurs propres méthodes d'extension.
    

## Éléments à considérer lors de la conception d'extensions

Bien que les méthodes d'extension soient puissantes et pratiques dans de nombreux cas, il existe certains inconvénients ou situations où leur utilisation pourrait ne pas être le meilleur choix :

### Comportement caché/Confusion

* Les méthodes d'extension n'apparaissent pas directement dans la définition de la classe, ce qui signifie qu'elles peuvent être plus difficiles à découvrir par les développeurs qui ne sont pas familiers avec les extensions disponibles.
    
* Les développeurs doivent savoir que ces méthodes d'extension existent, sinon ils pourraient ne pas les utiliser à moins qu'ils ne travaillent dans un IDE avec des fonctionnalités comme IntelliSense (par exemple, Visual Studio, JetBrains Rider). Ces IDE peuvent suggérer des méthodes d'extension à partir d'autres fichiers ou espaces de noms lorsqu'ils détectent le type approprié. Sans un IDE riche en fonctionnalités, le développeur devrait être conscient des méthodes d'extension ou trouver le dossier où elles sont stockées.
    

### **Ne peut pas accéder aux membres privés**

* Les méthodes d'extension ne peuvent accéder qu'aux membres (méthodes, propriétés, champs) qui sont publics ou internes.
    
* Elles ne peuvent pas accéder aux membres privés ou protégés d'une classe car les méthodes d'extension fonctionnent comme si elles faisaient partie de la classe de l'extérieur, similaire aux appels de méthodes réguliers depuis l'extérieur de la classe.
    

**Exemple :**

```csharp
public class Car
{
    private string engineNumber = "12345"; // Champ privé
    
    public string Brand { get; set; } = "Ford"; // Propriété publique
    
    private void StartEngine() // Méthode privée
    {
        Console.WriteLine("Moteur démarré");
    }
}
```

```csharp
public static class CarExtensions
{
    public static void DisplayBrand(this Car car)
    {
        Console.WriteLine($"Marque : {car.Brand}"); // Accès à la propriété publique 'Brand'
    }

    public static void TryAccessPrivateField(this Car car)
    {
        // Impossible d'accéder au champ privé 'engineNumber'
        // Cela entraînera une erreur de compilation.
        Console.WriteLine(car.engineNumber);
    }
}
```

### **Duplication de code et surutilisation**

* Dans certains cas, les méthodes d'extension peuvent encourager la duplication de code. Si plusieurs projets ou classes nécessitent des méthodes d'extension similaires, vous pourriez finir par écrire ou copier les mêmes méthodes d'extension à différents endroits, ce qui rend plus difficile la gestion et la mise à jour cohérente du code.
      
    Pour éviter cela, organisez votre code efficacement. Je recommanderais de garder toutes les extensions dans un dossier ou un projet d'extensions, proche de l'origine (en fonction des modèles de conception utilisés dans votre application).
    

* **Abus des extensions :** Si elles sont utilisées de manière excessive, elles peuvent encombrer l'espace global avec des méthodes qui n'ont peut-être pas besoin d'être globales. Cela peut causer une pollution de l'API du type, rendant plus difficile la compréhension de ce qui est central dans la classe par rapport à ce qui est ajouté via des extensions.
    
      
    Dans certains cas, il est préférable d'encapsuler la fonctionnalité dans des classes ou services d'assistance séparés plutôt que de l'ajouter via des méthodes d'extension.
    

## Conclusion

Les méthodes d'extension sont utiles pour ajouter des fonctionnalités de manière propre et modulaire, mais elles peuvent également introduire de la confusion, des conflits de noms et un manque d'accès aux membres privés.

Comme souligné tout au long de l'article, elles ont de nombreuses utilisations et sont certainement une fonctionnalité très intéressante du framework Dotnet lorsqu'elles sont utilisées efficacement. Elles doivent être utilisées lorsque cela est approprié, mais pas comme substitut à une fonctionnalité qui appartient à la classe elle-même.