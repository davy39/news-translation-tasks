---
title: 'Analyse de la Complexité Temporelle : Python VS C++'
subtitle: ''
author: Anthony Behery
co_authors: []
series: null
date: '2023-03-01T19:07:56.000Z'
originalURL: https://freecodecamp.org/news/python-vs-c-plus-plus-time-complexity-analysis
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/aron-visuals-BXOXnQ26B7o-unsplash.jpg
tags:
- name: algorithms
  slug: algorithms
- name: C++
  slug: c-2
- name: Python
  slug: python
seo_title: 'Analyse de la Complexité Temporelle : Python VS C++'
seo_desc: 'Speed is important in programming languages, and some execute much faster
  than others.

  For example, you might know that C++ is faster than Python. So why is this the case?

  Well, C++ is a language that uses a compiler, not to mention it is a much lowe...'
---

La vitesse est importante dans les langages de programmation, et certains s'exécutent beaucoup plus rapidement que d'autres.

Par exemple, vous savez peut-être que C++ est **plus rapide** que Python. Mais pourquoi en est-il ainsi ?

Eh bien, C++ est un langage qui utilise un compilateur, sans compter qu'il s'agit d'un langage de programmation de beaucoup plus bas niveau que Python. Cela signifie que C++ offre beaucoup moins d'**abstraction** par rapport au jeu d'instructions et à l'architecture d'un ordinateur.

D'un autre côté, Python est un langage interprété, ce qui signifie simplement que chaque ligne du programme est évaluée au fur et à mesure que le programme s'exécute.

Mais, combien plus rapide est C++ par rapport à Python ? Dans cet article, vous verrez 3 algorithmes et leurs performances en C++ et en Python. Ces algorithmes sont tirés de "Data Structures and Algorithms Using C++" par Michael T. Goodrich.

> _Note : L'ordinateur sur lequel j'ai exécuté ces tests était un Acer Swift 3. Le CPU était un Ryzen 7 7500U avec Radeon Graphics 1.80Gz. Avec 8 Go de RAM, sous Windows 10 Home._

Vous allez examiner ces algorithmes et leur **notation Big O**. Big O est une manière mathématique d'exprimer le scénario du pire cas pour la complexité temporelle ou spatiale d'un algorithme.

La complexité temporelle est le temps qu'il faut à un algorithme pour s'exécuter, tandis que la complexité spatiale est la quantité d'espace (mémoire) qu'un algorithme occupe. Voici un graphique pour aider à expliquer Big O :

![Chart](https://paper-attachments.dropbox.com/s_2D428973624E7FC84C7D69D11421DE762BEA6B6F3361231FCDCAE0425D14526F_1664885448372_Untitled.drawio+17.png)
_[Big O Cheat Sheet – Time Complexity Chart (freecodecamp.org)](https://www.freecodecamp.org/news/big-o-cheat-sheet-time-complexity-chart/)_

Désormais, je ferai référence à chaque algorithme comme s'exécutant avec une certaine complexité temporelle.

Par exemple, si je dis qu'un algorithme s'exécute avec une complexité temporelle **O(n)**, cela signifie que, à mesure que l'entrée grandit, le temps qu'il faut à l'algorithme pour s'exécuter est **linéaire**. Si je dis qu'il s'exécute avec une complexité temporelle **O(n^2)**, cela signifie que, à mesure que l'entrée grandit, le temps qu'il faut à l'algorithme pour s'exécuter est **quadratique**.

### Performance du 1er Algorithme :

```
Algorithme Ex1(A) :
    Entrée : Un tableau "A" stockant n >= 1 entiers.
    Sortie : La somme des éléments dans A.
    
    s = A[0]
    pour i = 1 à n - 1 faire :
        s = s + A[i]
    retourner s
```

En Python, nous pouvons exprimer cet algorithme comme suit :

```python
def ex1(A):
	sum = A[0]
	for i in A:
		sum = sum + A[i]
	return sum
```

Si vous utilisez des entrées allant jusqu'à environ 5 millions, vous verrez que cet algorithme prend environ 4 secondes pour s'exécuter avec une entrée aussi grande.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-228.png)
_Performance du 1er Algorithme_

Vous pouvez ensuite comparer cet algorithme en C++, comme ceci :

```c++
double ex1(double A[], size_t n)
{
    double sum = A[0];
    for(size_t i = 0; i < n; i++)
    {
        s = s + A[i];
    }
    return sum;
}
```

Vous vous demandez peut-être, qu'est-ce que `size_t` ? `size_t` est un "entier non signé". Cela signifie simplement que cette variable n'a pas de signe. Ce qui signifie également que cette variable n'est **pas négative**.

En C++, nous utilisons `size_t` pour suivre les positions dans un tableau, puisque ces positions ne peuvent pas être négatives (du moins en C++, car en Python nous pouvons avoir des index négatifs).

Examinons maintenant le temps d'exécution du premier algorithme :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-230.png)
_Performance du 1er Algorithme en C++_

Comme vous pouvez le voir sur ces deux graphiques, la complexité temporelle semble être linéaire. Cela signifie que la complexité temporelle de cet algorithme est **O(n)** – à mesure que la taille de l'entrée pour `A` grandit, le temps qu'il faut à cet algorithme pour s'exécuter grandit **de manière linéaire**.

Mais il est intéressant de noter que pour des entrées très grandes de 5 millions, C++ ne dépasse même pas la barre des 1 seconde. Alors qu'en Python, il dépasse la barre des 3-4 secondes pour des entrées d'environ 5 millions. Passons à notre prochain algorithme.

### Performance du 2ème Algorithme :

```
Algorithme Ex3(A) :
    Entrée : Un tableau "A" stockant n >= 1 entiers.
    Sortie : La somme des sommes de préfixes dans A.
    s = 0
    pour i = 0 à n - 1 faire :
        s = s + A[0]
        pour j = 1 à i faire :
            s = s + A[j]
    retourner s
```

Ici, vous pouvez voir que cet algorithme a deux boucles for. Donc, à l'avenir, c'est quelque chose à reconnaître lors de l'analyse de la complexité temporelle.

En Python, vous pouvez exprimer cet algorithme comme suit :

```python
def ex3(A):
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i]
        for j in range(1, i):
            sum = sum + A[j]
    return sum
```

Utilisons également des entrées allant jusqu'à 70 000. Ensuite, nous enregistrerons les temps et tracerons les données comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-235.png)
_Performance temporelle du 2ème Algorithme en Python_

Ces résultats sont très différents de nos graphiques précédents de l'algorithme 1. Il est important de noter qu'avec une entrée de 70 000, cet algorithme prend un temps considérable de 91 secondes en Python. C'est long !

De plus, lorsque j'ai essayé d'exécuter des entrées supérieures à 70 000, mon ordinateur a commencé à devenir non réactif. Oups.

Examinons cet algorithme en C++ :

```c++
double ex3(double A[], size_t n)
{
    double s = 0;
    for(size_t i = 0; i < n; i++)
    {
        s = s + A[i];
        for(size_t j = 1; j < i; j++)
        {
            s = s + A[j];
        }
    }
    return s;
}
```

Pour le code C++, j'ai pu augmenter la taille de l'entrée à ~90 000.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-238.png)
_Performance temporelle du 2ème Algorithme en C++_

Pour une taille d'entrée de 70 000, cet algorithme prend ~4 secondes pour s'exécuter en C++. Cette différence est énorme. Sans compter que j'ai pu utiliser des entrées d'environ ~90 000 éléments pour C++, sans même dépasser la barre des 10 secondes.

De plus, nous pouvons voir que la courbe n'est pas aussi lisse que le graphique Python. Cela pourrait être dû à d'autres processus s'exécutant en arrière-plan (puisque je suis sous Windows 10) ou à une autre raison.

De plus, nous pouvons classer la complexité temporelle de cet algorithme comme **O(n^2)**, ce qui signifie simplement que la complexité temporelle de cet algorithme est quadratique.

Passons au dernier algorithme.

### Performance du 3ème Algorithme :

```
Algorithme Ex5(A, B) :
    Entrée : Des tableaux "A" et "B" stockant chacun n >= 1 entiers.
    Sortie : Le nombre d'éléments dans B égal à la somme des
            sommes de préfixes dans A.
    c = 0
    pour i = 0 à n - 1 faire :
        s = 0
        pour j = 0 à n - 1 faire :
            s = s + A[0]
            pour k = 1 à j faire :
                s = s + A[k]
            si B[i] == s alors :
                c = c + 1
    retourner c
```

Examinons ce code en Python :

```python
def ex3(A, B):
    c = 0
    for i in range(len(A)):
        s = 0
        for j in range(len(A)):
            s = s + A[0]
            for k in range(1, j):
                s = s + A[k]
            if B[i] == s:
                c = c + 1
    return c
```

Analysons maintenant les temps d'exécution :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-241.png)
_Performance temporelle du 3ème Algorithme en Python_

Woah, que se passe-t-il ici ? Nous pouvons voir que, à mesure que nos entrées commencent à augmenter, le taux auquel l'algorithme s'exécute commence également à augmenter, mais il augmente à un rythme drastique.

Dans ce cas, nous pouvons voir qu'avec une taille d'entrée de 3500, il faut 761 secondes pour que cet algorithme s'exécute en Python. Vous vous demandez peut-être, "Avez-vous vraiment attendu toutes les 761 secondes ?", la réponse est oui. Oui, je l'ai fait.

Examinons maintenant le code C++ :

```c++
double ex5(double A[], double B[], size_t n)
{
    double c = 0;
    for(size_t i = 0; i < n; i++)
    {
        double s = 0;
        for(size_t j = 0; j < n; i++)
        {
            s = s + A[0];
            for(size_t k = 1; k < j; k++)
            {
                s = s + A[k];
            }
            if(B[i] == s)
            {
                c = c + 1;
            }
        }
    }
    return c;
}
```

Examinons le graphique.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/image-243.png)
_Performance temporelle du 3ème Algorithme en C++_

Similaire au deuxième algorithme, il est intéressant de voir que la courbe n'est pas aussi lisse que le graphique Python.

De plus, nous pouvons voir que nous pouvons aller bien au-delà d'une taille d'entrée de 3500. Mon ordinateur a commencé à avoir des problèmes une fois que j'ai poussé la taille d'entrée au-delà de 10 000 pour C++. Sans compter qu'avec une taille d'entrée de 10 000, l'algorithme a pris en moyenne environ 544-545 secondes.

Nous pouvons classer cet algorithme comme ayant une complexité temporelle de **O(n!)**. Ce qui signifie simplement que cet algorithme est factoriel, ce qui s'exécute **très lentement**.

## Conclusion

J'espère que vous avez trouvé les différences de temps d'exécution entre Python et C++ aussi fascinantes que moi.

De plus, simplement parce que Python s'exécute plus lentement que C++ pour chaque algorithme ne signifie pas que C++ est le langage "meilleur". Ces deux langages ont leurs propres objectifs en fonction du type de logiciel que vous essayez de créer.

C++ serait le langage préféré si la performance est critique. Si vous programmiez des jeux, des systèmes d'exploitation ou des communications entre machines, C++ serait le meilleur choix en raison de sa nature compilée et rapide.

Python serait préféré si vous devez développer des logiciels rapidement. Grâce à sa courbe d'apprentissage plus facile, presque tout le monde peut apprendre Python et commencer à créer des logiciels avec. Python offre également de nombreuses ressources pour la science des données et l'apprentissage automatique.

Consultez le code si vous souhaitez essayer ces tests sur votre propre ordinateur :

%[https://gist.github.com/tarmacjupiter/a1b590ceea0cb21fb01dfc7013b3a1da]

%[https://gist.github.com/tarmacjupiter/4120e8afb57db0559174b3caadbf426d]

Santé !