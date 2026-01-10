---
title: Comment modéliser une épidémie avec R
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T14:46:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-model-an-epidemic-with-r
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/PIXNIO-39014-1200x877.jpg
tags:
- name: data analysis
  slug: data-analysis
- name: Data Science
  slug: data-science
- name: R Programming
  slug: r-programming
seo_title: Comment modéliser une épidémie avec R
seo_desc: 'By Peter Gleeson

  Epidemiology has never been more topical. It is the scientific study of how health
  and disease affects populations, including infectious diseases such as COVID-19.

  Key to understanding the spread of such diseases is the practice of e...'
---

Par Peter Gleeson

L'épidémiologie n'a jamais été aussi d'actualité. Il s'agit de l'étude scientifique de la manière dont la santé et les maladies affectent les populations, y compris les maladies infectieuses telles que le COVID-19.

La clé pour comprendre la propagation de telles maladies est la pratique de la modélisation épidémique. Cela implique la construction de modèles quantitatifs pour décrire et prévoir la propagation des maladies.

L'approche classique de la modélisation épidémique consiste à utiliser un type de modèle mathématique connu sous le nom de "modèle compartimental".

L'approche est la suivante :

1. Assigner chaque individu de la population à l'un des plusieurs compartiments, en fonction de leur statut d'infection.
2. Ensuite, définir les taux auxquels les individus passent d'un compartiment à un autre à mesure que leur statut est mis à jour.
3. Utiliser ce modèle pour définir des équations différentielles qui peuvent prédire le cours de l'épidémie.

Le modèle SI est la forme la plus basique de modèle compartimental. Il comporte deux compartiments : "susceptible" et "infectieux".

![Deux compartiments, l'un étiqueté S, l'autre I. Une flèche va de S à I.](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-30-at-01.21.00.png)

Le modèle SIR ajoute un compartiment supplémentaire appelé "rétabli". Ce modèle est souvent utilisé comme référence en épidémiologie. Il s'agit d'un modèle simpliste qui caractérise néanmoins raisonnablement bien la progression d'une épidémie.

![Trois compartiments, étiquetés S, I et R. Des flèches vont de S à I et de I à R.](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-30-at-01.23.52.png)

Une extension du modèle SIR (et celle que nous allons considérer plus en détail dans cet article) est le modèle SEIR. Celui-ci ajoute un compartiment supplémentaire – "exposé".

## Qu'est-ce que le modèle SEIR ?

Le modèle SEIR de base comporte quatre compartiments :

![Quatre compartiments. S coule vers E, E coule vers I, I coule vers R. Les trois flèches sont étiquetées bêta, sigma et gamma respectivement.](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-30-at-01.29.52.png)

* "Susceptible" – individus qui n'ont pas été exposés au virus
* "Exposé" – individus exposés au virus, mais pas encore infectieux
* "Infectieux" – individus exposés qui deviennent infectieux
* "Rétabli" – individus infectieux qui se rétablissent et deviennent immunisés contre le virus

La taille de la population N est prise comme la somme des individus dans les quatre compartiments.

Le flux d'individus entre les compartiments est caractérisé par un certain nombre de paramètres.

**β - "bêta"**

β est le coefficient de transmission. Considérez cela comme le nombre moyen de contacts infectieux qu'un individu infectieux dans la population établit à chaque période de temps. Une valeur élevée de β signifie que le virus a plus d'opportunités de se propager.

**σ - "sigma"**

σ est le taux auquel les individus exposés deviennent infectieux. Considérez-le comme l'inverse du temps moyen qu'il faut pour devenir infectieux. C'est-à-dire, si un individu devient infectieux après 4 jours en moyenne, σ sera 1/4 (ou 0,25).

**γ - "gamma"**

γ est le taux auquel les individus infectieux se rétablissent. Comme avant, considérez-le comme l'inverse du temps moyen qu'il faut pour se rétablir. C'est-à-dire, si cela prend 10 jours en moyenne pour se rétablir, γ sera 1/10 (ou 0,1).

**μ - "mu"**

μ est un paramètre optionnel pour décrire le taux de mortalité des individus infectieux. Plus μ est élevé, plus le virus est mortel.

À partir de ces paramètres, vous pouvez construire un ensemble d'équations différentielles. Celles-ci décrivent le taux auquel chaque compartiment change de taille.

Commençons par le compartiment "susceptible", S.

### Équation (1) - Susceptible

La première chose à voir à partir du modèle est qu'il n'y a aucun moyen pour S d'augmenter avec le temps. Il n'y a pas de flux de retour dans le compartiment. L'équation (1) doit être négative, car S ne peut que diminuer.

De quelles manières un individu peut-il quitter le compartiment S ?

Eh bien, il peut être infecté par un individu infectieux dans la population.

À tout moment, la proportion d'individus infectieux dans la population = I/N.

Et la proportion d'individus susceptibles sera S/N.

Sous l'hypothèse de mélange parfait (c'est-à-dire, les individus ont la même probabilité d'entrer en contact avec n'importe quel autre individu de la population), la probabilité qu'un contact donné soit entre un individu infectieux et un individu susceptible est (I / N) * (S / N).

Cela est multiplié par le nombre de contacts dans la population. Cela est trouvé en multipliant le coefficient de transmission β par la taille de la population N.

En combinant tout cela et en simplifiant, on obtient l'équation (1) :

![delta S égale moins bêta fois S fois I tout sur N](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-29-at-21.42.45.png)

### Équation (2) - Exposé

Ensuite, considérons le compartiment "exposé", E. Les individus peuvent entrer et sortir de ce compartiment.

Le flux entrant dans E sera égal au flux sortant de S. Ainsi, la première partie de l'équation suivante sera simplement l'opposé du terme précédent.

Les individus peuvent quitter E en passant dans le compartiment infectieux. Cela se produit à un taux déterminé par deux variables – le taux σ et le nombre actuel d'individus dans E.

Ainsi, l'équation (2) globale est :

![deltaEI égale bêta fois S fois I tout sur N, moins sigma fois I](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-04-at-21.12.56-1.png)

### Équation (3) - Infectieux

Le compartiment suivant à considérer est le compartiment "infectieux", I.

Il y a une manière d'entrer dans ce compartiment, qui est depuis le compartiment "exposé".

Il y a deux manières pour un individu de quitter le compartiment "infectieux".

Certains passeront à "rétabli". Cela se produit à un taux γ.

D'autres ne survivront pas à l'infection. Ils peuvent être modélisés en utilisant le taux de mortalité μ.

Ainsi, l'équation (3) ressemble à ceci :

![delta I égale sigma fois E moins gamma fois I moins mu fois I](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-29-at-21.53.27.png)

### Équation (4) - Rétabli

Maintenant, regardons le compartiment "rétabli", R.

Cette fois, les individus peuvent entrer dans le compartiment (déterminé par le taux γ).

Et aucun individu ne peut sortir du compartiment (bien que dans certains modèles, il soit supposé possible de revenir dans le compartiment "susceptible").

Ainsi, l'équation (4) globale ressemble à ceci :

![delta R égale gamma fois I](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-29-at-22.00.50.png)

### Équation (5) - Mortalité (optionnel)

En utilisant un raisonnement similaire, vous pourriez également construire l'équation (5) pour le changement de mortalité. Vous pourriez considérer cela comme un cinquième compartiment dans le modèle.

Si vous définissez μ à zéro, vous pouvez exclure cet aspect du modèle.

![delta M égale mu fois I](https://www.freecodecamp.org/news/content/images/2020/03/Screenshot-2020-03-29-at-22.00.13.png)

Ainsi, vous avez maintenant l'ensemble complet des équations différentielles (1-5).

![Image](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-04-at-21.15.12.png)

Un nombre important dans tout modèle épidémique est connu sous le nom de nombre de reproduction de base, ou R₀. Celui-ci est défini comme :

![R zéro égale bêta sur gamma](https://www.freecodecamp.org/news/content/images/2020/10/Screenshot-2020-10-03-at-21.02.11.png)

Ce nombre estime le nombre de personnes qui seront infectées par un individu infectieux moyen.

Par conséquent, il s'agit d'un nombre crucial :

* Si R₀ est supérieur à 1, alors une épidémie du virus est susceptible de devenir une épidémie
* Si R₀ est inférieur à 1, alors une épidémie est susceptible d'être contenue

### Comment résoudre ces équations

Afin d'utiliser le modèle pour prédire le cours de l'épidémie, il est nécessaire de résoudre le système d'équations.

Cela peut être fait en utilisant le [langage de programmation R](https://www.r-project.org/).

En particulier, vous pouvez utiliser un package appelé [deSolve](https://www.rdocumentation.org/packages/deSolve/versions/1.27.1) pour résoudre les équations différentielles par rapport à une variable de temps.

Dans R, collez le code suivant :

```r
require(deSolve)

SEIR <- function(time, current_state, params){
  
  with(as.list(c(current_state, params)),{
    N <- S+E+I+R
    dS <- -(beta*S*I)/N
    dE <- (beta*S*I)/N - sigma*E
    dI <- sigma*E - gamma*I - mu*I
    dR <- gamma*I
    dM <- mu*I
    
    return(list(c(dS, dE, dI, dR, dM)))
  })
}
```

Ce code importe le package deSolve.

Il définit ensuite une fonction appelée `SEIR`. Elle prend trois arguments :

* L'étape de temps actuelle.
* Une liste des états actuels du système (c'est-à-dire, les estimations pour chacun de S, E, I et R à l'étape de temps actuelle).
* Une liste de paramètres utilisés dans les équations (rappelons que ce sont β, σ, γ et μ).

À l'intérieur du corps de la fonction, vous définissez le système d'équations différentielles comme décrit ci-dessus. Celles-ci sont évaluées pour l'étape de temps donnée et sont retournées sous forme de liste. L'ordre dans lequel elles sont retournées doit correspondre à l'ordre dans lequel vous fournissez les états actuels.

Maintenant, regardez le code ci-dessous :

```r
params <- c(beta=0.5, sigma=0.25, gamma=0.2, mu=0.001)

initial_state <- c(S=999999, E=1, I=0, R=0, M=0)

times <- 0:365
```

Cela initialise les paramètres et l'état initial (conditions de départ) pour le modèle.

Il génère également un vecteur de temps de zéro à 365 jours.

Maintenant, créez le modèle :

```r
model <- ode(initial_state, times, SEIR, params)
```

Cela utilise la fonction `ode()` de deSolve pour résoudre les équations par rapport au temps.

Voir [ici](https://www.rdocumentation.org/packages/deSolve/versions/1.27.1/topics/ode) pour la documentation.

Les arguments requis sont :

* L'état initial pour chacun des compartiments
* Le vecteur de temps (cet exemple résout pour jusqu'à 365 jours)
* La fonction `SEIR()`, qui définit le système d'équations
* Un vecteur de paramètres à passer à la fonction `SEIR()`

Exécuter :

```r
summary(model)
```

...donnera les statistiques de résumé du modèle.

```
               S            E            I         R         M
Min.    108263.6 3.616607e-07 0.000000e+00      0.00    0.0000
1st Qu. 108263.7 5.957435e-03 1.414971e-02  63894.43  319.4721
Median  108395.7 8.470071e+00 1.273726e+01 886814.36 4434.0718
Mean    362798.6 9.745754e+03 1.212158e+04 612272.74 3061.3637
3rd Qu. 852375.5 1.734331e+03 2.533956e+03 887299.83 4436.4991
Max.    999999.0 1.092967e+05 1.265161e+05 887299.86 4436.4993
N          366.0 3.660000e+02 3.660000e+02    366.00  366.0000
sd      381257.2 2.475783e+04 2.969234e+04 387333.47 1936.6673
```

Déjà, vous trouverez quelques informations intéressantes.

* Sur un million d'individus, 108 264 n'ont pas été infectés.
* Au pic de l'épidémie, 126 516 individus étaient infectieux simultanément.
* 887 300 individus se sont rétablis à la fin du modèle.
* Un total de 4 436 individus sont morts pendant l'épidémie.

Vous pouvez également visualiser l'évolution de la pandémie en utilisant la fonction `matplot()`.

Alternativement, vous pourriez utiliser une autre bibliothèque de traçage telle que [ggplot2](https://ggplot2.tidyverse.org/index.html) pour produire des graphiques de meilleure qualité.

```r
matplot(model, type="l", lty=1, main="Modèle SEIR", xlab="Temps")

legend <- colnames(model)[2:6]

legend("right", legend=legend, col=2:6, lty = 1)
```

Le graphique est montré ci-dessous :

![Graphique montrant des courbes qui représentent comment la taille de chaque compartiment change au fil du temps. S décline en une courbe en forme de S, R et M augmentent en courbes en forme de S. I et E culminent après le jour 100 avant de décliner à zéro](https://www.freecodecamp.org/news/content/images/2020/10/seir_model.png)

Vous pouvez également forcer la sortie du modèle à un type de dataframe. Ensuite, vous pouvez analyser davantage le modèle.

```r
infections <- as.data.frame(model)$I

peak <- max(infections)

match(peak, infections)
```

Le code ci-dessus révèle que le nombre d'infections a culminé au jour 112.

L'utilisation d'autres bibliothèques, telles que dplyr, vous permettrait de réaliser des analyses aussi avancées que vous le souhaitez.

## Comment modéliser les méthodes d'intervention

Le modèle SEIR est un exemple intéressant de la manière dont une épidémie se développe sans aucun changement dans le comportement de la population.

Vous pouvez construire des modèles plus sophistiqués en prenant le modèle SEIR comme point de départ et en ajoutant des fonctionnalités supplémentaires.

Cela vous permet de modéliser les changements de comportement (soit volontaires, soit résultant d'une intervention gouvernementale).

De nombreux (mais pas tous) pays du monde sont entrés dans une forme de "confinement" pendant la pandémie de coronavirus de 2020.

En fin de compte, l'intention du confinement est de modifier le cours de l'épidémie en réduisant le coefficient de transmission, β.

Le code ci-dessous définit un modèle qui change la valeur de β entre le début et la fin d'une période de confinement.

**Tous les nombres utilisés sont purement illustratifs**. Vous pourriez faire une carrière de recherche entière (plusieurs fois) en essayant de déterminer les valeurs les plus réalistes.

```r
SEIR_lockdown <- function(time, current_state, params){
  
    with(as.list(c(current_state, params)),{
      
      beta = ifelse(
        (time <= start_lockdown || time >= end_lockdown),
        0.5, 0.1
        )
      
      N <- S+E+I+R
      dS <- -(beta*S*I)/N
      dE <- (beta*S*I)/N - sigma*E
      dI <- sigma*E - gamma*I - mu*I
      dR <- gamma*I
      dM <- mu*I
      
      return(list(c(dS, dE, dI, dR, dM)))
    })
  }
```

Le seul changement est l'instruction `ifelse()` supplémentaire pour ajuster la valeur de β à 0,1 pendant le confinement.

Vous devez passer deux nouveaux paramètres au modèle. Ce sont les heures de début et de fin de la période de confinement.

Ici, le confinement commence au jour 90 et se termine au jour 150.

```r
params <- c(
    sigma=0.25,
    gamma=0.2,
    mu=0.001,
    start_lockdown=90,
    end_lockdown=150
    )
  
  initial_state <- c(S=999999, E=1, I=0, R=0, M=0)
  
  times <- 0:365
  
  model <- ode(initial_state, times, SEIR_lockdown, params)
```

Maintenant, vous pouvez voir le résumé et les graphiques associés à ce modèle.

```r
summary(model)
```

Cela révélera :

```
               S            E           I         R         M
Min.    156885.7 7.699207e-01     0.00000      0.00    0.0000
1st Qu. 160478.2 6.929205e+01    97.71405  63668.75  318.3438
Median  789214.4 1.246389e+03  1735.66330 194379.16  971.8958
Mean    589558.9 9.216918e+03 11460.62036 387824.44 1939.1222
3rd Qu. 867639.6 1.030043e+04 13780.17591 829898.56 4149.4928
Max.    999999.0 6.083432e+04 72443.97892 838916.89 4194.5845
N          366.0 3.660000e+02   366.00000    366.00  366.0000
sd      350719.3 1.570278e+04 18893.31145 346542.57 1732.7128
```

Vous pouvez voir :

* Sur un million d'individus, 156 886 n'ont pas été infectés.
* Au pic de l'épidémie, 72 444 individus étaient infectieux simultanément.
* 838 917 individus se sont rétablis à la fin du modèle.
* Un total de 4 195 individus sont morts pendant l'épidémie.

Le traçage du modèle en utilisant `matplot()` révèle un fort effet de "deuxième vague" (comme cela a été observé dans de nombreux pays d'Europe vers la fin de 2020).

```r
  matplot(
    model, 
    type="l",
    lty=1, 
    main="Modèle SEIR (avec intervention)", 
    xlab="Temps"
    )
    
legend <- colnames(model)[2:6]

legend("right", legend=legend, col=2:6, lty = 1)
```

![Graphique montrant des courbes qui représentent comment la taille de chaque compartiment change au fil du temps. S décline rapidement, avant de se stabiliser pendant le confinement, puis décline rapidement à nouveau, R et M augmentent rapidement avant de se stabiliser, puis augmentent rapidement à nouveau. I et E montrent un petit pic avant le jour 100, puis déclinent, avant de culminer à nouveau après le jour 200](https://www.freecodecamp.org/news/content/images/2020/10/seir_intervention.png)

Enfin, vous pouvez forcer le modèle à un dataframe et réaliser une analyse plus détaillée à partir de là.

```r
infections <- as.data.frame(model)$I

peak <- max(infections)

match(peak, infections)
```

Dans ce scénario, le nombre d'infections a culminé au jour 223.

Dans d'autres scénarios, vous pourriez modéliser l'effet de la vaccination. Ou, vous pourriez intégrer des différences saisonnières dans le taux de transmission.

## Limites des modèles compartimentaux

Comme pour toute modélisation, un modèle épidémique n'est aussi bon que les données et les hypothèses qui y sont intégrées.

Et certaines des hypothèses derrière le modèle SEIR tel que décrit sont irréalistes.

Par exemple :

* Dans les grandes populations, le mélange est non uniforme. Les individus sont beaucoup plus susceptibles d'interagir avec des individus de leur localité. Des modèles compartimentaux plus avancés tiendront compte de cela.
* Le modèle suppose que la population est isolée. En réalité, le mélange entre les populations permet à un virus d'être introduit et réintroduit plusieurs fois.
* Les individus ne naissent généralement pas avec une immunité. Des modèles plus sophistiqués tiendront compte du taux de natalité lors de la considération de périodes plus longues.
* Le modèle SEIR de base ne tient pas compte des structures d'âge dans la population. Souvent, un virus se propagera plus rapidement parmi les jeunes, les villes densément peuplées. Mais il pourrait s'avérer plus mortel pour les populations plus âgées en dehors de ces villes. Des modèles plus complexes tiendront compte de ces différences.
* Le modèle SEIR ne considère que les moyennes pour chacun de ses paramètres. En réalité, il y aura beaucoup de variation. Certains individus restent infectieux pendant une longue période. Un petit nombre d'individus pourrait faire un très grand nombre de contacts. Par conséquent, le modèle est adapté pour décrire l'épidémie à un niveau élevé, sur une longue période de temps. Mais il n'est pas adapté pour prédire les détails à une échelle plus petite.

Malgré ses limites, le modèle SEIR est un bon point de départ pour comprendre la dynamique d'une épidémie.

Plus généralement, l'approche consistant à utiliser des équations différentielles pour représenter les flux entre les compartiments afin de modéliser des processus complexes est très puissante.

Et la disponibilité de packages logiciels pour des langages tels que R et Python rend plus facile que jamais de commencer à explorer ces techniques.

Vous pouvez approfondir le code utilisé pour les exemples [ici](https://github.com/pg0408/seir).

Merci d'avoir lu !