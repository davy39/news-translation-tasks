---
title: Comment établir la confiance dans les prédictions de votre modèle de Machine
  Learning avec LIME
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-20T16:58:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-trust-in-models-prediction-with-code
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c12740569d1a4ca2fc3.jpg
tags:
- name: Machine Learning
  slug: machine-learning
seo_title: Comment établir la confiance dans les prédictions de votre modèle de Machine
  Learning avec LIME
seo_desc: 'By Siddhesh Jadhav

  This article is a step by step guide that''ll help you interpret your machine learning
  model''s predictions using LIME. Even when your model achieves close to 100% accuracy,
  there is always one question that runs in your mind: should...'
---

Par Siddhesh Jadhav

Cet article est un guide étape par étape qui vous aidera à interpréter les prédictions de votre modèle de machine learning en utilisant LIME. Même lorsque votre modèle atteint une précision proche de 100%, il y a toujours une question qui vous trotte dans la tête : devons-nous lui faire confiance ?

Imaginez une situation dans un cabinet médical – un médecin ferait-il confiance à un ordinateur s'il affichait simplement un diagnostic sans donner de raison valable derrière celui-ci ?

Tout modèle qui ne parvient pas à expliquer la raison derrière sa sortie est considéré comme une boîte noire. Et faire confiance à un tel modèle n'est pas la bonne approche.

Supposons que nous ayons un modèle qui prédit si un animal est un chien ou un chat et qui a une précision de 100%. Mais que se passe-t-il s'il fait cette prédiction en fonction de l'arrière-plan de l'image ? Feriez-vous confiance à ce modèle ?

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-50.png)

Comme vous pouvez le voir sur la figure ci-dessus, la couleur verte représente les caractéristiques qu'il a prises pour identifier l'image comme un chat, et le rouge indique les caractéristiques qu'il a prises pour la représenter comme un chien.

Si notre modèle fournit une raison valable pour sa prédiction, cela renforce notre confiance dans ce modèle. De même, pour la situation du médecin, si le modèle peut indiquer quelles caractéristiques étaient importantes dans sa prédiction et à quels symptômes il a donné plus de poids, il est plus facile pour le médecin de faire confiance à ce modèle.

Mais est-ce aussi simple d'interpréter n'importe quel modèle ? Heureusement, oui. Marco Tulio Ribeiro, Sameer Singh et Carlos Guestrin ont publié un article intitulé "Why Should I Trust You?": Explaining the Predictions of Any Classifier en 2016.

Dans cet article, ils ont proposé leur technique LIME. L'approche de base de cette technique était d'interpréter facilement n'importe quel modèle en l'apprenant localement autour de sa prédiction.

Ils ont écrit cet article pour comprendre les explications derrière les prédictions de n'importe quel modèle. Ainsi, chaque fois que vous devez choisir un modèle, vous pouvez utiliser les informations de LIME.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-51.png)
_Explication des prédictions individuelles en utilisant LIME [source](https://arxiv.org/pdf/1602.04938.pdf)_

Dans le diagramme ci-dessus, le modèle prédit qu'un patient a la grippe, et LIME met en évidence les symptômes dans l'historique du patient qui ont conduit à la prédiction.

Les éternuements et les maux de tête contribuent à la prédiction de la "grippe", tandis que "pas de fatigue" est une preuve contre celle-ci. Avec ces informations, un médecin peut prendre une décision éclairée sur le fait de faire confiance ou non à la prédiction du modèle.

### Alors, qu'est-ce que LIME exactement ?

> _LIME est agnostique aux modèles, ce qui signifie qu'il peut être appliqué à n'importe quel modèle de machine learning. Le but de LIME est d'identifier un modèle interprétable sur la représentation interprétable qui est localement fidèle au classificateur._
>
> _-_ Définition du papier officiel ([lien](https://arxiv.org/pdf/1602.04938.pdf))

Pour comprendre cela, nous devons comprendre la signification de l'acronyme LIME.

**Local** : Fait référence à la manière dont nous obtenons ces explications. LIME approxime le modèle de boîte noire localement dans le voisinage des prédictions.

**Interprétable** : Les explications fournies par LIME sont suffisamment simples pour que les humains les comprennent.

**Agnostique aux modèles** : LIME traite le modèle comme une boîte noire, et donc il fonctionne pour n'importe quel modèle.

**Explications** : Les justifications données pour les actions effectuées par le modèle.

LIME fournit une interprétabilité locale du modèle. Il modifie un seul échantillon de données en ajustant les valeurs des caractéristiques et en observant l'impact résultant sur la sortie.

Avec LIME, nous pouvons expliquer pourquoi le `RandomForestClassifier` pense ce qu'il fait avant de donner une prédiction.

## Regardons un peu de code

Nous commencerons par utiliser le modèle `RandomForestClassifier` pour travailler sur le dataset "A-t-il plu à Seattle". Les données sont disponibles [ici](https://github.com/Sid11/Lime).

Tout d'abord, nous importerons nos bibliothèques de base :

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

Pour éviter les avertissements futurs dans notre code, nous ajouterons ceci au début de notre script :

```python
import warnings
warnings.filterwarnings('ignore')
```

Nous importons ensuite quelques bibliothèques sklearn pour diviser le dataset et pour définir les métriques. Le `RandomForestClassifier` sera également importé de la même bibliothèque.

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
```

Puisque nous avons toutes nos bibliothèques requises, nous allons lire nos données :

```python
df = pd.read_csv('seattleWeather_1948-2017.csv')
df.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-52.png)

Les données se composent de 4 colonnes de caractéristiques et d'une colonne cible, c'est-à-dire RAIN. Notre tâche est de prédire s'il a plu à Seattle.

```python
df.shape
```

(25551, 5)

Nos données se composent de 25 551 lignes, ce qui est suffisant pour que notre modèle s'entraîne.

Nous vérifierons s'il y a des valeurs manquantes :

```python
df.isnull().sum()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-53.png)

Puisque notre principal objectif est d'interpréter la prédiction du modèle, nous supprimerons directement les lignes avec des valeurs manquantes. Pour simplifier, nous supprimerons également la colonne DATE.

```python
df.dropna(inplace=True)
df.pop('DATE')
```

Nous allons maintenant encoder notre colonne cible :

```python
df.RAIN.replace({True:1,False:0},inplace=True)
df.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-54.png)

Voici à quoi ressemblent nos données à la fin.

```python
target = df.pop('RAIN')
x_train , x_test , y_train , y_test = train_test_split(df, target, train_size=0.75)
```

Nous avons maintenant divisé les données en ensembles d'entraînement et de test, avec l'entraînement égal à 75% des données originales.

Nous allons maintenant créer notre modèle avec les paramètres par défaut :

```python
rfc = RandomForestClassifier()
```

Et ajuster le modèle aux échantillons d'entraînement :

```python
rfc.fit(x_train,y_train)
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-55.png)

```python
accuracy_score(y_test,rfc.predict(x_test))
```

1.0

Le modèle a atteint une précision de 100%. Mais maintenant, interprétons le modèle pour pouvoir lui faire confiance.

## LIME

Tout d'abord, nous devons discuter un peu de théorie avant de continuer.

LIME crée de nouvelles données qui incluent des échantillons permutés et leurs prédictions respectives.

Sur cela, LIME entraîne un modèle local qui est pondéré par la proximité des instances d'échantillon. Ce modèle peut être n'importe quel modèle de base, à savoir un arbre de décision.

Ce modèle doit avoir des prédictions locales similaires à celles du modèle existant. Cette précision est appelée fidélité locale.

```python
import lime
from lime import lime_tabular
```

Maintenant que nous avons importé les packages requis, nous devons effectuer notre interprétation.

Voici la recette pour entraîner des modèles de substitution locaux :

1. Sélectionnez le modèle pour lequel vous voulez obtenir l'explication de sa prédiction
2. Entraînez ce modèle et obtenez sa prédiction pour les valeurs de test
3. Pour LIME, nous pondérons les nouveaux échantillons en fonction de leur proximité avec le modèle
4. Créez un modèle local sur le dataset
5. Enfin, nous expliquons la prédiction en interprétant le modèle local

Définissez un modèle `LimeTableExplainer`. Les paramètres de ce modèle sont l'échantillon d'entraînement, les noms des caractéristiques et les noms des classes :

```python
explainer = lime_tabular.LimeTabularExplainer(x_train.values,feature_names=['PRCP','TMAX','TMIN'],class_names=['False','True'],discretize_continuous=True)
```

Nous devons passer les échantillons d'entraînement, les noms des colonnes d'entraînement et les noms des classes cibles attendus.

Nous appelons ensuite la fonction `explain_instance()` de l'explicateur que nous avons créé.

Nous utiliserons les paramètres suivants de cette fonction : échantillon de test, fonction de prédiction du modèle, nombre de caractéristiques et les meilleures étiquettes à considérer :

```python
i = np.random.randint(0,x_test.shape[0])
exp = explainer.explain_instance(x_test.iloc[i],rfc.predict_proba,num_features=x_train.shape[1],top_labels=None)
```

Pour afficher l'explication dans le notebook, le code suivant est requis.

```python
exp.show_in_notebook()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-56.png)

Décryptons la sortie.

Le diagramme en haut à gauche indique la sortie prédite avec la probabilité.

La sortie du modèle est **False** avec une probabilité de 100%.

Le diagramme en haut à droite indique les conditions requises pour chaque catégorie avec leurs poids.

Puisque la condition pour les variables PRCP pour prédire la cible comme **False** est PRCP ≤ 0.00 et elle a un poids de 0.96.

Le diagramme en bas à droite indique nos valeurs de test. Puisque les valeurs de PRCP satisfont une condition **False**, vous pouvez voir la couleur bleue comme fond pour cela.

Pour afficher l'explication sous forme de graphique :

```python
fig = exp.as_pyplot_figure()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-57.png)

Ici, vous pouvez voir le poids pour chaque caractéristique avec leur classe prédite (représentée par la couleur). Ils représentent les poids locaux attribués à chaque caractéristique. La couleur rouge représente une cible **False** tandis que la couleur verte représente une cible **True**.

Il est maintenant facile d'interpréter le modèle en voyant le poids donné à chaque caractéristique ainsi que la condition pour chaque valeur de test tombant sous une classe spécifique.

Les valeurs de `PRCP` et `TMAX` indiquent que la cible prédite devrait être **False** tandis que la valeur de `TMIN` indique une cible **True**.

LIME n'est pas seulement utilisé pour la classification binaire des données tabulaires, mais aussi pour les cas multi-classes, les images et le texte.

Le code peut être trouvé dans mon dépôt GitHub : [https://github.com/Sid11/Lime](https://github.com/Sid11/Lime)

Et voici un lien vers le dépôt GitHub officiel de LIME : [https://github.com/marcotcr/lime](https://github.com/marcotcr/lime)

Si vous avez des questions, n'hésitez pas à me contacter. J'espère que vous avez aimé l'article !