---
title: Tutoriel sur les méthodes de chaînes Python – Comment utiliser find() et replace()
  sur les chaînes Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-09-01T15:39:30.000Z'
originalURL: https://freecodecamp.org/news/python-string-methods-tutorial-how-to-use-find-and-replace-on-python-strings
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/find
seo_title: Tutoriel sur les méthodes de chaînes Python – Comment utiliser find() et
  replace() sur les chaînes Python
---

and-replace----1--1.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "Lorsqu'on travaille avec des chaînes en Python, il peut être nécessaire de rechercher un motif dans les chaînes, ou même de remplacer des parties de chaînes par une autre sous-chaîne. Python dispose des méthodes de chaîne utiles find() et replace() qui nous aident à effectuer ces tâches de traitement de chaînes..."
---

Lorsqu'on travaille avec des chaînes en Python, il peut être nécessaire de rechercher un motif dans les chaînes, ou même de remplacer des parties de chaînes par une autre sous-chaîne. 

Python dispose des méthodes de chaîne utiles `find()` et `replace()` qui nous aident à effectuer ces tâches de traitement de chaînes. 

Dans ce tutoriel, nous allons apprendre à utiliser ces deux méthodes de chaîne avec des exemples de code.

## Immuabilité des chaînes Python

Les chaînes en Python sont _immuables_. Par conséquent, nous ne pouvons pas modifier les chaînes _en place_. 

> Les chaînes sont des itérables Python qui suivent un indexage à partir de zéro. Les indices valides pour une chaîne de longueur `n` sont `0,1,2,..,(n-1)`.  
>   
> Nous pouvons également utiliser l'_indexation négative_, où le dernier élément est à l'index `-1`, l'avant-dernier élément est à l'index `-2` et ainsi de suite.

Par exemple, nous avons `my_string` qui contient la chaîne `"writer"`. Essayons de la changer en `"writes"` en définissant le dernier caractère sur `"s"`.

```python
my_string = "writer"

```

Essayons d'assigner le dernier caractère à la lettre `"s"` comme montré ci-dessous. Par indexation négative, nous savons que l'index du dernier caractère dans `my_string` est `-1`.

```python
my_string[-1]="s"

# Output
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-670491032ba6> in <module>()
      1 my_string = "writer"
----> 2 my_string[-1]="s"

TypeError: 'str' object does not support item assignment
```

Comme montré dans l'extrait de code ci-dessus, nous obtenons une `TypeError`. Cela est dû au fait que l'objet chaîne est _immuable_, et l'assignation que nous avons essayé d'effectuer est invalide. 

Cependant, nous devons souvent modifier les chaînes. Et les méthodes de chaîne nous aident à le faire facilement. 

> Les méthodes de chaîne opèrent sur des chaînes _existantes_ et _retournent de nouvelles_ chaînes modifiées. La chaîne existante n'est _pas_ modifiée.

Passons à la section suivante pour apprendre les méthodes `find()` et `replace()`.

## Comment utiliser find() pour rechercher des motifs dans les chaînes Python

Vous pouvez utiliser la méthode `find()` de Python pour rechercher un motif dans une chaîne. La syntaxe générale est montrée ci-dessous.

```
<this_string>.find(<this_pattern>)
```

La chaîne d'entrée que nous aimerions rechercher est désignée par le placeholder `this_string`. Le motif que nous aimerions rechercher est donné par le placeholder `this_pattern`.

Analysons maintenant la syntaxe ci-dessus.

* La méthode `find()` recherche dans `this_string` l'occurrence de `this_pattern`.
* Si `this_pattern` est présent, elle retourne l'index de départ de la _première_ occurrence de `this_pattern`.
* Si `this_pattern` n'apparaît pas dans `this_string`, elle retourne `-1`.

▶ Regardons quelques exemples.

### Exemples de la méthode find() de Python

Prenons une chaîne d'exemple `"I enjoy coding in Python!"`.

```python
my_string = "I enjoy coding in Python!"
my_string.find("Python")

# Output
18
```

Dans l'exemple ci-dessus, nous avons essayé de rechercher `"Python"` dans `"my_string"`. La méthode `find()` a retourné `18`, l'index de départ du motif `"Python"`. 

Pour vérifier si l'index retourné est correct, nous pouvons vérifier si `my_string[18]=="P"` évalue à `True`.

▶ Maintenant, nous allons essayer de rechercher une sous-chaîne qui n'est pas présente dans notre chaîne.

```python
my_string.find("JavaScript")

# Output
-1
```

Dans cet exemple, nous avons essayé de rechercher `"JavaScript"` qui n'est pas présent dans notre chaîne. La méthode `find()` a retourné `-1`, comme discuté précédemment.

## Comment utiliser find() pour rechercher des motifs dans les sous-chaînes Python

Nous pouvons également utiliser la méthode `find()` pour rechercher un motif dans une certaine _sous-chaîne_ ou _tranche_ d'une chaîne, au lieu de la chaîne entière. 

Dans ce cas, l'appel de la méthode `find()` prend la forme suivante:

```
<this_string>.find(<this_pattern>, <start_index>,<end_index>)
```

Cela fonctionne de manière très similaire à la syntaxe discutée précédemment. 

> La seule différence est que la recherche du motif ne porte pas sur toute la chaîne. Elle ne porte que sur une _tranche_ de la chaîne spécifiée par `start_index:end_index`.

## Comment utiliser index() pour rechercher des motifs dans les chaînes Python

Pour rechercher une occurrence d'un motif dans une chaîne, nous pouvons également utiliser la méthode `index()`. L'appel de la méthode prend la syntaxe montrée ci-dessous.

```
<this_string>.index(<this_pattern>)
```

Le fonctionnement de la méthode `index()` est très similaire à celui de la méthode `find()`. 

* Si `this_pattern` est présent dans `this_string`, la méthode `index()` retourne l'index de départ de la _première_ occurrence de `this_pattern`.
* Cependant, elle lève une `ValueError` si `this_pattern` n'est pas trouvé dans `this_string`.

▶ Il est temps de voir des exemples.

### Exemples de la méthode index() de Python

Utilisons la chaîne `my_string = "I enjoy coding in Python!"` de notre exemple précédent.

```python
my_string.index("Python")

# Output
18

```

Dans ce cas, la sortie est identique à celle de la méthode `find()`.

Si nous recherchons une sous-chaîne qui n'est pas présente dans notre chaîne, la méthode `index()` lève une `ValueError`. Cela est montré dans l'extrait de code ci-dessous. 

```
my_string.index("JavaScript")

# Output
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-4-377f7c374e16> in <module>()
----> 1 my_string.index("JavaScript")

ValueError: substring not found
```

Dans la section suivante, nous allons apprendre à trouver et remplacer des motifs dans les chaînes.

## Comment utiliser replace() pour trouver et remplacer des motifs dans les chaînes Python

Si vous devez rechercher un motif dans une chaîne et le remplacer par un autre motif, vous pouvez utiliser la méthode `replace()`. La syntaxe générale est montrée ci-dessous:

```
<this_string>.replace(<this>,<with_this>)
```

Nous allons maintenant analyser cette syntaxe.

* La méthode `replace()` recherche dans `this_string` le motif `this`.
* Si le motif `this` est présent, elle retourne une nouvelle chaîne où _toutes_ les occurrences du motif `this` sont remplacées par le motif spécifié par l'argument `with_this`.
* Si le motif `this` n'est pas trouvé dans `this_string`, la chaîne retournée est la même que `this_string`.

> Que faire si vous souhaitez remplacer seulement un certain nombre d'occurrences au lieu de toutes les occurrences du motif?

Dans ce cas, vous pouvez ajouter un argument _optionnel_ dans l'appel de la méthode qui spécifie combien d'occurrences du motif vous souhaitez remplacer.

```
<this_string>.replace(<this>,<with_this>, n_occurrences)
```

Dans la syntaxe montrée ci-dessus, `n_occurrences` garantit que seules les `n` premières occurrences du motif sont remplacées dans la chaîne retournée.

▶ Regardons quelques exemples pour comprendre comment la fonction `replace()` fonctionne.

### Exemples de la méthode replace() de Python

Redéfinissons maintenant `my_string` pour qu'elle soit la suivante:

```
I enjoy coding in C++.
C++ is easy to learn.
I've been coding in C++ for 2 years now.:)
```

Cela est montré dans l'extrait de code ci-dessous:

```python
my_string = "I enjoy coding in C++.\nC++ is easy to learn.\nI've been coding in C++ for 2 years now.:)"


```

Remplaçons maintenant toutes les occurrences de `"C++"` par `"Python"`, comme ceci:

```python
my_string.replace("C++","Python")

# Output
'I enjoy coding in Python.\nPython is easy to learn.\nI've been coding in Python for 2 years now.:)'
```

Comme la méthode `replace()` retourne une chaîne, nous voyons les caractères `\n` dans la sortie. Pour que le caractère `\n` introduise des sauts de ligne, nous pouvons imprimer la chaîne comme montré ci-dessous:

```python
print(my_string.replace("C++","Python"))


# Output
I enjoy coding in Python.
Python is easy to learn.
I've been coding in Python for 2 years now.:)
```

Dans l'exemple ci-dessus, nous voyons que toutes les occurrences de `"C++"` ont été remplacées par `"Python"`.

▶ Maintenant, nous allons utiliser l'argument supplémentaire `n_occurrences` également. 

Le code suivant retourne une chaîne où les deux premières occurrences de `"C++"` sont remplacées par `"Python"`.

```python
print(my_string.replace("C++","Python",2))

# Output
I enjoy coding in Python.
Python is easy to learn.
I've been coding in C++ for 2 years now.:)
```

Le code suivant retourne une chaîne où seule la première occurrence de `"C++"` est remplacée par `"Python"`:

```python
print(my_string.replace("C++","Python",1))

# Output
I enjoy coding in Python.
C++ is easy to learn.
I've been coding in C++ for 2 years now.:)
```

▶ Maintenant, nous essayons de remplacer une sous-chaîne `"JavaScript"` qui n'existe pas dans `my_string`. Par conséquent, la chaîne retournée est la même que `my_string`.

```python
print(my_string.replace("JavaScript","Python"))

# Output
I enjoy coding in C++.
C++ is easy to learn.
I've been coding in C++ for 2 years now.:)
```

## Conclusion

Dans ce tutoriel, nous avons appris ce qui suit:

* Comment rechercher dans des chaînes en Python en utilisant les méthodes `find()` et `index()`, et
* Comment trouver et remplacer des motifs ou des sous-chaînes en utilisant la méthode `replace()`

J'espère que vous avez apprécié ce tutoriel.

À bientôt dans un autre article. En attendant, bon apprentissage!