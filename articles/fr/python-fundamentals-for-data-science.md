---
title: Fondamentaux de Python pour la Science des Données
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2020-07-15T00:05:23.000Z'
originalURL: https://freecodecamp.org/news/python-fundamentals-for-data-science
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/1_5YaueU4meqq-bCM8y3OlkQ.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: Fondamentaux de Python pour la Science des Données
seo_desc: 'Beginners in the field of data science who are not familiar with programming
  often have a hard time figuring out where they should start.

  With hundreds of questions about how to get started with Python for DS on various
  forums, this post (and video s...'
---

Les débutants dans le domaine de la science des données qui ne sont pas familiers avec la programmation ont souvent du mal à déterminer par où commencer.

Avec des centaines de questions sur la façon de commencer avec [Python pour la DS](https://github.com/dswh/python_fundamentals) sur divers forums, cet article (et cette série vidéo) est ma tentative de répondre à toutes ces questions.

Je suis un évangéliste Python qui a commencé en tant que développeur Python Full Stack avant de passer à l'ingénierie des données puis à la science des données. Mon expérience préalable avec Python et une bonne maîtrise des mathématiques ont facilité ma transition vers la science des données.

Voici donc les fondamentaux pour vous aider à programmer en Python.

Avant de plonger dans les essentiels, assurez-vous d'avoir [installé votre environnement Python](https://youtu.be/t8AUwTDtno8) et de savoir comment utiliser un [Jupyter Notebook (optionnel).](https://www.youtube.com/watch?v=TmDUZfkdZoo&list=PLIkXejH7XPT_y00hj-mB-zTzePsMu2gRb&index=3&t=0s)

Un programme d'études Python de base peut être divisé en 4 sujets essentiels qui incluent :

1. Types de données (int, float, strings)

2. Structures de données composées (listes, tuples et dictionnaires)

3. Conditionnelles, boucles et fonctions

4. Programmation orientée objet et utilisation de bibliothèques externes

Passons en revue chacun d'eux et voyons quels sont les fondamentaux que vous devriez apprendre.

## 1. Types de données et structures

La toute première étape consiste à comprendre comment Python interprète les données.

En commençant par les types de données largement utilisés, vous devriez être familier avec les entiers (int), les flottants (float), les chaînes de caractères (str) et les booléens (bool). Voici ce que vous devriez pratiquer.

### Type, transtypage et fonctions d'I/O :

* Apprendre le type de données en utilisant la méthode `type()`.

```py
type('Harshit')

# output: str
```

* Stocker des valeurs dans des variables et fonctions d'entrée-sortie (`a = 5.67`)

* Transtypage — convertir un type particulier de variable/donnée en un autre type si possible. Par exemple, convertir une chaîne d'entiers en un entier :

```py
astring = "55"
print(type(astring))

# output: <class 'str'>
```

```py
astring = int(astring)
print(type(astring))

# output: <class 'int64'>
```

Mais si vous essayez de convertir une chaîne alphanumérique ou alphabétique en un entier, cela générera une erreur :

![Image](https://www.freecodecamp.org/news/content/images/2020/07/2.png align="left")

Une fois que vous êtes familier avec les types de données de base et leur utilisation, vous devriez apprendre les **opérateurs arithmétiques et l'évaluation des expressions** **(DMAS)** et comment vous pouvez stocker le résultat dans une variable pour une utilisation ultérieure.

```py
answer = 43 + 56 / 14 - 9 * 2
print(answer)

# output: 29.0
```

### Chaînes de caractères :

Savoir comment traiter les données textuelles et leurs opérateurs est utile lorsque l'on travaille avec le type de données chaîne de caractères. Pratiquez ces concepts :

* Concaténer des chaînes de caractères en utilisant `+`

* Diviser et joindre la chaîne de caractères en utilisant les méthodes `split()` et `join()`

* Changer la casse de la chaîne de caractères en utilisant les méthodes `lower()` et `upper()`

* Travailler avec des sous-chaînes d'une chaîne de caractères

Voici [le Notebook](https://github.com/dswh/python_fundamentals/blob/master/Notebooks/python_fundamentals_part-1.ipynb) qui couvre tous les points discutés.

## 2. Structures de données composées (listes, tuples et dictionnaires)

### Listes et tuples (types de données composés) :

L'une des structures de données les plus couramment utilisées et importantes en Python sont les listes. Une liste est une collection d'éléments, et la collection peut être de types de données identiques ou variés.

Comprendre les listes ouvrira éventuellement la voie au calcul d'équations algébriques et de modèles statistiques sur votre tableau de données.

Voici les concepts avec lesquels vous devriez être familier :

* Comment plusieurs types de données peuvent être stockés dans une liste Python.

* **Indexation et découpage** pour accéder à un élément spécifique ou à une sous-liste de la liste.

* Méthodes d'aide pour **trier, inverser, supprimer des éléments, copier et ajouter**.

* Listes imbriquées — listes contenant des listes. Par exemple, `[1,2,3, [10,11]]`.

* Addition dans une liste.

```py
alist + alist

# output: ['harshit', 2, 5.5, 10, [1, 2, 3], 'harshit', 2, 5.5, 10, [1, 2, 3]]
```

Multiplier la liste par un scalaire :

```py
alist * 2

# output: ['harshit', 2, 5.5, 10, [1, 2, 3], 'harshit', 2, 5.5, 10, [1, 2, 3]]
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/5.png align="left")

Les **tuples** sont une séquence ordonnée immuable d'éléments. Ils sont similaires aux listes, mais la **principale différence est que** les tuples **sont immuables alors que les listes sont mutables.**

Concepts sur lesquels se concentrer :

* Indexation et découpage (similaire aux listes).

* Tuples imbriqués.

* Ajout de tuples et méthodes d'aide comme `count()` et `index()`.

### Dictionnaires

Ce sont un autre type de collection en Python. Alors que les listes sont indexées par des entiers, les dictionnaires sont plus comme des adresses. Les dictionnaires ont des paires clé-valeur, et les clés sont analogues aux index dans les listes.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/6.png align="left")

Pour accéder à un élément, vous devez passer la clé entre crochets.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/7.png align="left")

Concepts sur lesquels se concentrer :

* Itérer à travers un dictionnaire (également couvert dans les boucles).

* Utiliser des méthodes d'aide comme `get()`, `pop()`, `items()`, `keys()`, `update()`, et ainsi de suite.

Le Notebook pour les sujets ci-dessus peut être trouvé [ici](https://github.com/dswh/python_fundamentals/blob/master/Notebooks/python_fundamentals_part-2.ipynb).

## 3. Conditionnelles, boucles et fonctions

### Conditions et branchement

Python utilise ces variables booléennes pour évaluer les conditions. Chaque fois qu'il y a une comparaison ou une évaluation, les valeurs booléennes sont la solution résultante.

```py
x = True

ptint(type(x))

# output: <class bool>
```

```py
print(1 == 2)

# output: False
```

La comparaison dans l'image doit être observée attentivement car les gens confondent l'opérateur d'assignation (`=`) avec l'opérateur de comparaison (`==`).

### Opérateurs booléens (or, and, not)

Ceux-ci sont utilisés pour évaluer des assertions complexes ensemble.

* `or` — L'une des nombreuses comparaisons doit être vraie pour que la condition entière soit vraie.

* `and` — Toutes les comparaisons doivent être vraies pour que la condition entière soit vraie.

* `not` — Vérifie l'inverse de la comparaison spécifiée.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/9.png align="left")

```py
score = 76
percentile = 83

if score > 75 or percentile > 90:
    print("Admission réussie !")
else:
    print("Réessayez l'année prochaine")
    
# output: Réessayez l'année prochaine
```

Concepts à apprendre :

* Les instructions `if`, `else` et `elif` pour construire votre condition.

* Faire des comparaisons complexes dans une condition.

* Garder à l'esprit l'indentation lors de l'écriture d'instructions `if` / `else` imbriquées.

* Utiliser les opérateurs booléens, `in`, `is` et `not`.

### Boucles

Souvent, vous devrez effectuer une tâche répétitive, et les boucles seront vos meilleures amies pour éliminer le surcoût de la redondance du code. Vous devrez souvent itérer à travers chaque élément d'une liste ou d'un dictionnaire, et les boucles sont pratiques pour cela. `while` et `for` sont deux types de boucles.

Concentrez-vous sur :

* La fonction `range()` et l'itération à travers une séquence en utilisant des boucles `for`.

* Les boucles `while`

```py
age = [12,43,45,10]
i = 0
while i < len(age):
    if age[i] >= 18:
        print("Adulte")
    else:
        print("Juvénile")
    i += 1

# output: 
# Juvénile
# Adulte
# Adulte
# Juvénile
```

* Itérer à travers des listes et ajouter (ou toute autre tâche avec des éléments de liste) des éléments dans un ordre particulier

```py
cubes = []
for i in range(1,10):
    cubes.append(i ** 3)
print(cubes)

#output: [1, 8, 27, 64, 125, 216, 343, 512, 729]
```

* Utiliser les mots-clés `break`, `pass` et `continue`.

### Compréhension de liste

Une manière sophistiquée et succincte de créer une liste en utilisant un itérable suivi d'une clause `for`.

Par exemple, vous pouvez créer une liste de 9 cubes comme montré dans l'exemple ci-dessus en utilisant la compréhension de liste.

```py
# list comprehension
cubes = [n** 3 for n in range(1,10)]
print(cubes)

# output: [1, 8, 27, 64, 125, 216, 343, 512, 729]
```

### Fonctions

Lors du travail sur un grand projet, la maintenance du code devient une vraie corvée. Si votre code effectue des tâches similaires plusieurs fois, une manière pratique de gérer votre code est d'utiliser des fonctions.

Une fonction est un bloc de code qui effectue certaines opérations sur des données d'entrée et vous donne la sortie souhaitée.

L'utilisation de fonctions rend le code plus lisible, réduit la redondance, rend le code réutilisable et fait gagner du temps.

Python utilise l'indentation pour créer des blocs de code. Voici un exemple de fonction :

```py
def add_two_numbers(a, b):
    sum = a + b
    return sum
```

Nous définissons une fonction en utilisant le mot-clé `def` suivi du nom de la fonction et des arguments (entrée) entre parenthèses, suivi d'un deux-points.

Le corps de la fonction est le bloc de code indenté, et la sortie est retournée avec le mot-clé `return`.

Vous appelez une fonction en spécifiant le nom et en passant les arguments entre parenthèses selon la définition.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/14.png align="left")

Plus d'exemples et de détails [ici](https://github.com/dswh/python_fundamentals/blob/master/Notebooks/python_fundamentals_part-2.ipynb).

## 4. Programmation orientée objet et utilisation de bibliothèques externes

Nous avons utilisé les méthodes d'aide pour les listes, les dictionnaires et autres types de données, mais d'où viennent-elles ?

Lorsque nous disons liste ou dict, nous interagissons en réalité avec un objet de classe liste ou un objet de classe dict. L'impression du type d'un *objet dictionnaire* vous montrera qu'il s'agit d'un objet de classe dict.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/15.png align="left")

Ce sont toutes des classes prédéfinies dans le langage Python, et elles rendent nos tâches très faciles et pratiques.

Les objets sont des instances d'une classe et sont définis comme une encapsulation de variables (données) et de fonctions en une seule entité. Ils ont accès aux variables (attributs) et aux méthodes (fonctions) des classes.

Maintenant, la question est, pouvons-nous créer nos propres classes et objets personnalisés ? La réponse est OUI.

Voici comment vous définissez une classe et un objet de celle-ci :

```py
class Rectangle:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        area = self.height * self.width
        return area

rect1 = Rectangle(12, 10)

print(type(rect1))

# output: <class '__main__.Rectangle'>
```

Vous pouvez ensuite accéder aux attributs et aux méthodes en utilisant l'opérateur point (.).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/17.png align="left")

### Utilisation de bibliothèques/modules externes

L'une des principales raisons d'utiliser Python pour la science des données est la communauté incroyable qui développe des packages de haute qualité pour différents domaines et problèmes. L'utilisation de bibliothèques et de modules externes fait partie intégrante du travail sur des projets en Python.

Ces bibliothèques et modules ont des classes, des attributs et des méthodes définis que nous pouvons utiliser pour accomplir nos tâches. Par exemple, la bibliothèque `math` contient de nombreuses fonctions mathématiques que nous pouvons utiliser pour effectuer nos calculs. Les bibliothèques sont des fichiers `.py`.

Vous devriez apprendre à :

* Importer des bibliothèques dans votre espace de travail

![Image](https://www.freecodecamp.org/news/content/images/2020/07/18.png align="left")

* Utiliser la fonction `help` pour en savoir plus sur une bibliothèque ou une fonction

![Image](https://www.freecodecamp.org/news/content/images/2020/07/19.png align="left")

* Importer directement la fonction requise.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/20.png align="left")

* Comment lire la documentation des packages bien connus comme pandas, numpy et sklearn et les utiliser dans vos projets

## Conclusion

Cela devrait couvrir les fondamentaux de Python et vous permettre de commencer avec la science des données.

Il existe quelques autres fonctionnalités, fonctionnalités et types de données avec lesquels vous vous familiariserez au fil du temps à mesure que vous travaillerez sur de plus en plus de projets.

Vous pouvez parcourir ces concepts dans le dépôt GitHub où vous trouverez également les **notebooks d'exercices** :

%[https://github.com/dswh/python_fundamentals]

Voici une série vidéo en 3 parties basée sur cet article pour que vous puissiez suivre :

%[https://youtu.be/TLLHJC79rDU]

## Science des données avec Harshit

%[https://youtu.be/yapSsspJzAw]

Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/tyagiharshit/), [Twitter](https://twitter.com/tyagi_harshit24), [Instagram](https://www.instagram.com/upgradewithharshit/?hl=en), et consulter ma [chaîne YouTube](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) pour des tutoriels et des interviews plus approfondis.

Si ce tutoriel vous a été utile, vous devriez consulter mes cours de science des données et d'apprentissage automatique sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une base solide de travail à présenter.