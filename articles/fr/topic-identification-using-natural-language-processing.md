---
title: Techniques de traitement du langage naturel pour l'identification de sujets
  – Expliqué avec des exemples
subtitle: ''
author: Ibrahim Ogunbiyi
co_authors: []
series: null
date: '2024-01-25T16:16:15.000Z'
originalURL: https://freecodecamp.org/news/topic-identification-using-natural-language-processing
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/pexels-wallace-chuck-3109168.jpg
tags:
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
seo_title: Techniques de traitement du langage naturel pour l'identification de sujets
  – Expliqué avec des exemples
seo_desc: 'There''s a lot of textual information available these days. It ranges from
  articles to social media posts and research papers. So our ability to distill meaningful
  insights is key. This helps us make informed decisions in a wide array of contexts.

  For...'
---

Il existe une grande quantité d'informations textuelles disponibles de nos jours. Cela va des articles aux publications sur les réseaux sociaux et aux articles de recherche. Ainsi, notre capacité à distiller des informations significatives est essentielle. Cela nous aide à prendre des décisions éclairées dans une grande variété de contextes.

Par exemple, vous pouvez analyser un grand volume de contenu textuel pour en extraire un thème commun. Les entreprises et les entreprises utilisent cette technique pour comprendre l'opinion publique sur leur marque. Cela leur permet de prendre des décisions éclairées et d'améliorer leurs services.

La capacité à extraire des thèmes à partir d'une grande quantité de données textuelles est appelée identification de sujets.

Dans cet article, vous apprendrez à utiliser les techniques de NLP pour l'identification de sujets, améliorant ainsi vos compétences en tant que scientifique des données. Alors installez-vous, car cela va être un voyage intéressant.

## Qu'est-ce que l'identification de sujets ?

L'identification de sujets, simplement dit, est un sous-domaine du traitement du langage naturel. Elle implique le processus de découverte et d'organisation automatiques des thèmes ou sujets principaux présents dans une collection de données textuelles.

Il existe plusieurs techniques de traitement du langage naturel (NLP) que vous pouvez utiliser pour identifier des thèmes dans un texte, allant des techniques simples aux techniques plus algorithmiques. Dans cet article, nous examinerons les techniques courantes de NLP utilisées pour l'identification de sujets. Nous les discuterons plus en détail ci-dessous.

J'ai récemment tweeté sur l'essence du NLP. Il s'agit vraiment de statistiques pures, car il existe différentes manipulations que vous pouvez effectuer pour garantir que les nombres servent de représentations pour le texte (puisque les ordinateurs ne comprennent pas le texte).

%[https://twitter.com/Ibrahim_Geek/status/1742877290227187989?s=20] 

## Exigences pour ce projet

Pour que vous puissiez suivre et obtenir une expérience pratique tout en apprenant, vous devez avoir Python 3.x installé sur votre machine.

Nous utiliserons également les bibliothèques suivantes : Gensim, Scikit-Learn et NLTK. Vous pouvez les installer à l'aide de l'installateur de paquets Pip avec la commande suivante :

```bash
pip install gensim nltk scikit-learn
```

## Techniques utilisées en NLP pour l'identification de sujets

Il existe diverses techniques que vous pouvez utiliser pour l'identification de sujets. Dans cet article, vous apprendrez quelques techniques courantes de NLP qui fonctionnent assez bien, allant des méthodes simples et efficaces aux méthodes plus avancées.

### Sac de mots

Le sac de mots (BoW) est une représentation courante utilisée en NLP pour les données textuelles. Vous pouvez l'utiliser pour compter la fréquence à laquelle chaque mot apparaît dans un document.

BoW, dans le contexte de l'identification de sujets, est basé sur l'hypothèse que plus un mot apparaît fréquemment dans un document, plus il est important. Ensuite, vous pouvez utiliser ces mots plus courants pour déduire de quoi parle le document.

Le sac de mots est la technique la plus simple utilisée pour identifier les sujets en NLP. Bien que le sac de mots soit simple et efficace, il est fortement affecté par les mots vides, qui sont des mots courants dans les données textuelles (comme "le", "et", "est", et ainsi de suite).

Mais une fois que vous avez éliminé le problème des mots vides du texte, vous permettant d'effectuer un traitement de texte efficace (en utilisant des techniques comme la normalisation), BoW peut encore s'avérer efficace pour identifier certains sujets principaux.

Regardons comment vous pouvez utiliser BoW pour identifier le sujet ci-dessous.

#### Comment implémenter le sac de mots en Python

Un peu de contexte sur l'article d'exemple que nous utiliserons ici : je l'ai obtenu de la BBC, et il est intitulé "Les États-Unis lèvent l'interdiction des importations de la dernière montre Apple". L'article discute de la levée de l'interdiction des dernières montres d'Apple, Ultra 2 et Series 9.

Maintenant, passons en revue comment implémenter le sac de mots en Python. Je vais diviser ce bloc de code en sections et expliquer chaque partie au fur et à mesure pour le rendre un peu plus facile à digérer.

```python
#importation des bibliothèques nécessaires
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

article = "Les dernières montres intelligentes d'Apple peuvent reprendre leur vente aux États-Unis après que la société technologique a déposé un appel d'urgence auprès des autorités.\
Les ventes des montres Series 9 et Ultra 2 avaient été suspendues aux États-Unis en raison d'un litige de brevet.\
Le corps commercial des États-Unis avait interdit les importations et les ventes de montres Apple avec une technologie pour lire le niveau d'oxygène dans le sang.\
Le fabricant de dispositifs Masimo avait accusé Apple de débaucher son personnel et sa technologie. \
Cela survient après que la Maison Blanche a refusé d'annuler une interdiction des ventes et des importations des montres Series 9 et Ultra 2 qui est entrée en vigueur cette semaine.\
Apple avait déclaré être fortement en désaccord avec la décision.\
Le fabricant d'iPhone a fait une demande d'urgence à la Cour d'appel des États-Unis, qui s'est avérée réussie pour lever l'interdiction."
```

Dans le code ci-dessus, nous importons les bibliothèques nécessaires que nous utiliserons pour implémenter le BoW.

Nous utiliserons la bibliothèque Counter pour compter la fréquence de chaque mot, et la bibliothèque word\_tokenize pour tokeniser le document en jetons de mots individuels afin qu'ils puissent être comptés. Enfin, la bibliothèque stopwords supprimera les mots vides du document.

```python

# Initialiser les mots vides en anglais
english_stopwords = stopwords.words("english")

# convertir l'article en jetons
tokens = word_tokenize(article)

# extraire les mots alphabétiques et convertir en minuscules
alpha_lower_tokens = [word.lower() for word in tokens if word.isalpha()]

# supprimer les mots vides
alpha_no_stopwords = [word for word in alpha_lower_tokens if word not in english_stopwords]

# Compter les mots
BoW = Counter(alpha_no_stopwords)

# 3 mots les plus courants
BoW.most_common(3)
```

Dans le code ci-dessus, nous utilisons la première ligne de code pour extraire tous les mots vides en langue anglaise. Ensuite, la deuxième ligne tokenise la chaîne de l'article en mots individuels. La troisième ligne de code normalise chaque mot en minuscules et n'extrait que les mots alphabétiques de l'article. Les deux dernières lignes de code sont utilisées pour compter la fréquence de chaque mot et sélectionner les trois mots les plus courants.

Voici le résultat du modèle BoW :

```javascript
[('watches', 4), ('us', 4), ('apple', 3), ('emergency', 2)]
```

De cela, nous pouvons déduire que l'article parle des "montres d'Apple aux États-Unis". Comme vous pouvez le voir, avec la simplicité du raisonnement derrière le sac de mots, il est encore possible de déduire un peu de connaissances sur l'article.

### Allocation de Dirichlet latente

L'allocation de Dirichlet latente, ou LDA pour faire court, est un modèle probabiliste populaire utilisé en NLP et en apprentissage automatique pour la modélisation de sujets (utilisation d'algorithmes pour identifier des sujets). Elle est basée sur l'hypothèse que les documents sont des mélanges de sujets, et les sujets sont des mélanges de mots.

En termes simples, LDA est une technique de NLP utilisée pour identifier le sujet auquel appartient un document en fonction des mots qu'il contient.

LDA fonctionne sur la représentation de sac de mots des documents, où chaque document est représenté comme un vecteur de fréquences de mots. Vous pouvez implémenter LDA en utilisant la bibliothèque Gensim en Python (qui est une bibliothèque open source utilisée pour la modélisation de sujets et l'analyse de similarité de documents).

Les étapes pour implémenter LDA incluent :

* **Importer les bibliothèques** : La première étape consiste à importer les bibliothèques nécessaires que vous allez utiliser.
    
* **Préparation des données** : Convertir les données brutes en un format de document, puis tokeniser, supprimer les mots vides, et éventuellement effectuer une lemmatisation ou une radicalisation.
    
* **Créer un dictionnaire et un corpus** : Construire un dictionnaire avec des identifiants de mots uniques. Ensuite, former un corpus de sac de mots représentant la fréquence document-mot.
    
* **Entraîner le modèle LDA** : Utiliser la fréquence document-mot et le dictionnaire pour entraîner le modèle LDA, en définissant le nombre de sujets souhaité.
    
* **Imprimer les sujets** : Explorer et imprimer les sujets découverts.
    

```python
# Importer les bibliothèques nécessaires
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

article = "Les dernières montres intelligentes d'Apple peuvent reprendre leur vente aux États-Unis après que la société technologique a déposé un appel d'urgence auprès des autorités. \
Les ventes des montres Series 9 et Ultra 2 avaient été suspendues aux États-Unis en raison d'un litige de brevet. \
Le corps commercial des États-Unis avait interdit les importations et les ventes de montres Apple avec une technologie pour lire le niveau d'oxygène dans le sang. \
Le fabricant de dispositifs Masimo avait accusé Apple de débaucher son personnel et sa technologie. \
Cela survient après que la Maison Blanche a refusé d'annuler une interdiction des ventes et des importations des montres Series 9 et Ultra 2 qui est entrée en vigueur cette semaine. \
Apple avait déclaré être fortement en désaccord avec la décision. \
Le fabricant d'iPhone a fait une demande d'urgence à la Cour d'appel des États-Unis, qui s'est avérée réussie pour lever l'interdiction."
```

Les lignes de code ci-dessus incluent les bibliothèques nécessaires que nous utiliserons pour implémenter le LDA.

La première ligne de code contient l'objet Dictionary. Ensuite, la deuxième ligne importe le modèle LDA, et la troisième ligne de code contient le `sent_tokenize`, que nous utiliserons pour convertir l'article en document. Après cela, `word_tokenize` tokenisera le document en mots individuels. Enfin, nous avons la bibliothèque `stop_words`.

```python
# convertir l'article en documents
documents = sent_tokenize(article)

# tokeniser et normaliser le document
tokenized_words = [word_tokenize(doc.lower()) for doc in documents]

# supprimer les mots vides et n'extraire que les alphabets
cleaned_token = [[word for word in sentence if word not in english_stopwords and word.isalpha()]
                 for sentence in tokenize_words]

# créer un dictionnaire
dictionary = Dictionary(cleaned_token)

# Créer un corpus à partir du document
corpus = [dictionary.doc2bow(text) for text in cleaned_token]
```

Les lignes de code ci-dessus incluent les étapes de prétraitement qui seront effectuées sur l'article, y compris la conversion de l'article en un document, la normalisation et la tokenisation du document en mots individuels.

La partie suivante supprime les mots vides du texte, puis extrait les mots et les chiffres du document. Après cela, nous créons un dictionnaire, qui est une carte entre chaque mot et son identifiant numérique. La dernière ligne de code crée ensuite un corpus du document.

```javascript
# Construire le modèle LDA
model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=3)

# Imprimer les sujets
print("Sujets identifiés :")
for idx, topic in lda_model.print_topics():
    print(f"Sujet {idx + 1}: {topic}")
```

Le code ci-dessus est utilisé pour entraîner le modèle sur le corpus, puis imprime les 3 principaux sujets de l'article.

Voici le résultat du modèle LDA :

```javascript
Sujets identifiés :
Sujet 1 : 0.045*"9" + 0.045*"ultra" + 0.044*"sales" + 0.044*"2" + 0.043*"series" + 0.043*"watches" + 0.029*"apple" + 0.028*"ruling" + 0.028*"disagrees" + 0.028*"said"
Sujet 2 : 0.051*"maker" + 0.035*"ban" + 0.035*"us" + 0.031*"emergency" + 0.031*"made" + 0.031*"successful" + 0.031*"court" + 0.031*"lifted" + 0.031*"request" + 0.031*"proved"
Sujet 3 : 0.055*"apple" + 0.054*"us" + 0.054*"watches" + 0.031*"sales" + 0.031*"technology" + 0.031*"imports" + 0.031*"authorities" + 0.031*"barred" + 0.031*"appeal" + 0.031*"filed"
```

La technique LDA montre une certaine amélioration par rapport à la méthode BoW. Nous pouvons encore obtenir plus d'informations que l'article parle d'une interdiction liée aux montres Apple de la série Ultra aux États-Unis.

### Factorisation de matrices non négatives

La factorisation de matrices non négatives (NMF), tout comme LDA, est une autre technique de modélisation de sujets qui découvre des sujets latents dans une collection de documents.

Mais au lieu de s'appuyer sur BoW, elle s'appuie sur la représentation de la fréquence des termes-fréquence inverse des documents (TF-IDF) pour capturer et récupérer des thèmes ou sujets cachés à partir des documents.

En incorporant les informations TF-IDF, NMF est capable de peser l'importance des termes, identifiant ainsi plus de motifs cachés. Vous pouvez effectuer NMF en utilisant la bibliothèque Scikit-learn.

### Étapes pour effectuer NMF

* Importer les bibliothèques nécessaires
    
* Préparation des données : Convertir le texte en document, puis effectuer la préparation nécessaire des données comme la suppression des mots vides. La fonction TF-IDF dans Scikit-Learn a un argument qui fait cela.
    
* Convertir le document en une matrice TF-IDF en utilisant le vectoriseur TF-IDF dans Scikit-learn
    
* Appliquer la fonction NMF sur la matrice TF-IDF et spécifier le nombre de sujets que vous voulez et le nombre de mots dans chaque sujet
    
* Enfin, interpréter votre résultat.
    

```python
# importer les bibliothèques nécessaires
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

article = "Les dernières montres intelligentes d'Apple peuvent reprendre leur vente aux États-Unis après que la société technologique a déposé un appel d'urgence auprès des autorités. \
Les ventes des montres Series 9 et Ultra 2 avaient été suspendues aux États-Unis en raison d'un litige de brevet. \
Le corps commercial des États-Unis avait interdit les importations et les ventes de montres Apple avec une technologie pour lire le niveau d'oxygène dans le sang. \
Le fabricant de dispositifs Masimo avait accusé Apple de débaucher son personnel et sa technologie. \
Cela survient après que la Maison Blanche a refusé d'annuler une interdiction des ventes et des importations des montres Series 9 et Ultra 2 qui est entrée en vigueur cette semaine. \
Apple avait déclaré être fortement en désaccord avec la décision. \
Le fabricant d'iPhone a fait une demande d'urgence à la Cour d'appel des États-Unis, qui s'est avérée réussie pour lever l'interdiction."
```

Le code ci-dessus contient les bibliothèques que nous utiliserons pour implémenter NMF et l'article lui-même.

```python
# convertir l'article en documents
documents = sent_tokenize(article)

# Créer un vectoriseur TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english').fit_transform(document)

# Appliquer NMF
num_topics = 5  # Définir le nombre de sujets que vous souhaitez identifier
nmf_model = NMF(n_components=num_topics, init='random', random_state=42)
nmf_matrix = nmf_model.fit_transform(tfidf)
```

Le code ci-dessus convertit l'article en documents. Ensuite, il crée une matrice de fréquence des termes-fréquence inverse des documents de l'article. Les trois dernières lignes de code définissent ensuite le nombre de sujets et créent les sujets à partir de la matrice de documents en utilisant NMF.

Voici le résultat du modèle NMF :

```javascript
Sujet #1 : ultra, series, sales, watches, row, halted, patent, white, house, effect
Sujet #2 : lifted, court, iphone, getting, request, successful, proved, appeals, ban, maker
Sujet #3 : disagrees, strongly, ruling, said, apple, body, blood, level, trade, oxygen
Sujet #4 : filed, resume, appeal, latest, tech, authorities, sold, smart, company, emergency
Sujet #5 : technology, apple, accused, masimo, device, staff, poaching, maker, trade, level
```

Vous pouvez voir que NMF révèle plus d'informations concernant les thèmes du document. Par exemple, vous pouvez dire qu'une autre entreprise appelée Masimo accuse Apple d'une violation de brevet dans leurs montres de la série Ultra.

## Comment choisir quelle technique utiliser ?

Je recommande d'expérimenter avec toutes les approches afin d'obtenir différentes perspectives concernant le contenu de votre document.

Le sac de mots et LDA sont basés sur la fréquence d'apparition des mots, ce qui rend ces techniques utiles pour déduire les thèmes les plus grands/les plus généraux du document.

D'autre part, lors de l'utilisation de NMF, qui est basé sur TF-IDF, des mots moins fréquents peuvent être utilisés pour déduire des sujets supplémentaires et fournir une perspective différente sur le document.

Par exemple, NMF a pu identifier des termes clés comme "Masimo" et "accusé", alors que LDA n'a pas pu le faire. Donc, selon vos besoins, allez-y et expérimentez avec toutes les approches pour voir laquelle est capable de donner de meilleurs résultats.

## Conclusion

Dans cet article, vous avez appris l'identification de sujets et comment vous pouvez l'utiliser pour extraire des thèmes ou des sujets d'un grand document.

Nous avons couvert différentes techniques que vous pouvez utiliser pour identifier les sujets, y compris des techniques simples comme BoW et des techniques plus avancées comme LDA et NMF.

Bonne apprentissage, et à la prochaine.