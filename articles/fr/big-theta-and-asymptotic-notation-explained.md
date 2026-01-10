---
title: Big Theta et Notation Asymptotique Expliqués
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-06T22:16:00.000Z'
originalURL: https://freecodecamp.org/news/big-theta-and-asymptotic-notation-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e1b740569d1a4ca3b63.jpg
tags:
- name: algorithms
  slug: algorithms
seo_title: Big Theta et Notation Asymptotique Expliqués
seo_desc: "Big Omega tells us the lower bound of the runtime of a function, and Big\
  \ O tells us the upper bound. \nOften times, they are different and we can’t put\
  \ a guarantee on the runtime - it will vary between the two bounds and the inputs.\
  \ But what happens w..."
---

Big Omega nous indique la borne inférieure du temps d'exécution d'une fonction, et Big O nous indique la borne supérieure. 

Souvent, elles sont différentes et nous ne pouvons pas garantir le temps d'exécution - il variera entre les deux bornes et les entrées. Mais que se passe-t-il lorsqu'elles sont les mêmes ? Alors nous pouvons donner une borne **theta** (Θ) - notre fonction s'exécutera dans ce temps, peu importe l'entrée que nous lui donnons. 

En général, nous voulons toujours donner une borne theta si possible car c'est la borne la plus précise et la plus serrée. Si nous ne pouvons pas donner une borne theta, la meilleure chose suivante est la borne O la plus serrée possible.

Prenons, par exemple, une fonction qui recherche un tableau pour la valeur 0 :

```python
def containsZero(arr): #supposons un tableau normal de longueur n sans cas particuliers
  for num x in arr:
    if x == 0:
       return true
  return false
```

1. Quel est le meilleur cas ? Eh bien, si le tableau que nous lui donnons a 0 comme première valeur, il prendra un temps constant : Ω (1)
2. Quel est le pire cas ? Si le tableau ne contient pas 0, nous aurons parcouru tout le tableau : O(n)

Nous lui avons donné une borne omega et O, alors qu'en est-il de theta ? Nous ne pouvons pas lui en donner une ! Selon le tableau que nous lui donnons, le temps d'exécution sera quelque part entre constant et linéaire.

Changeons un peu notre code.

```python
def printNums(arr): #supposons un tableau normal de longueur n sans cas particuliers
  for num x in arr:
    print(x)
```

Pouvez-vous penser à un meilleur cas et à un pire cas ?? Je ne peux pas ! Peu importe le tableau que nous lui donnons, nous devons parcourir chaque valeur du tableau. Donc la fonction prendra AU MOINS n temps (Ω(n)), mais nous savons aussi qu'elle ne prendra pas plus de n temps (O(n)). Que signifie cela ? Notre fonction prendra **exactement** n temps : Θ(n).

Si les bornes sont confuses, pensez-y comme ceci. Nous avons 2 nombres, x et y. On nous dit que x <= y et que y <= x. Si x est inférieur ou égal à y, et y est inférieur ou égal à x, alors x doit être égal à y !

Si vous êtes familier avec les listes chaînées, testez-vous et pensez aux temps d'exécution pour chacune de ces fonctions !

1. get
2. remove
3. add

Les choses deviennent encore plus intéressantes lorsque vous considérez une liste doublement chaînée !

## **Notation Asymptotique**

Comment mesurons-nous la valeur de performance des algorithmes ?

Considérez comment le temps est l'une de nos ressources les plus précieuses. En informatique, nous pouvons mesurer la performance avec la quantité de temps qu'un processus prend pour se compléter. Si les données traitées par deux algorithmes sont les mêmes, nous pouvons décider de la meilleure implémentation pour résoudre un problème.

Nous faisons cela en définissant les limites mathématiques d'un algorithme. Ce sont les big-O, big-omega, et big-theta, ou les notations asymptotiques d'un algorithme. Sur un graphique, le big-O serait le temps le plus long qu'un algorithme pourrait prendre pour un ensemble de données donné, ou la "borne supérieure". Big-omega est comme l'opposé de big-O, la "borne inférieure". C'est là que l'algorithme atteint sa vitesse maximale pour un ensemble de données. Big theta est soit la valeur de performance exacte de l'algorithme, soit une plage utile entre des bornes supérieure et inférieure étroites.

Quelques exemples :

* "La livraison sera là dans votre vie." (big-O, borne supérieure)
* "Je peux vous payer au moins un dollar." (big-omega, borne inférieure)
* "Le maximum aujourd'hui sera de 25°C et le minimum sera de 19°C." (big-theta, étroit)
* "C'est une marche d'un kilomètre jusqu'à la plage." (big-theta, exact)

#### **Plus d'informations :**

[https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation](https://www.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-big-theta-notation) [https://stackoverflow.com/questions/10376740/what-exactly-does-big-%D3%A8-notation-represent](https://stackoverflow.com/questions/10376740/what-exactly-does-big-%D3%A8-notation-represent) [https://www.geeksforgeeks.org/analysis-of-algorithms-set-3asymptotic-notations/](https://www.geeksforgeeks.org/analysis-of-algorithms-set-3asymptotic-notations/)