---
title: Exemples de NamedTuple en Python – Comment créer et travailler avec des NamedTuples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-12T15:34:19.000Z'
originalURL: https://freecodecamp.org/news/python-namedtuple-examples-how-to-create-and-work-with-namedtuples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/named-tuple-2.png
tags:
- name: Python
  slug: python
seo_title: Exemples de NamedTuple en Python – Comment créer et travailler avec des
  NamedTuples
seo_desc: "In Python, you'll probably use a tuple to initialize a sequence that shouldn't\
  \ be modified elsewhere in the program. This is because tuples are immutable. \n\
  However, using a tuple may reduce the readability of your code as you cannot describe\
  \ what eac..."
---

En Python, vous utiliserez probablement un tuple pour initialiser une séquence qui ne doit pas être modifiée ailleurs dans le programme. Cela est dû au fait que les tuples sont _immuables_.

Cependant, l'utilisation d'un tuple peut réduire la lisibilité de votre code, car vous ne pouvez pas décrire ce que représente chaque élément du tuple. C'est là que les NamedTuples peuvent être utiles.

Un NamedTuple offre l'immuabilité d'un tuple, tout en rendant votre code facile à comprendre et à utiliser.

Dans ce tutoriel, vous apprendrez à créer et à utiliser des NamedTuples efficacement.

## Tuples Python – Un bref rappel

Avant de plonger dans les NamedTuples, faisons un rapide rappel sur les tuples Python.

Les tuples sont des structures de données intégrées puissantes en Python. Ils sont similaires aux listes Python en ce sens qu'ils peuvent contenir des éléments de différents types, et vous pouvez les parcourir.

> Cependant, les tuples diffèrent des listes en ce sens qu'ils sont _immuables_. Cela signifie que vous _ne pouvez pas_ modifier un tuple existant, et essayer de le faire générera une erreur.

➡️ Supposons que vous créiez le tuple suivant aujourd'hui. Le tuple `house` contient cinq éléments qui décrivent la maison, à savoir la ville, le pays, l'année de construction, la superficie en pieds carrés et le nombre de pièces. Cela est montré dans l'extrait de code ci-dessous :

```python
house = ("Bangalore","India",2020,2018,4)
```

* Cette `house` est située dans la ville de Bangalore en Inde.
* Elle a été construite en l'an `2020`.
* Et elle a `4` pièces qui couvrent collectivement une superficie de `2018` pieds carrés.

Supposons que votre ami lise cette ligne de code, ou que vous reveniez une semaine plus tard et relisiez votre code. Étant donné que vous n'avez ajouté aucun commentaire sur ce que représentent les valeurs dans le tuple, il y a certainement un problème de lisibilité.

Par exemple, vous pourriez devoir deviner s'il s'agit d'une maison de 2018 pieds carrés construite en 2020, ou d'une maison de 2020 pieds carrés construite en 2018. 🤔

Vous pourriez suggérer d'utiliser un dictionnaire à la place – vous pouvez spécifier _ce que_ représentent les différentes valeurs en tant que _clés_ du dictionnaire, et les _valeurs_ réelles en tant que _valeurs_ du dictionnaire.

Passez à la section suivante pour un bref rappel sur les dictionnaires Python.

## Dictionnaires Python – Un bref rappel

Avec la motivation d'améliorer la lisibilité du code, envisageons de passer aux dictionnaires Python.

Les dictionnaires sont des structures de données intégrées qui stockent des valeurs en _paires clé-valeur_. Vous pouvez accéder à un dictionnaire et à ses valeurs en utilisant les clés.

Ainsi, vous pouvez réécrire le tuple de la section précédente en tant que dictionnaire comme suit :

```python
house = {"city":"Bangalore","country":"India","year":2020,"area":2018,"num_rooms":4}
```

Dans l'extrait de code ci-dessus :

* `"city"`, `"country"`, `"year"`, `"area"` et `"num_rooms"` sont les clés.
* Et les valeurs du tuple, `"Bangalore"`, `"India"`, `2020`, `2018`, et `4` sont utilisées comme valeurs correspondant aux clés.
* Vous pouvez accéder aux valeurs en utilisant les clés : `house["city"]` pour obtenir `"Bangalore"`, `house["area"]` pour obtenir `2018`, et ainsi de suite.

Comme vous pouvez le voir, l'utilisation d'un dictionnaire améliore la lisibilité du code. Mais, contrairement aux tuples, vous pouvez toujours modifier les valeurs dans un dictionnaire.

> Tout ce que vous avez à faire est de définir la clé correspondante à une valeur différente.

Dans l'exemple ci-dessus, vous pouvez utiliser `house["city"] = "Delhi"` pour changer la ville où se trouve votre maison. Clairement, cela n'est pas autorisé, car vous ne voulez pas que les valeurs soient modifiées ailleurs dans le programme.

Et si vous devez stocker des descriptions pour de nombreuses maisons, vous devrez créer autant de dictionnaires que de maisons, en répétant les noms des clés à chaque fois. Cela rend également votre code répétitif et pas très intéressant !

> Avec les NamedTuples de Python, vous pouvez avoir à la fois l'immuabilité des tuples et la lisibilité des dictionnaires.

Passez à la section suivante pour en savoir plus sur les `NamedTuple`s.

## Syntaxe des NamedTuples en Python

Pour utiliser un `NamedTuple`, vous devez l'importer depuis le module collections intégré de Python, comme montré :

```python
from collections import namedtuple
```

La syntaxe générale pour créer un NamedTuple est la suivante :

```python
namedtuple(<Name>,<[Names of Values]>)
```

* `<Name>` est un espace réservé pour ce que vous souhaitez appeler votre NamedTuple, et
* `<[Names of Values]>` est un espace réservé pour la liste contenant les _noms_ des différentes valeurs, ou attributs.

Maintenant que vous êtes familiarisé avec la syntaxe pour créer des NamedTuples, développons notre exemple de `house`, et essayons de le créer en tant que NamedTuple.

## Exemple de NamedTuple en Python

Comme mentionné précédemment, la première étape consiste à importer `namedtuple`.

```python
from collections import namedtuple


```

Maintenant, vous pouvez créer un NamedTuple en utilisant la syntaxe discutée dans la section précédente :

```python
House = namedtuple("House",["city","country","year","area","num_rooms"])
```

Dans cet exemple,

* Vous choisissez d'appeler le NamedTuple `House`, et
* Mentionnez les noms des valeurs, `"city"`, `"country"`, `"year"`, `"area"` et `"num_rooms"` dans une liste.

✅ Et vous avez créé votre premier NamedTuple – `House`.

Maintenant, vous pouvez créer une maison `house_1` avec les spécifications requises en utilisant `House` comme suit :

```python
house_1 = House("Bangalore","India",2020,2018,4)
```

Vous devez simplement passer les valeurs réelles que les noms, ou attributs dans votre `<[Names of Values]>` doivent prendre.

Pour créer une autre maison, par exemple `house_2`, tout ce que vous avez à faire est de créer une nouvelle `House` en utilisant ses valeurs.

```python
house_2 = House("Chennai","India",2018,2050,3)
```

> Remarquez comment vous pouvez utiliser `House` comme un modèle pour créer autant de maisons que vous le souhaitez, sans avoir à taper les noms des attributs chaque fois que vous créez une nouvelle maison.

## Comment utiliser la notation `dot` pour accéder aux valeurs d'un NamedTuple

Une fois que vous avez créé les objets NamedTuple `house_1` et `house_2`, vous pouvez utiliser la notation `dot` pour accéder à leurs valeurs. La syntaxe est montrée ci-dessous :

```
<namedtuple_object>.<value_name>
```

* Ici, `<namedtuple_object>` désigne l'objet NamedTuple créé. Dans cet exemple, `house_1` et `house_2`.
* `<value_name>` désigne l'un des noms valides utilisés lors de la création du NamedTuple. Dans cet exemple, `"city"`, `"country"`, `"year"`, `"area"` et `"num_rooms"` sont les choix valides pour `<value_name>`.

Cela est illustré dans l'extrait de code suivant :

```python
print(house_1.city)
print(house_1.country)
print(house_1.year)
print(house_1.area)
print(house_1.num_rooms)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-33.png)

De même, vous pouvez utiliser `house_2.city`, `house_2.country`, et ainsi de suite pour accéder aux valeurs correspondant au NamedTuple `house_2`.

## 📋 Essayez par vous-même ! Exemple de NamedTuple

Dans cette section, vous allez créer un NamedTuple `ProblemSet`.

N'hésitez pas à essayer cet exemple dans l'IDE de votre choix.

Le NamedTuple `ProblemSet` doit prendre les valeurs suivantes :

* `num_questions` : un entier représentant le nombre de questions dans un ensemble de problèmes particulier,
* `difficulty` : une chaîne qui indique le niveau de difficulté de l'ensemble de problèmes, et
* `topic` : le sujet que couvre l'ensemble de problèmes, par exemple, `"Arrays"`, `"Strings"`, `"Graphs"`, etc.

La procédure est très similaire à notre exemple précédent où nous avons créé le NamedTuple `House`.

1️⃣ Importez `namedtuple` depuis le module `collections`.

```python
from collections import namedtuple
```

2️⃣ Créez un NamedTuple et appelez-le `ProblemSet`.

```python
ProblemSet = namedtuple("ProblemSet",["num_questions","difficulty","topic"])
```

3️⃣ Maintenant que vous avez créé `ProblemSet`, vous pouvez créer autant d'ensembles de problèmes que vous le souhaitez en utilisant `ProblemSet` comme modèle.

* Ici, `problem_set1` contient 5 questions faciles sur `Strings`.

```python
problem_set1 = ProblemSet(5,"Easy","Strings")
```

* Et `problem_set2` contient 3 questions difficiles sur `Bit Manipulation`.

```python
problem_set2 = ProblemSet(3,"Hard","Bit Manipulation")
```

4️⃣ Comme dans l'exemple précédent, vous pouvez utiliser la notation `dot` pour accéder aux valeurs des deux ensembles de problèmes créés ci-dessus.

```python
print(problem_set1.topic)

# Output
Strings
```

```python
print(problem_set2.difficulty)

# Output
Hard
```

J'espère que vous avez pu compléter cet exercice. 🎉

## Conclusion

Dans ce tutoriel, vous avez appris :

* comment les NamedTuples vous aident à combiner les avantages des tuples et des dictionnaires,
* comment créer des NamedTuples, et
* comment utiliser la notation `dot` pour accéder aux valeurs des NamedTuples.

Si vous êtes familiarisé avec la POO en Python, vous pourriez trouver cela similaire au fonctionnement des classes Python. Une classe avec ses attributs sert de modèle à partir duquel vous pouvez créer autant d'objets, ou instances – chacun avec ses propres valeurs pour les attributs.

Cependant, créer une classe et définir les attributs requis juste pour améliorer la lisibilité de votre code peut souvent être excessif, et il est beaucoup plus facile de créer des NamedTuples à la place.

À bientôt dans le prochain tutoriel. En attendant, bon codage !