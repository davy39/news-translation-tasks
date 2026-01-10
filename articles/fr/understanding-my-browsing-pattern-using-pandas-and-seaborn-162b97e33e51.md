---
title: Comprendre mon comportement de navigation en utilisant Pandas et Seaborn
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-30T19:29:56.000Z'
originalURL: https://freecodecamp.org/news/understanding-my-browsing-pattern-using-pandas-and-seaborn-162b97e33e51
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Ag762hM4z29h33Pf_pkIWA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comprendre mon comportement de navigation en utilisant Pandas et Seaborn
seo_desc: 'By Kartik Godawat


  By three methods we may learn wisdom. First, by reflection, which is noblest; Second,
  by imitation, which is easiest; and third by experience, which is the bitterest.
  — Confucius


  For the purpose of tracking the time I spend on a b...'
---

Par Kartik Godawat

> Par trois méthodes nous pouvons apprendre la sagesse. Premièrement, par la réflexion, qui est la plus noble ; deuxièmement, par l'imitation, qui est la plus facile ; et troisièmement par l'expérience, qui est la plus amère. — Confucius

Pour suivre le temps que je passe sur un navigateur, j'utilise l'extension [Limitless](https://chrome.google.com/webstore/detail/be-limitless/jdpnljppdhjpafeaokemhcggofohekbp?hl=en) sur Chrome. Bien qu'elle me donne le temps passé sous différentes catégories, j'ai pensé qu'il pourrait être utile d'inspecter toutes mes données de navigation de l'année passée.

Voici le début de ma quête pour comprendre _tout ce qu'il y avait_ dans mes données de navigation.

Dans ce processus, j'ai utilisé Pandas et Seaborn. [Pandas](https://pandas.pydata.org/) est une bibliothèque Python pour la manipulation et l'analyse de données. [Seaborn](https://seaborn.pydata.org) est construit sur matplotlib, ce qui rend la création de visualisations plus facile que jamais.

#### Obtenir les données d'historique

La première étape du processus a été d'obtenir toutes les données de navigation de l'année passée. Google Chrome stocke les trois derniers mois d'historique sur un appareil au format SQLite, mais j'ai fini par exporter mes données suivies par Google en utilisant [Google TakeOut](http://takeout.google.com). Le fichier JSON exporté contient mon historique de navigation sur tous les appareils, y compris mobile.

L'historique stocké par Chrome ou suivi par Google ne me donne pas les informations de session, c'est-à-dire le temps passé sur chaque onglet. Mon analyse est donc principalement axée sur le nombre de visites et l'heure de visite plutôt que sur la session ou la durée. Une partie de moi est soulagée, en fait, de savoir que Google ne le suit pas _encore_.

Une fois les données téléchargées, j'ai commencé par charger les données dans un dataframe Pandas :

```
import pandas as pd
with open("BrowserHistory.json") as f:
    data = json.loads(f.read())
    df = pd.DataFrame(data["Browser History"])
```

```
# Un paramètre possible si une différenciation est nécessaire entre différents clients
df.drop('client_id', axis=1, inplace=True)
df.drop('favicon_url', axis=1, inplace=True)
df.sample(1)
```

Voici à quoi ressemble la sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/YA-NrAjL7fL7vNCLCI-qL2ljqXb7dfPBZTq2)

_page_transition :_ Contient des informations sur le type de page ouverte comme le rechargement, la frappe et l'entrée, l'ouverture de lien, etc. J'ai été satisfait en filtrant uniquement sur LINK et TYPED

```
df = df[(df['page_transition'] == "LINK") | (df['page_transition'] == "TYPED")]
```

#### Extraction/Extrapolation de nouvelles colonnes (caractéristiques) :

Pour commencer, j'avais besoin de convertir le temps (en microsecondes) en un format datetime lisible par l'homme. Ensuite, j'avais besoin d'extraire des caractéristiques comme l'heure, le jour, le mois ou le jour de la semaine. À partir du champ URL, extraire le domaine de premier niveau pourrait être un champ utile pour l'analyse. J'ai donc utilisé [tldextract](https://github.com/john-kurkowski/tldextract) pour créer une nouvelle colonne de domaine dans le dataframe.

```
def convert_time(x):
    return datetime.datetime.fromtimestamp(x/1000000)
```

```
days_arr = ["Mon","Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
def get_day_of_week(x):
    return days_arr[x.weekday()]
```

```
def get_domain(x):
    domain = tldextract.extract(x)[1]
    sub_domain = tldextract.extract(x)[0]
    if sub_domain == "mail":
        return sub_domain + "." + domain
    # Solution temporaire pour différencier drive.google.com et google.com
    if domain == "google" and sub_domain=="www":
        return "google_search"
    return domain
```

```
# La colonne time_usec est sélectionnée et pour chaque ligne, convert_time(row) est appelée. Le résultat est stocké dans le même dataframe sous la colonne dt
df['dt'] = df['time_usec'].apply(convert_time)
...
df['domain'] = df['url'].apply(get_domain)
```

Ensuite, j'ai extrapolé les informations de domaine pour regrouper les domaines bien connus dans une ou plusieurs catégories (compartiments) définies par moi :

```
def get_category(x):
    if x in ["coursera", "kadenze", "fast", "kaggle", "freecodecamp"]:
        return "Learning"
    elif x in ["ycombinator", "medium", "hackernoon"]:
        return "TechReads"
    ...
    else:
        return "Other"
```

```
# Regrouper les domaines populaires dans une catégorie
df['category'] = df['domain'].apply(get_category)
```

Après toutes les opérations, le dataframe contient maintenant les colonnes suivantes et l'analyse de base pouvait commencer.

**Colonnes disponibles :** title,date,hour,month,is_secure,is_weekend,day_of_week,domain,category

### Explorer les données et créer des visualisations

#### Utilisation sécurisée vs non sécurisée :

Une fois que j'ai un dataframe avec quelques colonnes numériques et catégorielles (mois), créer un graphique est super facile.

```
import seaborn as snssns.countplot(x="month", hue="is_secure", data=df)
```

![Image](https://cdn-media-1.freecodecamp.org/images/uegjuXfIh-7mrHWSIKdSoPeyOcNdtdai1YzK)
_Tendance à la baisse pour les sites web uniquement en http lors de la navigation récente_

```
# Inspection manuelle, sélection de 50 domaines aléatoires qui n'étaient pas sécurisés
random.sample(df[df["is_secure"] == "N"].domain.unique(), 50)
```

```
# Pour afficher les données pour de tels domaines
df[(df["domain"] == "mydomain") & (df["is_secure"] == "N")]["url"]
```

Après avoir examiné quelques-unes de ces visites, j'ai fini par vérifier [ce](http://www.girnationalpark.co.in/girsafari/) site. Il **demande un numéro de passeport ou d'Aadhar (équivalent indien du SSN), ainsi qu'un email et un mobile, lors de la réservation d'un safari dans la jungle, via HTTP.** Je n'ai pas remarqué cela plus tôt ! La réservation finale est gérée via une passerelle sécurisée et distincte. Cependant, je me sentirais beaucoup plus en sécurité en tapant mes données démographiques et les détails de mon passeport via HTTPS.

Au lieu d'explorer manuellement les lignes, une solution plus stricte pourrait être d'ajouter tous ces domaines à une extension comme [BlockSite](https://chrome.google.com/webstore/detail/block-site-website-blocke/eiimnmioipafcokbfikbljfdeojpcgbh?hl=en). Ils pourraient être activés au besoin.

#### Utilisation du navigateur en semaine vs le week-end :

```
#is_weekend="Y" pour samedi et dimanche, "N" sinon
sns.countplot(x="hour", hue="is_weekend", data=df)
```

![Image](https://cdn-media-1.freecodecamp.org/images/GU7zJ5c5iZlF8uSdCFdkVb9BHVGH6H5WIIvL)
_Indicateur que je dors plus longtemps le week-end :P_

#### Utilisation du navigateur sur plusieurs mois :

Pour y parvenir, j'ai sélectionné un sous-ensemble de lignes en fonction de la condition du mois, puis j'ai tout regroupé par heure et date, pour former une visualisation de type heatmap GitHub.

```
from matplotlib import pyplot as plt
```

```
# Obtenir des valeurs uniques après regroupement par heure et date
df_new = df[(df["month"] >= 11)].groupby(["hour", "date"])["domain"].size()
df_new = df_new.reset_index(name="count")
```

```
plt.figure(figsize = (16,5))
```

```
# Pivoter le dataframe pour créer une matrice [heure x date] contenant des comptes
sns.heatmap(df_new.pivot("hour", "date", "count"), annot=False, cmap="PuBuGn")
```

![Image](https://cdn-media-1.freecodecamp.org/images/MWUr2PnFaw8DdH6sH-daaQPSbPwA1Mi5ofwo)
_Les lignes verticales vides signifient que j'étais soit en vacances, soit que je n'utilisais pas le navigateur Chrome._

Le code ci-dessus peut facilement être filtré. Cela peut être fait en ajoutant plus de conditions pour identifier les horaires d'ouverture d'onglets productifs vs non productifs et pour voir les schémas sur plusieurs jours. Par exemple :

```
cat_arr = ["Shopping", "TravelBookings", "YouTube", "Social"]
```

```
df_new = df[(df["category"] in cat_arr)].groupby(["hour", "date"])["domain"].size()
```

#### Visites du navigateur par jour de la semaine et heure :

J'ai créé un autre type de heatmap agrégée où j'ai essayé de visualiser par rapport aux heures et au jour de la semaine.

```
df_heat = df.groupby(["hour", "day_of_week"])["domain"].size().reset_index()
df_heat2 = df_heat.pivot("hour", "day_of_week", "domain")
sns.heatmap(df_heat2[days_arr] , cmap="YlGnBu")
```

![Image](https://cdn-media-1.freecodecamp.org/images/md9YvYsDlyvOm-lt74KFkUSPoD8PBtpIjPQI)
_Heures productives de la semaine de 10h à 16h avec un grand nombre de visites sur le navigateur les soirs de jeudi_

On pourrait s'attendre à une utilisation légère du vendredi après 17h jusqu'au lundi matin. Mais ce qui était intéressant pour moi de réfléchir, c'était les zones de couleur claire les soirs de mercredi.

Maintenant, pour utiliser les catégories personnalisées que j'ai manuellement regroupées pour les domaines. Je génère à nouveau la même heatmap. Mais maintenant avec une condition sur les sites de shopping populaires. Notez que la liste est créée manuellement par moi en fonction de ma mémoire et de quelques regards aléatoires sur les domaines uniques que j'ai visités.

```
df_heat = df[df["category"] == "Shopping"].groupby(["hour", "day_of_week"])["category"].size().reset_index()
```

![Image](https://cdn-media-1.freecodecamp.org/images/9Nafi1Ehl3rFMRAL5cOhQy1oFhEXWjxxT0dF)

C'est bien d'avoir la satisfaction que je ne fais généralement pas de shopping effréné pendant les heures de bureau. Cependant, le graphique m'a encouragé à explorer manuellement le jeudi (20:00–21:00) et le vendredi (15:00–16:00, 00:00–01:00). À un niveau plus élevé, j'étais très confiant de ne jamais faire de shopping pendant les heures de bureau. Cependant, la heatmap montre quelques instances de telles visites, brisant mes illusions.

#### Questions StackOverflow les plus revisitées :

Un bon ami m'a dit un jour :

> Comprendre l'utilisation de StackOverflow vous aide à comprendre soit vos domaines d'amélioration, soit les configurations/syntaxes que vous devriez vous rappeler.

Dans tous les cas, il est bon de jeter un coup d'œil aux visites les plus fréquentes pour chaque mois/trimestre.

```
df_so = df[df["domain"] == "stackoverflow"].groupby(["url", "title"]).size()
df_so = df_so.reset_index(name='count').sort_values('count',ascending=False)[["title", 'count']]
```

```
df_so.head(15)
```

![Image](https://cdn-media-1.freecodecamp.org/images/wIQT4eK6PSmKyUnpS7ytYzuuht482UI0GW1o)
_Les lignes intitulées « Newest question » et None montrent qu'il y a place pour le prétraitement des données dans ce contexte_

Peut-être devrais-je mettre en cache la page qui me montre comment itérer sur un dataframe Pandas !

En dehors de StackOverflow, l'un de mes sites les plus visités liés à Pandas serait [les notes de Chris Albon sur Python et la manipulation de données](https://chrisalbon.com/#python).

En général, il est très intéressant d'observer comment vos pages les plus visitées changent de thème au fil des mois. Par exemple, elles peuvent passer de questions simples à des questions plus complexes et plus profondes. Cela est vrai à mesure que vous construisez votre compréhension vers quelque chose de nouveau.

Enfin, juste pour le plaisir, j'ai fini par concaténer les titres de toutes mes recherches StackOverflow de l'année passée. J'ai ensuite généré un [nuage de mots](https://github.com/amueller/word_cloud) d'aspect décent à partir de celui-ci.

![Image](https://cdn-media-1.freecodecamp.org/images/vJmTP5yIcxmdjD887Avv-9REXxDs8TIpoXPX)

Merci beaucoup pour votre temps. Si vous avez aimé lire, veuillez m'applaudir afin que plus de personnes voient l'article. Merci ! Et, jusqu'à la prochaine fois, passez une excellente journée :)

Un notebook fonctionnel est présent sur [GitHub](https://github.com/daerty0153/visualize-browser-history) avec quelques visualisations supplémentaires et quelques astuces rapides autour des données. N'hésitez pas à l'essayer avec votre propre historique et à partager des insights intéressants !