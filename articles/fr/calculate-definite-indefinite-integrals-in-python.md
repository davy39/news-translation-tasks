---
title: Comment calculer les intégrales définies et indéfinies en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-07-31T18:02:27.000Z'
originalURL: https://freecodecamp.org/news/calculate-definite-indefinite-integrals-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/calculating-integrals-python-1.png
tags:
- name: Advanced Mathematics
  slug: advanced-mathematics
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: Comment calculer les intégrales définies et indéfinies en Python
seo_desc: "By Roy Chng\nPython is a versatile programming language that offers libraries\
  \ and tools for scientific computing and mathematical calculations. \nMany essential\
  \ mathematical operations frequently involve definite and indefinite integrals.\
  \ In this artic..."
---

Par Roy Chng

Python est un langage de programmation polyvalent qui offre des bibliothèques et des outils pour le calcul scientifique et les calculs mathématiques.

De nombreuses opérations mathématiques essentielles impliquent fréquemment des intégrales définies et indéfinies. Dans cet article, nous allons explorer comment effectuer ces calculs en utilisant Python.

## Comment calculer les intégrales définies à une variable

### Installer SciPy

Avant de commencer, nous devons installer le module SciPy. Il fournit une collection d'algorithmes et de fonctions mathématiques que nous allons utiliser.

Vous pouvez le faire en exécutant la commande suivante dans un terminal :

```
pip install scipy
```

Pour calculer les intégrales définies à une variable, nous devons d'abord importer `quad` depuis `scipy.integrate`. C'est une fonction polyvalente utilisée pour calculer les intégrales définies à une variable.

```python
from scipy.integrate import quad
```

### Fonctions élémentaires

À partir de là, nous devons définir l'intégrande comme une fonction en Python.

Par exemple, si nous voulions calculer l'intégrale de x au carré, nous définirions l'intégrande comme une fonction Python comme suit :

```python
def integrand(x):
	return x**2
```

Une fois que nous avons défini l'intégrande, nous pouvons calculer l'intégrale définie en utilisant la fonction quad comme ceci :

```python
print(quad(integrand, 0, 1))
# (0.33333333333333337, 3.700743415417189e-15)

```

Dans le code ci-dessus, `0` représente la limite inférieure d'intégration et `1` représente la limite supérieure d'intégration. Elles peuvent être n'importe quel autre nombre.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_1-4.png)
_Résultat de l'intégrale de x^2 de 0 à 1 avec le code associé_

Dans cet exemple, nous calculons que le résultat estimé de l'intégrale de 0 à 1 de x au carré est d'environ 0,333 avec une erreur absolue d'environ 3,7e-15.

La fonction quad retourne un tuple d'une estimation de l'intégrale définie suivie de l'erreur absolue de l'estimation.

Ce que fait la fonction `quad`, c'est essentiellement évaluer la fonction `integrand` à plusieurs valeurs différentes entre nos limites d'intégration pour pouvoir calculer une estimation de l'intégrale.

Un autre exemple serait si je voulais calculer l'intégrale de `(x+1)/x**2`. Nous la définirions d'abord comme une fonction en Python, et la passerions dans la fonction `quad` avec les limites d'intégration :

```python
from scipy.integrate import quad

def integrand(x):
	return(x+1)/x**2
    
print(quad(integrand, 1, 2))
# (1.1931471805599452, 1.3246594716242401e-14)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_2-3.png)
_Résultat de l'intégrale de (x+1)/x^2 de 1 à 2 avec le code associé_

Dans cet exemple, nous calculons que le résultat estimé de l'intégrale de 1 à 2 de x +1 sur x au carré est d'environ 1,19 avec une erreur absolue d'environ 1,32e-14.

### Autres fonctions courantes

Si nous voulions utiliser des fonctions mathématiques courantes telles que `sin(x)` ou `log(x)`, nous pouvons utiliser un autre package Python pour le calcul scientifique - NumPy. Vous pouvez installer le package en utilisant la commande suivante :

```
pip install numpy
```

En l'important, nous avons accès à ces fonctions courantes que nous pouvons utiliser dans notre intégrande :

```python
from scipy.integrate import quad
from numpy import log, sin

def integrand(x):
	return log(sin(x))
    
print(quad(integrand, 0, 2))
# (-1.1022223889049558, 1.2237126744196256e-15)


```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_3-2.png)
_Résultat de l'intégrale de log(sin(x)) de 0 à 2 avec le code associé_

Dans cet exemple, nous calculons que le résultat estimé de l'intégrale de 0 à 2 de log(sin(x)) est d'environ -1,10 avec une erreur absolue d'environ 1,22e-15.

Une liste complète des fonctions mathématiques que NumPy fournit est [dans leur documentation](https://numpy.org/doc/stable/reference/routines.math.html).

### Comment utiliser les constantes

NumPy fournit également des constantes utiles telles que `e` et `pi`, ainsi que `inf`. C'est une représentation en virgule flottante de l'infini positif. Nous pouvons l'utiliser pour calculer une intégrale définie qui converge.

```python
from scipy.integrate import quad
from numpy import inf, exp

def integrand(x):
  return exp(-x)
    
print(quad(integrand, 0, inf))
# (1.0000000000000002, 5.842606742906004e-11)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_4-4.png)
_Résultat de l'intégrale de e^x de 0 à l'infini avec le code associé_

Dans cet exemple, nous calculons que le résultat estimé de l'intégrale de e élevé à la puissance négative x de 0 à l'infini est d'environ 1,00 avec une erreur absolue d'environ 5,84e-11.

## Comment calculer les intégrales à plusieurs variables

### Intégrales doubles

Pour calculer les intégrales doubles, nous devons importer la fonction `dblquad` depuis `scipy.integrate` :

```
from scipy.integrate import dblquad
```

Nous définissons l'intégrande de manière similaire à celle d'une intégrale définie à une variable, sauf que cette fois nous spécifions deux arguments au lieu d'un.

```python
def integrand(y, x):
	return x*y**2
```

Nous pouvons ensuite calculer l'intégrale définie en utilisant la fonction `dblquad` fournie par `scipy`.

Notez que l'intégrande est une fonction qui doit accepter `y` comme premier paramètre et `x` comme deuxième paramètre.

```python
print(dblquad(integrand, 0, 1, 2, 4))
# (9.333333333333334, 2.0679162295394134e-13)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_5-2.png)
_Résultat de l'intégrale de (xy^2) dxdy de 2 à 4 pour y et intégrale de 0 à 1 pour x avec le code associé_

Dans cet exemple, nous calculons que le résultat estimé de l'intégrale double x fois y au carré de x = 0 à 1 et de y = 2 à y = 4 est d'environ 9,33 avec une erreur absolue d'environ 2,07e-13.

La fonction nécessite que nous passions l'intégrande, et les limites inférieure et supérieure d'intégration pour `x`, suivies des limites inférieure et supérieure d'intégration pour `y`.

### Limites variables

Pour calculer les intégrales avec des limites variables, nous devons définir des fonctions pour les limites inférieure et supérieure d'intégration pour y en termes de x :

```python
def upper_limit_y(x):
	return x**2
    
def lower_limit_y(x):
	return x
    
def integrand(y, x):
	return x+y
  
print(dblquad(integrand, 0, 2, lower_limit_y, upper_limit_y))
```

Dans cet exemple, nous calculons que le résultat estimé de l'intégrale double de x+y de x = 0 à x = 2, et de y = x à y = x^2 est d'environ 3,2 avec une erreur absolue d'environ 1,10e-13.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/indefinite_integral_example_3-1.png)
_Résultat de l'intégrale double (x+y) dydx de 0 à 2 pour x et intégrale de x à x^2 pour y avec le code associé_

### Intégrales triples

Pour calculer les intégrales triples, nous pouvons utiliser la fonction `tplquad` :

```python
from scipy.integrate import tplquad

def integrand(z, y, x):
	return z*(x+y+z)
    
print(tplquad(integrand, 0, 1, 4, 5, 0, 1))
# (2.8333333333333335, 3.6983326566167174e-14)

```

La fonction nécessite que nous passions des arguments similaires, étant les limites supérieure et inférieure d'intégration en `x`, `y` et `z`.

Dans cet exemple, nous calculons que le résultat estimé de l'intégrale triple de z multiplié par (x+y+z) de x = 0 à x = 1, y = 4 à y = 5, et z = 0 à z = 1 est d'environ 2,83 avec une erreur absolue de 3,70e-14 :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/definite_integral_example_6-1.png)
_Résultat de l'intégrale triple z(x+y+z) dxdydz de 0 à 1 pour x, 4 à 5 pour y et 0 à 1 pour z avec le code associé_

## Comment évaluer les intégrales indéfinies à une variable

Pour calculer les intégrales indéfinies à une variable avec Python, nous devons utiliser la bibliothèque SymPy. Elle est utilisée pour le calcul symbolique et implique un calcul exact en utilisant des variables. Pour l'installer, installez le module SymPy :

```
pip install sympy
```

Une fois qu'il est installé, nous pouvons importer les méthodes `Symbol` et `integrate` depuis `sympy` :

```python
from sympy import Symbol, integrate
```

Nous devons d'abord définir les variables utilisées dans l'intégrande :

```python
x = Symbol('x')

```

Après cela, nous pouvons intégrer la fonction en utilisant la méthode `integrate` que SymPy fournit. Elle attend deux arguments : le premier est l'intégrande, et le second est la variable par rapport à laquelle nous intégrons.

Par exemple, si nous voulions intégrer x au carré par rapport à `x`, nous pouvons définir l'intégrande en Python comme `x**2` :

```python
print(integrate(x**2, x))
# (x**3)/3
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/indefinite_integral_example_1-3.png)
_Résultat de l'intégrale indéfinie de x^2_

Dans cet exemple, nous calculons l'intégrale de x au carré qui est x au cube sur 3.

**Notez que SymPy n'ajoute pas la constante d'intégration, mais elle est implicite.**

SymPy fournit également d'autres fonctions courantes telles que `sin(x)` et `exp(x)` que nous pouvons utiliser.

Avant de les utiliser, nous devons d'abord les importer depuis `sympy` :

```python
from sympy import Symbol, integrate, sin
```

En utilisant la fonction `sin` importée, nous pouvons ensuite évaluer l'intégrale de `sin(x)`.

```python
x = Symbol('x')
print(integrate(sin(x), x))
# -cos(x)
```

Dans cet exemple, nous calculons l'intégrale de sin(x) qui est -cos(x) :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/indefinite_integral_example_2-1.png)
_Résultat de l'intégrale indéfinie de sin(x)_

Sympy fournit la liste complète des fonctions mathématiques que vous pouvez utiliser [dans leur documentation](https://docs.sympy.org/latest/modules/functions/elementary.html)

## Résumé

Dans ce tutoriel, nous avons passé en revue les bases du calcul des intégrales définies et indéfinies en Python. Nous avons également examiné comment calculer les intégrales de fonctions élémentaires, celles qui impliquent des fonctions mathématiques courantes, ainsi que l'utilisation de constantes.

Nous avons utilisé des bibliothèques Python populaires pour le calcul scientifique et passé en revue des exemples de calcul d'intégrales.

Si vous aimez mes écrits, envisagez de vous abonner à [ma chaîne YouTube](https://www.youtube.com/@turbinethree).

Bon codage !

##