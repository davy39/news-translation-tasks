---
title: Slicing et indexation en Python – Explications avec exemples
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-29T14:26:25.000Z'
originalURL: https://freecodecamp.org/news/slicing-and-indexing-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/Sabi.JPG
tags: []
seo_title: Slicing et indexation en Python – Explications avec exemples
seo_desc: 'Slicing and indexing are two fundamental concepts in Python. They help
  you access specific elements in a sequence, such as a list, tuple or string.

  By using these techniques, you can extract substrings from strings, filter lists,
  and extract columns ...'
---

Le slicing et l'indexation sont deux concepts fondamentaux en Python. Ils vous aident à accéder à des éléments spécifiques dans une séquence, telle qu'une liste, un tuple ou une chaîne de caractères.

En utilisant ces techniques, vous pouvez extraire des sous-chaînes de chaînes de caractères, filtrer des listes et extraire des colonnes de listes 2D, entre autres.

Comprendre comment utiliser le slicing et l'indexation est essentiel pour travailler avec des données en Python, explorons donc ces concepts en détail et fournissons des exemples concrets pour vous aider à comprendre comment ils fonctionnent.

## L'indexation en Python

L'indexation est le processus d'accès à un élément dans une séquence en utilisant sa position dans la séquence (son index).

En Python, l'indexation commence à 0, ce qui signifie que le premier élément d'une séquence est à la position 0, le deuxième élément à la position 1, et ainsi de suite.

Pour accéder à un élément dans une séquence, vous pouvez utiliser des crochets `[]` avec l'index de l'élément auquel vous souhaitez accéder.

Considérons l'exemple suivant :

```python
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[0]) # sortie : 'apple'
print(my_list[1]) # sortie : 'banana'
```

Dans le code ci-dessus, nous avons créé une liste appelée `my_list`, puis nous avons utilisé l'indexation pour accéder aux premier et deuxième éléments de la liste en utilisant leurs index respectifs.

## Le slicing en Python

Le slicing est le processus d'accès à une sous-séquence d'une séquence en spécifiant un index de début et un index de fin. En Python, vous effectuez le slicing en utilisant l'opérateur deux-points `:`. La syntaxe pour le slicing est la suivante :

```python
sequence[start_index:end_index]
```

où `start_index` est l'index du premier élément de la sous-séquence et `end_index` est l'index du dernier élément de la sous-séquence (en excluant l'élément à l'index `end_index`). Pour découper une séquence, vous pouvez utiliser des crochets `[]` avec les index de début et de fin séparés par un deux-points.

Par exemple :

```python
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[1:3]) # sortie : ['banana', 'cherry']
```

Dans le code ci-dessus, nous avons utilisé le slicing pour accéder à une sous-séquence de `my_list` contenant les deuxième et troisième éléments.

Vous pouvez également omettre soit le `start_index`, soit l' `end_index` dans un slice pour obtenir tous les éléments depuis le début ou jusqu'à la fin de la séquence. Par exemple :

```python
my_list = ['apple', 'banana', 'cherry', 'date']
print(my_list[:2]) # sortie : ['apple', 'banana']
print(my_list[2:]) # sortie : ['cherry', 'date']
```

Dans la première ligne du code ci-dessus, nous avons utilisé le slicing pour obtenir tous les éléments depuis le début de `my_list` jusqu'à (mais sans inclure) l'élément à l'index 2. Dans la deuxième ligne, nous avons utilisé le slicing pour obtenir tous les éléments de l'index 2 jusqu'à la fin de `my_list`.

## Exemples de slicing et d'indexation en Python

Jetons un coup d'œil à quelques exemples concrets de la façon dont vous pouvez utiliser le slicing et l'indexation en Python.

### Exemple 1 : Comment extraire des sous-chaînes d'une chaîne de caractères

Supposons que nous ayons une phrase sous forme de chaîne de caractères et que nous voulions en extraire le premier mot. Nous pouvons le faire en utilisant l'indexation comme suit :

```python
sentence = "The quick brown fox jumps over the lazy dog"
first_word = sentence[:3]
print(first_word) # sortie : "The"
```

Dans le code ci-dessus, nous avons utilisé l'indexation pour extraire les trois premiers caractères de la chaîne `sentence`, qui correspondent au premier mot. La syntaxe `[:3]` signifie que nous sélectionnons tous les caractères depuis le début de la chaîne jusqu'à (mais sans inclure) le caractère à l'index 3.

Nous pourrions également extraire les deuxième et troisième mots de la phrase en utilisant le slicing comme suit :

```python
second_word = sentence[4:9]
third_word = sentence[10:15]
print(second_word) # sortie : "quick"
print(third_word) # sortie : "brown"
```

Dans ces exemples, nous avons utilisé le slicing pour extraire une plage de caractères de la chaîne `sentence`. Le slice `4:9` signifie que nous sélectionnons les caractères commençant à l'index 4 (inclus) jusqu'à l'index 9 (exclus), ce qui correspond au deuxième mot "quick". De même, le slice `10:15` signifie que nous sélectionnons les caractères commençant à l'index 10 jusqu'à l'index 15 (exclus), ce qui correspond au troisième mot "brown".

### Exemple 2 : Comment filtrer une liste

Supposons que nous ayons une liste de nombres et que nous voulions extraire tous les nombres impairs de la liste. Nous pouvons le faire en utilisant le slicing comme suit :

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = numbers[::2]
print(odd_numbers) # sortie : [1, 3, 5, 7, 9]
```

Dans le code ci-dessus, nous avons utilisé le slicing pour extraire tous les nombres impairs de la liste `numbers`. Le slice `::2` signifie que nous sélectionnons un élément sur deux en commençant par le premier élément, ce qui correspond aux nombres impairs de la liste. Puisque nous ne voulons que les nombres impairs, nous commençons par le premier élément (index 0), puis nous sélectionnons un élément sur deux après cela.

Nous pourrions également extraire tous les nombres pairs de la liste en utilisant le slicing comme suit :

```python
even_numbers = numbers[1::2]
print(even_numbers) # sortie : [2, 4, 6, 8]
```

Dans cet exemple, nous avons utilisé le slicing pour extraire un élément sur deux en commençant par le deuxième élément (index 1), ce qui correspond aux nombres pairs de la liste.

### Exemple 3 : Comment extraire des colonnes d'une liste 2D

Supposons que nous ayons une liste 2D représentant un tableau de données et que nous voulions extraire une colonne particulière du tableau. Nous pouvons le faire en utilisant la compréhension de liste et l'indexation comme suit :

```python
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
column = [row[1] for row in data]
print(column) # sortie : [2, 5, 8]
```

Dans le code ci-dessus, nous avons utilisé la compréhension de liste pour extraire le deuxième élément (index 1) de chaque ligne de la liste `data`, puis nous avons combiné ces éléments dans une nouvelle liste appelée `column`. La syntaxe `row[1]` signifie que nous sélectionnons le deuxième élément de chaque ligne, ce qui correspond à la deuxième colonne du tableau.

Nous pourrions également extraire d'autres colonnes du tableau en changeant l'index utilisé dans la compréhension de liste, par exemple :

```python
column_0 = [row[0] for row in data]
column_2 = [row[2] for row in data]
print(column_0) # sortie : [1, 4, 7]
print(column_2) # sortie : [3, 6, 9]
```

Dans ces exemples, nous avons utilisé l'indexation pour sélectionner les premier et troisième éléments de chaque ligne, ce qui correspond aux première et troisième colonnes du tableau.

### Exemple 4 : Comment modifier des parties d'une liste

Supposons que nous ayons une liste de nombres et que nous voulions modifier les valeurs de certains éléments de la liste. Nous pouvons le faire en utilisant le slicing comme suit :

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[1:4] = [10, 20, 30]
print(numbers) # sortie : [1, 10, 20, 30, 5, 6, 7, 8, 9]
```

Dans le code ci-dessus, nous avons utilisé le slicing pour sélectionner une plage d'éléments de la liste `numbers` (index 1 à 3), puis nous avons remplacé ces éléments par une nouvelle liste `[10, 20, 30]`. Le résultat est que les éléments aux index 1 à 3 de la liste `numbers` ont été remplacés par les nouvelles valeurs.

Nous pourrions également insérer de nouveaux éléments dans la liste en utilisant le slicing comme suit :

```python
numbers[4:4] = [40, 50]
print(numbers) # sortie : [1, 10, 20, 30, 40, 50, 5, 6, 7, 8, 9]
```

Dans cet exemple, nous avons utilisé le slicing pour insérer une nouvelle liste `[40, 50]` à l'index 4 de la liste `numbers`. Le slice `4:4` signifie que nous insérons la nouvelle liste à l'index 4 (c'est-à-dire avant l'élément à l'index 4), sans supprimer d'éléments existants.

## Conclusion

Dans cet article, nous avons discuté des concepts de slicing et d'indexation en Python et fourni plusieurs exemples de la façon dont ils peuvent être utilisés pour manipuler des listes et des chaînes de caractères.

Le slicing et l'indexation sont des outils puissants qui peuvent grandement simplifier certaines tâches en programmation Python, telles que la sélection de sous-ensembles de données, la modification de listes et l'extraction de sous-chaînes. En comprenant ces concepts et en les utilisant efficacement dans votre code, vous pouvez devenir un programmeur Python plus efficace et performant.