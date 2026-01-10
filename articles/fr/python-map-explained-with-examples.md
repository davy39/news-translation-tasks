---
title: Python map() – Fonction de Liste avec Exemples
subtitle: ''
author: Jason
co_authors: []
series: null
date: '2021-11-09T17:50:02.000Z'
originalURL: https://freecodecamp.org/news/python-map-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/pexels-andrew-neel-2859169.jpg
tags:
- name: Python
  slug: python
seo_title: Python map() – Fonction de Liste avec Exemples
seo_desc: 'Python offers a number of functional programming utilities even though
  it''s primarily an object-oriented programming language. And the most notable one
  is the map() function.

  In this article, we''ll explore what the map() function is and how to use it...'
---

Python offre un certain nombre d'utilitaires de programmation fonctionnelle même s'il s'agit principalement d'un langage de programmation orienté objet. Et le plus notable est la fonction map().

Dans cet article, nous allons explorer ce qu'est la fonction `map()` et comment l'utiliser dans votre code.

# La fonction map() en Python

La fonction `map()` (qui est une fonction intégrée en Python) est utilisée pour appliquer une fonction à chaque élément d'un *itérable* (comme une liste ou un dictionnaire Python). Elle retourne un nouvel itérable (un *objet map*) que vous pouvez utiliser dans d'autres parties de votre code.

La syntaxe générale est la suivante :

```python
map(function, iterable, [iterable1, iterable2, ...])
```

Voyons un exemple : imaginez que vous avez une liste de nombres et que vous souhaitez créer une nouvelle liste avec les *cubes* des nombres de la première liste. Une approche traditionnelle impliquerait l'utilisation de la boucle *for* :

```python
org_list = [1, 2, 3, 4, 5]
fin_list = []

for num in org_list:
    fin_list.append(num**3)

print(fin_list) # [1, 8, 27, 64, 125]
```

ce qui est parfaitement valide, mais voyons comment l'utilisation de la fonction `map()` simplifie votre code :

```python
org_list = [1, 2, 3, 4, 5]

# définir une fonction qui retourne le cube de `num`
def cube(num):
    return num**3
   
fin_list = list(map(cube, org_list))
print(fin_list) # [1, 8, 27, 64, 125]
```

Je ne sais pas pour vous, mais je trouve que cette logique est beaucoup plus propre.

> Au cas où vous vous demanderiez ce qui s'est passé en coulisses, la fonction `map()` a essentiellement itéré à travers chaque élément de l'itérable (dans notre cas, `org_list`) et a appliqué la fonction cube dessus. Elle a finalement retourné un nouvel itérable (`fin_list`) avec le résultat.

## Comment Utiliser les Expressions Lambda en Python

Au lieu d'écrire une fonction séparée pour calculer le cube d'un nombre, nous pouvons utiliser une expression *lambda* à sa place. Voici comment vous feriez cela :

```python
fin_list = list(map(lambda x:x**3, org_list))
print(fin_list) # [1, 8, 27, 64, 125]
```

Beaucoup plus propre, n'est-ce pas ?

## Comment Utiliser les Fonctions Intégrées en Python

Vous pouvez également passer des fonctions intégrées de Python. Par exemple, si vous avez une liste de chaînes de caractères, vous pouvez facilement créer une nouvelle liste avec la longueur de chaque chaîne dans la liste.

```python
org_list = ["Hello", "world", "freecodecamp"]
fin_list = list(map(len, org_list))
print(fin_list) # [5, 5, 12]
```

## Comment Utiliser des Fonctions avec Plusieurs Itérables en Python

Jusqu'à présent, nous avons passé dans `map()` des fonctions qui prennent un seul argument (rappelons `cube(num)`). Mais que faire si votre fonction prend plusieurs arguments ? Un exemple de cela serait la fonction `pow(x, y)` qui prend 2 arguments (elle retourne le résultat de x^y).

Pour appliquer une fonction avec plusieurs arguments, il suffit de passer un autre nom d'itérable après le premier.

```python
base = [1, 2, 3, 4]
power = [1, 2, 3, 4]

result = list(map(pow, base, power))
print(result) # [1, 4, 27, 256]
```

# Conclusion

Dans cet article, vous avez appris comment travailler avec la fonction `map()` en Python. Vous avez également vu comment elle peut réduire considérablement la taille de votre code, le rendant plus lisible et sans bogues.

Vous devriez maintenant être à l'aise avec l'utilisation de `map()` en utilisant des fonctions intégrées, des expressions lambda, et même vos propres fonctions personnalisées !

N'oubliez pas de [me suivre sur Twitter](http://twitter.com/jasmcaus) pour des mises à jour sur les futurs articles. Passez une bonne journée !