---
title: 'Quand utiliser différents algorithmes de machine learning : un guide simple'
subtitle: ''
author: Roger Huang
co_authors: []
series: null
date: '2019-02-06T19:30:14.000Z'
originalURL: https://freecodecamp.org/news/when-to-use-different-machine-learning-algorithms-a-simple-guide-ba615b19fb3b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*uvJMjgk5h-wS7PkdHVJ7GA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Computer Science
  slug: computer-science
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
seo_title: 'Quand utiliser différents algorithmes de machine learning : un guide simple'
seo_desc: 'If you’ve been at machine learning long enough, you know that there is
  a “no free lunch” principle — there’s no one-size-fits-all algorithm that will help
  you solve every problem and tackle every dataset.

  I work for Springboard — we’ve put a lot of r...'
---

Si vous vous intéressez au machine learning depuis suffisamment longtemps, vous savez qu'il existe un principe de "pas de repas gratuit" — il n'existe pas d'algorithme universel qui vous aidera à résoudre tous les problèmes et à traiter tous les ensembles de données.

Je travaille pour Springboard — nous avons investi beaucoup de recherche dans la formation et les ressources en machine learning. Chez Springboard, [nous proposons le premier cours en ligne avec une garantie d'emploi en machine learning](https://www.springboard.com/workshops/ai-machine-learning-career-track/?utm_source=freecodecamp&utm_medium=medium&utm_content=freecodecampdifferentml).

Ce qui aide beaucoup lorsqu'on est confronté à un nouveau problème, c'est d'avoir une introduction sur l'algorithme qui pourrait être le mieux adapté à certaines situations. Ici, nous parlons de différents problèmes et types de données et discutons de l'algorithme le plus efficace à essayer pour chacun, ainsi qu'une ressource qui peut vous aider à implémenter ce modèle particulier.

Rappelez-vous : la preuve est dans le pudding : la meilleure approche pour vos données est le modèle qui vous donne empiriquement les meilleurs résultats. Ce guide est destiné à affiner vos premiers instincts et à vous aider à vous souvenir des modèles qui pourraient être les plus efficaces pour chaque problème, et lesquels seraient impraticables à utiliser.

Commençons par parler des variables que nous devons considérer.

#### **Apprentissage non supervisé vs apprentissage supervisé**

L'**apprentissage non supervisé** est celui où vous permettez à l'algorithme de machine learning de commencer à apprendre et à produire un résultat sans aucun traitement explicite des données par l'homme au préalable.

L'**apprentissage supervisé** implique un certain étiquetage et traitement des données d'entraînement au préalable afin de les structurer pour le traitement.

Le type d'apprentissage que vous pouvez effectuer aura beaucoup d'importance lorsque vous commencerez à travailler avec différents algorithmes de machine learning.

#### **Considérations d'espace et de temps**

Il existe des **considérations d'espace et de temps** pour chaque algorithme de machine learning. Bien qu'en pratique vous travaillerez probablement avec des versions optimisées de chaque algorithme intégrées dans un framework, il est bon de considérer comment les algorithmes que vous choisissez peuvent affecter les performances.

#### **La sortie**

Troisièmement, et peut-être le plus important, c'est **la sortie que vous souhaitez obtenir**. Essayez-vous de catégoriser des données ? Les utiliser pour prédire de futurs points de données ? Ce que vous cherchez à obtenir comme résultat et ce que vous voulez faire avec vos données déterminera largement les approches algorithmiques que vous devriez adopter.

### Quelques exemples

#### **Vous cherchez à construire un modèle prédictif simple avec un ensemble de données bien structuré sans trop de complications.**

Votre meilleur choix ici est probablement la régression linéaire, quelque chose qui peut prendre une multitude de facteurs et ensuite vous donner un résultat prédictif avec une explication simple du taux d'erreur et une explication simple des facteurs qui contribuent à la prédiction. Cela ne prend pas beaucoup de puissance de calcul pour exécuter une régression linéaire non plus.

**Ressource** : [Régression Linéaire — Vue Détaillée](https://towardsdatascience.com/linear-regression-detailed-view-ea73175f6e86)

#### **Vous cherchez à classifier des données déjà étiquetées en deux ou plusieurs types de labels distincts (par exemple, déterminer si les enfants sont probablement masculins ou féminins en fonction de leur poids et de leur taille) dans un cadre supervisé.**

Le premier instinct que vous devriez avoir lorsque vous voyez une situation comme celle-ci est d'appliquer le **modèle de régression logistique**. Après avoir exécuté le modèle, vous verrez qu'il force chaque point de données dans deux catégories différentes, vous permettant de sortir facilement quel point appartient à quelle catégorie. Le modèle de régression logistique peut également être facilement généralisé pour travailler avec plusieurs classes cibles et de résultats si c'est ce que votre problème exige.

**Ressource** : [Construction d'une Régression Logistique](https://towardsdatascience.com/building-a-logistic-regression-in-python-301d27367c24)

#### **Vous cherchez à placer des données continues non étiquetées dans différents groupes (par exemple, mettre des clients avec certains traits enregistrés et essayer de découvrir des catégories/groupes auxquels ils peuvent appartenir).**

Le premier choix naturel pour ce problème est l'algorithme de clustering K-Means, qui regroupera et clusterisera les données en mesurant la distance entre chaque point. Ensuite, il existe une variété d'algorithmes de clustering, tels que le Density-Based Spatial Clustering of Applications with Noise et les algorithmes Mean-Shift.

**Ressource** : [Les 5 Algorithmes de Clustering que les Data Scientists Doivent Connaître](https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68)

#### **Vous cherchez à prédire si une chaîne de caractères ou un regroupement de traits appartient à une catégorie de données ou à une autre (classification de texte supervisée) — par exemple, si un avis est positif ou négatif.**

Votre meilleur choix ici est probablement Naive Bayes, qui est un modèle simple mais puissant qui peut être utilisé pour la classification de texte. Avec un certain prétraitement et nettoyage du texte (en étant particulièrement prudent pour supprimer les mots vides de sens tels que "et" qui pourraient ajouter du bruit à votre ensemble de données), vous pouvez obtenir un ensemble remarquable de résultats avec un modèle très simple.

Un autre bon choix est la régression logistique, qui est un modèle simple à comprendre et à expliquer, et moins difficile à démêler que Naive Bayes (qui attribuera souvent des probabilités mot par mot plutôt que d'étiqueter globalement un extrait de texte comme appartenant à un groupe ou à un autre).

Passons à quelque chose de plus puissant, un algorithme de Machine à Vecteurs de Support Linéaire améliorera probablement vos performances. Si vous voulez sauter directement ici, vous pouvez (bien que je suggère d'essayer les deux modèles et de comparer lequel fonctionne le mieux — [Naive Bayes a une implémentation absurdement facile](https://scikit-learn.org/stable/modules/naive_bayes.html) sur des frameworks comme scikit-learn et ce n'est pas très coûteux en calcul, donc vous pouvez vous permettre de tester les deux).

Enfin, l'analyse de sac de mots pourrait également fonctionner — envisagez de faire un ensemble de différentes méthodes et de tester toutes ces méthodes les unes contre les autres, selon l'ensemble de données en question.

**Ressource** : [Comparaison et Sélection de Modèles de Classification de Texte Multi-Classe](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)

#### **Vous cherchez à faire de l'apprentissage non structuré sur des ensembles de données d'images ou de vidéos à grande échelle (par exemple, classification d'images).**

Le meilleur algorithme pour traiter différentes images est un réseau de neurones convolutionnel organisé de manière similaire à l'analyse des cortex visuels animaux.

Mesuré par la performance (taux d'erreur réduit) dans la compétition ImageNet, l'architecture SE-Resnet se distingue, bien que le domaine étant encore en développement, de nouvelles avancées apparaissent presque tous les jours.

Vous devez cependant être conscient que les réseaux de neurones convolutionnels sont denses et nécessitent beaucoup de puissance de calcul — assurez-vous donc d'avoir la capacité matérielle pour exécuter ces modèles sur des ensembles de données à grande échelle.

**Ressource** : [Revue des Algorithmes de Deep Learning pour la Classification d'Images](https://medium.com/zylapp/review-of-deep-learning-algorithms-for-image-classification-5fdbca4a05e2)

#### **Vous cherchez à classifier des points de résultat qui proviennent d'un processus bien défini (ex : nombre d'embauches issues d'un processus d'entretien préétabli, où vous connaissez ou pouvez inférer computationnellement les probabilités de chaque événement).**

La meilleure option pour cela est probablement un algorithme d'arbre de décision qui expliquera clairement quels sont les points de division entre le fait de classifier quelque chose dans un groupe ou un autre.

**Ressource** : [Arbres de Décision en Machine Learning](https://towardsdatascience.com/decision-trees-in-machine-learning-641b9c4e8052)

#### **Vous cherchez à faire une analyse de séries temporelles avec des données bien définies et supervisées (par exemple, prédire les prix des actions sur la base de modèles historiques du marché boursier disposés sur une base chronologique du passé au présent).**

Un réseau de neurones récurrent est conçu pour faire de l'analyse de séquences en contenant une mémoire interne en flux des données qu'il traite, lui permettant de prendre en compte la relation entre les données et l'horizon temporel et l'ordre dans lequel elles sont déployées.

**Ressource** : [Réseaux de Neurones Récurrents et LSTM](https://builtin.com/data-science/recurrent-neural-networks-and-lstm)

### Conclusion

Prenez les recommandations et les ressources ci-dessus, et appliquez-les comme une sorte de premier instinct pour votre modélisation — cela vous aidera à vous lancer dans tout travail que vous faites un peu plus rapidement. Si vous êtes intéressé à être mentoré par un expert en machine learning pour apprendre à entraîner davantage vos instincts, consultez le [Parcours Carrière en IA/Machine Learning](https://www.springboard.com/workshops/ai-machine-learning-career-track/?utm_source=freecodecamp&utm_medium=medium&utm_content=freecodecampdifferentml) de Springboard.