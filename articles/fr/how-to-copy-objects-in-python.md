---
title: Comment copier des objets en Python
subtitle: ''
author: Sara Jadhav
co_authors: []
series: null
date: '2025-04-17T18:57:20.271Z'
originalURL: https://freecodecamp.org/news/how-to-copy-objects-in-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744913871670/5ed210bd-1d42-436e-907b-5b304010dbd7.png
tags:
- name: Python
  slug: python
seo_title: Comment copier des objets en Python
seo_desc: In this tutorial, you’ll learn about copying objects in Python using the
  copy module. We’ll cover how to use the copy module and when to use its copy() function
  and deepcopy() function, depending on the scenario. You’ll also learn which way
  of copyin...
---

Dans ce tutoriel, vous apprendrez à copier des objets en Python en utilisant le module `copy`. Nous aborderons comment utiliser le module `copy` et quand utiliser sa fonction `copy()` et sa fonction `deepcopy()`, selon le scénario. Vous apprendrez également quelle méthode de copie est adaptée aux objets mutables et immutables.

À la fin de ce tutoriel, vous comprendrez :

* Qu'est-ce que le module `copy` ?
  
* La différence entre la copie et la référence.
  
* La différence entre une copie profonde et une copie superficielle.
  
* Comment effectuer une copie superficielle et une copie profonde des objets en Python.
  
* La différence de référence pour les objets immutables et les objets mutables.
  

## Prérequis

Pour tirer le meilleur parti de ce tutoriel, vous devez avoir une compréhension de base des éléments suivants :

1. Connaissances fondamentales de la programmation et de sa terminologie (telles que les objets, les adresses mémoire, etc.)
  
2. Connaissances de base de la programmation Python, en particulier (pour ce tutoriel),
  
  * Fonction `id()` : Affiche l'adresse mémoire de l'objet passé en argument.
      
  * Structures de données : Dictionnaires et Listes.
      
  * Modules : importation et utilisation dans le programme. Compréhension de base des méthodes et des fonctions.
      

## Table des matières :

1. [Qu'est-ce que le module Copy en Python ?](#heading-questce-que-le-module-copy-en-python)
  
  * [Pourquoi ne pouvons-nous pas simplement utiliser l'opérateur d'affectation ?](#heading-pourquoi-ne-pouvons-nous-pas-simplement-utiliser-loperateur-daffectation)
      
2. [Comment copier correctement des objets en Python](#heading-comment-copier-correctement-des-objets-en-python)
  
3. [Plus sur la copie d'objets en Python](#heading-plus-sur-la-copie-dobjets-en-python)
  
4. [Résumé](#heading-resume)
  

## Qu'est-ce que le module `copy` ?

Le module `copy` est un module intégré en Python qui est principalement utilisé pour copier des objets en Python. Il vous permet d'apporter des modifications à un objet mutable et de l'enregistrer sous une copie différente en mémoire. En gros, il crée une copie de l'objet original et la stocke à un emplacement mémoire différent.

### Pourquoi ne pouvons-nous pas simplement utiliser l'opérateur d'affectation (`=`) pour copier des objets ?

Si nous utilisons l'opérateur d'affectation dans le but de copier des objets, il ne **copie** pas réellement l'objet – plutôt, il crée une liaison entre l'objet et l'identifiant. Cela signifie que si l'objet original pointe vers l'emplacement mémoire `x`, alors l'identifiant dans lequel nous avons tenté de copier l'objet en utilisant l'opérateur `=` pointera également vers le même emplacement mémoire, c'est-à-dire l'emplacement `x`.

Maintenant, cela peut créer des problèmes lors de la manipulation de divers aspects des données, car les modifications que nous apportons à l'objet se refléteront également dans sa liaison.

Avant de plonger dans le code, regardons d'abord la différence entre la copie et la référence :

* **Copie** : Créer une copie fait référence à la réplication de l'objet cible et à son stockage séparément dans la mémoire, en faisant un objet indépendant avec les mêmes données.
  
* **Référence** : Référencer un objet fait référence au fait de pointer vers la même adresse mémoire où l'objet cible est stocké. L'objet référencé est juste un autre nom (que nous appelons un « alias » en programmation) pour appeler l'objet original.
  

Comprenons cela avec un exemple :

```python
# création d'un objet dictionnaire.
d1 = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

# utilisation de l'opérateur d'affectation pour copier d1 dans d2.
d2=d1

# impression des deux dictionnaires.
print(f'd1 = {d1} \nd2 = {d2}')
```

**Sortie** :

> d1 = {'A': 1, 'B': 2, 'C': 3}
> 
> d2 = {'A': 1, 'B': 2, 'C': 3}

D'après l'exemple ci-dessus, il peut sembler que le dictionnaire a été copié dans la variable `d2` – mais en réalité, il pointe simplement vers l'objet stocké dans la variable `d1`. Dans ce cas, la variable `d2` est simplement un alias ou une référence au même objet `d1`. Nous pouvons le prouver comme suit :

```python
d1 = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

d2=d1

d1['D'] = 4 # ajouté une paire clé-valeur dans d1

print(f'd1 = {d1} \nd2 = {d2}')
```

Sortie :

> d1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
> 
> d2 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

Maintenant, dans le code ci-dessus, nous avons ajouté une paire clé-valeur dans le dictionnaire `d1` uniquement – mais le changement est également visible dans le dictionnaire `d2`. De cela, il est évident que les deux identifiants référençaient le même objet.

De cela, nous comprenons que l'opérateur d'affectation `=` peut être utilisé pour référencer les objets et nous ne pouvons pas l'utiliser pour copier les objets au vrai sens du terme.

## Comment copier correctement des objets en Python

Maintenant que vous comprenez la différence entre la copie et la référence, voyons comment vous pouvez réellement copier des objets en Python. Pour cela, nous utiliserons le module `copy` (mentionné précédemment).

Avant d'utiliser ce module, vous devez comprendre la différence entre une copie profonde et une copie superficielle.

* **Copie profonde** : Lors de la manipulation d'objets composés (également appelés objets conteneurs ou objets composites), la copie profonde signifie créer une copie des objets internes ainsi que de l'objet externe.
  
* **Copie superficielle** : Lors de la manipulation d'objets composés, la copie superficielle fait référence à la copie uniquement de l'objet externe et à la référence des objets internes.
  

**Note** : Les objets composés sont des objets qui contiennent d'autres objets à l'intérieur.

Comprenons mieux la différence entre les copies profondes et superficielles en les implémentant réellement dans un programme :

```python
import copy # importation du module copy

# création d'un objet composite
categories = {
    'Fruits' : ['Apple', 'Banana', 'Mango'],
    'Flowers' : ['Rose', 'Sunflower', 'Tulip'],
}

# copie de l'objet en utilisant la fonction copy() du module copy
categories_copy = copy.copy(categories)

print(f'Categories = {categories}\nCategories (Copied) = {categories_copy}')
```

**Sortie** :

> Categories = {'Fruits': \['Apple', 'Banana', 'Mango'\], 'Flowers': \['Rose', 'Sunflower', 'Tulip'\]}
> 
> Categories (Copied) = {'Fruits': \['Apple', 'Banana', 'Mango'\], 'Flowers': \['Rose', 'Sunflower', 'Tulip'\]}

Dans l'exemple ci-dessus, nous avons créé un objet composite appelé `categories` qui contient des listes comme objets internes. Ensuite, nous avons utilisé la fonction `copy()` du module `copy` pour copier superficiellement l'objet original. De plus, comme le module `copy` est intégré, il n'est pas nécessaire de l'installer manuellement ! Maintenant, les deux objets semblent similaires.

Ensuite, modifions l'objet original pour voir si l'objet est réellement copié ou s'il est simplement référencé :

```python
import copy

categories = {
    'Fruits' : ['Apple', 'Banana', 'Mango'],
    'Flowers' : ['Rose', 'Sunflower', 'Tulip'],
}

categories_copy = copy.copy(categories)

# ajouté une paire clé-valeur dans le dictionnaire original.
categories['Color'] = ['Red', 'Yellow', 'Blue']

print(f'Categories = {categories}\nCategories (Copied) = {categories_copy}')
```

**Sortie** :

> Categories = {'Fruits': \['Apple', 'Banana', 'Mango'\], 'Flowers': \['Rose', 'Sunflower', 'Tulip'\], 'Color': \['Red', 'Yellow', 'Blue'\]}
> 
> Categories (Copied) = {'Fruits': \['Apple', 'Banana', 'Mango'\], 'Flowers': \['Rose', 'Sunflower', 'Tulip'\]}

Ici, nous pouvons voir que même lorsque nous avons modifié le dictionnaire original, le dictionnaire copié (stocké dans la variable `categories_copy`) est resté le même. Cela signifie que nous avons réussi à copier le dictionnaire à un emplacement mémoire différent.

Mais nous avons copié superficiellement le dictionnaire. Nous savons que, pour un objet composite copié superficiellement, les objets internes pointent vers le même emplacement mémoire que celui de l'objet composite original. Vous pouvez voir cela dans l'exemple suivant :

```python
import copy

categories = {
    'Fruits' : ['Apple', 'Banana', 'Mango'],
    'Flowers' : ['Rose', 'Sunflower', 'Tulip'],
}

categories_copy = copy.copy(categories)

# vérification si l'objet interne liste 'Fruits' des deux dictionnaires pointe vers la même adresse mémoire.
print(f"""
Do 'categories' and 'categories_copy' inner object share same memory address? 
--> {id(categories_copy['Fruits']) == id(categories['Fruits'])}
""")

# vérification si les objets externes (dictionnaires) pointent vers la même adresse mémoire.
print(f"""
Do 'categories' and 'categories_copy' outer object share same memory address? 
--> {id(categories_copy) == id(categories)}
""")
```

**Sortie** :

> Do 'categories' and 'categories\_copy' inner object share same memory address?
> 
> \--&gt; True
> 
> Do 'categories' and 'categories\_copy' outer object share same memory address?
> 
> \--&gt; False

Dans le code ci-dessus, nous avons utilisé le même exemple que précédemment. Ensuite, nous avons utilisé la fonction intégrée `id()` pour extraire et comparer les adresses mémoire des deux dictionnaires.

Pour les objets internes, l'adresse mémoire est la même. Mais les objets externes sont situés à différents emplacements dans la mémoire. Ainsi, nous pouvons dire que lors de la copie superficielle des objets, les objets internes sont uniquement référencés, tandis que les objets externes sont copiés à une adresse mémoire séparée.

D'autre part, la fonction `deepcopy()` du module `copy` copie l'objet complètement (les objets internes et externes sont stockés à différents emplacements mémoire). Le code suivant montre comment nous pouvons copier profondément les objets dans notre code :

```python
import copy

categories = {
    'Fruits' : ['Apple', 'Banana', 'Mango'],
    'Flowers' : ['Rose', 'Sunflower', 'Tulip'],
}

# copie profonde du dictionnaire
categories_copy = copy.deepcopy(categories)

print(f"""
Do 'categories' and 'categories_copy' inner object share same memory address? 
--> {id(categories_copy['Fruits']) == id(categories['Fruits'])}
""")

print(f"""
Do 'categories' and 'categories_copy' outer object share same memory address? 
--> {id(categories_copy) == id(categories)}
""")
```

**Sortie** :

> Do 'categories' and 'categories\_copy' inner object share same memory address?
> 
> \--&gt; False
> 
> Do 'categories' and 'categories\_copy' outer object share same memory address?
> 
> \--&gt; False

Dans le code, nous avons copié profondément le dictionnaire en utilisant la fonction `deepcopy()`. Lorsque nous avons comparé les adresses mémoire des objets internes et externes stockés dans les deux identifiants, nous pouvons voir qu'ils sont stockés séparément dans la mémoire.

Ainsi, vous utiliserez une copie superficielle ou une copie profonde selon la situation.

Par exemple, si vous souhaitez simplement copier l'objet externe et garder l'objet imbriqué identique pour tous, vous devriez opter pour une copie superficielle. Si vous avez défini une classe pour créer des identifiants d'étudiants de la classe X, vous devrez peut-être garder `self.grade = X` pour tous les étudiants. Dans de tels cas, vous pouvez simplement référencer l'objet imbriqué.

De plus, pour les objets non imbriqués, la méthode de copie superficielle remplit le but, car il n'y a pas d'objets imbriqués et la copie superficielle copie complètement l'objet externe à un emplacement mémoire différent.

D'autre part, si vous souhaitez une copie complète et indépendante de l'objet, vous devriez copier profondément l'objet.

## Plus sur la copie d'objets en Python

Vous pouvez utiliser le module `copy` pour les objets immutables et mutables. Mais pour les objets immutables, vous pouvez également utiliser l'opérateur d'affectation `=` pour copier les objets.

Maintenant, comme je l'ai mentionné précédemment, dans ce cas également, l'objet est référencé lorsque vous utilisez l'opérateur `=`. Mais, lorsque vous mutez des objets immutables, les objets mutés sont stockés à un emplacement mémoire différent. Cela fait de l'alias de l'objet original un objet indépendant, pointant vers la même adresse mémoire qu'auparavant.

Comprenons cela avec un exemple :

```python
str1 = "String" # création d'un objet chaîne

str2 = str1 # utilisation de '=' pour référencer la chaîne stockée dans 'str1'

print(str2, str1, sep='\n') # impression des chaînes
```

**Sortie** :

> String
> 
> String

Ci-dessus, la variable `str2` référençait la chaîne stockée dans la variable `str1`. En gros, `str2` et `str1` pointent vers la même adresse mémoire et `str2` est simplement un alias de `str1`.

Mais si nous allons plus loin et modifions la chaîne dans `str1`, alors `str1` commence à pointer vers un nouvel emplacement mémoire (puisqu'une chaîne est immutable, si elle est modifiée, elle est stockée à un emplacement mémoire différent). Mais `str2` pointera toujours vers l'emplacement mémoire précédent, remplissant ainsi le but de copier les objets.

```python
str1 = "String"

str2 = str1

# impression des adresses mémoire des deux variables avant la mutation.
print(f"""
Memory address of str1: {id(str1)}
Memory address of str2: {id(str2)}
""")

str1+='***' # concaténation de la chaîne '***' avec str1.

print(str2, str1, sep='\n')

# impression des adresses mémoire des deux variables après la mutation.
print(f"""
Memory address of str1: {id(str1)}
Memory address of str2: {id(str2)}
""")
```

**Sortie** :

> Memory address of str1: 2652367074480
> 
> Memory address of str2: 2652367074480
> 
> String
> 
> String\*\*\*
> 
> Memory address of str1: 2652367370736
> 
> Memory address of str2: 2652367074480

**Note** : Les adresses mémoire peuvent varier sur votre appareil par rapport à celles affichées ci-dessus.

Maintenant, dans l'exemple ci-dessus, nous avons d'abord créé un objet chaîne et l'avons référencé dans une autre variable, puis nous avons imprimé les adresses mémoire des deux variables. Ensuite, nous avons modifié la chaîne originale, et à nouveau, nous avons imprimé les adresses mémoire des deux variables.

Dans la sortie, nous pouvons voir que les adresses mémoire des deux variables avant la mutation étaient les mêmes. Vous pouvez donc voir que les deux variables pointaient vers le même emplacement mémoire. Mais après la mutation, la variable `str1` a commencé à pointer vers un emplacement mémoire différent, faisant ainsi de l'alias `str2` un objet indépendant, qui pointe toujours vers l'emplacement mémoire précédent.

En résumé, vous pouvez utiliser l'opérateur `=` pour stocker une copie de l'objet original si vous prévoyez de le modifier davantage dans le programme.

## Résumé

Dans ce tutoriel, vous avez appris à copier des objets en Python. Plus précisément, nous avons parlé de :

* Comment l'opérateur d'affectation `=` est utilisé pour la référence et non pour la copie.
  
* Le module intégré `copy`, qui fournit des fonctions qui nous permettent de copier superficiellement et profondément les objets dans notre programme.
  
* Le concept de copie superficielle et de copie profonde, qui sont essentiels lors de la copie d'objets composés.
  
* Comment une copie superficielle copie l'objet externe et référence les objets internes.
  
* Comment une copie profonde copie à la fois l'objet externe et les objets internes.
  
* Comment pour les objets immutables, l'opérateur d'affectation fonctionne bien pour copier les objets la plupart du temps.
  

Merci d'avoir lu !