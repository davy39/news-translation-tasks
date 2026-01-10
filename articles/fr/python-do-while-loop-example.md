---
title: Python Do While – Exemple de boucle
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-08-31T21:15:26.000Z'
originalURL: https://freecodecamp.org/news/python-do-while-loop-example
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/pexels-pixabay-106155.jpg
tags:
- name: loop
  slug: loop
- name: Python
  slug: python
seo_title: Python Do While – Exemple de boucle
seo_desc: 'Loops are a useful and frequently used feature in all modern programming
  languages.

  If you want to automate a specific repetitive task or prevent yourself from writing
  repetitive code in your programs, using a loop is the best option for that.

  Loops ...'
---

Les boucles sont une fonctionnalité utile et fréquemment utilisée dans tous les langages de programmation modernes.

Si vous souhaitez automatiser une tâche répétitive spécifique ou éviter d'écrire du code répétitif dans vos programmes, l'utilisation d'une boucle est la meilleure option.

Les boucles sont un ensemble d'instructions qui s'exécutent répétitivement jusqu'à ce qu'une condition soit remplie. Apprenons-en plus sur le fonctionnement des boucles en Python.

## Boucles en Python

Il existe deux types de boucles intégrées en Python :

- les boucles `for`
- les boucles `while`

Concentrons-nous sur la manière de créer une boucle `while` en Python et sur son fonctionnement.

## Qu'est-ce qu'une boucle while en Python ?

La syntaxe générale d'une boucle `while` en Python ressemble à ceci :

```python
while condition:
    exécuter ce code dans le corps de la boucle
```

Une boucle while exécutera un morceau de code tant qu'une condition est vraie. Elle continuera à exécuter l'ensemble souhaité d'instructions de code jusqu'à ce que cette condition ne soit plus vraie.

Une boucle while vérifiera toujours d'abord la condition avant de s'exécuter.

Si la condition est évaluée à `True`, la boucle exécutera le code dans le corps de la boucle.

Par exemple, cette boucle s'exécute tant que `number` est inférieur à `10` :

```python
number = 0
while number < 10:
    print(f"Number is {number}!")
    number = number + 1
```

Sortie :

```
Number is 0!
Number is 1!
Number is 2!
Number is 3!
Number is 4!
Number is 5!
Number is 6!
Number is 7!
Number is 8!
Number is 9!
```

Ici, la variable `number` est initialement définie à `0`.

Avant qu'un code ne soit exécuté, Python vérifie la condition (`number < 10`). Elle est évaluée à True, donc l'instruction print est exécutée et `Number is 0!` est affiché sur la console.

`number` est ensuite incrémenté de `1`. La condition est réévaluée et elle est à nouveau True, donc toute la procédure se répète jusqu'à ce que `number` soit égal à `9`.

Cette fois, `Number is 9!` est affiché et `number` est incrémenté, mais maintenant `number` est égal à `10`, donc la condition n'est plus remplie et la boucle est terminée.

Il est possible que la boucle `while` ne s'exécute jamais si elle ne remplit pas la condition, comme dans cet exemple :

```python
number = 50
while number < 10 :
    print(f"Number is {number}!")
```

Puisque la condition est toujours False, les instructions dans le corps de la boucle ne s'exécutent pas.

### Ne créez pas de boucles infinies

Comme vous l'avez vu dans l'exemple ci-dessus, les boucles `while` sont généralement accompagnées d'une variable dont la valeur change tout au long de la durée de la boucle. Et elle détermine finalement quand la boucle se terminera.

Si vous n'ajoutez pas cette ligne, vous créerez une boucle infinie.

`number` ne sera pas incrémenté et mis à jour. Il sera toujours défini et restera à `0` et donc la condition `number < 10` sera True pour toujours. Cela signifie que la boucle continuera à boucler indéfiniment.

```python

# ne pas exécuter ceci

number = 0
while number < 10:
    print(f"Number is {number}!")
```

Sortie :

```
Number is 0!
Number is 0!
Number is 0!
Number is 0!
Number is 0!
Number is 0!
Number is 0!
...
```

Elle s'exécute indéfiniment.

C'est la même chose que de faire ceci :

```python

# ne pas exécuter ceci
while True:
    print("I am always true")
```

Que faire si vous vous trouvez dans une situation comme celle-ci ?

Appuyez sur `Control C` pour échapper et terminer la boucle.

## Qu'est-ce qu'une boucle do while ?

La syntaxe générale d'une boucle `do while` dans d'autres langages de programmation ressemble à ceci :

```
do {
  instruction de bloc de boucle à exécuter;
  }
while(condition);
```

Par exemple, une boucle do while en C ressemble à ceci :

```c
#include <stdio.h>
 
int main(void)
 {
   int i = 10;
   do {
      printf("the value of i: %i\n", i);
      i++;
      }
  while( i < 20 );
 }
```

Ce qui est unique dans les boucles do while, c'est que le code dans le bloc de boucle sera exécuté *au moins* une fois.

Le code dans l'instruction s'exécute une fois, puis la condition est vérifiée *uniquement après* que le code soit exécuté.

Donc le code s'exécute une fois d'abord, puis la condition est vérifiée.

Si la condition vérifiée est évaluée à true, la boucle continue.

Il existe des cas où vous souhaitez que votre code s'exécute au moins une fois, et c'est là que les boucles do while sont pratiques.

Par exemple, lorsque vous écrivez un programme qui prend une entrée de l'utilisateur, vous pouvez demander uniquement un nombre positif. Le code s'exécutera au moins une fois. Si le nombre que l'utilisateur soumet est négatif, la boucle continuera à s'exécuter. Si le nombre est positif, elle s'arrêtera.

Python ne dispose pas de fonctionnalité intégrée pour créer explicitement une boucle `do while` comme d'autres langages. Mais il est possible d'émuler une boucle `do while` en Python.

## Comment émuler une boucle do while en Python

Pour créer une boucle `do while` en Python, vous devez modifier légèrement la boucle `while` afin d'obtenir un comportement similaire à une boucle `do while` dans d'autres langages.

Pour rappel jusqu'à présent, une boucle `do while` s'exécutera au moins une fois. Si la condition est remplie, elle s'exécutera à nouveau.

La boucle `while`, en revanche, ne s'exécute pas au moins une fois et peut en fait ne jamais s'exécuter. Elle s'exécute lorsque et uniquement lorsque la condition est remplie.

Donc, disons que nous avons un exemple où nous voulons qu'une ligne de code s'exécute au moins une fois.

```python
secret_word = "python"
counter = 0

while True:
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 7: 
        break
```

Le code s'exécutera au moins une fois, demandant une entrée de l'utilisateur.

Il est toujours garanti de s'exécuter au moins une fois, avec `True`, ce qui crée autrement une boucle infinie.

Si l'utilisateur entre le mot secret correct, la boucle est terminée.

Si l'utilisateur entre le mauvais mot secret plus de 7 fois, la boucle sera complètement quittée.

L'instruction `break` vous permet de contrôler le flux d'une boucle `while` et d'éviter une boucle infinie.

`break` mettra immédiatement fin à la boucle actuelle et en sortira.

C'est ainsi que vous créez un effet similaire à une boucle `do while` en Python.

La boucle s'exécute toujours au moins une fois. Elle continuera à boucler si une condition n'est pas remplie, puis se terminera lorsqu'une condition sera remplie.

## Conclusion

Vous savez maintenant comment créer une boucle `do while` en Python.

Si vous êtes intéressé à en apprendre davantage sur Python, vous pouvez regarder la vidéo [12 Python Projects](https://www.youtube.com/watch?v=8ext9G7xspg&t=40s) sur la chaîne YouTube de freeCodeCamp. Vous pourrez construire 12 projets et c'est destiné aux débutants.

freeCodeCamp propose également une certification gratuite [Python Certification](https://www.freecodecamp.org/learn/scientific-computing-with-python/) pour vous aider à acquérir une bonne compréhension et une vue d'ensemble bien équilibrée des fondamentaux importants du langage.

Vous pourrez également construire cinq projets à la fin du cours pour pratiquer ce que vous avez appris.

Merci d'avoir lu et bon apprentissage !