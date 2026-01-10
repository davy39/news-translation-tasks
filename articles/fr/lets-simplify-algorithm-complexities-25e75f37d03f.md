---
title: Simplifions les complexités des algorithmes !
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-27T06:00:49.000Z'
originalURL: https://freecodecamp.org/news/lets-simplify-algorithm-complexities-25e75f37d03f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*C9fLwET5OfP4H3GuN0f-SQ.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Mathematics
  slug: mathematics
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Simplifions les complexités des algorithmes !
seo_desc: 'By Shruti Tanwar

  It’s been a while since I started thinking about going back to the basics and brushing
  up on core computer science concepts. And I figured, before jumping into the pool
  of heavyweight topics like data structures, operating systems, O...'
---

Par Shruti Tanwar

Cela fait un moment que j'ai commencé à penser à revenir aux bases et à me rafraîchir les concepts fondamentaux de l'informatique. Et je me suis dit, avant de plonger dans le pool des sujets lourds comme les structures de données, les systèmes d'exploitation, la POO, les bases de données et la conception de systèmes (sérieusement, la liste est sans fin) ?, je devrais probablement aborder le sujet que nous ne voulons tous pas vraiment toucher : l'analyse de la complexité des algorithmes.

Oui ! Le concept qui est souvent négligé, parce que la majorité d'entre nous, développeurs, pensons, « Hmm, je n'aurai probablement pas besoin de savoir cela en codant réellement ! ». ?

Eh bien, je ne suis pas sûre que vous ayez déjà ressenti le besoin de comprendre comment fonctionne réellement l'analyse des algorithmes. Mais si c'est le cas, voici ma tentative pour l'expliquer de la manière la plus claire possible. J'espère que cela aidera quelqu'un comme moi. ?

#### **Qu'est-ce que l'analyse des algorithmes, et pourquoi en avons-nous besoin ?** ?

Avant de plonger dans l'analyse de la complexité des algorithmes, obtenons d'abord une brève idée de ce qu'est l'analyse des algorithmes. L'analyse des algorithmes consiste à comparer les algorithmes en fonction du nombre de ressources informatiques que chaque algorithme utilise.

Ce que nous voulons atteindre avec cette pratique, c'est être capable de prendre une décision éclairée sur quel algorithme est le gagnant en termes d'utilisation efficace des ressources (temps ou mémoire, selon le cas d'utilisation). Cela a-t-il du sens ?

Prenons un exemple. Supposons que nous avons une fonction _product()_ qui multiplie tous les éléments d'un tableau, sauf l'élément à l'index actuel, et retourne le nouveau tableau. Si je passe [1,2,3,4,5] comme entrée, je devrais obtenir [120, 60, 40, 30, 24] comme résultat.

La fonction ci-dessus utilise deux boucles _for_ imbriquées pour calculer le résultat souhaité. Dans le premier passage, elle prend l'élément à la position actuelle. Dans le second passage, elle multiplie cet élément avec chaque élément du tableau — sauf lorsque l'élément de la première boucle correspond à l'élément actuel de la deuxième boucle. Dans ce cas, elle le multiplie simplement par 1 pour garder le produit inchangé.

Êtes-vous capable de suivre ? Super !

C'est une approche simple qui fonctionne bien, mais pouvons-nous l'améliorer légèrement ? Pouvons-nous la modifier de telle sorte que nous n'ayons pas à utiliser deux boucles imbriquées ? Peut-être en stockant le résultat à chaque passage et en utilisant cela ?

Considérons la méthode suivante. Dans cette version modifiée, le principe appliqué est que pour chaque élément, calculer le produit des valeurs à droite, calculer les produits des valeurs à gauche, et simplement multiplier ces deux valeurs. Plutôt bien, n'est-ce pas ?

Ici, plutôt que d'utiliser des boucles imbriquées pour calculer les valeurs à chaque exécution, nous utilisons deux boucles non imbriquées, ce qui réduit la complexité globale d'un facteur de O(n) (nous y viendrons plus tard).

Nous pouvons en déduire que le deuxième algorithme performe mieux que le premier. Jusqu'à présent, tout va bien ? Parfait !

À ce stade, nous pouvons également jeter un rapide coup d'œil aux différents types d'analyse des algorithmes qui existent. Nous n'avons pas besoin d'entrer dans les détails les plus fins, mais nous devons avoir une compréhension de base du jargon technique.

Selon le moment où un algorithme est analysé, c'est-à-dire avant l'implémentation ou après l'implémentation, l'analyse des algorithmes peut être divisée en deux étapes :

* **Analyse Apriori** — Comme le nom le suggère, dans apriori (prior), nous faisons une analyse (espace et temps) d'un algorithme avant de l'exécuter sur un système spécifique. Fondamentalement, il s'agit donc d'une analyse théorique d'un algorithme. L'efficacité d'un algorithme est mesurée sous l'hypothèse que tous les autres facteurs, par exemple la vitesse du processeur, sont constants et n'ont aucun effet sur l'implémentation.
* **Analyse Apostiari** — L'analyse Apostiari d'un algorithme n'est effectuée qu'après l'avoir exécuté sur un système physique. L'algorithme sélectionné est implémenté à l'aide d'un langage de programmation qui est exécuté sur une machine informatique cible. Il dépend directement des configurations du système et change d'un système à l'autre.

Dans l'industrie, nous effectuons rarement une analyse Apostiari, car les logiciels sont généralement conçus pour des utilisateurs anonymes qui pourraient les exécuter sur différents systèmes.  
Étant donné que la complexité en temps et en espace peut varier d'un système à l'autre, l'analyse Apriori est la méthode la plus pratique pour trouver les complexités des algorithmes. Cela est dû au fait que nous ne regardons que les variations asymptotiques (nous y viendrons plus tard) de l'algorithme, ce qui donne la complexité en fonction de la taille de l'entrée plutôt que des configurations du système.

Maintenant que nous avons une compréhension de base de ce qu'est l'analyse des algorithmes, nous pouvons avancer vers notre sujet principal : la complexité des algorithmes. Nous nous concentrerons sur l'_Analyse Apriori_, en gardant à l'esprit le cadre de cet article, alors commençons.

#### **Plongeons dans la complexité avec l'analyse asymptotique**

L'analyse de la complexité des algorithmes est un outil qui nous permet d'expliquer comment un algorithme se comporte lorsque l'entrée devient plus grande.

Donc, si vous voulez exécuter un algorithme avec un ensemble de données de taille _n_, par exemple, nous pouvons définir la complexité comme une fonction numérique _f(n)_ — temps par rapport à la taille de l'entrée _n_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8jALHD5cvsBd81r916YclA@2x.jpeg)
_Temps vs Entrée_

Maintenant, vous devez vous demander, n'est-il pas possible qu'un algorithme prenne des temps différents sur les mêmes entrées, en fonction de facteurs comme la vitesse du processeur, l'ensemble d'instructions, la vitesse du disque et la marque du compilateur ? Si oui, alors félicitez-vous, car vous avez absolument raison ! ?

C'est là que l'_Analyse Asymptotique_ entre en jeu. Ici, le concept est d'évaluer la performance d'un algorithme en termes de taille d'entrée (sans mesurer le temps réel qu'il prend pour s'exécuter). Donc, fondamentalement, nous calculons comment le temps (ou l'espace) pris par un algorithme augmente lorsque nous rendons la taille de l'entrée infiniment grande.

L'analyse de la complexité est effectuée sur deux paramètres :

1. **Temps** : La complexité en temps donne une indication de la durée nécessaire à un algorithme pour se terminer par rapport à la taille de l'entrée. La ressource qui nous préoccupe dans ce cas est le CPU (et le temps réel).
2. **Espace** : La complexité en espace est similaire, mais est une indication de la quantité de mémoire « requise » pour exécuter l'algorithme par rapport à la taille de l'entrée. Ici, nous traitons avec la RAM du système comme ressource.

Êtes-vous toujours avec moi ? Bien ! Maintenant, il existe différentes notations que nous utilisons pour analyser la complexité par le biais de l'analyse asymptotique. Nous allons les passer en revue une par une et comprendre les principes fondamentaux derrière chacune.

**Le Big O (Grand O)**  
La toute première et la plus populaire notation utilisée pour l'analyse de la complexité est la notation BigO. La raison en est qu'elle donne l'analyse du pire cas d'un algorithme. L'univers des nerds s'intéresse principalement à la manière dont un algorithme peut mal se comporter, et à la manière dont il peut être amélioré. BigO nous fournit exactement cela.

Plongeons dans le côté mathématique pour comprendre les choses à leur cœur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*WH9HVd8jV7N4dbUR5jsttg@2x.jpeg)
_BigO (borne supérieure la plus serrée d'une fonction)_

Considérons un algorithme qui peut être décrit par une fonction _f(n)_. Donc, pour définir le BigO de _f(n)_, nous devons trouver une fonction, disons, _g(n)_, qui le borne. Cela signifie qu'après une certaine valeur, n0, la valeur de _g(n)_ dépassera toujours _f(n)_.

Nous pouvons l'écrire comme,  
_f(n) ≤ C g(n)_   
où n≥n0 ; C> 0 ; n0≥1

Si les conditions ci-dessus sont remplies, nous pouvons dire que _g(n)_ est le BigO de _f(n), ou_  
_f(n) = O (g(n))_

Pouvons-nous appliquer la même chose pour analyser un algorithme ? Cela signifie fondamentalement que dans le pire des cas de l'exécution d'un algorithme, la valeur ne doit pas dépasser un certain point, qui est _g(n)_ dans ce cas. Par conséquent, _g(n)_ est le BigO de _f(n)._

Passons en revue quelques notations BigO couramment utilisées et leur complexité pour mieux les comprendre.

* **O(1)** : Décrit un algorithme qui s'exécutera toujours dans le même temps (ou espace) indépendamment de la taille de l'ensemble de données d'entrée.

```
function firstItem(arr){      return arr[0];}
```

La fonction ci-dessus _firstItem()_, prendra toujours le même temps pour s'exécuter, car elle retourne le premier élément d'un tableau, quelle que soit sa taille. Le temps d'exécution de cette fonction est indépendant de la taille de l'entrée, et donc elle a une complexité constante de O(1).

En relation avec l'explication ci-dessus, même dans le pire des cas de cet algorithme (en supposant que l'entrée soit extrêmement grande), le temps d'exécution resterait constant et ne dépasserait pas une certaine valeur. Donc, sa complexité BigO est constante, c'est-à-dire O(1).

* **O(N)** : Décrit un algorithme dont la performance croîtra linéairement et en proportion directe de la taille de l'ensemble de données d'entrée. Jetez un coup d'œil à l'exemple ci-dessous. Nous avons une fonction appelée _matchValue(_) qui retourne vrai dès qu'un cas correspondant est trouvé dans le tableau. Ici, puisque nous devons itérer sur tout le tableau, le temps d'exécution est directement proportionnel à la taille du tableau.

```
function matchValue(arr, k){   for(var i = 0; i < arr.length; i++){     if(arr[i]==k){       return true;     }     else{       return false;     }   }   }
```

Cela démontre également comment Big O favorise le scénario de performance du pire cas. Un cas correspondant pourrait être trouvé lors de n'importe quelle itération de la boucle `for` et la fonction retournerait tôt. Mais la notation Big O supposera toujours la limite supérieure (pire cas) où l'algorithme effectuera le nombre maximum d'itérations.

* **O(N²)** : Cela représente un algorithme dont la performance est directement proportionnelle au carré de la taille de l'ensemble de données d'entrée. Cela est courant avec les algorithmes qui impliquent des itérations imbriquées sur l'ensemble de données. Des itérations imbriquées plus profondes entraîneront O(N³), O(N⁴), etc.

```
function containsDuplicates(arr){    for (var outer = 0; outer < arr.length; outer++){        for (var inner = 0; inner < arr.length; inner++){            if (outer == inner)                 continue;            if (arr[outer] == arr[inner])                return true;        }    }       return false;}
```

* **O(2^N)** : Désigne un algorithme dont la croissance double avec chaque ajout à l'ensemble de données d'entrée. La courbe de croissance d'une fonction O(2^N) est exponentielle — commençant très lentement, puis augmentant de manière météorique. Un exemple de fonction O(2^N) est le calcul récursif des nombres de Fibonacci :

```
function recursiveFibonacci(number){    if (number <= 1) return number;    return recursiveFibonacci(number - 2) + recursiveFibonacci(number - 1);}
```

Comprenez-vous cela ? Parfait. Si ce n'est pas le cas, n'hésitez pas à poser vos questions dans les commentaires ci-dessous. :)

En continuant, maintenant que nous avons une meilleure compréhension de la notation BigO, passons au type suivant d'analyse asymptotique qui est le Big Omega (Ω).

**Le Big Omega (Ω)** ?  
**L**e Big Omega (Ω) nous donne le meilleur scénario pour l'exécution d'un algorithme. Cela signifie qu'il nous donnera la quantité minimale de ressources (temps ou espace) qu'un algorithme prendra pour s'exécuter.

Plongeons dans les mathématiques pour l'analyser graphiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*X5E8pk9w3caz2qrrwug58w@2x.jpeg)
_BigΩ (borne inférieure la plus serrée d'une fonction)_

Nous avons un algorithme qui peut être décrit par une fonction _f(n)_. Donc, pour définir le BigΩ de _f(n)_, nous devons trouver une fonction, disons, _g(n)_, qui est la plus serrée à la borne inférieure de _f(n)_. Cela signifie qu'après une certaine valeur, n0, la valeur de _f(n)_ dépassera toujours _g(n)_.

Nous pouvons l'écrire comme,  
_f(n) ≥ C g(n)_   
où n≥n0 ; C> 0 ; n0≥1

Si les conditions ci-dessus sont remplies, nous pouvons dire que _g(n)_ est le BigΩ de _f(n), ou_  
_f(n) =_ Ω _(g(n))_

Pouvons-nous en déduire que Ω(...) est complémentaire à O(...) ? Passons à la dernière section de cet article...

**Le Big Theta (Θ)** ?  
**L**e Big Theta (Θ) est une sorte de combinaison du BigO et du BigΩ. Il nous donne le scénario moyen de l'exécution d'un algorithme. Cela signifie qu'il nous donnera la moyenne des meilleurs et des pires cas. Analysons-le mathématiquement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*c1N4K2a264c7Lz5a79HCAA@2x.jpeg)
_BigΘ (borne inférieure et supérieure la plus serrée d'une fonction)_

Considérons un algorithme qui peut être décrit par une fonction _f(n)_. Le BigΘ de _f(n)_ serait une fonction, disons, _g(n)_, qui le borne le plus serré par les bornes inférieure et supérieure, de sorte que,  
_C₁g(n) ≤ f(n) ≤ C₂ g(n)_  
où C₁, C₂ >0, n≥ n0,   
n0 ≥ 1

Cela signifie qu'après une certaine valeur, n0, la valeur de _C₁g(n)_ sera toujours inférieure à _f(n)_, et la valeur de _C₂ g(n)_ dépassera toujours _f(n)_.

Maintenant que nous avons une meilleure compréhension des différents types de complexités asymptotiques, prenons un exemple pour avoir une idée plus claire de la manière dont tout cela fonctionne en pratique.

Considérons un tableau, de taille, disons, _n_, et nous voulons effectuer une recherche linéaire pour trouver un élément _x_ dedans. Supposons que le tableau ressemble à quelque chose comme ceci en mémoire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aQTqrkxiEDXDu-UIMlt51A.png)
_Recherche linéaire_

Selon le concept de la recherche linéaire, si x=9, alors ce serait le meilleur scénario pour le cas suivant (car nous n'avons pas à itérer sur tout le tableau). Et d'après ce que nous venons d'apprendre, la complexité pour cela peut s'écrire Ω(1). Cela a-t-il du sens ?

De même, si x était égal à 14, ce serait le pire scénario, et la complexité aurait été O(n).

Quelle serait la complexité moyenne pour ce cas ?   
Θ(n/2) => 1/2 Θ(n) => Θ(n) (car nous ignorons les constantes lors du calcul des complexités asymptotiques).

Alors, voilà, les gens. Une vision fondamentale des complexités algorithmiques. Cela vous a-t-il plu ? Laissez vos conseils, questions, suggestions dans les commentaires ci-dessous. Merci d'avoir lu ! ❤️

**Références :**

* **Un bon article de Dionysis « dionyziz » Zindros :** [https://discrete.gr/complexity/](https://discrete.gr/complexity/)
* **Une bonne série sur les algorithmes et les structures de données :** [http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html](http://interactivepython.org/runestone/static/pythonds/AlgorithmAnalysis/WhatIsAlgorithmAnalysis.html)