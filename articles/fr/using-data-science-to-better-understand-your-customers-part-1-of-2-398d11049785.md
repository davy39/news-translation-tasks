---
title: Comment utiliser la Data Science pour mieux comprendre vos clients
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-15T13:57:09.000Z'
originalURL: https://freecodecamp.org/news/using-data-science-to-better-understand-your-customers-part-1-of-2-398d11049785
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ZmsRm4xaKe99RG4v.jpg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: marketing
  slug: marketing
- name: sales
  slug: sales
- name: technology
  slug: technology
seo_title: Comment utiliser la Data Science pour mieux comprendre vos clients
seo_desc: 'By Jerin Paul

  How much prominence do customers hold in your business layout? Well, this was a
  rhetorical question. We all know that the majority of businesses thrive only because
  of their customers. Therefore it is imperative that you understand your...'
---

Par Jerin Paul

Quelle importance accordent les clients dans votre structure commerciale ? Eh bien, c'était une question rhétorique. Nous savons tous que la majorité des entreprises prospèrent uniquement grâce à leurs clients. Il est donc impératif de bien comprendre vos clients avant de les servir. Connaître vos clients vous aide à fournir des services sur mesure. Cela entraîne une meilleure engagement des clients et une augmentation des ventes.

![Image](https://cdn-media-1.freecodecamp.org/images/yYhA-GMzdl7VqIm21g5SlqhBwdclVm3LQXzb)
_Cette image vaut définitivement mille mots. Source : [economictimes](https://economictimes.indiatimes.com" rel="noopener" target="_blank" title=")_

Connaissez-vous vos clients ? Eh bien, cette question est très vague. Si vous n'êtes pas en mesure de répondre à cela avec certains aspects qualitatifs de vos clients, alors vous devez vous mettre au travail maintenant. Je suis sûr que tous les propriétaires d'entreprise ont une image de leur client idéal dans leur esprit, peu importe à quel point elle peut être obscure. Souvent, cette image est fabriquée à partir de l'intuition. Elle peut ne pas être soutenue par des preuves tautologiques.

Les données ne mentent jamais. Ce n'est rien de plus qu'une collection de faits et de chiffres, et parfois elles peuvent nous montrer un miroir. Cet article expliquera comment utiliser la « magie » de la data science pour obtenir une compréhension cohérente de vos clients. Précisément, nous apprendrons comment appliquer un algorithme de clustering à ce [jeu de données des clients du centre commercial](https://www.kaggle.com/shwetabh123/mall-customers). Nous tirerons ensuite des inferences de la sortie pour mieux comprendre les clients qui fréquentent le centre commercial. Merci d'avoir supporté une si longue introduction, et vous obtenez [le code source du projet](https://github.com/AssiduousArchitect/Customer-Clustering) pour votre patience.

### Qu'est-ce que le regroupement de clients ?

La segmentation des clients ou le regroupement des clients est la pratique consistant à diviser les clients d'une entreprise en groupes (a.k.a. buckets) qui reflètent la similarité entre les clients de chaque groupe. Le but de segmenter les clients est de décider comment se rapporter aux clients de chaque segment afin de maximiser la valeur de chaque client pour l'entreprise.

Le regroupement des clients vous permet de répondre à chaque groupe de clients de manière à maximiser vos ventes. Pour les marketeurs, segmenter vos clients cibles vous permet de façonner vos communications de manière à causer un impact maximal.

Dans ce projet, nous utiliserons l'analyse de clusters pour segmenter les clients en clusters basés sur leur revenu annuel. Pour cela, nous utiliserons Kmeans, qui est l'un des meilleurs algorithmes de clustering. Le clustering K-means est un algorithme d'apprentissage non supervisé qui trouve des groupes dans les données. Le nombre de groupes est représenté par la lettre K.

### Commençons.

N'hésitez pas à suivre. Le jeu de données peut être téléchargé [ici](https://www.kaggle.com/shwetabh123/mall-customers).

#### Un aperçu des données.

Le jeu de données des clients du centre commercial est un jeu de données relativement petit car il ne contient que 199 lignes et 5 colonnes. Si vous jetez un coup d'œil à l'image ci-dessous ce paragraphe, vous remarquerez que ces cinq titres de colonnes sont CustomerID, Genre, Age, Annual Income (k$), et Spending Score (1100).

![Image](https://cdn-media-1.freecodecamp.org/images/QYDu05zfckCaB1IdJpQoZAwK3ye93G50RN4E)

Nous allons commencer par importer les bibliothèques nécessaires.

```py
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt 
plt.rc("font", size=14)
```

Maintenant, nous allons importer le jeu de données.

```py
data_path = "Mall_Customers.csv"
df = pd.read_csv(data_path)
```

Peut-être que c'est juste moi, mais je trouve quelques en-têtes de colonnes dérangeants pour une raison quelconque. Plongeons-nous et changeons ceux-ci.

```py
df.rename(columns={'Genre':'Gender',
                   'Annual Income (k$)':'Annual_Income',
                   'Spending Score (1-100)':'Spending_Score'
                  }, 
                   inplace=True
          )
```

Dans ce projet, nous allons regrouper les clients en utilisant leur revenu annuel et leur score de dépenses (entre 1 et 100). Par conséquent, nous n'utiliserons que ces deux colonnes.

```py
X = df.iloc[:, [3, 4]].values
```

Maintenant que nous sommes tous prêts sur le front des données, il est temps de commencer notre clustering. Avant de lancer notre algorithme de clustering, il est impératif de déterminer le nombre de clusters pour diviser nos clients. Il existe quelques méthodes différentes pour déterminer le nombre idéal de clusters pour ce jeu de données. Pour cela, nous utiliserons la méthode du coude.

#### Méthode du coude

Une méthode pour déterminer le nombre de clusters consiste à utiliser la méthode du coude. Cette méthode consiste à exécuter l'algorithme de clustering K-means sur les données pour différentes valeurs de K et à calculer la somme des erreurs quadratiques (S.S.E.) pour chaque valeur de K.

Ensuite, ces valeurs sont tracées sur un graphique, et nous pouvons voir que la S.S.E. tend à diminuer à mesure que la valeur de K augmente. La S.S.E. devient 0 lorsque les valeurs de K sont égales au nombre de points de données, car alors chaque point de données est son propre cluster. Notre objectif est de trouver un point avec une petite valeur de K et qui a une faible S.S.E.

Dans cette expérience, nous exécuterons K-means pour différentes valeurs de K dans la plage de 0 à 10 et stockerons la S.S.E. dans une liste appelée distortions.

```py
distortions = []
K = range(1, 10)
for k in K:
    kmeansModel = KMeans(n_clusters = k, init = 'k-means++',    random_state = 23)
    kmeansModel.fit(X)
    distortions.append(kmeansModel.inertia_)
    
plt.plot(K, distortions)
plt.title("The Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("S.S.E.")
plt.show()
```

Maintenant, jetons un coup d'œil au graphique.

![Image](https://cdn-media-1.freecodecamp.org/images/zLZampxMLJ4pfA1B2g-tn9I3N9CFtq4o7v6E)

Sur ce graphique, vous pouvez observer que la S.S.E. chute fortement après chaque itération de K. Vous pouvez également observer qu'après que K atteint 5, c'est une pente descendante à partir de là. Donc, 5 semble être une valeur optimale pour K, et cela signifie que nous diviserons les clients en 5 clusters.

Maintenant que nous avons déterminé le nombre de clusters, nous pouvons aller de l'avant et créer ces clusters.

```py
kmeansModel = KMeans(n_clusters = 5, init = 'k-means++', random_state = 23)
Y = kmeansModel.fit_predict(X)
```

Étant donné que le jeu de données était petit, tous ces processus ne prennent pas de temps à se terminer. Une fois les clusters créés, nous pouvons les tracer sur un graphique. Chaque point de cluster est marqué à l'aide d'un signe différent, et les centroïdes de chaque cluster sont marqués à l'aide de points rouges solides.

![Image](https://cdn-media-1.freecodecamp.org/images/pHXGAqO2-AV501JSnrgnUVzcmPzxYKEhYCPC)
_Regardez-les !_

Simplement en regardant le graphique, nous en apprenons sur les cinq différents types de clients qui fréquentent le centre commercial. Si nous devions les nommer, ils pourraient être nommés comme suit :  
i. Faible revenu, grands dépensiers (Rouge).  
ii. Faible revenu, petits dépensiers (Bleu).  
iii. Revenu moyen, dépenses moyennes (Orange).  
iv. Revenu élevé, grands dépensiers (Vert)  
v. Revenu élevé, petits dépensiers (Violet).

Les membres de chacun de ces groupes auraient plus de caractéristiques communes entre eux, et donc nous avons un groupe homogène. Les personnes de chacun de ces clusters peuvent avoir des besoins et des désirs similaires. En gardant cela à l'esprit, toutes les activités de marketing/vente peuvent accommoder ces besoins et désirs pour attirer plus de tels clients. Par exemple, une vente de réduction hebdomadaire qui cible le groupe à faible revenu ou des points de récompense pour les achats qui cibleront les grands dépensiers, les transformant en clients réguliers. Les possibilités sont illimitées et ne sont limitées que par notre imagination.

### Conclusion

Comprendre la base de clients d'une entreprise est d'une importance capitale. L'une des façons de gagner une compréhension plus profonde du comportement des clients est de les segmenter en différents groupes basés sur leur comportement (revenu et dépenses dans cette expérience.) Les personnes similaires tendent à se comporter de manière similaire, et c'est le cœur de la segmentation des clients. Par conséquent, en planifiant toutes les activités de vente et de marketing autour de ces groupes, cela promettrait un retour sur investissement plus élevé et une expérience client agréable.