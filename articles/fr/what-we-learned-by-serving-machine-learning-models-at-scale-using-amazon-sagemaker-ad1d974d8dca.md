---
title: Ce que nous avons appris en servant des modèles de Machine Learning à grande
  échelle avec Amazon SageMaker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-07T14:52:21.000Z'
originalURL: https://freecodecamp.org/news/what-we-learned-by-serving-machine-learning-models-at-scale-using-amazon-sagemaker-ad1d974d8dca
coverImage: https://cdn-media-1.freecodecamp.org/images/1*sjGuFoMotJaC512BpsL0-Q.png
tags:
- name: AI
  slug: ai
- name: AWS
  slug: aws
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Ce que nous avons appris en servant des modèles de Machine Learning à grande
  échelle avec Amazon SageMaker
seo_desc: 'By Daitan

  By Bruno Schionato, Diego Domingos, Fernando Moraes, Gustavo Rozato, Isac Souza,
  Marciano Nardi, Thalles Silva — Daitan Group

  Last time, we talked about how to deploy Machine Learning (ML) models to production
  using AWS Lambda. Following ou...'
---

Par Daitan

_Par Bruno Schionato, Diego Domingos, Fernando Moraes, Gustavo Rozato, Isac Souza, Marciano Nardi, Thalles Silva — [Daitan Group](http://www.daitangroup.com/)_

La dernière fois, nous avons parlé de la manière de [déployer des modèles de Machine Learning (ML) en production en utilisant AWS Lambda](https://medium.freecodecamp.org/what-we-learned-by-serving-machine-learning-models-using-aws-lambda-c70b303404a1). Suivant nos plans, nous avons fait un pas de plus et étudié des solutions plus complètes. Dans cet article, nous nous concentrons sur Amazon SageMaker.

SageMaker est une plateforme pour développer et déployer des modèles de ML. Elle promet de simplifier le processus de formation et de déploiement des modèles en production à grande échelle.

Pour atteindre cet objectif, elle offre des services visant à résoudre les différentes étapes du pipeline de data science, tels que :

* Collecte et stockage des données
* Nettoyage et préparation des données
* Formation et ajustement des modèles de ML
* Déploiement dans le cloud à grande échelle

Avec cela en tête, SageMaker se positionne comme un service ML entièrement géré.

Le flux de travail typique pour créer des modèles de ML implique de nombreuses étapes. Dans ce contexte, SageMaker vise à abstraire le processus de résolution de chacune de ces étapes. En fait, comme nous le verrons, en utilisant les algorithmes intégrés de SageMaker, nous pouvons déployer nos modèles avec une simple ligne de code.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Z91ECrPmlC7dzJYV.png)
_Crédits image : [Site web de SageMaker.](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-mlconcepts.html" rel="noopener" target="_blank" title=")_

Le processus de formation, d'évaluation et de déploiement est entièrement réalisé en utilisant des notebooks Jupyter. Jupyter notebook apporte de nombreux avantages. Il offre une liberté aux scientifiques des données expérimentés qui sont déjà habitués à l'outil. De plus, il offre également une flexibilité pour ceux qui n'ont pas beaucoup d'expérience dans le domaine.

En résumé, SageMaker offre de nombreux avantages pour quiconque souhaite former et déployer des modèles de ML en production. Cependant, le prix peut être un problème.

Généralement, le prix dépend de la manière et de l'endroit où vous utilisez l'infrastructure d'Amazon. Pour des raisons évidentes, les instances de machines normales ont des coûts inférieurs à ceux des instances capables de GPU. Notez que différentes régions ont des prix différents. De plus, Amazon regroupe les machines pour différentes tâches : construction, formation et déploiement. Vous pouvez trouver le tableau complet des [prix ici](https://aws.amazon.com/sagemaker/pricing/).

Pour la formation, SageMaker offre de nombreux algorithmes de ML intégrés parmi les plus populaires. Certains d'entre eux incluent K-Means, PCA, les modèles de séquence, les apprenants linéaires et XGBoost. De plus, Amazon promet des performances exceptionnelles sur ces implémentations.

De plus, si vous souhaitez former un modèle en utilisant une bibliothèque tierce comme Keras, SageMaker vous couvre également. En effet, il supporte les frameworks de ML les plus populaires. Certains d'entre eux incluent :

![Image](https://cdn-media-1.freecodecamp.org/images/0*hJqpGx46PZkUPjwV.png)

Consultez ces exemples utilisant l'API [Tensorflow Estimators](https://docs.aws.amazon.com/sagemaker/latest/dg/tf-example1.html) et [Apache MXNet](https://docs.aws.amazon.com/sagemaker/latest/dg/mxnet-example1.html).

### SageMaker — un bref aperçu

Pour comprendre comment SageMaker fonctionne, regardez le diagramme suivant. Supposons que vous souhaitez former un simple réseau de neurones convolutifs (CNN) en utilisant Tensorflow.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y_y1yYIDDp6_DLP66DsnKg.gif)
_Crédits image : [Site web de SageMaker](https://aws.amazon.com/blogs/machine-learning/bring-your-own-pre-trained-mxnet-or-tensorflow-models-into-amazon-sagemaker/" rel="noopener" target="_blank" title=")._

La première boîte « Model Files » représente les fichiers de définition des CNN. Il s'agit de l'architecture de votre modèle. Les convolutions, le pooling et les couches denses, par exemple, y sont définis. Notez que tout est développé en utilisant le framework de votre choix — Tensorflow dans ce cas.

Ensuite, nous procédons à la formation du modèle en utilisant ce framework. Pour ce faire, Amazon lance des instances de calcul ML et utilise le code de formation et le jeu de données pour effectuer le processus de formation. Ensuite, il sauvegarde les artefacts finaux du modèle et d'autres résultats dans un bucket S3 spécifié. Notez que nous pouvons tirer parti de la formation parallèle. Cela peut être fait via le parallélisme d'instances ou en ayant des machines capables de GPU.

En utilisant les artefacts du modèle et un simple protocole, il crée un modèle SageMaker. Enfin, ce modèle peut être déployé sur un endpoint avec des options concernant le nombre et le type d'instances sur lesquelles déployer le modèle.

SageMaker dispose également d'un mécanisme très intéressant pour ajuster les modèles de ML — l'ajustement automatique des modèles. Habituellement, l'ajustement des modèles de ML est une tâche très chronophage et coûteuse en calcul. La raison est que les techniques disponibles reposent sur des méthodes de force brute comme la recherche par grille ou la recherche aléatoire.

Pour donner un exemple, en utilisant l'ajustement automatique des modèles, nous pouvons sélectionner un sous-ensemble d'optimiseurs possibles, disons Adam et/ou SGD, et quelques valeurs pour le taux d'apprentissage. Ensuite, le moteur s'occupera des combinaisons possibles et se concentrera sur l'ensemble de paramètres qui donne les meilleurs résultats.

De plus, ce processus est scalable. Nous pouvons choisir le nombre de tâches à exécuter en parallèle ainsi que le nombre maximum de tâches à exécuter. Après cela, l'ajustement automatique fera le travail. Cette fonctionnalité fonctionne avec les bibliothèques tierces et les algorithmes intégrés. Notez qu'Amazon fournit l'ajustement automatique des modèles sans frais supplémentaires.

Et si nous utilisions les capacités de déploiement de SageMaker pour servir un modèle pré-entraîné ? C'est exact, vous pouvez soit entraîner un nouveau modèle en utilisant le cloud Amazon, soit l'utiliser pour servir un modèle préexistant. En d'autres termes, vous pouvez tirer parti de la partie de service de SageMaker pour déployer des modèles qui ont été entraînés en dehors de celui-ci.

### Formation et déploiement sur SageMaker

Comme nous le savons, SageMaker offre une variété d'estimateurs ML populaires. Il permet également de prendre un modèle pré-entraîné et de le déployer. Cependant, sur la base de nos expériences, il est beaucoup plus facile d'utiliser ses implémentations intégrées. La raison est que pour déployer des modèles tiers en utilisant les API de SageMaker, il faut gérer les conteneurs.

Ainsi, nous posons ici le défi de gérer le pipeline ML complet en utilisant SageMaker. Nous l'utiliserons des tâches ML les plus basiques aux plus avancées. Certaines des tâches impliquent :

* Téléchargement du jeu de données sur un bucket S3
* Prétraitement du jeu de données pour la formation
* Formation et déploiement du modèle

Tout est fait dans le cloud.

Comme dans l'article précédent, nous allons ajuster un modèle linéaire en utilisant le jeu de données d'intrusion KDD99. Vous pouvez trouver plus de détails sur le jeu de données et les étapes de prétraitement dans [cet article](https://medium.freecodecamp.org/what-we-learned-by-serving-machine-learning-models-using-aws-lambda-c70b303404a1).

Tout le processus de formation et de déploiement du modèle est réalisé en utilisant l'interface Jupyter notebook de SageMaker. Elle ne nécessite aucune configuration et le notebook s'exécute sur une instance EC2 de votre choix. Ici, nous avons choisi une instance EC2 _ml.m4.xlarge_ pour héberger le notebook. Nous avons eu des problèmes pour charger le jeu de données KDD99 en utilisant une instance moins puissante (en raison du manque d'espace).

Jetez un coup d'œil aux configurations des machines EC2 :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lpqeEVtlI3F-oHcbrmdNrw.png)

Pour ajuster les modèles linéaires, SageMaker dispose de l'algorithme [**Linear Learner**](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html). Il fournit une solution pour la classification et la régression. Avec très peu de lignes, nous pouvons définir et ajuster le modèle sur le jeu de données.

Jetez un coup d'œil à la classe Estimator. Il s'agit d'une classe de base qui encapsule tous les différents algorithmes intégrés de SageMaker. Parmi d'autres paramètres, certains des plus importants incluent :

* image_name : L'image du conteneur à utiliser pour la formation.
* train_instance_count : Nombre d'instances EC2 utilisées pour la formation.
* train_instance_type : Le type d'instance EC2 à utiliser pour la formation.
* output_path : Emplacement S3 pour sauvegarder le résultat de la formation.

Pour définir le type de modèle que nous voulons utiliser, nous définissons le paramètre 'image_name' sur 'linear-learner'. Pour exécuter la procédure de formation, nous avons choisi une instance EC2 _ml.c4.xlarge_. Elle dispose de 4 CPU virtuels et de 7,5 Go de RAM.

Les hyperparamètres du modèle incluent :

* feature_dim : les dimensions d'entrée
* predictor_type : si classification ou régression
* mini_batch_size : combien d'échantillons utiliser par étape.

Enfin, SageMaker fournit une API très similaire à celle de scikit-learn pour la formation. Il suffit d'appeler la fonction fit(), et vous êtes opérationnel.

Voici la partie finale — le déploiement. Pour ce faire, comme pour la formation, nous exécutons simplement une ligne de code.

Cette routine s'occupera de déployer le modèle formé sur un endpoint Amazon. Notez que nous devons spécifier le type d'instance que nous voulons, dans ce cas, une instance EC2 _ml.m4.xlarge_. De plus, nous pouvons définir un nombre minimum d'instances EC2 pour déployer notre modèle. Pour ce faire, nous définissons simplement le paramètre _initial_instance_count_ à une valeur supérieure à 1.

### Auto Scaling

Nous avons deux objectifs principaux avec les tests.

* Évaluer le pipeline ML complet offert par SageMaker
* Évaluer la scalabilité de la formation et du déploiement.

Dans tous les tests, nous avons utilisé l'outil Auto Scaling de SageMaker. Comme nous le verrons, il aide à contrôler le compromis trafic/instances.

Comme indiqué sur le site web d'AWS :

> AWS Auto Scaling surveille vos applications et ajuste automatiquement la capacité pour maintenir des performances stables et prévisibles au coût le plus bas possible.

En bref, SageMaker Auto Scaling facilite la création de plans de scalabilité pour diverses ressources à travers de nombreux services. Ces services incluent Amazon EC2, Spot Fleets, les tâches Amazon ECS, et plus encore. L'idée est d'ajuster le nombre d'instances en cours d'exécution en réponse aux changements de la charge de travail.

Il est important de noter que l'Auto Scaling peut échouer dans certaines situations. Plus précisément, lorsque votre application subit des pics de trafic, l'Auto Scaling peut ne pas aider du tout. Nous savons que pour les nouvelles instances (EC2), Amazon a besoin de temps pour configurer la machine avant qu'elle ne soit capable de traiter les requêtes. Sur la base de nos expériences, ce temps de configuration peut prendre de 5 à 7 minutes. Si votre application a des pics de courte durée (disons 2 à 4 minutes) dans le nombre de requêtes entrantes, au moment où le temps de configuration de l'instance EC2 se termine, le besoin de plus de puissance de calcul peut être passé.

Pour remédier à cette situation, Amazon met en œuvre une politique simple pour scaler les nouvelles instances. Basiquement, après une décision de scalabilité, une période de refroidissement doit être respectée avant qu'une autre activité de scalabilité ne se produise. En d'autres termes, chaque action pour émettre une nouvelle instance est entrecoupée d'une quantité de temps fixe (configurable). Ce mécanisme vise à faciliter la surcharge de lancement d'une nouvelle machine.

De plus, si votre application a un trafic utilisateur bien défini/prévisible, l'Auto Scaling peut également être un mauvais choix. Supposons que vous hébergez le site web d'une application. Vous savez qu'à un moment spécifique, les applications seront ouvertes à des centaines de millions d'utilisateurs. Dans cette situation, le temps requis pour que l'Auto Scaling soit correctement configuré peut se terminer par une mauvaise expérience utilisateur.

### Résultats

Nous avons utilisé Tauros et JMeter pour exécuter des tests de charge sur notre modèle de ML développé avec Amazon SageMaker.

Le premier scénario est défini comme suit :

* Nombre d'utilisateurs simultanés : 1000
* Temps de montée en charge de 10 minutes
* Période de maintien de 10 minutes

En termes simples, le test consiste à émettre des requêtes à partir de 1000 utilisateurs parallèles. Dans la première partie du test (les 10 premières minutes), le nombre d'utilisateurs est augmenté de 0 à 1000 (montée en charge). Ensuite, les 1000 utilisateurs continuent à envoyer des requêtes parallèles pendant 10 minutes supplémentaires (période de maintien). Notez que chaque utilisateur envoie des requêtes de manière sérielle. C'est-à-dire, pour émettre une nouvelle requête, un utilisateur doit attendre que la requête actuelle se termine.

Pour les premiers tests, nous avons décidé d'utiliser une seule machine. Par conséquent, nous n'avons pas défini de plan de scalabilité qui créerait de nouvelles instances en atteignant un certain critère.

Dans le graphique ci-dessous, la ligne bleue (augmentant en forme d'escalier) est le nombre d'utilisateurs parallèles. La ligne orange représente le temps de réponse moyen, et la ligne verte le nombre de requêtes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1oDZB4z3g6d4Oq2BGH96LA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Az1SXcQWdK3I2d6xK7RLXA.png)

Au début, le nombre d'utilisateurs passe de 0 à 1000. Comme prévu, le nombre de requêtes émises vers le modèle augmente de manière similaire.

Dans la dernière partie de l'expérience (les 10 dernières minutes), le nombre de requêtes et le temps de réponse moyen restent stables. Cela suggère que cette seule machine semble capable de gérer la charge actuelle.

De plus, cette seule machine a été capable de traiter une moyenne globale de 961,3 requêtes par seconde. En fait, après avoir atteint le nombre maximum d'utilisateurs simultanés (1000), cette moyenne était de près de 1200 requêtes par seconde.

Pour approfondir notre hypothèse, nous avons décidé d'ajouter un plan de scalabilité à nos tests de charge. Ici, lorsque le nombre de requêtes parallèles/minute atteint la marque de 30k, nous instruisons le système de scaler le nombre d'instances en cours d'exécution. Pour tous les tests, le nombre maximum d'instances a été fixé à 10. Cependant, dans tous les cas, l'Auto Scaling de SageMaker n'a pas utilisé toutes les ressources disponibles.

Pour le test ci-dessous, Amazon Auto Scaling n'a émis qu'une instance supplémentaire pour aider à traiter la charge actuelle. Cela est représenté par la ligne rouge dans la figure d'utilisation du CPU ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*J2kdym-_2fMWo8Xm2nPb4Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*r6R5tNAOMVEfYtS6qBrPpQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GWQihM2kdb7rk4YjREXfKg.png)

Néanmoins, l'ajout de cette nouvelle instance a permis d'augmenter le débit et de réduire la latence. Cela est notable après la marque de temps 15:48.

Pour mieux évaluer l'outil Auto Scaling, nous avons décidé de réduire le nombre seuil de requêtes/minute avant le scalage. Maintenant, l'Auto Scaling est conseillé de lancer une nouvelle instance dès que le débit atteint 15k requêtes/minute. Par conséquent, Auto Scale a utilisé un total de 4 instances pour correspondre au plan de scalabilité. Il est également assez intuitif de voir que lorsque le nombre d'instances augmente, le pourcentage d'utilisation du CPU diminue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-_HU_oJ0iZcoI701o3LooA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*v-LTgSXxkMCQpbZaC_zj5A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YEvZRd4GAhu26t3gGPUn5A.png)

Nous avons remarqué qu'au début de tous les tests, nous avions un pic important de latence. Nos expériences suggèrent que cette valeur moyenne élevée est causée par le test lui-même (Taurus/JMeter) qui se réchauffe et prépare les ressources. Notez qu'après le pic, le temps de réponse diminue rapidement pour atteindre des valeurs normales. Plus tard, il augmente avec le nombre d'utilisateurs virtuels (comme prévu). De plus, ce pic initial n'est pas observé dans les statistiques de latence pour l'API Gateway ou SageMaker — ce qui soutient nos premières réflexions.

De plus, spécifiquement pour ce test et ce choix de modèle, Auto Scale n'a pas été très efficace. La raison est que la quantité de charge que nous effectuons sur le serveur est entièrement gérée par une seule machine.

#### Conclusion

Voici quelques-unes de nos observations sur SageMaker :

* Il offre une interface très propre et facile à utiliser. Les notebooks Jupyter offrent de nombreux avantages et les algorithmes intégrés sont faciles à utiliser (API basée sur scikit-learn). De plus, les machines utilisées pour la formation ne sont facturées que lorsque la formation a lieu. Pas de paiement pour le temps d'inactivité :)
* Il élimine de nombreuses tâches fastidieuses du ML. L'auto-scaling et l'auto-ajustement des hyperparamètres sont d'excellentes fonctionnalités.
* Si vous utilisez les algorithmes intégrés, le déploiement est très simple. Juste une ligne de code.
* Bien que SageMaker supporte les bibliothèques ML tierces, nous avons constaté que servir un modèle pré-entraîné n'est pas aussi simple que d'utiliser leur API native.