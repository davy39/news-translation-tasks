---
title: Python List .remove() - Comment supprimer un élément d'une liste en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-03-02T19:49:19.000Z'
originalURL: https://freecodecamp.org/news/python-list-remove-how-to-remove-an-item-from-a-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pavel-danilyuk-5496463.jpg
tags:
- name: Python
  slug: python
seo_title: Python List .remove() - Comment supprimer un élément d'une liste en Python
seo_desc: 'In this article, you''ll learn how to use Python''s built-in remove() list
  method.

  By the end, you''ll know how to use remove() to remove an item from a list in Python.

  Here is what we will cover:


  Syntax of the remove() method

  Remove an element from a ...'
---

Dans cet article, vous apprendrez à utiliser la méthode intégrée `remove()` des listes en Python.

À la fin, vous saurez comment utiliser `remove()` pour supprimer un élément d'une liste en Python.

Voici ce que nous allons couvrir :

1. [Syntaxe de la méthode `remove()`](#syntaxe)
2. [Supprimer un élément d'une liste en utilisant `remove()`](#demo-intro)
3. [`remove()` supprime uniquement la première occurrence d'un élément](#premiere-occurrence)
    1. [Comment supprimer toutes les occurrences d'un élément](#toutes-les-occurrences)

## La méthode `remove()` - Aperçu de la syntaxe <a name="syntaxe"></a>

La méthode `remove()` est l'une des façons de supprimer des éléments d'une liste en Python.

La méthode `remove()` supprime un élément d'une liste par sa **valeur** et non par son numéro d'index.

La syntaxe générale de la méthode `remove()` ressemble à ceci :

```python
nom_liste.remove(valeur)
```

Décomposons cela :

- `nom_liste` est le nom de la liste avec laquelle vous travaillez.
- `remove()` est l'une des méthodes intégrées des listes en Python.
- `remove()` prend un seul argument **requis**. Si vous ne le fournissez pas, vous obtiendrez une erreur `TypeError` – spécifiquement, vous obtiendrez une erreur `TypeError: list.remove() prend exactement un argument (0 donné)`.
- `valeur` est la valeur spécifique de l'élément que vous souhaitez supprimer de `nom_liste`.

La méthode `remove()` ne retourne pas la valeur qui a été supprimée mais retourne simplement `None`, ce qui signifie qu'il n'y a pas de valeur de retour.

Si vous devez supprimer un élément par son numéro d'index et/ou pour une raison quelconque vous souhaitez retourner (sauvegarder) la valeur que vous avez supprimée, utilisez plutôt la [méthode `pop()`](https://www.freecodecamp.org/news/python-pop-how-to-pop-from-a-list-or-an-array-in-python/).


## Comment supprimer un élément d'une liste en utilisant la méthode `remove()` en Python <a name="demo-intro"></a>

Pour supprimer un élément d'une liste en utilisant la méthode `remove()`, spécifiez la valeur de cet élément et passez-la comme argument à la méthode.

`remove()` recherchera dans la liste pour le trouver et le supprimer.

```python
# liste originale
langages_de_programmation = ["JavaScript", "Python", "Java", "C++"]

# imprimer la liste originale
print(langages_de_programmation)

# supprimer la valeur 'JavaScript' de la liste
langages_de_programmation.remove("JavaScript")

# imprimer la liste mise à jour
print(langages_de_programmation)

# sortie

# ['JavaScript', 'Python', 'Java', 'C++']
# ['Python', 'Java', 'C++']
```

Si vous spécifiez une valeur qui n'est pas contenue dans la liste, vous obtiendrez une erreur – spécifiquement, l'erreur sera une `ValueError` :

```python
langages_de_programmation = ["JavaScript", "Python", "Java", "C++"]

# Je veux supprimer la valeur 'React'
langages_de_programmation.remove("React")

# imprimer la liste
print(langages_de_programmation)

# sortie

# ligne 5, dans <module>
# langages_de_programmation.remove("React")
# ValueError: list.remove(x): x not in list
```

Pour éviter que cette erreur ne se produise, vous pourriez d'abord vérifier si la valeur que vous souhaitez supprimer est dans la liste, en utilisant le mot-clé `in`.

Il retournera une valeur booléenne – `True` si l'élément est dans la liste ou `False` si la valeur n'est pas dans la liste.

```python
langages_de_programmation = ["JavaScript", "Python", "Java", "C++"]

# vérifier si 'React' est dans la liste 'langages_de_programmation'
print("React" in langages_de_programmation)

# sortie
# False
```

Une autre façon d'éviter cette erreur est de créer une condition qui dit essentiellement : "Si cette valeur fait partie de la liste, alors supprimez-la. Si elle n'existe pas, alors affichez un message indiquant qu'elle n'est pas contenue dans la liste".

```python
langages_de_programmation = ["JavaScript", "Python", "Java", "C++"]

if "React" in langages_de_programmation:
    langages_de_programmation.remove("React")
else:
    print("Cette valeur n'existe pas")
    
# sortie
# Cette valeur n'existe pas
```

Maintenant, au lieu d'obtenir une erreur Python lorsque vous essayez de supprimer une certaine valeur qui n'existe pas, vous obtenez un message indiquant que l'élément que vous vouliez supprimer n'est pas dans la liste avec laquelle vous travaillez.

## La méthode `remove()` supprime la première occurrence d'un élément dans une liste <a name="premiere-occurrence"></a>

Une chose à garder à l'esprit lors de l'utilisation de la méthode `remove()` est qu'elle recherchera et supprimera uniquement la **première** instance d'un élément.

Cela signifie que si dans la liste il y a plus d'une instance de l'élément dont la valeur vous avez passée comme argument à la méthode, alors seule la première occurrence sera supprimée.

Regardons l'exemple suivant :

```python
langages_de_programmation = ["JavaScript", "Python", "Java", "Python", "C++", "Python"]

langages_de_programmation.remove("Python")

print(langages_de_programmation)

# sortie
# ['JavaScript', 'Java', 'Python', 'C++', 'Python']
```

Dans l'exemple ci-dessus, l'élément avec la valeur `Python` est apparu trois fois dans la liste.

Lorsque `remove()` a été utilisé, seule la première instance correspondante a été supprimée – celle suivant la valeur `JavaScript` et précédant la valeur `Java`.

Les deux autres occurrences de `Python` restent dans la liste.

Que se passe-t-il cependant lorsque vous souhaitez supprimer toutes les occurrences d'un élément ?

L'utilisation de `remove()` seul ne permet pas d'y parvenir, et vous ne souhaitez peut-être pas supprimer uniquement la première instance de l'élément que vous avez spécifié.

### Comment supprimer toutes les instances d'un élément dans une liste en Python <a name="toutes-les-occurrences"></a>
 
L'une des façons de supprimer toutes les occurrences d'un élément dans une liste est d'utiliser la compréhension de liste.

La compréhension de liste crée une nouvelle liste à partir d'une liste existante, ou crée ce que l'on appelle une sous-liste.

Cela ne modifiera pas votre liste originale, mais créera plutôt une nouvelle liste qui satisfait une condition que vous avez définie.


```python
# liste originale
langages_de_programmation = ["JavaScript", "Python", "Java", "Python", "C++", "Python"]

# sous-liste créée avec la compréhension de liste
langages_de_programmation_mis_a_jour = [valeur for valeur in langages_de_programmation if valeur != "Python"]


# imprimer la liste originale
print(langages_de_programmation)

# imprimer la nouvelle sous-liste qui ne contient pas 'Python'
print(langages_de_programmation_mis_a_jour)

# sortie

# ['JavaScript', 'Python', 'Java', 'Python', 'C++', 'Python']
# ['JavaScript', 'Java', 'C++']
```

Dans l'exemple ci-dessus, il y a la liste originale `langages_de_programmation`.

Ensuite, une nouvelle liste (ou sous-liste) est retournée.

Les éléments contenus dans la sous-liste doivent répondre à une condition. La condition était que si un élément de la liste originale avait une valeur de `Python`, il ne ferait pas partie de la sous-liste.

Maintenant, si vous ne souhaitez pas créer une nouvelle liste, mais plutôt modifier la liste déjà existante *en place*, utilisez alors l'affectation de tranche combinée avec la compréhension de liste.

Avec l'affectation de tranche, vous pouvez modifier et remplacer certaines parties (ou tranches) d'une liste.

Pour remplacer toute la liste, utilisez la syntaxe de tranchage `[:]`, ainsi que la compréhension de liste.

La compréhension de liste définit la condition que tout élément avec une valeur de `Python` ne fera plus partie de la liste.

```python
langages_de_programmation = ["JavaScript", "Python", "Java", "Python", "C++", "Python"]

langages_de_programmation[:] = (valeur for valeur in langages_de_programmation if valeur != "Python")

print(langages_de_programmation)

# sortie

# ['JavaScript', 'Java', 'C++']
```

## Conclusion

Et voilà ! Vous savez maintenant comment supprimer un élément d'une liste en Python en utilisant la méthode `remove()`. Vous avez également vu quelques façons de supprimer toutes les occurrences d'un élément dans une liste en Python.

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [Certification en calcul scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage 😊 !