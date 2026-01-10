---
title: Python pour la Finance – Tutoriel de Trading Algorithme pour Débutants
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2020-09-24T15:11:44.000Z'
originalURL: https://freecodecamp.org/news/algorithmic-trading-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/Algorithmic-Trading-in-Python-Explained.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Data Science
  slug: data-science
- name: Python
  slug: python
seo_title: Python pour la Finance – Tutoriel de Trading Algorithme pour Débutants
seo_desc: 'Technology has become an asset in finance. Financial institutions are now
  evolving into technology companies rather than just staying occupied with the financial
  aspects of the field.

  Mathematical Algorithms bring about innovation and speed. They can...'
---

La technologie est devenue un atout dans le domaine de la finance. Les institutions financières évoluent désormais vers des entreprises technologiques plutôt que de se concentrer uniquement sur les aspects financiers du secteur.

Les algorithmes mathématiques apportent innovation et rapidité. Ils peuvent nous aider à obtenir un avantage concurrentiel sur le marché.

La vitesse et la fréquence des transactions financières, ainsi que les grands volumes de données, ont attiré beaucoup d'attention vers la technologie de la part de toutes les grandes institutions financières.

Le trading algorithmique ou quantitatif est le processus de conception et de développement de stratégies de trading basées sur des analyses mathématiques et statistiques. C'est un domaine extrêmement sophistiqué de la finance.

Ce tutoriel sert de guide pour débutants au trading quantitatif avec Python. Vous trouverez cet article très utile si vous êtes :

1. Un étudiant ou quelqu'un visant à devenir analyste quantitatif (quant) dans un fonds ou une banque.

2. Quelqu'un qui prévoit de lancer sa propre entreprise de trading quantitatif.

Nous aborderons les sujets suivants dans cet article :

* Les bases des actions et du trading

* Extraction de données à partir de l'API Quandl

* Analyse exploratoire des données sur les prix des actions

* Moyennes mobiles

* Formulation d'une stratégie de trading avec Python

* Visualisation de la performance de la stratégie

Avant de plonger dans les détails et la dynamique des données de prix des actions, nous devons d'abord comprendre les bases de la finance. Si vous êtes déjà familiarisé avec la finance et le fonctionnement du trading, vous pouvez sauter cette section et cliquer ici pour passer à la suivante.

## Qu'est-ce que les Actions ? Qu'est-ce que le Trading d'Actions ?

### Actions

Une action est une représentation d'une part dans la propriété d'une société, émise à un certain montant. C'est un type de titre financier qui établit votre droit sur les actifs et la performance d'une entreprise.

Une organisation ou une entreprise émet des actions pour lever plus de fonds/capital afin de se développer et de s'engager dans plus de projets. Ces actions sont ensuite disponibles publiquement et sont achetées et vendues.

### Trading d'Actions et Stratégie de Trading

Le processus d'achat et de vente d'actions existantes et précédemment émises est appelé trading d'actions. Il existe un prix auquel une action peut être achetée et vendue, et celui-ci fluctue en fonction de la demande et de l'offre sur le marché boursier.

En fonction de la performance et des actions de l'entreprise, les prix des actions peuvent monter et descendre, mais le mouvement des prix des actions n'est pas limité à la performance de l'entreprise.

Les traders paient de l'argent en échange de la propriété d'une entreprise, espérant réaliser des transactions rentables et vendre les actions à un prix plus élevé.

Une autre technique importante que les traders suivent est la vente à découvert. Cela implique d'emprunter des actions et de les vendre immédiatement dans l'espoir de les racheter plus tard à un prix inférieur, de les rendre au prêteur et de réaliser la marge.

Ainsi, la plupart des traders suivent un plan et un modèle pour trader. Cela est connu sous le nom de stratégie de trading.

Les traders quantitatifs des fonds spéculatifs et des banques d'investissement conçoivent et développent ces stratégies et cadres de trading pour les tester. Cela nécessite une expertise approfondie en programmation et une compréhension des langages nécessaires pour construire votre propre stratégie.

Python est l'un des langages de programmation les plus populaires utilisés, parmi C++, Java, R et MATLAB. Il est largement adopté dans tous les domaines, en particulier en science des données, grâce à sa syntaxe facile, sa grande communauté et son support tiers.

Vous aurez besoin de vous familiariser avec Python et les statistiques afin de tirer le meilleur parti de ce tutoriel. Assurez-vous de vous rafraîchir la mémoire sur Python et de consulter les [fondamentaux des statistiques](https://sites.google.com/site/fundamentalstatistics/unit-1-the-basics).

## Extraction de données à partir de l'API Quandl

Afin d'extraire les données de prix des actions, nous utiliserons l'[API Quandl](https://docs.quandl.com/). Mais avant cela, configurons l'environnement de travail. Voici comment procéder :

1. Dans votre terminal, créez un nouveau répertoire pour le projet (nommez-le comme vous le souhaitez) :

```javascript
mkdir <nom_du_répertoire>
```

1. Assurez-vous d'avoir [Python 3](https://www.python.org/downloads/) et [virtualenv](https://pypi.org/project/virtualenv/) installés sur votre machine.

2. Créez un nouvel environnement virtuel Python 3 en utilisant `virtualenv <nom_env>` et activez-le avec `source <nom_env>/bin/activate`.

3. Maintenant, installez jupyter-notebook en utilisant [pip](https://pip.pypa.io/en/stable/installing/), et tapez `pip install jupyter-notebook` dans le terminal.

4. De même, installez les packages `pandas`, `quandl` et `numpy`.

5. Exécutez votre `jupyter-notebook` à partir du terminal.

Maintenant, votre notebook devrait s'exécuter sur localhost comme dans la capture d'écran ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-1.png align="left")

Vous pouvez créer votre premier notebook en cliquant sur le menu déroulant `New` à droite. Assurez-vous d'avoir créé un compte sur [Quandl](https://docs.quandl.com/). Suivez les étapes mentionnées [ici](https://docs.quandl.com/docs/python-installation) pour créer votre clé API.

Une fois que vous êtes prêt, plongeons directement dans le sujet :

```javascript
# importation des packages requis
```

```javascript
import pandas as pd
import quandl as q
```

Pandas sera le package le plus utilisé dans ce tutoriel car nous allons faire beaucoup de manipulation de données et de traçage.

Après avoir importé les packages, nous allons faire des requêtes à l'API Quandl en utilisant le package Quandl :

```javascript
# définir la clé API
q.ApiConfig.api_key = "<clé_API>"
```

```javascript
# envoyer une requête GET pour interroger les prix de clôture des actions de Microsoft du 1er janvier 2010 au 1er janvier 2019

msft_data = q.get("EOD/MSFT", start_date="2010-01-01", end_date="2019-01-01")
```

```javascript
# regarder les 5 premières lignes du dataframe

msft_data.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/2-3.png align="left")

Ici, nous avons les données de prix des actions EOD de Microsoft pour les 9 dernières années. Tout ce que vous aviez à faire était d'appeler la méthode `get` du package Quandl et de fournir le symbole boursier, MSFT, et la période pour les données dont vous avez besoin.

C'était vraiment simple, n'est-ce pas ? Passons à l'étape suivante pour comprendre et explorer ces données plus en détail.

## Analyse Exploratoire des Données sur les Prix des Actions

Avec les données en notre possession, la première chose que nous devrions faire est de comprendre ce qu'elles représentent et quel type d'informations elles encapsulent.

En imprimant les informations du DataFrame, nous pouvons voir tout ce qu'il contient :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/3-1.png align="left")

Comme on peut le voir dans la capture d'écran ci-dessus, le DataFrame contient un DatetimeIndex, ce qui signifie que nous traitons des données de séries temporelles.

Un index peut être considéré comme une structure de données qui nous aide à modifier ou à référencer les données. Les données de séries temporelles sont une séquence d'instantanés de prix pris à des intervalles de temps consécutifs et équidistants.

Dans le trading, les données de prix des actions EOD capturent le mouvement de certains paramètres concernant une action, tels que le prix de l'action, sur une période spécifiée avec des points de données enregistrés à des intervalles réguliers.

### Terminologie Importante

En regardant les autres colonnes, essayons de comprendre ce que représente chaque colonne :

* Open/Close – Capture le prix d'ouverture/de clôture de l'action

* Adj_Open/Adj_Close – Un prix d'ouverture/de clôture ajusté est le prix d'une action à un jour de trading donné qui a été révisé pour inclure toute distribution de dividendes, divisions d'actions et autres actions corporatives qui se sont produites à tout moment avant l'ouverture du jour suivant.

* Volume – Il enregistre le nombre d'actions qui sont négociées à un jour de trading donné.

* High/Low – Il suit le prix le plus élevé et le plus bas de l'action pendant un jour de trading particulier.

Ce sont les colonnes importantes sur lesquelles nous allons nous concentrer pour le moment.

Nous pouvons apprendre les statistiques récapitulatives des données, qui nous montrent le nombre de lignes, la moyenne, le maximum, les écarts types, etc. Essayez d'exécuter la ligne de code suivante dans la cellule Ipython :

```javascript
msft_data.describe()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/4-1.png align="left")

### resample()

La méthode resample() de Pandas est utilisée pour faciliter le contrôle et la flexibilité sur la conversion de fréquence des données de séries temporelles. Nous pouvons spécifier les intervalles de temps pour rééchantillonner les données en mensuel, trimestriel ou annuel, et effectuer l'opération requise sur celles-ci.

```javascript
msft_data.resample('M').mean()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/5-1.png align="left")

C'est une manière intéressante d'analyser la performance des actions dans différents cadres temporels.

### Calcul des rendements

Un rendement financier est simplement l'argent gagné ou perdu sur un investissement. Un rendement peut être exprimé nominalement comme le changement dans le montant d'un investissement au fil du temps. Il peut être calculé comme le pourcentage dérivé du rapport du profit à l'investissement.

Nous avons le pct_change() à notre disposition à cette fin. Voici comment vous pouvez calculer les rendements :

```javascript
# Importer le package numpy
import numpy as np
```

```javascript
# assigner `Adj Close` à `daily_close`
daily_close = msft_data[['Adj_Close']]
```

```javascript
# rendements en tant que changement fractionnaire
daily_return = daily_close.pct_change()
```

```javascript
# remplacer les valeurs NA par 0

daily_return.fillna(0, inplace=True)
```

```javascript
print(daily_return)
```

Cela imprimera les rendements que l'action a générés sur une base quotidienne. Multiplier le nombre par 100 vous donnera le changement en pourcentage.

La formule utilisée dans pct_change() est :

> Rendement = {(Prix à t) — (Prix à t-1)} / {Prix à t-1}

Maintenant, pour calculer les rendements mensuels, tout ce que vous avez à faire est :

```javascript
mdata = msft_data.resample('M').apply(lambda x: x[-1])

monthly_return = mdata.pct_change()
```

Après avoir rééchantillonné les données en mois (pour les jours ouvrables), nous pouvons obtenir le dernier jour de trading du mois en utilisant la fonction `apply()`.

`apply()` prend une fonction et l'applique à chaque ligne de la série Pandas. La fonction `lambda` est une fonction anonyme en Python qui peut être définie sans nom et ne prend que des expressions dans le format suivant :

```javascript
Lambda : expression
```

Par exemple, `lambda x: x * 2` est une fonction lambda. Ici, x est l'argument et `x * 2` est l'expression qui est évaluée et retournée.

## Moyennes Mobiles dans le Trading

Le concept des moyennes mobiles va constituer la base de notre stratégie de trading basée sur la dynamique.

En finance, les analystes doivent souvent évaluer des métriques statistiques en continu sur une fenêtre de temps glissante, ce qui est appelé calculs de fenêtre mobile.

Voyons comment nous pouvons calculer la moyenne mobile sur une fenêtre de 50 jours, et faire glisser la fenêtre d'un jour.

### rolling()

C'est la fonction magique qui fait les tours pour nous :

```javascript
# assigner les prix de clôture ajustés à adj_prices
adj_price = msft_data['Adj_Close']
```

```javascript
# calculer la moyenne mobile
mav = adj_price.rolling(window=50).mean()
```

```javascript
# imprimer le résultat
print(mav[-10:])
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/6-1.png align="left")

Vous verrez la moyenne mobile sur une fenêtre de 50 jours (environ 2 mois). Les moyennes mobiles aident à lisser les fluctuations ou les pics dans les données, et vous donnent une courbe plus lisse pour la performance de l'entreprise.

Nous pouvons tracer et voir la différence :

```javascript
# importer le package matplotlib pour voir le tracé

import matplotlib.pyplot as plt

adj_price.plot()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/7-1.png align="left")

Vous pouvez maintenant tracer la moyenne mobile() :

```javascript
mav.plot()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/09/8-1.png align="left")

Et vous pouvez voir la différence par vous-même, comment les pics dans les données sont consommés pour donner un sentiment général autour de la performance de l'action.

## Formulation d'une Stratégie de Trading

Voici la partie finale et la plus intéressante : la conception et la création de la stratégie de trading. Ce sera un guide étape par étape pour développer une stratégie de croisement de moyennes mobiles simples (SMAC) basée sur la dynamique.

Les stratégies basées sur la dynamique reposent sur un indicateur technique qui capitalise sur la continuité de la tendance du marché. Nous achetons des titres qui montrent une tendance à la hausse et vendons à découvert des titres qui montrent une tendance à la baisse.

La stratégie SMAC est une stratégie de dynamique schématique bien connue. C'est une stratégie uniquement à la hausse. La dynamique, ici, est le rendement total de l'action incluant les dividendes sur les *n* derniers mois. Cette période de *n* mois est appelée la période de rétrospective.

Il existe 3 principaux types de périodes de rétrospective : court terme, moyen terme et long terme. Nous devons définir 2 périodes de rétrospective différentes pour une série temporelle particulière.

Un signal d'achat est généré lorsque la moyenne mobile de la période de rétrospective la plus courte (ou moyenne mobile) dépasse la moyenne mobile de la période de rétrospective la plus longue. Un signal de vente se produit lorsque la moyenne mobile de la période de rétrospective la plus courte descend en dessous de la moyenne mobile la plus longue.

Maintenant, voyons à quoi ressemblera le code pour cette stratégie :

```javascript
# étape1 : initialiser les périodes de rétrospective courtes et longues

short_lb = 50
long_lb = 120
```

```javascript
# étape2 : initialiser un nouveau DataFrame appelé signal_df avec une colonne signal

signal_df = pd.DataFrame(index=msft_data.index)
signal_df['signal'] = 0.0
```

```javascript
# étape3 : créer une moyenne mobile simple courte sur la période de rétrospective courte
signal_df['short_mav'] = msft_data['Adj_Close'].rolling(window=short_lb, min_periods=1, center=False).mean()
```

```javascript
# étape4 : créer une moyenne mobile simple longue sur la période de rétrospective longue

signal_df['long_mav'] = msft_data['Adj_Close'].rolling(window=long_lb, min_periods=1, center=False).mean()
```

```javascript
# étape5 : générer les signaux basés sur l'instruction conditionnelle

signal_df['signal'][short_lb:] = np.where(signal_df['short_mav'][short_lb:] > signal_df['long_mav'][short_lb:], 1.0, 0.0)
```

```javascript
# étape6 : créer les ordres de trading basés sur la colonne positions

signal_df['positions'] = signal_df['signal'].diff()
signal_df[signal_df['positions'] == -1.0]
```

Voyons ce qui se passe ici. Nous avons créé 2 périodes de rétrospective. La période de rétrospective courte `short_lb` est de 50 jours, et la période de rétrospective plus longue pour la moyenne mobile longue est définie comme un `long_lb` de 120 jours.

Nous avons créé un nouveau DataFrame conçu pour capturer les signaux. Ces signaux sont générés chaque fois que la moyenne mobile courte croise la moyenne mobile longue en utilisant `np.where`. Il attribue `1.0` pour vrai et `0.0` si la condition s'avère fausse.

La colonne `positions` dans le DataFrame nous indique s'il y a un signal d'achat ou de vente, ou si nous devons rester en place. Nous calculons essentiellement la différence dans la colonne des signaux par rapport à la ligne précédente en utilisant [diff](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.diff.html).

Et voilà, notre stratégie est implémentée en seulement 6 étapes en utilisant Pandas. Facile, n'est-ce pas ?

Maintenant, essayons de visualiser cela en utilisant Matplotlib. Tout ce que nous avons à faire est d'initialiser une figure de tracé, d'ajouter les prix de clôture ajustés, les moyennes mobiles courtes et longues au tracé, puis de tracer les signaux d'achat et de vente en utilisant la colonne des positions dans le `signal_df` ci-dessus :

```javascript
# initialiser le tracé en utilisant plt
fig = plt.figure()
```

```javascript
# Ajouter un sous-tracé et une étiquette pour l'axe y

plt1 = fig.add_subplot(111, ylabel='Prix en $')
```

```javascript
msft_data['Adj_Close'].plot(ax=plt1, color='r', lw=2.)
```

```javascript
# tracer les moyennes mobiles de rétrospective courtes et longues
signal_df[['short_mav', 'long_mav']].plot(ax=plt1, lw=2., figsize=(12,8))
```

```javascript
# tracer les signaux de vente

plt1.plot(signal_df.loc[signal_df.positions == -1.0].index, signal_df.short_mav[signal_df.positions == -1.0],'v', markersize=10, color='k')
```

```javascript
# tracer les signaux d'achat

plt1.plot(signal_df.loc[signal_df.positions == 1.0].index, signal_df.short_mav[signal_df.positions == 1.0], '^', markersize=10, color='m')
# Afficher le tracé
plt.show()
```

L'exécution de la cellule ci-dessus dans le notebook Jupyter produira un tracé comme celui ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/9-1.png align="left")

Maintenant, vous pouvez clairement voir que chaque fois que la ligne bleue (moyenne mobile courte) monte et dépasse la ligne orange (moyenne mobile longue), il y a un marqueur rose vers le haut indiquant un signal d'achat.

Un signal de vente est indiqué par un marqueur noir vers le bas où il y a une chute de la `short_mav` en dessous de la `long_mav`.

## Visualiser la Performance de la Stratégie sur Quantopian

[Quantopian](https://www.quantopian.com/) est une plateforme alimentée par Zipline qui a de multiples cas d'utilisation. Vous pouvez écrire vos propres algorithmes, accéder à des données gratuites, backtester votre stratégie, contribuer à la communauté et collaborer avec Quantopian si vous avez besoin de capital.

Nous avons écrit un algorithme pour backtester notre stratégie SMA, et voici les résultats :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/10-1.png align="left")

Voici une explication des métriques ci-dessus :

* Rendement total : Le rendement total en pourcentage du portefeuille du début à la fin du backtest.

* Rendement spécifique : La différence entre les rendements totaux du portefeuille et les rendements communs.

* Rendement commun : Les rendements attribuables aux facteurs de risque communs. Il y a 11 facteurs de risque sectoriels et 5 facteurs de risque de style qui composent ces rendements. Les graphiques d'exposition sectorielle et d'exposition de style dans la section des risques fournissent plus de détails sur ces facteurs.

* Sharpe : Le ratio de Sharpe sur 6 mois. C'est une mesure de l'investissement ajusté au risque. Il est calculé en divisant les rendements excédentaires du portefeuille par rapport au taux sans risque par l'écart type du portefeuille.

* Drawdown maximum : La plus grande baisse de tous les mouvements de pic à creux dans l'histoire du portefeuille.

* Volatilité : Écart type des rendements du portefeuille.

Félicitez-vous car vous avez réussi à implémenter votre stratégie de trading quantitatif !

## Où aller à partir de là ?

Maintenant que votre algorithme est prêt, vous devrez backtester les résultats et évaluer les [métriques cartographiant le risque](https://www.investopedia.com/ask/answers/041415/what-are-some-common-measures-risk-used-risk-management.asp) impliqué dans la stratégie et l'action. Encore une fois, vous pouvez utiliser [BlueShift](https://blueshift.quantinsti.com/) et [Quantopian](https://www.quantopian.com/) pour en savoir plus sur le backtesting et les stratégies de trading.

### Ressources Complémentaires

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Quantra-logo-Black.png align="left")

*https://quantra.quantinsti.com/learning-track/algorithmic-trading-for-everyone?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=lt_everyone*

[Quantra](https://quantra.quantinsti.com/learning-track/algorithmic-trading-for-everyone?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=lt_everyone) est une création de QuantInsti. Avec une gamme de cours gratuits et payants par des experts du domaine, Quantra offre un guide complet sur un ensemble de stratégies de trading de base et avancées.

* [Cours de Science des Données](https://quantra.quantinsti.com/course/introduction-to-data-science?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=data_science) – Ils ont lancé un cours d'introduction à la Science des Données qui vous aide à construire une base solide pour les projets en Science des Données.

* [Cours de Trading pour Débutants](https://quantra.quantinsti.com/learning-track/algorithmic-trading-for-everyone?utm_source=harshit_tyagi&utm_medium=affiliate&utm_campaign=lt_everyone) – Du trading de dynamique aux stratégies de trading basées sur l'apprentissage automatique et profond, des chercheurs du monde du trading comme le Dr. Ernest P. Chan sont les auteurs de ces cours de niche.

#### Ressources Gratuites

Pour en savoir plus sur les algorithmes de trading, consultez ces blogs :

* [Quantstart](https://www.quantstart.com/) – ils couvrent une large gamme d'algorithmes de backtesting, de guides pour débutants et plus encore.

* [Investopedia](https://www.investopedia.com/) – tout ce que vous voulez savoir sur l'investissement et la finance.

* [Quantivity](https://quantivity.wordpress.com/) – des explications mathématiques détaillées des algorithmes et de leurs avantages et inconvénients.

Warren Buffet dit qu'il lit environ 500 pages *par jour*, ce qui devrait vous indiquer que la lecture est essentielle pour réussir dans le domaine de la finance.

Embarquez-vous dans ce voyage du trading et vous pourrez mener une vie pleine d'excitation, de passion et de mathématiques.

# [Data Science avec Harshit](https://www.youtube.com/c/DataSciencewithHarshit?sub_confirmation=1)

%[https://youtu.be/_ANbV9lVA-M]

Avec cette chaîne, je prévois de lancer une couple de [séries couvrant tout l'espace de la science des données](https://towardsdatascience.com/hitchhikers-guide-to-learning-data-science-2cc3d963b1a2?source=---------8------------------). Voici pourquoi vous devriez vous abonner à la [chaîne](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ) :

* Ces séries couvriront tous les tutoriels de qualité requis/demandés sur chacun des sujets et sous-sujets comme les [fondamentaux de Python pour la Science des Données](https://towardsdatascience.com/python-fundamentals-for-data-science-6c7f9901e1c8?source=---------5------------------).

* Explications des [mathématiques et dérivations](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea?source=---------9------------------) de pourquoi nous faisons ce que nous faisons en ML et Deep Learning.

* [Podcasts avec des Data Scientists et Ingénieurs](https://www.youtube.com/watch?v=a2pkZCleJwM&t=2s) chez Google, Microsoft, Amazon, etc., et PDG de grandes entreprises axées sur les données.

* [Projets et instructions](https://towardsdatascience.com/building-covid-19-analysis-dashboard-using-python-and-voila-ee091f65dcbb?source=---------2------------------) pour implémenter les sujets appris jusqu'à présent. Apprenez de nouvelles certifications, Bootcamp, et ressources pour réussir ces certifications comme cet [**Examen de Certificat de Développeur TensorFlow par Google.**](https://youtu.be/yapSsspJzAw)

Si ce tutoriel était utile, vous devriez consulter mes cours de science des données et d'apprentissage automatique sur [Wiplane Academy](https://www.wiplane.com/). Ils sont complets mais compacts et vous aident à construire une base solide de travail à présenter.