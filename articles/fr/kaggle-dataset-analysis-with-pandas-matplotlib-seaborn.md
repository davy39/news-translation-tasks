---
title: 'Analyse de données Python : Comment visualiser un jeu de données Kaggle avec
  Pandas, Matplotlib et Seaborn'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-22T17:49:27.000Z'
originalURL: https://freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9822740569d1a4ca1855.jpg
tags:
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: kaggle
  slug: kaggle
- name: Matplotlib
  slug: matplotlib
- name: pandas
  slug: pandas
seo_title: 'Analyse de données Python : Comment visualiser un jeu de données Kaggle
  avec Pandas, Matplotlib et Seaborn'
seo_desc: 'By Srijan

  The Indian Premier League or IPL is a T20 cricket tournament organized annually
  by the Board of Control for Cricket In India (BCCI). Eight city-based franchises
  compete with each other over 6 weeks to find the winner.

  In this article, I''m g...'
---

Par Srijan

La **Indian Premier League** ou IPL est un tournoi de cricket T20 organisé annuellement par le Board of Control for Cricket In India (BCCI). Huit franchises basées dans des villes s'affrontent pendant 6 semaines pour trouver le vainqueur.

Dans cet article, je vais analyser les données des saisons passées de l'IPL pour voir quelles équipes ont remporté le plus de matchs, comment les équipes se comportent lorsqu'elles gagnent un toss, qui a le plus grand héritage, et ainsi de suite.

J'ai fait cette analyse d'un point de vue historique, donnant un aperçu de ce qui s'est passé dans l'IPL au fil des ans. J'ai utilisé des outils tels que _Pandas_, _Matplotlib_ et _Seaborn_ ainsi que _Python_ pour donner une représentation visuelle ainsi que numérique des données devant nous.

**Pandas** signifie _Python Data Analysis_ library. Il est généralement utilisé pour travailler avec des données tabulaires (similaires aux données stockées dans une feuille de calcul). Pandas fournit des fonctions d'assistance pour lire des données à partir de divers formats de fichiers comme CSV, des feuilles de calcul Excel, des tableaux HTML, JSON, SQL et effectuer des opérations sur eux.

**Matplotlib** et **Seaborn** sont deux bibliothèques Python qui sont utilisées pour produire des graphiques. Matplotlib est généralement utilisé pour tracer des lignes, des camemberts et des graphiques à barres.

Seaborn fournit certaines fonctionnalités de visualisation plus avancées avec moins de syntaxe et plus de personnalisations. Je passe de l'un à l'autre pendant l'analyse.

## Table des matières

1. [Obtention du jeu de données](#heading-1-obtention-du-jeu-de-donnees)
2. [Préparation et nettoyage des données](#heading-2-preparation-et-nettoyage-des-donnees)
3. [Analyse exploratoire et visualisation](#heading-3-analyse-exploratoire-et-visualisation)
4. [Poser et répondre à des questions](#poser-et-repondre-a-des-questions)
5. [Inférences de l'analyse](#heading-5-inferences-de-lanalyse)
6. [Conclusion](#heading-6-conclusion)

## 1. Obtention du jeu de données

J'ai téléchargé le jeu de données depuis [Kaggle](https://www.kaggle.com/nowke9/ipldata). Vous verrez qu'il y a deux fichiers CSV (Comma Separated Value), matches.csv et deliveries.csv. J'ai choisi de faire mon analyse sur matches.csv.

Pour trouver d'autres jeux de données intéressants, vous pouvez consulter [cette](https://jovian.ml/forum/t/recommended-datasets-for-course-project/11711) page.

## 2. Préparation et nettoyage des données

Un jeu de données contient de nombreuses colonnes et lignes. Il est toujours possible que certaines lignes aient des valeurs manquantes ou `NaN` pour une ou plusieurs colonnes.

Il est également possible qu'il y ait certaines colonnes ou lignes que vous souhaitez écarter de votre analyse. Vous pouvez également combiner deux jeux de données ou plus pour une analyse approfondie.

Le nettoyage des données implique de faire des corrections à ces données, en laissant de côté les colonnes ou lignes inutiles, en fusionnant des jeux de données, et ainsi de suite.

Avant de prendre ces mesures, j'ai dû installer et importer les outils (_bibliothèques_) à utiliser pendant l'analyse. J'ai importé les bibliothèques avec différents alias tels que `pd`, `plt` et `sns`. J'ai ensuite défini quelques styles de base pour les graphiques.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=5" title="Jovian Viewer" height="308" width="800" frameborder="0" scrolling="auto"></iframe>

Remarquez la commande spéciale `%matplotlib inline`. Elle garantit que les graphiques sont affichés et intégrés dans le notebook Jupyter lui-même. Sans cette commande, parfois les graphiques peuvent apparaître dans des fenêtres pop-up.

En utilisant la méthode `read_csv()` de la bibliothèque _Pandas_, j'ai chargé le fichier _matches.csv_.

Les données du fichier sont lues et stockées dans un objet `DataFrame` - l'une des structures de données principales dans Pandas pour stocker et travailler avec des données tabulaires. J'ai utilisé le suffixe `_df` dans les noms de variables pour les data frames.

J'ai utilisé le nom `matches_raw_df` pour le data frame. Cela indique qu'il s'agit de données non traitées que je vais nettoyer, filtrer et modifier pour préparer un data frame prêt pour l'analyse.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=9" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=10" title="Jovian Viewer" height="308" width="800" frameborder="0" scrolling="auto"></iframe>

En utilisant la propriété `shape` d'un objet `Dataframe`, j'ai trouvé que le jeu de données contient 756 lignes et 18 colonnes. Pour trouver les noms de ces colonnes, j'ai utilisé la propriété `columns`. Elle a retourné une liste des colonnes dans un data frame.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=11" title="Jovian Viewer" height="138" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=13" title="Jovian Viewer" height="222" width="800" frameborder="0" scrolling="auto"></iframe>

Pour obtenir un résumé de ce que contient le data frame, j'ai utilisé `info()`. Cela donne des informations sur les colonnes, le nombre de valeurs non nulles dans chaque colonne, leur type de données et l'utilisation de la mémoire.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=15" title="Jovian Viewer" height="717" width="800" frameborder="0" scrolling="auto"></iframe>

Presque toutes les colonnes sauf `umpire3` n'ont pas ou très peu de valeurs nulles. La présence de valeurs nulles pourrait résulter d'un manque d'informations ou d'une entrée de données incorrecte.

Une chose intéressante à observer est que, bien qu'il n'y ait pas de valeurs nulles pour la colonne `result`, il y en a pour les colonnes `winner` et `player_of_match`. Découvrons pourquoi.

J'ai d'abord accédé à la colonne `result` en utilisant la _notation par point_ (`matches_raw_df.result`). Ensuite, j'ai utilisé la méthode `vaule_counts()` sur la colonne `result`.

`value_counts()` retourne une _série_ qui contient les comptes des valeurs uniques. Ici, elle nous informe des différentes valeurs présentes dans `result` et du nombre total pour chacune d'elles.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=18" title="Jovian Viewer" height="218" width="800" frameborder="0" scrolling="auto"></iframe>

Ainsi, sur 756 matchs (lignes), 4 matchs se sont terminés sans résultat.

Le cricket est un sport de plein air et contrairement, par exemple, au football, il n'est pas possible de jouer lorsqu'il pleut. Il est très courant que des matchs soient abandonnés en raison de pluies incessantes. Par conséquent, nous n'avons pas de vainqueurs ou de joueur du match pour ces 4 matchs.

Pour cette analyse, la colonne `umpire3` n'est pas nécessaire. J'ai donc supprimé la colonne en utilisant la méthode `drop()` en passant le nom de la colonne et la valeur de l'axe. Si vous souhaitez supprimer plusieurs colonnes, les noms des colonnes doivent être donnés dans une liste.

J'ai assigné ce data frame **nettoyé** à `matches_df`. J'ai utilisé ce data frame pour une analyse plus approfondie.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=22" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=23" title="Jovian Viewer" height="308" width="800" frameborder="0" scrolling="auto"></iframe>

## 3. Analyse exploratoire et visualisation

L'analyse exploratoire implique d'effectuer des opérations sur le jeu de données pour comprendre les données et trouver des motifs. Cela nous aide à donner un sens aux données que nous avons.

La visualisation est la représentation graphique des données. Elle implique la production de graphiques qui communiquent ces motifs parmi les données représentées aux spectateurs.

Maintenant, jetons un coup d'œil aux données que j'ai analysées et à ce que j'ai appris dans le processus.

### Nombre de matchs et d'équipes

J'ai essayé de trouver le nombre de matchs joués lors de chaque saison de l'IPL depuis sa création jusqu'en 2019.

Puisque je voulais les matchs joués chaque saison, il était logique de regrouper nos données selon les différentes saisons. Pandas a une méthode `groupby()` pour y parvenir, où j'ai passé `season` comme argument.

Puisqu'un `id` est unique pour chaque match (ligne), compter le nombre d'ids pour chaque saison conduit à ce que nous voulons. J'ai utilisé la méthode `count()` sur la colonne `id` pour trouver le nombre de matchs tenus chaque saison. Cette série est assignée à la variable `matches_per_season`.

J'ai ensuite utilisé la méthode `barplot()` de la bibliothèque Seaborn pour tracer la série. L'index de la série, c'est-à-dire les saisons, a été donné comme valeur x tandis que les valeurs de ces index ont été données comme valeurs y.

J'ai utilisé diverses méthodes `matpllotlib.pyplot` telles que `figure()`, `xticks()` et `title()` pour définir la taille du graphique, le titre du graphique, et ainsi de suite.

`figure` prend un paramètre, `figsize`, que j'ai défini à `(12,6)`. Remarquez que la taille a été donnée sous forme de tuple. À `xticks()`, j'ai donné au paramètre `rotation` une valeur de `75` pour faciliter la lecture.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=30" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=31" title="Jovian Viewer" height="565" width="800" frameborder="0" scrolling="auto"></iframe>

Chaque saison, presque 60 matchs ont été joués. Cependant, nous voyons une augmentation du nombre de matchs de 2011 à 2013. Cela est dû à l'introduction de deux nouvelles franchises, les **Pune Warriors** et **Kochi Tuskers Kerala**, ce qui a porté le nombre d'équipes à 10.

Cependant, Kochi a été retirée dès la saison suivante, tandis que les Pune Warriors ont été retirés en 2013, ramenant le nombre à 8 à partir de 2014.

Avant le début de la saison 2016, deux équipes, les **Chennai Super Kings** et **Rajasthan Royals**, ont été bannies pour deux saisons. Pour compenser leur absence, deux nouvelles équipes (les **Rising Pune Supergiants** et **Gujarat Lions**) ont rejoint la compétition.

Lorsque les Chennai Super Kings et Rajasthan Royals sont revenus, ces deux équipes ont été retirées de la compétition.

### Analyse des résultats du toss

L'un des événements les plus significatifs dans tout match de cricket est le toss, qui a lieu au tout début d'un match. Le vainqueur du toss peut choisir s'il veut battre en premier ou en second (fielding en premier).

Voyons quelle a été la tendance parmi les équipes au fil des différentes saisons.

J'ai à nouveau regroupé les lignes par saison puis compté les différentes valeurs de la colonne `toss_decision` en utilisant `value_counts()`.

Puisqu'un pourcentage donne une image plus claire, j'ai divisé le résultat ci-dessus par `matches_per_season` et multiplié par 100. Cette série a été assignée à `toss_decision_percentage`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=35" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=36" title="Jovian Viewer" height="643" width="800" frameborder="0" scrolling="auto"></iframe>

Ici, `toss_decision_percentage` est une série avec un _index multi-niveaux_. Si nous imprimons l'index de la série en utilisant la propriété `index`, nous voyons qu'il est de la forme `(2008, 'bat'), (2008, 'field')` et ainsi de suite.

La série a utilisé à la fois `season` et `toss_decision` comme index. Mais je ne voulais que les saisons comme index. J'ai utilisé `unstack()` pour y parvenir.

En utilisant la méthode `unstack()` sur la série, elle a converti les valeurs de `toss_decision` (c'est-à-dire, `bat` et `field`) en colonnes séparées.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/85&cellId=38" title="Jovian Viewer" height="490" width="800" frameborder="0" scrolling="auto"></iframe>

Ensuite, j'ai utilisé la méthode `plot()` de Matplotlib pour représenter ces valeurs sous forme de graphiques à barres. `plot()` a un paramètre `kind` qui décide du type de graphique à dessiner. La valeur a été définie sur `bar`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/85&cellId=39" title="Jovian Viewer" height="484" width="800" frameborder="0" scrolling="auto"></iframe>

De 2008 à 2013, les équipes semblaient favoriser à la fois la frappe en premier et en second. Pour cette période, les équipes ont choisi de frapper en premier plus en 2009, 2010 et 2013. D'autre part, elles ont choisi de fielding en premier plus en 2008 et 2011. Les choses étaient égales en 2012.

Cela pourrait être dû au fait que l'IPL et le cricket T20 en général étaient à leurs débuts. Donc, les équipes apprenaient probablement et essayaient de déterminer quelle option serait la plus bénéfique.

Cependant, depuis 2014, les équipes ont massivement choisi de frapper en second. Surtout depuis 2016, les équipes ont choisi de fielding en premier **plus de 80%** du temps.

Frapper en premier nécessite que l'équipe évalue les conditions et le terrain, puis fixe un objectif en conséquence. La poursuite est moins compliquée, car il y a un objectif fixe à atteindre.

Les conditions sont également devenues plus favorables aux batteurs et les compétences des batteurs ont considérablement augmenté (_lire plus_ [_ici_](https://www.espncricinfo.com/story/_/id/18568387/tim-wigmore-how-batting-second-become-more-fruitful-more-popular)).

### Nombre de victoires

Nous avons vu comment les équipes dans le passé récent ont choisi de frapper en second plus de 4 fois sur 5. Cette décision a-t-elle transformé les résultats ? Voyons cela.

Pour `wins_batting_first`, les valeurs de `win_by_wickets` doivent être 0. De plus, la colonne `result` doit avoir une valeur de `normal` puisque les matchs nuls ont également des marges de victoire de 0. Cette condition a été stockée sous `filter1`.

De même, pour `wins_fielding_first`, la valeur de `win_by_runs` doit être 0 et la colonne `result` doit avoir une valeur de `normal`. Cette condition a été stockée sous `filter1`.

Dans les deux séries, j'ai utilisé la méthode `count()` sur la colonne `winner` pour trouver les matchs gagnés dans les conditions filtrées. J'ai divisé les résultats par `matches_per_season` calculés précédemment pour donner une meilleure compréhension.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/88&cellId=43" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/88&cellId=44" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/88&cellId=45" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/89&cellId=46" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>

Pour tracer ces deux séries ensemble, je les ai combinées en utilisant la méthode `concat()` de Pandas. J'ai passé les noms des deux séries sous forme de liste et défini la valeur de `axis` à `1`. Cela nous donne un nouveau data frame qui a été stocké sous `combined_wins_df`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/89&cellId=47" title="Jovian Viewer" height="547" width="800" frameborder="0" scrolling="auto"></iframe>

Ensuite, j'ai tracé `combined_wins_df` sous forme de graphique à barres en utilisant `plot()`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=44" title="Jovian Viewer" height="484" width="800" frameborder="0" scrolling="auto"></iframe>

Nous avons vu précédemment que pour 2008-2013, les équipes faisaient face à un dilemme : frapper en premier ou fielding en premier. Cela est partiellement visible dans les résultats également.

Les victoires en frappant en premier sont très proches de celles en fielding en premier. Cependant, il n'y a qu'une seule saison où les équipes frappant en premier ont remporté plus de victoires, les choses étant égales en 2013.

À nouveau, depuis 2014, les choses ont été en faveur des équipes qui poursuivent, sauf en 2015. En excluant 2015, les choses ont été massivement en faveur des équipes fielding en premier.

Ainsi, les équipes choisissant de fielding plus ont été justifiées dans leurs décisions.

### Équipes avec "Histoire"

Dans les ligues de différents sports, il y a toujours des discussions sur les équipes avec "histoire" - les équipes qui ont le plus joué dans la ligue et continuent de le faire. Trouvons ces équipes dans l'IPL.

Maintenant, entre deux équipes A et B, cela peut être "A vs B" ou "B vs A", selon la manière dont l'entrée de données a été faite. J'ai donc décidé de compter le nombre total de valeurs différentes pour les colonnes `team1` et `team2` en utilisant `value_counts()`. Ensuite, je les ai additionnées.

J'ai trié les résultats par ordre décroissant en utilisant la méthode `sort_values()` de Pandas. Le paramètre `ascending` a été défini sur `False`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=48" title="Jovian Viewer" height="470" width="800" frameborder="0" scrolling="auto"></iframe>

Ici, j'ai utilisé `sns.barplot()` pour tracer le graphique.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=49" title="Jovian Viewer" height="451" width="800" frameborder="0" scrolling="auto"></iframe>

Les **Mumbai Indians** ont joué le plus de matchs. Ils sont suivis par les Royal Challengers Bangalore, Kolkata Knight Riders, Kings XI Punjab et Chennai Super Kings.

Les Chennai Super Kings et Rajasthan Royals auraient pu être plus haut s'ils n'avaient pas été bannis.

Vous verrez qu'il y a deux équipes de Delhi, les **Delhi Daredevils** et **Delhi Capitals**. Cela résulte d'un changement de propriété puis de nom d'équipe en 2018.

C'est une histoire similaire pour les **Deccan Chargers** et **Sunrisers Hyderabad**, car les Deccan Chargers ont été retirés de l'IPL en 2013 et les Sunrisers sont venus à leur place.

De plus, il y a deux équipes avec presque le même nom : les **Rising Pune Supergiants** et **Rising Pune Supergiant**. Ils sont la même équipe, et il n'y a pas eu de changement de propriété - cela a plus à voir avec des superstitions.

Lors de la saison 2016, les Rising Pune Supergiants ont terminé 7èmes. Les propriétaires ont changé le capitaine pour 2017 et ont également **supprimé le 's'** de Supergiants. Eh bien, cela a porté ses fruits car ils ont terminé comme finalistes cette saison-là !

### Équipes avec "Héritage"

Maintenant, les équipes peuvent avoir beaucoup d'histoire, mais c'est leur "héritage" - à quelle fréquence elles gagnent - qui les rend populaires et attire de nouveaux fans et des fans neutres.

Pour trouver de telles équipes, j'ai simplement utilisé `value_counts()` sur la colonne `winner`. Cela nous donne le nombre de matchs que chaque équipe a remportés.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=53" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=54" title="Jovian Viewer" height="433" width="800" frameborder="0" scrolling="auto"></iframe>

Ainsi, Mumbai a le plus de victoires. Mais une meilleure métrique pour juger serait le pourcentage de victoires. Pour trouver le pourcentage de victoires, j'ai divisé `most_wins` par `total_matches_played` pour trouver le `win_percentage` pour chaque équipe.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=57" title="Jovian Viewer" height="88" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=58" title="Jovian Viewer" height="444" width="800" frameborder="0" scrolling="auto"></iframe>

Le Rising Pune Supergiant et les Delhi Capitals ont le pourcentage de victoires le plus élevé. Cela est largement dû au fait qu'ils ont joué moins de matchs par rapport à la plupart des équipes. Surtout le Rising Pune Supergiant, qui est techniquement devenu une nouvelle équipe après avoir supprimé le 's'.

Les Chennai Super Kings, malgré avoir joué deux saisons de moins que les Mumbai Indians, n'avaient que 9 victoires de moins. Ils, ainsi que les Mumbai Indians, sont les seules équipes du top 5 qui faisaient également partie de l'IPL en 2008.

**Chennai** et **Mumbai** sont les équipes avec le plus d'héritage.

## 4. Poser et répondre à des questions à partir des données

Nous avons déjà obtenu quelques informations sur l'IPL en explorant diverses colonnes de notre jeu de données.

Posons quelques questions spécifiques et essayons d'y répondre en utilisant des opérations de data frame et des visualisations intéressantes.

### Q. Qui a remporté le tournoi de l'IPL ?

* Regrouper les lignes selon les saisons en utilisant `groupby()`.
* Trouver le dernier match de chaque saison, c'est-à-dire la finale en utilisant `tail()`. Il retourne les dernières n lignes d'un objet Dataframe ou d'une série en fonction de la position.
* Trier les valeurs par saison en utilisant `sort_values()`.
* Compter les différents vainqueurs et le nombre de fois où ils ont gagné en utilisant `value_counts()` sur `winner`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=65" title="Jovian Viewer" height="134" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=66" title="Jovian Viewer" height="264" width="800" frameborder="0" scrolling="auto"></iframe>

Ensuite, j'ai tracé la série `ipl_winners` en utilisant `sns.barplot()`.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=67" title="Jovian Viewer" height="353" width="800" frameborder="0" scrolling="auto"></iframe>

Mumbai et Chennai, nos équipes _héritage_, ont remporté l'IPL au moins 3 fois. Les Sunrisers Hyderabad sont la seule équipe qui a rejoint la ligue plus tard et a remporté le trophée.

### Q. Quelles sont les équipes les plus et les moins constantes à travers toutes les saisons ?

* Créé un data frame entre différentes valeurs de `winner` et `season` en utilisant `pd.crosstab()`.
* Tracé le data frame sous forme de heatmap.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=71" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=72" title="Jovian Viewer" height="208" width="800" frameborder="0" scrolling="auto"></iframe>

`pd.crosstab()` donne une simple tabulation croisée des colonnes `winner` et `season`. Pour chaque valeur différente de `winner`, `pd.crosstab()` trouve sa fréquence pour chaque valeur différente dans `season`.

Ensuite, j'ai tracé `matches_won_each_season` en utilisant `sns.heatmap()`. J'ai passé le data frame `matches_won_each_season`, avec `annot` à `True` pour avoir les valeurs affichées également. Ici, la couleur plus foncée indique plus de matchs gagnés.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=73" title="Jovian Viewer" height="496" width="800" frameborder="0" scrolling="auto"></iframe>

Les **Chennai Super Kings** ont été l'équipe la plus constante, remportant au moins 8 matchs lors de chacune des saisons où ils ont joué. Cela est soutenu par le fait qu'ils sont la **seule** équipe à atteindre le stade des playoffs chaque saison.

À l'autre extrémité du spectre se trouvent 3 équipes, les **Delhi Daredevils**, **Kings XI Punjab** et **Rajasthan Royals**. Toutes les trois ont eu deux saisons où elles ont très bien performé. Cependant, elles ont été assez moyennes lors des autres saisons.

### Q. Quelle a été la plus grande marge de victoire en termes de runs dans l'IPL ?

* Filtrer le data frame en utilisant la condition requise.
* Trier les valeurs par ordre décroissant en utilisant `sort_values()`.
* Trouver les 10 plus grandes victoires de la liste en utilisant la méthode `head()`. Elle fonctionne à l'opposé de `tail()`, retournant les premières n lignes.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=81" title="Jovian Viewer" height="134" width="800" frameborder="0" scrolling="auto"></iframe>

J'ai tracé le data frame filtré `highest_wins_by_runs_df` en utilisant `sns.scatterplot()`. Pour le paramètre `x`, j'ai utilisé `season`, et j'ai utilisé `win_by_runs` comme paramètre `y`. J'ai agrandi la taille des points pour les 10 meilleures victoires en utilisant le paramètre `s`.

Pour mettre l'accent sur les 10 meilleures victoires, j'ai également utilisé une couleur différente et annoté ces points de données en utilisant `plt.annotate()`. Le premier paramètre est le texte de l'annotation. La position du point à annoter est donnée sous forme de tuple.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=82" title="Jovian Viewer" height="501" width="800" frameborder="0" scrolling="auto"></iframe>

La plus grande marge de victoire en termes de runs est de **146 runs**. En 2017, les Mumbai Indians ont battu les Delhi Daredevils par cette marge. Les Royal Challengers Bangalore ont 3 victoires parmi les 5 premières.

### Q. Mumbai et Chennai sont les deux équipes les plus performantes jusqu'à présent. Quelle équipe mène dans les confrontations directes ?

* Filtrer le data frame en utilisant la condition requise pour trouver les matchs joués entre les deux équipes.
* Utiliser `value_counts()` sur la colonne `winner` pour trouver combien de fois chacune des équipes a gagné.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=105" title="Jovian Viewer" height="105" width="800" frameborder="0" scrolling="auto"></iframe>
<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=108" title="Jovian Viewer" height="180" width="800" frameborder="0" scrolling="auto"></iframe>

J'ai tracé la série `mivcsk` sous forme de graphique à barres pour une meilleure visualisation.

<iframe src="https://jovian.ai/embed?url=https://jovian.ai/srijansrj5901/ipl-data-analysis/v/83&cellId=109" title="Jovian Viewer" height="507" width="800" frameborder="0" scrolling="auto"></iframe>

MI a dominé CSK et mène les confrontations directes 17-11. Nous pouvons voir leur domination surtout lors de la saison 2019, où MI a battu CSK 4 fois sur 4 lorsqu'ils se sont rencontrés, y compris les playoffs et la finale.

## 5. Inférences de l'analyse

Nous avons tiré quelques inférences intéressantes et en savons maintenant plus sur l'IPL que lorsque nous avons commencé. Voici un résumé de ce que nous avons appris grâce à notre analyse :

* Presque 60 matchs sont joués chaque saison de l'IPL parmi 8 équipes.
* Il y a eu une tentative d'étendre l'IPL à 10 équipes, mais l'idée des 8 équipes a été ramenée et a été continuée depuis.
* Pendant les six premières saisons (2008-2013), les équipes essayaient de déterminer si frapper en premier ou poursuivre serait mieux après avoir gagné le toss. Cela pourrait être dû au fait que l'IPL et le cricket T20 étaient tous deux à leurs débuts, donc les équipes essayaient différentes stratégies.
* Mais, depuis 2014, les équipes ont préféré poursuivre, surtout lors des 4 dernières saisons (2016-2019) où les équipes ont choisi de fielding plus de 4 fois sur 5. Cela est probablement dû au fait qu'avoir un total fixe à poursuivre simplifie les choses. Cela pourrait également résulter du fait que les équipes préfèrent poursuivre dans les ODIs également.
* Bien que les équipes aient massivement choisi de fielding en premier, le pourcentage de victoires après avoir choisi de frapper ou de fielding n'est pas si unilatéral. Cependant, leur différence est en hausse.
* Les Mumbai Indians ont joué le plus de matchs dans l'IPL. En raison de la brève expansion, du changement de propriétaires, et du retrait et de l'interdiction d'équipes, il y a eu 15 équipes qui ont joué dans l'IPL.
* Chennai et Mumbai sont les deux équipes avec le pourcentage de victoires le plus élevé. Le fait qu'ils soient les seules équipes qui faisaient également partie de la première saison, dans le top 5, montre leur domination.
* Les Mumbai Indians ont remporté l'IPL 4 fois, le plus. Ils sont suivis par Chennai avec 3 et Kolkata Knight Riders avec 2. Sunrisers Hyderabad, Deccan Chargers et Rajasthan Royals complètent la liste des champions de l'IPL, ayant chacun remporté une fois.
* 146 runs est la plus grande marge de victoire en termes de runs. Les Mumbai Indians ont battu les Delhi Daredevils par cette marge en 2017. La plus grande marge de victoire en termes de wickets est de 10, qui a été atteinte à plusieurs reprises.
* Les deux poids lourds, Mumbai et Chennai, ont un bilan en confrontations directes en faveur de Mumbai à 17-11. Mumbai a eu le dessus lors de la saison 2019 à chaque fois qu'ils se sont rencontrés, y compris la finale.

## 6. Conclusion

Dans cet article, nous avons fait un tas d'analyses et vu quelques visualisations intéressantes. Cependant, ce n'était que la surface.

Vous pouvez effectuer des analyses plus intéressantes sur _matches.csv_ en tant que jeu de données autonome. Mais combiner _deliveries.csv_ avec ce jeu de données pourrait conduire à une analyse plus approfondie.

J'ai fait cette analyse de données et cette visualisation dans le cadre d'un projet pour le cours de 6 semaines [Data Analysis with Python: Zero to Pandas](https://www.freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn/zerotopandas.com). Ce cours a été mené par [Jovian.ml](https://jovian.ml) en partenariat avec [freeCodeCamp.org](https://www.freecodecamp.org/news/kaggle-dataset-analysis-with-pandas-matplotlib-seaborn/www.freecodecamp.org). Consultez le projet [ici](https://jovian.ml/srijansrj5901/ipl-data-analysis).

De plus, l'IPL est en cours en ce moment. Allez le regarder et profitez-en !