---
title: Bases de C# - Votre premier programme C#, types et variables, et instructions
  de contrôle de flux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/c-basics-your-first-c-program-types-and-variables-and-flow-control-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d0a740569d1a4ca3590.jpg
tags:
- name: C
  slug: c
- name: toothbrush
  slug: toothbrush
seo_title: Bases de C# - Votre premier programme C#, types et variables, et instructions
  de contrôle de flux
seo_desc: 'Setup

  LinqPad is an .NET scratchpad to quickly test your C# code snippets. The standard
  edition is free and a perfect tool for beginners to execute language statements,
  expressions and programs.

  Alternatively, you could also download Visual Studio Co...'
---

## **Installation**

[LinqPad](http://www.linqpad.net/) est un bloc-notes .NET pour tester rapidement vos extraits de code C#. L'édition standard est gratuite et constitue un outil parfait pour les débutants afin d'exécuter des instructions, des expressions et des programmes.

Alternativement, vous pouvez également télécharger [Visual Studio Community 2015](https://www.visualstudio.com/en-us/products/visual-studio-community-vs.aspx), un [IDE](https://en.wikipedia.org/wiki/Integrated_development_environment) extensible utilisé par la plupart des professionnels pour créer des applications d'entreprise.

## **Votre premier programme C#**

```text
//ci est un commentaire sur une seule ligne

/** Ceci est un commentaire multiline,
le compilateur ignore tout code à l'intérieur des blocs de commentaires.
**/

//Ceci est l'espace de noms, partie de la bibliothèque de classes du Framework .NET standard
using System;
// l'espace de noms définit la portée des objets apparentés dans des packages
namespace Learning.CSharp
{  
  // nom de la classe, doit être le même que celui du fichier .cs
  public class Program
  {
    //méthode de point d'entrée pour les applications console
   public static void Main()
    {
      //imprimer des lignes sur la console
      Console.WriteLine("Hello, World!");
      //Lit la ligne suivante de caractères à partir du flux d'entrée standard. L'utilisation la plus courante est de mettre en pause l'exécution du programme avant de vider la console.
      Console.ReadLine();
    }
  }
}
```

Chaque application console C# doit avoir une [méthode Main](https://msdn.microsoft.com/en-gb/library/acy3edy3.aspx) qui est le point d'entrée du programme.

Modifiez [HelloWorld](https://dotnetfiddle.net/kY7QRm) dans .NET Fiddle, un outil inspiré par [JSFiddle](http://jsfiddle.net/) où vous pouvez modifier les extraits de code et vérifier le résultat par vous-même. Notez que ceci est juste pour partager et tester les extraits de code, et non pour développer des applications.

Si vous utilisez Visual Studio, suivez ce [tutoriel](https://msdn.microsoft.com/en-us/library/k1sx6ed2.aspx) pour créer une application console et comprendre votre premier programme C#.

## **Types et variables**

C# est un langage fortement typé. Chaque variable a un type. Chaque expression ou instruction évalue une valeur. Il existe deux types de types en C# :

* Types de valeur
* Types de référence.

**Types de valeur** : Les variables qui sont des types de valeur contiennent directement des valeurs. L'assignation d'une variable de type valeur à une autre copie la valeur contenue.

[Modifier dans .NET Fiddle](https://dotnetfiddle.net/JCkTxb)

```text
int a = 10;
int b = 20;
a=b;
Console.WriteLine(a); //imprime 20
Console.WriteLine(b); //imprime 20
```

Notez que dans d'autres langues dynamiques, cela pourrait être différent, mais en C#, il s'agit toujours d'une copie de valeur. Lorsqu'un type de valeur est créé, un seul espace est probablement créé dans la [pile](http://gribblelab.org/CBootcamp/7_Memory_Stack_vs_Heap.html#orgheadline2), qui est une structure de données "LIFO" (dernier entré, premier sorti). La pile a des limites de taille et les opérations de mémoire sont efficaces. Quelques exemples de types de données intégrés sont `int, float, double, decimal, char et string`.

Type | Exemple | Description  
--------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------  
_Integer_ | `int fooInt = 7;` | **Entier signé 32 bits**  
_Long_ | `long fooLong = 3000L;` | **Entier signé 64 bits**. **L est utilisé pour spécifier que la valeur de cette variable est de type long/ulong**  
_Double_ | `double fooDouble = 20.99;` | Précision : **15-16 chiffres**  
_Float_ | `float fooFloat = 314.5f;` | Précision : **7 chiffres**. **F est utilisé pour spécifier que la valeur de cette variable est de type float**  
_Decimal_ | `decimal fooDecimal = 23.3m;` | Précision : **28-29 chiffres**. Sa précision plus élevée et sa plage plus petite le rendent approprié pour les **calculs financiers et monétaires**  
_Char_ | `char fooChar = 'Z';` | Un seul **caractère Unicode 16 bits**  
_Boolean_ | `bool fooBoolean = false;` | Booléen - **vrai & faux**  
_String_ | `string fooString = "\"escape\" quotes and add \n (new lines) and \t (tabs);` | **Une chaîne de caractères Unicode**.

Pour la liste complète de tous les types de données intégrés, voir [ici](https://msdn.microsoft.com/en-us/library/ms228360)

[**Types de référence**](https://msdn.microsoft.com/en-us/library/490f96s2.aspx) : Les variables de types de référence stockent des références à leurs objets, ce qui signifie qu'elles stockent l'adresse de l'emplacement des données sur la [pile](http://gribblelab.org/CBootcamp/7_Memory_Stack_vs_Heap.html#orgheadline2), également connues sous le nom de pointeurs. Les données réelles sont stockées dans la mémoire [tas](http://gribblelab.org/CBootcamp/7_Memory_Stack_vs_Heap.html#orgheadline3). L'assignation d'un type de référence à un autre ne copie pas les données, mais crée plutôt une seconde copie de la référence qui pointe vers le même emplacement sur le tas.

Dans le tas, les objets sont alloués et désalloués dans un ordre aléatoire, c'est pourquoi cela nécessite la surcharge de la gestion de la mémoire et de la [collecte des déchets](https://msdn.microsoft.com/en-us/library/hh156531(v=vs.110).aspx).

Sauf si vous écrivez du [code non sécurisé](https://msdn.microsoft.com/en-us/library/t2yzs44b.aspx) ou traitez avec du [code non géré](https://msdn.microsoft.com/en-us/library/sd10k43k(v=vs.100).aspx), vous n'avez pas besoin de vous soucier de la durée de vie de vos emplacements de mémoire. Le compilateur .NET et le CLR s'en occuperont, mais il est toujours bon de garder cela à l'esprit afin d'optimiser les performances de vos applications.

Plus d'informations [ici](http://www.c-sharpcorner.com/UploadFile/rmcochran/csharp_memory01122006130034PM/csharp_memory.aspx?ArticleID=9adb0e3c-b3f6-40b5-98b5-413b6d348b91).

## **Instructions de contrôle de flux**

### [Instruction If else](https://msdn.microsoft.com/en-us/library/5011f09h.aspx)

```text
int myScore = 700;
if (myScore == 700) {
 Console.WriteLine("J'ai été imprimé sur la console");
} else if (myScore > 10) {
 Console.WriteLine("Je ne le suis pas");
} else {
 Console.WriteLine("Je ne le suis pas non plus");
}

/** Opérateurs ternaires
 Une simple instruction if/else peut également être écrite comme suit
 <condition> ? <vrai> : <faux> **/
int myNumber = 10;
string isTrue = myNumber == 10 ? "Oui" : "Non";
```

[Modifier dans .NET Fiddle](https://dotnetfiddle.net/IFVB33)

### [Instruction Switch](https://msdn.microsoft.com/en-GB/library/06tc147t.aspx)

```csharp
using System;
public class Program {
 public static void Main() {
   int myNumber = 0;
   switch (myNumber) { // Une section switch peut avoir plus d'une étiquette de cas. 
    case 0:
    case 1:
     {
      Console.WriteLine("Cas 0 ou 1");
      break;
     }

   }
```

[Modifier dans .NET Fiddle](https://dotnetfiddle.net/lPZftO)

### [For](https://msdn.microsoft.com/en-us/library/ch45axte.aspx) & [Foreach](https://msdn.microsoft.com/en-gb/library/ttw7t8t6.aspx)

```csharp
for (int i = 0; i < 10; i++) {
 Console.WriteLine(i); //imprime 0-9 }
 Console.WriteLine(Environment.NewLine);
 for (int i = 0; i <= 10; i++) {
  Console.WriteLine(i); //imprime 0-10 }
  Console.WriteLine(Environment.NewLine);
  for (int i = 10 - 1; i >= 0; i--) //boucle de décrémentation 
  {
   Console.WriteLine(i); //imprime 9-0 }
   Console.WriteLine(Environment.NewLine); //for (; ; ) { // Toutes les expressions sont facultatives. Cette instruction //crée une boucle infinie.* //}
```

[Modifier dans .NET Fiddle](https://dotnetfiddle.net/edxtvq)

### [While](https://msdn.microsoft.com/en-us/library/2aeyhxcd.aspx) & [do-while](https://msdn.microsoft.com/en-us/library/370s1zax.aspx) 

```csharp
// Continuer la boucle while jusqu'à ce que l'index soit égal à 10. 
int i = 0;
while (i < 10) {
 Console.Write("Instruction While");
 Console.WriteLine(i); // Écrire l'index à l'écran. i++;// Incrémenter la variable. }
 int number = 0; // faire le travail d'abord, jusqu'à ce que la condition soit satisfaite, c'est-à-dire se termine lorsque le nombre est égal à 4. do 
 {
  Console.WriteLine(number); //imprime la valeur de 0-4 
  number++; // Ajouter un au nombre. 
 }
 while (number <= 4);
```

[Modifier dans .NET Fiddle](https://dotnetfiddle.net/O5hOF1)