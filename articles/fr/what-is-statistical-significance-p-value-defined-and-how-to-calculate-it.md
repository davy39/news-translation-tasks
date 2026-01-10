---
title: Qu'est-ce que la significativité statistique ? Valeur P définie et comment
  la calculer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-03T12:47:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-statistical-significance-p-value-defined-and-how-to-calculate-it
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cd4740569d1a4ca346d.jpg
tags:
- name: statistics
  slug: statistics
seo_title: Qu'est-ce que la significativité statistique ? Valeur P définie et comment
  la calculer
seo_desc: 'By Peter Gleeson

  P values are one of the most widely used concepts in statistical analysis. They
  are used by researchers, analysts and statisticians to draw insights from data and
  make informed decisions.

  Along with statistical significance, they are...'
---

Par Peter Gleeson

Les valeurs P sont l'un des concepts les plus largement utilisés en analyse statistique. Elles sont utilisées par les chercheurs, les analystes et les statisticiens pour tirer des insights des données et prendre des décisions éclairées.

Avec la significativité statistique, elles sont également l'un des concepts les plus largement mal utilisés et mal compris en analyse statistique.

Cet article expliquera :

* comment une valeur P est utilisée pour inférer la significativité statistique
* comment les valeurs P sont calculées
* et comment éviter certaines idées reçues courantes

### Rappel : Test d'hypothèses

Le test d'hypothèses est une approche standard pour tirer des insights des données. Il est utilisé dans pratiquement toutes les disciplines quantitatives et a une histoire riche remontant à plus de cent ans.

L'approche habituelle du test d'hypothèses est de définir une question en termes des variables qui vous intéressent. Ensuite, vous pouvez former deux hypothèses opposées pour y répondre.

* L'**hypothèse nulle** affirme qu'il n'y a pas de relation statistiquement significative entre les variables
* L'**hypothèse alternative** affirme qu'il existe une relation statistiquement significative entre les variables

Par exemple, supposons que vous testez si la caféine affecte la productivité en programmation. Il y a deux variables qui vous intéressent - la dose de caféine et la productivité d'un groupe de développeurs de logiciels.

L'**hypothèse nulle** serait :

* "La consommation de caféine n'a **aucun effet significatif** sur la productivité en programmation".

L'**hypothèse alternative** serait :

* "La consommation de caféine a **un effet significatif** sur la productivité".

Le mot 'significatif' a ici une signification très spécifique. Il fait référence à une relation entre les variables existant en raison de quelque chose **de plus que le simple hasard**.

Au lieu de cela, la relation existe (au moins en partie) en raison de différences ou d'effets 'réels' entre les variables.

L'étape suivante consiste à collecter des données pour tester les hypothèses. Cela peut être collecté à partir d'une expérience ou d'une enquête, ou à partir d'un ensemble de données auquel vous avez accès.

La dernière étape consiste à calculer une statistique de test à partir des données. Il s'agit d'un nombre unique qui représente une caractéristique de vos données. Les exemples incluent le test t, le test du Chi-carré et le test de Kruskal-Wallis - parmi beaucoup d'autres.

Exactement lequel calculer dépendra de la question que vous posez, de la structure de vos données et de la distribution de vos données.

[Voici un aide-mémoire pratique](https://stats.idre.ucla.edu/other/mult-pkg/whatstat/) pour votre référence.

Dans l'exemple de la caféine, un test approprié pourrait être un [test t à deux échantillons](https://www.itl.nist.gov/div898/handbook/eda/section3/eda353.htm).

Vous obtiendrez une statistique de test unique à partir de vos données. Il ne reste plus qu'à interpréter ce résultat pour déterminer s'il soutient ou rejette l'hypothèse nulle.

C'est là que les valeurs P entrent en jeu.

### À quel point cette statistique est-elle improbable ?

Rappelons que vous avez calculé une statistique de test, qui représente une caractéristique de vos données. Vous voulez comprendre si elle soutient ou rejette l'hypothèse nulle.

L'approche adoptée est de supposer que l'hypothèse nulle est vraie. C'est-à-dire, supposer qu'il n'y a pas de relations significatives entre les variables qui vous intéressent.

Ensuite, regardez les données que vous avez collectées. À quel point votre statistique de test serait-elle probable si l'hypothèse nulle était vraiment vraie ?

Reprenons l'exemple de la consommation de caféine.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/Screenshot-2020-02-02-at-17.15.04.png)

* Supposons que les niveaux de productivité étaient répartis de manière assez égale entre les développeurs, indépendamment du fait qu'ils aient bu de la caféine ou non (graphique A). Ce résultat serait **susceptible de se produire par hasard** si l'hypothèse nulle était vraie.
* Cependant, supposons que presque toute la productivité la plus élevée a été observée chez les développeurs qui ont bu de la caféine (graphique B). Il s'agit d'un résultat plus 'extrême', et il serait **peu probable de se produire simplement par hasard** si l'hypothèse nulle était vraie.

Mais à quel point un résultat doit-il être 'extrême' avant d'être considéré comme trop improbable pour soutenir l'hypothèse nulle ?

C'est ce qu'une valeur P vous permet d'estimer. Elle fournit une réponse numérique à la question : "si l'hypothèse nulle est vraie, quelle est la probabilité d'un résultat aussi extrême ou plus extrême ?"

Les valeurs P sont des probabilités, donc elles sont toujours comprises entre 0 et 1.

* Une **valeur P élevée** indique que les résultats observés sont **susceptibles de se produire par hasard** sous l'hypothèse nulle.
* Une **valeur P faible** indique que les résultats sont **moins susceptibles de se produire par hasard** sous l'hypothèse nulle.

Habituellement, un seuil est choisi pour déterminer la significativité statistique. Ce seuil est souvent noté α.

Si la valeur P est **inférieure au seuil**, vos résultats sont '**statistiquement significatifs**'. Cela signifie que vous pouvez rejeter l'hypothèse nulle (et accepter l'hypothèse alternative).

Il n'existe pas de seuil universel adapté à toutes les applications. Habituellement, un seuil arbitraire sera utilisé qui est approprié pour le contexte.

Par exemple, dans des domaines tels que l'écologie et l'évolution, il est difficile de contrôler les conditions expérimentales car de nombreux facteurs peuvent affecter le résultat. Il peut également être difficile de collecter des tailles d'échantillon très grandes. Dans ces domaines, un seuil de 0,05 sera souvent utilisé.

Dans d'autres contextes tels que la physique et l'ingénierie, un seuil de 0,01 ou même inférieur sera plus approprié.

### Exemple du Chi-carré

Dans cet exemple, il y a deux variables (fictives) : la région et l'appartenance à un parti politique. Il utilise le [test du Chi-carré](https://www.mathsisfun.com/data/chi-square-test.html) pour voir s'il existe une relation entre la région et l'appartenance à un parti politique.

Vous pouvez changer le nombre de membres pour chaque parti.

* Hypothèse nulle : "il n'y a **pas de relation significative** entre la région et l'appartenance à un parti politique"
* Hypothèse alternative : "il **existe une relation significative** entre la région et l'appartenance à un parti politique"

%[https://codepen.io/pg2020/pen/zYxgZvK]

Appuyez sur le bouton "réexécuter" pour essayer différents scénarios.

### Idées reçues courantes et comment les éviter

Il existe plusieurs erreurs que même les praticiens expérimentés commettent souvent concernant l'utilisation des valeurs P et des tests d'hypothèses. Cette section vise à clarifier ces points.

❌ **L'hypothèse nulle est sans intérêt** - si les données sont bonnes et que l'analyse est bien faite, alors c'est une conclusion valable en soi.

✅ **Une question qui vaut la peine d'être posée doit avoir une réponse intéressante - quel que soit le résultat.**

❌ **La valeur P est la probabilité que l'hypothèse nulle soit vraie** - une valeur P représente "la probabilité des résultats, étant donné que l'hypothèse nulle est vraie". Ce n'est pas la même chose que "la probabilité que l'hypothèse nulle soit vraie, étant donné les résultats".

_P(Données | Hypothèse) ≠ P(Hypothèse | Données)_

✅ **Cela signifie qu'une valeur P faible vous indique : "si l'hypothèse nulle est vraie, ces résultats sont improbables". Elle ne vous indique **pas** : "si ces résultats sont vrais, l'hypothèse nulle est improbable".**

❌ **Vous pouvez utiliser le même seuil de significativité pour plusieurs comparaisons** - rappelez-vous la définition de la valeur P. Il s'agit de la probabilité d'observer une certaine statistique de test par simple hasard.

Si vous utilisez un seuil de α = 0,05 (ou 1 sur 20) et que vous effectuez, par exemple, 20 tests statistiques... vous pourriez vous attendre, par simple hasard, à trouver une valeur P faible.

✅ **Vous devriez utiliser un seuil plus bas si vous effectuez plusieurs comparaisons. Il existe des [méthodes de correction](https://en.wikipedia.org/wiki/Family-wise_error_rate#Controlling_procedures) qui vous permettront de calculer combien le seuil doit être plus bas.**

❌ **Le seuil de significativité signifie quoi que ce soit** - il est entièrement arbitraire. 0,05 est juste une convention. La différence entre p = 0,049 et p = 0,051 est presque la même qu'entre p = 0,039 et p = 0,041.

C'est l'une des plus grandes faiblesses du test d'hypothèses de cette manière. Il vous force à tracer une ligne dans le sable, même si aucune ligne ne peut facilement être tracée.

✅ **Par conséquent, considérez toujours les seuils de significativité pour ce qu'ils sont - totalement arbitraires.**

❌ **La significativité statistique signifie que le hasard ne joue aucun rôle** - loin de là. Souvent, il y a de nombreuses causes pour un résultat donné. Certaines seront aléatoires, d'autres moins.

✅ **Trouver une cause non aléatoire ne signifie pas qu'elle explique toutes les différences entre vos variables. Il est important de ne pas confondre la significativité statistique avec "la taille de l'effet".**

❌ **Les valeurs P sont le seul moyen de déterminer la significativité statistique** - il existe d'autres approches qui sont parfois meilleures.

✅ **En plus des tests d'hypothèses classiques, envisagez d'autres approches - telles que l'utilisation de [facteurs de Bayes](https://en.wikipedia.org/wiki/Bayes_factor), ou de [risque de faux positifs](https://arxiv.org/pdf/1802.04888.pdf).**