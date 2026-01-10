---
title: Comment écrire des tests de benchmark pour vos fonctions Golang
subtitle: ''
author: Pedro
co_authors: []
series: null
date: '2024-09-23T14:37:10.472Z'
originalURL: https://freecodecamp.org/news/how-to-write-benchmark-tests-for-your-golang-functions
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1726668982641/58540086-9f98-4ac9-8c8a-84ef45e27875.png
tags:
- name: golang
  slug: golang
- name: Golang developer
  slug: golang-developer
- name: Testing
  slug: testing
- name: Benchmark
  slug: benchmark
seo_title: Comment écrire des tests de benchmark pour vos fonctions Golang
seo_desc: 'Hello Gophers 👋

  Let me start by asking you a question: How would you test the performance of a piece
  of code or a function in Go? Well, you could use benchmark tests.

  In this tutorial, I will show you how to use an awesome benchmarking tool that’s
  b...'
---

Salut les Gophers 👋

Laissez-moi commencer par vous poser une question : Comment testeriez-vous la performance d'un morceau de code ou d'une fonction en Go ? Eh bien, vous pourriez utiliser des tests de **benchmark**.

Dans ce tutoriel, je vais vous montrer comment utiliser un outil de benchmarking génial qui est intégré au package testing de Golang.

C'est parti.

## Que sont les tests de benchmark ?

En Go, les [tests de benchmark](https://pkg.go.dev/testing#hdr-Benchmarks) sont utilisés pour mesurer la performance (vitesse et utilisation de la mémoire) des fonctions ou des blocs de code. Ces tests font partie du Framework de test de Go et sont écrits dans les mêmes fichiers que les tests unitaires, mais ils sont spécifiquement destinés à l'analyse de performance.

## Exemple de cas d'utilisation : la suite de Fibonacci

Pour cet exemple, j'utiliserai la classique suite de Fibonacci, qui est déterminée par :

```plaintext
si (x < 2) 
   F(0) = 1
   F(2) = 2
sinon 
   F(x) = F(x-1) + F(x-2)

En pratique, la suite est :
1, 1, 2, 3, 5, 8, 13, etc.
```

Cette suite est importante car elle apparaît dans diverses parties des mathématiques et de la nature également, comme illustré ci-dessous :

![Suite de Fibonacci en spirale (comme une coquille d'escargot)](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/v6fqdlmiqjob46joyfpz.png align="left")

Il existe plusieurs façons d'implémenter ce code, et j'en choisirai deux pour nos tests de benchmark : les méthodes récursive et itérative. L'objectif principal des fonctions est de fournir une *position* et de retourner le nombre de Fibonacci à cette position.

### Méthode récursive

```go
// main.go
func fibRecursive(n uint) uint {
	if n <= 2 {
		return 1
	}
	return fibRecursive(n-1) + fibRecursive(n-2)
}
```

La fonction ci-dessus est une implémentation récursive du calcul de la suite de Fibonacci. Je vais maintenant la détailler étape par étape pour vous, en tant que débutant en Go.

Voici votre fonction pour calculer les nombres de Fibonacci :

```go
func fibRecursive(n uint) uint {
	if n <= 2 {
		return 1
	}
	return fibRecursive(n-1) + fibRecursive(n-2)
}
```

#### 1\. **Fonction :**

```go
func fibRecursive(n uint) uint
```

* `func` : Ce mot-clé définit une fonction en Go.
    
* `fibRecursive` : C'est le nom de la fonction. Elle est appelée `fibRecursive` car elle calcule les nombres de Fibonacci par récursion.
    
* `n uint` : La fonction prend un seul argument, `n`, qui est de type `uint` (un entier non signé). Cela représente la position dans la suite de Fibonacci que nous voulons calculer.
    
* `uint` : La fonction retourne un `uint` (entier non signé) car les nombres de Fibonacci sont des entiers non négatifs.
    

#### 2\. **Étape de base :**

```go
if n <= 2 {
    return 1
}
```

* L'instruction `if` vérifie si `n` est inférieur ou égal à 2.
    
* Dans la suite de Fibonacci, le 1er et le 2e nombres sont tous deux 1. Donc, si `n` est 1 ou 2, la fonction retourne 1.
    
* C'est ce qu'on appelle l'**étape de base**, et elle empêche la récursion de descendre à l'infini.
    

#### 3\. **Étape récursive :**

```go
return fibRecursive(n-1) + fibRecursive(n-2)
```

* Si `n` est supérieur à 2, la fonction s'appelle elle-même deux fois :
    
    * `fibRecursive(n-1)` : Calcule le nombre de Fibonacci pour la position juste avant `n`.
        
    * `fibRecursive(n-2)` : Calcule le nombre de Fibonacci pour deux positions avant `n`.
        
* La fonction additionne ensuite ces deux résultats, car chaque nombre de Fibonacci est la somme des deux nombres précédents.
    

Pour plus de théorie sur la récursion, consultez ces [articles](https://www.freecodecamp.org/news/tag/recursion/).

### Méthode itérative

```go
// main.go

func fibIterative(position uint) uint {
	slc := make([]uint, position)
	slc[0] = 1
	slc[1] = 1

	if position <= 2 {
		return 1
	}

	var result, i uint
	for i = 2; i < position; i++ {
		result = slc[i-1] + slc[i-2]
		slc[i] = result
	}

	return result
}
```

Ce code implémente une approche **itérative** pour calculer la suite de Fibonacci en Go, ce qui est différent de l'approche **récursive**. Voici le détail de son fonctionnement :

#### 1\. **Fonction :**

```go
func fibIterative(position uint) uint
```

* `func` : Ce mot-clé déclare une fonction en Go.
    
* `fibIterative` : Le nom de la fonction suggère qu'elle calcule les nombres de Fibonacci par itération (une boucle).
    
* `position uint` : La fonction prend un argument, `position`, qui est un entier non signé (`uint`). Cela représente la position de la suite de Fibonacci que vous souhaitez calculer.
    
* `uint` : La fonction retourne un entier non signé (`uint`), qui sera le nombre de Fibonacci à la position spécifiée.
    

#### 2\. **Création d'un Slice (structure de type tableau) :**

```go
slc := make([]uint, position)
```

* `slc` est un slice (un tableau dynamique en Go) créé avec une longueur égale à `position`. Ce slice stockera les nombres de Fibonacci à chaque index.
    

#### 3\. **Valeurs initiales pour la suite de Fibonacci :**

```go
slc[0] = 1
slc[1] = 1
```

* Les deux premiers nombres de Fibonacci sont `1`, donc les deux premières positions du slice (`slc[0]` et `slc[1]`) sont définies sur `1`.
    

#### 4\. **Retour anticipé pour les petites positions :**

```go
if position <= 2 {
	return 1
}
```

* Si l'entrée `position` est `1` ou `2`, la fonction retourne directement `1`, car les deux premiers nombres de Fibonacci sont toujours `1`.
    

#### 5\. **Boucle itérative :**

```go
var result, i uint
for i = 2; i < position; i++ {
	result = slc[i-1] + slc[i-2]
	slc[i] = result
}
```

* La boucle commence à `i = 2` et s'exécute jusqu'à ce qu'elle atteigne la `position`.
    
* À chaque itération, le nombre de Fibonacci à l'index `i` est calculé comme la somme des deux nombres de Fibonacci précédents (`slc[i-1]` et `slc[i-2]`).
    
* Le résultat est stocké à la fois dans `result` et dans le slice `slc[i]` pour les calculs futurs.
    

#### 6\. **Retour du résultat :**

```go
return result
```

* Une fois la boucle terminée, la variable `result` contient le nombre de Fibonacci à la position souhaitée, et la fonction le retourne.
    

C'est une approche plus *efficace* pour calculer les nombres de Fibonacci par rapport à la récursion, surtout quand la `position` est grande, car **elle ne répète pas de calculs inutiles**, ce que nous allons prouver en utilisant des tests de benchmark. Prouvons-le.

## Comment exécuter les tests de benchmark

Maintenant, pour les tests de benchmark, écrivons du code de test. D'abord, vous devrez créer un fichier **main_test.go**. À l'intérieur, en utilisant la [documentation](https://pkg.go.dev/testing@go1.22.3#hdr-Benchmarks) de Golang sur les tests de benchmark, vous pouvez créer les fonctions à tester comme suit :

```go
// main_test.go

// Benchmark pour la fonction itérative
func BenchmarkFibIterative(b *testing.B) {
	for i := 0; i < b.N; i++ { 
		fibIterative(uint(10))
	}
}
// Benchmark pour la fonction récursive
func BenchmarkFibRecursive(b *testing.B) {
	for i := 0; i < b.N; i++ {
		fibRecursive(uint(10))
	}
}
```

Exécutons le test pour la position 10 puis augmentons de manière appropriée. Pour exécuter les tests de benchmark, lancez simplement la commande `go test -bench=NomDeLaFonction`.

Si vous voulez en savoir plus sur cette commande, regardez [ici](https://pkg.go.dev/testing@go1.22.3#Benchmark). Vérifions la fonction pour la **position 10** :

```go
func BenchmarkFibIterative(b *testing.B) {
	for i := 0; i < b.N; i++ { 
		fibIterative(uint(10))
	}
}
```

```go
go test -bench=BenchmarkFibIterative
Results:
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibIterative-8         27715262                42.86 ns/op
PASS
ok      playground      2.617s
```

Analysons à l'aide de cette image :

![visitez https://www.practical-go-lessons.com/chap-34-benchmarks](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/484ap11qw8d81b43gg0v.png align="left")

Selon l'image, nous avons 8 cœurs pour les tests, et pas de limite de temps (il s'exécutera jusqu'à la fin). Il a fallu **27\_715\_262 itérations** et **1,651 secondes** pour terminer la tâche.

```go
func BenchmarkFibRecursive(b *testing.B) {
	for i := 0; i < b.N; i++ {
		fibRecursive(uint(10))
	}
}
```

```go
go test -bench=BenchmarkFibRecursive
Results:
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibRecursive-8          6644950               174.3 ns/op
PASS
ok      playground      1.819s
```

En utilisant la même image pour analyser le résultat, dans ce cas, il a fallu **6\_644\_950 itérations** et **1,819 secondes** pour terminer la tâche, nous avons :

| Fonction Fibonacci | Position | Itérations | Temps d'exécution (s) |
| --- | --- | --- | --- |
| Itérative | 10 | 27\_715\_262 | 1.651 |
| Récursive | 10 | 6\_644\_950 | 1.819 |

Les **résultats du benchmark** montrent que l'approche itérative est nettement plus efficace que l'approche récursive pour calculer la suite de Fibonacci.

Pour la position 10, la fonction itérative a effectué environ **27,7 millions d'itérations** en **1,651 secondes**, tandis que la fonction récursive n'a réussi que **6,6 millions d'itérations** en **1,819 secondes**. La méthode itérative a surpassé la méthode récursive tant en termes d'itérations que de temps, soulignant son efficacité.

Pour prouver cela encore plus loin, essayons avec la **position 40** (4 fois la valeur précédente) :

```go
// Résultats pour la fonction itérative
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibIterative-8          9904401               114.5 ns/op
PASS
ok      playground      1.741s

// Résultats pour la fonction récursive
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibRecursive-8                4         324133575 ns/op
PASS
ok      playground      3.782s
```

| Fonction Fibonacci | Position | Itérations | Temps d'exécution (s) |
| --- | --- | --- | --- |
| Itérative | 40 | 9\_904\_401 | 1.741 |
| Récursive | 40 | 4 | 3.782 |

Les résultats du benchmark soulignent à nouveau clairement la différence d'efficacité entre les approches itérative et récursive pour le calcul de Fibonacci.

La **fonction itérative** a terminé environ **9,9 millions d'itérations** avec un temps d'exécution moyen de **114,5 nanosecondes par opération**, finissant le benchmark en **1,741 secondes**. En revanche, la **fonction récursive** n'a effectué que **4 itérations** avec un temps d'exécution moyen de **324 133 575 nanosecondes par opération** (plus de 324 millisecondes par appel), prenant **3,782 secondes** pour finir.

Ces résultats démontrent que l'approche récursive est beaucoup moins efficace en raison des appels de fonction répétés et des recalculs, ce qui rend la méthode itérative largement supérieure tant en vitesse qu'en utilisation des ressources, surtout à mesure que la taille de l'entrée augmente.

Juste par curiosité, j'ai essayé la **position 60** et cela a littéralement fait planter le test :

```go
// Résultats pour la fonction itérative
cpu: Intel(R) Core(TM) i7-7700HQ CPU @ 2.80GHz
BenchmarkFibIterative-8          7100899               160.9 ns/op

// Résultats pour la fonction récursive
SIGQUIT: quit
PC=0x7ff81935f08e m=0 sigcode=0

goroutine 0 gp=0x3bf1800 m=0 mp=0x3bf26a0 [idle]:
runtime.pthread_cond_wait(0x3bf2be0, 0x3bf2ba0)
...
```

## Conclusion

Si votre code de production s'exécute lentement ou est imprévisiblement lent, vous pouvez utiliser cette technique, combinée avec [**pprof**](https://pkg.go.dev/runtime/pprof) ou d'autres outils du package testing intégré, pour identifier et tester les endroits où votre code est peu performant et travailler sur la façon de l'optimiser.

Rappelez-vous : un code qui est beau à regarder n'est pas nécessairement le plus performant.

### Référence

* Fonctions récursive et itérative pour la suite de Fibonacci [ici](https://gist.github.com/pedrobertao/a31466b3287f165f22d05f0fb2b066f2).
    
* Tests de benchmark [ici](https://gist.github.com/pedrobertao/d435d9f1b0915cbc1cb54bc385f45104).
    

### Devoirs

Cet [article](https://www.meccanismocomplesso.org/en/the-fibonacci-series-three-different-algorithms-compared/) explique pourquoi pour certains petits nombres, la stratégie récursive est meilleure. Pouvez-vous trouver un meilleur moyen d'améliorer la fonction récursive ? (Astuce : utilisez la programmation dynamique).