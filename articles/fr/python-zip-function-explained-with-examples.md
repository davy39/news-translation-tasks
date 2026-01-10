---
title: La fonction zip() de Python expliquée avec des exemples simples
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-10-10T14:58:09.603Z'
originalURL: https://freecodecamp.org/news/python-zip-function-explained-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728351007032/90a321bb-4079-4480-90e7-7aa847c54d9d.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
- name: python beginner
  slug: python-beginner
- name: programming languages
  slug: programming-languages
seo_title: La fonction zip() de Python expliquée avec des exemples simples
seo_desc: 'The zip() function in Python is a neat tool that allows you to combine
  multiple lists or other iterables (like tuples, sets, or even strings) into one
  iterable of tuples. Think of it like a zipper on a jacket that brings two sides
  together.

  In this g...'
---

La fonction `zip()` en Python est un outil pratique qui permet de combiner plusieurs listes ou autres itérables (comme des tuples, des ensembles, ou même des chaînes de caractères) en un seul itérable de tuples. Imaginez-la comme une fermeture éclair sur une veste qui rassemble deux côtés.

Dans ce guide, nous explorerons les tenants et aboutissants de la fonction `zip()` avec des exemples simples et pratiques qui vous aideront à comprendre comment l'utiliser efficacement.

## Comment fonctionne la fonction `zip()` ?

La fonction `zip()` associe les éléments de plusieurs itérables, comme des listes, en fonction de leur position. Cela signifie que les premiers éléments de chaque liste seront associés, puis les deuxièmes, et ainsi de suite. Si les itérables n'ont pas la même longueur, `zip()` s'arrêtera à la fin de l'itérable le plus court.

La syntaxe de `zip()` est assez simple :

```python
zip(*iterables)
```

Vous pouvez passer plusieurs itérables (listes, tuples, etc.), et il les combinera en tuples.

### Exemple 1 : Combinaison de deux listes

Commençons par un cas simple où nous avons deux listes et nous voulons les combiner. Imaginez que vous avez une liste de noms et une liste correspondante de scores, et que vous souhaitez les associer.

```python
# Deux listes à combiner
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]

# Utilisation de zip() pour les combiner
zipped = zip(names, scores)

# Conversion du résultat en liste pour le visualiser
zipped_list = list(zipped)
print(zipped_list)
```

Dans cet exemple, la fonction `zip()` prend les deux listes — `names` et `scores` — et les associe élément par élément. Le premier élément de `names` (`"Alice"`) est associé au premier élément de `scores` (`85`), et ainsi de suite. Lorsque nous convertissons le résultat en liste, cela ressemble à ceci :

**Sortie :**

```python
[('Alice', 85), ('Bob', 90), ('Charlie', 88)]
```

Cela facilite le travail avec des données liées de manière structurée.

### Exemple 2 : Que se passe-t-il lorsque les listes sont de longueurs différentes ?

Supposons que vous avez des listes de longueurs différentes. Que se passe-t-il alors ? La fonction `zip()` est assez intelligente pour s'arrêter dès qu'elle atteint la fin de la liste la plus courte.

```python
# Listes de longueurs différentes
fruits = ["apple", "banana"]
prices = [100, 200, 150]

# Zippage ensemble
result = list(zip(fruits, prices))
print(result)
```

Dans ce cas, la liste `fruits` a deux éléments, et la liste `prices` en a trois. Mais `zip()` ne combinera que les deux premiers éléments, ignorant la valeur supplémentaire dans `prices`.

**Sortie :**

```python
[('apple', 100), ('banana', 200)]
```

Remarquez comment la dernière valeur (`150`) dans la liste `prices` est ignorée car il n'y a pas de troisième fruit pour l'associer. La fonction `zip()` garantit que vous n'obtenez pas d'erreurs lorsque vous travaillez avec des listes de longueurs inégales, mais cela signifie également que vous pourriez perdre certaines données si vos listes ne sont pas équilibrées.

### Exemple 3 : Dézippage d'un objet zippé

Que faire si vous souhaitez inverser l'opération `zip()` ? Par exemple, après avoir zippé deux listes ensemble, vous pourriez vouloir les séparer à nouveau en listes individuelles. Vous pouvez le faire facilement en utilisant l'opérateur de déballage `*`.

```python
# Listes zippées
cities = ["New York", "London", "Tokyo"]
populations = [8000000, 9000000, 14000000]

zipped = zip(cities, populations)

# Dézippage
unzipped_cities, unzipped_populations = zip(*zipped)

print(unzipped_cities)
print(unzipped_populations)
```

Ici, nous zippons d'abord les listes `cities` et `populations` ensemble. Ensuite, en utilisant `zip(*zipped)`, nous pouvons "dézipper" les tuples combinés en deux listes séparées. L'opérateur `*` déballage les tuples zippés en leurs composants d'origine.

**Sortie :**

```python
('New York', 'London', 'Tokyo')
(8000000, 9000000, 14000000)
```

Cela montre comment vous pouvez inverser le processus de zippage pour récupérer les données originales.

### Exemple 4 : Zippage de plus de deux listes

Vous n'êtes pas limité à seulement deux listes avec `zip()`. Vous pouvez zipper autant d'itérables que vous le souhaitez. Voici un exemple avec trois listes.

```python
# Trois listes à zipper
subjects = ["Math", "English", "Science"]
grades = [88, 79, 92]
teachers = ["Mr. Smith", "Ms. Johnson", "Mrs. Lee"]

# Zippage de trois listes ensemble
zipped_info = zip(subjects, grades, teachers)

# Conversion en liste pour voir le résultat
print(list(zipped_info))
```

Dans cet exemple, nous zippons trois listes — `subjects`, `grades`, et `teachers`. Le premier élément de chaque liste est regroupé ensemble, puis le deuxième, et ainsi de suite.

**Sortie :**

```python
[('Math', 88, 'Mr. Smith'), ('English', 79, 'Ms. Johnson'), ('Science', 92, 'Mrs. Lee')]
```

De cette manière, vous pouvez combiner plusieurs informations liées en tuples faciles à manipuler.

### Exemple 5 : Zippage de chaînes de caractères

Les chaînes de caractères sont également des itérables en Python, donc vous pouvez les zipper comme vous le feriez avec des listes. Essayons de combiner deux chaînes.

```python
# Zippage de deux chaînes
str1 = "ABC"
str2 = "123"

# Zippage des caractères ensemble
zipped_strings = list(zip(str1, str2))
print(zipped_strings)
```

Ici, le premier caractère de `str1` est combiné avec le premier caractère de `str2`, et ainsi de suite.

**Sortie :**

```python
[('A', '1'), ('B', '2'), ('C', '3')]
```

Cela est particulièrement utile si vous devez traiter ou associer des caractères de plusieurs chaînes ensemble.

### Exemple 6 : Zippage de dictionnaires

Bien que les dictionnaires soient légèrement différents des listes, vous pouvez toujours utiliser `zip()` pour les combiner. Par défaut, `zip()` ne zippera que les clés des dictionnaires. Voici un exemple :

```python
# Deux dictionnaires
dict1 = {"name": "Alice", "age": 25}
dict2 = {"name": "Bob", "age": 30}

# Zippage des clés des dictionnaires
zipped_keys = list(zip(dict1, dict2))
print(zipped_keys)
```

Ici, `zip()` associe les clés des deux dictionnaires.

**Sortie :**

```python
[('name', 'name'), ('age', 'age')]
```

Si vous souhaitez zipper les valeurs des dictionnaires, vous pouvez le faire en utilisant la méthode `.values()` :

```python
zipped_values = list(zip(dict1.values(), dict2.values()))
print(zipped_values)
```

**Sortie :**

```python
[('Alice', 'Bob'), (25, 30)]
```

Maintenant, vous pouvez facilement combiner les valeurs des deux dictionnaires.

### Exemple 7 : Utilisation de `zip()` dans les boucles

L'une des utilisations les plus courantes de `zip()` est dans les boucles lorsque vous souhaitez traiter plusieurs listes en même temps. Voici un exemple :

```python
# Listes de noms et de scores
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 88]

# Utilisation de zip() dans une boucle
for name, score in zip(names, scores):
    print(f"{name} a obtenu {score}")
```

Cette boucle itère sur les listes `names` et `scores` simultanément, associant chaque nom à son score correspondant.

**Sortie :**

```python
Alice a obtenu 85
Bob a obtenu 90
Charlie a obtenu 88
```

L'utilisation de `zip()` dans des boucles comme celle-ci rend votre code plus propre et plus facile à lire lorsque vous travaillez avec des données liées.

## Conclusion

La fonction `zip()` est un outil pratique en Python qui permet de combiner plusieurs itérables en tuples, facilitant ainsi le travail avec des données liées. Que vous associiez des éléments de listes, de tuples ou de chaînes de caractères, `zip()` simplifie votre code et peut être particulièrement utile dans les boucles.

Avec les exemples de cet article, vous devriez maintenant bien comprendre comment utiliser `zip()` dans divers scénarios.

Si vous avez trouvé cette explication de la fonction `zip()` de Python utile, vous pourriez également apprécier des tutoriels et concepts de programmation plus approfondis que je couvre sur mon [blog](https://blog.theenthusiast.dev).

Bon codage !