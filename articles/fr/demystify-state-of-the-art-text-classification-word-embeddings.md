---
title: 'La classification de texte démystifiée : une introduction aux plongements
  lexicaux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-20T14:39:00.000Z'
originalURL: https://freecodecamp.org/news/demystify-state-of-the-art-text-classification-word-embeddings
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/head-image-word-embeddings_papr.jpg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: neural networks
  slug: neural-networks
- name: nlp
  slug: nlp
seo_title: 'La classification de texte démystifiée : une introduction aux plongements
  lexicaux'
seo_desc: 'By Sebastian Sigl

  Natural language processing (NLP) is an old science that started in the 1950s. The
  Georgetown IBM experiment in 1954 was a big step towards a fully automated text
  translation. More than 60 Russian sentences were translated into Engl...'
---

Par Sebastian Sigl

Le traitement du langage naturel (NLP) est une science ancienne qui a commencé dans les années 1950. L'[expérience Georgetown IBM](https://en.wikipedia.org/wiki/Georgetown%E2%80%93IBM_experiment) en 1954 a été une grande étape vers une traduction de texte entièrement automatisée. Plus de 60 phrases russes ont été traduites en anglais en utilisant des règles simples de réorganisation et de remplacement.

La révolution statistique dans le NLP a commencé à la fin des années 1980. Au lieu de créer manuellement un ensemble de règles, un grand corpus de texte a été analysé pour créer des règles en utilisant des approches statistiques. Différentes métriques ont été calculées pour les données d'entrée données, et des prédictions ont été faites en utilisant des arbres de décision ou des [calculs basés sur la régression](https://en.wikipedia.org/wiki/Regression_analysis).

Aujourd'hui, les métriques complexes sont remplacées par des approches plus holistiques qui créent de meilleurs résultats et qui sont plus faciles à maintenir.

Cet article traite des plongements lexicaux, qui est la première partie de ma série sur l'apprentissage automatique pour les codeurs (avec plus à venir !).

## Qu'est-ce que les plongements lexicaux ?

Traditionnellement, dans le traitement du langage naturel (NLP), les mots étaient remplacés par des identifiants uniques pour effectuer des calculs. Prenons l'exemple suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/example-of-examples-word-embeddings_grey.jpg)

Cette approche a l'inconvénient que vous devrez créer une énorme liste de mots et donner à chaque élément un identifiant unique. Au lieu d'utiliser des nombres uniques pour vos calculs, vous pouvez également utiliser des vecteurs pour représenter leur signification, appelés plongements lexicaux :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/example-of-examples-word-embeddings_vectors.jpg)

Dans cet exemple, chaque mot est représenté par un vecteur. La longueur d'un vecteur peut être différente. Plus le vecteur est grand, plus il peut stocker d'informations contextuelles. De plus, les coûts de calcul augmentent avec la taille du vecteur.

Le nombre d'éléments d'un vecteur est également appelé le nombre de dimensions du vecteur. Dans l'exemple ci-dessus, le mot **exemple** est exprimé avec (4 2 6), où 4 est la valeur de la première dimension, 2 de la deuxième, et 6 de la troisième dimension.

Dans des exemples plus complexes, il peut y avoir plus de 100 dimensions qui peuvent encoder beaucoup d'informations. Des choses comme :

* le genre,
* la race,
* l'âge,
* le type de mot

seront stockées.

Un mot comme **one** est un mot qui est une quantité comme **many**. Par conséquent, les deux vecteurs sont plus proches comparés aux mots qui sont plus différents dans leur utilisation.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/word-embeddings-diagram.png)

Simplifié, si les vecteurs sont similaires, alors les mots ont des similitudes dans leur utilisation. Pour d'autres tâches de NLP, cela présente de nombreux avantages car les calculs peuvent être effectués sur la base d'un seul vecteur avec seulement quelques centaines de paramètres par rapport à un énorme dictionnaire avec des centaines de milliers d'identifiants.

De plus, s'il y a des mots inconnus qui n'ont jamais été vus auparavant, alors ce n'est pas un problème. Vous avez juste besoin d'un bon plongement lexical du nouveau mot, et les calculs sont similaires. La même chose s'applique à d'autres langues. C'est essentiellement la magie des plongements lexicaux qui permet des choses comme l'apprentissage rapide, le traitement multilingue, et bien plus encore.

## Création de plongements lexicaux

Il est très populaire d'étendre le concept de plongements lexicaux à d'autres domaines. Par exemple, une plateforme de location de films peut créer des plongements de films et effectuer des calculs sur des vecteurs au lieu d'identifiants de films.

### Mais comment créer de tels plongements ?

Il existe diverses techniques, mais toutes suivent l'aspect clé selon lequel la signification d'un mot est définie par son utilisation.

Supposons que nous avons un ensemble de phrases :

```python
text_for_training = [
    'he is a king',
    'she is a queen',
    'he is a man',
    'she is a woman',
    'she is a daughter',
    'he is a son'
]
```

Les phrases contiennent 10 mots uniques, et nous voulons créer un plongement lexical pour chaque mot.

```python
{
    0: 'he',
    1: 'a',
    2: 'is',
    3: 'daughter',
    4: 'man',
    5: 'woman',
    6: 'king',
    7: 'she',
    8: 'son',
    9: 'queen'
}
```

Il existe diverses approches pour créer des plongements à partir de ceux-ci. Choisissons l'une des approches les plus utilisées appelée [word2vec](https://en.wikipedia.org/wiki/Word2vec). Le concept derrière cette technique utilise un réseau de neurones très simple pour créer des vecteurs qui représentent les significations des mots.

Commençons par le mot cible « **king** ». Il est utilisé dans le contexte du pronom masculin « **he** ». Le contexte dans cet exemple signifie qu'il fait simplement partie de la même phrase. La même chose s'applique à « **queen** » et « **she** ». Il est également logique de faire la même approche pour des mots plus génériques. Le mot « **he** » peut être le mot cible et « **is** » est le mot de contexte.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/he_is_king_target_context_example.gif)

Si nous faisons cela pour chaque combinaison, nous pouvons en fait obtenir des plongements lexicaux simples. Des approches plus holistiques ajoutent plus de complexité et de calculs, mais elles sont toutes basées sur cette approche.

Pour utiliser un mot comme entrée pour un réseau de neurones, nous avons besoin d'un vecteur. Nous pouvons décoder l'identifiant unique d'un mot en un vecteur en mettant un 1 à la position du mot de notre dictionnaire et en gardant tous les autres index à 0. Cela s'appelle un vecteur encodé one-hot :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/input_output_idx.jpg)

Entre l'entrée et la sortie se trouve une seule couche cachée. Cette couche contient autant d'éléments que le plongement lexical doit avoir. Plus les plongements lexicaux ont d'éléments, plus ils peuvent stocker d'informations. 

Vous pourriez penser, alors faites-le simplement très grand. Mais nous devons considérer que nous devons stocker un plongement pour chaque mot existant, ce qui s'additionne rapidement à une quantité décente de données à stocker. De plus, des plongements plus grands signifient beaucoup plus de calculs pour les réseaux de neurones qui utilisent des plongements.

Dans notre exemple, nous utiliserons simplement 5 comme taille de vecteur de plongement.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/input_output_hidden_layer.jpg)

La magie des réseaux de neurones réside dans ce qu'il y a entre les couches, appelé poids. Ils stockent des informations entre les couches, où chaque nœud de la couche précédente est connecté à chaque nœud de la couche suivante.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/input_output_hidden_layer_connections.jpg)

Chaque connexion entre les couches est un paramètre. Ces paramètres contiennent les informations importantes des réseaux de neurones. 100 paramètres - 50 entre la couche d'entrée et la couche cachée, et 50 entre la couche cachée et la couche de sortie - sont initialisés avec des valeurs aléatoires et ajustés en entraînant le modèle.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/head-image-word-embeddings.jpg)

Dans cet exemple, tous sont initialisés avec 0,1 pour simplifier. Pensons à un exemple de tour d'entraînement, également appelé une époque :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/input_output_hidden_layer_example_1.jpg)

À la fin du calcul du réseau de neurones, nous n'obtenons pas la sortie attendue qui nous dit pour le contexte donné « **he** » que la cible est « **king** ».

Cette différence entre le résultat et le résultat attendu est appelée l'erreur d'un réseau. En trouvant de meilleures valeurs de paramètres, nous pouvons ajuster le réseau de neurones pour prédire pour les entrées de contexte futures qui délivrent la sortie cible attendue.

Le contenu de nos connexions de couches changera après avoir essayé de trouver de meilleurs paramètres qui nous rapprochent de notre vecteur de sortie attendu. L'erreur est minimisée dès que le réseau prédit correctement pour différents mots cibles et mots de contexte. Les poids entre la couche d'entrée et la couche cachée contiendront tous nos plongements lexicaux.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/example_train_weights_word_embedding.gif)

Vous pouvez trouver l'exemple complet avec du code exécutable [ici](https://colab.research.google.com/drive/1KN4wi_dcTAp55FqqFs-ashf4NqdIlYy0). Vous pouvez créer une copie et jouer avec en appuyant sur « Open in playground. »

Si vous n'êtes pas familier avec les notebooks, c'est assez simple : il peut être lu de haut en bas, et vous pouvez cliquer et éditer le code Python directement. 

En appuyant sur « SHIFT+Enter », vous pouvez exécuter des extraits de code. Assurez-vous simplement de commencer en haut en cliquant dans le premier extrait et en appuyant sur SHIFT+Enter, attendez un peu et appuyez à nouveau sur SHIFT+Enter, et ainsi de suite.

## Conclusion

En résumé, les plongements lexicaux sont utilisés pour créer des réseaux de neurones de manière plus flexible. Ils peuvent être construits en utilisant des réseaux de neurones qui ont une certaine tâche, telle que la prédiction d'un mot cible pour un mot de contexte donné. Les poids entre les couches sont des paramètres qui sont ajustés au fil du temps. Et voilà, vous avez vos plongements lexicaux.

J'espère que vous avez apprécié l'article. Si vous l'aimez et ressentez le besoin d'une ronde d'applaudissements, [suivez-moi sur Twitter](https://twitter.com/sesigl). Je travaille chez eBay Kleinanzeigen, l'une des plus grandes entreprises de petites annonces au monde. Au fait, [nous recrutons](https://jobs.ebayclassifiedsgroup.com/ebay-kleinanzeigen) !

Bonne exploration de l'IA :)

Références

* Wikipedia natural language processing  
[https://en.wikipedia.org/wiki/Natural_language_processing](https://en.wikipedia.org/wiki/Natural_language_processing)
* Great paper about text classification created by co-founders of fastai  
[https://arxiv.org/abs/1801.06146](https://arxiv.org/abs/1801.06146)
* Googles state of the art approach for NLP tasks  
[https://arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)