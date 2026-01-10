---
title: Comment développer votre mémoire musculaire pour la Science des Données avec
  Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-22T23:38:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-up-your-muscle-memory-for-data-science-with-python-5960df1c930e
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca8fb740569d1a4ca819a.jpg
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'self-improvement '
  slug: self-improvement
- name: 'tech '
  slug: tech
seo_title: Comment développer votre mémoire musculaire pour la Science des Données
  avec Python
seo_desc: 'By Zhen Liu

  Up first: data preprocessing

  Do you feel frustrated by breaking your data analytics flow when searching for syntax?
  Why do you still not remember it after looking up it for the third time?? It’s because
  you haven’t practiced it enough to ...'
---

Par Zhen Liu

#### Pour commencer : le prétraitement des données

Vous sentez-vous frustré de rompre votre flux d'analyse de données lorsque vous recherchez la syntaxe ? Pourquoi ne vous en souvenez-vous toujours pas après l'avoir cherchée pour la troisième fois ?? C'est parce que vous ne l'avez pas assez pratiquée pour développer une mémoire musculaire.

Maintenant, imaginez que lorsque vous codez, la syntaxe et les fonctions Python sortent de vos doigts en suivant vos pensées analytiques. C'est génial, n'est-ce pas ! Ce tutoriel est là pour vous aider à y parvenir.

Je recommande de pratiquer ce script chaque matin pendant 10 minutes, et de le répéter pendant une semaine. **C'est comme faire quelques petits crunchs par jour — pas pour vos abdos, mais pour vos muscles de la science des données.** Graduellement, vous remarquerez une amélioration de l'efficacité de la programmation d'analyse de données après cet entraînement répété.

Pour commencer mon "entraînement de science des données", dans ce tutoriel, nous pratiquerons la syntaxe la plus courante pour le **prétraitement des données** comme séance d'échauffement ;)

```
Contenu :
```

```
0 . Lire, Visualiser et Sauvegarder les données1 . Dimension et Types de Données de la Table2 . Manipulation Basique des Colonnes3 . Valeurs Null : Visualisation, Suppression et Imputation4 . Déduplication des Données
```

### 0. Lire, Visualiser et Sauvegarder les données

Tout d'abord, chargez les bibliothèques pour notre exercice :

Maintenant, nous allons lire les données depuis mon dépôt GitHub. J'ai téléchargé les données depuis [Zillow](https://www.zillow.com/research/data/#other-metrics).

Et les résultats ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*eaM_mFSWaGj89cAvF7Bnsg.png)

Sauvegarder un fichier se fait avec dataframe.to_csv(). Si vous ne voulez pas que le numéro d'index soit sauvegardé, utilisez dataframe.to_csv(index = False).

### 1 . Dimension et Types de Données de la Table

#### 1.1 Dimension

Combien de lignes et de colonnes dans ces données ?

#### 1.2 Types de Données

Quels sont les types de données de vos données, et combien de colonnes sont numériques ?

Sortie des types de données des premières colonnes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*JLYBz5WpEUcFGHdCPlXJGg.png)

Si vous voulez être plus spécifique sur vos données, utilisez select_dtypes() pour inclure ou exclure un type de données. Question : si je veux seulement regarder les données de 2018, comment faire ?

### 2. Manipulation Basique des Colonnes

#### 2.1 Sous-ensemble de données par colonnes

Sélectionnez les colonnes par types de données :

Par exemple, si vous ne voulez que les colonnes float et integer :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bBq6iH8R-W4g6Cd3HP674g.png)

Sélectionnez et supprimez les colonnes par noms :

![Image](https://cdn-media-1.freecodecamp.org/images/1*d795R8XUxwjkwc1nVRUgGQ.png)

#### 2.2 Renommer les Colonnes

Comment renommer les colonnes si je ne les aime pas ? Par exemple, changer 'State' en 'state_'; 'City' en 'city_' :

### 3. Valeurs Null : Visualisation, Suppression et Imputation

#### 3.1 Combien de lignes et de colonnes ont des valeurs null ?

Les sorties de isnull.any() versus isnull.sum() :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jyJODeWUJR1k4-GQk7tRrw.png)
_isnull.any()_

![Image](https://cdn-media-1.freecodecamp.org/images/1*fun7aRvU3jjbtKmBZmKsag.png)
_isnull.sum()_

Sélectionnez les données qui ne sont pas null dans une colonne, par exemple, 'Metro' n'est pas null.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VqOIxXhSLWhSKxbRNG35-A.png)
_Lignes avec des valeurs 'Metro' N/A_

#### 3.2 Sélectionnez les lignes qui ne sont pas null pour un ensemble fixe de colonnes

Sélectionnez un sous-ensemble de données qui n'a pas de null après 2000 :

Si vous voulez sélectionner les données de juillet, vous devez trouver les colonnes contenant '-07'. Pour voir si une chaîne contient une sous-chaîne, vous pouvez utiliser substring in string, et cela retournera vrai ou faux.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3nalUQfXwC_Ywa-r8YsJ0w.png)

#### 3.3 Sous-ensemble de Lignes par Valeurs Null

Sélectionnez les lignes où nous voulons avoir au moins 50 valeurs non-NA, mais sans besoin d'être spécifique sur les colonnes :

#### 3.4 Supprimer et Imputer les Valeurs Manquantes

Remplir NA ou imputer NA :

Utilisez votre propre condition pour remplir en utilisant la fonction where :

### 4. Déduplication des Données

Nous devons nous assurer qu'il n'y a pas de lignes dupliquées avant d'agréger les données ou de les joindre.

Nous voulons voir s'il y a des villes/régions dupliquées. Nous devons décider quel identifiant unique (ville, région) nous voulons utiliser dans l'analyse.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GhiZCDmg_I-nE8vowIIGsA.png)
_Définit keep=False pour voir toutes les lignes dupliquées par 'RegionName'_

#### Supprimer les valeurs dupliquées.

La combinaison 'CountyName' et 'SizeRank' est déjà unique. Nous utilisons donc ces colonnes pour démontrer la syntaxe de drop_duplicated.

C'est tout pour la première partie de ma série sur le développement de la mémoire musculaire pour la science des données en Python. _Le script complet peut être trouvé [ici](https://gist.github.com/zhendata/5d73068e5b31b616938af51bedf65382)._

Restez à l'écoute ! Mon prochain tutoriel vous montrera comment "muscler la science des données" pour découper et analyser les données.

Suivez-moi et donnez-moi quelques applaudissements si vous trouvez cela utile :)

Pendant que vous travaillez sur Python, peut-être serez-vous intéressé par mon article précédent :

[**Apprendre Spark pour l'Analyse de Big Data en 15 mins！**](https://towardsdatascience.com/learn-spark-essentials-in-15-mins-cf1495882ae0)  
[_Je vous garantis que ce court tutoriel vous fera économiser un TON de temps à lire les longues documentations. Prêt à..._towardsdatascience.com](https://towardsdatascience.com/learn-spark-essentials-in-15-mins-cf1495882ae0)