---
title: Fonctions Lambda Python – Comment utiliser les fonctions anonymes avec des
  exemples
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-02-24T17:25:28.000Z'
originalURL: https://freecodecamp.org/news/python-lambda-functions
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/lambda-1.png
tags:
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: Fonctions Lambda Python – Comment utiliser les fonctions anonymes avec
  des exemples
seo_desc: "Lambda functions, also known as anonymous functions, are small, one-time-use\
  \ functions in Python. \nYou can define them using the lambda keyword followed by\
  \ the function's inputs, a colon, and the function's expression. The output of a\
  \ lambda function..."
---

Les fonctions lambda, également connues sous le nom de fonctions anonymes, sont de petites fonctions à usage unique en Python. 

Vous pouvez les définir en utilisant le mot-clé `lambda` suivi des entrées de la fonction, d'un deux-points et de l'expression de la fonction. Le résultat d'une fonction lambda est retourné comme résultat de l'expression, plutôt que par une instruction return.

Le but principal des fonctions lambda est de permettre la création de petites fonctions jetables que vous pouvez utiliser dans d'autres parties d'un programme. Cela peut être utile lorsque vous devez passer une fonction simple comme argument à une autre fonction, par exemple.

### Syntaxe pour créer des fonctions lambda

Voici la syntaxe pour créer une fonction lambda en Python :

```python
lambda arguments: expression

```

## Fonctions Lambda vs Fonctions Nominales Définies avec le Mot-Clé `def`

Comparées aux fonctions nominales définies avec le mot-clé `def`, les fonctions lambda présentent quelques différences clés. 

Les fonctions nominales peuvent avoir plusieurs expressions et utilisent des instructions return. Les fonctions lambda ne peuvent avoir qu'une seule expression et la valeur de cette expression est retournée automatiquement. 

Les fonctions nominales peuvent également être réutilisées dans un programme, tandis que les fonctions lambda ne sont utilisées qu'une seule fois.

```python
def greet(name):
    return "Hello " + name
print(greet("John")) 

# Sortie : "Hello John"

```

Comme vous pouvez le voir, la fonction nominale est définie en utilisant le mot-clé `def`, suivi du nom de la fonction et de ses entrées entre parenthèses. Le corps de la fonction est indenté, et l'instruction return est utilisée pour retourner le résultat de l'expression. 

Les fonctions nominales peuvent être appelées plusieurs fois, ce qui les rend plus flexibles que les fonctions lambda pour les opérations complexes.

Voici le code équivalent utilisant une fonction nominale définie avec le mot-clé `lambda` :

```python
greet = lambda name: "Hello " + name
print(greet("John")) 

# Sortie : "Hello John"

```

## **Comment Utiliser les Fonctions Lambda**

Cette section couvre les bases de la création et de l'utilisation des fonctions lambda, y compris leur syntaxe et comment les utiliser comme arguments dans des fonctions d'ordre supérieur telles que map, filter et reduce. 

De plus, cette section explore comment vous pouvez utiliser les fonctions lambda dans le tri et dans les compréhensions de liste. À la fin, vous devriez avoir une compréhension fondamentale des utilisations de base des fonctions lambda.

### Comment utiliser les fonctions lambda comme arguments dans les fonctions d'ordre supérieur (`map`, `filter`, `reduce`)

Les fonctions lambda sont souvent utilisées comme arguments dans les fonctions d'ordre supérieur telles que `map`, `filter` et `reduce`. Ces fonctions vous permettent d'appliquer une opération donnée à chaque élément d'une liste ou d'un autre itérable.

Voici un exemple d'utilisation d'une fonction lambda avec la fonction `map` :

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) 

# Sortie : [1, 4, 9, 16, 25]

```

Dans cet exemple, la fonction lambda prend une entrée `x` et retourne le carré de cette valeur. La fonction `map` applique cette opération à chaque élément de la liste `numbers` et retourne une nouvelle liste avec les résultats.

Voici un autre exemple utilisant la fonction `filter` :

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

# Sortie : [2, 4]

```

Dans cet exemple, la fonction lambda prend une entrée `x` et retourne `True` si `x` est pair, et `False` sinon. La fonction `filter` applique cette opération à chaque élément de la liste `numbers` et retourne une nouvelle liste avec uniquement les éléments qui ont retourné `True`.

### Comment utiliser les fonctions lambda pour retourner des fonctions comme valeurs

Vous pouvez également utiliser les fonctions lambda pour retourner des fonctions comme valeurs. Par exemple :

```python
def make_adder(x):
    return lambda y: x + y
add5 = make_adder(5)
print(add5(3)) 

# Sortie : 8

```

Dans cet exemple, la fonction `make_adder` prend une entrée `x` et retourne une fonction lambda qui prend une entrée `y` et retourne la somme de `x` et `y`. La variable `add5` est assignée au résultat de l'appel à `make_adder(5)`, ce qui signifie qu'elle référence maintenant une fonction lambda qui ajoute 5 à son entrée.

### Comment utiliser les fonctions lambda dans le tri

Vous pouvez également utiliser les fonctions lambda dans les opérations de tri pour spécifier des ordres de tri personnalisés. Par exemple :

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_numbers = sorted(numbers, key=lambda x: -x)
print(sorted_numbers) 

# Sortie : [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]

```

Dans cet exemple, la fonction lambda prend une entrée `x` et retourne `-x`, ce qui signifie que l'ordre de tri sera décroissant. La fonction `sorted` trie la liste `numbers` en fonction des valeurs retournées par la fonction lambda.

## Limites des Fonctions Lambda

Bien que les fonctions lambda soient un moyen pratique d'écrire des fonctions courtes et simples, elles ont certaines limites. 

L'une des principales limites est que les fonctions lambda sont limitées à une seule expression, ce qui signifie qu'elles ne peuvent pas contenir plusieurs instructions ou un flux de contrôle complexe. 

De plus, les fonctions lambda ne peuvent pas être référencées par leur nom et ne peuvent être invoquées que lorsqu'elles sont définies, ce qui les rend moins flexibles que les fonctions nommées.

Une autre limite est que les fonctions lambda n'ont pas de nom, ce qui peut rendre le débogage plus difficile et rendre le code plus difficile à comprendre. 

En général, il est bon d'utiliser des fonctions nommées pour les opérations complexes et de n'utiliser les fonctions lambda que pour les opérations courtes et simples.

## **Utilisations Avancées des Fonctions Lambda**

Cette section couvre comment utiliser les fonctions lambda avec des fonctions avancées telles que reduce, filter, sorted et les arguments key. De plus, cette section fournit des informations sur l'utilisation des fonctions lambda pour créer des fonctions anonymes pour les gestionnaires d'événements.

### Comment utiliser les fonctions lambda avec `reduce`

La fonction `reduce` est une fonction d'ordre supérieur qui prend une fonction binaire (une fonction qui prend deux arguments) et une liste. Elle retourne une seule valeur qui est le résultat de l'application de la fonction binaire aux éléments de la liste de manière cumulative. 

Par exemple, pour calculer le produit de tous les éléments d'une liste, vous pourriez utiliser le code suivant :

```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, numbers)
print(product) 

# Sortie : 120

```

Dans cet exemple, la fonction lambda `lambda x, y: x*y` est utilisée comme fonction binaire dans la fonction `reduce`. La fonction `reduce` commence par appliquer la fonction binaire aux deux premiers éléments de la liste, puis applique le résultat à l'élément suivant, et ainsi de suite jusqu'à ce qu'elle ait traité tous les éléments de la liste.

### Comment utiliser les fonctions lambda avec `filter`

La fonction `filter` est une autre fonction d'ordre supérieur qui prend une fonction et une liste, et retourne une nouvelle liste qui contient uniquement les éléments de la liste originale pour lesquels la fonction retourne `True`. 

Par exemple, pour filtrer les nombres pairs d'une liste, vous pourriez utiliser le code suivant :

```python
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

# Sortie : [2, 4]

```

Dans cet exemple, la fonction lambda `lambda x: x % 2 == 0` est utilisée comme argument de fonction dans la fonction `filter`. La fonction `filter` invoque cette fonction lambda pour chaque élément de la liste `numbers` et inclut l'élément dans la liste de résultats uniquement si la fonction lambda retourne `True`.

### Comment utiliser les fonctions lambda avec la fonction `sorted`

La fonction `sorted` est une fonction intégrée qui trie une liste d'éléments. La fonction `sorted` peut prendre un argument `key` optionnel, qui est une fonction qui prend un élément de la liste et retourne une valeur utilisée comme clé de tri. 

Par exemple, pour trier une liste de dictionnaires par une clé spécifique, vous pourriez utiliser le code suivant :

```python
employees = [{"name": "John", "age": 32},              {"name": "Jane", "age": 27},              {"name": "Jim", "age": 40}]
sorted_employees = sorted(employees, key=lambda x: x["age"])
print(sorted_employees)

# Sortie : [{"name": "Jane", "age": 27}, 
#          {"name": "John", "age": 32}, 
#          {"name": "Jim", "age": 40}]

```

Dans cet exemple, la fonction lambda `lambda x: x["age"]` est utilisée comme argument `key` dans la fonction `sorted`. La fonction `sorted` utilise cette fonction lambda pour extraire la valeur "age" pour chaque dictionnaire dans la liste `employees` et utilise ces valeurs comme clés de tri.

### Comment utiliser les fonctions lambda dans l'argument `key` de diverses fonctions

En plus de la fonction `sorted`, de nombreuses autres fonctions en Python peuvent prendre un argument `key`, y compris les fonctions `max`, `min` et `sorted`. 

L'argument `key` est une fonction qui prend un élément de la liste et retourne une valeur utilisée comme clé de tri, ainsi qu'à des fins de comparaison dans le cas des fonctions `max` et `min`.

Par exemple, pour trouver l'employé avec le salaire le plus élevé dans une liste d'employés, vous pourriez utiliser le code suivant :

```python
employees = [{"name": "John", "salary": 50000}, {"name": "Jane", "salary": 55000}, {"name": "Jim", "salary": 60000}]
highest_salary_employee = max(employees, key=lambda x: x["salary"])
print(highest_salary_employee) 

# Sortie : {"name": "Jim", "salary": 60000}

```

Dans cet exemple, la fonction lambda `lambda x: x["salary"]` est utilisée comme argument `key` dans la fonction `max`. La fonction `max` utilise cette fonction lambda pour extraire la valeur "salary" pour chaque employé dans la liste `employees` et utilise ces valeurs pour comparer les employés et trouver celui avec le salaire le plus élevé.

### Comment utiliser les fonctions lambda pour créer des fonctions anonymes pour les gestionnaires d'événements

Vous pouvez également utiliser les fonctions lambda pour créer des fonctions anonymes pour les gestionnaires d'événements en programmation GUI ou pour d'autres fins similaires. 

Par exemple, dans le code suivant, un événement de clic sur un bouton est géré en utilisant une fonction lambda dans Tkinter (un outil de programmation GUI pour Python) :

```python
import tkinter as tk

def on_button_click():
    print("Button clicked!")

root = tk.Tk()
button = tk.Button(root, text="Click Me!", command=lambda: print("Button clicked!"))
button.pack()
root.mainloop()

```

Dans cet exemple, nous utilisons la fonction lambda `lambda: print("Button clicked!")` comme argument `command` du widget `Button` dans Tkinter. Lorsque le bouton est cliqué, la fonction lambda est exécutée et le message "Button clicked!" est imprimé dans la console.

Cela démontre la polyvalence et la flexibilité des fonctions lambda. Vous pouvez les utiliser dans une variété de contextes où des fonctions anonymes sont requises.

## **Bonnes Pratiques pour Utiliser les Fonctions Lambda**

Cette section couvre une gamme de bonnes pratiques, y compris le fait de garder les fonctions lambda simples et faciles à comprendre, d'éviter les expressions et instructions complexes, de choisir le type de fonction approprié pour la tâche, et de documenter les fonctions lambda pour une meilleure lisibilité du code. 

Nous soulignerons également l'importance d'utiliser des noms de variables descriptifs dans les fonctions lambda pour améliorer la lisibilité de votre code.

### Gardez les fonctions lambda simples et faciles à comprendre

L'une des meilleures pratiques pour utiliser les fonctions lambda est de les garder simples et faciles à comprendre. 

Les fonctions lambda sont destinées à être de petites fonctions anonymes à expression unique, et les fonctions complexes ou multi-instructions sont mieux adaptées pour être définies en utilisant le mot-clé `def`.

Par exemple, la fonction lambda suivante est simple, facile à comprendre et fait exactement ce qu'elle est censée faire :

```python
square = lambda x: x * x
print(square(5)) 

# Sortie : 25

```

### Évitez les expressions et instructions complexes dans les fonctions lambda

En plus de garder les fonctions lambda simples, il est également important d'éviter les expressions et instructions complexes dans les fonctions lambda. 

Les expressions et instructions complexes rendent le code plus difficile à comprendre et à maintenir, et peuvent entraîner des bugs.

Par exemple, la fonction lambda suivante est trop complexe et difficile à comprendre :

```python
calculate = lambda x, y: x + y if x > y else x - y
print(calculate(5, 10)) 

# Sortie : -5

```

Dans de tels cas, il est préférable de définir une fonction nominale en utilisant le mot-clé `def` et de fournir un nom significatif à la fonction. Cela rend le code plus lisible et plus facile à maintenir :

```python
def calculate(x, y):
    if x > y:
        return x + y
    else:
        return x - y

print(calculate(5, 10)) 

# Sortie : -5

```

### Quand utiliser les fonctions lambda et quand utiliser les fonctions nommées

Les fonctions lambda sont mieux utilisées dans les situations où vous avez besoin d'une petite fonction anonyme à expression unique. Elles ne sont pas bien adaptées pour les fonctions complexes avec plusieurs expressions et instructions.

Par exemple, un bon cas d'utilisation pour une fonction lambda est en tant qu'argument pour une fonction d'ordre supérieur telle que `map`, `filter` ou `reduce`. Un mauvais cas d'utilisation pour une fonction lambda est une fonction complexe avec plusieurs expressions et instructions.

En général, il est préférable d'utiliser des fonctions nommées définies avec le mot-clé `def` pour les fonctions qui sont complexes, multi-instructions ou utilisées plusieurs fois dans votre code.

### Documentez les fonctions lambda pour une meilleure lisibilité du code

Une autre bonne pratique pour utiliser les fonctions lambda est de les documenter pour une meilleure lisibilité du code. 

Bien que les fonctions lambda soient souvent destinées à être simples et faciles à comprendre, il peut toujours être utile de fournir une brève explication de ce que fait la fonction sous forme de docstring ou de commentaire.

Par exemple, la fonction lambda suivante est documentée pour une meilleure lisibilité du code :

```python
# Cette fonction lambda retourne le carré de son entrée
square = lambda x: x * x
print(square(5)) 

# Sortie : 25

```

### Utilisez des noms de variables descriptifs dans les fonctions lambda

Enfin, il est important d'utiliser des noms de variables descriptifs dans les fonctions lambda, comme vous le feriez dans toute autre fonction. Les noms de variables descriptifs rendent le code plus facile à comprendre et à maintenir.

Par exemple, la fonction lambda suivante utilise des noms de variables descriptifs :

```python
# Cette fonction lambda retourne la somme de ses entrées
sum = lambda x, y: x + y
print(sum(5, 10)) 

# Sortie : 15

```

En suivant ces bonnes pratiques, vous pouvez vous assurer que vos fonctions lambda sont claires, concises et faciles à comprendre, rendant votre code plus lisible, maintenable et sans erreur.

## **Conclusion**

Dans ce guide, nous avons couvert les bases des fonctions lambda en Python, y compris leur définition et leur but, leur syntaxe, et leur utilisation de base et avancée dans diverses applications. 

Nous avons également discuté de certaines bonnes pratiques pour utiliser les fonctions lambda, y compris le fait de les garder simples et faciles à comprendre, d'éviter les expressions et instructions complexes, de choisir le type de fonction approprié pour la tâche, et de les documenter pour une meilleure lisibilité du code.

Les fonctions lambda peuvent être un outil puissant pour écrire un code concis, lisible et efficace. Mais elles ont certaines limites, comme être limitées à une seule expression et avoir des fonctionnalités limitées par rapport aux fonctions nommées. Il est important de prendre en compte ces limites et de choisir le type de fonction approprié pour la tâche à accomplir.

En conclusion, ce guide a fourni un aperçu des fonctions lambda et de leurs utilisations en Python, et j'espère qu'il a été utile dans votre parcours pour en apprendre davantage sur ce sujet. Pour aller plus loin, vous pourriez explorer la documentation officielle de Python et pratiquer l'utilisation des fonctions lambda dans vos propres projets.

---

Visitez mon [blog](https://blog.ashutoshkrris.in) pour lire plus d'articles comme celui-ci. Vous pouvez également choisir de me suivre sur [Twitter](https://twitter.com/ashutoshkrris).