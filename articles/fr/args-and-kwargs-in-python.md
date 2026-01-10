---
title: Comment utiliser *args et **kwargs en Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-03-23T18:55:00.000Z'
originalURL: https://freecodecamp.org/news/args-and-kwargs-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/args.png
tags:
- name: Python
  slug: python
seo_title: Comment utiliser *args et **kwargs en Python
seo_desc: "In this article, we'll discuss *args and ****kwargs** in Python along with\
  \ their uses and some examples.\nWhen writing a function, we often need to pass\
  \ values to the function. These values are called function arguments. \nProblem\
  \ with Function Argumen..."
---

Dans cet article, nous allons discuter de **`*args`** et **`**kwargs`** en Python ainsi que de leurs utilisations et de quelques exemples.

Lors de l'écriture d'une fonction, nous avons souvent besoin de passer des valeurs à la fonction. Ces valeurs sont appelées **arguments de fonction**.

## Problème avec les arguments de fonction

Définissons une fonction pour additionner deux nombres en Python. Nous l'écrirons comme ceci :

```python
def add(x, y):
    return x+y

print(add(2,3))
```

Sortie :

```bash
5
```

Et si vous avez besoin d'additionner trois nombres ? C'est simple, nous pouvons modifier la fonction pour qu'elle accepte trois arguments et renvoie leur somme ainsi :

```python
def add(x, y, z):
    return x+y+z

print(add(2, 3, 5))
```

Sortie :

```bash
10
```

N'était-ce pas assez simple ? Oui, ça l'était !

Mais que se passe-t-il si nous ne devons à nouveau additionner que deux nombres ? Notre fonction modifiée nous aidera-t-elle à obtenir la somme ? Voyons voir :

```python
def add(x, y, z):
    return x+y+z


print(add(2, 3))
```

Sortie :

```bash
Traceback (most recent call last):
  File "D:\\Quarantine\\Test\\Blog-Codes\\args-kwargs\\main.py", line 14, in <module>
    print(add(2, 3))
TypeError: add() missing 1 required positional argument: 'z'
```

Vous voyez le problème ?

Le problème survient lorsque nous avons un nombre variable d'arguments. Devons-nous continuer à modifier la fonction pour qu'elle accepte le nombre exact d'arguments ? Bien sûr que non, nous ne ferons pas cela.

Il doit donc y avoir un autre moyen de le faire. C'est ici que **`*args`** et **`**kwargs`** interviennent.

Vous pouvez utiliser `*args` et `**kwargs` comme arguments d'une fonction lorsque vous n'êtes pas sûr du nombre d'arguments à passer dans les fonctions.

## Comment utiliser *args en Python

**`*args`** nous permet de passer un nombre variable d'arguments non-nommés (arguments positionnels) à une fonction Python. Dans la fonction, nous devons utiliser un astérisque (**`*`**) devant le nom du paramètre pour passer un nombre variable d'arguments.

```python
def add(*args):
    # Affiche les arguments et leur type
    print(args, type(args))

add(2, 3)
```

Sortie :

```bash
(2, 3) <class 'tuple'>
```

Ainsi, nous sommes sûrs que ces arguments passés forment un tuple à l'intérieur de la fonction avec le même nom que le paramètre, à l'exclusion de **`*`**.

Maintenant, réécrivons notre fonction `**add()**` avec un nombre variable d'arguments.

```python
def add(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(add(2, 3))
print(add(2, 3, 5))
print(add(2, 3, 5, 7))
print(add(2, 3, 5, 7, 9))
```

Sortie :

```bash
5
10
17
26
```

Notez que le nom de l'argument n'est pas nécessairement `**args**` – il peut être n'importe quoi. Dans ce cas, c'est `**numbers**`. Mais c'est généralement une pratique standard d'utiliser `***args**` comme nom.

## Comment utiliser **kwargs en Python

**`**kwargs`** nous permet de passer un nombre variable d'arguments nommés (keyword arguments) à une fonction Python. Dans la fonction, nous utilisons le double astérisque (**`**`**) devant le nom du paramètre pour désigner ce type d'argument.

```python
def total_fruits(**kwargs):
    # Affiche les kwargs et leur type
    print(kwargs, type(kwargs))


total_fruits(banana=5, mango=7, apple=8)
```

Sortie :

```bash
{'banana': 5, 'mango': 7, 'apple': 8} <class 'dict'>
```

Ainsi, nous voyons que les arguments, dans ce cas, sont passés sous forme de [dictionnaire](https://ireadblog.com/posts/127/everything-you-need-to-know-about-python-dictionaries) et ces arguments forment un dictionnaire à l'intérieur de la fonction avec le même nom que le paramètre, à l'exclusion de **`**`**.

Maintenant, complétons la fonction `**total_fruits()**` pour renvoyer le nombre total de fruits.

```python
def total_fruits(**fruits):
    total = 0
    for amount in fruits.values():
        total += amount
    return total


print(total_fruits(banana=5, mango=7, apple=8))
print(total_fruits(banana=5, mango=7, apple=8, oranges=10))
print(total_fruits(banana=5, mango=7))
```

Sortie :

```bash
20
30
12
```

Notez que le nom de l'argument n'est pas nécessairement `**kwargs**` – encore une fois, il peut être n'importe quoi. Dans ce cas, c'est `**fruits**`. Mais c'est généralement une pratique standard d'utiliser `****kwargs**` comme nom.

## Conclusion

Dans cet article, nous avons découvert deux mots-clés spéciaux en Python – **`*args`** et **`**kwargs`**. Ceux-ci rendent une fonction Python flexible afin qu'elle puisse accepter un nombre variable d'arguments et d'arguments nommés, respectivement.

Merci pour votre lecture !

Vous pouvez trouver le code de ce blog [ici](https://gist.github.com/ashutoshkrris/fe85f95ced7f0df2488aef122a7e1910).