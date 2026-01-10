---
title: Comment les personnes de différentes villes interagissent dans les salons de
  discussion de freeCodeCamp
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-07T21:05:54.000Z'
originalURL: https://freecodecamp.org/news/how-people-from-different-cities-interact-in-the-freecodecamp-chatrooms-a22378571790
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TKSiMUTSE-fOMa63dLTkmQ.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: statistics
  slug: statistics
- name: 'tech '
  slug: tech
seo_title: Comment les personnes de différentes villes interagissent dans les salons
  de discussion de freeCodeCamp
seo_desc: 'By Déborah Mesquita

  A primer on Inferential statistics and how to extract information from text using
  spaCy


  _They’re talking about this article in the fcc chat-room (haha just kidding! Thanks
  [rawpixel](https://unsplash.com/photos/5eClbgffg8w" rel="...'
---

Par Déborah Mesquita

#### Une introduction aux statistiques inférentielles et comment extraire des informations à partir de texte en utilisant spaCy

![Image](https://cdn-media-1.freecodecamp.org/images/V4WDOCwXnTRsjrQ0mAE0t7DMRWdWjQupUjrc)
_Ils parlent de cet article dans le salon de discussion de fcc (haha, je plaisante ! Merci à [rawpixel](https://unsplash.com/photos/5eClbgffg8w" rel="noopener" target="_blank" title=") pour la photo !)_

En science des données, nous parlons généralement beaucoup de l'[analyse exploratoire des données](https://en.wikipedia.org/wiki/Exploratory_data_analysis) (statistiques descriptives), mais il existe un autre "monde statistique" qui peut également être très utile : le monde des **statistiques inférentielles**. 

> L'analyse statistique inférentielle déduit les propriétés d'une population, par exemple en testant des hypothèses et en dérivant des estimations. Les statistiques descriptives ne concernent que les propriétés des données observées et ne reposent pas sur l'hypothèse que les données proviennent d'une population plus large. — [Inférence statistique](https://en.wikipedia.org/wiki/Statistical_inference)

Dans cet article, nous utiliserons le jeu de données gitter-history de freeCodeCamp open data pour répondre à cette question : **y a-t-il un schéma de mention différent dans les salons de discussion de différentes villes ?**

Nous apprendrons les statistiques inférentielles et comment extraire des informations à partir de texte en utilisant la classe [Matcher](https://spacy.io/api/matcher) de spaCy. D'abord, extrayons les données, puis nous nous mettrons les mains dans les statistiques (hé, c'est amusant ! vous verrez).

### Extraction d'informations avec spacy.Matcher

La manière dont nous utilisons le Matcher est très similaire à la manière dont nous utilisons les expressions régulières (en fait, nous pouvons utiliser regex pour créer des motifs). Chaque règle peut avoir de nombreux motifs, et un motif consiste en une liste de dictionnaires, où chaque dictionnaire décrit un token.

```
// ce motif correspond à tous les tokens == 'hello' (minuscules)
{'LOWER': 'hello'}
```

Créons quelques exemples de choses que nous pouvons extraire des messages.

#### Salutations

Ici, nous avons 4 motifs pour la même règle (`"GREETINGS"`) :

```
matcher = Matcher(nlp.vocab)        
```

```
self.matcher.add("GREETINGS", None,                 [{"LOWER": "good"}, {"LOWER": "morning"}],                   [{"LOWER": "good"}, {"LOWER": "evening"}],                     [{"LOWER": "good"}, {"LOWER": "afternoon"}],                     [{"LOWER": "good"}, {"LOWER": "night"}])
```

```
matches = matcher(text)
```

#### Messages avec ponctuation

Nous pouvons utiliser tous les attributs de token disponibles comme motifs. Voyons si un message contient un token de ponctuation.

```
matcher = Matcher(nlp.vocab)
```

```
self.matcher.add("PUNCT", None,                 [{"IS_PUNCT": True}])
```

```
matches = matcher(text)
```

#### Que ressentent les gens ?

Ici, les choses deviennent un peu plus intéressantes. Nous allons faire correspondre le [lemme](https://en.wikipedia.org/wiki/Lemma_(morphology)) du verbe "être" pour détecter toutes les conjugaisons du verbe. Le matcher permet également d'utiliser des quantificateurs, spécifiés comme la clé `'OP'`. Nous allons faire correspondre tous les tokens d'adverbe après le verbe "être" (avec `'OP': '*'` nous pouvons faire correspondre n'importe lesquels et tous).

Après cela, il y a beaucoup de possibilités pour les deux mots suivants, donc nous utiliserons le token générique `{}` pour les faire correspondre.

```
matcher = Matcher(nlp.vocab)
```

```
self.matcher.add("FEELING", None,                 [                 {"LOWER": "i"}, {"LEMMA":"be"},                    {"POS": "ADV", "OP": "*"},                     {"POS": "ADJ"}                 ])
```

```
matches = matcher(text)
```

#### Mentions

Il n'y a pas d'attribut de token pour @some_token, alors créons-en un.

```
mention_flag = lambda text: bool(re.compile(r'\@(\w+)').match(text))
```

```
IS_MENTION = nlp.vocab.add_flag(mention_flag)
```

```
self.matcher.add("MENTION", None, [{IS_MENTION: True}])
```

```
matches = matcher(text)
```

J'ai construit un jeu de données avec des mentions pour le reste de l'article.

```
[menssage, mention, sent_at, city]
```

Vous pouvez trouver tout le code [ici](https://github.com/dmesquita/chi-square-test-for-homogeneity).

### Une introduction aux statistiques inférentielles

L'inférence statistique est le processus d'utilisation de l'analyse de données pour **déduire les propriétés d'une distribution de probabilité sous-jacente** ([Inférence statistique](https://en.wikipedia.org/wiki/Statistical_inference)).

Nous avons des échantillons et nous voulons les comparer. Avec la statistique de test, nous pouvons mesurer la **probabilité** qu'ils proviennent de la même distribution ou non. En appliquant cela à notre scénario, **si la probabilité que les mentions proviennent de la même distribution est inférieure à un seuil** (définie par nous), alors nous pourrons déduire que **les personnes de différentes villes ont des schémas de mention différents**. 

Définissons quelques concepts pour clarifier les choses (toutes les définitions sont tirées de Wikipedia) :

* **Distribution de fréquence** : une liste, un tableau ou un graphique qui affiche la fréquence de divers résultats dans un [échantillon](https://en.wikipedia.org/wiki/Sampling_(statistics))
* **Hypothèse nulle** : une déclaration générale ou une position par défaut selon laquelle _il n'y a pas de relation entre deux phénomènes mesurés_, ou pas d'association entre les groupes
* **Valeur p** : la probabilité, lorsque l'hypothèse nulle est vraie, d'obtenir un résultat égal ou plus extrême que ce qui a été réellement observé. Plus la valeur p est petite, plus la signification est élevée car elle indique à l'investigateur que l'hypothèse considérée peut ne pas expliquer adéquatement l'observation
* **Signification statistique** : quelque chose est statistiquement significatif s'il nous permet de rejeter l'hypothèse nulle

Une chose à garder à l'esprit lors de la manipulation des tests d'hypothèses statistiques est que cela se passe comme suit :

1. Nous supposons que quelque chose est vrai
2. Ensuite, nous essayons de prouver qu'il est impossible que cela puisse être vrai
3. Ensuite, lorsque nous voyons que, en effet, cela ne peut probablement pas être vrai pour les résultats que nous avons obtenus, nous rejetons l'affirmation

> "**Le test d'hypothèse nulle est un argument [reductio ad absurdum](https://en.wikipedia.org/wiki/Reductio_ad_absurdum) adapté aux statistiques. En essence, une affirmation est considérée comme valide si sa contre-affirmation est improbable**". — [Valeur p](https://en.wikipedia.org/wiki/P-value)

Dans notre cas, nous traitons des variables catégorielles (une variable qui peut prendre l'une des valeurs possibles limitées et généralement fixes). Pour cette raison, nous utiliserons la distribution du chi carré.

> En théorie des probabilités et en statistiques, la **distribution du chi carré** (également **chi carré** ou **distribution _χ2_**) avec _k_ degrés de liberté est la distribution d'une somme des carrés de _k_ variables aléatoires normales standard indépendantes. C'est l'une des distributions de probabilité les plus largement utilisées en statistiques inférentielles, notamment dans les tests d'hypothèses ou dans la construction d'intervalles de confiance. — [Distribution du chi carré](https://en.wikipedia.org/wiki/Chi-squared_distribution)

> "Les statisticiens ont identifié plusieurs distributions courantes, connues sous le nom de distributions de probabilité. À partir de ces distributions, il est possible de calculer la probabilité d'obtenir des scores particuliers en fonction des fréquences auxquelles un score particulier se produit dans une distribution avec ces formes courantes." — [Découverte des statistiques en utilisant R](https://www.discoveringstatistics.com/books/discovering-statistics-using-r/)

### Comprendre le test du chi carré pour l'homogénéité

Nous voulons savoir si la distribution des mentions est la même pour chaque ville. D'abord, nous supposons qu'elles proviennent effectivement de la même population, puis nous obtenons tous les messages de chaque ville et les additionnons. Cette distribution (tous les messages ensemble) devrait être la même pour chaque ville si nous supposons qu'elles proviennent de la même population.

Nous ne pouvons pas prouver que les distributions sont différentes en utilisant les statistiques, mais nous pouvons **rejeter qu'elles sont les mêmes**. 

> "La raison pour laquelle nous avons besoin de l'hypothèse nulle est que nous ne pouvons pas prouver l'hypothèse expérimentale en utilisant les statistiques, mais nous pouvons rejeter l'hypothèse nulle. Si nos données nous donnent la confiance de rejeter l'hypothèse nulle, cela soutient notre hypothèse expérimentale. Cependant, soyez conscient que même si nous pouvons rejeter l'hypothèse nulle, **cela ne prouve pas** l'hypothèse expérimentale — cela la soutient simplement." — [Découverte des statistiques en utilisant R](https://www.discoveringstatistics.com/books/discovering-statistics-using-r/)

C'est très important. Nous ne prouvons pas que l'hypothèse expérimentale (ou alternative) est vraie. Nous disons que **à un niveau de signification donné, il est probable qu'elle soit vraie**. 

> "Ainsi, plutôt que de parler d'accepter ou de rejeter une hypothèse (ce que certains manuels vous disent de faire), nous devrions parler des 'chances d'obtenir les données que nous avons collectées en supposant que l'hypothèse nulle est vraie'." — [Découverte des statistiques en utilisant R](https://www.discoveringstatistics.com/books/discovering-statistics-using-r/)

En essence, lorsque nous collectons des données pour tester des théories, nous ne pouvons parler qu'en termes de **probabilité** d'obtenir un ensemble particulier de données (Field, Andy). Et pour juger cela, nous utilisons les valeurs p.

* **Valeurs p élevées** : vos données sont **probables** avec une hypothèse nulle vraie
* **Valeurs p faibles** : vos données sont **improbables** avec une hypothèse nulle vraie, ([_Comment interpréter correctement les valeurs P_](http://blog.minitab.com/blog/adventures-in-statistics-2/how-to-correctly-interpret-p-values))

Nous fixerons notre niveau de signification à 5 % (seuil de _valeur p_ de 0,05).

D'accord, maintenant revenons au test.

#### Les données

Nous utiliserons le jeu de données de toute l'activité de discussion dans les salons de discussion Gitter de freeCodeCamp. Ce jeu de données peut être trouvé [ici](https://github.com/freeCodeCamp/open-data/tree/master/gitter-history).

![Image](https://cdn-media-1.freecodecamp.org/images/Rn9Wa7jpO7VM8PI2L6DJRjCuzeQz5dcVg3oZ)
_À quoi ressemblent les données après avoir extrait les informations de mention_

Notre échantillon contient tous les messages de San Francisco, Toronto, Boston, Belgrade, Londres et São Paulo envoyés entre le 2015-08-16 et le 2016-08-16 (un an de messages).

#### Conditions pour effectuer le test du chi carré pour l'homogénéité

Pour utiliser le test du chi carré, nous devons remplir certaines conditions :

1. Pour chaque population, la méthode d'échantillonnage est un échantillonnage aléatoire simple
2. Tous les comptes attendus sont de 5 ou plus

Nous supposerons que la première condition est remplie (1 an de données de chaque ville). Voyons si la deuxième condition est remplie.

#### Exploration des données

Puisque nous nous initions aux statistiques, utilisons R au lieu de Python.

J'ai créé un fichier JSON et nous le chargerons dans un dataframe en utilisant la bibliothèque jsonlite. Pour voir le contenu, nous utiliserons la fonction tally.

```
> library(jsonlite)
```

```
> df <- fromJSON("experiment_sample_data.json")
```

```
> library(mosaic)
```

```
> mentiontable <- tally(~city+mention, data=df, margins=T)> mentiontable              mentioncity            NON OUI  Belgrade     184  45  Boston       383 121  London       278  98  SanFrancisco 156  51  SaoPaulo     153 132  Toronto      379  81
```

Il est maintenant temps d'introduire les tableaux de contingence.

* **Tableaux de contingence** : en statistiques, un tableau de contingence (également connu sous le nom de tableau croisé ou crosstab) est un type de tableau dans un format matriciel qui affiche la distribution de fréquence (multivariée) des variables.

Avec `chisq.test`, nous pouvons effectuer des tests de tableau de contingence du chi carré et des tests d'ajustement. Calculons les comptes attendus pour cet échantillon.

Résultat attendu = (somme des données dans cette ligne) × (somme des données dans cette colonne) / données totales.

Ainsi, le nombre attendu de messages avec mentions (mention=OUI) pour la ville de São Paulo est :

285*407/1557 = **74,49903**

La valeur `expected` de `chisq.test` donne les comptes attendus sous l'hypothèse nulle pour toutes les villes :

```
> chisq.test(mentiontable)$expected               mentioncity                 NON       OUI  Belgrade     170.3333  58.66667  Boston       374.8821 129.11790  London       279.6739  96.32606  SanFrancisco 153.9694  53.03057  SaoPaulo     211.9869  73.01310  Toronto      342.1543 117.84571
```

Les comptes attendus sont tous supérieurs à 5, donc nous pouvons effectuer le test.

#### Réalisation du test du chi carré

Nous supposerons que les distributions sont les mêmes, donc la colonne totale est la meilleure estimation de ce que cette distribution devrait être :

```
> tally(~mention, data=df)mention  NON  OUI 1150  407 
```

Le test du chi carré est utilisé pour déterminer s'il existe une différence significative entre les **fréquences attendues** et les **fréquences observées**. 

> Pour chaque cellule, **la fréquence attendue est soustraite de la fréquence observée, la différence est élevée au carré, et le total est divisé par la fréquence attendue**. Les valeurs sont ensuite additionnées sur toutes les cellules. Cette somme est la statistique de test du chi carré — [Le test du chi carré](http://www.tiem.utk.edu/~gross/bioed/bealsmodules/chi-square.html)

Avec la valeur du test du chi carré et avec la valeur pour les degrés de liberté (nombre_de_lignes -1 × nombre_de_colonnes -1), nous pouvons calculer la probabilité d'obtenir les résultats par hasard ou non.

```
> chisq.test(mentiontable)        Test du Chi-deux de Pearson
```

```
data:  mentiontableX-squared = 84.667, df = 5, p-value < 2.2e-16
```

La valeur p est inférieure à la valeur alpha (0,05), donc nous allons **rejeter l'hypothèse nulle**. Cela signifie qu'avec ces résultats pour chaque ville, il est peu probable que toutes les villes aient la même distribution de mentions.

Nous pouvons également examiner la source des différences du test.

#### Examen des résidus pour la source des différences

Nous avons les valeurs attendues pour chaque ville, donc il est possible de voir les résidus : `(observé - attendu) / sqrt(attendu)`

> Le résidu standardisé fournit une mesure de l'écart de l'observé par rapport à l'attendu qui conserve la direction de l'écart (le fait que l'observé soit plus ou moins que l'attendu est intéressant pour les interprétations) pour chaque cellule du tableau. Il est mis à l'échelle de manière similaire à une distribution normale standard, fournissant une échelle pour les écarts "importants" pour les valeurs absolues qui sont supérieures à 2 ou 3. — [Statistiques intermédiaires avec R](http://www.math.montana.edu/courses/s217/documents/_book/chapter5.html#section5-7)

```
mosaicplot(mentiontable, shade=T)
```

![Image](https://cdn-media-1.freecodecamp.org/images/qXLkO1vvnbN4BlPFEsxGUR0r425Qn6ZSOPEV)
_Tracé en mosaïque_

Pour São Paulo et Toronto, le nombre de messages avec mention et sans mention semble être à plus de 2,4 écarts types des valeurs attendues. Le salon de discussion de São Paulo a **plus de personnes** mentionnant d'autres personnes que prévu, et pour Toronto, il y a **moins de personnes** mentionnant d'autres personnes que prévu.

C'est intéressant. Une prochaine étape serait d'explorer les sources de ces différences. Peut-être est-ce dû au nombre de personnes dans chaque salon de discussion ? Ou peut-être se connaissent-ils déjà, donc ils ont plus de conversations en tête-à-tête ?

### En conclusion

En statistiques inférentielles, nous **déduisons les propriétés d'une distribution de probabilité sous-jacente**. Lorsque vous avez une variable catégorielle, vous pouvez utiliser le test du chi carré pour trouver la probabilité que la distribution soit la même pour deux populations ou plus (ou sous-groupes d'une population).

Et les étapes pour utiliser un test d'hypothèse statistique sont :

1. D'abord, supposer que l'hypothèse nulle est vraie
2. Ensuite, essayer de prouver qu'il est impossible qu'elle puisse être vraie
3. Ensuite, si nous voyons que, en effet, cela ne peut probablement pas être vrai pour les résultats que nous avons obtenus, nous rejetons l'hypothèse nulle (ou sinon nous échouons à rejeter et acceptons que les données soutiennent l'hypothèse expérimentale)

En outre, nous avons également vu que Spacy.Matcher est un excellent moyen d'extraire des informations à partir de texte. Ici, nous avons fait l'expérience avec les mentions de chaque message, mais [le code](https://github.com/dmesquita/chi-square-test-for-homogeneity) contient d'autres motifs extraits que nous pourrions explorer.

Et c'est tout ! Merci d'avoir lu !