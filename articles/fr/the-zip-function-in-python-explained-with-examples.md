---
title: Fonction Python zip() – Expliquée avec des exemples de code
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2021-07-23T17:25:34.000Z'
originalURL: https://freecodecamp.org/news/the-zip-function-in-python-explained-with-examples
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Python-zip
seo_title: Fonction Python zip() – Expliquée avec des exemples de code
---

function.png
tags:
- name: Python
  slug: python
seo_title: null
seo_desc: 'Avez-vous déjà eu besoin de parcourir plusieurs itérables en parallèle lors de la programmation en Python ?

Dans ce tutoriel, nous utiliserons la fonction zip() de Python pour effectuer efficacement une itération parallèle sur plusieurs itérables.

Voici ce que nous allons couvrir dans cet article :

* [Comment utiliser l'opérateur "in" en Python pour parcourir les itérables](#heading-comment-utiliser-loperateur-in-en-python-pour-parcourir-les-iterables)
* [Pourquoi l'utilisation de l'objet range() de Python n'est pas toujours un choix optimal](#heading-pourquoi-lutilisation-de-lobjet-range-de-python-nest-pas-toujours-un-choix-optimal)
* [Comment fonctionne la fonction zip() de Python](#heading-comment-fonctionne-la-fonction-zip-de-python)
* [Comment la fonction zip() crée un itérateur de tuples](#heading-comment-la-fonction-zip-cree-un-iterateur-de-tuples)
* [Comment utiliser la fonction zip() de Python - Essayez par vous-même !](#heading-comment-utiliser-la-fonction-zip-de-python-essayez-par-vous-meme)
* [Que se passe-t-il lorsque les itérables sont de longueurs différentes ?](#heading-que-se-passe-t-il-lorsque-les-iterables-sont-de-longueurs-differentes)
* [Que se passe-t-il lorsque vous passez un ou aucun itérable à la fonction zip() ?](#heading-que-se-passe-t-il-lorsque-vous-passez-un-ou-aucun-iterable-a-la-fonction-zip)
* [Comment utiliser la fonction zip_longest() en Python](#heading-comment-utiliser-la-fonction-ziplongest-en-python)

## Comment utiliser l'opérateur "in" en Python pour parcourir les itérables

Avant d'aller de l'avant et d'apprendre la fonction `zip()`, revoyons rapidement comment nous utilisons l'opérateur `in` avec une boucle `for` pour accéder aux éléments d'un itérable (listes, tuples, dictionnaires, chaînes de caractères, etc.). Le snippet ci-dessous montre la syntaxe générale :

```python
for item in list_1:
	# faire quelque chose sur item
```

En termes simples, nous disons à l'interpréteur Python : "_Hey là ! S'il te plaît, parcours `list_1` pour accéder à chaque `item` et fais une opération sur chaque `item`._"

Et si nous avions plus d'une liste (ou tout itérable) ? Disons, `N` listes – vous pouvez insérer votre nombre préféré à la place de `N`. Les choses peuvent sembler un peu difficiles maintenant, et l'approche suivante ne fonctionnera pas :

```python
# Exemple - 2 listes, list_1 et list_2

for i1 in list_1:
	for i2 in list_2:
    	 # faire quelque chose sur i1 et i2
```

Veuillez noter que le code ci-dessus :

* accède d'abord au premier élément de `list_1`, 
* puis parcourt `list_2` en accédant à chaque élément de `list_2`,
* puis accède au deuxième élément de `list_1`,
* et parcourt à nouveau toute la `list_2`, et 
* fait cela jusqu'à ce qu'il parcourt toute la `list_1`

Clairement, ce n'est pas ce que nous voulons. Nous devons pouvoir accéder aux éléments à un index particulier des deux listes. C'est précisément ce qu'on appelle l'_itération parallèle_.

## Pourquoi l'utilisation de l'objet range() de Python n'est pas toujours un choix optimal

Vous pourriez penser à utiliser l'objet `range()` avec la boucle `for`. "_Si je sais que toutes les listes ont le même nombre d'éléments, ne puis-je pas simplement utiliser l'`index` pour accéder à chacune de ces listes, et extraire l'élément à l'`index` spécifié ?_"

Eh bien, essayons. Le code est dans le snippet ci-dessous. Vous savez que toutes les listes – `list_1`, `list_2`,..., `list_N` – contiennent le même nombre d'éléments. Et vous créez un objet `range()` comme montré ci-dessous et utilisez l'index `i` pour accéder à l'élément à la position `i` dans chacun des itérables.

```python
for i in range(len(list_1)):
	# faire quelque chose sur list_1[i],list_2[i],list_3[i],...,list_N[i]
```

Comme vous l'avez peut-être deviné maintenant, cela fonctionne comme prévu _uniquement lorsque tous les itérables contiennent le même nombre d'éléments_. 

Considérez le cas où une ou plusieurs des listes sont mises à jour – disons, une liste peut avoir un élément supprimé, et une autre peut avoir un élément ajouté. Cela causerait de la confusion :

* Vous pourriez rencontrer des `IndexErrors` car vous accédez à des éléments à des _indices qui ne sont plus valides_ parce que l'élément à l'index a été supprimé, ou
* Vous pourriez _ne pas du tout accéder aux nouveaux éléments ajoutés_ car ils sont à des indices non actuellement dans la plage des indices accessibles.

Voyons maintenant comment la fonction `zip()` de Python peut nous aider à itérer à travers plusieurs listes en parallèle. Lisez la suite pour le découvrir.

## Comment fonctionne la fonction zip() de Python

Commençons par consulter la documentation de `zip()` et analysons-la dans les sections suivantes.

**Syntaxe** : `zip(*iterables)` – la fonction `zip()` prend un ou plusieurs itérables comme arguments.

> _Crée un itérateur qui agrège les éléments de chacun des itérables._  
> 1. Retourne un itérateur de tuples, où le _i-ème_ tuple contient le _i-ème_ élément de chacune des séquences ou itérables d'arguments.   
> 2. L'itérateur s'arrête lorsque l'itérable d'entrée le plus court est épuisé.   
> 3. Avec un seul argument itérable, il retourne un itérateur de 1-tuples.   
> 4. Sans arguments, il retourne un itérateur vide. – Documentation Python

## Comment la fonction zip() crée un itérateur de tuples

L'illustration suivante nous aide à comprendre comment la fonction `zip()` fonctionne en créant un _itérateur de tuples_ à partir de deux listes d'entrée, `L1` et `L2`. Le résultat de l'appel de `zip()` sur les itérables est affiché à droite.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/zipf.png)

* Remarquez comment le premier tuple (à l'index `0`) à droite contient 2 éléments, à l'index `0` dans `L1` et `L2`, respectivement.
* Le deuxième tuple (à l'index `1`) contient les éléments à l'index `1` dans `L1` et `L2`.
* En général, le tuple à l'index `i` contient les éléments à l'index `i` dans `L1` et `L2`.

Essayons quelques exemples dans la section suivante.

## Comment utiliser la fonction zip() de Python – Essayez par vous-même !

Essayez d'exécuter les exemples suivants dans votre IDE préféré.

En premier exemple, prenons deux listes `L1` et `L2` qui contiennent chacune 5 éléments. Appelons la fonction `zip()` et passons `L1` et `L2` comme arguments.

```python
L1 = [1,2,3,4,5]
L2 = ['a','b','c','d','e']

zip_L1L2 = zip(L1,L2)

print(zip_L1L2)
# Exemple de sortie
<zip object at 0x7f92f44d5550>

```

Convertissons l'objet zip en une liste et affichons-le, comme montré ci-dessous.

```python
print(list(zip_L1L2))

# Sortie
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
```

### Que se passe-t-il lorsque les itérables sont de longueurs différentes ?

Si vous revenez à la documentation, le deuxième élément de la liste numérotée indique : "_L'itérateur s'arrête lorsque l'itérable d'entrée le plus court est épuisé._"

Contrairement à l'utilisation de l'objet `range()`, l'utilisation de `zip()` ne génère pas d'erreurs lorsque tous les itérables sont de longueurs potentiellement différentes. Vérifions cela comme montré ci-dessous.

Retirons `'e'` de `L2`, et répétons les étapes ci-dessus.

```python
L1 = [1,2,3,4,5]
L2 = ['a','b','c','d']

zip_L1L2 = zip(L1,L2)

print(list(zip_L1L2))

# Sortie
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
```

Nous voyons maintenant que la liste de sortie ne contient que 4 tuples et que l'élément `5` de `L1` n'a pas été utilisé. Jusqu'à présent, tout va bien ! 

### Que se passe-t-il lorsque vous passez un ou aucun itérable à la fonction zip() ?

Revisitons les éléments 3 et 4 de la documentation.

> "Avec un seul argument itérable, il retourne un itérateur de 1-tuples.   
> Sans arguments, il retourne un itérateur vide."

Allons-y et vérifions cela. Observez comment nous obtenons des 1-tuples lorsque nous passons uniquement `L1` dans le snippet de code ci-dessous :

```python
L1 = [1,2,3,4,5]
zip_L1 = zip(L1)
print(list(zip_L1))

# Sortie
[(1,), (2,), (3,), (4,), (5,)]

```

Lorsque nous appelons la fonction `zip()` sans arguments, nous obtenons une liste vide, comme montré ci-dessous :

```python
zip_None = zip()
print(list(zip_None))

# Sortie
[]
```

Créons maintenant un exemple plus intuitif. Le snippet de code ci-dessous montre comment nous pouvons utiliser `zip()` pour combiner 3 listes et effectuer des opérations significatives. 

Étant donné une liste de fruits, leurs prix et les quantités que vous avez achetées, le montant total dépensé pour chaque article est affiché.

```python
fruits = ["apples","oranges","bananas","melons"]
prices = [20,10,5,15]
quantities = [5,7,3,4]

for fruit, price, quantity in zip(fruits,prices,quantities):
  print(f"Vous avez acheté {quantity} {fruit} pour ${price*quantity}")
  
# Sortie
Vous avez acheté 5 apples pour $100
Vous avez acheté 7 oranges pour $70
Vous avez acheté 3 bananas pour $15
Vous avez acheté 4 melons pour $60
  
```

Maintenant, nous comprenons comment la fonction `zip()` fonctionne, et nous connaissons sa limitation que l'itérateur s'arrête lorsque l'itérable le plus court est épuisé. Voyons donc comment nous pouvons surmonter cette limitation en utilisant la fonction `zip_longest()` en Python.

## Comment utiliser la fonction zip_longest() en Python

Importons la fonction `zip_longest()` du module `itertools` :

```
from itertools import zip_longest
```

Essayons maintenant un exemple précédent où `L2` contient un élément de moins que `L1`.

```python
L1 = [1,2,3,4,5]
L2 = ['a','b','c','d']

zipL_L1L2 = zip_longest(L1,L2)

print(list(zipL_L1L2))

# Sortie
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, None)]
```

Remarquez comment l'élément `5` de `L1` est toujours inclus. Mais comme il n'y a pas d'élément correspondant dans `L2`, le deuxième élément dans le dernier tuple est `None`. 

Vous pouvez le personnaliser davantage si vous le souhaitez. Par exemple, vous pouvez remplacer `None` par un terme plus indicatif tel que `Empty`, `Item Not Found`, etc. Tout ce que vous avez à faire est de définir l'argument optionnel `fillvalue` avec le terme que vous souhaitez afficher lorsqu'il n'y a pas d'élément correspondant dans un itérable lorsque vous appelez `zip_longest()`.

J'espère que vous comprenez maintenant les fonctions `zip()` et `zip_longest()` de Python.

Merci d'avoir lu ! À bientôt dans un autre article.