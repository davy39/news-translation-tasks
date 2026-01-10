---
title: Comment extraire les données YouTube Analytics et les analyser en Python
subtitle: ''
author: Adejumo Ridwan Suleiman
co_authors: []
series: null
date: '2025-03-26T16:05:29.893Z'
originalURL: https://freecodecamp.org/news/extract-youtube-analytics-data-and-analyze-in-python
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743005089726/39e2323d-8f7b-4bf4-94cb-288aeb9cea4f.png
tags:
- name: Python
  slug: python
- name: Machine Learning
  slug: machine-learning
- name: Data Science
  slug: data-science
- name: youtube
  slug: youtube
- name: data analysis
  slug: data-analysis
seo_title: Comment extraire les données YouTube Analytics et les analyser en Python
seo_desc: 'If you’re a YouTube content creator, you’ll make data-driven decisions
  when posting content. This helps you target the right audience when creating your
  videos.

  YouTube Studio provides YouTube Analytics, where you can get comprehensive data
  about you...'
---

Si vous êtes un créateur de contenu YouTube, vous prendrez des décisions basées sur les données lors de la publication de contenu. Cela vous aide à cibler le bon public lors de la création de vos vidéos.

YouTube Studio fournit YouTube Analytics, où vous pouvez obtenir des données complètes sur votre chaîne. Mais il y a un piège : la plupart des statistiques fournies par YouTube Analytics sont descriptives et non prédictives. Cela signifie que des informations comme les vues futures, le nombre d'abonnés et les facteurs influençant le temps de visionnage ou les revenus ne sont pas disponibles. Cela signifie que vous devrez calculer ces métriques vous-même.

Dans cet article, vous apprendrez comment exporter des données de YouTube Analytics vers Python afin de pouvoir les analyser davantage ou créer des visualisations. Vous pouvez même construire votre propre tableau de bord personnalisé en utilisant diverses bibliothèques Python comme [Streamlit](https://streamlit.io/), [Shiny](https://shiny.posit.co/py/), ou [Dash](https://dash.plotly.com/).

### Voici ce que nous allons couvrir

* [Prérequis](#heading-prerequis)
    
* [Étape 1 : Identifier l'énoncé du problème](#heading-etape-1-identifier-lenonce-du-probleme)
    
* [Étape 2 : Extraire les données](#heading-etape-2-extraire-les-donnees)
    
* [Étape 3 : Analyser les données en Python](#heading-etape-3-analyser-les-donnees-en-python)
    
    * [Analyse de corrélation](#heading-analyse-de-correlation)
        
    * [Analyse de la rétention du public](#heading-analyse-de-la-retention-du-public)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis

* Compte YouTube et YouTube Studio actif
    
* Jupyter Notebook, Google Colab, Kaggle, ou tout autre environnement prenant en charge Python
    
* Bibliothèque [Pandas](https://pandas.pydata.org/) installée
    
* Bibliothèque [Seaborn](https://seaborn.pydata.org/) installée
    
* Bibliothèque [Matplotlib](https://matplotlib.org/) installée
    

## Étape 1 : Identifier l'énoncé du problème

Avant de procéder, nous devons savoir ce que nous cherchons – car YouTube Analytics dispose de nombreuses métriques, et cela peut devenir écrasant. Ma chaîne n'a pas un nombre énorme d'abonnés, mais j'ai assez de vidéos et de vues. Nous utiliserons donc mes données comme exemple.

Notez simplement que cette analyse que je vais mener dans ce tutoriel est spécifique à ma chaîne et peut varier d'une chaîne à l'autre. Vous pourrez utiliser les techniques ici pour répondre aux mêmes questions similaires en utilisant vos données, mais vos résultats seront différents des miens.

Voici les questions auxquelles je souhaite trouver une réponse :

1. **Analyse de corrélation**
    

* **Vues et temps de visionnage** – Les temps de visionnage plus longs sont-ils associés à des vues plus élevées ?
    
* **Vues et abonnés** – Plus de vues se traduisent-elles par plus d'abonnés ?
    
* **Impressions et taux de clics (CTR%)** – Une impression plus forte conduit-elle à un meilleur engagement ?
    
* **Temps de visionnage et durée moyenne de visionnage** – Les vidéos plus longues sont-elles plus regardées ?
    

2. **Analyse de la rétention du public**
    

* **Durée moyenne de visionnage vs. Durée de la vidéo** – Les vidéos plus longues sont-elles regardées en entier ?
    
* **Points de décrochage** – Quelle plage de durée a la meilleure rétention ?
    
* **Taux de rétention (%)** – Temps de visionnage divisé par la durée ?
    

## Étape 2 : Extraire les données

Connectez-vous à votre compte YouTube Studio, allez dans l'onglet Analytics et cliquez sur Mode avancé.

![Image montrant le tableau de bord YouTube Analytics et le Mode avancé](https://cdn.hashnode.com/res/hashnode/image/upload/v1742548010236/1392de34-a280-4117-9a3d-feda80392f62.png align="center")

Cela ouvrira un tableau de bord montrant des analyses descriptives complètes de votre chaîne YouTube. Cela peut devenir écrasant, car il y a beaucoup de métriques et de filtres avec divers types de données. C'est pourquoi j'ai souligné l'importance de connaître votre problème et d'identifier vos questions avant de plonger.

Vous pouvez sélectionner la plage de données qui vous intéresse en utilisant le menu déroulant de date (1 dans l'image ci-dessous) et le bouton Comparer à (2) pour comparer les données de différentes plages de dates.

![Image montrant le menu déroulant de date et le bouton Comparer à](https://cdn.hashnode.com/res/hashnode/image/upload/v1742548329162/3b8be0ea-769a-4723-b427-f911b3cfec83.png align="center")

Les en-têtes de colonne que vous voyez dans le tableau de bord sont les filtres. Chacun contient différentes métriques, et vous pouvez trouver certaines métriques dans un ou plusieurs filtres. Vous pouvez jouer avec les onglets et les menus déroulants pour mieux les comprendre.

Ceci n'est qu'une base pour comprendre les performances de votre chaîne YouTube. Si vous avez une chaîne de longue date avec un grand nombre d'abonnés et de vues, faites-moi confiance – vous pouvez obtenir beaucoup d'informations à partir de vos données.

Pour ce tutoriel, je vais sélectionner toutes mes données de durée de vie (1) et cliquer sur le bouton de téléchargement en haut à droite (2).

![Image montrant l'option de durée de vie sous le menu déroulant de date](https://cdn.hashnode.com/res/hashnode/image/upload/v1742548442210/8fbddcac-98cb-4e52-9355-5383e6afc172.png align="center")

Cela affichera deux options : ouvrir les données dans Google Sheets dans un nouvel onglet ou télécharger le fichier CSV.

![Image montrant les options de téléchargement pour ouvrir les données dans un nouvel onglet Google Sheets ou télécharger le CSV](https://cdn.hashnode.com/res/hashnode/image/upload/v1742548490620/c8829a2b-228b-45fd-8789-45dfb397f2da.png align="center")

Puisque nous voulons utiliser les données en Python, sélectionnez l'option pour télécharger le fichier CSV. Après avoir téléchargé le fichier, extrayez les fichiers du dossier zip, et dans le dossier extrait, vous verrez trois fichiers CSV : `Chart data.csv`, `Table data.csv`, et `Totals.csv`.

Pour ce tutoriel, nous nous intéressons au fichier `Table data.csv`. Cliquez sur les données pour les ouvrir et les afficher dans Excel afin de faire un peu de nettoyage manuel des données avant d'importer les données dans Python.

![Image montrant les données du tableau dans Excel](https://cdn.hashnode.com/res/hashnode/image/upload/v1742548741025/ace69aaf-bb0e-40de-aa1e-e716bb4182aa.png align="center")

Les données sont une liste de toutes les vidéos de ma chaîne YouTube, soit quarante (la vôtre peut en avoir plus ou moins). Supprimez la première ligne, qui est la ligne `Total`, et enregistrez les modifications.

Voici les colonnes du jeu de données :

* `Content` : L'identifiant de la vidéo
    
* `Video title` : Le titre de la vidéo
    
* `Video publish time` : Le jour où la vidéo a été publiée
    
* `Duration` : La durée de la vidéo en secondes
    
* `Views` : Le nombre de vues par vidéo
    
* `Watch time` : La quantité estimée de temps de visionnage de la vidéo par votre public en heures
    
* `Subscribers` : Changement dans le nombre total d'abonnés trouvé en soustrayant les abonnés perdus des abonnés gagnés pour la date et la région sélectionnées.
    
* `Average view duration` : Durée moyenne estimée de visionnage par vidéo.
    
* `Impressions` : Nombre de fois où vos vidéos ont été montrées aux spectateurs.
    
* `Impressions click-through rate (%)` : Nombre de fois où les spectateurs ont cliqué sur votre vidéo après avoir vu une impression.
    

## Étape 3 : Analyser les données en Python

Allez dans votre Jupyter Notebook et importez les bibliothèques Pandas, Seaborn et Matplotlib.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
```

Ensuite, importez le fichier `Table data.csv`.

```python
# Charger les données
df = pd.read_csv("/content/Table data.csv")
```

### Analyse de corrélation

Concernant notre énoncé de problème, nous allons tracer une [carte thermique de corrélation](https://www.quanthub.com/how-to-read-a-correlation-heatmap/) entre les variables suivantes : `Views`, `Watch time (hours)`, `Subscribers`, `Average view duration`, et `Impressions-click-through rate (%)` pour voir la force et la direction de la relation entre elles.

```python
# Convertir "Average view duration" (formaté comme H:M:S) en secondes
df['Average view duration'] = pd.to_timedelta(df['Average view duration']).dt.total_seconds()

# Sélectionner les colonnes pertinentes pour l'analyse de corrélation
correlation_data = df[['Views', 'Watch time (hours)', 'Subscribers', 'Average view duration', 'Impressions', 'Impressions click-through rate (%)']]

# Calculer la matrice de corrélation
corr_matrix = correlation_data.corr()

# Visualisation à l'aide d'une carte thermique
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Carte thermique de corrélation des analyses YouTube")
plt.show()
```

![Carte thermique de corrélation montrant la relation entre les variables sélectionnées](https://cdn.hashnode.com/res/hashnode/image/upload/v1742632975699/427811d8-09ca-4a8d-8fdc-98cdaf5b7033.png align="center")

Le coefficient de corrélation varie de -1 à 1, où les valeurs inférieures à 0 signifient une relation négative, tandis que celles supérieures à 0 signifient une relation positive. Plus la valeur est basse dans une relation négative, plus la relation négative est forte, tandis que plus la valeur est élevée dans une relation positive, plus la relation est forte.

Sur la base du graphique ci-dessus, voici les principales informations :

* **Vues et temps de visionnage** : Il y a une forte corrélation (0,94) entre les vues et le temps de visionnage, ce qui suggère que lorsque les vidéos obtiennent plus de vues, elles accumulent également plus d'heures de visionnage, proportionnellement.
    
* **Vues et impressions** : Il y a une forte corrélation (0,89) entre les vues et les impressions, indiquant que les vidéos qui sont montrées plus fréquemment dans les recommandations et les résultats de recherche tendent à obtenir plus de vues.
    
* **Durée moyenne de visionnage** : Cette métrique a des corrélations très faibles avec presque toutes les autres métriques. Elle est particulièrement notable dans les vues (0,06), les abonnés (0,01) et les impressions (0,03).
    
* **Abonnés et métriques** : Les abonnés ont une corrélation modérée à forte avec les vues (0,75) et les impressions (0,79) et une corrélation plus faible avec le taux de clics (0,54).
    
* **Taux de clics** : A des corrélations modérées avec les vues (0,69) et le temps de visionnage (0,66) mais une corrélation plus faible avec les abonnés (0,54).
    

L'information la plus significative est que la durée moyenne de visionnage semble fonctionner indépendamment des autres métriques. Cela suggère que sur ma chaîne YouTube, la capacité d'une vidéo à retenir les spectateurs tout au long de sa durée n'est pas nécessairement liée au nombre de personnes qui la regardent, à la fréquence à laquelle elle est recommandée, ou au nombre d'abonnés de la chaîne.

Cela implique que les stratégies que je mettrais en œuvre pour augmenter mes vues, abonnés et impressions pourraient différer de celles nécessaires pour améliorer la durée moyenne de visionnage, un facteur important dans l'algorithme de recommandation de YouTube. Cela signifie que je dois examiner d'autres métriques YouTube qui ont une relation avec la durée moyenne de visionnage, ce qui est un sujet pour un autre article.

### Analyse de la rétention du public

Pour analyser la rétention du public, nous devons créer une nouvelle variable `Retention Rate (%)`, qui est calculée en divisant la `Average view duration` d'une vidéo par la `Duration` et en l'exprimant en pourcentage.

```python

# Calculer le taux de rétention comme (Average View Duration / Total Video Duration) * 100
df['Retention Rate (%)'] = (df['Average view duration'] / df['Duration']) * 100
```

Ensuite, trier les vidéos par ordre croissant en fonction du `Retention Rate (%)` et afficher les 10 premières vidéos avec le taux de rétention le plus élevé.

```python
# Trier les vidéos par taux de rétention
df_sorted = df.sort_values(by='Retention Rate (%)', ascending=False)

# Afficher les 10 premières vidéos avec le taux de rétention le plus élevé
df_sorted[['Video title', 'Duration', 'Average view duration', 'Retention Rate (%)']].head(10)
```

![Image montrant les dix premières vidéos par taux de rétention](https://cdn.hashnode.com/res/hashnode/image/upload/v1742634265073/fc5bac65-18f3-467a-a8da-85f95ae00488.png align="center")

D'après le tableau ci-dessus, vous remarquerez que la plupart des vidéos dans le top 10 ne dépassent pas 503 secondes, ce qui est approximativement 8 minutes. Cela implique que mon public s'intéresse aux vidéos courtes et moyennes.

La plupart des vidéos avec un taux de rétention élevé ont une durée inférieure à 4 minutes, avec un taux de rétention allant de 27 % à 40 %. Avec cette information, je peux m'assurer que les prochaines vidéos que je téléchargerai auront une durée de 5 à 8 minutes.

Examinons les 10 vidéos avec le taux de rétention le plus faible :

```python
# Trier les vidéos par taux de rétention
df_sorted = df.sort_values(by='Retention Rate (%)', ascending=False)

# Afficher les 10 vidéos avec le taux de rétention le plus faible
df_sorted[['Video title', 'Duration', 'Average view duration', 'Retention Rate (%)']].tail(10)
```

![Image montrant les dix vidéos avec le taux de rétention le plus faible](https://cdn.hashnode.com/res/hashnode/image/upload/v1742634531458/28b1d8e8-38d9-480e-8259-a30f659386a3.png align="center")

D'après les informations ci-dessus, vous remarquerez que les longues vidéos de ma chaîne, d'une durée approximative de 22 à 58 minutes, ont un faible taux de rétention. Cela soutient davantage l'affirmation ci-dessus selon laquelle mon public s'intéresse davantage aux vidéos plus courtes.

Nous pouvons décider de tracer un graphique de dispersion de la `Duration` par rapport au `Retention Rate (%)` pour résumer les tableaux ci-dessus.

```python
# Définir le style des graphiques
sns.set_style("whitegrid")

# Tracer le taux de rétention par rapport à la durée de la vidéo
plt.figure(figsize=(12, 6))

sns.scatterplot(data=df, x='Duration', y='Retention Rate (%)', hue='Views', size='Views', sizes=(20, 200), palette='coolwarm')
plt.title("Rétention du public par rapport à la durée de la vidéo")
plt.xlabel("Durée de la vidéo (secondes)")
plt.ylabel("Taux de rétention (%)")
plt.legend(title="Vues", loc="upper right")

plt.show()
```

![Graphique de dispersion montrant la rétention du public par rapport à la durée de la vidéo](https://cdn.hashnode.com/res/hashnode/image/upload/v1742634776775/e024b61c-d86f-45d6-b8fb-13ff87e101e9.png align="center")

Le [graphique de dispersion](https://byjus.com/commerce/scatter-diagram/) ci-dessus montre la relation entre le taux de rétention du public (axe y, mesuré en pourcentage) et la durée de la vidéo (axe x, mesurée en secondes) pour diverses vidéos. Voici les principales observations :

* Il y a une corrélation négative claire entre la durée de la vidéo et le taux de rétention – lorsque les vidéos deviennent plus longues, le taux de rétention diminue généralement.
    
* Les taux de rétention les plus élevés (35-40 %) se trouvent dans les vidéos plus courtes, principalement en dessous de 500 secondes (environ 8 minutes).
    
* Les vidéos de plus de 1500 secondes (25 minutes) montrent systématiquement des taux de rétention inférieurs à 15 %.
    
* La taille et la couleur des points représentent le nombre de vues, les points plus grands et plus rouges indiquant plus de vues (jusqu'à 1000) et les points plus petits et bleus représentant moins de vues (environ 200).
    
* Intéressamment, certaines vidéos de durée moyenne (environ 500 secondes) ont à la fois un nombre de vues plus élevé (indiqué par des points rouges plus grands) et des taux de rétention décents d'environ 25 %.
    
* La vidéo la plus longue du jeu de données (environ 3500 secondes ou 58 minutes) a un taux de rétention d'environ 14 % et relativement peu de vues.
    

Ce graphique confirme davantage l'affirmation selon laquelle les vidéos plus courtes tendent à mieux maintenir l'attention du public sur ma chaîne, bien que certaines vidéos de durée moyenne puissent encore bien performer en termes de rétention et de nombre de vues.

## Conclusion

Ce que nous avons appris de mes données n'est que la partie émergée de l'iceberg. YouTube dispose de nombreuses métriques, et comme ma chaîne n'est pas monétisée et a peu d'abonnés et de vidéos, je n'ai pas de données sur la monétisation, les démographiques et autres métriques.

Mais après avoir lu cet article, j'espère que vous pouvez penser à une infinité d'informations que vous souhaitez obtenir sur la base de ces métriques. Vous pouvez même prévoir vos vues, le nombre d'abonnés et les revenus pour les prochains jours ou mois. Vous pouvez également effectuer une analyse de séries temporelles multivariées pour voir comment ces facteurs affectent votre variable principale d'intérêt.

Si vous trouvez cet article intéressant, n'oubliez pas de consulter mon [blog](https://learndata.xyz/blog) pour d'autres articles intéressants, suivez-moi sur [Medium](https://medium.com/@adejumo999), connectez-vous sur [LinkedIn](https://www.linkedin.com/in/adejumoridwan/), et abonnez-vous à ma [chaîne YouTube](http://www.youtube.com/@learndata_xyz).