---
title: Comment prédire les likes et les partages basés sur le titre de votre article
  en utilisant le Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-21T22:24:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-predict-likes-and-shares-based-on-your-articles-title-using-machine-learning-47f98f0612ea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gQRQ6x29YFA_ngSpaoDCUw.png
tags:
- name: data scientist
  slug: data-scientist
- name: Machine Learning
  slug: machine-learning
- name: social media
  slug: social-media
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment prédire les likes et les partages basés sur le titre de votre article
  en utilisant le Machine Learning
seo_desc: 'By Flavio H. Freitas

  Choosing a good title for an article is an important step in the writing process.
  The more interesting the title seems, the higher the chance a reader will interact
  with the whole thing. Furthermore, showing the user content they...'
---

Par Flavio H. Freitas

Choisir un bon titre pour un article est une étape importante dans le processus d'écriture. Plus le titre semble intéressant, plus la chance qu'un lecteur interagisse avec l'ensemble est élevée. De plus, montrer à l'utilisateur du contenu qu'il préfère (avec lequel interagir) augmente la satisfaction de l'utilisateur.

C'est ainsi que mon projet final de la spécialisation [Machine Learning Engineer Nanodegree](https://udacity.com/course/machine-learning-engineer-nanodegree--nd009) a commencé. Je viens de le terminer, et je me sens _si fier et heureux_ 😊 que je voulais partager avec vous quelques idées que j'ai eues sur l'ensemble du processus. De plus, j'avais promis à Q[uincy Larson](https://medium.com/@quincylarson) cet article lorsque j'ai terminé le projet.

Si vous voulez voir le document technique final [cliquez ici](https://github.com/flaviohenriquecbc/machine-learning-capstone-project/blob/master/final-report.pdf). Si vous voulez l'implémentation du code, consultez-la [ici](https://github.com/flaviohenriquecbc/machine-learning-capstone-project/blob/master/title-success-prediction.ipynb) ou fork mon projet sur [GitHub](https://github.com/flaviohenriquecbc/machine-learning-capstone-project). Si vous voulez simplement un aperçu en termes profanes, vous êtes au bon endroit — continuez à lire cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gQRQ6x29YFA_ngSpaoDCUw.png)
_Publication FreeCodeCamp Medium sur Twitter_

Certaines des plateformes les plus utilisées pour diffuser des idées de nos jours sont Twitter et Medium (vous êtes ici !). Sur Twitter, les articles sont normalement publiés en incluant des URLs externes et le titre, où les utilisateurs peuvent accéder à l'article et démontrer leur satisfaction avec un like ou un retweet du post original.

Medium montre le texte complet avec des tags (pour classer l'article) et des applaudissements (similaires aux likes de Twitter) pour montrer à quel point les utilisateurs apprécient le contenu. _Une corrélation entre ces deux plateformes peut nous apporter des informations précieuses._

### Le projet

Le problème que j'ai défini était une tâche de classification utilisant l'apprentissage supervisé : _Prédire le nombre de likes et de retweets qu'un article reçoit en fonction du titre._

Corréler le nombre de likes et de retweets de Twitter avec un article Medium est une tentative d'isoler l'effet du nombre de lecteurs atteints et du nombre d'applaudissements Medium. Parce que plus l'article est partagé sur différentes plateformes, plus il atteindra de lecteurs et plus il recevra (probablement) d'applaudissements Medium.

En utilisant uniquement les statistiques de Twitter, nous nous attendrions à ce que les articles atteignent initialement presque le même nombre de lecteurs (ces lecteurs étant les abonnés du compte freeCodeCamp sur Twitter). Leurs performances et interactions seraient donc limitées aux caractéristiques du tweet — par exemple, le titre de l'article. Et c'est exactement ce que nous voulons mesurer.

J'ai choisi le [compte freeCodeCamp](https://twitter.com/freecodecamp) pour ce projet parce que l'idée était de limiter la portée du sujet des articles et de mieux prédire la réponse dans un domaine spécifique. Le même titre peut bien performer dans une catégorie (par exemple, Technologie), mais pas nécessairement dans une autre (par exemple, Culinaire). De plus, ce compte publie le titre de l'article original et l'URL sur Medium comme contenu du tweet.

### À quoi ressemblent les données ?

La première étape de ce projet était d'obtenir les informations de Twitter et Medium puis de les corréler. Le jeu de données peut être trouvé [ici](https://github.com/flaviohenriquecbc/machine-learning-capstone-project/blob/master/dataset/dataset-tweets-final.json) et il contient 711 points de données. Voici à quoi ressemble le jeu de données :

### Analyser et apprendre avec les données

Après avoir analysé le jeu de données et tracé quelques graphiques, j'ai trouvé des informations intéressantes à ce sujet. Pour ces analyses, **les valeurs aberrantes ont été supprimées**, et j'ai simplement considéré les **25 % meilleurs performeurs** pour chaque caractéristique (retweet, like et applaudissement).

Alors, examinons ce que les chiffres disent pour les articles freeCodeCamp écrits sur Medium et partagés sur Twitter.

#### Quelle est la bonne longueur de titre ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*Mm7zCNram85z-qmQ2PYGgA.png)
_Performance de la longueur du titre_

Écrire des titres ayant une longueur **supérieure à 50 et inférieure à 110** caractères aide à augmenter les chances de succès d'un article.

#### Quel est le bon nombre de mots dans le titre ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*fQ1kXH82jeikkfUtsl7baA.png)
_Performance du nombre de mots_

Le nombre de mots le plus efficace dans le titre est **9 à 17**. Pour optimiser le nombre de retweets et de likes, essayez quelque chose de 9 à 18 mots, et pour les applaudissements de 7 à 17.

#### Quelles sont les meilleures catégories à taguer ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*NNmbj8LjKK4Mj1eBvRD2wQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*spIxtLO9qD042AP-XFiicA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*WSluJ1QtQNwukYnW60TU1A.png)

**Programmation**, **Tech**, **Technologie**, **JavaScript** et **Développement Web** sont des catégories que vous devriez considérer lors du taggage de votre prochain article. Elles apparaissent pour les trois caractéristiques comme un bon indicateur.

#### Quels sont les meilleurs mots à utiliser ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*f1vJmkiXf0Nlxc9nCU0Vrw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*vKj2TVnOSgLHWuv3WiAZUA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y4PqnyR2dF4da5WWKuqS1g.png)

Dans cette analyse lexicale, vous remarquerez que certains mots attirent beaucoup plus l'attention de la communauté freeCodeCamp que d'autres. Si l'intention est de faire en sorte que les articles atteignent un plus grand nombre de personnes, parler de JavaScript, React ou CSS augmentera leur appréciation. Utiliser les mots « apprendre » ou « guide » pour décrire augmentera également la probabilité.

### Utilisation du Machine Learning

OK ! Après avoir examiné les données et en avoir extrait quelques informations, l'objectif était de créer un modèle de Machine Learning qui prédit le nombre de retweets, de likes et d'applaudissements en fonction du titre de l'article.

Prédire le nombre de retweets, de likes et d'applaudissements d'un article peut être traité comme un problème de classification, et c'est une tâche courante du machine learning (ML). Mais pour cela, nous devons utiliser la sortie comme des valeurs discrètes (une plage de nombres). L'entrée sera le titre des articles avec chaque mot comme un token (t1, t2, t3, … tn), la longueur du titre et le nombre de mots dans le titre.

Les plages pour nos caractéristiques sont :

* Retweets : 0–10, 10–30, 30+
* Likes : 0–25, 25–60, 60+
* Applaudissements : 0–50, 50–400, 400+

Et enfin, après avoir prétraité notre jeu de données et évalué quelques modèles (tout est entièrement décrit [ici](https://github.com/flaviohenriquecbc/machine-learning-capstone-project/blob/master/final-report.pdf)), nous avons conclu que le modèle MultinomialNB performait mieux pour les retweets, atteignant une précision de 60,6 %. La régression logistique a atteint 55,3 % pour les likes et 49 % pour les applaudissements.

En tant qu'expérience pour cet article, j'ai exécuté la prédiction du titre de cet article et le modèle a prédit que :

Il aura 10–30 retweets et 25–60 favoris sur Twitter et 400+ applaudissements sur Medium.

Comment est cette prédiction ? 😊

[_Suivez-moi_](https://medium.com/@flaviohfreitas) _si vous voulez lire plus de mes articles_ 😊 _Et si vous avez aimé cet article, n'oubliez pas de l'aimer et de me donner beaucoup d'applaudissements — cela signifie beaucoup pour l'auteur._

**Flávio H. de Freitas** est un entrepreneur, ingénieur, passionné de technologie, rêveur et voyageur. Il a travaillé en tant que **CTO** au **Brésil**, dans la **Silicon Valley et en Europe**.