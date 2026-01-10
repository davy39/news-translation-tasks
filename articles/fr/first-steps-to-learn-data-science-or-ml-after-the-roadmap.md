---
title: Programmation, Mathématiques et Statistiques à Connaître pour la Science des
  Données et le Machine Learning
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-08-20T03:21:20.000Z'
originalURL: https://freecodecamp.org/news/first-steps-to-learn-data-science-or-ml-after-the-roadmap
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-14-at-3.08.07-AM.png
tags: []
seo_title: Programmation, Mathématiques et Statistiques à Connaître pour la Science
  des Données et le Machine Learning
seo_desc: 'At the start of this year, I published a mind map on the Data Science learning
  roadmap (shown below). Many people found the roadmap useful, my article got translated
  into different languages, and a large number of folks thanked me for publishing
  it.

  ...'
---

Au début de cette année, j'ai publié une carte mentale sur le [parcours d'apprentissage de la science des données (montré ci-dessous)](https://www.freecodecamp.org/news/data-science-learning-roadmap/). Beaucoup de gens ont trouvé le parcours utile, mon article a été traduit dans différentes langues, et un grand nombre de personnes m'ont remercié de l'avoir publié.

Tout allait bien jusqu'à ce que quelques développeurs soulignent qu'il y a trop de ressources et que beaucoup d'entre elles sont coûteuses. La programmation Python était la seule branche qui avait un certain nombre de très bons cours, mais elle s'arrête là pour les débutants.

Quelques questions importantes sur les fondements de la science des données m'ont frappé :

* Que devriez-vous faire après avoir appris à coder ? Y a-t-il des sujets qui vous aident à renforcer vos bases pour la science des données ?

* Que faire si vous détestez les mathématiques et que les tutoriels disponibles sont soit trop basiques, soit trop approfondis ? Pourrais-je recommander un cours compact mais complet sur les mathématiques et les statistiques ?

* Combien de mathématiques sont nécessaires pour commencer à apprendre comment les algorithmes de ML fonctionnent ?

* Quels sont les sujets essentiels de statistiques pour commencer avec l'analyse de données ou la science des données ?

Vous pouvez trouver des réponses à beaucoup de ces questions dans le livre [Deep Learning](https://www.deeplearningbook.org/) de **Ian Goodfellow et Yoshua Bengio**. Mais ce livre est un peu trop technique et mathématique pour beaucoup.

Alors dans cet article, je vais exposer quelques-unes des premières étapes que vous devriez suivre pour apprendre la science des données ou le machine learning.

## Les Trois Piliers de la Science des Données et du Machine Learning

![Image](https://www.freecodecamp.org/news/content/images/2021/08/pillars_ds.png align="left")

*Source :* [*wiplane.com*](wiplane.com)

Si vous parcourez les prérequis ou le travail préparatoire de tout cours de ML/DS, vous trouverez une combinaison de programmation, de mathématiques et de statistiques.

Voici ce que [Google recommande](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework) de faire avant de suivre un cours de ML :

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-18-at-5.42.43-PM.png align="left")

*Compétences Python recommandées par Google pour la Science des Données et le Machine Learning*

![Image](https://www.freecodecamp.org/news/content/images/2021/08/Screenshot-2021-08-18-at-5.42.34-PM.png align="left")

*Compétences en Mathématiques et Statistiques recommandées par Google pour le ML et la DS (*[*Source*](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework)*)*

Examinons ces compétences essentielles un peu plus en détail pour voir ce que vous devez apprendre pour vous lancer dans la Science des Données et le Machine Learning.

## Compétences Essentielles en Programmation pour la Science des Données et le Machine Learning

La plupart des rôles liés aux données sont basés sur la programmation, à l'exception de quelques-uns comme l'intelligence commerciale, l'analyse de marché, l'analyste produit, et autres.

Je vais me concentrer sur les emplois techniques liés aux données qui nécessitent une expertise dans au moins un langage de programmation.

Je préfère personnellement Python à tout autre langage en raison de sa polyvalence et de sa relative facilité d'apprentissage. Sans aucun doute un bon choix pour développer des projets de bout en bout.

### Sujets et bibliothèques à connaître pour la science des données :

* **Structures de données courantes** (types de données, listes, dictionnaires, ensembles, tuples), écriture de fonctions, logique, flux de contrôle, algorithmes de recherche et de tri, programmation orientée objet, et travail avec des bibliothèques externes.

* **Écriture de scripts Python pour extraire**, formater et stocker des données dans des fichiers ou les renvoyer vers des bases de données.

* **Gestion de tableaux multidimensionnels**, indexation, découpage, transposition, diffusion et génération de nombres pseudo-aléatoires avec NumPy.

* Exécution d'opérations vectorisées à l'aide de bibliothèques de calcul scientifique comme NumPy.

* **Manipulation de données avec Pandas**

séries, dataframe, indexation dans un dataframe, opérateurs de comparaison, fusion de dataframes, mappage et application de fonctions.

* **Nettoyage de données avec Pandas**

vérification des valeurs nulles, imputation, regroupement de données, description, réalisation d'une analyse exploratoire, et ainsi de suite.

* **Visualisation de données avec Matplotlib**

la hiérarchie de l'API, comment ajouter des styles, des couleurs et des marqueurs à un graphique, connaissance des différents types de graphiques et quand les utiliser, graphiques en ligne, graphiques en barres, graphiques de dispersion, histogrammes, boxplots, et Seaborn pour des graphiques plus avancés.

## Mathématiques Essentielles pour la Science des Données et le Machine Learning

Il existe des [raisons pratiques pour lesquelles les mathématiques sont essentielles](https://towardsdatascience.com/practical-reasons-to-learn-mathematics-for-data-science-1f6caec161ea) pour ceux qui veulent une carrière en tant que praticien du ML, scientifique des données ou ingénieur en deep learning.

### Vous Utiliserez l'Algèbre Linéaire pour Représenter les Données

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0063.JPG align="left")

*Une image du cours sur les normes vectorielles (*[*de ce cours*](https://www.wiplane.com/p/foundations-for-data-science-ml)*)*

Le ML est intrinsèquement basé sur les données. Les données sont au cœur du machine learning. Nous pouvons considérer les données comme des **vecteurs**

un objet qui respecte les règles arithmétiques. Cela nous amène à comprendre comment les règles de l'algèbre linéaire opèrent sur des tableaux de données.

### Vous Utiliserez le Calcul pour Entraîner les Modèles de ML

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0065.JPG align="left")

L'entraînement des modèles ne se fait pas "automatiquement". Le calcul différentiel est le moteur de l'apprentissage de la plupart des algorithmes de ML et de DL.

L'un des algorithmes d'optimisation les plus couramment utilisés

la **descente de gradient**est une application des dérivées partielles.

Un modèle est une représentation mathématique de certaines croyances et hypothèses. Il apprend (de manière approximative) le processus (linéaire, polynomial, etc.) de la façon dont les données sont fournies, et comment elles ont été générées en premier lieu. Il fait ensuite des prédictions basées sur ce processus appris.

### Sujets Importants en Mathématiques à Connaître pour la Science des Données et le Machine Learning :

* **Algèbre de base**

variables, coefficients, équations, fonctions

linéaires, exponentielles, logarithmiques, et ainsi de suite.

* **Algèbre Linéaire**

scalaires, vecteurs, tenseurs, normes (L1 & L2), produit scalaire, types de matrices, transformation linéaire, représentation d'équations linéaires en notation matricielle, résolution de problèmes de régression linéaire en utilisant des vecteurs et des matrices.

* **Calcul différentiel**

dérivées et limites, règles de dérivation, règle de la chaîne (pour l'algorithme de rétropropagation), dérivées partielles (pour calculer les gradients), convexité des fonctions, minima locaux/globaux, mathématiques derrière un modèle de régression, mathématiques appliquées pour entraîner un modèle à partir de zéro.

## Statistiques Essentielles pour la Science des Données et le Machine Learning

Chaque organisation aujourd'hui s'efforce de devenir axée sur les données. Pour y parvenir, les analystes et scientifiques de données doivent utiliser leurs données de différentes manières afin de guider leur prise de décision.

### Comment décrire les données

des données aux insights

Les données arrivent toujours brutes et désordonnées. L'exploration initiale vous indique ce qui manque, comment les données sont distribuées, et quelle est la meilleure façon de les nettoyer pour atteindre l'objectif final.

Afin de répondre aux questions définies, les statistiques descriptives vous permettent de transformer chaque observation dans vos données en insights compréhensibles.

### Comment quantifier l'incertitude

Vous devez également être capable de quantifier l'incertitude, et c'est une compétence extrêmement précieuse qui est très appréciée dans toute entreprise de données. Connaître les chances de succès dans toute expérience/décision est crucial pour toutes les entreprises.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/stats_dist.png align="left")

### Statistiques de base à connaître pour la Science des Données et le Machine Learning :

* Estimations de position

moyenne, médiane et autres variantes de celles-ci.

* Estimations de variabilité

* Corrélation et covariance

* Variables aléatoires

discrètes et continues

* Distributions de données PMF, PDF, CDF

* Probabilité conditionnelle

statistiques bayésiennes

* Distributions statistiques couramment utilisées

Gaussienne, Binomiale, Poisson, Exponentielle.

* Théorèmes importants

Loi des grands nombres et Théorème central limite.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0074.JPG align="left")

*Image du cours sur la distribution de Poisson (*[*de ce cours*](https://www.wiplane.com/p/foundations-for-data-science-ml)*)*

* **Statistiques Inférentielles**

Une branche plus pratique et avancée des statistiques qui aide à concevoir des expériences de test d'hypothèses, nous pousse à comprendre profondément la signification des métriques et en même temps nous aide à quantifier la signification des résultats.

* **Tests importants**

Test t de Student, test du Chi-Carré, test ANOVA, et ainsi de suite.

Et voilà. Tout enthousiaste de la science des données de niveau débutant devrait se concentrer sur ces trois piliers avant de plonger dans des cours de base en science des données ou en ML.

## Ressources pour Apprendre les Fondamentaux de la Science des Données et du Machine Learning

![Image](https://www.freecodecamp.org/news/content/images/2021/08/ds_roadmap.png align="left")

*\[https://www.freecodecamp.org/news/data-science-learning-roadmap/\](https://www.freecodecamp.org/news/data-science-learning-roadmap/" rel="nofollow noopener)*

[Mon parcours d'apprentissage](https://towardsdatascience.com/data-science-learning-roadmap-for-2021-84f2ba09a44f) vous a également indiqué quoi apprendre, et il était chargé de ressources, de cours et de programmes que vous pouvez suivre pour acquérir ces compétences.

Mais il y a quelques incohérences dans les ressources recommandées et le parcours que j'avais tracé. Et beaucoup de gens cherchaient un cours compact, complet, mais abordable.

### Problèmes avec les Cours de Science des Données ou de ML

1. Chaque cours de science des données que j'ai recommandé dans cet article nécessitait que vous ayez une compréhension décente de la programmation, des mathématiques ou des statistiques. Par exemple, [le cours le plus célèbre sur le ML par Andrew Ng](https://www.youtube.com/watch?v=PPLop4L2eGk&list=PLLssT5z_DsK-h9vYZkQkYNWcItqhlRJLN) repose également fortement sur la compréhension des étudiants de l'algèbre vectorielle et du calcul différentiel.

2. La plupart des cours qui couvrent les mathématiques et les statistiques pour la science des données sont simplement une liste de concepts requis pour la DS/ML sans explication sur la façon dont ils sont appliqués et comment ils sont programmés dans une machine.

3. Il existe des ressources exceptionnelles pour approfondir les mathématiques, mais la plupart d'entre nous ne sont pas faits pour cela et vous n'avez pas besoin d'être médaillé d'or en mathématiques pour apprendre la science des données.

**En résumé** : une ressource qui couvre juste assez de mathématiques appliquées ou de statistiques ou de programmation pour commencer avec la science des données ou le ML manque.

### Wiplane Academy

wiplane.com

J'ai donc décidé de me lancer et de tout faire moi-même. J'ai passé les trois derniers mois à développer un programme qui fournira une base solide pour votre carrière en tant que

* Analyste de données

* Scientifique des données

* Praticien/Ingénieur en ML

Ainsi, je vous présente les [**Fondamentaux pour la Science des Données ou le ML**](https://www.wiplane.com/p/foundations-for-data-science-ml)
**
[**Premières Étapes pour Apprendre la Science des Données et le ML**](https://www.wiplane.com/p/foundations-for-data-science-ml)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/IMG_0723.JPG align="left")

*C'est moi quand j'ai décidé de lancer.*

C'est un cours complet, compact et abordable qui couvre non seulement **tous les essentiels, les prérequis et le travail préparatoire**, mais explique également comment chaque concept est utilisé **de manière computationnelle et programmatique (en Python)**.

Et ce n'est pas tout  je continuerai à mettre à jour le contenu du cours chaque mois en fonction de vos retours.

En savoir plus [ici](https://www.wiplane.com/p/foundations-for-data-science-ml).

#### Offre Early Bird !

Je suis ravi de lancer la pré-vente de ce cours car je suis actuellement en train d'enregistrer et de monter les derniers modules (15-20 leçons). Ceux-ci seront également disponibles dès la première semaine de septembre.

Profitez de l'offre early bird, valable uniquement jusqu'au 30 août 2021.