---
title: Comment créer un modèle de ML avec Azure Machine Learning Designer
subtitle: ''
author: Eniola Ajala
co_authors: []
series: null
date: '2024-06-25T14:45:20.000Z'
originalURL: https://freecodecamp.org/news/create-an-ml-model-with-azure-machine-learning-designer
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/F8825B00-8A4C-41D9-AE75-02A8631DE983.jpeg
tags:
- name: Azure
  slug: azure
- name: Low Code
  slug: low-code
- name: Machine Learning
  slug: machine-learning
seo_title: Comment créer un modèle de ML avec Azure Machine Learning Designer
seo_desc: 'Did you know that you can create machine learning models without writing
  any code? If you’re here, you’re probably curious about how to achieve this.

  In this article, I will guide you through building a regression model that predicts
  automobile price...'
---

Saviez-vous que vous pouvez créer des modèles de machine learning sans écrire une seule ligne de code ? Si vous êtes ici, vous êtes probablement curieux de savoir comment y parvenir.

Dans cet article, je vais vous guider à travers la création d'un modèle de régression qui prédit les prix des automobiles en utilisant les outils Low-Code/No-Code d'Azure Machine Learning.

La `régression` est une technique de machine learning supervisée utilisée pour prédire des valeurs numériques. Pour mieux comprendre la régression, vous pouvez lire mon article précédent [ici](https://medium.com/@ajalaeniola454/supervised-and-unsupervised-learning-in-machine-learning-06c7151a0c2a).

### Prérequis

Pour comprendre et suivre les étapes de ce tutoriel, vous avez besoin des éléments suivants :

1. Un compte Azure : Vous devez avoir un compte Azure actif.

2. Un abonnement Azure : Un abonnement Azure actif est requis.

Si vous n'avez pas encore de compte Azure, vous pouvez vous inscrire pour [Azure pour les étudiants](https://azure.microsoft.com/en-us/free/students?wt.mc_id=studentamb_230833), le [GitHub Student Developer Pack](https://github.com/edu/students?wt.mc_id=studentamb_230833), ou un [essai gratuit Azure](https://azure.microsoft.com/en-us/free?wt.mc_id=studentamb_230833). Ces options offrent divers avantages et des crédits gratuits pour commencer.

Maintenant, commençons à construire notre modèle. Suivez les étapes ci-dessous pour commencer ! Assurez-vous de lire jusqu'à la fin pour apprendre tout le processus.

## Table des matières

* [Comment configurer votre espace de travail Azure Machine Learning](#heading-comment-configurer-votre-espace-de-travail-azure-machine-learning)

* [Comment configurer les ressources de calcul dans Azure Machine Learning Studio](#heading-comment-configurer-les-ressources-de-calcul-dans-azure-machine-learning-studio)

* [Comment créer votre pipeline de Machine Learning](#heading-comment-creer-votre-pipeline-de-machine-learning)

* [Comment construire le modèle](#heading-comment-construire-le-modele)

* [Comment évaluer le modèle](#heading-comment-evaluer-le-modele)

* [Comment déployer le modèle](#heading-comment-deployer-le-modele)

* [Nettoyage](#heading-nettoyage)

* [Conclusion](#heading-conclusion)

## Comment configurer votre espace de travail Azure Machine Learning

Pour commencer à travailler avec `Azure Machine Learning`, vous devez d'abord créer un `workspace`. Un `workspace` est un endroit centralisé pour gérer toutes les ressources et expériences de vos projets de machine learning.

### Étape 1 : Créer un groupe de ressources

Commencez par vous connecter au [Portail Azure](https://azure.microsoft.com/en-us/get-started/azure-portal?wt.mc_id=studentamb_230833). Cliquez sur le bouton `Créer une ressource` (l'icône plus) dans la barre de navigation de gauche.

Dans la barre de recherche, tapez « Machine Learning » et sélectionnez `Azure Machine Learning` dans la liste.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1-1.png align="left")

*Navigation vers la page d'accueil Azure et clic sur l'icône plus pour créer une nouvelle ressource pour le projet de machine learning*

### Étape 2 : Créer une nouvelle ressource Azure Machine Learning

Maintenant, cliquez sur `Créer` pour commencer à configurer votre espace de travail. Vous devrez remplir les détails nécessaires :

* **Abonnement** : Sélectionnez votre abonnement Azure.

* **Groupe de ressources** : Sélectionnez un groupe de ressources existant ou créez-en un nouveau en cliquant sur `Créer` et en fournissant un nom.

* **Nom de l'espace de travail** : Fournissez un nom unique pour votre espace de travail.

* **Région** : Choisissez une région proche de votre emplacement pour réduire la latence.

* **Registre de conteneurs** : Choisissez `Créer` sauf si vous avez un registre de conteneurs existant que vous souhaitez utiliser.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/3-1.png align="left")

*Parcourir le marketplace Azure pour les services de machine learning afin de trouver l'outil approprié pour construire et déployer des modèles.*

### Étape 3 : Vérifier et créer

Remplissez le formulaire avec toutes les informations requises. Assurez-vous de fournir un `Nom` unique et de sélectionner une région. Ensuite, créez votre nouveau registre de conteneurs.

Passez en revue vos paramètres pour vous assurer que tout est correct. Ensuite, cliquez sur `Vérifier + créer` pour valider votre configuration. Une fois la validation terminée, cliquez sur `Créer` pour déployer votre espace de travail. Ce processus peut prendre quelques minutes.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/5-1.png align="left")

*Configuration d'un nouvel espace de travail de machine learning dans Azure avec les détails de configuration essentiels.*

### Étape 4 : Déploiement

Une fois le déploiement terminé, cliquez sur le bouton `Aller à la ressource` pour naviguer vers votre nouvel espace de travail.

Dans l'aperçu de l'espace de travail, cliquez sur `Lancer le studio` pour ouvrir le `Azure Machine Learning Studio`, où vous effectuerez toutes vos tâches de machine learning.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/7.png align="left")

*Déploiement de la ressource terminé dans les services Microsoft Azure Machine Learning.*

## Comment configurer les ressources de calcul dans Azure Machine Learning Studio

Une fois le déploiement de votre espace de travail terminé, vous devez configurer les ressources de calcul nécessaires pour exécuter vos expériences de machine learning. Suivez les étapes ci-dessous pour ce faire.

### Étape 1 : Accéder à l'espace de travail

Une fois le déploiement terminé, cliquez sur le bouton `Aller à la ressource`. Dans l'aperçu de l'espace de travail, cliquez sur `Lancer le studio` pour ouvrir Azure Machine Learning Studio.

### Étape 2 : Créer une instance de calcul

Dans Azure Machine Learning Studio, naviguez vers le menu de gauche et cliquez sur Calcul. Sélectionnez l'onglet `Instances de calcul`, puis cliquez sur `+ Nouveau` pour créer une nouvelle instance de calcul.

Remplissez les détails requis :

* **Taille de la machine virtuelle** : Sélectionnez `Standard_DS11_v2` pour un équilibre entre performance et coût minimal.

* **Nom du calcul** : Entrez un nom unique pour votre instance de calcul.

Ensuite, cliquez sur `Créer` pour configurer l'instance de calcul. Ce processus peut prendre quelques minutes.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/conp-running.png align="left")

*Configuration des instances de calcul dans Azure Machine Learning pour garantir la puissance de calcul requise pour l'entraînement des modèles de machine learning.*

### Étape 3 : Créer un cluster de calcul

En plus d'une instance de calcul, vous aurez besoin d'un cluster de calcul pour un entraînement scalable. Toujours dans la section `Calcul`, sélectionnez l'onglet `Clusters de calcul` et cliquez sur `+ Nouveau`.

Remplissez les détails :

* **Nom du cluster** : Entrez un nom unique pour votre cluster de calcul.

* **Taille de la machine virtuelle** : Choisissez `Standard_DS11_v2`.

* **Nombre minimal de nœuds** : Définissez à `0` pour économiser des coûts lorsqu'il n'est pas utilisé.

* **Nombre maximal de nœuds** : Définissez à `2` pour ce tutoriel.

Ensuite, cliquez sur `Créer` pour configurer le cluster de calcul. Attendez que le cluster soit en état de fonctionnement avant de continuer.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/11.png align="left")

*Aperçu des clusters de calcul dans Azure Machine Learning*

## Comment créer votre pipeline de Machine Learning

Dans cette section, nous allons créer un `pipeline de machine learning` en utilisant `Azure Machine Learning Designer`. Les pipelines aident à rationaliser le processus de préparation des données, d'entraînement des modèles et de leur déploiement.

### Étape 1 : Naviguer vers le Designer

Dans Azure Machine Learning Studio, allez dans la barre de navigation de gauche et cliquez sur `Designer`. Ensuite, cliquez sur `+ Nouveau pipeline` pour commencer à créer un nouveau pipeline.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/p1.png align="left")

*Interface montrant la création d'un nouveau pipeline.*

### Étape 2 : Ajouter vos données

Vous avez la possibilité d'utiliser des données externes ou des jeux de données d'exemple préconstruits. Pour ce tutoriel, nous utiliserons un jeu de données d'exemple préconstruit.

Pour utiliser des données d'exemple préconstruites, cliquez sur l'onglet `Composants`. Utilisez la barre de recherche ou faites défiler manuellement pour trouver le jeu de données `Automobile price data`. Glissez-déposez le jeu de données sur le canevas dans le Designer.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/p2.png align="left")

*Interface montrant l'ajout du jeu de données Automobile price data.*

### Étape 3 : Explorer les données

Une fois le jeu de données sur le canevas, cliquez dessus pour voir ses détails. Naviguez vers l'onglet `Visualisations` pour explorer la distribution des données et les résumés statistiques. Cliquez sur l'onglet `Output+logs` puis sur `Preview data` pour inspecter les premières lignes du jeu de données. Cela vous aidera à comprendre la structure des données et à identifier d'éventuels problèmes.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/p3.png align="left")

*Visualisation du jeu de données*

### Étape 4 : Préparer les données

Pour spécifier les variables avec lesquelles nous voulons travailler, nous devons filtrer les colonnes inutiles.

Dans la section `Transformation des données`, glissez-déposez le module `Sélectionner les colonnes dans le jeu de données` sur le canevas sous le jeu de données. Connectez le nœud de sortie du jeu de données au nœud d'entrée du module `Sélectionner les colonnes dans le jeu de données`.

Ouvrez les paramètres du module, sélectionnez les colonnes que vous souhaitez inclure dans votre modèle, et excluez les colonnes non pertinentes telles que `normalized-losses`. (*Nous supprimons cette colonne car elle contient un pourcentage élevé de données manquantes*). Cliquez sur `Enregistrer et fermer` pour appliquer les modifications.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n1-1.png align="left")

*Interface pour sélectionner les colonnes dans le jeu de données.*

Ensuite, vous devrez nettoyer les données manquantes. Cela nous aide à gérer les valeurs manquantes pour améliorer la précision du modèle.

Pour ce faire, glissez-déposez le module `Nettoyer les données manquantes` sur le canevas, sous le module `Sélectionner les colonnes dans le jeu de données`. Connectez les nœuds et configurez les paramètres pour supprimer les lignes avec des valeurs manquantes. Enregistrez et fermez les paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n2.png align="left")

*Interface pour nettoyer les colonnes dans le jeu de données.*

### Étape 5 : Normaliser les données

Pour garantir que le modèle fonctionne bien, nous devons normaliser les données. Pour ce faire, dans la section `Transformation des données`, glissez-déposez le module `Normaliser les données` sur le canevas. Connectez la sortie du module `Nettoyer les données manquantes` à l'entrée du module `Normaliser les données`.

Vous devrez configurer le module pour utiliser la méthode de mise à l'échelle `MinMax` et sélectionner les colonnes à normaliser. Vous pouvez les saisir manuellement en séparant chaque colonne par une virgule. Ensuite, enregistrez et fermez les paramètres.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n3.png align="left")

*Interface pour normaliser les colonnes dans le jeu de données.*

### Étape 6 : Finaliser la configuration du pipeline

Une fois toutes les transformations en place, passez en revue le pipeline pour vous assurer que toutes les étapes sont correctement configurées. Cliquez sur `Soumettre` pour exécuter le pipeline. Vous pouvez surveiller la progression du pipeline dans la section `Jobs`.

REMARQUE : Chaque fois que vous configurez un module et que vous cliquez sur soumettre, `afficher les détails` du `travail de pipeline` pour suivre vos flux.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n4.png align="left")

*Surveillance du pipeline via le lien*

## Comment construire le modèle

C'est l'étape amusante où nous commençons à construire notre modèle de machine learning en préparant le jeu de données pour l'entraînement et en appliquant les algorithmes appropriés.

### Étape 1 : Diviser le jeu de données

Glissez-déposez le module Diviser les données sur le canevas. Ensuite, connectez la sortie du module Normaliser les données à l'entrée du module `Diviser les données`.

Dans le panneau des paramètres du module Diviser les données :

* Définissez la `Fraction de lignes` dans le premier jeu de données de sortie à 0,7. Cela signifie que 70 % des données seront utilisées pour entraîner le modèle.

* Définissez la `Graine aléatoire` à n'importe quel nombre pour garantir la reproductibilité. Pour ce tutoriel, utilisez 123.

### Étape 2 : Entraîner le modèle

Il est maintenant temps d'ajouter le bloc `Entraîner le modèle`. Glissez-déposez le module `Entraîner le modèle` sur le canevas. Connectez la première sortie du module `Diviser les données` (les 70 % de données d'entraînement) à l'entrée du module `Entraîner le modèle`.

Cliquez sur le module `Entraîner le modèle` pour configurer ses paramètres. Dans la section `Modifier la colonne`, sélectionnez la variable cible, qui dans ce cas est `price`. Enregistrez et fermez les paramètres.

Ensuite, vous ajouterez l'algorithme d'entraînement. Dans la section `Algorithmes de Machine Learning`, glissez-déposez le module `Régression linéaire` sur le canevas. Connectez la sortie du module `Régression linéaire` à l'entrée droite du module `Entraîner le modèle`.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n7.png align="left")

*Interface montrant la connexion des modules dans le pipeline*

### Étape 3 : Évaluer le modèle

Glissez-déposez le module `Noter le modèle` sur le canevas. Connectez la deuxième sortie du module `Diviser les données` (les 30 % de données de test) à l'entrée gauche du module `Noter le modèle`. Connectez la sortie du module `Entraîner le modèle` à l'entrée droite du module `Noter le modèle`. Cela appliquera le modèle entraîné aux données de test pour évaluer ses performances.

Ensuite, glissez-déposez le module `Évaluer le modèle` sur le canevas. Connectez la sortie du module `Noter le modèle` à l'entrée du module `Évaluer le modèle`. Cela fournira diverses métriques d'évaluation pour évaluer la précision du modèle.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/model-1.png align="left")

*Interface montrant la connexion des modules dans le pipeline*

### Étape 4 : Vérifier et soumettre

Vérifiez toutes les connexions et paramètres dans votre pipeline. Ensuite, cliquez sur `Soumettre` pour exécuter le pipeline d'entraînement et d'évaluation du modèle. Vous pouvez surveiller la progression du travail dans la section `Jobs`, où vous pouvez voir les journaux et les sorties.

## Comment évaluer le modèle

Après avoir entraîné notre modèle, il est important d'évaluer ses performances pour s'assurer qu'il fait des prédictions précises. Nous utiliserons les modules `Noter le modèle` et `Évaluer le modèle` à cette fin.

### Étape 1 : Évaluer les performances du modèle

Glissez-déposez le module `Évaluer le modèle` sur le canevas. Connectez la sortie du module `Noter le modèle` à l'entrée du module `Évaluer le modèle`.

Le module `Évaluer le modèle` générera diverses métriques d'évaluation, telles que l'erreur absolue moyenne (MAE), l'erreur quadratique moyenne (RMSE) et le R-carré (R²), qui sont essentielles pour évaluer la précision et les performances du modèle de régression.

### Explorer les métriques d'évaluation

Une fois l'exécution du pipeline terminée, cliquez sur le module `Évaluer le modèle` pour explorer les métriques détaillées.

Voici quelques métriques clés sur lesquelles se concentrer :

* **Erreur absolue moyenne (MAE)** : Mesure l'ampleur moyenne des erreurs dans les prédictions, sans tenir compte de leur direction. Des valeurs plus faibles indiquent une meilleure précision.

* **Erreur quadratique moyenne (RMSE)** : Similaire à la MAE mais donne plus de poids aux erreurs plus grandes. Des valeurs plus faibles sont meilleures.

* **R-carré (R²)** : Indique à quel point les prédictions du modèle correspondent aux données réelles. Des valeurs plus proches de 1 signifient un meilleur ajustement.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n9.png align="left")

*Visualisation des données de sortie du modèle de régression.*

Nous venons de construire et d'évaluer notre modèle. Hourra !

## Comment déployer le modèle

Maintenant que nous avons entraîné et évalué notre modèle de régression, il est temps de le déployer pour une inférence en temps réel en utilisant Azure Machine Learning. Suivez ces étapes pour déployer le modèle et créer un pipeline d'inférence.

### Étape 1 : Créer le pipeline d'inférence

Naviguez vers la section `Designer` dans Azure Machine Learning Studio et créez un nouveau pipeline pour le déploiement. Sélectionnez `Inférence en temps réel` pour configurer automatiquement le pipeline de déploiement.

### Étape 2 : Configurer le pipeline

Après avoir sélectionné l'inférence en temps réel, le pipeline sera initialisé avec des composants par défaut. Vous pouvez modifier le pipeline en ajoutant les composants nécessaires.

Nous devons apporter quelques modifications comme ajouter les modules `Saisir les données manuellement`, `Exécuter le script Python`. De plus, dans le bloc `sélectionner les colonnes dans le jeu de données`, modifiez et supprimez la colonne de prix. Supprimez la connexion entre `Noter le modèle` et `service web`.

* `Saisir les données manuellement` : Glissez-déposez ce bloc sur le canevas. Ce composant permet la saisie manuelle des données pour la prédiction. Copiez et collez les données ci-dessous dans le champ `data`.

symboling,fuel-type,aspiration,num-of-doors,body-style,drive-wheels,engine-location,wheel-base,length,width,height,curb-weight,engine-type,num-of-cylinders,engine-size,fuel-system,bore,stroke,compression-ratio,horsepower,peak-rpm,city-mpg,highway-mpg,make 3,gas,std,two,convertible,rwd,front,88.6,168.8,64.1,48.8,2548,dohc,four,130,mpfi,3.47,2.68,9,111,5000,21,27,alfa-romero giulia 3,gas,std,two,convertible,rwd,front,88.6,168.8,64.1,48.8,2548,dohc,four,130,mpfi,3.47,2.68,9,111,5000,21,27,alfa-romero stelvio 1,gas,std,two,hatchback,rwd,front,94.5,171.2,65.5,52.4,2823,ohcv,six,152,mpfi,2.68,3.47,9,154,5000,19,26,alfa-romero Quadrifoglio 2,gas,std,four,sedan,fwd,front,99.8,176.6,66.2,54.3,2337,ohc,four,109,mpfi,3.19,3.4,10,102,5500,24,30,audi 100 ls 2,gas,std,four,sedan,4wd,front,99.4,176.6,66.4,54.3,2824,ohc,five,136,mpfi,3.19,3.4,8,115,5500,18,22,audi 100ls 2,gas,std,two,sedan,fwd,front,99.8,177.3,66.3,53.1,2507,ohc,five,136,mpfi,3.19,3.4,8.5,110,5500,19,25,audi fox 1,gas,std,four,sedan,fwd,front,105.8,192.7,71.4,55.7,2844,ohc,five,136,mpfi,3.19,3.4,8.5,110,5500,19,25,audi 100ls 1,gas,std,four,wagon,fwd,front,105.8,192.7,71.4,55.7,2954,ohc,five,136,mpfi,3.19,3.4,8.5,110,5500,19,25,audi 5000 1,gas,turbo,four,sedan,fwd,front,105.8,192.7,71.4,55.9,3086,ohc,five,131,mpfi,3.13,3.4,8.3,140,5500,17,20,audi 4000

* `Exécuter le script Python` : Remplacez le code dans ce bloc par :

import pandas as pd def azureml\_main(dataframe1=None, dataframe2=None): scored\_results = dataframe1\[\["Scored Labels"\]\] scored\_results.rename(columns={"Scored Labels": "predicted price"}, inplace=True)  
return scored\_results

* `Sélectionner les colonnes dans le jeu de données` : Modifiez et supprimez la colonne `price` pour vous assurer qu'elle n'est pas incluse dans les données d'entrée pour les prédictions.

* `Supprimer la connexion` : Déconnectez le module `Noter le modèle` de la sortie du service web pour vous assurer que seul le bloc `Exécuter le script Python` s'y connecte.

Voir les images ci-dessous pour une représentation visuelle de la manière dont les connexions sont configurées.

![Image](https://www.freecodecamp.org/news/content/images/2024/08/3E905EDF-3F19-4451-8F31-6F80F7212957.png align="left")

*Interface de connexion des modules dans le pipeline*

### Étape 3 : Soumettre et déployer le modèle

Soumettez le flux et attendez que tous les processus se terminent avec succès (coche verte). Une fois votre déploiement réussi, vous pouvez explorer la sortie pour vérifier que tout fonctionne comme prévu.

Vous pouvez maintenant déployer le modèle en tant que service web en temps réel pour les prédictions.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n13.png align="left")

*Paramètres de configuration pour la mise en place d'un nouveau pipeline*

Une fois que tous les processus sont terminés avec succès dans Azure Machine Learning Studio, vous êtes prêt à explorer la sortie et à déployer votre modèle entraîné en tant que service web en temps réel.

Voici comment vous pouvez procéder :

1. **Vérifier l'exécution du pipeline** : Assurez-vous que toutes les étapes de votre pipeline se sont terminées avec une coche verte indiquant le succès.

2. **Voir les sorties et les visualisations** : Naviguez à travers les différents composants de votre pipeline pour inspecter les sorties et les visualisations générées lors des étapes de transformation des données, d'entraînement du modèle et d'évaluation. Cela aide à comprendre comment chaque étape a contribué à la performance globale du modèle.

3. **Vérifier les métriques d'évaluation** : Examinez les scores d'évaluation générés par le bloc `Noter le modèle` pour évaluer les performances de votre modèle de régression entraîné. Les métriques d'évaluation courantes incluent l'erreur quadratique moyenne (MSE), le R-carré (R2) et l'erreur quadratique moyenne (RMSE). Ces métriques fournissent des informations sur la manière dont votre modèle prédit les prix des automobiles en fonction des caractéristiques d'entrée.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n10-1.png align="left")

*Visualisation des données de sortie de l'évaluation du modèle.*

Mettez en place les vérifications suivantes avant de commencer le déploiement :

#### Préparer le déploiement

Tout d'abord, assurez-vous que le bloc `Exécuter le script Python` est correctement configuré pour transformer les données d'entrée et produire les prix prédits.

Vous devrez également vérifier que le pipeline est configuré pour gérer l'inférence en temps réel pour le déploiement du modèle.

#### Soumettre le pipeline

Cliquez sur le bouton soumettre pour initier le processus de déploiement. Attendez qu'Azure Machine Learning termine le déploiement et vérifiez que tous les composants ont été déployés avec succès.

#### Déployer en tant que service web

Une fois le déploiement confirmé comme réussi, vous pouvez déployer le modèle en tant que service web en temps réel. Ce service web sera hébergé sur Azure et pourra être accessible via des points de terminaison API, permettant aux applications d'envoyer des données et de recevoir des prédictions en temps réel.

#### Tester le service web

Utilisez le bloc `Saisir les données manuellement` pour saisir manuellement des données de test ou utilisez des systèmes externes pour envoyer des requêtes au point de terminaison du service web déployé. Vous pouvez vérifier que le service web répond avec des prix prédits en fonction des caractéristiques d'entrée.

#### Surveiller et gérer

Surveillez les performances de votre service web déployé à l'aide des outils de surveillance d'Azure Machine Learning. Vous pouvez gérer le déploiement en mettant à l'échelle les ressources si nécessaire ou en mettant à jour le modèle avec de nouvelles données ou des versions améliorées.

Le déploiement de votre modèle de régression en tant que service web en temps réel vous permet d'utiliser ses capacités prédictives dans diverses applications sans avoir besoin d'une intervention humaine directe. Il garantit que votre modèle peut continuellement fournir des prédictions précises basées sur des entrées de données en temps réel.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/n17.png align="left")

*Interface montrant le prix prédit*

## Nettoyage

Le service web que vous avez créé est hébergé dans une `instance de conteneur Azure`. Si vous n'avez pas l'intention de l'utiliser davantage, vous devez supprimer le point de terminaison pour éviter d'accumuler des coûts inutiles sur Azure.

La suppression de votre calcul garantit que votre abonnement ne sera pas facturé pour les ressources de calcul. Cependant, vous serez facturé d'un petit montant pour le stockage des données tant que l'espace de travail Azure Machine Learning existe dans votre abonnement.

Si vous avez terminé d'explorer Azure Machine Learning, vous pouvez supprimer l'espace de travail Azure Machine Learning et les ressources associées.

Pour supprimer votre espace de travail :

1. Dans le [portail Azure](https://portal.azure.com/?azure-portal=true), dans la page **Groupes de ressources**, ouvrez le groupe de ressources que vous avez spécifié lors de la création de votre espace de travail Azure Machine Learning.

2. Cliquez sur **Supprimer le groupe de ressources**, tapez le nom du groupe de ressources pour confirmer que vous souhaitez le supprimer, et sélectionnez **Supprimer**.

## Conclusion

Félicitations ! Vous avez réussi à créer et à déployer un modèle de régression en utilisant Azure Machine Learning Designer sans écrire une seule ligne de code.

Dans ce tutoriel, vous avez appris à nettoyer et pré-traiter les données, à construire et entraîner un modèle de machine learning, à évaluer ses performances et à le déployer en tant que service web. Cette approche low-code/no-code dans Azure Machine Learning Designer le rend accessible à tous pour utiliser la puissance du machine learning.

N'oubliez pas de nettoyer vos ressources pour éviter des frais inutiles. Avec ces compétences, vous pouvez maintenant expérimenter avec d'autres jeux de données et problèmes de machine learning. Les possibilités d'Azure sont infinies, et Azure Machine Learning fournit une plateforme robuste pour vos projets de science des données.

Jusqu'à la prochaine fois, santé ! :)