---
title: Tutoriel m2cgen – Comment transformer des modèles de Machine Learning en code
  natif sans dépendances
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-25T17:20:30.000Z'
originalURL: https://freecodecamp.org/news/transform-machine-learning-models-into-native-code-with-zero-dependencies
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/dandelion-2817950_1920.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Tutoriel m2cgen – Comment transformer des modèles de Machine Learning en
  code natif sans dépendances
seo_desc: "By Davis David\nMost trained machine learning models are saved as pickle\
  \ files. This file type is the standard way of serializing and de-serializing objects\
  \ in Python. \nIn order to make predictions, you need to load the saved trained\
  \ model and then pe..."
---

Par Davis David

La plupart des modèles de machine learning entraînés sont sauvegardés sous forme de [fichiers pickle](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/). Ce type de fichier est la méthode standard de sérialisation et de désérialisation d'objets en Python. 

Pour faire des prédictions, vous devez charger le modèle entraîné sauvegardé, puis effectuer des prédictions à partir des entrées fournies. 

Dans cet article, vous apprendrez à utiliser la bibliothèque Python **m2cgen** pour convertir le modèle de machine learning entraîné en code natif (par exemple Python, PHP ou JavaScript) sans dépendances. Ensuite, vous ferez des prédictions basées sur celui-ci.

## Qu'est-ce que la bibliothèque Python m2cgen ?

m2cgen (Model 2 Code Generator) est une bibliothèque Python simple qui convertit un modèle de machine learning entraîné dans différents langages de programmation. 

Par exemple, vous pouvez entraîner votre modèle de machine learning à partir de la bibliothèque Scikit-learn, puis le convertir dans le langage de programmation de votre choix.

Cette bibliothèque est très utile si vous souhaitez déployer des modèles dans des environnements où vous ne pouvez pas installer votre stack Python pour supporter vos prédictions de modèle.

### Langages supportés par la bibliothèque m2cgen 

[M2cgen](https://github.com/BayesWitnesses/m2cgen) supporte 14 langages de programmation différents :

* C
* C#
* Dart
* F#
* Go
* Haskell
* Java
* JavaScript
* PHP
* PowerShell
* Python
* R
* Ruby
* Visual Basic (compatible VBA)

### Modèles supportés par la bibliothèque m2cgen

La bibliothèque supporte différents modèles de régression et de classification de Scikit-learn, ainsi que différents frameworks de gradient boosting tels que XGBoost et LightGBM (Light Gradient Boosting Machine). 

Si vous souhaitez en savoir plus sur les autres modèles supportés, consultez cette page : [https://github.com/BayesWitnesses/m2cgen#supported-models](https://github.com/BayesWitnesses/m2cgen#supported-models).

## Comment installer la bibliothèque Python m2cgen

Pour installer m2cgen, exécutez la commande suivante dans votre terminal :

```terminal
pip install m2cgen
```

Notez que m2cgen est supporté par les versions Python >= **3.6**.

## Comment utiliser la bibliothèque Python m2cgen

Dans les exemples suivants, nous utiliserons le jeu de données de prêts pour créer un modèle simple de machine learning en utilisant un algorithme de régression logistique. L'algorithme sera capable de prédire si un client est éligible pour un montant de prêt. 

Ensuite, nous convertirons le modèle entraîné en Python, PHP et JavaScript en utilisant la bibliothèque m2cgen. Vous pouvez télécharger le jeu de données [ici](https://github.com/Davisy/Convert-Trained-ML-Models-To-Native-Code/tree/main/data).

Commençons ! 🚀

Importez les packages importants suivants pour ce cas d'utilisation :

```python
import pandas as pd
import numpy as np                     
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
import m2cgen as m2c 
import warnings                        # Pour ignorer les avertissements
warnings.filterwarnings("ignore")
```

Chargez le jeu de données de prêts en utilisant Pandas avec cette commande :

```python
data = pd.read_csv("data/loans_data.csv")
```

Affichez ensuite une liste de toutes les colonnes du jeu de données :

```python
list(data.columns)
```

Voici les colonnes qui nous intéressent :

Loan_ID  
Gender  
Married  
Dependents  
Education  
Self_Employed  
ApplicantIncome  
CoapplicantIncome  
LoanAmount  
Loan_Amount_Term  
Credit_History  
Property_Area  
Loan_Status

Nous avons 12 caractéristiques indépendantes et une cible (**Loan_Status**). Vous pouvez lire la description de chaque caractéristique ici :

![Image](https://www.freecodecamp.org/news/content/images/2021/01/1_H192S1SuTPt0AVdxNwHdQA.png)
_Descriptions des colonnes_

Voici les 5 premières lignes du jeu de données :

```python
# afficher les 5 premières lignes du jeu de données
data.head() 
```

![Image](https://www.freecodecamp.org/news/content/images/2021/01/5-rows.PNG)
_5 premières lignes_

Comme vous pouvez le voir, le jeu de données contient des données manquantes et des caractéristiques catégorielles qui doivent être converties en valeurs numériques. Voici une fonction Python simple qui nous aidera à gérer les données manquantes et l'ingénierie des caractéristiques. Ensuite, elle retournera les caractéristiques traitées et la cible.

```python
# prétraitement du jeu de données.

def preprocessing(data):

    # remplacer par des valeurs numériques
    data['Dependents'].replace('3+', 3,inplace=True)
    data['Loan_Status'].replace('N', 0,inplace=True)
    data['Loan_Status'].replace('Y', 1,inplace=True)

    # gérer les données manquantes 
    data['Gender'].fillna(data['Gender'].mode()[0], inplace=True)
    data['Married'].fillna(data['Married'].mode()[0], inplace=True)
    data['Dependents'].fillna(data['Dependents'].mode()[0], inplace=True)
    data['Self_Employed'].fillna(data['Self_Employed'].mode()[0], inplace=True)
    data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True)
    data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0], inplace=True)
    data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)

    # supprimer la colonne ID
    data = data.drop('Loan_ID',axis=1)
    
    # diviser les caractéristiques et la cible 
    X = data.drop('Loan_Status',axis=1)
    y = data.Loan_Status.values

    # mettre à l'échelle les caractéristiques 
    X  = pd.get_dummies(X,columns=["Gender","Married","Education","Self_Employed","Property_Area"])
    X = StandardScaler().fit_transform(X)
    

    return X,y 
```

Prétraitons le jeu de données de prêts. Cela retournera les caractéristiques traitées et la cible.

```python
X,y = preprocessing(data) 
```

Nous divisons ensuite les données traitées en ensembles d'entraînement et de test en utilisant la fonction **`train_test_split`** de Scikit-learn.

```python
# diviser en ensemble d'entraînement et de test 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
```

Maintenant, nous créons et entraînons le modèle de régression logistique sur notre ensemble d'entraînement.

```python
# créer et entraîner le classificateur 

classifier = LogisticRegression()

classifier.fit(X_train,y_train)
```

## Comment convertir le modèle entraîné en code Python

La bibliothèque m2cgen fournit des méthodes pour convertir le modèle entraîné dans l'un des langages supportés mentionnés ci-dessus. Dans cet exemple, nous convertirons le modèle entraîné en Python en utilisant la méthode **`export_to_python()`** de m2cgen.

```python
# convertir le modèle en code Python pur  
model_to_python = m2c.export_to_python(classifier)  
```

Voici le modèle entraîné représenté en code Python :

```python
# code Python pur 

def score(input):
    
    return (((((((((((((((((0.7929123964945446) + ((input[0]) * (0.07801862594632314))) + ((input[1]) * (-0.014853900985478468))) + ((input[2]) * (-0.15783041201914427))) + ((input[3]) * (-0.05222073553791883))) + ((input[4]) * (-0.0787403404504791))) + ((input[5]) * (1.3714807410150505))) + ((input[6]) * (0.015077765348160292))) + ((input[7]) * (-0.015077765348160353))) + ((input[8]) * (-0.12161041350915254))) + ((input[9]) * (0.12161041350915253))) + ((input[10]) * (0.09387440269562626))) + ((input[11]) * (-0.09387440269562626))) + ((input[12]) * (-0.0047109053878701835))) + ((input[13]) * (0.004710905387870008))) + ((input[14]) * (-0.14569247529698154))) + ((input[15]) * (0.19858601990225683))) + ((input[16]) * (-0.06417592734444703))
```

Le code de la fonction Python généré recevra des données d'entrée et effectuera ses prédictions. Testons maintenant le code Python généré. 

Nous allons d'abord faire des prédictions à partir du modèle entraîné réel. Voici les données de test échantillon que nous utiliserons à partir de l'ensemble de test :

```python
test_data = X_test[6]
print(test_data)
```

array([ 1.24474546,  1.9817189 , -0.55448733,  3.02536229,  0.2732313 , 0.41173269, -0.47234264,  0.47234264, -0.72881553,  0.72881553, 0.52836225, -0.52836225, -2.54711697,  2.54711697,  1.55889948, -0.7820157 , -0.70020801])

Maintenant, nous faisons des prédictions avec le modèle entraîné réel.

```python
pred = classifier.predict(test_data.reshape(1,-1))  
print("résultat de la prédiction : {}".format(pred))
```

résultat de la prédiction : [1]

La prédiction du modèle est **1**, ce qui signifie que le client est éligible pour le montant du prêt.

Nous utiliserons les mêmes données de test pour effectuer des prédictions dans le code Python pur généré et évaluer si cela donnera la même prédiction.

```python
# test de prédiction en code Python pur 
input = [ 1.24474546,  1.9817189 , -0.55448733,  3.02536229,  0.2732313 ,
        0.41173269, -0.47234264,  0.47234264, -0.72881553,  0.72881553,
        0.52836225, -0.52836225, -2.54711697,  2.54711697,  1.55889948,
       -0.7820157 , -0.70020801]

pred = score(input) 
print("résultat de la prédiction : {}".format(int(pred)))
```

résultat de la prédiction : 1

Le code Python pur fournit également les mêmes résultats de prédiction.

## Comment convertir le modèle entraîné en code PHP

Nous utiliserons la méthode **`export_to_php()`** de m2cgen pour convertir le modèle entraîné en code PHP pur.

```python
# convertir le modèle en code PHP pur  
model_to_php = m2c.export_to_php(classifier)  
```

Voici le modèle entraîné représenté en code PHP :

```php
function score(array $input)
{
    return (((((((((((((((((0.8166973302490392) + (($input[0]) * (0.035269518507829584))) + (($input[1]) * (0.05203333118549156))) + (($input[2]) * (-0.13217178253938103))) + (($input[3]) * (-0.13136526173536608))) + (($input[4]) * (-0.024875019809902837))) + (($input[5]) * (1.2864103414352563))) + (($input[6]) * (-0.005259373701309709))) + (($input[7]) * (0.005259373701309715))) + (($input[8]) * (-0.11512289603368371))) + (($input[9]) * (0.11512289603368378))) + (($input[10]) * (0.06905305123713898))) + (($input[11]) * (-0.06905305123713898))) + (($input[12]) * (0.021080906307735767))) + (($input[13]) * (-0.02108090630773594))) + (($input[14]) * (-0.14491490189610398))) + (($input[15]) * (0.2189862115713242))) + (($input[16]) * (-0.08599736364921017));
}
```

Nous utiliserons les mêmes données de test pour effectuer des prédictions dans le code PHP pur généré et évaluer si cela nous donnera la même prédiction :

```php
# test de prédiction en code PHP pur
$input = [1.24474546, 1.9817189, -0.55448733, 3.02536229, 0.2732313,
    0.41173269, -0.47234264, 0.47234264, -0.72881553, 0.72881553,
    0.52836225, -0.52836225, -2.54711697, 2.54711697, 1.55889948,
    -0.7820157, -0.70020801];

// effectuer la prédiction avec le code PHP pur
$pred = score($input);


echo "Résultat de la prédiction : ". round($pred);
```

Résultat de la prédiction : 1

Le code PHP pur fournit également les mêmes résultats de prédiction.

## Comment convertir le modèle entraîné en code JavaScript

Dans notre dernier exemple, nous utiliserons la méthode **`export_to_javascript()`** de m2cgen pour convertir le modèle entraîné en code JavaScript pur.

```python
# convertir le modèle en code JavaScript pur  
model_to_javascript = m2c.export_to_javascript(classifier)  
```

Voici le modèle entraîné représenté en code JavaScript :

```javascript
function score(input)
{
    return (((((((((((((((((0.8166973302490392) + ((input[0]) * (0.035269518507829584))) + ((input[1]) * (0.05203333118549156))) + ((input[2]) * (-0.13217178253938103))) + ((input[3]) * (-0.13136526173536608))) + ((input[4]) * (-0.024875019809902837))) + ((input[5]) * (1.2864103414352563))) + ((input[6]) * (-0.005259373701309709))) + ((input[7]) * (0.005259373701309715))) + ((input[8]) * (-0.11512289603368371))) + ((input[9]) * (0.11512289603368378))) + ((input[10]) * (0.06905305123713898))) + ((input[11]) * (-0.06905305123713898))) + ((input[12]) * (0.021080906307735767))) + ((input[13]) * (-0.02108090630773594))) + ((input[14]) * (-0.14491490189610398))) + ((input[15]) * (0.2189862115713242))) + ((input[16]) * (-0.08599736364921017));
}
```

Nous utiliserons les mêmes données de test pour effectuer des prédictions dans le code JavaScript pur généré et évaluer si cela nous donnera la même prédiction.

```javascript
// effectuer la prédiction avec le code JavaScript pur
let input =  [1.24474546, 1.9817189, -0.55448733, 3.02536229, 0.2732313,
    0.41173269, -0.47234264, 0.47234264, -0.72881553, 0.72881553,
    0.52836225, -0.52836225, -2.54711697, 2.54711697, 1.55889948,
    -0.7820157, -0.70020801];

let pred = score(input);

console.log("Résultat de la prédiction :",Math.round(pred));
```

"Résultat de la prédiction :", 1

Le code JavaScript pur fournit également les mêmes résultats de prédiction.

## Conclusion

Parfois, le code natif généré par la bibliothèque m2cgen peut fournir des résultats différents par rapport au modèle original de machine learning entraîné en Python. Voici une brève explication des développeurs de la bibliothèque :

> "Certains modèles forcent les données d'entrée à être d'un type particulier lors de la phase de prédiction dans leurs bibliothèques Python natives. Actuellement, m2cgen fonctionne uniquement avec le type de données `float64` (`double`). Vous pouvez essayer de convertir vos données d'entrée vers un autre type manuellement et vérifier les résultats à nouveau. De plus, certaines petites différences peuvent survenir en raison de l'implémentation spécifique de l'arithmétique à virgule flottante dans le langage cible." ([**Source : Dépôt Github**](https://github.com/BayesWitnesses/m2cgen))

Dans les exemples mentionnés ci-dessus, j'utilise **`int()`** pour **Python**, **`round()`** pour **PHP** et **`Math.round()`** pour **JavaScript** pour convertir les résultats de prédiction du type de données _float_ vers le type de données _integer_.

Félicitations, vous êtes arrivé à la fin de cet article !

Vous pouvez télécharger le jeu de données, le notebook et les fichiers de script utilisés dans cet article ici : [https://github.com/Davisy/Convert-Trained-ML-Models-To-Native-Code](https://github.com/Davisy/Convert-Trained-ML-Models-To-Native-Code)

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine ! Vous pouvez également me joindre sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid).