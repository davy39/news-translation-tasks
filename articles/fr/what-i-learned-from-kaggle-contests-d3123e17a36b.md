---
title: Ce que j'ai appris en participant à des concours de machine learning sur Kaggle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-08T13:07:40.000Z'
originalURL: https://freecodecamp.org/news/what-i-learned-from-kaggle-contests-d3123e17a36b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0mOv-6h9-5oM_BAoWpjAnw.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Ce que j'ai appris en participant à des concours de machine learning sur
  Kaggle
seo_desc: 'By Parminder Singh

  Recently I decided to get more serious about my data science skills. So I decided
  to practice my skills, which led me to Kaggle.

  The experience has been very positive.

  When I arrived at Kaggle, I was confused about what to do and h...'
---

Par Parminder Singh

Récemment, j'ai décidé de prendre mes compétences en science des données plus au sérieux. J'ai donc décidé de pratiquer mes compétences, ce qui m'a conduit à [Kaggle](http://kaggle.com).

L'expérience a été très positive.

Quand je suis arrivé sur Kaggle, j'étais confus quant à ce qu'il fallait faire et comment tout fonctionnait. Cet article vous aidera à surmonter la confusion que j'ai ressentie.

J'ai rejoint le concours [Redefining Cancer Treatment](https://www.kaggle.com/c/msk-redefining-cancer-treatment) parce que c'était pour une noble cause. De plus, les données étaient plus faciles à gérer car elles étaient basées sur du texte.

### Où coder

Ce qui rend Kaggle génial, c'est que vous n'avez pas besoin d'un serveur cloud qui génère des résultats pour vous. Kaggle dispose d'une fonctionnalité où vous pouvez exécuter des scripts et des notebooks directement sur Kaggle gratuitement, tant qu'ils finissent de s'exécuter en moins d'une heure. J'ai utilisé les notebooks de Kaggle pour beaucoup de mes soumissions et j'ai expérimenté avec de nombreuses variables.

Dans l'ensemble, ce fut une excellente expérience.

![Image](https://cdn-media-1.freecodecamp.org/images/LKwWbZdU1qEaGJU-ux9GzXCo7-Zq18SfuBZH)
_Ce nouveau bouton Kernels est votre ami !_

Pour les concours, vous devez utiliser des images ou avoir un grand corpus de texte. Et vous aurez besoin d'un ordinateur personnel (PC) rapide ou d'un conteneur cloud. Mon PC est médiocre, donc j'ai utilisé l'instance c4.2xlarge d'Amazon Web Services (AWS). Elle était suffisamment puissante pour le texte et coûtait seulement 0,40 $ par heure. J'avais également un crédit gratuit de 150 $ du pack développeur étudiant GitHub, donc je n'ai pas eu à me soucier du coût.

Plus tard, lorsque j'ai participé au concours [Dog Breed Identification](https://www.kaggle.com/c/dog-breed-identification), j'ai beaucoup travaillé avec des images, donc j'ai dû mettre à niveau mon instance vers g2.2xlarge. Cela coûtait 0,65 $ par heure, mais elle avait une puissance de traitement graphique (GPU), donc elle pouvait calculer des milliers d'images en quelques minutes seulement.

L'instance g2.2xlarge n'était toujours pas assez grande pour contenir toutes les données avec lesquelles je travaillais, donc j'ai mis en cache les données intermédiaires sous forme de fichiers et j'ai supprimé les données de la RAM. J'ai fait cela en utilisant `del <nom_variable>` pour éviter les erreurs `ResourceExhaustionError` ou `MemoryError`. Les deux étaient tout aussi décourageantes.

### Comment commencer avec les compétitions Kaggle

Ce n'est pas aussi effrayant que cela en a l'air. Les onglets Discussion et Kernel pour chaque concours sont une excellente façon de commencer. Quelques jours après le début d'un concours, vous verrez plusieurs kernels de démarrage apparaître dans l'onglet Kernel. Vous pouvez les utiliser pour commencer.

Au lieu de gérer le chargement et la création de soumissions, concentrez-vous simplement sur la manipulation des données. Je préfère les kernels de démarrage XGBoost. Leurs codes sont toujours courts et bien classés sur les tableaux de classement.

[Extreme Gradient Boosting](http://xgboost.readthedocs.io/en/latest/) (XGBoost) est basé sur le [modèle d'arbre de décision](https://en.wikipedia.org/wiki/Decision_tree_learning). Il est très rapide et incroyablement précis, même avec les variables par défaut. Pour les grandes données, je préfère utiliser [Light Gradient Boosting Machine](http://lightgbm.readthedocs.io/en/latest/) (LightGBM). Il est similaire en concept à XGBoost, mais aborde le problème un peu différemment. Il y a un hic, il n'est pas aussi précis. Vous pouvez donc expérimenter avec LightGBM, et lorsque vous savez qu'il fonctionne bien, passer à XGBoost (ils ont une API similaire).

Vérifiez les discussions tous les quelques jours pour voir si quelqu'un a trouvé une nouvelle approche. Si quelqu'un le fait, utilisez-la dans votre script et testez pour voir si vous en bénéficiez.

### **Comment monter dans le classement**

Donc, vous avez votre code de démarrage prêt et vous voulez monter plus haut ? Il y a plusieurs approches possibles :

* **Validation croisée (CV) :** Divisez toujours les données d'entraînement en 80 % et 20 %. Ainsi, lorsque vous entraînez sur 80 % des données, vous pouvez vérifier manuellement avec 20 % des données pour voir si vous avez un bon modèle. Pour citer le tableau de discussion sur Kaggle, « Faites toujours plus confiance à votre CV qu'au tableau de classement. » Le tableau de classement contient 50 % à 70 % de l'ensemble de test réel, donc vous ne pouvez pas être sûr de la qualité de votre solution en fonction des pourcentages. Parfois, votre modèle peut être excellent dans l'ensemble, mais mauvais sur les données, spécifiquement dans l'ensemble de test public.
* **Mettez en cache vos données intermédiaires :** Vous ferez moins de travail la prochaine fois en faisant cela. Concentrez-vous sur une étape spécifique plutôt que de tout exécuter depuis le début. Presque tous les objets Python peuvent être `picklés`, mais pour l'efficacité, utilisez toujours les fonctions `.save()` et `.load()` de la bibliothèque que vous utilisez pour votre code.
* **Utilisez [GridSearchCV](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) :** C'est un excellent module qui vous permet de fournir un ensemble de valeurs de variables. Il essaiera toutes les combinaisons possibles jusqu'à ce qu'il trouve l'ensemble optimal de valeurs. C'est une excellente automatisation pour l'optimisation. Un XGBoost finement réglé peut battre un réseau de neurones générique dans de nombreux problèmes.
* **Utilisez le modèle approprié au problème :** Utiliser un couteau dans un combat à l'arme à feu n'est pas une bonne idée. J'ai une approche simple : Pour les données textuelles, utilisez XGBoost ou Keras LSTM. Pour les données d'image, utilisez un modèle Keras pré-entraîné (j'utilise [Inception](https://keras.io/applications/#inceptionv3) la plupart du temps) avec quelques couches de goulot d'étranglement personnalisées.
* **Combinez les modèles :** Utiliser un couteau de cuisine pour tout n'est pas suffisant. Vous avez besoin d'un couteau suisse. Essayez de combiner divers modèles pour obtenir des informations encore plus précises. Par exemple, Inception plus le modèle [Xception](https://arxiv.org/abs/1610.02357) fonctionnent très bien pour les données d'image. Les modèles combinés prennent beaucoup de RAM, que g2.2xlarge pourrait ne pas fournir. Évitez-les donc, sauf si vous voulez vraiment obtenir ce gain de précision.
* **Extraction de caractéristiques :** Facilitez le travail du modèle en extrayant plusieurs caractéristiques plus simples à partir d'une seule caractéristique, ou en combinant plusieurs caractéristiques en une seule. Par exemple, vous pouvez extraire le pays et l'indicatif régional d'un numéro de téléphone. Les modèles ne sont pas très intelligents, ce sont simplement des algorithmes qui ajustent les données. Assurez-vous donc que les données sont appropriées pour un ajustement optimal.

### Que faire d'autre sur Kaggle

En plus d'être une plateforme de compétition pour la science des données, Kaggle est également une plateforme pour explorer des ensembles de données et créer des kernels qui explorent les insights des données.

Vous pouvez donc choisir n'importe quel ensemble de données parmi les cinq premiers qui apparaissent sur la [page des ensembles de données](https://www.kaggle.com/datasets), et simplement vous lancer. Les données peuvent être étranges, et vous pourriez rencontrer des difficultés en tant que débutant. Ce qui compte, c'est que vous analysiez les données et que vous créiez des visualisations en rapport avec elles, ce qui contribue à votre apprentissage.

### Quelles bibliothèques utiliser pour l'analyse

Pour les **visualisations**, explorez les bibliothèques [seaborn](https://seaborn.pydata.org/) et [matplotlib](https://matplotlib.org/)
Pour la **manipulation des données**, explorez [NumPy](http://www.numpy.org/) et [_pandas_](http://pandas.pydata.org/)
Pour le **prétraitement des données**, explorez le module [sklearn.preprocessing](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)

La bibliothèque Pandas dispose également de certaines fonctions de traçage de base, et elles sont extrêmement pratiques.
`intel_sorted["Instruction_Set"].value_counts().plot(kind='pie')`

La ligne de code ci-dessus a créé un diagramme circulaire avec "Instruction_Set". Et le meilleur, c'est qu'il a toujours l'air joli.

![Image](https://cdn-media-1.freecodecamp.org/images/0sILkGqo-po80Uk-3muh41Ggi5vvGc9tFWRD)
_Ce diagramme circulaire montre qu'Intel a beaucoup de processeurs 64 bits_

### Pourquoi faire tout cela

Le machine learning est un domaine magnifique avec beaucoup de développements en cours. Participer à ces concours vous aidera à apprendre beaucoup sur les algorithmes et les diverses approches des données. J'ai moi-même appris beaucoup de ces choses grâce à Kaggle.

De plus, pouvoir dire : « Mon IA est dans le top 15 % pour <insérer le nom du concours ici> » est assez génial.

### Quelques extras de mon parcours

![Image](https://cdn-media-1.freecodecamp.org/images/SeATHycaIT8wAlT0Dj4Qm14dS-rmmV6PkBrt)
_Cette fois où j'étais dans le top 5... au moins pendant quelques heures :P_

Le graphique ci-dessous représente l'exploration de mon kernel du [jeu de données Intel CPU](https://www.kaggle.com/trion129/intel-cpus-eda) sur Kaggle :

![Image](https://cdn-media-1.freecodecamp.org/images/Og1FUz8erIZODhjpEPpDbJwAIOUJSYSfhGMz)
_Un graphique montrant l'épaisseur décroissante d'une puce_

Ma solution pour le concours [Redefining Cancer Treatment](https://www.kaggle.com/trion129/lightgbm-version) :

![Image](https://cdn-media-1.freecodecamp.org/images/RorDPJ1xR6eUi39aqz8pp28bmu6605EqrP77)
_Je me suis classé 217e dans le concours._

C'est tout pour aujourd'hui.

Merci d'avoir lu. J'espère vous avoir rendu plus confiant quant à la participation aux concours de Kaggle.

À bientôt sur les tableaux de classement.