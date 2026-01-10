---
title: Tuple Python VS Liste – Quelle est la différence ?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-09-20T21:15:57.000Z'
originalURL: https://freecodecamp.org/news/python-tuple-vs-list-what-is-the-difference
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-christina-morillo-1181359--1-.jpg
tags:
- name: Python
  slug: python
seo_title: Tuple Python VS Liste – Quelle est la différence ?
seo_desc: 'Tuples and lists are two of the four available built-in data types that
  you can use to store data in Python.

  They are both useful and they might seem similar at first glance. But they have
  significant differences and each one is best used in differen...'
---

Les tuples et les listes sont deux des quatre types de données intégrés disponibles que vous pouvez utiliser pour stocker des données en Python.

Ils sont tous deux utiles et peuvent sembler similaires à première vue. Mais ils ont des différences significatives et chacun est mieux utilisé dans différents cas.

Cet article vous donnera un aperçu de la façon dont les tuples et les listes fonctionnent. Nous discuterons de leurs caractéristiques individuelles et de leurs cas d'utilisation uniques, et je présenterai leurs similitudes et différences tout au long.

Vous pouvez essayer les exemples de code présentés dans l'article en utilisant l'interpréteur Python interactif, que vous obtenez lorsque vous installez Python sur votre ordinateur.

Commençons !

## Qu'est-ce que les Tuples et les Listes en Python ?

Les tuples et les listes sont tous deux des structures de données intégrées en Python.

Ce sont des conteneurs qui vous permettent d'organiser vos données en vous permettant de stocker une collection ordonnée d'un ou plusieurs éléments.

Un tuple a une classe de 'tuple', `<class 'tuple'>`, et une liste a une classe de 'list', `<class 'list'>`.

Vous pouvez toujours utiliser la fonction intégrée `type()` et passer l'objet comme argument que vous souhaitez tester. Cela vous permet de vérifier s'il s'agit d'un tuple ou d'une liste.

Supposons que vous avez créé un tuple nommé `my_tuple`. Vous pouvez vérifier son type comme suit :

```python
>>>type(my_tuple)

#sortie
<class 'tuple'>
```

Cela est particulièrement utile pour le débogage.

Maintenant, regardons quelques autres similitudes entre les tuples et les listes.

## Similitudes entre les Tuples et les Listes en Python

Comme je l'ai mentionné précédemment, les tuples et les listes sont effectivement similaires, et ils partagent certaines caractéristiques que nous allons couvrir maintenant.

### Les tuples et les listes peuvent tous deux stocker plusieurs éléments sous une seule variable

Les tuples et les listes peuvent être vides ou contenir un ou même plusieurs éléments sous une seule variable.

La seule différence est dans la syntaxe : vous créez des tuples en entourant les éléments à l'intérieur avec des parenthèses ouvrantes et fermantes, `()`, tandis que les listes sont désignées et définies par la présence de crochets ouvrants et fermants, `[]`.

Pour créer un tuple *vide*, vous utilisez soit des parenthèses seules, `()`, soit la méthode de constructeur `tuple()`.

```python
>>>type(())
<class 'tuple'>

>>>my_tuple = ()

>>>type(my_tuple)
<class 'tuple'>

#ou..


>>>my_tuple = tuple()

>>>type(my_tuple)
<class 'tuple'>
```

Pour créer une liste *vide*, vous pouvez simplement utiliser deux crochets vides seuls ou appeler la méthode de constructeur `list()`.

```python
>>>type([])
<class 'list'>


>>>my_list = []

#ou..

>>>my_list = list()
```


Lors de la création d'un tuple avec *un seul élément*, n'oubliez pas d'ajouter une virgule à la fin.

```python
>>>age = (28,)
```

Si vous utilisez la méthode `tuple()` pour créer le tuple, n'oubliez pas qu'elle nécessite des doubles parenthèses.

```
>>>age = tuple((28,))

>>>type(age)
<class 'tuple'>
```

Si vous n'ajoutez pas la virgule finale, Python ne le reconnaîtra pas comme un tuple.

```python
>>>age = (28)

>>>type(age)
<class 'int'>
```


Lors de la création d'une liste avec *un seul élément*, vous n'avez pas à vous soucier d'ajouter la virgule finale.

```python
>>> age = [28]

>>> type(age)
<class 'list'>
```

Les éléments stockés sont généralement similaires par nature et sont liés les uns aux autres d'une certaine manière.

Vous pouvez créer un tuple ou une liste qui contient simplement une séquence de chaînes de caractères, simplement une séquence d'entiers, ou simplement une séquence de valeurs booléennes, chaque élément de la séquence étant séparé par une virgule.

Vous pouvez également créer un tuple ou une liste qui contient un mélange de différents types de données.

```python
>>>my_information = ["Dionysia",27,True,"Lemonaki",7,"Python",False]

#ou..

>>>my_information = list(("Dionysia",27,True,"Lemonaki",7,"Python",False))

print(my_information)
['Dionysia', 27, True, 'Lemonaki', 7, 'Python', False]
```

Les listes et les tuples peuvent contenir des éléments en double et les valeurs peuvent être répétées, apparaissant plusieurs fois.

```python
>>>information = ("Jimmy",50,True,"Kate",50)

>>>print(information)
('Jimmy', 50, True, 'Kate', 50)

ou..

>>>my_information = ["Dionysia",27,True,"Lemonaki",7,"Python",False,27,"Python",27]
```

Si vous oubliez les virgules, vous obtiendrez une erreur :

```python
>>>information = ("Jimmy" 50,True,"Kate",50)
File "<stdin>", line 1
    >>>information = ("Jimmy" 50,True,"Kate",50)
    ^
SyntaxError: invalid syntax
```

```python
>>>my_information = ["Dionysia" 28,True,"Lemonaki",7,"Python",False]
 File "<stdin>", line 1
    my_information = ["Dionysia" 28,True,"Lemonaki",7,"Python",False]
                                 ^
SyntaxError: invalid syntax
```

Pour vérifier la longueur et déterminer combien d'éléments il y a dans un tuple ou une liste, vous utilisez la méthode `len()`.

```python
>>>my_information = ["Dionysia",27,True,"Lemonaki",7,"Python",False,27,"Python",27]

>>>len(my_information)
7
```

### Les tuples et les listes en Python supportent tous deux le déballage

Essentiellement, lors de la création d'un tuple ou d'une liste, de nombreuses valeurs sont 'emballées' dans une seule variable comme je l'ai mentionné précédemment.

```python
>>>front_end = ("html","css","javascript")
```

Ces valeurs peuvent être 'déballées' et assignées à des variables individuelles.

```python
>>>front_end = ("html","css","javascript")

>>>content,styling,interactivity = front_end

>>>content
'html'

>>>styling
'css'

>>>interactivity
'javascript'
```


Assurez-vous que les variables que vous créez sont exactement du même nombre que les valeurs à l'intérieur du tuple/liste, sinon Python vous lancera une erreur :

```python
>>>front_end = ("html","css","javascript")

>>>content,styling = front_end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)


#ou..


>>>front_end = ("html","css","javascript")

>>>content,styling,interactivity,data =  front_end
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
```


### Vous pouvez accéder aux éléments par leur index dans les tuples et les listes en Python

Comme mentionné précédemment, les tuples et les listes sont tous deux une collection **ordonnée** d'éléments.

L'ordre est fixé et immuable, et il est préservé tout au long de la vie du programme.

L'ordre dans lequel les éléments sont spécifiés restera toujours le même depuis le moment où ils ont été créés.

Chaque valeur dans un tuple et une liste a un identifiant unique, également connu sous le nom d'index.

Chaque élément dans un tuple et une liste peut donc être accessible en référençant cet index.

L'indexation en Python (et dans la plupart des langages de programmation et de l'informatique en général) commence à `0`.

Ainsi, le premier élément a un index de `0`, le deuxième élément a un index de `1`, et ainsi de suite.

Vous écrivez le nom du tuple ou de la liste puis le nom de l'index entre crochets.

```python
>>>names = ("Jimmy","Timmy","John","Kate")

>>>names[2]
'John'
```
Ou comme ceci :
```
>>>programming_languages = ["Python","JavaScript","Java","C"]

>>>programming_languages[0]
'Python'

>>>programming_languages[1]
'JavaScript'
```

D'accord, maintenant que nous avons vu comment ils sont similaires, regardons les façons dont les tuples et les listes diffèrent.

## Différences entre les Tuples et les Listes en Python

### Les tuples sont immuables tandis que les listes sont mutables en Python

Les tuples sont **immuables** en Python, ce qui signifie qu'une fois que vous avez créé un tuple, les éléments à l'intérieur ne peuvent pas changer.

Les tuples ne peuvent pas être continuellement modifiés.

Si vous essayez de changer la valeur de l'un des éléments, vous obtiendrez une erreur :

```python
>>>names = ("Jimmy","Timmy","John","Kate")

>>>names[2] = "Kelly"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

Vous ne pouvez pas ajouter, remplacer, réassigner ou supprimer aucun des éléments puisque les tuples ne peuvent pas être changés.

Cela signifie également que les tuples ont une longueur fixe. Leur longueur ne change jamais tout au long du cycle de vie du programme.

#### Quand utiliser les tuples

Les tuples sont idéaux à utiliser si vous voulez que les données de votre collection soient en lecture seule, ne changent jamais et restent toujours les mêmes et constantes.

Grâce à cette capacité et à la garantie que les données ne sont jamais modifiées, les tuples peuvent être utilisés dans les dictionnaires et les ensembles, qui nécessitent que les éléments contenus à l'intérieur soient d'un type immuable.

#### Quand utiliser les listes

D'autre part, vous pouvez facilement changer et modifier les listes car les listes sont **mutables**.

Cela signifie que les listes sont modifiables – vous pouvez ajouter des éléments à une liste, supprimer des éléments d'une liste, déplacer des éléments et les échanger facilement dans une liste.

Les listes sont utiles lorsque vous voulez que vos données soient flexibles, ou ne restent pas toujours les mêmes, et soient modifiées lorsque nécessaire.

Les listes supportent une variété de méthodes Python intégrées qui effectuent certaines opérations sur la liste que vous ne pouvez pas utiliser sur les tuples.

Cela signifie que la longueur et la taille des listes augmentent et diminuent tout au long du cycle de vie du programme.

Maintenant, regardons quelques façons simples de changer les listes.

## Comment mettre à jour les listes en Python

Puisque les listes sont mutables, vous devrez connaître quelques façons de base pour mettre à jour les données qu'elles contiennent.

### Comment mettre à jour un élément dans une liste en Python

Pour mettre à jour un élément unique et particulier dans une liste, vous référencez son numéro d'index entre crochets puis vous lui attribuez une nouvelle valeur.

```python
#syntaxe générale
>>>list_name[index] = new_value

>>>programming_languages = ["Python","JavaScript","Java","C"]
>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']

>>>programming_languages[2] = "C++"
>>>print(programming_languages)
['Python', 'JavaScript', 'C++', 'C']
```

### Comment ajouter des éléments à une liste en Python

Il existe quelques méthodes intégrées en Python pour ajouter des éléments aux listes.

La méthode `.append()` ajoute un nouvel élément à la *fin* de la liste.

```python
#syntaxe générale
>>>list_name.append(item)

>>>programming_languages = ["Python","JavaScript","Java","C"]
>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']

>>>programming_languages.append("C++")

>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C', 'C++']
```

Pour ajouter un élément à une position spécifique, vous utilisez la méthode `.insert()`.

Cela insère un élément dans la liste à la position donnée. Le reste des éléments de la liste qui viennent après l'élément que vous souhaitez ajouter sont tous poussés d'une position vers la droite.

```python
#syntaxe générale
>>>list_name.insert(index,item)

>>>names = ["Cody","Dillan","James","Nick"]
>>>print(names)
['Cody', 'Dillan', 'James', 'Nick']


>>>names.insert(0,"Stephanie")

>>>print(names)
['Stephanie', 'Cody', 'Dillan', 'James', 'Nick']
```

Si vous voulez ajouter plus d'un élément à votre liste, vous utilisez la méthode `.extend()`.

Cela ajoute un itérable à la *fin* de la liste. Par exemple, vous pourriez ajouter une nouvelle liste à la fin d'une liste existante.

```python
#syntaxe générale
>>>list_name.extend(iterable)

>>>programming_languages = ["Python","JavaScript"]
>>>more_programming_languages = ["Java","C"]

#ajouter more_programming_languages à programming_languages
>>>programming_languages.extend(more_programming_languages) 

>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']
```

### Comment supprimer des éléments d'une liste en Python

Il existe deux méthodes intégrées pour supprimer des éléments d'une liste en Python.

L'une est la méthode `.remove()`. Cela supprime la première instance de l'élément que vous spécifiez.

```python
#syntaxe générale
>>>list_name.remove(item)

>>>programming_languages = ["Python", "JavaScript", "Java", "C"]
>>>print(programming_languages)
['Python', 'JavaScript', 'Java', 'C']

>>>programming_languages.remove("Java")
>>>print(programming_languages)
['Python', 'JavaScript', 'C']

#supprime uniquement la première occurrence
>>>programming_languages = ["Python", "JavaScript", "Java", "C","Python"]
>>>programming_languages.remove("Python")
>>>print(programming_languages)
['JavaScript', 'Java', 'C', 'Python']
```

L'autre façon est d'utiliser la méthode `.pop()`.

Sans passer d'argument, elle supprimera le dernier élément d'une liste.

Vous pouvez passer en argument l'index de l'élément spécifique que vous souhaitez supprimer.

Dans les deux cas, la valeur supprimée est retournée, ce qui est utile. Si vous le souhaitez, vous pourriez la stocker dans une variable pour une utilisation ultérieure.

```python
>>>programming_languages = ["Python", "JavaScript", "Java", "C"]

>>>programming_languages.pop()
'C'


>>>print(programming_languages)
['Python', 'JavaScript', 'Java']

#stocker la valeur retournée dans une variable
>>>programming_languages = ["Python", "JavaScript", "Java", "C"]

>>>fave_language = programming_languages.pop(0)
>>>print(fave_language)
Python
```

## Conclusion

Cela marque la fin de notre introduction à la façon dont les tuples et les listes fonctionnent et comment ils sont couramment utilisés.

Pour résumer, les **similitudes** entre les tuples et les listes sont :

- Ils sont tous deux considérés comme des objets en Python.
- Ce sont des conteneurs, utilisés pour stocker des données. Ces données peuvent être de n'importe quel type.
- Ils sont tous deux ordonnés et maintiennent cet ordre tout le temps. Une fois l'ordre des éléments défini, il ne changera pas.
- Dans les tuples et les listes, vous pouvez accéder à des éléments individuels par index.

Les **différences** entre les tuples et les listes sont :

- Les tuples sont **immuables**. Utilisez-les lorsque vous êtes sûr que vos données ne changeront pas dans le cycle de vie de votre programme ou lorsque vous voulez une garantie que vos données resteront toujours les mêmes.
- Les listes sont **mutables**. Vous pouvez ajouter et supprimer des éléments. Les listes grandissent et rétrécissent tout au long de la vie d'un programme. Utilisez-les lorsque vos données sont destinées à être modifiées.

Si vous voulez apprendre Python en profondeur, freeCodeCamp offre une certification Python gratuite [Python certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

Vous commencez par les bases absolues et avancez vers des sujets plus complexes tels que les structures de données et les bases de données relationnelles. À la fin, il y a cinq projets pratiques pour solidifier vos connaissances.

Merci d'avoir lu et bon apprentissage !