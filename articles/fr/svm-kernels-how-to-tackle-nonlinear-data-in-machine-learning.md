---
title: 'Noyaux SVM expliqués : comment gérer les données non linéaires en Machine
  Learning'
subtitle: ''
author: Josiah Adesola
co_authors: []
series: null
date: '2025-01-06T22:32:35.270Z'
originalURL: https://freecodecamp.org/news/svm-kernels-how-to-tackle-nonlinear-data-in-machine-learning
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1735894336456/dae0caa1-7c01-4b88-a748-79d682bbed78.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: MathJax
  slug: mathjax
seo_title: 'Noyaux SVM expliqués : comment gérer les données non linéaires en Machine
  Learning'
seo_desc: 'Have you ever considered how your phone can recognize handwritten text
  and convert it into regular computer text? Or how your email can separate messages
  automatically into spam and non-spam categories?

  Both of these examples work based on classifica...'
---

Avez-vous déjà réfléchi à la manière dont votre téléphone peut reconnaître le texte manuscrit et le convertir en texte informatique régulier ? Ou comment votre email peut séparer automatiquement les messages en spam et non-spam ?

Ces deux exemples fonctionnent sur la base de tâches de classification, tout comme la fonction de reconnaissance faciale sur votre téléphone.

Lors de la création d'un algorithme de classification, les données du monde réel ont souvent une relation non linéaire. Et de nombreux algorithmes de classification de machine learning ont du mal avec les algorithmes non linéaires. Mais dans cet article, nous allons voir comment les fonctions noyau des machines à vecteurs de support (SVM) peuvent aider à résoudre ce problème. Nous allons approfondir une implémentation Python de la classification non linéaire et des fonctions noyau SVM.

## Prérequis

1. [Compréhension de base du Machine Learning](https://www.freecodecamp.org/news/learn-machine-learning-in-2024/)
    
2. [Bases de l'algèbre linéaire](https://www.freecodecamp.org/news/linear-algebra-full-course/)
    
3. [Compétences de base en programmation Python](https://www.freecodecamp.org/news/ultimate-beginners-python-course/)
    
4. [Compréhension de la visualisation de données](https://www.freecodecamp.org/news/learn-data-visualization-in-this-free-17-hour-course/)
    
5. [Un compte Google Colab](https://colab.research.google.com/) ou [Jupyter Notebook](https://www.anaconda.com/)
    

## Table des matières

1. [Aperçu de la technique des machines à vecteurs de support (SVM)](#heading-aperçu-de-la-technique-des-machines-à-vecteurs-de-support-svm)
    
2. [Fondamentaux du SVM](#heading-fondamentaux-du-svm)
    
3. [Fonction objectif du SVM](#heading-fonction-objectif-du-svm)
    
4. [Comprendre les fonctions noyau](#heading-comprendre-les-fonctions-noyau)
    
5. [Fonctions noyau populaires](#heading-fonctions-noyau-populaires)
    
6. [Comment choisir le bon noyau](#heading-comment-choisir-le-bon-noyau)
    
7. [Implémentation du noyau SVM](#heading-implémentation-du-noyau-svm)
    
8. [Conclusion](#heading-conclusion)
    

## Aperçu de la technique des machines à vecteurs de support (SVM)

Les machines à vecteurs de support (SVM) sont un algorithme d'apprentissage supervisé. Elles utilisent un hyperplan qui divise les caractéristiques à l'intérieur d'un espace de caractéristiques en catégories distinctes. Elles sont efficaces pour les applications de classification et de régression.

En identifiant la ligne ou le plan de division optimal qui servira de frontière de décision, le SVM cherche à maximiser la marge entre les différentes variables cibles. Il est principalement utilisé dans les tâches de classification et est très utile pour ignorer les valeurs aberrantes. Il catégorise les points de données des caractéristiques dans le jeu de données en sorties ou classes distinctes.

![Comparaison des frontières de décision utilisant SVC avec différents noyaux sur un jeu de données.](https://cdn.hashnode.com/res/hashnode/image/upload/v1734965953633/54d38f2a-8062-4bcb-8cc6-9795064241de.png align="center")

Le SVM cherche à atteindre la marge maximale optimale et une séparation idéale ou quasi parfaite. Il existe diverses applications pour le SVM, telles que la classification d'images, la détection de visages, la classification de texte, la classification d'images et la bioinformatique. Le SVM est également efficace dans les problèmes de classification linéaire et non linéaire.

### Importance des méthodes à noyau dans le SVM

La classification non linéaire est un type de classification qui implique de catégoriser des caractéristiques ayant des frontières de décision non linéaires, courbes ou complexes. Les frontières de décision sont des régions de l'espace qui séparent deux classes différentes.

Dans les tâches de classification linéaire, la région de l'espace entre les différentes classes, comme si l'email est du spam ou non, peut être facilement séparée avec une ligne droite. Mais dans les relations non linéaires, elle pourrait avoir une frontière de décision circulaire, parabolique ou de forme complexe.

Les tâches de classification non linéaire ont des motifs qui ne peuvent pas être découverts par des modèles linéaires. Cela est dû au fait que les caractéristiques ont une relation non linéaire entre elles.

[![Deux diagrammes illustrant les frontières de décision entre deux classes : (a) montre une frontière de décision complexe et ondulée, tandis que (b) montre une frontière plus simple et plus lisse. Les points bleus représentent la classe A, et les triangles rouges représentent la classe B. Techniques de Machine Learning pour l'imagerie THz et la spectroscopie dans le domaine temporel par Hochong Park et Joo-Huik Son](https://cdn.hashnode.com/res/hashnode/image/upload/v1735885699184/222d7252-7ece-4e31-97f5-577bb8577797.png align="center")](https://www.researchgate.net/publication/349186066_Machine_Learning_Techniques_for_THz_Imaging_and_Time-Domain_Spectroscopy)

Le SVM, en tant qu'algorithme de classification linéaire, n'est pas efficace pour des données non linéaires. Pour gérer ce type de données, il nécessitera une méthode à noyau, qui est le sujet principal de cet article.

Une méthode à noyau est une technique utilisée dans le SVM pour transformer des données non linéaires en dimensions supérieures. Par exemple, si les données ont une frontière de décision complexe dans un espace 2D (comme je l'expliquerai plus loin dans cet article), elles peuvent être transformées en un espace 3D. Cela permet une classification efficace avec un simple plan linéaire.

Le but de cet article est de vous enseigner les noyaux SVM et leur application aux tâches de classification non linéaire.

## Fondamentaux du SVM

### Classificateurs linéaires et maximisation de la marge

Les classificateurs linéaires sont des algorithmes de classification qui font des prédictions en utilisant une ligne droite de meilleur ajustement comme frontière de décision entre deux ou plusieurs catégories.

Les plans marginaux sont utilisés pour déterminer le vecteur de support dans la tâche de classification. Les vecteurs de support sont les points de données dans le jeu de données qui sont utilisés pour séparer les différentes catégories de variables cibles – ce sont des points de données très proches de la frontière de décision.

Dans l'image ci-dessous, les plans marginaux sont les lignes jaunes, tandis que l'hyperplan est la ligne rouge. L'hyperplan sert de ligne de meilleur ajustement ou de frontière de décision. Les points de données qui sont les plus proches du plan marginal sont les vecteurs de support – les points de données encerclés en vert dans l'image ci-dessous.

![Marge dure : Frontière de décision pour la classification de deux étiquettes Image par l'auteur](https://cdn.hashnode.com/res/hashnode/image/upload/v1735889303238/33e28db8-a0aa-4aa9-ac63-0ece6b2d8c15.png align="center")

Le plan marginal vise à atteindre une marge maximale entre son plan et l'hyperplan – tous deux ayant une distance égale par rapport à l'hyperplan pour atteindre la meilleure classification. L'hyperplan dans l'image ci-dessus montre une relation linéaire parfaite entre `feature x1` et `feature x2`. Les vecteurs de support aident également à établir l'emplacement du plan marginal.

Nous avons la marge dure et la marge souple, servant de méthodologies d'optimisation de modèle pour le SVM. La marge dure montre que vous ne pouvez pas trouver un point de données de `feature x1` dans la même zone où il y a des points de données `feature x2` et vice versa. Elle était utilisée pour décrire une classification parfaite par l'algorithme. L'image ci-dessus donne une représentation d'une marge dure.

Une marge souple montre que la classification est imparfaite, car vous pouvez trouver certains points de données de `feature x1` dans la même zone où nous avons des points de données de feature two, ce qui pourrait être causé par des valeurs aberrantes. L'image ci-dessous donne une représentation de marge souple.

![Marge souple : Frontière de décision pour la classification de deux étiquettes Image par l'auteur](https://cdn.hashnode.com/res/hashnode/image/upload/v1735888972196/3e9dfaa1-999e-4e55-b1eb-bc04ef8de24e.png align="center")

## Fonction objectif du SVM

Pour une classification binaire, comme un chien ou un chat, le chien peut être représenté comme la classe 1 et le chat comme -1. Cela montre que la frontière de décision ou l'hyperplan est le facteur déterminant. Toute valeur au-dessus du plan est donnée comme 1, et la classe en dessous du plan est donnée comme -1.

La fonction mathématique pour l'hyperplan est donnée comme suit :

$$f(x) = \mathbf{w}^T\mathbf{x} + b$$

$$\begin{array}{l} \text{ Les variables utilisées sont :} \\ \mathbf{w}: \text{Vecteur de poids (définissant l'orientation de l'hyperplan)} \\ b: \text{Terme de biais (définissant la position de l'hyperplan)} \\ \mathbf{x}: \text{Vecteur de caractéristiques d'entrée} \\ \\ \text{La décision de classification est basée sur le signe de } f(x)\text{ :} \\ f(x) > 0: \text{Classe 1} \\ f(x) < 0: \text{Classe -1} \end{array}$$

### SVM à marge dure

Le SVM à marge dure garantit que tous les points de données sont correctement classés sans erreur, en s'assurant que les points de données ne se retrouvent pas dans l'autre partie de l'hyperplan, et en maximisant également la marge. C'est une méthode efficace pour un ensemble de données "sans bruit". Cela est réalisé en minimisant une fonction objectif donnée ci-dessous :

$$\begin{array}{l} \text{Fonction objectif du SVM à marge dure :} \ \min_{\mathbf{w},b} \frac{1}{2}\|\mathbf{w}\|^2 \\ \\ \text{Sous réserve de :} \\ y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1, \,\, \forall i \\ \\ \text{Où :} \\ y_i: \text{ Étiquette de classe du }i\text{-ème échantillon } (+1 \text{ ou } -1) \\ \mathbf{x}_i: \text{ Vecteur de caractéristiques du }i\text{-ème échantillon} \end{array}$$

Cette contrainte donnée ci-dessus dans la fonction objectif garantit que tous les points de données ne sont pas mal classés et restent à l'extérieur de la marge.

### SVM à marge souple

Le SVM à marge souple est indulgent, car il permet certaines erreurs de classification. Il est adapté aux ensembles de données du monde réel, qui sont bruyants, et il gère les données non linéairement séparables. Il introduit une variable de relâchement qui pénalise les prédictions incorrectes.

$$\begin{array}{l} \text{Fonction objectif :} \ \min_{\mathbf{w},b,\xi} \frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{i=1}^n \xi_i \\ \\ \text{Sous réserve de :} \\ y_i(\mathbf{w}^T\mathbf{x}_i + b) \geq 1 - \xi_i, \,\, \forall i \\ \xi_i \geq 0, \,\, \forall i \\ \\ \text{Où :} \\ \xi_i: \text{ Variables de relâchement représentant le degré de mauvaise classification ou} \\ \text{violation de marge.} \\ C: \text{ Paramètre de régularisation contrôlant le compromis entre} \\ \text{maximisation de la marge et minimisation de l'erreur.} \end{array}$$

L'hyperparamètre C aide à contrôler la pénalité pour un équilibre entre la maximisation de la marge et la minimisation de l'erreur. Une grande valeur de C minimise les erreurs de classification, mais provoque une marge plus petite. Une petite valeur de C permet certaines erreurs de classification mais provoque une marge plus grande.

### Problèmes de classification non linéaire

Les problèmes de classification non linéaire incluent des ensembles de données avec des motifs non linéaires qui sont difficiles à capturer pour les modèles SVM linéaires. C'est un inconvénient, mais les noyaux SVM peuvent aider.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734969794598/58fcb341-735f-4a57-943b-c748b7a3f85c.png align="center")

La classification non linéaire contient des ensembles de données avec des relations compliquées et les modèles linéaires comme la régression linéaire ne pourront pas générer des prédictions précises ou identifier des tendances.

## Comprendre les fonctions noyau

Dans les fonctions noyau, nous transformons l'ensemble de données utilisé dans la tâche de classification en un espace de caractéristiques de dimension supérieure. Cette ligne d'action permet à l'hyperplan (une frontière de décision linéaire) de diviser les données en données linéairement séparables.

Par exemple, si un ensemble de données contient trois caractéristiques dans un plan 2D, la fonction noyau convertit les données en un plan 3D, ce qui rend beaucoup plus simple la partition de l'ensemble de données en utilisant un hyperplan de base. Cette technique peut être utilisée pour capturer des relations non linéaires dans les données.

Pour fournir une image mentale plus claire, considérons trois ensembles de caractéristiques distincts dans le plan 2D (x et y). Cela peut être pris dans un plan 3D par la machine à noyau, où `features x1` et `feature x2` peuvent être dans le plan x-y, qui est facilement divisé par un hyperplan simple, et `feature x3` peut être dans le plan y-z, qui est déjà séparé.

### L'astuce du noyau expliquée

La transformation en un espace de dimension supérieure est intensivement computationnelle et n'est pas la meilleure option. Mais nous connaissons l'importance des fonctions noyau dans la classification des données non linéaires. Alors, quelle est la voie à suivre pour atteindre le même exploit tout en contournant le coût de calcul ? C'est ce qu'on appelle l'astuce du noyau. L'astuce du noyau explique le "pouvoir magique" des fonctions noyau.

L'astuce du noyau est le calcul du produit interne ou produit scalaire entre les points de données dans l'espace dimensionnel original au lieu de transformer les données en un espace de dimension supérieure avant d'effectuer le calcul.

Le côté droit de l'équation ci-dessous montre le produit scalaire de ϕ(x), représentant le vecteur transformé en un espace de dimension supérieure (ce qui n'est pas efficace). C'est la même chose qu'une fonction noyau du côté gauche :

$$K(x_i, x_j) = \phi(x_i) \cdot \phi(x_j)$$

Le but de l'astuce du noyau est d'effectuer le calcul basé sur le point de données dans son espace dimensionnel original, au lieu d'effectuer des calculs sur des données complexes qui pourraient nécessiter un nombre infini de dimensions.

### Implémentation mathématique de l'astuce du noyau

Supposons que nous avons deux classes de données qui sont non linéaires dans l'espace 2D représentant l'espace de caractéristiques original. Aucune ligne droite ne peut séparer ces points car ils sont disposés diagonalement à travers l'origine.

$$\begin{array}{l} \textbf{Mapping Without Kernel Trick: }\\ \\ \begin{align*} \textbf{The 2D data is given as: } \\ & \mathbf{x}_1 = (1,1), & y_1 = +1 \\ & \mathbf{x}_2 = (-1,-1), & y_2 = -1 \end{align*} \\ \\ \textbf{Let's use a mapping function: } \\ \\ \phi(x, y) = (x^2, \sqrt{2}xy, y^2)\ \\ \\ Mapping\ \mathbf{x}_1 \ and \ \ \mathbf{x}_2: \\ \\ \begin{array}{l} - \ \phi(\mathbf{x}_1) = (1^2, \sqrt{2}(1)(1), 1^2) = (1, \sqrt{2}, 1) \\ \\ -\ \phi(\mathbf{x}_2) = ((-1)^2, \sqrt{2}(-1)(-1), (-1)^2) = (1, \sqrt{2}, 1) \end{array} \\ \\ \\ \textbf{Dot Product in Higher-Dimensional Space:} \\ \\ \phi(\mathbf{x}_1) \cdot \phi(\mathbf{x}_2) = (1)(1) + (\sqrt{2})(\sqrt{2}) + (1)(1) = 1 + 2 + 1 = 4 \\ \\ \\ \begin{array}{l} \text{This is the dot product of }\mathbf{x}_1\text{ and }\mathbf{x}_2\text{ after explicitly} \\ \text{mapping them to the higher-dimensional space.} \end{array} \end{array}$$

$$\begin{array}{l} \textbf{Using the Kernel Trick: }\\ \\ \textbf{Polynomial Kernel Definition:} \\ \\ K(\mathbf{x}_i, \mathbf{x}_j) = (\mathbf{x}_i^\top \mathbf{x}_j + c)^d \\ \\ \textbf{For this example:} \\ \\ d = 2 \ (\text{degree of the polynomial}), \quad c = 0 \ (\text{no bias term}) \\ \\ \textbf{Given: } \\ \\ \mathbf{x}_1 = (1, -1), \quad \mathbf{x}_2 = (-1, -1) \\ \\ \textbf{Compute } K(\mathbf{x}_1, \mathbf{x}_2): \\ \\ \begin{align*} K(\mathbf{x}_1, \mathbf{x}_2) &= ((1)(-1) + (1)(-1))^2 \\ &= (-1 - 1)^2 \\ &= (-2)^2 \\ &= 4 \end{align*} \\ \\ \begin{array}{l} \text{Using the kernel trick, we directly compute the dot product in the higher} \\ \text{dimensional space without explicitly mapping the points.} \end{array} \end{array}$$

## Fonctions noyau populaires

### Noyau linéaire

Pour un ensemble de données qui est linéairement séparable, le noyau linéaire est idéal. Lorsqu'il est utilisé pour des ensembles de données non linéaires, qui sont le sujet principal de cet article, il peut entraîner un sous-ajustement et créer une frontière de décision linéaire. Il est fourni comme le produit scalaire des vecteurs de caractéristiques d'entrée.

Ce noyau construit simplement l'hyperplan ou la ligne de meilleur ajustement pour diviser les points de données. Il ne effectue aucune transformation particulière vers une dimension supérieure.

$$Linear Kernel Function: K(x_i, x_j) = x_i \cdot x_j$$

### Noyau polynomial

Le noyau polynomial transforme les données en un espace de caractéristiques polynomial d'ordre d. Il effectue un produit scalaire sur le vecteur de caractéristiques avec une constante c, le tout dans le degré d. Plus le degré du polynôme est élevé, mieux le noyau capture les relations dans l'ensemble de données non linéaire.

$$Polynomial Kernel Function: K(x_i, x_j) = (x_i \cdot x_j + c)^d$$

### Noyau gaussien ou fonction de base radiale (RBF)

Le noyau gaussien, également connu sous le nom de noyau RBF, est souvent utilisé dans le SVM pour mapper le vecteur de caractéristiques d'entrée vers un espace de caractéristiques de dimension infinie en utilisant une fonction gaussienne. Ce noyau peut gérer des relations plus complexes.

$$RBF Kernel Function: K(x_i, x_j) = \exp(-\gamma \|x_i - x_j\|^2)$$

### Noyau sigmoïde

Le noyau sigmoïde agit de manière similaire à la fonction d'activation dans les réseaux de neurones. Il fonctionne de manière similaire à un réseau de perception à deux couches et peut mapper les données dans un espace de caractéristiques de dimension supérieure.

$$Sigmoid Kernel Function: K(x_i, x_j) = \tanh(\alpha(x_i \cdot x_j) + c)$$

Il existe d'autres fonctions noyau telles que les noyaux laplaciens, les noyaux hyperboliques, les noyaux exponentiels et les noyaux personnalisés que vous pouvez explorer si vous êtes curieux.

## Comment choisir le bon noyau

Les différentes fonctions noyau sont appliquées en fonction des relations linéaires et non linéaires dans l'espace de caractéristiques. Le noyau linéaire est simple et rapide, et il fonctionne bien avec les données linéairement séparables mais pas avec les données de haute dimension.

Le noyau polynomial est bien adapté pour les données avec des relations non linéaires ou polynomiales, ainsi que pour les données de faible dimension. Le noyau RBF est idéal pour les données denses dont vous n'avez aucune connaissance préalable. Enfin, le noyau sigmoïde fonctionne bien pour les points de données binaires et catégoriques.

## Implémentation du noyau SVM

Passons maintenant à un exemple montrant comment vous pouvez utiliser cette technique.

### **Étape 1 : Importer les bibliothèques nécessaires**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
```

### **Étape 2 : Générer l'ensemble de données non linéaire**

L'ensemble de données non linéaire utilisé dans cet article est un ensemble de données circulaire de `sklearn.datasets`. Nous avons utilisé 1500 échantillons avec un `random_state` de 46 pour garder l'ensemble de données cohérent pour la reproductibilité. Nous avons ajouté un bruit gaussien aux données de 10 %. Cette fonction `generate_circle_data` est implémentée pour générer l'ensemble de données utilisé dans l'article.

```python
def generate_circle_data(n_samples=1500, noise=0.10, random_state=46):
    """
    Générer deux ensembles de données de cercles concentriques.
    
    Paramètres :
    -----------
    n_samples : int
        Le nombre total de points générés
    noise : float
        Écart-type du bruit gaussien ajouté aux données
    random_state : int
        Graine aléatoire pour la reproductibilité
        
    Retourne :
    --------
    X : tableau de forme [n_samples, 2]
        Les échantillons générés
    y : tableau de forme [n_samples]
        Les étiquettes entières (0 ou 1) pour l'appartenance à chaque classe
    """
    return make_circles(n_samples=n_samples, 
                       noise=noise, 
                       random_state=random_state)
```

### **Étape 3 : Tracer les données 2D**

Les données générées ci-dessus se présentent sous forme 2D. Chaque couleur représente les deux différents échantillons de données. Les points de données ont été tracés, ce qui nous permet de les voir comme un ensemble de données circulaire en utilisant la bibliothèque `Matplotlib`.

```python
def plot_2d_data(X, y, title="2D Circle Dataset"):
    """
    Tracer l'ensemble de données 2D avec des couleurs différentes pour chaque classe.
    
    Paramètres :
    -----------
    X : tableau de forme (n_samples, 2)
        Les échantillons d'entrée
    y : tableau de forme (n_samples,)
        Les valeurs cibles (étiquettes de classe)
    title : str
        Le titre du graphique
    """
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, marker='.', cmap='viridis')
    plt.title(title)
    plt.xlabel('X₁')
    plt.ylabel('X₂')
    plt.colorbar(label='Classe')
    plt.grid(True, alpha=0.3)
    plt.show()
```

L'image de sortie de l'ensemble de données est donnée ci-dessous :

![Output of circular dataset](https://cdn.hashnode.com/res/hashnode/image/upload/v1734978596496/a529c7e6-13ce-427e-b462-1241ea6de1bf.png align="center")

### **Étape 4 : Transformer en un espace de dimension supérieure**

Les données en 2D sont transformées en un espace 3D en utilisant le noyau polynomial. Nous avons réalisé cela en créant une troisième caractéristique X3 afin qu'elle puisse être mappée dans un espace de dimension supérieure pour une séparation facile.

```python
def transform_to_3d(X):
    """Transformer les données 2D en 3D en utilisant une transformation basée sur le rayon"""
    X1 = X[:, 0].reshape(-1, 1)
    X2 = X[:, 1].reshape(-1, 1)
    # Transformation modifiée pour créer une meilleure séparation
    X3 = X1**2 + X2**2
    return np.hstack((X1, X2, X3))
```

### Étape 5 : Tracer la transformation 3D

L'étape suivante consiste à tracer l'ensemble de données transformé en 3D. Il ressemble maintenant à un bol en forme de U, et est séparé avec un hyperplan après avoir ajusté un modèle `LinearSVC` de la bibliothèque `sklearn` comme le noyau que nous utilisons. Cela montre un exemple pratique des concepts que vous avez appris jusqu'à présent :

```python
def plot_3d_transformation_with_separator(X_transformed, y, title="3D Transformed Dataset with Linear Separator"):
    """Tracer l'ensemble de données transformé en 3D avec un plan de séparation linéaire clair"""
    
    # Mettre à l'échelle les caractéristiques transformées
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_transformed)
    
    # Ajuster le SVM linéaire avec des paramètres ajustés pour une meilleure séparation
    svm = LinearSVC(C=1.0, dual="auto", max_iter=5000)
    svm.fit(X_scaled, y)
    
    # Créer le graphique 3D
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Tracer les deux classes avec des couleurs et des marqueurs différents pour plus de clarté
    class_0 = y == 0
    class_1 = y == 1
    
    ax.scatter(X_transformed[class_0, 0], 
              X_transformed[class_0, 1], 
              X_transformed[class_0, 2],
              c='blue', 
              marker='o',
              label='Classe 0',
              alpha=0.6)
    
    ax.scatter(X_transformed[class_1, 0], 
              X_transformed[class_1, 1], 
              X_transformed[class_1, 2],
              c='red', 
              marker='^',
              label='Classe 1',
              alpha=0.6)
    
    # Créer une grille pour le plan séparateur
    x_min, x_max = X_transformed[:, 0].min() - 0.2, X_transformed[:, 0].max() + 0.2
    y_min, y_max = X_transformed[:, 1].min() - 0.2, X_transformed[:, 1].max() + 0.2
    
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 50),
                        np.linspace(y_min, y_max, 50))
    
    # Obtenir les coefficients du plan séparateur
    w = svm.coef_[0]
    b = svm.intercept_[0]
    
    # Calculer les coordonnées z du plan
    grid_points = np.c_[xx.ravel(), yy.ravel(), np.zeros(xx.ravel().shape[0])]
    scaled_grid = scaler.transform(grid_points)
    
    # Calculer le plan séparateur
    z = (-w[0] * scaled_grid[:, 0] - w[1] * scaled_grid[:, 1] - b) / w[2]
    z = z.reshape(xx.shape)
    z = scaler.inverse_transform(np.c_[xx.ravel(), yy.ravel(), z.ravel()])[:, 2].reshape(xx.shape)
    
    # Tracer le plan séparateur avec une transparence ajustée
    surface = ax.plot_surface(xx, yy, z, alpha=0.3, cmap='coolwarm')
    
    # Personnaliser le graphique
    ax.set_xlabel('X₁')
    ax.set_ylabel('X₂')
    ax.set_zlabel('X₁² + X₂²')
    ax.set_title(title)
    
    # Ajouter une légende
    ax.legend()
    
    # Ajuster l'angle de vue pour une meilleure visualisation
    ax.view_init(elev=20, azim=45)
    
    # Ajouter une description textuelle
    ax.text2D(0.05, 0.95, 
              "Transformation du noyau polynomial :\nΦ(x₁,x₂) → (x₁,x₂,x₁²+x₂²)\n\nLes classes sont linéairement séparables\ndans l'espace transformé", 
              transform=ax.transAxes, 
              bbox=dict(facecolor='white', alpha=0.8))
    
    plt.show()

def main():
    # Générer et tracer l'ensemble de données
    X, y = generate_circle_data()
    
    # Transformer et tracer les données 3D avec un séparateur clair
    X_transformed = transform_to_3d(X)
    plot_3d_transformation_with_separator(X_transformed, y)

if __name__ == "__main__":
    main()
```

La fonction `main` est une fonction de fonctions qui rassemble toutes les autres fonctions telles que `generate_circle_data`, `transform_to_3d` et `plot_3d_transformation_with_separator` pour établir le modèle. L'image ci-dessous montre une meilleure séparation avec l'aide du noyau polynomial.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1734979669969/2e0af04a-93cc-44e8-8ed5-15a484385fd1.png align="center")

### Voici le code complet :

%[https://gist.github.com/Josiah-Adesola/f980d950df07000b6779e53641f13a4d] 

## Conclusion

Dans cet article, vous avez appris l'efficacité des noyaux SVM pour les applications de classification non linéaire. Les différentes fonctions ont démontré une efficacité computationnelle en transformant les données d'entrée en données de dimension supérieure, comme montré dans l'exemple, sans nécessiter de grandes quantités de stockage ou de traitement.

Le SVM peut être utilisé dans une variété de tâches de classification, y compris la classification d'images et de texte, et il s'est avéré extrêmement efficace.

### Références

1. Park, H., & Son, J.-H. (2021). Techniques de machine learning pour l'imagerie THz et la spectroscopie dans le domaine temporel. *Sensors, 21*(4), 1186. [https://doi.org/10.3390/s21041186](https://doi.org/10.3390/s21041186)
    
2. [Développeurs de Scikit-learn. (2024). Machines à vecteurs de support. Scikit-learn.https://scikit-learn.org/1.5/modules/svm.html](https://scikit-learn.org/1.5/modules/svm.html)