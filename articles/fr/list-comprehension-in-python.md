---
title: Compréhension de liste en Python expliquée pour les débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-07T17:25:39.000Z'
originalURL: https://freecodecamp.org/news/list-comprehension-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/list-comprehension-1.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: Compréhension de liste en Python expliquée pour les débutants
seo_desc: 'By Buggy Programmer

  List comprehension is an easy to read, compact, and elegant way of creating a list
  from any existing iterable object. Basically, it''s a simpler way to create a new
  list from the values in a list you already have.

  It is generally a...'
---

Par Buggy Programmer

La compréhension de liste est une méthode facile à lire, compacte et élégante pour créer une liste à partir de n'importe quel objet itérable existant. En gros, c'est une manière plus simple de créer une nouvelle liste à partir des valeurs d'une liste que vous avez déjà.

C'est généralement une seule ligne de code enfermée dans des crochets. Vous pouvez l'utiliser pour filtrer, formater, modifier ou effectuer d'autres petites tâches sur des itérables existants tels que des chaînes de caractères, des tuples, des ensembles, des dataframes, des listes de tableaux, et ainsi de suite.

Dans cette leçon courte, nous verrons différentes manières de créer des compréhensions de liste et quelques-unes de ses variantes comme :

* Compréhension de liste simple
* Compréhension de liste avec des conditions if simples et imbriquées
* Compréhension de liste avec des conditions if et else simples et multiples
* Compréhension de liste avec des boucles for imbriquées

En plus de cela, nous examinerons également les concepts suivants :

* Boucles for vs compréhension de liste
* Quels sont les avantages de la compréhension de liste ?
* Quand utiliser et quand éviter la compréhension de liste.

## Qu'est-ce que la compréhension de liste en Python ?

Alors, commençons par la syntaxe de la compréhension de liste. La compréhension de liste est une seule ligne de code que vous écrivez à l'intérieur des crochets. Elle a trois composants :

1. Boucle for
2. Condition et expression
3. Sortie


![Syntaxe de la compréhension de liste, comment fonctionne la compréhension de liste](https://www.freecodecamp.org/news/content/images/2021/07/list-comprehension.png)
_**Syntaxe de la compréhension de liste** - Crédit [buggyprogrammer](http://buggyprogrammer.com/)_

### Exemple de compréhension de liste simple

L'extrait de code ci-dessous est un exemple de la compréhension de liste la plus simple. Ici, nous parcourons simplement la liste `lst` et stockons tous ses éléments dans la liste `a` :

```python
lst = [1,2,3,4,5,6,7,8,9,10]
# compréhension de liste simple
a = [x for x in lst]
print(a)
 
# sortie
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Le code ci-dessus est équivalent à ceci :

```python
for x in lst:
    a.append(x)
```

Pour y parvenir, nous n'avons même pas besoin de la méthode append dans une compréhension de liste.

Maintenant, dans le code ci-dessus (compréhension de liste), vous pouvez utiliser n'importe quelle expression pour modifier les éléments de `lst`, par exemple :

```python
# ajouter un nombre à chaque élément de lst et le stocker dans a
a = [x+1 for x in lst]
 
# soustraire un nombre à chaque élément de lst et le stocker dans a
a = [x-1 for x in lst]
 
# multiplier un nombre à chaque élément de lst et le stocker dans a
a = [x*2 for x in lst]
```

## Compréhension de liste avec des conditions if simples et imbriquées

Dans la compréhension de liste, nous pouvons également ajouter une condition `if`, qui peut nous aider à filtrer les données. Par exemple, dans le code ci-dessous, nous stockons toutes les valeurs de `lst` dans la liste `c` dont les valeurs sont supérieures à 4 :

```python
lst = [1,2,3,4,5,6,7,8,9,10]
# avec condition if
c = [x for x in lst if x > 4]
print(c)
 
# sortie
[5, 6, 7, 8, 9, 10]
```

Le code ci-dessus est équivalent à ceci :

```python
for x in lst:
    if x > 4:
        a.append(x)

```

Nous pouvons également ajouter une condition `if imbriquée` à notre compréhension de liste. Par exemple, dans le code ci-dessous, nous stockons tous les éléments de `lst` dans la liste `d` dont les valeurs sont supérieures à 4 et divisibles par 2 :

```python
# avec plusieurs if 
d = [x for x in lst if x > 4 if x%2 == 0]
 
# sortie
[6, 8, 10]

```

Le code ci-dessus est équivalent à ceci :

```python
for x in lst:
    if x > 4:
        if x % 2 == 0:
            a.append(x)
```

## Compréhension de liste avec des conditions if et else simples et multiples

D'accord, maintenant nous allons voir comment nous pouvons ajouter `else` avec `if` dans la compréhension de liste.

Ici, nous avons créé une compréhension de liste simple qui stockera toutes les valeurs de `lst` dans la liste `e` dont les valeurs sont supérieures à 4 – sinon, si les valeurs sont inférieures à 4, elle stockera la chaîne de caractères `"moins que 4"` à sa place.

```python
lst = [1,2,3,4,5,6,7,8,9,10]
# avec condition if et else
e = [x if x > 4 else 'moins que 4' for x in lst]
print(e)
 
# sortie
['moins que 4', 'moins que 4', 'moins que 4', 'moins que 4', 5, 6, 7, 8, 9, 10]
```

Le code ci-dessus est équivalent à ceci :

```python
for x in lst:
    if x > 4:
        d.append(x)
    else: 
        d.append('moins que 4')
```

Maintenant, voyons la compréhension de liste avec plusieurs `if et else`.

Dans l'exemple ci-dessous, nous stockons la chaîne de caractères `"Deux"` si la valeur est divisible par 2. Ou si la valeur est divisible par 3, nous stockons `"Trois"`, sinon nous stockons `"pas 2 & 3"`.

```python
# avec plus d'une condition if et else
f = ['Deux' if x%2 == 0 else "Trois" if x%3 == 0 else 'pas 2 & 3' for x in lst]
print(f)
 
# sortie
['pas 2 & 3', 'Deux', 'Trois', 'Deux', 'pas 2 & 3', 'Deux', 'pas 2 & 3', 'Deux', 'Trois', 'Deux']
```

Alors, comment cela fonctionne-t-il ? Pour comprendre cela, nous pouvons diviser toute la condition en trois parties, après chaque else :

```python
'Deux' if x%2 == 0 else "Trois" if x%3 == 0 else 'pas 2 & 3'
```

Ici, si la première condition `if` est vraie, alors elle prendra la valeur `"Deux"` – sinon, elle passera à la deuxième condition `if`, au lieu de stocker une autre valeur, tout comme la commande `elif`.

Maintenant, dans la deuxième condition `if`, elle enregistrera `"Trois"` si l'instruction est vraie. Sinon, elle vérifiera la condition suivante, que nous n'avons pas. Donc, quelle que soit la valeur qui suit après `else` sera stockée, qui dans notre cas est une chaîne de caractères `"pas 2 & 3"`.

Donc, de manière traditionnelle, nous pouvons écrire tout le code comme ceci :

```python
for x in lst:
    if x%2 == 0:
        f.append('Deux')
    elif x%3 == 0:
        f.append('Trois')
    else: 
        f.append('pas 2 & 3')
```

Voyez-vous la puissance de la compréhension de liste ? Elle effectue la tâche en une seule ligne, là où une boucle for traditionnelle en a besoin de 7.

**Vous pouvez également lire cet article 👉** [Résoudre le défi Python fizzbuzz avec la compréhension de liste](https://buggyprogrammer.com/python-fizzbuzz/) pour en savoir plus.

## Compréhension de liste avec une boucle for imbriquée

D'accord ! Maintenant, nous allons voir comment la compréhension de liste fonctionne avec une `boucle for imbriquée`.

Pour comprendre ce qui se passe ici, regardons l'exemple ci-dessous. Ici, nous générons toutes les combinaisons possibles de [1,2,3] et [3,2,1].

```python
lst = [1,2,3]
lst_rev = [3,2,1]
g = [(x,y) for x in lst for y in lst_rev]
print(g)
 
#sortie
[(1, 3), (1, 2), (1, 1), (2, 3), (2, 2), (2, 1), (3, 3), (3, 2), (3, 1)]

```

Le code ci-dessus peut également être écrit comme :

```python
for x in lst:
    for y in lst_rev:
        f.append((x,y))
```

D'accord, maintenant, comme promis, voyons la comparaison entre les boucles for et la compréhension de liste.

## Boucles For vs Compréhension de liste

Ci-dessus, nous avons vu comment la compréhension de liste a pu accomplir une tâche en une seule ligne, là où une boucle for en avait besoin de plusieurs.

La compréhension de liste n'est pas seulement compacte, mais elle est également plus facile à lire et plus rapide que les boucles for en termes de performance.

Dans certains cas, la compréhension de liste semble être deux fois plus rapide qu'une boucle for. Si vous voulez en savoir plus sur la performance de la compréhension de liste, vous pouvez en lire plus [ici](https://switowski.com/blog/for-loop-vs-list-comprehension).

Mais si vous voulez exécuter plus d'une condition simple, la compréhension de liste ne pourra pas la gérer sans sacrifier la lisibilité. C'est le principal problème avec la compréhension de liste.

## Avantages de la compréhension de liste

En plus d'être simple, compacte et plus rapide, la compréhension de liste est également fiable dans de nombreuses situations différentes. Et vous pouvez l'utiliser dans une variété de circonstances.

Vous pouvez utiliser la compréhension de liste pour mapper et filtrer en plus de la génération de liste de base. Vous n'avez pas besoin d'adopter une nouvelle stratégie pour chaque situation. C'est l'une des raisons pour lesquelles elle est considérée comme plus pythonique qu'une boucle for.

## Quand utiliser la compréhension de liste (et quand l'éviter)

Vous pouvez utiliser la compréhension de liste si vous effectuez un filtrage simple, des modifications ou une tâche de formatage sur d'autres objets itérables. C'est également un bon choix si vous voulez garder votre code compact et lisible.

De plus, vous pouvez l'utiliser lorsque même un petit peu de performance compte pour vous.

Mais vous devriez éviter d'utiliser la compréhension de liste si vous avez trop de conditions à ajouter pour le filtrage ou la modification, car cela rendra votre code plus complexe et plus difficile à lire.

## Conclusion

Dans cet article, nous avons appris ce qu'est la compréhension de liste, quels sont ses avantages et quand nous devons l'utiliser. Et nous avons vu comment la compréhension de liste est simple, facile à lire, compacte et plus rapide qu'une boucle for.

Nous avons également appris comment écrire une compréhension de liste avec ou sans condition, avec des if et else imbriqués, et avec une boucle for imbriquée.

Si vous avez aimé cet article, alors vous aimerez définitivement mes autres blogs aussi. Vous pouvez visiter mon site personnel [ici](http://buggyprogrammer.com/).