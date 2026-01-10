---
title: Comment convertir une chaîne de caractères en entier en C# – avec des exemples
  de code
subtitle: ''
author: Israel Chidera
co_authors: []
series: null
date: '2023-02-23T23:22:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-convert-a-string-to-an-integer-in-c-sharp
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/luca-bravo-XJXWbfSo2f0-unsplash.jpg
tags:
- name: C
  slug: c
seo_title: Comment convertir une chaîne de caractères en entier en C# – avec des exemples
  de code
seo_desc: 'There are various situations where you need to convert a string to a number.
  Whether you are working with user input or data from an external source, converting
  a string to a number is a common task for developers.

  This article will explore some of t...'
---

Il existe diverses situations où vous devez convertir une chaîne de caractères en nombre. Que vous travailliez avec des entrées utilisateur ou des données provenant d'une source externe, la conversion d'une chaîne de caractères en nombre est une tâche courante pour les développeurs.

Cet article explorera certaines des méthodes les plus courantes pour convertir une chaîne de caractères en entier en C# en utilisant les méthodes **`int.Parse()`**, **`int.TryParse()`** et **`Convert.ToInt32()`**. 

Cet article fournira également des exemples pour vous aider à comprendre la syntaxe de chaque méthode. Que vous soyez débutant ou programmeur expérimenté, ce guide offrira une introduction conviviale au sujet.

Le mot-clé **`Int`** est un alias pour le type **`System.Int32`**, et il est utilisé pour déclarer des variables qui peuvent contenir des entiers signés de 32 bits dans la plage de -2 147 483 648 à 2 147 483 647. **`Int32`** est un type de valeur intégré qui représente un entier signé de 32 bits. Vous pouvez convertir une chaîne de caractères en Int en utilisant la méthode suivante.

## Comment convertir une chaîne de caractères en Int en utilisant `Int32.Parse()`

`Int32.Parse()` est le moyen le plus simple de convertir une chaîne de caractères en entier. Il prend une chaîne de caractères comme paramètre. Voici un exemple :

```cs
string numberString = "8";
int i = int.Parse(numberString); 
Console.WriteLine("Valeur de i : {0}", i);
```

Le code ci-dessus montre comment convertir une chaîne de caractères en entier en utilisant la méthode **`int.Parse()`**. La méthode prend une variable de chaîne de caractères appelée **`numberString`** et la convertit en int. 

L'inconvénient de l'utilisation de la méthode **`int.Parse()`** est qu'une exception sera levée si elle ne peut pas être analysée avec succès en entier. Pour éviter ce problème, vous pouvez utiliser un bloc try-catch lors de l'utilisation de **`int.Parse()`**. Voici comment faire :

```cs
string numString = "12"; 
try
{
    int num = int.Parse(numString);              
}
catch(FormatException ex)
{
    Console.WriteLine(ex.Message);                
}
```

Une autre solution possible est d'utiliser **`TryParse()`**, que nous allons discuter ci-dessous.

## Comment convertir une chaîne de caractères en Int en utilisant `Convert.ToInt32()`

`Convert.ToInt32()` est une méthode statique fournie par C# pour convertir une chaîne de caractères en entier signé de 32 bits. Cette méthode prend une variable de chaîne de caractères en entrée et retourne un entier. Voici un exemple :

```cs
string numString = "123";
int num = Convert.ToInt32(numString);
```

Dans le bloc de code ci-dessus, nous avons déclaré une variable de chaîne de caractères, **`numString`**, et lui avons attribué une valeur. Nous utilisons ensuite la méthode **`Convert.ToInt32()`** pour convertir cette chaîne de caractères en entier et l'assigner à une variable nommée **`num`**. 

La méthode `Convert.ToInt32()` a deux exceptions, **`FormatException`** et **`OverflowException`**, et est capable de convertir une variable nulle en 0 sans lever d'exception.

## Comment convertir une chaîne de caractères en Int en utilisant `Int32.TryParse()`

Comparé à la méthode **`int.Parse()`**, **`int.TryParse()`** est un moyen plus sûr de convertir une chaîne de caractères en entier signé de 32 bits. 

Cette méthode prend une variable de chaîne de caractères et un paramètre **`out`** et retourne un **`bool`** de valeur `true` si l'analyse est réussie. Le résultat de l'analyse est stocké dans un paramètre **`out`**. 

C'est le moyen le plus sûr de convertir une variable de chaîne de caractères en entier. Voici un exemple :

```cs
string numString = "12";

if (int.TryParse(numString, out int num))
{
	// Conversion réussie, faites quelque chose avec num.
    Console.WriteLine("Réussie");
    Console.WriteLine(num);
}
else
{
	// Conversion échouée, gérez l'erreur.
    Console.WriteLine("Échouée..");
}
```

Dans le code ci-dessus, nous avons essayé d'analyser une variable de chaîne de caractères appelée **`numString`** en entier en utilisant la méthode **`int.TryParse()`**. Le résultat est stocké dans la variable **`num`** si la conversion est réussie. Si la conversion échoue, la variable de succès est définie sur false et la variable num est assignée à sa valeur par défaut.

## Conclusion

Convertir une chaîne de caractères en nombre est une tâche courante en programmation, et C# offre diverses façons d'accomplir cette tâche. 

Dans cet article, nous avons vu certaines des méthodes pour convertir une chaîne de caractères en entier en C# en utilisant les méthodes `Parse()`, `TryParse()` et `Convert()`. J'espère que cet article vous a aidé à en apprendre davantage sur la conversion de chaînes de caractères en entiers en C#.  
  
Bon codage !