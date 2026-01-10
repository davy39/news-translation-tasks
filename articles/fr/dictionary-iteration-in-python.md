---
title: Itération de dictionnaire en Python – Comment itérer sur un dictionnaire avec
  une boucle For
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-01-06T23:16:43.000Z'
originalURL: https://freecodecamp.org/news/dictionary-iteration-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-stas-knop-1194723.jpg
tags:
- name: Python
  slug: python
seo_title: Itération de dictionnaire en Python – Comment itérer sur un dictionnaire
  avec une boucle For
seo_desc: "In Python, a dictionary is one of the built-in data structures (the others\
  \ are tuples, lists, and sets). A dictionary is a collection of key:value pairs\
  \ and you can use them to solve various programming problems. \nDictionaries are\
  \ very flexible to wo..."
---

En Python, un dictionnaire est l'une des structures de données intégrées (les autres sont les tuples, les listes et les ensembles). Un dictionnaire est une collection de paires clé:valeur et vous pouvez les utiliser pour résoudre divers problèmes de programmation. 

Les dictionnaires sont très flexibles à utiliser. Vous pouvez obtenir les clés et les valeurs séparément, ou même ensemble.

Cet article traite de la boucle sur un dictionnaire avec la boucle `for`, mais vous pouvez également parcourir un dictionnaire avec trois méthodes :

- la méthode `key()` : obtient les clés d'un dictionnaire 
- la méthode `values()` : obtient les valeurs d'un dictionnaire 
- la méthode `items()` : obtient à la fois les clés et les valeurs d'un dictionnaire 

Dans l'exemple ci-dessous, j'utilise ces 3 méthodes pour obtenir les clés, les valeurs et les éléments du dictionnaire.

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

# Clés
states_keys = states_tz_dict.keys()
print(states_keys) # dict_keys(['Florida', 'Hawaii', 'Arizona', 'Colorado', 'Idaho', 'Texas', 'Washington', 'Wisconsin'])

# Valeurs
tz_values = states_tz_dict.values()
print(tz_values) # dict_values(['EST and CST', 'HST', 'DST', 'MST', 'MST and PST', 'CST and MST', 'PST', 'CST']) 

# Clés et valeurs
states_tz_dict_items = states_tz_dict.items()
print(states_tz_dict_items) # dict_items([('Florida', 'EST and CST'), ('Hawaii', 'HST'), ('Arizona', 'DST'), ('Colorado', 'MST'), ('Idaho', 'MST and PST'), ('Texas', 'CST and MST'), ('Washington', 'PST'), ('Wisconsin', 'CST')])
```

Ce sont quelques itérations que nous avons faites. Mais vous pouvez également parcourir un dictionnaire avec une boucle `for`. C'est ce que nous allons examiner dans ce tutoriel.

## Ce que nous allons couvrir
- [Comment itérer à travers un dictionnaire avec une boucle `for`](#heading-comment-iterer-a-travers-un-dictionnaire-avec-une-boucle-for)
- [Comment itérer à travers les clés d'un dictionnaire avec une boucle `for`](#heading-comment-iterer-a-travers-les-cles-dun-dictionnaire-avec-une-boucle-for)
  - [Comment itérer à travers les valeurs d'un dictionnaire avec une boucle `for`](#heading-comment-iterer-a-travers-les-valeurs-dun-dictionnaire-avec-une-boucle-for)
  - [Comment itérer à travers les éléments d'un dictionnaire avec une boucle `for`](#heading-comment-iterer-a-travers-les-elements-dun-dictionnaire-avec-une-boucle-for)
- [Comment parcourir un dictionnaire et le convertir en une liste de tuples](#heading-comment-parcourir-un-dictionnaire-et-le-convertir-en-une-liste-de-tuples)
- [Conclusion](#heading-conclusion)

## Comment itérer à travers un dictionnaire avec une boucle `for`

Avec la boucle `for` de Python, vous pouvez parcourir les clés, les valeurs ou les éléments d'un dictionnaire. Vous pouvez également parcourir le dictionnaire et placer la paire clé:valeur dans une liste de tuples. Nous allons les examiner un par un.

### Comment itérer à travers les clés d'un dictionnaire avec une boucle `for`
Vous vous souvenez comment j'ai obtenu les clés du dictionnaire avec la méthode `keys()` dans la première partie de cet article ? Vous pouvez utiliser la même méthode dans une boucle `for` et assigner chacune des clés à une variable que nous pouvons appeler `k` :

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

for k in states_tz_dict.keys():
    print(k)

# Résultat:
# Florida   
# Hawaii    
# Arizona   
# Colorado  
# Idaho     
# Texas     
# Washington
# Wisconsin
```

### Comment itérer à travers les valeurs d'un dictionnaire avec une boucle `for`
Vous pouvez également utiliser la méthode `values()` dans une boucle `for`, et assigner les valeurs à une variable que vous pouvez appeler `v` :

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

for v in states_tz_dict.values():
    print(v)
    
# Résultat:
# EST and CST
# HST        
# DST        
# MST        
# MST and PST
# CST and MST
# PST        
# CST
```

### Comment itérer à travers les éléments d'un dictionnaire avec une boucle `for`
La méthode `items()` est utile pour obtenir les clés et les valeurs à l'intérieur d'une boucle `for`. Cette fois-ci, vous devez assigner deux variables au lieu d'une :

```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

for k, v in states_tz_dict.items():
    print(k, "--->", v)

# Résultat:
# Florida ---> EST and CST
# Hawaii ---> HST
# Arizona ---> DST        
# Colorado ---> MST       
# Idaho ---> MST and PST  
# Texas ---> CST and MST  
# Washington ---> PST     
# Wisconsin ---> CST 
```

**Note** : Vous pouvez utiliser n'importe quelle lettre pour la ou les variables dans une boucle `for`. Ce n'est pas obligatoirement k ou v, ou k, v. 


### Comment parcourir un dictionnaire et le convertir en une liste de tuples
Pour convertir un dictionnaire en une liste de tuples en Python, vous devez toujours utiliser la méthode `items()` à l'intérieur d'une boucle `for`. 

Mais cette fois-ci, vous devez entourer la boucle avec des crochets. Vous devez également assigner la boucle à une variable séparée et envelopper la variable pour les clés et les valeurs dans des crochets : 
```py
states_tz_dict = {
    'Florida': 'EST and CST',
    'Hawaii': 'HST',
    'Arizona': 'DST',
    'Colorado': 'MST',
    'Idaho': 'MST and PST',
    'Texas': 'CST and MST',
    'Washington': 'PST',
    'Wisconsin': 'CST'
}

list_of_tuples = [(k, v) for k, v in states_tz_dict.items()]
print(list_of_tuples)

# Résultat: [('Florida', 'EST and CST'), ('Hawaii', 'HST'), ('Arizona', 'DST'), ('Colorado', 'MST'), ('Idaho', 'MST and PST'), ('Texas', 'CST 
# and MST'), ('Washington', 'PST'), ('Wisconsin', 'CST')]
```


## Conclusion
Dans ce tutoriel, nous avons examiné comment itérer à travers un dictionnaire avec la boucle `for`. 

Si vous ne voulez pas utiliser une boucle `for`, vous pouvez également utiliser l'une des méthodes `keys()`, `values()` ou `items()` directement comme je l'ai fait dans la première partie de cet article.

Si vous trouvez cet article utile, n'hésitez pas à le partager sur les réseaux sociaux.