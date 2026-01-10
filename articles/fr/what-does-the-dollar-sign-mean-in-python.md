---
title: Que signifie $ en Python ? Signification de l'opérateur + exemples de formatage
  de chaînes
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-04-18T16:39:34.000Z'
originalURL: https://freecodecamp.org/news/what-does-the-dollar-sign-mean-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/what-does-the-dollar-sign-mean-in-python.png
tags:
- name: Python
  slug: python
seo_title: Que signifie $ en Python ? Signification de l'opérateur + exemples de formatage
  de chaînes
seo_desc: "Operators are special symbols you can use to perform different operations\
  \ on variables (operands) in programming. \nPython has different operators like\
  \ arithmetic operators, assignment operators, logical operators, boolean operators,\
  \ comparison operat..."
---

Les opérateurs sont des symboles spéciaux que vous pouvez utiliser pour effectuer différentes opérations sur des variables (opérandes) en programmation. 

Python dispose de différents opérateurs comme les opérateurs arithmétiques, les opérateurs d'affectation, les opérateurs logiques, les opérateurs booléens, les opérateurs de comparaison, les opérateurs bit à bit, et ainsi de suite. 

Bien que vous ne rencontrerez pas l'opérateur symbole dollar ($) lorsque vous apprendrez les opérateurs en Python, vous pouvez l'utiliser pour formater des chaînes en utilisant la classe de modèle de chaîne.

Dans cet article, vous apprendrez comment formater des chaînes en Python en utilisant les méthodes suivantes :

* La classe de modèle de chaîne.
* L'opérateur `%`.
* La méthode `format()`.
* Utilisation des f-strings. 

## Comment formater des chaînes en Python en utilisant la classe de modèle de chaîne

La classe de modèle de chaîne en Python vous permet de substituer ou d'injecter des valeurs de variables dans des chaînes. 

Pour utiliser la classe de modèle, vous devez d'abord l'importer depuis le module `string`. C'est-à-dire :

```python
from string import Template
```

Voici comment l'utiliser pour formater des chaînes : 

```python
from string import Template

template_string = Template("Mon nom est $name ! Je crée du contenu sur $language")

output = template_string.substitute(name="Ihechikara", language="Python")

print(output) # Mon nom est Ihechikara ! Je crée du contenu sur Python
```

Dans l'exemple ci-dessus, nous avons créé une variable appelée `template_string` pour contenir la chaîne : "Mon nom est $name ! Je crée du contenu sur $language". 

La chaîne a été passée en tant que paramètre à la classe de modèle : `Template("Mon nom est $name ! Je crée du contenu sur $language")`. 

Vous remarquerez que, dans la chaîne, certains caractères ont l'opérateur `$` avant eux — `$name` et `$language`. Ce sont des espaces réservés qui peuvent être assignés à des valeurs. 

Dans la ligne suivante, nous avons substitué des valeurs pour ces espaces réservés : `template_string.substitute(name="Ihechikara", language="Python")`. 

Dans la sortie, nous avons eu ces valeurs de substitution remplacer les espaces réservés. 

De "Mon nom est $name ! Je crée du contenu sur $language" à "Mon nom est Ihechikara ! Je crée du contenu sur Python". 

## Comment formater des chaînes en Python en utilisant l'opérateur `%`

L'opérateur `%` a différents espaces réservés utilisés pour formater des chaînes. Vous pouvez voir tous les espaces réservés [ici](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting). 

Voici un exemple qui utilise les espaces réservés `%s` et `%d` :

```python
name = "John"
age = 80
print("%s a %d ans" %(name, age)) # John a 80 ans

```

Dans l'exemple ci-dessus, nous avons créé deux variables — `name` et `age`. 

Pour passer ces variables dans la chaîne, nous avons utilisé `%s` pour substituer la chaîne (`name`), et l'espace réservé `%d` pour substituer l'entier (`age`). C'est-à-dire :

```python
"%s a %d ans"
```

Pour s'assurer que les variables sont substituées dans ces positions, nous avons fourni les noms des variables entre parenthèses : `%(name, age)`. 

En les joignant ensemble, nous avons ceci : 

```python
"%s a %d ans" %(name, age)
```

Ainsi, l'espace réservé `%s` cherchera toute chaîne stockée dans les parenthèses et la substituera tandis que l'espace réservé `%d` fera de même pour toute valeur entière. 

## Comment formater des chaînes en Python en utilisant la méthode `format()`

La méthode `format()` est assez similaire à l'utilisation de l'opérateur `%`. 

Au lieu d'utiliser des espaces réservés, vous utilisez des accolades `{}` pour substituer les paramètres de la méthode `format()`. 

Voici un exemple :

```python
name = "John"
age = 80
print("{} a {} ans".format(name, age)) # John a 80 ans

```

Dans l'exemple ci-dessus, les accolades seront remplacées par les paramètres de la méthode `format()` — `format(name, age)`. 

De "{} a {} ans" à "John a 80 ans". 

## Comment formater des chaînes en Python en utilisant les f-strings

La méthode des f-strings utilise également des accolades. Dans la dernière section, nous avons dû attacher la méthode `format()` en utilisant la notation par point. 

Avec les f-strings, vous pouvez passer les noms des variables directement dans les accolades : 

```python
name = "John"
age = 80
print(f"{name} a {age} ans") # John a 80 ans
```

Pour utiliser les f-strings, placez simplement un `f` avant la marque de citation d'ouverture de la chaîne. Cela vous permet de passer des variables directement dans la chaîne.

Vous pouvez même effectuer des opérations arithmétiques dans la chaîne : 

```python
num1 = 20
num2 = 80
print(f"{num1} + {num2} = {num1 + num2}") # 20 + 80 = 100
```

## Résumé

Dans cet article, nous avons parlé des différentes méthodes utilisées pour formater des chaînes en Python. 

Nous avons commencé par examiner la classe de modèle de chaîne qui utilise l'opérateur `$` pour formater des chaînes. 

Nous avons ensuite vu comment d'autres méthodes comme l'opérateur `%`, la méthode `format()`, et les f-strings peuvent être utilisées pour formater des chaînes en Python. 

Bon codage ! Je parle également de Python sur [mon blog](https://ihechikara.com/).