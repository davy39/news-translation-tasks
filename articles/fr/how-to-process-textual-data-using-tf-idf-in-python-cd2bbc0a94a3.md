---
title: Comment traiter les données textuelles en utilisant TF-IDF en Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-06T16:07:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-process-textual-data-using-tf-idf-in-python-cd2bbc0a94a3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JTk6iVMiZCQCr8duiaKlHQ.png
tags:
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment traiter les données textuelles en utilisant TF-IDF en Python
seo_desc: 'By Mayank Tripathi

  Computers are good with numbers, but not that much with textual data. One of the
  most widely used techniques to process textual data is TF-IDF. In this article,
  we will learn how it works and what are its features.

  From our intuiti...'
---

Par Mayank Tripathi

Les ordinateurs sont bons avec les nombres, mais pas autant avec les données textuelles. L'une des techniques les plus largement utilisées pour traiter les données textuelles est le TF-IDF. Dans cet article, nous allons apprendre comment cela fonctionne et quelles sont ses caractéristiques.

Selon notre intuition, nous pensons que les mots qui apparaissent plus souvent devraient avoir un poids plus grand dans l'analyse des données textuelles, mais ce n'est pas toujours le cas. Des mots tels que « the », « will » et « you » — appelés **stopwords** — apparaissent le plus dans un corpus de texte, mais sont de très peu de signification. Au lieu de cela, les mots qui sont rares sont ceux qui aident réellement à distinguer les données et qui portent plus de poids.

### Introduction au TF-IDF

**TF-IDF** signifie « Term Frequency — Inverse Data Frequency ». Tout d'abord, nous allons apprendre ce que ce terme signifie mathématiquement.

**Term Frequency (tf)** : nous donne la fréquence du mot dans chaque document du corpus. C'est le rapport du nombre de fois où le mot apparaît dans un document par rapport au nombre total de mots dans ce document. Il augmente à mesure que le nombre d'occurrences de ce mot dans le document augmente. Chaque document a son propre tf.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HM0Vcdrx2RApOyjp_ZeW_Q.png)

**Inverse Data Frequency (idf)** : utilisé pour calculer le poids des mots rares dans tous les documents du corpus. Les mots qui apparaissent rarement dans le corpus ont un score IDF élevé. Il est donné par l'équation ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*A5YGwFpcTd0YTCdgoiHFUw.png)

En combinant ces deux éléments, nous obtenons le score TF-IDF (w) pour un mot dans un document du corpus. C'est le produit de tf et idf :

![Image](https://cdn-media-1.freecodecamp.org/images/1*nSqHXwOIJ2fa_EFLTh5KYw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*q2tRgjV_J-MLvnhwNAl0KQ.png)

Prenons un exemple pour avoir une compréhension plus claire.

Phrase 1 : The car is driven on the road.

Phrase 2 : The truck is driven on the highway.

Dans cet exemple, chaque phrase est un document séparé.

Nous allons maintenant calculer le TF-IDF pour les deux documents ci-dessus, qui représentent notre corpus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*q3qYevXqQOjJf6Pwdlx8Mw.png)

D'après le tableau ci-dessus, nous pouvons voir que le TF-IDF des mots courants était zéro, ce qui montre qu'ils ne sont pas significatifs. En revanche, le TF-IDF de « car », « truck », « road » et « highway » sont non nuls. Ces mots ont plus de signification.

### Utilisation de Python pour calculer le TF-IDF

Maintenant, codons le TF-IDF en Python à partir de zéro. Après cela, nous verrons comment nous pouvons utiliser sklearn pour automatiser le processus.

La fonction `computeTF` calcule le score TF pour chaque mot dans le corpus, par document.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AgBLM-NRFEpWVhXM7I3XjQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RE_h1NoBqyW24oGU3tthew.png)

La fonction `computeIDF` calcule le score IDF de chaque mot dans le corpus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EjHweFHuNa-rznvdPQaRbQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*cGGCFDVZRdh4yVWKdUKj1g.png)

La fonction `computeTFIDF` ci-dessous calcule le score TF-IDF pour chaque mot, en multipliant les scores TF et IDF.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QSTMOhLvIEcRtrEBzwrfPA.png)

La sortie produite par le code ci-dessus pour l'ensemble des documents D1 et D2 est la même que celle que nous avons calculée manuellement ci-dessus dans le tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aLUwNr58mazdfs7DHT1Z6Q.png)

Vous pouvez vous référer à [ce lien](https://github.com/mayank408/TFIDF) pour l'implémentation complète.

#### sklearn

Maintenant, nous allons voir comment nous pouvons implémenter cela en utilisant sklearn en Python.

Tout d'abord, nous allons importer `TfidfVectorizer` depuis `sklearn.feature_extraction.text` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*w9tnnHtsjZwyuFhve5uM1g.png)

Maintenant, nous allons initialiser le `vectorizer` puis appeler fit et transform pour calculer le score TF-IDF pour le texte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*H0_K3rA-tK3hP8KUdq3o8A.png)

Sous le capot, le fit_transform de sklearn exécute les fonctions `fit` et `transform` suivantes. Celles-ci peuvent être trouvées dans la bibliothèque officielle sklearn sur GitHub.

```py

def fit(self, X, y=None):
    """Apprendre le vecteur idf (poids globaux des termes)
    Paramètres
    ----------
    X : matrice creuse, [n_samples, n_features]
        une matrice de comptes de termes/jetons
    """
    if not sp.issparse(X):
        X = sp.csc_matrix(X)
    if self.use_idf:
        n_samples, n_features = X.shape
        df = _document_frequency(X)

        # effectuer le lissage idf si nécessaire
        df += int(self.smooth_idf)
        n_samples += int(self.smooth_idf)

        # log+1 au lieu de log pour s'assurer que les termes avec un idf zéro ne sont pas
        # entièrement supprimés.
        idf = np.log(float(n_samples) / df) + 1.0
        self._idf_diag = sp.spdiags(idf, diags=0, m=n_features,
                                    n=n_features, format='csr')

    return self

def transform(self, X, copy=True):
    """Transformer une matrice de comptes en une représentation tf ou tf-idf
    Paramètres
    ----------
    X : matrice creuse, [n_samples, n_features]
        une matrice de comptes de termes/jetons
    copy : booléen, par défaut True
        Si on copie X et opère sur la copie ou si on effectue des opérations en place.
    Retourne
    -------
    vectors : matrice creuse, [n_samples, n_features]
    """
    if hasattr(X, 'dtype') and np.issubdtype(X.dtype, np.floating):
        # préserver le type de données de la famille float
        X = sp.csr_matrix(X, copy=copy)
    else:
        # convertir les comptes ou occurrences binaires en floats
        X = sp.csr_matrix(X, dtype=np.float64, copy=copy)

    n_samples, n_features = X.shape

    if self.sublinear_tf:
        np.log(X.data, X.data)
        X.data += 1

    if self.use_idf:
        check_is_fitted(self, '_idf_diag', 'le vecteur idf n'est pas ajusté')

        expected_n_features = self._idf_diag.shape[0]
        if n_features != expected_n_features:
            raise ValueError("L'entrée a n_features=%d tandis que le modèle"
                             " a été entraîné avec n_features=%d" % (
                                 n_features, expected_n_features))
        # *= ne fonctionne pas
        X = X * self._idf_diag

    if self.norm:
        X = normalize(X, norm=self.norm, copy=False)

    return X
```

Une chose à noter dans le code ci-dessus est que, au lieu de simplement le log de n_samples, 1 a été ajouté à n_samples pour calculer le score IDF. Cela garantit que les mots avec un score IDF de zéro ne sont pas entièrement supprimés.

La sortie obtenue est sous la forme d'une matrice biaisée, qui est normalisée pour obtenir le résultat suivant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_Pk4czfcod_vFlFugWysA.png)

Ainsi, nous avons vu comment nous pouvons facilement coder le TF-IDF en seulement 4 lignes en utilisant sklearn. Maintenant, nous comprenons à quel point le TF-IDF est puissant en tant qu'outil pour traiter les données textuelles d'un corpus. Pour en savoir plus sur le TF-IDF de sklearn, vous pouvez utiliser [ce lien](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html).

**Bon codage !**

Merci d'avoir lu cet article. N'oubliez pas de le partager si vous le trouvez utile.

Pour plus d'informations sur la programmation, vous pouvez me suivre, afin d'être averti chaque fois que je publie un nouvel article.

Santé !

De plus, restons connectés sur [**Twitter**](https://twitter.com/mayank_408), [**Linkedin**](https://www.linkedin.com/in/mayank-tripathi-a49563126/), [**Github**](https://github.com/mayank408) et [**Facebook**](https://www.facebook.com/profile.php?id=100001106266064).