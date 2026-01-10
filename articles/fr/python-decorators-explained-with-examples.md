---
title: Décorateurs Python – Comment créer et utiliser des décorateurs en Python avec
  des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-06-15T17:57:54.000Z'
originalURL: https://freecodecamp.org/news/python-decorators-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/06/cover_image9.png
tags:
- name: decorator
  slug: decorator
- name: Python
  slug: python
seo_title: Décorateurs Python – Comment créer et utiliser des décorateurs en Python
  avec des exemples
seo_desc: 'By Brandon Wallace

  Python decorators allow you to change the behavior of a function without modifying
  the function itself.

  In this article I will show you how to create and use decorators. You will see how
  easy it is to use this advanced Python featu...'
---

Par Brandon Wallace

Les décorateurs Python vous permettent de modifier le comportement d'une fonction sans modifier la fonction elle-même.

Dans cet article, je vais vous montrer comment créer et utiliser des décorateurs. Vous verrez à quel point il est facile d'utiliser cette fonctionnalité avancée de Python.

Dans cet article, je vais discuter des sujets suivants :

* Quand utiliser un décorateur en Python
* Les éléments de base utilisés pour créer un décorateur
* Comment créer un décorateur Python
* Exemples concrets de décorateurs Python
* Décorateurs de classe en Python

## Quand utiliser un décorateur en Python

Vous utiliserez un décorateur lorsque vous devrez modifier le comportement d'une fonction sans modifier la fonction elle-même. Voici quelques bons exemples : lorsque vous souhaitez ajouter des logs, tester les performances, effectuer une mise en cache, vérifier les permissions, etc.

Vous pouvez également l'utiliser lorsque vous devez exécuter le même code sur plusieurs fonctions. Cela évite d'écrire du code dupliqué.

## Voici les éléments de base utilisés pour créer des décorateurs Python

Pour mieux comprendre comment fonctionnent les décorateurs, vous devez d'abord comprendre quelques concepts.

1. Une fonction est un objet. De ce fait, une fonction peut être assignée à une variable. La fonction peut être accessible à partir de cette variable.

```python
def my_function():

    print('I am a function.')

# Assigner la fonction à une variable sans parenthèses. Nous ne voulons pas exécuter la fonction.

description = my_function
```

```python
# Accéder à la fonction à partir de la variable à laquelle je l'ai assignée.

print(description())

# Sortie

'I am a function.'

```

2. Une fonction peut être imbriquée dans une autre fonction.

```python
def outer_function():

    def inner_function():

        print('I came from the inner function.')

    # Exécuter la fonction interne dans la fonction externe.
    inner_function()

```

```python
outer_function()

# Sortie

I came from the inner function.

```

Notez que la fonction `inner_function` n'est pas disponible en dehors de la fonction `outer_function`. Si j'essaie d'exécuter la fonction `inner_function` en dehors de la fonction `outer_function`, je reçois une exception NameError.

```python
inner_function()

Traceback (most recent call last):
  File "/tmp/my_script.py", line 9, in <module>
    inner_function()
NameError: name 'inner_function' is not defined
```

3. Puisqu'une fonction peut être imbriquée dans une autre fonction, elle peut également être retournée.

```python
def outer_function():
    '''Assigner une tâche à un étudiant'''

    task = 'Read Python book chapter 3.'
    def inner_function():
        print(task)
    return inner_function

homework = outer_function()

```

```python
homework()

# Sortie

'Read Python book chapter 5.'

```

4. Une fonction peut être passée à une autre fonction en tant qu'argument.

```python
def friendly_reminder(func):
    '''Rappel pour le mari'''

    func()
    print('Don\'t forget to bring your wallet!')

def action():

    print('I am going to the store buy you something nice.')

```

```python
# Appeler la fonction friendly_reminder avec la fonction action utilisée comme argument.

friendly_reminder(action)

# Sortie

I am going to the store buy you something nice.
Don't forget to bring your wallet!

```

## Comment créer un décorateur Python

Pour créer une fonction décorateur en Python, je crée une fonction externe qui prend une fonction comme argument. Il y a également une fonction interne qui enveloppe la fonction décorée.

Voici la syntaxe pour un décorateur Python de base :

```python
def my_decorator_func(func):

    def wrapper_func():
        # Faire quelque chose avant la fonction.
        func()
        # Faire quelque chose après la fonction.
    return wrapper_func

```

Pour utiliser un décorateur, vous l'attachez à une fonction comme vous le voyez dans le code ci-dessous. Nous utilisons un décorateur en plaçant le nom du décorateur directement au-dessus de la fonction sur laquelle nous voulons l'utiliser. Vous préfixez la fonction décorateur avec un symbole `@`.

```python
@my_decorator_func
def my_func():

    pass
```

Voici un exemple simple. Ce décorateur journalise la date et l'heure d'exécution d'une fonction :

```python
from datetime import datetime


def log_datetime(func):
    '''Journaliser la date et l'heure d'une fonction'''

    def wrapper():
        print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
        print(f'{"-"*30}')
        func()
    return wrapper


@log_datetime
def daily_backup():

    print('Daily backup job has finished.')   

     
daily_backup()

# Sortie

Daily backup job has finished.
Function: daily_backup
Run on: 2021-06-06 06:54:14
---------------------------
```

## Comment ajouter des arguments aux décorateurs en Python

Les décorateurs peuvent recevoir des arguments. Pour ajouter des arguments aux décorateurs, j'ajoute `*args` et `**kwargs` aux fonctions internes.

* `*args` prendra un nombre illimité d'arguments de n'importe quel type, tels que `10`, `True`, ou `'Brandon'`.
* `**kwargs` prendra un nombre illimité d'arguments clés, tels que `count=99`, `is_authenticated=True`, ou `name='Brandon'`.

Voici un décorateur avec des arguments :

```python
def my_decorator_func(func):

    def wrapper_func(*args, **kwargs):
        # Faire quelque chose avant la fonction.
        func(*args, **kwargs)
        # Faire quelque chose après la fonction.
    return wrapper_func


@my_decorator_func
def my_func(my_arg):
    '''Exemple de docstring pour une fonction'''

    pass
```

Les décorateurs masquent la fonction qu'ils décorent. Si je vérifie la méthode `__name__` ou `__doc__`, nous obtenons un résultat inattendu.

```python
print(my_func.__name__)
print(my_func.__doc__)

# Sortie

wrapper_func
None

```

Pour résoudre ce problème, j'utiliserai `functools`. Functools wraps mettra à jour le décorateur avec les attributs de la fonction décorée.

```python
from functools import wraps

def my_decorator_func(func):

    @wraps(func)
    def wrapper_func(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper_func

@my_decorator_func
def my_func(my_args):
    '''Exemple de docstring pour une fonction'''

    pass
```

Maintenant, je reçois la sortie à laquelle je m'attends.

```python
print(my_func.__name__)
print(my_func.__doc__)

# Sortie

my_func
Exemple de docstring pour une fonction

```

## Exemple d'un décorateur Python en action

J'ai créé un décorateur qui mesurera la mémoire et la vitesse d'une fonction. Nous utiliserons le décorateur pour tester les performances de la génération de listes en utilisant quatre méthodes : range, list comprehension, append et concatenation.

```python
from functools import wraps
import tracemalloc
from time import perf_counter 


def measure_performance(func):
    '''Mesurer les performances d'une fonction'''

    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = perf_counter()
        func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        finish_time = perf_counter()
        print(f'Function: {func.__name__}')
        print(f'Method: {func.__doc__}')
        print(f'Memory usage:\t\t {current / 10**6:.6f} MB \n'
              f'Peak memory usage:\t {peak / 10**6:.6f} MB ')
        print(f'Time elapsed is seconds: {finish_time - start_time:.6f}')
        print(f'{"-"*40}')
        tracemalloc.stop()
    return wrapper


@measure_performance
def make_list1():
    '''Range'''

    my_list = list(range(100000))


@measure_performance
def make_list2():
    '''List comprehension'''

    my_list = [l for l in range(100000)]


@measure_performance
def make_list3():
    '''Append'''

    my_list = []
    for item in range(100000):
        my_list.append(item)


@measure_performance
def make_list4():
    '''Concatenation'''

    my_list = []
    for item in range(100000):
        my_list = my_list + [item]


print(make_list1())
print(make_list2())
print(make_list3())
print(make_list4())

# Sortie

Function: make_list1
Method: Range
Memory usage:		        0.000072 MB 
Peak memory usage:	        3.693040 MB 
Time elapsed is seconds:    0.049359
----------------------------------------

Function: make_list2
Method: List comprehension
Memory usage:		        0.000856 MB 
Peak memory usage:	        3.618244 MB 
Time elapsed is seconds:    0.052338
----------------------------------------

Function: make_list3
Method: Append
Memory usage:		        0.000448 MB 
Peak memory usage:	        3.617692 MB 
Time elapsed is seconds:    0.060719
----------------------------------------

Function: make_list4
Method: Concatenation
Memory usage:		        0.000440 MB 
Peak memory usage:	        4.393292 MB 
Time elapsed is seconds:    61.649138
----------------------------------------

```

Vous pouvez également utiliser des décorateurs avec des classes. Voyons comment utiliser des décorateurs avec une classe Python.

Dans cet exemple, notez qu'il n'y a pas de caractère `@` impliqué. Avec la méthode `__call__`, le décorateur est exécuté lorsqu'une instance de la classe est créée.

Cette classe suit le nombre de fois qu'une fonction de requête vers une API a été exécutée. Une fois la limite atteinte, le décorateur empêche la fonction de s'exécuter.

```python
import requests


class LimitQuery:

    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.limit = args[0]
        if self.count < self.limit:
            self.count += 1
            return self.func(*args, **kwargs)
        else:
            print(f'No queries left. All {self.count} queries used.')
            return

@LimitQuery
def get_coin_price(limit):
    '''Voir le Bitcoin Price Index (BPI)'''
    
    url = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

    if url.status_code == 200:
        text = url.json()
        return f"${float(text['bpi']['USD']['rate_float']):.2f}"


print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))
print(get_coin_price(5))

# Sortie

$35968.25
$35896.55
$34368.14
$35962.27
$34058.26
No queries left. All 5 queries used.

```

Cette classe suivra l'état de la classe.

# Conclusion

Dans cet article, j'ai parlé de la manière de passer une fonction à une variable, des fonctions imbriquées, du retour des fonctions et du passage d'une fonction à une autre fonction en tant qu'argument.

Je vous ai également montré comment créer et utiliser des décorateurs Python avec quelques exemples concrets. Maintenant, j'espère que vous serez en mesure d'ajouter des décorateurs à vos projets.

Suivez-moi sur [Github](https://github.com/brandon-wallace) | [DEV.to](https://dev.to/brandonwallace)