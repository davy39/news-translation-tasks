---
title: 'Dictionnaires Python 101 : Une Introduction Visuelle Détaillée'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2019-12-30T00:19:00.000Z'
originalURL: https://freecodecamp.org/news/python-dictionaries-detailed-visual-introduction
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/Dictionaries-2.png
tags:
- name: data structures
  slug: data-structures
- name: dictionary
  slug: dictionary
- name: learning to code
  slug: learning-to-code
- name: Python
  slug: python
seo_title: 'Dictionnaires Python 101 : Une Introduction Visuelle Détaillée'
seo_desc: 'Welcome

  In this article, you will learn how to work with Python dictionaries, an incredibly
  helpful built-in data type that you will definitely use in your projects.

  In particular, you will learn:


  What dictionaries are used for and their main charac...'
---

## Bienvenue

Dans cet article, vous apprendrez à travailler avec les dictionnaires Python, un type de données intégré incroyablement utile que vous utiliserez définitivement dans vos projets.

**En particulier, vous apprendrez :**

* À quoi servent les dictionnaires et quelles sont leurs principales caractéristiques.
* Pourquoi ils sont importants pour vos projets de programmation.
* L'"anatomie" d'un dictionnaire : clés, valeurs et paires clé-valeur.
* Les règles spécifiques qui déterminent si une valeur peut être une clé.
* Comment accéder, ajouter, modifier et supprimer des paires clé-valeur.
* Comment vérifier si une clé est dans un dictionnaire.
* Ce que représente la longueur d'un dictionnaire.
* Comment itérer sur les dictionnaires en utilisant des boucles for.
* Quelles méthodes de dictionnaire intégrées vous pouvez utiliser pour exploiter la puissance de ce type de données.

À la fin de cet article, nous plongerons dans un projet simple pour appliquer vos connaissances : nous écrivons une fonction qui crée et retourne un dictionnaire avec un but particulier.

**Commençons ! f380fe0f**

## f4e5 Dictionnaires en Contexte

Commençons par discuter de l'importance des dictionnaires. Pour illustrer cela, laissez-moi faire une comparaison rapide avec un autre type de données que vous connaissez probablement : les listes.

Lorsque vous travaillez avec des listes en Python, vous pouvez accéder à un élément en utilisant un index, un **entier** qui décrit la position de l'élément dans la liste. Les indices commencent à zéro pour le premier élément et augmentent de un pour chaque élément suivant dans la liste. Vous pouvez voir un exemple juste ici :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-51.png)

**Mais que faire si nous devons stocker deux valeurs liées et garder cette "connexion" dans notre code ?** Pour l'instant, nous n'avons que des valeurs uniques et indépendantes stockées dans une liste.

Disons que nous voulons stocker les noms des étudiants et "connecter" chaque nom avec les notes de chaque étudiant particulier. Nous voulons garder la "connexion" entre eux. Comment feriez-vous cela en Python ?

Si vous utilisez des listes imbriquées, les choses deviendraient très complexes et inefficaces après avoir ajouté seulement quelques éléments car vous devriez utiliser deux indices ou plus pour accéder à chaque valeur, selon la liste finale. **C'est là que les dictionnaires Python viennent à la rescousse.** 

### Rencontrez les Dictionnaires

Un dictionnaire Python ressemble à ceci (voir ci-dessous). Avec un dictionnaire, vous pouvez "connecter" une valeur à une autre valeur pour représenter la relation entre elles dans votre code. Dans cet exemple, "Gino" est "connecté" à l'entier 15 et la chaîne "Nora" est "connectée" à l'entier 30.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-48.png)

Regardons les différents éléments qui composent un dictionnaire.

## f4e4 L'"Anatomie" d'un Dictionnaire Python

Puisqu'un dictionnaire "connecte" deux valeurs, il a deux types d'éléments :

* **Clés** : une clé est une valeur utilisée pour accéder à une autre valeur. Les clés sont l'équivalent des "indices" dans les chaînes, les listes et les tuples. Dans les dictionnaires, pour accéder à une valeur, vous utilisez la clé, qui est une valeur elle-même. 
* **Valeurs** : ce sont les valeurs auxquelles vous pouvez accéder avec leur clé correspondante. 

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-96.png)

Ces deux éléments forment ce qu'on appelle une **paire clé-valeur** (une clé avec sa valeur correspondante).

### Syntaxe

Voici un exemple de dictionnaire Python associant la chaîne "Gino" au nombre 15 et la chaîne "Nora" au nombre 30 :

```python
>>> {"Gino": 15, "Nora": 30}
```

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-49.png)

* Pour créer un dictionnaire, nous utilisons des **accolades `{ }`** .
* Entre ces accolades, nous écrivons des paires clé-valeur séparées par une virgule. 
* Pour les paires clé-valeur, nous écrivons la clé suivie de deux points, d'un espace et de la valeur qui correspond à la clé.

f4a1 **Conseils :** 

* Pour des raisons de lisibilité et de style, il est recommandé d'ajouter un espace après chaque virgule pour séparer les paires clé-valeur.
* Vous pouvez créer un dictionnaire vide avec une paire d'accolades vides `{}`.

### Règles Importantes pour les Clés

Toutes les valeurs ne peuvent pas être des clés dans un dictionnaire Python. Les clés doivent suivre un ensemble de règles :

Selon la [Documentation Python](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) :

* Les clés doivent être uniques dans un dictionnaire.

> Il est préférable de penser à un dictionnaire comme un ensemble de paires _clé: valeur_, avec l'exigence que les clés soient **uniques** (dans un dictionnaire).

* Les clés doivent être immuables. 

> Contrairement aux séquences, qui sont indexées par une plage de nombres, les dictionnaires sont indexés par des _clés_, qui peuvent être de n'importe quel type **immuable** ; les chaînes et les nombres peuvent toujours être des clés.

* Si la clé est un tuple, il ne peut contenir que des chaînes, des nombres ou des tuples. 

> Les tuples peuvent être utilisés comme clés s'ils ne contiennent que des chaînes, des nombres ou des tuples ; si un tuple contient un objet mutable directement ou indirectement, il ne peut pas être utilisé comme clé.

* Les listes ne peuvent pas être des clés car elles sont mutables. Cela est une conséquence de la règle précédente. 

> Vous ne pouvez pas utiliser les listes comme clés, puisque les listes peuvent être modifiées en place en utilisant des affectations d'index, des affectations de tranches ou des méthodes comme `append()` et `extend()`.

f4a1 **Note :** Les valeurs n'ont pas de règles spécifiques, elles peuvent être des valeurs mutables ou immuables.  

## f4e5 Dictionnaires en Action

Maintenant, voyons comment nous pouvons travailler avec les dictionnaires en Python. Nous allons accéder, ajouter, modifier et supprimer des paires clé-valeur. 

Nous allons commencer à travailler avec ce dictionnaire, assigné à la variable `ages` :

```python
>>> ages = {"Gino": 15, "Nora": 30}
```

### Accéder aux Valeurs en utilisant les Clés

Si nous devons accéder à la valeur associée à une clé spécifique, nous écrivons le nom de la variable qui référence le dictionnaire suivi de crochets `[]` et, entre les crochets, la clé qui correspond à la valeur :

```
<variable>[<key>]
```

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-52.png)

Voici un exemple de la façon dont nous pouvons accéder à la valeur qui correspond à la chaîne `"Gino"` :

```python
>>> ages = {"Gino": 15, "Nora": 30}
>>> ages["Gino"]
15
```

Remarquez que la syntaxe est très similaire à l'indexation d'une chaîne, d'un tuple ou d'une liste, mais maintenant nous utilisons la clé comme index au lieu d'un entier.

Si nous voulons accéder à la valeur qui correspond à "Nora", nous ferions ceci :

```python
>>> ages = {"Gino": 15, "Nora": 30}
>>> ages["Nora"]
30
```

f4a1 **Conseil :** Si vous essayez d'accéder à une clé qui n'existe pas dans le dictionnaire, vous obtiendrez une `KeyError` :

```python
>>> ages = {"Gino": 15, "Nora": 30}
>>> ages["Talina"]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    ages["Talina"]
KeyError: 'Talina'
```

### Ajouter des Paires Clé-Valeur

Si une paire clé-valeur n'existe pas dans le dictionnaire, nous pouvons l'ajouter. Pour ce faire, nous écrivons la variable qui référence le dictionnaire suivie de la clé entre crochets, d'un signe égal et de la nouvelle valeur :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-53.png)

Voici un exemple dans IDLE :

```python
>>> ages = {"Gino": 15, "Nora": 30}

# Ajouter la paire clé-valeur "Talina": 24
>>> ages["Talina"] = 24

# Le dictionnaire contient maintenant cette paire clé-valeur
>>> ages
{'Gino': 15, 'Nora': 30, 'Talina': 24}
```

### Modifier une Paire Clé-Valeur

Pour modifier la valeur associée à une clé spécifique, nous utilisons la même syntaxe que celle utilisée pour ajouter une nouvelle paire clé-valeur, mais maintenant nous allons assigner la nouvelle valeur à une clé existante :

```python
>>> ages = {"Gino": 15, "Nora": 30}

# La clé "Gino" existe déjà dans le dictionnaire, donc sa valeur associée
# sera mise à jour à 45.
>>> ages["Gino"] = 45

# La valeur a été mise à jour à 45.
>>> ages
{'Gino': 45, 'Nora': 30}
```

### Supprimer une Paire Clé-Valeur

Pour supprimer une paire clé-valeur, vous utiliseriez le mot-clé `del` suivi du nom de la variable qui référence le dictionnaire et, entre crochets `[]`, la clé de la paire clé-valeur :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-55.png)

Voici un exemple dans IDLE :

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}

# Supprimer la paire clé-valeur "Gino": 15.
>>> del ages["Gino"]

# La paire clé-valeur a été supprimée.
>>> ages
{'Nora': 30, 'Talina': 45}
```

## f4e4 Vérifier si une Clé est dans un Dictionnaire

Parfois, il peut être très utile de vérifier si une clé existe déjà dans un dictionnaire (rappelons que les clés doivent être uniques).

Selon la [Documentation Python](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) :

> Pour vérifier si une seule **clé** est dans le dictionnaire, utilisez le mot-clé [`in`](https://docs.python.org/3/reference/expressions.html#in).

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> "Talina" in ages
True
>>> "Gino" in ages
True
>>> "Lulu" in ages
False
```

L'opérateur `in` vérifie les clés, pas les valeurs. Si nous écrivons ceci :

```python
>>> 15 in ages
False
```

Nous vérifions si la **_clé_** 15 est dans le dictionnaire, pas la valeur. C'est pourquoi l'expression est évaluée à `False`.

f4a1 **Conseil :** Vous pouvez utiliser l'opérateur `in` pour vérifier si une valeur est dans un dictionnaire avec <dict>[.values()](https://docs.python.org/3/library/stdtypes.html#dict.values).

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> 30 in ages.values()
True
>>> 10 in ages.values()
False
```

## f4e5 Longueur d'un Dictionnaire Python

La longueur d'un dictionnaire est le nombre de paires clé-valeur qu'il contient. Vous pouvez vérifier la longueur d'un dictionnaire avec la fonction [len()](https://docs.python.org/3/library/functions.html#len) que nous utilisons couramment, tout comme nous vérifions la longueur des listes, des tuples et des chaînes :

```
# Deux paires clé-valeur. Longueur 2.
>>> ages = {"Gino": 15, "Nora": 30}
>>> len(ages)
2

# Trois paires clé-valeur. Longueur 3.
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> len(ages)
3
```

## f4e4 Itérer sur les Dictionnaires en Python

Vous pouvez itérer sur les dictionnaires en utilisant une boucle for. Il existe diverses approches pour le faire et elles sont toutes également pertinentes. Vous devriez choisir l'approche qui fonctionne le mieux pour vous, en fonction de ce que vous essayez d'accomplir.

### Première Option - Itérer sur les Clés

Nous pouvons itérer sur les clés d'un dictionnaire comme ceci :

```
for <key> in <dictionary>:
	# Faire ceci
```

Par exemple :

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> for student in ages:
	print(student)
    
Gino
Nora
Talina
```

### Deuxième Option - Itérer sur les Paires Clé-Valeur

Pour ce faire, nous devons utiliser la méthode intégrée [.items()](https://docs.python.org/3/library/stdtypes.html#dict.items), qui nous permet d'itérer sur les paires clé-valeur sous forme de tuples de ce format `(key, value)`. 

```
for <key-value-pair-as-tuple> in <dictionary>.items():
	# Faire ceci
```

Par exemple :

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}

>>> for pair in ages.items():
	print(pair)
	
('Gino', 15)
('Nora', 30)
('Talina', 45)
```

### Troisième Option - Assigner les Clés et les Valeurs à des Variables Individuelles

Avec [.items()](https://docs.python.org/3/library/stdtypes.html#dict.items) et les boucles for, vous pouvez utiliser la puissance d'une affectation de tuple pour assigner directement les clés et les valeurs à des variables individuelles que vous pouvez utiliser dans la boucle :

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}

# Affectation de tuple pour assigner la clé à la variable key 
# et la valeur à la variable value.
>>> for key, value in ages.items():
	print("Clé:", key, "; Valeur:", value)

	
Clé: Gino ; Valeur: 15
Clé: Nora ; Valeur: 30
Clé: Talina ; Valeur: 45
```

### Quatrième Option - Itérer sur les Valeurs

Vous pouvez itérer sur les valeurs d'un dictionnaire en utilisant la méthode [.values()](https://docs.python.org/3/library/stdtypes.html#dict.values).

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> for age in ages.values():
	print(age)

15
30
45
```

## f4e5 Méthodes des Dictionnaires

Les dictionnaires incluent des méthodes intégrées très utiles qui peuvent vous faire gagner du temps et du travail pour effectuer des fonctionnalités courantes :

### .clear()

Cette méthode supprime toutes les paires clé-valeur du dictionnaire.

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> ages.clear()
>>> ages
{}
```

### .get(<key>, <default>)

Cette méthode retourne la valeur associée à la clé. Sinon, elle retourne la valeur par défaut qui a été fournie comme deuxième argument (ce deuxième argument est facultatif).

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> ages.get("Nora")
30
>>> ages.get("Nor", "Non Trouvé")
'Non Trouvé'
```

Si vous n'ajoutez pas de deuxième argument, cela est équivalent à la syntaxe précédente avec des crochets `[]` que vous avez apprise :

```
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> ages["Nora"]
30
>>> ages.get("Nora")
30
```

### .pop(<key>, <default>)

Cette méthode supprime la paire clé-valeur du dictionnaire et retourne la valeur. 

```python
>>> ages = {"Gino": 15, "Nora": 30, "Talina": 45}
>>> ages.pop("Talina")
45
>>> ages
{'Gino': 15, 'Nora': 30}
```

### .update(<other>)

Cette méthode remplace les valeurs d'un dictionnaire par les valeurs d'un autre dictionnaire uniquement pour les clés qui existent dans les deux dictionnaires. 

Un exemple de cela serait un dictionnaire avec les notes originales de trois étudiants (voir le code ci-dessous). Nous voulons seulement remplacer les notes des étudiants qui ont passé l'examen de rattrapage (dans ce cas, un seul étudiant a passé l'examen de rattrapage, donc les autres notes doivent rester inchangées). 

```
>>> grades = {"Gino": 0, "Nora": 98, "Talina": 99}
>>> new_grades = {"Gino": 67}
>>> grades.update(new_grades)
>>> grades
{'Gino': 67, 'Nora': 98, 'Talina': 99}
```

En utilisant la méthode .update(), nous avons pu mettre à jour la valeur associée à la chaîne "Gino" dans le dictionnaire original puisque c'est la seule clé commune dans les deux dictionnaires. 

La valeur originale serait remplacée par la valeur associée à cette clé dans le dictionnaire qui a été passé comme argument à .update().

f4a1 **Conseils :** Pour en savoir plus sur les méthodes des dictionnaires, je recommande de lire [cet article dans la Documentation Python](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict).

## f4e5 Mini Projet - Un Dictionnaire de Fréquences

Maintenant, vous allez appliquer vos connaissances en écrivant une fonction `freq_dict` qui crée et retourne un dictionnaire avec la fréquence de chaque élément d'une liste, d'une chaîne ou d'un tuple (le nombre de fois où l'élément apparaît). Les éléments seront les clés et les fréquences seront les valeurs. 

### Code

Nous allons écrire la fonction étape par étape pour voir la logique derrière chaque ligne de code.

* **Étape 1 :** La première chose que nous devons faire est d'écrire l'en-tête de la fonction. Remarquez que cette fonction ne prend qu'un seul argument, la liste, la chaîne ou le tuple, que nous appelons `data`.

```python
def freq_dict(data):
```

* **Étape 2 :** Ensuite, nous devons créer un dictionnaire vide qui mappera chaque élément de la liste, de la chaîne ou du tuple à sa fréquence correspondante.

```python
def freq_dict(data):
	freq = {}
```

* **Étape 3 :** Ensuite, nous devons itérer sur la liste, la chaîne ou le tuple pour déterminer quoi faire avec chaque élément. 

```python
def freq_dict(data):
	freq = {}
	for elem in data: 
```

* **Étape 4 :** Si l'élément a déjà été inclus dans le dictionnaire, alors l'élément apparaît plus d'une fois et nous devons ajouter 1 à sa fréquence actuelle. Sinon, si l'élément n'est pas déjà dans le dictionnaire, c'est la première fois qu'il apparaît et sa valeur initiale doit être 1. 

```python
def freq_dict(data):
	freq = {}
	for elem in data:
		if elem in freq:
			freq[elem] += 1
		else:
			freq[elem] = 1
```

* **Étape 5 :** Enfin, nous devons retourner le dictionnaire.

```python
def freq_dict(data):
	freq = {}
	for elem in data:
		if elem in freq:
			freq[elem] += 1
		else:
			freq[elem] = 1
	return freq
```

f4a1 **Important :** Puisque nous assignons les éléments comme clés du dictionnaire, ils doivent être d'un type de données immuable.

### Exemples

Voici un exemple de l'utilisation de cette fonction. Remarquez comment le dictionnaire mappe chaque caractère de la chaîne au nombre de fois où il apparaît. 

```python
>>> def freq_dict(data):
	freq = {}
	for elem in data:
		if elem in freq:
			freq[elem] += 1
		else:
			freq[elem] = 1
	return freq

>>> freq_dict("Hello, how are you?")
{'H': 1, 'e': 2, 'l': 2, 'o': 3, ',': 1, ' ': 3, 'h': 1, 'w': 1, 'a': 1, 'r': 1, 'y': 1, 'u': 1, '?': 1}
```

Voici un autre exemple appliqué à une liste d'entiers :

```python
>>> def freq_dict(data):
	freq = {}
	for elem in data:
		if elem in freq:
			freq[elem] += 1
		else:
			freq[elem] = 1
	return freq

>>> freq_dict([5, 2, 6, 2, 6, 5, 2, 2, 2])
{5: 2, 2: 5, 6: 2}
```

Excellent travail ! Maintenant nous avons la fonction finale. 

## f4e5 En Résumé 

* Les dictionnaires sont des types de données intégrés en Python qui associent (mappent) des clés à des valeurs, formant des paires clé-valeur.
* Vous pouvez accéder à une valeur avec sa clé correspondante.  
* Les clés doivent être d'un type de données immuable.
* Vous pouvez accéder, ajouter, modifier et supprimer des paires clé-valeur. 
* Les dictionnaires offrent une grande variété de méthodes qui peuvent vous aider à effectuer des fonctionnalités courantes.

**J'espère vraiment que vous avez aimé mon article et que vous l'avez trouvé utile.** Maintenant vous pouvez travailler avec des dictionnaires dans vos projets Python. [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Suivez-moi sur [Twitter](https://twitter.com/EstefaniaCassN). f380fe0f