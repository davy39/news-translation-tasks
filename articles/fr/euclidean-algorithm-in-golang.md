---
title: Comment fonctionne l'algorithme d'Euclide – avec des exemples de code en Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-08T20:18:08.000Z'
originalURL: https://freecodecamp.org/news/euclidean-algorithm-in-golang
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-skitterphoto-1019470.jpg
tags:
- name: algorithms
  slug: algorithms
- name: golang
  slug: golang
- name: Mathematics
  slug: mathematics
seo_title: Comment fonctionne l'algorithme d'Euclide – avec des exemples de code en
  Go
seo_desc: "By Otavio Ehrenberger\nThe Euclidean Algorithm is a well-known and efficient\
  \ method for finding the greatest common divisor (GCD) of two integers. The GCD\
  \ is the largest number that can divide both integers without leaving a remainder.\
  \ \nThe algorithm ..."
---

Par Otavio Ehrenberger

L'algorithme d'Euclide est une méthode bien connue et efficace pour trouver le plus grand commun diviseur (PGCD) de deux entiers. Le PGCD est le plus grand nombre qui peut diviser les deux entiers sans laisser de reste. 

L'algorithme porte le nom du mathématicien grec ancien Euclide, qui l'a présenté dans son livre "Éléments" vers 300 avant J.-C.

Vous pouvez utiliser cet algorithme pour résoudre des [équations diophantiennes](https://en.wikipedia.org/wiki/Diophantine_equation), pour aborder le [problème du plus court vecteur](https://en.wikipedia.org/wiki/Lattice_problem) qui est la base de la [cryptographie basée sur les réseaux](https://en.wikipedia.org/wiki/Lattice-based_cryptography), et également pour détecter des motifs communs de pixels dans les images. Cela est, entre autres, appliqué pour optimiser les processus de rendu et détecter différents objets dans les images.

## Comment fonctionne l'algorithme d'Euclide ?

Voici une explication étape par étape du fonctionnement de l'algorithme d'Euclide :

Commencez avec deux entiers positifs, a et b, où a >= b. Si a < b, échangez simplement leurs valeurs. Notez que cela est destiné à une démonstration mathématique pratique, car l'implémentation fonctionne également pour a < b.

Divisez a par b et trouvez le reste, r (utilisez l'opération modulo, représentée par a % b). Si r est 0, le PGCD est b, et l'algorithme se termine.

Si r n'est pas 0, définissez a sur b et b sur r. Ensuite, répétez l'étape 2.

L'algorithme continue à itérer jusqu'à ce que le reste soit 0. À ce moment-là, le dernier reste non nul est le PGCD des deux nombres originaux. 

L'algorithme d'Euclide fonctionne parce que le PGCD de deux nombres reste inchangé lorsque le plus grand nombre est remplacé par son reste lorsqu'il est divisé par le plus petit nombre.

### Exemple de l'algorithme d'Euclide

Voici un exemple pour illustrer l'algorithme :

Trouvons le PGCD de 30 et 9 :

a = 30, b = 9

Calculez le reste : r = a % b = 30 % 9 = 3 (puisque 3 n'est pas 0, continuez à l'étape 3)

Mettez à jour les valeurs : a = 9, b = 3

Calculez le nouveau reste : r = a % b = 9 % 3 = 0 (r est maintenant 0)

Le PGCD de 30 et 9 est 3.

## Pourquoi l'algorithme d'Euclide fonctionne-t-il ?

Le plus grand commun diviseur de deux entiers est le plus grand entier positif qui divise les deux sans laisser de reste. Ainsi, l'algorithme est basé sur la propriété clé suivante :

**Si `a` et `b` sont deux entiers, alors le PGCD de `a` et `b` est le même que le PGCD de `b` et `a % b`, où `%` représente l'opérateur modulo (le reste après division)**.

Mathématiquement, la propriété clé de l'algorithme peut être justifiée en utilisant l'algorithme de division :

Soit `a` et `b` deux entiers positifs, tels que `a >= b`. Nous pouvons écrire l'algorithme de division comme :

`a = bq + r`, où `q` est le quotient et `r` est le reste.

Maintenant, soit `d` un diviseur commun de `a` et `b`. Alors, `a = d * m1` et `b = d * m2` pour certains entiers `m1` et `m2`. Nous pouvons réécrire l'algorithme de division comme :

`d * m1 = (d * m2) * q + r`.

En réarrangeant l'équation, nous obtenons :

`r = d * (m1 - m2 * q)`.

Puisque `d` est un facteur de `a` et `b`, et que `r` peut également s'écrire comme un multiple de `d`, nous pouvons conclure que `d` est également un diviseur de `r`. Cela signifie que le PGCD de `a` et `b` est également un diviseur de `r`. Ainsi, nous pouvons remplacer `b` par `r` et continuer à trouver le PGCD en utilisant cet algorithme jusqu'à ce que `b` devienne 0.

L'algorithme d'Euclide est particulièrement utile en raison de son efficacité et de sa simplicité, ce qui le rend facile à implémenter dans des algorithmes informatiques et des langages de programmation.

Voyons différentes façons de l'implémenter en Go :

## Implémentation récursive de l'algorithme d'Euclide en Go

Cette implémentation de l'algorithme d'Euclide en Golang est une version récursive qui trouve le PGCD de deux entiers. Passons en revue étape par étape :

La fonction est définie comme `GCD(a, b int) int`. Elle prend deux entrées entières, `a` et `b`, et retourne une sortie entière.

Le cas de base de la récursion est vérifié avec `if b == 0`. Si `b` est 0, la fonction retourne la valeur de `a` comme PGCD.

Si `b` n'est pas 0, une variable temporaire `tmp` est créée et reçoit la valeur de `a`. Cette variable temporaire est utilisée pour stocker la valeur de `a` avant de mettre à jour sa valeur à l'étape suivante.

Les valeurs de `a` et `b` sont mises à jour comme suit :

* `a` reçoit la valeur actuelle de `b`.
* `b` reçoit la valeur du reste lorsque `tmp` (l'ancienne valeur de `a`) est divisé par la nouvelle valeur de `a` (qui était `b` avant la mise à jour).

La fonction s'appelle elle-même de manière récursive avec les valeurs mises à jour de `a` et `b` comme entrée, `return GCD(a, b)`.

L'algorithme continue à s'appeler lui-même de manière récursive jusqu'à ce que le cas de base soit atteint, c'est-à-dire que `b` devienne 0. À ce moment-là, la fonction retourne le PGCD, qui est la valeur de `a`.

```go
// Approche récursive :
func GCD(a, b int) int {
	if b == 0 {
		return a
	}
	tmp := a
	a = b
	b = tmp % a
	return GCD(a, b)
}

```

Par exemple, disons que nous voulons trouver le PGCD de 56 et 48 :

Premier appel : GCD(56, 48)

* Puisque `b` (48) n'est pas 0, mettez à jour `a` et `b` :
* `a` devient 48
* `b` devient 56 % 48 = 8
* La fonction s'appelle elle-même avec les nouvelles valeurs : GCD(48, 8)

Deuxième appel : GCD(48, 8)

* Puisque `b` (8) n'est pas 0, mettez à jour `a` et `b` :
* `a` devient 8
* `b` devient 48 % 8 = 0
* La fonction s'appelle elle-même avec les nouvelles valeurs : GCD(8, 0)

Troisième appel : GCD(8, 0)

* Maintenant, `b` (0) est 0, donc la fonction retourne `a` (8) comme PGCD.

## Implémentation itérative de l'algorithme d'Euclide en Go

Cette implémentation de l'algorithme d'Euclide en Golang est une version itérative utilisant une boucle pour trouver le PGCD de deux entiers. Passons en revue le code étape par étape :

La fonction est définie comme `GCD(a, b int) int`. Elle prend deux entrées entières, `a` et `b`, et retourne une sortie entière.

Une boucle est utilisée pour itérer tant que `b` n'est pas égal à 0. La condition de la boucle est `b != 0`. Notez que cette construction de boucle `for` en Go est essentiellement une boucle `while` dans de nombreux autres langages.

À l'intérieur de la boucle, les valeurs de `a` et `b` sont mises à jour simultanément en utilisant une affectation de tuple : `a, b = b, a%b`. Cette ligne fait ce qui suit :

* `a` reçoit la valeur actuelle de `b`.
* `b` reçoit la valeur du reste lorsque `a` est divisé par `b`.

Lorsque la boucle se termine (c'est-à-dire que `b` devient 0), la valeur de `a` est retournée comme PGCD.

L'algorithme itère jusqu'à ce que le reste (`b`) soit 0, moment auquel le PGCD est le dernier reste non nul, qui est la valeur de `a`.

```go
func GCD(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

```

Par exemple, disons que nous voulons trouver le PGCD de 100 et 64 :

Initialisez `a` à 100 et `b` à 64. Vérifiez la condition de la boucle : `b` (64) n'est pas 0.

À l'intérieur de la boucle, mettez à jour `a` et `b` :

* `a` devient 64
* `b` devient 100 % 64 = 36  
Vérifiez à nouveau la condition de la boucle : `b` (36) n'est pas 0.

À l'intérieur de la boucle, mettez à jour `a` et `b` :

* `a` devient 36
* `b` devient 64 % 36 = 28  
Vérifiez à nouveau la condition de la boucle : `b` (28) n'est pas 0.

À l'intérieur de la boucle, mettez à jour `a` et `b` :

* `a` devient 28
* `b` devient 36 % 28 = 8  
Vérifiez à nouveau la condition de la boucle : `b` (8) n'est pas 0.

À l'intérieur de la boucle, mettez à jour `a` et `b` :

* `a` devient 8
* `b` devient 28 % 8 = 4  
Vérifiez à nouveau la condition de la boucle : `b` (4) n'est pas 0.

À l'intérieur de la boucle, mettez à jour `a` et `b` :

* `a` devient 4
* `b` devient 8 % 4 = 0  
Vérifiez à nouveau la condition de la boucle : Maintenant, `b` (0) est 0, donc la boucle se termine.

La fonction retourne la valeur de `a` (4) comme PGCD.

## Tester les solutions

Ces tests ont été créés par Jon Calhoun dans son cours gratuit [Go Algorithms](https://courses.calhoun.io/courses/cor_algo). En supposant que vous avez défini votre fonction `GCD` dans un fichier nommé `gcd.go`, placez ces tests dans un fichier nommé `gcd_test.go`. Lisez ce qui suit pour voir comment les tests fonctionneront :

La fonction `TestGCD` est définie, prenant un seul paramètre `t *testing.T`. Le `*testing.T` est un pointeur vers un objet `testing.T` qui fournit des méthodes pour signaler les échecs de test et journaliser des informations supplémentaires.

Un tableau de structs anonymes est défini, appelé `tests`. Chaque struct a trois champs : `a`, `b`, et `want`. Ces structs représentent des cas de test, où `a` et `b` sont des valeurs d'entrée pour la fonction GCD, et `want` est le résultat attendu (PGCD correct).

Plusieurs cas de test sont définis dans le tableau `tests`, couvrant différents scénarios.

Une boucle `for` itère à travers le tableau `tests`. À chaque itération, un seul cas de test (struct) est assigné à la variable `tc`.

La fonction `t.Run` est appelée pour exécuter un sous-test pour le cas de test actuel. Le premier argument est une chaîne formatée qui décrit le cas de test (en utilisant les valeurs d'entrée `tc.a` et `tc.b`). Le deuxième argument est une fonction anonyme qui prend un paramètre `*testing.T`, similaire à la fonction de test principale.

À l'intérieur de la fonction de sous-test, la fonction GCD est appelée avec les valeurs d'entrée `tc.a` et `tc.b`, et le résultat est assigné à la variable `got`.

Le résultat `got` est comparé au résultat attendu `tc.want`. S'ils ne sont pas égaux, la fonction `t.Fatalf` est appelée pour signaler l'échec du test et fournir un message d'erreur avec le résultat incorrect et le résultat attendu.

Cette fonction de test aide à garantir que la fonction GCD fonctionne correctement pour diverses valeurs d'entrée et cas limites. Exécuter cette fonction de test avec la commande `go test` exécutera tous les cas de test et signalera les échecs, ce qui peut aider à identifier les problèmes potentiels avec l'implémentation de la fonction GCD.

```go

import (
	"fmt"
	"testing"
)

func TestGCD(t *testing.T) {
	tests := []struct {
		a, b int
		want int
	}{
		{10, 5, 5},
		{25, 5, 5},
		{30, 15, 15},
		{30, 9, 3},
		{100, 9, 1},
		{
			2 * 2 * 3 * 3 * 5,
			2 * 3 * 5 * 7 * 13,
			2 * 3 * 5,
		}, {
			2 * 2 * 3 * 3 * 13,
			2 * 3 * 5 * 7 * 13,
			2 * 3 * 13,
		}, {
			2 * 3 * 5 * 7 * 11 * 13 * 17 * 19,
			3 * 3 * 7 * 7 * 11 * 11 * 17 * 17,
			3 * 7 * 11 * 17,
		},
	}
	for _, tc := range tests {
		t.Run(fmt.Sprintf("(%v,%v)", tc.a, tc.b), func(t *testing.T) {
			got := GCD(tc.a, tc.b)
			if got != tc.want {
				t.Fatalf("GCD() = %v; want %v", got, tc.want)
			}
		})
	}
}

```

Exécutez les tests, créez différents cas comme vous le souhaitez :

```bash
go test -v # flag verbose

```

## Conclusion

J'espère que vous avez passé un bon moment à apprendre l'algorithme d'Euclide et son implémentation en Go. 

Si vous êtes intéressé par le fonctionnement de ces astuces ingénieuses, jetez un coup d'œil au domaine de la théorie des nombres en mathématiques, qui se concentre particulièrement sur les propriétés des entiers, notamment en impliquant les nombres premiers.