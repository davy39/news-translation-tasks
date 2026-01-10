---
title: Apprendre les statistiques pour la Data Science, le Machine Learning et l'IA
  – Le guide complet
date: '2024-04-12T23:08:39.000Z'
author: Tatev Aslanyan
authorURL: https://www.freecodecamp.org/news/author/tatevkaren/
originalURL: https://freecodecamp.org/news/statistics-for-data-scientce-machine-learning-and-ai-handbook
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Learn-Statistics-Cover-Version-2--1-.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: handbook
  slug: handbook
- name: Machine Learning
  slug: machine-learning
- name: MathJax
  slug: mathjax
- name: statistics
  slug: statistics
seo_desc: 'Karl Pearson was a British mathematician who once said "Statistics is the
  grammar of science". This holds true especially for Computer and Information Sciences,
  Physical Science, and Biological Science.

  When you are getting started with your journey ...'
---


Karl Pearson était un mathématicien britannique qui a dit un jour : "La statistique est la grammaire de la science". Cela est particulièrement vrai pour les sciences de l'informatique et de l'information, les sciences physiques et les sciences biologiques.

<!-- more -->

Lorsque vous commencez votre parcours en Data Science, Data Analytics, Machine Learning ou IA (y compris l'IA générative), posséder des connaissances statistiques vous aidera à mieux exploiter les insights issus des données et à comprendre réellement tous les algorithmes au-delà de leur simple approche d'implémentation.

On ne saurait trop insister sur l'importance des statistiques en Data Science et en Intelligence Artificielle. Les statistiques fournissent des outils et des méthodes pour trouver une structure et donner des insights plus profonds sur les données. Les statistiques comme les mathématiques aiment les faits et détestent les suppositions. Connaître les fondamentaux de ces deux sujets importants vous permettra de penser de manière critique et d'être créatif lorsque vous utiliserez les données pour résoudre des problèmes métier et prendre des décisions basées sur les données.

### Concepts statistiques clés pour votre parcours en Data Science ou Data Analysis avec du code Python

Dans ce guide, je couvrirai les sujets statistiques suivants pour la Data Science, le Machine Learning et l'Intelligence Artificielle (y compris la GenAI) :

-   [Variables aléatoires][1]
-   [Moyenne, variance, écart-type][2]
-   [Covariance et corrélation][3]
-   [Fonctions de distribution de probabilité (PDF)][4]
-   [Théorème de Bayes][5]
-   [Régression linéaire et moindres carrés ordinaires (MCO)][6]
-   [Théorème de Gauss-Markov][7]
-   [Propriétés des paramètres (biais, convergence, efficacité)][8]
-   [Intervalles de confiance][9]
-   [Tests d'hypothèses][10]
-   [Signification statistique][11]
-   [Erreur de type I et de type II][12]
-   [Tests statistiques (test t de Student, test F, test T à 2 échantillons, test Z à 2 échantillons, test du Khi-deux)][13]
-   [La p-value et ses limites][14]
-   [Statistiques inférentielles][15]
-   [Théorème Central Limite et Loi des Grands Nombres][16]
-   [Techniques de réduction de dimensionnalité (ACP, AF)][17]
-   [Préparation aux entretiens - Top 7 des questions de statistiques avec réponses][18]
-   [À propos de l'auteur][19]
-   [Comment aller plus loin ?][20]

Si vous n'avez aucune connaissance statistique préalable et que vous souhaitez identifier et apprendre les concepts statistiques essentiels en partant de zéro pour préparer vos entretiens d'embauche, alors ce guide est pour vous. Il sera également une excellente lecture pour quiconque souhaite rafraîchir ses connaissances statistiques.

## Prérequis

Avant de commencer la lecture de ce guide sur les concepts clés des statistiques pour la Data Science, le Machine Learning et l'Intelligence Artificielle, quelques prérequis vous aideront à en tirer le meilleur parti.

Cette liste est conçue pour s'assurer que vous êtes bien préparé et que vous pouvez pleinement saisir les concepts statistiques abordés :

1.  **Compétences mathématiques de base** : Une aisance avec les mathématiques de niveau lycée, incluant l'algèbre et le calcul de base, est essentielle. Ces compétences sont cruciales pour comprendre les formules et méthodes statistiques.
2.  **Pensée logique** : La capacité à penser de manière logique et méthodique pour résoudre des problèmes aidera à comprendre le raisonnement statistique et à appliquer ces concepts à des scénarios basés sur les données.
3.  **Maîtrise de l'outil informatique** : Une connaissance de base de l'utilisation des ordinateurs et d'Internet est nécessaire, car de nombreux exemples et exercices pourraient nécessiter l'utilisation de logiciels statistiques ou de codage.
4.  Une connaissance de base de Python, telle que la création de variables et la manipulation de structures de données de base, est également requise (si vous n'êtes pas familier avec ces concepts, consultez mon cours **[Python for Data Science 2024 - Full Course for Beginners][21]** ici).
5.  **Curiosité et volonté d'apprendre** : Un vif intérêt pour l'apprentissage et l'exploration des données est peut-être le prérequis le plus important. Le domaine de la Data Science évolue constamment, et une approche proactive de l'apprentissage sera incroyablement bénéfique.

Ce guide ne suppose aucune connaissance préalable en statistiques, ce qui le rend accessible aux débutants. Néanmoins, une familiarité avec les concepts ci-dessus améliorera considérablement votre compréhension et votre capacité à appliquer efficacement les méthodes statistiques dans divers domaines.

Si vous souhaitez apprendre les mathématiques, les statistiques, le Machine Learning ou l'IA, consultez notre **[chaîne YouTube][22]** et **[LunarTech.ai][23]** pour des ressources gratuites.

## Variables aléatoires

Les variables aléatoires constituent la pierre angulaire de nombreux concepts statistiques. Il peut être difficile de digérer la définition mathématique formelle d'une variable aléatoire, mais pour faire simple, c'est un moyen d'associer les résultats de processus aléatoires, tels que le lancer d'une pièce ou d'un dé, à des nombres.

Par exemple, nous pouvons définir le processus aléatoire du lancer d'une pièce par une variable aléatoire X qui prend la valeur 1 si le résultat est _face_ et 0 si le résultat est _pile_.

$$X =  
\\begin{cases}  
1 & \\text{si face} \\\\  
0 & \\text{si pile}  
\\end{cases}  
$$

Dans cet exemple, nous avons un processus aléatoire de lancer de pièce où cette expérience peut produire **deux** **résultats possibles** : {0,1}. Cet ensemble de tous les résultats possibles est appelé l'**espace échantillonnal** de l'expérience. Chaque fois que le processus aléatoire est répété, on parle d'**événement**.

Dans cet exemple, lancer une pièce et obtenir pile comme résultat est un événement. La chance ou la probabilité que cet événement se produise avec un résultat particulier est appelée la **probabilité** de cet événement.

La probabilité d'un événement est la vraisemblance qu'une variable aléatoire prenne une valeur spécifique x, ce qui peut être décrit par P(x). Dans l'exemple du lancer de pièce, la probabilité d'obtenir face ou pile est la même, soit 0,5 ou 50 %. Nous avons donc la configuration suivante :

$$  
\\begin{align}  
\\Pr(X = \\text{face}) = 0,5 \\\\  
\\Pr(X = \\text{pile}) = 0,5  
\\end{align}  
$$

où la probabilité d'un événement, dans cet exemple, ne peut prendre que des valeurs comprises dans l'intervalle [0,1].

## Moyenne, variance, écart-type

Pour comprendre les concepts de moyenne, de variance et de nombreux autres sujets statistiques, il est important d'apprendre les concepts de **population** et d'**échantillon.**

La population est l'ensemble de toutes les observations (individus, objets, événements ou procédures) et est généralement très large et diversifiée. D'un autre côté, un échantillon est un sous-ensemble d'observations de la population qui, idéalement, est une représentation fidèle de la population.

![1-VnNrkwNuW2hBKA8DC84Gdg](https://www.freecodecamp.org/news/content/images/2024/04/1-VnNrkwNuW2hBKA8DC84Gdg.png)

Source de l'image : [LunarTech][24]

Étant donné qu'expérimenter sur une population entière est soit impossible, soit simplement trop coûteux, les chercheurs ou analystes utilisent des échantillons plutôt que la population entière dans leurs expériences ou essais.

Pour s'assurer que les résultats expérimentaux sont fiables et valables pour l'ensemble de la population, l'échantillon doit être une représentation fidèle de la population. C'est-à-dire que l'échantillon doit être non biaisé.

À cette fin, nous pouvons utiliser des [techniques d'échantillonnage statistique][25] telles que l'échantillonnage aléatoire, l'échantillonnage systématique, l'échantillonnage en grappes, l'échantillonnage pondéré et l'échantillonnage stratifié.

### Moyenne

La moyenne, également connue sous le nom de moyenne arithmétique, est une valeur centrale d'un ensemble fini de nombres. Supposons qu'une variable aléatoire X dans les données possède les valeurs suivantes :

$$ X\_1, X\_2, X\_3, \\ldots, X\_N $$

où N est le nombre d'observations ou de points de données dans l'ensemble de l'échantillon, ou simplement la fréquence des données. Alors la **moyenne échantillonnale** définie par **μ**, qui est très souvent utilisée pour approximer la **moyenne de la population**, peut être exprimée comme suit :

$$  
\\mu = \\frac{\\sum\_{i=1}^{N} x\_i}{N}  
$$

La moyenne est également appelée **espérance**, qui est souvent définie par **E**() ou par une variable aléatoire surmontée d'une barre. Par exemple, l'espérance des variables aléatoires X et Y, soit **E**(X) et **E**(Y) respectivement, peut être exprimée comme suit :

$$  
\\bar{X} = \\frac{\\sum\_{i=1}^{N} X\_i}{N}  
$$  
  
$$  
\\bar{Y} = \\frac{\\sum\_{i=1}^{N} Y\_i}{N}  
$$

Maintenant que nous avons une solide compréhension de la moyenne en tant que mesure statistique, voyons comment nous pouvons appliquer ces connaissances de manière pratique en utilisant Python. Python est un langage de programmation polyvalent qui, à l'aide de bibliothèques comme NumPy, facilite l'exécution d'opérations mathématiques complexes, y compris le calcul de la moyenne.

Dans l'extrait de code suivant, nous démontrons comment calculer la moyenne d'un ensemble de nombres en utilisant NumPy. Nous commencerons par montrer le calcul pour un simple tableau de nombres. Ensuite, nous aborderons un scénario courant en Data Science : calculer la moyenne d'un jeu de données comprenant des valeurs non définies ou manquantes, représentées par NaN (Not a Number). NumPy fournit une fonction spécifiquement conçue pour gérer de tels cas, nous permettant de calculer la moyenne tout en ignorant ces valeurs NaN.

Voici comment vous pouvez effectuer ces opérations en Python :

```python
import numpy as np
import math
x = np.array([1,3,5,6])
mean_x = np.mean(x)

# au cas où les données contiennent des valeurs Nan
x_nan = np.array([1,3,5,6, math.nan])
mean_x_nan = np.nanmean(x_nan)
```

### Variance

La variance mesure l'écart entre les points de données et la valeur moyenne. Elle est égale à la somme des carrés des différences entre les valeurs des données et la moyenne.

Nous pouvons exprimer la **variance de la population** comme suit :

```python
x = np.array([1,3,5,6])
variance_x = np.var(x)

# ici vous devez spécifier les degrés de liberté (df), le nombre maximum de points de données logiquement indépendants qui ont la liberté de varier
x_nan = np.array([1,3,5,6, math.nan])
mean_x_nan = np.nanvar(x_nan, ddof = 1)
```

Pour dériver les espérances et les variances de différentes fonctions de distribution de probabilité populaires, [consultez ce dépôt Github][26].

### Écart-type

L'écart-type est simplement la racine carrée de la variance et mesure la mesure dans laquelle les données varient par rapport à leur moyenne. L'écart-type défini par **sigma** peut être exprimé comme suit :

$$  
\\sigma^2 = \\frac{\\sum\_{i=1}^{N} (x\_i - \\mu)^2}{N}  
$$

L'écart-type est souvent préféré à la variance car il possède les mêmes unités que les points de données, ce qui signifie que vous pouvez l'interpréter plus facilement.

Pour calculer la variance de la population à l'aide de Python, nous utilisons la fonction `var` de la bibliothèque NumPy. Par défaut, cette fonction calcule la variance de la population en réglant le paramètre `ddof` (Delta Degrees of Freedom) sur 0. Cependant, lorsque vous traitez des échantillons et non la population entière, vous réglez généralement `ddof` sur 1 pour obtenir la variance de l'échantillon.

L'extrait de code fourni montre comment calculer la variance pour un ensemble de données. De plus, il montre comment calculer la variance lorsqu'il y a des valeurs NaN dans les données. Les valeurs NaN représentent des données manquantes ou non définies. Lors du calcul de la variance, ces valeurs NaN doivent être gérées correctement ; sinon, elles peuvent donner une variance qui n'est pas un nombre (NaN), ce qui n'est pas informatif.

Voici comment vous pouvez calculer la variance de la population en Python, en tenant compte de la présence potentielle de valeurs NaN :

```python
x = np.array([1,3,5,6])
variance_x = np.std(x)

x_nan = np.array([1,3,5,6, math.nan])
mean_x_nan = np.nanstd(x_nan, ddof = 1)
```

### Covariance

La covariance est une mesure de la variabilité conjointe de deux variables aléatoires et décrit la relation entre ces deux variables. Elle est définie comme l'espérance du produit des écarts des deux variables aléatoires par rapport à leurs moyennes respectives.

La covariance entre deux variables aléatoires X et Z peut être décrite par l'expression suivante, où **E**(X) et **E**(Z) représentent les moyennes de X et Z, respectivement.

$$ \\text{Cov}(X, Z) = E\\left\[(X - E(X))(Z - E(Z))\\right\] $$

La covariance peut prendre des valeurs négatives ou positives ainsi qu'une valeur de 0. Une valeur positive de covariance indique que deux variables aléatoires ont tendance à varier dans la même direction, tandis qu'une valeur négative suggère que ces variables varient dans des directions opposées. Enfin, la valeur 0 signifie qu'elles ne varient pas ensemble.

Pour explorer le concept de covariance de manière pratique, nous utiliserons Python avec la bibliothèque NumPy, qui fournit des opérations numériques puissantes. La fonction `np.cov` peut être utilisée pour calculer la matrice de covariance pour deux jeux de données ou plus. Dans la matrice, les éléments diagonaux représentent la variance de chaque jeu de données, et les éléments hors diagonale représentent la covariance entre chaque paire de jeux de données.

Regardons un exemple de calcul de la covariance entre deux ensembles de données :

```python
x = np.array([1,3,5,6])
y = np.array([-2,-4,-5,-6])

# ceci retournera la matrice de covariance de x,y contenant x_variance, y_variance sur les éléments diagonaux et la covariance de x,y
cov_xy = np.cov(x,y)
```

### Corrélation

La corrélation est également une mesure de relation. Elle mesure à la fois la force et la direction de la relation linéaire entre deux variables.

Si une corrélation est détectée, cela signifie qu'il existe une relation ou un motif entre les valeurs de deux variables cibles. La corrélation entre deux variables aléatoires X et Z est égale à la covariance entre ces deux variables divisée par le produit des écarts-types de ces variables. Cela peut être décrit par l'expression suivante :

$$ \\rho\_{X,Z} = \\frac{\\text{Cov}(X, Z)}{\\sigma\_X \\sigma\_Z} $$

Les valeurs des coefficients de corrélation varient entre -1 et 1. Gardez à l'esprit que la corrélation d'une variable avec elle-même est toujours égale à 1, soit **Cor(X, X) = 1**.

Une autre chose à garder à l'esprit lors de l'interprétation de la corrélation est de ne pas la confondre avec la **causalité**, étant donné qu'une corrélation n'est pas nécessairement une causalité. Même s'il existe une corrélation entre deux variables, vous ne pouvez pas conclure qu'une variable provoque un changement dans l'autre. Cette relation pourrait être fortuite, ou un troisième facteur pourrait être à l'origine du changement des deux variables.

```python
x = np.array([1,3,5,6])
y = np.array([-2,-4,-5,-6])

corr = np.corrcoef(x,y)
```

## Fonctions de distribution de probabilité

Une fonction qui décrit toutes les valeurs possibles, l'espace échantillonnal et les probabilités correspondantes qu'une variable aléatoire peut prendre dans une plage donnée, délimitée entre les valeurs minimales et maximales possibles, est appelée **une fonction de distribution de probabilité (PDF)** ou densité de probabilité.

Chaque PDF doit satisfaire aux deux critères suivants :

$$  
0 \\leq \\Pr(X) \\leq 1 \\\\  
\\sum p(X) = 1  
$$

où le premier critère stipule que toutes les probabilités doivent être des nombres compris dans l'intervalle [0,1] et le second critère stipule que la somme de toutes les probabilités possibles doit être égale à 1.

Les fonctions de probabilité sont généralement classées en deux catégories : **discrètes** et **continues**.

Une fonction de distribution discrète décrit un processus aléatoire avec un espace échantillonnal **dénombrable**, comme dans l'exemple du lancer d'une pièce qui n'a que deux résultats possibles. Les fonctions de distribution continues décrivent un processus aléatoire avec un espace échantillonnal **continu**.

Des exemples de fonctions de distribution discrètes sont [Bernoulli][27], [Binomiale][28], [Poisson][29], [Uniforme discrète][30]. Des exemples de fonctions de distribution continues sont [Normale][31], [Uniforme continue][32], [Cauchy][33].

### Distribution binomiale

[La distribution binomiale][34] est la distribution de probabilité discrète du nombre de succès dans une séquence de **n** expériences indépendantes, chacune avec un résultat de valeur booléenne : **succès** (avec une probabilité **p**) ou **échec** (avec une probabilité **q** = 1 − p).

Supposons qu'une variable aléatoire X suive une distribution binomiale, alors la probabilité d'observer **k** succès dans n essais indépendants peut être exprimée par la fonction de densité de probabilité suivante :

$$ \\Pr(X = k) = \\binom{n}{k} p^k q^{n-k} $$

La distribution binomiale est utile lors de l'analyse des résultats d'expériences indépendantes répétées, surtout si vous vous intéressez à la probabilité d'atteindre un seuil particulier étant donné un taux d'erreur spécifique.

#### Moyenne et variance de la distribution binomiale

La moyenne d'une distribution binomiale, notée _E_(_X_)=_np_, vous indique le nombre moyen de succès auxquels vous pouvez vous attendre si vous menez _n_ essais indépendants d'une expérience binaire.

Une expérience binaire est une expérience où il n'y a que deux résultats : succès (avec probabilité _p_) ou échec (avec probabilité _q_=1−_p_).

$$  
E(X) = np \\\\  
\\text{Var}(X) = npq  
$$

Par exemple, si vous deviez lancer une pièce 100 fois et que vous définissiez un succès comme la pièce tombant sur face (disons que la probabilité de face est de 0,5), la distribution binomiale vous dirait quelle est la probabilité d'obtenir n'importe quel nombre de faces dans ces 100 lancers. La moyenne _E_(_X_) serait de 100×0,5=50, indiquant qu'en moyenne, vous vous attendriez à obtenir 50 faces.

La variance Var(X)=npq mesure l'étalement de la distribution, indiquant dans quelle mesure le nombre de succès est susceptible de s'écarter de la moyenne.

En reprenant l'exemple du lancer de pièce, la variance serait de 100×0,5×0,5=25, ce qui vous renseigne sur la variabilité des résultats. Une variance plus petite signifierait que les résultats sont plus étroitement regroupés autour de la moyenne, tandis qu'une variance plus grande indique qu'ils sont plus étalés.

Ces concepts sont cruciaux dans de nombreux domaines. Par exemple :

-   **Contrôle qualité** : Les fabricants peuvent utiliser la distribution binomiale pour prédire le nombre d'articles défectueux dans un lot, les aidant ainsi à comprendre la qualité et la cohérence de leur processus de production.
-   **Santé** : En médecine, elle pourrait être utilisée pour calculer la probabilité qu'un certain nombre de patients répondent à un traitement, sur la base des taux de réussite passés.
-   **Finance** : En finance, les modèles binomiaux sont utilisés pour évaluer le risque de stratégies de portefeuille ou d'investissement en prédisant le nombre de fois qu'un actif atteindra un certain prix.
-   **Sondages et analyse d'enquêtes** : Lors de la prédiction des résultats électoraux ou des préférences des clients, les sondeurs peuvent utiliser la distribution binomiale pour estimer combien de personnes favoriseront un candidat ou un produit, compte tenu de la probabilité tirée d'un échantillon.

Comprendre la moyenne et la variance de la distribution binomiale est fondamental pour interpréter les résultats et prendre des décisions éclairées basées sur la probabilité de différents résultats.

La figure ci-dessous visualise un exemple de distribution binomiale où le nombre d'essais indépendants est égal à 8 et la probabilité de succès à chaque essai est égale à 16 %.

![1-68nMYVFT0e5VsMBf8c226g](https://www.freecodecamp.org/news/content/images/2024/04/1-68nMYVFT0e5VsMBf8c226g.png)

Distribution binomiale - montrant le nombre de succès et la probabilité. Source de l'image : [LunarTech][35]

Le code Python ci-dessous crée un histogramme pour visualiser la distribution des résultats de 1000 expériences, chacune composée de 8 essais avec une probabilité de succès de 0,16. Il utilise NumPy pour générer les données de distribution binomiale et Matplotlib pour tracer l'histogramme, montrant la probabilité du nombre de succès dans ces essais.

```python
# Génération aléatoire de 1000 échantillons binomiaux indépendants
import numpy as np
import matplotlib.pyplot as plt


n = 8
p = 0.16
N = 1000
X = np.random.binomial(n,p,N)
# Histogramme de la distribution binomiale

counts, bins, ignored = plt.hist(X, 20, density = True, rwidth = 0.7, color = 'purple')
plt.title("Distribution binomiale avec p = 0.16 n = 8")
plt.xlabel("Nombre de succès")
plt.ylabel("Probabilité")plt.show()
```

### Distribution de Poisson

[La distribution de Poisson][36] est la distribution de probabilité discrète du nombre d'événements se produisant dans une période de temps spécifiée, étant donné le nombre moyen de fois où l'événement se produit sur cette période.

Supposons qu'une variable aléatoire X suive une distribution de Poisson. Alors la probabilité d'observer **k** événements sur une période de temps peut être exprimée par la fonction de probabilité suivante :

$$ \\Pr(X = k) = \\frac{\\lambda^k e^{-\\lambda}}{k!} $$

où **e** est le [**nombre d'Euler**][37] et **λ** lambda, le **paramètre de taux d'arrivée**, est l'espérance de X. La fonction de distribution de Poisson est très populaire pour son utilisation dans la modélisation d'événements dénombrables se produisant dans un intervalle de temps donné.

#### Moyenne et variance de la distribution de Poisson

La distribution de Poisson est particulièrement utile pour modéliser le nombre de fois qu'un événement se produit dans un laps de temps spécifié. La moyenne E(X) et la variance Var(X) d'une distribution de Poisson sont toutes deux égales à λ, qui est le taux moyen auquel les événements se produisent (également appelé paramètre de taux). Cela rend la distribution de Poisson unique, car elle est caractérisée par ce seul paramètre.

Le fait que la moyenne et la variance soient égales signifie qu'à mesure que nous observons plus d'événements, la distribution du nombre d'occurrences devient plus prévisible. Elle est utilisée dans divers domaines tels que le commerce, l'ingénierie et la science pour des tâches telles que :

Prédire le nombre d'arrivées de clients dans un magasin en une heure. Estimer le nombre d'e-mails que vous recevriez en une journée. Comprendre le nombre de défauts dans un lot de matériaux.

Ainsi, la distribution de Poisson aide à faire des prévisions probabilistes sur l'occurrence d'événements rares ou aléatoires sur des intervalles de temps ou d'espace.

$$  
E(X) = \\lambda \\\\  
\\text{Var}(X) = \\lambda  
$$

Par exemple, la distribution de Poisson peut être utilisée pour modéliser le nombre de clients arrivant dans un magasin entre 19h et 22h, ou le nombre de patients arrivant dans une salle d'urgence entre 23h et minuit.

La figure ci-dessous visualise un exemple de distribution de Poisson où nous comptons le nombre de visiteurs Web arrivant sur le site Web où le taux d'arrivée, lambda, est supposé être égal à 7 minutes.

![1-pMhbq88yZEp4gGFYhId82Q](https://www.freecodecamp.org/news/content/images/2024/04/1-pMhbq88yZEp4gGFYhId82Q.png)

Génération aléatoire à partir d'une distribution de Poisson avec lambda = 7. Source de l'image : [LunarTech][38]

Dans l'analyse de données pratique, il est souvent utile de simuler la distribution d'événements. Voici un extrait de code Python qui démontre comment générer une série de points de données qui suivent une distribution de Poisson en utilisant NumPy. Nous créons ensuite un histogramme en utilisant Matplotlib pour visualiser la distribution du nombre de visiteurs (à titre d'exemple) auxquels nous pourrions nous attendre, sur la base de notre taux moyen λ = 7.

Cet histogramme aide à comprendre la forme et la variabilité de la distribution. Le nombre de visiteurs le plus probable se situe autour de la moyenne λ, mais la distribution montre également la probabilité d'en voir un nombre inférieur ou supérieur.

```python
# Génération aléatoire de 1000 échantillons de Poisson indépendants
import numpy as np
lambda_ = 7
N = 1000
X = np.random.poisson(lambda_,N)

# Histogramme de la distribution de Poisson
import matplotlib.pyplot as plt
counts, bins, ignored = plt.hist(X, 50, density = True, color = 'purple')
plt.title("Génération aléatoire à partir d'une distribution de Poisson avec lambda = 7")
plt.xlabel("Nombre de visiteurs")
plt.ylabel("Probabilité")
plt.show()
```

### Distribution normale

[La distribution de probabilité normale][39] est la distribution de probabilité continue pour une variable aléatoire à valeur réelle. La distribution normale, également appelée **distribution gaussienne**, est sans doute l'une des fonctions de distribution les plus populaires, couramment utilisée dans les sciences sociales et naturelles à des fins de modélisation. Par exemple, elle est utilisée pour modéliser la taille des personnes ou les scores aux tests.

Supposons qu'une variable aléatoire X suive une distribution normale. Alors sa fonction de densité de probabilité peut être exprimée comme suit :

$$  
\\Pr(X = k) = \\frac{1}{\\sigma\\sqrt{2\\pi}} e^{-\\frac{1}{2} \\left(\\frac{x-\\mu}{\\sigma}\\right)^2}  
$$

où le paramètre **μ** (mu) est la moyenne de la distribution, également appelée **paramètre de position**, le paramètre **σ** (sigma) est l'écart-type de la distribution, également appelé **paramètre d'échelle**. Le nombre [**π**][40] (pi) est une constante mathématique approximativement égale à 3,14.

#### Moyenne et variance de la distribution normale

$$  
E(X) = \\mu \\\\  
\\text{Var}(X) = \\sigma^2  
$$

La figure ci-dessous visualise un exemple de distribution normale avec une moyenne de 0 (**μ = 0**) et un écart-type de 1 (**σ = 1**), appelée distribution **normale centrée réduite** qui est symétrique.

![1-T_jAWtNjpf5lx29TbqwigQ](https://www.freecodecamp.org/news/content/images/2024/04/1-T_jAWtNjpf5lx29TbqwigQ.png)

Génération aléatoire de 1000 obs à partir d'une distribution normale (mu = 0, sigma = 1). Source de l'image : [LunarTech][41]

La visualisation de la distribution normale centrée réduite est cruciale car cette distribution sous-tend de nombreuses méthodes statistiques et la théorie des probabilités. Lorsque les données sont normalement distribuées avec une moyenne ( μ ) de 0 et un écart-type (σ) de 1, on parle de distribution normale centrée réduite. Elle est symétrique autour de la moyenne, et la forme de la courbe est souvent appelée "courbe en cloche" en raison de sa forme caractéristique.

La distribution normale centrée réduite est fondamentale pour les raisons suivantes :

-   **Théorème Central Limite :** Ce théorème stipule que, sous certaines conditions, la somme d'un grand nombre de variables aléatoires sera approximativement distribuée normalement. Il permet d'utiliser la théorie des probabilités normales pour les moyennes et les sommes d'échantillons, même lorsque les données originales ne sont pas normalement distribuées.
-   **Z-Scores :** Les valeurs de n'importe quelle distribution normale peuvent être transformées en distribution normale centrée réduite à l'aide des Z-scores, qui indiquent à combien d'écarts-types un élément se trouve par rapport à la moyenne. Cela permet de comparer des scores provenant de différentes distributions normales.
-   **Inférence statistique et tests A/B :** De nombreux tests statistiques, tels que les tests t et les ANOVA, supposent que les données suivent une distribution normale ou s'appuient sur le théorème central limite. Comprendre la distribution normale centrée réduite aide à interpréter les résultats de ces tests.
-   **Intervalles de confiance et tests d'hypothèses :** Les propriétés de la distribution normale centrée réduite sont utilisées pour construire des intervalles de confiance et effectuer des tests d'hypothèses.

Tous ces sujets seront abordés ci-dessous !

Ainsi, être capable de visualiser et de comprendre la distribution normale centrée réduite est essentiel pour appliquer avec précision de nombreuses techniques statistiques.

Le code Python ci-dessous utilise NumPy pour générer 1000 échantillons aléatoires à partir d'une distribution normale avec une moyenne (μ) de 0 et un écart-type (σ) de 1, qui sont les paramètres standards de la distribution normale centrée réduite. Ces échantillons générés sont stockés dans la variable X.

Pour visualiser la distribution de ces échantillons, le code utilise Matplotlib pour créer un histogramme. La fonction `plt.hist` est utilisée pour tracer l'histogramme des échantillons avec 30 bins, et le paramètre `density` est réglé sur `True` pour normaliser l'histogramme afin que l'aire sous celui-ci soit égale à 1. Cela transforme efficacement l'histogramme en un tracé de densité de probabilité.

De plus, la bibliothèque SciPy est utilisée pour superposer la fonction de densité de probabilité (PDF) de la distribution normale théorique sur l'histogramme. La fonction `norm.pdf` génère les valeurs y pour la PDF étant donné un tableau de valeurs x. Cette courbe théorique est tracée en jaune sur l'histogramme pour montrer à quel point les échantillons aléatoires correspondent à la distribution attendue.

Le graphique résultant affiche l'histogramme des échantillons générés en violet, avec la distribution normale théorique superposée en jaune. L'axe des x représente la plage de valeurs que les échantillons peuvent prendre, tandis que l'axe des y représente la densité de probabilité. Cette visualisation est un outil puissant pour comparer la distribution empirique des données avec le modèle théorique, nous permettant de voir si nos échantillons suivent le motif attendu d'une distribution normale.

```python
# Génération aléatoire de 1000 échantillons normaux indépendants
import numpy as np
mu = 0
sigma = 1
N = 1000
X = np.random.normal(mu,sigma,N)

# Distribution de la population
from scipy.stats import norm
x_values = np.arange(-5,5,0.01)
y_values = norm.pdf(x_values)
# Histogramme de l'échantillon avec distribution de la population
import matplotlib.pyplot as plt
counts, bins, ignored = plt.hist(X, 30, density = True,color = 'purple',label = 'Distribution d\'échantillonnage')
plt.plot(x_values,y_values, color = 'y',linewidth = 2.5,label = 'Distribution de la population')
plt.title("Génération aléatoire de 1000 obs à partir d'une distribution normale mu = 0 sigma = 1")
plt.ylabel("Probabilité")
plt.legend()
plt.show()
```

## Théorème de Bayes

Le théorème de Bayes (souvent appelé **loi de Bayes**) est sans doute la règle la plus puissante des probabilités et des statistiques. Il porte le nom du célèbre statisticien et philosophe anglais, Thomas Bayes.

![0-ypJ6xW1FA_Lh7Faw](https://www.freecodecamp.org/news/content/images/2024/04/0-ypJ6xW1FA_Lh7Faw.gif)

Le mathématicien et philosophe anglais Thomas Bayes

Le théorème de Bayes est une loi de probabilité puissante qui introduit le concept de **subjectivité** dans le monde des statistiques et des mathématiques où tout est question de faits. Il décrit la probabilité d'un événement, basée sur l'information préalable des **conditions** qui pourraient être liées à cet événement.

Par exemple, si l'on sait que le risque de contracter le Coronavirus ou la Covid-19 augmente avec l'âge, le théorème de Bayes permet de déterminer plus précisément le risque pour un individu d'un âge connu. Il le fait en le conditionnant sur l'âge plutôt qu'en supposant simplement que cet individu est représentatif de la population dans son ensemble.

Le concept de **probabilité conditionnelle**, qui joue un rôle central dans le théorème de Bayes, est une mesure de la probabilité qu'un événement se produise, étant donné qu'un autre événement s'est déjà produit.

Le théorème de Bayes peut être décrit par l'expression suivante où X et Y représentent respectivement les événements X et Y :

$$ \\Pr(X | Y) = \\frac{\\Pr(Y | X) \\Pr(X)}{\\Pr(Y)} $$

-   _Pr_ (X|Y) : la probabilité que l'événement X se produise étant donné que l'événement ou la condition Y s'est produit ou est vrai.
-   _Pr_ (Y|X) : la probabilité que l'événement Y se produise étant donné que l'événement ou la condition X s'est produit ou est vrai.
-   _Pr_ (X) & _Pr_ (Y) : les probabilités d'observer respectivement les événements X et Y.

Dans le cas de l'exemple précédent, la probabilité de contracter le Coronavirus (événement X) conditionnelle au fait d'avoir un certain âge est _Pr_ (X|Y). Elle est égale à la probabilité d'avoir un certain âge étant donné que la personne a contracté le Coronavirus, _Pr_ (Y|X), multipliée par la probabilité de contracter le Coronavirus, _Pr_ (X), divisée par la probabilité d'avoir un certain âge, _Pr_ (Y).

## Régression linéaire

Précédemment, nous avons introduit le concept de causalité entre variables, qui se produit lorsqu'une variable a un impact direct sur une autre variable.

Lorsque la relation entre deux variables est linéaire, la régression linéaire est une méthode statistique qui peut aider à modéliser l'impact d'un changement unitaire d'une variable, **la variable indépendante**, sur les valeurs d'une autre variable, **la variable dépendante**.

Les variables dépendantes sont souvent appelées **variables de réponse** ou **variables expliquées**, tandis que les variables indépendantes sont souvent appelées **régresseurs** ou **variables explicatives**.

Lorsque le modèle de régression linéaire est basé sur une seule variable indépendante, on parle de **régression linéaire simple**. Lorsque le modèle est basé sur plusieurs variables indépendantes, on parle de **régression linéaire multiple.**

La régression linéaire simple peut être décrite par l'expression suivante :

$$ Y\_i = \\beta\_0 + \\beta\_1X\_i + u\_i $$

où **Y** est la variable dépendante, **X** est la variable indépendante qui fait partie des données, **β0** est l'ordonnée à l'origine (intercept) qui est inconnue et constante, **β1** est le coefficient de pente ou un paramètre correspondant à la variable X qui est également inconnu et constant. Enfin, **u** est le terme d'erreur que le modèle commet lors de l'estimation des valeurs de Y.

L'idée principale derrière la régression linéaire est de trouver la droite la mieux ajustée, **la droite de régression**, à travers un ensemble de paires de données ( X, Y ).

Un exemple d'application de la régression linéaire est la modélisation de l'impact de la longueur des nageoires sur la masse corporelle des manchots, visualisée ci-dessous :

![1-cS-5_yS2xa--V97U1RoAIQ](https://www.freecodecamp.org/news/content/images/2024/04/1-cS-5_yS2xa--V97U1RoAIQ.png)

Source de l'image : [LunarTech][42]

L'extrait de code R que vous avez partagé sert à créer un diagramme de dispersion avec une droite de régression linéaire en utilisant le package `ggplot2` en R, qui est une bibliothèque puissante et largement utilisée pour créer des graphiques et des visualisations. Le code utilise un jeu de données nommé `penguins` du package `palmerpenguins`, contenant vraisemblablement des données sur les espèces de manchots, incluant des mesures comme la longueur des nageoires et la masse corporelle.

```python
# Code R pour le graphique
install.packages("ggplot2")
install.packages("palmerpenguins")
library(palmerpenguins)
library(ggplot2)
View(data(penguins))
ggplot(data = penguins, aes(x = flipper_length_mm,y = body_mass_g))+
  geom_smooth(method = "lm", se = FALSE, color = 'purple')+
  geom_point()+
  labs(x="Longueur des nageoires (mm)",y="Masse corporelle (g)")
```

La régression linéaire multiple avec trois variables indépendantes peut être décrite par l'expression suivante :

$$ Y\_i = \\beta\_0 + \\beta\_1X\_{1,i} + \\beta\_2X\_{2,i} + \\beta\_3X\_{3,i} + u\_i $$

### Moindres carrés ordinaires

La méthode des moindres carrés ordinaires (MCO) est une méthode d'estimation des paramètres inconnus tels que β0 et β1 dans un modèle de régression linéaire. Le modèle est basé sur le principe des **moindres carrés**. Cela minimise la somme des carrés des différences entre la variable dépendante observée et ses valeurs prédites par la fonction linéaire de la variable indépendante (souvent appelées **valeurs ajustées**).

Cette différence entre les valeurs réelles et prédites de la variable dépendante Y est appelée **résidu**. Ainsi, les MCO minimisent la somme des carrés des résidus.

Ce problème d'optimisation aboutit aux estimations MCO suivantes pour les paramètres inconnus β0 et β1, également connues sous le nom d'**estimations des coefficients** :

$$ \\hat{\\beta}_1 = \\frac{\\sum_{i=1}^{N} (X\_i - \\bar{X})(Y\_i - \\bar{Y})}{\\sum\_{i=1}^{N} (X\_i - \\bar{X})^2} $$

$$ \\hat{\\beta}\_0 = \\bar{Y} - \\hat{\\beta}\_1\\bar{X} $$

Une fois ces paramètres du modèle de régression linéaire simple estimés, les **valeurs ajustées** de la variable de réponse peuvent être calculées comme suit :

$$ \\hat{Y}\_i = \\hat{\\beta}\_0 + \\hat{\\beta}\_1X\_i $$

### Erreur type

Les **résidus** ou les termes d'erreur estimés peuvent être déterminés comme suit :

$$ \\hat{u}\_i = Y\_i - \\hat{Y}\_i $$

Il est important de garder à l'esprit la différence entre les termes d'erreur et les résidus. Les termes d'erreur ne sont jamais observés, tandis que les résidus sont calculés à partir des données. Les MCO estiment les termes d'erreur pour chaque observation mais pas le terme d'erreur réel. Ainsi, la variance réelle de l'erreur reste inconnue.

De plus, ces estimations sont sujettes à l'incertitude d'échantillonnage. Cela signifie que nous ne serons jamais en mesure de déterminer l'estimation exacte, la valeur réelle, de ces paramètres à partir de données échantillonnales dans une application empirique. Mais nous pouvons l'estimer en calculant la **variance résiduelle de l'échantillon** en utilisant les résidus comme suit :

$$ \\hat{\\sigma}^2 = \\frac{\\sum\_{i=1}^{N} \\hat{u}\_i^2}{N - 2} $$

Cette estimation de la variance des résidus de l'échantillon nous aide à estimer la variance des paramètres estimés, qui est souvent exprimée comme suit :

$$ \\text{Var}(\\hat{\\beta}) $$

La racine carrée de ce terme de variance est appelée **l'erreur type** de l'estimation. C'est un composant clé pour évaluer la précision des estimations des paramètres. Elle est utilisée pour calculer les statistiques de test et les intervalles de confiance.

L'erreur type peut être exprimée comme suit :

$$ SE(\\hat{\\beta}) = \\sqrt{\\text{Var}(\\hat{\\beta})} $$

Il est important de garder à l'esprit la différence entre les termes d'erreur et les résidus. Les termes d'erreur ne sont jamais observés, tandis que les résidus sont calculés à partir des données.

#### Hypothèses des MCO

La méthode d'estimation des MCO repose sur les hypothèses suivantes qui doivent être satisfaites pour obtenir des résultats de prédiction fiables :

1.  L'hypothèse de **linéarité** stipule que le modèle est linéaire dans ses paramètres.
2.  L'hypothèse d'**échantillon aléatoire** stipule que toutes les observations de l'échantillon sont sélectionnées de manière aléatoire.
3.  L'hypothèse d'**exogénéité** stipule que les variables indépendantes ne sont pas corrélées avec les termes d'erreur.
4.  L'hypothèse d'**homoscédasticité** stipule que la variance de tous les termes d'erreur est constante.
5.  L'hypothèse de **non-multicolinéarité parfaite** stipule qu'aucune des variables indépendantes n'est constante et qu'il n'y a pas de relations linéaires exactes entre les variables indépendantes.

L'extrait de code Python que vous avez partagé effectue une régression par les moindres carrés ordinaires (MCO), une méthode utilisée en statistiques pour estimer la relation entre des variables indépendantes et une variable dépendante. Ce processus consiste à calculer la droite la mieux ajustée à travers les points de données qui minimise la somme des carrés des différences entre les valeurs observées et les valeurs prédites par le modèle.

Le code définit une fonction `runOLS(Y, X)` qui prend une variable dépendante `Y` et une variable indépendante `X` et effectue les étapes suivantes :

1.  Estime les coefficients MCO (`beta_hat`) en utilisant la solution d'algèbre linéaire au problème des moindres carrés.
2.  Effectue des prédictions (`Y_hat`) en utilisant les coefficients estimés et calcule les résidus.
3.  Calcule la somme des carrés des résidus (RSS), la somme totale des carrés (TSS), l'erreur quadratique moyenne (MSE), la racine de l'erreur quadratique moyenne (RMSE) et la valeur du R-carré, qui sont des métriques courantes utilisées pour évaluer l'ajustement du modèle.
4.  Calcule l'erreur type des estimations des coefficients, les statistiques t, les p-values et les intervalles de confiance pour les coefficients estimés.

Ces calculs sont standards dans l'analyse de régression et sont utilisés pour interpréter et comprendre la force et la signification de la relation entre les variables. Le résultat de cette fonction inclut les coefficients estimés et diverses statistiques qui aident à évaluer les performances du modèle.

```python
def runOLS(Y,X):

   # Estimation MCO Y = Xb + e --> beta_hat = (X'X)^-1(X'Y)
   beta_hat = np.dot(np.linalg.inv(np.dot(np.transpose(X), X)), np.dot(np.transpose(X), Y))

   # Prédiction MCO
   Y_hat = np.dot(X,beta_hat)
   residuals = Y-Y_hat
   RSS = np.sum(np.square(residuals))
   sigma_squared_hat = RSS/(N-2)
   TSS = np.sum(np.square(Y-np.repeat(Y.mean(),len(Y))))
   MSE = sigma_squared_hat
   RMSE = np.sqrt(MSE)
   R_squared = (TSS-RSS)/TSS

   # Erreur type des estimations : racine carrée de la variance de l'estimation
   var_beta_hat = np.linalg.inv(np.dot(np.transpose(X),X))*sigma_squared_hat
   
   SE = []
   t_stats = []
   p_values = []
   CI_s = []
   
   for i in range(len(beta)):
       # erreurs types
       SE_i = np.sqrt(var_beta_hat[i,i])
       SE.append(np.round(SE_i,3))

        # statistiques t
        t_stat = np.round(beta_hat[i,0]/SE_i,3)
        t_stats.append(t_stat)

        # p-value de la statistique t p[|t_stat| >= t-seuil bilatéral] 
        p_value = t.sf(np.abs(t_stat),N-2) * 2
        p_values.append(np.round(p_value,3))

        # Intervalles de confiance = beta_hat -+ marge_d_erreur
        t_critical = t.ppf(q =1-0.05/2, df = N-2)
        margin_of_error = t_critical*SE_i
        CI = [np.round(beta_hat[i,0]-margin_of_error,3), np.round(beta_hat[i,0]+margin_of_error,3)]
        CI_s.append(CI)
        return(beta_hat, SE, t_stats, p_values,CI_s, 
               MSE, RMSE, R_squared)
```

## Propriétés des paramètres

Sous l'hypothèse que les critères/hypothèses MCO que nous venons de discuter sont satisfaits, les estimateurs MCO des coefficients β0 et β1 sont **BLUE** et **convergents**. Alors, qu'est-ce que cela signifie ?

### Théorème de Gauss-Markov

Ce théorème met en évidence les propriétés des estimations MCO où le terme **BLUE** signifie **Best Linear Unbiased Estimator** (Meilleur estimateur linéaire non biaisé). Explorons ce que cela signifie plus en détail.

#### Biais

Le **biais** d'un estimateur est la différence entre sa valeur attendue et la valeur réelle du paramètre estimé. Il peut être exprimé comme suit :

$$ \\text{Bias}(\\beta, \\hat{\\beta}) = E(\\hat{\\beta}) - \\beta $$

Lorsque nous affirmons que l'estimateur est **non biaisé**, nous voulons dire que le biais est égal à zéro. Cela implique que la valeur attendue de l'estimateur est égale à la valeur réelle du paramètre, soit :

$$ E(\\hat{\\beta}) = \\beta $$

L'absence de biais ne garantit pas que l'estimation obtenue avec un échantillon particulier soit égale ou proche de β. Ce que cela signifie, c'est que si nous tirons **répétitivement** des échantillons aléatoires de la population et calculons l'estimation à chaque fois, alors la moyenne de ces estimations serait égale ou très proche de β.

#### Efficacité

Le terme **Best** (Meilleur) dans le théorème de Gauss-Markov se rapporte à la variance de l'estimateur et est appelé **efficacité**. Un paramètre peut avoir plusieurs estimateurs, mais celui qui possède la variance la plus faible est dit efficace.

#### Convergence

Le terme de convergence va de pair avec les termes **taille de l'échantillon** et **convergence**. Si l'estimateur converge vers le paramètre réel à mesure que la taille de l'échantillon devient très grande, alors cet estimateur est dit convergent, soit :

$$ N \\to \\infty \\text{ alors } \\hat{\\beta} \\to \\beta $$

Toutes ces propriétés s'appliquent aux estimations MCO, comme le résume le théorème de Gauss-Markov. En d'autres termes, les estimations MCO ont la variance la plus petite, sont non biaisées, linéaires dans leurs paramètres et convergentes. Ces propriétés peuvent être prouvées mathématiquement en utilisant les hypothèses MCO formulées précédemment.

## Intervalles de confiance

L'intervalle de confiance est la plage qui contient le paramètre réel de la population avec une certaine probabilité pré-spécifiée. On parle alors de **niveau de confiance** de l'expérience, et on l'obtient en utilisant les résultats de l'échantillon et la **marge d'erreur**.

### Marge d'erreur

La marge d'erreur est la différence entre les résultats de l'échantillon et ce qu'aurait été le résultat si vous aviez utilisé la population entière.

### Niveau de confiance

Le niveau de confiance décrit le degré de certitude des résultats expérimentaux. Par exemple, un niveau de confiance de 95 % signifie que si vous deviez effectuer la même expérience de manière répétée 100 fois, 95 de ces 100 essais mèneraient à des résultats similaires.

Notez que le niveau de confiance est défini avant le début de l'expérience car il affectera l'importance de la marge d'erreur à la fin de l'expérience.

### Intervalle de confiance pour les estimations MCO

Comme je l'ai mentionné précédemment, les estimations MCO de la régression linéaire simple, les estimations de l'ordonnée à l'origine β0 et du coefficient de pente β1, sont sujettes à l'incertitude d'échantillonnage. Mais nous pouvons construire des intervalles de confiance (IC) pour ces paramètres qui contiendront la valeur réelle de ces paramètres dans 95 % de tous les échantillons.

C'est-à-dire qu'un intervalle de confiance à 95 % pour β peut être interprété comme suit :

-   L'intervalle de confiance est l'ensemble des valeurs pour lesquelles un test d'hypothèse ne peut pas être rejeté au seuil de 5 %.
-   L'intervalle de confiance a 95 % de chances de contenir la valeur réelle de β.

L'intervalle de confiance à 95 % des estimations MCO peut être construit comme suit :

$$ CI\_{0.95}^{\\beta} = \\left\[\\hat{\\beta}\_i - 1,96 \\times SE(\\hat{\\beta}\_i), \\hat{\\beta}\_i + 1,96 \\times SE(\\hat{\\beta}\_i)\\right\] $$

Ceci est basé sur l'estimation du paramètre, l'erreur type de cette estimation et la valeur 1,96 représentant la marge d'erreur correspondant à la règle de rejet de 5 %.

Cette valeur est déterminée à l'aide de la [table de distribution normale][43], dont nous discuterons plus tard dans ce guide.

En attendant, la figure suivante illustre l'idée de l'IC à 95 % :

![1-XtBhY43apW_xIyf23eOWow](https://www.freecodecamp.org/news/content/images/2024/04/1-XtBhY43apW_xIyf23eOWow.png)

Source de l'image : [LunarTech][44]

Notez que l'intervalle de confiance dépend également de la taille de l'échantillon, étant donné qu'il est calculé à l'aide de l'erreur type qui est basée sur la taille de l'échantillon.

## Tests d'hypothèses statistiques

Tester une hypothèse en statistiques est un moyen de tester les résultats d'une expérience ou d'une enquête pour déterminer leur degré de signification.

Fondamentalement, vous testez si les résultats obtenus sont valides en calculant les probabilités que les résultats se soient produits par hasard. Si c'est le cas, alors les résultats ne sont pas fiables, pas plus que l'expérience. Le test d'hypothèse fait partie de l'**inférence statistique**.

### Hypothèse nulle et alternative

Tout d'abord, vous devez déterminer la thèse que vous souhaitez tester. Ensuite, vous devez formuler l'**hypothèse nulle** et l'**hypothèse alternative.** Le test peut avoir deux résultats possibles. Sur la base des résultats statistiques, vous pouvez soit rejeter l'hypothèse énoncée, soit l'accepter.

En règle générale, les statisticiens ont tendance à placer dans l'hypothèse nulle la version ou la formulation de l'hypothèse qui doit être rejetée, tandis que la version acceptable et souhaitée est énoncée dans l'hypothèse alternative.

### Signification statistique

Regardons l'exemple mentionné précédemment où nous avons utilisé le modèle de régression linéaire pour étudier si la longueur des nageoires d'un manchot (variable indépendante) a un impact sur sa masse corporelle (variable dépendante).

Nous pouvons formuler ce modèle avec l'expression statistique suivante :

$$ Y\_{\\text{MasseCorporelle}} = \\beta\_0 + \\beta\_1X\_{\\text{LongueurNageoire}} + u\_i $$

Ensuite, une fois les estimations MCO des coefficients calculées, nous pouvons formuler l'hypothèse nulle et l'hypothèse alternative suivantes pour tester si la longueur des nageoires a un impact **statistiquement significatif** sur la masse corporelle :

![1-DVPqyel26EtGY__fwp_-rA](https://www.freecodecamp.org/news/content/images/2024/04/1-DVPqyel26EtGY__fwp_-rA.png)

où H0 et H1 représentent respectivement l'hypothèse nulle et l'hypothèse alternative.

Rejeter l'hypothèse nulle signifierait qu'une augmentation d'une unité de la longueur des nageoires a un impact direct sur la masse corporelle (étant donné que l'estimation du paramètre β1 décrit cet impact de la variable indépendante, la longueur des nageoires, sur la variable dépendante, la masse corporelle). Nous pouvons reformuler cette hypothèse comme suit :

$$  
\\begin{cases}  
H\_0: \\hat{\\beta}\_1 = 0 \\\\  
H\_1: \\hat{\\beta}\_1 \\neq 0  
\\end{cases}  
$$

où H0 stipule que l'estimation du paramètre β1 est égale à 0, c'est-à-dire que l'effet de la longueur des nageoires sur la masse corporelle est **statistiquement insignifiant**, tandis que H1 stipule que l'estimation du paramètre β1 n'est pas égale à 0, suggérant que l'effet de la longueur des nageoires sur la masse corporelle est **statistiquement significatif**.

### Erreurs de type I et de type II

Lors de l'exécution de tests d'hypothèses statistiques, vous devez prendre en compte deux types conceptuels d'erreurs : l'erreur de type I et l'erreur de type II.

Les erreurs de type I se produisent lorsque l'hypothèse nulle est rejetée à tort, et les erreurs de type II se produisent lorsque l'hypothèse nulle n'est pas rejetée à tort. Une [matrice][45] de confusion peut vous aider à visualiser clairement la gravité de ces deux types d'erreurs.

En règle générale, les statisticiens ont tendance à placer dans l'hypothèse nulle la version de l'hypothèse qui doit être rejetée, tandis que la version acceptable et souhaitée est énoncée dans l'hypothèse alternative.

## Tests statistiques

Une fois que vous avez énoncé les hypothèses nulle et alternative et défini les hypothèses du test, l'étape suivante consiste à déterminer quel test statistique est approprié et à calculer la **statistique de test**.

Le rejet ou le non-rejet de l'hypothèse nulle peut être déterminé en comparant la statistique de test avec la **valeur critique**. Cette comparaison montre si la statistique de test observée est plus extrême que la valeur critique définie.

Elle peut avoir deux résultats possibles :

-   La statistique de test est plus extrême que la valeur critique → l'hypothèse nulle peut être rejetée.
-   La statistique de test n'est pas aussi extrême que la valeur critique → l'hypothèse nulle ne peut pas être rejetée.

La valeur critique est basée sur un **niveau de signification α** pré-spécifié (généralement choisi égal à 5 %) et le type de distribution de probabilité que suit la statistique de test.

La valeur critique divise l'aire sous cette courbe de distribution de probabilité en **région(s) de rejet** et **région de non-rejet**. Il existe de nombreux tests statistiques utilisés pour tester diverses hypothèses. Des exemples de tests statistiques sont le [test t de Student][46], le [test F][47], le [test du Khi-deux][48], le [test d'endogénéité de Durbin-Hausman-Wu][49], le [test d'hétéroscédasticité de White][50]. Dans ce guide, nous examinerons deux de ces tests statistiques : le test t de Student et le test F.

### Test t de Student

L'un des tests statistiques les plus simples et les plus populaires est le test t de Student. Vous pouvez l'utiliser pour tester diverses hypothèses, en particulier lorsqu'il s'agit d'une hypothèse dont l'intérêt principal est de trouver des preuves d'un effet statistiquement significatif d'une **seule variable**.

La statistique de test du test t suit la [**distribution t de Student**][51] et peut être déterminée comme suit :

$$ T\_{\\text{stat}} = \\frac{\\hat{\\beta}\_i - h\_0}{SE(\\hat{\\beta})} $$

où h0 au numérateur est la valeur par rapport à laquelle l'estimation du paramètre est testée. Ainsi, les statistiques du test t sont égales à l'estimation du paramètre moins la valeur hypothétique divisée par l'erreur type de l'estimation du coefficient.

Utilisons cela pour notre hypothèse précédente, où nous voulions tester si la longueur des nageoires a un impact statistiquement significatif sur la masse corporelle ou non. Ce test peut être effectué à l'aide d'un test t. Le h0 est dans ce cas égal à 0 puisque l'estimation du coefficient de pente est testée par rapport à une valeur de 0.

#### Test t bilatéral vs unilatéral

Il existe deux versions du test t : le **test t bilatéral** et le **test t unilatéral**. Le choix de l'une ou l'autre version du test dépend entièrement de l'hypothèse que vous souhaitez tester.

Vous pouvez utiliser le test t bilatéral (ou **à deux queues**) lorsque l'hypothèse teste une relation d'égalité par rapport à une relation d'inégalité sous les hypothèses nulle et alternative. Cela ressemblerait à l'exemple suivant :

$$  
H\_{0} = \\hat{\\beta}\_1 = h\_0\\  
H\_{1} = \\hat{\\beta}\_1 \\neq h\_0  
$$

Le test t bilatéral possède **deux régions de rejet**, comme visualisé dans la figure ci-dessous :

![1-otgnlBKy306KgrFUZxk0Og](https://www.freecodecamp.org/news/content/images/2024/04/1-otgnlBKy306KgrFUZxk0Og.png)

Source de l'image : [_Hartmann, K., Krois, J., Waske, B. (2018): E-Learning Project SOGA: Statistics and Geospatial Data Analysis. Department of Earth Sciences, Freie Universitaet Berlin_][52]

Dans cette version du test t, l'hypothèse nulle est rejetée si la statistique t calculée est soit trop petite, soit trop grande.

$$ T\_{\\text{stat}} < -t\_{\\alpha,N} \\text{ ou } T\_{\\text{stat}} > t\_{\\alpha,N} $$

$$ |T\_{\\text{stat}}| > t\_{\\alpha,N} $$

Ici, les statistiques de test sont comparées aux valeurs critiques basées sur la taille de l'échantillon et le niveau de signification choisi. Pour déterminer la valeur exacte du point de coupure, vous pouvez utiliser une [table de distribution t bilatérale][53].

D'un autre côté, vous pouvez utiliser le test t unilatéral (ou **à une seule queue**) lorsque l'hypothèse teste des relations positives/négatives par rapport à des relations négatives/positives sous les hypothèses nulle et alternative. Cela ressemble à ceci :

![1-uKChnDWApLtrCf8bq13o4w](https://www.freecodecamp.org/news/content/images/2024/04/1-uKChnDWApLtrCf8bq13o4w.png)

Queue à gauche vs queue à droite

Le test t unilatéral possède une **seule région de rejet**. Selon le côté de l'hypothèse, la région de rejet se trouve soit sur le côté gauche, soit sur le côté droit, comme visualisé dans la figure ci-dessous :

![1-SVKBOOFtXIvYwL2gC9XEoQ](https://www.freecodecamp.org/news/content/images/2024/04/1-SVKBOOFtXIvYwL2gC9XEoQ.png)

Source de l'image : [_Hartmann, K., Krois, J., Waske, B. (2018): E-Learning Project SOGA: Statistics and Geospatial Data Analysis. Department of Earth Sciences, Freie Universitaet Berlin_][54]

Dans cette version du test t, l'hypothèse nulle est rejetée si la statistique t calculée est plus petite/plus grande que la valeur critique.

![1-UvLof79AQigLFgxbKAvYgA](https://www.freecodecamp.org/news/content/images/2024/04/1-UvLof79AQigLFgxbKAvYgA.png)

### Test F

Le test F est un autre test statistique très populaire, souvent utilisé pour tester des hypothèses portant sur la **signification statistique conjointe de plusieurs variables**. C'est le cas lorsque vous souhaitez tester si plusieurs variables indépendantes ont un impact statistiquement significatif sur une variable dépendante.

Voici un exemple d'hypothèse statistique que vous pouvez tester à l'aide du test F :

$$  
\\begin{cases}  
H\_0: \\hat{\\beta}\_1 = \\hat{\\beta}\_2 = \\hat{\\beta}\_3 = 0 \\\\  
H\_1: \\hat{\\beta}\_1 \\neq \\hat{\\beta}\_2 \\neq \\hat{\\beta}\_3 \\neq 0  
\\end{cases}  
$$

où l'hypothèse nulle stipule que les trois variables correspondant à ces coefficients sont conjointement statistiquement insignifiantes, et l'alternative stipule que ces trois variables sont conjointement statistiquement significatives.

La statistique de test du test F suit la [distribution F][55] et peut être déterminée comme suit :

$$ F\_{\\text{stat}} = \\frac{(SSR\_{\\text{restreint}} - SSR\_{\\text{non restreint}}) / q}{SSR\_{\\text{non restreint}} / (N - k\_{\\text{non restreint}} - 1)} $$

où :

-   le SSRrestreint est la **somme des carrés des résidus** du **modèle restreint**, qui est le même modèle excluant des données les variables cibles déclarées insignifiantes sous l'hypothèse nulle.
-   le SSRnon restreint est la somme des carrés des résidus du **modèle non restreint**, qui est le modèle incluant toutes les variables.
-   le q représente le nombre de variables testées conjointement pour l'insignifiance sous l'hypothèse nulle.
-   N est la taille de l'échantillon.
-   et k est le nombre total de variables dans le modèle non restreint.

Les valeurs SSR sont fournies à côté des estimations des paramètres après l'exécution de la régression MCO, et il en va de même pour la statistique F.

Voici un exemple de sortie de modèle MLR où les valeurs SSR et de statistique F sont marquées.

![1-5kTyYIc3LztrgM-oLKltwg](https://www.freecodecamp.org/news/content/images/2024/04/1-5kTyYIc3LztrgM-oLKltwg.png)

Source de l'image : [Stock and Whatson][56]

Le test F possède **une seule région de rejet**, comme visualisé ci-dessous :

![1-U3c2dRBPYCqtDqNGvk1BKA](https://www.freecodecamp.org/news/content/images/2024/04/1-U3c2dRBPYCqtDqNGvk1BKA.jpg)

Source de l'image : [_U of Michigan_][57]

Si la statistique F calculée est supérieure à la valeur critique, alors l'hypothèse nulle peut être rejetée. Cela suggère que les variables indépendantes sont conjointement statistiquement significatives. La règle de rejet peut être exprimée comme suit :

$$ F\_{\\text{stat}} > F\_{\\alpha,q,N} $$

## Test t à 2 échantillons

Si vous souhaitez tester s'il existe une différence statistiquement significative entre les métriques des groupes de contrôle et expérimentaux qui se présentent sous forme de moyennes (par exemple, le montant moyen des achats), et que la métrique suit la distribution _t de Student_. Lorsque la taille de l'échantillon est inférieure à 30, vous pouvez utiliser le test t à 2 échantillons pour tester l'hypothèse suivante :

$$  
\\begin{cases}  
H\_0: \\mu\_{\\text{con}} = \\mu\_{\\text{exp}} \\\\  
H\_1: \\mu\_{\\text{con}} \\neq \\mu\_{\\text{exp}}  
\\end{cases}  
$$  
  
$$  
\\begin{cases}  
H\_0: \\mu\_{\\text{con}} - \\mu\_{\\text{exp}} = 0 \\\\  
H\_1: \\mu\_{\\text{con}} - \\mu\_{\\text{exp}} \\neq 0  
\\end{cases}  
$$

où la distribution d'échantillonnage des moyennes du groupe de contrôle suit la distribution t de Student avec N_con-1 degrés de liberté. De même, la distribution d'échantillonnage des moyennes du groupe expérimental suit également la distribution t de Student avec N_exp-1 degrés de liberté.

Notez que N_con et N_exp sont respectivement le nombre d'utilisateurs dans les groupes de contrôle et expérimental.

$$ \\hat{\\mu}\_{\\text{con}} \\sim t(N\_{\\text{con}} - 1) $$  
  
$$ \\hat{\\mu}\_{\\text{exp}} \\sim t(N\_{\\text{exp}} - 1) $$

Ensuite, vous pouvez calculer une estimation de la **variance pondérée** (pooled variance) des deux échantillons comme suit :

$$ S^2\_{\\text{pooled}} = \\frac{(N\_{\\text{con}} - 1) \* \\sigma^2\_{\\text{con}} + (N\_{\\text{exp}} - 1) \* \\sigma^2\_{\\text{exp}}}{N\_{\\text{con}} + N\_{\\text{exp}} - 2} \* \\left(\\frac{1}{N\_{\\text{con}}} + \\frac{1}{N\_{\\text{exp}}}\\right) $$

où σ²_con et σ²_exp sont les variances d'échantillon des groupes de contrôle et expérimental, respectivement. Ensuite, l'**erreur type** est égale à la racine carrée de l'estimation de la variance pondérée, et peut être définie comme :

$$ SE = \\sqrt{\\hat{S}^2\_{\\text{pooled}}} $$

Par conséquent, la **statistique de test** du test t à 2 échantillons avec l'hypothèse énoncée précédemment peut être calculée comme suit :

$$ T = \\frac{\\hat{\\mu}\_{\\text{con}} - \\hat{\\mu}\_{\\text{exp}}}{\\sqrt{\\hat{S}^2\_{\\text{pooled}}}} $$

Afin de tester la **signification statistique** de la différence observée entre les moyennes d'échantillon, nous devons calculer la **p-value** de notre statistique de test.

La p-value est la probabilité d'observer des valeurs au moins aussi extrêmes que la valeur commune lorsque cela est dû au hasard. En d'autres termes, la p-value est la probabilité d'obtenir un effet au moins aussi extrême que celui de vos données échantillonnales, en supposant que l'hypothèse nulle soit vraie.

Ensuite, la p-value de la statistique de test peut être calculée comme suit :

$$ p\_{\\text{value}} = \\Pr\[t \\leq -T \\text{ ou } t \\geq T\] $$  
  
$$ = 2 \* \\Pr\[t \\geq T\] $$

L'interprétation d'une _p_-value dépend du niveau de signification choisi, alpha, que vous choisissez avant d'exécuter le test lors de l'_analyse de puissance_.

Si la _p_-value calculée s'avère inférieure ou égale à alpha (par exemple, 0,05 pour un niveau de signification de 5 %), nous pouvons rejeter l'hypothèse nulle et affirmer qu'il existe une différence statistiquement significative entre les métriques primaires des groupes de contrôle et expérimental.

Enfin, pour déterminer la précision des résultats obtenus et également pour commenter la signification pratique des résultats obtenus, vous pouvez calculer l'**intervalle de confiance** de votre test en utilisant la formule suivante :  
  
$$ CI = \\left\[ (\\hat{\\mu}\_{\\text{con}} - \\hat{\\mu}\_{\\text{exp}}) - t\_{\\frac{\\alpha}{2}} \* SE(\\hat{\\mu}\_{\\text{con}} - \\hat{\\mu}\_{\\text{exp}}), (\\hat{\\mu}\_{\\text{con}} - \\hat{\\mu}\_{\\text{exp}}) + t\_{\\frac{\\alpha}{2}} \* SE \\right\] $$

où t_(1-alpha/2) est la valeur critique du test correspondant au test t bilatéral avec un niveau de signification alpha. Elle peut être trouvée à l'aide de la [table t][58].

Le code Python fourni effectue un test t à deux échantillons, utilisé en statistiques pour déterminer si deux ensembles de données sont significativement différents l'un de l'autre. Cet extrait simule deux groupes (contrôle et expérimental) avec des données suivant une distribution t, calcule la moyenne et la variance pour chaque groupe, puis effectue les étapes suivantes :

1.  Il calcule la variance pondérée, qui est une moyenne pondérée des variances des deux groupes.
2.  Il calcule l'erreur type de la différence entre les deux moyennes.
3.  Il calcule la statistique t, qui est la différence entre les deux moyennes d'échantillon divisée par l'erreur type. Cette statistique mesure l'écart entre les groupes en unités d'erreur type.
4.  Il détermine la valeur t critique à partir de la distribution t pour le niveau de signification et les degrés de liberté donnés, ce qui est utilisé pour décider si la statistique t est suffisamment grande pour indiquer une différence statistiquement significative entre les groupes.
5.  Il calcule la p-value, qui indique la probabilité d'observer une telle différence entre les moyennes si l'hypothèse nulle (selon laquelle il n'y a pas de différence) est vraie.
6.  Il calcule la marge d'erreur et construit l'intervalle de confiance autour de la différence des moyennes.

Enfin, le code affiche la statistique t, la valeur t critique, la p-value et l'intervalle de confiance. Ces résultats peuvent être utilisés pour déduire si les différences observées dans les moyennes sont statistiquement significatives ou probablement dues à une variation aléatoire.

```python
import numpy as np
from scipy.stats import t

N_con = 20
df_con = N_con - 1 # degrés de liberté du groupe de contrôle 
N_exp = 20
df_exp = N_exp - 1 # degrés de liberté du groupe expérimental 

# Niveau de signification
alpha = 0.05

# données du groupe de contrôle avec distribution t
X_con = np.random.standard_t(df_con,N_con)
# données du groupe expérimental avec distribution t
X_exp = np.random.standard_t(df_exp,N_exp)

# moyenne du contrôle
mu_con = np.mean(X_con)
# moyenne de l'expérimental
mu_exp = np.mean(X_exp)

# variance du contrôle
sigma_sqr_con = np.var(X_con)
# variance de l'expérimental
sigma_sqr_exp = np.var(X_exp)

# variance pondérée
pooled_variance_t_test = ((N_con-1)*sigma_sqr_con + (N_exp -1) * sigma_sqr_exp)/(N_con + N_exp-2)*(1/N_con + 1/N_exp)

# Erreur type
SE = np.sqrt(pooled_variance_t_test)

# Statistique de test
T = (mu_con-mu_exp)/SE

# Valeur critique pour le test t bilatéral à 2 échantillons
t_crit = t.ppf(1-alpha/2, N_con + N_exp - 2)

# P-value du test t bilatéral en utilisant la distribution t et sa propriété de symétrie
p_value = t.sf(T, N_con + N_exp - 2)*2

# Marge d'erreur
margin_error = t_crit * SE
# Intervalle de confiance
CI = [(mu_con-mu_exp) - margin_error, (mu_con-mu_exp) + margin_error]

print("T-score: ", T)
print("T-critical: ", t_crit)
print("P_value: ", p_value)
print("Confidence Interval of 2 sample T-test: ", np.round(CI,2))
```

## Test z à 2 échantillons

Il existe diverses situations où vous pourriez vouloir utiliser un test z à 2 échantillons :

-   si vous souhaitez tester s'il existe une différence statistiquement significative entre les métriques des groupes de contrôle et expérimentaux qui se présentent sous forme de moyennes (par exemple, le montant moyen des achats) ou de proportions (par exemple, le taux de clics).
-   si la métrique suit une distribution _normale_.
-   lorsque la taille de l'échantillon est supérieure à 30, de sorte que vous pouvez utiliser le théorème central limite (TCL) pour affirmer que les distributions d'échantillonnage des groupes de contrôle et expérimentaux sont asymptotiquement normales.

Ici, nous ferons une distinction entre deux cas : celui où la métrique primaire est sous forme de proportions (comme le taux de clics) et celui où la métrique primaire est sous forme de moyennes (comme le montant moyen des achats).

### Cas 1 : Test z pour comparer des proportions (bilatéral)

Si vous souhaitez tester s'il existe une différence statistiquement significative entre les métriques des groupes de contrôle et expérimentaux qui se présentent sous forme de proportions (comme le CTR) et si l'événement de clic se produit de manière indépendante, vous pouvez utiliser un test z à 2 échantillons pour tester l'hypothèse suivante :

$$  
\\begin{cases}  
H\_0: p\_{\\text{con}} = p\_{\\text{exp}} \\\\  
H\_1: p\_{\\text{con}} \\neq p\_{\\text{exp}}  
\\end{cases}  
$$  
  
$$  
\\begin{cases}  
H\_0: p\_{\\text{con}} - p\_{\\text{exp}} = 0 \\\\  
H\_1: p\_{\\text{con}} - p\_{\\text{exp}} \\neq 0  
\\end{cases}  
$$

où chaque événement de clic peut être décrit par une variable aléatoire pouvant prendre deux valeurs possibles : 1 (succès) et 0 (échec). Elle suit également une distribution de Bernoulli (clic : succès et pas de clic : échec) où p_con et p_exp sont respectivement les probabilités de cliquer (probabilité de succès) des groupes de contrôle et expérimentaux.

Ainsi, après avoir collecté les données d'interaction des utilisateurs de contrôle et expérimentaux, vous pouvez calculer les estimations de ces deux probabilités comme suit :

$$ SE = \\sqrt{\\hat{S}^2\_{\\text{pooled}}} $$  
  
$$ Z = \\frac{(\\hat{p}\_{\\text{con}} - \\hat{p}\_{\\text{exp}})}{SE} $$

Puisque nous testons la différence entre ces probabilités, nous devons obtenir une estimation de la probabilité de succès pondérée et une estimation de la variance pondérée, ce qui peut être fait comme suit :

$$ \\hat{p}\_{\\text{pooled}} = \\frac{X\_{\\text{con}} + X\_{\\text{exp}}}{N\_{\\text{con}} + N\_{\\text{exp}}} = \\frac{\\#\\text{clics}\_{\\text{con}} + \\#\\text{clics}\_{\\text{exp}}}{\\#\\text{impressions}\_{\\text{con}} + \\#\\text{impressions}\_{\\text{exp}}} $$

$$ \\hat{S}^2\_{\\text{pooled}} = \\hat{p}\_{\\text{pooled}}(1 - \\hat{p}\_{\\text{pooled}}) \* \\left(\\frac{1}{N\_{\\text{con}}} + \\frac{1}{N\_{\\text{exp}}}\\right) $$

Ensuite, l'**erreur type** est égale à la racine carrée de l'estimation de la variance pondérée. Elle peut être définie comme :

$$ SE = \\sqrt{\\hat{S}^2\_{\\text{pooled}}} $$

Et ainsi, la **statistique de test** du test z à 2 échantillons pour la différence de proportions peut être calculée comme suit :

$$ Z = \\frac{(\\hat{p}_{\\text{con}} - \\hat{p}_{\\text{exp}})}{SE} $$

Ensuite, la p-value de cette statistique de test peut être calculée comme suit :

$$ p\_{\\text{value}} = \\Pr\[Z \\leq -T \\text{ ou } z \\geq T\] $$  
  
$$ = 2 \* \\Pr\[Z \\geq T\] $$

Enfin, vous pouvez calculer l'**intervalle de confiance** du test comme suit :

$$ CI = \\left\[ (\\hat{p}\_{\\text{con}} - \\hat{p}\_{\\text{exp}}) - z\_{\\frac{\\alpha}{2}} \* SE, (\\hat{p}\_{\\text{con}} - \\hat{p}\_{\\text{exp}}) + z\_{\\frac{\\alpha}{2}} \* SE \\right\] $$

où z_(1-alpha/2) est la valeur critique du test correspondant au test z bilatéral avec un niveau de signification alpha. Vous pouvez la trouver en utilisant la [table Z][59].

La région de rejet de ce test z à 2 échantillons bilatéral peut être visualisée par le graphique suivant :

![Source de l'image : LunarTech](https://www.freecodecamp.org/news/content/images/2024/04/1-hHddr3psz2Zxy-hzbLVVwA.png)

Source de l'image : L'auteur

L'extrait de code Python que vous avez fourni effectue un test z à deux échantillons pour des proportions. Ce type de test est utilisé pour déterminer s'il existe une différence significative entre les proportions de deux groupes. Voici une brève explication des étapes effectuées par le code :

1.  Calcule les proportions d'échantillon pour les groupes de contrôle et expérimentaux.
2.  Calcule la proportion d'échantillon pondérée, qui est une estimation de la proportion en supposant que l'hypothèse nulle (selon laquelle il n'y a pas de différence entre les proportions des groupes) est vraie.
3.  Calcule la variance d'échantillon pondérée basée sur la proportion pondérée et les tailles des deux échantillons.
4.  Dérive l'erreur type de la différence des proportions d'échantillon.
5.  Calcule la statistique de test z, qui mesure le nombre d'erreurs types entre la différence de proportion d'échantillon et l'hypothèse nulle.
6.  Trouve la valeur z critique à partir de la distribution normale centrée réduite pour le niveau de signification donné.
7.  Calcule la p-value pour évaluer les preuves contre l'hypothèse nulle.
8.  Calcule la marge d'erreur et l'intervalle de confiance pour la différence de proportions.
9.  Affiche la statistique de test, la valeur critique, la p-value et l'intervalle de confiance, et sur la base de la statistique de test et de la valeur critique, il peut afficher une déclaration pour rejeter ou ne pas rejeter l'hypothèse nulle.

La dernière partie du code utilise Matplotlib pour créer une visualisation de la distribution normale centrée réduite et des régions de rejet pour le test z bilatéral. Cette aide visuelle permet de comprendre où se situe la statistique de test par rapport à la distribution et aux valeurs critiques.

```
import numpy as np
from scipy.stats import norm

X_con = 1242 # clics contrôle
N_con = 9886 # impressions contrôle
X_exp = 974 # clics expérimental
N_exp = 10072 # impressions expérimental

# Niveau de signification
alpha = 0.05

p_con_hat = X_con / N_con
p_exp_hat = X_exp / N_exp

p_pooled_hat = (X_con + X_exp)/(N_con + N_exp)
pooled_variance = p_pooled_hat*(1-p_pooled_hat) * (1/N_con + 1/N_exp)

# Erreur type
SE = np.sqrt(pooled_variance)

# statistique de test
Test_stat = (p_con_hat - p_exp_hat)/SE
# valeur critique en utilisant la distribution normale centrée réduite
Z_crit = norm.ppf(1-alpha/2)

# Marge d'erreur
m = SE * Z_crit
# test bilatéral et utilisation de la propriété de symétrie de la distribution normale, donc on multiplie par 2
p_value = norm.sf(Test_stat)*2

# Intervalle de confiance
CI = [(p_con_hat-p_exp_hat) - SE * Z_crit, (p_con_hat-p_exp_hat) + SE * Z_crit]

if np.abs(Test_stat) >= Z_crit:
    print("rejeter l'hypothèse nulle")
    print(p_value)

print("Test Statistics stat: ", Test_stat)
print("Z-critical: ", Z_crit)
print("P_value: ", p_value)
print("Confidence Interval of 2 sample Z-test for proportions: ", np.round(CI,2))

import matplotlib.pyplot as plt
z = np.arange(-3,3,  0.1)
plt.plot(z, norm.pdf(z), label = 'Distribution normale centrée réduite',color = 'purple',linewidth = 2.5)
plt.fill_between(z[z>Z_crit], norm.pdf(z[z>Z_crit]), label = 'Région de rejet droite',color ='y' )
plt.fill_between(z[z<(-1)*Z_crit], norm.pdf(z[z<(-1)*Z_crit]), label = 'Région de rejet gauche',color ='y' )
plt.title("Région de rejet du test z à deux échantillons")
plt.legend()
plt.show()
```

### Cas 2 : Test z pour comparer des moyennes (bilatéral)

Si vous souhaitez tester s'il existe une différence statistiquement significative entre les métriques des groupes de contrôle et expérimentaux qui se présentent sous forme de moyennes (comme le montant moyen des achats), vous pouvez utiliser un test z à 2 échantillons pour tester l'hypothèse suivante :

$$  
\\begin{cases}  
H\_0: {CR}\_{\\text{con}} = {CR}\_{\\text{exp}} \\\\  
H\_1:{CR}\_{\\text{con}} \\neq {CR}\_{\\text{exp}}  
\\end{cases}  
$$  
  
$$  
\\begin{cases}  
H\_0: {CR}\_{\\text{con}} - {CR}\_{\\text{exp}} = 0 \\\\  
H\_1: {CR}\_{\\text{con}} - {CR}\_{\\text{exp}} \\neq 0  
\\end{cases}  
$$

où la distribution d'échantillonnage des moyennes du groupe de contrôle suit une distribution normale de moyenne mu_con et de variance σ²_con/N_con. De plus, la distribution d'échantillonnage des moyennes du groupe expérimental suit également une distribution normale de moyenne mu_exp et de variance σ²_exp/N_exp.

$$ \\hat{\\mu}\_{\\text{con}} \\sim N(\\mu\_{con}, \\frac{\\sigma^2\_{con}}{N\_{con}}) $$  
  
$$ \\hat{\\mu}\_{\\text{exp}} \\sim N(\\mu\_{exp}, \\frac{\\sigma^\_{exp}2}{N\_{exp}}) $$

Ensuite, la différence des moyennes des groupes de contrôle et expérimentaux suit également une distribution normale de moyenne mu_con-mu_exp et de variance σ²_con/N_con + σ²_exp/N_exp.

$$ \\hat{\\mu}\_{\\text{con}}-\\hat{\\mu}\_{\\text{exp}}  \\sim N(\\mu\_{con}-\\mu\_{exp}, \\frac{\\sigma^2\_{con}}{N\_{con}}+\\frac{\\sigma^2\_{exp}}{N\_{exp}}) $$

Par conséquent, la **statistique de test** du test z à 2 échantillons pour la différence des moyennes peut être calculée comme suit :

$$ T = \\frac{\\hat{\\mu}\_{\\text{con}}-\\hat{\\mu}\_{\\text{exp}}}{\\sqrt{\\frac{\\sigma^2\_{con}}{N\_{con}} + \\frac{\\sigma^2\_{exp}}{N\_{exp}}}}  \\sim N(0,1) $$

L'**erreur type** est égale à la racine carrée de l'estimation de la variance pondérée et peut être définie comme :

$$ SE = \\sqrt{\\frac{\\sigma^2\_{con}}{N\_{con}} + \\frac{\\sigma^2\_{exp}}{N\_{exp}}}} $$

Ensuite, la p-value de cette statistique de test peut être calculée comme suit :

$$ p\_{\\text{value}} = \\Pr\[Z \\leq -T \\text{ ou } Z \\geq T\] $$  
  
$$ = 2 \* \\Pr\[Z \\geq T\] $$

Enfin, vous pouvez calculer l'**intervalle de confiance** du test comme suit :

$$ CI = \[(\\mu\_hat\_{con} - \\mu\_hat\_{exp}) - z\_{1-\\alpha/2}\*SE,((\\mu\_hat\_{con} - \\mu\_hat\_{exp}) + z\_{1-\\alpha/2)\*SE\] $$

Le code Python fourni semble être configuré pour mener un test z à deux échantillons, généralement utilisé pour déterminer s'il existe une différence significative entre les moyennes de deux groupes indépendants. Dans ce contexte, le code pourrait comparer deux processus ou traitements différents.

1.  Il génère deux tableaux d'entiers aléatoires pour représenter les données d'un groupe de contrôle (`X_A`) et d'un groupe expérimental (`X_B`).
2.  Il calcule les moyennes d'échantillon (`mu_con`, `mu_exp`) et les variances (`variance_con`, `variance_exp`) pour les deux groupes.
3.  La variance pondérée est calculée, laquelle est utilisée au dénominateur de la formule de la statistique de test pour le test z, fournissant une mesure de la variance commune des données.
4.  La statistique de test z (`T`) est calculée en prenant la différence entre les deux moyennes d'échantillon et en la divisant par l'erreur type de la différence.
5.  La p-value est calculée pour tester l'hypothèse selon laquelle les moyennes des deux groupes sont statistiquement différentes l'une de l'autre.
6.  La valeur z critique (`Z_crit`) est déterminée à partir de la distribution normale centrée réduite, ce qui définit les points de coupure pour la signification.
7.  Une marge d'erreur est calculée, et un intervalle de confiance pour la différence des moyennes est construit.
8.  La statistique de test, la valeur critique, la p-value et l'intervalle de confiance sont affichés dans la console.

Enfin, le code utilise Matplotlib pour tracer la distribution normale centrée réduite et mettre en évidence les régions de rejet pour le test z. Cette visualisation peut aider à comprendre le résultat du test z en termes de position de la statistique de test par rapport à la distribution et aux valeurs critiques pour un test bilatéral.

```python
import numpy as np
from scipy.stats import norm

N_con = 60
N_exp = 60

# Niveau de signification
alpha = 0.05

X_A = np.random.randint(100, size = N_con)
X_B = np.random.randint(100, size = N_exp)

# Calcul des moyennes des groupes de contrôle et expérimental
mu_con = np.mean(X_A)
mu_exp = np.mean(X_B)

variance_con = np.var(X_A)
variance_exp = np.var(X_B)

# Variance pondérée
pooled_variance = np.sqrt(variance_con/N_con + variance_exp/N_exp)

# Statistique de test
T = (mu_con-mu_exp)/np.sqrt(variance_con/N_con + variance_exp/N_exp)

# test bilatéral et utilisation de la propriété de symétrie de la distribution normale, donc on multiplie par 2
p_value = norm.sf(T)*2

# Valeur z critique
Z_crit  = norm.ppf(1-alpha/2)

# Marge d'erreur
m = Z_crit*pooled_variance

# Intervalle de confiance
CI = [(mu_con - mu_exp) - m, (mu_con - mu_exp) + m]


print("Test Statistics stat: ", T)
print("Z-critical: ", Z_crit)
print("P_value: ", p_value)
print("Confidence Interval of 2 sample Z-test for proportions: ", np.round(CI,2))

import matplotlib.pyplot as plt
z = np.arange(-3,3,  0.1)
plt.plot(z, norm.pdf(z), label = 'Distribution normale centrée réduite',color = 'purple',linewidth = 2.5)
plt.fill_between(z[z>Z_crit], norm.pdf(z[z>Z_crit]), label = 'Région de rejet droite',color ='y' )
plt.fill_between(z[z<(-1)*Z_crit], norm.pdf(z[z<(-1)*Z_crit]), label = 'Région de rejet gauche',color ='y' )
plt.title("Région de rejet du test z à deux échantillons")
plt.legend()
plt.show()
```

### Test du Khi-deux

Si vous souhaitez tester s'il existe une différence statistiquement significative entre les métriques de performance des groupes de contrôle et expérimentaux (par exemple leurs conversions) et que vous ne voulez pas vraiment connaître la nature de cette relation (lequel est meilleur), vous pouvez utiliser un test du Khi-deux pour tester l'hypothèse suivante :

$$  
\\begin{cases}  
H\_0: \\CR\_{\\text{con}} = \\CR\_{\\text{exp}} \\\\  
H\_1: \\CR\_{\\text{con}} \\neq \\CR\_{\\text{exp}}  
\\end{cases}  
$$  
  
$$\\begin{cases}  
H\_0: \\CR\_{\\text{con}} - \\CR\_{\\text{exp}} = 0 \\\\  
H\_1: \\CR\_{\\text{con}} - \\CR\_{\\text{exp}} \\neq 0  
\\end{cases}  
$$

Notez que la métrique doit être sous la forme d'une variable binaire (par exemple, conversion ou pas de conversion/clic ou pas de clic). Les données peuvent alors être représentées sous la forme du tableau suivant, où O et T correspondent respectivement aux valeurs observées et théoriques.

![1-1RVqOq4mc4-oach5QHCy5g](https://www.freecodecamp.org/news/content/images/2024/04/1-1RVqOq4mc4-oach5QHCy5g.png)

Tableau montrant les données du test du Khi-deux

Ensuite, la statistique de test du test Khi-2 peut être exprimée comme suit :

$$ T = \\sum\_{i} \\frac{(Observed\_i - Expected\_i)^2}{Expected\_i} $$

où _Observed_ correspond aux données observées et _Expected_ correspond à la valeur théorique, et i peut prendre les valeurs 0 (pas de conversion) et 1 (conversion). Il est important de voir que chacun de ces facteurs a un dénominateur séparé. La formule de la statistique de test lorsque vous n'avez que deux groupes peut être représentée comme suit :

$$ T = \\frac{(Observed\_{con,1} - T\_{con,1})^2}{T\_{con,1}} + \\frac{(Observed\_{con,0} - T\_{con,0})^2}{T\_{con,0}} + \\frac{(Observed\_{exp,1} - T\_{exp,1})^2}{T\_{exp,1}} + \\frac{(Observed\_{exp,0} - T\_{exp,0})^2}{T\_{exp,0}} $$

La valeur attendue est simplement égale au nombre de fois où chaque version du produit est vue multiplié par la probabilité qu'elle mène à une conversion (ou à un clic dans le cas du CTR).

Notez que, puisque le test Khi-2 n'est pas un test paramétrique, son erreur type et son intervalle de confiance ne peuvent pas être calculés de manière standard comme nous l'avons fait dans le test z ou le test t paramétriques.

La région de rejet de ce test z à 2 échantillons bilatéral peut être visualisée par le graphique suivant :

![Source de l'image : LunarTech](https://www.freecodecamp.org/news/content/images/2024/04/1-t8GYhf7iX1NJ2wNA8bHQ_A.png)

Source de l'image : L'auteur

Le code Python que vous avez partagé sert à effectuer un test du Khi-deux, un test d'hypothèse statistique utilisé pour déterminer s'il existe une différence significative entre les fréquences attendues et les fréquences observées dans une ou plusieurs catégories.

Dans l'extrait de code fourni, il semble que le test soit utilisé pour comparer deux jeux de données catégorielles :

1.  Il calcule la statistique de test du Khi-deux en sommant la différence au carré entre les fréquences observées (`O`) et attendues (`T`), divisée par les fréquences attendues pour chaque catégorie. C'est ce qu'on appelle la distance relative au carré et elle est utilisée comme statistique de test pour le test du Khi-deux.
2.  Il calcule ensuite la p-value pour cette statistique de test en utilisant les degrés de liberté, qui dans ce cas sont supposés être de 1 (mais cela dépendrait normalement du nombre de catégories moins un).
3.  La bibliothèque Matplotlib est utilisée pour tracer la fonction de densité de probabilité (pdf) de la distribution du Khi-deux avec un degré de liberté. Elle met également en évidence la région de rejet pour le test, qui correspond à la valeur critique de la distribution du Khi-deux que la statistique de test doit dépasser pour que la différence soit considérée comme statistiquement significative.

La visualisation aide à comprendre le test du Khi-deux en montrant où se situe la statistique de test par rapport à la distribution du Khi-deux et à sa valeur critique. Si la statistique de test se trouve dans la région de rejet, l'hypothèse nulle d'absence de différence dans les fréquences peut être rejetée.

```python
import numpy as np
from scipy.stats import chi2

O = np.array([86, 83, 5810,3920])
T = np.array([105,65,5781, 3841])

# Distance_relative_au_carre

def calculate_D(O,T):
    D_sum = 0
    for i in range(len(O)):
        D_sum += (O[i] - T[i])**2/T[i]
    return(D_sum)

D = calculate_D(O,T)
p_value = chi2.sf(D, df = 1)


import matplotlib.pyplot as plt
# Étape 1 : choisir une plage d'axes x comme dans le cas du test z (-3,3,0.1)
d = np.arange(0,5,0.1)
# Étape 2 : dessiner la pdf initiale du khi-2 avec df = 1 et la plage d'axes x d que nous venons de créer
plt.plot(d, chi2.pdf(d, df = 1), color = "purple")
# Étape 3 : remplir la région de rejet
plt.fill_between(d[d>D], chi2.pdf(d[d>D], df = 1), color = "y")
# Étape 4 : ajouter un titre
plt.title("Région de rejet du test Khi-2 à deux échantillons")
# Étape 5 : afficher le graphique plt
plt.show()
```

### P-Values

Un autre moyen rapide de déterminer s'il faut rejeter ou soutenir l'hypothèse nulle est d'utiliser les **p-values**. La p-value est la probabilité que la condition sous l'hypothèse nulle se produise. En d'autres termes, la p-value est la probabilité, en supposant que l'hypothèse nulle soit vraie, d'observer un résultat au moins aussi extrême que la statistique de test. Plus la p-value est petite, plus les preuves contre l'hypothèse nulle sont fortes, suggérant qu'elle peut être rejetée.

L'interprétation d'une _p_-value dépend du niveau de signification choisi. Le plus souvent, des niveaux de signification de 1 %, 5 % ou 10 % sont utilisés pour interpréter la p-value. Ainsi, au lieu d'utiliser le test t et le test F, les p-values de ces statistiques de test peuvent être utilisées pour tester les mêmes hypothèses.

La figure suivante montre un exemple de sortie d'une régression MCO avec deux variables indépendantes. Dans ce tableau, la p-value du test t, testant la signification statistique de l'estimation du paramètre de la variable _class_size_, et la p-value du test F, testant la signification statistique conjointe des estimations des paramètres des variables _class_size_ et _el_pct_, sont soulignées.

![1-aJh-8BEvYnwid5jS7fDLHA](https://www.freecodecamp.org/news/content/images/2024/04/1-aJh-8BEvYnwid5jS7fDLHA.png)

Source de l'image : [Stock and Whatson][60]

La p-value correspondant à la variable _class_size_ est 0,011. Lorsque nous comparons cette valeur aux niveaux de signification 1 % ou 0,01, 5 % ou 0,05, 10 % ou 0,1, nous pouvons tirer les conclusions suivantes :

-   0,011 > 0,01 → L'hypothèse nulle du test t ne peut pas être rejetée au niveau de signification de 1 %.
-   0,011 < 0,05 → L'hypothèse nulle du test t peut être rejetée au niveau de signification de 5 %.
-   0,011 < 0,10 → L'hypothèse nulle du test t peut être rejetée au niveau de signification de 10 %.

Ainsi, cette p-value suggère que le coefficient de la variable _class_size_ est statistiquement significatif aux niveaux de signification de 5 % et 10 %. La p-value correspondant au test F est 0,0000. Et puisque 0 est plus petit que les trois valeurs de coupure (0,01, 0,05, 0,10), nous pouvons conclure que l'hypothèse nulle du test F peut être rejetée dans les trois cas.

Cela suggère que les coefficients des variables _class_size_ et _el_pct_ sont conjointement statistiquement significatifs aux niveaux de signification de 1 %, 5 % et 10 %.

#### Limites des p-values

L'utilisation des p-values présente de nombreux avantages, mais elle a aussi ses limites. L'une des principales est que la p-value dépend à la fois de l'ampleur de l'association et de la taille de l'échantillon. Si l'ampleur de l'effet est faible et statistiquement insignifiante, la p-value pourrait tout de même montrer un **impact significatif** parce que la taille de l'échantillon est grande. L'inverse peut également se produire : un effet peut être important, mais ne pas répondre aux critères p < 0,01, 0,05 ou 0,10 si la taille de l'échantillon est petite.

## Statistiques inférentielles

Les statistiques inférentielles utilisent les données d'un échantillon pour porter des jugements raisonnables sur la population dont proviennent les données de l'échantillon. Nous les utilisons pour étudier les relations entre les variables au sein d'un échantillon et faire des prédictions sur la façon dont ces variables se rapporteront à une population plus large.

La **Loi des Grands Nombres (LGN)** et le **Théorème Central Limite (TCL)** jouent tous deux un rôle important dans les statistiques inférentielles car ils montrent que les résultats expérimentaux sont valables quelle que soit la forme de la distribution de la population d'origine lorsque les données sont suffisamment volumineuses.

Plus on recueille de données, plus les inférences statistiques deviennent précises – par conséquent, plus les estimations des paramètres générées sont précises.

### Loi des Grands Nombres (LGN)

Supposons que **X1, X2, . . . , Xn** soient toutes des variables aléatoires indépendantes ayant la même distribution sous-jacente (également appelées indépendantes et identiquement distribuées ou i.i.d), où tous les X ont la même moyenne **μ** et le même écart-type **σ**. À mesure que la taille de l'échantillon augmente, la probabilité que la moyenne de tous les X soit égale à la moyenne μ est égale à 1.

La Loi des Grands Nombres peut être résumée comme suit :

![1-guDCKe5lIntrCicvX1WeBQ](https://www.freecodecamp.org/news/content/images/2024/04/1-guDCKe5lIntrCicvX1WeBQ.png)

### Théorème Central Limite (TCL)

Supposons que **X1, X2, . . . , Xn** soient toutes des variables aléatoires indépendantes ayant la même distribution sous-jacente (également appelées indépendantes et identiquement distribuées ou i.i.d), où tous les X ont la même moyenne **μ** et le même écart-type **σ**. À mesure que la taille de l'échantillon augmente, la distribution de probabilité de X **converge en loi** vers une distribution normale de moyenne **μ** et de variance **σ²**.

Le Théorème Central Limite peut être résumé comme suit :

![1-FCDUcznU-VRRdctstA1WJA](https://www.freecodecamp.org/news/content/images/2024/04/1-FCDUcznU-VRRdctstA1WJA.png)

En d'autres termes, lorsque vous avez une population de moyenne μ et d'écart-type σ et que vous prélevez des échantillons aléatoires suffisamment grands dans cette population avec remise, alors la distribution des moyennes d'échantillon sera approximativement distribuée normalement.

## Techniques de réduction de dimensionnalité

La réduction de dimensionnalité est la transformation de données d'un **espace de grande dimension** vers un **espace de faible dimension** de telle sorte que cette représentation de faible dimension des données contienne toujours autant que possible les propriétés significatives des données d'origine.

Avec la popularité croissante du Big Data, la demande pour ces techniques de réduction de dimensionnalité, réduisant la quantité de données et de caractéristiques inutiles, a également augmenté. Des exemples de techniques de réduction de dimensionnalité populaires sont l'[Analyse en Composantes Principales][61], l'[Analyse Factorielle][62], la [Corrélation Canonique][63], la [Forêt Aléatoire][64].

### Analyse en Composantes Principales (ACP)

L'Analyse en Composantes Principales (ACP) est une technique de réduction de dimensionnalité très souvent utilisée pour réduire la dimensionnalité de grands jeux de données. Elle le fait en transformant un grand ensemble de variables en un ensemble plus petit qui contient toujours la majeure partie de l'information ou de la variation du jeu de données original.

Supposons que nous ayons des données X avec p variables X1, X2, …., Xp avec des **vecteurs propres** e1, …, ep et des **valeurs propres** λ1,…, λp. Les valeurs propres montrent la variance expliquée par un champ de données particulier par rapport à la variance totale.

L'idée derrière l'ACP est de créer de nouvelles variables (indépendantes), appelées Composantes Principales, qui sont une combinaison linéaire des variables existantes. La i-ème composante principale peut être exprimée comme suit :

$$ Y\_i = e\_{i1}X\_1 + e\_{i2}X\_2 + e\_{i3}X\_3 + ... + e\_{ip}X\_p $$

Ensuite, en utilisant la **règle du coude** ou la [**règle de Kaiser**][65], vous pouvez déterminer le nombre de composantes principales qui résument de manière optimale les données sans perdre trop d'information.

Il est également important d'examiner **la proportion de variation totale (PRTV)** expliquée par chaque composante principale pour décider s'il est bénéfique de l'inclure ou de l'exclure. La PRTV pour la i-ème composante principale peut être calculée à l'aide des valeurs propres comme suit :

$$ PRTV\_i = \\frac{{\\lambda\_i}}{{\\sum\_{k=1}^{p} \\lambda\_k}} $$

### Règle du coude

La règle du coude (elbow rule) ou méthode du coude est une approche heuristique que nous pouvons utiliser pour déterminer le nombre optimal de composantes principales à partir des résultats de l'ACP.

L'idée derrière cette méthode est de tracer _la variation expliquée_ en fonction du nombre de composantes et de choisir le "coude" de la courbe comme nombre optimal de composantes principales.

Voici un exemple d'un tel diagramme de dispersion où la PRTV (axe Y) est tracée en fonction du nombre de composantes principales (axe X). Le coude correspond à la valeur 2 sur l'axe X, ce qui suggère que le nombre optimal de composantes principales est 2.

![1-cLCESS2u2ZIsQbPBd7Ljlg](https://www.freecodecamp.org/news/content/images/2024/04/1-cLCESS2u2ZIsQbPBd7Ljlg.png)

Source de l'image : [Multivariate Statistics Github][66]

### Analyse factorielle (AF)

L'analyse factorielle ou AF est une autre méthode statistique de réduction de dimensionnalité. C'est l'une des techniques d'interdépendance les plus couramment utilisées. Nous pouvons l'utiliser lorsque l'ensemble pertinent de variables présente une interdépendance systématique et que notre objectif est de découvrir les facteurs latents qui créent une communauté.

Supposons que nous ayons des données X avec p variables X1, X2, …., Xp. Le modèle AF peut être exprimé comme suit :

$$ X-\\mu = AF + u $$

où :

-   X est une matrice [p x N] de p variables et N observations.
-   µ est la matrice [p x N] de la moyenne de la population.
-   A est la matrice [p x k] des **chargements factoriels** communs.
-   F [k x N] est la matrice des facteurs communs.
-   et u [p x N] est la matrice des facteurs spécifiques.

Ainsi, pour le dire autrement, un modèle factoriel est une série de régressions multiples, prédisant chacune des variables Xi à partir des valeurs des facteurs communs inobservables :

$$  
X\_1 = \\mu\_1 + a\_{11}f\_1 + a\_{12}f\_2 + ... + a\_{1m}f\_m + u1\\\\  
X\_2 = \\mu\_2 + a\_{21}f\_1 + a\_{22}f\_2 + ... + a\_{2m}f\_m + u2\\\\  
.\\\\  
.\\\\  
.\\\\  
X\_p = \\mu\_p + a\_{p1}f\_1 + a\_{p2}f\_2 + ... + a\_{pm}f\_m + up  
$$

Chaque variable possède k de ses propres facteurs communs, et ceux-ci sont liés aux observations via la matrice de chargement factoriel pour une seule observation comme suit :

Dans l'analyse factorielle, les **facteurs** sont calculés pour **maximiser la variance entre les groupes** tout en **minimisant la variance au sein des groupes**. Ce sont des facteurs car ils regroupent les variables sous-jacentes. Contrairement à l'ACP, dans l'AF, les données doivent être normalisées, étant donné que l'AF suppose que le jeu de données suit une distribution normale.

## Préparation aux entretiens – Top 7 des questions de statistiques avec réponses

Vous préparez des entretiens en statistiques, analyse de données ou Data Science ? Il est crucial de connaître les concepts statistiques clés et leurs applications.

Ci-dessous, j'ai inclus sept questions de statistiques importantes avec leurs réponses, couvrant les tests statistiques de base, la théorie des probabilités et l'utilisation des statistiques dans la prise de décision, comme les tests A/B.

### Question 1 : Quelle est la différence entre un test t et un test z ?

La question "Quelle est la différence entre un test t et un test z ?" est une question courante dans les entretiens de Data Science car elle teste la compréhension par le candidat des concepts statistiques de base utilisés pour comparer les moyennes de groupes.

Cette connaissance est cruciale car le choix du bon test affecte la validité des conclusions tirées des données, ce qui est une tâche quotidienne dans le rôle d'un Data Scientist lorsqu'il s'agit d'interpréter des expériences, d'analyser des résultats d'enquêtes ou d'évaluer des modèles.

### Réponse :

Les tests t et les tests z sont tous deux des méthodes statistiques utilisées pour déterminer s'il existe des différences significatives entre les moyennes de deux groupes. Mais ils présentent des différences clés :

-   **Hypothèses** : Vous pouvez utiliser un test t lorsque les tailles d'échantillon sont petites et que l'écart-type de la population est inconnu. Il ne nécessite pas que la moyenne de l'échantillon soit normalement distribuée si la taille de l'échantillon est suffisamment grande grâce au théorème central limite. Le test z suppose que les distributions de l'échantillon et de la population sont normalement distribuées.
-   **Taille de l'échantillon** : Les tests t sont généralement utilisés pour des tailles d'échantillon inférieures à 30, tandis que les tests z sont utilisés pour des tailles d'échantillon plus grandes (supérieures ou égales à 30) lorsque l'écart-type de la population est connu.
-   **Statistique de test** : Le test t utilise la distribution t pour calculer la statistique de test, en tenant compte de l'écart-type de l'échantillon. Le test z utilise la distribution normale centrée réduite, en utilisant l'écart-type connu de la population.
-   **P-Value** : La p-value dans un test t est déterminée sur la base de la distribution t, qui tient compte de la variabilité dans les échantillons plus petits. Le test z utilise la distribution normale centrée réduite pour calculer la p-value, adaptée aux échantillons plus grands ou aux paramètres de population connus.

### Question 2 : Qu'est-ce qu'une p-value ?

La question "Qu'est-ce qu'une p-value ?" nécessite la compréhension d'un concept fondamental dans les tests d'hypothèses que nous avons abordé en détail dans ce blog avec des exemples. Ce n'est pas juste un nombre – c'est un pont entre les données que vous collectez et les conclusions que vous tirez pour une prise de décision basée sur les données.

Les p-values quantifient les preuves contre une hypothèse nulle — quelle est la probabilité d'observer les données collectées si l'hypothèse nulle était vraie.

Pour les Data Scientists, les p-values font partie du langage quotidien de l'analyse statistique, de la validation de modèles et de la conception expérimentale. Ils doivent interpréter correctement les p-values pour prendre des décisions éclairées et doivent souvent expliquer leurs implications aux parties prenantes qui n'ont peut-être pas de connaissances statistiques approfondies.

Ainsi, comprendre les p-values aide les Data Scientists à transmettre le niveau de certitude ou de doute dans leurs conclusions et à justifier les actions ou recommandations ultérieures.

Ici, vous devez donc montrer votre compréhension de ce que mesure la p-value et la relier à la signification statistique et aux tests d'hypothèses.

### Réponse :

La p-value mesure la probabilité d'observer une statistique de test au moins aussi extrême que celle observée, sous l'hypothèse que l'hypothèse nulle est vraie. Elle aide à décider si les données observées s'écartent de manière significative de ce qui serait attendu sous l'hypothèse nulle.

Si la p-value est inférieure à un seuil prédéterminé (niveau alpha, généralement fixé à 0,05), l'hypothèse nulle est rejetée, indiquant que le résultat observé est statistiquement significatif.

### Question 3 : Quelles sont les limites des p-values ?

Les p-values sont un élément de base des statistiques inférentielles, fournissant une métrique pour évaluer les preuves contre une hypothèse nulle. Dans cette question, vous devez en nommer quelques-unes.

### Réponse :

-   **Dépendance à la taille de l'échantillon** : La p-value est sensible à la taille de l'échantillon. De grands échantillons peuvent donner des p-values significatives même pour des effets insignifiants, tandis que de petits échantillons peuvent ne pas détecter d'effets significatifs même s'ils existent.
-   **Pas une mesure de la taille de l'effet ou de l'importance** : Une petite p-value ne signifie pas nécessairement que l'effet est pratiquement significatif – elle indique simplement qu'il est peu probable qu'il se soit produit par hasard.
-   **Mauvaise interprétation** : Les p-values peuvent être mal interprétées comme étant la probabilité que l'hypothèse nulle soit vraie, ce qui est incorrect. Elles mesurent seulement les preuves contre l'hypothèse nulle.

### Question 4 : Qu'est-ce qu'un niveau de confiance ?

Un niveau de confiance représente la fréquence avec laquelle un intervalle de confiance estimé contiendrait le paramètre réel de la population si le même processus était répété plusieurs fois.

Par exemple, un niveau de confiance de 95 % signifie que si l'étude était répétée 100 fois, environ 95 des intervalles de confiance calculés à partir de ces études contiendraient le paramètre réel de la population.

### Question 5 : Quelle est la probabilité de tirer 5 boules rouges et 5 boules bleues sans remise ?

Quelle est la probabilité de tirer exactement 5 boules rouges et 5 boules bleues en 10 tirages sans remise à partir d'un ensemble de 100 boules, où il y a 70 boules rouges et 30 boules bleues ? Le texte décrit comment calculer cette probabilité en utilisant les mathématiques combinatoires et la distribution hypergéométrique.

Dans cette question, vous traitez un problème de probabilité classique qui implique des principes combinatoires et le concept de probabilité sans remise. Le contexte est un ensemble fini de boules, chaque tirage affectant les suivants car la composition de l'ensemble change à chaque tirage.

Pour aborder ce problème, vous devez considérer :

-   **Le nombre total de boules** : Si la question ne le précise pas, vous devez le demander ou faire une hypothèse raisonnable basée sur le contexte.
-   **Proportion initiale de boules** : Connaître le nombre initial de boules rouges et bleues dans l'ensemble.
-   **Probabilité séquentielle** : Rappelez-vous que chaque fois que vous tirez une boule, vous ne la remettez pas, donc la probabilité de tirer une boule d'une certaine couleur change à chaque tirage.
-   **Combinaisons** : Calculez le nombre de façons de choisir 5 boules rouges parmi le total des boules rouges et 5 boules bleues parmi le total des boules bleues, puis divisez par le nombre de façons de choisir n'importe quelles 10 boules parmi le total.

Réfléchir à ces points vous guidera dans la formulation de la solution basée sur la distribution hypergéométrique, qui décrit la probabilité d'un nombre donné de succès dans des tirages sans remise à partir d'une population finie.

Cette question teste votre capacité à appliquer la théorie des probabilités à un scénario dynamique, une compétence inestimable dans la prise de décision basée sur les données et la modélisation statistique.

### Réponse :

Pour trouver la probabilité de tirer exactement 5 boules rouges et 5 boules bleues en 10 tirages sans remise, nous calculons la probabilité de tirer 5 boules rouges sur 70 et 5 boules bleues sur 30, puis nous divisons par le nombre total de façons de tirer 10 boules sur 100 :

![Screenshot-2024-04-09-at-12.35.56-AM](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-09-at-12.35.56-AM.png)

Calculons cette probabilité :

![Screenshot-2024-04-09-at-12.36.16-AM](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-09-at-12.36.16-AM.png)

### Question 6 : Expliquez le théorème de Bayes et son importance dans le calcul des probabilités a posteriori.

Donnez un exemple de la façon dont il pourrait être utilisé dans les tests génétiques pour déterminer la probabilité qu'un individu soit porteur d'un certain gène.

Le théorème de Bayes est une pierre angulaire de la théorie des probabilités qui permet de mettre à jour des croyances initiales (probabilités a priori) avec de nouvelles preuves pour obtenir des croyances mises à jour (probabilités a posteriori). Cette question vise à tester la capacité du candidat à expliquer le concept et le cadre mathématique permettant d'incorporer de nouvelles preuves dans des prédictions ou des modèles existants.

### Réponse :

Le théorème de Bayes est un théorème fondamental de la théorie des probabilités et des statistiques qui décrit la probabilité d'un événement, sur la base de connaissances préalables des conditions qui pourraient être liées à l'événement. Il est crucial pour calculer les probabilités a posteriori, qui sont les probabilités d'hypothèses étant donné les preuves observées.

![Screenshot-2024-04-09-at-12.41.03-AM](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-09-at-12.41.03-AM.png)

-   _P_(_A_∣_B_) est la probabilité a posteriori : la probabilité de l'hypothèse _A_ étant donné la preuve _B_.
-   P(B∣A) est la vraisemblance : la probabilité d'observer la preuve _B_ étant donné que l'hypothèse _A_ est vraie.
-   P(A) est la probabilité a priori : la probabilité initiale de l'hypothèse _A_, avant d'observer la preuve _B_.
-   P(B) est la probabilité marginale : la probabilité totale d'observer la preuve _B_ sous toutes les hypothèses possibles.

### Question 7 : Décrivez comment vous détermineriez statistiquement si les résultats d'un test A/B sont significatifs - guidez-moi à travers le processus de test A/B.

Dans cette question, l'interviewer évalue votre connaissance globale du cadre des tests A/B. Il cherche des preuves que vous pouvez naviguer dans tout le spectre des procédures de test A/B, ce qui est essentiel pour les Data Scientists et les professionnels de l'IA chargés d'optimiser les fonctionnalités, de prendre des décisions basées sur les données et de tester des produits logiciels.

L'interviewer veut confirmer que vous comprenez chaque étape du processus, en commençant par la formulation d'hypothèses statistiques dérivées d'objectifs commerciaux. Il s'intéresse à votre capacité à mener une analyse de puissance et à discuter de ses composants, notamment la détermination de la taille de l'effet, du niveau de signification et de la puissance, tous essentiels pour calculer la taille minimale de l'échantillon nécessaire pour détecter un effet réel et éviter le p-hacking.

La discussion sur la randomisation, la collecte de données et le suivi permet de vérifier si vous comprenez comment maintenir l'intégrité des conditions de test. Vous devez également être prêt à expliquer la sélection des tests statistiques appropriés, le calcul des statistiques de test, des p-values et l'interprétation des résultats pour la signification statistique et pratique.

En fin de compte, l'interviewer teste si vous pouvez agir en tant que défenseur des données : quelqu'un capable de mener méticuleusement des tests A/B, d'en interpréter les résultats et de communiquer efficacement les conclusions et recommandations aux parties prenantes, favorisant ainsi une prise de décision basée sur les données au sein de l'organisation.

Pour apprendre le test A/B, consultez mon [cours intensif sur le test A/B sur YouTube][67].

### Réponse :

Dans un test A/B, ma première étape consiste à établir des hypothèses commerciales et statistiques claires. Par exemple, si nous testons une nouvelle mise en page de page Web, l'hypothèse commerciale pourrait être que la nouvelle mise en page augmente l'engagement des utilisateurs. Statistiquement, cela se traduit par l'attente d'un score d'engagement moyen plus élevé pour la nouvelle mise en page par rapport à l'ancienne.

Ensuite, je mènerais une analyse de puissance. Cela implique de décider d'une taille d'effet qui est pratiquement significative pour notre contexte commercial — disons, une augmentation de 10 % de l'engagement. Je choisirais un niveau de signification, généralement 0,05, et viserais une puissance de 80 %, réduisant ainsi la probabilité d'erreurs de type II.

L'analyse de puissance, qui prend en compte la taille de l'effet, le niveau de signification et la puissance, aide à déterminer la taille minimale de l'échantillon nécessaire. C'est crucial pour s'assurer que notre test est suffisamment puissant pour détecter l'effet qui nous intéresse et pour éviter le p-hacking en s'engageant sur une taille d'échantillon dès le départ.

Une fois notre taille d'échantillon déterminée, je m'assurerais d'une randomisation appropriée lors de l'affectation des utilisateurs aux groupes de contrôle et de test, afin d'éliminer le biais de sélection. Pendant le test, je surveillerais de près la collecte de données pour détecter toute anomalie ou ajustement nécessaire.

Une fois la collecte de données terminée, je choisirais un test statistique approprié en fonction de la distribution des données et de l'homogénéité de la variance — généralement un test t si la taille de l'échantillon est petite ou si une distribution normale ne peut être supposée, ou un test z pour des échantillons plus grands avec une variance connue.

Le calcul de la statistique de test et de la p-value correspondante nous permet de tester l'hypothèse nulle. Si la p-value est inférieure au niveau alpha choisi, nous rejetons l'hypothèse nulle, ce qui suggère que la nouvelle mise en page a un impact statistiquement significatif sur l'engagement.

En plus de la signification statistique, j'évaluerais la signification pratique en examinant l'intervalle de confiance pour la taille de l'effet et en considérant l'impact commercial.

Enfin, je documenterais l'ensemble du processus et des résultats, puis je les communiquerais aux parties prenantes dans un langage clair et non technique. Cela inclut non seulement la signification statistique, mais aussi la manière dont les résultats se traduisent en résultats commerciaux. En tant que défenseur des données, mon objectif est de soutenir des décisions basées sur les données qui s'alignent sur nos objectifs commerciaux et notre stratégie d'expérience utilisateur.

Pour obtenir plus de questions d'entretien, des statistiques au Deep Learning - avec plus de 400 Q&A ainsi qu'une préparation personnalisée aux entretiens, consultez notre [centre de ressources gratuites][68] et notre [Bootcamp Data Science avec essai gratuit][69].

Merci d'avoir choisi ce guide comme compagnon d'apprentissage. Alors que vous continuez à explorer le vaste domaine du Machine Learning, j'espère que vous le ferez avec confiance, précision et un esprit d'innovation. Meilleurs vœux dans tous vos projets futurs !

## À propos de l'auteur

Je suis **[Tatev Aslanyan][70]**, chercheuse senior en Machine Learning et IA, et co-fondatrice de **[LunarTech][71]** où nous rendons la Data Science et l'IA accessibles à tous. J'ai eu le privilège de travailler en Data Science dans de nombreux pays, notamment aux États-Unis, au Royaume-Uni, au Canada et aux Pays-Bas.

Avec un MSc et un BSc en économétrie en poche, mon parcours dans le Machine Learning et l'IA a été tout simplement incroyable. En m'appuyant sur mes études techniques pendant ma licence et mon master, ainsi que sur plus de 5 ans d'expérience pratique dans l'industrie de la Data Science, du Machine Learning et de l'IA, j'ai rassemblé ce résumé de haut niveau des sujets de ML pour le partager avec vous.

## Comment aller plus loin ?

Après avoir étudié ce guide, si vous souhaitez approfondir vos connaissances et qu'un apprentissage structuré vous convient, envisagez de nous rejoindre chez [**LunarTech**][72]. Nous proposons des cours individuels et un Bootcamp en Data Science, Machine Learning et IA.

Nous proposons un programme complet qui offre une compréhension approfondie de la théorie, une mise en œuvre pratique, un matériel de pratique étendu et une préparation aux entretiens sur mesure pour vous préparer au succès à votre propre rythme.

Vous pouvez consulter notre [Ultimate Data Science Bootcamp][73] et rejoindre [un essai gratuit][74] pour tester le contenu par vous-même. Il a été reconnu comme l'un des [meilleurs Bootcamps Data Science de 2023][75] et a été présenté dans des publications prestigieuses comme [Forbes][76], [Yahoo][77], [Entrepreneur][78] et plus encore. C'est votre chance de faire partie d'une communauté qui prospère grâce à l'innovation et à la connaissance. Voici le message de bienvenue !

<iframe width="356" height="200" src="https://www.youtube.com/embed/c-SXFXegVTw?start=2&amp;feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen="" title="Welcome to LunarTech - The Most Comprehensive Data Science Bootcamp" name="fitvid0"></iframe>

## Connectez-vous avec moi

![Screenshot-2024-04-09-at-12.05.32-AM](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-09-at-12.05.32-AM.png)

Newsletter [LunarTech][79]

-   [Suivez-moi sur **LinkedIn**][80] et sur **[YouTube][81]**
-   [Consultez LunarTech.ai pour des ressources GRATUITES][82]
-   Abonnez-vous à ma [**Newsletter Data Science et IA**][83]

[

LunarTech | Substack

Recherche en Machine Learning & IA avec plus de 5 millions de lecteurs de blog | 🌐 Bootcamp Data Science le mieux noté en 2024 | Présenté dans Forbes, Entrepreneur, Yahoo, Bloomberg et d'autres.

![apple-touch-icon-1024x1024](https://substackcdn.com/icons/substack/apple-touch-icon-1024x1024.png)SubstackSubstack

![https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfaccf84-5dd3-421e-ae5e-37cd6bfb8146_100x100](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdfaccf84-5dd3-421e-ae5e-37cd6bfb8146_100x100.jpeg)

][84]

Si vous souhaitez en savoir plus sur une carrière en Data Science, Machine Learning et IA, et apprendre comment décrocher un emploi en Data Science, vous pouvez télécharger gratuitement ce [guide des carrières en Data Science et IA][85].

[1]: #heading-variables-aleatoires
[2]: #heading-moyenne-variance-ecart-type
[3]: #heading-covariance
[4]: #heading-fonctions-de-distribution-de-probabilite
[5]: #heading-theoreme-de-bayes
[6]: #heading-regression-lineaire
[7]: #heading-theoreme-de-gauss-markov
[8]: #heading-proprietes-des-parametres
[9]: #heading-intervalles-de-confiance
[10]: #heading-tests-dhypotheses-statistiques
[11]: #heading-signification-statistique
[12]: #heading-erreur-de-type-i-et-de-type-ii
[13]: #heading-tests-statistiques
[14]: #heading-p-value-et-ses-limites
[15]: #heading-statistiques-inferentielles
[16]: #heading-theoreme-central-limite-et-loi-des-grands-nombres
[17]: #heading-techniques-de-reduction-de-dimensionnalite
[18]: #heading-preparation-aux-entretiens-top-7-des-questions-de-statistiques-avec-reponses
[19]: #heading-a-propos-de-lauteur
[20]: #heading-comment-aller-plus-loin
[21]: https://www.youtube.com/watch?v=HXL58Ikh7UM&t=244s
[22]: https://www.youtube.com/watch?v=TJSfLo49iTM&t=144s
[23]: https://lunartech.ai
[24]: https://www.freecodecamp.org/news/statistics-for-data-scientce-machine-learning-and-ai-handbook/LunarTech.ai
[25]: https://github.com/TatevKaren/mathematics-statistics-for-data-science/tree/main/Sampling%20Techniques
[26]: https://github.com/TatevKaren/mathematics-statistics-for-data-science/tree/main/Deriving%20Expectation%20and%20Variances%20of%20Densities
[27]: https://en.wikipedia.org/wiki/Bernoulli_distribution
[28]: https://en.wikipedia.org/wiki/Binomial_distribution
[29]: https://en.wikipedia.org/wiki/Poisson_distribution
[30]: https://en.wikipedia.org/wiki/Discrete_uniform_distribution
[31]: https://en.wikipedia.org/wiki/Normal_distribution
[32]: https://en.wikipedia.org/wiki/Continuous_uniform_distribution
[33]: https://en.wikipedia.org/wiki/Cauchy_distribution
[34]: https://brilliant.org/wiki/binomial-distribution/
[35]: https://lunartech.ai
[36]: https://www.freecodecamp.org/news/poisson-distribution-a-formula-to-calculate-probability-distribution/
[37]: https://brilliant.org/wiki/eulers-number/
[38]: https://lunartech.ai
[39]: https://www.freecodecamp.org/news/normal-distribution-explained/
[40]: https://www.mathsisfun.com/numbers/pi.html
[41]: https://lunartech.ai
[42]: https://lunartech.ai
[43]: https://www.google.com/url?sa=i&url=https%3A%2F%2Ffreakonometrics.hypotheses.org%2F9404&psig=AOvVaw2IcJrhGrWbt9504WTCWBwW&ust=1618940099743000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOjR4v7rivACFQAAAAAdAAAAABAI
[44]: https://lunartech.ai
[45]: https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/
[46]: https://en.wikipedia.org/wiki/Student%27s_t-test
[47]: https://en.wikipedia.org/wiki/F-test
[48]: https://en.wikipedia.org/wiki/Chi-squared_test
[49]: https://www.stata.com/support/faqs/statistics/durbin-wu-hausman-test/
[50]: https://en.wikipedia.org/wiki/White_test#:~:text=In%20statistics%2C%20the%20White%20test,by%20Halbert%20White%20in%201980.
[51]: https://en.wikipedia.org/wiki/Student%27s_t-distribution
[52]: https://www.geo.fu-berlin.de/en/v/soga/Basics-of-statistics/Hypothesis-Tests/Introduction-to-Hypothesis-Testing/Critical-Value-and-the-p-Value-Approach/index.html
[53]: https://www.google.com/search?q=t-table+two+sided&client=safari&rls=en&sxsrf=ALeKk01KSlU3EEtBeMcXPuh13ud42kRCWw:1618592162824&tbm=isch&source=iu&ictx=1&fir=ZGAb8l8KaBNJiM%252CZaqfSsY36WrUvM%252C_&vet=1&usg=AI4_-kSaUb_tv_3EBZQRhYaQVYYaJ1uBHQ&sa=X&ved=2ahUKEwjBtZrXnYPwAhWHgv0HHQPmASUQ9QF6BAgSEAE&biw=1981&bih=1044#imgrc=ZGAb8l8KaBNJiM
[54]: https://www.geo.fu-berlin.de/en/v/soga/Basics-of-statistics/Hypothesis-Tests/Introduction-to-Hypothesis-Testing/Critical-Value-and-the-p-Value-Approach/index.html
[55]: https://en.wikipedia.org/wiki/F-distribution
[56]: https://www.uio.no/studier/emner/sv/oekonomi/ECON4150/v18/lecture7_ols_multiple_regressors_hypothesis_tests.pdf
[57]: https://www.statisticshowto.com/probability-and-statistics/f-statistic-value-test/
[58]: https://www.sjsu.edu/faculty/gerstman/StatPrimer/t-table.pdf
[59]: http://www.z-table.com/
[60]: https://www.uio.no/studier/emner/sv/oekonomi/ECON4150/v18/lecture7_ols_multiple_regressors_hypothesis_tests.pdf
[61]: https://builtin.com/data-science/step-step-explanation-principal-component-analysis
[62]: https://en.wikipedia.org/wiki/Factor_analysis
[63]: https://en.wikipedia.org/wiki/Canonical_correlation
[64]: https://towardsdatascience.com/understanding-random-forest-58381e0602d2
[65]: https://docs.displayr.com/wiki/Kaiser_Rule
[66]: https://raw.githubusercontent.com/TatevKaren/Multivariate-Statistics/main/Elbow_rule_%25varc_explained.png
[67]: https://www.youtube.com/watch?v=QzAXW7kQ0I8&t=1707s
[68]: https://lunartech.ai/free-resources/
[69]: https://lunartech.ai/course-overview/
[70]: https://tatevaslanyan.com
[71]: https://lunartech.ai
[72]: https://lunartech.ai
[73]: https://lunartech.ai/course-overview/
[74]: https://lunartech.ai/pricing/
[75]: https://www.itpro.com/business-strategy/careers-training/358100/best-data-science-boot-camps
[76]: https://www.forbes.com.au/brand-voice/uncategorized/not-just-for-tech-giants-heres-how-lunartech-revolutionizes-data-science-and-ai-learning/
[77]: https://finance.yahoo.com/news/lunartech-launches-game-changing-data-115200373.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAAM3JyjdXmhpYs1lerU37d64maNoXftMA6BYjYC1lJM8nVa_8ZwTzh43oyA6Iz0DfqLtjVHnknO0Zb8QTLIiHuwKzQZoodeM85hkI39fta3SX8qauBUsNw97AeiBDR09BUDAkeVQh6eyvmNLAGblVj3GSf1iCo81bwHQxknmhgng#
[78]: https://www.entrepreneur.com/ka/business-news/outpacing-competition-how-lunartech-is-redefining-the/463038
[79]: https://substack.com/@lunartech
[80]: https://www.linkedin.com/in/tatev-karen-aslanyan/
[81]: https://www.youtube.com/@LunarTech_ai
[82]: https://lunartech.ai/free-resources/
[83]: https://tatevaslanyan.substack.com/
[84]: https://substack.com/@lunartech
[85]: https://downloads.tatevaslanyan.com/six-figure-data-science-ebook