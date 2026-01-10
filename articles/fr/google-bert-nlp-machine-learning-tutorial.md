---
title: Tutoriel Google BERT NLP Machine Learning
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-27T16:29:34.000Z'
originalURL: https://freecodecamp.org/news/google-bert-nlp-machine-learning-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/BERT-Tutorial.png
tags:
- name: Google
  slug: google
- name: Machine Learning
  slug: machine-learning
- name: nlp
  slug: nlp
seo_title: Tutoriel Google BERT NLP Machine Learning
seo_desc: "By Milecia McGregor\nThere are plenty of applications for machine learning,\
  \ and one of those is natural language processing or NLP. \nNLP handles things like\
  \ text responses, figuring out the meaning of words within context, and holding\
  \ conversations wi..."
---

Par Milecia McGregor

Il existe de nombreuses applications pour le machine learning, et l'une d'entre elles est le traitement du langage naturel ou NLP.

Le NLP gère des choses comme les réponses textuelles, la compréhension de la signification des mots dans leur contexte, et la tenue de conversations avec nous. Il aide les ordinateurs à comprendre le langage humain afin que nous puissions communiquer de différentes manières.

Des chatbots aux candidatures pour des emplois, en passant par le tri de vos emails dans différents dossiers, le NLP est utilisé partout autour de nous.

À sa base, le traitement du langage naturel est un mélange d'informatique et de linguistique. La linguistique nous donne les règles à utiliser pour entraîner nos modèles de machine learning et obtenir les résultats que nous recherchons.

Il y a de nombreuses raisons pour lesquelles le traitement du langage naturel est devenu une partie importante du machine learning. Il aide les machines à détecter le sentiment à partir des retours des clients, il peut aider à trier les tickets de support pour les projets sur lesquels vous travaillez, et il peut lire et comprendre le texte de manière cohérente.

Et comme il fonctionne à partir d'un ensemble de règles linguistiques, il n'a pas les mêmes biais qu'un humain.

Puisque le NLP est un domaine d'étude si vaste, il existe un certain nombre d'outils que vous pouvez utiliser pour analyser les données à vos fins spécifiques.

Il y a l'approche basée sur les règles où vous configurez beaucoup d'instructions si-alors pour gérer la manière dont le texte est interprété. Habituellement, un linguiste sera responsable de cette tâche et ce qu'il produit est très facile à comprendre pour les gens.

Cela peut être bien pour commencer, mais cela devient très complexe lorsque vous commencez à travailler avec de grands ensembles de données.

Une autre approche consiste à utiliser le machine learning où vous n'avez pas besoin de définir des règles. Cela est idéal lorsque vous essayez d'analyser rapidement et avec précision de grandes quantités de données.

Choisir le bon algorithme pour que l'approche de machine learning fonctionne est important en termes d'efficacité et de précision. Il existe des algorithmes courants comme [Naïve Bayes](https://scikit-learn.org/stable/modules/naive_bayes.html) et [Support Vector Machines](https://www.freecodecamp.org/news/svm-machine-learning-tutorial-what-is-the-support-vector-machine-algorithm-explained-with-code-examples/). Ensuite, il y a des algorithmes plus spécifiques comme Google BERT.

## Qu'est-ce que BERT ?

BERT est une bibliothèque open-source créée en 2018 chez Google. C'est une nouvelle technique pour le NLP et elle adopte une approche complètement différente pour entraîner les modèles que toute autre technique.

BERT est un acronyme pour Bidirectional Encoder Representations from Transformers. Cela signifie que, contrairement à la plupart des techniques qui analysent les phrases de gauche à droite ou de droite à gauche, BERT fonctionne dans les deux directions en utilisant le [Transformer encoder](https://arxiv.org/pdf/1706.03762.pdf). Son objectif est de générer un modèle de langage.

Cela lui confère une incroyable précision et performance sur des ensembles de données plus petits, ce qui résout un énorme problème en traitement du langage naturel.

Bien qu'il existe une énorme quantité de données textuelles disponibles, très peu d'entre elles ont été étiquetées pour être utilisées pour entraîner un modèle de machine learning. Puisque la plupart des approches des problèmes de NLP tirent parti du deep learning, vous avez besoin de grandes quantités de données pour l'entraînement.

Vous voyez vraiment les énormes améliorations dans un modèle lorsqu'il a été entraîné avec des millions de points de données. Pour aider à contourner ce problème de manque de données étiquetées, les chercheurs ont trouvé des moyens d'entraîner des modèles de représentation de langage à usage général par pré-entraînement en utilisant du texte provenant d'Internet.

Ces modèles de représentation pré-entraînés peuvent ensuite être affinés pour travailler sur des ensembles de données spécifiques qui sont plus petits que ceux couramment utilisés en deep learning. Ces ensembles de données plus petits peuvent être pour des problèmes comme l'analyse de sentiment ou la détection de spam. C'est ainsi que la plupart des problèmes de NLP sont abordés car cela donne des résultats plus précis que de commencer avec l'ensemble de données plus petit.

C'est pourquoi BERT est une si grande découverte. Il fournit un moyen de pré-entraîner vos modèles plus précisément avec moins de données. L'approche bidirectionnelle qu'il utilise signifie qu'il obtient plus de contexte pour un mot que s'il était simplement entraîné dans une seule direction. Avec ce contexte supplémentaire, il est capable de tirer parti d'une autre technique appelée masked LM.

## Comment il est différent des autres algorithmes de machine learning

Masked LM masque aléatoirement 15 % des mots dans une phrase avec un jeton [MASK] puis essaie de les prédire en fonction des mots entourant le mot masqué. C'est ainsi que BERT est capable de regarder les mots de gauche à droite et de droite à gauche.

Cela est complètement différent de tous les autres modèles de langage existants car il regarde les mots avant et après un mot masqué en même temps. Une grande partie de la précision de BERT peut être attribuée à cela.

Pour faire fonctionner BERT avec votre ensemble de données, vous devez ajouter un peu de métadonnées. Il devra y avoir des **token embeddings** pour marquer le début et la fin des phrases. Vous aurez besoin d'avoir des **segment embeddings** pour pouvoir distinguer différentes phrases. Enfin, vous aurez besoin de **positional embeddings** pour indiquer la position des mots dans une phrase.

Cela ressemblera à ceci.

```
[CLS] the [MASK] has blue spots [SEP] it rolls [MASK] the parking lot [SEP]
```

Avec les métadonnées ajoutées à vos points de données, masked LM est prêt à fonctionner.

Une fois qu'il a terminé de prédire les mots, BERT tire parti de la prédiction de la phrase suivante. Cela examine la relation entre deux phrases. Il le fait pour mieux comprendre le contexte de l'ensemble de données entier en prenant une paire de phrases et en prédisant si la deuxième phrase est la phrase suivante en fonction du texte original.

Pour que la prédiction de la phrase suivante fonctionne dans la technique BERT, la deuxième phrase est envoyée à travers le [modèle basé sur le Transformer](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html).

Il existe quatre versions pré-entraînées différentes de BERT en fonction de l'échelle des données avec lesquelles vous travaillez. Vous pouvez en apprendre plus sur elles ici : [https://github.com/google-research/bert#bert](https://github.com/google-research/bert#bert)

L'inconvénient de cette approche est que la fonction de perte ne considère que les prédictions de mots masqués et non les prédictions des autres. Cela signifie que la technique BERT converge plus lentement que les autres techniques de droite à gauche ou de gauche à droite.

BERT peut être appliqué à n'importe quel problème de NLP auquel vous pouvez penser, y compris la prédiction d'intention, les applications de questions-réponses et la classification de texte.

## Exemple de code

### Installation

Maintenant, nous allons passer par un exemple de BERT en action. La première chose que vous devrez faire est de cloner le dépôt Bert.

```
git clone https://github.com/google-research/bert.git
```

Maintenant, vous devez télécharger les fichiers du modèle BERT pré-entraîné depuis la [page GitHub de BERT](https://github.com/google-research/bert#pre-trained-models). Tout au long du reste de ce tutoriel, je ferai référence au répertoire de ce dépôt comme le répertoire racine.

Ces fichiers vous donnent les hyper-paramètres, les poids et autres choses dont vous avez besoin avec les informations que Bert a apprises pendant le pré-entraînement. J'utiliserai le [modèle BERT-Base, Uncased](https://storage.googleapis.com/bert_models/2018_10_18/uncased_L-12_H-768_A-12.zip), mais vous trouverez plusieurs autres options dans différentes langues sur la page GitHub.

Certaines raisons pour lesquelles vous choisirez le modèle BERT-Base, Uncased sont si vous n'avez pas accès à un TPU Google, auquel cas vous choisirez généralement un modèle Base.

Si vous pensez que la casse du texte que vous essayez d'analyser est sensible à la casse (la casse du texte donne une signification contextuelle réelle), alors vous opterez pour un modèle Cased.

Si la casse n'est pas importante ou si vous n'êtes pas tout à fait sûr, alors un modèle Uncased serait un choix valide.

Nous travaillerons avec des avis Yelp comme ensemble de données. N'oubliez pas que BERT attend les données dans un certain format en utilisant ces **token embeddings** et autres. Nous devrons les ajouter à un fichier .tsv. Ce fichier sera similaire à un .csv, mais il aura quatre colonnes et aucune ligne d'en-tête.

Voici à quoi ressembleront les quatre colonnes.

* Colonne 0 : ID de ligne
* Colonne 1 : Libellé de ligne (doit être un entier)
* Colonne 2 : Une colonne de la même lettre pour toutes les lignes (elle n'est utilisée pour rien, mais BERT l'attend)
* Colonne 3 : Le texte que nous voulons classer

Vous devrez créer un dossier appelé data dans le répertoire où vous avez cloné BERT et y ajouter trois fichiers : _train.tsv, dev.tsv, test.tsv_.

Dans les fichiers _train.tsv_ et _dev.tsv_, nous aurons les quatre colonnes dont nous avons parlé précédemment. Dans le fichier _test.tsv_, nous n'aurons que l'ID de ligne et le texte que nous voulons classer comme colonnes. Ce sont les fichiers de données que nous utiliserons pour entraîner et tester notre modèle.

### Préparation des données

Tout d'abord, nous devons obtenir les données avec lesquelles nous allons travailler. Vous pouvez télécharger les avis Yelp vous-même ici : https://course.fast.ai/datasets#nlp. Cela se trouvera dans la section NLP et vous voudrez la version Polarity.

La raison pour laquelle nous travaillerons avec cette version est que les données ont déjà une polarité, ce qui signifie qu'elles ont déjà un sentiment associé. Enregistrez ce fichier dans le répertoire des données.

Maintenant que nous sommes prêts à commencer à écrire du code. Créez un nouveau fichier dans le répertoire racine appelé _pre_processing.py_ et ajoutez le code suivant.

```python
import pandas as pd
# ceci est pour extraire les données de ce fichier .tgz
import tarfile
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# obtenir toutes les données de ce .tgz
yelp_reviews = tarfile.open('data/yelp_review_polarity_csv.tgz')
yelp_reviews.extractall('data')
yelp_reviews.close()

# jeter un coup d'œil à ce à quoi ressemblent les données avant de commencer
# regarder l'ensemble de données d'entraînement
train_df = pd.read_csv('data/yelp_review_polarity_csv/train.csv', header=None)
print(train_df.head())

# regarder l'ensemble de données de test
test_df = pd.read_csv('data/yelp_review_polarity_csv/test.csv', header=None)
print(test_df.head())
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-44.png)

Dans ce code, nous avons importé quelques packages Python et décompressé les données pour voir à quoi ressemblent les données. Vous remarquerez que les valeurs associées aux avis sont 1 et 2, avec 1 étant un mauvais avis et 2 étant un bon avis. Nous devons convertir ces valeurs en libellés plus standard, donc 0 et 1. Vous pouvez faire cela avec le code suivant.

```python
train_df[0] = (train_df[0] == 2).astype(int)
test_df[0] = (test_df[0] == 2).astype(int)
```

Chaque fois que vous apportez des mises à jour à vos données, il est toujours important de vérifier si les choses se sont bien passées. Nous allons donc faire cela avec les commandes suivantes.

```python
print(train_df.head())
print(test_df.head())
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/image-45.png)

Lorsque vous voyez que vos valeurs de polarité ont changé pour être ce que vous attendiez. Maintenant, les données devraient avoir des 1 et des 0.

Puisque nous avons nettoyé les données initiales, il est temps de préparer les choses pour BERT. Nous devrons faire en sorte que nos données correspondent aux formats de colonnes dont nous avons parlé précédemment. Commençons par les données d'entraînement.

Les données d'entraînement auront les quatre colonnes : id de ligne, libellé de ligne, lettre unique, texte que nous voulons classer.

BERT attend deux fichiers pour l'entraînement appelés _train_ et _dev_. Nous créerons ces fichiers en divisant le fichier d'entraînement initial en deux fichiers après avoir formaté nos données avec les commandes suivantes.

```python
bert_df = pd.DataFrame({
    'id': range(len(train_df)),
    'label': train_df[0],
    'alpha': ['q']*train_df.shape[0],
    'text': train_df[1].replace(r'\n', ' ', regex=True)
})

train_bert_df, dev_bert_df = train_test_split(bert_df, test_size=0.01)
```

Avec la variable _bert_df_, nous avons formaté les données pour qu'elles soient ce que BERT attend. Vous pouvez choisir une autre lettre pour la valeur alpha si vous le souhaitez. La méthode _train_test_split_ que nous avons importée au début gère la division des données d'entraînement en les deux fichiers dont nous avons besoin.

Jetez un coup d'œil à la manière dont les données ont été formatées avec cette commande.

```python
print(train_bert_df.head())
```

Maintenant, nous devons formater les données de test. Cela sera différent de la manière dont nous avons traité les données d'entraînement. BERT n'attend que deux colonnes pour les données de test : id de ligne, texte que nous voulons classer. Nous n'avons pas besoin de faire autre chose avec les données de test une fois que nous les avons dans ce format et nous le ferons avec la commande suivante.

```python
test_bert_df = pd.DataFrame({
    'id': range(len(test_df)),
    'text': test_df[1].replace(r'\n', ' ', regex=True)
})
```

C'est similaire à ce que nous avons fait avec les données d'entraînement, juste sans deux des colonnes. Jetez un coup d'œil aux nouvelles données de test formatées.

```python
test_bert_df.head()
```

Si tout semble bon, vous pouvez enregistrer ces variables sous forme de fichiers .tsv avec lesquels BERT travaillera.

```python
train_bert_df.to_csv('data/train.tsv', sep='\t', index=False, header=False)
dev_bert_df.to_csv('data/dev.tsv', sep='\t', index=False, header=False)
test_bert_df.to_csv('data/test.tsv', sep='\t', index=False, header=False)
```

### Entraînement du modèle

Une petite note avant de nous lancer dans l'entraînement du modèle : BERT peut être très gourmand en ressources sur les ordinateurs portables. Cela peut provoquer des erreurs de mémoire car il n'y a pas assez de RAM ou un autre matériel n'est pas assez puissant. Vous pourriez essayer de rendre le _training_batch_size_ plus petit, mais cela va rendre l'entraînement du modèle vraiment lent.

Ajoutez un dossier au répertoire racine appelé _model_output_. C'est là que notre modèle sera enregistré après la fin de l'entraînement. Maintenant, ouvrez un terminal et allez dans le répertoire racine de ce projet. Une fois que vous êtes dans le bon répertoire, exécutez la commande suivante et cela commencera à entraîner votre modèle.

```bash
python run_classifier.py --task_name=cola --do_train=true --do_eval=true --data_dir=./data/ --vocab_file=./uncased_L-12_H-768_A-12/vocab.txt --bert_config_file=./uncased_L-12_H-768_A-12/bert_config.json --init_checkpoint=./uncased_L-12_H768_A-12/bert_model.ckpt.index --max_seq_length=128 --train_batch_size=32 --learning_rate=2e-5 --num_train_epochs=3.0 --output_dir=./model_output --do_lower_case=False
```

Vous devriez voir un certain résultat défiler dans votre terminal. Une fois que cela a fini de s'exécuter, vous aurez un modèle entraîné prêt à faire des prédictions !

### Faire une prédiction

Si vous jetez un coup d'œil dans le répertoire _model_output_, vous remarquerez qu'il y a un tas de fichiers _model.ckpt_. Ces fichiers contiennent les poids pour le modèle entraîné à différents moments pendant l'entraînement, donc vous voulez trouver celui avec le numéro le plus élevé. Ce sera le modèle entraîné final que vous voudrez utiliser.

Maintenant, nous allons exécuter _run_classifier.py_ à nouveau avec des options légèrement différentes. En particulier, nous allons changer la valeur _init_checkpoint_ pour le point de contrôle du modèle le plus élevé et définir une nouvelle valeur _--do_predict_ à true. Voici la commande que vous devez exécuter dans votre terminal.

```bash
python run_classifier.py --task_name=cola --do_predict=true --data_dir=./data --vocab_file=./uncased_L-12_H-768-A-12/bert_config.json --init_checkpoint=./model_output/model.ckpt-<highest checkpoint number> --max_seq_length=128 --output_dir=./model_output
```

Une fois la commande terminée, vous devriez voir un nouveau fichier appelé _test_results.tsv_. Cela contiendra vos résultats prédits basés sur le modèle que vous avez entraîné !

Vous venez d'utiliser BERT pour analyser des données réelles et, espérons-le, tout cela avait du sens.

## Autres réflexions

J'ai jugé nécessaire de passer par le processus de nettoyage des données ici au cas où quelqu'un ne l'aurait pas encore fait. Parfois, le machine learning semble magique, mais il s'agit vraiment de prendre le temps de mettre vos données dans le bon état pour les entraîner avec un algorithme.

BERT est encore relativement nouveau puisqu'il n'a été publié qu'en 2018, mais il s'est jusqu'à présent avéré plus précis que les modèles existants, même s'il est plus lent.