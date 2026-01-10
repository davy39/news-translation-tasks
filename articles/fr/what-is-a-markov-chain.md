---
title: Qu'est-ce que les chaînes de Markov ? Expliqué avec des exemples de code Python
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-07-08T12:53:27.000Z'
originalURL: https://freecodecamp.org/news/what-is-a-markov-chain
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/miltiadis-fragkidis-2zGTh-S5moM-unsplash.jpg
tags:
- name: Python
  slug: python
- name: statistics
  slug: statistics
seo_title: Qu'est-ce que les chaînes de Markov ? Expliqué avec des exemples de code
  Python
seo_desc: 'There are various mathematical tools that can be used to predict the near
  future based on a current state. One of the most widely used are Markov chains.

  Markov chains allow you to predict the uncertainty of future events under certain
  conditions. Fo...'
---

Il existe divers outils mathématiques qui peuvent être utilisés pour prédire le futur proche en fonction d'un état actuel. L'un des plus largement utilisés sont les chaînes de Markov.

Les chaînes de Markov vous permettent de prédire l'incertitude des événements futurs sous certaines conditions. Pour cette raison, elles sont largement utilisées en science, en ingénierie, en économie et dans de nombreux autres domaines.

Cependant, il existe de nombreux types de chaînes de Markov et chacune a ses propres applications.

Ce guide introduit ce que sont les chaînes de Markov, les différents types de chaînes de Markov, y compris les chaînes de Markov à temps discret, à temps continu, réversibles, et un exemple de code des modèles de Markov cachés (HMMs).

Nous verrons :

* [Analogie](#analogie)
* [Chaîne de Markov expliquée en anglais simple](#heading-chaine-de-markov-expliquee-en-anglais-simple)
* [Applications des chaînes de Markov](#heading-applications-des-chaines-de-markov)
* [Types de chaînes de Markov](#types-de-chaines-de-markov)
* [Exemple de code des chaînes de Markov cachées](#heading-exemple-de-code-des-chaines-de-markov-cachees)

<h2 href="analogie"> Analogie </h2>

Imaginez que vous voulez prédire la météo de demain, et qu'elle dépend **uniquement** de la météo d'aujourd'hui. La météo peut être soit ensoleillée, soit pluvieuse.

Voici les probabilités :

* Si aujourd'hui il fait ensoleillé, il y a 80 % de chances qu'il fasse à nouveau ensoleillé demain, et 20 % de chances qu'il pleuve.
* Si aujourd'hui il pleut, il y a 50 % de chances qu'il fasse ensoleillé demain, et 50 % de chances qu'il pleuve.

Dans ce scénario, nous pouvons prédire les états futurs de la météo en fonction des états actuels en utilisant des probabilités.

Cette idée de prédire le futur uniquement sur la base des probabilités du présent est appelée chaîne de Markov.

Ici, les états sont soit ensoleillés, soit pluvieux, et les probabilités décrivent les chances que la météo change en fonction de l'état actuel.

## Chaîne de Markov expliquée en anglais simple

Une chaîne de Markov décrit des processus aléatoires où les systèmes passent d'un état à un autre, et un nouvel état ne dépend que de l'état actuel, et non de la manière dont il y est parvenu.

Mathématiquement, les chaînes de Markov sont appelées modèles stochastiques car elles modélisent (simulent) des événements de la vie réelle qui sont aléatoires par nature (stochastiques).

Les chaînes de Markov sont très faciles à implémenter et efficaces pour modéliser des systèmes complexes.

Un autre avantage clé est leur propriété "sans mémoire". Cela les rend plus rapides à exécuter sur des ordinateurs, et puissantes pour étudier des processus aléatoires et faire des prédictions basées sur des conditions actuelles.

## Applications des chaînes de Markov

À un certain niveau, presque tous les événements de la vie réelle sont stochastiques. En d'autres termes, ils impliquent de l'aléatoire et de l'incertitude.

C'est exactement pourquoi elles sont si largement utilisées. Elles peuvent prédire le comportement des systèmes en fonction des conditions actuelles.

En finance, elles sont utilisées pour détecter les changements dans les notations de crédit pour prévoir les régimes de marché.

En génétique, elles aident à comprendre comment les protéines changent au fil du temps. Ce qui est important lors de l'étude des variations génétiques.

En robotique, elles assistent dans la prise de décision en prédisant le prochain mouvement du robot en fonction de l'observation actuelle.

Là, des exemples concrets montrent à quel point les chaînes de Markov peuvent être efficaces pour résoudre des problèmes réels dans différents domaines.

<h2 href="types"> Types de chaînes de Markov </h2>

Il existe de nombreux types de chaînes de Markov. Dans cette section, nous ne discuterons que des variantes les plus importantes des chaînes de Markov.

### Chaînes de Markov à temps discret (DTMCs)

Dans les DTMCs, le système change d'état à des étapes de temps spécifiques. Elles sont appelées discrètes car les transitions d'état se produisent à des intervalles de temps distincts et séparés.

Elles sont utilisées dans la théorie des files d'attente (étude du comportement des files d'attente), la génétique et l'économie car elles sont simples à analyser.

### Chaînes de Markov à temps continu (CTMCs)

Les CTMCs diffèrent des DTMCs en ce que les transitions d'état peuvent se produire à n'importe quel point dans le temps continu, et non à des intervalles fixes.

Cela en fait des modèles stochastiques où les changements d'état se produisent en continu. Cela est important dans les réactions chimiques et l'ingénierie de la fiabilité.

### Chaînes de Markov réversibles

Les chaînes de Markov réversibles sont spéciales. Le processus de changement d'état est le même que la direction soit vers l'avant ou vers l'arrière, comme rembobiner une vidéo et la rejouer.

Cette propriété facilite la connaissance de la stabilité d'un système et l'étude du comportement d'un système au fil du temps. Elles sont largement utilisées en physique statistique et en économie.

### Chaînes de Markov doublement stochastiques

Les chaînes de Markov doublement stochastiques sont définies par une matrice de probabilités de transition. Dans la matrice, la somme des probabilités dans chaque ligne et chaque colonne est égale à 1.

Cela signifie que chaque ligne et chaque colonne représentent une distribution de probabilités valide. En d'autres termes, chaque ligne et colonne représentent une liste de chances pour différents résultats.

Cette propriété est cruciale en informatique quantique et en mécanique statistique.

Grâce aux chaînes de Markov doublement stochastiques, les systèmes changent de manière à préserver les probabilités et la symétrie, rendant la modélisation et l'analyse des systèmes d'informatique quantique bien plus précises.

<h2 href="code"> Exemple de code des chaînes de Markov cachées </h2>

Avant de plonger dans les exemples de code, comprenons d'abord ce que sont les chaînes de Markov cachées.

### Chaînes de Markov cachées : Modélisation des états invisibles

L'idée principale derrière les chaînes de Markov cachées est de modéliser des systèmes qui ont des états cachés (états dont nous ne connaissons pas les valeurs) qui ne peuvent être découverts que par des événements observables.

En d'autres termes, les chaînes de Markov cachées nous permettent de prédire le comportement d'un système en :

* Considérant la probabilité de passer d'un état à un autre.
* Connaissant la probabilité d'observer un certain événement à partir de chaque état.

Nous pouvons comprendre cela en observant comment les états changent d'un point de vue indirect.

Nous ne connaissons peut-être pas les valeurs originales des états.

Mais en connaissant la manière dont ils changent, nous pouvons prédire quelles seront leurs valeurs dans le futur.

Ainsi, les chaînes de Markov cachées sont flexibles dans la modélisation des séquences, capturant à la fois les transitions entre les états cachés et les résultats observables.

Grâce à cela, les modèles de Markov cachés sont utilisés dans des domaines tels que l'ingénierie, la modélisation financière, la reconnaissance vocale, la bioinformatique, et bien d'autres.

### Exemple de code

Dans cet exemple de code, nous verrons un exemple simple avec des données synthétiques.

Voici le code complet :

```
import numpy as np
from hmmlearn import hmm

# Définir la graine aléatoire pour la reproductibilité
np.random.seed(42)

# Définir les paramètres du HMM
n_components = 2  # Nombre d'états
n_features = 1    # Nombre de caractéristiques d'observation

# Créer un HMM gaussien
model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag")

# Définir la matrice de transition (les lignes doivent faire 1)
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

# Définir les moyennes et les covariances pour chaque état
model.means_ = np.array([[0.0], [3.0]])
model.covars_ = np.array([[0.5], [0.5]])

# Générer des données d'observation synthétiques
X, Z = model.sample(100)  # 100 échantillons

# Créer une nouvelle instance de HMM
new_model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=100)

# Ajuster le modèle aux données
new_model.fit(X)

# Imprimer les paramètres appris
print("Matrice de transition :")
print(new_model.transmat_)
print("Moyennes :")
print(new_model.means_)
print("Covariances :")
print(new_model.covars_)

# Prédire les états cachés pour les données observées
hidden_states = new_model.predict(X)

print("États cachés :")
print(hidden_states)

```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/1.png)
_Code complet_

Regardons le code bloc par bloc !

### Importer les bibliothèques et définir la graine aléatoire

```
import numpy as np
from hmmlearn import hmm

np.random.seed(42)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/2.png)
_Importer les bibliothèques et définir la graine aléatoire_

Dans ce bloc de code, nous avons importé deux bibliothèques Python :

* [NumPy](https://numpy.org/) : Pour les opérations numériques.
* [hmmlearn](https://hmmlearn.readthedocs.io/en/latest/index.html) : Pour l'implémentation des modèles de Markov cachés.

Ensuite, nous avons défini une graine aléatoire avec la bibliothèque `numpy`.

#### Qu'est-ce qu'une graine aléatoire ?

Une graine aléatoire est une valeur utilisée pour démarrer un générateur de nombres pseudo-aléatoires.

Avec une graine aléatoire fixe, nous nous assurons que la séquence de nombres pseudo-aléatoires générée est toujours la même.

Cela nous permet de dupliquer des expériences et de vérifier les résultats.

La valeur spécifique de la graine n'a pas d'importance tant qu'elle reste cohérente.

### Définir les paramètres du HMM et créer un HMM gaussien

```
n_components = 2  # Nombre d'états
n_features = 1    # Nombre de caractéristiques d'observation

model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/3.png)
_Définir les paramètres du HMM et créer un HMM gaussien_

Dans ce bloc de code, nous avons créé un HMM avec deux états cachés et une seule variable observée.

`covariance_type "diag"` signifie que les matrices qui représentent la covariance—comment deux variables changent ensemble—sont diagonales. En d'autres termes, chaque ligne et colonne est supposée être indépendante des autres.

Cela implique que les distributions de probabilités de chaque ligne et colonne sont indépendantes les unes des autres.

Cependant, il y a encore quelque chose d'étrange lorsque nous avons défini la chaîne de Markov cachée.

#### Que signifie "Gaussien" ?

C'est un très grand sujet en statistiques, mais en quelques mots, les chaînes de Markov ne peuvent être créées que lorsque nous spécifions les probabilités de transition—chances de passer d'un état à un autre dans une chaîne de Markov—et une distribution de probabilités initiale.

Un HMM gaussien suppose que les événements sont initialement modélisés par une distribution gaussienne, également appelée distribution normale.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/normal-distribution.png)
_Distribution normale_

Une distribution normale est comme une courbe en forme de cloche qui décrit comment les choses sont souvent réparties dans la nature.

La distribution normale est cruciale car elle décrit de nombreux phénomènes naturels comme les tailles humaines, les erreurs de mesure, la probabilité de propagation d'une maladie et bien d'autres.

Et bien que de nombreux événements naturels ne soient pas décrits par une distribution normale avec le [théorème central limite](https://www.investopedia.com/terms/c/central_limit_theorem.asp), ils peuvent être approximés pour être décrits par une distribution normale.

Ainsi, de nombreux modèles de Markov cachés (HMMs) sont définis par une distribution normale, qui représente de nombreux phénomènes dans la nature et la société.

Dans la bibliothèque hmmlearn, il est également possible de créer des chaînes de Markov basées sur des distributions de Poisson.

En termes simples, les distributions de Poisson modélisent les probabilités qui décrivent l'occurrence d'événements sur un intervalle de temps ou d'espace fixe. Cela est largement utilisé dans les télécommunications.

Les HMMs basés sur une distribution de Poisson prédiraient des événements qui ont souvent tendance à être aléatoires et indépendants sur un intervalle spécifié.

### Définir la matrice de transition, les moyennes et les covariances pour chaque état

```
model.startprob_ = np.array([0.6, 0.4])
model.transmat_ = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

model.means_ = np.array([[0.0], [3.0]])
model.covars_ = np.array([[0.5], [0.5]])
```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/4.png)
_Définir la matrice de transition, les moyennes et les covariances pour chaque état_

**`model.startprob_ = np.array([0.6, 0.4])`** :

* Cette ligne définit les probabilités initiales des états pour un modèle de Markov caché (HMM). Elle indique qu'il y a 60 % de chances de commencer dans l'état 0 et 40 % de chances de commencer dans l'état 1.

**`model.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]])`** :

* Cette ligne définit la matrice des probabilités de transition d'état pour le HMM. La matrice spécifie les probabilités de passer d'un état à un autre :
* De l'état 0, il y a 70 % de chances de rester dans l'état 0 et 30 % de chances de passer à l'état 1.
* De l'état 1, il y a 40 % de chances de passer à l'état 0 et 60 % de chances de rester dans l'état 1.

**`model.means_ = np.array([[0.0], [3.0]])`** :

* Cette ligne définit les valeurs moyennes pour les distributions d'observation dans chaque état. Elle indique que les observations sont normalement distribuées avec une moyenne de 0,0 dans l'état 0 et une moyenne de 3,0 dans l'état 1.

**`model.covars_ = np.array([[0.5], [0.5]])`** :

* Cette ligne définit les valeurs de covariance pour les distributions d'observation dans chaque état. Elle spécifie que la variance (covariance dans ce cas unidimensionnel) des observations est de 0,5 pour l'état 0 et l'état 1.

### Créer des données, une nouvelle instance de HMM et ajuster le modèle avec les données

```
X, Z = model.sample(100)  # 100 échantillons

new_model = hmm.GaussianHMM(n_components=n_components, covariance_type="diag", n_iter=100)

new_model.fit(X)

print("Matrice de transition :")
print(new_model.transmat_)
print("Moyennes :")
print(new_model.means_)
print("Covariances :")
print(new_model.covars_)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/5.png)
_Créer des données, une nouvelle instance de HMM et ajuster le modèle avec les données_

Dans ce code, nous avons créé un modèle avec 100 échantillons, l'avons itéré 100 fois, et avons imprimé la nouvelle matrice de transition d'état, les moyennes et les covariances.

En d'autres termes, nous avons généré 100 échantillons à partir du modèle original, ajusté un nouveau modèle de Markov caché (HMM) à ces échantillons, puis imprimé les paramètres appris de ce nouveau modèle.

* **X** signifie les échantillons de données observées générés par le modèle original.
* **Z** signifie les séquences d'états cachés correspondant aux échantillons de données observées générés par le modèle original.

**La matrice de transition s'affiche :**

```
[[0.8100804  0.1899196 ]
 [0.49398918 0.50601082]]
```

Ce qui signifie que le modèle tend à rester dans l'état 0 et a presque les mêmes chances de changer ou de rester lorsqu'il est dans l'état 1.

**Les moyennes s'affichent :**

```
[[0.01577373]
 [3.06245496]]
```

Ce qui signifie que la valeur observée moyenne est d'environ 0,016 dans l'état 0 et 3,062 dans l'état 1.

**Les covariances s'affichent :**

```
[[[0.41987084]]
 [[0.53146802]]]
```

Ce qui signifie que les valeurs observées varient d'environ 0,420 dans l'état 0 et 0,531 dans l'état 1.

Ainsi, nous ne connaîtrons peut-être jamais exactement les valeurs des états, mais nous savons :

* Comment ils tendent à changer les uns avec les autres
* Leur valeur observée moyenne
* Comment ils varient

### Prédire les états cachés pour les données observées

```
hidden_states = new_model.predict(X)

print("États cachés :")
print(hidden_states)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/6.png)
_Prédire les états cachés pour les données observées_

Dans ce code, basé sur les échantillons de données observées X, nous avons prédit les nouveaux états du modèle de Markov.

Les états cachés s'affichent :

```
[0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 0 0 1 1 0 1 1 0 1 0 0 0 1
 1 1 1 1 0 0 0 1 1 0 0 1 1 1 1 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 1 0 0 0 0
 0 0 0 0 0 0 0 0 1 1 0 0 1 0 0 0 0 0 0 0 0 1 1 0 0 0]
```

Ce qui signifie que les états cachés passent de l'état 0 à l'état 1, montrant comment le système change d'états au fil du temps.

## Conclusion : L'avenir des chaînes de Markov

Les chaînes de Markov sont largement utilisées dans les domaines STEM grâce à leur capacité à prédire le futur en fonction du présent.

Les chaînes de Markov ont été de plus en plus intégrées avec l'intelligence artificielle, améliorant l'automatisation et l'analyse prédictive des systèmes.

De plus, le développement de chaînes de Markov plus efficaces sur le plan computationnel est une grande priorité, les rendant plus accessibles pour le traitement en temps réel et les simulations à grande échelle.

En résumé, les chaînes de Markov sont un outil très important en science grâce à leur capacité à prédire le futur.

Avec l'IA et une plus grande efficacité computationnelle, les chaînes de Markov peuvent être appliquées dans de nombreux autres domaines et résoudre de nombreux problèmes.