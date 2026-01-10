---
title: Comment échanger les valeurs de deux variables sans variable temporaire en
  Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-10-24T14:50:48.000Z'
originalURL: https://freecodecamp.org/news/swapping-values-of-two-variables-without-a-temporary-variable-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/How-To-Swap-The-Values-of-Two-Variables-Without-a-Temporary-Variable-in-python-1-1.png
tags:
- name: Python
  slug: python
seo_title: Comment échanger les valeurs de deux variables sans variable temporaire
  en Python
seo_desc: "By Jacob Isah \nSwapping the values of two variables is a common task in\
  \ programming. While the most straightforward approach involves using a temporary\
  \ variable, Python provides several elegant techniques to achieve the same result\
  \ without the need f..."
---

Par Jacob Isah

L'échange des valeurs de deux variables est une tâche courante en programmation. Bien que l'approche la plus directe implique l'utilisation d'une variable temporaire, Python offre plusieurs techniques élégantes pour obtenir le même résultat sans avoir besoin de cette variable supplémentaire.

Dans ce tutoriel, nous allons examiner quelques méthodes pour échanger les valeurs de variables en Python sans utiliser de variable temporaire.

## Pourquoi vous pourriez vouloir échanger les valeurs de deux variables sans variable temporaire en Python

Échanger les valeurs de deux variables sans utiliser de variable temporaire est important dans les situations où vous souhaitez minimiser l'utilisation de la mémoire ou la complexité du code.

Bien que l'utilisation d'une variable temporaire soit une méthode directe et courante pour échanger des valeurs, il existe des situations où vous pourriez préférer des techniques alternatives.

### Avantages de l'échange sans variable temporaire

* **Efficacité mémoire** : L'échange sans variable temporaire réduit la surcharge mémoire car vous n'avez pas besoin d'une variable supplémentaire pour contenir temporairement l'une des valeurs. Dans certains environnements contraints en ressources, cela peut être important.
* **Concis** : Des méthodes comme le déballage de tuples et les opérations bit à bit XOR offrent des solutions plus concises et élégantes. Elles peuvent rendre votre code plus lisible et nécessitent moins de lignes, ce qui est particulièrement bénéfique pour les petits extraits de code.
* **Code fonctionnel et expressif** : Certains développeurs préfèrent un code concis et expressif. L'utilisation de ces méthodes peut rendre l'intention du code plus claire et réduire l'encombrement.

### Avantages de l'utilisation d'une variable temporaire

* **Compatibilité** : Toutes les situations ne permettent pas l'utilisation de certaines techniques avancées d'échange. Par exemple, la méthode de l'opération bit à bit **XOR** est conçue pour les entiers et ne fonctionne pas bien avec d'autres types de données.
* **Clarté et lisibilité** : C'est plus facile à comprendre pour les développeurs qui ne sont peut-être pas familiers avec des techniques plus avancées. L'échange de valeurs avec une variable temporaire est la méthode la plus directe et la plus largement reconnue.
* **Maintenabilité** : Le code qui utilise une variable temporaire est souvent plus maintenable à long terme car il est plus facile à comprendre et moins sujet aux erreurs.

## Comment échanger des variables en Python en utilisant le déballage de tuples

Python nous permet d'échanger les valeurs de deux variables avec une seule ligne de code en utilisant le déballage de tuples. (Vous pouvez [en savoir plus sur les tuples en Python ici](https://www.freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference/) si vous avez besoin d'une révision.)

Le déballage de tuples, également connu sous le nom d'affectation de tuples ou de décomposition de tuples, permet aux développeurs d'affecter les éléments d'un tuple à plusieurs variables en une seule instruction.

Cette technique est possible car vous pouvez affecter plusieurs variables à la fois en utilisant un tuple du côté droit de l'opérateur d'affectation. Voici un exemple :

```python
a = 5
b = 10
a, b = b, a
print("a:", a)
print("b:", b)
```

Dans ce code, `a` et `b` sont échangés sans variable temporaire. Les valeurs sont réaffectées en une seule étape, ce qui rend cette approche concise et lisible.

## Comment échanger des variables en Python en utilisant des opérations arithmétiques

Une autre approche pour échanger des valeurs consiste à utiliser des opérations arithmétiques. Ici, nous utilisons l'addition et la soustraction pour effectuer l'échange sans avoir besoin d'une variable supplémentaire.

```python
a = 5
b = 10
a = a + b
b = a - b
a = a - b
print("a:", a)
print("b:", b)
```

Dans cette méthode, la somme de `a` et `b` est affectée à `a`, puis `b` est mis à jour avec la différence entre le nouveau `a` et l'ancien `b`. Enfin, `a` est mis à jour pour montrer la différence entre le nouveau `a` et le nouveau `b`. Le résultat est un échange réussi des valeurs.

## Comment échanger des variables en Python en utilisant l'opérateur bit à bit XOR

Pour les valeurs entières, une méthode astucieuse implique l'utilisation de l'opérateur bit à bit [**XOR (^)**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_XOR) pour échanger des valeurs sans variable temporaire.

L'opérateur XOR, représenté par le symbole `^`, est un opérateur bit à bit qui opère sur les bits individuels des nombres. Lorsqu'il est appliqué à des entiers, il peut être une manière astucieuse d'échanger les valeurs des variables sans variable temporaire.

```python
a = 5
b = 10

a = a ^ b
b = a ^ b
a = a ^ b

print("a:", a)
print("b:", b)
```

### Voici comment cette méthode fonctionne étape par étape

Passons en revue ce qui se passe dans le code ci-dessus :

**Valeurs initiales** : Au début, `a` est défini à 5 et `b` est défini à 10.

* En binaire, `a` est `0101` et `b` est `1010`.

**XOR de `a` et `b` (Première ligne)** :

* `a ^ b` est l'opération XOR entre `a` et `b`.
* L'opérateur XOR (^) compare les représentations binaires de `a` et `b` bit par bit.
* En binaire, `a` est `0101` et `b` est `1010`. Lorsqu'ils sont XORés, il inverse les bits qui sont différents et laisse les bits qui sont identiques.
* Le résultat est `1111` en binaire, ce qui est 15 en décimal.
* Par conséquent, après la première ligne, `a` devient 15.

**XOR de `a` et du nouveau `b` (Deuxième ligne)** :

* Maintenant que `a` a la valeur 15 et `b` est toujours 10, nous XORons `a` avec le nouveau `b`.
* `a ^ b` est `15 ^ 10`. En binaire, `a` est `1111` et `b` est `1010`.
* L'opération XOR inverse les bits différents, donc le résultat est `0101` en binaire, ce qui est 5 en décimal.
* Après cette ligne, `b` devient 5.

**XOR de `a` et du nouveau `b` à nouveau (Troisième ligne)** :

* Maintenant, avec `a` étant 15 et `b` étant 5, nous XORons `a` avec le nouveau `b` une fois de plus.
* `a ^ b` est `15 ^ 5`. En binaire, `a` est `1111` et `b` est `0101`.
* L'opération XOR inverse à nouveau les bits différents, donc le résultat est `1010` en binaire, ce qui est 10 en décimal.
* Après cette ligne, `a` devient 10.

À ce stade, les valeurs de `a` et `b` ont été effectivement échangées. L'opération XOR nous a permis d'effectuer l'échange sans utiliser de variable temporaire supplémentaire.

Cette méthode fonctionne car l'opération XOR entre deux nombres identiques donne 0, et XORer un nombre avec 0 laisse le nombre inchangé.

Cette technique est une manière astucieuse d'échanger les valeurs des variables entières et peut être utile dans les scénarios où l'efficacité mémoire ou la concision du code est une priorité. Cependant, il est important de se rappeler qu'elle est spécifiquement conçue pour les valeurs entières et peut ne pas fonctionner comme prévu pour d'autres types de données.

## Comment échanger des variables en Python en utilisant des expressions mathématiques (pour les valeurs numériques)

Une autre méthode directe implique l'utilisation d'expressions mathématiques pour échanger des valeurs.

```python
a = 3
b = 7
a = a + b - (b := a)
print("a:", a)
print("b:", b)
```

En Python, une expression d'affectation `(:=)` vous permet d'affecter une valeur à une variable dans le cadre d'une expression plus large. Elle est souvent utilisée pour affecter une valeur à une variable et utiliser cette valeur affectée en une seule ligne. Cela peut être particulièrement utile lorsque vous souhaitez éviter la répétition et écrire un code plus concis.

### Voici ce qui se passe étape par étape

1. `b := a` : Cette partie de l'expression est une expression d'affectation. Elle affecte la valeur de `a` à `b`. Ainsi, après cette affectation, `b` aura la valeur de `a`, et `a` reste inchangé. Cette affectation se produit dans l'expression plus large.
2. `a + b - (b := a)` : Le reste de l'expression effectue des opérations mathématiques. Il calcule la somme de `a` et de l'ancien `b`, en soustrayant la valeur de `b` après qu'il a été affecté à la valeur de `a`.

* `a + b` additionne les valeurs originales de `a` et `b`.
* `(b := a)` a déjà mis à jour `b` pour qu'il ait la valeur de `a`, donc cette partie évalue à `a`.
* Enfin, le résultat est soustrait de la somme de `a` et de l'ancien `b`.

Effectivement, cette seule ligne de code échange les valeurs de `a` et `b` sans avoir besoin d'une variable temporaire. Elle affecte la valeur de `a` à `b` et la valeur de `b` à `a` tout en effectuant l'opération d'échange en une ligne.

Mais vous devez noter que bien que les expressions d'affectation puissent rendre le code plus concis, elles peuvent aussi le rendre moins lisible si vous n'êtes pas familier avec cette fonctionnalité. Assurez-vous donc d'utiliser les expressions d'affectation avec prudence et tenez compte de la lisibilité et de la maintenabilité lorsque vous décidez de les utiliser.

## Comment échanger des variables en Python en utilisant une fonction

Si vous devez échanger des variables à plusieurs endroits dans votre code, vous pouvez créer une fonction pour rendre le processus plus réutilisable.

```python
def swap(a, b):
	return b, a
a = 5
b = 10
a, b = swap(a, b)
print("a:", a)
print("b:", b)
```

Cette fonction cache la logique d'échange et retourne les valeurs échangées, rendant le code plus modulaire et lisible.

## Quand utiliser chaque méthode

Chaque méthode d'échange de valeurs en Python sans variable temporaire a ses propres forces et faiblesses. Le choix de la méthode à utiliser dépend du cas d'utilisation spécifique et de vos préférences de codage.

Voici un résumé des cas d'utilisation les mieux adaptés à chaque exemple, ainsi que quelques considérations :

### Déballage de tuples

* Cas d'utilisation : Échanger deux valeurs avec simplicité et lisibilité à l'esprit.
* Forces : Cette méthode est concise, facile à comprendre et est particulièrement bien adaptée pour échanger deux variables de manière claire et directe.
* Considérations : Elle fonctionne mieux pour deux variables et n'est pas adaptée pour des structures de données plus complexes.

### Opérations arithmétiques

* Cas d'utilisation : Une méthode simple et facile à comprendre pour échanger des valeurs, adaptée à une large gamme de scénarios.
* Forces : L'approche arithmétique est une méthode polyvalente qui fonctionne bien avec les valeurs numériques et est facile à appliquer dans divers contextes.
* Considérations : Elle nécessite trois opérations arithmétiques, ce qui peut être moins concis que d'autres méthodes.

### Opérateur bit à bit XOR

* Cas d'utilisation : Échanger des valeurs entières tout en minimisant l'utilisation de la mémoire.
* Forces : Cette méthode est efficace en mémoire et concise. Elle est adaptée aux scénarios où vous souhaitez économiser de la mémoire et utiliser une approche plus avancée et efficace.
* Considérations : Elle est spécifique aux entiers et peut ne pas être aussi lisible pour les développeurs qui ne sont pas familiers avec les opérations bit à bit.

### Expressions mathématiques (Expression d'affectation)

* Cas d'utilisation : Une méthode concise pour échanger des valeurs tout en maintenant la lisibilité du code.
* Forces : Cette technique peut être utilisée pour échanger des valeurs de manière concise en une seule ligne. Elle est particulièrement utile lorsque vous voulez un équilibre entre concision et lisibilité.
* Considérations : Elle repose sur l'utilisation des expressions d'affectation (:=), qui peuvent ne pas être familières à tous les développeurs Python.

### Utilisation d'une fonction

* Cas d'utilisation : Lorsque vous devez échanger des valeurs à plusieurs endroits dans votre code.
* Forces : Créer une fonction pour l'échange de valeurs encapsule la logique et la rend réutilisable. Cela est utile lorsque vous devez échanger des valeurs dans différentes parties de votre code.
* Considérations : Elle introduit un appel de fonction, ce qui peut être moins concis pour un simple échange ponctuel.

Il n'existe pas de méthode universelle qui fonctionne mieux dans toutes les situations. Votre choix doit être guidé par des facteurs tels que le cas d'utilisation spécifique, les types de données impliqués et l'importance de l'efficacité mémoire ou de la lisibilité du code.

En termes de facilité, des méthodes comme le déballage de tuples et les opérations arithmétiques sont généralement plus faciles à comprendre pour la plupart des développeurs Python. La méthode bit à bit XOR, bien qu'efficace, peut être moins lisible et moins couramment utilisée. La méthode d'expression mathématique avec les expressions d'affectation est concise mais peut être moins familière aux développeurs qui ne sont pas à jour avec les dernières fonctionnalités de Python.

En fin de compte, la meilleure méthode dépend de vos exigences spécifiques et de vos préférences de style de codage. Il est essentiel de trouver un équilibre entre l'efficacité, la lisibilité et la maintenabilité lors du choix d'une technique d'échange de valeurs.

## Conclusion

Dans cet article, j'ai expliqué comment vous pouvez échanger les valeurs de deux variables en Python sans variable temporaire. Nous avons examiné l'utilisation de plusieurs techniques, telles que le déballage de tuples, les opérations arithmétiques, les opérations bit à bit XOR, les expressions mathématiques, ou l'encapsulation (cachage) de la logique dans une fonction.

Ces méthodes offrent des options pour différentes situations, des lignes de code concises aux fonctions réutilisables. Choisissez celle qui convient le mieux à vos besoins spécifiques, en tenant compte des types de données et du contexte de votre code. Que vous privilégiez la lisibilité, la performance ou la concision, Python offre une solution pour tous.