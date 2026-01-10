---
title: Comment extraire des mots-clés d'un texte avec TF-IDF et Scikit-Learn de Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-07T18:00:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-extract-keywords-from-text-with-tf-idf-and-pythons-scikit-learn-b2a0f3d7e667
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PWe5w-WzMaP14YR3lzLIUA.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: naturallanguageprocessing
  slug: naturallanguageprocessing
- name: Python
  slug: python
- name: text mining
  slug: text-mining
seo_title: Comment extraire des mots-clés d'un texte avec TF-IDF et Scikit-Learn de
  Python
seo_desc: 'By Kavita Ganesan

  Back in 2006, when I had to use TF-IDF for keyword extraction in Java, I ended up
  writing all of the code from scratch. Neither Data Science nor GitHub were a thing
  back then and libraries were just limited.

  The world is much differ...'
---

Par Kavita Ganesan

En 2006, lorsque j'ai dû utiliser TF-IDF pour l'extraction de mots-clés en Java, j'ai fini par écrire tout le code à partir de zéro. Ni la science des données ni GitHub n'existaient à l'époque et les bibliothèques étaient très limitées.

Le monde est bien différent aujourd'hui. Vous avez plusieurs [bibliothèques](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfTransformer.html#sklearn.feature_extraction.text.TfidfTransformer) et [dépôts de code open-source sur Github](https://github.com/topics/tf-idf?o=desc&s=forks) qui fournissent une implémentation décente de TF-IDF. Si vous n'avez pas besoin de beaucoup de contrôle sur la façon dont les calculs TF-IDF sont effectués, je vous recommande vivement de réutiliser des bibliothèques de packages connus tels que [MLLib de Spark](https://spark.apache.org/docs/2.2.0/mllib-feature-extraction.html) ou [scikit-learn de Python](http://scikit-learn.org/stable/).

**Un problème** que j'ai remarqué avec ces bibliothèques est qu'elles sont conçues comme une étape préliminaire pour d'autres tâches comme le clustering, la modélisation de sujets et la classification de texte. [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) peut en fait être utilisé pour extraire des mots-clés importants d'un document afin de comprendre ce qui caractérise un document. Par exemple, si vous travaillez avec des articles de Wikipedia, vous pouvez utiliser tf-idf pour extraire des mots qui sont uniques à un article donné. Ces mots-clés peuvent être utilisés comme un résumé très simple d'un document, et pour l'analyse de texte lorsque nous examinons ces mots-clés dans leur ensemble.

**Dans cet article**, je vais vous montrer comment vous pouvez utiliser scikit-learn pour extraire des mots-clés de documents en utilisant TF-IDF. Nous allons spécifiquement le faire sur un ensemble de données de stack overflow. Si vous voulez accéder au **Jupyter Notebook complet**, veuillez [vous rendre dans mon dépôt](https://github.com/kavgan/data-science-tutorials/tree/master/tf-idf).

**Note importante** : J'assume que les personnes suivant ce tutoriel sont déjà familières avec le concept de TF-IDF. Si ce n'est pas le cas, veuillez vous familiariser avec le concept avant de continuer. Il y a quelques [vidéos en ligne](https://www.youtube.com/results?search_query=tf-idf.) qui donnent une explication intuitive de ce que c'est. Pour une explication plus académique, je recommande l'explication de [mon directeur de thèse](https://www.coursera.org/lecture/text-retrieval/lesson-2-2-tf-transformation-W0NZe).

### Ensemble de données

Dans cet exemple, nous allons utiliser un ensemble de données de Stack Overflow qui est un peu bruyant et simule ce que vous pourriez traiter dans la vie réelle. Vous pouvez trouver cet ensemble de données dans [mon dépôt de tutoriel](https://github.com/kavgan/data-science-tutorials/tree/master/tf-idf/data).

Remarquez qu'il y a **deux fichiers**. Le fichier plus grand, `stackoverflow-data-idf.json` avec 20 000 posts, est utilisé pour calculer la Fréquence Inverse de Document (IDF). Le fichier plus petit, `stackoverflow-test.json` avec 500 posts, sera utilisé comme ensemble de test pour extraire des mots-clés. Cet ensemble de données est basé sur le [dump public de Stack Overflow de Google Big Query](https://cloud.google.com/bigquery/public-data/stackoverflow).

Jetons un coup d'œil à notre ensemble de données. Le code ci-dessous lit une chaîne json par ligne à partir de `data/stackoverflow-data-idf.json` dans un dataframe pandas et imprime son schéma et le nombre total de posts.

Ici, `lines=True` signifie simplement que nous traitons chaque ligne dans le fichier texte comme une chaîne json séparée.

![Image](https://cdn-media-1.freecodecamp.org/images/WHKg5Ngu5mwuBeI4y5UIcysbPM2XDdqMimnL)
_Lire le fichier json et imprimer le schéma et le nombre total de posts de Stack Overflow._

![Image](https://cdn-media-1.freecodecamp.org/images/YAXt6ZDQTvw4R5gWJrtC0UhEqxfmEswodALs)
_Le schéma et le nombre total de posts._

Remarquez que cet ensemble de données de Stack Overflow contient 19 champs, y compris le titre du post, le corps, les tags, les dates et d'autres métadonnées que nous n'avons pas besoin pour ce tutoriel. Pour ce tutoriel, nous nous intéressons principalement au corps et au titre. Ceux-ci deviendront notre source de texte pour l'extraction de mots-clés.

Nous allons maintenant créer un champ qui combine à la fois `body` et `title` afin d'avoir les deux dans un seul champ. Nous allons également imprimer la deuxième entrée de texte dans notre nouveau champ juste pour voir à quoi ressemble le texte.

![Image](https://cdn-media-1.freecodecamp.org/images/QTx3-ZVcC-v2478agne5hwk7UIwH-OvmeigO)

Oh oh, cela ne semble pas très lisible ! Eh bien, c'est à cause de tout le nettoyage qui a été fait dans `pre_process(..)`. Vous pouvez faire beaucoup plus de choses dans `pre_process(..)`, comme éliminer toutes les sections de code et normaliser les mots à leur racine. Pour simplifier, nous allons effectuer uniquement un léger prétraitement.

### Création du vocabulaire et des comptes de mots pour l'IDF

Nous devons maintenant créer le vocabulaire et commencer le processus de comptage. Nous pouvons utiliser [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) pour créer un vocabulaire à partir de tout le texte dans notre `df_idf['text']`, suivi des comptes de mots dans le vocabulaire :

![Image](https://cdn-media-1.freecodecamp.org/images/Vz6XrDGC4Zu6h1JK9xcgu4jTJOn7kpyl-wtB)

Le résultat des deux dernières lignes du code ci-dessus est une représentation de matrice creuse des comptes. Chaque colonne représente un mot dans le vocabulaire. Chaque ligne représente le document dans notre ensemble de données, où les valeurs sont les comptes de mots.

**Notez** que, avec cette représentation, les comptes de certains mots pourraient être 0 si le mot n'est pas apparu dans le document correspondant.

Ici, nous passons deux paramètres à CountVectorizer, `max_df` et `stop_words`. Le premier est simplement pour ignorer tous les mots qui sont apparus dans 85 % des documents, car ceux-ci peuvent être sans importance. Le second est une liste personnalisée de mots vides. Vous pouvez également utiliser des mots vides natifs à sklearn en définissant `stop_words='english'`. La liste de mots vides utilisée pour ce tutoriel peut être trouvée [ici](https://github.com/kavgan/data-science-tutorials/tree/master/tf-idf/resources).

La forme résultante de `word_count_vector` est (20000,124901) puisque nous avons 20 000 documents dans notre ensemble de données (les lignes) et la taille du vocabulaire est de 124 901.

Dans certaines applications de fouille de texte, telles que le clustering et la classification de texte, nous limitons généralement la taille du vocabulaire. Il est vraiment facile de le faire en définissant `max_features=vocab_size` lors de l'instanciation de CountVectorizer. Pour ce tutoriel, limitons la taille de notre vocabulaire à 10 000 :

![Image](https://cdn-media-1.freecodecamp.org/images/pLhHU6UYk86G5P5KUoJ87sc6cYIKnTmDPiuB)

Maintenant, regardons 10 mots de notre vocabulaire :

![Image](https://cdn-media-1.freecodecamp.org/images/SMqynykFACPWIGAlcDN0PQV2vaBw9dAwfA3a)

```
['serializing', 'private', 'struct', 'public', 'class', 'contains', 'properties', 'string', 'serialize', 'attempt']
```

Super, ceux-ci sont principalement liés à la programmation.

### TfidfTransformer pour calculer l'IDF

Il est maintenant temps de calculer les valeurs IDF.

Dans le code ci-dessous, nous prenons essentiellement la matrice creuse de CountVectorizer (`word_count_vector`) pour générer l'IDF lorsque vous invoquez `fit(...)` :

![Image](https://cdn-media-1.freecodecamp.org/images/NpfT2hZD8VVfv2wR0hnGrLRfoOjLi0vtX75f)

**Point extrêmement important** : l'IDF doit toujours être basé sur un grand corpus et doit être représentatif des textes que vous utiliseriez pour extraire des mots-clés. J'ai vu plusieurs articles sur le Web qui calculent l'IDF en utilisant une poignée de documents. Vous **détruirez tout le but** de la pondération IDF si elle n'est pas basée sur un grand corpus car :

1. votre vocabulaire devient trop petit, et
2. vous avez une capacité limitée à observer le comportement des mots que vous connaissez.

### Calcul du TF-IDF et extraction des mots-clés

Une fois que nous avons calculé notre IDF, nous sommes prêts à calculer le TF-IDF puis à extraire les mots-clés principaux des vecteurs TF-IDF.

Dans cet exemple, nous allons extraire les mots-clés principaux pour les questions dans `data/stackoverflow-test.json`. Ce fichier de données contient 500 questions avec des champs identiques à ceux de `data/stackoverflow-data-idf.json` comme nous l'avons vu ci-dessus. Nous allons commencer par lire notre fichier de test, extraire les champs nécessaires — titre et corps — et obtenir les textes dans une liste.

![Image](https://cdn-media-1.freecodecamp.org/images/KnapC5ZcFkMU4dGz3VttCj0gZBPvIVs9nQoO)

L'étape suivante consiste à calculer la valeur tf-idf pour un document donné dans notre ensemble de test en invoquant `tfidf_transformer.transform(...)`. Cela génère un vecteur de scores tf-idf.

Ensuite, nous trions les mots dans le vecteur dans l'ordre **décroissant** des valeurs tf-idf, puis nous itérons pour extraire les n premiers mots-clés. Dans l'exemple ci-dessous, nous extrayons les mots-clés pour le premier document de notre ensemble de test.

![Image](https://cdn-media-1.freecodecamp.org/images/88UsQ05S1GAomTM7V03RNGR3MUm9z5l6n-Jx)

![Image](https://cdn-media-1.freecodecamp.org/images/gfoZfIRRVeyBXoAMNnmgP44BKtEjeVCPTalf)

La méthode `sort_coo(...)` trie essentiellement les valeurs dans le vecteur tout en préservant l'index de colonne. Une fois que vous avez l'index de colonne, il est vraiment facile de rechercher la valeur de mot correspondante comme vous le verriez dans `extract_topn_from_vector(...)` où nous faisons `feature_vals.append(feature_names[idx])`.

### Certains résultats !

Dans cette section, vous verrez la question de stack overflow suivie des mots-clés extraits correspondants.

#### Question sur l'intégration du plugin Eclipse

![Image](https://cdn-media-1.freecodecamp.org/images/fLsoeShixrFFLm-y5IVDzJgPjZzWTO9f360B)
_Mots-clés extraits réels._

D'après les mots-clés ci-dessus, les principaux mots-clés ont en fait du sens, il parle de `eclipse`, `maven`, `integrate`, `war`, et `tomcat`, qui sont tous uniques à cette question spécifique.

Il y a quelques mots-clés qui auraient pu être éliminés comme `possibility` et peut-être même `project`. Vous pouvez le faire en ajoutant plus de mots courants à votre liste de mots vides. Vous pouvez même créer votre propre ensemble de liste de mots vides, [très spécifique à votre domaine](http://kavita-ganesan.com/tips-for-constructing-custom-stop-word-lists/).

Maintenant, regardons un autre exemple.

#### Question sur l'importation SQL

![Image](https://cdn-media-1.freecodecamp.org/images/uTTNMaq3bVfhUEU2q1Ua4VX83KBpbDzWbBtv)
_Mots-clés extraits réels_

Même avec toutes les balises html, grâce au prétraitement, nous sommes en mesure d'extraire ici quelques mots-clés assez intéressants. Le dernier mot `appropriately` pourrait être qualifié de mot vide. Vous pouvez continuer à exécuter différents exemples pour obtenir des idées sur la façon d'affiner les résultats.

Voilà ! Maintenant vous pouvez extraire des mots-clés importants de n'importe quel type de texte !

### Ressources

* [Code source complet et ensemble de données pour ce tutoriel](https://github.com/kavgan/data-science-tutorials/tree/master/tf-idf/)
* Données de stack overflow sur [Google BigQuery](https://cloud.google.com/bigquery/public-data/stackoverflow)

[Suivez mon blog](http://kavita-ganesan.com/subscribe/#.XGs_lpNKigQ) pour en savoir plus sur le Text Mining, le NLP et le Machine Learning d'un point de vue appliqué.

Cet article a été initialement publié sur [kavita-ganesan.com](http://kavita-ganesan.com/extracting-keywords-from-text-with-tf-idf-and-pythons-scikit-learn/).