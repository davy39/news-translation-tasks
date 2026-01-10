---
title: Comment créer un clone de Wordle avec Python
subtitle: ''
author: Tantoluwa Heritage Alabi NB
co_authors: []
series: null
date: '2022-05-12T21:24:00.000Z'
originalURL: https://freecodecamp.org/news/building-a-wordle-game
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/pexels-suzy-hazelwood-1822568.jpg
tags:
- name: Python
  slug: python
seo_title: Comment créer un clone de Wordle avec Python
seo_desc: 'Solving puzzles is a way to relax and pass the time after a long day. It
  is also beneficial to the mind.

  And even better – there are correlations between puzzle-solving and increased problem-solving
  skills.

  Wordle is a new word puzzle game that chall...'
---

Résoudre des énigmes est une façon de se détendre et de passer le temps après une longue journée. C'est également bénéfique pour l'esprit.

Et encore mieux – il existe des corrélations entre la résolution d'énigmes et l'amélioration des compétences en résolution de problèmes.

[Wordle](https://wordlegame.org/) est un nouveau jeu de mots qui défie ses joueurs de deviner un mot de cinq lettres en six essais.

Dans ce tutoriel, vous allez créer un jeu de devinettes similaire à Wordle avec les mêmes règles que le jeu original. Nous allons construire le jeu en Python. Travailler sur ce défi améliorera vos connaissances des fonctions et des boucles while, et cela vous aidera à devenir plus familier avec la méthode zip.

## Prérequis

* Connaissance de base de Python

## Ce que nous allons couvrir :

* Comment fonctionne le jeu

* Comment écrire la logique du jeu

* Résultats du jeu

## Comment fonctionne le jeu

Le jeu consistera en :

* une variable qui stocke un mot de cinq lettres appelé "hidden_word".

* une entrée de l'utilisateur.

* une variable qui stocke le nombre de fois (jusqu'à 6 essais) où l'utilisateur essaie de deviner le mot.

* une condition pour vérifier si une lettre est devinée correctement et dans la bonne position, indiquée par "✓"

* une autre condition pour vérifier si une lettre est devinée correctement mais dans la mauvaise position, indiquée par "➕"

* la condition finale pour vérifier si une lettre est devinée mais n'est pas dans le mot caché, indiquée par "✖"

## Comment écrire la logique du jeu

### Premier bloc de fonction

Tout d'abord, nous devons informer les joueurs des règles. Cela est nécessaire pour que les gens sachent comment jouer correctement.

Commencez par créer une fonction avec le nom "game_instruction".

```python
def game_instruction():
```

Ensuite, passez les instructions sous forme de chaîne à la fonction "print" pour afficher le résultat. Enveloppez les chaînes dans des docstrings (""" """) car les symboles ("✓✖✖✓➕") seront enveloppés dans des guillemets doubles (" "). De plus, chaque instruction apparaîtra sur une nouvelle ligne sans utiliser ("\n") [tag](https://replit.com/@HeritageAlabi/triplequote#main.py).

```python
print("""Wordle est un jeu pour un seul joueur
Un joueur doit deviner un mot caché de cinq lettres
Vous avez six tentatives
Votre guide de progression "✓✖✖✓➕"
"✓" Indique que la lettre à cette position a été devinée correctement
"➕" indique que la lettre à cette position est dans le mot caché, mais à une position différente
"✖" indique que la lettre à cette position est incorrecte et n'est pas dans le mot caché   """)
```

Chaque phrase commence sur une nouvelle ligne et apparaîtra ainsi sur la console. Nous terminons en appelant notre fonction pour que les instructions soient imprimées à l'écran.

```python
game_instruction()
```

Si vous obtenez une erreur, cela peut être dû au fait que vous avez oublié de mettre le deux-points (:) à la fin de la définition de la fonction `def game_instruction()` ou que votre code n'est pas correctement formaté. Faites attention à l'erreur de la console, car elle vous guidera.

### Mettre tout ensemble

```python
 def game_instruction():
     print("""Wordle est un jeu pour un seul joueur
Un joueur doit deviner un mot caché de cinq lettres
Vous avez six tentatives
Votre guide de progression "✓✖✖✓➕"
"✓" Indique que la lettre à cette position a été devinée correctement
"➕" indique que la lettre à cette position est dans le mot caché, mais à une position différente
"✖" indique que la lettre à cette position est incorrecte et n'est pas dans le mot caché   """)
game_instruction()
```

Et enfin, si vous exécutez votre code et qu'il n'y a aucun résultat sur votre console, cela signifie que vous avez probablement oublié d'appeler la fonction.

### Sortie

![Image](https://www.freecodecamp.org/news/content/images/2022/04/game_instruction.jpg align="left")

*Instructions du jeu pour les joueurs*

### Deuxième bloc de fonction

L'étape suivante consiste à travailler avec l'entrée de l'utilisateur et à la comparer avec le mot caché. La capacité à faire cela est essentielle pour le jeu.

Créez une fonction appelée "check_word". Dans le bloc de code, créez une variable nommée "hidden_word" et attribuez-lui un mot de cinq lettres de votre choix. Ce mot caché est ce que l'utilisateur essaiera de deviner correctement.

```python
def check_word():
  hidden_word = "snail"
```

Puisque le joueur a 6 essais, attribuez une nouvelle variable appelée "attempt" à la valeur "6" et créez une instruction while.

Il est préférable d'utiliser une boucle while ici car le processus s'exécute jusqu'à ce que l'utilisateur devine le bon mot ou épuise ses essais. La condition pour que l'instruction while s'exécute est si le nombre de tentatives est supérieur à "0".

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
```

L'entrée de l'utilisateur est ensuite créée à l'intérieur de la boucle while, et les conditions sont vérifiées par rapport au mot caché. Si l'entrée de l'utilisateur est la même que le mot caché, la boucle se termine et le jeu est terminé.

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Devinez le mot : "))
    if guess == hidden_word:
      print("Vous avez deviné le mot correctement ! GAGNÉ 🎺🎺🎺 ")
      break
```

Les chaînes de format (f" ") sont une autre méthode pour joindre des variables et des chaînes ensemble sans utiliser le signe "+".

Voici un exemple :

```python
# Au lieu de,
print("il vous reste" + attempt + " essai(s) ,, \n") # '\n' est utilisé pour une nouvelle ligne

# utilisez ceci,
print(f"il vous reste {attempt} essai(s) ,, \n") # la variable à imprimer est enveloppée dans des accolades
```

Si l'entrée de l'utilisateur n'est pas égale au mot caché, introduisez une instruction else et toutes les conditions seront vérifiées dans le bloc "else". Le nombre de tentatives diminue de 1 et les tentatives restantes sont imprimées sur la console au fur et à mesure que l'utilisateur joue au jeu.

```python

def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Devinez le mot : "))
    if guess == hidden_word:
      print("Vous avez deviné le mot correctement ! GAGNÉ 🎺🎺🎺 ")
      break
    else:
      attempt = attempt - 1
      print(f"il vous reste {attempt} essai(s) ,, \n ")
```

Si l'entrée de l'utilisateur ne correspond pas au mot caché, il y a trois conditions à vérifier :

* Premièrement, si la lettre est dans la mauvaise position mais dans le mot caché, imprimez un "➕" à côté de la lettre.

* Deuxièmement, si la lettre est dans la bonne position et dans le mot caché, imprimez un "✓" à côté de la lettre.

* Troisièmement, si la lettre n'est pas du tout dans le mot caché, imprimez un "✖" à côté de la lettre.

Pour comparer les lettres à la fois dans l'entrée de l'utilisateur et le mot caché, incluez une boucle for avec une fonction zip() comme instruction.

`for i, j in zip(food, drink):`

Une fonction zip() est une fonction intégrée qui parcourt des éléments comme des listes et des tuples. Elle peut extraire des valeurs de plusieurs variables de la même taille.

Pour les chaînes, vous ne pouvez pas utiliser directement la fonction zip() seule. La boucle "for" est incluse pour obtenir les lettres des variables qui stockent les chaînes.

Voici un exemple :

Un utilisateur entre un mot de cinq lettres et une variable avec un mot de cinq lettres est créée. En parcourant les deux variables en même temps avec zip(), tous les éléments seront imprimés et séparés par un trait d'union.

Bloc de code

```python
user_entry = input("épeler un mot de 5 lettres : ")
default_value = "shell"
for i, j in zip(user_entry, default_value):
  print(i + " - " +  j)
```

Sortie

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-82.png align="left")

Retour à notre code :

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Devinez le mot : "))
    if guess == hidden_word:
      print("Vous avez deviné le mot correctement ! GAGNÉ 🎺🎺🎺 ")
      break
    else:
      attempt = attempt - 1
      print(f"il vous reste {attempt} essai(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✓ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ✖ ")
```

Passons en revue ce qui se passe ici :

`for char, word in zip(hidden_word, guess)` - cette instruction signifie parcourir `hidden_word` avec le nom de variable `char` et parcourir `guess` avec le nom de variable `word`. Toutes les lettres du mot caché sont accessibles par `char` et toutes les lettres de la devinette sont accessibles par `word`.

Ensuite, les trois conditions mentionnées précédemment seront vérifiées en comparant les lettres dans `word` (l'entrée de l'utilisateur) et `char` dans (mot caché) :

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Devinez le mot : "))
    if guess == hidden_word:
      print("Vous avez deviné le mot correctement ! GAGNÉ 🎺🎺🎺 ")
      break
    else:
      attempt = attempt - 1
      print(f"il vous reste {attempt} essai(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✓ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ✖ ")
      if attempt == 0:
        print(" Game over !!!! ")
```

La dernière étape consiste à appeler la fonction :

```python
def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Devinez le mot : "))
    if guess == hidden_word:
      print("Vous avez deviné le mot correctement ! GAGNÉ 🎺🎺🎺 ")
      break
    else:
      attempt = attempt - 1
      print(f"il vous reste {attempt} essai(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✓ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ✖ ")
      if attempt == 0:
        print(" Game over !!!! ")

check_word()
```

En mettant tous les blocs de code ensemble, cela devrait ressembler à ceci :

```python
def game_instruction():
    print("""Wordle est un jeu pour un seul joueur 
Un joueur doit deviner un mot caché de cinq lettres 
Vous avez six tentatives 
Votre guide de progression "✓✖✖✓➕"  
"✓" Indique que la lettre à cette position a été devinée correctement 
"➕" indique que la lettre à cette position est dans le mot caché, mais à une position différente 
"✖" indique que la lettre à cette position est incorrecte et n'est pas dans le mot caché   """)


game_instruction()

def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Devinez le mot : "))
    if guess == hidden_word:
      print("Vous avez deviné le mot correctement ! GAGNÉ 🎺🎺🎺 ")
      break
    else:
      attempt = attempt - 1
      print(f"il vous reste {attempt} essai(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✓ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ✖ ")
      if attempt == 0:
        print(" Game over !!!! ")

check_word()
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-42.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-44.png align="left")

## Conclusion

Excellent travail ! Vous avez terminé la création d'un jeu de mots avec Python. L'exemple de code se trouve [ici](https://replit.com/@HeritageAlabi/woordle-game#main.py), et vous pouvez me contacter sur [Twitter](https://twitter.com/HeritageAlabi1) si vous avez des questions. 💙