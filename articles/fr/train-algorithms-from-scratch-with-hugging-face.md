---
title: Comment entraîner les tokenizers BPE, WordPiece et Unigram à partir de zéro
  en utilisant Hugging Face
subtitle: ''
author: Harshit Tyagi
co_authors: []
series: null
date: '2021-10-18T22:27:40.000Z'
originalURL: https://freecodecamp.org/news/train-algorithms-from-scratch-with-hugging-face
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/tok_hf.png
tags:
- name: algorithms
  slug: algorithms
- name: Machine Learning
  slug: machine-learning
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: Comment entraîner les tokenizers BPE, WordPiece et Unigram à partir de
  zéro en utilisant Hugging Face
seo_desc: 'If you''ve had some experience with NLP, you probably know that tokenization
  is at the helm of any NLP pipeline.

  Tokenization is often regarded as a subfield of NLP but it has its own story of
  evolution. And now it underpins many state-of-the-art NLP ...'
---

Si vous avez déjà une certaine expérience en NLP, vous savez probablement que la tokenization est au cœur de tout pipeline NLP.

La tokenization est souvent considérée comme un sous-domaine du NLP, mais elle a sa propre [histoire d'évolution](https://dswharshit.substack.com/p/the-evolution-of-tokenization-byte). Et maintenant, elle sous-tend de nombreux modèles NLP de pointe.

Cet article traite de l'entraînement des tokenizers à partir de zéro en utilisant le **package de tokenizers de Hugging Face**.

Avant de passer à la partie amusante de l'entraînement et de la comparaison des différents tokenizers, je veux vous donner un bref résumé des principales différences entre les algorithmes.

La principale différence réside dans le **choix des paires de caractères** à fusionner et **la politique de fusion** que chacun de ces algorithmes utilise pour générer l'ensemble final de tokens.

## Algorithme BPE – un modèle basé sur la fréquence

Le Byte Pair Encoding utilise la fréquence des motifs de sous-mots pour les présélectionner en vue de la fusion.

L'inconvénient d'utiliser la fréquence comme facteur principal est que vous pouvez obtenir des encodages finaux ambigus qui pourraient ne pas être utiles pour le nouveau texte d'entrée.

Mais il offre encore la possibilité de s'améliorer en termes de génération de tokens non ambigus.

## Algorithme Unigram – un modèle basé sur la probabilité

Ensuite, nous avons le modèle Unigram qui aborde le problème de fusion en calculant la probabilité de chaque combinaison de sous-mots plutôt qu'en choisissant le motif le plus fréquent.

Il calcule la probabilité de chaque token de sous-mot et le supprime ensuite en fonction d'une fonction de perte expliquée dans [cet article de recherche](https://arxiv.org/pdf/1804.10959.pdf).

Sur la base d'un certain seuil de la valeur de perte, vous pouvez ensuite déclencher le modèle pour supprimer les 20-30 % inférieurs des tokens de sous-mots.

Unigram est un algorithme entièrement probabiliste qui choisit à la fois les paires de caractères et la décision finale de fusion (ou non) à chaque itération en fonction de la probabilité.

## Algorithme WordPiece

Avec la sortie de BERT en 2018, un nouvel algorithme de tokenization de sous-mots appelé WordPiece est apparu, qui peut être considéré comme un intermédiaire entre les algorithmes BPE et Unigram.

WordPiece est également un algorithme glouton qui utilise la probabilité plutôt que la fréquence de comptage pour fusionner la meilleure paire à chaque itération, mais le choix des caractères à apparier est basé sur la fréquence de comptage.

Ainsi, il est similaire à BPE en termes de choix des caractères à apparier et similaire à Unigram en termes de choix de la meilleure paire à fusionner.

Les différences algorithmiques étant couvertes, j'ai essayé de mettre en œuvre chacun de ces algorithmes (pas à partir de zéro) pour comparer la sortie générée par chacun d'eux.

## Comment entraîner les algorithmes BPE, Unigram et WordPiece

Maintenant, afin d'avoir une comparaison impartiale des sorties, je ne voulais pas utiliser des algorithmes pré-entraînés, car cela introduirait la taille, la qualité et le contenu du jeu de données dans l'équation.

Une solution pourrait être de coder ces algorithmes à partir de zéro en utilisant les articles de recherche, puis de les tester. C'est une bonne approche pour vraiment comprendre le fonctionnement de chaque algorithme, mais vous pourriez passer des semaines à le faire.

J'ai plutôt utilisé le **package de tokenizers de Hugging Face** qui offre l'implémentation de tous les tokenizers les plus utilisés aujourd'hui. Il m'a également permis d'entraîner ces modèles à partir de zéro sur mon choix de jeu de données, puis de tokenizer la chaîne d'entrée de mon choix.

### Comment entraîner les jeux de données

J'ai choisi deux jeux de données différents pour entraîner ces modèles. L'un est un livre gratuit de Gutenberg qui sert de petit jeu de données, et l'autre est le [wikitext-103](https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/) qui contient 516 Mo de texte.

Dans le Colab, vous pouvez d'abord télécharger les jeux de données et les décompresser (si nécessaire) :

```javascript
!wget http://www.gutenberg.org/cache/epub/16457/pg16457.txt
```

```javascript
!wget https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-103-raw-v1.zip
```

```javascript
!unzip wikitext-103-raw-v1.zip
```

### Importer les modèles et entraîneurs requis

En parcourant la documentation, vous trouverez que l'API principale du package est la classe `Tokenizer`.

Vous pouvez ensuite instancier n'importe quel tokenizer avec le modèle de votre choix (BPE/Unigram/WordPiece).

Ici, j'ai importé la classe principale, tous les modèles que je voulais tester, et leurs entraîneurs, car je veux entraîner ces modèles à partir de zéro.

```javascript
## importation du tokenizer et de l'entraîneur de sous-mots BPE
from tokenizers import Tokenizer
from tokenizers.models import BPE, Unigram, WordLevel, WordPiece
from tokenizers.trainers import BpeTrainer, WordLevelTrainer, \
                                WordPieceTrainer, UnigramTrainer

## un pré-tokenizer pour segmenter le texte en mots
from tokenizers.pre_tokenizers import Whitespace
```

### Comment automatiser l'entraînement et la tokenization

Puisque je dois effectuer des processus quelque peu similaires pour trois modèles différents, j'ai divisé les processus en 3 fonctions. Je n'aurai besoin d'appeler ces fonctions pour chaque modèle et mon travail sera terminé.

Alors, quelles sont ces fonctions ?

#### Étape 1 - Préparer le tokenizer

La préparation du tokenizer nécessite d'instancier la classe Tokenizer avec un modèle de notre choix. Mais puisque nous avons quatre modèles (j'ai également ajouté un algorithme simple de niveau mot) à tester, nous allons écrire des cas if/else pour instancier le tokenizer avec le bon modèle.

Pour entraîner le tokenizer instancié sur les petits et grands jeux de données, nous devrons également instancier un entraîneur, dans notre cas, ce seront [`BpeTrainer`](https://huggingface.co/docs/tokenizers/python/latest/api/reference.html#tokenizers.trainers.BpeTrainer)`, WordLevelTrainer, WordPieceTrainer, et UnigramTrainer.`

L'instanciation et l'entraînement nécessiteront de spécifier certains tokens spéciaux. Ce sont des tokens pour les mots inconnus et d'autres tokens spéciaux que nous devrons utiliser plus tard pour ajouter à notre vocabulaire.

Vous pouvez également spécifier d'autres arguments d'entraînement, comme la taille du vocabulaire ou la fréquence minimale ici.

```javascript
unk_token = "<UNK>"  # token pour les mots inconnus
spl_tokens = ["<UNK>", "<SEP>", "<MASK>", "<CLS>"]  # tokens spéciaux

def prepare_tokenizer_trainer(alg):
    """
    Prépare le tokenizer et l'entraîneur avec des tokens inconnus et spéciaux.
    """
    if alg == 'BPE':
        tokenizer = Tokenizer(BPE(unk_token = unk_token))
        trainer = BpeTrainer(special_tokens = spl_tokens)
    elif alg == 'UNI':
        tokenizer = Tokenizer(Unigram())
        trainer = UnigramTrainer(unk_token= unk_token, special_tokens = spl_tokens)
    elif alg == 'WPC':
        tokenizer = Tokenizer(WordPiece(unk_token = unk_token))
        trainer = WordPieceTrainer(special_tokens = spl_tokens)
    else:
        tokenizer = Tokenizer(WordLevel(unk_token = unk_token))
        trainer = WordLevelTrainer(special_tokens = spl_tokens)
    
    tokenizer.pre_tokenizer = Whitespace()
    return tokenizer, trainer
```

Nous aurons également besoin d'ajouter un pré-tokenizer pour diviser notre entrée en mots, car sans pré-tokenizer, nous pourrions obtenir des tokens qui chevauchent plusieurs mots : par exemple, nous pourrions obtenir un token `"there is"` puisque ces deux mots apparaissent souvent côte à côte.

> *L'utilisation d'un pré-tokenizer garantira qu'aucun token n'est plus grand qu'un mot retourné par le pré-tokenizer.*

Cette fonction retournera le tokenizer et son objet entraîneur que nous pouvons utiliser pour entraîner le modèle sur un jeu de données.

Ici, nous utilisons le même pré-tokenizer (`Whitespace`) pour tous les modèles. Vous pouvez choisir de le tester avec [d'autres](https://huggingface.co/docs/tokenizers/python/latest/api/reference.html#module-tokenizers.pre_tokenizers).

#### Étape 2 - Entraîner le tokenizer

Après avoir préparé les tokenizers et les entraîneurs, nous pouvons commencer le processus d'entraînement.

Voici une fonction qui prendra les fichiers sur lesquels nous avons l'intention d'entraîner notre tokenizer ainsi que l'identifiant de l'algorithme.

* `'WLV'` - Algorithme de niveau mot

* `'WPC'` - Algorithme WordPiece

* `'BPE'` - Byte Pair Encoding

* `'UNI'` - Unigram

```javascript
def train_tokenizer(files, alg='WLV'):
    """
    Prend les fichiers et entraîne le tokenizer.
    """
    tokenizer, trainer = prepare_tokenizer_trainer(alg)
    tokenizer.train(files, trainer) # entraînement du tokenizer
    tokenizer.save("./tokenizer-trained.json")
    tokenizer = Tokenizer.from_file("./tokenizer-trained.json")
    return tokenizer
```

C'est la fonction principale que nous devrons appeler pour entraîner le tokenizer. Elle préparera d'abord le tokenizer et l'entraîneur, puis commencera à entraîner les tokenizers avec les fichiers fournis.

Après l'entraînement, elle sauvegarde le modèle dans un fichier JSON, le charge à partir du fichier et retourne le tokenizer entraîné pour commencer à encoder la nouvelle entrée.

#### Étape 3 - Tokenizer la chaîne d'entrée

La dernière étape consiste à commencer à encoder les nouvelles chaînes d'entrée et à comparer les tokens générés par chaque algorithme.

Ici, nous allons écrire une boucle for imbriquée pour entraîner chaque modèle d'abord sur le jeu de données plus petit, puis sur le jeu de données plus grand, et tokenizer la chaîne d'entrée également.

**Chaîne d'entrée -** "This is a deep learning tokenization tutorial. Tokenization is the first step in a deep learning NLP pipeline. We will be comparing the tokens generated by each tokenization model. Excited much?!😍"

```javascript
small_file = ['pg16457.txt']
large_files = [f"./wikitext-103-raw/wiki.{split}.raw" for split in ["test", "train", "valid"]]

for files in [small_file, large_files]:
    print(f"========Using vocabulary from {files}=======")
    for alg in ['WLV', 'BPE', 'UNI', 'WPC']:
        trained_tokenizer = train_tokenizer(files, alg)
        input_string = "This is a deep learning tokenization tutorial. Tokenization is the first step in a deep learning NLP pipeline. We will be comparing the tokens generated by each tokenization model. Excited much?!😍"
        output = tokenize(input_string, trained_tokenizer)
        tokens_dict[alg] = output.tokens
        print("----", alg, "----")
        print(output.tokens, "->", len(output.tokens))
```

**Et voici la sortie :**

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F43eb1a88-36a1-4343-be1e-ac65843e3837_1306x430.png align="left")

## Analyse de la sortie :

En regardant la sortie, vous verrez la différence dans la manière dont les tokens ont été générés, ce qui a conduit à un nombre différent de tokens générés.

* Un simple **algorithme de niveau mot** a créé 35 tokens, peu importe le jeu de données sur lequel il a été entraîné.

* L'algorithme **BPE** a créé 55 tokens lorsqu'il a été entraîné sur un jeu de données plus petit et 47 lorsqu'il a été entraîné sur un jeu de données plus grand. Cela montre qu'il a été capable de fusionner plus de paires de caractères lorsqu'il a été entraîné sur un jeu de données plus grand.

* Le **modèle Unigram** a créé un nombre similaire (68 et 67) de tokens avec les deux jeux de données. Mais vous pouvez voir la différence dans les tokens générés :

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fbdf3d128-641c-4680-9b43-0e04a505d67c_428x43.png align="left")

Avec un jeu de données plus grand, la fusion s'est rapprochée de la génération de tokens mieux adaptés pour encoder les mots de la langue anglaise du monde réel que nous utilisons souvent.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Feb49063b-8896-496e-acec-0dea60d6ea37_260x40.png align="left")

**WordPiece** a créé 52 tokens lorsqu'il a été entraîné sur un jeu de données plus petit et 48 lorsqu'il a été entraîné sur un jeu de données plus grand. Les tokens générés ont un double ## pour indiquer l'utilisation d'un token comme préfixe/suffixe.

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5225119-6158-45e7-83b1-26bf587791f3_391x45.png align="left")

Les trois algorithmes ont généré des tokens de sous-mots meilleurs et moins bons lorsqu'ils ont été entraînés sur un jeu de données plus grand.

## Comment comparer les tokens

Pour comparer les tokens, j'ai stocké la sortie de chaque algorithme dans un dictionnaire et je vais le transformer en un dataframe pour mieux visualiser les différences entre les tokens.

Puisque le nombre de tokens générés par chaque modèle est différent, j'ai ajouté un token pour rendre les données rectangulaires et les adapter à un dataframe.

est essentiellement nan dans le dataframe.

```javascript
import pandas as pd

max_len = max(len(tokens_dict['UNI']), len(tokens_dict['WPC']), len(tokens_dict['BPE']))
diff_bpe = max_len - len(tokens_dict['BPE'])
diff_wpc = max_len - len(tokens_dict['WPC'])

tokens_dict['BPE'] = tokens_dict['BPE'] + ['<PAD>']*diff_bpe
tokens_dict['WPC'] = tokens_dict['WPC'] + ['<PAD>']*diff_wpc

del tokens_dict['WLV']

df = pd.DataFrame(tokens_dict)
df.head(10)
```

**Voici la sortie :**

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F856ab4bc-7343-4114-9867-27e64a71d21a_306x474.png align="left")

Vous pouvez également regarder la différence entre les tokens en utilisant des ensembles :

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7be68b1a-d979-4688-94e9-b19219f2259d_370x692.png align="left")

![Image](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8942a6e1-d1bc-4a6e-bbec-3473a87ef9ca_370x626.png align="left")

Pour consulter le code, rendez-vous sur ce [notebook Colab](https://colab.research.google.com/drive/10gwzRY55JqzgeEQOX6nwFs6bQ84-mB9f?usp=sharing).

## Réflexions finales et prochaines étapes

Sur la base des types de tokens générés, WPC semble générer des tokens de sous-mots plus couramment trouvés dans la langue anglaise – mais ne me tenez pas à cette observation.

Ces algorithmes sont légèrement différents les uns des autres et font un travail quelque peu similaire de développement d'un modèle NLP décent. Mais une grande partie de la performance dépend de l'utilisation de votre modèle de langage, de la taille du vocabulaire, de la vitesse et d'autres facteurs.

Cela conclut notre examen des algorithmes de tokenization. La prochaine étape pour approfondir ce sujet est de comprendre ce que sont les embeddings, comment la tokenization joue un rôle vital dans la création de ces embeddings et comment ils affectent les performances d'un modèle.

Une avancée supplémentaire de ces algorithmes est l'[algorithme SentencePiece](https://arxiv.org/pdf/1808.06226.pdf), qui est une approche globale du problème de tokenization. Mais une grande partie de ce problème est atténuée par HuggingFace, et encore mieux – ils ont tous les algorithmes implémentés dans un seul dépôt GitHub.

### Références et notes

Si vous avez des questions sur mon analyse ou sur mon travail dans cet article, je vous encourage vivement à consulter ces ressources pour une compréhension précise du fonctionnement de chaque algorithme :

1. [Subword regularization: Improving Neural Network Translation Models with Multiple Subword Candidates](https://arxiv.org/pdf/1804.10959.pdf) par Taku Kudo

2. [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/pdf/1508.07909.pdf) - Article de recherche qui discute des différentes techniques de segmentation basées sur l'algorithme de compression BPE.

3. [Package de tokenizers de Hugging Face](https://huggingface.co/docs/tokenizers/python/latest/quicktour.html).

### Me contacter

Si vous cherchez à vous lancer dans le domaine de la science des données ou du ML, consultez mon cours sur les [**Fondamentaux de la science des données et du ML**](https://www.wiplane.com/p/foundations-for-data-science-ml).

Si vous souhaitez voir plus de contenu de ce type et que vous n'êtes pas abonné, envisagez de vous abonner à [ma newsletter](https://dswharshit.substack.com/).

Vous avez quelque chose à ajouter ou à suggérer, vous pouvez me contacter via :

* [YouTube](https://www.youtube.com/channel/UCH-xwLTKQaABNs2QmGxK2bQ)

* [Twitter](https://twitter.com/dswharshit)

* [LinkedIn](https://www.linkedin.com/in/tyagiharshit/)