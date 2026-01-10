---
title: Fonction range() en Python – Expliquée avec des exemples de code
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-10-06T17:21:45.000Z'
originalURL: https://freecodecamp.org/news/python-range-function-explained-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/range
seo_title: Fonction range() en Python – Expliquée avec des exemples de code
---

function.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: "En Python, vous pouvez utiliser la fonction range() pour obtenir une séquence d'indices\
  \ pour parcourir un itérable. Vous utiliserez souvent range() en conjonction avec une\
  \ boucle for. \nDans ce tutoriel, vous apprendrez les différentes façons d'utiliser la fonction range() f..."
---

En Python, vous pouvez utiliser la fonction `range()` pour obtenir une séquence d'indices afin de parcourir un itérable. Vous utiliserez souvent `range()` en conjonction avec une boucle `for`. 

Dans ce tutoriel, vous apprendrez les différentes façons d'utiliser la fonction `range()` – avec des indices de début et de fin explicites, une taille de pas personnalisée et une taille de pas négative.

Commençons.

## Comprendre la fonction `range()` de Python

Avant d'examiner les différentes façons d'utiliser la fonction `range()`, vous devez comprendre comment elle fonctionne.

> La fonction `range()` retourne un objet range.    
> Cet objet range retourne à son tour les éléments successifs de la séquence lorsque vous l'itérez.

Comme indiqué ci-dessus, la fonction range ne retourne pas une liste d'indices. Elle retourne plutôt un objet range qui retourne les indices au fur et à mesure que vous en avez besoin. Cela la rend également efficace en mémoire.  

Vous pouvez utiliser la fonction `range()` avec la syntaxe générale suivante :

```
range(debut,fin,pas)
```

Lorsque vous utilisez cette syntaxe en conjonction avec une boucle, vous pouvez obtenir une séquence d'indices de `debut` jusqu'à, mais sans inclure `fin`, par pas de `pas`.

* Vous devez spécifier l'argument requis `fin`, qui peut être n'importe quel entier positif. Si vous spécifiez un nombre à virgule flottante à la place, vous rencontrerez une erreur `TypeError` comme montré :

```python
my_range = range(2.5)
```

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-24.png)

* Si vous ne spécifiez pas l'indice `debut`, l'indice de début par défaut de `0` est utilisé.
* Si vous ne spécifiez pas la valeur `pas`, la taille de pas par défaut de `1` est utilisée.

Dans les sections suivantes, vous apprendrez les différentes façons d'utiliser la fonction `range()`. 

## Comment utiliser la fonction `range()` de Python pour parcourir n'importe quel itérable

Comme mentionné dans la section précédente, vous n'avez besoin que d'un seul entier positif pour utiliser la fonction `range()`. La syntaxe est montrée ci-dessous :

```
range(fin)


```

Vous pouvez utiliser la ligne de code ci-dessus pour obtenir une séquence de `0` à `fin-1` : `0`, `1`, `2`, `3`,..., `fin-1`.  

➡ Considérez l'exemple suivant où vous appelez `range()` avec 5 comme argument. Et vous parcourez l'objet range retourné en utilisant une boucle `for` pour obtenir les indices 0,1,2,3,4 comme prévu.

```python
for index in range(5):
  print(index)
  
#Output
0
1
2
3
4
```

Si vous vous souvenez, tous les itérables en Python suivent un indexage à partir de zéro. C'est pourquoi il est pratique d'utiliser `range()` pour parcourir les itérables. 

Un itérable de longueur `len` a `0`, `1`, `2`, ..., `len-1` comme indices valides. Donc pour parcourir n'importe quel itérable, tout ce que vous avez à faire est de définir la valeur `fin` pour qu'elle soit égale à `len`. La séquence que vous obtiendrez – `0`, `1`, `2`, ..., `len-1` – est la séquence des indices valides.

➡ Prenons un exemple plus utile. Vous avez une liste `my_list`. Vous pouvez accéder à tous les éléments de la liste en connaissant leurs indices, et vous pouvez obtenir ces indices en utilisant `range()` comme montré ci-dessous :

```python
my_list = ["Python","C","C++","JavaScript","Julia","Rust","Go"]
for index in range(len(my_list)):
  print(f"À l'index {index}, nous avons {my_list[index]}")
```

Rappelez-vous, vous pouvez utiliser la fonction intégrée de Python `len` pour obtenir la longueur de n'importe quel itérable. Dans le code ci-dessus, vous utilisez à la fois les indices valides et les éléments de la liste à ces indices valides. Voici le résultat :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/image-25.png)

Remarquez comment `my_list` contient 7 éléments, et les indices obtenus vont de 0 à 6, comme prévu.

Parfois, vous pourriez avoir besoin d'utiliser des entiers négatifs à la place. Dans ce cas, si vous utilisez uniquement l'argument `fin`, vous n'obtiendrez pas le résultat souhaité, bien que le code ne génère pas d'erreur. 

C'est parce que la valeur `debut` par défaut est supposée être `0`, et vous ne pouvez pas compter de `0` à `-5`.

```python
for index in range(-5):
  print (index)
  
  
#Output
#RIEN ICI
```

## Comment utiliser la fonction `range()` de Python avec des indices de début et de fin explicites

Vous ne voulez peut-être pas toujours commencer à zéro. Vous pouvez commencer à n'importe quel indice arbitraire en définissant la valeur `debut` à l'indice à partir duquel vous souhaitez commencer. La syntaxe est la suivante :

```
range(debut,fin)
```

Dans ce cas, vous pourrez obtenir la séquence : `debut`, `debut + 1`, `debut + 2`, et ainsi de suite jusqu'à `fin-1`. 

➡ Dans l'exemple ci-dessous, vous commencez à 10, comptez jusqu'à mais sans inclure 15 par pas de 1.

```python
for index in range(10,15):
  print(index)

#Output
10
11
12
13
14
```

Dans la section précédente, vous avez vu comment l'utilisation de l'argument `fin` seul ne fonctionne pas lorsque vous avez besoin d'entiers négatifs. Cependant, lorsque vous spécifiez les indices `debut` et `fin` explicitement, vous pouvez également travailler avec des entiers négatifs.

➡ Dans cet exemple, vous essayez de compter de -5 par pas de 1. Gardez toujours à l'esprit que le comptage s'arrête à la valeur qui est inférieure d'une unité à l'indice `fin`.

```python
for index in range(-5,0):
  print(index)
  
#Output
-5
-4
-3
-2
-1
```

## Comment utiliser la fonction `range()` de Python **avec** une **taille de pas personnalisée**

Au lieu de parcourir un itérable séquentiellement, vous pouvez parfois vouloir le parcourir par strides, en accédant à chaque `k`-ième élément. C'est là que l'argument optionnel `pas` devient utile. La syntaxe générale est montrée ci-dessous :

```
range(debut,fin,pas)
```

Lorsque vous utilisez cette syntaxe et parcourez l'objet range, vous pouvez aller de `debut` à `fin-1` avec des strides de taille `pas`.

* Vous obtiendrez la séquence : `debut`, `debut + pas`, `debut + 2*pas`, et ainsi de suite jusqu'à `debut + k*pas` tel que `debut + k*pas` < `fin` et `debut + (k+1)*pas` > `fin`.

➡ Dans l'exemple ci-dessous, vous souhaitez aller de 0 à 20 par pas de 2. Remarquez comment le dernier indice imprimé est 19. C'est parce que, si vous faites un autre pas, vous serez à 21 qui est supérieur à 20. 

Rappelez-vous toujours, la dernière valeur que vous obtenez peut être aussi proche que possible de `fin`, mais ne peut jamais être `fin`.

```python
for index in range(1,20,2):
  print(index)

#Output
1
3
5
7
9
11
13
15
17
19
```

## Comment utiliser la fonction `range()` de Python **avec** une taille de pas négative

Jusqu'à présent, vous avez appris à utiliser la fonction `range()` avec des indices `debut` et `fin`, et une taille de pas spécifique, tout en comptant de `debut` à `fin`. 

Si vous avez besoin de compter à rebours à partir d'un entier, vous pouvez spécifier une valeur négative pour `pas`. La syntaxe générale est :

```
range(debut,fin,<pas_negatif>)
```

* L'objet range peut maintenant être utilisé pour retourner une séquence qui compte à rebours à partir de `debut` par pas de `pas_negatif`, jusqu'à mais sans inclure `fin`. 
* La séquence retournée est `debut`, `debut - pas_negatif`, `debut - 2*pas_negatif`, et ainsi de suite jusqu'à `debut - k*pas_negatif` tel que `debut - k*pas_negatif` > `fin` et `debut - (k+1)*pas_negatif` < `fin`.
* Il n'y a pas de valeur par défaut pour le pas négatif – vous devez définir `pas_negatif = -1` pour compter à rebours en couvrant chaque nombre.

➡ Dans cet exemple, vous souhaitez compter à rebours à partir de 20 par pas de -2. La séquence est donc 20, 18, 16, et ainsi de suite jusqu'à 2. Si vous allez deux pas plus bas, vous atteindrez 0, ce que vous ne pouvez pas faire car il est inférieur à la valeur d'arrêt de 1.

```python
for index in range(20,1,-2):
  print(index)
  
#Output
20
18
16
14
12
10
8
6
4
2
```

Il est facile de voir que `debut` > `fin` pour pouvoir compter à rebours. 

```python
for index in range(10,20,-1):
  print(index)
  
 #Ouput
 #Rien n'est imprimé - la séquence est vide.
```

➡ Dans l'exemple ci-dessus, vous essayez de compter à rebours de 10 à 20, ce qui est impossible. Et vous n'obtenez aucune sortie, ce qui est attendu.

## Comment utiliser les fonctions `range()` et `reversed()` de Python pour inverser une séquence

Si vous avez besoin d'accéder aux éléments d'un itérable dans l'ordre inverse, vous pouvez utiliser la fonction `range()` couplée avec la fonction `reversed()`.

> La fonction intégrée `reversed()` de Python retourne un itérateur inverse sur les valeurs d'une séquence donnée.

➡ Prenons notre tout premier exemple, où nous avons utilisé `range(5)`. Dans l'exemple ci-dessous, nous appelons `reversed()` sur l'objet range. Et nous voyons que nous avons compté à rebours de 4 à 0. 

```python
for index in reversed(range(5)):
  print (index)
  
#Output
4
3
2
1
0
```

Comme vous pouvez le voir, cela équivaut à utiliser `range(4,-1,-1)`. Si vous préférez, vous pouvez utiliser la fonction `reversed()` au lieu de l'argument `pas_negatif` discuté dans la section précédente.

## Conclusion

Dans ce tutoriel, vous avez appris les différentes façons d'utiliser la fonction `range()`. Vous pouvez essayer quelques exemples pour obtenir une séquence différente à chaque fois. Cette pratique vous aidera à utiliser `range()` efficacement lors du parcours d'itérables.

Bon codage ! Jusqu'au prochain tutoriel.👋