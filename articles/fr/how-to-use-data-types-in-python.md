---
title: Comment utiliser les types de données en Python – Expliqué avec des exemples
  de code
subtitle: ''
author: Kamaldeen Lawal
co_authors: []
series: null
date: '2024-02-09T15:15:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-data-types-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/Python-Data-Types.png
tags:
- name: Python
  slug: python
seo_title: Comment utiliser les types de données en Python – Expliqué avec des exemples
  de code
seo_desc: 'In Python, a data type communicates with the interpreter about how the
  programmer intends to use the data and information stored. The classification of
  data specifies the type of value a variable can hold.

  In Python programming, you don''t need to exp...'
---

En Python, un type de données communique avec l'interpréteur sur la manière dont le programmeur entend utiliser les données et les informations stockées. La classification des données spécifie le type de valeur qu'une variable peut contenir.

En programmation Python, vous n'avez pas besoin de déclarer explicitement le type de données de votre variable. Au lieu de cela, Python, en tant que langage à typage dynamique, détermine le type de données de votre variable selon la valeur assignée.

Une compréhension solide des types de données en Python est cruciale car elle permet aux programmeurs d'écrire un code concis. Python dispose de plusieurs types de données intégrés comme les types de données de séquence, numérique, de mappage, d'ensemble, none et booléen.

Cet article abordera les sujets suivants :

* [Types de données numériques en Python](#heading-types-de-donnees-numeriques-en-python)
* [Types de données de séquence en Python](#heading-types-de-donnees-de-sequence-en-python)
* [Type de données de mappage en Python](#heading-type-de-donnees-de-mappage-en-python)
* [Type de données d'ensemble en Python](#heading-type-de-donnees-densemble-en-python)
* [Type de données None en Python](#heading-type-de-donnees-none-en-python)
* [Type de données booléen en Python](#heading-type-de-donnees-booleen-en-python)
* [Conclusion](#heading-conclusion)

## Types de données numériques en Python

Avez-vous déjà pensé à travailler avec des valeurs numériques avec Python ? Si oui, les types de données numériques sont utilisés pour représenter toute valeur numérique.

Il existe trois principaux types de données numériques en Python : les entiers, les nombres à virgule flottante et les nombres complexes.

### Type de données entier en Python

En Python, les entiers sont connus sous le nom de `int`. Ils sont un type de données intégré pour les nombres entiers. `int` peut représenter n'importe quelle taille d'entiers sans erreurs de dépassement car ils peuvent être positifs, nuls ou négatifs.

```python
# Entier Python
a = 7
y = -1
c = 0

print(a)  # Sortie : 7
print(y)  # Sortie : -1
print(c)  # Sortie : 0

```

De nombreux calculs arithmétiques comme l'addition, la soustraction, la multiplication, le modulo, la division entière, l'exponentiation et la division peuvent être effectués avec des entiers.

```python
# Opération d'addition +

addition = 8 + 3
print("Addition :", addition)  # Sortie : 11

# Opération de soustraction -
soustraction = 9 - 4
print("Soustraction :", soustraction)  # Sortie : 5

# Opération de multiplication *
multiplication = 10 * 2
print("Multiplication :", multiplication)  # Sortie : 20

# Opération de division /
division = 10 / 6
print("Division :", division)  # Sortie : 1.6666666666666667

# Opération de division entière //
division_entière = 10 // 2
print("Division entière :", division_entière)  # Sortie : 5

# Opération de modulo %
modulo = 10 % 5
print("Modulo :", modulo)  # Sortie : 0

# Opération d'exponentiation **
exponentiation = 2 ** 6
print("Exponentiation :", exponentiation)  # Sortie : 64

```

### Type de données à virgule flottante en Python

En Python, `float` peut représenter à la fois des nombres entiers et des fractions. Ils sont utilisés pour approximer des nombres réels. Par conséquent, ils ne sont pas précis lorsqu'ils traitent des nombres très petits ou très grands.

```python
# Float Python
b = 2.47
y = -0.1
k = 5.0

print(b)  # Sortie : 2.47
print(y)  # Sortie : -0.1
print(k)  # Sortie : 5.0

```

Les calculs arithmétiques à virgule flottante comme l'addition, la soustraction, la multiplication, le modulo, la division entière, l'exponentiation et la division sont effectués en utilisant des nombres à virgule flottante. Le float est n'importe quel nombre avec un point décimal.

```python
# Opération d'addition

a = 3.5
b = 2.1
print(a + b) # La sortie sera 5.3

 # Opération de soustraction
c = 5.5
d = 2.2
print(c - d) # La sortie sera 3.3

# Opération de multiplication

e = 4.0
f = 2.5
print(e * f)  # La sortie sera 10.0

# Opération de division
g= 10.0
h = 7.0
print(g / h) # La sortie sera 1.4285714285714286

# Opération exponentielle 
i = 2.0
j = 3.0
print(i * j)# La sortie sera 6.0

# Opération de modulo
k = 10.5
l = 4.0
print(k % l) # La sortie sera 2.5

# Opération de division entière
m = 10.5
n = 3.0
print(k // l) # La sortie sera 2.0
```

**Note :** En Python 3, par défaut, diviser deux entiers retourne un résultat à virgule flottante.

### Type de données complexe en Python

Les nombres `complex` sont couramment utilisés en ingénierie, en physique et en mathématiques pour modéliser les composantes réelles et imaginaires. Les nombres prennent la forme `a + bj`, où `a` et `b` sont des nombres réels, et `j` représente l'unité imaginaire, définie comme la racine carrée de -1.

```python
z1 = 8 + 2j  # Crée un nombre complexe 8 + 2j
z2 = -9 - 6j # Crée un nombre complexe -9 - 6j

```

Python peut effectuer diverses opérations arithmétiques comme l'addition, la soustraction, la multiplication et la division avec des nombres complexes.

```python
z2 = complex(3, 2)
z4 = complex(-1, 6)

# Opération d'addition
sum_z = z2 + z4  # Résultat : 3 - 1 + (2 + 6)j = 2 + 8j

# Soustraction
diff_z = z2 - z4  # Résultat : 3 - (-1) + (2 - 6)j = 4 - 4j

# Multiplication
prod_z = z2 * z4 

# Résultat : (3 * -1 - 2 * 6) + (3 * 6 + 2 * -1)j = (-15+16j)

# Division
div_z = z2 / z4 
# Résultat:(0.24324324324324323-0.5405405405405406j)



```

## Types de données de séquence en Python

En Python, il existe plusieurs types de données de séquence utilisés pour représenter des collections de données dans un ordre spécifique. Ils sont les suivants :

### Type de données liste en Python

Les listes sont définies en utilisant des crochets `[]` avec des éléments séparés par des virgules. Elles sont une structure de données intégrée et mutable pour stocker des collections d'éléments. La caractéristique de mutabilité de `[]` signifie qu'elle est modifiable après la création.

Les listes sont des structures de données largement utilisées en Python car elles supportent diverses opérations et offrent de la flexibilité.

L'élément à l'intérieur d'une liste peut être de n'importe quel type de données, y compris une liste.

```python
# Création de liste

the_list = [1, 2, 4, 5]


# création d'une liste de données mixtes
multiple_data_list = [1, 'hi', 2.57, False]



print(the_list[0])   # Sortie : 1
print(multiple_data_list[2])  # Sortie :2.57


# Caractéristique mutable de la liste

the_list[0] = 10          # Modifier le premier élément
the_list.append(9)        # Ajouter un nouvel élément
the_list.extend([5, 4])   # Étendre la liste avec une autre liste
the_list.remove(2)        # Supprimer un élément par valeur
del the_list[0]           # Supprimer un élément par index

```

### Type de données tuple en Python

En Python, un tuple est un type de données intégré et immuable pour stocker une collection ordonnée d'éléments.

Les tuples sont créés en utilisant des parenthèses `()`. Tout comme les listes, les tuples ont des éléments séparés par des virgules.

Un tuple nécessite une virgule après l'élément pour le différencier d'une expression parenthésée, même s'il contient un seul élément. La caractéristique d'immuabilité des tuples implique que vous ne pouvez pas les changer après la création.

```python
# Tuple vide
zilch_tuple = ()   
 
 # Tuple avec un seul élément            
single_tuple = (1,)  

 # Tuple avec plusieurs éléments 
multiple_tuple = (1,8,9,3, 5) 

# Immuabilité du tuple

single_slice[0] = 5

print(tuple_slice) # TypeError : l'objet 'tuple' ne supporte pas l'assignation d'élément


# Tuples avec différents éléments 
mixed_tuple = (1, 'hello', 3.14, True) 

 # Tuple imbriqué 

nested_tuple = ('Orange', ('banana', 'Pineapple'), ["he", 'she', 'them']) 


 # Concaténer des tuples

add_tuple = multiple_tuple + (6, 7, 8)  # Sortie : (1, 8, 9, 4, 3, 5, 7, 8)

# Créer une tranche du tuple
tuple_slice = add_tuple[1:3]     # Sortie : (8, 9)

```

### Type de données chaîne de caractères en Python

Une chaîne de caractères enfermée dans des guillemets simples `(')` ou doubles `(")` est une séquence immuable de caractères utilisée pour représenter des données textuelles.

Python vous permet d'effectuer des opérations comme l'indexation, le découpage et la concaténation sur les chaînes de caractères.

```python
# Création d'une chaîne de caractères avec des guillemets simples et doubles

single_string = 'Hello!'
double_string = "Python Programming!"

# Affichage du résultat 

print(single_string[0])    # Sortie : 'H'
print(double_string[-1])   # Sortie : '!'


print(single_string[0:5])    # Sortie : 'Hello'
print(double_string[::2])    # Sortie : 'Pto rgamn!'

# Concaténer les deux chaînes de caractères

concatenate_string = single_string + ' ' + double_string
print(concatenate_string)   # Sortie : 'Hello! Python Programming'


# Quelques méthodes populaires de chaînes de caractères comme upper, lower, find, replace, split et strip.

print(single_string.upper())              # Sortie : 'HELLO!'
print(double_string.lower())              # Sortie : 'python programming!'
print(single_string.find('World'))        # Sortie : -1
print(double_string.replace('Python', 'Java'))  # Sortie : 'Java Programming'
print(single_string.split(','))           # Sortie : ['Hello!']
print(double_string.strip())              # Sortie : 'Python Programming!'

```

### Type de données range en Python

La fonction `range` est utilisée pour itérer sur les éléments d'une liste. En exécutant une tâche de manière répétée, `range` génère des indices pour la structure de données.

La syntaxe pour une fonction `range` est la suivante :

```python
range(start, stop, step)

```

Le `start` représente une valeur de départ si, lorsqu'elle est omise, la plage commence à 0, tandis que `stop` est le nombre qui indique que la plage doit arrêter de générer des nombres.

Le `step` étant la dernière valeur, spécifie l'incrément ou le pas entre chaque nombre différent dans la séquence. La valeur par défaut pour ce paramètre est 1.

La fonction `range` retourne une série immuable de nombres.

```python
# Générer un nombre de 0 à 10
for i in range(11):
    print(i)  # SORTIE..... 0,1,2,3,4,5,6,7,8,9,10


# Générer un nombre de 1 à 19.
for i in range(1, 20):
    print(i) # SORTIE.....1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19
    
    
# Générer des nombres de 0 à 10 avec un pas de 2 :

for i in range(0, 21, 2):
    print(i)  # SORTIE.... 0,2,4,6,8,10,12,14,16,18,20


# Générer une liste de nombres en utilisant la fonction list en conjonction avec range :

new_list = list(range(15))
print(new_list)  # Sortie : [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14]

```

## Type de données de mappage en Python

En Python, le dictionnaire `dict` est le principal type de données pour stocker une collection de paires clé-valeur.

Le `dict` est largement utilisé en Python pour différentes fonctions, telles que le mappage entre des informations liées, la représentation d'un ensemble d'enregistrements de données et le stockage de configurations.

Nous pouvons créer un `dict` en Python soit avec des accolades `{}` soit avec le constructeur `dict()`.

Certaines des caractéristiques d'un dictionnaire sont les suivantes :

* **Paires Clé-Valeur** : Un `dict` se compose d'une clé associée à une valeur spécifique dans une paire clé-valeur. La fonction de la clé est de rechercher la valeur correspondante dans le dictionnaire.
* **Unicité** : Les clés en double ne sont pas autorisées dans `dict`. Attribuer une nouvelle valeur à une clé existante ne remplacera que l'ancienne valeur associée à cette clé.
* **Immuabilité des Clés** : La nature immuable des clés garantit que les clés restent "hachables" et cohérentes. Par conséquent, les clés dans un dictionnaire doivent être immuables. Certains exemples de types de données immuables incluent les entiers, les chaînes de caractères et les tuples.
* **Valeurs Flexibles** : N'importe quel type de données, y compris, mais sans s'y limiter, les listes, les tuples, les chaînes de caractères, les nombres et même les dictionnaires peuvent être associés à des clés dans un dictionnaire.

```python
person = {
    "name": "Kamaldeen",
    "age": 32,
    "city": "Nigeria"
}

```

Dans le code ci-dessus, les clés sont `"name"`, `"age"`, et `"city"` tandis que leurs valeurs correspondantes sont `"kamaldeen"`, `32`, et `"Nigeria"`.

```python
# Accéder aux valeurs par clé :

print(person["name"])  # Sortie : Kamaldeen

# Modifier les valeurs

person["age"] = 35  # Sortie : {'name': 'Kamaldeen', 'age': 35, 'city':
'Nigeria'}

# Ajouter une nouvelle paire clé-valeur

person["job"] = "Engineer"  # Sortie : {'name': 'Kamaldeen', 'age': 32, 'city': 'Nigeria', 'job': 'Engineer'}

# Vérifier si le nom est dans le dictionnaire person

if "name" in person:
    print("Le nom est présent dans le dictionnaire.") # Sortie : Le nom est présent dans le dictionnaire





```

## Type de données d'ensemble en Python

En Python, un `set` est un type de données intégré qui représente une collection d'éléments uniques sans ordre particulier.

Les éléments dans le `set` sont immuables, mais le `set` lui-même est mutable. Les ensembles peuvent être définis en utilisant des accolades `{}` avec des éléments séparés par des virgules ou par le constructeur `set()`. Ils sont utilisés pour des opérations mathématiques comme les unions, les intersections et les différences.

```python
# Création d'un ensemble avec des accolades
curly_set = {1, 2, 6, 4, 9}

# Création d'un ensemble avec la fonction set()
func_set = set([1, 2, 6, 9, 5])

```

Certaines des caractéristiques sont :

* **Pas d'ordre défini** : Dans un `set`, il n'y a pas d'ordre défini car les éléments sont non ordonnés.
* **Unicité** : Les ensembles sont uniques par nature, car ils ne permettent pas d'éléments en double.
* **Mutabilité** : Les ensembles vous permettent de les mettre à jour soit en ajoutant soit en supprimant des éléments après la création.
* **Immuabilité des éléments** : Les éléments mutables comme les `listes` ne peuvent pas être un élément d'un ensemble, car les éléments d'un ensemble doivent être immuables. Par conséquent, des types de données immuables comme les floats, les entiers, les tuples et les chaînes de caractères peuvent être utilisés à la place.

### Opération sur les ensembles

Python supporte les opérations mathématiques comme l'union, l'intersection, la différence et plus pour les ensembles.

#### Opération d'union utilisant les ensembles en Python

L'opération mathématique d'union de deux ensembles joint tous les éléments uniques des deux ensembles.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

union_set = first_set | second_set  # Utilisation de l'opérateur '|'
# Sortie : {1, 2, 3, 4, 5}

# ou

union_method = first_set.union(second_set)  # Utilisation de la méthode union()

# Sortie : {1, 2, 3, 4, 5}

```

L'union peut être créée soit avec `|` soit avec la méthode `union()`.

#### Opération d'intersection utilisant les ensembles en Python

En Python, l'intersection est une opération mathématique de deux ensembles qui imprime uniquement les éléments communs.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

union_set = first_set & second_set  # Utilisation de l'opérateur '&'
# Sortie : {3}

# ou

union_method = first_set.intersection(second_set)  # Utilisation de la méthode union()
# Sortie : {3}

print(union_set)
print(union_method)
```

L'intersection peut être créée soit avec `&` soit avec la méthode `intersection()`.

#### Opération de différence utilisant les ensembles en Python

En Python, l'opération mathématique de différence entre deux ensembles se produit lorsqu'un élément est présent dans le premier, mais pas dans le second.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

union_set = first_set - second_set  # Utilisation de l'opérateur '-'

# ou

union_method = first_set.difference(second_set)  # Utilisation de la méthode difference()


print(union_set)
print(union_method)
```

La différence peut être créée soit avec `-` soit avec la méthode `difference()`.

#### Opération d'ajout utilisant les ensembles en Python

La méthode `add()` des ensembles est utilisée pour ajouter un seul élément à la collection d'ensemble, tandis que la méthode `update()` est utilisée pour ajouter plusieurs éléments.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

# Ajout avec la méthode add
first_set.add(4)

# Mise à jour avec la méthode update 
second_set.update({4,8,9,7})

print(first_set) # Sortie : {1, 2, 3, 4}
print(second_set)  # Sortie : {3, 4, 5, 7, 8, 9}

```

#### Opération de suppression utilisant les ensembles en Python

En Python, la fonction de la méthode `remove()` dans les ensembles est de supprimer un élément spécifique s'il existe. La méthode `discard()` est également utilisée pour supprimer un élément s'il existe.

La seule différence est que `discard()` ne lèvera pas d'erreur si l'élément n'existe pas, mais `remove()` lèvera une `KeyError`.

```python
first_set = {1, 2, 3}
second_set = {3, 4, 5}

first_set.remove(5) # Sortie : KeyError : 5
second_set.discard(4)  # Sortie : KeyError : {3, 5}

print(first_set)
print(second_set)

```

#### Opération Frozenset utilisant les ensembles en Python

Le `frozenset` est un ensemble immuable intégré. Il est défini comme un ensemble régulier avec `{}`, mais ses éléments ne peuvent pas être changés ou modifiés après la création.

```python
# Création d'un frozenset

frozen_set = frozenset([7, 2, 3, 1, 5])

# Les frozensets sont immuables.

 frozen_set.add(6)  # Une AttributeError sera levée

# Les éléments d'un frozenset ne peuvent pas être changés une fois qu'il est créé

frozen_set[0] = 10  # Une TypeError sera levée

# Vous pouvez effectuer des opérations sur les ensembles comme l'union, l'intersection et la différence sur le frozenset
```

## Type de données None en Python

En Python, le type de données `None` représente l'absence de valeur ou une valeur nulle.

Il indique que la fonction n'a pas de valeur de retour ou que l'expression manque de valeur significative.

Certains points clés à retenir du type de données None :

* **Type** : `None` est appelé le type de données `NoneType` en Python.
* **Valeur de retour** : `None` est la valeur de retour par défaut pour une fonction sans valeur.
* **Valeur par défaut** : Nous pouvons utiliser `None` comme argument par défaut dans la définition de la fonction.

```python
# Initialisation de z avec None, indiquant qu'il ne contient actuellement aucune valeur significative.

z = None
print(z)  # Sortie : None


y = None
if y is None:
    print("La valeur de y est :" "x est None")

# Sortie : La valeur de y est : y est None


def pair(y=None):
    if y is None:
        print("y est None")

pair()  # Sortie : y est None


# La fonction greeting() imprime un message si un nom est fourni, sinon elle salue un inconnu, mais comme la fonction ne retourne aucune valeur explicitement, elle retourne None par défaut.

def greeting(name):
    if name:
        print("Hi, " + name)
    else:
        print("Hi, Stranger")

result = greeting("Kamaldeen")  # Sortie : Hello, Kamaldeen
print(result)  # Sortie : None

```

## Type de données booléen en Python

En Python, il n'y a que deux valeurs utilisées pour les comparaisons et les opérations logiques lors de l'utilisation du type de données `boolean`. Ce sont les valeurs `True` et `False`.

Les valeurs `boolean` sont le résultat qui provient des opérateurs de comparaison tels que l'égalité (`==`), la non-égalité (`!=`), le supérieur à (`>`), le inférieur à (`<`), le supérieur ou égal à (`>=`), et le inférieur ou égal à (`<=`).

```python
a = 10
b = 15

# Opérateurs de comparaison

print(a == b)  # False
print(a < b)   # True

# Opérateurs logiques

print(a < 10 and b > 5)  # False
print(a < 3 or b> 20)   # False
print(not(a == b))        # True

# Flux de contrôle

age = 75

if age >= 18:
    print("Vous êtes un adulte.")
else:
    print("Vous êtes un mineur.")

# Fonctions de retour

def is_even(number):
    return number % 2 == 0

print(is_even(10))  # True
print(is_even(7))  # False

```

## Conclusion

Dans ce tutoriel, vous avez appris les différents types de données en Python.

Nous avons parlé de plusieurs types de données intégrés comme les types de données de séquence, de mappage, d'ensemble, none et booléen.

Bonne lecture !