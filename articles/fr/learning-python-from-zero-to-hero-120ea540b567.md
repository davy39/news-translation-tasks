---
title: 'Apprendre Python : De Zéro à Héros'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-30T20:48:17.000Z'
originalURL: https://freecodecamp.org/news/learning-python-from-zero-to-hero-120ea540b567
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ueWmI48uuShON-hX7LwI0w.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: 'Apprendre Python : De Zéro à Héros'
seo_desc: 'By TK

  First of all, what is Python? According to its creator, Guido van Rossum, Python
  is a:


  “high-level programming language, and its core design philosophy is all about code
  readability and a syntax which allows programmers to express concepts in ...'
---

Par TK

Tout d'abord, qu'est-ce que Python ? Selon son créateur, Guido van Rossum, Python est un :

> « langage de programmation de haut niveau, et sa philosophie de conception principale est centrée sur la lisibilité du code et une syntaxe qui permet aux programmeurs d'exprimer des concepts en quelques lignes de code. »

Pour moi, la première raison d'apprendre Python était qu'il s'agit, en fait, d'un langage de programmation magnifique. Il était vraiment naturel de coder avec et d'exprimer mes pensées.

Une autre raison était que nous pouvons utiliser la programmation en Python de multiples façons : la science des données, le développement web et l'apprentissage automatique excellent ici. Quora, Pinterest et Spotify utilisent tous Python pour leur développement web backend. Alors apprenons un peu à ce sujet.

### Les Bases

#### 1. Variables

Vous pouvez penser aux variables comme des mots qui stockent une valeur. C'est aussi simple que cela.

En Python, il est vraiment facile de définir une variable et de lui attribuer une valeur. Imaginez que vous voulez stocker le nombre 1 dans une variable appelée « one ». Faisons-le :

```py
one = 1
```

C'était simple, n'est-ce pas ? Vous venez d'attribuer la valeur 1 à la variable « one ».

```py
two = 2
some_number = 10000
```

Et vous pouvez attribuer n'importe quelle autre **valeur** à n'importe quelle autre **variable** que vous voulez. Comme vous le voyez dans le tableau ci-dessus, la variable « **two** » stocke l'entier **2**, et « **some_number** » stocke **10 000**. 

En plus des entiers, nous pouvons également utiliser des booléens (True / False), des chaînes de caractères, des flottants, et tant d'autres types de données.

```py
# booléens
true_boolean = True
false_boolean = False

# chaîne de caractères
my_name = "Leandro Tk"

# flottant
book_price = 15.80
```

#### 2. Contrôle de Flux : instructions conditionnelles

« **If** » utilise une expression pour évaluer si une instruction est True ou False. Si c'est True, il exécute ce qui est à l'intérieur de l'instruction « if ». Par exemple :

```py
if True:
  print("Hello Python If")

if 2 > 1:
  print("2 est plus grand que 1")
```

**2** est plus grand que **1**, donc le code « **print** » est exécuté.

L'instruction « **else** » sera exécutée si l'expression « **if** » est **false**. 

```py
if 1 > 2:
  print("1 est plus grand que 2")
else:
  print("1 n'est pas plus grand que 2")
```

**1** n'est pas plus grand que **2**, donc le code à l'intérieur de l'instruction « **else** » sera exécuté.

Vous pouvez également utiliser une instruction « **elif** » :

```py
if 1 > 2:
  print("1 est plus grand que 2")
elif 2 > 1:
  print("1 n'est pas plus grand que 2")
else:
  print("1 est égal à 2")
```

#### 3. Boucles / Itérateur

En Python, nous pouvons itérer de différentes manières. Je vais parler de deux : **while** et **for**.

**Boucle While** : tant que l'instruction est True, le code à l'intérieur du bloc sera exécuté. Donc, ce code imprimera les nombres de **1** à **10**. 

```py
num = 1

while num <= 10:
    print(num)
    num += 1
```

La boucle **while** a besoin d'une « **condition de boucle** ». Si elle reste True, elle continue à itérer. Dans cet exemple, lorsque `num` est `11`, la **condition de boucle** devient `False`.

Un autre morceau de code basique pour mieux le comprendre :

```py
loop_condition = True

while loop_condition:
    print("La condition de boucle reste : %s" %(loop_condition))
    loop_condition = False
```

La **condition de boucle** est `True`, donc elle continue à itérer — jusqu'à ce que nous la définissions à `False`.

**Boucle For** : vous appliquez la variable « **num** » au bloc, et l'instruction « **for** » l'itérera pour vous. Ce code imprimera la même chose que le code **while** : de **1** à **10**. 

```py
for i in range(1, 11):
  print(i)
```

Vous voyez ? C'est si simple. La plage commence avec `1` et va jusqu'au `11`ème élément (`10` est le `10`ème élément).

### Liste : Collection | Tableau | Structure de Données

Imaginez que vous voulez stocker l'entier 1 dans une variable. Mais peut-être que maintenant vous voulez stocker 2. Et 3, 4, 5 …

Y a-t-il une autre façon de stocker tous les entiers que je veux, mais pas dans **des millions de variables** ? Vous l'avez deviné — il y a effectivement une autre façon de les stocker.

`Liste` est une collection qui peut être utilisée pour stocker une liste de valeurs (comme ces entiers que vous voulez). Alors utilisons-la :

```py
my_integers = [1, 2, 3, 4, 5]
```

C'est vraiment simple. Nous avons créé un tableau et l'avons stocké dans **my_integer**.

Mais peut-être vous demandez-vous : « Comment puis-je obtenir une valeur de ce tableau ? »

Excellente question. `Liste` a un concept appelé **index**. Le premier élément obtient l'index 0 (zéro). Le deuxième obtient 1, et ainsi de suite. Vous comprenez l'idée.

Pour le rendre plus clair, nous pouvons représenter le tableau et chaque élément avec son index. Je peux le dessiner :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ReMk6NgghLII20vPD6uNEA.jpeg)

En utilisant la syntaxe Python, c'est aussi simple à comprendre :

```py
my_integers = [5, 7, 1, 3, 4]
print(my_integers[0]) # 5
print(my_integers[1]) # 7
print(my_integers[4]) # 4
```

Imaginez que vous ne voulez pas stocker des entiers. Vous voulez juste stocker des chaînes de caractères, comme une liste des noms de vos proches. La mienne ressemblerait à ceci :

```py
relatives_names = [
  "Toshiaki",
  "Juliana",
  "Yuji",
  "Bruno",
  "Kaio"
]

print(relatives_names[4]) # Kaio
```

Cela fonctionne de la même manière que les entiers. Bien.

Nous venons d'apprendre comment fonctionnent les indices des `Listes`. Mais je dois encore vous montrer comment nous pouvons ajouter un élément à la structure de données `Liste` (un élément à une liste).

La méthode la plus courante pour ajouter une nouvelle valeur à une `Liste` est `append`. Voyons comment cela fonctionne :

```py
bookshelf = []
bookshelf.append("The Effective Engineer")
bookshelf.append("The 4 Hour Work Week")
print(bookshelf[0]) # The Effective Engineer
print(bookshelf[1]) # The 4 Hour Work Week
```

`append` est super simple. Vous devez simplement appliquer l'élément (par exemple, « **The Effective Engineer** ») comme paramètre de `append`.

Bien, assez parlé des `Listes`. Parlons d'une autre structure de données.

### Dictionnaire : Structure de Données Clé-Valeur

Maintenant, nous savons que les `Listes` sont indexées avec des nombres entiers. Mais que faire si nous ne voulons pas utiliser des nombres entiers comme indices ? Certaines structures de données que nous pouvons utiliser sont numériques, des chaînes de caractères ou d'autres types d'indices.

Apprenons à connaître la structure de données `Dictionnaire`. `Dictionnaire` est une collection de paires clé-valeur. Voici à quoi cela ressemble :

```py
dictionary_example = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
```

La **clé** est l'index pointant vers la valeur. Comment accédons-nous à la **valeur** du `Dictionnaire` ? Vous l'avez deviné — en utilisant la **clé**. Essayons :

```py
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %s" %(dictionary_tk["nationality"])) # And by the way I'm Brazilian
```

J'ai créé un `Dictionnaire` à mon sujet. Mon nom, mon surnom et ma nationalité. Ces attributs sont les **clés** du `Dictionnaire`.

Comme nous avons appris à accéder à la `Liste` en utilisant l'index, nous utilisons également des indices (**clés** dans le contexte du `Dictionnaire`) pour accéder à la **valeur** stockée dans le `Dictionnaire`.

Dans l'exemple, j'ai imprimé une phrase à mon sujet en utilisant toutes les valeurs stockées dans le `Dictionnaire`. Assez simple, n'est-ce pas ?

Une autre chose intéressante à propos du `Dictionnaire` est que nous pouvons utiliser n'importe quoi comme valeur. Dans le `Dictionnaire` que j'ai créé, je veux ajouter la **clé** « age » et mon âge entier réel :

```py
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

print("My name is %s" %(dictionary_tk["name"])) # My name is Leandro
print("But you can call me %s" %(dictionary_tk["nickname"])) # But you can call me Tk
print("And by the way I'm %i and %s" %(dictionary_tk["age"], dictionary_tk["nationality"])) # And by the way I'm Brazilian
```

Ici, nous avons une paire **clé** (age) **valeur** (24) utilisant une chaîne de caractères comme **clé** et un entier comme **valeur**.

Comme nous l'avons fait avec les `Listes`, apprenons comment ajouter des éléments à un `Dictionnaire`. La **clé** pointant vers une valeur est une grande partie de ce qu'est un `Dictionnaire`. Cela est également vrai lorsque nous parlons d'ajouter des éléments :

```py
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian"
}

dictionary_tk['age'] = 24

print(dictionary_tk) # {'nationality': 'Brazilian', 'age': 24, 'nickname': 'Tk', 'name': 'Leandro'}

```

Nous devons simplement attribuer une **valeur** à une clé de `Dictionnaire`. Rien de compliqué ici, n'est-ce pas ?

### Itération : Boucler à travers les Structures de Données

Comme nous l'avons appris dans les [**Bases de Python**](https://medium.com/the-renaissance-developer/python-101-the-basics-441136fb7cc3), l'itération des `Listes` est très simple. Nous, les développeurs `Python`, utilisons couramment la boucle `For`. Faisons-le :

```py
bookshelf = [
  "The Effective Engineer",
  "The 4-hour Workweek",
  "Zero to One",
  "Lean Startup",
  "Hooked"
]

for book in bookshelf:
    print(book)
```

Donc pour chaque livre dans la bibliothèque, nous (**pouvons tout faire avec**) l'imprimons. C'est si simple et intuitif. C'est Python.

Pour une structure de données de type hash, nous pouvons également utiliser la boucle `for`, mais nous appliquons la `clé` :

```py
dictionary = { "some_key": "some_value" }

for key in dictionary:
    print("%s --> %s" %(key, dictionary[key]))
    
# some_key --> some_value
```

C'est un exemple de la façon de l'utiliser. Pour chaque `clé` dans le `dictionnaire`, nous `imprimons` la `clé` et sa `valeur` correspondante.

Une autre façon de le faire est d'utiliser la méthode `iteritems`.

```py
dictionary = { "some_key": "some_value" }

for key, value in dictionary.items():
    print("%s --> %s" %(key, value))

# some_key --> some_value
```

Nous avons nommé les deux paramètres `key` et `value`, mais ce n'est pas nécessaire. Nous pouvons les nommer comme nous voulons. Voyons cela :

```py
dictionary_tk = {
  "name": "Leandro",
  "nickname": "Tk",
  "nationality": "Brazilian",
  "age": 24
}

for attribute, value in dictionary_tk.items():
    print("My %s is %s" %(attribute, value))
    
# My name is Leandro
# My nickname is Tk
# My nationality is Brazilian
# My age is 24
```

Nous pouvons voir que nous avons utilisé l'attribut comme paramètre pour la **clé** du `Dictionnaire`, et cela fonctionne correctement. Super !

### Classes & Objets

#### Un peu de théorie :

Les **Objets** sont une représentation d'objets du monde réel comme les voitures, les chiens ou les vélos. Les objets partagent deux caractéristiques principales : les **données** et le **comportement**. 

Les voitures ont des **données**, comme le nombre de roues, le nombre de portes et la capacité d'assise. Elles présentent également un **comportement** : elles peuvent accélérer, s'arrêter, montrer combien de carburant il reste, et tant d'autres choses.

En programmation orientée objet, nous identifions les **données** comme des **attributs** et le **comportement** comme des **méthodes**. Encore une fois :

Données → Attributs et Comportement → Méthodes

Et une **Classe** est le plan à partir duquel des objets individuels sont créés. Dans le monde réel, nous trouvons souvent de nombreux objets du même type. Comme les voitures. Toutes du même fabricant et modèle (et toutes ont un moteur, des roues, des portes, etc.). Chaque voiture a été construite à partir du même ensemble de plans et a les mêmes composants.

#### Mode Programmation Orientée Objet Python : ACTIVÉ

Python, en tant que langage de programmation orienté objet, a ces concepts : **classe** et **objet**.

Une classe est un plan, un modèle pour ses objets.

Donc encore une fois, une classe n'est qu'un modèle, ou une façon de définir des **attributs** et un **comportement** (comme nous en avons parlé dans la section théorie). Par exemple, une **classe** de véhicule a ses propres **attributs** qui définissent quels **objets** sont des véhicules. Le nombre de roues, le type de réservoir, la capacité d'assise et la vitesse maximale sont tous des attributs d'un véhicule.

Avec cela en tête, regardons la syntaxe Python pour les **classes** :

```py
class Vehicle:
    pass
```

Nous définissons les classes avec une **instruction de classe** — et c'est tout. Facile, n'est-ce pas ?

Les **Objets** sont des instances d'une **classe**. Nous créons une instance en nommant la classe.

```py
car = Vehicle()
print(car) # <__main__.Vehicle instance at 0x7fb1de6c2638>
```

Ici, `car` est un **objet** (ou instance) de la **classe** `Vehicle`.

Rappelez-vous que notre **classe** de véhicule a quatre **attributs** : nombre de roues, type de réservoir, capacité d'assise et vitesse maximale. Nous définissons tous ces **attributs** lors de la création d'un **objet** véhicule. Donc ici, nous définissons notre **classe** pour recevoir des données lorsqu'elle l'initialise :

```py
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
```

Nous utilisons la méthode `init`. Nous l'appelons une méthode de constructeur. Donc lorsque nous créons l'**objet** véhicule, nous pouvons définir ces **attributs**. Imaginez que nous aimons la **Tesla Model S**, et nous voulons créer ce type d'**objet**. Elle a quatre roues, fonctionne à l'énergie électrique, a de la place pour cinq sièges, et la vitesse maximale est de 250 km/h (155 mph). Créons cet **objet** :

```py
tesla_model_s = Vehicle(4, 'electric', 5, 250)
```

Quatre roues + réservoir de type « électrique » + cinq sièges + vitesse maximale de 250 km/h.

Tous les attributs sont définis. Mais comment pouvons-nous accéder aux valeurs de ces attributs ? Nous **envoyons un message à l'objet pour lui demander**. Nous appelons cela une **méthode**. C'est le **comportement de l'objet**. Implémentons-le :

```py
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def number_of_wheels(self):
        return self.number_of_wheels

    def set_number_of_wheels(self, number):
        self.number_of_wheels = number
```

C'est une implémentation de deux méthodes : **number_of_wheels** et **set_number_of_wheels**. Nous l'appelons `getter` & `setter`. Parce que le premier obtient la valeur de l'attribut, et le second définit une nouvelle valeur pour l'attribut.

En Python, nous pouvons faire cela en utilisant `@property` (`decorateurs`) pour définir les `getters` et `setters`. Voyons cela avec du code :

```py
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
    
    @property
    def number_of_wheels(self):
        return self.__number_of_wheels
    
    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.__number_of_wheels = number
```

Et nous pouvons utiliser ces méthodes comme des attributs :

```py
tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels) # 4
tesla_model_s.number_of_wheels = 2 # définir le nombre de roues à 2
print(tesla_model_s.number_of_wheels) # 2
```

Cela est légèrement différent de la définition des méthodes. Les méthodes fonctionnent comme des attributs. Par exemple, lorsque nous définissons le nouveau nombre de roues, nous n'appliquons pas deux comme paramètre, mais définissons la valeur 2 à `number_of_wheels`. C'est une façon d'écrire du code `pythonique` pour les `getters` et `setters`.

Mais nous pouvons également utiliser des méthodes pour d'autres choses, comme la méthode « **make_noise** ». Voyons cela :

```py
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def make_noise(self):
        print('VRUUUUUUUM')
```

Lorsque nous appelons cette méthode, elle retourne simplement une chaîne de caractères **_« VRRRRUUUUM. »_**

```py
tesla_model_s = Vehicle(4, 'electric', 5, 250)
tesla_model_s.make_noise() # VRUUUUUUUM
```

### Encapsulation : Masquer les Informations

L'encapsulation est un mécanisme qui restreint l'accès direct aux données et méthodes des objets. Mais en même temps, elle facilite les opérations sur ces données (méthodes des objets).

> « L'encapsulation peut être utilisée pour masquer les membres de données et les fonctions membres. Selon cette définition, l'encapsulation signifie que la représentation interne d'un [objet](https://en.wikipedia.org/wiki/Object_(computer_science)) est généralement cachée de la vue en dehors de la définition de l'objet. » — Wikipedia

Toute la représentation interne d'un objet est cachée de l'extérieur. Seul l'objet peut interagir avec ses données internes.

Tout d'abord, nous devons comprendre comment fonctionnent les variables et méthodes d'instance `public` et `non-public`.

#### Variables d'Instance Publiques

Pour une classe Python, nous pouvons initialiser une `variable d'instance publique` dans notre méthode de constructeur. Voyons cela :

Dans la méthode de constructeur :

```py
class Person:
    def __init__(self, first_name):
        self.first_name = first_name
```

Ici, nous appliquons la valeur `first_name` comme argument à la `variable d'instance publique`.

```py
tk = Person('TK')
print(tk.first_name) # => TK
```

Dans la classe :

```py
class Person:
    first_name = 'TK'
```

Ici, nous n'avons pas besoin d'appliquer `first_name` comme argument, et tous les objets d'instance auront un `attribut de classe` initialisé avec `TK`.

```py
tk = Person()
print(tk.first_name) # => TK
```

Super. Nous avons maintenant appris que nous pouvons utiliser des `variables d'instance publiques` et des `attributs de classe`. Une autre chose intéressante à propos de la partie `public` est que nous pouvons gérer la valeur de la variable. Que veux-je dire par là ? Notre `objet` peut gérer sa valeur de variable : `Get` et `Set` les valeurs de variable.

En gardant à l'esprit la classe `Person`, nous voulons définir une autre valeur à sa variable `first_name` :

```py
tk = Person('TK')
tk.first_name = 'Kaio'
print(tk.first_name) # => Kaio
```

Nous avons défini une autre valeur (`kaio`) à la variable d'instance `first_name` et elle a mis à jour la valeur. C'est aussi simple que cela. Puisqu'il s'agit d'une variable `public`, nous pouvons faire cela.

#### Variable d'Instance Non-Publique

> Nous n'utilisons pas le terme « privé » ici, puisque aucun attribut n'est vraiment privé en Python (sans une quantité généralement inutile de travail). — [PEP 8](https://www.python.org/dev/peps/pep-0008/#designing-for-inheritance)

Comme pour la `variable d'instance publique`, nous pouvons définir la `variable d'instance non-publique` à la fois dans la méthode de constructeur ou dans la classe. La différence de syntaxe est : pour les `variables d'instance non-publiques`, utilisez un tiret bas (`_`) avant le nom de la `variable`.

> « Les variables d'instance 'privées' qui ne peuvent être accédées que depuis l'intérieur d'un objet n'existent pas en Python. Cependant, il existe une convention suivie par la plupart du code Python : un nom précédé d'un tiret bas (par exemple, `_spam`) doit être traité comme une partie non-publique de l'API (qu'il s'agisse d'une fonction, d'une méthode ou d'un membre de données) » — [Python Software Foundation](https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references)

Voici un exemple :

```py
class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email
```

Avez-vous vu la variable `email` ? C'est ainsi que nous définissons une `variable non-publique` :

```py
tk = Person('TK', 'tk@mail.com')
print(tk._email) # tk@mail.com
```

> Nous pouvons y accéder et la mettre à jour. Les `variables non-publiques` sont juste une convention et doivent être traitées comme une partie non-publique de l'API.

Nous utilisons donc une méthode qui nous permet de le faire à l'intérieur de notre définition de classe. Implémentons deux méthodes (`email` et `update_email`) pour comprendre cela :

```py
class Person:
    def __init__(self, first_name, email):
        self.first_name = first_name
        self._email = email

    def update_email(self, new_email):
        self._email = new_email

    def email(self):
        return self._email
```

Maintenant, nous pouvons mettre à jour et accéder aux `variables non-publiques` en utilisant ces méthodes. Voyons cela :

```py
tk = Person('TK', 'tk@mail.com')
print(tk.email()) # => tk@mail.com
# tk._email = 'new_tk@mail.com' -- traiter comme une partie non-publique de l'API de la classe
print(tk.email()) # => tk@mail.com
tk.update_email('new_tk@mail.com')
print(tk.email()) # => new_tk@mail.com
```

1. Nous avons initié un nouvel objet avec `first_name` TK et `email` tk@mail.com
2. Imprimé l'email en accédant à la `variable non-publique` avec une méthode
3. Essayé de définir un nouvel `email` en dehors de notre classe
4. Nous devons traiter la `variable non-publique` comme une partie `non-publique` de l'API
5. Mis à jour la `variable non-publique` avec notre méthode d'instance
6. Succès ! Nous pouvons la mettre à jour à l'intérieur de notre classe avec la méthode d'aide

#### Méthode Publique

Avec les `méthodes publiques`, nous pouvons également les utiliser en dehors de notre classe :

```py
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._age
```

Testons cela :

```py
tk = Person('TK', 25)
print(tk.show_age()) # => 25
```

Super — nous pouvons l'utiliser sans aucun problème.

#### Méthode Non-Publique

Mais avec les `méthodes non-publiques`, nous ne pouvons pas le faire. Implémentons la même classe `Person`, mais maintenant avec une méthode `show_age` `non-publique` en utilisant un tiret bas (`_`).

```py
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def _show_age(self):
        return self._age
```

Et maintenant, nous allons essayer d'appeler cette `méthode non-publique` avec notre objet :

```py
tk = Person('TK', 25)
print(tk._show_age()) # => 25
```

> Nous pouvons y accéder et la mettre à jour. Les `méthodes non-publiques` sont juste une convention et doivent être traitées comme une partie non-publique de l'API.

Voici un exemple de la façon dont nous pouvons l'utiliser :

```py
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self._age = age

    def show_age(self):
        return self._get_age()

    def _get_age(self):
        return self._age

tk = Person('TK', 25)
print(tk.show_age()) # => 25
```

Ici, nous avons une méthode `_get_age` `non-publique` et une méthode `show_age` `publique`. La méthode `show_age` peut être utilisée par notre objet (en dehors de notre classe) et la méthode `_get_age` n'est utilisée qu'à l'intérieur de notre définition de classe (à l'intérieur de la méthode `show_age`). Mais encore une fois : par convention.

#### Résumé de l'Encapsulation

Avec l'encapsulation, nous pouvons nous assurer que la représentation interne de l'objet est cachée de l'extérieur.

### Héritage : Comportements et Caractéristiques

Certains objets ont des choses en commun : leur comportement et leurs caractéristiques.

Par exemple, j'ai hérité de certaines caractéristiques et comportements de mon père. J'ai hérité de ses yeux et de ses cheveux comme caractéristiques, et de son impatience et de son introversion comme comportements.

En programmation orientée objet, les classes peuvent hériter de caractéristiques communes (données) et de comportements (méthodes) d'une autre classe.

Voyons un autre exemple et implémentons-le en Python.

Imaginez une voiture. Le nombre de roues, la capacité d'assise et la vitesse maximale sont tous des attributs d'une voiture. Nous pouvons dire qu'une classe **ElectricCar** hérite de ces mêmes attributs de la classe **Car** régulière.

```py
class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity
```

Notre classe **Car** implémentée :

```py
my_car = Car(4, 5, 250)
print(my_car.number_of_wheels)
print(my_car.seating_capacity)
print(my_car.maximum_velocity)
```

Une fois initiée, nous pouvons utiliser toutes les `variables d'instance` créées. Bien.

En Python, nous appliquons une `classe parente` à la `classe enfant` comme paramètre. Une classe **ElectricCar** peut hériter de notre classe **Car**.

```py
class ElectricCar(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)
```

C'est aussi simple que cela. Nous n'avons pas besoin d'implémenter une autre méthode, car cette classe l'a déjà (héritée de la classe **Car**). Prouvons-le :

```py
my_electric_car = ElectricCar(4, 5, 250)
print(my_electric_car.number_of_wheels) # => 4
print(my_electric_car.seating_capacity) # => 5
print(my_electric_car.maximum_velocity) # => 250
```

Magnifique.

### C'est tout !

Nous avons appris beaucoup de choses sur les bases de Python :

* Comment fonctionnent les variables Python
* Comment fonctionnent les instructions conditionnelles Python
* Comment fonctionnent les boucles Python (while & for)
* Comment utiliser les Listes : Collection | Tableau
* Collection Clé-Valeur de Dictionnaire
* Comment nous pouvons itérer à travers ces structures de données
* Objets et Classes
* Attributs comme données d'objets
* Méthodes comme comportement d'objets
* Utilisation des getters et setters Python & décorateur property
* Encapsulation : masquer les informations
* Héritage : comportements et caractéristiques

Félicitations ! Vous avez terminé ce morceau dense de contenu sur Python.

Si vous voulez un cours complet sur Python, apprendre plus de compétences de codage du monde réel et construire des projets, essayez [**_One Month Python Bootcamp_**](https://onemonth.com/courses/python?campaignid=33447&discount_code=TKPython1&mbsy=lG6tv&mbsy_source=7d89eeb0-0031-478c-a60c-6a96d762712a). À bientôt ☺

Pour plus d'histoires et de posts sur mon parcours d'apprentissage et de maîtrise de la programmation, suivez ma publication [**The Renaissance Developer**](https://medium.com/the-renaissance-developer).

Amusez-vous, continuez à apprendre et codez toujours.

Mon [Twitter](https://twitter.com/LeandroTk_) & [Github](https://github.com/LeandroTk). ☺