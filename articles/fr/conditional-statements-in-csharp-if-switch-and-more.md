---
title: 'Comment utiliser les instructions conditionnelles en C# : If, Switch et plus
  expliqués avec des exemples de code'
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-10-21T18:27:32.145Z'
originalURL: https://freecodecamp.org/news/conditional-statements-in-csharp-if-switch-and-more
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729432206658/e802fcca-bf0c-424f-9915-b02fd847bdcc.png
tags:
- name: Conditionals
  slug: conditionals
- name: C#
  slug: csharp
- name: Tutorial
  slug: tutorial
seo_title: 'Comment utiliser les instructions conditionnelles en C# : If, Switch et
  plus expliqués avec des exemples de code'
seo_desc: 'Being able to update variables, call particular branches of code, or simply
  output different code based on a certain condition is a vital part of programming
  in any language.

  C# (C Sharp) offers multiple ways to do these things, and I’m about to show...'
---

Pouvoir mettre à jour des variables, appeler des branches spécifiques de code ou simplement produire un code différent en fonction d'une certaine condition est une partie vitale de la programmation dans n'importe quel langage.

C# (C Sharp) offre plusieurs façons de faire ces choses, et je vais vous montrer certaines des plus courantes. Nous discuterons des avantages et des inconvénients de chaque méthode, et lesquelles sont plus adaptées à des scénarios particuliers.

## Table des matières

* [Ce que vous apprendrez dans cet article](#heading-ce-que-vous-apprendrez-dans-cet-article)
    
* [Instructions If / Else if / Else](#heading-instructions-if-else-if-else)
    
* [Remplacer If / Else par l'opérateur ternaire](#heading-remplacer-if-else-par-loperateur-ternaire)
    
* [Instructions Switch Case](#heading-instructions-switch-case)
    
* [Instructions Switch - Syntaxe d'expression](#heading-instructions-switch-syntaxe-dexpression)
    
* [Résumé des performances](#heading-resume-des-performances)
    
* [Conclusion](#heading-conclusion)
    

## Ce que vous apprendrez dans cet article

Je vais vous enseigner tout sur les mécanismes de codage conditionnel suivants dans C#.

* Instructions If / Else If / Else
    
* Instructions ternaires
    
* Instructions Switch-Case
    
* Analyse des performances des options de codage conditionnel
    

**Prérequis :**

* Connaissance très basique du langage de codage C#
    
* IDE de codage (pour coder en même temps si vous le souhaitez)
    

## Instructions If / Else if / Else

Lors de l'apprentissage d'un nouveau langage de programmation, l'instruction `If` est un élément de base dans le programme d'apprentissage de tout développeur. C'est le moyen le plus simple de diriger conditionnellement le flux d'exécution de votre code.

Examinons comment construire la complexité de la syntaxe de l'instruction `If`. Dans sa forme la plus basique, vous pouvez l'utiliser comme une simple clause `if`, ce qui signifie que le code à l'intérieur du bloc `if` ne sera exécuté que si une condition est remplie.

**Exemple :**

```csharp
// Pour la démonstration, nous utilisons un âge codé en dur.
int age = 22;

// vérifier si la personne est en âge légal au Royaume-Uni
if (!string.IsNullOrEmpty(age) && age >= 18)
{
   // Si vrai, exécuter le code suivant
   AllowAccessToNightClub();
}
```

Allant un peu plus loin, si nous voulions exécuter un certain code lorsque l'instruction résulte en `false`, nous pouvons le faire en utilisant une instruction `if / else` comme suit :

```csharp
var ageLimit = 18;
var customersAge = 17

if(customersAge >= ageLimit){
{   
    AllowAccessToTheClub();
} else{
    // Refuser l'accès
    DenyAccess();
    // nous pouvons aussi imbriquer les instructions if
    // si le client ne part pas, appelez la police !
    if(!CustomerLeaves()){
        CallThePolice();
    };
}

```

L'exemple ci-dessus illustre comment vous pouvez utiliser les instructions `if / else` pour contrôler le flux de votre code. Vous avez vu comment vous pouvez gérer des scénarios spécifiques avec des instructions imbriquées, vous permettant de vérifier les résultats futurs.

Dans le code ci-dessus, nous vérifions si `CustomerLeaves()` retourne une valeur vraie ou fausse, et selon le résultat, nous voyons si nous devons `CallThePolice()` ou non.

Pour les situations où vous souhaitez vérifier plus d'une condition avant de passer à `else`, vous pouvez utiliser la syntaxe `if / else if / else`. Voyons comment cela fonctionne :

```csharp
int age = 17;

if(age >= 18){
    Console.WriteLine("Vous pouvez boire de l'alcool au Royaume-Uni");
    Console.WriteLine("Vous pouvez voter au Royaume-Uni");
    Console.WriteLine("Vous pouvez vous faire tatouer");
} else if(age >= 16 && age < 18){
    Console.WriteLine("Vous pouvez rejoindre les forces royales au Royaume-Uni");
} else{
   Console.WriteLine("Restez à l'école !");
}
```

L'exemple ci-dessus utilise `if / else if / else` pour afficher différents textes en fonction de la condition remplie. Un seul bloc sera jamais exécuté, car vous ne pouvez correspondre qu'à une seule condition avec cette syntaxe.

Supposons que vous souhaitiez construire une chaîne basée sur plusieurs conditions, mais que vous souhaitiez que toutes les conditions soient vérifiées individuellement. Dans ce cas, vous pourriez utiliser plusieurs `if statements` pour accomplir cela. Soyez cependant conscient que cela peut rendre votre code moins performant et plus difficile à lire.

```csharp
using System.Text;

int age = 20;
bool hasDrivingLicense = true;
bool hasVoterID = false;

var builder = new StringBuilder();

// Plusieurs instructions if indépendantes
if (age >= 18)
{
    builder.Append("Vous êtes un adulte.");
}

if (hasDrivingLicense)
{
    builder.Append("Vous pouvez conduire.");
}

if (hasVoterID)
{
    builder.Append("Vous êtes éligible pour voter.");
}

Console.WriteLine(builder.ToString());
Console.WriteLine(builder.ToString());
/* Sortie
Vous êtes un adulte.Vous pouvez conduire.
*/
```

Le code ci-dessus démontre l'utilisation de plusieurs instructions `if` au lieu de `if`, `else if`, `else`. Cela permet de vérifier plusieurs conditions indépendamment, donc plusieurs blocs de code peuvent s'exécuter si les conditions sont remplies. Cela est utile lorsque vous souhaitez assigner des valeurs aux propriétés d'un objet en fonction de différents critères ou conditions indépendantes.

## Remplacer If / Else par l'opérateur ternaire

Les instructions `If / Else` sont très utiles, mais parfois elles peuvent prendre beaucoup de place pour un code d'assignation vraiment simple. L'**opérateur ternaire** est parfait pour ces situations. Sa syntaxe utilise `?` et `:` pour représenter ce qui se passe si la condition est vraie ou fausse, éliminant le besoin de crochets.

Voici un exemple :

```csharp
var backgroundColor = isDarkMode ? "black" : "white";
```

**Explication :**

* `backgroundColor` : La variable à laquelle on assigne une valeur.
    
* `isDarkMode` : Une condition booléenne évaluée.
    
* `?` : Marque le début de l'opérateur ternaire. Si `isDarkMode` est `true`, la valeur après `?` ("black") est assignée.
    
* `:` : Sépare le cas vrai du cas faux. Si `isDarkMode` est `false`, la valeur après `:` ("white") est assignée.
    

L'instruction ternaire est une abréviation pour les assignations conditionnelles simples, rendant votre code plus compact. Je recommande de l'utiliser pour les assignations de variables simples ou les appels binaires simples de fonctions (comme appeler A ou appeler B).

Voici un exemple :

```csharp
isLoggedIn ? ShowWelcomeMessage() : PromptLogin();

void ShowWelcomeMessage()
{
    Console.WriteLine("Bienvenue, utilisateur !");
}

void PromptLogin()
{
    Console.WriteLine("Veuillez vous connecter pour continuer.");
}
```

Les opérations ternaires peuvent également être imbriquées comme suit :

```csharp
var isDarkMode = true;
var isAccessibilityActive = true;

var backgroundColor = isDarkMode ? isAccessibilityActive ? "green" : "black" : "white";

Console.WriteLine(backgroundColor);
```

L'exemple ci-dessus utilise des opérateurs ternaires imbriqués pour remplacer une instruction if / else imbriquée. Gardez simplement à l'esprit que le flux est différent d'une opération ternaire régulière. Cela se lirait comme suit :

```csharp
SI isDarkMode est vrai, alors vérifier si isAccessibilityActive est vrai

SI isAccessibility est vrai, définir la valeur sur "green" sinon retourner "black"

SI isDarkMode est faux, il ignorera les vérifications internes et retournera "white" ;
```

J'éviterais d'utiliser des opérateurs ternaires imbriqués lorsque c'est possible, car ils sont désordonnés et peuvent être difficiles à lire.

## Instructions Switch Case

Les instructions switch case fonctionnent en testant une variable (*switch*) contre plusieurs possibilités (*case*).

```csharp
string userRole = "Admin";

// vérifier le rôle de l'utilisateur contre les critères suivants.
switch (userRole)
{
    case "Admin":
        Console.WriteLine("Vous avez un accès complet.");
        break;
    case "Moderator":
        Console.WriteLine("Vous pouvez modérer le contenu.");
        break;
    case "User":
        Console.WriteLine("Vous avez un accès limité.");
        break;
    default:
        Console.WriteLine("Rôle non reconnu.");
        break;
}
```

**Note :** *la valeur et le type de la variable évaluée doivent correspondre.* Par exemple, vous ne pouvez pas comparer une chaîne avec un entier (sans conversion / analyse préalable)*.* Si aucun des cas ne correspond, le bloc `default` est exécuté, similaire à `else` dans une structure `if/else`, généralement utilisé pour un cas de repli.

### Pourquoi utiliser Switch-Case plutôt que l'instruction If ?

**Lisibilité** : Lorsque vous gérez **plusieurs valeurs distinctes** (comme des rôles, des commandes ou des types enum), `switch` est plus facile à lire et à maintenir car il organise les conditions plus clairement, sans plusieurs blocs `if` et `else if`.

**Performance** : Dans certains cas, les instructions **switch** peuvent être plus efficaces que plusieurs blocs `if / else if`, surtout lorsqu'on traite avec plusieurs valeurs possibles d'une seule variable. Certains compilateurs optimisent les instructions `switch` en tables de recherche, améliorant ainsi les performances.

**Évolutivité** : Lorsque vous gérez une longue liste d'options ou de conditions distinctes, un `switch` case s'adapte mieux. L'ajout de nouveaux cas est plus simple et ne nécessite pas de mettre à jour de longues chaînes de `if / else if`.

**Defaults propres** : Le cas `default` fournit un moyen clair de gérer les scénarios non reconnus ou inattendus, similaire au bloc `else` dans une instruction `if / else if`, mais il semble plus naturellement intégré à la structure `switch`. Cela peut être utile pour lancer des exceptions, journaliser, etc.

### Instructions Switch - Syntaxe d'expression

Il arrive que vous ayez besoin de conditions légèrement plus complexes à évaluer tout en souhaitant toujours utiliser la syntaxe `switch`. Dans ce scénario, vous pouvez utiliser la syntaxe `switch expression` qui a été introduite dans C# 8.

```csharp
string userType = "VIP";
decimal purchaseAmount = 500m;

decimal discount = userType switch
{
    "Regular" when purchaseAmount < 100 => 0.05m,  
    "Regular" => 0.10m,  
    "VIP" when purchaseAmount < 500 => 0.15m,  
    "VIP" => 0.20m,  
    "Employee" => 0.25m,  
    _ => 0m 
};

Console.WriteLine($"Votre remise est de : {discount * 100}%");
```

Cette syntaxe est idéale lorsque vous devez assigner une valeur au résultat du cas.

* `userType switch { ... }` : une **expression switch** qui retourne une valeur (dans ce cas, la remise) basée sur le `userType` et des conditions optionnelles (comme `purchaseAmount`).
    
* La clause `when` permet des conditions plus complexes, comme vérifier le `purchaseAmount` en plus du `userType` pour modifier le montant de la remise.
    

**Cas par défaut / Repli**

Le cas par défaut dans cette syntaxe utilise le caractère `_`. Dans notre exemple, si aucun des cas ci-dessus n'est rempli, le cas par défaut est rempli et nous retournons `0m` (pas de remise).

### Avantages des expressions Switch par rapport aux instructions `switch` conventionnelles :

**Concis et lisible** : L'expression switch est plus **compacte** et **lisible**, surtout lorsqu'elle retourne des valeurs directement basées sur des conditions, sans avoir besoin de déclarer des variables ou d'utiliser des instructions `break`.

**Correspondance de motifs** : Elle supporte la **correspondance de motifs** (`when`), ce qui facilite l'ajout de conditions complexes à chaque cas, quelque chose qui nécessiterait des vérifications `if` plus verbeuses dans une instruction switch traditionnelle.

**Retourne une valeur** : L'expression switch est une **expression** qui retourne directement une valeur, ce qui la rend idéale pour les assignations ou l'utilisation en ligne, réduisant le code répétitif. Ci-dessous, vous trouverez un exemple utilisant une expression switch comme valeur de retour dans une méthode sans l'assigner à une variable.

**Simplifie la logique complexe** : Elle est excellente pour des scénarios comme celui-ci, où plusieurs conditions affectent le résultat, les traitant de manière concise sans blocs `if / else if` profondément imbriqués.

```csharp
decimal CalculateDiscount(string userType, decimal purchaseAmount) =>
    userType switch
    {
        "Regular" when purchaseAmount < 100 => 0.05m,
        "Regular" => 0.10m,
        "VIP" when purchaseAmount < 500 => 0.15m,
        "VIP" => 0.20m,
        "Employee" => 0.25m,
        _ => 0m
    };

// Utilisation
decimal discount = CalculateDiscount("VIP", 500m);
Console.WriteLine($"Votre remise est de : {discount * 100}%");
```

## Résumé des performances

Pour vous aider à décider, voici un projet de benchmarking rapide (utilisant le package BenchmarkDotNet, que vous pouvez installer avec `dotnet add package BenchmarkDotnet`) :

```csharp
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Order;
using System.Collections.Generic;

namespace Csharp_Console_Playground
{
    [MemoryDiagnoser]
    [Orderer(SummaryOrderPolicy.FastestToSlowest)]
    public class BenchMarkRunner
    {
        private static readonly Dictionary<int, string> RankingMessages = new()
        {
            { 0, "Do not stay in this hotel" },
            { 1, "It's cheap and cheerful" },
            { 2, "It's clean and tidy" },
            { 3, "In the middle hotel, good service and great amenities" },
            { 4, "It's a nice hotel, but the price is not too high" },
            { 5, "It's the best hotel in the area" }
        };

        private int ranking = 5;

        [Benchmark]
        public string BenchMarkIfElse()
        {
            var winningMessage = "";

            if (ranking == 0)
            {
                winningMessage = "Do not stay in this hotel";
            }
            else if (ranking == 1)
            {
                winningMessage = "It's cheap and cheerful";
            }
            else if (ranking == 2)
            {
                winningMessage = "It's clean and tidy";
            }
            else if (ranking == 3)
            {
                winningMessage = "In the middle hotel, good service and great amenities";
            }
            else if (ranking == 4)
            {
                winningMessage = "It's a nice hotel, but the price is not too high";
            }
            else if (ranking == 5)
            {
                winningMessage = "It's the best hotel in the area";
            }

            return winningMessage;
        }

        [Benchmark]
        public string BenchMarkSwitchCaseExpression()
        {
            var winningMessage = ranking switch
            {
                0 => "Do not stay in this hotel",
                1 => "It's cheap and cheerful",
                2 => "It's clean and tidy",
                3 => "In the middle hotel, good service and great amenities",
                4 => "It's a nice hotel, but the price is not too high",
                5 => "It's the best hotel in the area",
                _ => ""
            };

            return winningMessage;
        }

        [Benchmark]
        public string BenchMarkSwitchCase()
        {
            var winningMessage = "";
            switch (ranking)
            {
                case 0:
                    winningMessage = "Do not stay in this hotel";
                    break;
                case 1:
                    winningMessage = "It's cheap and cheerful";
                    break;
                case 2:
                    winningMessage = "It's clean and tidy";
                    break;
                case 3:
                    winningMessage = "In the middle hotel, good service and great amenities";
                    break;
                case 4:
                    winningMessage = "It's a nice hotel, but the price is not too high";
                    break;
                case 5:
                    winningMessage = "It's the best hotel in the area";
                    break;
                default:
                    winningMessage = "Invalid ranking";
                    break;
            }

            return winningMessage;
        }

        [Benchmark]
        public string? BenchMarkDictionary()
        {
            return RankingMessages.TryGetValue(ranking, out var rankingMessage) ? rankingMessage : null;
        }
    }
}
```

Vous pouvez ensuite exécuter ces tests dans votre `Program.cs` :

```csharp
using BenchmarkDotNet.Running;
using Csharp_Console_Playground;

BenchmarkRunner.Run<BenchMarkRunner>();
```

Assurez-vous d'utiliser votre profil de build `Release` afin d'exécuter les benchmarks.

```csharp
 dotnet build -c Release
```

puis exécutez `dotnet` sur votre emplacement de build, par exemple :

```csharp
dotnet bin/Release/net8.0/FCC-Conditions.dll
```

**Résultats :**

| **Méthode** | **Moyenne (temps d'exécution - [nano secondes](https://en.wikipedia.org/wiki/Nanosecond))** |
| --- | --- |
| BenchMarkSwitchCaseExpression | 0.0000 ns |
| BenchMarkSwitchCase | 0.0003 ns |
| BenchMarkIfElse | 0.3628 ns |
| BenchMarkDictionary | 2.6356 ns |

Les instructions `switch` peuvent être plus rapides que les dictionnaires car le compilateur aide à les optimiser. Lorsque le compilateur voit un `switch`, il peut créer une table de recherche spéciale (table de saut, ou arbre de recherche binaire) qui lui permet de trouver le bon cas rapidement, surtout lorsque les cas sont proches les uns des autres (comme les nombres 1, 2 et 3). Cela signifie qu'il peut vérifier la valeur presque instantanément.

La raison pour laquelle le dictionnaire est le plus lent est due à l'allocation de mémoire. Dans notre test de benchmark, nous avons dû créer une variable en mémoire pour que le dictionnaire soit créé et stocké (ce qui prend du temps), et la récupération doit également être effectuée lors de la recherche.

#### **Expressions Switch-Case :**

**Optimisation à la compilation** : Les cas switch sont généralement optimisés à la **compilation** (lorsque vous construisez votre code). Le compilateur analyse les valeurs possibles des cas et génère un code machine efficace pour les gérer. Selon les cas, cela pourrait être via des tables de saut, ou des mécanismes de branchement / recherche binaire.

Puisque tout cela est fait pendant la **compilation**, l'instruction switch n'a pas de surcharge supplémentaire à l'exécution au-delà de ce que le compilateur a mis en place.

#### **Dictionnaires :**

**Construction à l'exécution** : En revanche, un dictionnaire (par exemple, `Dictionary<TKey, TValue>` en C#) est construit à l'**exécution**. Le dictionnaire utilise une **table de hachage** sous le capot, où les clés sont hachées pour générer un index qui mappe à une valeur. Voici la différence clé :

* **Fonction de hachage** : Lorsque vous ajoutez une clé à un dictionnaire, la fonction de hachage est appliquée à la clé pour déterminer où la valeur doit être stockée.
    
* **Gestion des collisions** : Si deux clés ont le même hachage (une "collision"), le dictionnaire doit la résoudre (généralement par chaînage ou sondage), ce qui peut introduire une surcharge supplémentaire.
    

Puisque les dictionnaires sont construits et modifiés à l'exécution, ils doivent effectuer ces opérations dynamiquement, ce qui ajoute plus de surcharge par rapport à la structure statique des cas switch.

## Conclusion

Comprendre comment contrôler le flux de votre code grâce à la logique conditionnelle est une compétence fondamentale en programmation, et C# offre divers outils pour y parvenir. Que vous utilisiez des instructions `if/else` pour des conditions simples, l'opérateur ternaire pour des assignations concises, ou des instructions switch pour une logique complexe, chaque approche a ses forces et ses cas d'utilisation idéaux.

Les instructions switch offrent une clarté et des optimisations de performance, surtout lorsqu'on traite avec plusieurs conditions. D'un autre côté, les dictionnaires offrent de la flexibilité mais viennent avec une surcharge à l'exécution. Savoir quand utiliser chaque méthode vous permet d'écrire un code plus efficace, lisible et maintenable, adapté à des scénarios spécifiques.

Comme toujours, si vous souhaitez discuter de l'un de mes articles, vous pouvez me suivre sur [Twitter](https://x.com/grantdotdev).