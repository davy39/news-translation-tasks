---
title: Qu'est-ce que le test d'hypothèses ? Types et exemple de code Python
subtitle: ''
author: Mene-Ejegi Ogbemi
co_authors: []
series: null
date: '2023-09-22T00:41:23.000Z'
originalURL: https://freecodecamp.org/news/what-is-hypothesis-testing
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Banner
seo_title: Qu'est-ce que le test d'hypothèses ? Types et exemple de code Python
---

Tech-writing---hypothesis.jpg
tags:
- name: analyse de données
  slug: analyse-de-donnees
- name: Science des données
  slug: science-des-donnees
- name: statistiques
  slug: statistiques
seo_title: null
seo_desc: La curiosité a toujours fait partie de la nature humaine. Depuis le début des temps, cela a été l'un des outils les plus importants pour la naissance des civilisations. Pourtant, notre curiosité grandit — elle teste et repousse nos limites. L'humanité a exploré les plaines de la terre, de l'eau et de l'air. Nous avons construit des habitats sous-marins où nous pourrions vivre pendant des semaines. Notre civilisation a exploré diverses planètes. Nous avons exploré la terre à un degré illimité. 

Ces choses ont été possibles parce que les humains ont posé des questions et ont cherché jusqu'à ce qu'ils trouvent des réponses. Cependant, pour que nous obtenions ces réponses, une méthode éprouvée doit être utilisée et suivie pour valider nos résultats. Historiquement, les philosophes supposaient que la terre était plate et que vous tomberiez lorsque vous atteindriez le bord. Alors que des philosophes comme Aristote soutenaient que la terre était sphérique en fonction de la formation des étoiles, ils ne pouvaient pas le prouver à l'époque. 

C'est parce qu'ils n'avaient pas de ressources adéquates pour explorer l'espace ou prouver mathématiquement la forme de la Terre. C'est un mathématicien grec nommé Ératosthène qui a calculé la circonférence de la terre avec une précision incroyable. Il a utilisé des méthodes scientifiques pour montrer que la Terre n'était pas plate. Depuis lors, d'autres méthodes ont été utilisées pour prouver la forme sphérique de la Terre.

Lorsque des questions ou des déclarations n'ont pas encore été testées et confirmées sur la base d'une méthode scientifique, elles sont appelées hypothèses. En gros, nous avons deux types d'hypothèses : nulle et alternative.

Une **hypothèse nulle** est la croyance ou l'argument par défaut de quelqu'un sur un sujet. Dans le cas de la forme de la terre, l'hypothèse nulle était que la terre était plate.

Une **hypothèse alternative** est une croyance ou un argument qu'une personne pourrait essayer d'établir. Aristote et Ératosthène soutenaient que la terre était sphérique.

D'autres exemples d'hypothèses alternatives aléatoires incluent :

* La météo peut avoir un impact sur l'humeur d'une personne.
* Plus de personnes portent des costumes le lundi par rapport aux autres jours de la semaine.
* Les enfants sont plus susceptibles d'être brillants si les deux parents sont dans le milieu universitaire, et ainsi de suite.

## Qu'est-ce que le test d'hypothèses ?

Le test d'hypothèses est l'acte de tester si une hypothèse ou une inférence est vraie. Lorsqu'une hypothèse alternative est introduite, nous la testons contre l'hypothèse nulle pour savoir laquelle est correcte. Utilisons une expérience de plante par un étudiant de 12 ans pour voir comment cela fonctionne.

L'hypothèse est qu'une plante poussera plus haute lorsqu'on lui donne un certain type d'engrais. L'étudiant prend deux échantillons de la même plante, fertilise l'un et laisse l'autre non fertilisé. Il mesure la hauteur des plantes tous les quelques jours et enregistre les résultats dans un tableau. 

Après une semaine ou deux, il compare la hauteur finale des deux plantes pour voir laquelle a poussé plus haute. Si la plante à laquelle on a donné de l'engrais a poussé plus haute, l'hypothèse est établie comme un fait. Sinon, l'hypothèse n'est pas soutenue. Cette simple expérience montre comment former une hypothèse, la tester expérimentalement et analyser les résultats.

Dans le test d'hypothèses, il existe deux types d'erreurs : Type I et Type II.

Lorsque nous rejetons l'hypothèse nulle dans un cas où elle est correcte, nous avons commis une erreur de Type I. Les erreurs de Type II se produisent lorsque nous ne parvenons pas à rejeter l'hypothèse nulle lorsqu'elle est incorrecte.

Dans notre expérience de plante ci-dessus, si l'étudiant découvre que les hauteurs des deux plantes sont les mêmes à la fin de la période de test, mais qu'il affirme que l'engrais aide à la croissance des plantes, il a commis une erreur de Type I. 

Cependant, si la plante fertilisée est plus haute et que l'étudiant enregistre que les deux plantes sont les mêmes ou que celle sans engrais a poussé plus haute, il a commis une erreur de Type II parce qu'il n'a pas réussi à rejeter l'hypothèse nulle.

## Quelles sont les étapes du test d'hypothèses ?

Les étapes suivantes expliquent comment nous pouvons tester une hypothèse :

### Étape #1 - Définir les hypothèses nulle et alternative

Avant de faire un test, nous devons d'abord définir ce que nous testons et quelle est l'hypothèse par défaut sur le sujet. Dans cet article, nous allons tester si le poids moyen des enfants de 10 ans est supérieur à 32 kg. 

Notre hypothèse nulle est que les enfants de 10 ans pèsent en moyenne 32 kg. Notre hypothèse alternative est que le poids moyen est supérieur à 32 kg. `Ho` désigne une hypothèse nulle, tandis que `H1` désigne une hypothèse alternative.

Ho = 32

H1 > 32

### Étape #2 - Choisir un niveau de signification

Le niveau de signification est un seuil pour déterminer si le test est valide. Il donne de la crédibilité à notre test d'hypothèse pour nous assurer que nous ne dépendons pas seulement de la chance, mais que nous avons suffisamment de preuves pour soutenir nos affirmations. Nous fixons généralement notre niveau de signification avant de mener nos tests. Le critère pour déterminer notre valeur de signification est connu sous le nom de p-valeur. 

Une p-valeur plus faible signifie qu'il y a des preuves plus solides contre l'hypothèse nulle, et donc, un plus grand degré de signification. Une p-valeur de 0,05 est largement acceptée comme étant significative dans la plupart des domaines de la science. Les p-valeurs ne désignent pas la probabilité du résultat, elles servent simplement de référence pour déterminer si notre résultat de test est dû au hasard. Pour notre test, notre p-valeur sera de 0,05.

### Étape #3 - Collecter des données et calculer une statistique de test

Vous pouvez obtenir vos données à partir de magasins de données en ligne ou mener directement vos recherches. Les données peuvent être extraites ou recherchées en ligne. La méthodologie peut dépendre de la recherche que vous essayez de mener.

Nous pouvons calculer notre test en utilisant l'un des tests d'hypothèse appropriés. Cela peut être un test T, un test Z, un Chi-carré, etc. Il existe plusieurs tests d'hypothèses, chacun convenant à différents objectifs et questions de recherche. Dans cet article, nous utiliserons le test T pour exécuter notre hypothèse, mais j'expliquerai également le test Z et le Chi-carré.

Le test T est utilisé pour la comparaison de deux ensembles de données lorsque nous ne connaissons pas l'écart type de la population. C'est un test paramétrique, ce qui signifie qu'il fait des hypothèses sur la distribution des données. Ces hypothèses incluent que les données sont normalement distribuées et que les variances des deux groupes sont égales. Dans un sens plus simple et pratique, imaginez que nous avons des notes de test dans une classe pour les garçons et les filles, mais nous ne savons pas à quel point ces notes sont différentes ou similaires. Nous pouvons utiliser un test t pour voir s'il y a une réelle différence.

Le test Z est utilisé pour la comparaison entre deux ensembles de données lorsque l'écart type de la population est connu. C'est également un test paramétrique, mais il fait moins d'hypothèses sur la distribution des données. Le test z suppose que les données sont normalement distribuées, mais il ne suppose pas que les variances des deux groupes sont égales. Dans notre exemple de test de classe, avec le test t, nous pouvons dire que si nous savons déjà à quel point les notes sont réparties dans les deux groupes, nous pouvons maintenant utiliser le test z pour voir s'il y a une différence dans les notes moyennes.

Le test du Chi-carré est utilisé pour comparer deux ou plusieurs variables catégorielles. Le test du Chi-carré est un test non paramétrique, ce qui signifie qu'il ne fait aucune hypothèse sur la distribution des données. Il peut être utilisé pour tester une variété d'hypothèses, y compris si deux ou plusieurs groupes ont des proportions égales.

### Étape #4 - Décider de l'hypothèse nulle en fonction de la statistique de test et du niveau de signification

Après avoir mené notre test et calculé la statistique de test, nous pouvons comparer sa valeur au niveau de signification prédéterminé. Si la statistique de test dépasse le niveau de signification, nous pouvons décider de rejeter l'hypothèse nulle, indiquant qu'il y a suffisamment de preuves pour soutenir notre hypothèse alternative. 

Au contraire, si la statistique de test ne dépasse pas le niveau de signification, nous ne parvenons pas à rejeter l'hypothèse nulle, signifiant que nous n'avons pas suffisamment de preuves statistiques pour conclure en faveur de l'hypothèse alternative.

### Étape #5 - Interpréter les résultats

En fonction de la décision prise à l'étape précédente, nous pouvons interpréter le résultat dans le contexte de notre étude et les implications pratiques. Pour notre étude de cas, nous pouvons interpréter si nous avons des preuves significatives pour soutenir notre affirmation que le poids moyen des enfants de 10 ans est supérieur à 32 kg ou non.

Pour notre test, nous générons des données factices aléatoires pour le poids des enfants. Nous utiliserons un test t pour évaluer si notre hypothèse est correcte ou non.

```python
import numpy as np
import scipy.stats as stats

# Créer un ensemble de données factices du poids des enfants de 10 ans
data = np.random.randint(20, 40, 100)

# Définir l'hypothèse nulle
H0 = "Le poids moyen des enfants de 10 ans est de 32 kg."

# Définir l'hypothèse alternative
H1 = "Le poids moyen des enfants de 10 ans est supérieur à 32 kg."

# Calculer la statistique de test
t_stat, p_value = stats.ttest_1samp(data, 32)

# Imprimer les résultats
print("Statistique de test :", t_stat)
print("p-valeur :", p_value)

# Conclusion
if p_value < 0.05:
    print("Rejeter l'hypothèse nulle.")
else:
    print("Échec du rejet de l'hypothèse nulle.")
```

Pour une meilleure compréhension, examinons ce que fait chaque bloc de code.

```python
import numpy as np
import scipy.stats as stats
```

Le premier bloc est l'instruction d'importation, où nous importons `numpy` et `scipy.stats`. Numpy est une bibliothèque Python utilisée pour le calcul scientifique. Elle dispose d'une grande bibliothèque de fonctions pour travailler avec des tableaux. Scipy est une bibliothèque pour les fonctions mathématiques. Elle dispose d'un module stat pour effectuer des fonctions statistiques, et c'est ce que nous allons utiliser pour notre test t.

```python
# Créer un ensemble de données factices du poids des enfants de 10 ans
data = np.random.randint(20, 40, 100)
```

Les poids des enfants ont été générés aléatoirement puisque nous ne travaillons pas avec un ensemble de données réel. Le module aléatoire dans la bibliothèque Numpy fournit une fonction pour générer des nombres aléatoires, qui est `randint`. 

La fonction `randint` prend trois arguments. Le premier (20) est la borne inférieure des nombres aléatoires à générer. Le second (40) est la borne supérieure, et le troisième (100) spécifie le nombre d'entiers aléatoires à générer. C'est-à-dire que nous générons des valeurs de poids aléatoires pour 100 enfants. Dans des circonstances réelles, ces échantillons de poids auraient été obtenus en prenant le poids du nombre requis d'enfants nécessaires pour le test.

```python
# Définir l'hypothèse nulle
H0 = "Le poids moyen des enfants de 10 ans est de 32 kg."

# Définir l'hypothèse alternative
H1 = "Le poids moyen des enfants de 10 ans est supérieur à 32 kg."
```

En utilisant le code ci-dessus, nous avons déclaré nos hypothèses nulle et alternative en indiquant le poids moyen d'un enfant de 10 ans dans les deux cas.

```python
# Calculer la statistique de test
t_stat, p_value = stats.ttest_1samp(data, 32)
```

`t_stat` et `p_value` sont les variables dans lesquelles nous allons stocker les résultats de nos fonctions. `stats.ttest_1samp` est la fonction qui calcule notre test. Elle prend deux variables, la première est la variable `data` qui stocke le tableau des poids des enfants, et la seconde (32) est la valeur contre laquelle nous allons tester la moyenne de notre tableau de poids ou de l'ensemble de données dans les cas où nous utilisons un ensemble de données du monde réel.

```python

# Imprimer les résultats
print("Statistique de test :", t_stat)
print("p-valeur :", p_value)
```

Le code ci-dessus imprime les deux valeurs pour `t_stats` et `p_value`.

```python
# Conclusion
if p_value < 0.05:
    print("Rejeter l'hypothèse nulle.")
else:
    print("Échec du rejet de l'hypothèse nulle.")
```

Enfin, nous avons évalué notre `p_value` par rapport à notre valeur de signification, qui est de 0,05. Si notre `p_value` est inférieure à 0,05, nous rejetons l'hypothèse nulle. Sinon, nous ne parvenons pas à rejeter l'hypothèse nulle. Voici la sortie de ce programme. Notre hypothèse nulle a été rejetée.

```python
Statistique de test : -5.114430435590074
p-valeur : 1.541000376540265e-06
Rejeter l'hypothèse nulle.
```

## Conclusion

Dans cet article, nous avons discuté de l'importance du test d'hypothèses. Nous avons mis en évidence comment la science a fait progresser les connaissances et la civilisation humaines grâce à la formulation et au test d'hypothèses.

Nous avons discuté des erreurs de Type I et de Type II dans le test d'hypothèses et comment elles soulignent l'importance d'une considération et d'une analyse minutieuses dans l'enquête scientifique. Cela renforce l'idée que les conclusions doivent être tirées sur la base d'une analyse statistique approfondie plutôt que sur des hypothèses ou des biais.

Nous avons également généré un ensemble de données d'échantillon en utilisant les bibliothèques Python pertinentes et utilisé les fonctions nécessaires pour calculer et tester notre hypothèse alternative.

Merci d'avoir lu ! Veuillez me suivre sur [LinkedIn](https://www.linkedin.com/in/ogbemi-ejegi/) où je publie également plus de contenu lié aux données.