---
title: 'TypeError: can''t multiply sequence by non-int of type ''float'' [RÉSOLU]'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-05-24T23:30:53.000Z'
originalURL: https://freecodecamp.org/news/typeerror-cant-multiply-sequence-by-non-int-of-type-float-solved
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/jake-walker-MPKQiDpMyqU-unsplash.jpg
tags:
- name: error
  slug: error
- name: error handling
  slug: error-handling
- name: Python
  slug: python
seo_title: 'TypeError: can''t multiply sequence by non-int of type ''float'' [RÉSOLU]'
seo_desc: "When coding, you're likely to encounter errors. Error messages, in most\
  \ cases, help you understand what the error is about. And understanding an error\
  \ message is one of the steps in solving an error. \nIn this article, we'll talk\
  \ about an error in Pyt..."
---

Lorsque vous codez, vous êtes susceptible de rencontrer des erreurs. Les messages d'erreur, dans la plupart des cas, vous aident à comprendre de quoi il s'agit. Et comprendre un message d'erreur est l'une des étapes pour résoudre une erreur. 

Dans cet article, nous allons parler d'une erreur en Python – l'erreur "TypeError: can't multiply sequence by non-int of type 'float'". 

Nous allons comprendre quel type d'erreur c'est, pourquoi elle se produit, et comment la corriger avec différentes solutions et exemples de code. 

## Pourquoi l'erreur "TypeError: can’t multiply sequence by non-int of type ‘float’" se produit-elle ?

Eh bien, pour comprendre cette erreur, examinons le message d'erreur et voyons ce que nous pouvons en tirer. Le premier mot dit **TypeError**.

Alors, qu'est-ce qu'une TypeError ? Une TypeError en Python se produit lorsque les types de données impliqués dans une opération sont incompatibles pour ladite opération. Donc, cela se produit lorsqu'une valeur inattendue est vue dans une opération. Vous comprendrez mieux cela avec quelques exemples de code.

Le reste du message d'erreur met l'accent sur le mot "float". Découvrons pourquoi. 

```python
print("John " * 2)
# John John  
```

Dans le code ci-dessus, nous avons multiplié une chaîne par un entier (2). Cela a abouti à la duplication de la chaîne. 

De même, nous allons multiplier un tuple avec un entier comme montré ci-dessous :

```python
names = ("John ", "Jane ")

print(names * 2)
# ('John ', 'Jane ', 'John ', 'Jane ')
```

Nous avons les valeurs dans le tuple dupliquées après une opération de multiplication. Le tuple a été multiplié par 2. Cela est possible parce que nous multiplions par un entier.

Voici ce qui se passe lorsque nous essayons la même chose en utilisant un nombre à virgule flottante :

```python
print("John " * 2.0)
# TypeError: can't multiply sequence by non-int of type 'float'  
```

```python
names = ("John ", "Jane ")

print(names * 2.0)
# TypeError: can't multiply sequence by non-int of type 'float'
```

L'erreur "TypeError: can't multiply sequence by non-int of type 'float'" nous est lancée. Cela se produit parce que nous ne pouvons pas multiplier une chaîne et un nombre à virgule flottante ou un tuple et un nombre à virgule flottante. 

Généralement, cette erreur se produit lorsque nous effectuons une opération avec un type de données qui ne devrait pas être multiplié avec un nombre à virgule flottante.

Dans la section suivante, nous allons examiner certaines des façons de résoudre cette erreur.

## Comment résoudre l'erreur TypeError: can’t multiply sequence by non-int of type ‘float’

Cette section sera divisée en sous-sections car il existe diverses façons de résoudre cette erreur. Chaque sous-section aura un ou plusieurs exemples de code.

### Solution 1 – Convertir le Float en Entier

Pour résoudre l'erreur "TypeError: can't multiply sequence by non-int of type 'float'", nous pouvons convertir le float en entier. 

Voici un exemple :

```python
names = ("John ", "Jane ")

print(names * int(2.0))
# ('John ', 'Jane ', 'John ', 'Jane ')
```

Maintenant, nous obtenons le résultat attendu – le tuple a été dupliqué. 

Nous avons passé le nombre à virgule flottante dans une fonction `int()` afin de le convertir d'un float en un entier. Cela élimine l'erreur.

### Solution 2 - Convertir la Chaîne en Entier ou Float

Cette solution est importante lorsque la chaîne est d'une valeur numérique. Nous pouvons essayer d'obtenir une entrée utilisateur puis effectuer une opération de multiplication sur celle-ci.

```python
userId = "10"

print(float(userId) * 2.0)
# 20.0

```

Afin d'effectuer l'opération sans obtenir d'erreur, nous avons converti la chaîne en un type de données float en utilisant la fonction `float()`.  

Nous pouvons également la convertir en un entier en utilisant la fonction `int()` pour obtenir le même résultat. C'est-à-dire :

```python
userId = "10"

print(int(userId) * 2.0)
# 20.0

```

### Solution 3 – Convertir l'Entrée Utilisateur en Entier ou Float

Cette solution s'applique aux situations où nous effectuons une opération après avoir obtenu une entrée d'un utilisateur. 

Jetez un coup d'œil à l'exemple ci-dessous :

```python
userId = input("Enter user ID: ")
print(userId * 2.0)
# TypeError: can't multiply sequence by non-int of type 'float'
```

Cela génère une erreur après avoir entré un nombre comme identifiant utilisateur.

Pour corriger cela, nous allons convertir le résultat de l'entrée de l'utilisateur avant d'effectuer l'opération.

Voici comment nous pouvons faire cela :

```python
userId = int(input("Enter user ID: "))
print(userId * 2.0)


```

Maintenant, le programme devrait fonctionner parfaitement lorsqu'un utilisateur tape un nombre car il sera converti en un entier : `int(input("Enter user ID: "))`. 

Nous pouvons faire la même chose en utilisant la fonction `float()` qui convertit l'entrée utilisateur en un nombre à virgule flottante.

Voici un exemple :

```python
userId = float(input("Enter user ID: "))
print(userId * 2.0)

```

## Conclusion

Dans cet article, nous avons parlé de l'erreur "TypeError: can't multiply sequence by non-int of type 'float'" en Python. 

Nous avons commencé par comprendre ce que signifie le message d'erreur en définissant une TypeError. 

Nous avons ensuite vu quelques exemples montrant pourquoi le type de données float provoque cette erreur. 

Pour corriger l'erreur, nous avons examiné trois solutions différentes avec des exemples relatifs aux différentes situations où cette erreur était susceptible de se produire.

Bon codage !