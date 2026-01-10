---
title: Apprentissage supervisé vs non supervisé – Quelle est la différence ?
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-06-29T16:10:36.000Z'
originalURL: https://freecodecamp.org/news/supervised-vs-unsupervised-learning
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-27-14-46-14.png
tags:
- name: Machine Learning
  slug: machine-learning
seo_title: Apprentissage supervisé vs non supervisé – Quelle est la différence ?
seo_desc: 'In the field of machine learning, there are two approaches: supervised
  learning and unsupervised learning. And it all depends on whether your data is labeled
  or not. Labels shape the way models are trained and affect how we gather insights
  from them....'
---

Dans le domaine de l'apprentissage automatique, il existe deux approches : l'apprentissage supervisé et l'apprentissage non supervisé. Et tout dépend du fait que vos données soient étiquetées ou non. Les étiquettes façonnent la manière dont les modèles sont entraînés et affectent la façon dont nous en tirons des informations.

Dans cet article, nous explorerons les concepts d'apprentissage supervisé et non supervisé, et mettrons en lumière leurs différences clés.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-27-13-51-30.png)
_Types d'apprentissage en apprentissage automatique_

## Apprentissage supervisé : guidé par des données étiquetées

L'apprentissage supervisé est comme avoir un enseignant utile à vos côtés. Dans cette approche, nous avons des données étiquetées, ce qui signifie que chaque morceau de données est accompagné d'une étiquette ou d'un tag spécial. 

Imaginez cela comme avoir les réponses aux questions avant le grand test. Vous pouvez apprendre à partir de ces exemples étiquetés et faire des prédictions ou des classifications sur de nouvelles données invisibles.

L'apprentissage supervisé tourne autour de l'utilisation de données étiquetées, où chaque point de données est associé à une étiquette ou à un résultat connu. En exploitant ces étiquettes, le modèle apprend à faire des prédictions ou des classifications précises sur des données invisibles.

Un exemple classique d'apprentissage supervisé est un modèle de détection de spam par e-mail. Ici, le modèle est entraîné sur un ensemble de données où chaque e-mail est étiqueté comme "spam" ou "non spam". En apprenant à partir de ces exemples étiquetés, le modèle peut généraliser ses connaissances et classer avec précision les e-mails entrants comme spam ou légitimes.

Un autre exemple d'apprentissage supervisé est un modèle de reconnaissance d'écriture manuscrite. En fournissant au modèle un ensemble de données de chiffres manuscrits ainsi que leurs étiquettes correspondantes, le modèle peut apprendre les motifs et les variations associés à chaque chiffre. Par conséquent, il devient compétent dans la reconnaissance de chiffres manuscrits dans de nouveaux échantillons invisibles.

## Étiquettes catégorielles et continues

Les étiquettes catégorielles sont utilisées lorsque la variable cible tombe dans un nombre fini de catégories ou de classes distinctes. Ces étiquettes sont également connues sous le nom d'étiquettes nominales ou discrètes.

Décomposons quelques termes pour faciliter la compréhension. Une étiquette catégorielle a un ensemble discret de valeurs possibles, comme "est une vache" ou "n'est pas une vache". C'est comme dire que quelque chose ne peut être qu'une chose ou une autre. 

Discret est un terme emprunté à la statistique, faisant référence à des résultats qui ne peuvent prendre qu'un nombre fini de valeurs, comme les jours de la semaine. C'est comme avoir un nombre limité d'options parmi lesquelles choisir.

Les étiquettes continues, également connues sous le nom d'étiquettes numériques, sont utilisées lorsque la variable cible représente une quantité continue ou à valeur réelle. Ces étiquettes peuvent prendre n'importe quelle valeur numérique dans une certaine plage.

Cela signifie qu'une étiquette continue n'a pas un ensemble discret de valeurs possibles. Il peut y avoir un nombre illimité de possibilités. Imaginez cela comme une échelle mobile au lieu de catégories strictes.

Il est important de noter que le type d'étiquettes détermine le type de problème d'apprentissage automatique auquel vous êtes confronté. 

Les étiquettes catégorielles sont associées à des problèmes de classification, où l'objectif est d'assigner une catégorie ou une classe à une entrée donnée. 

Les étiquettes continues sont associées à des problèmes de régression, où l'objectif est de prédire une valeur continue. 

Mais il existe également des problèmes hybrides qui impliquent à la fois des étiquettes catégorielles et continues, tels que la classification multi-étiquettes ou la régression multi-sorties.

## Algorithmes d'apprentissage supervisé 

Voici quelques techniques d'apprentissage supervisé que vous devriez connaître :

### Régression linéaire

La régression linéaire est une technique fondamentale en apprentissage automatique utilisée pour modéliser la relation entre une variable dépendante et une ou plusieurs variables indépendantes. Elle vise à trouver la meilleure ligne droite qui représente la relation linéaire entre les variables.

Imaginez que vous avez un ensemble de points sur un graphique. Chaque point a deux valeurs : une sur l'axe des x et une sur l'axe des y. Par exemple, supposons que nous avons des variables représentant le nombre d'heures étudiées (x) et les notes de test correspondantes (y) pour différents étudiants.

La régression linéaire est un moyen de tracer une ligne droite qui représente au mieux la tendance générale ou la relation entre ces deux variables. Nous voulons trouver une ligne qui se rapproche le plus possible de tous les points.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-29-11-15-08.png)
_Image d'un graphique montrant la régression linéaire_

La régression linéaire est utilisée dans de nombreuses situations réelles. Par exemple, la prédiction des prix des maisons en fonction de facteurs tels que la superficie, le nombre de pièces et l'emplacement.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-27-14-36-37.png)
_Image d'une maison et d'une boussole_

### Régression logistique

La régression logistique est employée lorsque la variable cible est binaire ou catégorielle. Elle prédit la probabilité qu'une instance appartienne à une classe particulière. Elle est couramment utilisée pour des tâches telles que l'analyse de sentiment ou la détection de spam.

Pour comprendre la régression logistique, imaginons que nous avons un ensemble de données avec certaines caractéristiques et des étiquettes correspondantes. Par exemple, nous pourrions avoir des informations sur des étudiants, telles que leur temps d'étude et s'ils ont réussi ou échoué un examen.

Dans la régression logistique, nous nous intéressons à la prédiction d'un résultat binaire, comme "réussite" ou "échec". L'objectif est de trouver une relation entre les caractéristiques d'entrée (par exemple, le temps d'étude) et la probabilité du résultat (par exemple, la probabilité de réussir l'examen).

Au lieu d'une ligne droite comme dans la régression linéaire, la régression logistique utilise une courbe spéciale appelée sigmoïde ou fonction logistique. Cette courbe varie entre 0 et 1 et a une forme caractéristique en S. Elle mappe toute valeur d'entrée à une valeur de probabilité entre 0 et 1.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-29-11-16-04.png)
_Image d'un graphique montrant la régression logistique_

### Arbres de décision

Les arbres de décision sont des structures graphiques qui aident à prendre des décisions ou à faire des prédictions sur la base d'un ensemble de conditions. Ils divisent les données en branches, où chaque branche représente une décision ou un résultat. Les arbres de décision sont largement utilisés pour les tâches de classification et peuvent gérer à la fois des données catégorielles et continues.

L'arbre de décision commence par un seul nœud, appelé nœud racine, représentant l'ensemble de données. Chaque nœud interne de l'arbre représente une décision basée sur une caractéristique spécifique, et chaque branche représente les résultats possibles de cette décision. Les feuilles de l'arbre représentent les prédictions ou les résultats finaux.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-29-12-00-34.png)
_Illustration d'un arbre de décision_

Imaginez que vous êtes un détective essayant de résoudre un mystère et que vous avez une liste d'indices ou de caractéristiques à considérer. Chaque indice pourrait être une pièce de preuve qui vous aide à déterminer si un suspect est coupable ou non.

Un arbre de décision est comme un ensemble de questions qui vous guident tout au long du processus d'investigation, vous aidant à prendre des décisions en fonction des indices.

Par exemple, supposons que vous avez les indices suivants :

* Indice 1 : Y a-t-il une arme sur la scène de crime ?
* Indice 2 : Le suspect avait-il un mobile ?
* Indice 3 : Y a-t-il des témoignages oculaires ?

En commençant par la question racine, vous demanderiez s'il y a une arme sur la scène de crime. Si la réponse est "oui", vous suivez une branche de l'arbre de décision. Si la réponse est "non", vous suivez une branche différente.

Considérons la branche "oui" :

* S'il y a une arme sur la scène de crime, vous passez à la question suivante : Le suspect avait-il un mobile ? Selon la réponse, vous suivez la branche correspondante.
* Si le suspect avait un mobile, vous continuez à la question suivante : Y a-t-il des témoignages oculaires ? Encore une fois, vous suivez la branche appropriée en fonction de la réponse.

Chaque question ou indice vous aide à réduire les possibilités et à prendre une décision à chaque étape. Finalement, vous atteignez un nœud feuille, qui représente votre décision ou prédiction finale.

Par exemple, si vous trouvez une arme sur la scène de crime, que le suspect avait un mobile et qu'il y a des témoignages oculaires, l'arbre de décision pourrait vous amener à conclure que le suspect est coupable. D'un autre côté, si l'un des indices pointe dans la direction opposée, l'arbre de décision pourrait vous amener à conclure que le suspect n'est pas coupable.

Dans cette analogie du détective, l'arbre de décision agit comme un organigramme logique, vous aidant à prendre des décisions en fonction des preuves ou des caractéristiques disponibles. 

De même, en apprentissage automatique, les arbres de décision utilisent des caractéristiques d'entrée pour faire des prédictions ou des classifications basées sur un ensemble hiérarchique de conditions si-alors.

```yaml
             Début
               |
         Y a-t-il une arme sur la scène de crime ?
               |
        /                  \
       /                    \
  Oui /                      \ Non
     /                        \
    |                 Le suspect avait-il un mobile ?
    |                      |
   Oui                    Non
    |                      |
    |                 Y a-t-il des témoignages oculaires ?
    |                      |
    |                       \
   Oui                       Non
    |                        |
   Coupable                 Non Coupable
```

## Apprentissage non supervisé : Extraire des motifs cachés à partir de données non étiquetées

Maintenant, préparez-vous à libérer votre Sherlock Holmes intérieur car l'apprentissage non supervisé consiste à découvrir des mystères cachés dans vos données. 

Dans cette approche, nous n'avons aucune étiquette ou réponse au préalable. C'est comme se voir présenter un puzzle et essayer de comprendre les motifs tout seul.

L'apprentissage non supervisé traite des données non étiquetées, où aucune étiquette ou résultat préexistant n'est fourni. Dans cette approche, l'objectif est de découvrir des motifs ou des structures cachés inhérents aux données elles-mêmes. 

Par exemple, le clustering est une technique populaire d'apprentissage non supervisé utilisée pour identifier des regroupements naturels au sein des données.

Imaginez que vous avez un ensemble de données contenant divers attributs de clients tels que l'âge, le revenu et le comportement d'achat. En appliquant des algorithmes de clustering à ces données, vous pouvez identifier des segments de clients distincts en fonction de leurs similitudes. Ces informations peuvent ensuite être utilisées pour adapter les stratégies marketing ou personnaliser les recommandations pour chaque segment.

Une autre application convaincante de l'apprentissage non supervisé est la détection d'anomalies. En cybersécurité, les algorithmes non supervisés peuvent analyser les motifs de trafic réseau et identifier des activités inhabituelles ou suspectes qui s'écartent de la norme. En détectant les anomalies, les violations de sécurité potentielles ou les cyberattaques peuvent être traitées de manière préventive.

## Algorithmes d'apprentissage non supervisé

Les algorithmes d'apprentissage non supervisé peuvent être classés en deux types de problèmes :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-29-12-22-02.png)
_Types d'algorithmes d'apprentissage non supervisé : clustering et association_

## Clustering 

Une technique populaire d'apprentissage non supervisé est le clustering. Le clustering est comme un superpouvoir qui nous aide à déterminer s'il existe des regroupements naturels dans les données. C'est comme trouver des amis qui ont des intérêts similaires sans même connaître leurs noms. 

Avec le clustering, vous pouvez regrouper des points de données similaires ensemble et découvrir des motifs ou des structures significatifs dans les données.

Il existe divers algorithmes de clustering disponibles, tels que k-means, le clustering hiérarchique et DBSCAN. Ces algorithmes diffèrent dans leurs approches, mais l'idée générale est de mesurer la distance ou la similarité entre les points de données et de les assigner à des clusters. Le nombre de clusters peut être prédéfini (k-means) ou déterminé automatiquement (clustering hiérarchique).

Le clustering a de nombreuses applications, notamment la segmentation de clients, la reconnaissance d'images, le clustering de documents, la détection d'anomalies et les systèmes de recommandation.

## Association

L'association est une autre technique en apprentissage non supervisé qui se concentre sur la découverte de relations ou d'associations intéressantes entre différents éléments ou variables dans un ensemble de données. Elle vise à identifier des motifs qui apparaissent fréquemment ensemble dans les données.

L'algorithme le plus connu pour l'extraction de règles d'association est Apriori. Étant donné un ensemble de données de transactions, Apriori trouve des ensembles d'éléments qui se produisent fréquemment ensemble et en dérive des règles d'association. 

Une règle d'association se compose d'un antécédent (ou côté gauche) et d'un conséquent (ou côté droit), indiquant la présence de certains éléments impliquant la présence d'autres éléments.

Par exemple, dans une analyse de panier de marché, des règles d'association peuvent être dérivées pour identifier les articles qui sont souvent achetés ensemble. Ces règles peuvent aider à faire des recommandations, optimiser les dispositions des magasins ou comprendre le comportement des clients.

L'analyse d'association peut également être étendue à des scénarios plus complexes, tels que les motifs séquentiels, où l'ordre des occurrences d'éléments est important.

Le clustering et l'association sont des techniques d'apprentissage non supervisé qui aident à explorer et analyser des données sans dépendre d'étiquettes ou de classes prédéfinies. Ils jouent des rôles cruciaux dans la découverte de motifs, l'exploration de données et l'obtention d'informations à partir d'ensembles de données non étiquetés.

## Conclusion

L'apprentissage supervisé et non supervisé représentent deux approches distinctes dans le domaine de l'apprentissage automatique, la présence ou l'absence d'étiquetage étant un facteur déterminant. 

L'apprentissage supervisé exploite la puissance des données étiquetées pour entraîner des modèles capables de faire des prédictions ou des classifications précises. 

En revanche, l'apprentissage non supervisé se concentre sur la découverte de motifs et de structures cachés au sein de données non étiquetées, en utilisant des techniques comme le clustering ou la détection d'anomalies.

Que vous travailliez avec des données étiquetées dans l'apprentissage supervisé, comme la détection de spam par e-mail ou la reconnaissance d'écriture manuscrite, ou que vous exploriez le potentiel de l'apprentissage non supervisé dans la segmentation de clients ou la détection d'anomalies, la compréhension des principes sous-jacents de ces approches vous permet de tirer des informations précieuses et de prendre des décisions éclairées dans un large éventail d'applications.