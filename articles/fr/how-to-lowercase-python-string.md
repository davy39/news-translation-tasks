---
title: Python lower() – Comment convertir une chaîne Python en minuscules avec l'équivalent
  de la fonction tolower
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2022-11-03T16:16:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-lowercase-python-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/pexels-pixabay-278881.jpg
tags:
- name: Python
  slug: python
seo_title: Python lower() – Comment convertir une chaîne Python en minuscules avec
  l'équivalent de la fonction tolower
seo_desc: 'A string is a datatype that consists of characters wrapped in quotation
  marks. These characters can be letters, symbols, or numbers.

  In Python, there are different ways of working with strings. These methods are built-in
  functions that change the res...'
---

Une chaîne de caractères est un type de données qui se compose de caractères entourés de guillemets. Ces caractères peuvent être des lettres, des symboles ou des chiffres.

En Python, il existe différentes façons de travailler avec les chaînes de caractères. Ces méthodes sont des fonctions intégrées qui modifient les résultats de la chaîne.

Par exemple, si je veux afficher mon nom avec sa première lettre en majuscule, j'utilise la méthode `.title()` pour mettre en majuscule la première lettre.

Dans cet article, nous allons apprendre comment convertir des lettres majuscules en lettres minuscules sans utiliser la méthode intégrée.

## Comment convertir une chaîne en minuscules en utilisant `.lower()`

Les chaînes peuvent se composer de différents caractères – l'un de ces caractères étant les lettres de l'alphabet. Vous pouvez écrire l'alphabet anglais en lettres majuscules ou minuscules. Lorsque vous changez une chaîne en minuscules, cela ne s'applique qu'aux lettres.

En Python, il existe une méthode intégrée qui peut changer une chaîne en majuscules en minuscules. Elle s'applique également aux chaînes qui ont des lettres à la fois en majuscules et en minuscules. La méthode « .lower() » change les chaînes en minuscules.

```python
name = "BOB STONE"
print(name.lower()) # >> bob stone
name1 = "Ruby Roundhouse"
print(name1.lower()) # >> ruby roundhouse
name2 = "joHN Wick"
print(name2.lower()) # >> john wick
name3 = "charlieNew"
print(name3.lower()) # >> charlienew
```

Nous pouvons voir dans le bloc de code ci-dessus que les variables qui stockent chaque chaîne ont des lettres majuscules. Ensuite, avec la méthode `.lower()`, elle convertit ces lettres en minuscules.

## Autres façons de convertir une chaîne Python en minuscules

Outre la méthode intégrée « .lower() », il existe différentes façons de convertir des lettres majuscules en lettres minuscules en Python. Dans cet article, nous allons examiner deux façons différentes.

Il existe deux façons d'accéder aux lettres :

* les copier manuellement dans une liste ou

* utiliser la norme Unicode

### Comment accéder aux lettres à partir d'une liste

L'idée est de parcourir une liste de lettres et de remplacer les lettres majuscules dans une chaîne par des lettres minuscules.

Tout d'abord, créez une variable qui stocke une entrée acceptant une chaîne avec des lettres majuscules.

Ensuite, créez une autre variable qui stocke une liste de lettres majuscules et minuscules.

Enfin, créez la variable finale qui stocke une chaîne vide, où les lettres minuscules seront stockées.

```python
word = str(input("Enter a word: "))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

lowercase_letters = ''
```

Dans la liste ci-dessus, nous voyons qu'elle contient des lettres minuscules et majuscules. Il y a 26 lettres dans l'alphabet anglais, mais l'index dans une liste commence à 0, donc le compte de l'alphabet est de 51 (pour les lettres majuscules et minuscules).

Nous pouvons également voir que les lettres minuscules sont écrites en premier (côté gauche), et les lettres majuscules sont écrites en second (côté droit). Les index des lettres minuscules vont de 0 à 25, tandis que les index des lettres majuscules vont de 26 à 51.

Ensuite, nous parcourons chaque caractère de la chaîne.

```python
for char in word:
```

`<char>` est le nouveau nom de variable qui stocke tous les caractères de la variable `<word>`.

Il y a deux cas de chaînes que nous allons convertir. Le premier cas est les chaînes avec uniquement des lettres majuscules et le second a des chaînes avec des symboles spéciaux, des chiffres, certaines minuscules et certaines majuscules.

**CAS I** : chaînes avec uniquement des majuscules

Pour convertir les lettres majuscules en minuscules, nous devons trouver l'index de chaque lettre stockée par la variable `<char>` dans la liste. Pour trouver un index, nous utilisons la méthode ".index()" :

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
word = str(input("Enter a word: " ))
for char in word:
    print(alphabet.index(char))

# Résultats
# Enter a word: GIRL
# 32
# 34
# 43
# 37
```

Dans le code ci-dessus, les index des lettres dans "GIRL" sont imprimés.

Dans la liste, les lettres minuscules ont des index de 0 à 25 et les lettres majuscules ont des index de 26 à 51. Lorsque nous définissons la condition (instruction "if"), nous commençons à vérifier si l'index de la lettre est supérieur à '25' car le premier index majuscule commence à '26'.

Pour obtenir les lettres minuscules correspondantes, nous soustrayons 26 de chaque index majuscule. Lorsque nous obtenons les index des chiffres minuscules, nous utilisons l'indexation (nom_variable[index_number]) pour trouver les lettres correspondantes. Les lettres minuscules sont maintenant ajoutées au nom de variable &lt;lower_case_letters&gt; qui stocke une chaîne vide.

Nous retournons la variable &lt;lowercase_letters&gt; en l'imprimant à l'extérieur de la boucle.

```python
for char in word:
      if alphabet.index(char) > 25:
          lowercase_letters += alphabet[alphabet.index(char)-26]
  print(lowercase_letters)
```

Voici à quoi ressemble le code lorsque nous le rassemblons :

```python
def change_to_lowercase(word):
    
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lowercase_letters = ''
  
  for char in word:
      if alphabet.index(char) > 25:
          lowercase_letters += alphabet[alphabet.index(char)-26]
      
  return lowercase_letters

word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Résultats
# Enter a word: FERE
# fere
# Enter a word: PYTHONISFUN
# pythonisfun
```

**CAS II** : chaînes avec des symboles spéciaux, des chiffres, des lettres minuscules ainsi que des lettres majuscules.

Avant de convertir les lettres majuscules en minuscules, il y a certaines conditions que nous devons vérifier. Les conditions vérifieront si chaque caractère `<char>` du mot :

* n'est pas une lettre

* a à la fois des lettres majuscules et minuscules dans le mot. Si certaines lettres du mot sont en minuscules, elles resteront inchangées.

Après ces vérifications, il suppose que les caractères restants sont des lettres majuscules.

Pour vérifier si un caractère n'est pas une lettre, nous utilisons le mot-clé "not in". Pour vérifier si un caractère est en minuscule, nous trouvons l'index et le comparons au dernier compte des lettres minuscules dans la liste.

Encore une fois, les lettres minuscules ont des index de 0 à 25, et l'index de la dernière lettre minuscule est 25. Ces caractères sont ajoutés au nom de variable &lt;lower_case_letters&gt; qui stocke une chaîne vide.

```python
for char in word:
    if char not in alphabet or alphabet.index(char)<=25:
        lowercase_letters += char
```

Dans le bloc de code ci-dessus, nous avons utilisé la méthode `.index()` pour trouver la position des lettres dans l'alphabet.

Pour les caractères restants que nous supposons être des lettres majuscules, dans la liste de lettres, les index de ces lettres sont de 26 à 51. Pour trouver leurs index de lettres minuscules correspondants, nous soustrayons 26, et utilisons la méthode `.index()` pour trouver la lettre.

Indexation = nom_variable[index_number]. Nous ajoutons le résultat final à la variable stockant la chaîne vide.

```python
for char in word:
    if char not in alphabet or alphabet.index(char)<=25:
        lowercase_letters += char
    else:
        lowercase_letters += alphabet[alphabet.index(char)-26]
```

Ensuite, nous imprimons lowercase_letters à l'extérieur de la boucle :

```python
for char in word:
    if char not in alphabet or alphabet.index(char)<=25:
        lowercase_letters += char
    else:
        lowercase_letters += alphabet[alphabet.index(char)-26]
print(lowercase_letters)
```

Voici à quoi ressemble le code lorsque nous le rassemblons :

```python
def change_to_lowercase(word):
    
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  lowercase_letters = ''
  
  for char in word:
      if char not in alphabet or alphabet.index(char)<=25:
          lowercase_letters += char
      else:
          lowercase_letters += alphabet[alphabet.index(char)-26]
  return lowercase_letters

word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Résultats
# Enter a word: 2022BlackADAM&&
# 2022blackadam&&
# Enter a word: Weasle2@3568QQQAJHGB
# weasle2@3568qqqajhgb
```

## Comment accéder aux lettres en utilisant la norme Unicode

Unicode signifie norme universelle de codage des caractères. Selon unicode.org,

> "La norme Unicode fournit un numéro unique pour chaque caractère, quelle que soit la plateforme, le périphérique, l'application ou la langue."

En termes simples, toutes les lettres de différentes langues ont un numéro unique représentant chaque caractère présent dans Unicode.

Nous utilisons deux méthodes lorsque nous travaillons avec Unicode en Python : `ord()` et `chr()`.

* ord() : cette fonction accepte des caractères (lettres dans n'importe quelle langue) et retourne le numéro unique selon la norme Unicode.

* chr() : cette fonction accepte des entiers et retourne le caractère équivalent selon la norme Unicode.

Avant de plonger dans l'explication du code, voici un tableau contenant tous les numéros uniques pour l'alphabet anglais, en lettres minuscules et majuscules.

![Image](https://lh5.googleusercontent.com/BaC12Gudvtl2Wu1uAaFqqNudQKHi0mwoF5H2JT_GtrELW-sPK5IzoybnhL426kPy_4XXas-7MU3PVsmzNQJEJZqoWrq-xhApaoYFZjBuDnA5ugnJFaoBaCb2EcvAVDV5tHJyS2wbi5Wp2Iw8Gka5YWYjVTPVkxbMIwM0Uc86Ude9YNf2FQjxq4xBgQ align="left")

[*Tableau ASCII représentant les numéros uniques des alphabets anglais*](https://linuxhint.com/understanding-ascii-table/)

Maintenant que nous sommes familiers avec ce qu'est Unicode et comment accéder aux valeurs en Python, plongeons-nous.

Tout d'abord, créez une variable qui stocke une entrée acceptant une chaîne avec des lettres majuscules.

Ensuite, créez la variable finale qui stocke une chaîne vide, où les lettres minuscules seront stockées.

```python
word = str(input("Enter a word: "))
lowercase_letters = ''
```

Ensuite, nous parcourons chaque caractère de la chaîne.

```python
for char in word:
```

`<char>` est le nouveau nom de variable qui stocke tous les caractères de la variable `<word>`.

**CAS I** : chaînes contenant uniquement des lettres majuscules.

Avant de convertir les lettres majuscules en minuscules, nous devons vérifier si chaque caractère du mot est en majuscule.

Selon le tableau Unicode, la lettre majuscule A a le numéro « 65 », et la lettre majuscule Z a le numéro « 90 ». Nous vérifions si chaque caractère `<char>` dans `<word>` a des numéros entre 65 et 90. Si c'est le cas, ce sont des lettres majuscules.

```python
print((ord('A')))
# RÉSULTAT
# 65
print((ord('Z')))
# RÉSULTAT
# 90
print((ord('F')))
# RÉSULTAT
# 70
```

La fonction `ord()` retourne le numéro unique de chaque lettre en majuscule.

Pour convertir les lettres majuscules en lettres minuscules, nous ajoutons la différence entre les deux cas, « 32 », à chaque numéro de la majuscule pour obtenir les lettres minuscules.

Par exemple :

```python
number_for_A = ord('A')
number_for_a = ord('a')
difference_a = number_for_a - number_for_A
print("Differences in letters" , difference_a)
print("The unique number for A", number_for_A)
print("The unique number for a", number_for_a)

 # Résultats
# The unique number for A 65
# The unique number for a 97
# Differences in letters 32

number_for_F = ord('F')
number_for_f = ord('f')
difference_f = number_for_f - number_for_F
print("The unique number for F", number_for_F)
print("The unique number for f", number_for_f)
print("Differences in letters" , difference_f)
# Résultats
# The unique number for F 70
# The unique number for f 102
# Differences in letters 32
```

Dans le code ci-dessus, 'a' est 97 sur le tableau unicode et 'A' est 65. La différence entre eux est 32. Si nous voulons obtenir la valeur de 'a' sur le tableau, nous ajoutons 32 à la valeur de A « 65 » et obtenons « 97 ».

Ainsi, pour convertir en minuscules, nous devons ajouter 32 à chacun des numéros des lettres majuscules pour obtenir leurs lettres minuscules correspondantes.

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char) + 32
    print(char)
# Résultats
# Enter a word: REAL
# 114
# 101
# 97
# 108
```

Dans le code ci-dessus, nous parcourons la variable `<word>` pour accéder à chaque caractère.

Ensuite, nous vérifions si chaque caractère dans la variable `<word>` a un numéro unique entre 65 et 90. Si c'est le cas, il se compose de lettres majuscules.

Pour obtenir les lettres minuscules correspondantes, nous ajoutons 32. Le résultat ci-dessus imprime les numéros uniques des lettres minuscules.

Nous pouvons faire correspondre les numéros avec leurs lettres en utilisant la fonction `chr()`.

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char) + 32
        to_letters = chr(char)
    print(to_letters) 
    
    
# Résultat
# Enter a word: REAL
# r
# e
# a
# l
```

Maintenant, nous voyons que les lettres retournées sont en minuscules. Pour obtenir les lettres en une seule ligne, nous les ajoutons à la variable qui stocke la chaîne vide et retournons la variable.

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char) + 32
        to_letters = chr(char)
        lowercase_letters += to_letters
print(lowercase_letters)
# Résultat
# Enter a word: FERE
# fere
```

Voici à quoi cela ressemble lorsque nous le rassemblons :

```python
def change_to_lowercase(word):
    lowercase_letters = ''
    for char in word:
        if ord(char) >= 65 and ord(char) <= 90:
            char = ord(char)+32
            to_letters = chr(char)
            lowercase_letters += to_letters
    return lowercase_letters
word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Résultats
# Enter a word: HARDWORKPAYS
# hardworkpays
# Enter a word: PYTHONISFUN
# pythonisfun
```

**CAS II** : chaînes avec des symboles spéciaux, des chiffres, des minuscules ainsi que des majuscules.

Pour les chaînes qui ont des non-lettres et certaines lettres minuscules, nous ajoutons une instruction 'else' pour retourner les valeurs telles qu'elles apparaissent dans la chaîne. Les lettres majuscules sont ensuite converties en minuscules :

```python
word = str(input("Enter a word: " ))
lowercase_letters = ''
for char in word:
    if ord(char) >= 65 and ord(char) <= 90:
        char = ord(char)+32
        to_letters = chr(char)
        lowercase_letters += to_letters
    else:
        lowercase_letters += char
print(lowercase_letters)

# Résultat
# Enter a word: @#&YEAERS09=
# @#&yeaers09=
```

Voici à quoi cela ressemble lorsque nous le rassemblons :

```python
def change_to_lowercase(word):
    lowercase_letters = ''
    for char in word:
        if ord(char) >= 65 and ord(char) <= 90:
            char = ord(char)+32
            to_letters = chr(char)
            lowercase_letters += to_letters
        else:
            lowercase_letters += char
    return lowercase_letters
word = str(input("Enter a word: " ))
print(change_to_lowercase(word=word))

# Enter a word: YOUGOT#$^
# yougot#$
# Enter a word: BuLLettrAIn@2022
# bullettrain@2022
```

Je sais que la deuxième méthode est difficile à assimiler, mais elle donne également le résultat, tout comme la première méthode.

## Résumé

Dans cet article, vous avez appris comment convertir des caractères et des chaînes d'un cas à un autre. Nous avons également examiné le tableau ASCII.

La deuxième méthode est plus efficace et directe une fois que vous savez comment utiliser les deux fonctions importantes. Les index des lettres sont intégrés en Python, donc il n'est pas nécessaire de les mémoriser.

Merci d'avoir lu !