---
title: Fonction Python str() – Comment convertir en chaîne de caractères
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-04-04T12:48:48.000Z'
originalURL: https://freecodecamp.org/news/python-str-function-how-to-convert-to-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/str-2.png
tags:
- name: Python
  slug: python
- name: Python 3
  slug: python3
seo_title: Fonction Python str() – Comment convertir en chaîne de caractères
seo_desc: 'Python’s primitive data types include float, integer, Boolean, and string.
  The programming language provides several functions you can use to convert any of
  these data types to the other.

  One of those functions we’ll look at in this article is str()....'
---

Les types de données primitifs de Python incluent float, integer, Boolean et string. Le langage de programmation fournit plusieurs fonctions que vous pouvez utiliser pour convertir l'un de ces types de données en un autre.

L'une de ces fonctions que nous allons examiner dans cet article est `str()`. Il s'agit d'une fonction intégrée que vous pouvez utiliser pour convertir tout objet non-chaine en une chaîne de caractères.


## Qu'est-ce que la fonction `str()` ?
La fonction `str()` prend un objet non-chaine obligatoire et le convertit en une chaîne de caractères. Cet objet que la fonction `str()` prend peut être un float, un integer ou même un Boolean.

Outre les données obligatoires à convertir en une chaîne de caractères, la fonction `str()` prend également deux autres paramètres. Voici tous les paramètres qu'elle prend :

* **object** : les données que vous souhaitez convertir en une chaîne de caractères. Il s'agit d'un paramètre obligatoire. Si vous ne le fournissez pas, `str()` retourne une chaîne vide comme résultat.
* **encoding** : l'encodage des données à convertir. Il est généralement `UTF-8`. La valeur par défaut est `UTF-8` lui-même.
* **errors** : spécifie quoi faire si le décodage échoue. Les valeurs que vous pouvez utiliser pour ce paramètre incluent `strict`, `ignore`, `replace`, et autres.


## Syntaxe de base de la fonction `str()`
Vous devez séparer chaque paramètre de la fonction `str()` par une virgule, et les valeurs de l'encodage et des erreurs doivent être en chaînes de caractères :

```py
str(object_to_convert, encoding='encoding', errors='errors')
``` 

## Comment utiliser la fonction `str()`
Tout d'abord, voyons comment utiliser tous les paramètres de la fonction `str()` :

```py
my_num = 45
converted_my_num = str(my_num, encoding='utf-8', errors='errors')

print(converted_my_num)
```

Si vous exécutez le code, vous obtiendrez cette erreur :

```py
converted_my_num = str(my_num, encoding='utf-8', errors='errors')
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: decoding to str: need a bytes-like object, int found
```

Cette erreur se produit parce que vous utilisez le paramètre d'encodage sans fournir un objet bytes. Dans ce cas, vous n'avez pas besoin du tout de l'`encoding` et des `errors`. Vous avez seulement besoin du nombre que vous souhaitez convertir :

```py
my_num = 45
converted_my_num = str(my_num)

print(converted_my_num) # 45
```

Si vous insistez pour utiliser les paramètres `encoding` et `errors`, alors l'objet à convertir doit être un objet bytes :

```py
my_num = b'45'
converted_my_num = str(my_num, encoding='utf-8', errors='strict')

print(converted_my_num) # 45
```

### Comment convertir un entier et un float en chaîne de caractères avec la fonction `str()`
Vous pouvez convertir un entier ou un float en chaîne de caractères avec str() de cette manière :

```py
my_int = 45
my_float = 34.8

# Convertir les deux en chaîne de caractères
converted_my_int = str(my_int)
converted_my_float = str(my_float)

print(converted_my_int) # sortie: 45
print(converted_my_float) # sortie: 34.8
```

Vous pouvez voir que j'ai récupéré les nombres. Vous pouvez également vérifier que les types des résultats sont des chaînes de caractères avec la fonction `type()` :

```py
my_int = 45
my_float = 34.8

# Convertir les deux en chaîne de caractères
converted_my_int = str(my_int)
converted_my_float = str(my_float)

print("Converted integer is", converted_my_int, "and the type of the result is ", type(converted_my_int)) # Converted integer is 45 and the type of the result is <class 'str'>
print("Converted float is", converted_my_float, "and the type of the result is ", type(converted_my_float)) # Converted float is 34.8 and the type of the result is <class 'str'>
```

Vous pouvez voir que le type de l'entier et du float convertis est une chaîne de caractères.

### Comment convertir un Boolean en chaîne de caractères avec la fonction `str()`
Vous pouvez également convertir un Boolean en une chaîne de caractères si vous le souhaitez :

```py
my_true_bool = True
my_false_bool = False

converted_my_true_bool = str(my_true_bool)
converted_my_false_bool = str(my_false_bool)

print("Converted Boolean is", converted_my_true_bool, "and the type of the result is ", type(converted_my_true_bool)) # Converted Boolean is True and the type of the result is <class 'str'>

print("Converted Boolean is", converted_my_false_bool, "and the type of the result is ", type(converted_my_false_bool)) # Converted Boolean is False and the type of the result is <class 'str'>
```

## Comment utiliser le paramètre `encoding` de la fonction `str()` pour encoder et décoder des objets
Le paramètre `encoding` est utile pour encoder une chaîne de caractères en bytes et décoder des bytes en chaînes de caractères.

Pour encoder une chaîne de caractères en bytes, par exemple, vous devez utiliser la méthode `encoding()` de cette manière :

```py
my_str = "Hello world!"
my_bytes = my_str.encode(encoding='UTF-8', errors='strict')

print(my_bytes) # Output: b'Hello, world!'
print(type(my_bytes)) # Output: <class 'bytes'>
```

Pour décoder des bytes en chaîne de caractères, vous devez utiliser la méthode `decode()` de cette manière :

```py
my_bytes = b'Hello, world!'
my_str = my_bytes.decode(encoding='UTF-8', errors='strict')

print(my_str)  # Output: "Hello, world!"
print(type(my_str))  # Output: <class 'str'>
```


## Conclusion
Vous avez vu que la fonction `str()` est instrumentale pour convertir des objets non-chaine et des types de données primitifs en chaînes de caractères.

Vous vous demandez peut-être si vous pouvez utiliser la fonction `str()` pour convertir des données itérables comme les listes, les tuples et les dictionnaires en une chaîne de caractères. Eh bien, vous n'obtenez pas d'erreur si vous faites cela, ce que vous obtiendrez en retour est l'itérable tel quel :

```py
my_list = ['ant', 'soldier', 'termite']
converted_my_list = str(my_list)

print(converted_my_list) # ['ant', 'soldier', 'termite']
```

Pour convertir la liste en une chaîne de caractères, vous devez utiliser la méthode `join()` :

```py
my_list = ['ant', 'soldier', 'termite']
converted_my_list =' '.join(my_list)

print(converted_my_list) # ant, soldier, termite
print(type(converted_my_list)) # <class 'str'>
```

La même chose est applicable aux dictionnaires et aux tuples.

Merci d'avoir lu.