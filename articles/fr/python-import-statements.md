---
title: Les instructions d'importation Python expliquées
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-14T19:25:00.000Z'
originalURL: https://freecodecamp.org/news/python-import-statements
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c95740569d1a4ca3304.jpg
tags:
- name: Python
  slug: python
- name: toothbrush
  slug: toothbrush
seo_title: Les instructions d'importation Python expliquées
seo_desc: 'While learning programming and reading some resources you’d have come across
  this word ‘abstraction’ which simply means to reduce and reuse the code as much
  as possible.

  Functions and Modules facilitate abstraction. You create functions when you want...'
---

En apprenant la programmation et en lisant certaines ressources, vous aurez rencontré le mot « abstraction », qui signifie simplement réduire et réutiliser le code autant que possible.

Les fonctions et les modules facilitent l'abstraction. Vous créez des fonctions lorsque vous voulez faire quelque chose de manière répétée dans un fichier.

Les modules entrent en jeu lorsque vous voulez réutiliser un groupe de fonctions dans différents fichiers sources. Les modules sont également utiles pour structurer le programme.

* Utilisation des bibliothèques standard et d'autres modules tiers
* Structuration du programme

## **Utilisation des bibliothèques standard**

Exemple : Vous pouvez lire sur les méthodes/fonctions de toutes les bibliothèques standard dans la documentation officielle de Python en détail.

```text
import time
for i in range(100):
    time.sleep(1)   # Attend 1 seconde puis exécute la commande suivante
    print(str(i) + ' seconds have passed')  # affiche le nombre de secondes écoulées depuis le début du programme
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le code](https://repl.it/CS6C)

```text
# Pour calculer le temps d'exécution d'une partie du programme
import time
start = time.time()
# code ici
end = time.time()
print('Temps d'exécution :', end-start)
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le code](https://repl.it/CS6C/1)

```text
# Utilisation du module math
import math
print(math.sqrt(100))   # affiche 10
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le code](https://repl.it/CS6C/2)

## **Utilisation de modules tiers**

Les modules tiers ne sont pas fournis avec Python, mais nous devons les installer externement en utilisant des gestionnaires de paquets comme [`pip`](https://bootstrap.pypa.io/get-pip.py) et [`easy install`](https://bootstrap.pypa.io/ez_setup.py)

```text
# Pour faire des requêtes http
import requests
rq = requests.get(target_url)
print(rq.status_code)
```

En savoir plus sur le module python-requests [ici](http://docs.python-requests.org/en/master/)

## **Pour structurer les programmes**

Nous voulons créer un programme qui a diverses fonctions concernant les nombres premiers. Alors commençons. Nous allons définir toutes les fonctions dans `prime_functions.py`

```text
# prime_functions.py
from math import ceil, sqrt
def isPrime(a):
    if a == 2:
        return True
    elif a % 2 == 0:
        return False
    else:
        for i in range(3,ceil(sqrt(a)) + 1,2):
            if a % i == 0:
                return False
        return True

def print_n_primes(a):
    i = 0
    m = 2
    while True:
        if isPrime(m) ==True:
            print(m)
            i += 1
        m += 1
        if i == a:
            break
```

Maintenant, nous voulons utiliser les fonctions que nous venons de créer dans `prime_functions.py`, donc nous créons un nouveau fichier `playground.py` pour utiliser ces fonctions.

*Veuillez noter que ce programme est beaucoup trop simple pour créer deux fichiers séparés, c'est juste pour démontrer. Mais lorsque les programmes sont grands et complexes, créer différents fichiers est vraiment utile.*

```text
# playground.py
import prime_functions
print(prime_functions.isPrime(29)) # retourne True
```

## **Trier les imports**

Une bonne pratique consiste à trier les modules `import` en trois groupes - les imports de bibliothèques standard, les imports tiers liés et les imports locaux. Dans chaque groupe, il est judicieux de trier par ordre alphabétique par nom de module. Vous pouvez trouver [plus d'informations dans le PEP8](https://www.python.org/dev/peps/pep-0008/?#imports).

L'une des choses les plus importantes pour le langage Python est la lisibilité, et le tri alphabétique des modules est plus rapide à lire et à rechercher. De plus, il est plus facile de vérifier qu'un module est importé et d'éviter les imports dupliqués.

## De X importer Y : un exemple

Voici un exemple de problème :

```text
>>> from math import ceil, sqrt
>>> # ici ce serait
>>> sqrt(36)
<<< 6
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le code](https://repl.it/CS5t/1)

Ou nous pourrions utiliser celui-ci à la place :

```text
>>> import math
>>> # ici ce serait
>>> math.sqrt(36)
<<< 6
```

![:rocket:](https://forum.freecodecamp.com/images/emoji/emoji_one/rocket.png?v=2)

[Exécuter le code](https://repl.it/CS5u)

Ensuite, notre code ressemblerait à `math.sqrt(x)` au lieu de `sqrt(x)`. Cela se produit parce que lorsque nous utilisons `import x`, un espace de noms `x` est créé pour éviter les conflits de noms. Vous devez accéder à chaque objet du module en tant que `x.<nom>`.

Mais lorsque nous utilisons `from x import y`, nous acceptons d'ajouter `y` à l'espace de noms global principal. Donc, en utilisant cela, nous devons nous assurer que nous n'avons pas d'objet avec le même nom dans notre programme.

**N'utilisez jamais `from x import y` si un objet nommé `y` existe déjà**

Par exemple, dans le module `os`, il y a une méthode `open`. Mais nous avons même une fonction intégrée appelée `open`. Donc, ici, nous devons éviter d'utiliser `from os import open`.

Nous pouvons même utiliser `from x import *`, cela importerait toutes les méthodes, classes de ce module dans l'espace de noms global du programme. Ce n'est pas une bonne pratique de programmation. Veuillez l'éviter.

En général, vous devriez éviter `from x import y` simplement à cause des problèmes qu'il peut causer dans les programmes à grande échelle. Par exemple, vous ne savez jamais si un autre programmeur pourrait vouloir créer une nouvelle fonction qui se trouve être le nom de l'une des fonctions existantes. Vous ne savez pas non plus si Python changera la bibliothèque à partir de laquelle vous importez des fonctions. Bien que ces problèmes n'existent pas aussi souvent pour les projets solo, comme indiqué précédemment, c'est une mauvaise pratique de programmation et elle doit être évitée.