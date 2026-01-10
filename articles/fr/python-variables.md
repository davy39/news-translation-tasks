---
title: Variables Python – Le guide complet pour débutants
subtitle: ''
author: Reed
co_authors: []
series: null
date: '2023-03-22T18:30:52.000Z'
originalURL: https://freecodecamp.org/news/python-variables
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/mugshotbot.com_customize_color-yellow-image-9820e115-mode-light-pattern-texture-theme-two_up-url-https___gifcoins.io.png
tags:
- name: Python
  slug: python
- name: variables
  slug: variables
seo_title: Variables Python – Le guide complet pour débutants
seo_desc: 'Variables are an essential part of Python. They allow us to easily store,
  manipulate, and reference data throughout our projects.

  This article will give you all the understanding of Python variables you need to
  use them effectively in your projects.

  ...'
---

Les variables sont une partie essentielle de Python. Elles nous permettent de stocker, manipuler et référencer facilement des données tout au long de nos projets.

Cet article vous apportera toute la compréhension des variables Python dont vous avez besoin pour les utiliser efficacement dans vos projets.

Si vous souhaitez disposer du moyen le plus pratique pour revoir tous les sujets abordés ici, j'ai préparé une antisèche utile pour vous juste ici :

**[Téléchargez l'](https://reedbarger.com/resources/python-variables)** antisèche sur les variables Python (cela prend 5 secondes).

## Qu'est-ce qu'une variable en Python ?

Alors, que sont les variables et pourquoi en avons-nous besoin ?

Les variables sont essentielles pour conserver et référencer des valeurs tout au long de notre application. En stockant une valeur dans une variable, vous pouvez la réutiliser autant de fois et de la manière que vous le souhaitez dans votre projet.

Vous pouvez considérer les variables comme des boîtes avec des étiquettes, où l'étiquette représente le nom de la variable et le contenu de la boîte est la valeur que la variable contient.

En Python, les variables sont créées au moment où vous leur donnez ou **assignez** une valeur.

## Comment assigner une valeur à une variable ?

Assigner une valeur à une variable en Python est un processus facile.

Vous utilisez simplement le signe égal `=` comme opérateur d'assignation, suivi de la valeur que vous souhaitez affecter à la variable. Voici un exemple :

```python
country = "United States"
year_founded = 1776
```

Dans cet exemple, nous avons créé deux variables : `country` et `year_founded`. Nous avons assigné la valeur de type chaîne de caractères "United States" à la variable `country` et la valeur entière 1776 à la variable `year_founded`.

Il y a deux choses à noter dans cet exemple :

1. Les variables en Python sont **sensibles à la casse**. En d'autres termes, faites attention à la casse lors de la création de variables, car `Year_Founded` sera une variable différente de `year_founded`, même si elles contiennent les mêmes lettres.
2. Les noms de variables utilisant plusieurs mots en Python doivent être séparés par un tiret bas `_`. Par exemple, une variable nommée "site name" doit être écrite "site_name". Cette convention est appelée **snake case** (très approprié pour le langage "Python").

## Comment devrais-je nommer mes variables Python ?

Il y a quelques règles à suivre lors du nommage des variables Python.

Certaines sont des règles strictes qui doivent être respectées, sinon votre programme ne fonctionnera pas, tandis que d'autres sont connues sous le nom de **conventions**. Cela signifie qu'il s'agit plutôt de suggestions.

### Règles de nommage des variables

1. Les noms de variables doivent commencer par une lettre ou le caractère de soulignement `_`.
2. Les noms de variables ne peuvent contenir que des lettres, des chiffres et des tirets bas.
3. Les noms de variables ne peuvent pas contenir d'espaces ou de caractères spéciaux.

```python
user_age = 20 # valide

website = 'https://freecodecamp.org' # valide

1password = True # invalide
```

### Conventions de nommage des variables

1. Les noms de variables doivent être descriptifs et ne pas être trop courts ou trop longs.
2. Utilisez des lettres minuscules et des tirets bas pour séparer les mots dans les noms de variables (connu sous le nom de "snake_case").

## Quels types de données les variables Python peuvent-elles contenir ?

L'une des meilleures caractéristiques de Python est sa flexibilité en ce qui concerne la gestion de divers types de données.

Les variables Python peuvent contenir divers types de données, notamment des entiers, des nombres à virgule flottante (floats), des chaînes de caractères, des booléens, des tuples et des listes :

**Les entiers (Integers)** sont des nombres entiers, positifs ou négatifs.

```python
answer = 42
```

**Les nombres à virgule flottante (Floats)** sont des nombres réels ou des nombres avec un point décimal.

```python
weight = 34.592
```

**Les chaînes de caractères (Strings)** sont des séquences de caractères, à savoir des mots ou des phrases.

```python
message = "Hello Python"
```

**Les booléens (Booleans)** sont des valeurs Vrai (True) ou Faux (False).

```python
is_authenticated = True

```

**Les listes** sont des collections de valeurs ordonnées et mutables.

```python
fruits = ['apple', 'banana', 'cherry']
```

**Les tuples** sont des collections de valeurs ordonnées et immuables.

```python
point = (3, 4)

```

Il existe d'autres types de données en Python, mais ce sont les plus courants que vous rencontrerez en travaillant avec des variables Python.

## Python est un langage à typage dynamique

Python est ce qu'on appelle un langage à **typage dynamique**. Cela signifie que le type d'une variable peut changer pendant l'exécution d'un programme.

Une autre caractéristique du typage dynamique est qu'il n'est pas nécessaire de déclarer manuellement le type de chaque variable, contrairement à d'autres langages de programmation comme Java.

Vous pouvez utiliser la fonction `type()` pour déterminer le type d'une variable. Par exemple :

```python
print(type(answer))  # Sortie : <class 'int'>
print(type(message))  # Sortie : <class 'str'>

```

## Quelles opérations peuvent être effectuées ?

Les variables peuvent être utilisées dans diverses opérations, ce qui nous permet de les transformer mathématiquement (s'il s'agit de nombres), de modifier leurs valeurs de chaîne par des opérations comme la concaténation, et de comparer les valeurs à l'aide d'opérateurs d'égalité.

### Opérations mathématiques

Il est possible d'effectuer des opérations mathématiques de base avec des variables, telles que l'addition, la soustraction, la multiplication et la division :

```python
# Opérations arithmétiques
a = 10
b = 5

sum = a + b
difference = a - b
product = a * b
quotient = a / b

print(sum, difference, product, quotient)  # Sortie : 15 5 50 2.0
```

Il est également possible de trouver le reste d'une opération de division en utilisant l'opérateur modulo `%` ainsi que de créer des exposants en utilisant la syntaxe `**` :

```python
# Opération modulo
remainder = a % b
print(remainder)  # Sortie : 0

# Exponentiation
power = a ** b
print(power)  # Sortie : 100000
```

### Opérateurs de chaînes de caractères

Les chaînes de caractères peuvent être ajoutées les unes aux autres ou **concaténées** en utilisant l'opérateur `+`.

```python
# Concaténation de chaînes
first_name = "Guido"
last_name = "van Rossum"
full_name = first_name + " " + last_name
print(full_name)  # Sortie : Guido van Rossum
```

### Comparaisons d'égalité

Les valeurs peuvent également être comparées en Python en utilisant les opérateurs `<`, `>`, `==` et `!=`.

Ces opérateurs comparent respectivement si les valeurs sont inférieures à, supérieures à, égales à ou non égales les unes aux autres.

```python
# Opérations de comparaison
x = 15
y = 20

print(x < y)  # Sortie : True
print(x > y)  # Sortie : False
print(x == y)  # Sortie : False
print(x != y)  # Sortie : True
```

Enfin, notez que lors de l'exécution d'opérations avec des variables, vous devez vous assurer que les types des variables sont compatibles entre eux.

Par exemple, vous ne pouvez pas ajouter directement une chaîne de caractères et un entier. Vous devrez convertir l'une des variables en un type compatible à l'aide d'une fonction comme `str()` ou `[int()](https://www.freecodecamp.org/news/python-string-to-int-convert-a-string-example/)`.

## Portée des variables

La portée d'une variable fait référence aux parties d'un programme où la variable peut être consultée et modifiée. En Python, il existe deux types principaux de portée de variable :

**Portée globale** : Les variables définies en dehors de toute fonction ou classe ont une portée globale. Elles peuvent être consultées et modifiées tout au long du programme, y compris à l'intérieur des fonctions et des classes.

```python
global_var = "Je suis une variable globale"

def access_global_var():
    print(global_var)

access_global_var()  # Sortie : Je suis une variable globale

```

**Portée locale** : Les variables définies à l'intérieur d'une fonction ou d'une classe ont une portée locale. Elles ne peuvent être consultées et modifiées qu'à l'intérieur de cette fonction ou de cette classe.

```python
def function_with_local_var():
    local_var = "Je suis une variable locale"
    print(local_var)

function_with_local_var()  # Sortie : Je suis une variable locale
print(local_var)  # Erreur : NameError: name 'local_var' is not defined

```

Dans cet exemple, tenter d'accéder à `local_var` en dehors de la fonction `function_with_local_var` entraîne une erreur `NameError`, car la variable n'est pas définie dans la portée globale.

## Conclusion

N'ayez pas peur d'expérimenter différents types de variables, d'opérations et de portées pour vraiment saisir leur importance et leur fonctionnalité. Plus vous travaillerez avec les variables Python, plus vous serez confiant dans l'application de ces concepts.

Enfin, si vous voulez apprendre pleinement tous ces concepts, j'ai préparé pour vous une antisèche super utile qui résume tout ce que nous avons couvert ici.

Cliquez simplement sur le lien ci-dessous pour la récupérer gratuitement. Bonne lecture !

**[Téléchargez l'](https://reedbarger.com/resources/python-variables)** antisèche sur les variables Python

## Devenez un développeur React professionnel

React est difficile. Vous ne devriez pas avoir à le comprendre tout seul.

J'ai mis tout ce que je sais sur React dans un seul cours, pour vous aider à atteindre vos objectifs en un temps record :

[**Présentation de : The React Bootcamp**](https://www.thereactbootcamp.com)

**C’est le cours que j’aurais aimé avoir quand j’ai commencé à apprendre React.**

Cliquez ci-dessous pour essayer le React Bootcamp par vous-même :

[![Cliquez pour rejoindre le React Bootcamp](https://reedbarger.nyc3.digitaloceanspaces.com/reactbootcamp/react-bootcamp-cta-alt.png)](https://www.thereactbootcamp.com)
*Cliquez pour commencer*