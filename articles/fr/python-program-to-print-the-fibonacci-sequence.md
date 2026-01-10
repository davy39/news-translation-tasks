---
title: Programme Python pour imprimer la suite de Fibonacci
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-27T00:34:03.000Z'
originalURL: https://freecodecamp.org/news/python-program-to-print-the-fibonacci-sequence
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-jeff-wang-462402.jpg
tags:
- name: algorithms
  slug: algorithms
- name: interview questions
  slug: interview-questions
- name: Python
  slug: python
seo_title: Programme Python pour imprimer la suite de Fibonacci
seo_desc: "By Sonia Jessica \nQuestions about the Fibonacci Series are some of the\
  \ most commonly asked in Python interviews. \nIn this article, I'll explain a step-by-step\
  \ approach on how to print the Fibonacci sequence using two different techniques,\
  \ iteration a..."
---

Par Sonia Jessica

Les questions sur la suite de Fibonacci sont parmi les plus fréquemment posées lors des entretiens Python.

Dans cet article, je vais expliquer une approche étape par étape sur la façon d'imprimer la suite de Fibonacci en utilisant deux techniques différentes, l'itération et la récursion.

Avant de commencer, comprenons d'abord quelques termes de base.

## Qu'est-ce que la suite de Fibonacci ?

La [suite de Fibonacci](https://en.wikipedia.org/wiki/Fibonacci_number) est une suite de nombres dans laquelle un nombre donné est le résultat de l'addition des 2 nombres qui le précèdent. Et l'addition des deux nombres précédents un certain nombre de fois forme une série que nous appelons la série de Fibonacci.

La suite de Fibonacci commence avec deux nombres, à savoir 0 et 1. Ensuite, chaque nombre suivant est constitué de l'addition des deux nombres précédents.

Par exemple, prenons 0 et 1. Ce sont les deux premiers nombres de la suite. Si vous les additionnez, vous obtenez 1. Ainsi, la suite commence par 0, 1, 1,...

Ensuite, pour trouver le nombre suivant, vous additionnez le dernier nombre que vous avez et le nombre qui le précède. Donc 1+1 = 2. Ainsi, la suite jusqu'à présent est 0, 1, 1, 2, ... Comprenez-vous ?

Nous pouvons représenter cela de manière plus mathématique comme 0, 1, (1) - [0 + 1]. De même, le nombre Fibonacci suivant est - 0, 1, 1, (2) - [1 + 1]. Et ainsi de suite. Voici un diagramme montrant les 10 premiers nombres de Fibonacci :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Fibonacci-series.png)

Ceci est un exemple de série de Fibonacci – **0, 1, 1, 2, 3, 5, 8, 13, 21, 34**. Dans cette séquence continue, chaque nombre individuel est un nombre de Fibonacci.

Mathématiquement, la suite de Fibonacci est représentée par cette formule :

**F(n) = F(n-1) + F(n-2)**, où **n > 1**. 

Nous pouvons utiliser cette suite pour trouver n'importe quel nombre de Fibonacci.

Cette suite fascinante est largement associée au mathématicien Leonardo Pisano, également connu sous le nom de Fibonacci. Il était de la République de Pise, c'est pourquoi il est également connu sous le nom de Leonardo de Pise.

Leonardo était connu comme l'un des mathématiciens les plus talentueux du Moyen Âge.

## Comment imprimer la suite de Fibonacci en Python

Vous pouvez écrire un programme informatique pour imprimer la suite de Fibonacci de 2 manières différentes :

* De manière itérative, et
* De manière récursive.

L'itération signifie répéter le travail jusqu'à ce que la condition spécifiée soit remplie. La récursion, en revanche, signifie effectuer une seule tâche et passer à la suivante pour effectuer la tâche restante.

### Voici un algorithme itératif pour imprimer la suite de Fibonacci :

1. Créez 2 variables et initialisez-les avec 0 et 1 (first = 0, second = 1)
2. Créez une autre variable pour garder une trace de la longueur de la suite de Fibonacci à imprimer (length)
3. Boucle (length est inférieur à la longueur de la série)
4. Imprimez **first + second**
5. Mettez à jour les variables **first** et **second** (first pointera vers second, et second pointera vers first + second)
6. Décrémentez la variable length et répétez à partir de l'étape 3
7. Une fois la boucle terminée, terminez le programme

### Comment fonctionne l'algorithme itératif :

Supposons que nous devons imprimer une suite de Fibonacci de longueur 7. Alors le flux de l'algorithme sera comme suit :

|Itérations|Étapes expliquées|Sortie|
|----|--------|---------|
|Initial|First = 0, Second = 1|[0, 1]|
|1|Imprimer (first + second) = [0+1] Maintenant la variable `first` pointera vers la variable `second`. Et second pointera vers le nombre Fibonacci suivant que nous avons calculé ci-dessus.|[0, 1, 1]|
|2|Imprimer (first + second) = [1+1] Maintenant la variable first pointera vers la variable second. Et second pointera vers le nombre Fibonacci suivant que nous avons calculé ci-dessus.|[0, 1, 1, 2]|
|3|Imprimer (first + second) = [1+2] Maintenant la variable first pointera vers la variable second. Et second pointera vers le nombre Fibonacci suivant que nous avons calculé ci-dessus.|[0, 1, 1, 2, 3]|
|4|Imprimer (first + second) = [2+3] Maintenant la variable first pointera vers la variable second. Et second pointera vers le nombre Fibonacci suivant que nous avons calculé ci-dessus.|[0, 1, 1, 2, 3, 5]|
|5|Imprimer (first + second) = [3+5] Maintenant la variable first pointera vers la variable second. Et second pointera vers le nombre Fibonacci suivant que nous avons calculé ci-dessus.|[0, 1, 1, 2, 3, 5, 8]|

Ainsi, la suite de Fibonacci finale pour une longueur de 7 sera **[0, 1, 1, 2, 3, 5, 8]**.

### Code Python itératif pour imprimer la suite de Fibonacci :

```python
def PrintFibonacci(length):
    # Variable initiale pour le cas de base.
    first = 0
    second = 1

    # Impression des nombres initiaux de Fibonacci.
    print(first, second, end=" ")

    # Diminuer la longueur de deux car les deux premiers nombres de Fibonacci
    # sont déjà imprimés.
    length -= 2
    
    # Boucle jusqu'à ce que la longueur devienne 0.
    while length > 0:

        # Impression du nombre de Fibonacci suivant.
        print(first + second, end=" ")

        # Mise à jour des variables first et second pour trouver le nombre suivant.
        temp = second
        second = first + second
        first = temp

        # Diminuer la longueur qui indique les nombres de Fibonacci à être
        # imprimés en plus.
        length -= 1

if __name__ == "__main__":
    print("Série de Fibonacci - ")
    PrintFibonacci(7)
    pass
```

[Sortie](https://www.interviewbit.com/snippet/242ec6ca5cec8a2fcaf6/) pour une longueur de 7 :

```python
Série de Fibonacci - 
1 1 2 3 5 8
```

**Explication du code :**

Dans le code ci-dessus, nous avons d'abord défini une fonction qui imprimera la série de Fibonacci. Elle accepte un paramètre pour la longueur, et la fonction doit imprimer la série de Fibonacci.

Ensuite, nous avons créé 2 variables qui contiennent les 2 premières valeurs de Fibonacci, à savoir 0 et 1.

Puis nous avons imprimé les 2 premières valeurs [0, 1] et diminué la longueur de 2, car 2 valeurs avaient déjà été imprimées.

Nous allons exécuter une boucle pour le temps restant de la longueur, et chaque fois imprimer la valeur Fibonacci suivante en additionnant les 2 termes précédents qui sont stockés dans les variables first et second (que nous avons créées initialement pour garder une trace des 2 valeurs précédentes).

Mettre à jour les valeurs first et second qui pointeront vers les 2 valeurs précédentes [first = second, et second = previous first + second].

La boucle s'exécutera jusqu'à ce que la longueur devienne 0, ce qui indique que la longueur requise de la suite de Fibonacci est imprimée.

Ensuite, nous appelons la fonction définie pour imprimer Fibonacci depuis la fonction principale en passant l'argument de la longueur requise à imprimer. Et voilà !

Il existe une autre approche pour imprimer la suite de Fibonacci en utilisant l'aide de la récursion. Alors comprenons cette approche aussi.

### Algorithme récursif pour imprimer la suite de Fibonacci :

* Accepter la valeur du premier et du second nombre de Fibonacci précédent comme la longueur à imprimer.
* Vérifier si la longueur est 0, puis terminer l'appel de la fonction.
* Imprimer la valeur de Fibonacci en additionnant les 2 valeurs précédentes reçues dans le paramètre de la fonction (first et second).
* Appeler récursivement la fonction pour la valeur mise à jour de first et second, ainsi que la valeur diminuée de la longueur.

Pour cet appel de fonction récursif, nous devons passer la valeur initiale de Fibonacci, c'est-à-dire (0 et 1), dans les variables first et second.

Pour vous aider à mieux comprendre cet algorithme, voyons l'implémentation Python des algorithmes. Ensuite, nous examinerons un exemple pour que vous puissiez voir comment cet algorithme récursif fonctionne.

### Code Python récursif pour imprimer la suite de Fibonacci :

```python
def PrintFibonacci(first, second, length):

    # Arrêter l'impression et l'appel récursif si la longueur atteint
    # la fin.
    if(length == 0):
        return

    # Impression du nombre de Fibonacci suivant.
    print(first + second, end=" ")

    # Appel récursif de la fonction en mettant à jour la valeur et
    # en diminuant la longueur.
    PrintFibonacci(second, first+second, length-1)

if __name__ == "__main__":
    # Imprimer les 2 valeurs initiales.
    print(0,1,end=" ")

    # Appel de la fonction pour imprimer la longueur restante
    # de la série de Fibonacci
    PrintFibonacci(0,1,7-2)
```

[Sortie](https://www.interviewbit.com/snippet/1e85af84b1916aed890b/) :

```python
Pour une longueur de 7
1 1 2 3 5 8

Pour une longueur de 10
1 1 2 3 5 8 13 21 34
```

**Explication du code :**

Tout d'abord, nous avons créé une fonction et effectué une récursion sur celle-ci. Dans cette fonction, nous avons accepté la valeur des deux nombres de Fibonacci précédents pour calculer le nombre de Fibonacci actuel. Et nous avons une longueur qui garde une trace du cas de base.

Pour le cas de base de la récursion, nous vérifions si la longueur atteint 0. Si c'est le cas, alors nous allons terminer l'appel récursif.

Dans les autres cas, nous imprimons le nombre de Fibonacci en additionnant les deux nombres de Fibonacci précédents.

Et ensuite, nous appelons récursivement la fonction pour imprimer la valeur de Fibonacci suivante en mettant à jour les deux valeurs précédentes et en diminuant la longueur.

Maintenant, visualisons les appels récursifs de cette fonction à l'aide d'un arbre de récursion. La longueur que nous voulons imprimer est 7.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/length-to-be-printed-is-7.png)

Avant que l'appel récursif ne soit fait, la fonction principale imprime les 2 valeurs initiales, 0 et 1. Et ensuite, elle passe ces valeurs à la fonction récursive.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/main-function-prints-the-initial-2-values.-0-and-1.png)

La fonction récursive imprime la valeur (0 + 1) et appelle récursivement avec la valeur mise à jour suivante.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Recursive-function-is-printing-the-value--0---1-.png)

Ensuite, la fonction récursive imprime la valeur **(1 + 1)** et appelle récursivement avec la valeur mise à jour suivante.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-1-2-3-.png)

Maintenant, la fonction récursive imprime la valeur **(1 + 2)** et appelle récursivement avec la valeur mise à jour suivante.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-2-3-2-.png)

Et ensuite, la fonction récursive imprime la valeur **(2 + 3)** et appelle récursivement avec la valeur mise à jour suivante.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-3-5-1-.png)

Maintenant, la fonction récursive imprime la valeur **(3 + 5)** et appelle récursivement avec la valeur mise à jour suivante.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/printfibonacci-5-8-0-.png)

Enfin, le dernier appel est fait. Et la longueur est 0, donc il va terminer l'appel récursif à nouveau et la série est imprimée sur la console.

## Analyse de la complexité temporelle

### Pour l'approche itérative

Dans l'algorithme itératif, nous bouclons jusqu'à ce que la longueur devienne 0. Dans la boucle, nous effectuons une opération en temps constant d'impression de la valeur et de mise à jour des variables.

Si nous considérons que la longueur est n, alors la complexité temporelle sera **O(n)**.

### Pour l'approche récursive

Dans l'approche récursive, nous appelons les fonctions récursives jusqu'au nombre de fois donné par la longueur. Nous effectuons également une opération constante simple d'impression.

Donc, si nous considérons que la longueur est de n nombres, alors la complexité temporelle sera **O(n)**.

## Analyse de la complexité spatiale

### Pour l'approche itérative

Dans l'approche itérative, nous n'avons pas pris de mémoire supplémentaire pour accepter les deux variables qui gardent une trace des deux nombres de Fibonacci précédents et la constante pour n'importe quel nombre de la longueur de la série. Donc la complexité spatiale sera constante O(1).

### Pour l'approche récursive

Dans l'approche récursive, nous appelons les fonctions un nombre de fois égal à la longueur. Nous savons que la récursion utilise interne une pile d'appels.

Donc, si nous considérons que la mémoire prise par le programme, alors l'appel récursif est fait un nombre de fois égal à la longueur. Alors la complexité spatiale sera O(n).

## Conclusion

La suite de Fibonacci est la série de nombres dans laquelle chaque nombre est l'addition des deux nombres qui le précèdent.

Les suites de Fibonacci se trouvent non seulement en mathématiques mais partout dans le monde naturel – comme dans les pétales de fleurs, les feuilles ou les épines d'un cactus, et ainsi de suite.

C'est aussi une question d'entretien couramment posée – il est donc bon de savoir comment cela fonctionne.

Je me suis inspiré de cet article de [InterviewBit](https://www.interviewbit.com/python-interview-questions/).