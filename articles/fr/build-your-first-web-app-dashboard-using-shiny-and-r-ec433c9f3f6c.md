---
title: Créez votre premier tableau de bord d'application web en utilisant Shiny et
  R
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-22T08:23:35.000Z'
originalURL: https://freecodecamp.org/news/build-your-first-web-app-dashboard-using-shiny-and-r-ec433c9f3f6c
coverImage: https://cdn-media-1.freecodecamp.org/images/0*fzEovljutLXcaBIH.png
tags:
- name: analytics
  slug: analytics
- name: Data Science
  slug: data-science
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Créez votre premier tableau de bord d'application web en utilisant Shiny
  et R
seo_desc: 'By AMR

  One of the beautiful gifts that R has (that Python missed,until dash) is Shiny.
  Shiny is an R package that makes it easy to build interactive web apps straight
  from R. Dashboards are popular since they are good in helping businesses make insig...'
---

Par AMR

L'un des beaux cadeaux que R possède (que Python a manqué, jusqu'à [dash](https://plot.ly/products/dash/)) est [**Shiny**](http://shiny.rstudio.com/). **Shiny** est un package **R** qui facilite la création d'applications web interactives directement à partir de **R**. Les tableaux de bord sont populaires car ils aident les entreprises à tirer des insights des données existantes.

Dans cet article, nous verrons comment utiliser **Shiny** pour créer un tableau de bord simple des revenus de vente. Vous aurez besoin d'avoir [**R installé**](https://cran.r-project.org/).

#### Chargement des packages dans R

Les packages dont vous avez besoin doivent être téléchargés séparément et [installés](https://www.r-bloggers.com/installing-r-packages/) en utilisant **R**. Tous les packages listés ci-dessous peuvent être directement installés depuis CRAN, vous pouvez choisir quel miroir CRAN utiliser. Les dépendances des packages seront également téléchargées et installées par défaut.

Une fois les packages installés, vous devez les charger dans votre session **R**. Les commandes library et require sont utilisées et, encore une fois, les dépendances des packages sont également chargées automatiquement par **R**.

```
# charger les packages requis
library(shiny)
require(shinydashboard)
library(ggplot2)
library(dplyr)
```

#### Fichier d'entrée exemple

Comme un tableau de bord a besoin de données d'entrée à visualiser, nous utiliserons [recommendation.csv](https://raw.githubusercontent.com/amrrs/sample_revenue_dashboard_shiny/master/recommendation.csv) comme exemple de données d'entrée pour notre tableau de bord. Comme il s'agit d'un fichier .csv, la commande read.csv a été utilisée. La première ligne du .csv est une ligne de titre, donc header=T est utilisé. Il y a deux façons d'obtenir le fichier [recommendation.csv](https://raw.githubusercontent.com/amrrs/sample_revenue_dashboard_shiny/master/recommendation.csv) dans votre session R actuelle :

1. Ouvrez ce lien — [recommendation.csv](https://raw.githubusercontent.com/amrrs/sample_revenue_dashboard_shiny/master/recommendation.csv) et **enregistrez**-le (Ctrl+S) dans votre [répertoire de travail actuel](http://stat.ethz.ch/R-manual/R-devel/library/base/html/getwd.html), où ce code R est enregistré. Ensuite, le code suivant fonctionnera parfaitement.

```
recommendation <- read.csv('recommendation.csv',stringsAsFactors = F,header=T)
head(recommendation)
      Account Product Region Revenue
1    Axis Bank     FBB  North    2000
2         HSBC     FBB  South   30000
3          SBI     FBB   East    1000
4        ICICI     FBB   West    1000
5 Bandhan Bank     FBB   West     200
6    Axis Bank    SIMO  North     200
```

2. Au lieu de lire le .csv depuis votre ordinateur local, vous pouvez également le lire depuis une URL (web) en utilisant la même fonction _read.csv_. Comme ce .csv est déjà téléchargé sur mon Github, nous pouvons utiliser ce lien dans notre _read.csv_ pour lire le fichier.

```
recommendation <- read.csv('https://raw.githubusercontent.com/amrrs/sample_revenue_dashboard_shiny/master/recommendation.csv',stringsAsFactors = F,header=T)
head(recommendation)
      Account Product Region Revenue
1    Axis Bank     FBB  North    2000
2         HSBC     FBB  South   30000
3          SBI     FBB   East    1000
4        ICICI     FBB   West    1000
5 Bandhan Bank     FBB   West     200
6    Axis Bank    SIMO  North     200
```

#### Aperçu de Shiny

Chaque application **Shiny** a deux sections principales : **UI** et **Server**. **UI** contient le code pour le front-end comme les boutons, les visuels de graphiques, les onglets, etc. **Server** contient le code pour le back-end comme la récupération de données, la manipulation et le nettoyage.

![Image](https://cdn-media-1.freecodecamp.org/images/tdyv26oYvF-L49m5a0FeaZCaEzZ67gYaiDRR)
_Image Courtesy: [Slideplayer](http://slideplayer.com/slide/9179790/" rel="noopener" target="_blank" title=")_

Au lieu d'utiliser simplement **Shiny**, nous le couplons avec [**shinydashboard**](https://rstudio.github.io/shinydashboard/). **shinydashboard** est un package **R** dont le travail est de faciliter, comme son nom l'indique, la création de tableaux de bord avec **Shiny**.

#### Création d'un tableau de bord peuplé : UI

La partie UI d'une application **Shiny** construite avec **shinydashboard** a 3 éléments de base enveloppés dans la commande dashboardPage(). Le code **Shiny** le plus simple avec **shinydashboard**

```
## app.R ##
library(shiny)
library(shinydashboard)
ui <- dashboardPage(
  dashboardHeader(),
  dashboardSidebar(),
  dashboardBody())
server <- function(input, output) { }
shinyApp(ui, server)
```

donne cette application

![Image](https://cdn-media-1.freecodecamp.org/images/PGHSdjhyNcW0GXSvKfuw4p3gFa6VinXgwfVu)
_Image Courtesy: [rstudio](http://rstudio.github.io/shinydashboard/get_started.html" rel="noopener" target="_blank" title=")_

Peuplons `dashboardHeader()` et `dashboardSidebar()`. Le code contient des commentaires, précédés de #.

```
# En-tête du tableau de bord portant le titre du tableau de bord
header <- dashboardHeader(title = "Tableau de bord de base")
  # Contenu de la barre latérale du tableau de bord
sidebar <- dashboardSidebar(
  sidebarMenu(
    menuItem("Tableau de bord", tabName = "dashboard", icon = icon("dashboard")),
    menuItem("Visitez-nous", icon = icon("send",lib='glyphicon'),
              href = "https://www.salesforce.com")
  ))
```

Les éléments UI que nous souhaitons afficher dans notre tableau de bord peuplent `dashboardPage()`. Puisque l'exemple est un tableau de bord des revenus de vente, affichons trois boîtes d'indicateurs de performance clés (KPI) en haut qui représentent un résumé rapide, suivies de deux box plots pour une vue détaillée.

Pour aligner ces éléments, un par un, nous les définissons à l'intérieur de `fluidRow()`.

```
frow1 <- fluidRow(
  valueBoxOutput("value1")
  ,valueBoxOutput("value2")
  ,valueBoxOutput("value3"))
frow2 <- fluidRow(
   box(
    title = "Revenu par compte"
    ,status = "primary"
    ,solidHeader = TRUE
     ,collapsible = TRUE
     ,plotOutput("revenuebyPrd", height = "300px")
  )
  ,box(
    title = "Revenu par produit"
    ,status = "primary"
    ,solidHeader = TRUE
     ,collapsible = TRUE
     ,plotOutput("revenuebyRegion", height = "300px")
  )
)
# combiner les deux fluid rows pour faire le body
body <- dashboardBody(frow1, frow2)
```

Dans le code ci-dessus, `valueBoxOutput()` est utilisé pour afficher les informations KPI. `valueBoxOutput()` et `plotOutput()` sont écrits dans la partie **Server**, qui est utilisée dans la partie UI pour afficher un graphique. `box()` est une fonction fournie par `shinydashboard` pour enfermer le graphique dans une boîte qui a des fonctionnalités comme `title`, `solidHeader` et `collapsible`. Ayant défini deux fonctions `fluidRow()` individuellement pour des raisons de modularité, nous les combinons toutes les deux dans `dashbboardBody()`.

Ainsi, nous pouvons compléter la partie **UI**, comprenant l'en-tête, la barre latérale et la page, avec le code ci-dessous :

```
# compléter la partie ui avec dashboardPage
ui <- dashboardPage(title = 'Ceci est le titre de ma page', header, sidebar, body, skin='red')
```

La valeur de `title` dans `dashboardPage()` est le titre de la page/onglet du navigateur, tandis que le titre défini dans `dashboardHeader()` est visible comme le titre du tableau de bord.

#### Création d'un tableau de bord peuplé : Server

Avec la partie **UI** terminée, nous allons créer la partie **Server** où le programme et la logique derrière `valueBoxOutput()` et `plotOutput()` sont ajoutés avec `renderValueBox()` et `renderPlot()` respectivement. Ceux-ci sont enfermés dans une `fonction server`, avec `input` et `output` comme ses paramètres. Les valeurs à l'intérieur de `input` sont reçues de **UI** (comme la valeur de `textBox`, la valeur de `Slider`). Les valeurs à l'intérieur de `output` sont envoyées à **UI** (comme `plotOutput`, `valueBoxOutput`).

Voici le code **Server** complet :

```
# créer les fonctions server pour le tableau de bord
server <- function(input, output) {
   # quelques manipulations de données pour dériver les valeurs des boîtes KPI
  total.revenue <- sum(recommendation$Revenue)
  sales.account <- recommendation %>% group_by(Account) %>% summarise(value = sum(Revenue)) %>% filter(value==max(value))
  prof.prod <- recommendation %>% group_by(Product) %>% summarise(value = sum(Revenue)) %>% filter(value==max(value))
# création du contenu valueBoxOutput
  output$value1 <- renderValueBox({
    valueBox(
      formatC(sales.account$value, format="d", big.mark=',')
      ,paste('Top Compte:',sales.account$Account)
      ,icon = icon("stats",lib='glyphicon')
      ,color = "purple")
    })
  output$value2 <- renderValueBox({
     valueBox(
      formatC(total.revenue, format="d", big.mark=',')
      ,'Revenu total attendu'
      ,icon = icon("gbp",lib='glyphicon')
      ,color = "green")
    })
output$value3 <- renderValueBox({
    valueBox(
      formatC(prof.prod$value, format="d", big.mark=',')
      ,paste('Top Produit:',prof.prod$Product)
      ,icon = icon("menu-hamburger",lib='glyphicon')
      ,color = "yellow")
     })
# création du contenu plotOutput
  output$revenuebyPrd <- renderPlot({
    ggplot(data = recommendation,
            aes(x=Product, y=Revenue, fill=factor(Region))) +
       geom_bar(position = "dodge", stat = "identity") +
 ylab("Revenu (en Euros)") +
       xlab("Produit") +
 theme(legend.position="bottom"
                               ,plot.title = element_text(size=15, face="bold")) +
       ggtitle("Revenu par produit") +
 labs(fill = "Région")
  })
output$revenuebyRegion <- renderPlot({
    ggplot(data = recommendation,
            aes(x=Account, y=Revenue, fill=factor(Region))) +
       geom_bar(position = "dodge", stat = "identity") +
 ylab("Revenu (en Euros)") +
       xlab("Compte") +
 theme(legend.position="bottom"
                               ,plot.title = element_text(size=15, face="bold")) +
       ggtitle("Revenu par région") +
 labs(fill = "Région")
  })
}
```

Jusqu'à présent, nous avons défini les deux parties essentielles d'une application **Shiny** — **UI** et **Server**. Enfin, nous devons appeler/exécuter **Shiny**, avec **UI** et **Server** comme ses paramètres.

```
# exécuter/appeler l'application shiny
shinyApp(ui, server)
Listening on http://127.0.0.1:5101
```

L'ensemble du fichier **R** doit être enregistré sous `app.R` dans un dossier **avant** [d'exécuter l'application shiny](https://shiny.rstudio.com/reference/shiny/latest/runApp.html). N'oubliez pas non plus de placer le fichier de données d'entrée (dans notre cas, `recommendation.csv`) dans le même dossier que `app.R`. Bien qu'il existe une autre façon valide de structurer l'application **Shiny** avec deux fichiers `ui.R` et `server.R` (optionnellement, `global.R`), elle a été ignorée dans cet article pour des raisons de brièveté, car cela est destiné aux débutants.

Lors de l'exécution du fichier, l'application web **Shiny** s'ouvrira dans votre navigateur par défaut et ressemblera aux captures d'écran ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/DmJJXakuaZj1lccAZw5Xv0guUmJjqXAScswX)

![Image](https://cdn-media-1.freecodecamp.org/images/69XDs0yXlKj47J6ZtOTUIC4WcKWc92dVHHgE)

Espérons qu'à ce stade, vous avez cette application web **Shiny** exemple en cours d'exécution. Le code et les graphiques utilisés ici sont disponibles sur [mon Github](https://github.com/amrrs/sample_revenue_dashboard_shiny). Si vous êtes intéressé par **Shiny**, vous pouvez en apprendre plus avec le cours [Building Web Applications in R with Shiny Course](https://www.datacamp.com/courses/building-web-applications-in-r-with-shiny?tap_a=5644-dce66f&tap_s=210728-e54afe) de DataCamp.