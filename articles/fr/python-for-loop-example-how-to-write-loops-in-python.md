---
title: Exemple de boucle For en Python – Comment écrire des boucles en Python
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-04-26T19:01:37.000Z'
originalURL: https://freecodecamp.org/news/python-for-loop-example-how-to-write-loops-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/forLoop.png
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: Exemple de boucle For en Python – Comment écrire des boucles en Python
seo_desc: 'If you are just getting started in Python, for loops are one of the fundamentals
  you should learn how to use.

  In the Python programming language, for loops are also called “definite loops” because
  they perform the instruction a certain number of time...'
---

Si vous débutez en Python, les boucles for sont l'un des fondamentaux que vous devez apprendre à utiliser.

Dans le langage de programmation Python, les boucles for sont également appelées « boucles définies » car elles exécutent l'instruction un certain nombre de fois.

Cela contraste avec les boucles while, ou boucles indéfinies, qui exécutent une action jusqu'à ce qu'une condition soit remplie et qu'on leur dise de s'arrêter.

Les boucles for sont utiles lorsque vous souhaitez exécuter le même code pour chaque élément d'une séquence donnée. Avec une boucle for, vous pouvez itérer sur n'importe quelle donnée itérable telle que les listes, les ensembles, les tuples, les dictionnaires, les plages et même les chaînes de caractères.

Dans cet article, je vais vous montrer comment fonctionne la boucle for en Python. Vous apprendrez également le mot-clé que vous pouvez utiliser lors de l'écriture de boucles en Python.

## Syntaxe de base d'une boucle For en Python

La syntaxe de base ou la formule des boucles for en Python ressemble à ceci :

```py
for i in data:
    faire quelque chose
```

- `i` représente l'itérateur. Vous pouvez le remplacer par ce que vous voulez
- `data` représente n'importe quelle donnée itérable telle que les listes, les tuples, les chaînes de caractères et les dictionnaires
- La chose suivante que vous devez faire est de taper un deux-points puis d'indenter. Vous pouvez le faire avec une tabulation ou appuyer sur la barre d'espace 4 fois.

## Exemple de boucle For en Python
Comme je l'ai mentionné ci-dessus, vous pouvez itérer sur n'importe quelle donnée itérable avec une boucle for.

### Comment itérer sur une chaîne de caractères avec une boucle For
Vous pouvez itérer sur une chaîne de caractères comme montré ci-dessous :
```py
name = "freeCodeCamp"

for letter in name:
    print(letter)
```
Cela imprimera toutes les lettres de la chaîne individuellement :
```py
# Sortie :
# f
# r
# e
# e
# C
# o
# d
# e
# C
# a
# m
# p
```

Que faire si vous souhaitez imprimer les lettres sur une seule ligne ?

Vous pouvez le faire en passant un espace blanc au paramètre `end` directement dans l'instruction `print()`. Avec cela, vous dites à Python que vous voulez un espace blanc au lieu d'une nouvelle ligne dans la console.

```py
name = "freeCodeCamp"

for letter in name:
    print(letter, end=" ")

# Sortie : f r e e C o d e C a m p 
```

### Comment itérer sur une liste avec une boucle For

Pour itérer sur une liste avec la boucle for, définissez la liste comme une donnée séparée puis écrivez la boucle for, comme ceci :

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    print(lang)

# Sortie :
# Python
# JavaScript
# PHP       
# Rust      
# Solidity  
# Assembly  
```

N'oubliez pas que vous pouvez imprimer tous les éléments en une seule ligne avec le mot-clé end :

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    print(lang, end=" ")

# Sortie : Python JavaScript PHP Rust Solidity Assembly 
```

### Comment itérer sur un tuple avec une boucle For
Un tuple est un type de donnée itérable en Python, donc vous pouvez écrire une boucle for pour imprimer les éléments qu'il contient.
```py
footballers_tuple = ("Ronaldo", "Mendy", "Lukaku", "Lampard", "Messi", "Pogba")

for footballer in footballers_tuple:
    print(footballer, end=" ")

# Sortie : Ronaldo Mendy Lukaku Lampard Messi Pogba 
```

Vous pouvez être un peu plus créatif en faisant savoir aux gens que les noms dans le tuple représentent certains footballeurs actifs :

```py
footballers_tuple = ("Ronaldo", "Mendy", "Lukaku", "Lampard", "Messi", "Pogba")

for footballer in footballers_tuple:
    print(footballer, "est un footballeur actif")

# Sortie :
# Ronaldo est un footballeur actif
# Mendy est un footballeur actif  
# Lukaku est un footballeur actif 
# Lampard est un footballeur actif
# Messi est un footballeur actif  
# Pogba est un footballeur actif  
```

### Comment itérer sur un ensemble avec une boucle For

Vous pouvez imprimer les éléments individuels d'un ensemble avec la boucle for comme ceci :

```py
soc_set = {"Twitter", "Facebook", "Instagram", "Quora"}

for platform in soc_set:
    print(platform, end=" ")

# Sortie : Twitter Facebook Instagram Quora
```

Vous pouvez également être plus créatif avec cela. Dans l'exemple ci-dessous, avec l'aide d'une instruction if, j'ai pu imprimer la plateforme qui est sur le point d'être achetée par Elon Musk :

```py
soc_set = {"Twitter", "Facebook", "Instagram", "Quora"}

for platform in soc_set:
    if(platform == "Twitter"):
        print(platform, "est sur le point d'être acheté par Elon Musk.")

# Sortie : Twitter est sur le point d'être acheté par Elon Musk.
```

### Comment itérer sur un dictionnaire avec une boucle For

Un dictionnaire est une collection de données sous forme de paires clé-valeur. Un dictionnaire est probablement le type de donnée avec lequel vous pouvez faire le plus de choses en utilisant une boucle for.

Par exemple, vous pouvez obtenir les clés d'un dictionnaire en parcourant celui-ci :

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for key in fcc_dict:
    print(key, end=" ")

# Sortie : name type mode paid 
```

Vous pouvez également obtenir les valeurs avec une boucle for :

```py
for values in fcc_dict.values():
    print(values , end=" ")

# Sortie : freeCodeCamp non-profit remote no 
```

Vous pouvez obtenir les clés et les valeurs d'un dictionnaire avec une boucle for :

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for key, value in fcc_dict.items():
    print(key, value)

# Sortie :
# name freeCodeCamp
# type non-profit
# mode remote
# paid no
```

Je ne connais aucun autre langage de programmation qui peut faire cela d'une manière aussi élégante et propre !

Vous pouvez même remplacer `key, value` par ce que vous voulez et cela fonctionnera toujours comme prévu :

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for a, b in fcc_dict.items():
    print(a, b)

# Sortie :
# name freeCodeCamp
# type non-profit
# mode remote
# paid no
```

Vous pouvez également exécuter une instruction particulière lorsque l'itération atteint une certaine clé. Dans l'exemple ci-dessous, j'ai imprimé « freeCodeCamp est une organisation à but non lucratif » dans la console lorsque la clé est égale à `type` :

```py
fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for a, b in fcc_dict.items():
    # print(a, b)
    if a == "type":
        print("freeCodeCamp est une organisation à but non lucratif")

# Sortie : freeCodeCamp est une organisation à but non lucratif
```

### Comment itérer sur des nombres avec une boucle For en utilisant la fonction `range()`

Itérer à travers un entier génère l'erreur populaire `int object not iterable` en Python. Mais vous pouvez contourner cela en utilisant la fonction `range()` pour spécifier que vous souhaitez itérer à travers les nombres entre deux nombres certains.

La fonction `range()` accepte deux arguments, donc vous pouvez parcourir les nombres compris entre les deux arguments. Exemple ci-dessous :

```py
for i in range(1, 10):
    print(i, end="")

# Sortie : 123456789
```

Vous pouvez extraire la plage dans une variable et cela fonctionnera toujours :

```py
my_num = range(1, 10)

for i in my_num:
    print(i, end="")

# Sortie : 123456789
```

Notez que le résultat inclut le premier nombre mais exclut le second nombre.

## Comment utiliser le mot-clé Break en Python
Vous pouvez utiliser le mot-clé `break` pour arrêter la boucle avant qu'elle ne se termine.

Dans l'exemple ci-dessous, l'exécution n'a pas atteint Solidity et Assembly car j'ai interrompu la boucle lorsque `lang` était égal à Rust :

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    if lang == "Rust":
        break
    print(lang, end=" ")
# Sortie : Python JavaScript PHP 
```

## Comment utiliser le mot-clé Continue en Python
Vous pouvez utiliser le mot-clé `continue` pour sauter l'itération actuelle et continuer avec le reste.

Dans l'exemple ci-dessous, avec le mot-clé continue, j'ai fait en sorte que la boucle saute PHP et continue la boucle après celui-ci :

```py
lang_list = ["Python", "JavaScript", "PHP", "Rust", "Solidity", "Assembly"]

for lang in lang_list:
    if lang == "PHP":
        continue
    print(lang, end=" ")

# Sortie : Python JavaScript Rust Solidity Assembly 
```

## Comment utiliser le mot-clé Else en Python
Vous pouvez utiliser le mot-clé `else` pour spécifier qu'un bloc de code doit s'exécuter après la fin de la boucle :

```py
for i in range(10):
    print(i)
else:
    print("Do + ne = Done")

# Sortie :
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Do + ne = Done
```

## Conclusion
La boucle for en Python ne semble pas aussi compliquée que dans de nombreux autres langages de programmation. Mais son implémentation reste puissante lorsqu'elle s'exécute.

La boucle for est une fonctionnalité très puissante de Python avec laquelle vous pouvez accomplir beaucoup de choses.

Merci d'avoir lu. Si vous trouvez cet article utile, partagez-le avec vos amis et votre famille !