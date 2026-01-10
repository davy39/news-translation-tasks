---
title: Guide des dictionnaires Python – Comment itérer, copier et fusionner des dictionnaires
  en Python 3.9
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-26T21:36:29.000Z'
originalURL: https://freecodecamp.org/news/python-dictionary-guide
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/thumb.png
tags:
- name: Data Science
  slug: data-science
- name: dictionary
  slug: dictionary
- name: Python
  slug: python
seo_title: Guide des dictionnaires Python – Comment itérer, copier et fusionner des
  dictionnaires en Python 3.9
seo_desc: "By Florian Dedov\nPython is a popular language for data science. And working\
  \ with collections is one of the most fundamental skills you need to have. \nCollections\
  \ are data structures that contain multiple elements of various different data types.\
  \ \nTod..."
---

Par Florian Dedov

Python est un langage populaire pour la science des données. Et travailler avec des collections est l'une des compétences les plus fondamentales que vous devez avoir. 

Les collections sont des structures de données qui contiennent plusieurs éléments de différents types de données. 

Aujourd'hui, nous allons examiner en détail les dictionnaires, qui sont un type spécial de collection en Python. Nous couvrirons leur fonctionnalité de base, leur fonctionnement interne et également certaines fonctionnalités de pointe de la dernière version de Python.

À la fin de ce tutoriel, vous saurez

<ul>
    <li>Ce que sont les dictionnaires</li>
    <li>Comment travailler avec les dictionnaires</li>
    <li>Comment itérer sur les dictionnaires</li>
    <li>Comment copier les dictionnaires</li>
    <li>Comment fusionner les dictionnaires en Python 3.9</li>
</ul>

## Qu'est-ce que les dictionnaires en Python ?

Avant d'apprendre quelque chose en profondeur, il est toujours bon de commencer par une définition simple et basique. 

Comme je l'ai déjà dit, les dictionnaires sont un type de collection en Python. Cependant, contrairement aux listes, aux tuples et aux ensembles, vous ne stockez pas des valeurs individuelles mais des paires clé-valeur. Cela signifie qu'au lieu de faire référence à vos valeurs par un index, vous utilisez une clé, qui est un identifiant unique.

```python
l1 = [10, "Hello", True, 20.23] # Liste
t1 = (10, "Hello", True, 20.23) # Tuple
s1 = {10, "Hello", True, 20.23} # Ensemble

d1 = {'number': 10,
      'greeting': "Hello",
      'boolean': True,
      'float': 20.23} # Dictionnaire

```

Dans l'exemple ci-dessus, vous pouvez voir la différence. Les paires clé-valeur individuelles sont séparées par des virgules. Chaque paire commence par une clé unique suivie d'un deux-points et de la valeur respective. Remarquez que la valeur n'a pas besoin d'être unique, puisque nous ne l'utilisons pas pour accéder ou identifier quoi que ce soit. 

Gardez également à l'esprit que nous pouvons utiliser n'importe quel type de données pour les clés et les valeurs que nous voulons. Ici, nous utilisons uniquement des chaînes de caractères pour les identifiants, mais nous pouvons également utiliser des entiers, des flottants, des collections ou même des booléens. 

Cependant, vous devriez toujours vous demander si cela est raisonnable. La plupart du temps, une chaîne de caractères sera le meilleur choix.

## Comment travailler avec les dictionnaires en Python

D'accord, maintenant que nous savons ce que sont les dictionnaires, voyons comment travailler avec eux. 

Tout d'abord, nous allons passer en revue les opérations de base comme l'accès, l'ajout et la suppression de valeurs. Après cela, nous examinerons des sujets plus avancés et plus intéressants.

Vous pouvez accéder aux éléments d'un dictionnaire en Python de la même manière que vous accédez aux éléments de toute autre collection. La seule différence est que vous passez une clé plutôt qu'un index. Cela s'applique également à la modification et même à l'ajout de valeurs.

```python
person = {'name': "Mike", 'age': 25, 'weight': 80.5}

print(person['name'])
person['name'] = "Bob" # Modification de la valeur existante
print(person['name'])

person['gender'] = 'm' # Création d'une nouvelle paire clé-valeur
print(person['gender'])

```

Comme vous pouvez le voir ici, vous passez simplement une clé pour accéder à la valeur à laquelle elle fait référence. D'abord, vous imprimez le nom, puis vous le modifiez. Ensuite, vous l'imprimez à nouveau pour vous assurer que les modifications ont été effectuées. 

Remarquez que cela fonctionne non seulement pour les paires existantes, mais aussi pour les nouvelles. Pour créer une nouvelle paire clé-valeur, il suffit de faire référence à une clé qui n'existe pas encore et de lui attribuer une valeur. La paire est alors ajoutée automatiquement au dictionnaire.

La suppression de valeurs d'un dictionnaire fonctionne différemment. Ici, vous pouvez soit utiliser le mot-clé **del**, soit la méthode **pop()**. 

La principale différence entre ces deux approches est que **del** supprime uniquement la paire clé-valeur, tandis que **pop()** retourne également la valeur supprimée par la suite. Selon votre cas d'utilisation, vous devrez décider quelle méthode convient le mieux à votre tâche.

## Comment itérer sur les dictionnaires en Python

Puisque les dictionnaires sont des collections, vous pouvez également itérer sur eux. Mais ce n'est pas aussi simple et direct que cela l'est avec les autres types de collections. 

Cela est dû au fait que vous ne traitez pas avec des valeurs individuelles mais avec des paires. Lorsque vous itérez sur un dictionnaire en utilisant une boucle for, vous itérez en fait uniquement sur les clés.

```python
names_ages = {'Bob': 50,
              'Anna': 28,
              'Max': 30,
              'John': 76}

for element in names_ages:
    print(element)
    
# Sortie : Bob  Anna  Max  John

```

Par conséquent, si vous souhaitez itérer sur les valeurs ou même sur les paires complètes, vous devez utiliser des méthodes supplémentaires. 

Pour accéder aux valeurs, vous devez simplement appeler la méthode **values()**. Elle retourne un itérateur pour toutes les valeurs du dictionnaire. 

Pour accéder aux paires complètes, vous pouvez appeler la méthode **items()**. Ici, vous itérez sur une liste de tuples, où chaque tuple représente une paire clé-valeur. 

Bien sûr, il y a aussi la méthode **keys()**, au cas où vous souhaitez travailler avec les clés du dictionnaire en dehors d'une boucle for.

```python
print(list(names_ages.keys()))
print(list(names_ages.values()))
print(list(names_ages.items()))

# Sortie
# > ['Bob', 'Anna', 'Max', 'John']
# > [50, 28, 30, 76]
# > [('Bob', 50), ('Anna', 28), ('Max', 30), ('John', 76)]

```

Une chose importante à garder à l'esprit ici est que ces méthodes ne retournent pas de listes réelles. Elles retournent des objets que vous pouvez utiliser pour itérer sur les clés et les valeurs. Mais vous pouvez facilement convertir ces objets en listes en utilisant la fonction **list()**.

## Comment copier les dictionnaires en Python

Maintenant, nous abordons des sujets plus avancés. 

Vous ne croiriez pas combien de fois des programmeurs nouveaux et inexpérimentés rencontrent des problèmes parce qu'ils copient des collections de la mauvaise manière. Ils dépannent leurs projets pendant des heures et sont incapables de trouver le problème. 

Alors, faites attention ici si vous ne voulez pas vivre cette frustration vous-même. 

Avant de parler de la copie des collections et des dictionnaires, voyons comment vous copieriez généralement des types de données primitifs comme les entiers.

```python
i1 = 20
i2 = i1

i2 += 10
print(i1, i2)

# Sortie : 20  30

```

Lorsque vous voulez créer une nouvelle variable et copier la valeur d'un autre entier, vous assigner directement la variable. Ensuite, vous pouvez changer la valeur du deuxième entier et travailler avec, sans changer quoi que ce soit au premier. 

Cela fonctionne également pour les booléens, les flottants, les chaînes de caractères, etc. Cependant, voyons ce qui se passe lorsque nous faisons cela avec un dictionnaire.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = d1
d2['c'] = 50

print(d1)
print(d2)

# Sortie
# {'a': 10, 'b': 20, 'c': 50}
# {'a': 10, 'b': 20, 'c': 50}

```

Que s'est-il passé ici ? N'avons-nous pas fait la même chose qu'avant ? Pourquoi le premier dictionnaire change-t-il lorsque nous modifions le deuxième ? N'est-ce pas juste une copie ? 

La réponse est clairement non. Lorsque vous assigner un dictionnaire à une nouvelle variable, vous passez en fait une référence. 

La deuxième variable n'est pas en fait un dictionnaire mais juste une autre variable pointant vers le même dictionnaire que la première. Par conséquent, peu importe sur quelle variable vous appliquez des changements, puisque ils sont tous effectués sur le dictionnaire auquel ils font tous les deux référence.

Si vous voulez créer une copie superficielle d'un dictionnaire en Python, vous devez soit utiliser la fonction **dict()**, soit appeler la méthode **copy()** du dictionnaire. En faisant cela, vous créez un nouveau dictionnaire qui a les mêmes éléments que l'original.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = dict(d1)
d3 = d1.copy()

d2['b'] = 50
d3['a'] = -90
print(d1) # inchangé

```

Remarquez cependant que les objets à l'intérieur de la copie sont toujours les mêmes objets que dans le premier dictionnaire. Par conséquent, s'ils sont des objets ou des collections plus complexes, vous vous retrouverez avec un nouveau dictionnaire séparé (mais les objets à l'intérieur feront référence aux mêmes objets que ceux du premier dictionnaire). 

Pour changer cela, vous devriez faire une copie profonde, mais cela n'est pas dans le cadre de cet article.

## Comment fusionner les dictionnaires en Python

Dernier point mais non des moindres, parlons des fonctionnalités de pointe des dictionnaires de Python 3.9. Ces fonctionnalités sont axées sur la fusion des dictionnaires. 

Jusqu'à récemment, les programmeurs devaient soit utiliser la méthode **update()**, soit utiliser les opérateurs de déballage.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}
d1.update(d2)
print(d1)

d1 = {'a': 10, 'b': 20, 'c': 30}
d3 = {**d1, **d2}
print(d3)

```

La principale différence entre ces deux approches est que la méthode **update()** ajoute les valeurs d'un dictionnaire à un autre et applique les changements directement. Le dictionnaire résultant n'est pas retourné mais est en fait enregistré dans le premier objet. 

Lorsque vous utilisez les opérateurs de déballage, en revanche, vous créez un nouveau dictionnaire et placez les paires clé-valeur des deux dictionnaires en les déballant.

Maintenant, vous pouvez vous demander ce qui se passe lorsque vous fusionnez deux dictionnaires qui ont la même clé à l'intérieur. 

Vous pouvez penser à cela comme suit : Le premier dictionnaire crée la paire clé-valeur et le second la remplace. Donc, si vous appelez la méthode de mise à jour sur la première collection et passez la deuxième collection comme argument, la paire clé-valeur du deuxième dictionnaire se retrouvera dans le résultat. 

Il en va de même pour le déballage. Le dictionnaire que vous passez en dernier remplace les précédents.

Donc, c'est l'ancienne façon de faire les choses. Dans Python 3.9, cependant, les opérateurs de fusion et de mise à jour ont été introduits. Ils rendent la jonction des dictionnaires plus simple.

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'c': 40, 'd': 60, 'e': 20}

d3 = d1 | d2  # Fusion
d1 |= d2      # Mise à jour

```

Comme vous pouvez le voir, l'opérateur de fusion est le même que celui utilisé pour l'opération OR bit à bit. L'ordre des dictionnaires est important si vous avez des clés identiques dans les deux dictionnaires. La collection de droite remplace la collection de gauche. 

Si vous voulez mettre à jour le premier dictionnaire au lieu de retourner un nouveau, combinez simplement l'opérateur de fusion avec l'opérateur d'assignation de base. Cette façon de fusionner les dictionnaires est la méthode recommandée depuis Python 3.9.

Si vous êtes plus un apprenant visuel ou auditif, vous pouvez regarder mon tutoriel vidéo sur la fusion des dictionnaires ci-dessous.

%[https://www.youtube.com/watch?v=RWqPfsFK1eo]

## Conclusion

D'accord, vous devriez maintenant être très à l'aise lorsque vous travaillez avec des dictionnaires. Vous savez non seulement ce qu'ils sont et comment les utiliser, mais vous comprenez également comment ils fonctionnent à un niveau plus profond. 

Lorsque vous travaillez sur un projet, vous saurez comment copier les dictionnaires de la bonne manière. Nous avons même couvert l'une des fonctionnalités de pointe de la dernière version de Python. 

Assurez-vous de passer en revue les extraits de code une fois de plus et de comprendre comment et pourquoi ils fonctionnent. Cela fera de vous un bien meilleur programmeur Python.

Si vous êtes intéressé par plus de contenu comme celui-ci, vous pouvez consulter ma chaîne YouTube [NeuralNine](https://www.youtube.com/c/NeuralNine/) ou mon site web [neuralnine.com](https://www.neuralnine.com/). 

Pour les passionnés de Python, j'ai une série spéciale de livres sur Python qui vous enseigne le langage à partir de zéro et aborde également des sujets plus avancés comme l'apprentissage automatique et la vision par ordinateur. Vous pouvez la trouver [ici](https://www.neuralnine.com/books).

J'espère que vous avez apprécié cet article et je vous souhaite une excellente journée ! :)