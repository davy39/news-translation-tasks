---
title: Comment construire un modèle d'intelligence artificielle interprétable - Exemple
  simple de code Python
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-07-23T22:11:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-interpretable-ai-deep-learning-model
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/pexels-dmitry-demidov-515774-3852577.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: Python
  slug: python
seo_title: Comment construire un modèle d'intelligence artificielle interprétable
  - Exemple simple de code Python
seo_desc: 'Artificial Intelligence is being used everywhere these days. And many of
  the groundbreaking applications come from Machine Learning, a subfield of AI.

  Within Machine Learning, a field called Deep Learning represents one of the main
  areas of research....'
---

L'intelligence artificielle est utilisée partout de nos jours. Et beaucoup des applications révolutionnaires proviennent du Machine Learning, un sous-domaine de l'IA.

Au sein du Machine Learning, un domaine appelé Deep Learning représente l'un des principaux domaines de recherche. C'est du Deep Learning que naissent la plupart des nouveaux systèmes d'IA vraiment efficaces.

Mais typiquement, les systèmes d'IA nés du Deep Learning sont des systèmes assez étroits et spécialisés. Ils peuvent surpasser les humains dans un domaine très spécifique pour lequel ils ont été conçus.

Pour cette raison, de nombreux nouveaux développements en IA proviennent de systèmes spécialisés ou d'une combinaison de systèmes travaillant ensemble.

L'un des plus grands problèmes dans le domaine des modèles de Deep Learning est leur manque d'interprétabilité. L'interprétabilité signifie comprendre comment les décisions sont prises.

C'est un grand problème qui a son propre domaine, appelé IA explicable. C'est le domaine au sein de l'IA qui se concentre sur le fait de rendre les décisions d'un modèle d'IA plus facilement compréhensibles.

Voici ce que nous allons couvrir dans cet article :

* [Intelligence artificielle et l'essor du Deep Learning](#heading-intelligence-artificielle-et-lessor-du-deep-learning)
* [Un grand problème dans le deep learning : le manque d'interprétabilité](#heading-un-grand-probleme-dans-le-deep-learning-le-manque-dinterpretabilite)
* [Une solution à l'interprétabilité : les modèles de type "boîte transparente"](#heading-une-solution-a-linterpretabilite-les-modeles-de-type-boite-transparente)
* [Exemple de code : résoudre le problème avec l'IA explicable](#heading-exemple-de-code-resoudre-le-probleme-avec-lia-explicable)
* [Conclusion : KAN (Kolmogorov–Arnold Networks)](#heading-conclusion-kan-kolmogorovarnold-networks)

Cet article ne couvrira pas le dropout ou d'autres techniques de régularisation, l'optimisation des hyperparamètres, les architectures complexes comme les CNNs, ou les différences détaillées dans les variantes de descente de gradient.

Nous discuterons simplement des bases du deep learning, du problème de manque d'interprétabilité et d'un exemple de code.

<h2 id="Artificial">Intelligence artificielle et l'essor du Deep Learning</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/AI.jpg)
_Photo par [Tara Winstead](https://www.pexels.com/photo/robot-pointing-on-a-wall-8386440/)_

### Qu'est-ce que le Deep Learning dans l'intelligence artificielle ?

Le Deep Learning est un sous-domaine de l'intelligence artificielle. Il utilise des réseaux de neurones pour traiter des motifs complexes, tout comme les stratégies qu'une équipe sportive utilise pour gagner un match.

Plus le réseau de neurones est grand, plus il est capable de faire des choses impressionnantes – comme ChatGPT, par exemple, qui utilise le traitement du langage naturel pour répondre aux questions et interagir avec les utilisateurs.

Pour vraiment comprendre les bases des réseaux de neurones – ce que chaque modèle d'IA a en commun qui lui permet de fonctionner – nous devons comprendre les couches d'activation.

### Deep Learning = Entraînement des réseaux de neurones

![4-2](https://www.freecodecamp.org/news/content/images/2024/01/4-2.png)
_Réseau de neurones simple_

Au cœur du deep learning se trouve l'entraînement des réseaux de neurones.

Cela signifie essentiellement utiliser des données pour obtenir les bonnes valeurs de chaque neurone afin de pouvoir prédire ce que nous voulons.

Les réseaux de neurones sont composés de neurones organisés en couches. Chaque couche extrait des caractéristiques uniques des données.

Cette structure en couches permet aux modèles de deep learning d'analyser et d'interpréter des données complexes.

<h2 id="problem">Un grand problème dans le Deep Learning : le manque d'interprétabilité</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/interptret.jpg)
_Photo par [Koshevaya_k](https://www.pexels.com/photo/crop-unrecognizable-woman-reading-book-on-soft-bed-4170628/)_

Le Deep Learning a révolutionné de nombreux domaines en obtenant d'excellents résultats dans des tâches très complexes.

Cependant, il y a un grand problème : le manque d'interprétabilité.

Bien qu'il soit vrai que les réseaux de neurones peuvent très bien performer, nous ne comprenons pas en interne comment les réseaux de neurones peuvent obtenir d'excellents résultats.

En d'autres termes, nous savons qu'ils performant très bien avec les tâches que nous leur donnons, mais pas comment ils le font en détail.

Il est important de savoir comment le modèle pense dans des domaines tels que la santé et la conduite autonome.

En comprenant comment un modèle pense, nous pouvons être plus confiants dans sa fiabilité dans certains domaines critiques.

Ainsi, les modèles qui travaillent dans des domaines avec des réglementations strictes sont plus transparents vis-à-vis de la loi et inspirent plus de confiance lorsqu'ils sont interprétables.

Les modèles qui permettent l'interprétabilité sont appelés **modèles de type "boîte transparente"**. D'autre part, les modèles qui n'ont pas cette capacité (c'est-à-dire la plupart d'entre eux) sont appelés **modèles de type "boîte noire"**.

<h2 id="solution">Une solution à l'interprétabilité : les modèles de type "boîte transparente"</h2>

### Modèles de type "boîte transparente"

![Image](https://www.freecodecamp.org/news/content/images/2024/07/glass-pixabay-416528.jpg)
_Photo par Pixabay : https://www.pexels.com/photo/fluid-pouring-in-pint-glass-416528/_

Les modèles de type "boîte transparente" sont des modèles de machine learning conçus pour être facilement compris par les humains.

Les modèles de type "boîte transparente" fournissent des informations claires sur la manière dont ils prennent leurs décisions.

Cette transparence dans le processus de prise de décision est importante pour la confiance, la conformité et l'amélioration.

Ci-dessous, nous verrons un exemple de code d'un modèle d'IA qui, basé sur un ensemble de données pour prédire le cancer du sein, atteint une précision de 97 %.

Nous découvrirons également, en fonction des caractéristiques des données, celles qui étaient les plus importantes dans la prédiction du cancer.

### Modèles de type "boîte noire"

En plus des modèles de type "boîte transparente", il existe également des modèles de type "boîte noire".

Ces modèles sont essentiellement différentes architectures de réseaux de neurones utilisées dans divers ensembles de données. Voici quelques exemples :

* **CNN (Convolutional Neural Networks)** : Conçus spécifiquement pour la classification et l'interprétation d'images.
* **RNN (Recurrent Neural Networks) et LSTM (Long Short Term Memory)** : Principalement utilisés pour les données séquentielles – texte et données de séries temporelles. En 2017, ils ont été surpassés par une architecture de réseau de neurones appelée transformers dans un article intitulé [Attention is All You Need.](https://arxiv.org/abs/1706.03762)
* **Architectures basées sur les transformers** : Ont révolutionné l'IA en 2017 grâce à leur capacité à gérer les données séquentielles plus efficacement. Les RNN et LSTM ont des capacités limitées à cet égard.

De nos jours, la plupart des modèles qui traitent le texte sont basés sur des modèles de transformers.

Par exemple, dans ChatGPT, **GPT** signifie **Generative Pre-trained Transformer**, indiquant une architecture de réseau de neurones de type transformer qui génère du texte.

Tous ces modèles – CNN, RNN, LSTM et Transformers – sont des exemples d'intelligence artificielle étroite (IA).

Atteindre une intelligence générale, à mon avis, implique de combiner beaucoup de ces modèles d'IA étroits pour imiter le comportement humain.

<h2 id="example">Exemple de code : résoudre le problème avec l'IA explicable</h2>

![Image](https://www.freecodecamp.org/news/content/images/2024/07/cancer-chokniti-khongchum-1197604-2280571.jpg)
_Photo par Chokniti Khongchum : https://www.pexels.com/photo/person-holding-laboratory-flask-2280571/_

Dans cet exemple de code, nous allons créer un modèle d'IA interprétable basé sur 30 caractéristiques.

Nous allons également apprendre quelles sont les 5 caractéristiques les plus importantes dans la détection du cancer du sein, basé sur cet ensemble de données.

Nous allons utiliser un modèle de machine learning de type "boîte transparente" appelé Explainable Boosting Machine.

Voici le code ci-dessous, que nous verrons bloc par bloc :

```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from interpret.glassbox import ExplainableBoostingClassifier
import matplotlib.pyplot as plt
import numpy as np

# Charger un ensemble de données d'exemple
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Diviser les données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle EBM
ebm = ExplainableBoostingClassifier()
ebm.fit(X_train, y_train)

# Faire des prédictions
y_pred = ebm.predict(X_test)
print(f"Précision : {accuracy_score(y_test, y_pred)}")

# Interpréter le modèle
ebm_global = ebm.explain_global(name='EBM')

# Extraire les importances des caractéristiques
feature_names = ebm_global.data()['names']
importances = ebm_global.data()['scores']

# Trier les caractéristiques par importance
sorted_idx = np.argsort(importances)
sorted_feature_names = np.array(feature_names)[sorted_idx]
sorted_importances = np.array(importances)[sorted_idx]

# Augmenter l'espacement entre les noms des caractéristiques
y_positions = np.arange(len(sorted_feature_names)) * 1.5  # Augmenter le multiplicateur pour plus d'espace

# Tracer les importances des caractéristiques
plt.figure(figsize=(12, 14))  # Augmenter la hauteur de la figure si nécessaire
plt.barh(y_positions, sorted_importances, color='skyblue', align='center')
plt.yticks(y_positions, sorted_feature_names)
plt.xlabel('Importance')
plt.title('Importances des caractéristiques de l\'Explainable Boosting Classifier')
plt.gca().invert_yaxis()

# Ajuster l'espacement
plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.08)  # Affiner les marges si nécessaire

plt.show()

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/1-4.png)
_Code complet_

D'accord, maintenant décomposons-le.

### Importation des bibliothèques

Tout d'abord, nous allons importer les bibliothèques dont nous avons besoin pour notre exemple. Vous pouvez le faire avec le code suivant :

```
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from interpret.glassbox import ExplainableBoostingClassifier
import matplotlib.pyplot as plt
import numpy as np

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/2-3.png)
_Importation des bibliothèques_

Ce sont les bibliothèques que nous allons utiliser :

* [Pandas](https://pandas.pydata.org/) : Il s'agit d'une bibliothèque Python utilisée pour la manipulation et l'analyse de données.
* [sklearn](https://scikit-learn.org/stable/index.html) : La bibliothèque [scikit-learn](https://scikit-learn.org/stable/index.html) est utilisée pour implémenter des algorithmes de machine learning. Nous l'importons pour le prétraitement des données et l'évaluation du modèle.
* [Interpret](https://interpret.ml/) : La bibliothèque Python [interpretAI](https://interpret.ml/) est ce que nous allons utiliser pour importer le modèle que nous allons utiliser.
* [Matplotlib](https://matplotlib.org/) : Une bibliothèque Python utilisée pour créer des graphiques en Python.
* [Numpy](https://numpy.org/) : Utilisée pour des calculs numériques très rapides.

### Chargement, préparation de l'ensemble de données et division des données

```
# Charger un ensemble de données d'exemple
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.Series(data.target)

# Diviser les données
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/3-3.png)
_Chargement, préparation de l'ensemble de données et division des données_

**Tout d'abord, nous chargeons un ensemble de données d'exemple** : Nous importons un ensemble de données sur le cancer du sein en utilisant la bibliothèque Interpret.

**Ensuite, nous préparons les données** : Les caractéristiques (points de données) de l'ensemble de données sont organisées dans un format de tableau, où chaque colonne est étiquetée avec un nom de caractéristique spécifique. Les résultats cibles (étiquettes) de l'ensemble de données sont stockés séparément.

**Ensuite, nous divisons les données en ensembles d'entraînement et de test** : Les données sont divisées en deux parties : une pour entraîner le modèle et une pour tester le modèle. 80 % des données sont utilisées pour l'entraînement, tandis que 20 % sont réservées pour le test.

Une graine aléatoire spécifique est définie pour garantir que la division des données est cohérente à chaque fois que le code est exécuté.

Note rapide : Dans la vie réelle, l'ensemble de données est prétraité avec des techniques de manipulation de données pour rendre le modèle d'IA plus rapide et plus petit.

### Entraînement du modèle, réalisation de prédictions et évaluation du modèle

```
# Entraîner un modèle EBM
ebm = ExplainableBoostingClassifier()
ebm.fit(X_train, y_train)

# Faire des prédictions
y_pred = ebm.predict(X_test)
print(f"Précision : {accuracy_score(y_test, y_pred)}")


```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/4-2.png)
_Entraînement du modèle, réalisation de prédictions et évaluation du modèle_

**Tout d'abord, nous entraînons un modèle EBM** : Nous initialisons un modèle Explainable Boosting Machine puis nous l'entraîons en utilisant les données d'entraînement. Dans cette étape, avec les données que nous avons, nous créons le modèle.

De cette manière, avec une ligne de code, nous créons le modèle d'IA basé sur l'ensemble de données qui prédira le cancer du sein.

**Ensuite, nous faisons nos prédictions** : Le modèle EBM entraîné est utilisé pour faire des prédictions sur les données de test. Ensuite, nous calculons et affichons la précision des prédictions du modèle.

### Interprétation du modèle, extraction et tri des importances des caractéristiques

```
# Interpréter le modèle
ebm_global = ebm.explain_global(name='EBM')

# Extraire les importances des caractéristiques
feature_names = ebm_global.data()['names']
importances = ebm_global.data()['scores']

# Trier les caractéristiques par importance
sorted_idx = np.argsort(importances)
sorted_feature_names = np.array(feature_names)[sorted_idx]
sorted_importances = np.array(importances)[sorted_idx]

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/5-2.png)
_Interprétation du modèle, extraction et tri des importances des caractéristiques_

**À ce stade, nous devons interpréter le modèle** : L'explication globale du modèle Explainable Boosting Machine (EBM) entraîné est obtenue, fournissant un aperçu de la manière dont le modèle prend des décisions.

Dans ce modèle, nous concluons que la précision est d'environ 0,9736842105263158 – ce qui signifie que le modèle est précis 97 % du temps.

Bien sûr, cela ne s'applique qu'aux données sur le cancer du sein de **cet ensemble de données** – et non à chaque cas de détection du cancer du sein. Puisque cela est un échantillon, l'ensemble de données ne représente pas l'ensemble de la population des personnes cherchant à détecter le cancer du sein.

Note rapide : Dans le monde réel, pour la classification, nous utiliserions le **score F1** au lieu de la précision pour prédire la précision d'un modèle en raison de sa prise en compte à la fois de la **précision** et du **rappel**.

**Ensuite, nous extrayons les importances des caractéristiques** : Nous extrayons les noms et les scores d'importance correspondants des caractéristiques utilisées par le modèle à partir de l'explication globale.

**Ensuite, nous trions les caractéristiques par importance** : Les caractéristiques sont triées en fonction de leurs scores d'importance, ce qui donne une liste de noms de caractéristiques et de leurs scores d'importance respectifs, classés du moins important au plus important.

### Tracé des importances des caractéristiques

```
# Augmenter l'espacement entre les noms des caractéristiques
y_positions = np.arange(len(sorted_feature_names)) * 1.5  # Augmenter le multiplicateur pour plus d'espace

# Tracer les importances des caractéristiques
plt.figure(figsize=(12, 14))  # Augmenter la hauteur de la figure si nécessaire
plt.barh(y_positions, sorted_importances, color='skyblue', align='center')
plt.yticks(y_positions, sorted_feature_names)
plt.xlabel('Importance')
plt.title('Importances des caractéristiques de l\'Explainable Boosting Classifier')
plt.gca().invert_yaxis()

# Ajuster l'espacement
plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.08)  # Affiner les marges si nécessaire

plt.show()

```

![Image](https://www.freecodecamp.org/news/content/images/2024/07/6-1.png)
_Tracé des importances des caractéristiques_

**Maintenant, nous devons augmenter l'espacement entre les noms des caractéristiques** : Les positions des noms des caractéristiques sur l'axe des y sont ajustées pour augmenter l'espacement entre eux.

**Ensuite, nous traçons les importances des caractéristiques** : Un graphique à barres horizontales est créé pour visualiser les importances des caractéristiques. La taille du graphique est définie pour garantir qu'il est clair et lisible.

Les barres représentent les scores d'importance des caractéristiques, et les noms des caractéristiques sont affichés le long de l'axe des y.

L'axe des x du graphique est étiqueté "Importance", et le titre "Importances des caractéristiques de l'Explainable Boosting Classifier" est ajouté. L'axe des y est inversé pour avoir les caractéristiques les plus importantes en haut.

**Ensuite, nous ajustons l'espacement** : Les marges autour du graphique sont affinées pour garantir un espacement approprié et une apparence soignée.

**Enfin, nous affichons le graphique** : Le graphique est affiché pour visualiser efficacement les importances des caractéristiques.

Le résultat final devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/interpret-1.png)
_Graphique des importances des caractéristiques_

De cette manière, nous pouvons conclure à partir d'un modèle d'intelligence artificielle qui est interprétable et a une précision de 97 %, que les cinq facteurs les plus importants dans la détection des tumeurs du sein sont :

* Points concaves les plus graves
* Texture la plus grave
* Aire la plus grave
* Points concaves moyens
* Erreur d'aire et concavité la plus grave

Encore une fois, cela est selon l'ensemble de données fourni.

Ainsi, selon la population que représente cet échantillon de données, nous pouvons conclure de manière **basée sur les données** que ces facteurs sont des indicateurs clés pour la détection des tumeurs du cancer du sein.

De cette manière, nous pouvons conclure à partir d'un modèle d'intelligence artificielle, dont les méthodes interprètent le modèle, qu'il fournit des informations claires sur les caractéristiques significatives pour la prédiction.

<h2 id="Conclusion">Conclusion : KAN (Kolmogorov–Arnold Networks)</h2>

Grâce à l'IA explicable, nous pouvons étudier les populations en utilisant de nouvelles méthodes basées sur les données.

Au lieu d'utiliser uniquement les statistiques traditionnelles, les enquêtes et l'analyse manuelle des données, nous pouvons tirer des conclusions plus précisément en utilisant une bibliothèque de programmation d'IA et une base de données ou un fichier Excel.

Mais ce n'est pas la seule façon d'avoir des modèles construits avec une IA explicable.

En avril 2024, un article intitulé [KAN: Kolmogorov–Arnold Networks](https://arxiv.org/html/2404.19756v1) a été publié et pourrait secouer encore plus le domaine.

Les réseaux de Kolmogorov–Arnold (KANs) promettent d'être plus précis et plus faciles à comprendre que les modèles traditionnels et de mieux performer.

Ils sont également plus faciles à visualiser et à interagir. Nous verrons donc ce qu'il en est.

Vous pouvez trouver le code complet ici :

%[https://github.com/tiagomonteiro0715/freecodecamp-my-articles-source-code]