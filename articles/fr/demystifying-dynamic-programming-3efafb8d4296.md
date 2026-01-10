---
title: Démystifier la programmation dynamique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-31T18:40:40.000Z'
originalURL: https://freecodecamp.org/news/demystifying-dynamic-programming-3efafb8d4296
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7QbvB25maQRxi7LGYOAfYw.png
tags:
- name: Computer Science
  slug: computer-science
- name: Dynamic Programming
  slug: dynamic-programming
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
seo_title: Démystifier la programmation dynamique
seo_desc: 'By Alaina Kafkes

  How to construct & code dynamic programming algorithms


  Maybe you’ve heard about it in preparing for coding interviews. Maybe you’ve struggled
  through it in an algorithms course. Maybe you’re trying to learn how to code on
  your own, ...'
---

Par Alaina Kafkes

#### Comment construire et coder des algorithmes de programmation dynamique

![Image](https://cdn-media-1.freecodecamp.org/images/1*7QbvB25maQRxi7LGYOAfYw.png)

Peut-être en avez-vous entendu parler en vous préparant pour des entretiens de codage. Peut-être avez-vous lutté avec cela dans un cours d'algorithmes. Peut-être essayez-vous d'apprendre à coder par vous-même et on vous a dit quelque part en cours de route qu'il est important de comprendre la programmation dynamique. Utiliser la programmation dynamique (DP) pour écrire des algorithmes est aussi essentiel que redouté.

Et qui peut blâmer ceux qui s'en éloignent ? La programmation dynamique semble intimidante parce qu'elle est mal enseignée. De nombreux tutoriels se concentrent sur le résultat — *expliquer* l'algorithme, au lieu du processus — *trouver* l'algorithme. Cela encourage la mémorisation, pas la compréhension.

Pendant mon cours d'algorithmes cette année, j'ai assemblé mon propre processus pour résoudre des problèmes qui nécessitent de la programmation dynamique. Certaines parties proviennent de [mon professeur d'algorithmes](https://sites.northwestern.edu/hartline/) (à qui beaucoup de crédit est dû !), et d'autres de ma propre dissection des algorithmes de programmation dynamique.

Mais avant de partager mon processus, commençons par les bases. Qu'est-ce que la programmation dynamique, au fait ?

### Définition de la programmation dynamique

La programmation dynamique consiste à **décomposer un problème d'optimisation** en sous-problèmes plus simples, et à **stocker la solution à chaque sous-problème** afin que chaque sous-problème ne soit résolu qu'une seule fois.

Pour être honnête, cette définition peut ne pas avoir totalement de sens jusqu'à ce que vous voyiez un exemple de sous-problème. Ce n'est pas grave, cela arrive dans la section suivante.

Ce que j'espère transmettre, c'est que la DP est une technique utile pour les problèmes d'optimisation, ces problèmes qui cherchent la solution maximale ou minimale donnée certaines contraintes, car elle examine tous les sous-problèmes possibles et ne recalcule jamais la solution à un sous-problème. Cela garantit la justesse et l'efficacité, ce que nous ne pouvons pas dire de la plupart des techniques utilisées pour résoudre ou approximer des algorithmes. Cela seul rend la DP spéciale.

Dans les deux sections suivantes, j'expliquerai ce qu'est un **sous-problème**, puis je motiverai pourquoi le stockage des solutions — une technique connue sous le nom de **mémoisation** — est important en programmation dynamique.

### Sous-problèmes sur sous-problèmes sur sous-problèmes

Les sous-problèmes sont des versions plus petites du problème original. En fait, les sous-problèmes ressemblent souvent à une version reformulée du problème original. Si ils sont formulés correctement, les sous-problèmes se construisent les uns sur les autres afin d'obtenir la solution au problème original.

Pour vous donner une meilleure idée de comment cela fonctionne, trouvons le sous-problème dans un exemple de problème de programmation dynamique.

Imaginez que vous êtes de retour dans les années 1950 travaillant sur un ordinateur IBM-650. Vous savez ce que cela signifie — des cartes perforées ! Votre travail est de gérer l'IBM-650 pour une journée. Vous recevez un nombre naturel *n* de cartes perforées à exécuter. Chaque carte perforée *i* doit être exécutée à un temps de début prédéterminé *s_i* et doit cesser de s'exécuter à un temps de fin prédéterminé *f_i*. Une seule carte perforée peut s'exécuter sur l'IBM-650 à la fois. Chaque carte perforée a également une valeur associée *v_i* basée sur son importance pour votre entreprise.

**Problème** : En tant que personne responsable de l'IBM-650, vous devez déterminer l'horaire optimal des cartes perforées qui maximise la valeur totale de toutes les cartes perforées exécutées.

Parce que je vais passer en revue cet exemple en détail tout au long de cet article, je ne vais vous donner que son sous-problème pour l'instant :

**Sous-problème** : L'horaire de valeur maximale pour les cartes perforées *i* à *n* tel que les cartes perforées sont triées par temps de début.

Remarquez comment le sous-problème décompose le problème original en composants qui construisent la solution. Avec le sous-problème, vous pouvez trouver l'horaire de valeur maximale pour les cartes perforées *n-1* à *n*, puis pour les cartes perforées *n-2* à *n*, et ainsi de suite. En trouvant les solutions pour chaque sous-problème, vous pouvez ensuite aborder le problème original lui-même : l'horaire de valeur maximale pour les cartes perforées 1 à *n*. Puisque le sous-problème ressemble au problème original, les sous-problèmes peuvent être utilisés pour résoudre le problème original.

En programmation dynamique, après avoir résolu chaque sous-problème, vous devez le mémoïser, ou le stocker. Découvrons pourquoi dans la section suivante.

### Motiver la mémoïsation avec les nombres de Fibonacci

Lorsque l'on vous demande d'implémenter un algorithme qui calcule la [valeur de Fibonacci](https://www.mathsisfun.com/numbers/fibonacci-sequence.html) pour un nombre donné, que feriez-vous ? La plupart des gens que je connais opteraient pour un [algorithme récursif](https://softwareengineering.stackexchange.com/questions/25052/in-plain-english-what-is-recursion) qui ressemble à ceci en Python :

```
def fibonacciVal(n):  if n == 0:    return 0  elif n == 1:    return 1  else:    return fibonacciVal(n-1) + fibonacciVal(n-2)
```

Cet algorithme accomplit son but, mais à un coût *énorme*. Par exemple, regardons ce que cet algorithme doit calculer afin de résoudre pour n = 5 (abrévié en F(5)) :

```
F(5)                      /      \                                     /        \                  /          \               F(4)          F(3)            /       \        /   \          F(3)     F(2)     F(2)  F(1)         /   \     /  \     /   \       F(2) F(1) F(1) F(0) F(1) F(0)       /  \     F(1) F(0)
```

L'arbre ci-dessus représente chaque calcul qui doit être fait afin de trouver la valeur de Fibonacci pour n = 5. Remarquez comment le sous-problème pour n = 2 est résolu **trois fois**. Pour un exemple relativement petit (n = 5), c'est beaucoup de calculs répétés, et gaspillés !

Et si, au lieu de calculer la valeur de Fibonacci pour n = 2 trois fois, nous créions un algorithme qui la calcule une fois, stocke sa valeur, et accède à la valeur de Fibonacci stockée pour chaque occurrence ultérieure de n = 2 ? C'est *exactement* ce que fait la mémoïsation.

Avec cela en tête, j'ai écrit une solution de programmation dynamique pour le problème de la valeur de Fibonacci :

```
def fibonacciVal(n):  memo = [0] * (n+1)  memo[0], memo[1] = 0, 1  for i in range(2, n+1):    memo[i] = memo[i-1] + memo[i-2]  return memo[n]
```

Remarquez comment la solution de la valeur de retour provient du tableau de mémoïsation memo[ ], qui est rempli de manière itérative par la boucle for. Par "itérativement", je veux dire que memo[2] est calculé et stocké avant memo[3], memo[4], ..., et memo[_n_]. Parce que memo[ ] est rempli dans cet ordre, la solution pour chaque sous-problème (n = 3) peut être résolue par les solutions à ses sous-problèmes précédents (n = 2 et n = 1) parce que ces valeurs ont déjà été stockées dans memo[ ] à un moment antérieur.

La mémoïsation signifie pas de re-calcul, ce qui rend l'algorithme plus efficace. Ainsi, la mémoïsation garantit que la programmation dynamique est efficace, mais c'est le choix du bon sous-problème qui garantit qu'un programme dynamique passe par toutes les possibilités afin de trouver la meilleure.

Maintenant que nous avons abordé la mémoïsation et les sous-problèmes, il est temps d'apprendre le processus de programmation dynamique. Attachez vos ceintures.

### Mon processus de programmation dynamique

#### Étape 1 : Identifier le sous-problème en mots.

Trop souvent, les programmeurs se tournent vers l'écriture de code *avant* de réfléchir de manière critique au problème en question. Pas bien. Une stratégie pour activer votre cerveau avant de toucher au clavier est d'utiliser des mots, en anglais ou autre, pour décrire le sous-problème que vous avez identifié dans le problème original.

Si vous résolvez un problème qui nécessite de la programmation dynamique, prenez une feuille de papier et réfléchissez aux informations dont vous avez besoin pour résoudre ce problème. Écrivez le sous-problème en gardant cela à l'esprit.

Par exemple, dans le problème des cartes perforées, j'ai déclaré que le sous-problème peut s'écrire comme "l'horaire de valeur maximale pour les cartes perforées *i* à *n* tel que les cartes perforées sont triées par temps de début." J'ai trouvé ce sous-problème en réalisant que, afin de déterminer l'horaire de valeur maximale pour les cartes perforées 1 à *n* tel que les cartes perforées sont triées par temps de début, je devrais trouver la réponse aux sous-problèmes suivants :

* L'horaire de valeur maximale pour les cartes perforées *n-1* à *n* tel que les cartes perforées sont triées par temps de début
* L'horaire de valeur maximale pour les cartes perforées *n-2* à *n* tel que les cartes perforées sont triées par temps de début
* L'horaire de valeur maximale pour les cartes perforées *n-3* à *n* tel que les cartes perforées sont triées par temps de début
* (Et ainsi de suite)
* L'horaire de valeur maximale pour les cartes perforées 2 à *n* tel que les cartes perforées sont triées par temps de début

Si vous pouvez identifier un sous-problème qui s'appuie sur des sous-problèmes précédents pour résoudre le problème en question, alors vous êtes sur la bonne voie.

#### Étape 2 : Écrire le sous-problème comme une décision mathématique récurrente.

Une fois que vous avez identifié un sous-problème en mots, il est temps de l'écrire mathématiquement. Pourquoi ? Eh bien, la **récurrence** mathématique, ou décision répétée, que vous trouvez sera finalement ce que vous mettrez dans votre code. De plus, écrire le sous-problème mathématiquement valide votre sous-problème en mots de l'Étape 1. Si c'est difficile d'encoder votre sous-problème de l'Étape 1 en maths, alors ce peut être le mauvais sous-problème !

Il y a deux questions que je me pose chaque fois que j'essaie de trouver une récurrence :

* Quelle décision prends-je à chaque étape ?
* Si mon algorithme est à l'étape *i*, quelles informations aurait-il besoin pour décider quoi faire à l'étape *i+1* ? (Et parfois : Si mon algorithme est à l'étape *i*, quelles informations avait-il besoin pour décider quoi faire à l'étape *i-1* ?)

Revenons au problème des cartes perforées et posons ces questions.

**Quelle décision prends-je à chaque étape ?** Supposons que les cartes perforées sont triées par temps de début, comme mentionné précédemment. Pour chaque carte perforée qui est compatible avec l'horaire jusqu'à présent (son temps de début est après le temps de fin de la carte perforée qui est actuellement en cours d'exécution), l'algorithme doit choisir entre deux options : exécuter, ou ne pas exécuter la carte perforée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*b69mBGpwu6bGJrIlodV6Jw.jpeg)
*Ce programme dynamique choisit entre deux options à chaque étape, tout comme notre cher ami Hamlet !*

**Si mon algorithme est à l'étape** **_i_, quelles informations aurait-il besoin pour décider quoi faire à l'étape** **_i+1_?** Pour décider entre les deux options, l'algorithme doit connaître la prochaine carte perforée compatible dans l'ordre. La prochaine carte perforée compatible pour une carte perforée donnée *p* est la carte perforée *q* telle que *s_q* (le temps de début prédéterminé pour la carte perforée *q*) se produit après *f_p* (le temps de fin prédéterminé pour la carte perforée *p*) et la différence entre *s_q* et *f_p* est minimisée. Abandonnant le langage mathématicien, la prochaine carte perforée compatible est celle avec le temps de début le plus tôt après que la carte perforée actuelle ait fini de s'exécuter.

**Si mon algorithme est à l'étape** **_i_, quelles informations avait-il besoin pour décider quoi faire à l'étape** **_i-1_?** L'algorithme doit connaître les décisions futures : celles prises pour les cartes perforées *i* à *n* afin de décider d'exécuter ou non la carte perforée *i-1*.

Maintenant que nous avons répondu à ces questions, peut-être avez-vous commencé à former une décision mathématique récurrente dans votre esprit. Si ce n'est pas le cas, ce n'est pas grave non plus, il devient plus facile d'écrire des récurrences à mesure que vous êtes exposé à plus de problèmes de programmation dynamique.

Sans plus tarder, voici notre récurrence :

```
OPT(i) = max(v_i + OPT(next[i]), OPT(i+1))
```

Cette récurrence mathématique nécessite quelques explications, surtout pour ceux qui n'en ont jamais écrit auparavant. J'utilise OPT(*i*) pour représenter l'horaire de valeur maximale pour les cartes perforées *i* à *n* tel que les cartes perforées sont triées par temps de début. Cela semble familier, n'est-ce pas ? OPT(•) est notre sous-problème de l'Étape 1.

Afin de déterminer la valeur de OPT(*i*), nous considérons deux options, et nous voulons prendre le *maximum* de ces options afin d'atteindre notre objectif : l'horaire de *valeur maximale* pour toutes les cartes perforées. Une fois que nous avons choisi l'option qui donne le résultat maximum à l'étape *i*, nous mémoïson sa valeur en tant que OPT(*i*).

Les deux options — exécuter ou ne pas exécuter la carte perforée *i* — sont représentées mathématiquement comme suit :

```
v_i + OPT(next[i])
```

Cette clause représente la décision d'exécuter la carte perforée *i*. Elle ajoute la valeur obtenue de l'exécution de la carte perforée *i* à OPT(next[*i*]), où next[*i*] représente la prochaine carte perforée compatible suivant la carte perforée *i*. OPT(next[*i*]) donne l'horaire de valeur maximale pour les cartes perforées next[*i*] à *n* tel que les cartes perforées sont triées par temps de début. L'addition de ces deux valeurs ensemble produit l'horaire de valeur maximale pour les cartes perforées *i* à *n* tel que les cartes perforées sont triées par temps de début si la carte perforée *i* est exécutée.

```
OPT(i+1)
```

Inversement, cette clause représente la décision de ne pas exécuter la carte perforée *i*. Si la carte perforée *i* n'est pas exécutée, sa valeur n'est pas obtenue. OPT(*i+1*) donne l'horaire de valeur maximale pour les cartes perforées *i+1* à *n* tel que les cartes perforées sont triées par temps de début. Ainsi, OPT(*i+1*) donne l'horaire de valeur maximale pour les cartes perforées *i* à *n* tel que les cartes perforées sont triées par temps de début si la carte perforée *i* n'est pas exécutée.

De cette manière, la décision prise à chaque étape des problèmes de cartes perforées est encodée mathématiquement pour refléter le sous-problème de l'Étape 1.

#### Étape 3 : Résoudre le problème original en utilisant les Étapes 1 et 2.

Dans l'Étape 1, nous avons écrit le sous-problème pour le problème des cartes perforées en mots. Dans l'Étape 2, nous avons écrit une décision mathématique récurrente qui correspond à ces sous-problèmes. Comment pouvons-nous résoudre le problème original avec ces informations ?

```
OPT(1)
```

C'est aussi simple que cela. Puisque le sous-problème que nous avons trouvé dans l'Étape 1 est l'horaire de valeur maximale pour les cartes perforées *i* à *n* tel que les cartes perforées sont triées par temps de début, nous pouvons écrire la solution au problème original comme l'horaire de valeur maximale pour les cartes perforées 1 à *n* tel que les cartes perforées sont triées par temps de début. Puisque les Étapes 1 et 2 vont de pair, le problème original peut également s'écrire comme OPT(1).

#### Étape 4 : Déterminer les dimensions du tableau de mémoïsation et la direction dans laquelle il doit être rempli.

Avez-vous trouvé l'Étape 3 trompeusement simple ? Cela semble être le cas. Vous pensez peut-être, comment OPT(1) peut-il être la solution à notre programme dynamique s'il dépend de OPT(2), OPT(next[1]), et ainsi de suite ?

Vous avez raison de remarquer que OPT(1) dépend de la solution à OPT(2). Cela découle directement de l'Étape 2 :

```
OPT(1) = max(v_1 + OPT(next[1]), OPT(2))
```

Mais ce n'est pas un problème écrasant. Reprenons l'exemple de mémoïsation de Fibonacci. Pour trouver la valeur de Fibonacci pour *n* = 5, l'algorithme dépend du fait que les valeurs de Fibonacci pour *n* = 4, *n* = 3, *n* = 2, *n* = 1, et *n* = 0 ont déjà été mémoïsées. Si nous remplissons notre tableau de mémoïsation dans le bon ordre, la dépendance de OPT(1) à d'autres sous-problèmes n'est pas un gros problème.

Comment pouvons-nous identifier la bonne direction pour remplir le tableau de mémoïsation ? Dans le problème des cartes perforées, puisque nous savons que OPT(1) dépend des solutions à OPT(2) et OPT(next[1]), et que les cartes perforées 2 et next[1] ont des temps de début après la carte perforée 1 en raison du tri, nous pouvons déduire que nous devons remplir notre tableau de mémoïsation de OPT(*n*) à OPT(1).

Comment déterminons-nous les dimensions de ce tableau de mémoïsation ? Voici un truc : les dimensions du tableau sont égales au nombre et à la taille des variables sur lesquelles OPT(•) dépend. Dans le problème des cartes perforées, nous avons OPT(*i*), ce qui signifie que OPT(•) ne dépend que de la variable *i*, qui représente le numéro de la carte perforée. Cela suggère que notre tableau de mémoïsation sera unidimensionnel et que sa taille sera *n* puisque il y a *n* cartes perforées au total.

Si nous savons que *n* = 5, alors notre tableau de mémoïsation pourrait ressembler à ceci :

```
memo = [OPT(1), OPT(2), OPT(3), OPT(4), OPT(5)]
```

Cependant, parce que de nombreux langages de programmation [commencent l'indexation des tableaux à 0](https://en.wikipedia.org/wiki/Zero-based_numbering), il peut être plus pratique de créer ce tableau de mémoïsation de sorte que ses indices s'alignent avec les numéros de cartes perforées :

```
memo = [0, OPT(1), OPT(2), OPT(3), OPT(4), OPT(5)]
```

#### Étape 5 : Codez-le !

Pour coder notre programme dynamique, nous assemblons les Étapes 2–4. La seule nouvelle information dont vous aurez besoin pour écrire un programme dynamique est un cas de base, que vous pouvez trouver en bidouillant avec votre algorithme.

Un programme dynamique pour le problème des cartes perforées ressemblera à ceci :

```
def punchcardSchedule(n, values, next): # Initialiser le tableau de mémoïsation - Étape 4  memo = [0] * (n+1)   # Définir le cas de base  memo[n] = values[n]   # Construire le tableau de mémoïsation de n à 1 - Étape 2  for i in range(n-1, 0, -1):    memo[i] = max(v_i + memo[next[i]], memo[i+1])  # Retourner la solution au problème original OPT(1) - Étape 3  return memo[1]
```

Félicitations pour avoir écrit votre premier programme dynamique ! Maintenant que vous avez mouillé vos pieds, je vais vous guider à travers un type différent de programme dynamique.

### Paradoxe du choix : Exemple de DP à options multiples

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZOy2VkYyok5a5YoBEUGMtg.jpeg)
*Sans rapport avec la DP, mais une représentation exacte de la façon dont les décisions à plusieurs options peuvent être harcelantes.*

Bien que l'exemple précédent de programmation dynamique avait une décision à deux options — exécuter ou ne pas exécuter une carte perforée — certains problèmes nécessitent que plusieurs options soient considérées avant qu'une décision puisse être prise à chaque étape.

Il est temps pour un nouvel exemple.

Imaginez que vous vendez des bracelets d'amitié à *n* clients, et la valeur de ce produit augmente de manière monotone. Cela signifie que le produit a des prix {*p*1, ..., *p_n*} tels que *p_i ≤ p_j* si le client *j* vient après le client *i*. Ces *n* clients ont des valeurs {*v*1, ..., *v_n*}. Un client donné *i* achètera un bracelet d'amitié au prix *p_i* si et seulement si *p_i ≤ v_i* ; sinon, le revenu obtenu de ce client est 0. Supposons que les prix sont des nombres naturels.

**Problème** : Vous devez trouver l'ensemble de prix qui vous garantit le revenu maximum possible de la vente de vos bracelets d'amitié.

Prenez un moment pour réfléchir à la manière dont vous pourriez aborder ce problème avant de regarder mes solutions aux Étapes 1 et 2.

#### Étape 1 : Identifier le sous-problème en mots.

**Sous-problème** : Le revenu maximum obtenu des clients *i* à *n* tel que le prix pour le client *i-1* était fixé à *q*.

J'ai trouvé ce sous-problème en réalisant que pour déterminer le revenu maximum pour les clients 1 à *n*, je devrais trouver la réponse aux sous-problèmes suivants :

* Le revenu maximum obtenu des clients *n-1* à *n* tel que le prix pour le client *n-2* était fixé à *q*.
* Le revenu maximum obtenu des clients *n-2* à *n* tel que le prix pour le client *n-3* était fixé à *q*.
* (Et ainsi de suite)

Remarquez que j'ai introduit une seconde variable *q* dans le sous-problème. Je l'ai fait parce que, afin de résoudre chaque sous-problème, j'ai besoin de connaître le prix que j'ai fixé pour le client *avant* ce sous-problème. La variable *q* assure la nature monotone de l'ensemble des prix, et la variable *i* suit le client actuel.

#### Étape 2 : Écrire le sous-problème comme une décision mathématique récurrente.

Il y a deux questions que je me pose chaque fois que j'essaie de trouver une récurrence :

* Quelle décision prends-je à chaque étape ?
* Si mon algorithme est à l'étape *i*, quelles informations aurait-il besoin pour décider quoi faire à l'étape *i+1* ? (Et parfois : Si mon algorithme est à l'étape *i*, quelles informations aurait-il besoin pour décider quoi faire à l'étape *i-1* ?)

Revenons au problème des bracelets d'amitié et posons ces questions.

**Quelle décision prends-je à chaque étape ?** Je décide à quel prix vendre mon bracelet d'amitié au client actuel. Puisque les prix doivent être des nombres naturels, je sais que je devrais fixer mon prix pour le client *i* dans la plage de *q* — le prix fixé pour le client *i-1* — à *v_i* — le prix maximum auquel le client *i* achètera un bracelet d'amitié.

**Si mon algorithme est à l'étape** **_i_, quelles informations aurait-il besoin pour décider quoi faire à l'étape** **_i+1_?** Mon algorithme doit connaître le prix fixé pour le client *i* et la valeur du client *i+1* afin de décider à quel nombre naturel fixer le prix pour le client *i+1*.

Avec cette connaissance, je peux écrire mathématiquement la récurrence :

```
OPT(i,q) = max~([Revenue(v_i, a) + OPT(i+1, a)])
```

```
tel que max~ trouve le maximum sur tous les a dans la plage q ≤ a ≤ v_i
```

Une fois de plus, cette récurrence mathématique nécessite quelques explications. Puisque le prix pour le client *i-1* est *q*, pour le client *i*, le prix *a* reste soit à l'entier *q* soit il change pour être un entier entre *q+1* et *v_i*. Pour trouver le revenu total, nous ajoutons le revenu du client *i* au revenu maximum obtenu des clients *i+1* à *n* tel que le prix pour le client *i* était fixé à *a*.

En d'autres termes, pour maximiser le revenu total, l'algorithme doit trouver le prix optimal pour le client *i* en vérifiant tous les prix possibles entre *q* et *v_i*. Si *v_i ≤ q*, alors le prix *a* doit rester à *q*.

#### Et les autres étapes ?

Travailler à travers les Étapes 1 et 2 est la partie la plus difficile de la programmation dynamique. En tant qu'exercice, je suggère que vous travailliez à travers les Étapes 3, 4, et 5 par vous-même pour vérifier votre compréhension.

### Analyse du temps d'exécution des programmes dynamiques

Maintenant, la partie amusante de l'écriture des algorithmes : l'analyse du temps d'exécution. J'utiliserai la notation big-O tout au long de cette discussion. Si vous n'êtes pas encore familier avec le big-O, je vous suggère de vous renseigner à ce sujet [ici](https://www.interviewcake.com/article/java/big-o-notation-time-and-space-complexity).

Généralement, le temps d'exécution d'un programme dynamique est composé des caractéristiques suivantes :

* Pré-traitement
* Combien de fois la boucle for s'exécute
* Combien de temps il faut à la récurrence pour s'exécuter en une itération de la boucle for
* Post-traitement

Globalement, le temps d'exécution prend la forme suivante :

```
Pré-traitement + Boucle * Récurrence + Post-traitement
```

Effectuons une analyse du temps d'exécution du problème des cartes perforées pour nous familiariser avec le big-O pour les programmes dynamiques. Voici le programme dynamique du problème des cartes perforées :

```
def punchcardSchedule(n, values, next): # Initialiser le tableau de mémoïsation - Étape 4  memo = [0] * (n+1)   # Définir le cas de base  memo[n] = values[n]   # Construire le tableau de mémoïsation de n à 1 - Étape 2  for i in range(n-1, 0, -1):    memo[i] = max(v_i + memo[next[i]], memo[i+1])  # Retourner la solution au problème original OPT(1) - Étape 3  return memo[1]
```

Décomposons son temps d'exécution :

* Pré-traitement : Ici, cela signifie construire le tableau de mémoïsation. O(*n*).
* Combien de fois la boucle for s'exécute : O(*n*).
* Combien de temps il faut à la récurrence pour s'exécuter en une itération de la boucle for : La récurrence prend un temps constant pour s'exécuter car elle fait un choix entre deux options à chaque itération. O(1).
* Post-traitement : Aucun ici ! O(1).

Le temps d'exécution global du programme dynamique du problème des cartes perforées est O(*n*) O(*n*) * O(1) + O(1), ou, sous forme simplifiée, O(*n*).

### Vous l'avez fait !

Eh bien, c'est tout — vous êtes un pas de plus vers devenir un magicien de la programmation dynamique !

![Image](https://cdn-media-1.freecodecamp.org/images/1*iFMwuyC5ym3f_Ep6L_GEEA.jpeg)
*Margaret Hamilton : l'une des nombreuses magiciennes de la programmation dans notre histoire !*

Un dernier conseil : **continuez à pratiquer la programmation dynamique**. Peu importe à quel point ces algorithmes peuvent sembler frustrants, écrire répétitivement des programmes dynamiques fera venir les sous-problèmes et les récurrences plus naturellement. Voici une liste crowdsourcée de [problèmes classiques de programmation dynamique](https://www.quora.com/What-are-the-top-10-most-popular-dynamic-programming-problems-among-interviewers) pour que vous puissiez essayer.

Alors, sortez et prenez vos entretiens, vos cours, et votre **vie** (bien sûr) avec vos nouvelles connaissances en programmation dynamique !

Un grand merci à [Steven Bennett](https://stebenn.wordpress.com/), [Claire Durand](https://medium.com/@eeclaire), et [Prithaj Nath](https://medium.com/@prithajnath) pour la relecture de cet article. Merci à [Professeur Hartline](https://sites.northwestern.edu/hartline/) pour m'avoir tant excité à propos de la programmation dynamique que j'en ai écrit longuement.

Vous avez aimé ce que vous avez lu ? Partagez l'amour en aimant et en partageant cet article. Vous avez des pensées ou des questions ? Contactez-moi sur [Twitter](https://twitter.com/alainakafkes) ou dans les commentaires ci-dessous.