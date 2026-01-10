---
title: Comment résoudre le problème de la Tour de Hanoï - Un guide illustré sur les
  algorithmes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T16:55:19.000Z'
originalURL: https://freecodecamp.org/news/analyzing-the-algorithm-to-solve-the-tower-of-hanoi-problem-686685f032e3
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca6e9740569d1a4ca739a.jpg
tags:
- name: algorithms
  slug: algorithms
- name: code
  slug: code
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
seo_title: Comment résoudre le problème de la Tour de Hanoï - Un guide illustré sur
  les algorithmes
seo_desc: 'By Dipto Karmakar

  Before getting started, let’s talk about what the Tower of Hanoi problem is. Well,
  this is a fun puzzle game where the objective is to move an entire stack of disks
  from the source position to another position. Three simple rules ar...'
---

Par Dipto Karmakar

Avant de commencer, parlons de ce qu'est le problème de la Tour de Hanoï. Eh bien, il s'agit d'un jeu de puzzle amusant où l'objectif est de déplacer une pile entière de disques de la position source vers une autre position. Trois règles simples sont suivies :

1. Un seul disque peut être déplacé à la fois.
2. Chaque mouvement consiste à prendre le disque supérieur d'une des piles et à le placer sur une autre pile. En d'autres termes, un disque ne peut être déplacé que s'il est le disque le plus haut d'une pile.
3. Aucun disque plus grand ne peut être placé sur un disque plus petit.

Maintenant, essayons d'imaginer un scénario. Supposons que nous avons une pile de trois disques. Notre travail est de déplacer cette pile de **source A** à **destination C**. Comment faisons-nous cela ?

Avant de pouvoir y parvenir, imaginons qu'il y a un **point intermédiaire B**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*UB4f9VNg1RRs4k93.png)
_[Trois disques](http://www.texample.net/tikz/examples/towers-of-hanoi/" rel="noopener" target="_blank" title=")._

Nous pouvons utiliser B comme aide pour terminer ce travail. Nous sommes maintenant prêts à passer à l'étape suivante. Passons en revue chacune des étapes :

1. Déplacer le premier disque de A à C
2. Déplacer le premier disque de A à B
3. Déplacer le premier disque de C à B
4. Déplacer le premier disque de A à C
5. Déplacer le premier disque de B à A
6. Déplacer le premier disque de B à C
7. Déplacer le premier disque de A à C

Boom ! Nous avons résolu notre problème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fLOJ9bbxmHuFgYCeeRslhA.gif)
_Tour de Hanoï pour 3 disques. [**Wikipedia**](https://en.wikipedia.org/wiki/Tower_of_Hanoi" rel="noopener" target="_blank" title=")_

Vous pouvez voir l'image animée ci-dessus pour une meilleure compréhension.

Maintenant, essayons de construire l'algorithme pour résoudre le problème. Attendez, nous avons un nouveau mot ici : **Algorithme**. Qu'est-ce que c'est ? Une idée ? Pas de problème, voyons cela.

![Image](https://cdn-media-1.freecodecamp.org/images/0*B4f6VtfIxmB04Od1)
_Photo par [Unsplash](https://unsplash.com/@brucemars?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">bruce mars</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Qu'est-ce qu'un algorithme ?

Un algorithme est l'un des concepts les plus importants pour un développeur de logiciels. En fait, je pense qu'il n'est pas seulement important pour le développement de logiciels ou la programmation, mais pour tout le monde. Les algorithmes nous affectent dans notre vie quotidienne. Voyons comment.

Supposons que vous travaillez dans un bureau. Donc chaque matin, vous effectuez une série de tâches dans un ordre précis : d'abord vous vous réveillez, puis vous allez aux toilettes, vous prenez votre petit-déjeuner, vous vous préparez pour le bureau, vous quittez la maison, puis vous pouvez prendre un taxi ou un bus ou commencer à marcher vers le bureau et, après un certain temps, vous arrivez à votre bureau. Vous pouvez dire que toutes ces étapes forment un **algorithme**.

En termes simples, un algorithme est un ensemble de tâches. J'espère que vous n'avez pas oublié ces étapes que nous avons faites pour déplacer une pile de trois disques de A à C. Vous pouvez aussi dire que ces étapes sont l'algorithme pour résoudre le problème de la Tour de Hanoï.

> _En mathématiques et en informatique, un algorithme est une spécification non ambiguë de la manière de résoudre une classe de problèmes. Les algorithmes peuvent effectuer des calculs, des traitements de données et des tâches de raisonnement automatisé. — [Wikipedia](https://en.wikipedia.org/wiki/Algorithm)_

Si vous regardez ces étapes, vous pouvez voir que nous avons fait la même tâche plusieurs fois — déplacer des disques d'une pile à une autre. Nous pouvons appeler ces étapes à l'intérieur des étapes **récursion**.

### Récursion

![Image](https://cdn-media-1.freecodecamp.org/images/1*fsYHEgadIdn0fJt-cBXDHQ.gif)
_Récursion — [giphy](https://giphy.com/gifs/homer-simpson-the-simpsons-3ov9jQX2Ow4bM5xxuM" rel="noopener" target="_blank" title=")_

La [**récursion**](https://en.wikipedia.org/wiki/Recursion_(computer_science)) consiste à appeler la même action depuis cette action. Tout comme l'image ci-dessus.

Il y a donc une règle pour effectuer tout travail récursif : il doit y avoir une condition pour arrêter l'exécution de cette action. J'espère que vous comprenez les bases de la récursion.

Maintenant, essayons de construire une procédure qui nous aide à résoudre le problème de la Tour de Hanoï. Nous essayons de construire la solution en utilisant du **pseudocode**. Le pseudocode est une méthode d'écriture de code informatique en utilisant la langue anglaise.

```
tour(disque, source, intermédiaire, destination)
{

}
```

C'est le squelette de notre solution. Nous prenons le nombre total de disques comme argument. Ensuite, nous devons passer la source, le lieu intermédiaire et la destination afin que nous puissions comprendre la carte que nous utiliserons pour accomplir le travail.

Maintenant, nous devons trouver un **état terminal**. L'état terminal est l'état où nous n'allons plus appeler cette fonction.

```
SI disque est égal à 1
```

Dans notre cas, ce serait notre état terminal. Parce que lorsqu'il y aura un disque dans notre pile, il sera facile de faire cette dernière étape et après cela, notre tâche sera terminée. Ne vous inquiétez pas si ce n'est pas clair pour vous. Lorsque nous atteindrons la fin, ce concept sera plus clair.

Très bien, nous avons trouvé notre point d'état terminal où nous déplaçons notre disque vers la destination comme ceci :

```
déplacer le disque de la source vers la destination
```

Maintenant, nous appelons notre fonction à nouveau en passant ces arguments. Dans ce cas, nous divisons la pile de disques en deux parties. Le plus grand disque (**n-ième** disque) est dans une partie et tous les autres (**n-1**) disques sont dans la deuxième partie. Là, nous appelons la méthode deux fois pour -(n-1).

```
tour(disque - 1, source, destination, intermédiaire)
```

Comme nous l'avons dit, nous passons **total_disques_sur_pile — 1** comme argument. Et ensuite, nous déplaçons à nouveau notre disque comme ceci :

```
déplacer le disque de la source vers la destination
```

Après cela, nous appelons à nouveau notre méthode comme ceci :

```
tour(disque - 1, intermédiaire, source, destination)
```

Regardons notre pseudocode complet :

```
tour(disque, source, inter, dest)

SI disque est égal à 1, ALORS
      déplacer le disque de la source vers la destination
   SINON
      tour(disque - 1, source, destination, intermédiaire)   // Étape 1
      déplacer le disque de la source vers la destination                 // Étape 2
      tour(disque - 1, intermédiaire, source, destination)   // Étape 3
   FIN SI
   
FIN
```

Voici l'arbre pour trois disques :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LEkUpm8-CoxGko2f84gjOg.jpeg)
_Arbre de la tour de Hanoï (3 disques)_

Voici le code complet en Ruby :

```rb
def tour(nombre_disques, source, auxiliaire, destination)
  if nombre_disques == 1
    puts "#{source} -> #{destination}"
    return
  end
  tour(nombre_disques - 1, source, destination, auxiliaire)
  puts "#{source} -> #{destination}"
  tour(nombre_disques - 1, auxiliaire, source, destination)
  nil
end
```

Appeler `tour(3, 'source','aux','dest')`

Sortie :

```
source -> dest
source -> aux
dest -> aux
source -> dest
aux -> source
aux -> dest
source -> dest
```

Il a fallu sept étapes pour que trois disques atteignent la destination. Nous appelons cela une **méthode récursive**.

![Image](https://cdn-media-1.freecodecamp.org/images/0*VXmzOesqL7l18gAr)
_Photo par [Unsplash](https://unsplash.com/@aronvisuals?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Aron Visuals</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

### Calculs de la complexité temporelle et spatiale

#### [Complexité temporelle](https://www.techopedia.com/definition/22573/time-complexity)

Lorsque nous exécutons du code ou une application sur notre machine, cela prend du temps — des cycles CPU. Mais ce n'est pas la même chose pour tous les ordinateurs. Par exemple, le temps de traitement pour un core i7 et un dual core ne sont pas les mêmes. Pour résoudre ce problème, il existe un concept utilisé en informatique appelé **complexité temporelle**.

> La complexité temporelle est un concept en informatique qui traite de la quantification de la quantité de temps prise par un ensemble de code ou un algorithme pour traiter ou s'exécuter en fonction de la quantité d'entrée. 
> 
> En d'autres termes, la complexité temporelle est essentiellement l'efficacité, ou combien de temps une fonction de programme prend pour traiter une entrée donnée. — [techopedia](https://www.techopedia.com/definition/22573/time-complexity)

La complexité temporelle des algorithmes est le plus souvent exprimée en utilisant la **notation big O**. C'est une notation asymptotique pour représenter la complexité temporelle.

Maintenant, le **temps** nécessaire pour déplacer **n** disques est **T(n)**. Il y a deux appels récursifs pour (**n-1**). Il y a une opération en temps constant pour déplacer un disque de la source à la destination, appelons cela **m1**. Par conséquent :

```
T(n) = 2T(n-1) + m1    ..... eq(1)
```

Et

```
T(0) = m2, une constante   ...... eq(2)
D'après eq (1)
T(1) = 2T(1-1) + m1
     = 2T(0)+m1
     = 2m2 + m1 ..... eq(3) [D'après eq 2]
T(2) = 2T(2-1) + m1
     = 2T(1) + m1
     = 4m2 + 2m1 + m1 .... eq(4) [D'après eq(3)]
T(3) = 2T(3-1) + m1
     = 2T(2) + m1
     = 8m2 + 4m1 + 2m1 + m1  [D'après eq(4)]
```

D'après ces motifs — eq(2) au dernier — nous pouvons dire que la complexité temporelle de cet algorithme est **O(2^n)** ou **O(a^n)** où **a** est une constante supérieure à 1. Il a donc une complexité temporelle exponentielle. Pour une seule augmentation de la taille du problème, le temps requis est le double du précédent. Cela est très coûteux en termes de calcul. La plupart des programmes récursifs prennent un temps exponentiel, et c'est pourquoi il est très difficile de les écrire de manière itérative.

#### [Complexité spatiale](https://www.cs.northwestern.edu/academics/courses/311/html/space-complexity.html)

Après l'explication de l'analyse de la complexité temporelle, je pense que vous pouvez maintenant deviner ce que c'est... Il s'agit du calcul de l'espace requis en RAM pour exécuter un code ou une application.

Dans notre cas, l'espace pour le paramètre de chaque appel est indépendant de **n**, ce qui signifie qu'il est constant. Appelons-le **J**. Lorsque nous faisons le deuxième appel récursif, le premier est terminé. Cela signifie que nous pouvons réutiliser l'espace après avoir terminé le premier. Par conséquent :

```
T(n) = T(n-1) + k .... eq(1)
T(0) = k, [constante] .... eq(2)
T(1) = T(1-1) + k
     = T(0) + k
     = 2K
T(2) = 3k
T(3) = 4k
```

La complexité spatiale est donc **O(n)**.

Après ces analyses, nous pouvons voir que la complexité temporelle de cet algorithme est exponentielle mais que la complexité spatiale est linéaire.

### Conclusion

À partir de cet article, j'espère que vous pouvez maintenant comprendre le puzzle de la **Tour de Hanoï** et comment le résoudre. De plus, j'ai essayé de vous donner une compréhension de base des **algorithmes, de leur importance, de la récursion, du pseudocode, de la complexité temporelle** et de la **complexité spatiale**. Si vous souhaitez apprendre ces sujets en détail, voici quelques liens de cours en ligne bien connus :

1. [Algorithmes, Partie I](https://www.coursera.org/course/algs4partI)
2. [Algorithmes, Partie II](https://www.coursera.org/course/algs4partII)
3. [Le cours Google sur Udacity](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513)
4. [Certification en Algorithmes et Structures de Données en JavaScript (300 heures)](https://learn.freecodecamp.org/)

Vous pouvez visiter mon [dépôt de structures de données et algorithmes](https://github.com/dipto0321/datastructures-and-algorithm) pour voir mes autres solutions de problèmes.

Je suis sur [GitHub](https://github.com/dipto0321/) | [Twitter](https://twitter.com/Diptokmk47) | [LinkedIn](https://www.linkedin.com/in/diptokarmakar47/)