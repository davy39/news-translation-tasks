---
title: Tutoriel SVM Machine Learning – Qu'est-ce que l'algorithme Support Vector Machine,
  expliqué avec des exemples de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-01T11:30:00.000Z'
originalURL: https://freecodecamp.org/news/svm-machine-learning-tutorial-what-is-the-support-vector-machine-algorithm-explained-with-code-examples
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/SVMs.png
tags:
- name: algorithms
  slug: algorithms
- name: Machine Learning
  slug: machine-learning
seo_title: Tutoriel SVM Machine Learning – Qu'est-ce que l'algorithme Support Vector
  Machine, expliqué avec des exemples de code
seo_desc: 'By Milecia McGregor

  Most of the tasks machine learning handles right now include things like classifying
  images, translating languages, handling large amounts of data from sensors, and
  predicting future values based on current values. You can choose ...'
---

Par Milecia McGregor

La plupart des tâches que le machine learning gère actuellement incluent des choses comme la classification d'images, la traduction de langues, la gestion de grandes quantités de données provenant de capteurs et la prédiction de valeurs futures basées sur les valeurs actuelles. Vous pouvez choisir différentes stratégies pour résoudre le problème que vous essayez de résoudre.

La bonne nouvelle ? Il existe un algorithme en machine learning qui gérera presque toutes les données que vous pouvez lui lancer. Mais nous y viendrons dans un instant.

## Apprentissage supervisé vs non supervisé

Deux des stratégies les plus couramment utilisées en machine learning incluent l'apprentissage supervisé et l'apprentissage non supervisé.

### Qu'est-ce que l'apprentissage supervisé ?

L'apprentissage supervisé est lorsque vous entraînez un modèle de machine learning en utilisant des données étiquetées. Cela signifie que vous avez des données qui ont déjà la bonne classification associée. Une utilisation courante de l'apprentissage supervisé est de vous aider à prédire des valeurs pour de nouvelles données.

Avec l'apprentissage supervisé, vous devrez reconstruire vos modèles à mesure que vous obtenez de nouvelles données pour vous assurer que les prédictions retournées sont toujours précises. Un exemple d'apprentissage supervisé serait l'étiquetage d'images de nourriture. Vous pourriez avoir un ensemble de données dédié uniquement aux images de pizza pour enseigner à votre modèle ce qu'est une pizza.

### Qu'est-ce que l'apprentissage non supervisé ?

L'apprentissage non supervisé est lorsque vous entraînez un modèle avec des données non étiquetées. Cela signifie que le modèle devra trouver ses propres caractéristiques et faire des prédictions basées sur la manière dont il classe les données.

Un exemple d'apprentissage non supervisé serait de donner à votre modèle des images de plusieurs types de nourriture sans étiquettes. L'ensemble de données aurait des images de pizza, de frites et d'autres aliments, et vous pourriez utiliser différents algorithmes pour faire en sorte que le modèle identifie uniquement les images de pizza sans aucune étiquette.

### Alors, qu'est-ce qu'un algorithme ?

Lorsque vous entendez les gens parler d'algorithmes de machine learning, rappelez-vous qu'ils parlent de différentes équations mathématiques.

Un algorithme est simplement une fonction mathématique personnalisable. C'est pourquoi la plupart des algorithmes ont des choses comme des fonctions de coût, des valeurs de poids et des fonctions de paramètres que vous pouvez échanger en fonction des données avec lesquelles vous travaillez. Au cœur du machine learning, il y a simplement un ensemble d'équations mathématiques qui doivent être résolues très rapidement.

C'est pourquoi il existe tant d'algorithmes différents pour gérer différents types de données. Un algorithme particulier est la machine à vecteurs de support (SVM) et c'est ce que cet article va couvrir en détail.

## Qu'est-ce qu'une SVM ?

Les machines à vecteurs de support sont un ensemble de méthodes d'apprentissage supervisé utilisées pour la classification, la régression et la détection d'anomalies. Toutes ces tâches sont courantes en machine learning.

Vous pouvez les utiliser pour détecter des cellules cancéreuses basées sur des millions d'images ou vous pouvez les utiliser pour prédire des itinéraires de conduite futurs avec un modèle de régression bien ajusté.

Il existe des types spécifiques de SVM que vous pouvez utiliser pour des problèmes particuliers de machine learning, comme la régression à vecteurs de support (SVR) qui est une extension de la classification à vecteurs de support (SVC).

La chose principale à garder à l'esprit ici est que ce ne sont que des équations mathématiques ajustées pour vous donner la réponse la plus précise possible aussi rapidement que possible.

Les SVM sont différentes des autres algorithmes de classification en raison de la manière dont elles choisissent la frontière de décision qui maximise la distance par rapport aux points de données les plus proches de toutes les classes. La frontière de décision créée par les SVM est appelée le classificateur à marge maximale ou l'hyperplan à marge maximale.

## Comment fonctionne une SVM

Un classificateur SVM linéaire simple fonctionne en traçant une ligne droite entre deux classes. Cela signifie que tous les points de données d'un côté de la ligne représenteront une catégorie et les points de données de l'autre côté de la ligne seront placés dans une catégorie différente. Cela signifie qu'il peut y avoir un nombre infini de lignes parmi lesquelles choisir.

Ce qui rend l'algorithme SVM linéaire meilleur que certains des autres algorithmes, comme les k-plus proches voisins, c'est qu'il choisit la meilleure ligne pour classer vos points de données. Il choisit la ligne qui sépare les données et qui est la plus éloignée possible des points de données les plus proches.

Un exemple en 2-D aide à comprendre tout le jargon du machine learning. Basiquement, vous avez des points de données sur une grille. Vous essayez de séparer ces points de données par la catégorie à laquelle ils devraient appartenir, mais vous ne voulez pas avoir de données dans la mauvaise catégorie. Cela signifie que vous essayez de trouver la ligne entre les deux points les plus proches qui maintient les autres points de données séparés.

Ainsi, les deux points de données les plus proches vous donnent les vecteurs de support que vous utiliserez pour trouver cette ligne. Cette ligne est appelée la frontière de décision.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/linear-svm.png)
_SVM linéaire_

La frontière de décision n'a pas besoin d'être une ligne. Elle est également appelée hyperplan car vous pouvez trouver la frontière de décision avec n'importe quel nombre de caractéristiques, pas seulement deux.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/non-linear-svm.png)
_SVM non linéaire utilisant le noyau RBF_

### Types de SVM

Il existe deux types différents de SVM, chacun utilisé pour des choses différentes :

* SVM simple : Typiquement utilisé pour les problèmes de régression linéaire et de classification.
* SVM à noyau : Plus flexible pour les données non linéaires car vous pouvez ajouter plus de caractéristiques pour ajuster un hyperplan au lieu d'un espace bidimensionnel.

## Pourquoi les SVM sont utilisées en machine learning

Les SVM sont utilisées dans des applications comme la reconnaissance d'écriture manuscrite, la détection d'intrusions, la détection de visages, la classification d'e-mails, la classification de gènes et dans les pages web. C'est l'une des raisons pour lesquelles nous utilisons les SVM en machine learning. Elles peuvent gérer à la fois la classification et la régression sur des données linéaires et non linéaires.

Une autre raison pour laquelle nous utilisons les SVM est qu'elles peuvent trouver des relations complexes entre vos données sans que vous ayez besoin de faire beaucoup de transformations vous-même. C'est une excellente option lorsque vous travaillez avec des ensembles de données plus petits qui ont des dizaines à des centaines de milliers de caractéristiques. Elles trouvent généralement des résultats plus précis par rapport à d'autres algorithmes en raison de leur capacité à gérer des ensembles de données petits et complexes.

Voici quelques-uns des avantages et inconvénients de l'utilisation des SVM.

### Avantages

* Efficaces sur des ensembles de données avec plusieurs caractéristiques, comme les données financières ou médicales.
* Efficaces dans les cas où le nombre de caractéristiques est supérieur au nombre de points de données.
* Utilise un sous-ensemble de points d'entraînement dans la fonction de décision appelés vecteurs de support, ce qui les rend efficaces en mémoire.
* Différentes fonctions noyau peuvent être spécifiées pour la fonction de décision. Vous pouvez utiliser des noyaux courants, mais il est également possible de spécifier des noyaux personnalisés.

### Inconvénients

* Si le nombre de caractéristiques est beaucoup plus grand que le nombre de points de données, éviter le surajustement lors du choix des fonctions noyau et du terme de régularisation est crucial.
* Les SVM ne fournissent pas directement d'estimations de probabilité. Celles-ci sont calculées en utilisant une validation croisée coûteuse à cinq plis.
* Fonctionnent mieux sur des ensembles d'échantillons réduits en raison de leur temps d'entraînement élevé.

Puisque les SVM peuvent utiliser n'importe quel nombre de noyaux, il est important que vous en connaissiez quelques-uns.

## Fonctions noyau

### Linéaire

Celles-ci sont couramment recommandées pour la classification de texte car la plupart de ces types de problèmes de classification sont linéairement séparables.

Le noyau linéaire fonctionne très bien lorsqu'il y a beaucoup de caractéristiques, et les problèmes de classification de texte ont beaucoup de caractéristiques. Les fonctions noyau linéaires sont plus rapides que la plupart des autres et vous avez moins de paramètres à optimiser.

Voici la fonction qui définit le noyau linéaire :

```
f(X) = w^T * X + b
```

Dans cette équation, **w** est le vecteur de poids que vous voulez minimiser, **X** est la donnée que vous essayez de classer, et **b** est le coefficient linéaire estimé à partir des données d'entraînement. Cette équation définit la frontière de décision que la SVM retourne.

### Polynomial

Le noyau polynomial n'est pas utilisé en pratique très souvent car il n'est pas aussi efficace sur le plan computationnel que d'autres noyaux et ses prédictions ne sont pas aussi précises.

Voici la fonction pour un noyau polynomial :

```
f(X1, X2) = (a + X1^T * X2) ^ b
```

C'est l'une des équations de noyau polynomial les plus simples que vous pouvez utiliser. **f(X1, X2)** représente la frontière de décision polynomiale qui séparera vos données. **X1** et **X2** représentent vos données.

### Fonction de base radiale gaussienne (RBF)

L'un des noyaux les plus puissants et couramment utilisés dans les SVM. Généralement le choix pour les données non linéaires.

Voici l'équation pour un noyau RBF :

```
f(X1, X2) = exp(-gamma * ||X1 - X2||^2)
```

Dans cette équation, **gamma** spécifie combien un seul point d'entraînement a d'influence sur les autres points de données autour de lui. **||X1 - X2||** est le produit scalaire entre vos caractéristiques.

### Sigmoïde

Plus utile dans les réseaux de neurones que dans les machines à vecteurs de support, mais il y a des cas d'utilisation spécifiques occasionnels.

Voici la fonction pour un noyau sigmoïde :

```
f(X, y) = tanh(alpha * X^T * y + C)
```

Dans cette fonction, **alpha** est un vecteur de poids et **C** est une valeur de décalage pour tenir compte de certaines mauvaises classifications de données qui peuvent se produire.

### Autres

Il existe de nombreux autres noyaux que vous pouvez utiliser pour votre projet. Cela peut être une décision à prendre lorsque vous devez répondre à certaines contraintes d'erreur, que vous souhaitez essayer d'accélérer le temps d'entraînement ou que vous souhaitez super ajuster les paramètres.

[Certains autres noyaux incluent](https://data-flair.training/blogs/svm-kernel-functions/) : ANOVA radial basis, tangente hyperbolique et Laplace RBF.

Maintenant que vous en savez un peu plus sur le fonctionnement des noyaux sous le capot, passons à quelques exemples.

## Exemples avec des ensembles de données

Pour vous montrer comment les SVM fonctionnent en pratique, nous allons passer par le processus d'entraînement d'un modèle avec celui-ci en utilisant la bibliothèque [Python Scikit-learn](https://scikit-learn.org/stable/). Celle-ci est couramment utilisée pour tous types de problèmes de machine learning et fonctionne bien avec d'autres bibliothèques Python.

Voici les étapes régulièrement trouvées dans les projets de machine learning :

* Importer l'ensemble de données
* Explorer les données pour comprendre à quoi elles ressemblent
* Prétraiter les données
* Diviser les données en attributs et étiquettes
* Diviser les données en ensembles d'entraînement et de test
* Entraîner l'algorithme SVM
* Faire quelques prédictions
* Évaluer les résultats de l'algorithme

Certaines de ces étapes peuvent être combinées en fonction de la manière dont vous gérez vos données. Nous allons faire un exemple avec un SVM linéaire et un SVM non linéaire. Vous pouvez trouver le [code pour ces exemples ici](https://github.com/flippedcoder/probable-waddle/blob/master/svm_point_ex.py).

### Exemple de SVM linéaire

Nous allons commencer par importer quelques bibliothèques qui faciliteront le travail avec la plupart des projets de machine learning.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import svm
```

Pour un exemple linéaire simple, nous allons simplement créer des données factices et cela servira de remplacement à l'importation d'un ensemble de données.

```python
# données linéaires
X = np.array([1, 5, 1.5, 8, 1, 9, 7, 8.7, 2.3, 5.5, 7.7, 6.1])
y = np.array([2, 8, 1.8, 8, 0.6, 11, 10, 9.4, 4, 3, 8.8, 7.5])
```

La raison pour laquelle nous travaillons avec des tableaux numpy est de rendre les opérations matricielles plus rapides car elles utilisent moins de mémoire que les listes Python. Vous pourriez également tirer parti de la typage du contenu des tableaux. Maintenant, regardons à quoi ressemblent les données dans un graphique :

```python
# montrer les données non classées
plt.scatter(X, y)
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/linear-svm_raw.png)

Une fois que vous voyez à quoi ressemblent les données, vous pouvez faire une meilleure estimation de l'algorithme qui fonctionnera le mieux pour vous. Gardez à l'esprit que c'est un ensemble de données vraiment simple, donc la plupart du temps vous devrez faire un peu de travail sur vos données pour les rendre utilisables.

Nous allons faire un peu de prétraitement sur le code déjà structuré. Cela mettra les données brutes dans un format que nous pouvons utiliser pour entraîner le modèle SVM.

```python
# mise en forme des données pour l'entraînement du modèle
training_X = np.vstack((X, y)).T
training_y = [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1]
```

Maintenant, nous pouvons créer le modèle SVM en utilisant un noyau linéaire.

```python
# définir le modèle
clf = svm.SVC(kernel='linear', C=1.0)
```

Cette seule ligne de code vient de créer un modèle entier de machine learning. Maintenant, nous devons simplement l'entraîner avec les données que nous avons prétraitées.

```python
# entraîner le modèle
clf.fit(training_X, training_y)
```

C'est ainsi que vous pouvez construire un modèle pour n'importe quel projet de machine learning. L'ensemble de données que nous avons peut être petit, mais si vous rencontrez un ensemble de données du monde réel qui peut être classé avec une frontière linéaire, ce modèle fonctionne toujours.

Avec votre modèle entraîné, vous pouvez faire des prédictions sur la manière dont un nouveau point de données sera classé et vous pouvez faire un graphique de la frontière de décision. Faisons un graphique de la frontière de décision.

```python
# obtenir les valeurs de poids pour l'équation linéaire à partir du modèle SVM entraîné
w = clf.coef_[0]

# obtenir le décalage y pour l'équation linéaire
a = -w[0] / w[1]

# créer l'espace de l'axe x pour les points de données
XX = np.linspace(0, 13)

# obtenir les valeurs y pour tracer la frontière de décision
yy = a * XX - clf.intercept_[0] / w[1]

# tracer la frontière de décision
plt.plot(XX, yy, 'k-')

# montrer le graphique visuellement
plt.scatter(training_X[:, 0], training_X[:, 1], c=training_y)
plt.legend()
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/linear-svm.png)

### Exemple de SVM non linéaire

Pour cet exemple, nous allons utiliser un ensemble de données légèrement plus compliqué pour montrer l'un des domaines où les SVM excellent. Importons quelques packages.

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm
```

Cet ensemble d'importations est similaire à celui de l'exemple linéaire, sauf qu'il importe une chose de plus. Maintenant, nous pouvons utiliser un ensemble de données directement depuis la bibliothèque Scikit-learn.

```python
# données non linéaires
circle_X, circle_y = datasets.make_circles(n_samples=300, noise=0.05)
```

L'étape suivante consiste à regarder à quoi ressemblent ces données brutes avec un graphique.

```python
# montrer les données non linéaires brutes
plt.scatter(circle_X[:, 0], circle_X[:, 1], c=circle_y, marker='.')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/nonlinear-svm_raw.png)

Maintenant que vous pouvez voir comment les données sont séparées, nous pouvons choisir un SVM non linéaire pour commencer. Cet ensemble de données n'a pas besoin de prétraitement avant de l'utiliser pour entraîner le modèle, donc nous pouvons sauter cette étape. Voici à quoi ressemblera le modèle SVM pour cela :

```python
# créer un algorithme non linéaire pour le modèle
nonlinear_clf = svm.SVC(kernel='rbf', C=1.0)
```

Dans ce cas, nous allons utiliser un [noyau RBF (Gaussian Radial Basis Function)](http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=MachineLearning&doc=exercises/ex8/ex8.html) pour classer ces données. Vous pourriez également essayer le noyau polynomial pour voir la différence entre les résultats que vous obtenez. Il est maintenant temps d'entraîner le modèle.

```python
# entraînement du modèle non linéaire
nonlinear_clf.fit(circle_X, circle_y)
```

Vous pouvez commencer à étiqueter de nouvelles données dans la bonne catégorie en fonction de ce modèle. Pour voir à quoi ressemble la frontière de décision, nous devrons créer une fonction personnalisée pour la tracer.

```python
# Tracer la frontière de décision pour un problème SVM non linéaire
def plot_decision_boundary(model, ax=None):
    if ax is None:
        ax = plt.gca()
        
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # créer une grille pour évaluer le modèle
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)

	# mise en forme des données
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    
	# obtenir la frontière de décision basée sur le modèle
    P = model.decision_function(xy).reshape(X.shape)
    
    # tracer la frontière de décision
    ax.contour(X, Y, P,
               levels=[0], alpha=0.5,
               linestyles=['-'])
```

Vous avez tout ce dont vous avez besoin pour tracer la frontière de décision pour ces données non linéaires. Nous pouvons le faire avec quelques lignes de code qui utilisent la bibliothèque [Matlibplot](https://matplotlib.org/), tout comme les autres graphiques.

```python
# tracer les données et la frontière de décision
plt.scatter(circle_X[:, 0], circle_X[:, 1], c=circle_y, s=50)
plot_decision_boundary(nonlinear_clf)
plt.scatter(nonlinear_clf.support_vectors_[:, 0], nonlinear_clf.support_vectors_[:, 1], s=50, lw=1, facecolors='none')
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/nonlinear-svm.png)

Lorsque vous avez vos données et que vous connaissez le problème que vous essayez de résoudre, cela peut vraiment être aussi simple.

Vous pouvez changer complètement votre modèle d'entraînement, vous pouvez choisir différents algorithmes et caractéristiques à utiliser, et vous pouvez affiner vos résultats en fonction de plusieurs paramètres. Il existe des bibliothèques et des packages pour tout cela maintenant, donc il n'y a pas beaucoup de mathématiques que vous devez gérer.

## Conseils pour les problèmes du monde réel

Les ensembles de données du monde réel ont quelques problèmes courants en raison de leur taille, des types de données variés qu'ils contiennent et de la puissance de calcul nécessaire pour entraîner un modèle.

Il y a quelques choses auxquelles vous devez faire attention avec les SVM en particulier :

* Assurez-vous que vos données sont sous forme numérique plutôt que catégorielle. Les SVM attendent des nombres au lieu d'autres types d'étiquettes.
* Évitez de copier les données autant que possible. Certaines bibliothèques Python créeront des doublons de vos données si elles ne sont pas dans un format spécifique. Copier les données ralentira également votre temps d'entraînement et faussera la manière dont votre modèle attribue les poids à une caractéristique spécifique.
* Surveillez la taille du cache du noyau car il utilise votre RAM. Si vous avez un ensemble de données vraiment grand, cela pourrait causer des problèmes pour votre système.
* Mettez à l'échelle vos données car les algorithmes SVM ne sont pas invariants à l'échelle. Cela signifie que vous pouvez convertir toutes vos données pour qu'elles soient dans les plages [0, 1] ou [-1, 1].

## Autres réflexions

Vous pourriez vous demander pourquoi je ne suis pas entré dans les détails approfondis des mathématiques ici. C'est principalement parce que je ne veux pas effrayer les gens et les empêcher d'en apprendre davantage sur le machine learning.

C'est amusant d'apprendre ces longues équations mathématiques compliquées et leurs dérivations, mais il est rare que vous écriviez vos propres algorithmes et que vous rédigez des preuves sur des projets réels.

C'est comme utiliser la plupart des autres choses que vous faites tous les jours, comme votre téléphone ou votre ordinateur. Vous pouvez faire tout ce dont vous avez besoin sans savoir comment les processeurs sont construits.

Le machine learning est comme toute autre application d'ingénierie logicielle. Il existe une tonne de packages qui facilitent l'obtention des résultats dont vous avez besoin sans avoir un arrière-plan approfondi en statistiques.

Une fois que vous avez un peu de pratique avec les différents packages et bibliothèques disponibles, vous découvrirez que la partie la plus difficile du machine learning est d'obtenir et d'étiqueter vos données.

Je travaille sur une chose basée sur la neuroscience, le machine learning et le web ! Vous devriez me suivre sur [Twitter](https://twitter.com/flippedcoding) pour en apprendre davantage à ce sujet et sur d'autres trucs technologiques cool.