---
title: Comment fonctionne node2vec — et ce qu'il peut faire que word2vec ne peut pas
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T16:12:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-think-about-your-data-in-a-different-way-b84306fc2e1d
coverImage: https://cdn-media-1.freecodecamp.org/images/0*F6r_nGc1ofNeYFmw.png
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Deep Learning
  slug: deep-learning
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
seo_title: Comment fonctionne node2vec — et ce qu'il peut faire que word2vec ne peut
  pas
seo_desc: 'By Zohar Komarovsky

  How to think about your data differently


  In the last couple of years, deep learning (DL) has become the main enabler for
  applications in many domains such as vision, NLP, audio, clickstream data etc. Recently,
  researchers started...'
---

Par Zohar Komarovsky

#### Comment penser à vos données différemment

![Image](https://cdn-media-1.freecodecamp.org/images/CLJqT9ZZlgJfMUcv0zhZQNVqrPX0QUzZmQl-)

Au cours des dernières années, l'apprentissage profond (DL) est devenu le principal moteur des applications dans de nombreux domaines tels que la vision, le NLP, l'audio, les données de clics, etc. Récemmement, les chercheurs ont commencé à appliquer avec succès des méthodes d'apprentissage profond aux ensembles de données graphiques dans des domaines comme les réseaux sociaux, les systèmes de recommandation et la biologie, où les données sont naturellement structurées de manière graphique.

Alors, comment fonctionnent les réseaux de neurones graphiques ? Pourquoi en avons-nous besoin ?

### Le Postulat de l'Apprentissage Profond

Dans les tâches d'apprentissage automatique qui impliquent des données graphiques, nous voulons généralement décrire chaque nœud du graphe de manière à pouvoir l'alimenter dans un algorithme d'apprentissage automatique. Sans le DL, il faudrait extraire manuellement des caractéristiques, comme le nombre de voisins qu'un nœud possède. Mais c'est un travail fastidieux.

C'est là que le DL brille. Il exploite automatiquement la structure du graphe afin d'extraire des caractéristiques pour chaque nœud. Ces caractéristiques sont appelées embeddings.

Ce qui est intéressant, c'est que même si vous n'avez absolument aucune information sur les nœuds, vous pouvez toujours utiliser le DL pour extraire des embeddings. La structure du graphe, c'est-à-dire les motifs de connectivité, contient des informations viables.

Alors, comment pouvons-nous utiliser la structure pour extraire des informations ? Le contexte de chaque nœud au sein du graphe peut-il vraiment nous aider ?

### Apprendre du Contexte

Un algorithme bien connu qui extrait des informations sur des entités en utilisant uniquement le contexte est [word2vec](https://www.tensorflow.org/tutorials/representation/word2vec). L'entrée de word2vec est un ensemble de phrases, et la sortie est un embedding pour chaque mot. De manière similaire à la façon dont le texte décrit le contexte de chaque mot via les mots qui l'entourent, les graphes décrivent le contexte de chaque nœud via les nœuds voisins.

Alors que dans le texte, les mots apparaissent dans un ordre linéaire, dans les graphes, ce n'est pas le cas. Il n'y a pas d'ordre naturel entre les nœuds voisins. Nous ne pouvons donc pas utiliser word2vec... Ou pouvons-nous ?

### Réduction comme un Mathématicien Badass

Nous pouvons appliquer une réduction de la structure graphique de nos données en une structure linéaire de sorte que l'information encodée dans la structure graphique ne soit pas perdue. En faisant cela, nous pourrons utiliser le bon vieux word2vec.

Le point clé est d'effectuer des marches aléatoires dans le graphe. Chaque marche commence à un nœud aléatoire et effectue une série d'étapes, où chaque étape va vers un voisin aléatoire. Chaque marche aléatoire forme une phrase qui peut être alimentée dans word2vec. Cet algorithme est appelé [node2vec](https://snap.stanford.edu/node2vec/). Il y a plus de détails dans le processus, que vous pouvez lire dans [l'article original](https://arxiv.org/abs/1607.00653).

### Étude de cas

Le système de recommandation de contenu de Taboola collecte beaucoup de données, dont certaines peuvent être représentées de manière graphique. Inspectons un type de données comme étude de cas pour l'utilisation de node2vec.

Taboola recommande des articles dans un widget affiché sur les sites web des éditeurs :

![Image](https://cdn-media-1.freecodecamp.org/images/wrDUiTx51a9rETzHd0FdXSfgkffDLXGV6vIK)

Chaque article contient des entités nommées — les entités décrites par le titre. Par exemple, l'élément « les chiens les plus mignons de la planète » contient les entités « chien » et « planète ». Chaque entité nommée peut apparaître dans de nombreux éléments différents.

Nous pouvons décrire cette relation à l'aide d'un graphe de la manière suivante : chaque nœud sera une entité nommée. Il y aura une arête entre deux nœuds si les deux entités nommées apparaissent dans le même élément :

![Image](https://cdn-media-1.freecodecamp.org/images/IhE2zMm-vJUJTLQEghWqD8xupOoa6qdAvZSM)

Maintenant que nous sommes capables de décrire nos données de manière graphique, exécutons node2vec pour voir quelles informations nous pouvons tirer des données. Vous pouvez trouver le code fonctionnel [ici](https://github.com/taboola/node2vec-example).

Après avoir appris les embeddings de nœuds, nous pouvons les utiliser comme caractéristiques pour une tâche en aval, par exemple la prédiction du CTR (Taux de Clics). Bien que cela puisse bénéficier au modèle, il sera difficile de comprendre les qualités apprises par node2vec.

Une autre option serait de regrouper les embeddings similaires ensemble en utilisant [K-means](https://en.wikipedia.org/wiki/K-means_clustering), et de colorier les nœuds selon leur cluster associé :

![Image](https://cdn-media-1.freecodecamp.org/images/wyi9ZeO-x0wghF6wofDdYJj6zmUdf-3MQnIs)

Cool ! Les clusters capturés par node2vec semblent être homogènes. En d'autres termes, les nœuds qui sont proches les uns des autres dans le graphe sont également proches les uns des autres dans l'espace d'embedding. Prenons par exemple le cluster orange — toutes ses entités nommées sont liées au basket-ball.

Vous pourriez vous demander quel est l'avantage d'utiliser node2vec par rapport aux algorithmes graphiques classiques, tels que les algorithmes de détection de communautés (par exemple, l'[algorithme de Girvan-Newman](https://arxiv.org/abs/cond-mat/0308217)). Capturer la communauté à laquelle chaque nœud appartient peut définitivement être fait en utilisant de tels algorithmes, il n'y a rien de mal à cela.

En fait, c'est exactement de l'ingénierie de caractéristiques. Et nous savons déjà que le DL peut vous faire gagner du temps en évitant de concevoir soigneusement de telles caractéristiques. Alors pourquoi ne pas profiter de cet avantage ? Nous devons également garder à l'esprit que node2vec apprend des embeddings de haute dimension. Ces embeddings sont beaucoup plus riches que la simple appartenance à une communauté.

### Prendre une autre approche

Utiliser node2vec dans ce cas d'utilisation pourrait ne pas être la première idée qui vient à l'esprit. Certains pourraient suggérer d'utiliser simplement word2vec, où chaque phrase est la séquence d'entités nommées à l'intérieur d'un seul élément. Dans cette approche, nous ne traitons pas les données comme ayant une structure graphique. Alors, quelle est la différence entre cette approche — qui est valide, et node2vec ?

Si nous y réfléchissons, chaque phrase que nous générons dans l'approche word2vec est une marche dans le graphe que nous avons défini précédemment. node2vec définit également des marches sur le même graphe. Donc, elles sont les mêmes, n'est-ce pas ? Regardons les clusters que nous obtenons avec l'approche word2vec :

![Image](https://cdn-media-1.freecodecamp.org/images/qCIzNZB-SyuFfyWuFE3i8kBYvmH1-0BQ-Ad0)

Maintenant, le cluster « basket-ball » est moins homogène — il contient à la fois des nœuds orange et bleus. L'entité nommée « Basket-ball » a été colorée en orange. Alors que les joueurs de basket-ball « Lebron James » et « Kobe Bryant » ont été colorés en bleu !

![Image](https://cdn-media-1.freecodecamp.org/images/Anio-hQU7RLZEI9A5Gfu-qxtW97X8Zskrcjj)

Mais pourquoi cela s'est-il produit ?

Dans cette approche, chaque marche dans le graphe est composée uniquement d'entités nommées qui apparaissent ensemble dans un seul élément. Cela signifie que nous sommes limités à des marches qui ne vont pas plus loin que la distance 1 du nœud de départ. Dans node2vec, nous n'avons pas cette limite. Puisque chaque approche utilise un type différent de marches, les embeddings appris capturent un type différent d'informations.

Pour rendre cela plus concret, considérons l'exemple suivant. Supposons que nous avons deux éléments — l'un avec les entités nommées A, B, C et un autre avec D, B, E. Ces éléments induisent le graphe suivant :

![Image](https://cdn-media-1.freecodecamp.org/images/sN3PAiNFMZOSSoazpQQAYGXowrHhFqFy5Urv)

Dans l'approche simple de word2vec, nous générerons les phrases suivantes : [A, B, C] et [D, B, E]. Dans l'approche node2vec, nous pourrions également obtenir des phrases comme [A, B, E]. Si nous intégrons cette dernière dans le processus de formation, nous apprendrons que E et C sont interchangeables. Le préfixe [A, B] pourra prédire à la fois C et E. Par conséquent, C et E obtiendront des embeddings similaires et seront regroupés ensemble.

### Points clés

Utiliser la bonne structure de données pour représenter vos données est important. Chaque structure de données implique un algorithme d'apprentissage différent. Ou en d'autres termes — introduit un biais inductif différent.

Identifier que vos données ont une certaine structure, afin de pouvoir utiliser le bon outil pour la tâche, peut être un défi.

Puisque tant de jeux de données du monde réel sont naturellement représentés sous forme de graphes, nous pensons que les réseaux de neurones graphiques sont un incontournable dans notre boîte à outils en tant que scientifiques des données.

_Publié à l'origine sur [engineering.taboola.com](https://engineering.taboola.com/think-data-different) par moi et [Yoel Zeldes](https://www.freecodecamp.org/news/how-to-think-about-your-data-in-a-different-way-b84306fc2e1d/undefined).