---
title: "Résoudre l'\x18insoluble\x19 avec les méthodes de Monte Carlo"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-18T13:27:09.000Z'
originalURL: https://freecodecamp.org/news/solve-the-unsolvable-with-monte-carlo-methods-294de03c80cd
coverImage: https://cdn-media-1.freecodecamp.org/images/0*zgdRA5k-JRPOGc_J.
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: "Résoudre l'\x18insoluble\x19 avec les méthodes de Monte Carlo"
seo_desc: 'By Peter Gleeson

  How do you solve an ‘unsolvable’ problem?

  The worlds of data science, mathematical finance, physics, engineering and bioinformatics
  (amongst many others) readily produce intractable problems. These are problems for
  which no computati...'
---

Par Peter Gleeson

Comment résoudre un problème insoluble ?

Les mondes de la science des données, de la finance mathématique, de la physique, de l'ingénierie et de la bioinformatique (entre autres) produisent facilement des problèmes inextricables. Ce sont des problèmes pour lesquels aucune solution facile sur le plan computationnel n'est disponible.

Heureusement, il existe des méthodes qui peuvent approximer les solutions à ces problèmes avec un truc remarquablement simple.

Les **méthodes de Monte Carlo** sont une classe de méthodes qui peuvent être appliquées à des problèmes computationnellement difficiles pour obtenir des réponses suffisamment précises. Le principe général est remarquablement simple :

1. Échantillonner aléatoirement les entrées du problème
2. Pour chaque échantillon, calculer une sortie
3. Agrégat les sorties pour approximer la solution

Pour une analogie, imaginez que vous êtes une fourmi rampant sur une grande mosaïque carrelée. De votre point de vue, vous n'avez aucun moyen facile de déterminer ce que la mosaïque représente.

Si vous commenciez à marcher autour de la mosaïque et à échantillonner les carreaux que vous visitez à des intervalles aléatoires, vous vous feriez une idée approximative de ce que la mosaïque montre. Plus vous prenez d'échantillons, meilleure sera votre approximation.

Si vous pouviez couvrir chaque carreau, vous auriez finalement une représentation parfaite de la mosaïque. Cependant, cela ne serait pas nécessaire — après un certain nombre d'échantillonnages, vous auriez une assez bonne estimation.

C'est exactement ainsi que les méthodes de Monte Carlo approximer les solutions à des problèmes autrement insolubles.

Le nom fait référence à un célèbre casino à Monaco. Il a été inventé en 1949 par l'un des pionniers de la méthode, Stanislaw Ulam. L'oncle de Ulam était apparemment un joueur, et la connexion entre l'élément de chance dans le jeu et dans les méthodes de Monte Carlo doit avoir été particulièrement apparente pour Stanislaw.

La meilleure façon de comprendre un concept technique est de plonger directement et de voir comment il fonctionne. Le reste de cet article montrera comment les méthodes de Monte Carlo peuvent résoudre trois problèmes intéressants. Les exemples seront présentés en [langage de programmation Julia](https://julialang.org/).

### Présentation de Julia

Il existe un [certain nombre de langages que vous pourriez envisager d'apprendre](https://medium.freecodecamp.org/which-languages-should-you-learn-for-data-science-e806ba55a81f) si vous êtes intéressé par la spécialisation en science des données. L'un d'eux, qui s'est imposé comme une option de plus en plus sérieuse ces dernières années, est un langage appelé Julia.

Julia est un langage de programmation numérique qui a été adopté dans une gamme de disciplines quantitatives. Il est gratuit à télécharger. Il existe également une interface vraiment pratique basée sur un navigateur appelée JuliaBox, qui est alimentée par [Jupyter Notebook](http://jupyter.org/try).

L'une des fonctionnalités intéressantes de Julia dont nous allons nous servir aujourd'hui est la facilité avec laquelle il permet la [programmation parallèle](https://computing.llnl.gov/tutorials/parallel_comp/). Cela vous permet d'effectuer des calculs sur plusieurs processus, offrant un sérieux gain de performance lorsqu'il est fait à grande échelle.

#### Passage au parallèle

Pour lancer Julia sur plusieurs processus, allez dans le terminal (ou ouvrez une nouvelle session de terminal dans JuliaBox) et exécutez la commande suivante :

```
$ julia -p 4
```

Cela initie une session Julia sur quatre CPU. Pour définir une fonction dans Julia, la syntaxe suivante est utilisée :

```
function square(x) return x^2 end
```

C'est exact — au lieu d'indentations ou d'accolades, Julia utilise une approche `début-fin`. Les boucles for sont similaires :

```julia
for i = 1:10 print(i) end
```

Vous pouvez bien sûr ajouter des espaces et des indentations pour aider à la lisibilité.

Les capacités de programmation parallèle de Julia reposent principalement sur deux concepts : les **références distantes** et les **appels distants**.

* Les références distantes sont des objets qui agissent essentiellement comme des espaces réservés nommés pour des objets définis sur d'autres processus.
* Les appels distants permettent aux processus d'appeler des fonctions sur des arguments stockés sur d'autres processus.

Il est important de définir des fonctions sur tous les processus. Consultez le code ci-dessous :

```julia
@everywhere function hello(x)
    return "Hello " * x
    end
    
result = @spawn hello("World!")
print(result)
fetched = fetch(result)
print(fetched)
```

La macro `@everywhere` garantit que la fonction `hello()` est définie sur tous les processus. La macro `@spawn` est utilisée pour envelopper une [fermeture](https://guide.freecodecamp.org/javascript/closures/) autour de l'expression `hello("World!")`, qui est ensuite évaluée à distance sur un processus choisi automatiquement.

Le résultat de cette expression est immédiatement retourné sous forme de référence distante `Future`. Si vous essayez d'imprimer `result`, vous serez déçu. Le résultat de `hello("World!")` a été évalué sur un processus différent et n'est pas disponible ici. Pour le rendre disponible, utilisez la méthode `fetch()`.

Si le fait de créer et de récupérer semble trop fastidieux, vous avez de la chance. Julia dispose également d'une macro `@parallel` qui prend en charge une partie du travail nécessaire à l'exécution de tâches en parallèle.

`@parallel` fonctionne soit de manière autonome, soit avec une fonction de réduction pour collecter les résultats sur tous les processus et les réduire à une sortie finale. Consultez le code ci-dessous :

```julia
@parallel (+) for i = 1:1000000000
    return i
    end
```

La boucle for retourne simplement la valeur de `i` à chaque étape. La macro `@parallel` utilise l'opérateur d'addition comme réducteur. Elle prend chaque valeur de `i` et l'ajoute aux valeurs précédentes.

Le résultat est la somme des premiers milliards d'entiers.

Avec cette visite rapide des capacités de programmation parallèle de Julia en tête, passons à la manière dont nous pouvons utiliser les méthodes de Monte Carlo pour résoudre quelques problèmes exemples intéressants.

### Jouer à la loterie

En tant que premier exemple, imaginons jouer à un jeu de loterie. L'idée est simple — choisir six numéros uniques entre 1 et 50. Chaque ticket coûte, disons, 2 £.

* Si vous correspondez à tous les six numéros à ceux tirés, vous gagnez un gros lot (1 000 000 £)
* Si vous correspondez à cinq numéros, vous gagnez un lot moyen (100 000 £)
* Si vous correspondez à quatre numéros, vous gagnez un petit lot (100 £)
* Si vous correspondez à trois numéros, vous gagnez un très petit lot (10 £)

Que pourriez-vous espérer gagner si vous jouiez à cette loterie tous les jours pendant vingt ans ?

Vous pourriez calculer cela avec un stylo et du papier, en utilisant un peu de théorie des probabilités. Mais cela prendrait du temps ! Au lieu de cela, pourquoi ne pas utiliser une méthode de Monte Carlo ?

L'approche est presque simple à un point suspect — simuler le jeu encore et encore de nombreuses fois, et faire la moyenne du résultat.

Démarrez Julia :

```
$ julia -p 4
```

Maintenant, importez le package StatsBase. Utilisez la macro `@everywhere` pour le rendre disponible... partout.

```
using StatsBase@everywhere using StatsBase
```

Ensuite, définissez une fonction qui simulera un seul jeu de loterie. Les arguments vous permettent de changer les règles du jeu, pour explorer différents scénarios.

```julia
@everywhere function lottery(n, outOf, price)
    ticket = sample(1:outOf, n, replace = false)
    draw = sample(1:outOf, n, replace = false)
    matches = sum(indexin(ticket,draw) .!= 0 )
    if matches == 6
        return 1000000 - price
    elseif matches == 5
        return 100000 - price
    elseif matches == 4
        return 100 - price
    elseif matches == 3
        return 10 - price
    else
        return 0 - price
    end
    end
```

Le nombre de numéros correspondants est calculé en utilisant la fonction `indexin()` de Julia. Cela prend un tableau, et pour chaque élément, retourne l'index de sa position dans un autre tableau (ou zéro si l'élément n'est pas trouvé). Contrairement à de nombreux langages modernes, Julia indexe à partir de un, et non de zéro.

La syntaxe `.!= 0` vérifie lesquels de ces indices ne sont pas égaux à zéro, et retourne soit `true` soit `false` pour chacun. Enfin, le nombre de `true` est additionné, donnant le total des numéros correspondants.

Maintenant, simulons jouer à la loterie tous les jours pendant vingt ans... dix mille fois en parallèle.

```julia
winnings = @parallel (+) for i = 1:(365*20*10000)          
    lottery(6,50,2)
    end
    
print(winnings/10000)
```

Pas un grand retour, hein ?

Vous pourriez étendre le code pour permettre des règles et des scénarios plus avancés, et voir l'effet que cela a sur le résultat.

Les simulations de Monte Carlo permettent de modéliser des situations considérablement plus complexes que cet exemple de loterie. Cependant, l'approche est la même que celle présentée ici.

Voyons ce que les méthodes de Monte Carlo nous permettent de faire d'autre...

### La valeur de pi

Pi (ou π) est une constante mathématique. Il est peut-être surtout célèbre pour son apparition dans la formule de l'aire d'un cercle :

_A = πr²_

π est un exemple de [nombre irrationnel](http://mathworld.wolfram.com/IrrationalNumber.html). Sa valeur exacte est impossible à représenter comme une fraction de deux entiers. En fait, π est également un exemple de [nombre transcendant](https://www.mathsisfun.com/numbers/transcendental-numbers.html) — il n'existe même pas d'[équations polynomiales](http://mathworld.wolfram.com/Polynomial.html) dont il est une solution.

Vous pourriez penser que cela rend l'obtention d'une valeur précise pour π moins que simple. Ou pas ?

En fait, vous pouvez trouver une assez bonne estimation de π en utilisant une méthode inspirée de Monte Carlo. Une analogie visuelle pourrait être la suivante :

* Dessinez un carré de 2m×2m sur un mur. À l'intérieur, dessinez un cercle de rayon 1m.
* Maintenant, reculez de quelques pas et lancez de la peinture aléatoirement sur le mur. Comptez chaque fois que la peinture atterrit dans le cercle.
* Après cent lancers, calculez quelle fraction des lancers a atterri dans le cercle. Multipliez cela par l'aire du carré. Voici votre estimation pour π.

![Image](https://cdn-media-1.freecodecamp.org/images/Nx1UB51Yol0GpIObWhytD9phm5kkZLEgftGw)
_L'aire du cercle est d'environ 78 % de celle du carré, donc environ ce pourcentage de peinture atterrit à l'intérieur du cercle_

La raison pour laquelle cela fonctionne est très intuitive. Lorsque l'on échantillonne des points aléatoires à partir d'un carré contenant un cercle, la probabilité de sélectionner des points à l'intérieur du cercle est proportionnelle à l'aire du cercle.

Avec suffisamment d'échantillons aléatoires, nous pouvons trouver une estimation fiable de cette proportion, _p_.

Maintenant, nous savons que l'aire du carré est de 2×2 = 4m², et nous savons que l'aire du cercle est π×_r_². Puisque le rayon _r_ est égal à 1, l'aire du cercle est simplement π.

Comme nous connaissons l'aire du carré et avons une estimation de la proportion _p_ de son aire couverte par le cercle, nous pouvons estimer π. Il suffit de multiplier _p_×4.

Plus nous lançons d'échantillons aléatoires, meilleure sera l'estimation _p_. Cependant, le gain de précision diminue à mesure que nous prenons de plus en plus d'échantillons.

Voici le code Julia pour simuler cet exemple. J'ai exécuté cela dans le terminal JuliaBox, en utilisant la commande suivante pour lancer Julia sur quatre CPU :

```
$ julia -p 4
```

Tout d'abord, définissez une méthode d'échantillonnage.

```julia
@everywhere function throwPaint(N)
    hits = 0
    for i = 1:N
        x = rand() ; y = rand()
        if x^2 + y^2 < 1
            hits += 1
        end
    end
    return float(hits / N * 4)
end
```

Cela exécute une boucle, échantillonnant aléatoirement les coordonnées `x` et `y` entre 0 et 1. L'instruction if utilise [l'équation du cercle](https://www.khanacademy.org/math/algebra2/intro-to-conics-alg2/expanded-equation-circle-alg2/a/circle-equation-review) pour vérifier si les points se trouvent à l'intérieur d'un cercle imaginaire, comptant le nombre de coups. La fonction retourne la proportion de coups, multipliée par quatre.

L'exécution de cette fonction en parallèle permettra de tirer un nombre extrêmement élevé d'échantillons, offrant une bien plus grande précision.

```julia
Pi = @parallel (+) for i = 1:nworkers()              
    throwPaint(100000000) / nworkers() 
    end

print(Pi)
```

La méthode `nworkers()` retourne le nombre de CPU utilisés (dans ce cas, quatre). Cela signifie que chaque processus exécute la méthode `throwPaint()`, cent millions de fois. Globalement, cela nous donne un énorme nombre d'échantillons, et permet une estimation très précise de la valeur de π.

### Le tableau d'ensemble : Intégration

L'exemple d'estimation de π ci-dessus est un exemple spécifique d'un cas d'utilisation plus général pour l'approximation de Monte Carlo — résoudre des problèmes d'intégration.

[L'intégration est une technique de calcul](http://mathworld.wolfram.com/Integral.html) qui trouve une aire définie par une [fonction mathématique](http://mathworld.wolfram.com/Function.html). Par exemple, une courbe simple pourrait être définie par la fonction :

_f(x) → x²_

Et le graphique correspondant serait :

![Image](https://cdn-media-1.freecodecamp.org/images/dD-8jjpkSQZNigDOy-Bn12P1SAD1YGp-0CZn)
_f(x) → x² donne une courbe classique en forme de U passant par l'origine_

L'aire sous la courbe est trouvée en intégrant _f(x)_.

![Image](https://cdn-media-1.freecodecamp.org/images/gN77Fve6MF4oTwJhJFPEKXnCh8cPkB0vswMj)

Pour des fonctions plus simples, [l'intégration est assez facile à résoudre avec un peu de pratique](https://www.mathsisfun.com/calculus/integration-introduction.html). Cependant, pour des fonctions plus compliquées, nous devons nous tourner vers des méthodes d'estimation.

En basse dimension, l'aire sous une courbe peut être approximée par des algorithmes relativement simples, tels que [la méthode des trapèzes](https://en.wikipedia.org/wiki/Trapezoidal_rule).

Cependant, en raison de [la malédiction de la dimensionnalité](https://medium.freecodecamp.org/the-curse-of-dimensionality-how-we-can-save-big-data-from-itself-d9fa0f872335), cela devient computationnellement irréalisable en dimensions supérieures. Les méthodes basées sur Monte Carlo peuvent être utilisées pour estimer l'aire à la place.

Cela peut être visualisé exactement de la même manière que l'exemple de π ci-dessus, sauf que la courbe n'a pas besoin d'être définie comme un cercle. Au lieu de cela, imaginez lancer de la peinture sur un carré unitaire contenant une forme arbitraire. Par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/apgKXkwcEs7p6sDQiFYdth4DAHW2UUh-yNDp)
_L'aire sous la courbe est d'environ 45 % de celle du carré. Pas besoin de calcul !_

En dimensions supérieures, le principe reste le même. Le problème est toujours résolu en échantillonnant aléatoirement des valeurs d'entrée, en les évaluant et en les agrégeant pour approximer la solution. Au lieu d'échantillonner à partir d'un cercle dans un carré, imaginez échantillonner une sphère dans un cube.

En tant qu'exemple final, prenons un casse-tête mathématique difficile.

#### Un casse-tête mathématique difficile

> _Prenez deux points au hasard dans un cube unitaire. En moyenne, quelle est la distance entre eux ?_

![Image](https://cdn-media-1.freecodecamp.org/images/LycK4mnl7-FALRaqOlQUIYDWAEHcRUTLnV5B)
_Prenez deux points au hasard à l'intérieur d'un cube unitaire. Quelle est la distance attendue entre eux ?_

Je vous donne un avertissement maintenant — la [solution mathématique n'est pas exactement triviale](http://mathworld.wolfram.com/HypercubeLinePicking.html).

![Image](https://cdn-media-1.freecodecamp.org/images/30gI-9USoAyUK1kzjqfli28VwbJ2wpOb04Jl)
_Si vous aimez résoudre des intégrales multiples, eh bien... bonne chance ! Pour le reste d'entre nous, il y a toujours Monte Carlo..._

Cependant, il est possible d'obtenir une estimation précise en utilisant — vous l'avez deviné — une méthode de Monte Carlo.

```
$ julia -p 4
```

Tout d'abord, définissez une méthode d'échantillonnage.

```julia
@everywhere function samplePoints(dimensions)
    pt1 = []
    pt2 = []
    for i = 1:dimensions
        pt1 = push!(pt1, rand())
        pt2 = push!(pt2, rand())
    end
    return [pt1, pt2]
    end
```

Maintenant, définissez une fonction qui calcule la distance entre les points.

```julia
@everywhere function distance(points)
    pt1 = points[1]
    pt2 = points[2]
    arr = []
    for i = 1:length(pt1)
        d = (pt2[i] - pt1[i]) ^ 2
        arr = push!(arr, d)
    end
    dist = sqrt(sum(arr))
    return dist
    end
```

Enfin, exécutez ces deux fonctions ensemble en parallèle. Au lieu de réduire à une seule sortie, cette fois nous allons écrire chaque résultat dans un objet `SharedArray`. Les objets `SharedArray` permettent à différents processus d'accéder aux données stockées dans le même objet de tableau.

```julia
results = SharedArray{Float64}(1000000)
@parallel for i = 1:1000000
    results[i] = distance(samplePoints(3))
    end
    
sum(results) / length(results)
```

Vous devriez obtenir une réponse très proche de 0,6617 — et c'est bien sûr la bonne réponse ! En changeant l'argument passé à `samplePoints()`, vous pouvez résoudre le problème généralisé dans autant de dimensions que vous le souhaitez.

### Et ensuite ?

Espérons que vous avez trouvé cette introduction aux méthodes de Monte Carlo utile !

Lorsqu'elles sont mises en œuvre correctement, elles fournissent un outil inestimable pour les scientifiques des données, les ingénieurs, les mathématiciens financiers et les chercheurs... et toute autre personne dont le travail implique la compréhension de systèmes complexes.

Si vous êtes intéressé à en apprendre davantage sur leurs applications, il existe une tonne de ressources en ligne. Cependant, la meilleure façon d'apprendre est de pratiquer ! Une fois que vous êtes à l'aise avec le principe de base, pourquoi ne pas essayer de simuler vos propres exemples de Monte Carlo ?

Tout commentaire ou feedback, veuillez le laisser ci-dessous !