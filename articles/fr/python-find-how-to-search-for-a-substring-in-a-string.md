---
title: Python find() – Comment rechercher une sous-chaîne dans une chaîne
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-07-25T13:56:30.000Z'
originalURL: https://freecodecamp.org/news/python-find-how-to-search-for-a-substring-in-a-string
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/tarn-nguyen-XlEafYGDvV0-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Python find() – Comment rechercher une sous-chaîne dans une chaîne
seo_desc: 'When you''re working with a Python program, you might need to search for
  and locate a specific string inside another string.

  This is where Python''s built-in string methods come in handy.

  In this article, you will learn how to use Python''s built-in fin...'
---

Lorsque vous travaillez avec un programme Python, vous pourriez avoir besoin de rechercher et de localiser une chaîne spécifique à l'intérieur d'une autre chaîne.

C'est là que les méthodes de chaîne intégrées de Python deviennent utiles.

Dans cet article, vous apprendrez à utiliser la méthode de chaîne intégrée `find()` de Python pour vous aider à rechercher une sous-chaîne à l'intérieur d'une chaîne.

Voici ce que nous allons couvrir :

1. [Syntaxe de la méthode `find()`](#syntaxe)
    1. [Comment utiliser `find()` sans paramètres de début et de fin exemple](#sans-parametres)
    2. [Comment utiliser `find()` avec des paramètres de début et de fin exemple](#avec-parametres)
    3. [Exemple de sous-chaîne non trouvée](#non-trouvee)
    4. [La méthode `find()` est-elle sensible à la casse ?](#sensible-casse)
2. [`find()` vs mot-clé `in`](#find-vs-in)
3. [`find()` vs `index()`](#find-vs-index)

## La méthode `find()` - Aperçu de la syntaxe <a name="syntaxe"></a>

La méthode de chaîne `find()` est intégrée à la bibliothèque standard de Python.

Elle prend une sous-chaîne en entrée et trouve son index - c'est-à-dire la position de la sous-chaîne à l'intérieur de la chaîne sur laquelle vous appelez la méthode.

La syntaxe générale de la méthode `find()` ressemble à ceci :

```
string_object.find("substring", start_index_number, end_index_number)
```

Décomposons cela :

- `string_object` est la chaîne originale avec laquelle vous travaillez et la chaîne sur laquelle vous allez appeler la méthode `find()`. Cela pourrait être n'importe quel mot que vous souhaitez rechercher.
- La méthode `find()` prend trois paramètres – un requis et deux optionnels.
- `"substring"` est le premier paramètre *requis*. Il s'agit de la sous-chaîne que vous essayez de trouver à l'intérieur de `string_object`. Assurez-vous d'inclure les guillemets.
- `start_index_number` est le deuxième paramètre et il est *optionnel*. Il spécifie l'index de départ et la position à partir de laquelle la recherche commencera. La valeur par défaut est `0`.
- `end_index_number` est le troisième paramètre et il est également *optionnel*. Il spécifie l'index de fin et l'endroit où la recherche s'arrêtera. La valeur par défaut est la longueur de la chaîne.
- Les paramètres `start_index_number` et `end_index_number` spécifient tous deux la plage sur laquelle la recherche aura lieu et ils restreignent la recherche à une section particulière.

La valeur de retour de la méthode `find()` est une valeur entière.

Si la sous-chaîne est présente dans la chaîne, `find()` retourne l'index, ou la position du caractère, de la **première** occurrence de la sous-chaîne spécifiée à partir de cette chaîne donnée.

Si la sous-chaîne que vous recherchez n'est **pas** présente dans la chaîne, alors `find()` retournera `-1`. Elle ne lèvera pas d'exception.

### Comment utiliser `find()` sans paramètres de début et de fin exemple <a name="sans-parametres"></a>

Les exemples suivants illustrent comment utiliser la méthode `find()` en utilisant uniquement le paramètre requis – la sous-chaîne que vous souhaitez rechercher.

Vous pouvez prendre un seul mot et rechercher l'index d'une lettre spécifique :

```python
fave_phrase = "Hello world!"

# trouver l'index de la lettre 'w'
search_fave_phrase = fave_phrase.find("w")

print(search_fave_phrase)

#output

# 6
```

J'ai créé une variable nommée `fave_phrase` et j'y ai stocké la chaîne `Hello world!`.

J'ai appelé la méthode `find()` sur la variable contenant la chaîne et j'ai recherché la lettre 'w' à l'intérieur de `Hello world!`.

J'ai stocké le résultat de l'opération dans une variable nommée `search_fave_phrase` puis j'ai affiché son contenu dans la console.

La valeur de retour était l'index de `w` qui, dans ce cas, était l'entier `6`.

Gardez à l'esprit que l'indexation en programmation et en informatique en général commence toujours à `0` et **non** à `1`.

### Comment utiliser `find()` avec des paramètres de début et de fin exemple <a name="avec-parametres"></a>

L'utilisation des paramètres de début et de fin avec la méthode `find()` vous permet de limiter votre recherche.

Par exemple, si vous souhaitez trouver l'index de la lettre 'w' et commencer la recherche à partir de la position `3` et non avant, vous feriez ce qui suit :

```python
fave_phrase = "Hello world!"

# trouver l'index de la lettre 'w' en commençant par la position 3
search_fave_phrase = fave_phrase.find("w",3)

print(search_fave_phrase)

#output

# 6
```

Puisque la recherche commence à la position 3, la valeur de retour sera la première instance de la chaîne contenant 'w' à partir de cette position et au-delà.

Vous pouvez également affiner davantage la recherche et être plus spécifique avec votre recherche avec le paramètre de fin :

```python
fave_phrase = "Hello world!"

# trouver l'index de la lettre 'w' entre les positions 3 et 8
search_fave_phrase = fave_phrase.find("w",3,8)

print(search_fave_phrase)

#output

# 6
```

### Exemple de sous-chaîne non trouvée <a name="non-trouvee"></a>

Comme mentionné précédemment, si la sous-chaîne que vous spécifiez avec `find()` n'est pas présente dans la chaîne, alors la sortie sera `-1` et non une exception.

```python
fave_phrase = "Hello world!"

# rechercher l'index de la lettre 'a' dans "Hello world"
search_fave_phrase = fave_phrase.find("a")

print(search_fave_phrase)

# -1
```

### La méthode `find()` est-elle sensible à la casse ? <a name="sensible-casse"></a>

Que se passe-t-il si vous recherchez une lettre dans une casse différente ?

```python
fave_phrase = "Hello world!"

# rechercher l'index de la lettre 'W' en majuscule
search_fave_phrase = fave_phrase.find("W")

print(search_fave_phrase)

#output

# -1
```

Dans un exemple précédent, j'ai recherché l'index de la lettre `w` dans la phrase "Hello world!" et la méthode `find()` a retourné sa position.

Dans ce cas, la recherche de la lettre `W` en majuscule retourne `-1` – ce qui signifie que la lettre n'est pas présente dans la chaîne.

Donc, lorsque vous recherchez une sous-chaîne avec la méthode `find()`, rappelez-vous que la recherche sera sensible à la casse.

## La méthode `find()` vs le mot-clé `in` – Quelle est la différence ? <a name="find-vs-in"></a>

Utilisez le mot-clé `in` pour vérifier si la sous-chaîne est présente dans la chaîne en premier lieu.

La syntaxe générale du mot-clé `in` est la suivante :

```
substring in string
```

Le mot-clé `in` retourne une valeur booléenne – une valeur qui est soit `True` soit `False`.

```python
>>> "w" in "Hello world!"
True
```

L'opérateur `in` retourne `True` lorsque la sous-chaîne est présente dans la chaîne.

Et si la sous-chaîne n'est pas présente, il retourne `False` :

```python
>>> "a" in "Hello world!"
False
```

L'utilisation du mot-clé `in` est une première étape utile avant d'utiliser la méthode `find()`.

Vous vérifiez d'abord si une chaîne contient une sous-chaîne, puis vous pouvez utiliser `find()` pour trouver la position de la sous-chaîne. Ainsi, vous savez avec certitude que la sous-chaîne est présente.

Donc, utilisez `find()` pour trouver la position d'index d'une sous-chaîne à l'intérieur d'une chaîne et non pour vérifier si la sous-chaîne est présente dans la chaîne.

## La méthode `find()` vs la méthode `index()` – Quelle est la différence ? <a name="find-vs-index"></a>

Similaire à la méthode `find()`, la méthode `index()` est une méthode de chaîne utilisée pour trouver l'index d'une sous-chaîne à l'intérieur d'une chaîne.

Ainsi, les deux méthodes fonctionnent de la même manière.

La différence entre les deux méthodes est que la méthode `index()` lève une exception lorsque la sous-chaîne n'est pas présente dans la chaîne, contrairement à la méthode `find()` qui retourne la valeur `-1`.

```python
fave_phrase = "Hello world!"

# rechercher l'index de la lettre 'a' dans 'Hello world!'
search_fave_phrase = fave_phrase.index("a")

print(search_fave_phrase)

#output

# Traceback (most recent call last):
#  File "/Users/dionysialemonaki/python_article/demopython.py", line 4, in <module>
#    search_fave_phrase = fave_phrase.index("a")
# ValueError: substring not found
```

L'exemple ci-dessus montre que `index()` lève une `ValueError` lorsque la sous-chaîne n'est pas présente.

Vous pourriez vouloir utiliser `find()` plutôt que `index()` lorsque vous ne souhaitez pas gérer la capture et le traitement des exceptions dans vos programmes.

## Conclusion

Et voilà ! Vous savez maintenant comment rechercher une sous-chaîne dans une chaîne en utilisant la méthode `find()`.

J'espère que vous avez trouvé ce tutoriel utile.

Pour en savoir plus sur le langage de programmation Python, consultez [la certification Python de freeCodeCamp](https://www.freecodecamp.org/learn/scientific-computing-with-python/).

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer votre compréhension des concepts que vous avez appris.

Merci d'avoir lu, et bon codage !

Bon codage !