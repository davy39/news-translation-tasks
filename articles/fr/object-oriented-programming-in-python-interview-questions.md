---
title: Comment utiliser la programmation orientée objet en Python – Concepts clés
  de la POO et questions d'entretien pour débutants
subtitle: ''
author: Casmir Onyekani
co_authors: []
series: null
date: '2024-10-25T01:04:39.220Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-in-python-interview-questions
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729679277832/18ab2f5b-0636-44e7-b063-0773e5039fb0.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
- name: interview questions
  slug: interview-questions
seo_title: Comment utiliser la programmation orientée objet en Python – Concepts clés
  de la POO et questions d'entretien pour débutants
seo_desc: OOP is a crucial concept that every developer should grasp, especially when
  getting ready for job interviews. It helps you organize code into modular and reusable
  sections, which simplifies the development, maintenance, and scaling of software
  applic...
---

La POO est un concept crucial que tout développeur doit maîtriser, surtout lorsqu'il se prépare pour des entretiens d'embauche. Elle vous aide à organiser le code en sections modulaires et réutilisables, ce qui simplifie le développement, la maintenance et la mise à l'échelle des applications logicielles.

Dans cet article, j'utiliserai quelques questions d'entretien courantes pour simplifier les concepts clés de la POO, en fournissant des explications claires et des extraits de code pour renforcer votre confiance pour votre prochain entretien.

## Table des matières

* [Qu'est-ce que la POO ?](#heading-questce-que-la-poo)
    
* [Quels sont les quatre principes principaux de la POO ?](#heading-quels-sont-les-quatre-principes-principaux-de-la-poo)
    
* [Qu'est-ce que la surcharge de méthode ?](#heading-questce-que-la-surcharge-de-methode)
    
* [Qu'est-ce qu'un constructeur en POO ?](#heading-questce-quun-constructeur-en-poo)
    
* [Qu'est-ce qu'un destructeur en POO ?](#heading-questce-quun-destructeur-en-poo)
    
* [Qu'est-ce qu'une classe en POO ?](#heading-questce-quune-classe-en-poo)
    
* [Qu'est-ce qu'un objet en POO ?](#heading-questce-quun-objet-en-poo)
    
* [Qu'est-ce qu'une méthode statique ?](#heading-questce-quune-methode-statique)
    
* [Quelle est la différence entre une variable de classe et une variable d'instance ?](#heading-quelle-est-la-difference-entre-une-variable-de-classe-et-une-variable-dinstance)
    
* [Python supporte-t-il l'héritage multiple ?](#heading-python-supporte-t-il-lheritage-multiple)
    
* [Quelle est la différence entre une classe abstraite et une interface ?](#heading-quelle-est-la-difference-entre-une-classe-abstraite-et-une-interface)
    
* [Conclusion](#heading-conclusion)
    

## Qu'est-ce que la POO ?

La programmation orientée objet (POO) est une manière d'écrire des logiciels qui tourne autour des objets. Ces objets peuvent stocker des données et leurs actions (méthodes). Plutôt que de se concentrer uniquement sur les processus et la logique, la POO vous encourage à structurer votre code autour de ces objets.

Cette approche facilite la création de conceptions de logiciels modulaires, réutilisables et évolutives.

## Quels sont les quatre principes principaux de la POO ?

Les quatre piliers de la POO sont :

* Encapsulation
    
* Abstraction
    
* Héritage
    
* Polymorphisme
    

### Qu'est-ce que l'encapsulation et pourquoi est-elle importante ?

L'encapsulation aide à protéger les données à l'intérieur d'un objet. Pensez à cela comme à garder certains détails privés, permettant uniquement un accès contrôlé à ceux-ci.

C'est-à-dire, au lieu de modifier ou de visualiser directement les données, vous interagissez avec elles via des méthodes spécifiques. Cela garantit que les données sont protégées contre les modifications non intentionnelles.

Exemple :

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Attribut privé (remarquez le double underscore)
    
    def get_age(self):
        return self.__age  # Une méthode pour accéder à l'attribut privé age
```

Dans cet exemple, `__age` est gardé privé, et nous pouvons uniquement obtenir l'âge en utilisant la méthode `get_age()`. Cela garantit que `age` n'est pas modifié accidentellement de manière à causer des problèmes.

### Qu'est-ce que l'abstraction et en quoi est-elle différente de l'encapsulation ?

L'abstraction vous permet de montrer uniquement les détails importants d'un objet ou d'un système, tout en cachant les parties complexes que l'utilisateur n'a pas besoin de voir.

Pensez à cela comme à conduire une voiture, vous avez seulement besoin de savoir comment utiliser le volant, les vitesses, la pédale de gaz et les freins pour conduire. Vous n'avez pas besoin de comprendre comment le moteur fonctionne en interne.

En programmation, l'abstraction vous aide à vous concentrer sur ce que quelque chose fait, et non sur la manière dont cela fonctionne en interne.

**Exemple :** Supposons que vous utilisez une classe `Car`. L'abstraction vous permet de démarrer la voiture sans connaître tous les détails mécaniques :

```python
class Car:
    def start_engine(self):
        print("Engine started")
    
    def drive(self):
        print("Car is driving")

# L'utilisateur interagit avec la voiture sans connaître le fonctionnement du moteur
my_car = Car()
my_car.start_engine()
my_car.drive()
```

Ici, vous n'avez pas besoin de vous soucier de la manière dont la méthode `start_engine` fonctionne en interne, vous l'utilisez simplement !

Différence clé :

* Encapsulation : Se concentre sur le regroupement des données et la restriction de l'accès.
    
* Abstraction : Se concentre sur la dissimulation de la complexité et l'exposition uniquement des détails nécessaires.
    

### Qu'est-ce que l'héritage en POO ?

L'héritage vous permet de créer une nouvelle classe en utilisant une classe existante. La nouvelle classe (appelée classe enfant) obtient tous les attributs et méthodes de la classe existante (appelée classe parente).

Cela vous permet de réutiliser le code et de construire sur ce que vous avez déjà écrit sans tout recommencer.

Exemple :

```python
# Classe parente
class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # Il s'agit d'un attribut (marque)
    
    def start(self):
        print(f"{self.brand} vehicle started")  # Il s'agit d'une méthode

# Classe enfant qui hérite de Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # Hérite de la marque de Vehicle (classe parente)
        self.model = model  # Ajoute un nouvel attribut spécifique à Car

    def display_info(self):
        print(f"Car: {self.brand}, Model: {self.model}")

# Création d'un objet de la classe Car
my_car = Car("IVM", "Ikenga")
my_car.start()  # Sortie : IVM vehicle started
my_car.display_info()  # Sortie : Car: IVM, Model: Ikenga
```

Dans cet exemple, `Vehicle` est la classe parente, et `Car` est la classe enfant. `Car` hérite de la `brand` et de la méthode `start()` de `Vehicle`, mais elle a également son propre attribut (`model`) et sa propre méthode (`display_info()`).

L'héritage facilite la création de classes plus spécialisées (comme `Car`) basées sur une classe générale (comme `Vehicle`).

### Qu'est-ce que le polymorphisme ?

Le polymorphisme permet à différents types d'objets de répondre à la même action de manière unique. C'est comme si les chats et les chiens faisaient des sons, mais chacun fait un son différent lorsque vous leur demandez !

Le polymorphisme peut être réalisé par le biais de la surcharge de méthode (quand une classe enfant a une méthode avec le même nom qu'une méthode dans sa classe parente mais fournit sa propre implémentation).

Exemple de surcharge de méthode :

```python
# Classe parente
class Animal:
    def sound(self):
        return "Some generic animal sound"

# Classe enfant Dog surchargeant la méthode sound
class Dog(Animal):
    def sound(self):
        return "Bark"

# Classe enfant Cat surchargeant la méthode sound
class Cat(Animal):
    def sound(self):
        return "Meow"

# Création d'instances de chaque classe
my_dog = Dog()
my_cat = Cat()

# Appel de la méthode sound
print(my_dog.sound())  # Sortie : Bark
print(my_cat.sound())  # Sortie : Meow
```

Dans cet exemple :

* `Animal` est la classe parente, et elle a une méthode appelée `sound()`.
    
* `Dog` et `Cat` sont des classes enfants de `Animal`, et elles surchargent la méthode `sound()` pour fournir leur propre son spécifique.
    
* Lorsque vous appelez `sound()` sur un chien, il retourne "Bark", et pour un chat, il retourne "Meow."
    

C'est le polymorphisme en action, différents objets (Dog, Cat) répondant à la même méthode (`sound()`) de différentes manières.

C'est un outil puissant qui aide à créer un code flexible et facile à maintenir !

## Qu'est-ce que la surcharge de méthode ?

La surcharge de méthode se produit lorsque vous créez plusieurs méthodes avec le même nom, mais avec différents types de paramètres à l'intérieur de la même classe.

Bien que Python ne supporte pas la surcharge de méthode traditionnelle, vous pouvez imiter un comportement similaire en utilisant des arguments/paramètres par défaut ou en gérant plusieurs arguments à l'intérieur de la méthode.

Exemple 1 : Utilisation de paramètres par défaut

```python
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Créer une instance de Calculator
calc = Calculator()

# Appeler la méthode add avec différents nombres d'arguments
print(calc.add(5))        # Sortie : 5 (a = 5, b et c par défaut à 0)
print(calc.add(5, 10))    # Sortie : 15 (a = 5, b = 10, c par défaut à 0)
print(calc.add(5, 10, 15))# Sortie : 30 (a = 5, b = 10, c = 15)
```

Dans cet exemple, la méthode `add` a un paramètre requis (`a`) et deux paramètres optionnels (`b` et `c`) avec des valeurs par défaut de `0`.

En changeant le nombre d'arguments que vous passez lors de l'appel de la méthode, vous pouvez obtenir un effet de surcharge de méthode.

Exemple 2 : Utilisation de `*args` pour des paramètres dynamiques

```python
class Calculator:
    def add(self, *args):
        return sum(args)

# Créer une instance de Calculator
calc = Calculator()

# Appeler la méthode add avec différents nombres d'arguments
print(calc.add(5))           # Sortie : 5 (additionne juste un nombre)
print(calc.add(5, 10))       # Sortie : 15 (additionne deux nombres)
print(calc.add(5, 10, 15))   # Sortie : 30 (additionne trois nombres)
```

Dans cet exemple, la méthode `add` peut gérer n'importe quel nombre d'arguments grâce à `*args`, vous permettant d'appeler la méthode avec un ou plusieurs paramètres. Elle additionne tous les nombres qui lui sont passés.

## Qu'est-ce qu'un constructeur en POO ?

Un constructeur est une méthode spéciale qui s'exécute automatiquement lorsque vous créez un nouvel objet à partir d'une classe. Il aide à définir les valeurs initiales de l'objet (comme définir le nom ou l'âge d'une personne).

En Python, la méthode constructeur est nommée `__init__`, qui signifie "initialiser".

Exemple :

```python
class Student:
    def __init__(self, name, grade):  # La méthode constructeur
        self.name = name  # Définir le nom lorsque l'objet est créé
        self.grade = grade  # Définir la note lorsque l'objet est créé

# Création d'un nouvel objet Student
student1 = Student("Alice", "A")

# Accéder aux détails de l'étudiant
print(student1.name)  # Sortie : Alice
print(student1.grade)  # Sortie : A
```

Dans cet exemple, la méthode `__init__` attribue automatiquement les valeurs pour `name` et `grade` lorsque nous créons un objet `Student` (comme `student1`). Lorsque vous imprimez `student1.name`, il affiche "Alice", et `student1.grade` affiche "A."

Cela aide à configurer chaque objet étudiant avec des détails différents lorsque cela est nécessaire !

## Qu'est-ce qu'un destructeur en POO ?

Un destructeur est une méthode qui est appelée lorsque qu'un objet est détruit. En Python, le destructeur est défini en utilisant `__del__`.

Exemple :

```python
class Demo:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

obj = Demo()
del obj  # Appel explicite du destructeur
```

Dans cet exemple, la classe `Demo` a un constructeur (`__init__`) qui imprime "Constructor called" lorsqu'un objet est créé, et un destructeur (`__del__`) qui imprime "Destructor called" lorsque l'objet est supprimé.

Le `del obj` déclenche explicitement le destructeur pour nettoyer l'objet.

## Qu'est-ce qu'une classe en POO ?

Une classe est comme un modèle pour créer des objets en programmation. Elle décrit quelles propriétés (appelées attributs) et actions (appelées méthodes) les objets auront. Pensez à une classe comme à une recette qui vous dit comment créer quelque chose, comme une voiture.

Exemple :

```python
 class Car:
    def __init__(self, make, model):
        self.make = make  # La marque de la voiture, comme IVM
        self.model = model  # Le modèle spécifique, comme Ikenga
    
    def display_info(self):
        return f"Car: {self.make}, Model: {self.model}"  # Affiche les informations de la voiture
```

Dans cet exemple :

* `Car` est la classe qui décrit ce qu'est une voiture.
    
* `make` et `model` sont des attributs qui contiennent des informations sur la voiture.
    
* `display_info` est une méthode qui nous indique comment obtenir des détails sur la voiture.
    

Lorsque nous créons un objet voiture à partir de cette classe, il aura sa propre marque et son propre modèle, tout comme les voitures réelles !

## Qu'est-ce qu'un objet en POO ?

Un objet est un exemple spécifique d'une classe. Pensez à cela comme à un article de la vie réelle qui a certaines caractéristiques définies par la classe. Lorsque vous créez un objet, vous lui donnez des valeurs réelles pour ses propriétés.

```python
my_car = Car("IVM", "Ikenga")
print(my_car.display_info())  # Cela affichera : Car: IVM, Model: Ikenga
```

Dans cet exemple, `my_car` est un objet créé à partir de la classe `Car`.

## Qu'est-ce qu'une méthode statique ?

Il s'agit d'une méthode qui appartient à une classe, et non à une instance (objet) de cette classe. Contrairement aux autres méthodes, les méthodes statiques n'ont pas besoin d'accéder aux données spécifiques à l'instance (attributs) ou aux données spécifiques à la classe.

Vous pouvez appeler une méthode statique directement à partir de la classe sans créer d'objet.

Exemple :

```python
class MathOperations:
    @staticmethod  # Cela indique à Python qu'il s'agit d'une méthode statique
    def add(a, b):
        return a + b

# Nous n'avons pas besoin de créer un objet de la classe pour utiliser la méthode statique
result = MathOperations.add(5, 3)
print(result)  # Sortie : 8
```

Dans cet exemple, `@staticmethod` est utilisé pour définir la méthode comme statique. Vous pouvez appeler `MathOperations.add()` directement en utilisant le nom de la classe, sans créer d'objet de `MathOperations`.

## Quelle est la différence entre une variable de classe et une variable d'instance ?

Une variable de classe est partagée entre toutes les instances d'une classe, tandis qu'une variable d'instance est spécifique à chaque objet et définie à l'intérieur des méthodes, généralement dans le constructeur.

Exemple :

```python
class MyClass:
    class_var = "I am a class variable"
    
    def __init__(self, instance_var):
        self.instance_var = instance_var  # Variable d'instance
```

Dans cet exemple, une classe `MyClass` a une variable de classe `class_var` qui est partagée par toutes les instances, et une variable d'instance `instance_var` qui est unique à chaque objet créé à partir de la classe.

## Python supporte-t-il l'héritage multiple ?

Oui, Python permet l'héritage multiple, où une classe peut hériter de plus d'une classe parente.

Exemple :

```python
class Parent1:
    def display(self):
        print("Parent1")

class Parent2:
    def display(self):
        print("Parent2")

class Child(Parent1, Parent2):
    pass

child = Child()
child.display()  # L'ordre de résolution des méthodes détermine quelle méthode display() est appelée
```

Dans cet exemple, la classe `Child` hérite à la fois de `Parent1` et `Parent2`, et en raison de l'ordre de résolution des méthodes (MRO), `Child` appellera la méthode `display()` de `Parent1` en premier.

## Quelle est la différence entre une classe abstraite et une interface ?

Une classe abstraite est un type spécial de classe dont vous ne pouvez pas créer d'objet. Elle peut avoir à la fois des méthodes incomplètes (appelées méthodes abstraites) qui n'ont aucune implémentation, ainsi que des méthodes entièrement implémentées qui ont du code.

Une interface est comme un contrat qui définit des méthodes qui doivent être implémentées par toute classe qui l'utilise. En Python, nous réalisons des interfaces à travers des classes de base abstraites (ABC), qui ne contiennent que des méthodes abstraites. Elles n'ont aucune implémentation.

Exemple simple pour illustrer les concepts :

```python
from abc import ABC, abstractmethod

# Classe abstraite
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Il s'agit d'une méthode abstraite, sans implémentation

    def sleep(self):
        return "Sleeping..."  # Il s'agit d'une méthode régulière avec implémentation

# Sous-classe qui implémente la méthode abstraite
class Dog(Animal):
    def sound(self):
        return "Bark"  # Implémentation de la méthode abstraite

class Cat(Animal):
    def sound(self):
        return "Meow"  # Une autre implémentation de la méthode abstraite

# Utilisation des classes
my_dog = Dog()
print(my_dog.sound())  # Sortie : Bark
print(my_dog.sleep())  # Sortie : Sleeping...

my_cat = Cat()
print(my_cat.sound())  # Sortie : Meow
print(my_cat.sleep())  # Sortie : Sleeping...
```

Dans cet exemple, une classe abstraite `Animal` avec une méthode abstraite `sound`, et deux sous-classes, `Dog` et `Cat`, implémentent la méthode `sound`, démontrant l'utilisation de classes abstraites et de la surcharge de méthode en Python.

## Conclusion

Comprendre ces principes de la POO est crucial pour tout développeur. Cela constitue la base de la plupart des langages de programmation modernes.

En maîtrisant les concepts clés et en étant préparé aux questions d'entretien, vous ne construirez pas seulement de meilleurs logiciels, mais vous augmenterez également vos chances de décrocher votre prochain rôle de développeur.

Si vous avez trouvé ce guide utile, veuillez lui donner un like. Vous pouvez me suivre sur [X](https://x.com/casweb_dev) pour plus d'articles perspicaces.