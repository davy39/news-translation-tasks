---
title: Créer un Dictionnaire en Python – Méthodes des Dictionnaires Python
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2022-03-14T14:19:43.000Z'
originalURL: https://freecodecamp.org/news/create-a-dictionary-in-python-python-dict-methods
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-kevin-ku-577585.jpg
tags:
- name: beginner
  slug: beginner
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Créer un Dictionnaire en Python – Méthodes des Dictionnaires Python
seo_desc: 'In this article, you will learn the basics of dictionaries in Python.

  You will learn how to create dictionaries, access the elements inside them, and
  how to modify them depending on your needs.

  You will also learn some of the most common built-in met...'
---

Dans cet article, vous apprendrez les bases des dictionnaires en Python.

Vous apprendrez comment créer des dictionnaires, accéder aux éléments qu'ils contiennent et comment les modifier selon vos besoins.

Vous apprendrez également certaines des méthodes intégrées les plus courantes utilisées sur les dictionnaires.

Voici ce que nous allons couvrir :

1. [Définir un dictionnaire](#definition-introduction)
    1. [Définir un dictionnaire vide](#definition-vide)
    2. [Définir un dictionnaire avec des éléments](#definition-elements)
2. [Aperçu des clés et des valeurs](#aperçu)
    1. [Trouver le nombre de paires `clé-valeur` contenues dans un dictionnaire](#longueur)
    2. [Voir toutes les paires `clé-valeur`](#clé-valeur)
    3. [Voir toutes les `clés`](#clés)
    4. [Voir toutes les `valeurs`](#valeurs)
3. [Accéder aux éléments individuels](#accès)
4. [Modifier un dictionnaire](#modifier)
    1. [Ajouter de nouveaux éléments](#ajouter)
    2. [Mettre à jour les éléments](#mettre-à-jour)
    3. [Supprimer des éléments](#supprimer)

## Comment Créer un Dictionnaire en Python <a name="definition-introduction"></a>

Un dictionnaire en Python est composé de paires clé-valeur.

Dans les deux sections suivantes, vous verrez deux façons de créer un dictionnaire.

La première façon est d'utiliser un ensemble d'accolades, `{}`, et la deuxième façon est d'utiliser la fonction intégrée `dict()`.

### Comment Créer un Dictionnaire Vide en Python <a name="definition-vide"></a>

Pour créer un dictionnaire vide, commencez par créer un nom de variable qui sera le nom du dictionnaire.

Ensuite, attribuez la variable à un ensemble vide d'accolades, `{}`.

```python
#créer un dictionnaire vide
mon_dictionnaire = {}

print(mon_dictionnaire)

#pour vérifier le type de données, utilisez la fonction type()
print(type(mon_dictionnaire))

#sortie

#{}
#<class 'dict'>
```

Une autre façon de créer un dictionnaire vide est d'utiliser la fonction `dict()` sans passer d'arguments.

Elle agit comme un constructeur et crée un dictionnaire vide :

```python
#créer un dictionnaire vide
mon_dictionnaire = dict()

print(mon_dictionnaire)

#pour vérifier le type de données, utilisez la fonction type()
print(type(mon_dictionnaire))

#sortie

#{}
#<class 'dict'>
```

### Comment Créer un Dictionnaire avec des Éléments en Python <a name="definition-elements"></a>

Pour créer un dictionnaire avec des éléments, vous devez inclure des paires *clé-valeur* à l'intérieur des accolades.

La syntaxe générale pour cela est la suivante :

```python
nom_dictionnaire = {clé: valeur}
```

Décomposons cela :

- `nom_dictionnaire` est le nom de la variable. C'est le nom que le dictionnaire aura.
- `=` est l'opérateur d'affectation qui attribue la paire `clé:valeur` au `nom_dictionnaire`.
- Vous déclarez un dictionnaire avec un ensemble d'accolades, `{}`.
- À l'intérieur des accolades, vous avez une paire clé-valeur. Les clés sont séparées de leurs valeurs associées par un deux-points, `:`.

Voyons un exemple de création d'un dictionnaire avec des éléments :

```python
#créer un dictionnaire
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

print(mes_informations)

#vérifier le type de données
print(type(mes_informations))

#sortie

#{'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}
#<class 'dict'>
```

Dans l'exemple ci-dessus, il y a une séquence d'éléments à l'intérieur des accolades.

Plus précisément, il y a trois paires clé-valeur : `'nom': 'Dionysia'`, `'âge': 28`, et `'emplacement': 'Athènes'`.

Les clés sont `nom`, `âge`, et `emplacement`. Leurs valeurs associées sont `Dionysia`, `28`, et `Athènes`, respectivement.

Lorsque plusieurs paires clé-valeur sont présentes dans un dictionnaire, chaque paire clé-valeur est séparée de la suivante par une virgule, `,`.

Voyons un autre exemple.

Supposons que vous souhaitez créer un dictionnaire avec des éléments en utilisant cette fois la fonction `dict()`.

Vous y parviendriez en utilisant `dict()` et en passant les accolades avec la séquence de paires clé-valeur qu'elles contiennent comme argument à la fonction.

```python
#créer un dictionnaire avec dict()
mes_informations = dict({'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'})

print(mes_informations)

#vérifier le type de données
print(type(mes_informations))

#sortie

#{'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}
#<class 'dict'>
```

Il est intéressant de mentionner la méthode `fromkeys()`, qui est une autre façon de créer un dictionnaire.

Elle prend une séquence prédéfinie d'éléments comme argument et retourne un nouveau dictionnaire avec les éléments de la séquence définis comme les clés spécifiées du dictionnaire.

Vous pouvez *optionnellement* définir une valeur pour toutes les clés, mais par défaut la valeur des clés sera `None`.

La syntaxe générale de la méthode est la suivante :

```python
nom_dictionnaire = dict.fromkeys(séquence,valeur)
```

Voyons un exemple de création d'un dictionnaire en utilisant `fromkeys()` sans définir de valeur pour toutes les clés :

```python
#créer une séquence de chaînes
villes = ('Paris','Athènes', 'Madrid')

#créer le dictionnaire, `mon_dictionnaire`, en utilisant la méthode fromkeys()
mon_dictionnaire = dict.fromkeys(villes)

print(mon_dictionnaire)

#{'Paris': None, 'Athènes': None, 'Madrid': None}
```

Maintenant, voyons un autre exemple qui définit une valeur qui sera la même pour toutes les clés du dictionnaire :

```python
#créer une séquence de chaînes
villes = ('Paris','Athènes', 'Madrid')

#créer une seule valeur
continent = 'Europe'

mon_dictionnaire = dict.fromkeys(villes,continent)

print(mon_dictionnaire)

#sortie

#{'Paris': 'Europe', 'Athènes': 'Europe', 'Madrid': 'Europe'}
```

## Aperçu des Clés et des Valeurs dans les Dictionnaires en Python <a name="aperçu"></a>

Les clés à l'intérieur d'un dictionnaire Python ne peuvent **être que d'un type immuable**.

Les types de données immuables en Python sont les `entiers`, les `chaînes`, les `tuples`, les `nombres à virgule flottante`, et les `booléens`.

Les clés des dictionnaires **ne peuvent pas** être d'un type mutable, comme les `ensembles`, les `listes`, ou les `dictionnaires`.

Ainsi, supposons que vous avez le dictionnaire suivant :

```python
mon_dictionnaire = {True: "True", 1: 1, 1.1: 1.1, "one": 1, "languages": ["Python"]}

print(mon_dictionnaire)

#sortie

#{True: 1, 1.1: 1.1, 'one': 1, 'languages': ['Python']}
```

Les clés du dictionnaire sont de types de données `booléen`, `entier`, `nombre à virgule flottante`, et `chaîne`, qui sont tous acceptables.

Si vous essayez de créer une clé qui est d'un type mutable, vous obtiendrez une erreur - spécifiquement l'erreur sera une `TypeError`.

```python
mon_dictionnaire = {["Python"]: "languages"}

print(mon_dictionnaire)

#sortie

#line 1, in <module>
#    mon_dictionnaire = {["Python"]: "languages"}
#TypeError: unhashable type: 'list'
```

Dans l'exemple ci-dessus, j'ai essayé de créer une clé qui était de type `liste` (un type de données mutable). Cela a entraîné une erreur `TypeError: unhashable type: 'list'`.

En ce qui concerne les valeurs à l'intérieur d'un dictionnaire Python, il n'y a pas de restrictions. Les valeurs peuvent être de n'importe quel type de données - c'est-à-dire qu'elles peuvent être à la fois de types mutables et immuables.

Une autre chose à noter concernant les différences entre les clés et les valeurs dans les dictionnaires Python est le fait que les clés sont **uniques**. Cela signifie qu'une clé ne peut apparaître qu'une seule fois dans le dictionnaire, alors qu'il peut y avoir des valeurs en double.

### Comment Trouver le Nombre de Paires `clé-valeur` Contenues dans un Dictionnaire en Python <a name="longueur"></a>

La fonction `len()` retourne la longueur totale de l'objet qui est passé comme argument.

Lorsque qu'un dictionnaire est passé comme argument à la fonction, elle retourne le nombre total de paires clé-valeur contenues dans le dictionnaire.

Voici comment calculer le nombre de paires clé-valeur en utilisant `len()` :

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

print(len(mes_informations))

#sortie

#3
```

### Comment Voir Toutes les Paires `clé-valeur` Contenues dans un Dictionnaire en Python <a name="clé-valeur"></a>

Pour voir chaque paire clé-valeur qui se trouve dans un dictionnaire, utilisez la méthode intégrée `items()` :

```python
année_de_création = {'Python': 1993, 'JavaScript': 1995, 'HTML': 1993}

print(année_de_création.items())

#sortie

#dict_items([('Python', 1993), ('JavaScript', 1995), ('HTML', 1993)])
```

La méthode `items()` retourne une liste de tuples qui contient les paires clé-valeur qui se trouvent dans le dictionnaire.

### Comment Voir Toutes les `clés` Contenues dans un Dictionnaire en Python <a name="clés"></a>

Pour voir toutes les clés qui se trouvent dans un dictionnaire, utilisez la méthode intégrée `keys()` :

```python
année_de_création = {'Python': 1993, 'JavaScript': 1995, 'HTML': 1993}

print(année_de_création.keys())

#sortie

#dict_keys(['Python', 'JavaScript', 'HTML'])
```

La méthode `keys()` retourne une liste qui contient uniquement les clés qui se trouvent dans le dictionnaire.

### Comment Voir Toutes les `valeurs` Contenues dans un Dictionnaire en Python <a name="valeurs"></a>

Pour voir toutes les valeurs qui se trouvent dans un dictionnaire, utilisez la méthode intégrée `values()` :

```python
année_de_création = {'Python': 1993, 'JavaScript': 1995, 'HTML': 1993}

print(année_de_création.values())

#sortie

#dict_values([1993, 1995, 1993])
```

La méthode `values()` retourne une liste qui contient uniquement les valeurs qui se trouvent dans le dictionnaire.

## Comment Accéder aux Éléments Individuels dans un Dictionnaire en Python <a name="accès"></a>

Lorsque vous travaillez avec des listes, vous accédez aux éléments de la liste en mentionnant le nom de la liste et en utilisant la notation entre crochets. Dans les crochets, vous spécifiez le numéro d'index de l'élément (ou sa position).

Vous ne pouvez pas faire exactement la même chose avec les dictionnaires.

Lorsque vous travaillez avec des dictionnaires, vous ne pouvez pas accéder à un élément en référençant son numéro d'index, puisque les dictionnaires contiennent des paires clé-valeur.

Au lieu de cela, vous accédez à l'élément en utilisant le nom du dictionnaire et la notation entre crochets, mais cette fois dans les crochets vous spécifiez une clé.

Chaque clé correspond à une valeur spécifique, donc vous mentionnez la clé qui est associée à la valeur à laquelle vous souhaitez accéder.

La syntaxe générale pour le faire est la suivante :

```python
nom_dictionnaire[clé]
```

Regardons l'exemple suivant sur la façon d'accéder à un élément dans un dictionnaire Python :

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

#accéder à la valeur associée à la clé 'âge'
print(mes_informations['âge'])

#sortie

#28
```

Que se passe-t-il cependant lorsque vous essayez d'accéder à une clé qui n'existe pas dans le dictionnaire ?

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

#essayer d'accéder à la valeur associée à la clé 'emploi'
print(mes_informations['emploi'])

#sortie

#line 4, in <module>
#    print(mes_informations['emploi'])
#KeyError: 'emploi'
```

Cela entraîne une `KeyError` puisque cette clé n'existe pas dans le dictionnaire.

Une façon d'éviter cela est de d'abord rechercher si la clé est dans le dictionnaire.

Vous faites cela en utilisant le mot-clé `in` qui retourne une valeur booléenne. Il retourne `True` si la clé est dans le dictionnaire et `False` si elle ne l'est pas.

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

#rechercher la clé 'emploi'
print('emploi' in mes_informations)

#sortie

#False
```

Une autre façon de contourner cela est d'accéder aux éléments du dictionnaire en utilisant la méthode `get()`.

Vous passez la clé que vous recherchez comme argument et `get()` retourne la valeur qui correspond à cette clé.

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

#essayer d'accéder à la clé 'emploi' en utilisant la méthode get()
print(mes_informations.get('emploi'))

#sortie

#None
```

Comme vous le remarquez, lorsque vous recherchez une clé qui n'existe pas, par défaut `get()` retourne `None` au lieu d'une `KeyError`.

Si, au lieu d'afficher cette valeur `None` par défaut, vous souhaitez afficher un message différent lorsqu'une clé n'existe pas, vous pouvez personnaliser `get()` en fournissant une valeur différente.

Vous faites cela en passant la nouvelle valeur comme second argument optionnel à la méthode `get()` :

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

#essayer d'accéder à la clé 'emploi' en utilisant la méthode get()
print(mes_informations.get('emploi', 'Cette valeur n\'existe pas'))

#sortie

#Cette valeur n'existe pas
```

Maintenant, lorsque vous recherchez une clé et qu'elle n'est pas contenue dans le dictionnaire, vous verrez le message `Cette valeur n'existe pas` apparaître sur la console.

## Comment Modifier un Dictionnaire en Python <a name="modifier"></a>

Les dictionnaires sont *mutables*, ce qui signifie qu'ils sont modifiables.

Ils peuvent croître et décroître tout au long de la vie du programme.

De nouveaux éléments peuvent être ajoutés, des éléments déjà existants peuvent être mis à jour avec de nouvelles valeurs, et des éléments peuvent être supprimés.

### Comment Ajouter de Nouveaux Éléments à un Dictionnaire en Python <a name="ajouter"></a>

Pour ajouter une paire clé-valeur à un dictionnaire, utilisez la notation entre crochets.

La syntaxe générale pour le faire est la suivante :

```python
nom_dictionnaire[clé] = valeur
```

Tout d'abord, spécifiez le nom du dictionnaire. Ensuite, entre crochets, créez une clé et attribuez-lui une valeur.

Supposons que vous commencez avec un dictionnaire vide :

```python
mon_dictionnaire = {}

print(mon_dictionnaire)

#sortie

#{}
```

Voici comment vous ajouteriez une paire clé-valeur à `mon_dictionnaire` :

```python
mon_dictionnaire = {}

#ajouter une paire clé-valeur au dictionnaire vide
mon_dictionnaire['nom'] = "John Doe"

#imprimer le dictionnaire
print(mon_dictionnaire)

#sortie

#{'nom': 'John Doe'}
```

Voici comment vous ajouteriez une autre nouvelle paire clé-valeur :

```python
mon_dictionnaire = {}

#ajouter une paire clé-valeur au dictionnaire vide
mon_dictionnaire['nom'] = "John Doe"

# ajouter une autre paire clé-valeur
mon_dictionnaire['âge'] = 34

#imprimer le dictionnaire
print(mon_dictionnaire)

#sortie

#{'nom': 'John Doe', 'âge': 34}
```

Gardez à l'esprit que si la clé que vous essayez d'ajouter existe déjà dans ce dictionnaire et que vous lui attribuez une valeur différente, la clé finira par être mise à jour.

Rappelez-vous que les clés doivent être uniques.

```python
mon_dictionnaire = {'nom': "John Doe", 'âge':34}

print(mon_dictionnaire)

#essayer de créer une clé 'âge' et lui attribuer une valeur
#la clé 'âge' existe déjà

mon_dictionnaire['âge'] = 46

#la valeur de 'âge' sera maintenant mise à jour

print(mon_dictionnaire)

#sortie

#{'nom': 'John Doe', 'âge': 34}
#{'nom': 'John Doe', 'âge': 46}
```

Si vous souhaitez éviter de changer la valeur d'une clé déjà existante par accident, vous pourriez vouloir vérifier si la clé que vous essayez d'ajouter existe déjà dans le dictionnaire.

Vous faites cela en utilisant le mot-clé `in` comme nous l'avons discuté ci-dessus :

```python
mon_dictionnaire = {'nom': "John Doe", 'âge':34}

#Je veux ajouter une clé `âge`. Avant de le faire, je vérifie si elle existe déjà
print('âge' in mon_dictionnaire)

#sortie

#True
```

### Comment Mettre à Jour les Éléments dans un Dictionnaire en Python <a name="mettre-à-jour"></a>

La mise à jour des éléments dans un dictionnaire fonctionne de manière similaire à l'ajout d'éléments à un dictionnaire.

Lorsque vous savez que vous voulez mettre à jour la valeur d'une clé existante, utilisez la syntaxe générale suivante que vous avez vue dans la section précédente :

```python
nom_dictionnaire[clé_existante] = nouvelle_valeur
```

```python
mon_dictionnaire = {'nom': "John Doe", 'âge':34}

mon_dictionnaire['âge'] = 46

print(mon_dictionnaire)

#sortie

#{'nom': 'John Doe', 'âge': 46}
```

Pour mettre à jour un dictionnaire, vous pouvez également utiliser la méthode intégrée `update()`.

Cette méthode est particulièrement utile lorsque vous souhaitez mettre à jour plus d'une valeur à l'intérieur d'un dictionnaire en même temps.

Supposons que vous souhaitez mettre à jour la clé `nom` et `âge` dans `mon_dictionnaire`, et ajouter une nouvelle clé, `profession` :

```python
mon_dictionnaire = {'nom': "John Doe", 'âge':34}

mon_dictionnaire.update(nom='Mike Green', âge=46, profession="développeur logiciel")

print(mon_dictionnaire)

#sortie

#{'nom': 'Mike Green', 'âge': 46, 'profession': 'développeur logiciel'}
```

La méthode `update()` prend un tuple de paires clé-valeur.

Les clés qui existaient déjà ont été mises à jour avec les nouvelles valeurs qui leur ont été attribuées, et une nouvelle paire clé-valeur a été ajoutée.

La méthode `update()` est également utile lorsque vous souhaitez ajouter le contenu d'un dictionnaire dans un autre.

Supposons que vous avez un dictionnaire, `nombres`, et un deuxième dictionnaire, `plus_de_nombres`.

Si vous souhaitez fusionner le contenu de `plus_de_nombres` avec le contenu de `nombres`, utilisez la méthode `update()`.

Toutes les paires clé-valeur contenues dans `plus_de_nombres` seront ajoutées à la fin du dictionnaire `nombres`.

```python
nombres = {'un': 1, 'deux': 2, 'trois': 3}
plus_de_nombres = {'quatre': 4, 'cinq': 5, 'six': 6}

#mettre à jour le dictionnaire 'nombres'
#vous le mettez à jour en ajoutant le contenu d'un autre dictionnaire, 'plus_de_nombres',
#à la fin de celui-ci
nombres.update(plus_de_nombres)

print(nombres)

#sortie

#{'un': 1, 'deux': 2, 'trois': 3, 'quatre': 4, 'cinq': 5, 'six': 6}
```

### Comment Supprimer des Éléments d'un Dictionnaire en Python <a name="supprimer"></a>

L'une des façons de supprimer une clé spécifique et sa valeur associée d'un dictionnaire est d'utiliser le mot-clé `del`.

La syntaxe pour le faire est la suivante :

```python
del nom_dictionnaire[clé]
```

Par exemple, voici comment vous supprimeriez la clé `emplacement` du dictionnaire `mes_informations` :

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

del mes_informations['emplacement']

print(mes_informations)

#sortie

#{'nom': 'Dionysia', 'âge': 28}
```

Si vous souhaitez supprimer une clé, mais que vous souhaitez également sauvegarder cette valeur supprimée, utilisez la méthode intégrée `pop()`.

La méthode `pop()` supprime mais retourne également la clé que vous spécifiez. De cette façon, vous pouvez stocker la valeur supprimée dans une variable pour une utilisation ou une récupération ultérieure.

Vous passez la clé que vous souhaitez supprimer comme argument à la méthode.

Voici la syntaxe générale pour le faire :

```python
nom_dictionnaire.pop(clé)
```

Pour supprimer la clé `emplacement` de l'exemple ci-dessus, mais cette fois en utilisant la méthode `pop()` et en sauvegardant la valeur associée à la clé dans une variable, faites ce qui suit :

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

ville = mes_informations.pop('emplacement')

print(mes_informations)
print(ville)

#sortie

#{'nom': 'Dionysia', 'âge': 28}
#Athènes
```

Si vous spécifiez une clé qui n'existe pas dans le dictionnaire, vous obtiendrez un message d'erreur `KeyError` :

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

mes_informations.pop('profession')

print(mes_informations)

#sortie

#line 3, in <module>
#   mes_informations.pop('profession')
#KeyError: 'profession'
```

Une façon de contourner cela est de passer un deuxième argument à la méthode `pop()`.

En incluant le deuxième argument, il n'y aurait pas d'erreur. Au lieu de cela, il y aurait un échec silencieux si la clé n'existait pas, et le dictionnaire resterait inchangé.

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

mes_informations.pop('profession','Non trouvé')

print(mes_informations)

#sortie

#{'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}
```

La méthode `pop()` supprime une clé spécifique et sa valeur associée – mais que faire si vous souhaitez uniquement supprimer la **dernière** paire clé-valeur d'un dictionnaire ?

Pour cela, utilisez plutôt la méthode intégrée `popitem()`.

Voici la syntaxe générale de la méthode `popitem()` :

```python
nom_dictionnaire.popitem()
```

La méthode `popitem()` ne prend aucun argument, mais supprime et retourne la dernière paire clé-valeur d'un dictionnaire.

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

élément_supprimé = mes_informations.popitem()

print(mes_informations)
print(élément_supprimé)

#sortie

#{'nom': 'Dionysia', 'âge': 28}
#('emplacement', 'Athènes')
```

Enfin, si vous souhaitez supprimer toutes les paires clé-valeur d'un dictionnaire, utilisez la méthode intégrée `clear()`.

```python
mes_informations = {'nom': 'Dionysia', 'âge': 28, 'emplacement': 'Athènes'}

mes_informations.clear()

print(mes_informations)

#sortie

#{}
```

L'utilisation de cette méthode vous laissera avec un dictionnaire vide.

## Conclusion

Et voilà ! Vous connaissez maintenant les bases des dictionnaires en Python.

J'espère que vous avez trouvé cet article utile.

Pour en savoir plus sur le langage de programmation Python, consultez la [Certification en Calcul Scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) de freeCodeCamp.

Vous commencerez par les bases et apprendrez de manière interactive et adaptée aux débutants. Vous construirez également cinq projets à la fin pour mettre en pratique et renforcer ce que vous avez appris.

Merci d'avoir lu et bon codage !