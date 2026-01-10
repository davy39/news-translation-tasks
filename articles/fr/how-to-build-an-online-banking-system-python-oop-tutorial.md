---
title: Comment construire un système de banque en ligne – Tutoriel Python sur la programmation
  orientée objet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-03-20T18:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-online-banking-system-python-oop-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/OOP_in_Python.png
tags:
- name: Object Oriented Programming
  slug: object-oriented-programming
- name: Python
  slug: python
seo_title: Comment construire un système de banque en ligne – Tutoriel Python sur
  la programmation orientée objet
seo_desc: "By Jacob Isah \nObject-Oriented Programming (OOP) is a fundamental concept\
  \ in software engineering that allows software engineers to structure code in a\
  \ more organized and modular way. \nPython, with its clear and concise syntax, is\
  \ an excellent langua..."
---

Par Jacob Isah

La programmation orientée objet (POO) est un concept fondamental en ingénierie logicielle qui permet aux ingénieurs logiciels de structurer le code de manière plus organisée et modulaire.

Python, avec sa syntaxe claire et concise, est un excellent langage pour apprendre et implémenter les principes de la POO.

Dans cet article, nous allons examiner les bases de la POO en Python en construisant un système bancaire en ligne simple.

## Aperçu des concepts de la POO

Avant de commencer à coder, comprenons les concepts clés de la POO :

* **Classes** : Les classes sont des plans pour créer des objets. Elles définissent les attributs (données) et les méthodes (fonctions) que les objets de cette classe auront.
* **Objets** : Les objets sont des instances de classes. Ils représentent des entités du monde réel et encapsulent des données et des comportements.
* **Héritage** : L'héritage permet à une classe (sous-classe) d'hériter des attributs et des méthodes d'une autre classe (superclasse). Il favorise la réutilisation du code et soutient les relations hiérarchiques entre les classes.
* **Constructeur** : Un constructeur (`__init__()`) est un type spécial de méthode qui est automatiquement appelé lorsqu'un objet d'une classe est créé. Son but principal est d'initialiser le nouvel objet, en définissant les valeurs initiales pour ses attributs ou en effectuant toute tâche de configuration nécessaire.

## Comment construire un système de banque en ligne

Commençons par créer la structure de base pour notre système bancaire en ligne en utilisant les principes de la POO.

### Comment créer une classe et un constructeur

Créons une classe et initialisons la classe avec le constructeur :

```python
class Account:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
```

Dans l'exemple ci-dessus :

* Le mot-clé `class` déclare une classe `Account`.
* La méthode `__init__()` est le constructeur, défini avec la notation spéciale double underscore au début et à la fin.
* `self` est une référence à l'instance de la classe. C'est le premier paramètre de toutes les méthodes d'instance en Python.
* `name` est le nom du titulaire du compte.
* `account_number` est un identifiant unique pour le compte d'épargne, et `balance` sont des paramètres passés au constructeur.
* À l'intérieur du constructeur, `self.name`, `self.account_number`, et `self.balance` sont des attributs de la classe `Account` qui sont initialisés avec les valeurs de `name`, `account_number` et `balance`, respectivement.

Les constructeurs peuvent effectuer diverses tâches telles que l'initialisation des attributs, l'ouverture de connexions, le chargement de données, et plus encore. Ils sont essentiels pour garantir que les objets sont correctement configurés et prêts à l'emploi dès leur création.

### Comment créer des méthodes (fonctions)

La prochaine chose à faire est d'écrire les différentes méthodes pour notre classe `Account`. Les utilisateurs doivent pouvoir déposer et retirer des fonds.

#### Comment créer une méthode de dépôt

```python
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} a déposé {amount} $. Solde actuel est : {self.balance}")
```

Dans l'exemple ci-dessus :

* La méthode `deposit` permet aux utilisateurs d'ajouter des fonds à leur compte.
* La méthode prend un paramètre supplémentaire `amount`, qui est le montant à déposer.
* À l'intérieur de la méthode, le `amount` est ajouté au solde actuel en utilisant `self.balance += amount`.
* Un message est imprimé montrant le nom du déposant et le montant déposé, et le solde est mis à jour.

#### Comment créer une méthode de retrait

```python
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name} a retiré {amount} $. Solde actuel est : {self.balance}")
        else:
            print("Vous n'avez pas assez de fonds pour retirer.")
```

Dans l'exemple ci-dessus :

* La méthode `withdraw` permet aux utilisateurs de retirer des fonds de leur compte.
* La méthode prend également un paramètre `amount` qui est le montant que notre utilisateur souhaite retirer.
* La méthode vérifie si le solde du compte (`self.balance`) est supérieur ou égal au montant que notre utilisateur souhaite retirer.
* Si le solde est suffisant, le montant du retrait est soustrait du solde en utilisant `self.balance -= amount`.
* Si le solde n'est pas suffisant, un message indiquant « Vous n'avez pas assez de fonds pour retirer. » est imprimé pour l'utilisateur.

### Comment fonctionne l'héritage

Ayant expliqué l'héritage ci-dessus, voyons comment il fonctionne en code. Nous allons créer une classe qui hérite de la classe `Account`.

Notez que la classe `Account` est la superclasse, tandis que la classe `Savings_Account` est une sous-classe, également connue sous le nom de classe enfant.

```python
class Savings_Account(Account):
    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate
```

Dans le code ci-dessus :

* La méthode `__init__` est le constructeur pour la classe `Savings_Account`.
* Elle accepte quatre paramètres : `name` qui est le nom du titulaire du compte, `account_number`, qui est un identifiant unique pour le compte d'épargne, `balance`, qui est le solde initial du compte, et `interest_rate`, qui est le taux d'intérêt annuel (exprimé sous forme décimale) pour le compte.
* La ligne `super().__init__(name, account_number, balance)` appelle le constructeur de la classe parente (`Account`) pour initialiser le numéro de compte et le solde.
* La ligne `self.interest_rate = interest_rate` définit le taux d'intérêt spécifique au compte d'épargne. Il n'est pas hérité.

### Comment créer une méthode `add_interest`

```python
def add_interest(self):
    interest = self.balance * self.interest_rate
    self.deposit(interest)
```

Dans l'exemple ci-dessus :

* La méthode `add_interest` calcule et ajoute des intérêts au solde du compte.
* La méthode calcule les intérêts en multipliant le solde actuel (`self.balance`) par le taux d'intérêt (`self.interest_rate`).
* Le résultat est stocké dans la variable `interest`.
* Enfin, la ligne `self.deposit(interest)` appelle la méthode `deposit` (définie dans la classe parente `Account`) pour ajouter le montant des intérêts au solde du compte.

### Comment créer et utiliser des objets

Votre classe n'est qu'un modèle. Vous devez créer un objet pour que votre classe fonctionne.

Maintenant, créons des objets à partir de nos classes et interagissons avec eux.

```python
account1 = Account("John Doe", "123456", 1000)
account1.deposit(500)
account1.withdraw(200)
print()

savings_account = Savings_Account("John Doe", "789012", 2000, 0.05)
savings_account.deposit(1000)
savings_account.add_interest()
savings_account.withdraw(500)
savings_account.withdraw(1000)
```

Dans le code ci-dessus :

* Nous avons créé une instance `account1` de la classe `Account` et effectué des opérations de dépôt et de retrait.
* De même, nous avons créé une instance `savings_account` de la classe `Savings_Account` et démontré des opérations de dépôt, d'ajout d'intérêts et de retrait.

## Conclusion

La programmation orientée objet est un paradigme puissant qui permet aux ingénieurs logiciels d'écrire du code réutilisable, maintenable et évolutif.

La simplicité de Python en fait un excellent choix pour apprendre et implémenter les concepts de la POO.

En construisant un système bancaire en ligne simple, je vous ai montré les concepts de base des classes, des objets et de l'héritage en Python.

Bon codage !