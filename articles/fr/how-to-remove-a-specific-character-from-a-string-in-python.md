---
title: Comment supprimer un caractère spécifique d'une chaîne en Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-12-07T18:43:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-remove-a-specific-character-from-a-string-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-josh-sorenson-1714208.jpg
tags:
- name: Python
  slug: python
seo_title: Comment supprimer un caractère spécifique d'une chaîne en Python
seo_desc: 'When coding in Python, there may be times when you need to remove a character
  from a string.

  Removing characters from strings is handy if you are working with user-generated
  inputs and need to clean your data and remove unwanted characters.

  Specifica...'
---

Lorsque vous codez en Python, il peut arriver que vous deviez supprimer un caractère d'une chaîne.

Supprimer des caractères des chaînes est utile si vous travaillez avec des entrées générées par l'utilisateur et que vous devez nettoyer vos données et supprimer les caractères indésirables.

Plus précisément, vous devrez peut-être supprimer une seule instance d'un caractère ou même toutes les occurrences d'un caractère dans une chaîne.

Python offre de nombreuses façons de vous aider à faire cela.

Deux des méthodes les plus courantes pour supprimer des caractères des chaînes en Python sont :

- utiliser la méthode de chaîne `replace()`
- utiliser la méthode de chaîne `translate()`

Lorsque vous utilisez l'une ou l'autre des deux méthodes, vous pouvez spécifier le ou les caractères que vous souhaitez supprimer de la chaîne.

Les deux méthodes remplacent un caractère par une valeur que vous spécifiez. Et si vous spécifiez un caractère vide à la place, le caractère que vous souhaitez supprimer est effacé sans remplacement.

Une chose à noter lorsque vous utilisez ces méthodes est que la chaîne originale n'est pas altérée puisque les chaînes sont immuables. Au lieu de cela, les deux méthodes retournent une nouvelle chaîne modifiée qui ne contient pas les caractères que vous vouliez supprimer.

Dans cet article, vous apprendrez à utiliser les deux méthodes pour supprimer un ou plusieurs caractères d'une chaîne à l'aide d'exemples de code.

Voici ce que nous allons couvrir :

1. [Comment supprimer un caractère spécifique d'une chaîne en utilisant la méthode `replace()`](#supprimer-caractere-remplacer)
2. [Comment supprimer plusieurs caractères d'une chaîne en utilisant la méthode `replace()`](#supprimer-caracteres-remplacer)
    1. [Supprimer plusieurs caractères avec l'enchaînement de méthodes](#enchainement)
    2. [Supprimer plusieurs caractères avec une boucle `for`](#boucle-for)
    3. [Supprimer plusieurs caractères avec des expressions régulières](#expressions-regulieres)
3. [Comment supprimer un caractère spécifique d'une chaîne en utilisant la méthode `translate()`](#supprimer-caractere-traduire)
4. [Comment supprimer plusieurs caractères d'une chaîne en utilisant la méthode `translate()`](#supprimer-caracteres-traduire)

Commençons !

## Comment supprimer un caractère spécifique d'une chaîne en Python en utilisant la méthode `replace()` <a name="supprimer-caractere-remplacer"></a>

La syntaxe générale de la méthode `replace()` ressemble à ceci :

```
string.replace(caractere, remplacement, compte)
```

Décomposons cela :

- Vous ajoutez la méthode `replace()` à une `string`.
- La méthode `replace()` accepte trois arguments :
    - `caractere` est un argument requis et représente le caractère spécifique que vous souhaitez supprimer de `string`.
    - `remplacement` est un argument requis et représente la nouvelle chaîne/caractère qui prendra la place de `caractere`.
    - `compte` est un argument optionnel qui représente le nombre maximum d'occurrences de `caractere` que vous souhaitez supprimer de `string`. Si vous n'incluez pas `compte`, alors par défaut, la méthode `replace()` supprimera toutes les occurrences de `caractere`.

La méthode `replace()` ne modifie pas la chaîne originale. Au lieu de cela, sa valeur de retour est une copie de la chaîne originale sans les caractères que vous vouliez supprimer.

Maintenant, voyons `replace()` en action !

Supposons que vous avez la chaîne suivante et que vous souhaitez supprimer tous les points d'exclamation :

```python
my_string = "Hi! I! Love! Python!"
```

Voici comment vous supprimeriez toutes les occurrences du caractère `!` :

```python
my_string = "Hi! I! Love! Python!"

my_new_string = my_string.replace("!", "")

print(my_new_string)

# output

# Hi I Love Python
```

Dans l'exemple ci-dessus, j'ai ajouté la méthode `replace()` à `my_string`.

J'ai ensuite stocké le résultat dans une nouvelle variable nommée `my_new_string`.

Rappelez-vous, les chaînes sont immuables. La chaîne originale reste inchangée - `replace()` retourne une nouvelle chaîne et ne modifie pas l'originale.

J'ai spécifié que je voulais supprimer le caractère `!` et indiqué que je voulais remplacer `!` par un caractère vide.

Je n'ai pas non plus utilisé l'argument `compte`, donc `replace()` a remplacé *toutes* les occurrences du caractère `!` par un caractère vide.

La chaîne originale stockée dans une variable `my_string` a quatre occurrences du caractère `!`.

Si je voulais supprimer seulement trois occurrences du caractère et non toutes, j'utiliserais l'argument `compte` et passerais une valeur de `3` pour spécifier le nombre de fois où je souhaite remplacer le caractère :

```python
my_string = "Hi! I! love! Python!"

my_new_string = my_string.replace("!", "", 3)

print(my_new_string)

# output

# Hi I love Python!
```

## Comment supprimer plusieurs caractères d'une chaîne en Python en utilisant la méthode `replace()` <a name="supprimer-caracteres-remplacer"></a>

Il peut arriver que vous deviez remplacer plusieurs caractères d'une chaîne.

Dans les sections suivantes, vous verrez trois façons d'y parvenir en utilisant la méthode `replace()`.

### Supprimer plusieurs caractères avec l'enchaînement de méthodes <a name="enchainement"></a>

Une façon d'y parvenir est d'enchaîner la méthode `replace()` comme suit :

```python
my_string = "Hi!? I!? love!? Python!?"

my_new_string = my_string.replace("!","").replace("?","")

print(my_new_string)

# output

# Hi I love Python
```

Cela dit, cette façon de supprimer des caractères peut être assez difficile à lire.

### Supprimer plusieurs caractères avec une boucle `for` <a name="boucle-for"></a>

Une autre façon d'y parvenir est d'utiliser la méthode `replace()` à l'intérieur d'une boucle `for` :

```python
my_string = "Hi!? I!? love!? Python!?"

replacements = [('!', ''), ('?', '')]

for char, replacement in replacements:
    if char in my_string:
        my_string = my_string.replace(char, replacement)

print(my_string)

# output

# Hi I love Python
```

J'ai d'abord créé une chaîne contenant les deux caractères que je veux supprimer, `!` et `?`, et je l'ai stockée dans la variable `my_string`.

J'ai stocké les caractères que je veux remplacer, ainsi que leurs remplacements, dans une liste de tuples avec le nom `replacements` - je veux remplacer `!` par une chaîne vide et `?` par une chaîne vide.

Ensuite, j'ai utilisé une boucle `for` pour itérer sur la liste de tuples (si vous avez besoin d'un rappel sur les boucles `for`, lisez [cet article](https://www.freecodecamp.org/news/python-for-loop-example-and-tutorial/)).

À l'intérieur de la boucle `for`, j'ai utilisé l'opérateur `in` pour vérifier si les caractères sont dans la chaîne. Et s'ils y étaient, j'ai utilisé la méthode `replace()` pour les remplacer.

Enfin, j'ai réassigné la variable.

### Supprimer plusieurs caractères avec des expressions régulières <a name="expressions-regulieres"></a>

Et une autre façon d'y parvenir est d'utiliser la bibliothèque d'expressions régulières `re` et la méthode `sub`.

Vous devez d'abord importer la bibliothèque :

```python
import re
```

Ensuite, spécifiez le groupe de caractères que vous souhaitez supprimer (dans ce cas, les caractères `!` et `?`), ainsi que les caractères par lesquels vous souhaitez les remplacer. Dans ce cas, le remplacement est un caractère vide :

```python
import re

my_string = "Hi!? I!? love!? Python!?"

my_new_string = re.sub('[!?]',"",my_string)

print(my_new_string)

# output

# Hi I love Python
```

## Comment supprimer un caractère spécifique d'une chaîne en Python en utilisant la méthode `translate()` <a name="supprimer-caractere-traduire"></a>

De manière similaire à la méthode `replace()`, `translate()` supprime des caractères d'une chaîne.

Cela dit, la méthode `translate()` est un peu plus compliquée et pas très adaptée aux débutants.

La méthode `replace()` est la solution la plus simple à utiliser lorsque vous devez supprimer des caractères d'une chaîne.

Lorsque vous utilisez la méthode `translate()` pour remplacer un caractère dans une chaîne, vous devez créer une table de traduction de caractères, où `translate()` utilise le contenu de la table pour remplacer les caractères.

Une table de traduction est un dictionnaire de mappages clé-valeur, et chaque clé est remplacée par une valeur.

Vous pouvez utiliser la fonction `ord()` pour obtenir la valeur Unicode du caractère, puis mapper cette valeur à un autre caractère.

Cette méthode retourne une nouvelle chaîne où chaque caractère de l'ancienne chaîne est mappé à un caractère de la table de traduction.

La valeur de retour est une nouvelle chaîne.

Voyons un exemple en utilisant le même code que dans les sections précédentes :

```python
my_string = "Hi! I! love! Python!"

my_new_string = my_string.translate( { ord("!"): None } )

print(my_new_string)

# output

# Hi I love Python
```

Dans l'exemple ci-dessus, j'ai utilisé la fonction `ord()` pour retourner la valeur Unicode associée au caractère que je voulais remplacer, qui dans ce cas était `!`.

Ensuite, j'ai mappé cette valeur Unicode à `None` - un autre mot pour rien ou vide - ce qui permet de le supprimer. Plus précisément, il a remplacé chaque instance du caractère `!` par une valeur `None`.

## Comment supprimer plusieurs caractères d'une chaîne en Python en utilisant la méthode `translate()` <a name="supprimer-caracteres-traduire"></a>

Et si vous devez remplacer plus d'un caractère en utilisant la méthode `translate()` ? Pour cela, vous pouvez utiliser un itérateur comme suit :

```python
my_string = "Hi!? I!? love!? Python!?"

my_new_string = my_string.translate( { ord(i): None for i in '!?'} )

print(my_new_string)

# output

# Hi I love Python
```

Dans l'exemple ci-dessus, j'ai remplacé les caractères `!` et `?` par la valeur `None` en utilisant un itérateur qui a parcouru les caractères que je voulais supprimer.

La méthode `translate()` vérifie si chaque caractère dans `my_string` est égal à un point d'exclamation ou à un point d'interrogation. Si c'est le cas, il est remplacé par `None`.

## Conclusion

Espérons que cet article vous a aidé à comprendre comment supprimer des caractères d'une chaîne en Python en utilisant les méthodes de chaîne intégrées `replace()` et `translate()`.

Merci d'avoir lu, et bon codage !