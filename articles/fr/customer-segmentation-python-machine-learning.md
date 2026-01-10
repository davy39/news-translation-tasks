---
title: Comment effectuer la segmentation client en Python – Tutoriel de Machine Learning
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2022-11-02T18:56:39.000Z'
originalURL: https://freecodecamp.org/news/customer-segmentation-python-machine-learning
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/-GetPaidStock.com--635e3fa0c561f.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
seo_title: Comment effectuer la segmentation client en Python – Tutoriel de Machine
  Learning
seo_desc: 'Before I get into what this post is all about, I''d like to share the motivation
  that prompted me to write it.

  I''m writing this article because I recall the first time I learned about customer
  segmentation or clustering. I didn''t fully grasp what I wa...'
---

Avant d'aborder le sujet de cet article, je souhaite partager la motivation qui m'a poussé à l'écrire.

J'écris cet article parce que je me souviens de la première fois où j'ai appris la segmentation client ou le clustering. À l'époque, je ne comprenais pas pleinement ce que je faisais.

Tout ce dont je me souviens, c'est d'avoir mis toutes les caractéristiques dans `KMeans` et **voilà** – j'avais développé une segmentation client. Je ne comprenais pas les attributs du modèle pour chaque segment.

C'est pour cette raison que je partage mes connaissances sur la manière dont j'ai fini par comprendre la segmentation client, afin que vous puissiez en tirer profit.

Dans ce tutoriel, vous apprendrez à construire une segmentation client efficace ainsi qu'à effectuer une analyse exploratoire des données (EDA) efficace. Ce sont les ingrédients qui rendront votre résultat de segmentation client délicieux à consommer 😋. Sans plus attendre, commençons.

## Qu'est-ce que la segmentation client ?

Nous parlons de segmentation client depuis le début de l'article – mais vous ne savez peut-être pas ce que cela signifie.

Notez qu'il est important d'essayer de comprendre cette partie théorique avant de passer à la partie codage du tutoriel. Cette base vous aidera à construire le modèle de segmentation de manière efficace.

D'accord, revenons à la définition de ce qu'est la segmentation :

La segmentation signifie regrouper des entités en fonction de propriétés similaires. Les entités peuvent être des clients, des produits, etc.

Par exemple, la **segmentation client**, en particulier, signifie regrouper les clients en fonction de caractéristiques ou de propriétés similaires.

Il y a une chose à noter lors du regroupement des clients en fonction des propriétés : les propriétés que vous choisissez pour regrouper les clients doivent être pertinentes par rapport aux critères sur lesquels vous souhaitez les regrouper.

Par exemple, supposons que vous souhaitez catégoriser les clients en fonction de ce qu'ils achètent. Dans ce scénario, l'attribut du genre du client peut ne pas être optimal ou pertinent pour la segmentation.

Savoir comment sélectionner des attributs appropriés pour la segmentation client est crucial.

Examinons les différents types de segmentation client :

* Segmentation démographique.
  
* Segmentation comportementale.
  
* Segmentation géographique.
  
* Segmentation psychographique.
  
* Segmentation technographique.
  
* Segmentation basée sur les besoins.
  
* Segmentation basée sur la valeur.
  

Les types les plus typiques de segmentation des consommateurs sur lesquels vous travaillerez lors de la réalisation d'une segmentation tournent autour de la segmentation démographique et comportementale.

La **segmentation démographique** est le processus de regroupement des clients en fonction de leur démographie – c'est-à-dire, regrouper les clients en fonction de leur âge, revenu, éducation, état matrimonial, etc.

La **segmentation comportementale** signifie regrouper les clients en fonction de leur comportement. Par exemple, la fréquence à laquelle ils achètent en groupe, le montant total qu'ils dépensent pour un bien, la dernière fois qu'ils ont acheté un produit, etc.

Pour en savoir plus sur les autres types de segmentation client, vous pouvez lire [cet article](https://blog.hubspot.com/service/customer-segmentation).

## Critères pour la segmentation client

Lors du regroupement des clients, vous devez sélectionner des caractéristiques pertinentes qui sont adaptées à ce que vous souhaitez segmenter. Mais dans certaines circonstances, combiner des caractéristiques de plusieurs types de segmentation client pour générer un autre type de segmentation a du sens.

Par exemple, vous pouvez combiner des caractéristiques de la segmentation démographique et comportementale pour créer une nouvelle segmentation. C'est précisément ce que vous apprendrez dans cet article – nous construirons une segmentation client en utilisant des caractéristiques démographiques et comportementales.

Assez parlé – passons aux choses sérieuses.

## Comprendre le problème commercial.

Le problème commercial est de segmenter les clients en fonction de leur personnalité (démographique) et du montant qu'ils dépensent pour les produits (comportemental). Cela aidera l'entreprise à mieux comprendre la personnalité et les habitudes de ses clients.

### Outils que nous utiliserons pour ce projet

Bien sûr, nous utilisons Python pour construire notre projet – mais voici les outils et bibliothèques que nous utiliserons également pour nous aider.

1. Environnement Jupyter (Jupyter Lab ou Jupyter notebook) – pour expérimenter avec notre projet.
   
2. Pandas – pour charger les données sous forme de dataframe et manipuler les données.
   
3. Numpy et Scipy – pour effectuer quelques calculs mathématiques de base.
   
4. Scikit-Learn – pour construire notre modèle de segmentation client.
   
5. Seaborn, Matplotlib et Plotly Express – pour la visualisation des données.
   

Si vous n'avez pas certaines ou aucune de ces bibliothèques, vous pouvez consulter leur documentation officielle en ligne pour voir comment les installer.

### Ensemble de données que nous utiliserons pour ce projet

L'ensemble de données que nous utiliserons dans ce projet provient de Kaggle. Vous pouvez aller [ici](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis/download?datasetVersionNumber=1) pour le télécharger.

Voici quelques informations sur l'ensemble de données :

Pour faire simple, l'ensemble de données contient les données démographiques des clients et leur comportement en relation avec l'entreprise. Les caractéristiques de l'ensemble de données sont :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Customer-Personality-Features.png align="left")

### Caractéristiques de l'analyse de la personnalité des clients

| People | Promotion | Product | Place |
| --- | --- | --- | --- |
| Year Birth | NumberDealPurchase | MntWines | NumWebPurchases |
| Title | AcceptedCmp1 | MntFruits | NumCatalogPurchases |
| Education | AcceptedCmp2 | MntMeatProducts | NumStorePurchases |
| Marital_Status | AcceptedCmp3 | MntFishProducts | NumWebVisitsMonth |
| Income | AcceptedCmp4 | MntSweetProducts |  |
| Kidhome | AcceptedCmp5 | MntGoldProds |  |
| Teenhome | Response |  |  |
| Dt_customer, Recency, |  |  |  |
| and Complain |  |  |  |

Pour tirer le meilleur parti de ce tutoriel, vous pouvez télécharger l'intégralité du notebook Jupyter au préalable afin de pouvoir suivre facilement. Vous pouvez aller [ici](https://github.com/ibrahim-ogunbiyi/Customer-Segmentation) pour forker le dépôt.

## Analyse exploratoire des données (EDA)

Comme vous le savez peut-être, l'EDA est la clé pour bien performer en tant qu'analyste de données ou scientifique des données. Elle vous donne des informations de première main sur l'ensemble de données, et elle vous aide à comprendre toutes les relations entre les caractéristiques de votre ensemble de données.

Nous effectuerons les trois phases de l'EDA dans ce tutoriel qui sont :

1. Analyse univariée.
   
2. Analyse bivariée.
   
3. Analyse multivariée
   

Tout d'abord, nous devons importer toutes les bibliothèques nécessaires que nous utiliserons dans ce projet. Nous devons également charger l'ensemble de données dans un dataframe afin de voir toutes les caractéristiques qui y sont présentes.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
from scipy.stats import iqr
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


df = pd.read_csv("data/marketing_campaign.csv", sep="\t")
df.head()
```

Pour commencer, il y a de nombreuses caractéristiques dans l'ensemble de données – mais comme nous voulons nous concentrer sur la démographie et le comportement des clients, nous n'effectuerons l'EDA que sur les caractéristiques liées à ces catégories.

Gardez à l'esprit que l'EDA réalisée dans cet article est simplement un sous-ensemble de celle du Jupyter Notebook. J'ai fait cela pour éviter que l'article ne devienne trop encombré. Pour trouver l'intégralité de l'EDA dans le notebook, forkez le dépôt en cliquant sur ce [lien](https://github.com/ibrahim-ogunbiyi/Customer-Segmentation).

L'âge, le revenu, l'état matrimonial, l'éducation, le nombre total d'enfants et le montant dépensé pour les produits sont les attributs qui appartiennent à cette catégorie.

Tout d'abord, puisque la segmentation est basée sur le montant total que les clients ont dépensé, nous ajouterons le montant dépensé pour le produit :

```python
df["TotalAmountSpent"] = df["MntFishProducts"] + df["MntFruits"] + df["MntGoldProds"] + df["MntSweetProducts"] + df["MntMeatProducts"] + df["MntWines"]
```

Une fois cela fait, nous pouvons maintenant commencer notre EDA. Une EDA efficace comporte toujours trois étapes, comme je l'ai mentionné ci-dessus. Encore une fois, elles sont les suivantes :

1. Analyse univariée
   
2. Analyse bivariée.
   
3. Analyse multivariée.
   

### Analyse univariée

L'analyse univariée consiste à évaluer une seule caractéristique afin d'obtenir des informations à son sujet. Ainsi, la première étape pour effectuer une EDA est d'entreprendre une analyse univariée, qui inclut l'évaluation des statistiques descriptives ou récapitulatives concernant la caractéristique.

Par exemple, vous pourriez vérifier la distribution d'une caractéristique, la proportion d'une caractéristique, et ainsi de suite.

Dans notre cas, nous vérifierons la distribution des âges des clients dans l'ensemble de données. Nous pouvons faire cela en tapant ce qui suit :

```python
sns.histplot(data=df, x="Age", bins = list(range(10, 150, 10)))
plt.title("Distribution de l'âge des clients")
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Age-1.png align="left")

Nous pouvons voir d'après le résumé ci-dessus que la plupart des clients appartiennent à la tranche d'âge de `40-60`.

### Analyse bivariée

Après avoir effectué une analyse univariée sur toutes vos caractéristiques d'intérêt, l'étape suivante consiste à effectuer une analyse bivariée. Cela implique de comparer deux attributs en même temps.

L'analyse bivariée consiste à déterminer la corrélation entre deux caractéristiques, par exemple.

Dans notre cas, certaines des analyses bivariées que nous effectuerons dans le projet incluent l'observation du montant total moyen dépensé dans différents groupes d'âge de clients, la détermination d'une corrélation entre le revenu des clients et le montant total dépensé, et ainsi de suite, comme montré ci-dessous.

Par exemple, dans notre cas, nous voulons vérifier la relation entre le `Revenu` d'un client et le `TotalAmountSpent`. Nous pouvons faire cela en tapant ce qui suit :

```python
fig = px.scatter(data_frame=df_cut, x="Income",
                 y="TotalAmountSpent",
                 title="Relation entre le revenu du client et le montant total dépensé",
                height=500,
                color_discrete_sequence = px.colors.qualitative.G10[1:])
fig.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/newplot--14-.png align="left")

*Analyse de la relation entre le revenu du client et le montant total dépensé.*

Nous pouvons voir d'après l'analyse ci-dessus que lorsque le `Revenu` augmente, le `TotalAmountSpent` augmente également. Ainsi, d'après l'analyse, nous pouvons postuler que le `Revenu` est l'un des principaux facteurs qui déterminent combien un client pourrait dépenser.

### Analyse multivariée

Après avoir terminé l'analyse univariée (analyse d'une seule caractéristique) et bivariée (analyse de deux caractéristiques), la dernière phase de l'EDA consiste à effectuer une analyse multivariée.

L'analyse multivariée consiste à comprendre la relation entre deux variables ou plus.

Dans notre projet, l'une des analyses multivariées que nous ferons est de comprendre la relation entre le `Revenu`, le `TotalAmountSpent` et l'`Éducation` du client.

```python
fig = px.scatter(
    data_frame=df_cut,
    x = "Income",
    y= "TotalAmountSpent",
    title = "Relation entre le revenu et le montant total dépensé en fonction de l'éducation",
    color = "Education",
    height=500
)
fig.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/newplot--15-.png align="left")

*Analyse de la relation entre le revenu, le montant total dépensé et l'éducation.*

Nous pouvons voir d'après l'analyse que les clients ayant un niveau d'éducation de premier cycle dépensent généralement moins que les autres clients ayant des niveaux d'éducation plus élevés. Cela est dû au fait que les clients de premier cycle gagnent généralement moins que les autres clients, ce qui affecte leurs habitudes de dépense.

## Comment construire le modèle de segmentation

Après avoir terminé notre analyse, l'étape suivante consiste à créer le modèle qui segmentera les clients. `KMeans` est le modèle que nous utiliserons. C'est un modèle de segmentation populaire qui est également assez efficace.

Le modèle `KMeans` est un modèle d'apprentissage automatique non supervisé qui fonctionne simplement en divisant N observations en K nombres de clusters. Les observations sont regroupées dans ces clusters en fonction de leur proximité avec la moyenne de ce cluster, qui est communément appelée centroïdes.

Lorsque vous ajustez les caractéristiques dans le modèle et spécifiez le nombre de clusters ou de segments que vous souhaitez, `KMeans` sortira l'étiquette de cluster à laquelle chaque observation dans la caractéristique appartient.

Parlons des caractéristiques que vous pourriez vouloir ajuster dans un modèle `KMeans`. Il n'y a pas de limites au nombre de caractéristiques que vous pouvez utiliser pour construire un modèle de segmentation client – mais à mon avis, moins c'est mieux. Cela est dû au fait que vous pourrez saisir et interpréter les résultats de chaque segment plus facilement et clairement avec moins de caractéristiques.

Dans notre scénario, nous construirons d'abord le modèle `KMeans` avec deux caractéristiques, puis nous construirons le modèle final avec trois caractéristiques. Mais avant de commencer, passons en revue les hypothèses de `KMeans`, qui sont les suivantes :

* Les caractéristiques doivent être numériques.
   
* Les caractéristiques que vous ajustez dans `KMeans` doivent être normalement distribuées. Cela est dû au fait que `KMeans` (puisqu'il calcule la distance moyenne) est affecté par les valeurs aberrantes (valeurs qui s'écartent beaucoup des autres). Par conséquent, toute caractéristique asymétrique doit être modifiée afin d'être normalement distribuée. Heureusement, nous pouvons utiliser le package de transformation logarithmique de Numpy `np.log()`
   
* Les caractéristiques doivent également être à la même échelle. Pour cela, nous utiliserons le module `StandardScaler()` de Scikit-learn.
   

Nous concevrons notre modèle `KMeans` maintenant que nous avons saisi le concept principal. Donc, pour notre premier modèle, nous utiliserons les caractéristiques `Revenu` et `TotalAmountSpent`.

Pour commencer, puisque la caractéristique `Revenu` a des valeurs manquantes, nous les remplirons avec le nombre médian.

```python
df["Income"].fillna(df["Income"].median(), inplace=True)
```

Après cela, nous assignerons les caractéristiques avec lesquelles nous voulons travailler, `Revenu` et `TotalAmountSpent`, à une variable appelée `data`.

```python
data = df[["Income", "TotalAmountSpent"]]
```

Une fois cela fait, nous transformerons les caractéristiques et sauvegarderons le résultat dans une variable appelée `data_log`.

```python
df_log = np.log(data)
```

Ensuite, nous mettrons à l'échelle le résultat en utilisant `StandardScaler()` de Scikit-learn :

```python
std_scaler = StandardScaler()
df_scaled = std_scaler.fit_transform(df_log)
```

Une fois cela fait, nous pourrons alors construire le modèle. Donc, le modèle `KMeans` nécessite deux paramètres. Le premier est `random_state` et le second est `n_clusters` où :

* `n_clusters` représente le nombre de clusters ou de segments à dériver de `KMeans`.
   
* `random_state` : est requis pour des résultats reproductibles.
   

Donc, dans un contexte commercial, vous pourriez connaître le nombre de clusters dans lesquels vous souhaitez segmenter les clients à l'avance. Mais si ce n'est pas le cas, vous devrez expérimenter avec différents nombres de clusters pour trouver le nombre optimal.

Puisque nous ne sommes pas dans un contexte commercial, nous expérimenterons avec différents nombres de clusters.

La méthode du coude est la stratégie que nous utiliserons pour sélectionner le meilleur cluster. Elle fonctionne simplement en traçant l'erreur de chaque cluster et en cherchant un point qui forme un coude sur le graphique. Par conséquent, le cluster idéal est celui qui produit ce coude.

Voici le code qui nous aidera à atteindre cet objectif :

```python
errors = []
for k in range(1, 11):
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(df_scaled)
    error.append(model.inertia_)
    
 
plt.title('La méthode du coude')
plt.xlabel('k'); plt.ylabel('Erreur du cluster')
sns.pointplot(x=list(range(1, 11), y=errors)
plt.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/Elbow.png align="left")

Résumé de ce que fait le code ci-dessus. Nous avons spécifié le nombre de clusters à expérimenter, qui est dans la `range(1, 11)`. Ensuite, nous avons ajusté les caractéristiques sur ces clusters et ajouté l'erreur à la liste que nous avons créée précédemment.

Après cela, nous traçons l'erreur pour chaque cluster. Le diagramme montre que le cluster qui crée le coude est trois. Donc, trois clusters est la meilleure valeur pour notre modèle. Par conséquent, nous construirons le modèle `KMeans` en utilisant trois clusters.

```python
model = KMeans(n_clusters = 3, random_state=42)
model.fit(df_scaled)
```

Maintenant, nous avons construit notre modèle. La prochaine chose sera d'assigner l'étiquette de cluster pour chaque observation. Donc, nous assignerons l'étiquette à la caractéristique originale que nous n'avons pas traitée. C'est-à-dire, où nous avons assigné `Revenu` et `TotalAmountSpent` à la variable `data`

```python
data = data.assign(ClusterLabel = model.labels_)
```

### Comment interpréter le résultat du cluster

Maintenant que nous avons construit le modèle, la prochaine chose sera d'interpréter le résultat de chaque cluster.

Il existe de nombreuses façons de résumer les résultats de votre cluster en fonction de ce que vous souhaitez atteindre. Le résumé le plus courant est l'utilisation de la tendance centrale qui inclut la moyenne, la médiane et le mode.

Pour notre cas, nous utiliserons la médiane. Nous utilisons la médiane parce que les caractéristiques originales ont des valeurs aberrantes et la moyenne est très sensible aux valeurs aberrantes.

Donc, nous agrégerons les étiquettes de cluster et trouverons la médiane pour `Revenu` et `TotalAmountSpent`. Nous pouvons utiliser la méthode `groupby` de Pandas pour cela.

```python
data.groupby("ClusterLabel")[["Income", "TotalAmountSpent"]].median()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-265.png align="left")

Nous pouvons voir qu'il y a une tendance au sein des clusters :

* Le cluster 0 correspond aux clients qui gagnent moins et dépensent moins.
   
* Le cluster 1 représente les clients qui gagnent plus et dépensent plus.
   
* Le cluster 2 représente les clients qui gagnent modérément et dépensent modérément.
   

Nous pouvons également visualiser la relation en entrant le code suivant :

```python
fig = px.scatter(
    data_frame=data,
    x = "Income",
    y= "TotalAmountSpent",
    title = "Relation entre le revenu et le montant total dépensé",
    color = "ClusterLabel",
    height=500
)
fig.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/newplot--10-.png align="left")

*Analyse de la relation entre le revenu et le montant total dépensé*

Maintenant, de la même manière que nous avons construit le modèle formel, nous construirons le modèle KMeans en utilisant 3 caractéristiques (la méthode du coude montre également que 3 clusters est le nombre optimal).

```python
data = df[["Age", "Income", "TotalAmountSpent"]]
df_log = np.log(data)
std_scaler = StandardScaler()
df_scaled = std_scaler.fit_transform(df_log)
```

```python
model = KMeans(n_clusters=3, random_state=42)
model.fit(df_scaled)

data = data.assign(ClusterLabel= model.labels_)

result = df_result.groupby("ClusterLabel").agg({"Age":"mean", "Income":"median", "TotalAmountSpent":"median"}).round()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-249.png align="left")

Nous pouvons voir d'après le résumé ci-dessus que :

* Le cluster 0 représente les jeunes clients qui gagnent beaucoup et dépensent également beaucoup.
   
* Le cluster 1 représente les clients plus âgés qui gagnent beaucoup et dépensent également beaucoup.
   
* Le cluster 2 représente les jeunes clients qui gagnent moins et dépensent également moins.
   

Nous pouvons également visualiser notre résultat en tapant le code suivant :

```python
fig = px.scatter_3d(data_frame=data, x="Income", 
                    y="TotalAmountSpent", z="Age", color="ClusterLabel", height=550,
                   title = "Visualisation du résultat du cluster en utilisant 3 caractéristiques")
fig.show()
```

![Image](https://www.freecodecamp.org/news/content/images/2022/10/newplot--17-.png align="left")

*Résultats des clusters utilisant trois caractéristiques*

# Conclusion

Dans ce tutoriel, vous avez appris à construire un modèle de segmentation client. Il y a beaucoup de caractéristiques que nous n'avons pas abordées dans cet article. Mais je vous suggère d'expérimenter avec et de créer des modèles de segmentation client en utilisant différentes caractéristiques.

J'espère que vous apprendrez davantage en faisant cela. Merci d'avoir lu l'article. Bon codage !

Le lien vers le code complet peut être trouvé ci-dessous. Et [voici un article sur le clustering K-Means si vous souhaitez en savoir plus](https://www.freecodecamp.org/news/how-to-build-and-train-k-nearest-neighbors-ml-models-in-python/).

%[https://github.com/ibrahim-ogunbiyi/Customer-Segmentation]