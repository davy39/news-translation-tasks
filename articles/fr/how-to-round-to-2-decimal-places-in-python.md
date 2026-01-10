---
title: Comment arrondir à 2 décimales en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-22T17:17:58.000Z'
originalURL: https://freecodecamp.org/news/how-to-round-to-2-decimal-places-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/round-up-numbers-1.png
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: Comment arrondir à 2 décimales en Python
seo_desc: "By Dillion Megida\nPython provides many math methods for mathematical operations\
  \ such as square roots, exponents, and so on. \nIn this article, I will show you\
  \ how to round up a number to a specified decimal place.\nWhat is a Decimal Place?\n\
  Look at this..."
---

Par Dillion Megida

Python fournit de nombreuses méthodes mathématiques pour des opérations telles que les racines carrées, les exposants, et ainsi de suite. 

Dans cet article, je vais vous montrer comment arrondir un nombre à un nombre spécifique de décimales.

## Qu'est-ce qu'une décimale ?

Regardez ce nombre : **324,89**. 

Chaque chiffre ici a une position qui est appelée **valeur de position**. La valeur de position de :
* **3** est **centaines**
* **2** est **dizaines**
* **4** est **unités**
* **8** est **dixièmes**
* **9** est **centièmes**

Après la virgule, vous avez deux chiffres : **8**, puis **9**. La décimale d'un nombre est la position du chiffre après la virgule (à droite de celle-ci). 

Cette définition signifie que la décimale de **8** (en position des dixièmes) est 1, et celle de **9** (en position des centièmes) est 2.

## Comment arrondir à une certaine décimale

Que signifie alors arrondir à une certaine décimale ? Cela signifie que vous arrondissez un nombre à une décimale en fonction du chiffre qui suit. 

Si le chiffre après la décimale est 5 ou plus, le chiffre à la décimale est arrondi **+1**. Sinon, le chiffre à la décimale reste le même et le chiffre après la décimale est arrondi à 0.

Par exemple, disons que nous voulons arrondir **24,89** à **1** décimale. Ou vous pouvez dire arrondir **24,89** au dixième le plus proche.

Le chiffre **8** est à la 1ère décimale, et le chiffre après 8 est **9**. Puisque 9 est supérieur à 5, **24,89**, arrondi au dixième le plus proche sera **24,9**. 

Un autre exemple, prenons **24,82** et arrondissons-le à 1 décimale (au dixième le plus proche). Puisque **2** n'est pas supérieur à 5, **8** reste le même, et **2** est arrondi à 0 – ce qui donne **24,8**. 

## Comment arrondir une décimale en Python

Maintenant que vous comprenez comment arrondir une décimale, voyons comment le faire en Python.

Vous pouvez utiliser la fonction globale `round` pour arrondir les nombres à une décimale. La syntaxe est :

```python
round(nombre, decimale)
```

La fonction accepte le nombre et `decimale` comme arguments. `decimale` spécifie la décimale à laquelle vous souhaitez arrondir le nombre. Voici un exemple :

```python
num = 24.89

arrondi = round(num, 1)
print(arrondi)

# 24.9
```

Voici un autre exemple avec un nombre plus long :

```python
num = 20.4454

arrondi3 = round(num, 3)
# à 3 décimales

arrondi2 = round(num, 2)
# à 2 décimales

print(arrondi3)
# 20.445

print(arrondi2)
# 20.45
```

Pour `arrondi3`, le `num` est arrondi à 3 décimales. À la 3ème décimale se trouve **5**, et le chiffre qui suit est **4**. Puisque 4 n'est pas supérieur à 5, le chiffre 5 reste le même et 4 est arrondi à 0.

Pour `arrondi2`, le `num` est arrondi à 2 décimales. À la 2ème décimale se trouve **4**, et le chiffre qui suit est **5**. Puisque ce chiffre est supérieur ou égal à 5, le chiffre **4** est arrondi à 5.

## Conclusion

Arrondir les nombres peut être utile pour maintenir les nombres à virgule dans un nombre fixe de chiffres. 

Par exemple, cela est utile avec les devises qui n'acceptent que deux décimales (comme le dollar : 100,99 $). Dans les cas où un calcul pour un produit donne 50,678 $, vous pouvez vouloir l'arrondir à 2 décimales, comme ceci : 50,68 $. Ainsi, il est plus facile de donner à quelqu'un la valeur monétaire exacte.

Dans cet article, j'ai brièvement expliqué ce que sont les décimales et comment arrondir les nombres à certaines décimales en Python.