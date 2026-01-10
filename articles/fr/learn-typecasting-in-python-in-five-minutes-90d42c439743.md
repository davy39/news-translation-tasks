---
title: Apprendre le transtypage en Python en cinq minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-05T16:57:47.000Z'
originalURL: https://freecodecamp.org/news/learn-typecasting-in-python-in-five-minutes-90d42c439743
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Z-48Ln0Z7S9M8sI9
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Apprendre le transtypage en Python en cinq minutes
seo_desc: 'By PALAKOLLU SRI MANIKANTA

  A crash course on Typecasting and Type conversion in Python in a very non-verbose
  manner


  _Photo by [Unsplash](https://unsplash.com/@scw1217?utm_source=medium&utm_medium=referral"
  rel="noopener" target="_blank" title="">Suz...'
---

Par PALAKOLLU SRI MANIKANTA

#### Un cours accéléré sur le transtypage et la conversion de types en Python de manière très concise

![Image](https://cdn-media-1.freecodecamp.org/images/pH646PiGhvTTFSW0l649xmzU-3d08zvH-dbS)
_Photo par [Unsplash](https://unsplash.com/@scw1217?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Suzanne D. Williams</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Transtypage

Le processus de conversion d'un type de données en un autre type de données est appelé **Transtypage** ou **Coercition de type** ou **Conversion de type**.

Les sujets sur lesquels je vais me concentrer dans cet article sont :

1. Conversion de type implicite
2. Conversion de type explicite
3. Avantages
4. Inconvénients

### Conversion de type implicite

Lorsque la conversion de type est effectuée automatiquement par l'interpréteur sans l'intervention du programmeur, ce type de conversion est appelé **conversion de type implicite**.

#### **Programme d'exemple :**

```
myInt = 143     # Valeur entière.myFloat = 1.43  # Valeur flottante.
```

```
myResult = myInt + myFloat   # Résultat de la somme
```

```
print("datatype of myInt:",type(myInt))print("datatype of myFloat:",type(myFloat))
```

```
print("Value of myResult:",myResult)print("datatype of myResult:",type(myResult))
```

#### **Sortie :**

La sortie du programme ci-dessus sera :

```
datatype of myInt: <class 'int'>datatype of myFloat: <class 'float'>Value of myResult: 144.43datatype of myResult: <class 'float'>
```

Dans le programme ci-dessus,

* Nous additionnons deux variables myInt et myFloat, en stockant la valeur dans myResult.
* Nous allons examiner le type de données des trois objets respectivement.
* Dans la sortie, nous pouvons voir que le type de données de myInt est un `entier`, le type de données de myFloat est un `flottant`.
* De plus, nous pouvons voir que myFloat a un type de données `flottant` car Python convertit le type de données plus petit en type de données plus grand pour éviter la perte de données.

Ce type de conversion est appelé **conversion de type implicite** (ou) **UpCasting**_._

### Conversion de type explicite

Dans la conversion de type explicite, les utilisateurs convertissent le type de données d'un objet en le type de données requis. Nous utilisons des fonctions intégrées prédéfinies comme :

1. int()
2. float()
3. complex()
4. bool()
5. str()

La syntaxe pour la conversion de type explicite est :

```
(required_datatype)(expression)
```

Ce type de conversion est appelé **conversion de type explicite** (ou) **DownCasting**_._

#### **Conversion en Int**

Nous pouvons utiliser cette fonction pour convertir des valeurs d'autres types en int.

Par exemple :

```
>>> int(123.654)123
```

```
>>>int(False)0
```

```
>>> int("10")10
```

```
>>> int("10.5")ValueError: invalid literal for int() with base 10: '10.5'
```

```
>>> int("ten")ValueError: invalid literal for int() with base 10: 'ten'
```

```
>>> int("0B1111")ValueError: invalid literal for int() with base 10: '0B1111'
```

```
>>> int(10+3j)TypeError: can't convert complex to int
```

#### **Note :**

1. Vous ne pouvez pas convertir le type de données complexe en int
2. Si vous voulez convertir un type de chaîne en type int, le littéral de chaîne doit contenir la valeur en Base-10

#### Conversion en Float

Cette fonction est utilisée pour convertir **n'importe quel type de données en un nombre à virgule flottante**.

Par exemple :

```
>>> float(10) 10.0
```

```
>>> float(True)1.0
```

```
>>> float(False)0.0
```

```
>>> float("10")10.0
```

```
>>> float("10.5")10.5
```

```
>>> float("ten")ValueError: could not convert string to float: 'ten'
```

```
>>> float(10+5j)TypeError: can't convert complex to float
```

```
>>> float("0B1111")ValueError: could not convert string to float: '0B1111'
```

#### Note :

1. Vous pouvez convertir le type complexe en valeur de type flottant.
2. Si vous voulez convertir un type de chaîne en type flottant, le littéral de chaîne doit contenir la valeur en base-10.

#### Conversion en Complexe

Cette fonction est utilisée **pour convertir des nombres réels en un nombre complexe (réel, imaginaire)**.

#### **Forme 1 : complex (x)**

Vous pouvez utiliser cette fonction pour convertir une seule valeur en un nombre complexe avec une partie réelle x et une partie imaginaire 0.

Par exemple :

```
>>> complex(10)10+0j
```

```
>>> complex(10.5)10.5+0j
```

```
>>> complex(True)1+0j
```

```
>>> complex(False)0+0j
```

```
>>> complex("10")10+0j
```

```
>>> complex("10.5")10.5+0j
```

```
>>> complex("ten")ValueError: complex() arg is a malformed string
```

#### **Forme 2 : complex (x, y)**

Si vous voulez convertir X et Y en nombre complexe de sorte que X sera la partie réelle et Y sera la partie imaginaire.

Par exemple :

```
>>> complex(10,-2)10-2j
```

```
>>> complex(True, False)1+0j
```

#### Conversion en Booléen

Cette fonction est utilisée pour convertir facilement n'importe quel type de données en type de données booléen. C'est le type de données le plus flexible en Python.

Par exemple :

```
>>> bool(0)False
```

```
>>> bool(1)True
```

```
>>> bool(10)True
```

```
>>> bool(0.13332)True
```

```
>>> bool(0.0)False
```

```
>>> bool(10+6j)True
```

```
>>> bool(0+15j)True
```

```
>>> bool(0+0j)False
```

```
>>> bool("Apple")True
```

```
>>> bool("")False
```

> Note : Avec l'aide de la fonction bool, vous pouvez convertir n'importe quel type de données en booléen et la sortie sera - Pour toutes les valeurs, elle produira True sauf pour 0, 0+0j et pour une chaîne vide.

#### Conversion en Chaîne

Cette fonction est utilisée **pour convertir n'importe quel type en un type de chaîne**.

Par exemple :

```
>>> str(10)'10'
```

```
>>> str(10.5)'10.5'
```

```
>>> str(True)'True'
```

```
>>> str(False)'False'
```

```
>>> str(10+5j)'10+5j'
```

```
>>> str(False)'False'
```

#### Programme d'exemple :

```
integer_number = 123  # Intstring_number = "456" # String
```

```
print("Data type of integer_number:",type(integer_number))print("Data type of num_str before Type Casting:",type(num_str))
```

```
string_number = int(string_number)print("Data type of string_number after Type Casting:",type(string_number))
```

```
number_sum = integer_number + string_number
```

```
print("Sum of integer_number and num_str:",number_sum)print("Data type of the sum:",type(number_sum))
```

#### **Sortie :**

Lorsque nous exécutons le programme ci-dessus, la sortie sera :

```
Data type of integer_number: <class 'int'>Data type of num_str before Type Casting: <class 'str'>Data type of string_number after Type Casting: <class 'int'>Sum of integer_number and num_str: 579Data type of the sum: <class 'int'>
```

Dans le programme ci-dessus,

* Nous additionnons les variables string_number et integer_number.
* Nous avons converti string_number de string (type supérieur) en integer (type inférieur) en utilisant la fonction `int()` pour effectuer l'addition.
* Après avoir converti string_number en une valeur entière, Python additionne ces deux variables.
* Nous avons obtenu la valeur number_sum et le type de données comme étant un entier.

### Avantages du Transtypage

1. Plus pratique à utiliser

### Inconvénients du Transtypage

1. Système de types plus complexe
2. Source de bugs dus à des transtypages inattendus

J'ai couvert presque tout ce qui est nécessaire pour effectuer toute opération de transtypage en Python3.

**J'espère que cela vous a aidé à apprendre le transtypage en Python de manière rapide et facile.**

**Si vous avez aimé cet article, veuillez cliquer sur l'applaudissement et laissez-moi vos précieux commentaires.**