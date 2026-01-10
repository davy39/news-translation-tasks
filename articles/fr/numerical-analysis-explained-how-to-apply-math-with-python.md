---
title: Comment appliquer les mathématiques avec Python – Analyse numérique expliquée
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-02-29T11:41:59.000Z'
originalURL: https://freecodecamp.org/news/numerical-analysis-explained-how-to-apply-math-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/maxim-hopman-fiXLQXAhCfk-unsplash.jpg
tags:
- name: Math
  slug: math
- name: Mathematics
  slug: mathematics
- name: Python
  slug: python
seo_title: Comment appliquer les mathématiques avec Python – Analyse numérique expliquée
seo_desc: "Numerical analysis is the bridge between math and computer science. \n\
  Essentially, it is the development of algorithms that approximate solutions that\
  \ pure math would also solve, but using less computational resources and faster.\n\
  This field is very im..."
---

L'analyse numérique est le pont entre les mathématiques et l'informatique. 

Essentiellement, il s'agit du développement d'algorithmes qui approchent des solutions que les mathématiques pures résoudraient également, mais en utilisant moins de ressources informatiques et plus rapidement.

Ce domaine est très important. Parce que pour la plupart des solutions dans le monde réel, nous avons seulement besoin de bonnes approximations et non des solutions exactes.

Dans cet article, nous explorerons :

* [Une analogie illustrant l'importance de l'analyse numérique](#heading-une-analogie-qui-illustre-limportance-de-lanalyse-numerique) 
* [Fondamentaux de l'analyse numérique](https://www.freecodecamp.org/news/p/a66b15d8-ae59-4c46-8e58-5211690e1032/fundamentals) 
* [Application de l'analyse numérique dans les problèmes du monde réel](#heading-application-de-lanalyse-numerique-dans-les-problemes-du-monde-reel)
* [Introduction aux équations différentielles partielles (EDP)](#heading-une-introduction-aux-equations-differentielles-partielles-edp)
* [Introduction à l'optimisation en analyse numérique](#heading-une-introduction-a-loptimisation-en-analyse-numerique)

<h2 id="analogie">Une analogie qui illustre l'importance de l'analyse numérique</h2>

Comment pouvons-nous mesurer le littoral d'une île ?

Si nous essayons de mesurer chaque centimètre de chaque petit segment, ce serait impossible et probablement chronophage.

À cause de la mer, le littoral change toujours à ce niveau de détail.

Cependant, en approximant et en mesurant en segments plus grands, nous pouvons obtenir une mesure pratique du littoral.

Cette situation reflète l'analyse numérique.

L'approximation donne des informations dans des situations où la mesure précise est impossible ou peu pratique.

Tout comme nous acceptons une bonne estimation de la longueur du littoral, l'analyse numérique utilise l'approximation pour résoudre des problèmes difficiles.

<h2 id="fondamentaux">Fondamentaux de l'analyse numérique</h2>

L'analyse numérique est tout au sujet de l'approximation. C'est comme utiliser des jumelles pour voir un paysage qui est très loin. Nous ne pouvons pas voir chaque feuille. Mais nous obtenons une image suffisamment bonne pour comprendre le terrain.

Cela est crucial en analyse numérique.

Dans ce domaine, nous résolvons des problèmes mathématiques difficiles où les solutions exactes sont soit impossibles, soit extrêmement gourmandes en ressources.

En approximant, nous obtenons des résultats suffisamment bons avec moins d'efforts computationnels.

<h2 id="application">Application de l'analyse numérique dans les problèmes du monde réel</h2>

Il existe de nombreuses applications de l'analyse numérique

* En ingénierie, elle permet la simulation de structures et de fluides.
* En finance, pour l'évaluation des risques et l'optimisation de portefeuille.
* En science environnementale, elle prédit les modèles climatiques.

Dans chaque domaine, l'analyse numérique est une boîte à outils pour résoudre des problèmes où les mathématiques pures prennent simplement trop de temps, ou il est impossible de donner de bons résultats.

<h2 id="intro-edp">Une introduction aux équations différentielles partielles (EDP)</h2>

Les équations différentielles partielles (EDP) sont des équations qui décrivent comment des quantités comme la chaleur, le son ou l'électricité changent dans différents endroits et au fil du temps.

Résoudre les EDP est très important. Parce que cela nous permet de contrôler ces changements.

En nous permettant de les contrôler, nous pouvons :

* Prédire les modèles météorologiques.
* Comprendre la propagation du son dans différents environnements.
* Concevoir des systèmes de transport efficaces.
* Optimiser la distribution d'énergie.

Cependant, la plupart des EDP ne peuvent être qu'approximées avec des méthodes numériques.

C'est soit trop difficile, soit impossible à trouver par des calculs normaux.

De cette manière, avec des méthodes numériques, nous sommes capables de résoudre les EDP, ce qui à son tour nous permet de résoudre de nombreux problèmes de la vie réelle.

### Solutions numériques des EDP avec SciPy

Résoudre les EDP avec des méthodes numériques implique souvent de diviser les EDP en petites parties gérables. Résoudre chacune d'elles puis les additionner.

SciPy, une bibliothèque Python pour le calcul scientifique et technique, offre de nombreux outils à cet effet.

Maintenant, résolvons un problème de transfert de chaleur dans une tige.

Dans le code ci-dessous, nous verrons ligne par ligne comment il nous permet de savoir comment la chaleur se propage dans une tige :

```
import numpy as np
from scipy.integrate import solve_bvp

def heat_equation(x, y):
    return np.vstack((y[1], -y[0]))

def boundary_conditions(ya, yb):
    return np.array([ya[0], yb[0] - 1])

x = np.linspace(0, 1, 5)
y = np.zeros((2, x.size))

sol = solve_bvp(heat_equation, boundary_conditions, x, y)
```

Voyons comment le code fonctionne bloc par bloc dans les sections suivantes.

### Comment importer les bibliothèques

```
import numpy as np
from scipy.integrate import solve_bvp
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/5-1.png)
_Importation des bibliothèques_

Ici, nous importons 2 bibliothèques Python :

* [NumPy](https://numpy.org/)
* [SciPy](https://scipy.org/)

Ces deux bibliothèques Python sont parmi les plus utilisées en science des données.

### Comment définir l'équation de la chaleur et les conditions aux limites

```
def heat_equation(x, y):
    return np.vstack((y[1], -y[0]))

def boundary_conditions(ya, yb):
    return np.array([ya[0], yb[0] - 1])
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/6.png)
_Définition de l'équation de la chaleur et des conditions aux limites_

Nous créons `heat_equation(x, y)` et `boundary_conditions(ya, yb)`.

Dans `heat_equation(x, y)`, nous définissons l'équation différentielle que nous voulons résoudre.

La fonction `boundary_conditions(ya, yb)` définit les contraintes au début et à la fin d'une solution. La condition est que la fin de la solution doit être d'une unité de moins que le début.

### Comment résoudre l'équation

```
x = np.linspace(0, 1, 5)
y = np.zeros((2, x.size))

sol = solve_bvp(heat_equation, boundary_conditions, x, y)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/7.png)
_Résolution de l'équation_

La ligne `sol = solve_bvp(heat_equation, boundary_conditions, x, y)` est la solution.

Le code [`solve_bvp` signifie résoudre un problème de valeur limite](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_bvp.html).

Il prend quatre arguments :

* `heat_equation` : Il s'agit du problème principal que nous essayons de résoudre.
* `boundary_conditions` : Ce sont les contraintes mathématiques au début et à la fin d'une solution.
* `x` : Ce sont les points que nous choisissons pour explorer nos réponses.
* `y` : Ce sont les tentatives initiales pour résoudre le problème, basées sur vos valeurs `x` choisies.

<h2 id="intro-optimisation">Une introduction à l'optimisation en analyse numérique</h2>

L'optimisation consiste à trouver la meilleure solution parmi toutes les solutions. C'est comme trouver l'itinéraire le plus efficace dans un réseau complexe de routes.

Les méthodes d'optimisation numérique trouvent la solution la plus efficace ou la plus rentable à un problème, qu'il s'agisse de :

* Minimiser les déchets dans la production.
* Maximiser l'efficacité dans un réseau logistique.
* Trouver le meilleur ajustement pour un certain modèle de données.

### Aperçu des techniques d'optimisation numérique avec SciPy

L'objectif dans cet exemple est de minimiser le coût de transport à travers un réseau. 

Par exemple, considérons un problème d'optimisation en logistique, où l'objectif est de minimiser le coût de transport à travers un réseau. 

La fonction `minimize` de SciPy peut être utilisée pour trouver la meilleure stratégie afin de minimiser les coûts tout en respectant toutes les contraintes :

```
from scipy.optimize import minimize

def objective_function(x):
    return x[0]**2 + x[1]**2

def constraint_eq(x):
    return x[0] + x[1] - 10

con_eq = {'type': 'eq', 'fun': constraint_eq}

bounds = [(0, 10), (0, 10)]

x0 = [5, 5]

result = minimize(objective_function, x0, method='SLSQP', bounds=bounds, constraints=[con_eq])
```

Expliquons comment le code fonctionne bloc par bloc.

### Comment importer la bibliothèque

```
from scipy.optimize import minimize
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/8.png)
_Importation de scipy_

Une fois de plus, nous importons la bibliothèque nécessaire :

%[https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.minimize.html]

### Comment définir l'objectif et l'équation de contrainte

```
def objective_function(x):
    return x[0]**2 + x[1]**2

def constraint_eq(x):
    return x[0] + x[1] - 10

con_eq = {'type': 'eq', 'fun': constraint_eq}
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/9.png)
_Définir les équations d'objectif et de contrainte_

* La fonction objectif est la fonction que nous voulons minimiser pour trouver la meilleure réponse.
* L'équation de contrainte est l'équation qui limite l'espace de recherche à ces valeurs `x` qui remplissent cette équation.

`con_eq` est défini par ce qui suit :

* `'type': 'eq'` indique le type de contrainte. `'eq'` signifie égalité, en d'autres termes, la fonction doit être égale à zéro à la solution.
* `'fun': constraint_eq` assigne la fonction de contrainte.

Nous verrons dans le bloc de code suivant, c'est là que nous contraignons les solutions possibles du problème.

### Comment définir une condition initiale et un résultat

```
bounds = [(0, 10), (0, 10)]

x0 = [5, 5]

result = minimize(objective_function, x0, method='SLSQP', bounds=bounds, constraints=[con_eq])
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/10.png)
_Définition de la condition initiale et résolution de l'équation_

Pour comprendre ce bloc de code, comprenons chaque paramètre de `result = minimize(objective_function, x0, method='SLSQP', bounds=bounds, constraints=[con_eq])` :

* `objective_function` : Il s'agit de la fonction à minimiser.
* `x0` : Il s'agit de la supposition initiale pour les variables.
* `method='SLSQP'` : Cela spécifie l'algorithme d'optimisation que nous utilisons. Dans ce cas, nous utilisons [SLSQP (Sequential Least SQuares Programming)](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html).
* `bounds=bounds` : Ce paramètre spécifie les limites pour chacune des variables de décision. 
* `constraints=[con_eq]` : Ce paramètre nous indique les contraintes appliquées dans le problème d'optimisation.

## C'est ainsi que de nombreux problèmes de la vie réelle sont résolus

De nombreuses choses dans la vie réelle sont modélisées avec des équations différentielles partielles.

Ensuite, avec des méthodes d'optimisation développées avec l'analyse numérique, elles sont optimisées.

J'écris cela parce que je sais que les mathématiques peuvent être ennuyeuses pour certaines personnes, et qu'elles ne sont peut-être pas conscientes de leur application pour résoudre des problèmes réels. Le calcul qu'elles apprennent peut être appliqué dans des situations non idéales en dehors des exercices d'examen.

Ici, nous pouvons enfin voir pourquoi les mathématiques sont importantes dans deux scénarios :

* Pour modéliser des systèmes afin d'obtenir des solutions
* Pour optimiser un certain système

## Conclusion

L'analyse numérique est l'un des domaines les plus importants des mathématiques appliquées en STEM.

De la résolution des EDP à l'optimisation des problèmes, l'analyse numérique est partout.

Avec des problèmes de plus en plus complexes, l'analyse numérique prend de l'importance pour obtenir des algorithmes plus rapides qui approchent les solutions des mathématiques pures.

De cette manière, elle est un pont entre les mathématiques théoriques et l'application pratique.

Si vous le souhaitez, vous pouvez obtenir le code complet utilisé dans cet article sur [GitHub](https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code).