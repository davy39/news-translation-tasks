---
title: Deux heures plus tard et toujours en cours d'exécution ? Comment garder votre
  sklearn.fit sous contrôle.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-13T15:36:10.000Z'
originalURL: https://freecodecamp.org/news/two-hours-later-and-still-running-how-to-keep-your-sklearn-fit-under-control-cc603dc1283b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg
tags:
- name: Data Sc
  slug: data-sc
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: scikit learn
  slug: scikit-learn
- name: timer
  slug: timer
seo_title: Deux heures plus tard et toujours en cours d'exécution ? Comment garder
  votre sklearn.fit sous contrôle.
seo_desc: 'By Nathan Toubiana

  Written by Gabriel Lerner and Nathan Toubiana

  All you wanted to do was test your code, yet two hours later your Scikit-learn fit
  shows no sign of ever finishing. Scitime is a package that predicts the runtime
  of machine learning al...'
---

Par Nathan Toubiana

_Ecrit par [Gabriel Lerner](https://medium.com/@gabi10004) et [Nathan Toubiana](https://medium.com/@toubiana.nathan)_

Tout ce que vous vouliez faire était de tester votre code, pourtant deux heures plus tard, votre ajustement Scikit-learn ne montre aucun signe de fin. Scitime est un package qui prédit le temps d'exécution des algorithmes de machine learning afin que vous ne soyez pas pris au dépourvu par un ajustement sans fin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aVzJTznRRfP1lM7AXe9yLw.jpeg)
_Image par Kevin Ku sur [unsplash.com](https://unsplash.com/photos/aiyBwbrWWlo" rel="noopener" target="_blank" title=")_

Que vous soyez en train de construire un modèle de machine learning ou de déployer votre code en production, connaître le temps que votre algorithme prendra pour s'ajuster est essentiel pour rationaliser votre flux de travail. Avec Scitime, vous pourrez en quelques secondes estimer combien de temps l'ajustement devrait prendre pour les algorithmes Scikit Learn les plus couramment utilisés.

Il y a eu quelques articles de recherche (comme [celui-ci](https://www.sciencedirect.com/science/article/pii/S0004370213001082)) publiés sur ce sujet. Cependant, autant que nous sachions, il n'y a pas d'implémentation pratique de cela. Le but ici n'est pas de prédire le temps d'exécution exact de l'algorithme, mais plutôt de donner une approximation grossière.

### Qu'est-ce que Scitime ?

Scitime est un package Python nécessitant au moins Python 3.6 avec les dépendances [pandas](https://github.com/pandas-dev/pandas), [scikit-learn](https://github.com/scikit-learn/scikit-learn), [psutil](https://github.com/giampaolo/psutil) et [joblib](https://github.com/joblib/joblib). Vous trouverez le dépôt Scitime [ici](https://github.com/nathan-toubiana/scitime).

La fonction principale de ce package s'appelle "_time_". Étant donné une matrice vectorielle X, le vecteur estimé Y ainsi que le modèle Scikit Learn de votre choix, _time_ fournira à la fois le temps estimé et son intervalle de confiance. Le package prend actuellement en charge les algorithmes Scikit Learn suivants avec des plans pour en ajouter d'autres dans un proche avenir :

* [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
* [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
* [SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
* [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

### Guide de démarrage rapide

Installons le package et exécutons les bases.

Tout d'abord, créez un nouvel environnement virtuel (c'est facultatif, pour éviter tout conflit de version !)

```
 virtualenv env source env/bin/activate
```

puis exécutez :

```
 (env) pip install scitime
```

ou avec conda :

```
 (env) conda install -c conda-forge scitime
```

Une fois l'installation réussie, vous êtes prêt à estimer le temps de votre premier algorithme.

Supposons que vous souhaitiez entraîner un clustering kmeans, par exemple. Vous devriez d'abord importer le package scikit-learn, définir les paramètres kmeans, et également choisir les entrées (a.k.a _X_), ici générées [aléatoirement](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs) pour simplifier.

Exécuter cela avant de faire l'ajustement réel donnerait une approximation du temps d'exécution :

Comme vous pouvez le voir, vous pouvez obtenir cette info en une seule ligne de code supplémentaire ! Les entrées de la fonction _time_ sont exactement ce dont vous avez besoin pour exécuter l'ajustement (c'est-à-dire l'algo lui-même, et X), ce qui la rend encore plus facile à utiliser.

En regardant de plus près la dernière ligne du code ci-dessus, la première sortie (_estimation :_ 15 secondes dans ce cas) est le temps d'exécution prédit que vous recherchez. Scitime fournira également un intervalle de confiance (_lower_bound_ et _upper_bound :_ 10 et 30 secondes dans ce cas). Vous pouvez toujours le comparer au temps de formation réel en exécutant :

Dans ce cas, sur notre machine locale, l'estimation est de 15 secondes, tandis que le temps de formation réel est de 20 secondes (mais vous pourriez ne pas obtenir les mêmes résultats, comme nous l'expliquerons plus tard).

**En tant que guide d'utilisation rapide :**

_Estimator(meta_algo, verbose, confidence) class :_

* **meta_algo** : L'estimateur utilisé pour prédire le temps, soit 'RF' soit 'NN' (voir les détails dans le paragraphe suivant) — par défaut 'RF'
* **verbose** : Contrôle de la quantité de sortie de journal (soit 0, 1, 2 ou 3) — par défaut 0
* **confidence** : Confiance pour les intervalles — par défaut 95%

_estimator.time(algo, X, y) function :_

* **algo** : algo dont le temps d'exécution l'utilisateur veut prédire
* **X** : tableau numpy des entrées à entraîner
* **y** : tableau numpy des sorties à entraîner (définir à _None_ si l'algo est non supervisé)

Note rapide : pour éviter toute confusion, il est utile de souligner que **algo** et **meta_algo** sont deux choses différentes ici : **algo** est l'algorithme dont nous voulons estimer le temps d'exécution, **meta_algo** est l'algorithme utilisé par Scitime pour prédire le temps d'exécution.

### Comment fonctionne Scitime

Nous sommes capables de prédire le temps d'exécution de l'ajustement en utilisant notre propre estimateur, que nous appelons meta algorithme (_meta_algo_), dont les poids sont stockés dans un fichier pickle dédié dans les métadonnées du package. Pour chaque modèle Scikit Learn, vous trouverez un fichier pickle meta algo correspondant dans la base de code de Scitime.

Vous pourriez penser :

> Pourquoi ne pas estimer manuellement la complexité temporelle avec les notations big O ?

C'est un point valable. C'est une manière valide d'aborder le problème et quelque chose à quoi nous avons pensé au début du projet. Une chose cependant est que nous devrions formuler la complexité explicitement pour chaque algo et ensemble de paramètres, ce qui est plutôt difficile dans certains cas, étant donné le nombre de facteurs jouant un rôle dans le temps d'exécution. Le meta_algo fait essentiellement tout le travail pour vous, et nous expliquerons comment.

Deux types de meta algos ont été entraînés pour estimer le temps d'ajustement (tous deux de Scikit Learn) :

* Le **RF** meta algo, un estimateur [RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html).
* Le **NN** meta algo, un estimateur [MLPRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html) de base.

Ces meta algos estiment le temps d'ajustement en utilisant un tableau de caractéristiques 'meta'. Voici un résumé de la manière dont nous construisons ces caractéristiques :

Tout d'abord, nous récupérons la forme de votre matrice d'entrée X et du vecteur de sortie y. Ensuite, les paramètres que vous fournissez au modèle Scikit Learn sont pris en considération car ils auront également un impact sur le temps d'entraînement. Enfin, votre matériel spécifique, unique à votre machine, tel que la mémoire disponible et le nombre de CPU, sont également pris en compte.

Comme montré précédemment, nous fournissons également des intervalles de confiance sur la prédiction de temps. La manière dont ceux-ci sont calculés dépend du meta algo choisi :

* Pour **RF**, puisque tout régresseur de forêt aléatoire est une combinaison de plusieurs arbres (également appelés _estimateurs_), l'intervalle de confiance sera basé sur la distribution de l'ensemble des prédictions calculées par chaque estimateur.
* Pour **NN**, le processus est un peu moins direct : nous calculons d'abord un ensemble de [MSE](https://en.wikipedia.org/wiki/Mean_squared_error) ainsi que le nombre d'observations sur un ensemble de test, regroupés par tranches de durée prédite (c'est-à-dire de 0 à 1 seconde, 1 à 5 secondes, et ainsi de suite), puis nous calculons un [t-stat](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.t.html) pour obtenir les bornes inférieure et supérieure de l'estimation. Comme nous n'avons pas beaucoup de données pour les modèles très longs, l'intervalle de confiance pour ces données peut devenir très large.

### Comment nous l'avons construit

Vous pourriez penser :

> Comment avez-vous obtenu suffisamment de données sur le temps d'entraînement de tous ces ajustements scikit-learn sur diverses configurations de paramètres et de matériel ?

La réponse (peu glamour) est que nous avons généré les données nous-mêmes en utilisant une combinaison d'ordinateurs et de matériels de machines virtuelles pour simuler le temps d'entraînement sur différents systèmes. Nous avons ensuite ajusté nos meta algos sur ces points de données générés aléatoirement pour construire un estimateur destiné à être fiable, quel que soit votre système.

Alors que le fichier [estimate.py](https://github.com/nathan-toubiana/scitime/blob/master/scitime/estimate.py) gère la prédiction du temps d'exécution, le fichier [__model.py_](https://github.com/nathan-toubiana/scitime/blob/master/scitime/_model.py) nous a aidés à générer des données pour entraîner nos meta algos, en utilisant notre classe Model dédiée. Voici un exemple de code correspondant, pour kmeans :

Notez que vous pouvez également utiliser le fichier [__data.py_](https://github.com/nathan-toubiana/scitime/blob/master/_data.py) directement avec la ligne de commande pour générer des données ou entraîner un nouveau modèle. Les instructions connexes peuvent être trouvées dans le fichier Readme du dépôt.

Lors de la génération de points de données, vous pouvez modifier les paramètres des modèles Scikit Learn que vous souhaitez entraîner. Vous pouvez vous rendre dans [_scitime/_config.json_](https://github.com/nathan-toubiana/scitime/blob/master/scitime/_config.json) et modifier les paramètres des modèles ainsi que le nombre de lignes et de colonnes avec lesquelles vous souhaitez vous entraîner.

Nous utilisons une fonction [itertool](https://docs.python.org/2/library/itertools.html#itertools.product) pour boucler à travers chaque combinaison possible, ainsi qu'un taux de chute défini entre 0 et 1 pour contrôler la rapidité avec laquelle la boucle passera à travers les différentes itérations possibles.

### À quel point Scitime est-il précis ?

Ci-dessous, nous mettons en évidence comment nos prédictions se comportent pour le cas spécifique de kmeans. Notre ensemble de données généré contient ~100k points de données, que nous divisons en ensembles d'entraînement et de test (75% — 25%).

Nous avons regroupé les temps prédits d'entraînement par différents intervalles de temps et calculé le [MAPE](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error) et le [RMSE](https://en.wikipedia.org/wiki/Root-mean-square_deviation) sur chacun de ces intervalles pour tous nos estimateurs en utilisant le meta-algo RF et le meta-algo NN.

Veuillez noter que ces résultats ont été obtenus sur un ensemble de données restreint, ils peuvent donc être différents sur des points de données inexplorés (comme d'autres systèmes / valeurs extrêmes de certains paramètres de modèle). Pour cet ensemble d'entraînement spécifique, le [R-carré](https://en.wikipedia.org/wiki/Coefficient_of_determination) est d'environ 80% pour NN et 90% pour RF.

Comme nous pouvons le voir, sans surprise, la précision est constamment plus élevée sur l'ensemble d'entraînement que sur le test, pour NN et RF. Nous voyons également que RF semble performer bien mieux que NN dans l'ensemble. Le MAPE pour RF est d'environ 20% sur l'ensemble d'entraînement et 40% sur l'ensemble de test. Le MAPE de NN est surprenamment très élevé.

Découpons le MAPE (sur l'ensemble de test) par le nombre de secondes prédites :

Une chose importante à garder à l'esprit est que pour certains cas, la prédiction de temps est sensible au meta algo choisi (RF ou NN). Dans notre expérience, RF a très bien performé dans les plages de données d'entrée, comme montré ci-dessus. Cependant, pour les points hors plage, NN pourrait performer mieux, comme suggéré par la fin du graphique ci-dessus. Cela expliquerait pourquoi le MAPE de NN est assez élevé tandis que le RMSE est décent : il performe mal sur les petites valeurs.

Par exemple, si vous essayez de prédire le temps d'exécution d'un kmeans avec des paramètres par défaut et avec une matrice d'entrée de quelques milliers de lignes, le meta algo RF sera précis car notre ensemble de données d'entraînement contient des points de données similaires. Cependant, pour prédire des paramètres très spécifiques (par exemple, un nombre très élevé de clusters), NN pourrait performer mieux car il extrapole à partir de l'ensemble d'entraînement, alors que RF ne le fait pas. NN performe moins bien sur les graphiques ci-dessus car ces graphiques sont uniquement basés sur des données proches de l'ensemble des entrées des données d'entraînement.

Cependant, comme montré dans ce graphique, les valeurs hors plage (lignes fines) sont extrapolées par l'estimateur NN, tandis que l'estimateur RF prédit la sortie par étapes.

Maintenant, regardons les caractéristiques 'meta' les plus importantes pour l'exemple de kmeans :

Comme nous pouvons le voir, seulement 6 caractéristiques représentent plus de 80% de la variance du modèle. Parmi elles, la plus importante est un paramètre de la classe kmeans de scikit-learn elle-même (nombre de clusters), mais de nombreux facteurs externes ont une grande influence sur le temps d'exécution, comme le nombre de lignes/colonnes et la mémoire disponible.

### Limites

Comme mentionné précédemment, la première limite est liée aux intervalles de confiance : ils peuvent être très larges, surtout pour NN, et pour les modèles lourds (qui prendraient au moins une heure).

De plus, le NN peut mal performer sur les prédictions petites à moyennes. Parfois, pour les petites durées, le NN peut même prédire une durée négative, auquel cas nous basculons automatiquement vers RF.

Une autre limite de l'estimateur survient lorsque des valeurs de paramètres d'algo 'spéciales' sont utilisées. Par exemple, dans un scénario RandomForest, lorsque max_depth est défini sur _None_, la profondeur pourrait prendre n'importe quelle valeur. Cela pourrait entraîner un temps d'ajustement beaucoup plus long, ce qui est plus difficile pour le meta algo à détecter, bien que nous ayons fait de notre mieux pour les prendre en compte.

Lors de l'exécution de _estimator.time(algo, X, y)_, nous exigeons que l'utilisateur entre le vecteur X et y réel, ce qui semble inutile, car nous pourrions simplement demander la forme des données pour estimer le temps d'entraînement. La raison en est que nous essayons en fait d'ajuster le modèle avant de prédire le temps d'exécution, afin de lever toute erreur instantanée. Nous exécutons _algo.fit(X, y)_ dans un sous-processus pendant une seconde pour vérifier toute erreur d'ajustement après quoi nous passons à la partie prédiction. Cependant, il arrive que l'algo (et/ou la matrice d'entrée) soient si grands que l'exécution de _algo.fit(X,y)_ finira par lancer une erreur de mémoire, que nous ne pouvons pas prendre en compte.

### Améliorations futures

La manière la plus efficace et évidente d'améliorer les performances de nos prédictions actuelles serait de générer plus de points de données sur différents systèmes pour mieux supporter une large gamme de matériel/paramètres.

Nous chercherons à ajouter plus d'algos Scikit Learn pris en charge dans un proche avenir. Nous pourrions également implémenter d'autres algos tels que [lightGBM](https://github.com/Microsoft/LightGBM) ou [xgboost](https://github.com/dmlc/xgboost). N'hésitez pas à nous contacter si vous souhaitez que nous implémentions un algorithme dans les prochaines itérations de Scitime !

D'autres pistes intéressantes pour améliorer les performances de l'estimateur consisteraient à inclure des informations plus granulaires sur la matrice d'entrée telles que la variance ou la corrélation avec la sortie. Nous générons actuellement des données complètement aléatoires, pour lesquelles le temps d'ajustement peut être plus élevé que pour les ensembles de données du monde réel. Donc, dans certains cas, cela peut surestimer le temps d'entraînement.

De plus, nous pourrions suivre des informations spécifiques au matériel plus fines telles que la fréquence du CPU ou l'utilisation actuelle du CPU.

Idéalement, comme l'algorithme peut changer d'une version scikit-learn à une autre, et avoir ainsi un impact sur le temps d'exécution, nous en tiendrions également compte, par exemple en utilisant la version comme caractéristique 'meta'.

À mesure que nous acquérons plus de données pour ajuster nos meta algos, nous pourrions envisager d'utiliser des meta algos plus complexes, tels que des réseaux de neurones sophistiqués (utilisant des techniques de régularisation comme le dropout ou la normalisation par lots). Nous pourrions même envisager d'utiliser [tensorflow](https://www.tensorflow.org) pour ajuster le meta algo (et l'ajouter en option) : cela nous aiderait non seulement à obtenir une meilleure précision, mais aussi à construire des intervalles de confiance plus robustes en utilisant le [dropout](https://towardsdatascience.com/uncertainty-estimation-for-neural-network-dropout-as-bayesian-approximation-7d30fc7bc1f2).

### Contribuer à Scitime et nous envoyer vos commentaires

Tout d'abord, tout type de commentaire, en particulier sur les performances des prédictions et sur les idées pour améliorer ce processus de génération de données, est grandement apprécié !

Comme discuté précédemment, vous pouvez utiliser notre dépôt pour générer vos propres points de données afin d'entraîner votre propre meta algorithme. En faisant cela, vous pouvez aider à améliorer Scitime en partageant vos points de données trouvés dans le fichier csv de résultat (_~/scitime/scitime/[algo]_results.csv_) afin que nous puissions les intégrer à notre modèle.

Pour générer vos propres données, vous pouvez exécuter une commande similaire à celle-ci (à partir de la source du dépôt du package) :

```
 python _data.py --verbose 3 --algo KMeans --drop_rate 0.99
```

Note : si vous exécutez directement en utilisant la source du code (avec la classe _Model_), n'oubliez pas de définir _write_csv_ à true, sinon les points de données générés ne seront pas sauvegardés.

_Nous utilisons les problèmes GitHub pour suivre tous les bugs et les demandes de fonctionnalités. N'hésitez pas à ouvrir un problème si vous avez trouvé un bug ou souhaitez voir une nouvelle fonctionnalité implémentée. Plus d'informations peuvent être trouvées sur la manière de contribuer dans le dépôt Scitime._

_Pour les problèmes avec les prédictions de temps d'entraînement, lors de l'envoi de commentaires, inclure le dictionnaire complet des paramètres que vous ajustez dans votre modèle pourrait aider, afin que nous puissions diagnostiquer pourquoi la performance est médiocre pour votre cas d'utilisation spécifique. Pour ce faire, définissez simplement le paramètre verbose à 3 et copiez-collez le journal du dictionnaire de paramètres dans la description du problème._

_Trouvez la [source du code](https://github.com/nathan-toubiana/scitime)_

_Trouvez la [documentation](https://scitime.readthedocs.io)_

### Crédits

* [_Gabriel Lerner_](https://github.com/gabrielRTR) _& [Nathan Toubiana](https://github.com/nathan-toubiana) sont les principaux contributeurs de ce package et co-auteurs de cet article_
* _Un merci spécial à [Philippe Mizrahi](https://github.com/philippemizrahi) pour son aide tout au long du chemin_
* _Merci pour toute l'aide que nous avons reçue des premières critiques / tests bêta_