---
title: Tutoriel sur la boucle While en Python – Exemple d'instruction Do While True
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-24T17:47:29.000Z'
originalURL: https://freecodecamp.org/news/python-while-loop-tutorial-do-while-true-example-statement
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Blue-Engagement-Essentials-Blog-Banner.png
tags:
- name: Loops
  slug: loops
- name: Python
  slug: python
seo_title: Tutoriel sur la boucle While en Python – Exemple d'instruction Do While
  True
seo_desc: 'Loops are a sequence of instructions executed until a condition is satisfied.
  Let''s look at how while loops work in Python.

  What are loops?

  If you are learning to code, loops are one of the main concepts you should understand.
  Loops help you execute ...'
---

Les boucles sont une séquence d'instructions exécutées jusqu'à ce qu'une condition soit satisfaite. Examinons comment fonctionnent les boucles while en Python.

## Qu'est-ce que les boucles ?

Si vous apprenez à coder, les boucles sont l'un des principaux concepts que vous devez comprendre. Les boucles vous aident à exécuter une séquence d'instructions jusqu'à ce qu'une condition soit satisfaite.

Il existe deux principaux types de boucles en Python.

* Boucles For
* Boucles While

Ces deux types de boucles peuvent être utilisés pour des actions similaires. Mais à mesure que vous apprenez à écrire des programmes efficaces, vous saurez quand utiliser l'une ou l'autre.

Dans cet article, nous allons examiner les boucles while en Python. Pour en savoir plus sur les boucles for, [consultez cet article récemment publié sur freeCodeCamp](https://www.freecodecamp.org/news/for-loops-in-python/).

## Boucles While

Le concept derrière une boucle while est simple : _Tant qu'une condition est vraie -> Exécute mes commandes._

La boucle while vérifiera la condition à chaque fois, et si elle retourne "vrai", elle exécutera les instructions à l'intérieur de la boucle.

Avant de commencer à écrire du code, examinons le diagramme pour voir comment cela fonctionne.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/while-loop.jpg)

Maintenant, écrivons un peu de code. Voici comment écrire une simple boucle while pour imprimer les nombres de 1 à 10.

```python
#!/usr/bin/python

x = 1

while(x <= 10):
	print(x)
	x = x+1
```

Si vous regardez le code ci-dessus, la boucle ne s'exécutera que si x est inférieur ou égal à 10. Si vous initialisez x à 20, la boucle ne s'exécutera jamais.

Voici le résultat de cette boucle while :

```
> python script.py
1
2
3
4
5
6
7
8
9
10
```

### Boucle Do-While

Il existe deux variantes de la boucle while – while et do-While. La différence entre les deux est que do-While s'exécute au moins une fois.

Une boucle while peut ne pas s'exécuter même une fois si la condition n'est pas remplie. Cependant, do-While s'exécutera une fois, puis vérifiera la condition pour les boucles suivantes.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/do-while.jpg)

En dépit d'être présente dans la plupart des langages de programmation populaires, Python ne dispose pas d'une instruction do-while native. Mais vous pouvez facilement émuler une boucle do-while en utilisant d'autres approches, telles que les fonctions.

Essayons l'approche do-while en enveloppant les commandes dans une fonction.

```
#!/usr/bin/python

x = 20

def run_commands():
	x = x+1
	print(x)


run_commands()
while(x <= 10):
	run_commands()
```

Le code ci-dessus exécute la fonction "run_commands()" une fois avant d'invoquer la boucle while. Une fois la boucle while démarrée, la fonction "run_commands" ne sera jamais exécutée puisque x est égal à 20.

### While - Else

Vous pouvez ajouter une instruction "else" à exécuter si la condition de la boucle échoue.

Ajoutons une condition else à notre code pour imprimer "Terminé" une fois que nous avons imprimé les nombres de 1 à 10.

```
#!/usr/bin/python

x = 1

while(x <= 10):
	print(x)
	x = x+1
else:
	print("Terminé")
```

Le code ci-dessus imprimera d'abord les nombres de 1 à 10. Lorsque x est 11, la condition while échouera, déclenchant la condition else.

### Instruction While sur une seule ligne

Si vous n'avez qu'une seule ligne de code dans votre boucle while, vous pouvez utiliser la syntaxe sur une seule ligne.

```
#!/usr/bin/python

x = 1
while (x): print(x)
```

### Boucles infinies

Si vous n'êtes pas prudent lors de l'écriture de boucles, vous créerez des boucles infinies. Les boucles infinies sont celles où la condition est toujours vraie.

```
#!/usr/bin/python

x = 1
while (x >= 1):
	print(x)
```

Le code ci-dessus est un exemple de boucle infinie. Il n'y a pas de commande pour modifier la valeur de x, donc la condition "x est supérieur ou égal à 1" est toujours vraie. Cela fera tourner la boucle indéfiniment.

Faites toujours attention lors de l'écriture de boucles. Une petite erreur peut entraîner une boucle infinie et faire planter votre application.

## Contrôle de boucle

Enfin, examinons comment contrôler le flux d'une boucle pendant son exécution.

Lorsque vous écrivez des applications réelles, vous rencontrerez souvent des scénarios où vous devez ajouter des conditions supplémentaires pour sauter une boucle ou pour sortir d'une boucle.

### Break

Examinons comment sortir de la boucle alors que la condition est vraie.

```
#!/usr/bin/python

x = 1
while (x <= 10):
    if(x == 5):
    	break
    print(x)
    x += 1
```

Dans le code ci-dessus, la boucle arrêtera l'exécution lorsque x est 5, malgré le fait que x soit supérieur ou égal à 1.

### Continue

Voici un autre scénario : disons que vous voulez sauter la boucle si une certaine condition est remplie. Cependant, vous voulez continuer les exécutions suivantes jusqu'à ce que la condition principale while devienne fausse.

Vous pouvez utiliser le mot-clé "continue" pour cela, comme ceci :

```
#!/usr/bin/python

x = 1
while (x <= 10):
    if(x == 5):
    	x += 1
    	continue
    print(x)
```

Dans l'exemple ci-dessus, la boucle imprimera de 1 à 10, sauf 5. Lorsque x est 5, le reste des commandes est ignoré et le flux de contrôle retourne au début du programme while.

## Résumé

Les boucles sont l'un des composants les plus utiles en programmation que vous utiliserez au quotidien.

For et while sont les deux principales boucles en Python. La boucle while a deux variantes, while et do-while, mais Python ne supporte que la première.

Vous pouvez contrôler le flux du programme en utilisant les commandes 'break' et 'continue'. Faites toujours attention à ne pas créer accidentellement des boucles infinies.

Je rédige régulièrement des articles sur des sujets incluant l'intelligence artificielle et la cybersécurité. Si vous avez aimé cet article, [vous pouvez lire mon blog ici](https://medium.com/manishmshiva).