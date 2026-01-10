---
title: Comment utiliser les collections en C# - Listes, Tableaux, Dictionnaires et
  plus
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2025-01-24T14:51:58.961Z'
originalURL: https://freecodecamp.org/news/how-to-use-collections-in-csharp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1737729136643/4cc12d37-da1c-45f0-928f-fbe02d7fdf52.png
tags:
- name: C#
  slug: csharp
- name: Tutorial
  slug: tutorial
- name: beginner
  slug: beginner
seo_title: Comment utiliser les collections en C# - Listes, Tableaux, Dictionnaires
  et plus
seo_desc: One of the first challenges beginners face when developing applications
  in C# is organising and managing data efficiently. Imagine keeping track of a list
  of items, mapping unique keys to values, or ensuring there are no duplicates in
  a collection – ...
---

L'un des premiers défis auxquels les débutants sont confrontés lors du développement d'applications en C# est l'organisation et la gestion efficaces des données. Imaginez suivre une liste d'éléments, mapper des clés uniques à des valeurs ou garantir qu'il n'y a pas de doublons dans une collection - ce sont toutes des tâches courantes où le choix de la bonne structure de données peut faire une grande différence.

C# fournit un ensemble riche de structures de données intégrées, telles que les **listes**, les **dictionnaires** et plus encore, ce qui facilite le travail avec les données de différentes manières. Chaque structure a ses forces et est optimisée pour des scénarios spécifiques, donc comprendre leurs différences est la clé pour écrire un code propre, efficace et maintenable.

Dans ce tutoriel, nous explorerons :

* **Listes** : Votre solution pour les collections dynamiques et ordonnées où les éléments peuvent croître et décroître sans effort.

* **Tableaux** : Le choix efficace pour les collections de taille fixe avec une utilisation de mémoire prévisible et une indexation ultra-rapide.

* **Dictionnaires** : Parfaits pour les recherches rapides et la gestion des paires clé-valeur avec une vitesse et une clarté inégalées.

* **Piles** : Idéales pour les opérations dernier entré, premier sorti (LIFO), comme le suivi de l'historique ou des structures imbriquées.

* **Files d'attente** : Les meilleures pour les tâches premier entré, premier sorti (FIFO), comme le traitement de travaux ou la gestion de flux de travail séquentiels.

* **HashSets** : Le choix pour les collections où l'unicité compte et où les recherches rapides sont essentielles.

À la fin de ce guide, vous comprendrez les différences entre ces structures et serez équipé pour choisir la bonne pour votre prochain projet.

## Table des matières

1. [Tableaux en C#](#heading-tableaux)

2. [Listes en C#](#heading-listes)

3. [Dictionnaires en C#](#heading-dictionnaires)

4. [HashSets en C#](#heading-hashsets)

5. [Files d'attente en C#](#heading-filesdattente)

6. [Piles en C#](#heading-piles)

7. [Problèmes courants](#heading-problemescourants)

Pour certains des exemples suivants, vous aurez besoin de l'enregistrement `Animal` ci-dessous :

```csharp
public record Animal(int Age, string Name, int Legs, string Sound);
```

## Tableaux

Un **tableau** en C# est une collection de taille fixe d'éléments. Les tableaux sont indexés, et leur taille est définie lors de leur création, contrairement aux listes et autres collections. Une fois défini, la taille d'un tableau ne peut pas être modifiée, ce qui le rend efficace en mémoire avec une faible surcharge.

### Tableaux à une dimension

Les tableaux sont basés sur un index zéro, ce qui signifie que leur index commence à 0, plutôt qu'à 1. Si vous n'êtes pas familier, un index est un pointeur pour vous aider à trouver un élément.

Par exemple, si vous avez 5 noms dans un tableau, le premier nom est à l'index [0], et le dernier nom serait à l'index [4].

Les tableaux sont excellents dans les scénarios où les performances de bas niveau sont critiques, car ils ont très peu de surcharge en raison de leur manque de métadonnées (informations supplémentaires attachées).

```csharp
int[] numbers = new int[] { 1, 2, 3, 4, 5 };

foreach(var number in numbers){
    Console.Write(number);
}
//Sortie
// 1 2 3 4 5
```

Dans l'exemple ci-dessus, nous instancions un tableau avec ses valeurs (lui donnant ainsi une longueur fixe). Mais nous pouvons attribuer des valeurs après la création du tableau en utilisant l'assignation par index.

*Note : Vous devez toujours spécifier la taille du tableau au moment de la création, car le code doit connaître la taille fixe du tableau.*

```csharp
// créer un tableau vide de 20 index
var numbers = new int[20];

// boucler sur les index disponibles et assigner `i`
for (int i = 0; i < numbers.Length; i++)
{
    numbers[i] = i + 1;
}

foreach (var number in numbers)
{
    Console.Write($" {number}");
}
// Sortie
//  1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
```

### Tableaux multidimensionnels

Les tableaux peuvent également être multidimensionnels (par exemple, lignes et colonnes), ce qui signifie qu'ils peuvent contenir deux valeurs. Cela les rend parfaits pour construire des structures de type grille.

Contrairement à un tableau irrégulier, où chaque élément est un tableau qui peut avoir des longueurs différentes, un tableau multidimensionnel est une structure de type matrice où chaque dimension a une taille fixe.

```csharp
// Créer un tableau multidimensionnel 2D pour représenter un échiquier

string[,] chessBoard = new string[8, 8];

// Créer les positions de départ d'un échiquier
chessBoard[0, 0] = "Tour";
chessBoard[0, 1] = "Cavalier";
chessBoard[0, 2] = "Fou";
chessBoard[0, 3] = "Dame";
chessBoard[0, 4] = "Roi";
chessBoard[0, 5] = "Fou";
chessBoard[0, 6] = "Cavalier";
chessBoard[0, 7] = "Tour";

chessBoard[1, 0] = "Pion";
chessBoard[1, 1] = "Pion";
chessBoard[1, 2] = "Pion";
chessBoard[1, 3] = "Pion";
chessBoard[1, 4] = "Pion";
chessBoard[1, 5] = "Pion";
chessBoard[1, 6] = "Pion";
chessBoard[1, 7] = "Pion";

chessBoard[6, 0] = "Pion";
chessBoard[6, 1] = "Pion";
chessBoard[6, 2] = "Pion";
chessBoard[6, 3] = "Pion";
chessBoard[6, 4] = "Pion";
chessBoard[6, 5] = "Pion";
chessBoard[6, 6] = "Pion";
chessBoard[6, 7] = "Pion";

chessBoard[7, 0] = "Tour";
chessBoard[7, 1] = "Cavalier";
chessBoard[7, 2] = "Fou";
chessBoard[7, 3] = "Dame";
chessBoard[7, 4] = "Roi";
chessBoard[7, 5] = "Fou";
chessBoard[7, 6] = "Cavalier";
chessBoard[7, 7] = "Tour";


// Imprimer l'échiquier
for (int row = 0; row < 8; row++)
{
    for (int col = 0; col < 8; col++)
    {
        string piece = chessBoard[row, col] ?? "Vide";
        Console.Write($"{piece}\t");
    }
    Console.WriteLine();
}
```

**Sortie :**

```bash
Tour    Cavalier  Fou  Dame   Roi    Fou  Cavalier  Tour    
Pion    Pion    Pion    Pion    Pion    Pion    Pion    Pion    
Vide   Vide   Vide   Vide   Vide   Vide   Vide   Vide   
Vide   Vide   Vide   Vide   Vide   Vide   Vide   Vide   
Vide   Vide   Vide   Vide   Vide   Vide   Vide   Vide   
Vide   Vide   Vide   Vide   Vide   Vide   Vide   Vide   
Pion    Pion    Pion    Pion    Pion    Pion    Pion    Pion    
Tour    Cavalier  Fou  Dame   Roi    Fou  Cavalier  Tour  
```

### Tableau irrégulier

Bienvenue dans l'inception. Un **tableau irrégulier** en C# est un tableau de tableaux, où chaque tableau "interne" peut avoir une longueur différente.

Contrairement aux tableaux multidimensionnels, les tableaux irréguliers ne sont pas rectangulaires, ce qui signifie que les lignes peuvent avoir des tailles variables.

Un exemple d'utilisation pourrait être la construction d'une application de calendrier. Ci-dessous, un exemple de base affichant les jours de chaque mois de l'année :

```csharp
int[][] daysInMonths = new int[12][];

// Initialiser chaque mois avec son nombre correspondant de jours
daysInMonths[0] = new int[31]; // Janvier
daysInMonths[1] = new int[28]; // Février (année non bissextile)
daysInMonths[2] = new int[31]; // Mars
daysInMonths[3] = new int[30]; // Avril
daysInMonths[4] = new int[31]; // Mai
daysInMonths[5] = new int[30]; // Juin
daysInMonths[6] = new int[31]; // Juillet
daysInMonths[7] = new int[31]; // Août
daysInMonths[8] = new int[30]; // Septembre
daysInMonths[9] = new int[31]; // Octobre
daysInMonths[10] = new int[30]; // Novembre
daysInMonths[11] = new int[31]; // Décembre

// Imprimer le nombre de jours dans chaque mois
for (int month = 0; month < daysInMonths.Length; month++)
{
    Console.WriteLine($"Mois {month + 1}: {daysInMonths[month].Length} jours");
}
```

Vous devriez utiliser un `Array` dans :

* **Applications critiques en performance** où la surcharge mémoire et la vitesse comptent.

* **Ensembles de données fixes** où la taille ne changera pas.

* **Données multidimensionnelles**, par exemple, les coordonnées de graphique (x, y)

## Listes

Une `List<T>` en C# est une collection redimensionnable d'éléments du même type, signalée ci-dessus par la lettre `T`. Elle permet d'ajouter, de supprimer et d'accéder aux éléments par index. Contrairement aux tableaux, les listes croissent dynamiquement selon les besoins.

Communément utilisées pour les données séquentielles, elles supportent les requêtes [LINQ](https://www.freecodecamp.org/news/how-to-use-linq/) et diverses méthodes utilitaires pour la manipulation de données.

```csharp
var animals = new List<Animal>()
{
    new Animal(10, "Dog", 4, "Woof"),
    new Animal(5, "Cat", 4, "Meow"),
    new Animal(2, "Lion", 4, "Roar"),
    new Animal(6, "Giraffe", 4, "Trumpet"),
    new Animal(15, "Red-Panda", 4, "Squeak")    
};

animals.Add(new Animal(2, "Hamster",4,"Squeak"));
animals.Remove(x=>x.Sound == "Meow"); // Supprimer tous les animaux qui miaulent
```

Les listes sont une structure de données très polyvalente, où l'ordre des éléments reste le même ordre dans lequel ils sont ajoutés ou supprimés (pas de manipulation. Par exemple, chaque fois que vous appelez la méthode `.Add()` sur une liste, elle ajoutera l'élément à la liste, et l'ordre reste le même qu'avant mais avec l'animal supplémentaire.

Vous pouvez modifier les données (par exemple, filtrer, mapper ou trier) avant d'envoyer les listes à d'autres parties de votre application grâce aux nombreuses méthodes utilitaires disponibles dans la classe `List<T>`.

## Dictionnaires

Les dictionnaires fonctionnent exactement comme le terme que nous connaissons dans la langue anglaise.

Nous avons une clé (un terme de recherche) et une valeur (l'objet ou la donnée mappée). Pour cette raison, vous pourriez entendre le terme 'paire clé-valeur' lorsque l'on fait référence aux dictionnaires.

Les dictionnaires sont mieux utilisés pour récupérer efficacement des données basées sur un identifiant unique, tel qu'un ID, un nom ou d'autres champs identifiants uniques. Ils garantissent que leurs clés uniques sont idéales pour les scénarios nécessitant des performances optimales sans recherche itérative.

Je recommande d'utiliser les dictionnaires lorsque l'ordre des éléments est sans importance et que vous devez représenter des relations, telles que la cartographie des pays aux capitales, des produits aux prix, ou des personnes aux adresses.

```csharp
var animalDictionary = new Dictionary<string, Animal>()
{
    { "Dog", new Animal(10, "Dog", 4, "Woof") },
    { "Cat", new Animal(5, "Cat", 4, "Meow") },
    { "Elephant", new Animal(8, "Elephant", 4, "Trumpet") },
    { "Lion", new Animal(2, "Lion", 4, "Roar") },
    { "Giraffe", new Animal(6, "Giraffe", 4, "Trumpet") },
};
// Ajouter
animalDictionary.Add("Red panda", new Animal(2, "Red Panda", 4, "Squeaker"));

// Supprimer
animalDictionary.Remove("Cat");

// Obtenir
var giraffe = animalDictionary["Giraffe"];
```

## HashSets

Un `HashSet<T>` est une collection en C# qui stocke des éléments uniques. Il utilise une implémentation basée sur le hachage pour garantir des recherches, des ajouts et des suppressions très efficaces. Cela signifie qu'il utilise des fonctions de hachage pour mapper rapidement les clés aux valeurs, vous pouvez en lire plus à ce sujet ici.

Les éléments en double sont automatiquement ignorés.

En quoi cela diffère-t-il d'un Dictionnaire ? Les HashSets n'ont pas de clés comme les Dictionnaires. Au lieu de cela, ils stockent les valeurs directement et sont accessibles en itérant sur les éléments à l'aide d'une boucle `foreach` ou de requêtes LINQ.

```csharp
var animalHashSet = new HashSet<Animal>()
{
    new Animal(3, "Lion", 4, "Roar"),
    new Animal(5, "Tiger", 4, "Roar"),
    new Animal(2, "Elephant", 4, "Trumpet"),
    new Animal(1, "Giraffe", 4, "Neigh")
};
// Ajouter
animalHashSet.Add(new Animal(3, "Lion", 4, "Roar"));
// Supprimer
animalHashSet.Remove(x=>x.Sound == "Neigh");
// Obtenir
animalHashSet.FirstOrDefault(x=>x.Name == "Elephant");
```

Ci-dessus, nous créons un `HashSet<Animal>` et tentons d'ajouter un objet en double. Vous pourriez vous attendre à ce que cela génère une erreur, car nous savons que les HashSets ne peuvent stocker que des valeurs uniques. Mais au lieu de cela, il gère cela assez élégamment et n'ajoute simplement pas l'objet en double, donc la sortie est :

```bash
Animal { Age = 3, Name = Lion, Legs = 4, Sound = Roar }
Animal { Age = 5, Name = Tiger, Legs = 4, Sound = Roar }
Animal { Age = 2, Name = Elephant, Legs = 4, Sound = Trumpet }
```

## Files d'attente

Les files d'attente fonctionnent exactement de la même manière qu'une file d'attente dans la vie quotidienne, avec une approche premier entré, premier sorti.

`Queue<T>` n'implémente pas l'interface ICollection comme les Dictionnaires et les Listes, ce qui signifie qu'il n'a pas de méthode **Add()**. Cela signifie que vous ne pouvez pas ajouter d'éléments à la file d'attente lors de l'instanciation. Cela signifie également que vous ne pouvez pas utiliser la méthode **Add()** pour ajouter des éléments - à la place, vous utilisez la méthode **Enqueue()**.

```csharp
var arc = new Queue<string>();
arc.Enqueue("2 Lions");
arc.Enqueue("2 Tigers");
arc.Enqueue("2 Bears");

// La méthode Peek permet de regarder le début de la file d'attente
Console.WriteLine("Début de la file d'attente : " + arc.Peek());

// Sortie
// Début de la file d'attente : 2 Lions

Console.WriteLine($"Traitement : {arc.Dequeue()}"); // Sortie : 2 Lions
Console.WriteLine($"Traitement : {arc.Dequeue()}"); // Sortie : 2 Tigers
```

La méthode `Dequeue` non seulement retourne l'élément suivant dans la file d'attente, mais supprime également l'élément de la file d'attente comme prévu. Vous pouvez également vider la file d'attente en utilisant la méthode `Clear()`.

## Piles

Les piles fonctionnent à l'opposé de `Queue<T>`, en ce sens qu'au lieu de premier entré, premier sorti, elles fonctionnent sur un mécanisme dernier entré, premier sorti.

```csharp
var stack = new Stack<int>();
stack.Push(1);
stack.Push(2);
stack.Push(3);
stack.Push(4);
stack.Push(5);

// itérer sur la pile
foreach(var number in stack )
{
    Console.WriteLine(number);
}

// Sortie
// 5 4 3 2 1

```

Vous pourriez penser que parcourir les éléments dans une `Stack` fonctionnerait de la même manière qu'une Liste ou une File d'attente et les imprimerait toujours dans l'ordre d'entrée. Mais le système sait qu'il s'agit d'une pile, et il énumère donc les éléments dans l'ordre inverse de leur ajout - c'est-à-dire que l'élément le plus récemment ajouté (`5`) est retourné en premier.

Vous pouvez également utiliser la méthode `Pop()` qui retournera le dernier élément de la collection et le supprimera en même temps.

## Problèmes courants

Lors de l'utilisation de diverses collections, vous rencontrerez probablement des problèmes courants, tels que `KeyNotFoundException` lors de l'utilisation de dictionnaires, `IndexOutOfRangeException` sur les listes/tableaux, ou `InvalidOperationException` lors de la modification d'une collection pendant l'itération.

### `KeyNotFoundException`

**Scénario :** Vous essayez d'accéder à une clé de dictionnaire qui n'existe pas dans le dictionnaire. Cela entraînera une `KeyNotFoundException`, et une erreur.

```csharp
var dictionary = new Dictionary<string, string>()
{
    { "Morning", "Good Morning" },
    { "Afternoon", "Good afternoon" },
    { "Evening", "Good evening" },
    { "Night", "Good night" },
};

var message = dictionary["Dusk"];

Console.WriteLine(message);

// Sortie
//Unhandled exception. System.Collections.Generic.KeyNotFoundException: The given key 'Dusk' was not present in the dictionary.
```

**Solution :** Je recommande d'utiliser la fonction `TryGetValue`, qui gérera cela élégamment et retournera l'élément en tant que paramètre `out` (s'il peut être trouvé, sinon la valeur par défaut).

`TryGetValue` retourne un booléen pour indiquer s'il a pu ou non trouver la clé fournie. Cette valeur booléenne peut ensuite être utilisée pour déterminer la fonctionnalité basée sur une récupération réussie ou non, plutôt que de vérifier le paramètre de sortie, par exemple (s'il est null/vide ou non).

```csharp
var dictionary = new Dictionary<string, string>()
{
    { "Morning", "Good Morning" },
    { "Afternoon", "Good afternoon" },
    { "Evening", "Good evening" },
    { "Night", "Good night" },
};

var input = Console.ReadLine(); // Dusk

dictionary.TryGetValue(input, out var message);
Console.WriteLine($"`Message:{message}`");
// Ouput = `Message ` (message vide car la valeur par défaut de la chaîne est une chaîne vide

//ou vérifier si la récupération a été possible et accéder à la sortie si c'était le cas
if(dictionary.TryGetValue(input,out var m)){
    Console.WriteLine(message);
}
```

### `IndexOutOfRangeException` (Listes/Tableaux) :

**Scénario** : Essayer d'accéder à un index qui est en dehors de la plage valide d'une liste ou d'un tableau.

Comme nous le savons, les tableaux sont basés sur un index zéro, donc essayer d'accéder à un index de [5] sur un tableau de 5 éléments lancera une `IndexOutOfRangeException`.

**Solutions** :

1. Assurez-vous que l'index est dans les limites en utilisant `list.Count` ou `array.Length` avant l'accès.

2. Utilisez la méthode `ElementAtOrDefault()`. Si elle ne peut pas accéder à un élément à l'index donné, elle retournera la valeur par défaut, qui peut ensuite être gérée en conséquence.

```csharp
var names = new string[]
{
    "Tony", "Clint", "Bob", "Alice", "Lisa"
};

var name = names.ElementAtOrDefault(6);
Console.WriteLine(name ?? "Nom non trouvé.");
```

### `InvalidOperationException` (Itération des Collections) :

**Scénario** : Modifier une collection (par exemple, ajouter ou supprimer des éléments) tout en itérant dessus avec une boucle `foreach` lancera une `InvalidOperationException` car vous essayez de supprimer un élément de la liste tout en itérant dessus avec une boucle `foreach`.

```csharp
var myList = new List<string> { "Apple", "Banana", "Cherry", "Banana" };

foreach (var item in myList)
{
    if (item == "Banana")
    {
        myList.Remove(item); // Lance InvalidOperationException
    }
}
```

#### **Pourquoi cela arrive-t-il :**

* La boucle `foreach` maintient un énumérateur interne pour la collection.

* Modifier la collection (par exemple, ajouter/supprimer des éléments) invalide l'énumérateur, ce qui fait que le runtime lance une `InvalidOperationException`.

**Solution 1 : Utiliser une boucle `for`**

Vous pouvez utiliser une boucle `for` avec un index pour modifier la liste en toute sécurité pendant l'itération :

```csharp
var fruits = new List<string> { "Apple", "Banana", "Cherry", "Banana" };

for (int i = 0; i < fruits.Count; i++)
{
    if (fruits[i] == "Banana")
    {
        fruits.RemoveAt(i);
        // Ajuster l'index pour tenir compte de l'élément supprimé
        i--; 
    }
}
Console.WriteLine(string.Join(", ", fruits)); 
// Sortie : Apple, Cherry
```

**Solution 2 : Itérer sur une copie**

Une autre approche consiste à itérer sur une copie de la liste en utilisant `ToList()`. Ainsi, vous n'itérez pas directement sur la collection originale, donc les modifications n'affecteront pas la boucle.

```csharp
var originalList = new List<string> { "Apple", "Banana", "Cherry", "Banana" };

foreach (var item in originalList.ToList()) // Créer une copie
{
    if (item == "Banana")
    {
        originalList.Remove(item); // Suppression sécurisée
    }
}
Console.WriteLine(string.Join(", ", originalList)); 
// Sortie : Apple, Cherry
```

**Solution 3 : Utiliser LINQ pour filtrer**

Si vous souhaitez uniquement supprimer des éléments en fonction d'une condition, vous pouvez utiliser LINQ pour créer une nouvelle liste filtrée :

```csharp
var fruits = new List<string> { "Apple", "Banana", "Cherry", "Banana" };

fruits = fruits.Where(item => item != "Banana").ToList(); // Filtrer "Banana"

Console.WriteLine(string.Join(", ", fruits)); 
// Sortie : Apple, Cherry
```

## Réflexions finales

Dans cet article, vous avez appris de nombreuses structures de données courantes pour stocker plusieurs objets et valeurs.

Que vous stockiez des données dans un tableau de taille fixe, gériez une liste dynamique, travailliez avec des files d'attente premier entré, premier sorti, des piles dernier entré, premier sorti, ou des dictionnaires de paires clé-valeur, savoir quand et comment utiliser chaque collection est la clé pour devenir un développeur C# confiant et compétent.

Maîtriser ces concepts améliorera non seulement votre capacité à gérer les données efficacement, mais posera également les bases pour des sujets plus avancés en structures de données et algorithmes. Combiner ces structures de données avec LINQ peut fournir des mécanismes performants et faciles à utiliser. Pour en savoir plus sur LINQ, vous pouvez consulter mon article [ici](https://www.freecodecamp.org/news/how-to-use-linq/).

Alors que vous continuez votre parcours de codage, continuez à expérimenter avec ces collections, appliquez-les dans des scénarios réels et approfondissez votre compréhension de leur fonctionnement interne.

Comme toujours, si vous souhaitez discuter davantage de cet article, d'autres problèmes liés au codage, ou entendre parler d'autres articles que j'écris, suivez-moi sur [X(Twitter)](https://x.com/grantdotdev)

Bon codage ! 😊