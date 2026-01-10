---
title: 'Projet de science des données en conditions réelles : analyse des accidents
  de la circulation'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-06T14:49:58.000Z'
originalURL: https://freecodecamp.org/news/real-world-data-science-project-traffic-accident-analysis-e5a36775ee11
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ip96iQ8qKQMwTHVLPEtlRA.gif
tags:
- name: data
  slug: data
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: 'Projet de science des données en conditions réelles : analyse des accidents
  de la circulation'
seo_desc: 'By Hari Santanam

  Using Python and Folium to clean, analyze and visualize state traffic accident data


  Driving in the snow. GIF and source: mine :).

  I love data science, data visualization and analysis. Recently, I researched a project
  that piqued my ...'
---

Par Hari Santanam

#### **Utilisation de Python et Folium pour nettoyer, analyser et visualiser les données d'accidents de la circulation de l'État**

![Image](https://cdn-media-1.freecodecamp.org/images/dpQTvfPZcdokKIaheHQUe2tsMWzWrtwXB3-B)
_Conduite dans la neige. GIF et source : les miens :)._

J'adore la science des données, la visualisation et l'analyse des données. Récemment, j'ai étudié un projet qui a piqué ma curiosité — les accidents de la circulation à l'échelle de l'État.

Les processus et tâches de science des données en conditions réelles sont des choses que les scientifiques des données (au sens large) doivent faire. Cela inclut la collecte, la collation, le nettoyage, l'agrégation, l'ajout et la suppression de parties des données. Cela inclut également la décision de la manière d'analyser les données.

Et ce n'est que la première partie ! Après cela, ils doivent décider comment présenter les résultats.

Cela dit, voici ce que j'ai fait dans un projet récent.

J'ai collecté des données sur les accidents de la circulation de l'État du New Jersey (NJ), aux États-Unis, pour l'année 2017. C'était la dernière année pour laquelle des données étaient disponibles sur le site web du gouvernement de l'État du NJ.

Je suis heureux de la politique ouverte de partage des données avec les citoyens, bien que l'organisation des données soit quelque peu étrange (mon opinion !), et ce n'est pas, comme on pourrait s'y attendre, simple.

Voici les étapes que j'ai suivies pour le projet :

* J'ai collecté, nettoyé et analysé les données.
* Les données devaient être divisées en deux sous-ensembles. Un ensemble avait des coordonnées géographiques exactes, l'autre non.
* J'ai recueilli des informations et préparé les données.
* J'ai créé des cartes thermiques — statiques et avec le temps — qui montrent les accidents par lieu, pour l'année, sur une carte du NJ, pour la visualisation.

Avant d'aller plus loin, je vais fournir un peu de contexte à ceux qui ne sont peut-être pas familiers avec la géographie de la région.

L'État du New Jersey est situé à l'ouest de New York et s'étend vers l'ouest et le sud (et un peu vers le nord).

En gros, les conducteurs allant de New York directement vers le reste des États-Unis (sauf vers le nord, vers la région de la Nouvelle-Angleterre et le Canada) en automobile doivent passer par le NJ. L'État dispose d'un excellent réseau d'autoroutes. Il a également une population dense de banlieues, et une fois que vous avez passé de nombreux kilomètres de vieilles villes étroitement liées, il y a des zones suburbaines, pastorales et même rurales.

#### **Préparation et nettoyage des données**

Voici les étapes que j'ai suivies pour nettoyer et préparer l'ensemble de données :

* **Recherche et étude des données.** J'ai obtenu les données à partir du site web du gouvernement de l'État du New Jersey. La latitude et la longitude (Lat, Long) sont des points de coordonnées géographiques qui peuvent cartographier des emplacements sur n'importe quel point de la Terre. Lisez [ici](https://en.wikipedia.org/wiki/Geographic_coordinate_system#Latitude_and_longitude) pour plus d'informations à leur sujet.
* J'ai utilisé les données récapitulatives pour l'ensemble de l'État pour 2017, la dernière année pour laquelle des données sont disponibles.
* Il y a un fichier séparé qui liste les en-têtes et leurs descriptions. J'ai copié le fichier d'en-tête dans Excel, l'ai analysé, puis l'ai collé en utilisant un éditeur de texte.

![Image](https://cdn-media-1.freecodecamp.org/images/4Wk27IZIsWA2gY7px6TGwcyX4JsXA1PMXRwc)
_Le fichier d'en-tête — je l'ai copié du pdf dans Excel puis analysé._

![Image](https://cdn-media-1.freecodecamp.org/images/34olwsCiiRdkTQenOhtrEePYzyPWXj4c9BhS)
_2ème étape : Suppression de certains éléments, sauvegarde en fichier csv._

Que révèlent ces étapes ?

Sur environ 277 000 lignes, seulement 70 000 avaient des coordonnées de latitude et de longitude (soit environ 26 %).

Cela posait un défi. Après tout, l'objectif du projet est de produire une représentation visuelle superposée des données d'accidents à travers le NJ. Voici ce que j'ai fait :

J'ai séparé les lignes sans coordonnées Lat, Long dans un nouveau dataframe pandas. Ces lignes avaient un nom de ville, donc j'ai décidé de faire une carte thermique séparée pour les villes de ces données.

Il y a donc deux ensembles de cartes thermiques : un pour le jeu de données avec des coordonnées précises de latitude et de longitude, l'autre pour les autres données avec seulement des informations sur la ville.

J'ai écrit un peu de code pour obtenir les coordonnées de latitude et de longitude des villes pour ces données. Maintenant, ce jeu de données est beaucoup plus grand, représentant 74 % des données totales ! Ce sont des données réelles — souvent incomplètes et nécessitant un nettoyage et une préparation.

Voir l'extrait de code d'initialisation ci-dessous.

```
#TSB - Importation des outils, lecture du fichier, préparation des données#les noms de colonnes sont dans un fichier différent (pdf), ils doivent donc être définis ici
```

```
#outils nécessaires pour dessiner la carte avec les données superposées
```

```
import folium                    import folium.plugins as pluginsfrom folium.plugins import HeatMapWithTime
```

```
import pandas as pdcolumn_names =['Mumbo-jumbo','Nom du comté','Nom de la municipalité','Date de l'accident','Jour de la semaine de l'accident','Heure de l'accident','Code du département de police','Département de police','Poste de police','Total des morts','Total des blessés',              'Piétons tués','Piétons blessés','Gravité','Intersection','Alcool impliqué','Matières dangereuses impliquées','Code de type d'accident','Total des véhicules impliqués','Lieu de l'accident','Direction du lieu',               'Route','Suffixe de la route','SRI (Identifiant de route standard)','MilePost','Système routier','Caractère de la route','Alignement horizontal de la route','Pente de la route','Type de surface de la route','Condition de la surface','Condition d'éclairage',               'Condition environnementale','Route divisée par','Zone de contrôle du trafic temporaire','Distance jusqu'à la rue transversale','Unité de mesure','Direction depuis la rue transversale','Nom de la rue transversale',               'Est une bretelle','Nom de la route de la bretelle vers/depuis','Direction de la route de la bretelle vers/depuis','Vitesse affichée','Vitesse affichée de la rue transversale','Premier événement dommageable','Latitude','Longitude',               'Indicateur d'utilisation du téléphone portable','Autres dommages matériels','Numéro de badge du rapport']#lire le fichier et le charger dans un dataframe df1 = pd.read_csv('/content/drive/My Drive/Colab/NewJersey2017Accidents.txt', header=None)
```

La première étape (définition de l'ensemble de données et chargement du contenu) est maintenant terminée.

Maintenant, le vrai travail commence. Voyons combien de contenu manque de valeurs de latitude et de longitude nécessaires pour faire fonctionner la carte.

Nous allons conserver les enregistrements avec de bonnes valeurs dans le premier dataframe `df1` et prendre les enregistrements sans valeurs Lat, Long dans un ensemble de données différent `df2`,

Pour cela, je vais essayer d'obtenir les noms des villes afin de pouvoir identifier, sur une carte différente, les taux d'accidents dans ces villes sans emplacements de rues spécifiques.

Le code ci-dessous permettra d'y parvenir.

```
#convertir le champ 'Date de l'accident' en format mois/jour/année lisible par pandas df1['Date de l'accident'] = pd.to_datetime(df1['Date de l'accident'], format = '%m/%d/%Y')
```

```
#convertir les colonnes Latitude, Longitude de chaîne en numérique cols_to_convert = ['Latitude', 'Longitude'] for col in cols_to_convert:  df1[col] = pd.to_numeric(df1[col], errors='coerce')
```

```
#Les valeurs de longitude dans les données originales n'avaient pas le signe négatif (-) #le code ci-dessous corrige cela en remplaçant toutes les valeurs Lat par #Lat * -1. Sans cela, la carte affiche une partie totalement différente #du monde ! df1['Longitude']=df1['Longitude']* -1
```

```
#mettre tous les enregistrements sans données (NaN) pour Lat et Long dans un #dataframe séparé (df2) df2 = df1.loc[df1.Latitude.isnull()] #df2 = df1.loc[df1.Latitude.isnull()] & df1.loc[df1.Longitude.isnull()] df2.shape #df2.head()
```

```
#supprimer les enregistrements avec NaN dans Lat et Long de df1 (ils sont sauvegardés #ci-dessus dans df2) df1 = df1.dropna(subset=['Latitude','Longitude']) df1.shape print(df1.dtypes)
```

![Image](https://cdn-media-1.freecodecamp.org/images/vwMcDi3Sut6TL87If-093BjD1qUCB8QYj2ky)
_la sortie de df1.dtypes montre chaque type de colonne dans le dataframe_

```
#exécuter quelques requêtes sur le dataframe 1 (avec Lat, Long disponibles) #lister les accidents où une ou plusieurs personnes sont tuées — très graves #ne montre pas la sortie ici, trop longue print(df1.loc[(df1['Total des morts'] >= 1.0), ['Nom de la municipalité','Latitude','Longitude', 'Total des morts']])
```

```
#montrer les accidents impliquant l'utilisation d'un téléphone portable print(df1.loc[(df1['Indicateur d'utilisation du téléphone portable'] == 'Y'),['Vitesse affichée','Poste de police','Latitude','Longitude']])
```

```
#montrer les accidents le vendredi print(df1.loc[(df1['Jour de la semaine de l'accident'] == 'FR'),['Nom de la municipalité','Vitesse affichée','Poste de police','Latitude','Longitude']])
```

```
#montrer les accidents pour une ville spécifique et une limite de vitesse print(df1.loc[(df1['Nom de la municipalité'] == 'WATCHUNG BORO'), ['Nom de la municipalité','Vitesse affichée','Poste de police','Latitude','Longitude']])
```

#### **Créer des cartes thermiques**

Obtenons l'emplacement superposé sur une carte thermique. Nous pouvons également créer une carte thermique pour montrer les changements au fil du temps.

```
#définir une fonction de génération de carte de base #note - si folium ne fonctionne pas correctement (ce n'était pas le cas, au début, pour moi #:) - dans Google Colab - J'ai désinstallé Folium, redémarré le noyau et #réinstallé Folium #J'ai également sauvegardé dans un fichier car l'exécution n'a pas produit de résultats
```

```
def generateBaseMap(default_location=[40.5397293,-74.6273494], default_zoom_start=12):    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)    return base_map
```

```
base_map = generateBaseMap() base_map
```

```
#appliquer la carte thermique à la carte de base ci-dessus et sauvegarder 'm' (sortie)  # dans un fichier. Comme expliqué en haut des notes de code, Exécuter n'a pas #fonctionné pour moi. J'ai ouvert le fichier sauvegardé dans le navigateur pour voir la sortie
```

```
m = HeatMap(data=df_map[['Latitude', 'Longitude', 'count']].groupby(['Latitude','Longitude']).sum().reset_index().values.tolist(), radius=7, max_zoom=10).add_to(base_map) m.save('/content/drive/My Drive/Colab/heatmap.html')
```

![Image](https://cdn-media-1.freecodecamp.org/images/5An1TqgEkEN2Ea3jCSLrlLjK9jFbBNN-UDxn)
_Carte thermique des accidents de la circulation pour 2017 pour tout le NJ, vue compressée. Quelques-uns ont de mauvaises coordonnées (certains sont dans l'océan, certains ne sont pas dans le NJ), comme vous pouvez le voir :) — problème de données du monde réel._

![Image](https://cdn-media-1.freecodecamp.org/images/p88k4orpUxRTTA4OPzAqGBH8htM20RYQ7POw)
_Carte thermique, étendue, des accidents de la circulation de 2017._

C'est bien — maintenant, regardons une carte thermique au fil du temps.

```
from folium.plugins import HeatMap #d'abord, copier toutes les données [tous les accidents de comté de 2017] dans notre carte #dataframe df_map = df1.copy()
```

```
#définir le champ count à 1 initialement. Ensuite, regrouper par Lat, Long et compter #combien sont dans chaque ensemble de coordonnées pour créer les données de la carte de base
```

```
df_map['count']=1 df_map[['Latitude', 'Longitude', 'count']].groupby(['Latitude', 'Longitude']).sum().sort_values('count', ascending=False).head(10)
```

```
base_map = generateBaseMap() base_map m = HeatMap(data=df_map[['Latitude', 'Longitude', 'count']].groupby(['Latitude','Longitude']).sum().reset_index().values.tolist(), radius=7, max_zoom=10).add_to(base_map) m.save('/content/drive/My Drive/Colab/heatmap_with_time-1.html')
```

![Image](https://cdn-media-1.freecodecamp.org/images/44QVTHKYMkiFF4X2VNwJ1ByQeDW50Yx3nAgy)
_Carte thermique avec le temps — éditée et montrée en GIF. Montre essentiellement la concentration des accidents par lieu et jour pour 2017. Remarquez les contrôles, étendus ci-dessous. Les zones peuplées (Nord du NJ, près de NYC, et Sud du NJ, près de Philadelphie) et les principaux corridors de transit ont des taux d'accidents plus élevés, comme prévu._

![Image](https://cdn-media-1.freecodecamp.org/images/xjwMOZhXTNDUx8ciFpMLBJ8j1gXkIZZd5wSw)
_Contrôles sur le fichier de sortie (rendu dans le navigateur) — contrôles de vitesse et boutons de lecture. Le '83' est le jour dans cet exemple._

### **Partie 2 — Création de cartes thermiques du deuxième jeu de données**

Plus tôt, nous avons divisé le jeu de données et créé un jeu de données `df2` pour les enregistrements sans coordonnées spécifiques de latitude et de longitude.

Les raisons de cela peuvent être nombreuses. Peut-être que les données ont été contaminées au moment de la capture, ou les officiers de police étaient trop occupés par les devoirs de premiers intervenants pour saisir des informations précises.

Quelle que soit la raison, obtenons les données de localisation pour les villes. Cela s'est avéré plus compliqué que je ne l'avais imaginé. Il se peut simplement que je n'aie pas pensé à une méthode optimale. C'est la manière dont je l'ai fait.

Dans les situations de travail réelles, de nombreuses fois, vous devrez opter pour la « solution la plus viable », ce qui signifie la meilleure possible étant donné le temps, les contraintes environnementales et les données incomplètes.

```
#créer une liste de noms de villes uniques à partir de df2 pour une utilisation ultérieure afin de faire un #appel à une fonction pour obtenir Lat, Long — facile à lire chaque valeur à partir d'une #liste town_names=[] df2.dropna(subset=['Nom de la municipalité']) town_names = df2['Nom de la municipalité'].unique() print(town_names)
```

Voici ce que nous faisons dans les prochaines étapes. Prenez la liste des noms de villes uniques que nous venons de créer. Ensuite, utilisez une fonction pour faire un appel d'API à `maps.google` afin d'obtenir les coordonnées de latitude et de longitude.

Prenez le dataframe avec les taux d'accidents par ville (regroupés) et fusionnez-le avec la liste qui contient les coordonnées de latitude et de longitude créées à l'étape précédente.

Ensuite, appelez la fonction de traçage pour créer une carte thermique comme nous l'avons fait auparavant pour le premier jeu de données.

```
#appeler une fonction créée précédemment (listée dans le gist — le lien est #ci-dessous cette boîte de code et la sortie), puis stocker les coordonnées géo de google #dans un fichier csv.
```

```
#Assurez-vous d'avoir un jeton API : cliquez sur le lien pour savoir comment : #Jeton API Google maps Lat_Long=[] API_KEY = 'VOTRE CLÉ API ICI' for address in town_names:    geocode_result = get_google_results(address, API_KEY, return_full_response=RETURN_FULL_RESULTS)    Lat_Long.append(geocode_result)
```

```
#maintenant, convertir la liste avec nos coordonnées géographiques en un fichier csv qui #sera appelé par un autre programme pour superposer sur une carte. pd.DataFrame(Lat_Long).to_csv('../Colab/town_with_Lat_Long_output.csv', encoding='utf8')
```

```
#lire le fichier csv qui contient la latitude et la longitude pour les #enregistrements dans df2, qui n'avaient pas à l'origine de lat et long df6 = pd.read_csv('/content/drive/My Drive/Colab/town_with_Lat_Long_output.csv') df6.shape
```

```
#fusionner les deux ensembles de données - un a les noms de villes et les coordonnées géographiques, #l'autre a les noms de villes et les informations agrégées sur les accidents
```

```
df7 = pd.read_csv('/content/drive/My Drive/Colab/df5_output.csv') dfinal = df6.merge(df7, on="Nom de la municipalité", how = 'inner')
```

```
#maintenant, nous traçons enfin la carte thermique pour le deuxième jeu de données !
```

```
from folium.plugins import HeatMap def generateBaseMap(default_location=[40.5397293,-74.6273494], default_zoom_start=12):    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)    return base_map
```

```
base_map = generateBaseMap() base_map m = HeatMap(data=dfinal[['latitude', 'longitude', 'count']].groupby(['latitude','longitude']).sum().reset_index().values.tolist(), radius=7, max_zoom=10).add_to(base_map) m.save('/content/drive/My Drive/Colab/heatmap_town_total_accidents_2017.html')
```

![Image](https://cdn-media-1.freecodecamp.org/images/PFrrM7pJr04ll92s3r6-UtEsJnSrD5Ea12YT)
_Carte thermique pour le deuxième jeu de données (villes). Similaire à l'autre carte, les banlieues du nord et du sud avec des populations plus élevées et à proximité de grandes villes ont des taux d'accidents plus élevés._

Le gist pour le code est [ici](https://gist.github.com/HariSan1/0245dca9ba3b32caf9b59ff81a4bd9b5).

Merci d'avoir lu jusqu'au bout. Si vous êtes novice, chaque projet de science des données est une aventure — accrochez-vous. Des problèmes inattendus (et attendus) surgiront — mais aussi votre ingéniosité, votre talent et l'application des expériences d'autres codeurs, pour obtenir les solutions que vous cherchez.

Veuillez m'applaudir si vous avez aimé l'article !