---
title: Comment utiliser les modèles linéaires et les arbres de décision en Julia
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-08-29T13:46:21.000Z'
originalURL: https://freecodecamp.org/news/linear-models-vs-decision-trees-in-julia
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/LinearModels-1.png
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: Julia
  slug: julia
- name: Julialang
  slug: julialang
- name: Machine Learning
  slug: machine-learning
seo_title: Comment utiliser les modèles linéaires et les arbres de décision en Julia
seo_desc: 'By Logan Kilpatrick

  As a machine learning engineer or data scientist, one of the most critical decisions
  you can make is what type of model to use to solve a specific problem.

  Do you really need to use Deep Learning to model this specific problem? Wi...'
---

Par Logan Kilpatrick

En tant qu'ingénieur en machine learning ou scientifique des données, l'une des décisions les plus critiques que vous puissiez prendre est de choisir quel type de modèle utiliser pour résoudre un problème spécifique.

Avez-vous vraiment besoin d'utiliser le Deep Learning pour modéliser ce problème spécifique ? Un modèle comme Random Forest ou un arbre de décision serait-il plus efficace ?

Bien que parfois la meilleure chose à faire soit d'essayer des choses et de voir par vous-même, il y a un certain contexte dont vous devriez être conscient lorsque vous évaluez spécifiquement un modèle linéaire par rapport à un arbre de décision.

**🚨 TL;DR** – Les modèles linéaires sont bons lorsque les données elles-mêmes ont une relation linéaire. Les arbres de décision, en revanche, sont utiles car ils peuvent modéliser des problèmes de classification ou de régression plus complexes avec des relations non linéaires de manière explicable.

Plongeons plus profondément dans les raisons pour lesquelles c'est le cas.

## Qu'est-ce qu'un modèle linéaire ? 🧑🏽‍🏫

Le terme modèle linéaire a de nombreuses significations différentes puisqu'il est utilisé dans plusieurs domaines, y compris, dans notre cas, le machine learning (ML).

Dans le monde du ML, les modèles linéaires désignent une classe spécifique de modèles où l'objectif est de cartographier la relation entre la ou les valeurs d'entrée et un résultat, généralement où une relation linéaire est présente (plus d'informations à ce sujet plus tard).

Un exemple classique de cela est la prédiction du prix d'une maison basée sur différents attributs (souvent appelés "features" en ML) tels que la superficie, le nombre de chambres, l'année de construction, et ainsi de suite.

Le modèle linéaire le plus couramment utilisé est la régression linéaire (LR) où le modèle devient essentiellement une ligne de meilleure adaptation pour les données que vous pouvez tracer comme montré ci-dessous.

Dans la LR, l'objectif principal est de prédire une valeur numérique, ce qui est différent de l'objectif d'un modèle de classification. En classification, nous voulons prédire la classe à laquelle certaines données d'entrée sont associées, ce qui peut souvent être un problème plus simple à modéliser.

![Graphique montrant une relation linéaire](https://www.freecodecamp.org/news/content/images/2022/08/linear.png)
_Exemple de régression linéaire. Image par l'auteur_

Tout comme dans d'autres formes de ML, nous entraînons le modèle linéaire en lui donnant des données d'entrée et de sortie d'entraînement qui sont utilisées pour définir les poids du modèle. Puisque cette méthode nécessite l'utilisation de données étiquetées, il s'agit d'un problème d'apprentissage supervisé.

Alors, quand utiliserais-je un modèle LR ? La règle générale est que les modèles LR ne fonctionnent que lorsque nous modélisons un type de relation qui est lui-même linéaire.

## Comprendre les relations linéaires

La prochaine question logique est donc : "Comment savoir si les données avec lesquelles je travaille ont une relation linéaire".

Avant de répondre à cela, il est important de souligner que la connaissance approfondie des données avec lesquelles vous travaillez dans un problème particulier de ML est probablement ce qui vous rendra le plus réussi dans la résolution du problème.

Dans le "monde réel", les ingénieurs et les scientifiques passent près de 80 % de leur temps à travailler avec des données, et seulement 20 % de leur temps à résoudre réellement des problèmes (ce qui est un problème en soi, mais c'est la réalité du moment).

D'accord, revenons donc aux relations linéaires dans les données et comment nous savons si cela existe pour notre ensemble de données. La manière la plus simple de tester cela est de simplement tracer les données et de les observer.

Si vous voyez un tracé comme celui représenté ci-dessus, vous êtes prêt puisque la relation semble être linéaire.

Si vous voyez un tracé comme celui ci-dessous, vous ne pourrez peut-être pas utiliser la LR.

![Graphique montrant une relation non linéaire](https://www.freecodecamp.org/news/content/images/2022/08/non-linear-2.png)
_Données non linéaires. Image par l'auteur_

Ensuite, regardons un modèle de régression linéaire en Julia. Si vous n'êtes pas familier avec Julia, vous pourriez vouloir consulter mon "**[Learn Julia For Beginners](https://www.freecodecamp.org/news/learn-julia-programming-language/)"** ici même sur freeCodeCamp.

## Régression linéaire en action 📣

Utilisons l'exemple de base du logement que j'ai mentionné précédemment. Vous pouvez télécharger les données à partir de [ce lien](https://raw.githubusercontent.com/julia4ta/tutorials/master/Series%2005/Files/housingdata.csv). Nous pouvons créer un nouveau fichier Julia et ajouter les importations suivantes :

```julia
using GLM, Plots, TypedTables, CSV
```

Le package clé ici est [GLM.jl](https://github.com/JuliaStats/GLM.jl) qui signifie Generalized linear models en Julia. Il nous aidera à créer le modèle initial LR ! Plots.jl, TypedTables.jl et CSV.jl jouent tous un rôle de soutien dans cet exemple.

L'étape suivante consiste à utiliser CSV.jl pour charger l'ensemble de données, puis à configurer nos valeurs X et Y :

```julia
housing_data = CSV.File("housingdata.csv")

X = housing_data.size

Y = housing_data.price

# Configuration d'une table typée
t = Table(X = X, Y = Y)
```

Ensuite, nous allons tracer les données pour nous assurer qu'il semble y avoir une relation linéaire présente :

```julia
# Utiliser le package Plots pour générer un nuage de points des données
gr(size = (600, 600))

# Créer un nuage de points
p_scatter = scatter(X, Y,
    xlims = (0, 5000),
    ylims = (0, 800000),
    xlabel = "Taille en pieds carrés",
    ylabel = "Prix de la maison",
    title = "Exemple de prix de l'immobilier freeCodeCamp",
    legend = false,
    color = :red
)
```

Cela générera un tracé qui ressemble à ceci :

![Tracé des prix de l'immobilier montrant une relation linéaire entre la taille et le prix](https://www.freecodecamp.org/news/content/images/2022/08/plot_5.svg)
_Image par l'auteur_

Nous pouvons voir que la relation semble être linéaire dans ce cas, ce qui signifie que nous pouvons procéder à la construction d'un modèle de base.

GLM fournit deux méthodes de base pour ajuster les modèles, vous pouvez [lire à ce sujet dans la documentation](https://juliastats.org/GLM.jl/stable/#Fitting-GLM-models). Pour notre exemple, nous utiliserons la première option qui ressemble à ceci :

```julia
lm(formula, data)
```

où formula signifie ce qui suit :

> `formula` : un objet [StatsModels.jl `Formula`](https://juliastats.org/StatsModels.jl/stable/formula/) faisant référence aux colonnes dans `data` ; par exemple, si les noms de colonnes sont `:Y`, `:X1`, et `:X2`, alors une formule valide est `@formula(Y ~ X1 + X2)`

Donc dans notre cas, puisque nous n'avons qu'une seule colonne (la taille de la maison), notre formule ressemblera à ceci :

```julia
ols = lm(@formula(Y ~ X), t)
```

Et nous passons à nouveau la variable `t` qui est les données auxquelles nous voulons ajuster le modèle.

Après cela, nous pouvons essayer de tracer le nouveau modèle ajusté sur le graphique initial pour voir à quoi il ressemble et s'il modélise correctement les données.

```julia
plot!(X, predict(ols), color = :green, linewidth = 3)
```

![Graphique des prix de l'immobilier montrant que le modèle de régression linéaire s'ajuste correctement aux données](https://www.freecodecamp.org/news/content/images/2022/08/plot_6.svg)
_Image par l'auteur_

Nous pouvons voir à partir de l'image ci-dessus que nous ajustons correctement le modèle aux données, ce qui signifie que nous l'avons fait ! Nous avons réussi à créer notre modèle de régression linéaire en Julia.

Faisons un autre test rapide pour voir si nous pouvons utiliser le modèle sur de nouvelles données pour une maison de seulement 750 pieds carrés :

```julia
small_house = Table(X = [750])

predict(ols, small_house)
```

Le modèle prédit que la maison coûtera `172164.45`, ce qui semble correct lorsque nous observons le graphique ci-dessus (malgré la plupart des données concernant des maisons de plus de 1 000 pieds carrés).

## Conclusion de la régression linéaire 🎀

Nous venons de terminer notre tour rapide des modèles linéaires en Julia. Nous avons parlé de pourquoi vous pourriez vouloir les utiliser, des contraintes (la relation doit être linéaire), de la manière de vérifier si la relation est linéaire, et de la manière d'ajuster une LR en Julia.

J'espère que cela a aidé à cadre le contexte pour savoir quand vous pourriez vouloir utiliser l'un de ces modèles ainsi que comment vous le feriez en pratique en utilisant Julia.

Si vous souhaitez en savoir plus sur les modèles LR en Julia, consultez ce tutoriel vidéo :

%[https://www.youtube.com/watch?v=n03pSsA7NtQ]

## Il est temps de parler des arbres de décision 🌴

Nous connaissons maintenant les principales contraintes des modèles linéaires : la relation doit être linéaire. Mais qu'en est-il des arbres de décision (DTs) ? Quel est leur principal cas d'utilisation et quelles sont les limitations ?

À leur cœur, les DTs nous permettent de modéliser le résultat de différents événements ou situations potentiels. Par exemple, vous pouvez créer un DT pour le résultat d'un lancer de pièce ou d'un autre événement. La structure de base ressemble à l'image suivante :

![Structure de base de l'arbre](https://www.freecodecamp.org/news/content/images/2022/08/tree.png)
_Arbre de décision. Image par l'auteur_

Ici, nous pouvons voir que nous commençons avec une certaine condition initiale, et selon le résultat de cette situation, nous allons dans l'un des trois nœuds possibles. Les nœuds externes ont une autre condition imbriquée associée, mais le nœud interne est un état final.

L'une des meilleures choses à propos des DTs est que pour notre exemple de données de logement, nous pouvons construire un arbre qui pourrait dire quelque chose comme : "Si la superficie est comprise entre 1000 et 2000 pieds, alors la valeur est de 400 000 $". C'est une simplification excessive, mais vous pouvez utiliser les DTs pour modéliser des exemples de régression ainsi que des problèmes de classification.

La raison pour laquelle cette structure si/alors est si importante est que l'arbre lui-même devient assez lisible par un humain. Cela contraste avec les modèles de ML dans le domaine du Deep Learning, par exemple, où ils sont des boîtes noires que nous ne pouvons généralement pas comprendre. L'explicabilité des DTs est l'une des raisons principales pour lesquelles les gens les utilisent en pratique.

## Arbres de décision vs régression linéaire

Une autre chose importante à souligner à propos des DTs, qui est la différence clé par rapport aux modèles linéaires, est que les DTs sont couramment utilisés pour modéliser des relations non linéaires.

Lorsqu'on traite des problèmes où de nombreuses variables sont en jeu, les arbres de décision sont également très utiles pour identifier rapidement les variables importantes.

Maintenant que nous connaissons les bases des arbres de décision (et si vous souhaitez encore en savoir plus sur le vocabulaire spécifique des arbres et autres, consultez [cet article](https://www.mastersindatascience.org/learning/machine-learning-algorithms/decision-tree/)), plongeons dans quelques exemples de code et configurons un arbre.

## Arbres de décision en action 🌳🚂

Pour cet exemple, nous utiliserons l'ensemble de données [Iris](https://archive.ics.uci.edu/ml/datasets/iris) avec le package [DecisionTree.jl](https://github.com/JuliaAI/DecisionTree.jl). Nous commençons par charger l'ensemble de données comme suit :

```julia
using DecisionTree

features, labels = load_data("iris")
```

Par défaut, la fonction `load_data` crée les variables `features` et `labels` de type `any`, ce qui est très coûteux en termes de calcul. Nous pouvons réduire cette charge en convertissant explicitement les types en float et string, respectivement :

```julia
features = float.(features)
labels   = string.(labels)
```

Ensuite, nous pouvons appeler la fonction `build_tree` et passer nos labels et features :

```julia
model = build_tree(labels, features)
```

Maintenant que nous avons notre arbre, nous devons l'élaguer pour obtenir des résultats.

```julia
model = prune_tree(model, 0.9)

# impression de l'arbre avec une profondeur de 6 nœuds (optionnel)
print_tree(model, 6)
```

Lorsque nous élaguons l'arbre, nous pouvons définir le niveau de pureté à 90 % dans ce cas, ce qui signifie que nous fusionnons les feuilles qui ont une pureté de 90 %.

La pureté dans les DTs est l'idée qu'il y a certaines données dans chaque décision qui tombent au mauvais endroit. Par exemple, nous pourrions n'avoir que 70 % des données que nous attendrions pour tomber dans une certaine classe, ce qui nous donnerait une pureté de 70 %.

La fonction `print_tree` ci-dessus est un bon moyen de voir ce que nous avons fait jusqu'à présent :

```julia
Feature 4 < 0.8 ?
├─ Iris-setosa : 50/50
└─ Feature 4 < 1.75 ?
    ├─ Feature 3 < 4.95 ?
        ├─ Iris-versicolor : 47/48
        └─ Feature 4 < 1.55 ?
            ├─ Iris-virginica : 3/3
            └─ Feature 3 < 5.45 ?
                ├─ Iris-versicolor : 2/2
                └─ Iris-virginica : 1/1
    └─ Feature 3 < 4.85 ?
        ├─ Feature 1 < 5.95 ?
            ├─ Iris-versicolor : 1/1
            └─ Iris-virginica : 2/2
        └─ Iris-virginica : 43/43
```

Cette visualisation nous montre exactement ce que fait l'arbre et comment il crée ces compartiments de classification. Il existe également des outils de visualisation plus avancés comme D3Trees.jl qui rendraient cela plus interactif à visualiser.

Maintenant que nous avons le modèle, nous pouvons le tester sur un seul point de données :

```julia
julia> apply_tree(model, [5.9,3.0,5.1,1.9])
"Iris-virginica"
```

Ou, nous pouvons faire des prédictions sur toutes nos données et regarder la matrice de confusion :

```julia
preds = apply_tree(model, features)

DecisionTree.confusion_matrix(labels, preds)

Classes:  ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
Matrix:   3×3 Matrix{Int64}:
 50   0   0
  0  50   0
  0   1  49

Accuracy: 0.9933333333333333
Kappa:    0.9899999999999998
3×3 Matrix{Int64}:
 50   0   0
  0  50   0
  0   1  49
```

Comme vous pouvez le voir, la précision de ce modèle est en fait assez bonne étant donné l'ensemble de données limité et le temps d'entraînement court.

Cet exemple devrait être suffisant pour vous lancer dans votre voyage DT, mais si vous avez besoin de plus d'aide, consultez cette vidéo géniale :

%[https://www.youtube.com/watch?v=XTApO31m3Xs]

## Conclusion 👋

Cet article était un tour rapide de certaines des différences entre les arbres de décision et les modèles linéaires ainsi que de la manière de les programmer en Julia.

J'espère que vous partez de cela avec la confiance que vous pouvez aller et appliquer ces outils dans vos propres flux de travail !

Si vous avez aimé l'article, envisagez de le partager et vous êtes toujours le bienvenu pour me contacter sur Twitter : [https://twitter.com/OfficialLoganK](https://twitter.com/OfficialLoganK)

Bon codage !