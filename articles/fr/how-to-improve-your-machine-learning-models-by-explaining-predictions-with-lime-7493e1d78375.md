---
title: Comment améliorer vos modèles de machine learning en expliquant les prédictions
  avec LIME
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T23:30:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-improve-your-machine-learning-models-by-explaining-predictions-with-lime-7493e1d78375
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LJj4hmOES-c0DYj4Kwg89A.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Comment améliorer vos modèles de machine learning en expliquant les prédictions
  avec LIME
seo_desc: 'By Déborah Mesquita

  Increase users’ trust and find bugs faster


  _With LIME we can have discussions like this about our models with everyone (thanks
  [Štefan](https://unsplash.com/@cikstefan" rel="noopener" target="blank" title=")
  for the pic!)

  Even th...'
---

Par Débora Mesquita

#### Augmentez la confiance des utilisateurs et trouvez les bugs plus rapidement

![Image](https://cdn-media-1.freecodecamp.org/images/1*LJj4hmOES-c0DYj4Kwg89A.jpeg)
_Avec LIME, nous pouvons avoir des discussions comme celle-ci sur nos modèles avec tout le monde (merci [Štefan](https://unsplash.com/@cikstefan" rel="noopener" target="_blank" title=") pour la photo !)_

Même si nous aimons l'idée que nous ne faisons jamais d'erreurs, tout logiciel peut contenir des bugs. En supposant que nous puissions utiliser des modèles de Machine Learning pour prendre des décisions dans le monde réel, un bug dans notre code peut être très dangereux. Se fier uniquement à la précision des prédictions peut ne pas être une bonne idée, car si nous obtenons un bon score de précision, nous pourrions ne pas considérer qu'il y a un bug dans notre pipeline de données.

<iframe width="560" height="315" src="https://www.youtube.com/embed/veiLCvcLIg8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

La plupart des algorithmes de Machine Learning sont des boîtes noires, mais [LIME](https://github.com/marcotcr/lime) a une proposition de valeur audacieuse : **expliquer les résultats de n'importe quel modèle prédictif**. L'outil peut expliquer des modèles entraînés avec du texte, des données catégorielles ou continues. Aujourd'hui, nous allons expliquer les prédictions d'un modèle entraîné pour classer des phrases d'articles scientifiques.

Commençons par comprendre comment LIME fonctionne. Ensuite, je vous montrerai comment construire un modèle de deep learning pour classer les phrases (en utilisant AllenNLP) et expliquer les prédictions avec LIME.

### Explications locales interprétables et agnostiques (LIME)

Les prédictions agnostiques sont utilisées lorsque l'algorithme n'essaie pas de travailler avec la fonction de décision des modèles. LIME utilise le critère de **fidélité locale** :

> [] Pour qu'une explication soit significative, elle doit au moins être localement fidèle, c'est-à-dire **qu'elle doit correspondre à la manière dont le modèle se comporte dans le voisinage de l'instance prédite**.  [Ribeiro, Marco Tulio, Sameer Singh, et Carlos Guestrin](https://arxiv.org/abs/1602.04938)

Pour créer ce voisinage de l'instance, LIME perturbe l'instance qu'il va expliquer. Les auteurs notent également que **la fidélité locale n'implique pas la fidélité globale** :

> [] **Les caractéristiques qui sont globalement importantes peuvent ne pas être importantes dans le contexte local, et vice versa**. Bien que la fidélité globale impliquerait la fidélité locale, l'identification d'explications globalement fidèles qui sont interprétables reste un défi pour les modèles complexes.  [Ribeiro, Marco Tulio, Sameer Singh, et Carlos Guestrin](https://arxiv.org/abs/1602.04938)

L'image ci-dessous présente un exemple jouet de la manière dont LIME fonctionne. Cela est tiré de [l'article qui présente l'algorithme](https://arxiv.org/abs/1602.04938).

![Image](https://cdn-media-1.freecodecamp.org/images/1*dZsU2fe84gMYb3pierxI-Q.png)
_Les zones rouges et bleues représentent la fonction de décision complexe du modèle, qui est inconnue de LIME. La croix rouge en gras est l'instance de données que nous voulons expliquer._

Les croix rouges et les cercles bleus sont des instances d'échantillons que LIME crée uniformément au hasard. LIME obtient la prédiction pour ces instances et les pondère par la proximité avec l'instance expliquée  la croix rouge en gras. Dans l'image, la proximité est représentée par la **taille** de chaque croix et de chaque cercle. La ligne en pointillés représente l'explication qui est localement  mais pas globalement  fidèle.

Voici une catégorisation de champignons produite avec LIME :

![Image](https://cdn-media-1.freecodecamp.org/images/0*y6DD7Z9K6tDdFqZy.png)
_Explication pour les données catégorielles_

Le modèle prédit si un champignon est toxique ou non. Nous pouvons voir que `odor=foul` est indicatif d'un champignon toxique.

> Puisque nous perturbons chaque caractéristique catégorielle en tirant des échantillons selon la distribution d'entraînement originale, la manière d'interpréter cela est : **si l'odeur n'était pas fétide, en moyenne, cette prédiction serait 0,26 moins 'toxique'**  [Tutoriel sur les données tabulaires](https://marcotcr.github.io/lime/tutorials/Tutorial%20-%20continuous%20and%20categorical%20features.html)

Maintenant, voyons comment utiliser l'outil.

### Expliquer les prédictions avec LIME

Il existe trois types d'explicateurs :

* **LimeTabularExplainer** : explique les prédictions sur des données tabulaires ou matricielles
* **LimeImageExplainer** : explique les prédictions sur des données d'image
* **LimeTextExplainer** : explique les classificateurs de texte

Dans cet article, nous allons utiliser le **LimeTextExplainer**. Il existe des tutoriels pour [tous les autres explicateurs ici](https://github.com/marcotcr/lime).

Actuellement, l'outil restreint les explications aux mots présents dans les documents, [comme expliqué ici](https://github.com/marcotcr/lime/blob/226c758cdc58d77b534278d30e2c83438ecd865a/lime/lime_text.py#L292).

Pour construire le LimeTextExplainer, nous devons simplement fournir les noms de classe, alias les labels. Expliquer une instance signifie que nous devons passer les données de l'instance **et** une fonction qui fournira les prédictions. Pour cela, nous avons besoin d'un modèle entraîné. Construisons-en un en utilisant AllenNLP.

### AllenNLP

[**AllenNLP**](http://allennlp.org/) est un framework pour construire des modèles de Deep Learning pour le traitement du langage naturel. **C'est un outil fantastique.** Je suis toujours amoureuse de la manière dont il facilite la tâche de construction de modèles de Deep Learning.

Le modèle que nous allons construire utilise des embeddings de mots pour encoder l'entrée et le réseau possède des cellules LSTM.

Si vous devez en apprendre un peu plus sur les cellules LSTM et RNN, consultez cet [autre article](https://medium.com/swlh/deep-learning-for-text-made-easy-with-allennlp-62bc79d41f31) que j'ai écrit. **J'explique également [comment AllenNLP fonctionne en détail là-bas](https://medium.com/swlh/deep-learning-for-text-made-easy-with-allennlp-62bc79d41f31)**.

Avec le framework, nous définissons l'architecture du modèle dans un fichier JSON. Voici l'architecture de notre modèle :

```json
{
  "dataset_reader": {
    "type": "az_papers"
  },
  "train_data_path": "../../data/AZ_distribution/train/",
  "model": {
    "type": "sentence_classifier",
    "text_field_embedder": {
      "tokens": {
        "type": "embedding",
        "pretrained_file": "https://s3-us-west-2.amazonaws.com/allennlp/datasets/glove/glove.6B.100d.txt.gz",
        "embedding_dim": 100,
        "trainable": false
      }
    },
    "title_encoder": {
      "type": "lstm",
      "bidirectional": true,
      "input_size": 100,
      "hidden_size": 100,
      "num_layers": 1,
      "dropout": 0.2
    },
    "sentence_encoder": {
      "type": "lstm",
      "bidirectional": true,
      "input_size": 100,
      "hidden_size": 100,
      "num_layers": 1,
      "dropout": 0.2
    },
    "classifier_feedforward": {
      "input_dim": 400,
      "num_layers": 2,
      "hidden_dims": [200, 7],
      "activations": ["relu", "linear"],
      "dropout": [0.2, 0.0]
    }
  },
  "iterator": {
    "type": "bucket",
    "sorting_keys": [["sentence", "num_tokens"], ["title", "num_tokens"]],
    "batch_size": 64
  },
  "trainer": {
    "num_epochs": 40,
    "patience": 10,
    "cuda_device": -1,
    "grad_clipping": 5.0,
    "validation_metric": "+accuracy",
    "optimizer": {
      "type": "adagrad"
    }
  }
}
```

Cela ne fait probablement aucun sens si vous êtes nouveau dans AllenNLP. Le but de cet article est de montrer comment utiliser LIME, donc nous n'allons pas approfondir. J'essaie d'expliquer plus sur AllenNLP dans cet [autre article](https://medium.com/swlh/deep-learning-for-text-made-easy-with-allennlp-62bc79d41f31). Et, bien sûr, [le code complet pour entraîner le modèle est ici](https://github.com/dmesquita/explaining_predictions_with_LIME).

Le jeu de données est le corpus original [Argumentative Zoning corpus [AZ corpus]](https://www.cl.cam.ac.uk/~sht25/AZ_corpus.html). Il se compose de 80 articles de conférence annotés AZ en linguistique informatique, initialement tirés de arXiv. Chaque phrase a l'une de ces étiquettes :

* BKG : Contexte scientifique général
* OTH : Descriptions neutres du travail des autres
* OWN : Descriptions neutres du propre travail, nouveau travail
* AIM : Déclarations de l'objectif particulier de l'article actuel
* TXT : Déclarations de l'organisation textuelle de l'article actuel (dans le chapitre 1, nous introduisons)
* CTR : Déclarations contrastives ou comparatives sur d'autres travaux ; mention explicite des faiblesses d'autres travaux
* BAS : Déclarations selon lesquelles le propre travail est basé sur d'autres travaux

Pour entraîner le modèle, nous utilisons cette commande :

```bash
python3 run.py train experiments/the_file_presented_before.json  
--include-package newsgroups.dataset_readers 
--include-package newsgroups.models 
-s /tmp/our_model 
```

### Expliquer les prédictions du modèle

Pour prédire la classe de chaque phrase, nous utilisons le `title` de l'article et la `sentence` elle-même. Avec AllenNLP, voici comment nous faisons :

![Image](https://cdn-media-1.freecodecamp.org/images/1*fqjwt8S8qoci-dfrxjX-DA.png)
_Faire des prédictions avec AllenNLP_

Comme je le disais plus tôt, les deux paramètres clés de `LimeTextExplainer.explain_instance()` sont l'instance elle-même et une fonction qui retourne la probabilité de prédiction pour chaque classe  comme la fonction [predict_proba](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier.predict_proba) de scikit-learn. Ici, cette fonction prend une liste de **d** chaînes et produit un tableau NumPy (**d**, **n_classes**) avec les probabilités de prédiction.

L'algorithme perturbe les données d'entrée en supprimant toutes les occurrences de mots individuels et en obtenant les probabilités de prédiction pour les nouvelles instances. Je ne suis intéressée que par la perturbation des mots de la partie `sentence` de l'entrée, donc voici comment j'ai défini la fonction :

```py
#Pour chaque phrase perturbée, nous obtenons le predict_proba d'AllenNLP

predict_function = lambda x: np.array([predictor.predict_json(json.loads('{"title": "Incremental Interpretation of Categorial Grammar","sentence":"'+s+'"}'))['class_probabilities'] for s in x])
```

Ensuite, nous importons LIME, définissons les `class_names`, et appelons la méthode `explain_instance` :

```py
from lime.lime_text import LimeTextExplainer

explainer = LimeTextExplainer(class_names=['OWN', 'OTH', 'BKG', 'CTR', 'AIM', 'TXT', 'BAS'])

row = json.loads('{"title": "Incremental Interpretation of Categorial Grammar", "sentence": "In processing a sentence using a lexicalised formalism we do not have to look at the grammar as a whole , but only at the grammatical information indexed by each of the words ."}')

exp = explainer.explain_instance(row["sentence"], predict_fn, num_features=10,top_labels=2)

#Afficher les résultats dans le notebook
exp.show_in_notebook(text=False)
```

Et voici le résultat :

![Image](https://cdn-media-1.freecodecamp.org/images/1*v4oEQzJa-Ci53JtXPYM__w.png)

La phrase est classée comme OWN  description du travail de l'auteur. Nous pouvons voir pourquoi : les mots indexed, grammatical, et we.

Il semble que le mot the ait une grande pertinence pour OWN. Cela peut être dû uniquement à la **fidélité locale** et peut-être est-il bon de supprimer les mots vides.

Regardons d'autres exemples :

![Image](https://cdn-media-1.freecodecamp.org/images/1*H7FZk2soeSuGy6jnq3p7ZQ.png)
_Celui-ci était facile à classer_

![Image](https://cdn-media-1.freecodecamp.org/images/1*O7iuovxvu-HOUDIWSrJGVA.png)
_Explication pour une phrase de contexte scientifique général_

### Points clés

En voyant ce dont LIME est capable, je pense que **pouvoir comprendre les raisons derrière une prédiction est un must pour chaque projet de Machine Learning.** Surtout lorsque nos intérêts vont au-delà de la simple considération de la précision des résultats.

Les explications peuvent aider les utilisateurs à faire confiance aux prédictions, mais elles peuvent également nous aider  nous, les data scientists  à identifier les bugs ou les choses qui ne fonctionnent pas comme prévu.

Je travaille sur un projet qui utilise des données catégorielles. Parce que j'utilisais LIME pour expliquer les prédictions, j'ai pu trouver un bug tôt dans le processus. Les raisons des prédictions n'avaient pas de sens, ce qui m'a poussé à creuser profondément dans le code et à trouver le bug. Si je m'étais uniquement fiée à la précision du modèle, cela m'aurait pris beaucoup de temps pour trouver le bug car le modèle avait des scores de précision raisonnablement bons.

**Alors, si vous construisez des modèles de Machine Learning, essayez LIME !** Pour plus d'informations, vous pouvez [lire l'article](https://arxiv.org/abs/1602.04938) et [consulter le dépôt sur GitHub](https://github.com/marcotcr/lime).

Si vous travaillez avec le NLP et le Deep Learning, consultez également [AllenNLP](https://allennlp.org/tutorials).

Tout le code de cet article peut être trouvé [ici](https://github.com/dmesquita/explaining_predictions_with_LIME). Et merci pour la lecture ! ?

Si vous avez trouvé cet article utile, cela signifierait beaucoup si vous cliquez sur le ?? et le partagez sur le web.

Suivez-moi pour plus d'articles sur la Data Science et le Machine Learning.