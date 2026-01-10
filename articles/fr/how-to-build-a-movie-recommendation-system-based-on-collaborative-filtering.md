---
title: Comment construire un système de recommandation de films basé sur le filtrage
  collaboratif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-11-29T15:45:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-movie-recommendation-system-based-on-collaborative-filtering
coverImage: https://www.freecodecamp.org/news/content/images/2024/08/pexels-nathan-engel-50858-436413.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
seo_title: Comment construire un système de recommandation de films basé sur le filtrage
  collaboratif
seo_desc: "By Jess Wilk\nIn today’s world of technology, we get more recommendations\
  \ from Artificial Intelligence models than from our friends. \nSurprised? Think\
  \ of the content you see and the apps you use daily. We get product recommendations\
  \ on Amazon, clothin..."
---

Par Jess Wilk

Dans le monde technologique d'aujourd'hui, nous recevons plus de recommandations de la part de modèles d'Intelligence Artificielle que de nos amis. 

Surpris ? Pensez au contenu que vous voyez et aux applications que vous utilisez quotidiennement. Nous recevons des recommandations de produits sur Amazon, des recommandations de vêtements sur Myntra, et des suggestions de films sur Netflix basées sur nos préférences passées, nos achats, et ainsi de suite. 

Vous êtes-vous déjà demandé ce qu'il y avait sous le capot ? La réponse est les systèmes de recommandation alimentés par le machine learning. Les systèmes de recommandation sont des algorithmes de machine learning développés à l'aide de données historiques et d'informations issues des réseaux sociaux pour trouver des produits personnalisés selon nos préférences. 

Dans cet article, je vais vous guider à travers les différents types de méthodes de ML pour construire un système de recommandation et me concentrer sur la **méthode de filtrage collaboratif**. Nous allons obtenir un ensemble de données d'exemple et créer un système de recommandation basé sur le filtrage collaboratif étape par étape. 

Assurez-vous de prendre une tasse de cappuccino (ou toute autre boisson de votre choix) et préparez-vous !

## Prérequis

Avant de nous lancer dans cette aventure, vous devriez avoir une compréhension de base des concepts de machine learning et une familiarité avec la programmation Python. La connaissance du traitement des données et l'expérience avec des bibliothèques comme Pandas, NumPy et Scikit-learn seront également bénéfiques. 

Si vous êtes nouveau dans ces sujets, vous pouvez consulter le cours [Introduction à la Data Science](https://hyperskill.org/tracks/28) sur Hyperskill, où je contribue en tant qu'expert.

## Différents types de systèmes de recommandation

Vous serez probablement d'accord pour dire qu'il existe plus d'une façon de décider quoi suggérer ou recommander lorsqu'un ami demande notre opinion. Cela s'applique également à l'IA ! 

En machine learning, deux méthodes principales de construction de moteurs de recommandation sont les méthodes basées sur le contenu et le filtrage collaboratif.

Lorsque vous utilisez la méthode de filtrage basée sur le contenu, les produits ou articles suggérés sont basés sur ce que vous avez aimé ou acheté. Cette méthode alimente le modèle de machine learning avec des données historiques telles que l'historique de recherche du client, les enregistrements d'achat et les articles dans leurs listes de souhaits. Le modèle trouve d'autres produits qui partagent des caractéristiques similaires à vos préférences passées. 

Comprenons mieux cela avec un exemple de recommandation de film. Supposons que vous avez vu Inception et que vous lui avez donné une note de cinq étoiles. Trouver des films de thèmes et de genres similaires, comme Interstellar et Matrix, et les recommander s'appelle le filtrage basé sur le contenu.

Imaginez si tous les systèmes de recommandation suggéraient simplement des choses basées sur ce que vous avez vu. Comment découvririez-vous de nouveaux genres et films ? C'est là que la méthode de filtrage collaboratif intervient. Alors, qu'est-ce que c'est ?  
  
Plutôt que de trouver un contenu similaire, la méthode de filtrage collaboratif trouve d'autres utilisateurs et clients similaires à vous et recommande leurs choix. L'algorithme ne prend pas en compte les caractéristiques des produits comme dans le cas du filtrage basé sur le contenu. 

Pour comprendre comment cela fonctionne, revenons à notre exemple de recommandation de films. Le système regarde les films que vous avez aimés et trouve d'autres utilisateurs qui ont aimé les mêmes films. Ensuite, il voit ce que ces utilisateurs similaires ont également aimé et suggère ces films à vous. 

Par exemple, si vous et un ami aimez tous les deux The Shawshank Redemption, et que votre ami aime également Forrest Gump, le système recommandera Forrest Gump à vous, pensant que vous pourriez partager les goûts de votre ami. 

Dans les sections à venir, je vais vous montrer comment construire un moteur de recommandation de films en utilisant Python basé sur le filtrage collaboratif.

![Image](https://lh7-us.googleusercontent.com/wJ_Zjqr5YvwCMHqnbazh_QBZU6mXFVbtWfk9JoLvvpB5xj9YyuQ-uLAs3wUBMkqhvYGzo4w2ORz9H8qwDm1U97TlLUpjkQDH-8liZE7OUAadKG9rXH18VsIuWqhVKKEnsXfSaJZH3_Hu7lL-Y_cVNuQ)
_Apprendre à construire un moteur de recommandation de films en utilisant Python basé sur le filtrage collaboratif_

## Comment préparer et traiter l'ensemble de données de films

La première étape de tout projet de machine learning est la collecte et la préparation des données. Notre objectif étant de construire un moteur de recommandation de films, j'ai choisi un ensemble de données d'évaluations de films. L'ensemble de données est disponible gratuitement sur [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/).

L'ensemble de données contient deux fichiers principaux au format CSV :

1. _Ratings.csv_ : Contient les évaluations données par chaque utilisateur pour chaque film qu'il a regardé
2. _Movies_metadata.csv_ : Contient des informations sur le genre, le budget, la date de sortie, les revenus, etc. pour tous les films de l'ensemble de données.

Commençons par importer les packages Python nécessaires pour lire les fichiers CSV. 

```python
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Ensuite, lisez le fichier _Ratings_ dans des dataframes Pandas et regardez les colonnes.

```python
user_ratings_df = pd.read_csv("../input/the-movies-dataset/ratings.csv")
user_ratings_df.head()
```

![Image](https://lh7-us.googleusercontent.com/gwVTHmk5vVq5272EqnszziBLxG0jUPFZifPyzvWKicWgN8CRf_Qit01kdDwrtcOrkUSJJJkwRPInDb5evsAuk98c1x9CeSWZFEX6yjio8syzg5H5LhpB2UWFq_BAQCNzR5xPwlZWNfv8dsD6CWqsMmM)
_Colonnes dans le dataframe Pandas_

La colonne **UserId** contient l'ID unique pour chaque client, et **movieId** contient le numéro d'identification unique pour chaque film. La colonne **rating** contient l'évaluation donnée par l'utilisateur particulier au film sur 5. La colonne **timestamp** peut être supprimée, car nous n'en aurons pas besoin pour notre analyse.

Ensuite, lisons les informations de métadonnées des films dans un dataframe. Gardons seulement les colonnes pertinentes du titre du film et du genre pour chaque MovieID.

```python
movie_metadata = pd.read_csv("../input/the-movies-dataset/movies_metadata.csv")
movie_metadata = movie_names[['title', 'genres']]
movie_metadata.head()
```

![Image](https://lh7-us.googleusercontent.com/85sTR6KWMLUBRn7vtlCtLK-pfZzuBdgy13w76iCQ6elqnOhFmSsHk2me6Sh35eAV277VkWKpTWIFy6fL3Bl6T6gvyHwXu8eZ0mK18snH-M78u9sb-CvNGXL25LE9j6d_WzLRgzqEOyl-8C7dLth_tBI)
_Les colonnes du titre du film et du genre pour chaque MovieID_

Ensuite, combinons ces dataframes sur la colonne commune **movieID**.

```python
movie_data = user_ratings_df.merge(movie_metadata, on='movieId')
movie_data.head()
```

Cet ensemble de données peut être utilisé pour l'analyse exploratoire des données. Vous pouvez trouver le film avec le plus grand nombre d'évaluations, la meilleure évaluation, etc. Essayez-le pour mieux comprendre les données avec lesquelles vous travaillez.

## Comment construire la matrice utilisateur-article

Maintenant que notre ensemble de données est prêt, concentrons-nous sur le fonctionnement du filtrage collaboratif. L'algorithme de machine learning vise à découvrir des modèles de préférences utilisateur utilisés pour faire des recommandations. 

Une approche courante consiste à utiliser une **matrice utilisateur-article**. Cela implique une grande feuille de calcul où les utilisateurs sont listés d'un côté et les films de l'autre. Chaque cellule de la feuille de calcul montre si un utilisateur aime un film particulier. Le système utilise ensuite divers algorithmes pour analyser cette matrice, trouver des modèles et générer des recommandations.

Cette matrice nous conduit à l'un des avantages du filtrage collaboratif : il est excellent pour découvrir de nouvelles recommandations inattendues. Puisqu'il est basé sur le comportement des utilisateurs, il peut suggérer un film que vous n'auriez peut-être jamais considéré mais que vous aimerez probablement.

Créons une matrice d'évaluations utilisateur-film pour notre ensemble de données. Vous pouvez le faire en utilisant la fonction pivot intégrée d'un dataframe Pandas, comme montré ci-dessous. Nous utilisons également la méthode **`fillna()`** pour imputer les valeurs manquantes ou nulles avec 0.

```python
user_item_matrix = ratings_data.pivot(index=['userId'], columns=['movieId'], values='rating').fillna(0)
user_item_matrix

```

Voici notre matrice de sortie :

![Image](https://lh7-us.googleusercontent.com/pSpOQE0CsFOdRl1Rkf4Udo0FvTz7N7NDEHi82vYkHkZRwXp0cjsfgTW2OubIg1gHOgX27lBTsVExbsJoTO93M9THzmGduM_PulBPTXvv_df6U-bLxUzCXKKDFfVjk5lP8CvphnVglBGwWvNn-neQjEI)
_Une matrice d'évaluations utilisateur-film pour notre ensemble de données_

Parfois, la matrice peut être creuse. La sparsité fait référence aux valeurs nulles. Cela pourrait augmenter considérablement la quantité de ressources de calcul nécessaires. Il est recommandé de compresser les matrices creuses en utilisant le package Python **scipy** lors de la manipulation d'un grand ensemble de données.

## Comment définir et entraîner le modèle

Vous pouvez utiliser plusieurs algorithmes de machine learning pour le filtrage collaboratif, comme **K-nearest neighbors** (KNN) et **SVD**. J'utiliserai un modèle KNN ici. 

KNN est super simple. Imaginez un grand tableau coloré avec des points représentant différents articles (comme des films). Chaque point est proche des autres qui sont similaires. Lorsque vous demandez à KNN des recommandations, il trouve l'emplacement de votre article préféré sur ce tableau et regarde ensuite autour de lui pour voir les points les plus proches—ce sont vos recommandations. 

Maintenant, le paramètre métrique dans KNN est crucial. C'est comme la règle que le système utilise pour mesurer la distance entre ces points. La métrique utilisée ici est la similarité cosinus.

### Qu'est-ce que la similarité cosinus ?

C'est une métrique qui mesure à quel point deux entités sont similaires (comme des documents ou des vecteurs dans un espace multidimensionnel), indépendamment de la taille. La similarité cosinus est largement utilisée en NLP pour trouver des mots de contexte similaires.  
  
Suivez l'extrait ci-dessous pour définir un modèle KNN, la métrique et d'autres paramètres. Le modèle est ajusté sur la matrice utilisateur-article créée dans la section précédente.

```python
# Définir un modèle KNN sur la similarité cosinus
cf_knn_model= NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10, n_jobs=-1)


# Ajuster le modèle sur notre matrice
cf_knn_model.fit(user_item_matrix)


```

Ensuite, définissons une fonction pour fournir le nombre souhaité de recommandations de films, étant donné un titre de film comme entrée. Le code ci-dessous trouve les données des voisins les plus proches et pointe vers le nom du film d'entrée en utilisant l'algorithme KNN. Les paramètres d'entrée pour la fonction sont :

1. `**n_recs**` : Contrôle le nombre de recommandations finales que nous obtiendrons en sortie
2. `**Movie_name**` : Nom du film d'entrée, sur la base duquel nous trouvons de nouvelles recommandations
3. `**Matrix**` : La matrice d'évaluations utilisateur-film

```python
def movie_recommender_engine(movie_name, matrix, cf_model, n_recs):
    # Ajuster le modèle sur la matrice
    cf_knn_model.fit(matrix)
    
    # Extraire l'ID du film d'entrée
    movie_id = process.extractOne(movie_name, movie_names['title'])[2]
    
    # Calculer les distances des voisins
    distances, indices = cf_model.kneighbors(matrix[movie_id], n_neighbors=n_recs)
    movie_rec_ids = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
    
    # Liste pour stocker les recommandations
    cf_recs = []
    for i in movie_rec_ids:
        cf_recs.append({'Title':movie_names['title'][i[0]],'Distance':i[1]})
    
    # Sélectionner le nombre de recommandations nécessaires
    df = pd.DataFrame(cf_recs, index = range(1,n_recs))
     
    return df

```

## Comment obtenir des recommandations à partir du modèle

Appelons notre fonction définie pour obtenir des recommandations de films. Par exemple, nous pouvons obtenir une liste des 10 films recommandés pour quelqu'un qui est fan de Batman.

```python
n_recs = 10
movie_recommender_engine('Batman', user_rating_matrix, cf_knn_model, n_recs)
```

![Image](https://lh7-us.googleusercontent.com/PRRCkFh6z1KyQkE4lDUCf8acQFlCwV9WBBVfiGeG7Fn77dD9412QDW54tCH7On9HXdIR4dLYvyA0zs7LXHgmeLqXHIXgQ3yaMt6g5GGdiT2BHNo1o2IZ56gfg4jfKY86wG_pRB7vKsPg5JLsme9AMig)
_Une liste des 10 films recommandés pour quelqu'un qui est fan de Batman_

Hourra ! Nous avons obtenu le résultat dont nous avions besoin.

## Avantages et limitations du filtrage collaboratif

Les avantages de cette méthode incluent :

* **Recommandations personnalisées** : Offre des suggestions sur mesure basées sur le comportement de l'utilisateur, conduisant à des expériences hautement personnalisées.
* **Découverte de contenu diversifié** : Capable de recommander une large gamme d'articles, aidant les utilisateurs à découvrir du contenu qu'ils pourraient ne pas trouver par eux-mêmes. Cela donne un avantage à la découverte de contenu diversifié par rapport au filtrage basé sur le contenu.
* **Sagesse communautaire** : Exploite les préférences collectives des utilisateurs, conduisant souvent à des recommandations plus précises que l'analyse individuelle ou basée sur le contenu seule.
* **Adaptation dynamique** : Le modèle est continuellement mis à jour avec les interactions des utilisateurs, gardant les recommandations pertinentes et à jour.

Ce n'est pas tout rose, cependant. Un grand défi est le problème du _démarrage à froid_. Par exemple, cela se produit lorsque de nouveaux films ou utilisateurs sont ajoutés au système. Le système a du mal à faire des recommandations précises car il n'y a pas assez de données sur ces nouvelles entrées. 

Un autre problème est le biais de popularité. Les films populaires sont souvent recommandés, éclipsant des pépites moins connues. Il y a aussi des problèmes de scalabilité qui viennent avec la gestion d'un si grand ensemble de données. 

Lors du développement de moteurs basés sur le filtrage collaboratif, les dépenses computationnelles et la sparsité des données doivent être gardées à l'esprit pour un processus efficace. Il est également recommandé de prendre des mesures pour garantir la confidentialité et la sécurité des données.

## Conclusion

L'utilisation du filtrage collaboratif pour construire un système de recommandation de films représente une avancée significative dans la personnalisation du contenu numérique. Ce système reflète nos préférences et nous expose à une gamme plus large de choix basés sur les goûts d'utilisateurs similaires. 

Malgré ses défis, tels que le problème du démarrage à froid et le biais de popularité, les avantages des recommandations personnalisées en font un outil puissant dans l'industrie du machine learning. À mesure que la technologie avance, ces systèmes deviendront encore plus sophistiqués, offrant des expériences utilisateur raffinées et agréables dans le monde numérique.

Merci d'avoir lu ! Je suis Jess, et je suis un expert chez Hyperskill. Vous pouvez consulter un cours [Introduction à la Data Science](https://hyperskill.org/tracks/28) sur la plateforme.