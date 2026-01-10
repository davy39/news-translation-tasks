---
title: Fonctions Python any() et all() – Expliquées avec des Exemples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-08-10T20:26:25.000Z'
originalURL: https://freecodecamp.org/news/python-any-and-all-functions-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/POINTERS-IN-c--8-.png
tags:
- name: Python
  slug: python
seo_title: Fonctions Python any() et all() – Expliquées avec des Exemples
seo_desc: 'When coding in Python, have you ever had to check if any item or all items
  in an iterable evaluate to True? The next time you need to do so, be sure to use
  the nifty functions any() and all().

  In this tutorial, we''ll learn about Python''s any() and al...'
---

Lorsque vous codez en Python, avez-vous déjà dû vérifier si _n'importe quel_ élément ou _tous_ les éléments d'un itérable évaluent à `True` ? La prochaine fois que vous en aurez besoin, assurez-vous d'utiliser les fonctions pratiques `any()` et `all()`.

Dans ce tutoriel, nous allons apprendre les fonctions `any()` et `all()` de Python et utiliser des exemples simples pour comprendre comment elles fonctionnent.

## Le type de données Booléen en Python

Avant de plonger dans `any()` et `all()`, revisitons rapidement le type de données booléen en Python. Vous pouvez appeler `bool()` sur n'importe quel objet Python pour obtenir sa valeur de vérité. Vous pouvez exécuter les exemples de code ci-dessous dans votre IDE préféré.

```python
# valeur de vérité de None est False
print(bool(None))
# Sortie
False

# valeur de vérité d'une chaîne vide ("") est False
print(bool(""))
# Sortie
False

# valeur de vérité d'une liste vide (ou de tout itérable) est False
print(bool([]))
# Sortie
False

# valeur de vérité de 0 {int (0), float (0.0) et complexe (0j)} est False
print(bool(0))
# Sortie
False
```

Comme montré dans l'extrait ci-dessus,

* `None` a une valeur de vérité de `False`,
* Le nombre zéro (`0`) – entier, flottant et représentation complexe de `0` – ont tous une valeur de vérité de `False`, et
* Tous les itérables vides comme les listes, les tuples et les chaînes ont une valeur de vérité de `False`.

Cela dit, il est assez intuitif que toutes les valeurs _non nulles_, et les itérables _non vides_ ont une valeur de vérité de `True`.

## Comment utiliser la fonction any() en Python

Comprenons la syntaxe de la fonction `any()`, regardons quelques exemples simples, puis passons à des exemples plus utiles.

**👉 Syntaxe** : `any(iterable)`

* Retourne `True` si `bool(x)` est `True` pour n'importe quel `x` dans l'itérable.
* Retourne `False` si l'itérable est vide.

Par conséquent, la fonction `any()` prend un itérable comme argument et retourne `True` tant qu'au moins un des éléments de l'itérable est `True`.

Voici quelques exemples simples pour vérifier comment la fonction `any()` fonctionne :

```python
list_1 = [0,0,0,1,0,0,0,0]
# any(une liste avec au moins une entrée non nulle) retourne True
print(any(list_1))
# Sortie
True

list_2 = [0j,0,0,0.0,0,0,0.0,0]
# any(une liste de zéros) retourne False
print(any(list_2))
# Sortie
False

list_3 = [True, False, False]
# any(une liste avec au moins une valeur True) retourne True
print(any(list_3))
# Sortie
True

list_4 = ["","","code more"]
# any(une liste avec au moins une chaîne non vide) retourne True
print(any(list_4))
# Sortie
True

list_5 = ["","",""]
# any(une liste de chaînes vides) retourne False
print(any(list_5))
# Sortie
False


```

### Comment utiliser la fonction any() de Python pour vérifier la présence de chiffres dans une chaîne

Utilisons maintenant la fonction `any()` pour vérifier s'il y a des chiffres dans une chaîne. Écrivons les étapes.

* À vérifier : Y a-t-il des chiffres dans la chaîne ?
* Parcourez la chaîne pour accéder à chaque caractère de la chaîne.
* Vérifiez si chaque caractère est un chiffre en appelant la méthode `isdigit()` sur celui-ci.
* `isdigit()` retourne `True` si le caractère testé est un chiffre, sinon il retourne `False`.

Les compréhensions de liste peuvent être très utiles pour collecter toutes ces valeurs de vérité dans une liste. Voici un rapide récapitulatif :

```
 # Compréhension de liste

 [output_expression for every_item in an_iterable]
     |
     |
     V
    résultat de faire quelque chose sur chaque élément de l'itérable
    
 # En essence, parcourez l'itérable, faites quelque chose sur chaque élément et
 retournez le résultat de l'opération.
 
```

Comme montré dans l'extrait de code ci-dessous, notre exemple de chaîne `coding**is**cool**345` contient des chiffres.

Par conséquent, l'appel de la fonction `any()` sur la chaîne devrait retourner `True`. Nous utilisons la compréhension de liste pour obtenir une liste de valeurs `True` et `False` selon que le caractère est un chiffre ou non.

```python
my_string = "coding**is**cool**345"
are_there_digits = [char.isdigit() for char in my_string]
print(any(are_there_digits))

# Sortie
True
```

Remarquez comment `are_there_digits` est une liste avec autant d'éléments que la longueur de la chaîne.

Pour chaque caractère dans la chaîne, il y a une valeur de vérité correspondante – `True` si le caractère est un chiffre, et `False` si le caractère n'est pas un chiffre, comme montré ci-dessous.

```python
print(are_there_digits)

# Sortie
[False, False, False, False, False, False, False, False, False, False, False,
False, False, False, False, False, False, False, True, True, True]
```

### Comment utiliser la fonction any() de Python pour vérifier la présence de lettres dans une chaîne

Prenons un autre exemple similaire. Cette fois, vérifions l'occurrence de lettres dans une chaîne.

La chaîne testée est `***456278)))` qui ne contient pas de lettres – l'appel de `any()` retourne `False` comme prévu. Pour chaque caractère dans la chaîne, appelez la méthode `isalpha()` pour vérifier s'il s'agit d'une lettre ou non.

```python
my_string = "***456278)))"
num = [char.isalpha() for char in my_string]
print(any(num))

# Sortie
False
```

La liste `is_letter` est une liste de valeurs `False`, comme vérifié ci-dessous :

```python
print(is_letter)

# Sortie
[False, False, False, False, False, False, False, False, False, False, False, False]
```

### Comment utiliser la fonction any() de Python pour combiner plusieurs conditions avec un OU logique

Supposons que vous décidiez d'être plus productif et écriviez la liste montrée ci-dessous. Cependant, vous choisissez de ne pas être dur avec vous-même et décidez que vous pouvez avoir beaucoup de sucreries tant qu'un des éléments de la liste se produit !😀

![Image](https://www.freecodecamp.org/news/content/images/2021/08/any.png)

Remarquez comment nous avons plusieurs conditions à considérer, mais choisissons d'avoir des sucreries même si l'une d'elles évalue à `True`.

Cela ne ressemble-t-il pas à une instruction `if` où vous devez vérifier si plusieurs conditions enchaînées par l'opérateur logique `or` évaluent à `True` ? Oui, c'est le cas et la fonction `any()` peut être très utile pour cela.

Supposons que vous avez `N` conditions `c1`, `c2`, `c3`, ..., `cN`. Considérez le pseudocode ci-dessous :

```
if c1 or c2 or ... c_(N-1) or CN:
	# FAIRE CECI

else:
	# FAIRE CELA
```

Vous pouvez maintenant collecter toutes ces conditions dans un itérable, par exemple, une liste ou un tuple, puis appeler `any()` sur cet itérable pour vérifier si une ou plusieurs conditions sont `True`, comme montré ci-dessous. N'est-ce pas simple ? 😀

```
conditions = [c1,c2,..., c_N]

if any(conditions):
	# FAIRE CECI
else:
	# FAIRE CELA
```

## Comment utiliser la fonction all() en Python

Commençons par la syntaxe de la fonction `all()`.

👉 **Syntaxe** : `all(iterable)`

* Retourne `True` si `bool(x)` est `True` pour toutes les valeurs `x` dans l'itérable.
* Retourne `True` si l'itérable est vide.

La fonction `all()` prend un itérable comme argument, retourne `True` uniquement si tous les éléments de l'itérable évaluent à `True` ou si l'itérable est vide. Dans tous les autres cas, la fonction `all()` retourne `False`.

### Comment utiliser la fonction all() de Python pour vérifier la présence de lettres dans une chaîne

Prenons des exemples similaires pour vérifier certaines caractéristiques des chaînes.

La chaîne de test `coding**is**cool` contient le caractère spécial `*` en plus des lettres. Donc, lorsque nous vérifions si tous les caractères de la chaîne sont des lettres en utilisant la fonction `all()`, nous devrions obtenir `False`.

```python
my_string = "coding**is**cool"
are_all_letters = [char.isalpha() for char in my_string]
print(all(are_all_letters))
# Sortie
False

print(are_all_letters)
# Sortie
[True, True, True, True, True, True, False, False, True, True, False, False,
True, True, True, True]
```

Remarquez comment la liste `are_all_letters` a des valeurs `False` à toutes les positions où le `*` est présent dans notre chaîne.

### Comment utiliser la fonction all() de Python pour vérifier la présence de chiffres dans une chaîne

Vérifions maintenant si tous les caractères de la chaîne sont des chiffres en utilisant la fonction `all()`. La chaîne de test `56456278` ne contient que des chiffres, donc, l'appel de `all()` devrait retourner `True` car la compréhension de liste nous donne une liste de valeurs `True`.

```python
my_string = "56456278"
are_all_digits = [char.isdigit() for char in my_string]
print(all(are_all_digits))
# Sortie
True

print(are_all_digits)
# Sortie
[True, True, True, True, True, True, True, True]
```

### Comment utiliser la fonction all() de Python pour combiner plusieurs conditions avec un ET logique

Considérons l'exemple suivant. Cette fois, vous êtes en compétition pour un iPad et les conditions sont plus strictes. Vous devez compléter _toutes_ les tâches de la liste pour obtenir un iPad de votre cousin.😀

![Image](https://www.freecodecamp.org/news/content/images/2021/08/all.png)

Maintenant, cela ressemble beaucoup à l'utilisation d'une instruction `if` pour vérifier si plusieurs conditions enchaînées par l'opérateur logique `and` évaluent à `True`, comme montré ci-dessous :

```
if c1 and c2 and ... c_(N-1) and CN:
	# FAIRE CECI

else:
	# FAIRE CELA
```

Vous pourriez utiliser la fonction `all()` pour rendre cela encore plus concis en collectant les conditions dans un itérable, puis en appelant la fonction `all()` sur l'itérable.

```
conditions = [c1,c2,..., c_N]

if all(conditions):
	# FAIRE CECI
else:
	# FAIRE CELA
```

## Conclusion

J'espère que ce tutoriel vous a aidé à comprendre les fonctions `any()` et `all()` en Python.

À bientôt dans un autre article. En attendant, bon apprentissage !