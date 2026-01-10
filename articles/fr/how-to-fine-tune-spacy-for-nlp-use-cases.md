---
title: Comment affiner les modèles spaCy pour des cas d'utilisation en TAL
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-07-11T14:11:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-fine-tune-spacy-for-nlp-use-cases
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/Fine-tune-Spacy
seo_title: Comment affiner les modèles spaCy pour des cas d'utilisation en TAL
---

Banner.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: traitement du langage naturel
  slug: traitement-du-langage-naturel
- name: Python
  slug: python
seo_title: null
seo_desc: "spaCy est une bibliothèque logicielle open-source pour le traitement avancé du langage naturel. Elle est écrite dans les langages de programmation Python et Cython, et est publiée sous la licence MIT. \nspaCy excelle dans les tâches d'extraction d'informations à grande échelle. Elle est écrite dès le départ en Cython géré soigneusement en mémoire."
---

spaCy est une bibliothèque logicielle open-source pour le traitement avancé du langage naturel. Elle est écrite dans les langages de programmation Python et Cython, et est publiée sous la licence MIT. 

spaCy excelle dans les tâches d'extraction d'informations à grande échelle. Elle est écrite dès le départ en Cython géré soigneusement en mémoire.

spaCy est conçu pour nous aider à construire de vrais produits, ou à recueillir de vraies informations. Il est construit avec 73+ langues, et supporte des modèles personnalisés construits avec Pytorch et Tensorflow. Il est robuste et a une précision rigoureusement évaluée.

Vous ne connaissez peut-être pas beaucoup Cython. Alors, jetons un rapide coup d'œil dessus. 

## Qu'est-ce que Cython ?

Cython est un compilateur Python qui facilite l'écriture d'extensions C pour Python aussi facilement que Python lui-même. Cython est basé sur Pyrex, mais supporte plus de fonctionnalités et d'optimisations de pointe. 

Pour le dire simplement, c'est un compilateur de Python vers C. 

En citant Wikipedia, 

> Cython est un langage de programmation, un sur-ensemble du langage de programmation Python, conçu pour donner des performances similaires à celles du C avec du code écrit principalement en Python avec une syntaxe supplémentaire inspirée du C en option. 

Vous vous demandez peut-être si vous devez apprendre Cython pour vous aider à affiner vos modèles spaCy.

Eh bien, ne vous inquiétez pas. Vous n'avez pas besoin d'apprendre Cython pour travailler avec spaCy. Je voulais juste m'assurer que vous savez ce que c'est pour vous aider à tirer le meilleur parti de ce tutoriel.

## Prérequis

### Connaissance de base de spaCy

Le [site de documentation officiel](https://spacy.io/usage/spacy-101) de spaCy fournit beaucoup d'informations sur l'outil. Alternativement, vous pouvez lire mon [autre tutoriel](https://www.freecodecamp.org/news/getting-started-with-nlp-using-spacy/) qui donne quelques informations de base sur spaCy. 

### Connaissance de base de la collecte de données

Pour affiner un modèle, vous devez avoir les données prêtes. Et elles doivent être de bonne qualité. 

Dans ce tutoriel, supposons que nous avons construit un logiciel de gestion d'événements. Nous voulons ajouter une assistance vocale à notre logiciel. Nous avons un module qui convertit l'entrée vocale en texte. Notre prochaine étape est de traiter ce texte et d'extraire des données de la phrase donnée en utilisant spaCy. 

Nous devons recueillir quelques phrases de base que nous entendons de la part de personnes essayant de planifier un événement. Voici quelques exemples :

1. Planifier un événement pour une visite à Trivandrum le 18 juillet
2. Créer un événement qui se déroule demain sur l'IA
3. Planifier un événement de célébration de Pongal à Oaks HOA le 20 juin 2023

De même, nous devons collecter des invites liées à la planification d'événements. Plus vous collectez et entrez de données, plus votre modèle sera précis. 

J'ai créé 7 phrases, ce qui est beaucoup trop peu pour une entreprise de logiciels de gestion d'événements pour entraîner son modèle. Mais d'un point de vue démonstration, cela devrait suffire. 

## Comment pré-traiter les données

La collecte de données ne couvre qu'une partie de l'équation. Nous devons pré-traiter les données et les transformer de manière à ce que spaCy puisse facilement les comprendre. Nous devons également définir quel type de données (tags) doit être identifié à partir des phrases données. 

Prenons la phrase suivante comme exemple :

> "Planifier un événement pour une visite à Trivandrum le 18 juillet". 

Essayons de diviser quelques tags de la phrase ci-dessus :

* Planifier – cela appartient au tag "action"
* événement – cela appartient au tag "domaine"
* visite à Trivandrum – cela appartient au tag "nom"
* 18 juillet – cela appartient au tag "date"

Chaque tag défini ci-dessus peut contenir des alternatives dans d'autres phrases. Par exemple, nous pouvons entrer les phrases suivantes :

1. Annuler la réunion client prévue demain
2. Changer l'heure de la visite au centre commercial à 18h

Dans les phrases ci-dessus, les tags d'action sont "Annuler" et "Changer". De même, les données pour chaque tag peuvent varier pour chaque phrase. 

Notre prochaine étape est d'enseigner à spaCy les mots pour chaque tag. Nous devons préparer un fichier JSON qui contient des exemples avec les tags et leurs indices. 

Par exemple, dans la phrase ci-dessus ("Planifier un événement pour une visite à Trivandrum le 18 juillet"), l'index pour le tag "action" commence à 0 (les indices commencent toujours à 0 en Python) et se termine à 7. 

De même pour les 7 phrases que j'ai choisies, j'ai préparé l'index pour chaque tag et créé le fichier JSON. 

<script src="https://gist.github.com/5minslearn/a6eefddc688184d60e84127b356e7a4f.js"></script>

## Comment affiner le modèle spaCy

Essayons d'affiner spaCy avec les données que nous avons. 

Créez un dossier et téléchargez le fichier JSON ci-dessus et placez-le dans le dossier. Créez un nouveau fichier nommé `custom_model.ipynb`. 

Toutes les sections suivantes ci-dessous nécessitent la création d'un bloc de code. Créez un bloc de code chaque fois que vous voyez un titre. Voici un exemple de capture d'écran. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-61.png)
_Création et exécution de blocs de code_

### Importer spaCy

```python
import spacy
```

### Charger le modèle pré-entraîné

```python
nlp = spacy.load("en_core_web_lg")
```

### Importer le fichier JSON

Importez le fichier JSON téléchargé ci-dessus. 

```
import json

with open('./event_schedule_data.json', 'r') as f:
    data = json.load(f)
```

### Convertir les données

Convertissez les données lues depuis le fichier JSON en un tuple de dictionnaires contenant le texte original et les entités. 

```
training_data = []
for example in data['examples']:
    temp_dict = {}
    temp_dict['text'] = example['content']
    temp_dict['entities'] = []
    for annotation in example['annotations']:
        start = annotation['start']
        end = annotation['end'] + 1
        label = annotation['tag_name'].upper()
        temp_dict['entities'].append((start, end, label))
    training_data.append(temp_dict)
print(training_data[0])
```

Le code ci-dessus convertira les données au format requis et imprimera le premier dictionnaire dans le tuple, qui ressemblera à quelque chose comme ci-dessous : 

```json
{'text': 'Schedule a calendar event in Teak oaks HOA about competitions happening tomorrow', 'entities': [(0, 8, 'ACTION'), (11, 25, 'DOMAIN'), (29, 42, 'HOA'), (49, 71, 'EVENT'), (72, 80, 'DATE')]}
```

### Importer les bibliothèques d'entraînement

```
from spacy.tokens import DocBin
from tqdm import tqdm
from spacy.util import filter_spans

nlp = spacy.blank('en')
```

### Entraîner le modèle

Le code ci-dessous créera un modèle personnalisé avec les données que nous fournissons. Un fichier binaire nommé `train.spacy` sera généré à la fin. 

```python
doc_bin = DocBin()
for training_example in tqdm(training_data):
    text = training_example['text']
    labels = training_example['entities']
    doc = nlp.make_doc(text)
    ents = []
    for start, end, label in labels: 
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    filtered_ents = filter_spans(ents)
    doc.ents = filtered_ents
    doc_bin.add(doc)

doc_bin.to_disk("train.spacy")
```

### Créer des fichiers de configuration

Créez un nouveau fichier nommé `base_config.cfg` et copiez le code ci-dessous dedans. 

<script src="https://gist.github.com/5minslearn/ef0167c0485d1589a9e6b66df66c44ce.js"></script>

Créez un autre fichier nommé `config.cfg` et copiez le code ci-dessous dedans. 

<script src="https://gist.github.com/5minslearn/57cb5476c60441f988391ef942174ec4.js"></script>

Ne vous inquiétez pas. Ce sont des configurations par défaut que j'ai prises de leur documentation officielle et je n'ai apporté aucune modification.

### Initialiser spaCy avec les fichiers de configuration

Exécutez la commande suivante dans le bloc de code du notebook pour initialiser spaCy avec le fichier de configuration. Ce fichier de configuration sera utilisé pour entraîner le modèle spaCy avec notre modèle personnalisé généré. 

```python
!python -m spacy init fill-config base_config.cfg config.cfg
```

### Entraîner le modèle spaCy

Exécutez la commande suivante pour entraîner le modèle spaCy :

```
!python -m spacy train config.cfg --output ./ --paths.train ./train.spacy --paths.dev ./train.spacy
```

Cela peut prendre un certain temps en fonction de la configuration de votre système. Idéalement, pas trop longtemps (environ 5 à 10 minutes). À la fin, il générera 2 dossiers nommés `model-best` et `model-last`. 

### Charger le meilleur modèle

```
nlp_ner = spacy.load("model-best")
```

### Tester notre modèle

Testons notre modèle avec l'entrée suivante. 

"Pourriez-vous s'il vous plaît réserver une session de brainstorming d'équipe mercredi prochain à 11h ?"

```python
doc = nlp_ner("Could you please reserve a team brainstorming session on coming Wednesday at 11 AM?")

spacy.displacy.render(doc, style="ent")
```

Vous devriez être surpris de voir le résultat. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-45.png)
_Représentation des entités de notre phrase d'entrée_

C'est bien, n'est-ce pas ? 

Éventuellement, vous pourriez avoir une question : en tant que programmeur, comment puis-je obtenir ces données dans mon code backend ? 

Eh bien, c'est quelque chose que tout le monde demande. 

spaCy a une réponse pour cela. Vous pouvez exposer les données ci-dessus sous forme de JSON. 

### Convertir les données extraites en JSON

```python
json_obj = doc.to_json()
json_obj
```

Cela affichera une sortie similaire à celle ci-dessous. 

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-46.png)
_JSON de notre entrée de phrase de test_

Écrivez une API REST et exposez ces données sous forme de JSON. C'est tout. Mais souvenez-vous, spaCy ne vous donnera que les indices, vous devez analyser votre phrase et extraire les mots entre ces indices. 

## Conclusion

Dans cet article, nous avons appris comment personnaliser et affiner un modèle pré-entraîné spaCy avec les données qui correspondent à nos connaissances du domaine. 

De même, vous pouvez également entraîner avec vos données spécifiques au domaine. Le modèle que vous affinez sera privé pour vous, sauf si vous l'exposez au public. Il est donc mieux adapté pour l'entraînement avec les données du domaine qui ne sont pas disponibles publiquement. 

Si vous souhaitez en savoir plus sur le TAL/apprentissage automatique, abonnez-vous à ma [newsletter par email](https://5minslearn.gogosoon.com/?ref=fcc_fine_tune_spacy) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_fine_tune_spacy)) et suivez-moi sur les réseaux sociaux.