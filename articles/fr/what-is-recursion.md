---
title: Comment fonctionne la récursivité ? Explications avec des exemples de code
subtitle: ''
author: Palistha Singh
co_authors: []
series: null
date: '2024-07-25T15:03:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-recursion
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/Frame-1--6-.png
tags:
- name: beginner
  slug: beginner
- name: Python
  slug: python
- name: Recursion
  slug: recursion
seo_title: Comment fonctionne la récursivité ? Explications avec des exemples de code
seo_desc: 'In this article, you will learn about recursion and how it works.

  You need a good understanding of how functions work before learning recursion. I
  have used Python code for examples in this article because of its simple syntax,
  but the concept of rec...'
---

Dans cet article, vous apprendrez ce qu'est la récursivité et comment elle fonctionne.

Vous devez bien comprendre comment fonctionnent les fonctions avant d'apprendre la récursivité. J'ai utilisé du code Python pour les exemples dans cet article en raison de sa syntaxe simple, mais le concept de récursivité est le même pour tous les langages de programmation.

## Qu'est-ce que la récursivité ?

Dans la plupart des langages de programmation, une fonction peut appeler une autre fonction. Mais une fonction peut aussi s'appeler elle-même. La récursivité est la technique où une fonction s'appelle elle-même.

Voici un exemple :

```bash
def call_me():
    call_me()
```

Ici, la fonction s'appelle elle-même, ce qui est appelé récursivité.

Mais "s'appeler elle-même" n'est qu'une définition programmatique de la récursivité. La récursivité consiste à décomposer un problème en morceaux plus petits jusqu'à ce qu'il ne puisse plus être décomposé. Vous résolvez les petits morceaux et les assemblez pour résoudre le problème global.

## Analogie de la récursivité dans la vie réelle

Comprenons comment la récursivité fonctionne vraiment avec l'aide d'un exemple.

Imaginez que vous êtes dans une file d'attente pour une attraction Disney, et vous ne savez pas combien de personnes sont devant vous.

Pour le découvrir, vous demandez à la personne devant vous.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/How-many--4-.png align="left")

*Essayer de découvrir combien de personnes sont devant vous dans la file*

Cette personne ne sait pas non plus, alors elle demande à la personne devant elle.

Ce processus continue jusqu'à ce que la question atteigne la personne tout devant dans la file, qui voit qu'il n'y a personne devant elle et répond qu'il y a zéro personne devant.

Les réponses commencent alors à se propager à travers la file. Chaque personne ajoute un au nombre qu'on lui a dit avant de transmettre l'information.

Lorsque la personne à l'avant répond, **"Il y a 0 personne devant"**, la personne suivante ajoute un et répond, **"Il y a 1 personne devant"**, et ainsi de suite.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/How-many--5-.png align="left")

*Tout le monde sait combien de personnes sont devant eux dans la file*

Au moment où la réponse atteint la personne directement devant vous, elle ajoute un de plus et vous le dit. Ainsi, vous pouvez déterminer votre position dans la file en ajoutant simplement **1** au nombre que la personne devant vous a donné.

Cet exemple illustre comment la récursivité décompose un problème en sous-problèmes plus petits, puis combine leurs solutions pour résoudre le problème original.

Chaque personne dans la file représente une instance plus petite du même problème : déterminer le nombre de personnes devant. En résolvant ces instances plus petites et en combinant leurs résultats, le problème global est résolu. C'est exactement ainsi que fonctionne la récursivité.

## Détails techniques de la récursivité

Les choses les plus importantes à considérer lors de la programmation de la récursivité sont de déterminer :

* **Cas récursif** : Le travail minimum que nous pouvons faire. Dans l'exemple ci-dessus, demander à la personne devant vous combien de personnes sont devant elle est la moindre quantité de travail que nous pouvons faire.
  
* **Cas de base** : Condition où aucun travail n'est requis. Dans l'exemple ci-dessus, la personne à l'avant de la file n'a pas besoin de demander quoi que ce soit, donc c'est la condition où aucun travail n'est requis.
  
## Exemple simple de récursivité

Calculer une factorielle est l'exemple le plus simple de récursivité qui vous aidera vraiment à comprendre comment elle fonctionne.

Il existe de nombreuses façons de calculer la factorielle d'un nombre. Mais ici, nous verrons la manière récursive de la trouver.

Avant de penser à la manière de le faire, nous devons savoir ce qu'est la factorielle d'un nombre.

La factorielle d'un nombre est la multiplication de tous les nombres de **1** jusqu'à ce nombre.

Par exemple, la factorielle de **5** est **120**, c'est-à-dire **5**×**4**×**3**×**2**×**1**.

Nous pouvons aussi représenter cela mathématiquement comme ceci :

`5×(5−1)!`

Cela signifie que si nous connaissons la valeur de `(5−1)!`, nous pouvons facilement obtenir la factorielle en multipliant simplement **5** par celle-ci.

Voici comment nous trouvons les factorielles de **4**, **3**, **2**, **1** et **0** :

```bash
Factorial of 4 = 4×(4−1)!
Factorial of 3 = 3×(3−1)!
Factorial of 2 = 2×(2−1)!
Factorial of 1 = 1
Factorial of 0 = 1
```

En regardant cela, il est clair que pour trouver la factorielle de **5**, nous devons multiplier **5** par `4!`.

### Exemple plus général

Pour trouver la factorielle de `n`, nous devons multiplier `n` par `(n−1)!`. C'est quelque chose que vous devez faire de manière récursive.

Maintenant, il doit y avoir une condition d'arrêt pour la récursivité. La condition d'arrêt est celle où nous n'effectuons aucune opération supplémentaire. Lorsque `n` est **1** ou `n` est **0**, nous pouvons simplement arrêter la récursivité car ces valeurs ont des factorielles connues. Nous pouvons simplement dire que la factorielle de **1** est **1** et il en va de même pour **0**.

Donc, en le décomposant, le minimum de travail que nous devons faire pour trouver la factorielle de n est `n×(n−1)!`. Et nous pouvons arrêter d'effectuer des opérations dessus lorsque nous trouvons la factorielle de **1** ou **0**.

Voyons à quoi cela ressemble en code :

```bash
# calculer la factorielle de n
def fact(n):
   
   # aucun travail requis
    if n == 1 or n == 0:
        return 1
        
    # quantité minimale de travail
    return n * fact(n - 1)

n = 5

# calculer la factorielle
factorial = fact(n)
print(factorial)
```

**Sortie :**

```bash
120
```

Voyons comment cela fonctionne :

Dans le premier appel de fonction, la factorielle de **5** est évaluée. Ensuite, dans le deuxième appel, la factorielle de **4** est évaluée, et ainsi de suite jusqu'à ce que la factorielle de **2** soit évaluée.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-1--5-.png align="left")

*Calcul récursif de la factorielle de 5*

Lors de l'appel de la factorielle de **2**, nous avons `2×fact(2−1)`, qui est `2×fact(1)`.

Cela atteint notre cas de base. Donc, la récursivité s'arrête et `2×fact(1)` retourne `2×1` à l'appel de fonction précédent, et le résultat est remonté dans la pile.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-3.png align="left")

*Quatrième appel de fonction retournant 2 à l'appel de fonction précédent et étant remonté de la pile*

De même, voici comment tout le reste est évalué :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-4.png align="left")

*3ème appel de fonction retournant 6 à l'appel de fonction précédent et étant remonté de la pile*

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-5.png align="left")

*2ème appel de fonction retournant 24 à l'appel de fonction précédent et étant remonté de la pile*

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-6.png align="left")

*1er appel de fonction retournant 120 à l'appel de fonction initial et étant remonté de la pile*

Ainsi, la fonction retourne finalement la valeur **120** à l'appel de fonction initial.

### Pourquoi avons-nous besoin d'un cas de base ?

Dans l'exemple ci-dessus, nous avons utilisé la condition d'arrêt pour le code. Mais que se passe-t-il si nous n'ajoutons pas de condition d'arrêt ou si la fonction que nous écrivons ne rencontre jamais la condition d'arrêt ?

Le code va-t-il tourner indéfiniment ?

Non – même si vous ne terminez pas, votre code ne tournera pas indéfiniment. Comprenons pourquoi c'est le cas avec l'aide d'un exemple.

```bash
def print_five():
    print(5)
    
    # s'appeler elle-même
    print_five()
    
# appel de fonction
print_five()
```

**Sortie :**

```bash
5
5
5
...

RecursionError: maximum recursion depth exceeded
```

Si vous exécutez le code ci-dessus, vous verrez que la fonction ne tourne pas indéfiniment et se termine avec un message `RecursionError: maximum recursion depth exceeded`.

Lorsque une fonction est invoquée, elle est stockée dans une pile d'appels. Voici comment la fonction `print_five()` est stockée dans la pile d'appels lorsqu'elle est invoquée pour la première fois.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/How-many--6-.png align="left")

*Pile d'appels au premier appel de fonction*

La fonction s'appelle elle-même encore et encore, et la fonction est stockée dans la pile d'appels à chaque appel.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/How-many--8-.png align="left")

*Pile d'appels après n appels de fonction*

Mais la pile d'appels a une taille limitée et ne peut pas stocker un nombre illimité de fonctions.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/How-many--7-.png align="left")

*Aucun espace sur la pile d'appels résultant en un débordement de pile*

Lorsque la pile est pleine, elle ne peut plus accommoder d'autres appels, provoquant une erreur de débordement de pile.

Par conséquent, le cas de base est essentiel pour prévenir de telles erreurs et garantir que la récursivité se termine correctement.

Maintenant, voyons un autre exemple pour comprendre encore mieux la récursivité.

## Comment vérifier si un mot est un palindrome

Avant de plonger dans le code, vous devez savoir ce qu'est un palindrome. Un palindrome est un mot qui se lit de la même manière à l'endroit et à l'envers.

Par exemple, `racecar` se lit de la même manière à l'endroit et à l'envers.

Pour vérifier si un mot est un palindrome, nous devons vérifier si la première et la dernière lettre sont les mêmes. Si elles le sont, nous vérifions ensuite si la deuxième et l'avant-dernière lettre sont les mêmes.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-7.png align="left")

*Vérifier si le premier et le dernier caractère de racecar sont les mêmes*

Dans le contexte de `racecar`, la première et la dernière lettre sont les mêmes, donc nous vérifions si la deuxième et l'avant-dernière lettre sont les mêmes. Elles le sont, donc maintenant nous vérifions si la troisième et l'avant-avant-dernière lettre sont les mêmes. Maintenant, il ne reste plus qu'une seule lettre à vérifier. Une seule lettre est toujours un palindrome car elle se lit de la même manière dans les deux sens.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-8.png align="left")

*Comment vérifier si racecar est un palindrome*

Alors, maintenant, essayons d'y penser de manière récursive, ce qui implique la quantité minimale de travail et déterminer quand aucun travail n'est requis.

### Quantité minimale de travail

Vérifier si la première et la dernière lettre sont les mêmes, et si elles le sont, supprimer la première et la dernière lettre du mot.

### Aucun travail requis

Lorsque qu'il reste une lettre ou aucune lettre du tout, nous pouvons simplement dire que c'est un palindrome.

Maintenant, voyons à quoi ressemble le code :

```bash
# vérifier palindrome
def check_palindrome(text):
   
    # condition d'arrêt
    # si la taille du texte est 1 ou 0, retourner vrai
    if len(text) == 0 or len(text) == 1:
        return True
    
    # quantité minimale de travail
    # vérifier si le premier et le dernier caractère sont les mêmes
    # si c'est le cas, supprimer le premier et le dernier caractère de la chaîne
    if(text[0]==text[-1]):
        return(check_palindrome(text[1:-1]))
    
    return False

# vérifier si la chaîne est un palindrome
text = "racecar"
is_palindrome = check_palindrome(text)
print(is_palindrome)
```

Voici comment le code ci-dessus fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Frame-9.png align="left")

*Vérifier si racecar est un palindrome*

![Image](https://www.freecodecamp.org/news/content/images/2024/07/checkpalindrome.png align="left")

*Vérifier si racecar est un palindrome*

## Quand utiliser la récursivité

La récursivité peut sembler élégante et simple. Mais elle nécessite souvent de nombreuses étapes pour résoudre même des problèmes simples en raison de la surcharge CPU due à l'ajout répété de méthodes à la pile. Donc, avant de l'utiliser, assurez-vous de bien réfléchir si c'est la bonne solution pour votre problème.

Lorsque le code nécessite plusieurs boucles et semble confus et désordonné, la récursivité peut offrir une solution plus propre. Son utilisation, cependant, dépend du code spécifique et du type de données ou de structure de données impliqué. Pour des structures de données comme les arbres et les graphes, la récursivité peut être particulièrement utile.

Malgré son apparente simplicité, la récursivité peut être difficile à comprendre et peut prendre plusieurs étapes même pour des problèmes simples. Donc, encore une fois, assurez-vous de réfléchir à votre cas d'utilisation particulier.

## Conclusion

Ce n'est qu'une introduction à la récursivité. Il existe de nombreux cas où la récursivité est utilisée, et vous pourriez être confus sur le fonctionnement de tout cela. Je couvrirai des exemples plus avancés sur la récursivité dans le prochain article.

Au fait, voici les ressources que j'ai trouvées simples et utiles lors de l'apprentissage de la récursivité :

* [Vidéo de freeCodeCamp sur la récursivité](https://www.youtube.com/watch?v=IJDJ0kBx2LM&t=657s) : Je dois rendre hommage à freeCodeCamp pour leur excellente vidéo sur la récursivité, qui a inspiré une grande partie de cet article.
  
* [Récursivité par Programiz Pro](https://programiz.pro/course/learn-recursion-with-python) : Une autre bonne ressource est le cours sur la récursivité par Programiz. C'est un cours premium, donc il n'est pas gratuit, mais il est bien conçu. De plus, vous pouvez pratiquer directement sur leur plateforme, ce qui en vaut vraiment la peine.
  

Peu importe d'où vous apprenez, ne passez pas trop de temps à chercher la ressource parfaite. Saisissez simplement les concepts et commencez à pratiquer – c'est la seule façon d'apprendre vraiment.