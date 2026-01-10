---
title: '%.2f en Python – Que signifie-t-il ?'
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2022-06-22T18:30:58.000Z'
originalURL: https://freecodecamp.org/news/2f-in-python-what-does-it-mean
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/susan-holt-simpson-GQ327RPuxhI-unsplash.jpg
tags:
- name: Math
  slug: math
- name: Python
  slug: python
seo_title: '%.2f en Python – Que signifie-t-il ?'
seo_desc: "In Python, there are various methods for formatting data types. \nThe %f\
  \ formatter is specifically used for formatting float values (numbers with decimals).\
  \ \nWe can use the %f formatter to specify the number of decimal numbers to be returned\
  \ when a fl..."
---

En Python, il existe diverses méthodes pour formater les types de données. 

Le formateur `%f` est spécifiquement utilisé pour formater les valeurs flottantes (nombres avec décimales). 

Nous pouvons utiliser le formateur `%f` pour spécifier le nombre de décimales à retourner lorsqu'un nombre à virgule flottante est arrondi. 

## Comment utiliser le formateur `%f` en Python

Dans cette section, vous verrez quelques exemples sur la façon d'utiliser le formateur `%f` et les différents paramètres avec lesquels il peut être utilisé pour retourner des résultats variés.

Voici le premier exemple :

```python
floatNumber = 1.9876

print("%f" % floatNumber)
# 1.987600
```

L'utilisation de `%f` dans l'exemple ci-dessus a ajouté deux zéros au nombre. Mais ce n'est pas très spécial. Nous verrons bientôt ce que nous pouvons faire d'autre pour modifier la valeur résultante.

Notez que le formateur `%f` doit être imbriqué dans des guillemets et doit être séparé du nombre flottant qu'il formate par un opérateur modulo (%) : `"%f" % floatNumber`.

Regardons un autre exemple.

```python
floatNumber = 1.9876

print("%.1f" % floatNumber)
# 2.0
```

Dans le code ci-dessus, nous avons ajouté .1 entre % et f dans l'opérateur `%f`. Cela signifie que nous voulons que le nombre soit arrondi à une décimale.

Notez que vous obtiendrez un résultat similaire à celui du premier exemple si vous omettez le point (**.**) qui précède le chiffre que nous avons passé entre % et f.

La valeur résultante dans notre exemple est 2.0, qui a été retournée lorsque 1.9876 a été arrondi à une décimale.

Utilisons `%.2f` et voyons ce qui se passe.

```python
floatNumber = 1.9876

print("%.2f" % floatNumber)
# 1.99
```

Comme prévu, le nombre à virgule flottante (1.9876) a été arrondi à deux décimales – 1.99. Donc `%.2f` signifie arrondir à deux décimales.

Vous pouvez jouer avec le code pour voir ce qui se passe lorsque vous changez le nombre dans le formateur.

## Comment utiliser le formateur `%d` en Python

Une autre méthode de formatage que nous pouvons utiliser avec les nombres à virgule flottante en Python est le formateur `%d`. Cela retourne le nombre entier dans un nombre à virgule flottante.

Voici un exemple :

```python
floatNumber = 1.9876

print("%d" % floatNumber)
# 1
```

Dans l'exemple ci-dessus, nous avons créé un nombre à virgule flottante : `floatNumber = 1.9876`.

Lorsque la variable `floatNumber` a été formatée en utilisant `%d`, seul 1 a été retourné.

Le formateur `%d` ignore les décimales et retourne uniquement le nombre entier.

## Résumé

Dans cet article, nous avons parlé du formateur `%f` en Python. Vous l'utilisez pour formater les nombres à virgule flottante.

Selon les paramètres fournis, le formateur `%f` arrondit une valeur flottante à la décimale la plus proche fournie.

Nous avons également parlé du formateur `%d` qui retourne uniquement un nombre entier à partir d'un nombre à virgule flottante.

Bonne programmation !