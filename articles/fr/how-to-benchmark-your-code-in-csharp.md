---
title: Comment mesurer les performances de votre code en C#
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-11-19T00:33:26.377Z'
originalURL: https://freecodecamp.org/news/how-to-benchmark-your-code-in-csharp
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1731752379027/4ec760c3-4183-4852-9d3d-e3a5c75b4bcf.png
tags:
- name: C#
  slug: csharp
- name: .NET
  slug: net
seo_title: Comment mesurer les performances de votre code en C#
seo_desc: 'Knowing how your code performs is a crucial part of development. We strive
  to write the most optimal and performant code whilst keeping readability.

  In this article, I will show you how to test the performance of your code, benchmark
  your code, and i...'
---

Savoir comment votre code se comporte est une partie cruciale du développement. Nous nous efforçons d'écrire le code le plus optimal et performant tout en maintenant la lisibilité.

Dans cet article, je vais vous montrer comment tester les performances de votre code, mesurer les performances de votre code et identifier les domaines d'amélioration dans votre base de code.

## Table des matières

* [Qu'est-ce que le Benchmarking ?](#heading-quest-ce-que-le-benchmarking)
    
* [Pourquoi utiliser un chronomètre n'est pas fiable](#heading-pourquoi-utiliser-un-chronometre-nest-pas-fiable)
    
* [Comment utiliser BenchMarkDotnet](#heading-comment-utiliser-benchmarkdotnet)
    
* [Que pouvez-vous tester d'autre avec BenchmarkDotnet ?](#heading-que-pouvez-vous-tester-dautre-avec-benchmarkdotnet)
    

## Qu'est-ce que le Benchmarking ?

Le Benchmarking mesure les performances de votre code, application, système ou matériel dans des conditions spécifiques.  
  
L'objectif est de recueillir des données précises sur le comportement du système pour des métriques comme la vitesse de traitement, l'utilisation de la mémoire, la consommation des ressources ou le débit, et d'identifier les domaines où les performances peuvent être optimisées.

## Pourquoi utiliser un chronomètre n'est pas fiable

L'utilisation de la classe `Stopwatch` pour le benchmarking en C# pose de nombreux problèmes. Bien qu'elle fournisse un moyen simple de mesurer le temps écoulé pour une méthode ou un processus, elle manque de précision, de contrôle et de cohérence nécessaires pour un benchmarking précis.  
  
Avant d'aborder les inconvénients de cet utilitaire, voyons comment vous pourriez l'utiliser pour des tâches très simples.

```csharp
using System.Diagnostics;

// Créer une nouvelle instance de Stopwatch
var sw = new Stopwatch();

// Démarrer l'horloge du chronomètre
sw.Start();

// exécuter votre code
var sum = 0;
for (int i = 0; i < 100; i++)
{
    sum += i * i;
    Console.WriteLine($"{sw.ElapsedMilliseconds}");
}
// Arrêter l'horloge !
sw.Stop();

// Afficher le temps total écoulé sur le Stopwatch.
Console.WriteLine($"Temps écoulé : {sw.ElapsedMilliseconds} ms");
```

Cela imprimerait combien de millisecondes se sont écoulées à chaque itération ainsi que les millisecondes écoulées à la fin. Comme il s'agit d'un programme court, vous pouvez convertir en nanosecondes en utilisant `ticks` comme suit :

```csharp
long ticks = stopwatch.ElapsedTicks;
double nanoseconds = (ticks * 1e9) / Stopwatch.Frequency;
```

Utiliser un chronomètre peut être utile si vous souhaitez comparer rapidement deux méthodes ou identifier des goulots d'étranglement de performance évidents pendant le développement. C'est un moyen léger d'avoir une première idée des sections de code qui pourraient nécessiter une optimisation.

### Inconvénients de Stopwatch

* Manque de précision par défaut, n'étant précis qu'à environ 100 nanosecondes, ce qui peut ne pas être utile pour des opérations micro plus petites et rapides.
    
* Compilation JIT (Just in Time) - Lorsque le code s'exécute pour la première fois, un compilateur JIT compile le code avant de l'exécuter, provoquant un délai et faussant le temps de complétion. Les exécutions ultérieures du code seront légèrement plus rapides, cependant, `Stopwatch` ne tient pas compte de cela. En gardant cela à l'esprit, il est utile d'exécuter le code plusieurs fois pour essayer d'atténuer ce problème.
    
* Garbage Collection (GC) - Si le garbage collection se produit pendant une mesure `Stopwatch`, le temps enregistré inclura le temps de pause du GC, ce qui ne reflète pas le temps d'exécution réel de votre code.
    

Ce ne sont là que quelques-uns des défauts de base et les plus courants de l'utilisation d'un `Stopwatch` pour tester les performances de votre code, mais il en existe d'autres.  
  
Alors, quelle est la meilleure approche ?

**BenchmarkDotNet** est une bibliothèque populaire et robuste pour le benchmarking en .NET, qui peut être installée en utilisant `nuget`.

Elle surmonte de nombreux défis mentionnés ci-dessus, de la manière suivante :

* Échauffement du code - Échauffe automatiquement le code (en l'exécutant plusieurs fois) pour éviter les inexactitudes liées au JIT.
    
* Itérations multiples du code - Exécute le code plusieurs fois pour analyser et calculer des résumés statistiques sur le temps d'exécution, l'allocation de mémoire heap et plus encore. Le nombre de fois où le code est exécuté peut être configuré.
    
* Environnements isolés - Gère le garbage collection et isole l'environnement d'exécution pour réduire les interférences externes.
    

## Comment utiliser BenchMarkDotnet

Tout d'abord, nous devons installer le package Nuget. Pour ce faire, exécutez la commande suivante dans votre ligne de commande/terminal :

```plaintext
dotnet add package BenchmarkDotnet
```

Nous avons ensuite besoin de méthodes à mesurer, alors créez une application console C# .Net 8 avec les deux fichiers de classe suivants :

```csharp
// Program.cs
using BenchmarkDotNet.Running;

BenchmarkRunner.Run<Benchmarks>();
```

```csharp
//Benchmarks.cs
using BenchmarkDotNet.Attributes;

public class Benchmarks
{
    private readonly int[] _numbers = Enumerable.Range(1, 1000).ToArray();

    [Benchmark]
    public int ForLoopSum()
    {
        int sum = 0;
        for (int i = 0; i < _numbers.Length; i++)
        {
            sum += _numbers[i];
        }

        return sum;
    }

    [Benchmark]
    public int ForeachLoopSum()
    {
        var sum = 0;
        foreach (int number in _numbers)
        {
            sum += number;
        }

        return sum;
    }

    [Benchmark]
    public int LinqSelect()
    {
        return _numbers.Sum();
    }
}
```

Ci-dessus, nous avons 3 méthodes différentes pour additionner un tableau d'entiers, chacune le faisant de manière légèrement différente. C'est un exemple parfait pour montrer comment le benchmarking peut nous aider à choisir la meilleure solution dans notre base de code.

### Comment exécuter les Benchmarks

Pour exécuter les benchmarks, vous pouvez exécuter les commandes suivantes dans votre terminal/ligne de commande.

```bash
dotnet build
# puis exécuter 
dotnet run -c Release
```

BenchmarkDotnet exécutera alors les méthodes marquées avec l'attribut `[Benchmark]` plusieurs fois, et affichera les résultats dans un tableau facile à lire, comme suit :

```bash
| Méthode         | Moyenne     | Erreur   | StdDev  |
|--------------- |---------:|--------:|--------:|
| ForLoopSum     | 434.2 ns | 0.40 ns | 0.31 ns |
| ForeachLoopSum | 321.9 ns | 1.22 ns | 1.14 ns |
| LinqSelect     | 189.4 ns | 0.84 ns | 0.70 ns |
```

Que signifie cela ?

**Méthode** - Nom de la méthode sous test  
  
**Moyenne** - Montre le temps moyen (moyenne) qu'il a fallu en nanosecondes.  
  
**Erreur** - Représente la marge d'erreur, vous indiquant combien le résultat "Moyenne" peut varier en raison de facteurs aléatoires dans le système. Plus le nombre est bas, mieux c'est, ici vous pouvez voir une très petite marge d'erreur signifiant que les résultats sont stables, tandis que des nombres plus grands signifieraient plus d'incertitude/résultats peu fiables.

**StdDev -** (Écart type) montre la cohérence des résultats de benchmark. Un score de déviation faible indique que le temps pris était très similaire sur plusieurs exécutions, augmentant la fiabilité. Si l'écart type est élevé, cela signifierait que le temps d'exécution de la méthode a varié beaucoup entre les exécutions.

### Comment mesurer l'allocation de mémoire

Savoir à quelle vitesse vos méthodes s'exécutent est une statistique importante à comprendre et à connaître. Cependant, vos performances et optimisations ne concernent pas seulement le temps d'exécution, parfois vous devez vous assurer qu'il n'y a pas de fuites de mémoire ou de grandes quantités de mémoire utilisées, surtout avec des processus d'exécution importants.

Nous pouvons utiliser le `[MemoryDiagnoser]` pour la classe `Benchmarks`, ce qui informe la bibliothèque de benchmarking d'inclure les statistiques de mémoire pour les méthodes sous test.

Lorsque nous exécutons nos benchmarks, nous obtenons la sortie suivante :

```bash
| Méthode         | Moyenne     | Erreur   | StdDev  | Alloué |
|--------------- |---------:|--------:|--------:|----------:|
| ForLoopSum     | 436.8 ns | 5.32 ns | 4.98 ns |         - |
| ForeachLoopSum | 324.6 ns | 2.20 ns | 2.06 ns |         - |
| LinqSelect     | 192.7 ns | 2.40 ns | 2.24 ns |         - |
```

Mais attendez, la colonne **Alloué** n'a qu'un tiret ? Où sont les résultats ?

Les opérations simples, comme la somme des valeurs dans un tableau, n'allouent généralement pas de mémoire, car elles utilisent souvent uniquement la mémoire de la pile, que BenchmarkDotNet ne suit pas de la même manière.

Mais en utilisant les tests suivants, nous pouvons voir comment l'allocation de mémoire peut être analysée :

```csharp
public class MemoryBenchmark
{
    [Benchmark]
    public string StringConcatenation()
    {
        string result = "";
        for (int i = 0; i < 1000; i++)
        {
            result += "text";
        }
        return result;
    }

    [Benchmark]
    public string StringBuilderConcatenation()
    {
        var builder = new System.Text.StringBuilder();
        for (int i = 0; i < 1000; i++)
        {
            builder.Append("text");
        }
        return builder.ToString();
    }
}
```

Sortie :

```bash
| Méthode                     | Moyenne       | Erreur     | StdDev    | Gen0     | Alloué  |
|--------------------------- |-----------:|----------:|----------:|---------:|-----------:|
| StringConcatenation        | 218.930 us | 0.7230 us | 0.6409 us | 641.8457 | 3933.56 KB |
| StringBuilderConcatenation |   1.645 us | 0.0034 us | 0.0030 us |   2.6875 |   16.47 KB |
```

Ici, nous avons 2 nouvelles colonnes :  
**Colonne Gen0 :**  
La colonne **Gen0** indique combien de collectes de garbage de Gen 0 se sont produites pendant l'exécution de chaque méthode.  
  
.Net utilise un système de garbage collection générationnel, où la mémoire est divisée en trois "générations" (Gen0, Gen1 et Gen2).

* **Gen0 (Génération 0)** : Contient des objets de courte durée de vie, tels que des variables temporaires et des objets petits et rapidement jetés. Les collectes Gen0 sont le type de GC le plus rapide mais introduisent tout de même une certaine surcharge. Des exemples de Gen0 seraient des variables locales dans des méthodes, des objets temporaires ou des arguments d'appel de méthode qui ne sont pas utilisés plus tard.
    
* **Gen1 et Gen2** : Cela concerne les objets de plus longue durée de vie qui survivent aux collectes Gen0, comme les objets statiques qui sont maintenus en vie pendant la durée de vie de l'application (c'est-à-dire, les singletons), les objets de cache ou les grandes collections utilisées dans de nombreuses opérations.
    

Les objets dans **Gen0** sont collectés rapidement mais souvent, et les objets dans **Gen2** sont collectés rarement mais avec plus d'efforts car ils sont plus grands ou plus persistants. Beaucoup de collectes **Gen0** peuvent être un indicateur d'une utilisation inefficace de la mémoire, tandis que les collectes **Gen2 ou 3** peuvent indiquer que votre application conserve trop d'objets de longue durée de vie en mémoire.

**Colonne Alloué :**  
La colonne **Alloué** montre la mémoire totale allouée par chaque méthode pendant son exécution. Cela est généralement rapporté en kilo-octets (KB).

Ces informations vous aident à voir à quel point chaque méthode est intensive en mémoire, ce qui peut avoir un impact sur les performances, surtout si la méthode est appelée fréquemment.

Par exemple, `StringBuilderConcatenation` est beaucoup plus efficace en mémoire que `StringConcatenation`, ce qui le rend préférable dans les cas où l'utilisation de la mémoire est une préoccupation ou où cette opération est effectuée fréquemment.

## Que pouvez-vous tester d'autre avec BenchmarkDotnet ?

### Débit

* Analyse combien d'itérations d'une méthode peuvent être exécutées par seconde.
    
* Indique l'efficacité et l'évolutivité du code.
    

### Impact de l'optimisation JIT (Just-In-Time)

* Évalue les effets des optimisations JIT sur les performances.
    
* Peut tester les démarrages à froid (performances de la première exécution) par rapport aux performances en régime établi (exécutions ultérieures).
    

### Différences de plateforme et de Framework

Vous pourriez exécuter des benchmarks du même code sur différents runtimes .NET (par exemple, .NET 6, .NET 8, .NET Framework) pour comparer s'il vaut la peine de mettre à niveau votre application vers des systèmes plus récents ou non.

Mettez simplement à jour le nœud TargetFramework dans le fichier `.csproj` de votre application pour cibler les frameworks que vous souhaitez tester.

Ajoutez les attributs suivants à votre classe de benchmark (en fonction du runtime cible).

```bash
[SimpleJob(runtimeMoniker: RuntimeMoniker.Net60)]
[SimpleJob(runtimeMoniker: RuntimeMoniker.Net80)]
```

Lorsque vous exécutez votre application, vous obtiendrez une sortie comme ci-dessous mettant en évidence les différences dans les méthodes entre .net 6 et .net 8

| Méthode | Job | Runtime | Moyenne | Erreur | StdDev |
| --- | --- | --- | --- | --- | --- |
| StringConcatenation | .NET 6.0 | .NET 6.0 | 286.503 us | 3.5004 us | 3.1030 us |
| StringBuilderConcatenation | .NET 6.0 | .NET 6.0 | 4.595 us | 0.0620 us | 0.0580 us |
| StringConcatenation | .NET 8.0 | .NET 8.0 | 222.270 us | 1.7561 us | 1.4664 us |
| StringBuilderConcatenation | .NET 8.0 | .NET 8.0 | 1.650 us | 0.0139 us | 0.0116 us |

### Impact des paramètres d'entrée

* Prend en charge les benchmarks paramétrés pour tester comment différentes entrées affectent les performances.
    
* Aide à identifier les plages d'entrée optimales ou les cas limites problématiques.
    

Vous pouvez faire quelque chose comme ceci

```csharp
using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

public class SortBenchmark
{
    [Params(10, 100, 1000)]  // Taille du tableau
    public int N;

    [Params(10, 100, 1000)]  // Valeur maximale des éléments du tableau
    public int MaxValue;

    private int[] data;

    // Méthode de configuration pour créer un tableau avant chaque benchmark
    [GlobalSetup]
    public void Setup()
    {
        data = new int[N];
        var rand = new Random();
        for (int i = 0; i < N; i++)
        {
            data[i] = rand.Next(MaxValue);
        }
    }

    [Benchmark]
    public void SortArray()
    {
        Array.Sort(data);  // Trier le tableau
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Exécuter le benchmark
        BenchmarkRunner.Run<SortBenchmark>();
    }
}
```

Donnant la sortie suivante :

| Méthode | N | MaxValue | Moyenne | Erreur | StdDev | Alloué |
| --- | --- | --- | --- | --- | --- | --- |
| SortArray | 10 | 10 | 3.5 ns | 0.1 ns | 0.05 ns | 0 B |
| SortArray | 10 | 1000 | 4.0 ns | 0.2 ns | 0.1 ns | 0 B |
| SortArray | 100 | 10 | 20.1 ns | 0.5 ns | 0.3 ns | 0 B |
| SortArray | 100 | 1000 | 25.2 ns | 0.8 ns | 0.4 ns | 0 B |
| SortArray | 1000 | 10 | 300.3 ns | 5.6 ns | 2.7 ns | 0 B |
| SortArray | 1000 | 1000 | 320.1 ns | 6.3 ns | 3.1 ns | 0 B |

### Performances des bibliothèques tierces

En utilisant les techniques mentionnées ci-dessus, vous pouvez comparer les performances de différentes bibliothèques tierces pour la même tâche afin de prendre des décisions éclairées sur l'utilisation des bibliothèques.

## Conclusion

Voilà, comment mesurer les performances de votre application C#. En utilisant une combinaison de ces méthodes, outils et techniques, les possibilités de benchmarking sont incroyables.

Vous pouvez utiliser le benchmarking pour améliorer la base de code de votre application, aider à prendre des décisions sur les chemins de mise à niveau et les choix de méthodes.

J'espère que vous trouverez cet article utile, et comme toujours, si vous souhaitez en discuter, vous pouvez me suivre sur [Twitter](https://x.com/grantdotdev).