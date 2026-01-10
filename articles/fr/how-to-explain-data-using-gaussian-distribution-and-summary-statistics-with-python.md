---
title: Comment expliquer les données à l'aide de la distribution gaussienne et des
  statistiques récapitulatives avec Python
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2020-11-27T02:28:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-explain-data-using-gaussian-distribution-and-summary-statistics-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/1.jpeg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: Python
  slug: python
- name: statistics
  slug: statistics
seo_title: Comment expliquer les données à l'aide de la distribution gaussienne et
  des statistiques récapitulatives avec Python
seo_desc: 'Once you understand the taxonomy of data, you should learn to apply a few
  essential foundational concepts that help describe the data using a set of statistical
  methods.

  Before we dive into data and its distribution, we should understand the differen...'
---

Une fois que vous comprenez la [taxonomie des données](https://towardsdatascience.com/types-of-structured-data-every-data-science-enthusiast-should-know-a656b95afbe2), vous devriez apprendre à appliquer quelques concepts fondamentaux essentiels qui aident à décrire les données à l'aide d'un ensemble de méthodes statistiques.

Avant de plonger dans les données et leur distribution, nous devons comprendre la différence entre deux mots-clés très importants - **échantillon** et **population**.

Un *échantillon* est un instantané de données provenant d'un ensemble de données plus large. Cet ensemble de données plus large, qui représente toutes les données pouvant être collectées, est appelé *population*.

En statistiques, la population est un ensemble large, défini et souvent théorique de toutes les observations possibles générées par une expérience ou un domaine.

Les observations dans un ensemble de données d'échantillon suivent souvent un certain type de distribution, communément appelée **distribution normale**, et formellement appelée **distribution gaussienne**. Il s'agit de la distribution la plus étudiée, et il existe un sous-domaine entier des statistiques dédié aux données gaussiennes.

## Ce que nous allons couvrir

Dans cet article, nous allons nous concentrer sur la compréhension de :

* la distribution gaussienne et comment elle peut être utilisée pour décrire les données et les observations d'un modèle d'apprentissage automatique.

* **estimations de localisation** — la tendance centrale d'une distribution.

* **estimations de variabilité** — la dispersion des données par rapport à la moyenne dans la distribution.

* les extraits de code pour générer des données normalement distribuées et calculer des estimations à l'aide de divers packages Python comme [numpy](https://towardsdatascience.com/numpy-essentials-for-data-science-25dc39fae39), [scipy](https://www.scipy.org/docs.html), [matplotlib](https://matplotlib.org/), et ainsi de suite.

Et avec cela, commençons.

## Qu'est-ce qu'une distribution normale ou gaussienne ?

Lorsque nous traçons un ensemble de données tel qu'un histogramme, la forme de ce graphique est ce que nous appelons sa distribution. La forme la plus couramment observée des valeurs continues est la courbe en cloche, également appelée distribution gaussienne ou normale.

Elle porte le nom du mathématicien allemand, Carl Friedrich Gauss. Voici quelques exemples courants d'ensembles de données qui suivent une distribution gaussienne :

* Température corporelle

* Taille des personnes

* Kilométrage des voitures

* Scores de QI

Essayons de générer la distribution normale idéale et de la tracer à l'aide de Python.

### Comment tracer une distribution gaussienne en Python

Nous avons des bibliothèques comme Numpy, scipy et matplotlib pour nous aider à tracer une courbe normale idéale.

```py
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt 

## générer les données et les tracer pour une courbe normale idéale

## axe x pour le graphique
x_data = np.arange(-5, 5, 0.001)

## axe y comme la gaussienne
y_data = stats.norm.pdf(x_axis, 0, 1)

## tracer les données
plt.plot(x_data, y_data)
plt.show()
```

Sortie :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/2-2.png align="left")

Les points sur l'axe des x sont les observations et l'axe des y est la probabilité de chaque observation.

Nous avons généré des observations régulièrement espacées dans la plage (-5, 5) en utilisant `np.arange()`. Ensuite, nous l'avons passé à la fonction `norm.pdf()` avec une moyenne de 0,0 et un écart-type de 1, ce qui a retourné la probabilité de cette observation.

Les observations autour de 0 sont les plus courantes et celles autour de -5,0 et 5,0 sont rares. Le terme technique pour la fonction `pdf()` est la [**fonction de densité de probabilité**](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html).

## Comment tester une distribution gaussienne

Il est important de noter que toutes les données ne suivent pas une distribution gaussienne, et nous devons découvrir la distribution soit en examinant les graphiques d'histogrammes des données, soit en implémentant certains tests statistiques.

Voici quelques exemples d'observations qui ne suivent pas une distribution gaussienne et qui peuvent plutôt suivre une distribution exponentielle (forme de crosse de hockey) :

* Revenus des personnes

* Population des pays

* Ventes de voitures.

Jusqu'à présent, nous avons simplement parlé de la courbe en forme de cloche idéale de la distribution, mais si nous devions travailler avec des données aléatoires et déterminer leur distribution.

Voici comment nous allons procéder :

* Créer des données aléatoires pour cet exemple en utilisant la fonction `randn()` de numpy.

* Tracer les données à l'aide d'un histogramme et analyser le graphique retourné pour la forme attendue.

En réalité, les données sont rarement parfaitement gaussiennes, mais elles auront une distribution de type gaussien. Si la taille de l'échantillon est suffisamment grande, nous la traitons comme gaussienne.

Notez que vous devrez peut-être modifier la configuration de traçage (échelle, nombre de bacs, etc.) pour rechercher le motif souhaité.

Examinons un peu de code :

```py
## définir la graine pour la génération aléatoire
np.random.seed(1)

## générer des données univariées
data = 10 * np.random.randn(1000) + 100

## tracer les données
plt.hist(data)
plt.show()
```

Sortie :

Voici le résultat du code ci-dessus avec le graphique d'histogramme des données :

![Image for post](https://www.freecodecamp.org/news/content/images/2020/11/3-1.png align="left")

Le graphique ressemble davantage à un simple ensemble de blocs. Mais nous changeons l'échelle, qui dans ce cas est le nombre arbitraire de bacs dans l'histogramme.

Spécifions le nombre de bacs et traçons-le à nouveau :

```py
plt.hist(data, bins=100)
plt.show()
```

![Image for post](https://www.freecodecamp.org/news/content/images/2020/11/4-1.png align="left")

Nous pouvons maintenant voir que la courbe ressemble davantage à une courbe en cloche gaussienne.

Cependant, notez que nous avons quelques observations qui sortent des limites et peuvent être considérées comme du bruit.

Cela souligne un autre point important lors du travail avec un ensemble de données d'échantillon — vous devez toujours vous attendre à un certain bruit ou à des valeurs aberrantes.

## Estimations de localisation

Une étape fondamentale dans l'exploration d'un ensemble de données consiste à obtenir une valeur récapitulative pour chaque caractéristique ou variable. Il s'agit généralement d'une estimation de l'endroit où se trouvent la plupart des données, ou en d'autres termes, la **tendance centrale**.

Au premier abord, résumer les données peut sembler simple — il suffit de prendre la moyenne des données. En réalité, bien que la moyenne soit très facile à calculer et à utiliser, elle n'est pas toujours la meilleure mesure pour la valeur centrale.

Pour résoudre ce problème, les statisticiens ont développé des estimations alternatives à la moyenne.

Nous allons utiliser l'ensemble de données Boston du package sklearn.

Notez que j'ai supprimé quelques colonnes, et voici à quoi ressemble le dataframe maintenant :

![Image for post](https://www.freecodecamp.org/news/content/images/2020/11/5-1.png align="left")

Examinons les estimations de localisation couramment utilisées à l'aide d'un ensemble de données d'échantillon réel, plutôt que de symboles grecs :

### Moyenne

La somme de toutes les valeurs divisée par le nombre de valeurs, également connue sous le nom de moyenne.

Voici comment calculer la moyenne de la variable `Age` :

```py
df['Age'].mean()

## sortie : 68.57490118577076
```

### Moyenne pondérée

La somme de toutes les valeurs multipliées par un poids divisée par la somme des poids. Cela est également connu sous le nom de moyenne pondérée.

Voici deux motivations principales pour utiliser une moyenne pondérée :

* Certaines observations sont intrinsèquement plus variables (écart-type élevé) que d'autres, et les observations très variables se voient attribuer un poids inférieur.

* Les données collectées ne représentent pas de manière égale les différents groupes que nous souhaitons mesurer.

### Médiane

La valeur qui sépare une moitié des données de l'autre, divisant ainsi en une moitié supérieure et une moitié inférieure. Cela est également appelé le 50e percentile.

Voici comment calculer la médiane de la variable `Age` :

```py
df['Age'].median()

## sortie : 77.5
```

### Percentile

La valeur telle que *P* pour cent des données se situent en dessous, également connue sous le nom de quantile.

La méthode `describe` facilite la recherche du percentile :

```py
df.describe()
```

![Image for post](https://www.freecodecamp.org/news/content/images/2020/11/6-1.png align="left")

Cela donne des statistiques récapitulatives de toutes les variables numériques. Notez que les métriques sont différentes pour les variables catégorielles.

### Médiane pondérée

La valeur telle qu'une moitié de la somme des poids se situe au-dessus et en dessous des données triées.

### Moyenne tronquée

La moyenne de toutes les valeurs après avoir supprimé un nombre fixe de valeurs extrêmes.

Une moyenne tronquée élimine l'influence des valeurs extrêmes. Par exemple, lors du jugement d'un événement, nous pouvons calculer le score final en utilisant la moyenne tronquée de tous les scores afin qu'aucun juge ne puisse manipuler le résultat.

Cela est également connu sous le nom de moyenne tronquée.

Pour cela, nous allons utiliser le module stats de la bibliothèque `scipy` :

```py
## trim = 0.1 supprime 10% de chaque extrémité

stats.trim_mean(df['Age'], 0.1)

## sortie : 71.19605911330049
```

### Valeur aberrante

Une valeur aberrante, ou valeur extrême, est une valeur de données très différente de la plupart des données. La médiane est appelée une estimation *robuste* de la localisation car elle n'est pas influencée par les *valeurs aberrantes*, c'est-à-dire les cas extrêmes, alors que la moyenne est sensible aux valeurs aberrantes.

## Estimations de variabilité

![Image for post](https://www.freecodecamp.org/news/content/images/2020/11/7-1.png align="left")

Outre la localisation, nous avons une autre méthode pour résumer une caractéristique. La **variabilité**, également appelée dispersion, nous indique à quel point les données sont étalées ou regroupées.

Calcul des mesures de variabilité pour le même dataframe à l'aide de bibliothèques comme pandas, numpy et scipy.

### Écarts

La différence entre les valeurs observées et l'estimation de la localisation. Les écarts sont parfois appelés erreurs ou résidus.

### Variance

La somme des écarts quadratiques par rapport à la moyenne divisée par *n* — 1 où *n* est le nombre de valeurs de données. Cela est également appelé l'erreur quadratique moyenne.

```py
df['Age'].var()
```

### Écart-type

La racine carrée de la variance.

```py
df['Age'].std()

## sortie : 28.148861406903617
```

### Écart absolu moyen

La moyenne des valeurs absolues des écarts par rapport à la moyenne. Cela est également appelé la norme l1 ou norme de Manhattan.

J'ai couvert cela plus en détail avec une explication mathématique ici : [Calcul des normes P-Norms des vecteurs — Algèbre linéaire pour la science des données -IV](https://towardsdatascience.com/calculating-vector-p-norms-linear-algebra-for-data-science-iv-400511cffcf0)

### Écart absolu médian par rapport à la médiane

La médiane des valeurs absolues des écarts par rapport à la médiane.

```py
df['Age'].mad()

## sortie : 24.610885188020433
```

### Étendue

La différence entre la plus grande et la plus petite valeur dans un ensemble de données.

Nous pouvons calculer l'étendue d'une variable en utilisant le min et le max des statistiques récapitulatives du dataframe :

```py
df['Age'].iloc[df['Age'].idxmax] - df['Age'].iloc[df['Age'].idxmin()]

## sortie : 97.1
```

### Statistiques d'ordre

Les statistiques d'ordre, ou rangs, sont des métriques basées sur les valeurs de données triées de la plus petite à la plus grande.

### Percentile

La valeur telle que *P* pour cent des valeurs prennent cette valeur ou moins et (100–P) pour cent prennent cette valeur ou plus. Cela est parfois appelé quantile.

### Étendue interquartile

L'étendue interquartile, ou IQR, est la différence entre le 75e percentile et le 25e percentile.

```py
Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

## Sortie : 49.04999999999999
```

Maintenant que vous avez une compréhension claire de la distribution gaussienne et des estimations courantes de localisation et de variabilité, vous pouvez résumer et interpréter les données facilement en utilisant ces méthodes statistiques.

## [Data Science with Harshit](https://www.youtube.com/c/DataSciencewithHarshit?sub_confirmation=1)

[Contenu intégré](https://cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F_ANbV9lVA-M%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D_ANbV9lVA-M&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F_ANbV9lVA-M%2Fhqdefault.jpg&key=a19fcc184b9711e1b4764040d3dc5c07&type=text%2Fhtml&schema=youtube)

Avec cette chaîne, je prévois de lancer quelques [séries couvrant tout l'espace de la science des données](https://towardsdatascience.com/hitchhikers-guide-to-learning-data-science-2cc3d963b1a2?source=---------8------------------). Voici pourquoi vous devriez vous abonner à la [chaîne](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) :

* Cette série couvrira tous les tutoriels de qualité requis/demandés sur chacun des sujets et sous-sujets comme [Python fundamentals for Data Science](https://towardsdatascience.com/python-fundamentals-for-data-science-6c7f9901e1c8?source=---------5------------------).

* Explications des [mathématiques et dérivations](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea?source=---------9------------------) de pourquoi nous faisons ce que nous faisons en ML et Deep Learning.

* [Podcasts avec des scientifiques des données et des ingénieurs](https://www.youtube.com/watch?v=a2pkZCleJwM&t=2s) chez Google, Microsoft, Amazon, et PDG de grandes entreprises axées sur les données.

* [Projets et instructions](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb?source=---------2------------------) pour implémenter les sujets appris jusqu'à présent. Apprenez les nouvelles certifications, Bootcamps et ressources pour obtenir ces certifications comme cet [**examen de certificat de développeur TensorFlow par Google**](https://youtu.be/yapSsspJzAw).

Si ce tutoriel était utile, vous devriez consulter mes cours de science des données et d'apprentissage automatique sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une base solide de travail à présenter.