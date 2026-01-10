---
title: Distribution de Poisson – Une formule pour calculer la distribution de probabilité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-28T16:48:34.000Z'
originalURL: https://freecodecamp.org/news/poisson-distribution-a-formula-to-calculate-probability-distribution
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/thisisengineering-raeng-GzDrm7SYQ0g-unsplash.jpg
tags:
- name: Data Science
  slug: data-science
- name: Mathematics
  slug: mathematics
- name: Python
  slug: python
- name: statistics
  slug: statistics
seo_title: Distribution de Poisson – Une formule pour calculer la distribution de
  probabilité
seo_desc: "By Pier Paolo Ippolito\nProbability Distributions play an important role\
  \ in our daily lives. We commonly use them when trying to summarise and gain insights\
  \ from different forms of data. \nBecause of this, they're quite an important topic\
  \ in fields suc..."
---

Par Pier Paolo Ippolito

Les distributions de probabilité jouent un rôle important dans notre vie quotidienne. Nous les utilisons couramment lorsque nous essayons de résumer et de tirer des insights de différentes formes de données. 

Pour cette raison, elles constituent un sujet assez important dans des domaines tels que les mathématiques, l'informatique, les statistiques et la science des données.

Il existe deux principaux types de données : **Numériques** (par exemple, entiers et flottants) et **Catégorielles** (par exemple, chaînes de texte). 

Les données numériques peuvent également être sous l'une des deux formes suivantes :

* **Discrètes** : cette forme de données ne peut prendre qu'un nombre limité de valeurs (comme le nombre de vêtements que nous avons). Nous pouvons déduire des fonctions de masse de probabilité à partir de données discrètes.
* **Continues** : en revanche, les données continues sont utilisées pour décrire des concepts plus abstraits tels que le poids/la distance, qui peuvent prendre n'importe quelle valeur fractionnaire ou réelle. À partir de données continues, nous pouvons plutôt déduire des fonctions de densité de probabilité.

Les fonctions de masse de probabilité peuvent nous donner la probabilité qu'une variable soit égale à une certaine valeur. En revanche, les valeurs des fonctions de densité de probabilité ne représentent pas des probabilités en elles-mêmes, mais doivent d'abord être intégrées (dans la plage considérée).

## Qu'est-ce qu'une distribution de Poisson ?

Les distributions de Poisson sont couramment utilisées pour deux principaux objectifs :

* Prédire combien de fois un événement se produira dans une période de temps choisie. Cette technique peut être utilisée pour différentes applications d'analyse de risque telles que l'estimation des prix d'assurance habitation.
* Estimer une probabilité qu'un événement puisse se produire étant donné la fréquence à laquelle il s'est produit dans le passé (par exemple, la probabilité qu'il y ait une coupure de courant dans les deux prochains mois). 

Les distributions de Poisson nous permettent d'être confiants quant au temps moyen entre l'occurrence de différents événements. Elles ne peuvent cependant pas nous dire le moment précis où un événement pourrait se produire (puisque les processus ont généralement un comportement stochastique).

### Systèmes linéaires vs non linéaires

Les systèmes naturels peuvent en fait être divisés en deux catégories principales : **linéaires** et **non linéaires (stochastiques)**. 

Dans les systèmes linéaires, les causes précèdent toujours leurs effets, ce qui crée un fort effet de précédence temporelle. 

Mais cela ne s'applique pas aux systèmes non linéaires, car de petits changements dans les conditions initiales du système peuvent conduire à des résultats imprévisibles. 

Considérant à quel point notre monde réel est complexe et chaotique, la plupart des processus sont mieux décrits en utilisant des systèmes non linéaires, bien que des approximations linéaires soient parfois possibles.

Les distributions de Poisson peuvent être modélisées à l'aide de l'expression dans la figure ci-dessous, où **λ** est utilisé pour représenter le nombre attendu d'événements qui peuvent se produire dans la période considérée.

![Image for post](https://www.freecodecamp.org/news/content/images/2020/07/unnamed.png)

Les principales caractéristiques qui décrivent les processus de Poisson sont :

1. Deux événements ne peuvent pas se produire simultanément.
2. Le taux moyen entre l'occurrence des événements est globalement constant.
3. Les événements sont indépendants les uns des autres (si l'un se produit, cela n'a aucune influence sur la probabilité qu'un autre événement puisse se produire).
4. Les événements peuvent se produire un nombre quelconque de fois (dans la période considérée).

## Un exemple de distribution de Poisson

Dans la figure ci-dessous, vous pouvez voir comment la variation du nombre attendu d'événements (λ) qui peuvent se produire dans une période peut changer une distribution de Poisson. L'image ci-dessous a été simulée, en utilisant ce code Python :

```py
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# n = nombre d'événements, lambd = nombre attendu d'événements 
# qui peuvent se produire dans une période
for lambd in range(2, 12, 2):
    n = np.arange(0, 9)
    poisson = stats.poisson.pmf(n, lambd)
    plt.plot(n, poisson, '-o', label="λ = {:f}".format(lambd))
    plt.xlabel('Nombre d'événements', fontsize=12)
    plt.ylabel('Probabilité', fontsize=12)
    plt.title("Distribution de Poisson variant λ")
    plt.legend()
    plt.savefig('name.png')
```

En examinant de plus près cette simulation, nous pouvons découvrir les motifs suivants :

* Dans chacun des différents cas, le nombre attribué à λ correspond au pic de la distribution, qui diminue ensuite en s'éloignant du pic. 
* Plus le nombre d'événements attendus pendant la simulation est élevé, plus la surface attendue sous la courbe de distribution sera grande.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/poss.png)

Ce type de simulation pourrait, par exemple, être utilisé pour essayer de réduire le temps d'attente lors des courses dans un supermarché. 

Le propriétaire pourrait créer un enregistrement du nombre de clients visitant le magasin à différents moments et différents jours de la semaine afin d'ajuster ces données à une distribution de Poisson. 

De cette manière, il serait beaucoup plus facile de déterminer combien de caissiers devraient travailler à différents moments de la journée/semaine afin d'améliorer l'expérience client.

## Conclusion

Si vous êtes intéressé à en apprendre davantage sur les applications des distributions dans des contextes stochastiques, plus d'informations sont disponibles [ici](https://towardsdatascience.com/stochastic-processes-analysis-f0a116999e4).

_J'espère que vous avez apprécié cet article, merci pour votre lecture !_

### Contactez-moi

Si vous souhaitez rester informé de mes derniers articles et projets, [suivez-moi sur Medium](https://medium.com/@pierpaoloippolito28?source=post_page---------------------------) et abonnez-vous à ma [liste de diffusion](http://eepurl.com/gwO-Dr?source=post_page---------------------------). Voici quelques-uns de mes détails de contact :

* [Linkedin](https://uk.linkedin.com/in/pier-paolo-ippolito-202917146?source=post_page---------------------------)
* [Blog Personnel](https://pierpaolo28.github.io/blog/?source=post_page---------------------------)
* [Site Web Personnel](https://pierpaolo28.github.io/?source=post_page---------------------------)
* [Patreon](https://www.patreon.com/user?u=32155890)
* [Profil Medium](https://towardsdatascience.com/@pierpaoloippolito28?source=post_page---------------------------)
* [GitHub](https://github.com/pierpaolo28?source=post_page---------------------------)
* [Kaggle](https://www.kaggle.com/pierpaolo28?source=post_page---------------------------)