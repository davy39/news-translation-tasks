---
title: Comment utiliser les données pour découvrir les secrets du baseball
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-27T22:55:23.000Z'
originalURL: https://freecodecamp.org/news/discovering-the-secrets-of-baseball-with-data-56f793852de0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t6bdAIXvBropF4AMwTP9Jg.jpeg
tags:
- name: baseball
  slug: baseball
- name: data analysis
  slug: data-analysis
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les données pour découvrir les secrets du baseball
seo_desc: 'By ?? Anton de Regt

  Data can tell lots of stories, and finding the hidden secrets is like finding a
  needle in a haystack.

  After finishing my first data analysis course on Udacity, it was time for a real-world
  project.

  In this project, I’m going to ex...'
---

Par ?? Anton de Regt

Les données peuvent raconter beaucoup d'histoires, et trouver les secrets cachés revient à chercher une aiguille dans une botte de foin.

Après avoir terminé mon premier cours d'analyse de données sur [Udacity](https://classroom.udacity.com/courses/ud170), il était temps pour un projet concret.

Dans ce projet, je vais explorer les données du baseball. Plus précisément : les données de frappe pour chaque joueur ayant joué entre 1871 et 2016. Vous pouvez télécharger l'ensemble du jeu de données [ici](http://www.seanlahman.com/baseball-archive/statistics/).

Mon processus :

1. Jeter un premier coup d'œil aux données
2. Formuler une question
3. Nettoyer les données
4. Explorer les données
5. Tirer des conclusions/prédictions
6. Communiquer mes résultats

Mon objectif est de trouver les secrets du baseball dans les données et de les partager avec vous, afin que vous puissiez apprendre quelque chose et améliorer votre jeu.

[antonderegt/data-baseball](https://github.com/antonderegt/data-baseball/blob/master/Baseball%20Project.ipynb)
[data-baseball — Un projet final d'Udacitygithub.com](https://github.com/antonderegt/data-baseball/blob/master/Baseball%20Project.ipynb)

### Premier coup d'œil aux données

La première étape consiste à importer un jeu de données. Pour ce premier aperçu, je vais afficher les cinq premières entrées pour avoir une idée de ce avec quoi je travaille.

```
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
%matplotlib inline
```

```
# Lecture des données de frappe
filename = 'Batting.csv'
batting_df = pd.read_csv(filename)
```

```
# Affichage des cinq premières entrées
batting_df.head()
```

```
# Obtention de quelques métriques sur les coups de circuit, le nombre de matchs, les points battus et le nombre de retraits sur prises
batting_df[['HR','G', 'RBI', 'SO']].describe()
```

En regardant le tableau ci-dessus, il semble que les batteurs frappent en moyenne 2,8 coups de circuit par saison avec une moyenne de 51 matchs.

```
batting_df_groupedby_year = batting_df.groupby(['yearID']).sum()
homeruns_per_year = batting_df_groupedby_year[['HR']]
```

```
# Tracé de la heatmap dans l'ordre inverse pour faciliter la visualisation des augmentations
sns.heatmap(homeruns_per_year.iloc[::-1])
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*a-xusvHac4NFo_4FVWzYew.png)
_Tracé de la heatmap_

Ci-dessus, vous pouvez voir le nombre de coups de circuit augmenter au fil des années. Sur l'axe des y de gauche, vous pouvez voir l'année, et sur l'axe des y de droite, vous pouvez voir le nombre de coups de circuit.

### Questions

Avant que les données ne révèlent leurs secrets, je dois leur poser quelques questions. Voici quelques exemples de questions que je peux poser aux données :

1. Quelles équipes ont les batteurs les plus efficaces ?
2. Y a-t-il une corrélation entre les retraits sur prises et les coups de circuit ?
3. Qui est le meilleur voleur de l'histoire (Caught Stealing vs. Stolen Bases) ?
4. Quelle région produit les meilleurs batteurs (il faut fusionner avec une autre table pour cela) ?
5. Quelle est la relation entre différentes métriques de performance ? Certaines ont-elles une relation négative ou positive forte ?
6. Quelles sont les caractéristiques des joueurs de baseball avec les salaires les plus élevés ?

La question sur laquelle je vais me concentrer est : quelles métriques sont corrélées et quelles métriques ne le sont pas ?

### Nettoyage

```
# Affichage des données de frappe pour les dix dernières années
batting_last_ten_years = batting_df.groupby(['yearID'], as_index=False).sum().sort_values(by='yearID', ascending=False).head(10)
batting_last_ten_years
```

Le jeu de données que j'utilise est déjà très propre. Je n'ai pas besoin de faire beaucoup de nettoyage pour obtenir les données dont j'ai besoin. Ci-dessus, vous pouvez voir les données de frappe des 10 dernières années.

### Exploration

Dans le bloc de code suivant, je vais calculer les corrélations entre les coups de circuit et toutes les autres métriques. De cette façon, nous pouvons voir quelles métriques contribuent aux coups de circuit et quelles métriques sont mauvaises pour marquer des coups de circuit. Par exemple, je m'attends à ce que les batteurs qui jouent plus de matchs marquent plus de coups de circuit. Je m'attends également à ce que les batteurs avec un RBI élevé marquent le plus de coups de circuit.

Une corrélation de 1 entre deux valeurs est une corrélation positive parfaite. Cela signifie que lorsque l'une des deux valeurs augmente, l'autre augmente également.

Une corrélation de -1 est une corrélation négative. Cela signifie que lorsque l'une des valeurs augmente, l'autre diminue.

Lorsque la valeur d'une corrélation tend vers 0, la corrélation est très faible ou inexistante. J'appellerai une corrélation positive ++, + ou +- selon la force de la corrélation. Aucune corrélation ne sera 0, et les corrélations négatives iront de -+, —, ou —— étant une forte corrélation négative.

```
def standardize(data):
    return (data - data.mean()) / data.std(ddof=0)
```

```
def pearsons_r(x, y):
    return (standardize(x) * standardize(y)).mean()
```

```
# Il n'a pas de sens de calculer la corrélation entre ces valeurs et les coups de circuit
leave_out = ['playerID', 'yearID', 'teamID', 'lgID', 'HR']
```

```
# Signification des noms de colonnes dans les données
dictionary = {'playerID':'Joueur', 'yearID':'Année', 'teamID':'Équipe', 'lgID':'Ligue', 'HR':'Coups de circuit','stint':'Périodes', 'G':'Matchs', 'AB': 'Au bat', 'R': 'Points', 'H':'Coups', '2B':'Doubles', '3B':'Triples', 'RBI':'Points battus', 'SB':'Bases volées', 'CS':'Pris en vol', 'BB':'Ballons', 'SO':'Retraits sur prises', 'IBB':'Ballons intentionnels', 'HBP':'Frappe par la balle', 'SH':'Coups de sacrifice', 'SF':'Volées de sacrifice', 'GIDP':'Mise en double jeu'}
```

```
strong_positive_correlation = []
strong_negative_correlation = []
```

```
def correlations_for_hr(df):
    columns = list(df)
    for x in columns:
        if x not in leave_out:
            name_of_metric = dictionary[x]
            r = pearsons_r(df['HR'], df[x])
                        # Calcul de la force de la corrélation
            correlation = ''
            if r > 0.7:
                correlation = '++'
                strong_positive_correlation.append(name_of_metric)
            elif r > 0.5:
                correlation = '+ '
            elif r > 0.3:
                correlation = '+-'
            elif r >= -0.3:
                correlation = 'O '
            elif r > -0.5:
                correlation = '-+'
            elif r > -0.7:
                correlation = '- '
            elif r > -1:
                correlation = '--'
                strong_negative_correlation.append(name_of_metric)
                            print('{} Corrélation entre les coups de circuit et {}:{}'.format(correlation, name_of_metric, "%.3f"%r))
            print('-----------------------------------------')
            print('Corrélations :')
print('-----------------------------------------------------')
print(correlations_for_hr(batting_df))
print('\n')
```

```
print('Corrélations positives : {}'.format(strong_positive_correlation))
print('\n')
```

```
print('Corrélations négatives : {}'.format(strong_negative_correlation))
```

Sortie :

```
Corrélations :--------------------------------------------------------------------
O  Corrélation entre les coups de circuit et les périodes : -0.065
--------------------------------------------------------------------
+  Corrélation entre les coups de circuit et les matchs : 0.668
--------------------------------------------------------------------
+  Corrélation entre les coups de circuit et les coups au bat : 0.695
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les points : 0.729
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les coups : 0.703
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les doubles : 0.725
--------------------------------------------------------------------
+- Corrélation entre les coups de circuit et les triples : 0.348
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les points battus : 0.837
--------------------------------------------------------------------
O  Corrélation entre les coups de circuit et les bases volées : 0.265
--------------------------------------------------------------------
+- Corrélation entre les coups de circuit et les pris en vol : 0.409
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les ballons : 0.731
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les retraits sur prises : 0.822
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les ballons intentionnels : 0.753
--------------------------------------------------------------------
+- Corrélation entre les coups de circuit et les frappes par la balle : 0.497
--------------------------------------------------------------------
O  Corrélation entre les coups de circuit et les coups de sacrifice : 0.064
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les volées de sacrifice : 0.792
--------------------------------------------------------------------
++ Corrélation entre les coups de circuit et les mises en double jeu : 0.767
--------------------------------------------------------------------
```

```
Corrélations positives : ['Points', 'Coups', 'Doubles', 'Points battus', 'Ballons', 'Retraits sur prises', 'Ballons intentionnels', 'Volées de sacrifice', 'Mises en double jeu']
```

```
Corrélations négatives : []
```

### Réexamen des premières attentes

Vous vous souvenez de mes attentes ? Je m'attendais à ce que le nombre de matchs et le score RBI aient une corrélation positive avec les coups de circuit. Selon mes calculs ci-dessus, le nombre de matchs a une corrélation positive avec un Pearson R de 0,668. Donc, les joueurs qui ont joué plus de matchs dans une saison ont un nombre plus élevé de coups de circuit. Cela semble très logique, puisque les batteurs qui jouent plus de matchs ont plus de chances de marquer un coup de circuit.

Mon autre attente était qu'un RBI élevé signifierait un nombre élevé de coups de circuit. La corrélation entre les coups de circuit et le RBI est grande avec 0,837 ! Cela est à nouveau assez logique, car les coups de circuit sont capables de récompenser le joueur avec le plus de points RBI.

Un autre fait intéressant est qu'il n'y a pas de corrélations négatives. Donc, il n'y a pas de métrique qui diminue lorsque le nombre de coups de circuit augmente.

```
# COUPS DE CIRCUIT vs. POINTS BATTUS
sns.lmplot(size=10, data=batting_df[['HR', 'RBI']], x='HR', y='RBI', x_estimator=np.mean)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*OgrJ3wEmh75BYlyu71Pn4A.png)
_COUPS DE CIRCUIT vs. POINTS BATTUS_

Le graphique ci-dessus montre comment les coups de circuit se corrèlent aux points battus. Vous pouvez voir le nombre de coups de circuit sur l'axe des x et le nombre de points battus sur l'axe des y.

```
# COUPS DE CIRCUIT vs. RETRAITS SUR PRISES
sns.lmplot(size=10, data=batting_df[['HR', 'SO']], x='HR', y='SO', x_estimator=np.mean)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*imXXUHBOTge6FRDyCyYPpw.png)
_COUPS DE CIRCUIT vs. RETRAITS SUR PRISES_

Le graphique ci-dessus révèle une corrélation intéressante. Il s'agit de la corrélation entre les coups de circuit et les retraits sur prises. La corrélation de Pearson R est de 0,822, presque aussi élevée que la corrélation entre les coups de circuit et les points battus.

Cette corrélation m'a intéressé davantage parce que les points battus sont un résultat direct des coups de circuit. Les retraits sur prises, en revanche, ont une corrélation directe avec la perte de votre chance de marquer un coup de circuit. Comment les retraits sur prises pourraient-ils entraîner plus de coups de circuit ?

### Comment les coups de circuit et les retraits sur prises sont-ils liés

Pour résoudre ce mystère, j'ai commencé à réfléchir... Peut-être que les batteurs qui prennent plus de risques sont plus susceptibles de marquer un coup de circuit. Parce qu'ils frappent même sur des balles qui semblent difficiles à frapper. Donc, si prendre plus de risques vous donne plus de coups de circuit, j'ai jeté un coup d'œil aux métriques risquées. Les métriques risquées sont des métriques qui impliquent la prise de risques, comme voler des bases. Examinons la corrélation.

```
# COUPS DE CIRCUIT vs. PRISES EN VOL
sns.lmplot(size=10, data=batting_df[['HR', 'CS']], x='HR', y='CS', x_estimator=np.mean)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*F6UO9ZsBNxHxcsM9mGs9Xg.png)
_COUPS DE CIRCUIT vs. PRISES EN VOL_

Ci-dessus, vous pouvez voir la corrélation (0,409) entre les coups de circuit (axe des x) et le nombre de fois où un coureur est pris en vol (axe des y). Il y a une corrélation vague, mais ce n'est pas suffisant pour tirer une conclusion. Peut-être que les preneurs de risques sont devenus très bons pour voler des bases et ne se font pas prendre en vol ? Regardons les bases volées.

```
# COUPS DE CIRCUIT vs. BASES VOLÉES
sns.lmplot(size=10, data=batting_df[['HR', 'SB']], x='HR', y='SB', x_estimator=np.mean)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*6MsW8r0ef2wXT-sz_2Eicw.png)
_COUPS DE CIRCUIT vs. BASES VOLÉES_

Ci-dessus, vous pouvez voir la corrélation de 0,265 entre les coups de circuit (axe des x) et les bases volées (axe des y). Cette corrélation est inexistante. Donc, prendre des risques n'a rien à voir avec le fait de marquer un coup de circuit.

Les données seules ne vont pas révéler le secret pour marquer un coup de circuit. Je dois en apprendre davantage sur le baseball pour résoudre ce mystère. Mon prochain plan d'attaque était de regarder des vidéos YouTube pour voir comment se comportent les batteurs à haut score.

Il s'avère que marquer un coup de circuit a plus à voir avec des calculs précis qu'avec la prise de risques. J'ai vu des batteurs attendre le bon lancer. Ils préfèrent avoir une prise, espérant que le prochain lancer leur servira mieux. Un avantage supplémentaire est que le lanceur se fatigue plus vite car il doit lancer plus de balles.

### Conclusions/Prédictions

Pour les batteurs qui essaient d'améliorer leurs statistiques de coups de circuit, j'ai quelques suggestions. La première étape pour obtenir plus de coups de circuit est : jouer plus de matchs, sans excuses — jouer ! Deuxième étape : obtenir quelques retraits sur prises. Cela semble contre-intuitif, mais cela augmente votre nombre de coups de circuit. Voici comment cela fonctionne : cela épuise le lanceur et donne au batteur plus de temps pour attendre le meilleur lancer pour frapper ce GRAND CHELEM.

Pour en savoir plus sur la corrélation entre les coups de circuit et les retraits sur prises, lisez [cet article](https://www.mlb.com/news/anthony-castrovince-increasing-strikeout-totals-acceptable-if-a-batter-produces-offensively/c-47432098).

Ou celui-ci sur [les risques d'un lanceur fatigué](http://www.stack.com/a/pitcher-fatigue)

Pour plus d'informations, consultez [ditisAnton.com](http://ditisanton.com) et [INSCRIVEZ-VOUS](https://goo.gl/mBggzD) à ma newsletter hebdomadaire.