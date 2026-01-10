---
title: Comment utiliser Texthero pour préparer un ensemble de données textuelles pour
  votre projet NLP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-22T16:23:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-work-and-understand-text-based-dataset-with-texthero
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/priscilla-du-preez-I79wWVFyhEQ-unsplash.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: nlp
  slug: nlp
- name: Python
  slug: python
seo_title: Comment utiliser Texthero pour préparer un ensemble de données textuelles
  pour votre projet NLP
seo_desc: "By Davis David\nNatural Language Processing (NLP) is one of the most important\
  \ fields of study and research in today’s world. It has many applications in the\
  \ business sector such as chatbots, sentiment analysis, and document classification.\
  \  \nPreproce..."
---

Par Davis David

Le traitement du langage naturel (NLP) est l'un des domaines d'étude et de recherche les plus importants dans le monde actuel. Il a de nombreuses applications dans le secteur des affaires telles que les chatbots, l'analyse des sentiments et la classification de documents. 

La préprocessing et la représentation du texte sont l'une des parties les plus délicates et les plus ennuyeuses du travail sur un projet NLP. Les ensembles de données basés sur du texte peuvent être incroyablement épineux et difficiles à préprocesser. Mais heureusement, le dernier package Python appelé Texthero peut vous aider à résoudre ces défis.

## Qu'est-ce que Texthero ?

Texthero est un simple outil Python qui vous aide à travailler avec un ensemble de données textuelles. Il fournit des fonctionnalités rapides et faciles qui vous permettent de _préprocesser, représenter, mapper en vecteurs_ et _visualiser_ les données textuelles en seulement quelques lignes de code.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/texthero-logo.png)
_Logo Texthero_

Texthero est conçu pour être utilisé sur pandas, il facilite donc le préprocessing et l'analyse des séries ou DataFrames pandas basés sur du texte.

Si vous travaillez sur un projet NLP, Texthero peut vous aider à accomplir les choses plus rapidement qu'avant et vous donne plus de temps pour vous concentrer sur les tâches importantes.

**NOTE :** La bibliothèque Texthero est encore en version bêta. Vous pourriez rencontrer des bugs et les pipelines pourraient changer. Une version plus rapide et meilleure sera publiée et apportera des changements majeurs.

## Aperçu de Texthero

![Image](https://www.freecodecamp.org/news/content/images/2020/07/texthero-modules.jpg)
_Modules Texthero_

Texthero dispose de quatre modules utiles qui gèrent différentes fonctionnalités que vous pouvez appliquer à votre ensemble de données textuelles.

1. [**Prétraitement**](https://texthero.org/docs/api-preprocessing)
Ce module permet le prétraitement efficace des séries ou DataFrames pandas basés sur du texte. Il dispose de différentes méthodes pour nettoyer votre ensemble de données textuelles telles que lowercase(), remove_html_tags() et remove_urls().
2. [**NLP**](https://texthero.org/docs/api-nlp)
Ce module contient quelques tâches NLP telles que named_entities, noun_chunks, etc.
3. [**Représentation**](https://texthero.org/docs/api-representation)
Ce module dispose de différents algorithmes pour mapper les mots en vecteurs tels que TF-IDF, GloVe, Principal Component Analysis (PCA) et term_frequency.
4. [**Visualisation**](https://texthero.org/docs/api-visualization)
Le dernier module dispose de trois méthodes différentes pour visualiser les insights et les statistiques d'un DataFrame pandas basé sur du texte. Il peut tracer un nuage de points et un nuage de mots.

## Installer Texthero

Texthero est gratuit, open-source et bien documenté. Pour l'installer, ouvrez un terminal et exécutez la commande suivante :

```command
pip install texthero
```

Le package utilise de nombreuses autres bibliothèques en backend telles que Gensim, SpaCy, scikit-learn et NLTK. Vous n'avez pas besoin de les installer toutes séparément, pip s'en chargera.

### Comment utiliser Texthero

Dans cet article, j'utiliserai un ensemble de données de nouvelles pour vous montrer comment vous pouvez utiliser différentes méthodes fournies par les modules de Texthero dans votre propre projet NLP.

Nous commencerons par importer les packages Python importants que nous allons utiliser.

```python
#import important packages

import texthero as hero
import pandas as pd
```

Ensuite, nous chargerons un ensemble de données à partir du répertoire de données. L'ensemble de données pour cet article se concentre sur les nouvelles en langue [Swahili](https://medium.com/@Davis_David/meet-the-winners-of-swahili-news-classification-challenge-60f5edd7aa9).

```python
#load dataset 

data = pd.read_csv("data/swahili_news_dataset.csv")
```

Regardons les 5 premières lignes de l'ensemble de données :

```python
# show top 5 rows 

data.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/top-5.PNG)
_5 premières lignes_

Comme vous pouvez le voir, dans notre ensemble de données, nous avons trois colonnes (id, content, et category). Pour cet article, nous nous concentrerons sur la fonctionnalité content.

```python
# select news content only and show top 5 rows

news_content = data[["content"]]
news_content.head()
```

Nous avons créé un nouveau dataframe axé uniquement sur le contenu, puis nous avons affiché les 5 premières lignes.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/news-content.PNG)
_5 premières lignes_

### Prétraitement avec Texthero.

Nous pouvons utiliser la méthode **clean().** pour prétraiter une série pandas basée sur du texte.

```python
# clean the news content by using clean method from hero package

news_content['clean_content'] = hero.clean(news_content['content'])
```

La méthode **clean()** exécute sept fonctions lorsque vous passez une série pandas. Ces sept fonctions sont :

* lowercase(s): Met tout le texte en minuscules.
* remove_diacritics(): Supprime tous les accents des chaînes.
* remove_stopwords(): Supprime tous les mots vides.
* remove_digits(): Supprime tous les blocs de chiffres.
* remove_punctuation(): Supprime toute la ponctuation des chaînes (!"#$%&'()*+,-./:;<=>?@[]^_`{|}~).
* fillna(s): Remplace les valeurs non assignées par des espaces vides.
* remove_whitespace(): Supprime tous les espaces blancs entre les mots.

Maintenant, nous pouvons voir le contenu des nouvelles nettoyé.

```python
#show unclean and clean news content

news_content.head()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/unclean-vs-clean.PNG)
_content vs clean_content_

### Nettoyage personnalisé

Si le pipeline par défaut de la méthode **clean()** ne répond pas à vos besoins, vous pouvez créer un pipeline personnalisé avec la liste des fonctions que vous souhaitez appliquer à votre ensemble de données.

Par exemple, j'ai créé un pipeline personnalisé avec seulement 5 fonctions pour nettoyer mon ensemble de données.

```python
#create custom pipeline
from texthero import preprocessing

custom_pipeline = [preprocessing.fillna,
                   preprocessing.lowercase,
                   preprocessing.remove_whitespace,
                   preprocessing.remove_punctuation,
                   preprocessing.remove_urls,
                   ]
```

Maintenant, je peux utiliser le custome_pipeline pour nettoyer mon ensemble de données.

```python
#altearnative for custom pipeline

news_content['clean_custom_content'] = news_content['content'].pipe(hero.clean, custom_pipeline)
```

Vous pouvez voir l'ensemble de données nettoyé que nous avons créé en utilisant le pipeline personnalisé.

```python
# show output of custome pipeline

news_content.clean_custom_content.head() 
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/custom_clean_pipeline.PNG)
_résultat du pipeline de nettoyage personnalisé_

## Méthodes de prétraitement utiles

Voici quelques autres fonctions utiles des modules de prétraitement que vous pouvez essayer pour nettoyer votre ensemble de données textuelles.

### Supprimer les chiffres

Vous pouvez utiliser la fonction **remove_digits()** pour supprimer les chiffres dans vos ensembles de données textuelles.

```python
text = pd.Series("Hi my phone number is +255 711 111 111 call me at 09:00 am")
clean_text = hero.preprocessing.remove_digits(text)

print(clean_text)
```

sortie : Hi my phone number is +        call me at  :  am   
dtype: object

### Supprimer les mots vides

Vous pouvez utiliser la fonction **remove_stopwords()** pour supprimer les mots vides dans vos ensembles de données textuelles.

```python
text = pd.Series("you need to know NLP to develop the chatbot that you desire")
clean_text = hero.remove_stopwords(text)

print(clean_text) 
```

sortie :    need  know NLP  develop  chatbot   desire  
 dtype: object

### Supprimer les URLs

Vous pouvez utiliser la fonction **remove_urls()** pour supprimer les liens dans vos ensembles de données textuelles.

```python
text = pd.Series("Go to https://www.freecodecamp.org/news/ to read more articles you like")
clean_text = hero.remove_urls(text)

print(clean_text)
```

sortie :   Go to    to read more articles you like   
dtype: object

### Tokenize

Tokenize chaque ligne de la série pandas donnée en utilisant la méthode **tokenize()** et retourne une série pandas où chaque ligne contient une liste de tokens.

```python
text = pd.Series(["You can think of Texthero as a tool to help you understand and work with text-based dataset. "])
clean_text = hero.tokenize(text)

print(clean_text)
```

sortie :   [You, can, think, of, Texthero, as, a, tool, to, help, you, understand, and, work, with, text, based, dataset]  
 dtype: object

### Supprimer les balises HTML

Vous pouvez supprimer les balises html de la série pandas donnée en utilisant la méthode **remove_html_tags()**.

```python
text = pd.Series("<html><body><h2>hello world</h2></body></html>")
clean_text = hero.remove_html_tags(text)

print(clean_text)
```

sortie :   hello world   
dtype: object

## Méthodes de visualisation utiles

Texthero contient différentes méthodes pour visualiser les insights et les statistiques d'un DataFrame pandas basé sur du texte.

### Mots les plus fréquents

Si vous voulez connaître les mots les plus fréquents dans votre ensemble de données textuelles, vous pouvez utiliser la méthode **top_words()** du module de visualisation. Cette méthode est utile si vous voulez voir des mots supplémentaires que vous pouvez ajouter aux listes de mots vides.

Cette méthode ne retourne pas de graphique à barres, donc j'utiliserai **matplotlib** pour visualiser les mots les plus fréquents dans un graphique à barres.

```python
import matplotlib.pyplot as plt

NUM_TOP_WORDS = 20

top_20 = hero.visualization.top_words(news_content['clean_content']).head(NUM_TOP_WORDS)

# Draw the bar chart

top_20.plot.bar(rot=90, title="Top 20 words");

plt.show(block=True);
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/top-2o-words.PNG)

Dans le graphique ci-dessus, nous pouvons visualiser les 20 mots les plus fréquents de notre ensemble de données de nouvelles.

### Nuages de mots

La méthode **wordcloud()** du module de visualisation trace une image en utilisant WordCloud du package word_cloud.

```python
#Plot wordcloud image using WordCloud method
hero.wordcloud(news_content.clean_content, max_words=100,)
```

Nous avons passé la série de dataframe et le nombre maximum de mots (pour cet exemple, il s'agit de 100 mots) dans la méthode **wordcloud()**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/wordclouds.png)
_nuages de mots_

## Méthodes de représentation utiles

Texthero contient différentes méthodes du module de représentation qui vous aident à mapper les mots en vecteurs en utilisant différents algorithmes tels que TF-IDF, word2vec ou GloVe. Dans cette section, je vais vous montrer comment vous pouvez utiliser ces méthodes.

### TF-IDF

Vous pouvez représenter une série pandas basée sur du texte en utilisant TF-IDF. J'ai créé une nouvelle série pandas avec deux morceaux de contenu de nouvelles et les ai représentés en caractéristiques TF_IDF en utilisant la méthode **tfidf()**.

```python
# Create a new text-based Pandas Series.

news = pd.Series(["mkuu wa mkoa wa tabora aggrey mwanri amesitisha likizo za viongozi wote mkoani humo kutekeleza maazimio ya jukwaa la fursa za biashara la mkoa huo", "serikali imetoa miezi sita kwa taasisi zote za umma ambazo hazitumii mfumo wa gepg katika ukusanyaji wa fedha kufanya hivyo na baada ya hapo itafanya ukaguzi na kuwawajibisha"])

#convert into tfidf features 
hero.tfidf(news)
```

sortie : [0.187132760851739, 0.0, 0.187132760851739, 0....  
               [0.0, 0.18557550845969953, 0.0, 0.185575508459...   
dtype: object

**NOTE :** TF-IDF signifie _term frequency-inverse document frequency_.

### Fréquence des termes

Vous pouvez représenter une série pandas basée sur du texte en utilisant la méthode **term_frequency()**. La fréquence des termes (TF) est utilisée pour montrer à quelle fréquence une expression (terme ou mot) apparaît dans un document ou un contenu textuel.

```python

news = pd.Series(["mkuu wa mkoa wa tabora aggrey mwanri amesitisha likizo za viongozi wote mkoani humo kutekeleza maazimio ya jukwaa la fursa za biashara la mkoa huo", "serikali imetoa miezi sita kwa taasisi zote za umma ambazo hazitumii mfumo wa gepg katika ukusanyaji wa fedha kufanya hivyo na baada ya hapo itafanya ukaguzi na kuwawajibisha"])

# Represent a text-based Pandas Series using term_frequency.
hero.term_frequency(news)
```

sortie : [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, ...   
              [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, ...   
dtype: object

### K-means

Texthero peut effectuer l'algorithme de clustering K-means en utilisant la méthode **kmeans()**. Si vous avez un ensemble de données textuelles non étiqueté, vous pouvez utiliser cette méthode pour regrouper le contenu selon leurs similitudes.

Dans cet exemple, je vais créer un nouveau dataframe pandas appelé **news** avec les colonnes suivantes _content, tfidf et kmeans_labels_.

```
column_names = ["content","tfidf", "kmeans_labels"]

news = pd.DataFrame(columns = column_names)

```

Nous utiliserons uniquement les 30 premiers morceaux de contenu nettoyé de notre _news_content dataframe_ et les regrouperons en groupes en utilisant la méthode **kmeans()**.

```python
# collect 30 clean content.
news["content"] = news_content.clean_content[:30]

# convert them into tf-idf features.
news['tfidf'] = (
    news['content']
    .pipe(hero.tfidf)
)

# perform clustering algorithm by using kmeans() 
news['kmeans_labels'] = (
    news['tfidf']
    .pipe(hero.kmeans, n_clusters=5)
    .astype(str)
)
```

Dans le code source ci-dessus, dans le pipeline de la méthode k-means, nous avons passé le nombre de clusters qui est 5. Cela signifie que nous allons regrouper ces contenus en 5 groupes.

Maintenant, le contenu des nouvelles sélectionné a été étiqueté en cinq groupes.

```python
# show content and their labels
news[["content","kmeans_labels"]].head()
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/labeled-content.PNG)
_contenu des nouvelles avec des étiquettes_

### PCA

Vous pouvez également utiliser la méthode **pca()** pour effectuer une analyse en composantes principales sur la série pandas donnée. L'**analyse en composantes principales** (**PCA**) est une technique pour réduire la dimensionnalité de vos ensembles de données. Cela augmente l'interprétabilité tout en minimisant la perte d'informations.

Dans cet exemple, nous utilisons les caractéristiques tfidf du dataframe news et les représentons en deux composantes en utilisant la méthode **pca()**. Enfin, nous afficherons un scatterplot en utilisant la méthode **scatterplot()**.

```
#perform pca
news['pca'] = news['tfidf'].pipe(hero.pca)

#show scatterplot
hero.scatterplot(news, 'pca', color='kmeans_labels', title="news")
```

![Image](https://www.freecodecamp.org/news/content/images/2020/07/scatterplot.PNG)
_Scatter Plot_

## **Conclusion**

Dans cet article, vous avez appris les bases de l'utilisation du package Python Texthero dans votre projet NLP. Vous pouvez en apprendre davantage sur les méthodes disponibles dans la [documentation](https://texthero.org/docs/api-preprocessing).

Vous pouvez télécharger l'ensemble de données et le notebook utilisés dans cet article ici : [https://github.com/Davisy/Texthero-Python-Toolkit](https://github.com/Davisy/Texthero-Python-Toolkit).

Si vous avez appris quelque chose de nouveau ou apprécié la lecture de cet article, veuillez le partager afin que d'autres puissent le voir. En attendant, à la prochaine ! Vous pouvez également me joindre sur Twitter [@Davis_McDavid](https://twitter.com/Davis_McDavid)