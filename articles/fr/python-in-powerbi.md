---
title: Comment utiliser Python dans Power BI
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-23T16:27:48.000Z'
originalURL: https://freecodecamp.org/news/python-in-powerbi
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Python-Power-BI-1.png
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: Comment utiliser Python dans Power BI
seo_desc: "By Yannawut Kimnaruk\nMicrosoft Power BI is a business analytics tool which\
  \ allows users to gain insight from their data. \nYou can easily create an interactive\
  \ dashboard by just dragging and dropping data columns into the visualization plane.\n\
  In this ..."
---

Par Yannawut Kimnaruk

Microsoft Power BI est un outil d'analyse commerciale qui permet aux utilisateurs de tirer des informations de leurs données. 

Vous pouvez facilement créer un tableau de bord interactif en faisant simplement glisser et déposer des colonnes de données dans le plan de visualisation.

Dans cet article, je vais vous montrer comment utiliser Python pour vous aider à tirer parti des capacités de Power BI.

## Pourquoi utiliser Python et Power BI ensemble ?

De nombreux analystes de données et scientifiques des données sont déjà familiers avec la programmation Python. Ils peuvent donc facilement adopter Power BI pour l'utiliser dans le processus d'EDA (Exploratory Data Analysis). Les analystes de données peuvent également raconter une histoire à partir des données avec un tableau de bord créé à partir de Power BI.

J'aime Power BI parce qu'il est facile d'approfondir les données et de trouver des informations. Lorsque je filtre des fonctionnalités/colonnes dans une visualisation, cela affecte également les autres visualisations. Ensuite, je peux me concentrer sur une catégorie avant de passer à d'autres.

Microsoft Power BI prend déjà en charge deux langages différents : le langage M et DAX (Data Analysis Expression). Mais il est parfois plus pratique d'utiliser Python pour le processus de préparation des données. Cela est dû au fait qu'il vous donne accès à diverses bibliothèques Python, un ensemble de fonctions utiles qui éliminent le besoin d'écrire du code à partir de zéro. 

En implémentant Python dans Power BI, vous pouvez bénéficier à la fois de Python et de Power BI. Vous pouvez facilement effectuer des EDA et créer des présentations en utilisant le tableau de bord interactif de Power BI. Vous avez également la flexibilité d'écrire du code Python pour le tableau de bord.

### Ce que nous allons couvrir :

* Comment installer Python
* Comment configurer Python dans Power BI
* Comment utiliser Python pour obtenir des données
* Comment utiliser Python pour transformer des données
* Comment utiliser Python pour visualiser des données

## Comment installer Python 📅

Avant d'utiliser Python dans Power BI, vous devez installer Python. Je recommande d'installer Anaconda car c'est un outil utile pour gérer les bibliothèques et les environnements Python.

### Étape 1 : Installer Anaconda

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-59.png)

Rendez-vous sur [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution) et téléchargez et installez Anaconda sur votre ordinateur.

### Étape 2 : Ouvrir l'invite Anaconda

Recherchez l'invite Anaconda et cliquez pour ouvrir.

![Image](https://miro.medium.com/max/1308/1*1s9Qobi-Nwj5FHxDwbSV7A.png)

Vous verrez une fenêtre noire apparaître. Assurez-vous que la barre de titre est Anaconda Prompt.

![Image](https://miro.medium.com/max/1400/1*9di4tqkz_q4-o0TSuZspCQ.png)

### Étape 3 : Créer un environnement Python 3.6

Power BI peut avoir des problèmes lorsqu'il travaille avec des versions élevées de Python (au moment de la rédaction de cet article, la dernière version de Python est 3.9). Pour éviter les problèmes techniques, j'ai créé un nouvel environnement Python 3.6 et je n'ai eu aucun problème avec celui-ci.

Vous pouvez rétrograder votre version de Python directement, mais cela n'est pas recommandé car cela peut affecter d'autres projets. Vous pouvez considérer l'environnement Anaconda comme une boîte de travail contenant une collection spécifique de paquets Python. Lorsque vous travaillez dans cet environnement, cela n'affectera pas les autres projets.

Dans l'invite Anaconda, créez un nouvel environnement en tapant le code suivant 
(remplacez simplement **<env_name>** par le nom de votre environnement tel que python36) :

```
conda create --name <env_name> python=3.6
```

Ensuite, lorsque vous voyez Proceed ([y]/n)?, tapez y et Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-124.png)

Attendez qu'il ait fini de s'exécuter.

Vérifiez qu'un nouvel environnement a été créé avec succès en tapant cette commande :

```
conda env list
```

Vous verrez une liste des environnements Anaconda. Si vous voyez un nouvel environnement, vous êtes prêt à passer à l'étape suivante.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-126.png)

### Étape 4 : Installer des bibliothèques Python utiles

Avant d'installer des paquets Python, assurez-vous d'être dans l'environnement que vous venez de créer en tapant la commande suivante dans l'invite Anaconda :

```
conda activate <env_name>
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-60.png)

Ensuite, vous observerez le changement de nom d'environnement dans les parenthèses.

Vous pouvez installer des bibliothèques/paquets Python que vous allez utiliser dans Power BI en tapant la commande suivante (remplacez simplement **<package_name>** par le nom du paquet que vous souhaitez installer, tel que pandas, numpy, matplotlib, etc.) :

```
pip install <package_name>
```

## Comment configurer Python dans Power BI ⚙️ 

Après avoir terminé l'installation de Python, il est temps de passer à Power BI !

### Étape 1 : Installer Power BI 

Rendez-vous sur [https://www.microsoft.com/en-us/download/details.aspx?id=58494](https://www.microsoft.com/en-us/download/details.aspx?id=58494).  
Téléchargez et installez Power BI sur votre ordinateur.

Ouvrez ensuite Power BI.

### Étape 2 : Cliquez sur 'Fichier' dans le coin supérieur gauche.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-64.png)

### Étape 3 : Cliquez sur 'Options et paramètres'. Cliquez sur 'Options'.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-65.png)

### Étape 4 : Cliquez sur 'Script Python'

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-66.png)

### Étape 5 : Changer les répertoires et naviguer vers votre environnement Python

Changez le répertoire d'accueil Python détecté en "Autre" et parcourez votre environnement Python créé à l'étape précédente.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-67.png)

**Astuce** pour trouver le répertoire de l'environnement Python :

Ouvrez l'invite Anaconda et tapez le code ci-dessous :

```
conda env list
```

Vous verrez une liste des environnements Anaconda.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-127.png)

Copiez le chemin après le nom de l'environnement tel que C:\Users\yannawutk\.conda\envs\python36

Maintenant, vous êtes prêt à utiliser Python dans Power BI.

Vous pouvez utiliser Python de trois manières importantes : pour obtenir des données, transformer des données et visualiser des données.

Si vous souhaitez suivre le code dans cet article, vous pouvez [télécharger les données d'exemple à partir de ce jeu de données Kaggle](https://www.kaggle.com/datasets/datatattle/covid-19-nlp-text-classification/download).

## Comment utiliser Python pour obtenir des données 🧏 

Vous pouvez utiliser Python pour obtenir des données. Cela est utile pour le web scraping (obtenir des données à partir d'un site web) et pour extraire des données d'une API (Application Program Interface). Par exemple, si vous souhaitez collecter des données à partir de Twitter ou Trello. 

Ces méthodes d'acquisition de données ne sont pas nécessairement disponibles dans Power BI sans Python.

Dans cet exemple, je vais créer un fichier Python pour obtenir des données à partir de deux sources : un fichier CSV (téléchargez-le à partir du lien fourni ci-dessus) et un dataframe créé (un tableau avec des lignes et des colonnes).

### Étape 1 : Cliquez sur Obtenir des données

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-70.png)

### Étape 2 : Recherchez Python Script et cliquez pour ouvrir une nouvelle fenêtre de codage.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-128.png)

### Étape 3 : Tapez le code ci-dessous et cliquez sur Ok

Le df1 est un fichier CSV et df2 est un dataframe créé avec deux colonnes, A et B. Vous devez changer le répertoire de df1 pour l'emplacement du fichier CSV téléchargé.

```
import pandas as pd

df1 = pd.read_csv("C:/Corona_NLP_train.csv", encoding = "ISO-8859-1")
df2 = pd.DataFrame({'A': [1, 3, 6, 8],'B': [10, 30, 50, 90]})
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-72.png)

### Étape 4 : Charger les données

Vous verrez un plan de navigation montrant les données (comme dans d'autres méthodes de récupération de données.). Cochez la case des données que vous souhaitez charger et cliquez sur 'Charger'.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-73.png)

Et voilà ! Maintenant, voyons comment nous pouvons transformer les données.

## Comment utiliser Python pour transformer des données 🔍 

Vous pouvez également utiliser Python pour transformer vos données. Principalement, je l'utilise avec des expressions régulières. Par exemple, vous pouvez l'utiliser pour extraire des sous-chaînes d'une autre colonne qui correspondent à des motifs définis (comme obtenir des hashtags à partir du texte de Twitter).

Dans cet exemple, je vais trouver la longueur du texte en utilisant la fonction `len()` en Python.

### Étape 1 : Cliquez sur Transformer les données

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-74.png)

### Étape 2 : Sélectionnez la requête que vous souhaitez transformer

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-75.png)

### Étape 3 : Dans l'onglet Transformer, cliquez sur Exécuter le script Python

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-76.png)

Vous verrez une nouvelle fenêtre de script Python. Écrivez votre code ici et cliquez sur ok.

```python
dataset['Count'] = dataset['OriginalTweet'].str.len()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-77.png)

**Concept clé** : les données seront un DataFrame 'dataset', vous pouvez donc les manipuler avec des fonctions Pandas.

### Étape 4 : Développer le tableau

Le résultat sera un tableau. Cliquez pour développer le tableau. Assurez-vous que 'Utiliser le nom de colonne original comme préfixe' n'est pas coché.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-78.png)

Vous verrez le résultat de la transformation des données et les étapes sont ajoutées dans le plan des ÉTAPES APPLIQUÉES.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-79.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-80.png)

## Comment utiliser Python pour visualiser des données 📊 

Créer un graphique en utilisant la visualisation de Power BI seul peut avoir certaines limitations et certains graphiques peuvent ne pas être disponibles dans Power BI.

Python est pratique car il existe de nombreuses bibliothèques en Python qui peuvent générer n'importe quelle visualisation que vous souhaitez.

Les bibliothèques Python pour la visualisation de données qui sont couramment utilisées de nos jours incluent Matplotlib, Plotly, Seaborn et ggplot.

Bien qu'écrire du code en Python pour créer un graphique puisse être plus difficile que le concept de glisser-déposer de Power BI, il existe de nombreuses personnalisations de graphiques et d'exemples de code (à utiliser comme références).

Voyons comment cela fonctionne maintenant, étape par étape.

### Étape 1 : Dans le plan de visualisations, cliquez sur l'icône Py (Abréviation pour Python)

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-82.png)

Vous verrez une zone d'édition de script Python vide. 

### Étape 2 : Sélectionnez les colonnes que vous souhaitez visualiser.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-83.png)

Vous verrez une zone de codage vide. 

### Étape 3 : Écrivez le code 

Maintenant, il est temps d'écrire votre code. N'oubliez pas d'ajouter `plt.show()` pour afficher les graphiques. Cliquez sur l'icône d'exécution et attendez le résultat. Et vous avez terminé !

```python
import seaborn as sns
import matplotlib.pyplot as plt
import re

def find_hash(text):
	line=re.findall(r'(?<=#)\w+',text)
	return " ".join(line)
    
dataset['hash'] = dataset['OriginalTweet'].apply(lambda x:find_hash(x))
temp = dataset['hash'].value_counts()[:][1:11]
temp = temp.to_frame().reset_index().rename(columns={'index':'Hashtag','hash':'count'})

plt.figure(figsize=(20, 15))
sns.barplot(x="Hashtag",y="count", data = temp)
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-84.png)

**Note :** Si une erreur s'affiche après l'exécution du code, prenez une profonde inspiration et lisez le message d'erreur. :)

## Conclusion

Cet article vous a montré comment utiliser Python dans Power BI étape par étape, afin que vous puissiez tirer parti à la fois du tableau de bord interactif de Power BI et de la flexibilité de Python. 

Vous pouvez appliquer le code Python de nombreuses manières, y compris l'acquisition de données, la transformation et la visualisation.