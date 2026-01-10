---
title: Une introduction au sac de mots et comment le coder en Python pour le NLP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-18T17:17:41.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-bag-of-words-and-how-to-code-it-in-python-for-nlp-282e87a9da04
coverImage: https://cdn-media-1.freecodecamp.org/images/1*dcFrKbfBRJzm514gaxp4YA.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: code
  slug: code
- name: Machine Learning
  slug: machine-learning
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: Une introduction au sac de mots et comment le coder en Python pour le NLP
seo_desc: 'By Praveen Dubey

  Bag of Words (BOW) is a method to extract features from text documents. These features
  can be used for training machine learning algorithms. It creates a vocabulary of
  all the unique words occurring in all the documents in the traini...'
---

Par Praveen Dubey

Bag of Words (BOW) est une méthode pour extraire des caractéristiques à partir de documents textuels. Ces caractéristiques peuvent être utilisées pour entraîner des algorithmes de machine learning. Il crée un vocabulaire de tous les mots uniques apparaissant dans tous les documents de l'ensemble d'entraînement.

**En termes simples, c'est une collection de mots pour représenter une phrase avec le compte des mots et en ignorant principalement l'ordre dans lequel ils apparaissent.**

BOW est une approche largement utilisée avec :

1. Le traitement du langage naturel
2. La récupération d'informations à partir de documents
3. La classification de documents

À un niveau élevé, cela implique les étapes suivantes.

![Image](https://cdn-media-1.freecodecamp.org/images/qRGh8boBcLLQfBvDnWTXKxZIEAk5LNfNABHF)

**Les vecteurs générés peuvent être utilisés comme entrée pour votre algorithme de machine learning.**

Commençons par un exemple pour comprendre en prenant quelques phrases et en générant des vecteurs pour celles-ci.

Considérons les deux phrases suivantes.

```
1. "John likes to watch movies. Mary likes movies too."
```

```
2. "John also likes to watch football games."
```

Ces deux phrases peuvent également être représentées par une collection de mots.

```
1. ['John', 'likes', 'to', 'watch', 'movies.', 'Mary', 'likes', 'movies', 'too.']
```

```
2. ['John', 'also', 'likes', 'to', 'watch', 'football', 'games']
```

Ensuite, pour chaque phrase, supprimez les occurrences multiples du mot et utilisez le compte des mots pour représenter cela.

```
1. {"John":1,"likes":2,"to":1,"watch":1,"movies":2,"Mary":1,"too":1}
```

```
2. {"John":1,"also":1,"likes":1,"to":1,"watch":1,"football":1,   "games":1}
```

En supposant que ces phrases font partie d'un document, voici la fréquence combinée des mots pour l'ensemble de notre document. Les deux phrases sont prises en compte.

```
 {"John":2,"likes":3,"to":2,"watch":2,"movies":2,"Mary":1,"too":1,  "also":1,"football":1,"games":1}
```

Le vocabulaire ci-dessus de tous les mots d'un document, avec leur compte de mots respectif, sera utilisé pour créer les vecteurs pour chacune des phrases.

**La longueur du vecteur sera toujours égale à la taille du vocabulaire. Dans ce cas, la longueur du vecteur est de 11.**

Afin de représenter nos phrases originales dans un vecteur, chaque vecteur est initialisé avec tous les zéros — **[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]**

Cela est suivi par l'itération et la comparaison avec chaque mot dans notre vocabulaire, et l'incrémentation de la valeur du vecteur si la phrase contient ce mot.

```
John likes to watch movies. Mary likes movies too.[1, 2, 1, 1, 2, 1, 1, 0, 0, 0]
```

```
John also likes to watch football games.[1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
```

Par exemple, dans la phrase 1, le mot `likes` apparaît en deuxième position et apparaît deux fois. Donc le deuxième élément de notre vecteur pour la phrase 1 sera 2 : **[1, 2, 1, 1, 2, 1, 1, 0, 0, 0]**

Le vecteur est toujours proportionnel à la taille de notre vocabulaire.

Un grand document où le vocabulaire généré est énorme peut entraîner un vecteur avec beaucoup de valeurs à 0. Cela est appelé un **vecteur creux**. Les vecteurs creux nécessitent plus de mémoire et de ressources de calcul lors de la modélisation. Le grand nombre de positions ou de dimensions peut rendre le processus de modélisation très difficile pour les algorithmes traditionnels.

### Coder notre algorithme BOW

L'entrée de notre code sera plusieurs phrases et la sortie sera les vecteurs.

Le tableau d'entrée est le suivant :

```
["Joe waited for the train", "The train was late", "Mary and Samantha took the bus",
```

```
"I looked for Mary and Samantha at the bus station",
```

```
"Mary and Samantha arrived at the bus station early but waited until noon for the bus"]
```

#### Étape 1 : Tokeniser une phrase

Nous commencerons par supprimer les stopwords des phrases.

Les **stopwords** sont des mots qui ne contiennent pas assez de signification pour être utilisés dans notre algorithme. Nous ne voudrions pas que ces mots prennent de la place dans notre base de données, ou prennent un temps de traitement précieux. Pour cela, nous pouvons les supprimer facilement en stockant une liste de mots que vous considérez comme des stopwords.

La **tokenisation** est l'acte de diviser une séquence de chaînes en morceaux tels que des mots, des mots-clés, des phrases, des symboles et d'autres éléments appelés **tokens**. Les tokens peuvent être des mots individuels, des phrases ou même des phrases entières. Dans le processus de tokenisation, certains caractères comme les marques de ponctuation sont supprimés.

```
def word_extraction(sentence):    ignore = ['a', "the", "is"]    words = re.sub("[^\w]", " ",  sentence).split()    cleaned_text = [w.lower() for w in words if w not in ignore]    return cleaned_text
```

Pour une implémentation plus robuste des stopwords, vous pouvez utiliser la bibliothèque **nltk** de Python. Elle dispose d'un ensemble de mots prédéfinis par langue. Voici un exemple :

```
import nltkfrom nltk.corpus import stopwords set(stopwords.words('english'))
```

#### Étape 2 : Appliquer la tokenisation à toutes les phrases

```
def tokenize(sentences):    words = []    for sentence in sentences:        w = word_extraction(sentence)        words.extend(w)            words = sorted(list(set(words)))    return words
```

La méthode itère toutes les phrases et ajoute le mot extrait dans un tableau.

La sortie de cette méthode sera :

```
['and', 'arrived', 'at', 'bus', 'but', 'early', 'for', 'i', 'joe', 'late', 'looked', 'mary', 'noon', 'samantha', 'station', 'the', 'took', 'train', 'until', 'waited', 'was']
```

#### Étape 3 : Construire le vocabulaire et générer les vecteurs

Utilisez les méthodes définies dans les étapes 1 et 2 pour créer le vocabulaire du document et extraire les mots des phrases.

```
def generate_bow(allsentences):        vocab = tokenize(allsentences)    print("Word List for Document \n{0} \n".format(vocab));
```

```
for sentence in allsentences:        words = word_extraction(sentence)        bag_vector = numpy.zeros(len(vocab))        for w in words:            for i,word in enumerate(vocab):                if word == w:                     bag_vector[i] += 1                            print("{0}\n{1}\n".format(sentence,numpy.array(bag_vector)))
```

Voici l'entrée définie et l'exécution de notre code :

```
allsentences = ["Joe waited for the train train", "The train was late", "Mary and Samantha took the bus",
```

```
"I looked for Mary and Samantha at the bus station",
```

```
"Mary and Samantha arrived at the bus station early but waited until noon for the bus"]
```

```
generate_bow(allsentences)
```

Les vecteurs de sortie pour chacune des phrases sont :

```
Output:
```

```
Joe waited for the train train[0. 0. 0. 0. 0. 0. 1. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 2. 0. 1. 0.]
```

```
The train was late[0. 0. 0. 0. 0. 0. 0. 0. 0. 1. 0. 0. 0. 0. 0. 1. 0. 1. 0. 0. 1.]
```

```
Mary and Samantha took the bus[1. 0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 1. 0. 1. 0. 0. 1. 0. 0. 0. 0.]
```

```
I looked for Mary and Samantha at the bus station[1. 0. 1. 1. 0. 0. 1. 1. 0. 0. 1. 1. 0. 1. 1. 0. 0. 0. 0. 0. 0.]
```

```
Mary and Samantha arrived at the bus station early but waited until noon for the bus[1. 1. 1. 2. 1. 1. 1. 0. 0. 0. 0. 1. 1. 1. 1. 0. 0. 0. 1. 1. 0.]
```

Comme vous pouvez le voir, **chaque phrase a été comparée avec notre liste de mots générée à l'étape 1. Sur la base de la comparaison, la valeur de l'élément du vecteur peut être incrémentée**. Ces vecteurs peuvent être utilisés dans des algorithmes de ML pour la classification de documents et les prédictions.

Nous avons écrit notre code et généré des vecteurs, mais maintenant, comprenons un peu mieux le sac de mots.

### Informations sur le sac de mots

Le modèle BOW ne considère que si un mot connu apparaît dans un document ou non. Il ne se soucie pas de la signification, du contexte et de l'ordre dans lequel ils apparaissent.

Cela donne l'information que des documents similaires auront des comptes de mots similaires les uns aux autres. En d'autres termes, plus les mots dans deux documents sont similaires, plus les documents peuvent être similaires.

### Limites de BOW

1. **Signification sémantique** : l'approche de base de BOW ne considère pas la signification du mot dans le document. Il ignore complètement le contexte dans lequel il est utilisé. Le même mot peut être utilisé à plusieurs endroits en fonction du contexte ou des mots voisins.
2. **Taille du vecteur** : Pour un grand document, la taille du vecteur peut être énorme, ce qui entraîne beaucoup de calculs et de temps. Vous devrez peut-être ignorer des mots en fonction de leur pertinence pour votre cas d'utilisation.

C'était une petite introduction à la méthode BOW. Le code a montré comment cela fonctionne à un niveau bas. Il y a beaucoup plus à comprendre sur BOW. Par exemple, au lieu de diviser notre phrase en un seul mot (1-gram), vous pouvez diviser en paires de deux mots (bi-gram ou 2-gram). Parfois, la représentation bi-gram semble être beaucoup meilleure que l'utilisation de 1-gram. Ceux-ci peuvent souvent être représentés en utilisant la notation N-gram. J'ai listé quelques articles de recherche dans la section ressources pour plus de connaissances approfondies.

Vous n'avez pas à coder BOW chaque fois que vous en avez besoin. Il fait déjà partie de nombreux frameworks disponibles comme CountVectorizer dans sci-kit learn.

Notre code précédent peut être remplacé par :

```
from sklearn.feature_extraction.text import CountVectorizervectorizer = CountVectorizer()X = vectorizer.fit_transform(allsentences)print(X.toarray())
```

Il est toujours bon de comprendre comment les bibliothèques des frameworks fonctionnent, et de comprendre les méthodes derrière elles. Mieux vous comprenez les concepts, meilleure utilisation vous pouvez faire des frameworks.

**Merci d'avoir lu l'article. Le code présenté est disponible sur mon [GitHub](https://gist.github.com/edubey/c52a3b34541456a76a2c1f81eebb5f67).**

Vous pouvez me suivre sur [Medium](https://medium.com/@edubey), [Twitter](https://twitter.com/edubey1), et [LinkedIn](https://www.linkedin.com/in/edubey/). Pour toute question, vous pouvez me contacter par email (praveend806 [at] gmail [dot] com).

### **Ressources pour en savoir plus sur le sac de mots**

1. [Wikipedia-BOW](https://en.wikipedia.org/wiki/Bag-of-words_model)
2. [Understanding Bag-of-Words Model: A Statistical Framework](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.453.5924&rep=rep1&type=pdf)
3. [Semantics-Preserving Bag-of-Words Models and Applications](https://ieeexplore.ieee.org/document/5428847)