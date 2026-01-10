---
title: Fonctions Lambda en Python – Comment utiliser les Lambdas avec Map, Filter
  et Reduce
subtitle: ''
author: Samyak Jain
co_authors: []
series: null
date: '2024-06-14T14:44:05.000Z'
originalURL: https://freecodecamp.org/news/lambda-functions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/python-lambda-functions.jpg
tags:
- name: Python
  slug: python
seo_title: Fonctions Lambda en Python – Comment utiliser les Lambdas avec Map, Filter
  et Reduce
seo_desc: 'In this tutorial, we will explore the various aspects of lambda functions
  in Python, including their syntax, use cases, and limitations.

  By understanding how to effectively utilize lambda functions, you can write more
  concise and efficient Python cod...'
---

Dans ce tutoriel, nous allons explorer les différents aspects des fonctions lambda en Python, y compris leur syntaxe, leurs cas d'utilisation et leurs limitations.

En comprenant comment utiliser efficacement les fonctions lambda, vous pouvez écrire un code Python plus concis et plus efficace. Cela améliorera vos compétences en programmation et rendra votre base de code plus propre et plus facile à gérer.

## **Table des matières :**

1. [Qu'est-ce que les fonctions Lambda en Python ?](https://www.freecodecamp.org/news/lambda-functions-in-python/#questce-que-les-fonctions-lambda-en-python)
2. [Syntaxe des fonctions Lambda et utilisations de base](https://www.freecodecamp.org/news/lambda-functions-in-python/#syntaxe-des-fonctions-lambda-et-utilisations-de-base)
3. [Façons d'appeler les fonctions Lambda](https://www.freecodecamp.org/news/lambda-functions-in-python/#facons-dappeler-les-fonctions-lambda)
   - [Assignation à une variable](https://www.freecodecamp.org/news/lambda-functions-in-python/#1-assignation-a-une-variable)
   - [Appel direct de la fonction Lambda](https://www.freecodecamp.org/news/lambda-functions-in-python/#2-appel-direct-de-la-fonction-lambda)
   - [Utilisation comme argument pour les fonctions d'ordre supérieur](https://www.freecodecamp.org/news/lambda-functions-in-python/#3-utilisation-comme-argument-pour-les-fonctions-dordre-superieur)
4. [Cas d'utilisation supplémentaires](https://www.freecodecamp.org/news/lambda-functions-in-python/#cas-dutilisation-supplementaires)
5. [Conclusion](https://www.freecodecamp.org/news/lambda-functions-in-python/#conclusion)

## **Qu'est-ce que les fonctions Lambda en Python ?**

En Python, une fonction lambda est une petite fonction anonyme définie à l'aide du mot-clé `lambda`.

Ces fonctions sont généralement utilisées pour des opérations courtes et jetables où une définition complète de fonction pourrait être excessive. Elles sont appelées anonymes car elles ne nécessitent pas de nom (bien qu'elles puissent être assignées à une variable pour être réutilisées).

Les fonctions lambda excellent dans les scénarios où vous avez besoin d'une fonction rapide et simple pour une courte période, et où une définition complète de fonction serait excessive. Cela les rend idéales pour des opérations simples qui peuvent être écrites en une seule ligne, comme des calculs mathématiques simples ou des transformations de données basiques.

Elles sont particulièrement utilisées dans les contextes de programmation fonctionnelle avec des fonctions d'ordre supérieur comme `map`, `filter` et `reduce`, où elles sont souvent passées en tant qu'arguments. N'oubliez pas que pour des opérations plus complexes, les fonctions régulières sont préférées pour leur lisibilité et leur maintenabilité.

## **Syntaxe des fonctions Lambda et utilisations de base**

```python
lambda arguments: expression

# pour lui donner un nom, assigner à une variable :
nom_de_la_fonction = lambda arguments: expression

# ceci est équivalent à :
def nom_de_la_fonction(arguments):
	return expression
```

Contrairement aux fonctions régulières définies avec `def`, les fonctions lambda sont limitées à une seule expression en raison de leur conception pour la simplicité et la brièveté. Elles peuvent prendre un ou plusieurs arguments mais ne peuvent pas contenir d'instructions ou plusieurs expressions.

Les fonctions lambda sont destinées à des opérations courtes et simples qui peuvent être écrites en une seule ligne.

Exemple :

```python
# Fonction régulière pour trouver la moyenne de trois nombres
def moyenne(x, y, z):
    return (x + y + z) / 3

# Fonction lambda pour trouver la moyenne de trois nombres
moyenne = lambda x, y, z: (x + y + z) / 3
```

Bien que les fonctions lambda ne puissent contenir qu'une seule expression, nous pouvons encore faire beaucoup avec elles.

Par exemple, voici une fonction lambda pour concaténer deux chaînes et les convertir en majuscules :

```python
concat_et_maj = lambda str1, str2: (f'La chaîne concaténée est {str1 + str2}'.upper())

print(concat_et_maj("bonjour", "monde"))  # Sortie : LA CHAÎNE CONCATÉNÉE EST BONJOURMONDE
```

## **Façons d'appeler les fonctions Lambda**

Il existe principalement trois façons d'utiliser ou d'appeler les fonctions lambda :

### **1. Assignation à une variable**

Assignez la fonction lambda à une variable puis appelez-la en utilisant cette variable :

```python
multiplier = lambda x, y: print(f'{x} * {y} = {x * y}')
multiplier(2, 10)  # Sortie : 2 * 10 = 20

ou

multiplier = lambda x, y: f'{x} * {y} = {x * y}'
print(multiplier(2, 10))  # Sortie : 2 * 10 = 20
```

### **2. Appel direct de la fonction Lambda**

Définissez et invoquez immédiatement la fonction lambda en enveloppant la définition dans des parenthèses et en fournissant les arguments directement :

```python
print((lambda x, y: f'{x} * {y} = {x * y}')(2, 10))  # Sortie : 2 * 10 = 20

ou

(lambda x, y: print(f'{x} * {y} = {x * y}'))(2, 10)  # Sortie : 2 * 10 = 20
```

### **3. Utilisation comme argument pour les fonctions d'ordre supérieur**

Les fonctions lambda sont souvent utilisées comme arguments pour les fonctions d'ordre supérieur comme `map`, `filter` et `reduce`.

Ce sont des fonctions qui prennent d'autres fonctions comme arguments. Elles aident à traiter des collections de données (comme des listes ou des tuples) dans un style de programmation fonctionnelle.

#### **Utilisation des fonctions lambda avec `map()`**

La fonction `map` applique une fonction spécifiée à chaque élément d'un itérable (comme une liste) et retourne un nouvel itérable avec les éléments mis à jour.

```python
# syntaxe

map(fonction, iterable)

```

* `fonction` ici prend un argument et retourne une valeur.
* Les éléments de l'itérable (par exemple, `list`, `tuple`) seront passés à la fonction.

Exemple :

```python
# Liste de paires de nombres
paires = [(2, 3), (4, 5), (6, 7)]

# Utilisation de la fonction lambda avec map pour multiplier chaque paire et afficher le résultat
list(map(lambda paire: print(f'{paire[0]} * {paire[1]} = {paire[0] * paire[1]}'), paires))
```

**Explication :** Dans ce code, nous utilisons une fonction lambda pour définir une petite fonction anonyme qui prend chaque paire de nombres et affiche leur multiplication.

La fonction `map` applique cette fonction lambda à chaque paire (tuple) dans la liste. En enveloppant l'appel de `map` avec `list`, nous nous assurons que la fonction lambda est exécutée pour chaque paire. En conséquence, le code affiche les résultats de multiplication pour chaque paire dans la liste, montrant des sorties comme "2 * 3 = 6", "4 * 5 = 20", et "6 * 7 = 42".

#### **Utilisation des fonctions lambda avec `filter()`**

La fonction `filter` filtre les éléments d'un itérable en fonction d'un prédicat spécifié. Seuls les éléments pour lesquels le prédicat retourne `True` sont inclus dans le nouvel itérable.

```python
# syntaxe

filter(predicat, iterable)
```

Le prédicat est une fonction qui prend un argument et retourne une valeur booléenne (True ou False). Les éléments de l'itérable seront testés par le prédicat.

Exemple :

```python
# Liste d'âges
ages = [25, 30, 18, 42, 17, 50, 22, 19]

# Fonction pour filtrer les adultes (âge 18 et plus) en utilisant filter avec lambda
adultes = filter(lambda age: age >= 18, ages)
print(list(adultes))  # Sortie : [25, 30, 18, 42, 50, 22, 19]
```

**Explication :** Dans ce code, nous commençons avec une liste d'âges. Nous utilisons une fonction lambda pour définir une condition simple qui vérifie si un âge est 18 ou plus.

La fonction `filter` applique cette fonction lambda à chaque âge dans la liste, filtrant les âges inférieurs à 18. En convertissant le résultat de `filter` en une liste, nous obtenons une liste d'âges qui sont 18 et plus. Enfin, nous affichons cette liste filtrée, ce qui donne les âges `[25, 30, 18, 42, 50, 22, 19]`, car ce sont les âges qui répondent au critère d'être 18 ou plus.

#### **Utilisation des fonctions lambda avec `reduce()`**

La fonction `reduce` applique une fonction spécifiée aux éléments d'un itérable de manière cumulative pour les réduire à une seule valeur. Elle fait partie du module `functools`.

```python
# syntaxe

from functools import reduce
reduce(fonction, iterable)

```

Ici, la fonction prend deux arguments et retourne une seule valeur. Les éléments de l'itérable seront traités par la fonction.

Exemple :

```python
from functools import reduce

# Liste de nombres
nombres = [1, 2, 3, 4, 5]

# Utilisation de reduce avec lambda pour additionner les nombres
somme_des_nombres = reduce(lambda x, y: x + y, nombres)
print(somme_des_nombres)  # Sortie : 15
```

**Explication :** Dans ce code, nous commençons avec une liste de nombres. Nous utilisons la fonction `reduce` du module `functools` pour calculer la somme de tous les nombres dans la liste. Nous utilisons une fonction lambda pour définir une simple opération d'addition qui prend deux arguments, `x` et `y`, et retourne leur somme. La fonction `reduce` applique cette fonction lambda de manière cumulative aux éléments de la liste, en commençant par la première paire et en continuant à travers toute la liste, comme ceci :

* Initialement, `x` est le premier élément de la liste (1) et `y` est le deuxième élément (2), ce qui donne 3.
* Cette somme (3) devient alors `x`, et le prochain élément de la liste (3) devient `y`, ce qui donne 6.
* Ce processus continue jusqu'à ce que tous les éléments de la liste aient été additionnés. Finalement, le résultat final est 15, représentant la somme de tous les nombres dans la liste [1, 2, 3, 4, 5].

## **Cas d'utilisation supplémentaires**

Les fonctions lambda peuvent également être utilisées dans le tri ou d'autres contextes de programmation fonctionnelle. Par exemple :

### **Tri d'une liste de chaînes :**

```python
villes = ["Inde", "Allemagne", "Amérique", "Japon"]
villes_triees = sorted(villes, key=lambda ville: ville.lower())

print(villes_triees)  # Sortie : ['Amérique', 'Allemagne', 'Inde', 'Japon']
```

Dans ce code, nous avons une liste appelée `villes` contenant les noms de différentes villes. Nous utilisons la fonction `sorted` pour trier ces noms de villes par ordre alphabétique, en ignorant la sensibilité à la casse. Le paramètre `key` dans la fonction `sorted` nous permet de spécifier une fonction (dans ce cas, une fonction lambda) pour personnaliser l'ordre de tri.

La fonction lambda `lambda ville: ville.lower()` convertit chaque nom de ville en minuscules avant le tri. Cela garantit que le tri est insensible à la casse, de sorte que les villes avec différentes capitalisations sont traitées de la même manière.

Après le tri, la liste triée est assignée à la variable `villes_triees`, et nous affichons le résultat. La sortie montre la liste triée des villes : `['Amérique', 'Allemagne', 'Inde', 'Japon']`, où les villes sont disposées par ordre alphabétique en ignorant la casse des lettres.

### **Fonctions Lambda dans les compréhensions de liste :**

Les fonctions lambda peuvent être utilisées dans les compréhensions de liste pour appliquer une fonction à chaque élément d'une liste.

**Exemple :**

```python
# Liste de nombres
nombres = [1, 2, 3, 4, 5]

# Utilisation de lambda dans la compréhension de liste pour élever au carré chaque nombre
nombres_au_carre = [(lambda x: x ** 2)(x) for x in nombres]
print(nombres_au_carre)  # Sortie : [1, 4, 9, 16, 25]
```

## **Conclusion**

Les fonctions lambda en Python offrent un moyen rapide et concis de créer de petites fonctions jetables. Elles sont particulièrement utiles en programmation fonctionnelle avec des fonctions d'ordre supérieur comme `map`, `filter` et `reduce`.

Bien que les fonctions lambda soient puissantes et concises, assurez-vous d'équilibrer leur utilisation avec la lisibilité et la maintenabilité du code. Pour une logique plus complexe, les fonctions régulières définies avec `def` sont préférées car elles supportent plusieurs expressions et instructions, et vous pouvez inclure de la documentation.

En comprenant et en utilisant efficacement les fonctions lambda, vous pouvez écrire un code Python plus concis et plus efficace.

**Merci d'avoir lu !** Si vous avez des commentaires, des critiques ou des questions, n'hésitez pas à tweeter ou à me contacter à @[OGsamyak](https://x.com/OGsamyak). Vos retours m'aident à m'améliorer !