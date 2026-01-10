---
title: Fonctions Python – Comment définir et appeler une fonction
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-03-16T17:17:43.000Z'
originalURL: https://freecodecamp.org/news/python-functions-define-and-call-a-function
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/functions.png
tags:
- name: Python
  slug: python
seo_title: Fonctions Python – Comment définir et appeler une fonction
seo_desc: 'In programming, a function is a reusable block of code that executes a
  certain functionality when it is called.

  Functions are integral parts of every programming language because they help make
  your code more modular and reusable.

  In this article, I ...'
---

En programmation, une fonction est un bloc de code réutilisable qui exécute une certaine fonctionnalité lorsqu'elle est appelée.

Les fonctions font partie intégrante de tout langage de programmation car elles permettent de rendre votre code plus modulaire et réutilisable.

Dans cet article, je vais vous montrer comment définir une fonction en Python et comment l'appeler, afin que vous puissiez diviser le code de vos applications Python en plus petits morceaux.

Je vais également vous montrer comment fonctionnent les arguments et le mot-clé return dans les fonctions Python.

## Syntaxe de base pour définir une fonction en Python

En Python, vous définissez une fonction avec le mot-clé `def`, puis vous écrivez l'identifiant (nom) de la fonction suivi de parenthèses et de deux-points.

La chose suivante à faire est de vous assurer d'indenter avec une tabulation ou 4 espaces, puis de spécifier ce que vous voulez que la fonction fasse pour vous.

```py
def functionName():
    # Ce que la fonction doit faire
```
## Exemples de base d'une fonction en Python

En suivant la syntaxe de base ci-dessus, un exemple de fonction Python simple affichant « Hello World » dans le terminal ressemble à ceci :

```py
def myfunction():
    print("Hello World")
``` 

**Pour appeler cette fonction**, écrivez le nom de la fonction suivi de parenthèses :

```py
myfunction()

```

Ensuite, exécutez votre code dans le terminal en tapant `python nom_du_fichier.py` pour afficher ce que vous voulez que la fonction fasse :

![sss-1](https://www.freecodecamp.org/news/content/images/2022/03/sss-1.png)

Un autre exemple simple de soustraction de 2 nombres ressemble à ceci :

```py
def subtractNum():
    print(34 - 4)

subtractNum()
# Sortie : 30
```

## Les arguments dans les fonctions Python

Lors de la définition d'une fonction en Python, vous pouvez passer un ou plusieurs arguments dans la fonction en les plaçant à l'intérieur des parenthèses.

La syntaxe de base pour ce faire est illustrée ci-dessous :

```py
def functionName(arg1, arg2):
    # Ce qu'il faut faire avec la fonction
    
```

Lorsque la fonction est appelée, vous devez alors spécifier une valeur pour les arguments :

```py
functionName(valueForArg1, valueForArg2)
```

Voici un exemple d'arguments dans une fonction Python :

```py
def addNum(num1, num2):
    print(num1 + num2)
addNum(2, 4)

# Sortie : 6
```

Dans l'exemple ci-dessus :
- J'ai passé 2 arguments dans la fonction nommée `addNum`
- Je lui ai dit d'afficher la somme des 2 arguments dans le terminal
- Je l'ai ensuite appelée avec les valeurs spécifiées pour les 2 arguments

**N.B.** : Vous pouvez spécifier autant d'arguments que vous le souhaitez.

## Comment utiliser le mot-clé Return en Python

En Python, vous pouvez utiliser le mot-clé `return` pour quitter une fonction afin qu'elle revienne là où elle a été appelée. C'est-à-dire, renvoyer quelque chose hors de la fonction. 

L'instruction return peut contenir une expression à exécuter une fois la fonction appelée.

L'exemple ci-dessous montre comment fonctionne le mot-clé return en Python :

```py
def multiplyNum(num1):
    return num1 * 8

result = multiplyNum(8)
print(result)

# Sortie : 64
```

**Que fait le code ci-dessus ?** 
- J'ai défini une fonction nommée `multiplyNum` et je lui ai passé `num1` comme argument
- À l'intérieur de la fonction, j'ai utilisé le mot-clé return pour spécifier que je veux que `num1` soit multiplié par 8
- Après cela, j'ai appelé la fonction, j'y ai passé `8` comme valeur pour l'argument `num1`, et j'ai assigné l'appel de la fonction à une variable que j'ai nommée `result`
- Avec la variable result, j'ai pu afficher dans le terminal ce que j'avais l'intention de faire avec la fonction

## Conclusion

Dans cet article, vous avez appris à définir et à appeler des fonctions en Python. Vous avez également appris à passer des arguments dans une fonction et à utiliser le mot-clé return, afin d'être plus créatif avec les fonctions que vous écrivez.

Si vous trouvez cet article utile, n'hésitez pas à le partager avec vos amis et votre famille.