---
title: Comment nous avons transformé l'LDA non supervisée en GuidedLDA semi-supervisée
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-16T07:11:00.000Z'
originalURL: https://freecodecamp.org/news/how-we-changed-unsupervised-lda-to-semi-supervised-guidedlda-e36a95f3a164
coverImage: https://cdn-media-1.freecodecamp.org/images/1*34tkrlrhSOdsBZy0ZRr6ow.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment nous avons transformé l'LDA non supervisée en GuidedLDA semi-supervisée
seo_desc: 'By Vikash Singh

  This is the story of how and why we had to write our own form of Latent Dirichlet
  Allocation (LDA). I also talk about why we needed to build a Guided Topic Model
  (GuidedLDA), and the process of open sourcing everything on GitHub.

  What...'
---

Par Vikash Singh

Ceci est l'histoire de comment et pourquoi nous avons dû écrire notre propre forme d'[Allocation de Dirichlet latente](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) (LDA). Je parle également de la raison pour laquelle nous avons dû construire un modèle de sujet guidé (GuidedLDA), et du processus de mise en open source de l'ensemble sur [GitHub](https://github.com/vi3k6i5/guidedlda).

### **Qu'est-ce que l'LDA (Modélisation thématique) ?**

Supposons que vous ayez un ensemble d'articles de presse qui sont des documents. En lisant ces articles, vous serez en mesure de dire s'ils traitent de Sport, de Politique ou de Science.

Pour les titres suivants, vous conviendrez que 1 et 5 concernent la Politique, 2 et 4 le Sport, et 3 et 6 la Science :

![Image](https://cdn-media-1.freecodecamp.org/images/1*lhiPVM0SmNA6lLoXkoKyXA.png)
_Exemples de titres d'articles de presse._

Pour un être humain, ce n'est pas un défi de déterminer à quel thème appartient un article de presse. Mais comment pouvons-nous apprendre à un ordinateur à comprendre ces mêmes thèmes ?

C'est là que la modélisation thématique entre en jeu. La modélisation thématique est une classe non supervisée d'algorithmes d'apprentissage automatique (Machine Learning). Ces modèles sont généralement doués pour regrouper des mots en thèmes. L'LDA est [la technique de modélisation thématique la plus populaire](https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GOmQ7gnPDib0FW1yaniyDg.png)
_Mots regroupés pour former des thèmes_

Une fois que nous avons regroupé les mots en thèmes, nous pouvons maintenant voir de quel groupe de mots traitent les articles de presse et les documents. Ensuite, nous pouvons les classer dans ce groupe ou ce thème.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sOrYD13DKo3mUciTUy6LSQ.png)
_classer de nouveaux documents sur la base de mots précédemment classés._

Comme nous pouvons le voir, ce nouvel article de presse parle du **Prix Nobel**. Nous pouvons maintenant prédire que ce document traite du thème de la **Science**.

**Note** : Les mots ne sont pas regroupés directement en thèmes. On calcule plutôt une probabilité telle que « Quelle est la probabilité qu'un mot appartienne à un thème ? ».

Elle est donnée par **_p(t|w)_**, soit la probabilité du thème **_t_** étant donné le mot **_w_**. À la base, il s'agit simplement de [probabilité bayésienne](https://en.wikipedia.org/wiki/Bayesian_probability).

J'aimerais en parler davantage, mais je ne veux pas m'écarter du problème central. Si vous êtes intéressé, vous pouvez en lire plus à ce sujet [ici](https://tedunderwood.com/2012/04/07/topic-modeling-made-just-simple-enough/).

### **Alors, qu'est-ce que Guided LDA ?**

La modélisation thématique est généralement un algorithme d'apprentissage non supervisé. Nous savons que l'**Espace** et la **Technologie** sont des thèmes à part entière. Mais si nous ne recevons pas beaucoup d'articles à leur sujet ou s'ils sont mentionnés ensemble, ils pourraient être classés dans un seul thème.

J'ai rencontré un problème similaire récemment. Je travaille en tant que Data Scientist chez [Belong.co](https://medium.com/u/559d189d881) et le Traitement du Langage Naturel (NLP) représente la moitié de mon travail. Récemment, j'effectuais une modélisation thématique LDA sur notre corpus de données. La plupart des thèmes sont ressortis comme je m'y attendais. Mais certains thèmes n'avaient pas de sens.

Certains thèmes se chevauchaient et certains thèmes que je m'attendais à voir n'étaient pas là. Quelque chose de ce genre s'est produit : l'Espace et la Technologie ont fusionné.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U2bi875Rn80MUrBEyriO9g.png)
_L'Espace et la Technologie fusionnent_

Dans un algorithme d'apprentissage supervisé, vous pouvez revenir en arrière et déboguer l'endroit où vous vous êtes trompé dans le processus de prise de décision. Peut-être aviez-vous besoin de plus de caractéristiques (features). Ou de plus de données d'entraînement. Ou peut-être d'une meilleure fonction de perte, de meilleures métriques et d'un meilleur échantillonnage.

Mais par où commencer quand le modèle est non supervisé ? Nous avons décidé de déboguer…

![Image](https://cdn-media-1.freecodecamp.org/images/1*YXVr2zDo76OOBXKDnMlCPg.jpeg)
_Ce moment de l'histoire où nous avons décidé de déboguer l'LDA…_

Nous avons constaté que les thèmes qui se mélangeaient n'avaient pas assez de documents pour se démarquer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*L-IBXL6JlRu6ZYTmCVaEUA.png)
_Les thèmes Espace et Technologie fusionnent._

Nous avons décidé de dire au modèle de garder l'Espace et la Technologie séparés. L'idée était de définir quelques mots graines (seed words) pour l'Espace et quelques mots graines pour la Technologie. Ensuite, guider le modèle pour qu'il converge autour de ces termes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*x-LyhAlx0KczZ04t4ski4g.png)
_Mots graines définis pour les identifiants de thèmes_

C'était une idée simple et intuitive, mais nous n'avons trouvé aucune implémentation de GuidedLDA. Il y avait très peu d'articles de recherche qui parlaient de guider l'LDA.

Nous nous sommes référés à l'article de Jagadeesh Jagarlamudi, Hal Daume III et Raghavendra Udupa [Incorporating Lexical Priors into Topic Models](http://www.umiacs.umd.edu/~jags/pdfs/GuidedLDA.pdf). L'article explique comment les priors (dans ce cas, les **priors** signifient les mots graines) peuvent être définis dans le modèle pour le guider dans une certaine direction. Nous entrerons dans les détails dans un instant.

Une fois ces changements effectués, le modèle a convergé de la manière que nous souhaitions.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2t3R1uKBwdfpACttEOt0Bw.png)
_Les thèmes Espace et Technologie sont séparés après avoir semé les thèmes._

### **Alors, comment avons-nous transformé l'LDA en GuidedLDA ?**

Pour expliquer cette partie, nous devrons entrer dans les détails du fonctionnement de l'LDA. Je ferai de mon mieux pour rester simple. Si vous ne voulez pas entrer dans les détails, vous pouvez passer directement à la section **Utiliser GuidedLDA**.

Le fonctionnement de l'LDA classique est le suivant : d'abord, chaque mot est assigné de manière aléatoire à un thème. Cette initialisation peut être contrôlée avec des priors de Dirichlet via le paramètre Alpha. C'est de là que l'LDA (Allocation de Dirichlet latente) tire son nom. Ce caractère aléatoire peut être une initialisation uniforme si l'alpha est grand, ou une initialisation asymétrique lorsque l'alpha est petit. Continuons avec l'initialisation uniforme pour le moment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RojQi7m5yBGHSD0Q0HGGYg.png)
_Initialisation par défaut avec une distribution uniforme des mots par thèmes._

L'étape suivante consiste à découvrir quel terme appartient à quel thème. C'est la partie modélisation thématique de l'algorithme. L'LDA adopte une approche très simple en trouvant le thème d'un terme à la fois.

Supposons que vous vouliez trouver un thème pour le terme **Blue Origin**. L'LDA supposera d'abord que tous les autres termes du corpus sont assignés au bon thème. À l'étape précédente, nous avions distribué uniformément chaque terme dans tous les thèmes, nous supposerons donc que c'est le bon thème pour ces termes.

Ensuite, nous calculons avec quels termes **Blue Origin** apparaît fréquemment. Ensuite, quel est le thème le plus courant parmi ces termes. Nous assignerons **Blue Origin** à ce thème.

**Blue Origin** se rapprochera probablement du thème dans lequel se trouvent **SpaceX** et **NASA**. Maintenant, vous pouvez voir que **NASA**, **SpaceX** et **Blue Origin** sont un peu plus proches les uns des autres qu'ils ne l'étaient avant cette étape. Ensuite, nous passerons au terme suivant et répéterons le processus. Nous répéterons l'ensemble de ce processus le nombre de fois nécessaire pour que le modèle converge.

La formule pour cela sera :  
La `Probabilité` que **_Blue Origin_** s'insère dans le thème `Z` {0,1,2,..} lorsqu'il apparaît dans un `document` est égale au nombre de fois où **_Blue Origin_** est assigné au thème `Z` multiplié par le nombre d'autres `mots` de ce document qui appartiennent déjà à `Z`, divisé par le nombre total de fois où n'importe quel mot est assigné au thème `Z`.

Voici la formule réelle :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zbQ4v-jKMG0e5e5KeKtUnQ.png)

Pour chaque document **(`D`)** et pour chaque mot **(`W`)** de ce document, nous calculerons la probabilité que ce mot appartienne à chaque thème **(`Z`)**.

```
for d in all_documents_D:    for w in all_words_W_in_d:        for z in all_topics_Z:            w_in_z = count(à travers tous les documents où w appartient à z)            d_in_z = count(dans d tous les mots qui appartiennent à z)            tokens_in_z = count(toutes les affectations dans z)            p(z| w, d) = w_in_z * d_in_z / tokens_in_z        # donc w appartient au p(z) maximum        # quel que soit le thème pour lequel la probabilité était maximale pour w        w_z = max(p(z| w, d))
```

Les résultats initiaux seront erronés. Mais nous lancerons l'ensemble de ce processus plusieurs fois et, à chaque itération, ils s'amélioreront. Au fil du temps, ils convergeront pour former la distribution des mots par thèmes.

### **Qu'est-ce qui change quand on sème des documents ?**

Supposons que nous voulions semer `**SpaceX**`, `**NASA**` pour converger vers le `**topic_0**`. Lors de l'initialisation, nous pouvons donner un coup de pouce supplémentaire à `**SpaceX**` et `**NASA**` pour qu'ils se situent dans ce thème spécifique.

Nous pouvons contrôler ce paramètre de l'ampleur du coup de pouce supplémentaire à donner à un terme. Dans notre algorithme, nous l'appelons `**seed_confidence**` et il peut varier entre 0 et 1. Avec une `**seed_confidence**` de 0,1, vous pouvez biaiser les mots graines de 10 % de plus vers les thèmes grainés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kMxQ47DFkpxIDBCyXeff6w.png)
_Initialisation par graines avec une distribution modifiée des mots par thèmes._

Dans l'initialisation illustrée ci-dessus, `**NASA**` et `**SpaceX**` sont grainés pour le `**Topic_0**`, `**Apple**` et `**Google**` pour le `**Topic_1**`, et `**Physics**` (Physique) et `**Chemistry**` (Chimie) pour le `**Topic_2**`.

Désormais, lorsque nous lancerons le processus ci-dessus, nous aurons un décompte plus élevé pour les mots graines appartenant aux thèmes grainés. La formule restera la même pour GuidedLDA et la convergence se modifiera vers les thèmes grainés.

```
# pour les mots graines appartenant aux thèmes graines# ce décompte sera désormais plus élevé pour le z grainé.
```

```
w_in_z = count(à travers tous les documents où w appartient à z)
```

```
# Ainsi, la probabilité que p appartienne au z grainé sera plus élevée
```

```
p(z| w, d) ∝ w_in_z
```

Hence guiding the LDA. Or GuidedLDA.

Nous avons essayé de nombreuses approches différentes avant de finalement faire fonctionner celle-ci.

### Utiliser GuidedLDA

GuidedLDA est une bibliothèque Python que j'ai passée en open source sur ce [répertoire GitHub](https://github.com/vi3k6i5/guidedlda).

Vous pouvez l'installer avec un simple pip install :

```
pip install guidedlda
```

Le code pour l'utiliser est assez simple. Créez un dictionnaire pour `seed_topics` avec une correspondance `word_id` vers `topic_id`. Et passez-le à la méthode `model.fit()`.

1. `seed_confidence` peut varier entre 0 et 1.
2. `seed_topics` est le dictionnaire {`word_id` vers `topic_id`}
3. `X` est la [matrice document-terme](https://en.wikipedia.org/wiki/Document-term_matrix).

```
seed_topics = {    'NASA': 0, 'SpaceX': 0,    'Apple': 1, 'Google': 1,    'Physics': 2, 'Chemistry': 2,}model.fit(X, seed_topics=seed_topics, seed_confidence=0.15).
```

La documentation de GuidedLDA est liée [ici](http://guidedlda.readthedocs.io/).

#### Crédits

Une grande partie du code est empruntée à la [bibliothèque LDA de python](https://github.com/lda-project/lda).

Un grand merci aux auteurs de cette bibliothèque : [Allen Riddell](https://twitter.com/ariddell) et [Tim Hopper](https://twitter.com/tdhopper).

Un merci spécial à [Vinodh Ravindranath](https://www.linkedin.com/in/vinodhkumarr/), qui m'a mentoré tout au long du projet.

En utilisant GuidedLDA, nous avons pu séparer les thèmes qui avaient une plus faible représentation dans le corpus et guider la classification des documents.

Nous avons rencontré du succès avec ce modèle en production. Mais l'algorithme et l'implémentation n'en sont encore qu'à un stade précoce. Nous vous invitons à l'essayer et à partager vos réflexions, vos expériences et vos résultats. Nous serions ravis d'avoir votre avis.