---
title: Fonction Lambda en Python – Syntaxe d'Exemple
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-09-27T15:23:43.000Z'
originalURL: https://freecodecamp.org/news/lambda-function-in-python-example-syntax
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-aleksandar-pasaric-4344759.jpg
tags:
- name: beginner
  slug: beginner
- name: Lambda Expressions
  slug: lambda-expressions
- name: Python
  slug: python
seo_title: Fonction Lambda en Python – Syntaxe d'Exemple
seo_desc: 'Lambda functions are anonymous functions that can contain only one expression.

  You may think that lambda functions are an intermediate or advanced feature, but
  here you will learn how you can easily start using them in your code.

  In Python, functions...'
---

Les fonctions lambda sont des fonctions anonymes qui ne peuvent contenir qu'une seule expression.

Vous pourriez penser que les fonctions lambda sont une fonctionnalité intermédiaire ou avancée, mais ici vous apprendrez comment vous pouvez facilement commencer à les utiliser dans votre code.

En Python, les fonctions sont généralement créées comme ceci :

```pithon
def my_func(a):
  # corps de la fonction
```

Vous les déclarez avec le mot-clé `def`, vous leur donnez un nom, puis vous ajoutez la liste des arguments entourée de parenthèses. Il peut y avoir de nombreuses lignes de code, avec autant d'instructions et d'expressions que vous avez besoin à l'intérieur.

Mais parfois, vous pourriez avoir besoin d'une fonction avec une seule expression à l'intérieur, par exemple une fonction qui double son argument :

```python
def double(x):
  return x*2
```

C'est une fonction que vous pouvez utiliser, par exemple, avec la méthode `map`.

```python
def double(x):
  return x*2
  
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(double, my_list))
print(new_list) # [2, 4, 6, 8, 10, 12]
```

Ce serait un bon endroit pour utiliser une fonction lambda, car elle peut être créée exactement là où vous en avez besoin. Cela signifie utiliser moins de lignes de code et vous pouvez éviter de créer une fonction nommée qui n'est utilisée qu'une seule fois (et qui doit ensuite être stockée en mémoire).

## Comment utiliser les fonctions lambda en Python

Vous utilisez les fonctions lambda lorsque vous avez besoin d'une petite fonction pour une courte durée – par exemple comme argument d'une fonction d'ordre supérieur comme `[map](https://www.freecodecamp.org/news/python-map-function-how-to-map-a-list-in-python-3-0-with-example-code/)` ou `filter`.

La syntaxe d'une fonction lambda est `lambda args: expression`. Vous écrivez d'abord le mot `lambda`, puis un espace, puis une liste séparée par des virgules de tous les arguments, suivie d'un deux-points, et enfin l'expression qui est le corps de la fonction.

Notez que vous ne pouvez pas donner de nom aux fonctions lambda, car elles sont anonymes (sans nom) par définition.

Une fonction lambda peut avoir autant d'arguments que vous avez besoin d'utiliser, mais le corps doit être une seule expression.

### Exemple 1

Par exemple, vous pourriez écrire une fonction lambda qui double son argument : `lambda x: x*2`, et l'utiliser avec la fonction `map` pour doubler tous les éléments d'une liste :

```python
my_list = [1, 2, 3, 4, 5, 6]
new_list = list(map(lambda x: x*2, my_list))
print(new_list) # [2, 4, 6, 8, 10, 12]
```

Remarquez la différence entre celle-ci et la fonction que nous avons écrite ci-dessus avec la fonction `double`. Celle-ci est plus compacte, et il n'y a pas de fonction supplémentaire occupant de l'espace en mémoire.

### Exemple 2

Ou vous pourriez écrire une fonction lambda qui vérifie si un nombre est positif, comme `lambda x: x > 0`, et l'utiliser avec `filter` pour créer une liste de nombres uniquement positifs.

```python
my_list = [18, -3, 5, 0, -1, 12]
new_list = list(filter(lambda x: x > 0, my_list))
print(new_list) # [18, 5, 12]
```

La fonction lambda est définie là où elle est utilisée, de cette manière il n'y a pas de fonction nommée en mémoire. Si une fonction est utilisée à un seul endroit, il est logique d'utiliser une fonction lambda pour éviter l'encombrement.

### Exemple 3

Vous pouvez également retourner une fonction lambda depuis une fonction.

Si vous devez créer plusieurs fonctions qui multiplient des nombres, par exemple doubler ou tripler et ainsi de suite, lambda peut aider.

Au lieu de créer plusieurs fonctions, vous pourriez créer une fonction `multiplyBy` comme ci-dessous, puis appeler cette fonction plusieurs fois avec différents arguments pour créer les fonctions qui doublent, triplent, etc.

```python
def muliplyBy (n):
  return lambda x: x*n
  
double = multiplyBy(2)
triple = muliplyBy(3)
times10 = multiplyBy(10)
```

La fonction lambda prend la valeur `n` de la fonction parente, de sorte que dans `double` la valeur de `n` est `2`, dans `triple` elle est `3` et dans `times10` elle est `10`. Maintenant, appeler ces fonctions avec un argument multipliera ce nombre.

```python
double(6)
> 12
triple(5)
> 15
times10(12)
> 120
```

Si vous n'utilisiez pas de fonction lambda ici, vous devriez définir une fonction différente à l'intérieur de `multiplyBy`, quelque chose comme ceci :

```python
def muliplyBy (x):
  def temp (n):
    return x*n
  return temp
```

L'utilisation d'une fonction lambda utilise la moitié des lignes et la rend plus lisible.

## Conclusion

Les fonctions lambda sont un moyen compact d'écrire des fonctions si votre fonction ne contient qu'une seule petite expression. Elles ne sont généralement pas quelque chose que les codeurs débutants utilisent, mais ici vous avez vu comment vous pouvez facilement les utiliser à n'importe quel niveau.