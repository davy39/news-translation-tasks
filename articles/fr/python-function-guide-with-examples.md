---
title: Guide des fonctions Python avec exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-28T22:43:00.000Z'
originalURL: https://freecodecamp.org/news/python-function-guide-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d54740569d1a4ca372d.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Guide des fonctions Python avec exemples
seo_desc: 'Introduction to Functions in Python

  A function allows you to define a reusable block of code that can be executed many
  times within your program.

  Functions allow you to create more modular and DRY solutions to complex problems.

  While Python already p...'
---

## Introduction aux fonctions en Python

Une fonction permet de définir un bloc de code réutilisable qui peut être exécuté plusieurs fois au sein de votre programme.

Les fonctions permettent de créer des solutions plus modulaires et [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) à des problèmes complexes.

Bien que Python fournisse déjà de nombreuses fonctions intégrées telles que `print()` et `len()`, vous pouvez également définir vos propres fonctions à utiliser dans vos projets.

L'un des grands avantages de l'utilisation des fonctions dans votre code est qu'elles réduisent le nombre total de lignes de code dans votre projet.

### **Syntaxe**

En Python, une définition de fonction présente les caractéristiques suivantes :

1. Le mot-clé `def`
2. un nom de fonction
3. des parenthèses `()`, et à l'intérieur des parenthèses, des paramètres d'entrée, bien que les paramètres d'entrée soient facultatifs.
4. un deux-points `:`
5. un bloc de code à exécuter
6. une instruction de retour (facultative)

```python
# une fonction sans paramètres ni valeurs de retour
def sayHello():
  print("Hello!")

sayHello()  # appelle la fonction, 'Hello!' est imprimé dans la console

# une fonction avec un paramètre
def helloWithName(name):
  print("Hello " + name + "!")

helloWithName("Ada")  # appelle la fonction, 'Hello Ada!' est imprimé dans la console

# une fonction avec plusieurs paramètres avec une instruction de retour
def multiply(val1, val2):
  return val1 * val2

multiply(3, 5)  # imprime 15 dans la console
```

Les fonctions sont des blocs de code qui peuvent être réutilisés simplement en appelant la fonction. Cela permet une réutilisation simple et élégante du code sans réécrire explicitement des sections de code. Cela rend le code à la fois plus lisible, facilite le débogage et limite les erreurs de frappe.

Les fonctions en Python sont créées en utilisant le mot-clé `def`, suivi d'un nom de fonction et des paramètres de la fonction à l'intérieur des parenthèses.

Une fonction retourne toujours une valeur. Le mot-clé `return` est utilisé par la fonction pour retourner une valeur. Si vous ne souhaitez pas retourner de valeur, la valeur par défaut `None` sera retournée.

Le nom de la fonction est utilisé pour appeler la fonction, en passant les paramètres nécessaires à l'intérieur des parenthèses.

```python
# ceci est une fonction de somme basique
def sum(a, b):
  return a + b

result = sum(1, 2)
# result = 3
```

Vous pouvez définir des valeurs par défaut pour les paramètres, de sorte que Python interprétera que la valeur de ce paramètre est celle par défaut si aucune n'est donnée.

```python
def sum(a, b=3):
  return a + b

result = sum(1)
# result = 4
```

Vous pouvez passer les paramètres dans l'ordre que vous souhaitez, en utilisant le nom du paramètre.

```python
result = sum(b=2, a=2)
# result = 4
```

Cependant, il n'est pas possible de passer un argument clé avant un argument non clé.

```python
result = sum(3, b=2)
#result = 5
result2 = sum(b=2, 3)
#Lèvera une SyntaxError
```

Les fonctions sont également des objets, vous pouvez donc les assigner à une variable et utiliser cette variable comme une fonction.

```python
s = sum
result = s(1, 2)
# result = 3
```

### **Notes**

Si une définition de fonction inclut des paramètres, vous devez fournir le même nombre de paramètres lorsque vous appelez la fonction.

```python
print(multiply(3))  # TypeError: multiply() prend exactement 2 arguments (0 donné)

print(multiply('a', 5))  # 'aaaaa' imprimé dans la console

print(multiply('a', 'b'))  # TypeError: Python ne peut pas multiplier deux chaînes de caractères
```

Le bloc de code que la fonction exécutera inclut toutes les instructions indentées à l'intérieur de la fonction.

```python
def myFunc():
print('ceci sera imprimé')
print('ceci aussi')

x = 7
# l'assignation de x ne fait pas partie de la fonction car elle n'est pas indentée
```

Les variables définies dans une fonction n'existent que dans le cadre de cette fonction.

```python
def double(num):
x = num * 2
return x

print(x)  # erreur - x n'est pas défini
print(double(4))  # imprime 8
```

Python interprète le bloc de fonction uniquement lorsque la fonction est appelée et non lorsque la fonction est définie. Ainsi, même si le bloc de définition de la fonction contient une sorte d'erreur, l'interpréteur Python ne la signalera que lorsque la fonction sera appelée.

Examinons maintenant quelques fonctions spécifiques avec des exemples.

## Fonction max()

`max()` est une fonction intégrée en Python 3. Elle retourne l'élément le plus grand dans un itérable ou le plus grand de deux ou plusieurs arguments.

### Arguments

Cette fonction prend deux ou plusieurs nombres ou tout type d'itérable comme argument. Lors de la transmission d'un itérable comme argument, nous devons nous assurer que tous les éléments de l'itérable sont du même type. Cela signifie que nous ne pouvons pas transmettre une liste qui contient à la fois des valeurs de chaîne et des valeurs entières. Syntaxe : max(iterable, *iterables[,key, default]) max(arg1, arg2, *args[, key])

Arguments valides :

```text
max(2, 3)
max([1, 2, 3])
max('a', 'b', 'c')
```

Arguments invalides :

```text
max(2, 'a')
max([1, 2, 3, 'a'])
max([])
```

### Valeur de retour

L'élément le plus grand dans l'itérable est retourné. Si deux ou plusieurs arguments positionnels sont fournis, le plus grand des arguments positionnels est retourné. Si l'itérable est vide et que la valeur par défaut n'est pas fournie, une erreur `ValueError` est levée.

### Exemple de code

```text
print(max(2, 3)) # Retourne 3 car 3 est le plus grand des deux valeurs
print(max(2, 3, 23)) # Retourne 23 car 23 est le plus grand de toutes les valeurs

list1 = [1, 2, 4, 5, 54]
print(max(list1)) # Retourne 54 car 54 est la plus grande valeur dans la liste

list2 = ['a', 'b', 'c' ]
print(max(list2)) # Retourne 'c' car 'c' est le plus grand dans la liste car c a une valeur ascii plus grande que 'a' et 'b'.

list3 = [1, 2, 'abc', 'xyz']
print(max(list3)) # Donne TypeError car les valeurs dans la liste sont de types différents

# Corrigez d'abord le TypeError mentionné ci-dessus avant de passer à l'étape suivante

list4 = []
print(max(list4)) # Donne ValueError car l'argument est vide
```

[Exécuter le code](https://repl.it/CVok)

[Documentation officielle](https://docs.python.org/3/library/functions.html#max)

## Fonction min()

`min()` est une fonction intégrée en Python 3. Elle retourne l'élément le plus petit dans un itérable ou le plus petit de deux ou plusieurs arguments.

### Arguments

Cette fonction prend deux ou plusieurs nombres ou tout type d'itérable comme argument. Lors de la transmission d'un itérable comme argument, nous devons nous assurer que tous les éléments de l'itérable sont du même type. Cela signifie que nous ne pouvons pas transmettre une liste qui contient à la fois des valeurs de chaîne et des valeurs entières.

Arguments valides :

```text
min(2, 3)
min([1, 2, 3])
min('a', 'b', 'c')
```

Arguments invalides :

```text
min(2, 'a')
min([1, 2, 3, 'a'])
min([])
```

### Valeur de retour

L'élément le plus petit dans l'itérable est retourné. Si deux ou plusieurs arguments positionnels sont fournis, le plus petit des arguments positionnels est retourné. Si l'itérable est vide et que la valeur par défaut n'est pas fournie, une erreur ValueError est levée.

### Exemple de code

```text
print(min(2, 3)) # Retourne 2 car 2 est le plus petit des deux valeurs
print(min(2, 3, -1)) # Retourne -1 car -1 est le plus petit des deux valeurs

list1 = [1, 2, 4, 5, -54]
print(min(list1)) # Retourne -54 car -54 est la plus petite valeur dans la liste

list2 = ['a', 'b', 'c' ]
print(min(list2)) # Retourne 'a' car 'a' est le plus petit dans la liste dans l'ordre alphabétique

list3 = [1, 2, 'abc', 'xyz']
print(min(list3)) # Donne TypeError car les valeurs dans la liste sont de types différents

# Corrigez d'abord le TypeError mentionné ci-dessus avant de passer à l'étape suivante

list4 = []
print(min(list4)) # Donne ValueError car l'argument est vide
```

[Exécuter le code](https://repl.it/CVir/4)

[Documentation officielle](https://docs.python.org/3/library/functions.html#min)

# Fonction divmod()

`divmod()` est une fonction intégrée en Python 3, qui retourne le quotient et le reste lors de la division du nombre `a` par le nombre `b`. Elle prend deux nombres comme arguments `a` et `b`. L'argument ne peut pas être un nombre complexe.

### Argument

Elle prend deux arguments `a` et `b` - un entier, ou un nombre décimal. Cela ne peut pas être un nombre complexe.

### Valeur de retour

La valeur de retour sera la paire de nombres positifs constituée du quotient et du reste obtenus en divisant `a` par `b`. En cas de types d'opérandes mixtes, les règles pour les opérateurs arithmétiques binaires seront appliquées. Pour les **arguments de nombres entiers**, la valeur de retour sera la même que `(a // b, a % b)`. Pour les **arguments de nombres décimaux**, la valeur de retour sera la même que `(q, a % b)`, où `q` est généralement **math.floor(a / b)** mais peut être 1 de moins que cela.

### Exemple de code

```text
print(divmod(5,2)) # imprime (2,1)
print(divmod(13.5,2.5)) # imprime (5.0, 1.0)
q,r = divmod(13.5,2.5)  # Assigne q=quotient & r= reste
print(q) # imprime 5.0 car math.floor(13.5/2.5) = 5.0
print(r) # imprime 1.0 car (13.5 % 2.5) = 1.0
```

[REPL It!](https://repl.it/FGLK/0)

[Documentation officielle](https://docs.python.org/3/library/functions.html#divmod)

## Fonction Hex(x)

`hex(x)` est une fonction intégrée en Python 3 pour convertir un nombre entier en une chaîne hexadécimale en minuscules préfixée avec "0x".

### Argument

Cette fonction prend un argument, `x`, qui doit être de type entier.

### Retour

Cette fonction retourne une chaîne hexadécimale en minuscules préfixée avec "0x".

### Exemple

```text
print(hex(16))    # imprime  0x10
print(hex(-298))  # imprime -0x12a
print(hex(543))   # imprime  0x21f
```

[Exécuter le code](https://repl.it/CV0S)

[Documentation officielle](https://docs.python.org/3/library/functions.html#hex)

## Fonction len()

`len()` est une fonction intégrée en Python 3. Cette méthode retourne la longueur (le nombre d'éléments) d'un objet. Elle prend un argument `x`.

### Arguments

Elle prend un argument, `x`. Cet argument peut être une séquence (comme une chaîne, des octets, un tuple, une liste ou une plage) ou une collection (comme un dictionnaire, un ensemble ou un ensemble figé).

### Valeur de retour

Cette fonction retourne le nombre d'éléments dans l'argument qui est passé à la fonction `len()`.

### Exemple de code

```text
list1 = [123, 'xyz', 'zara'] # liste
print(len(list1)) # imprime 3 car il y a 3 éléments dans list1

str1 = 'basketball' # chaîne
print(len(str1)) # imprime 10 car str1 est composée de 10 caractères

tuple1 = (2, 3, 4, 5) # tuple 
print(len(tuple1)) # imprime 4 car il y a 4 éléments dans tuple1

dict1 = {'name': 'John', 'age': 4, 'score': 45} # dictionnaire
print(len(dict1)) # imprime 3 car il y a 3 paires clé-valeur dans dict1
```

[Exécuter le code](https://repl.it/CUmt/15)

[Documentation officielle](https://docs.python.org/3/library/functions.html#len)

## **Fonction Ord**

`ord()` est une fonction intégrée en Python 3, pour convertir la chaîne représentant un caractère Unicode en un entier représentant le code Unicode du caractère.

#### **Exemples :**

```text
>>> ord('d')
100
>>> ord('1')
49
```

## Fonction chr

`chr()` est une fonction intégrée en Python 3, pour convertir l'entier représentant le code Unicode en une chaîne représentant un caractère correspondant.

#### **Exemples :**

```text
>>> chr(49)
'1'
```

Une chose à noter est que, si la valeur entière passée à `chr()` est hors de portée, alors une ValueError sera levée.

```text
>>> chr(-10)
'Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    chr(-1)
ValueError: chr() arg not in range(0x110000)'
```

## Fonctions input()

De nombreuses fois, dans un programme, nous avons besoin d'une entrée de l'utilisateur. Prendre des entrées de l'utilisateur rend le programme interactif. En Python 3, pour prendre une entrée de l'utilisateur, nous avons une fonction `input()`. Si la fonction d'entrée est appelée, le flux du programme sera arrêté jusqu'à ce que l'utilisateur ait donné une entrée et ait terminé l'entrée avec la touche de retour. Voyons quelques exemples :

Lorsque nous voulons simplement prendre l'entrée :

# **Cela donnera simplement une invite sans aucun message**

inp = input()

[Exécuter le code](https://repl.it/CUqX/0)

Pour donner une invite avec un message :

prompt_with_message = input('')

# **_**

# **Le '_' dans la sortie est l'invite**

[Exécuter le code](https://repl.it/CUqX/1)

3. Lorsque nous voulons prendre une entrée entière :

```text
number = int(input('Veuillez entrer un nombre : '))
```

[Exécuter le code](https://repl.it/CUqX/2)

Si vous entrez une valeur non entière, Python lèvera une erreur `ValueError`. **Donc, chaque fois que vous utilisez cela, assurez-vous de le capturer également.** Sinon, votre programme s'arrêtera de manière inattendue après l'invite.

```text
number = int(input('Veuillez entrer un nombre : '))
# Veuillez entrer un nombre : as
# Entrez une chaîne et cela lèvera cette erreur
# ValueError: invalid literal for int() with base 10 'as'
```

4. Lorsque nous voulons une entrée de chaîne :

```text
string = str(input('Veuillez entrer une chaîne : '))
```

[Exécuter le code](https://repl.it/CUqX/3)

Bien que les entrées soient stockées par défaut sous forme de chaîne, l'utilisation de la fonction `str()` rend clair pour le lecteur de code que l'entrée sera une 'chaîne'. C'est une bonne pratique de mentionner quel type d'entrée sera pris au préalable.

[Documentation officielle](https://docs.python.org/3/library/functions.html#input)

## Comment appeler une fonction en Python

Une instruction de définition de fonction n'exécute pas la fonction. L'exécution (l'appel) d'une fonction se fait en utilisant le nom de la fonction suivi de parenthèses contenant les arguments requis (le cas échéant).

```text
>>> def say_hello():
...     print('Hello')
...
>>> say_hello()
Hello
```

L'exécution d'une fonction introduit une nouvelle table de symboles utilisée pour les variables locales de la fonction. Plus précisément, toutes les assignations de variables dans une fonction stockent la valeur dans la table de symboles locale ; alors que les références de variables cherchent d'abord dans la table de symboles locale, puis dans les tables de symboles locales des fonctions englobantes, puis dans la table de symboles globale, et enfin dans la table des noms intégrés. Ainsi, les variables globales ne peuvent pas être directement assignées à une valeur au sein d'une fonction (sauf si elles sont nommées dans une instruction globale), bien qu'elles puissent être référencées.

```text
>>> a = 1
>>> b = 10
>>> def fn():
...     print(a)    # a local n'est pas assigné, pas de fonction englobante, a global référencé.
...     b = 20      # b local est assigné dans la table de symboles locale pour la fonction.
...     print(b)    # b local est référencé.
...
>>> fn()
1
20
>>> b               # b global n'est pas changé par l'appel de la fonction.
10
```

Les paramètres réels (arguments) d'un appel de fonction sont introduits dans la table de symboles locale de la fonction appelée lorsqu'elle est appelée ; ainsi, les arguments sont passés en utilisant le passage par valeur (où la valeur est toujours une référence d'objet, et non la valeur de l'objet). Lorsqu'une fonction appelle une autre fonction, une nouvelle table de symboles locale est créée pour cet appel.

```text
>>> def greet(s):
...     s = "Hello " + s    # s dans la table de symboles locale est réassigné.
...     print(s)
...
>>> person = "Bob"
>>> greet(person)
Hello Bob
>>> person                  # person utilisé pour appeler reste lié à l'objet original, 'Bob'.
'Bob'
```

Les arguments utilisés pour appeler une fonction ne peuvent pas être réassignés par la fonction, mais les arguments qui référencent des objets mutables peuvent avoir leurs valeurs changées :

```text
>>> def fn(arg):
...     arg.append(1)
...
>>> a = [1, 2, 3]
>>> fn(a)
>>> a
[1, 2, 3, 1]
```