---
title: Programmation Orientée Objet en Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-02-02T15:24:30.000Z'
originalURL: https://freecodecamp.org/news/object-oriented-programming-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/02/oop--2-.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: Programmation Orientée Objet en Python
seo_desc: "Python is a fantastic programming language that allows you to use both\
  \ functional and object-oriented programming paradigms. \nPython programmers should\
  \ be able to use fundamental object-oriented programming concepts, whether they\
  \ are software develop..."
---

Python est un langage de programmation fantastique qui permet d'utiliser à la fois les paradigmes de programmation fonctionnelle et orientée objet. 

Les programmeurs Python doivent être capables d'utiliser les concepts fondamentaux de la programmation orientée objet, qu'ils soient développeurs de logiciels, ingénieurs en machine learning ou autre chose. 

Le système de programmation orientée objet de Python prend en charge les quatre aspects principaux d'un framework OOP générique : l'encapsulation, l'abstraction, l'héritage et le polymorphisme. 

Dans ce tutoriel, nous allons jeter un rapide coup d'œil à ces fonctionnalités et nous entraîner avec elles.

# Concepts de Programmation Orientée Objet en Python

## Qu'est-ce que les Classes et les Objets ?

Python, comme tout autre langage orienté objet, permet de définir des classes pour créer des objets. Les classes Python intégrées sont les types de données les plus courants en Python, tels que les chaînes de caractères, les listes, les dictionnaires, etc. 

Une classe est une collection de variables d'instance et de méthodes associées qui définissent un type d'objet particulier. Vous pouvez penser à une classe comme un plan ou un modèle d'objet. Les attributs sont les noms donnés aux variables qui composent une classe. 

Un objet est une instance de classe avec un ensemble défini de propriétés. Par conséquent, la même classe peut être utilisée pour construire autant d'objets que nécessaire.

Définissons une classe nommée _Book_ pour un logiciel de vente de librairie.

```py
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

```

La méthode spéciale `__init__`, également connue sous le nom de **Constructeur**, est utilisée pour initialiser la classe Book avec des attributs tels que le titre, la quantité, l'auteur et le prix. 

En Python, les classes intégrées sont nommées en minuscules, mais les classes définies par l'utilisateur sont nommées en Camel ou Snake case, avec la première lettre en majuscule.

Cette classe peut être instanciée en autant d'objets que nécessaire. Trois livres sont instanciés dans l'exemple de code suivant :

```python
book1 = Book('Book 1', 12, 'Author 1', 120)
book2 = Book('Book 2', 18, 'Author 2', 220)
book3 = Book('Book 3', 28, 'Author 3', 320)
```

book1, book2 et book3 sont des objets distincts de la classe _Book_. Le terme **self** dans les attributs fait référence aux instances correspondantes (objets).

```python
print(book1)
print(book2)
print(book3)
```

Sortie :

```bash
<__main__.Book object at 0x00000156EE59A9D0>
<__main__.Book object at 0x00000156EE59A8B0>
<__main__.Book object at 0x00000156EE59ADF0>
```

Lorsque les objets sont imprimés, la classe et l'emplacement mémoire des objets sont affichés. Nous ne pouvons pas nous attendre à ce qu'ils fournissent des informations spécifiques sur les qualités, telles que le titre, le nom de l'auteur, etc. Mais nous pouvons utiliser une méthode spécifique appelée `__repr__` pour cela. 

En Python, une méthode spéciale est une fonction définie qui commence et se termine par deux underscores et est invoquée automatiquement lorsque certaines conditions sont remplies.

```python
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


book1 = Book('Book 1', 12, 'Author 1', 120)
book2 = Book('Book 2', 18, 'Author 2', 220)
book3 = Book('Book 3', 28, 'Author 3', 320)

print(book1)
print(book2)
print(book3)

```

Sortie :

```bash
Book: Book 1, Quantity: 12, Author: Author 1, Price: 120
Book: Book 2, Quantity: 18, Author: Author 2, Price: 220
Book: Book 3, Quantity: 28, Author: Author 3, Price: 320
```

## Qu'est-ce que l'Encapsulation ?

L'encapsulation est le processus qui empêche les clients d'accéder à certaines propriétés, qui ne peuvent être accessibles que par des méthodes spécifiques. 

Les attributs privés sont des attributs inaccessibles, et le masquage d'informations est le processus qui consiste à rendre des attributs particuliers privés. Vous utilisez deux underscores pour déclarer des caractéristiques privées.

Introduisons un attribut privé appelé **`__discount`** dans la classe _Book_.

```python
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        self.__discount = 0.10

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"


book1 = Book('Book 1', 12, 'Author 1', 120)

print(book1.title)
print(book1.quantity)
print(book1.author)
print(book1.price)
print(book1.__discount)
```

Sortie :

```bash
Book 1
12
Author 1
120
Traceback (most recent call last):
  File "C:\Users\ashut\Desktop\Test\hello\test.py", line 19, in <module>
    print(book1.__discount)
AttributeError: 'Book' object has no attribute '__discount'
```

Nous pouvons voir que tous les attributs sont imprimés sauf l'attribut privé **`__discount`**. Vous utilisez des méthodes getter et setter pour accéder aux attributs privés. 

Dans l'exemple de code suivant, nous rendons la propriété price privée et nous utilisons une méthode setter pour assigner l'attribut discount et une fonction getter pour obtenir l'attribut price.

```python
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"

```

Cette fois, nous allons créer deux objets, l'un pour l'achat d'un seul livre et l'autre pour l'achat de livres en grande quantité. Lors de l'achat de livres en grande quantité, nous obtenons une remise de 20 %, nous allons donc utiliser la méthode **`set_discount()`** pour définir la remise à 20 % dans ce cas.

```python
single_book = Book('Two States', 1, 'Chetan Bhagat', 200)

bulk_books = Book('Two States', 25, 'Chetan Bhagat', 200)
bulk_books.set_discount(0.20)

print(single_book.get_price())
print(bulk_books.get_price())
print(single_book)
print(bulk_books)

```

Sortie :

```bash
200
160.0
Book: Two States, Quantity: 1, Author: Chetan Bhagat, Price: 200
Book: Two States, Quantity: 25, Author: Chetan Bhagat, Price: 160.0
```

## Qu'est-ce que l'Héritage ?

L'héritage est considéré comme la caractéristique la plus significative de l'OOP. La capacité d'une classe à hériter de méthodes et/ou de caractéristiques d'une autre classe est appelée héritage. 

La sous-classe ou classe enfant est la classe qui hérite. La superclasse ou classe parente est la classe à partir de laquelle les méthodes et/ou attributs sont hérités.

Deux nouvelles classes ont été ajoutées à notre logiciel de vente de librairie : une classe _Novel_ et une classe _Academic_. 

Nous pouvons voir que, qu'un livre soit classé comme roman ou académique, il peut avoir certains attributs similaires comme le titre et l'auteur, ainsi que des méthodes communes comme **`get_price()`** et **`set_discount()`**. Réécrire tout ce code pour chaque nouvelle classe est une perte de temps, d'efforts et de mémoire.

```python
class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

```

Créons des objets pour ces classes afin de les visualiser.

```python
novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)
```

Sortie :

```bash
Book: Two States, Quantity: 20, Author: Chetan Bhagat, Price: 160.0
Book: Python Foundations, Quantity: 12, Author: PSF, Price: 655
```

## Qu'est-ce que le Polymorphisme ?

Le terme '**polymorphisme**' vient de la langue grecque et signifie '_quelque chose qui prend plusieurs formes._' 

Le polymorphisme fait référence à la capacité d'une sous-classe à adapter une méthode qui existe déjà dans sa superclasse pour répondre à ses besoins. En d'autres termes, une sous-classe peut utiliser une méthode de sa superclasse telle quelle ou la modifier selon ses besoins.

```python
class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
```

La superclasse _Book_ a une méthode spécifique appelée `__repr__`. Cette méthode peut être utilisée par la sous-classe Novel de sorte qu'elle est appelée chaque fois qu'un objet est imprimé. 

La sous-classe _Academic_, en revanche, est définie avec sa propre fonction spéciale `__repr__` dans l'exemple de code ci-dessus. La sous-classe _Academic_ invoquera sa propre méthode en supprimant la même méthode présente dans sa superclasse, grâce au polymorphisme.

```python
novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)
```

Sortie :

```bash
Book: Two States, Quantity: 20, Author: Chetan Bhagat, Price: 160.0
Book: Python Foundations, Branch: IT, Quantity: 12, Author: PSF, Price: 655
```

## Qu'est-ce que l'Abstraction ?

L'abstraction n'est pas directement prise en charge en Python. Cependant, l'appel à une méthode magique permet l'abstraction. 

Si une méthode abstraite est déclarée dans une superclasse, les sous-classes qui héritent de la superclasse doivent avoir leur propre implémentation de la méthode. 

Une méthode abstraite d'une superclasse ne sera jamais appelée par ses sous-classes. Mais l'abstraction aide à maintenir une structure similaire dans toutes les sous-classes.

Dans notre classe parente _Book_, nous avons défini la méthode `__repr__`. Rendons cette méthode abstraite, obligeant chaque sous-classe à avoir sa propre méthode `__repr__`.

```python
from abc import ABC, abstractmethod


class Book(ABC):
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price
        self.__discount = None

    def set_discount(self, discount):
        self.__discount = discount

    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price

    @abstractmethod
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch

    def __repr__(self):
        return f"Book: {self.title}, Branch: {self.branch}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 655, 'IT')

print(novel1)
print(academic1)
```

Dans le code ci-dessus, nous avons hérité de la classe _ABC_ pour créer la classe _Book_. Nous avons rendu la méthode `__repr__` abstraite en ajoutant le décorateur **`@abstractmethod`**.

Lors de la création de la classe Novel, nous avons intentionnellement omis l'implémentation de la méthode `__repr__` pour voir ce qui se passe.

Sortie :

```bash
Traceback (most recent call last):
  File "C:\Users\ashut\Desktop\Test\hello\test.py", line 40, in <module>
    novel1 = Novel('Two States', 20, 'Chetan Bhagat', 200, 187)
TypeError: Can't instantiate abstract class Novel with abstract method __repr__

```

Nous obtenons une **TypeError** indiquant que nous ne pouvons pas instancier l'objet de la classe Novel. Ajoutons l'implémentation de la méthode `__repr__` et voyons ce qui se passe maintenant.

```python
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"
```

Sortie :

```bash
Book: Two States, Quantity: 20, Author: Chetan Bhagat, Price: 160.0
Book: Python Foundations, Branch: IT, Quantity: 12, Author: PSF, Price: 655
```

Maintenant, cela fonctionne bien.

## Surcharge de Méthode

Le concept de surcharge de méthode se trouve dans presque tous les langages de programmation bien connus qui suivent les concepts de programmation orientée objet. Il fait simplement référence à l'utilisation de plusieurs méthodes avec le même nom qui prennent divers nombres d'arguments au sein d'une seule classe.

Comprenons maintenant la surcharge de méthode à l'aide du code suivant :

```python
class OverloadingDemo:
    def add(self, x, y):
        print(x+y)

    def add(self, x, y, z):
        print(x+y+z)


obj = OverloadingDemo()
obj.add(2, 3)

```

Sortie :

```bash
Traceback (most recent call last):
  File "C:\Users\ashut\Desktop\Test\hello\setup.py", line 10, in <module>
    obj.add(2, 3)
TypeError: add() missing 1 required positional argument: 'z'
```

Vous vous demandez probablement pourquoi cela s'est produit. En conséquence, l'erreur est affichée car Python ne se souvient que de la définition la plus récente de add(self, x, y, z), qui prend trois paramètres en plus de self. Par conséquent, trois arguments doivent être passés à la méthode `add()` lorsqu'elle est appelée. En d'autres termes, elle ignore la définition précédente de add().

Ainsi, Python **ne supporte pas** la surcharge de méthode par défaut.

## Redéfinition de Méthode

Lorsque une méthode avec le même nom et les mêmes arguments est utilisée à la fois dans une classe dérivée et une classe de base ou super classe, nous disons que la méthode de la classe dérivée "remplace" la méthode fournie dans la classe de base. 

Lorsque la méthode redéfinie est appelée, la méthode de la classe dérivée est toujours invoquée. La méthode qui était utilisée dans la classe de base est maintenant masquée.

```python
class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()
```

Sortie :

```bash
I am parent class
I am child class
```

Dans le code ci-dessus, lorsque la méthode **`call_me()`** a été appelée sur l'objet enfant, la méthode `call_me()` de la classe enfant a été invoquée. Nous pouvons invoquer la méthode `call_me()` de la classe parente à partir de la classe enfant en utilisant **`super()`**, comme ceci :

```python
class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")
        super().call_me()

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()
```

Sortie :

```bash
I am parent class
I am child class
I am parent class
```

## Conclusion

Dans cet article, nous avons couvert ce que signifient les classes et les objets. Nous avons également couvert les quatre piliers de la Programmation Orientée Objet. 

En plus de cela, nous avons également abordé deux sujets importants : la surcharge de méthode et la redéfinition de méthode.

Merci d'avoir lu !

<a class="cta-button" href="https://www.getrevue.co/profile/ashutoshkrris" target="_blank">S'abonner à ma newsletter</a>