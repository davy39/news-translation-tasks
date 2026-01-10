---
title: Comment construire un projet de science des données à partir de zéro
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-13T23:17:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-data-science-project-from-scratch-dc4f096a62a1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kF7On_Ajcb5g0ASNNetA7Q.png
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: data visualization
  slug: data-visualization
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: Comment construire un projet de science des données à partir de zéro
seo_desc: 'By Jekaterina Kokatjuhha

  A demonstration using an analysis of Berlin rental prices


  There are many online courses about data science and machine learning that will
  guide you through a theory and provide you with some code examples and an analysis
  of ...'
---

Par Jekaterina Kokatjuhha

#### **Une démonstration utilisant une analyse des prix des locations à Berlin**

![Image](https://cdn-media-1.freecodecamp.org/images/ms8KLB-gLlSD6kB5FgFwKWNuiDhHdSrfxOQP)

Il existe de nombreux cours en ligne sur la science des données et l'apprentissage automatique qui vous guideront à travers la théorie et vous fourniront des exemples de code et une analyse de données **très propres**.

Cependant, pour commencer à pratiquer la science des données, il est préférable de relever un problème réel. Creuser dans les données pour trouver des informations plus profondes. Réaliser l'ingénierie des caractéristiques en utilisant des sources de données supplémentaires et construire des pipelines d'apprentissage automatique autonomes.

Cet article de blog vous guidera à travers les principales étapes de la construction d'un projet de science des données à partir de zéro. Il est basé sur un **problème réel** — quels sont les principaux facteurs des prix des locations à Berlin ? Il fournira une analyse de cette situation. Il mettra également en lumière l'erreur courante que les débutants ont tendance à commettre en matière d'apprentissage automatique.

Voici les étapes qui seront discutées en détail :

* trouver un sujet
* extraire des données du web et les nettoyer
* obtenir des informations plus profondes
* ingénierie des caractéristiques en utilisant des API externes
* erreurs courantes lors de la réalisation de l'apprentissage automatique
* importance des caractéristiques : trouver les facteurs des prix des locations
* construction de modèles d'apprentissage automatique.

![Image](https://cdn-media-1.freecodecamp.org/images/HEcZhCOGhmtTxl9hI3xiJVJrJBPil3FWdrwU)

### Trouver un sujet

Il existe de nombreux problèmes qui peuvent être résolus en analysant des données, mais il est toujours préférable de trouver un problème qui vous intéresse et qui vous motive. Lors de la recherche d'un sujet, vous devriez définitivement vous concentrer sur vos préférences et intérêts.

Par exemple, si vous êtes intéressé par les systèmes de santé, il existe de nombreux angles sous lesquels vous pourriez analyser les données fournies sur ce sujet. [« Exploring the ChestXray14 dataset: problems »](https://lukeoakdenrayner.wordpress.com/2017/12/18/the-chestxray14-dataset-problems/) est un exemple de la manière de questionner la qualité des données médicales. Un autre exemple — si vous êtes intéressé par la musique, vous pourriez essayer de [prédire le genre de la chanson à partir de son audio](https://hackernoon.com/finding-the-genre-of-a-song-with-deep-learning-da8f59a61194).

Cependant, je suggère non seulement de vous concentrer sur vos intérêts, mais aussi d'écouter ce dont parlent les gens autour de vous. Qu'est-ce qui les dérange ? De quoi se plaignent-ils ? Cela peut être une autre bonne source d'idées pour un projet de science des données. Dans les cas où les gens se plaignent encore, cela peut signifier que le problème n'a pas été résolu correctement la première fois. Ainsi, si vous le relevez avec des données, vous pourriez fournir une solution encore meilleure et avoir un impact sur la manière dont ce sujet est perçu.

Cela peut sembler un peu trop abstrait, alors découvrons comment j'ai eu l'idée d'analyser les prix des locations à Berlin.

> « Si j'avais su que les prix des locations étaient si élevés ici, j'aurais négocié un salaire plus élevé. »

Ce n'est qu'une des choses que j'ai entendues de la part de personnes qui avaient récemment déménagé à Berlin pour travailler. La plupart des nouveaux arrivants se plaignaient de ne pas avoir imaginé Berlin si chère, et qu'il n'y avait aucune statistique sur les fourchettes de prix possibles de l'appartement. S'ils l'avaient su à l'avance, ils auraient pu demander un salaire plus élevé lors du processus de candidature ou auraient pu envisager d'autres options.

J'ai googlé, vérifié plusieurs sites web de locations d'appartements, et demandé à plusieurs personnes, mais je n'ai pas pu trouver de statistiques ou de visualisations plausibles des prix actuels du marché. Et c'est ainsi que j'ai eu l'idée de cette analyse.

Je voulais rassembler les données, construire un tableau de bord interactif où vous pourriez sélectionner différentes options telles qu'un appartement de 40m2 situé à Berlin Mitte avec un balcon et une cuisine équipée, et il vous montrerait les fourchettes de prix. Cela, à lui seul, aiderait les gens à comprendre les prix des appartements à Berlin. De plus, en appliquant l'apprentissage automatique, je pourrais identifier les facteurs des prix des locations et pratiquer avec différents algorithmes d'apprentissage automatique.

### Extraire des données du web et les nettoyer

#### Obtenir les données

Maintenant que vous avez une idée de votre projet de science des données, vous pouvez commencer à chercher les données. Il existe des tonnes de dépôts de données incroyables, tels que [Kaggle](http://kaggle.com/), [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php) ou [moteurs de recherche de jeux de données](https://toolbox.google.com/datasetsearch), et [sites web](https://www.ncbi.nlm.nih.gov/) contenant des articles académiques avec des jeux de données. Alternativement, vous pourriez utiliser le [web scraping](https://en.wikipedia.org/wiki/Web_scraping).

Mais soyez prudent — les anciennes données sont partout. Lorsque je cherchais des informations sur les prix des locations à Berlin, j'ai trouvé de nombreuses visualisations **mais** elles étaient anciennes, ou sans aucune année spécifiée.

Pour certaines statistiques, elles avaient même une note disant que ce prix ne serait que pour un appartement de 2 pièces de 50 m2 sans meubles. Mais que faire si je cherche un appartement plus petit avec une cuisine meublée ?

![Image](https://cdn-media-1.freecodecamp.org/images/OfYfzPZ0DuXY1QH6zLCxzl3evl7KhLJybYtc)
_Les anciennes données sont partout._

Comme je ne pouvais trouver que des anciennes données, j'ai décidé de **web scraper** les sites web qui proposaient des appartements à louer. Le web scraping est une technique utilisée pour extraire des données de sites web par un processus automatisé.

[Mon article de blog sur le web scraping](https://hackernoon.com/web-scraping-tutorial-with-python-tips-and-tricks-db070e70e071) entre dans les détails des pièges et des modèles de conception du web scraping.

[**Web Scraping Tutorial with Python: Tips and Tricks**](https://hackernoon.com/web-scraping-tutorial-with-python-tips-and-tricks-db070e70e071)
[_J'étais à la recherche de billets d'avion et j'ai remarqué que les prix des billets fluctuent pendant la journée. J'ai essayé de découvrir quand..._hackernoon.com](https://hackernoon.com/web-scraping-tutorial-with-python-tips-and-tricks-db070e70e071)

Voici les principales conclusions :

* Avant de scraper, vérifiez s'il existe une API publique disponible
* **Soyez gentil** ! Ne surchargez pas le site web en envoyant des centaines de requêtes par seconde
* Enregistrez la date à laquelle l'extraction a eu lieu. Il sera expliqué pourquoi cela est important.

#### Nettoyage des données

Une fois que vous commencez à obtenir les données, il est très important de les examiner le plus tôt possible afin de trouver d'éventuels problèmes.

Lors du web scraping des données de location, j'ai inclus quelques petites vérifications telles que le nombre de valeurs manquantes pour toutes les caractéristiques. Les webmasters pourraient changer le HTML du site web, ce qui entraînerait mon programme à ne plus obtenir les données.

Une fois que j'ai assuré que tous les aspects techniques du web scraping étaient couverts, j'ai pensé que les données seraient presque idéales. Cependant, j'ai fini par nettoyer les données pendant environ une semaine en raison de doublons pas si évidents.

Une fois que vous commencez à obtenir les données, il est très important de les examiner le plus tôt possible afin de trouver d'éventuels problèmes. Par exemple, si vous faites du web scraping, vous auriez pu manquer certains champs importants. Si vous utilisez un séparateur de virgule lors de l'enregistrement des données dans un fichier, et que l'un des champs contient également des virgules, vous pouvez finir par avoir des fichiers qui ne sont pas bien séparés.

![Image](https://cdn-media-1.freecodecamp.org/images/XQFpm6-6PuLVfl86ZtxUzCFkT81v-nVBMymH)
_ILLUSION vs RÉALITÉ_

Il y avait plusieurs sources de doublons :

* Appartements dupliqués car ils étaient en ligne depuis un certain temps
* Les agences avaient des erreurs de saisie, par exemple le prix de location ou l'étage de l'appartement. Elles les corrigeaient après un certain temps, ou publiaient une nouvelle annonce complètement nouvelle avec des valeurs corrigées et des modifications de description supplémentaires
* Certains prix ont été modifiés (augmentés et diminués) après un mois pour le même appartement

Alors que les doublons du premier cas étaient faciles à identifier par leur ID, les doublons du deuxième cas étaient très compliqués. La raison est qu'une agence pouvait légèrement modifier une description, corriger le prix erroné, et le publier comme une nouvelle annonce de sorte que l'ID serait également nouveau.

J'ai dû inventer de nombreuses règles basées sur la logique pour filtrer les anciennes versions des annonces. Une fois que j'ai pu identifier que ces appartements seraient les véritables doublons mais avec des modifications mineures, j'ai pu les trier par date d'extraction, en prenant le dernier comme le plus récent.

De plus, certaines agences augmentaient ou diminuaient le prix pour le même appartement après un mois. On m'a dit que si personne ne voulait cet appartement, le prix diminuerait. Inversement, on m'a dit que, s'il y avait tant de demandes pour celui-ci, les agences augmentaient le prix. Ces explications semblent bonnes.

### Obtenir des informations plus profondes

Maintenant que nous avons tout prêt, nous pouvons commencer à analyser les données. Je sais que les scientifiques des données adorent seaborn et ggplot2, ainsi que de nombreuses visualisations statiques à partir desquelles ils peuvent tirer des informations.

Cependant, les tableaux de bord interactifs peuvent vous aider, vous et les autres parties prenantes, à trouver des informations utiles. Il existe de nombreux outils incroyables et faciles à utiliser pour cela, tels que [Tableau](https://www.tableau.com/) et [Microstrategy](https://www.microstrategy.com/us).

Il m'a fallu moins de 30 minutes pour créer un tableau de bord interactif où l'on peut sélectionner tous les composants importants et voir comment le prix changerait.

![Image](https://cdn-media-1.freecodecamp.org/images/v-GcLn7g5Dpu9DPliwe5wmc1EnOFD7QGMpFQ)
_Tableau de bord interactif des prix des locations à Berlin : on peut sélectionner toutes les configurations possibles et voir la distribution de prix correspondante. (Date des données : Hiver 2017/18)_

Un tableau de bord assez simple pourrait déjà fournir des **informations** sur les prix à Berlin pour les nouveaux arrivants et pourrait être un bon **moteur utilisateur pour un site web de locations d'appartements**.

Déjà à partir de cette visualisation de données, vous pouvez voir que la distribution des prix des appartements de 2,5 pièces tombe dans la distribution des appartements de 2 pièces. La raison en est que la plupart des appartements de 2,5 pièces ne sont pas situés au centre de la ville, ce qui, bien sûr, réduit le prix.

![Image](https://cdn-media-1.freecodecamp.org/images/eSUd6KemodW6Q9qXWRjQQwE7YqZMGy8Tigo1)
_Distribution des prix et nombre d'appartements à Berlin._

Ces données ont été recueillies en hiver 2017/18 et elles deviendront également obsolètes. Cependant, mon point est que les sites web de locations pourraient mettre à jour fréquemment leurs statistiques et visualisations pour fournir plus de transparence à cette question.

### Ingénierie des caractéristiques en utilisant des API externes

La visualisation vous aide à identifier les attributs importants, ou « caractéristiques », qui pourraient être utilisés par ces algorithmes d'apprentissage automatique. Si les caractéristiques que vous utilisez sont très peu informatives, tout algorithme produira de mauvaises prédictions. Avec des caractéristiques très fortes, même un algorithme très simple peut produire des résultats assez décents.

Dans le projet de prix de location, le prix est une variable continue, donc c'est un problème de régression typique. En prenant toutes les informations extraites, j'ai collecté les caractéristiques suivantes afin de pouvoir prédire un prix de location.

![Image](https://cdn-media-1.freecodecamp.org/images/5jLyNwUnWIDvzXC5Ye4B77ElHPZT8vB65fZ4)
_Ce sont la majorité des caractéristiques utilisées pour prédire le prix de location de l'appartement._

Cependant, il y avait une caractéristique qui était problématique, à savoir l'adresse. Il y avait 6,6K appartements et environ 4,4K adresses uniques de granularité différente. Il y avait environ 200 codes postaux uniques qui pourraient être convertis en variables fictives, mais alors des informations très précieuses sur un emplacement particulier seraient perdues.

![Image](https://cdn-media-1.freecodecamp.org/images/IJtEp4SDjt4uzoh1UHLrzWnzWJZ8LhDEFzB7)
_Différente granularité de l'adresse : rue avec le numéro de maison, rue avec numéro de maison masqué et seulement un code postal._

**Que faites-vous lorsque vous recevez une nouvelle adresse ?**
Vous la googlez pour voir où elle se trouve ou comment y aller.

En utilisant une API externe suivant les quatre caractéristiques supplémentaires données, l'adresse de l'appartement pourrait être calculée :

1. durée d'un trajet en train jusqu'à la S-Bahn Friedrichstrasse (gare centrale)

2. distance jusqu'à U-Bahn Stadtmitte (centre-ville) en voiture

3. durée d'un trajet à pied jusqu'à la station de métro la plus proche

4. nombre de stations de métro dans un rayon d'un kilomètre de l'appartement

Ces quatre caractéristiques ont considérablement amélioré les performances.

### **Erreurs courantes lors de la réalisation de l'apprentissage automatique et de la science des données**

Après le scraping ou l'obtention des données, il y a de nombreuses étapes à accomplir **avant** d'appliquer un modèle d'apprentissage automatique.

Vous devez visualiser chacune des variables pour voir les distributions, trouver les valeurs aberrantes et comprendre pourquoi il y a de telles valeurs aberrantes.

Que pouvez-vous faire avec les valeurs manquantes dans certaines caractéristiques ?

Quelle serait la meilleure façon de convertir les caractéristiques catégorielles en caractéristiques numériques ?

Il y a de nombreuses questions de ce type, mais je vais donner quelques détails sur celles où la majorité des débutants rencontrent des erreurs.

#### 1. Visualisation

Tout d'abord, vous devriez visualiser la distribution des caractéristiques continues pour avoir une idée s'il y a beaucoup de valeurs aberrantes, quelle serait la distribution et si cela a du sens.

Il existe de nombreuses façons de le visualiser, par exemple [box plots](https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/box-plot-review), [histogrammes](https://en.wikipedia.org/wiki/Histogram), [fonctions de distribution cumulatives](https://en.wikipedia.org/wiki/Cumulative_distribution_function) et [violin plots](https://en.wikipedia.org/wiki/Violin_plot). Cependant, on devrait choisir le graphique qui donnera le plus d'informations sur les données.

Pour voir la distribution (si elle est [normale](https://en.wikipedia.org/wiki/Normal_distribution), ou [bimodale](https://en.wikipedia.org/wiki/Multimodal_distribution)), les histogrammes seront les plus utiles. Bien que les histogrammes soient un bon point de départ, les box plots pourraient être supérieurs pour identifier le nombre de valeurs aberrantes et voir où se situent les quartiles médians.

Sur la base des graphiques, la question la plus intéressante serait : **voyez-vous ce que vous vous attendiez à voir ?** Répondre à cette question vous aidera soit à trouver des informations, soit à trouver des bugs dans les données.

Pour m'inspirer et comprendre quel graphique donnera le plus de valeur, je me suis fréquemment référé à la [galerie seaborn de Python](https://seaborn.pydata.org/examples/index.html). Une autre bonne source d'inspiration pour la visualisation et la recherche d'informations sont les noyaux sur Kaggle. [Voici mon noyau Kaggle](https://www.kaggle.com/jkokatjuhha/in-depth-visualisations-simple-methods) de la visualisation approfondie du jeu de données Titanic.

Dans le contexte des prix des locations, j'ai tracé les histogrammes de chaque caractéristique continue et je m'attendais à voir une longue queue à droite dans la distribution du loyer sans factures et de la surface totale.

![Image](https://cdn-media-1.freecodecamp.org/images/OQfpf4O6rIr2hyAgp6oWPaOSirpej2-H8gMR)
_Histogrammes des caractéristiques continues_

Les box plots m'ont aidé à voir le nombre de valeurs aberrantes pour chacune des caractéristiques. En fait, la plupart des appartements aberrants basés sur le loyer sans factures étaient soit les ateliers pour les petites boutiques de plus de 200m2, soit les résidences étudiantes avec un loyer très bas.

![Image](https://cdn-media-1.freecodecamp.org/images/o8jxLkLMlY6UgebyEjvpy6hfBySSGkqExNhb)
_Boxplots des caractéristiques continues_

#### 2. Dois-je imputer les valeurs en fonction de l'ensemble du jeu de données ?

Parfois, il y aura des valeurs manquantes, pour diverses raisons. Si nous excluons chaque observation avec au moins une valeur manquante, nous pouvons finir avec un jeu de données très réduit.

Il existe [de nombreuses façons d'imputer](https://www.iriseekhout.com/missing-data/missing-data-methods/imputation-methods/) les valeurs, moyenne ou médiane. C'est à vous de décider comment le faire **mais** assurez-vous de calculer les statistiques d'imputation **uniquement sur les données d'entraînement pour éviter la [fuite de données](https://machinelearningmastery.com/data-leakage-machine-learning/)** de votre jeu de test.

Dans les données de location, j'ai également extrait une description de l'appartement. Chaque fois que la qualité, l'état ou le type d'appartement était manquant, je l'imputais à partir de la description si la description contenait cette information.

#### 3. Comment transformer les variables catégorielles ?

Certains algorithmes, selon l'implémentation, ne fonctionneraient pas directement avec les données catégorielles, donc il faudrait les transformer d'une manière ou d'une autre en valeurs numériques.

Il existe de nombreuses façons de transformer les variables catégorielles en caractéristiques numériques, telles que [Label Encoder, One Hot Encoding, bin encoding](http://pbpython.com/categorical-encoding.html), et hashing encoding. Cependant, la plupart des gens utilisent le Label Encoding **incorrectement** lorsque le One Hot Encoding aurait dû être utilisé à la place.

Supposons, dans nos données de location, que nous avons une colonne de type d'appartement avec les valeurs suivantes : [rez-de-chaussée, loft, maisonnette, loft, loft, rez-de-chaussée]. LabelEncoder peut transformer cela en [3,2,1,2,2,1], introduisant une ordinalité, ce qui signifie que rez_de_chaussée > loft > maisonnette. Pour certains algorithmes comme les arbres de décision et leurs dérivés, ce type de codage pour cette caractéristique serait acceptable, mais appliquer des régressions et SVM pourrait ne pas avoir autant de sens.

Dans le jeu de données des prix de location, la **condition** est codée comme suit :

* neuf : 1
* rénové : 2
* nécessite rénovation : 3

et la **qualité** comme :

* Luxe : 1
* mieux que normal : 2
* normal : 3
* simple : 4
* inconnu : 5

#### 4. Dois-je standardiser les variables ?

La standardisation amène toutes les variables continues à la même échelle, ce qui signifie que si une variable a des valeurs de 1K à 1M et une autre de 0,1 à 1, après standardisation, elles auront la même plage.

Les [régularisations L1 ou L2](https://towardsdatascience.com/l1-and-l2-regularization-methods-ce25e7fc831c) sont le moyen courant de réduire le [surapprentissage](https://machinelearningmastery.com/overfitting-and-underfitting-with-machine-learning-algorithms/) et peuvent être utilisées dans de nombreux algorithmes de régression. Cependant, il est important d'appliquer la standardisation des caractéristiques **avant** L1 ou L2.

Le prix de location est en euros, donc le coefficient ajusté serait environ 100 fois plus grand que le coefficient ajusté si le prix était en centimes. L1 et L2 pénalisent davantage les coefficients plus grands, ce qui signifie qu'ils pénaliseront davantage les caractéristiques à plus petites échelles. Pour éviter cela, les caractéristiques doivent être standardisées avant d'appliquer L1 ou L2.

Une autre raison de standardiser est que si vous ou votre algorithme utilisez la descente de gradient, la descente de gradient converge beaucoup plus rapidement avec la mise à l'échelle des caractéristiques.

#### 5. Dois-je dériver le logarithme de la variable cible ?

Il m'a fallu un certain temps pour comprendre qu'il n'y a **pas de réponse universelle**.

Cela dépend de nombreux facteurs :

* si vous voulez une erreur fractionnaire ou absolue
* quel algorithme vous utilisez
* ce que les graphiques de résidus et les changements dans les métriques vous indiquent

En régression, [faites d'abord attention aux graphiques de résidus](http://docs.statwing.com/interpreting-residual-plots-to-improve-your-regression/) et à la métrique. Parfois, la logarithisation de la variable cible conduit à un meilleur modèle et les résultats du modèle seraient encore faciles à comprendre. Cependant, il existe encore d'autres transformations qui pourraient être intéressantes, comme prendre la racine carrée.

Il existe de nombreuses réponses sur Stack Overflow concernant cette question, et je pense que [Residual Plots and RMSE on raw and log target variable](https://stats.stackexchange.com/questions/319880/non-linear-regression-residual-plots-and-rmse-on-raw-and-log-target-variable) l'explique très bien.

Pour les données de location, j'ai dérivé le logarithme du prix car les graphiques de résidus semblaient un peu meilleurs.

![Image](https://cdn-media-1.freecodecamp.org/images/TcZRXjNf4kUTLAvu-LqWikfo2HIc8OVzJdyF)
_Graphiques de résidus des logarithmes (à gauche) et des données non transformées (à droite) de la variable loyer sans les factures. Le graphique de droite présente une « hétéroscédasticité » — les résidus deviennent plus grands à mesure que la prédiction passe de petite à grande._

#### 6. Autres éléments importants

Certains algorithmes, comme les régressions, souffriront de [colinéarités](https://en.wikipedia.org/wiki/Multicollinearity) dans les données car les coefficients deviennent très instables ([plus de maths](http://www.stat.cmu.edu/~larry/=stat401/lecture-17.pdf)). [SVM](https://en.wikipedia.org/wiki/Support_vector_machine) [peut ou non souffrir](https://stats.stackexchange.com/questions/149662/is-support-vector-machine-sensitive-to-the-correlation-between-the-attributes) de colinéarité en raison du choix du noyau.

Les algorithmes basés sur les décisions ne souffriront pas de multicolinéarité car ils pourraient utiliser des caractéristiques de manière interchangeable dans différents arbres sans que cela n'affecte les performances. Cependant, l'interprétation de l'importance des caractéristiques devient alors plus difficile car la variable corrélée peut ne pas sembler aussi importante qu'elle ne l'est.

### Apprentissage automatique

Après vous être familiarisé avec les données et avoir nettoyé les valeurs aberrantes, c'est le moment idéal pour vous initier à l'apprentissage automatique. Il existe de nombreux algorithmes que vous pourriez utiliser pour cet apprentissage automatique supervisé.

Il y avait trois algorithmes différents que je voulais explorer, en comparant des caractéristiques telles que les différences de performance et la vitesse. Ces trois algorithmes étaient des arbres boostés par gradient avec différentes implémentations (XGBoost et LightGMB), Random Forest (FR, scikit-learn) et des réseaux neuronaux à 3 couches (NN, Tensorflow). J'ai sélectionné RMSLE (root mean squared logarithm error) comme métrique pour l'optimisation du processus. J'ai utilisé RMSLE parce que j'ai dérivé le logarithme de la variable cible.

XGBoost et LigthGBM ont performé de manière comparable, RF légèrement moins bien, tandis que NN était le pire.

![Image](https://cdn-media-1.freecodecamp.org/images/QGTor8s2YdV0z0Qbaz0bHV4M2fSXNI9vJFA9)
_Performance (RMSLE) des algorithmes sur l'ensemble de test._

Les algorithmes basés sur les arbres de décision sont très bons pour interpréter les caractéristiques. Par exemple, ils produisent un score d'importance des caractéristiques.

#### Importance des caractéristiques : trouver les facteurs du prix de location

Après avoir ajusté un modèle basé sur les arbres de décision, vous pouvez voir quelles caractéristiques sont les plus précieuses pour la prédiction des prix.

L'importance des caractéristiques fournit un score qui indique à quel point chaque caractéristique a été informative dans la construction des arbres de décision au sein du modèle. L'une des façons de calculer ce score est de compter combien de fois une caractéristique est utilisée pour diviser les données à travers tous les arbres. Ce score peut être calculé de [différentes manières](https://datascience.stackexchange.com/questions/12318/how-do-i-interpret-the-output-of-xgboost-importance).

L'importance des caractéristiques peut révéler d'autres informations sur les principaux facteurs de prix.

Pour la prédiction des prix de location, il n'est pas surprenant que la surface totale soit le facteur le plus important du prix. Intéressamment, certaines caractéristiques qui ont été conçues avec une API externe sont également parmi les caractéristiques les plus importantes.

![Image](https://cdn-media-1.freecodecamp.org/images/BdO3HBXjWAoIWXoqxIrdnAmVVDBAWYlDeWZm)
_Importance des caractéristiques calculée par division (ci-dessus) et par gain (ci-dessous)_

Cependant, comme mentionné dans « Interpretable Machine Learning with XGBoost », il peut y avoir des incohérences dans l'importance des caractéristiques en fonction de l'option d'attribution. L'auteur de l'article de blog lié, et du papier SHAP NIPS, propose une nouvelle façon de calculer l'importance des caractéristiques qui sera à la fois précise et cohérente. Cela utilise la [bibliothèque shap Python](https://github.com/slundberg/shap). Les valeurs SHAP représentent la responsabilité d'une caractéristique pour un changement dans la sortie du modèle.

Le résultat de l'analyse sur les données de prix de location est montré dans la figure ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/PT9ETep2V9uLrrvJrMqJNN0YkoMhbswXPEPv)
_Chaque appartement a un point sur chaque ligne. La position x du point est l'impact de cette caractéristique sur la prédiction du modèle pour le client, et la couleur du point représente la valeur de cette caractéristique pour l'appartement_

La figure incorpore beaucoup d'informations précieuses (les caractéristiques sont triées par moyenne (|Tree SHAP|)). Petit avertissement : les données datent du début de 2018 ; le district peut évoluer et donc les facteurs dépendant du prix pourraient changer.

* la proximité du centre-ville (kilomètres jusqu'à U-Bahn Stadtmitte en voiture et durée d'un trajet en train jusqu'à S-Bahn Friedrichstrasse) augmente le prix de location prédit de l'appartement
* la surface totale comme facteur le plus fort du prix de location
* si le propriétaire de l'appartement exige que vous ayez un certificat de faible revenu (WBS en allemand), le prix prédit est plus bas
* louer un appartement dans ces districts augmenterait également le prix de location : Mitte, Prenzlauer Berg, Wilmersdorf, Charlottenburg, Zehlendorf et Friedrichshain.
* les districts avec des prix plus bas seraient : Spandau, Tempelhof, Wedding et Reinickendorf
* évidemment, un appartement en meilleur état — la valeur la plus basse est la meilleure — de meilleure qualité — la valeur la plus basse est meilleure — avec des meubles, une cuisine intégrée et un ascenseur coûtera plus cher

Les impacts des caractéristiques suivantes sont intéressants :

* durée jusqu'à la station de métro la plus proche
* nombre de stations dans un rayon de 1 km.

**Durée jusqu'à la station de métro la plus proche :**
Il semble que, pour certains appartements, la valeur élevée de cette caractéristique indique un prix plus élevé. La raison en est que ces appartements sont situés dans des zones résidentielles très riches en dehors de Berlin.

On peut également voir que la proximité de la station de métro a deux directions : elle diminue **et** elle augmente le prix pour certains appartements. La raison pourrait être que les appartements qui sont très proches de la station de métro souffriraient également du bruit souterrain ou des vibrations causées par les trains, mais d'autre part, ils seraient bien connectés aux transports publics. Cependant, on pourrait enquêter un peu plus sur cette caractéristique car elle montre la proximité uniquement des stations de métro les plus proches et non des stations de tramway/bus.

**Nombre de stations dans un rayon de 1 km :**
La même chose s'applique au nombre de stations dans un rayon d'un kilomètre de l'appartement. De nombreuses stations de métro autour augmenteraient généralement le prix de location. Cependant, cela avait également un effet négatif — plus de bruit.

#### Moyenne d'ensemble

Après avoir joué avec différents modèles et comparé les performances, vous pourriez simplement combiner les résultats de chaque modèle et construire un ensemble !

Le bagging est le modèle d'ensemble d'apprentissage automatique qui utilise les prédictions de plusieurs algorithmes pour calculer les prédictions finales agrégées. Il est conçu pour prévenir le surapprentissage et réduire la variance des algorithmes.

![Image](https://cdn-media-1.freecodecamp.org/images/HT9qesuH98q20J2vUusVk75hXdH3pGaevQKH)
_Avantage de l'utilisation des ensembles : Le modèle rouge performe mieux dans la boîte inférieure gauche, cependant, le modèle bleu performe mieux dans la boîte supérieure droite. En combinant les prédictions des deux modèles, cela pourrait améliorer les performances globales. Fig prise de [ici.](https://burakhimmetoglu.com/2016/12/01/stacking-models-for-improved-predictions/" rel="noopener" target="_blank" title=")_

Comme j'avais déjà des prédictions des algorithmes mentionnés ci-dessus, j'ai combiné les quatre modèles de toutes les manières possibles et j'ai choisi les sept meilleurs modèles simples et d'ensemble basés sur le RMSLE de l'ensemble de validation.

Ensuite, le RMSLE de ces sept modèles a été calculé sur l'ensemble de test.

![Image](https://cdn-media-1.freecodecamp.org/images/7-TD75VZRYezXvqABEOlTgtev6kIYzSLvtkG)
_RMSLE de test des algorithmes._

L'ensemble des trois algorithmes basés sur les arbres de décision a performé le mieux par rapport à chaque modèle simple.

Vous pourriez également produire un ensemble pondéré, attribuant plus de poids à un meilleur modèle simple. La raison derrière cela est que les autres modèles pourraient contredire le meilleur modèle seulement s'ils sont collectivement d'accord sur une alternative.

En réalité, on ne saurait jamais si un ensemble moyenné serait meilleur que le modèle simple sans simplement l'essayer.

#### Modèles empilés

Un ensemble moyenné ou pondéré n'est pas la seule façon de combiner les prédictions de différents modèles. Vous pourriez également empiler les modèles de très différentes manières !

L'idée derrière les modèles empilés est de créer plusieurs modèles de base et un méta-modèle au-dessus des résultats des modèles de base afin de produire des prédictions finales. Cependant, il n'est pas si évident comment entraîner le méta-modèle car il peut être biaisé vers le meilleur des modèles de base. Une très bonne explication de la manière de le faire correctement peut être trouvée dans le post « Stacking models for improved predictions ».

Pour le cas des prix de location, les modèles empilés n'ont pas du tout amélioré le RMSLE — ils ont même augmenté les métriques. Il pourrait y avoir plusieurs raisons à cela — soit je l'ai codé incorrectement ;) soit il y avait simplement trop de bruit introduit par l'empilement.

Si vous souhaitez explorer davantage les articles sur les ensembles et les modèles empilés, le [Guide d'ensemble Kaggle](https://mlwave.com/kaggle-ensembling-guide/) explique de nombreux types différents d'ensemble avec la comparaison de performance et les références sur la manière dont de tels modèles empilés sont arrivés en tête des compétitions de Kaggle.

### **Réflexions finales**

* écoutez ce dont parlent les gens autour de vous ; leurs plaintes peuvent servir de bon point de départ pour résoudre quelque chose de grand
* laissez les gens trouver leurs propres informations en fournissant des tableaux de bord interactifs
* ne vous limitez pas à l'ingénierie des caractéristiques courantes comme multiplier deux variables. Essayez de trouver des sources de données ou des explications supplémentaires
* essayez les ensembles et les modèles empilés car ces méthodes pourraient améliorer les performances

**Et s'il vous plaît, fournissez la date des données que vous affichez !**

Sources des figures :
[https://www.pinterest.de/minimalcouture/paris-apartments/](https://www.pinterest.de/minimalcouture/paris-apartments/)
[https://www.theodysseyonline.com/the-struggles-of-moving-into-your-first-apartment](https://www.theodysseyonline.com/the-struggles-of-moving-into-your-first-apartment)
[https://www.fashionbeans.com/content/the-worlds-10-smallest-apartments-are-downright-shocking/](https://www.fashionbeans.com/content/the-worlds-10-smallest-apartments-are-downright-shocking/)