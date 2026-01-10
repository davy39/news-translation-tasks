---
title: Classification et prédiction de texte en utilisant l'approche Bag Of Words
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T21:40:55.000Z'
originalURL: https://freecodecamp.org/news/text-classification-and-prediction-using-bag-of-words-8aeb1396cded
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wdtdcVQQRzc7xPNZzyCsUg.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: scikit learn
  slug: scikit-learn
- name: 'tech '
  slug: tech
seo_title: Classification et prédiction de texte en utilisant l'approche Bag Of Words
seo_desc: 'By gk_

  There are a number of approaches to text classification. In other articles I’ve
  covered Multinomial Naive Bayes and Neural Networks.

  One of the simplest and most common approaches is called “Bag of Words.” It has
  been used by commercial analyt...'
---

Par gk_

Il existe plusieurs approches pour la classification de texte. Dans d'autres articles, j'ai abordé [Multinomial Naive Bayes](https://chatbotslife.com/text-classification-using-algorithms-e4d50dcba45) et [Neural Networks](https://machinelearnings.co/text-classification-using-neural-networks-f5cd7b8765c6).

L'une des approches les plus simples et les plus courantes s'appelle « Bag of Words ». Elle a été utilisée par des produits d'analyse commerciaux tels que [Clarabridge](https://www.clarabridge.com/), [Radian6](https://www.webanalyticsworld.net/analytics-measurement-and-management-tools/radian-6-overview), et d'autres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*j3HUg18QwjDJTJwW9ja5-Q.png)
_Image [source](https://machinelearnings.co/text-classification-using-neural-networks-f5cd7b8765c6" rel="noopener" target="_blank" title=")._

L'approche est relativement simple : étant donné un ensemble de sujets et un ensemble de termes associés à chaque sujet, déterminer quel(s) sujet(s) existe(nt) dans un document (par exemple, une phrase).

Bien que d'autres algorithmes plus exotiques organisent également les mots en « sacs », dans cette technique, nous ne créons pas de modèle ni n'appliquons de mathématiques à la manière dont ce « sac » intersecte avec un document classé. La classification d'un document sera polymorphe, car elle peut être associée à plusieurs sujets.

Cela semble-t-il trop simple pour être utile ? Essayez-le avant de tirer des conclusions. En NLP, il est souvent vrai qu'une approche simple peut parfois aller loin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aIUBmmPz2K44OdZnWCj4jw.png)
_crédit : Smitha Milli [https://twitter.com/smithamilli](https://twitter.com/smithamilli/status/837153616116985856" rel="noopener" target="_blank" title=")_

Nous aurons besoin de trois choses :

* Un fichier de définition des sujets/mots
* Une fonction de classification
* Un notebook pour tester notre classificateur

Ensuite, nous irons un peu plus loin et construirons et testerons un modèle prédictif en utilisant nos données de classification.

#### Sujets et mots

Notre fichier de définition est au format JSON. Nous l'utiliserons pour classer les messages entre les patients et une infirmière assignée à leurs soins.

#### topics.json

Il y a deux éléments à noter dans cette définition.

Premièrement, examinons certains termes. Par exemple, « bruis » est une **racine**. Elle couvrira des supersets tels que « bruise », « bruising », et ainsi de suite. Deuxièmement, les termes contenant * sont en fait des **motifs**, par exemple ***dpm** est un motif pour un chiffre numérique suivi de « pm ».

Pour garder les choses simples, nous ne traitons que la correspondance de motifs numériques, mais cela pourrait être étendu à un champ plus large.

Cette capacité de trouver des motifs dans un terme est très utile pour classer des documents contenant des dates, des heures, des valeurs monétaires, etc.

Essayons quelques classifications.

Le classificateur retourne un ensemble de résultats JSON contenant la ou les phrases associées à chaque sujet trouvé dans le message. Un message peut contenir plusieurs phrases, et une phrase peut être associée à aucun, un ou plusieurs sujets.

Examinons notre classificateur. Le code est [ici](https://github.com/ugik/notebooks/blob/master/msgClassify.py).

#### msgClassify.py

Le code est relativement simple et inclut une fonction de commodité pour diviser un document en phrases.

#### Modélisation prédictive

La classification agrégée pour **un ensemble de documents associés à un résultat** peut être utilisée pour construire un modèle prédictif.

Dans ce cas d'utilisation, nous voulions voir si nous pouvions prédire les hospitalisations en fonction des messages entre le patient et l'infirmière avant l'incident. Nous avons comparé les messages des patients qui ont et n'ont pas subi d'hospitalisations.

Vous pourriez utiliser une technique similaire pour d'autres types de messagerie associés à un résultat binaire.

Ce processus comprend plusieurs étapes :

* Un ensemble de messages est classé et chaque sujet reçoit un compte pour cet ensemble. Le résultat est **une liste fixe de sujets avec une allocation en % des messages.**
* L'allocation des sujets est ensuite **assignée à une valeur binaire**, dans notre cas 0 s'il n'y a pas eu d'hospitalisation et 1 s'il y a eu une hospitalisation
* Un algorithme de **régression logistique** est utilisé pour construire un modèle prédictif
* Le modèle est utilisé pour **prédire le résultat à partir de nouvelles entrées**

Examinons nos données d'entrée. Vos données doivent avoir une structure similaire. Nous utilisons un pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html).

![Image](https://cdn-media-1.freecodecamp.org/images/1*SRMLWhU-cEgK_ludaN9gMQ.png)

**« incident »** est le résultat binaire, et il doit être la première colonne dans les données d'entrée.

Chaque colonne suivante est un sujet et le % de classification de l'ensemble de messages appartenant au patient.

Dans la ligne 0, nous voyons qu'environ un quart des messages de ce patient concernent le sujet **thanks**, et aucun ne concerne **medical terms** ou **money**. Ainsi, chaque ligne est un résultat binaire et un **profil de classification de messagerie** à travers les sujets.

Vos données d'entrée auront des sujets différents, des étiquettes de colonnes différentes et une condition binaire différente, mais auront sinon une structure similaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*SE1UtYrUBvtca6qmwN3P2g.png)

Utilisons [scikit-learn](http://scikit-learn.org/stable/) pour construire une régression logistique et tester notre modèle.

Voici notre sortie :

```
precision    recall  f1-score   support          0       0.66      0.69      0.67       191          1       0.69      0.67      0.68       202avg / total       0.68      0.68      0.68       393
```

La [précision et le rappel](https://en.wikipedia.org/wiki/Precision_and_recall) de ce modèle par rapport aux données de test sont dans les années 60 supérieures — **légèrement mieux qu'une supposition**, et malheureusement pas assez précis pour être d'une grande valeur.

Dans cet exemple, la quantité de données était relativement faible (un millier de patients, ~30 messages échantillonnés par patient). N'oubliez pas que seule la moitié des données peut être utilisée pour l'entraînement, tandis que l'autre moitié (après mélange) est utilisée pour le test.

En incluant des données structurées telles que l'âge, le sexe, la condition, les incidents passés, etc., nous pourrions renforcer notre modèle et produire un signal plus fort. Avoir plus de données serait également utile car le nombre de colonnes de données d'entraînement est assez grand.

Essayez cela avec vos données structurées/non structurées et voyez si vous pouvez obtenir un modèle hautement prédictif. Vous n'obtiendrez peut-être pas le type de précision qui mène à des actions automatisées, mais une probabilité de « risque » pourrait être utilisée comme filtre ou fonction de tri ou comme signe d'alerte précoce pour les experts humains.

L'approche « Bag of Words » est adaptée à certains types de travail de classification de texte, en particulier lorsque le langage n'est pas nuancé.

**Profitez.**