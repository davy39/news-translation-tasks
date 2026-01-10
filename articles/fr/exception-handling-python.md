---
title: 'Comment gérer les exceptions en Python : une introduction visuelle détaillée'
subtitle: ''
author: Estefania Cassingena Navone
co_authors: []
series: null
date: '2019-12-22T15:27:27.000Z'
originalURL: https://freecodecamp.org/news/exception-handling-python
coverImage: https://www.freecodecamp.org/news/content/images/2019/12/Exception-Handling-in-Python.png
tags:
- name: Exception Handling
  slug: exception-handling
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: 'Comment gérer les exceptions en Python : une introduction visuelle détaillée'
seo_desc: 'Welcome! In this article, you will learn how to handle exceptions in Python.

  In particular, we will cover:


  Exceptions

  The purpose of exception handling

  The try clause

  The except clause

  The else clause

  The finally clause

  How to raise exceptions


  Are ...'
---

Bienvenue ! Dans cet article, vous apprendrez à gérer les exceptions en Python.

**En particulier, nous aborderons :**

* Les exceptions
* Le but de la gestion des exceptions
* La clause try
* La clause except
* La clause else
* La clause finally
* Comment lever des exceptions

**Êtes-vous prêt ? Commençons ! f600**

## 1️⃣ Introduction aux exceptions

Nous commencerons par les exceptions :

* **Qu'est-ce que** c'est ? 
* **Pourquoi** sont-elles pertinentes ? 
* **Pourquoi** devriez-vous les gérer ?

Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#exceptions) :

> Les erreurs détectées pendant l'exécution sont appelées **_exceptions_** et ne sont pas nécessairement fatales.

**Les exceptions sont levées lorsque le programme rencontre une erreur pendant son exécution.** Elles perturbent le flux normal du programme et le terminent généralement de manière abrupte. Pour éviter cela, vous pouvez les capturer et les gérer de manière appropriée.

Vous les avez probablement vues pendant vos projets de programmation. 

Si vous avez déjà essayé de diviser par zéro en Python, vous devez avoir vu ce message d'erreur :

```python
>>> a = 5/0
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a = 5/0
ZeroDivisionError: division by zero
```

Si vous avez essayé d'indexer une chaîne avec un index invalide, vous avez définitivement obtenu ce message d'erreur :

```python
>>> a = "Hello, World"
>>> a[456]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[456]
IndexError: string index out of range
```

Ce sont des exemples d'exceptions.

### f4e5 Exceptions courantes

Il existe de nombreux types d'exceptions différents, et elles sont toutes levées dans des situations particulières. Certaines des exceptions que vous verrez probablement lors de vos projets sont :

* **IndexError** - levée lorsque vous essayez d'indexer une liste, un tuple ou une chaîne au-delà des limites autorisées. Par exemple :

```python
>>> num = [1, 2, 6, 5]
>>> num[56546546]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num[56546546]
IndexError: list index out of range
```

* **KeyError** - levée lorsque vous essayez d'accéder à la valeur d'une clé qui n'existe pas dans un dictionnaire. Par exemple :

```python
>>> students = {"Nora": 15, "Gino": 30}
>>> students["Lisa"]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    students["Lisa"]
KeyError: 'Lisa'
```

* **NameError** - levée lorsqu'un nom que vous référencez dans le code n'existe pas. Par exemple :

```python
>>> a = b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a = b
NameError: name 'b' is not defined
```

* **TypeError** - levée lorsqu'une opération ou une fonction est appliquée à un objet d'un type inapproprié. Par exemple :

```python
>>> (5, 6, 7) * (1, 2, 3)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    (5, 6, 7) * (1, 2, 3)
TypeError: can't multiply sequence by non-int of type 'tuple'
```

* **ZeroDivisionError** - levée lorsque vous essayez de diviser par zéro.

```python
>>> a = 5/0
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a = 5/0
ZeroDivisionError: division by zero
```

f4a1 **Conseils :** Pour en savoir plus sur d'autres types d'exceptions intégrées, veuillez [vous référer à cet article](https://docs.python.org/3/library/exceptions.html) dans la documentation Python.

### f4e4 **Anatomie d'une exception**

Je suis sûr que vous avez remarqué un schéma général dans ces messages d'erreur. Décomposons leur structure générale pièce par pièce :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-8.png)

Tout d'abord, nous trouvons cette ligne (voir ci-dessous). Un **traceback** est essentiellement une liste détaillant les appels de fonction qui ont été faits avant que l'exception ne soit levée. 

Le traceback vous aide pendant le processus de débogage car vous pouvez analyser la séquence des appels de fonction qui ont abouti à l'exception :

```python
Traceback (most recent call last):
```

Ensuite, nous voyons cette ligne (voir ci-dessous) avec le chemin vers le fichier et la ligne qui a levé l'exception. Dans ce cas, le chemin était le shell Python <pyshell#0> puisque l'exemple a été exécuté directement dans IDLE.

```python
File "<pyshell#0>", line 1, in <module>
   a - 5/0
```

**f4a1 Conseil :** Si la ligne qui a levé l'exception appartient à une fonction, <module> est remplacé par le nom de la fonction.

Enfin, nous voyons un message descriptif détaillant le type d'exception et fournissant des informations supplémentaires pour nous aider à déboguer le code :

```
NameError: name 'a' is not defined
```

## 2️⃣ Gestion des exceptions : but et contexte

Vous pourriez demander : pourquoi devrais-je gérer les exceptions ? Pourquoi est-ce utile pour moi ? En gérant les exceptions, vous pouvez fournir un flux d'exécution alternatif pour éviter que votre programme ne plante de manière inattendue.

### f4e5 Exemple : entrée utilisateur

Imaginez ce qui se passerait si un utilisateur travaillant avec votre programme entre une entrée invalide. Cela lèverait une exception car une opération invalide a été effectuée pendant le processus. 

Si votre programme ne gère pas cela correctement, il plantera soudainement et l'utilisateur aura une expérience très décevante avec votre produit.

**Mais si vous gérez l'exception, vous pourrez fournir une alternative pour améliorer l'expérience de l'utilisateur.** 

Peut-être pourriez-vous afficher un message descriptif demandant à l'utilisateur d'entrer une entrée valide, ou vous pourriez fournir une valeur par défaut pour l'entrée. Selon le contexte, vous pouvez choisir quoi faire lorsque cela se produit, et c'est la magie de la gestion des erreurs. Cela peut sauver la journée lorsque des choses inattendues se produisent. f31ff600

### f4e4 Que se passe-t-il en coulisses ?

En gros, lorsque nous gérons une exception, nous disons au programme quoi faire si l'exception est levée. Dans ce cas, le flux "alternatif" d'exécution viendra à la rescousse. Si aucune exception n'est levée, le code s'exécutera comme prévu.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-10.png)

## 3️⃣ C'est l'heure de coder : l'instruction try ... except

Maintenant que vous savez ce que sont les exceptions et pourquoi vous devriez les gérer, nous allons commencer à plonger dans les outils intégrés que le langage Python offre à cet effet. 

**Tout d'abord, nous avons l'instruction la plus basique : try ... except.**

Illustrons cela avec un exemple simple. Nous avons ce petit programme qui demande à l'utilisateur d'entrer le nom d'un étudiant pour afficher son âge :

```python
students = {"Nora": 15, "Gino": 30}

def print_student_age():
    name = input("Veuillez entrer le nom de l'étudiant : ")
    print(students[name])

print_student_age()
```

Remarquez comment nous ne validons pas l'entrée utilisateur pour le moment, donc l'utilisateur pourrait entrer des valeurs invalides (noms qui ne sont pas dans le dictionnaire) et les conséquences seraient catastrophiques car le programme planterait si une KeyError est levée :

```python
# Entrée utilisateur
Veuillez entrer le nom de l'étudiant : "Daniel"

# Message d'erreur
Traceback (most recent call last):
  File "<path>", line 15, in <module>
    print_student_age()
  File "<path>", line 13, in print_student_age
    print(students[name])
KeyError: '"Daniel"'
```

### f4e5 Syntaxe

Nous pouvons gérer cela élégamment en utilisant try ... except. Voici la syntaxe de base :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-11.png)

Dans notre exemple, nous ajouterions l'instruction try ... except dans la fonction. Décomposons cela pièce par pièce :

```python
students = {"Nora": 15, "Gino": 30}

def print_student_age():
    while True:
        try:
            name = input("Veuillez entrer le nom de l'étudiant : ")
            print(students[name])
            break
        except:
            print("Ce nom n'est pas enregistré")
    

print_student_age()
```

Si nous "zoomons", nous voyons l'instruction try ... except :

```
try:
	name = input("Veuillez entrer le nom de l'étudiant : ")
	print(students[name])
	break
except:
	print("Ce nom n'est pas enregistré")
```

* Lorsque la fonction est appelée, la clause try s'exécutera. Si aucune exception n'est levée, le programme s'exécutera comme prévu. 
* Mais si une exception est levée dans la clause try, le flux d'exécution sautera immédiatement à la clause except pour gérer l'exception.

**f4a1 Note :** Ce code est contenu dans une boucle while pour continuer à demander l'entrée utilisateur si la valeur est invalide. Voici un exemple :

```python
Veuillez entrer le nom de l'étudiant : "Lulu"
Ce nom n'est pas enregistré
Veuillez entrer le nom de l'étudiant : 
```

C'est génial, n'est-ce pas ? Maintenant, nous pouvons continuer à demander l'entrée utilisateur si la valeur est invalide. 

Pour le moment, nous gérons toutes les exceptions possibles avec la même clause except. Mais que faire si nous voulons gérer uniquement un type spécifique d'exception ? Voyons comment nous pourrions faire cela.

### f4e4 Capture d'exceptions spécifiques

Puisque tous les types d'exceptions ne sont pas gérés de la même manière, nous pouvons spécifier quelles exceptions nous souhaitons gérer avec cette syntaxe :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-15.png)

Voici un exemple. Nous gérons l'exception ZeroDivisionError au cas où l'utilisateur entre zéro comme dénominateur :

```python
def divide_integers():
    while True:
        try:
            a = int(input("Veuillez entrer le numérateur : "))
            b = int(input("Veuillez entrer le dénominateur : "))
            print(a / b)
        except ZeroDivisionError:
            print("Veuillez entrer un dénominateur valide.")


divide_integers()
```

Voici le résultat :

```python
# Première itération
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 0
Veuillez entrer un dénominateur valide. 

# Deuxième itération
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 2
2.5
```

Nous gérons cela correctement. Mais... si un autre type d'exception est levé, le programme ne le gérera pas élégamment. 

Voici un exemple de ValueError car l'une des valeurs est un float, pas un int :

```python
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 0.5
Traceback (most recent call last):
  File "<path>", line 53, in <module>
    divide_integers()
  File "<path>", line 47, in divide_integers
    b = int(input("Veuillez entrer le dénominateur : "))
ValueError: invalid literal for int() with base 10: '0.5'
```

Nous pouvons personnaliser la manière dont nous gérons différents types d'exceptions.

### f4e5 Clauses except multiples

Pour ce faire, nous devons ajouter plusieurs clauses `except` pour gérer différents types d'exceptions différemment. 

Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) :

> Une instruction try peut avoir **plus d'une clause except**, pour spécifier des gestionnaires pour différentes exceptions. **Au plus un gestionnaire sera exécuté.**

Dans cet exemple, nous avons deux clauses except. L'une d'elles gère ZeroDivisionError et l'autre gère ValueError, les deux types d'exceptions qui pourraient être levées dans ce bloc try. 

```
def divide_integers():
    while True:
        try:
            a = int(input("Veuillez entrer le numérateur : "))
            b = int(input("Veuillez entrer le dénominateur : "))
            print(a / b)
        except ZeroDivisionError:
            print("Veuillez entrer un dénominateur valide.")
        except ValueError:
            print("Les deux valeurs doivent être des entiers.")


divide_integers() 
```

f4a1 **Conseil :** Vous devez déterminer quels types d'exceptions pourraient être levées dans le bloc try pour les gérer de manière appropriée.

### f4e4 Exceptions multiples, une clause except

Vous pouvez également choisir de gérer différents types d'exceptions avec la même clause except. 

Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) :

> Une clause except peut nommer **plusieurs exceptions** sous la forme d'un tuple entre parenthèses.

Voici un exemple où nous capturons deux exceptions (ZeroDivisionError et ValueError) avec la même clause `except` :

```python
def divide_integers():
    while True:
        try:
            a = int(input("Veuillez entrer le numérateur : "))
            b = int(input("Veuillez entrer le dénominateur : "))
            print(a / b)
        except (ZeroDivisionError, ValueError):
            print("Veuillez entrer des entiers valides.")

divide_integers()
```

La sortie serait la même pour les deux types d'exceptions car elles sont gérées par la même clause except :

```python
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 0
Veuillez entrer des entiers valides.
```

```python
Veuillez entrer le numérateur : 0.5
Veuillez entrer des entiers valides.
Veuillez entrer le numérateur : 
```

### f4e5 Gestion des exceptions levées par des fonctions appelées dans la clause try

Un aspect intéressant de la gestion des exceptions est que si une exception est levée dans une fonction qui a été appelée précédemment dans la clause try d'une autre fonction et que la fonction elle-même ne la gère pas, l'appelant la gérera s'il existe une clause except appropriée. 

Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) :

> Les gestionnaires d'exceptions ne gèrent pas seulement les exceptions si elles se produisent immédiatement dans la clause try, mais aussi **si elles se produisent à l'intérieur de fonctions qui sont appelées (même indirectement) dans la clause try.**

Voyons un exemple pour illustrer cela :

```
def f(i):
    try:
        g(i)
    except IndexError:
        print("Veuillez entrer un index valide")

def g(i):
    a = "Hello"
    return a[i]

f(50)
```

Nous avons la fonction `f` et la fonction `g`. `f` appelle `g` dans la clause try. Avec l'argument 50, `g` lèvera une IndexError car l'index 50 n'est pas valide pour la chaîne a. 

Mais `g` elle-même ne gère pas l'exception. Remarquez comment il n'y a pas d'instruction try ... except dans la fonction `g`. Puisqu'elle ne gère pas l'exception, elle "l'envoie" à `f` pour voir si elle peut la gérer, comme vous pouvez le voir dans le diagramme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-16.png)

Puisque f _sait_ comment gérer une IndexError, la situation est gérée élégamment et voici la sortie :

```python
Veuillez entrer un index valide
```

**f4a1 Note :** Si `f` n'avait pas géré l'exception, le programme se serait terminé brusquement avec le message d'erreur par défaut pour une IndexError.

### f4e4 Accès à des détails spécifiques des exceptions

Les exceptions sont des objets en Python, vous pouvez donc assigner l'exception qui a été levée à une variable. De cette manière, vous pouvez imprimer la description par défaut de l'exception et accéder à ses arguments.

Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) :

> La clause except **peut spécifier une variable après le nom de l'exception**. La variable est liée à une instance d'exception avec les arguments stockés dans instance.args.

Voici un exemple (voir ci-dessous) où nous assignons l'instance de `ZeroDivisionError` à la variable `e`. Ensuite, nous pouvons utiliser cette variable dans la clause except pour accéder au type de l'exception, à son message et à ses arguments. 

```python
def divide_integers():
    while True:
        try:
            a = int(input("Veuillez entrer le numérateur : "))
            b = int(input("Veuillez entrer le dénominateur : "))
            print(a / b)
        # Ici, nous assignons l'exception à la variable e
        except ZeroDivisionError as e:
            print(type(e))
            print(e)
            print(e.args)

divide_integers()
```

La sortie correspondante serait :

```python
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 0

# Type
<class 'ZeroDivisionError'>

# Message
division by zero

# Args
('division by zero',)
```

**f4a1 Conseil :** Si vous êtes familier avec les méthodes spéciales, selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) : "pour plus de commodité, l'instance d'exception définit `[__str__()](https://docs.python.org/3/reference/datamodel.html#object.__str__)` afin que les arguments puissent être imprimés directement sans avoir à référencer `.args`."

## 4️⃣ Ajoutons maintenant : la clause "else"

La clause `else` est facultative, mais c'est un excellent outil car elle nous permet d'exécuter du code qui ne doit s'exécuter que si aucune exception n'a été levée dans la clause try.

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-17.png)

Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) :

> L'instruction [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) f4a1 [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) a une **clause else optionnelle**, qui, lorsqu'elle est présente, doit suivre toutes les clauses except. Elle est utile pour le code qui doit être exécuté **si la clause try ne lève pas d'exception.**

Voici un exemple de l'utilisation de la clause `else` :

```python
def divide_integers():
    while True:
        try:
            a = int(input("Veuillez entrer le numérateur : "))
            b = int(input("Veuillez entrer le dénominateur : "))
            result = a / b
        except (ZeroDivisionError, ValueError):
            print("Veuillez entrer des entiers valides. Le dénominateur ne peut pas être zéro")
        else:
            print(result)

divide_integers()
```

Si aucune exception n'est levée, le résultat est imprimé :

```python
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 5
1.0
```

Mais si une exception est levée, le résultat n'est pas imprimé :

```python
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 0
Veuillez entrer des entiers valides. Le dénominateur ne peut pas être zéro
```

f4a1 **Conseil :** Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#handling-exceptions) :

> L'utilisation de la clause `else` est meilleure que l'ajout de code supplémentaire à la clause [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) car elle évite de capturer accidentellement une exception qui n'a pas été levée par le code protégé par l'instruction `try` f4a1 `except`.

## 5️⃣ La clause "finally"

La clause finally est la dernière clause de cette séquence. Elle est **facultative**, mais si vous l'incluez, elle doit être la dernière clause de la séquence. La clause `finally` est **toujours** exécutée, même si une exception a été levée dans la clause try.  

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-19.png)

Selon la [documentation Python](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions) :

> Si une clause [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) est présente, la clause [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) s'exécutera comme dernière tâche avant que l'instruction [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) ne se termine. La clause [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) **s'exécute que l'instruction [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) produise une exception ou non.**

La clause finally est généralement utilisée pour effectuer des actions de "nettoyage" qui doivent toujours être complétées. Par exemple, si nous travaillons avec un fichier dans la clause try, nous devrons toujours fermer le fichier, même si une exception a été levée lorsque nous travaillions avec les données.

Voici un exemple de la clause finally :

```python
def divide_integers():
    while True:
        try:
            a = int(input("Veuillez entrer le numérateur : "))
            b = int(input("Veuillez entrer le dénominateur : "))
            result = a / b
        except (ZeroDivisionError, ValueError):
            print("Veuillez entrer des entiers valides. Le dénominateur ne peut pas être zéro")
        else:
            print(result)
        finally:
            print("À l'intérieur de la clause finally")

divide_integers()
```

Voici la sortie lorsque aucune exception n'a été levée :

```
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 5
1.0
À l'intérieur de la clause finally
```

Voici la sortie lorsqu'une exception a été levée :

```python
Veuillez entrer le numérateur : 5
Veuillez entrer le dénominateur : 0
Veuillez entrer des entiers valides. Le dénominateur ne peut pas être zéro
À l'intérieur de la clause finally
```

Remarquez comment la clause `finally` **s'exécute toujours**.

**f4a1 Important :** rappelez-vous que la clause `else` et la clause `finally` sont facultatives, mais si vous décidez d'inclure les deux, la clause finally doit être la dernière clause de la séquence.

## 6️⃣ Lever des exceptions

Maintenant que vous savez comment gérer les exceptions en Python, je voudrais partager avec vous ce conseil utile : **vous pouvez également choisir quand lever des exceptions dans votre code.** 

Cela peut être utile pour certains scénarios. Voyons comment vous pouvez faire cela :

![Image](https://www.freecodecamp.org/news/content/images/2019/12/image-20.png)

Cette ligne lèvera une ValueError avec un message personnalisé.

Voici un exemple (voir ci-dessous) d'une fonction qui imprime la valeur des éléments d'une liste ou d'un tuple, ou les caractères d'une chaîne. Mais vous avez décidé que vous voulez que la liste, le tuple ou la chaîne ait une longueur de 5. Vous commencez la fonction avec une instruction if qui vérifie si la longueur de l'argument `data` est 5. Si ce n'est pas le cas, une exception ValueError est levée :

```python
def print_five_items(data):
    
    if len(data) != 5:
        raise ValueError("L'argument doit avoir cinq éléments")
    
    for item in data:
        print(item)

print_five_items([5, 2])
```

La sortie serait :

```python
Traceback (most recent call last):
  File "<path>", line 122, in <module>
    print_five_items([5, 2])
  File "<path>", line 117, in print_five_items
    raise ValueError("L'argument doit avoir cinq éléments")
ValueError: L'argument doit avoir cinq éléments
```

Remarquez comment la dernière ligne affiche le message descriptif :

```python
ValueError: L'argument doit avoir cinq éléments
```

Vous pouvez ensuite choisir comment gérer l'exception avec une instruction try ... except. Vous pourriez ajouter une clause else et/ou une clause finally. Vous pouvez la personnaliser pour répondre à vos besoins. 

### f4e5 Ressources utiles

* [Exceptions](https://docs.python.org/3/tutorial/errors.html#exceptions)
* [Gestion des exceptions](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
* [Définition des actions de nettoyage](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)

**J'espère que vous avez apprécié la lecture de mon article et que vous l'avez trouvé utile.** Maintenant, vous avez les outils nécessaires pour gérer les exceptions en Python et vous pouvez les utiliser à votre avantage lorsque vous écrivez du code Python. f600 [Découvrez mes cours en ligne](https://www.udemy.com/user/estefania-cn/). Vous pouvez me suivre sur [Twitter](https://twitter.com/EstefaniaCassN). 

f31ff600 Vous pourriez apprécier mes autres articles freeCodeCamp /news :

* [Le décorateur @property en Python : ses cas d'utilisation, avantages et syntaxe](https://www.freecodecamp.org/news/python-property-decorator/)
* [Structures de données 101 : Graphesf4a1f4a1 Une introduction visuelle pour débutants](https://www.freecodecamp.org/news/data-structures-101-graphs-a-visual-introduction-for-beginners-6d88f36ec768/)
* [Structures de données 101 : Tableauxf4a1f4a1 Une introduction visuelle pour débutants](https://www.freecodecamp.org/news/data-structures-101-arrays-a-visual-introduction-for-beginners-7f013bcc355a/)