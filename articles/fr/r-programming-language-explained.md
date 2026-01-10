---
title: Langage de programmation R expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/r-programming-language-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d09740569d1a4ca358a.jpg
tags:
- name: R Programming
  slug: r-programming
- name: toothbrush
  slug: toothbrush
seo_title: Langage de programmation R expliqué
seo_desc: R is an open source programming language and software environment for statistical
  computing and graphics. It is one of the primary languages used by data scientists
  and statisticians alike. It is supported by the R Foundation for Statistical Computin...
---

R est un langage de programmation open source et un environnement logiciel pour le calcul statistique et les graphiques. Il est l'un des principaux langages utilisés par les data scientists et les statisticiens. Il est soutenu par la R Foundation for Statistical Computing et une grande communauté de développeurs open source. Puisque R utilise une interface en ligne de commande, il peut y avoir une courbe d'apprentissage abrupte pour certaines personnes habituées à utiliser des programmes axés sur les interfaces graphiques comme SPSS et SAS, donc des extensions à R comme RStudio peuvent être très bénéfiques. Puisque R est un programme open source et librement disponible, il peut attirer les universitaires dont l'accès aux programmes statistiques est réglementé par leur association à divers collèges ou universités.

## **Installation**

La première chose dont vous avez besoin pour commencer avec R est de le télécharger depuis son [site officiel](https://www.r-project.org/) selon votre système d'exploitation.

## **Outils et packages R populaires**

* [RStudio](https://www.rstudio.com/products/rstudio/) est un environnement de développement intégré (IDE) pour R. Il inclut une console, un éditeur avec coloration syntaxique qui supporte l'exécution directe de code, ainsi que des outils pour le traçage, l'historique, le débogage et la gestion de l'espace de travail.
* [The Comprehensive R Archive Network (CRAN)](https://cran.r-project.org/) est une source majeure pour les outils et ressources R.
* [Tidyverse](https://www.tidyverse.org/) est une collection d'opinions de packages R conçus pour la science des données comme ggplot2, dplyr, readr, tidyr, purr, tibble.
* [data.table](https://github.com/Rdatatable/data.table/wiki) est une implémentation de base `data.frame` axée sur l'amélioration des performances et une syntaxe concise et flexible.
* [Shiny](https://shiny.rstudio.com/) est un framework pour construire des applications web de style tableau de bord en R.

## Types de données en R

### Vecteur

Il s'agit d'une séquence d'éléments de données du même type de base. Par exemple :

```text
> o <- c(1,2,5.3,6,-2,4)                             	 # Vecteur numérique
> p <- c("one","two","three","four","five","six")    	 # Vecteur de caractères
> q <- c(TRUE,TRUE,FALSE,TRUE,FALSE,TRUE)                # Vecteur logique
> o;p;q
[1]  1.0  2.0  5.3  6.0 -2.0  4.0
[1] "one"   "two"   "three" "four"  "five"  "six"
[1]  TRUE  TRUE FALSE  TRUE FALSE
```

### Matrice

Il s'agit d'un ensemble de données rectangulaire à deux dimensions. Les composants d'une matrice doivent également être du même type de base comme un vecteur. Par exemple :

```text
> m = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
> m
>[,1] [,2] [,3]
[1,] "a"  "a"  "b" 
[2,] "c"  "b"  "a"
```

### Data Frame

Il est plus général qu'une matrice, dans le sens où différentes colonnes peuvent avoir différents types de données de base. Par exemple :

```text
> d <- c(1,2,3,4)
> e <- c("red", "white", "red", NA)
> f <- c(TRUE,TRUE,TRUE,FALSE)
> mydata <- data.frame(d,e,f)
> names(mydata) <- c("ID","Color","Passed")
> mydata
```

### Listes

Il s'agit d'un objet R qui peut contenir de nombreux types d'éléments différents à l'intérieur, comme des vecteurs, des fonctions et même une autre liste à l'intérieur. Par exemple :

```text
> list1 <- list(c(2,5,3),21.3,sin)
> list1
[[1]]
[1] 2 5 3
[[2]]
[1] 21.3
[[3]]
function (x)  .Primitive("sin")
```

## Fonctions en R

Une fonction vous permet de définir un bloc de code réutilisable qui peut être exécuté plusieurs fois dans votre programme.

Les fonctions peuvent être nommées et appelées à plusieurs reprises ou peuvent être exécutées anonymement en place (similaire aux fonctions lambda en Python).

Développer une compréhension complète des fonctions R nécessite de comprendre les environnements. Les environnements sont simplement un moyen de gérer les objets. Un exemple d'environnements en action est que vous pouvez utiliser un nom de variable redondant dans une fonction, qui ne sera pas affecté si l'environnement d'exécution plus large a déjà la même variable. De plus, si une fonction appelle une variable non définie dans la fonction, elle vérifiera l'environnement de niveau supérieur pour cette variable.

### **Syntaxe**

En R, une définition de fonction a les caractéristiques suivantes :

1. Le mot-clé `function`
2. un nom de fonction
3. des paramètres d'entrée (optionnels)
4. un bloc de code à exécuter
5. une instruction de retour (optionnelle)

```text
# une fonction sans paramètres ni valeurs retournées
direBonjour() = function(){
  "Bonjour !"
}

direBonjour()  # appelle la fonction, 'Bonjour !' est affiché dans la console

# une fonction avec un paramètre
bonjourAvecNom = function(nom){
  paste0("Bonjour, ", nom, "!")
}

bonjourAvecNom("Ada")  # appelle la fonction, 'Bonjour, Ada !' est affiché dans la console

# une fonction avec plusieurs paramètres avec une instruction de retour
multiplier = function(val1, val2){
  val1 * val2
}
  
multiplier(3, 5)  # affiche 15 dans la console
```

Les fonctions sont des blocs de code qui peuvent être réutilisés simplement en appelant la fonction. Cela permet une réutilisation de code simple et élégante sans réécrire explicitement des sections de code. Cela rend le code à la fois plus lisible, facilite le débogage et limite les erreurs de frappe.

Les fonctions en R sont créées en utilisant le mot-clé `function`, ainsi qu'un nom de fonction et des paramètres de fonction entre parenthèses.

La fonction `return()` peut être utilisée par la fonction pour retourner une valeur, et est généralement utilisée pour forcer la terminaison anticipée d'une fonction avec une valeur retournée. Alternativement, la fonction retournera la dernière valeur imprimée.

```text
# retourner une valeur explicitement ou simplement en l'imprimant
somme = function(a, b){
  c = a + b
  return(c)
}

somme = function(a, b){
  a + b
}


resultat = somme(1, 2)
# resultat = 3
```

Vous pouvez également définir des valeurs par défaut pour les paramètres, que R utilisera lorsqu'une variable n'est pas spécifiée lors de l'appel de la fonction.

```text
somme = function(a, b = 3){
  a + b
}

resultat = somme(a = 1)
# resultat = 4
```

Vous pouvez également passer les paramètres dans l'ordre que vous souhaitez, en utilisant le nom du paramètre.

```text
resultat = somme(b=2, a=2)
# resultat = 4
```

R peut également accepter des paramètres supplémentaires et optionnels avec '...'

```text
somme = function(a, b, ...){
  a + b + ...
}

somme(1, 2, 3) # retourne 6
```

Les fonctions peuvent également être exécutées anonymement. Celles-ci sont très utiles en combinaison avec la famille de fonctions 'apply'.

```text
# boucler à travers 1, 2, 3 - ajouter 1 à chaque
sapply(1:3,
       function(i){
         i + 1
         })
```

### **Notes**

Si une définition de fonction inclut des arguments sans valeurs par défaut spécifiées, des valeurs pour ces arguments doivent être incluses.

```text
somme = function(a, b = 3){
a + b
}

somme(b = 2) # Erreur dans somme(b = 2) : argument "a" est manquant, sans valeur par défaut
```

Les variables définies dans une fonction n'existent que dans le cadre de cette fonction, mais vérifieront l'environnement plus large si la variable n'est pas spécifiée

```text
double = function(a){
a * 2
}

double(x)  # Erreur dans double(x) : objet 'x' non trouvé


double = function(){
a * 2
}

a = 3
double() # 6
```

### Fonctions intégrées en R

* R vient avec de nombreuses fonctions que vous pouvez utiliser pour effectuer des tâches sophistiquées comme l'échantillonnage aléatoire.
* Par exemple, vous pouvez arrondir un nombre avec `round()`, ou calculer sa factorielle avec `factorial()`.

```r
> round(4.147)
[1] 4
> factorial(3)
[1] 6
> round(mean(1:6))
[1] 4
```

* Les données que vous passez à la fonction sont appelées les arguments de la fonction.
* Vous pouvez simuler un lancer de dé avec la fonction `sample()` de R. La fonction `sample()` prend deux arguments : un vecteur nommé x et un nombre nommé size. Par exemple :

```r
> sample(x = 1:4, size = 2)
[] 4 2
> sample(x = die, size = 1)
[] 3
>dice <- sample(die, size = 2, replace = TRUE)
>dice
[1] 2 4
>sum(dice)
[1] 6
```

* Si vous n'êtes pas sûr des noms à utiliser avec une fonction, vous pouvez rechercher les arguments de la fonction avec args.

```r
> args(round)
[1] function(x, digits=0)
```

## **Objets en R**

R permet de sauvegarder les données en les stockant à l'intérieur d'un objet R.

### Qu'est-ce qu'un objet ?

C'est simplement un nom que vous pouvez utiliser pour appeler des données stockées. Par exemple, vous pouvez sauvegarder des données dans un objet comme a ou b.

```r
> a <- 5
> a
[1] 5
```

### Comment créer un objet en R ?

1. Pour créer un objet R, choisissez un nom puis utilisez le symbole inférieur à, `<`, suivi d'un signe moins, `-`, pour sauvegarder des données dedans. Cette combinaison ressemble à une flèche, `<-`. R créera un objet, lui donnera votre nom et y stockera ce qui suit la flèche.
2. Lorsque vous demandez à R ce qu'il y a dans a, il vous le dit à la ligne suivante. Par exemple :

```r
> die <- 1:6
> die
[1] 1 2 3 4 5 6
```

1. Vous pouvez nommer un objet en R presque comme vous le souhaitez, mais il y a quelques règles. Premièrement, un nom ne peut pas commencer par un nombre. Deuxièmement, un nom ne peut pas utiliser certains symboles spéciaux, comme `^, !, $, @, +, -, /, ou *`:
2. R comprend également la casse (ou est sensible à la casse), donc name et Name feront référence à des objets différents.
3. Vous pouvez voir quels noms d'objets vous avez déjà utilisés avec la fonction `ls()`.

## Plus d'informations :

* [Apprenez les bases du langage de programmation R en seulement 2 heures avec ce cours gratuit sur la programmation statistique](https://www.freecodecamp.org/news/r-programming-course/)
* [Une introduction au web scraping en utilisant R](https://www.freecodecamp.org/news/an-introduction-to-web-scraping-using-r-40284110c848/)
* [Une introduction aux agrégats en R : un outil puissant pour jouer avec les données](https://www.freecodecamp.org/news/aggregates-in-r-one-of-the-most-powerful-tool-you-can-ask-for-4dd14eafff1f/)