---
title: Une plongée approfondie dans l'étiquetage grammatical en utilisant l'algorithme
  de Viterbi
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-08T19:05:31.000Z'
originalURL: https://freecodecamp.org/news/a-deep-dive-into-part-of-speech-tagging-using-viterbi-algorithm-17c8de32e8bc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*x-5ZBtUvlD78BOMuMnMAbg.png
tags:
- name: algorithms
  slug: algorithms
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une plongée approfondie dans l'étiquetage grammatical en utilisant l'algorithme
  de Viterbi
seo_desc: 'By Sachin Malhotra

  by Sachin Malhotra and Divya Godayal


  _Source: [https://www.vocal.com/echo-cancellation/viterbi-algorithm-in-speech-enhancement-and-hmm/](https://www.vocal.com/echo-cancellation/viterbi-algorithm-in-speech-enhancement-and-hmm/"
  rel...'
---

Par Sachin Malhotra

_par [Sachin Malhotra](https://medium.com/@sachinmalhotra) et [Divya Godayal](https://medium.com/@divyagodayal)_

![Image](https://cdn-media-1.freecodecamp.org/images/0xW2T6PJWIqsqxhx40O2lZICrr5nUZR51wdt)
_Source : [https://www.vocal.com/echo-cancellation/viterbi-algorithm-in-speech-enhancement-and-hmm/](https://www.vocal.com/echo-cancellation/viterbi-algorithm-in-speech-enhancement-and-hmm/" rel="noopener" target="_blank" title=")_

Bienvenue à nouveau, Gardien !

Au cas où vous auriez oublié le [problème](https://medium.freecodecamp.org/an-introduction-to-part-of-speech-tagging-and-the-hidden-markov-model-953d45338f24) que nous essayions de résoudre dans l'article précédent, laissez-nous le réviser pour vous.

Il y a donc cet enfant turbulent Peter et il va importuner son nouveau gardien, vous !

En tant que gardien, l'une des tâches les plus importantes pour vous est de border Peter dans son lit et de vous assurer qu'il est profondément endormi. Une fois que vous l'avez bordé, vous voulez vous assurer qu'il est réellement endormi et non en train de faire des bêtises.

Vous ne pouvez cependant pas entrer à nouveau dans la pièce, car cela réveillerait sûrement Peter. Tout ce que vous pouvez entendre, ce sont les bruits qui pourraient provenir de la pièce.

Soit la pièce est **silencieuse**, soit il y a du **bruit** provenant de la pièce. Ce sont vos observations.

Tout ce que vous avez en tant que gardien, ce sont :

* un ensemble d'observations, qui est essentiellement une séquence contenant **bruit** ou **silence** au fil du temps, et
* Un diagramme d'état fourni par la mère de Peter — qui se trouve être une scientifique en neurologie — qui contient tous les différents ensembles de probabilités que vous pouvez utiliser pour résoudre le problème défini ci-dessous.

### Le problème

Étant donné le diagramme d'état et une séquence de N observations au fil du temps, nous devons indiquer l'état du bébé à l'instant actuel. Mathématiquement, nous avons N observations aux instants `t0, t1, t2 .... tN`. Nous voulons savoir si Peter serait éveillé ou endormi, ou plutôt quel état est le plus probable à l'instant `tN+1`.

Au cas où tout cela vous semblerait du grec, lisez l'[article précédent](https://medium.com/@divyagodayal/part-of-speech-tagging-hmms-part-1-953d45338f24) pour vous rafraîchir la mémoire sur le modèle de chaîne de Markov, les modèles de Markov cachés et l'étiquetage grammatical.

![Image](https://cdn-media-1.freecodecamp.org/images/RIOlv0lcV03Ol30xkYD-rr0vbLMrMEdJreAe)
_Le diagramme d'état que la mère de Peter vous a donné avant de partir._

Dans cet [article précédent](https://medium.com/@divyagodayal/part-of-speech-tagging-hmms-part-1-953d45338f24), nous avions brièvement modélisé le problème de l'étiquetage grammatical en utilisant le modèle de Markov caché.

Le problème de savoir si Peter est endormi ou non est simplement un exemple de problème pris pour une meilleure compréhension de certains des concepts clés impliqués dans ces deux articles. Au cœur, les articles traitent de la résolution du problème de l'étiquetage grammatical en utilisant les modèles de Markov cachés.

Alors, avant de passer à l'**algorithme de Viterbi**, regardons d'abord une explication beaucoup plus détaillée de la manière dont le problème d'étiquetage peut être modélisé en utilisant les HMM.

### Modèles génératifs et le modèle de canal bruyant

Beaucoup de problèmes en traitement automatique du langage naturel sont résolus en utilisant une approche d'apprentissage supervisé.

Les problèmes supervisés en apprentissage automatique sont définis comme suit. Nous supposons des exemples d'entraînement `(x(1), y(1))`. . .`(x(m) , y(m))`, où chaque exemple se compose d'une entrée x(i) associée à une étiquette y(i). Nous utilisons X pour désigner l'ensemble des entrées possibles, et Y pour désigner l'ensemble des étiquettes possibles. Notre tâche est d'apprendre une fonction f : X → Y qui mappe toute entrée x à une étiquette f(x).

Dans les problèmes d'étiquetage, chaque x(i) serait une séquence de mots `X1 X2 X3 …. Xn(i)`, et chaque y(i) serait une séquence d'étiquettes `Y1 Y2 Y3 … Yn(i)` (nous utilisons n(i) pour désigner la longueur du i-ème exemple d'entraînement). X désignerait l'ensemble de toutes les séquences x1 . . . xn, et Y serait l'ensemble de toutes les séquences d'étiquettes y1 . . . yn. Notre tâche serait d'apprendre une fonction f : X → Y qui mappe les phrases aux séquences d'étiquettes.

Une approche intuitive pour obtenir une estimation de ce problème est d'utiliser les probabilités conditionnelles. `p(y | x)` qui est la probabilité de l'entrée y étant donné une entrée x. Les paramètres du modèle seraient estimés en utilisant les échantillons d'entraînement. Enfin, étant donné une entrée inconnue `x`, nous aimerions trouver

`f(x) = arg max(p(y | x)) ∀y ∈ Y`

Ceci est le modèle conditionnel pour résoudre ce problème générique étant donné les données d'entraînement. Une autre approche qui est principalement adoptée en apprentissage automatique et en traitement automatique du langage naturel est d'utiliser un **modèle génératif**.

Plutôt que d'estimer directement la distribution conditionnelle `p(y|x)`, dans les modèles génératifs, nous modélisons plutôt la probabilité conjointe `p(x, y)` sur toutes les paires (x, y).

Nous pouvons décomposer davantage la probabilité conjointe en valeurs plus simples en utilisant la règle de Bayes :

![Image](https://cdn-media-1.freecodecamp.org/images/YPoMzlM9CMykbU3qcdwDXf9yPpO43F7zl2Yc)

* `p(y)` est la probabilité a priori de toute entrée appartenant à l'étiquette y.
* `p(x | y)` est la probabilité conditionnelle de l'entrée x étant donné l'étiquette y.

Nous pouvons utiliser cette décomposition et la règle de Bayes pour déterminer la probabilité conditionnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/FIHhUBpd1JM7OxMMP6A20Vpipi8hJVIwOhOn)

Rappelons que nous voulions estimer la fonction

```
f(x) = arg max( p(y|x) ) ∀y ∈ Y
```

```
f(x) = arg max( p(y) * p(x | y) )
```

La raison pour laquelle nous avons ignoré le dénominateur ici est que la probabilité `p(x)` reste la même quelle que soit l'étiquette de sortie considérée. Et donc, d'un point de vue computationnel, elle est traitée comme une **constante de normalisation et est normalement ignorée.**

Les modèles qui décomposent une probabilité conjointe en termes `p(y)` et `p(x|y)` sont souvent appelés **modèles de canal bruyant**. Intuitivement, lorsque nous voyons un exemple de test x, nous supposons qu'il a été généré en deux étapes :

1. d'abord, une étiquette y a été choisie avec une probabilité p(y)
2. ensuite, l'exemple x a été généré à partir de la distribution p(x|y). Le modèle p(x|y) peut être interprété comme un **"canal"** qui prend une étiquette y comme entrée, et la corrompt pour produire x comme sortie.

### Modèle génératif d'étiquetage grammatical

Supposons un ensemble fini de mots V et une séquence finie d'étiquettes K. Alors l'ensemble S sera l'ensemble de toutes les séquences, paires d'étiquettes `<x1, x2, x3 ... xn, y1, y2, y3, ...,` yn> telles que `n >` 0 ∀x ∈ V et ∀y ∈ K.

Un modèle génératif d'étiquetage est alors celui où

![Image](https://cdn-media-1.freecodecamp.org/images/baWhcBHFiwW1aPtPwNpMeM7PdxYfxIL9jBkF)

2.

![Image](https://cdn-media-1.freecodecamp.org/images/oDp5BDuHy8wCkLUiGoEATp9TsM9yCda0GbQy)

Étant donné un modèle génératif d'étiquetage, la fonction dont nous avons parlé précédemment de l'entrée à la sortie devient

![Image](https://cdn-media-1.freecodecamp.org/images/hmF3FST1pwqbP5a3lRI9mTsIZOH-5ilqgMv8)

Ainsi, pour toute séquence d'entrée de mots donnée, la sortie est la séquence d'étiquettes de probabilité la plus élevée du modèle. Ayant défini le modèle génératif, nous devons déterminer trois choses différentes :

1. Comment définissons-nous exactement la probabilité du modèle génératif `p(<x1, x2, x3 ... xn, y1, y2, y3, ..., y`n>)
2. Comment estimons-nous les paramètres du modèle, et
3. Comment calculons-nous efficacement

![Image](https://cdn-media-1.freecodecamp.org/images/uHq7WaF9wQkNmagfOqC2SM-S0dLGpJDCkC0X)

Regardons comment nous pouvons répondre à ces trois questions côte à côte, une fois pour notre problème d'exemple et ensuite pour le problème réel en question : l'étiquetage grammatical.

### Définition du modèle génératif

Regardons d'abord comment nous pouvons estimer la probabilité `p(x1 .. xn, y1 .. yn)` en utilisant le HMM.

Nous pouvons avoir n'importe quel HMM N-gramme qui considère les événements dans la fenêtre précédente de taille N.

Les formules fournies ci-après correspondent à un modèle de Markov caché **Trigramme**.

#### Modèle de Markov caché Trigramme

Un modèle de Markov caché trigramme peut être défini en utilisant

* Un ensemble fini d'états.
* Une séquence d'observations.
* q(s|u, v)  
**Probabilité de transition** définie comme la probabilité qu'un état "s" apparaisse juste après avoir observé "u" et "v" dans la séquence d'observations.
* e(x|s)  
**Probabilité d'émission** définie comme la probabilité de faire une observation x étant donné que l'état était s.

Alors, la probabilité du modèle génératif serait estimée comme

![Image](https://cdn-media-1.freecodecamp.org/images/QXdufboQ1sB0ZSP3vta1yiteOpT47xDCy6xf)

En ce qui concerne le problème du sommeil du bébé que nous considérons, nous n'aurons que deux états possibles : soit le bébé est éveillé, soit il est endormi. Le gardien ne peut faire que deux observations au fil du temps. Soit il y a du bruit provenant de la pièce, soit la pièce est absolument silencieuse. La séquence des observations et des états peut être représentée comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/hRYCLfJnsmLORhZSejKBvp6lzz5AoAepQuNu)
_Observations et états au fil du temps pour le problème du sommeil du bébé_

En ce qui concerne le problème de l'étiquetage grammatical, les états seraient représentés par les étiquettes réelles attribuées aux mots. Les mots seraient nos observations. La raison pour laquelle nous disons que les étiquettes sont nos états est que dans un modèle de Markov caché, les états sont toujours cachés et tout ce que nous avons, c'est l'ensemble des observations qui sont visibles pour nous. De la même manière, la séquence des états et des observations pour le problème de l'étiquetage grammatical serait

![Image](https://cdn-media-1.freecodecamp.org/images/35SQfert2ZVmpA4biNBYbdh18x1E8CaxpfYI)
_Observations et états au fil du temps pour le problème de l'étiquetage grammatical_

### Estimation des paramètres du modèle

Nous supposerons que nous avons accès à certaines données d'entraînement. Les données d'entraînement consistent en un ensemble d'exemples où chaque exemple est une séquence composée d'observations, chaque observation étant associée à un état. Étant donné ces données, comment estimons-nous les paramètres du modèle ?

L'estimation des paramètres du modèle est effectuée en lisant divers comptes à partir du corpus d'entraînement que nous avons, puis en calculant les estimations de probabilité maximale :

![Image](https://cdn-media-1.freecodecamp.org/images/c9IK15ggYYCC2jj7xqv49szM4T9z865wOYZW)
_Probabilité de transition et probabilité d'émission pour un HMM Trigramme_

Nous savons déjà que le premier terme représente la probabilité de transition et le deuxième terme représente la probabilité d'émission. Regardons ce que signifient les quatre comptes différents dans les termes ci-dessus.

1. **c(u, v, s)** représente le compte trigramme des états u, v et s. Cela signifie qu'il représente le nombre de fois où les trois états u, v et s sont apparus ensemble dans cet ordre dans le corpus d'entraînement.
2. **c(u, v)** suivant les mêmes lignes que celles du compte trigramme, il s'agit du compte bigramme des états u et v étant donné le corpus d'entraînement.
3. **c(s → x)** est le nombre de fois dans l'ensemble d'entraînement où l'état s et l'observation x sont appariés ensemble. Et enfin,
4. **c(s)** est la probabilité a priori qu'une observation soit étiquetée comme l'état s.

Regardons un ensemble d'entraînement d'exemple pour le problème jouet d'abord et voyons les calculs pour les probabilités de transition et d'émission en utilisant le même.

Les marquages BLEUS représentent la probabilité de transition, et ROUGE est pour les calculs de probabilité d'émission.

Notez que puisque le problème d'exemple n'a que deux états distincts et deux observations distinctes, et étant donné que l'ensemble d'entraînement est très petit, les calculs montrés ci-dessous pour le problème d'exemple utilisent un HMM **bigramme** au lieu d'un HMM trigramme.

La mère de Peter tenait un registre des observations et des états. Et ainsi, elle vous a même fourni un corpus d'entraînement pour vous aider à obtenir les probabilités de transition et d'émission.

#### Exemple de probabilité de transition :

![Image](https://cdn-media-1.freecodecamp.org/images/RKqKpVSWRASp7UFYpk7Bp6pKnJGbK5gEpFCB)
_Corpus d'entraînement_

![Image](https://cdn-media-1.freecodecamp.org/images/gs1MZiI98zSRoppmv3Qt4adg7QSLaHZhxO7b)
_Calculs pour Awake apparaissant après Awake_

#### Exemple de probabilité d'émission :

![Image](https://cdn-media-1.freecodecamp.org/images/AptxqtG6x4IV6wvGhVjoYNIkT51zcFq85TYL)
_Corpus d'entraînement_

![Image](https://cdn-media-1.freecodecamp.org/images/Aa3DVOy0-gbjaMqMRiBPUvOr5LOg3gDjX45J)
_Calculs pour observer 'Quiet' lorsque l'état est 'Awake'_

C'était assez simple, puisque l'ensemble d'entraînement était très petit. Regardons un ensemble d'entraînement d'exemple pour notre problème réel d'étiquetage grammatical. Ici, nous pouvons considérer un HMM trigramme, et nous montrerons les calculs en conséquence.

Nous utiliserons les phrases suivantes comme corpus de données d'entraînement (la notation mot/TAG signifie mot étiqueté avec une étiquette spécifique de partie du discours).

![Image](https://cdn-media-1.freecodecamp.org/images/fjB8BXYUF0A3PMGLF1Hwt2E4ueO0VwLfhea8)

L'ensemble d'entraînement que nous avons est un corpus étiqueté de phrases. Chaque phrase se compose de mots étiquetés avec leurs étiquettes de partie du discours correspondantes. Par exemple : eat/VB signifie que le mot est "eat" et l'étiquette de partie du discours dans cette phrase dans ce contexte très précis est "VB" c'est-à-dire Phrase Verbale. Regardons un exemple de calcul pour la probabilité de transition et la probabilité d'émission comme nous l'avons vu pour le problème du sommeil du bébé.

#### **Probabilité de transition**

Supposons que nous voulons calculer la probabilité de transition q(IN | VB, NN). Pour cela, nous voyons combien de fois nous voyons un trigramme (VB,NN,IN) dans le corpus d'entraînement dans cet ordre spécifique. Nous le divisons ensuite par le nombre total de fois où nous voyons le bigramme (VB,NN) dans le corpus.

#### **Probabilité d'émission**

Supposons que nous voulons trouver la probabilité d'émission e(an | DT). Pour cela, nous voyons combien de fois le mot "an" est étiqueté comme "DT" dans le corpus et nous le divisons par le nombre total de fois où nous voyons l'étiquette "DT" dans le corpus.

![Image](https://cdn-media-1.freecodecamp.org/images/wcnkQ4ipbUSMdUueW30dPf9i5KO-MNz5O4Ka)

Ainsi, si vous regardez ces calculs, cela montre que le calcul des paramètres du modèle n'est pas coûteux en termes de calcul. C'est-à-dire que nous n'avons pas à faire plusieurs passes sur les données d'entraînement pour calculer ces paramètres. Tout ce dont nous avons besoin, c'est d'un ensemble de comptes différents, et une seule passe sur le corpus d'entraînement devrait nous fournir cela.

Passons à l'étape finale que nous devons examiner étant donné un modèle génératif. Cette étape consiste à calculer efficacement

![Image](https://cdn-media-1.freecodecamp.org/images/L5g6txDpMnwxRtLNPdYQpVdLSHr6wqX1Sa1l)

Nous allons examiner le célèbre algorithme de Viterbi pour ce calcul.

### Trouver la séquence la plus probable — Algorithme de Viterbi

Enfin, nous allons résoudre le problème de trouver la séquence d'étiquettes la plus probable étant donné un ensemble d'observations x1 … xn. C'est-à-dire que nous devons trouver

![Image](https://cdn-media-1.freecodecamp.org/images/FTsxJ83x3QI1X94coodh0ADunrNpdYMBX4rS)

La probabilité ici est exprimée en termes de probabilités de transition et d'émission que nous avons appris à calculer dans la section précédente de l'article. Juste pour vous rappeler, la formule pour la probabilité d'une séquence d'étiquettes étant donné une séquence d'observations sur "n" étapes de temps est

![Image](https://cdn-media-1.freecodecamp.org/images/-tn5T49bhdb4TugyAO4mwO3t1Wx3KlqWgF6T)

Avant de regarder un algorithme optimisé pour résoudre ce problème, regardons d'abord une approche simple de force brute pour ce problème. Essentiellement, nous devons trouver la séquence d'étiquettes la plus probable étant donné un ensemble d'observations parmi un ensemble fini de séquences possibles d'étiquettes. Regardons le nombre total possible de séquences pour un petit exemple pour notre problème d'exemple et aussi pour un problème d'étiquetage grammatical.

Supposons que nous avons l'ensemble suivant d'observations pour le problème d'exemple.

```
Noise     Quiet     Noise
```

Nous avons deux étiquettes possibles {Asleep et Awake}. Certaines des séquences possibles d'étiquettes pour les observations ci-dessus sont :

```
Awake      Awake     Awake
```

```
Awake      Awake     Asleep
```

```
Awake      Asleep    Awake
```

```
Awake      Asleep    Asleep
```

Au total, nous pouvons avoir 2³ = 8 séquences possibles. Cela peut ne pas sembler beaucoup, mais si nous augmentons le nombre d'observations au fil du temps, le nombre de séquences augmenterait exponentiellement. C'est le cas lorsque nous n'avions que deux étiquettes possibles. Et si nous en avions plus ? Comme c'est le cas avec l'étiquetage grammatical.

Par exemple, considérons la phrase

```
the dog barks
```

et en supposant que l'ensemble des étiquettes possibles est {D, N, V}, regardons certaines des séquences d'étiquettes possibles :

```
D     D     DD     D     ND     D     VD     N     DD     N     ND     N     V ... etc
```

Ici, nous aurions 3³ = 27 séquences d'étiquettes possibles. Et comme vous pouvez le voir, la phrase était extrêmement courte et le nombre d'étiquettes n'était pas très élevé. En pratique, nous pouvons avoir des phrases qui pourraient être beaucoup plus longues que trois mots. Ensuite, le nombre d'étiquettes uniques à notre disposition serait également trop élevé pour suivre cette approche d'énumération et trouver la meilleure séquence d'étiquettes possible de cette manière.

Ainsi, la croissance exponentielle du nombre de séquences implique que pour toute phrase de longueur raisonnable, l'approche de force brute ne fonctionnerait pas car elle prendrait trop de temps à s'exécuter.

Au lieu de cette approche de force brute, nous allons voir que nous pouvons trouver la séquence d'étiquettes la plus probable de manière efficace en utilisant un algorithme de programmation dynamique connu sous le nom d'**algorithme de Viterbi**.

Définissons d'abord quelques termes qui seraient utiles pour définir l'algorithme lui-même. Nous savons déjà que la probabilité d'une séquence d'étiquettes étant donné un ensemble d'observations peut être définie en termes de probabilité de transition et de probabilité d'émission. Mathématiquement, c'est

![Image](https://cdn-media-1.freecodecamp.org/images/XLJtbWQh3n77eqrPauYh9Mme1rSGcXpukUc6)

Regardons une version tronquée de celle-ci qui est

![Image](https://cdn-media-1.freecodecamp.org/images/Df1ie2E2jxAmM38UZ7UrartTKLYjfOcPXHcS)

et appelons cela le coût d'une séquence de longueur k.

Ainsi, la définition de "r" consiste simplement à considérer les k premiers termes de la définition de la probabilité où k ∈ {1..n} et pour toute séquence d'étiquettes y1…yk.

Ensuite, nous avons l'ensemble S(k, u, v) qui est essentiellement l'ensemble de toutes les séquences d'étiquettes de longueur k qui se terminent par le bigramme (u, v) c'est-à-dire

![Image](https://cdn-media-1.freecodecamp.org/images/HOOiuLM6Cyf0eesIiJjBzo1uNbCcxLjLAsqU)

Enfin, nous définissons le terme π(k, u, v) qui est essentiellement la séquence avec le coût maximum.

![Image](https://cdn-media-1.freecodecamp.org/images/L4CHoJ6epH9hjOrvEzbN3SpyCcudEkdnHlE6)

L'idée principale derrière l'algorithme de Viterbi est que nous pouvons calculer les valeurs du terme π(k, u, v) de manière efficace, récursive et mémoisée. Afin de définir l'algorithme de manière récursive, regardons les cas de base pour la récursion.

```
π(0, *, *) = 1
```

```
π(0, u, v) = 0
```

Puisque nous considérons un HMM trigramme, nous considérerions tous les trigrams dans le cadre de l'exécution de l'algorithme de Viterbi.

Maintenant, nous pouvons commencer la première fenêtre trigramme à partir des trois premiers mots de la phrase, mais alors le modèle manquerait ces trigrams où le premier mot ou les deux premiers mots se produisent indépendamment. Pour cette raison, nous considérons deux symboles de départ spéciaux comme `*` et ainsi notre phrase devient

```
*    *    x1   x2   x3   ......         xn
```

Et le premier trigramme que nous considérons serait alors (*, *, x1) et le deuxième serait (*, x1, x2).

Maintenant que nous avons tous nos termes en place, nous pouvons enfin regarder la définition récursive de l'algorithme qui est essentiellement le cœur de l'algorithme.

![Image](https://cdn-media-1.freecodecamp.org/images/1onixt5VxC32oTxrUAF9MklN61N79VXLrfuL)

Cette définition est clairement récursive, car nous essayons de calculer un terme π et nous utilisons un autre avec une valeur inférieure de k dans la relation de récurrence pour celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/RNHTlxO-aqNvguCPosqS0pkGoS1M1gA12iKy)

Chaque séquence se terminerait par un symbole spécial STOP. Pour le modèle trigramme, nous aurions également deux symboles de départ spéciaux "*" au début.

Jetez un coup d'œil au pseudo-code de l'algorithme entier.

![Image](https://cdn-media-1.freecodecamp.org/images/7I6yqBEAw6BHPUbVMoT3ReqTFNQWjeAzw2rT)

L'algorithme remplit d'abord les valeurs π(k, u, v) en utilisant la définition récursive. Il utilise ensuite l'identité décrite précédemment pour calculer la probabilité la plus élevée pour toute séquence.

Le temps d'exécution de l'algorithme est O(n|K|³), il est donc linéaire en fonction de la longueur de la séquence, et cubique en fonction du nombre d'étiquettes.

NOTE : Nous montrerons les calculs pour le problème du sommeil du bébé et le problème de l'étiquetage grammatical basé sur un **HMM bigramme uniquement**. Les calculs pour le trigramme sont laissés au lecteur. Mais le code qui est joint à la fin de cet article est basé sur un HMM trigramme. Il est simplement plus facile d'expliquer et de représenter les calculs pour l'algorithme de Viterbi lorsque l'on considère un HMM bigramme au lieu d'un HMM trigramme.

Par conséquent, avant de montrer les calculs pour l'algorithme de Viterbi, regardons la formule récursive basée sur un HMM bigramme.

![Image](https://cdn-media-1.freecodecamp.org/images/8oFED1zwh-vesv886QdRAf6OJPjpXHFED80v)

Celui-ci est extrêmement similaire à celui que nous avons vu précédemment pour le modèle trigramme, sauf que maintenant nous ne nous préoccupons que de l'étiquette actuelle et de celle précédente, au lieu des deux précédentes. La complexité de l'algorithme devient maintenant O(n|K|²).

#### Calculs pour le problème du sommeil du bébé

Maintenant que nous avons la formule récursive prête pour l'algorithme de Viterbi, voyons un exemple de calcul de celui-ci d'abord pour le problème d'exemple que nous avions, c'est-à-dire le problème du sommeil du bébé, puis pour la version d'étiquetage grammatical.

Notez que lorsque nous sommes à cette étape, c'est-à-dire les calculs pour l'algorithme de Viterbi pour trouver la séquence d'étiquettes la plus probable étant donné un ensemble d'observations sur une série d'étapes de temps, nous supposons que les probabilités de transition et d'émission ont déjà été calculées à partir du corpus donné. Jetons un coup d'œil à un échantillon de probabilités de transition et d'émission pour le problème du sommeil du bébé que nous utiliserions pour nos calculs de l'algorithme.

![Image](https://cdn-media-1.freecodecamp.org/images/rdYzTQzvmJsm-7XqqYuuOWsWk4eV-Y7ZdLD3)

Le bébé commence par être éveillé et reste dans la pièce pendant trois points de temps, t1 . . . t3 (trois itérations de la chaîne de Markov). Les observations sont : silence, silence, bruit. Jetez un coup d'œil au diagramme suivant qui montre les calculs pour jusqu'à deux étapes de temps. Le diagramme complet avec toutes les valeurs finales sera montré par la suite.

![Image](https://cdn-media-1.freecodecamp.org/images/lUkTHXkAb3o6Qw-2bl4s5NRFtMncTRSREwGY)

Nous n'avons pas montré les calculs pour l'état "endormi" à k = 2 et les calculs pour k = 3 dans le diagramme ci-dessus pour garder les choses simples.

Maintenant que nous avons tous ces calculs en place, nous voulons calculer la séquence d'états la plus probable dans laquelle le bébé peut se trouver sur les différentes étapes de temps données. Donc, pour k = 2 et l'état Éveillé, nous voulons savoir l'état le plus probable à k = 1 qui a fait la transition vers Éveillé à k = 2. (k = 2 représente une séquence d'états de longueur 3 commençant à partir de 0 et t = 2 signifierait l'état à l'étape de temps 2. Nous avons l'état à t = 0 c'est-à-dire Éveillé).

![Image](https://cdn-media-1.freecodecamp.org/images/hV8XAZkdEJ-HENyJ9DBZgu0Vwm7u0lQWHWT2)

Clairement, si l'état à l'étape de temps 2 était ÉVEILLÉ, alors l'état à l'étape de temps 1 aurait également été ÉVEILLÉ, comme le montrent les calculs. Ainsi, l'algorithme de Viterbi nous aide non seulement à trouver les valeurs π(k), c'est-à-dire les valeurs de coût pour toutes les séquences en utilisant le concept de programmation dynamique, mais il nous aide également à trouver la séquence d'étiquettes la plus probable étant donné un état de départ et une séquence d'observations. L'algorithme, ainsi que le pseudo-code pour stocker les **pointeurs arrière**, est donné ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/VqlLFmx7w4LC6rnzTzA3LgvUv0b2vf9F2txl)

#### Calculs pour le problème d'étiquetage grammatical

Regardons un corpus légèrement plus grand pour l'étiquetage grammatical et le graphe Viterbi correspondant montrant les calculs et les pointeurs arrière pour l'algorithme de Viterbi.

Voici le corpus que nous allons considérer :

![Image](https://cdn-media-1.freecodecamp.org/images/Coevve7f9ffS700x33OV4OFAL0D8C1SW8l3y)

Maintenant, jetez un coup d'œil aux probabilités de transition calculées à partir de ce corpus.

![Image](https://cdn-media-1.freecodecamp.org/images/FLAyUOfUmBVGToY3jhS8GNlCC4Vwe7UD5JxF)

Ici, q0 → VB représente la probabilité qu'une phrase commence par l'étiquette VB, c'est-à-dire que le premier mot d'une phrase est étiqueté comme VB. De même, q0 → NN représente la probabilité qu'une phrase commence par l'étiquette NN. Remarquez que sur 10 phrases dans le corpus, 8 commencent par NN et 2 par VB et donc les probabilités de transition correspondantes.

En ce qui concerne les probabilités d'émission, idéalement, nous devrions examiner toutes les combinaisons d'étiquettes et de mots dans le corpus. Comme cela serait trop, nous ne considérerons que les probabilités d'émission pour la phrase qui serait utilisée dans les calculs pour l'algorithme de Viterbi.

```
Time flies like an arrow
```

Les probabilités d'émission pour la phrase ci-dessus sont :

![Image](https://cdn-media-1.freecodecamp.org/images/NNBG1YsFT9KY4LgXojD-wlO5tkkc0akbifBP)

Enfin, nous sommes prêts à voir les calculs pour la phrase donnée, les probabilités de transition, les probabilités d'émission et le corpus donné.

![Image](https://cdn-media-1.freecodecamp.org/images/oHM8ZO9SqAQ3oXTd0GgQPsKVpzDRefYgAN2G)

Alors, est-ce tout ce qu'il y a dans l'algorithme de Viterbi ?

Jetez un coup d'œil à l'exemple ci-dessous.

Le seau sous chaque mot est rempli des étiquettes possibles vues à côté du mot dans le corpus d'entraînement. La phrase donnée peut avoir les combinaisons d'étiquettes en fonction du chemin que nous prenons. Mais il y a un piège. Pouvez-vous déterminer ce que c'est ?

![Image](https://cdn-media-1.freecodecamp.org/images/XsP3zTF1Jcy-t1s3jnlYGCjvieey08uA0PwV)
_Toutes les combinaisons de chemins de séquence_

Avez-vous pu le déterminer ?

Non ??

Permettez-moi de vous dire ce que c'est.

Il pourrait y avoir un chemin dans le graphe de calcul pour lequel nous n'avons pas de probabilité de transition. Donc notre algorithme peut simplement ignorer ce chemin et prendre l'autre chemin.

![Image](https://cdn-media-1.freecodecamp.org/images/WO2lchwGpds8OKBCsBIHuibwSEt7ZFJC81HN)

Dans le diagramme ci-dessus, nous ignorons le chemin marqué en rouge puisque nous n'avons pas q(VB|VB). Le corpus d'entraînement n'a jamais un **VB** suivi d'un **VB**. Donc dans les calculs de Viterbi, nous finissons par prendre q(VB|VB) = 0. Et si vous avez suivi l'algorithme de près, vous trouveriez qu'un seul 0 dans les calculs rendrait la probabilité entière ou le coût maximum pour une séquence d'étiquettes/labels à 0.

Cela signifie cependant que nous ignorons les combinaisons qui ne sont pas vues dans le corpus d'entraînement.

Est-ce la bonne façon d'aborder les exemples du monde réel ?

Considérons une petite modification dans la phrase ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/rwKP4uok5cPSrHwrBw1nzB8D-fnVn2iKB95q)
_Time flies like **take** arrow_

Dans cette phrase, nous n'avons pas de chemin alternatif. Même si nous avons une probabilité de Viterbi jusqu'à ce que nous atteignions le mot "like", nous ne pouvons pas aller plus loin. Puisque q(VB|VB) = 0 et q(VB|IN) = 0. Que faisons-nous maintenant ?

Le corpus que nous avons considéré ici était très petit. Considérons n'importe quel corpus de taille raisonnable avec beaucoup de mots et nous avons un problème majeur de rareté des données. Jetez un coup d'œil ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/ckuxohKqg8EpJCrJ2yJXnAy3vn1woRsCor4P)
_Source : [http://www.cs.pomona.edu/~kim/CSC181S08/lectures/Lec6/Lec6.pdf](http://www.cs.pomona.edu/~kim/CSC181S08/lectures/Lec6/Lec6.pdf" rel="noopener" target="_blank" title=")_

Cela signifie que nous pouvons avoir potentiellement 68 milliards de bigrammes, mais le nombre de mots dans le corpus est juste en dessous d'un milliard. C'est un nombre énorme de probabilités de transition nulles à remplir. Le problème de la rareté des données est encore plus élaboré dans le cas où nous considérons des trigrammmes.

Pour résoudre ce problème de rareté des données, nous recourons à une solution appelée Lissage.

### Lissage

L'idée derrière le Lissage est simplement la suivante :

1. **Réduire** — les valeurs de probabilité existantes quelque peu et
2. **Réallouer** — cette probabilité aux zéros

De cette manière, nous redistribuons les valeurs de probabilité non nulles pour compenser les combinaisons de transitions non vues. Considérons un type très simple de technique de lissage connu sous le nom de Lissage de Laplace.

Le lissage de Laplace est également connu sous le nom de lissage à un compte. Vous comprendrez exactement pourquoi il porte ce nom dans un instant. Révisez comment les paramètres pour un modèle HMM trigramme sont calculés étant donné un corpus d'entraînement.

![Image](https://cdn-media-1.freecodecamp.org/images/ICpHbDq7uB06MmmV1dnZbbFOaiUJm1mEsYdq)

Les valeurs possibles qui peuvent mal tourner ici sont

1. `c(u, v, s)` est 0
2. `c(u, v)` est 0
3. Nous obtenons un mot inconnu dans la phrase de test, et nous n'avons aucune étiquette d'entraînement associée à celui-ci.

Tous ceux-ci peuvent être résolus via le lissage. Ainsi, les comptes de lissage de Laplace deviendraient

![Image](https://cdn-media-1.freecodecamp.org/images/xwUoAtAzIUaU0vQWKyaqBpZJHJ-B4AlxGs9J)

Ici, V est le nombre total d'étiquettes dans notre corpus et λ est essentiellement une valeur réelle entre 0 et 1. Il agit comme un facteur de réduction. Une valeur λ = 1 nous donnerait **trop de redistribution des valeurs de probabilité**. Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/PTWcfPCoCcpB4rRBO1HTHnUvcJf3SeUoIKne)

Trop de poids est donné aux trigrammmes non vus pour λ = 1 et c'est pourquoi la version modifiée mentionnée ci-dessus du lissage de Laplace est considérée pour toutes les applications pratiques. La valeur du facteur de réduction doit être variée d'une application à l'autre.

Notez que λ = 1 ne créerait un problème que si la taille du vocabulaire est trop grande. Pour un corpus plus petit, λ = 1 nous donnerait une bonne performance pour commencer.

Une chose à noter sur le lissage de Laplace est qu'il s'agit d'une redistribution uniforme, c'est-à-dire que tous les trigrammmes qui n'avaient pas été vus auparavant auraient des probabilités égales. Supposons donc que nous soyons donnés certaines données et que nous observions que

* La fréquence du trigramme <gave, the, thing> est nulle
* La fréquence du trigramme <gave, the, think> est également nulle
* La distribution uniforme sur les événements non vus signifie :   
P(thing|gave, the) = P(think|gave, the)

Cela reflète-t-il notre connaissance de l'usage de l'anglais ?  
P(thing|gave, the) > P(think|gave, the) idéalement, mais la distribution uniforme utilisant le lissage de Laplace ne tiendra pas compte de cela.

Cela signifie que des millions de trigrammmes non vus dans un énorme corpus auraient des probabilités égales lorsqu'ils sont considérés dans nos calculs. Ce n'est probablement pas la bonne chose à faire. Cependant, c'est mieux que de considérer les probabilités 0 qui conduiraient à ces trigrammmes et finalement à certains chemins dans le graphe de Viterbi étant complètement ignorés. Mais cela doit encore être travaillé et amélioré.

Il existe cependant de nombreux types de techniques de lissage qui améliorent la technique de base du lissage de Laplace et aident à surmonter ce problème de distribution uniforme des probabilités. Certaines de ces techniques sont :

* Estimation de Good-Turing
* Lissage de Jelinek-Mercer (interpolation)
* Lissage de Katz (retour en arrière)
* Lissage de Witten-Bell
* Réduction absolue
* Lissage de Kneser-Ney

Pour en savoir plus sur ces différents types de techniques de lissage en détail, consultez ce [tutoriel](https://nlp.stanford.edu/~wcmac/papers/20050421-smoothing-tutorial.pdf). Le choix de la technique de lissage dépend fortement du type d'application en question, du type de données considéré et également de la taille de l'ensemble de données.

Si vous avez suivi cet article, alors je dois dire

![Image](https://cdn-media-1.freecodecamp.org/images/DQRTVyAtupCa8fq-19mLOv0j9j5CpF2EQBnZ)
_Source : [https://sebreg.deviantart.com/art/You-re-Kind-of-Awesome-289166787](https://sebreg.deviantart.com/art/You-re-Kind-of-Awesome-289166787" rel="noopener" target="_blank" title=")_

Passons à une légère optimisation que nous pouvons apporter à l'algorithme de Viterbi qui peut réduire le nombre de calculs et qui a également du sens pour de nombreux ensembles de données.

Avant cela, cependant, regardez le pseudo-code de l'algorithme une fois de plus.

![Image](https://cdn-media-1.freecodecamp.org/images/rpYO5Tck74JJbbhHl8MBjVHTKmIAtR60c2Eu)

Si nous regardons de près, nous pouvons voir que **pour chaque trigramme de mots, nous considérons tous les ensembles possibles d'étiquettes.** C'est-à-dire que si le nombre d'étiquettes est V, alors nous considérons |V|³ nombre de combinaisons pour chaque trigramme de la phrase de test.

Ignorez le trigramme pour l'instant et considérons simplement un seul mot. Nous considérerions toutes les étiquettes uniques pour un mot donné dans l'algorithme mentionné ci-dessus. Considérons un corpus où nous avons le mot "kick" qui est associé à seulement deux étiquettes, disons {NN, VB} et le nombre total d'étiquettes uniques dans le corpus d'entraînement est d'environ 500 (c'est un énorme corpus).

![Image](https://cdn-media-1.freecodecamp.org/images/PKSiOWrD0TuGlbX9jAD2HlUJio07lBWI2Cyh)

Le problème ici est apparent. Nous pourrions finir par attribuer une étiquette qui n'a pas de sens avec le mot considéré, simplement parce que la probabilité de transition du trigramme se terminant par l'étiquette était très élevée, comme dans l'exemple montré ci-dessus. De plus, il serait computationnellement inefficace de considérer toutes les 500 étiquettes pour le mot "kick" s'il n'apparaît qu'avec deux étiquettes uniques dans l'ensemble du corpus.

Ainsi, l'optimisation que nous faisons est que pour chaque mot, au lieu de considérer toutes les étiquettes uniques dans le corpus, **nous considérons simplement les étiquettes avec lesquelles il est apparu dans le corpus**.

Cela fonctionnerait parce que, pour un corpus raisonnablement grand, un mot donné apparaîtrait idéalement avec tous les différents ensembles d'étiquettes avec lesquels il peut apparaître (la plupart d'entre eux au moins). Il serait alors raisonnable de considérer simplement ces étiquettes pour l'algorithme de Viterbi.

En ce qui concerne l'algorithme de décodage de Viterbi, la complexité reste la même car nous sommes toujours préoccupés par la complexité du pire cas. Dans le pire des cas, chaque mot apparaît avec chaque étiquette unique dans le corpus, et ainsi la complexité reste à O(n|V|³) pour le modèle trigramme et O(n|V|²) pour le modèle bigramme.

Pour l'implémentation récursive du code, veuillez vous référer à

[**DivyaGodayal/HMM-POS-Tagger**](https://github.com/DivyaGodayal/HMM-POS-Tagger)  
[_HMM-POS-Tagger — Une implémentation d'étiqueteur de parties du discours basée sur HMM utilisant le lissage de Laplace et les HMM Trigrammes_github.com](https://github.com/DivyaGodayal/HMM-POS-Tagger)

L'implémentation récursive est faite avec le lissage de Laplace.

Pour l'implémentation itérative, veuillez vous référer à

[**edorado93/HMM-Part-of-Speech-Tagger**](https://github.com/edorado93/HMM-Part-of-Speech-Tagger)  
[_HMM-Part-of-Speech-Tagger — Un étiqueteur de parties du discours basé sur HMM_github.com](https://github.com/edorado93/HMM-Part-of-Speech-Tagger)

Cette implémentation est faite avec la technique de lissage One-Count qui conduit à une meilleure précision par rapport au lissage de Laplace.

De nombreuses captures d'écran de formules et de calculs dans les deux articles sont dérivées de [ici](http://1. http://www.cs.columbia.edu/~mcollins/courses/nlp2011/notes/hmms.pdf).

N'hésitez pas à nous faire savoir comment cet article de blog vous a aidé, et à signaler les erreurs si vous en trouvez en lisant l'article dans la section des commentaires ci-dessous. De plus, veuillez recommander (en applaudissant) et partager l'amour autant que possible pour cet article si vous pensez que cela pourrait être utile pour quelqu'un.