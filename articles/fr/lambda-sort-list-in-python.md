---
title: Lambda Sorted en Python – Comment trier une liste avec une fonction Lambda
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2023-03-16T19:37:09.000Z'
originalURL: https://freecodecamp.org/news/lambda-sort-list-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/lambdaSort.png
tags:
- name: lambda
  slug: lambda
- name: Python
  slug: python
seo_title: Lambda Sorted en Python – Comment trier une liste avec une fonction Lambda
seo_desc: "The sort() method and the sorted() function let you sort iterable data\
  \ like lists and tuples in ascending or descending order. \nThey take parameters\
  \ with which you can modify how they perform the sorting. And one of those parameters\
  \ could be a functi..."
---

La méthode `sort()` et la fonction `sorted()` vous permettent de trier des données itérables comme les listes et les tuples par ordre croissant ou décroissant. 

Elles prennent des paramètres avec lesquels vous pouvez modifier la façon dont elles effectuent le tri. Et l'un de ces paramètres peut être une fonction ou même une fonction lambda.

Dans cet article, vous apprendrez comment trier une liste avec la fonction lambda.


## Ce que nous allons aborder
- [Comment trier une liste en Python](#heading-comment-trier-une-liste-en-python)
- [Qu'est-ce qu'une fonction Lambda ?](#heading-quest-ce-quune-fonction-lambda)
- [Comment trier une liste avec la fonction Lambda](#heading-comment-trier-une-liste-avec-la-fonction-lambda)
  - [Comment trier avec la méthode `sort()` et une Lambda](#heading-comment-trier-avec-la-methode-sort-et-une-lambda)
  - [Comment trier avec la fonction `sorted()` et une Lambda](#heading-comment-trier-avec-la-fonction-sorted-et-une-lambda)
- [Conclusion](#heading-conclusion)


## Comment trier une liste en Python
Vous pouvez trier une liste avec la méthode `sort()` et la fonction `sorted()`. 

La méthode `sort()` prend deux paramètres : `key` (clé) et `reverse` (inverse). Vous pouvez utiliser une fonction comme clé, mais le paramètre `reverse` ne peut prendre qu'un booléen. 

Si vous spécifiez la valeur du paramètre `reverse` comme `True`, la méthode `sort()` effectuera le tri par ordre décroissant. Et si vous spécifiez `False` comme valeur de `reverse`, le tri se fera par ordre croissant. Vous n'avez même pas besoin de spécifier `False` comme valeur car c'est le réglage par défaut.

Mais ces deux paramètres sont facultatifs, donc la méthode fonctionne toujours très bien sans eux :

```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Noms originaux :", name_list) # Noms originaux : ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


name_list.sort()
print("Noms triés :", name_list) # Noms triés : ['Ben Benson', 'John Ann', 'Luigi Austin', 'Zen Jack']


num_list = [34, 11, 35, 89, 37]
print("Nombres originaux :", num_list) # Nombres originaux : [34, 11, 35, 89, 37]


num_list.sort()
print("Nombres triés :", num_list) # Nombres triés : [11, 34, 35, 37, 89]
```

D'autre part, la fonction `sorted()` fonctionne également comme `sort()`. Elle prend aussi les paramètres facultatifs `key` et `reverse`, mais elle nécessite un paramètre obligatoire qui est l'itérable que vous souhaitez trier – ce qui la rend idéale pour trier d'autres itérables en dehors des listes.

Voici comment fonctionne la fonction `sorted()` :
```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Noms originaux :", name_list) # Noms originaux : ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


sorted(name_list)
print("Noms triés :", name_list) # Noms triés : ['Ben Benson', 'John Ann', 'Luigi Austin', 'Zen Jack']


num_list = [34, 11, 35, 89, 37]
print("Nombres originaux :", num_list) # Nombres originaux : [34, 11, 35, 89, 37]


sorted(num_list)
print("Nombres triés :", num_list) # Nombres triés : [11, 34, 35, 37, 89]
```

Comme je l'ai souligné précédemment, vous pouvez également trier d'autres itérables avec la fonction `sorted()`. Voici comment j'ai trié un tuple avec la fonction `sorted()` :
```py
name_tuple = ('Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann')
print("Tuple original :", name_tuple) # Tuple original : ('Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann')


sorted(name_tuple)
print("Tuple trié :", name_tuple) # Tuple trié : ('Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann')
```

Rappelez-vous que j'ai également indiqué que vous pouvez passer une fonction comme valeur pour le paramètre `key` de la méthode `sort()` et de la fonction `sorted()`. Cette fonction peut vous aider à être plus précis sur la manière dont vous souhaitez trier la liste ou le tuple itérable.

Par exemple, la fonction `sorted()` et la méthode `sort()` ne trieraient que par la première partie de la chaîne de caractères ou du nombre. Mais vous pouvez également trier par la deuxième partie en passant une fonction comme paramètre `key`. C'est avec cette fonction que vous déciderez comment vous voulez trier la liste ou d'autres itérables.

Une fonction lambda serait idéale pour faire cela car elle ne prend qu'une seule expression. Mais avant de plonger dans le tri avec une fonction lambda, laissez-moi vous rappeler ce qu'est une fonction lambda.


## Qu'est-ce qu'une fonction Lambda ?
Une fonction lambda est une fonction anonyme – une fonction que vous n'écrivez pas avec le mot-clé `def`. Une fonction lambda peut prendre plusieurs arguments, mais elle ne peut avoir qu'une seule expression.

Puisque vous ne définissez pas une fonction lambda avec le mot-clé `def`, comment l'appelez-vous ? Vous pouvez assigner une fonction lambda à une variable, puis l'appeler par le nom de cette variable.

Dans l'exemple ci-dessous, la fonction lambda `addNums` a 3 arguments et les additionne :

```py
addNums = lambda a, b, c : a + b + c


res = addNums(4, 12, 4)
print(res) # 20
``` 


## Comment trier une liste avec la fonction Lambda
Vous pouvez effectuer un « lambda tri » sur une liste avec la méthode `sort()` et la fonction `sorted()`. Regardons d'abord comment trier avec la méthode `sort()`.


### Comment trier avec la méthode `sort()` et une Lambda
Prenons les noms que nous avons triés auparavant et trions-les par le deuxième nom (le nom de famille). Cette fonction lambda serait idéale pour trier par le deuxième nom :

```py
lambda name: name.split()[1]
```
La fonction lambda divise un nom et prend la deuxième partie du nom – le deuxième nom. La première partie est le prénom et ce serait `[0]`.

Vous pouvez passer cette fonction lambda comme paramètre `key` – triant ainsi les noms par les seconds noms :
```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Liste originale", name_list) # Liste originale ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


name_list.sort(key=lambda name: name.split()[1])
print("Liste de noms triée", name_list) # Liste de noms triée ['John Ann', 'Luigi Austin', 'Ben Benson', 'Zen Jack']
```

Vous pouvez voir que les noms ont été triés par ordre alphabétique des seconds noms. `John Ann` est arrivé en premier, et `Zen Jack` en dernier. Ann commence par A et Jack commence par J.

Si vous le souhaitez, vous pouvez même passer une fonction directement. Ce que vous devez faire, c'est ne pas appeler la fonction. Vous devez la passer en tant qu'objet.
```py
name_list = ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']
print("Liste originale", name_list) # Liste originale ['Zen Jack', 'Luigi Austin', 'Ben Benson', 'John Ann']


def sort_by_second_name(name):
    return name.split()[1]


name_list.sort(key=sort_by_second_name)
print("Liste de noms triée", name_list) # Liste de noms triée ['John Ann', 'Luigi Austin', 'Ben Benson', 'Zen Jack']
```

Maintenant, trions les nombres en fonction de leur dernier chiffre. Au cas où vous ne le sauriez pas, si vous utilisez l'opérateur modulo (`%`) sur deux nombres, il divise les deux nombres et renvoie le reste :

```py
print(4 % 2) # renvoie 0
print(44 % 11) # renvoie 0
print(104 % 60) # renvoie 44
print(21 % 2) # renvoie 1
```

Mais si vous faites un modulo d'un nombre à plusieurs chiffres par 10, cela renvoie le dernier chiffre du nombre :
```py
print (44 % 10) # renvoie 4
print (402 % 10) # renvoie 2
print (152 % 10) # renvoie 2
print (1596 % 10) # renvoie 6
```

C'est ainsi que vous pouvez obtenir le dernier chiffre et trier les nombres en fonction de celui-ci.

Voici comment j'ai trié les nombres des exemples précédents avec une fonction lambda :
```py
num_list = [22, 34, 11, 35, 89, 37, 93, 56, 108]
print('Nombre original :', num_list) # Nombre original : [22, 34, 11, 35, 89, 37, 93, 56, 108]


num_list.sort(key=lambda num: num % 10)
print('Nombre trié par lambda :', num_list) # Nombre trié par lambda : [11, 22, 93, 34, 35, 56, 37, 108, 89]
```

Comme vous pouvez le voir, cette fonction lambda, `lambda num: num % 10`, est responsable du tri des nombres en fonction de chacun des seconds chiffres. J'ai passé le nombre à la fonction lambda et j'ai obtenu le dernier chiffre avec `% 10`. Cette fonction lambda parcourt chacun des nombres et récupère leur dernier chiffre.

Si vous le souhaitez, vous pouvez même passer une fonction directement comme clé :
```py
num_list = [22, 34, 11, 35, 89, 37, 93, 56, 108]
print('Nombre original :', num_list) # Nombre original : [22, 34, 11, 35, 89, 37, 93, 56, 108]


def sort_by_second_num(num):
    return num % 10


num_list.sort(key=sort_by_second_num)
print('Nombre trié par lambda :', num_list) # Nombre trié par lambda : [11, 22, 93, 34, 35, 56, 37, 108, 89]
```


### Comment trier avec la fonction `sorted()` et une Lambda
Dans cet exemple, nous allons trier une liste de tuples en utilisant les numéros de maillot de certains footballeurs.

La seule différence entre la méthode `sort()` et la fonction `sorted()` est que `sorted()` prend un itérable obligatoire et `sort()` non.

Ainsi, pour effectuer un tri lambda avec la fonction `sorted()`, tout ce que vous avez à faire est de passer la liste comme itérable et votre fonction lambda comme clé :

```py
 footballers_and_nums = [("Fabregas", 4),("Beckham" ,10),("Yak", 9), ("Lampard", 8), ("Ronaldo", 7), ("Terry", 26), ("Van der Saar", 1), ("Yobo", 2)]


sorted_footballers_and_nums = sorted(footballers_and_nums, key=lambda index : index[1])


print("Footballeurs et numéros de maillot originaux", footballers_and_nums) # Footballeurs et numéros de maillot originaux [('Fabregas', 4), ('Beckham', 10), ('Yak', 9), ('Lampard', 8), ('Ronaldo', 7), ('Terry', 26), ('Van der Saar', 1), ('Yobo', 2)]


print("Footballeurs triés par numéros de maillot :", sorted_footballers_and_nums) # Footballeurs triés par numéros de maillot : [('Van der Saar', 1), ('Yobo', 2), ('Fabregas', 4), ('Ronaldo', 7), ('Lampard', 8), ('Yak', 9), ('Beckham', 10), ('Terry', 26)]
```

La fonction lambda qui a effectué le tri est celle-ci : `lambda index : index[1]`. La lambda a parcouru tous les tuples de la liste, a pris le deuxième index (`[1]`), et les a utilisés pour effectuer le tri.


## Conclusion
Cet article vous a montré comment trier une liste avec la méthode `sort()` et la fonction `sorted()` en utilisant une fonction lambda.

Mais ce n'était pas tout. Nous avons examiné comment la méthode `sort()` et la fonction `sorted()` fonctionnent seules sans fonction lambda. Je vous ai également rappelé ce qu'est la fonction lambda, afin que vous puissiez comprendre comment j'ai effectué le tri avec une fonction lambda.

Merci de votre lecture !