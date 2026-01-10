---
title: Comment utiliser les boucles en C#
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2025-09-17T12:14:48.985Z'
originalURL: https://freecodecamp.org/news/how-to-use-loops-in-c
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757595108095/f7bd2673-3da5-4f34-8541-64cc8129fe96.jpeg
tags:
- name: C#
  slug: csharp
- name: Loops
  slug: loops
seo_title: Comment utiliser les boucles en C#
seo_desc: Writing the same code repeatedly is poor practice in C# and doesn’t follow
  the Don’t Repeat Yourself (DRY) principle. But, there are many times in programming
  where you need to repeat commands, operations, or computations multiple times —
  perhaps cha...
---

Écrire le même code de manière répétée est une mauvaise pratique en C# et ne respecte pas le principe DRY (Don’t Repeat Yourself). Cependant, il arrive souvent en programmation que vous deviez répéter des commandes, des opérations ou des calculs plusieurs fois — en changeant peut-être un petit détail à chaque itération.

C'est là que les boucles entrent en jeu. Dans cet article, vous apprendrez :

* Comment créer votre première boucle
    
* Les avantages et les mises en garde liés à l'utilisation des boucles
    
* Les différents types de boucles en C# et comment les utiliser
    
* Quand il est préférable d'utiliser chacune d'elles
    

## Table des matières

* [Comment utiliser une boucle For en C#](#heading-comment-utiliser-une-boucle-for-en-c#)
    
* [Comment utiliser une boucle ForEach en C#](#heading-comment-utiliser-une-boucle-foreach-en-c#)
    
* [Comment utiliser une boucle Do..While en C#](#heading-comment-utiliser-une-boucle-dowhile-en-c#)
    
* [Comment utiliser une boucle While en C#](#heading-comment-utiliser-une-boucle-while-en-c#)
    
* [Dernières réflexions : choisir la bonne boucle](#heading-dernieres-reflexions-choisir-la-bonne-boucle)
    

Commençons. Ouvrez votre IDE ou éditeur de code préféré et créez une nouvelle Application Console en .Net 8+.

## Comment utiliser une boucle For en C#

Une boucle `for` répète un bloc de code un nombre défini de fois en :

* Initialisant une variable de boucle.
    
* Vérifiant une condition avant chaque itération.
    
* Mettant à jour la variable de boucle après chaque itération.
    

Vous pouvez créer une boucle `for` avec le code ci-dessous :

```csharp
// nombre d'itérations
var totalIterations = 5

// la boucle
for(int i = 0; i <= totalIterations; i++){
   Console.Write($"{i},");
}

// Sortie
0,1,2,3,4,5,
```

**Analyse détaillée :**

* `for` — déclare la boucle
    
* `int i = 0;` — définit le point de départ de la variable de boucle `i`
    
* `i <= totalIterations;` — la condition pour continuer la boucle. Le code à l'intérieur de la boucle ne s'exécute que si cette condition est vraie.
    
* `i++` — raccourci pour « augmenter `i` de 1 » après chaque itération
    

### Itérations et zéro

Pourquoi l'exemple affiche-t-il six nombres alors que `totalIterations` est égal à 5 ? C# utilise une indexation basée sur zéro. Compter de 0 → 5 inclut six nombres : 0, 1, 2, 3, 4, 5.

Si vous souhaitez afficher 1 → 5 à la place, commencez `i` à 1 :

```csharp
var totalIterations = 5;
for (int i = 1; i <= totalIterations; i++)
{
    Console.Write($"{i},");
}
// Sortie : 1,2,3,4,5
```

**Conseil :**  
En général, les boucles `for` sont utilisées pour indexer/accéder aux éléments dans des collections. Il est donc courant de commencer votre variable de boucle à 0 et d'utiliser `<` (inférieur à) un nombre donné ou la longueur de la collection.

### Inversion de direction

Vous pouvez inverser une boucle `for` en commençant par la fin et en décrémentant `i` :

```csharp
for (int i = 5; i > 0; i--)
{
    Console.Write($"{i},");
}
// Sortie : 5,4,3,2,1
```

La boucle vérifie si `i > 0`. Après chaque itération, `i` diminue de 1, affichant les nombres par ordre décroissant.

### Autres utilisations des boucles For

Supposons que vous vouliez accéder à un élément sur deux dans une liste. C'est ici que la puissance des boucles `for` se révèle, et nous pouvons maximiser notre `variable de boucle` en l'utilisant comme accesseur d'index.

```csharp
public class Address
{
    public string Name { get; set; } = string.Empty;
    public string AddressLineOne { get; set; } = string.Empty;
    public int HouseNumber { get; set; } = default;
    public string PostCode { get; set; } = string.Empty;
    public string Telephone { get; set; } = string.Empty;
}

internal class Program
{
    public static void Main()
    {
        var addressBook = new List<Address>
        {
            new Address
            {
                Name = "Grant", AddressLineOne = "Developer Avenue", HouseNumber = 1, PostCode = "DV19 8EP",
                Telephone = "0102919 93020-92019"
            },
            new Address
            {
                Name = "Bill", AddressLineOne = "Developer Avenue", HouseNumber = 19, PostCode = "DV19 8EP",
                Telephone = "0102919 93020-92019"
            },
            new Address
            {
                Name = "Rebecca", AddressLineOne = "Developer Avenue", HouseNumber = 4, PostCode = "DV19 8EP",
                Telephone = "0102919 93020-92019"
            },
            new Address
            {
                Name = "Amy", AddressLineOne = "Rower Avenue", HouseNumber = 1, PostCode = "DV19 8EP",
                Telephone = "0102919 93020-92019"
            },
            new Address
            {
                Name = "Joe", AddressLineOne = "Olympic Drive", HouseNumber = 1, PostCode = "DV19 10E",
                Telephone = "0102919 93020-92019"
            }
        };

        for (var i = 0; i < addressBook.Count; i += 2)
        {
            Console.WriteLine($"Name: {addressBook[i].Name}, PostCode: {addressBook[i].PostCode}");
        }
    }
}

/* Sortie :
Name: Grant, PostCode: DV19 8EP
Name: Rebecca, PostCode: DV19 8EP
Name: Joe, PostCode: DV19 10E
*/
```

### **Ce qui se passe :**

* `i` commence à 0 et augmente de 2 (`i += 2`) à chaque itération.
    
* `addressBook[i]` accède désormais à un élément sur deux.
    
* Cela montre l'intérêt d'utiliser `i` comme index.
    

Jusqu'à présent, nous avons vu comment les boucles `for` permettent de contrôler les index et les pas d'itération.

Mais parfois, vous voulez simplement parcourir chaque élément d'une collection sans vous soucier des index. C'est là que la boucle `foreach` excelle.

## Comment utiliser une boucle ForEach en C#

Une boucle `foreach` itère sur n'importe quel objet qui hérite d' `IEnumerable` (listes, tableaux, collections). Elle accède automatiquement à chaque élément dans l'ordre, vous n'avez donc pas besoin d'index.

### Comment écrire une boucle ForEach

```csharp
var characters = new List<string>{"Batman", "CatWoman", "The Joker","Harley Quinn"};

foreach(var character in characters){
    Console.WriteLine(character);
}

/* Sortie :
Batman
CatWoman
The Joker
Harley Quinn
*/
```

**Points clés :**

* Pas besoin d'index.
    
* Fonctionne avec n'importe quelle collection énumérable.
    
* Code plus propre et plus expressif.
    

### Mises en garde de la boucle ForEach

#### Pas d'indexation

Vous ne pouvez pas accéder directement aux éléments avec `addressBook[i]` à l'intérieur d'un `foreach`. C'est parce que `foreach` fonctionne sur `IEnumerable`, qui n'expose pas d'index.

#### Performance

Une boucle `foreach` présente un léger surcoût par rapport à une boucle `for`. Dans la plupart des cas, cela n'aura pas d'importance, mais dans un code critique pour les performances, une boucle `for` peut être plus rapide.

#### Modification des éléments

`foreach` vous donne une copie de l'élément actuel, pas une référence directe. Cela signifie que vous ne pouvez pas réassigner de valeurs aux éléments de la liste à l'intérieur de la boucle.

* Vous pouvez lire les propriétés.
    
* Vous ne pouvez pas mettre à jour les éléments eux-mêmes (utilisez une boucle `for` pour cela).
    

`foreach` est idéal lorsque vous voulez visiter chaque élément, mais sans contrôler le nombre d'itérations.

## Comment utiliser une boucle Do..While en C#

Les boucles `do..while` exécutent le code au moins une fois, puis se répètent tant qu'une condition est vraie :

```csharp
int num;
do {
    Console.Write("Entrez un nombre positif : ");
    num = int.Parse(Console.ReadLine());
} while (num <= 0);

Console.WriteLine(num);
```

Le code ci-dessus demande la saisie d'un nombre dans l'application console si la condition est remplie. C'est-à-dire que si un nombre positif est fourni, le code n'en demandera pas d'autre et sortira de la boucle.

Si l'utilisateur entre un nombre négatif, la boucle continuera, demandant la saisie d'un nombre positif.

Et si vous ne vouliez pas que le code s'exécute au moins une fois, mais seulement si une condition est remplie ? C'est là que vous pouvez utiliser une boucle `while`.

## Comment utiliser une boucle While en C#

Les boucles `while` répètent le code tant qu'une condition est vraie, mais le corps de la boucle peut ne jamais s'exécuter si la condition est initialement fausse.

Prenons l'exemple d'un tableau de score de fléchettes :

```csharp
var sum = 0;
var dartsThrown = 0;
var random = new Random();

while (sum < 180 && dartsThrown < 3)
{
    var dartScore = random.Next(61); // 0–60
    sum += dartScore;
    dartsThrown++;
}

Console.WriteLine("Votre score est " + sum);
```

Tant que le joueur a des fléchettes à lancer, le code choisira un nombre au hasard et augmentera son score.

**Conseil :** Incluez toujours du code qui modifie la condition, sinon vous risquez de créer une boucle infinie. Une boucle infinie est une boucle qui ne s'arrête jamais et provoque le plantage de votre application.

Vous avez vu quatre façons différentes de répéter du code en C# : `for`, `foreach`, `do..while` et `while`. Résumons quand utiliser chacune d'elles.

## Dernières réflexions : choisir la bonne boucle

C# nous offre plusieurs types de boucles. Choisir la bonne rend votre code lisible, efficace et intentionnel.

* **Boucle For :** Utilisez-la lorsque vous savez combien de fois exécuter quelque chose, ou lorsque vous avez besoin d'un index, comme pour utiliser des tableaux ou sauter des éléments. Utilisez une boucle `for` lorsque vous avez besoin de plus de contrôle sur la nature itérative de la boucle.
    
* **Boucle ForEach :** Utilisez-la lorsque vous voulez parcourir chaque élément d'une collection sans vous soucier des index.
    
* **Boucle While :** Utilisez-la lorsque vous ne savez pas à l'avance combien de fois exécuter le code, mais qu'une condition guide la boucle.
    
* **Boucle Do..While :** Utilisez-la lorsque le corps de la boucle doit s'exécuter au moins une fois, par exemple pour une saisie utilisateur ou une logique de tentative (retry).
    

En adaptant le type de boucle à votre intention, votre code sera correct, lisible et maintenable.

J'espère que ce tutoriel vous a été utile. Comme toujours, j'aimerais connaître votre avis et en discuter davantage sur les réseaux sociaux. Vous pouvez me trouver sur [twitter/x](https://x.com/grantdotdev).