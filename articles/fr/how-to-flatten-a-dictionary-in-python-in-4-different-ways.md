---
title: Comment aplatir un dictionnaire en Python de 4 manières différentes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-27T19:59:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-flatten-a-dictionary-in-python-in-4-different-ways
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/convert_nested_dictionary_flat_one_python.png
tags:
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Comment aplatir un dictionnaire en Python de 4 manières différentes
seo_desc: 'By Miguel Brito

  In this post, we’ll look at 4 different ways to flatten a dict in Python. For each
  method I’ll point out the pros and cons, and I''ll give a quick performance analysis.
  For this tutorial, I ran all examples on Python 3.7.

  Why Should Yo...'
---

Par Miguel Brito

Dans cet article, nous allons examiner 4 manières différentes d'aplatir un dictionnaire en Python. Pour chaque méthode, je soulignerai les **avantages et inconvénients**, et je donnerai une rapide analyse de performance. Pour ce tutoriel, j'ai exécuté tous les exemples sur Python 3.7.

## Pourquoi devriez-vous savoir comment aplatir un dictionnaire en Python ?

Il existe de nombreuses raisons pour lesquelles vous pourriez avoir besoin d'un dictionnaire aplati. L'une d'elles est qu'il est plus simple de [comparer deux dictionnaires](https://miguendes.me/the-best-way-to-compare-two-dictionaries-in-python). L'autre est qu'il est plus facile de le naviguer et de le manipuler, car une structure plate n'a qu'un seul niveau de profondeur.

Python est un langage polyvalent, ce qui signifie que vous pouvez atteindre les mêmes objectifs de plusieurs manières. Choisir la meilleure solution pour un problème nécessite de peser les avantages d'une solution par rapport à une autre.

Le but de cet article est de vous fournir de nombreuses options pour ce problème et de vous donner autant de données que possible afin que vous puissiez prendre une décision éclairée. Alors, commençons.

PS : Si vous n'avez pas Python 3.7, vous pouvez l'installer en utilisant `pyenv` et même avoir [plusieurs versions en même temps](https://miguendes.me/how-i-set-up-my-python-workspace) sans conflit.

## Table des matières

1. [Utilisation de votre propre fonction récursive](heading-comment-aplatir-un-dictionnaire-en-python-en-utilisant-votre-propre-fonction-recursive)
2. [Utilisation de votre propre fonction récursive + générateurs](heading-comment-aplatir-un-dictionnaire-en-python-en-utilisant-votre-propre-fonction-recursive-generateurs)
3. [Utilisation de pandas json_normalize](heading-comment-aplatir-un-dictionnaire-en-python-en-utilisant-pandas-jsonnormalize)
4. [Utilisation de la bibliothèque flatdict](heading-comment-aplatir-un-dictionnaire-en-python-en-utilisant-la-bibliotheque-flatdict)
5. [Conclusion](heading-conclusion)

## Comment aplatir un dictionnaire en Python en utilisant votre propre fonction récursive

Un rapide coup d'œil sur Google nous mène à [stackoverflow](https://stackoverflow.com). La [première réponse](https://stackoverflow.com/a/6027615) montre une fonction récursive qui parcourt le dictionnaire et retourne une instance aplatie. Je vais m'inspirer de cette fonction et montrer une version légèrement améliorée.

Nous pouvons commencer par ajouter des indications de type pour améliorer la lisibilité et la rendre plus sûre.

```python
from collections.abc import MutableMapping

def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str ='.') -> MutableMapping:
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


>>> flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
{'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}

```

### Benchmark de performance

Nous avons rapidement vérifié que la fonction retourne un dictionnaire plat, mais qu'en est-il de ses performances ? Est-elle adaptée à une utilisation en production ? Exécutons un rapide benchmark pour voir sa vitesse.

Pour ce benchmark et tous les benchmarks de cet article, j'utiliserai la fonction magique `timeit` de `IPython` et `memit` de la bibliothèque [`memory_profiler`](https://pypi.org/project/memory-profiler/).

PS : Pour que `%memit` fonctionne, vous devez d'abord exécuter `%load_ext memory_profiler`.

```python
In [4]: %timeit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
7.28 µs ± 54.6 ns par boucle (moyenne ± écart-type de 7 exécutions, 100000 boucles chacune)

In [5]: %load_ext memory_profiler

In [6]: %memit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
pic mémoire : 84.94 MiB, incrément : 0.29 MiB

```

**Avantages :** Facile à comprendre, et ça marche.

**Inconvénients :** Il stocke les éléments dans une liste en mémoire qui est ensuite passée au constructeur `dict`. Cela est gaspilleur non seulement en termes de mémoire mais aussi de vitesse.

Même si ajouter des éléments à une liste en Python est rapide, le faire de manière répétée n'est pas réellement nécessaire. Dans la section suivante, nous verrons comment améliorer cela en utilisant des générateurs.

## Comment aplatir un dictionnaire en Python en utilisant votre propre fonction récursive + générateurs

La première version fonctionne et est quelque peu rapide. Cependant, elle a un problème.

Pour créer un nouveau dictionnaire avec les clés aplaties, elle maintient en mémoire une liste Python. Cela est inefficace, car nous devons garder une structure de données entière en mémoire juste pour servir de stockage temporaire.

Une solution bien meilleure est d'utiliser les [générateurs de Python](https://docs.python.org/3/glossary.html#term-generator), qui est un objet capable de suspendre l'exécution et de se souvenir de l'état qui peut être repris plus tard. En utilisant un générateur, nous pouvons nous débarrasser de la liste temporaire sans changer le comportement.

```python
from collections.abc import MutableMapping

def _flatten_dict_gen(d, parent_key, sep):
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, MutableMapping):
            yield from flatten_dict(v, new_key, sep=sep).items()
        else:
            yield new_key, v


def flatten_dict(d: MutableMapping, parent_key: str = '', sep: str = '.'):
    return dict(_flatten_dict_gen(d, parent_key, sep))

>>> flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
{'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}

```

### Benchmark de performance

```python
In [9]: %timeit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
7.39 µs ± 78.7 ns par boucle (moyenne ± écart-type de 7 exécutions, 100000 boucles chacune)

In [7]: %memit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
pic mémoire : 45.27 MiB, incrément : 0.25 MiB

```

**Avantages :** Facile à comprendre, ça marche comme la version précédente, et c'est efficace en mémoire. Cette version consomme environ 50 % de mémoire en moins que la version utilisant des listes.

**Inconvénients :** Cela ne gère peut-être pas très bien les cas limites. Par exemple, si nous passons un objet de type dictionnaire qui n'est pas une instance de `MutableMapping`, alors cet exemple échouera. Mais c'est aussi un inconvénient de la version précédente.

## Comment aplatir un dictionnaire en Python en utilisant pandas `json_normalize`

Les solutions précédentes fonctionnent bien, comme nous pouvons le voir, mais écrire notre propre solution pour un problème courant comme celui-ci revient à réinventer la roue. En alternative, nous pouvons utiliser des bibliothèques populaires de manipulation de données telles que [`pandas`](https://pandas.pydata.org).

`pandas` vient avec une [fonction générique pour normaliser les objets JSON](https://pandas.pydata.org/docs/user_guide/io.html?highlight=json_normalize#normalization) qui sont représentés en Python sous forme de dictionnaire. C'est une excellente opportunité pour nous de ne pas recréer des solutions existantes et d'utiliser une solution plus robuste.

De plus, le résultat final est excellent en une seule ligne, et nous pouvons même le cacher derrière une interface mince.

```python
from collections.abc import MutableMapping
import pandas as pd

def flatten_dict(d: MutableMapping, sep: str= '.') -> MutableMapping:
    [flat_dict] = pd.json_normalize(d, sep=sep).to_dict(orient='records')
    return flat_dict


>>> flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
{'a': 1, 'd': [6, 7, 8], 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5}

```

### Benchmark de performance

```python
In [5]: %timeit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
779 µs ± 10.7 µs par boucle (moyenne ± écart-type de 7 exécutions, 1000 boucles chacune)

In [6]: %memit flatten_dict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]})
pic mémoire : 86.30 MiB, incrément : 0.90 MiB

```

**Avantages :** Facile à comprendre, et nous réutilisons une bibliothèque bien établie.

**Inconvénients :** Utiliser `pandas` juste pour aplatir un dictionnaire semble exagéré. Si votre projet n'en a pas besoin, alors nous pouvons utiliser une bibliothèque plus légère comme `FlatDict`. De plus, selon `timeit`, cette version est **100 fois plus lente** que l'utilisation de notre propre solution, ce qui n'est pas idéal.

## Comment aplatir un dictionnaire en Python en utilisant la bibliothèque `flatdict`

[`flatdict`](https://flatdict.readthedocs.io/en/stable/index.html) est une bibliothèque Python qui crée un dictionnaire à un seul niveau à partir d'un dictionnaire imbriqué et est disponible à partir de Python 3.5.

Nous avons vu jusqu'à présent que l'écriture de notre propre solution peut ne pas être idéale, et l'utilisation d'une bibliothèque complète comme `pandas` juste à cette fin n'est pas non plus idéale.

En alternative, nous pouvons utiliser `flatdict`, qui est beaucoup plus légère et testée en conditions réelles.

La bibliothèque est très polyvalente et permet également d'utiliser des séparateurs personnalisés. Cependant, l'une des meilleures fonctionnalités qu'elle offre est la possibilité d'accéder au nouveau dictionnaire créé comme avant, c'est-à-dire que vous pouvez accéder aux valeurs en utilisant soit les nouvelles clés, soit les anciennes.

Voyons un exemple.

```python
>>> import flatdict
>>> d =  flatdict.FlatDict(data, delimiter='.')

# d est une instance de FlatDict
>>> d
<FlatDict id=140665244199904 {'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}>"

# et il permet d'accéder aux clés plates
>>> d['c.b.y']
4

# mais aussi aux clés imbriquées
>>> d['c']['b']['y']
4

# et peut être converti en un dictionnaire plat
>>> dict(d)
{'a': 1, 'c.a': 2, 'c.b.x': 3, 'c.b.y': 4, 'c.b.z': 5, 'd': [6, 7, 8]}

```

Comme vous pouvez le voir, `flatdict` permet une grande flexibilité et commodité.

### Benchmark de performance

```python
In [3]: %timeit flatdict.FlatDict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}, delimiter='.')
8.97 µs ± 21.6 ns par boucle (moyenne ± écart-type de 7 exécutions, 100000 boucles chacune)

In [4]: %memit flatdict.FlatDict({'a': 1, 'c': {'a': 2, 'b': {'x': 3, 'y': 4, 'z': 5}}, 'd': [6, 7, 8]}, delimiter='.')
pic mémoire : 45.21 MiB, incrément : 0.14 MiB

```

**Avantages :** Facile à comprendre, ça marche, et c'est une bibliothèque légère. Permet d'accéder aux éléments imbriqués de deux manières différentes. Tout aussi rapide et efficace en mémoire que la solution utilisant des générateurs.

**Inconvénients :** C'est toujours une bibliothèque externe, et comme beaucoup d'outils open-source, s'il y a un bug, vous devez attendre que l'auteur le corrige. Et parfois les auteurs abandonnent leurs projets, ce qui introduit un risque pour votre projet. Néanmoins, je pense toujours que les avantages l'emportent sur les inconvénients dans ce cas.

## Conclusion

Dans cet article, nous avons vu 4 manières différentes d'aplatir un dictionnaire en Python. Chaque solution présente des avantages et des inconvénients, et choisir la meilleure dépend des préférences personnelles et des contraintes du projet.

J'espère que vous avez aimé cet article et je vous dis à la prochaine fois !