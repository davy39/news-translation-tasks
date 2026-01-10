---
title: Exemple de la fonction range() en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2023-03-17T11:55:33.000Z'
originalURL: https://freecodecamp.org/news/python-range-function-example
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-christina-morillo-1181671.jpg
tags:
- name: Python
  slug: python
seo_title: Exemple de la fonction range() en Python
seo_desc: 'In this article, you will learn how to use the range() function in Python
  with the help of code examples along the way.

  What is the range() Function in Python? range() Function Syntax Breakdown

  Python''s built-in range() function is mainly used when w...'
---

Dans cet article, vous apprendrez à utiliser la fonction `range()` en Python à l'aide d'exemples de code tout au long du parcours.


## Qu'est-ce que la fonction `range()` en Python ? Décomposition de la syntaxe de la fonction `range()`
La fonction intégrée `range()` de Python est principalement utilisée lors du travail avec des boucles `for` – vous pouvez l'utiliser pour parcourir certains blocs de code un nombre spécifié de fois.

La fonction `range()` accepte trois arguments – un est obligatoire, et deux sont optionnels.

Par défaut, la syntaxe de la fonction `range()` ressemble à ceci :

```
range(stop)
```

L'argument `stop` est **obligatoire**. 

La fonction `range()` renvoie une séquence de nombres commençant à `0`, s'incrémentant de `1`, et se terminant à la valeur que vous spécifiez comme `stop` (non inclusif). 

Mais que faire si vous voulez itérer à travers une plage de deux nombres que vous spécifiez et que vous ne voulez pas commencer le comptage à partir de `0` ?

Vous pouvez passer un deuxième argument **optionnel**, `start`, pour spécifier le nombre de départ. La syntaxe pour le faire ressemble à ceci :
```
range(start, stop)
```

Cette syntaxe génère une séquence de nombres basée sur les valeurs `start` (inclusif) et `stop` (non inclusif) qui s'incrémentent de `1`.

Enfin, si vous ne voulez pas que l'incrément par défaut soit de `1`, vous pouvez spécifier un troisième argument **optionnel**, `step`. La syntaxe pour le faire ressemble à ceci :
```
range(start, stop, step)
```

Cette syntaxe génère une séquence de nombres qui commence à compter à `start` (inclusif) et s'incrémente selon `step` jusqu'à ce qu'elle atteigne `stop` (non inclusif).


## Comment utiliser la fonction `range()` avec seulement l'argument `stop` 
Lorsque vous utilisez uniquement l'argument `stop` avec `range()`, le comptage commence à `0` et s'incrémente de `1`. Le comptage s'arrête lorsque vous atteignez la valeur que vous spécifiez comme `stop`. 

Gardez à l'esprit que la valeur `stop` que vous spécifiez n'est pas inclusive !

Si vous spécifiez un argument `stop` de `5`, la plage comprend les nombres `0 - 4` et non `0 - 5` – le comptage s'arrêtera à `4` et non à `5`.

Jetons un coup d'œil à l'exemple ci-dessous :
```python
for num in range(5):
    print(num)
    
# sortie 

# 0
# 1
# 2
# 3
# 4
```

Dans cet exemple, j'ai spécifié un `range(5)`.

La fonction a commencé à compter à partir de `0`, s'est incrémentée de `1` à chaque itération et s'est terminée à `4`.


## Comment utiliser la fonction `range()` avec les arguments `start` et `stop` 
Si vous voulez avoir une plage de deux nombres, vous utilisez deux arguments – `start` et `stop`. Gardez à l'esprit que la valeur `start` est inclusive, tandis que la valeur `stop` ne l'est pas.

Si vous voulez une plage de valeurs de 5 inclus à 10 inclus, vous écrivez un `range(5,11)` comme ceci :
```python
for num in range(5,11):
  print(num)
  
# sortie

# 5
# 6
# 7
# 8
# 9
# 10
```

Vous pouvez également passer des valeurs entières négatives à `range()` :
```python
for num in range(-5, 1):
  print(num)

# sortie

# -5
# -4
# -3
# -2
# -1
# 0
```

Quelque chose à noter ici est que vous ne pouvez pas passer de valeurs de type float (flottants) à `range()`.

Dans cet exemple, quand je passe deux valeurs flottantes comme arguments, une erreur est levée :
```python
for num in range(5.2, 4.3):
  print(num)

# sortie

# Traceback (most recent call last):
#  File "main.py", line 1, in <module>
#    for num in range(5.2, 4.3):
# TypeError: 'float' object cannot be interpreted as an integer
```
   
Vous pouvez passer des entiers négatifs ou positifs comme arguments `start` et `stop`.


## Comment utiliser la fonction `range()` avec les arguments `start`, `stop` et `step` 
Par défaut, la valeur d'incrément est `1` et n'est pas spécifiée. Cela dit, vous pouvez la modifier en passant un argument `step` à la fonction `range()`.

Jetons un coup d'œil à l'exemple suivant :
```python
for num in range(10,21,2):
  print(num)
  
# sortie

# 10
# 12
# 14
# 16
# 18
# 20
```

Dans l'exemple ci-dessus, j'ai généré une séquence de nombres de `10` à `20` et j'ai incrémenté les étapes de `2`. J'ai réalisé cela en spécifiant une valeur de pas (`step`) de `2`.

Une chose à noter est que `step` peut être un nombre négatif ou positif, mais il ne peut pas être `0`.

Voici comment vous pouvez générer une plage avec un argument `step` négatif :
```python
for num in range(20, 11, -2):
  print(num)

# sortie

# 20
# 18
# 16
# 14
# 12
```

Le code ci-dessus génère une séquence de nombres en sens inverse.

Et regardez ce qui se passe quand le `step` est `0` :
```python
for num in range(10, 21, 0):
  print(num)

# sortie

#  File "main.py", line 1
#    for num in range(10, 21, 0):
# ValueError: range() arg 3 must not be zero
```


## Comment créer une liste de nombres en utilisant la fonction `range()` 
Vous pouvez créer une liste de nombres en passant la fonction `range()` comme argument au constructeur `list()` comme ceci :

```python
my_numbers_list = list(range(5))

print(my_numbers_list)

# sortie

# [0, 1, 2, 3, 4]
```
    
Dans l'exemple ci-dessus, j'ai créé une liste de nombres de `0` à `4`.


## Comment utiliser la fonction `len()` avec `range()` en Python 
Supposons que vous ayez une liste d'éléments et que vous vouliez faire quelque chose sur les éléments en fonction de la longueur de la liste.

Pour cela, vous pourriez utiliser `range()` et passer la longueur de votre liste comme argument à la fonction.

Pour calculer la longueur d'une liste, utilisez la fonction `len()`.

```python
programming_languages = ["Python", "JavaScript", "Java", "C++"]

programming_languages_length = len(programming_languages)

for languages in range(programming_languages_length):
  print("Hello World")
  
# sortie

# Hello World
# Hello World
# Hello World
# Hello World
```

## Conclusion
Et voilà ! Vous savez maintenant comment utiliser la fonction `range()` en Python.

Pour en savoir plus sur Python, consultez le [cours Python pour débutants](https://www.freecodecamp.org/news/python-programming-course/) de freeCodeCamp.

Merci de votre lecture, et bon codage !