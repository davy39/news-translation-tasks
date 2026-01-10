---
title: NLP avec spaCy – Comment commencer avec le traitement du langage naturel
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-06-26T23:10:31.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-nlp-using-spacy
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/NLP-using-Spacy
seo_title: NLP avec spaCy – Comment commencer avec le traitement du langage naturel
---

Banner.png
tags:
- name: Machine Learning
  slug: machine-learning
- name: traitement du langage naturel
  slug: traitement-du-langage-naturel
seo_title: null
seo_desc: "Dans le monde actuel axé sur les données, d'énormes quantités de données textuelles non structurées sont \
  \ générées chaque jour. Et pour aider à gérer toutes ces données, le traitement du langage naturel \
  \ (NLP) est apparu comme une technologie transformative. \nLe NLP est un sous-domaine de l'intelligence \
  \ artificielle..."
---

Dans le monde actuel axé sur les données, d'énormes quantités de données textuelles non structurées sont générées chaque jour. Et pour aider à gérer toutes ces données, le traitement du langage naturel (NLP) est apparu comme une technologie transformative. 

Le NLP est un sous-domaine de l'intelligence artificielle. Il se concentre sur la capacité des machines à comprendre, interpréter et générer le langage humain. 

Dans ce tutoriel, nous explorerons les concepts fondamentaux du NLP et nous examinerons une implémentation particulière avec spaCy. Cela montrera son immense potentiel pour révolutionner diverses industries.

Jetons un rapide coup d'œil au traitement du langage naturel avant de commencer avec spaCy.

## Qu'est-ce que le traitement du langage naturel ?

Le NLP implique l'intersection de la linguistique, de l'informatique et de l'apprentissage automatique. Son objectif principal est de combler le fossé entre le langage humain et la compréhension des machines. 

Le NLP englobe une large gamme de tâches, y compris la classification de texte, la reconnaissance d'entités nommées (NER), l'analyse de sentiment, et plus encore.

### Classification de texte

Cela implique de catégoriser le texte en classes ou catégories prédéfinies en fonction de son contenu. 

Cela a des applications dans l'analyse de sentiment, la détection de spam, la classification de sujets, et plus encore.

### Reconnaissance d'entités nommées (NER)

Cela implique d'identifier et d'extraire des entités nommées telles que des noms, des organisations, des lieux et des dates à partir du texte. 

La NER est cruciale pour l'extraction d'informations, les systèmes de réponse aux questions et les moteurs de recommandation. 

### Analyse de sentiment

Cela implique de déterminer le sentiment ou l'émotion exprimée dans un texte, qu'il soit positif, négatif ou neutre. 

L'analyse de sentiment est largement utilisée pour le monitoring de marque, l'analyse des retours clients et le monitoring des réseaux sociaux. 

## Défis du traitement du langage naturel

Bien que le NLP ait fait des avancées significatives, plusieurs défis persistent :

1. Le langage humain est intrinsèquement ambigu, ce qui le rend parfois difficile à comprendre et à interpréter avec précision pour les machines.
2. Les différentes langues, dialectes, argots et nuances culturelles ajoutent de la complexité aux tâches de NLP, nécessitant des modèles spécifiques à chaque langue et adaptables.
3. Capturer les informations contextuelles et comprendre la sémantique sous-jacente du texte reste un défi majeur pour les algorithmes de NLP.
4. Les modèles de NLP dépendent fortement des données d'entraînement, et des données biaisées ou de mauvaise qualité peuvent entraîner des prédictions biaisées ou inexactes, soulevant des préoccupations éthiques potentielles.

## Qu'est-ce que spaCy ?

Dans le monde du traitement du langage naturel (NLP), spaCy s'est imposé comme une bibliothèque puissante et efficace, révolutionnant la manière dont les développeurs et les chercheurs travaillent avec les données textuelles. 

spaCy est une bibliothèque Python open-source conçue spécifiquement pour les tâches de NLP telles que l'étiquetage grammatical, la reconnaissance d'entités nommées, l'analyse de dépendance, et plus encore. 

Elle a été développée avec pour objectif de fournir des performances de niveau industriel, tout en restant facile à utiliser et à intégrer dans les flux de travail existants. 

spaCy est basée sur les dernières recherches et met en œuvre des techniques de pointe, ce qui en fait un choix idéal pour les débutants et les praticiens expérimentés du NLP.

## Fonctionnalités clés de spaCy

### Annotations linguistiques

spaCy fournit une large gamme de modèles pré-entraînés qui peuvent analyser rapidement le texte et extraire diverses caractéristiques linguistiques. Ces caractéristiques incluent les étiquettes grammaticales, les entités nommées, les dépendances syntaxiques, les limites de phrases, et plus encore. 

Les modèles pré-entraînés sont formés sur de grands corpus et ont une grande précision, permettant aux développeurs de se concentrer sur leurs tâches spécifiques de NLP sans avoir à s'inquiéter de l'entraînement des modèles à partir de zéro.

### Tokenisation et segmentation de phrases

La tokenisation est une étape cruciale en NLP qui décompose le texte en mots individuels ou en sous-mots. Les algorithmes de tokenisation de spaCy sont très efficaces et spécifiques à chaque langue, permettant une tokenisation précise et personnalisable. 

spaCy peut également segmenter automatiquement le texte en phrases, facilitant le travail avec les données textuelles à un niveau granulaire. 

### Reconnaissance d'entités

La reconnaissance d'entités nommées (NER) est la tâche d'identification et de classification des entités nommées telles que les personnes, les organisations, les lieux, les dates, et plus encore. 

Les capacités de NER de spaCy sont exceptionnelles, offrant un support prêt à l'emploi pour plusieurs langues. Elle permet aux développeurs d'entraîner des modèles NER personnalisés en utilisant leurs propres données étiquetées, permettant une reconnaissance d'entités spécifique à un domaine. 

### Analyse de dépendance

L'analyse de dépendance implique l'analyse de la structure grammaticale d'une phrase en déterminant les relations entre les mots. 

L'analyse de dépendance de spaCy est basée sur des algorithmes efficaces et atteint une grande précision. Elle fournit un ensemble riche d'annotations syntaxiques, y compris le chef de chaque mot, l'étiquette de dépendance et la structure de sous-arbre. 

Ces informations sont inestimables pour des tâches comme l'extraction d'informations, la réponse aux questions et l'analyse de sentiment.

### Personnalisation et extensibilité

L'une des grandes forces de spaCy est sa flexibilité et son extensibilité. Les développeurs peuvent facilement personnaliser et affiner les modèles de spaCy pour les adapter à des domaines spécifiques ou améliorer les performances sur des tâches spécifiques. 

La bibliothèque fournit également une API simple pour ajouter des composants personnalisés, tels que de nouveaux tokeniseurs, des reconnaisseurs d'entités ou des analyseurs syntaxiques, ce qui en fait un outil polyvalent pour la recherche et le développement. 

### Performance et scalabilité

spaCy est connu pour ses performances et sa scalabilité exceptionnelles. La bibliothèque est implémentée en Cython, un langage de programmation qui compile du code de type Python en modules C/C++ hautement efficaces. Cela permet à spaCy de traiter les données textuelles à une vitesse fulgurante, ce qui le rend adapté aux applications NLP à grande échelle et aux systèmes en temps réel. 

## Exemple de reconnaissance d'entités nommées dans spaCy

Essayons d'implémenter la NER en utilisant spaCy. 

J'utiliserai Google Colab. Google Colab est un service d'hébergement de notebooks Jupyter qui ne nécessite aucune configuration pour être utilisé et offre un accès gratuit à des ressources de calcul, y compris des GPU et des TPU. 

Vous pouvez utiliser Kaggle à la place ou l'exécuter sur votre propre ordinateur si vous le souhaitez. Comme spaCy est un modèle pré-entraîné, il ne nécessite pas beaucoup de puissance de calcul pour commencer. 

Mais je vous conseille de configurer Anaconda sur votre machine si vous travaillez sur des problèmes de machine learning. 

Accédez à [https://colab.research.google.com](https://colab.research.google.com) et cliquez sur le bouton "Nouveau Notebook". 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-244.png)
_Console Google Colab_

Dans l'en-tête, entrez un nom pour votre fichier. Assurez-vous que le nom de votre fichier se termine par l'extension `.pynb`. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-245.png)
_Changer le nom du fichier et créer un bloc de code_

Cliquez sur le bouton "+ Code" pour créer un bloc de code. 

Par défaut, Google Colab est fourni avec certains outils de machine et des bibliothèques Python préinstallées. Nous n'avons donc pas à nous soucier des installations et de la préparation de notre environnement de développement. 

Mais il ne vient pas avec la bibliothèque `spacy`. 

Exécutez la commande suivante à l'intérieur du bloc de code pour installer la bibliothèque `spacy`. 

```bash
!pip install -U spacy
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-246.png)
_Installer la bibliothèque `spacy`_

Choisissez l'option que vous souhaitez et poursuivez. La principale différence entre chacune d'elles est la quantité de données avec laquelle elles ont été entraînées. 

* Petit – [en_core_web_sm](https://www.freecodecamp.org/news/p/eb6f9486-7030-463a-9ec3-30a1f7858d94/spacy.io/models/en#en_core_web_sm)
* Moyen – [en_core_web_md](https://www.freecodecamp.org/news/p/eb6f9486-7030-463a-9ec3-30a1f7858d94/spacy.io/models/en#en_core_web_md)
* Grand – [en_core_web_lg](https://www.freecodecamp.org/news/p/eb6f9486-7030-463a-9ec3-30a1f7858d94/spacy.io/models/en#en_core_web_lg)
* Transformer – [en_core_web_trf](https://www.freecodecamp.org/news/p/eb6f9486-7030-463a-9ec3-30a1f7858d94/spacy.io/models/en#en_core_web_trf)

Notre prochaine étape consiste à télécharger l'un de ces modèles. Ajoutez un bloc de code et choisissez l'un des modèles de la liste ci-dessus, puis exécutez la commande suivante. Je vais télécharger le grand modèle.

```bash
!python -m spacy download en_core_web_lg
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-247.png)
_Télécharger le modèle pré-entraîné_

Ajoutez un bloc de code et exécutez la commande suivante pour charger le modèle. 

```python
import spacy
nlp = spacy.load("en_core_web_lg")
```

Très bien. Nous sommes prêts. 

Essayons de séparer les entités d'une phrase. Ajoutez un bloc de code et exécutez le bloc de code suivant :

```python
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

Dans le code ci-dessus, nous demandons au modèle spaCy de trouver les entités dans la phrase "Apple is looking at buying U.K. startup for $1 billion". 

Nous parcourons ensuite chaque entité et affichons l'entité, les index de début et de fin des caractères dans la phrase, et l'étiquette de l'entité.

Vous devriez voir la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-248.png)
_Exemple 1 de reconnaissance d'entités nommées avec `spaCy`_

La sortie ci-dessus décrit que "Apple" est une entité et qu'elle est présente de l'index 0 à l'index 5 dans la phrase donnée et qu'il s'agit d'une organisation (ORG). 

Si vous êtes confus au sujet de l'index, rappelez-vous qu'il commence à 0. Les cinq premiers caractères dans notre texte d'entrée donné sont "Apple". Donc, c'est de 0 à 5. 

De même, il identifie "U.K." comme une entité et le décrit comme une entité géopolitique (GPE). Il étiquette "$1 billion" comme une entité d'argent (MONEY). 

Essayons une phrase différente cette fois. 

"Le Premier ministre de l'Inde Narendra Modi a rencontré le président américain Joe Biden à Washington DC". 

Voyons quelles sont les entités qu'il identifie. Ajoutez un bloc de code et exécutez le code suivant :

```python
doc = nlp("Prime Minister of India Narendra Modi met US President Joe Biden at Washington DC")

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-249.png)
_Exemple 2 de reconnaissance d'entités nommées avec `spaCy`_

Ce n'est pas génial, n'est-ce pas ? 

Il a identifié "India", "US", et "Washington DC" comme des entités géopolitiques (GPE). Il a également identifié "Narendra Modi" et "Joe Biden" comme des entités de personne (PERSON). 

Essayez d'entrer différentes phrases et jouez avec. Je suis sûr que vous serez émerveillé par ses capacités à identifier les entités. 

## Conclusion

Dans ce tutoriel, nous avons appris le NLP avec une implémentation simple en utilisant la bibliothèque spaCy. 

Le traitement du langage naturel offre un immense potentiel pour transformer la manière dont nous interagissons avec les machines et analysons de vastes quantités de données textuelles. spaCy est devenu une bibliothèque de référence pour de nombreux praticiens du NLP grâce à ses fonctionnalités puissantes, sa facilité d'utilisation et ses performances exceptionnelles. 

Si vous souhaitez en savoir plus sur le NLP/l'apprentissage automatique, abonnez-vous à ma [newsletter par email](https://5minslearn.gogosoon.com/?ref=fcc_getting_started_nlp_spacy) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_getting_started_nlp_spacy)) et suivez-moi sur les réseaux sociaux.