---
title: Opérateurs Python – Les opérateurs logiques en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-03-22T00:21:14.000Z'
originalURL: https://freecodecamp.org/news/operators-in-python-how-to-use-logical-operators-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/pexels-pixabay-161154.jpg
tags:
- name: Python
  slug: python
seo_title: Opérateurs Python – Les opérateurs logiques en Python
seo_desc: "By Suchandra Datta\nOperators in any programming language are the basic\
  \ building blocks using which we can construct powerful, complex statements for\
  \ problem solving. \nPython offers different types of operators, like arithmetic\
  \ operators, logical oper..."
---

Par Suchandra Datta

Les opérateurs dans n'importe quel langage de programmation sont les briques de base avec lesquelles nous pouvons construire des instructions puissantes et complexes pour résoudre des problèmes. 

Python propose différents types d'opérateurs, tels que les opérateurs arithmétiques, les opérateurs logiques, les opérateurs relationnels, etc. Dans cet article, plongeons-nous dans les opérateurs logiques en Python et apprenons comment les utiliser.

Python propose trois opérateurs logiques ou booléens : les opérateurs "and", "or" et "not". Ceux-ci fonctionnent sur un ou plusieurs opérandes et, selon leurs valeurs, sont évalués à True ou False. Les décisions sont ensuite prises sur cette base. 

### L'opérateur "and" en Python

L'opérateur "and" en Python est un opérateur binaire, ce qui signifie qu'il nécessite deux opérandes. La syntaxe générale ressemble à ceci :

```
operand1 and operand2
```

Le résultat est True si et seulement si les deux opérandes sont True. Si l'un des opérandes est False, le résultat est False. Voyons quelques exemples :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-70.png)

Ici, nous utilisons l'opérateur "and" pour décider si une personne peut être considérée comme un joueur dans Squid Game ou non. 

Les 2 opérandes pour "and" sont les variables `person_has_debt` et `person_willing_to_play`. Comme les valeurs des deux sont True, le résultat de l'expression and est True et un nouvel objet joueur est créé où nous spécifions le nom et le numéro du joueur. 

Maintenant, que se passe-t-il si la valeur de `person_willing_to_play` est False ?

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-69.png)

Nous savons que "and" renvoie True seulement si les deux opérandes sont True. Si l'une des deux est False, le résultat est False et les instructions de la clause else sont exécutées. Nous pouvons ajouter autant d'expressions que nous le souhaitons en utilisant "and", par exemple :

```python
if person_has_debt and person_willing_to_play and proper_age and total_player_capacity_not_full:
    player_obj = SquidGamePlayer("Sae-byok", 67)
    player_obj.show_details()
else:
    print("Joueur non ajouté au jeu")
```

La valeur de vérité de l'opérande est évaluée de gauche à droite et le résultat est False si n'importe quel opérande est False, sinon le résultat est True. 

Les opérandes peuvent être des expressions arithmétiques ou relationnelles (ou toute combinaison des deux), des expressions logiques imbriquées, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-73.png)

### L'opérateur "or" en Python

L'opérateur "or" est également un opérateur binaire et nécessite 2 opérandes. Le résultat de l'expression "or" est True si l'un de ses opérandes est True, sinon le résultat est False.

```
operand1 or operand2
```

 Jetons un coup d'œil à quelques exemples simples :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-74.png)

Ici, les opérandes pour "or" sont le résultat de la méthode `has_high_traffic` avec les entrées `"some_road_name"` et `"another_road_name"`. 

Par souci de simplicité, cette méthode renvoie True ou False de manière aléatoire. Lors de la 1ère exécution, False est renvoyé pour les deux appels de méthode et "or" s'évalue à False car les deux opérandes sont False. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-76.png)

Lors de la 2ème exécution, le nombre aléatoire est maintenant 1, donc l'appel de méthode `has_high_traffic("some_road_name")` renvoie True. Nous savons que si n'importe quel opérande de "or" est True, alors le résultat final est également True. Donc dans ce cas, l'expression "or" est True et les instructions de la clause if sont exécutées. 

Avez-vous remarqué une chose ici ? Seul le 1er appel de méthode a été exécuté, et `has_high_traffic("another_road_name")` n'a pas été invoqué. Pourquoi ? Cela est dû à ce qu'on appelle le **court-circuitage** (short-circuiting), que nous allons découvrir sous peu.

### L'opérateur "not" en Python

Le "not" est un opérateur unaire, ce qui signifie qu'il fonctionne avec 1 opérande et renvoie la valeur de vérité inversée de cet opérande. 

```
not ( operand )
```

En termes simples, si l'entrée est True, alors la sortie est False et si l'entrée est False, alors la sortie est True. 

C'est simple quand les opérandes sont directement de type `bool`. Cependant, les entrées peuvent être des types numériques, des objets, des listes, etc. Dans de tels cas, le résultat dépend de la manière dont Python calcule la valeur de vérité de cette entité. 

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-78.png)

### Comment Python calcule-t-il la valeur de vérité ?

Tous les opérateurs logiques fonctionnent avec la valeur de vérité de leurs opérandes – mais qu'est-ce qu'une valeur de vérité exactement ? 

Nous savons que le type bool `True` représente le vrai et `False` représente le faux. Python considère que zéro est False et que tous les autres nombres, qu'ils soient positifs ou négatifs, sont considérés comme True. 

Regardez les exemples ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-71.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-72.png)

La valeur de vérité des entités en Python est calculée sur la base de certaines règles standards, comme défini dans la section "Truth value testing" de la documentation liée [ici](https://docs.python.org/3/library/stdtypes.html#truth-value-testing).

Ainsi, nous savons maintenant comment l'opérateur not fonctionne dans les exemples suivants :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-79.png)

Une liste vide `[]` a une longueur de zéro, sa valeur de vérité est donc False. Les zéros sont False, dans les deux cas la valeur inversée est True et 3 est True, donc `not(3)` est équivalent à `not(True)` qui est False. 

### Court-circuitage des opérateurs logiques

Les opérateurs logiques "and" et "or" en Python sont court-circuités, ce qui signifie qu'ils n'évaluent que le strict minimum nécessaire pour obtenir le bon résultat. Par exemple :

```python
if expression1 and expression2 and expression3:
	# faire quelque chose
else:
	# faire autre chose	
```

Si `expression1` est False, nous savons que le résultat final de `and` est False. Dès lors, est-il logique d'évaluer `expression2` et `expression3` ? Non, cela n'a pas de sens, et Python ne le fait pas non plus. Il commence l'évaluation de gauche à droite, et dès qu'une expression est False, le "and" s'évalue à False, sautant l'exécution des opérandes restantes. 

La même chose se produit pour l'opérateur "or" :

```
if expression1 or expression2 or expression3:
	# faire quelque chose
else:
	# faire autre chose	
```

Si `expression1` est True, alors immédiatement le résultat de l'expression "or" devient True, ignorant les 2 opérandes restantes. 

Cela permet d'éviter de passer du temps inutile à évaluer des expressions dont le résultat n'affectera de toute façon pas le résultat final de l'expression. 

### Une dernière note sur le fonctionnement de "and" et "or"

Au début de cet article, j'ai mentionné que le résultat de "and" est True si et seulement si tous ses opérandes sont True – sinon le résultat est False, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-82.png)

Voyons maintenant un peu ce qui se passe sous le capot. `and` ne renvoie pas réellement une valeur True ou False. À la place, il renvoie l'un de ses opérandes ! C'est mentionné dans la documentation [ici](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), spécifiquement cette partie, citée de la documentation :

> (Exception importante : les opérations booléennes `or` et `and` renvoient toujours l'un de leurs opérandes.)

```
operand1 and operand2
```

Ainsi, si `operand1` est False, `and` renvoie `operand1`, sinon il renvoie `operand2`. Si les opérandes sont de type bool, alors c'est facile à comprendre. Qu'en est-il si nous avons des opérandes comme les suivantes :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-80.png)

Que se passe-t-il ici ? `operand1` est 12, ce qui est True, `operand2` est 56, ce qui est aussi True, donc `and` renvoie `operand2` qui est 56. 

D'accord, mais comment cela fonctionne-t-il dans les instructions conditionnelles comme dans if-else ? Rappelez-vous que 56 a aussi une valeur de vérité, n'est-ce pas ? Donc `and` donne un résultat de 56, et maintenant la valeur de vérité de 56 est utilisée dans le if-else. 56 est True, donc la clause if est exécutée. 

De même, nous avons "or" qui renvoie également l'un de ses opérandes :

```
operand1 or operand2
```

Il renvoie `operand2` si `operand1` est False, sinon il renvoie `operand1`, comme nous pouvons le voir clairement dans l'extrait suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-81.png)

## Conclusion

Dans cet article, nous avons appris :

1. Les différents opérateurs logiques en Python et comment les utiliser avec des exemples
2. Comment Python calcule la valeur de vérité des entités
3. Ce qu'est le court-circuitage
4. Comment les opérateurs "and" et "or" fonctionnent sous le capot

Merci beaucoup de m'avoir lu, j'espère que vous avez apprécié l'article et appris quelques faits intéressants liés aux opérateurs logiques en Python. Prenez soin de vous et bon codage !