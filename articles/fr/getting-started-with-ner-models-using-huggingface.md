---
title: Comment affiner BERT pour la reconnaissance d'entités nommées (NER) en utilisant
  HuggingFace
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-31T15:42:18.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-ner-models-using-huggingface
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/pexels-digital-buggu-171198.jpg
tags:
- name: Machine Learning
  slug: machine-learning
seo_title: Comment affiner BERT pour la reconnaissance d'entités nommées (NER) en
  utilisant HuggingFace
seo_desc: "By Suchandra Datta\nI've always been fascinated with languages and the\
  \ inherent beauty of words. But I used to think that language comprehension was\
  \ an exclusive human trait. \nSo when machines started generating, understanding,\
  \ classifying, and summar..."
---

Par Suchandra Datta

J'ai toujours été fasciné par les langues et la beauté inhérente des mots. Mais je pensais que la compréhension du langage était une caractéristique exclusivement humaine. 

Alors, lorsque les machines ont commencé à générer, comprendre, classer et résumer du texte en utilisant les Transformers, j'étais enthousiaste à l'idée d'en apprendre davantage. Et je voulais apprendre à l'implémenter et à le voir en action. 

Dans cet article, je vais vous guider à travers les sujets suivants :

* comment affiner BERT pour les tâches de NER en utilisant HuggingFace
* comment configurer Weights and Biases pour MLOps
* comment écrire une carte de modèle et partager votre modèle sur Huggingface Model Hub

J'ai pu créer ce modèle dans le cadre d'un projet parallèle et le partager sur [https://huggingface.co/Suchandra/bengali_language_NER](https://huggingface.co/Suchandra/bengali_language_NER), grâce aux ressources merveilleuses que je vais lier ci-dessous :

* [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
* [The Illustrated BERT, ELMo, and co.](https://jalammar.github.io/illustrated-bert/)
* [HuggingFace docs](https://huggingface.co/)
* [Model Hub docs](https://huggingface.co/docs/hub/main)
* [Weights and Biases docs](https://wandb.ai/site)

C'est parti !

## Un bref aperçu des Transformers, des tokenizers et de BERT

### Tokenizers

La tokenization est le processus de division d'une entité plus grande en ses unités constituantes. De grands blocs de texte sont d'abord tokenisés afin qu'ils soient décomposés en un format plus facile à représenter, apprendre et comprendre pour les machines. 

Il existe différentes façons de tokeniser du texte, comme :

* la tokenization par caractères
* la tokenization par mots
* la tokenization par sous-mots

Par exemple, considérons le texte suivant :

```
The moon shone over laketown
```

* pour la tokenization par caractères, nous le représenterions comme une liste de caractères composants comme [ 'T', 'h','e','m','o','o','n','s','h','o','n','e','o','v','e','r','l','a','k','e','t','o','w','n' ] 
* pour la tokenization par mots, ce serait [ 'The', 'moon','shone','over','laketown']
* pour la tokenization par sous-mots, les mots fréquents resteraient les mêmes, les mots moins fréquents seraient divisés en mots plus fréquents comme ['The','moon','shone','over','lake','##town'] ici le mot plus rare "laketown" est divisé en mots qui apparaissent plus fréquemment — "lake" et "town". Les deux dièses avant town sont nécessaires pour indiquer que "town" n'est pas un mot en soi mais fait partie d'un mot plus grand.

Les algorithmes de tokenization par sous-mots les plus populaires utilisés dans les Transformers sont BPE et WordPiece. Voici un lien vers l'article pour [WordPiece](https://arxiv.org/pdf/1609.08144v2.pdf) et [BPE](https://arxiv.org/abs/1508.07909v5) pour plus d'informations. Super, maintenant notre texte d'entrée ressemble à ceci :

```
['The','moon','shone','over','lake','##town']
```

Et maintenant ? Comment cela aura-t-il du sens pour une machine ? Entrez les transformers.

### Transformers et BERT

Les Transformers sont une architecture particulière pour les modèles de deep learning qui ont révolutionné le traitement du langage naturel. 

La caractéristique déterminante d'un Transformer est le mécanisme d'auto-attention. Grâce à lui, chaque mot apprend à quel point il est lié aux autres mots d'une séquence. 

Par exemple, dans l'exemple de texte de la section précédente, le mot 'the' se réfère au mot 'moon' donc le score d'attention pour 'the' et 'moon' serait élevé, tandis qu'il serait moins élevé pour des paires de mots comme 'the' et 'over'. 

Pour une description complète des formules nécessaires pour calculer le score d'attention et la sortie, vous pouvez lire l'article [ici](https://paperswithcode.com/paper/attention-is-all-you-need).

Voici un exemple simplifié de la façon dont tout cela fonctionne ensemble. Nous avons notre entrée :

```
['The','moon','shone','over','lake','##town']
```

Chaque token est représenté comme un vecteur. Donc disons que 'the' est représenté comme [0.1,0.2,1.3,-2.4,0.05] avec une taille arbitraire de 5. Le modèle ne sait pas encore quelles doivent être les valeurs du vecteur, donc il initialise avec quelques valeurs aléatoires. 

Ensuite, il commence à apprendre les relations entre les mots en utilisant l'architecture Transformer et continue à mettre à jour les valeurs des vecteurs jusqu'à ce qu'il puisse effectuer la classification avec la précision souhaitée. 

Et maintenant, nous passons à BERT, qui est une architecture de modèle basée sur les Transformers. Il utilise un grand corpus de texte pour apprendre comment mieux représenter les tokens et effectuer des tâches en aval comme la classification de texte, la classification de tokens, et ainsi de suite. 

## Le jeu de données du projet

La reconnaissance d'entités nommées (NER) consiste à identifier les labels auxquels chaque mot d'une phrase appartient. 

Par exemple, dans la phrase "La semaine dernière, Gandalf a visité la Comté", nous pouvons considérer les entités comme étant "Gandalf" avec le label "Personne" et "Comté" avec le label "Lieu". 

Pour construire un modèle qui effectuera cette tâche, nous avons d'abord besoin d'un jeu de données. Nous utiliserons le jeu de données WikiANN pour la langue bengali, qui est facilement disponible via le module datasets de HuggingFace. 

Il inclut plusieurs langues, où les mots sont annotés avec des labels comme lieu (LOC), organisation (ORG) et personne (PER). Voici un [lien vers la carte du jeu de données](https://huggingface.co/datasets/wikiann) pour plus d'informations.

## Le modèle pour l'affinage

Nous utiliserons le modèle BERT base multilingue, spécifiquement la version avec casse. J'ai commencé avec la version sans casse, ce que j'ai réalisé plus tard être une erreur. 

J'ai rapidement découvert que si j'encode un mot puis le décode, j'obtiens bien le mot original mais l'orthographe du mot décodé a changé. 

Il s'avère que la version sans casse rencontre des problèmes de normalisation qui pourraient expliquer ce comportement. De tels problèmes sont résolus dans la version avec casse, comme décrit dans le dépôt officiel GitHub [ici](https://github.com/google-research/bert/blob/master/multilingual.md). 

## Comment charger le jeu de données

Tout d'abord, installons tous les modules principaux dont nous avons besoin depuis HuggingFace. Voici comment faire sur Jupyter :

```python
!pip install datasets
!pip install tokenizers
!pip install transformers
```

Ensuite, nous chargeons le jeu de données comme ceci :

```python
from datasets import load_dataset

dataset = load_dataset("wikiann", "bn")
```

Et enfin, inspectons les noms des labels :

```python
label_names = dataset["train"].features["ner_tags"].feature.names

```

## Comment prétraiter le jeu de données

Pour chaque échantillon, nous devons obtenir les valeurs pour `input_ids`, `token_type_ids` et `attention_mask` ainsi qu'ajuster les labels. 

Pourquoi est-il nécessaire d'ajuster les labels ? Eh bien, les modèles BERT utilisent la tokenization par sous-mots, où les tokens fréquents sont regroupés en un seul token et les tokens rares sont décomposés en tokens fréquents. 

Par exemple, disons que nous avons un nom "Johnpeter". Il serait divisé en mots plus fréquents comme "John" et "##peter". Mais "Johnpeter" n'a qu'un seul label dans le jeu de données qui est "B-PER". Donc après la tokenization, les labels ajustés seraient "B-PER" pour "John" et à nouveau "B-PER" pour "##peter". 

Le code ci-dessous encode d'abord tous les échantillons pour chaque division d'entraînement, de test et de validation. Ensuite, il utilise word_ids, qui est une liste avec des index répétés pour chaque mot qui est divisé comme word_ids = [0,0,0,1,2,3,3]. Cela signifie que le mot à l'index 0 est divisé en 3 tokens, le mot à l'index 3 est divisé en 2 tokens. Donc nous répétons les labels dans adjusted_label_ids jusqu'à ce qu'un changement d'index se produise. 

```python
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

#Obtenir les valeurs pour input_ids, token_type_ids, attention_mask
def tokenize_adjust_labels(all_samples_per_split):
  tokenized_samples = tokenizer.batch_encode_plus(all_samples_per_split["tokens"], is_split_into_words=True)
  #tokenized_samples n'est pas un objet datasets donc cela seul ne fonctionnera pas avec l'API Trainer, d'où l'utilisation de map 
  #donc les nouvelles clés [input_ids, labels (après ajustement)]
  #peuvent être ajoutées au dictionnaire datasets pour chaque division train test validation
  total_adjusted_labels = []
  print(len(tokenized_samples["input_ids"]))
  for k in range(0, len(tokenized_samples["input_ids"])):
    prev_wid = -1
    word_ids_list = tokenized_samples.word_ids(batch_index=k)
    existing_label_ids = all_samples_per_split["ner_tags"][k]
    i = -1
    adjusted_label_ids = []
   
    for wid in word_ids_list:
      if(wid is None):
        adjusted_label_ids.append(-100)
      elif(wid!=prev_wid):
        i = i + 1
        adjusted_label_ids.append(existing_label_ids[i])
        prev_wid = wid
      else:
        label_name = label_names[existing_label_ids[i]]
        adjusted_label_ids.append(existing_label_ids[i])
        
    total_adjusted_labels.append(adjusted_label_ids)
  tokenized_samples["labels"] = total_adjusted_labels
  return tokenized_samples

tokenized_dataset = dataset.map(tokenize_adjust_labels, batched=True)
```

Voici à quoi cela ressemble après la tokenization pour 1 échantillon :

```
{'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 'input_ids': [101,
  978,
  12235,
  38044,
  40349,
  52245,
  950,
  21790,
  12079,
  89362,
  77045,
  117,
  978,
  12235,
  38044,
  40349,
  102],
 'labels': [-100, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 0, 5, 5, 5, 5, -100],
 'langs': ['bn', 'bn', 'bn', 'bn', 'bn'],
 'ner_tags': [5, 6, 6, 0, 5],
 'spans': ['LOC: \u09b8\u09bf\u09a1\u09a8\u09bf \u0995\u09cd\u09b0\u09bf\u0995\u09c7\u099f \u0997\u09cd\u09b0\u09be\u0989\u09a8\u09cd\u09a1', 'LOC: \u09b8\u09bf\u09a1\u09a8\u09bf'],
 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 'tokens': ['\u09b8\u09bf\u09a1\u09a8\u09bf', '\u0995\u09cd\u09b0\u09bf\u0995\u09c7\u099f', '\u0997\u09cd\u09b0\u09be\u0989\u09a8\u09cd\u09a1', ',', '\u09b8\u09bf\u09a1\u09a8\u09bf']}
```

## Comment remplir les échantillons 

Un autre problème est que différents échantillons peuvent être tokenisés en différentes longueurs, donc nous devons ajouter des tokens de remplissage pour que tous les échantillons aient la même longueur.

```python
from transformers import DataCollatorForTokenClassification

data_collator = DataCollatorForTokenClassification(tokenizer)
```

## Comment configurer l'intégration pour Weights and Biases

Weights and Biases est une plateforme super puissante qui aide à rationaliser le suivi de l'entraînement des modèles, le versionnage des jeux de données, l'optimisation des hyperparamètres et les visualisations. Elle dispose d'intégrations pour HuggingFace, Keras et PyTorch. 

Il est plus facile de garder une trace de tous les paramètres pour chaque expérience, de la façon dont les pertes varient pour chaque exécution, etc., ce qui rend le débogage plus rapide. 

Consultez leur site web lié [ici](https://docs.wandb.ai/) pour une liste complète des fonctionnalités offertes, des plans d'utilisation et comment commencer. 

```
!pip install wandb

```

```python
import os
import wandb
os.environ["WANDB_API_KEY"]="API KEY GOES HERE"
os.environ["WANDB_ENTITY"]="Suchandra"
os.environ["WANDB_PROJECT"]="finetune_bert_ner"
```

L'avantage de Weights and Biases est le journalisation automatique et les graphiques grâce auxquels nous pouvons comparer les performances du modèle sur plusieurs exécutions et déterminer pour quelles valeurs il fonctionne bien. Comme ici :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-127.png)

Je peux voir en un coup d'œil comment le score F1 et la perte varient pour différentes valeurs d'époque :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-128.png)

## Comment entraîner le modèle en utilisant l'API Trainer

L'API Trainer de HuggingFace est très intuitive et fournit une boucle d'entraînement générique, quelque chose que nous n'avons pas dans PyTorch pour le moment. 

Pour obtenir des métriques sur l'ensemble de validation pendant l'entraînement, nous devons définir la fonction qui calculera la métrique pour nous. Cela est très bien documenté dans leur [docs](https://huggingface.co/docs/transformers/training) officiel. 

```
from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer
import numpy as np
from datasets import load_metric
metric = load_metric("seqeval")
def compute_metrics(p):
    predictions, labels = p
    predictions = np.argmax(predictions, axis=2)

    # Supprimer l'index ignoré (tokens spéciaux)
    true_predictions = [
        [label_names[p] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]
    true_labels = [
        [label_names[l] for (p, l) in zip(prediction, label) if l != -100]
        for prediction, label in zip(predictions, labels)
    ]

    results = metric.compute(predictions=true_predictions, references=true_labels)
    flattened_results = {
        "overall_precision": results["overall_precision"],
        "overall_recall": results["overall_recall"],
        "overall_f1": results["overall_f1"],
        "overall_accuracy": results["overall_accuracy"],
    }
    for k in results.keys():
      if(k not in flattened_results.keys()):
        flattened_results[k+"_f1"]=results[k]["f1"]

    return flattened_results


```

Je voulais voir les métriques au niveau des entités aussi, donc j'ai ajouté ce snippet :

```python
flattened_results = {"overall_precision": results["overall_precision"],"overall_recall": results["overall_recall"],"overall_f1": results["overall_f1"],"overall_accuracy": results["overall_accuracy"],}

for k in results.keys():
	if(k not in flattened_results.keys()):
    	flattened_results[k+"_f1"]=results[k]["f1"]
```

Ensuite, nous chargeons le point de contrôle du modèle à affiner et passons tous les arguments à Trainer et entraînons. 

```
model = AutoModelForTokenClassification.from_pretrained("bert-base-multilingual-cased", num_labels=len(label_names))
training_args = TrainingArguments(
    output_dir="./fine_tune_bert_output",
    evaluation_strategy="steps",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=7,
    weight_decay=0.01,
    logging_steps = 1000,
    report_to="wandb",
    run_name = "ep_10_tokenized_11",
    save_strategy='no'
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["validation"],
    data_collator=data_collator,
    tokenizer=tokenizer,
    compute_metrics=compute_metrics
)

trainer.train()
wandb.finish()
```

J'entraînais cela sur Google Colab et j'ai atteint les limites d'utilisation de Colab. Je ne suis pas sûr de pourquoi cela est arrivé, puisque je n'ai pas entraîné pendant 12 heures ou quelque chose comme ça. 

D'après la FAQ officielle de Colab [ici](https://research.google.com/colaboratory/faq.html), elle décrit ce problème et les causes possibles. J'ai terminé l'entraînement en passant à Kaggle.

Voici quelques résultats des ensembles d'entraînement, de validation et de test :

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-80.png)
_Résultats d'entraînement et de validation_

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-81.png)
_Résultats de test_

## Comment sauvegarder le modèle sur HuggingFace Model Hub

J'ai trouvé que cloner le dépôt, ajouter des fichiers et commiter en utilisant Git était la manière la plus simple de sauvegarder le modèle sur le hub.

```
!transformers-cli login
!git config --global user.email "youremail"
!git config --global user.name "yourname"
!sudo apt-get install git-lfs 
%cd your_model_output_dir
!git add .
!git commit -m "Adding the files"
!git push
```

## Comment créer une carte de modèle

Maintenant, ajoutons des informations utiles sur notre modèle en créant une carte de modèle sur HuggingFace. Elle sert de README.md pour le dépôt. 

Bien que la plupart soit très simple, voici quelques choses qui m'ont pris un certain temps à comprendre :

* comment changer la langue par défaut de l'API d'inférence. Mon modèle NER est affiné sur la langue bengali mais les exemples d'entrées étaient en anglais. Pour changer cela, j'ai dû donner les informations de langue dans les métadonnées de la carte de modèle, qui est écrite en YAML. Vous pouvez vous référer aux docs du dépôt de modèle [ici](https://huggingface.co/docs/hub/model-repos)
* personnaliser les exemples d'entrée comme ceci :
```examples:
widget:
- text: "\u09ae\u09be\u09b0\u09ad\u09bf\u09a8 \u09a6\u09bf \u09ae\u09be\u09b0\u09b8\u09bf\u09af\u09bc\u09be\u09a8"
```
* vous pouvez également donner un nom à chaque exemple comme ceci :
```
- text: "\u09b8\u09be\u0989\u09a5 \u0987\u09b8\u09cd\u099f \u0987\u0989\u09a8\u09bf\u09ad\u09be\u09b0\u09cd\u09b8\u09bf\u099f\u09bf"
  example_title: "Sentence_4"
```

Voici toutes les métadonnées que j'ai ajoutées à ma carte de modèle

```yaml
---
language: bn
datasets:
- wikiann
examples:
widget:
- text: "\u09ae\u09be\u09b0\u09ad\u09bf\u09a8 \u09a6\u09bf \u09ae\u09be\u09b0\u09b8\u09bf\u09af\u09bc\u09be\u09a8"
  example_title: "Sentence_1"
- text: "\u09b2\u09bf\u0993\u09a8\u09be\u09b0\u09cd\u09a6\u09cb \u09a6\u09be \u09ad\u09bf\u099e\u09cd\u099a\u09bf"
  example_title: "Sentence_2"
- text: "\u09ac\u09b8\u09a8\u09bf\u09af\u09bc\u09be \u0993 \u09b9\u09be\u09b0\u09cd\u099c\u09c7\u0997\u09cb\u09ad\u09bf\u09a8\u09be"
  example_title: "Sentence_3"
- text: "\u09b8\u09be\u0989\u09a5 \u0987\u09b8\u09cd\u099f \u0987\u0989\u09a8\u09bf\u09ad\u09be\u09b0\u09cd\u09b8\u09bf\u099f\u09bf"
  example_title: "Sentence_4"
- text: "\u09ae\u09be\u09a8\u09bf\u0995 \u09ac\u09a8\u09cd\u09a6\u09cd\u09af\u09cb\u09aa\u09be\u09a7\u09cd\u09af\u09be\u09af\u09bc \u09b2\u09c7\u0996\u0995"
  example_title: "Sentence_5"
---
```

Et voici à quoi ressemble ma carte de modèle

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-129.png)

## Résumons

Dans cet article, nous avons couvert comment affiner un modèle pour les tâches de NER en utilisant la puissante bibliothèque HuggingFace. 

Nous avons également vu comment intégrer avec Weights and Biases, comment partager notre modèle terminé sur HuggingFace model hub, et écrire une belle carte de modèle documentant notre travail. 

C'est tout pour moi dans cet article. Continuez à apprendre, codeurs, continuez à vous perfectionner, et restez toujours curieux. Prenez soin de vous et bon codage !