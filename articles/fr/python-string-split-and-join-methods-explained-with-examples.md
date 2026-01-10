---
title: Méthodes Python String split() et join() – Expliquées avec des Exemples
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-18T22:40:12.000Z'
originalURL: https://freecodecamp.org/news/python-string-split-and-join-methods-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/split-join.png
tags:
- name: Python
  slug: python
seo_title: Méthodes Python String split() et join() – Expliquées avec des Exemples
seo_desc: 'When working with strings in Python, you may have to split a string into
  substrings. Or you might need to join together smaller chunks to form a string.
  Python''s split() and join() string methods help you do these tasks easily.

  In this tutorial, you''...'
---

Lorsque vous travaillez avec des chaînes de caractères en Python, vous pouvez avoir besoin de diviser une chaîne en sous-chaînes. Ou vous pourriez avoir besoin de joindre des morceaux plus petits pour former une chaîne. Les méthodes de chaîne `split()` et `join()` de Python vous aident à effectuer ces tâches facilement.

Dans ce tutoriel, vous apprendrez à utiliser les méthodes de chaîne `split()` et `join()` avec de nombreux exemples de code.

Comme les chaînes de caractères en Python sont immuables, vous pouvez appeler des méthodes sur elles sans modifier les chaînes originales. Commençons.

## Syntaxe de la Méthode `split()` en Python

Lorsque vous devez diviser une chaîne en sous-chaînes, vous pouvez utiliser la méthode `split()`.

La méthode `split()` agit sur une chaîne et _retourne_ une liste de sous-chaînes. La syntaxe est :

```python
<chaîne>.split(sep, maxsplit)
```

Dans la syntaxe ci-dessus :

* `<chaîne>` est une chaîne Python valide,
* `sep` est le séparateur sur lequel vous souhaitez diviser. Il doit être spécifié comme une _chaîne_.

> Par exemple, si vous souhaitez diviser `<chaîne>` à l'occurrence d'une virgule, vous pouvez définir `sep = ","`.

* `sep` est un argument _optionnel_. Par défaut, cette méthode divise les chaînes sur les _espaces blancs_.
* `maxsplit` est un argument _optionnel_ indiquant le nombre de fois où vous souhaitez diviser `<chaîne>`.
* `maxsplit` a une valeur par défaut de `-1`, qui divise la chaîne sur _toutes_ les occurrences de `sep`.

> Si vous souhaitez diviser `<chaîne>` à l'occurrence de la _première_ virgule, vous pouvez définir `maxsplit = 1`.

Et définir `maxsplit = 1` vous laissera avec deux morceaux – un avec la section de `<chaîne>` avant la première virgule, et un autre avec la section de `<chaîne>` après la première virgule.

Lorsque vous divisez une chaîne une fois, vous obtenez 2 morceaux. Lorsque vous divisez une chaîne deux fois, vous obtenez 3 morceaux. Lorsque vous divisez une chaîne `k` fois, vous obtenez `k+1` morceaux.

➡️ Prenons quelques exemples pour voir la méthode `split()` en action.

## Exemples de la Méthode `split()` en Python

Commençons par `ma_chaîne` présentée ci-dessous.

```python
ma_chaîne = "Je code pendant 2 heures tous les jours"
```

Maintenant, appelez la méthode `split()` sur `ma_chaîne`, sans les arguments `sep` et `maxsplit`.

```python
ma_chaîne.split()
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-50.png)

Vous pouvez voir que `ma_chaîne` a été divisée sur tous les espaces blancs et la liste des sous-chaînes est retournée, comme montré ci-dessus.

➡️ Considérons maintenant l'exemple suivant. Ici, `ma_chaîne` contient des noms de fruits, séparés par des virgules.

```python
ma_chaîne = "Pommes,Oranges,Poires,Bananes,Baies"
```

Divisons maintenant `ma_chaîne` sur les virgules – définissons `sep = ","` ou spécifions uniquement `","` dans l'appel de la méthode.

```python
ma_chaîne.split(",")
```

Comme prévu, la méthode `split()` retourne une liste de fruits, où chaque fruit dans `ma_chaîne` est maintenant un élément de la liste.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-51.png)

➡️ Utilisons maintenant l'argument optionnel `maxsplit` en le définissant égal à 2.

```python
ma_chaîne.split(",", 2)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-52.png)

Essayons d'analyser la liste retournée.

Rappelons que `ma_chaîne` est `"Pommes,Oranges,Poires,Bananes,Baies"`, et nous avons décidé de diviser sur les virgules (`","`).

* La première virgule est après `Pommes`, et après la première division, vous aurez 2 éléments, `Pommes` et `Oranges,Poires,Bananes,Baies`.
* La deuxième virgule est après `Oranges`. Et vous aurez 3 éléments, `Pommes`, `Oranges`, et `Poires,Bananes,Baies` après la deuxième division.
* À ce stade, vous avez atteint le compte `maxsplit` de 2, et aucune autre division ne peut être faite.
* C'est pourquoi la portion de la chaîne après la deuxième virgule est regroupée en un seul élément dans la liste retournée.

J'espère que vous comprenez comment la méthode `split()` et les arguments `sep` et `maxsplit` fonctionnent.

## Syntaxe de la Méthode `join()` en Python

Maintenant que vous savez comment diviser une chaîne en sous-chaînes, il est temps d'apprendre à utiliser la méthode `join()` pour former une chaîne à partir de sous-chaînes.

La syntaxe de la méthode `join()` de Python est :

```python
<sep>.join(<itérable>)
```

Ici,

* `<itérable>` est un itérable Python contenant les sous-chaînes, par exemple, une liste ou un tuple, et
* `<sep>` est le séparateur que vous souhaitez utiliser pour joindre les sous-chaînes.

> En essence, la méthode `join()` joint tous les éléments dans `<itérable>` en utilisant `<sep>` comme séparateur.

➡️ Et il est temps pour des exemples.

## Exemples de la Méthode `join()` en Python

Dans la section précédente sur la méthode `split()`, vous avez divisé `ma_chaîne` en une liste à l'occurrence des virgules. Appelons la liste `ma_liste`.

Maintenant, vous allez former une chaîne en utilisant la méthode `join()` pour assembler les éléments de la liste retournée. Les éléments de `ma_liste` sont tous des noms de fruits.

```python
ma_liste = ma_chaîne.split(",")

# après que ma_chaîne est divisée, ma_liste est :
['Pommes', 'Oranges', 'Poires', 'Bananes', 'Baies']


```

📝 Notez que le séparateur pour joindre doit être spécifié comme une _chaîne_. Vous rencontrerez des erreurs de syntaxe si vous ne le faites pas, comme montré ci-dessous.

```python
,.join(ma_liste)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-49.png)

➡️ Pour joindre les éléments de `ma_liste` en utilisant une virgule comme séparateur, utilisez `","` et non `,`. Cela est montré dans l'extrait de code ci-dessous.

```python
", ".join(ma_liste)
```

La ligne de code ci-dessus joint les éléments de `ma_liste` en utilisant une virgule suivie d'un espace comme séparateur.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-53.png)

Vous pouvez spécifier n'importe quel séparateur de votre choix. Cette fois, vous allez utiliser 3 traits de soulignement (`___`) pour joindre les éléments de `ma_liste`.

```python
"___".join(ma_liste)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-54.png)

Les éléments de `ma_liste` ont maintenant été joints en une seule chaîne, et ont tous été séparés les uns des autres par un `___`.

Et vous savez maintenant comment vous pouvez former une chaîne Python en assemblant des sous-chaînes en utilisant la méthode `join()`.

## Conclusion

Dans ce tutoriel, vous avez appris ce qui suit :

* `<chaîne>.split(sep, maxsplit)` divise `<chaîne>` à l'occurrence de `sep`, `maxsplit` nombre de fois,
* `<sep>.join(<itérable>)` joint les sous-chaînes dans `<itérable>` en utilisant `<sep>` comme séparateur.

J'espère que vous avez trouvé ce tutoriel utile. Bon codage !