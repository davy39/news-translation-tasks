---
title: Comment fonctionne la fonction Lambda en Python – Expliqué avec des exemples
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-10-25T20:37:45.000Z'
originalURL: https://freecodecamp.org/news/python-lambda-function-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/pexels-pixabay-45246--1-.jpg
tags:
- name: Python
  slug: python
seo_title: Comment fonctionne la fonction Lambda en Python – Expliqué avec des exemples
seo_desc: 'One of the beautiful things about Python is that it is generally one of
  the most intuitive programming languages out there. Still, certain concepts can
  be difficult to grasp and comprehend. The lambda function is one of them.

  I''ve been there. When I ...'
---

L'une des belles choses à propos de Python est qu'il s'agit généralement de l'un des langages de programmation les plus intuitifs qui existent. Pourtant, certains concepts peuvent être difficiles à comprendre. La fonction lambda en est un exemple.

J'ai été à votre place. Lorsque j'ai commencé à apprendre Python, j'ai sauté la fonction lambda car elle n'était pas claire pour moi. Mais avec le temps, j'ai commencé à la comprendre. Alors ne vous inquiétez pas – si vous avez du mal avec elle, je vous couvre.

Ce tutoriel vous apprendra ce qu'est une fonction lambda, quand l'utiliser, et nous passerons en revue quelques cas d'utilisation courants où la fonction lambda est couramment appliquée. Sans plus attendre, commençons.

## Qu'est-ce qu'une fonction Lambda ?

Les fonctions lambda sont similaires aux fonctions définies par l'utilisateur mais sans nom. Elles sont communément appelées fonctions anonymes.

Les fonctions lambda sont efficaces lorsque vous souhaitez créer une fonction qui ne contiendra que des expressions simples – c'est-à-dire des expressions qui sont généralement une seule ligne d'instruction. Elles sont également utiles lorsque vous souhaitez utiliser la fonction une seule fois.

## Comment définir une fonction Lambda

Vous pouvez définir une fonction lambda comme ceci :

```python
lambda argument(s) : expression
```

1. `lambda` est un mot-clé en Python pour définir la fonction anonyme.

2. `argument(s)` est un espace réservé, c'est-à-dire une variable qui sera utilisée pour contenir la valeur que vous souhaitez passer dans l'expression de la fonction. Une fonction lambda peut avoir plusieurs variables selon ce que vous souhaitez réaliser.

3. `expression` est le code que vous souhaitez exécuter dans la fonction lambda.

Remarquez que la fonction anonyme n'a pas de mot-clé return. Cela est dû au fait que la fonction anonyme retournera automatiquement le résultat de l'expression dans la fonction une fois qu'elle est exécutée.

Regardons un exemple de fonction lambda pour voir comment elle fonctionne. Nous la comparerons à une fonction définie par l'utilisateur régulière.

Supposons que je veuille écrire une fonction qui retourne le double du nombre que je lui passe. Nous pouvons définir une fonction définie par l'utilisateur comme suit :

```python
def f(x):
  return x * 2

f(3)
>> 6
```

Maintenant pour une fonction lambda. Nous la créerons comme ceci :

```python
lambda x: x * 3
```

Comme je l'ai expliqué ci-dessus, la fonction lambda n'a pas de mot-clé return. Par conséquent, elle retournera le résultat de l'expression par elle-même. Le x dans celle-ci sert également d'espace réservé pour la valeur à passer dans l'expression. Vous pouvez le changer en ce que vous voulez.

Maintenant, si vous souhaitez appeler une fonction lambda, vous utiliserez une approche connue sous le nom d'invocation immédiate de la fonction. Cela ressemble à ceci :

```python
(lambda x : x * 2)(3)

>> 6
```

La raison en est que, puisque la fonction lambda n'a pas de nom que vous pouvez invoquer (elle est anonyme), vous devez enfermer toute l'instruction lorsque vous souhaitez l'appeler.

## Quand devez-vous utiliser une fonction Lambda ?

Vous devez utiliser la fonction lambda pour créer des expressions simples. Par exemple, des expressions qui n'incluent pas de structures complexes telles que if-else, for-loops, etc.

Ainsi, par exemple, si vous souhaitez créer une fonction avec une boucle for, vous devez utiliser une fonction définie par l'utilisateur.

## Cas d'utilisation courants des fonctions Lambda

### Comment utiliser une fonction Lambda avec des itérables

Un itérable est essentiellement tout ce qui consiste en une série de valeurs, telles que des caractères, des nombres, etc.

En Python, les itérables incluent les chaînes de caractères, les listes, les dictionnaires, les plages, les tuples, etc. Lorsque vous travaillez avec des itérables, vous pouvez utiliser des fonctions lambda en conjonction avec deux fonctions courantes : `filter()` et `map()`.

#### `Filter()`

Lorsque vous souhaitez vous concentrer sur des valeurs spécifiques dans un itérable, vous pouvez utiliser la fonction filter. Voici la syntaxe d'une fonction filter :

```python
filter(function, iterable)
```

Comme vous pouvez le voir, une fonction filter nécessite une autre fonction qui contient l'expression ou les opérations qui seront effectuées sur l'itérable.

Par exemple, supposons que j'ai une liste telle que `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`. Maintenant, supposons que je ne m'intéresse qu'à ces valeurs dans cette liste qui ont un reste de 0 lorsqu'elles sont divisées par 2. Je peux utiliser `filter()` et une fonction lambda.

Tout d'abord, j'utiliserai la fonction lambda pour créer l'expression que je veux dériver comme ceci :

```python
lambda x: x % 2 == 0
```

Ensuite, je l'insérerai dans la fonction filter comme ceci :

```python
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter(lambda x: x % 2 == 0, list1)

>> <filter at 0x1e3f212ad60> # Le résultat est toujours un objet filter, donc je devrai le convertir en liste en utilisant list()

list(filter(lambda x: x % 2 == 0, list1))
>> [2, 4, 6, 8, 10]
```

#### `Map()`

Vous utilisez la fonction `map()` chaque fois que vous souhaitez modifier chaque valeur dans un itérable.

```python
map(function, iterable)
```

Par exemple, supposons que je veuille élever toutes les valeurs dans la liste ci-dessous à la puissance de 2. Je peux facilement le faire en utilisant les fonctions lambda et map comme ceci :

```python
list1 = [2, 3, 4, 5]

list(map(lambda x: pow(x, 2), list1))
>> [4, 9, 16, 25]
```

### Séries Pandas

Un autre endroit où vous utiliserez les fonctions lambda est en science des données lors de la création d'un cadre de données à partir de Pandas. Une série est une colonne de cadre de données. Vous pouvez manipuler toutes les valeurs d'une série en utilisant la fonction lambda.

Par exemple, si j'ai un cadre de données avec les colonnes suivantes et que je souhaite convertir les valeurs de la colonne nom en minuscules, je peux le faire en utilisant la fonction apply de Pandas et une fonction lambda Python comme ceci :

```python
import pandas as pd

df = pd.DataFrame(
    {"name": ["IBRAHIM", "SEGUN", "YUSUF", "DARE", "BOLA", "SOKUNBI"],
     "score": [50, 32, 45, 45, 23, 45]
    }
)
```

![image](https://user-images.githubusercontent.com/73393430/188447505-9ae1baa2-9225-4834-a630-c32b9d1a29f3.png align="left")

```python
df["lower_name"] = df["name"].apply(lambda x: x.lower())
```

La fonction apply appliquera chaque élément de la série à la fonction lambda. La fonction lambda retournera ensuite une valeur pour chaque élément en fonction de l'expression que vous lui avez passée. Dans notre cas, l'expression était de mettre chaque élément en minuscules.

![image](https://user-images.githubusercontent.com/73393430/188447749-a483bbad-a91f-40df-b008-5695efe05073.png align="left")

## Conclusion

Dans ce tutoriel, vous avez appris les bases de la fonction lambda et comment vous pouvez l'appliquer couramment. Merci d'avoir pris le temps de lire ceci.