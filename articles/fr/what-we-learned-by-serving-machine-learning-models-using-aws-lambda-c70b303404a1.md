---
title: Ce que nous avons appris en servant des modèles de Machine Learning avec AWS
  Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-30T21:29:22.000Z'
originalURL: https://freecodecamp.org/news/what-we-learned-by-serving-machine-learning-models-using-aws-lambda-c70b303404a1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IpYwXDmIfFQj4lDE-QfHFA.jpeg
tags:
- name: AI
  slug: ai
- name: AWS
  slug: aws
- name: Machine Learning
  slug: machine-learning
- name: 'tech '
  slug: tech
- name: TensorFlow
  slug: tensorflow
seo_title: Ce que nous avons appris en servant des modèles de Machine Learning avec
  AWS Lambda
seo_desc: 'By Daitan

  Moving machine learning (ML) models from training to serving in production at scale
  is an open problem. Many software vendors and cloud providers are currently trying
  to properly address this issue.

  One of the biggest challenges is that ser...'
---

Par Daitan

Passer des modèles de machine learning (ML) de l'entraînement à la mise en production à grande échelle est un problème ouvert. De nombreux éditeurs de logiciels et fournisseurs de cloud tentent actuellement de résoudre ce problème de manière adéquate.

L'un des plus grands défis est que servir un modèle (c'est-à-dire accepter des requêtes et retourner une prédiction) n'est qu'une partie du problème. Il existe une longue liste d'exigences adjacentes. Celles-ci incluent, par exemple :

* La gestion des versions des modèles
* Le réentraînement (automatique ou à la demande)
* Le prétraitement des entrées avant les prédictions
* La mise à l'échelle de l'infrastructure à la demande

Afin de mieux conseiller nos équipes à cet égard, nous avons mis en place un petit groupe de recherche, mais intelligent et dédié, ici chez [Daitan Group](https://medium.com/@DaitanGroup).

Pour commencer, nous avons établi une feuille de route pour apprendre les exigences et les pièges du déploiement de modèles de machine learning dans plusieurs pipelines ML et infrastructures.

Le but de cet article est de fournir un aperçu de notre méthodologie et des résultats que nous avons obtenus à partir de notre implémentation de référence.

### Création d'une référence de base

[Amazon SageMaker](https://aws.amazon.com/sagemaker/), [Google Cloud ML](https://cloud.google.com/ml-engine/), [Seldon Core](https://www.seldon.io/open-source/), et d'autres promettent un pipeline fluide, de bout en bout, de l'entraînement à la mise en production à grande échelle. Cependant, avant de travailler avec de telles solutions, nous voulions nous salir les mains avec un processus manuel pour créer une référence de base.

L'objectif était d'entraîner, d'exporter et de servir à grande échelle un modèle ML dans le cloud avec le moins d'efforts possible.

Pour commencer, nous avons choisi [TensorFlow](https://www.tensorflow.org/) comme framework ML et [AWS Lambda](https://aws.amazon.com/lambda/) comme infrastructure de déploiement. Nous avons utilisé [Apache JMeter](http://jmeter.apache.org/) et [Taurus](https://gettaurus.org/) pour générer des tests de charge.

Notre référence de base était basée sur l'expérimentation des combinaisons suivantes :

* Un modèle ML léger
* Dans différentes configurations d'AWS Lambda
* En utilisant deux langages de programmation populaires — Python et Java

Avec certaines combinaisons, nous avons atteint **~40 prédictions par seconde** avec un **temps de réponse moyen de ~200ms**. De tels résultats pourraient répondre à de nombreux cas d'utilisation en production. Et nous pourrions facilement monter en charge, si nécessaire.

Cependant, il y avait des pièges, que nous discutons ci-dessous lorsque nous détaillons les résultats des tests.

De plus, une deuxième expérience avec un modèle plus "lourd" (modèle de segmentation d'images) a été réalisée, qui sera détaillée dans un article de suivi.

#### Pourquoi TensorFlow et AWS Lambda ?

TensorFlow est une bibliothèque open-source créée par Google pour programmer des flux de données à travers une gamme de tâches. Nous avons commencé avec TF pour plusieurs raisons :

* C'est actuellement le framework de machine learning le plus populaire sur GitHub avec environ [110k étoiles et 1.6k contributeurs](https://github.com/tensorflow/tensorflow)
* Il accumule un certain nombre d'histoires de succès et est disponible sur plusieurs plateformes
* Il devient de mieux en mieux en tant que framework large pour le ML, pas seulement pour le deep learning

Ces facteurs, combinés, font de TF un candidat naturel pour nos clients lorsqu'ils construisent des modèles prédictifs.

AWS Lambda est l'implémentation par Amazon de l'architecture [Function-as-a-Service (FaaS) ou Serverless](https://martinfowler.com/articles/serverless.html). Nous avons remarqué une augmentation significative de son utilisation au cours des dernières années.

Certains de ses utilisateurs les plus fervents incluent des entreprises comme Netflix et Coca-Cola. Des études récentes (ci-dessous) montrent que cette domination est susceptible de se poursuivre au cours des prochaines années.

![Image](https://cdn-media-1.freecodecamp.org/images/9LIKMhsjfMRYBslKs6HRpyTalwnu2Rcrr816)

La plupart de la popularité vient de la polyvalence et de la flexibilité de FaaS pour déployer des applications. De plus, ils réduisent les coûts opérationnels et sont faciles à utiliser car la plupart de la complexité est cachée à l'utilisateur final.

Un autre point important en faveur d'AWS Lambda est son modèle de tarification à l'exécution. Par exemple, dans une seule configuration, tous nos tests décrits ci-dessous n'ont coûté qu'environ un dollar. Par conséquent, il peut être adapté à une large gamme d'applications rentables et pilotées par événements.

Cependant, lorsque vous utilisez AWS Lambda pour servir des modèles ML en production, vous devez prendre en charge toutes les étapes du pipeline total. Ces étapes incluent généralement :

* L'entraînement
* Les tests
* La gestion des versions
* Le déploiement
* La publication de la nouvelle version du modèle ML

Si ces tâches ne sont pas correctement automatisées, elles peuvent contribuer à des coûts plus élevés que prévu et à un pipeline plus lent.

Dans une série d'articles à venir, nous explorerons comment d'autres pipelines ML facilitent les étapes ci-dessus, en comparaison avec l'utilisation exclusive d'AWS Lambda.

### Entraînement de notre modèle de Machine Learning

Dans l'ensemble, nous voulions étudier les performances de diverses plateformes pour servir des modèles ML à grande échelle.

Dans cette direction, nos premières expériences se sont concentrées sur le déploiement d'un modèle de machine learning simple. Ce choix a apporté des avantages majeurs, notamment en éliminant le temps et les préoccupations liés à l'entraînement et aux performances du modèle.

Pour entraîner notre modèle, nous avons choisi le [jeu de données KDD99](http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html). Le jeu de données contient un total de 567 498 enregistrements, dont 2 211 sont considérés comme des anomalies.

Après avoir vérifié les valeurs manquantes, nous avons procédé en divisant le corpus actuel en ensembles d'entraînement et de test. Nous avons ensuite normalisé les données d'entraînement en utilisant la technique de standardisation par la moyenne.

Ensuite, nous avons entraîné un modèle de régression logistique binaire sur le problème donné. Enfin, nous avons évalué la précision du modèle en calculant la matrice de confusion :

![Image](https://cdn-media-1.freecodecamp.org/images/plIH25Fr4r4xRHYXaEpvkfktBDX1jEstbbWo)

Il est important de noter que notre focus se situe sur l'infrastructure pour servir les modèles ML. Ainsi, les meilleures pratiques pour l'entraînement des algorithmes ML ne font pas partie de notre champ d'étude.

### Configuration de l'environnement

Pour aller plus vite, nous avons utilisé certains services AWS populaires. Ils incluaient [API Gateway](https://aws.amazon.com/api-gateway/), les fonctions Lambda, [S3](https://aws.amazon.com/s3/), [Cloudwatch](https://aws.amazon.com/cloudwatch/), et [IAM](https://aws.amazon.com/iam/).

Ce qui suit décrit le rôle de chacun :

* API Gateway est la porte d'entrée pour envoyer des requêtes à notre modèle. Il gère les requêtes HTTP des clients et déclenche des événements à l'arrivée des requêtes.
* Les fonctions Lambda sont déclenchées par de telles requêtes. En résumé, le code à l'intérieur d'une fonction Lambda est responsable de l'exécution de nos fonctions d'inférence ML.
* Nous utilisons S3 pour stocker des fichiers comme les modèles et les bibliothèques.
* Cloudwatch est responsable de la collecte des logs générés par nos fonctions Lambda.
* IAM fournit l'infrastructure pour contrôler l'authentification et l'autorisation dans notre application.

### Conception des tests de charge

Nous avons conçu les tests pour répondre aux questions concernant le meilleur rapport coût-bénéfice lors de l'utilisation des services AWS Lambda. Dans ce contexte, nos tests se sont concentrés sur trois composants principaux :

* L'exploration de différentes capacités de mémoire (machine)
* La performance de différents langages de programmation
* Différentes stratégies pour charger un modèle dans une fonction Lambda

Nous avons utilisé Java et Python. Pour rendre les tests plus comparables, nous avons conçu les deux implémentations pour qu'elles soient aussi similaires que possible.

En résumé, le code Python et Java qui s'exécute à l'intérieur de la Lambda effectue les mêmes opérations. Tout d'abord, il décompresse le fichier contenant les métadonnées sur le modèle. Ensuite, il prépare les paramètres d'entrée. Et enfin, il effectue l'inférence du modèle.

Une caractéristique intéressante d'AWS Lambda est que nous pouvons le configurer pour déployer notre modèle avec différentes quantités de mémoire. En d'autres termes, nous pouvons choisir la quantité de mémoire que nous permettons à la fonction Lambda d'utiliser. De plus, lorsque nous augmentons cette mémoire, les paramètres CPU sont également mis à niveau — ce qui signifie que nous passons à une machine plus puissante.

Nous avons choisi trois configurations de mémoire différentes dans nos tests de charge. Pour Python et Java, nous avons effectué les tests en utilisant les tailles de mémoire de 256, 512 et 1024 Mo.

Nous avons exécuté chaque scénario en utilisant les paramètres suivants :

#### Scénario 1 : Requêtes progressives par minute

Dans ce scénario, nous envoyons une seule requête et attendons M minutes pour envoyer la suivante. Au début du test (minute 0), le framework de test de charge envoie une seule requête à la Lambda. Ensuite, il attend 6 minutes et envoie une nouvelle requête. Ensuite, il attend 10 minutes de plus pour émettre la requête suivante, et ainsi de suite. Au total, le test prend environ une heure et les requêtes sont effectuées aux minutes 0, 6, 16, 31 et 61.

Le but est d'évaluer combien de temps une instance de fonction Lambda sera maintenue en vie avant de s'arrêter. Comme nous le savons, chaque fois qu'AWS lance une nouvelle Lambda, il faut du temps pour la configurer et installer les dépendances (démarrage à froid). Nous voulons donc évaluer la fréquence de cette situation pour une seule instance.

En bref, un démarrage à froid peut se produire dans deux situations.

* Lorsque nous invoquons une fonction Lambda pour la première fois
* Lorsque la Lambda n'est pas utilisée pendant une période prolongée

Dans le second cas, après un délai d'inactivité, la Lambda s'arrête. Par conséquent, les requêtes suivantes nécessitent de nouveaux démarrages à froid, ce qui entraîne une latence de configuration accrue.

#### Scénario 2 : Évaluation des requêtes parallèles

Dans ce scénario, nous avons joué avec différents utilisateurs effectuant des requêtes concurrentes. Pour commencer, nous avons défini le paramètre de concurrency à C = 9. Cela signifie qu'il y aura 9 utilisateurs différents faisant des requêtes pendant une période de temps T. Cette période T est la somme d'une période R (montée en charge en minutes) et d'une période H (maintien en minutes).

La période de montée en charge signifie qu'un nouvel utilisateur commencera à faire des requêtes après une période de R/C temps. À la fin de ce temps de montée en charge, les 9 utilisateurs ont rejoint le système et commencé à faire des requêtes.

La période de maintien signifie que les 9 utilisateurs (faisant des requêtes parallèles) seront maintenus pendant H minutes. Nous avons défini R égal à 3 et H à 1 au premier stade.

Après cela, C a été défini à 18, ce qui signifie que 9 nouveaux utilisateurs vont "rejoindre le système" et commencer à faire des requêtes, R est alors défini à 0 et H à 1 minute.

Nous avions pour but de répondre à deux questions avec ce test. Nous voulions voir le temps de réponse des nouveaux utilisateurs faisant des requêtes et son impact lorsque de nouvelles instances Lambda doivent être instanciées (démarrages à froid).

### Résultats et discussion

Le premier graphique montre les résultats du premier scénario de test. Ici, étant donné une période de temps, nous effectuons des requêtes à une instance AWS Lambda à différents taux. Un seul utilisateur — une seule requête parallèle est faite tout au long du test.

![Image](https://cdn-media-1.freecodecamp.org/images/52w1VFcFwzpDIm072ACztPBaplMcn2ro8nkJ)

Comme prévu, le premier utilisateur/requête a présenté un temps de réponse beaucoup plus long. Presque 8 secondes pour le démarrage à froid. Après 5 minutes de la première requête, nous pouvons voir qu'AWS a utilisé la même instance Lambda, ce qui a provoqué un temps de réponse très court (seulement 1 seconde).

Intéressamment, même avec des intervalles plus longs entre les requêtes, AWS a réussi à utiliser la même instance. Plus précisément, les requêtes après 10 et 14 minutes après la précédente ont toujours utilisé la même Lambda. Cependant, pour un intervalle de temps de 30 minutes, AWS a dû lancer une nouvelle Lambda — ce qui a entraîné un temps de réponse plus long en raison du démarrage à froid (près de 6 secondes). En pratique, AWS a dû arrêter la Lambda quelque part dans l'intervalle de 14 à 30 minutes.

Encore une fois, notre objectif était d'évaluer combien de temps AWS maintient une instance Lambda en vie. En pratique, AWS ne le garantit pas. En fait, les algorithmes AWS peuvent décider de ce temps en fonction de nombreuses autres circonstances telles que la charge du réseau, etc. Cependant, ce test nous a aidé à mieux comprendre le fonctionnement de la logique interne d'AWS Lambda.

Pour les seconds scénarios de test, nous avons les paramètres suivants.

Pour toutes les expériences, nous affichons 4 types d'informations.

1. Le nombre total de hits (requêtes) — ligne bleue.
2. La latence maximale — ligne rouge.
3. La latence moyenne — ligne jaune.
4. Le nombre d'utilisateurs à un moment donné — ligne verte.

L'ensemble de graphiques ci-dessous montre les comparaisons de tests de performance entre les deux langages de programmation : Java et Python.

Nous augmentons le nombre total d'utilisateurs de 3 à 18 pendant un temps de test total de 5 minutes (axe des x). Le taux d'augmentation des utilisateurs est de 3, 6, 9 et 18. Notez également que chaque utilisateur effectue des requêtes parallèles au serveur. Ainsi, lorsque le nombre d'utilisateurs est de 18, il peut y avoir jusqu'à 18 requêtes parallèles émises.

Pour une meilleure compréhension, l'axe des y à gauche montre les résultats en millisecondes. Utilisez cet axe pour évaluer la latence maximale et moyenne. En revanche, l'axe des y à droite affiche des informations sur le nombre de hits et d'utilisateurs parallèles.

![Image](https://cdn-media-1.freecodecamp.org/images/82XZiYCsld-e98MorsaSo4Zf9Kij1e3iH1mu)

![Image](https://cdn-media-1.freecodecamp.org/images/DEIZkX8dHiQ2YRv5XvsGsv7J6PFgN7xrJAh3)

![Image](https://cdn-media-1.freecodecamp.org/images/VpqDOG17cIWV65vclJC2fLi2cHyTu5HImCZ1)

![Image](https://cdn-media-1.freecodecamp.org/images/UgNBmAOL6M-TawzEpjpRwLzriFbo3YBI2RrZ)

Dans l'ensemble, les tests utilisant Python se sont comportés comme prévu. Notez que le nombre de requêtes parallèles (hits) augmente à mesure que le nombre d'utilisateurs parallèles augmente. Un point très intéressant est l'effet du démarrage à froid en termes de nombre d'utilisateurs.

Tout d'abord, la ligne rouge (latence maximale) montre le premier pic au début de chaque expérience. En pratique, au début de l'expérience, AWS instancie 3 instances Lambda. Une pour chaque requête utilisateur. Comme nous l'avons discuté, chaque requête (d'un nouvel utilisateur) nécessite cette configuration. C'est le démarrage à froid.

Cependant, nous pouvons voir d'autres pics de latence pendant l'exécution du test. Ces pics semblaient être liés à l'augmentation du nombre d'utilisateurs (requêtes parallèles). Lorsque nous augmentons le nombre d'utilisateurs, AWS (à nouveau) doit configurer de nouvelles fonctions Lambda pour prendre en charge les nouvelles requêtes entrantes. Et comme prévu, les requêtes suivantes, du même utilisateur, sont exécutées par les mêmes instances Lambda. Par conséquent, cela évite un nouveau démarrage à froid pour chaque nouvelle requête.

Un autre point intéressant est l'effet de la mémoire Lambda sur la scalabilité du test. Avec 256 Mo, le test atteint un pic de 77 hits (avec 18 utilisateurs parallèles) et une moyenne de hits de 33,4. Ce chiffre a considérablement augmenté avec 512 Mo, mais n'a pas progressé davantage avec 1024 Mo. En effet, la plupart des statistiques (temps de réponse moyen, hits moyens et temps de réponse minimum) n'ont pas beaucoup changé. Peut-être que l'amélioration la plus significative (de 512 à 1024 Mo) est le temps de réponse maximum, ce qui indique des démarrages à froid plus rapides. Nos tests suggèrent que 512 Mo est la meilleure configuration coût/bénéfice pour ce modèle spécifique.

Pour Java, à l'exception de la configuration 256 Mo, les performances globales étaient très similaires à celles de Python. Pour commencer, le test 256 Mo n'a obtenu qu'une moyenne de 0,55 en nombre de hits. Moins d'une requête par seconde.

En fait, cette configuration de test n'a pas été en mesure de mettre à l'échelle le nombre de requêtes en termes d'utilisateurs. De plus, elle a souffert d'une latence très élevée tout au long des tests. Le temps de réponse moyen est resté à 17 049 millisecondes, soit ~17 secondes !

Une raison possible de cette mauvaise performance est l'empreinte mémoire de la JVM, puisque les autres configurations de mémoire se sont bien comportées.

![Image](https://cdn-media-1.freecodecamp.org/images/D7yy3jyWkge-RtC6jNIxM-axad75z7bRBj6t)

![Image](https://cdn-media-1.freecodecamp.org/images/Pbu6ySGDIHXyfVYdO90-TgFpUn-fnNQqVPUg)

![Image](https://cdn-media-1.freecodecamp.org/images/A2CjA1CMsixJKOw6EL-FC5N0QsoLlRSKhYij)

![Image](https://cdn-media-1.freecodecamp.org/images/31vJZ7bRMKQetGMquRmsse34PHqn2gNJTKsu)

Pour 512 et 1024 Mo, les résultats ont confirmé le comportement attendu. En comparaison avec les résultats correspondants de Python, nous pouvons voir des résultats très similaires.

Une divergence notable, de Java 512 à Python 512, est le comportement du temps de réponse maximum. Pour Java, le temps de réponse était beaucoup plus élevé, ce qui se traduit par des démarrages à froid plus longs.

Enfin, de manière similaire aux résultats de Python, l'augmentation de la taille de la mémoire du processus de 512 à 1024 Mo n'a pas permis d'obtenir des résultats significativement meilleurs. Bien que le nombre de hits ne se soit pas beaucoup amélioré, certains démarrages à froid ont connu une énorme amélioration. Comme le montre le tableau, le temps de réponse maximum pour Java 512 Mo était de ~18s, tandis que pour 1024 Mo, il était de ~10s.

### Conclusion

En résumé, AWS Lambda est un bon choix pour le provisionnement de modèles ML légers qui doivent être mis à l'échelle, avec seulement quelques pièges.

Parmi ses principaux **avantages** pour les cas d'utilisation que nous envisageons :

1. **Convenience** :

* AWS Lambda est facile à déployer et à mettre à l'échelle automatiquement
* AWS est un leader sur le marché du cloud. Ainsi, de nombreuses organisations déploient déjà leurs applications et stockent leurs données avec eux

2. **Coût** : selon la charge de travail, le paiement à l'exécution peut réduire les coûts d'infrastructure.

Parmi les **pièges**, le langage de choix de la fonction Lambda compte. Ainsi, il peut avoir des impacts significatifs sur les performances et les coûts.

De plus, si votre application repose sur une latence très faible, AWS Lambda pourrait ne pas être le meilleur choix. La pénalité de démarrage à froid réduit la gamme d'applications qui peuvent en bénéficier. En général, on peut tirer le meilleur parti des Lambdas si l'application possède l'une de ces caractéristiques.

* Un trafic bien défini et/ou prévisible
* La latence de démarrage à froid n'est pas un problème pour atteindre les exigences du produit

Dans certaines situations, on pourrait atténuer le temps de démarrage à froid avec des approches comme un ping pour maintenir les fonctions Lambda actives.

Une autre considération est que les modèles TF (même un modèle simple comme celui utilisé dans ce test) peuvent ne pas être l'option la plus petite disponible dans certaines situations.

Enfin, mais non des moindres, toute autre étape dans le flux de travail ML, telle que la gestion des versions et le réentraînement, doit être effectuée par nous-mêmes. Cela est attendu puisque AWS Lambda n'est qu'un environnement de calcul général.

### Prochaines étapes

Maintenant, nous allons essayer des pipelines ML plus avancés, de bout en bout, et comparer l'expérience. La question est, vont-ils nous fournir un processus rationalisé de l'entraînement à la mise en production, avec la flexibilité et la scalabilité que nous recherchons ?

Restez à l'écoute !

### Auteurs

Bruno Schionato, Diego Domingos, Fernando Moraes, Gustavo Rozato, Isac Souza, Marciano Nardi, Thalles Silva — [Daitan Group](http://www.daitangroup.com/)