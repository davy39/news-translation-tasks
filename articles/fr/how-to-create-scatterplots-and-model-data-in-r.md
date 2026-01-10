---
title: Comment créer des nuées de points et modéliser des données dans R en utilisant
  ggplot2
subtitle: ''
author: Tiffany Mojo Omondi
co_authors: []
series: null
date: '2026-01-05T12:05:54.926Z'
originalURL: https://freecodecamp.org/news/how-to-create-scatterplots-and-model-data-in-r
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767614352690/8b993426-f193-4ff3-b5ec-dd6dda11028e.png
tags:
- name: data visualization
  slug: data-visualization
- name: data analysis
  slug: data-analysis
- name: R Language
  slug: r
- name: R Programming
  slug: r-programming
seo_title: Comment créer des nuées de points et modéliser des données dans R en utilisant
  ggplot2
seo_desc: You can use R as a powerful tool for data analysis, data visualization,
  and statistical modelling. In this guide, you’ll learn how to load real-world data
  into R, visualize patterns using ggplot2, build simple linear and logistic regression
  models, a...
---

Vous pouvez utiliser R comme un outil puissant pour l'analyse de données, la visualisation de données et la modélisation statistique. Dans ce guide, vous apprendrez à charger des données réelles dans R, à visualiser des motifs en utilisant ggplot2, à construire des modèles de régression linéaire et logistique simples, et à interpréter les modèles. À la fin, vous devriez savoir comment utiliser R pour vos propres projets.

## Table des matières


* [Prérequis](#heading-prerequis)
    
* [Comment configurer votre environnement R](#heading-comment-configurer-votre-environnement-r)
    
* [Comment utiliser les types de données dans R](#heading-comment-utiliser-les-types-de-donnees-dans-r)
    
* [Comment utiliser les structures de données dans R](#heading-comment-utiliser-les-structures-de-donnees-dans-r)
    
* [Comment importer des données dans R](#heading-comment-importer-des-donnees-dans-r)
    
* [Comment visualiser des données avec ggplot2](#heading-comment-visualiser-des-donnees-avec-ggplot2)
    
* [Comment construire des modèles statistiques dans R](#heading-comment-construire-des-modeles-statistiques-dans-r)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer, vous devez avoir les éléments suivants :

* R installé (version 4.0 ou supérieure).
    
* RStudio installé (recommandé pour les débutants).
    
* Une familiarité de base avec les concepts de programmation tels que les variables et les fonctions.
    
* Une compréhension de base des statistiques (moyenne, corrélation, régression).
    

## Comment configurer votre environnement R

Avant de commencer à travailler avec des données, chargez les bibliothèques requises :

```plaintext
library(tidyverse)   # Manipulation de données + ggplot2
library(readxl)      # Importation de fichiers Excel
```

Cela charge les bibliothèques requises dans R. `tidyverse` est une collection de packages utilisés pour la manipulation et la visualisation de données, y compris `ggplot2`. `readxl` vous permet d'importer des fichiers Excel directement dans R sans les convertir au format CSV au préalable.

## Comment utiliser les types de données dans R

Connaître les types de données vous aide à éviter les erreurs et à choisir les bonnes méthodes d'analyse.

### Types de données courants

| Type de données | Exemple | Cas d'utilisation |
| --- | --- | --- |
| Numérique | `x <- 5.7` | Mesures, prix |
| Entier | `y <- 10L` | Comptages |
| Caractère | `"Prix des maisons"` | Étiquettes de texte |
| Logique | `TRUE` | Conditions |
| Complexe | `2 + 3i` | Mathématiques avancées |

### Types de données numériques dans R

```r
prix <- 199.99
taxe <- 16.5
coût_total <- prix + taxe
coût_total
```

Les données numériques sont utilisées pour des valeurs continues telles que les mesures, les prix ou les moyennes. Comme vous pouvez le voir, ce sont des valeurs numériques qui peuvent être utilisées dans un calcul. Les types de données numériques permettent des opérations arithmétiques telles que l'addition, la soustraction, la multiplication et la division.

### Types de données entières dans R

```r
étudiants <- 30L
classes <- 4L
étudiants_totaux <- étudiants * classes
étudiants_totaux
```

Les entiers sont des nombres entiers et sont couramment utilisés pour le comptage. Le `L` indique à R que les valeurs sont des entiers. Les entiers sont utiles lorsque vous travaillez avec des comptages, des index ou des valeurs discrètes.

### Types de données caractères dans R

```r
nom_cours <- "Science des données"
université <- "Université Harvard"
paste(nom_cours, "à", université)
```

Les données caractères sont utilisées pour stocker du texte tel que des noms, des étiquettes ou des catégories. L'exemple ci-dessus montre comment les données caractères peuvent être combinées en utilisant la fonction `paste()`. Ce type de données ne peut pas être utilisé dans des opérations mathématiques.

### Types de données logiques dans R

```r
score <- 75
réussi <- score >= 50
réussi
```

Les données logiques représentent des valeurs booléennes : `TRUE` ou `FALSE`. Celles-ci sont couramment utilisées dans des conditions et des filtres. Ici, R évalue une condition et retourne `TRUE` parce que le score répond à l'exigence. Les valeurs logiques sont essentielles dans la prise de décision et le flux de contrôle.

### Types de données complexes dans R

Les nombres complexes contiennent à la fois des parties réelles et imaginaires et sont principalement utilisés dans des calculs mathématiques avancés.

```r
z <- 2 + 3i
Mod(z)
```

Cet exemple calcule la magnitude d'un nombre complexe. Les types de données complexes sont rarement utilisés dans l'analyse de données de base mais sont disponibles dans R.

## Comment utiliser les structures de données dans R

R stocke les données dans différentes structures en fonction de vos objectifs. Cela est important car choisir la bonne structure rend les opérations plus faciles. Ses fonctions se comportent différemment en fonction de la structure. De plus, les structures aident R à comprendre si vos données sont des nombres, des catégories ou du texte.

### Structures de données courantes dans R

| Structure | Meilleure pour |
| --- | --- |
| Vecteur | Colonne unique de données |
| Matrice | Tableaux numériques |
| Data Frame | Données de type tableau |
| Liste | Objets mixtes |

```r
vec <- c(1, 2, 3, 4)
mat <- matrix(1:9, nrow = 3)
df <- data.frame(Name = c("Voiture", "Vélo"), Number = c(110, 95))
lst <- list(numbers = vec, matrix = mat, info = df)

str(lst) ##montre la structure de la liste
```

Comprenons le code ci-dessus :

* `vec` est un vecteur qui stocke un seul type de données.
    
* `mat` est une matrice qui organise des valeurs numériques en lignes et colonnes.
    
* `df` est un data frame qui fonctionne comme un tableau, permettant différents types de données dans chaque colonne.
    
* `lst` est une liste qui stocke plusieurs objets de différents types.
    
* La fonction `str()` montre comment ces objets sont imbriqués dans la liste.
    

## **Comment importer des données dans R**

Maintenant, vous pouvez commencer à travailler avec vos données réelles. Vous pouvez importer des fichiers dans R en copiant le chemin du fichier CSV ou Excel et en le collant dans la commande.

**Pour Windows :** Remplacez les barres obliques inverses simples / par des barres obliques inverses doubles \\ ou des barres obliques simples \\. Par exemple :

````r

Windows
```r
données <- read.csv("C:\\Users\\file\\Documents\\data.csv") ou 
données <- read.csv("C:/Users/file/Documents/data.csv") 
````

**Pour macOS/Linux :** Les barres obliques simples fonctionnent bien :

```r
macOS/Linux
données <- read.csv("/Users/file/Documents/data.csv")
```

### **Comment lire un fichier CSV et Excel**

```r
#Importer un fichier CSV 
données <- read.csv("C:/Users/file/Documents/data.csv") ou données <- read.csv("C:\\Users\\file\\Documents\\data.csv") ## pour Windows

head(data.csv)
```

Vous pouvez importer un fichier CSV dans R en utilisant un chemin de fichier. Sur les systèmes Windows, les chemins de fichiers peuvent utiliser soit des barres obliques doubles (`//`) soit des barres obliques inverses doubles (`\`). Les données importées sont stockées sous forme de data frame nommé données.

```r
données_excel <- read_excel("C:/Users/file/Documents/HR Data Set.xlsx")
head(données_excel)
```

Vous pouvez importer un fichier Excel dans R en utilisant la fonction `read_excel()` du package `readxl`. La fonction `head()` est ensuite utilisée pour prévisualiser les premières lignes du jeu de données.

Utilisez les commandes suivantes pour comprendre vos données :

```r
str(data.csv)
summary(data.csv)

str(données_excel)
summary(données_excel)
```

`str()` montre la structure du jeu de données, y compris les noms de colonnes et les types de données. `summary()` fournit des statistiques descriptives telles que le minimum, le maximum, la moyenne et les quartiles pour chaque variable. Ensemble, ces fonctions vous aident à comprendre le jeu de données avant l'analyse.

## **Comment visualiser des données avec ggplot2**

La visualisation vous aide à repérer des motifs avant de construire des modèles.

### **Exemple de nuage de points**

Nous utiliserons le jeu de données intégré `mtcars` dans R. Tout d'abord, chargez la bibliothèque pour la rendre disponible pour l'utilisation :

```r
data(mtcars)
library(ggplot2)

ggplot(mtcars, aes(x = wt, y = mpg, color = factor(cyl))) +
  geom_point(size = 3,color="blue") +geom_smooth(method="lm",color="red",se=FALSE)+
  labs(
    title = "Efficacité énergétique par poids et cylindres",
    x = "Poids (1000 lbs)",
    y = "Miles par gallon"
  ) +
  theme_minimal()
```

Décomposons le code pour le comprendre pleinement :

* `data(mtcars)` charge le jeu de données intégré `mtcars`, qui contient des informations sur les spécifications des voitures.
    
* `library(ggplot2)` active la visualisation de données.
    
* `aes()` a été utilisé pour insérer les colonnes de votre jeu de données, qui définit les valeurs `x` et `y`.
    
* `aes()` a été utilisé pour concevoir le graphique à l'extérieur. Par exemple, définir la taille et la couleur des points.
    
* `geom_smooth()` a été utilisé pour ajouter une ligne de tendance. Ici, nous utilisons `method="lm"` pour ajuster une ligne de régression linéaire. L'option `se=TRUE/FALSE` contrôle l'ombrage pour les intervalles de confiance. Utilisez `TRUE` si vous voulez l'ombrage et `FALSE` si vous ne le voulez pas.
    
* `labs()` a été utilisé pour étiqueter le graphique et définir le `title`, les étiquettes de l'axe `x` et de l'axe `y`.
    
* Enfin, nous définissons le thème du graphique en utilisant `theme_minimal()`.
    

L'exécution de ce code produira un nuage de points montrant l'efficacité énergétique par poids et cylindres. Le graphique devrait ressembler à ceci :

![Nuage de points de mpg contre le poids du véhicule avec ligne de régression](https://cdn.hashnode.com/res/hashnode/image/upload/v1765914755069/8921e803-7fa6-4705-802c-23ff8918bee5.png align="center")

## **Comment construire des modèles statistiques dans R**

### **Régression linéaire**

Vous pouvez utiliser la régression linéaire pour des résultats continus, essentiellement pour prédire des valeurs numériques. Par exemple, pour prédire les miles par gallon (`mpg`) d'une voiture en fonction du poids (`wt`) et de la puissance (`hp`), vous pouvez utiliser cette formule :

```r
lm_model <- lm(mpg ~ wt + hp, data = mtcars)
summary(lm_model)
```

Mais que signifie-t-il ?

* `lm()` signifie modèle linéaire.
    
* La variable de réponse est `mpg`. C'est le résultat que vous voulez prédire.
    
* Les variables prédictives sont `wt` et `hp`. Celles-ci expliquent les changements dans la réponse.
    

Une fois que vous exécutez le modèle, il devrait ressembler à ceci dans votre console :

```r
Appel:
lm(formula = mpg ~ wt + hp, data = mtcars)

Résidus:
   Min     1Q Médiane     3Q    Max 
-3.941 -1.600 -0.182  1.050  5.854 

Coefficients:
            Estimation Erreur standard valeur t Pr(>|t|)    
(Intercept) 37.22727    1.59879  23.285  < 2e-16 ***
wt          -3.87783    0.63273  -6.129 1.12e-06 ***
hp          -0.03177    0.00903  -3.519  0.00145 ** 
---
Codes de signification :  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

Erreur standard résiduelle : 2.593 sur 29 degrés de liberté
R-carré multiple :  0.8268,	R-carré ajusté :  0.8148 
Statistique F : 69.21 sur 2 et 29 DF,  valeur p : 9.109e-12
```

Voici une interprétation du modèle de régression linéaire :

* Vous avez créé un modèle sur les miles par gallon (`mpg`) basé sur le poids (`wt`) et la puissance (`hp`).
    
* L'interception `37.227` est le `mpg` lorsque `wt=0` et `hp=0`. En d'autres termes, lorsque toutes les autres variables sont `0`, le `mpg` de base est `37.227`. L'interception est toujours la valeur de base du résultat lorsque toutes les autres variables du modèle sont à zéro.
    
* Avec chaque unité supplémentaire de poids (1000 lbs), le `mpg` diminue de `3.877`. Cette variable affecte grandement le `mpg` comme on peut le voir avec la `valeur p`. La `valeur p` est <0.001, donc forte et statistiquement significative.
    
* Avec chaque unité supplémentaire de puissance, le `mpg` diminue de `0.031`. Cette variable affecte le `mpg`, comme on peut le voir avec la `valeur p` étant `0.00145`, qui est **inférieure à 0.01**, indiquant que la puissance est un prédicteur statistiquement significatif du `mpg`, bien que son effet soit plus petit par rapport au poids du véhicule.
    

### Le modèle correspond-il aux données, et pourquoi ?

La valeur R-carré montre que 83 % de la variation dans `mpg` est expliquée par le poids et la puissance.

**Résumé de l'interprétation** : Les voitures qui sont plus lourdes et avec plus de puissance ont une efficacité énergétique plus faible. Ces deux variables expliquent la plupart de la variation dans `mpg` dans le jeu de données.

### **Régression logistique**

Vous pouvez utiliser la régression logistique pour des résultats binaires, comme des questions oui/non. Par exemple, prédire si un véhicule est automatique ou manuel en fonction du poids et de la puissance.

```r
glm_model <- glm(am ~ wt + hp, data = mtcars, family = binomial)
summary(glm_model)
```

Comprenons le code

* `glm()` signifie modèle linéaire généralisé.
    
* L'option `family=binomial` indique à R d'exécuter une régression logistique.
    
* La variable de réponse `am` indique le type de transmission : 0 = automatique, 1 = manuel.
    
* Les variables prédictives restent `wt` et `hp`.
    

Une fois que vous exécutez le modèle, il devrait ressembler à ceci dans votre console :

```r
Appel:
glm(formula = am ~ wt + hp, family = binomial, data = mtcars)

Coefficients:
            Estimation Erreur standard valeur z Pr(>|z|)   
(Intercept) 18.86630    7.44356   2.535  0.01126 * 
wt          -8.08348    3.06868  -2.634  0.00843 **
hp           0.03626    0.01773   2.044  0.04091 * 
---
Codes de signification :  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

(Paramètre de dispersion pour la famille binomiale pris égal à 1)

    Déviance nulle : 43.230  sur 31  degrés de liberté
Déviance résiduelle : 10.059  sur 29  degrés de liberté
AIC : 16.059

Nombre d'itérations de Fisher Scoring : 8
```

Voici une interprétation du modèle de régression logistique :

* L'interception `18.866` représente les log-odds qu'une voiture soit manuelle lorsque `wt=0` et `hp=0`. En d'autres termes, lorsque toutes les autres variables sont `0`, les log-odds de base du résultat sont `18.866`. L'interception est toujours la valeur de base du résultat lorsque toutes les autres variables du modèle sont à zéro.
    
* Avec chaque unité supplémentaire de poids (1000 lbs), les log odds que la voiture soit manuelle diminuent de `8.083`. Cette variable affecte fortement la probabilité que la voiture soit manuelle, comme on peut le voir avec la `valeur p` étant `0.008`, qui est statistiquement significative.
    
* Avec chaque unité supplémentaire de puissance, les log odds que la voiture soit manuelle augmentent de `0.036`. Cette variable affecte également la probabilité d'être manuelle, comme on peut le voir avec la `valeur p` étant `0.041`, qui est statistiquement significative.
    

**Résumé de l'interprétation** : Les voitures plus lourdes sont plus susceptibles d'être automatiques, tandis qu'une puissance plus élevée augmente légèrement la chance d'être manuelle. Ensemble, `wt` et `hp` expliquent une grande partie de la variation du type de transmission.

## Conclusion

Dans ce tutoriel, vous avez appris à utiliser R pour l'analyse de données, la visualisation et la modélisation statistique, et comment configurer votre environnement R et travailler avec des types de données et des structures de données de base.

Cet article vous a également montré comment importer des jeux de données réels et les explorer en utilisant des statistiques récapitulatives. Cela devrait vous aider à comprendre vos données avant l'analyse.

En utilisant ggplot2, nous avons visualisé les relations et identifié des motifs. Nous avons construit et interprété un modèle de régression linéaire pour prédire l'efficacité énergétique et un modèle de régression logistique pour classer le type de transmission.

Vous avez également appris à interpréter les coefficients, les valeurs p et les mesures de qualité d'ajustement.

Avec ces compétences, vous pouvez charger des jeux de données, visualiser des tendances et construire des modèles prédictifs simples dans R. Continuez à pratiquer avec de nouveaux jeux de données et explorez des techniques plus avancées pour améliorer vos compétences en analyse de données.