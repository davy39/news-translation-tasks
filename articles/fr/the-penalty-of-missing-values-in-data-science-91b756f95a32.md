---
title: La pénalité des valeurs manquantes en Data Science
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-04T15:46:44.000Z'
originalURL: https://freecodecamp.org/news/the-penalty-of-missing-values-in-data-science-91b756f95a32
coverImage: https://cdn-media-1.freecodecamp.org/images/1*an9j2v3NKxvhghxoRxF9nw.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: 'tech '
  slug: tech
seo_title: La pénalité des valeurs manquantes en Data Science
seo_desc: 'By Tanveer Sayyed

  And using a “soft” method to impute the same.

  This post focuses more on a conceptual level rather than coding skills and is divided
  into two parts. Part-I describes the problems with missing values and when and why
  should we use mea...'
---

Par Tanveer Sayyed

#### Et l'utilisation d'une méthode "souple" pour imputer les mêmes.

Cet article se concentre davantage sur un niveau conceptuel plutôt que sur des compétences en codage et est divisé en deux parties. La partie I décrit les problèmes liés aux valeurs manquantes et quand et pourquoi nous devrions utiliser la moyenne/médiane/mode. La partie II **répudie** la partie I et argue pourquoi nous ne devrions utiliser aucune d'entre elles et utiliser plutôt la méthode _souple_ — représentation aléatoire mais proportionnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*an9j2v3NKxvhghxoRxF9nw.jpeg)
_Photo par [Pexels](https://www.pexels.com/@rakicevic-nenad-233369?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener" target="_blank" title="">Rakicevic Nenad</a> de <a href="https://www.pexels.com/photo/silhouette-photo-of-man-throw-paper-plane-1262304/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener" target="_blank" title=")_

### Partie I : Pourquoi supprimons-nous les valeurs manquantes ? Quand utiliser la moyenne, la médiane, le mode ? Et pourquoi ?

Le problème avec les données manquantes est qu'il n'existe pas de méthode fixe pour les traiter, et le problème est universel. Les valeurs manquantes affectent nos performances et notre capacité prédictive. Elles ont le potentiel de changer tous nos paramètres statistiques. La manière dont elles interagissent avec les valeurs aberrantes affecte à nouveau nos statistiques. Les conclusions peuvent ainsi être trompeuses.

Les différentes valeurs manquantes peuvent être :

1. NaN  
2. None  
3.  
4. "Null"  
5. "missing"  
6. "not available"  
7. "NA"

Alors que les quatre dernières sont des valeurs de chaîne, pandas identifie par défaut NaN (aucun nombre assigné) et None. Cependant, les deux ne sont pas identiques ; l'extrait de code ci-dessous montre pourquoi.

Le problème est que si nous ne supprimons pas les NaN, nous sommes alors en double péril. Premièrement, nous souffrons déjà de la perte de données réelles et deuxièmement, si elles ne sont pas traitées avec soin, les NaN commencent à "dévorer" nos données réelles et pourraient se propager dans tout l'ensemble de données au fur et à mesure que nous avançons. Instancions deux séries et voyons.

Maintenant, voyons ce qui se passe lorsque nous effectuons certaines opérations sur ces listes.

Nous pouvons voir comment les données réelles (entiers 1, 2) ont été perdues lors de l'exécution des opérations (Sortie : 21, 22). Une autre chose à noter est les résultats conflictuels dans la méthode Python intégrée et la méthode de série en raison de la présence de NaN (Sortie : 23, 24).

Maintenant, créons un data-frame qui contient toutes les valeurs manquantes énoncées ci-dessus ainsi qu'une valeur de garbage ('#$%'). Nous supprimerons les valeurs manquantes en manipulant cet ensemble de données jouet minuscule.

Le data-frame a une ligne complète (i1) et une colonne complète (c2) remplies uniquement de NaN. D'autres identifiants de valeurs manquantes ont également été délibérément dispersés.

Ci-dessus, nous pouvons voir que le dernier terme dans c3 devrait être "True" (pour "not available"). Pour que ce soit le cas, nous devons relire le data-frame. Cette fois, nous allons [_forcer_](https://towardsdatascience.com/data-cleaning-with-python-and-pandas-detecting-missing-values-3e9c6ebcf78b) pandas à identifier "missing"/"not available"/"NA" comme des NaN.

Toutes les valeurs manquantes ont été identifiées, devons-nous nous en débarrasser en les supprimant complètement ?

Il semble que nous ayons perdu toutes les valeurs ! La méthode _.dropna()_ supprime la ligne complète (index) même si une seule valeur est manquante. Par conséquent, _.dropna()_ a le prix de perdre des données qui peuvent être précieuses.

#### Comment procéder ?

On pourrait présumer d'imputer toutes les valeurs manquantes avec zéro. Mais il y a un problème fondamental avec cette approche : _la sainteté/véracité de nos données est perdue, car dans le monde réel, une valeur manquante peut prendre n'importe quelle valeur. Mais nous la forçons à ne prendre qu'une seule valeur rigide, c'est-à-dire 0._

Le [_document officiel_](https://scikit-learn.org/stable/modules/impute.html) de sklearn mentionne : (l'accent est de moi)

>  infer them(missing values) from the **known** part of the data.

Alors, que devrions-nous faire maintenant ? Une meilleure option est d'utiliser la **moyenne** car elle est au moins un meilleur "représentant" d'une caractéristique que zéro. Pourquoi ? Parce que pour les caractéristiques continues/numériques, peu importe combien de fois nous ajoutons la moyenne, elle reste conservée. Voici comment :

> Trois nombres — 2, 6, 7 — ont une moyenne = (2 + 6 + 7)/3 = 5

> En supposant que cette liste a un nombre infini de valeurs manquantes, remplaçons-les par la moyenne : — 2, 6, 7, 5, 5, 5, 5….. La moyenne restera 5 peu importe combien de fois nous l'ajoutons !

Mais il y a des problèmes avec la moyenne. Premièrement, elle est fortement influencée par les valeurs aberrantes, moyenne(2 + 6 + 7 + **55**) = 17,5 ! Deuxièmement, bien qu'elle "représente" une caractéristique, elle est aussi la _pire_ pour refléter la tendance centrale d'une donnée normale (voir les puces ci-dessous **b & c** [respectivement pour les données asymétriques à droite et à gauche]).

![Image](https://cdn-media-1.freecodecamp.org/images/1*1xILJ73AYrAibYZrbpobbg.png)
_[commons.wikimedia](https://commons.wikimedia.org/wiki/File:Measures_of_Central_Tendency.png" rel="noopener" target="_blank" title=")_

Comme nous pouvons clairement l'observer dans les puces b & c, le mode reflète le mieux la tendance centrale. Le **mode** est la valeur la plus fréquente dans notre ensemble de données. Mais lorsqu'il s'agit de données continues, le mode peut créer des _ambiguïtés_. Il peut y avoir plus d'un mode ou (rarement) aucun du tout si aucune des valeurs n'est répétée. Le mode est ainsi utilisé pour imputer les valeurs manquantes dans les colonnes qui sont **catégorielles** par nature.

Après le mode, c'est la médiane qui reflète le mieux la tendance centrale. Ce qui implique que pour les données **continues**, l'utilisation de la médiane [_est meilleure_](https://creativemaths.net/blog/median/) que la moyenne ! La **médiane** est le score médian des points de données lorsqu'ils sont disposés dans l'ordre. Et contrairement à la moyenne, la médiane n'est pas influencée par les valeurs aberrantes de l'ensemble de données — la médiane des nombres déjà disposés (2, 6, 7, **55**) est 6,5 !

> Donc, pour les données catégorielles, l'utilisation du mode a plus de sens et pour les données continues, la médiane. Alors pourquoi utilisons-nous encore la moyenne pour les données continues ?

#### Héritage

Auparavant, dans un monde sans ordinateurs, il était plus facile de calculer la moyenne que la médiane. À cette époque, cela avait définitivement du sens car réorganiser manuellement des milliers d'entrées chaque fois que l'ensemble de données est mis à jour, puis trouver la médiane était effectivement une tâche fastidieuse. Mais devrions-nous continuer cet héritage, alors que nous avons le pouvoir de calcul à portée de main, aujourd'hui ? **Non**, cela impliquerait une sous-utilisation de notre potentiel.

Mais encore une fois, la rigidité reste, car nous utilisons toujours une _seule_ valeur — moyenne/médiane/mode. Nous en discuterons davantage dans la section suivante. Pour l'instant, remplaçons les valeurs par la moyenne (dans c0), la médiane (dans c1) et le mode (dans c3). Avant cela, traitons la valeur de garbage '#$%' à ('i2', 'c3').

Les valeurs respectives sont :

Nous utiliserons 3 méthodes différentes pour remplacer les NaN.

Il semble que nous devrons supprimer complètement la colonne c2 car elle ne contient aucune donnée. _Notez_ qu'au début, une ligne et une colonne étaient complètement remplies de NaN, mais nous n'avons pu manipuler avec succès que les lignes et non les colonnes. Suppression de c2.

Nous nous sommes enfin débarrassés de toutes les valeurs manquantes !

### Partie II : Remplacement aléatoire mais proportionnel (RBPR)

![Image](https://cdn-media-1.freecodecamp.org/images/1*QCpGBZ7v5RdL_oi7ChteSw.jpeg)
_Photo par [Pexels](https://www.pexels.com/@rakicevic-nenad-233369?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener" target="_blank" title="">Rakicevic Nenad</a> de <a href="https://www.pexels.com/photo/silhouette-of-person-holding-glass-mason-jar-1274260/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels" rel="noopener" target="_blank" title=")_

Les méthodes ci-dessus, _je pense_, peuvent être décrites comme des **approches d'imputation rigides**, car elles acceptent rigidement une seule valeur. Maintenant, concentrons-nous sur une approche d'imputation "souple". Souple car elle utilise des **probabilités**. Ici, nous ne sommes pas _forcés_ de choisir une seule valeur. Nous remplacerons les NaN _aléatoirement dans un ratio qui est "proportionnel" à la population sans NaN_ (la proportion est calculée en utilisant des probabilités mais avec une touche d'aléatoire).

Une explication avec un exemple serait meilleure. Supposons une liste ayant 15 éléments avec _un tiers de données manquantes_ :

[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, **_NaN, NaN, NaN, NaN, NaN_**] — — — (_original_)

Maintenant, observez dans la liste _originale_ qu'il y a des ensembles de **4** uns, **4** deux, **2** trois, et **5** NaN. Ainsi, les uns et les deux sont en **majorité** tandis que les trois sont en **minorité**. Maintenant, commençons par calculer les probabilités et les valeurs attendues.

* _prob_(1 se produisant dans les NaN)   
= (nombre de 1s)/(population sans NaN)  
= 4/10  
= 2/5
* Valeur attendue/comptage de 1  
= (prob) * (nombre total de NaN)  
= (2 / 5) * (5)  
= **2**

De même, la valeur attendue de prob(2 se produisant dans les NaN) est **2** et prob(3 se produisant dans les NaN) est **1** (Notez que **2+2+1=5**, est égal au nombre de NaN). Ainsi, notre liste ressemblera maintenant à ceci :

[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, **_1, 1, 2, 2, 3_**] — — — (_remplacé_par_proportion_)

Le ratio des uns, des deux et des trois remplaçant les NaN est ainsi **2 : 2 : 1**. C'est-à-dire que lorsque nous avons 'rien', il est **très probable** que les 'uns' et les 'deux' forment la majeure partie de celui-ci plutôt que les 'trois', au lieu d'une seule moyenne/mode/médiane rigide.

Si nous imputons simplement les NaN par la moyenne (1,8), alors notre liste ressemble à :

[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, **_1.8, 1.8, 1.8, 1.8, 1.8_**] — — — (_remplacé_par_moyenne_)

Traçons ces trois listes et tirons des **conclusions** de celles-ci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*07_PPCvgCODpm6kC1AQQyQ.png)
_[Code de la boîte à moustaches (NaN-12.py)](https://gist.github.com/Vernal-Inertia/e8d95749416b2df6b8f63ee124b7b73b" rel="noopener" target="_blank" title=")_

**Premièrement**, la liste avec remplacement proportionnel a une bien meilleure _distribution des données_ que celle remplacée par la moyenne. **Deuxièmement**, observez comment la moyenne affecte la distribution avec '3'_(une minorité) :_ elle n'était à l'origine _pas_ une valeur aberrante, soudainement devenue telle dans le graphique-2 mais a retrouvé son statut d'origine dans le graphique-3. Cela montre que la distribution du graphique-3 est moins [_biaisée_](https://towardsdatascience.com/is-your-machine-learning-model-biased-94f9ee176b67). **Troisièmement**, cette approche est également plus équitable, elle a donné à '3'_(la minorité)_ une "chance" dans les valeurs manquantes qu'elle n'aurait _jamais_ eue autrement. La **quatrième** beauté de cette approche est que nous avons toujours réussi à conserver la moyenne !

**Cinquième**, la distribution (basée sur la probabilité) garantit, sans aucun doute, que les chances de cette méthode à surajuster un modèle sont définitivement moindres que l'imputation avec l'approche _rigide_. **Sixième**, si les NaN sont remplacés "aléatoirement", alors en appliquant un peu de logique, nous pouvons facilement calculer qu'il y a : 5!/(2!*2!*1!) = 30, arrangements différents (permutations) possibles :

… 1, 1, 2, 2, 3],  
 … 1, 1, 2, 3, 2],  
 … 1, 1, 3, 2, 2],  
 … 1, 3, 1, 2, 2],  
 … 3, 1, 1, 2, 2] et 25 de plus !

Pour rendre ce dynamisme encore plus clair et intuitif, voyez ce gif avec 4 NaN. Chaque couleur représente une valeur NaN différente.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VJ4AX9GIyXmc013vlkDFCg.gif)

Remarquez comment différents arrangements génèrent différentes _interactions_ entre les colonnes chaque fois que nous exécutons le code. Par conséquent, nous ne générons pas de 'nouvelles' données ici, car nous utilisons simplement de manière ingénieuse les données déjà disponibles. Nous générons simplement de nouvelles interactions. _Et ces interactions fluctuantes sont la vraie **pénalité des NaN**._

#### Code :

Maintenant, codons ce concept et bornons-le. Le code pour traiter les caractéristiques numériques peut être trouvé [**_ici_**](https://gist.github.com/Vernal-Inertia/e49fc188e25d76f86df8a19874439b91) et pour les caractéristiques catégorielles [**_ici_**](https://gist.github.com/Vernal-Inertia/0a56f6b8b5aa5b6b175522dfc188b34f). (J'évite délibérément d'afficher le code ici car l'accent est mis sur le concept, et cela rendrait inutilement l'article long. Si vous trouvez le code utile et que vous êtes [algorithmiquement] _avide_ de l'optimiser davantage, je serais _ravi_ que vous le fassiez). Comment utiliser le code ?

```
random.seed = 0 np.random.seed = 0# important pour que les résultats soient reproductibles
```

```
# Le df_original est exempt d'impuretés (par exemple, pas de '$' ou ',' dans le champ de prix   # et df_original.dtypes sont tous définis.
```

```
1. df = df_original.copy()2. Appelez la fonction CountAll() donnée dans le code3. liste catégorielle = [tous les noms de colonnes catégorielles dans df]4. liste numérique = [tous les noms de colonnes numériques dans df]5. exécutez une boucle for pour remplir les NaN à travers la liste numérique, en utilisant la fonction Fill_NaNs_Numeric()6. exécutez une boucle for pour remplir les NaN à travers la liste catégorielle, en utilisant la fonction Fill_NaNs_Catigorical()7. effectuez une division train-test et vérifiez la précision (ne spécifiez pas le random_state)
```

```
(Après l'étape 7, nous avons besoin d'un peu de réglage de l'imputation. En veillant à ce que les étapes 1-7 soient dans une seule cellule, exécutez-la manuellement 15-20 fois pour avoir une idée de la 'plage' de précisions car elle continuera à fluctuer en raison de l'aléatoire. L'étape 7 aide à obtenir une estimation des limites des précisions et nous aide à réduire à la "meilleure précision")
```

```
8.("sautez" cette étape si df est extrêmement grand) exécutez une boucle while conditionnée à nouveau à travers 1 à 7 cette fois pour obtenir directement notre précision souhaitée (réglée).
```

```
(On peut vouloir écrire et sauvegarder ce 'df' mis à jour pour une utilisation future afin de s'épargner de répéter ce processus).
```

[**_Ici_**](https://gist.github.com/Vernal-Inertia/bf2e75e23ea0a508bbebfeadb0aafabe) se trouve un exemple complet, avec toutes les étapes mentionnées, sur le célèbre ensemble de données Iris inclus dans la bibliothèque sklearn. 20 % des valeurs de chaque colonne, y compris la cible, ont été supprimées aléatoirement. Ensuite, les NaN de cet ensemble de données sont imputés en utilisant _cette_ approche. À l'étape 7, il est facilement identifiable qu'après imputation, nous pouvons _ajuster_ notre _rappel_ à au moins ≥ 0,7 pour **"chaque" classe de la plante iris**, et c'est la condition à l'étape 8. Après plusieurs exécutions, quelques rapports sont les suivants :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytcUE1dbxPdPUBi6kvz_fA.png)
_Imputation souple sur l'ensemble de données Iris_

Ensuite, pour une deuxième confirmation, nous traçons les courbes PR après réglage, cette fois avec un RandomForestClassifier (n_estimators= 100). [les _classes_ sont {0 :'setosa', 1: 'versicolor', 2: 'virginica'}].

![Image](https://cdn-media-1.freecodecamp.org/images/1*7dI54GxjKeZsBJr45OPjDA.png)
_**Mesure de la qualité du RBPR par l'aire sous la courbe**_

Ces chiffres semblent corrects. Maintenant, tournons notre attention vers l'imputation _rigide_. _L'une_ des nombreux rapports de classification est montré ci-dessous : [observez les 1 (à discuter bientôt) dans la _précision_ et le _rappel_ ainsi que le **déséquilibre de classe** dans le _support_]

```
               precision  recall   f1-score   support
```

```
setosa           1.00      0.52      0.68        25versicolor       0.45      1.00      0.62         9virginica        0.67      0.73      0.70        11
```

#### La loi des grands nombres

Maintenant, utilisons la _loi des grands nombres_ en utilisant DecisionTreeClassifier pour effectuer 500 itérations, chacune avec un ensemble différent de valeurs supprimées aléatoirement, sur le même ensemble de données Iris **sans régler** les imputations ; c'est-à-dire, nous sautons l'étape de réglage pour obtenir "délibérément" les scores _souples_ les **pires**. Le code est [_ici_](https://gist.github.com/Vernal-Inertia/45cfda9c4fe06243d70a6a5b66b55b7e). Les comparaisons finales en termes de scores de précision et de rappel, pour l'imputation rigide et souple, sont les suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/1*D-P5ZuIpPbckBmsVkkx46A.png)
_**RAPPELS**_

![Image](https://cdn-media-1.freecodecamp.org/images/1*K3ZYGoCcngDYgbqmt3kSFg.png)
_**PRÉCISIONS**_

La _précision_ et le _rappel_ sont pratiques principalement lorsque nous observons un déséquilibre de classe. Bien qu'initialement, nous avions une cible bien équilibrée, l'imputation **rigide** avec le mode l'a rendue déséquilibrée. Observez un grand nombre de _rappels_ rigides et de _précisions_ rigides ayant une valeur = 1. Ici, l'utilisation du mot "surajusté" serait incorrecte car ce sont des scores de test et non d'entraînement. La bonne façon de le dire serait : le modèle prophétique _rigide_ savait déjà quoi prédire, ou l'utilisation du mode a assuré que les deux scores dépassent.

Maintenant, observez les scores **souples**. Malgré l'absence de _réglage_ ainsi que beaucoup moins de valeurs étant = 1, les scores _souples_ sont _toujours_ capables de **rattraper/converger** avec les scores _rigides_ (sauf dans deux cas — _rappel-versicolor_ et _précision-setosa_ — pour des raisons évidentes où un grand nombre de 1 prophétiques tirent de force la moyenne vers le haut). Observez également le _rappel-souple-setosa_ (malgré la présence de nombreux 1 dans le _homologue rigide_), et la _précision-souple-versicolor_ augmentée. La dernière chose à noter est la réduction globale de la variation et de l'écart-type dans l'approche _souple_.

Pour référence, les scores f1 et les scores de précision sont : (observez à nouveau la variation réduite et l'écart-type dans l'approche _souple_)

![Image](https://cdn-media-1.freecodecamp.org/images/1*vdMlSimy9p3L1C351cdu2A.png)
_**SCORE F1**_

![Image](https://cdn-media-1.freecodecamp.org/images/1*AVzJm2GtmGnmhgb6uFlGNQ.png)
_**SCORES DE PRÉCISION**_

> Ainsi, nous pouvons observer qu'à long terme, même **sans** réglage de l'imputation souple, nous avons obtenu des résultats qui correspondent à la performance de la stratégie d'imputation rigide. Ainsi, **après** réglage, nous pouvons obtenir des résultats encore meilleurs.

### Conclusion

Pourquoi faisons-nous cela ? La seule raison est d'améliorer nos chances de [_faire face à l'incertitude_](https://www.technologyreview.com/s/612764/giving-algorithms-a-sense-of-uncertainty-could-make-them-more-ethical/). _Nous ne nous pénalisons jamais pour les valeurs manquantes !_ Chaque fois que nous trouvons une valeur manquante, nous ancrons simplement notre navire au 'milieu' de la mer en supposant faussement que notre ancre a réussi à sonder la tranchée la plus profonde des "incertitudes". La tentative ici est de garder le navire en navigation en employant les ressources disponibles à portée de main — la vitesse et la direction du vent, la localisation des étoiles, l'énergie des vagues et des marées, etc. pour obtenir la meilleure 'diversification' de la prise, pour un meilleur retour.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TmIQgJZka4OWKUqECJvi5Q.jpeg)
_Photo par Simon Matzinger de Pexels_

(Si vous identifiez quelque chose de faux/incorrect, veuillez répondre. La critique est la bienvenue).