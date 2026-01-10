---
title: Une introduction à l'IA explicable et pourquoi nous en avons besoin
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T20:38:58.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-explainable-ai-and-why-we-need-it-a326417dd000
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yT52DLV4NWUp6KFN1S2Qxg.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Future
  slug: future
- name: Machine Learning
  slug: machine-learning
- name: technology
  slug: technology
seo_title: Une introduction à l'IA explicable et pourquoi nous en avons besoin
seo_desc: 'By Patrick Ferris

  Neural networks (and all of their subtypes) are increasingly being used to build
  programs that can predict and classify in a myriad of different settings.

  Examples include machine translation using recurrent neural networks, and ima...'
---

Par Patrick Ferris

Les réseaux de neurones (et tous leurs sous-types) sont de plus en plus utilisés pour construire des programmes capables de prédire et de classer dans une multitude de contextes différents.

Les exemples incluent la [traduction automatique](https://arxiv.org/pdf/1806.08730.pdf) utilisant des réseaux de neurones récurrents, et la [classification d'images](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf) utilisant un réseau de neurones convolutionnel. Les recherches publiées par Google DeepMind ont suscité un intérêt pour l'[apprentissage par renforcement](https://arxiv.org/pdf/1312.5602.pdf).

Toutes ces approches ont fait progresser de nombreux domaines et produit des modèles utilisables qui peuvent améliorer la productivité et l'efficacité.

Cependant, **nous ne savons pas vraiment comment ils fonctionnent**.

J'ai eu la chance d'assister à la conférence [Knowledge Discovery and Data Mining](http://www.kdd.org/kdd2018/) (KDD) cette année. Parmi les conférences auxquelles j'ai assisté, il y avait deux principaux domaines de recherche qui semblent préoccuper beaucoup de monde :

* Tout d'abord, trouver une représentation significative des structures de graphes à alimenter dans les réseaux de neurones. [Oriol Vinyals](https://ai.google/research/people/OriolVinyals) de DeepMind a donné une conférence sur leurs [Message Passing Neural Networks](https://arxiv.org/pdf/1704.01212.pdf).
* Le deuxième domaine, et le sujet de cet article, concerne les modèles d'IA explicables. Alors que nous générons des applications neuves et plus innovantes pour les réseaux de neurones, la question de « Comment fonctionnent-ils ? » devient de plus en plus importante.

#### Pourquoi le besoin de modèles explicables ?

Les réseaux de neurones ne sont pas infaillibles.

Outre les problèmes de surapprentissage et de sous-apprentissage pour lesquels nous avons développé de nombreux outils (comme le Dropout ou l'augmentation de la taille des données) pour les contrer, les réseaux de neurones fonctionnent de manière opaque.

Nous ne savons pas vraiment pourquoi ils prennent les décisions qu'ils prennent. À mesure que les modèles deviennent plus complexes, la tâche de produire une version interprétable du modèle devient plus difficile.

Prenons, par exemple, l'[attaque par un pixel](https://arxiv.org/pdf/1710.08864.pdf) (voir ici pour une excellente [vidéo](https://www.youtube.com/watch?v=SA4YEAWVpbk) sur l'article). Cela est réalisé en utilisant une approche sophistiquée qui analyse les CNNs et applique l'évolution différentielle (un membre de la classe évolutive des algorithmes).

Contrairement à d'autres stratégies d'optimisation qui restreignent la fonction objectif à être différentiable, cette approche utilise un algorithme évolutif itératif pour produire de meilleures solutions. Plus précisément, pour cette attaque par un pixel, les seules informations requises étaient les probabilités des étiquettes de classe.

![Image](https://cdn-media-1.freecodecamp.org/images/xh9yxzzOW8B7zibKo1JbjkaWOacnxx8mK0kl)
_De [One pixel attack for fooling deep neural networks](https://arxiv.org/pdf/1710.08864.pdf" rel="noopener" target="_blank" title=") par Jiawei Su et al._

La facilité relative à tromper ces réseaux de neurones est inquiétante. Au-delà de cela se pose un problème plus systémique : faire confiance à un réseau de neurones.

Le meilleur exemple de cela se trouve dans le domaine médical. Supposons que vous construisez un réseau de neurones (ou tout modèle de boîte noire) pour aider à prédire les maladies cardiaques à partir des dossiers d'un patient.

Lorsque vous entraînez et testez votre modèle, vous obtenez une bonne précision et une valeur prédictive positive convaincante. Vous le présentez à un clinicien et ils conviennent qu'il semble être un modèle puissant.

Mais ils hésiteront à l'utiliser parce que vous (ou le modèle) ne pouvez pas répondre à la simple question : « Pourquoi avez-vous prédit que cette personne est plus susceptible de développer une maladie cardiaque ? »

Ce manque de transparence est un problème pour le clinicien qui veut comprendre le fonctionnement du modèle pour l'aider à améliorer son service. C'est aussi un problème pour le patient qui veut une raison concrète pour cette prédiction.

Éthiquement, est-il juste de dire à un patient qu'il a une probabilité plus élevée d'avoir une maladie si votre seule raison est que « la boîte noire me l'a dit » ? Les soins de santé sont autant une question de science que d'empathie pour le patient.

Le domaine de l'IA explicable a connu une croissance ces dernières années, et cette tendance semble destinée à se poursuivre.

Ce qui suit sont quelques-unes des avenues intéressantes et innovantes que les chercheurs et les experts en apprentissage automatique explorent dans leur quête de modèles qui non seulement performant bien, mais peuvent aussi vous dire pourquoi ils prennent les décisions qu'ils prennent.

#### Modèle d'Attention Inversée dans le Temps (RETAIN)

Le modèle RETAIN a été développé à l'Institut de Technologie de Géorgie par [Edward Choi et al.](https://arxiv.org/pdf/1608.05745.pdf). Il a été introduit pour aider les médecins à comprendre pourquoi un modèle prédisait que des patients étaient à risque d'insuffisance cardiaque.

![Image](https://cdn-media-1.freecodecamp.org/images/ezTATi55cPwwF3y4ntYTSiqV0JudbaOVVowa)
_Le modèle de réseau de neurones récurrents RETAIN utilise des mécanismes d'attention pour améliorer l'interprétabilité_

L'idée est, étant donné les dossiers des visites à l'hôpital d'un patient qui contiennent également les événements de la visite, ils pourraient prédire le risque d'insuffisance cardiaque.

Les chercheurs ont divisé l'entrée en deux réseaux de neurones récurrents. Cela leur a permis d'utiliser le [mécanisme d'attention](http://www.wildml.com/2016/01/attention-and-memory-in-deep-learning-and-nlp/) sur chacun pour comprendre sur quoi le réseau de neurones se concentrait.

Une fois entraîné, le modèle pouvait prédire le risque d'un patient. Mais il pouvait également utiliser les paramètres alpha et bêta pour indiquer quelles visites à l'hôpital (et quels événements au cours d'une visite) avaient influencé son choix.

#### Explications Locales Interprétables et Agnostiques aux Modèles (LIME)

Une autre approche qui est devenue assez courante est [LIME](https://arxiv.org/pdf/1602.04938.pdf).

Il s'agit d'un modèle post-hoc — il fournit une explication d'une décision après qu'elle ait été prise. Cela signifie qu'il n'est pas un modèle transparent de type « boîte de verre » (comme les arbres de décision) du début à la fin.

L'un des principaux atouts de cette approche est qu'elle est agnostique aux modèles. Elle peut être appliquée à n'importe quel modèle afin de produire des explications pour ses prédictions.

Le concept clé sous-jacent à cette approche est la perturbation des entrées et l'observation de la manière dont cela affecte les sorties du modèle. Cela nous permet de construire une image des entrées sur lesquelles le modèle se concentre et qu'il utilise pour faire ses prédictions.

Par exemple, imaginez un type de CNN pour la classification d'images. Il y a quatre étapes principales pour utiliser le modèle LIME afin de produire une explication :

* Commencez avec une image normale et utilisez le modèle de boîte noire pour produire une distribution de probabilité sur les classes.
* Ensuite, perturbez l'entrée d'une certaine manière. Pour les images, cela pourrait être masquer des pixels en les colorant en gris. Passez maintenant ces images à travers le modèle de boîte noire pour voir comment les probabilités pour la classe qu'il a initialement prédite ont changé.
* Utilisez un modèle interprétable (généralement linéaire) comme un arbre de décision sur cet ensemble de données de perturbations et de probabilités pour extraire les caractéristiques clés qui expliquent les changements. Le modèle est pondéré localement — ce qui signifie que nous nous soucions davantage des perturbations qui sont les plus similaires à l'image originale que nous utilisions.
* Sortez les caractéristiques (dans notre cas, les pixels) avec les plus grands poids comme notre explication.

#### Propagation de Pertinence par Couche (LRP)

Cette [approche](https://arxiv.org/pdf/1604.00825.pdf) utilise l'idée de redistribution et de conservation de la pertinence.

Nous commençons avec une entrée (par exemple, une image) et sa probabilité de classification. Ensuite, nous travaillons à rebours pour redistribuer cela à toutes les entrées (dans ce cas, les pixels).

Le processus de redistribution est assez simple d'une couche à l'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/f5l2bqv5EmPztk1i0dyRMBRdj1AK5HdPMNX8)
_Ne vous effrayez pas — cette équation pondère simplement les pertinences en fonction de l'activation des neurones et de la connexion des poids_

Dans l'équation ci-dessus, chaque terme représente les idées suivantes :

* `x_j` — la valeur d'activation pour le neurone _j_ dans la couche _l_
* `w_j,k` — la pondération de la connexion entre le neurone _j_ dans la couche _l_ et le neurone _k_ dans la couche _l + 1_
* `R_j` — Scores de pertinence pour chaque neurone dans la couche _l_
* `R_k` — Scores de pertinence pour chaque neurone dans la couche _l+1_

L'epsilon est simplement une petite valeur pour éviter de diviser par zéro.

Comme vous pouvez le voir, nous pouvons travailler à rebours pour déterminer la pertinence des entrées individuelles. De plus, nous pouvons les trier par ordre de pertinence. Cela nous permet d'extraire un sous-ensemble significatif d'entrées comme les plus utiles ou les plus puissantes pour faire une prédiction.

#### Et ensuite ?

Les méthodes ci-dessus pour produire des modèles explicables ne sont en aucun cas exhaustives. Elles représentent un échantillon de certaines des approches que les chercheurs ont essayées pour produire des prédictions interprétables à partir de modèles de boîte noire.

Espérons que cet article éclaire également pourquoi il s'agit d'un domaine de recherche si important. Nous devons continuer à rechercher ces méthodes et en développer de nouvelles, afin que l'apprentissage automatique puisse bénéficier à autant de domaines que possible — de manière sûre et fiable.

Si vous souhaitez plus d'articles et de domaines à lire, essayez quelques-uns des éléments suivants.

* Les recherches de [DeepMind](http://proceedings.mlr.press/v80/kim18d/kim18d.pdf) sur les vecteurs d'activation de concepts, ainsi que les [diapositives](http://s.interpretable.ml/nips_interpretable_ml_2017_victoria_Krakovna.pdf) de la conférence de Victoria Krakovna à la conférence Neural Information Processing Systems (NIPS).
* Un [article](https://arxiv.org/pdf/1711.07373.pdf) de Dung Huk Park et al. sur les ensembles de données pour mesurer les modèles explicables.
* L'[article](https://arxiv.org/pdf/1702.08608.pdf) de [Finale Doshi-Velez](https://www.seas.harvard.edu/directory/finale) et [Been Kim](https://beenkim.github.io/) sur le domaine en général

L'intelligence artificielle ne devrait pas devenir une divinité puissante que nous suivons aveuglément. Mais nous ne devrions pas non plus l'oublier et les perspectives bénéfiques qu'elle peut offrir. Idéalement, nous construirons des modèles flexibles et interprétables qui pourront travailler en collaboration avec des experts et leurs connaissances domainiales pour offrir un avenir plus radieux à tous.