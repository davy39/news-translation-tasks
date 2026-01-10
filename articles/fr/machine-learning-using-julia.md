---
title: Machine learning avec Julia – Comment construire et déployer un modèle d'IA
  entraîné en tant que service web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-17T22:33:02.000Z'
originalURL: https://freecodecamp.org/news/machine-learning-using-julia
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/cover-3.png
tags:
- name: Julia
  slug: julia
- name: Machine Learning
  slug: machine-learning
seo_title: Machine learning avec Julia – Comment construire et déployer un modèle
  d'IA entraîné en tant que service web
seo_desc: 'By Andrey Germanov

  Julia is a general purpose programming language well suited for numerical analysis
  and computational science. Some consider it the future of machine learning and the
  most natural replacement for Python in this field.

  This article i...'
---

Par Andrey Germanov

[Julia](https://julialang.org/) est un langage de programmation généraliste bien adapté à l'analyse numérique et à la science computationnelle. Certains le considèrent comme l'avenir du machine learning et le remplacement le plus naturel de Python dans ce domaine.

Cet article présente le langage Julia et son écosystème. Vous apprendrez à l'utiliser pour résoudre une [compétition de machine learning sur le Titanic](https://www.kaggle.com/competitions/titanic) et à le soumettre à Kaggle. 

Vous apprendrez également à déployer votre modèle de machine learning en production en tant que service web et à créer une interface web pour envoyer des demandes de prédiction à ce service depuis un navigateur web.

À la fin de l'article, vous aurez créé une simple application web alimentée par l'IA que vous pourrez utiliser comme modèle pour créer des solutions ML Julia plus complexes.

Voici ce que nous allons couvrir :

1. [Ce que vous devez savoir à l'avance](#heading-ce-que-vous-devez-savoir-a-lavance)
2. [Pourquoi utiliser Julia pour le machine learning ?](#heading-pourquoi-utiliser-julia-pour-le-machine-learning)
3. [Comment installer Julia et le support des notebooks Jupyter](#heading-comment-installer-julia-et-le-support-des-notebooks-jupyter)
4. [Les bases du langage Julia](#heading-les-bases-du-langage-julia)
5. [Comment visualiser les données dans Julia](#heading-comment-visualiser-les-donnees-dans-julia)
6. [Aperçu du problème de machine learning du Titanic sur Kaggle](#heading-apercu-du-probleme-de-machine-learning-du-titanic-sur-kaggle)
7. [Comment préparer les données d'entraînement pour le machine learning](#heading-comment-preparer-les-donnees-dentrainement-pour-le-machine-learning)
8. [Comment entraîner notre modèle de machine learning](#heading-comment-entrainer-notre-modele-de-machine-learning)
9. [Comment faire des prédictions et les soumettre à Kaggle](#heading-comment-faire-des-predictions-et-les-soumettre-a-kaggle)
10. [Comment déployer le modèle en production](#heading-comment-deployer-le-modele-en-production)
11. [Conclusion](#heading-conclusion)

## Ce que vous devez savoir à l'avance

Ce n'est pas un livre, mais seulement un article. Je ne couvrirai pas tout et je suppose que vous avez déjà certaines connaissances de base pour que vous puissiez tirer le meilleur parti de sa lecture. 

Il est essentiel que vous soyez familier avec le machine learning en Python et que vous compreniez comment entraîner des modèles de machine learning en utilisant les bibliothèques Python [Numpy](https://numpy.org/), [Pandas](https://pandas.pydata.org/), [SciKit-Learn](https://scikit-learn.org/) et [Matplotlib](https://matplotlib.org/). 

De plus, je suppose que vous êtes familier avec la théorie du machine learning : [les types de problèmes de machine learning](https://www.practicalai.io/categorizing-machine-learning-problems/) comme la régression et la classification, le concept et le processus de [l'apprentissage supervisé](https://en.wikipedia.org/wiki/Supervised_learning) (fit/predict et évaluer la qualité en utilisant des métriques) et les modèles courants utilisés pour cela, y compris le [Random Forest Classifier](https://scikit-learn.org/stable/modules/ensemble.html#forest), et son implémentation dans la bibliothèque Python SciKit-Learn. 

De plus, ce serait bien si vous avez déjà participé à des compétitions Kaggle, car pour comprendre et exécuter tout le code de cet article, vous devez avoir un compte sur [https://kaggle.com](https://kaggle.com). 

Il existe déjà [beaucoup de livres](https://www.google.com/search?q=machine+learning+with+sklearn+books) écrits et [de nombreux cours déjà publiés](https://www.freecodecamp.org/news/machine-learning-for-everybody/) sur les sujets décrits ci-dessus. Dans cet article, mon objectif est de vous montrer comment créer, entraîner et déployer un modèle de machine learning de base en utilisant Julia, sans plonger dans les aspects théoriques du ML et de l'IA.

## Pourquoi utiliser Julia pour le machine learning ?

Pendant longtemps, Python a été une référence pour la science des données et le machine learning en raison de sa simplicité et de son excellent ensemble de bibliothèques et d'outils. 

Parmi d'autres, il existe de grandes bibliothèques comme Numpy pour vous aider à faire de l'algèbre linéaire avec des vecteurs et des matrices, Pandas pour manipuler des ensembles de données, Matplotlib pour les visualisations de données, et Scikit-Learn qui fournit une interface uniforme pour travailler avec des modèles de machine learning bien connus. 

De plus, les notebooks Jupyter vous permettent d'écrire et d'exécuter du code Python en ligne directement dans un navigateur web. Cela crée un environnement confortable pour les chercheurs en données pour concevoir et implémenter le cycle complet de machine learning même s'ils ne sont pas très expérimentés en programmation.

Tout cela est bon pour la recherche en laboratoire, mais à un moment donné, vous devez passer en production. À ce moment-là, les choses changent radicalement. 

Python a été créé au début des années quatre-vingt-dix et n'a jamais été censé être rapide. Son noyau n'a jamais été supposé être utilisé pour les nouvelles technologies modernes comme le calcul distribué. 

C'est pourquoi, pour rendre les tâches ML complexes prêtes pour la production, vous devez installer de nombreuses dépendances tierces. Vous devrez également employer quelques astuces pour accélérer le code Python. Vous pouvez même réécrire ou convertir des modèles de machine learning Python avant de les déployer en production dans des langages plus rapides comme C++.

Eh bien, Julia visait à résoudre ces problèmes. Voici ce que les auteurs ont écrit sur les raisons pour lesquelles ils ont créé Julia :

> Nous sommes gourmands : nous voulons plus. Nous voulons un langage open source, avec une licence libérale. Nous voulons la vitesse de C avec le dynamisme de Ruby. Nous voulons un langage qui soit homoiconique, avec de vraies macros comme Lisp, mais avec une notation mathématique évidente et familière comme Matlab. Nous voulons quelque chose d'aussi utilisable pour la programmation générale que Python, aussi facile pour les statistiques que R, aussi naturel pour le traitement des chaînes que Perl, aussi puissant pour l'algèbre linéaire que Matlab, aussi bon pour coller des programmes ensemble que le shell. Quelque chose qui soit simple à apprendre, mais qui garde les hackers les plus sérieux heureux. Nous le voulons interactif et nous le voulons compilé. Source : [Le blog Julia](https://julialang.org/blog/2012/02/why-we-created-julia/).

Ainsi, d'un point de vue ML, Julia a le meilleur des deux mondes. Il a été construit pour être aussi rapide que C et aussi simple que Python. De plus, il dispose de bibliothèques similaires à celles que les scientifiques des données Python sont habitués à intégrer dans leur travail :

<table>
    <tbody>
    <tr>
        <th>Objectif</th>
        <th>Python</th>
        <th>Julia</th>
    </tr>
    <tr>
        <td>Algèbre linéaire</td>
        <td><a href="https://numpy.org/">Numpy</a></td>
        <td>Tableaux intégrés, package <a href="https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/">LinearAlgebra</a></td>
    </tr>
    <tr>
        <td>Travail avec des ensembles de données</td>
        <td><a href="https://pandas.pydata.org/">Pandas</a></td>
        <td><a href="https://dataframes.juliadata.org/stable/">DataFrames.jl</a></td>
    </tr>
    <tr>
        <td>Visualisation de données</td>
        <td><a href="https://matplotlib.org/">Matplotlib</a></td>
        <td><a href="https://docs.juliaplots.org/stable/">Plots.jl</a></td>
    </tr>
    <tr>
        <td>Machine learning classique</td>
        <td><a href="https://scikit-learn.org/">SciKit-Learn</a></td>
        <td><a href="https://alan-turing-institute.github.io/MLJ.jl/dev/about_mlj/">MLJ.jl</a> ou <a href="https://scikitlearnjl.readthedocs.io/en/latest/">ScikitLearn.jl</a></td>
    </tr>
    <tr>
        <td>Réseaux de neurones</td>
        <td><a href="https://www.tensorflow.org/">TensorFlow</a> ou <a href="https://pytorch.org/">Pytorch</a></td>
        <td><a href="https://fluxml.ai/Flux.jl/stable/">Flux.jl</a></td>
    </tr>
    </tbody>
</table>

Vous pouvez lire plus sur pourquoi Julia est un excellent choix pour le machine learning [ici](https://towardsdatascience.com/the-future-of-machine-learning-and-why-it-looks-a-lot-like-julia-a0e26b51f6a6). 

De plus, Julia dispose d'un module pour supporter les notebooks Jupyter, vous pouvez donc écrire du code Julia là-bas de la même manière qu'avec Python. 

Tout cela rend Julia prêt à effectuer des tâches de machine learning, y compris les compétitions Kaggle, dans le même environnement que lorsque vous utilisez Python. 

Maintenant que vous savez pourquoi Julia est un excellent choix pour le ML, installons cet environnement et introduisons quelques bases du ML Julia.

## Comment installer Julia et le support des notebooks Jupyter

Pour installer Julia, suivez ce lien : [https://julialang.org/downloads/](https://julialang.org/downloads/). Là, téléchargez le package Julia pour votre système d'exploitation et exécutez-le. 

Après une installation réussie, vous pourrez exécuter la commande `julia` pour entrer dans l'environnement Julia REPL. Ici, vous pouvez écrire et exécuter du code Julia. Pour quitter REPL, tapez la commande `exit()`. 

De plus, vous pouvez écrire votre code dans n'importe quel éditeur de texte et l'enregistrer dans des fichiers avec l'extension `.jl`. Ensuite, vous pouvez exécuter vos programmes Julia avec cette commande :

```bash
julia <nom_du_fichier>.jl
```

De plus, vous pouvez utiliser VSCode pour développer en Julia. Il dispose d'une excellente extension pour cela : [https://www.julia-vscode.org/](https://www.julia-vscode.org/).

Cependant, la meilleure option pour développer des solutions de machine learning et de science des données est d'utiliser un [notebook Jupyter](https://jupyter.org/). Assurez-vous donc qu'il est [installé](https://jupyter.org/install) avant de continuer. Ensuite, installez le support Jupyter pour le package Julia en utilisant REPL :

* Entrez dans REPL en utilisant la commande `julia`
* Importez le module `Pkg` comme ceci :

```julia
using Pkg
```

* Ensuite, installez le package `IJulia` :

```julia
Pkg.add("IJulia")

* Quittez REPL en utilisant la commande `exit()`

Ensuite, vous pouvez exécuter Jupyter et créer des notebooks avec le support Julia. Pour votre commodité, la vidéo suivante montre comment installer Julia et l'intégrer à Jupyter sur macOS (en supposant que Jupyter lui-même est déjà installé).

%[https://youtu.be/rnJkT4G3-sE]

## Les bases du langage Julia

Julia a une syntaxe simple. Si vous êtes familier avec Python, alors il sera facile de commencer à écrire en Julia. Vous pouvez lire plus sur la syntaxe de base de Julia dans cet [article](https://www.freecodecamp.org/news/learn-julia-programming-language/). 

Dans ce tutoriel, je ne couvrirai que les fonctionnalités nécessaires pour le machine learning et seulement les fonctionnalités que nous utiliserons pour résoudre la compétition Kaggle du Titanic. Pour en savoir plus sur chacune de ces bibliothèques et modules, je fournirai des liens utiles.

Créez un nouveau notebook Jupyter pour entrer et exécuter tous les exemples de code ci-dessous.

### Fonctionnalités d'algèbre linéaire

Les fonctionnalités de base de l'algèbre linéaire sont déjà intégrées dans la bibliothèque standard de Julia. Chaque tableau 1D est un vecteur, et chaque tableau 2D fonctionne comme un tableau Numpy par défaut. Vous n'avez pas besoin d'inclure de packages supplémentaires pour cela. 

Par exemple, si vous écrivez et exécutez ce code :

```julia
A = [
    [1 2 3]
    [4 5 6]
    [7 8 9]
]
B = [
    [7 8 9]
    [4 5 6]
    [1 2 3]
]

A*B
```

Il effectuera une multiplication de matrices et affichera le résultat suivant :

```
3×3 Matrix{Int64}:
 18   24   30
 54   69   84
 90  114  138
```

Pour des fonctionnalités supplémentaires, vous pouvez importer le module LinearAlgebra.

```julia
using LinearAlgebra
```

Ensuite, vous pouvez utiliser des fonctions telles que `det`, `tr` ou `inv` avec des matrices pour obtenir leurs déterminants, traces ou matrices inverses, respectivement :

```julia
using LinearAlgebra

A = [
	[1 2 3]
	[4 5 6]
	[7 8 9]
]
println("Déterminant : ",det(A))
println("Trace : ",tr(A))
println("Inverse : ")
inv(A)
```

Vous pouvez en savoir plus sur les fonctionnalités d'algèbre linéaire dans la [documentation du module LinearAlgebra](https://docs.julialang.org/en/v1/stdlib/LinearAlgebra/).

### Comment travailler avec des ensembles de données dans Julia

Pour travailler avec des ensembles de données, vous devez installer un module externe `Dataframes.jl`. De plus, pour charger et sauvegarder des ensembles de données dans des fichiers CSV, vous devez ajouter le module `CSV.jl`.

Le gestionnaire de packages Julia est implémenté en tant que module `Pkg`, vous devez donc l'importer puis utiliser la méthode `add` pour installer les packages requis. 

Exécutez ceci dans votre notebook Jupyter pour installer ces packages :

```julia
using Pkg
Pkg.add("DataFrames")
Pkg.add("CSV")
```

Ensuite, vous pouvez importer les modules installés dans votre programme :

```julia
using DataFrames, CSV
```

Le module DataFrames importe le type de données `DataFrame` que vous utiliserez pour construire des ensembles de données et manipuler des objets de cadre de données. 

#### Comment créer un cadre de données

Voici comment vous pouvez créer un cadre de données avec deux colonnes :

```julia
df = DataFrame(name=["Julia", "Robert", "Bob","Mary"], age=[12,15,45,32])
```

Ce code créera et affichera l'ensemble de données suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/basic-df.png)
_Cadre de données des personnes_

#### Comment sélectionner des données dans un cadre de données

Pour sélectionner des données dans un cadre de données, vous pouvez utiliser la syntaxe de tableau :

```julia
df[<lignes>,<colonnes>]
```

Vous devez spécifier la plage de lignes à sélectionner dans `<lignes>` et la plage de colonnes à sélectionner dans `<colonnes>`. Vous pouvez utiliser cela pour sélectionner les trois premières lignes et seulement la colonne "âge" :

```julia
subs = df[1:3,"age"]
```

Il est important de noter que la numérotation des tableaux dans Julia commence à 1, et non à 0 comme dans la plupart des autres langages. Pour sélectionner les trois premières lignes et toutes les colonnes, vous pouvez exécuter ceci :

```julia
subs = df[1:3,:]
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/subset2.png)
_Sélectionner un sous-ensemble de lignes à partir d'un cadre de données_

De plus, pour sélectionner une seule colonne, vous pouvez utiliser la syntaxe par points :

```julia
names = df.name
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/names-column.png)
_Colonne des noms_

Comme vous le voyez, chaque colonne est un tableau natif Julia (vecteur).

Vous pouvez utiliser des conditions pour spécifier des plages de lignes. Par exemple, vous pouvez utiliser ce code pour sélectionner toutes les personnes d'un ensemble de données qui ont plus de 15 ans :

```julia
older = df[df.age .>15,:]
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/older.png)
_Cadre de données "older"_

Ce code placera toutes les personnes qui ont plus de 15 ans dans le cadre de données `older`.

#### Comment trier les données dans un cadre de données

Pour trier les données dans un cadre de données, vous pouvez utiliser la fonction `sort`. Cela triera l'ensemble de données par âge dans l'ordre croissant :

```julia
sort(df,"age")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/sort_ascending.png)
_Trier le cadre de données par âge dans l'ordre croissant_

Et ce code le triera dans l'ordre décroissant :

```julia
sort(df,"age",rev=true)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/sort_descending.png)
_Trier le cadre de données par âge dans l'ordre décroissant_

#### Comment ajouter des colonnes à un cadre de données

Pour ajouter une nouvelle colonne, utilisez simplement la syntaxe par points :

```julia
df.sex = ["female","male","male","female"]
```

Cela a ajouté la colonne `sex` pour les personnes au cadre de données.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/frame_with_sex.png)

#### Comment supprimer des colonnes d'un cadre de données

Vous pouvez utiliser la fonction `select` pour des extractions de données plus complexes à partir des cadres. En particulier, vous pouvez l'utiliser pour extraire toutes les colonnes sauf celle(s) spécifiée(s), ce qui équivaut à supprimer ces colonnes :

```julia
new_df = select(df,Not("sex"))
```

Ce code retourne un nouveau cadre de données en sélectionnant toutes les colonnes de l'original sauf `sex`.

#### Comment regrouper et résumer les données dans un cadre de données

Vous pouvez utiliser les fonctions `groupby` et `combine` pour regrouper les données et afficher des informations de résumé pour chaque groupe. La première regroupe les données par champ ou champs spécifiés et la seconde ajoute des colonnes de résumé, comme le nombre de lignes dans chaque groupe ou la valeur moyenne d'une colonne dans le groupe. 

Le code suivant regroupe les données par sexe, calcule le nombre de lignes dans chaque groupe et l'ajoute en tant que colonne "count" :

```julia
group_df = groupby(df,"sex")
combine(group_df,nrow => "count")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/group_count.png)
_Il y a deux femmes et deux hommes dans cet ensemble de données._

Ainsi, la première ligne de ce code crée un objet GroupDataFrame avec des lignes, regroupées par "sex". La deuxième ligne crée la colonne "count" avec le nombre d'éléments dans chaque groupe. Il y a 2 femmes et 2 hommes dans cet ensemble de données.

De plus, vous pouvez utiliser une fonction personnalisée pour calculer les données de résumé. Par exemple, vous pouvez utiliser ce code pour ajouter à la fois les comptes de lignes et les âges moyens pour chaque groupe :

```julia
combine(group_df, 
	nrow => "count", 
	"age" => ((rows) -> sum(rows)/length(rows)) => "Average Age"
)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/group_count_average-1.png)

Ce code ajoute la colonne "Average Age" qui est produite à partir des valeurs de la colonne "age" en appliquant une fonction anonyme personnalisée qui calcule la moyenne des valeurs dans ce groupe.

Ce n'est qu'un petit échantillon de toutes les manipulations possibles que vous pouvez faire avec les données en utilisant la bibliothèque DataFrames.jl. Vous pouvez en lire plus dans la [documentation](https://dataframes.juliadata.org/stable/).

### Comment visualiser les données dans Julia

En utilisant [Plots.jl](https://docs.juliaplots.org/stable/), vous pouvez créer de nombreux graphiques différents pour analyser vos données, similaires à [Matplotlib](https://matplotlib.org/) ou [Seaborn](https://seaborn.pydata.org/) en Python. Pour l'utiliser, vous devez installer le package `Plots` dans votre notebook et l'importer :

```julia
using Pkg
Pkg.add("Plots")
using Plots
```

Permettez-moi de fournir quelques exemples de graphiques.

**Graphique en ligne :**

```julia
plot([1,2,3,4,5],[3,6,9,15,16],title="Graphique en ligne de base",label="Ligne")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/basic_line_chart.png)
_Graphique en ligne de base_

**Nuage de points :**

```julia
plot([1,2,3,4,5],[3,6,9,15,16],title="Nuage de points de base",label="Données",seriestype="scatter")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/scatter_plot-1.png)
_Nuage de points de base_

**Graphique à barres :**

Le code suivant génère un graphique à barres à partir de l'ensemble de données `df` que nous avons créé précédemment.

```julia
plot(df.name,df.age,title="Âges",label=nothing,seriestype="bar")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/bar_chart.png)
_Graphique à barres_

Il y a beaucoup plus que vous pouvez faire en utilisant Plots.js. Lisez plus sur ses fonctionnalités dans la [documentation](https://docs.juliaplots.org/stable/).

Après cet aperçu des fonctionnalités de base de la science des données de Julia, il est temps de créer et d'entraîner notre premier modèle de machine learning et d'évaluer sa qualité dans la compétition.

## Aperçu du problème de machine learning du Titanic sur Kaggle

"Titanic - Machine Learning from Disaster" est l'un des premiers problèmes éducatifs de machine learning que vous pourriez voir dans de nombreux livres, articles ou cours. 

Dans cette tâche, vous disposez d'un ensemble de données sur les passagers du Titanic. Chaque donnée de passager comprend un ID, un nom, un sexe, le coût du billet, la classe du billet, le numéro de cabine, le port d'embarquement et le nombre de membres de la famille. 

Pour les passagers de cet ensemble de données, il est connu s'ils ont survécu ou non et le résultat est enregistré dans la colonne "Survived". Si le passager a survécu, la valeur est 1, sinon 0. 

Formellement, cela s'appelle un ensemble de données étiqueté ou **ensemble de données d'entraînement**. Toutes les colonnes de données sauf une appelée la "matrice de caractéristiques", et la colonne "Survived" appelée le "vecteur d'étiquettes".

Il existe également un deuxième ensemble de données avec les mêmes données sur d'autres passagers mais sans la colonne "Survived". En d'autres termes, cet ensemble de données ne contient que la matrice de caractéristiques, mais ne dispose pas du vecteur d'étiquettes. Cela s'appelle l'**ensemble de données de test**. 

La tâche consiste à entraîner un modèle de machine learning sur l'ensemble de données d'entraînement et à utiliser ce modèle pour prédire les valeurs de la colonne "Survived" dans l'ensemble de données de test. En d'autres termes, sa tâche est de prédire le "vecteur d'étiquettes" de l'ensemble de données de test sur la base de sa "matrice de caractéristiques".

La [compétition Kaggle est disponible ici](https://www.kaggle.com/competitions/titanic).

![Image](https://www.freecodecamp.org/news/content/images/2023/02/titanic1.png)
_La compétition Titanic_

Lisez brièvement la description, puis ouvrez la section "Évaluation" pour découvrir comment Kaggle évaluera les prédictions que vous soumettez.

## Comment préparer les données d'entraînement pour le machine learning

L'onglet "Données" sur la page de la compétition Kaggle contient des ensembles de données d'entraînement et de test dans les fichiers `train.csv` et `test.csv`, ainsi que des descriptions pour chaque colonne de données.

Créez un nouveau notebook Jupyter avec un backend Julia et téléchargez ces fichiers dans le même dossier que votre notebook.

Chargez `train.csv` dans `DataFrames` en utilisant le module CSV :

```julia
# Ajouter des packages
using Pkg
Pkg.add("DataFrames")
Pkg.add("CSV")

# Importer des modules
using DataFrames, CSV

# Charger les données d'entraînement dans un cadre de données
train_df = CSV.read("train.csv", DataFrame)
```

En cas d'erreurs, vérifiez simplement que le fichier `train.csv` existe dans le dossier où vous exécutez votre notebook.

S'il n'y a pas d'erreurs, il affichera les premières lignes des données :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Train-dataset.png)
_Ensemble de données d'entraînement_

Comme vous pouvez le voir, cet ensemble de données contient 891 lignes et 12 colonnes. Ce sont les données de base sur les passagers comme "Nom", "Sexe" et "Âge". De plus, nous voyons la colonne "Survived", avec 0 si le passager n'a pas survécu et 1 s'il a survécu.

Regardons les informations de résumé sur ces données en utilisant la fonction `describe` :

```julia
describe(train_df)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/data-summarty.png)
_Résumé des données d'entraînement_

Ce tableau de résumé montre des informations sur chaque colonne. Il montre le min, max, moyenne et médiane des données dans chacune d'elles. L'objectif de base de la préparation des données est de transformer ces colonnes en matrice de caractéristiques et vecteur d'étiquettes. 

Le vecteur d'étiquettes est prêt – c'est la colonne "Survived" avec des valeurs numériques. Toutes les autres colonnes forment la matrice de caractéristiques, et tout n'est pas correct avec elles.

Regardons le `nmissing` et `eltype` pour chaque colonne. Le `nmissing` montre le nombre de valeurs manquantes dans la colonne appropriée, et le `eltype` montre le type de valeurs de données qu'elles contiennent. 

La matrice ne doit contenir que des nombres, mais il y a de nombreuses colonnes de type de données "string". De plus, la matrice ne doit pas avoir de valeurs manquantes, mais nous avons des valeurs manquantes dans les colonnes `Age`, `Cabin` et `Embarked`. Corrigons tout cela.

### Comment corriger les valeurs manquantes

Comme le montre le tableau précédent, les colonnes `Age`, `Embarked` et `Cabin` contiennent des valeurs manquantes. La colonne `Embarked` a des blancs dans seulement 2 lignes, donc nous ne perdrons pas trop de données si nous supprimons simplement ces lignes. Le module DataFrames dispose d'une fonction pratique `dropmissing` que vous pouvez utiliser pour cela :

```julia
train_df = dropmissing(train_df,"Embarked")
```

Cela supprimera toutes les lignes avec des valeurs manquantes dans la colonne `Embarked`.

La colonne `Age` contient 177 valeurs manquantes. Ce n'est pas une bonne idée de supprimer ces lignes, car nous perdrions environ 20 % des données de l'ensemble de données. Donc, remplissons-la simplement avec quelque chose, par exemple avec la valeur médiane. 

L'âge médian est de 28 comme affiché dans le tableau de description. Utilisons la fonction `replace` de DataFrames pour remplacer les âges manquants par une valeur de 28 :

```julia
train_df.Age = replace(train_df.Age,missing=>28)
```

La colonne `Cabin` contient 687 valeurs manquantes, ce qui représente plus de 50 % de l'ensemble de données. Il y a trop peu de données dans cette colonne pour être utiles pour les prédictions. De plus, il est difficile de prédire quelles données devraient se trouver dans ces lignes si plus de données sont manquantes qu'existantes. Donc, supprimons simplement cette colonne en utilisant la fonction `select` :

```julia
train_df = select(train_df, Not("Cabin"))
```

Enfin, toutes les données manquantes dans l'ensemble de données sont corrigées.

### Comment corriger les données non numériques

Comme je l'ai expliqué précédemment, toutes les données doivent être encodées en nombres. Mais nous avons `Name`, `PassengerId`, `Sex`, `Ticket` et `Embarked` en tant que chaînes de caractères. 

Les valeurs `Name` et `PassengerId` sont uniques pour chaque passager, donc le modèle ML ne peut pas les utiliser pour diviser les données en catégories ou les classifier. Donc, vous pouvez simplement supprimer ces colonnes :

```julia
train_df = select(train_df,Not(["PassengerId","Name"]));
```

Pour les autres colonnes de chaînes de caractères, nous devons encoder toutes les valeurs de texte en nombres. Pour cela, nous devons découvrir toutes les valeurs uniques de ces colonnes. Commençons par `Embarked` :

```julia
combine(groupby(train_df,"Embarked"),nrow=>"count")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/embarked_group.png)
_Catégories Embarked_

Ce code a regroupé l'ensemble de données par la colonne `Embarked` et a montré toutes les valeurs possibles et leurs comptes. Donc, ici il y a seulement les valeurs "S", "C" et "Q". Il est facile de les encoder comme S=1, C=2, et Q=3. Vous pouvez faire cela simplement avec la fonction `replace` suivante :

```julia
train_df.Embarked = Int64.(replace(train_df.Embarked, "S" => 1, "C" => 2, "Q" => 3))
```

De plus, ce code a converti la colonne de "String" en type de données "Int64".

Ensuite, répétez la même chose pour la colonne `Sex` :

```julia
combine(groupby(train_df,"Sex"),nrow=>"count")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/sex_group.png)
_Catégories de sexe_

Et remplacez female par 1 et male par 2.

```julia
train_df.Sex = Int64.(replace(train_df.Sex, "female" => 1, "male" => 2))
```

Maintenant, il est temps de voir les informations de résumé pour la colonne `Ticket` :

```julia
combine(groupby(train_df,"Ticket"),nrow=>"count")
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/ticket_group.png)
_Catégories de billets_

Ici, nous voyons qu'il y a 680 catégories différentes de billets, ce qui représente plus de 50 % des données. Mais nous devons prédire seulement deux catégories, soit survécu ou non survécu. Nous ne sommes pas sûrs que ces données puissent aider le modèle à faire de bonnes prédictions sans traitement supplémentaire pour réduire le nombre de catégories dans cette colonne. 

Bien que cela dépasse notre modèle de base actuel, en tant que pratique supplémentaire, vous pouvez jouer un peu plus avec les données de cette colonne pour améliorer les résultats de prédiction. Par exemple, vous pouvez essayer de découvrir comment regrouper les billets en catégories plus générales et encoder ces catégories par des nombres uniques. 

Pour l'instant, supprimons simplement cette colonne :

```julia
train_df = select(train_df,Not("Ticket"))
```

Maintenant, toutes les données de chaîne sont catégorisées, et toutes les valeurs remplacées par des nombres. Décrire à nouveau l'ensemble de données pour s'assurer que tous les problèmes avec les données ont été résolus :

```julia
describe(train_df)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/fixed_train_data.png)
_Ensemble de données d'entraînement corrigé_

Vous pouvez voir que toutes les colonnes ne contiennent que des données numériques et qu'il n'y a pas de valeurs manquantes. 

### Analyse visuelle des données

Maintenant, nous sommes prêts à entraîner un modèle de machine learning sur notre ensemble de données. Visualisons ces données pour trouver certaines relations.

```julia
using Plots

# Regrouper l'ensemble de données par la colonne "Survived"
survived = combine(groupby(train_df,"Survived"), nrow => "Count")

# Afficher les données sur un graphique à barres
plot(survived.Survived, survived.Count, title="Passagers survivants", label=nothing, seriestype="bar", texts=survived.Count)

# Modifier l'axe X pour afficher des étiquettes de texte au lieu de nombres
xticks!([0:1:1;],["Not Survived","Survived"])
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/survived.png)

Ici, nous voyons que 340 passagers ont survécu. Maintenant, voyons comment ces passagers sont répartis par sexe.

```julia
# Regrouper l'ensemble de données par la colonne Sex et afficher uniquement les lignes où Survived=1
survived_by_sex = combine(groupby(train_df[train_df.Survived .== 1,:],"Sex"), nrow => "Count")

# Afficher les données sur un graphique à barres 
plot(survived_by_sex.Sex, survived_by_sex.Count, title="Passagers survivants par sexe", label=nothing, seriestype="bar", texts=survived_by_sex.Count)

# Modifier l'axe X pour afficher des étiquettes de texte au lieu de nombres
xticks!([1:1:2;],["Female","Male"])
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/survived_by_sex.png)

Intéressant, il y a deux fois plus de femmes qui ont survécu que d'hommes dans l'ensemble de données d'entraînement. Maintenant, voyons la distribution des passagers non survivants par classe de billet.

```julia
# Regrouper l'ensemble de données par la colonne PClass et afficher uniquement les lignes où Survived=0
death_by_pclass = combine(groupby(train_df[train_df.Survived .== 0,:],"Pclass"), nrow => "Count")

# Afficher les données sur un graphique à barres 
plot(death_by_pclass.Pclass, death_by_pclass.Count, title="Passagers décédés par classe de billet", label=nothing, 
    seriestype="bar", texts=death_by_pclass.Count)

# Modifier l'axe X pour afficher des étiquettes de texte au lieu de nombres
xticks!([1:1:3;],["First","Second","Third"])
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/survived_by_pclass.png)

Cela montre clairement que les passagers de première et de deuxième classe avaient plus de chances de survie que les passagers de troisième classe.

En supposant que les données dans les ensembles de données d'entraînement et de test sont distribuées aléatoirement, il est très probable qu'un modèle de machine learning entraîné sur ces données prédise que les femmes en première ou deuxième classe avaient beaucoup plus de chances de survie que les autres. 

Rappelons cette découverte pour vérifier cette hypothèse à la fin de l'article, après avoir entraîné et déployé le modèle ML.

Enfin, regardons à nouveau l'ensemble de données d'entraînement nettoyé :

```julia
train_df
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/data_matrix.png)
_L'ensemble de données d'entraînement nettoyé_

Maintenant, cela ressemble vraiment à une matrice – ou, pour être plus précis, à un système d'équations linéaires algébriques écrit sous forme matricielle. Les données au format matriciel sont exactement ce que la plupart des algorithmes de machine learning s'attendent à recevoir en entrée. Commençons.

## Comment entraîner notre modèle de machine learning

Pour le machine learning, nous utiliserons la bibliothèque [SciKitLearn.jl](https://github.com/cstjean/ScikitLearn.jl), qui réplique la bibliothèque [SciKit-Learn](https://scikit-learn.org/stable/) pour Python. Elle fournit une interface pour les modèles de machine learning couramment utilisés comme la régression logistique, l'arbre de décision ou la forêt aléatoire. 

SciKitLearn.jl n'est pas un seul package mais un riche écosystème avec de nombreux packages, et vous devez sélectionner lesquels installer et importer. Vous pouvez trouver une liste des modèles pris en charge [ici](https://cstjean.github.io/ScikitLearn.jl/dev/man/models/ ). Certains d'entre eux sont des modèles Julia intégrés, d'autres sont importés de Python. De plus, SciKitLearn.jl dispose de nombreux outils pour ajuster le processus d'apprentissage et évaluer les résultats. 

Pour cette tâche "Titanic", nous utiliserons le modèle `RandomForestClassifier` du package [DecisionTree.jl](https://juliapackages.com/p/decisiontree). Habituellement, il fonctionne bien pour les problèmes de classification. De plus, nous utiliserons le module [Cross Validation](https://scikit-learn.org/stable/modules/cross_validation.html) pour calculer la précision des prédictions du modèle à partir du package [SciKitLearn.CrossValidation](https://scikitlearnjl.readthedocs.io/en/latest/cross_validation/). 

Vous devez installer et importer ces packages avant de les utiliser :

```julia
Pkg.add("DecisionTree")
Pkg.add("SciKitLearn")
using DecisionTree, SciKitLearn.CrossValidation
```

Ensuite, nous implémenterons le processus d'entraînement. Tout d'abord, nous devons diviser l'ensemble de données d'entraînement en **matrice de caractéristiques** et **vecteur d'étiquettes**. Ensuite, nous devons créer le modèle `RandomForestClassifier` et l'entraîner en utilisant ces données. Enfin, nous évaluerons la précision des prédictions de ce modèle en utilisant la fonction `cross_val_score`.

```julia
# Mettre la colonne "Survived" dans le vecteur d'étiquettes
y = train_df[:,"Survived"]
# Mettre toutes les autres colonnes dans la matrice de caractéristiques (important de convertir en type de données "Matrix")
X = Matrix(train_df[:,Not(["Survived"])])

# Créer un classificateur Random Forest avec 100 arbres
model = RandomForestClassifier(n_trees=100)

# Entraîner le modèle, en utilisant la matrice de caractéristiques et le vecteur d'étiquettes
fit!(model,X,y)

# Évaluer la précision des prédictions en utilisant la validation croisée
accuracy = minimum(cross_val_score(model, X, y, cv=5))
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/cross_validation.png)
_La précision du modèle ML entraîné_

La validation croisée divise les tableaux X et y en 5 parties (folds) et retourne le tableau des précisions pour chacune de ces parties. Ensuite, la fonction `minimum` sélectionne la pire précision de ce tableau, ce qui signifie que toutes les autres sont meilleures que celle sélectionnée. 

Enfin, la précision obtenue est de plus de 0,78, soit 78 % pour nos données d'entraînement. Ce n'est pas mal, mais cela ne garantit pas que sur l'ensemble de données de test le résultat sera le même.

 Vous pouvez essayer d'améliorer cette valeur en sélectionnant différents modèles, ou en ajustant leurs hyperparamètres. 

Par exemple, vous pouvez augmenter le nombre d'arbres (n_trees) de 100 à 1000 ou le réduire à 10 et voir comment cela change la précision. Après avoir obtenu le meilleur résultat, il est temps de l'utiliser pour les prédictions.

## Comment faire des prédictions et les soumettre à Kaggle

Maintenant, lorsque le modèle est prêt, il est temps de l'appliquer aux données du fichier `test.csv` qui ne contient pas les étiquettes "survived". Tout d'abord, nous devons le charger et regarder le tableau de résumé comme nous l'avons fait pour l'ensemble de données d'entraînement :

```julia
test_df = CSV.read("test.csv",DataFrame)
describe(test_df)
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/tesing_description.png)
_Description de l'ensemble de données de test_

Ici, vous pouvez voir les mêmes problèmes avec les données : valeurs manquantes et colonnes de chaînes de caractères. Vous devez appliquer exactement les mêmes transformations à ces données que vous avez faites dans l'ensemble de données d'entraînement – sauf pour la suppression des lignes, car Kaggle exige que vous fassiez des prédictions pour chaque ligne, donc vous ne pouvez que remplir les valeurs manquantes. 

Heureusement, la colonne `Embarked` n'a pas de valeurs manquantes, donc il n'est pas nécessaire de la corriger. Cet ensemble de données a une seule valeur manquante dans la colonne `Fare`, mais nous n'avions aucune valeur manquante dans l'ensemble d'entraînement. Ce n'est pas un gros problème, car vous pouvez simplement remplacer cette valeur manquante par la médiane 14,4542.

Mais la première chose que nous devons faire est de sauvegarder la colonne `PassengerId` dans une variable séparée. Elle sera requise plus tard pour la soumission à Kaggle.

```julia
PassengerId = test_df[:,"PassengerId"]
```

Ensuite, appliquez toutes les techniques de correction de données requises :

```julia
# Répétez les mêmes transformations que nous avons faites pour l'ensemble de données d'entraînement
test_df = select(test_df,Not(["PassengerId","Name","Ticket","Cabin"]))
test_df.Age = replace(test_df.Age,missing=>28)
test_df.Embarked = replace(test_df.Embarked,"S" => 1, "C" => 2, "Q" => 3)
test_df.Embarked = convert.(Int64,test_df.Embarked)
test_df.Sex = replace(test_df.Sex,"female" => 1,"male" => 2)
test_df.Sex = convert.(Int64,test_df.Sex)

# En plus, remplacez la valeur manquante dans le champ 'Fare' par la médiane
test_df.Fare = replace(test_df.Fare,missing=>14.4542)
```

Après que l'ensemble de données de test soit propre, vous pouvez utiliser le modèle entraîné pour faire des prédictions :

```julia
Survived = predict(model, Matrix(test_df)) 
```

Ce code retourne un tableau de prédictions pour chaque ligne de la matrice de l'ensemble de données de test et le sauvegarde dans la variable `Survived`.

Maintenant, il est temps de le soumettre à Kaggle. Avant de le faire, regardez à nouveau l'onglet "Évaluation" sur la page de la compétition Titanic de Kaggle pour voir le format de soumission requis :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/evaluation.png)
_Description des règles de soumission de Kaggle_

La compétition nécessite un fichier CSV avec deux colonnes : "PassengerId" et "Survived". Vous avez déjà toutes ces données. Créons le cadre de données avec ces deux colonnes et sauvegardons-le dans un fichier CSV :

```julia
submit_df = DataFrame(PassengerId=PassengerId,Survived=Survived)
CSV.write("submission.csv",submit_df)
```

La première ligne de ce code construit le cadre de données `submit_df` avec la colonne `PassengerId` qui a été sauvegardée précédemment et la colonne `Survived` avec les prédictions pour chaque identifiant de passager. La deuxième ligne sauvegarde ce `submit_df` dans le fichier `submission.csv`. Voici à quoi ressemble le contenu de ce fichier :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/submit_dataframe.png)
_Cadre de données pour la soumission à Kaggle_

Enfin, allez sur la page de la compétition Kaggle, appuyez sur le bouton "Submit Predictions", téléchargez le fichier `submission.csv` et voyez votre résultat. Lorsque je l'ai fait, j'ai reçu ce qui suit :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/SUBMIT.png)
_Résultat de la soumission à Kaggle_

La précision de la prédiction est de 0,76555, soit plus de 76 %, et est proche de la précision que nous avons obtenue sur l'ensemble de données d'entraînement. 

Pas mal pour la première fois, mais vous pouvez continuer : jouer avec les données, essayer différents modèles, changer leurs hyperparamètres, surfer sur Internet pour des articles et des notebooks Jupyter d'autres personnes qui ont résolu la compétition Titanic auparavant. Je sais qu'il est possible d'atteindre jusqu'à 98 % de précision en utilisant divers trucs avec les modèles et les données.

## Comment déployer le modèle en production

C'est amusant de jouer avec le machine learning sur votre ordinateur, mais cela n'a pas beaucoup d'impact sur les problèmes du monde réel. 

Habituellement, les clients n'ont pas de notebooks Jupyter et ils n'entraînent pas les modèles. Ils doivent avoir un outil simple qui les aidera à prendre des décisions basées sur les prédictions à partir des données qu'ils ont. 

C'est pourquoi la seule chose vraiment importante est la façon dont vos modèles fonctionnent en production. 

Dans cette section, je vais expliquer comment utiliser Julia pour créer une application web qui chargera le modèle de machine learning que vous avez entraîné pour faire des prédictions en ligne dans un navigateur web.

### Comment exporter le modèle vers un fichier

Tout d'abord, vous devez sauvegarder le `model` du notebook dans un fichier. Pour cela, vous pouvez utiliser le module [JLD2.jl](https://github.com/JuliaIO/JLD2.jl). Ce module est utilisé pour sérialiser les objets Julia au format compatible HDF5 (qui est bien connu des scientifiques des données Python) et le sauvegarder dans un fichier. 

Installez et chargez le package dans le notebook :

```julia
Pkg.add("JLD2")
using JLD2
```

et ensuite sauvegardez la variable `model` dans le fichier `titanic.jld2` :

```julia
save_object("titanic.jld2", model)
```

Nous avons terminé notre travail avec le notebook Jupyter maintenant. Vous devez écrire tout le code suivant en tant qu'application séparée. 

Créez un dossier pour une nouvelle application, par exemple `titanic`, et copiez le fichier `titanic.jld2` dedans.

Maintenant, vous pouvez créer un fichier texte `titanic.jl` qui contiendra le code de l'application web que vous allez écrire bientôt. Utilisez n'importe quel éditeur de texte pour cela – VS Code avec l'[extension Julia](https://www.julia-vscode.org/) est un bon choix. Entrez le code suivant dans `titanic.jl` :

```julia
using JLD2, DecisionTree
model = load_object("titanic2.jld2")
survived = predict(model,[1 2 35 0 2 144.5 1])
println(survived)
```

Ce code importe d'abord les modules requis. Comme vous pouvez le voir, seuls deux modules sont nécessaires pour exécuter le processus de prédiction : `JLD2` pour charger l'objet modèle, et `DecisionTree` pour exécuter la fonction `predict` pour le RandomForestClassifier. 

Ensuite, le code charge le modèle à partir du fichier et fait des prédictions pour une seule ligne de données. Les colonnes de cette ligne doivent être dans le même ordre que celui passé à partir de l'ensemble de données lorsque nous avons entraîné le modèle : `Pclass`, `Sex`, `Age`, `SibSp`, `Parch`, `Fare` et `Embarked`. 

Enfin, il imprime le tableau des prédictions. Dans ce cas, il imprimera le tableau avec un seul élément, car une seule ligne de données a été passée au modèle pour les prédictions.

Vous pouvez exécuter ce code en utilisant la commande `julia` :

```
julia titanic.jl
```

Si tout a fonctionné correctement, il devrait imprimer `[0]` ou `[1]` sur la console en fonction du résultat de la prédiction. Si vous recevez des erreurs, vous devrez peut-être installer les packages `JLD2` et `DecisionTree` en utilisant l'environnement Julia REPL, comme vous l'avez fait dans le notebook Jupyter.

Maintenant, refactorisons ce code en une fonction qui recevra la ligne de données et retournera une prédiction de survie (soit 0 soit 1) :

```julia
using JLD2, DecisionTree

# Retourne 1 si un passager avec
# les 'data' spécifiées a survécu ou 0 sinon
function isSurvived(data)
	model = load_object("titanic2.jld2")
	survived = predict(model,data)
	return survived[1]
end
```

### Comment créer le front-end

L'étape suivante consiste à créer une interface web qui sera utilisée pour collecter les `data` pour cette fonction. Cela ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/02/ui.png)
_Interface utilisateur de l'application web_

Avec cette interface, l'utilisateur peut entrer les données concernant un passager, puis appuyer sur le bouton "PREDICT" et découvrir si le passager avec ces données aurait pu survivre sur le Titanic ou non. Voici le code HTML pour cette page web :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Titanic</title>
</head>
<body>
    <table>
        <tbody>
            <tr>
                <td>Classe de billet</td>
                <td>
                    <select id="pclass">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Sexe</td>
                <td>
                    <select id="sex">
                        <option value="1">Femme</option>                        
                        <option value="2">Homme</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Âge</td>
                <td>
                    <input id="age" type="number"/>
                </td>
            </tr>
            <tr>
                <td>Nombre de frères/sœurs/conjoints</td>
                <td>
                    <input id="sibsp" type="number"/>
                </td>
            </tr>
            <tr>
                <td>Nombre de parents/enfants</td>
                <td>
                    <input id="parch" type="number"/>
                </td>
            </tr>
            <tr>
                <td>Tarif</td>
                <td>
                    <input id="fare"/>
                </td>
            </tr>
            <tr>
                <td>Embarqué</td>
                <td>
                    <select id="embarked">
                        <option value="1">S</option>
                        <option value="2">C</option>
                        <option value="3">Q</option>
                    </select>
                </td>
            </tr>
            <tr>
                <td>Survécu</td>
                <td id="survived"></td>
            </tr>
            <tr>
                <td colspan="2">
                    <div>
                        <button id="submit" type="button">PRÉDIRE</button>
                    </div>
                </td>
            </tr>
        </tbody>
    </table>
    <script>
        document.getElementById("survived").innerHTML = "";
        document.getElementById("submit").addEventListener("click",async() => {
            response = await fetch("http://localhost:8080",{
                method:"POST",
                body: JSON.stringify({
                    "pclass":parseInt(document.getElementById("pclass").value),
                    "sex":parseInt(document.getElementById("sex").value),
                    "age":parseFloat(document.getElementById("age").value),
                    "sibsp":parseInt(document.getElementById("sibsp").value),
                    "parch":parseInt(document.getElementById("parch").value),
                    "fare":parseFloat(document.getElementById("fare").value),
                    "embarked":parseInt(document.getElementById("embarked").value),
                })
            });
            const survivedCode =  parseInt(await response.text());
            document.getElementById("survived").innerHTML = survivedCode ? "OUI" : "NON"
        })
    </script>
    <style>
        input,select {
            width:100%;
        }
        td {
            padding:5px;
        }
        td > div {
            text-align: center;
        }
        #survived {
            font-weight: bold;
            color:green;
        }
    </style>
</body>
</html>
```

Créez un fichier `index.html` dans le même dossier et copiez ce code dedans. La partie HTML du fichier contient un simple formulaire avec tous les champs de données. Comme vous pouvez le voir, toutes les valeurs sont encodées avec les mêmes nombres que nous avons utilisés pour les données dans les ensembles de données d'entraînement et de test. 

Ensuite, la partie JavaScript de ce code définit le gestionnaire du bouton "PRÉDIRE". Lorsque l'utilisateur clique dessus, le script collecte toutes les données saisies et les sauvegarde sous forme de chaîne JSON. Ensuite, il effectue une requête AJAX au service web s'exécutant sur le port 8080 de l'hôte local (que nous n'avons pas encore créé) et envoie ce JSON au service web.

Ainsi, le service web doit être capable de recevoir des requêtes HTTP POST avec un corps JSON au format suivant :

```json
{
     "pclass": 1,
        "sex": 1,
        "age": 32,
      "sibsp": 5,
      "parch": 6,
       "fare": 123.44,
   "embarked": 1
}
```

### Comment créer le back-end

Maintenant, il est temps de modifier le fichier `julia.jl` pour qu'il fonctionne comme un serveur web capable d'afficher la page `index.html`, de recevoir des requêtes POST, de parser le corps de cette requête en JSON, de faire des prédictions basées sur ces données JSON et de retourner cette prédiction à la page web.

Créer un serveur web sur Julia est la même chose que sur Python, Go ou Node.js. En utilisant le package HTTP.jl, vous pouvez créer et exécuter un serveur web avec une seule ligne de code :

```julia
using HTTP

HTTP.serve(handler,8080)

function handler(req)
	# gérer la requête HTTP
end
```

La fonction `HTTP.serve` exécute le serveur web sur le port spécifié. Chaque fois que le serveur web reçoit une requête client, il appelle la fonction `handler` spécifiée et envoie un objet de requête HTTP en tant qu'argument `req`. 

La fonction doit lire cette requête, la traiter et écrire une réponse au client appelant.

Le champ `req.url` contient l'URL de la requête reçue. Le champ `req.method` contient la méthode de requête, comme GET ou POST. Le champ `req.body` contient le corps POST de la requête au format binaire. L'objet de requête HTTP contient beaucoup d'autres informations. Tout cela peut être trouvé dans la [documentation](https://github.com/JuliaWeb/HTTP.jl) de HTTP.jl. 

Notre application web ne vérifiera que la méthode de requête. Si la requête reçue est une requête POST, elle analysera `req.body` en objet JSON et enverra les données de cet objet à la fonction `isSurvived` pour faire une prédiction et la retourner au navigateur client. 

Pour tous les autres types de requêtes, elle retournera simplement le contenu du fichier `index.html`, pour afficher l'interface web. 

Voici à quoi ressemble le code source complet du service web `titanic.jl` :

```julia
using JLD2, DecisionTree

# Retourne 1 si un passager avec
# les 'data' spécifiées a survécu ou 0 sinon
function isSurvived(data)
	model = load_object("titanic.jld2")
	survived = predict(model,data)
	return survived[1]
end

using HTTP,JSON3

function handle(req)
    if req.method == "POST"
        form = JSON3.read(String(req.body))
        survived = isSurvived([
            form.pclass
            form.sex
            form.age
            form.sibsp
            form.parch
            form.fare
            form.embarked
        ])
        return HTTP.Response(200,"$survived")
    end
    return HTTP.Response(200,read("./index.html"))
end

HTTP.serve(handle, 8080)
```

Avant de l'exécuter, vous devez installer le package HTTP.jl en exécutant `Pkg.add("HTTP")` dans l'environnement Julia REPL.

Le code du service web vient juste après la fonction `isSurvived`. Tout d'abord, les modules requis sont importés : `HTTP` pour créer un serveur web et `JSON3` pour analyser le JSON du corps de la requête. 

Ensuite, la fonction `handler` est définie. La fonction vérifie la méthode de requête des requêtes reçues et si elle est égale à POST, elle convertit le corps JSON de cette requête en objet `form`. Ensuite, en utilisant les champs de cet objet, la fonction `isSurvived` est appelée. 

Il est important de mettre les éléments du tableau dans le bon ordre ici. 

Enfin, le résultat de la prédiction est retourné au client en utilisant la fonction `HTTP.Response`.

Pour tous les autres types de requêtes, la fonction retourne le corps du fichier `index.html` dans la ligne `HTTP.Response(200,read("./index.html"))`.

Enfin, la fonction `HTTP.serve` démarre un serveur web sur le port 8080 qui attend les requêtes HTTP et les traite en utilisant la fonction `handle`, comme défini ci-dessus. 

Maintenant, vous pouvez exécuter cela en tapant `julia titanic.jl` dans le terminal ou en appuyant sur Ctrl+F5 dans VSCode. Ensuite, vous pouvez accéder à l'interface web depuis un navigateur web sur `http://localhost:8080` et jouer avec le service en entrant des données dans le formulaire, en appuyant sur le bouton `PRÉDIRE`, et en voyant soit `OUI` soit `NON` sur la ligne `Survived` en fonction du résultat de la prédiction. 

Vous pouvez vérifier l'hypothèse que nous avons faite à partir des graphiques à barres : _les femmes en première ou deuxième classe ont plus de chances de survie que les autres_.

## Conclusion

Dans cet article, je vous ai présenté le langage de programmation Julia ainsi que son écosystème et expliqué pourquoi il est si génial pour le machine learning. 

Je vous ai montré comment configurer un environnement de développement confortable et donné un bref aperçu des modules Julia courants utilisés pour la science des données. 

Ensuite, je vous ai guidé à travers le processus d'entraînement du modèle de machine learning pour la compétition Titanic et vous ai montré comment faire des prédictions et les soumettre à la plateforme Kaggle pour le scoring. 

Enfin, je vous ai montré comment exporter ce modèle vers une application externe, créer le service web avec ce modèle et l'interface web pour entrer les données dans le formulaire, et prédire si l'humain avec ces données aurait pu survivre sur le Titanic ou non.

Pour tous les sujets qui ont été expliqués brièvement, j'ai fourni des liens avec une documentation plus approfondie. De plus, je vous recommande vivement de lire ce [livre en ligne sur la science des données avec Julia](https://juliadatascience.io/) et d'étudier le grand ensemble d'exemples de machine learning dans le [dépôt GitHub de l'Académie Julia Data Science](https://github.com/JuliaAcademy/DataScience).

Voir le code source de cet article, y compris le notebook Jupyter et le service web [dans ce dépôt](https://github.com/AndreyGermanov/julia_titanic_model).

Amusez-vous à coder et ne cessez jamais d'apprendre ! 

Vous pouvez me trouver sur [LinkedIn](https://www.linkedin.com/in/andrey-germanov-dev/), [Twitter](https://twitter.com/GermanovDev), et [Facebook](https://www.facebook.com/AndreyGermanovDev) pour être le premier informé des nouveaux articles comme celui-ci et d'autres nouvelles sur le développement logiciel.