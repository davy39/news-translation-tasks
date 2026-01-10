---
title: Apprenez à construire un perceptron multicouche avec des exemples concrets
  et du code Python
subtitle: ''
author: Kuriko Iwai
co_authors: []
series: null
date: '2025-05-30T18:21:29.776Z'
originalURL: https://freecodecamp.org/news/build-a-multilayer-perceptron-with-examples-and-python-code
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1748616370600/01903917-4be7-476b-90d1-18295d19edef.png
tags:
- name: Deep Learning
  slug: deep-learning
- name: neural networks
  slug: neural-networks
- name: binary classification
  slug: binary-classification
- name: MLP (Multi-Layer Perceptrons)
  slug: mlp-multi-layer-perceptrons
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: MathJax
  slug: mathjax
seo_title: Apprenez à construire un perceptron multicouche avec des exemples concrets
  et du code Python
seo_desc: 'The perceptron is a fundamental concept in deep learning, with many algorithms
  stemming from its original design.

  In this tutorial, I’ll show you how to build both single layer and multi-layer perceptrons
  (MLPs) across three frameworks:


  Custom class...'
---

Le **perceptron** est un concept fondamental du deep learning, de nombreux algorithmes découlant de sa conception originale.

Dans ce tutoriel, je vais vous montrer comment construire des perceptrons à couche unique et des perceptrons multicouches (MLP) à travers trois Framework :

* Un classificateur personnalisé
    
* Le `MLPClassifier` de Scikit-learn
    
* Le classificateur Keras Sequential utilisant les optimiseurs SGD et Adam.
    

Cela vous aidera à découvrir leurs différents cas d'utilisation et leur fonctionnement.

### Table des matières

* [Qu'est-ce qu'un perceptron ?](#heading-quest-ce-quun-perceptron)
    
* [Comment construire un classificateur à couche unique](#heading-comment-construire-un-classificateur-a-couche-unique)
    
* [Qu'est-ce qu'un perceptron multicouche ?](#heading-quest-ce-quun-perceptron-multicouche)
    
* [Comment construire des perceptrons multicouches](#heading-comment-construire-des-perceptrons-multicouches)
    
* [Comprendre les optimiseurs](#heading-comprendre-les-optimiseurs)
    
* [Comment construire un classificateur MLP avec l'optimiseur SGD](#heading-comment-construire-un-classificateur-mlp-avec-loptimiseur-sgd)
    
* [Comment construire un classificateur MLP avec l'optimiseur Adam](#heading-comment-construire-un-classificateur-mlp-avec-loptimiseur-adam)
    
* [Résultats finaux : Généralisation](#heading-resultats-finaux-generalisation)
    
* [Conclusion](#heading-conclusion)
    

### Prérequis

* Mathématiques (Calcul, Algèbre linéaire, Statistiques)
    
* Programmation en Python
    
* Compréhension de base des concepts de Machine Learning
    

## Qu'est-ce qu'un perceptron ?

Un perceptron est l'un des types de neurones artificiels les plus simples utilisés en Machine Learning. C'est un bloc de construction des réseaux de neurones artificiels qui apprend à partir de données étiquetées pour effectuer des tâches de classification et de reconnaissance de formes, généralement sur des données linéairement séparables.

Un perceptron à couche unique se compose d'une seule couche de neurones artificiels, appelés perceptrons.

Mais lorsque vous connectez de nombreux perceptrons ensemble en couches, vous obtenez un perceptron multicouche (MLP). Cela permet au réseau d'apprendre des modèles plus complexes en combinant les décisions simples de chaque perceptron. Cela fait des MLP des outils puissants pour des tâches telles que la reconnaissance d'images et le traitement du langage naturel.

Le perceptron se compose de quatre parties principales :

* **Couche d'entrée** : Reçoit les valeurs numériques initiales dans le système pour un traitement ultérieur.
    
* **Poids** : Combine les valeurs d'entrée avec des poids (et des termes de biais).
    
* **Fonction d'activation** : Détermine si le neurone doit s'activer en fonction de la valeur de seuil.
    
* **Couche de sortie** : Produit le résultat de la classification.
    

![Image : Organisation d'un perceptron. Source : Rosenblatt 1958](https://cdn.hashnode.com/res/hashnode/image/upload/v1748438698612/5b2920db-4ec1-455b-840e-7b5e9d6c2e75.png align="center")

Il effectue une somme pondérée des entrées, ajoute un biais et passe le résultat par une fonction d'activation – tout comme la régression logistique. C'est un peu comme un petit décideur qui dit "oui" ou "non" en fonction des informations qu'il reçoit.

Ainsi, par exemple, lorsque nous utilisons une activation sigmoïde, sa sortie est une probabilité comprise entre 0 et 1, imitant le comportement de la régression logistique.

### Applications des perceptrons

Les perceptrons sont appliqués à des tâches telles que :

* **Classification d'images :** Les perceptrons classent les images contenant des objets spécifiques. Ils y parviennent en effectuant des tâches de classification binaire.
    
* **Régression linéaire :** Les perceptrons peuvent prédire des sorties continues basées sur des caractéristiques d'entrée. Cela les rend utiles pour résoudre des problèmes de régression linéaire.
    

### Comment fonctionne la fonction d'activation

Pour un perceptron unique utilisé pour la classification binaire, la fonction d'activation la plus courante est la **fonction de seuil** (également connue sous le nom de fonction step) :

$$\phi(z) = \begin{cases} 1 &\text{si } z \geq \theta \\ 0 &\text{si } z < \theta \end{cases}$$

où :

* `ϕ(z)` : la sortie de la fonction d'activation.
    
* `z` : la somme pondérée des entrées plus le biais :
    

$$z = \sum_{i=1}^m w_i x_i + b$$

(xi : valeurs d'entrée, w : poids associé à chaque entrée, b : termes de biais)

`θ` est le seuil. Souvent, le seuil θ est fixé à zéro, et le biais (b) contrôle efficacement le seuil d'activation.

Dans ce cas, la formule devient :

$$\phi(z) = \begin{cases} 1 &\text{si } z \geq 0 \\ 0 &\text{si } z < 0 \end{cases}$$

![Image : Fonction de seuil (Auteur)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748439460839/e74f1c1c-4e89-419b-aa9e-24a297d81ff5.png align="center")

Lorsque la fonction de seuil ϕ(z) renvoie un, cela signifie que l'entrée appartient à la classe étiquetée un.

Cela se produit **lorsque la somme pondérée est supérieure à zéro**, ce qui amène le perceptron à prédire que l'entrée est dans cette classe binaire.

Bien que la fonction de seuil soit conceptuellement l'activation originale d'un perceptron, sa discontinuité à zéro pose des défis informatiques.

Dans les implémentations modernes, nous pouvons utiliser d'autres fonctions d'activation comme la fonction **sigmoïde** :

$$\sigma (z) = \frac {1} {1 + e^{-z}}$$

La fonction sigmoïde produit également zéro ou un selon la somme pondérée (z).

### Comment fonctionne la fonction de perte

La **fonction de perte** (loss function) est un concept crucial en machine learning qui quantifie l'erreur ou l'écart entre les prédictions du modèle et les valeurs cibles réelles.

Son but est de pénaliser le modèle lorsqu'il fait des prédictions incorrectes ou inexactes, ce qui guide l'algorithme d'apprentissage (par exemple, la descente de gradient) pour ajuster les paramètres du modèle de manière à minimiser cette erreur et à améliorer les performances.

Dans une tâche de classification binaire, le modèle peut adopter la **fonction de perte charnière** (hinge loss) pour pénaliser les erreurs de classification en facturant un coût supplémentaire pour les prédictions incorrectes :

$$L(y, h(x)) = max(0, 1- y*h(x))$$

(h(x) : étiquette de prédiction, y : étiquette réelle)

## Comment construire un classificateur à couche unique

Maintenant, construisons un simple perceptron à couche unique pour la classification binaire.

### 1. Classificateur personnalisé

#### Initialiser le classificateur

Nous allons d'abord initialiser le classificateur avec les `poids`, le `biais`, le nombre d'époques (`n_iterations`) et le taux d'apprentissage (`learning_rate`).

```python
def __init__(self, learning_rate=0.01, n_iterations=1000):
    self.learning_rate = learning_rate
    self.n_iterations = n_iterations
    self.weights = None
    self.bias = None
```

#### Définir la fonction d'activation

Utilisez une fonction de seuil qui renvoie zéro si l'entrée (x) ≤ 0, sinon 1. Par défaut, le `threshold` (seuil) est fixé à zéro.

```python
def _step_function(self, x, threshold: int = 0):
     return np.where(x > threshold, 1, 0)
```

#### Entraîner le modèle

Il est maintenant temps de commencer l'entraînement. Le processus d'apprentissage consiste à mettre à jour de manière itérative les paramètres internes du perceptron : les `poids` et le `biais`.

Ce processus est contrôlé par un nombre spécifié d'époques d'entraînement défini par `n_iterations`.

À chaque époque, le modèle traite l'ensemble du jeu de données d'entrée (X) et ajuste ses poids et son biais en fonction de la différence entre ses prédictions et les étiquettes réelles (y), guidé par un `learning_rate` prédéfini.

```python
def fit(self, X, y):
    n_samples, n_features = X.shape

    self.weights = np.zeros(n_features)
    self.bias = 0

    for _ in range(self.n_iterations):
        for i in range(n_samples):
            # calculer la somme pondérée (z)
            z = np.dot(X[i], self.weights) + self.bias
            
            # appliquer la fonction d'activation
            y_pred = self._step_function(z)
            
            # mettre à jour les poids et le biais
            self.weights += self.learning_rate * (y[i] - y_pred) * X[i]
            self.bias += self.learning_rate * (y[i] - y_pred)
```

#### Comment fonctionnent les poids dans la boucle d'itération

Les poids dans un perceptron définissent l'orientation (la pente) de la frontière de décision qui sépare les classes.

Leur mise à jour itérative dans la boucle `for` vise à réduire les erreurs de classification de telle sorte que :

$$\begin {align*} w_j &:= w_j + \Delta w_j \\ & := w_j + \eta (y_i - \hat y_i)x_{ij} \\ &= \begin{cases} w_j &\text{(a) } y_i - \hat y_i = 0\\ w_j + \eta x_ij &\text{(b) } y_i - \hat y_i = 1 \\ w_j - \eta x_ij &\text{(c) } y_i - \hat y_i = -1 \\ \end{cases} \end{align*}$$

(`w_j` : j-ème poids, `η` : taux d'apprentissage, (`yi​−y^​i​`) : erreur)

Cela signifie que :

1. Lorsque la prédiction est **correcte**, l'erreur est nulle, donc le poids est inchangé.
    
2. Lorsque la prédiction est **trop basse** (yi​=1 et y^​i​=0), le poids est ajusté dans la même direction pour augmenter la somme pondérée.
    
3. Lorsque la prédiction est **trop haute** (yi​=0 et y^​i​=1), le poids est ajusté dans la direction opposée pour abaisser la somme pondérée.
    

#### Comment fonctionnent les termes de biais dans la boucle d'itération

Le biais détermine l'ordonnée à l'origine (position par rapport à l'origine) de la frontière de décision.

Tout comme pour les poids, nous ajustons les termes de biais à chaque époque pour positionner la frontière de décision :

$$\begin {align*} b &:= b + \Delta b \\ & := b + \eta (y_i - \hat y_i) \\ &= \begin{cases} b &\text{(a) } y_i - \hat y_i = 0\\ b + \eta &\text{(b) } y_i - \hat y_i = 1 \\ b - \eta &\text{(c) } y_i - \hat y_i = -1 \\ \end{cases} \end{align*}$$

Cet ajustement répété vise à optimiser la capacité du modèle à classer correctement les données d'entraînement.

#### Faire une prédiction

Enfin, nous ajoutons une fonction pour générer une valeur de résultat (zéro ou un) pour de nouvelles données non vues (X) :

```python
def predict(self, X):
      linear_output = np.dot(X, self.weights) + self.bias
      predictions = self._step_function(linear_output)
      return predictions
```

**Le classificateur complet ressemble à ceci :**

```python
import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None

    def _step_function(self, x, threshold: int = 0):
        return np.where(x > threshold, 1, 0)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.n_iterations):
            for i in range(n_samples):
                linear_output = np.dot(X[i], self.weights) + self.bias
                y_pred = self._step_function(linear_output)
                self.weights += self.learning_rate * (y[i] - y_pred) * X[i]
                self.bias += self.learning_rate * (y[i] - y_pred)
        return self

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_pred = self._step_function(linear_output)
        return y_pred
```

#### Simuler avec des jeux de données synthétiques

Tout d'abord, nous avons généré un jeu de données synthétique linéairement séparable à l'aide de `make_blob` et calculé une frontière de décision, puis entraîné le classificateur que nous avons créé.

```python
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
import numpy as np

# créer un jeu de données factice
X, y = make_blobs(n_features=2, centers=2, n_samples=1000, random_state=12)

# division des données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# entraîner le modèle
perceptron = Perceptron(learning_rate=0.1, n_iterations=1000).fit(X_train, y_train)

# faire une prédiction
y_pred_train = perceptron.predict(X_train)
y_pred_test = perceptron.predict(X_test)

# évaluer les résultats
acc_train = np.mean(y_pred_train == y_train)
acc_test = np.mean(y_pred_test == y_test)
print(f"Accuracy (Train): {acc_train:.3} \
Accuracy (Test): {acc_test:.3}")
```

#### Résultats

Le classificateur a généré une frontière de décision linéaire claire et très précise.

* *Accuracy (Train): 0.981*
    
* *Accuracy (Test): 0.975*
    

![Frontière de décision d'un perceptron à couche unique (Classificateur personnalisé)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748440470195/0a01c5ad-124e-4f59-b4d5-9ee5dd5b23ce.png align="center")

### 2. Tirer parti du classificateur MLP de Scikit-learn

Pour notre commodité, nous utiliserons le classificateur intégré de scikit-learn (`MLPClassifier`) pour construire un classificateur similaire, mais plus robuste :

```python
model = MLPClassifier(
    hidden_layer_sizes=(), # intentionnellement vide pour créer un perceptron à couche unique
    activation='logistic', # choix d'une fonction sigmoïde comme fonction d'activation
    solver='sgd', # choix de l'optimiseur SGD
    max_iter=1000,
    random_state=42, 
    learning_rate='constant', 
    learning_rate_init=0.1
).fit(X_train, y_train)

y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

acc_train = np.mean(y_pred_train == y_train)
acc_test = np.mean(y_pred_test == y_test)
print(f"MLPClassifier\
Accuracy (Train): {acc_train:.3} \
Accuracy (Test): {acc_test:.3}")
```

#### Résultats

Le `MLPClassifier` a généré une frontière de décision linéaire claire avec des scores de précision légèrement meilleurs.

* *Accuracy (Train): 0.985*
    
* *Accuracy (Test): 0.995*
    

![Frontière de décision d'un perceptron à couche unique (MLPClassifier)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748440118956/f5391f47-711a-4948-b956-1a76dbd7ca92.png align="center")

### Limites des perceptrons à couche unique

Parlons maintenant des différences clés entre le `MLPClassifier` et notre perceptron à couche unique personnalisé.

Contrairement aux réseaux de neurones plus généraux, les perceptrons à couche unique utilisent une **fonction de seuil** comme activation.

En raison de sa discontinuité en x=0, la fonction de seuil n'est pas dérivable sur l'ensemble de son domaine (−∞ à ∞).

Cette propriété fondamentale empêche l'utilisation d'**algorithmes d'optimisation basés sur le gradient** tels que SGD ou Adam, car ces méthodes dépendent du calcul de gradients et de dérivées partielles pour la fonction de coût.

En revanche, la plupart des réseaux de neurones emploient des fonctions d'activation dérivables (par exemple, **sigmoïde**, **ReLU**) et des fonctions de perte (par exemple, **MSE**, **Entropie croisée**) pour une optimisation efficace.

D'autres défis du perceptron à couche unique incluent :

* **Limité à la séparabilité linéaire :** Parce qu'ils ne peuvent apprendre que des frontières de décision linéaires, ils sont incapables de gérer des données complexes non linéairement séparables.
    
* **Manque de profondeur :** Étant à couche unique, ils ne peuvent pas apprendre de représentations hiérarchiques complexes.
    
* **Options d'optimiseur limitées :** Comme mentionné, leur fonction d'activation non dérivable empêche l'utilisation des principaux optimiseurs basés sur le gradient.
    

Ainsi, dans la section suivante, vous découvrirez les perceptrons multicouches pour surmonter ces inconvénients.

## Qu'est-ce qu'un perceptron multicouche ?

Un MLP est une classe de réseau de neurones artificiels à propagation avant (feedforward) qui se compose d'au moins **trois couches** de nœuds :

* une couche d'entrée,
    
* une ou plusieurs couches cachées, et
    
* une couche de sortie.
    

À l'exception des nœuds d'entrée, chaque nœud est un neurone qui utilise une fonction d'activation **non linéaire**.

Les MLP sont largement utilisés pour les problèmes de classification ainsi que pour la régression :

* **Tâches de classification :** Les MLP sont largement utilisés pour les problèmes de classification, tels que la reconnaissance de l'écriture manuscrite et la reconnaissance vocale.
    
* **Analyse de régression :** Ils sont également appliqués dans les problèmes de régression où la relation entre l'entrée et la sortie est complexe.
    

## Comment construire des perceptrons multicouches

Abordons une tâche de classification binaire en utilisant une architecture MLP standard.

### Aperçu du projet

#### Objectif

* Détecter les transactions frauduleuses
    

#### Métriques d'évaluation

* Compte tenu du coût d'une mauvaise classification, nous donnerons la priorité à l'amélioration des scores de **Rappel (Recall)** et de **Précision**.
    
* Ensuite, nous vérifierons la précision de la classification avec le score d'**Exactitude (Accuracy)** (TP + TN / (TP + TN + FP + FN ))
    

**Coût d'une mauvaise classification (du plus élevé au plus bas) :**

* **Faux Négatif (FN) :** Le modèle identifie incorrectement une transaction frauduleuse comme légitime (Fraude réelle manquée)
    
* **Faux Positif (FP) :** Le modèle identifie incorrectement une transaction légitime comme frauduleuse (Blocage de clients légitimes.)
    
* **Vrai Positif (TP) :** Le modèle identifie correctement une transaction frauduleuse comme fraude.
    
* **Vrai Négatif (TN) :** Le modèle identifie correctement une transaction non frauduleuse comme non-fraude.
    

### Planification d'une architecture MLP

Dans le réseau, 19 caractéristiques d'entrée alimentent les 30 neurones de la première couche cachée, qui utilisent une fonction d'activation ReLU.

Ensuite, leurs sorties sont transmises à la deuxième couche, aboutissant à des valeurs sigmoïdes comme sortie finale.

Au cours du processus d'optimisation, nous laisserons l'optimiseur (SGD et Adam) effectuer des passes avant et arrière pour ajuster les paramètres.

![Architecture MLP standard pour les tâches de classification binaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1748440761512/37753a4c-f7f8-44bc-bea9-c50360830456.png align="center")

Image : Architecture MLP standard pour les tâches de classification binaire (Créée par Kuriko Iwai en utilisant cette [source d'image](https://www.researchgate.net/publication/355148120_SS-MLP_A_Novel_Spectral-Spatial_MLP_Architecture_for_Hyperspectral_Image_Classification))

Surtout dans les réseaux plus profonds, la fonction **ReLU** est avantageuse pour prévenir les [problèmes de gradient évanescent](https://en.wikipedia.org/wiki/Vanishing_gradient_problem#:~:text=In%20machine%20learning%2C%20the%20vanishing,derivative%20of%20the%20loss%20function) où les gradients deviennent extrêmement petits lorsqu'ils sont rétropropagués depuis les couches de sortie.

![Comparaison des principales fonctions d'activation : De gauche à droite : Sigmoïde, Tanh, ReLU](https://cdn.hashnode.com/res/hashnode/image/upload/v1748440797954/ba19bf66-cdb9-4bfb-9b92-e1e3f72e9fc7.png align="center")

[En savoir plus : Guide complet sur les réseaux de neurones en Deep Learning](https://medium.com/data-science-collective/a-comprehensive-guide-on-neural-network-in-deep-learning-442ba9f1f0e5)

### Prétraitement des jeux de données

Tout d'abord, nous consolidons [trois jeux de données – transaction, client et carte de crédit](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets) – en un seul DataFrame, en nettoyant indépendamment les données numériques et catégorielles :

```python
import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# télécharger les données brutes en local
import kagglehub
path = kagglehub.dataset_download("computingvictor/transactions-fraud-datasets")
dir = f'{path}/gd_card_flaud_demo'

def sanitize_df(amount_str):
    """Supprime le '$' et convertit la chaîne en float."""
    if isinstance(amount_str, str):
        return float(amount_str.replace('$', ''))
    return amount_str

# charger les données de transaction
trx_df = pd.read_csv(f'{dir}/transactions_data.csv')

# nettoyer le jeu de données (supprimer les colonnes inutiles et les transactions erronées, convertir les types string en int/float)
trx_df = trx_df[trx_df['errors'].isna()]
trx_df = trx_df.drop(columns=['merchant_city','merchant_state', 'date', 'mcc', 'errors'], axis='columns')
trx_df['amount'] = trx_df['amount'].apply(sanitize_df)

# fusionner le dataframe avec l'indicateur de transaction frauduleuse.
with open(f'{dir}/train_fraud_labels.json', 'r') as fp:
    fraud_labels_json = json.load(fp=fp)

fraud_labels_dict = fraud_labels_json.get('target', {})
fraud_labels_series = pd.Series(fraud_labels_dict, name='is_fraud')
fraud_labels_series.index = fraud_labels_series.index.astype(int) # convertir le type de données de string à integer
merged_df = pd.merge(trx_df, fraud_labels_series, left_on='id', right_index=True, how='left')
merged_df.fillna({'is_fraud': 'No'}, inplace=True)
merged_df['is_fraud'] = merged_df['is_fraud'].map({'Yes': 1, 'No': 0})

# charger les données de carte
card_df = pd.read_csv(f'{dir}/cards_data.csv')
card_df = card_df.drop(columns=['client_id', 'acct_open_date', 'card_number', 'expires', 'cvv'], axis='columns')
card_df['credit_limit'] = card_df['credit_limit'].apply(sanitize_df)

# fusionner les données de transaction et de carte
merged_df = pd.merge(left=merged_df, right=card_df, left_on='card_id', right_on='id', how='inner')
merged_df = merged_df.drop(columns=['id_y', 'card_id'], axis='columns')

# convertit les variables catégorielles en une nouvelle colonne binaire (0 ou 1)
categorical_cols = merged_df.select_dtypes(include=['object']).columns
df = merged_df.copy()
df = pd.get_dummies(df, columns=categorical_cols, dummy_na=False, dtype=float) 
df = df.dropna().drop(['client_id', 'id_x'], axis=1)
print('\
DataFrame: \
', df.head(n=3))
```

DataFrame :

![Base DataFrame](https://cdn.hashnode.com/res/hashnode/image/upload/v1748440856826/ba79bdaf-e0a1-457f-ab19-fda3e0f08141.png align="center")

Notre DataFrame montre une **distribution de données extrêmement asymétrique** avec :

* Échantillons de fraude : 1 191
    
* Échantillons sans fraude : 11 477 397
    

Pour les tâches de classification, **il est crucial d'être conscient des déséquilibres de taille d'échantillon et d'employer des stratégies appropriées pour atténuer leur impact négatif** sur les performances du modèle de classification, en particulier en ce qui concerne la classe minoritaire.

Pour nos données, nous allons :

1. diviser les 1 191 échantillons de fraude en ensembles d'entraînement, de validation et de test,
    
2. ajouter un nombre égal d'échantillons sans fraude choisis au hasard dans le DataFrame, et
    
3. ajuster les équilibres de division plus tard si des défis de généralisation apparaissent.
    

```python
# définir la taille souhaitée des échantillons de fraude pour les ensembles de validation et de test
val_size_per_class = 200
test_size_per_class = 200

# créer les ensembles de test
X_test_fraud = df_fraud.sample(n=test_size_per_class, random_state=42)
X_test_non_fraud = df_non_fraud.sample(n=test_size_per_class, random_state=42)

# combiner pour former l'ensemble de test équilibré
X_test = pd.concat([X_test_fraud, X_test_non_fraud]).sample(frac=1, random_state=42).reset_index(drop=True)
y_test = X_test['is_fraud']
X_test = X_test.drop('is_fraud', axis=1)

# supprimer les lignes échantillonnées des dataframes originaux pour éviter les fuites de données
df_fraud_remaining = df_fraud.drop(X_test_fraud.index)
df_non_fraud_remaining = df_non_fraud.drop(X_test_non_fraud.index)


# créer les ensembles de validation
X_val_fraud = df_fraud_remaining.sample(n=val_size_per_class, random_state=42)
X_val_non_fraud = df_non_fraud_remaining.sample(n=val_size_per_class, random_state=42)

# combiner pour former l'ensemble de validation équilibré
X_val = pd.concat([X_val_fraud, X_val_non_fraud]).sample(frac=1, random_state=42).reset_index(drop=True)
y_val = X_val['is_fraud']
X_val = X_val.drop('is_fraud', axis=1)

# supprimer les lignes échantillonnées des dataframes restants
df_fraud_train = df_fraud_remaining.drop(X_val_fraud.index)
df_non_fraud_train = df_non_fraud_remaining.drop(X_val_non_fraud.index)


# créer les ensembles d'entraînement
min_train_samples_per_class = min(len(df_fraud_train), len(df_non_fraud_train))

X_train_fraud = df_fraud_train.sample(n=min_train_samples_per_class, random_state=42)
X_train_non_fraud = df_non_fraud_train.sample(n=min_train_samples_per_class, random_state=42)

X_train = pd.concat([X_train_fraud, X_train_non_fraud]).sample(frac=1, random_state=42).reset_index(drop=True)
y_train = X_train['is_fraud']
X_train = X_train.drop('is_fraud', axis=1)


print("\
--- Final Dataset Shapes and Distributions ---")
print(f"X_train shape: {X_train.shape}, y_train distribution: {np.unique(y_train, return_counts=True)}")
print(f"X_val shape: {X_val.shape}, y_val distribution: {np.unique(y_val, return_counts=True)}")
print(f"X_test shape: {X_test.shape}, y_test distribution: {np.unique(y_test, return_counts=True)}")
```

Après l'opération, nous avons obtenu 1 582 échantillons d'entraînement, 400 de validation et 400 de test, chaque jeu de données conservant une **répartition 50:50 entre les transactions frauduleuses et non frauduleuses** :

![X, y datasets shape](https://cdn-images-1.medium.com/max/1440/1*IZtK3l0hSqmkOrm9h_d9Jw.png align="left")

Compte tenu de l'espace de caractéristiques de haute dimension avec 19 caractéristiques d'entrée, nous allons appliquer **SMOTE** pour rééchantillonner les données d'entraînement (SMOTE ne doit pas être appliqué aux ensembles de validation ou de test pour éviter les fuites de données) :

```python
from imblearn.over_sampling import SMOTE
from collections import Counter

train_target = 2000

smote_train = SMOTE(
  sampling_strategy={0: train_target, 1: train_target},  # augmenter la taille de l'échantillon à 2 000
  random_state=12
)
X_train, y_train = smote_train.fit_resample(X_train, y_train)

print(f"\
Après SMOTE avec sampling_strategy personnalisée (cible train : {train_target}) :")
print(f"X_train_oversampled shape: {X_train.shape}")
print(f"y_train_oversampled distribution: {Counter(y_train)}")
```

Nous avons obtenu 4 000 échantillons d'entraînement, en maintenant une répartition 50:50 entre les transactions frauduleuses et non frauduleuses :

![Forme de l'échantillon d'entraînement après SMOTE](https://cdn.hashnode.com/res/hashnode/image/upload/v1748440986995/ed079321-3972-4226-b1a8-244010445162.png align="center")

Enfin, nous appliquerons des **transformateurs de colonnes** (column transformers) aux caractéristiques numériques et catégorielles séparément.

Les transformateurs de colonnes sont avantageux pour gérer les jeux de données avec plusieurs types de données, car ils peuvent appliquer différentes transformations à différents sous-ensembles de colonnes tout en évitant les fuites de données.

```python
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

categorical_features = X_train.select_dtypes(include=['object']).columns.tolist()
categorical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='most_frequent')),('onehot', OneHotEncoder(handle_unknown='ignore'))])

numerical_features = X_train.select_dtypes(include=['int64', 'float64']).columns.tolist()
numerical_transformer = Pipeline(steps=[('imputer', SimpleImputer(strategy='mean')), ('scaler', StandardScaler())])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

X_train_processed = preprocessor.fit_transform(X_train)
X_val_processed = preprocessor.transform(X_val)
X_test_processed = preprocessor.transform(X_test)
```

## Comprendre les optimiseurs

En deep learning, un optimiseur est un élément crucial qui affine les paramètres d'un réseau de neurones pendant l'entraînement. Son rôle principal est de minimiser la fonction de perte du modèle, améliorant ainsi les performances.

Divers algorithmes d'optimisation, appelés optimiseurs, emploient des stratégies distinctes pour converger efficacement vers les paramètres optimaux pour de meilleures prédictions.

Dans cet article, nous utiliserons l'optimiseur SGD et l'optimiseur Adam.

### 1. Comment fonctionne un optimiseur SGD (Descente de gradient stochastique)

SGD est un algorithme d'optimisation majeur qui calcule le gradient (dérivée partielle de la fonction de coût) en utilisant un petit mini-lot d'exemples à chaque époque :

$$\begin{align*} w_j &:= w_j - \eta \frac {\partial J} {\partial w_j} \\ \\ b &:= b - \eta \frac {\partial J} {\partial b} \end{align*}$$

(w : poids, b : biais, J : fonction de coût, *η* : taux d'apprentissage)

Dans la classification binaire, la fonction de coût (J) est définie avec une fonction sigmoïde (σ(z)) où z génère la somme pondérée des entrées et des termes de biais :

$$\begin{align*} J(y, \hat y) &=\u2212[y log(\hat y) + (1-y)log(1-\hat y)] \\ \\ \hat y &= \sigma (z) = \frac {1} {1+e^{-z}} \\ \\ z &= \sum_{i=1}^m w_i x_i + b \end {align*}$$

### 2. Comment fonctionne l'optimiseur Adam (Estimation adaptative du moment)

Adam est un algorithme d'optimisation qui calcule des **taux d'apprentissage adaptatifs individuels** pour différents paramètres à partir d'estimations des premiers et seconds moments des gradients.

L'optimiseur Adam combine les avantages de [**RMSprop**](https://keras.io/api/optimizers/rmsprop/) (utilisation de gradients au carré pour mettre à l'échelle le taux d'apprentissage) et du [**Momentum**](https://optimization.cbe.cornell.edu/index.php?title=Momentum) (utilisation de gradients passés pour accélérer la convergence) :

$$w_{j,t+1} = w_{j,t} - \alpha \cdot \frac{\hat{m}{t,w_j}}{\sqrt{\hat{v}{t,w_j}} + \epsilon}$$

où :

* `α` : Le taux d'apprentissage (par défaut 0,001)
    
* `ϵ` : Une petite constante positive utilisée pour éviter la division par zéro
    
* `m^` : Estimation du premier moment (moyenne) avec une correction de biais, tirant parti du **Momentum** :
    

$$\begin{align*} \hat m_t &= \frac {m_t} {1 - \beta_1^t} \\ \\ m_t &= \beta_1 m_{t-1} + (1-\beta_1) \underbrace{ \frac {\partial L} {\partial w_t}}_{\text{gradient}} \end{align*}$$

(`β1​​` : **Taux de décroissance**, généralement fixé à β1=0,9)

`v^` : Estimation du second moment (variance) avec une correction de biais, tirant parti de **RMSprop** :

$$\begin{align*} \hat v_t &= \frac {v_t} {1 - \beta_2^t} \\ \\ v_t &=\beta_2 v_{t-1} + (1- \beta_2) (\frac {\partial L} {\partial w_t})^2 \end {align*}$$

(`β2​​` : **Taux de décroissance**, généralement fixé à β2=0,999)

Comme `m​​` et `v​` sont tous deux initialisés à zéro, Adam calcule les estimations corrigées du biais pour éviter qu'elles ne soient biaisées vers zéro.

En savoir plus : [Guide complet sur les réseaux de neurones en Deep Learning](https://medium.com/@kuriko-iwai/a-comprehensive-guide-on-neural-network-in-deep-learning-9c795a1f1648)

## Comment construire un classificateur MLP avec l'optimiseur SGD

### Classificateur personnalisé

Ce processus implique une **passe avant** (forward pass) et une **rétropropagation** (backpropagation), au cours de laquelle SGD calcule les poids et biais optimaux à l'aide des gradients :

```python
for i in range(0, n_samples, self.batch_size):
    # SGD commence par un mini-lot sélectionné au hasard pour l'époque
    X_batch = X_shuffled[i : i + self.batch_size]
    y_batch = y_shuffled[i : i + self.batch_size]

    # A. passe avant
    activations, zs = self._forward_pass(X_batch)
    y_pred = activations[-1]  # sortie finale du réseau

    # B. rétropropagation
    # 1) calcul des gradients pour la couche de sortie)
    delta = y_pred - y_batch
    dW = np.dot(activations[-2].T, delta) / X_batch.shape[0]
    db = np.sum(delta, axis=0) / X_batch.shape[0]

    # 2) mise à jour des paramètres de la couche de sortie
    self.weights[-1] -= self.learning_rate * dW
    self.biases[-1] -= self.learning_rate * db

    # 3) itération arrière de la dernière couche cachée vers la couche d'entrée
    for l in range(len(self.weights) - 2, -1, -1):
        delta = np.dot(delta, self.weights[l+1].T) * self._relu_derivative(zs[l]) # d_activation(z)
        dW = np.dot(activations[l].T, delta) / X_batch.shape[0]
        db = np.sum(delta, axis=0) / X_batch.shape[0]

        self.weights[l] -= self.learning_rate * dW
        self.biases[l] -= self.learning_rate * db
```

Dans le processus de passe avant, le réseau calcule une somme pondérée des poids et du biais (z), applique une fonction d'activation (ReLU) aux valeurs de chaque couche cachée, puis calcule la sortie prédite (y\_pred) à l'aide d'une fonction sigmoïde.

```python
def _forward_pass(self, X):
    activations = [X]
    zs = []

    # propagation avant à travers les couches cachées
    for i in range(len(self.weights) - 1):
        z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
        zs.append(z)
        a = self._relu(z) # utilisation de ReLU pour les couches cachées
        activations.append(a)

    # propagation avant à travers la couche de sortie
    z_output = np.dot(activations[-1], self.weights[-1]) + self.biases[-1]
    zs.append(z_output)
    
    # calcule la sortie finale à l'aide de la fonction sigmoïde
    y_pred = 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    activations.append(y_pred)
    return activations, zs
```

Ainsi, le classificateur final ressemble à ceci :

```python
from sklearn.metrics import accuracy_score

class MLP_SGD:
    def __init__(self, hidden_layer_sizes=(10,), learning_rate=0.01, n_epochs=1000, batch_size=32):
        self.hidden_layer_sizes = hidden_layer_sizes
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs
        self.batch_size = batch_size
        self.weights = []
        self.biases = []
        self.weights_history = []
        self.biases_history = []
        self.loss_history = []

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def _sigmoid_derivative(self, x):
        s = self._sigmoid(x)
        return s * (1 - s)

    def _relu(self, x):
        return np.maximum(0, x)

    def _relu_derivative(self, x):
        return (x > 0).astype(float)

    def _initialize_parameters(self, n_features):
        layer_sizes = [n_features] + list(self.hidden_layer_sizes) + [1]
        self.weights = []
        self.biases = []

        for i in range(len(layer_sizes) - 1):
            fan_in = layer_sizes[i]
            fan_out = layer_sizes[i+1]
            limit = np.sqrt(6 / (fan_in + fan_out))
            self.weights.append(np.random.uniform(-limit, limit, (fan_in, fan_out)))
            self.biases.append(np.zeros((1, fan_out)))

    def _forward_pass(self, X):
        activations = [X]
        zs = []

        for i in range(len(self.weights) - 1):
            z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            zs.append(z)
            a = self._relu(z)
            activations.append(a)

        z_output = np.dot(activations[-1], self.weights[-1]) + self.biases[-1]
        zs.append(z_output)
        y_pred = self._sigmoid(z_output)
        activations.append(y_pred)

        return activations, zs

    def _compute_loss(self, y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-10, 1 - 1e-10)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    def fit(self, X, y):
        n_samples, n_features = X.shape
        y = np.asarray(y).reshape(-1, 1)
        X = np.asarray(X)
        self._initialize_parameters(n_features)
        self.weights_history.append([w.copy() for w in self.weights])
        self.biases_history.append([b.copy() for b in self.biases])
        activations, _ = self._forward_pass(X)
        initial_loss = self._compute_loss(y, activations[-1])
        self.loss_history.append(initial_loss)

        for epoch in range(self.n_epochs):
            # mélanger les jeux de données
            permutation = np.random.permutation(n_samples)
            X_shuffled = X[permutation]
            y_shuffled = y[permutation]

            # boucle mini-lot
            for i in range(0, n_samples, self.batch_size):
                X_batch = X_shuffled[i : i + self.batch_size]
                y_batch = y_shuffled[i : i + self.batch_size]

                activations, zs = self._forward_pass(X_batch)
                y_pred = activations[-1]

                delta = y_pred - y_batch
                dW = np.dot(activations[-2].T, delta) / X_batch.shape[0]
                db = np.sum(delta, axis=0) / X_batch.shape[0]
                self.weights[-1] -= self.learning_rate * dW
                self.biases[-1] -= self.learning_rate * db

                for l in range(len(self.weights) - 2, -1, -1):
                    delta = np.dot(delta, self.weights[l+1].T) * self._relu_derivative(zs[l]) # d_activation(z)
                    dW = np.dot(activations[l].T, delta) / X_batch.shape[0]
                    db = np.sum(delta, axis=0) / X_batch.shape[0]

                    self.weights[l] -= self.learning_rate * dW
                    self.biases[l] -= self.learning_rate * db

            self.weights_history.append([w.copy() for w in self.weights])
            self.biases_history.append([b.copy() for b in self.biases])

            activations, _ = self._forward_pass(X)
            epoch_loss = self._compute_loss(y, activations[-1])
            self.loss_history.append(epoch_loss)

            if (epoch + 1) % 100 == 0:
                print(f"Epoch {epoch+1}/{self.n_epochs}, Loss: {epoch_loss:.4f}")
        return self

    def predict_proba(self, X):
        activations, _ = self._forward_pass(X)
        return activations[-1]

    def predict(self, X, threshold=0.5):
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int).flatten() # pour sortie 1D
```

### Entraînement / Prédiction

Entraînez le modèle et faites une prédiction à l'aide des jeux de données d'entraînement et de validation :

```python
# 1. définir le modèle
mlp_sgd = MLP_SGD(
  hidden_layer_sizes=(30, 30, ), # 2 couches cachées avec 30 neurones chacune
  learning_rate=0.001,           # un pas (step size)
  n_epochs=1000,                 # nombre d'époques
  batch_size=32                  # taille du mini-lot
)

# 2. entraîner le modèle
mlp_sgd.fit(X_train_processed, y_train)

# 3. faire une prédiction avec les jeux de données d'entraînement et de validation
y_pred_train = mlp_sgd.predict(X_train_processed)
y_pred_val = mlp_sgd.predict(X_val_processed)

# 4. calculer les métriques d'évaluation
conf_matrix = confusion_matrix(y_true, y_pred)
acc = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, pos_label=1)
recall = recall_score(y_true, y_pred, pos_label=1)
f1 = f1_score(y_true, y_pred, pos_label=1)


print(f"\
MLP (Custom SGD) Accuracy (Train): {acc_train:.3f}")
print(f"MLP (Custom SGD) Accuracy (Validation): {acc_val:.3f}")
```

### Résultats

* Rappel (Recall) : *0.7930 — 0.6650 (de l'entraînement à la validation)*
    
* Précision : *0.7790 — 0.6786 (de l'entraînement à la validation)*
    

Le modèle a efficacement appris et généralisé les modèles, atteignant un **Rappel de 79,3 %** (environ 80 % de précision dans l'identification des transactions frauduleuses) avec une baisse de 12 points sur l'ensemble de validation.

**Historique des pertes :**

![Perte par époque, historique des poids, historique du biais (Source : Kuriko Iwai)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748441103897/088deb38-846d-4026-a706-701be93036ca.png align="center")

Nous avons visualisé la **frontière de décision** en utilisant les deux premières composantes principales (PCA) comme axes x et y. Notez que la frontière n'est pas linéaire.

![Image : Frontière de décision du classificateur MLP avec l'optimiseur SGD (Source : Kuriko Iwai)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748442430297/032ee809-1b7e-4bb1-81c0-8715361658a5.png align="center")

### Tirer parti du classificateur MLP de Scikit-learn

Nous pouvons utiliser un `MLPClassifier` pour définir un modèle similaire, en incorporant ;

* L'**arrêt précoce** (early stopping) en utilisant la validation interne pour éviter le surapprentissage et
    
* La **régularisation L2** avec une petite tolérance.
    

```python
from sklearn.neural_network import MLPClassifier

# définir un modèle
model_sklearn_mlp_sgd = MLPClassifier(
    hidden_layer_sizes=(30, 30),
    activation='relu',
    solver='sgd',
    learning_rate_init=0.001,
    learning_rate='constant',
    momentum=0.9,
    nesterovs_momentum=True,
    alpha=0.00001,           # force de régularisation l2
    max_iter=3000,           # époques max (garder élevé)
    batch_size=16,           # taille du mini-lot
    random_state=42,
    early_stopping=True,     # appliquer l'arrêt précoce
    n_iter_no_change=50,     # arrêter l'itération si le score de validation interne ne s'améliore pas pendant 50 époques
    validation_fraction=0.1, # proportion des données d'entraînement pour la validation interne (par défaut 0,1)
    tol=1e-4,                # tolérance pour l'optimisation
    verbose=False,
)

# entraînement
model_sklearn_mlp_sgd.fit(X_train_processed, y_train)

# faire une prédiction
y_pred_train_sklearn = model_sklearn_mlp_sgd.predict(X_train_processed)
y_pred_val_sklearn = model_sklearn_mlp_sgd.predict(X_val_processed)
```

### Résultats

* Rappel (Recall) : *0.7830 - 0.6200 (de l'entraînement à la validation)*
    
* Précision : *0.8208 — 0.6703 (de l'entraînement à la validation)*
    

Le modèle a montré de fortes performances pendant l'entraînement, atteignant un Rappel **de 78,30 %**. Ses performances ont décliné sur l'ensemble de validation.

Cela suggère que bien que le modèle ait appris efficacement à partir des données d'entraînement, il peut être en surapprentissage et ne pas généraliser aussi bien aux données non vues.

### Tirer parti du classificateur séquentiel Keras

Pour le classificateur séquentiel, nous pouvons encore améliorer le classificateur en :

* Initialisant le biais de la couche de sortie avec le log-odds des occurrences de la classe positive dans les données d'entraînement (y\_train​) pour remédier au déséquilibre du jeu de données et favoriser une convergence plus rapide,
    
* Intégrant un dropout de 10 % entre les couches cachées pour éviter le surapprentissage en désactivant aléatoirement des neurones pendant l'entraînement,
    
* Incluant la Précision et le Rappel dans les métriques de compilation du modèle pour optimiser les performances de classification,
    
* Appliquant des poids de classe pour pénaliser plus lourdement les erreurs de classification de la classe minoritaire, améliorant ainsi la capacité du modèle à apprendre des modèles rares, et
    
* Utilisant un jeu de données de validation distinct pour surveiller les performances pendant l'entraînement afin d'aider à détecter le surapprentissage et de guider le réglage des hyperparamètres.
    

```python
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Input
from keras.optimizers import SGD
from keras.callbacks import EarlyStopping
from sklearn.utils import class_weight


# calcule un biais initial pour la couche de sortie 
initial_bias = np.log([np.sum(y_train == 1) / np.sum(y_train == 0)])


# définit le modèle
model_keras_sgd = Sequential([
    Input(shape=(X_train_processed.shape[1],)), 
    Dense(30, activation='relu'),
    Dropout(0.1), # 10 % des neurones de cette couche sont abandonnés au hasard
    Dense(30, activation='relu'),
    Dropout(0.1),
    Dense(1, activation='sigmoid', # classification binaire
          bias_initializer=tf.keras.initializers.Constant(initial_bias)) # pour remédier au déséquilibre des jeux de données
])



# compile le modèle avec l'optimiseur SGD
opt = SGD(learning_rate=0.001)
model_keras_sgd.compile(
    optimizer=opt, 
    loss='binary_crossentropy',
    metrics=[
        'accuracy', # ajouter plusieurs métriques à retourner
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall'),
        tf.keras.metrics.AUC(name='auc') 
    ]
)


# définit l'arrêt précoce pour éviter le surapprentissage
early_stopping_callback = EarlyStopping(
    monitor='val_recall',  # surveiller le rappel 
    mode='max',         # maximiser le rappel
    patience=50,        # arrêter après 50 époques sans amélioration de la perte
    min_delta=1e-4,     # changement minimum pour être considéré comme une amélioration (tol)
    verbose=0
)


# calculer le poids de la classe
class_weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)
class_weights_dict = dict(zip(np.unique(y_train), class_weights))


# entraîner le modèle
history = model_keras_sgd.fit(
    X_train_processed, y_train,
    epochs=1000,
    batch_size=32,
    validation_data=(X_val_processed, y_val), # utiliser notre ensemble val externe
    callbacks=[early_stopping_callback], # arrêt précoce pour éviter le surapprentissage
    class_weight=class_weights_dict, # pénaliser davantage les erreurs de classification sur la classe minoritaire
    verbose=0
)

# évaluer
loss_train, accuracy_train, precision_train, recall_train, auc_train = model_keras_sgd.evaluate(X_train_processed, y_train, verbose=0)
print(f"\
--- Keras Model Accuracy (Train) ---")
print(f"Loss: {loss_train:.4f}")
print(f"Accuracy: {accuracy_train:.4f}")
print(f"Precision: {precision_train:.4f}")
print(f"Recall: {recall_train:.4f}")
print(f"AUC: {auc_train:.4f}")

loss_val, accuracy_val, precision_val, recall_val, auc_val = model_keras_sgd.evaluate(X_val_processed, y_val, verbose=0)
print(f"\
--- Keras Model Accuracy (Validation) ---")
print(f"Loss: {loss_val:.4f}")
print(f"Accuracy: {accuracy_val:.4f}")
print(f"Precision: {precision_val:.4f}")
print(f"Recall: {recall_val:.4f}")
print(f"AUC: {auc_val:.4f}")

# afficher le résumé du modèle
model_keras_sgd.summary()
```

### Résultats

* Rappel (Recall) : *0.7125 — 0.7250 (de l'entraînement à la validation)*
    
* Précision : *0.7607 — 0.7545 (de l'entraînement à la validation)*
    

Étant donné que les écarts entre l'entraînement et la validation sont relativement faibles, le modèle généralise raisonnablement bien.

Cela suggère que les techniques de régularisation sont probablement efficaces pour prévenir un surapprentissage significatif.

![Image : Résumé du modèle séquentiel Keras avec l'optimiseur SGD](https://cdn.hashnode.com/res/hashnode/image/upload/v1748441165170/4e0528e3-514a-454c-b52a-2a0318ba405a.png align="center")

## Comment construire un classificateur MLP avec l'optimiseur Adam

### Classificateur personnalisé

Ce processus itératif de mise à jour des paramètres se produit dans la boucle mini-lot pour continuer à mettre à jour les poids et le biais :

```python
# appliquer les mises à jour d'Adam pour les paramètres de la couche de sortie
# 1) poids (w)
self.m_weights[-1] = self.beta1 * self.m_weights[-1] + (1 - self.beta1) * grad_w_output
self.v_weights[-1] = self.beta2 * self.v_weights[-1] + (1 - self.beta2) * (grad_w_output ** 2)
m_w_hat = self.m_weights[-1] / (1 - self.beta1**t)
v_w_hat = self.v_weights[-1] / (1 - self.beta2**t)
self.weights[-1] -= self.learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.epsilon)

# 2) biais (b)
self.m_biases[-1] = self.beta1 * self.m_biases[-1] + (1 - self.beta1) * grad_b_output
self.v_biases[-1] = self.beta2 * self.v_biases[-1] + (1 - self.beta2) * (grad_b_output ** 2)
m_b_hat = self.m_biases[-1] / (1 - self.beta1**t)
v_b_hat = self.v_biases[-1] / (1 - self.beta2**t)
self.biases[-1] -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)
```

En suivant les principes des passes avant et arrière, nous construisons le classificateur final en l'initialisant avec `beta1` et `beta2`, bâti sur une architecture `MLP_SGD` :

```python
class MLP_Adam:
    def __init__(self, hidden_layer_sizes=(10,), learning_rate=0.001, n_epochs=1000, batch_size=32,
                 beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.hidden_layer_sizes = hidden_layer_sizes
        self.learning_rate = learning_rate
        self.n_epochs = n_epochs
        self.batch_size = batch_size
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon

        self.weights = [] 
        self.biases = []

        # États internes de l'optimiseur Adam pour chaque paramètre (poids et biais)
        self.m_weights = []
        self.v_weights = []
        self.m_biases = []
        self.v_biases = []

        self.weights_history = []
        self.biases_history = []
        self.loss_history = []

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def _sigmoid_derivative(self, x):
        s = self._sigmoid(x)
        return s * (1 - s)

    def _relu(self, x):
        return np.maximum(0, x)

    def _relu_derivative(self, x):
        return (x > 0).astype(float)

    def _initialize_parameters(self, n_features):
        layer_sizes = [n_features] + list(self.hidden_layer_sizes) + [1]

        self.weights = []
        self.biases = []
        self.m_weights = []
        self.v_weights = []
        self.m_biases = []
        self.v_biases = []

        for i in range(len(layer_sizes) - 1):
            fan_in = layer_sizes[i]
            fan_out = layer_sizes[i+1]
            limit = np.sqrt(6 / (fan_in + fan_out))

            self.weights.append(np.random.uniform(-limit, limit, (fan_in, fan_out)))
            self.biases.append(np.zeros((1, fan_out)))

            self.m_weights.append(np.zeros((fan_in, fan_out)))
            self.v_weights.append(np.zeros((fan_in, fan_out)))
            self.m_biases.append(np.zeros((1, fan_out)))
            self.v_biases.append(np.zeros((1, fan_out)))


    def _forward_pass(self, X):
        activations = [X]
        zs = []

        for i in range(len(self.weights) - 1):
            z = np.dot(activations[-1], self.weights[i]) + self.biases[i]
            zs.append(z)
            a = self._relu(z)
            activations.append(a)

        z_output = np.dot(activations[-1], self.weights[-1]) + self.biases[-1]
        zs.append(z_output)
        y_pred = self._sigmoid(z_output)
        activations.append(y_pred)

        return activations, zs

    def _compute_loss(self, y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-10, 1 - 1e-10)
        loss = -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
        return loss

    def fit(self, X, y):
        n_samples, n_features = X.shape
        y = np.asarray(y).reshape(-1, 1)
        X = np.asarray(X)

        self._initialize_parameters(n_features)
        self.weights_history.append([w.copy() for w in self.weights])
        self.biases_history.append([b.copy() for b in self.biases])
        activations, _ = self._forward_pass(X)
        initial_loss = self._compute_loss(y, activations[-1])
        self.loss_history.append(initial_loss)

        # pas de temps global pour la correction du biais d'Adam
        t = 0

        for epoch in range(self.n_epochs):
            permutation = np.random.permutation(n_samples)
            X_shuffled = X[permutation]
            y_shuffled = y[permutation]

            # Boucle mini-lot
            for i in range(0, n_samples, self.batch_size):
                X_batch = X_shuffled[i : i + self.batch_size]
                y_batch = y_shuffled[i : i + self.batch_size]

                t += 1

                # 1. passe avant
                activations, zs = self._forward_pass(X_batch)
                y_pred = activations[-1] # Sortie du réseau

                # 2. rétropropagation
                delta = y_pred - y_batch
                grad_w_output = np.dot(activations[-2].T, delta) / X_batch.shape[0] # Moyenne sur le lot
                grad_b_output = np.sum(delta, axis=0) / X_batch.shape[0]

                # appliquer les mises à jour d'Adam aux poids
                self.m_weights[-1] = self.beta1 * self.m_weights[-1] + (1 - self.beta1) * grad_w_output
                self.v_weights[-1] = self.beta2 * self.v_weights[-1] + (1 - self.beta2) * (grad_w_output ** 2)
                m_w_hat = self.m_weights[-1] / (1 - self.beta1**t)
                v_w_hat = self.v_weights[-1] / (1 - self.beta2**t)
                self.weights[-1] -= self.learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.epsilon)
                
                # appliquer les mises à jour d'Adam au biais
                self.m_biases[-1] = self.beta1 * self.m_biases[-1] + (1 - self.beta1) * grad_b_output
                self.v_biases[-1] = self.beta2 * self.v_biases[-1] + (1 - self.beta2) * (grad_b_output ** 2)
                m_b_hat = self.m_biases[-1] / (1 - self.beta1**t)
                v_b_hat = self.v_biases[-1] / (1 - self.beta2**t)
                self.biases[-1] -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)


                # Propager les gradients en arrière à travers les couches cachées
                for l in range(len(self.weights) - 2, -1, -1):
                    delta = np.dot(delta, self.weights[l+1].T) * self._relu_derivative(zs[l]) # d_activation(z)
                    grad_w_hidden = np.dot(activations[l].T, delta) / X_batch.shape[0]
                    grad_b_hidden = np.sum(delta, axis=0) / X_batch.shape[0]

                    # appliquer les mises à jour d'Adam aux poids
                    self.m_weights[l] = self.beta1 * self.m_weights[l] + (1 - self.beta1) * grad_w_hidden
                    self.v_weights[l] = self.beta2 * self.v_weights[l] + (1 - self.beta2) * (grad_w_hidden ** 2)
                    m_w_hat = self.m_weights[l] / (1 - self.beta1**t)
                    v_w_hat = self.v_weights[l] / (1 - self.beta2**t)
                    self.weights[l] -= self.learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.epsilon)
                    
                    # appliquer les mises à jour d'Adam au biais
                    self.m_biases[l] = self.beta1 * self.m_biases[l] + (1 - self.beta1) * grad_b_hidden
                    self.v_biases[l] = self.beta2 * self.v_biases[l] + (1 - self.beta2) * (grad_b_hidden ** 2)
                    m_b_hat = self.m_biases[l] / (1 - self.beta1**t)
                    v_b_hat = self.v_biases[l] / (1 - self.beta2**t)
                    self.biases[l] -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)

          
            self.weights_history.append([w.copy() for w in self.weights])
            self.biases_history.append([b.copy() for b in self.biases])

            activations, _ = self._forward_pass(X)
            epoch_loss = self._compute_loss(y, activations[-1])
            self.loss_history.append(epoch_loss)

            if (epoch + 1) % 100 == 0:
                print(f"Epoch {epoch+1}/{self.n_epochs}, Loss: {epoch_loss:.4f}")
        return self


    def predict_proba(self, X):
        activations, _ = self._forward_pass(X)
        return activations[-1]

    def predict(self, X, threshold=0.5):
        probabilities = self.predict_proba(X)
        return (probabilities >= threshold).astype(int).flatten()
```

### Entraînement / Prédiction

Entraînez le modèle et faites une prédiction à l'aide des jeux de données d'entraînement et de validation :

```python
mlp_adam = MLP_Adam(hidden_layer_sizes=(30, 10), learning_rate=0.001, n_epochs=500, batch_size=32)
mlp_adam.fit(X_train_processed, y_train)

y_pred_train = mlp_adam.predict(X_train_processed)
y_pred_val = mlp_adam.predict(X_val_processed)

acc_train = accuracy_score(y_train, y_pred_train)
acc_val = accuracy_score(y_val, y_pred_val)

print(f"\
MLP (Custom Adam) Accuracy (Train): {acc_train:.3f}")
print(f"MLP (Custom Adam) Accuracy (Validation): {acc_val:.3f}")
```

### Résultats

* Rappel (Recall) : *0.9870–0.6150 (de l'entraînement à la validation)*
    
* Précision : *0.9811–0.6474 (de l'entraînement à la validation)*
    

Bien que l'optimiseur Adam ait surpassé SGD, le modèle a présenté un surapprentissage important, avec une baisse d'environ 30 points du Rappel et de la Précision entre l'entraînement et la validation.

**Historique des pertes**

![Perte par époque, milieu : historique des poids par époque, droite : historique du biais par époque (Source : Kuriko Iwai)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748442341394/3183a9b1-5df0-4f74-9473-6b5b595dc9c0.png align="center")

Nous avons visualisé la frontière de décision en utilisant les deux premières composantes principales (PCA) comme axes x et y.

![Frontière de décision d'un MLP avec l'optimiseur Adam (Source : Kuriko Iwai)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748442311514/34f004c9-bf1d-41e5-a0af-08c62802b78c.png align="center")

### Tirer parti du classificateur MLP de Scikit-learn

Nous avons remplacé l'optimiseur SGD par Adam, en gardant tous les autres paramètres constants :

```python
model_sklearn_mlp_adam = MLPClassifier(
    hidden_layer_sizes=(30, 30),
    activation='relu',
    solver='adam',             # mise à jour de l'optimiseur de SGD à Adam
    learning_rate_init=0.001,
    learning_rate='constant',
    alpha=0.0001,
    max_iter=3000,
    batch_size=16,
    random_state=42,
    early_stopping=True,
    n_iter_no_change=50,
    validation_fraction=0.1,
    tol=1e-4,
    verbose=False,
)

model_sklearn_mlp_adam.fit(X_train_processed, y_train)

y_pred_train_sklearn = model_sklearn_mlp_adam.predict(X_train_processed)
y_pred_val_sklearn = model_sklearn_mlp_adam.predict(X_val_processed)
```

### Résultats

* *Rappel (Recall) : 0.8975–0.6400 (de l'entraînement à la validation)*
    
* *Précision : 0.8864 — 0.6305 (de l'entraînement à la validation)*
    

Malgré une amélioration des performances par rapport à l'optimiseur SGD, la chute importante du Rappel (de 0,8975 à 0,6400) et de la Précision (de 0,8864 à 0,6305) des données d'entraînement aux données de validation indique que le modèle est toujours en surapprentissage.

### Tirer parti du classificateur séquentiel Keras

Semblable au `MLPClassifier`, nous avons remplacé l'optimiseur SGD par Adam, toutes les autres conditions restant les mêmes :

```python
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Input
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from sklearn.utils import class_weight


initial_bias = np.log([np.sum(y_train == 1) / np.sum(y_train == 0)])
model_keras_adam = Sequential([
    Input(shape=(X_train_processed.shape[1],)), 
    Dense(30, activation='relu'),
    Dropout(0.1),
    Dense(30, activation='relu'),
    Dropout(0.1),
    Dense(1, activation='sigmoid', 
          bias_initializer=tf.keras.initializers.Constant(initial_bias))
])


optimizer_keras = Adam(learning_rate=0.001)
model_keras_adam.compile(
    optimizer=optimizer_keras, 
    loss='binary_crossentropy', 
    metrics=[
        'accuracy',
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall'),
        tf.keras.metrics.AUC(name='auc') 
    ]
)

early_stopping_callback = EarlyStopping(
    monitor='val_recall',
    mode='max',
    patience=50,
    min_delta=1e-4,
    verbose=0
)

class_weights = class_weight.compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)
class_weights_dict = dict(zip(np.unique(y_train), class_weights))

model_keras_adam.fit(
    X_train_processed, y_train,
    epochs=1000,
    batch_size=32,
    validation_data=(X_val_processed, y_val),
    callbacks=[early_stopping_callback],
    class_weight=class_weights_dict,
    verbose=0
)


loss_train, accuracy_train, precision_train, recall_train, auc_train = model_keras_adam.evaluate(X_train_processed, y_train, verbose=0)
print(f"\
--- Keras Model Accuracy (Train) ---")
print(f"Loss: {loss_train:.4f}")
print(f"Accuracy: {accuracy_train:.4f}")
print(f"Precision: {precision_train:.4f}")
print(f"Recall: {recall_train:.4f}")
print(f"AUC: {auc_train:.4f}")


loss_val, accuracy_val, precision_val, recall_val, auc_val = model_keras_adam.evaluate(X_val_processed, y_val, verbose=0)
print(f"\
--- Keras Model Accuracy (Validation) ---")
print(f"Loss: {loss_val:.4f}")
print(f"Accuracy: {accuracy_val:.4f}")
print(f"Precision: {precision_val:.4f}")
print(f"Recall: {recall_val:.4f}")
print(f"AUC: {auc_val:.4f}")


model_keras_adam.summary()
```

### Résultats

* *Rappel (Recall) : 0.7995–0.7500 (de l'entraînement à la validation)*
    
* *Précision : 0.8409–0.8065 (de l'entraînement à la validation)*
    

Le modèle présente de bonnes performances, avec un Rappel diminuant légèrement de 0,7995 (entraînement) à 0,7500 (validation), et une Précision chutant de la même manière de 0,8409 (entraînement) à 0,8065 (validation).

Cela indique une bonne généralisation, avec seulement une dégradation mineure des performances sur les données non vues.

![Image : Modèle séquentiel Keras avec l'optimiseur Adam (Source : Kuriko Iwai)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748441767800/fe43f181-4323-461f-b56a-125fc78e9c84.png align="center")

## Résultats finaux : Généralisation

Enfin, nous allons évaluer les performances ultimes du modèle sur le jeu de données de test, qui est resté complètement séparé de tous les processus d'entraînement et de validation précédents.

```python
# Classificateurs personnalisés
y_pred_test_custom_sgd = mlp_sgd.fit(X_train_processed, y_train).predict(X_test_processed)
y_pred_test_custom_adam = mlp_adam.fit(X_train_processed, y_train).predict(X_test_processed)

# MLPClassifier
y_pred_test_sk_sgd = model_sklearn_mlp_sgd.fit(X_train_processed, y_train).predict(X_test_processed)
y_pred_test_sk_adam = model_sklearn_mlp_adam.fit(X_train_processed, y_train).predict(X_test_processed)

# Keras Sequential
_, accuracy_val_sgd, precision_val_sgd, recall_val_sgd, auc_val_sgd = model_keras_sgd.evaluate(X_test_processed, y_test, verbose=0)
_, accuracy_val_adam, precision_val_adam, recall_val_adam, auc_val_adam = model_keras_adam.evaluate(X_test_processed, y_test, verbose=0)
```

Globalement, le modèle Keras Sequential, optimisé avec SGD, a obtenu les meilleures performances avec une **AUPRC (Area Under Precision-Recall Curve) de 0,72.**

![Courbes Précision-Rappel pour six modèles de classificateurs (Comparaison des classificateurs Custom, MLP et Keras Sequential avec les optimiseurs SGD et Adam (Source : Kuriko Iwai)](https://cdn.hashnode.com/res/hashnode/image/upload/v1748874699534/f0f008c4-9067-4e2a-b070-4bb5cbae8f23.png align="center")

## Conclusion

Dans cette exploration, nous avons expérimenté avec des classificateurs personnalisés, des modèles Scikit-learn et des architectures de Deep Learning Keras.

Nos conclusions soulignent qu'un Machine Learning efficace repose sur trois facteurs critiques :

1. **un prétraitement des données robuste** (adapté aux objectifs et à la distribution des données),
    
2. **une sélection judicieuse du modèle**, et
    
3. **des choix stratégiques de Framework ou de bibliothèques**.
    

### **Choisir le bon Framework**

D'une manière générale, choisissez `MLPClassifier` lorsque :

* Vous travaillez principalement avec des **données tabulaires**,
    
* Vous voulez privilégier la **simplicité, l'itération rapide et l'intégration transparente**,
    
* Vous avez des architectures simples et peu profondes, et
    
* Vous avez une taille de jeu de données modérée (gérable sur un CPU).
    

Choisissez Keras `Sequential` lorsque :

* Vous traitez des **images, du texte, de l'audio ou d'autres données séquentielles**,
    
* Vous construisez des **modèles de Deep Learning** tels que des CNN, RNN, LSTM,
    
* Vous avez besoin d'un **contrôle fin** sur l'architecture du modèle, le processus d'entraînement ou les composants personnalisés,
    
* Vous avez besoin de tirer parti de l'**accélération GPU**,
    
* Vous planifiez un **déploiement en production**, et
    
* Vous voulez expérimenter des techniques de Deep Learning plus avancées.
    

### Limites des MLP

Bien que les perceptrons multicouches (MLP) se soient avérés précieux, leur sensibilité à la complexité de calcul et au surapprentissage sont apparues comme des défis majeurs.

À l'avenir, nous verrons comment les réseaux de neurones récurrents (RNN) et les réseaux de neurones convolutifs (CNN) offrent des solutions puissantes à ces limitations inhérentes aux MLP.

Vous pouvez trouver plus d'informations sur moi sur mon [Portfolio](https://kuriko.vercel.app/) / [LinkedIn](https://www.linkedin.com/in/k-i-i) / [Github](https://github.com/versionhq/multi-agent-system).
