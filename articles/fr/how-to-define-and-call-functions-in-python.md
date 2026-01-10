---
title: Comment définir et appeler des fonctions en Python
subtitle: ''
author: Jeremiah Oluseye
co_authors: []
series: null
date: '2023-03-03T21:18:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-define-and-call-functions-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/CD.JPG
tags:
- name: Python
  slug: python
seo_title: Comment définir et appeler des fonctions en Python
seo_desc: 'Python is a powerful and versatile programming language that offers a wide
  range of functionalities for developers.

  One of the most essential features of Python is the ability to define and call functions.

  A function is a block of code that performs ...'
---

Python est un langage de programmation puissant et polyvalent qui offre une large gamme de fonctionnalités pour les développeurs.

L'une des fonctionnalités les plus essentielles de Python est la capacité à définir et appeler des fonctions.

Une fonction est un bloc de code qui effectue une tâche spécifique. En Python, définir et appeler des fonctions est facile et peut grandement améliorer la lisibilité et la réutilisabilité de votre code.

## Comment définir une fonction

Définir une fonction en Python implique deux étapes principales : définir la fonction et spécifier les arguments qu'elle prend.

Pour définir une fonction, vous utilisez le mot-clé def suivi du nom de la fonction et de parenthèses (). Si la fonction prend des arguments, ils sont inclus dans les parenthèses. Le bloc de code de la fonction est ensuite indenté après le deux-points.

Voici un exemple :

```python
def greet(name):
    print("Hello, " + name + "! How are you?")
```

Dans cet exemple, nous définissons une fonction appelée `greet` qui prend un argument appelé `name`. La fonction imprime ensuite un message de salutation sur la console qui inclut l'argument name.

## Comment appeler une fonction

Une fois que vous avez défini une fonction, vous pouvez l'appeler dans votre code autant de fois que nécessaire.

Pour appeler une fonction en Python, vous tapez simplement le nom de la fonction suivi de parenthèses (). Si la fonction prend des arguments, ils sont inclus dans les parenthèses.

Voici un exemple :

```python
greet("John")
```

Dans cet exemple, nous appelons la fonction greet avec l'argument "John". La sortie sur la console serait :

```python
Hello, John! How are you?
```

## Exemples de code de fonctions Python

Voici un exemple de code complet qui définit et appelle la fonction greet :

```python
def greet(name):
    print("Hello, " + name + "! How are you?")

greet("John")
```

Lorsque vous exécutez ce code, il produira la sortie suivante sur la console :

```python
Hello, John! How are you?
```

Prenons un exemple plus avancé de définition et d'appel de fonctions en Python.

Supposons que vous souhaitiez écrire une fonction qui prend une liste d'entiers et retourne une nouvelle liste avec tous les nombres pairs de la liste originale. Voici comment vous pourriez définir et appeler cette fonction :

```python
def get_even_numbers(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = get_even_numbers(numbers)
print(even_numbers)
```

Dans cet exemple, nous définissons une fonction appelée get_even_numbers qui prend un argument appelé numbers. La fonction crée ensuite une liste vide appelée even_numbers et parcourt chaque nombre dans la liste numbers.

Si le nombre est pair, il est ajouté à la liste even_numbers en utilisant la méthode append. Enfin, la fonction retourne la liste even_numbers.

Pour appeler cette fonction, nous créons d'abord une liste de nombres appelée numbers avec les valeurs [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Nous appelons ensuite la fonction get_even_numbers avec la liste numbers comme argument et attribuons la valeur retournée à une nouvelle liste appelée even_numbers.

Enfin, nous imprimons la liste even_numbers sur la console.

Lorsque vous exécutez ce code, il produira la sortie suivante sur la console :

```python
[2, 4, 6, 8, 10]
```

Ceci est la liste des nombres pairs dans la liste originale numbers.

Cet exemple démontre comment définir une fonction plus complexe qui effectue une tâche spécifique, et comment appeler cette fonction avec les arguments appropriés.

En décomposant des tâches complexes en fonctions plus petites et réutilisables, vous pouvez rendre votre code plus lisible, maintenable et efficace.

## Conclusion

Définir et appeler des fonctions en Python est un processus simple qui peut grandement améliorer la fonctionnalité et la lisibilité de votre code.

Avec la syntaxe simple et les capacités puissantes de Python, vous pouvez définir et appeler des fonctions avec n'importe quel nombre d'arguments et effectuer n'importe quel nombre de tâches dans le bloc de code de la fonction.

Alors, allez-y et commencez à définir et appeler des fonctions dans votre code Python pour faire passer vos compétences en programmation au niveau supérieur.

Restons en contact sur [Twitter](https://twitter.com/Olujerry19) et [LinkedIn](https://www.linkedin.com/in/jeremiah-oluseye-58457719a/).