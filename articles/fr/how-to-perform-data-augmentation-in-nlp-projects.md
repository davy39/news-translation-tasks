---
title: Comment effectuer l'augmentation de données dans les projets de NLP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-06-24T15:33:57.000Z'
originalURL: https://freecodecamp.org/news/how-to-perform-data-augmentation-in-nlp-projects
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/1_eproIleJllsp0enh6HA2Hw.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: data analytics
  slug: data-analytics
- name: Machine Learning
  slug: machine-learning
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: Comment effectuer l'augmentation de données dans les projets de NLP
seo_desc: "By Davis David\nIn machine learning, you need to have a large amount of\
  \ data in order to achieve strong model performance. \nUsing a method known as data\
  \ augmentation, you can create more data for your machine learning project. Data\
  \ augmentation is a c..."
---

Par Davis David

En apprentissage automatique, vous devez disposer d'une grande quantité de données pour obtenir des performances de modèle solides. 

En utilisant une méthode connue sous le nom d'augmentation de données, vous pouvez créer plus de données pour votre projet d'apprentissage automatique. L'augmentation de données est un ensemble de techniques qui gèrent le processus de génération automatique de données de haute qualité en plus des données existantes.

Dans les applications de vision par ordinateur, les approches d'augmentation sont assez courantes. Si vous travaillez sur un projet de vision par ordinateur (comme la classification d'images), par exemple, vous pouvez appliquer des dizaines de techniques à chaque image : décalage, modification des intensités de couleur, mise à l'échelle, rotation, recadrage, et plus encore.

Si vous avez un ensemble de données minuscule pour votre projet de ML ou si vous souhaitez réduire le surapprentissage dans vos modèles d'apprentissage automatique, il peut être judicieux d'appliquer des approches d'augmentation de données.

> « Nous n'avons pas de meilleurs algorithmes. Nous avons simplement plus de données. » - Peter [Norvig](https://research.google/people/author205/?ref=hackernoon.com)

Dans le domaine du traitement du langage naturel (NLP), la complexité énorme du langage rend difficile l'augmentation du texte. Le processus d'augmentation des données textuelles est plus difficile et pas aussi simple que vous pourriez le penser.

Dans cet article, vous apprendrez à utiliser une bibliothèque appelée [TextAttack](https://github.com/QData/TextAttack?ref=hackernoon.com) pour améliorer les données pour le traitement du langage naturel.

## Qu'est-ce que TextAttack ?

TextAttack est un framework Python qui a été construit par l'équipe [QData](https://qdata.github.io/qdata-page/?ref=hackernoon.com) dans le but de mener des attaques adverses, un entraînement adverse et une augmentation de données dans le traitement du langage naturel. 

TextAttack possède des composants qui peuvent être utilisés indépendamment pour une variété de tâches de base de traitement du langage naturel, y compris l'encodage de phrases, la vérification de la grammaire et la substitution de mots.

TextAttack excelle dans l'exécution des trois fonctions suivantes :

1. Attaques adverses (Python : `**textattack.Attack**`, Bash : `**textattack attack**`).
2. Augmentation de données (Python : `**textattack.augmentation.Augmenter**`, Bash : `**textattack augment**`).
3. Entraînement de modèles (Python : `**textattack.Trainer**`, Bash : `**textattack train**`).

Pour cet article, nous nous concentrerons sur l'utilisation de la bibliothèque TextAttack pour l'augmentation de données.

## Comment installer TextAttack

Pour utiliser cette bibliothèque, assurez-vous d'avoir Python 3.6 ou une version ultérieure dans votre environnement.

Exécutez la commande suivante pour installer TextAttack :

```python
pip install textattack
```

**Note :** Une fois que vous avez installé TextAttack, vous pouvez l'exécuter via le module Python ou via la ligne de commande.

## Techniques d'augmentation de données pour les données textuelles

La bibliothèque TextAttack dispose de diverses techniques d'augmentation que vous pouvez utiliser dans votre projet de NLP pour ajouter plus de données textuelles. 

Voici quelques-unes des techniques que vous pouvez appliquer :

### Technique `CharSwapAugmenter`

Cette technique augmente les mots en échangeant des caractères contre d'autres caractères.

```python
from textattack.augmentation import CharSwapAugmenter

text = "I have enjoyed watching that movie, it was amazing."

charswap_aug = CharSwapAugmenter()

charswap_aug.augment(text)
```

['I have enjoyed watching that omvie, it was amazing.']

L'augmenteur a échangé le mot **« movie »** par **« omvie »**.

### Technique `DeletionAugmenter`

Cette technique augmente le texte en supprimant certaines parties du texte pour créer un nouveau texte.

```python
from textattack.augmentation import DeletionAugmenter

text = "I have enjoyed watching that movie, it was amazing."

deletion_aug = DeletionAugmenter()

deletion_aug.augment(text)
```

['I have watching that, it was amazing.']

Cette méthode a supprimé le mot **« enjoyed »** pour créer un nouveau texte augmenté.

### Technique `EasyDataAugmenter`

Cette technique augmente le texte avec une combinaison de différentes méthodes, telles que :

* Échanger aléatoirement les positions des mots dans la phrase.
* Supprimer aléatoirement des mots de la phrase.
* Insérer aléatoirement un synonyme aléatoire d'un mot aléatoire à un emplacement aléatoire.
* Remplacer aléatoirement des mots par leurs synonymes.

```python
from textattack.augmentation import EasyDataAugmenter

text = "I was billed twice for the service and this is the second time it has happened"

eda_aug = EasyDataAugmenter()

eda_aug.augment(text)
```

['I was billed twice for the service and this is the second time it has happen', 'I was billed twice for the one service and this is the second time it has happened', 'I billed twice for the service and this is the second time it has happened',  
'I was billed twice for the this and service is the second time it has happened']

Comme vous pouvez le voir à partir des textes augmentés, cela montre différents résultats en fonction des méthodes appliquées. Par exemple, dans le premier texte augmenté, le dernier mot a été modifié de **« happened »** à **« happen »**.

### Technique `WordNetAugmenter`

Cette technique peut augmenter le texte en le remplaçant par des synonymes du thésaurus WordNet.

```python
from textattack.augmentation import WordNetAugmenter

text = "I was billed twice for the service and this is the second time it has happened"

wordnet_aug = WordNetAugmenter()

wordnet_aug.augment(text)
```

['I was billed twice for the service and this is the second time it has pass']

Cette méthode a changé le mot **« happened »** en **« pass »** afin de créer un nouveau texte augmenté.

### Comment créer votre propre Augmenter

L'importation de transformations et de contraintes depuis `textattack.transformations` et `textattack.constraints` vous permet de construire votre propre augmenteur à partir de zéro. 

Ce qui suit est une illustration de l'utilisation de l'algorithme `WordSwapRandomCharacterDeletion` pour produire des augmentations d'une chaîne :

```python
from textattack.transformations import WordSwapRandomCharacterDeletion
from textattack.transformations import CompositeTransformation
from textattack.augmentation import Augmenter

my_transformation = CompositeTransformation([WordSwapRandomCharacterDeletion()])
augmenter = Augmenter(transformation=my_transformation, transformations_per_example=3)

text = 'Siri became confused when we reused to follow her directions.'

augmenter.augment(text)
```

['Siri became cnfused when we reused to follow her directions.', 'Siri became confused when e reused to follow her directions.', 'Siri became confused when we reused to follow hr directions.']

La sortie montre différents textes augmentés après la mise en œuvre de la méthode `WordSwapRandomCharacterDeletion`. Par exemple, dans le premier texte augmenté, la méthode supprime aléatoirement le caractère **« o »** dans le mot **« confused »**.

## Conclusion

Dans cet article, vous avez appris l'importance de l'augmentation de données pour vos projets de Machine Learning. Vous avez également appris à exécuter l'augmentation de données pour les données textuelles en utilisant la bibliothèque TextAttack.

À ma connaissance, ces techniques sont les approches les plus efficaces disponibles pour accomplir la tâche pour votre projet de NLP. Espérons qu'elles vous seront utiles dans votre travail.

Vous pouvez également essayer d'utiliser d'autres techniques d'augmentation disponibles dans la bibliothèque TextAttack telles que :

* EmbeddingAugmenter
* CheckListAugmenter
* CLAREAugmenter

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine !

Vous pouvez également me trouver sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid?ref=hackernoon.com).

Et vous pouvez lire plus d'articles comme celui-ci [ici](https://hackernoon.com/u/davisdavid).