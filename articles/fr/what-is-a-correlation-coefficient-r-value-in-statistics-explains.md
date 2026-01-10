---
title: Qu'est-ce qu'un coefficient de corrélation ? La valeur r en statistiques expliquée
subtitle: ''
author: Eric Leung
co_authors: []
series: null
date: '2020-07-08T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-correlation-coefficient-r-value-in-statistics-explains
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/positive_plots.png
tags:
- name: Mathematics
  slug: mathematics
- name: MathJax
  slug: mathjax
- name: statistics
  slug: statistics
seo_title: Qu'est-ce qu'un coefficient de corrélation ? La valeur r en statistiques
  expliquée
seo_desc: Correlations are a great tool for learning about how one thing changes with
  another. After reading this, you should understand what correlation is, how to think
  about correlations in your own work, and code up a minimal implementation to calculate
  co...
---

Les corrélations sont un excellent outil pour comprendre comment une chose change avec une autre. Après avoir lu ceci, vous devriez comprendre ce qu'est la corrélation, comment penser aux corrélations dans votre propre travail, et coder une implémentation minimale pour calculer les corrélations.

## Une corrélation concerne la manière dont deux choses changent ensemble

La corrélation est un concept mathématique abstrait, mais vous avez probablement déjà une idée de ce qu'elle signifie. Voici quelques exemples des trois catégories générales de corrélation.

Lorsque vous mangez plus de nourriture, vous vous sentirez probablement plus rassasié. C'est un cas où deux choses changent ensemble de la même manière. L'une augmente (manger plus de nourriture), puis l'autre augmente également (se sentir rassasié). **C'est une corrélation positive.**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/pos_plot.png align="left")

*Corrélation positive entre la nourriture mangée et la sensation de satiété. Plus on mange de nourriture, plus on se sent rassasié (tendance vers le haut à droite).* [*Code R*](https://gist.github.com/erictleung/d6bda6a61b8de03e76cb081257f183ee)

Lorsque vous êtes dans une voiture et qu'elle va plus vite, vous arriverez probablement plus rapidement à destination et votre temps de trajet total sera moindre. C'est un cas où deux choses changent dans des directions opposées (plus de vitesse, mais moins de temps). **C'est une corrélation négative.**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/neg_plot.png align="left")

*Corrélation négative entre la vitesse de la voiture et le temps de trajet. Plus la voiture est rapide, moins le temps de trajet est long (tendance vers le bas à droite).* [*Code R*](https://gist.github.com/erictleung/d6bda6a61b8de03e76cb081257f183ee)

Il existe également une troisième manière dont deux choses peuvent "changer". Ou plutôt, ne pas changer. Par exemple, si vous preniez du poids et que vous regardiez comment vos notes de test changent, il n'y aura probablement aucun schéma général de changement dans vos notes de test. **Cela signifie qu'il n'y a pas de corrélation.**

![Image](https://www.freecodecamp.org/news/content/images/2020/07/non_plot.png align="left")

*Un graphique exagéré de l'absence de corrélation entre la prise de poids et les notes de test.* [*Code R*](https://gist.github.com/erictleung/d6bda6a61b8de03e76cb081257f183ee)

## Savoir comment deux choses changent ensemble est la première étape vers la prédiction

Pouvoir décrire ce qui se passe dans nos exemples précédents est bien et tout. Mais quel est l'intérêt ? La raison est d'appliquer cette connaissance de manière significative pour aider à prédire ce qui va se passer ensuite.

Dans notre exemple de nourriture, nous pouvons enregistrer combien nous mangeons pendant une semaine entière, puis noter comment nous nous sentons rassasiés ensuite. Comme nous l'avons trouvé précédemment, plus nous mangeons, plus nous nous sentons rassasiés.

Après avoir collecté toutes ces informations, nous pouvons poser plus de questions sur pourquoi cela se produit pour mieux comprendre cette relation. Ici, nous pouvons commencer à nous demander quels types d'aliments nous rassasient davantage, ou si l'heure de la journée affecte également la sensation de satiété.

Un raisonnement similaire peut être appliqué à votre travail ou à votre entreprise. Si vous remarquez que les ventes ou d'autres métriques importantes augmentent ou diminuent avec d'autres mesures de votre entreprise (en d'autres termes, les choses sont positivement corrélées ou négativement corrélées), il peut être utile d'explorer et d'en apprendre davantage sur cette relation pour améliorer votre entreprise.

## Les corrélations peuvent avoir différents niveaux de force

Nous avons couvert certaines corrélations générales comme étant

* positives,

* négatives, ou

* inexistantes

Bien que ces descriptions soient acceptables, toutes les corrélations positives et négatives ne sont pas identiques.

Ces descriptions peuvent également être traduites en nombres. Une valeur de corrélation peut prendre n'importe quelle valeur décimale entre moins un (-1) et plus un (+1).

Les valeurs décimales entre (-1) et (0) sont des corrélations négatives, comme (-0,32).

Les valeurs décimales entre (0) et (+1) sont des corrélations positives, comme (+0,63).

Une corrélation parfaitement nulle signifie qu'il n'y a pas de corrélation.

Pour chaque type de corrélation, il existe une plage de corrélations fortes et de corrélations faibles. Les valeurs de corrélation **plus proches de zéro sont des corrélations plus faibles**, tandis que les valeurs **plus proches de positif ou négatif un sont des corrélations plus fortes**.

Les corrélations fortes montrent des tendances plus évidentes dans les données, tandis que les corrélations faibles semblent plus désordonnées. Par exemple, la corrélation positive forte ci-dessous ressemble davantage à une ligne par rapport à la corrélation positive plus faible et plus basse.

![Exemples de corrélations positives faibles, élevées et parfaites entre x et y](https://www.freecodecamp.org/news/content/images/2020/06/positive_plots-1.png align="left")

*Niveaux variables de corrélations positives.* [*Code R*](https://gist.github.com/erictleung/d6bda6a61b8de03e76cb081257f183ee)*.*

De même, les corrélations négatives fortes ont une tendance plus évidente que les corrélations négatives plus faibles et plus basses.

![Exemples de corrélations négatives faibles, élevées et parfaites entre x et y](https://www.freecodecamp.org/news/content/images/2020/07/negative_plots-2.png align="left")

*Niveaux variables de corrélations négatives.* [*Code R*](https://gist.github.com/erictleung/d6bda6a61b8de03e76cb081257f183ee)

## D'où vient la valeur *r* ? Et quelles valeurs peut-elle prendre ?

La « valeur *r* » est une manière courante d'indiquer une valeur de corrélation. Plus spécifiquement, elle fait référence à la corrélation de Pearson (échantillon), ou Pearson's *r*. La note « échantillon » est pour souligner que vous ne pouvez revendiquer la corrélation que pour les données que vous avez, et vous devez être prudent dans la formulation de revendications plus larges au-delà de vos données.

Le tableau ci-dessous résume ce que nous avons couvert sur les corrélations jusqu'à présent.

| Valeur r de Pearson | La corrélation entre deux choses est... | Exemple |
| --- | --- | --- |
| r = -1 | Parfaitement négative | Heure de la journée et nombre d'heures restantes dans la journée |
| r < 0 | Négative | Vitesse plus élevée des voitures et temps de trajet plus court |
| r = 0 | Indépendante ou non corrélée | Prise de poids et notes de test |
| r > 0 | Positive | Plus de nourriture mangée et sensation de satiété accrue |
| r = 1 | Parfaitement positive | Augmentation de mon âge et augmentation de votre âge |

Dans les prochaines sections, nous allons

* Décomposer l'équation mathématique pour calculer les corrélations

* Utiliser des exemples de nombres pour utiliser cette équation de corrélation

* Coder l'équation mathématique en Python et JavaScript

## Décomposer les mathématiques pour calculer les corrélations

Pour rappel, les corrélations ne peuvent être qu'entre (-1) et (1). Pourquoi ?

La réponse rapide est que nous ajustons la quantité de changement dans les deux variables à une échelle commune. En termes plus techniques, nous normalisons la quantité de changement des deux variables ensemble par la quantité de changement de chacune des deux variables par elles-mêmes.

À partir de [Wikipedia](https://en.wikipedia.org/wiki/Correlation_and_dependence#Sample_correlation_coefficient), nous pouvons obtenir la définition mathématique du coefficient de corrélation de Pearson. Cela semble très compliqué, mais décomposons-le ensemble.

$$\textcolor{lime}{r} { \textcolor{#4466ff}{x} \textcolor{fuchsia}{y} } = \frac{ \sum{i=1}^{n} (x_i - \textcolor{green}{\bar{x}})(y_i - \textcolor{olive}{\bar{y}}) }{ \sqrt{ \sum_{i=1}^{n} (x_i - \textcolor{green}{\bar{x}})^2 \sum_{i=1}^{n} (y_i - \textcolor{olive}{\bar{y}})^2 } }$$

À partir de cette équation, pour trouver la (\\textcolor{lime}{\\text{corrélation}}) entre une ( \\textcolor{#4466ff}{\\text{variable x}} ) et une ( \\textcolor{fuchsia}{\\text{variable y}} ), nous devons d'abord calculer la ( \\textcolor{green}{\\text{valeur moyenne pour toutes les valeurs x}} ) et la ( \\textcolor{olive}{ \\text{valeur moyenne pour toutes les valeurs y}} ).

Concentrons-nous sur le haut de l'équation, également connu sous le nom de numérateur. Pour chacune des variables (x) et (y), nous devons ensuite trouver la distance des valeurs (x) par rapport à la moyenne de (x), et faire la même soustraction avec (y).

Intuitivement, comparer toutes ces valeurs à la moyenne nous donne un point de référence pour voir combien de changement il y a dans l'une des variables.

Cela se voit dans la forme mathématique, (\\textcolor{#800080}{\\sum\_{i=1}^{n}}(\\textcolor{#000080}{x\_i - \\overline{x}})), (\\textcolor{#800080}{\\text{ajoute tout}}) les (\\textcolor{#000080}{\\text{différences entre}}) vos valeurs avec la valeur moyenne pour votre variable (x).

Dans le bas de l'équation, également connu sous le nom de dénominateur, nous faisons un calcul similaire. Cependant, avant d'additionner toutes les distances de nos valeurs et de leurs moyennes, nous les multiplierons par elles-mêmes (c'est ce que fait le ((\\ldots)^2)).

Ce dénominateur est ce qui "ajuste" la corrélation de sorte que les valeurs soient comprises entre (-1) et (1).

## Utiliser des nombres dans notre équation pour la rendre réelle

Pour démontrer les mathématiques, trouvons la corrélation entre les âges de vous et de vos frères et sœurs l'année dernière ([1, 2, 6]) et vos âges pour cette année ([2, 3, 7]). Notez que ceci est un petit exemple. Typiquement, vous voudriez beaucoup plus de trois échantillons pour avoir plus de confiance dans la véracité de votre corrélation.

En regardant les nombres, ils semblent augmenter de la même manière. Vous pouvez également remarquer qu'ils sont la même séquence de nombres, mais le deuxième ensemble de nombres a un ajouté. C'est aussi proche d'une corrélation parfaite que nous pouvons obtenir. En d'autres termes, nous devrions obtenir un (r = 1).

Tout d'abord, nous devons calculer les moyennes de chacun. La moyenne de ([1, 2, 6]) est ((1+2+6)/3 = 3) et la moyenne de ([2, 3, 7]) est ((2+3+7)/3 = 4). En remplissant notre équation, nous obtenons

$$r { x y } = \frac{ \sum{i=1}^{n} (x_i - 3)(y_i - 4) }{ \sqrt{ \sum_{i=1}^{n} (x_i - 3)^2 \sum_{i=1}^{n} (y_i - 4)^2 } }$$

En regardant le haut de l'équation, nous devons trouver les différences appariées de (x) et (y). Rappelez-vous, le (\\sum) est le symbole pour l'addition. Le haut devient alors simplement

$$(1-3)(2-4) + (2-3)(3-4) + (6-3)(7-4)$$

$$= (-2)(-2) + (-1)(-1) + (3)(3)$$

$$= 4 + 1 + 9 = 14$$

Ainsi, le haut devient 14.

$$r { x y } = \frac{ 14 }{ \sqrt{ \sum{i=1}^{n} (x_i - 3)^2 \sum_{i=1}^{n} (y_i - 4)^2 } }$$

Dans le bas de l'équation, nous devons faire des calculs très similaires, sauf en nous concentrant sur (x) et (x) séparément avant la multiplication.

Concentrons-nous d'abord sur ( \\sum\_{i=1}^n (x\_i - 3)^2 ). Rappelez-vous, (3) ici est la moyenne de toutes les valeurs (x). Ce nombre changera en fonction de vos données particulières.

$$(1-3)^2 + (2-3)^2 + (6-3)^2$$

$$= (-2)^2 + (-1)^2 + (3)^2 = 4 + 1 + 9 = 14$$

Et maintenant pour les valeurs (y).

$$(2-4)^2 + (3-4)^2 + (7-4)^2$$

$$(-2)^2 + (-1)^2 + (3)^2 = 4 + 1 + 9 = 14$$

Avec ces nombres remplis, nous pouvons les remettre dans notre équation et résoudre pour notre corrélation.

$$r _{ x y } = \frac{ 14 }{ \sqrt{ 14 \times 14 }} = \frac{14}{\sqrt{ 14^2}} = \frac{14}{14} = 1$$

Nous avons confirmé avec succès que nous obtenons (r = 1).

Bien que ceci soit un exemple simple, il est toujours préférable d'utiliser des exemples simples à des fins de démonstration. Cela montre que notre équation fonctionne effectivement, ce qui sera important lors de son codage dans la section suivante.

## Code Python et JavaScript pour le coefficient de corrélation de Pearson

Les mathématiques peuvent parfois être trop abstraites, alors codons cela pour que vous puissiez expérimenter. Pour rappel, voici l'équation que nous allons coder.

$$r { x y } = \frac{ \sum{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) }{ \sqrt{ \sum_{i=1}^{n} (x_i - \bar{x})^2 \sum_{i=1}^{n} (y_i - \bar{y})^2 } }$$

Après avoir passé en revue les mathématiques ci-dessus et lu le code ci-dessous, il devrait être un peu plus clair sur la manière dont tout fonctionne ensemble.

Voici la version Python de la corrélation de Pearson.

```python
import math


def pearson(x, y):
    """
    Calculer le coefficient de corrélation de Pearson des tableaux de même longueur.
    Le numérateur est la somme de la multiplication de (x - x_avg) et (y - y_avg).
    Le dénominateur est la racine carrée du produit entre la somme de 
    (x - x_avg)^2 et la somme de (y - y_avg)^2.
    """
    n = len(x)
    idx = range(n)
    
    # Moyennes
    avg_x = sum(x) / n
    avg_y = sum(y) / n
    
    numerator = sum([(x[i] - avg_x)*(y[i] - avg_y) for i in idx])
    
    denom_x = sum([(x[i] - avg_x)**2 for i in idx])
    denom_y = sum([(y[i] - avg_y)**2 for i in idx])
    denominator = math.sqrt(denom_x * denom_y)
    
    return numerator / denominator
```

Voici un exemple de notre code Python en action, et nous pouvons double vérifier notre travail en utilisant [une fonction de corrélation de Pearson](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html) du package SciPy.

```python
import numpy as np
import scipy.stats

# Créer des données fictives
x = np.arange(5, 15)  # array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])
y = np.array([24, 0, 58, 26, 82, 89, 90, 90, 36, 56])

# Utiliser un package pour calculer le r de Pearson
# Note : la variable p ci-dessous est la p-valeur pour le r de Pearson. Cela teste
#   à quelle distance notre corrélation est de zéro et a une tendance.
r, p = scipy.stats.pearsonr(x, y)
r  # 0.506862548805646

# Utiliser notre propre fonction
pearson(x, y)  # 0.506862548805646
```

Voici la version JavaScript de la corrélation de Pearson.

```javascript
function pearson(x, y) {
    let n = x.length;
    let idx = Array.from({length: n}, (x, i) => i);
    
    // Moyennes
    let avgX = x.reduce((a,b) => a + b) / n;
    let avgY = y.reduce((a,b) => a + b) / n;
    
    let numMult = idx.map(i => (x[i] - avg_x)*(y[i] - avg_y));
    let numerator = numMult.reduce((a, b) => a + b);
    
    let denomX = idx.map(i => Math.pow((x[i] - avgX), 2)).reduce((a, b) => a + b);
    let denomY = idx.map(i => Math.pow((y[i] - avgY), 2)).reduce((a, b) => a + b);
    let denominator = Math.sqrt(denomX * denomY);
    
    return numerator / denominator;
};
```

Voici un exemple de notre code JavaScript en action pour double vérifier notre travail.

```javascript
x = Array.from({length: 10}, (x, i) => i + 5)
// Array(10) [ 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 ]

y = [24, 0, 58, 26, 82, 89, 90, 90, 36, 56]

pearson(x, y)
// 0.506862548805646
```

N'hésitez pas à traduire la formule en Python ou en JavaScript pour mieux comprendre son fonctionnement.

## En conclusion

Les corrélations sont un outil utile et accessible pour mieux comprendre la relation entre deux mesures numériques. Cela peut être considéré comme un début pour les problèmes de prédiction ou simplement pour mieux comprendre votre entreprise.

Les valeurs de corrélation, le plus couramment utilisées comme Pearson's *r*, varient de (-1) à (+1) et peuvent être catégorisées en corrélation négative ((-1 < r < 0)), positive ((0 < r < 1)), et absence de corrélation ((r = 0)).

## Un aperçu du monde plus large des corrélations

Il existe plus d'une manière de calculer une corrélation. Ici, nous avons abordé le cas où les deux variables changent de la même manière. Il existe d'autres cas où une variable peut changer à un rythme différent, mais avoir toujours une relation claire. Cela donne lieu à ce qu'on appelle les [relations non linéaires](https://www.freecodecamp.org/news/how-machines-make-predictions-finding-correlations-in-complex-data-dfd9f0d87889/).

Notez que [la corrélation n'implique pas la causalité](https://www.freecodecamp.org/news/why-correlation-does-not-imply-causation-the-meaning-of-this-common-saying-in-statistics/). Si vous avez besoin d'exemples rapides pour comprendre pourquoi, [ne cherchez pas plus loin](http://tylervigen.com/spurious-correlations).

Ci-dessous se trouve une liste d'autres articles que j'ai rencontrés et qui m'ont aidé à mieux comprendre le coefficient de corrélation.

* Si vous souhaitez explorer une visualisation interactive sur la corrélation, consultez [ce site simple et fantastique](https://rpsychologist.com/d3/correlation/).

* En utilisant Python, il existe plusieurs façons d'implémenter une corrélation et il existe plusieurs types de corrélation. Ce [tutoriel excellent](https://realpython.com/numpy-scipy-pandas-correlation-python/) montre de bons exemples de code Python à expérimenter soi-même.

* Un [article de blog par Sabatian Sauer](https://sebastiansauer.github.io/correlation-intuition/) passe en revue les corrélations en utilisant des "rectangles de déviation moyenne", où chaque point crée un rectangle visuel à partir de chaque point en utilisant la moyenne, et l'illustre en utilisant le langage de programmation R.

* Et pour les personnes profondément curieuses, consultez [cet article montrant 13 façons de regarder le coefficient de corrélation](http://www.stat.berkeley.edu/~rabbee/correlation.pdf) (PDF).

Suivez-moi sur [Twitter](https://twitter.com/erictleung) et consultez mon [blog personnel](https://erictleung.com) où je partage d'autres informations et ressources utiles pour la programmation, les statistiques et l'apprentissage automatique.

Merci d'avoir lu !