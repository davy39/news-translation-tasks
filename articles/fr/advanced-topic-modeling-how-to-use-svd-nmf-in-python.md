---
title: Tutoriel sur la modélisation de sujets – Comment utiliser SVD et NMF en Python
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2023-02-21T18:32:38.000Z'
originalURL: https://freecodecamp.org/news/advanced-topic-modeling-how-to-use-svd-nmf-in-python
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/brett-jordan-M3cxjDNiLlQ-unsplash-cover-img.jpg
tags:
- name: natural language processing
  slug: natural-language-processing
- name: nlp
  slug: nlp
- name: Python
  slug: python
- name: topic modeling
  slug: topic-modeling
seo_title: Tutoriel sur la modélisation de sujets – Comment utiliser SVD et NMF en
  Python
seo_desc: "In the context of Natural Language Processing (NLP), topic modeling is\
  \ an unsupervised learning problem whose goal is to find abstract topics in a collection\
  \ of documents. \nTopic Modeling answers the question: \"Given a text corpus of\
  \ many documents, ..."
---

Dans le contexte du traitement automatique du langage naturel (NLP), la **modélisation de sujets** est un problème d'apprentissage non supervisé dont le but est de trouver des sujets abstraits dans une collection de documents. 

La **modélisation de sujets** répond à la question : "Étant donné un corpus de texte contenant de nombreux documents, pouvons-nous trouver les sujets abstraits dont parle le texte ?"

Dans ce tutoriel, vous allez :

* Apprendre deux techniques puissantes de factorisation de matrices - **Décomposition en valeurs singulières (SVD)** et **Factorisation de matrices non négatives (NMF)**
* Les utiliser pour trouver des sujets dans une collection de documents

À la fin de ce tutoriel, vous serez en mesure de construire vos propres modèles de sujets pour trouver des sujets dans n'importe quel texte. 📚📝 

Commençons.

## Table des matières

1. [Qu'est-ce que la modélisation de sujets ?](#heading-quest-ce-que-la-modelisation-de-sujets)
2. [Équation du score TF-IDF](#heading-equation-du-score-tf-idf)
3. [Modélisation de sujets utilisant la décomposition en valeurs singulières (SVD)](#heading-modelisation-de-sujets-utilisant-la-decomposition-en-valeurs-singulieres-svd)
4. [Qu'est-ce que la SVD tronquée ou k-SVD ?](#heading-quest-ce-que-la-svd-tronquee-ou-k-svd)
5. [Modélisation de sujets utilisant la factorisation de matrices non négatives (NMF)](#heading-modelisation-de-sujets-utilisant-la-factorisation-de-matrices-non-negatives-nmf)
6. [7 étapes pour utiliser SVD pour la modélisation de sujets](#heading-7-etapes-pour-utiliser-svd-pour-la-modelisation-de-sujets)
7. [Comment visualiser les sujets sous forme de nuages de mots](#heading-comment-visualiser-les-sujets-sous-forme-de-nuages-de-mots)
8. [Comment utiliser NMF pour la modélisation de sujets](#heading-comment-utiliser-nmf-pour-la-modelisation-de-sujets)
9. [SVD vs NMF – Aperçu des différences](#heading-svd-vs-nmf-aperçu-des-différences)

## Qu'est-ce que la modélisation de sujets ?

Commençons par comprendre ce qu'est la modélisation de sujets.

Supposons que vous avez un grand corpus de texte contenant plusieurs documents. Vous aimeriez connaître les **sujets clés** qui résident dans la collection donnée de documents sans avoir à lire chaque document.

La modélisation de sujets vous aide à distiller les informations du grand corpus de texte en un certain nombre de sujets. Les sujets sont des groupes de mots qui sont _similaires en contexte_ et qui sont indicatifs des informations dans la collection de documents.

La structure générale de la matrice Document-Terme pour un corpus de texte contenant `M` documents et `N` termes au total est montrée ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/1.png)
_Structure de la matrice Document-Terme_

Analysons la représentation matricielle :

* D1, D2, ..., DM sont les M documents.
* T1, T2, ..., TN sont les N termes

Pour remplir la matrice Document-Terme, utilisons la métrique largement utilisée—le score TF-IDF.

## Équation du score TF-IDF

Le score TF-IDF est donné par l'équation suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/2.png)

où,

* `TF_ij` est le nombre de fois que le terme `Tj` apparaît dans le document `Di`.
* `dfj` est le nombre de documents contenant le terme `Tj`

Un terme qui apparaît fréquemment dans un document particulier, et rarement dans l'ensemble du corpus a un score IDF plus élevé. 

J'espère que vous avez maintenant une compréhension sommaire de la DTM et du score TF-IDF. Passons maintenant en revue les techniques de factorisation de matrices.

## Modélisation de sujets utilisant la décomposition en valeurs singulières (SVD)

L'utilisation de la décomposition en valeurs singulières (SVD) pour la modélisation de sujets est expliquée dans la figure ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/3.jpeg)

La décomposition en valeurs singulières sur la matrice Document-Terme D donne les trois matrices suivantes :

* La matrice des vecteurs singuliers gauches **U**. Cette matrice est obtenue par la décomposition propre de la matrice de Gram **D.D_T**—aussi appelée matrice de similarité des documents. L'entrée i,j de la matrice de similarité des documents indique à quel point le document `i` est similaire au document `j`.
* La matrice des valeurs singulières **S**, qui (valeurs) indiquent l'importance relative des sujets.
* La matrice des vecteurs singuliers droits **V_T**, qui est aussi appelée matrice des termes de sujets. Les sujets dans le texte résident le long des lignes de cette matrice.

Si vous souhaitez rafraîchir le concept de décomposition propre, voici un excellent tutoriel de [Grant Sanderson de 3Blue1Brown](https://www.youtube.com/c/3blue1brown). Il explique les vecteurs propres et les valeurs propres visuellement.

[Contenu intégré](https://www.youtube.com/embed/PFDu9oVAE-g)

Il est tout à fait normal si vous trouvez le fonctionnement de la SVD un peu difficile à comprendre. 🤒 Pour l'instant, vous pouvez penser à la SVD comme une boîte noire qui opère sur votre matrice Document-Terme (DTM) et produit 3 matrices, **U, S**, et **V_T**. Et les sujets résident le long des lignes de la matrice **V_T**. 

![Image](https://www.freecodecamp.org/news/content/images/2023/02/4.jpeg)

**Note** : La SVD est aussi appelée **Indexation sémantique latente (LSI).**

## Qu'est-ce que la SVD tronquée ou k-SVD ?

Supposons que vous avez un corpus de texte de 150 documents. Préféreriez-vous parcourir 150 sujets différents qui décrivent le corpus, ou seriez-vous heureux de lire 10 sujets qui peuvent transmettre le contenu du corpus ?

Eh bien, il est souvent utile de fixer un petit nombre de sujets qui transmettent le mieux le contenu du texte. Et c'est ce qui motive **k-SVD**.

Comme la multiplication de matrices nécessite beaucoup de calculs, il est préférable de choisir les **k plus grandes valeurs singulières**, et les sujets qui leur correspondent. Le fonctionnement de k-SVD est illustré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/5.jpeg)

## Modélisation de sujets utilisant la factorisation de matrices non négatives (NMF)

La factorisation de matrices non négatives (NMF) fonctionne comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/6.jpeg)

La factorisation de matrices non négatives agit sur la matrice Document-Terme et produit les éléments suivants :

* La matrice **W** qui est appelée la **matrice document-sujet**. Cette matrice montre la distribution des sujets à travers les documents du corpus.
* La matrice **H** qui est aussi appelée la **matrice terme-sujet**. Cette matrice capture la signification des termes à travers les sujets.

La NMF est plus facile à interpréter car tous les éléments des matrices **W** et **H** sont maintenant non négatifs. Ainsi, un score plus élevé correspond à une plus grande pertinence.

**Mais comment obtenons-nous les matrices W et H ?** 

La NMF est une technique de factorisation de matrices _non exacte_. Cela signifie que vous ne pouvez pas multiplier W et H pour obtenir la matrice document-terme originale V. 

Les matrices W et H sont initialisées aléatoirement. Et l'algorithme est exécuté de manière itérative jusqu'à ce que nous trouvions un W et un H qui minimisent la fonction de coût. 

La fonction de coût est la norme de Frobenius de la matrice **V - W.H**, comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/e2.png)

La norme de Frobenius d'une matrice A avec m lignes et n colonnes est donnée par l'équation suivante :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/e3.png)

## 7 étapes pour utiliser SVD pour la modélisation de sujets

1️⃣ Pour utiliser SVD pour obtenir des sujets, obtenons d'abord un corpus de texte. La cellule de code suivante contient un texte sur la [programmation informatique](https://en.wikipedia.org/wiki/Computer_programming).

```python
text=["Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task.",

     "Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language (commonly referred to as coding).",

     "The source program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit.",

     "The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem.",

     "Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic.",

     "Tasks accompanying and related to programming include: testing, debugging, source code maintenance, implementation of build systems, and management of derived artifacts, such as the machine code of computer programs.",

     "These might be considered part of the programming process, but often the term software development is used for this larger process with the term programming, implementation, or coding reserved for the actual writing of code.",

     "Software engineering combines engineering techniques with software development practices.",

     "Reverse engineering is a related process used by designers, analysts and programmers to understand and re-create/re-implement"]
```

Le texte pour lequel vous devez trouver des sujets est maintenant prêt.

2️⃣ L'étape suivante consiste à importer la classe `TfidfVectorizer` du module d'extraction de caractéristiques de scikit-learn pour les données textuelles :

```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

Vous utiliserez la classe `TfidfVectorizer` pour obtenir la DTM remplie avec les scores TF-IDF pour le corpus de texte.

3️⃣ Pour utiliser la **SVD tronquée (k-SVD)** discutée précédemment, vous devez importer la classe `TruncatedSVD` du module `decomposition` de scikit-learn :

```python
from sklearn.decomposition import TruncatedSVD
```

▶ Maintenant que vous avez importé tous les modules nécessaires, il est temps de commencer votre quête de sujets dans le texte.

4️⃣ Dans cette étape, vous allez instancier un objet `Tfidfvectorizer`. Appelons-le vectorizer.

```python
vectorizer = TfidfVectorizer(stop_words='english',smooth_idf=True)
# sous le capot - mise en minuscules, suppression des caractères spéciaux, suppression des mots vides
input_matrix = vectorizer.fit_transform(text).todense()
```

Jusqu'à présent, vous avez :

✓ collecté le texte,  
✓ importé les modules nécessaires, et  
✓ obtenu la matrice DTM d'entrée.

Maintenant, vous allez procéder à l'utilisation de SVD pour obtenir des sujets.

5️⃣ Vous allez maintenant utiliser la classe `TruncatedSVD` que vous avez importée à l'étape 3️⃣.

```python
svd_modeling= TruncatedSVD(n_components=4, algorithm='randomized', n_iter=100, random_state=122)
svd_modeling.fit(input_matrix)
components=svd_modeling.components_
vocab = vectorizer.get_feature_names()
```

6️⃣ Écrivons une fonction qui obtient les sujets pour nous.

```python
topic_word_list = []
def get_topics(components):
    for i, comp in enumerate(components):
        terms_comp = zip(vocab,comp)
        sorted_terms = sorted(terms_comp, key= lambda x:x[1], reverse=True)[:7]
        topic=" "
        for t in sorted_terms:
            topic= topic + ' ' + t[0]
        topic_word_list.append(topic)
    print(topic_word_list)
    return topic_word_list
get_topics(components)
```

7️⃣ Et il est temps de visualiser les sujets, et de voir s'ils ont du sens. Lorsque vous appelez la fonction `get_topics()` avec les composants obtenus de SVD comme argument, vous obtiendrez une liste de sujets, et les mots principaux dans chacun de ces sujets.

```python
Topic 1:
    code programming process software term computer engineering

Topic 2:
    engineering software development combines practices techniques used

Topic 3:
    code machine source central directly executed intelligible

Topic 4:
    computer specific task automate complex given instructions

```

Et vous avez vos sujets en seulement 7 étapes. Les sujets semblent-ils bons ?

## Comment visualiser les sujets sous forme de nuages de mots

Dans la section précédente, vous avez imprimé les sujets, et donné un sens aux sujets en utilisant les mots principaux de chaque sujet.

Une autre méthode de visualisation populaire pour les sujets est le **nuage de mots**. Dans un nuage de mots, les termes d'un sujet particulier sont affichés en fonction de leur **signification relative**. Le mot le plus important a la plus grande taille de police, et ainsi de suite.

```python
!pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
for i in range(4):
    wc = WordCloud(width=1000, height=600, margin=3, prefer_horizontal=0.7,scale=1,background_color='black', relative_scaling=0).generate(topic_word_list[i])
    plt.imshow(wc)
    plt.title(f"Topic{i+1}")
    plt.axis("off")
    plt.show()
```

Les nuages de mots pour les sujets 1 à 4 sont montrés dans la grille d'images ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/wc1.jpeg)
_Nuages de sujets de SVD_

Comme vous pouvez le voir, la taille de la police des mots indique leur importance relative dans un sujet. Ces nuages de mots sont aussi appelés nuages de sujets.

## Comment utiliser NMF pour la modélisation de sujets

Dans cette section, vous allez suivre les mêmes étapes que pour SVD. Vous devez d'abord importer la classe `NMF` du module `decomposition` de scikit-learn.

```python
from sklearn.decomposition import NMF
NMF_model = NMF(n_components=4, random_state=1)
W = NMF_model.fit_transform(input_matrix)
H = NMF_model.components_
```

Et ensuite, vous pouvez appeler la fonction `get_topics()` sur la matrice **H** pour obtenir les sujets.

```python
Topic 1:
    code machine source central directly executed intelligible

Topic 2:
    engineering software process development used term combines

Topic 3:
    algorithms programming application different domain expertise formal

Topic 4: 
    computer specific task programming automate complex given
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/wc2.jpeg)
_Nuages de sujets de NMF_

Pour le texte donné, vous pouvez voir que SVD et NMF donnent des nuages de sujets similaires.

## SVD vs NMF – Aperçu des différences

Maintenant, rassemblons les différences entre ces deux techniques de factorisation de matrices pour la modélisation de sujets.

* La SVD est une technique de factorisation de matrices exacte – vous pouvez reconstruire la matrice DTM d'entrée à partir des matrices résultantes.
* Si vous choisissez d'utiliser k-SVD, c'est la meilleure approximation possible de rang k de la matrice DTM d'entrée.
* Bien que la NMF soit une approximation non exacte de la matrice DTM d'entrée, elle est connue pour capturer des sujets plus diversifiés que la SVD.

## Conclusion

J'espère que vous avez apprécié ce tutoriel. Comme prochaine étape, vous pouvez créer votre propre notebook Colab en utilisant les cellules de code de ce tutoriel. Vous n'avez qu'à insérer le texte pour lequel vous souhaitez trouver des sujets, et vous aurez vos sujets et nuages de mots prêts !

Merci pour votre lecture, et bon codage !

### Références et lectures supplémentaires sur la modélisation de sujets

* [Une approche code-first pour le traitement automatique du langage naturel](https://www.fast.ai/2019/07/08/fastai-nlp/) par fast.ai
* [Algèbre linéaire computationnelle](https://www.fast.ai/2017/07/17/num-lin-alg/) par fast.ai

Image de couverture : Photo de [Brett Jordan](https://unsplash.com/ja/@brett_jordan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) sur [Unsplash](https://unsplash.com/photos/M3cxjDNiLlQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)