---
title: Python Map – Comment mapper une liste en Python 3.0, avec exemple de code de
  fonction
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-04-12T14:25:17.000Z'
originalURL: https://freecodecamp.org/news/python-map-function-how-to-map-a-list-in-python-3-0-with-example-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60721be2d5756f080ba9871d.jpg
tags:
- name: Python
  slug: python
seo_title: Python Map – Comment mapper une liste en Python 3.0, avec exemple de code
  de fonction
seo_desc: "By Daniel Chae\nIf you're learning how to code, the Python Map Function\
  \ is your opportunity to level up. \nPicture this: you want to become a more efficient\
  \ coder. You want your code to compile faster. You want to impress your peers with\
  \ your robust co..."
---

Par Daniel Chae

Si vous apprenez à coder, la fonction Python Map est votre opportunité de passer au niveau supérieur. 

Imaginez ceci : vous voulez devenir un codeur plus efficace. Vous voulez que votre code compile plus rapidement. Vous voulez impressionner vos pairs avec vos solides connaissances en codage. Si tout cela vous parle, alors vous êtes au bon endroit. 

Avant de continuer, vous devez comprendre ce que sont les fonctions et les itérables :

Les fonctions sont des codes qui effectuent une tâche spécifique.

_Exemples : `len()`, `print()`, `str()`_

Les itérables sont des objets qui contiennent un ou plusieurs membres.

_Exemples : liste, dictionnaire, tuple_

La fonction Python Map est une fonction qui vous permet de transformer un itérable entier en utilisant une autre fonction. Le concept clé ici est la transformation, qui peut inclure, sans s'y limiter :

* Convertir des chaînes en nombres
* Arrondir des nombres
* Obtenir la longueur de chaque membre de l'itérable

Vous vous demandez peut-être, "pourquoi ne puis-je pas simplement faire ce qui précède avec une boucle for ?"

La réponse est, vous pouvez. Mais l'utilisation de la fonction Python Map vous fait économiser de la mémoire (ce qui signifie que votre code s'exécute plus rapidement) et nécessite moins de code. Passons en revue un exemple pour que vous puissiez comprendre ce que je veux dire. 

## Commençons d'abord avec une boucle For

Supposons que vous avez une liste de chaînes qui sont en réalité des nombres, mais vous devez convertir la liste de chaînes en entiers :

`list_of_strings = ["5","6","7","8","9", "10"]`

Vous pourriez utiliser une liste vide et une boucle for pour accomplir cela :

```
list_of_strings = ["5","6","7","8","9", "10"]

result = []

for string in list_of_strings:
    result.append(int(string))
    
print(result)
```

Si vous exécutiez cet exemple, vous obtiendriez :

Sortie : [5, 6, 7, 8, 9, 10]

### Ce qui se passe sous le capot avec la boucle For

Vous pouvez être satisfait du résultat, mais pensez à ce que votre code vient de faire. 

Vous avez dit à l'ordinateur de parcourir chaque membre ("5", "6", "7", etc...), de convertir le membre, puis de stocker ce membre dans une nouvelle liste. Bien que l'utilisation d'une boucle for pour transformer une liste soit fonctionnelle, elle n'est pas optimale.

## Fonction Python Map (avec exemple de code)

Au lieu de cela, utilisons la fonction Python Map pour produire un résultat à la fois fonctionnel et optimal. Nous commencerons avec notre liste de chaînes qui doivent être converties :

```
list_of_strings = ["5","6","7","8","9", "10"]

```

Ensuite, nous utiliserons la fonction Python Map pour transformer la liste de chaînes en une liste d'entiers :

```
result = map(int,list_of_strings)

print(list(result))
```

Si vous exécutez l'exemple ci-dessus, vous obtiendriez le même résultat :

Sortie : [5, 6, 7, 8, 9, 10]

Avant d'aborder pourquoi la fonction Python Map est plus optimale que l'utilisation d'une boucle for, décomposons ce que nous venons de faire :

```
list_of_strings = ["5","6","7","8","9", "10"]

```

Tout ce que nous avons fait ici est de créer une variable qui stocke la liste de chaînes que nous voulons convertir en nombres. 

```
result = map(int,list_of_strings)

```

Décomposons le code ci-dessus de l'intérieur vers l'extérieur. La syntaxe de la fonction Python Map est la suivante :

```
map(insérer fonction ici, insérer itérable ici)
```

`map()` est simplement le nom de la fonction Python Map, rien de compliqué ici.

`insérer fonction ici` est l'espace où vous écririez une fonction. Dans l'exemple de code ci-dessus, nous avons utilisé la fonction `int`. Nous aurions pu utiliser une autre fonction intégrée comme `len()` ou nous aurions pu créer notre propre fonction et l'utiliser ici également.

`insérer itérable ici` est l'espace où vous écririez l'itérable de votre choix. Dans ce cas, nous avons inséré notre liste (`list_of_strings`).

`result` est la variable où nous stockons nos membres nouvellement transformés.  

Passons à la dernière ligne de code. Encore une fois, nous travaillerons de l'intérieur vers l'extérieur :

```
print(list(result))
```

`list()` prend nos membres itérables nouvellement transformés et indique à notre ordinateur que ces membres font partie d'une liste. 

`print()` imprime notre nouvelle liste ! 

### Ce qui se passe sous le capot avec la fonction Python Map

Au lieu d'itérer à travers chaque membre de la liste de chaînes, la fonction Python Map a transformé l'ensemble de la liste de chaînes en une liste de nombres. Vous avez économisé de la mémoire et votre code s'est exécuté plus rapidement. 

## Si vous voulez transformer, la fonction Python Map > les boucles For

![Image](https://www.freecodecamp.org/news/content/images/2021/04/nubelson-fernandes-Y376h7VN27c-unsplash.jpg)

En fin de compte, la fonction Python Map est plus élégante qu'une boucle for et vous aidera à compiler votre code plus rapidement. 

L'utilisation de la fonction Python Map vous aidera à faire passer vos compétences en codage au niveau supérieur et à devenir un meilleur programmeur. Dans le processus, vous pourriez même impressionner vos pairs en codage avec cette nouvelle compétence. 

Cela dit, la fonction Python Map n'est qu'un début. Il existe de nombreuses autres astuces Python qui vous aideront à écrire un code plus élégant et à améliorer vos compétences en programmation. Bon codage !