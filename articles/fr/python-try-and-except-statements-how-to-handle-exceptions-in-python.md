---
title: Instructions Try et Except en Python – Comment gérer les exceptions en Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-09-23T21:00:47.000Z'
originalURL: https://freecodecamp.org/news/python-try-and-except-statements-how-to-handle-exceptions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/try-except.png
tags:
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: Instructions Try et Except en Python – Comment gérer les exceptions en
  Python
seo_desc: "When coding in Python, you can often anticipate runtime errors even in\
  \ a syntactically and logically correct program. These errors can be caused by invalid\
  \ inputs or some predictable inconsistencies. \nIn Python, you can use the try and\
  \ the except blo..."
---

Lorsque vous codez en Python, vous pouvez souvent anticiper des erreurs d'exécution même dans un programme syntaxiquement et logiquement correct. Ces erreurs peuvent être causées par des entrées invalides ou certaines incohérences _prévisibles_.

En Python, vous pouvez utiliser les blocs `try` et `except` pour gérer la plupart de ces erreurs en tant qu'_exceptions_ de manière plus élégante.

Dans ce tutoriel, vous apprendrez la syntaxe générale de `try` et `except`. Ensuite, nous procéderons à des exemples de code simples, discuterons de ce qui peut mal se passer, et fournirons des mesures correctives en utilisant les blocs `try` et `except`.

## Syntaxe des blocs Try et Except en Python

Commençons par comprendre la syntaxe des instructions `try` et `except` en Python. Le modèle général est présenté ci-dessous :

```
try:
	# Il peut y avoir des erreurs dans ce bloc
    
except <type d'erreur>:
	# Faites ceci pour gérer l'exception ;
	# exécuté si le bloc try génère une erreur
    
else:
	# Faites ceci si le bloc try s'exécute avec succès sans erreurs
   
finally:
	# Ce bloc est toujours exécuté

```

Examinons à quoi servent les différents blocs :

* Le bloc `try` est le bloc d'instructions que vous souhaitez essayer d'exécuter. Cependant, il peut y avoir des erreurs d'exécution en raison d'une exception, et ce bloc peut ne pas fonctionner comme prévu.
* Le bloc `except` est déclenché lorsque le bloc `try` échoue en raison d'une exception. Il contient un ensemble d'instructions qui donnent souvent un contexte sur ce qui s'est mal passé dans le bloc `try`.
* Vous devez toujours mentionner le _type_ d'_erreur_ que vous souhaitez attraper en tant qu'exception dans le bloc `except`, désigné par le placeholder `<type d'erreur>` dans l'extrait ci-dessus.
* Vous pouvez également utiliser `except` sans spécifier le `<type d'erreur>`. Cependant, ce n'est pas une pratique recommandée car vous ne tenez pas compte des différents types d'erreurs qui peuvent survenir.

> En essayant d'exécuter le code dans le bloc `try`, il est également possible que plusieurs erreurs se produisent.

Par exemple, vous pouvez accéder à une liste en utilisant un index qui est hors de portée, utiliser une clé de dictionnaire incorrecte, et essayer d'ouvrir un fichier qui n'existe pas - tout cela dans le bloc `try`.

Dans ce cas, vous pouvez rencontrer `IndexError`, `KeyError`, et `FileNotFoundError`. Et vous devez ajouter autant de blocs `except` que le nombre d'erreurs que vous anticipez, un pour chaque type d'erreur.

* Le bloc `else` est déclenché uniquement si le bloc `try` est exécuté sans erreurs. Cela peut être utile lorsque vous souhaitez prendre une mesure de suivi lorsque le bloc `try` réussit. Par exemple, si vous essayez et ouvrez un fichier avec succès, vous pouvez vouloir lire son contenu.
* Le bloc `finally` est toujours exécuté, indépendamment de ce qui se passe dans les autres blocs. Cela est utile lorsque vous souhaitez libérer des ressources après l'exécution d'un bloc de code particulier.

> **Note** : Les blocs `else` et `finally` sont _optionnels._ Dans la plupart des cas, vous pouvez utiliser uniquement le bloc `try` pour essayer de faire quelque chose, et attraper les erreurs en tant qu'exceptions dans le bloc `except`.

Au cours des prochaines minutes, vous utiliserez ce que vous avez appris jusqu'à présent pour gérer les exceptions en Python. Commençons.

## Comment gérer une erreur `ZeroDivisionError` en Python

Considérez la fonction `divide()` présentée ci-dessous. Elle prend deux arguments – `num` et `div` – et retourne le quotient de l'opération de division `num/div`.

```python
def divide(num,div):
  return num/div
```

▶ L'appel de la fonction avec différents nombres retourne des résultats comme prévu :

```python
res = divide(100,8)
print(res)

# Sortie
12.5

res = divide(568,64)
print(res)

# Sortie
8.875

```

Ce code fonctionne bien jusqu'à ce que vous essayiez de diviser par zéro :

```python
divide(27,0)


```

Vous voyez que le programme plante en lançant une erreur `ZeroDivisionError` :

```
# Sortie
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-19-932ea024ce43> in <module>()
----> 1 divide(27,0)

<ipython-input-1-c98670fd7a12> in divide(num, div)
      1 def divide(num,div):
----> 2   return num/div

ZeroDivisionError: division by zero

```

Vous pouvez gérer cette division par zéro en tant qu'exception en faisant ce qui suit :

* Dans le bloc `try`, placez un appel à la fonction `divide()`. En essence, vous essayez de diviser `num` par `div`.
* Gérez le cas où `div` est `0` en tant qu'exception dans le bloc `except`.
* Dans cet exemple, vous pouvez attraper `ZeroDivisionError` en affichant un message informant l'utilisateur qu'il a essayé de diviser par zéro.

Cela est montré dans l'extrait de code ci-dessous :

```python
try:
    res = divide(num,div)
    print(res)
except ZeroDivisionError:
    print("Vous avez essayé de diviser par zéro :( ")

```

Avec une entrée valide, le code fonctionne toujours bien.

```python
divide(10,2)
# Sortie
5.0

```

Lorsque vous essayez de diviser par zéro, vous êtes informé de l'exception qui se produit, et le programme se termine élégamment.

```python
divide(10,0)
# Sortie
Vous avez essayé de diviser par zéro :(

```

## Comment gérer une erreur `TypeError` en Python

Dans cette section, vous verrez comment utiliser `try` et `except` pour gérer une erreur `TypeError` en Python.

▶ Considérez la fonction suivante `add_10()` qui prend un nombre en argument, ajoute 10 à celui-ci, et retourne le résultat de cette addition.

```python
def add_10(num):
  return num + 10
```

Vous pouvez appeler la fonction `add_10()` avec n'importe quel nombre et elle fonctionnera bien, comme montré ci-dessous :

```python
result = add_10(89)
print(result)

#Sortie
99
```

Maintenant, essayez d'appeler `add_10()` avec `"five"` au lieu de `5`.

```python
add_10("five")
```

Vous remarquerez que votre programme plante avec le message d'erreur suivant :

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-15-9844e949c84e> in <module>()
----> 1 add_10("five")

<ipython-input-13-2e506d74d919> in add_10(num)
      1 def add_10(num):
----> 2   return num + 10

TypeError: can only concatenate str (not "int") to str
```

Le message d'erreur `TypeError: can only concatenate str (not "int") to str` explique que vous ne pouvez concaténer que deux chaînes de caractères, et non ajouter un entier à une chaîne.

Maintenant, vous avez ce qui suit :

* Étant donné un nombre `my_num`, _essayez_ d'appeler la fonction `add_10()` avec `my_num` comme argument. Si l'argument est de type valide, il n'y a pas d'exception.
* Sinon, le bloc `except` correspondant à `TypeError` est déclenché, informant l'utilisateur que l'argument est de type invalide.

Cela est expliqué ci-dessous :

```python
my_num = "five"
try:
  result = add_10(my_num)
  print(result)
except TypeError:
  print("L'argument `num` devrait être un nombre")
```

Puisque vous avez maintenant géré `TypeError` en tant qu'exception, vous êtes simplement informé que l'argument est de type invalide.

```
L'argument `num` devrait être un nombre
```

## Comment gérer une erreur `IndexError` en Python

Si vous avez travaillé avec des listes Python, ou tout itérable Python auparavant, vous avez probablement rencontré `IndexError`.

Cela est dû au fait qu'il est souvent difficile de suivre toutes les modifications apportées aux itérables. Et vous pouvez essayer d'accéder à un élément à un index qui n'est pas valide.

▶ Dans cet exemple, la liste `my_list` contient 4 éléments. Les indices valides sont 0, 1, 2, et 3, et -1, -2, -3, -4 si vous utilisez l'indexation négative.

Puisque `2` est un index valide, vous voyez que l'élément à l'index `2`, qui est `C++`, est affiché :

```python
my_list = ["Python","C","C++","JavaScript"]
print(my_list[2])

#Sortie
C++
```

Si vous essayez d'accéder à un élément à un index qui est en dehors de la plage des indices valides, vous rencontrerez une erreur `IndexError` :

```python
print(my_list[4])
```

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-7-437bc6501dea> in <module>()
      1 my_list = ["Python","C","C++","JavaScript"]
----> 2 print(my_list[4])

IndexError: list index out of range
```

Si vous êtes familier avec le schéma, vous utiliserez maintenant `try` et `except` pour gérer les erreurs d'index.

▶ Dans l'extrait de code ci-dessous, vous essayez d'accéder à l'élément à l'index spécifié par `search_idx`.

```python
search_idx = 3
try:
  print(my_list[search_idx])
except IndexError:
  print("Désolé, l'index de la liste est hors de portée")
```

Ici, `search_idx` (`3`) est un index valide, et l'élément à cet index particulier est affiché :

```
JavaScript
```

Si `search_idx` est en dehors de la plage valide pour les indices, le bloc except attrape `IndexError` en tant qu'exception, et il n'y a plus de longs messages d'erreur. 😊

```python
search_idx = 4
try:
  print(my_list[search_idx])
except IndexError:
  print("Désolé, l'index de la liste est hors de portée")
```

Plutôt, le message que `search_idx` est en dehors de la plage valide des indices est affiché :

```
Désolé, l'index de la liste est hors de portée
```

## Comment gérer une erreur `KeyError` en Python

Vous avez probablement rencontré `KeyError` lorsque vous travaillez avec des dictionnaires Python.

▶ Considérez cet exemple où vous avez un dictionnaire `my_dict`.

```python
my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
search_key = "non-existent key"
print(my_dict[search_key])
```

* Le dictionnaire `my_dict` a 3 paires clé-valeur, `"key1:value1"`, `"key2:value2"`, et `"key3:value3"`.
* Maintenant, vous essayez d'accéder au dictionnaire et d'obtenir la valeur correspondant à la clé `"non-existent key"`.

Comme prévu, vous obtiendrez une erreur `KeyError` :

```
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-2-2a61d404be04> in <module>()
      1 my_dict ={"key1":"value1","key2":"value2","key3":"value3"}
      2 search_key = "non-existent key"
----> 3 my_dict[search_key]

KeyError: 'non-existent key'
```

Vous pouvez gérer `KeyError` presque de la même manière que vous avez géré `IndexError`.

* Vous pouvez essayer d'accéder à la valeur correspondant à la clé spécifiée par `search_key`.
* Si `search_key` est effectivement une clé valide, la valeur correspondante est affichée.
* Si vous rencontrez une exception en raison d'une clé inexistante, vous utilisez le bloc `except` pour informer l'utilisateur.

Cela est expliqué dans l'extrait de code ci-dessous :

```python
try:
  print(my_dict[search_key])
except KeyError:
  print("Désolé, ce n'est pas une clé valide !")
```

```
Désolé, ce n'est pas une clé valide !
```

▶ Si vous souhaitez fournir un contexte supplémentaire tel que le nom de la clé invalide, vous pouvez le faire également. Il est possible que la clé ait été mal orthographiée, ce qui l'a rendue invalide. Dans ce cas, informer l'utilisateur de la clé utilisée l'aidera probablement à corriger la faute de frappe.

Vous pouvez faire cela en attrapant la clé invalide en tant que `<error_msg>` et l'utiliser dans le message affiché lorsque l'exception se produit :

```python
try:
  print(my_dict[search_key])
except KeyError as error_msg:
  print(f"Désolé, {error_msg} n'est pas une clé valide !")
```

▶ Remarquez comment le nom de la clé est également affiché :

```
Désolé, 'non-existent key' n'est pas une clé valide !
```

## Comment gérer une erreur `FileNotFoundError` en Python

Une autre erreur courante qui se produit lors de la manipulation de fichiers en Python est `FileNotFoundError`.

▶ Dans l'exemple suivant, vous essayez d'ouvrir le fichier `my_file.txt` en spécifiant son chemin à la fonction `open()`. Et vous souhaitez lire le fichier et afficher le contenu du fichier.

Cependant, vous n'avez pas encore créé le fichier à l'emplacement spécifié.

Si vous essayez d'exécuter l'extrait de code ci-dessous, vous obtiendrez une erreur `FileNotFoundError` :

```python
my_file = open("/content/sample_data/my_file.txt")
contents = my_file.read()
print(contents)
```

```
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-4-4873cac1b11a> in <module>()
----> 1 my_file = open("my_file.txt")

FileNotFoundError: [Errno 2] No such file or directory: 'my_file.txt'
```

Et en utilisant `try` et `except`, vous pouvez faire ce qui suit :

* Essayez d'ouvrir le fichier dans le bloc `try`.
* Gérez `FileNotFoundError` dans le bloc `except` en informant l'utilisateur qu'il a essayé d'ouvrir un fichier qui n'existe pas.
* Si le bloc `try` réussit et que le fichier existe, lisez et affichez le contenu du fichier.
* Dans le bloc `finally`, fermez le fichier afin qu'il n'y ait pas de gaspillage de ressources. Rappelez-vous comment le fichier sera fermé indépendamment de ce qui se passe dans les étapes d'ouverture et de lecture du fichier.

```python
try:
  my_file = open("/content/sample_data/my_file.txt")
except FileNotFoundError:
  print(f"Désolé, le fichier n'existe pas")
else:
  contents = my_file.read()
  print(contents)
finally:
  my_file.close()
```

Remarquez comment vous avez géré l'erreur en tant qu'exception et le programme se termine élégamment en affichant le message ci-dessous :

```
Désolé, le fichier n'existe pas
```

▶ Considérons le cas où le bloc `else` est déclenché. Le fichier `my_file.txt` est maintenant présent au chemin mentionné précédemment.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-77.png)

Et voici ce que contient le fichier `my_file.txt` :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-78.png)

Maintenant, la réexécution de l'extrait de code précédent fonctionne comme prévu.

Cette fois, le fichier `my_file.txt` est présent, le bloc `else` est déclenché et son contenu est affiché, comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-80.png)

J'espère que cela clarifie comment vous pouvez gérer les exceptions lors de la manipulation de fichiers.

## Conclusion

Dans ce tutoriel, vous avez appris comment utiliser les instructions `try` et `except` en Python pour gérer les exceptions.

Vous avez codé des exemples pour comprendre quels types d'exceptions peuvent se produire et comment vous pouvez utiliser `except` pour attraper les erreurs les plus courantes.

J'espère que vous avez apprécié ce tutoriel. Bon codage ! À la prochaine :)