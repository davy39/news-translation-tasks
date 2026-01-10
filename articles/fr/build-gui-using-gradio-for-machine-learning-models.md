---
title: Comment créer une GUI avec Gradio pour les modèles de Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-27T21:00:00.000Z'
originalURL: https://freecodecamp.org/news/build-gui-using-gradio-for-machine-learning-models
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/gradio-image-2.png
tags:
- name: deployment
  slug: deployment
- name: Machine Learning
  slug: machine-learning
- name: scikit learn
  slug: scikit-learn
seo_title: Comment créer une GUI avec Gradio pour les modèles de Machine Learning
seo_desc: "By Edem Gold\nIf you have ever built a Machine Learning model, you've probably\
  \ thought \"well this was cool, but how will other people be able to see how cool\
  \ it is?\" \nModel deployment is a part of Machine Learning which isn't talked about\
  \ as much as i..."
---

Par Edem Gold

Si vous avez déjà construit un modèle de Machine Learning, vous vous êtes probablement dit "c'était bien, mais comment les autres pourront-ils voir à quel point c'est cool ?" 

Le déploiement de modèles est une partie du Machine Learning dont on ne parle pas autant qu'il le faudrait.

Dans cet article, je vais donc vous présenter un nouvel outil qui vous aidera à générer une application web pour votre modèle de Machine Learning, que vous pourrez ensuite partager avec d'autres développeurs pour qu'ils puissent l'essayer.

Je vais construire un simple modèle de réseau de neurones en utilisant scikit-learn et je vais créer une GUI pour le modèle en utilisant Gradio (c'est le nouvel outil cool dont je parlais).

Commençons.

> Nous ne pouvons pas résoudre nos problèmes avec la même pensée que nous avons utilisée pour les créer - Albert Einstein

# Qu'est-ce que Gradio ?

![gradio cover.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1632054788128/NVI4Jgdrd.png?auto=compress,format&format=webp)
_****crédits image : [gradio](https://gradio.app/)****_

Selon le [site web de Gradio](https://gradio.app/),

> Gradio vous permet de créer rapidement des composants d'interface utilisateur personnalisables autour de vos modèles TensorFlow ou PyTorch, ou même des fonctions Python arbitraires.

Bon, ce n'est pas très informatif, n'est-ce pas ? 😅.

Si vous avez déjà utilisé une bibliothèque GUI Python comme Tkinter, alors Gradio est similaire.

Gradio est une bibliothèque GUI qui vous permet de créer des composants GUI personnalisables pour votre modèle de Machine Learning.

Maintenant que nous comprenons ce qu'est Gradio, passons au projet.

## **Prérequis**

Pour suivre ce tutoriel avec succès, vous devez avoir Python installé.

# Commençons à construire

Vous pouvez consulter le dépôt GitHub du projet [ici](https://github.com/EdemGold/gradio_project). Je vais maintenant vous guider à travers le projet étape par étape.

### Installer les packages requis

Installons les packages requis :

```
pip install sklearn

```

```
pip install pandas

```

```
pip install numpy

```

```
pip install gradio

```

### Obtenir nos données

Nos données seront au format .CSV. Vous pouvez obtenir les données en cliquant [ici](https://raw.githubusercontent.com/EdemGold/gradio_project/main/diabetes.csv).

### Importer les packages

Nous allons importer les packages requis comme ceci :

```
import numpy as np

import pandas as pd

import gradio as gr

```

Ensuite, nous allons filtrer les avertissements pour ne pas les voir.

```
import warnings

warnings.filterwarnings('ignore')

```

### Importer les données

Ensuite, nous allons importer nos données :

```
data = pd.read_csv('diabetes.csv')

```

Maintenant, voyons un petit aperçu de notre ensemble de données avec cette commande :

```
data.head()

```

Voyons les colonnes de caractéristiques dans notre ensemble de données :

```
print(data.columns)

```

### Obtenir nos variables

Ensuite, nous obtenons nos variables X et Y, alors tapez ces commandes :

```
x = data.drop(['Outcome'], axis=1)

y = data['Outcome']

```

### Diviser les données

Maintenant, nous allons diviser nos données en utilisant la fonction intégrée _train_test_split_ de scikit-learn.

```
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y)

```

### Mettre à l'échelle nos données

Ensuite, nous allons mettre à l'échelle nos données en utilisant l'objet _StandardScaler_ intégré de scikit-learn.

```
from sklearn.preprocessing import StandardScaler

#instancier l'objet StandardScaler
scaler = StandardScaler()

#mettre à l'échelle les données
x_train_scaled = scaler.fit_transform(x_train)

x_test_scaled = scaler.fit_transform(x_test)

```

Dans le code ci-dessus, nous avons mis à l'échelle nos données en utilisant l'objet StandardScaler mis à notre disposition par scikit-learn. Pour en savoir plus sur la mise à l'échelle et pourquoi nous le faisons, cliquez [ici](https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/).

### Instancier et entraîner le modèle

Dans cette section, nous allons créer et entraîner notre modèle. Le modèle que nous allons utiliser sera un classificateur Multi-Layer Perceptron, un réseau de neurones intégré dans scikit-learn.

```
#importation de l'objet modèle
from sklearn.neural_network import MLPClassifier
model =  MLPClassifier(max_iter=1000,  alpha=1)

#entraînement du modèle sur les données d'entraînement
model.fit(x_train_scaled, y_train)

#obtention des performances du modèle sur les données de test
print("précision :", model.score(x_test_scaled, y_test))

```

### Créer la fonction pour Gradio

Maintenant vient la partie amusante. Ici, nous allons créer une fonction qui prendra les caractéristiques de l'ensemble de données sur lequel notre modèle a été entraîné et les passera sous forme de tableau à notre modèle pour prédiction. Ensuite, nous allons construire notre application web Gradio basée sur cette fonction.

Pour comprendre pourquoi nous devons écrire une fonction, vous devez d'abord comprendre que Gradio construit des composants GUI pour notre modèle de Machine Learning basé sur la fonction. La fonction fournit un moyen pour Gradio d'obtenir des entrées de la part des utilisateurs et de les transmettre au modèle ML, qui les traitera puis les renverra à Gradio qui transmettra ensuite le résultat.

Écrivons un peu de code...

Tout d'abord, nous allons obtenir les colonnes de caractéristiques que nous allons ensuite passer à notre fonction.

```
#obtention de nos colonnes

print(data.columns)

```

Maintenant, nous allons créer notre fonction comme ceci :

```
def diabetes(Pregnancies, Glucose, Blood_Pressure, SkinThickness, Insulin, BMI, Diabetes_Pedigree, Age):
#transformation des arguments en un tableau numpy  

 x = np.array([Pregnancies,Glucose,Blood_Pressure,SkinThickness,Insulin,BMI,Diabetes_Pedigree,Age])

  prediction = model.predict(x.reshape(1, -1))

  return prediction

```

Dans le code ci-dessus, nous avons passé les colonnes de caractéristiques de nos données en tant qu'arguments dans une fonction que nous avons nommée _diabetes_. Ensuite, nous avons transformé les arguments en un tableau NumPy que nous avons ensuite passé à notre modèle pour prédiction. Enfin, nous avons retourné le résultat prédit de notre modèle.

### Créer notre interface Gradio

Maintenant, nous allons créer notre interface d'application web en utilisant Gradio :

```
outputs = gr.outputs.Textbox()

app = gr.Interface(fn=diabetes, inputs=['number','number','number','number','number','number','number','number'], outputs=outputs,description="Ceci est un modèle de diabète")

```

La première chose que nous avons faite ci-dessus a été de créer une variable nommée outputs qui contient le composant GUI pour le résultat de notre modèle. Le résultat de la prédiction de notre modèle sera affiché dans une zone de texte.

Ensuite, nous avons instancié l'objet interface Gradio et passé notre fonction _diabetes_ précédente. Ensuite, nous avons généré notre composant GUI d'entrées et dit à Gradio de s'attendre à 8 entrées sous forme de nombres.

Les entrées représentent les colonnes de caractéristiques présentes dans notre ensemble de données – les mêmes 8 noms de colonnes de caractéristiques que nous avons passés dans notre fonction _diabetes_.

Ensuite, nous avons passé notre variable de sortie précédente dans le paramètre outputs présent dans l'objet.

Enfin, nous avons passé la description de notre application web dans le paramètre description.

### Lancer l'application web Gradio

Maintenant, nous allons lancer notre application web Gradio.

```
app.launch()

```

**NOTE :** Si vous lancez l'application Gradio en tant que script à partir de la ligne de commande, vous recevrez un lien d'hôte local que vous copierez et collerez dans votre navigateur pour voir votre application web.

Si vous lancez l'application à partir d'un notebook Jupyter, vous verrez un aperçu en direct de l'application lorsque vous exécuterez la cellule (et vous recevrez également un lien).

### Héberger et partager votre application web

Si vous souhaitez partager votre application web, tout ce que vous avez à faire est de mettre `share=True` en tant que paramètre dans votre objet de lancement.

```
#Pour fournir un lien partageable
app.launch(share=True)

```

Vous obtiendrez alors un lien avec une extension .gradio. Mais ce lien partageable ne dure que 24 heures et ne durera que si votre système est en cours d'exécution. Parce que Gradio héberge simplement l'application web sur votre système.

En termes simples, pour que votre lien fonctionne, votre système doit être allumé. Cela est dû au fait que Gradio utilise votre système pour héberger l'application web, donc une fois votre système éteint, la connexion au serveur est rompue et vous obtenez une erreur 500 😅.

Heureusement pour nous, Gradio propose également un moyen d'héberger votre modèle de manière permanente. Mais le service est basé sur un abonnement, vous devez donc payer 7 $ par mois pour y accéder. L'hébergement permanent est hors de la portée de cet article (en partie parce que l'auteur est fauché 😅). Mais si cela vous intéresse, cliquez [ici](https://www.gradio.app/introducing-hosted).

## **Ressources importantes**

* [Site web de Gradio](https://gradio.app/)
* [Documentation de Gradio](https://gradio.app/docs)
* [Gradio sur GitHub](https://github.com/gradio-app/gradio)

## **Résumé**

La bibliothèque Gradio est vraiment cool et elle aide à résoudre un énorme problème qui afflige la communauté du Machine Learning – le déploiement de modèles.

90 % des modèles de Machine Learning construits ne sont pas déployés, et Gradio travaille à résoudre ce problème.

Cela sert également de moyen pour les débutants et les experts de montrer leurs modèles et de les tester en conditions réelles.

Vous ne pouvez pas vous tromper avec la bibliothèque Gradio. Essayez-la.

[Source de l'image de couverture](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/tv8zrejyehjshagvxgt7).