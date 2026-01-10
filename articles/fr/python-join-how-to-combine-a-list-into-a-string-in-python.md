---
title: Python join() – Comment combiner une liste en une chaîne de caractères en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-01-03T20:11:53.000Z'
originalURL: https://freecodecamp.org/news/python-join-how-to-combine-a-list-into-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/pexels-francesco-ungaro-96081.jpg
tags:
- name: Python
  slug: python
seo_title: Python join() – Comment combiner une liste en une chaîne de caractères
  en Python
seo_desc: "By Suchandra Datta\njoin() is one of the built-in string functions in Python\
  \ that lets us create a new string from a list of string elements with a user-defined\
  \ separator. \nToday we'll explore join() and learn about:\n\njoin() syntax\nhow\
  \ to use join() t..."
---

Par Suchandra Datta

`join()` est l'une des fonctions de chaîne intégrées en Python qui nous permet de créer une nouvelle chaîne à partir d'une liste d'éléments de chaîne avec un séparateur défini par l'utilisateur. 

Aujourd'hui, nous allons explorer `join()` et apprendre :

* La syntaxe de `join()`
* comment utiliser `join()` pour combiner une liste en une chaîne
* comment combiner des tuples en une chaîne avec `join()`
* comment utiliser `join()` avec des dictionnaires
* quand ne pas utiliser `join()` 

## Syntaxe de `join()`

```py
str.join(iterable)
```

* elle nécessite un seul argument d'entrée, un itérable. Un itérable est un objet qui supporte l'itération, ce qui signifie qu'il a défini les méthodes `__next__` et `__iter__`. Des exemples d'itérables sont les listes, les tuples, les chaînes, les dictionnaires et les ensembles.
* `join()` est une fonction de chaîne intégrée, donc elle nécessite une chaîne pour l'invoquer
* elle retourne une valeur de sortie, une chaîne formée en combinant les éléments de l'itérable avec la chaîne qui l'invoque, agissant comme un séparateur

## Comment utiliser `join()` pour combiner une liste en une chaîne

Regardons un exemple :

Nous créons une chaîne composée d'une seule occurrence du caractère `|`, comme ceci :

```python
s = "|"
```

Nous pouvons utiliser la méthode `dir` pour voir quelles méthodes nous avons disponibles pour invoquer en utilisant l'objet chaîne `s` :

```python
dir(s)
```

Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-146.png)

Parmi les différents attributs et noms de méthodes, nous pouvons voir la méthode `join()` :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-147.png)

Créons une liste de chaînes :

```python
country_names = ["Brazil", "Argentina", "Spain", "France"]
```

Et maintenant, joignons les éléments de la liste en une seule chaîne avec le `|` comme séparateur :

```python
country_names = ["Brazil", "Argentina", "Spain", "France"]
s.join(country_names)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-148.png)

Ici, nous voyons que `join()` retourne une seule chaîne comme sortie. Le contenu de la variable chaîne invoquant `join()` est le séparateur, séparant les éléments de la liste de l'itérable `country_names` qui forme la sortie. Nous pouvons utiliser n'importe quelle chaîne que nous aimons comme séparateur comme ceci :

```python
s = ","
s.join(country_names)
```

ou ceci :

```python
s = "__WC__"
s.join(country_names)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-149.png)

L'utilisation de `join()` avec des listes de chaînes a de nombreuses applications utiles. Par exemple, nous pouvons l'utiliser pour supprimer les espaces supplémentaires entre les mots. Supposons que nous ayons une phrase comme celle ci-dessous où il y a plusieurs espaces. Nous pouvons utiliser `split()` qui divisera sur les espaces blancs pour créer une liste de mots :

```python
paragraph = "Argentina  wins   football   world cup 2022 in a nail biting final match that led to a \
spectacular    penalty shootout. Football lovers   across the world   hailed   it as one of the most\
 memorable   matches."
step1 = paragraph.split()
print(step1)
```

Maintenant, nous utilisons `join()` en utilisant un seul espace pour recréer la phrase originale sans les espaces supplémentaires entre les mots :

```python
" ".join(step1)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-156.png)

## Comment combiner des tuples en une chaîne avec `join()`

Les tuples sont l'un des types de données intégrés en Python qui n'autorise pas les modifications une fois qu'ils sont créés - ils sont immuables. Les tuples sont des listes d'éléments séparés par des virgules et enfermés dans des parenthèses comme ceci :

```python
t = ('quarter-final', 'semi-final', 'final')
```

Nous pouvons combiner les éléments de tuple ensemble de la même manière que nous combinions les éléments de liste ensemble en utilisant `join()` :

```python
",".join(t)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-151.png)

Cela est utile pour les cas où nous devons utiliser des tuples - comme stocker de grandes collections d'éléments qui doivent être traités une seule fois, puis afficher les éléments dans une chaîne séparée par des virgules.

## Comment utiliser `join()` avec des dictionnaires

Les dictionnaires sont un type de mappage en Python où nous spécifions des paires clé-valeur pour le stockage. Supposons que nous ayons ce dictionnaire imbriqué :

```python
d = { "event":
     {
        "world cup":{
            "sport":"Football",
            "info":{"year":"2022", "country":"Argentina"}
        }
     }
    }
```

Nous pouvons utiliser `join()` pour extraire une chaîne séparée par des virgules avec les clés et les valeurs comme ceci :

```python
column_values = ",".join(d["event"]["world cup"]["info"].keys())
row_values = ",".join(d["event"]["world cup"]["info"].values())
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-152.png)

## Quand ne pas utiliser `join()`

`join()` ne fonctionnera pas si vous essayez de :

* combiner des itérables avec des éléments qui ne sont pas des chaînes
* combiner des itérables imbriqués 

Regardons quelques exemples.

### Itérables avec des éléments qui ne sont pas des chaînes

`join()` ne peut pas être appliqué sur des séquences qui contiennent des éléments autres que des chaînes. Nous ne pourrons donc pas combiner des listes avec des éléments de type numérique. Cela lèverait une erreur de type TypeError comme ceci :

```python
names_and_numbers = ["Tom", 1234, "Harry"]
",".join(names_and_numbers)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-153.png)

### Itérables imbriqués

Si nous essayons de combiner les valeurs d'un dictionnaire comme ceci :

```python
nested = ["Tom", "Harry", ["Jack", "Jill"]]
",".join(nested)
```

Nous obtiendrons une erreur de type TypeError, car `join()` attend une liste de chaînes mais a reçu une liste de listes de chaînes.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-154.png)

Pour de tels cas, aplatissez la liste comme ceci :

```python
flatten = 
[ x for x in nested if isinstance(x, list)!=True] + \
[ e for each in nested for e in each if isinstance(each, list)==True]
```

Ici, ceci :

```python
[ x for x in nested if isinstance(x, list)!=True] 
```

vérifie si chaque élément dans `nested` est une liste. Si ce n'est pas le cas, il l'ajoute à une nouvelle liste. Et ceci :

```python
[ e for each in nested for e in each if isinstance(each, list)==True]
```

crée un nouvel élément de liste 1D pour tout élément dans `nested` qui est une liste. Maintenant, nous exécutons `join()` comme ceci :

```python
nested = ["Tom", "Harry", ["Jack", "Jill"]]
flatten = [ x for x in nested if isinstance(x, list)!=True] + \
[ e for each in nested for e in each if isinstance(each, list)==True]
",".join(flatten)
```

![Image](https://www.freecodecamp.org/news/content/images/2022/12/image-155.png)

## Conclusion

Dans cet article, nous avons appris comment utiliser la méthode `join()` sur des itérables comme les listes, les dictionnaires et les tuples. Nous avons également appris quels types de cas d'utilisation nous pouvons appliquer et les situations à surveiller où `join()` ne fonctionnerait pas. 

J'espère que vous avez apprécié cet article et je vous souhaite une semaine très heureuse et revigorante.