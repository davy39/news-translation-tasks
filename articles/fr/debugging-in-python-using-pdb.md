---
title: Comment déboguer votre code Python avec le débogueur Python (pdb)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-09-27T17:50:42.000Z'
originalURL: https://freecodecamp.org/news/debugging-in-python-using-pdb
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/paulius-andriekus-552Vm3_Ah6A-unsplash.jpg
tags:
- name: debugging
  slug: debugging
- name: Python
  slug: python
seo_title: Comment déboguer votre code Python avec le débogueur Python (pdb)
seo_desc: "By Jagruti Tiwari\nDebugging tools are at the heart of any programming\
  \ language. \nAnd as a developer, it's hard to make progress and write clean code\
  \ unless you know your way around these tools. \nThis article will help you get\
  \ acquainted with one such..."
---

Par Jagruti Tiwari

Les outils de débogage sont au cœur de tout langage de programmation. 

Et en tant que développeur, il est difficile de progresser et d'écrire du code propre sans maîtriser ces outils. 

Cet article vous aidera à vous familiariser avec l'un de ces outils : [Le débogueur Python (pdb)](https://docs.python.org/3/library/pdb.html#:~:text=The%20module%20pdb%20defines%20an,context%20of%20any%20stack%20frame)

Notez qu'il s'agit d'un tutoriel de débogage. Je suppose que vous connaissez au moins un langage de programmation et que vous avez une idée de la rédaction de cas de test.

# Comment débuter avec `pdb` 
Il existe deux façons d'invoquer `pdb` :

## 1. Appeler `pdb` de l'extérieur

Pour appeler `pdb` depuis un terminal, vous pouvez l'invoquer lors de l'exécution de votre fichier `.py`.

```
python -m pdb <test-file-name>.py
```

Si vous utilisez [poetry](https://python-poetry.org/) et [pytest](https://docs.pytest.org/en/7.1.x/), vous pouvez appeler `pdb` en utilisant le flag `--pdb` à la fin.

```
poetry run python <path/to_your/test_file.py> --pdb
```

Pour appeler `pdb` avec Docker, `poetry` et `pytest`, vous pouvez utiliser la syntaxe suivante :

```
COMPOSE_PROJECT_NAME=<test_docker_image_name> docker-compose run --rm workers poetry run pytest <path/to_your/test_file.py>::<name_of_the_test_function> --pdb
```

Vous ajouterez toujours le flag `--pdb` après le nom de votre fichier de test. Cela ouvrira la console `pdb` lorsque le test échoue. Mais n'oubliez pas que `--pdb` est un flag `pytest`.
 

## 2. Ajouter un point d'arrêt avec `pdb` 

Il peut arriver que vous obteniez des faux positifs dans un test. Votre cas de test peut réussir, mais vous n'obtenez pas les données attendues. 

Et si vous vouliez lire la requête brute de la base de données ? Dans ce cas, vous pouvez appeler `pdb` depuis l'intérieur de la fonction Python.

Pour entrer dans le débogueur `pdb`, vous devez appeler `import pdb; pdb.set_trace()` à l'intérieur de votre fonction. 

Comprenons cela avec un exemple de fonction imbriquée :

``` 
# file1.py

from . import function3

def function1():
    // logique pour function1
    function3()
```


``` 
# file2.py

def function2():
    // logique pour function2
    // une requête de base de données
```

``` 
# file3.py

from . import function2

def function3():
    // logique pour function3
    function2()
    // la logique pour function3 continue
```

Dans le code ci-dessus, une fonction en appelle une autre. 

Vous voulez ajouter un point d'arrêt dans `function2` pour comprendre ce qui se passe réellement dans la fonction.

Vous pouvez ajouter un point d'arrêt avec l'instruction suivante :

`import pdb; pdb.set_trace()`

``` 
# file2.py

1. def function2():
2.     // logique pour function2
3.     // ligne 1
4.     // ligne 2
5.    
6.     import pdb; pdb.set_trace();
7.    
8.     // une requête de base de données
9.     // ligne 3
10.    // ligne 4
```

`pdb` ouvre sa console lorsque votre code s'arrête. Quelque chose comme ceci :

```
(Pdb)
```

Lorsque l'interpréteur Python exécute la `ligne 2`, il lira le point d'arrêt et ouvrira la console `pdb`. Nous utilisons les commandes `pdb` pour naviguer dans le code. Nous apprendrons ces commandes dans la section suivante.

# Commandes `pdb` courantes

`pdb` est un débogueur interactif en ligne de commande. Vous ne pouvez pas exploiter tout son potentiel à moins d'être familier avec ses commandes. 

Comme tout autre log de console, `pdb` vous dira exactement à quelle ligne votre code s'arrête.

### La commande [print](https://docs.python.org/3/library/pdb.html#pdbcommand-p)

Supposons que vous ayez un cas de test avec une instruction `assert`. Quelque chose comme ceci :

```
# test.py
    
def test1():
    ...
    result = function1()
    assert result.json = {'status_code':1, 'status': 'saved', 'description':'data saved'}
```

Vous utiliserez la commande `p` pour afficher une valeur dans la console.

```
(Pdb) p result.json
{'status_code':1, 'status': 'saved', 'description':'data saved'}
```

Ceci affiche la valeur contenue dans la variable.

### La commande [up](https://docs.python.org/3/library/pdb.html#pdbcommand-up)

La commande `up` vous déplace d'une frame vers le haut dans la pile. 

Dans le cas d'appels de fonctions imbriquées, elle vous déplacera vers le haut dans la fonction qui a appelé votre fonction.

Prenons un exemple :

```
# test.py

def function1():
    print("invoking function1")
    import pdb;pdb.set_trace()
    print("function1 invoked")


def function2():
    print("invoking function2")
    function1()
    print("function2 invoked")


def function3():
    print("inside function3")
    function2()
    print("function3 invoked")

# démarrage de l'appel avec function2()
 
function3()
```

Dans `pdb`, nous l'appellerons ainsi :

```
$ python -m pdb test.py

> test.py(1)<module>()
-> def function1():
(Pdb) n
> test.py(7)<module>()
-> def function2():
(Pdb) n
> test.py(13)<module>()
-> def function3():
(Pdb) n
> test.py(20)<module>()
-> function3()
(Pdb) n
inside function3
invoking function2
invoking function1
> test.py(4)function1()
-> print("function1 invoked")
(Pdb) n
function1 invoked
--Return--
> test.py(4)function1()->None
-> print("function1 invoked")
(Pdb) u
> test.py(9)function2()
-> function1()
(Pdb) l
  4         print("function1 invoked")
  5
  6
  7     def function2():
  8         print("invoking function2")
  9  ->     function1()
 10         print("function2 invoked")
 11
 12
 13     def function3():
 14         print("inside function3")
(Pdb) u
> test.py(15)function3()
-> function2()
(Pdb) l
 10         print("function2 invoked")
 11
 12
 13     def function3():
 14         print("inside function3")
 15  ->     function2()
 16         print("function3 invoked")
 17
 18     # démarrage de l'appel avec function2()
 19
 20     function3()
(Pdb) u
> test.py(20)<module>()
-> function3()
(Pdb) l
 15         function2()
 16         print("function3 invoked")
 17
 18     # démarrage de l'appel avec function2()
 19
 20  -> function3()
[EOF]
(Pdb) u
> <string>(1)<module>()
```

Ici, nous commençons par invoquer `function3()`. L'exécution s'arrête lorsqu'elle rencontre `import pdb`.

`pdb` ouvre la console et attend la saisie. Nous tapons `u` pour up, et il renvoie la fonction appelante : `function2()`. À la commande `u` suivante, il renvoie `function3` (la fonction qui appelle `function2`).

Nous utilisons la commande `l`. C'est la commande list. Elle liste exactement où se trouve la ligne d'exécution actuelle.

### La commande [step](https://docs.python.org/3/library/pdb.html#pdbcommand-step)

Pour comprendre la commande `step`, continuons avec l'exemple précédent.

```
# test.py
    
1. def test1():
2.    ...
3.    result = function1()
4.    assert result.json.status_code == 1
5.    assert result.json.status == 'saved'
6.    assert result.json.description == 'data saved'
7.
```

```
# function_file.py

def function1():
    foo = ['bar']
    ...
```

Vous soupçonnez que le résultat renvoyé par `function1()` est incorrect. Votre code s'arrête à la ligne 6. Comment entrer dans la ligne 3 ?

Vous utiliserez d'abord la commande `up` et enfin entrerez dans la fonction avec la commande `s`.

```
(Pdb) u
assert result.json.status == 'saved'
(Pdb) u
assert result.json.status_code == 1
(Pdb) p assert result.json.status_code
1
(Pdb) u
result = function1()
(Pdb) s
(Pdb) n
foo = ['bar']
```

Lorsque vous entrez dans `function1()`, la console `pdb` commencera à afficher les instructions de cette fonction.

# Conclusion

`pdb` est un débogueur puissant. Ce tutoriel a pour but de vous familiariser avec les bases de `pdb`. 

Je vous recommande de lire [sa documentation](https://docs.python.org/3/library/pdb.html) pour explorer tout son potentiel.