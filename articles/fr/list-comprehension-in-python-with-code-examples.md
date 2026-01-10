---
title: Compréhension de liste en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-11-18T16:20:35.000Z'
originalURL: https://freecodecamp.org/news/list-comprehension-in-python-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/christian-wiediger-WkfDrhxDMC8-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Compréhension de liste en Python
seo_desc: "Lists are a helpful and frequently used feature in Python. \nAnd list comprehension\
  \ gives you a way to create lists while writing more elegant code that is easy to\
  \ read.\nIn this beginner-friendly article, I'll give an overview of how list comprehensio..."
---

Les listes sont une fonctionnalité utile et fréquemment utilisée en Python. 

Et la compréhension de liste vous donne un moyen de créer des listes tout en écrivant un code plus élégant et facile à lire.

Dans cet article adapté aux débutants, je vais donner un aperçu de la façon dont la compréhension de liste fonctionne en Python. Je vais également montrer de nombreux exemples de code tout au long de l'article.

Commençons !

## Comment utiliser une boucle `for` pour créer une liste en Python

Une façon de créer une liste en Python est d'utiliser une boucle `for`.

Par exemple, vous pouvez utiliser la fonction `range()` pour créer une liste de nombres allant de 0 à 4.

```python
# d'abord créer une liste vide
my_list = []

# itérer sur les nombres 0 - 4 en utilisant la fonction range()
# range(5) crée un itérable, commençant de 0 jusqu'à (mais n'incluant pas) 5
# Utiliser la méthode .append() pour ajouter les nombres 0 - 4 à my_list

for num in range(5):
    my_list.append(num)
    
# imprimer my_list
print(my_list)

# sortie
# [0, 1, 2, 3, 4]
```

Et si vous avez déjà une liste de nombres, mais que vous voulez créer une nouvelle liste avec leurs carrés ?

Vous pourriez à nouveau utiliser une boucle `for`, comme ceci :

```python
# liste initiale de nombres
numbers = [1,2,3,4,5,6]

# créer une nouvelle liste vide pour contenir leurs carrés
square_numbers = []

# itérer sur la liste initiale
# multiplier chaque nombre par lui-même
# utiliser la méthode .append(), pour ajouter le carré à la nouvelle liste, square_numbers

for num in numbers: 
    square_numbers.append(num * num)

# imprimer la nouvelle liste
print(square_numbers)

# sortie
# [1, 4, 9, 16, 25, 36]
```

Mais il existe une méthode plus rapide et plus succincte pour obtenir les mêmes résultats – en utilisant la compréhension de liste.

## Qu'est-ce que la compréhension de liste en Python ? Un aperçu de la syntaxe

Lorsque vous analysez et travaillez avec des listes en Python, vous devrez souvent manipuler, modifier ou effectuer des calculs sur chaque élément de la liste, tout à la fois.

Vous devrez peut-être également créer de nouvelles listes à partir de zéro, ou créer une nouvelle liste basée sur les valeurs d'une liste déjà existante.

La compréhension de liste est un moyen rapide, court et élégant de créer des listes par rapport à d'autres méthodes itératives, comme les boucles `for`.

La syntaxe générale de la compréhension de liste ressemble à ceci :

```
new_list = [expression for variable in iterable]
```

Décomposons cela :

- Les compréhensions de liste commencent et se terminent par des crochets ouvrants et fermants, `[]`.
- Ensuite vient l'`expression` ou l'opération que vous souhaitez effectuer et réaliser sur chaque valeur à l'intérieur de l'itérable actuel. Les résultats de ces calculs entrent dans la nouvelle liste.
- L'`expression` est suivie d'une clause `for`.
- `variable` est un nom temporaire que vous souhaitez utiliser pour chaque élément dans la liste actuelle qui passe par l'itération.
- Le mot-clé `in` est utilisé pour boucler sur l'itérable.
- `iterable` peut être n'importe quel objet Python, tel qu'une liste, un tuple, une chaîne de caractères et ainsi de suite.
- À partir de l'itération qui a été effectuée et des calculs qui ont eu lieu sur chaque élément pendant l'itération, de nouvelles valeurs ont été créées qui sont sauvegardées dans une variable, dans ce cas `new_list`. **L'ancienne liste (ou autre objet) restera inchangée**.
- Il peut y avoir une instruction `if` optionnelle et une clause `for` supplémentaire.

## Comment utiliser la compréhension de liste en Python

En utilisant le même exemple que précédemment, voici comment vous créeriez une nouvelle liste de nombres de 0 à 4 avec la fonction `range()` en une seule ligne, en utilisant la compréhension de liste :

```python
new_list = [num for num in range(5)]

print(new_list)

# sortie
# [0, 1, 2, 3, 4]
```

Cela donne la même sortie que l'exemple avec la boucle `for`, mais avec significativement moins de code !

Décomposons cela :

- l'itérable dans ce cas est une séquence de nombres de 0 à 4, en utilisant `range(5)`. `range()` construit une liste de nombres.
- Vous utilisez le mot-clé `in` pour itérer sur les nombres.
- Le `num` suivant la clause `for` est une variable, un nom temporaire pour chaque valeur dans l'itérable. Donc `num` serait égal à `0` dans la première itération, puis `num` serait égal à `1` dans l'itération suivante et ainsi de suite, jusqu'à ce qu'il atteigne et soit égal au nombre 4, où l'itération s'arrêterait.
- Le `num` avant la clause `for` est une expression pour chaque élément dans la séquence.
- Enfin, la nouvelle liste (ou autre itérable) qui est créée est stockée dans la variable `new_list`.

Vous pouvez même effectuer des opérations mathématiques sur les éléments contenus dans l'itérable et le résultat sera ajouté à la nouvelle liste :

```python
new_list = [num * 2 for num in range(5)]

print(new_list)

# sortie
# [0, 2, 4, 6, 8]
```

Ici, chaque nombre dans `range(5)` sera multiplié par deux et la nouvelle valeur sera stockée dans la variable `new_list`.

Et si vous aviez une liste préexistante où vous souhaiteriez manipuler et modifier chaque élément ? Cela serait similaire à l'exemple précédent, où nous avons créé une liste de carrés.

Encore une fois, vous pouvez y parvenir avec une seule ligne de code, en utilisant la compréhension de liste :

```python
# liste initiale
numbers = [1,2,3,4,5,6]

# nouvelle liste
# num * num est l'opération qui a lieu pour créer les carrés

square_numbers = [num * num for num in numbers]

print(square_numbers)

# sortie
# [1, 4, 9, 16, 25, 36]
```

### Comment utiliser des conditionnelles avec la compréhension de liste en Python

Optionnellement, vous pouvez utiliser une instruction `if` avec une compréhension de liste.

La syntaxe générale ressemble à ceci :

```
new_list = [expression for variable in iterable if condition == True]
```

Les conditionnelles agissent comme un filtre et ajoutent une vérification supplémentaire pour une précision et une personnalisation supplémentaires lors de la création d'une nouvelle liste.

Cela signifie que la valeur dans l'expression doit répondre à certains critères et à une certaine condition que vous spécifiez, afin d'entrer dans la nouvelle liste.

```python
new_list = [num for num in range(50) if num % 2 == 0]

print(new_list)

# sortie
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
```

Dans l'exemple ci-dessus, seules les valeurs où la condition `num % 2 == 0` est vérifiée et évaluée à True entreront dans `new_list`.

L'opérateur modulo est utilisé sur chacun des nombres dans la séquence de nombres commençant de 0 et se terminant à 49.

Si le reste des nombres lorsqu'ils sont divisés par 2 est 0, alors et seulement alors il entre dans la liste.

Donc dans ce cas, cela crée une liste de nombres pairs uniquement.

Vous pouvez ensuite la rendre aussi spécifique que vous le souhaitez.

Par exemple, vous pourriez ajouter plus d'une condition, comme ceci :

```python
new_list = [num for num in range(50) if  num > 20 and num % 2 == 0]

print(new_list)

# sortie
# [22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
```

Dans cet exemple, il y a deux conditions `num > 20` et `num % 2 == 0`. 

L'opérateur `and` indique que *les deux* doivent être satisfaites pour que la valeur soit ajoutée à la nouvelle liste.

Les valeurs qui ne satisfont pas les conditions sont exclues et ne sont pas ajoutées.

### Comment utiliser la compréhension de liste sur les chaînes de caractères en Python

Vous pouvez créer une nouvelle liste avec les caractères individuels contenus dans une chaîne de caractères donnée.

```python
fave_language_chars = [letter for letter in "Python"]

print(fave_language_chars)

# sortie
# ['P', 'y', 't', 'h', 'o', 'n']
```

La nouvelle liste qui est créée est composée de toutes les lettres séparées contenues dans la chaîne "Python", qui agit comme un itérable.

Tout comme les nombres, vous pouvez effectuer des opérations sur les caractères contenus dans une chaîne et les personnaliser en fonction de la manière dont vous souhaitez qu'ils soient dans la nouvelle liste que vous créez.

Si vous souhaitez que toutes les lettres soient en majuscules, vous feriez ce qui suit :

```python
fave_language_chars_upper = [letter.upper() for letter in "Python"]

print(fave_language_chars_upper)

# sortie
# ['P', 'Y', 'T', 'H', 'O', 'N']
```

Ici, vous utilisez la méthode `.upper()` pour convertir chaque lettre de "Python" en majuscules et les ajouter à la variable `fave_language_chars_upper`.

Il en va de même si vous souhaitez que toutes vos lettres soient en minuscules - vous utiliseriez plutôt la méthode `lower()`.

## Conclusion

Et voilà ! Vous connaissez maintenant les bases de la compréhension de liste en Python.

Elle offre une syntaxe élégante et concise pour créer de nouvelles listes basées sur des listes existantes ou d'autres itérables.

Si vous êtes intéressé à en apprendre davantage sur Python, freeCodeCamp propose une [Certification Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

Dans ce programme basé sur des projets, vous commencerez par apprendre les bases de la programmation et progresserez vers des sujets plus complexes tels que les structures de données. Vous construirez également cinq projets pour mettre en pratique ce que vous avez appris.

Merci d'avoir lu et bon codage !