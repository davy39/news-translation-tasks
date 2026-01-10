---
title: Boucle For en Python – Exemple et Tutoriel
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-07-27T22:36:10.000Z'
originalURL: https://freecodecamp.org/news/python-for-loop-example-and-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/kevin-canlas-cFFEeHNZEqw-unsplash.jpg
tags:
- name: Python
  slug: python
seo_title: Boucle For en Python – Exemple et Tutoriel
seo_desc: "Loops let you control the logic and flow structures of your programs. \n\
  Specifically, a for loop lets you execute a block of similar code operations, over\
  \ and over again, until a condition is met.\nYou repeat certain code instructions\
  \ for a set of valu..."
---

Les boucles vous permettent de contrôler la logique et les structures de flux de vos programmes. 

Plus précisément, une boucle `for` vous permet d'exécuter un bloc d'opérations de code similaires, encore et encore, jusqu'à ce qu'une condition soit remplie.

Vous répétez certaines instructions de code pour un ensemble de valeurs que vous déterminez, et vous effectuez des actions sur chaque valeur pour un nombre prédéterminé de fois.

## Qu'est-ce qu'une boucle for en Python ?
 
Une boucle `for` peut itérer sur chaque élément d'une liste ou parcourir chaque caractère d'une chaîne et ne s'arrêtera pas tant qu'elle n'aura pas parcouru chaque caractère.

Écrire des boucles `for` aide à réduire la répétitivité dans votre code, en suivant le principe DRY (Don't Repeat Yourself). Vous n'écrivez pas le même bloc de code plus d'une fois.

Dans cet article, nous allons découvrir les bases des boucles `for` dans le langage de programmation Python en utilisant différents exemples. Mais d'abord, apprenons quelques bases des boucles `for`.

## Comment fonctionne une boucle for dans d'autres langages de programmation ?

La boucle dans la plupart des langages de programmation modernes comme JavaScript, Java ou C ressemble à quelque chose comme l'exemple ci-dessous. 

Boucles en JavaScript :

```JavaScript
for (let i = 0; i < 10; i++) {
  console.log('Compter les nombres');
  // imprime "Compter les nombres" 10 fois
  // valeurs de i de 0 à 9 
  }
```

La boucle for suit généralement trois choses :

1. L'instruction d'expression d'initialisation qui est exécutée une fois, `let i = 0;`
2. La condition qui doit être remplie, `i < 10;`. Cette condition est évaluée comme `true` ou `false`. Si elle est `false`, la boucle est terminée.
3. Si la condition est `true`, le corps de la boucle sera exécuté et l'expression initialisée prendra une certaine action. Dans ce cas, elle sera incrémentée de 1 (`i++`), jusqu'à ce que la condition soit remplie. 


## Syntaxe de la boucle for en Python

La boucle for en Python semble assez différente par rapport à d'autres langages de programmation.

Python se targue de sa lisibilité, donc sa boucle `for` est plus propre, plus simple et plus compacte.

La structure de base est la suivante :

```
pour élément dans séquence :
    exécuter expression
```

où : 

- `for` commence une boucle `for`.
- `item` est un élément individuel lors de chaque itération. Il est donné un nom de variable arbitraire temporaire.
- `in` sépare chaque élément des autres.
- `sequence` est ce que nous voulons itérer.
- un deux-points `:` donne l'instruction d'exécuter le corps de code qui suit.
- Une nouvelle ligne.
- Un niveau d'indentation. 4 espaces avant d'écrire le corps de la boucle, sinon nous obtenons une `IndentationError`.
- Le corps avec les actions à prendre et à répéter (par exemple, imprimer quelque chose sur la console). Il va où se trouve la ligne `execute experssion`.

### Comment fonctionne la boucle for en Python

Supposons que nous avons une séquence, une liste d'éléments stockés que nous voulons parcourir – dans ce cas, une liste de courses :

```Python
courses = ["bananas","beurre","fromage","dentifrice"]
```


Le mot-clé `in` vérifie si un élément est inclus dans une séquence. Lorsqu'il est combiné avec le mot-clé `for`, il indique l'itération sur chaque élément de la séquence. 

Il fait quelque chose avec chaque élément de la liste. Dans ce cas, il imprime séparément chaque élément individuel sur la console jusqu'à ce que chaque élément ait été itéré.

```Python
for course in courses:
    # pour chaque itération, imprime la valeur de course
    print(course)
```

`course` est un nom de variable temporaire pour désigner chaque élément de la liste.

C'est une `variable d'itérateur`, qui à chaque itération successive, sa valeur est définie à chaque valeur que la liste inclut. Essentiellement, c'est une variable temporaire avec une valeur temporaire.

Nous pourrions la nommer comme nous le souhaitons, comme `c` ou `item`. Mais le nom doit être unique et ne doit pas être le même que toute autre variable dans notre programme.

Lors de la première exécution, le premier élément – `bananas` – est stocké dans la variable `item`.

Ensuite, l'expression `print(course)`, qui est essentiellement `print("bananas")`, est exécutée. 

Lors de la deuxième exécution, l'élément `butter` est stocké dans la variable `item` et comme ci-dessus, il est imprimé sur la console. 

Ce processus continue jusqu'à ce que tous les éléments aient été itérés.

Voici le résultat de ce code :

```
bananas
butter
cheese
toothpaste
```


### Comment utiliser une boucle for pour une plage de nombres

Nous pouvons utiliser la fonction `range()` avec une plage donnée pour spécifier combien de fois de suite nous voulons que la boucle `for` itère. Cela simplifie la boucle `for`.

La fonction `range()` crée une séquence d'entiers en fonction des arguments que nous lui donnons.

Comment cela fonctionne-t-il ?

Regardez l'exemple ci-dessous :

```python
for i in range(5):
    print(i)
```

Le résultat est :

```
0
1
2
3
4
```

Elle crée une liste de nombres entre 0 et 4. 

Par défaut, lorsque nous donnons à `range()` un argument, la plage commence à compter à partir de `0`. 

Remarquez que `5` n'est pas imprimé sur la console.

Dans `range(5)`, nous spécifions que `5` est le nombre le plus élevé que nous voulons, mais *non inclusif*. Il ne l'inclut pas, c'est juste le point d'arrêt. Il définit le nombre de fois où nous voulons que notre boucle s'exécute. Nous voyons qu'elle s'exécute 5 fois et crée une sorte de liste de 5 éléments : `0,1,2,3,4`.

Si vous voulez voir ce que `range()` produit à des fins de débogage, vous pouvez le passer à la fonction `list()`.

Ouvrez l'interpréteur Python interactif dans votre console, généralement avec la commande `python3`, et tapez :

```python
show_numbers = list(range(5))

print(show_numbers)
```

Et si nous voulons que notre plage commence à 1 et que 5 soit également imprimé sur la console ? Nous donnons plutôt à `range()` deux arguments différents cette fois :

```python
for i in range(1,6):
    print(i)
```

Résultat :

```
1
2
3
4
5
```

Le premier argument (`start`) qui, comme nous l'avons vu précédemment, est facultatif, est l'endroit où la séquence doit commencer (dans ce cas, c'est 1). Cet argument est *inclusif* et le nombre est inclus. 
 
Le deuxième argument (`stop`) qui est requis, est l'endroit où la séquence doit se terminer et est *non inclusif*, comme mentionné précédemment. Dans ce cas, c'est 6.
 
Enfin, vous pouvez passer un troisième paramètre facultatif : `step`.
 
Cela contrôle l'*incrément* entre les deux valeurs de la plage. La valeur par défaut de `step` est 1.
 
Supposons que nous voulions sauter tous les deux nombres et obtenir les nombres impairs d'une séquence. Nous pourrions faire :
 
 ```python
 for i in range(1,10,2):
     print(i)
```

Résultat :

```
1
3
5
7
9
```

`1` est l'endroit où nous commençons, `10` est 1 de plus que ce que nous voulons (qui est 9), et `2` est la quantité que nous voulons sauter entre les nombres (dans ce cas, nous sautons tous les deux nombres).
 
 
### Comment utiliser enumerate() en Python

Jusqu'à présent, nous n'avons pas utilisé d'index lors de l'itération. Parfois, nous devons accéder à l'index de l'élément que nous parcourons et l'afficher.

Nous pouvons parcourir les éléments avec l'index en utilisant `enumerate()`.

Notre exemple précédent :

```Python
courses = ["bananas","butter","cheese","toothpaste"]

for course in courses:
    print(course)
```

Peut maintenant être écrit comme ceci :

```Python
courses = ["bananas","butter","cheese","toothpaste"]

for index, course in enumerate(courses):
    print(index,course)   
```


Résultat :
```
0 bananas
1 butter
2 cheese
3 toothpaste
```

Ou pour une sortie un peu plus complexe :

```Python
courses = ["bananas","butter","cheese","toothpaste"]
for index, course in enumerate(courses):
    print(f"Course : {course} est à l'index : {index}.") 
```

Résultat :

```
Course : bananas est à l'index : 0.
Course : butter est à l'index : 1.
Course : cheese est à l'index : 2.
Course : toothpaste est à l'index : 3
```


- Au lieu d'écrire une seule variable `course` comme avant, nous en écrivons maintenant deux : `index,course`. À chaque itération, `index` contient l'index de la valeur et `course` la valeur de `courses`.
- `index` est l'index de la valeur en cours d'itération.
- Les index en Python commencent à compter à `0`.
- `course` est la valeur de l'élément à l'itération actuelle.
- La ligne `enumerate(courses)` nous permet de parcourir la séquence et de garder une trace de l'index de la valeur et de la valeur elle-même.  
  
  
## Conclusion

J'espère que vous avez apprécié cette introduction de base à la boucle `for` en Python.

Nous avons passé en revue la syntaxe de base qui constitue une boucle `for` et son fonctionnement.

Nous avons ensuite brièvement expliqué ce que font les deux méthodes intégrées de Python, `range()` et `enumerate()`, dans les boucles `for`.

Merci d'avoir lu et bon codage !